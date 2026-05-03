---
name: theming-system
description: Use when designing or extending Manfred's theming architecture — anyone says "add a theme", "white-label", "sub-brand", "dark mode", "high contrast", "theme switcher", "OS theme preference", "tokens per theme", "Figma variable modes", "test in dark mode", "compact density mode". Stack: Tailwind v4 + CSS custom properties + shadcn token contract + Manfred design system.
---

# theming-system

Themes are token overrides, not parallel codebases. Get the token layers right and a new theme is a CSS file. Get them wrong and a new theme is a rewrite.

## Overview

Manfred's theming sits on the same three-layer architecture as `manfred-design-systems:design-token`: primitives → semantic → shadcn contract. Themes override at **layer 2** (semantic) — never at the component level, never directly at the primitive level except to add new primitives a theme needs.

Two axes:

- **Mode** — light, dark (Manfred ships both day-one), high-contrast (optional)
- **Brand** — default Manfred, sub-brand, white-label, seasonal

Plus density (`comfortable`, `compact`, `spacious`) if the project needs it.

## When to use

- Adding dark mode to a project that ships only light (rarer at Manfred — design system ships dark day-one, but project apps may have lagged)
- Adding a sub-brand, white-label, or seasonal theme
- Adding a high-contrast or reduced-motion mode
- Reviewing whether a theme is implemented correctly (does it actually override the right layer?)
- Setting up a theme switcher in a project (toggle, OS preference, persisted)

**Skip when:**

- The user wants to change a token value (use `manfred-design-systems:design-token`)
- The user wants to style one component differently in one place (variant prop, not a theme)
- The "theme" is one screen with a different background (just use brand utilities)

## Pre-flight

Before adding or extending a theme:

```bash
test -f src/tokens/tokens.css && head -50 src/tokens/tokens.css
test -f src/styles/themes/dark.css && head -30 src/styles/themes/dark.css
grep -n "@theme\|\.dark" src/**/*.css 2>/dev/null | head -20
```

Find:

1. How layer 2 (semantic) is currently defined
2. Whether dark mode already exists (it should — Manfred design system ships it)
3. How themes are scoped (CSS class on `<html>` like `.dark`, attribute like `[data-theme="x"]`, or `@media (prefers-color-scheme)`)

## The architecture

Three layers, override at layer 2:

```
Layer 1 — Primitives (raw brand)
:root {
  --color-business-blue: #2c28ec;
  --color-almost-black: #1e1e24;
  --color-light-beige: #f4f3e8;
  --color-white: #ffffff;
}

Layer 2 — Semantic (theme-aware) ← THEMES OVERRIDE HERE
:root {
  --background: hsl(var(--color-light-beige));
  --foreground: hsl(var(--color-almost-black));
  --primary: hsl(var(--color-business-blue));
  --card: hsl(var(--color-white));
}

.dark {
  --background: hsl(var(--color-almost-black));
  --foreground: hsl(var(--color-light-beige));
  --primary: hsl(var(--color-business-blue));  /* same primitive, still works */
  --card: hsl(var(--color-almost-black) / 0.8);
}

Layer 3 — shadcn contract (consumed by components)
[same as semantic — components read --background, --foreground, --primary]
```

Components consume `--background` / `--foreground` / `--primary` etc. They never know which theme is active. Switching themes = switching the layer-2 values under a class/attribute. That's it.

## Theme types

| Type | Override scope | Example |
|---|---|---|
| **Mode** (light / dark / high-contrast) | Semantic (layer 2). Same primitives, different semantic mapping | `.dark { --background: …almost-black; --foreground: …light-beige }` |
| **Brand** (sub-brand, white-label) | Primitives (layer 1) + semantic (layer 2). New brand colour primitive, mapped through semantic | `[data-brand="acme"] { --color-brand-primary: #ff6600; --primary: var(--color-brand-primary) }` |
| **Density** (comfortable / compact / spacious) | Spacing primitives (layer 1) | `[data-density="compact"] { --spacing-2: 0.25rem; --spacing-4: 0.5rem }` |

Combinations stack: `<html class="dark" data-brand="acme" data-density="compact">` — each scope contributes its overrides, components stay unchanged.

