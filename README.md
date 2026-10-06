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
/plugin install manfred-discovery@manfred              # Cagan + Torres product discovery
/plugin install manfred-design-research@manfred        # interviews, archetypes, journeys, JTBD, usability tests, transcript anonymisation
/plugin install manfred-ux-strategy@manfred            # principles, vision, competitive, briefs, opportunities, stakeholders, metrics
/plugin install manfred-design-systems@manfred         # tokens, components, theming, a11y (design / dev / QA)
/plugin install manfred-ui-design@manfred              # layout, colour, type, responsive, dark mode, data viz, illustration, visual hierarchy
/plugin install manfred-interaction-design@manfred     # animation, feedback, gestures, loading, micro-interactions, state machines, error-handling UX
/plugin install manfred-prototyping-testing@manfred    # prototype strategy, click + A/B tests, heuristic eval, a11y test plan, test scenarios, user flows, wireframes
/plugin install manfred-design-ops@manfred             # handoff specs, critiques, QA, review gates, sprints, team workflow, version control
/plugin install manfred-toolkit@manfred                # ux-writing, case studies, design rationale, presentations, DS adoption + audits, meeting summaries, LinkedIn (Swedish)
/plugin install manfred-dev@manfred                    # Vite/React: pre-merge QA, deploy, release
/plugin install manfred-knowledge@manfred              # Obsidian vault linting, batch Markdown conversion, marketplace static QA (lint-marketplace)
```

**3. (Optional) Install the home-level CLAUDE.md and shared design references:**

```bash
curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-shared-knowledge/main/install.sh | bash
```

This installs the home `~/.claude/CLAUDE.md` and `~/.claude/shared/` reference docs only — skills are plugin-distributed.

Re-run with `--force` to overwrite existing files (backups are created automatically).

## Plugins

11 plugins covering the full design discipline + supporting engineering / knowledge utilities. Each plugin's own `README.md` lists the trigger phrases for its skills.

| Plugin | Skills + commands | Use it if |
|--------|-------------------|-----------|
| `manfred-discovery` | 7 skills (`cagan-risks`, `opportunity-solution-tree`, `assumption-test`, `customer-touchpoint-plan`, `product-brief`, `discovery-readout`, `discovery-rituals`) + 3 commands (`/kickoff`, `/weekly`, `/risk-check`) | You shape product opportunities, run continuous discovery, or want to make customer-driven decisions over feature lists |
| `manfred-design-research` | 11 skills (`interview-script`, `summarize-interview`, `affinity-diagram`, `card-sort-analysis`, `diary-study-plan`, `empathy-map`, `jobs-to-be-done`, `usability-test-plan`, `journey-map`, `user-archetype`, `transcript-anonymizer`) + 4 commands (`/discover`, `/interview`, `/synthesize`, `/test-plan`) | You run user research — interviews, synthesis, archetypes, journeys, usability tests, transcript anonymisation. Continuous over project-shaped, Trio-attended, story-based |
| `manfred-ux-strategy` | 8 skills (`design-principles`, `north-star-vision`, `competitive-analysis`, `design-brief`, `experience-map`, `metrics-definition`, `opportunity-framework`, `stakeholder-alignment`) + 3 commands (`/benchmark`, `/frame-problem`, `/strategize`) | You set strategic direction — principles, vision, briefs, prioritisation. Customer-driven floor, outcomes over outputs, warm + precise voice, critical & ethical (principle 6) non-negotiable |
| `manfred-design-systems` | 10 skills (`design-token`, `component-spec`, `documentation-template`, `icon-system`, `naming-convention`, `pattern-library`, `theming-system`, `a11y-design`, `a11y-dev`, `a11y-qa`) + 3 commands (`/audit-system`, `/create-component`, `/tokenize`) | You build on Manfred's design system. Three-layer tokens (primitives → semantic → shadcn contract), shadcn shapes, WCAG 2.2 AA baseline, dark mode day-one |
| `manfred-ui-design` | 9 skills (`color-system`, `dark-mode-design`, `data-visualization`, `illustration-style`, `layout-grid`, `responsive-design`, `spacing-system`, `typography-scale`, `visual-hierarchy`) + 4 commands (`/color-palette`, `/design-screen`, `/responsive-audit`, `/type-system`) | You're designing UI — layout, colour, type, responsive, dark mode. Hooks into `shared/DESIGN.md` tokens (no hex generation). Mobile first; flat first, depth is earned; Host Grotesk; dark day-one |
| `manfred-interaction-design` | 7 skills (`animation-principles`, `error-handling-ux`, `feedback-patterns`, `gesture-patterns`, `loading-states`, `micro-interaction-spec`, `state-machine`) + 3 commands (`/design-interaction`, `/error-flow`, `/map-states`) | You're designing the moment-to-moment behaviour — motion, feedback, gestures, loading, errors, state. `error-handling-ux` refuses generic copy and routes to `manfred-toolkit:ux-writing`; reduced-motion fallback non-negotiable; tokens for durations |
| `manfred-prototyping-testing` | 8 skills (`a-b-test-design`, `accessibility-test-plan`, `click-test-plan`, `heuristic-evaluation`, `prototype-strategy`, `test-scenario`, `user-flow-diagram`, `wireframe-spec`) + 4 commands (`/evaluate`, `/experiment`, `/prototype-plan`, `/test-plan`) | You're choosing how to test or prototype. `prototype-strategy` refuses fidelity-first questions and routes to assumption + risk + audience first; LEARN ≠ SHOW; cheapest test wins; heuristic eval uses Nielsen + Manfred 15; a11y testing covers four layers including real users with disabilities |
| `manfred-design-ops` | 7 skills (`handoff-spec`, `design-critique`, `design-qa-checklist`, `design-review-process`, `design-sprint-plan`, `team-workflow`, `version-control-strategy`) + 3 commands (`/handoff`, `/plan-sprint`, `/setup-workflow`) | You're running design ops — handoffs, reviews, sprints, team rituals, version control. Trio attendance, design system as source of truth, Linear-anchored handoffs, async-first |
| `manfred-toolkit` | 10 skills (`ux-writing`, `case-study`, `design-rationale`, `design-system-adoption`, `design-token-audit`, `meeting-summary`, `presentation-deck`, `linkedin-reflect`, `linkedin-show-and-tell`, `linkedin-teach`) + 3 commands (`/build-presentation`, `/write-case-study`, `/write-rationale`) | You're producing content — UX copy, case studies, rationales, presentations, DS adoption + audits, meeting summaries (bilingual SV/EN), LinkedIn (Swedish). Voice rules from `manfred-brand.md` enforced |
| `manfred-dev` | 5 skills (`test-my-code`, `deploy`, `release`, `bootstrap-manfred-project`, `install-manfred-claude-skills`) | You ship Vite/React features and want pre-merge QA gates plus production-grade release flow, OR you want to scaffold a new Manfred project / add Manfred conventions to an existing repo. Calls `manfred-design-systems:a11y-qa` for the runtime accessibility scan |
| `manfred-knowledge` | 3 skills (`markitdown-convert`, `clippings-linter`, `lint-marketplace`) | You manage an Obsidian vault, batch-convert documents to Markdown, or want a re-runnable static QA pass over the marketplace plugins themselves (10 deterministic checks; HARD vs SOFT exit) |

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

Use conventional commits. Update `CHANGELOG.md` in the same PR. New skills: follow `docs/manfred-skill-template.md` and run the TDD-for-skills loop (RED → GREEN → REFACTOR per `superpowers:writing-skills`).

## Uninstall

Inside Claude Code:

```
/plugin marketplace remove manfred
```

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).
