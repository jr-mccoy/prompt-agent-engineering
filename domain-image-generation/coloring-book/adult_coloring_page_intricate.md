---
title: "Adult Coloring Page - Intricate (Zentangle / Floral / Geometric)"
category: image-generation/coloring-book
description: "Generate a highly detailed, fine-line adult coloring page (zentangle, florals, geometric, paisley, mandala-adjacent) as pure black-on-white print-ready line art with no shading or fills."
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
  - adult-coloring
  - zentangle
  - line-art
  - print-ready
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - kids_coloring_page_simple.md
  - mandala_pattern_page.md
  - coloring_book_kdp_interior.md
  - themed_coloring_set.md
---

# Adult Coloring Page - Intricate (Zentangle / Floral / Geometric)

**Purpose:** Generate a highly detailed adult coloring page with fine line weight and dense, intricate detail (zentangle, layered florals, geometric tessellations, paisley). The output is pure black outlines on pure white, ready to print and color.

**Format / Dimensions:** Single flat page, 8.5" x 11" portrait (letter) by default — also supports A4 (8.27" x 11.69"), at 300 DPI. Pure line art, no color, no grayscale.

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core print techniques cited below
- [kids_coloring_page_simple.md](kids_coloring_page_simple.md) — the bold, simple counterpart for young children
- [mandala_pattern_page.md](mandala_pattern_page.md) — radial-symmetry variant
- [coloring_book_kdp_interior.md](coloring_book_kdp_interior.md) — wrap this style into a publishable book

---

## Image Generation Prompt (Production-Ready)

```
TASK: Generate ONE FLAT PRINT ARTWORK IMAGE that is an INTRICATE ADULT COLORING PAGE.

IMPORTANT REAL-WORLD CONTEXT:
This is a coloring page for ADULTS.
It will be PRINTED on letter-size paper.
An adult will color it in with fine markers, gel pens, or colored pencils.
The pleasure of the page is in its dense, meditative detail.

This is NOT a finished illustration.
This is NOT a grayscale or shaded drawing.
This is NOT a sketch, a mockup, or a photo of a book.
This image IS the literal black ink-on-paper line art sent directly to a printer.

THEME (fill in): [e.g. layered peony-and-vine floral / geometric zentangle tessellation / paisley garden / botanical mandala]

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY ONE IMAGE.
- PURE BLACK line art (#000000) on PURE WHITE (#FFFFFF) background.
- NO color anywhere.
- NO grayscale, NO gray tones.
- NO shading, hatching, crosshatching, stippling used as shading, or solid black fills.
- NO gradients of any kind.
- NO filled regions — every enclosed space stays WHITE so it can be colored.
- Single flat page, viewed straight-on. NOT a 3D render, NOT a book mockup, NOT a page-on-a-desk scene.

If any gray tone, shading, color, or solid black fill appears, the output is INCORRECT.

================================================
LINE ART SPECIFICATIONS
================================================

- Fine, consistent line weight: 1 pt to 1.5 pt.
- Crisp, smooth, confident lines — NOT sketchy, NOT rough, NOT doubled.
- All shapes have CLOSED outlines (no gaps) so colors won't bleed between regions.
- High detail and density: small intricate motifs, layered patterns, repeated decorative fills drawn as OUTLINES (not as solid black).
- Decorative pattern fills (dots, scales, petals, lattice) are allowed ONLY as open outlined shapes, never as solid black areas.
- Balance density: leave a mix of tiny intricate regions and a few larger open regions for visual rest.

================================================
COMPOSITION & LAYOUT
================================================

- Subject fills the page edge-to-edge within the margins, well composed and centered.
- White margin: 0.5 inch clean white border on all four sides (the safe zone for printing/binding).
- No title text, no captions, no watermark, no signature, no page numbers.
- No frame/border decoration unless it is itself clean colorable line art.

================================================
ALLOWED vs FORBIDDEN
================================================

ALLOWED:
- Dense outlined patterns and motifs
- Fine, closed, intricate line work
- Symmetry or organic flow
- Outlined texture (scales, petals, lattice as open shapes)

FORBIDDEN:
- Any solid black areas / ink fills
- Any gray, shading, or gradient
- Any color
- Open / broken outlines
- Sketchy or doubled lines
- Background scenery, shadows, or 3D depth
- A picture OF a coloring book (mockup)

================================================
OUTPUT SPECIFICATIONS
================================================

- Dimensions: 8.5 x 11 inches, portrait. (Use 8.27 x 11.69 in for A4 if requested.)
- Resolution: 300 DPI (2550 x 3300 px for letter).
- Background: pure white (#FFFFFF) only — no texture, no vignette, no fade.

================================================
FINAL VALIDATION CHECK
================================================

- [ ] Exactly one image
- [ ] Pure black lines only — no gray, no color
- [ ] Every interior space is pure white (colorable)
- [ ] NO shading, gradients, or solid black fills
- [ ] Fine but fully closed outlines (no gaps)
- [ ] Intricate, dense, well-balanced detail
- [ ] 0.5 inch clean white margin on all sides
- [ ] No text, watermark, or signature
- [ ] Flat page, not a mockup or 3D render

If ANY shading, fill, gray tone, or color appears, the output is INCORRECT.
If the lines are broken or the page looks like a photo of a book, the output is INCORRECT.

================================================
GENERATE NOW
================================================

Produce a single black-and-white intricate adult coloring page following all rules above.
```

