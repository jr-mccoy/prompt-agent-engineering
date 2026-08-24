---
title: "Kids Coloring Page - Simple Bold Outlines"
category: image-generation/coloring-book
description: "Generate a simple, bold, thick-outline coloring page for young children (ages 2-6) with large open areas, few regions, and friendly subjects — pure black line art on white, print-ready."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-11
  - SV-13
  - SV-14
  - SV-16
  - SV-17
  - SV-18
difficulty: beginner
tags:
  - coloring-book
  - image-generation
  - kids-coloring
  - toddler
  - bold-outlines
  - line-art
  - print-ready
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - adult_coloring_page_intricate.md
  - educational_coloring_page.md
  - themed_coloring_set.md
  - image_to_coloring_book_page.md
---

# Kids Coloring Page - Simple Bold Outlines

**Purpose:** Generate a simple, friendly coloring page for young children (ages 2-6) with very bold, thick outlines, a small number of large open colorable areas, and a single clearly recognizable subject. Pure black line art on white, ready to print.

**Format / Dimensions:** Single flat page, 8.5" x 11" portrait (letter) at 300 DPI. Pure line art, no color, no grayscale.

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core print techniques
- [adult_coloring_page_intricate.md](adult_coloring_page_intricate.md) — the fine-detail counterpart for adults
- [educational_coloring_page.md](educational_coloring_page.md) — add a letter/number/fact to the page
- [image_to_coloring_book_page.md](image_to_coloring_book_page.md) — convert an existing image into a kids' page

---

## Image Generation Prompt (Production-Ready)

```
TASK: Generate ONE FLAT PRINT ARTWORK IMAGE that is a SIMPLE COLORING PAGE FOR YOUNG CHILDREN (ages 2-6).

IMPORTANT REAL-WORLD CONTEXT:
This is a coloring page for a TODDLER or PRESCHOOLER.
It will be PRINTED on letter-size paper.
A small child with limited motor control will color it with CHUNKY crayons.
Areas must be big and outlines must be thick so the child can color inside them.

This is NOT a finished illustration.
This is NOT a grayscale or shaded drawing.
This is NOT a sketch, a mockup, or a photo of a book.
This image IS the literal black ink-on-paper line art sent directly to a printer.

SUBJECT (fill in): [e.g. a smiling cartoon elephant / a happy round sun / a friendly dump truck / a single big flower]

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY ONE IMAGE.
- PURE BLACK line art (#000000) on PURE WHITE (#FFFFFF) background.
- NO color anywhere.
- NO grayscale, NO gray tones.
- NO shading, hatching, crosshatching, or solid black fills.
- NO gradients of any kind.
- NO filled regions — every enclosed space stays WHITE so a child can color it.
- Single flat page, viewed straight-on. NOT a 3D render, NOT a book mockup.

If any gray tone, shading, color, or solid black fill appears, the output is INCORRECT.

================================================
LINE ART SPECIFICATIONS (BOLD FOR LITTLE HANDS)
================================================

- VERY thick, bold outlines: 4 pt to 6 pt line weight.
- Simple, rounded, friendly shapes — no sharp scary points.
- All shapes have CLOSED outlines (no gaps).
- Few, LARGE colorable regions — aim for 5 to 12 big areas total.
- Minimum colorable region size: about 1 inch across when printed.
- NO tiny details, NO fine texture, NO inner pattern fills.
- One clear central subject. Keep the background nearly empty (maybe a ground line, a sun, or one simple cloud).

================================================
CONTENT & TONE
================================================

- Cheerful, cute, approachable — a happy face if a creature.
- Age-appropriate for ages 2-6: nothing scary, violent, or complex.
- Subject is instantly recognizable.

================================================
COMPOSITION & LAYOUT
================================================

- Large central subject filling most of the page.
- White margin: 0.5 inch clean white border on all four sides.
- No title text, no captions, no watermark, no signature, no page numbers.

================================================
ALLOWED vs FORBIDDEN
================================================

ALLOWED:
- Big, simple, rounded shapes
- Thick bold closed outlines
- One friendly subject with a happy expression
- A tiny bit of simple context (ground line, one cloud/sun)

FORBIDDEN:
- Any color, gray, shading, gradient, or solid black fill
- Thin or delicate lines
- Open / broken outlines
- Small, busy, or intricate detail
- Scary, sad, or complex content
- Background scenery, shadows, or 3D depth
- A picture OF a coloring book (mockup)

================================================
OUTPUT SPECIFICATIONS
================================================

- Dimensions: 8.5 x 11 inches, portrait.
- Resolution: 300 DPI (2550 x 3300 px).
- Background: pure white (#FFFFFF) only — no texture, no vignette, no fade.

================================================
FINAL VALIDATION CHECK
================================================

- [ ] Exactly one image
- [ ] Pure black lines only — no gray, no color
- [ ] Every interior space is pure white (colorable)
- [ ] NO shading, gradients, or solid black fills
- [ ] VERY thick bold outlines (4-6 pt), fully closed
- [ ] Only 5-12 large colorable regions
- [ ] Friendly, simple, recognizable subject
- [ ] 0.5 inch clean white margin on all sides
- [ ] No text, watermark, or signature
- [ ] Flat page, not a mockup or 3D render

If ANY shading, fill, gray tone, or color appears, the output is INCORRECT.
If the lines are thin or the detail is busy, the output is INCORRECT for this age.

================================================
GENERATE NOW
================================================

Produce a single bold, simple black-and-white coloring page for young children following all rules above.
```

