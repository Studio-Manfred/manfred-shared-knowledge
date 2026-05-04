---
name: data-visualization
description: Use when designing charts, dashboards, or any data viz — anyone says "data viz", "chart design", "dashboard", "graph", "visualisation", "what chart should I use", "design a sparkline", "data colours", "chart accessibility". Manfred-flavoured: chart selection follows the question; colour from the token layer; accessibility never optional.
---

# data-visualization

Data viz is communication, not decoration. The right chart answers the user's question; the wrong chart obscures it. This skill picks chart types for specific questions, designs them against the Manfred token system, and bakes accessibility in from the start.

## Overview

Five question types map to five chart families. Pick by the question, not by what's available in the chart library:

| Question | Chart family |
|---|---|
| Compare values across categories? | Bar charts (vertical / horizontal / grouped / bullet) |
| How does X change over time? | Line charts (continuous) / area charts (volume) / sparklines (inline) |
| What share of the whole? | Pie / donut (≤4 categories) / stacked bar (more categories) / treemap (hierarchical) |
| What's the distribution? | Histogram / box plot / scatter |
| What's the relationship between two variables? | Scatter / bubble / heat map |

## When to use

- Designing a dashboard or analytics page
- Picking the chart type for a specific data question
- Reviewing existing data viz for design or accessibility issues
- Designing an empty / loading / error state for a chart
- Defining chart styling tokens for a project

**Skip when:**

- The user wants generic palette work — use `manfred-ui-design:color-system`
- The user wants raw component code — use `manfred-design-systems:component-spec`
- The user wants a specific charting library setup — defer to project tech choices

## Pre-flight

Ask, before designing:

- **What's the question the chart answers?** "How did revenue change over time?" or "Which segment is biggest?" — specific question, not generic "show the data".
- **Who's the audience?** Executives → simpler, fewer data points. Analysts → more detail, drill-down.
- **What's the data shape?** Categorical / continuous / hierarchical / time series.
- **What's the medium?** Inline (sparkline), small (card-sized), large (full-width hero), interactive (hover + drill)?
- **Token surface** — `~/.claude/shared/DESIGN.md` for colour tokens, especially for categorical / sequential / diverging palettes.

If the user can't name the question — push back. Charts answering no question are decoration.

## The hard rules

| Rule | What it means |
|---|---|
| **Pick by the question, not the library** | A library that ships 50 chart types tempts variety. Pick the chart that answers the question — usually 1 of 4. |
| **Data-ink ratio** | Maximise data, minimise decoration. Drop chart junk (3D effects, gradient fills, drop shadows on bars). |
| **Y-axis at zero for bars** | Bars compare lengths. Truncating the y-axis makes small differences look big — visually dishonest. |
| **Direct labels over legends** | If you can label the line directly on the chart, do. Legends are a lookup tax. |
| **Colour-blind safe** | Don't rely on colour alone — pair with shape, label, or pattern. Use colour-blind safe sequences (avoid red-green). |
| **Tokens, not hex** | Categorical, sequential, diverging palettes resolve through tokens. If the system doesn't ship a data-viz palette, surface that as a design-system gap (don't invent). |
| **Accessibility per chart** | Text alternative, keyboard navigation for interactive charts, sufficient contrast for data elements. |
| **Responsive simplification** | At small sizes: fewer data points, larger labels, possibly a different chart entirely (table on mobile, chart on desktop). |

## Chart selection in detail

### Comparison
- **Vertical bar** — categorical comparison (default). Y-axis zero-based.
- **Horizontal bar** — when category labels are long or there are many categories.
- **Grouped bar** — multi-series comparison; use when comparison across groups matters more than total.
- **Bullet chart** — actual vs target with thresholds. Compact; good for KPI cards.

### Trend over time
- **Line chart** — continuous data, single or multi-series. Limit to 4–5 series before legend tax overwhelms.
- **Area chart** — volume + trend; good for cumulative or stacked metrics.
- **Sparkline** — inline trend at a glance, no axes needed. Pair with the latest value as text.

### Part of whole
- **Pie / donut** — ≤4 categories with clearly different sizes. More than 4 — use stacked bar.
- **Stacked bar** — comparison + composition; when both matter.
- **Treemap** — hierarchical part-of-whole; when categories nest.

### Distribution
- **Histogram** — frequency distribution of a continuous variable.
- **Box plot** — summary distribution; good for comparing distributions across categories.
- **Scatter** — when looking at every point, not just summaries.

