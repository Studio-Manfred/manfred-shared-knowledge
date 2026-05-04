---
name: user-flow-diagram
description: Use when mapping a user flow / task flow / wire-flow — anyone says "user flow", "flow diagram", "task flow", "happy path", "decision tree", "branching logic", "where does the user go after X", "wire flow". Manfred-flavoured: happy path first, then branches, then errors; decision criteria explicit at every diamond; map error paths in addition to success (pair with `manfred-interaction-design:error-handling-ux`); one flow per goal.
---

# user-flow-diagram

A user flow is a map of how someone gets from intent to outcome through a product. It surfaces decision points, branches, error paths, and system processes — the things that get hand-waved in feature descriptions and become bugs in production.

Manfred defaults:

- **One flow per user goal.** "Whole app flow" is wallpaper. "User signs up and verifies email" is a flow.
- **Happy path first, then branches, then errors.** Trying to map all paths at once produces unreadable diagrams.
- **Every decision diamond labelled.** A diamond without criteria is a bug-in-waiting.
- **Map error paths.** Pair with `manfred-interaction-design:error-handling-ux` so error states have flow representation, not just visual designs.

## When to use

- Documenting an existing flow (audit, onboarding, hand-off)
- Designing a new flow before screens
- Surfacing decision points and branches in stakeholder discussions
- Pairing with `manfred-interaction-design:state-machine` (flows live "above" state machines — flows are user goals, machines are component states)
- Pairing with `manfred-prototyping-testing:wireframe-spec` for wire-flow (flow + screen thumbnails)

**Skip when:**

- The component is a single screen with no branching — you don't need a flow diagram
- The need is component state modelling — that's `manfred-interaction-design:state-machine`
- The need is a process diagram for engineering (system orchestration) — that's a different artifact

## Flow elements (notation)

| Element | Shape | What it represents |
|---|---|---|
| **Entry point** | Circle / oval | Where the user enters the flow |
| **Screen / page** | Rectangle | A view the user sees |
| **Decision** | Diamond | A branching point — either a user choice or a system condition |
| **User action** | Rounded rectangle | Something the user does (click, type, swipe) |
| **System process** | Rectangle with side bars | Backend operation (API call, calculation, write) |
| **End point** | Circle with border | Flow completion (success or terminal failure) |
| **Connector** | Arrow | Direction of flow; label every arrow with the trigger |

Use consistently. If you're mixing shapes mid-diagram, the diagram is harder to read than the underlying flow.

## Flow types

| Type | What it shows | When |
|---|---|---|
| **Task flow** | Single linear path for one task | Documenting a known flow; happy-path artifact |
| **User flow** | Multiple paths based on user type, choice, or condition | Real flows almost always — mostly never linear |
| **Wire flow** | Flow + wireframe thumbnails next to each step | Stakeholder review, design hand-off |
| **Error flow** | Failure modes + recovery paths (see `manfred-interaction-design:error-flow`) | Pair with main flow; don't bury error paths inside happy path |

## The flow

### Step 1 — Define the goal

Specific, user-stated, single goal. Example:

- ✅ "User signs up for a new account and verifies their email"
- ✅ "Returning user resets their forgotten password"
- ❌ "User uses the app" — too broad
- ❌ "User signs up, verifies email, completes onboarding, makes first purchase" — multiple goals; split

If you can't write the goal in one sentence — split into multiple flows.

### Step 2 — Identify entry points

Where does the user enter? List all:

- Marketing landing page
- Email link
- Push notification deep-link
- In-app banner
- Direct URL
- Returning from offline / interrupted state

Different entries often need different flows (e.g. signup from landing vs from invite-link).

### Step 3 — Map the happy path

Linear, no branches. The 80%-case where everything goes right.

```
[Landing] → (Click "Sign up") → [Sign up form] → (Submit) 
  → {{System: validate + create}} → [Verify email screen] 
  → (Click verify link) → [Welcome screen] → ((Done))
```

This is the spine. Don't add branches yet.

### Step 4 — Add decisions + branches

For every point where the path forks, add a diamond. Label both the *decision criteria* and each branch:

```
                      ┌── (Yes) → [Welcome screen] → ((Done))
[Email verified?] ◇───┤
                      └── (No)  → [Resend / change email] → (Loop back)
```

Each diamond gets:

- **Decision criteria** — what makes the system / user pick a branch (system-driven? user choice? both?)
- **Each branch labelled** — what the answer was

Common branch sources:

- User choice (single sign-on vs email)
- System condition (email already exists? free vs paid plan? user role?)
- Validation state (form valid / invalid)
- External service state (third-party available / down)

### Step 5 — Add error paths

Often skipped. Often where users actually live.

For each step that can fail:

- What's the failure mode? (Network error, validation failure, timeout, third-party down, permission denied — see `manfred-interaction-design:error-handling-ux` for the full list)
- What does the user see?
- What's the recovery path? (Retry / fix / go back / get help / abandon)
- Where do they re-enter the flow?

