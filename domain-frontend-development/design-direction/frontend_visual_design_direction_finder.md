---
title: "Visual Design Direction Finder — From Brand Attributes to 2–3 Distinct Direction Options"
category: frontend-development/design-direction
description: "Discover a visual design direction through brand-attribute elicitation, moodboard direction, and design-principle articulation. Outputs 2–3 distinct direction options (each with palette intent, type personality, layout energy, motion feel) plus a recommendation."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - visual-design
  - brand-attributes
  - design-direction
  - moodboard
  - design-principles
updated: "2026-06-07"
related_prompts:
  - domain-frontend-development/design-direction/frontend_look_and_feel_hunt.md
  - domain-product-management/prompts/product_create_prd.md
  - domain-image-generation/IMAGE_GENERATION_GUIDE.md
---

# Visual Design Direction Finder

**Objective:** Help a team converge on a visual design direction by eliciting brand attributes, translating them into moodboard direction and design principles, and producing 2–3 genuinely distinct direction options — each specified by palette intent, type personality, layout energy, and motion feel — with a clear recommendation.

**When to Use:**
- You're starting design for a product/brand and need to align on direction *before* anyone opens a design tool.
- Stakeholders keep saying "make it clean / modern / premium" and you need to turn those vague words into actionable, distinct directions.
- You want a few real options to react to, not one direction presented as a fait accompli.
- You need a shared design-language brief to hand to a designer, an AI image tool, or a frontend implementation.

**When NOT to use:**
- You need the implementation-level UI look-and-feel spec (components, tokens, states) — use the sibling prompt `domain-frontend-development/design-direction/frontend_look_and_feel_hunt.md`, which goes deeper on the build side.
- You need to generate actual images/mockups — use the image-generation guide and prompts.
- The direction is already locked and you need critique of an existing design — this is a discovery prompt, not a review.

---

## Inputs / Context

1. **What you're designing** — product, brand, app, marketing site, etc., and its core purpose.
2. **Audience** — who it's for; their expectations, sophistication, and context of use.
3. **Brand attributes / desired feeling** — adjectives or phrases (e.g., "trustworthy but not stuffy," "playful," "premium," "approachable"). Even messy ones help.
4. **Comparables you like / dislike** — products or brands whose feel resonates or repels, and *why* (described, not assumed).
5. **Constraints** — existing logo/colors that must stay, accessibility requirements, platform (web/mobile/print), brand guidelines, technical limits.
6. **Emotional goal** — how should someone feel in the first five seconds?

If comparables or attributes are missing, elicit them rather than inventing a brand personality.

---

## Constraints

### Must
- Begin by translating raw brand attributes into a small set of **design principles** (3–5) that any direction must honor.
- Produce **2–3 distinct direction options** — distinct meaning they make genuinely different choices, not three shades of the same idea.
- For each direction, specify all four dimensions:
  - **Palette intent** — the *role and mood* of color (e.g., "warm neutrals with a single saturated accent for calm focus"), not invented hex codes unless the user supplied brand colors.
  - **Type personality** — what the typography should feel like (e.g., "humanist sans for warmth; generous spacing for calm"), described by character, not necessarily named fonts.
  - **Layout energy** — density, rhythm, whitespace, and structure (e.g., "spacious, grid-disciplined, editorial").
  - **Motion feel** — how transitions/interactions should feel (e.g., "subtle, quick, confident" vs. "playful, springy").
- Tie each direction back to the brand attributes and audience — say *why* it fits.
- End with a **recommendation** and the trade-off it accepts.
- Respect locked brand assets and accessibility requirements in every direction.

### Must Not
- Invent specific hex codes, named fonts, or pixel values as if they were prescribed — describe intent unless the user provided exact assets.
- Produce three near-identical directions (false variety).
- Fabricate claims about what competitors' designs do unless the user described them.
- Ignore accessibility (contrast, legibility) — it constrains every direction.
- Present the recommendation as the only valid option; name what each rejected direction was better at.

---

## Instructions

1. **Elicit and consolidate brand attributes.** Restate the user's adjectives/comparables. If they're thin or contradictory ("minimal but bold and busy"), surface the tension and ask which wins, rather than papering over it.

