---
description: Frame a design problem end-to-end — design brief + experience map + stakeholder alignment + metrics, ending in a signed brief the team can execute against.
argument-hint: [problem or engagement, e.g. "redesign the KYC flow for our fintech app, Q3 engagement"]
---

You're framing a design problem so the team can execute. The user mentioned: $ARGUMENTS

## Step 1 — Confirm the problem is real

Ask:

- What's the evidence the problem exists? (Research sessions, ticket patterns, analytics, churn data — specific. "We believe…" gets flagged.)
- Whose problem is it? (Specific user segment, named — and why this segment now.)
- What changes if we don't solve it? (Quantify if possible — revenue, churn, support load, brand cost.)
- Has anyone tried to solve it before? (What happened, why it didn't stick.)

If evidence is thin, **don't frame the problem yet**. Run `manfred-design-research:summarize-interview` or `manfred-design-research:affinity-diagram` first — framing on assumptions produces briefs that point the team at the wrong target.

## Step 2 — Map the experience (if multi-channel)

If the problem touches multiple touchpoints / channels, run `manfred-ux-strategy:experience-map` for current state:

- User actions across phases
- Touchpoints and channels
- Emotions, pain points, opportunities — evidenced
- Cross-team handoffs (often where the real friction lives)

This step is optional for narrow problems (single-screen redesign, single-flow optimisation).

## Step 3 — Align stakeholders (`manfred-ux-strategy:stakeholder-alignment`)

Before writing the brief, sort decision rights:

- Stakeholder map (influence × interest)
- RACI for the key decisions in this engagement
- Decision framework (which decisions need what process)
- Communication plan
- Feedback protocol

Decision rights decided **at kickoff, not during conflict**. The brief will reference this alignment doc.

## Step 4 — Pick metrics (`manfred-ux-strategy:metrics-definition`)

Define how the team will know whether the work landed:

- Hypothesis (what change in the design produces what change in user behaviour)
- 3–5 primary metrics across behavioural / attitudinal / business
- Baselines (current state values)
- Targets (where we're trying to get to)
- Action thresholds (what movement triggers what action)
- Qualitative companion (verbatims, spot interviews)

Without metrics, "did the work land?" becomes opinion. With them, it becomes evidence.

## Step 5 — Write the brief (`manfred-ux-strategy:design-brief`)

Now produce the brief. The brief pulls from:

- Step 1 evidence → Section 2 (Problem statement)
- Step 2 experience map → Section 6 (Context + inputs)
- Step 3 stakeholder map → Section 1 (Stakeholders) + decision framework
- Step 4 metrics → Section 4 (Goals + success criteria)
- The strategic frame → Section 5 (Scope + constraints)
- Manfred principle 6 → Section 8 (Ethics check) — non-negotiable

Save to `discovery/briefs/<engagement-slug>-<YYYY-MM-DD>.md`.

## Step 6 — Sign-off

The brief gets explicit sign-off from whoever's Accountable per the RACI. No sign-off, no kickoff. Verbal agreement is not shared understanding.

If the Accountable can't sign off, surface what's blocking — usually a missing piece (more research, missing stakeholder, unclear decision rights). Fix that first.

## Step 7 — Capture assumptions

Every brief has assumptions stated as facts. Pull them into Section 9 (Assumptions to test) and route to `manfred-discovery:assumption-test` for week 1 of the engagement.

## Step 8 — Linear update

If a Linear ticket is in scope, post a comment via `mcp__linear-server__save_comment` with:

- Path to the signed brief
- Top 3 assumptions to test in week 1
- The success metric set
- Stakeholder map summary

## Wrap-up

Confirm the framing covers:

- [ ] Evidence-led problem statement (not "we believe…")
- [ ] Experience map (if multi-channel)
- [ ] Stakeholder alignment with decision rights
- [ ] Measurable success criteria with baselines
- [ ] Signed brief
- [ ] Ethics check
- [ ] Assumptions identified for week-1 testing

Then offer:

> "Run `/manfred-discovery:weekly` to start the discovery cadence — assumption tests in week 1, opportunity-solution tree by end of week 2. Or `/manfred-design-research:discover` for the research side."
