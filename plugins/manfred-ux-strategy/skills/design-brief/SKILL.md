---
name: design-brief
description: Use when writing a brief that defines the problem, audience, constraints, and success criteria for a design engagement — anyone says "design brief", "project brief", "kick off this project", "write a brief", "scope this engagement", "what are we doing here", "client brief", "internal brief". Manfred-flavoured: customer evidence floor, outcomes over outputs, ethics non-negotiable.
---

# design-brief

A design brief sets the team up to do focused work. Done right, every later argument routes back to the brief — "is this in scope?" gets answered by reading the doc, not by a meeting. Done wrong, the brief reads like marketing copy and resolves nothing.

Manfred briefs are concise (3–5 pages), evidence-led (research cites are non-optional), and outcome-shaped (success is measurable, not aspirational).

## Overview

A brief covers seven things — none optional, but each scaled to what the engagement actually needs:

1. **Project overview** — what, who, why
2. **Problem statement** — what's broken, who feels it, evidence, consequence
3. **Target audience** — primary and secondary; archetypes (not personas) where possible
4. **Goals + success criteria** — measurable outcomes, not output lists
5. **Scope + constraints** — in / out of scope, technical / brand / timeline / legal
6. **Context + inputs** — research available, prior attempts, references
7. **Deliverables + timeline** — outputs, milestones, review points, deadline

The brief is signed off before work starts. Disputes during the engagement get resolved by reading the brief, not by re-arguing.

## When to use

- Starting a new design engagement (client work, internal project, side bet)
- Mid-project when scope is drifting and the team needs an anchor
- Writing the brief for someone else (designer, agency, freelancer) — handoff requires precision
- Refreshing a stale brief that no longer reflects what the team is actually building

**Skip when:**

- The user wants strategic direction (use `manfred-ux-strategy:north-star-vision` or `manfred-ux-strategy:design-principles`)
- The user wants a product spec for engineering (different artifact — PRD, often `manfred-discovery:product-brief` is closer)
- The user wants a research plan (use `manfred-design-research:diary-study-plan` / `usability-test-plan` / etc.)

## Pre-flight

Ask, before drafting:

- Who's the audience for this brief? (Internal team, client, freelancer, board?)
- Is this a new engagement or a refresh of an existing one?
- What's been agreed verbally that needs to be captured? (Verbal agreements rot; the brief locks them in.)
- What evidence is available? (Existing research, analytics, customer touchpoint notes — cite specifically, not "research suggests".)
- Who signs off?

If "evidence" is "we believe…" or "we've heard…", flag it. The brief can still ship, but mark assumptions explicitly so they get tested in discovery, not assumed away.

## The hard rules

| Rule | What it means |
|---|---|
| **Customer evidence floor** | The problem statement cites specific evidence (research session, ticket pattern, NPS verbatim, churn cohort). "We believe users want…" is an assumption — flag it, don't disguise it as fact. |
| **Outcomes, not outputs** | Success criteria are measurable user / business changes — not "ship feature X" or "deliver 5 wireframes". Outputs are the work; outcomes are why we're doing the work. |
| **Scope is also "out of scope"** | What's NOT in scope is more important than what is. List explicitly. Things not in the "out of scope" list will be argued about. |
| **Brief is signed, not assumed** | The brief gets explicit sign-off from whoever's accountable (PM / client / lead). No sign-off = no shared agreement = scope creep is guaranteed. |
| **Concise, complete** | 3–5 pages, every section earned. A 20-page brief nobody reads beats a 4-page brief that does its job. |
| **Living document** | The brief gets revisited at milestones. Changes get agreed and dated. "The brief said X" beats "I thought we agreed to Y". |
| **Ethics test (principle 6)** | Every brief includes a "what does this design do in the world?" question and an honest answer. If the answer is "captures more attention" or "sells more stuff at the user's expense", revise. |

## Brief structure

