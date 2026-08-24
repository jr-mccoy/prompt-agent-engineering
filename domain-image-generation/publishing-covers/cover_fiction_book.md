---
title: "Book Cover — Fiction"
category: image-generation/publishing-covers
description: "Genre-conventional fiction book cover with verbatim title + author typography, optional spine/back layout."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: advanced
tags:
  - book-cover
  - fiction
  - publishing
  - typography
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/publishing-covers/cover_ebook_kdp.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-image-generation/NANO_BANANA_GUIDE.md
---

# Book Cover — Fiction

**Objective:** Produce a genre-legible fiction cover where the title and author name render verbatim with controlled typography, the imagery signals genre at a glance, and the composition holds up both full-size on a shelf and at thumbnail scale online.

**Why this model:** The cover lives or dies on text rendering — the title and author must be spelled exactly and set in a deliberate face. Use **gpt-image-2** (`quality="high"`, 95%+ text accuracy, strong section-based briefing) or **Nano Banana Pro** (`gemini-3-pro-image`, near-perfect text + exact font specification) for any cover where the title is part of the artwork. Avoid speed-first models for the production pass.

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `size="1024x1536"` (portrait, 2:3-ish trade paperback feel), `quality="high"`, `n=4` for a cover concept pool
- Nano Banana Pro path: `model="gemini-3-pro-image"`, portrait aspect, `quality="high"`, system prompt to lock typographic style across a series

---

## Inputs

- `[TITLE]` — verbatim, exact capitalization
- `[AUTHOR]` — verbatim author name as it should appear
- `[SUBTITLE OR TAGLINE]` — optional, verbatim
- `[GENRE]` — literary, thriller, romance, fantasy, sci-fi, horror, mystery, historical, YA
- `[MOOD]` — 3 adjectives ("brooding, atmospheric, cold")
- `[KEY IMAGE]` — the central symbol/scene (a lone figure on a cliff, a single object, an abstract motif)
- `[PALETTE]` — hex codes for 2–3 dominant colors
- `[TITLE TYPE STYLE]` — serif display / condensed sans / hand-lettered / gothic / etc.
- `[COMP TITLES]` — optional: covers whose category feel you want to evoke (mood, not copying)
- `[TRIM]` — final trim size for print (e.g., 5.5×8.5 in) or ebook-only
- `[FORBIDDEN]` — clichés to avoid

---

## Constraints (Must / Must Not)

**Must:**
- Render `[TITLE]` and `[AUTHOR]` verbatim in an EXACT TEXT block with face, weight, hex, and placement.
- Signal `[GENRE]` through color, imagery, and type — a thriller and a romance should never be confusable.
- Reserve a quiet zone for the title so type sits on clean ground, not busy texture.
- Keep the title legible at 200×300 px thumbnail (test by squinting).
- Leave a small margin of safe area inside the trim so type isn't cut at the bleed.

**Must Not:**
- Misspell, abbreviate, or re-case the title or author.
- Render real authors' brand marks, publisher logos, or trademarked fonts by name-as-image.
- Use lorem ipsum, fake review blurbs, or invented award seals.
- Add barcodes on the front cover.
- Use stock-cover clichés in `[FORBIDDEN]` (back-to-camera couple for non-romance, generic "person walking away").

---

## Production Prompt (gpt-image-2)

```
SCENE / ARTWORK:
Front cover artwork for a [GENRE] novel. The central image: [KEY IMAGE].
Render it so the genre reads instantly — [MOOD]. Composition is portrait,
built for a [TRIM] book, with a quiet zone reserved for the title.

ART DIRECTION:
- Palette: dominant [HEX], secondary [HEX], accent [HEX]. Genre-true mood.
- Style commitment: [photographic / painterly / illustrated / graphic-design-led]
  cover art. Choose ONE and commit; do not blend rendering styles.
- Atmosphere over detail — the image should suggest, not over-explain.
- Comp feel (mood only, no copying): [COMP TITLES].

TYPOGRAPHY (verbatim — this is part of the artwork):
- Title: "[TITLE]" — set in a [TITLE TYPE STYLE] face, [weight], color [HEX],
  placed in the [upper third / lower third], occupying ~18-28% of cover height.
  100% readable at full size AND at 200x300 px thumbnail.
- Author: "[AUTHOR]" — [smaller, complementary face], [weight], color [HEX],
  placed [opposite the title / under the title]. Clearly subordinate to the title.
- Tagline (if present): "[SUBTITLE OR TAGLINE]" — small, [hex], near the title.

LAYOUT:
- Reserve a visually quiet zone behind the title (no busy texture there).
- Keep all type at least 0.25 in (proportionally) inside the trim edge.
- Strong figure/ground contrast between type and the area it sits on.

CONSTRAINTS:
- EXACT TEXT, no extra characters, no invented copy: title and author only
  (plus tagline if listed). No review blurbs, no award seals, no publisher logo.
- No barcode on the front.
- Forbidden: [FORBIDDEN], stock-cover clichés, watermarks, lorem ipsum.
- Format: portrait, [size], full-bleed artwork.

If the title or author is misspelled, re-cased, or illegible at thumbnail size,
the output is incorrect.
```

## Production Prompt (Nano Banana Pro)

```
TASK: Design the front cover for a [GENRE] novel. Portrait orientation, built for
a [TRIM] book. Genre must read at a glance; mood is [MOOD].

ARTWORK:
The central image is [KEY IMAGE]. Treat it as [photographic / painterly /
illustrated] cover art — commit to one rendering style. Palette: [HEX], [HEX],
[HEX]. Atmosphere over literal detail.

TYPOGRAPHY (render exactly, this is the hero of the cover):
- Title: "[TITLE]" in a [TITLE TYPE STYLE] typeface, [weight], [HEX]. Place it in
  the [upper / lower] third over a quiet area. Must be legible at thumbnail size.
- Author: "[AUTHOR]" in a smaller complementary face, [weight], [HEX], subordinate
  to the title.
- Tagline (if present): "[SUBTITLE OR TAGLINE]", small, [HEX].

CONSTRAINTS:
- MUST: verbatim title + author; quiet zone behind the title; type inside a safe
  margin from the trim edge; strong type/background contrast.
- MUST NOT: misspell or re-case any text; add review blurbs, award seals, publisher
  logos, or a front-cover barcode; use [FORBIDDEN].
- Quality: "high".
```

---

## Iteration Plan

1. "The title competes with the artwork — darken/lighten the quiet zone behind the title so the type has clean ground."
2. "Genre isn't reading as [GENRE] — push the palette toward [direction] and adjust the central image to [more specific motif]."
3. "Author name is fighting the title — drop it to [smaller %] and move it to [opposite corner]."
4. "Test thumbnail: at 200×300 px the title blurs. Increase weight / contrast / size."

---

## Verification

- [ ] Title and author in an EXACT TEXT block, verbatim and correctly cased.
- [ ] Genre reads instantly from color + imagery + type.
- [ ] Quiet zone reserved behind the title.
- [ ] Title legible at 200×300 px thumbnail.
- [ ] Type inside a safe margin from the trim edge.
- [ ] No invented blurbs, award seals, publisher logos, or front-cover barcode.
- [ ] `quality="high"`.
