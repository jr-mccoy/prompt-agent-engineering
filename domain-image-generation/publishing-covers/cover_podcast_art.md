---
title: "Podcast Cover Art"
category: image-generation/publishing-covers
description: "3000x3000 podcast cover legible at small size, with verbatim show-title typography and series consistency."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: intermediate
tags:
  - podcast
  - cover
  - square
  - typography
  - series-consistency
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/publishing-covers/cover_album_art.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-image-generation/NANO_BANANA_GUIDE.md
---

# Podcast Cover Art

**Objective:** Produce a podcast cover that is **legible at small size** (Apple Podcasts/Spotify show it as a small tile), renders the show title verbatim, and is built to stay consistent across a series of episode covers.

**Why this model:** The show title is the cover's most important element and must spell correctly while staying readable at ~55–300 px. Use **gpt-image-2** (`quality="high"`) or **Nano Banana Pro** (`gemini-3-pro-image`) for verbatim title text. For series consistency, **Nano Banana Pro** is the strongest pick because system prompts can lock the typographic + color template across every episode cover.

**Directory spec (verify against current Apple Podcasts docs):**
- **3000 × 3000 px square**, RGB, JPEG/PNG; sRGB
- Minimum 1400×1400; 3000×3000 is the production standard
- Displayed as small as ~55 px in app lists — small-size legibility is mandatory

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `size="1024x1024"` (square), `quality="high"`, `n=4`; upscale to 3000×3000 in post
- Nano Banana Pro path: `model="gemini-3-pro-image"`, square aspect, `quality="high"`, **system prompt** to fix the series template

---

## Inputs

- `[SHOW TITLE]` — verbatim show name, exact case
- `[TAGLINE]` — optional verbatim subtitle/episode label
- `[HOST OR NETWORK]` — optional verbatim
- `[TOPIC / GENRE]` — true crime, business, comedy, news, interview, niche hobby
- `[TONE]` — 3 adjectives ("bold, friendly, energetic")
- `[VISUAL DEVICE]` — central icon/motif/portrait that represents the show
- `[PALETTE]` — hex codes (high contrast for small-size punch)
- `[TITLE TYPE STYLE]` — bold, simple face
- `[SERIES?]` — single cover / series template (specify which slots vary per episode)
- `[FORBIDDEN]` — to avoid

---

## Constraints (Must / Must Not)

**Must:**
- Optimize for small-tile legibility first: big bold title, high contrast, one clear motif.
- Render `[SHOW TITLE]` verbatim in an EXACT TEXT block.
- Use a square composition with all text inside a safe margin (≥8% inset).
- For a series, define a fixed template (logo position, color band, title placement) and call out which zone changes per episode.

**Must Not:**
- Use thin/script faces for the title (illegible at 55 px).
- Crowd the tile with small text or busy detail.
- Render real podcast network logos or trademarked marks not owned by the show.
- Invent host names, episode numbers, or ratings.
- Misspell the show title.

---

## Production Prompt (gpt-image-2)

```
ARTWORK:
Square podcast cover for a [TOPIC / GENRE] show, engineered for small-tile
legibility (displayed as small as ~55 px in podcast apps). [TONE].

SMALL-SIZE-FIRST DESIGN:
- One clear central device: [VISUAL DEVICE]. Bold and simple — recognizable as a
  tiny tile.
- Palette: dominant [HEX], contrast [HEX], accent [HEX]. High contrast over subtlety.
- Style commitment: [flat illustration / bold graphic / photographic portrait].
  Commit to one.

TYPOGRAPHY (verbatim, small-tile-legible):
- Show title: "[SHOW TITLE]" — BIG, BOLD, [TITLE TYPE STYLE], [weight ≥ semibold],
  [HEX]. The dominant text element; 100% readable at ~55 px tile size.
- Tagline (if present): "[TAGLINE]" — small, [HEX], near the title. Drop it if it
  hurts small-size legibility.
- Host/network (if provided): "[HOST OR NETWORK]" — small, [HEX].

LAYOUT:
- Square. All text inset at least 8% from every edge.
- Strong figure/ground contrast where the title sits.

SERIES TEMPLATE (if [SERIES?] = template):
- Fix these elements across all episodes: title placement, color band/frame,
  logo/device position.
- Variable per episode (call out the zone): [e.g., "the portrait in the center
  changes per guest; the title bar stays identical"].

CONSTRAINTS:
- EXACT TEXT only, verbatim, no extra characters: show title (plus tagline /
  host if listed). No invented host names, episode numbers, or ratings.
- No thin/script title.
- Forbidden: real network/platform logos not owned by the show, [FORBIDDEN],
  busy small-text clutter, watermarks, lorem ipsum.
- Format: square, target 3000x3000.

If the show title is not readable at ~55 px tile size, or any text is misspelled
or outside the 8% safe area, the output is incorrect.
```

## Production Prompt (Nano Banana Pro — series template via system prompt)

```
SYSTEM PROMPT (locks the series template — reuse for every episode):
You are generating covers for the podcast "[SHOW TITLE]". Every cover MUST use:
- Title "[SHOW TITLE]" in [TITLE TYPE STYLE], [weight], [HEX], placed [position],
  always identical across episodes.
- Color band/frame: [HEX] [describe device], fixed position.
- Square format, high contrast, legible at ~55 px tile size.
Only the [variable zone — e.g., central portrait/topic illustration] changes per
episode. Never alter the title treatment, colors, or layout grid.

USER PROMPT (per episode):
TASK: Episode cover for "[SHOW TITLE]". Variable zone this episode: [VISUAL DEVICE
for this episode]. [TONE].

TYPOGRAPHY (render exactly):
- Title "[SHOW TITLE]" per the locked template.
- Tagline (if present): "[TAGLINE]", small, [HEX].

CONSTRAINTS:
- MUST: verbatim title; template fidelity; small-tile legibility; 8% safe margin.
- MUST NOT: alter the locked template; render network logos not owned by the show;
  invent host/episode/rating text; use [FORBIDDEN].
- Quality: "high".
```

---

## Iteration Plan

1. "Small-tile fail at 55 px — title is unreadable. Increase title size, switch to a heavier face, raise contrast."
2. "Series drift — episode 4's title bar shifted. Restore the locked template position/color from episode 1."
3. "Too busy as a tile — strip secondary detail, keep the one central device."
4. "Tagline is hurting legibility at small size — remove it or shrink the device to make room."

---

## Verification

- [ ] Show title in an EXACT TEXT block, verbatim and correctly cased.
- [ ] Title 100% readable at ~55 px tile size (downscale-test it).
- [ ] Square, target 3000×3000, sRGB.
- [ ] All text inset ≥8% from every edge.
- [ ] Series template fixed; variable zone explicitly identified (if applicable).
- [ ] No network/platform logos not owned by the show; no invented host/episode text.
- [ ] `quality="high"`.
