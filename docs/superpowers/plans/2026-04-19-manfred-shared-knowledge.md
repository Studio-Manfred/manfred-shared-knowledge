# Manfred Shared Knowledge Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scaffold the `manfred-shared-knowledge` repo — a public GitHub repository that packages Manfred's shared Claude Code assets (skills, commands, plugins, CLAUDE.md templates) with a simple two-step install flow.

**Architecture:** Static repo. `.claude-plugin/marketplace.json` at root registers a Claude Code plugin marketplace. `install.sh` does a `curl`-based copy of home-level `CLAUDE.md` and `shared/` reference files into `~/.claude/`. `uninstall.sh` reverses the install. Content directories (`skills/`, `commands/`, `plugins/`) ship empty with `.gitkeep` so PRs can add content without further scaffolding.

**Tech Stack:** bash, JSON, Markdown, git. No build step. No runtime dependencies beyond `curl` on the user machine. Verification uses `bash -n` (syntax check), `shellcheck` (lint), and a manual smoke test against a temp `$HOME`.

**Target repo:** `github.com/jens-wedin/manfred-shared-knowledge` (public)

**Working directory:** `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge`

---

## File Structure

Files this plan creates in the target repo:

- `.gitignore` — macOS/editor noise
- `.claude-plugin/marketplace.json` — plugin marketplace manifest
- `plugins/.gitkeep` — empty placeholder for future plugins
- `skills/.gitkeep` — empty placeholder for loose skills
- `commands/.gitkeep` — empty placeholder for loose slash commands
- `shared/home-claude.md` — installed as `~/.claude/CLAUDE.md`
- `shared/manfred-brand.md` — placeholder reference doc
- `shared/roles/.gitkeep` — empty placeholder for role docs
- `CLAUDE.md` — template for user projects (NOT auto-installed)
- `README.md` — top-level project docs
- `CHANGELOG.md` — Keep-a-Changelog style, starting v0.1.0
- `install.sh` — executable, copies loose files to `~/.claude/`
- `uninstall.sh` — executable, reverses install

Files that already exist (keep as-is):
- `docs/superpowers/specs/2026-04-19-manfred-shared-knowledge-design.md`
- `docs/superpowers/plans/2026-04-19-manfred-shared-knowledge.md` (this file)

---

## Task 1: Initialize git repo

**Files:**
- Create: `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/.gitignore`

- [ ] **Step 1: Initialize git**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git init -b main
```

Expected: `Initialized empty Git repository in .../manfred-shared-knowledge/.git/`

- [ ] **Step 2: Create `.gitignore`**

Write `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/.gitignore` with:

```
# macOS
.DS_Store

# Editor
.vscode/
.idea/
*.swp
*~

# Logs
*.log
```

- [ ] **Step 3: Commit initial state (with existing spec and plan)**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git add .gitignore docs/
git commit -m "chore: init repo with design spec and implementation plan"
```

Expected: one commit on main.

---

## Task 2: Create plugin marketplace manifest

**Files:**
- Create: `.claude-plugin/marketplace.json`

- [ ] **Step 1: Create the marketplace manifest**

Write `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/.claude-plugin/marketplace.json` with exactly:

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

- [ ] **Step 2: Validate JSON**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
python3 -m json.tool .claude-plugin/marketplace.json > /dev/null
```

Expected: no output (command exits 0). Any parse error means the JSON is malformed — fix and retry.

- [ ] **Step 3: Commit**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git add .claude-plugin/marketplace.json
git commit -m "feat: add plugin marketplace manifest (v0.1.0, empty plugins array)"
```

---

## Task 3: Scaffold content directories with .gitkeep

**Files:**
- Create: `plugins/.gitkeep`
- Create: `skills/.gitkeep`
- Create: `commands/.gitkeep`
- Create: `shared/roles/.gitkeep`

- [ ] **Step 1: Create each .gitkeep file**

Write the following empty files:

- `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/plugins/.gitkeep`
- `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/skills/.gitkeep`
- `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/commands/.gitkeep`
- `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/shared/roles/.gitkeep`

Each file has zero bytes of content. Use the Write tool with empty string content for each.

- [ ] **Step 2: Verify directories exist**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
ls -la plugins skills commands shared/roles
```

Expected: each directory lists just `.gitkeep` (plus `.` and `..`).

- [ ] **Step 3: Commit**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git add plugins/.gitkeep skills/.gitkeep commands/.gitkeep shared/roles/.gitkeep
git commit -m "chore: scaffold empty plugins/, skills/, commands/, shared/roles/ directories"
```