## Dark mode — Manfred specifics

Manfred design system ships dark day-one (`~/.claude/shared/DESIGN.md` Section 9). Rules:

- **Don't invert.** Light → dark is not "swap white and black". Reduce brightness thoughtfully.
- **Lighter surfaces for elevation, not heavier shadows.** In dark mode, elevated surfaces get *lighter*, not heavier shadows. (Material Design's surface tinting model.)
- **Desaturate for dark backgrounds.** Bright primary colours often feel aggressive on dark. Reduce saturation 10-20% in the dark token mapping.
- **Test text legibility carefully.** Body text on dark background needs more contrast than the WCAG minimum to feel comfortable. Aim 7:1 (AAA) for body, not just 4.5:1.
- **Image / illustration variants.** Logo plates, hero illustrations, screenshots — provide a dark variant or a neutral background container that works in both.
- **Brand utilities don't flip.** `bg-business-blue` is literal; in dark mode it's still `#2c28ec`. Pair with an absolute foreground (`text-white`) that also doesn't flip — see `manfred-design-systems:design-token`.

## Implementation patterns

### Theme switcher (toggle + persisted)

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

### OS preference, no toggle

```tsx
useEffect(() => {
  const mq = window.matchMedia('(prefers-color-scheme: dark)');
  const apply = () => document.documentElement.classList.toggle('dark', mq.matches);
  apply();
  mq.addEventListener('change', apply);
  return () => mq.removeEventListener('change', apply);
}, []);
```

### Figma variable modes

Themes mirror in Figma using **variable modes** (Color collection has `Light` / `Dark` modes; Brand collection has `Manfred` / `Acme` modes). Component instances inherit the active mode — designers can preview the same composition in any theme without duplicating frames.

## The hard rules

| Rule | What it means |
|---|---|
| **Themes override at layer 2 (semantic)** | Components consume layer 3 (shadcn contract). Themes redefine layer 2. Layer 1 (primitives) only gets new entries when a theme needs a colour the brand doesn't ship. |
| **Components never know which theme is active** | If a component has `if (theme === 'dark')` logic, that's a token failure. The token should already be different. |
| **Test every component in every theme** | Storybook + theme switcher addon. CI screenshot diff per theme. Don't ship a theme without verifying every shipped component renders correctly in it. |
| **Respect OS preference by default** | First load uses `prefers-color-scheme`. User toggle persists and overrides. Don't lock to light. |
| **Accessibility floor doesn't change between themes** | WCAG 2.2 AA in light = WCAG 2.2 AA in dark. Re-run `manfred-design-systems:a11y-qa` per theme. |

## Common rationalisations

| Excuse | Reality |
|---|---|
| "I'll add dark mode after launch" | Use semantic tokens from day-one and dark mode is a CSS file. Add it later and it's a rewrite of every component that hardcoded a colour. |
| "Just invert the colours for dark mode" | No. Dark UI design is its own discipline — surface elevation, desaturation, image treatment. Inversion produces ugly, hard-to-read interfaces. |
| "We don't need to test dark mode in QA, the tokens flip automatically" | Tokens flip; *contrast* doesn't. Run `manfred-design-systems:a11y-qa` per theme. Contrast failures hide in dark mode often. |
| "I'll add a sub-brand by overriding in components" | Sub-brand overrides go in tokens, not components. Component-level overrides scatter brand decisions across the codebase — unfixable later. |
| "High contrast is a niche, skip it" | Forced-colors mode (`@media (forced-colors: active)`) is the high-contrast surface. Test once, ship once. |

## Manfred lens

Theming is **infrastructure** — Cagan/Torres lens doesn't apply directly. But theming touches **brand consistency** (every theme should still feel like Manfred unless it's an explicit white-label) and **accessibility** (per-theme contrast). Both are testable; both are worth treating as gates, not afterthoughts.

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md` Section 9 (Dark Mode), Section 2 (Color)
- `Bash` / `Grep` — survey current theme implementation
- `manfred-design-systems:design-token` — for the token-layer rules
- `manfred-design-systems:a11y-qa` — to verify contrast per theme
- Storybook + Storybook themes addon — for per-theme visual review

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
