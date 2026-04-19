# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] — 2026-04-19

### Added
- `shared/DESIGN.md` — full Manfred design system specification (colors, typography, components, dark mode, accessibility), sourced from `github.com/jens-wedin/manfred-design_system`
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
