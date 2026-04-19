---
name: a11y-qa
description: >
  Use when asked to run an accessibility audit, test for WCAG compliance, check a11y,
  scan for accessibility issues, generate an accessibility report, or when the user
  says "audit a11y", "a11y-qa", "accessibility-qa", "test accessibility", "check WCAG",
  "axe-core scan", "jsx-a11y lint", or "find accessibility violations". Also activate
  when the user is preparing for a release, running pre-merge checks, or mentions
  "audit", "compliance", or "before we ship".
---

# Accessibility QA Testing

Systematically find, classify, and report accessibility violations so developers can fix them.

---

## When to Use

- User wants a formal accessibility audit or compliance report
- Pre-release, pre-merge, or staging QA checks
- User says "audit", "scan", "check WCAG compliance", "find violations"

**When NOT to use:**
- Writing or fixing accessible code → use `a11y-dev`
- Reviewing designs/mockups before handoff → use `a11y-design`
- No code or running app available (design-only stage)

## Step 1: Choose a Scan Mode

Ask the user which mode to use if not specified:

| Mode | What it does | When to use |
|------|-------------|-------------|
| **runtime** | Injects axe-core into running pages via browser | Final QA, staging, before release |
| **static** | Runs eslint-plugin-jsx-a11y on source code | During development, PR review |
| **full** | Static first, then runtime | Comprehensive release audit |

Default to **runtime** unless the user specifies otherwise or no dev server is available.

---

## Step 2: Runtime Scan (axe-core)

Tests the live rendered page — catches issues that only appear at runtime (dynamic content, third-party components, CSS-driven visibility).

**Standards:** WCAG 2.2 Level AA (`wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, `wcag22aa`) + best practices.

### 2a. Discover pages to scan

Look for routes in the project:
- **Next.js (App Router):** `src/app/**/page.tsx`
- **Next.js (Pages Router):** `pages/**/*.tsx`
- **React Router:** route definitions file
- **Static site:** `*.html` files or `sitemap.xml`
- Ask the user if the route list is unclear.

### 2b. Start the dev server

Detect the right command from `package.json` scripts (usually `dev`, `start`, or `serve`). Wait for HTTP 200 on `localhost` before proceeding.

### 2c. Inject axe-core and scan each page

For each page, navigate via browser automation, wait 2–3 seconds for content to render, then execute `scripts/axe-scan.js`. Wait 3 seconds, then retrieve `window.__axeResults`.

### 2d. Kill the dev server

After all pages are scanned, stop the background server process.

---

## Step 3: Static Analysis (ESLint jsx-a11y)

Catches source-level issues in JSX/TSX without a running server.

Check for `eslint-plugin-jsx-a11y` in `package.json`. If not present, install it. Create a temporary standalone config and run the scan.

Full config, usage, and false-positive guidance → `references/eslint-config.md`

---

## Step 4: Classify Violations by Severity

Every axe-core violation carries an impact level:

| Impact | Meaning | Action |
|--------|---------|--------|
| **critical** | Completely blocks assistive technology users | Fix before release |
| **serious** | Causes significant difficulty for AT users | Fix before release |
| **moderate** | Causes some difficulty, workarounds exist | Fix in current sprint |
| **minor** | Small issue, low impact | Fix when convenient |

---

## Step 5: Auto-Fix Reference

Violation-to-fix lookup table → `references/auto-fix.md`

---

## Step 6: Generate the Report

Use the structured report template → `references/report-template.md`

Include: scan mode, standards, date, per-page summary table, each violation with rule-id/impact/WCAG criterion/example element/fix/reference URL, and prioritised next steps.

---

## Step 7: Manual Test Checklist

Automated tools find ~30–40% of accessibility issues. Complete the manual checklist after the automated scan → `references/manual-checklist.md`

Covers: keyboard navigation, screen reader testing, visual/cognitive checks, touch/mobile.

---

## Step 8: WCAG 2.2 AA Quick Reference

Full success-criteria table → `references/wcag-quick-ref.md`

Key thresholds: **4.5:1** text contrast, **3:1** non-text/UI, **24×24 px** minimum target size, usable at **400% zoom**.

---

## Examples

**Example 1 — Runtime audit before release**
Input: "run an accessibility audit on my app"
Output: Discover routes, start dev server, inject axe-core per page, classify violations by impact, generate structured report with prioritised next steps.

**Example 2 — Static scan during PR review**
Input: "check accessibility in my components before I merge"
Output: Install jsx-a11y if absent, create temp config, scan source, report violations with file/line references, filter false positives.

---

## Troubleshooting

**Dev server won't start** — Check `package.json` scripts for the right command. For monorepos, confirm you're in the correct package directory.

**axe-core CDN blocked** — A strict CSP blocks the CDN injection silently. Switch to static mode, or install axe-core locally and serve from `localhost`.

**ESLint scan produces no output** — Verify the glob in `eslint.a11y.mjs` matches your file structure. Adjust `files` pattern if source is outside `src/`.

**axe-core `incomplete` results** — Means axe could not automatically pass or fail (common with colour contrast on dynamic content). Treat as manual review candidates.

---

## Common Mistakes

- **Relying only on automated scans** — axe-core finds ~30-40% of issues. Always complete the manual checklist after automated scans.
- **Skipping runtime scan** — Static analysis misses issues from dynamic content, CSS-driven visibility, and third-party components. Use runtime mode for final QA.
- **Treating "incomplete" results as passes** — axe-core "incomplete" means it couldn't determine pass/fail automatically. These need manual review.
- **Not killing the dev server** — Always stop the background server process after scanning completes.
- **Ignoring "minor" violations** — Minor issues compound. Include them in the report even if they're lower priority.

## Standards Reference

- [WCAG 2.2 Guidelines](https://www.w3.org/TR/WCAG22/)
- [axe-core Rules](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md)
- [jsx-a11y Rules](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y#supported-rules)
