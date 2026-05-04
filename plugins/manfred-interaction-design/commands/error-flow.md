---
description: Design a complete error-handling flow for a feature — chains failure-mode inventory + prevention + state model + recovery + copy handoff.
argument-hint: [feature name, e.g. "checkout payment" or "file upload" or "calendar sync"]
---

You're designing the error UX for a feature. The user mentioned: $ARGUMENTS

Errors get the same design care as the happy path — usually more, because the user is already frustrated when they meet your error UX.

## Step 1 — Pre-flight (do not skip)

`manfred-interaction-design:error-handling-ux` opens with four required answers. Get them now or hold the rest of this command.

1. **Failure modes** — list every specific mode (HTTP statuses, network states, client-side conditions). Not "error". 504 ≠ 503 ≠ 401 ≠ network drop.
2. **Surface per mode** — inline / toast / page-level / banner / modal.
3. **Recovery per mode** — auto-retry / manual retry / re-auth / fix / save-draft / navigate.
4. **User state** — what was the user trying to do, what input they had, what MUST survive the error.

If the user says "quick is fine, just give me copy" — refuse and offer the (a)/(b)/(c) menu from the skill. Don't generate copy without the four answers (or an explicit (c) placeholder + follow-up flag).

**Linear ticket** — capture if known.

## Step 2 — Inventory failure modes (`manfred-interaction-design:error-handling-ux`)

For the feature scope, list every failure mode. Walk through:

- **HTTP**: 400 / 401 / 403 / 404 / 422 / 429 / 500 / 502 / 503 / 504
- **Network**: offline / slow / mid-request drop / DNS fail
- **Client**: validation, expired session, browser feature unsupported, storage quota exceeded
- **Domain**: payment declined, inventory depleted, permission revoked, integration down

For each mode that *can* hit this feature: how likely, how user-impacting.

## Step 3 — Prevention layer (`manfred-interaction-design:error-handling-ux`)

For each mode, what prevents it from happening?

- Inline validation
- Smart defaults / constraints
- Optimistic UI with reconciliation
- Idempotency keys
- Auto-save / draft preservation
- Disabled-state on impossible actions
- Auth refresh in background

The cheapest error is the one that doesn't happen.

## Step 4 — Detection layer

How do we catch it?

- Real-time validation (blur/debounce — never every keystroke for noisy fields)
- `navigator.onLine` watcher
- Client `AbortController` timeouts (always — server timeouts are slower than user patience)
- Optimistic UI rollback hooks
- Auth expiry watchdog

## Step 5 — State modelling (`manfred-interaction-design:state-machine`)

Add the error states to the feature's state model. Per failure mode:

- Where does it sit in the state graph?
- What event transitions into it?
- What's the recovery transition out?
- What context (failure mode, attempt count, original intent) does it carry?

Verify: are any error + non-error states simultaneously reachable? They shouldn't be.

## Step 6 — Communication layer

For each mode:

- **Surface** (per Step 1)
- **ARIA**: `role="alert"` (assertive — for errors that need immediate attention) vs `role="status"` (polite — for warnings/info)
- **Focus**: where focus moves when the error appears (typically: the error itself or the first invalid field)
- **Animation**: 150–250ms fade-in via `manfred-interaction-design:animation-principles`; reduced-motion fallback (instant)
- **Pair colour with icon + text** — never colour-only

## Step 7 — Recovery layer

For each mode, design the path:

- **Primary action** — Retry / Fix / Re-sign-in / Save draft / Navigate
- **Secondary action** (if any) — single secondary; "Contact support" or "View status"
- **Auto-retry policy** if applicable: only for 502 / 503 / 504 / network drop; exponential backoff (500ms / 2s / 8s); max 3 attempts; idempotency key required for mutations
- **Fallback** when recovery exhausted: save draft + email link / redirect to known-good / queue for offline sync
- **State preservation rules** — form values always survive; multi-step progress always survives; scroll position usually survives

## Step 8 — Loading + timeout integration (`manfred-interaction-design:loading-states`)

For each async transition:

- Client timeout duration (`AbortController` — 10s default; tune per endpoint)
- What loading state shows during the wait
- What renders during auto-retry attempts (don't go silent — "Trying again…")
- When loading exceeds threshold, what becomes the error UX

## Step 9 — Copy handoff (`manfred-toolkit:ux-writing`)

For each failure mode, write a structured handoff request. Do **not** write the copy here.

Format per mode:

```markdown
## Copy request — <mode>
- **Failure mode**: <e.g. 504 timeout on /api/checkout/submit>
- **Surface**: <toast>
- **Primary action**: <Try again>
- **Secondary action** (if any): <Save draft>
- **User context**: <reviewing 3-item cart, payment entered, on review step>
- **State preserved**: <cart items, payment details, scroll>
- **Locale**: <English / Swedish / both>
```

## Step 10 — Document

Save to:

```
docs/error-flows/<feature-slug>-<YYYY-MM-DD>.md
```

Format:

```markdown
# Error flow — <feature>

**Date**: YYYY-MM-DD
**Linear**: STU-XXX

## Failure modes covered
[list with likelihood / impact ratings]

## Prevention
[per mode, where prevention applies]

## Detection
[per mode, how we catch it]

## State model integration
[reference manfred-interaction-design:state-machine output; show error states + transitions]

## Per failure mode
[full spec per mode — surface / ARIA / focus / animation / recovery / state preservation]

## Auto-retry policy
[modes / backoff / idempotency strategy]

## Loading + timeout
[per async transition]

## Copy handoffs to manfred-toolkit:ux-writing
[one structured request per mode]

## Outstanding decisions
- Tokens to add (motion / colour / spacing)
- Copy waiting on real failure-condition info
- a11y items for `manfred-design-systems:a11y-qa`

## Cagan risks (if critical path)
[reference manfred-discovery:cagan-risks output]
```

## Step 11 — Linear update

Post via `mcp__linear-server__save_comment`:

- Path to spec
- Summary: failure modes covered, surfaces used, recovery paths, copy handoffs queued
- Outstanding decisions

## Wrap-up checklist

- [ ] All four pre-flight answers captured per mode (or explicit (c) placeholder flagged)
- [ ] Every failure mode has surface + recovery + state-preservation
- [ ] No "Something went wrong" / "Error 500" / "Oops!" in the spec
- [ ] Auto-retry policy is specific (which modes, backoff, idempotency)
- [ ] State model integrates the error states cleanly
- [ ] Reduced-motion fallback for error animations
- [ ] ARIA `role="alert"` vs `status` chosen per mode
- [ ] Focus management defined per mode
- [ ] Form values / multi-step progress preservation rule explicit
- [ ] Copy handoff requests written for `manfred-toolkit:ux-writing` — one per mode
- [ ] Linear comment posted

Then offer:

> "For the full state model, run `/manfred-interaction-design:map-states`. For the actual error copy, hand off to `manfred-toolkit:ux-writing` with the structured requests above."
