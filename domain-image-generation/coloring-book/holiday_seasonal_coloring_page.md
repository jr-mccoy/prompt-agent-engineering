---
title: "Holiday / Seasonal Coloring Page (Template-Driven)"
category: image-generation/coloring-book
description: "Template-driven generator for holiday and seasonal coloring pages (Christmas, Halloween, Easter, Valentine's, Thanksgiving, spring, summer, fall, winter) as pure black-on-white print-ready line art — choose holiday, motifs, and difficulty."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-11
  - SV-12
  - SV-13
  - SV-14
  - SV-16
  - SV-17
  - SV-18
difficulty: intermediate
tags:
  - coloring-book
  - image-generation
  - holiday
  - seasonal
  - christmas
  - halloween
  - line-art
  - print-ready
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - themed_coloring_set.md
  - kids_coloring_page_simple.md
  - educational_coloring_page.md
  - coloring_book_kdp_interior.md
---

# Holiday / Seasonal Coloring Page (Template-Driven)

**Purpose:** Generate a holiday or seasonal coloring page from a simple template — pick the holiday/season, the motifs, the audience/difficulty, and (optionally) a colorable greeting. Pure black line art on white, print-ready. Works for single pages or a seasonal set (pair with [themed_coloring_set.md](themed_coloring_set.md)).

**Format / Dimensions:** Single flat page, 8.5" x 11" portrait (letter) at 300 DPI. Pure line art, no color, no grayscale. Any greeting text renders as **hollow/outline (colorable) letters**.

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core print techniques
- [themed_coloring_set.md](themed_coloring_set.md) — generate a whole seasonal set in one style
- [kids_coloring_page_simple.md](kids_coloring_page_simple.md) / [educational_coloring_page.md](educational_coloring_page.md) — pick a difficulty tier / add learning
- [coloring_book_kdp_interior.md](coloring_book_kdp_interior.md) — publish a seasonal book

---

## Holiday / Season Template Table

| Holiday / Season | Common motifs | Tone |
|---|---|---|
| Christmas | tree, ornaments, stockings, snowman, Santa, reindeer, gifts | festive, cozy |
| Halloween | pumpkins, bats, friendly ghosts, witch hat, candy, spiderweb | playful-spooky (keep kid-friendly) |
| Easter | eggs, bunny, basket, flowers, chicks | spring, cheerful |
| Valentine's Day | hearts, cupid, roses, "love" banner | warm, decorative |
| Thanksgiving | turkey, cornucopia, autumn leaves, pumpkin pie | harvest, grateful |
| Spring | flowers, butterflies, rain, growing seeds | fresh, light |
| Summer | sun, beach, ice cream, watermelon, sandcastle | bright, fun |
| Fall / Autumn | leaves, acorns, pumpkins, sweaters, scarecrow | cozy, warm |
| Winter | snowflakes, mittens, hot cocoa, snowman, sled | crisp, cozy |

---

## Image Generation Prompt (Production-Ready)

