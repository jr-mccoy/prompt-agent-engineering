---
title: "Concert / Gig Poster"
category: image-generation/events-print
description: "Stylized concert/gig poster with band name, lineup, and verbatim date/venue, print-ready with bleed."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: advanced
tags:
  - poster
  - concert
  - gig
  - music
  - print
  - typography
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/events-print/event_poster.md
  - domain-image-generation/events-print/promotional_flyer.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# Concert / Gig Poster

**Objective:** Produce a stylized, collectible concert/gig poster where the **headliner name dominates**, the lineup reads in clear billing order, and the date/venue/ticket info render verbatim — with a strong art-led aesthetic and print bleed respected.

**Why this model:** Gig posters are aesthetic-led (screen-print, psychedelic, punk, indie, metal looks) but still carry exact text: band names, lineup, date, venue, ticket source. Use **gpt-image-2** (`quality="high"`) or **Nano Banana Pro** (`gemini-3-pro-image`) for verbatim band/lineup text inside a stylized treatment. For a purely art-driven background with no text (you'll set the lineup yourself), Nano Banana 2 or Midjourney can do the imagery — but the default below renders text.

**Print spec (verify against your printer's specs):**
- Common sizes: 11×17 in (tabloid), 18×24 in, 24×36 in, A2
- **Bleed:** 0.125 in (3 mm); **safe area:** text 0.25 in (6 mm) inside trim
- 300 DPI; for true screen-print, limit to a defined spot-color count (see constraints)

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `size="1024x1536"` (portrait), `quality="high"`, `n=3`; upscale to print resolution
- Nano Banana Pro path: `model="gemini-3-pro-image"`, portrait aspect, `quality="high"`

---

## Inputs

- `[HEADLINER]` — verbatim, exact case (the dominant name)
- `[SUPPORT ACTS]` — verbatim, in billing order ("with Opener A, Opener B")
- `[DATE]` — verbatim
- `[VENUE]` — verbatim name + city
- `[DOORS / SHOW TIME]` — verbatim ("Doors 7 PM / Show 8 PM")
- `[TICKET INFO]` — verbatim ("Tickets at venue.com", "$25 ADV / $30 DOS", "18+")
- `[GENRE / STYLE]` — punk, psych-rock, indie folk, metal, electronic, hip-hop
- `[ART AESTHETIC]` — the poster art movement to evoke (e.g., "60s psychedelic screen-print", "DIY punk photocopy", "minimalist Swiss")
- `[KEY VISUAL]` — central art motif
- `[PALETTE]` — hex codes (and spot-color count if screen-print)
- `[SPOT COLORS?]` — yes (give N) / no (full color)
- `[FORBIDDEN]` — to avoid

---

## Constraints (Must / Must Not)

**Must:**
- Make `[HEADLINER]` the dominant text element; support acts clearly smaller, in billing order.
- Render all text verbatim in an EXACT TEXT block.
- Commit hard to `[ART AESTHETIC]` — gig posters are art objects.
- Respect bleed + safe area; keep critical text (date/venue/tickets) inside the safe area and legible.
- If `[SPOT COLORS?]` = yes, constrain the palette to the stated number of flat spot colors (no gradients/blends) for screen-print feasibility.

**Must Not:**
- Render real bands' existing logos or another artist's trade dress.
- Misspell band names, date, venue, or ticket info.
- Invent support acts, prices, or age restrictions.
- Bury the headliner under the artwork.
- Use gradients/photographic blends if a spot-color screen-print is requested.

---

## Production Prompt (gpt-image-2)

```
ARTWORK:
Stylized, collectible [ORIENTATION] concert/gig poster for a [GENRE / STYLE] show.
Art aesthetic: [ART AESTHETIC] — commit fully, this is an art object. Central
motif: [KEY VISUAL]. Full-bleed artwork; critical text inside the safe area.

ART DIRECTION:
- Palette: [HEX], [HEX], [HEX]. [If SPOT COLORS = yes: limit to exactly [N] flat
  spot colors, no gradients or photographic blends — must be screen-print feasible.]
- Texture/treatment true to [ART AESTHETIC] (e.g., halftone, registration offset,
  woodcut, risograph grain).

TEXT HIERARCHY (verbatim, billing order):
1) Headliner: "[HEADLINER]" — the DOMINANT text element, stylized to fit the
   aesthetic, [HEX]. Reads from across the room.
2) Support acts: "[SUPPORT ACTS]" — clearly smaller, in billing order, [HEX].
3) Date: "[DATE]" — clear and legible, [HEX].
4) Venue: "[VENUE]" — clear, [HEX].
5) Doors/show: "[DOORS / SHOW TIME]" — [HEX].
6) Ticket info: "[TICKET INFO]" — findable, [HEX], usually a bottom band.

LAYOUT:
- Headliner dominates the upper/central zone; the info block (date/venue/doors/
  tickets) sits as a clean, legible band even within the stylized art.
- Keep all critical info inside the 0.25 in safe area.

CONSTRAINTS:
- EXACT TEXT only, verbatim, no extra characters: the names and lines above and
  nothing else. No invented support acts, prices, or age limits.
- Forbidden: real bands' existing logos, another artist's trade dress, [FORBIDDEN],
  watermarks, lorem ipsum.
- [If SPOT COLORS = yes: no gradients, blends, or photographic shading.]
- Format: [ORIENTATION + SIZE], full-bleed, print-ready.

If a band name, date, venue, or ticket line is misspelled or altered, or the
headliner is not the dominant text, the output is incorrect.
```

## Production Prompt (Nano Banana Pro)

```
TASK: Design a stylized [ORIENTATION] gig poster for a [GENRE / STYLE] show in the
[ART AESTHETIC] style. Central motif [KEY VISUAL]. Full bleed; critical text inside
a safe margin. Palette [HEX], [HEX], [HEX]. [If spot colors: exactly [N] flat colors,
no gradients.]

TEXT (render exactly, billing order):
- Headliner "[HEADLINER]" — dominant, stylized, [HEX].
- Support "[SUPPORT ACTS]" — smaller, billing order, [HEX].
- Date "[DATE]", Venue "[VENUE]", Doors/show "[DOORS / SHOW TIME]", Tickets
  "[TICKET INFO]" — legible info block, [HEX].

CONSTRAINTS:
- MUST: verbatim names + info; headliner dominant; info block legible within the art;
  critical text ≥0.25 in inside trim; full commitment to [ART AESTHETIC].
- MUST NOT: render real bands' logos or others' trade dress; misspell/alter any text;
  invent acts/prices/age limits; use gradients if spot-color screen-print; use [FORBIDDEN].
- Quality: "high".
```

---

## Iteration Plan

1. "Headliner doesn't dominate — scale it up and stylize it as the poster's centerpiece; shrink the support acts."
2. "Info block is buried in the art — pull date/venue/tickets into a clean legible band."
3. "Spot-color violation — gradients appeared; flatten to the [N] requested screen-print colors."
4. "Push the [ART AESTHETIC] harder — add [halftone / registration offset / riso grain]."

---

## Verification

- [ ] Headliner is the dominant text element; support acts smaller in billing order.
- [ ] All text in an EXACT TEXT block, verbatim — band names, date, venue, tickets correct.
- [ ] Art aesthetic fully committed.
- [ ] If spot-color: palette limited to N flat colors, no gradients (screen-print feasible).
- [ ] Full-bleed artwork; critical info inside the 0.25 in safe area and legible.
- [ ] No real bands' logos or others' trade dress; no invented acts/prices.
- [ ] `quality="high"`.
