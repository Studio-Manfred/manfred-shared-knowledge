---
name: install-manfred-claude-skills
description: Use when the user wants to install the Manfred Claude Code plugin marketplace (manfred-shared-knowledge) on a new machine, bring over Manfred Claude skills, or set up Claude for Manfred conventions. Triggers on "install manfred Claude skills", "set up manfred Claude", "install manfred-shared-knowledge", "add the Manfred plugin marketplace", "get the Manfred plugins". Walks through marketplace registration, plugin selection, and the optional home-level install.sh.
---

# Install Manfred Claude skills

Register the Manfred plugin marketplace in Claude Code, pick the plugins that fit the user's discipline, and optionally install shared home-level docs.

## When to use

- "install manfred Claude skills", "set up manfred Claude"
- "install manfred-shared-knowledge", "add the Manfred plugin marketplace"
- "get the Manfred plugins"

## Step 1: register the marketplace

Tell the user to run inside Claude Code:

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
```

## Step 2: pick plugins

Ask what the user does: design, product discovery, engineering, prototyping, writing. Recommend:

- **Everything:** `/plugin install manfred-discovery@manfred manfred-design-research@manfred manfred-ux-strategy@manfred manfred-design-systems@manfred manfred-ui-design@manfred manfred-interaction-design@manfred manfred-prototyping-testing@manfred manfred-design-ops@manfred manfred-toolkit@manfred manfred-dev@manfred manfred-knowledge@manfred` (split across several `/plugin install` calls if the UI prefers it).
- **Engineering only:** `manfred-dev`.
- **Product + research:** `manfred-discovery`, `manfred-design-research`, `manfred-ux-strategy`.
- **Design discipline:** `manfred-design-systems`, `manfred-ui-design`, `manfred-interaction-design`, `manfred-prototyping-testing`, `manfred-design-ops`.
- **Content + comms:** `manfred-toolkit`.

Give the exact `/plugin install <name>@manfred` commands for their answer. They can rerun this skill later to add more.

## Step 3: optional home-level install

If they want shared home-level docs (`~/.claude/CLAUDE.md`, `~/.claude/shared/manfred-brand.md`, `~/.claude/shared/DESIGN.md`, `~/.claude/shared/design-principles.md`), run:

```
curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-shared-knowledge/main/install.sh | bash
```

This step is OPTIONAL. Skip it for a lean install.

## Step 4: verify

- Type `/plugin` in Claude Code to see installed plugins.
- Ask Claude a trigger phrase such as "run QA on my code". It should match `manfred-dev:test-my-code`, which confirms skills are discoverable.

## Related skills

Next step once Claude knows the Manfred conventions: `bootstrap-manfred-project` (scaffold a new project or add the Manfred way-of-working to an existing repo).

## Links

- Marketplace repo: https://github.com/Studio-Manfred/manfred-shared-knowledge
- Bootstrap site: https://manfred-bootstrap-site.vercel.app
