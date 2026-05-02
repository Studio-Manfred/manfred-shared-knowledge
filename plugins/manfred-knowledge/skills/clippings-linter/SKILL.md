---
name: clippings-linter
description: Use whenever the user wants to lint, audit, health-check, clean up, or find problems in their Obsidian Clippings folder. Triggers on "lint my clippings", "audit clippings", "check obsidian vault health", "clean up clippings", "find broken notes", "missing tags", "duplicate notes", "orphan notes", "vault hygiene". Always prefer this skill over generic file-search when the user mentions cleaning or quality-checking their knowledge base.
---

# Clippings Linter

Scan the Obsidian `Clippings/` folder for structural, content, and graph-level issues, then apply safe auto-fixes and produce a markdown report for everything that needs human judgement.

## When to use

- User says "lint my clippings", "audit", "clean up", or "check vault health"
- User mentions missing tags, empty notes, duplicate files, or orphan pages
- User asks which clippings need attention, or wants a report of broken stuff
- User is preparing a maintenance pass on their Obsidian knowledge base

**When not to use:**
- Tagging only — use the tagging skill instead
- Scraping URLs into empty notes — use the scraping skill
- Linting other folders in the vault (Daily Notes, MacWhisper, etc.) — different schema, different rules

## Why this matters

A knowledge base that grows past ~1,000 files develops drift you can't see: missing frontmatter fields, orphan notes, tag vocabulary inconsistencies, duplicates from bulk imports, topics mentioned so often they deserve their own page. Left unchecked, drift makes the vault harder to search, link, and trust. Linting catches drift while it's still cheap to fix.

## What this skill does

This is a **v1** skill focused on fast, deterministic checks plus light graph analysis. It does not use an LLM at runtime — it runs a Python script, applies safe auto-fixes, and writes a markdown report. Semantic checks (contradictions, stale claims) are planned for v2/v3.

### Checks performed

**Frontmatter (auto-fixable)**
- Missing required fields: `title`, `url`, `source`, `created`, `tags`, `read_status`
- Malformed URLs (unquoted, obviously broken)

**Content (flag only)**
- Empty or stub body (<50 chars of actual prose)
- Files with only placeholder tags (`to-categorize`)
- Files with no tags

**Filenames (flag only)**
- Duplicate pairs (` 1`, ` 2` suffixes indicating re-imports)
- Generic names (`Untitled`, `Untitled 1`)
- URL-encoded characters (`%20`, `%3A`)
- Very long or truncated-looking names ending mid-word

**Graph (flag only)**
- **Orphans:** files with no outgoing `related:` links AND never referenced from any `[[wiki-link]]` in another file
- **Article candidates:** capitalized noun phrases appearing in ≥N files that don't have their own page — gaps in coverage

### v2: Semantic checks (opt-in, LLM-powered)

v2 adds two checks that can't be done deterministically:

- **Contradictions** — files in the same tag cluster making claims that disagree (e.g. two UX sources citing different conversion numbers for the same thing)
- **Stale claims** — claims anchored to old dates or phrases like "currently", "recently", "the latest" that may have been superseded

These are opt-in because they are slower and cost real money (LLM + web-search calls). Run them on demand, not as part of the default lint.

### What this skill deliberately does NOT do

- **URL liveness checking** — slow, flaky, rate-limits; we rely on the existing `scrape_errors.md` instead
- **Tag vocabulary repair** — belongs to the tagging skill

## Workflow

### Step 1: Confirm scope

Default target: `/Users/jens.wedin/Sandbox/Obsidian/Clippings`. Confirm with the user if they want a different path. Ask whether auto-fix should run or if they want report-only first.

### Step 2: Run the linter

The bundled script at `scripts/lint.py` does all the work. Run it from the skill directory:

```bash
python3 scripts/lint.py \
  --path "/Users/jens.wedin/Sandbox/Obsidian/Clippings" \
  --auto-fix \
  --report "/Users/jens.wedin/Sandbox/Obsidian/Clippings/lint_report.md"
```

Flags:
- `--path PATH` — folder to lint (required)
- `--auto-fix` — apply safe auto-fixes in place (missing frontmatter defaults, URL quoting); omit for report-only
- `--report PATH` — output report file (default: `<path>/lint_report.md`)
- `--candidates-threshold N` — min occurrences for a term to be an article candidate (default 5)

The script prints a short summary to stdout and writes the full report to the file. Do not try to re-implement any of this in Python inline — use the script.

### Step 3: Show the summary

