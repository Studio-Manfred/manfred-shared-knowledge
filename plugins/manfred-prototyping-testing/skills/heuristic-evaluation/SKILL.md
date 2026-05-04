---
name: heuristic-evaluation
description: Use when conducting an expert review against usability heuristics — anyone says "heuristic evaluation", "Nielsen's heuristics", "expert review", "design audit", "find issues before user testing", "usability inspection", "evaluate against principles". Manfred-flavoured: combines Nielsen's 10 with Manfred's 15 design principles; multi-evaluator (3–5) recommended; produces issues with severity *and* user impact (not just rule citations); cheap usability-risk technique on `manfred-discovery:assumption-test`'s menu.
---

# heuristic-evaluation

Heuristic evaluation is an expert review — designers walk through a product against established principles and flag issues. It's cheap (no users, no infra), quick (hours per evaluator), and finds the obvious-in-hindsight problems before user testing reveals them at higher cost.

It's not a substitute for user testing. It's a **first pass** that frees user testing to find the things experts miss (real workflow friction, mental-model mismatches, AT-specific bugs, edge cases experts don't generate).

Manfred defaults:

- **Two heuristic sets together.** Nielsen's 10 (universal usability) + Manfred's 15 design principles (`shared/design-principles.md`). Both lenses, every time.
- **Multi-evaluator.** One evaluator finds ~30% of issues. Three to five evaluators find 75–85%. Solo heuristic evaluation is half-blind.
- **Severity AND user impact.** A WCAG A violation hitting 0.01% of users ≠ a UX-pattern violation breaking the primary task for 50%. Rate both.
- **Pair with user testing.** Heuristic evaluation finds *what experts notice*. User testing finds *what users actually do*. Different lenses.

## When to use

- Pre-launch directional review before user testing
- Evaluating a competitor / inheriting an existing product
- Quick design audit when budget / timeline excludes user testing
- Before a major redesign — surface what's actually broken vs assumed
- Pairing with `manfred-design-research:usability-test-plan` (heuristic first as cheap pass; user testing for the rest)

**Skip when:**

- The product hasn't been designed yet — heuristic review on wireframes is premature
- The need is "validate the concept" — that's discovery, not heuristics
- Stakeholders need *user voice* specifically — heuristics can't substitute for that

## The hard rules

| Rule | What it means |
|---|---|
| **Use both rule sets** | Nielsen's 10 + Manfred's 15. Each catches what the other misses. |
| **3–5 evaluators** | Solo evaluations find 30%; 3 evaluators find ~60%; 5 evaluators find ~80%. Below 3, the report is unreliable. |
| **Evaluate independently first** | Each evaluator does a full pass alone. Compare findings only after — otherwise groupthink. |
| **Walk real flows** | Pick the real primary user tasks. Edge cases are post-hoc. |
| **Severity AND user impact** | Both ratings, separate. Severity = how bad the bug; user impact = how many / how often / how much it costs them. |
| **Suggest fixes, don't just list problems** | "Heading hierarchy violates principle 11" is half a finding. Pair with the recommended fix. |

## Nielsen's 10 (the universal lens)

| # | Heuristic | What it catches |
|---|---|---|
| 1 | **Visibility of system status** | Users don't know what's happening — silent failure, missing loading state, no confirmation |
| 2 | **Match real world** | Jargon, technical errors, conventions that don't match user mental model |
| 3 | **User control and freedom** | No undo, hard-to-exit modals, "are you sure" prompts, no escape from flows |
| 4 | **Consistency and standards** | Same action looks different across the product; non-standard patterns |
| 5 | **Error prevention** | Could-have-been-prevented errors; no inline validation; destructive actions without confirmation; no auto-save |
| 6 | **Recognition over recall** | User has to remember things between screens; menus that hide common actions |
| 7 | **Flexibility and efficiency** | No shortcuts for power users; one-path-fits-all design |
| 8 | **Aesthetic and minimalist design** | Visual clutter; competing for attention; "every feature on screen at once" |
| 9 | **Error recovery** | Errors fire but don't help — no recovery path, no preserved state, no clear next action |
| 10 | **Help and documentation** | Help is hard to find or assumes the user knows the jargon |

## Manfred's 15 design principles (the Manfred lens)

From `~/.claude/shared/design-principles.md`:

| # | Principle | What it catches |
|---|---|---|
| 1 | **Customer-Driven, Always** | Decisions justified by stakeholder preference / "best practice" without customer evidence |
| 2 | **Research Isn't a Phase** | Build-launch-hope cycle; no continuous touchpoints with customers |
| 3 | **Craft Seriously, Yourself Not So Much** | Either over-precious craft or shrug-shipped output — neither is Manfred |
| 4 | **Warm + Precise** | Marketing-speak, corporate adjectives, hedging, forced levity, "Oops!", or generic-SaaS-friendly tone |
| 5 | **Accessible First** | Contrast failures, missing focus state, keyboard traps, no AT testing — see `manfred-prototyping-testing:accessibility-test-plan` |
| 6 | **Critical & Ethical Design** | Dark patterns, manipulation, missing consent, performative inclusion |
| 7 | **Simple by Default** | Premature complexity, abstractions before warranted, feature creep |
| 8 | **Use the Tokens** | Hardcoded hex / spacing / type — bypassing the token layer; see `manfred-design-systems:design-token` |
| 9 | **Ship Components That Work in the Dark** | Light-mode-only design, unverified dark-mode behaviour |
| 10 | **shadcn Shapes Are the Contract** | Components diverging from shadcn primitives without justification |
| 11 | **Consistent, Not Uniform** | Same patterns implemented differently across screens (different padding, different button shapes, etc.) |
| 12 | **Mobile First, Responsive Always** | Desktop-first design with mobile as afterthought; broken at 320px |
| 13 | **Performance Is a Feature** | Heavy bundles, blocking animations, unoptimised images, slow time-to-interactive |
| 14 | **Design with Data** | Decisions made on hunch where data exists; no measurement plan |
| 15 | **Inclusive Language and Content** | Gendered defaults, ableist metaphors, cultural assumptions, English-only when SV parity matters |

## The flow

### Step 1 — Define scope + recruit evaluators

- **Scope**: which screens / flows? Be specific — "the whole app" is too broad to evaluate well in finite time.
- **Evaluators**: 3–5 people who can hold both rule sets in their head. If the team only has 1–2 senior designers, run solo + ask for an external partner pass.
- **Linear ticket**

### Step 2 — Each evaluator does an independent pass

For each evaluator, three lenses through the same flows:

1. **As a new user** — first-impression, learnability, default paths
2. **As an experienced user** — efficiency, shortcuts, friction in repeat tasks
3. **Per task flow** — concrete real tasks (e.g. "complete signup", "find settings", "recover from a payment failure")

Document each issue inline using the format in Step 4.

### Step 3 — Compare + consolidate

- Each evaluator submits independently
- Compare lists, dedupe, retain unique findings
- Discuss disagreements — sometimes one evaluator caught what others missed; sometimes one is wrong
- Consolidate into a single report

### Step 4 — Issue documentation format

Per finding:

```markdown
## Issue: <short name>

**Heuristic violated**: 
  - Nielsen: <#> <name>
  - Manfred: <#> <name>
  - (or both — issues often hit multiple)

**Location**: <screen / flow / component>

**Description**: <what's broken — concrete, not vague>

**Severity (Manfred scale)**:
  - **0** — Cosmetic, not actually a problem
  - **1** — Minor, low impact
  - **2** — Major, important to fix
  - **3** — Critical, blocks task completion
  - **4** — Catastrophic, ship-blocker

**User impact**:
  - **Frequency**: how often does the user hit this? (per session / once / rare)
  - **Affected segment**: who hits this? (everyone / mobile / new users / AT users / etc.)
  - **Cost to user**: lost time / lost work / abandoned task / safety / financial

**Recommendation**:
  <specific fix — design + implementation pointers; not just "fix it">

**Linear**: <related STU-XXX>

**Owner / target**: <who, by when>
```

### Step 5 — Prioritise

Sort by *user impact* primarily, severity secondarily.

A severity-2 issue that hits every user every session > a severity-3 issue that hits 1% of users monthly. Rank by what the user actually pays.

### Step 6 — Report + handoff

```markdown
# Heuristic evaluation report — <product / scope>

**Date**: YYYY-MM-DD
**Linear**: STU-XXX
**Evaluators**: <names + roles>
**Scope**: <flows + screens>

## Summary
[N issues found across N flows; severity distribution; top 3 themes]

## Critical issues (severity 3+, hits primary task)
[Listed issues with full format]

## Major issues (severity 2)
[Listed]

## Minor issues (severity 1)
[Listed]

## Cosmetic / observational (severity 0)
[Listed for completeness]

## Themes
[Cross-issue patterns — e.g. "consistent failure to honour reduced-motion across the product"]

## Recommended next steps
- Fix list with owners + targets
- Items requiring user testing to validate (route to `manfred-design-research:usability-test-plan`)
- Items requiring discovery (route to `manfred-discovery:opportunity-solution-tree`)

## Cross-plugin handoffs
- `manfred-design-systems:a11y-qa` for principle 5 issues
- `manfred-toolkit:design-token-audit` for principle 8 issues
- `manfred-design-research:usability-test-plan` for issues needing user-side validation
```

### Step 7 — Linear comment

Post via `mcp__linear-server__save_comment` with summary + path to report + critical-issue count.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Nielsen's heuristics are enough." | Nielsen catches universal usability. Manfred's 15 catches Manfred-specific problems (token compliance, dark mode, voice). Both. |
| "I can do it solo — I'm experienced." | Solo finds 30%. Ego is not a substitute for evaluator count. |
| "Heuristic evaluation replaces user testing." | It doesn't. Experts don't generate the workflows users actually take. Pair, don't substitute. |
| "Severity is enough — skip user impact." | Severity tells you how bad the bug; impact tells you how many people pay. Both ratings. |
| "Just list the problems — let dev figure out the fix." | Half a finding. Recommendations are the deliverable, not the bug list. |

## Red flags — STOP

- Solo evaluation with no external check.
- One rule set (Nielsen only or Manfred only).
- No severity or no user impact rating — just "issue exists".
- Findings without recommended fixes.
- Report not handed off to the team that owns the product.
- Heuristic eval positioned as "user testing in lite form" — they're different.

## Manfred lens

**Cagan's 4 risks** — heuristic evaluation primarily retires **usability risk** at very low cost. Some Manfred-15 violations also surface **viability risk** (principle 6 ethics; principle 5 accessibility — legal exposure). Route flagged risks via `manfred-discovery:cagan-risks`.

**Torres OST** — heuristic findings often surface *new opportunities* (recurring frustration patterns become opportunity-tree nodes). Route to `manfred-discovery:opportunity-solution-tree` when patterns recur.

## Cross-references

- `manfred-discovery:assumption-test` — heuristic eval is one technique on the usability-risk menu
- `manfred-design-research:usability-test-plan` — for findings that need user-side validation
- `manfred-design-systems:a11y-qa` + `manfred-design-systems:a11y-design` — for principle 5 issues
- `manfred-toolkit:design-token-audit` — for principle 8 issues
- `manfred-toolkit:ux-writing` — for principle 4 issues (voice + tone)
- `manfred-discovery:opportunity-solution-tree` — when findings reveal recurring opportunity patterns

## Tools used

- `Read` — to inspect production code / design files
- `mcp__linear-server__get_issue` / `save_comment` — for ticket linkage

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, dual-rule-set discipline (Nielsen + Manfred 15), severity-AND-user-impact rule, fix-required rule, and Manfred-specific guidance are original.*
