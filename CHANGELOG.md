# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.20.0] — 2026-05-04

### Added
- **`manfred-interaction-design` plugin** — Manfred-flavoured interaction design mirroring `Owl-Listener/designer-skills/interaction-design` (MIT) with Manfred opinions baked in. **7 skills + 3 commands**:
  - **Adapted (6):** `animation-principles`, `feedback-patterns`, `gesture-patterns`, `loading-states`, `micro-interaction-spec`, `state-machine`. Each carries an attribution footer per `docs/manfred-skill-template.md` rule 8.
  - **Foundational + TDD'd (1):** `error-handling-ux` — Manfred-original. Built via the full RED → GREEN → REFACTOR loop. RED baseline scored 1/8 on the rubric — agent took "quick is fine, blocking release" at face value, generated drop-in copy + React state without naming the failure mode (collapsed all timeout sub-modes — 504 / network drop / server overload / abort — into one generic "timed out"), wrote the copy directly instead of routing to `manfred-toolkit:ux-writing`, asserted "your changes haven't been lost" as fact without verifying, skipped motion / focus / reduced-motion / ARIA entirely, and missed the prevention layer (no client timeout, idempotency, optimistic UI mention). GREEN closed all 10 failure-mode gaps with: four mandatory pre-flight answers (failure mode + surface + recovery + user state), explicit (a)/(b)/(c) refusal menu when context missing, surface → recovery rules table (inline / toast / page / banner / modal mapped to recovery shapes), failure-mode → recovery defaults table (10 HTTP / network modes mapped to specific recovery paths), state-preservation non-negotiables (form values always survive, multi-step progress always survives), auto-retry policy with idempotency-key requirement (never auto-retry non-idempotent mutations without keys; 502/503/504/network-drop only with exponential backoff), focus management on error appearance (move focus to error or first invalid field), reduced-motion fallback for error animations, ARIA `role="alert"` vs `status` per mode, structured copy-handoff template that routes to `manfred-toolkit:ux-writing` (skill refuses to write copy directly — that's the failure mode this skill exists to prevent). REFACTOR scored 9/4/10 across three pressure-test scenarios; surfaced three patches: (1) closed the "Skip when: user wants the copy" loophole (a literal agent could deflect copy-only requests to `manfred-toolkit:ux-writing` without pre-flight — now requires the four answers first, even when only copy was requested), (2) added rationaliser trigger phrases to the description (`"just give me the error copy"`, `"keep it casual"`, `"Oops!"`, `"Something went wrong"`, `"we can iterate later"`) so the skill activates on the rationaliser path it would've missed, plus a new Common rationalisations row covering the iterate-later excuse, (3) hardened the (c) placeholder escape — used to be "flag as follow-up", now requires three concrete artifacts (Linear ticket titled `Replace placeholder error copy — <feature>`, code-level `// TODO(STU-XXX)` marker at the call site, worst-case design that gets state preservation + focus + ARIA + reduced-motion right) before (c) is on the table at all.
  - **Commands (3):** `/manfred-interaction-design:design-interaction` (chains state-machine → micro-interactions → animation → gestures → feedback → error → loading), `/manfred-interaction-design:error-flow` (inventories failure modes → prevention → state model → recovery → copy handoff), `/manfred-interaction-design:map-states` (models states + transitions → loading + error + feedback + animation per state, verifies impossible states unreachable).

### Manfred opinions enforced across the plugin

- **Errors explain, don't blame** — `error-handling-ux` enforces `shared/manfred-brand.md` rule (what happened / what to do / one clear action; user is never the subject of failure)
- **Copy lives in `manfred-toolkit:ux-writing`** — interaction skills design *flow*; words live in the toolkit. Generic "Something went wrong" is the failure mode this plugin exists to prevent
- **Reduced motion is non-negotiable** (WCAG 2.3.3) — every animated skill mandates `prefers-reduced-motion: reduce` fallback
- **Sustainability in the small** (principle 13) — motion / loading skills note CPU / battery / bundle cost
- **Tokens, not raw values** — durations / easings reference `manfred-design-systems:design-token`; flag inline values as token leaks
- **Undo > confirmation** — `feedback-patterns` defaults to undo; confirmation reserved for genuinely-irreversible actions
- **Platform conventions first** — `gesture-patterns` follows iOS / Android HIG; custom gestures need a stated reason
- **State preservation non-negotiable** — `error-handling-ux` requires form values, multi-step progress, scroll position to survive errors
- **Discriminated unions over boolean soup** — `state-machine` enforces (state with `{status, ...context}` shape; not `{isLoading, isError, isSuccess, data?, error?}`)

### Cross-plugin handoffs (codified)

- **Routes copy to `manfred-toolkit:ux-writing`** — error messages, loading copy, toast text, button labels — the words are always written there with structured context from here
- **Built on `manfred-design-systems:design-token`** — duration / easing / motion tokens
- **Pairs with `manfred-design-systems:a11y-design` + `manfred-design-systems:a11y-qa`** — ARIA patterns, focus management, reduced-motion, keyboard equivalents
- **Built on `manfred-ui-design`** — visual surface for the interaction lives there
- **Feeds `manfred-design-ops:handoff-spec`** — interaction specs become engineering handoffs
- **Surfaces `manfred-discovery:cagan-risks`** — when error UX or interaction friction is on a critical revenue / retention path