The script's stdout output shows totals per issue class and a count of auto-fixes applied. Relay that to the user in 5-10 lines. Do not read the full report into your context — instead, tell the user it's been written to `lint_report.md` and let them open it in Obsidian.

### Step 4: v2 semantic checks (only when user asks)

When the user asks to run contradiction or stale-claim detection, use the bundled `extract_claims.py` pre-processor and then dispatch subagents for the LLM work.

**Step 4a — preprocess.** Run:

```bash
python3 scripts/extract_claims.py \
  --path "/Users/jens.wedin/Sandbox/Obsidian/Clippings" \
  --out /tmp/v2_worklist.json
```

This writes a JSON worklist with (a) the top 5 tag clusters, each with up to 100 files and their top-ranked claim candidates, and (b) up to 50 stale-claim candidates ranked by earliest-mentioned year. The script is deterministic, fast, and makes no network calls.

**Step 4b — dispatch contradiction agents.** For each tag cluster in the worklist, dispatch a subagent with this brief:

> You are auditing the `<tag>` cluster of a personal Obsidian knowledge base for contradictions. Read the claims array for each file in the cluster (from `/tmp/v2_worklist.json`). Look for pairs or groups of claims across different files that disagree on the same specific topic — e.g. different percentages for the same metric, opposed advice on the same situation, conflicting historical timelines. For each candidate contradiction, read the relevant file bodies (from `/Users/jens.wedin/Sandbox/Obsidian/Clippings/<file>`) to verify it's a real disagreement, not just loose wording. Report findings as markdown to `/Users/jens.wedin/Sandbox/Obsidian/Clippings/contradictions.md`, one entry per contradiction: the claim, the sources (as `[[wiki-link]]`s), and a one-sentence note on what to investigate. Be conservative — no false positives. Return a short count-only summary.

Run clusters sequentially unless the user says otherwise. One agent per cluster — cost is roughly $0.20-0.50 per cluster depending on size.

**Step 4c — dispatch stale-claim agents.** For the `stale_candidates` list in the worklist, dispatch a single subagent with Firecrawl access:

> For each candidate in `/tmp/v2_worklist.json` under `stale_candidates`, use firecrawl `search` to check whether the claim is still accurate in light of the current date. Flag claims as `stale` (newer evidence contradicts it), `outdated` (still true but framed as "new/recent" when it's years old), or `still_valid`. Report to `/Users/jens.wedin/Sandbox/Obsidian/Clippings/stale_claims.md` with the claim, source file, verdict, and a one-line citation. Batch search calls sensibly and respect rate limits. Return a short summary.

**Step 4d — show the user.** After agents finish, tell the user the report files are ready and suggest opening them in Obsidian. Do NOT paste the report contents into the main conversation.

### Step 5: Handle proposed fixes interactively

For each class of proposed (non-auto) fix — duplicates, filename junk, orphans, article candidates — the report groups issues together. If the user asks "apply the duplicate cleanups", offer to delete the newer-suffixed file of each pair after confirming one by one (or in bulk if they explicitly say "yes to all"). Never delete files without an explicit go-ahead.

## Report structure

The report is a single markdown file grouped by severity so the user can triage top-down. Structure:

```markdown
# Clippings lint report — YYYY-MM-DD HH:MM

**Scanned:** N files
**Auto-fixes applied:** M
**Issues requiring review:** K

## Summary

| Check | Count | Severity |
|---|---|---|
| ... | | |

## 🔴 Errors

(issues that break the vault's structure — missing required fields, malformed URLs)

## 🟡 Warnings

(issues worth fixing — empty bodies, placeholder tags, duplicates)

## 🔵 Suggestions

(judgement calls — orphans, article candidates, filename cleanup)

## Auto-fixes applied

(list of what the script changed in place)
```

Each issue line links to the offending file using `[[wiki-link]]` syntax so the report is navigable in Obsidian.

## Design principles

- **Safe by default.** Only trivially-safe changes run on `--auto-fix`. Everything else goes to the report.
- **Deterministic.** Same input → same output. No LLM at runtime in v1.
- **Fast.** Should scan 1,500 files in under 10 seconds.
- **Idempotent.** Running twice without new files → identical report, zero new auto-fixes.
- **No external dependencies.** Python stdlib only, so the script runs on any machine with Python 3.

## Notes on the target vault

The Clippings folder has these known conventions (the script assumes them):
- Frontmatter is YAML between `---` fences
- Tags block uses `tags:\n  - kebab-case\n` format
- Wiki-links are `[[filename without .md]]`
- `related:` is a frontmatter array of wiki-links

If these conventions change, update the parsing logic in `lint.py` — not in this SKILL.md.
