---
name: ux-writing
description: Use when writing UI copy — anyone says "write microcopy", "write error messages", "write button labels", "write empty state copy", "write onboarding copy", "write CTAs", "write a tooltip", "ux writing", "interface copy", "drop-in copy for the app". Manfred-specific: voice rules from `shared/manfred-brand.md` enforced; refuses generic-SaaS-friendly tics; demands real failure-mode context for errors.
---

# ux-writing

Manfred's voice is warmer-and-stranger-than-friendly. Conversational fragments, direct second person, concrete over abstract, no marketing verbs, no forced levity. UI copy carries that voice — every microcopy moment, every error message, every button label.

This skill refuses generic-SaaS-friendly tics ("Oops!", "Hmm,", "Yikes!", "Let's get you started!") and demands real context before writing error copy. Error messages without knowing the actual failure mode are guesses; guesses ship as user confusion.

## Overview

Manfred UI copy follows three rules:

1. **Voice from `shared/manfred-brand.md`** — fragments OK, Q&A beat OK, no marketing verbs, no corporate adjectives, no chirpy levity
2. **Errors explain, don't blame** — what happened / what to do / one clear action; user is never the subject of the failure
3. **CTAs are specific verbs with outcomes** — "Get in touch" not "Submit"; "Save changes" not "Save"; the button names what happens

Categories covered: microcopy, error messages, empty states, confirmation messages, onboarding copy, CTAs, tooltips, placeholder text.

## When to use

- Writing UI copy for any Manfred-built or Manfred-adjacent product
- Reviewing existing copy for voice compliance
- Translating product strings (Swedish ↔ English; the voice rules apply in both)
- Designing new states (loading, error, success, empty) where copy is part of the design
- Defining CTAs in a `manfred-design-systems:component-spec` or `manfred-design-ops:handoff-spec`

**Skip when:**

- The user wants long-form writing — case studies (`manfred-toolkit:case-study`), LinkedIn posts (`manfred-toolkit:linkedin-*`), design rationale (`manfred-toolkit:design-rationale`)
- The user wants brand strategy / messaging architecture (different scope — out of plugin)
- The user wants legal copy (terms of service, privacy policy — defer to legal counsel)

## Pre-flight (do this every time)

Two reads before drafting:

```bash
test -f ~/.claude/shared/manfred-brand.md && head -200 ~/.claude/shared/manfred-brand.md
```

Find:

1. **The Register** — fragments, shrug ellipsis, direct second person, concrete over abstract, self-deprecating
2. **Anti-patterns** — marketing verbs, corporate adjectives, "we're passionate about…", forced levity, hedging
3. **Manfred Vocabulary** — Manfred Magic, the Mmmms, peeps, Ping us

If `~/.claude/shared/manfred-brand.md` is unreadable, ask the user to install `manfred-shared-knowledge` or paste the relevant sections. **Do not draft copy without the voice doc — the failure mode is generic-SaaS-friendly that reads "fine" but isn't Manfred.**

## The hard rules

| Rule | What it means |
|---|---|
| **Voice from brand doc** | Every output passes against `shared/manfred-brand.md` voice rules. Read aloud — would I cringe? Rewrite. |
| **No marketing verbs** | Never: *transform, empower, leverage, unlock, supercharge, drive, deliver value*. Always: *do, build, make, ship, help, teach, research*. |
| **No corporate adjectives** | Never: *cutting-edge, world-class, innovative, best-in-class, passionate*. Confidence is shown, not claimed. |
| **No forced levity** | Never: "Oops!", "Hmm,", "Yikes!", "Whoops!", "Ta-da!", "Welcome aboard!", excessive "!", "let's get you started!". Manfred is warmer-and-stranger, not chirpy-customer-success. |
| **No hedging** | Never: "we might be able to…", "perhaps you could…", "if you'd like to…". Direct second person. |
| **Errors explain, don't blame** | Structure: **what happened** + **what to do next** + **one clear action**. User is never the subject of "you entered…" / "you forgot…". The system describes the condition. |
| **Context-required for errors** | Don't write error copy without knowing: real failure condition (specific HTTP status, specific validation rule), what the user was trying to do, what action would actually fix it. Generic "something went wrong" is the failure mode this skill exists to prevent. |
| **CTAs are specific verbs with outcomes** | "Get in touch" not "Submit". "Save changes" not "Save". "Send invite" not "OK". The button names what happens. |
| **Direct second person** | "Check your email" not "An email needs to be checked". "You're signed in" not "Sign-in successful". |
| **Concrete over abstract** | "Messy scale-ups, suit-heavy orgs" not "mid-sized to enterprise clients". "Save changes" not "Save". |
| **Sentence case** | "Save changes" not "Save Changes". Title case is for headings; UI labels are sentence case. |

## The flow

### Step 1 — Confirm context

Ask if not stated:

