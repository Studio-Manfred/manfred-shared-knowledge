---
name: loading-states
description: Use when designing loading / empty / progressive-reveal experiences — anyone says "loading state", "skeleton", "spinner", "progress bar", "blank screen", "feels slow", "optimistic UI", "pull-to-refresh", "lazy load", "perceived performance", "shimmer". Manfred-flavoured: never a blank screen; layout shape before content; honour `prefers-reduced-motion` for shimmer; copy goes through `manfred-toolkit:ux-writing`.
---

# loading-states

A loading state is the system saying "I'm working on it". A bad loading state — blank screen, mismatched skeleton, indefinite spinner — says "I might be broken". Perceived performance is a design problem, not just an engineering one.

Manfred's defaults:

- **Never a blank screen.** Skeleton, placeholder, or last-known content while new content loads.
- **Skeleton matches the real layout.** Wrong-shape skeletons cause layout shift on reveal — worse than no skeleton.
- **Reduced motion honoured.** Shimmer animations have a `prefers-reduced-motion: reduce` fallback (static skeleton).
- **Copy is not this skill's job.** "Loading…" and "Just a moment…" are voice decisions — route to `manfred-toolkit:ux-writing`.

## When to use

- Designing the loading state for a screen, list, image, or data fetch
- Choosing between skeleton / spinner / progress bar / optimistic UI
- Specifying transition behaviour from loading → loaded
- Reviewing a state that "feels slow" even when network is fast

**Skip when:**

- The data fetch is genuinely instant (< 100ms) — no loading state needed; flash of skeleton is worse than nothing
- The user wants the empty state *post-load* (no results) — that's `manfred-ui-design:visual-hierarchy` + `manfred-toolkit:ux-writing`
- The user wants long-running progress reporting (multi-minute job) — that's a status / progress design problem; pair with `manfred-interaction-design:feedback-patterns`

## The hard rules

| Rule | What it means |
|---|---|
| **Never a blank screen** | Show layout shape (skeleton) or last-known content, not a void. |
| **Skeleton = real layout** | Skeleton blocks must match the dimensions and arrangement of the loaded content. Wrong shapes cause CLS and disorientation. |
| **Reduced-motion fallback** | Shimmer animations honour `prefers-reduced-motion: reduce` — fall back to a static skeleton. |
| **No double indicators** | Don't show a spinner *and* a skeleton *and* a "Loading…" text. Pick one channel. |
| **Cancel for long loads** | Anything > 10s needs a way to cancel and a sense of how long is left. |

## Pattern → use case

| Pattern | Use when | Notes |
|---|---|---|
| **Skeleton screen** | Known layout, > 200ms expected wait, content-heavy view | Match the real shape; honour reduced-motion |
| **Spinner / loader** | Unknown duration, < 1s expected, single-element load (e.g. button) | Inline, near the action; tiny — not a full-screen spinner |
| **Progress bar (determinate)** | Known progress (file upload, multi-step job) | Show percentage or step count; cancel button if multi-second |
| **Progress bar (indeterminate)** | Unknown duration, page-level load | Top-of-screen bar; doesn't block interaction |
| **Optimistic UI** | Network call expected to succeed (toggle, like, status change) | Show the result immediately; reconcile on response; roll back on failure (see state-machine) |
| **Progressive reveal** | Long pages with above-the-fold + below-the-fold content | Load critical content first; lazy-load the rest |
| **Last-known content** | Refreshing existing data | Keep showing the old data; subtle indicator (top-of-list spinner, refresh icon spinning) that new is loading |
| **Blur-up image** | Large hero / above-fold images | Tiny low-quality preview → full image; smooth fade between |

## Duration thresholds

| Duration | UX response |
|---|---|
| < 100ms | No indicator. The flash of an indicator is worse than the wait. |
| 100ms – 1s | Subtle indicator. Skeleton fade-in or small spinner. |
| 1s – 10s | Clear loading state. Skeleton or progress bar. Show what's loading. |
| > 10s | Detailed progress. Time estimate if possible. Cancel + background option. |
| > 30s | This isn't a loading state — it's a job. Move to background, send notification when done, free the UI. |

## Transitions in / out

- **Fade content in, don't pop.** 150–200ms opacity transition from skeleton → real content.
- **Stagger lists.** 30–50ms between items so the page reveals in a wave, not all at once.
- **No layout shift.** Real content lands in the same dimensions as the skeleton.
- **Maintain scroll position** when refreshing existing content. Users hate being thrown back to the top.

## Optimistic UI

Use when: action is expected to succeed, latency would be visible (>200ms round-trip), the result is naturally reversible.

Pattern:

1. Show the expected result immediately on user action.
2. Send the request in the background.
3. On success: do nothing visible (the user already saw the result).
4. On failure: roll back the UI + surface the error via `manfred-interaction-design:error-handling-ux`.

Pair with `manfred-interaction-design:state-machine` for the rollback path. Optimistic UI without a rollback design is a bug factory.

## Reduced-motion

Shimmer animations are the most common reduced-motion violation. Spec them with a fallback:

```css
.skeleton {
  background: linear-gradient(90deg, var(--muted) 25%, var(--muted-light) 50%, var(--muted) 75%);
  background-size: 200% 100%;
  animation: shimmer 1.4s infinite linear;
}

@media (prefers-reduced-motion: reduce) {
  .skeleton {
    background: var(--muted);
    animation: none;
  }
}
```

The static skeleton still does its job (signals "loading", preserves layout) without the motion.

## Performance budget

- Skeleton CSS is cheap; shimmer animation is not free (especially on long lists).
- If the page already loaded the layout shell (server-rendered, edge-cached), don't add a skeleton on top — you're paying twice for the same signal.
- Spinners that loop indefinitely keep the GPU active. Use sparingly.

Manfred design principle 13 (performance is a feature). Cheap loading states win.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Spinners are universal — just use a spinner." | Spinners signal "indeterminate wait", which is the worst possible UX message. Skeleton or progress communicates more. |
| "Loading text is friendlier than a skeleton." | "Loading…" three times in a session is friction text. Skeleton signals the same with no words. |
| "Skip the skeleton — most users have fast connections." | The slow connections are the ones who'll bounce. Skeletons help them most. |
| "Optimistic UI feels fast — let's use it everywhere." | Without a rollback design, optimistic UI lies. Verify the rollback path before shipping. |

## Red flags — STOP

- Blank screen during a load > 200ms.
- Skeleton dimensions don't match the loaded content (causes CLS).
- Shimmer animation with no `prefers-reduced-motion` fallback.
- Multiple loading indicators stacked (spinner + skeleton + "Loading…" text).
- Optimistic UI with no rollback path defined.
- Spinner with no time-out / cancel for waits > 10s.

## Manfred lens

Skip Cagan / Torres — loading is execution craft. Exception: if a load that's perceived as broken risks adoption (users assume the app is dead), surface as **usability risk** and route to `manfred-discovery:cagan-risks`.

## Cross-references

- `manfred-interaction-design:state-machine` — for the loading / loaded / error states + transitions
- `manfred-interaction-design:error-handling-ux` — for what happens when the load fails
- `manfred-interaction-design:animation-principles` — for shimmer + transition timing
- `manfred-interaction-design:feedback-patterns` — for in-progress feedback channels
- `manfred-toolkit:ux-writing` — for any loading copy ("Loading", "Just a moment", "This is taking longer than usual")
- `manfred-design-systems:a11y-qa` — for `aria-busy`, `aria-live`, and reduced-motion verification

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, copy-routing rule, reduced-motion enforcement, and Manfred-specific guidance are original.*
