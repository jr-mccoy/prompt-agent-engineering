---
title: "Children's Book — Consistent Illustration Style Across a Whole Book"
category: image-generation/childrens-illustration
description: "Maintain one illustration style and consistent characters across every spread of a complete picture book; a book-length style-lock workflow."
techniques:
  - ST-01
  - ST-02
  - SV-13
  - SV-15
  - SV-17
difficulty: advanced
tags:
  - childrens-illustration
  - style-consistency
  - picture-book
  - book-length
  - character-consistency
  - gpt-image-2
  - nano-banana
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/childrens-illustration/childrens_book_illustration_spread.md
  - domain-image-generation/childrens-illustration/childrens_character_design_sheet.md
  - domain-image-generation/CHARACTER_BIBLE_PIPELINE.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/nano-banana/nanobana_multi_reference_character_scene.md
---

# Children's Book — Consistent Illustration Style Across a Whole Book

**Objective:** Keep **one illustration style** and **on-model characters** across every spread of a complete picture book (typically 12–16 spreads / 24–32 pages). This is a book-length style-lock workflow that wraps the single-spread prompt: you establish a **style anchor** + **character reference pack**, then generate each spread restating the same style and identity, and you re-anchor on a schedule before drift accumulates.

> **Audience boundary:** Illustrating *for* children (you are producing the book), not teaching kids. For the manuscript, see the repo's `domain-childrens-writing/`. This prompt is the picture-book specialization of the cross-model [CHARACTER_BIBLE_PIPELINE.md](../CHARACTER_BIBLE_PIPELINE.md) — read that for the full drift-management theory; this file adds the book-specific style discipline.

**Why model choice matters:** Book-length consistency is the hardest consistency task. **Nano Banana Pro** is the strongest choice because its dedicated **style slots** can lock the rendering approach independently of identity. **gpt-image-2** works well by restating an explicit style commitment in every spread prompt and passing the style anchor as a reference image. Pick one model and stay on it for the whole book — mixing models mid-book is a guaranteed style break.

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `/v1/images/edits` (pass style anchor + character refs), `quality="high"`, consistent `size` for all interior spreads, `n=1`
- Nano Banana path: `model="gemini-3-pro-image"` (Pro, style slots) preferred; `"gemini-3.1-flash-image"` (NB2) for cheaper iteration; `quality="high"`

---

## The Book-Length Workflow

```
Step 1: Write the STYLE GUIDE (text) + CHARACTER BIBLE
Step 2: Generate the STYLE ANCHOR spread (the "look" reference) + character design sheet
Step 3: Lock both — verify the look, then freeze it
Step 4: Generate each spread restating the style guide + bible (one change at a time)
Step 5: Re-anchor every 5 spreads (compare to the style anchor; fix drift before it compounds)
```

---

## Inputs

- `[BOOK TITLE]` / `[SPREAD COUNT]` — e.g., 14 spreads
- `[STYLE GUIDE]` — the durable rendering facts (see template below)
- `[CHARACTER BIBLE]` + `[REFERENCE PACK]` — from the character design sheet
- `[STYLE ANCHOR]` — the finished spread that defines the canonical look
- `[PALETTE]` — a fixed, named palette used across the whole book
- `[AGE BAND]` — target reader age

### Style Guide Template (write once, restate every spread)

```
STYLE GUIDE — [BOOK TITLE]
1. Medium look: [e.g., "soft watercolor with visible cold-press paper grain"]
2. Line: [e.g., "loose pencil under-drawing left visible; no hard ink outlines"]
3. Edges: [soft / hard / mixed]
4. Palette: [PALETTE — named anchor colors with hex; warm/cool bias]
5. Lighting: [direction, softness — kept consistent across spreads]
6. Texture: [paper grain / grain-free / brush texture]
7. Detail density: [low/medium — leaves room for text-safe areas]
8. Mood: [warm, gentle, whimsical, cozy]
```

---

## Constraints (Must / Must Not)

**Must:**
- Establish a **style anchor** before generating interior spreads; verify it, then freeze it.
- **Restate the full style guide AND character bible in every spread prompt** — never abbreviate to "same style as before."
- Pass the **style anchor and the original character reference pack** as references in every spread (Nano Banana Pro: style slots).
- Keep the **palette, lighting direction, and detail density** identical book-wide.
- Maintain a **consistent text-safe-area approach** across spreads (see childrens_book_illustration_spread.md).
- Re-anchor against the original style anchor every ~5 spreads.