- **What's the surface?** (Form, button, error toast, empty state, onboarding screen?)
- **What's the user trying to do?** (Action; not just "fill out a form" — *why* is the form there?)
- **For errors: what's the real failure mode?** (Specific HTTP status, specific validation rule, specific server condition. "Server error" isn't a failure mode — 500 vs 503 vs rate limit vs auth-expired all need different copy.)
- **For success: what comes next?** (Redirect? Verify email? Onboarding? Dashboard? The success copy points to the next action.)
- **Stack / locale?** (English? Swedish? Both? Manfred ships parity where the product supports both.)

If the user says "quick is fine" or "just give me drop-in copy" — push back. Copy without context is copy that gets rewritten. And the version that *doesn't* get rewritten is worse — generic "Something went wrong" copy lives in production for years because nobody opens a ticket to fix copy that technically works. The cost of guessing isn't 30 minutes of revision; it's permanent generic-SaaS-friendly drift.

### Step 2 — Draft against the voice rules

For each piece of copy:

1. Read the brand voice doc section in your head (or open it again)
2. Draft the copy
3. Run it through the anti-patterns lint:
   - Any marketing verbs? Rewrite.
   - Any corporate adjectives? Rewrite.
   - Any forced levity ("Oops!", "Hmm,")? Rewrite.
   - Hedging ("we might…")? Rewrite.
   - Read aloud — cringe? Rewrite.
4. Check structure for the category (errors: what/do/action; CTAs: verb + outcome; empty states: explain + guide + CTA)

### Step 3 — Categories

