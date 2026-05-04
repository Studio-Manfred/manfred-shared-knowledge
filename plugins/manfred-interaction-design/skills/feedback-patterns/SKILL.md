---
name: feedback-patterns
description: Use when designing system feedback for user actions — anyone says "design a toast", "success message", "confirmation pattern", "what kind of notification", "inline validation", "feedback after submit", "progress indicator", "status badge", "snackbar". Manfred-flavoured: feedback closest to the action wins; "Are you sure?" is a code smell — undo instead; copy goes through `manfred-toolkit:ux-writing`.
---

# feedback-patterns

Feedback is the system's reply to the user. It says "I heard you", "this is happening", "this is done", "this is what changed". Without it the interface feels broken; with too much of it the interface feels frantic.

Manfred's defaults:

- **Inline beats toast beats banner beats system notification.** The closer feedback sits to the action, the more confidence it builds.
- **Undo > "Are you sure?"** Confirmation dialogs are a friction tax that's wrong about 95% of the time. Reversible action + undo is almost always better.
- **Words are not this skill's job.** Pick the channel and the timing here; route the actual copy to `manfred-toolkit:ux-writing`.

## When to use

- Designing the response to a single user action (form submit, toggle, like, save)
- Choosing a feedback channel (inline / toast / banner / system)
- Specifying timing / dismissal behaviour
- Reviewing existing feedback that feels too loud, too quiet, or mistimed

**Skip when:**

- The user wants the *copy* — that's `manfred-toolkit:ux-writing`
- The user wants notifications outside the app (push / email / SMS) — that's a notification-strategy problem, not a feedback-pattern problem
- The user wants haptics for a native iOS / Android app — refer to platform HIG; Manfred doesn't ship a haptic system

## Pre-flight

Before specifying feedback, confirm:

- **What action are we acknowledging?** (Save, delete, navigate, fail validation.)
- **Is the action reversible?** (If yes — undo wins. If no — confirmation may be earned.)
- **What's the user's next move?** (Stay on the page, leave, retry.)
- **Could this feedback fire 10 times in 10 seconds?** (Then it needs deduplication, not louder feedback.)

## The hierarchy

Pick the *closest* channel that does the job:

1. **Inline / contextual** — directly on the field, button, or component the user touched. The default. Use unless inline literally can't show the message (e.g. action that navigates away).
2. **Component-level** — within the parent component (a list-level toast under the table, not at the screen edge). Use when inline would clutter or when the action affected the whole component.
3. **Page-level** — toast / snackbar / banner at the screen edge. Use for actions that affect the whole page (form submit, sign-in, network error reaching the page).
4. **System-level** — push notification, system tray. Use for events that happen *outside the user's current view* and matter enough to interrupt.

Rule of thumb: every level you escalate, you cost the user attention. Climb only when you must.

## Channels

| Channel | Use when | Dismissal | Notes |
|---|---|---|---|
| Inline text / icon | Validation, field state | Auto-clears on input change | Fastest, lowest cost. Default for forms. |
| Inline component (filled state, checkmark) | Toggle, like, save-in-place | State persists | The button itself becomes the feedback. |
| Toast / snackbar | Action confirmed at page level, transient | Auto-dismiss 4–6s, swipeable | Pair with undo when action is reversible. |
| Banner / alert | Persistent system status (offline, maintenance) | User-dismissed or condition-resolved | Use sparingly; banners stack into noise. |
| Modal / dialog | Action requires user response before continuing | User-dismissed | Use only when the user genuinely *must* respond. Almost never. |
| Activity indicator (inline progress, typing dots) | Async work in progress | Hides on completion | See `manfred-interaction-design:loading-states`. |

## Timing rules

- **Immediate** (< 100ms): visual response on click / hover / input. Always. If this is missing, the interaction feels broken.
- **Toast confirmations**: appear within 200ms of action completion; persist 4–6s; user can dismiss earlier.
- **Errors**: persist until resolved or user-dismissed. Never auto-dismiss an error the user might've missed.
- **Optimistic confirmations**: show immediately, reconcile with server, roll back if reconciliation fails. Pair with `manfred-interaction-design:state-machine` for the rollback path.

## Undo > confirmation

For reversible actions:

- ✅ Show success toast with **Undo** action.
- ❌ Show "Are you sure you want to delete?" dialog before the action.

Confirmation dialogs interrupt the user every time. Undo only appears when needed. Manfred default is undo. Reserve confirmation for:

- Truly destructive + irreversible (account deletion, "this will delete 4,000 records")
- Actions that affect other people (sending a campaign to 50,000 recipients)
- Actions where undo is technically infeasible

For everything else: do it, confirm with undo, get out of the way.

## Stacking + deduplication

If the same feedback could fire multiple times in quick succession (e.g. saving on every keystroke):

- **Debounce** the action so it doesn't fire 10x.
- **Replace, don't stack** — a new toast for the same event replaces the previous, doesn't add a second.
- **Cap visible toasts** — never more than 2–3 visible at once. Older ones dismiss to make room.

## Accessibility

- Feedback must not rely on colour alone — pair colour with icon + text.
- Toast / banner messages need `role="status"` (polite) for confirmations or `role="alert"` (assertive) for errors.
- Auto-dismiss timers respect WCAG 2.2.1 — provide a way to pause / extend, or make persistent for screen-reader users (Tailwind `aria-live` regions).
- Verify with `manfred-design-systems:a11y-qa` before shipping.

## Copy: out of scope here

Pick the channel and timing. Route the *words* to `manfred-toolkit:ux-writing` with:

- The exact failure or success condition
- The surface (toast, inline, banner)
- The user's next action

Generic "Saved!" copy is the failure mode that happens when feedback skills generate their own copy. Don't.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Add a confirm dialog so they don't make mistakes." | Undo prevents mistakes without interrupting the 99% of users who weren't going to make one. |
| "Toast for every save — users want to know it saved." | Inline filled state on the save button does the same job without stealing the corner of the screen. |
| "Stack toasts so nothing's missed." | Stacked toasts get scanned past as noise. Replace + log to a notifications page instead. |
| "Banner for system status; just leave it up." | Banners stack into wallpaper. Persist only the *current* status; show one. |

## Red flags — STOP

- Confirmation dialog for a reversible action.
- Toast that auto-dismisses an error.
- Feedback message containing the *copy* — copy decisions belong in `manfred-toolkit:ux-writing`, not here.
- More than 3 simultaneous toasts.
- Feedback that depends on colour alone.

## Manfred lens

Skip Cagan / Torres — feedback is execution craft, not discovery. The exception: if a feedback choice masks a usability risk (e.g. silent failure mode), surface it as **usability risk** and route to `manfred-discovery:cagan-risks`.

## Cross-references

- `manfred-toolkit:ux-writing` — for the actual copy
- `manfred-interaction-design:state-machine` — for rollback behaviour on optimistic UI
- `manfred-interaction-design:loading-states` — for in-progress feedback
- `manfred-interaction-design:error-handling-ux` — for error-specific feedback flows
- `manfred-interaction-design:micro-interaction-spec` — for the trigger / rules / feedback frame around a single feedback moment
- `manfred-design-systems:a11y-qa` — for live-region + dismissal-timing checks

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, undo-over-confirmation rule, copy-routing to `manfred-toolkit:ux-writing`, and Manfred-specific guidance are original.*
