---
description: Create a new component end-to-end — spec, tokens, accessible implementation, docs page. Manfred-flavored: shadcn shapes, semantic tokens, WCAG 2.2 AA baseline.
argument-hint: [component name and one-line purpose, e.g. "EmptyState — placeholder for empty lists/grids"]
---

You're creating a new component for a Manfred app. The user mentioned: $ARGUMENTS

## Step 1 — Confirm it should exist

Ask, in this order, until you have answers:

- **What problem does this component solve that an existing one doesn't?** (The Manfred design system already ships Alert, Badge, Breadcrumb, Button, Checkbox, Dialog, FormField, Icon, Logo, ProgressBar, Radio, SearchBar, Spinner, TextInput, Toast, Tooltip, Typography. If the answer is "X but blue" — variants belong in props, not components.)
- **Will it be used in 3+ places?** (One use = inline JSX. Two = local component. Three+ = library candidate.)
- **Does shadcn ship a primitive close to this?** (Dialog, Tooltip, RadioGroup, Toast, Popover, Combobox, Slider — Manfred mirrors stock shadcn shapes. If yes, the API will mirror that shape.)

If the answer is "actually it's a variant" or "actually we only use it once" — stop here and tell the user. Don't build a component that shouldn't exist.

## Step 2 — Spec it (`manfred-design-systems:component-spec`)

Run the `manfred-design-systems:component-spec` skill to produce the full spec:

- What it is (one sentence)
- When to use / not to
- Anatomy
- Props / API (mirror shadcn shape if applicable)
- States (default · hover · focus · active · disabled · loading · error)
- Tokens consumed (resolved through `manfred-design-systems:design-token`)
- Accessibility (WCAG 2.2 AA — keyboard, focus indicator, target size, screen reader)
- Composition (`asChild` for Slot composition)
- Examples
- Anti-patterns

Save the spec to `docs/components/<component-name>.md` (or wherever the project keeps specs).

## Step 3 — Resolve tokens (`manfred-design-systems:design-token`)

For every visual decision in the spec, run `manfred-design-systems:design-token`:

- Surface, text, border colours → semantic tokens (`bg-card`, `text-foreground`, `border-border`)
- Spacing, radius → Tailwind primitives
- States → semantic tokens that flip in dark mode

If the spec calls for a colour that doesn't exist in the token surface (a `success` green, a `warning` amber): the token skill will refuse and offer (a) add token, (b) reuse semantic, (c) neutral + icon. Resolve this **before** writing implementation code — don't punt the decision to JSX time.

## Step 4 — Implement (`manfred-design-systems:a11y-dev`)

Write the React component. Rules:

- Native HTML element first, ARIA second, custom last
- Tokens only — no hex, no `bg-green-500`
- Every interactive state has a focus indicator (`focus-visible:ring-2 focus-visible:ring-ring`)
- `asChild` if composition matters
- `forwardRef` for any focusable element
- Loading state uses `aria-busy`, not `disabled` (different a11y semantics)
- TypeScript props match the spec exactly

Save to `src/components/<ComponentName>.tsx` (or the project's component directory). Add a co-located test file (`<ComponentName>.test.tsx`) using vitest + Testing Library — cover the keyboard interactions and the a11y semantics, not just the happy path.

## Step 5 — Document (`manfred-design-systems:documentation-template`)

Run `manfred-design-systems:documentation-template` with the **component template** to produce the docs page (Storybook MDX or markdown). The spec from step 2 is most of the input — the docs page reformats it for consumers and adds:

- Live examples (Storybook stories — one per variant + one per state)
- Status indicator (`experimental` for first release)
- Related components / patterns

## Step 6 — Verify in dark mode

Build the component, render it in Storybook (or a dev server) with `.dark` toggled. Confirm:

- Tokens flip correctly (no hardcoded colours leaking through)
- Contrast still meets WCAG 2.2 AA in both modes
- Focus indicator visible against both light and dark surfaces

## Step 7 — A11y gate (`manfred-design-systems:a11y-qa`)

Run `manfred-design-systems:a11y-qa` against the new component (Storybook story or dev URL).

- 0 critical/serious findings → ship
- Any critical/serious → fix before merge
- Moderate/minor → backlog with the ticket

## Step 8 — Commit

Conventional commit:

```
feat(<scope>): add <ComponentName>

[brief description — what problem it solves, key API decisions]

- Spec: docs/components/<component-name>.md
- Storybook: <link>
- A11y: passed (axe scan, 0 serious findings)
```

If a Linear ticket is linked, post a comment with: spec path, component path, Storybook link, a11y scan result.

## Wrap-up

Confirm the component covers:

- [ ] Spec written and reviewed
- [ ] Tokens resolved (no hex, no bypass)
- [ ] Implementation matches spec API
- [ ] Tests cover keyboard + a11y semantics
- [ ] Docs page with live examples
- [ ] Dark-mode verified
- [ ] A11y gate passed
- [ ] Conventional commit

Then offer:

> "Run `/manfred-design-systems:audit-system` against this component (or its scope) before merge if you want a final compliance pass. Or `/manfred-design-research:test-plan` if a usability test should validate the behaviour with real users."
