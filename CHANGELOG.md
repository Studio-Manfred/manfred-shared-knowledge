# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.3] — 2026-04-29

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
