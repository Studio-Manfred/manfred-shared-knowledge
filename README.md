# Manfred Shared Knowledge

Shared Claude Code skills, slash commands, plugins, and CLAUDE.md templates for Manfred.

## What this is

A public repo that packages Manfred's shared Claude Code assets so every team member gets the same setup with two commands.

## Install

**1. Install shared files (CLAUDE.md + `~/.claude/shared/`):**

```bash
curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-shared-knowledge/main/install.sh | bash
```

Re-run with `--force` to overwrite existing files (backups are created automatically). Skills install via a shallow git clone, so `git` must be available on your machine.

**2. Register the plugin marketplace (inside Claude Code):**

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
```

Then browse with `/plugin` and install individual plugins with `/plugin install <name>@manfred`.

## What gets installed

| Source | Destination |
|--------|-------------|
| `shared/home-claude.md` | `~/.claude/CLAUDE.md` |
| `shared/manfred-brand.md` | `~/.claude/shared/manfred-brand.md` |
| `shared/DESIGN.md` | `~/.claude/shared/DESIGN.md` |
| `shared/design-principles.md` | `~/.claude/shared/design-principles.md` |
| `skills/<name>/` (11 skills) | `~/.claude/skills/<name>/` |

Plus any plugins you install via `/plugin install`.

## Skills

The installer adds these 11 skills to `~/.claude/skills/`. Each triggers automatically on specific phrases described in its `SKILL.md` frontmatter.

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
| `meeting-summary` | Summarize meeting notes or transcripts |
| `transcript-anonymizer` | Strip PII from transcripts for GDPR compliance |

Skills ship as loose files for now. A migration to proper Claude Code plugins — distributed and auto-updated through the `manfred` marketplace — is planned for a later release.

## Project-level setup

For each project you want to follow Manfred conventions, drop the template `CLAUDE.md` into the project root:

```bash
curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-shared-knowledge/main/CLAUDE.md -o ./CLAUDE.md
```

Then extend it with project-specific rules below the `---` marker.

## Contributing

Open a PR for any of:

- **Skills** — add a new folder under `skills/<name>/` with a `SKILL.md`; add an `install_file` call to `install.sh`
- **Commands (slash commands / prompts)** — add under `commands/<name>.md`; add an `install_file` call to `install.sh`
- **Plugins** — scaffold under `plugins/<name>/` per [Claude Code plugin docs](https://docs.claude.com/en/docs/claude-code/plugins), then register the plugin in `.claude-plugin/marketplace.json` under the `plugins` array
- **Shared references** — add under `shared/`; add an `install_file` call to `install.sh`
- **Role playbooks** — add under `shared/roles/<role-name>.md`; add an `install_file` call to `install.sh`

Use conventional commits. Update `CHANGELOG.md` in the same PR.

## Uninstall

```bash
curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-shared-knowledge/main/uninstall.sh | bash -s -- --yes
```

Run without `--yes` (by downloading the script first) for interactive confirmation.

Then inside Claude Code:

```
/plugin marketplace remove manfred
```

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).
