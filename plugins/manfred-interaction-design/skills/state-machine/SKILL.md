---
name: state-machine
description: Use when modeling complex UI behaviour as states + transitions — anyone says "model the states", "state diagram", "what states does this component have", "finite state machine", "XState", "impossible states", "wizard flow", "form state model", "loading/success/error states". Manfred-flavoured: discriminated-union pattern over boolean soup; every state has a way out; entry/exit actions explicit.
---

# state-machine

A state machine is a way to say: this component / flow can only be in one of these specific states at a time, and it gets between them only through these specific transitions. The benefit is that "loading + error simultaneously" or "submitted + still editing" become impossible by construction, not by careful guarding.

Manfred defaults:

- **Discriminated unions over boolean soup.** `{ status: 'loading' } | { status: 'success', data } | { status: 'error', error }` not `{ isLoading: bool, isError: bool, data?, error? }`.
- **Every state has a way out.** No dead ends. Even terminal states have a "reset" or "navigate away" transition.
- **One state machine per concern.** A wizard's step state and a single field's validation state are separate machines, not one giant blob.
- **Entry / exit actions explicit.** What runs when entering loading? Cancelling on exit? Spell it out.

## When to use

- Modelling a complex component (form with multi-step validation, media player, wizard, multi-pane editor)
- Resolving "this UI has weird bugs in edge cases" (usually = impossible-state bugs)
- Designing a flow that needs alignment with engineering before implementation
- Pairing with `manfred-interaction-design:loading-states` + `manfred-interaction-design:error-handling-ux` to close all the paths

**Skip when:**

- The component has 2 states (open / closed). A boolean is fine — don't over-engineer.
- The user wants the visual design — that's `manfred-ui-design:design-screen`
- The user wants a backend workflow / orchestration — that's a different problem; this skill is UI-only

## When a state machine pays off

| Signal | Likely worth modelling |
|---|---|
| 4+ distinct UI modes | Yes |
| Multiple async events that affect state | Yes |
| "We keep finding edge cases that show wrong UI" | Yes — impossible-state bugs |
| Multi-step flow with branches | Yes |
| Component shared across teams that need an interface contract | Yes |
| Toggle / boolean state | No — overkill |
| Pure presentation component | No |

## The components

| Term | What it is |
|---|---|
| **State** | A distinct mode the UI can be in (`idle`, `loading`, `success`, `error`, `editing`, `submitting`). Mutually exclusive — only one at a time. |
| **Event** | Something that triggers a transition (`SUBMIT`, `RESPONSE_RECEIVED`, `RETRY`, `CANCEL`, `TIMEOUT`). Past-tense or imperative. |
| **Transition** | A rule: "in state A, on event X, go to state B (with side effects)". |
| **Guard** | A condition that gates a transition (`isFormValid`, `hasPermission`, `attempt < MAX`). Without it the transition doesn't fire. |
| **Action** | A side effect during a transition (`fetchData`, `showToast`, `logEvent`, `cancelInflight`). |
| **Entry / exit action** | Runs when entering / leaving a state. (Entry `loading`: start spinner. Exit `loading`: clear timeout.) |
| **Context** | Data that travels with the machine (form values, attempt count, error). Lives outside the state but updates with transitions. |

## The flow

### Step 1 — List every state

Brainstorm exhaustively before pruning. For a form:

- `idle`, `editing`, `validating`, `submitting`, `success`, `error`, `retrying`

Then prune to the smallest set that maps to distinct UI. Maybe `editing` and `validating` collapse if they look the same. Maybe `retrying` is just `submitting` with an attempt counter.

### Step 2 — List every event

Events come from three sources:

- **User actions**: `SUBMIT`, `EDIT`, `CANCEL`, `RETRY`, `RESET`
- **System events**: `RESPONSE_OK`, `RESPONSE_ERROR`, `TIMEOUT`, `NETWORK_LOST`
- **Conditions**: `INACTIVITY_5MIN`, `THRESHOLD_REACHED`

Past-tense for things that happened (`RESPONSE_OK`); imperative for user intents (`SUBMIT`, `CANCEL`).

### Step 3 — Define transitions

For every (state, event) pair: where do we go? Or — does the event do nothing?

```
idle       + EDIT          → editing
editing    + SUBMIT        → validating       (action: validateForm)
validating + VALID         → submitting       (action: callApi)
validating + INVALID       → editing          (action: showFieldErrors)
submitting + RESPONSE_OK   → success
submitting + RESPONSE_ERR  → error            (context: store error)
submitting + TIMEOUT       → error            (context: store timeout)
error      + RETRY         → submitting       (guard: attempt < MAX)
error      + RESET         → idle             (action: clearForm)
success    + RESET         → idle
```

