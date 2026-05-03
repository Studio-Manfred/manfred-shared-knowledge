---
name: metrics-definition
description: Use when defining UX metrics that connect design decisions to measurable user and business outcomes — anyone says "what should we measure", "design metrics", "KPIs", "north-star metric", "HEART framework", "OKRs for design", "success criteria", "how do we know this worked", "track design impact". Manfred-flavoured: outcomes over outputs, behavioural + attitudinal balance, baselines before measurement.
---

# metrics-definition

A metric is a forced decision about what we're trying to change. Done right, metrics resolve "is this working?" arguments before they happen. Done wrong, they become a vanity dashboard nobody acts on.

Manfred picks 3–5 primary metrics per project. More than that and the team can't focus; fewer and the metric is too narrow to anchor real decisions.

## Overview

Four metric categories. Pick across all four — a metric set that's only behavioural misses how users *feel* about the work; only attitudinal misses what they *do*.

| Category | What it captures | Examples |
|---|---|---|
| **Behavioural** | What users actually do | Task completion rate, time on task, error rate, feature adoption |
| **Attitudinal** | How users perceive the experience | SUS, NPS, CSAT, perceived ease |
| **Business** | What the org cares about | Conversion, retention, support volume, cost per active user |
| **Engagement** | Frequency and depth of use | DAU/MAU, session duration, return visits, feature discovery |

Plus the **HEART framework** (Google) as a cross-cutting frame:

- **Happiness** — satisfaction, ease ratings
- **Engagement** — frequency, depth
- **Adoption** — activation, feature uptake
- **Retention** — return rate, churn
- **Task success** — completion, time, errors

HEART helps the team check coverage. A metric set with no Happiness signal is incomplete.

## When to use

- Defining success criteria for a new feature, project, or quarter
- Setting up a north-star metric for a product
- Operationalising the success criteria from `manfred-ux-strategy:design-brief`
- Planning a measurement approach for a `manfred-ux-strategy:north-star-vision`
- Reviewing existing metrics that aren't producing decisions
- Pre-launch: making sure the team will actually know if this worked

**Skip when:**

- The user wants research design (use `manfred-design-research:diary-study-plan` / `usability-test-plan`)
- The user wants analytics implementation (different artifact — instrumentation plan)
- The user wants a metric for "design quality" in the abstract (push back — measure outcomes, not aesthetics)

## Pre-flight

Ask:

- What decision will this metric inform? (If "we just want to track" — push for the decision first.)
- What's the time horizon? (Weekly check-in, quarterly review, annual planning?)
- What's the data source? (Existing analytics, new instrumentation, survey, manual sampling?)
- Who owns the metric? (Has accountability for movement.)
- What's the baseline? (No baseline = no signal.)

If the user can't answer "what decision will this inform" — the metric isn't ready to be picked. Pick the decision first.

## The hard rules

| Rule | What it means |
|---|---|
| **Connect to a hypothesis** | Every metric is tied to a specific hypothesis ("if we improve onboarding clarity, completion rate goes from 62% → 75%"). Metrics without hypotheses become dashboards nobody acts on. |
| **Baseline first** | Measure current state before claiming improvement. "We made onboarding 30% better" is meaningless without the starting number. |
| **Behavioural + attitudinal balance** | Pick across both. Behavioural metrics tell you what happened; attitudinal tells you whether users felt good about it. |
| **3–5 primary, not 15** | Beyond 5 primary metrics, the team can't focus. Secondary metrics live in a dashboard; primary metrics drive the work. |
| **Owner + cadence stated** | Metrics without an owner don't move. Metrics without a review cadence don't get acted on. Both fields required, not optional. |
| **Outcomes, not outputs** | "Ship the redesign" is an output. "Onboarding completion +13pp" is an outcome. Measure what users / business get, not what the team produces. |
| **Connect to qualitative signal** | Numeric metrics tell you what changed; customer verbatims tell you why. Always pair — "completion rate +13pp AND users say 'I finally understood what KYC was for'". |

## The flow

### Step 1 — Surface the decision

Ask: "If this metric moves up / down, what changes for the team?"

If "we'd celebrate" — not a decision. If "we'd reverse the launch and revisit the design" — that's a decision. The metric exists to inform one.

### Step 2 — Pick the hypothesis

Translate the decision into a falsifiable hypothesis:

> "If [specific design change], then [specific user behaviour], because [user mechanism we believe in]."

Example:
> "If we add a real-time KYC progress indicator, then onboarding completion will rise from 62% → 75% over 4 weeks, because users currently abandon during the wait when they don't know how long it takes."

The hypothesis dictates the metric. No hypothesis = no metric, just data collection.

### Step 3 — Pick the metric(s)

For the hypothesis above:

| Type | Metric | Why this captures the change |
|---|---|---|
| **Primary (behavioural)** | Onboarding completion rate (KYC start → first transaction) | Direct measure of the outcome |
| **Primary (attitudinal)** | Post-onboarding ease rating (5-pt) | Captures the felt-experience side |
| **Secondary (business)** | Support tickets containing "KYC" / "verification" / "wait" | Indirect signal — should drop if completion improves |
| **Guardrail** | KYC fraud rate | Make sure speed didn't break compliance |

