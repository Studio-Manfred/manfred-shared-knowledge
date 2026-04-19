# Skills Bundle v0.2.0 Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bundle 11 Manfred skills into `manfred-shared-knowledge` v0.2.0; ship via shallow git clone from `install.sh`.

**Architecture:** Copy 11 skill directories into `skills/` in the repo (excluding `evals/`). `install.sh` gains an `install_skills` function that shallow-clones the repo into a tmp dir and copies each `skills/<name>/` into `~/.claude/skills/<name>/`. `uninstall.sh` removes those directories. README + CHANGELOG + `shared/home-claude.md` updated.

**Tech Stack:** bash, git, markdown. No build step.

**Working dir:** `/Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge`

---

## Task 1: Copy skills from `~/.claude/skills/` into `skills/`

**Files:** 11 directories under `skills/`, removing placeholder `skills/.gitkeep`.

- [ ] Copy each skill with `cp -R`, excluding `evals/`.

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
rm -f skills/.gitkeep
for name in a11y-design a11y-dev a11y-qa brief-prd deploy \
            linkedin-reflect linkedin-show-and-tell linkedin-teach \
            markitdown-convert meeting-summary transcript-anonymizer; do
  rm -rf "skills/$name"
  cp -R "$HOME/.claude/skills/$name" "skills/$name"
  rm -rf "skills/$name/evals"
  find "skills/$name" -name .DS_Store -delete
