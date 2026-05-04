---
name: accessibility-test-plan
description: Use when planning accessibility testing for a feature, release, or product — anyone says "a11y test plan", "WCAG audit", "test with screen readers", "accessibility coverage", "AT testing", "test with real users with disabilities", "accessibility test before launch", "WCAG 2.2 AA". Manfred-flavoured: automated tools catch ~30%; AT testing + disabled-user testing are non-negotiable for principle 5; complements `manfred-design-systems:a11y-qa` (this skill plans, that skill executes the gate).
---

# accessibility-test-plan

Accessibility testing is layered. Automated tools catch ~30% of issues — necessary, not sufficient. The other 70% needs keyboard testing, real assistive-technology testing, and (for anything important) testing with people who use AT every day. Manfred design principle 5: accessible first.

Manfred defaults:

- **Automated, manual, AT, and user-with-disability testing — all four layers.** Skipping the bottom three is how you ship inaccessible code that passes the linter.
- **WCAG 2.2 AA is the floor**, not the ceiling.
- **Test early, not at the end.** Accessibility issues found at launch cost 10x what they cost in design.
- **Plans, doesn't execute the per-PR gate.** That's `manfred-design-systems:a11y-qa`. This skill builds the *plan*; that skill *runs* it on a specific change.

## When to use

- Planning the test coverage for a new feature, release, or whole product
- Reviewing existing test coverage for gaps (especially the bottom layers)
- Building a vendor / contractor accessibility-testing brief
- Pairing with `manfred-design-systems:a11y-qa` (per-PR gate execution)

**Skip when:**

- The need is per-PR a11y verification — that's `manfred-design-systems:a11y-qa`
- The need is design-time a11y review (contrast, focus, ARIA pattern selection) — that's `manfred-design-systems:a11y-design`
- The user wants AT-specific bug remediation — that's a debug task, not a planning task

## The four layers (cover all four)

| Layer | What it does | Tools | Catches |
|---|---|---|---|
| **1. Automated** | Lints + axe rules in CI/CD | axe-core, Lighthouse, WAVE, pa11y | ~30% — colour contrast, missing alt, missing labels, basic ARIA misuse |
| **2. Manual** | Human walkthrough | Keyboard only, zoom 200%/400%, prefers-reduced-motion, prefers-contrast | Focus order, focus visibility, keyboard traps, motion triggers, content reflow |
| **3. Assistive technology** | Screen reader / voice / switch testing | VoiceOver (Mac/iOS), NVDA (Windows), TalkBack (Android), Voice Control, Dragon, switch control | AT-specific bugs — wrong announcements, missing landmarks, broken semantics, custom widget failures |
| **4. Real users with disabilities** | Recruited testing with AT users | Moderated, with consent, fairly compensated | Real-world workflow breakage that compliance audits can't catch |

Skipping any layer leaves a class of bugs unfound.

## Pre-flight

Before building the plan:

- **Scope** — single feature / release / whole product?
- **WCAG target** — 2.2 AA (Manfred floor) / AAA / sector-specific (EAA, ADA Title III)?
- **Linear ticket** for the plan (`STU-XXX`)
- **Existing coverage** — what's already in CI? What's been audited externally?
- **Compliance trigger** — internal Manfred standard, EU EAA (June 2025), client requirement?
- **Recruitment realistic?** — for layer 4, have we sourced AT users (Fable, Knowbility, Access Works, internal network)?

## The hard rules

| Rule | What it means |
|---|---|
| **All four layers covered** | Skipping AT or disabled-user testing means shipping bugs only those layers find. |
| **Test in real AT, not simulators** | Accessibility Insights "screen reader" mode is not VoiceOver. Use the real thing. |
| **Cover the four major AT combos** | VoiceOver + Safari, NVDA + Firefox, JAWS + Chrome, TalkBack + Chrome. Different bugs in each. |
| **Test with the user's own setup** | For layer 4, AT users have years of personal config. Don't make them use yours. |
| **Severity ≠ priority** | A WCAG A violation that affects 0.01% of users matters less than a WCAG AA failure that breaks the primary task for 5%. Prioritise by *user impact*, not *compliance level*. |
| **Compensate disabled testers fairly** | Same rate as any other paid research participant. Same. |

## The flow

### Step 1 — Define test matrix

For each key user flow / surface:

