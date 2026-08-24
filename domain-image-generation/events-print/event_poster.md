---
title: "Event Poster"
category: image-generation/events-print
description: "Print-ready event poster with headline hierarchy, verbatim date/venue details, and bleed-safe layout."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: advanced
tags:
  - poster
  - event
  - print
  - typography
  - bleed
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/events-print/promotional_flyer.md
  - domain-image-generation/events-print/concert_gig_poster.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# Event Poster

**Objective:** Produce a print-ready event poster with a clear information hierarchy — headline first, then the essentials (date, time, venue), then secondary details — where every word renders verbatim and the layout respects print bleed and safe margins.

**Why this model:** A poster is dense with must-be-correct text (event name, date, venue, ticket info). Use **gpt-image-2** (`quality="high"`, 95%+ text accuracy) or **Nano Banana Pro** (`gemini-3-pro-image`, near-perfect text + exact font control). Never use a speed-first model when dates and addresses must be exact.

**Print spec (verify against your printer's specs):**
- Common sizes: 18×24 in, 24×36 in, A2 (420×594 mm), A1 (594×841 mm)
- **Bleed:** 0.125 in (3 mm) past trim on all sides; **safe area:** keep all text 0.25 in (6 mm) inside trim
- 300 DPI for print; CMYK for offset (generate RGB, convert in post)

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `size="1024x1536"` (portrait), `quality="high"`, `n=3`; upscale to print resolution in post
- Nano Banana Pro path: `model="gemini-3-pro-image"`, portrait aspect, `quality="high"`

---

## Inputs

- `[EVENT NAME]` — verbatim headline, exact case
- `[DATE]` — verbatim ("Saturday, October 12, 2026")
- `[TIME]` — verbatim ("7:30 PM – 10:00 PM")
- `[VENUE]` — verbatim name + address
- `[SUBHEAD / DESCRIPTION]` — optional verbatim one-liner
- `[CTA / TICKET INFO]` — verbatim ("Tickets at example.com", "Free admission", "RSVP required")
- `[ORGANIZER / SPONSORS]` — optional verbatim
- `[THEME / MOOD]` — 3 adjectives
- `[KEY VISUAL]` — central image/motif
- `[PALETTE]` — hex codes
- `[ORIENTATION + SIZE]` — portrait/landscape + trim size
- `[FORBIDDEN]` — to avoid

---

## Constraints (Must / Must Not)

**Must:**
- Establish a clear hierarchy: event name (largest) → date/venue → secondary details.
- Render every text element verbatim in an EXACT TEXT block with face, weight, hex, placement.
- Respect print: full-bleed artwork, all text inside a 0.25 in (proportional) safe area.
- Make the date and venue scannable from a distance (a poster is read while walking past).

**Must Not:**
- Misspell, abbreviate, or alter the date, time, or venue.
- Invent sponsor logos, prices, or URLs.
- Place critical text in the bleed zone (it will be trimmed off).
- Use slop hype words or stock-poster clichés in `[FORBIDDEN]`.

---

## Production Prompt (gpt-image-2)

```
ARTWORK:
Print-ready [ORIENTATION + SIZE] event poster. Theme: [THEME / MOOD]. Central
visual: [KEY VISUAL]. Designed to be read at a glance while walking past, and to
hold up at full poster size.

ART DIRECTION:
- Palette: dominant [HEX], secondary [HEX], accent [HEX].
- Style commitment: [photographic / illustrated / bold graphic / vintage print].
  Commit to ONE.
- Full-bleed artwork (extends past the trim). Keep ALL text inside the safe area:
  at least 0.25 in (proportionally ~4-5% of the shorter edge) inside the trim.

TEXT HIERARCHY (verbatim, largest to smallest):
1) Event name: "[EVENT NAME]" — [bold display / strong sans], [weight], [HEX].
   The single largest element; readable from across a room.
2) Date + time: "[DATE]" / "[TIME]" — clearly second in size, [weight], [HEX].
3) Venue: "[VENUE]" — third, [weight], [HEX].
4) Subhead (if present): "[SUBHEAD / DESCRIPTION]" — supporting, [HEX].
5) CTA / ticket info: "[CTA / TICKET INFO]" — clear and findable, [HEX].
6) Organizer / sponsors (if provided): "[ORGANIZER / SPONSORS]" — smallest,
   bottom band, [HEX].

LAYOUT:
- Reserve a quiet zone behind the event name (no busy texture there).
- Group date/time/venue so they read as one scannable block.
- Consistent alignment grid (flush-left or centered — pick one).

CONSTRAINTS:
- EXACT TEXT only, verbatim, no extra characters: the lines listed above and
  nothing else. No invented prices, URLs, or sponsor logos.
- Keep critical text out of the 0.125 in bleed zone.
- Forbidden: [FORBIDDEN], stock-poster clichés, watermarks, lorem ipsum.
- Format: [ORIENTATION + SIZE], full-bleed, print-ready.

If any date/time/venue line is misspelled or altered, or critical text sits in
the bleed zone, the output is incorrect.
```

## Production Prompt (Nano Banana Pro)

```
TASK: Design a print-ready [ORIENTATION + SIZE] event poster. Theme [THEME / MOOD].
Central visual: [KEY VISUAL]. Full-bleed artwork; all text inside a safe margin.

DESIGN:
Palette [HEX], [HEX], [HEX]. Commit to one rendering style ([photographic /
illustrated / bold graphic / vintage print]). Quiet zone behind the event name.

TEXT (render exactly, in strict size hierarchy):
- Event name: "[EVENT NAME]" — largest, [bold face], [weight], [HEX].
- Date/time: "[DATE]" / "[TIME]" — second, [HEX].
- Venue: "[VENUE]" — third, [HEX].
- Subhead (if present): "[SUBHEAD / DESCRIPTION]", [HEX].
- CTA: "[CTA / TICKET INFO]", [HEX].
- Organizer/sponsors (if provided): "[ORGANIZER / SPONSORS]", smallest, bottom.

CONSTRAINTS:
- MUST: verbatim text; strict hierarchy; date/time/venue grouped as one scannable
  block; all text ≥0.25 in inside the trim; consistent alignment.
- MUST NOT: alter date/time/venue; invent prices/URLs/sponsor logos; place text in
  the bleed; use [FORBIDDEN].
- Quality: "high".
```

---

## Iteration Plan

1. "Hierarchy is flat — the venue is competing with the event name. Drop date/venue to a clear second tier."
2. "Date block isn't scannable — group date/time/venue tighter and increase their size."
3. "Text is too close to the edge — pull everything ≥0.25 in inside the trim so the printer's bleed cut is safe."
4. "Quiet zone behind the headline is too busy — calm that area so the event name reads."

---

## Verification

- [ ] Every text element in an EXACT TEXT block, verbatim and correctly cased.
- [ ] Clear hierarchy: event name > date/venue > secondary details.
- [ ] Date/time/venue grouped into one scannable block.
- [ ] Full-bleed artwork; all critical text inside the 0.25 in safe area.
- [ ] No invented prices, URLs, or sponsor logos.
- [ ] `quality="high"`.
