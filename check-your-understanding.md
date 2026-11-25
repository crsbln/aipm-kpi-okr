# Check Your Understanding: My Answers

The four lessons end with 16 questions. Each lesson shows a model solution.
These are my own answers, written before re-reading the solutions and then
compared with them. Examples come from my Imageboost artifacts.

## 01 Measurement Foundations

**1. Why is "number of dashboard views" usually not enough as a KPI?**
It counts activity. Many views do not show that anyone decided better, or
that the product earned anything. No decision follows from it. In my
inventory, widget impressions (M5) are the same kind of number.

**2. What is the difference between a KPI and an initiative?**
A KPI measures a result that matters. An initiative is work we do in the
hope of moving that result. K1 (qualified lead conversion) is a KPI.
"Build the district-matching rule" is an initiative.

**3. Why should AI product teams define counter-metrics?**
A system pushed toward one number can reach it in harmful ways. A
counter-metric makes the harm visible early. Matching may lift K1 while a
few agents take most impressions, so G1 watches K3.

**4. Why is model accuracy alone not enough to measure an AI product?**
Accuracy describes one part on test data. It says nothing about value for
users, money for the business, fairness between groups, or whether people
can correct mistakes. In my mock data K3 is 100 % in the matching arm by
construction, and that alone proves nothing about leads.

## 02 KPI Design

**1. Why is "number of Imageboost leads" weaker than "qualified lead
conversion rate"?**
A count grows when traffic grows. A rate divides by the exposure, so
traffic cancels out. "Qualified" also filters out junk. In my mock data the
random arm went from 16 to 31 qualified leads while nothing had changed.

**2. What makes a counter-metric different from a secondary KPI?**
A secondary KPI is a second thing we want to improve. A counter-metric is a
line we must not cross while improving the first one. It has a limit, not a
growth target.

**3. Why should KPI definitions include exclusions?**
So everyone counts the same thing every time. Without written exclusions,
test traffic or spam leads slip in or out and the trend changes for no real
reason. K1 excludes internal, test and bot traffic and confirmed junk.

**4. Why should an Imageboost KPI set include both lead conversion and
exposure fairness?**
Conversion shows value on average. Fairness shows who gets that value. A
high average can hide that a few agents get nearly everything. I pair K1
with G1 and with M12, the share of agents with at least one qualified lead.

## 03 OKR Design and Alignment

**1. Why is "launch Imageboost reporting dashboard" not a strong key
result?**
It describes shipping something. It would be met even if nobody used the
dashboard. A key result names the change the dashboard should cause.

**2. Can a KPI appear inside an OKR?**
Yes. A key result is often a KPI with a target and a date. Product KR1 is
K1 with the target T1 over weeks 3-8. The objective adds the direction.

**3. Why should an AI-product OKR usually include both product outcomes and
AI-system quality?**
Outcomes show value. System quality shows whether the automated part can
carry that value. With only outcomes, a risky system can hide behind a good
number. With only system quality, a team can celebrate a metric nobody
needs.

**4. Why should AI critique OKRs before rewriting them?**
If the assistant rewrites at once, its wording replaces the team's
thinking, and it may invent priorities. Critique first keeps the choice
with people. In this repository the reviewer returned findings only; the
changes were decided afterwards and logged.

## 04 Metric Quality and Governance

**1. Why can a metric become less useful after it becomes a target?**
People and systems start to chase the number itself. It can then rise
without the real thing improving. This is Goodhart's law. A lead-count
target would invite duplicate and low-quality leads.

**2. Why should KPI definitions have change control?**
If a formula or data source changes quietly, old and new values are no
longer comparable. A change log tells readers whether reality moved or the
ruler did. My governance file has one, with two entries.

**3. Why is a weekly review cadence not automatically better than a monthly
cadence?**
Slow or noisy numbers jump around from week to week. Looking weekly invites
reactions to chance. K4 has between 7 and 25 flags a week in my mock data, so
it is judged monthly.

**4. Why should AI-system metric changes be documented alongside product
changes?**
When a rule, model or threshold changes, the numbers move. Without a note,
the team would read that movement as customer behaviour. In the pilot, a
switch from random to matching must be dated in the change log.

## Comparison with the lesson solutions

All 16 answers agree with the lesson solutions in substance. I found no
point where my answer contradicts one. Two solutions go further than mine:
lesson 03, question 1 lists example outcomes (fewer support questions,
higher retention), and lesson 04, question 1 also names qualitative review
as a protection.
