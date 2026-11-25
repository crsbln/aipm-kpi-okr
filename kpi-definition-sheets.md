# KPI Definition Sheets

Purpose: define the selected KPIs so exactly that another team would compute
the same number. Handout Parts 6 and 7, Checkpoint 3.

No KPI has a real baseline or a validated target. Every target below carries
a status: **mock** (placeholder used only in the dashboard prototype),
**assumed** (my proposal, unchecked) or **validated** (agreed with data and
stakeholders). Nothing is validated yet.

Shared terms:

- **Valid widget impression**: one display of the Imageboost widget on a
  search result page in the pilot market, without internal, test and bot
  traffic.
- **Pilot market**: Berlin rental searches, 8 weeks. Assumed scope.
- **Arms**: in weeks 3-8 each search is split by chance into the **random**
  arm (today's allocation) or the **matching** arm (an agent from the
  searched district). Proposed design, not agreed.
- **Qualified lead**: a valid lead that the agent labels as useful within 7
  days. Leads without a label are not counted as qualified. Label coverage
  is reported next to K1. The exact signal is open (backlog issue 20).
- **Week of a lead**: the week it was submitted. A week's K1 is final 7 days
  after the week ends.

## Part 6: Definition sheets

| Field | K1 | K2 | K3 |
| --- | --- | --- | --- |
| Name | Qualified lead conversion rate | Renewal rate gap | Relevant-agent display rate |
| Strategic goal | Make Imageboost a trusted acquisition channel for agents | Grow the paid agent business | Show agents who fit the search |
| Formula | Qualified leads ÷ valid widget impressions | Renewal rate of participating agents − renewal rate of matched comparison agents | Valid widget impressions where the shown agent lists the searched district as a service area ÷ valid widget impressions |
| Unit | Percent; also shown per 10,000 impressions | Percentage points | Percent |
| Measurement layer | User outcome | Business impact | AI-system quality |
| AI-system behavior | Allocation decides which agent gets the impression and so the chance of a useful lead | None direct; allocation acts through K1 | Allocation itself: a random draw, or the district-matching rule |
| Population | Valid widget impressions in the pilot market, per arm | Paying agents in the pilot market whose contract came up for renewal in the period | Same as K1 |
| Exclusions | Internal, test and bot traffic; leads confirmed as duplicate or spam | Test accounts; agents who joined mid-period. Agents who leave stay in: they are the result | K1 traffic exclusions; searches without a district |
| Segment | Arm, district, device, agent type | Agent type, agent size, district | Arm, district |
| Baseline needed | B1: K1 under random allocation, pilot weeks 1-2 and the random arm | B2: renewal rate of matched comparison agents | B3: K3 under random allocation |
| Target | See Part 7 | See Part 7 | See Part 7 |
| Cadence | Watched weekly; judged at weeks 4 and 8 | Quarterly | Weekly, and after every allocation change |
| Owner | Product lead | Sales lead | Data analyst |
| Counter-metric | K5 complaint rate, G2 invalid lead rate, label coverage | M22 agent support tickets about Imageboost (inventory only, no sheet yet) | G1 exposure concentration |

K3 is computed by a rule from agent profile data. It needs no human label
per impression. A human-checked sample tests whether the rule is right
(Team KR2 in `okrs.md`). In a rental-only pilot the deal type is constant,
so it is not part of the rule.

| Field | K4 | K5 |
| --- | --- | --- |
| Name | Flag override rate | Consumer complaint rate |
| Strategic goal | Keep people able to correct the system | Protect searcher trust |
| Formula | Reviewed flags where the reviewer restored the lead ÷ reviewed flags | Complaints that name the widget ÷ valid widget impressions × 10,000 |
| Unit | Percent | Complaints per 10,000 impressions |
| Measurement layer | Human oversight | Risk guardrail |
| AI-system behavior | The flag rule (duplicate or spam) is the automated step being checked | Allocation and widget design decide who sees what, and how often |
| Population | Imageboost leads flagged as duplicate or spam and reviewed | Valid widget impressions in the pilot market |
| Exclusions | Flags not yet reviewed (they count in G3) | Complaints about other products; internal tickets |
| Segment | Flag reason, arm | Arm, device, complaint reason |
| Baseline needed | B4: current flag volume, review coverage and override rate | B5: current complaint volume for the search page |
| Target | See Part 7 | See Part 7 |
| Cadence | Watched weekly; judged monthly, because flags are few | Weekly, at market level only |
| Owner | Product lead (not the reviewer, who would grade their own work) | Customer support lead |
| Counter-metric | G3 flag review coverage; junk leads that agents report and that were never flagged | K1: complaints must not be cut by hiding the widget |

### Guardrails defined next to the KPIs

