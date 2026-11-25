# Measurement Strategy Briefing

Purpose: a one-page briefing for product leadership on how Imageboost will be
measured and what decision the numbers will support. Handout Part 10 and
Checkpoint 5.

Status: a proposal from the workshop. No real data, baseline or target exists.

## Briefing

```text
Product goal:
Make Imageboost a trusted acquisition channel for real estate agents.

Decision question:
Should ImmoScout24 invest further in Imageboost as a paid agent-growth
product? Options at the end of the pilot: scale, change, stop.

Primary KPIs:
K1 Qualified lead conversion rate: leads that agents label as useful, per
valid widget impression. Judged at week 8, matching arm against random arm.
K2 Renewal rate gap: participating agents against matched agents outside
the pilot. This is the business proof. It has no data at week 8.

AI-system and oversight metrics:
K3 Relevant-agent display rate: how often the shown agent serves the
searched district.
K4 Flag override rate: how often a reviewer restores a flagged lead. Read
together with G3, the share of flags that were reviewed at all.

Counter-metrics:
K5 Consumer complaint rate per 10,000 impressions.
G1 Exposure concentration: share of impressions for the top 10 % of agents.
G2 Invalid lead rate: duplicates and spam.

OKR:
Objective: make Imageboost a trusted acquisition channel for agents in the
pilot market. Key results: K1 in the matching arm beats the random arm by
an agreed uplift; an agreed share of agents gets at least one qualified
lead; K3 reaches an agreed share; K5, G1 and G2 stay inside agreed limits.
A team OKR makes the numbers trustworthy: 4 of 4 pilot baselines measured
by week 3 (today 0 of 4).

Review cadence:
Weekly pilot review. Checkpoints at weeks 4 and 8. Quarterly for renewal.
Launch gate in pilot week 8.

Open validation questions:
1. What marks a lead as qualified, and what if agents label few leads?
2. Does the district rule match what people call a relevant agent?
3. May searches be split between random and matching? Is a no-widget
   holdout allowed?
4. How many leads are needed before a result is more than chance?
5. Which complaint level is a red line?
6. Is the pilot scope (Berlin, rental, 8 weeks) agreed?

Recommendation:
Do not decide yet. Agree targets and red lines before week 1. Measure
baselines in weeks 1-2. Compare random with matching in weeks 3-8. Decide
at week 8 on lead value, and check that decision against renewal later.
```

## What we ask leadership for

| Ask | Why |
| --- | --- |
| Confirm the pilot scope and allow the two-arm split | Without a comparison there is nothing to decide on |
| Name an owner per KPI | A number without an owner changes nothing |
| Agree targets and red lines before week 1 | Targets set after results bend to the results |
| Accept that week 8 proves lead value at best | Renewal is a lagging number |

## What this briefing does not claim

- It does not claim that Imageboost works. No hypothesis is tested.
- It contains no measured number. The dashboard shows mock data only.
- It does not claim the pilot is large enough. The sample size is not
  calculated.
- It assumes that an agent serves a known set of districts. If agents work
  city-wide, the matching rule and K3 lose their meaning.

## Checkpoint 5: rehearsal with a skeptical stakeholder

A separate Claude reviewer read the first version as a skeptical product
leader and asked five questions. Short answers:

| # | Question | Answer |
| --- | --- | --- |
| 1 | You call the pilot "controlled". Where is the control group, and why would K1 rise between week 2 and week 8 if nothing changes? | Correct: there was none. The pilot now has two arms in weeks 3-8, random and matching. K1 is judged between the arms. The word "controlled" was removed |
| 2 | K2 is a primary KPI but is not in the OKR or the gate. On what business evidence do I invest at week 8? | On none. Week 8 gives evidence on lead value only. The briefing now says so. K2 can reopen the decision |
| 3 | Agents label their own leads. What stops bias, and what about unlabelled leads? | Nothing stops bias yet. Unlabelled leads do not count as qualified, and label coverage is reported next to K1 (Team KR3). Still an open risk |
| 4 | K3 will be low by design and G1 fine by design. What do they tell me? | Under random allocation, nothing new. They matter in the matching arm, where K3 should rise and G1 may get worse. That trade-off is why both are kept |
| 5 | With a few dozen qualified leads and a couple of complaints a week, which rule fires on signal and not chance? | Unknown until a sample-size check is done (backlog issue 25). K1 and G1 are judged on six weeks per arm, not weekly. K5 is judged at market level only |

Unsupported claims that were found and removed or reworded: "controlled
pilot"; "agree targets before week 3" (now: before week 1); "few shown
agents will fit" (now an assumption).

All findings and decisions are in `ai-collaboration-log.md`.

## Open Questions

- Who is the audience: product leadership only, or sales leadership too?
- Does leadership want one headline number, and if so, is it K1?
- How much does the pilot cost, and who pays for the review work?
