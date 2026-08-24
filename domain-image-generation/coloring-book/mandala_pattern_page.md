---
title: "Mandala Pattern Coloring Page (Radial Symmetry)"
category: image-generation/coloring-book
description: "Generate a symmetric mandala coloring page with controllable radial symmetry (4/6/8/12/16-fold) and complexity level — pure black-on-white print-ready line art, perfectly centered, no shading or fills."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-11
  - SV-13
  - SV-14
  - SV-17
  - SV-18
difficulty: intermediate
tags:
  - coloring-book
  - image-generation
  - mandala
  - radial-symmetry
  - geometric
  - line-art
  - print-ready
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - adult_coloring_page_intricate.md
  - coloring_book_kdp_interior.md
  - themed_coloring_set.md
---

# Mandala Pattern Coloring Page (Radial Symmetry)

**Purpose:** Generate a mandala coloring page with controllable **radial symmetry** (4-, 6-, 8-, 12-, or 16-fold) and a chosen **complexity level**. The output is a perfectly centered, symmetric black-line mandala on pure white, ready to print and color.

**Format / Dimensions:** Single flat page, 8.5" x 11" portrait (letter) at 300 DPI, with the mandala centered as a square design (square aspect inside the portrait page). Pure line art, no color, no grayscale.

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core print techniques
- [adult_coloring_page_intricate.md](adult_coloring_page_intricate.md) — non-radial intricate detail
- [coloring_book_kdp_interior.md](coloring_book_kdp_interior.md) — wrap mandalas into a published book
- [themed_coloring_set.md](themed_coloring_set.md) — generate a matched mandala series

---

## Symmetry & Complexity Controls

| Control | Options | Effect |
|---|---|---|
| Fold symmetry | 4 / 6 / 8 / 12 / 16-fold | Number of identical wedges repeated around the center |
| Complexity | low / medium / high / very-high | Ring count and motif density |
| Ring count | 3-5 (low) → 8-12 (very-high) | Concentric bands of pattern from center to rim |
| Center motif | dot / flower / star / geometric | The anchor at the exact center |
| Line weight | 1 pt (intricate) → 3 pt (relaxed) | Adjust to colorist skill / age |

---

## Image Generation Prompt (Production-Ready)

