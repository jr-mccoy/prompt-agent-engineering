---
title: "T-Shirt / Apparel Graphic"
category: image-generation/merch-print-on-demand
description: "Isolated apparel graphic on transparent/solid background with print-area and screen-print color-count constraints."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: advanced
tags:
  - tshirt
  - apparel
  - merch
  - print-on-demand
  - transparent-background
  - screen-print
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/merch-print-on-demand/sticker_design.md
  - domain-image-generation/merch-print-on-demand/print_on_demand_pattern.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# T-Shirt / Apparel Graphic

**Objective:** Produce an isolated apparel graphic that drops cleanly onto a garment — subject on a transparent (or single solid) background, sized for a defined print area, with the color count constrained for screen-print feasibility and any text rendered verbatim.

**Why this model:** Apparel graphics blend creative illustration with hard print constraints — isolated background, defined print area, and a limited flat-color palette for screen-printing. Use **gpt-image-2** (`quality="high"`, `background="transparent"`) for clean isolation and verbatim text. **Nano Banana Pro** (`gemini-3-pro-image`) is the pick when the graphic is text-heavy (slogan tees) and needs exact font control. For purely illustrative, text-free, full-color DTG art, Nano Banana 2 or Midjourney can explore — but isolate the subject afterward.

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `size="1024x1024"` (square print area) or `1024x1536` (tall front print), `quality="high"`, `background="transparent"`, `n=4`
- Nano Banana Pro path: `model="gemini-3-pro-image"`, square/portrait aspect, `quality="high"`, request a flat solid background to key out in post if transparent isn't native

**Print methods (drives the palette constraint):**
- **Screen-print / vinyl:** flat spot colors only, limited count (state N). No gradients, no soft shadows, no fine halftone unless the printer supports it.
- **DTG / sublimation:** full color and gradients allowed.

---

## Inputs

- `[CONCEPT]` — the graphic idea ("retro mountain sunrise badge", "vintage typographic slogan")
- `[SLOGAN / TEXT]` — verbatim text on the graphic (optional)
- `[STYLE]` — vintage, line-art, mascot, distressed, minimalist, retro-badge
- `[PRINT METHOD]` — screen-print / vinyl / DTG / sublimation
- `[COLOR COUNT]` — if screen-print/vinyl: number of flat spot colors (e.g., 3)
- `[PALETTE]` — hex codes
- `[GARMENT COLOR]` — the shirt color the art sits on (drives contrast + whether to include a knockout)
- `[BACKGROUND]` — transparent / single solid hex
- `[PRINT AREA]` — target placement + max dimensions (e.g., "front chest, 11×14 in max")
- `[FORBIDDEN]` — to avoid

---

## Constraints (Must / Must Not)

**Must:**
- Isolate the subject on a transparent or single solid background — no scene, no environment, no mockup garment.
- Keep the whole design inside a centered print area with clean margin (it will be placed on a garment).
- If `[PRINT METHOD]` = screen-print/vinyl: restrict to exactly `[COLOR COUNT]` flat colors, no gradients, no soft drop shadows, no anti-aliased glows.
- Ensure contrast against `[GARMENT COLOR]` (design a knockout/outline if the art would disappear on that color).
- Render `[SLOGAN / TEXT]` verbatim in an EXACT TEXT block when present.

**Must Not:**
- Render a t-shirt mockup, a person wearing the shirt, a hanger, or any product staging — output the GRAPHIC only.
- Add a background scene, gradient backdrop, or drop shadow on a transparent output.
- Use trademarked logos, characters, or brand marks.
- Exceed the stated color count for screen-print.
- Misspell the slogan.

---

## Production Prompt (gpt-image-2)

