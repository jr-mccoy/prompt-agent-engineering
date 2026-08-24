---
title: "Children's Book Illustration — Full Picture-Book Spread"
category: image-generation/childrens-illustration
description: "Generate a full picture-book spread (two-page or single-page) with a reserved text-safe area, age-appropriate style, and gutter-safe composition."
techniques:
  - ST-01
  - ST-02
  - SV-12
  - SV-13
  - SV-15
difficulty: intermediate
tags:
  - childrens-illustration
  - picture-book
  - spread
  - text-safe-area
  - gpt-image-2
  - nano-banana
  - storybook
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/childrens-illustration/childrens_character_design_sheet.md
  - domain-image-generation/childrens-illustration/childrens_consistent_style_series.md
  - domain-image-generation/CHARACTER_BIBLE_PIPELINE.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/gpt-image-2/gptimage2_character_consistency_anchor.md
  - domain-image-generation/nano-banana/nanobana_multi_reference_character_scene.md
---

# Children's Book Illustration — Full Picture-Book Spread

**Objective:** Produce one finished picture-book spread — a single illustration sized for a two-page layout (or a single page) — that leaves a deliberate **text-safe area** for the manuscript copy, keeps the focal action out of the **gutter**, and renders in a consistent, age-appropriate illustration style. Use case: trade picture books (ages 2–8), early readers, read-aloud titles.

> **Audience boundary:** This prompt is for illustrating material *for* children (you are the author/illustrator producing a book). It is not a teaching tool for kids and produces no instructional content. For writing the manuscript itself, see the repo's `domain-childrens-writing/`.

**Why model choice matters:** A spread is one large composition with reserved negative space and a locked style. Use **gpt-image-2** when the spread carries in-image title/word art or you want the artifact-specification workflow. Use **Nano Banana 2/Pro** when you are iterating many spread compositions cheaply or need to carry a character reference pack across spreads.

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `/v1/images/generations` (or `/v1/images/edits` to carry a character reference), `quality="high"`, `size="1536x1024"` (landscape spread), `n=1`
- Nano Banana path: `model="gemini-3-pro-image"` (Pro, for text-safe precision) or `"gemini-3.1-flash-image"` (NB2, for fast iteration); pass character refs in CHARACTER slots; `quality="high"`, `n=1`

---

## Inputs

- `[BOOK TITLE]` / `[SPREAD NUMBER]` — which spread in the book (e.g., "Spread 4 of 16")
- `[MANUSCRIPT TEXT]` — the actual words that will sit on this spread (used only to size and place the text-safe area; do NOT render the text unless explicitly asked)
- `[AGE BAND]` — target reader age (e.g., 2–4 board, 4–8 picture book)
- `[CHARACTER NAME(S)]` + `[CHARACTER BIBLE]` — durable visual traits (see CHARACTER_BIBLE_PIPELINE.md)
- `[REFERENCE PACK]` — optional character anchor/reference images for consistency across spreads
- `[SCENE]` / `[ACTION]` / `[EMOTION]` — what happens on this spread
- `[STYLE]` — canonical illustration style (e.g., "soft watercolor with visible paper grain, warm palette, rounded forms")
- `[LAYOUT]` — single page (portrait) or full two-page spread (landscape); where the text block sits
- `[TEXT-SAFE ZONE]` — which region of the frame must stay low-detail for the copy (e.g., "lower third", "right page")
- `[TRIM/BLEED]` — optional final trim size and bleed allowance

---

## Constraints (Must / Must Not)

**Must:**
- Reserve a **text-safe area** as calm, low-contrast negative space sized for `[MANUSCRIPT TEXT]` (sky, water, a wash, a flat field of color).
- Keep faces, hands, and the focal action **out of the center gutter** (the vertical middle for two-page spreads) and away from the trim edges.
- Use **age-appropriate** content: friendly proportions, no scary/violent imagery for young bands, no small parts read as choking-hazard realism for board-book art.
- Restate the full character bible and the canonical `[STYLE]` (style is part of book identity).
- State the spread's read-aloud emotional beat (page turns should feel propulsive).

**Must Not:**
- Render the manuscript text inside the art unless explicitly requested (the publisher typesets type separately).
- Fill the entire frame edge-to-edge with busy detail (leaves no room for type).
- Place the hero's face or a key prop in the gutter (it disappears into the binding).
- Drift the character or the style from prior spreads (see childrens_consistent_style_series.md).
- Add adult-oriented, frightening, or unsafe imagery for the stated `[AGE BAND]`.

---

## Production Prompt — gpt-image-2 path