Pick across categories. Add a **guardrail metric** (something that should NOT regress) for any change with risk.

### Step 4 — Define each metric precisely

Use this template per metric:

```markdown
### Metric: [Name]

**Definition.** [Plain-language description. What's counted, what's excluded.]

**Calculation.** [Specific formula. "Number of users who completed KYC ÷ number who started KYC, in last 30 days, excluding test accounts."]

**Data source.** [Where the data lives. Specific event name if analytics. Survey instrument if attitudinal.]

**Baseline.** [Current value. Date measured.]

**Target.** [Where we're trying to get to.]

**Time horizon.** [When we'll measure improvement.]

**Owner.** [Person accountable.]

**Review cadence.** [Weekly? Per release? Quarterly?]

**Action thresholds.**
- If metric moves ≥X% — keep current direction
- If metric moves ≤Y% — reverse and revisit design
- If metric stays flat — investigate (is the change reaching users? wrong hypothesis?)
```

### Step 5 — HEART coverage check

Walk the metric set against HEART:

- **Happiness** — covered? (SUS, ease rating, NPS)
- **Engagement** — covered? (frequency, depth, return visits)
- **Adoption** — covered? (activation, feature uptake)
- **Retention** — covered? (return rate, churn)
- **Task success** — covered? (completion, errors, time)

If three+ HEART dimensions are uncovered, the set is too narrow. Add one or two metrics; don't add five.

### Step 6 — Pair with qualitative

Every primary metric needs a qualitative companion. Plan for:

- **Customer verbatim review.** Periodic read-through of support tickets, NPS comments, interview quotes — looking for the "why" behind the metric movement.
- **Spot interviews.** When a metric moves unexpectedly (positive or negative), 3–5 short calls in the next sprint to understand what users experienced.

A metric set without a qualitative companion is data theatre.

## Output format

Save to `discovery/metrics/<engagement-slug>-<YYYY-MM-DD>.md`:

```markdown
# Metrics — <project / engagement>

**Date**: YYYY-MM-DD
**Hypothesis**: [The hypothesis the metric set serves]
**Decision**: [What movement triggers what action]
**Owner of the set**: <name>

## Primary metrics
[3–5 metrics with full template per Step 4]

## Secondary metrics
[Supporting metrics — used for context, not for go/no-go decisions]

## Guardrail metrics
[Things that should NOT regress]

## HEART coverage
[Walk the framework — confirm not over- or under-indexed on one dimension]

## Qualitative companion plan
[How verbatims and spot interviews will pair with the numbers]

## Reporting cadence
[Weekly | per release | quarterly — and to whom]
```

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Let's measure everything, we'll figure out what matters later" | Measuring everything = measuring nothing. The set has to fit on one page or it won't drive decisions. |
| "We don't need a baseline, we'll just track from here" | Without a baseline you can't say whether the change made things better. Measure current state first. |
| "Vanity metrics are still useful for stakeholder updates" | Vanity metrics produce vanity decisions. If a number doesn't drive action, it doesn't belong in the primary set. |
| "Attitudinal metrics are too soft, just measure behaviour" | Behaviour without attitude misses *why* users acted. A completion rate that rose because users gave up trying alternatives is a fail dressed as a win. |
| "We'll add the qualitative read later" | Numbers without verbatims become dashboards nobody acts on. Plan the qualitative pairing now. |
| "5 metrics is too few — leadership wants more" | Leadership wants confidence, not metrics. 5 well-chosen metrics produce more confidence than 20 noisy ones. Push back. |

## Manfred lens

Metrics touch **value risk** (Cagan) directly — they're the operationalisation of "is this thing actually useful?". They're also the success criteria for `manfred-discovery:opportunity-solution-tree` outcomes — every node on the OST should map to a metric or be flagged "metric needed".

Critical & ethical (principle 6): some metrics are easy to game in ways that harm users (engagement without value, retention via dark patterns, conversion via misleading copy). Picking metrics without an ethics check produces metric-driven harm. Always ask: "if this metric maxes out, what does the experience look like? Is that good for users?"

## Cross-references

- `manfred-discovery:opportunity-solution-tree` — outcomes ladder up; metrics measure outcome movement
- `manfred-discovery:assumption-test` — assumption tests need metrics to know if they passed
- `manfred-ux-strategy:design-brief` — success criteria pull from this skill
- `manfred-ux-strategy:north-star-vision` — north-star metric pulls from this skill
- `manfred-design-research:summarize-interview` — for the qualitative companion plan

## Tools used

- `Read` — existing dashboards, analytics docs, prior brief
- `Write` — produce the metric set
- `manfred-discovery:opportunity-solution-tree` — for outcome anchoring
- `manfred-design-research:summarize-interview` — for verbatim companion plan

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
