# Validation Summary

Purpose: the coding-agent validation summary that handout Part 13 asks for.
It lists what was checked, what passed, and what is still open.

The first pass (2026-11-15) wrote every artifact but was cut off by a usage
limit before it wrote this file and before it committed. A resumed pass on
2026-11-25 ran the checks below. The result of the first pass's own
follow-up consistency check was not saved, so it is not reported here.

## 1. Changed files

| File | Change |
| --- | --- |
| `README.md` | New section "My work" |
| `measurement-backlog.md` | New: board, 30 issues, Checkpoint 1 |
| `business-model-and-decision-question.md` | New: Part 3 |
| `hypotheses.md` | New: Part 4, Checkpoint 2 |
| `metric-inventory.md` | New: Part 5 |
| `kpi-definition-sheets.md` | New: Parts 6 and 7, Checkpoint 3 |
| `okrs.md` | New: Part 8, Checkpoint 4 |
| `governance-and-review-cadence.md` | New: Part 9 |
| `measurement-briefing.md` | New: Part 10, Checkpoint 5 |
| `dashboard/` | New: Part 11, Checkpoint 6 |
| `ai-collaboration-log.md` | New: Part 12 |
| `check-your-understanding.md` | New: answers to the 16 lesson questions |
| `validation-summary.md` | New: this file |

The lesson files `01` to `05` and `assets/` are unchanged.

## 2. Validation results

| Check | Command | Result |
| --- | --- | --- |
| Markdown style | `rumdl check --config 'global.disable = ["MD033"]' .` (rumdl 0.3.6) | First run: 1 issue, a link to this file, which did not exist yet. After writing it: no issues |
| Whitespace | `git diff --check` (new files included with `git add -N`) | No output: clean |
| Mock data is reproducible | `uv run python dashboard/make_mock_data.py` | `data.js` came out byte for byte the same as before |
| Dashboard opens without build tools | Headless Chrome screenshot of `dashboard/index.html` from disk | All six sections render with numbers |
| Numbers quoted in the Markdown files | Compared with the output of the script | All match (see below) |

Numbers checked against the script output (all mock, seed 21):

| Claim | Where | Script says |
| --- | --- | --- |
| Random arm: 16 then 31 qualified leads, weeks 3-4 against 7-8 | `check-your-understanding.md`, `dashboard/README.md` | 16 and 31 |
| Random-arm rate moved by about half | `governance-and-review-cadence.md` | +54 % |
| 7 to 25 flags a week | `check-your-understanding.md` | 7 (week 1) to 25 (week 7) |
| Exposure concentration about 10 % random, about 14 % matching | `dashboard/README.md` | 10.4 % and 14.0 % |
| Relevance 100 % in the matching arm | several files | 100 % |

Counts checked by hand: 30 backlog issues (21 in Review, 9 Blocked), 8
hypotheses, 9 assumptions, 26 metrics (4 business, 10 user, 3 AI-system, 4
oversight, 5 risk), 5 KPIs and 3 guardrails, 7 key results, 54 log rows (44
accepted, 9 edited, 1 rejected), 16 lesson answers.

## 3. Dashboard files created

`dashboard/index.html`, `dashboard/styles.css`, `dashboard/data.js`,
`dashboard/README.md`, and `dashboard/make_mock_data.py`, the script that
writes `data.js`.

Checked in Chrome only. Firefox was not checked.

## 4. Mock values and assumptions still unresolved

- Every count on the dashboard is simulated. None is a measurement.
- Every threshold is a placeholder: T1 (+15 %), T3 (50 %), T4 (5 % to
  20 %), T5 (1.0 per 10,000), T7 (20 %), T8 (10 %), T9 (80 %), and 80 %
  review coverage. T2, T6 and T10 have no value at all.
- No baseline is measured: B1 to B5 are all open.
- The pilot scope (Berlin, rental, 8 weeks) is an assumption.
- The two-arm split and the district-matching rule are a proposal.
- The matching arm's large lead is built into the simulation settings. It is
  not a finding.

## 5. Decisions the team must make manually

1. Accept or change the two-arm pilot design. It is the largest change that
   came out of the reviews.
2. Define "qualified lead" and who labels it.
3. Agree T1 to T10 before pilot week 1.
4. Put named people behind the owner roles.
5. Decide whether a no-widget holdout is allowed.
6. Decide whether to create the GitHub Project board from
   `measurement-backlog.md`.

## Open Questions

- Should the dashboard also be checked in Firefox before a presentation?
- Who signs off this summary: the product lead or the whole group?
