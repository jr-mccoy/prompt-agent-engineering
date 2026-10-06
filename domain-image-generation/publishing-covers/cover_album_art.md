---
title: "Album Cover Art"
category: image-generation/publishing-covers
description: "Mood-driven 3000x3000 square album cover with optional verbatim artist/title typography."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: intermediate
tags:
  - album-art
  - music
  - cover
  - square
  - typography
  - gpt-image-2
  - nano-banana-pro
updated: "2026-10-06"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/publishing-covers/cover_podcast_art.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-image-generation/NANO_BANANA_GUIDE.md
---

# Album Cover Art

**Objective:** Produce a square album cover that is **mood-first** — the image carries the feel of the music — while any artist name and album title render verbatim and survive the brutal downscale to a streaming-grid thumbnail.

**Why this model:** Album art is aesthetic-led, but the moment text is involved (most covers carry artist + title), accuracy matters. Two paths: **gpt-image-2** / **Nano Banana Pro** when the cover needs verbatim typography; **Midjourney or Nano Banana 2** when you want a purely image-driven, text-free cover and will set type yourself afterward. The prompts below default to the text-rendering models.

**Distributor spec (verify against current Spotify/Apple/DistroKid docs):**
- **3000 × 3000 px square**, RGB, JPEG/PNG; sRGB color
- Minimum often 1400×1400, but 3000×3000 is the safe production standard

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `size="1024x1024"` (square), `quality="high"`, `n=4`; upscale to 3000×3000 in post
- Nano Banana Pro path: `model="gemini-3-pro-image"`, square aspect, `quality="high"`
- Text-free aesthetic path: Nano Banana 2 (`gemini-3.1-flash-image`) `n=6` screening, then upscale; add type in an editor

---

## Inputs

- `[ARTIST]` — verbatim artist/band name (if it appears on the cover)
- `[ALBUM TITLE]` — verbatim album/single title (if it appears)
- `[GENRE]` — the musical genre/subgenre
- `[MOOD]` — 3–4 adjectives that describe the sound ("hazy, nocturnal, romantic")
- `[VISUAL CONCEPT]` — the central image/feeling
- `[PALETTE]` — hex codes
- `[TEXT ON COVER?]` — yes (artist + title) / artist only / text-free
- `[TYPE STYLE]` — if text: face/treatment (e.g., "tiny lowercase sans in a corner")
- `[REFERENCE ERA]` — optional aesthetic era/movement (mood, not copying)
- `[FORBIDDEN]` — to avoid

---

## Constraints (Must / Must Not)

**Must:**
- Lead with mood — the cover should feel like the music before you read a word.
- If text is included, render `[ARTIST]` / `[ALBUM TITLE]` verbatim in an EXACT TEXT block.
- Keep the focal element readable at streaming-thumbnail size (~120–300 px square).
- Commit to a single rendering style.

**Must Not:**
- Render real artists' existing logos, label marks, or another band's trade dress.
- Imitate a specific existing album cover closely enough to confuse (evoke era/mood only).
- Add a "Parental Advisory" sticker unless explicitly requested.
- Misspell artist or album text.

---

## Production Prompt (gpt-image-2 — with text)

