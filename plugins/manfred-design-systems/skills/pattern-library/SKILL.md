---
name: pattern-library
description: Use when capturing or applying a reusable design pattern in a Manfred app — anyone says "what's the right pattern for…", "how do we usually handle X", "empty state pattern", "form error pattern", "loading pattern", "confirmation flow", "onboarding pattern", "document this pattern", "we keep solving this the same way". Stack: Manfred design system + shadcn shapes + Tailwind v4.
---

# pattern-library

A pattern is a recurring solution to a recurring problem. The library catches the team mid-pattern — once you've solved the same problem three times, document it. Once it's documented, the next person doesn't reinvent it.

## Overview

Patterns are bigger than components and smaller than features. A `Button` is a component; a "confirmation dialog before destructive action" is a pattern; a "checkout flow" is a feature. Patterns combine 2+ components into a known-good composition for a specific UX problem.

Manfred's pattern library lives next to the design system docs (Storybook MDX) and is **problem-first** — every entry leads with the problem it solves, not the components it uses.

## When to use

- You've solved the same UX problem twice and you're about to solve it a third time
- Someone asks "what's the right way to handle X" and the answer keeps changing per project
- Designing a flow that touches multiple components in a specific order (form + validation + submission + success/error feedback)
- Onboarding a new team member to a project's UX conventions
- Auditing inconsistency — same problem solved three different ways across screens

**Skip when:**

- One-off solution that won't recur (just build it, don't document a pattern)
- The "pattern" is actually a single component (use `manfred-design-systems:component-spec`)
- The problem is feature-specific, not UX-recurring (lives in the feature spec, not the pattern library)

## Pre-flight

Before adding a pattern:

1. **Confirm it's recurring.** Three times in real projects = pattern. One project = note. Zero = premature abstraction.
2. **Check if it's already documented.** Check existing pattern library, search the codebase for similar compositions.
3. **Check if it should be a component instead.** If the composition is identical every time with no contextual variation, it's a component. Patterns have intentional flex.

## Pattern entry structure

```markdown
# <Pattern Name>

> One sentence. The recurring problem this pattern solves.

## Problem
2-3 sentences. What goes wrong without this pattern? What context does it appear in? Why do teams keep getting it wrong?

## Solution
Plain words. The pattern. A diagram or screenshot if helpful.

## When to use
- [Specific context]
- [Specific context]

## When not to use
- [Specific context — and what to use instead]
- [Specific context]

## Anatomy
[Components involved, layout, what's required vs optional]

## Behaviour
[State transitions, interactions, error paths, edge cases]

## Examples

### Compliant
[Real example — link to Storybook, a live page, or include the JSX]

```tsx
// the actual composition
```

### Anti-pattern
[Specific wrong way + why it fails — what bad UX or a11y issue it produces]

## Accessibility
- Keyboard flow: …
- Focus management: …
- Screen reader announcements: …
- Reduced motion: …

## Tokens consumed
[Reference `manfred-design-systems:design-token` outputs — surface, text, border, spacing, radius]

## Related patterns
- [Pattern] — used together with this
- [Pattern] — alternative for [different context]

## Status
experimental | stable | deprecated
```

## Pattern categories (Manfred's working set)

| Category | Examples |
|---|---|
| **Navigation** | Top bar + breadcrumb, navigation rail, tab switching, back-link header |
| **Input** | Form with inline errors, multi-step form, search-as-you-type, file upload |
| **Display** | Card grid, list with selection, table with sort/filter, detail page |
| **Feedback** | Toast for transient confirmation, dialog for destructive confirmation, inline error, empty state with primary action, loading state (skeleton vs spinner) |
| **Onboarding** | First-run tooltip tour, progressive disclosure of advanced features, sample-data state |

The categories are not a taxonomy — they're a search index. If a pattern fits two categories, file under the primary one and cross-link.

## The hard rules

| Rule | What it means |
|---|---|
| **Problem first, solution second** | Every entry leads with what the user / team is trying to solve. Components and JSX come later. |
| **Compliant + anti-pattern, both** | Show the wrong way too. The anti-pattern is the most useful section — it stops the next person making the same mistake. |
| **Tokens, not literals** | Patterns reference semantic tokens; no hex, no `bg-green-500`. Pull from `manfred-design-systems:design-token`. |
| **Accessibility is a section, not a footnote** | Keyboard flow + focus + announcements + reduced motion. Every pattern. |
| **Status indicator at the top** | `experimental` / `stable` / `deprecated` so consumers know whether to bet on it. |
| **Three-strikes rule for inclusion** | Don't add a pattern after one use. Document it as a project-local note, promote to library after the third recurrence. |

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We've only done this twice but it'll definitely recur" | Maybe. Wait for the third use. Premature patterns lock in the wrong abstraction. |
| "The anti-pattern is obvious, I'll skip it" | If it's so obvious, why is the team still doing it? Document the failure mode. |
| "This is a feature, not a pattern" | If it touches multiple unrelated features and they all need it (empty states, error recovery, confirmation), it's a pattern. |
| "I'll just turn this into a component instead" | If the composition has no intentional flex (always the same components, same order, same content shape), yes — make it a component. If it has flex (same problem, different surfaces / copy / nesting), pattern. |
| "Patterns slow us down — let people compose freely" | Free composition for the first solve, document for the third. Doctrine without documentation is faster than divergence with debate. |

## Manfred lens

Patterns are **usability** infrastructure — Cagan's usability risk applies directly. A pattern that doesn't get tested with real users is just a confident guess. When introducing a new pattern (or seriously revising one), validate via `manfred-design-research:usability-test-plan` before promoting from `experimental` to `stable`.

The decision to promote: did the pattern survive a usability test with the actual users it serves? If yes, `stable`. If not, back to `experimental`.

## Tools used

- `Read` — existing pattern library, project codebase to confirm recurrence
- `manfred-design-systems:component-spec` — when a pattern decision becomes a new component
- `manfred-design-systems:documentation-template` — pattern template lives there
- `manfred-design-systems:design-token` — for token references in pattern examples
- `manfred-design-research:usability-test-plan` — to validate a pattern before promoting

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
