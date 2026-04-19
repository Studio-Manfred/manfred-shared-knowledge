# Manfred Brand Guidelines

## What Manfred Is

Manfred is a product design studio. The tagline on the front door:

> **Building Better Product Companies.**

The mission, in one line:

> **Make the product world more customer driven.**

Everything Manfred ships — research, design, leadership engagements, training, writing, the design system — is in service of that mission.

## Manfred Magic

The studio's shorthand for what it brings into a room: **smart work, sharp thinking, and a bit of fun.** It is the unserious name for a serious idea — that craft and warmth aren't trade-offs. You get both, or you haven't actually delivered.

## Services

Manfred is primarily a consulting studio. Engagements fall into four buckets:

- **Design & Product Leadership** — interim leadership, coaching, sparring, design-maturity work. "Just when you need it."
- **Customer Research** — qualitative and quantitative. Understanding people before shipping things to them.
- **Product, UX & Service Design** — the hands-on craft: flows, screens, services, systems.
- **Training & Courses** — open classes and custom programs. Topics include Design Leadership, Product Discovery, Customer Journey Mapping, Business Design, DesignOps, Design Thinking for HR, and CX Management (the last in partnership with House of CX through IHM business school).

Also on offer when it fits: workshops, co-creation sessions, speaking, writing — "winging it with a whiteboard" is a listed service.

## The Mmmms (the team)

- **Jens Wedin** — Design Director & Service Designer
- **Selma Hallqvist** — Senior Product Designer
- **Axel Nathorst-Böös** — Design & Product Leadership
- **Moa Bogren** — Senior User Research (UXR)

Small team, senior people, hands-on work.

## Clients

Manfred has worked with product teams across messy scale-ups and heavy-suit orgs alike. Named on the site: **Boka Direkt · Mentimeter · Fishbrain · Svea Bank · Trygg-Hansa**.

## Brand Values

### Customer-driven

- Users come before features, hypotheses before roadmaps, research before design.
- "Most products and services will never be used or bought. Why build something nobody wants?" — from the Product Discovery course page. That question is the studio's posture.

### Craft Taken Seriously (Yourself, Not So Much)

- From the careers page: *"You don't take yourself too seriously, but you take the craft seriously."* That's the line.
- Ship work that deserves the hours put into it. But keep the atmosphere human — "winging it with a whiteboard" is allowed.

### Human + Business Capability at the Same Time

- The design system encodes this in two color tokens: `business-blue` (`#2c28ec`) and `human-pink` (`#efd6d3`). Professional enough to trust with real work. Warm enough that people feel seen.
- In engagements, this shows up as: strategic clarity without corporate stiffness, research depth without academic distance.

### Critical & Ethical Design

- Technology brings responsibility. Manfred runs workshops on Critical Design (including at Stockholm Xperience) and publishes on ethical design practice.
- Ask what the design *does in the world*, not only whether it ships.

### Accessibility as Baseline

- Non-negotiable across everything Manfred makes. WCAG 2.2 AA minimum, AAA where practical.
- Tested with assistive technology, not only automated tools.

### Sustainability in the Small

- Lighter pages, smaller bundles, considered font loading.
- Design for longevity — avoid trendy patterns that age in a year.

## Brand Voice

### Tone

- **Warm and informal** — "Yep." "Of course." "Cool." "Ping us."
- **Playful** — "Manfred Magic", "the Mmmms", "winging it with a whiteboard"
- **Direct and confident** — short sentences, clear claims, no hedging
- **Unflashy** — the product is the hero; copy is the quiet shoulder-tap
- **Craft-serious** — casual register, never sloppy thinking

The voice is informal without being glib. Read the site copy back and you'll find full stops, plain verbs, and an occasional wink — never forced enthusiasm, never bullet-list marketing-speak.

### Writing Principles

- Lead with the benefit to the reader.
- Plain language over jargon. Every time.
- Short sentences, short paragraphs.
- Inclusive language always — no gendered terms, no ableist metaphors, no cultural assumptions.
- Swedish and English parity where the product supports both; pick one and commit per surface.
- A light joke is fine. Forced levity is not.

### CTAs

- Action-oriented, short: "Get started," "Save," "Continue," "Send," "Get in touch," "Ping us."
- Never "Click here." Never "Submit."

### Errors

- What happened, what to do next, one clear action — in that order.
- Explain, don't blame. "We couldn't save your changes — try again, or refresh the page if it keeps failing." Not "Error 500."

## Writing & Thought Leadership

Manfred publishes regularly on the studio blog (`/news`) and Jens Wedin writes on LinkedIn in Swedish (see the `linkedin-*` skills for voice specifics: *reflect*, *teach*, *show-and-tell*). Recurring themes:

- Customer research (qualitative vs. quantitative, mindset, synthesis)
- Critical and ethical design
- Product discovery and design maturity
- Personal/running/life notes ("Road to Average" series) — the studio voice includes the person writing it

The Swedish book: **Upplevelseblomman** (`upplevelseblomman.se`).

## Visual Language

The visual system is codified in `github.com/jens-wedin/manfred-design_system` and documented for LLM use in `~/.claude/shared/DESIGN.md`. Quick reference:

### Colors

| Name | Token | Hex | Role |
|---|---|---|---|
| Almost Black | `--color-almost-black` | `#1e1e24` | Primary text, dark surfaces |
| Business Blue | `--color-business-blue` | `#2c28ec` | Brand primary, CTAs, links |
| Human Pink | `--color-human-pink` | `#efd6d3` | Warm accent surface |
| Beige | `--color-beige` | `#e6dcc8` | Neutral warm surface |
| Light Beige | `--color-light-beige` | `#f4f3e8` | Default warm background |
| White | `--color-white` | `#ffffff` | Default surface, inverse text |

Blue leads, warm neutrals hold the room, pink is for moments of human emphasis. Named utilities (`bg-business-blue`, `bg-human-pink`, …) are literal primitives and **do not flip in dark mode**. Use semantic tokens (`bg-background`, `bg-primary`, …) for theme-aware styling.

### Typography

- **Host Grotesk** — all UI. Humanist sans-serif. Scale `xs` (12px) → `5xl` (56px). Weights 300 / 400 / 500 / 600 / 700 / 800.
- **Guttery** — Manfred logotype only. Never used in UI.

### Layout & Atmosphere

- Generous whitespace. Sections breathe.
- Warm background rhythm: alternate `light-beige` canvas with `white` or `beige` cards. Avoid gray-on-gray layering.
- Flat first. Depth is earned. No heavy shadows, gradients, or neumorphism.

## Contact

- **Work inquiries:** `hello@studiomanfred.com`
- **Site:** `studiomanfred.com`

## Quick Reference

- **Full design system spec:** `~/.claude/shared/DESIGN.md`
- **Decision framework:** `~/.claude/shared/design-principles.md`
- **Design system source:** `github.com/jens-wedin/manfred-design_system`
- **Shared knowledge repo:** `github.com/jens-wedin/manfred-shared-knowledge`
