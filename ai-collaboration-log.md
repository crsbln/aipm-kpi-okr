# AI Collaboration Log

Purpose: record what the coding agent contributed, which risks it found, and
what was decided. Handout Part 12. Decisions, not chat transcripts.

## How this work was really done

The handout describes a group that drafts, an agent that critiques, and a
group that decides. That is not what happened here. The truth:

- **One delegated pass on 2026-11-15.** Claude (Anthropic's coding agent)
  wrote every artifact and the dashboard, alone. No group and no workshop
  took place. The course session itself ran on 2026-09-21.
- **The checkpoints were real, but AI reviewed AI.** After the first draft, a
  second, separate Claude instance ran the six checkpoint prompts from the
  handout. It saw only the files, not the drafting, and it could not edit.
  It returned 42 numbered findings, five stakeholder questions with a
  list of unsupported claims, and six cross-file inconsistencies. The tables
  below hold one row for each: 54 rows.
- **The "team decision" column is Claude's decision.** The drafting Claude
  chose to accept, edit or reject each finding. No human decided anything.
- **Owner review is pending.** The repository owner has not yet read,
  approved or changed any of this.
- **Order.** The handout forbids running the workshop as one task and says
  to stop after each part. This pass drafted all parts, then ran all six
  reviews together, then revised. That breaks the handout's working rule.
- **One follow-up check.** After the revision, the reviewer checked the
  changed files once more for consistency (last table).
- **A resumed pass on 2026-11-25.** The first pass was cut off by a usage
  limit before it committed. A second Claude pass wrote
  `validation-summary.md`, ran the handout's validation commands and checked
  every quoted number against the script output. It changed no decision.

Nothing in the artifacts is validated evidence. All numbers on the dashboard
are simulated.

## Decision totals

| Decision | Findings |
| --- | --- |
| Accepted | 44 |
| Edited (accepted in a changed form) | 9 |
| Rejected | 1 |

## Checkpoint 1: backlog

| Activity | Coding-agent contribution | Assumption or risk found | Team decision | Reason |
| --- | --- | --- | --- | --- |
| Backlog review C1-1 | Statuses did not match their "done when"; two issues pointed to files that did not exist | A board that looks finished while work is open | Accepted | Rewrote criteria and statuses; wrote the two missing files |
| Backlog review C1-2 | No issue for the pilot comparison, sample size or the launch-gate rule | A pilot without a comparison cannot answer the decision question | Accepted | Added issues 25 and 26 |
| Backlog review C1-3 | No issue sets up the flag rule and review step | K4, G2 and H7 rest on a process nobody owns | Accepted | Added issue 27 |
| Backlog review C1-4 | No issue for hypotheses or for guardrail definitions | Work done without a tracking row | Accepted | Added issue 28; issue 9 now names G1 to G3 |
| Backlog review C1-5 | Issues 9 and 15 are too broad | Large issues hide progress | Rejected | For a solo pass both artifacts already exist; noted that a team should split them |
| Backlog review C1-6 | Three acceptance criteria were not observable | "Reads it once" cannot be checked | Accepted | Reworded the criteria of issues 12, 14 and 16 |
| Backlog review C1-7 | Layer "All" is not a single-select value; two fields never filled; one role owns half the issues | The board fields would not work in GitHub | Edited | Each issue now names one main layer. Metric type and Confidence stay per metric in the inventory. Owner overload became an open question |
| Backlog review C1-8 | Two prerequisites of K1 and K3 had no issue | Initiatives could be mistaken for outcomes | Accepted | Added issues 29 and 30, marked as initiatives |

## Checkpoint 2: hypotheses

| Activity | Coding-agent contribution | Assumption or risk found | Team decision | Reason |
| --- | --- | --- | --- | --- |
| Hypothesis review C2-1 | H5 said random allocation ignores fit, the diagram said the opposite; H5 held two claims | A hypothesis that cannot be disproved cleanly | Accepted | Split into H5 (matching raises K1) and H8 (exposure stays acceptable) |
| Hypothesis review C2-2 | H1, H2 and H6 compared against groups nobody had defined | No holdout, no evidence | Accepted | Wrote a pilot design with two arms; the no-widget holdout is an open leadership question |
| Hypothesis review C2-3 | H4 compares agents who chose to join with those who did not | Selection bias would look like an effect | Accepted | H4 names the bias; comparison agents must be matched |
| Hypothesis review C2-4 | H7's evidence measured wrong flags, not missed junk | Review only sees what was flagged | Accepted | H7 now measures junk that agents report and that was never flagged (M24) |
| Hypothesis review C2-5 | "Qualified" is the agent's own label; no rule for unlabelled leads | Label bias and thin coverage distort K1 | Accepted | Added assumption A8, label coverage (M25) and Team KR3 |
| Hypothesis review C2-6 | H1 claimed "useful" visibility but measured raw views | A proxy presented as the thing itself | Edited | Dropped "useful" from H1; usefulness is tested by H2 and H3 |
| Hypothesis review C2-7 | Missing hypotheses: searcher benefit, willingness to pay, perceived fairness | Business case rests on untested beliefs | Edited | Listed as open questions, not hypotheses: they need research with agents and searchers, and none exists |
| Hypothesis review C2-8 | Cannibalised listing contacts; agents may serve several districts | Widget leads may not be extra; the district rule may be crude | Accepted | H2 compares total leads (M26); H5 names the multi-district risk |

## Checkpoint 3: KPI definitions and targets

| Activity | Coding-agent contribution | Assumption or risk found | Team decision | Reason |
| --- | --- | --- | --- | --- |
| KPI audit C3-1 | K1's target compared week 8 with weeks 1-2 although nothing changes in between | The target could only be hit by chance | Accepted | K1 is now judged matching arm against random arm in weeks 3-8 |
| KPI audit C3-2 | K3 was computed from data, yet other files asked who labels it | Rule or human label: two different metrics | Accepted | K3 is a rule on profile data; a human-checked sample tests the rule (Team KR2) |
| KPI audit C3-3 | G2 had no limit, so a red line naming it could not fire | A rule that can never trigger | Accepted | G2 has a target row and a decision rule |
| KPI audit C3-4 | Four denominators did not match their populations | Numbers that cannot be reproduced | Accepted | Aligned K1, K5, G1 and G2 |
| KPI audit C3-5 | K2 excluded agents who left, and its target was weaker than H4 | Excluding leavers removes the result | Accepted | Leavers stay in; target says "higher" |
| KPI audit C3-6 | K4 weekly on about nine flags is noise; the reviewer owned a metric about their own work; counter-metrics had no formula | Self-grading and chance | Accepted | K4 judged monthly, owned by the product lead; G3 defined |
| KPI audit C3-7 | K3 and G1 could not move under random allocation | Two blind metrics | Accepted | Both are judged in the matching arm |
| KPI audit C3-8 | K5's pause rule worked on zero to one complaints per district-week | A rule firing on chance | Accepted | K5 is judged at market level only |
| KPI audit C3-9 | No rule for label lag; K2's counter-metric undefined; no drift check | Gaps at the edges | Edited | Added the 7-day label rule. M22 stays inventory-only and is marked so. Drift is not relevant for a fixed rule |

## Checkpoint 4: OKRs

| Activity | Coding-agent contribution | Assumption or risk found | Team decision | Reason |
| --- | --- | --- | --- | --- |
| OKR review C4-1 | No key result had an owner; the dashboard invented them | Nobody reacts | Accepted | Owner table added; dashboard uses it |
| OKR review C4-2 | The AI-system KR was unreachable with random allocation; its initiative would change what KR1 measures | KR and initiative worked against each other | Accepted | Solved by the two-arm design |
| OKR review C4-3 | "5 of 5 baselines by week 2" was impossible | The launch gate would always say "wait" | Accepted | Now 4 of 4 by week 3; K2 is left out and the file says why |
| OKR review C4-4 | No agent-side value measure in the product OKR | "Trusted" was scored without agents | Accepted | Added Product KR2 (M12) |
| OKR review C4-5 | No oversight KR; G2 missing from the guardrail KR | Oversight invisible in the OKR | Edited | G2 added. K4 stays out: it is a band to stay in, handled by governance |
| OKR review C4-6 | Team KR1 and KR3 were compliance states | Tasks in disguise | Edited | KR3 replaced by label coverage; the change log moved to initiatives. KR1 kept, with its weakness written down |
| OKR review C4-7 | KR said "every week" but G1 is reviewed less often | Cadence mismatch | Accepted | G1 judged at weeks 4 and 8 everywhere |
| OKR review C4-8 | Placeholders did not map to baselines; "enough impressions" undefined | Readers cannot tell T from B | Accepted | Placeholder table added; "trusted" stays an open question |

## Checkpoint 5: briefing rehearsal

The five questions and answers are in `measurement-briefing.md`.

| Activity | Coding-agent contribution | Assumption or risk found | Team decision | Reason |
| --- | --- | --- | --- | --- |
| Rehearsal Q1 | Asked for the control group | "Controlled pilot" was an unsupported claim | Accepted | Two-arm design; word removed |
| Rehearsal Q2 | Asked what business evidence exists at week 8 | A "primary KPI" with no data at decision time | Accepted | Briefing states that week 8 proves lead value at best |
| Rehearsal Q3 | Asked what stops label bias | Agents grade their own leads | Edited | Coverage is measured; bias itself stays an open risk |
| Rehearsal Q4 | Asked what K3 and G1 add | Blind under random allocation | Accepted | Explained by the matching arm |
| Rehearsal Q5 | Asked which rule fires on signal | Small counts | Edited | Rules judged on longer windows; the sample-size check is still not done |
| Rehearsal claims | Found three unsupported statements and four missing steps | Target timing contradicted itself; one claim assumed one district per agent | Accepted | Reworded; missing steps are backlog issues 19, 21 and 25; pilot cost stays open |

## Checkpoint 6: dashboard

The review ran on the first dashboard. The dashboard was then rebuilt for
the two-arm design.

| Activity | Coding-agent contribution | Assumption or risk found | Team decision | Reason |
| --- | --- | --- | --- | --- |
| Dashboard review C6-1 | Complaint status used the 8-week total although the rule is weekly; one mock week was over the limit | A green card that should have been amber | Accepted | Status now follows the weekly rule in code |
| Dashboard review C6-2 | K4 divided by flagged leads, the definition said reviewed leads | Card and definition disagreed | Accepted | The simulation has a "reviewed" state; G3 is shown |
| Dashboard review C6-3 | G2 was missing from cards and definitions | A named counter-metric nobody could see | Accepted | G2 card and row added |
| Dashboard review C6-4 | Status logic differed from the governance rules | Two sources of truth | Accepted | One set of rules, written in governance and coded in the script |
| Dashboard review C6-5 | Some notes showed simulated numbers without their own label | Mock data could be read as measured | Accepted | Every note with numbers ends with a MOCK label |
| Dashboard review C6-6 | A property of the simulation was stated as fact | Unsupported claim | Accepted | Reworded: 100 % relevance is "by construction" |
| Dashboard review C6-7 | A hard-coded "about 70 leads"; a count compared with a rate of a different thing | Wrong number on the page | Accepted | Numbers come from the data; the box compares like with like |
| Dashboard review C6-8 | Thresholds typed into the HTML; unused fields in the data | Page and data could drift apart | Accepted | Thresholds are read from `data.js` |
| Dashboard review C6-9 | Could not confirm the Chrome check; Firefox unchecked | Unverified claim in the README | Edited | Chrome render was repeated and looked at; Firefox is still unchecked and the README says so |

## Cross-file findings

| Activity | Coding-agent contribution | Assumption or risk found | Team decision | Reason |
| --- | --- | --- | --- | --- |
| Consistency check X1 | One launch-gate branch could never be reached; K2, K4 and G2 played no part | A decision rule with a dead end | Accepted | Gate redrawn; K2's absence is explained |
| Consistency check X2 | K1's red rule differed between two files | Two rules for one KPI | Accepted | One rule, in governance |
| Consistency check X3 | K1 owner differed between files | Unclear ownership | Accepted | Product lead everywhere |
| Consistency check X4 | "Growth channel" and "acquisition channel" both used | Wording drift | Accepted | "Acquisition channel" everywhere |
| Consistency check X5 | OKR cadence differed between two tables | Cadence drift | Accepted | Weeks 4 and 8 |
| Consistency check X6 | Inventory: M9 rejected as "a count" though it had a denominator; K2 derived from a metric with no comparison; M16 typed as counter-metric | Loose reasoning in the shortlist | Accepted | Reworded all three |

## Follow-up check after the revision

See `validation-summary.md` for the result of the second look.

## What the owner still has to do

- Read every artifact and overrule any decision above.
- Decide whether the two-arm pilot design is what the group would have
  chosen. It is the largest change that came out of the review.
- Replace role names with people, and placeholders with agreed values.
