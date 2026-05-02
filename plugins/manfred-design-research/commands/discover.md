---
description: Run a discovery cycle — interviews, summaries, affinity, archetypes — for a defined outcome or product area.
argument-hint: [outcome name or product area to research]
---

You're running a discovery cycle. The user named: $ARGUMENTS

Walk through these phases. Don't rush — discovery is the work, not paperwork around it.

## Phase 1 — Set up the cycle

Confirm with the user:

- Which outcome from the OST is this serving? (If none — first run `manfred-discovery:opportunity-solution-tree` to anchor; come back here.)
- Which segment / archetype hypothesis is being explored?
- What's the timeline — one week, sprint, longer?

If this is part of an existing continuous discovery rhythm, skip the rituals setup. If it's the team's first discovery cycle, point at `manfred-discovery:discovery-rituals` to set up the cadence first.

## Phase 2 — Plan the touchpoints

Use the `manfred-discovery:customer-touchpoint-plan` skill to plan the week's customer conversations:

- Mode: probably **expansion** (new outcome) or **refinement** (sharpening known opportunities)
- Recruit segment, Trio attendance, schedule

## Phase 3 — Script and run interviews

For each conversation, use `manfred-design-research:interview-script` to produce the script. Story-based questions only. One method per session (discovery, not usability — separate cycle for that).

Run the interviews, recordings consented and saved.

## Phase 4 — Summarise each interview

After each session, use `manfred-design-research:summarize-interview` to extract findings, jobs surfaced, pain points, surprises.

Each summary is one file under `discovery/summaries/`.

## Phase 5 — Synthesise across the cycle

Once 5+ summaries exist, use `manfred-design-research:affinity-diagram` to cluster the observations into themes.

Then, depending on what the themes show:

- **Behavioural clustering visible →** use `manfred-design-research:user-archetype` to produce archetypes
- **Stage-shaped patterns visible →** use `manfred-design-research:journey-map` (one per archetype)
- **Strong emotional patterns visible →** use `manfred-design-research:empathy-map` (one per archetype)
- **Jobs / motivations are the central insight →** use `manfred-design-research:jobs-to-be-done`

You don't need all four. Run the synthesis skills the data actually wants.

## Phase 6 — Update the OST + ship the readout

Push the High impact + High confidence themes into `manfred-discovery:opportunity-solution-tree` as new opportunities.

Use `manfred-discovery:discovery-readout` to wrap the cycle with a markdown report saved to `discovery-reports/` and a Linear comment if a ticket is linked.

## Wrap-up

Summarise:

- Number of interviews run
- Top 3 themes from synthesis
- Updates pushed to the OST
- Recommended next cycle (more interviews? assumption test? different segment?)

Then offer:

> "Next cycle: run `/manfred-design-research:discover` again with the gaps from this readout, or `/manfred-design-research:test-plan` to validate a specific assumption surfaced this week."
