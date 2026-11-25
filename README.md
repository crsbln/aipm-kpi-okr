# KPI and OKR Design

This repository is a Markdown-based learning path for defining useful
measurement systems in AI product work. Participants learn how to move from
business goals to hypotheses, KPIs, OKRs, AI-system quality metrics,
human-oversight metrics, risk guardrails, review cadences, and decision-ready
reporting.

## Project at a Glance

The project translates strategy into a balanced measurement system that teams
can use to make decisions without losing sight of risk or user value.

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Arial","primaryTextColor":"#172033","lineColor":"#64748B"},"flowchart":{"curve":"basis","nodeSpacing":36,"rankSpacing":52}}}%%
flowchart LR
    Goal[Design a decision-ready<br/>measurement system]
    subgraph Frame["<b>1. Frame What Must Be Measured</b>"]
        direction TB
        Strategy[Strategy and<br/>business outcome]
        Hypothesis[Product hypothesis]
        Questions[Decision questions<br/>and metric layers]
        Strategy --> Hypothesis --> Questions
    end
    subgraph Design["<b>2. Design KPIs, OKRs and Guardrails</b>"]
        direction TB
        KPIs[Outcome KPIs<br/>owners, targets and segments]
        Leading[Leading indicators]
        OKRs[Objective and<br/>key results]
        Guardrails[AI quality, oversight<br/>and risk guardrails]
        System[Balanced measurement<br/>system]
        KPIs --> System
        Leading --> System
        OKRs --> System
        Guardrails --> System
    end
    subgraph Operate["<b>3. Turn Measurement into Decisions</b>"]
        direction TB
        Dashboard[Static dashboard<br/>prototype]
        Cadence[Review cadence<br/>and governance]
        Decision{What decision does<br/>the evidence support?}
        Output[Measurement plan<br/>with clear decisions]
        Dashboard --> Cadence --> Decision --> Output
    end
    Goal --> Frame --> Design --> Operate
    classDef goal fill:#172033,color:#FFFFFF,stroke:#172033,stroke-width:2px;
    classDef input fill:#FFFFFF,color:#172033,stroke:#4677A8,stroke-width:1.5px;
    classDef work fill:#FFFFFF,color:#172033,stroke:#3B8A5A,stroke-width:1.5px;
    classDef output fill:#FFFFFF,color:#172033,stroke:#B77A1F,stroke-width:1.5px;
    class Goal goal;
    class Strategy,Hypothesis,Questions input;
    class KPIs,Leading,OKRs,Guardrails,System work;
    class Dashboard,Cadence,Decision,Output output;
    style Frame fill:#F5F9FD,stroke:#9BB8D2,stroke-width:1.5px;
    style Design fill:#F4FAF6,stroke:#9DC8AD,stroke-width:1.5px;
    style Operate fill:#FFFAEF,stroke:#D7B66B,stroke-width:1.5px;
