---
name: design-system-adoption
description: Use when driving adoption of a design system across teams — anyone says "design system adoption", "get teams to use the design system", "design system rollout", "DS launch plan", "increase component usage", "design system not being used", "system migration plan", "DS as a product". Manfred-flavoured: treat the system as a product with users; barriers surfaced honestly; metrics + qualitative pairing.
---

# design-system-adoption

A design system that nobody uses is worse than no system — it consumed the build budget and produces no consistency. Adoption isn't a launch event; it's a product strategy.

Manfred treats design systems as products: with users (designers + engineers), a roadmap, support obligations, and metrics. Adoption flows from making the system genuinely easier to use than the alternative.

## Overview

Four levers, used together:

1. **Awareness** — people know it exists, what it covers, what's new
2. **Education** — people know how to use it, beyond the README
3. **Enablement** — the friction of using it is lower than the friction of not
4. **Incentives** — adoption is recognised; non-adoption is surfaced (without being punitive)

Plus measurement: adoption percentage, support load, time-to-implement, audit scores. Numbers + qualitative pairing.

## When to use

- Launching a new design system or major version
- The design system exists but adoption is low / inconsistent
- Onboarding a new team or project to use the system
- Auditing why adoption stalled
- Building the case for design system investment (to leadership)

**Skip when:**

- The system itself isn't ready (don't drive adoption of a half-built thing — fix the system first)
- The user wants to *audit* token usage (use `manfred-toolkit:design-token-audit` — different artifact)
- The user wants component contribution patterns (different — that's `manfred-design-systems:component-spec` + `manfred-design-ops:version-control-strategy`)

## Pre-flight

Ask:

- **What's the current state of adoption?** (Anecdotal? Measured? Specific projects using vs. not?)
- **What's broken?** (System doesn't cover needs? Docs are bad? Components too rigid? Breaking changes too frequent? No clear contribution path?)
- **Who are the users?** (Designers? Engineers? Both? PMs sometimes?)
- **What's the baseline?** (Component usage %? Custom-override count? Support question volume?)
- **Stakeholder support?** (Leadership backing? Or grassroots?)

If the user can't name what's broken — push back. "We just want more adoption" produces generic adoption-strategy decks. Specific failure modes produce useful adoption work.

## The hard rules

| Rule | What it means |
|---|---|
| **Treat the system as a product with users** | Designers and engineers are the customers. Their experience using the system is the product. Apply product thinking — research, iterate, measure. |
| **Barriers surfaced honestly** | List specific barriers with evidence — "users say docs are confusing because [specific section]". Generic "docs need work" produces no action. |
| **Reduce friction first, then incentivise** | Adoption follows ease. If the system is harder than the alternative, no incentive will fix it. Make it easy first; recognition follows. |
| **Metrics + qualitative pairing** | Numbers tell what's happening; verbatims tell why. Track both. |
| **Migration support, not mandates** | Mandates without support produce malicious compliance. Support produces actual adoption. Offer codemods, office hours, paired onboarding. |
| **Public roadmap** | Consumers need to know what's coming. Hidden roadmap = consumer fork. |
| **Listen to objections** | Every objection reveals a real gap (or a real misunderstanding). Catalogue them; address the patterns. |

## The four levers

### 1. Awareness

People know the system exists, what it covers, what's new.

- **Launch announcement** — Slack post, email, optional all-hands. Brief: what's in v1, who it's for, where to start.
- **Documentation site** — searchable, with examples for every component. Storybook minimum; ideally a docs site with prose context.
- **Changelog communication** — every release ships with a changelog (per `manfred-design-ops:version-control-strategy`). Major releases get an extra Slack post + email.
- **Showcase projects** — internal teams that adopted well; show the before / after.

Without awareness, teams build their own components in parallel. They aren't malicious — they don't know yours exists.

### 2. Education

People know how to use it, beyond the README.

- **Getting started guides** — separate for designers (Figma library setup, naming conventions) and engineers (npm install, import patterns)
- **Component usage guidelines** — when to use which component, with examples
- **Workshop series** — introductory (1 hour), advanced (1 day for power users), contribution (how to add to the system)
- **Office hours** — weekly drop-in, 30 min, for questions and unblocking

The Slack `#design-system` channel is the lightest version. Workshops are heavier; office hours are weekly maintenance.

### 3. Enablement

The friction of using the system is lower than the friction of not.

- **Figma library setup** — designers can drag in components in <5 sec
- **Code packages** — `npm install @manfred/design-system` and import; types ship with the package
- **Templates and starter kits** — new project starts include the design system pre-wired
- **Migration guides** — for moving from legacy patterns; codemods where possible (`npx @manfred/migrate-button-to-action`)

The test: a designer who's never used the system should be able to drop in a Manfred Button + FormField + Toast in under 5 minutes. If it takes longer, the friction is the problem.

### 4. Incentives

Adoption is recognised; non-adoption is surfaced.