---

## Task 4: Create shared reference files

**Files:**
- Create: `shared/home-claude.md`
- Create: `shared/manfred-brand.md`

- [ ] **Step 1: Create `shared/home-claude.md`**

Write `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/shared/home-claude.md` with:

```markdown
# Home-level CLAUDE.md (Manfred)

This file is installed at `~/.claude/CLAUDE.md` by the `manfred-shared-knowledge` installer. Claude Code loads it at the start of every session.

## Shared references

Manfred's shared reference docs live in `~/.claude/shared/`. Consult them when relevant:

- `~/.claude/shared/manfred-brand.md` — brand guidelines
- `~/.claude/shared/roles/` — role-specific playbooks (added over time)

## Plugins

Manfred ships skills, commands, and plugins through the `manfred` plugin marketplace. To register it (one-time, inside Claude Code):

```
/plugin marketplace add jens-wedin/manfred-shared-knowledge
```

Then browse available plugins with `/plugin` and install with `/plugin install <name>@manfred`.

## Updating

Re-run the installer to pull the latest shared files:

```bash
curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/install.sh | bash -s -- --force
```

The `--force` flag overwrites existing files after creating timestamped backups.
```

- [ ] **Step 2: Create `shared/manfred-brand.md`**

Write `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/shared/manfred-brand.md` with:

```markdown
# Manfred Brand Guidelines

> Placeholder — to be filled in.

TODO: add Manfred brand guidelines (voice, tone, color, typography, do's and don'ts) here.
```

- [ ] **Step 3: Commit**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git add shared/home-claude.md shared/manfred-brand.md
git commit -m "feat: add initial shared reference files (home CLAUDE.md + brand placeholder)"
```

---

## Task 5: Create project-level CLAUDE.md template

**Files:**
- Create: `CLAUDE.md`

- [ ] **Step 1: Write the template**

Write `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/CLAUDE.md` with:

```markdown
# CLAUDE.md

> This project follows Manfred conventions. Copy this file into your own projects as a starting point — `curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/CLAUDE.md -o ./CLAUDE.md`.

## Conventions

- Prefer small, focused files with one clear responsibility
- Use conventional commits (`feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `test:`)
- Always update `README.md` and `CHANGELOG.md` when behavior changes
- Accessibility is non-negotiable — semantic HTML, ARIA, keyboard navigation

## Shared references

Consult Manfred shared docs in `~/.claude/shared/` (installed by `manfred-shared-knowledge`).

## Extend this file

Add project-specific guidance below this line. Keep it short and actionable.

---
```

- [ ] **Step 2: Commit**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git add CLAUDE.md
git commit -m "feat: add project-level CLAUDE.md template"
```

---

## Task 6: Create install.sh

**Files:**
- Create: `install.sh`

- [ ] **Step 1: Write `install.sh`**

Write `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/install.sh` with:

```bash
#!/bin/bash
set -euo pipefail

# Manfred Shared Knowledge — Claude Code Installer
# Usage: curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/install.sh | bash
# Use --force to overwrite existing files (creates backups first)

REPO_RAW="https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main"
CLAUDE_DIR="${CLAUDE_HOME:-$HOME/.claude}"
FORCE=false
INSTALLED=0
SKIPPED=0

# Parse flags
for arg in "$@"; do
  case $arg in
    --force) FORCE=true ;;
  esac
done

echo ""
echo "╔════════════════════════════════════════════════╗"
echo "║  Manfred Shared Knowledge — Claude Code Setup  ║"
echo "╚════════════════════════════════════════════════╝"
echo ""

install_file() {
  local remote_path="$1"
  local local_path="$2"
  local label="$3"

  if [ -f "$local_path" ] && [ "$FORCE" = false ]; then
    echo "  ⏭  $label — already exists, skipping"
    SKIPPED=$((SKIPPED + 1))
    return
  fi

  if [ -f "$local_path" ] && [ "$FORCE" = true ]; then
    local backup="${local_path}.backup.$(date +%Y%m%d%H%M%S)"
    cp "$local_path" "$backup"
    echo "  📦 $label — backed up to $(basename "$backup")"
  fi

  local dir
  dir=$(dirname "$local_path")
  mkdir -p "$dir"

  if curl -fsSL "$REPO_RAW/$remote_path" -o "$local_path" 2>/dev/null; then
    echo "  ✅ $label"
    INSTALLED=$((INSTALLED + 1))
  else
    echo "  ❌ $label — download failed"
    return 1
  fi
}