```
SCENE:
[BOOK TITLE], Spread [SPREAD NUMBER]. A [LAYOUT — full two-page landscape spread / single portrait page] picture-book illustration for readers aged [AGE BAND].
Setting: [SCENE — environment, time of day, season, weather].

SUBJECT:
[CHARACTER NAME(S)] [ACTION]. Emotional beat for this page: [EMOTION].

CHARACTER BIBLE (must persist across the whole book):
- Hair: [color, length, style]
- Eyes: [color, shape]
- Skin: [tone]
- Build: [proportions — note: friendly, slightly stylized child proportions]
- Default outfit: [garment by garment, colors]
- Distinctive marks: [the drift detector]

KEY DETAILS:
- Style: [STYLE] — this is the canonical style for the entire book.
- Composition: place [CHARACTER NAME(S)] and the focal action in the [left page / right page / lower foreground]. Keep all faces, hands, and key props clear of the center gutter and the outer trim edges.
- TEXT-SAFE AREA: reserve the [TEXT-SAFE ZONE — e.g., upper-left quadrant / lower third] as calm, low-detail negative space (a soft wash, open sky, or flat color field) sized to hold roughly [N words / N lines] of body copy. Do NOT draw text there — leave it visually quiet.
- Palette: [warm / cool / specific colors], age-appropriate, gentle contrast.
- Lighting: soft, even, inviting. No harsh shadows on faces.

USE CASE:
Finished interior illustration for a trade picture book. Type will be set separately by the publisher in the reserved text-safe area.

CONSTRAINTS:
- Age-appropriate for [AGE BAND]: friendly, non-frightening, no violence, no small-realistic-hazard imagery for board art.
- Do NOT render any manuscript text in the illustration.
- Keep the focal subject and faces out of the gutter and away from trim edges.
- Leave the text-safe area calm and low-contrast.
- Maintain the canonical [STYLE] exactly.
- Format: [size], landscape spread orientation, quality="high". Allow [TRIM/BLEED] margin if specified.

If the text-safe area is filled with busy detail, if a face or key prop sits in the gutter, or if the style differs from the book's canonical look, the output is incorrect.
```

---

## Production Prompt — Nano Banana path (carry character refs)

```
TASK: Create one [LAYOUT] picture-book illustration ([BOOK TITLE], Spread [SPREAD NUMBER]) for readers aged [AGE BAND].

REFERENCES (CHARACTER slots):
- Char 1–4: reference pack for [CHARACTER NAME].
  TAKE: face, hair, skin, eye color, proportions, outfit.
  IGNORE: backgrounds and poses from the reference images.
[Nano Banana Pro: add Style 1 = a prior finished spread, TAKE color grade + brush/render style, IGNORE composition.]

CHARACTER BIBLE — [CHARACTER NAME] (restated):
[full 5–10 trait bible]

SCENE: [CHARACTER NAME(S)] [ACTION] in [SCENE]. Emotional beat: [EMOTION].

COMPOSITION:
- Place the focal action in the [page region]; keep faces, hands, and key props clear of the center gutter and outer trim edges.
- TEXT-SAFE AREA: keep the [TEXT-SAFE ZONE] as calm, low-detail negative space (open sky / soft wash / flat color) for about [N words] of body copy. Leave it visually quiet — do not render any text.

STYLE: [STYLE] — canonical for the whole book; match the style reference.
PALETTE: [palette], age-appropriate, gentle contrast.
LIGHTING: soft, even, inviting.

PRESERVE:
- [CHARACTER NAME]'s exact face, hair color, eye color, proportions, distinctive marks from the references.
- Canonical [STYLE].

CONSTRAINTS:
- MUST: age-appropriate for [AGE BAND]; calm text-safe area; subject clear of gutter/trim.
- MUST NOT: render manuscript text; fill the frame edge-to-edge; drift character or style.
- Quality: "high".

If the text-safe area is cluttered, a face sits in the gutter, or the style/character drifts, the output is incorrect.
```

---

## Iteration Plan

1. "The text-safe area in the [zone] has too much detail — flatten it into calm negative space so type can sit there."
2. "[CHARACTER NAME]'s face is drifting into the center gutter — shift the figure toward the [left/right] page."
3. "The contrast in the text-safe zone is too high — lower it so dark body text will remain legible."
4. "The style reads more [digital/cartoon] than the book's canonical [watercolor] — restore the canonical [STYLE]."
5. "This page feels static — add a directional cue (gaze, gesture, leading line) that pulls the eye toward the page turn."

---

## Verification

- [ ] Text-safe area reserved, calm, low-contrast, and correctly sized for the copy.
- [ ] Faces, hands, and key props clear of the gutter and trim edges.
- [ ] Content is age-appropriate for `[AGE BAND]` (non-frightening, non-violent, safe).
- [ ] Character matches the bible/reference pack (no drift).
- [ ] Canonical `[STYLE]` maintained.
- [ ] No manuscript text rendered (unless explicitly requested).
- [ ] Spread orientation and trim/bleed correct.
- [ ] Page has a clear emotional beat and a forward read toward the page turn.
