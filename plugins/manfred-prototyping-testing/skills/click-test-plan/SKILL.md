---
name: click-test-plan
description: Use when designing a click test / first-click test / unmoderated findability test — anyone says "click test", "first-click test", "five-second test", "Maze test", "UsabilityHub", "where would users click", "navigation test", "findability test", "task-success rate". Manfred-flavoured: refuses "let's run a click test" without naming the assumption + risk type; cheap usability-risk technique on `manfred-discovery:assumption-test`'s menu (1–2 days build + 24h run).
---

# click-test-plan

Click tests answer one question well: **can users find the thing?** They're cheap, quantitative, fast, and unmoderated. Use them when you need a directional findability signal at scale (20–50 users in 24 hours). Don't use them when the question is "why" — that's a moderated test.

Manfred defaults:

- **Findability question only.** "Can they find it" = click test. "Can they understand it / use it / decide" = moderated test.
- **Realistic content.** Lorem ipsum makes the test about layout abstraction, not the actual product.
- **Don't hint at the path in the task.** "Click the settings icon" is not a click test — that's a UI-knowledge test.
- **Maps to `manfred-discovery:assumption-test`'s usability-risk menu.** Cost: 1–2 days build + 24h run. Cheaper than moderated, less rich. Pick consciously.

## When to use

- Validating navigation / IA findability
- Comparing two layouts on first-click target accuracy
- Five-second tests for first-impression / value-prop comprehension
- Pre-launch directional check on a single screen / single task
- After moderated testing surfaces a finding — quantify it at scale

**Skip when:**

- The question is "why" — moderated test (`manfred-design-research:usability-test-plan`)
- The flow has 5+ steps — click-paths get noisy past 3 clicks
- The task can't be described without revealing the UI — write a different task or use a different method
- You need to observe behaviour beyond the click (hesitation, comments, recovery) — moderated

## Pre-flight

Before designing the test:

1. **Risk + assumption** — what's the assumption? (Likely usability-risk per `manfred-discovery:assumption-test`.) What decision rests on the result?
2. **One question per task per stimulus** — keep tasks atomic
3. **Stimuli ready** — screens / prototype frames at the fidelity you'll ship at (or one step lower)
4. **Target population** — who clicks counts? Random crowdsourced ≠ your real users
5. **Linear ticket** for the test

If "we just want to see what users do" — that's not a question. Refuse and route to `manfred-discovery:assumption-test` for assumption framing.

## The hard rules

| Rule | What it means |
|---|---|
| **One task per screen** | Don't ask multiple findability questions on one stimulus — clicks contaminate each other |
| **Pre-define click target areas** | Decide what "correct" looks like *before* the test runs. Otherwise post-hoc rationalisation. |
| **Realistic content** | Real labels, real product names, real copy. Lorem ipsum invalidates findability findings. |
| **Don't hint** | "Click the settings icon" reveals the icon. "Where would you go to change your password?" doesn't. |
| **Sample 20–50 minimum** | Quantitative needs sample. Below 20, the heatmap is noise. |
| **Recruit your audience** | Generic crowdsourced users ≠ your customers. Screen for representativeness. |

## Test types

| Type | What it answers | Sample | When |
|---|---|---|---|
| **First-click test** | "Where do users click first to do X?" | 30–50 | IA / navigation findability for a single task |
| **Click-path test** | "What full sequence of clicks completes X?" | 30–50 | Multi-step tasks (≤ 3 clicks total to keep noise down) |
| **Five-second test** | "What's the first impression / value prop comprehension?" | 50+ | Above-the-fold messaging, brand tone, hero clarity |
| **Navigation test (e.g. tree test)** | "Can users find X in the IA?" | 50+ | Pure IA / category structure (no visual design needed) |
| **Comparative click test** | "Which design has better first-click rate?" | 30–50 per variant | A/B-style alternatives without engineering build |

## The flow

### Step 1 — Frame the question via `manfred-discovery:assumption-test`

What assumption is being tested? What's the decision the result will inform? If you can't answer both, you're not ready to design the test.

### Step 2 — Pick test type

From the table above, by question shape.

### Step 3 — Design the stimuli