2. **Translate attributes into design principles (3–5).** These are the rules every direction must obey (e.g., "Clarity over decoration," "Warmth without childishness," "One focal point per screen"). Principles are the through-line; directions are interpretations of them.

3. **Set the moodboard direction in words.** Describe the overall sensory territory each direction occupies — the feeling, references, and atmosphere — so a designer or image tool could pursue it. Use described references, not fabricated brand claims.

4. **Generate 2–3 distinct directions (RT-02 — multiple framings).** For each, make a deliberately different bet on the principles. For every direction, fill all four dimensions:
   - Palette intent (role/mood of color; honor any locked brand colors)
   - Type personality (character and spacing)
   - Layout energy (density, rhythm, whitespace)
   - Motion feel (pace and character of interaction)
   Then state which audience reaction it optimizes for and which it sacrifices.

5. **Check against constraints (CM-02).** Confirm each direction honors locked assets, platform, and accessibility. If a direction can't, adjust it or note the conflict.

6. **Recommend one (QA-04).** Pick the direction that best serves the principles and audience. State the trade-off it accepts and what the runner-up directions were better at — so the team chooses with eyes open. Note where your recommendation is a judgment call vs. constraint-driven.

---

## False-Positive Prevention

1. **False variety.** Three directions that all say "clean, modern, minimal" are one direction. Each must make a genuinely different bet — e.g., editorial vs. utilitarian vs. expressive — or it isn't a real option.
2. **Inventing prescriptive specifics.** Don't output "#2A5C8F, Inter 16px" as if specified. Describe color *role* and type *character*. Only state exact values the user actually provided.
3. **Fabricated competitor design claims.** "Competitor X uses a brutalist grid" is a fabrication unless the user said so. Describe references the user supplied; ask for more if needed.
4. **Ignoring contradictions in the brief.** "Premium and playful and ultra-minimal and information-dense" can't all win. Surface the tension and force a priority instead of silently averaging.
5. **Skipping accessibility.** A gorgeous low-contrast palette is a failed direction. Treat contrast and legibility as hard constraints in every option.
6. **One-option theater.** Presenting two weak strawmen next to one obvious winner is not real choice. Each direction must be defensible on its own terms.
7. **Decoupling from audience.** A direction is only "right" relative to who it's for and how they'll use it. Every direction must be justified against the audience, not aesthetics in a vacuum.
8. **Confusing this with implementation.** Tokens, component states, and spacing scales belong in the frontend look-and-feel spec, not here. Keep this at direction altitude.

---

## Output Format

```
# Visual Design Direction: [what you're designing]

## Brand attributes (consolidated)
[Restated attributes; any tensions surfaced and resolved.]

## Design principles (must hold across all directions)
1. [Principle]
2. [Principle]
3. [Principle]
(3–5 total)

## Direction A: [evocative name]
- Moodboard direction: [sensory territory / references in words]
- Palette intent: [role/mood of color]
- Type personality: [character + spacing]
- Layout energy: [density, rhythm, whitespace]
- Motion feel: [pace + character]
- Optimizes for: [audience reaction] / Sacrifices: [what it gives up]
- Constraint check: [locked assets, accessibility, platform — OK or conflict]

## Direction B: [name]
[Same structure — a genuinely different bet]

## Direction C: [name] (optional)
[Same structure]

## Recommendation
**Direction [X]** — [why it best serves the principles + audience].
- Trade-off accepted: [...]
- Runner-up [Y] was better at: [...]
- Confidence: High | Medium | Low — [judgment call vs. constraint-driven]
```

---

## Verification

- [ ] Brand attributes restated; contradictions surfaced, not averaged.
- [ ] 3–5 design principles articulated as the through-line.
- [ ] 2–3 directions that make genuinely different bets (no false variety).
- [ ] Each direction specifies palette intent, type personality, layout energy, and motion feel.
- [ ] Color/type described as intent/character unless exact assets were provided.
- [ ] Accessibility and locked brand assets respected in every direction.
- [ ] Each direction tied to audience and principles.
- [ ] Recommendation names its trade-off and the runner-ups' strengths.
- [ ] Confidence stated.
- [ ] No fabricated competitor design claims or invented prescriptive specifics.
