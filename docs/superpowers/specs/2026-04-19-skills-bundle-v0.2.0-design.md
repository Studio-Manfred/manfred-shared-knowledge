# Skills Bundle v0.2.0 — Design Spec

**Date:** 2026-04-19
**Author:** Jens Wedin
**Status:** Approved via brainstorming
**Target repo:** `github.com/jens-wedin/manfred-shared-knowledge`

## Purpose

Ship 11 existing skills from Jens's `~/.claude/skills/` as part of the Manfred shared-knowledge repo. Distribute as loose files copied into teammates' `~/.claude/skills/` via `install.sh`. Migration to Claude Code plugin format is explicit future work.

## Skills included

| Skill | Subdirs kept | Subdirs excluded |
|-------|--------------|------------------|
| `a11y-design` | `references/` | — |
| `a11y-dev` | `references/` | — |
| `a11y-qa` | `references/`, `scripts/` | — |
| `brief-prd` | — | `evals/` |
| `deploy` | — | — |
| `linkedin-reflect` | — | — |
| `linkedin-show-and-tell` | — | — |
| `linkedin-teach` | — | — |
| `markitdown-convert` | — | `evals/` |
| `meeting-summary` | — | — |
| `transcript-anonymizer` | — | — |

Each skill gets copied verbatim from `~/.claude/skills/<name>/` minus the excluded subdirs and any `.DS_Store` files.

## Non-goals

- **No plugin migration.** Skills stay as loose files under `skills/<name>/` in the repo; teammates install to `~/.claude/skills/<name>/`. Plugin migration is a future release.
- **No per-skill versioning.** The repo version (semver) is the only version. `CHANGELOG.md` records what changed per release.
- **No on-demand prompt fetcher.** Separate future feature.
- **No removal of `skills/.gitkeep`** is explicit — it disappears naturally when real skills land.

## Install model

### New: `install_skills` function in `install.sh`

Constants at the top of `install.sh`:
```bash
REPO_GIT="https://github.com/jens-wedin/manfred-shared-knowledge.git"
```

A hardcoded bash array inside `install.sh` enumerates the skill names:
```bash
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

Behavior:
1. Check `command -v git` — if missing, print error with install hint and increment `FAILED`.
2. `git clone --depth=1 --quiet "$REPO_GIT" "$TMP"` into a `mktemp -d` path.
3. On clone failure: print error, increment `FAILED`, `rm -rf $TMP`, return. (Do not abort the entire installer — the `shared/` files installed earlier should still count as successes.)
4. For each `$name` in `SKILLS`, call `install_skill_dir "$TMP/skills/$name" "$CLAUDE_DIR/skills/$name" "$name"`.
5. Trap clean up temp dir on return.

`install_skill_dir` semantics mirror `install_file`:
- If dest exists and `FORCE=false`: increment `SKIPPED`, return.
- If dest exists and `FORCE=true`: `mv` old dir to `${dest}.backup.$(date +%Y%m%d%H%M%S)`, then copy.
- `mkdir -p "$(dirname "$dest")"`.
- `cp -R "$src" "$dest"`. Increment `INSTALLED`.

Counter summary unchanged: `Installed`, `Skipped`, `Failed`. Exit 1 if `FAILED > 0`.

### Call order in `install.sh` body

```
install_file  shared/home-claude.md   ->  $CLAUDE_DIR/CLAUDE.md
install_file  shared/manfred-brand.md ->  $CLAUDE_DIR/shared/manfred-brand.md
install_skills                           # one clone + 11 dir copies
```

Shared files keep their current `curl`-based install so the first few messages print before the larger git clone.

### Error message for missing `git`

```
  ❌ skills — git not found. Install git and re-run.
     On macOS: xcode-select --install
     On Debian/Ubuntu: sudo apt-get install git
```

### Post-install summary addition

When skills install successfully, print after the plugin marketplace hint:
```
🧰 Installed 11 Manfred skills under ~/.claude/skills/
   Use them in Claude Code via /<skill-name> or let skills auto-trigger.
