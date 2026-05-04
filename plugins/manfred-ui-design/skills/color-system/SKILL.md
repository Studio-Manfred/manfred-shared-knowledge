---
name: color-system
description: Use when defining or extending colour at palette / page / surface level — anyone says "give me a colour palette", "what colours should this feature use", "design a colour system", "palette for X feature", "primary/secondary/accent for…", "pick brand colours", "feature page colours", "section palette", "palette generation". Manfred-specific: enforces the existing 6-colour palette from `~/.claude/shared/DESIGN.md`; refuses hex generation; distinguishes literal brand utilities from semantic tokens.
---

# color-system

Manfred ships six brand colours and a semantic / shadcn token layer on top. This skill is the gate that stops new palette generation. Every "give me colours for X" gets routed back to the existing token surface; every gap gets surfaced as a design-system decision, not a feature-page invention.

For component-level colour decisions ("which token does this Card use?"), use `manfred-design-systems:design-token`. This skill operates one level up — palette / page / surface.

## Overview

Manfred's palette (per `~/.claude/shared/DESIGN.md` Section 2):

| Name | Token | Hex | Role |
|---|---|---|---|
| Almost Black | `--color-almost-black` | `#1e1e24` | Primary text. Dark surfaces. |
| Business Blue | `--color-business-blue` | `#2c28ec` | Brand primary. CTAs, focus rings, links, interactive surfaces. |
| Human Pink | `--color-human-pink` | `#efd6d3` | Warm accent surface. Callouts, highlights, moments of care. |
| Beige | `--color-beige` | `#e6dcc8` | Neutral warm surface. Cards, sections, secondary backgrounds. |
| Light Beige | `--color-light-beige` | `#f4f3e8` | Default warm canvas. Page background in light mode. |
| White | `--color-white` | `#ffffff` | Default surface, inverse text on dark/brand backgrounds. |

Three layers (per `manfred-design-systems:design-token`):

1. **Primitives** — the six brand colours above. Components never reach this layer directly.
2. **Semantic aliases** — `--color-text-primary`, `--color-interactive-brand-bg`, etc. Theme-aware. Flip in dark mode.
3. **shadcn contract** — `--background`, `--foreground`, `--primary`, `--accent`, `--muted`, `--destructive`, `--border`, `--ring`. What components consume.

Two utility families in Tailwind:

- **Brand utilities** (`bg-business-blue`, `bg-human-pink`, `bg-beige`) — literal; do **not** flip in dark mode. Only for explicit literal-brand surfaces.
- **Semantic utilities** (`bg-background`, `bg-card`, `bg-primary`, `text-foreground`) — flip with theme. Default for components.

## When to use

- Designer asks for a palette for a new feature, page, or section
- Designer asks "what colours should we use for X"
- Reviewing a design that introduces colours not in the system
- Spec'ing a sub-brand or campaign palette
- Translating a competitor / inspirational palette into Manfred's system

**Skip when:**

- The user wants component-level CSS ("give me CSS for this Card") — use `manfred-design-systems:design-token`
- The user wants a colour audit across a project — use `manfred-toolkit:design-token-audit`
- The user wants dark-mode-specific design — use `manfred-ui-design:dark-mode-design`
- The user wants data-viz-specific colour work — use `manfred-ui-design:data-visualization`

## Pre-flight (do this every time)

```bash
test -f ~/.claude/shared/DESIGN.md && head -100 ~/.claude/shared/DESIGN.md
```

Find Section 2 (Color Palette & Roles), Section 9 (Dark Mode), and Section 11 (Do's and Don'ts). The six brand colours plus the semantic / shadcn contract are the entire surface — there is no "extra" palette to discover.

If `~/.claude/shared/DESIGN.md` is unreadable, ask the user to install `manfred-shared-knowledge` or paste the relevant sections. **Do not draft a palette without seeing the brand surface first.**

## The hard rules

| Rule | What it means |
|---|---|
| **Never generate hex** | Manfred's six brand colours exist; new hex values bypass them. If a request seems to need a new colour, the answer is one of the (a)/(b)/(c) options below — never "here's a new hex". |
| **Refuse semantic invention** | Manfred's palette doesn't ship `success`/`warning`/`error`/`info` greens or ambers. The skill refuses to invent and offers existing alternatives or a system-level addition path. (Same as `manfred-design-systems:design-token`; same refusal pattern.) |
| **Brand utilities don't flip; semantic tokens do** | `bg-business-blue` is literal — same value in dark mode. `bg-primary` is theme-aware — flips automatically. The output names which utility belongs where. |
| **Three-layer architecture** | Components consume layer 2/3. Never tell a designer to use a primitive directly in a component. |
| **Manfred isn't generic-fintech** | "Modern and trustworthy" doesn't mean "Slate + Indigo". Manfred's identity is `business-blue` + `human-pink` + warm neutrals — deliberately not generic-fintech. Push back on briefs that imply otherwise. |
| **Existing primary already exists** | Almost every "primary brand-feeling colour" ask resolves to `business-blue`. Don't invent a new one. |
| **Dark mode day-one** | Every palette decision states what happens in dark mode. Brand utilities stay literal; semantic tokens flip; verify contrast in both. |