---

## Simplified Prompt (If Full Prompt Misbehaves)

```
Create ONE intricate adult coloring page as black line art on a pure white background.

RULES:
- Theme: [your theme, e.g. detailed floral mandala]
- Fine clean black outlines only (1-1.5 pt) — NO color, NO gray, NO shading, NO solid black fills
- Every enclosed area stays white so it can be colored
- All shapes fully closed (no gaps)
- Dense, intricate, high-detail line work
- 8.5 x 11 inches, portrait, 300 DPI, 0.5 inch white margin
- This is FLAT PRINT LINE ART, not a mockup or 3D render
- No text, no watermark

If any shading, fill, gray, or color appears, it is WRONG.
```

---

## Why This Prompt Works

1. **Terminology Steering (SV-11)** — "flat print artwork" and "line art" steer away from UI/illustration/mockup tropes.
2. **Grid Forcing + Enumerated Slots (SV-12)** — applied loosely here as a single edge-to-edge composition; the strict-grid version lives in [themed_coloring_set.md](themed_coloring_set.md).
3. **Constraint Redundancy (SV-13)** — "no shading / no fills / no color" is repeated in critical rules, line specs, allowed/forbidden, and the checklist.
4. **Negative Space Control (SV-14)** — pure white background, no vignette, no scenery, and an explicit white margin.
5. **Allowed vs Forbidden (SV-15)** — distinguishes legitimate outlined pattern fills from forbidden solid black/gray fills (the #1 intricate-page failure).
6. **Physical Context Anchoring (SV-16)** — "an adult will color it with gel pens on letter paper" sets density and line weight.
7. **Deliverables Locking (SV-17)** — exactly one image, exact dimensions, DPI, and orientation.
8. **Validation Checklist (SV-18)** — final self-audit that re-evaluates every constraint.

---

## Model-Specific Notes

### gpt-image-2 (OpenAI, primary)
- Set `quality="high"` — intricate line art needs the high-detail path to keep fine lines crisp.
- Put the line-art constraints under a CONSTRAINTS block (matches gpt-image-2's 5-section structure).
- Do NOT pass `input_fidelity` (disabled in gpt-image-2).
- The "if X appears, the output is INCORRECT" phrasing is reliable here.

### Nano Banana (Gemini 3 Pro Image / Gemini 3.1 Flash Image, primary)
- Use Markdown structure and ALL-CAPS `MUST`/`NEVER` — Nano Banana parses structured prompts natively.
- Specify `#000000` lines on `#FFFFFF` explicitly rather than "black and white."
- Nano Banana Pro's realism bias can sneak in shading — add "flat line art only, NO rendering, NO depth."
- If a generation is 80% right, iterate conversationally ("remove all gray shading, keep every region white") rather than regenerating.

### DALL-E 3 (legacy)
Add: `"intricate adult coloring book page, fine black line art, no shading, no color, white background, zentangle detail"`

### Midjourney (legacy)
```
[theme] intricate adult coloring page, fine clean black line art, white background, zentangle detail
--ar 17:22 --v 6 --style raw --s 25
--no color shading gray gradient fill solid black 3d mockup photo realistic
```
The `--no color shading` flag is the key lever for line art in Midjourney.

### Stable Diffusion (legacy)
- Use a **lineart ControlNet** for the cleanest closed outlines.
Positive: `"intricate coloring page, fine black line art, clean closed outlines, white background, zentangle, highly detailed"`
Negative: `"shading, grayscale, gray, color, gradient, solid black, fill, realistic, texture, sketch, blurry"`

---

## Troubleshooting

### Problem: Areas filled solid black instead of outlined
**Add:** `"Pattern fills must be OUTLINED open shapes only. NEVER fill any region with solid black. Every area stays white."`

### Problem: Gray shading appears
**Add:** `"NO gray of any value. Only pure black #000000 lines and pure white #FFFFFF space."`

### Problem: Lines too thin / break up when printed
**Add:** `"Minimum line weight 1 pt, fully closed outlines, no broken or hairline strokes."`

### Problem: It rendered a photo of a coloring book
**Add:** `"This IS the page, not a photo OF a page. Flat, straight-on, no book, no desk, no shadow."`

### Problem: Watermark / signature / title text appears
**Add:** `"No text, no signature, no watermark, no page number anywhere."`

---

## Verification Checklist

- [ ] Exactly one image generated
- [ ] Pure black outlines, pure white interiors (no color, no gray)
- [ ] No shading, gradients, hatching-as-shading, or solid black fills
- [ ] All outlines closed (no bleed gaps)
- [ ] Intricate, dense, balanced detail appropriate for adults
- [ ] 0.5 inch clean white margin on all four sides
- [ ] 8.5 x 11 in (or A4), 300 DPI, portrait
- [ ] No text, watermark, signature, or page number
- [ ] Flat line art, not a mockup or 3D render

---

*Updated: 2026-06-23*