### Changed
- `.claude-plugin/marketplace.json` metadata bumped to `v0.10.0`. `manfred-interaction-design` registered as the 13th plugin.
- `README.md` — added `manfred-interaction-design` to install commands and plugin table.

### Attribution
- 6 adapted skills carry attribution footers per `docs/manfred-skill-template.md` rule 8.
- `error-handling-ux` is Manfred-original; the mirror's `error-handling-ux` provided structural inspiration only — four-pre-flight discipline, copy-routing-to-ux-writing rule, surface → recovery rules table, failure-mode → recovery defaults, state-preservation non-negotiables, auto-retry-with-idempotency policy, and the (a)/(b)/(c) refusal menu are Manfred-specific.

### Roadmap
- Linear ticket [STU-65](https://linear.app/studio-manfred/issue/STU-65) → Done. Next: [STU-66](https://linear.app/studio-manfred/issue/STU-66) (next mirror plugin per the v1.0.0 plan).

## [0.19.0] — 2026-05-04

### Added
- **`manfred-ui-design` plugin** — Manfred-flavoured UI design mirroring `Owl-Listener/designer-skills/ui-design` (MIT) with Manfred opinions baked in. **9 skills + 4 commands**:
  - **Adapted (8):** `dark-mode-design`, `data-visualization`, `illustration-style`, `layout-grid`, `responsive-design`, `spacing-system`, `typography-scale`, `visual-hierarchy`. Each carries an attribution footer per `docs/manfred-skill-template.md` rule 8.
  - **Foundational + TDD'd (1):** `color-system` — Manfred-original. Built via the full RED → GREEN → REFACTOR loop. RED baseline scored 0/10 — agent generated 12+ raw hex values, ignored Manfred's six-colour palette entirely, invented success/warning/error/info as if they were standard, accepted "modern and trustworthy, quick is fine, due Friday" without pushback, never distinguished literal brand utilities from semantic tokens, gave wrong dark-mode advice (told to flip literal brand colours). GREEN closed all 10 failure-mode gaps with: pre-flight requirement to read `~/.claude/shared/DESIGN.md`, hard-rule against hex generation (route to existing six-colour palette), refusal-and-redirect (a)/(b)/(c) menu when semantic doesn't exist (add to design system / reuse existing semantic / status by icon + copy + neutral surface), three-layer architecture enforcement (primitives → semantic → shadcn contract), explicit literal-vs-semantic distinction (`bg-business-blue` literal, `bg-primary` semantic), dark-mode rules (semantic flips automatically; brand utilities stay literal; pair with absolute foregrounds), warm-background rhythm enforcement (avoid gray-on-gray; reach for `bg-beige` before any gray). REFACTOR scored 10/10; surfaced three patches: harden path (a) of the (a)/(b)/(c) menu (require Linear ticket + contrast verification before hex lands, not just "30–60 min"), drop `bg-accent` for "soft positive emphasis" from path (b) (overloads `human-pink`'s "moment of care" semantic), add explicit rationalisation row covering brand-utilities-as-meaning-carriers ("I'll use `bg-human-pink` to mean positive insight" — collapses the brand-decoration vs meaning-carrying layers; the rot the three-layer architecture exists to prevent).
  - **Commands (4):** `/manfred-ui-design:color-palette`, `/manfred-ui-design:design-screen`, `/manfred-ui-design:responsive-audit`, `/manfred-ui-design:type-system`.

### Manfred opinions enforced across the plugin

- **Tokens from `~/.claude/shared/DESIGN.md`** — every visual output references the token layer; no hex generation
- **Three-layer architecture** — primitives → semantic → shadcn contract; brand utilities don't flip, semantic tokens do
- **Host Grotesk for UI; Guttery for logotype only** — typography skills enforce
- **Warm-background rhythm** — `light-beige` canvas alternates with `white` or `beige` cards; avoid gray-on-gray (per Manfred brand guidelines)
- **Flat first, depth is earned** — no heavy shadows, gradients, neumorphism unless functional
- **Mobile first** (principle 12) — design for 320px first; expand
- **Dark mode day-one** (principle 9) — use semantic tokens; dark mode is free
- **Performance is a feature** (principle 13) — typography, illustration, viz skills note bundle / font-loading impact
- **One primary action per view** — visual hierarchy reinforces user intent

### Boundary clarification (`color-system` vs `manfred-design-systems:design-token`)

Both skills enforce the token surface. They serve different units of work:

- **`manfred-design-systems:design-token`** — component-level ("give me CSS for this Card") — already shipped in v0.15
- **`manfred-ui-design:color-system`** — palette / page / surface-level ("colour palette for our new feature page") — shipped here

Same refusal pattern, different unit. Cross-reference between them is mandatory.

### Changed
- `.claude-plugin/marketplace.json` metadata bumped to `v0.9.0`. `manfred-ui-design` registered as the 12th plugin (first in list — closest to v1.0.0 final ordering).
- `README.md` — added `manfred-ui-design` to install commands and plugin table.

### Attribution
- 8 adapted skills carry attribution footers per `docs/manfred-skill-template.md` rule 8.
- `color-system` is Manfred-original; the mirror's `color-system` provided structural inspiration only — voice, refusal logic, three-layer enforcement, warm-background rhythm, and the (a)/(b)/(c) menu are Manfred-specific.

