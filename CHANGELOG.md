# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.13.0] — 2026-04-30

### Added
- **`manfred-discovery` plugin** — Manfred-flavoured product discovery synthesising Marty Cagan's four product risks and Teresa Torres's continuous discovery + opportunity-solution trees. 7 skills + 3 commands:
  - Skills: `cagan-risks`, `opportunity-solution-tree`, `assumption-test`, `customer-touchpoint-plan`, `product-brief`, `discovery-readout`, `discovery-rituals`
  - Commands: `/manfred-discovery:kickoff`, `/manfred-discovery:weekly`, `/manfred-discovery:risk-check`
  - `discovery-readout` integrates with Linear via `mcp__linear-server__save_comment` (pattern from `manfred-dev:test-my-code`)
  - `cagan-risks` built via the full TDD-for-skills loop in `superpowers:writing-skills` (RED baseline → GREEN → REFACTOR with three rationalization patches)
- **`docs/manfred-skill-template.md`** — codified Manfred SKILL.md conventions: voice rules, Cagan/Torres lens guidance, Manfred-outputs checklist, TDD-for-skills pointer, attribution rules. Reference for all subsequent Manfred plugins.

### Changed
- `.claude-plugin/marketplace.json` metadata bumped to `v0.3.0`. `manfred-discovery` registered as the 6th plugin.
- `README.md` — added `manfred-discovery` to the plugin table, documented the v1.0.0 design-discipline reorg roadmap (mirrors of `Owl-Listener/designer-skills` plugins, with absorption of existing utility plugins).

### Transitional
- `manfred-product:brief-prd` (Scandic-specific) and `manfred-discovery:product-brief` (generalised, with explicit Cagan/Torres hooks) coexist in v0.13.x. `brief-prd` carries a deprecation note. The full reorg lands in v1.0.0 — `manfred-product` removed, `brief-prd` content fully migrated.

### Roadmap
- v1.0.0 will reorg into 11 themed plugins replacing both the existing 5 utility plugins and the third-party `Owl-Listener/designer-skills` install. See README "Roadmap" section.

### Attribution
- Inspiration for the plugin/command structure (and several upcoming mirror plugins) draws from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) — MIT licensed. The `manfred-discovery` plugin itself is Manfred-original; mirror plugins (when they ship) will be structurally adapted with Manfred voice and opinions.

## [0.12.0] — 2026-04-30

### Changed
- **Skills now ship as plugins.** Migrated 14 skills from the loose `skills/<name>/` layout into 5 themed plugins under `plugins/<plugin-name>/`. The marketplace at `.claude-plugin/marketplace.json` now lists `manfred-a11y`, `manfred-writing`, `manfred-product`, `manfred-dev`, and `manfred-knowledge` (each at `v0.1.0`). Marketplace metadata bumped to `v0.2.0`.
- `install.sh` no longer copies skills. It now installs only the home `~/.claude/CLAUDE.md` and `~/.claude/shared/` reference docs, then prints the `/plugin install` commands. A new `check_legacy_skills` step warns users with leftover copies in `~/.claude/skills/` and prints the cleanup commands.
- `README.md` rewritten around the plugin-first install flow with a per-plugin table and a migration section for users coming from `install.sh`-installed skills.
- Top-level `skills/` directory removed — all skills now live under `plugins/<plugin>/skills/`.

### Added
- `plugins/manfred-dev/skills/test-my-code/` — opinionated pre-merge QA gate for Vite/React features (typecheck → lint → vitest → build → Playwright → axe). Saves a report file and posts the summary to the linked Linear ticket. Built today via the full TDD-for-skills loop. Calls into `manfred-a11y`'s `a11y-qa` for the runtime accessibility scan.
- `plugins/manfred-knowledge/skills/clippings-linter/` — Obsidian vault hygiene (broken notes, missing tags, duplicates, orphans). Includes Python lint scripts.

### Migration
Existing users with `~/.claude/skills/<name>/` from previous `install.sh` runs: re-run `install.sh` once — it detects the legacy directories and prints the cleanup commands. Then `rm -rf ~/.claude/skills/<name>` for each affected skill and `/plugin install manfred-<plugin>@manfred` to pick up the plugin-distributed version.

## [0.11.0] — 2026-04-29

### Added
- `skills/release` — full production release skill that runs quality gates (lint, types+build, unit tests, a11y audit), waits for the Vercel deploy to reach `READY` after pushing, then comments + transitions Linear tickets and updates Linear Project descriptions. Sibling to the lightweight `deploy` skill — use `release` for projects with Vercel-GitHub deploys and `STU-###` tickets, `deploy` for everything else. Includes `references/linear-actions.md` (verified Linear MCP call patterns including the Linear Project vs project-Milestone distinction) and `references/vercel-wait.md` (deployment polling pattern). Built via the full TDD-for-skills loop in `superpowers:writing-skills` — three baseline pressure scenarios (just-ship-it, Linear-stale, typo-fix) drove the rationalization table; three REFACTOR scenarios verified compliance and surfaced two cosmetic-fast-path ambiguities that were patched.
- `MEMORY.md` — repo-level self-learning log with a "Standing lessons" section (TDD-for-skills, Linear MCP gotchas, Vercel-GitHub deploy mechanics, repo conventions) and dated session entries. Read on session start, append on session close, promote recurring lessons.