- **Celebrate teams that adopt well** — internal newsletter / Slack post / show-and-tell
- **Track and share adoption metrics** — public dashboard or quarterly readout. Designers + engineers see how their team is doing.
- **Reduce friction further than the alternative** — make it easier to use the system than not (as above)
- **Include in code/design review criteria** — the gate at PR time (`manfred-design-ops:design-qa-checklist` checks token compliance)

Avoid: punishing teams for not adopting. The right response to "team X isn't adopting" is "what's blocking them?" — not "why won't they comply?".

## Measuring adoption

Pick 3-5 metrics across categories. Don't try to measure everything.

| Metric | What it captures | Cadence |
|---|---|---|
| **Component usage %** | Of all interactive UI on a project, what % uses Manfred components vs custom | Quarterly per project, automated where possible |
| **Custom override count** | Number of `style={{ ... }}` or token-bypass instances per project | Quarterly |
| **Support question volume** | Slack `#design-system` questions per month | Monthly — should decrease as docs improve |
| **Time-to-implement** | New feature dev time using the system vs without | Per major feature |
| **Consistency audit score** | `manfred-toolkit:design-token-audit` outputs | Quarterly |

Pair every quantitative metric with qualitative — what are designers / engineers actually saying about the system? Run a quarterly retro.

## Common adoption barriers

| Barrier | Pattern | Fix |
|---|---|---|
| **System doesn't cover team's needs** | Custom components proliferating because the system lacks something | Surface the gap; prioritise the missing component; fast-track |
| **Documentation is incomplete or confusing** | Repeated questions on the same topic | Improve the docs; office hours surfaces what's unclear |
| **Components are too rigid** | Teams forking components for local use | Add composition primitives (`asChild`, slots); revisit component API |
| **Breaking changes too frequent** | Teams avoiding upgrades | Better deprecation strategy (`manfred-design-ops:version-control-strategy`); longer transition windows |
| **No clear contribution path** | Teams want to add to system but don't know how | Document contribution; pair-program with first contributors |
| **Leadership unaware of value** | System investment under threat | Quarterly readout to leadership with metrics + business framing |

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Adoption will follow if we just ship the system" | It won't. Adoption is product work, not technical work. Plan for it. |
| "We'll mandate adoption" | Mandates produce malicious compliance — components used in name but worked around. Earn adoption via friction reduction. |
| "We don't have time for office hours / workshops" | Office hours / workshops are cheaper than the cost of teams forking the system. Make time. |
| "Teams just need to follow the docs" | If teams can't follow the docs, the docs are the failure point — not the teams. Improve docs first. |
| "We'll measure adoption with one number" | One number hides the why. Pair with qualitative. |
| "Public roadmap commits us to too much" | Hidden roadmap commits you to consumer surprise. Public roadmap (with caveats) is more honest and trust-building. |

## Red flags — STOP

- Driving adoption of a system that's still half-built (fix the system first)
- Mandating without offering migration support
- Measuring with vanity metrics (downloads, "engagement") instead of usage % + audit score
- Punitive responses to non-adoption (the response should be "what's blocking?")
- Hiding breaking changes from consumers
- Documentation that requires Slack DMs to interpret — improve the docs

## Manfred lens

Design system adoption touches **viability risk** (Cagan) — a system nobody uses isn't viable. It also reflects **design principle 8 (use the tokens)** and **principle 11 (consistent, not uniform)** — both depend on consumers actually using the system.

Critical & ethical (principle 6): adoption strategy should never resort to manipulation (false urgency, public shaming, gatekeeping legitimate work behind compliance). The goal is consumers *wanting* to use the system because it makes their work better.

## Cross-references

- `~/.claude/shared/DESIGN.md` — the design system spec being adopted
- `manfred-design-systems:design-token` — tokens are central to adoption metrics
- `manfred-design-systems:component-spec` — components are central to adoption
- `manfred-design-ops:version-control-strategy` — breaking-change cadence affects adoption
- `manfred-design-ops:team-workflow` — adoption fits into team rituals
- `manfred-toolkit:design-token-audit` — measures adoption quantitatively
- `manfred-toolkit:case-study` — adoption success stories become case studies

## Output format

Save the adoption strategy to `discovery/adoption/<system-name>-<YYYY-MM-DD>.md`:

```markdown
# Design system adoption strategy: <system>

**Date**: YYYY-MM-DD
**Owner**: <design system PM / lead>
**Audience**: <designers, engineers, leadership>

## Current state
[Adoption %, key barriers, where the system is succeeding / failing]

## Strategy
[Awareness, education, enablement, incentives — what's planned, by when]

## Metrics
[3-5 metrics with baselines + targets + cadence]

## Roadmap
[Public version — what's coming in next 2-4 releases]

## Office hours / support
[Cadence + channel]

## First milestone
[The next concrete deliverable + date]
```

## Tools used

- `Read` — current adoption data, support channel logs, prior retros
- `Write` — produce the strategy doc
- `manfred-toolkit:design-token-audit` — for adoption measurement
- `manfred-design-ops:version-control-strategy` — for breaking-change communication
- `manfred-discovery:discovery-readout` — for stakeholder readouts

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