| Flow | Layer 1 (auto) | Layer 2 (manual) | Layer 3 (AT) | Layer 4 (users) |
|---|---|---|---|---|
| Sign-up | axe in CI | Keyboard, zoom, motion | VO+Safari, NVDA+FF, TalkBack | 5 AT users |
| Checkout | axe in CI | Keyboard, zoom, motion | VO+Safari, NVDA+FF | 3 AT users |
| Settings | axe in CI | Keyboard, zoom | VO+Safari | (skip — low-impact) |
| ... | ... | ... | ... | ... |

If a row has gaps — that's the plan's gap. Justify or fill.

### Step 2 — WCAG criteria per layer

For each layer, list which WCAG 2.2 AA criteria it covers. Build a coverage matrix — for each criterion, which layer catches it?

Some criteria are layer-specific:

- **Contrast (1.4.3)** — Layer 1
- **Focus visible (2.4.7)** — Layer 1 + 2
- **Focus order (2.4.3)** — Layer 2
- **Bypass blocks (2.4.1)** — Layer 2 + 3
- **Name, role, value (4.1.2)** — Layer 3 (real AT) — automated tools miss real announcement bugs
- **Information from the AT user's experience** — Layer 4 only

If a criterion is only "covered" by Layer 1 — it's not actually covered.

### Step 3 — AT testing specifics

For each AT combo:

```markdown
**VoiceOver + Safari (macOS)**
- Walkthrough: <flow> with rotor, headings nav, form-controls nav
- Specific watch-outs: announcement of dynamic content (`aria-live`), modal focus trapping, custom widget roles
- Tester: <name + assistive-tech proficiency level>
- Time: 1–2 hours per major flow

**NVDA + Firefox (Windows)**
- Walkthrough: <flow> with browse mode, focus mode, list-of-headings (H), list-of-landmarks (D)
- Specific watch-outs: form-mode toggle, virtual cursor, table navigation
- Tester: <name>
- Time: 1–2 hours per major flow

**TalkBack + Chrome (Android)** or **VoiceOver + Safari (iOS)**
- Walkthrough: <flow> with swipe nav, explore-by-touch, rotor (iOS) / reading controls (Android)
- Specific watch-outs: gesture conflicts (see `manfred-interaction-design:gesture-patterns`), touch-target size
- Tester: <name>
- Time: 1–2 hours per major flow
```

### Step 4 — User-with-disability testing (layer 4)

| Decision | Recommended Manfred default |
|---|---|
| **N participants** | 5 per primary AT category (screen reader / motor / low vision / cognitive). Diminishing returns past 5 per category for qualitative findings. |
| **Recruitment** | Fable, Knowbility, AccessWorks, Disability Visibility Project (US); EnabledLove (EU); internal network or specialised recruiters. Avoid scraping disability forums — that's extractive. |
| **Compensation** | Same hourly rate as any other paid research participant. ≥ €100 / hour, payment in time, no payment in "exposure". |
| **Format** | Moderated (most signal), 60–90 min, real tasks, real product. Their device + AT setup. |
| **Consent + safety** | Recording consent explicit; flag scope of "what we'll do with insights"; offer to use a pseudonym; allow stopping any time without forfeiting compensation. |
| **Reporting back** | Share findings + planned remediation + timeline back to the participants. They invested time — close the loop. |

This is paired user-research work. Coordinate with `manfred-design-research:usability-test-plan` for moderation craft.

### Step 5 — Issue documentation format

For every finding (any layer), document:

```markdown
## Issue: <short name>

**Layer found**: 1 / 2 / 3 / 4
**WCAG criterion**: <e.g. 1.3.1 Info and Relationships, level A>
**AT affected**: <VoiceOver / NVDA / keyboard-only / etc>
**User impact**: <description — what breaks, for whom, in what situation>
**Severity (Manfred scale)**:
  - **0** — Cosmetic, no actual user impact
  - **1** — Inconvenient but workable
  - **2** — Blocks task with workaround available
  - **3** — Blocks task, no workaround
  - **4** — Catastrophic / safety / legal
**Steps to reproduce**: <verbatim>
**Recommendation**: <design + dev fix>
**Owner / target fix**: <who, by when>
**Related Linear**: STU-XXX
```

### Step 6 — Prioritise by user impact

Sort issues by:

1. Severity (3+4 first)
2. Frequency (how many AT users hit it)
3. WCAG level (AA before AAA — but compliance level is the *floor*, not the priority)

Don't sort purely by WCAG level. A WCAG A issue affecting one edge case ≠ a WCAG AAA enhancement on a primary path.

