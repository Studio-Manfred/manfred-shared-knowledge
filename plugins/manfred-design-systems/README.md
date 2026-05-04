# manfred-design-systems

Manfred-flavoured design systems work: tokens, components, theming, accessibility. Built on `~/.claude/shared/DESIGN.md`'s three-layer token architecture (primitives → semantic → shadcn contract). WCAG 2.2 AA baseline. Composition over wrapping (shadcn shapes are the contract, not the suggestion).

## Skills

| Skill | When it triggers |
|-------|-----------------|
| `design-token` | "give me CSS for…", "add a color/spacing/radius", "make a callout/badge", "what color should I use", "convert this hex to a token" — **foundational TDD'd skill**: refuses raw hex, refuses default Tailwind palette, refuses to invent missing semantics |
| `component-spec` | "spec a component", "what should the API for X look like", "design a Button variant", "props for…", "states for…" |
| `documentation-template` | "write docs for this component", "Storybook page for…", "MDX template", "what goes on a docs page" |
| `icon-system` | "add an icon", "what icon should I use", "icon size/naming", "SVG sprite", "icon accessibility" |
| `naming-convention` | "what should I call this", "rename this token", "PascalCase or kebab-case", "BEM", "Figma layer naming" |
| `pattern-library` | "what's the right pattern for…", "empty state pattern", "form error pattern", "loading pattern", "we keep solving this the same way" |
| `theming-system` | "add a theme", "white-label", "sub-brand", "dark mode", "high contrast", "theme switcher", "OS theme preference" |
| `a11y-design` | "review my design for accessibility", "annotate my Figma", "create a11y specs", "accessibility before handoff" — design-stage gate |
| `a11y-dev` | "make this accessible", "add ARIA", "fix accessibility", "WCAG", "screen reader support", "keyboard navigation", "focus management" — implementation gate |
| `a11y-qa` | "audit a11y", "test accessibility", "axe scan", "check WCAG compliance" — runtime gate (called by `manfred-dev:test-my-code` and `manfred-dev:release`) |

## Commands

| Command | What it does |
|---------|--------------|
| `/manfred-design-systems:audit-system` | Audit a project for token compliance + a11y + naming + dark-mode coverage. Produces a markdown report with prioritised fixes. |
| `/manfred-design-systems:create-component` | Create a new component end-to-end — spec → tokens → accessible implementation → docs page → a11y gate. |
| `/manfred-design-systems:tokenize` | Convert hardcoded values (hex, default Tailwind palette, phantom tokens) into Manfred tokens. Surfaces missing tokens; refuses to invent. |

## Cross-plugin handoffs

- **`manfred-dev:test-my-code` and `manfred-dev:release`** call `manfred-design-systems:a11y-qa` for the runtime accessibility gate
- **`manfred-design-research:usability-test-plan`** outputs accessibility findings that cross over into `manfred-design-systems:a11y-qa` for code-side fixes
- **`manfred-design-research:usability-test-plan`** validates new patterns from `manfred-design-systems:pattern-library` before promoting from `experimental` to `stable`

## Manfred opinions baked in

- **Tokens from `~/.claude/shared/DESIGN.md`** — every colour, spacing, radius, shadow output references existing tokens; fails loudly when asked to hardcode
- **Business-blue + human-pink + warm neutrals** — Manfred's palette doesn't ship `success`/`warning`/`info` greens or ambers. The skill refuses to invent them and offers (a) add to semantic layer, (b) reuse existing semantic, (c) neutral surface + icon
- **WCAG 2.2 AA baseline** — Manfred design principle 5; every component/pattern skill checks this floor
- **shadcn shapes are the contract** — Manfred design principle 10; component specs mirror stock shadcn APIs (Dialog, Tooltip, RadioGroup, Toast, Popover) for composability
- **Dark mode day-one** — `~/.claude/shared/DESIGN.md` Section 9; semantic tokens flip automatically, brand utilities stay literal

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-design-systems@manfred
```

## Migrating from `manfred-a11y`

Pre-v1.0.0, the three a11y skills (`a11y-design`, `a11y-dev`, `a11y-qa`) lived in the now-removed `manfred-a11y` plugin. They live here now. If you're still on a v0.15.x–v0.21.x install, uninstall the old plugin and install this one:

```
/plugin install manfred-design-systems@manfred
/plugin uninstall manfred-a11y@manfred
```
