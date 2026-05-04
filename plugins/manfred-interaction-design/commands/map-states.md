---
description: Model the states + transitions for a complex UI component or flow — chains state-machine + loading + error + feedback + animation specs per state.
argument-hint: [component or flow name, e.g. "media player" or "multi-step checkout" or "calendar editor"]
---

You're modelling the state machine for a component or flow. The user mentioned: $ARGUMENTS

This is the orchestrator — it walks the state-machine skill plus the per-state specs (loading, error, feedback, animation) so the output is a complete, executable model with no holes.

## Step 1 — Confirm scope

Ask:

- **What's the unit?** Single component or multi-step flow?
- **Linear ticket?** (`STU-XXX`)
- **Async involved?** (Affects whether `manfred-interaction-design:loading-states` is in scope.)
- **Failure modes possible?** (Affects whether `manfred-interaction-design:error-handling-ux` is in scope — it almost always is.)
- **Multi-pane / multi-screen?** (Affects whether multiple state machines should be modelled separately.)

Rule: one state machine per concern. If the user describes "checkout" as one big flow, ask whether cart-state, payment-state, and review-state should be separate machines (usually yes).

## Step 2 — Identify states (`manfred-interaction-design:state-machine`)

Brainstorm exhaustively before pruning.

For a typical flow: idle, editing, validating, submitting, retrying, success, error, recovered, abandoned.

Then prune to the smallest set that maps to *distinct UI*. Two states with identical UI + identical transitions → collapse them. State-with-context (different errors, same shape) → context, not separate states.

## Step 3 — Map transitions

For every (state, event) pair: where do we go?

Build the matrix. Anything not listed is impossible — that's the point.

Sources of events:

- **User**: `SUBMIT`, `EDIT`, `CANCEL`, `RETRY`, `RESET`, `BACK`
- **System**: `RESPONSE_OK`, `RESPONSE_ERR`, `TIMEOUT`, `NETWORK_LOST`, `AUTH_EXPIRED`
- **Conditions**: `INACTIVITY_5MIN`, `THRESHOLD_REACHED`

Add **guards** for conditional transitions (`attempt < MAX`, `isFormValid`, `hasPermission`).

Add **entry / exit actions** per state (start spinner on entry, clear timeout on exit, etc).

## Step 4 — Define loading states (`manfred-interaction-design:loading-states`)

For every state involving an async wait:

- Pattern: skeleton / spinner / progress / optimistic / last-known
- Duration thresholds (when does it switch from "fast" to "slow" UX?)
- Reduced-motion fallback for shimmer animations
- Cancel / abort behaviour for long waits
- Optimistic UI rollback path (if applicable — paired with state-machine)

## Step 5 — Define error states (`manfred-interaction-design:error-handling-ux`)

For every state that can fail or for a dedicated `error` state:

- Per failure mode (run pre-flight): surface, recovery, state preservation, focus, ARIA, animation
- Auto-retry policy if applicable (transient modes only, with idempotency)
- Copy handoff requests for `manfred-toolkit:ux-writing` (one per mode — never write copy here)

## Step 6 — Define feedback per transition (`manfred-interaction-design:feedback-patterns`)

For each transition the user should perceive:

- Channel: inline / component / page / system
- Timing: immediate / debounced / on-completion
- Auto-dismissal vs persistent
- ARIA `role` (`status` for confirmations, `alert` for errors)

## Step 7 — Define animations per transition (`manfred-interaction-design:animation-principles`)

For each animated transition:

- Duration + easing (use design-system motion tokens; flag for `manfred-design-systems:design-token` if missing)
- Stagger if multiple elements
- Reduced-motion fallback (always)
- Performance budget (transform / opacity preferred; layout properties flagged)

## Step 8 — Verify impossible states

Re-read the matrix. List what *can't* happen:

- `loading + error` simultaneous?
- `submitting + editing` simultaneous?
- `success + retry` reachable?

If any "impossible" state can be reached via some path — that's a bug in the model. Fix.

## Step 9 — Map states to UI

For each state: what does the user see?

- Empty state, populated state, locked state, error variants
- Per-state copy via `manfred-toolkit:ux-writing` (route, don't write)
- a11y: per-state ARIA + focus rules

If two states map to identical UI → collapse them.

## Step 10 — Document

Save to:

```
docs/state-machines/<component-slug>-<YYYY-MM-DD>.md
```

Format:

```markdown
# State machine — <component / flow>

**Date**: YYYY-MM-DD
**Linear**: STU-XXX

## Context (data carried)
- <name>: <type> — <purpose>

## States
- `idle`, `editing`, `loading`, `success`, `error`, ...

## Events
- User: ...
- System: ...
- Conditions: ...

## Transitions
[matrix: From | Event | Guard | Action | To]

## Entry / exit actions
[per state]

## Loading states
[per async transition — pattern + thresholds + reduced-motion]

## Error states
[per failure mode — surface + recovery + state preservation + ARIA + focus + copy handoff]

## Feedback per transition
[channel + timing + ARIA]

## Animation per transition
[duration + easing + reduced-motion]

## UI per state
[what the user sees]

## Impossible states (verified)
[list — these cannot be reached by construction]

## Diagram
[Optional Mermaid / XState code]

## Cross-plugin handoffs
- copy: `manfred-toolkit:ux-writing` (per surface)
- a11y verification: `manfred-design-systems:a11y-qa`
- token additions: `manfred-design-systems:design-token`
```

## Step 11 — Linear update

Post via `mcp__linear-server__save_comment`:

- Path to the model doc
- Summary: state count, transition count, error modes covered, impossible states verified
- Outstanding decisions

## Wrap-up checklist

- [ ] Every state has at least one way out
- [ ] Every state has UI defined (or explicit "same as state X")
- [ ] Every transition has guard + action explicit (or "none")
- [ ] Entry / exit actions defined where side effects exist
- [ ] Loading states designed per async wait
- [ ] Error states designed per failure mode (no "just throw an error")
- [ ] Reduced-motion fallback for every animation
- [ ] Impossible states listed + verified unreachable
- [ ] Copy handoff requests for every user-facing surface (`manfred-toolkit:ux-writing`)
- [ ] Linear comment posted

Then offer:

> "For full interaction spec, run `/manfred-interaction-design:design-interaction`. For deep error-flow work on the failure modes, run `/manfred-interaction-design:error-flow`."
