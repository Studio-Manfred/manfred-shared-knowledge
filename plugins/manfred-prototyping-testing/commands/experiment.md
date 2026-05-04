---
description: Design an A/B experiment for a design hypothesis — chains hypothesis-with-MDE + variants + sample sizing + duration + analysis-plan-pre-commit + decision-rule.
argument-hint: [hypothesis or design change to test, e.g. "new checkout flow will reduce abandonment by 5%" or "moving social proof above the form will increase signup completion"]
---

You're designing an A/B experiment. The user mentioned: $ARGUMENTS

This is the orchestrator — it runs `manfred-prototyping-testing:a-b-test-design` for the rigour, plus pulls in `manfred-prototyping-testing:user-flow-diagram` for variant-flow mapping and routes through `manfred-discovery:assumption-test` to confirm A/B is the cheapest test that retires the risk.

## Step 1 — Pre-flight (do not skip)

`manfred-prototyping-testing:a-b-test-design` opens with four required answers. Get them now or hold the rest of this command:

1. **Risk type retired** — value / usability / feasibility / viability. (For usability: a 5-user moderated test or click-test is almost always cheaper. Re-route via `manfred-discovery:assumption-test` before committing to A/B.)
2. **Hypothesis** — strict format: "If we [change], then [primary metric] will [direction] by at least [MDE]%, because [rationale grounded in user behaviour]."
3. **Baseline + traffic** — without these, sample sizing is fiction.
4. **Decision rule** — what we'll do at each outcome. Pre-committed.

If any answer is "we don't know" — A/B isn't the next step. Go answer that question first via `manfred-discovery:assumption-test`.

## Step 2 — Confirm A/B is the right tool (`manfred-discovery:assumption-test`)

A/B is one technique on the cheapest-test menu. Run through:

- **Sufficient traffic?** — without it, the MDE you can detect is too large to be meaningful within a sensible duration
- **Single hypothesis?** — A/B isolates one variable; multi-variable changes need a different design
- **Past the qualitative phase?** — A/B tells you "by how much"; you need to already know "why" or "what"
- **Decision genuinely needs a directional signal at scale?** — many decisions don't; a 5-user moderated test costs less and answers richer questions

If any check fails — A/B isn't the right tool. Route to the cheaper / better-fitted technique on the menu.

## Step 3 — Hypothesis (`manfred-prototyping-testing:a-b-test-design`)

Strict format with MDE:

```
If we [change to control], then [primary metric] will [direction] 
by at least [MDE]%, because [rationale grounded in user behaviour, not opinion].
```

Examples:

- ✅ "If we move the social-proof block above the form, signup completion will increase by at least 3%, because users hesitating on commitment can't see the trust signal in the current layout."
- ❌ "If we change the button colour, conversions will improve." *(no MDE; rationale is wish-thinking)*
- ❌ "If we redesign the page, things will get better." *(too many variables)*

## Step 4 — Variants

- **Control (A)**: current production
- **Treatment (B)**: the single change
- Document what stays the same in both
- Document what differs — single logical change

If 3+ variants are needed: this is a multivariate / factorial test, not A/B. Name it.

## Step 5 — Variant flows (`manfred-prototyping-testing:user-flow-diagram`)

Map the flow for control and treatment side-by-side. Surface:

- Decision points that differ
- Error / recovery paths in each variant
- Any other flows the variant change affects (the change might cascade)

## Step 6 — Metrics

| Type | Pick |
|---|---|
| **Primary** | One. The decision-driver. Sensitive to the change. |
| **Secondary** | 3–5. Context. Don't drive the call. |
| **Guardrails** | At least one. Things that mustn't get worse. |

Common guardrails: cart abandonment, error rate, a11y violations (per `manfred-design-systems:a11y-qa`), revenue per session, page load time.

## Step 7 — Sample size + duration

Power analysis (Optimizely / Evan's calculator / stats library):

- Baseline conversion rate from real data, last 4–8 weeks
- MDE from hypothesis
- Significance: 95% (α = 0.05)
- Power: 80% (β = 0.20)
- Two-tailed (you care about regressions)

Duration = required sample / (daily traffic × allocation %), rounded up to full weeks. Minimum 2 weeks for most consumer flows.

If duration > 6 weeks — rethink. Either MDE is too small for the traffic, or the change isn't worth the elapsed time.

## Step 8 — Pre-commit the analysis plan

Per the format in `manfred-prototyping-testing:a-b-test-design` Step 5:

- Decision rule for each outcome (win / no-op / loss / guardrail violation)
- Pre-committed segmentation (don't go fishing post-hoc)

Write it down before launch. Otherwise post-hoc rationalisation.

## Step 9 — Document

Save to:

```
docs/experiments/<test-slug>-<YYYY-MM-DD>.md
```

Format per `manfred-prototyping-testing:a-b-test-design` Step 6.

Include:

- Risk retired + assumption-test pointer
- Hypothesis with MDE
- Variants (control + treatment)
- Variant flows (link to `manfred-prototyping-testing:user-flow-diagram` output)
- Metrics (primary / secondaries / guardrails)
- Sample + duration with the math
- Pre-committed decision rule
- Pre-committed segmentation
- Owner + dates
- a11y guardrail check (`manfred-design-systems:a11y-qa`)

## Step 10 — Linear comment

Post via `mcp__linear-server__save_comment`:

- Path to design doc
- Hypothesis + MDE + duration
- Link to assumption-test that justified A/B
- Decision rule pre-commit
- Cross-plugin handoffs:
  - a11y guardrail: `manfred-design-systems:a11y-qa`
  - Token compliance for the treatment: `manfred-toolkit:design-token-audit`

## Wrap-up checklist

- [ ] Pre-flight four answers in hand
- [ ] A/B confirmed as cheapest test (or re-routed)
- [ ] Hypothesis with MDE
- [ ] Single variable in the variant
- [ ] Sample + duration calculated
- [ ] Primary + secondaries + ≥ 1 guardrail
- [ ] Decision rule pre-committed (in writing, before launch)
- [ ] Variant flows mapped
- [ ] Linear comment posted

Then offer:

> "Pair with qualitative testing via `/manfred-prototyping-testing:test-plan` to capture the *why* alongside the A/B's *what*. After ship: post-mortem the decision regardless of outcome — share learnings via `manfred-toolkit:design-rationale`."
