---
name: product-brief
description: Use when someone wants to write a product brief, PRD, feature spec, kick off a feature, or shape an opportunity before it moves to the roadmap. Triggers on "product brief", "PRD", "write a brief", "shape this feature", "kick off a feature", "feature spec", "move to roadmap", "define what we're building". Produces an 8-section brief (Opportunity → Strategic Alignment → Hypothesis → Success Metrics → Cagan Risks → Scope → Dependencies → Recommended Next Step). Co-shaped, not form-filled.
---

# product-brief

A facilitator for shaping an opportunity into a product brief the team can act on. Not a form. A conversation.

## Overview

A good brief does three things:

1. Makes the **problem** concrete from the customer's view, before any solution.
2. Makes **assumptions explicit** so the team knows what to learn.
3. Names the **right next step** — which is usually discovery, not build.

The PM owns the brief. You facilitate. The tech lead and designer are equal voices in the room — each sees something the others can't.

## When to use

- Someone wants to move an opportunity onto the roadmap and needs a brief first
- "Let's write a PRD / brief / feature spec for X"
- The team needs to align on problem, hypothesis, and next step before committing to build
- An existing brief needs to be deepened or updated

**Skip when:**

- Writing technical architecture or API specs (those come after the brief)
- Incident reports, bugs, sprint planning
- User stories for an already-approved initiative — use `superpowers:writing-plans` instead

## Two principles drive everything

1. **Problem first.** Describe the problem from the customer's view, not the solution. If you can't, you're not ready.
2. **Assumption made explicit.** If the hypothesis is incomplete, the initiative is not ready to move forward. Period.

## The shape

| Phase | What happens | Output |
|-------|-------------|--------|
| 1. Set the stage | Who's in the room, what we're shaping, what's already known | Context |
| 2. Walk the 8 sections | One at a time. Conversation, not form. | Aligned decisions |
| 3. Generate the brief | Markdown file, kebab-case filename | `<initiative-name>-brief.md` |

## How the conversation works

### Phase 1 — Set the stage

Start by understanding who's in the room and how far the thinking has gone:

- "Who's in the session — just you, or are the tech lead and designer here?"
- "What's the initiative called, even if it's a placeholder?"
- "Where are we — fresh opportunity, or already had a few discussions?"
- "Do we know who'll own the analytics for the success metrics, or is that a gap?"

If only the PM is present, play devil's advocate for the missing roles and mark their sections as provisional. When multiple roles are present, direct questions explicitly: **"Question for the tech lead:"**, **"Designer, what's your take on…"**. The PM is your primary partner — when the team disagrees, the PM's call is final.

### Phase 2 — Walk through the 8 sections

Work through sections in order. Don't dump everything at once. Ask one or two questions, listen, follow up if the answer is vague, then move on. Signal which section you're on so the PM can track progress.

---

**01 · The Opportunity — Problem First**

Everything flows from the problem. If this section is vague, stop and fix it before going further.

- **Problem statement.** "What's the customer or business problem we're solving? Describe it from the customer's view — not the solution." Push back on any answer that starts with "we need to build…" — that's a solution, not a problem.
- **Why now.** "What makes this the right moment? Commercial pressure, strategic window, competitive signal?"
- **Evidence & signals.** "What data, research, or customer feedback tells us this problem is real?" Probe for: drop-off analytics, support tickets, NPS verbatims, session recordings, interview quotes.
- **Scale of the opportunity.** "How many customers does this affect? Niche edge case or core journey?" Quantify if possible.

---

**02 · Strategic Alignment — Why Us, Why Now**

The brief must tie to a current company OKR or strategic objective. If it doesn't, it's a candidate for deprioritisation.

- **Primary objective / OKR.** Ask the PM: "Which one objective does this serve? Pick one — not three."
- **Key result.** "Which specific KR does this move? Concrete expected contribution — e.g. 'two to three points toward the conversion uplift target' or 'sign-up rate from X% to Y%'."

