---
title: "Book Cover — Nonfiction / Business"
category: image-generation/publishing-covers
description: "Authoritative nonfiction/business book cover with a clear title hierarchy and verbatim typography."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: advanced
tags:
  - book-cover
  - nonfiction
  - business
  - publishing
  - typography
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/publishing-covers/cover_fiction_book.md
  - domain-image-generation/publishing-covers/cover_ebook_kdp.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# Book Cover — Nonfiction / Business

**Objective:** Produce an authoritative nonfiction or business cover where the **title hierarchy is unambiguous** (main title > subtitle > author > credential), the design reads as credible rather than decorative, and every word renders verbatim.

**Why this model:** Nonfiction covers are typography-led — they often carry a main title, a subtitle, an author name, and a credential line, all of which must spell correctly and sit in a strict hierarchy. Use **gpt-image-2** (`quality="high"`) or **Nano Banana Pro** (`gemini-3-pro-image`) for exact text and font control. Speed-first models routinely scramble multi-line titles.

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `size="1024x1536"` (portrait, hardcover/trade proportions), `quality="high"`, `n=3`
- Nano Banana Pro path: `model="gemini-3-pro-image"`, portrait aspect, `quality="high"`

---

## Inputs

- `[TITLE]` — verbatim main title, exact case
- `[SUBTITLE]` — verbatim subtitle (the promise/argument)
- `[AUTHOR]` — verbatim author name
- `[CREDENTIAL]` — optional verbatim ("New York Times Bestselling Author", "PhD", "Founder of X") — only if true
- `[CATEGORY]` — leadership, finance, self-help, science, history, memoir, how-to
- `[TONE]` — 3 adjectives ("clean, confident, modern")
- `[MOTIF]` — optional restrained image/icon (a single object, abstract shape, no busy scene)
- `[PALETTE]` — hex codes
- `[TITLE TYPE STYLE]` — bold sans / classic serif / condensed grotesque
- `[FORBIDDEN]` — clichés to avoid (e.g., "no ladder-to-success", "no glowing lightbulb")

---

## Constraints (Must / Must Not)

**Must:**
- Establish a strict size hierarchy: main title largest, then subtitle, then author, then credential.
- Render every text element verbatim in an EXACT TEXT block with face, weight, hex, placement.
- Favor restraint — generous whitespace, a limited palette, type doing the work.
- Keep the main title legible at 200×300 px thumbnail.
- Only render `[CREDENTIAL]` if the user supplied it as factually true.

**Must Not:**
- Invent credentials, blurbs, bestseller seals, or publisher logos.
- Render a busy illustrated scene that buries the title (nonfiction is type-first).
- Misspell or re-case any line.
- Use the lightbulb / handshake / ladder / chess-piece cliché unless explicitly requested.
- Add a front-cover barcode.

**Note on credibility:** Do not fabricate awards, rankings, or endorsements. If `[CREDENTIAL]` is blank, omit it entirely — never invent one.

---

## Production Prompt (gpt-image-2)

```
ARTWORK:
Front cover for a [CATEGORY] nonfiction book. Type-first, authoritative, [TONE].
Portrait orientation. Generous whitespace; a restrained motif at most.

DESIGN DIRECTION:
- Palette: background [HEX], primary type [HEX], accent [HEX]. Limit to these.
- Motif (optional, restrained): [MOTIF] — a single clean element, not a scene.
  If no motif: a confident typographic cover on a solid or subtly textured field.
- Style commitment: clean graphic-design book cover, flat and confident. No
  photographic clutter, no 3D, no glossy effects.

TYPOGRAPHY HIERARCHY (verbatim, strict size order — largest to smallest):
1) Main title: "[TITLE]" — [TITLE TYPE STYLE], [weight], [HEX]. The single
   largest element, occupying ~25-35% of cover height. Legible at thumbnail size.
2) Subtitle: "[SUBTITLE]" — clearly smaller than the title, [weight], [HEX],
   directly beneath or above the title.
3) Author: "[AUTHOR]" — smaller still, [weight], [HEX], placed at the
   [bottom / top] in a stable position.
4) Credential (only if provided): "[CREDENTIAL]" — smallest, [HEX], near the author.

LAYOUT:
- Clear vertical hierarchy; the eye should read title → subtitle → author.
- Type aligned on a consistent grid (all flush-left, or all centered — pick one).
- All text inside a safe margin from the trim edge.

CONSTRAINTS:
- EXACT TEXT only, verbatim, no extra characters: the lines listed above and
  nothing else. No invented blurbs, award/bestseller seals, or publisher logo.
- No front-cover barcode.
- Forbidden: [FORBIDDEN], lightbulb/handshake/ladder/chess clichés (unless
  requested), watermarks, lorem ipsum.
- Format: portrait, [size].

If any line is misspelled, re-cased, or the hierarchy is unclear (subtitle as big
as the title, author competing with the title), the output is incorrect.
```

## Production Prompt (Nano Banana Pro)

```
TASK: Design an authoritative front cover for a [CATEGORY] nonfiction book.
Portrait, type-first, [TONE]. Generous whitespace, restrained palette.

DESIGN:
Background [HEX], type [HEX], accent [HEX]. Optional single restrained motif:
[MOTIF] (no busy scene). Clean graphic-design cover, flat and confident.

TYPOGRAPHY (render exactly, in strict size hierarchy):
- MAIN TITLE: "[TITLE]" — [TITLE TYPE STYLE], [weight], [HEX], the largest element,
  legible at thumbnail size.
- SUBTITLE: "[SUBTITLE]" — clearly smaller, [HEX].
- AUTHOR: "[AUTHOR]" — smaller still, [HEX].
- CREDENTIAL (only if provided): "[CREDENTIAL]" — smallest, [HEX].

CONSTRAINTS:
- MUST: verbatim text; strict title > subtitle > author hierarchy; consistent
  alignment grid; safe margin from trim edge.
- MUST NOT: invent credentials/blurbs/seals/logos; misspell or re-case; add a
  front-cover barcode; use [FORBIDDEN].
- Quality: "high".
```

---

## Iteration Plan

1. "Hierarchy is flat — the subtitle is competing with the title. Drop the subtitle to ~50% of the title size."
2. "Cover feels generic — commit harder to [TONE] via [type choice / single accent color]."
3. "Too busy — strip the motif and let the typography carry the cover on a solid [HEX] field."
4. "Thumbnail test: title doesn't survive at 200×300 px — increase weight and size."

---

## Verification

- [ ] Strict size hierarchy: title > subtitle > author > credential.
- [ ] Every line in an EXACT TEXT block, verbatim and correctly cased.
- [ ] No invented credentials, blurbs, seals, or publisher logos.
- [ ] Main title legible at 200×300 px thumbnail.
- [ ] Consistent alignment grid; all type inside a safe margin.
- [ ] No front-cover barcode.
- [ ] `quality="high"`.
