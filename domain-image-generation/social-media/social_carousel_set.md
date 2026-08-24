---
title: "Social — Carousel Set (Consistent Template)"
category: image-generation/social
description: "Multi-slide carousel where every slide shares one consistent template — same grid, fonts, colors, and brand frame — with verbatim per-slide copy."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-11
  - SV-13
  - SV-15
  - SV-17
difficulty: advanced
tags:
  - social-media
  - carousel
  - template-consistency
  - multi-slide
  - typography
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/social-media/README.md
  - domain-image-generation/social-media/social_quote_graphic.md
  - domain-image-generation/social-media/social_announcement_post.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# Social — Carousel Set (Consistent Template)

**Objective:** Generate a multi-slide social carousel (Instagram/LinkedIn swipe set) where every slide shares one consistent template — identical layout grid, fonts, color system, margins, and brand frame — while each slide carries its own verbatim copy. The throughline must read as a single designed set, not a collection of unrelated images.

**Why Nano Banana Pro (primary):** Carousels are text-heavy and consistency-critical. `gemini-3-pro-image` combines near-perfect text rendering with **system prompts** that lock the template (fonts, palette, layout, brand frame) across every slide generation — the single most reliable way to keep a multi-slide set visually unified with accurate copy.

**Why gpt-image-2 (alternate):** When you want a cover + a few slides in one coherent pass, gpt-image-2's one-pass multi-panel consistency and 95%+ text rendering work well — and `quality="high"` keeps per-slide copy legible. Use it for shorter sets or the cover/hero slide.

> Skip Nano Banana 2 / Midjourney / SD for carousels carrying real copy — text fidelity across many slides will drift.

**API parameters:**

Nano Banana Pro (primary — system-prompt locked template):
- `model="gemini-3-pro-image"`
- `size="1080x1350"` (4:5 portrait — best feed real estate) or `1080x1080`
- `quality="high"`
- `n=1` per slide (generate slides individually under one system prompt for tightest consistency)

gpt-image-2 (alternate — cover + short set):
- `model="gpt-image-2"`
- `size="1024x1024"` or portrait equivalent
- `quality="high"`
- `n=1` per slide; `n=4` for cover variations

---

## Inputs

- `[CAROUSEL TOPIC]` — the throughline (e.g., "5 mistakes first-time founders make")
- `[SLIDE COUNT]` — number of slides (typically 5–10)
- `[SLIDE COPY]` — per-slide verbatim text: headline + body for each slide, plus cover and CTA
- `[PLATFORM + RATIO]` — Instagram 1080×1350 (4:5) / 1080×1080 (1:1) / LinkedIn 1200×1200
- `[BRAND PALETTE]` — background hex, headline hex, body hex, accent hex
- `[FONT SYSTEM]` — headline font character + body font character
- `[BRAND FRAME]` — recurring elements: logo position, slide number style, footer handle, accent shape
- `[STYLE]` — minimal / bold editorial / illustrated-accent

---

## Constraints (Must / Must Not)

**Must:**
- Every slide uses the SAME template: identical margins, grid, fonts, palette, and brand frame.
- Render all per-slide copy 100% verbatim.
- Show slide progression cues consistently (e.g., "1/7", "2/7") in the same position and style.
- Keep a designed visual relationship between cover and content slides.
- Keep all text crop-safe (≥8% inset) and high-contrast.

**Must Not:**
- Let fonts, colors, margins, or the brand frame drift between slides.
- Paraphrase, truncate, or invent slide copy.
- Reposition the logo/handle/slide-number between slides.
- Overload any single slide with text (carousels favor one idea per slide).
- Break the cover/content visual relationship.

---

## Production Prompt — Nano Banana Pro (System Prompt + Per-Slide)

