---
name: discovery-rituals
description: Use when setting up or refreshing a team's continuous discovery rhythm — the recurring meetings, calendar holds, and review cadences that keep discovery from collapsing back into project research. Triggers on "discovery rituals", "team discovery cadence", "OST review meeting", "weekly assumption test review", "set up continuous discovery for our team", "make discovery routine", "discovery operating model". Produces a calendar of recurring rituals plus a one-page operating doc the team commits to.
---

# discovery-rituals

The recurring meetings that turn discovery from a thing-we-do-when-we-have-time into a thing-we-do-this-week. Without them, continuous discovery isn't.

## Overview

Continuous discovery only stays continuous because it's scheduled. Most teams that say "we do continuous discovery" have a few enthusiastic interviews in flight and no rhythm. This skill stands up four recurring rituals plus the meta-ritual that keeps them honest:

1. **Weekly Trio touchpoints** — 3–5 customer conversations a week, attended by PM + designer + tech lead
2. **Friday synthesis** — 60 min, Trio reviews what they heard, updates the OST
3. **Monthly OST review** — extended team (Trio + stakeholders) walks the tree, prunes, re-prioritises
4. **Quarterly outcome check** — is the outcome we're driving still the right one?
5. **Meta-ritual: Discovery health check** — every 6 weeks, the Trio asks "are we actually doing this, or LARPing?"

It's overkill for a single feature. It's underkill for a team that owns an outcome.

Source: Teresa Torres, *Continuous Discovery Habits* — operationalised. Marty Cagan's "discovery vs delivery" cadence sits underneath.

## When to use

- A new team / squad standing up around an outcome
- A team that's been "doing discovery" but it keeps slipping → time to make it rhythm
- After a `manfred-discovery:product-brief` recommends discovery as the next step → set up the rituals to do it
- Quarterly: time to refresh the cadence

**Skip when:**

- The team isn't accountable for an outcome (rituals without an outcome become meeting theatre)
- A genuine project-research mode (one-off, time-bounded — use design-research instead, when that plugin ships)

## Two principles drive everything

1. **Rituals require an outcome.** Without a stable outcome, discovery rituals devolve into "what should we research?" Get the outcome locked first (`manfred-discovery:product-brief` section 02), then build rituals on top.
2. **Trio attendance is the rate-limiter.** All rituals require PM + designer + tech lead. If the Trio can't show up to the rhythm, the rhythm needs to shrink to what they can sustain. 1 customer/week with the full Trio beats 5/week with only the PM.

## Phase 1 — Pre-flight

Before standing up rituals, confirm:

- "What outcome is this team accountable for? (One, named, measurable, stable for at least the quarter.)"
- "Who's the Trio? (PM, designer, tech lead — actual names, not roles.)"
- "What's the team's current discovery state — none, ad-hoc, struggling, or already running?"
- "Any existing meetings that overlap or could be repurposed? (Don't add 4 new meetings on top of 12 existing ones — repurpose first.)"

If the team can't name the Trio or the outcome, fix that before scheduling anything.

## Phase 2 — The four core rituals

### Ritual 1: Weekly Trio Touchpoints

| Field | Value |
|-------|-------|
| **Frequency** | Weekly |
| **Duration** | 3–5 × 60 min slots, spread across 3 days |
| **Attendees** | Trio (all three, every conversation) |
| **Output** | Recordings + transcripts; per-conversation notes |
| **Linked skill** | `manfred-discovery:customer-touchpoint-plan` |

Calendar holds: 5 fixed weekly slots that the Trio commits to. The PM owns recruit; the slots are recruited *into*, not the other way around.

### Ritual 2: Friday Synthesis

| Field | Value |
|-------|-------|
| **Frequency** | Weekly, Friday afternoon |
| **Duration** | 60 min |
| **Attendees** | Trio (extended team optional) |
| **Output** | OST updates + 1-paragraph weekly digest |
| **Linked skill** | `manfred-discovery:discovery-readout` (lightweight version), `manfred-discovery:opportunity-solution-tree` |