Pair every meaningful error path with a recovery path. "Show error" is half a flow — the other half is "what happens next".

### Step 6 — Add system actions

Things the user doesn't see directly but matter for understanding:

- Background API calls (e.g. `{{POST /api/signup}}`)
- Async processing (e.g. `{{Send verification email}}`)
- Time delays (e.g. waiting on external service)
- Side effects (e.g. analytics events, notifications to other users)

Engineering needs these on the diagram; they often surface coordination requirements that aren't obvious from the user-facing flow.

### Step 7 — Mark exit points

Every flow ends somewhere. Common exits:

- **Success terminal** — task completed (`((Done))`)
- **Abandonment terminal** — user left mid-flow (back button, close tab, navigate away)
- **Hand-off terminal** — user enters another flow (e.g. signup → onboarding)
- **Error terminal** — unrecoverable failure (rare; usually loop back to recovery)

Without exit points, the diagram is unbounded. Always close the loop.

### Step 8 — Annotate

Add notes for:

- **Time delays** ("Email arrives within 2 min")
- **Async coordination** ("If verify clicked >24h later, link expires → Step X")
- **A/B-test variants** (if the flow forks for an active experiment)
- **Locale differences** (e.g. EN flow shows X step; SV flow skips it)
- **AT-specific paths** (e.g. screen reader users skip a visual step that has no semantic equivalent)

### Step 9 — Validate the flow

Before finalising:

- Walk it as a new user — does anything not make sense?
- Walk it as someone who hits the unhappy path — do recovery routes work?
- Walk it as a screen-reader user — is the path equivalent?
- Walk it on mobile — do interactions translate?
- Show it to engineering — do system actions match what's actually built?

### Step 10 — Document

Save to:

```
docs/user-flows/<flow-slug>-<YYYY-MM-DD>.md
```

Include:

- Diagram (Mermaid / Whimsical / Figma / Lucid — pick a format the team can edit)
- Goal statement
- Entry points
- Happy path (text walkthrough)
- Branch criteria table
- Error / recovery table
- Annotations
- Open questions / decisions pending

```markdown
# User flow — <name>

**Date**: YYYY-MM-DD
**Linear**: STU-XXX
**Goal**: <one sentence>

## Entry points
[List]

## Diagram
[Embedded or linked]

## Happy path (walkthrough)
[Text — easier to review than diagram alone]

## Branches
[Table — diamond → criteria → outcomes]

## Errors + recovery
[Table — failure mode → user sees → recovery path]

## System actions
[List of backend operations + side effects]

## Annotations
[Time delays, async, A/B, locale, AT-specific]

## Cross-plugin handoffs
- Component states: `manfred-interaction-design:state-machine`
- Error UX: `manfred-interaction-design:error-handling-ux`
- Wireframes: `manfred-prototyping-testing:wireframe-spec`
```

### Step 11 — Linear comment

Post via `mcp__linear-server__save_comment` with summary + path to flow doc.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "One mega-flow shows everything." | Unreadable. One flow per goal — link related flows. |
| "Happy path is the flow." | The other 30% of users live in branches and error paths. Map them too. |
| "Decision diamonds without criteria — engineering will figure it out." | Engineering will guess; QA will find the bugs. Label every diamond. |
| "We don't need to show system actions." | Yes, you do. Async coordination + side effects are where flows actually break. |
| "Error paths are out of scope for the flow." | Then the flow doesn't represent reality. Pair with `manfred-interaction-design:error-flow`. |

## Red flags — STOP

- One flow trying to show every possible path
- Decision diamonds without criteria
- No error paths mapped
- No exit points (flow is unbounded)
- No system actions (engineering will guess)
- Diagram in a tool the team can't edit
- Flow contradicts what's actually built

## Manfred lens

**Cagan's 4 risks** — flow diagrams primarily surface **usability risk** (where users get lost) and **feasibility risk** (system coordination requirements). Skip Cagan call-out unless the flow reveals a critical decision point that's also a discovery question — then route to `manfred-discovery:cagan-risks`.

## Cross-references

- `manfred-interaction-design:state-machine` — flows live above state machines (flows = user goals; machines = component states)
- `manfred-interaction-design:error-handling-ux` — for the error-path detail
- `manfred-interaction-design:error-flow` — orchestrator for full error UX work
- `manfred-prototyping-testing:wireframe-spec` — for wire-flow (flow + screens together)
- `manfred-prototyping-testing:test-scenario` — flows inform task-writing for usability tests
- `manfred-design-systems:component-spec` — components in the flow get spec'd here
- `manfred-design-systems:a11y-design` — for AT-equivalent flow paths

## Tools used

- Mermaid, Whimsical, Figma FigJam, Lucidchart — for the diagram itself
- `mcp__linear-server__get_issue` / `save_comment` — for ticket linkage

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, happy-path-first discipline, error-paths-mandatory rule, decision-criteria-required rule, and Manfred-specific guidance are original.*