```

## Learning Objectives

By the end of this repository, you should be able to:

- Explain the difference between metrics, KPIs, OKRs, targets, and initiatives.
- Translate product strategy into measurable hypotheses and decision questions.
- Design a balanced AI product measurement stack across business value, user
  value, AI-system quality, human oversight, and risk guardrails.
- Design KPIs with clear definitions, owners, targets, segments, and review
  cadence.
- Write SMART KPI targets without confusing activity, output, and outcome.
- Use OKRs to connect ambitious objectives to measurable key results.
- Identify vanity metrics, proxy metrics, counter-metrics, and metric gaming
  risks.
- Use Claude Code, Codex, or a similar coding agent to challenge assumptions,
  improve KPI definitions, test OKRs, build a static dashboard prototype, and
  validate workshop artifacts while retaining human decision ownership.
- Use GitHub Projects to track measurement design work and open validation
  questions.

## Learning Path

The modules build on each other in order.

| File / Folder | Description |
|---|---|
| [**01 - Measurement Foundations**](01-measurement-foundations.md) | Understand metrics, KPIs, OKRs, leading and lagging indicators, and the AI product measurement stack. |
| [**02 - KPI Design**](02-kpi-design.md) | Design high-quality KPIs across business, user, AI-system, oversight, and risk layers. |
| [**03 - OKR Design and Alignment**](03-okr-design-and-alignment.md) | Write OKRs that connect product value, AI-system quality, guardrails, initiatives, and strategy. |
| [**04 - Metric Quality and Governance**](04-metric-quality-and-governance.md) | Review metric quality, avoid gaming, define governance, and connect measurement to decision cadence. |
| [**05 - Session Handout**](05-session-handout.md) | Run the practical workshop using GitHub Projects, a coding agent, the Imageboost scenario, and a static dashboard prototype. |

### Additional Folders and Files

| File / Folder | Description |
|---|---|
| [**assets**](assets/) | Local images used in the lesson files and handout. |

## My work

The workshop in `05-session-handout.md` is worked through for the case it
prescribes: **Imageboost**, the promoted agent widget on ImmoScout24.

> [!NOTE]
> The course session ran on 21 September 2026 (course week 5). This work was
> done later, on 2026-11-15, in one delegated pass by Claude (a coding agent).
> There was no group and no live workshop. The owner's review is pending.
> Nothing here is validated: there is no real Imageboost data, and every
> number on the dashboard is simulated and labelled as mock.

| Handout part | File | What it holds |
|---|---|---|
| Parts 1-2, Checkpoint 1 | [measurement-backlog.md](measurement-backlog.md) | The project board and 30 issues, written as a file |
| Part 3 | [business-model-and-decision-question.md](business-model-and-decision-question.md) | Business model, decision question, pilot design, KPI tree |
| Part 4, Checkpoint 2 | [hypotheses.md](hypotheses.md) | 8 hypotheses, 9 assumptions |
| Part 5 | [metric-inventory.md](metric-inventory.md) | 26 candidate metrics across the five layers, KPI shortlist |
| Parts 6-7, Checkpoint 3 | [kpi-definition-sheets.md](kpi-definition-sheets.md) | 5 KPI sheets, 3 guardrails, SMART targets |
| Part 8, Checkpoint 4 | [okrs.md](okrs.md) | One product OKR, one team OKR |
| Part 9 | [governance-and-review-cadence.md](governance-and-review-cadence.md) | Owners, cadences, decision rules, launch gate, change log |
| Part 10, Checkpoint 5 | [measurement-briefing.md](measurement-briefing.md) | One-page briefing and the skeptical-stakeholder rehearsal |
| Part 11, Checkpoint 6 | [dashboard/](dashboard/) | Static dashboard prototype: open `dashboard/index.html` |
| Part 12 | [ai-collaboration-log.md](ai-collaboration-log.md) | 54 review findings with decisions; how the work was really done |
| Part 13 | [validation-summary.md](validation-summary.md) | Validation commands, results, open items |
| Lessons 01-04 | [check-your-understanding.md](check-your-understanding.md) | My answers to the 16 lesson questions |

Not possible in a solo pass, and not done:

- No GitHub Project board and no GitHub issues were created. They are
  written down in `measurement-backlog.md`.
- No group drafted or decided. A second Claude instance ran the six
  checkpoint reviews; the drafting Claude decided what to change.
- No stakeholder, agent or searcher was asked anything.

## Setup

> [!NOTE]
> Throughout these steps, text in angle brackets like `<repo-name>` is a
> placeholder. Replace it including the `< >` brackets with your own value.
> For example, `cd <repo-name>` becomes `cd aipm-kpi-okr`.

### 1. Create the Repository from the Template

Click **Use this template** on GitHub.

When creating the repository:

- Set yourself as the **Owner**
- Choose a repository name
- Disable **Include all branches**
- Click **Create repository**

> [!IMPORTANT]
> If you are working in pairs or groups, only one person should complete this
> step.

---

### 2. Add Collaborators (Pairs/Groups Only)

If working with teammates:

1. Open the repository on GitHub
2. Go to **Settings -> Collaborators**
3. Add your teammates as collaborators
4. Share the repository link with your team

Teammates should accept the invitation before continuing.

---

### 3. Clone the Repository

Copy the SSH URL from the **Code** button on GitHub, then run:

```bash
git clone <copied-ssh-url>
```

The copied SSH URL will look like:
`git@github.com:<your-username>/<repo-name>.git`.

---

### 4. Move into the Project Folder

No Python environment is required for this repository.

```bash
cd <repo-name>
```

---

### 5. Open the Lesson Files

Open `README.md` and follow the lesson files in numerical order. The files are
plain Markdown and can be read directly on GitHub or in a local editor.

## References & Further Reading

- [**KPI.org: KPI Basics**](https://www.kpi.org/kpi-basics/):
  Practical overview of KPIs as critical, quantifiable measures of progress.
- [**KPI.org: KPI Development**](https://www.kpi.org/kpi-basics/kpi-development/):
  Measure-Perform-Review-Adapt approach for building KPI systems.
- [**Google re:Work: Set goals with OKRs**](https://rework.withgoogle.com/intl/en/guides/set-goals-with-okrs):
  Google-oriented guide to setting objectives and key results.
- [**What Matters: What is an OKR?**](https://www.whatmatters.com/faqs/okr-meaning-definition-example):
  Definition and examples of objectives and key results.
- [**SMART criteria**](https://en.wikipedia.org/wiki/SMART_criteria):
  Orientation on SMART goal-setting and its historical roots.
- [**Objectives and key results**](https://en.wikipedia.org/wiki/Objectives_and_key_results):
  Orientation on OKR history and structure.