Anything not listed is *impossible* — the event in that state is ignored or treated as a bug.

### Step 4 — Identify impossible states

Re-read the matrix. What's NOT listed?

- `loading + error simultaneously` → impossible (mutex by state)
- `submitting + editing` → impossible (no `EDIT` transition from `submitting`)
- `success + retry` → impossible (no `RETRY` from `success`)

The point of the model is that this list isn't theoretical — those bugs *cannot* happen.

### Step 5 — Add guards

Some transitions only fire if a condition holds:

```
error + RETRY → submitting [guard: attempt < MAX_ATTEMPTS]
error + RETRY → error (no-op, message: "Max retries exceeded") [guard: attempt >= MAX]
```

Make the guard explicit so engineering doesn't have to infer it.

### Step 6 — Add entry / exit actions

What side effects run on entry / exit?

- **Entry `loading`**: start request, start timeout
- **Exit `loading`**: clear timeout
- **Entry `error`**: log error, increment attempt counter, focus the retry button
- **Entry `success`**: emit success event, optionally reset after 3s
- **Exit `editing` (to `submitting`)**: snapshot form values into context

These are the things that always need to happen at that boundary, and forgetting them in code is where bugs live.

### Step 7 — Map states to UI

For each state, what does the user see?

```
idle       → empty form, primary button enabled
editing    → form with current input, button enabled
validating → form locked, inline spinner on button
submitting → form locked, full button spinner, "Submitting…"
success    → success state UI, "Done" or "Submit another"
error      → form unlocked, error banner via manfred-interaction-design:error-handling-ux, retry button
```

If two states map to identical UI — collapse them. If one state needs *contextual* UI (different errors look different), that lives in `context`, not as separate states.

## Output format

```markdown
## State machine: <component / flow name>

### Context (data carried)
- <name>: <type> — <purpose>

### States
- `idle`
- `editing`
- ...

### Events
- User: `SUBMIT`, `RESET`, `RETRY`
- System: `RESPONSE_OK`, `RESPONSE_ERR`, `TIMEOUT`

### Transitions

| From | Event | Guard | Action | To |
|---|---|---|---|---|
| idle | EDIT | — | — | editing |
| editing | SUBMIT | — | validateForm | validating |
| ... | ... | ... | ... | ... |

### Entry / exit actions
- Entry `loading`: startRequest, startTimeout
- Exit `loading`: clearTimeout
- ...

### UI per state
- `idle`: empty form
- `editing`: form with input
- ...

### Impossible states (verified)
- loading + error
- submitting + editing
- success + retry

### Diagram
[Optional Mermaid / XState diagram]
```

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Just use booleans — state machines are overkill." | For 2 states, yes. For 4+ async-influenced states, the boolean version is where bugs hide. |
| "We don't need to model exit actions." | Forgetting to clear a timeout on state exit is the #1 source of leaked async bugs. Model them. |
| "One big state machine for the whole feature." | Separate concerns. Form-state and modal-state are independent — separate machines. |
| "We'll just track `isLoading` and `error` and figure out the UI." | "Figure out" = ad-hoc guards in JSX = unreachable states reachable. Model first, code second. |

## Red flags — STOP

- A state can't transition to anything (dead end with no `RESET` / `BACK`).
- Two states have identical UI and identical transitions (collapse them).
- The same event in the same state is handled differently in different places (move to a guard).
- Ad-hoc "if this and that and not that" guards in the UI code instead of model-level guards.
- No defined behaviour for failure modes (timeout, network drop, server 5xx).

## Manfred lens

Skip Cagan / Torres — state modelling is execution craft. Exception: if state-modelling reveals a flow can't actually express the desired user journey (e.g. "user wants to pause mid-checkout" but no `PAUSE` event exists in any state), that's an **opportunity** — surface and route to `manfred-discovery:opportunity-solution-tree`.

## Cross-references

- `manfred-interaction-design:loading-states` — for the loading state's UI design
- `manfred-interaction-design:error-handling-ux` — for the error states' UI + recovery
- `manfred-interaction-design:micro-interaction-spec` — for individual transitions inside the machine
- `manfred-interaction-design:feedback-patterns` — for transition feedback channels
- `manfred-design-systems:component-spec` — when this state machine becomes a documented component
- XState (https://xstate.js.org/) — the most-adopted JS library for executable state machines if you want to ship the model as code

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, discriminated-union framing, entry/exit-action emphasis, and Manfred-specific guidance are original.*
