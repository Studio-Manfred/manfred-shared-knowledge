---
name: deploy
description: Use when the user wants to release, deploy, ship, version bump, cut a release, update the changelog, or finalize the current state of a repo for publishing. Triggers on "deploy", "release", "ship it", "prep for release", "version bump", "cut a release", "update changelog and push".
---

# Deploy

Prepare a release for the current repository: update documentation, commit, and push.

## When to Use

- User says "deploy", "release", "ship it", "version bump", "cut a release"
- User asks to update changelog and/or push a release
- User wants to finalize the current repo state for publishing

**When NOT to use:**
- Just committing code (no release intent)
- CI/CD pipeline triggers (this is a manual release workflow)

## Overview

This skill automates the release workflow:
1. Analyze commits since the last release to understand what changed
2. Determine the correct version bump (major/minor/patch)
3. Update CHANGELOG.md following Keep a Changelog + Conventional Commits
4. Update README.md to reflect significant changes
5. Commit the documentation updates
6. Push to GitHub — but only after asking the user
7. Optionally tag the release

The goal is to produce clean, informative release documentation and make the mechanical parts (commit, push, tag) seamless.

## Quick Reference

| Step | Action | Confirmation needed? |
|------|--------|---------------------|
| 1 | Analyze commits since last tag | No |
| 2 | Propose version bump | Yes |
| 3 | Update CHANGELOG.md | No |
| 4 | Update README.md (if significant changes) | No |
| 5 | Commit docs | No |
| 6 | Push to remote | Yes |
| 7 | Create git tag | Yes (optional) |

## Step 1: Analyze the commit history

Figure out what's happened since the last release:

```bash
# Find the latest tag (this is the "last release")
git describe --tags --abbrev=0 2>/dev/null

# If no tags exist, use the full history
git log --oneline --no-decorate
```

If there's a previous tag, get commits since then:
```bash
git log <last-tag>..HEAD --pretty=format:"%h %s" --no-decorate
```

Parse each commit message according to Conventional Commits:
- `feat:` or `feat(scope):` → new feature
- `fix:` or `fix(scope):` → bug fix
- `docs:` → documentation
- `refactor:` → refactoring
- `test:` → tests
- `chore:` → maintenance
- `perf:` → performance
- `BREAKING CHANGE:` in footer or `!` after type → breaking change

Commits that don't follow the convention should still be included — categorize them by best guess or put them under "Other".

## Step 2: Determine the version bump

Use semantic versioning based on what the commits contain:

- **Major** (X.0.0): Any commit has `BREAKING CHANGE` or a `!` suffix (e.g., `feat!:`)
- **Minor** (x.Y.0): Any `feat:` commits (new functionality)
- **Patch** (x.y.Z): Only `fix:`, `docs:`, `refactor:`, `chore:`, etc.

If there's no previous version tag, start at `1.0.0` (or `0.1.0` if the project feels early-stage — use your judgment based on the repo's maturity).

Tell the user what version you're proposing and why, e.g.: "Based on 2 features and 1 fix, I'd bump from 1.2.0 → 1.3.0. Sound good?"

Wait for confirmation before proceeding.

## Step 3: Update CHANGELOG.md

Use the [Keep a Changelog](https://keepachangelog.com/) format. If CHANGELOG.md doesn't exist, create it. If it exists, prepend the new release section below the header.

Structure for each release:

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- Description of new features (from `feat:` commits)

### Changed
- Description of changes to existing functionality (from `refactor:`, `perf:`)

### Fixed
- Description of bug fixes (from `fix:` commits)

### Removed
- Anything that was removed
```

Only include sections that have entries. Don't add empty sections.

Write human-readable descriptions — not raw commit messages. Group related commits and summarize them into clear, useful entries. A reader should understand what changed without needing to read the git log.

**Example transformation:**
- Raw commits: `fix(auth): handle null token`, `fix(auth): add token refresh retry`
- Changelog entry: `- Fixed authentication issues with null tokens and added retry logic for token refresh`

## Step 4: Update README.md

Review the changes and decide if the README needs updating. Significant changes that warrant a README update:
- New features that users need to know about
- Changed APIs or usage patterns
- New dependencies or requirements
- Removed functionality

Minor fixes, internal refactors, and test changes typically don't need README updates. Use your judgment — if nothing significant changed for the end user, skip this step and tell the user why.

When updating, modify the relevant sections in place rather than appending. Keep the existing README structure and voice.

## Step 5: Commit

Stage and commit the documentation changes:

```bash
git add CHANGELOG.md README.md
git commit -m "docs: update changelog and readme for vX.Y.Z"
```

Use `docs:` as the commit type since this is a documentation update. Only stage CHANGELOG.md and README.md — don't accidentally include other files.

## Step 6: Push (with confirmation)

Before pushing, show the user:
- Which branch you're on
- Which remote you'd push to
- A summary of what will be pushed (the docs commit + any unpushed commits)

Then ask: "Ready to push to `origin/main`?" (or whatever the branch/remote is).

Only push after explicit confirmation. Use:
```bash
git push origin <branch>
```

## Step 7: Tag (optional)

After pushing, suggest creating a git tag for the release:
```bash
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin vX.Y.Z
```

This is optional — ask the user if they want the tag. Some projects rely on tags for CI/CD releases, others don't.

## Edge cases

- **No conventional commits**: If the commit history doesn't use conventional commits at all, still do your best to categorize changes by reading the messages and diffs. Mention to the user that adopting Conventional Commits would make future changelogs more accurate.
- **Monorepo**: If the repo has multiple packages, ask the user which one they're releasing.
- **Dirty working tree**: If there are uncommitted changes, warn the user and ask if they want to commit those first or proceed with just the docs update.
- **No remote**: If there's no remote configured, skip the push step and let the user know.

## Common Mistakes

- **Skipping the changelog under pressure**: Even if the user says "just push it", the changelog is the point of this skill. Offer to make it fast, but don't skip it.
- **Raw commit messages in changelog**: Always rewrite commit messages into human-readable descriptions. Group related commits.
- **Forgetting to ask about tags**: Step 7 is optional but should always be offered — some CI/CD pipelines depend on tags.
- **Staging extra files**: Only stage CHANGELOG.md and README.md. Never use `git add .` or `git add -A`.
- **Pushing without confirmation**: Steps 2 and 6 both require explicit user confirmation before proceeding.
