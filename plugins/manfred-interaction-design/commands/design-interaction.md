---
description: Design a complete interaction flow for a feature or component — chains state model + micro-interactions + animation + gestures + feedback + error + loading.
argument-hint: [feature or component, e.g. "drag-to-reorder list" or "checkout review step"]
---

You're designing a complete interaction. The user mentioned: $ARGUMENTS

This is the orchestrator — it walks through every layer of the interaction in order, calling the relevant skill for each. Do not invent rules here; defer to the skill at every step.

## Step 1 — Confirm scope

Ask:

- **What's the unit?** A single component, a multi-step flow, a screen, or a feature crossing multiple screens?
- **Linear ticket?** (`STU-XXX`)
- **Existing implementation to revise**, or **net new**?
- **Touch / pointer / both?** (Affects whether `gesture-patterns` is in scope.)
- **Critical path?** (Affects whether `manfred-discovery:cagan-risks` should be looped in.)

If the unit is huge (whole-app interaction model), break it down before continuing — this command is for one bounded interaction at a time.

## Step 2 — Model the states (`manfred-interaction-design:state-machine`)

Run the state-machine skill. Outputs:

- Full state list (idle / editing / loading / success / error / etc)
- Event list (user + system + conditions)
- Transition matrix (from / event / guard / action / to)
- Entry / exit actions per state
- UI per state

This gives the *skeleton*. Everything else hangs off it.

## Step 3 — Spec each micro-interaction (`manfred-interaction-design:micro-interaction-spec`)

For every transition that involves user action: spec the micro-interaction (trigger / rules / feedback / loops). Don't spec the obvious ones (page navigation) — focus on the ones that need design judgement (toggle, swipe, like, confirm).

## Step 4 — Define motion (`manfred-interaction-design:animation-principles`)

For every animated transition: pick duration, easing, stagger. Use design-system motion tokens if they exist; flag for `manfred-design-systems:design-token` to add them if they don't.

`prefers-reduced-motion` fallback for every animation. Non-negotiable.

## Step 5 — Design gestures if applicable (`manfred-interaction-design:gesture-patterns`)

Only if touch is in scope. For each gesture: trigger, threshold, affordance, non-gesture alternative, conflict resolution, accessibility.

## Step 6 — Specify feedback channels (`manfred-interaction-design:feedback-patterns`)

For every state change the user should perceive: pick the channel (inline / component / page / system) and the timing. Route the actual *copy* to `manfred-toolkit:ux-writing` — don't write words here.

## Step 7 — Design error paths (`manfred-interaction-design:error-handling-ux`)

For every state that can fail: prevention layer, detection layer, communication layer (surface + ARIA + focus), recovery layer (retry / fallback / save-draft). State preservation rules. Hand off copy to `manfred-toolkit:ux-writing` with structured context.

## Step 8 — Design loading states (`manfred-interaction-design:loading-states`)

For every async transition: pick the pattern (skeleton / spinner / progress / optimistic). Honour reduced-motion. No blank screens. Match skeleton shape to loaded layout.

## Step 9 — Cross-cutting concerns

- **Accessibility** — pair with `manfred-design-systems:a11y-design` for ARIA pattern; verify with `manfred-design-systems:a11y-qa` post-implementation
- **Tokens** — verify everything visual references `~/.claude/shared/DESIGN.md` tokens; flag bypasses for `manfred-toolkit:design-token-audit`
- **Discovery risks** — for critical-path interactions, route to `manfred-discovery:cagan-risks` to flag usability/feasibility/viability concerns

## Step 10 — Document

Save the full interaction spec to:

```
docs/interactions/<feature-slug>-<YYYY-MM-DD>.md
```

Format:

```markdown
# Interaction spec — <feature>

**Date**: YYYY-MM-DD
**Linear**: STU-XXX
**Scope**: <component / flow / feature>

## State machine
[output from Step 2]

## Micro-interactions
[Step 3 output, one per spec]

## Motion
[Step 4 — table of animations + tokens used]

## Gestures (if applicable)
[Step 5 output]

## Feedback channels
[Step 6 — table of surfaces + timing]

## Error paths
[Step 7 — full error UX spec]

## Loading states
[Step 8 — pattern per async transition]

## Copy handoffs
[Structured copy requests for `manfred-toolkit:ux-writing` — one per surface]

## Cross-plugin handoffs
- a11y verification: `manfred-design-systems:a11y-qa`
- token audit: `manfred-toolkit:design-token-audit`
- discovery risks (if critical path): `manfred-discovery:cagan-risks`
```

## Step 11 — Linear update

Post via `mcp__linear-server__save_comment`:

- Path to the spec doc
- Summary: state count, transition count, error modes covered, gestures (if any)
- Cross-plugin handoffs queued
- Outstanding decisions (token additions, copy handoffs, a11y items)

## Wrap-up checklist

- [ ] State machine modelled — impossible states verified
- [ ] Every transition has feedback or motion spec'd (or explicit "none, by design")
- [ ] Reduced-motion fallback for every animation
- [ ] Every gesture has a non-gesture alternative
- [ ] Every error mode has surface + recovery + state-preservation rule
- [ ] No copy invented — all routed to `manfred-toolkit:ux-writing`
- [ ] Tokens used (no inline durations / colours / hex)
- [ ] a11y handoff queued (`manfred-design-systems:a11y-qa`)
- [ ] Linear comment posted

Then offer:

> "For the state model in detail, run `/manfred-interaction-design:map-states`. For the error path in detail, run `/manfred-interaction-design:error-flow`. For copy on every surface, hand off to `manfred-toolkit:ux-writing`."
