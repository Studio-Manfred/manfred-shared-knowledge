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