**Must Not:**
- Use a recent spread's output as the reference for the next spread — drift compounds; always reference the original anchor/pack.
- Change the medium look, line treatment, or palette mid-book.
- Switch image models mid-book.
- Bundle multiple changes per spread (new scene + new outfit + new mood all at once).

---

## Production Prompt — Per-Spread (style + identity lock)

```
[Pass references: STYLE ANCHOR image + CHARACTER REFERENCE PACK.
 Nano Banana Pro: STYLE ANCHOR in Style slot 1, character refs in Char slots 1–4.]

BOOK: [BOOK TITLE], Spread [N] of [SPREAD COUNT]. Picture book for readers aged [AGE BAND].

STYLE GUIDE (restated in full — this is canonical for the whole book):
[paste the 8-point style guide, including the named PALETTE with hex codes]

CHARACTER BIBLE — [CHARACTER NAME] (restated in full):
[paste the 5–10 trait bible]

SCENE FOR THIS SPREAD:
[CHARACTER NAME] [ACTION] in [SCENE]. Emotional beat: [EMOTION].

COMPOSITION:
- Place focal action in [page region]; keep faces, hands, key props out of the gutter and off the trim edges.
- TEXT-SAFE AREA: keep [TEXT-SAFE ZONE] calm and low-detail for the copy (no rendered text).

PRESERVE (every spread):
- Canonical look from the STYLE ANCHOR: medium, line, edges, palette, lighting direction, detail density.
- [CHARACTER NAME]'s exact face, hair color, eye color, proportions, distinctive marks from the reference pack.

CHANGE (only one major dimension vs. the previous spread):
- [new setting] OR [new outfit] OR [new action/expression] — not all three.

CONSTRAINTS:
- MUST: identical style guide + palette + lighting direction to the anchor; on-model character; age-appropriate.
- MUST NOT: shift medium/line/palette; use a recent output as reference; render manuscript text; clutter the text-safe area.
- Format: same size/orientation as all interior spreads. Quality: "high".

If the medium look, line treatment, palette, or lighting differs from the STYLE ANCHOR — or the character drifts from the reference pack — the spread is incorrect and breaks book consistency.
```

---

## Re-Anchor Protocol (book-length)

| Spread Count | Re-Anchor Check |
|---|---|
| 12–16 spreads (standard picture book) | Compare to the style anchor at spreads 5, 10, and final |
| 24–32 spreads (longer / chapter-illustrated) | Every 5 spreads |

When drift appears:
1. Regenerate the drifted spread from the **original** style anchor + character pack (not recent outputs).
2. If one trait keeps drifting (e.g., hair hue, palette warmth), tighten the bible/style guide with hex codes.
3. If the medium look wanders (watercolor → digital), reinforce with the style anchor in a style slot (Nano Banana Pro) or restate the medium explicitly (gpt-image-2).
4. If the outfit changes permanently mid-book, generate a new full-body reference in the new outfit and add it to the pack from that spread forward.

---

## Iteration Plan

1. "Spreads 1–4 are warmer than spreads 5–8 — re-lock the named `[PALETTE]` and re-render the cool spreads."
2. "The line treatment hardened into ink outlines on this spread — restore the loose visible pencil under-drawing from the anchor."
3. "Detail density crept up and crowded the text-safe area — return to the anchor's lower detail density."
4. "`[CHARACTER NAME]`'s hair hue shifted — restore the exact hex from the bible across all later spreads."
5. "The lighting direction flipped — restore the anchor's consistent key-light direction."

---

## Verification

- [ ] Style anchor generated and verified before interior spreads.
- [ ] Full style guide + character bible restated in every spread prompt.
- [ ] Style anchor + original character reference pack passed as references each spread.
- [ ] Palette, lighting direction, and detail density consistent book-wide.
- [ ] Text-safe-area approach consistent across spreads.
- [ ] Only one major change per spread.
- [ ] Same model used for the entire book.
- [ ] Re-anchor checks performed on schedule; drift corrected from the original anchor.