Format: Trio walks the week's conversations, surfaces themes, updates the OST. The output isn't minutes — it's tree changes and a 1-paragraph note that goes into the team channel.

### Ritual 3: Monthly OST Review

| Field | Value |
|-------|-------|
| **Frequency** | Monthly, ~90 min |
| **Attendees** | Trio + stakeholders (analyst, CS lead, key engineer, etc.) |
| **Duration** | 90 min |
| **Output** | OST pruned + reprioritised; assumption test backlog refreshed |
| **Linked skill** | `manfred-discovery:opportunity-solution-tree`, `manfred-discovery:assumption-test` |

Format: walk the OST top-to-bottom. For each opportunity, ask "still highest-impact?" For each solution, ask "still pursuing?" For each test, ask "still relevant?" Prune ruthlessly. Add the next month's planned tests.

### Ritual 4: Quarterly Outcome Check

| Field | Value |
|-------|-------|
| **Frequency** | Quarterly, ~90 min |
| **Attendees** | Trio + product leadership |
| **Output** | Outcome confirmed, rephrased, or replaced; OST re-rooted if outcome changes |
| **Linked skill** | `manfred-discovery:product-brief` (section 02 round-trip) |

Format: revisit the outcome the team is accountable for. Has it shifted? Is the team still the right team to drive it? Are the leading metrics still the right ones? Outcome changes are rare but consequential — when they happen, the OST gets re-rooted and old branches archived (not deleted — moved to a "previous outcomes" section for institutional memory).

## Phase 3 — The meta-ritual: Discovery Health Check

Every 6 weeks, the Trio asks itself five questions. 30 minutes, no extended team.

1. **How many customers did we actually talk to in the last 6 weeks?** Target: 25–30 (5/week × 5–6 weeks). Below 15: the rhythm is broken — diagnose what blocked it.
2. **How many assumption tests did we run? How many returned a clear yes/no?** If most returned inconclusive, the test designs need work — see `manfred-discovery:assumption-test`.
3. **Did the OST update weekly?** Check the `last updated` timestamps. Skipped weeks = synthesis didn't happen.
4. **What did discovery actually change in the last 6 weeks?** Name the decisions. If you can't, discovery wasn't influencing the team — it was decoration.
5. **What's the smallest change to the rituals that would make next 6 weeks better?** One change, not three. Ship and re-check.

Capture the answers in `discovery/health-checks/<YYYY-MM-DD>.md`. Honest answers > performative ones.

## Phase 4 — Save the operating doc

Save to `discovery/discovery-rituals.md`. This is the team's commitment to themselves.

```markdown
# Discovery rituals — [Team / Outcome name]

**Outcome:** [from the OST]
**Trio:** [PM] · [Designer] · [Tech lead]
**Last refreshed:** [YYYY-MM-DD]

## The rhythm

| Ritual | When | Attendees | Linked skill |
|--------|------|-----------|--------------|
| Customer touchpoints | 5×/week, [Mon/Wed/Fri] | Trio | `manfred-discovery:customer-touchpoint-plan` |
| Friday synthesis | Fridays 14:00–15:00 | Trio (+ optional) | `manfred-discovery:discovery-readout` |
| Monthly OST review | First Tuesday, 90 min | Trio + stakeholders | `manfred-discovery:opportunity-solution-tree` |
| Quarterly outcome check | Last week of quarter, 90 min | Trio + product leadership | `manfred-discovery:product-brief` (s2) |
| Discovery health check | Every 6 weeks, 30 min | Trio | (this skill, Phase 3) |

## Calendar holds

[Concrete recurring calendar invites — title, organiser, attendees, location/link.]

## Recruit pipeline

- **Source:** [in-product, support history, CS list, panel-as-fallback]
- **Owner:** [PM name]
- **Incentive:** [amount + format]
- **Backup channel:** [for weeks when primary recruit fails]

## What we're committing to

- The Trio attends every customer conversation. Async read-back is a fallback, not the default.
- The OST updates weekly. Skipped weeks are a health-check trigger.
- Assumption tests get a binary success/failure criterion before they run.
- Inconclusive tests get redesigned, not redone.
- Outcomes are stable for at least a quarter.

## What we're NOT committing to

- Build velocity targets that depend on skipping discovery
- "Lightweight" variants of these rituals during pressure (those become the default)
- Trio-of-one weeks (PM going alone) for more than one week in a row

## Health check log

| Date | What changed |
|------|--------------|
| [YYYY-MM-DD] | [one-line change to the rituals] |
```