```
TASK: Generate ONE FLAT PRINT ARTWORK IMAGE that is a SYMMETRIC MANDALA COLORING PAGE.

IMPORTANT REAL-WORLD CONTEXT:
This is a mandala coloring page.
It will be PRINTED on letter-size paper.
A person will color it in with markers, gel pens, or colored pencils.
The appeal is its perfect radial symmetry and meditative repetition.

This is NOT a finished illustration.
This is NOT a grayscale or shaded drawing.
This is NOT a sketch, a mockup, or a photo of a book.
This image IS the literal black ink-on-paper line art sent directly to a printer.

MANDALA PARAMETERS (fill in):
- Fold symmetry: [e.g. 8-fold]
- Complexity: [low / medium / high / very-high]
- Number of concentric rings: [e.g. 6]
- Center motif: [e.g. small 8-petal flower]
- Outer rim style: [e.g. pointed petal border]
- Line weight: [e.g. 1.5 pt]

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY ONE IMAGE.
- PURE BLACK line art (#000000) on PURE WHITE (#FFFFFF) background.
- NO color anywhere.
- NO grayscale, NO gray tones.
- NO shading, hatching, crosshatching, or solid black fills.
- NO gradients of any kind.
- NO filled regions — every enclosed space stays WHITE so it can be colored.
- Single flat page, viewed straight-on. NOT a 3D render, NOT a book mockup.

If any gray tone, shading, color, or solid black fill appears, the output is INCORRECT.

================================================
SYMMETRY RULES (MOST IMPORTANT)
================================================

- The mandala MUST have EXACT [N]-fold radial symmetry: the design is built from [N] identical wedges rotated around a single center point.
- The design MUST be PERFECTLY CENTERED on the page; the center of the mandala is the center of the design area.
- The mandala is CIRCULAR overall (fits within a circle), built from [number] CONCENTRIC RINGS of pattern, from the center motif outward to the rim.
- Each ring is itself symmetric and repeats its motif [N] times (or a multiple of [N]).
- Every wedge is an exact copy — no asymmetry, no off-center elements, no stray marks.

================================================
LINE ART SPECIFICATIONS
================================================

- Line weight: [as specified above, default 1.5 pt], consistent throughout.
- Crisp, smooth, CLOSED outlines — no gaps so colors won't bleed between regions.
- Detail scales with COMPLEXITY: low = bold, few rings, open areas; very-high = fine, many rings, dense intricate motifs.
- Decorative fills (dots, scallops, petals, lattice) allowed ONLY as open outlined shapes, never solid black.
- Leave a mix of small intricate regions and a few larger regions for color variety.

================================================
COMPOSITION & LAYOUT
================================================

- The circular mandala is centered and as large as fits within the margins.
- White margin: 0.5 inch clean white border on all four sides.
- Corners of the page (outside the circle) stay pure white (or carry a small symmetric corner flourish if requested).
- No title text, no captions, no watermark, no signature, no page numbers.

================================================
ALLOWED vs FORBIDDEN
================================================

ALLOWED:
- Exact radial symmetry and concentric rings
- Outlined decorative motifs and pattern fills
- Optional small symmetric corner flourishes

FORBIDDEN:
- Any color, gray, shading, gradient, or solid black fill
- Asymmetry, off-center placement, or an incomplete circle
- Open / broken outlines
- Background scenery, shadows, or 3D depth
- A picture OF a coloring book (mockup)

================================================
OUTPUT SPECIFICATIONS
================================================

- Dimensions: 8.5 x 11 inches, portrait. (Square 8.5 x 8.5 in if a square page is requested.)
- Resolution: 300 DPI (2550 x 3300 px for letter).
- Background: pure white (#FFFFFF) only — no texture, no vignette, no fade.

================================================
FINAL VALIDATION CHECK
================================================

- [ ] Exactly one image
- [ ] EXACT [N]-fold radial symmetry, perfectly centered
- [ ] Circular mandala built from the specified concentric rings
- [ ] Pure black lines only — no gray, no color
- [ ] Every interior space is pure white (colorable)
- [ ] NO shading, gradients, or solid black fills
- [ ] Outlines fully closed; line weight as specified
- [ ] 0.5 inch clean white margin on all sides
- [ ] No text, watermark, or signature
- [ ] Flat page, not a mockup or 3D render

If the symmetry is broken or the mandala is off-center, the output is INCORRECT.
If ANY shading, fill, gray tone, or color appears, the output is INCORRECT.

================================================
GENERATE NOW
================================================

Produce a single perfectly symmetric black-and-white mandala coloring page following all rules above.
```

---

## Simplified Prompt (If Full Prompt Misbehaves)

```
Create ONE symmetric mandala coloring page as black line art on a pure white background.

RULES:
- [N]-fold radial symmetry, perfectly centered, circular, [number] concentric rings
- Center motif: [e.g. small flower]; complexity: [low/medium/high]
- Black outlines only ([line weight] pt) — NO color, NO gray, NO shading, NO fills
- Every enclosed area stays white; all outlines closed
- 8.5 x 11 inches, portrait, 300 DPI, 0.5 inch white margin
- This is FLAT PRINT LINE ART, not a mockup
- No text, no watermark

If the symmetry is broken, off-center, or any shading/fill/color appears, it is WRONG.
```

---

## Why This Prompt Works

