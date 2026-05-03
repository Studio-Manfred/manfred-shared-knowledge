---
name: version-control-strategy
description: Use when defining version control for design files, components, tokens, or design assets — anyone says "version control for design", "design file versioning", "Figma versioning strategy", "component library versioning", "design system semver", "design changelog", "design asset versions", "design file branching". Manfred-flavoured: SemVer for components and tokens, changelog mandatory, breaking changes explicit.
---

# version-control-strategy

Design moves. Designers iterate, components evolve, tokens get renamed, the system gets reshaped. Without version control, every change becomes "wait, which version were we using?" — and consumer code breaks silently.

Manfred uses **SemVer for components + tokens** (same conventions as `Studio-Manfred/manfred-design_system`), Figma's named versions for design files, and mandatory changelogs for everything that consumers depend on.

## Overview

Five things to version, each with a different strategy:

| What | Strategy | Why |
|---|---|---|
| **Design system code** | SemVer (`major.minor.patch`) via `npm` package | Component consumers need predictable upgrade paths |
| **Design tokens** | Versioned alongside the code, breaking changes are major | Token renames break every consumer |
| **Component libraries** | SemVer | Same as above — compose and upgrade |
| **Figma design files** | Named versions at milestones + page-based history | Designers + stakeholders need to reference past states |
| **Icons + assets** | Versioned with the design system; deprecated assets archived not deleted | Consumers depending on a removed asset break |

The principle that ties them: **breaking changes get loud announcements; non-breaking changes get logged**.

## When to use

- Setting up version control for a new design system
- Defining the changelog process for an existing design system that doesn't have one
- Reviewing a versioning approach that's caused breakage (consumer code broken silently)
- Onboarding a new contributor to the design system
- Documenting the version policy for downstream consumers

**Skip when:**