## Manfred lens

- **`manfred-discovery:product-brief`** — Section 02 (Strategic Alignment) is where the outcome is named; rituals build on top
- **`manfred-discovery:opportunity-solution-tree`** — the OST is the central artifact; rituals exist to update and act on it
- **`manfred-discovery:customer-touchpoint-plan`** — used by the weekly touchpoint ritual
- **`manfred-discovery:assumption-test`** — used in the monthly OST review and individual test cycles
- **`manfred-discovery:discovery-readout`** — Friday synthesis produces a lightweight version; cycle wraps produce the full version
- **`manfred-discovery:weekly`** — the orchestrator command that walks through one weekly cycle of these rituals

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "We can do this lightweight — skip the synthesis ritual" | Skipping synthesis = touchpoints didn't enter the team's decision-making. Synthesis is the most-skipped, most-important ritual. |
| "We don't have time for all four rituals" | Then the team isn't doing continuous discovery — it's doing project research. Be honest about which mode you're in. |
| "Trio attendance is unrealistic — the tech lead is too busy" | Then the team isn't doing discovery at the pace of the OST decisions. Either reduce the touchpoint count to one the Trio can attend, or get a different tech lead aligned. |
| "We'll do the health check when we feel like we need it" | The health check exists to catch decay you can't feel. Schedule it or skip it explicitly — don't drift. |
| "The outcome shifts every sprint, so quarterly check is useless" | If the outcome shifts every sprint, the team doesn't have an outcome — it has a backlog. Fix that first. |
| "Adding meetings is the opposite of what the team needs" | Often true — that's why you repurpose existing meetings first. Net new meeting count should be 1–2, not 4. |
| "The PM can run all this solo, the team will catch up via the readout" | They can run it, but the team won't make the same decisions. Trio symmetry is the whole point. |

## Red flags — STOP

- About to schedule rituals without an explicit outcome → Stop. Outcome first.
- About to schedule weekly touchpoints without confirming the Trio can attend → Stop. Reduce frequency to what they can.
- About to skip the meta-health-check ritual because "we know we're doing fine" → Stop. The health check exists to catch what feels fine but isn't.
- About to set up the operating doc without naming the recruit pipeline → Stop. Touchpoints without recruit are aspirational.
- About to add 4 new meetings on top of 12 existing ones → Stop. Repurpose first; add net-new only as last resort.
- About to commit to rituals without naming what the team is NOT committing to → Stop. The "NOT committing to" list is what holds the line under pressure.

## Tools used

- **Read / Write**: `discovery/discovery-rituals.md`, `discovery/health-checks/<date>.md`
- **Skills called** (the ones the rituals operationalise):
  - `manfred-discovery:customer-touchpoint-plan`
  - `manfred-discovery:opportunity-solution-tree`
  - `manfred-discovery:assumption-test`
  - `manfred-discovery:discovery-readout`
  - `manfred-discovery:product-brief` (for outcome rephrasing)
- **Reference**: Teresa Torres, *Continuous Discovery Habits* (chapters on the team and the cadence); Marty Cagan, *Empowered* (chapters on discovery vs delivery and product team operating models)
