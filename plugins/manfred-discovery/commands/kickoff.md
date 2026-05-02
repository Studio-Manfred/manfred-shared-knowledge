---
description: Frame a new opportunity end-to-end — write the product brief, profile the Cagan risks, and stand up an opportunity-solution tree to track what comes next.
argument-hint: [initiative name or one-line opportunity description]
---

You're kicking off a new product opportunity. The user gave: $ARGUMENTS

Walk through these three steps in sequence. Don't rush — each one feeds the next.

## Step 1 — Product brief

Use the `product-brief` skill to facilitate the 8-section brief. Don't dump all the sections at once; have a conversation. Pay particular attention to:

- Section 01 (The Opportunity) — push hard on problem-first
- Section 03 (The Hypothesis) — gate on completeness
- Section 05 (Cagan Risks) — collect initial ratings; deeper assessment comes in Step 2

When the brief is drafted and saved, summarise the top three things you learned and move on.

## Step 2 — Cagan risk profile

Use the `cagan-risks` skill to produce a deeper risk profile, picking up from section 05 of the brief. For each risk:

- Confirm or revise the rating from the brief based on actual evidence
- Name the cheapest test that retires each High (and worth-retiring Med)
- Sequence the tests by cost and dependency

Save the risk profile under `discovery-reports/cagan-risks-<slug>-<date>.md`. Cross-reference it from the brief.

## Step 3 — Opportunity-solution tree

Use the `opportunity-solution-tree` skill to stand up the OST:

- Anchor on the outcome from section 02 of the brief
- Add the opportunities that came up in section 01 and any uncovered during the risk discussion
- Add 1–3 candidate solutions under the highest-impact opportunity
- For each solution, name the riskiest assumption (link to assumption tests designed in Step 2)

Save the OST under `discovery/<outcome-slug>-ost.md`.

## Wrap-up

Summarise:

- What was learned in each step
- The single most important next action (usually the cheapest assumption test)
- What's now scheduled vs. what's still open

Then offer:

> "Ready to set up the discovery rituals so this stays continuous? Run `/manfred-discovery:weekly` to plan the first week of customer touchpoints, or `/manfred-discovery:risk-check` to deep-dive a specific risk."