---

## Simplified Prompt (If Full Prompt Misbehaves)

```
Create ONE simple coloring page for a young child (age 2-6) as black line art on a pure white background.

RULES:
- Subject: [your subject, e.g. a smiling cartoon elephant]
- VERY thick bold black outlines (4-6 pt) — NO color, NO gray, NO shading, NO fills
- Only a few LARGE areas to color (5-12), each big enough for chunky crayons
- All shapes fully closed (no gaps), simple rounded friendly shapes
- One clear central subject, almost no background
- 8.5 x 11 inches, portrait, 300 DPI, 0.5 inch white margin
- This is FLAT PRINT LINE ART, not a mockup
- No text, no watermark

If lines are thin, or any shading/fill/color appears, it is WRONG.
```

---

## Why This Prompt Works

1. **Terminology Steering (SV-11)** — "flat print artwork" / "line art" avoids UI and 3D-render tropes.
2. **Grid Forcing + Enumerated Slots (SV-12)** — relaxed to "5-12 large regions" since a toddler page is one big subject, not a grid.
3. **Constraint Redundancy (SV-13)** — bold-outline and no-fill rules repeat across critical rules, line specs, allowed/forbidden, and checklist.
4. **Negative Space Control (SV-14)** — near-empty background plus an explicit white margin keep the page uncluttered.
5. **Allowed vs Forbidden (SV-15)** — explicitly permits a little context (ground line, sun) while forbidding busy detail.
6. **Physical Context Anchoring (SV-16)** — "a small child with chunky crayons" directly drives line weight and region size.
7. **Deliverables Locking (SV-17)** — one image, exact size, DPI, orientation.
8. **Validation Checklist (SV-18)** — final self-audit, including the age-specific "thin lines = incorrect" check.

---

## Model-Specific Notes

### gpt-image-2 (OpenAI, primary)
- `quality="high"` keeps the thick outlines crisp; the page is simple so generation is fast.
- Put the bold-line and large-region rules under CONSTRAINTS.
- Do NOT pass `input_fidelity` (disabled).

### Nano Banana (Gemini 3 Pro Image / Gemini 3.1 Flash Image, primary)
- Markdown + ALL-CAPS for `MUST`/`NEVER`; specify `#000000` lines on `#FFFFFF`.
- State "very thick bold outlines, like a toddler coloring book" — Nano Banana responds to comparative anchors.
- Iterate conversationally if regions come out too small ("make fewer, bigger areas; thicker outlines").

### DALL-E 3 (legacy)
Add: `"simple bold coloring book page for toddlers, thick black outlines, large areas, no shading, no color, white background"`

### Midjourney (legacy)
```
simple [subject] coloring page for toddlers, very thick bold black outlines, large open areas, white background
--ar 17:22 --v 6 --style raw --s 15
--no color shading gray gradient fill thin lines detail 3d mockup photo
```
`--no color shading` plus low `--s` keeps it flat and simple.

### Stable Diffusion (legacy)
- A **lineart ControlNet** with a simple input gives the cleanest bold closed outlines.
Positive: `"simple toddler coloring page, thick bold black outlines, large open areas, clean closed lines, white background"`
Negative: `"shading, grayscale, gray, color, gradient, fill, thin lines, intricate, detailed, texture, realistic"`

---

## Troubleshooting

### Problem: Lines too thin for a toddler
**Add:** `"Outlines must be VERY thick, 4-6 pt, like a board-book coloring page. Thin lines = rendering error."`

### Problem: Too many tiny areas
**Add:** `"Reduce to 5-12 LARGE colorable areas. Remove all small detail and inner patterns."`

### Problem: Shading or solid fills appear
**Add:** `"Every area stays pure white. NO gray, NO shading, NO solid black fill anywhere."`

### Problem: Subject looks scary or complex
**Add:** `"Make it cute and friendly with a happy face, simple and rounded, suitable for a 3-year-old."`

### Problem: It rendered a photo of a coloring book
**Add:** `"This IS the page, flat and straight-on. No book, no desk, no shadow, no 3D."`

---

## Verification Checklist

- [ ] Exactly one image generated
- [ ] Pure black outlines, pure white interiors (no color, no gray)
- [ ] No shading, gradients, or solid black fills
- [ ] Outlines very thick (4-6 pt) and fully closed
- [ ] Only 5-12 large colorable regions, each ~1 inch+
- [ ] Friendly, simple, instantly recognizable subject
- [ ] 0.5 inch clean white margin on all sides
- [ ] 8.5 x 11 in, 300 DPI, portrait
- [ ] No text, watermark, or signature
- [ ] Flat line art, not a mockup or 3D render

---

*Updated: 2026-06-23*
