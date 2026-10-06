---
title: "GPT Image 2 — Dense Text Infographic"
category: image-generation/infographic
description: "Multi-section infographic with verbatim labels, optionally web-search-grounded, using gpt-image-2's high text rendering accuracy."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-12
  - SV-13
  - SV-18
difficulty: advanced
tags:
  - gpt-image-2
  - infographic
  - text-rendering
  - data-visualization
  - openai
updated: "2026-10-06"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-image-generation/infographic_meta_prompt.md
---

# GPT Image 2 — Dense Text Infographic

**Objective:** Generate a multi-section infographic where every label, statistic, and section header is rendered verbatim. Leverage gpt-image-2's 95%+ text accuracy and (optionally) live web search for fact grounding.

**API parameters (required):**
- `model="gpt-image-2"`
- `size="1024x1536"` (portrait — standard infographic) or `1536x1024` (landscape — slide / blog hero)
- `quality="high"` (required; non-negotiable for dense text)
- `n=1`

---

## Inputs

- `[TITLE]` — verbatim infographic title
- `[SUBTITLE]` — optional verbatim subtitle / dek
- `[AUDIENCE]` — who reads this (executives / K-12 / clinicians / general public)
- `[SECTION COUNT]` — typically 3–6 sections
- `[SECTIONS]` — for each section: heading, 1–3 bullets/stats, optional small visual
- `[FOOTER]` — verbatim source attribution
- `[FACT GROUNDING]` — `web-search-on` (allow live lookup of current facts) or `web-search-off` (use only what's in this prompt)
- `[BRAND PALETTE]` — hex codes

---

## Constraints (Must / Must Not)

**Must:**
- Use `quality="high"`.
- Specify exact section count and grid (apply SV-12).
- Provide verbatim text for every label, header, statistic, and footer.
- State whether the model may search the web for facts.

**Must Not:**
- Allow the model to invent statistics ("a study showed...").
- Use clip-art or decorative-illustration framing.
- Mix multiple typefaces unless explicitly listed.
- Render lorem ipsum, faux-Latin, or placeholder copy.

---

## Production Prompt

```
SCENE / CANVAS:
A single flat infographic, [orientation], on a [background hex] canvas. This is print-style information design — not an illustration, not a UI screenshot, not a slide deck mockup.

SUBJECT / STRUCTURE:
[SECTION COUNT] sections arranged in a clean grid:
- TITLE BAR (top ~12% of canvas): "[TITLE]"
- SUBTITLE (just below, ~5% of canvas): "[SUBTITLE]" (omit if blank)
- SECTIONS (next ~75%): EXACTLY [SECTION COUNT] equal-sized panels arranged in a [N rows × M cols] grid. Each panel is the same width and height. Read order: left-to-right, top-to-bottom.
- FOOTER (bottom ~8%): "[FOOTER]"

KEY DETAILS — verbatim content per section:

SECTION 1:
- Heading: "[HEADING_1]"
- Body: "[BODY_1]" (verbatim)
- Stat (if any): "[STAT_1]"
- Visual cue (if any): [icon-style — e.g., "a simple line-art clipboard"]

SECTION 2:
- Heading: "[HEADING_2]"
- Body: "[BODY_2]"
- Stat: "[STAT_2]"
- Visual cue: [...]

[... continue for each section ...]

USE CASE:
[AUDIENCE]-facing infographic. Will be viewed at full size on a website / printed at A4 / used in a slide. All text must be 100% readable at full resolution.

CONSTRAINTS:
- Style commitment: clean information design, flat colors, sans-serif typography, light grid lines or hairlines only. Not an illustration. Not a UI mockup.
- Brand palette: primary [HEX], secondary [HEX], accent [HEX]. Use these exact hex values.
- Typography: single sans-serif family. Title weight: bold. Headings: semibold. Body: regular. Numbers in stats: tabular figures preferred.
- EXACT TEXT — every quoted string above (title, subtitle, all section headings, all body, all stats, footer) renders verbatim with no extra characters, no punctuation drift, no inserted line breaks unless I specify them.
- Layout discipline: panels are EQUAL size, EQUAL spacing, perfectly aligned. No spanning, no empty panels.
- Fact grounding: [FACT GROUNDING — "Use accurate, up-to-date references from web search for any factual claims" OR "Do not use external references; render only the facts provided in this prompt — do not invent additional statistics or sources."]
- Forbidden: clip-art, decorative illustrations, gradients, drop shadows, 3D effects, multiple typefaces beyond what's specified, fictional statistics, faux-Latin.
- Format: [size], [orientation].

If any quoted string has a typo, extra character, or paraphrase, the output is incorrect. If any panel is unequal in size to the others, the output is incorrect.
```

---

## Iteration Plan

1. "Section 3's stat is rendering in the wrong color — render it in the accent hex [HEX] instead."
2. "The title is too small — push it to ~10% of canvas height."
3. "Tighten the panel grid — there's too much gutter between sections 4 and 5."

---

## False-Positive Prevention

❌ **DON'T:**
- Treat `web-search-on` as fact-checking — search during generation can add numbers, dates, names, and labels that are not in `[SECTIONS]`, and the result looks well-sourced while nothing in it traces to a source.
- Accept one `[FOOTER]` source line as covering every statistic — a footer citation is a claim about provenance, not evidence of it.
- Pass a stat because it is a plausible number — "23%" re-rendered as "2.3%", or STAT_2 drifting into section 3's panel, still passes a skim.
- Let a countable visual cue contradict its stat (a 7-of-10 pictogram beside "65%").

✅ **DO:**
- Require a source list before generation: each fact in `[SECTIONS]` carries a source and access date supplied by the user; with `web-search-on`, any fact the model may look up is named in the prompt with the source it must match.
- Build a reconciliation table after generation — rendered string → input slot (TITLE, HEADING_n, BODY_n, STAT_n, FOOTER) → match/mismatch — and confirm the rendered-string count equals the input-string count; anything unmapped is removed.
- Make pictograms and icons either non-quantitative or count-matched to their stat.

---

## Verification

- [ ] Every label / stat / header / footer in EXACT TEXT.
- [ ] Section count matches grid (e.g., 6 sections = 2×3 or 3×2).
- [ ] `quality="high"` set.
- [ ] Fact-grounding mode stated explicitly.
- [ ] Brand palette hex codes provided.
- [ ] Single typeface family specified.
- [ ] Failure conditions stated (typos, unequal panels).