## The flow

### Step 1 — Confirm what the user actually needs

Most "palette for X" requests resolve to one of three things. Diagnose first:

| What they asked for | What they probably need |
|---|---|
| "Primary brand colour" | `business-blue` (already exists) |
| "Background for the page" | `bg-background` (semantic — light-beige in light mode, almost-black in dark) |
| "Cards / sections" | `bg-card` or `bg-muted` (semantic) — or `bg-beige` (brand utility) for warm-emphasis surfaces |
| "Accent for highlights / callouts" | `bg-human-pink` (brand utility) for literal warm-emphasis, or `bg-accent` (semantic) for theme-aware |
| "Text" | `text-foreground` (semantic) for body, `text-muted-foreground` for secondary |
| "Borders" | `border-border` (semantic) |
| "Destructive action" | `bg-destructive` (semantic — this one ships) |
| "Success / warning / info state" | **Stop.** These don't ship. See Step 3. |

If everything resolves to existing tokens — that's the answer. Tell the user; cross-reference `manfred-design-systems:design-token` for component-level usage.

### Step 2 — Surface the warm-background rhythm

Manfred's visual rhythm: `light-beige` canvas alternates with `white` or `beige` cards. Avoid gray-on-gray (per `~/.claude/shared/manfred-brand.md` and DESIGN.md Section 11 — "Don't reach for gray when warm neutral works").

When designing a new feature page:

