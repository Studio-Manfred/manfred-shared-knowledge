---
description: Quick risk pass on an in-flight feature — Cagan-risks deep dive, then design the cheapest assumption test for whatever's highest.
argument-hint: [feature or initiative name to risk-check]
---

You're pressure-testing an in-flight feature against Cagan's four risks. The user named: $ARGUMENTS

This is the shortest discovery cycle in the plugin. 30–60 minutes of conversation. Use it when:

- A feature is mid-build and someone wants to confirm it's still the right thing
- A new idea needs a fast sanity check before being added to the roadmap
- A `manfred-discovery:product-brief` got the risks at "Med" with no notes and someone wants the deeper read

## Step 1 — Cagan risk profile (deep)

Use the `manfred-discovery:cagan-risks` skill. Walk through Phase 1 (pre-flight: gather evidence) carefully — this is where the value of a risk-check sits. Don't accept "we know our customers" as evidence; ask for the data.

For each risk that comes back High:

- Confirm the rating with a one-line evidence-grounded reason
- Pick the cheapest test that retires it from the technique menu

Save the profile under `discovery-reports/cagan-risks-<slug>-<date>.md`.

## Step 2 — Design the test for the highest-rated risk

Use the `manfred-discovery:assumption-test` skill on the single highest-rated risk's cheapest test:

- State the assumption in the four-blank form (audience / behaviour / thing / reason)
- Pick the technique
- Write binary success / failure criteria
- Name the owner and timebox

Save under `discovery/tests/<assumption-slug>-<date>.md`.

## Step 3 — Decide what happens to the in-flight work

Based on the risk profile and test design, recommend one of:

- **Pause build, run the test first** — when the highest risk is genuinely High and the test is cheap (under a week)
- **Continue build in parallel with the test** — when the test takes longer than the next decision point
- **Continue build, accept the risk** — when stakes are low and re-work cost is acceptable; document the accepted risk explicitly so it doesn't get forgotten
- **Kill the work** — when one risk is High enough and well-evidenced enough that the answer is clearly "no"

Be direct about the recommendation. If the team has been building for weeks and the risk-check reveals a fundamental value-risk problem, name it clearly. The cost of saying so honestly is much lower than the cost of shipping the wrong thing.

## Wrap-up

Summarise:

- Highest risk and its rating
- The single test designed and its timebox
- The recommendation for the in-flight work
- Linear ticket update (if linked) — post the recommendation as a comment

Then offer:

> "Want to run `/manfred-discovery:weekly` to fold this test into a continuous discovery rhythm? Or `/manfred-discovery:kickoff` if the risk-check revealed this needs a proper brief and OST?"
