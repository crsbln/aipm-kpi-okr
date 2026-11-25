"""Generate MOCK pilot data for the Imageboost dashboard prototype.

    uv run python dashboard/make_mock_data.py      (standard library only)

Writes dashboard/data.js. Every number in that file is simulated from the
made-up settings below. Nothing here is a real ImmoScout24 measurement.
The seed is fixed, so the same numbers come out on every run.

Mock pilot design (see governance-and-review-cadence.md):
  weeks 1-2  baseline phase, every search uses random allocation
  weeks 3-8  test phase, each search is split 50/50 between
             "random"   (one agent drawn from all agents) and
             "matching" (one agent drawn from the searched district)
"""
import json
import random
from pathlib import Path

SEED = 21
WEEKS = 8
BASELINE_WEEKS = 2

# --- made-up settings (assumptions, not facts) -------------------------------
# The 12 Berlin boroughs are real; the shares and agent counts are invented.
DISTRICTS = [
    # name, share of searches, participating agents
    ("Mitte", 0.16, 14),
    ("Friedrichshain-Kreuzberg", 0.14, 12),
    ("Pankow", 0.13, 13),
    ("Charlottenburg-Wilmersdorf", 0.12, 16),
    ("Spandau", 0.05, 7),
    ("Steglitz-Zehlendorf", 0.07, 11),
    ("Tempelhof-Schoeneberg", 0.09, 10),
    ("Neukoelln", 0.08, 8),
    ("Treptow-Koepenick", 0.05, 8),
    ("Marzahn-Hellersdorf", 0.03, 6),
    ("Lichtenberg", 0.05, 8),
    ("Reinickendorf", 0.03, 7),
]
FIRST_WEEK_IMPRESSIONS = 60_000
WEEKLY_TRAFFIC_GROWTH = 0.06     # traffic grows, behaviour does not
P_EXCLUDED = 0.03                # internal, test and bot traffic
P_VIEW = {True: 0.035, False: 0.02}      # profile view, by "agent is relevant"
P_CLICK = {True: 0.18, False: 0.12}      # contact click after a view
P_SUBMIT = 0.60                          # lead sent after a click
P_FLAGGED = 0.10                         # lead flagged as duplicate or spam
P_REVIEWED = 0.90                        # flag looked at by a reviewer
P_OVERTURNED = 0.30                      # reviewer says the flag was wrong
P_LABELLED = 0.70                        # agent labels the lead within 7 days
P_USEFUL = {True: 0.60, False: 0.25}     # label says "useful"
P_COMPLAINT = 0.00004                    # consumer complaint per impression

# --- mock thresholds, only so the prototype can show a status ----------------
MOCK = {
    "uplift_target": 0.15,        # K1: matching arm vs random arm
    "breadth_min": 0.80,          # M12: agents with 1+ qualified lead
    "relevance_min": 0.50,        # K3
    "override_band": [0.05, 0.20],  # K4 healthy range
    "review_coverage_min": 0.80,  # G3
    "complaint_max_per_10k": 1.0,  # K5
    "top10_max": 0.20,            # G1
    "invalid_max": 0.10,          # G2
}

KEYS = ["raw", "excluded", "impressions", "relevant", "views", "clicks",
        "leads", "flagged", "reviewed", "overturned", "invalid", "labelled",
        "qualified", "complaints"]
ARMS = ["random", "matching"]


def simulate():
    rng = random.Random(SEED)
    weights = [d[1] for d in DISTRICTS]
    agent_district = [i for i, d in enumerate(DISTRICTS) for _ in range(d[2])]
    by_district = {}
    for agent, dist in enumerate(agent_district):
        by_district.setdefault(dist, []).append(agent)
    n = len(agent_district)
    exposure = {a: [0] * n for a in ARMS}       # test phase only
    qualified = {a: [0] * n for a in ARMS}
    weeks = []
    for w in range(WEEKS):
        row = {a: dict.fromkeys(KEYS, 0) for a in ARMS}
        test = w >= BASELINE_WEEKS
        raw = round(FIRST_WEEK_IMPRESSIONS * (1 + WEEKLY_TRAFFIC_GROWTH) ** w)
        for _ in range(raw):
            arm = rng.choice(ARMS) if test else "random"
            c = row[arm]
            c["raw"] += 1
            if rng.random() < P_EXCLUDED:
                c["excluded"] += 1
                continue
            c["impressions"] += 1
            district = rng.choices(range(len(DISTRICTS)), weights)[0]
            if arm == "matching":
                agent = rng.choice(by_district[district])
            else:
                agent = rng.randrange(n)
            if test:
                exposure[arm][agent] += 1
            rel = agent_district[agent] == district
            c["relevant"] += rel
            if rng.random() < P_COMPLAINT:
                c["complaints"] += 1
            if rng.random() >= P_VIEW[rel]:
                continue
            c["views"] += 1
            if rng.random() >= P_CLICK[rel]:
                continue
            c["clicks"] += 1
            if rng.random() >= P_SUBMIT:
                continue
            c["leads"] += 1
            if rng.random() < P_FLAGGED:
                c["flagged"] += 1
                if rng.random() < P_REVIEWED:
                    c["reviewed"] += 1
                    if rng.random() < P_OVERTURNED:
                        c["overturned"] += 1
                    else:
                        c["invalid"] += 1
                        continue
            if rng.random() < P_LABELLED:
                c["labelled"] += 1
                if rng.random() < P_USEFUL[rel]:
                    c["qualified"] += 1
                    if test:
                        qualified[arm][agent] += 1
        weeks.append({"week": w + 1, "phase": "test" if test else "baseline",
                      **row})
    return weeks, exposure, qualified, n


