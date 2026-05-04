---
name: typography-scale
description: Use when defining or applying typography — anyone says "type scale", "typography system", "font sizes", "heading hierarchy", "what font size for X", "line height", "letter spacing", "type choice", "Host Grotesk". Manfred-flavoured: Host Grotesk for everything UI; Guttery for the logotype only; scale per `~/.claude/shared/DESIGN.md` Section 3.
---

# typography-scale

Manfred's typography is anchored on Host Grotesk — a contemporary humanist sans-serif with a confident geometric backbone and warm, open apertures. It scales from microcopy to display headings without drawing attention to itself.

The full type scale lives in `~/.claude/shared/DESIGN.md` Section 3. This skill is the guide for applying it.

## Overview

| Role | Weight | Size | Tailwind | Character |
|---|---|---|---|---|
| Display / hero | 600–700 | 40–56px | `text-4xl` to `text-5xl` | Used sparingly. One per view. |
| Section heading | 600 | 24–32px | `text-2xl` to `text-3xl` | Wayfinding; establishes hierarchy. |
| Subheading | 500 | 18–20px | `text-lg` to `text-xl` | Supports without competing. |
| Body | 400 | 16px | `text-base` | Line-height 1.5. Comfortable reading. |
| UI / buttons | 500 | 14–16px | `text-sm` to `text-base` | Slight tracking on labels. |
| Captions / metadata | 400 | 12–14px | `text-xs` to `text-sm` | Secondary info; muted color. |

Weights available: 300 · 400 · 500 · 600 · 700 · 800 (per Host Grotesk shipped variants).

## When to use

- Picking a type style for a new heading, body, or label
- Reviewing existing typography for system consistency
- Defining responsive type scaling
- Pairing weight + size + line-height for a specific role
- Auditing a project for off-scale type sizes

**Skip when:**

- The work is layout / grid (use `manfred-ui-design:layout-grid`)
- The work is content / copy (use `manfred-toolkit:ux-writing`)
- The work is component spec (use `manfred-design-systems:component-spec`)
- The work is icon sizing (use `manfred-design-systems:icon-system`)

## Pre-flight

```bash
test -f ~/.claude/shared/DESIGN.md && sed -n '/^## 3/,/^## /p' ~/.claude/shared/DESIGN.md
```

Section 3 is the source of truth. Note: type values are tokens via Tailwind's `@theme` — no raw `font-size: 17px` in components.

## The hard rules

| Rule | What it means |
|---|---|
| **Host Grotesk for UI** | All UI typography uses Host Grotesk. Per `~/.claude/shared/DESIGN.md` Section 3. |
| **Guttery for logotype only** | The Manfred wordmark uses Guttery (a display face). Don't use Guttery anywhere else. |
| **Body minimum 16px** | Body text smaller than 16px is a readability regression. Use `text-sm` (14px) for captions / metadata only. |
| **Limit to 4–5 sizes per view** | Beyond that, hierarchy breaks. Use weight + colour for variations within a size. |
| **Use the scale, not arbitrary px** | Tailwind type sizes are tokens. Never `text-[17px]`. If a value isn't on the scale, round to the nearest scale step. |
| **Line lengths 45–75 characters** | Optimal for reading. Long lines (>90ch) and short lines (<40ch) both fatigue. Use `max-w-prose` for body content. |
| **Title case for display, sentence case for UI** | Display headings can use title case; UI labels and buttons are sentence case ("Save changes" not "Save Changes"). |
| **Mathematical ratio for harmony** | Manfred's scale uses ~1.25 ratio (major third) to give consistent steps. Don't introduce off-ratio sizes. |
| **Real content, not lorem ipsum** | Test type at the actual content length. Long names, long emails, long titles all break designs that look fine in lorem. |
| **Performance budget** | Per principle 13: only ship the weights you use. Each unused weight is a kilobyte loss. |

## Responsive typography

Headings scale down on mobile; body stays consistent.

```tsx
<h1 className="text-3xl md:text-4xl lg:text-5xl">Display heading</h1>
<h2 className="text-2xl md:text-3xl">Section heading</h2>
<p className="text-base">Body — same on every breakpoint, 16px minimum.</p>
```

For truly fluid scaling (between breakpoints), use Tailwind v4's `@theme` with `clamp()` values or Tailwind's responsive prefix steps. Don't shrink body below 16px.

## Line height

| Use | Line-height |
|---|---|
| Display headings | 1.1–1.2 (`leading-tight`) |
| Section headings | 1.2–1.3 |
| Body | 1.5 (`leading-normal`) — comfortable reading |
| Long-form reading | 1.6–1.75 (`leading-relaxed`) |
| UI labels | 1.2–1.4 |

## Letter spacing

| Use | Letter-spacing |
|---|---|
| Large display | -0.02em (`tracking-tight`) |
| Body | 0 (`tracking-normal`) |
| Uppercase labels / captions | 0.05em (`tracking-wide`) |
| All-caps headings (rare) | 0.1em |

## Font pairing

Manfred ships one face for UI (Host Grotesk) plus the logotype face (Guttery). Pairing rules:

- **UI / body**: Host Grotesk
- **Logotype**: Guttery (logotype only)
- **Code / data / technical content**: a monospace face — `JetBrains Mono`, `SF Mono`, or `ui-monospace` fallback. Define per project.

Avoid introducing additional faces. Each new face is a perf hit (font file size + render delay) and a brand drift risk.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Body at 14px feels more compact" | And less readable. 16px minimum for body text — design principle 5 (accessible first). |
| "Just `text-[17px]` to match Figma" | Either Figma is on the scale, or Figma is wrong. Round to `text-base` (16px) or `text-lg` (18px). |
| "I'll mix faces — Inter for UI, serif for headings" | Each new face costs bytes and brand consistency. Use Host Grotesk; vary by weight + size + color. |
| "Title Case For All UI Labels" | Sentence case for UI. Title case is for marketing display headings. |
| "Letter-spacing: 0.001em looks slightly better" | Doesn't matter at body sizes. Use the named tracking values (`tracking-normal` etc.) — invented offsets are noise. |
| "Display can be 80px on hero pages" | Probably too big. Test at actual viewport sizes; on mobile, `text-5xl` (56px) is usually plenty. |

## Red flags — STOP

- About to use a font size not on the scale
- About to use Guttery anywhere outside the logotype
- About to ship body text smaller than 16px
- About to use 6+ type sizes in one view
- About to introduce a third font family
- About to use title case for UI labels
- About to ship without testing with real content
- About to ship type weights that aren't loaded (or aren't used)

## Manfred lens

Typography is **brand surface** — Host Grotesk + the scale carry Manfred's identity. Drift here breaks the visual language.

It's also **accessibility** (principle 5 — readable body, no tiny captions, contrast against background) and **performance** (principle 13 — every weight loaded is bytes).

## Cross-references

- `~/.claude/shared/DESIGN.md` Section 3 (Typography Rules) — the source of truth
- `~/.claude/shared/design-principles.md` principles 5 (accessible), 13 (performance)
- `manfred-ui-design:visual-hierarchy` — type is a hierarchy tool
- `manfred-ui-design:responsive-design` — for responsive type scaling
- `manfred-design-systems:design-token` — for type tokens at component level
- `manfred-toolkit:ux-writing` — for the content side

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md`, project's `tailwind.config`
- `manfred-design-systems:design-token` — for type token decisions
- `manfred-ui-design:visual-hierarchy` — for hierarchy decisions

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