```
TASK: Generate ONE FLAT PRINT ARTWORK IMAGE that is a HOLIDAY / SEASONAL COLORING PAGE.

IMPORTANT REAL-WORLD CONTEXT:
This is a seasonal coloring page.
It will be PRINTED on letter-size paper and colored in (home, classroom, or party activity).
The appeal is recognizable holiday/seasonal motifs ready to color.

This is NOT a finished illustration.
This is NOT a grayscale or shaded drawing.
This is NOT a sketch, a mockup, or a photo of a book.
This image IS the literal black ink-on-paper line art sent directly to a printer.

HOLIDAY / SEASON PARAMETERS (fill in):
- Holiday / season: [e.g. Christmas]
- Main motif(s): [e.g. a decorated tree with gifts underneath]
- Supporting motifs: [e.g. ornaments, a star, stockings]
- Audience / difficulty: [e.g. ages 4-8, simple bold]  OR  [e.g. adult, medium-intricate]
- Optional greeting (hollow outline letters): [e.g. "Merry Christmas"]
- Optional border: [e.g. none]  OR  [thin holly-leaf colorable border]

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
- ANY text is HOLLOW / OUTLINE letterforms (colorable), NOT solid black.
- Single flat page, viewed straight-on. NOT a 3D render, NOT a book mockup.

If any gray tone, shading, color, or solid black fill (including solid black text) appears, the output is INCORRECT.

================================================
LINE ART SPECIFICATIONS
================================================

- Line weight matches the audience: 3-5 pt bold for young kids; 1-1.5 pt for intricate adult pages.
- Crisp, smooth, CLOSED outlines (no gaps) so colors won't bleed.
- Detail scales with difficulty: simple = few large areas; intricate = dense outlined patterns.
- Decorative fills (snow, fur, ornaments) allowed ONLY as open outlined shapes, never solid black.
- Holiday motifs must be instantly recognizable.

================================================
CONTENT & TONE
================================================

- Cheerful and age-appropriate. For Halloween keep it friendly/playful, not frightening, for kids.
- Greeting (if included) spelled EXACTLY as provided, in hollow outline letters.
- No brand logos or trademarked character likenesses (use generic seasonal motifs).

================================================
COMPOSITION & LAYOUT
================================================

- Main motif composed as the focal point; supporting motifs arranged around it without crowding.
- White margin: 0.5 inch clean white border on all four sides.
- Optional thin seasonal border INSIDE the margin (clean colorable line art).
- No watermark, no signature, no page number in the art.

================================================
ALLOWED vs FORBIDDEN
================================================

ALLOWED:
- Recognizable holiday/seasonal motifs as closed line art
- A hollow/outline colorable greeting
- An optional thin seasonal colorable border
- Difficulty appropriate to the audience

FORBIDDEN:
- Any color, gray, shading, gradient, or solid black fill
- SOLID black text (greetings must be colorable)
- Brand logos or trademarked characters
- Scary/violent content on kid-targeted pages
- Open / broken outlines
- Background scenery beyond the chosen motifs, shadows, or 3D depth
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
- [ ] Recognizable holiday/seasonal motifs for [holiday]
- [ ] Greeting (if any) spelled exactly, in hollow colorable letters
- [ ] Pure black lines only — no gray, no color
- [ ] Every interior space is pure white (colorable)
- [ ] NO shading, gradients, or solid black fills; outlines closed
- [ ] Line weight/detail match the audience/difficulty
- [ ] Age-appropriate tone; no trademarked characters/logos
- [ ] 0.5 inch clean white margin; no watermark/signature/page number
- [ ] Flat page, not a mockup or 3D render

If text is solid black or misspelled, or any shading/fill/color appears, the output is INCORRECT.

================================================
GENERATE NOW
================================================

Produce a single holiday/seasonal coloring page following all rules above.
```

---

## Simplified Prompt (If Full Prompt Misbehaves)

```
Create ONE [holiday/season] coloring page as black line art on a pure white background.

CONTENT:
- Holiday/season: [e.g. Christmas]; main motif: [e.g. decorated tree with gifts]
- Supporting motifs: [e.g. ornaments, star, stockings]
- Audience: [e.g. kids 4-8, simple bold]  or  [adult, intricate]
- Optional greeting (hollow outline letters, spelled exactly): "[e.g. Merry Christmas]"

RULES:
- Black outlines only — NO color, NO gray, NO shading, NO fills
- Any text is hollow/outline (colorable), NOT solid black
- Every enclosed area stays white; all outlines closed; recognizable motifs
- No trademarked characters or logos; keep kid pages friendly
- 8.5 x 11 inches, portrait, 300 DPI, 0.5 inch white margin
- Flat print line art, not a mockup; no watermark

If text is solid black/misspelled, or any shading/fill/color appears, it is WRONG.
```

---

## Why This Prompt Works