```
DELIVERABLE:
A single ISOLATED apparel graphic — the artwork ONLY, on a [transparent / solid
[HEX]] background. This is print artwork to be placed on a garment, NOT a product
photo. No t-shirt, no model, no hanger, no mockup, no scene, no backdrop.

ARTWORK:
Concept: [CONCEPT]. Style: [STYLE]. Centered, self-contained composition with clean
margin on all sides, sized to fit a [PRINT AREA] print zone.

COLOR / PRINT METHOD:
- Print method: [PRINT METHOD].
- [If screen-print/vinyl: use EXACTLY [COLOR COUNT] flat spot colors — [HEX], [HEX],
  [HEX]. NO gradients, NO soft drop shadows, NO glows, NO anti-aliased blends. Every
  shape is a flat solid fill.]
- [If DTG/sublimation: full color allowed; palette anchored on [HEX], [HEX], [HEX].]
- Garment color it will sit on: [GARMENT COLOR]. Ensure strong contrast; add a clean
  knockout/outline if the art would otherwise disappear on that color.

TEXT (if [SLOGAN / TEXT] present — verbatim):
- "[SLOGAN / TEXT]" — [face fitting the style], [weight], [HEX]. Integrated into the
  graphic, 100% readable.

CONSTRAINTS:
- Background: [transparent / single flat [HEX]] only. Nothing else in the frame.
- Output the graphic in isolation — absolutely no garment, model, hanger, or mockup.
- [If screen-print: do not exceed [COLOR COUNT] colors; no gradients/shadows/glows.]
- EXACT TEXT only, verbatim, no extra characters; no invented copy.
- Forbidden: trademarked logos/characters/marks, [FORBIDDEN], watermarks, lorem ipsum,
  background scenes, drop shadows on transparent output.
- Format: square/portrait print area, centered with margin.

If the output shows a shirt/model/mockup, includes a background scene, exceeds the
color count (screen-print), or misspells the slogan, the output is incorrect.
```

## Production Prompt (Nano Banana Pro)

```
TASK: Create an ISOLATED apparel graphic (artwork only — no garment, model, hanger,
or mockup) for placement on a shirt. Concept: [CONCEPT]. Style: [STYLE]. Centered,
self-contained, with clean margin, sized for a [PRINT AREA] zone.

BACKGROUND: [transparent / single flat [HEX]]. Nothing else in frame. (If transparent
isn't native, render on a flat solid [HEX] field for keying out in post.)

COLOR:
- Method: [PRINT METHOD].
- [Screen-print/vinyl: exactly [COLOR COUNT] flat spot colors — [HEX], [HEX], [HEX].
  No gradients, shadows, or glows.] [DTG: full color anchored on the palette.]
- Sits on [GARMENT COLOR]: ensure contrast; add a knockout/outline if needed.

TEXT (if present, render exactly): "[SLOGAN / TEXT]" — [face], [weight], [HEX].

CONSTRAINTS:
- MUST: isolated graphic only; correct background; color-count discipline (screen-print);
  garment contrast; verbatim text.
- MUST NOT: render a shirt/model/mockup/scene; add gradients/shadows on a transparent
  output; exceed the color count; use trademarks; misspell text; use [FORBIDDEN].
- Quality: "high".
```

---

## Iteration Plan

1. "It rendered a t-shirt mockup — output the graphic ONLY on a transparent background, no garment."
2. "Color-count violation — flatten gradients/shadows down to the [COLOR COUNT] flat spot colors for screen-print."
3. "The art disappears on [GARMENT COLOR] — add a clean knockout/outline for contrast."
4. "Subject is cropped too close to the edge — re-center with a clean margin inside the print area."

---

## Verification

- [ ] Graphic is isolated on transparent or single solid background — no garment/model/mockup/scene.
- [ ] Subject centered with clean margin, sized for the print area.
- [ ] Screen-print: exactly `[COLOR COUNT]` flat colors, no gradients/shadows/glows.
- [ ] Contrast against `[GARMENT COLOR]` (knockout/outline if needed).
- [ ] Any slogan in an EXACT TEXT block, verbatim.
- [ ] No trademarks; no drop shadow on transparent output.
- [ ] `quality="high"` (and `background="transparent"` on gpt-image-2 if applicable).
