---
description: Run a heuristic evaluation of an existing design — Nielsen's 10 + Manfred's 15 design principles, with severity AND user impact, multi-evaluator if possible.
argument-hint: [design / screen / flow to evaluate, e.g. "the new checkout flow" or "the settings screen"]
---

You're running a heuristic evaluation. The user mentioned: $ARGUMENTS

This is the orchestrator — it runs `manfred-prototyping-testing:heuristic-evaluation` against both Nielsen's 10 and Manfred's 15, plus pulls in `manfred-prototyping-testing:user-flow-diagram` for flow context and `manfred-prototyping-testing:accessibility-test-plan` for the a11y layer.

## Step 1 — Confirm scope + evaluators

- **Scope** — which screens / flows / surfaces? Be specific. "The whole app" is too broad to evaluate well.
- **Linear ticket** — `STU-XXX`
- **Evaluators** — solo or multi? Solo finds ~30%; 3–5 evaluators find 75–85%. If solo, name it as a limitation.
- **Existing flow doc?** — if there's a `manfred-prototyping-testing:user-flow-diagram` output, reference it; if not, sketch the primary flows first.

## Step 2 — Per-evaluator independent pass (`manfred-prototyping-testing:heuristic-evaluation`)

For each evaluator, three lenses through the same flows:

1. **As a new user** — first impression, learnability, default paths
2. **As an experienced user** — efficiency, shortcuts, friction in repeat tasks
3. **Per task flow** — concrete real tasks (signup, recover password, change settings, etc.)

Both rule sets:

- Nielsen's 10 (universal usability) — see the skill's table
- Manfred's 15 design principles (`shared/design-principles.md`) — see the skill's table

Document each issue in the format from the skill (heuristic violated + severity + user impact + recommendation).

## Step 3 — Flow analysis (`manfred-prototyping-testing:user-flow-diagram`)

Walk the flows for issues that surface only at the flow level:

- Missing decision criteria
- Unmapped error / recovery paths
- Dead ends
- Unbounded flows
- AT-equivalent path gaps

These often hide between heuristic findings.

## Step 4 — Accessibility check (`manfred-prototyping-testing:accessibility-test-plan` + `manfred-design-systems:a11y-qa`)

Even in a heuristic eval, run the a11y layer:

- Layer 1 (axe / Lighthouse) — automated scan
- Layer 2 (manual) — keyboard, zoom, reduced-motion
- Layer 3 (AT walkthrough) — VoiceOver + Safari minimum

Findings here often trigger principle 5 violations in the heuristic report.

## Step 5 — Compare + consolidate

Each evaluator's independent findings → consolidated list:

- Dedupe
- Discuss disagreements
- Note unique catches per evaluator
- Identify themes across issues (e.g. "consistent failure to honour reduced-motion across the product")

## Step 6 — Severity + user impact

For every finding, both ratings:

- **Severity (Manfred scale 0–4)** — how bad the bug
- **User impact** — how often, how many, how much it costs them

Sort by user impact primarily, severity secondarily. A severity-2 issue that hits every user every session > a severity-3 issue that hits 1% of users monthly.

## Step 7 — Recommendations (every issue)

Half a finding is a list of problems. The deliverable is recommendations — specific, designable, implementable fixes.

## Step 8 — Document + hand off

```
docs/heuristic-evals/<scope-slug>-<YYYY-MM-DD>.md
```

Format from the heuristic-evaluation skill (Step 6 of that skill's flow).

Include:

- Evaluators + scope + date
- Issue list by severity, with full format per issue
- Themes across issues
- Cross-plugin handoffs:
  - Principle 5 issues → `manfred-design-systems:a11y-qa`
  - Principle 8 issues → `manfred-toolkit:design-token-audit`
  - Principle 4 issues → `manfred-toolkit:ux-writing`
  - Issues needing user-side validation → `manfred-design-research:usability-test-plan`
  - Patterns suggesting opportunities → `manfred-discovery:opportunity-solution-tree`

## Step 9 — Linear comment

Post via `mcp__linear-server__save_comment`:

- Path to report
- Summary: N issues across N flows; severity distribution; top 3 themes
- Critical-issue count + owners + targets
- Cross-plugin handoffs queued

## Wrap-up checklist

- [ ] Scope + evaluators confirmed
- [ ] Both rule sets covered (Nielsen + Manfred 15)
- [ ] Three lenses per evaluator (new user / experienced / per-task)
- [ ] Flow analysis included
- [ ] a11y layer run
- [ ] Multi-evaluator if possible (or solo flagged as limitation)
- [ ] Severity + user impact per issue
- [ ] Recommendations per issue
- [ ] Cross-plugin handoffs identified
- [ ] Linear comment posted

Then offer:

> "For findings needing user-side validation, run `/manfred-prototyping-testing:test-plan`. For accessibility deep-dive, route to `manfred-design-systems:a11y-qa`. For design-token compliance, run `manfred-toolkit:design-token-audit`."