echo "Installing to $CLAUDE_DIR ..."
echo ""

echo "📋 Configuration"
install_file "shared/home-claude.md" "$CLAUDE_DIR/CLAUDE.md" "CLAUDE.md (home-level)"
echo ""

echo "📚 Shared References"
install_file "shared/manfred-brand.md" "$CLAUDE_DIR/shared/manfred-brand.md" "Manfred brand guidelines"
echo ""

echo "────────────────────────────────────────────────"
echo "  Installed: $INSTALLED file(s)"
echo "  Skipped:   $SKIPPED file(s) (already exist)"
echo "────────────────────────────────────────────────"
echo ""

if [ $INSTALLED -gt 0 ] || [ $SKIPPED -gt 0 ]; then
  echo "🔌 To install Manfred plugins, run this inside Claude Code:"
  echo "     /plugin marketplace add jens-wedin/manfred-shared-knowledge"
  echo ""
  echo "   Then: /plugin install <name>@manfred"
  echo ""
fi

if [ $SKIPPED -gt 0 ]; then
  echo "To overwrite existing files (with backup), re-run with --force"
  echo ""
fi

echo "📝 For project-level setup, copy the template CLAUDE.md to your repo:"
echo "   curl -fsSL $REPO_RAW/CLAUDE.md -o ./CLAUDE.md"
echo ""
```

- [ ] **Step 2: Make executable**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
chmod +x install.sh
```

- [ ] **Step 3: Syntax check**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
bash -n install.sh
```

Expected: no output, exit 0. Any error means there's a syntax problem — fix and retry.

- [ ] **Step 4: Optional shellcheck (if installed)**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
command -v shellcheck >/dev/null && shellcheck install.sh || echo "shellcheck not installed — skipping"
```

Expected: either no output (clean) or "shellcheck not installed — skipping". Treat warnings as informational; fix errors.

- [ ] **Step 5: Smoke test against a temp HOME**

The repo isn't published to GitHub yet, so simulate the copy by running install.sh against a local `REPO_RAW` pointing at the working tree via `file://`. But the script uses `https://...` hardcoded; instead, do a simpler test: verify the script parses and the function definitions are well-formed.

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
bash -c 'source ./install.sh --help 2>&1 || true' | head -5
```

Expected: the banner prints. (The script will then try to curl and fail since the repo isn't pushed yet — that's fine, we're only checking the script runs up to the curl call.)

Full end-to-end install testing happens after the repo is pushed to GitHub, in Task 10.

- [ ] **Step 6: Commit**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git add install.sh
git commit -m "feat: add install.sh with --force flag and Manfred banner"
```

---

## Task 7: Create uninstall.sh

**Files:**
- Create: `uninstall.sh`

- [ ] **Step 1: Write `uninstall.sh`**

Write `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/uninstall.sh` with:

```bash
#!/bin/bash
set -euo pipefail

# Manfred Shared Knowledge — Claude Code Uninstaller
# Removes files installed by install.sh
# Use --yes to skip confirmation prompts

CLAUDE_DIR="${CLAUDE_HOME:-$HOME/.claude}"
ASSUME_YES=false
REMOVED=0

for arg in "$@"; do
  case $arg in
    --yes|-y) ASSUME_YES=true ;;
  esac
done

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║  Manfred Shared Knowledge — Claude Code Uninstall  ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

FILES_TO_REMOVE=(
  "$CLAUDE_DIR/CLAUDE.md"
  "$CLAUDE_DIR/shared/manfred-brand.md"
)

echo "This will remove:"
for f in "${FILES_TO_REMOVE[@]}"; do
  if [ -f "$f" ]; then
    echo "  - $f"
  fi
done
echo ""

if [ "$ASSUME_YES" = false ]; then
  read -r -p "Proceed? [y/N] " reply
  case "$reply" in
    y|Y|yes|YES) ;;
    *) echo "Aborted."; exit 0 ;;
  esac
fi

for f in "${FILES_TO_REMOVE[@]}"; do
  if [ -f "$f" ]; then
    rm "$f"
    echo "  🗑  removed $f"
    REMOVED=$((REMOVED + 1))
  fi
done

# Clean up empty shared/ dir if nothing else is in it
if [ -d "$CLAUDE_DIR/shared" ] && [ -z "$(ls -A "$CLAUDE_DIR/shared")" ]; then
  rmdir "$CLAUDE_DIR/shared"
  echo "  🗑  removed empty $CLAUDE_DIR/shared/"
fi

echo ""
echo "────────────────────────────────────────────────"
echo "  Removed: $REMOVED file(s)"
echo "────────────────────────────────────────────────"
echo ""
echo "To remove the plugin marketplace, run inside Claude Code:"
echo "  /plugin marketplace remove manfred"
echo ""
```

