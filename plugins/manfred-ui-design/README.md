# manfred-ui-design

Manfred-flavoured UI design: layout, colour, typography, responsive, dark mode, data viz, illustration, visual hierarchy. Hooks into `~/.claude/shared/DESIGN.md` tokens — no hex generation. Mobile first; flat first, depth is earned; Host Grotesk for UI; Manfred ships dark day-one.

## Skills

| Skill | When it triggers |
|-------|-----------------|
| `color-system` | "give me a colour palette", "what colours should this feature use", "design a colour system", "feature page colours", "section palette" — **foundational TDD'd skill**: refuses hex generation; routes to existing 6-colour palette; (a)/(b)/(c) menu when semantic doesn't exist; brand utilities vs semantic tokens distinguished |
| `dark-mode-design` | "dark mode design", "make this work in dark", "dark theme review", "dim mode", "OS dark mode", "prefers-color-scheme" — semantic tokens flip; brand utilities stay literal; verify contrast in both modes |
| `data-visualization` | "data viz", "chart design", "dashboard", "graph", "what chart should I use" — pick by question, not library; data-ink ratio; colour-blind safe; tokens not hex |
| `illustration-style` | "illustration style", "empty state illustration", "spot illustration", "hero illustration", "character design" — subset of brand palette; warm geometric defaults; dark variants day-one |
| `layout-grid` | "layout grid", "column grid", "12-column", "container width", "page margins", "gutters" — 12/8/4 cols (desktop/tablet/mobile); gutters from spacing tokens; mobile-first |
| `responsive-design` | "responsive", "mobile design", "breakpoint behaviour", "tablet layout", "mobile first" — design for content not devices; tested 320/768/1024/1440; touch ≥44px |
| `spacing-system` | "spacing system", "padding", "margin", "gap", "vertical rhythm", "compact mode" — 4px base; always use the scale; consistent within components |
| `typography-scale` | "type scale", "typography system", "font sizes", "what font size for X", "Host Grotesk" — Host Grotesk for UI; Guttery for logotype only; body 16px minimum; 4–5 sizes max per view |
| `visual-hierarchy` | "visual hierarchy", "what should the user see first", "primary action", "scan order", "F-pattern", "Z-pattern" — one primary action per view; squint test; hierarchy reinforces user intent |

## Commands

| Command | What it does |
|---------|--------------|
| `/manfred-ui-design:color-palette` | Define a colour palette for a feature/page/surface. Routes through tokens; refuses hex; surfaces semantic gaps. |
| `/manfred-ui-design:design-screen` | Design a screen end-to-end. Layout + responsive + palette + type + hierarchy + dark mode + a11y. |
| `/manfred-ui-design:responsive-audit` | Audit a screen / feature / project for responsive coverage. Block-merge / high-priority / cleanup findings with screenshots. |
| `/manfred-ui-design:type-system` | Define a type system for a project. Roles + responsive scaling + line-length + performance budget. |

## Manfred opinions baked in

- **Tokens from `~/.claude/shared/DESIGN.md`** — every visual output references the token layer; no hex generation
- **Three-layer architecture** — primitives → semantic → shadcn contract; brand utilities don't flip, semantic tokens do
- **Host Grotesk for UI; Guttery for logotype only** — typography skills enforce
- **Warm-background rhythm** — `light-beige` canvas alternates with `white` or `beige` cards; avoid gray-on-gray
- **Flat first, depth is earned** — no heavy shadows, gradients, neumorphism unless functional
- **Mobile first** (principle 12) — design for 320px first; expand
- **Dark mode day-one** (principle 9) — use semantic tokens; dark mode is free
- **Performance is a feature** (principle 13) — typography, illustration, viz skills note bundle / font-loading impact
- **One primary action per view** — visual hierarchy reinforces user intent, not stakeholder politics

## Cross-plugin handoffs

- **Built on `manfred-design-systems:design-token`** — the token layer this plugin consumes; component-level token decisions defer there
- **Feeds `manfred-design-ops:handoff-spec`** — visual artifacts spec'd via the handoff skill
- **Pairs with `manfred-design-systems:a11y-design` + `a11y-qa`** — every visual decision gets the contrast + focus + reduced-motion check
- **Pairs with `manfred-design-systems:theming-system`** — for the architectural side of dark mode
- **Pairs with `manfred-toolkit:design-token-audit`** — for measuring token bypass across a codebase
- **Pairs with `manfred-toolkit:ux-writing`** — for empty-state and error copy that pairs with illustrations

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-ui-design@manfred
```