1. **Terminology Steering (SV-11)** — "flat print artwork" / "line art" avoids UI and 3D-render tropes.
2. **Grid Forcing + Enumerated Slots (SV-12)** — substituted by an explicit symmetry contract (N identical wedges, named concentric rings), which is the mandala equivalent of a layout grid.
3. **Constraint Redundancy (SV-13)** — no-fill, symmetry, and centering rules repeat across critical rules, symmetry rules, allowed/forbidden, and checklist.
4. **Negative Space Control (SV-14)** — pure white corners, white margin, no scenery or vignette.
5. **Allowed vs Forbidden (SV-15)** — permits outlined pattern fills and corner flourishes while forbidding solid fills and asymmetry.
6. **Physical Context Anchoring (SV-16)** — "meditative, colored with gel pens on letter paper" sets density and line weight.
7. **Deliverables Locking (SV-17)** — one image, exact symmetry order, ring count, dimensions, DPI, orientation.
8. **Validation Checklist (SV-18)** — final self-audit that explicitly re-checks symmetry and centering.

---

## Model-Specific Notes

### gpt-image-2 (OpenAI, primary)
- `quality="high"` keeps fine ring detail crisp.
- State the fold symmetry as a hard number ("EXACT 8-fold"); gpt-image-2 honors enumerated constraints well.
- Do NOT pass `input_fidelity` (disabled).

### Nano Banana (Gemini 3 Pro Image / Gemini 3.1 Flash Image, primary)
- Markdown + ALL-CAPS; specify `#000000` on `#FFFFFF`.
- Nano Banana Pro's reasoning step helps with true radial symmetry — explicitly say "perfectly symmetric, all wedges identical, centered."
- Iterate ("recenter the mandala; make all 8 wedges identical; remove gray") instead of regenerating.

### DALL-E 3 (legacy)
Add: `"symmetric mandala coloring page, black line art, radial symmetry, centered, no shading, no color, white background"`. DALL-E sometimes breaks exact symmetry — verify visually.

### Midjourney (legacy)
```
symmetric mandala coloring page, [N]-fold radial symmetry, clean black line art, centered, white background
--ar 17:22 --v 6 --style raw --s 25
--no color shading gray gradient fill solid black 3d mockup photo asymmetry
```
Midjourney does mandalas well; `--no color shading` keeps it as clean line art.

### Stable Diffusion (legacy)
- A **lineart ControlNet** seeded with a symmetric input gives the truest radial symmetry; some SD workflows offer a symmetry/kaleidoscope script.
Positive: `"mandala coloring page, radial symmetry, clean black line art, closed outlines, centered, white background, [complexity] detail"`
Negative: `"shading, grayscale, gray, color, gradient, solid black, fill, asymmetry, off-center, realistic, texture"`

---

## Troubleshooting

### Problem: Symmetry is broken / wedges differ
**Add:** `"EXACT [N]-fold symmetry: every one of the [N] wedges must be an identical rotated copy. No variation."`

### Problem: Mandala is off-center
**Add:** `"Center the mandala precisely; the design center is the page center. Equal white space on all sides."`

### Problem: Rings filled solid black
**Add:** `"Pattern fills must be OUTLINED open shapes. NEVER fill a ring or region with solid black; every area stays white."`

### Problem: Gray shading appears
**Add:** `"NO gray of any value. Pure black #000000 lines on pure white #FFFFFF only."`

### Problem: It rendered a photo of a coloring book
**Add:** `"This IS the page, flat and straight-on. No book, no desk, no shadow, no 3D."`

---

## Verification Checklist

- [ ] Exactly one image generated
- [ ] Exact N-fold radial symmetry, all wedges identical
- [ ] Perfectly centered, complete circular mandala with the specified rings
- [ ] Pure black outlines, pure white interiors (no color, no gray)
- [ ] No shading, gradients, or solid black fills; all outlines closed
- [ ] Complexity/line weight match the requested parameters
- [ ] 0.5 inch clean white margin on all sides
- [ ] 8.5 x 11 in (or square), 300 DPI
- [ ] No text, watermark, or signature
- [ ] Flat line art, not a mockup or 3D render

---

*Updated: 2026-06-23*
