# Manfred Shared Knowledge

Shared Claude Code skills, slash commands, plugins, and CLAUDE.md templates for Manfred.

## What this is

A public repo that packages Manfred's shared Claude Code assets so every team member gets the same setup with two commands.

## Install

**1. Register the plugin marketplace (inside Claude Code):**

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
```

**2. Install only the plugins you need:**

```
/plugin install manfred-discovery@manfred         # Cagan + Torres product discovery
/plugin install manfred-design-research@manfred   # interviews, archetypes, journeys, empathy, JTBD, usability tests
/plugin install manfred-design-systems@manfred    # tokens, components, theming, a11y (design/dev/QA)
/plugin install manfred-ux-strategy@manfred       # principles, vision, competitive, briefs, opportunities, stakeholders, metrics
/plugin install manfred-design-ops@manfred        # handoff specs, critiques, QA, review gates, sprints, team workflow, version control
/plugin install manfred-toolkit@manfred           # ux-writing, case studies, design rationale, presentations, DS adoption + audits, LinkedIn (Swedish)
/plugin install manfred-ui-design@manfred         # layout, colour, type, responsive, dark mode, data viz, illustration, visual hierarchy
/plugin install manfred-a11y@manfred              # DEPRECATED — moved into manfred-design-systems; removed in v1.0.0
/plugin install manfred-writing@manfred           # LinkedIn (Swedish) (transcript-anonymizer deprecated; use manfred-design-research)
/plugin install manfred-product@manfred           # Scandic product brief / PRD (transitional — folds into manfred-discovery in v1.0.0)
/plugin install manfred-dev@manfred               # Vite/React: pre-merge QA, deploy, release
/plugin install manfred-knowledge@manfred         # Obsidian vault linting, batch Markdown conversion
```

**3. (Optional) Install the home-level CLAUDE.md and shared design references:**

```bash
curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-shared-knowledge/main/install.sh | bash
```

This installs the home `~/.claude/CLAUDE.md` and `~/.claude/shared/` reference docs only — skills are now plugin-distributed.

Re-run with `--force` to overwrite existing files (backups are created automatically).

## Plugins

| Plugin | Skills + commands | Use it if |
|--------|-------------------|-----------|
| `manfred-discovery` | 7 skills (`cagan-risks`, `opportunity-solution-tree`, `assumption-test`, `customer-touchpoint-plan`, `product-brief`, `discovery-readout`, `discovery-rituals`) + 3 commands (`/kickoff`, `/weekly`, `/risk-check`) | You shape product opportunities, run continuous discovery, or want to make customer-driven decisions over feature lists |
| `manfred-design-research` | 11 skills (`interview-script`, `summarize-interview`, `affinity-diagram`, `card-sort-analysis`, `diary-study-plan`, `empathy-map`, `jobs-to-be-done`, `usability-test-plan`, `journey-map`, `user-archetype`, `transcript-anonymizer`) + 4 commands (`/discover`, `/interview`, `/synthesize`, `/test-plan`) | You run user research — interviews, synthesis, archetypes, journeys, usability tests. Continuous over project-shaped, Trio-attended, story-based |
| `manfred-design-systems` | 10 skills (`design-token`, `component-spec`, `documentation-template`, `icon-system`, `naming-convention`, `pattern-library`, `theming-system`, `a11y-design`, `a11y-dev`, `a11y-qa`) + 3 commands (`/audit-system`, `/create-component`, `/tokenize`) | You build on Manfred's design system. Three-layer tokens (primitives → semantic → shadcn contract), shadcn shapes, WCAG 2.2 AA baseline, dark mode day-one. Absorbs the a11y trio from `manfred-a11y`. |
| `manfred-ux-strategy` | 8 skills (`design-principles`, `north-star-vision`, `competitive-analysis`, `design-brief`, `experience-map`, `metrics-definition`, `opportunity-framework`, `stakeholder-alignment`) + 3 commands (`/benchmark`, `/frame-problem`, `/strategize`) | You set strategic direction — principles, vision, briefs, prioritisation. Customer-driven floor, outcomes over outputs, warm + precise voice, critical & ethical (principle 6) non-negotiable. |
| `manfred-design-ops` | 7 skills (`handoff-spec`, `design-critique`, `design-qa-checklist`, `design-review-process`, `design-sprint-plan`, `team-workflow`, `version-control-strategy`) + 3 commands (`/handoff`, `/plan-sprint`, `/setup-workflow`) | You're running design ops — handoffs, reviews, sprints, team rituals, version control. Trio attendance, design system as source of truth, Linear-anchored handoffs, async-first. |
| `manfred-toolkit` | 9 skills (`ux-writing`, `case-study`, `design-rationale`, `design-system-adoption`, `design-token-audit`, `presentation-deck`, `linkedin-reflect`, `linkedin-show-and-tell`, `linkedin-teach`) + 3 commands (`/build-presentation`, `/write-case-study`, `/write-rationale`) | You're producing content — UX copy, case studies, rationales, presentations, DS adoption + audits, LinkedIn (Swedish). Voice rules from `manfred-brand.md` enforced. Absorbs the linkedin trio from `manfred-writing`. |
| `manfred-ui-design` | 9 skills (`color-system`, `dark-mode-design`, `data-visualization`, `illustration-style`, `layout-grid`, `responsive-design`, `spacing-system`, `typography-scale`, `visual-hierarchy`) + 4 commands (`/color-palette`, `/design-screen`, `/responsive-audit`, `/type-system`) | You're designing UI — layout, colour, type, responsive, dark mode. Hooks into `shared/DESIGN.md` tokens (no hex generation). Mobile first; flat first, depth is earned; Host Grotesk; dark day-one. |
| `manfred-a11y` | `a11y-design`, `a11y-dev`, `a11y-qa` (**DEPRECATED** — skills moved to `manfred-design-systems` in v0.15; this plugin is removed in v1.0.0) | Transitional — install `manfred-design-systems` instead |
| `manfred-writing` | `meeting-summary` (active); `linkedin-reflect`/`linkedin-show-and-tell`/`linkedin-teach` (**deprecated** — moved to `manfred-toolkit:linkedin-*`); `transcript-anonymizer` (**deprecated** — moved to `manfred-design-research:transcript-anonymizer`) | Transitional — install `manfred-toolkit` for LinkedIn, `manfred-design-research` for transcript-anonymizer; only `meeting-summary` rooted here until v1.0.0 |
| `manfred-product` | `brief-prd` (transitional) | You write Scandic-specific product briefs. **Note:** new product-brief work should use `manfred-discovery:product-brief`. This plugin is removed in v1.0.0. |
| `manfred-dev` | `deploy`, `release`, `test-my-code` | You ship Vite/React features and want pre-merge QA gates plus production-grade release flow |
| `manfred-knowledge` | `markitdown-convert`, `clippings-linter` | You manage an Obsidian vault or batch-convert documents to Markdown |

Each plugin's own `README.md` lists the trigger phrases for its skills.

## Roadmap

`v1.0.0` will reorganise the marketplace into a clean design-discipline taxonomy modelled on `Owl-Listener/designer-skills` (MIT) but Manfred-flavoured. The shape:

| Plugin | What it covers |
|--------|----------------|
| `manfred-discovery` | Cagan + Torres product discovery (this v0.13 pilot) |
| `manfred-design-research` | User research: personas, journeys, interviews, usability tests, card sorting (will absorb `meeting-summary`, `transcript-anonymizer`) |
| `manfred-design-systems` | Tokens, components, theming, accessibility (will absorb `a11y-design`, `a11y-dev`, `a11y-qa`) |
| `manfred-ux-strategy` | Competitive analysis, design principles, north-star, alignment |
| `manfred-ui-design` | Layout, color, typography, responsive — built on `~/.claude/shared/DESIGN.md` |
| `manfred-interaction-design` | Animations, state machines, gestures, error handling |
| `manfred-prototyping-testing` | Usability tests, A/B, heuristics |
| `manfred-design-ops` | Handoff specs, sprint planning, critique |
| `manfred-toolkit` | Case studies, presentations, UX writing (will absorb `linkedin-*`) |
| `manfred-dev` | Engineering workflow (kept) |
| `manfred-knowledge` | Knowledge utilities (kept) |

The `Owl-Listener/designer-skills` plugins (`design-ops`, `design-research`, etc.) are useful in the meantime — Manfred's mirrors are intentionally opinionated reframings, not generic equivalents. Plan to uninstall those after the Manfred mirrors ship.

## What `install.sh` installs

| Source | Destination | Purpose |
|--------|-------------|---------|
| `shared/home-claude.md` | `~/.claude/CLAUDE.md` | Home-level conventions loaded into every session |
| `shared/manfred-brand.md` | `~/.claude/shared/manfred-brand.md` | Brand guidelines |
| `shared/DESIGN.md` | `~/.claude/shared/DESIGN.md` | Design system spec |
| `shared/design-principles.md` | `~/.claude/shared/design-principles.md` | Design principles |

Skills no longer ship via `install.sh`. They live in plugins — see above.

## Migrating from the old skill installer

If you previously ran `install.sh` to copy skills into `~/.claude/skills/`, those local copies will conflict with plugin-distributed versions. Re-run `install.sh` once — it detects legacy skill directories and prints the cleanup commands. Then:

```bash
rm -rf ~/.claude/skills/<skill-name>   # for each affected skill
/plugin install manfred-<plugin>@manfred
```

## Project-level setup

For each project that should follow Manfred conventions, drop the template `CLAUDE.md` into the project root:

```bash
curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-shared-knowledge/main/CLAUDE.md -o ./CLAUDE.md
```

Extend it with project-specific rules below the `---` marker.

## Contributing

Open a PR for any of:

- **A new skill in an existing plugin** — add a folder under `plugins/<plugin-name>/skills/<skill-name>/` with a `SKILL.md`. Bump the plugin's `version` in `plugins/<plugin-name>/.claude-plugin/plugin.json` and the corresponding entry in `.claude-plugin/marketplace.json`.
- **A new plugin** — scaffold under `plugins/<new-plugin>/` with `.claude-plugin/plugin.json`, `skills/`, and a `README.md`. Register it in `.claude-plugin/marketplace.json` under `plugins`.
- **Shared references** — add under `shared/`; add an `install_file` call to `install.sh`.
- **Project CLAUDE.md template** — edit `./CLAUDE.md` at the repo root.

Use conventional commits. Update `CHANGELOG.md` in the same PR.

## Uninstall

```bash
curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-shared-knowledge/main/uninstall.sh | bash -s -- --yes
```

Then inside Claude Code:

```
/plugin marketplace remove manfred
```

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).