```
SYSTEM PROMPT (apply identically to every slide in this carousel):
You are producing a [SLIDE COUNT]-slide social carousel for [CAROUSEL TOPIC], [PLATFORM + RATIO], in a [STYLE] style.
TEMPLATE (locked across all slides):
- Background: [background hex]. Headline color: [headline hex]. Body color: [body hex]. Accent: [accent hex].
- Fonts: headline = [headline font character]; body = [body font character].
- Margins: consistent safe margins, all text inset ≥8% from edges.
- Brand frame: [logo at (position)], slide-number indicator "[n]/[SLIDE COUNT]" at [position] in [accent hex], footer handle "[handle]" at [position].
- Every slide must look like part of the same designed set: same grid, same type scale, same frame.
Render all copy 100% verbatim. Never paraphrase or invent text.

PER-SLIDE TASK (repeat for each slide, changing only the copy):
Slide [n] of [SLIDE COUNT].
HEADLINE (verbatim): "[slide n headline]"
BODY (verbatim): "[slide n body]"
Place the slide-number indicator "[n]/[SLIDE COUNT]". Keep the template exactly as defined in the system prompt.

CONSTRAINTS:
- MUST: identical template, fonts, palette, margins, and brand frame on every slide; verbatim copy; consistent slide-number position; crop-safe high-contrast text.
- MUST NOT: drift fonts/colors/margins/frame, paraphrase or invent copy, reposition brand elements, or overload a slide.
- If any slide deviates from the locked template or any copy differs from the text above, the output is INCORRECT.
- Quality: "high"
```

Cover slide: use the same system prompt but with the cover headline/hook copy, and (optionally) a "Swipe →" cue in `[accent hex]`.

---

## Production Prompt — gpt-image-2 (Cover + Short Set)

```
SCENE:
A [STYLE] social carousel template, [PLATFORM + RATIO]. Background: [background hex]. Consistent safe margins.

SUBJECT — this slide (Slide [n] of [SLIDE COUNT]):
Template (must match every other slide): headline in [headline font character] / [headline hex]; body in [body font character] / [body hex]; accent [accent hex]; brand frame = [logo at position], slide number "[n]/[SLIDE COUNT]" at [position], footer handle "[handle]".

EXACT TEXT (verbatim):
HEADLINE: "[slide n headline]"
BODY: "[slide n body]"
SLIDE NUMBER: "[n]/[SLIDE COUNT]"

KEY DETAILS:
- One idea per slide; generous spacing; clear hierarchy headline > body.
- All text inset ≥8% from edges (crop-safe); strong contrast.
- This slide must be visually identical in template to the rest of the set — same grid, type scale, palette, and frame.

USE CASE:
Multi-slide social carousel. Posted as a swipe set; all slides must read as one designed system.

CONSTRAINTS:
- Style commitment: clean designed template graphic, consistent across the set.
- EXACT TEXT verbatim as above; forbidden: paraphrase, truncation, invented/lorem-ipsum text.
- Forbidden: template drift between slides, repositioned brand elements, low contrast, overloaded slide.
- Format: [PLATFORM + RATIO].

If this slide's template differs from the rest of the set, or any copy differs from the text above, the output is INCORRECT.
```

---

## Iteration Plan

1. "Slide 4's headline font is heavier than the rest — match it to the locked [headline font character]."
2. "The slide-number indicator moved on slide 3 — return it to [position] in [accent hex] on every slide."
3. "Slide 2 dropped a word — re-render its body 100% verbatim: \"[slide 2 body]\"."
4. "The background hex shifted between slides — normalize all slides to [background hex]."
5. "The cover doesn't relate visually to the content slides — apply the same grid and type scale."

---

## Verification

- [ ] Every slide uses an identical template (margins, grid, fonts, palette, brand frame).
- [ ] All per-slide copy rendered 100% verbatim.
- [ ] Slide-number indicator consistent in position and style across slides.
- [ ] Cover and content slides share a clear visual relationship.
- [ ] All text crop-safe (≥8% inset) and high-contrast.
- [ ] One idea per slide; no overloaded slides.
- [ ] No template drift or repositioned brand elements.
- [ ] `quality="high"` set (mandatory for text).
- [ ] Correct platform aspect ratio.
