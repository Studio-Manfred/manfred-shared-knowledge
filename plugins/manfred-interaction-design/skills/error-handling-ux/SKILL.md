---
name: error-handling-ux
description: Use when designing the error-handling experience for a feature — anyone says "design the error flow", "what happens when X fails", "API timeout UX", "error state for the form", "retry behaviour", "what error do we show", "the API can fail — design for it", "explain don't blame", "error UX", "just generate the error copy", "keep it casual", "Oops!", "Something went wrong", "we can iterate later", "drop-in error". Manfred-flavoured: refuses to ship copy without naming the failure mode + surface; routes copy generation to `manfred-toolkit:ux-writing`; flow over words.
---

# error-handling-ux

This skill designs the *flow* of an error: prevention → detection → recovery. The four hard questions:

1. **What's the actual failure mode?** (504 ≠ network drop ≠ 500 ≠ rate-limit ≠ auth-expired ≠ validation. Each needs different recovery.)
2. **Where does the error live?** (Inline / toast / page-takeover / blocking modal — different surfaces, different rules.)
3. **What's the recovery path?** (Retry, fallback, navigate away, save-and-resume — pick one as primary, name it.)
4. **What state was the user in?** (Their input must survive the error. Lost state is a worse failure than the original error.)

The *words* — the copy itself — are not this skill's job. Once the flow is designed, route to `manfred-toolkit:ux-writing` with the structured context. This skill refuses to write the copy directly because writing copy without a named failure mode + surface produces the generic "Something went wrong" that this whole plugin exists to prevent.

## When to use

- Designing the error path for a new feature (form, async action, multi-step flow)
- Reviewing existing error handling that's vague, generic, or losing user state
- Specifying retry behaviour, fallback paths, recovery flows
- Pairing with `manfred-interaction-design:state-machine` to close the error states in the model
- Pairing with `manfred-interaction-design:loading-states` to handle the timeout / stalled-load case

**Skip when:**

- The user wants the *copy itself* (write the toast text) AND has already supplied the four pre-flight answers (failure mode + surface + recovery + user state). Only then route to `manfred-toolkit:ux-writing`. **If any pre-flight answer is missing, this skill runs first — even when the user explicitly only asked for copy.** A copy-only request without context is the #1 failure mode this skill exists to prevent. ("Oops!" / "Something went wrong" / "keep it casual" / "we can iterate later" are all signals to run pre-flight, not deflect.)
- The user wants component-library error styling (Tailwind classes for error states) — that's `manfred-design-systems:component-spec`
- The user wants infrastructure-level error handling (how the backend retries, circuit-breakers) — that's engineering, not UX

## Pre-flight (do this every time)

Before designing anything, get four answers. If the user says "quick is fine, just give me the error":

```
Hold on. Error UX without these four answers ships as "Something went wrong" 
and lives in production for years. Three minutes of context now beats three 
years of unhelpful copy.

  (a) Tell me the failure mode + surface + recovery + user state, and I'll
      design the flow + hand off to ux-writing for the copy.

  (b) You don't know yet — let's make a checklist of what to ask the 
      backend / product owner before you commit to copy.

  (c) You have a placeholder error showing now and just need to ship; 
      I'll design for the *worst* version of unknown failure (network drop), 
      flag the hardcoded copy as a follow-up, and we revisit when the 
      real failure modes are known.

Which way?
```

(c) is a real option for genuinely-blocking releases — but it isn't a free pass. Picking (c) requires THREE artifacts before ship:

1. **Linear ticket** titled `Replace placeholder error copy — <feature>`, linked to the release, owned by the same person.
2. **Code-level marker** at the call site: `// TODO(STU-XXX): placeholder copy — needs failure-mode-specific replacement`.
3. **Worst-case design** (assume network drop) so the placeholder still gets state preservation, focus management, ARIA, and reduced-motion right. Copy can be generic; *behaviour* cannot.

If the user can't commit to all three, (c) isn't on the table — that's just shipping "Oops!" with extra steps.

The four pre-flight answers:

1. **Failure mode** (specific, not "error"):
   - HTTP status: 504 timeout / 503 service unavailable / 500 server / 429 rate-limit / 401 auth-expired / 400 validation / 404 not-found
   - Network: offline / slow / drop mid-request / DNS fail
   - Client: validation / invalid input / expired session / browser-feature-unsupported
   - Each has a different recovery story.

