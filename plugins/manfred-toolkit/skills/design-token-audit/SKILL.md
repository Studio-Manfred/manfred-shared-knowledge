---
name: design-token-audit
description: Use when auditing design token usage across a product or codebase — anyone says "design token audit", "token coverage", "are we using tokens", "token consistency check", "design system compliance scan", "find hex literals", "check token adoption", "DS audit". Manfred-flavoured: anchored to `~/.claude/shared/DESIGN.md`'s three-layer architecture (primitives → semantic → shadcn contract); flags + recommends, doesn't auto-fix without consent.
---

# design-token-audit

Tokens get added to a system, then components quietly bypass them. A year in, the design system claims 100% token coverage but production has hex literals, default Tailwind palette colours, and references to tokens that don't exist. The audit catches this.

Manfred audits track three things: what's covered, what's bypassed, what's missing. The output is an actionable report — every finding has a specific token recommendation or a flag for design-system gap.

## Overview

A token audit answers three questions:

1. **Coverage** — what % of visual values use tokens?
2. **Consistency** — are the same tokens used for the same purposes? Any redundant tokens?
3. **Gaps** — what visual values should be tokens but aren't yet?

The audit is run *across both code and Figma* — both surfaces can drift independently. A code-only audit misses the design-side problem; a Figma-only audit misses the implementation problem.

## When to use

- Quarterly health check on a product's token compliance
- Pre-major-release audit (before shipping a v1 or v2)
- Mid-engagement check on a project that's been running a while
- After absorbing a project from another team (legacy codebase)
- Preparing the case for a design system refresh / cleanup
- Setting up the baseline for `manfred-toolkit:design-system-adoption` measurement

**Skip when:**

- The project hasn't been built yet (no surface to audit)
- The user wants to *replace* hardcoded values with tokens (use `manfred-design-systems:tokenize` — different artifact)
- The user wants component-level QA (use `manfred-design-ops:design-qa-checklist`)
- The user wants design system version planning (use `manfred-design-ops:version-control-strategy`)

## Pre-flight

Before scoping:

- **What's the audit scope?** (Whole codebase? One feature? One component family?)
- **Code + Figma, or one?** (Both is best; one is incomplete but useful for a first pass)
- **Token surface available?** (`~/.claude/shared/DESIGN.md` + `tokens.css` + Tailwind config — confirm readable)
- **What's the audit serving?** (Pre-release gate? Quarterly health? Building a refresh case?)
- **Linear ticket?** (For posting findings)

If the user wants an audit but can't name what it serves — push back. "Just tell me how we're doing" produces generic reports. Specific decisions produce useful audits.

## The hard rules

