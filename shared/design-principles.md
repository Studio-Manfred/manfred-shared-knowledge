# Manfred Design Principles

These principles guide every design decision made with or for the Manfred design system. When something feels ambiguous, come back here.

## 1. Start with User Needs

- Base decisions on evidence, not assumptions.
- Research is continuous, not a project phase.
- Define the problem before picking a solution.
- Measure success from the user's perspective, not the team's.

## 2. Accessible First

- Accessibility is not an afterthought — design for it from the start.
- WCAG 2.2 AA is the minimum standard.
- Test with assistive technology, not just automated tools.
- Consider the full spectrum: visual, motor, cognitive, auditory, and situational.
- Ask "can everyone use this?" before "does this look good?"

## 3. Warm but Precise

- Manfred is `business-blue` and `human-pink` at the same time — professional capability with human warmth.
- Be precise in language, typography, and interaction. Be warm in tone, color, and spacing.
- Precision without warmth feels clinical. Warmth without precision feels amateur. Neither is Manfred.

## 4. Simple by Default

- The best interface is the one you barely notice.
- Remove complexity before adding instructions.
- One primary action per view.
- Progressive disclosure — show what's needed when it's needed.
- If it needs a tutorial, it needs redesigning.

## 5. Use the Tokens

- Every color, spacing value, radius, and font size comes from the token layer. No magic numbers.
- Reach for semantic tokens (`bg-background`, `text-foreground`, `bg-primary`) when the value should adapt to theme.
- Reach for named brand utilities (`bg-business-blue`, `bg-human-pink`) only when you explicitly want the literal brand color regardless of theme.
- If a token doesn't exist for what you need, the fix is to add a token — not to hardcode a value in a component.

## 6. Ship Components That Work in the Dark

- Light and dark mode are peers. Every component must be tested in both.
- Don't wait for a "dark mode pass" — if it doesn't work in dark, it isn't done.
- Honor `prefers-color-scheme` by default and let the consumer force with `.light` / `.dark` on `<html>`.

## 7. shadcn Shapes Are the Contract

- Compose, don't wrap. `<Dialog><DialogTrigger /><DialogContent /></Dialog>` is the public API. Do not hide this behind `<Modal isOpen />`.
- The three-layer token architecture (primitives → semantic → shadcn contract) is what lets stock utilities like `bg-primary` and `text-foreground` work across themes — don't short-circuit it.
- Think of components as thin glue over Radix primitives. If a component is growing its own behavior, ask whether that behavior belongs upstream in Radix or downstream in the consumer.

## 8. Consistent, Not Uniform

- Use the system — don't reinvent components.
- Same interaction pattern for the same task everywhere.
- Diverge intentionally, never accidentally. Document the reason when you do.
- Consistency builds trust and reduces cognitive load for both users and engineers.

## 9. Mobile First, Responsive Always

- Design for the smallest screen first, then expand.
- Touch-friendly (44px minimum targets) everywhere.
- Content priority must be clear at every breakpoint.
- Test at 320, 768, 1024, and 1440px minimum.

## 10. Performance Is a Feature

- Fast pages are accessible pages.
- Optimize images, minimize JavaScript, lazy-load below the fold.
- Every kilobyte is a design decision. Every font weight loaded is a choice.
- The fewer component variants, the less bundle weight; ship variants that earn their place.

## 11. Design with Data

- Use analytics to understand real usage.
- A/B test when impact is genuinely unclear.
- Let go of designs that don't serve users, regardless of effort already invested.
- Track accessibility and performance metrics alongside conversion metrics — regressions there are real regressions.

## 12. Inclusive Language and Content

- Plain language over jargon.
- Gender-neutral terminology.
- No ableist language ("crazy," "sanity check," etc.).
- Error messages help, never blame.
- Swedish and English parity where the product supports both — don't let one language lag.

## How to Apply These

When making a design decision, walk down the list:

1. Does it serve a real user need? (Principle 1)
2. Can everyone use it? (Principle 2)
3. Is it warm and precise? (Principle 3)
4. Is it as simple as it can be? (Principle 4)
5. Does it use tokens consistently? (Principle 5)
6. Does it work in dark mode? (Principle 6)
7. Does it follow shadcn composition shapes? (Principle 7)
8. Does it match existing patterns? (Principle 8)
9. Does it work on mobile? (Principle 9)
10. Is it performant? (Principle 10)
11. Can we measure its impact? (Principle 11)
12. Is the language inclusive? (Principle 12)

If the answer to any is "no," revisit the design before shipping.
