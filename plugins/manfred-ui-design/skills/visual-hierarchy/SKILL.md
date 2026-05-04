---
name: visual-hierarchy
description: Use when establishing or auditing visual hierarchy on a page or surface — anyone says "visual hierarchy", "what should the user see first", "page hierarchy", "scan order", "primary action", "make this stand out", "F-pattern", "Z-pattern", "above the fold". Manfred-flavoured: one primary action per view; squint test; hierarchy reinforces user intent, not decoration.
---

# visual-hierarchy

Visual hierarchy is the answer to "where do I look first?". Done right, users find the primary action without thinking; done badly, they bounce trying to figure out where to start.

Manfred prefers spare hierarchies over dense ones — one primary action per view, generous spacing around it, secondary content recedes. The hierarchy reinforces what the user is trying to do.

## Overview

Five hierarchy tools. Used together, they create unambiguous priority:

| Tool | How it works | Strongest at |
|---|---|---|
| **Size** | Larger = more attention. Use ≥1.5× size differences for clear distinction. | Establishing primary CTA, hero element |
| **Weight** | Bold / thick / filled = more weight than regular / thin / outline. | Differentiating headings from body |
| **Colour + contrast** | High-contrast attracts attention. Use sparingly. | CTAs, status, emphasis |
| **Spacing** | More whitespace around an element = more importance. | Focal elements; isolating primary action |
| **Position** | Top-left (LTR) seen first. F-pattern + Z-pattern scanning. | Above-the-fold; primary CTA placement |

Plus **density**: isolated elements stand out; grouped elements are scanned as a unit.

## When to use

- Designing a new page or screen
- Reviewing a page that "feels busy" or "where do I look?"
- Resolving a "users don't see the CTA" usability finding
- Refining a hero section, dashboard card, or landing page
- Auditing a project for hierarchy consistency

**Skip when:**

- The work is component-internal layout (use `manfred-design-systems:component-spec`)
- The work is type scale (use `manfred-ui-design:typography-scale`)
- The work is colour palette (use `manfred-ui-design:color-system`)
- The work is grid (use `manfred-ui-design:layout-grid`)

## Pre-flight

Ask:

- **What's the primary action on this view?** One. Not three. If you can't name one, the hierarchy is already broken.
- **What's the user trying to do?** The primary action serves the user's intent, not the team's.
- **What's secondary, what's tertiary?** Layered priority — what does the user see first, second, third?
- **What's the scan pattern?** Western LTR users scan in F-pattern (text-heavy) or Z-pattern (visual). RTL is mirrored.

If you can't name the primary action — stop. Hierarchy without priority is decoration.

## The hard rules

| Rule | What it means |
|---|---|
| **One primary action per view** | A view has one primary CTA. Two = no primary. Three = the user has to choose, and choice is friction. |
| **Layered priority (1° / 2° / 3° / 4°)** | Primary (page title, primary CTA) → secondary (section headings, key content) → tertiary (supporting text) → quaternary (fine print). Each level has consistent treatment. |
| **Squint test** | Blur your eyes. If hierarchy is still clear, it works. If everything reads the same — fix. |
| **Don't compete for attention** | If two elements both want primacy, the user picks neither. Decide what matters most; subordinate the rest. |
| **Use hierarchy to tell a story** | A page should read like a sentence: "First, here's the problem [hero copy]. Second, here's what to do [primary CTA]. Third, here's more context [supporting copy]." |
| **Above the fold matters** | The hero / first viewport is what users see first. Primary action lives there or is reachable in <2 seconds. |
| **Hierarchy works in dark + light** | Switch modes; hierarchy should hold. If contrast or colour is doing the work and dark mode breaks it, fix. |

## Hierarchy levels (typical patterns)

### Primary
Page title + primary CTA + hero visual. Typically 1–3 elements. Largest type, most contrast, most surrounding whitespace.

```tsx
<section className="py-12 px-6 max-w-3xl mx-auto">
  <h1 className="text-4xl md:text-5xl font-bold mb-4">Reduce KYC abandonment to 14%</h1>
  <p className="text-lg text-muted-foreground mb-8">Show users where they are; tell them what's left.</p>
  <Button variant="primary" size="lg">Start the redesign</Button>
</section>
```

### Secondary
Section headings, key content, secondary CTAs. Smaller than primary, less contrast, less whitespace.

### Tertiary
Supporting text, metadata, descriptive copy. Read on demand.

### Quaternary
Fine print, timestamps, technical details. Available but not prominent. `text-xs` muted.

## Common patterns

| Pattern | Hierarchy shape |
|---|---|
| **Hero section** | Large display + supporting copy + single CTA |
| **Card layout** | Image (or visual anchor) → title → description → CTA |
| **Form** | Section heading → label → input → helper text → error |
| **Navigation** | Current state (high contrast) > available items > disabled |
| **Dashboard card** | Number (large) → label (medium) → trend (small) → drill action (subtle) |
| **List item** | Primary text → secondary text → metadata → action |

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We need 3 primary CTAs because users have 3 jobs" | Users don't have 3 simultaneous jobs in one view. Pick the one most users want; subordinate the rest. |
| "Make everything big — emphasis everywhere" | If everything is emphasised, nothing is. Hierarchy is contrast; emphasis everywhere = no contrast. |
| "Stakeholders want their feature 'highlighted'" | Stakeholder politics is not hierarchy. Push back; the user's intent decides what's primary. |
| "We'll use bright colour for emphasis" | Colour alone is the weakest tool. Combine with size + weight + spacing. |
| "Squint test is subjective" | Less subjective than "I think this looks right". Run it; let the blur decide. |
| "Primary action below the fold is fine — users will scroll" | Maybe. Some won't. If the action is critical, surface it above the fold or anchor a sticky version. |

## Red flags — STOP

- More than one primary CTA per view
- Page where the primary action isn't obvious in <2 seconds of scanning
- Hierarchy that fails the squint test (everything looks the same when blurred)
- Hierarchy that depends entirely on colour (colour-blind / dark-mode breaks it)
- Stakeholder requests overriding user-need-driven hierarchy
- Decorative emphasis (large font, bold colour) on elements that aren't actually primary
- Hierarchy that doesn't reflect the user's intent

## Manfred lens

Visual hierarchy serves **usability** directly. The faster users find what they need, the better the design works. It also reinforces **principle 7 (simple by default)** — one primary action; remove complexity before adding instructions.

Critical & ethical (principle 6): hierarchy can manipulate (false-urgency emphasis, dark patterns that promote one option over the user's preferred choice). The primary action serves the user's intent, not the team's metric. Refuse the manipulation.

## Cross-references

- `~/.claude/shared/DESIGN.md` Sections 5 (Layout) and 11 (Do's and Don'ts)
- `~/.claude/shared/design-principles.md` principles 7 (simple), 5 (accessible), 6 (ethical)
- `manfred-ui-design:typography-scale` — type is a hierarchy tool
- `manfred-ui-design:color-system` — colour + contrast is a hierarchy tool
- `manfred-ui-design:spacing-system` — spacing is a hierarchy tool
- `manfred-ui-design:layout-grid` — grid is the structural floor for hierarchy
- `manfred-design-systems:component-spec` — component-internal hierarchy

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md`, prior designs
- `manfred-ui-design:typography-scale` — for type tools
- `manfred-ui-design:color-system` — for colour tools
- `manfred-ui-design:spacing-system` — for spacing tools

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