2. **Surface**:
   - Inline (next to the field that failed)
   - Toast / snackbar (at the screen edge)
   - Page-level (replaces the page content)
   - Blocking modal (forces user response — almost never the right answer)
   - Banner (persistent system status — for service-wide issues)

3. **Recovery path** (pick one as primary):
   - Auto-retry with backoff (transient: 504, network drop, 503)
   - Manual retry button (still transient, but user controls timing)
   - Fix-and-resubmit (validation: 400, malformed input)
   - Re-authenticate (401)
   - Wait + try later (429, scheduled maintenance)
   - Navigate elsewhere (404, permission denied)
   - Save draft + resume later (long-running flow that died)

4. **User state**:
   - What was the user trying to do? (Specific goal — not "use the form".)
   - What input did they have? (Form values, scroll position, multi-step progress.)
   - What MUST survive the error? (Form values: always. Scroll position: usually. Multi-step progress: depends on the recovery — if retry, yes; if navigate-away, save draft.)

## The hierarchy (Norman's design layers)

Design the error response in this order — the earlier you can intervene, the better the UX.

### 1. Prevention (best layer — error doesn't happen)

- **Inline validation** before submit (catches client-side issues before they hit the network)
- **Smart defaults** + suggestions (reduces input errors)
- **Constraint-based inputs** (date pickers, enum dropdowns, validated formats)
- **Optimistic UI with reconciliation** (see `manfred-interaction-design:loading-states`)
- **Idempotency keys** for retries (so a duplicate request doesn't double-charge / double-send)
- **Auto-save** so navigating away mid-form doesn't lose work
- **Disabled state on impossible-action buttons** (you can't submit-while-submitting)
- **Confirmation for destructive + irreversible actions** (the 5% case where it's earned — see `manfred-interaction-design:feedback-patterns`)

### 2. Detection (second-best — catch it as it happens)

- **Real-time field validation** (blur or after debounce — never on every keystroke for noisy fields)
- **Network-state detection** (`navigator.onLine`, fetch error catching)
- **Client-side timeouts** with `AbortController` (always — server timeouts are slower than user patience)
- **Optimistic-UI rollback hook** for failed reconciliation
- **Auth expiry watchdog** (don't make the user discover it on submit; refresh in background)

### 3. Communication (the visible layer — design carefully)

- Structured by surface (see table below)
- Copy via `manfred-toolkit:ux-writing` with the four pre-flight answers as context
- ARIA: `role="alert"` (assertive — interrupts screen reader) for errors; `role="status"` (polite) for warnings/info
- Pair colour with icon + text (never colour-only)
- Place near the source — not at the page bottom when the field is at the top

### 4. Recovery (the action layer — name the path)

- **Preserve input** — never clear the form on error. Ever. The user already paid for that input.
- **Offer one primary action** (Retry, Fix, Re-sign-in, Save draft) + at most one secondary.
- **Auto-retry with exponential backoff** for transient network errors — but with a max attempts + a manual escalation when exceeded.
- **Idempotency** for retried requests (matters for create / pay / send).
- **Fallback path** if retry exhausted: save draft + email link, redirect to a known-good page, queue for offline sync.
- **Undo for accidental destructive actions** (vs confirmation — see `manfred-interaction-design:feedback-patterns`).

## Surface → recovery rules

| Surface | Use when | Recovery action shape | Notes |
|---|---|---|---|
| **Inline (per-field)** | Validation, single-field server error | Inline icon + text below field; cursor returns to field on first focus | Default for forms. Pairs with field-level retry on next blur/submit. |
| **Form-level summary** | Multi-field errors, post-submit | Top of form, list of errors, links jump to fields | Pair with inline per-field. ARIA `role="alert"`. |
| **Toast / snackbar** | Async action confirmed-failed, retry possible, user can keep working | Single line + Retry / Undo action; persists until dismissed | Never auto-dismiss an error. Single retry button max. |
| **Banner** | System-wide condition (offline, maintenance, degraded service) | Persistent, dismissible only when condition clears | One banner at a time. Pair with status-page link when relevant. |
| **Page-level error** | Page can't load at all; the failure prevents any meaningful interaction | Centered, primary action (Retry / Go home), secondary (Contact support / View status) | Use the brand voice — empty-state energy, not 500-page energy. |
| **Blocking modal** | Genuinely cannot continue (auth expired mid-action; payment declined) | One primary action (Re-sign-in / Update card), one escape (Cancel + save draft) | Almost always wrong. Justify before using. |

## Failure mode → recovery defaults

| Failure mode | Surface | Primary recovery | Notes |
|---|---|---|---|
| 400 validation | Inline per-field | Fix the field | Don't re-submit until field changes |
| 401 auth expired | Modal or page-level | Re-sign-in (preserves intent: re-runs the action after auth) | Preserve form state in session storage |
| 403 permission denied | Page-level or inline | Explain what access is needed + how to get it | Don't just say "denied" — name the path |
| 404 not found | Page-level | Search / go home / view related | Manfred voice; not "Page not found" |
| 429 rate-limited | Toast or banner | Wait + try later (show countdown if possible) | Auto-retry with backoff if calling system has the patience |
| 500 server error | Toast (action-scoped) or page-level (page-load) | Manual retry + report-a-bug link | Log to error monitoring; surface support contact |
| 502 / 503 / 504 | Toast or page-level | Auto-retry with backoff (3 attempts, exponential) → manual retry → fallback | Most transient — most worth auto-retrying |
| Network offline | Banner | Wait for online; auto-retry queued actions | Queue locally if action is offline-friendly |
| Network slow / mid-request drop | Toast | Auto-retry once → manual retry | Distinguish from "offline" — connectivity is unstable, not gone |
| Client validation | Inline | Fix the field | Run before submit, don't wait for server |

## State preservation rules

Non-negotiable:

- **Form values survive errors.** Always. Never clear inputs on submission failure.
- **Multi-step progress survives.** If step 3 fails, step 1 + 2 input is intact when user returns.
- **Optimistic UI rolls back cleanly.** Show the previous state, surface the error, don't leave the optimistic state stuck.
- **Scroll position preserved on inline errors.** Page doesn't jump to top on validation fail.
- **Long-running flows save drafts.** If a multi-minute job dies, the user has a draft to resume.

State preservation pattern:

```
beforeRequest → snapshot user state to local/session storage
onSuccess → clear snapshot
onError → snapshot persists; recovery flow can restore
```

## Auto-retry rules

Auto-retry is good for transient network / server errors. It's bad for user errors, auth errors, or anything that costs money / changes state without idempotency.

- **Auto-retry only on**: 502, 503, 504, network drop mid-request
- **Never auto-retry**: 400, 401, 403, 404, 422, 429 (use backoff but explicit), 500 (one auto-retry max — these are usually bugs, not transients)
- **Backoff**: exponential — 500ms, 2s, 8s. Cap at 3 attempts.
- **Idempotency keys**: required for any retried mutation (POST that creates / charges / sends)
- **User feedback during auto-retry**: show "Trying again…" not silent — user thinks it's frozen
- **Escalation when exhausted**: switch to manual retry button + recovery options

## Animation + focus management

When an error appears:

- **Focus management**: focus moves to the error message (or the first invalid field) so screen-reader users hear it and keyboard users land at the right spot.
- **Animation**: short fade-in (150–250ms, ease-out) — see `manfred-interaction-design:animation-principles`.
- **Reduced-motion fallback**: instant appearance, no fade.
- **No bouncing / shaking error containers** — vestibular trigger; also patronising.

## The handoff to ux-writing

After designing the flow, hand off to `manfred-toolkit:ux-writing` with this structured context:

```markdown
## Error copy request — for `manfred-toolkit:ux-writing`

**Failure mode**: <specific — 504 timeout on /api/orders POST>
**Surface**: <toast / inline / page-level / banner / modal>
**Recovery primary action**: <"Try again" / "Re-sign-in" / "Fix and resubmit">
**Recovery secondary action** (if any): <"Save draft" / "Contact support">
**User context**: <what they were trying to do — specific>
**State preservation**: <what survived the error>
**Locale**: <English / Swedish / both>
```

Don't write the copy here. The copy lives in ux-writing because the voice work lives in ux-writing. This skill's contract: *flow design with structured handoff*.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Just give me 'Something went wrong' for now." | "For now" copy lives in production for years. The failure mode this whole skill exists to prevent. Use option (c) in pre-flight — flag as placeholder + follow-up. |
| "Just generate the copy — keep it casual, we can iterate later." | Iteration requires knowing what was wrong with v1. Without failure mode + surface + recovery + state, ux-writing produces generic-SaaS-friendly copy that "technically works" — and "later" is when the metric tanks and nobody opens a ticket because the copy isn't bugged. Run pre-flight. |
| "We don't know the failure modes yet." | Then design for the worst (network drop, server 5xx). Get the structure right — fill in modes as they're discovered. Don't generate "Error 500" copy. |
| "The error is rare — design effort isn't worth it." | Rare errors hit the unlucky 0.5% — and that's where churn happens. Spend the 30 minutes. |
| "Auto-retry everything — it's transparent." | Auto-retrying a 400 turns one validation error into three identical ones. Auto-retrying a non-idempotent mutation creates duplicates. Be specific. |
| "Modal forces them to deal with it." | Modal forces them to *quit*. Use only when continuing is genuinely impossible. |
| "Clear the form on error so they can start over." | The user's input is theirs, not yours. Clearing it is hostile. |
| "Show the technical error so engineers can debug." | Engineers debug from logs, not from production toasts. Users see human language; logs see stack traces. |

## Red flags — STOP

- Designing copy without a named failure mode.
- Toast that auto-dismisses an error.
- Form that clears on submission failure.
- Auto-retrying a non-idempotent mutation without an idempotency key.
- Modal blocking action when continuing is possible.
- "Something went wrong" / "Error 500" / "Oops!" anywhere in the spec.
- No focus management on error appearance (screen-reader users won't notice).
- No reduced-motion fallback for the error animation.
- No state preservation — user's input gets thrown away on retry.

## Manfred lens

**Cagan's 4 risks** — error UX touches:

- **Usability risk** — bad error UX is the #1 source of inflated abandonment metrics. If the failure rate is ≥ 1% of an action, the error UX *is* part of the user experience.
- **Viability risk** — for paid actions, broken error recovery is broken revenue. Failed payments without clear retry → churn.

When designing error UX for a critical revenue / retention path, surface the risk explicitly via `manfred-discovery:cagan-risks`.

**Torres OST** — if a failure pattern keeps recurring (e.g. payment-declined for international cards), it's an **opportunity** worth modelling. Route to `manfred-discovery:opportunity-solution-tree`.

## Output format

```markdown
# Error UX spec — <feature name>

## Pre-flight context
- **Failure modes covered**: <list with specifics>
- **Surfaces**: <inline / toast / page-level / etc>
- **Primary recovery**: <named path>
- **User state preserved**: <list>

## Per failure mode

### <mode 1> (e.g. 504 timeout)
- **Surface**: <toast>
- **Detection**: <client timeout 10s via AbortController>
- **Recovery**: <auto-retry × 3 with backoff → manual retry button → fallback save-draft>
- **State preserved**: <form values, scroll>
- **Focus**: <on retry button after toast appears>
- **Animation**: <250ms fade-in, reduced-motion fallback: instant>
- **ARIA**: <role="alert" — assertive>
- **Copy handoff**: <structured request to manfred-toolkit:ux-writing — see below>

### <mode 2>
...

## State preservation pattern
<pseudo or actual code showing snapshot/restore>

## Auto-retry policy
- **Modes auto-retried**: 502, 503, 504, network drop
- **Backoff**: 500ms / 2s / 8s, max 3 attempts
- **Idempotency**: <key strategy — UUID per action stored in context>

## State machine integration
<reference manfred-interaction-design:state-machine — show error states + transitions>

## Copy handoff
<structured request block per the template above — one per failure mode>

## Linear ticket
<STU-XXX>
```

## Tools used

- `Read` — to inspect existing error patterns in the codebase
- `Bash` (`grep`) — to find existing error-handling code, find current error copy
- `mcp__linear-server__get_issue` — to confirm ticket scope
- `mcp__linear-server__save_comment` — to log the spec to the ticket

## Cross-references

- `manfred-toolkit:ux-writing` — for the actual error message copy (always — never write it here)
- `manfred-interaction-design:state-machine` — for the error states + transitions in the model
- `manfred-interaction-design:loading-states` — for the timeout / stalled-load → error transition
- `manfred-interaction-design:feedback-patterns` — for the surface/channel choice
- `manfred-interaction-design:animation-principles` — for the error appearance animation + reduced-motion
- `manfred-discovery:cagan-risks` — when error UX is on a critical revenue / retention path
- `manfred-design-systems:a11y-design` + `manfred-design-systems:a11y-qa` — for ARIA + focus + reduced-motion verification