- **Page background**: `bg-background` (resolves to `light-beige` in light mode, `almost-black` in dark)
- **Primary cards / surfaces**: `bg-card` or `bg-white` (theme-aware) — sits on warm canvas, not on white-on-white
- **Warm-emphasis cards / callouts**: `bg-human-pink` or `bg-beige` (brand utilities — literal, don't flip)
- **Brand-emphasis cards** (rare): `bg-business-blue` with `text-white`

If the design needs more contrast between sections than `card` / `background` provides — reach for `bg-beige` (brand utility, warm) before any gray.

### Step 3 — Refuse semantic invention

When the user asks for `success` / `warning` / `error` / `info`:

```
Manfred's palette ships six brand colours plus the shadcn contract — no
canonical success/warning/info green or amber.

Three options:

  (a) Add to the design system — pick or add a primitive (e.g. a green for
      success, an amber for warning), wire into tokens.css + @theme,
      verify 4.5:1 contrast on every surface it'll sit on. Token PR first,
      feature PR second. Cost: 30–60 min. Required: a Linear ticket for
      the token + contrast-checked on every surface where the token will
      land before any hex is committed. Without those two, path (a) is
      just a hex leak with extra steps.

  (b) Reuse existing semantic — `bg-destructive` ships for negative.
      `bg-muted` works for neutral / pending. (Note: `bg-accent` resolves
      to `human-pink`, which means "moment of care" — overloading it as
      "success" creates the same semantic-collision problem as misusing
      brand utilities. Avoid.)

  (c) Status by icon + copy + neutral surface — `bg-muted` + check / alert
      / info icon + descriptive label carries meaning without colour
      doing the work. Most accessible.

Which way? I'm not going to invent a green and call it a token.
```

This is the same refusal pattern as `manfred-design-systems:design-token`. Same logic; different unit of work (palette / page level vs component level).

### Step 4 — Output the palette

Once the token mapping is clear:

```markdown
## Palette for <feature / page>

**Background rhythm**
- Page: `bg-background` (semantic, light-beige in light mode)
- Sections / cards: `bg-card` (semantic, white on light, almost-black on dark)
- Warm-emphasis cards: `bg-human-pink` or `bg-beige` (brand utilities, literal)

**Text**
- Primary: `text-foreground` (semantic)
- Secondary: `text-muted-foreground` (semantic)
- Inverse (on `bg-business-blue` etc.): `text-white`

**Interactive**
- Primary CTA: `bg-primary` (semantic, business-blue in both modes)
- Focus ring: `ring-ring` (semantic, business-blue)
- Links: `text-primary`
- Destructive action: `bg-destructive`

**Specific surfaces**
- [Smart Insights cards: `bg-card border-border` for default; `bg-human-pink border-business-blue/20` for "highlight" insights]
- [Recommendation status: see step 3 — refused semantic invention; recommend option (b) or (c)]

**Dark mode**
- All semantic tokens flip automatically (per `~/.claude/shared/DESIGN.md` Section 9)
- Brand utilities (`bg-business-blue`, `bg-human-pink`, `bg-beige`, `bg-light-beige`) stay literal
- Verified: contrast for body text (`text-foreground` on `bg-background`) ≥ 7:1 in both modes
```

If new tokens are required (semantic invention path (a)), name them explicitly and queue a `manfred-design-systems:design-token` work item before the feature can ship.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Quick is fine, designs are due Friday" | Friday is the reason to *use the existing system*, not bypass it. The system is the fast path. |
| "Modern and trustworthy" → "must be Slate + Indigo" | "Modern and trustworthy" in Manfred's vocabulary looks like `business-blue` + warm neutrals. The pink + beige + electric-blue combo is deliberately not generic-fintech — that's the brand argument. Refuse the generic translation. |
| "Just give me hex; the dev will translate to tokens" | They won't. Hex leaks into PRs. Token references force the right value at write-time. |
| "We need success/warning/info — every fintech has them" | Manfred's palette is intentionally narrower. If the feature needs status states, route through the (a)/(b)/(c) menu. Inventing colours under pressure produces token rot. |
| "Use the secondary / accent for variety" | "Variety" is a feature factory's job. Manfred is `business-blue` for action + warm neutrals for room + `human-pink` for moments of care. Resist the urge to expand. |
| "Dark mode can be done later" | Manfred ships dark day-one (principle 9). Use semantic tokens from the start; dark mode is free. Brand utilities go in places where literal-brand is intentional. |
| "It's just one feature page; it can have its own palette" | Feature-page palettes are how design systems rot. One feature's palette becomes the next feature's "well, the X tab does it". Use the system. |
| "I'll use brand utilities (`bg-human-pink`, `bg-business-blue`) to mean status (positive / urgent / etc.)" | Brand utilities are literal-brand surfaces, not meaning carriers. Using `bg-human-pink` for "positive insight" overloads it — pink already means *moment of care*. Future designer hits a pink callout and can't tell which meaning. Same problem with using `business-blue` as "urgent" — collapses the action layer. Brand-decoration and meaning-carrying are separate layers; collapsing them is the rot the three-layer architecture exists to prevent. |

## Red flags — STOP

- About to emit a hex value that isn't one of Manfred's six brand colours
- About to use a Tailwind palette colour (`bg-slate-900`, `bg-indigo-600`) that bypasses Manfred's tokens
- About to invent a `success` / `warning` / `info` token without routing through (a)/(b)/(c)
- About to recommend a "secondary" or "accent" colour Manfred doesn't ship
- About to tell a designer to flip a brand utility (`bg-business-blue`) in dark mode — brand utilities are literal, they don't flip
- About to ship a palette without naming what happens in dark mode
- About to accept "modern and trustworthy" as license to translate to generic-fintech (Slate / Indigo)

## Manfred lens

Colour decisions are **brand surface** — they touch every other Manfred surface that respects the palette. Drift here drifts everything. They're also a **usability** surface (contrast for text + UI components, colour-blind safety) and an **accessibility** surface (WCAG 2.2 AA contrast minimums per principle 5; never colour-alone for meaning per principle 15).

Critical & ethical (principle 6): colour can be used manipulatively (red for "danger" on a benign cancel button, urgent green on upsell CTAs). Refuse. Status colour follows status meaning, not engagement metric.

## Output format

For palette requests, return:

```markdown
## Tokens used (cross-check)
[List every token name referenced. If any aren't in `~/.claude/shared/DESIGN.md`, flag.]

## Palette
[The Step 4 markdown structure]

## Dark mode behaviour
[Verified: semantic tokens flip; brand utilities stay literal; contrast checked.]

## Token additions needed
[None — used existing tokens]
[OR: Need `--color-success` (semantic) + the primitive it resolves to. Queue token PR via `manfred-design-systems:design-token` before feature ship.]
```

When the user asked for a state colour that doesn't exist, return the (a)/(b)/(c) prompt from Step 3 and **do not produce hex** until they pick.

## Cross-references

- `~/.claude/shared/DESIGN.md` — the brand colour table and three-layer architecture
- `~/.claude/shared/manfred-brand.md` — brand voice + visual-language anti-patterns (no gray-on-gray, flat first)
- `~/.claude/shared/design-principles.md` — principle 8 (use the tokens), principle 9 (dark mode day-one)
- `manfred-design-systems:design-token` — component-level colour decisions; sibling skill, different unit of work (palette/page → component)
- `manfred-design-systems:a11y-design` — for the contrast-verification pass at design stage
- `manfred-design-systems:a11y-qa` — for the runtime contrast gate
- `manfred-toolkit:design-token-audit` — for measuring how often the system is bypassed across a codebase
- `manfred-ui-design:dark-mode-design` — for the dark-mode-specific design pass
- `manfred-ui-design:data-visualization` — for data-viz-specific colour work (different rules — categorical, sequential, diverging)

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md`, `~/.claude/shared/manfred-brand.md`, `~/.claude/shared/design-principles.md`
- `Bash` — `head ~/.claude/shared/DESIGN.md` for pre-flight
- `manfred-design-systems:design-token` — for component-level handoff after palette decisions
- `manfred-design-systems:a11y-design` — for contrast verification
