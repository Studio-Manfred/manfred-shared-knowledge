---
description: Plan, script, run, and summarise a single customer interview round.
argument-hint: [participant or session description]
---

You're running a single interview cycle — plan → script → conduct → summarise. The user mentioned: $ARGUMENTS

## Step 1 — Plan the conversation

If this interview is part of a touchpoint plan already, skip to Step 2. Otherwise use `manfred-discovery:customer-touchpoint-plan` to confirm:

- Which assumption / opportunity is this serving?
- Recruit fit (segment, recency, behavioural criteria)
- Trio attendance
- Recording protocol + consent
- Compensation

If any of those aren't sorted **before today**, recommend rescheduling. Tomorrow-morning recruit isn't viable.

## Step 2 — Write the script

Use `manfred-design-research:interview-script`. Don't combine discovery + usability in one 45-minute session. Pick one. Story-based questions only.

Save the script to `discovery/scripts/<participant-slug>-<date>.md`.

## Step 3 — Run the interview

Trio attends. Recording consented. Session within timebox.

## Step 4 — Summarise

Use `manfred-design-research:summarize-interview` after the recording is available. Extract:

- Top 3 takeaways
- Verbatim quotes
- Jobs surfaced
- Current behaviour
- Pain points
- Surprises
- Open questions for next cycle

Save to `discovery/summaries/<participant-slug>-<date>.md`. If the recording is sensitive, run `manfred-design-research:transcript-anonymizer` on the transcript first.

## Step 5 — Update the OST + Linear

Action items from the summary push into:

- `manfred-discovery:opportunity-solution-tree` — opportunity / solution / assumption updates
- Linear comment on the linked ticket (if any) via `mcp__linear-server__save_comment`

## Wrap-up

One sentence each:

- What was learned
- What changes in the OST
- The single most important next action

Then offer:

> "Next interview in this cycle: run `/manfred-design-research:interview` again. Or `/manfred-design-research:synthesize` if 5+ summaries are now ready for cross-cutting analysis."
