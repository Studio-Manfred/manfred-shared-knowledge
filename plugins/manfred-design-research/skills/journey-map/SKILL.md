---
name: journey-map
description: Use when mapping a user's end-to-end experience across stages, touchpoints, emotions, pain points, and opportunity areas. Triggers on "journey map", "experience map", "stages and touchpoints", "moments of truth", "user journey", "customer journey", "service blueprint" (related but different).
---

# journey-map

Maps a specific user (or archetype) across the full sequence of stages and touchpoints, with the emotional curve grounded in research and the moments of truth flagged. Includes the question most journey maps skip: where could this design *do harm*.

## Overview

Journey maps fail when the emotional curve is invented (rather than evidence-grounded), when stages are too generic to be actionable, or when "opportunity areas" become a wishlist of features. Done well, they make a user's whole experience legible to the team in one artifact and surface specific moments where small design changes have outsized impact.

This skill is for **persona-grounded journey maps** — one map per archetype, not one map for "the user." Generic journeys hide the variation that matters.

Source: Indi Young, Adaptive Path / Jim Kalbach (*Mapping Experiences*); the Manfred ethical-design lens adds the "where could this harm?" question.

## When to use

- Need to make a user's full experience visible to the team
- Designing a multi-stage flow (signup-through-first-value, complaint-through-resolution, etc.)
- Surfacing where the team's mental model diverges from the user's actual experience
- Pairs with `manfred-design-research:user-archetype` (one journey per archetype)

**Skip when:**

- The "journey" is single-screen — use `manfred-design-research:usability-test-plan` instead
- You don't have research data for the segment — go do interviews first
- Mapping internal/employee experience — use service blueprint instead (different artifact)

## Two principles drive everything

1. **One archetype, one journey.** Don't try to map the average user. Map one specific archetype's experience. If you have multiple archetypes, run this skill multiple times.
2. **Emotional curve = data, not vibes.** Every emotional rating must have a source — a quote, a behavioural observation, a survey signal. Inferences are labelled as inferences with confidence ratings.

## Phase 1 — Pre-flight

- **Linked archetype:** which `manfred-design-research:user-archetype` does this map serve? (If "all users" — stop, pick one.)
- **Scope of the journey:** start point and end point. "Awareness through first paid invoice" is scoped. "Using our app" is not.
- **Source data:** interview summaries, support tickets, analytics, NPS. Confirm enough exists.
- **Output path:** `discovery/journeys/<archetype-slug>-<scope-slug>-<YYYY-MM-DD>.md`

## Phase 2 — Define stages

5–7 stages from start to end. Stage boundaries are usually transitions in:

- Goal (what the user is trying to do shifts)
- Mode (e.g. evaluating → committed → using)
- Emotional state (e.g. excited → frustrated → resigned)

Common stage frames:

- **Awareness → Consideration → Decision → Onboarding → First Value → Habitual Use → Advocacy** (acquisition-style)
- **Trigger → Search → Evaluate → Purchase → Receive → Use → Reflect** (purchase-style)
- **Notice problem → Try DIY → Seek help → Get resolution → Reflect** (support-style)

Don't force a frame. Let the actual journey define the stages.

## Phase 3 — For each stage, capture

| Field | What goes here |
|-------|----------------|
| **Goal** | What is the user trying to do at this stage? In their voice. |
| **Actions** | What do they actually do? Concrete, observable, source-cited. |
| **Touchpoints** | Where they encounter your product / service (and competitors / alternatives) |
| **Thoughts** | Inferred — what's going through their mind. Confidence H/M/L. |
| **Feelings** | Source-grounded emotion + intensity (1–5 scale or descriptor). Source: quote, behaviour, survey. |
| **Pain points** | Where it breaks. Concrete, source-cited. |
| **Opportunities** | Where small design changes could matter (not feature wishlist) |

## Phase 4 — Draw the emotional curve

For each stage, plot the user's emotional state on a 1–5 scale (1 = bottom, 5 = top). Connect into a curve.

Read the curve for:

- **Drops** (a stage where emotion sinks) — usually pain points worth addressing
- **Peaks** (a stage where emotion is highest) — moments worth amplifying
- **Flatlines** (sustained low) — usually a sign the user is checking out

**The data discipline:** every point on the curve must be supported by source evidence. "Stage 3 drops to 2/5" needs a quote, a behavioural observation, or a survey signal — not "we think they'd be frustrated."

## Phase 5 — Identify moments of truth

Moments of truth are stages or transitions where the user's relationship with the product is decisively shaped — make-or-break moments. They get more design attention than ordinary stages.

Common patterns:

- **First-value moment** — the first time the user gets the core value. Massive predictor of retention.
- **First-failure moment** — the first time the product disappoints. Predictor of churn.
- **First-shared moment** — when the user first tells someone else about the product (positive or negative).
- **First-recovery moment** — the first time something went wrong and the team made it right.

Mark moments of truth on the journey explicitly.

## Phase 6 — The Manfred question: where could this harm?

For each stage, ask: **what does this design do in the world for this user?** (Per Manfred design principle 6.)

