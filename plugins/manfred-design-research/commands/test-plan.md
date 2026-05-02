---
description: Design a usability test plan — research questions, tasks, recruit (with accessibility inclusion), facilitation guide, synthesis path.
argument-hint: [feature or design to test]
---

You're designing a usability test plan. The user mentioned: $ARGUMENTS

## Step 1 — Clarify what the test serves

Ask:

- What specific research questions does the test answer? (3–5, max. "Is the design good?" doesn't count.)
- What's being tested — prototype, staging, or live product?
- Moderated or unmoderated? (Moderated → 5–8 participants, richer signal. Unmoderated → 15–30+, shallower.)
- Linked OST opportunity / assumption — what changes for the team based on the result?

If the question is "do users want this" — value risk — redirect to `manfred-discovery:cagan-risks` + `manfred-discovery:assumption-test` first. Usability tests answer can-they-use-it, not should-we-build-it.

## Step 2 — Use the usability-test-plan skill

Run `manfred-design-research:usability-test-plan` to produce the full plan:

- Research questions
- Recruit (accessibility-inclusive — at least 1 in 5 disabled / AT user)
- Tasks as scenarios in user language (not click instructions)
- Facilitation guide (don't help, don't explain, embrace silence)
- Pilot test
- Synthesis plan

Save to `discovery/usability/<study-slug>-<date>.md`.

## Step 3 — If moderated, write the moderator script

Use `manfred-design-research:interview-script` for the actual session script. Same rules apply: story-based probes, no leading, Trio attendance.

## Step 4 — Pilot

Pilot with 1 internal volunteer before going live. Catches ambiguous task instructions, tech setup issues, time mis-estimates.

## Step 5 — After the test, synthesise

Use `manfred-design-research:summarize-interview` for each moderated session debrief. For aggregate analysis, use `manfred-design-research:affinity-diagram`.

Findings push into:

- `manfred-discovery:opportunity-solution-tree` — confirmed issues become opportunities
- `manfred-discovery:assumption-test` — if the test was retiring a specific assumption
- `manfred-design-systems:a11y-qa` — accessibility findings cross over

## Wrap-up

Confirm the plan covers:

- [ ] Specific research questions (not "is it good")
- [ ] Tasks as scenarios in user language
- [ ] Accessibility-inclusive recruit (1 in 5 minimum)
- [ ] Pilot before live test
- [ ] Trio attendance (for moderated)
- [ ] Synthesis plan (who, when, output format)

Then offer:

> "Run the pilot, then `/manfred-design-research:test-plan` again if findings need a follow-up test. Or `/manfred-design-research:synthesize` once the test is run and you have summaries to cluster."