| Rule | What it means |
|---|---|
| **Three layers, audited per layer** | Primitives → semantic → shadcn contract (per `~/.claude/shared/DESIGN.md`). Each layer has different audit criteria — primitive raw hex is allowed (it's the layer); component hex is a violation. |
| **Code + Figma, audited together where possible** | Both surfaces drift. Code-only audit misses design drift; Figma-only audit misses implementation drift. |
| **Findings are actionable** | Every finding pairs with: file:line, current value, recommended token, severity. Generic "tokens need work" is not a finding. |
| **No auto-fix without consent** | The audit *flags*; replacement is a separate decision. Auto-replacing a hex with a token is the `manfred-design-systems:tokenize` skill's job. |
| **Phantom tokens are a finding** | `var(--token-that-doesnt-exist)` resolves to browser fallback (often broken). Flag it; route to `manfred-design-systems:design-token` to add the missing token or pick an existing one. |
| **Severity tagged** | Block-merge / high-priority / cleanup. Don't burn block-merge credibility on minor nits. |
| **Numbers + qualitative pairing** | The percentage tells you the score; the patterns tell you what to fix. Both belong in the report. |

## The flow

### Step 1 — Survey the token surface

```bash
test -f ~/.claude/shared/DESIGN.md && head -200 ~/.claude/shared/DESIGN.md
test -f src/tokens/tokens.css && cat src/tokens/tokens.css
test -f tailwind.config.* && grep -A 50 "theme:" tailwind.config.*
```

This is the constraint — every replacement must resolve to an existing token (or be flagged as needing a new one).

### Step 2 — Inventory visual values (code side)

For each category (color, spacing, typography, radius, shadow, motion):

```bash
# Color
grep -rn "#[0-9a-fA-F]\{3,6\}" src/components/ | grep -v "^.*\.svg" | head -50
grep -rn "\(bg\|text\|border\|ring\|fill\|stroke\)-\(red\|green\|blue\|amber\|yellow\|orange\|slate\|gray\|zinc\|stone\|neutral\)-[0-9]" src/

# Spacing (raw px outside Tailwind)
grep -rnE "(padding|margin|gap):\s*[0-9]+px" src/components/

# Typography (off-scale font sizes)
grep -rnE "font-size:\s*[0-9]+px" src/components/

# Phantom tokens
grep -rn "var(--[a-z-]\+)" src/ | awk -F'var(' '{print $2}' | awk -F')' '{print $1}' | sort -u
```

For each finding, check against `tokens.css` — does the value map to a token? Does the token exist?

### Step 3 — Inventory visual values (Figma side)

If Figma MCP is available (`figma-console`):

- List frames using non-token colour values
- List frames using non-grid spacing
- List components instances vs detached components
- Cross-check against the design system's shipped token set

If Figma MCP isn't available, run the audit on exported screens / Figma docs the designer provides; ask for the most recent design files.

### Step 4 — Categorise findings

Per finding, capture:

- **Where** (file:line for code, frame name for Figma)
- **What** (current value + the violation type)
- **Recommended token** (or "needs new token — see below")
- **Severity** (block-merge | high-priority | cleanup)

| Violation | Severity | Recommended action |
|---|---|---|
| Raw hex in component | High-priority | Replace with semantic token |
| Default Tailwind palette (`bg-green-50`) | High-priority | Replace with semantic token; if no semantic exists, add one (route to `manfred-design-systems:design-token`) |
| Phantom token (`var(--color-success)` not in tokens.css) | Block-merge | Component is silently broken. Add token or replace reference. |
| Brand utility used where semantic should be | Cleanup | Replace with semantic for theme-flip support |
| Off-scale font size / spacing | Cleanup | Map to nearest scale value or flag as gap |
| Inconsistent token usage (same purpose, different tokens) | Cleanup | Standardise on one token; deprecate the other |

### Step 5 — Surface gaps

Beyond violations, surface what *should* exist but doesn't:

- Recurring need for `success` / `warning` / `info` tokens (Manfred palette doesn't ship these — surface as design-system PR candidate)
- Spacing values that recur off-scale (signal that a new scale step is needed)
- Component tokens missing for a heavily-used component

These become inputs to `manfred-design-systems:design-token` work.

### Step 6 — Compute coverage

```
Coverage % = (token-driven values) / (total visual values surveyed) × 100
```

Per category (color, spacing, typography, radius, shadow, motion). A single coverage number across categories hides which areas need work.

### Step 7 — Write the report

Save to `audits/tokens-<scope-slug>-<YYYY-MM-DD>.md`:

```markdown
# Token audit: <scope>

**Date**: YYYY-MM-DD
**Scope**: [files / feature / project]
**Linear ticket**: [STU-XXX or n/a]
**Auditor**: [name]
**Audit covered**: code | figma | both

## Executive summary

- **Coverage**: NN% overall (Color: NN%, Spacing: NN%, Type: NN%, Radius: NN%, Shadow: NN%, Motion: NN%)
- **Block-merge**: N findings
- **High-priority**: N findings
- **Cleanup**: N findings
- **Gaps**: N (tokens that should exist but don't)

## Coverage per category

[Per-category coverage table with details]

## Findings

### Block-merge
[file:line | current | recommended token | reason]

### High-priority
[file:line | current | recommended token | reason]

### Cleanup
[file:line | current | recommended token | reason]

## Gaps — tokens that should exist
- [Recurring need + recommended token name + suggested primitive layer]
- [Recurring need + recommended token name]

## Patterns
[Brief: what's driving the violations? (e.g. "the billing module was built before the system shipped" or "the new variant of Card needed surface tokens that don't exist yet")]

## Recommended next steps
1. [Block-merge fixes — by date]
2. [Tokens to add — design-system PR per `manfred-design-systems:design-token`]
3. [High-priority replacements — backlog with priority]
4. [Cleanup — opportunistic]
```

### Step 8 — Linear update

If a Linear ticket is in scope, post a comment via `mcp__linear-server__save_comment` with:

- Coverage summary
- Block-merge count
- Top 3 patterns
- Path to full report

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We measured coverage at 95% last quarter, we're fine" | 95% measured against an outdated token surface, or measured one category, isn't 95% in current state. Re-audit before claiming. |
| "Hex literals in svg files are fine" | Inside `.svg` source files, yes — those are the literal brand asset. Inside JSX `fill={...}` props or inline CSS, no. |
| "Default Tailwind palette is technically a utility, not a hardcoded value" | It bypasses the token layer. Won't flip in dark mode. Not in your `@theme`. Treat as the same problem as a hex literal. |
| "Auto-fix the violations as part of the audit" | Audit flags; tokenize replaces (`manfred-design-systems:tokenize`). Mixing them produces uncontrolled changes. |
| "Coverage % is a vanity metric" | Coverage % alone is vanity. Coverage % + finding patterns + gap analysis is actionable. |
| "We don't need to audit Figma — devs implement what's spec'd" | Designers drift too. A Figma file with hex literals or off-scale spacing produces dev work that bypasses tokens. |

## Red flags — STOP

- About to compute coverage without a current token surface read
- About to auto-replace findings without explicit consent
- Reporting a single coverage number without per-category breakdown
- Calling something "block-merge" when it's a 1-pixel cleanup
- Auditing only code or only Figma when both are available
- Skipping the gaps section (gaps are often the most actionable finding)
- Producing a report with no recommended next steps

## Manfred lens

Token audits enforce **design principle 8 (use the tokens)** directly. They're also a check on **principle 11 (consistent, not uniform)** — inconsistencies are surfaced as audit findings.

Critical & ethical (principle 6) doesn't apply directly to token audits. But: a system claiming high token coverage when it's not is a form of design dishonesty. Audit honestly.

## Cross-references

- `~/.claude/shared/DESIGN.md` — the token surface being audited against
- `manfred-design-systems:design-token` — for filling identified gaps and resolving phantom tokens
- `manfred-design-systems:tokenize` — for the auto-replace step (separate from this audit)
- `manfred-design-systems:audit-system` (command) — broader compliance audit; this is the token-specific subset
- `manfred-toolkit:design-system-adoption` — coverage feeds adoption metrics
- `manfred-design-ops:version-control-strategy` — gaps and inconsistencies inform versioning decisions

## Tools used

- `Bash` — `grep`, browser dev tools (computed styles)
- `Read` — `~/.claude/shared/DESIGN.md`, `tokens.css`, `tailwind.config`
- `Write` — produce the audit report
- `mcp__linear-server__save_comment` — post summary to ticket
- `mcp__figma-console__*` — for the Figma side of the audit (when available)

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