- [ ] **Step 2: Make executable**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
chmod +x uninstall.sh
```

- [ ] **Step 3: Syntax check**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
bash -n uninstall.sh
```

Expected: no output, exit 0.

- [ ] **Step 4: Commit**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git add uninstall.sh
git commit -m "feat: add uninstall.sh to reverse install.sh"
```

---

## Task 8: Create README.md

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write README**

Write `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/README.md` with:

````markdown
# Manfred Shared Knowledge

Shared Claude Code skills, slash commands, plugins, and CLAUDE.md templates for Manfred.

## What this is

A public repo that packages Manfred's shared Claude Code assets so every team member gets the same setup with two commands.

## Install

**1. Install shared files (CLAUDE.md + `~/.claude/shared/`):**

```bash
curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/install.sh | bash
```

Re-run with `--force` to overwrite existing files (backups are created automatically).

**2. Register the plugin marketplace (inside Claude Code):**

```
/plugin marketplace add jens-wedin/manfred-shared-knowledge
```

Then browse with `/plugin` and install individual plugins with `/plugin install <name>@manfred`.

## What gets installed

| File | Destination |
|------|-------------|
| `shared/home-claude.md` | `~/.claude/CLAUDE.md` |
| `shared/manfred-brand.md` | `~/.claude/shared/manfred-brand.md` |

Plus any plugins you install via `/plugin install`.

## Project-level setup

For each project you want to follow Manfred conventions, drop the template `CLAUDE.md` into the project root:

```bash
curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/CLAUDE.md -o ./CLAUDE.md
```

Then extend it with project-specific rules below the `---` marker.

## Contributing

Open a PR for any of:

- **Skills** — add a new folder under `skills/<name>/` with a `SKILL.md`; add an `install_file` call to `install.sh`
- **Commands (slash commands / prompts)** — add under `commands/<name>.md`; add an `install_file` call to `install.sh`
- **Plugins** — scaffold under `plugins/<name>/` per [Claude Code plugin docs](https://docs.claude.com/en/docs/claude-code/plugins), then register the plugin in `.claude-plugin/marketplace.json` under the `plugins` array
- **Shared references** — add under `shared/`; add an `install_file` call to `install.sh`

Use conventional commits. Update `CHANGELOG.md` in the same PR.

## Uninstall

```bash
curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/uninstall.sh | bash
```

Then inside Claude Code:

```
/plugin marketplace remove manfred
```

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).
````

- [ ] **Step 2: Commit**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git add README.md
git commit -m "docs: add README covering install, contribute, uninstall"
```

---

## Task 9: Create CHANGELOG.md

**Files:**
- Create: `CHANGELOG.md`

- [ ] **Step 1: Write CHANGELOG**

Write `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge/CHANGELOG.md` with:

```markdown
# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] — 2026-04-19

### Added
- Initial scaffold: `.claude-plugin/marketplace.json`, `install.sh`, `uninstall.sh`
- Placeholder home-level `CLAUDE.md` installed via `shared/home-claude.md`
- Placeholder `shared/manfred-brand.md`
- Project-level `CLAUDE.md` template at repo root
- Empty `skills/`, `commands/`, `plugins/`, `shared/roles/` directories ready for content
- README with install, contribute, and uninstall instructions
```

- [ ] **Step 2: Commit**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git add CHANGELOG.md
git commit -m "docs: add CHANGELOG starting at v0.1.0"
```

---

## Task 10: End-to-end verification

**Files:** none created — verification only.

This task validates the repo scaffold works. It has two halves: local dry-run (before pushing) and remote install test (after pushing to GitHub).

- [ ] **Step 1: Check the git log looks clean**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git log --oneline
```

