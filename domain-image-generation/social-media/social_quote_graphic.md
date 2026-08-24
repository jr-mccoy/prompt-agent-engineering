---
title: "Social — Quote / Typography Graphic"
category: image-generation/social
description: "Quote or typography-led social graphic with verbatim text rendered accurately — exact fonts, hex colors, and placement."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: intermediate
tags:
  - social-media
  - quote-graphic
  - typography
  - text-rendering
  - verbatim-text
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/social-media/README.md
  - domain-image-generation/social-media/social_carousel_set.md
  - domain-image-generation/social-media/social_announcement_post.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# Social — Quote / Typography Graphic

**Objective:** Generate a typography-led social graphic where a quote (or short statement) is the entire design — rendered verbatim, in the specified font character, exact brand hex colors, and a clear visual hierarchy — ready to post without a text-overlay tool.

**Why text rendering matters:** This artifact's whole job is the text. A misspelled or garbled quote is a total failure. That makes model choice the most consequential decision here.

**Why Nano Banana Pro (primary):** `gemini-3-pro-image` has near-perfect text rendering and lets you specify exact fonts, making it the strongest choice for typography-led graphics with verbatim copy. Use it when the quote is long, multilingual, or the typography is the design.

**Why gpt-image-2 (strong alternate):** `gpt-image-2` renders text at 95%+ accuracy with `quality="high"` and gives precise control over layout sections — excellent for shorter quotes and when you want tight control over composition and brand palette. Use it as the alternate, or to batch layout variations with `n=4`.

> Avoid Nano Banana 2 / Midjourney / Stable Diffusion for verbatim-text graphics — text fidelity is not reliable enough.

**API parameters:**

Nano Banana Pro (primary):
- `model="gemini-3-pro-image"`
- `size="1080x1080"` (square feed) — see Inputs for other ratios
- `quality="high"`
- `n=2`

gpt-image-2 (alternate):
- `model="gpt-image-2"`
- `size="1024x1024"`
- `quality="high"` (always high for text)
- `n=4` to explore layouts

---

## Inputs

- `[QUOTE TEXT]` — the verbatim quote/statement (exact, including punctuation)
- `[ATTRIBUTION]` — who said it / handle (verbatim, or "none")
- `[PLATFORM + RATIO]` — Instagram feed 1080×1080 (1:1) / Instagram portrait 1080×1350 (4:5) / X 1600×900 (16:9) / LinkedIn 1200×1200 (1:1)
- `[FONT CHARACTER]` — e.g., "bold geometric sans-serif" / "elegant high-contrast serif" / named font if available
- `[BRAND PALETTE]` — background hex, text hex, accent hex
- `[STYLE]` — minimal / bold editorial / textured / gradient-backed
- `[LOGO/HANDLE]` — small brand mark or @handle placement (optional)

---

## Constraints (Must / Must Not)

**Must:**
- Render `[QUOTE TEXT]` 100% verbatim — exact spelling, punctuation, capitalization, and line content.
- Apply the specified font character and exact hex colors.
- Establish clear hierarchy: quote dominant, attribution secondary, handle/logo smallest.
- Keep all text within safe margins (≥8% inset from every edge) for platform crop safety.
- Maintain strong text/background contrast for legibility on small screens.

**Must Not:**
- Alter, paraphrase, truncate, or "improve" the quote.
- Render lorem ipsum, faux-Latin, or invented words.
- Place text against a busy area where it loses contrast.
- Add decorative elements that crowd or overlap the text.
- Misplace attribution so it reads as part of the quote.

---

## Production Prompt — Nano Banana Pro (Primary)

```
TASK: Create a typography-led social media quote graphic, [PLATFORM + RATIO].

DESIGN:
A [STYLE] quote graphic. The quote is the hero — large, centered, dominant. Attribution sits below it, clearly smaller and secondary. Optional small [LOGO/HANDLE] in a corner.

BACKGROUND: [background hex] — [solid / soft gradient to (second hex) / subtle texture], clean and uncluttered behind the text.

TYPOGRAPHY:
- Font character: [FONT CHARACTER] (use [named font] if available).
- Quote text color: [text hex]. Attribution color: [accent hex].
- Strong contrast between text and background for small-screen legibility.

EXACT TEXT (render 100% verbatim — exact spelling, punctuation, capitalization):
QUOTE: "[QUOTE TEXT]"
ATTRIBUTION: "[ATTRIBUTION]"
HANDLE/LOGO: "[LOGO/HANDLE]"

LAYOUT:
Quote centered with comfortable line breaks and even leading. Attribution below the quote with clear separation. All text inset at least 8% from every edge (crop-safe). Visual hierarchy: quote > attribution > handle.

CONSTRAINTS:
- MUST: render every word of the quote and attribution exactly as written; apply exact fonts and hex colors; keep text crop-safe and high-contrast.
- MUST NOT: paraphrase/alter/truncate the quote, render any invented or lorem-ipsum text, crowd the text with decoration, or break contrast.
- If a single character of the quote or attribution differs from the text above, the output is INCORRECT.
- Quality: "high"
```

---

## Production Prompt — gpt-image-2 (Alternate)

```
SCENE:
A [STYLE] typography-led social quote graphic, [PLATFORM + RATIO]. Background: [background hex] — [solid / soft gradient / subtle texture], clean behind the text.

SUBJECT:
A centered quote as the hero element, with secondary attribution below and an optional small handle/logo in a corner. Clear hierarchy: quote dominant, attribution secondary, handle smallest.

KEY DETAILS:
- Font character: [FONT CHARACTER].
- Quote color: [text hex]. Attribution color: [accent hex]. Background: [background hex]. Use exact hex values.
- Comfortable line breaks and even leading; all text inset ≥8% from edges (crop-safe); strong contrast for small screens.

USE CASE:
Organic social post / quote card. Posted as-is, no external text overlay.

CONSTRAINTS:
- Style commitment: clean designed typography graphic. Not a photo with text slapped on.
- EXACT TEXT (verbatim — exact spelling, punctuation, capitalization):
  QUOTE: "[QUOTE TEXT]"
  ATTRIBUTION: "[ATTRIBUTION]"
  HANDLE/LOGO: "[LOGO/HANDLE]"
- Forbidden: paraphrased/altered/truncated quote, invented or lorem-ipsum text, decoration that crowds the text, low contrast.
- Format: [PLATFORM + RATIO].

If any character of the quote or attribution differs from the text above, the output is INCORRECT.
```

---

## Iteration Plan

1. "The quote dropped a word — re-render it 100% verbatim: \"[QUOTE TEXT]\"."
2. "The attribution is too large and competes with the quote — shrink it and increase separation."
3. "Text contrast is weak against the gradient — darken the background or switch text to [higher-contrast hex]."
4. "Text is too close to the bottom edge — increase the inset to ≥8% for crop safety."
5. "Tighten the line breaks so the quote reads in [N] balanced lines."

---

## Verification

- [ ] `[QUOTE TEXT]` rendered 100% verbatim (spelling, punctuation, capitalization).
- [ ] `[ATTRIBUTION]` correct and clearly secondary.
- [ ] Specified font character + exact hex colors applied.
- [ ] Clear hierarchy: quote > attribution > handle/logo.
- [ ] All text inset ≥8% from edges (crop-safe).
- [ ] Strong text/background contrast for small screens.
- [ ] No invented/lorem-ipsum text; no decoration crowding the text.
- [ ] `quality="high"` set (mandatory for text).
- [ ] Correct platform aspect ratio.
