---
name: jobs-to-be-done
description: Use when mapping the jobs a customer is hiring a product to do — functional, emotional, social — with outcome expectations and lifecycle stages. Triggers on "JTBD", "jobs to be done", "what job is the customer hiring this for", "functional / emotional / social job", "outcome-driven innovation", "Christensen jobs", "switch interview".
---

# jobs-to-be-done

Maps the customer's job in three dimensions (functional, emotional, social) with lifecycle stages and outcome expectations. Reframes product decisions around customer motivation, not feature lists.

## Overview

JTBD's central reframe: customers don't buy products, they hire products to make progress on a job they're trying to get done. The same person hiring an invoicing app for a freelance side-hustle has a different job from a sole-trader carpenter doing it once a month — even though both are "small business owners doing invoicing."

Used well, JTBD prevents feature-list product thinking. Used badly, it's a label slapped on personas without the underlying motivation work.

This skill maps a job in three dimensions, breaks it into lifecycle stages, and surfaces solution gaps where current options don't serve the job well.

## When to use

- Reframing a product strategy from features to motivation
- Discovery research has surfaced a recurring pain — JTBD helps name what job underlies it
- Comparing competing solutions for the same customer (the alternatives + non-consumption are the competition)
- Pairs with `manfred-discovery:opportunity-solution-tree` — opportunities map to job dimensions

**Skip when:**

