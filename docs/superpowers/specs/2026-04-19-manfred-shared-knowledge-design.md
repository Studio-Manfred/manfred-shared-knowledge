# Manfred Shared Knowledge — Design Spec

**Date:** 2026-04-19
**Author:** Jens Wedin
**Status:** Approved via brainstorming session
**Target repo:** `github.com/jens-wedin/manfred-shared-knowledge` (public)

## Purpose

A public GitHub repository that packages Manfred's shared Claude Code assets — skills, slash commands, plugins, and CLAUDE.md templates — and makes them trivial to install for anyone in the Manfred orbit.

The v0.1.0 goal is a working, empty scaffold. Content gets added over time through normal PRs; the scaffold just has to stand on its own today.

## Non-goals

- No content porting from Jens's personal `~/.claude/skills/` in v0.1.0
- No mirror of the Scandic skills — Manfred authors its own over time
- No private-repo token flow — repo is public
- No automated plugin publishing pipeline — plugins get added manually to `marketplace.json`

## Repository layout

```
manfred-shared-knowledge/
├── .claude-plugin/
│   └── marketplace.json           # Manfred plugin marketplace manifest
├── plugins/                       # Individual plugin sources (referenced by marketplace.json)
│   └── .gitkeep
├── skills/                        # Loose skills (copied directly by install.sh)
│   └── .gitkeep
├── commands/                      # Loose slash commands / prompt templates
│   └── .gitkeep
├── shared/                        # Reference docs copied to ~/.claude/shared/
│   ├── home-claude.md             # Becomes ~/.claude/CLAUDE.md after install
│   ├── manfred-brand.md           # Placeholder
│   └── roles/
│       └── .gitkeep
├── CLAUDE.md                      # Template users can copy into their own projects
├── README.md
├── CHANGELOG.md
├── install.sh
└── uninstall.sh
```

Every content folder has a `.gitkeep` so the tree is visible but empty. Content folders are ready to receive PRs without further scaffolding.

## Install model

Two-step flow:

1. **Loose files via curl one-liner:**
   ```bash
   curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/install.sh | bash
   ```
   Copies home-level `CLAUDE.md` and `shared/` reference docs into `~/.claude/`.

2. **Plugin marketplace registration (inside Claude Code):**
   ```
   /plugin marketplace add jens-wedin/manfred-shared-knowledge
   ```
   One-time. Enables `/plugin install <name>@manfred` for any plugin listed in `marketplace.json`.

### `install.sh` behavior

Adapted from the Scandic version. Same semantics:

- `REPO_RAW="https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main"`
- `CLAUDE_DIR="$HOME/.claude"` target
- `--force` flag: overwrite existing files after timestamped backup (`.backup.YYYYMMDDHHMMSS`)
- Default behavior: skip files that already exist, report as skipped
- Counters: `INSTALLED` and `SKIPPED` printed in a summary footer
- Banner: Manfred-branded
- Post-install message: prints the `/plugin marketplace add` command and a pointer to the project-level `CLAUDE.md` template

In v0.1.0 it installs exactly two files:

- `shared/home-claude.md` → `~/.claude/CLAUDE.md`
- `shared/manfred-brand.md` → `~/.claude/shared/manfred-brand.md`

The repo-root `CLAUDE.md` is **not** installed by `install.sh` — it is a manual-copy template for users to drop into their own projects. The installer's footer prints a separate curl command for fetching it.

As `skills/`, `commands/`, or `shared/` grow, new `install_file` calls get added to `install.sh` via PR.

### `uninstall.sh` behavior

Mirrors the install list: removes the loose files `install.sh` placed under `~/.claude/`. Prints a reminder that the plugin marketplace must be removed separately with `/plugin marketplace remove manfred`.

## Plugin marketplace manifest

`.claude-plugin/marketplace.json`:

```json
{
  "name": "manfred",
  "owner": {
    "name": "Jens Wedin (Manfred)",
    "email": "jens@studiomanfred.com",
    "url": "https://studiomanfred.com"
  },
  "metadata": {
    "description": "Shared Claude Code skills, commands, and plugins for Manfred",
    "version": "0.1.0"
  },
  "plugins": []
}
```

`plugins` is an empty array in v0.1.0. First real plugin added later will include `name`, `source`, `description`, and a path under `plugins/`.

## Documentation

### `README.md`

Sections:
- **What this is** — Manfred's shared Claude Code knowledge base
- **Install** — the two steps (curl + `/plugin marketplace add`)
- **What gets installed** — `~/.claude/CLAUDE.md`, `~/.claude/shared/`, plus plugins on demand
- **Project-level setup** — how to fetch the repo-root `CLAUDE.md` template into a project (`curl ... -o ./CLAUDE.md`)
- **Contributing** — how to add a skill (`skills/`), a command (`commands/`), or a plugin (`plugins/` + register in `marketplace.json`)
- **Uninstall** — run `uninstall.sh`, then `/plugin marketplace remove manfred`
- **Changelog** — link to `CHANGELOG.md`

### `CHANGELOG.md`

Starts at:

```
## [0.1.0] — 2026-04-19
### Added
- Initial scaffold: marketplace.json, install.sh, uninstall.sh
- Placeholder home-level CLAUDE.md and shared/ reference folder
- Empty skills/, commands/, plugins/ directories ready for content
```

Conventional-commits style from v0.1.0 onward, consistent with the parent `Sandbox/Code/CLAUDE.md` convention.

### `CLAUDE.md` (project template)

A minimal stub users copy into their own projects. Says the project follows Manfred conventions and points at `~/.claude/shared/`. Placeholder content until Manfred has real conventions to codify.

### `shared/home-claude.md` (installed as `~/.claude/CLAUDE.md`)

Minimal — a few lines noting Manfred-shared-knowledge is installed and how to register the marketplace.

### `shared/manfred-brand.md`

Placeholder — single heading and a `TODO: add Manfred brand guidelines` line. Exists so `install.sh` has a second file to copy and so the `shared/` folder is demonstrably populated.

## Success criteria

- `install.sh` runs cleanly on a fresh machine: no errors, files land where the script says, re-running is idempotent (skip by default, `--force` backs up)
- `/plugin marketplace add jens-wedin/manfred-shared-knowledge` succeeds in Claude Code (marketplace manifest valid)
- `uninstall.sh` removes everything `install.sh` created, leaving no orphans
- `README.md` is clear enough that a teammate can install both halves without asking for help

## Open questions

None blocking v0.1.0.

Future decisions (out of scope for this spec):
- Which skills migrate from `~/.claude/skills/` and in what order
- Whether `plugins/` entries are hand-authored or scaffolded from a template
- Release/versioning cadence once content lands