done
```

- [ ] Verify SKILL.md present in each, no evals/ remaining:

```bash
for name in skills/*/; do
  [ -f "$name/SKILL.md" ] || echo "MISSING SKILL.md in $name"
  [ -d "$name/evals" ] && echo "evals/ left in $name"
done
```

Expected: no output.

- [ ] Commit:

```bash
git add skills/
git commit -m "feat: bundle 11 Manfred skills into skills/"
```

## Task 2: Extend `install.sh` with `install_skills` via git clone

**Files:** modify `install.sh` (add `REPO_GIT`, `SKILLS` array, `install_skill_dir`, `install_skills`, call from body).

- [ ] Add near the top (below `REPO_RAW`):

```bash
REPO_GIT="https://github.com/jens-wedin/manfred-shared-knowledge.git"
SKILLS=(
  a11y-design a11y-dev a11y-qa
  brief-prd
  deploy
  linkedin-reflect linkedin-show-and-tell linkedin-teach
  markitdown-convert
  meeting-summary
  transcript-anonymizer
)
```

- [ ] Add `install_skill_dir` function next to `install_file`:

```bash
install_skill_dir() {
  local src="$1"
  local dest="$2"
  local label="$3"

  if [ -d "$dest" ] && [ "$FORCE" = false ]; then
    echo "  ⏭  skill/$label — already exists, skipping"
    SKIPPED=$((SKIPPED + 1))
    return
  fi

  if [ -d "$dest" ] && [ "$FORCE" = true ]; then
    local backup
    backup="${dest}.backup.$(date +%Y%m%d%H%M%S)"
    mv "$dest" "$backup"
    echo "  📦 skill/$label — backed up to $(basename "$backup")"
  fi

  mkdir -p "$(dirname "$dest")"
  if cp -R "$src" "$dest"; then
    echo "  ✅ skill/$label"
    INSTALLED=$((INSTALLED + 1))
  else
    echo "  ❌ skill/$label — copy failed"
    FAILED=$((FAILED + 1))
  fi
}

install_skills() {
  if ! command -v git >/dev/null 2>&1; then
    echo "  ❌ skills — git not found. Install git and re-run."
    echo "     On macOS: xcode-select --install"
    echo "     On Debian/Ubuntu: sudo apt-get install git"
    FAILED=$((FAILED + 1))
    return
  fi

  local tmp
  tmp=$(mktemp -d)
  if ! git clone --depth=1 --quiet "$REPO_GIT" "$tmp" 2>/dev/null; then
    echo "  ❌ skills — git clone failed"
    FAILED=$((FAILED + 1))
    rm -rf "$tmp"
    return
  fi

  local name
  for name in "${SKILLS[@]}"; do
    install_skill_dir "$tmp/skills/$name" "$CLAUDE_DIR/skills/$name" "$name"
  done

  rm -rf "$tmp"
}
```

- [ ] Add a "⚡ Skills" section in the install body after "📚 Shared References":

```bash
echo "⚡ Skills"
install_skills
echo ""
```

- [ ] After the `--force` hint block, add a skills summary line shown only when skills were installed:

```bash
if [ $INSTALLED -gt 0 ]; then
  echo "🧰 Skills live under ~/.claude/skills/ — triggered automatically by keywords"
  echo ""
fi
```

- [ ] Syntax + shellcheck:

```bash
bash -n install.sh
command -v shellcheck >/dev/null && shellcheck install.sh || echo "shellcheck skipped"
```

- [ ] Commit:

```bash
git add install.sh
git commit -m "feat: install.sh installs 11 skills via shallow git clone"
```

## Task 3: Extend `uninstall.sh` to remove skills

**Files:** modify `uninstall.sh`.

- [ ] Add `SKILLS` array right after `CLAUDE_DIR` (copy verbatim from install.sh).
- [ ] Extend the "This will remove:" preview — after the existing file loop, loop `SKILLS`:

```bash
for name in "${SKILLS[@]}"; do
  if [ -d "$CLAUDE_DIR/skills/$name" ]; then
    echo "  - $CLAUDE_DIR/skills/$name/"
  fi
done
```

- [ ] After the existing `rm` loop, add:

```bash
for name in "${SKILLS[@]}"; do
  if [ -d "$CLAUDE_DIR/skills/$name" ]; then
    rm -rf "$CLAUDE_DIR/skills/$name"
    echo "  🗑  removed $CLAUDE_DIR/skills/$name/"
    REMOVED=$((REMOVED + 1))
  fi
done

if [ -d "$CLAUDE_DIR/skills" ] && [ -z "$(ls -A "$CLAUDE_DIR/skills")" ]; then
  rmdir "$CLAUDE_DIR/skills"
  echo "  🗑  removed empty $CLAUDE_DIR/skills/"
fi
```

- [ ] Syntax + shellcheck:

```bash
bash -n uninstall.sh
command -v shellcheck >/dev/null && shellcheck uninstall.sh || echo "shellcheck skipped"
```

- [ ] Commit:

```bash
git add uninstall.sh
git commit -m "feat: uninstall.sh removes installed skills"
```

## Task 4: Update docs

**Files:** `README.md`, `CHANGELOG.md`, `shared/home-claude.md`.

- [ ] README: add "## Skills" section between "What gets installed" and "Project-level setup", per the spec's table of 11 skills.
- [ ] README: update the "What gets installed" table to include a row: `skills/<name>/` → `~/.claude/skills/<name>/`.
- [ ] README: in the Install section, mention `git` is required for the skills step.
- [ ] CHANGELOG: add `## [0.2.0] — 2026-04-19` block per spec.
- [ ] shared/home-claude.md: add the Manfred skills note under "Shared references".
- [ ] Commit:

```bash
git add README.md CHANGELOG.md shared/home-claude.md
git commit -m "docs: document v0.2.0 skills bundle"
```

## Task 5: End-to-end smoke test

- [ ] Local clone-less simulation (use `file://` URL for git clone target):

```bash
cd /Users/jens.wedin/Sandbox/Code/manfred-shared-knowledge
TMP=$(mktemp -d)
CLAUDE_HOME="$TMP/claude" REPO_GIT="$(pwd)" bash ./install.sh
EC=$?
echo "EXIT=$EC"
ls "$TMP/claude/skills" | wc -l    # expect: 11
head -1 "$TMP/claude/skills/a11y-dev/SKILL.md"
```

Note: the local install.sh hardcodes `REPO_GIT`. Either edit the script temporarily to honour the env var, or push the commits to origin first and rely on the real clone. The simpler path is to **push main**, then re-run the smoke test using the live remote:

```bash
git push origin main
TMP=$(mktemp -d)
CLAUDE_HOME="$TMP/claude" bash -c 'curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/install.sh | bash'
echo "EXIT=$?"
ls "$TMP/claude/skills"
```

Expected: 11 directories, each with a `SKILL.md`.

- [ ] Uninstall smoke test:

```bash
CLAUDE_HOME="$TMP/claude" bash -c 'curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/uninstall.sh | bash -s -- --yes'
ls "$TMP/claude" 2>/dev/null || echo "claude dir gone"
rm -rf "$TMP"
```

Expected: skills directory gone; shared + CLAUDE.md gone; `$TMP/claude` empty or removed.

- [ ] Tag:

```bash
git tag -a v0.2.0 -m "v0.2.0 — 11 Manfred skills bundled"
git push origin v0.2.0
```

## Completion criteria

- [ ] 11 skill dirs committed under `skills/`, no `evals/` remaining
- [ ] `install.sh` passes `bash -n` and `shellcheck`; smoke test installs 11 skill dirs against a temp home
- [ ] `uninstall.sh` removes those 11 dirs cleanly
- [ ] README "Skills" section present, CHANGELOG v0.2.0 present
- [ ] v0.2.0 tag pushed to origin