### Relationship
- **Scatter** — two continuous variables; look for correlation, clusters, outliers.
- **Bubble** — three variables (x, y, size).
- **Heat map** — matrix of two categorical or binned-continuous variables.

## Colour in data viz

Three palette types — different rules per type:

### Categorical
Distinct hues for unrelated categories. Manfred's primary categorical palette emerges from the brand colours where they fit (`business-blue`, `human-pink`, `beige`); for more categories than the brand ships, it's a system-level gap (queue a token PR via `manfred-design-systems:design-token`).

Limit to 5–7 categorical colours. Beyond that, viewers can't distinguish or remember.

### Sequential
Light to dark for ordered data (e.g., low → high values). Single hue with stepped lightness.

If Manfred's tokens don't ship a sequential palette, route through `manfred-design-systems:design-token` — don't generate a custom one for one chart.

### Diverging
Two-hue scale with a midpoint (e.g., negative → zero → positive). Common: red ↔ blue with white middle.

Manfred's palette doesn't ship a diverging palette by default. Route through `manfred-design-systems:design-token` if the chart needs one.

## Accessibility

Per principle 5 + 15:

- **Don't rely on colour alone** — pair with shape, label, pattern, or position. A colour-blind user should still read the chart.
- **Text alternative** — every chart has an accessible name + summary description (e.g., for screen readers).
- **Keyboard navigation** — if the chart is interactive, keyboard users access every data point. Tab to chart, arrow keys to walk data points, Enter for detail.
- **Tooltips** — touch-friendly (>= 44px target), keyboard-triggerable, screen-reader announcements.
- **Sufficient contrast** — data elements ≥ 3:1 against background per WCAG 2.2.
- **Reduced motion** — respect `prefers-reduced-motion` for animated chart entrances.

Pair with `manfred-design-systems:a11y-design` for the design-stage annotation pass.

## Responsive

- **Simplify at small sizes** — fewer data points (latest 7 vs latest 90 days), larger labels, fewer y-axis ticks.
- **Alternative views** — a table on mobile when the chart genuinely doesn't work below 320px.
- **Touch-friendly tooltips** — bigger hit areas; no hover-only interactions.
- **Sparklines for inline mobile** — when the trend matters but axes don't.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Pie charts with 8 categories are fine" | They aren't readable. Use stacked bar. |
| "Truncated y-axis makes the change more visible" | And visually dishonest. Use a callout / annotation instead. |
| "3D bars look more polished" | They distort length comparison. Drop the 3D. |
| "Legend in the corner is fine" | Legend is a lookup tax. Direct-label the lines if you can. |
| "Red-green for good/bad is universal" | ~8% of men are red-green colourblind. Use colour + shape, or different hues. |
| "Animation makes it feel premium" | Motion that doesn't communicate the data is decoration. Keep it minimal; respect reduced-motion. |
| "I'll pick the colours later" | Late colour decisions become hex literals. Pick from tokens at design stage. |

## Red flags — STOP

- Picking a chart because it's available, not because it answers the question
- Truncating bar-chart y-axis below zero
- Using 3D / drop shadows / gradient fills on bars or lines
- Relying on colour alone to distinguish categories
- Charts without accessible names or text alternatives
- More than 7 categories on a categorical scale
- Pie chart with more than 4 slices
- Tooltip-only data points (no keyboard access)
- Charts that don't work below 320px without an alternative view

## Manfred lens

Data viz touches **usability** directly — bad charts mislead users and lead to wrong decisions. It also touches **principle 14 (design with data)** — the team using charts to evaluate their own work needs charts that don't lie.

Critical & ethical (principle 6): charts can manipulate. Truncated axes, cherry-picked time windows, scary colours on benign data, false precision (decimal places that don't matter). Refuse manipulative defaults; make the data legible.

## Cross-references

- `~/.claude/shared/DESIGN.md` — token surface for chart colours
- `~/.claude/shared/design-principles.md` — principles 5, 14, 15
- `manfred-ui-design:color-system` — palette decisions; data viz uses subsets of the token surface
- `manfred-design-systems:design-token` — for adding data-viz-specific tokens (categorical, sequential, diverging)
- `manfred-design-systems:a11y-design` — contrast + a11y annotation pass
- `manfred-design-systems:a11y-qa` — runtime gate

## Tools used

- `Read` — `~/.claude/shared/DESIGN.md`, existing chart designs
- `manfred-design-systems:design-token` — for chart-token additions
- `manfred-design-systems:a11y-design` — for chart accessibility
- `manfred-ui-design:color-system` — for palette / categorical colour decisions

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
