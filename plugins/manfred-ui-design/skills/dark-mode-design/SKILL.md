---
name: dark-mode-design
description: Use when designing or reviewing dark-mode interfaces — anyone says "dark mode design", "design dark mode", "make this work in dark", "dark theme review", "dark UI", "dim mode", "dark variant", "OS dark mode", "prefers-color-scheme". Manfred-flavoured: shipped day-one (principle 9); semantic tokens flip automatically; brand utilities stay literal; verify contrast in both modes.
---

# dark-mode-design

Manfred ships dark mode day-one — not as a "phase 2" feature. The token system makes it nearly free if you use semantic tokens; expensive if you don't. This skill is the design-side guide for getting dark mode right at the visual layer.

For the architectural side (which tokens flip, how they're defined), see `manfred-design-systems:theming-system`. For component-level dark behaviour, see `manfred-design-systems:design-token`.

## Overview

Dark mode is not "swap white and black". The discipline:

- Reduce overall luminance (eye strain)
- Use surface elevation through *lighter* shades, not heavier shadows
- Desaturate bright colours for dark backgrounds
- Maintain contrast — 4.5:1 minimum for body, 7:1 (AAA) preferred for comfort
- Provide image / illustration variants where needed

Manfred's dark mode (per `~/.claude/shared/DESIGN.md` Section 9):

- Background: `--color-almost-black` (`#1e1e24`)
- Foreground: warm light tone, not pure white (avoids harsh contrast)
- Brand utilities (`bg-business-blue`, `bg-human-pink`, `bg-beige`, `bg-light-beige`) **stay literal** — they don't flip
- Semantic tokens (`bg-background`, `bg-card`, `bg-primary`, `text-foreground`, `border-border`) flip automatically when `.dark` is set on `<html>`

## When to use

- Designing a new feature with dark mode in mind from day one
- Auditing an existing surface for dark-mode coverage
- Resolving a "this looks wrong in dark mode" bug at the design stage
- Picking image / illustration variants for dark mode
- Reviewing a component that uses brand utilities — does the surrounding context work in both modes?

**Skip when:**

- You want to set up the theming architecture itself — use `manfred-design-systems:theming-system`
- You want component-level token decisions — use `manfred-design-systems:design-token`
- You want palette-level decisions — use `manfred-ui-design:color-system`
- You want the runtime contrast gate — use `manfred-design-systems:a11y-qa`

## Pre-flight

```bash
test -f ~/.claude/shared/DESIGN.md && sed -n '/^## 9/,/^## /p' ~/.claude/shared/DESIGN.md
```

Section 9 is the source of truth on Manfred's dark behaviour.

## The hard rules

| Rule | What it means |
|---|---|
| **Don't invert** | Light → dark is not "swap colours". Reduce brightness; redesign surfaces. |
| **Surface elevation through lighter shades** | In dark mode, elevated surfaces get *lighter*, not heavier shadows. (Material's surface-tinting model.) |
| **Desaturate brights for dark** | Saturated colours feel aggressive on dark. Reduce saturation 10–20% in the dark token mapping. (Manfred's primitives are already moderate; this matters most for any added semantic states like success / warning.) |
| **Off-white over pure white** | Body text on dark uses warm-light, not `#FFFFFF`. Pure white on dark causes vibration and eye strain. |
| **Brand utilities don't flip** | `bg-business-blue` is literal in both modes. Pair with absolute foregrounds (`text-white`) so contrast works in both. |
| **Semantic tokens flip automatically** | `bg-background`, `bg-card`, `text-foreground`, `border-border` all flip via the `.dark` class. Using them = dark mode is free. |
| **Contrast verified per mode** | WCAG 2.2 AA in light = WCAG 2.2 AA in dark. Don't assume; verify with `manfred-design-systems:a11y-qa`. |
| **Image / illustration variants** | Logos and illustrations may need dark variants. Hero images may need dimmed overlays. Plan; don't punt. |

## The flow

### Step 1 — Identify which mode-aware surfaces are at play

For each surface in the design:

| Surface type | Token | Behaviour |
|---|---|---|
| Page canvas | `bg-background` (semantic) | Light-beige in light mode, almost-black in dark |
| Cards / sections | `bg-card` (semantic) | White on light, dark surface on dark |
| Warm-emphasis cards | `bg-beige` / `bg-human-pink` (brand utilities) | Stay literal — beige stays beige in dark |
| Brand-emphasis | `bg-business-blue` (brand utility) | Stays literal — pair with `text-white` (also literal) |
| Body text | `text-foreground` (semantic) | Almost-black on light, warm-light on dark |
| Secondary text | `text-muted-foreground` (semantic) | Flips automatically |
| Borders / dividers | `border-border` (semantic) | Flips |
| Focus ring | `ring-ring` (semantic; resolves to `business-blue`) | Flips? Note: business-blue stays — that's intentional |

If a surface uses a brand utility (literal), pair its foreground with another literal that works against it in both modes. `bg-business-blue` + `text-white` is the canonical pair.

### Step 2 — Walk the design in dark

Mentally toggle `.dark`. For each surface:

- **Contrast**: text + background pairing meets 4.5:1 (body) / 3:1 (large) / 3:1 (UI components)?
- **Elevation**: cards visible against background through *lighter shade*, not just shadow?
- **Saturation**: any added states (success / warning) feel too aggressive on dark? Desaturate.
- **Imagery**: photos / illustrations / logos render correctly? Or do they need dark variants?

### Step 3 — Image and illustration variants

Manfred's brand assets:

- **Logo**: Manfred wordmark has light + dark variants. Use the right one per mode.
- **Photography**: dimmed overlay (10–20% black) or alternative crop for dark mode. Bright photos against dark UI fight for attention.
- **Illustrations**: provide dark variants where the illustration uses light colours that wouldn't read on dark. `~/.claude/shared/DESIGN.md` Section 7 covers iconography + imagery.
- **Screenshots in marketing surfaces**: have a dark-mode screenshot ready or display in a neutral container.

### Step 4 — OS preference + manual toggle

Manfred respects `prefers-color-scheme` by default. Manual toggle persists override.

```tsx
function ThemeToggle() {
  const [theme, setTheme] = useState<'light' | 'dark'>(() => {
    const saved = localStorage.getItem('theme');
    if (saved === 'light' || saved === 'dark') return saved;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  });
  useEffect(() => {
    document.documentElement.classList.toggle('dark', theme === 'dark');
    localStorage.setItem('theme', theme);
  }, [theme]);
  return (
    <button
      onClick={() => setTheme(t => t === 'light' ? 'dark' : 'light')}
      aria-label={`Switch to ${theme === 'light' ? 'dark' : 'light'} mode`}
    >
      {theme === 'light' ? <MoonIcon aria-hidden /> : <SunIcon aria-hidden />}
    </button>
  );
}
```

(Same as `manfred-design-systems:theming-system` — that skill owns the architecture.)

## Common rationalisations

| Excuse | Reality |
|---|---|
| "I'll add dark mode after launch" | Use semantic tokens day-one and dark mode is a CSS file. Add it later and it's a rewrite. Manfred design principle 9 says day-one. |
| "Just invert the colours" | Inverted UI is harsh, hard to read, and aesthetically broken. Surface elevation, desaturation, image treatment — all matter. |
| "Pure white text on dark is fine" | It's not. Vibration + eye strain. Use `text-foreground` (semantic) which resolves to a warm-light off-white in dark. |
| "Drop shadows for elevation in dark" | Drop shadows on dark are nearly invisible. Use lighter surfaces for elevation in dark mode. |
| "We tested the design in light; dark is the same" | Tokens flip; *contrast* doesn't. Run `manfred-design-systems:a11y-qa` per mode. |
| "Brand utilities should flip too — `business-blue` looks too bright on dark" | If `business-blue` looks too bright, adjust the brand utility's literal value with the design-system team — don't make it theme-aware. The literal-vs-semantic distinction is structural; collapsing it breaks every consumer. |

## Red flags — STOP

- About to recommend "just invert" or "swap white and black"
- Using `text-white` on a `bg-card` (semantic) — `card` flips, `text-white` is literal; contrast breaks in light mode
- Using `text-black` anywhere — same problem, opposite direction
- About to use a heavy drop shadow for elevation in dark mode
- About to ship without verifying contrast in both modes
- About to make a brand utility (`bg-business-blue`) theme-aware
- About to ship illustrations / photos without considering dark-mode variants

## Manfred lens

Dark mode touches **accessibility** (principle 5 — contrast, eye strain, screen reader announcements of mode) and **usability** (principle 7 — simple defaults; users shouldn't fight the OS). Principle 9 is the explicit commitment: components ship dark day-one or they aren't done.

Critical & ethical (principle 6): some apps default to dark to feel "premium" while making the dark mode harder to read or use. Refuse that pattern. Light and dark are peers, not premium / standard.

## Cross-references

- `~/.claude/shared/DESIGN.md` Section 9 (Dark Mode) — the source of truth
- `~/.claude/shared/design-principles.md` principle 9
- `manfred-design-systems:theming-system` — for the architectural layer (how themes are defined)
- `manfred-design-systems:design-token` — for component-level token decisions
- `manfred-ui-design:color-system` — for palette-level decisions
- `manfred-design-systems:a11y-qa` — runtime contrast gate per mode
- `manfred-design-systems:a11y-design` — design-stage contrast annotation per mode

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md`, prior dark-mode designs
- `manfred-design-systems:theming-system` — for architectural questions
- `manfred-design-systems:a11y-qa` — for runtime contrast verification

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
