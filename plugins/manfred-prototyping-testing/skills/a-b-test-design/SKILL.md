---
name: a-b-test-design
description: Use when designing an A/B / split test — anyone says "let's A/B it", "design an experiment", "split test", "want to test two variants", "what's the sample size", "p-value", "lift / detectable effect", "control vs treatment", "AB test the new CTA". Manfred-flavoured: refuses "let's just A/B it" without a hypothesis; routes back to `manfred-discovery:assumption-test` to confirm A/B is the cheapest test that retires the risk; sample sizing + duration are non-negotiable; pre-commits to the analysis plan before launch.
---

# a-b-test-design

A/B tests are expensive — engineering time, traffic, opportunity cost. They're worth it when the call you're making depends on a directional signal at scale. They're not worth it for things you could've answered with a 5-user moderated test in two days.

Manfred defaults:

- **Hypothesis-first.** No hypothesis, no test. "Let's just A/B it" produces results you can't act on.
- **Sample size + duration calculated before launch.** Not "we'll see how it goes". Power analysis is the cost of admission.
- **Pre-commit to the analysis plan.** What does "win" look like? What does "no-op" look like? What's the guardrail? Decide before you peek.
- **Route through `manfred-discovery:assumption-test` first.** A/B is one technique on the menu — and almost always not the cheapest. If a 5-user moderated test or a click-test would retire the risk in 2 days vs 4 weeks, do that.

## When to use

- You have *significant existing traffic* on the surface to be tested
- You have a clear, single hypothesis (one variable changing)
- The decision genuinely needs a directional signal at scale
- You're past the qualitative phase — A/B answers "by how much", not "why"

**Skip when:**

- The traffic is too small for the minimum detectable effect (insufficient sample within a sensible duration)
- The hypothesis is foundational ("redesign the whole flow") — A/B can't isolate too many variables
- The decision is reversible cheaply — just ship, measure, iterate
- You haven't run qualitative testing first — A/B will tell you what changed, not why
- The change is ethically uncomfortable (withholding an obvious improvement from the control group)

## Pre-flight

Before designing the test, get four answers:

1. **Risk type retired** — value / usability / feasibility / viability. (If usability — moderated test or click-test is almost always cheaper. Re-route via `manfred-discovery:assumption-test`.)
2. **Hypothesis** — strict format: "If we [change], then [primary metric] will [direction] by at least [minimum detectable effect], because [rationale]."
3. **Baseline rate + traffic available** — without these, sample sizing is fiction.
4. **Decision rule** — what we'll do if it wins / loses / no-ops. Pre-committed.

If any answer is "we don't know" — A/B isn't the next step. Go answer that question first.

## The hard rules

| Rule | What it means |
|---|---|
| **One variable per test** | A/B isolates a single change. Two changes at once = uninterpretable result. Use multivariate (factorial) only if you understand the interpretation cost. |
| **Hypothesis with MDE** | Hypothesis must specify a minimum detectable effect. "Will improve" isn't a hypothesis — it's a wish. |
| **Sample size pre-calculated** | Power analysis: baseline rate × MDE × significance (typically 95%) × power (typically 80%). Document the math. |
| **Duration ≥ 1 weekly cycle** | Run in full weeks. Behaviour varies day-to-day; partial weeks distort. Minimum 2 weeks for most consumer flows. |
| **No peeking** | Don't stop the test on positive early results. Sequential testing or alpha-spending if you must monitor. |
| **Guardrails defined** | At least one guardrail metric (e.g. testing checkout improvement: guardrail on cart abandonment, on revenue per session, on accessibility-error rate). |
| **Analysis plan pre-committed** | Write down what you'll do at each outcome before launch. Otherwise post-hoc rationalisation. |

## The flow

### Step 1 — Risk + hypothesis

Run `manfred-discovery:assumption-test` first if you haven't. A/B should appear on the technique menu as the choice — if a cheaper test retires the same risk, do that.

Hypothesis template:

```
If we [change to control], then [primary metric] will [direction] 
by at least [MDE]%, because [rationale grounded in user behaviour, not just opinion].
```

Examples:

- ✅ "If we move the social-proof block above the form, signup completion will increase by at least 3%, because users hesitating on commitment can't see the trust signal in the current layout."
- ❌ "If we change the button colour, conversions will improve."  *(no MDE; rationale is wish-thinking)*
- ❌ "If we redesign the page, things will get better."  *(too many variables; not a single hypothesis)*

### Step 2 — Variants

- **Control (A)**: current production
- **Treatment (B)**: the single change
- Document what stays the same in both
- Document what differs — should be one logical change, even if it spans pixels

If you need 3+ variants, you need a different test design (multivariate / factorial) — the interpretation cost is real, name it.

### Step 3 — Metrics

| Metric type | What it does | Examples |
|---|---|---|
| **Primary** | The single measure of success. Must be sensitive to the change, must be the one you'll act on. | Signup completion rate, click-through rate, revenue per session |
| **Secondary** | Supporting context. Won't drive the decision but informs interpretation. | Time on page, scroll depth, returning-visitor rate |
| **Guardrails** | Things that mustn't get worse. If they regress, the win is overruled. | Cart abandonment, error rate, page load time, a11y violations |

