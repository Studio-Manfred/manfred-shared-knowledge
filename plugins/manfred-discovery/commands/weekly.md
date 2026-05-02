---
description: Run one week of continuous discovery — plan customer touchpoints, design any assumption tests for the week, and write the readout when the week wraps.
argument-hint: [outcome name or "this week's focus" optional]
---

You're running one week of continuous discovery. The user mentioned: $ARGUMENTS

Walk through the cycle in three phases — one at the start of the week, one mid-week (per assumption test), one Friday afternoon.

## Start of week — Plan touchpoints

Use the `manfred-discovery:customer-touchpoint-plan` skill to plan the week:

- Confirm the mode (expansion / refinement / probe)
- Set the recruit (segment, sample size, channel, incentive)
- Schedule 3–5 × 60-minute slots across 3 days
- Confirm Trio attendance for each
- Prep the topics and assumptions being probed

Save under `discovery/touchpoints/<YYYY>-W<week-number>.md`.

## Mid-week — Design assumption tests as needed

If the week's mode is **probe**, or if a customer conversation surfaces an assumption that needs a test, use the `manfred-discovery:assumption-test` skill to design the experiment:

- One assumption per test
- Specific technique from the menu (not "do user research")
- Binary success / failure criteria written before the test runs
- Owner and timebox

Save each test under `discovery/tests/<assumption-slug>-<date>.md`. If the test runs fast enough to complete in the same week, run it; otherwise it carries to next week.

## End of week — Friday synthesis + readout

Friday afternoon, run the synthesis ritual (60 min, Trio):

- Walk through what was heard in each conversation
- Surface themes
- Update the OST (`manfred-discovery:opportunity-solution-tree` skill) — opportunities added/refined/parked, solutions added/parked, test status updates
- Identify decisions taken

Then use the `manfred-discovery:discovery-readout` skill to produce the cycle readout:

- What we set out to learn (mode + outcome focus)
- What we actually learned (with evidence + confidence)
- What changes (OST updates, decisions, next tests)
- What's still open
- Cost & metadata

Save under `discovery-reports/<TICKET-or-cycle-slug>-<YYYY-MM-DD>.md`. If a Linear ticket is linked (branch matches `[A-Z]+-\d+`), post the readout summary as a Linear comment.

## Wrap-up

Confirm:

- Touchpoints attended ✓ (with Trio? if not, flag in next week's health check)
- OST updated ✓ (`last updated` timestamp matches today)
- Readout saved + posted ✓
- Next week's plan started ✓ (or scheduled for Monday)

Then offer:

> "Run `/manfred-discovery:weekly` again next Monday to start the cycle. Or `/manfred-discovery:risk-check` if a specific risk surfaced this week that needs deeper attention."
