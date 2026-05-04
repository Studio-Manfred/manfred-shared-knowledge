# manfred-prototyping-testing

Manfred-flavoured prototyping + testing: prototype strategy, click tests, A/B tests, heuristic evaluation, accessibility test plans, test scenarios, user flows, wireframes. Implementation layer for `manfred-discovery:assumption-test`'s cheapest-test menu — every skill here maps fidelity / method to which Cagan risk it retires.

## Skills

| Skill | When it triggers |
|-------|-----------------|
| `a-b-test-design` | "let's A/B it", "design an experiment", "split test", "what's the sample size", "p-value", "AB test the new CTA" — refuses without a hypothesis + MDE; routes through `manfred-discovery:assumption-test`; pre-commits to the analysis plan |
| `accessibility-test-plan` | "a11y test plan", "WCAG audit", "test with screen readers", "AT testing", "test with users with disabilities" — four layers (auto + manual + AT + disabled-user); WCAG 2.2 AA floor; pair with `manfred-design-systems:a11y-qa` for per-PR gate |
| `click-test-plan` | "click test", "first-click test", "five-second test", "Maze test", "where would users click", "findability" — cheap usability-risk technique on `manfred-discovery:assumption-test`'s menu; refuses without a question |
| `heuristic-evaluation` | "heuristic evaluation", "Nielsen's heuristics", "expert review", "design audit", "usability inspection" — Nielsen's 10 + Manfred's 15 design principles together; multi-evaluator (3–5); severity AND user impact |
| `prototype-strategy` | "should I build a high-fidelity prototype", "what fidelity for this", "Figma vs code", "Apple-level polish for the review", "CEO wants polish" — **foundational TDD'd skill**: refuses fidelity-first questions; routes to assumption + risk + decision + audience; (a)/(b)/(c) refusal menu with inline Cagan-risk hypothesis; separates LEARN from SHOW artifacts; "we've already decided" is a red flag, not an exit |
| `test-scenario` | "write test tasks", "test scenarios", "facilitator guide", "task wording" — goal-oriented not UI-oriented; participant's language; one goal per task; pilot before launch |
| `user-flow-diagram` | "user flow", "task flow", "happy path", "decision tree", "branching logic" — happy path first then branches then errors; decision criteria explicit at every diamond; one flow per goal; pair with `manfred-interaction-design:error-handling-ux` for error paths |
| `wireframe-spec` | "wireframe spec", "low-fi", "mid-fi", "annotated wireframe", "layout spec" — greyscale only (no colour decisions yet); content priority numbered; all 5 states (empty / loading / populated / error / partial); responsive breakpoints; spacing in tokens |

## Commands

| Command | What it does |
|---------|--------------|
| `/manfred-prototyping-testing:evaluate` | Run a heuristic evaluation. Nielsen + Manfred 15, with severity + user impact, multi-evaluator, plus flow + a11y layers. |
| `/manfred-prototyping-testing:experiment` | Design an A/B experiment. Hypothesis with MDE → variants → sample sizing → pre-committed decision rule. Routes through `manfred-discovery:assumption-test` to confirm A/B is the cheapest test. |
| `/manfred-prototyping-testing:prototype-plan` | Plan prototyping + testing for an initiative. Assumption-first, fidelity-last; LEARN vs SHOW separated; flows + wireframes + scenarios + a11y + timeline. |
| `/manfred-prototyping-testing:test-plan` | Design a complete usability test plan. Method matched to question shape; scenarios + click tests + a11y; pre-committed analysis plan. |

## Manfred opinions baked in

- **Cheapest test wins** — every skill maps to `manfred-discovery:assumption-test`'s cheapest-test menu. Hi-fi prototypes are last resort, not default.
- **Assumption-first, fidelity-last** — `prototype-strategy` refuses fidelity-first questions; routes to risk + decision + audience first
- **LEARN vs SHOW are different artifacts** — prototype-strategy enforces the split; user-research artifact and stakeholder-show artifact are not the same thing
- **Stakeholder polish ≠ fidelity** — "CEO wants polish" is stakeholder management, not a prototyping decision
- **A/B has hypotheses with MDE** — `a-b-test-design` refuses "let's just A/B it"; sample sizing pre-calculated; decision rule pre-committed
- **Heuristic eval uses both Nielsen + Manfred 15** — coverage neither alone provides
- **Multi-evaluator** — solo heuristic eval finds 30%; 3–5 evaluators find 75–85%
- **Accessibility = four layers** (auto + manual + AT + users-with-disabilities) — automated alone catches 30%; the rest needs the bottom three layers
- **Real users with disabilities, paid fairly** — same rate as any participant
- **Severity AND user impact** — a severity-3 issue affecting 0.01% of users ≠ a severity-2 issue breaking the primary task for everyone
- **Test tasks goal-oriented, not UI-oriented** — "Where would you go to change your email" not "Click the settings icon"
- **Pilot test scenarios** — bad task wording costs more in re-runs than pilots cost
- **Wireframes greyscale; spacing in tokens** — defer colour to visual phase via `manfred-ui-design:design-screen`

## Cross-plugin handoffs

- **Implementation layer for `manfred-discovery:assumption-test`** — this plugin provides techniques for the cheapest-test menu (click test, A/B, heuristic eval, AT testing, prototype-as-test)
- **`prototype-strategy` routes to `manfred-toolkit:presentation-deck`** when the artifact is stakeholder-comms (path (c) of the refusal menu)
- **`prototype-strategy` + `wireframe-spec` feed `manfred-ui-design:design-screen`** — wireframes inform visual design after stabilising
- **Wireframes hand off to `manfred-design-ops:handoff-spec`** for engineering hand-off
- **`heuristic-evaluation` complements `manfred-design-systems:a11y-qa`** — heuristic eval includes principle 5 (accessibility); a11y-qa is the per-PR gate
- **`accessibility-test-plan` plans, `manfred-design-systems:a11y-qa` executes** — the plan defines the gate, the gate runs per-PR
- **Pairs with `manfred-design-research:usability-test-plan`** — moderation craft for the qualitative side
- **Pairs with `manfred-interaction-design:error-handling-ux` + `manfred-interaction-design:state-machine`** — error paths and state modelling for flow diagrams

## Install

```
/plugin marketplace add Studio-Manfred/manfred-shared-knowledge
/plugin install manfred-prototyping-testing@manfred
```