One primary. Three to five secondaries. At least one guardrail.

### Step 4 — Sample size + duration

Calculate using a power analysis tool (Optimizely / Evan's calculator / stats library):

- **Baseline conversion rate**: from real data, last 4–8 weeks
- **Minimum detectable effect (MDE)**: from the hypothesis
- **Significance level**: 95% (α = 0.05)
- **Power**: 80% (β = 0.20)
- **Two-tailed**: usually (you care about regressions too)

Output: required sample per arm.

Then: required sample / (daily traffic × allocation %) = days. Round up to full weeks.

If duration > 6 weeks: rethink. Either MDE is too small (you can't detect that with the traffic you have) or the change isn't worth the elapsed time.

### Step 5 — Pre-commit the analysis plan

```markdown
## Decision rule

- **Primary metric: ≥ +<MDE>% with p < 0.05 AND no guardrail violation** → ship treatment, document, share learnings
- **Primary metric: 0 to +<MDE>% with p < 0.05** → no meaningful win, ship the cheaper-to-maintain version
- **Primary metric: not significant** → no-op confirmed; do not chase by extending duration
- **Primary metric: -X% with p < 0.05** → kill, post-mortem on the hypothesis
- **Any guardrail violation** → kill regardless of primary

## Segmentation analysis (after overall)
- New vs returning users
- Mobile vs desktop
- Locale (EN / SV)
- (Pre-commit which segments — don't go fishing post-hoc)
```

### Step 6 — Document + ship the test

```markdown
# A/B test — <name>

**Linear**: STU-XXX
**Risk retired**: <value / usability / feasibility / viability> via `manfred-discovery:assumption-test`
**Hypothesis**: <full form with MDE>
**Variants**: A (control, current); B (treatment, <description>)
**Allocation**: <e.g. 50/50>
**Primary metric**: <name + measurement>
**Secondaries**: <list>
**Guardrails**: <list with red-line thresholds>
**Sample required**: <per arm>
**Duration**: <weeks>
**Decision rule**: <pre-committed — see template above>
**Segments to analyse**: <pre-committed — list>
**Owner**: <name>
**Start / end dates**: <ISO>
```

### Step 7 — Linear comment

Post via `mcp__linear-server__save_comment`:

- Path to the test design doc
- Hypothesis + MDE + duration
- Link to the assumption-test that justified A/B
- Pre-committed decision rule

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Let's just A/B it and see what happens." | A/B without a hypothesis produces noise that gets read as signal. Design or don't run. |
| "We'll stop early if it's obviously winning." | Early peeks inflate false-positive rates dramatically. Sequential testing (or alpha-spending) or wait. |
| "MDE 0.5% — small but worth it." | If your traffic can't detect 0.5% in a sensible duration, A/B isn't the test. Either ship and measure cohorts, or run qualitative. |
| "Test 5 things at once — we're in a hurry." | Multi-variable tests give multi-variable results — usually unread, often misread. Pick one. |
| "Don't bother with guardrails — we'll spot regressions." | "We'll spot it" = we won't. Pre-define the red lines. |
| "Just gut-check the result, we don't need stats." | Then you didn't need an A/B test — you needed a qualitative test or a directional ship-and-measure. |

## Red flags — STOP

- No pre-committed hypothesis with MDE.
- Sample size not calculated before launch.
- More than one logical change between A and B.
- No guardrail metric defined.
- "We'll decide what to do based on the result" (no decision rule).
- Duration < 1 weekly cycle.
- Traffic insufficient to detect the MDE within 6 weeks.
- Test set up to validate a decision already made (motivated reasoning).

## Manfred lens

**Cagan's 4 risks** — A/B is almost always answering a **value risk** ("does this change move the metric") or a **usability risk** ("does this design land with users"). For usability risk: 5-user moderated test usually beats A/B on cost / speed. For value risk at scale: A/B is the right tool *if* you have the traffic.

**Torres OST** — A/B tests retire one specific assumption-test on the tree. Surface which node when documenting; if the test result invalidates the assumption, the OST node updates.

If the test couples to a meaningful **viability risk** (revenue, churn) — flag explicitly via `manfred-discovery:cagan-risks`.

## Cross-references

- `manfred-discovery:assumption-test` — A/B is one technique on the menu; route here to confirm A/B is the cheapest that retires the risk
- `manfred-discovery:cagan-risks` — for risk-type framing
- `manfred-discovery:opportunity-solution-tree` — to map the test result back to a tree node
- `manfred-prototyping-testing:test-scenario` — for qualitative tests that should run *before* the A/B
- `manfred-prototyping-testing:click-test-plan` — for findability questions cheaper than A/B
- `manfred-prototyping-testing:user-flow-diagram` — to map control + treatment flows
- `manfred-design-systems:a11y-qa` — to verify treatment doesn't introduce a11y regressions (a guardrail)
- `manfred-toolkit:design-token-audit` — for token compliance in the treatment

## Tools used

- `Read` — to inspect existing analytics / baseline data
- `Bash` — to call statistical tooling if available locally
- `mcp__linear-server__get_issue` / `save_comment` — for ticket linkage

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, hypothesis-first discipline, decision-rule pre-commit, route-through-assumption-test rule, and Manfred-specific guidance are original.*
