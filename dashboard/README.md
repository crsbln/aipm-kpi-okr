# Imageboost KPI and OKR Dashboard (Prototype)

A static dashboard for the KPI and OKR workshop. It shows how the Imageboost
measurement system would look to product leadership. It holds **no real
data**.

## How to open it

Double-click `index.html`, or drag it into a browser. No server, no install
and no build step are needed. It was rendered and looked at in Chrome on
2026-11-15. Firefox was not checked.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The page: six sections and a small script that fills in the numbers |
| `styles.css` | The look |
| `data.js` | The mock pilot data, written by the script below |
| `make_mock_data.py` | Simulates the mock pilot and writes `data.js` |
| `README.md` | This file |

## Sections

1. Executive summary: product goal, decision question, recommendation,
   confidence.
2. OKR scorecard: objective, key results, status, owner, confidence.
3. KPI cards by layer: business, user, AI-system, oversight, risk.
4. Metric definitions: formula, denominator, population, exclusions, cadence,
   owner.
5. Assumptions: mock values, missing baselines, validation questions.
6. Decision brief: recommendation, trade-offs, next steps.

## Which data is mock

Everything with a yellow `MOCK` label, which is every measured-looking number
on the page.

- **Counts** (impressions, views, clicks, leads, flags, labels, complaints)
  are simulated by `make_mock_data.py` with a fixed seed (21).
- **Design** of the mock pilot: 8 weeks. Weeks 1-2 use random allocation
  only. In weeks 3-8 each search is split by chance between a random arm and
  a matching arm (an agent from the searched district).
- **Settings** of the simulation are invented: 120 agents, 60,000 raw
  impressions in week 1 growing 6 % a week, district search shares, agent
  counts per district, and the view, click, lead, flag, review, label and
  complaint rates. The 12 Berlin borough names are real; their numbers are
  not.
- **Thresholds** behind the status colours are placeholders: +15 % uplift,
  80 % of agents with a qualified lead, 50 % relevance, 5 to 20 % override
  band, 80 % review coverage, 1.0 complaints per 10,000 impressions, 20 %
  top-10 share, 10 % invalid leads. Nobody agreed them.
- **Status colours** follow the decision rules in
  `governance-and-review-cadence.md`, applied to mock counts and mock
  thresholds. They say nothing about the real product.

The only real number is "0 of 4" pilot baselines measured. It counts the
state of `kpi-definition-sheets.md`.

## What the mock run shows, and what it does not

- The matching arm beats the random arm by a wide margin. That is **not a
  finding**. The settings say that a fitting agent gets more views, clicks
  and useful labels, so the result is built in.
- Relevance is 100 % in the matching arm by construction: the rule and the
  metric use the same test.
- Exposure concentration rises from about 10 % to about 14 % under matching.
  The size follows from the invented district shares. The direction is the
  trade-off to watch.
- The random arm shows why small counts mislead. Behaviour is the same in
  every week, yet the rate differs clearly between weeks 3-4 and weeks 7-8,
  on 16 and 31 qualified leads. That is chance.

It does not show how Imageboost performs. Change the settings and the story
changes.

## Rebuild the data

```bash
uv run python dashboard/make_mock_data.py
```

Run it from the repository root. It needs only the Python standard library
and prints the summary numbers.

## Before real use

- Replace `data.js` with measured pilot data.
- Replace every mock threshold with an agreed target.
- Remove the `MOCK` labels only for values that are validated.