### Changed
- `README.md` skills table now lists 12 skills; `deploy` row clarified as "lightweight"; new `release` row added.
- `install.sh` and `uninstall.sh` `SKILLS=( … )` arrays include `release`.

## [0.3.4] — 2026-04-29

### Changed
- Repository moved from `jens-wedin/manfred-shared-knowledge` to `Studio-Manfred/manfred-shared-knowledge`. All install/uninstall URLs, marketplace registration command, and cross-references in `README.md`, `CLAUDE.md`, `install.sh`, `uninstall.sh`, `shared/home-claude.md`, `shared/manfred-brand.md`, and `shared/DESIGN.md` updated to the new org.
- `skills/deploy/SKILL.md` — git tag step (Step 7) is now part of the standard flow rather than optional, since downstream releases consistently rely on tags.

## [0.3.2] — 2026-04-19

### Changed
- `shared/manfred-brand.md` Brand Voice section rewritten with prescriptive tone-of-voice guidance: concrete rhythms lifted from `studiomanfred.com` (Q&A beats, shrug ellipsis, serious-serious-wink triplets, provocation-where-a-pitch-would-go), a Manfred Vocabulary list (Manfred Magic, the Mmmms, peeps, 〰️, Ping us), a named Anti-Patterns list (no marketing verbs, no corporate adjectives, no "we're passionate about…", no forced levity, no hedging), and a four-question Quick Test for new copy. The previous version described the voice; this one shows it.

## [0.3.1] — 2026-04-19

### Changed
- `shared/manfred-brand.md` rewritten after auditing `studiomanfred.com` — real mission ("Building Better Product Companies" / "make the product world more customer driven"), actual services (Leadership · Customer Research · Product/UX/Service Design · Training), the team ("the Mmmms": Jens Wedin, Selma Hallqvist, Axel Nathorst-Böös, Moa Bogren), named clients (Boka Direkt · Mentimeter · Fishbrain · Svea Bank · Trygg-Hansa), and the playful/craft-serious site voice ("Manfred Magic", "winging it with a whiteboard", "ping us"). Colors and typography retained under a new "Visual Language" section.
- `shared/design-principles.md` expanded from 12 to 15 principles: added Customer-Driven, Research Isn't a Phase, Craft Seriously (Yourself Not So Much), Critical & Ethical Design — reflecting Manfred's actual practice (training courses include Critical Design, Product Discovery, Customer Journey Mapping). The existing design-system principles (tokens, dark mode, shadcn shapes, accessibility) retained.
- `shared/DESIGN.md` opening reframed to make clear this describes the Manfred design system (one artifact the studio makes), not the studio itself — pointers to `manfred-brand.md` and `design-principles.md` added.

## [0.3.0] — 2026-04-19

### Added
- `shared/DESIGN.md` — full Manfred design system specification (colors, typography, components, dark mode, accessibility), sourced from `github.com/Studio-Manfred/manfred-design_system`
- `shared/design-principles.md` — 12-principle decision framework for Manfred work
- `install.sh` now installs DESIGN.md and design-principles.md alongside manfred-brand.md
- `uninstall.sh` removes DESIGN.md and design-principles.md

### Changed
- `shared/manfred-brand.md` rewritten with real content (brand thesis, values, voice, color palette, typography), replacing the v0.1.0 placeholder
- README "What gets installed" table updated with DESIGN.md and design-principles.md rows

## [0.2.0] — 2026-04-19

### Added
- Bundled 11 Manfred skills under `skills/`: `a11y-design`, `a11y-dev`, `a11y-qa`, `brief-prd`, `deploy`, `linkedin-reflect`, `linkedin-show-and-tell`, `linkedin-teach`, `markitdown-convert`, `meeting-summary`, `transcript-anonymizer`
- `install.sh` now performs a shallow `git clone` to fetch multi-file skills and copies them into `~/.claude/skills/<name>/`
- `install.sh` errors clearly when `git` is not on `PATH`
- `uninstall.sh` removes installed skill directories (honours `--yes` and the TTY guard)
- README documents the 11 bundled skills and the planned plugin migration

### Changed
- README "What gets installed" table now includes the skills row
- `install.sh` honours optional `MANFRED_REPO_GIT` env var for testing against a local checkout

## [0.1.1] — 2026-04-19

### Fixed
- `uninstall.sh` piped via `curl | bash` now errors clearly with a `--yes` hint instead of silently aborting on consumed stdin
- README uninstall command updated to pass `-s -- --yes` so `curl | bash` works end-to-end

### Added
- `*.backup.*` to `.gitignore` (installer backup files)
- Contributing guide entry for `shared/roles/` playbooks

## [0.1.0] — 2026-04-19

### Added
- Initial scaffold: `.claude-plugin/marketplace.json`, `install.sh`, `uninstall.sh`
- Placeholder home-level `CLAUDE.md` installed via `shared/home-claude.md`
- Placeholder `shared/manfred-brand.md`
- Project-level `CLAUDE.md` template at repo root
- Empty `skills/`, `commands/`, `plugins/`, `shared/roles/` directories ready for content
- README with install, contribute, and uninstall instructions