### Step 7 — Plan the cadence

Accessibility testing is not a launch gate — it's continuous:

- **Per PR**: Layer 1 (axe) automatic via CI. `manfred-design-systems:a11y-qa` for any UI-touching PR.
- **Per release**: Layer 2 + Layer 3 manual walkthrough on changed flows.
- **Per major release**: Layer 4 user testing.
- **Annual**: Full external audit (especially if EAA / ADA-relevant).

Codify the cadence in the plan.

### Step 8 — Linear comment

Post via `mcp__linear-server__save_comment`:

- Path to the plan doc
- Test matrix summary
- Cadence
- Recruitment status for layer 4
- Outstanding gaps + decisions

## Output format

```markdown
# Accessibility test plan — <scope>

**Date**: YYYY-MM-DD
**Linear**: STU-XXX
**WCAG target**: 2.2 AA
**Compliance trigger**: <internal / EAA / client>

## Scope
[Flows + surfaces in scope; out-of-scope explicit]

## Test matrix
[Table from Step 1]

## WCAG coverage matrix
[For each criterion, which layers cover it]

## AT walkthrough briefs
[Per AT combo from Step 3]

## User-with-disability testing
[Recruitment + compensation + consent + format from Step 4]

## Issue documentation template
[Format from Step 5]

## Prioritisation rules
[Step 6]

## Cadence
[Step 7]

## Outstanding gaps
[Anything the plan can't cover yet — recruitment, tool, budget]

## Cross-plugin handoffs
- `manfred-design-systems:a11y-qa` for per-PR gate
- `manfred-design-systems:a11y-design` for design-time decisions
- `manfred-design-research:usability-test-plan` for layer 4 moderation
```

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Axe passes — we're accessible." | Axe catches 30%. The other 70% lives in screen-reader announcements, focus management, gesture alternatives, real workflow friction. |
| "We'll add AT testing in v2." | "v2" rarely happens. AT bugs found later cost 10x. |
| "Screen-reader simulators are close enough." | They're not. Use real VO / NVDA / TalkBack. The bugs are in the real announcement engine, not the simulation. |
| "We can't find AT users to test with." | Fable / Knowbility / AccessWorks exist. The barrier is willingness to budget, not findability. |
| "We'll save money by paying participants in product credits." | No. Same paid rate as any other participant. Otherwise this plugin's first principle (accessible first) is performative. |
| "WCAG AAA — we'll go for the gold." | AA first, fully. AAA for specific criteria where it serves the user (e.g. enhanced contrast for vision-affected primary persona). Going AAA across the board often reduces usability for everyone else. |

## Red flags — STOP

- Plan covers only Layer 1.
- AT testing in simulators only.
- Layer 4 missing for a high-impact / high-traffic feature.
- Compensation < market rate for participants.
- Issues prioritised purely by WCAG level (ignoring user impact).
- Plan exists but cadence is "before launch" — that's too late.

## Manfred lens

Maps to **principle 5 (accessible first)** and **principle 15 (inclusive language and content)** from `~/.claude/shared/design-principles.md`.

**Cagan's 4 risks** — accessibility violations are a **viability risk** (legal exposure: EAA, ADA Title III, sectoral regs) AND a **value risk** (15–20% of users excluded). For features in regulated sectors or public services: route to `manfred-discovery:cagan-risks` to make the risk explicit.

## Cross-references

- `manfred-design-systems:a11y-qa` — per-PR execution of the gate this plan defines
- `manfred-design-systems:a11y-design` — design-time decisions (contrast, focus, ARIA pattern)
- `manfred-design-research:usability-test-plan` — moderation craft for layer 4
- `manfred-interaction-design:gesture-patterns` — non-gesture alternatives are a layer-3 finding hotspot
- `manfred-interaction-design:animation-principles` — `prefers-reduced-motion` is a layer-2 finding hotspot
- `manfred-discovery:cagan-risks` — for viability + value framing on accessibility scope decisions

## Tools used

- `axe-core`, `Lighthouse`, `WAVE`, `pa11y` — Layer 1
- VoiceOver, NVDA, JAWS, TalkBack — Layer 3
- `mcp__linear-server__get_issue` / `save_comment` — for ticket linkage

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, four-layer-coverage rule, real-AT-not-simulators discipline, fair-compensation rule, principle-5 mapping, and Manfred-specific guidance are original.*