If the company doesn't run on OKRs, substitute the equivalent (strategic pillar, north-star metric, quarterly priority). Push for *one* objective, not several.

---

**03 · The Hypothesis — Assumption Made Explicit**

This is the gate. If the PM cannot complete all three parts, the initiative is not ready to move forward — say so plainly and help them work on it.

Capture the hypothesis in three parts:

- **WE BELIEVE THAT** [this change or solution]
- **WILL RESULT IN** [this measurable customer or business outcome]
- **WE WILL KNOW WHEN** [we observe this signal or metric movement]

Then pull out the **Key Assumptions** — the things that must be true for the hypothesis to hold. Push for the assumptions most likely to be wrong, because those become the discovery priorities. Common areas: user willingness, technical feasibility, data quality, downstream business impact.

> **Hand-off hook:** the assumptions identified here feed directly into `manfred-discovery:assumption-test` for designing the cheapest test for each one. Mention this when you finish the section.

---

**04 · Success Metrics — How We Know It Worked**

Require at least one of each before the brief is approved. Nothing fluffier than a number with a baseline and a target.

| Type | What it is | Example |
|------|-----------|---------|
| **Leading** | Early signal, moves before revenue | Sign-up rate (12% → 20% within 60 days post-launch) |
| **Lagging** | Business outcome, takes time to move | New paid members per month (~4,200 → +15% within Q2) |
| **Guardrail** | What we must not break | Existing conversion rate must not drop below current baseline |

Then cover **Tracking Readiness** — this is where briefs often die in execution.

> The PM owns the question — what to measure and why. Analytics owns the answer quality — whether it can be measured reliably. Both have to be confirmed before the brief is approved.

- "Are these metrics trackable today?" Classify each as:
  - ✓ Confirmed with analytics
  - ! Needs implementation
  - ✗ Not currently trackable
- "Who's the analytics contact who has reviewed this?" Get a name.
- "Any notes on tracking approach or gaps?" Probe for event coverage, query availability, dashboard ownership.

If the PM doesn't know the analytics contact, capture it as an open question. Don't let the brief pretend tracking exists when it doesn't.

---

**05 · Product Risk Assessment — Cagan's Four Risks**

Rate each risk Low / Med / High, with a one-line note. **High risk in any area means discovery must happen before development.** Hold the line on this — it's the whole point of the section.

- **Value risk.** "Will customers actually want this?" (signal quality, qualitative feedback, willingness-to-pay)
- **Usability risk.** "Can people figure out how to use it?" (novel interaction, unfamiliar pattern, needs prototyping)
- **Feasibility risk.** "Can we build it with current tech?" → **Question for the tech lead.** (API dependencies, rework needed, unknown spike)
- **Viability risk.** "Does it work for the business?" (legal, GDPR, brand, commercial model, operational impact)

Challenge any rating that doesn't include a reason. "Low risk" with no note isn't useful.

> **Hand-off hook:** for any High-risk rating, recommend `manfred-discovery:cagan-risks` for a deeper risk profile and `manfred-discovery:assumption-test` to design a test that retires it. The recommendation in section 08 should reference the deepest risk.

---

**06 · Scope — What's In, What's Out**

Most briefs fail here because out-of-scope is left implicit. Force explicit boundaries.

- **In scope.** "What we believe is within the problem space of this initiative." Be concrete about surfaces (mobile web, desktop, app, internal tooling).
- **Out of scope.** "What stakeholders might expect but we're deliberately not solving here. Being explicit prevents later conflict." Push the PM to name at least 2–3 adjacent things that could be confused with this work.
- **Open questions.** "What do we still not know?" These feed directly into discovery scope. Every unanswered item from earlier sections (especially risks and assumptions) lands here.

---

**07 · Dependencies & Stakeholders — Who Else Needs to Be Involved**