| Field | G1 | G2 | G3 |
| --- | --- | --- | --- |
| Name | Exposure concentration | Invalid lead rate | Flag review coverage |
| Formula | Impressions of the top 10 % of agents ÷ impressions of all agents active for the full period | Leads confirmed as duplicate or spam ÷ submitted leads | Flags reviewed ÷ flags raised |
| Unit | Percent. An even split gives 10 % | Percent | Percent |
| Measurement layer | Risk guardrail | Risk guardrail | Human oversight |
| Population | Agents active for the full period, per arm | Submitted Imageboost leads | Imageboost leads flagged as duplicate or spam |
| Exclusions | Agents who joined or left mid-period, with their impressions | None. Unreviewed flags count as valid until reviewed | None |
| Cadence | Weeks 4 and 8 | Weekly | Weekly |
| Owner | Data analyst | Lead-quality reviewer | Lead-quality reviewer |

## Part 7: SMART targets and counter-metrics

`B1` to `B5` are baselines that must be measured first. `T1` to `T8` are
target values that must be agreed before pilot week 1. The "Mock
placeholder" column exists only so the dashboard can show a status.

| KPI | SMART target | Target status | Mock placeholder | Counter-metric | AI or risk red-line threshold |
| --- | --- | --- | --- | --- | --- |
| K1 Qualified lead conversion rate | Over pilot weeks 3-8, K1 for Berlin rental searches in the matching arm is higher than in the random arm by at least the agreed uplift T1 | Assumed wording, no value | T1 = +15 % | K5, G2, label coverage | Red if the matching arm is not above the random arm at week 8 |
| K2 Renewal rate gap | At the first full renewal cycle after the pilot, participating agents renew at a rate higher than matched comparison agents by the agreed gap T2 | Assumed wording, no value | None: no data in an 8-week pilot | M22 agent support tickets | Review the product promise if the gap is zero or negative |
| K3 Relevant-agent display rate | K3 in the matching arm reaches the agreed share T3 over weeks 3-8, and a human-checked sample agrees with the rule | Assumed wording, no value | T3 = 50 % | G1 | Pause allocation changes if K3 drops after a change |
| K4 Flag override rate | Each month, K4 stays inside the agreed band T4 while G3 stays at or above its limit | Assumed wording, no value | T4 = 5 % to 20 %; G3 at least 80 % | G3, unflagged junk reported by agents | Red if G3 is below its limit: a low override rate then means nothing |
| K5 Consumer complaint rate | In every pilot week, widget complaints stay at or below the agreed limit T5 per 10,000 impressions, at market level | Assumed wording, no value | T5 = 1.0 per 10,000 | K1 | Pause the widget if T5 is crossed two weeks in a row |
| G1 Exposure concentration | At weeks 4 and 8, the top 10 % share in the matching arm stays at or below the agreed limit T7 | Assumed wording, no value | T7 = 20 % | K3 | Review the matching rule if the limit is crossed |
| G2 Invalid lead rate | In every pilot week, G2 stays at or below the agreed limit T8 | Assumed wording, no value | T8 = 10 % | K1 | Tighten the lead form or flag rule if T8 is crossed two weeks in a row |

`T6` is the agreement share for the relevance rule. It belongs to Team KR2
in `okrs.md`.

Small counts: the mock pilot produces only a handful of qualified leads,
flags and complaints per week. No rule fires on a single week of a single
district. How many events a rule needs is an open question (backlog issue
25).

### SMART check

| KPI | Specific | Measurable | Achievable | Relevant | Time-bound |
| --- | --- | --- | --- | --- | --- |
| K1 | Yes: which arm, where, which rate | Only once the qualified label exists | Unknown without B1 | Yes: the value promise | Yes: weeks 3-8 |
| K2 | Yes | Only if agents can be matched | Unknown | Yes: the business outcome | Yes, but after the pilot |
| K3 | Yes | Yes, from profile data; the rule itself needs a check | Likely in the matching arm, since rule and metric use the same test | Yes: explains K1 | Yes: weeks 3-8 |
| K4 | Yes | Yes, if a review step exists | Unknown without B4 | Yes: oversight | Yes: monthly |
| K5 | Yes | Yes, if complaints can be tagged | Unknown without B5 | Yes: trust | Yes: weekly |

## Checkpoint 3: audit of the KPI definitions

A separate Claude reviewer ran the handout prompt on the first version of
this file. Main changes made after the review:

- K1's target compared week 8 with weeks 1-2 although nothing would change
  in between. It now compares the matching arm with the random arm.
- K3 mixed a computed rule with a human label. It is now a rule; a human
  sample checks it.
- G2 had no limit, so a red line that named it could not fire. G2 now has a
  target row. G3 was added so "nobody reviews" becomes visible.
- Denominators now match their populations (K1, K5, G1).
- K2 no longer excludes agents who leave, and its target now says "higher".
- K4 is judged monthly and owned by the product lead.

All findings and decisions are in `ai-collaboration-log.md`.

## Open Questions

- What exactly marks a lead as qualified, and who labels it?
- If agents label few leads, is K1 still usable?
- Does the district rule agree with what a person would call relevant?
- How many events does each rule need before it may fire?
- Can agents be matched well enough for K2?
- Can a complaint be tied to the widget in the support tool?