#### Microcopy
- **Button labels** — verb + outcome. Examples: "Save changes", "Send invite", "Delete account". Forbidden: "OK", "Submit", "Done" (when ambiguous).
- **Form labels** — clear, no jargon. "Email address" not "E-mail Adresse" (well, that's German). "Phone number" not "Telephonic contact".
- **Tooltips** — brief explanations for complex features. Don't tooltip the obvious.
- **Placeholder text** — example format, not instructions. `e.g. lina@studiomanfred.com` not `Enter your email here`.

#### Error messages
Structure: **what happened** + **what to do** + **one clear action**.

- **What happened** — describe the condition, not blame the user. "We can't reach our servers right now" not "You're offline".
- **What to do** — specific. "Check your connection and try again in a minute" not "Try again later".
- **One clear action** — single CTA. "Try again" or "Contact support" — not both as equal options.

Anti-pattern: "Something went wrong. Please try again." This message tells the user nothing. Refuse to ship it. Demand the real failure condition.

Examples (with context):
- 500 from auth service: "Sign-in is having trouble on our side. Try again in a minute, or **contact support** if it keeps failing."
- 429 rate limit: "Too many sign-in attempts. Try again in 5 minutes."
- 401 expired session: "You've been signed out. **Sign in again** to continue."
- Network offline: "You're offline. Reconnect and we'll pick up where you left off."

#### Empty states
Structure: **explain what will appear** + **guide to action** + **clear CTA**.

- "No customers yet" + "Customers appear here once you've added your first." + **Add a customer**
- "No reports for last week" + "We're still gathering data. Reports usually appear by Tuesday." + (no CTA — passive state)

Avoid: "It's empty here!", "Nothing to see, move along!", "Looks like you have no [things] yet :("

#### Confirmation messages
Structure: **confirm what happened** + **next step (if relevant)** + **undo (if reversible)**.

- "Saved." (transient — Toast, auto-dismiss)
- "Account deleted. **Undo** within 30 days from settings." (reversible, undo CTA prominent)
- "Invite sent to [email]. **Send another** or **Done**." (action complete, optional next step)

Avoid: "You're in!", "Welcome aboard!", "Awesome!", celebratory animation on routine tasks.

#### Onboarding copy
Structure: **welcome without overwhelming** + **one concept at a time** + **action-oriented** + **allow skipping**.

- Don't recreate documentation in the product. Let users skip.
- Each step has one concept and one action.
- Tone: matter-of-fact, not breathless.

#### CTAs
- **Start with a verb.** "Save changes", "Get in touch", "Send invite".
- **Match user intent, not business intent.** "Get in touch" not "Talk to sales". "Get the report" not "Download PDF".
- **Primary CTA is the most common action.** Secondary CTAs are subordinated.
- **Manfred-specific shortcuts**: "Get in touch" (Manfred's CTA on `studiomanfred.com`). "Ping us" (warmer alternative). Use when the surface is Manfred's own.

#### Tooltips + placeholder text
- Don't tooltip the obvious. If you need a tooltip on a Save button, the button's wrong.
- Placeholders show format, not instructions. `e.g. lina@studiomanfred.com` not `Type your email here`.

### Step 4 — The quick test

Before shipping any copy:

1. **Read aloud** — would I cringe? Rewrite if yes.
2. **Cover the brand** — could this come from a generic-SaaS app? Make it specific to Manfred or to this product.
3. **No marketing-verb count** — exactly zero is the only acceptable number.
4. **Errors blame nobody** — re-read each error; is the user the subject of failure? Rewrite to make the system the subject.
5. **CTAs are specific** — does the button name what happens?

If any answer is no, rewrite. Don't ship "fine" copy because the deadline's tight — fine copy is the failure mode this skill exists to prevent.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Quick is fine, just give me drop-in copy" | Generic copy isn't faster — it's permanent. The version that gets rewritten in QA is the lucky outcome; the version that ships generic and stays generic for years is the common one. Demand context. |
| "Engineering needs copy in 30 min or they'll ship 'TODO: copy' placeholders" | Two faster paths: (a) paste the validation rules + error conditions from the code, copy back in 15 min; (b) ship the placeholders honestly — "TODO: copy" tells QA the work isn't done, generic copy lies and removes the forcing function to fix it. |
| "Friendly and on-brand" (when Manfred has a brand doc) | "Friendly" is underspecified. Manfred is warmer-and-stranger, not chirpy-customer-success. Read the brand doc; reference the rules; don't default to generic-SaaS-friendly. |
| "Add an emoji to make it warmer" | Emoji rarely add warmth — they add noise. Manfred's warmth comes from voice, not decoration. |
| "Let's add 'Oops!' to soften the error" | "Oops!" is the genre marker for chirpy-customer-success. Soften with structure (what / do / action), not interjection. |
| "We don't know the real failure mode, just write generic 'something went wrong'" | Generic copy ships generic confusion. Demand the real failure mode; if engineering doesn't know, that's a separate problem (instrumentation gap) — flag it, don't paper over it. |
| "The button just says 'Submit' — it's a form, what else would it say?" | "Submit" is the worst CTA — it names the action's mechanic, not its outcome. "Save changes", "Send invite", "Get the report" — name what happens. |
| "Title Case For All UI Labels" | Sentence case for UI. Title case is for marketing headings. |
| "We'll workshop the copy in QA" | Copy in QA is copy too late. Write copy first, design around it. Content-first beats content-last every time. |

## Red flags — STOP

- About to write error copy without knowing the real failure mode
- About to use "Oops!", "Hmm,", "Yikes!", "Whoops!", "Welcome aboard!", "Awesome!"
- About to use a marketing verb (transform, empower, leverage, unlock, supercharge, drive, deliver value)
- About to use a corporate adjective (cutting-edge, world-class, innovative, best-in-class, passionate)
- About to use exclamation-stacking ("Saved!! Great work!!")
- About to use the user as the subject of a failure ("You entered an invalid email")
- CTAs that are nouns ("Done", "OK") or vague verbs ("Submit", "Continue") instead of specific verb + outcome
- Title case on UI labels ("Save Changes" instead of "Save changes")
- Hedging ("we might be able to…", "perhaps you could…")

## Manfred lens

UX writing is **infrastructure** — Cagan/Torres lens doesn't apply directly. But: copy is a **usability** surface and an **accessibility** surface (clarity, screen-reader rendering, plain language per design principle 15). Bad copy makes good design unusable.

Critical & ethical (principle 6): UX writing is where dark patterns live. Manipulative urgency ("Only 2 left!"), false defaults ("Yes, sign me up for everything!"), shame-prompts on cancel ("Are you sure? You'll miss out!") — refuse them. Copy that makes users feel bad to keep them in is the failure mode of "engagement" metrics.

Inclusive language (principle 15): plain language over jargon, gender-neutral, no ableist language ("crazy", "sanity check", "blind spot"), error messages that help not blame. Manfred ships in Swedish + English with parity.

## Cross-references

- `~/.claude/shared/manfred-brand.md` — the voice doc; non-optional
- `manfred-design-systems:component-spec` — copy decisions are part of the spec
- `manfred-design-ops:handoff-spec` — copy lands here before engineering pickup
- `manfred-toolkit:case-study` — long-form copy (different shape, same voice)
- `manfred-toolkit:linkedin-*` — Swedish-language equivalents for LinkedIn (post-shaped, same voice)
- `manfred-design-systems:a11y-design` — copy contributes to a11y (SR labels, plain language)

## Output format

For each copy moment, return:

```markdown
## <surface / state>

**Context** — [brief: what's happening, what's the user doing]
**Voice notes** — [Manfred-specific notes — fragments used, anti-patterns avoided]

### Copy
**[Element type, e.g. error toast, button, empty state heading]**
[The actual copy]

### Why
[1-2 sentences — what voice rule this copy honours, what alternative was rejected and why]
```

If the user asked for multiple copy moments at once, group them under the same heading per state (signup error → all error variants together).

## Tools used

- `Read` — `~/.claude/shared/manfred-brand.md`, prior copy in the codebase, design specs
- `Write` — produce copy file or commit to design spec
- `manfred-design-ops:handoff-spec` — when copy lands in a handoff
- `manfred-design-systems:component-spec` — when copy is part of a component definition
