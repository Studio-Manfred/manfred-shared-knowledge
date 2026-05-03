# manfred-ux-strategy

Manfred-flavoured UX strategy work: design principles (rooted in `~/.claude/shared/design-principles.md`), north-star vision, competitive analysis, design briefs, experience maps, opportunity frameworks, stakeholder alignment, and metrics.

Customer-driven first. Outcomes over outputs. Warm + precise voice, not McKinsey. Critical & ethical (Manfred design principle 6) is non-negotiable.

## Skills

| Skill | When it triggers |
|-------|-----------------|
| `design-principles` | "give me design principles", "principles for the wall", "design principles for this project", "team manifesto" — **foundational TDD'd skill**: refuses cold-start posters; requires reading Manfred's canonical 15 first; offers (a) adapt, (b) workshop kit, (c) starter set with workshop date |
| `north-star-vision` | "north star", "product vision", "5-year vision", "where are we going", "design vision" |
| `competitive-analysis` | "competitive analysis", "competitor audit", "benchmark", "what are X and Y doing", "market gaps" |
| `design-brief` | "design brief", "project brief", "kick off this project", "scope this engagement" |
| `experience-map` | "experience map", "ecosystem map", "service blueprint", "touchpoint map", "omnichannel audit" |
| `metrics-definition` | "what should we measure", "design metrics", "KPIs", "north-star metric", "HEART", "OKRs for design" |
| `opportunity-framework` | "prioritise these ideas", "RICE scoring", "impact-effort matrix", "rank these opportunities", "Kano model" |
| `stakeholder-alignment` | "stakeholder map", "RACI", "decision framework", "who decides what", "feedback protocol" |

## Commands

| Command | What it does |
|---------|--------------|
| `/manfred-ux-strategy:benchmark` | Benchmark a product against competitors. Chains competitive-analysis + experience-map (optional) + opportunity-framework. Ends in defensible "where we should differ". |
| `/manfred-ux-strategy:frame-problem` | Frame a design problem end-to-end. Chains design-brief + experience-map + stakeholder-alignment + metrics-definition. Ends in a signed brief. |
| `/manfred-ux-strategy:strategize` | Develop a UX strategy end-to-end. Chains design-principles + north-star-vision + competitive-analysis + opportunity-framework + metrics-definition + stakeholder-alignment. Ends in a defensible direction. |

## Manfred opinions baked in

- **Customer-driven floor** (design principle 1) — every strategy output cites user evidence; "we believe…" gets flagged as assumption
- **Outcomes over outputs** — success criteria are measurable user / business changes, not feature lists
- **Warm + precise voice** — no marketing verbs (transform, empower, leverage, supercharge); no McKinsey-speak
- **Critical & ethical** (design principle 6) — every strategy includes "what does this design do in the world?" and an honest answer
- **Trade-offs stated** — visions name what they give up; principles name their trade-off partner; opportunities have stated confidence
- **Triangulation over single-framework certainty** — opportunity-framework runs impact-effort + RICE; disagreements get investigated

## Cross-plugin handoffs

- **Pairs with `manfred-discovery:product-brief`** — Section 02 (Strategic Alignment) cites the strategy outputs
- **Feeds `manfred-discovery:opportunity-solution-tree`** — opportunities and outcomes ladder up
- **Inputs from `manfred-design-research`** — research grounds competitive analysis, experience maps, archetype-driven scenarios
- **Pairs with `manfred-design-systems:design-token`** — visual strategy outputs reference Manfred's three-layer token architecture

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-ux-strategy@manfred
```
