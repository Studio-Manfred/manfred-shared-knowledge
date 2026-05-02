---
name: empathy-map
description: Use when building a Says/Thinks/Does/Feels empathy map from research data. Triggers on "empathy map", "Says/Thinks/Does/Feels", "build empathy", "synthesise the user emotionally", "what does the user feel", "empathy quadrants".
---

# empathy-map

A 4-quadrant Says / Thinks / Does / Feels map, grounded in research evidence — not in team imagination.

## Overview

Empathy maps are useful when grounded in real research and dangerous when fabricated. The danger is the same as personas: the team mistakes "what we wrote in the quadrants" for "what we know about the user."

This skill builds an empathy map from interview summaries, ticket clusters, observation notes — *not from a team brainstorm with no data*. Says + Does are observable (verbatim quotes, behavioural notes). Thinks + Feels are inferences — labelled as such. Where you have no data, you say "no data" rather than fill the quadrant with hopes.

## When to use

- 3+ interview summaries from a coherent segment exist
- The team needs a shared mental model of a specific user before designing
- Pairs with `manfred-design-research:user-archetype` (one empathy map per archetype)

**Skip when:**

- The team has zero research data — go do interviews first; an empathy map without data is a wish list
- You need to plan UX flow — use `manfred-design-research:journey-map` instead

## Two principles drive everything

1. **Says + Does are evidence; Thinks + Feels are inference.** Mark them differently in the output. Says/Does = verbatim with source. Thinks/Feels = inference with confidence rating.
2. **Empty quadrant > fabricated quadrant.** If you don't have evidence for what the user thinks or feels in a given context, write "no data — needs research" instead of inventing.

## Phase 1 — Pre-flight

- **Source data:** at least 3 interview summaries (from `manfred-design-research:summarize-interview`) for the segment, OR equivalent body of evidence (ticket clusters, observation notes)
- **Segment / archetype:** specific. "Small business owners" is too broad — "Solo invoice-issuing freelancers in their first year" is usable.
- **Output path:** `discovery/empathy-maps/<segment-slug>-<YYYY-MM-DD>.md`

## Phase 2 — Fill the quadrants

For each quadrant, work through the source data:

| Quadrant | Type | Format |
|----------|------|--------|
| **Says** | Observable (verbatim) | "[exact quote]" — [interview-3, 14:22] |
| **Does** | Observable (behaviour) | [observed/reported behaviour] — [source] |
| **Thinks** | Inference | [inferred thought, in their voice] — Confidence: H/M/L — [reason] |
| **Feels** | Inference | [inferred emotion / sensation] — Confidence: H/M/L — [reason] |

If a quadrant ends up with 0 entries: write "**No data — needs research**" plus a one-line note on what to ask in the next interview cycle.

## Phase 3 — Add Goals + Pain points + Inclusion notes

Below the four quadrants, three short sections:

- **Goals** — what is this user trying to achieve? (functional, emotional, social — bridge to `manfred-design-research:jobs-to-be-done`)
- **Pain points** — concrete frustrations, with source
- **Accessibility / inclusion notes** — does this segment include disabled users, AT users, neurodivergent users, non-native-language users? If yes, what specifically did they say or do? (Per Manfred design principle 5.) If no data on this — "needs research" goes here too.

## Phase 4 — Output

Save to `discovery/empathy-maps/<segment-slug>-<YYYY-MM-DD>.md`:

```markdown
# Empathy map — [Segment / archetype name]

**Date:** [YYYY-MM-DD]
**Segment:** [specific behavioural definition]
**Sources:** [N interviews / data points]
**Synthesised by:** [Trio names]

## Says (verbatim)

- "[Quote]" — [interview-3, 14:22]
- "[Quote]" — [interview-5, 27:10]
- [...]

## Does (observable / reported behaviour)

- [Behaviour] — [interview-3]
- [Behaviour from analytics / observation] — [source]
- [...]

## Thinks (inference)

- [Inferred thought, in their voice if possible] — Confidence: H/M/L ([reason])
- [...]
- _OR: "No data — needs research. Probe in next interview: [question]."_

## Feels (inference)

- [Inferred emotion] — Confidence: H/M/L ([reason])
- [...]
- _OR: "No data — needs research."_

## Goals

- **Functional:** [what they're trying to get done]
- **Emotional:** [how they want to feel]
- **Social:** [how they want to be perceived]

## Pain points

- [Concrete pain — verbatim quote if available] — [source]
- [...]

## Accessibility / inclusion notes

- [Specific notes about disabled / AT / neurodivergent / non-native-language users in this segment, with source]
- _OR: "No data on accessibility for this segment — recruit needs to include disabled / AT users in next cycle."_

## What this map is NOT

- A persona substitute (use `manfred-design-research:user-archetype` for that)
- A complete picture (it's specific to a moment / context)
- A reason to skip more research

## Linked artifacts

- Source summaries: [paths]
- Linked archetype: [path]
- Linked OST opportunity: [link]
```

## Manfred lens

- **Customer-driven always** (principle 1) — quadrants are evidence-grounded, not team-imagined
- **Accessible first** (principle 5) — explicit accessibility/inclusion section, not afterthought
- **Craft seriously** (principle 3) — confidence ratings on inferences, not hand-waving
- **Critical & ethical design** (principle 6) — empathy maps consider how the design might fail this segment, not just succeed for them

## Cross-plugin handoffs

- **Input from `manfred-design-research:summarize-interview`** — the source quotes and behavioural observations
- **Input from `manfred-design-research:affinity-diagram`** — themes inform the inference layers
- **Output to `manfred-design-research:user-archetype`** — empathy maps support archetype dimensions
- **Output to `manfred-design-research:journey-map`** — Feels populates the emotional curve
- **Output to `manfred-discovery:opportunity-solution-tree`** — pain points become opportunities

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Just fill in what we think — saves time" | Fabricated empathy maps are worse than no map. They create false consensus. Source-grounded only. |
| "Confidence ratings on inferences are tedious" | The reason for the rating is the value. Even a one-word reason. |
| "Skip the accessibility section unless it came up" | If it didn't come up, the recruit wasn't inclusive enough — that's a finding worth surfacing. |
| "Says/Thinks/Does/Feels are all the same — just fill any quadrant with whatever fits" | They're different epistemological categories. Says/Does = observable. Thinks/Feels = inferred. Marking them differently is the discipline. |
| "Empty quadrant looks bad in the deliverable" | An empty quadrant marked 'needs research' looks like honest research. A filled quadrant from imagination looks like consultancy. |

## Red flags — STOP

- About to fill Thinks/Feels without source data → Stop. Mark "no data — needs research."
- About to fabricate quotes for the Says quadrant → Stop. Verbatim or empty.
- About to skip the accessibility section → Stop. Either name what you found or surface the gap.
- About to build an empathy map for a segment with <3 interviews → Stop. Run more interviews first.

## Tools used

- **Read**: source interview summaries
- **Write**: `discovery/empathy-maps/<slug>-<date>.md`
- **Skills called**:
  - `manfred-design-research:user-archetype` — empathy maps support archetype detail
  - `manfred-design-research:journey-map` — Feels feeds the emotional curve
  - `manfred-discovery:opportunity-solution-tree` — pain points become opportunities

---

*Adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT). Says/Does vs Thinks/Feels epistemic distinction, "empty > fabricated" discipline, accessibility section, and Manfred grounding are original.*