- **Team & system dependencies.** Other teams, APIs, or systems this relies on. Surface surprises early — they're expensive later.
- **Key stakeholders.** Not everyone with an opinion — only those whose input changes the outcome.

Capture each as `Name — Role — Why they matter`.

---

**08 · Recommended Next Step — What Happens After This Brief**

This is the **PM's call, not leadership's.** Be specific. "Build it" is rarely the right answer for a brief — discovery usually is.

Good next-step language:

> "Recommend Solution Discovery. The problem is well evidenced. Value risk and feasibility risk both need validation before committing to build. Suggest 2-week spike with designer + tech lead, targeting one testable prototype."

Close by confirming the PM's recommendation with the team. If risks in section 05 are High and the recommendation is "build", flag the contradiction.

> **Hand-off hooks (use the right one):**
>
> - Discovery recommended? → `manfred-discovery:opportunity-solution-tree` to map opportunities and start identifying tests; `manfred-discovery:weekly` to set up a continuous discovery rhythm.
> - Build recommended (and risks genuinely Low)? → hand off to engineering, point at `manfred-dev:test-my-code` for the QA gate before merge.
> - Park recommended? → record reasoning, log a follow-up to revisit when conditions change.

### Phase 3 — Generate the brief

Once all 8 sections have been covered (some may be thin — that's fine, flag them as such), say:

> "I've got enough to draft the brief. Let me put it together — you can review and tell me what to adjust."

Generate the document using the template below. Save it as a markdown file in the current working directory, named `<initiative-name>-brief.md` in kebab-case. After saving, share the file path and offer:

- "Want to deepen any section?"
- "Should I pull the open questions into a separate discovery backlog?"
- "Ready to share this with the stakeholder group?"

## Document template

Use this exact structure. Sections that are genuinely unknown should say **"To be defined"** rather than be skipped — that itself is useful signal.

```markdown
# [Initiative Name]

**Product Manager:** [Name]
**Date:** [Month YYYY]
**Version:** v0.1 (Draft)
**Status:** Draft | In Review | Approved
**Contributors:** [names and roles]

---

## 01 · The Opportunity

### Problem statement
[From the customer's view — not the solution.]

### Why now
[Commercial pressure, strategic window, competitive signal.]

### Evidence & signals
[Data, research, customer feedback. Bullet the sources.]

### Scale of the opportunity
[How many customers this affects. Quantify.]

## 02 · Strategic Alignment

**Primary objective / OKR:** [the one objective this serves]

**Key result this moves:** [Named KR + expected contribution, or new-KR proposal with from/to numbers.]

## 03 · The Hypothesis

- **We believe that** [this change or solution]
- **Will result in** [this measurable customer or business outcome]
- **We will know when** [we observe this signal or metric movement]

### Key assumptions
1. [Assumption most likely to be wrong — a discovery priority.]
2. [...]
3. [...]

## 04 · Success Metrics

| Type | Metric & current baseline | Target |
|------|---------------------------|--------|
| Leading | [metric — baseline] | [target — timeline] |
| Lagging | [metric — baseline] | [target — timeline] |
| Guardrail | [metric — baseline] | [must-not-break threshold] |

### Tracking readiness

- **Are these metrics trackable today?** [✓ Confirmed / ! Needs implementation / ✗ Not currently trackable]
- **Analytics contact confirmed:** [Name]
- **Notes on tracking approach or gaps:** [event coverage, query availability, dashboard ownership.]

## 05 · Product Risk Assessment (Cagan's Four Risks)

| Risk | Rating | Note |
|------|--------|------|
| **Value** — Will customers want this? | Low / Med / High | [one line] |
| **Usability** — Can they figure it out? | Low / Med / High | [one line] |
| **Feasibility** — Can we build it? | Low / Med / High | [one line] |
| **Viability** — Does it work for the business? | Low / Med / High | [one line] |

> High risk in any area means discovery must happen before development.

## 06 · Scope

### In scope
- [item]

### Out of scope
- [adjacent thing we are deliberately not solving]

### Open questions
- [ ] [Unresolved question — feeds discovery scope]

## 07 · Dependencies & Stakeholders

### Team & system dependencies
- [System / team — owner — why it matters]

### Key stakeholders
- [Name — Role — Why their input changes the outcome]

## 08 · Recommended Next Step

**Recommendation:** [e.g. Solution Discovery / 2-week spike / Move to build / Park]

[2–4 sentences explaining why this is the right next move, referencing the risks and evidence above. PM's call.]

---
```

## Handling different starting points

**"We already have a rough brief"** — Ask to see it. Read it, map content onto the 8 sections, identify gaps, focus the conversation on the weakest sections.

**"We just have a vague idea"** — Fine. Spend more time on section 01 (Opportunity) and section 03 (Hypothesis). It's OK if the first draft has many "To be defined" entries — the point is to capture what's known and surface what isn't. A brief with honest unknowns beats a brief with fake confidence.

**"We already know we're going to build it"** — Still run the brief. If Cagan risks are High, push back on the build decision. A brief that rubber-stamps a premature build is worse than no brief.

**"Someone else wrote this and I'm updating it"** — Read the existing document. Focus the conversation on changes since the last version, new evidence, and shifted risks. Bump the version number.

## Tone and facilitation style

- **Be direct.** If an answer is vague, say so: "That's broad — can you name the specific segment and volume?"
- **Challenge gently but firmly.** "You said customers want this — what's that based on? NPS verbatim, analytics, or a hunch?"
- **Mediate tradeoffs.** "Tech lead is saying the integration is a spike; designer wants a single state. What if we…"
- **Keep momentum.** If a question is generating more heat than light, park it as an open question and move on.
- **Celebrate clarity.** When the team lands on a crisp problem statement or explicit out-of-scope item, acknowledge it. That's the whole job.
- **Hold the gates.** The hypothesis gate and the High-risk-means-discovery gate are not negotiable. If the PM tries to paper over them, name it.

## Common mistakes

| Mistake | Why it matters |
|---------|----------------|
| Dumping all 8 sections at once | Conversation, not form-filling. Walk them one at a time. |
| Accepting a solution as a problem statement | "We need a new check-in flow" is a solution. "Customers abandon at step 3" is a problem. Push back. |
| Letting the hypothesis be incomplete | If WE BELIEVE / WILL RESULT IN / WE WILL KNOW WHEN isn't all filled in, the initiative isn't ready. Say so. |
| Treating "low risk" with no note as an answer | Every risk rating needs a one-line reason. |
| Skipping tracking readiness | A success metric with no analytics owner is aspirational, not measurable. |
| Defaulting to "build" in the next step | Discovery is usually the right answer for a brief. Build is right when risks are Low and evidence is strong. |
| Ignoring missing roles | When designer or tech lead is absent, play devil's advocate and mark their answers as provisional. |

## Red flags — STOP

- About to skip section 01 because the PM has a "great idea" → No. Problem first. Always.
- About to accept a hypothesis with one of the three parts blank → No. Stop and complete it before moving on.
- About to mark all four Cagan risks Low without a single note → No. That's not an assessment, that's a wish.
- About to recommend "build" with a High-risk rating in section 05 → No. Flag the contradiction. Recommend discovery.
- About to dump the full template at the start of the conversation → No. One section at a time.

## Tools used

- **Write**: the brief markdown file in the working directory
- **Skills called next** (depending on section 08 outcome): `manfred-discovery:cagan-risks`, `manfred-discovery:opportunity-solution-tree`, `manfred-discovery:assumption-test`, `manfred-discovery:weekly`, `manfred-dev:test-my-code`
- **Skill it replaces**: the older `manfred-product:brief-prd` (Scandic-specific) — `manfred-product` was removed in v1.0.0.
