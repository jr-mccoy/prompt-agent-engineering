---
title: "Ebook Cover — Amazon KDP"
category: image-generation/publishing-covers
description: "KDP-spec ebook cover (2560x1600 portrait) engineered for thumbnail legibility in the Kindle store."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: intermediate
tags:
  - book-cover
  - ebook
  - kdp
  - kindle
  - thumbnail
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/publishing-covers/cover_fiction_book.md
  - domain-image-generation/publishing-covers/cover_nonfiction_book.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# Ebook Cover — Amazon KDP

**Objective:** Produce a Kindle Direct Publishing ebook cover that meets the KDP spec and, above all, **wins at thumbnail size** — the cover must read in a grid of dozens of competing thumbnails where it appears no larger than a postage stamp.

**Why this model:** The title must render verbatim and stay legible when shrunk to ~150 px tall. Use **gpt-image-2** (`quality="high"`) or **Nano Banana Pro** (`gemini-3-pro-image`) for reliable text. Generate, then immediately downscale to test thumbnail survival.

**KDP spec (verify against current KDP docs before upload):**
- Recommended pixel dimensions: **2560 × 1600** (height × width) — i.e., portrait, 1.6:1 height-to-width (KDP's ideal ratio)
- Minimum: 1000 px on the longest side; format JPEG or TIFF; RGB; under 50 MB
- KDP displays this image; thumbnail legibility is what sells

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, generate at `size="1024x1536"` (matches the 2:3-ish portrait), `quality="high"`, `n=4`; upscale/pad to 2560×1600 in post
- Nano Banana Pro path: `model="gemini-3-pro-image"`, portrait aspect, `quality="high"`

> Native model output sizes won't equal 2560×1600 exactly. Generate at the closest supported portrait size, then resize/crop to KDP's 1600×2560 (W×H) in an editor before upload. Lock composition with safe margins so the resize doesn't clip text.

---

## Inputs

- `[TITLE]` — verbatim, exact case
- `[AUTHOR]` — verbatim
- `[SUBTITLE]` — optional, verbatim
- `[GENRE OR CATEGORY]` — drives genre-legible color/imagery
- `[HOOK IMAGE]` — the single bold focal element
- `[PALETTE]` — hex codes (favor high contrast for thumbnail punch)
- `[TITLE TYPE STYLE]` — big, bold, high-contrast face
- `[SERIES NAME]` — optional, verbatim (for series consistency)
- `[FORBIDDEN]` — clichés to avoid

---

## Constraints (Must / Must Not)

**Must:**
- Optimize for the thumbnail first: big title, bold face, high contrast, one clear focal point.
- Render `[TITLE]` and `[AUTHOR]` verbatim in an EXACT TEXT block.
- Use the full bleed (no white KDP border — KDP adds its own thin frame on light covers, so include a defined edge or darker frame if the artwork is pale).
- Keep all text within a safe margin (≥8% inset) so post-resize to 1600×2560 never clips it.
- Test legibility at ~150 px tall.

**Must Not:**
- Use thin/light/script faces for the main title (they vanish at thumbnail size).
- Pack the cover with small text or busy detail that mud-blurs when scaled down.
- Invent series numbers, blurbs, or seals.
- Misspell or re-case the title or author.

---

## Production Prompt (gpt-image-2)

```
ARTWORK:
Ebook cover for a [GENRE OR CATEGORY] title, engineered to win at THUMBNAIL size
in the Kindle store. Portrait orientation, target ratio 1.6:1 (height:width),
full-bleed artwork, no white border.

THUMBNAIL-FIRST DESIGN:
- One bold focal element: [HOOK IMAGE]. Big, simple, high-contrast — readable
  when the whole cover is only ~150 px tall.
- Palette: dominant [HEX], contrast [HEX], accent [HEX]. Prioritize contrast over
  subtlety so the cover pops in a crowded grid.
- Style commitment: [photographic / illustrated / graphic-design-led]. Commit to one.

TYPOGRAPHY (verbatim, thumbnail-legible):
- Title: "[TITLE]" — BIG, BOLD, [TITLE TYPE STYLE], [weight ≥ semibold], [HEX].
  Occupies ~25-35% of cover height. Must be 100% readable at 150 px tall.
- Author: "[AUTHOR]" — smaller, [weight], [HEX], stable position at the
  [top / bottom].
- Subtitle (if present): "[SUBTITLE]" — short, [HEX], near the title; drop it if
  it threatens thumbnail legibility.
- Series (if present): "[SERIES NAME]" — small, consistent corner placement.

LAYOUT:
- All text inset at least 8% from every edge (safe area for post-resize to 1600x2560).
- Strong figure/ground contrast everywhere type sits.
- If artwork is pale, add a defined darker edge so the cover doesn't bleed into the
  white store background.

CONSTRAINTS:
- EXACT TEXT only, verbatim, no extra characters: title, author (plus subtitle /
  series if listed). No invented blurbs, seals, or series numbers.
- No thin/script main title.
- Forbidden: [FORBIDDEN], busy small-text clutter, watermarks, lorem ipsum.
- Format: portrait, full-bleed, target 1.6:1 (height:width).

If the title is not readable at 150 px tall, or any text is misspelled or sits
outside the 8% safe area, the output is incorrect.
```

## Production Prompt (Nano Banana Pro)

```
TASK: Design a Kindle ebook cover for a [GENRE OR CATEGORY] title that wins at
thumbnail size. Portrait, ratio 1.6:1 (height:width), full bleed, no white border.

DESIGN:
One bold focal element: [HOOK IMAGE], high contrast. Palette [HEX], [HEX], [HEX] —
contrast over subtlety. Commit to one rendering style.

TYPOGRAPHY (render exactly, thumbnail-legible):
- Title: "[TITLE]" — big, bold [TITLE TYPE STYLE], [weight], [HEX], readable at
  150 px tall.
- Author: "[AUTHOR]" — smaller, [HEX].
- Subtitle / series (if provided): "[SUBTITLE]" / "[SERIES NAME]", small, [HEX].

CONSTRAINTS:
- MUST: verbatim title + author; all text inset ≥8% from edges; high type/background
  contrast; defined edge if artwork is pale.
- MUST NOT: thin/script main title; invent blurbs/seals/series numbers; misspell or
  re-case; use [FORBIDDEN].
- Quality: "high".
```

---

## Iteration Plan

1. "Thumbnail fail at 150 px — the title disappears. Increase title size to ~30% of height and switch to a heavier weight."
2. "Cover blends into the white store background — add a darker defined edge or frame."
3. "Too busy at small size — strip secondary detail; keep one bold focal element."
4. "Push contrast: the [HEX] on [HEX] combination is too low-contrast to pop in a grid."

---

## Verification

- [ ] Title and author in an EXACT TEXT block, verbatim and correctly cased.
- [ ] Title 100% readable at ~150 px tall (squint-test the downscaled image).
- [ ] Portrait, target ratio 1.6:1 (height:width); resizes cleanly to 1600×2560 (W×H).
- [ ] All text inset ≥8% from every edge.
- [ ] Defined edge so a pale cover doesn't bleed into white.
- [ ] No invented blurbs, seals, or series numbers.
- [ ] `quality="high"`.
