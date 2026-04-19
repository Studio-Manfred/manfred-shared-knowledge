# Manfred Design Principles

These principles guide every design decision made by or for Manfred — whether it's a research plan, a client product, a training course, or a component in the design system. When something feels ambiguous, come back here.

## 1. Customer-Driven, Always

- Users before features. Hypotheses before roadmaps. Research before design.
- Most products that get built never get used. Ask *why would anyone want this?* before *how do we ship it?*
- Measure success from the user's perspective, not the team's.

## 2. Research Isn't a Phase

- It's continuous. Qualitative and quantitative. Every engagement has a research posture.
- Talk to real users regularly. Synthesize honestly. Don't privilege the easy finding.
- When research contradicts the brief, bring it to the brief — don't hide it.

## 3. Craft Seriously, Yourself Not So Much

- Ship work that deserves the hours put into it. Be precise in language, typography, spacing, interaction.
- Keep the atmosphere human. "Winging it with a whiteboard" is a legitimate mode. Jokes are allowed. Ego isn't.
- Casual register, never sloppy thinking.

## 4. Warm + Precise

- Manfred runs on `business-blue` and `human-pink` at the same time — professional capability with human warmth. That pairing is the brand argument.
- Precision without warmth feels clinical. Warmth without precision feels amateur. Neither is Manfred.
- Warm defaults over clinical ones. Soft off-black over pure black. Warm beige canvas over cold gray.

## 5. Accessible First

- Accessibility is not a feature or a compliance line item — it's a baseline brand value.
- WCAG 2.2 AA minimum, AAA where practical.
- Test with assistive technology, not only automated tools.
- Consider the full spectrum: visual, motor, cognitive, auditory, situational.
- Ask "can everyone use this?" before "does this look good?"

## 6. Critical & Ethical Design

- Technology brings responsibility. Every design decision has consequences beyond the screen.
- Ask what the design *does in the world*, not only whether it ships.
- Dark patterns are out. Manipulation is out. Attention-grabbing that doesn't serve the user is out.
- If in doubt, run the decision past someone unlike yourself.

## 7. Simple by Default

- The best interface is the one you barely notice.
- Remove complexity before adding instructions.
- One primary action per view.
- Progressive disclosure — show what's needed when it's needed.
- If it needs a tutorial, it needs redesigning.

## 8. Use the Tokens

- Every color, spacing value, radius, and font size comes from the token layer. No magic numbers.
- Reach for semantic tokens (`bg-background`, `text-foreground`, `bg-primary`) when the value should adapt to theme.
- Reach for named brand utilities (`bg-business-blue`, `bg-human-pink`) only when you explicitly want the literal brand color regardless of theme.
- If a token doesn't exist for what you need, the fix is to add a token — not to hardcode a value in a component.

## 9. Ship Components That Work in the Dark

- Light and dark mode are peers. Every component tested in both.
- Don't wait for a "dark mode pass" — if it doesn't work in dark, it isn't done.
- Honor `prefers-color-scheme` by default; let the consumer force with `.light` / `.dark` on `<html>`.

## 10. shadcn Shapes Are the Contract

- Compose, don't wrap. `<Dialog><DialogTrigger /><DialogContent /></Dialog>` is the public API.
- The three-layer token architecture (primitives → semantic → shadcn contract) is what keeps stock utilities working across themes. Don't short-circuit it.
- Components are thin glue over Radix primitives. If behavior is growing inside a component, ask whether it belongs upstream (Radix) or downstream (consumer).

## 11. Consistent, Not Uniform

- Use the system — don't reinvent components.
- Same interaction pattern for the same task everywhere.
- Diverge intentionally, never accidentally. Document the reason when you do.

## 12. Mobile First, Responsive Always

- Design for the smallest screen first, then expand.
- Touch-friendly (44px minimum targets) everywhere.
- Content priority must be clear at every breakpoint.
- Test at 320, 768, 1024, and 1440px minimum.

## 13. Performance Is a Feature

- Fast pages are accessible pages.
- Optimize images, minimize JavaScript, lazy-load below the fold.
- Every kilobyte is a design decision. Every font weight loaded is a choice.

## 14. Design with Data

- Use analytics to understand real usage.
- A/B test when impact is genuinely unclear.
- Let go of designs that don't serve users, regardless of effort already invested.
- Track accessibility and performance metrics alongside conversion metrics — regressions there are real regressions.

## 15. Inclusive Language and Content

- Plain language over jargon. Every time.
- Gender-neutral terminology.
- No ableist language ("crazy," "sanity check," etc.).
- Error messages help, never blame.
- Swedish and English parity where the product supports both.

## How to Apply These

When making a design decision, walk down the list:

1. Does it serve a real customer need? (Principle 1)
2. Is it grounded in research, or assumption? (Principle 2)
3. Is the work crafted but unfussy? (Principle 3)
4. Is it warm and precise? (Principle 4)
5. Can everyone use it? (Principle 5)
6. Have we thought about what this does in the world? (Principle 6)
7. Is it as simple as it can be? (Principle 7)
8. Does it use tokens consistently? (Principle 8)
9. Does it work in dark mode? (Principle 9)
10. Does it follow shadcn composition shapes? (Principle 10)
11. Does it match existing patterns? (Principle 11)
12. Does it work on mobile? (Principle 12)
13. Is it performant? (Principle 13)
14. Can we measure its impact? (Principle 14)
15. Is the language inclusive? (Principle 15)

If the answer to any is "no," revisit the design before shipping.
