---
name: interview-script
description: Use when preparing a customer interview script — discovery, usability, or both. Triggers on "interview script", "interview prep", "discovery interview", "usability interview", "user research script", "customer conversation guide", "write me a script for tomorrow's session", "interview questions for X". Refuses to mix discovery + usability in one script. Refuses leading and hypothetical questions.
---

# interview-script

A customer interview script that produces evidence, not opinions. Past behaviour beats hypothetical futures. One method per session, every time.

## Overview

Most interview scripts produce thin data because they ask the wrong shape of question. "Would you use…?", "How helpful is…?", "What do you think of…?" — all invite the participant to speculate, flatter, or guess. Past behaviour predicts future behaviour. Opinions don't.

This skill writes scripts that:

- Force story-based questions ("tell me about the last time you…") over hypothetical ones
- Refuse leading and multi-part questions
- Separate **discovery** (open exploration of context, jobs, pain) from **usability** (task-based observation of behaviour with an artifact) — they need different scripts
- Build in Trio attendance, recording protocol, probing techniques, and a real wrap-up
- Treat compensation as non-negotiable

Source: Steve Portigal, *Interviewing Users*; Teresa Torres, *Continuous Discovery Habits* (story-based interviewing chapter); Erika Hall, *Just Enough Research*; Rob Fitzpatrick, *The Mom Test*.

## When to use

- "Write me an interview script for tomorrow's session"
- A `manfred-discovery:customer-touchpoint-plan` is being filled in and each customer needs a per-conversation brief
- A `manfred-design-research:usability-test-plan` is being executed and needs the actual moderator script
- Fresh discovery research — first script for a new outcome

**Skip when:**

- The conversation is a sales call, support call, or 1:1 catch-up — different rules entirely
- The session is observational only (in-context shadowing without prompting) — script gets in the way
- The participant is internal (employee, stakeholder) and you really mean a stakeholder interview — use a different format

## Two principles drive everything

1. **Past behaviour beats hypothetical.** Replace nearly every "would you…?" / "how helpful…?" with "tell me about the last time you…". The Mom Test rule: ask about their life, not your idea.
2. **One method per session.** Discovery and usability are different methods with different goals. Discovery wants context, jobs, motivations. Usability wants behaviour against a specific artifact. Bolting them into one 45-minute conversation produces shallow versions of both. Pick one. If you genuinely need both, run two sessions (or the same participant twice).

## Phase 1 — Refuse to write without context

If asked to write a script with no context, ask first. The agent's job here is to slow the user down for 90 seconds before producing output that's worth using. Ask:

- **What's the method?** Discovery (open) or usability (task-based) — pick one. If user says "both," push back: name the primary one for this session, offer to script the second separately.
- **What outcome / opportunity / assumption is this serving?** If the answer is "we just want to talk to users," that's a smell — push for at least one specific thing the team wants to learn. If the script can't say "after this conversation we'll know X better," it's tourism not research.
- **Who's the participant?** Recruit segment, behavioural criteria, recency of using the product. "Recent users" is too broad.
- **Trio attending?** PM + designer + tech lead. If only the user is attending, mark sections as provisional and recommend rescheduling for Trio attendance where possible.
- **Recording protocol?** Tool, consent, transcript flow. If "we'll just take notes," recommend recording (with consent) — note-taking misses 80% of the verbatim that matters.
- **Compensation?** What are they paid? If "nothing" — refuse. Recommend at minimum the local-equivalent of one hour of fair work for a 45–60 min session.

**Wait for answers before producing anything.** If — after explicit pushback — the user genuinely re-declines and insists on script-only, produce a minimal version with the gaps marked **`TBD`** and a one-line recommendation per gap. Don't fake the answers, and don't go to the escape hatch on the first ask.

## Phase 2 — Pick the script shape

### Discovery script (45–60 min)

Goal: understand the participant's world, jobs, current behaviour, frustrations. No artifact required.

| Section | Time | Purpose |
|---------|------|---------|
| Warm-up | 3–5 min | Real warm-up, not just "tell me about yourself" — get them into story mode |
| Context | 10 min | Their world, business, role, related tools |
| Core exploration | 25–30 min | Story-based questions about the relevant jobs / pains / current behaviour |
| Wrap-up | 5 min | Anything we missed, referral ask, follow-up consent |

### Usability script (30–45 min)

Goal: watch behaviour against an artifact (prototype, live product, design). Tasks first; interpretation after.

| Section | Time | Purpose |
|---------|------|---------|
| Intro + warm-up | 3 min | Set the contract: "Think aloud. Nothing you say is wrong. We're testing the design, not you." |
| Pre-task context | 5 min | A few story-based questions about how they currently do this work |
| Tasks (3–5) | 20–30 min | Realistic task scenarios. Observe; don't explain. |
| Debrief | 5–10 min | What was confusing, what they expected, what was missing |
| Wrap-up | 2 min | Compensation handover, follow-up consent |