- The team needs to design a specific UI — JTBD is too high-altitude; use `journey-map` or `usability-test-plan`
- Single-interaction features (e.g. a single button's affordance) — wrong scope

## Two principles drive everything

1. **Three dimensions, not one.** Functional gets the headlines; emotional and social often drive the actual decision. A solo founder hiring an invoicing app emotionally hires it to feel "professional" and socially hires it to be perceived as "a real business" — not just to send invoices. Skip dimensions and you miss the actual motivation.
2. **Job, not feature.** "Send an invoice" is a feature. "Get paid quickly without looking unprofessional or pestering my client" is a job. Phrase jobs as outcomes the customer wants, not actions they take.

## Phase 1 — Pre-flight

- **Source data:** interviews, support tickets, NPS verbatims, switch-interview notes (if available)
- **Customer segment:** specific (segment matters — same product, different jobs per segment)
- **Output path:** `discovery/jobs/<segment-slug>-<YYYY-MM-DD>.md`

## Phase 2 — Identify the core job

The core job is the high-altitude outcome. Test it with two questions:

- "If we asked the customer what they hired our product to help them do, what would they say in their own words?"
- "What is the customer trying to make progress on?"

If the answer is a feature ("send invoices"), keep going up: "What does sending invoices help them do?" Eventually you reach: "Get paid for the work I did, without spending more than 10 minutes a week on the admin." That's the job.

## Phase 3 — Map the three dimensions

| Dimension | Question | Example |
|-----------|----------|---------|
| **Functional** | What practical outcome are they getting? | "Get paid within 14 days for work completed" |
| **Emotional** | How do they want to feel doing it? | "Feel in control without anxiety about cash flow" |
| **Social** | How do they want to be perceived by others? | "Look like a legit business to my clients" |

For each dimension, capture both the desired outcome and what currently undermines it. Source-link with verbatim quotes where possible.

## Phase 4 — Define lifecycle stages

The job isn't a single moment; it has stages. Map them:

| Stage | What happens | Customer outcome wanted |
|-------|--------------|-------------------------|
| **Define / Locate** | Recognising the need, finding options | "Find a tool that won't take a weekend to set up" |
| **Prepare** | Setting up to use the solution | "Get to first invoice without reading docs" |
| **Confirm** | Validating it works | "Trust the tool before sending real money through it" |
| **Execute** | Doing the job | "Send the invoice; track it" |
| **Monitor** | Tracking progress | "Know when it's been viewed / paid / overdue" |
| **Modify** | Adjusting / following up | "Chase late payers without burning the relationship" |
| **Conclude** | Ending the job for this cycle | "Reconcile this month's invoices before tax filing" |

Not every job has all 7 stages — collapse where appropriate. But don't skip stages just because they're hard.

## Phase 5 — Identify outcome expectations + gaps

For each stage, name what success looks like (the outcome expectation) and where current solutions fall short (the gap).

| Stage | Outcome expectation | Current gap |
|-------|---------------------|-------------|
| Define/Locate | "Tool I can find without research effort" | Discovery is dominated by ads from generic accounting software; no clear pre-purchase comparison |
| Prepare | "Set up in under 30 min" | Most tools require accountant-level field knowledge to configure |
| ... | ... | ... |

Gaps become opportunities (`manfred-discovery:opportunity-solution-tree`).

## Phase 6 — Surface non-consumption + competing alternatives

Two often-missed forces:

- **Non-consumption** — customers who could be doing this job but aren't. Why? (Often the most fertile market.)
- **Competing alternatives** — what else are customers hiring to do this job? Spreadsheets, manual tracking, a specific competitor, a friend who does this for them. The competition is usually broader than the team thinks.

## Phase 7 — Output

Save to `discovery/jobs/<segment-slug>-<YYYY-MM-DD>.md`:

```markdown
# Jobs-to-be-done — [Segment / job name]

**Date:** [YYYY-MM-DD]
**Segment:** [specific behavioural definition]
**Sources:** [N interviews, support clusters, etc.]

## The core job (one-line)

> "[Customer language phrasing of the high-altitude job]"

[Push past feature-shaped phrasing.]

## Dimensions

### Functional
- **Desired outcome:** [...]
- **What currently undermines it:** [...] — [source]

### Emotional
- **Desired feeling:** [...]
- **What currently undermines it:** [...] — [source]

### Social
- **Desired perception:** [...]
- **What currently undermines it:** [...] — [source]

## Lifecycle stages

| Stage | Outcome wanted | Current gap |
|-------|----------------|-------------|
| Define/Locate | [...] | [...] |
| Prepare | [...] | [...] |
| Confirm | [...] | [...] |
| Execute | [...] | [...] |
| Monitor | [...] | [...] |
| Modify | [...] | [...] |
| Conclude | [...] | [...] |

## Competing alternatives

- [Alternative 1] — [why customers use it]
- [Alternative 2 — non-consumption — what stops them from doing the job at all] — [reason]

## Top opportunities (for the OST)

- [Gap with highest impact + best fit for our team] — [link to OST]
- [...]

## Linked artifacts

- Source summaries: [paths]
- Linked archetype: [path]
- Linked OST opportunities: [links]
```

## Manfred lens

- **Customer-driven always** (principle 1) — JTBD is the operationalisation of "users before features"
- **Critical & ethical design** (principle 6) — opportunities should serve the customer's job, not exploit weaknesses (no dark-pattern opportunity gaps)
- **Research isn't a phase** (principle 2) — JTBD maps update as new interviews surface new dimensions

## Cross-plugin handoffs

- **Input from `manfred-design-research:interview-script`** — JTBD probing during discovery interviews ("What were you trying to do?", "Walk me through the last time you hired a tool to do this")
- **Input from `manfred-design-research:summarize-interview`** — Jobs surfaced section feeds here
- **Output to `manfred-discovery:opportunity-solution-tree`** — gaps become opportunities under the outcome
- **Output to `manfred-design-research:user-archetype`** — jobs become a behavioural dimension of archetypes
- **Output to `manfred-design-research:journey-map`** — lifecycle stages become journey phases

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Functional dimension is enough — emotional / social is fluff" | Emotional and social are usually where the actual decision lives. Skip them and you misread the customer. |
| "Let's just label our personas with their job" | Persona-with-a-job-label is not JTBD. JTBD's value is the dimensions + stages + gaps work. The label alone is theatre. |
| "Non-consumption isn't relevant — they're not customers" | Non-consumption is often the bigger opportunity. Why aren't they doing the job at all? |
| "Lifecycle stages are too granular" | Most products skip Confirm and Monitor — and lose customers there. Don't skip stages because they're inconvenient. |

## Red flags — STOP

- About to write the core job as a feature ("send invoices") → Stop. Keep asking "what does that help them do?"
- About to fill only the Functional dimension → Stop. Force Emotional and Social.
- About to skip Non-consumption + competing alternatives → Stop. They're often the most useful section.
- About to map a job for a segment defined demographically ("women aged 30–50") → Stop. Segment by behaviour, not demographics.

## Tools used

- **Write**: `discovery/jobs/<slug>-<date>.md`
- **Skills called**:
  - `manfred-design-research:interview-script` — JTBD-style probing in discovery interviews
  - `manfred-discovery:opportunity-solution-tree` — gaps become opportunities
  - `manfred-design-research:user-archetype` — jobs as archetype dimension
- **Reference**: Clayton Christensen et al, *Competing Against Luck*; Anthony Ulwick, *Outcome-Driven Innovation*; Bob Moesta on switch interviews

---

*Adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT). Three-dimensions emphasis, lifecycle-stages-as-default, non-consumption section, and Manfred OST integration are original.*
