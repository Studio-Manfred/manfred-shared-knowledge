---
description: Set up a design team's workflow end-to-end — task management + rituals + communication norms + tooling stack + design ↔ engineering seams + version control. Documented, visible, revisitable.
argument-hint: [team or engagement, e.g. "Manfred internal team workflow refresh"]
---

You're setting up or refreshing a design team workflow. The user mentioned: $ARGUMENTS

## Step 1 — Confirm what the workflow needs to fix

Ask:

- Is this a new team forming, or an existing team's refresh?
- What's currently broken? (Coordination, decisions disappearing, stakeholders surprised, design drift, missed accessibility gates?)
- Team size? Co-located, hybrid, or remote? Time zones?
- Existing tools? (Linear? Figma? Slack? Don't propose Notion if the team uses Confluence.)
- Trio composition? (PM + designer + tech lead — names + time-zones)

If the user can't name what's broken — push back. "We just feel like we should have one" produces unused process. Specific failure modes produce useful workflows.

## Step 2 — Run the team-workflow skill (`manfred-design-ops:team-workflow`)

Walk the five components:

1. **Task management** — Linear setup (project, issues, status, cycles, branch naming convention)
2. **Collaboration rituals** — standup (async), critique (`manfred-design-ops:design-critique`), reviews (`manfred-design-ops:design-review-process`), retros, show-and-tell, 1:1s
3. **Communication norms** — sync vs async defaults, response-time expectations, feedback request format, decision-sharing rules
4. **Tooling stack** — Linear / Figma / Slack / Loom / Notion / GitHub / Vercel / Storybook (or equivalents)
5. **Design ↔ engineering seams** — handoff (`manfred-design-ops:handoff-spec`), QA (`manfred-design-ops:design-qa-checklist`), bug filing, shared component library

Scale to team size. A 4-person team's workflow is a 1-page doc; a 20-person team needs more structure.

## Step 3 — Set up the rituals' cadence

For each ritual, confirm:

- Who attends (Trio always; others as needed)
- Cadence (daily / weekly / per cycle / per milestone / per release)
- Format (sync meeting / async write-up / mix)
- Time-box
- Output (decisions captured? action items?)
- Where it lives (Linear comment? Notion? Figma?)

Async-first where possible. Sync moments earned by producing decisions or shared understanding async can't.

## Step 4 — Set up version control (`manfred-design-ops:version-control-strategy`)

If the team produces design system code, components, or tokens — set up SemVer + changelog + branching:

- SemVer for components + tokens
- Changelog mandatory per release
- Breaking changes flagged loudly
- Deprecate before removing
- Communicate changes (Slack, README, optional email)

If the team only produces project-local components, defer to project conventions; just confirm the project has them.

## Step 5 — Set up cross-plugin handoffs

Confirm the workflow integrates with adjacent skills:

- `manfred-discovery:discovery-rituals` — discovery cadence (continuous-not-project)
- `manfred-design-research:*` — research workflow into the design workflow
- `manfred-design-systems:*` — design system contributions follow the version-control strategy
- `manfred-ux-strategy:design-brief` — engagement framing
- `manfred-dev:test-my-code` / `manfred-dev:release` — engineering gates

The workflow doc references these skills explicitly so the team knows where to reach.

## Step 6 — Document and make visible

The workflow doc lives in:

- Linear project description (top of every project)
- Repo `CLAUDE.md` (auto-loaded into Claude Code context per project)
- Team Notion / Confluence (long-form reference)

Don't pick one — pick at least two. Tribal knowledge dies on hire #4.

## Step 7 — Set the revisit cadence

Workflow on autopilot drifts. Schedule:

- **Quarterly retro on the workflow itself** — what's helping, what's friction, what changed in team or project shape
- **Per-engagement review** — does this engagement need a workflow tweak?

Capture changes in a workflow changelog (parallel to design system changelog).

## Step 8 — Linear update

If a Linear project is in scope, post a comment via `mcp__linear-server__save_comment` with:

- Workflow doc link
- Ritual schedule
- Tooling stack
- Trio composition
- Revisit date

## Wrap-up

Confirm the workflow covers:

- [ ] Task management (Linear or equivalent)
- [ ] Collaboration rituals with cadence + format + output
- [ ] Communication norms (sync/async, response times, feedback format)
- [ ] Tooling stack
- [ ] Design ↔ engineering seams
- [ ] Version control strategy (if design system work)
- [ ] Cross-plugin handoffs documented
- [ ] Workflow doc lives in 2+ visible places
- [ ] Quarterly revisit cadence set

Then offer:

> "Run the workflow for one cycle, then schedule a workflow retro. If specific rituals need refining, revisit `/manfred-design-ops:design-critique` for crit format or `/manfred-discovery:weekly` for discovery cadence."