- Use real or near-real content (no lorem ipsum on findability tests — confounds the result)
- Match the fidelity of the production design (mid-fi if production is mid-fi; high-fi if production is high-fi)
- Crop to what the user would actually see at the click moment (don't show the whole page if the click happens above the fold)
- Mobile or desktop? Test the breakpoint that matches the primary user

### Step 4 — Write the tasks

Rules:

- **Goal-oriented, not UI-oriented.** "Where would you click to change your email address?" not "Click the profile icon".
- **Use the participant's language**, not internal jargon. "Cancel my plan" not "Modify subscription tier".
- **One goal per task.**
- **Order easy → hard.** Build confidence; the hard tasks come after the user is calibrated.
- **Include a warm-up task** that's easy and unrelated, so people get the interface conventions before the real questions.

Example tasks (good):

- ✅ "You bought a sweater that doesn't fit. Where would you click to send it back?"
- ✅ "You want to know how this app handles your data. Where would you click first?"

Example tasks (bad):

- ❌ "Click on the returns link." *(reveals the answer)*
- ❌ "How would you initiate a return-merchandise authorisation flow?" *(jargon)*
- ❌ "Find the returns policy and tell us what you think of it." *(two tasks)*

### Step 5 — Define click targets + success

Before launch, decide:

- **Primary target area** (the "correct" zone — usually a polygon, not just a point)
- **Acceptable alternates** (e.g. menu *and* breadcrumb both lead to the same place)
- **Success rate threshold** that informs the decision (typically 65%+ first-click success indicates good findability; <50% is a redesign signal)

Document this *before* running the test. Otherwise you'll rationalise the result.

### Step 6 — Define participants + recruit

- N: 20–50 (more if comparing variants — 30 per variant minimum)
- Screen for: target audience characteristics, locale, AT use if accessibility-relevant
- Tools: Maze, UsabilityHub, Useberry, Userlytics — pick by panel availability and price

Generic panel ≠ your audience. Pay for screening.

### Step 7 — Pre-commit the analysis plan

```markdown
## Decision rule

- **First-click success ≥ <threshold>%** → ship; document the test as supporting evidence
- **First-click success < <threshold>%** → redesign signal; route to follow-up moderated session to understand *why*
- **Heatmap shows alternative click cluster** → consider the alternative target as a real user expectation; redesign IA to match

## Segmentation
- Mobile vs desktop
- Returning vs new users (if known)
- Locale (EN / SV)
```

### Step 8 — Run, then analyse

Click tests typically run in 12–48 hours. After:

- **First-click success rate** — primary
- **Time to first click** — hesitation indicator
- **Click distribution heatmap** — where clicks cluster outside the target tells you what users *expected*
- **Confidence rating** (if asked post-task) — correlates with comprehension; mismatch (high confidence + wrong click) is a usability red flag

### Step 9 — Document + Linear

```markdown
# Click test — <name>

**Linear**: STU-XXX
**Risk retired**: <usability> via `manfred-discovery:assumption-test`
**Question**: <findability question>
**Type**: <first-click / click-path / five-second / etc>
**Stimuli**: <screens tested>
**Tasks**: <verbatim task wording>
**Click targets**: <pre-defined>
**Success threshold**: <% pre-committed>
**N**: <participants>
**Tool**: <Maze / etc>
**Result**: <first-click rate, heatmap summary, time-to-click>
**Decision**: <ship / redesign / follow-up moderated>
**Owner**: <name>
```

Post via `mcp__linear-server__save_comment`.

## Common rationalisations

| Excuse | Reality |
|---|---|
| "Let's just run a click test." | Without a question, the result is noise that gets read as signal. Frame the assumption first. |
| "10 users is enough." | Quantitative needs sample. Below 20, the heatmap is wishful interpretation. |
| "Lorem ipsum is fine — we're testing layout." | If the test is "layout", the screen is incomplete. If the test is "findability", lorem ipsum invalidates it. Use real content. |
| "Click test will tell us why." | It tells you *what they did*. "Why" needs moderation. |
| "Let's test all 8 tasks at once." | Click order contaminates findings. Atomic tests only — one task per screen. |
| "We'll figure out what success looks like after." | That's post-hoc rationalisation. Pre-commit. |

## Red flags — STOP

- No assumption / decision framed.
- Click target area not pre-defined.
- Lorem ipsum in stimuli.
- Task wording reveals the UI path.
- Sample < 20.
- Generic panel without screening for your audience.
- Test set up to validate a decision already made.

## Manfred lens

**Cagan's 4 risks** — click tests retire **usability risk** specifically, on the cheap end of the spectrum. They're rarely the right tool for value, feasibility, or viability. Route via `manfred-discovery:assumption-test` to confirm.

**Torres OST** — a click test result updates one assumption-test node on the tree. If the result is "ship", the node closes; if "redesign", the node stays open with the result as evidence pointing to the next test.

## Cross-references

- `manfred-discovery:assumption-test` — click test is one technique on the usability-risk menu
- `manfred-design-research:usability-test-plan` — for moderated follow-up when "why" is needed
- `manfred-prototyping-testing:test-scenario` — task-writing craft (transferable across moderated + unmoderated)
- `manfred-prototyping-testing:wireframe-spec` — for the stimuli when prototype isn't ready
- `manfred-design-systems:a11y-design` — for testing AT-specific findability (separate plan)
- `manfred-toolkit:ux-writing` — for task wording that doesn't reveal the UI

## Tools used

- Maze, UsabilityHub, Useberry, Userlytics — unmoderated test platforms
- `mcp__linear-server__get_issue` / `save_comment` — for ticket linkage

---

*Structurally adapted from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) under MIT license. Voice, examples, route-through-assumption-test rule, hint-detection rules, pre-commit-decision rule, and Manfred-specific guidance are original.*
