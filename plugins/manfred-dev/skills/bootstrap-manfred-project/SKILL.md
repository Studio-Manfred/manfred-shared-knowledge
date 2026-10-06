---
name: bootstrap-manfred-project
description: Use when the user wants to scaffold a new Manfred project from scratch, add the Manfred way-of-working to an existing repo, or download the manfred-bootstrap template without stamping. Triggers on "start a new Manfred project", "new Manfred project", "bootstrap a Manfred project", "stamp a new Manfred project", "add manfred-bootstrap to this project", "overlay Manfred bootstrap", "add Manfred to this repo", "download the latest bootstrap", "get manfred-bootstrap", "clone the Manfred template". Walks through prereqs, asks for name/prefix/provisioning, and runs the single curl install.sh one-liner.
---

# Bootstrap a Manfred project

Scaffold a new Manfred project, overlay the Manfred way-of-working (WoW) onto an existing repo, or download the template. All three run through `curl … install.sh | bash -s -- …` against the public `Studio-Manfred/manfred-bootstrap` repo.

## When to use

- "start a new Manfred project", "new Manfred project", "bootstrap a Manfred project", "stamp a new Manfred project"
- "add manfred-bootstrap to this project", "overlay Manfred bootstrap", "add Manfred to this repo"
- "download the latest bootstrap", "get manfred-bootstrap", "clone the Manfred template"

## When NOT to use

- The project already has a `starter/`-style scaffold and you only want to add a feature. Use the project's own skills.
- The user is already inside a project stamped from manfred-bootstrap and asks about day-to-day work. Point at `docs/ways-of-working-overview.md` instead.

## Decide the path

Pick ONE based on the user's phrasing:

- **new** - fresh project, needs scaffolding and optionally provisioning.
- **overlay** - existing repo, drop in WoW files non-destructively.
- **download** - clone the template to inspect it; no stamping.

If ambiguous, ask ONE question: "New project, add to this existing repo, or just download the template to look at?"

## Prereqs (verify before running)

Run these and check they succeed:

- `git --version` - any 2.x+.
- `node --version` - Node 20+ (24+ recommended).
- `claude --version` - Claude Code CLI, for the follow-up.
- Only for `new` with `--github`: `gh auth status` - needs an authenticated gh.

If a required binary is missing, print the install hint and STOP:

- git: https://git-scm.com/downloads
- node: https://nodejs.org/
- claude: https://claude.com/claude-code
- gh: https://cli.github.com/

## Path: new (fresh project)

Ask one question at a time for anything the user did not volunteer:

- **Project name** - kebab-case, e.g. `acme-dashboard`. Validate with `/^[a-z][a-z0-9-]+$/`.
- **Linear prefix** - 2-4 uppercase letters. Default `STU` for Studio Manfred internal. Validate with `/^[A-Z]{2,4}$/`.
- **Target directory** - default `./<name>`.
- **Provisioning** - one yes/no each: "Create a GitHub repo?", "Create a Vercel project?", "Create a Linear team?" Defaults: all no. If yes to Linear, ask for the Linear team key (default: the prefix).

Compose the command:

```
curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-bootstrap/main/install.sh \
  | bash -s -- new \
  --name <name> \
  --prefix <prefix> \
  --dir <dir> \
  [--github] [--vercel] [--linear --linear-team <team>] \
  --yes
```

Show the full command to the user before running. Run it with `--yes` so the subcommands do not prompt interactively.

After it exits:

1. `cd <dir>` into the stamped project.
2. Tell the user: "Open `<dir>` in Claude Code - I'll be there for the first task."
3. Suggest they read `docs/ways-of-working-overview.md` and `docs/superpowers-workflow.md`.

## Path: overlay (existing repo)

Confirm the user is in the target repo root (`pwd` matches the repo's working tree). If not, ask them to `cd` first.

Ask: "What's the Linear team prefix for this project?" There is no sensible default. Do not guess `STU` for client-owned repos.

Compose:

```
curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-bootstrap/main/install.sh \
  | bash -s -- overlay \
  --dir . \
  --prefix <prefix>
```

Tell the user: overlay is non-destructive. Existing files are never overwritten. Review the diff after it finishes.

## Path: download (inspect only)

Ask: "Where should I clone the template? (default `./manfred-bootstrap`)"

Run:

```
git clone --depth 1 https://github.com/Studio-Manfred/manfred-bootstrap.git <dir>
```

Then say: "Cloned. Open `<dir>/docs/using-this-repo.md` for the tour, or run `node <dir>/scripts/bootstrap.mjs --help` for CLI options."

## Rails

- Never silently commit anything on the user's behalf.
- Never pass `--github`, `--vercel` or `--linear` without the user explicitly saying yes.
- If the install.sh command exits non-zero, print the actual error (do not paraphrase) and ask the user how to proceed.

## Links

- Site: https://manfred-bootstrap-site.vercel.app
- Repo: https://github.com/Studio-Manfred/manfred-bootstrap
- Linear tickets: STU-1035 (shipped), STU-1037, STU-1038, STU-1039
