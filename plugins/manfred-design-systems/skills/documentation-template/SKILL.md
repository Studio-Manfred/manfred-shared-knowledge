---
name: documentation-template
description: Use when documenting a component, pattern, or design foundation in a Manfred design system — anyone says "write docs for this component", "design system doc page", "Storybook page for…", "MDX template", "doc template", "how do I document this", "what goes on a docs page". Stack: Storybook + MDX + the Manfred design system.
---

# documentation-template

A docs page is the contract between the design system and the team using it. Manfred docs are short, written in second person, lead with the most important info, and assume the reader is an adult.

## Overview

This skill produces an MDX (or markdown) docs template for one of three artifacts:

- **Component** — a thing that ships in the library (Button, Dialog, Toast)
- **Pattern** — a reusable composition (form layout, error recovery, empty state)
- **Foundation** — a system rule (colour, typography, spacing, motion)

Each has a different shape. Pick the right one — using a component template for a foundation produces useless docs.

## When to use

- Writing a new Storybook docs page
- Documenting a component before merging it into the design system
- Capturing a recurring pattern as a reusable doc
- Writing a foundation page (colour, type, spacing, motion)

**Skip when:**

- The user wants a README, not a docs page (different shape — readme is install/quickstart, docs is reference)
- The user wants comments inside code (use JSDoc / TS doc comments, not this template)

## Pre-flight

Identify which template applies:

| Artifact | Template | Examples |
|---|---|---|
| **Component** | Component template | Button, Dialog, Toast, FormField |
| **Pattern** | Pattern template | "Form with inline errors", "Empty state with primary action", "Confirmation dialog flow" |
| **Foundation** | Foundation template | Colour palette, type scale, spacing scale, motion system |

If unsure, ask the user one question: "Is this a thing that ships (component), a way of using things (pattern), or a system rule (foundation)?"

## Component template

```mdx
# <ComponentName>

> One-sentence description. The job this component does.

## When to use
- [Specific use case]
- [Specific use case]
- Use [other component] when [different use case]

## Example
```tsx
<ComponentName variant="primary">Click me</ComponentName>
```

## Anatomy
[Visual breakdown — what's required, what's optional]

## Variants
| Variant | When | Example |
|---|---|---|
| primary | Default action | "Save", "Submit" |
| outline | Secondary | "Cancel" |
| ghost | Tertiary | "Skip for now" |

## Props
| Prop | Type | Default | Description |
|---|---|---|---|
| variant | "primary" \| "outline" \| "ghost" | "primary" | … |

## States
Default · Hover · Focus · Active · Disabled · Loading · Error

## Accessibility
- Role: …
- Keyboard: …
- Focus: …
- Screen reader: …
- Target size: 24×24 px min (44×44 px recommended)

## Tokens
Surface · Text · Border · Spacing · Radius

## Content guidelines
- Use sentence case for labels ("Save changes", not "Save Changes")
- Verbs for actions ("Delete", not "Deletion")
- Max [N] words

## Related
- [Related component] — when to use that instead
- [Pattern] — common composition

## Changelog
- v1.0.0 — initial release
```

## Pattern template

```mdx
# <Pattern Name>

> The recurring problem this pattern solves.

## Problem
[2-3 sentences. What goes wrong without this pattern? When does the team keep making the same mistake?]

## Solution
[The pattern, in plain words. Diagram or screenshot if helpful.]

## When to use
- [Context]
- [Context]

## When not to use
- [Context]
- [Context]

## Anatomy
[The components involved, how they compose]

## Behaviour
[State transitions, interactions, error paths]

## Examples
### Good
[Real example — link to Storybook or a live page]

### Anti-pattern
[Specific wrong approach, why it fails]

## Accessibility
[How this pattern stays accessible — keyboard flow, focus management, announcements]

## Related patterns
- [Pattern] — used together with this
- [Pattern] — alternative for [different context]
```

## Foundation template

```mdx
# <Foundation Name>

> The rule. One sentence.

## Why this rule exists
[2-3 sentences. The decision the rule makes for you so you don't have to relitigate it.]

## The rule
[Specific, testable statement. Examples of compliant + non-compliant values.]

## Examples
### Compliant
[Concrete example]

### Non-compliant
[Concrete example + what to do instead]

## Exceptions
[Where the rule doesn't apply, and why. If "no exceptions", say so.]

## Reference
- [Source spec — WCAG, Material, internal RFC]
- [Tooling that enforces this — linter, token validator]
```

## The hard rules

| Rule | What it means |
|---|---|
| **Second person** | "You use this when…" not "One uses this when…" or "Users use this when…" |
| **Lead with the most important info** | The first paragraph answers "should I use this?" — not history, not architecture |
| **Tables for parallel structure** | Variants, props, states, examples — anything with N rows of similar shape |
| **Code beside visuals** | Every example shows the JSX/markup, not just a screenshot |
| **One artifact per page** | A component page is just that component. Patterns and foundations get their own pages. |
| **Status indicators for maturity** | `experimental` / `stable` / `deprecated` at the top — tells consumers whether to bet on it |

## Common rationalisations

| Excuse | Reality |
|---|---|
| "I'll write docs after the component lands" | After-docs become never-docs. Write the page as the spec, ship them together. |
| "The code is self-documenting" | Code answers *how*, docs answer *should I* and *when*. Different question. |
| "I'll skip the accessibility section, the component is accessible" | If it's accessible, the section is short. If you can't write it, the component isn't ready. |
| "Anti-patterns make us look bad" | Anti-patterns make consumers stop making the same mistake. They're the most useful section. |

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md` to confirm tokens referenced in docs
- `Write` — produce the MDX/markdown file
- `manfred-design-systems:component-spec` — input for the component template
- `manfred-design-systems:design-token` — input for the foundation template (token-shaped foundations)

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
