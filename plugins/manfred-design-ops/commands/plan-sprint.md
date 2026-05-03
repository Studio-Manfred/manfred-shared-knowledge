---
description: Plan a design sprint end-to-end — challenge framing + pre-flight checklist + 5-day schedule + recruit + test plan + follow-up commitment.
argument-hint: [challenge or scope, e.g. "design sprint for the Settings page redesign, week of June 1"]
---

You're planning a design sprint. The user mentioned: $ARGUMENTS

## Step 1 — Confirm a sprint is the right shape

Ask:

- Is this a hard, well-bounded problem the team keeps circling? (Sprint shape.)
- Or is it a continuous-discovery question that `manfred-discovery:weekly` could serve? (Don't manufacture sprint.)
- Decision-maker available for the full week?
- Team can clear schedules?

If the problem isn't bounded — push for `manfred-ux-strategy:frame-problem` first to scope it. If the team can't clear the week — push to next week. **Sprint with half-attendance is sprint-shaped meetings.**

## Step 2 — Challenge statement

Draft the one-sentence challenge: "In [time-frame], [user] can [outcome] in [constraint]." Falsifiable, ambitious, specific.

Examples:
- "In 6 months, a new user can complete KYC verification in under 2 minutes."
- "In 3 months, an existing customer can dispute a transaction without contacting support."
- "In Q4, we can launch a sub-brand with full design-system support in under 2 weeks."

If the statement is vague ("improve onboarding"), the sprint will produce vague output. Sharpen first.

## Step 3 — Pre-flight checklist (`manfred-design-ops:design-sprint-plan`)

Run through the Day-0 checklist:

- [ ] Challenge statement defined
- [ ] Decision maker identified + committed
- [ ] Team assembled (5-7 people, cross-functional)
- [ ] Room + materials booked (or virtual setup ready)
- [ ] Users recruited for Day 5 (5 testers per `manfred-design-research:user-archetype`, paid)
- [ ] Schedules cleared
- [ ] Materials read in advance (research, prior artefacts)

If any is missing — block the sprint until it's locked. Don't run a sprint with gaps.

## Step 4 — Decide sprint shape (Classic / Mini / Discovery / Remote)

Run the `manfred-design-ops:design-sprint-plan` skill to produce the per-day schedule:

- Classic 5-day: Understand → Diverge → Decide → Prototype → Test
- Mini (2-3 days): compressed
- Discovery sprint: Days 1-2 only, no prototype
- Remote: replace whiteboards with FigJam, dot-vote with reactions, in-room interviews with video calls

## Step 5 — Day 5 test plan (`manfred-design-research:usability-test-plan`)

Even though the test happens Day 5, plan it Day 1. Specifically:

- 3-5 research questions tied to the challenge
- Recruit (5 users matching the archetype, paid, scheduled)
- Tasks as scenarios in user language
- Facilitation guide (don't help, don't explain)
- Pilot (Day 4 internal volunteer)
- Synthesis plan (debrief after each, patterns by Day 5 EOD)

Test plan ready Day 1 = recruit can be confirmed; prototype is built against known questions.

## Step 6 — Follow-up plan (commit on Day 5)

The sprint produces tested patterns + a go/iterate/kill recommendation. The follow-up commits:

- Who picks up what, by when?
- Does this feed `manfred-discovery:opportunity-solution-tree`?
- Does this feed `manfred-design-systems:component-spec` (new components surfaced)?
- Does this feed `manfred-design-research:test-plan` (need a follow-up test)?

Without a follow-up plan, the sprint produces slides nobody acts on.

## Step 7 — Linear update

If a Linear project / ticket is in scope, post a comment via `mcp__linear-server__save_comment` with:

- Sprint dates + decision maker
- Challenge statement
- Daily schedule
- Day 5 recruit confirmation
- Pre-flight checklist status

## Wrap-up

Confirm the sprint plan covers:

- [ ] Sharpened challenge statement
- [ ] Decision maker committed for the full week
- [ ] Team assembled + schedules cleared
- [ ] Day 5 recruit confirmed (5 paid users)
- [ ] Per-day schedule (Day 1 → Day 5)
- [ ] Test plan drafted ahead (Day 5 questions known Day 1)
- [ ] Follow-up plan template ready (Day 5 morning fills it in)

Then offer:

> "Run sprint Monday. Day 5 results feed `/manfred-design-research:synthesize` for affinity clustering and `manfred-discovery:opportunity-solution-tree` for the OST. If results need a follow-up validation cycle, `/manfred-design-research:test-plan`."