def div(a, b):
    return a / b if b else None


def build():
    weeks, exposure, qualified, n = simulate()

    def total(rows, arms=ARMS):
        return {k: sum(r[a][k] for r in rows for a in arms) for k in KEYS}

    base = total(weeks[:BASELINE_WEEKS])
    test = {a: total(weeks[BASELINE_WEEKS:], [a]) for a in ARMS}
    whole = total(weeks)
    top_n = max(1, round(n * 0.10))

    def top10(arm):
        e = sorted(exposure[arm], reverse=True)
        return sum(e[:top_n]) / sum(e)

    def conv(t):
        return div(t["qualified"], t["impressions"])

    def per10k(t):
        return div(t["complaints"], t["impressions"]) * 10_000

    weekly = []
    for r in weeks:
        both = total([r])
        weekly.append({
            "week": r["week"], "phase": r["phase"],
            "impressions": both["impressions"],
            "complaints": both["complaints"],
            "complaints_per_10k": per10k(both),
            "conv_random": conv(r["random"]),
            "conv_matching": conv(r["matching"]),
            "rel_random": div(r["random"]["relevant"], r["random"]["impressions"]),
            "rel_matching": div(r["matching"]["relevant"], r["matching"]["impressions"]),
            "random": r["random"], "matching": r["matching"],
        })

    # like-for-like trap: random arm, weeks 7-8 against weeks 3-4
    early, late = total(weeks[2:4], ["random"]), total(weeks[6:8], ["random"])
    trap = {
        "impressions": late["impressions"] / early["impressions"] - 1,
        "qualified_count": late["qualified"] / early["qualified"] - 1,
        "qualified_rate": conv(late) / conv(early) - 1,
        "early_qualified": early["qualified"],
        "late_qualified": late["qualified"],
    }

    uplift = conv(test["matching"]) / conv(test["random"]) - 1
    breadth = {a: sum(1 for q in qualified[a] if q) / n for a in ARMS}
    override = div(whole["overturned"], whole["reviewed"])
    coverage = div(whole["reviewed"], whole["flagged"])
    invalid = div(whole["invalid"], whole["leads"])
    over = [w["complaints_per_10k"] > MOCK["complaint_max_per_10k"] for w in weekly]
    bad = [div(sum(r[a]["invalid"] for a in ARMS), sum(r[a]["leads"] for a in ARMS))
           > MOCK["invalid_max"] for r in weeks]

    def weekly_rule(flags):
        if any(a and b for a, b in zip(flags, flags[1:])):
            return "red"
        return "amber" if any(flags) else "green"

    lo, hi = MOCK["override_band"]

    status = {
        # same rules as governance-and-review-cadence.md
        "k1": ("green" if uplift >= MOCK["uplift_target"]
               else "amber" if uplift > 0 else "red"),
        "k2": "nodata",
        "m12": "green" if breadth["matching"] >= MOCK["breadth_min"] else "amber",
        "k3": ("green" if div(test["matching"]["relevant"],
                              test["matching"]["impressions"])
               >= MOCK["relevance_min"] else "red"),
        "k4": ("red" if coverage < MOCK["review_coverage_min"]
               else "green" if lo <= override <= hi else "amber"),
        "k5": weekly_rule(over),
        "g1": "green" if top10("matching") <= MOCK["top10_max"] else "red",
        "g2": weekly_rule(bad),
    }
    summary = {
        "weeks": WEEKS, "baseline_weeks": BASELINE_WEEKS, "agents": n,
        "top10_agents": top_n,
        "baseline": {
            "totals": base, "conversion": conv(base),
            "relevance": div(base["relevant"], base["impressions"]),
            "complaints_per_10k": per10k(base),
        },
        "test": {a: {
            "totals": test[a], "conversion": conv(test[a]),
            "relevance": div(test[a]["relevant"], test[a]["impressions"]),
            "top10_share": top10(a), "breadth": breadth[a],
        } for a in ARMS},
        "uplift": uplift,
        "pilot": {
            "totals": whole, "override_rate": override,
            "review_coverage": coverage, "invalid_rate": invalid,
            "label_coverage": div(whole["labelled"],
                                  whole["leads"] - whole["invalid"]),
            "complaints_per_10k": per10k(whole),
            "weeks_over_complaint_limit": sum(over),
            "weeks_over_invalid_limit": sum(bad),
        },
        "trap": trap,
        "status": status,
        "mock_thresholds": MOCK,
    }
    data = {"generated_by": "dashboard/make_mock_data.py", "seed": SEED,
            "is_mock": True, "weekly": weekly, "summary": summary}
    out = Path(__file__).with_name("data.js")
    head = ("// MOCK DATA. Simulated by make_mock_data.py (seed %d).\n"
            "// Not a real ImmoScout24 measurement. Do not edit by hand.\n" % SEED)
    out.write_text(head + "window.MOCK = " + json.dumps(data, indent=1) + ";\n",
                   encoding="utf-8", newline="\n")
    return summary


if __name__ == "__main__":
    s = build()
    print(json.dumps(s, indent=1))