### "Both" — push back, then escape hatch only if they insist

The principle is one method per session. If the user insists on combining after you've recommended splitting into two sessions, produce a discovery-leaning script with a 10-minute usability mini-task at the end. Name the trade-off explicitly in the front matter ("This script trades depth for breadth — combined-method session at user's request"). Don't go to the escape hatch on the first ask.

## Phase 3 — Write the questions (the rules)

**Always:**

- Story-based form: "Tell me about the last time you…", "Walk me through what you did when…", "Show me how you usually…"
- One question per breath — no multi-parts
- Neutral wording — "How did that feel?" not "Was that frustrating?"
- Concrete past time — "the last time" / "the most recent" beats "usually" or "in general"
- Curiosity over confirmation — assume nothing; let them surprise you

**Never:**

- Hypothetical-future ("Would you use…?", "What if we built…?", "Would you pay…?")
- Leading ("How helpful is the dashboard?", "How frustrating is X?")
- Multi-part ("What do you do, how often, and why?")
- Solution-validation ("Does this make sense?", "Is this clear?")
- Compound assumptions ("When you log in to use the dashboard for your weekly report…")

**Probing toolkit** (include in facilitator notes for every question):

- "Tell me more about that."
- "What do you mean by [their word]?"
- Repeat their last few words back, with a small upward inflection.
- Wait. 4 seconds of silence usually pulls more than the next question.
- "Can you give me an example?"
- "What happened next?"

## Phase 4 — Trio + capture protocol

Every script ships with these two sections specified:

**Trio roles for the session:**

- **Moderator** (usually PM or designer): asks the questions, drives the conversation
- **Note-taker** (any of the Trio): captures verbatim quotes, behavioural observations, time-stamps for the recording
- **Observer / second note-taker** (any of the Trio): patterns across the session, follow-up question candidates that the moderator missed

If only one or two Trio members attend, name which roles are uncovered and recommend rescheduling. The asymmetry (PM-only research with everyone catching up via transcript) is one of the highest-frequency failure modes in continuous discovery — the team doesn't reach the same conclusions, so it doesn't act as a team.

**Recording + capture:**

- Recording tool (Tella, Otter, Riverside, Zoom local, etc.) — named explicitly
- Consent line at the start of the session — exact wording in the script
- Where the transcript goes — folder path, naming convention
- How quotes get extracted into the synthesis — pointer to `manfred-design-research:summarize-interview`

## Phase 5 — Output

Save the script to `discovery/scripts/<participant-or-session-slug>-<YYYY-MM-DD>.md`. Use this template:

```markdown
# Interview script — [Participant first name, segment]

**Session date:** [YYYY-MM-DD], [time + timezone]
**Method:** Discovery / Usability (one — not both)
**Outcome / assumption being served:** [one line]
**Trio attending:** [Moderator name] · [Note-taker name] · [Observer name or "absent — note-taker covers"]
**Recording:** [tool, consent confirmed yes/no]
**Compensation:** [amount + format + handover plan]
**Linked artifacts:**
- Touchpoint plan: [path]
- OST opportunity probed: [link]
- Assumption test (if usability): [path]

## Consent (read aloud at the start)

> "Thanks for joining. We're going to record this so we can listen properly without taking too many notes. The recording stays internal to the team, and we'll delete it after [N weeks]. We may quote you anonymously in our research summary. Are you OK with that?"

[Wait for explicit "yes" before continuing.]

## Section 1 — Warm-up (3–5 min)

> [Warm-up question — short, low-stakes, not "tell me about yourself"]

**Probe if needed:** [...]

## Section 2 — [Context / Pre-task context] (5–10 min)

> [Question 1 — story-based]
> _Probe: [tell-me-more / example / silence]_

> [Question 2 — story-based]
> _Probe: [...]_

## Section 3 — [Core exploration / Tasks] (20–30 min)

[For DISCOVERY: 4–6 story-based questions about the specific opportunity / job / pain. Each with probes.]

[For USABILITY: 3–5 task scenarios. Each scenario reads as: "You want to [task] — show me how you'd do it." NOT "click on the dashboard and tell me what you think."]

> [Task / question 1]
> _Probe: [...]_
> _Observation focus: [what to watch for — specific behaviour, not "usability issues"]_

## Section 4 — [Wrap-up / Debrief] (5–10 min)

> "Anything I didn't ask about that you think we should know?"
> "Is there someone else doing this kind of work who you think we should talk to?" [Referral ask]
> "Would you be open to us coming back in a few months as we learn more?" [Follow-up consent]

## Section 5 — Compensation handover (2 min)

[How they get paid — gift card link, bank transfer note, etc. Handle this before the call ends.]

## Facilitator notes

- **Embrace silence.** 4 seconds of waiting usually pulls more than the next question.
- **Don't explain the design** if they're confused — observe the confusion, that's the data.
- **Don't sell the product.** Stay curious; resist the urge to defend or pitch.
- **Watch for "I think" / "I'd probably"** — those are speculation, not evidence. Redirect: "Has that actually happened? Tell me about that time."
- **End on time.** Respect the booking. Cut a section short if needed.

---

*Adapted structure from [Owl-Listener/designer-skills/design-research/skills/interview-script](https://github.com/Owl-Listener/designer-skills/tree/main/design-research/skills/interview-script) under MIT licence. Voice, story-based discipline, Trio protocol, and Manfred-specific guidance are original.*
```