1. **Terminology Steering (SV-11)** — "flat print artwork" / "line art" steers to print, not UI/render.
2. **Grid Forcing + Enumerated Slots (SV-12)** — the holiday template table and enumerated main/supporting motifs act as a content slot list, preventing a vague holiday mash-up.
3. **Constraint Redundancy (SV-13)** — no-fill, hollow-text, and no-trademark rules repeat across critical rules, content/tone, allowed/forbidden, and checklist.
4. **Negative Space Control (SV-14)** — pure white background, no extra scenery, explicit margin.
5. **Allowed vs Forbidden (SV-15)** — permits motifs/greeting/border while forbidding solid text, trademarked characters, and scary content.
6. **Physical Context Anchoring (SV-16)** — "home/classroom/party activity, seasonal" sets recognizability and difficulty.
7. **Deliverables Locking (SV-17)** — one image, exact size/DPI/orientation; template-driven parameters make it reusable per holiday.
8. **Validation Checklist (SV-18)** — final self-audit including spelling and IP/age-appropriateness checks.

---

## Model-Specific Notes

### gpt-image-2 (OpenAI, primary)
- `quality="high"` keeps motifs and any greeting text crisp.
- gpt-image-2 renders seasonal motifs reliably; verify greeting spelling. Put line-art constraints under CONSTRAINTS.
- Do NOT pass `input_fidelity` (disabled).

### Nano Banana (Gemini 3 Pro Image / Gemini 3.1 Flash Image, primary)
- Strong in-image text for greetings (Nano Banana Pro near-perfect). Use Markdown + ALL-CAPS; specify `#000000` on `#FFFFFF`, "hollow outline letters, NOT filled."
- For a seasonal SET, put the style in a system prompt and iterate the holiday/motif (see [themed_coloring_set.md](themed_coloring_set.md)).

### DALL-E 3 (legacy)
Add: `"[holiday] coloring page, black line art, recognizable [holiday] motifs, no shading, no color, white background"`. Verify any greeting spelling.

### Midjourney (legacy)
```
[holiday] coloring page, [main motif], clean black line art, [line weight], white background
--ar 17:22 --v 6 --style raw --s 25
--no color shading gray gradient fill solid black 3d mockup photo trademark logo
```
`--no color shading` keeps it line art; keep greetings short (Midjourney text is weak).

### Stable Diffusion (legacy)
- A **lineart ControlNet** with a seasonal reference gives clean closed motifs; add greeting text in a layout tool.
Positive: `"[holiday] coloring page, clean black line art, closed outlines, recognizable [holiday] motifs, white background, [detail] detail"`
Negative: `"shading, grayscale, gray, color, gradient, solid black, fill, realistic, texture, logo, watermark, gibberish text"`

---

## Troubleshooting

### Problem: Motifs not recognizable as the holiday
**Add:** `"Use clear, classic [holiday] symbols: [list your motifs]. Make each instantly recognizable."`

### Problem: Greeting is solid black or misspelled
**Add:** `"The greeting reads EXACTLY '[text]' in HOLLOW outline letters with white interiors to color."` Add text in a layout tool on weaker models.

### Problem: Trademarked character appears (e.g. a specific franchise Santa/character)
**Add:** `"Use only generic seasonal motifs. NO trademarked characters, NO brand logos."`

### Problem: Halloween page too scary for kids
**Add:** `"Keep it friendly and cute (smiling pumpkin, friendly ghost). Nothing frightening."`

### Problem: Shading/fills appear
**Add:** `"Every area stays pure white. NO gray, NO shading, NO solid black fill."`

---

## Verification Checklist

- [ ] Exactly one image generated
- [ ] Recognizable holiday/seasonal motifs
- [ ] Greeting (if any) spelled exactly, hollow/colorable
- [ ] Pure black outlines, pure white interiors (no color, no gray)
- [ ] No shading, gradients, or solid black fills; outlines closed
- [ ] Line weight/detail match the audience/difficulty
- [ ] Age-appropriate tone; no trademarked characters or logos
- [ ] 0.5 inch clean white margin; no watermark/signature/page number
- [ ] 8.5 x 11 in, 300 DPI, portrait
- [ ] Flat line art, not a mockup or 3D render

---

*Updated: 2026-06-23*