```markdown
# <Project name> — design brief

**Date**: YYYY-MM-DD
**Status**: draft | signed | revised
**Owners**: <names>
**Sign-off**: <name>, <date>

## 1. Project overview

**One-line summary.** What this project is, in plain language.

**Business context.** Why this is happening now. What changed (market, internal, technical, regulatory).

**Stakeholders.** Who cares about this landing well. (Use `manfred-ux-strategy:stakeholder-alignment` for the full map if needed.)

## 2. Problem statement

**What's broken.** Specific moment in the user / business experience.

**Who feels it.** Specific user segment, named.

**Evidence.** Cite specifically — research sessions (date, count), analytics events, support ticket patterns, NPS verbatims, churn cohort data. "We believe…" gets flagged as assumption.

**Consequence.** What happens if we don't fix this. Quantify if possible (revenue, churn, support load, brand cost).

## 3. Target audience

**Primary user(s).** Named archetype (`manfred-design-research:user-archetype`) if research-backed; flagged assumption if not.

**Secondary user(s).** Less central but affected.

**Out of audience.** Who this is explicitly NOT for. (Critical — without this, every later argument re-litigates audience.)

## 4. Goals + success criteria

**Design goal.** Single sentence — the change this project is trying to make for users.

**Success criteria.**

| Type | Measure | Baseline | Target | When measured |
|---|---|---|---|---|
| Behavioural | Task completion rate | 62% | 80% | 4 weeks post-launch |
| Attitudinal | SUS score | 51 | 70 | 6 weeks post-launch |
| Business | Support tickets re: this flow | 120/wk | 40/wk | 8 weeks post-launch |

(Use `manfred-ux-strategy:metrics-definition` for picking the right measures.)

**Qualitative signal.** What we'll hear in customer conversations if this lands. ("Users will stop asking how to do X.")

## 5. Scope + constraints

**In scope.**
- [Specific deliverable / surface / flow]
- [Specific deliverable / surface / flow]

**Out of scope.**
- [Adjacent thing the team will be tempted to also fix — name it explicitly]
- [Thing that came up in discovery but isn't this engagement]

**Technical constraints.** Stack, performance budget, integration points, dependencies.

**Brand constraints.** Design system reference (`manfred-design-systems`), tokens, voice rules (`~/.claude/shared/manfred-brand.md`).

**Timeline constraint.** Hard date(s). What drives the date.

**Legal / regulatory.** Compliance requirements (PSD2, GDPR, WCAG 2.2 AA, accessibility legislation). The accessibility floor is non-negotiable — don't list it as "stretch goal".

**Budget / capacity.** Hours / people / weeks.

## 6. Context + inputs

**Research available.** Specific reports, with dates and links. (Not "we've done research" — name it.)

**Prior attempts.** What the team or others have tried before, and why it didn't work.

**Competitive context.** Output from `manfred-ux-strategy:competitive-analysis` if available.

**Reference material.** Inspirations, anti-examples, related work.

## 7. Deliverables + timeline

**Outputs.**

| Deliverable | Format | Owner | Due |
|---|---|---|---|
| User research synthesis | `manfred-design-research:affinity-diagram` output | … | … |
| Opportunity-solution tree | `manfred-discovery:opportunity-solution-tree` | … | … |
| Component spec(s) | `manfred-design-systems:component-spec` | … | … |
| Storybook + docs | `manfred-design-systems:documentation-template` | … | … |

**Milestones.**

- [Date] — kickoff + research
- [Date] — synthesis + opportunity prioritisation
- [Date] — design + prototype
- [Date] — usability test
- [Date] — handoff
- [Date] — launch
- [Date] — post-launch measurement

**Review points.** When and with whom decisions get made.

## 8. Ethics check (Manfred principle 6)

**What does this design do in the world?**
[Honest answer. Not marketing copy.]

**Who could this harm?**
[Specific. "Users who can't afford the upsell flow", "Users in regulated markets where this pattern is restricted", "People with cognitive disabilities for whom this density is exclusionary".]

**What's our mitigation?**
[Specific. If "no mitigation needed", justify.]

## 9. Assumptions to test

[Things stated above as fact that are actually assumptions. These feed `manfred-discovery:assumption-test` work in week 1.]
```

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We don't need a brief, the team's been talking about this for weeks" | Verbal agreement is not shared understanding. Write it down or watch the project drift. |
| "The brief is too formal for this small project" | A small project still needs scope, audience, success criteria. Scale the doc — keep the sections. |
| "We'll fill in the success criteria later" | "Later" is "never". A brief without measurable outcomes is a wish list. Pick metrics now, even if imperfect. |
| "Out of scope is too negative for the client" | The opposite — naming "out of scope" protects the client from paying for things they didn't budget. It's professional, not negative. |
| "Ethics check feels heavy for this project" | Heavy ethics for light projects is the bar. Light ethics for heavy projects is how brands quietly ship harm. Principle 6 doesn't have a project size threshold. |
| "We can skip 'assumptions to test' — we know what users want" | If you knew, you wouldn't need this engagement. Name the assumptions; test them in week 1; don't bake them into the design. |

## Red flags — STOP

- About to ship a brief without a sign-off line
- Success criteria are output-shaped ("ship 5 wireframes") rather than outcome-shaped ("users complete onboarding in <5 min")
- "Out of scope" section is empty
- Problem statement uses "we believe" / "we think" without flagging as assumption
- No ethics check
- No assumptions section (almost every brief has assumptions — claiming there are none = hiding them)
- Brief over 8 pages

## Manfred lens

A design brief touches **value risk** (Cagan) — is this product change worth doing at all? It also gates **discovery work** — every assumption in the brief is a candidate for `manfred-discovery:assumption-test`.

Cross-references:

- `manfred-discovery:product-brief` — the full PRD; design-brief is the design-side companion
- `manfred-discovery:opportunity-solution-tree` — the brief's "design goal" maps to a desired outcome at the OST root
- `manfred-discovery:cagan-risks` — every brief should pass a 4-risk check before kickoff
- `manfred-design-research:user-archetype` — the audience section uses real archetypes, not invented personas
- `manfred-ux-strategy:metrics-definition` — for picking success criteria

## Output format

Markdown brief, save to `discovery/briefs/<engagement-slug>-<YYYY-MM-DD>.md`.

The signed version sits at the same path with `-signed-<date>.md` suffix and is committed; revisions get a new dated copy, not in-place edits.

## Tools used

- `Read` — `~/.claude/shared/design-principles.md`, `~/.claude/shared/manfred-brand.md`, prior research
- `Write` — produce the brief
- `manfred-discovery:product-brief` — for product-level companion
- `manfred-discovery:cagan-risks` — for the 4-risk check
- `manfred-discovery:assumption-test` — for the assumptions section
- `manfred-design-research:user-archetype` — for the audience section
- `manfred-ux-strategy:metrics-definition` — for success criteria
- `manfred-ux-strategy:stakeholder-alignment` — for the stakeholders section

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
