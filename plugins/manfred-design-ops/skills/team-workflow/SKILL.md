---
name: team-workflow
description: Use when designing or refining a design team's workflow — anyone says "team workflow", "design team rituals", "design ops setup", "task management for designers", "communication norms", "tooling stack", "design sprint cadence", "how should our team work together". Manfred-flavoured: Trio attendance, Linear-anchored, async-first with sync moments earned.
---

# team-workflow

A workflow is the team's answer to "how do we actually do the work together?". Done well, it makes the small decisions automatic, leaving the team's attention for the hard ones. Done badly, every project re-invents process and the team drifts.

Manfred workflows lean **async-first with sync moments earned** — async surfaces individual perspectives, sync resolves tensions. The Trio (PM + designer + tech lead) attends the rituals that benefit from cross-functional input.

## Overview

Five components. Pick what the team needs — a 4-person team isn't a 40-person team.

1. **Task management** — how work is tracked
2. **Collaboration rituals** — recurring sync moments
3. **Communication norms** — when to use sync vs async, response expectations
4. **Tooling stack** — what tools and what they're for
5. **Design ↔ engineering collaboration** — where the design + dev surfaces meet

Plus the workflow stages: discovery → exploration → refinement → handoff → QA → iteration. Different rituals serve different stages.

## When to use

- New team forming and needs to agree on how it'll work
- Existing team where the workflow has drifted and rituals feel stale
- Onboarding a new team member
- Onboarding a new client engagement (Manfred-side workflow + client-side workflow)
- Reviewing a workflow that's producing friction (post-retro action)

**Skip when:**

- Solo work (rare)
- The team's current workflow is working (don't manufacture process)
- The user wants project-specific planning (use `manfred-design-ops:design-sprint-plan` for sprints, `manfred-ux-strategy:design-brief` for project framing)
- The user wants stakeholder dynamics specifically (use `manfred-ux-strategy:stakeholder-alignment`)

## Pre-flight

Ask:

- Team size? (4-person team's workflow is a 1-page doc; 20-person team needs more structure)
- Co-located, hybrid, or fully remote? (Different rituals work in each)
- Existing tools? (Don't propose Notion if the team uses Confluence; meet them where they are)
- What's broken in the current workflow? (Past failure surfaces real risks better than abstract design)
- Trio composition? (PM + designer + tech lead — confirm names and time-zones)

If the user can't name what's broken, the workflow change isn't ready. "We just feel like we should have one" produces unused process.

## The hard rules

| Rule | What it means |
|---|---|
| **Async-first, sync-when-earned** | Default to async (Linear comments, FigJam, Slack threads). Sync (meetings, calls, in-person) for moments where async stalls. Most "we need a meeting" can be solved async. |
| **Trio attends cross-functional rituals** | PM + designer + tech lead at design reviews, retros, planning. Not PM-only or designer-only. The Trio is the cross-functional check. |
| **Documented + visible** | Workflow doc lives somewhere everyone reads (Linear project description, repo CLAUDE.md, team Notion). Tribal knowledge dies on hire #4. |
| **Reviewed regularly** | Quarterly retro on the workflow itself: what's helping, what's friction, what changed in team or project shape. Workflows that don't get revisited drift. |
| **Optimised for actual needs** | Copying a workflow from another team rarely fits. Match the team's size, context, communication style. |
| **Linear is the source of truth for work** | All design work has a Linear ticket. Status reflects reality. Comments capture decisions + handoffs. Pattern reference: `manfred-dev:test-my-code` (Linear update section). |
| **Automate repetitive coordination** | Standup automated (Slack bot or Linear comment thread, not 15-min sync every morning). Status updates pulled from Linear, not manually compiled. |

## The five components

### 1. Task management

Manfred default: **Linear**. Setup:

- Project per engagement
- Issues per discrete piece of work (with `manfred-discovery:` / `manfred-design-systems:` / etc. labels for routing)
- Status: Backlog → Todo → In Progress → In Review → Done
- Cycles for week/sprint cadence
- Branch names follow `<author>/<key>-<slug>` (`jens-wedin/STU-100-settings-redesign`)

Capacity planning: Trio reviews load weekly. No planning poker theatre — just "is this realistic for the week?"

### 2. Collaboration rituals

| Ritual | Cadence | Format | Who | Purpose |
|---|---|---|---|---|
| **Standup** | Daily, async | Slack thread or Linear comments | Whole team | What's moving, what's stuck |
| **Design critique** | Weekly | 60 min sync (or async via Figma + 30 min sync close) | Designer + Trio + 1-2 peers | Structured feedback (`manfred-design-ops:design-critique`) |
| **Design review** | Per milestone | 60 min sync per gate | Trio + decider | Quality gate (`manfred-design-ops:design-review-process`) |
| **Discovery readout** | Per discovery cycle | Async write-up + 30 min Q&A | Trio + stakeholders | Research findings (`manfred-discovery:discovery-readout`) |
| **Retrospective** | Monthly or per cycle | 60 min sync | Whole team | Process improvement |
| **Show and tell** | Bi-weekly | 30 min sync | Whole team + adjacent teams | Share work, surface cross-team patterns |
| **1:1s** | Weekly or bi-weekly | 30 min | Manager + IC | Career, blockers, feedback |

The default is async-first. Sync rituals justify their time by producing decisions or shared understanding async can't.

### 3. Communication norms

```markdown
## Sync vs async

- **Sync** (calls, in-person, scheduled meetings): decisions that need real-time tension resolution, kickoffs, retros
- **Async** (Linear, Slack threads, Loom, FigJam): updates, structured feedback, documented decisions, anything one person can resolve

If you're about to schedule a meeting: ask if a Linear comment + Loom + 24h response would solve it. Most "quick syncs" should be async.

## Response time expectations

| Channel | Response time |
|---|---|
| Slack DM (urgent) | <2 hours during work day |
| Slack channel mention | <1 working day |
| Linear comment | <1 working day |
| Email | <2 working days |
| Figma comment | <2 working days |

Out-of-hours: no response expected. Weekends: no response expected. Time-zone differences: respected, not steamrolled.

## How to request feedback

Format:
1. **Context** — what is this, why does it exist, what stage
2. **Specific ask** — what feedback you want (and what you don't)
3. **Deadline** — when you need it by

Bad: "thoughts?"
Good: "Settings page — pre-handoff, looking for feedback on the empty state. Not looking for feedback on the layout. Need by Wed EOD."

## How to share decisions

Decisions that affect more than one person get written up + posted (Linear ticket, project log, Slack channel). Format:

- What was decided
- Why (the trade-off considered)
- Who's affected
- What needs to change

No decision-by-DM. Decisions in DM = decisions invisible to the team.
```

### 4. Tooling stack (Manfred default)

| Tool | Purpose |
|---|---|
| **Linear** | Project + task management, decisions log |
| **Figma** | Design tool, design system source, prototyping |
| **Slack** | Sync-ish comms, urgent comms |
| **Loom** | Async walkthroughs (handoffs, design reviews) |
| **Notion** | Long-form docs, team workflow doc, retro notes |
| **GitHub** | Code, design system source code, CLAUDE.md per project |
| **Vercel** | Deploy previews (per `manfred-dev:deploy`, `manfred-dev:release`) |
| **Storybook** | Design system + component documentation |

If the team uses different tools, swap. The pattern matters more than the brand.

### 5. Design ↔ engineering collaboration

The seams are where things break:

- **Designers in sprint ceremonies** — at minimum, designer in standup + planning. At best, designer in retros too. Designer-isolated-from-engineering produces designs engineering can't build.
- **Handoff** — `manfred-design-ops:handoff-spec` is the artifact; Linear is the channel; walk-through (or Loom) is the sync moment.
- **Design QA** — `manfred-design-ops:design-qa-checklist` runs designer-side; `manfred-dev:test-my-code` runs engineering-side. Both gates pass before merge.
- **Bug filing for design issues** — file in Linear (not Slack), with screenshot + spec ref + severity (`manfred-design-ops:design-qa-checklist`).
- **Shared component library management** — designers + engineers both contribute (`manfred-design-systems:component-spec`); breaking changes versioned (`manfred-design-ops:version-control-strategy`).

## Workflow stages

| Stage | What happens | Who's primary | Skills used |
|---|---|---|---|
| **Discovery** | Research, problem framing | Designer + PM | `manfred-design-research:*`, `manfred-discovery:*` |
| **Exploration** | Concept generation, evaluation | Designer + Trio | `manfred-design-ops:design-critique`, `manfred-design-ops:design-sprint-plan` (if sprint shape) |
| **Refinement** | Detailed design + spec | Designer + tech lead | `manfred-design-systems:component-spec`, `manfred-design-systems:design-token` |
| **Handoff** | Engineering pickup | Designer + engineer | `manfred-design-ops:handoff-spec` |
| **QA** | Implementation verification | Designer + engineer | `manfred-design-ops:design-qa-checklist`, `manfred-dev:test-my-code` |
| **Iteration** | Post-launch improvement | Trio | `manfred-discovery:weekly`, `manfred-design-research:summarize-interview` |

## Common rationalisations

| Excuse | Reality |
|---|---|
| "We don't need a documented workflow, we all know how to work" | Tribal knowledge dies on hire #4. Document it; revisit it; keep it visible. |
| "More meetings will fix our coordination problem" | Probably the opposite. Audit current meetings — half can usually go async. |
| "We'll do retros when we feel like it" | Retros that aren't on the calendar don't happen. Set a cadence. |
| "Async-first is just remote-work theatre" | Async-first respects time zones, deep work, and individual perspective. Sync-first respects nobody's calendar. |
| "We can't change our tools, we've always used X" | Tool match the workflow, not vice versa. If X doesn't serve the work, swap. |
| "Designers don't need to attend engineering ceremonies" | They do for any cross-functional ceremony. Designer-isolated-from-engineering = designs engineering can't build. |
| "The Trio is overkill for small projects" | The Trio is the smallest cross-functional unit. Small projects still benefit from PM + designer + tech lead checking each other. |

## Red flags — STOP

- Workflow doc not visible / not maintained
- Critical decisions captured only in DMs
- Designer or tech lead absent from cross-functional rituals
- Standup is a 15-min sync that could be async
- No retro cadence
- Tool sprawl (5 tools doing the job of 2)
- "Quick sync" requests for things that could be Linear comments

## Manfred lens

Workflow is **infrastructure** — Cagan/Torres lens doesn't apply directly. But: workflow shapes how research insights land, how decisions get made, how design work gets reviewed. A bad workflow makes good discovery invisible. The five components above are scaffolding for the substantive work — `manfred-discovery:discovery-rituals`, `manfred-design-ops:design-review-process`, `manfred-design-ops:design-critique`.

Critical & ethical (principle 6): workflow includes feedback channels for raising ethics concerns. The Trio + retro should explicitly include "anything we shipped this cycle that we'd be uncomfortable with our names on?". Process the answer; don't deflect.

## Cross-references

- `manfred-design-ops:design-critique` — the format for critique rituals
- `manfred-design-ops:design-review-process` — the gates for review rituals
- `manfred-design-ops:design-sprint-plan` — sprint-shape work
- `manfred-design-ops:handoff-spec` — design ↔ engineering seam
- `manfred-design-ops:design-qa-checklist` — design QA in the workflow
- `manfred-design-ops:version-control-strategy` — for the design-system-versioning side
- `manfred-discovery:discovery-rituals` — for the discovery-cadence side
- `manfred-ux-strategy:stakeholder-alignment` — for stakeholder dynamics
- `manfred-dev:test-my-code` — engineering-side gate

## Tools used

- `Read` — current workflow docs, retro notes, project briefs
- `Write` — produce or update the workflow doc
- `manfred-design-ops:design-review-process` — for the review-gate side
- `manfred-discovery:discovery-rituals` — for the discovery-cadence side

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, and Manfred-specific guidance are original.*
