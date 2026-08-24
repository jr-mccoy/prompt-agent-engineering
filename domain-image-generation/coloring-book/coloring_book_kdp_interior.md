---
title: "Coloring Book KDP Interior Page"
category: image-generation/coloring-book
description: "Generate a KDP-ready coloring book interior page with correct trim, bleed, and gutter margins, single-sided guidance, and a consistent style spec that holds across an entire book."
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
difficulty: advanced
tags:
  - coloring-book
  - image-generation
  - kdp
  - self-publishing
  - print-on-demand
  - interior-page
  - line-art
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - coloring_book_cover.md
  - themed_coloring_set.md
  - adult_coloring_page_intricate.md
  - mandala_pattern_page.md
---

# Coloring Book KDP Interior Page

**Purpose:** Generate a single interior page formatted for Amazon KDP (or comparable print-on-demand) coloring books — correct trim size, bleed, and gutter/outer margins, single-sided printing guidance, and a locked style spec so every page across the book looks like it belongs to the same title.

**Format / Dimensions:** Most common KDP coloring trim is **8.5" x 11"**. With full bleed, the document size becomes **8.75" x 11.25"** (adds 0.125" bleed on the three outer edges). Interior at 300 DPI. Pure black line art, no color, no grayscale.

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core print techniques
- [coloring_book_cover.md](coloring_book_cover.md) — the matching cover (color allowed)
- [themed_coloring_set.md](themed_coloring_set.md) — generate a consistent set/series for the book
- [adult_coloring_page_intricate.md](adult_coloring_page_intricate.md) / [mandala_pattern_page.md](mandala_pattern_page.md) — page content styles

---

## KDP Layout Quick Reference

| Element | Value (8.5 x 11 trim) | Notes |
|---|---|---|
| Trim size | 8.5" x 11" | The final cut page |
| Bleed | 0.125" on outer edges | Only if art runs to the edge |
| Doc size with bleed | 8.75" x 11.25" | 8.5 + 0.125 (one outer) + 0.125... see note |
| Outer/top/bottom safe margin | 0.25" minimum from trim | Keep all line art inside |
| Gutter (inside/binding) margin | 0.375" for <150 pages; more as page count grows | Binding eats the inner edge |
| Resolution | 300 DPI | KDP minimum for print |
| Color mode | Grayscale or Black & White interior | Coloring interiors are 1-color |

> **Bleed note:** KDP adds 0.125" bleed to the **outside, top, and bottom** edges, NOT the binding edge. For most coloring books, the safest approach is **no-bleed art**: keep all line art inside the safe margins on a white page, which sidesteps bleed math entirely. Use bleed only for intentional edge-to-edge decorative borders.

> **Single-sided guidance:** Markers and gel pens bleed through paper. Coloring books are usually laid out so colorable art is on **single-sided** pages (or the back of each art page is left blank). When assembling the book, alternate art page / blank page, or instruct KDP-equivalent layout accordingly. Each generated page should be a standalone right-hand (recto) art page.

---

## Image Generation Prompt (Production-Ready)

```
TASK: Generate ONE FLAT PRINT ARTWORK IMAGE that is a KDP-READY COLORING BOOK INTERIOR PAGE.

IMPORTANT REAL-WORLD CONTEXT:
This is ONE interior page of a printed, perfect-bound coloring book sold on Amazon KDP.
It will be PRINTED single-sided at 8.5 x 11 inches.
A person will color it in. The opposite side of the leaf is left blank to avoid marker bleed-through.
Every page in this book must share ONE consistent visual style.

This is NOT a finished illustration.
This is NOT a grayscale or shaded drawing.
This is NOT a sketch, a mockup, or a photo of a book.
This image IS the literal black ink-on-paper line art uploaded to KDP as an interior page.

PAGE SUBJECT (fill in): [e.g. a detailed garden scene with butterflies]
BOOK STYLE LOCK (fill in, keep identical on every page): [e.g. medium-detail botanical line art, 1.5 pt outlines, decorative thin border, bottom-center caption banner left empty]

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY ONE IMAGE (one interior page).
- PURE BLACK line art (#000000) on PURE WHITE (#FFFFFF) background.
- NO color anywhere.
- NO grayscale, NO gray tones.
- NO shading, hatching, crosshatching, or solid black fills.
- NO gradients of any kind.
- NO filled regions — every enclosed space stays WHITE so it can be colored.
- Single flat page, viewed straight-on. NOT a 3D book mockup, NOT a two-page spread.

If any gray tone, shading, color, or solid black fill appears, the output is INCORRECT.

================================================
KDP PAGE GEOMETRY (MOST IMPORTANT)
================================================

- Trim size: 8.5 x 11 inches, portrait.
- Full document canvas: treat as 8.5 x 11 in, 300 DPI (2550 x 3300 px), no-bleed.
- SAFE MARGIN: keep ALL line art at least 0.5 inch from the top, bottom, and OUTER edges.
- GUTTER MARGIN: keep ALL line art at least 0.625 inch from the BINDING (inner) edge — this page is a RIGHT-HAND (recto) page, so the binding is on the LEFT. Leave extra clear space on the left.
- Nothing important (no faces, no key motifs) inside the gutter zone.
- The page background is pure white right to the trim edge (no bleed art).

================================================
LINE ART SPECIFICATIONS (CONSISTENT ACROSS THE BOOK)
================================================

- Line weight: as specified in BOOK STYLE LOCK (default 1.5 pt), identical on every page.
- Crisp, smooth, closed outlines — no gaps, no sketchy or doubled lines.
- Detail level: as specified in BOOK STYLE LOCK, consistent page to page.
- Decorative pattern fills allowed ONLY as open outlined shapes, never solid black.

================================================
COMPOSITION & LAYOUT
================================================

- Single subject/scene composed within the safe area, accounting for the wider left gutter.
- Optional thin decorative border INSIDE the safe margin (must itself be clean colorable line art).
- No title text, no page numbers baked into the art, no watermark, no signature.
  (Page numbers, if any, are added at layout time, not drawn into the art.)

================================================
ALLOWED vs FORBIDDEN
================================================

ALLOWED:
- Closed outlined line art at the locked detail level
- A thin decorative colorable border inside the safe margin
- Consistent style matching the rest of the book

FORBIDDEN:
- Any color, gray, shading, gradient, or solid black fill
- Art crossing into the gutter or past the safe margins
- Edge-to-edge bleed art (unless explicitly requested)
- Open/broken outlines
- Baked-in page numbers, titles, watermarks, signatures
- A two-page spread or a 3D book mockup

================================================
OUTPUT SPECIFICATIONS
================================================

- Dimensions: 8.5 x 11 inches, portrait, 300 DPI (2550 x 3300 px).
- Background: pure white (#FFFFFF) only — no texture, no vignette, no fade.
- Interior color mode target: black & white / grayscale (1-color line art).

================================================
FINAL VALIDATION CHECK
================================================

- [ ] Exactly one image, single page (not a spread)
- [ ] 8.5 x 11 in, portrait, 300 DPI
- [ ] Pure black lines only — no gray, no color
- [ ] Every interior space is pure white (colorable)
- [ ] NO shading, gradients, or solid black fills
- [ ] All art inside 0.5 in outer/top/bottom safe margin
- [ ] All art inside 0.625 in LEFT gutter margin (recto page)
- [ ] Outlines fully closed, line weight matches the book style lock
- [ ] No baked-in page numbers, titles, watermark, or signature
- [ ] Flat page, not a 3D mockup

If ANY shading, fill, gray tone, or color appears, the output is INCORRECT.
If art crosses the gutter or safe margins, the output is INCORRECT.

================================================
GENERATE NOW
================================================

Produce a single KDP-ready coloring book interior page following all rules above.
```

---

## Simplified Prompt (If Full Prompt Misbehaves)

```
Create ONE KDP coloring book interior page as black line art on a pure white background.

RULES:
- Subject: [your subject]; style must match the rest of the book: [your style lock]
- 8.5 x 11 inches, portrait, 300 DPI, single page (not a spread)
- Black outlines only — NO color, NO gray, NO shading, NO fills
- Keep ALL art 0.5 in from top/bottom/outer edges and 0.625 in from the LEFT binding edge
- Every enclosed area stays white; all outlines closed
- No page numbers, titles, watermark, or signature in the art
- This is FLAT PRINT LINE ART for a KDP upload, not a mockup

If art crosses the margins, or any shading/fill/color appears, it is WRONG.
```

---

## Why This Prompt Works

1. **Terminology Steering (SV-11)** — "interior page," "flat print artwork," "uploaded to KDP" frame it as a production file, not a render.
2. **Grid Forcing + Enumerated Slots (SV-12)** — replaced here by explicit page-geometry zones (trim, safe margin, gutter) which act as the layout contract.
3. **Constraint Redundancy (SV-13)** — no-fill and margin rules repeat across geometry, line specs, allowed/forbidden, and checklist.
4. **Negative Space Control (SV-14)** — pure white to the trim, no bleed art by default, explicit gutter clearance.
5. **Allowed vs Forbidden (SV-15)** — permits a decorative colorable border while forbidding gutter intrusion and baked-in page numbers.
6. **Physical Context Anchoring (SV-16)** — "perfect-bound, single-sided, marker bleed-through" drives the single-page and gutter requirements.
7. **Deliverables Locking (SV-17)** — one page, exact trim, DPI, recto orientation, and a reusable BOOK STYLE LOCK for cross-page consistency.
8. **Validation Checklist (SV-18)** — final self-audit covering both line-art and KDP-geometry constraints.

---

## Model-Specific Notes

### gpt-image-2 (OpenAI, primary)
- `quality="high"` for crisp interior line art.
- Put the KDP geometry under CONSTRAINTS; keep the BOOK STYLE LOCK verbatim across every page generation so the title stays consistent.
- For a left-hand (verso) page, swap the gutter to the RIGHT edge in the prompt.
- Do NOT pass `input_fidelity` (disabled).

### Nano Banana (Gemini 3 Pro Image / Gemini 3.1 Flash Image, primary)
- Put the BOOK STYLE LOCK in a **system prompt** (functional on Nano Banana Pro) to enforce one style across the whole book.
- Use Markdown + ALL-CAPS for margins; state `#000000` on `#FFFFFF` and "flat line art, no rendering."
- Generate the book as a series, iterating only the page subject while holding the system prompt fixed.

### DALL-E 3 (legacy)
Add: `"coloring book interior page, black line art, white margins, no shading, no color, print-ready for self-publishing"`. Note: DALL-E 3 does not honor precise margins reliably — verify and crop in a layout tool.

### Midjourney (legacy)
```
[subject] coloring book interior page, clean black line art, white background, generous white margins
--ar 17:22 --v 6 --style raw --s 25
--no color shading gray gradient fill solid black 3d mockup photo text page number
```
Midjourney ignores exact gutters — always import into a KDP template and reposition.

### Stable Diffusion (legacy)
- Generate art with a **lineart ControlNet**, then place it inside a real KDP 8.5x11 template for exact margins/gutter.
Positive: `"coloring book page, clean black line art, closed outlines, white background, [detail level]"`
Negative: `"shading, grayscale, gray, color, gradient, solid black, fill, text, watermark, realistic, texture"`

---

## Troubleshooting

### Problem: Art runs into the binding/gutter
**Add:** `"Leave a WIDE clear white strip 0.625 in on the LEFT (binding) edge. Nothing important near the left edge."`

### Problem: Pages don't look like the same book
**Fix:** Keep the BOOK STYLE LOCK text byte-for-byte identical across generations; on Nano Banana Pro put it in the system prompt.

### Problem: Model bakes in a page number or title
**Add:** `"No text of any kind in the art. Page numbers and titles are added later at layout."`

### Problem: Gray/shaded areas appear (won't print as clean line art)
**Add:** `"Pure black #000000 lines only on pure white. NO gray, NO shading, NO fills."`

### Problem: Generated a two-page spread or a 3D book photo
**Add:** `"ONE single flat page only. Not a spread. Not a photo of a book. Straight-on, no shadow."`

---

## Verification Checklist

- [ ] One image, single flat page (not a spread)
- [ ] 8.5 x 11 in, portrait, 300 DPI (2550 x 3300 px)
- [ ] Pure black outlines, pure white interiors (no color, no gray)
- [ ] No shading, gradients, or solid black fills; all outlines closed
- [ ] All art inside 0.5 in outer/top/bottom margins
- [ ] All art inside 0.625 in LEFT gutter (recto page)
- [ ] Line weight / detail matches the book style lock
- [ ] No baked-in page numbers, titles, watermark, signature
- [ ] No-bleed white page (or intentional bleed if explicitly requested)
- [ ] Imported into a real KDP template and margins re-verified before upload

---

*Updated: 2026-06-23*