```
ARTWORK:
Square album cover for a [GENRE] release. Mood-first: the image must feel [MOOD]
before any text is read. Central concept: [VISUAL CONCEPT].

ART DIRECTION:
- Palette: [HEX], [HEX], [HEX]. Let the palette carry the mood.
- Style commitment: [photographic / painterly / collage / graphic / surreal].
  Commit to ONE.
- Aesthetic era (mood only, no copying of any specific cover): [REFERENCE ERA].
- One strong focal element that survives downscale to a streaming thumbnail.

TYPOGRAPHY (verbatim — [TEXT ON COVER?]):
- Artist: "[ARTIST]" — [TYPE STYLE], [weight], color [HEX], placed [corner /
  center / lower-third]. Subordinate to the image unless the concept is type-led.
- Album title: "[ALBUM TITLE]" — [TYPE STYLE], [weight], [HEX], placed near the
  artist or as the concept dictates.
(If text-free: omit all type entirely and leave a clean composition.)

LAYOUT:
- Keep type within a safe square margin; readable at thumbnail size.
- Strong contrast where any type sits.

CONSTRAINTS:
- EXACT TEXT only, verbatim, no extra characters: artist and/or album title as
  listed. No invented track text, no label logos, no parental-advisory sticker
  (unless requested).
- Forbidden: real existing band/label logos, close imitation of a specific real
  album cover, [FORBIDDEN], watermarks, lorem ipsum.
- Format: square, target 3000x3000.

If artist or album text is misspelled, or the focal element is illegible at
thumbnail size, the output is incorrect.
```

## Production Prompt (Nano Banana Pro — with text)

```
TASK: Design a square album cover for a [GENRE] release. Mood-first — it must feel
[MOOD]. Central concept: [VISUAL CONCEPT]. Palette [HEX], [HEX], [HEX].

ARTWORK:
Commit to one rendering style ([photographic / painterly / collage / graphic]).
Evoke the era/mood of [REFERENCE ERA] without copying any specific real cover.
One strong focal element readable at streaming-thumbnail size.

TYPOGRAPHY (render exactly — [TEXT ON COVER?]):
- Artist: "[ARTIST]" — [TYPE STYLE], [weight], [HEX].
- Album title: "[ALBUM TITLE]" — [TYPE STYLE], [weight], [HEX].
(If text-free: omit all type.)

CONSTRAINTS:
- MUST: verbatim artist/title; type within a safe square margin; thumbnail-readable
  focal element; one rendering style.
- MUST NOT: render real band/label logos; closely imitate a specific real cover;
  add a parental-advisory sticker (unless requested); misspell text; use [FORBIDDEN].
- Quality: "high".
```

---

## Iteration Plan

1. "Mood is off — the music is [MOOD] but the cover reads [other]. Shift palette toward [direction] and the concept toward [adjustment]."
2. "Thumbnail fail — at 150 px the focal element is unreadable. Simplify to one bold subject."
3. "Type fights the image — shrink the artist/title and move to a [corner] so the image leads."
4. "Push the [REFERENCE ERA] aesthetic harder via [texture / grain / color treatment]."

---

## False-Positive Prevention

❌ **DON'T:**
- Clear the text-free path because no title was rendered — check signage, graffiti, book spines, and clothing in the scene for pseudo-letters the model drew in.
- Let an intentionally stylized name be "fixed": an all-lowercase artist name, a deliberate misspelling, or a symbol standing in for a letter must render exactly as supplied, so compare against the release metadata, not standard spelling.
- Rely on the Distributor spec block in this file — minimum sizes, file limits, color profile, and content bans (URLs, social handles, pricing, blurriness, text that doesn't match the release metadata) vary by distributor and change [VERIFY: current distributor artwork requirements].
- Accept a photographic cover whose face resembles a recognizable real person — likeness drift is common when `[REFERENCE ERA]` names a scene tied to particular artists.

✅ **DO:**
- Reverse-image-search the final cover and compare it with the best-known covers of `[REFERENCE ERA]`; if subject, layout, and palette all line up with one, change at least the focal element.
- Downscale the 3000×3000 file to 150×150 px and view it in a grid of other covers in the genre; the focal element must be identifiable without zooming.
- Check artist and title on the cover against the exact strings entered in the distribution form, character by character.

---

## Verification

- [ ] Cover feels like the music (mood-first) before text is read.
- [ ] If text: artist/title in an EXACT TEXT block, verbatim and correctly cased.
- [ ] Square, target 3000×3000, sRGB.
- [ ] Focal element readable at ~150 px square thumbnail.
- [ ] No real band/label logos; no close imitation of a specific real cover.
- [ ] No parental-advisory sticker unless requested.
- [ ] `quality="high"`.
