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
/plugin install manfred-a11y@manfred       # accessibility — design, dev, QA
/plugin install manfred-writing@manfred    # LinkedIn (Swedish), meeting summaries, transcript anonymisation
/plugin install manfred-product@manfred    # Scandic product brief / PRD
/plugin install manfred-dev@manfred        # Vite/React: pre-merge QA, deploy, release
/plugin install manfred-knowledge@manfred  # Obsidian vault linting, batch Markdown conversion
```

**3. (Optional) Install the home-level CLAUDE.md and shared design references:**

```bash
curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-shared-knowledge/main/install.sh | bash
```

This installs the home `~/.claude/CLAUDE.md` and `~/.claude/shared/` reference docs only — skills are now plugin-distributed.

Re-run with `--force` to overwrite existing files (backups are created automatically).

## Plugins

| Plugin | Skills | Use it if |
|--------|--------|-----------|
| `manfred-a11y` | `a11y-design`, `a11y-dev`, `a11y-qa` | You design or build interfaces and want WCAG-grade accessibility checks across design, dev, and QA |
| `manfred-writing` | `linkedin-reflect`, `linkedin-show-and-tell`, `linkedin-teach`, `meeting-summary`, `transcript-anonymizer` | You publish on LinkedIn (Swedish), summarise meetings, or process research transcripts |
| `manfred-product` | `brief-prd` | You write product briefs / PRDs using the Scandic 8-section template |
| `manfred-dev` | `deploy`, `release`, `test-my-code` | You ship Vite/React features and want pre-merge QA gates plus production-grade release flow |
| `manfred-knowledge` | `markitdown-convert`, `clippings-linter` | You manage an Obsidian vault or batch-convert documents to Markdown |

Each plugin's own `README.md` lists the trigger phrases for its skills.

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
