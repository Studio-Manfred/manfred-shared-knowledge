---
description: Hand off a finished design to engineering — pre-handoff review + token compliance check + handoff spec drafted + Linear post + walk-through scheduled.
argument-hint: [surface or feature, e.g. "Settings page redesign STU-100"]
---

You're handing off a design to engineering. The user mentioned: $ARGUMENTS

## Step 1 — Confirm the design is ready for handoff

Ask:

- **Is the design done?** All states (default · hover · focus · active · disabled · loading · error · empty)?
- **Linear ticket?** (Or branch name to extract from?)
- **Figma link?** (URL to the source of truth)
- **Engineer assigned?** (Name, time-zone, prior context with this surface)
- **Walk-through scheduled?** (15 min, sync or async via Loom)
- **Pre-handoff review run?** (`manfred-design-ops:design-review-process` Gate 3)

If the design isn't done — push back. Handoff before completion produces churn. Run pre-handoff review first.

## Step 2 — Pre-handoff review (`manfred-design-ops:design-review-process` Gate 3)

Run Gate 3 if not already done:

- All states designed
- Edge cases addressed
- Accessibility annotated (per `manfred-design-systems:a11y-design`)
- Tokens used (no hex, no default Tailwind palette)
- Existing Manfred components referenced (not custom from scratch)

If any criterion fails — iterate before handoff. Don't ship gaps.

## Step 3 — Token + component compliance check

Walk the Figma:

- Every colour resolves to a token from `~/.claude/shared/DESIGN.md`?
- Every spacing value maps to a Tailwind primitive (`p-2`, `gap-4`, etc.)?
- Existing Manfred components used where possible (Button, Dialog, FormField, Toast, etc. — Section 4 of DESIGN.md)?
- New components have a `manfred-design-systems:component-spec` written?

Phantom tokens (designed against tokens that don't exist yet) get surfaced — route through `manfred-design-systems:design-token` to either add the token or pick a different existing one. **Do not let a phantom token reach the handoff spec.**

## Step 4 — Draft the handoff spec (`manfred-design-ops:handoff-spec`)

Run the `manfred-design-ops:handoff-spec` skill to produce the tight (~300-word cap) intent + decisions + open questions doc.

Specifically:
- Intent (2-3 sentences)
- Decisions (layout, surfaces, type, components, spacing, states, responsive, motion — anchored to tokens)
- Accessibility (focus order, keyboard, SR labels, reduced motion, contrast)
- Edge cases in scope
- Out of scope
- Open questions

If you're past 300 words, audit each section — what could be cut to the Figma link instead?

## Step 5 — Post to Linear

If a ticket exists:

```
mcp__linear-server__save_comment(
  issueId: "STU-XXX",
  body: <the handoff spec from Step 4>
)
```

Confirm the comment was created. If posting fails, surface to the user — don't pretend it succeeded.

If no ticket — pause, follow the handoff-spec skill's no-ticket flow (push for ticket creation; or confirm internal-only; or save as draft).

## Step 6 — Schedule the walk-through

15-min sync between designer + engineer (or async via Loom + Linear-comment Q&A).

Capture the time in the handoff spec header. The walk-through is prep, not substitute — and not the spec being long enough to skip the conversation.

If user says "no time for a walk-through": offer the async equivalent. Loom-record a 5-10 min walkthrough + post link in the Linear comment + engineer comments async + designer resolves before they start.

## Step 7 — Confirm next-stage gates

The handoff sets up:

- **Engineering pickup** — engineer reads spec + Loom + Figma; asks questions in Linear before starting
- **Implementation QA** (`manfred-design-ops:design-qa-checklist` + `manfred-dev:test-my-code` + `manfred-design-systems:a11y-qa`) — runs pre-merge

Mention both to the user so the handoff's downstream is set.

## Wrap-up

Confirm the handoff covers:

- [ ] Pre-handoff review passed (Gate 3)
- [ ] All states + edge cases designed
- [ ] Tokens used; no hex, no Tailwind-palette bypass
- [ ] Existing Manfred components referenced
- [ ] Handoff spec posted to Linear (or saved with no-ticket flow followed)
- [ ] Walk-through scheduled (sync or async)
- [ ] Open questions surfaced
- [ ] A11y section is first-class, not footnote

Then offer:

> "Engineer should read spec + Loom + Figma before our walk-through. Run `/manfred-dev:test-my-code` once the build is up to gate against the design + a11y. If new tokens or components were added, queue a design-system PR via `manfred-design-systems:design-token` / `manfred-design-systems:component-spec`."