```

## Uninstall model

Extend `uninstall.sh`:

1. Add the same `SKILLS` array.
2. In the "This will remove:" preview, list each `$CLAUDE_DIR/skills/$name/` that exists.
3. After removing `FILES_TO_REMOVE`, loop `SKILLS` and `rm -rf "$CLAUDE_DIR/skills/$name"` if the dir exists, incrementing `REMOVED` (rename the counter or just keep the existing one).
4. Keep the TTY/--yes guard from v0.1.1.
5. After file removal, also try to `rmdir "$CLAUDE_DIR/skills"` if empty.

## Documentation

### README

Add a new section after "What gets installed" and before "Project-level setup":

```markdown
## Skills

The installer adds these 11 skills to `~/.claude/skills/`. Each skill triggers on a specific set of phrases described in its `SKILL.md` frontmatter — see each skill's folder for the triggers.

| Skill | Purpose |
|-------|---------|
| `a11y-design` | Review designs for accessibility before handoff |
| `a11y-dev` | Write accessible front-end code (WCAG, ARIA, keyboard) |
| `a11y-qa` | Run accessibility audits on implemented code |
| `brief-prd` | Author a Scandic-style 8-section product brief |
| `deploy` | Cut a release — changelog, version bump, tag, push |
| `linkedin-reflect` | Reflective LinkedIn post (Swedish, Jens Wedin voice) |
| `linkedin-show-and-tell` | Demo/showcase LinkedIn post (Swedish) |
| `linkedin-teach` | Teaching LinkedIn post (Swedish) |
| `markitdown-convert` | Batch-convert PDFs/docs/images to Markdown |
| `meeting-summary` | Summarize meeting notes or transcripts (Swedish/English) |
| `transcript-anonymizer` | Strip PII from transcripts for GDPR compliance |

Skills ship as loose files for now. A migration to Claude Code plugins (automatic updates via the `manfred` marketplace) is planned for a later release.
```

Update the existing "What gets installed" table to mention skills go under `~/.claude/skills/<name>/`.

### CHANGELOG

```markdown
## [0.2.0] — 2026-04-19

### Added
- Eleven shared skills bundled under `skills/`: `a11y-design`, `a11y-dev`, `a11y-qa`, `brief-prd`, `deploy`, `linkedin-reflect`, `linkedin-show-and-tell`, `linkedin-teach`, `markitdown-convert`, `meeting-summary`, `transcript-anonymizer`
- `install.sh` now performs a shallow git clone to fetch multi-file skills and copies them into `~/.claude/skills/<name>/`
- `install.sh` errors clearly if `git` is not on PATH
- `uninstall.sh` removes installed skills (honours `--yes` and the existing TTY guard)
- README documents the 11 bundled skills and notes the plugin-migration roadmap
```

### `shared/home-claude.md`

Add a short note after "Shared references":
```
Manfred skills are installed under `~/.claude/skills/`. They trigger automatically
on keywords — see ~/.claude/skills/<name>/SKILL.md for each skill's trigger list.
```

## Success criteria

- `install.sh` on a fresh `$CLAUDE_HOME` installs 2 shared files + 11 skill directories, exits 0
- `install.sh --force` on an existing `$CLAUDE_HOME` backs up each skill dir before overwriting, exits 0
- `uninstall.sh --yes` removes the same 2 files + 11 skill dirs, exits 0, leaves no empties
- Claude Code loads the installed skills (verified by running `claude /a11y-dev` or similar in the test home)
- `git clone --depth=1` dependency is called out in the README's "Install" section
- Error path: if `git` is missing, installer still completes the shared-file copy and only flags the skill step as failed

## Open questions

None blocking.

Deferred:
- Plugin migration (future release; likely one plugin per semantic group or one bundle — decide when we migrate)
- On-demand prompt/slash-command fetcher
- Per-skill CHANGELOG tracking