- **Coercion risks** — where does the design pressure / nudge in ways that don't serve the user?
- **Exclusion risks** — where does the design exclude disabled users, low-bandwidth users, low-literacy users, non-native-language users?
- **Privacy risks** — where does the user surface data they may not realise is captured?
- **Cognitive load risks** — where is the cognitive cost disproportionate to the benefit?

This isn't a checklist; it's a thinking prompt. If a stage has no harm risk identified, write "Reviewed — no harm risks identified for this stage" so the team sees the question was asked.

## Phase 7 — Output

Save to `discovery/journeys/<archetype-slug>-<scope-slug>-<YYYY-MM-DD>.md`:

```markdown
# Journey map — [Archetype name], [Journey scope]

**Date:** [YYYY-MM-DD]
**Archetype:** [link to archetype file]
**Scope:** [start point → end point]
**Sources:** [N interviews / data points]

## Stages

### Stage 1 — [Name]

- **Goal:** [in user voice]
- **Actions:** [concrete] — [source]
- **Touchpoints:** [where they encounter the product / alternatives]
- **Thoughts:** [inferred] — Confidence: H/M/L
- **Feelings:** [grounded — quote / behaviour / survey] — Intensity: [1–5]
- **Pain points:** [concrete] — [source]
- **Opportunities:** [design changes worth considering]
- **Harm review:** [coercion / exclusion / privacy / cognitive load risks, OR "Reviewed — no harm risks identified"]

### Stage 2 — [...]
[...]

## Emotional curve

```
5  ┤            ●
4  ┤        ●       ●
3  ┤    ●               ●
2  ┤●                       ●
1  ┤                            ●
   └─────────────────────────────
   S1  S2  S3  S4  S5  S6  S7
```

(ASCII OK; otherwise reference the source data table.)

## Moments of truth

- **[Stage X — first-value moment]** — [why this matters; what the team should attend to]
- **[Stage Y — first-failure moment]** — [...]

## Top opportunities (for the OST)

- **[Opportunity 1]** — at stage [X] — addresses pain point [P] — links to OST opportunity [...]
- **[Opportunity 2]** — [...]

## Cross-cutting harm risks

- [Any harm risks that span multiple stages — e.g. "data capture pattern across stages 2–5 may exceed what user expects"]

## Linked artifacts

- Source archetype: [path]
- Source summaries: [paths]
- Linked OST opportunities: [links]
```

If a Linear ticket is linked, post the moments of truth + top opportunities as a Linear comment.

## Manfred lens

- **Customer-driven always** (principle 1) — journey starts from user goal, not product flow
- **Research isn't a phase** (principle 2) — emotional curve is data; updated as new research comes in
- **Critical & ethical design** (principle 6) — explicit harm review at every stage
- **Accessible first** (principle 5) — exclusion risks surfaced explicitly per stage
- **Craft seriously** (principle 3) — confidence ratings on inferences; precision over generic stage labels

## Cross-plugin handoffs

- **Input from `manfred-design-research:user-archetype`** — one journey per archetype
- **Input from `manfred-design-research:summarize-interview`** — Findings + Pain points feed stages
- **Input from `manfred-design-research:affinity-diagram`** — themes inform what the journey emphasises
- **Input from `manfred-design-research:jobs-to-be-done`** — lifecycle stages can mirror JTBD stages
- **Output to `manfred-discovery:opportunity-solution-tree`** — opportunities become OST entries
- **Output to `manfred-design-research:usability-test-plan`** — moments of truth become tasks to test
- **Output to `manfred-design-ops:handoff-spec`** — when designing a specific stage

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Map the average user — too many archetypes for separate maps" | Average users hide the variation. One map per archetype. If too many archetypes, that's an archetype problem — consolidate. |
| "Make up the emotional curve — we know what they feel" | Then the curve is fiction. Either ground in data or label as inference. |
| "Skip the harm review — out of scope" | It's not out of scope. Manfred principle 6 applies to every design artifact. |
| "Opportunities can be 'add a dashboard'" | That's a feature wishlist. Opportunities are 'address pain X at stage Y' — feature comes later. |
| "Stages should be the same as our funnel" | Funnels are team views. Journeys are user views. They often diverge — note where. |

## Red flags — STOP

- About to map a generic "user" instead of a specific archetype → Stop. Pick one archetype.
- About to invent emotional ratings without source → Stop. Either find the data or mark as inference with low confidence.
- About to skip the harm review section → Stop. At minimum write "Reviewed — no harm risks identified" per stage.
- About to make opportunities feature-shaped → Stop. Reframe as pain-at-stage.
- About to use the team's funnel stages instead of the user's actual journey → Stop. Where do they diverge?

## Tools used

- **Write**: `discovery/journeys/<slug>-<date>.md`
- **MCP** (when ticket linked): `mcp__linear-server__get_issue`, `mcp__linear-server__save_comment`
- **Skills called**:
  - `manfred-design-research:user-archetype` — the archetype the journey maps
  - `manfred-discovery:opportunity-solution-tree` — opportunities become OST entries
  - `manfred-design-research:usability-test-plan` — moments of truth become tasks
- **Reference**: Indi Young; Jim Kalbach, *Mapping Experiences*; Kerry Bodine

---

*Adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT). One-archetype-per-journey discipline, evidence-grounded emotional curve, harm review section (Manfred principle 6), and accessibility-as-stage-attribute are original.*
