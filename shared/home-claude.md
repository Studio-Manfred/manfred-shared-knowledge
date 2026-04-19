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