### Roadmap
- Linear ticket [STU-64](https://linear.app/studio-manfred/issue/STU-64) → Done. Next: [STU-65](https://linear.app/studio-manfred/issue/STU-65) (next mirror plugin per the v1.0.0 plan).

## [0.18.0] — 2026-05-03

### Added
- **`manfred-toolkit` plugin** — Manfred-flavoured designer toolkit mirroring `Owl-Listener/designer-skills/designer-toolkit` (MIT) with Manfred opinions baked in, plus absorbing the LinkedIn trio from `manfred-writing`. **9 skills + 3 commands**:
  - **Adapted (5):** `case-study`, `design-rationale`, `design-system-adoption`, `design-token-audit`, `presentation-deck`. Each carries an attribution footer per `docs/manfred-skill-template.md` rule 8.
  - **Foundational + TDD'd (1):** `ux-writing` — Manfred-original. Built via the full RED → GREEN → REFACTOR loop. RED baseline scored 3/10 — agent used "Oops!", "Hmm,", exclamation stacking ("You're in!"), generic-SaaS-friendly tics, never asked about voice doc, accepted "quick is fine, friendly and on-brand" without context, produced copy that could ship for any signup flow. GREEN closed all 7 failure-mode gaps with: pre-flight requirement to read `~/.claude/shared/manfred-brand.md`, anti-patterns lint (refuses "Oops!", "Hmm,", "Yikes!", "Welcome aboard!", marketing verbs, corporate adjectives, exclamation stacking), errors-explain-don't-blame structure (what happened / what to do / one clear action — user is never the subject of failure), context-required for error copy (refuses generic "something went wrong" — demands real failure mode), CTA rules (specific verb + outcome, not "Submit"/"OK"), the quick-test (read aloud — would I cringe?). REFACTOR scored 9/9; surfaced two patches: replace productivity-deck framing ("5 min of clarification saves 30 min of revision") with the sharper craft argument ("generic copy isn't faster — it's permanent"), and add an explicit rationalisation row covering the engineering-deadline pressure with two faster paths (paste failure modes from code, or ship honest "TODO: copy" placeholders).
  - **Absorbed (3):** `linkedin-reflect`, `linkedin-show-and-tell`, `linkedin-teach` — relocated from `manfred-writing`. Identical content; the versions in `manfred-writing` carry deprecation headers pointing here.
  - **Commands (3):** `/manfred-toolkit:build-presentation`, `/manfred-toolkit:write-case-study`, `/manfred-toolkit:write-rationale`.

### Manfred opinions enforced across the plugin

- **Voice rules from `manfred-brand.md`** — anti-marketing-verb list (transform, empower, leverage, unlock, supercharge, drive, deliver value), anti-corporate-adjective list (cutting-edge, world-class, innovative, best-in-class, passionate), fragments OK, direct second person, concrete over abstract
- **Errors explain, don't blame** — `ux-writing` enforces structure (what happened / what to do / one clear action); user is never the subject of failure
- **CTAs specific verbs with outcomes** — "Get in touch" not "Submit"; "Save changes" not "Save"
- **Quick test** — could I read this aloud without cringing? Run on every output before shipping
- **Customer evidence floor** — case studies, rationales, presentations cite specifically
- **Trade-offs named** — case studies + rationales surface what was given up; without trade-offs, both are propaganda

### Changed
- `.claude-plugin/marketplace.json` metadata bumped to `v0.8.0`. `manfred-toolkit` registered as the 11th plugin (first in list — closest to v1.0.0 final ordering). `manfred-writing` description updated to flag partial deprecation.
- `manfred-writing/README.md` — full rewrite to reflect partial-deprecation status (linkedin trio + transcript-anonymizer deprecated; only `meeting-summary` active).
- `plugins/manfred-writing/skills/linkedin-reflect/SKILL.md` — deprecation header pointing to `manfred-toolkit:linkedin-reflect`.
- `plugins/manfred-writing/skills/linkedin-show-and-tell/SKILL.md` — deprecation header pointing to `manfred-toolkit:linkedin-show-and-tell`.
- `plugins/manfred-writing/skills/linkedin-teach/SKILL.md` — deprecation header pointing to `manfred-toolkit:linkedin-teach`.
- `README.md` — added `manfred-toolkit` to install commands and plugin table; updated `manfred-writing` row to reflect deprecation status.

### Transitional
- LinkedIn trio lives in BOTH `manfred-writing` and `manfred-toolkit` during v0.18.x. Identical content. `manfred-writing` is removed in v1.0.0 once `meeting-summary` finds a v1.0.0 home (Linear ticket [STU-67](https://linear.app/studio-manfred/issue/STU-67) tracks the v1.0.0 cleanup; `meeting-summary` home decision is unresolved).
- `manfred-writing` remains installable for `meeting-summary` users; the deprecation is partial, not full.

### Attribution
- 5 adapted skills (`case-study`, `design-rationale`, `design-system-adoption`, `design-token-audit`, `presentation-deck`) carry attribution footers per `docs/manfred-skill-template.md` rule 8.
- `ux-writing` is Manfred-original; the mirror's `ux-writing` provided structural inspiration only — voice-doc enforcement, anti-patterns lint, errors-explain-don't-blame structure, context-required-for-errors discipline, and CTA rules are Manfred-specific.
- 3 absorbed LinkedIn skills are Manfred-original (no attribution change needed; they were Manfred-authored when they lived in `manfred-writing`).

### Roadmap
- Linear ticket [STU-63](https://linear.app/studio-manfred/issue/STU-63) → Done. Next: [STU-64](https://linear.app/studio-manfred/issue/STU-64) (next mirror plugin per the v1.0.0 plan).

## [0.17.0] — 2026-05-03

### Added
- **`manfred-design-ops` plugin** — Manfred-flavoured design ops mirroring `Owl-Listener/designer-skills/design-ops` (MIT) with Manfred opinions baked in. **7 skills + 3 commands**:
  - **Adapted (6):** `design-critique`, `design-qa-checklist`, `design-review-process`, `design-sprint-plan`, `team-workflow`, `version-control-strategy`. Each carries an attribution footer per `docs/manfred-skill-template.md` rule 8.
  - **Foundational + TDD'd (1):** `handoff-spec` — Manfred-original. Built via the full RED → GREEN → REFACTOR loop. RED baseline scored 0/8 — agent dumped a kitchen-sink spec with hex literals, raw px values, custom components from scratch, no Linear posting, no walk-through ritual, accessibility as footnote, never read `~/.claude/shared/DESIGN.md`. GREEN closed all 8 gaps with: pre-flight reads (DESIGN.md + Linear ticket via MCP), token-first enforcement (no hex, no raw px, no phantom tokens, no default Tailwind palette), reference-existing-components rule, refusal of "dump everything" with hard 300-word cap, mandatory Linear posting via `mcp__linear-server__save_comment` when ticket linked, walk-through scheduling required, accessibility as first-class section. REFACTOR scored 9.5/10; surfaced three patches: hard-gate the 300-word cap (was soft target), tighten the no-Linear-ticket fallback (was silent escape hatch — now requires user choice between push-for-ticket / confirm-internal-only / draft-pending-ticket), tighten Manfred Lens voice slip ("doesn't apply directly. But:" → direct statement).
  - **Commands (3):** `/manfred-design-ops:handoff` (pre-handoff review → token check → spec → Linear post → walk-through), `/manfred-design-ops:plan-sprint` (challenge framing → Day-0 checklist → 5-day schedule → recruit → test plan → follow-up), `/manfred-design-ops:setup-workflow` (5-component workflow setup, scaled to team size, documented in 2+ visible places).

### Manfred opinions enforced across the plugin

- **Trio attends cross-functional rituals** — PM + designer + tech lead at design reviews, critiques, retros, planning; not designer-solo
- **Design system is source of truth** — handoffs reference tokens not screenshots; QA verifies token compliance not memory
- **Linear is the delivery channel** — handoffs, design reviews, QA findings, sprint summaries all post via `mcp__linear-server__save_comment`
- **Async-first, sync earned** — most "quick syncs" should be Linear comments + Loom; sync for tension resolution, not coordination
- **Accessibility hard gate at every review** (design principle 5; WCAG 2.2 AA non-negotiable) — runtime gate via `manfred-design-systems:a11y-qa`
- **Handoff specs tight** — ~300-word hard cap on intent + decisions + open questions; Figma is the measurement source, not the spec doc
- **Kitchen-sink specs refused** — completeness theatre is worse than a tight spec engineering reads end-to-end

### Changed
- `.claude-plugin/marketplace.json` metadata bumped to `v0.7.0`. `manfred-design-ops` registered as the 10th plugin (first in list — closest to v1.0.0 final ordering).
- `README.md` — added `manfred-design-ops` to the install commands and plugin table.

### Note
- v0.16.0 CHANGELOG mentioned "Next: STU-62 manfred-ui-design" — that was incorrect. STU-62 is `manfred-design-ops` (this release). `manfred-ui-design` is a later ticket. Linear is the source of truth for ticket → plugin mapping.

### Attribution
- 6 adapted skills carry attribution footers per `docs/manfred-skill-template.md` rule 8.
- `handoff-spec` is Manfred-original; the mirror's version provided structural inspiration only — the Linear MCP integration, the hard 300-word cap, the existing-component reference rule, and the walk-through scheduling are Manfred-specific.

### Roadmap
- Linear ticket [STU-62](https://linear.app/studio-manfred/issue/STU-62) → Done. Next: [STU-63](https://linear.app/studio-manfred/issue/STU-63) (next mirror plugin per the v1.0.0 plan).

## [0.16.0] — 2026-05-03

### Added
- **`manfred-ux-strategy` plugin** — Manfred-flavoured UX strategy work mirroring `Owl-Listener/designer-skills/ux-strategy` (MIT) with Manfred opinions baked in. **8 skills + 3 commands**:
  - **Adapted (6):** `competitive-analysis`, `design-brief`, `experience-map`, `metrics-definition`, `opportunity-framework`, `stakeholder-alignment`. Each carries an attribution footer per `docs/manfred-skill-template.md` rule 8.
  - **Fresh (1):** `north-star-vision` — Manfred-original. Customer-driven floor, "what we give up" non-optional, scenarios as narratives not bullet points, ethics test against principle 6. The mirror's `north-star-vision` provided structural inspiration only — voice, refusal logic, trade-off enforcement are Manfred-specific.
  - **Foundational + TDD'd (1):** `design-principles` — built via the full RED → GREEN → REFACTOR loop. RED baseline scored ~1/7 — agent invented 5 cold-start fintech principles without checking Manfred's canonical 15, accepted "quick is fine, meeting tomorrow" without pushback, skipped prioritisation, mixed in aspirational mush ("delight the user"). GREEN closed those gaps with: pre-flight requirement to read `~/.claude/shared/design-principles.md`, refusal of cold-start posters, (a)/(b)/(c) menu (adapt canonical 15 / meeting prep kit / starter set with workshop date), testable + trade-off-stated requirement per principle, customer-driven + ethics floors as non-negotiable. REFACTOR scored 6/6; surfaced two patches: required side-by-side canonical-vs-adapted check in Scenario D (stops "adapting" from becoming "quietly inventing"), and explicit guardrail that workshop-date is mandatory for the starter-set escape hatch.
  - **Commands (3):** `/manfred-ux-strategy:benchmark` (competitive-analysis → experience-map → opportunity-framework), `/manfred-ux-strategy:frame-problem` (design-brief end-to-end), `/manfred-ux-strategy:strategize` (full strategy: principles → vision → competitive → opportunities → metrics → stakeholders).

### Manfred opinions enforced across the plugin

- **Customer-driven floor** (design principle 1) — every skill cites or flags evidence; "we believe…" gets surfaced as assumption
- **Outcomes over outputs** — success criteria measure user/business changes, not feature lists; opportunities phrased as outcomes ("reduce abandonment 38%→15%") not outputs ("build a progress indicator")
- **Warm + precise voice** — anti-pattern check against marketing verbs (transform, empower, leverage, supercharge, unlock, drive value)
- **Critical & ethical** (design principle 6) — every strategy/brief includes "what does this design do in the world?" + harm check; non-negotiable
- **Triangulation over single-framework certainty** — opportunity-framework runs impact-effort + RICE; disagreements become first-class outputs
- **Trade-offs stated** — visions name what they give up; principles name their trade-off partner; opportunities have stated confidence

### Changed
- `.claude-plugin/marketplace.json` metadata bumped to `v0.6.0`. `manfred-ux-strategy` registered as the 9th plugin (first in list — closest to v1.0.0 final ordering).
- `README.md` — added `manfred-ux-strategy` to the install commands and plugin table.

### Attribution
- 6 adapted skills (`competitive-analysis`, `design-brief`, `experience-map`, `metrics-definition`, `opportunity-framework`, `stakeholder-alignment`) carry attribution footers per `docs/manfred-skill-template.md` rule 8.
- `design-principles` and `north-star-vision` are Manfred-original; the mirror's versions provided structural inspiration only — voice, refusal logic, Manfred-15 anchoring, and trade-off enforcement are Manfred-specific.

### Roadmap
- Linear ticket [STU-61](https://linear.app/studio-manfred/issue/STU-61) → Done. Next: [STU-62 manfred-ui-design](https://linear.app/studio-manfred/issue/STU-62).

## [0.15.0] — 2026-05-03

### Added
- **`manfred-design-systems` plugin** — Manfred-flavoured design systems work mirroring `Owl-Listener/designer-skills/design-systems` (MIT) with Manfred opinions baked in. **10 skills + 3 commands**:
  - **Adapted (6):** `component-spec`, `documentation-template`, `icon-system`, `naming-convention`, `pattern-library`, `theming-system`. Each carries an attribution footer per `docs/manfred-skill-template.md` rule 8. (The mirror's `accessibility-audit` was skipped per Linear ticket [STU-60](https://linear.app/studio-manfred/issue/STU-60) — `a11y-qa` already covers the runtime gate.)
  - **Foundational + TDD'd (1):** `design-token` — built via the full RED → GREEN → REFACTOR loop. RED baseline scored 0/7 — agent hardcoded six hex literals, used Tailwind's default palette, ignored dark mode, and accepted "I'm in a hurry" without pushback. GREEN added: pre-flight requirement to read `~/.claude/shared/DESIGN.md`, hard rules against raw hex / default Tailwind palette / phantom tokens, the (a)/(b)/(c) refusal menu when a semantic doesn't exist (add token / reuse semantic / neutral + icon). REFACTOR pressure-test scored 6/6; surfaced two patches: time-cost annotation on option (a) so users don't read it as "blocked indefinitely" (added "(15–30 min, not blocked indefinitely)") and an explicit rationalisation row covering the `var(--token-that-doesnt-exist)` reframe.
  - **Absorbed (3):** `a11y-design`, `a11y-dev`, `a11y-qa` — relocated from `manfred-a11y`. Cross-references inside the skills updated to fully-qualified `manfred-design-systems:` form per template rule 6. `manfred-a11y` carries a deprecation note pointing here; both ship in v0.15.x and `manfred-a11y` is removed in v1.0.0.
  - **Commands (3):** `/manfred-design-systems:audit-system` (project-wide compliance scan), `/manfred-design-systems:create-component` (spec → tokens → impl → docs → a11y gate), `/manfred-design-systems:tokenize` (replace hardcoded values with semantic tokens).

### Manfred opinions enforced across the plugin

- **Tokens from `~/.claude/shared/DESIGN.md`** — three-layer architecture (primitives → semantic → shadcn contract). No raw hex, no default Tailwind palette, no inventing missing semantics.
- **Business-blue + human-pink + warm neutrals** — Manfred's palette doesn't ship `success`/`warning`/`info`. The skill refuses to invent and offers (a)/(b)/(c).
- **WCAG 2.2 AA baseline** (design principle 5) — every component / pattern skill checks this floor.
- **shadcn shapes are the contract** (design principle 10) — component specs mirror stock shadcn API where one exists.
- **Dark mode day-one** (`~/.claude/shared/DESIGN.md` Section 9) — semantic tokens flip automatically; brand utilities stay literal; pair literal-brand surfaces with absolute foregrounds.

### Changed
- `.claude-plugin/marketplace.json` metadata bumped to `v0.5.0`. `manfred-design-systems` registered as the 8th plugin (first in list — closest to v1.0.0 final ordering).
- `manfred-a11y` description prefixed with **DEPRECATED** in marketplace.json — skills moved to `manfred-design-systems`; plugin removed in v1.0.0.
- `plugins/manfred-dev/skills/test-my-code/SKILL.md` — cross-reference updated from bare `a11y-qa` to fully-qualified `manfred-design-systems:a11y-qa` (gate 7 + Tools-used section).
- `plugins/manfred-dev/skills/release/SKILL.md` — three references updated from `superpowers:a11y-qa` (typo from earlier era) and bare `a11y-qa` to `manfred-design-systems:a11y-qa` (prerequisites, gate 5, Cross-references section).
- `plugins/manfred-dev/README.md` — Cross-plugin dependencies section now points at `manfred-design-systems`; legacy migration note included.
- `README.md` — added `manfred-design-systems` to the install commands and plugin table; flagged `manfred-a11y` as deprecated.

### Transitional
- `a11y-design`, `a11y-dev`, `a11y-qa` live in BOTH `manfred-a11y` and `manfred-design-systems` during v0.15.x. Identical content. `manfred-a11y` is removed in v1.0.0 (Linear ticket [STU-67](https://linear.app/studio-manfred/issue/STU-67)).
- Users with `manfred-a11y` installed should also install `manfred-design-systems` so `manfred-dev` cross-references resolve. After verifying the new plugin works, `manfred-a11y` can be uninstalled.

### Attribution
- 6 adapted skills (`component-spec`, `documentation-template`, `icon-system`, `naming-convention`, `pattern-library`, `theming-system`) carry attribution footers per `docs/manfred-skill-template.md` rule 8.
- `design-token` is Manfred-original; the source mirror's `design-token` provided structural inspiration only (categories, tier names) — voice, refusal logic, three-layer-architecture enforcement, and the (a)/(b)/(c) menu are Manfred-specific.
- Three absorbed a11y skills are Manfred-original (no attribution change needed; they were Manfred-authored when they lived in `manfred-a11y`).

### Roadmap
- Linear ticket [STU-60](https://linear.app/studio-manfred/issue/STU-60) → Done. Next: [STU-61 manfred-ux-strategy](https://linear.app/studio-manfred/issue/STU-61).

## [0.14.0] — 2026-04-30

### Added
- **`manfred-design-research` plugin** — Manfred-flavoured user research mirroring `Owl-Listener/designer-skills/design-research` (MIT) with Manfred opinions baked in. **11 skills + 4 commands**:
  - **Adapted (9):** `summarize-interview`, `affinity-diagram`, `card-sort-analysis`, `diary-study-plan`, `empathy-map`, `jobs-to-be-done`, `usability-test-plan`, `journey-map`. Each carries an attribution footer per `docs/manfred-skill-template.md` rule 8.
  - **Fresh (1):** `user-archetype` — Manfred-original. Chosen over "user persona" to sidestep the projection / bias / fabrication failure modes common in persona work. No invented names, photos, or biographical detail; behavioural attributes only.
  - **Foundational + TDD'd (1):** `interview-script` — built via the full RED → GREEN → REFACTOR loop. RED baseline showed the typical agent writes hypothetical-future questions, blurs discovery and usability, and skips Trio attendance / recording / compensation. GREEN closed those gaps. REFACTOR pressure-test surfaced 3 patches: tighten Phase 1 escape hatch (require user pushback before the TBD escape), tighten Phase 2 "Both" combine path (require pushback before the escape hatch), and add a 24-hour-timeline rationalization row ("session is tomorrow, I'll sort logistics in the morning" → reschedule).
  - **Absorbed (1):** `transcript-anonymizer` — relocated from `manfred-writing`. Identical content; the version in `manfred-writing` carries a deprecation note pointing here.
  - **Commands (4):** `/manfred-design-research:discover`, `/manfred-design-research:interview`, `/manfred-design-research:synthesize`, `/manfred-design-research:test-plan` — orchestrators using fully-qualified skill references per template rule 6.

### Manfred opinions enforced across the plugin

- **Research isn't a phase** (design principle 2) — every skill ties back to continuous discovery cadence
- **Trio attendance** — interview / usability skills enforce PM + designer + tech lead, not solo research
- **Story-based interviewing** (Torres) — refuses leading + hypothetical questions
- **Pay people for their time** — recruit guidance includes incentives
- **Accessible first** (design principle 5) — recruit + test design include disabled / AT users; no skill leaves accessibility as a follow-up

### Changed
- `.claude-plugin/marketplace.json` metadata bumped to `v0.4.0`. `manfred-design-research` registered as the 7th plugin.
- `README.md` — added `manfred-design-research` to the install commands and plugin table; flagged `manfred-writing:transcript-anonymizer` as deprecated.
- `plugins/manfred-writing/skills/transcript-anonymizer/SKILL.md` — added deprecation note pointing to the new home.

### Transitional
- `transcript-anonymizer` lives in BOTH `manfred-writing` and `manfred-design-research` during v0.14.x. Identical content. The `manfred-writing` version is removed in v1.0.0 (Linear ticket [STU-67](https://linear.app/studio-manfred/issue/STU-67)).
- Existing `manfred-writing:meeting-summary` was *not* moved — per Linear ticket [STU-59](https://linear.app/studio-manfred/issue/STU-59) edits, that skill is destined for a different plugin (TBD) rather than `manfred-design-research`.

### Attribution
- 9 adapted skills carry attribution footers per `docs/manfred-skill-template.md` rule 8.
- `user-archetype` is Manfred-original; structurally inspired by `user-persona` in `Owl-Listener/designer-skills` but reframed end-to-end.

### Roadmap
- Linear ticket [STU-59](https://linear.app/studio-manfred/issue/STU-59) → Done. Next: [STU-60 manfred-design-systems](https://linear.app/studio-manfred/issue/STU-60).

## [0.13.0] — 2026-04-30

### Added
- **`manfred-discovery` plugin** — Manfred-flavoured product discovery synthesising Marty Cagan's four product risks and Teresa Torres's continuous discovery + opportunity-solution trees. 7 skills + 3 commands:
  - Skills: `cagan-risks`, `opportunity-solution-tree`, `assumption-test`, `customer-touchpoint-plan`, `product-brief`, `discovery-readout`, `discovery-rituals`
  - Commands: `/manfred-discovery:kickoff`, `/manfred-discovery:weekly`, `/manfred-discovery:risk-check`
  - `discovery-readout` integrates with Linear via `mcp__linear-server__save_comment` (pattern from `manfred-dev:test-my-code`)
  - `cagan-risks` built via the full TDD-for-skills loop in `superpowers:writing-skills` (RED baseline → GREEN → REFACTOR with three rationalization patches)
- **`docs/manfred-skill-template.md`** — codified Manfred SKILL.md conventions: voice rules, Cagan/Torres lens guidance, Manfred-outputs checklist, TDD-for-skills pointer, attribution rules. Reference for all subsequent Manfred plugins.

### Changed
- `.claude-plugin/marketplace.json` metadata bumped to `v0.3.0`. `manfred-discovery` registered as the 6th plugin.
- `README.md` — added `manfred-discovery` to the plugin table, documented the v1.0.0 design-discipline reorg roadmap (mirrors of `Owl-Listener/designer-skills` plugins, with absorption of existing utility plugins).

### Transitional
- `manfred-product:brief-prd` (Scandic-specific) and `manfred-discovery:product-brief` (generalised, with explicit Cagan/Torres hooks) coexist in v0.13.x. `brief-prd` carries a deprecation note. The full reorg lands in v1.0.0 — `manfred-product` removed, `brief-prd` content fully migrated.

### Roadmap
- v1.0.0 will reorg into 11 themed plugins replacing both the existing 5 utility plugins and the third-party `Owl-Listener/designer-skills` install. See README "Roadmap" section.

### Attribution
- Inspiration for the plugin/command structure (and several upcoming mirror plugins) draws from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) — MIT licensed. The `manfred-discovery` plugin itself is Manfred-original; mirror plugins (when they ship) will be structurally adapted with Manfred voice and opinions.

## [0.12.0] — 2026-04-30

### Changed
- **Skills now ship as plugins.** Migrated 14 skills from the loose `skills/<name>/` layout into 5 themed plugins under `plugins/<plugin-name>/`. The marketplace at `.claude-plugin/marketplace.json` now lists `manfred-a11y`, `manfred-writing`, `manfred-product`, `manfred-dev`, and `manfred-knowledge` (each at `v0.1.0`). Marketplace metadata bumped to `v0.2.0`.
- `install.sh` no longer copies skills. It now installs only the home `~/.claude/CLAUDE.md` and `~/.claude/shared/` reference docs, then prints the `/plugin install` commands. A new `check_legacy_skills` step warns users with leftover copies in `~/.claude/skills/` and prints the cleanup commands.
- `README.md` rewritten around the plugin-first install flow with a per-plugin table and a migration section for users coming from `install.sh`-installed skills.
- Top-level `skills/` directory removed — all skills now live under `plugins/<plugin>/skills/`.

### Added
- `plugins/manfred-dev/skills/test-my-code/` — opinionated pre-merge QA gate for Vite/React features (typecheck → lint → vitest → build → Playwright → axe). Saves a report file and posts the summary to the linked Linear ticket. Built today via the full TDD-for-skills loop. Calls into `manfred-a11y`'s `a11y-qa` for the runtime accessibility scan.
- `plugins/manfred-knowledge/skills/clippings-linter/` — Obsidian vault hygiene (broken notes, missing tags, duplicates, orphans). Includes Python lint scripts.

### Migration
Existing users with `~/.claude/skills/<name>/` from previous `install.sh` runs: re-run `install.sh` once — it detects the legacy directories and prints the cleanup commands. Then `rm -rf ~/.claude/skills/<name>` for each affected skill and `/plugin install manfred-<plugin>@manfred` to pick up the plugin-distributed version.

## [0.11.0] — 2026-04-29

### Added
- `skills/release` — full production release skill that runs quality gates (lint, types+build, unit tests, a11y audit), waits for the Vercel deploy to reach `READY` after pushing, then comments + transitions Linear tickets and updates Linear Project descriptions. Sibling to the lightweight `deploy` skill — use `release` for projects with Vercel-GitHub deploys and `STU-###` tickets, `deploy` for everything else. Includes `references/linear-actions.md` (verified Linear MCP call patterns including the Linear Project vs project-Milestone distinction) and `references/vercel-wait.md` (deployment polling pattern). Built via the full TDD-for-skills loop in `superpowers:writing-skills` — three baseline pressure scenarios (just-ship-it, Linear-stale, typo-fix) drove the rationalization table; three REFACTOR scenarios verified compliance and surfaced two cosmetic-fast-path ambiguities that were patched.
- `MEMORY.md` — repo-level self-learning log with a "Standing lessons" section (TDD-for-skills, Linear MCP gotchas, Vercel-GitHub deploy mechanics, repo conventions) and dated session entries. Read on session start, append on session close, promote recurring lessons.

### Changed
- `README.md` skills table now lists 12 skills; `deploy` row clarified as "lightweight"; new `release` row added.
- `install.sh` and `uninstall.sh` `SKILLS=( … )` arrays include `release`.

## [0.3.4] — 2026-04-29

### Changed
- Repository moved from `jens-wedin/manfred-shared-knowledge` to `Studio-Manfred/manfred-shared-knowledge`. All install/uninstall URLs, marketplace registration command, and cross-references in `README.md`, `CLAUDE.md`, `install.sh`, `uninstall.sh`, `shared/home-claude.md`, `shared/manfred-brand.md`, and `shared/DESIGN.md` updated to the new org.
- `skills/deploy/SKILL.md` — git tag step (Step 7) is now part of the standard flow rather than optional, since downstream releases consistently rely on tags.

## [0.3.2] — 2026-04-19

### Changed
- `shared/manfred-brand.md` Brand Voice section rewritten with prescriptive tone-of-voice guidance: concrete rhythms lifted from `studiomanfred.com` (Q&A beats, shrug ellipsis, serious-serious-wink triplets, provocation-where-a-pitch-would-go), a Manfred Vocabulary list (Manfred Magic, the Mmmms, peeps, 〰️, Ping us), a named Anti-Patterns list (no marketing verbs, no corporate adjectives, no "we're passionate about…", no forced levity, no hedging), and a four-question Quick Test for new copy. The previous version described the voice; this one shows it.

## [0.3.1] — 2026-04-19

### Changed
- `shared/manfred-brand.md` rewritten after auditing `studiomanfred.com` — real mission ("Building Better Product Companies" / "make the product world more customer driven"), actual services (Leadership · Customer Research · Product/UX/Service Design · Training), the team ("the Mmmms": Jens Wedin, Selma Hallqvist, Axel Nathorst-Böös, Moa Bogren), named clients (Boka Direkt · Mentimeter · Fishbrain · Svea Bank · Trygg-Hansa), and the playful/craft-serious site voice ("Manfred Magic", "winging it with a whiteboard", "ping us"). Colors and typography retained under a new "Visual Language" section.
- `shared/design-principles.md` expanded from 12 to 15 principles: added Customer-Driven, Research Isn't a Phase, Craft Seriously (Yourself Not So Much), Critical & Ethical Design — reflecting Manfred's actual practice (training courses include Critical Design, Product Discovery, Customer Journey Mapping). The existing design-system principles (tokens, dark mode, shadcn shapes, accessibility) retained.
- `shared/DESIGN.md` opening reframed to make clear this describes the Manfred design system (one artifact the studio makes), not the studio itself — pointers to `manfred-brand.md` and `design-principles.md` added.

## [0.3.0] — 2026-04-19

### Added
- `shared/DESIGN.md` — full Manfred design system specification (colors, typography, components, dark mode, accessibility), sourced from `github.com/Studio-Manfred/manfred-design_system`
- `shared/design-principles.md` — 12-principle decision framework for Manfred work
- `install.sh` now installs DESIGN.md and design-principles.md alongside manfred-brand.md
- `uninstall.sh` removes DESIGN.md and design-principles.md

### Changed
- `shared/manfred-brand.md` rewritten with real content (brand thesis, values, voice, color palette, typography), replacing the v0.1.0 placeholder
- README "What gets installed" table updated with DESIGN.md and design-principles.md rows

## [0.2.0] — 2026-04-19

### Added
- Bundled 11 Manfred skills under `skills/`: `a11y-design`, `a11y-dev`, `a11y-qa`, `brief-prd`, `deploy`, `linkedin-reflect`, `linkedin-show-and-tell`, `linkedin-teach`, `markitdown-convert`, `meeting-summary`, `transcript-anonymizer`
- `install.sh` now performs a shallow `git clone` to fetch multi-file skills and copies them into `~/.claude/skills/<name>/`
- `install.sh` errors clearly when `git` is not on `PATH`
- `uninstall.sh` removes installed skill directories (honours `--yes` and the TTY guard)
- README documents the 11 bundled skills and the planned plugin migration

### Changed
- README "What gets installed" table now includes the skills row
- `install.sh` honours optional `MANFRED_REPO_GIT` env var for testing against a local checkout

## [0.1.1] — 2026-04-19

### Fixed
- `uninstall.sh` piped via `curl | bash` now errors clearly with a `--yes` hint instead of silently aborting on consumed stdin
- README uninstall command updated to pass `-s -- --yes` so `curl | bash` works end-to-end

### Added
- `*.backup.*` to `.gitignore` (installer backup files)
- Contributing guide entry for `shared/roles/` playbooks

## [0.1.0] — 2026-04-19

### Added
- Initial scaffold: `.claude-plugin/marketplace.json`, `install.sh`, `uninstall.sh`
- Placeholder home-level `CLAUDE.md` installed via `shared/home-claude.md`
- Placeholder `shared/manfred-brand.md`
- Project-level `CLAUDE.md` template at repo root
- Empty `skills/`, `commands/`, `plugins/`, `shared/roles/` directories ready for content
- README with install, contribute, and uninstall instructions