Expected: roughly 9 commits, each with a conventional-commit prefix (`chore:`, `feat:`, `docs:`). One per task from Tasks 1-9.

- [ ] **Step 2: Verify the tree**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
ls -la
ls -la .claude-plugin shared shared/roles plugins skills commands
```

Expected: every file and directory from the "File Structure" section above is present. `.claude-plugin/marketplace.json` exists. `shared/home-claude.md` and `shared/manfred-brand.md` exist. All `.gitkeep` files are present.

- [ ] **Step 3: Validate marketplace.json one more time**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
python3 -m json.tool .claude-plugin/marketplace.json
```

Expected: pretty-printed JSON with `"name": "manfred"`, `"plugins": []`, and the owner/metadata blocks.

- [ ] **Step 4: Pause for user — push to GitHub**

**STOP. Tell the user:**

> Local scaffold complete. Next step is to create the GitHub repo and push. Please either:
> 1. Create `github.com/jens-wedin/manfred-shared-knowledge` (public) and push, then tell me to continue, OR
> 2. Tell me to run `gh repo create` for you.

Do not proceed to Step 5 until the user confirms the remote exists and main is pushed.

- [ ] **Step 5: Remote install smoke test**

After the repo is public and `main` is pushed, test the real install flow:

```bash
TEST_HOME=$(mktemp -d)
CLAUDE_HOME="$TEST_HOME/.claude" bash -c 'curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/install.sh | bash'
echo "--- installed tree ---"
ls -la "$TEST_HOME/.claude"
ls -la "$TEST_HOME/.claude/shared"
```

Expected:
- The banner prints
- `INSTALLED: 2 file(s)` in the summary
- `$TEST_HOME/.claude/CLAUDE.md` exists
- `$TEST_HOME/.claude/shared/manfred-brand.md` exists
- The post-install message prints the `/plugin marketplace add` hint

Note: `install.sh` honours `CLAUDE_HOME` as an override for `$HOME/.claude` (added in Task 6 — `CLAUDE_DIR="${CLAUDE_HOME:-$HOME/.claude}"`). This is what allows the smoke test to install into a temp directory without touching the real `~/.claude`.

- [ ] **Step 6: Remote uninstall smoke test**

```bash
# Same TEST_HOME from Step 5
CLAUDE_HOME="$TEST_HOME/.claude" bash -c 'curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/uninstall.sh | bash -s -- --yes'
echo "--- after uninstall ---"
ls -la "$TEST_HOME/.claude" 2>/dev/null || echo "$TEST_HOME/.claude is gone — expected if shared/ was the only subdir"
rm -rf "$TEST_HOME"
```

Expected:
- `REMOVED: 2 file(s)` in the summary
- `CLAUDE.md` and `shared/manfred-brand.md` are gone
- `shared/` directory is removed (since it's empty)
- The `/plugin marketplace remove manfred` reminder is printed

- [ ] **Step 7: Register the marketplace in real Claude Code (manual)**

Inside Claude Code (not in this plan's execution session), run:

```
/plugin marketplace add jens-wedin/manfred-shared-knowledge
```

Expected: Claude Code accepts the marketplace. Running `/plugin` shows "manfred" as a source with 0 plugins. This confirms `marketplace.json` is valid.

- [ ] **Step 8: Tag the release**

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
git tag -a v0.1.0 -m "v0.1.0 — initial scaffold"
git push origin v0.1.0
```

Expected: tag pushed. Visible at `https://github.com/jens-wedin/manfred-shared-knowledge/releases/tag/v0.1.0`.

---

## Completion criteria

All of the following must be true:

- [ ] 10 tasks complete with commits on `main`
- [ ] `install.sh` and `uninstall.sh` pass `bash -n` cleanly
- [ ] `marketplace.json` passes JSON validation
- [ ] `CLAUDE_HOME=<tmp> install.sh` installs both files into the temp dir
- [ ] `CLAUDE_HOME=<tmp> uninstall.sh --yes` removes them and cleans up `shared/` if empty
- [ ] GitHub repo is public at `github.com/jens-wedin/manfred-shared-knowledge`
- [ ] `v0.1.0` tag exists
- [ ] Inside Claude Code, `/plugin marketplace add jens-wedin/manfred-shared-knowledge` succeeds
