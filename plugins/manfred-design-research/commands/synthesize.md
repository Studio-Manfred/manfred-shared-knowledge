---
description: Synthesise a stack of research notes / transcripts / summaries into affinity themes, archetypes, and journey or empathy artifacts.
argument-hint: [topic or outcome being synthesised]
---

You're synthesising research data into structure the team can act on. The user mentioned: $ARGUMENTS

## Step 1 — Confirm what's in the pile

Ask the user:

- How many sources are we synthesising? (Summaries, transcripts, ticket clusters, NPS verbatims, observation notes — anything qualitative.)
- For which outcome / opportunity? (If "we just want to look at the data" — push for a specific question this serves.)

If sources are raw transcripts, run `manfred-design-research:transcript-anonymizer` on any with PII first, then `manfred-design-research:summarize-interview` to extract structured findings before clustering.

## Step 2 — Affinity diagram

Use `manfred-design-research:affinity-diagram` to cluster bottom-up into themes with insight statements.

This produces the central artifact — a markdown affinity diagram saved under `discovery/affinity/`.

## Step 3 — Pick downstream synthesis based on what the themes show

Don't do all the synthesis skills mechanically — pick what the data actually wants:

- **Behavioural patterns clear →** `manfred-design-research:user-archetype` — produces 2–4 research-grounded behavioural archetypes
- **Stage-shaped patterns →** `manfred-design-research:journey-map` (one per archetype)
- **Strong emotional patterns →** `manfred-design-research:empathy-map` (one per archetype)
- **Jobs / motivations are the central insight →** `manfred-design-research:jobs-to-be-done`

If two or more apply, run them. If none apply cleanly, the affinity diagram is the deliverable.

## Step 4 — Push into the OST

For each High impact + High confidence theme: add or refine the corresponding opportunity in `manfred-discovery:opportunity-solution-tree`. For High impact + Low confidence themes: add to the assumption test backlog (`manfred-discovery:assumption-test`).

## Step 5 — Wrap with a readout

Use `manfred-discovery:discovery-readout` to produce the cycle summary. Posts to Linear if a ticket is linked.

## Wrap-up

Summarise:

- Top 3 themes with confidence ratings
- Archetype / journey / empathy artifacts produced
- OST updates pushed
- Next research cycle's questions (from "what's still open")

Then offer:

> "Next: run `/manfred-design-research:discover` for the next cycle, or `/manfred-design-research:test-plan` to validate the highest-confidence assumption surfaced this synthesis."