## Manfred lens

- **Research isn't a phase** (principle 2) — every script ties back to a specific opportunity / assumption from the OST, not a one-off "let's go talk to users"
- **Customer-driven always** (principle 1) — the script's job is to make customer evidence beat team hunches
- **Accessible first** (principle 5) — recruit guidance includes disabled and neurodiverse participants; for usability, include AT users where relevant
- **Critical & ethical** (principle 6) — observation focus includes "where could this design do harm or coerce?"

## Cross-plugin handoffs

- **Input from `manfred-discovery:customer-touchpoint-plan`** — the per-conversation brief; this skill produces the actual script
- **Input from `manfred-design-research:usability-test-plan`** — when the script is for the usability portion
- **Output to `manfred-design-research:summarize-interview`** — once the recording exists
- **Output to `manfred-design-research:affinity-diagram`** — when synthesis crosses multiple interviews
- **Output to `manfred-discovery:opportunity-solution-tree`** — synthesis updates opportunities and assumption test status
- **Output to `manfred-discovery:assumption-test`** — qualitative signal feeds into the test result

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "Just write the script, I'll figure context out later" | The script you write without context is the wrong instrument. 90 seconds of clarifying questions changes the output. |
| "We need both discovery and usability in 45 minutes" | You'll get shallow versions of both. Pick one for this session, schedule a second. If you must combine, name what you're trading. |
| "The participants will love being asked what they think" | They will. And the data will be unreliable. People are bad at predicting their own behaviour. Ask about past behaviour. |
| "Story-based questions are too constraining" | The constraint is the point. It's the difference between "evidence" and "opinion." |
| "We don't have time for the Trio to attend" | Then reduce the participant count, not the Trio. Trio symmetry beats interview volume for team decision-making. |
| "Skip recording, just take notes" | Notes miss 80% of the verbatim that matters. Recording (with consent) is the default. |
| "Free participants are fine — they volunteered" | Volunteers self-select for opinions, not behaviour. Pay people. Always. |
| "How helpful is X?" is a fine question | It's a leading question. Replace: "Tell me about the last time you used X." |
| "We can call it 'gentle leading' to confirm what we already know" | Then you're not researching — you're seeking validation. Different exercise; rename and own it. |
| "I have a meeting in 10, just write the script fast" | A 10-minute hasty script wastes 45 minutes of participant time tomorrow plus everyone's analysis time after. The fast version is to send back 5 clarifying questions and reschedule the script writing. |
| "Session is tomorrow, I'll sort recruit / Trio / recording / pay in the morning" | Tomorrow-morning logistics aren't viable. Recruit changes need lead time. Trio calendars need lead time. Pay needs admin lead time. If those genuinely aren't ready, **the session itself isn't ready** — reschedule, or run as exploratory ("we're not synthesising findings from this") and label clearly. Don't smuggle a not-ready session into the OST as evidence. |

## Red flags — STOP

- About to write a script without asking what assumption it's serving → Stop. Phase 1 first.
- About to use any "would you" / "what if we" / "how helpful is" question → Stop. Restate as story-based.
- About to combine discovery + usability without flagging the trade-off → Stop. Pick one or split sessions.
- About to skip Trio / recording / compensation sections from the output → Stop. Mark as `TBD` with a one-line recommendation; don't omit.
- About to recommend a script for free participants → Stop. Refuse, recommend pay.
- About to omit the consent line from Phase 5's template → Stop. It's recorded research; consent is not optional.
- About to write more than 6 questions in Section 3 of a discovery script → Stop. You'll never get through them. Cut to the 4 highest-value.

## Tools used

- **Read** + **Write**: `discovery/scripts/<slug>-<date>.md`
- **Skills called**:
  - `manfred-design-research:summarize-interview` — once the recording exists
  - `manfred-discovery:customer-touchpoint-plan` — for the recruit and Trio scheduling
  - `manfred-discovery:opportunity-solution-tree` — for the linked opportunity / assumption
- **References**: Steve Portigal, *Interviewing Users*; Teresa Torres, *Continuous Discovery Habits* (story-based interviewing); Rob Fitzpatrick, *The Mom Test*; Erika Hall, *Just Enough Research*

---

*Adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT). Story-based discipline, Trio protocol, Phase 1 refusal-without-context, and Manfred-specific guidance are original.*
