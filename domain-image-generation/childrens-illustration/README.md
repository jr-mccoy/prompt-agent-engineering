# Children's Book Illustration Prompts

Production-ready prompts for **illustrating material for children** — picture-book spreads, recurring-character design sheets, and book-length style consistency. Built on the cross-model character and style discipline in [CHARACTER_BIBLE_PIPELINE.md](../CHARACTER_BIBLE_PIPELINE.md).

> **Audience boundary:** These prompts are for authors/illustrators producing books **for** children. They are not for teaching kids and they generate no instructional content. For writing the manuscript, see the repo's `domain-childrens-writing/`. For program-level lesson/worksheet *teaching* material, see `domain-education-teaching/`.

**Parent guides:** [CHARACTER_BIBLE_PIPELINE.md](../CHARACTER_BIBLE_PIPELINE.md) · [IMAGE_MODEL_SELECTION_GUIDE.md](../IMAGE_MODEL_SELECTION_GUIDE.md)

---

## Prompts

| Prompt | What It Produces | Recommended Model |
|--------|------------------|-------------------|
| [Picture-Book Spread](childrens_book_illustration_spread.md) | One finished spread with a reserved text-safe area, gutter-safe composition, age-appropriate style | gpt-image-2 (text/word-art) · Nano Banana 2/Pro (fast iteration + refs) |
| [Character Design Sheet](childrens_character_design_sheet.md) | Turnaround / model sheet (front, three-quarter, side, back + expression strip) = the reusable reference pack | gpt-image-2 (one-pass sheet) · Nano Banana 2/Pro (role-separated pack) |
| [Consistent Style Series](childrens_consistent_style_series.md) | One illustration style + on-model characters across a whole book; book-length style-lock + re-anchor workflow | Nano Banana Pro (style slots) · gpt-image-2 (style commitment per spread) |

---

## Suggested Order

1. **Design the character** → `childrens_character_design_sheet.md` (build the reference pack first).
2. **Lock the book look** → `childrens_consistent_style_series.md` (establish the style anchor + style guide).
3. **Illustrate each spread** → `childrens_book_illustration_spread.md` (one finished spread at a time, restating style + bible).

---

## Model ID Quick Reference

| Name | Model ID |
|------|----------|
| gpt-image-2 | `gpt-image-2` |
| Nano Banana | `gemini-2.5-flash-image` |
| Nano Banana Pro | `gemini-3-pro-image` |
| Nano Banana 2 | `gemini-3.1-flash-image` |

---

## Children's-Illustration Conventions

- **Text-safe area first.** Reserve calm, low-contrast negative space for the publisher's typeset copy. Do not render manuscript text in the art unless explicitly asked.
- **Gutter-safe composition.** Keep faces, hands, and key props out of the center gutter and away from trim edges.
- **Age-appropriate by band.** Friendly proportions, non-frightening, non-violent; board-book art avoids small-realistic-hazard imagery.
- **Style is part of book identity.** Lock one canonical style and restate it every spread; never switch models mid-book.
- **One change per spread; re-anchor on a schedule.** Always reference the original anchor/pack, never recent outputs.