- Pre-release single-team work where there are no external consumers (don't manufacture process)
- Project-local components with no consumers outside the project (the project's git is enough)
- The user wants regular code SemVer (it's a developer thing, not specific to design — defer to project conventions)

## Pre-flight

Ask:

- What's being versioned? (Design system code? Tokens? Figma files? All three?)
- Who are the consumers? (One project? Multiple? External clients?)
- Existing strategy? (Most teams have something — chaos counts)
- Where do consumers find the changelog? (npm? GitHub releases? Notion? Storybook?)
- Last time a breaking change broke a consumer silently? (If recent — that's the failure mode the strategy needs to prevent.)

## The hard rules

| Rule | What it means |
|---|---|
| **SemVer for code (components + tokens)** | `major.minor.patch`. Breaking changes = major (rename, remove, change behaviour). New additions backward-compatible = minor. Bug fixes / refinements = patch. |
| **Changelog mandatory** | Every release has a changelog entry. "Updated some components" doesn't count — list what changed, why, and migration steps for breaking changes. |
| **Breaking changes flagged loudly** | Major version bumps come with: changelog entry tagged `BREAKING`, migration guide, prominent README update, optional Slack / email announcement to consumers. |
| **Deprecate before removing** | Don't remove a component or token in one release. Mark deprecated → wait at least one minor release → remove in next major. Gives consumers time to migrate. |
| **Figma: named versions at milestones** | Don't version every save. Version at meaningful moments: design system v1.0, v1.1, v2.0. Within a file, use Figma's page-based history. |
| **Archive, don't delete** | Removed components / icons / assets get archived in a deprecated section, not removed entirely. Consumers depending on them can find the migration path. |
| **Communicate changes** | Breaking changes: explicit channel (Slack design-system, email, release notes). Non-breaking: changelog entry suffices. |

## Versioning per artifact

### Design system code (npm package)

SemVer:

| Bump | When | Example |
|---|---|---|
| **Major** (`1.0.0` → `2.0.0`) | Breaking change — renamed component, removed prop, changed default behaviour | `Button` renamed to `Action`, `<Toast>` API changed |
| **Minor** (`1.0.0` → `1.1.0`) | New components or features, backward-compatible | New `<Combobox>` added, new `variant="brand-inverse"` for `<Button>` |
| **Patch** (`1.0.0` → `1.0.1`) | Bug fixes, internal refinements, no API change | Fix focus ring colour in dark mode, fix Storybook story typo |

Tag every release in git: `git tag -a v1.2.3 -m "v1.2.3 — <summary>"`.

### Design tokens

Versioned alongside the design system code (same package, same version):

- Adding a new token = minor
- Renaming a token = major (breaks every consumer using the old name)
- Changing a token's value = patch (backward-compatible — same name, new colour) **unless** it's a contrast / accessibility regression in which case treat as breaking and major

Token changelog entries name the token + the change:

```
- Added: `--color-feedback-success-bg` (new semantic for success surfaces)
- Renamed: `--color-text-grey` → `--color-text-muted` (BREAKING — update consumers)
- Changed: `--color-business-blue` value `#2c2bea` → `#2c28ec` (refined; same intent)
```

### Component libraries

Same as design system code (usually the same package). Component-level changes documented per release:

- New component = minor (e.g. `Combobox` added)
- New variant on existing component = minor
- Removed component = major
- Renamed prop = major
- Changed default behaviour = major
- Bug fix = patch

### Figma design files

Different model — Figma versions are about preserving past states, not about API contracts.

- **Named versions at milestones**: `v1-exploration` (Day 2 of sprint), `v2-refinement` (after team crit), `v3-final` (pre-handoff)
- **Branch-based**: main file is "approved", feature branches for work-in-progress (Figma's branching feature)
- **Page-based**: within a file, Figma's auto-version-history captures saves; named pages capture states ("01 Final", "02 Exploration", "03 Archive")
- **Don't delete; archive**: a "graveyard" page or file holds removed designs. Future-you might need them.

### Icons + assets

Versioned with the design system. Names follow `manfred-design-systems:icon-system` conventions.

- Adding an icon = minor
- Renaming = major (rare — usually keep name, swap SVG)
- Removing = major, with deprecation period

Archived icons live in a deprecated section of the icon library + an entry in the changelog noting the new equivalent.

## Branching strategy (design system code)

```
main                  ← production-ready, tagged releases
└── feat/STU-XXX-foo  ← feature branch for new component or change
    └── PR → main
    
hotfix/STU-XXX-bar   ← urgent fix branch (off main, merged back to main + cherry-picked to active release branches if needed)

release/v1.x.x       ← optional long-lived support branch for older majors (rare; only when consumers can't upgrade)
```

Pattern matches engineering convention. If the design system code lives in the same repo as a project, follow that project's branching.

## Changelog format

```markdown
# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] — 2026-05-15

### Added
- `Combobox` component — searchable single-select with keyboard nav
- `--color-feedback-warning-bg` token — semantic warning surface

### Changed
- `Button` `variant="brand"` updated to use `--color-business-blue` (no API change)

### Fixed
- Focus ring colour in dark mode now resolves correctly

### Deprecated
- `--color-text-grey` — use `--color-text-muted` instead. Removed in 2.0.0.

## [1.1.0] — 2026-04-30

### Added
- ...
```

Every release. Public-facing. Linked from README + Storybook.

For **breaking changes**, add a migration guide:

```markdown
### BREAKING — Migration guide for v1.x → v2.0

**`Button` renamed to `Action`**

Old:
\`\`\`tsx
<Button variant="primary">Save</Button>
\`\`\`

New:
\`\`\`tsx
<Action variant="primary">Save</Action>
\`\`\`

Codemod available: `npx @manfred/migrate-button-to-action`.
```

## Communicating changes

| Change | Channel |
|---|---|
| Patch | Changelog only |
| Minor | Changelog + Storybook update + brief Slack note in #design-system |
| Major | Changelog + migration guide + prominent README + Slack announcement + (optional) email to known consumers |

Major changes shouldn't be a surprise. Consumers should hear about them at least one minor release before the major lands.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We don't need a changelog, the team's small" | The team's small *now*. The changelog protects future-you and any new contributor. Write it from day one. |
| "We'll do SemVer loosely" | "Loosely" = "consumers can't trust the version number". Then SemVer doesn't help. Either commit or don't bother. |
| "Breaking changes are rare, no need for migration guides" | The one breaking change without a migration guide is the one that breaks 5 consumer projects silently. Always provide. |
| "Figma versions every save" | Save-history is automatic; naming every save creates noise. Name at milestones only. |
| "We'll just remove the deprecated component, nobody uses it" | "Nobody uses it" = "I don't grep across consumer projects". Deprecate first, remove later. |
| "Token name changes are minor — same value, just renamed" | Rename = breaking. Every consumer referencing the old name breaks. Major. |

## Red flags — STOP

- About to remove a component or token without a deprecation period
- Releasing a major version with no migration guide
- Skipping the changelog for "small" changes
- Versioning every Figma save
- Treating a token rename as a minor or patch
- "Force-publishing" a breaking change without notice to consumers
- Working on a long-lived feature branch without rebasing periodically (merge conflicts compound)

## Manfred lens

Version control is **infrastructure** — Cagan/Torres lens doesn't apply directly. But: a well-versioned design system reduces the friction of every project that consumes it. Bad versioning produces silent breakage and trust loss; the design system stops being trusted, consumers fork, the system becomes decoration.

## Cross-references

- `manfred-design-systems:design-token` — for token-rename impact
- `manfred-design-systems:component-spec` — for the spec side of new components
- `manfred-design-systems:naming-convention` — for what gets renamed and why
- `manfred-design-ops:design-review-process` — design system changes go through review
- `manfred-design-ops:team-workflow` — version bumps fit into release rituals

## Tools used

- `Bash` — git, semver tagging, changelog generation
- `Read` — existing changelog, package.json, recent PRs
- `Write` — changelog entries, migration guides, release notes
- `manfred-design-systems:design-token` — for token-version impact
- `manfred-design-systems:component-spec` — for component-version impact

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
