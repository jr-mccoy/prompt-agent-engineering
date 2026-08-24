---
title: "Seamless Repeating Pattern (POD)"
category: image-generation/merch-print-on-demand
description: "Tileable, seamless repeating pattern for print-on-demand products with edge-matching constraints."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: advanced
tags:
  - pattern
  - seamless
  - tileable
  - repeat
  - merch
  - print-on-demand
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/merch-print-on-demand/tshirt_graphic.md
  - domain-image-generation/merch-print-on-demand/sticker_design.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# Seamless Repeating Pattern (POD)

**Objective:** Produce a single seamless, tileable pattern swatch whose edges match exactly so it can repeat infinitely across print-on-demand products (fabric, wrapping paper, phone cases, leggings, notebooks) with no visible seams or grid lines.

**Why this model:** Seamlessness is the entire job — the left edge must continue into the right, and the top into the bottom, with no break. Use **gpt-image-2** (`quality="high"`) for clean, controllable motifs, or **Nano Banana Pro** (`gemini-3-pro-image`) for richer detail with exact color control. For fast motif exploration, Nano Banana 2 can screen candidates cheaply before a high-quality production tile. **Always verify the tile by repeating it 2×2 in an editor** — model "seamless" output is not guaranteed and must be confirmed.

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `size="1024x1024"` (square tile), `quality="high"`, `n=4`
- Nano Banana Pro path: `model="gemini-3-pro-image"`, square aspect, `quality="high"`
- Screening: Nano Banana 2 (`gemini-3.1-flash-image`) `n=6` at low res to pick a motif/density first

> A single 1024×1024 tile is the unit. The repeat happens at print time when the POD product tiles the swatch. The prompt's job is to make that one tile edge-continuous.

---

## Inputs

- `[MOTIF]` — the repeating element(s) ("watercolor citrus slices and leaves")
- `[STYLE]` — flat-vector, watercolor, line-art, geometric, botanical, retro
- `[DENSITY]` — sparse / medium / dense packing
- `[LAYOUT]` — scattered/tossed / grid / half-drop / mirrored
- `[PALETTE]` — hex codes (background + motif colors)
- `[BACKGROUND COLOR]` — the field color the motifs sit on
- `[SCALE]` — how large the motif reads relative to the tile (small all-over vs large statement)
- `[PRODUCT]` — what it goes on (fabric, wrapping paper, phone case, leggings)
- `[FORBIDDEN]` — to avoid

---

## Constraints (Must / Must Not)

**Must:**
- Make the tile **seamless**: the left edge continues into the right, and the top into the bottom, so motifs cross edges and rejoin perfectly.
- Distribute motifs evenly per `[DENSITY]` and `[LAYOUT]` — no large empty dead zones, no clustered pile-ups unless the style calls for it.
- Keep one consistent background color and color palette across the whole tile.
- Commit to a single rendering style.

**Must Not:**
- Leave a hard border, frame, vignette, or margin around the tile (that breaks the repeat).
- Place a single centered "hero" subject (that's a graphic, not a pattern).
- Cut motifs off cleanly at the edge without continuing them on the opposite side.
- Render a mockup, a product, or a scene — output the flat swatch only.
- Use trademarked elements.

---

## Production Prompt (gpt-image-2)

```
DELIVERABLE:
A single SEAMLESS, TILEABLE repeating pattern swatch — a flat square tile only,
edge to edge, NO border, NO frame, NO margin, NO vignette, NO product, NO mockup,
NO scene. The artwork fills the entire square and bleeds off all four edges.

SEAMLESS REQUIREMENT (critical):
The tile must repeat infinitely with no visible seams. Motifs that touch an edge
must continue across to the OPPOSITE edge so they rejoin perfectly when tiled:
- A motif exiting the right edge re-enters at the left at the same height.
- A motif exiting the bottom re-enters at the top at the same horizontal position.
- No motif is cut flat at an edge without its other half on the opposite side.

PATTERN:
- Motif: [MOTIF]. Style: [STYLE]. Layout: [LAYOUT]. Density: [DENSITY]. Scale: [SCALE].
- Even all-over distribution — no large empty dead zones, no awkward clustering.
- Background field: solid [BACKGROUND COLOR]. Motif palette: [HEX], [HEX], [HEX].

CONSTRAINTS:
- Edge-continuous on all four sides (true seamless repeat).
- No border, frame, margin, vignette, or single centered hero subject.
- Output the flat swatch only — no product, mockup, or scene.
- Forbidden: trademarked elements, [FORBIDDEN], watermarks, text/labels, lorem ipsum.
- Format: square 1024x1024 tile, full bleed.

If the tile has a border/margin, a centered hero subject, or motifs that are cut at
an edge without continuing on the opposite side (i.e., it would show a seam when
tiled), the output is incorrect.
```

## Production Prompt (Nano Banana Pro)

```
TASK: Create ONE seamless, tileable square repeating-pattern swatch — flat artwork
only, edge to edge, no border/frame/margin/vignette, no product/mockup/scene.

SEAMLESS (critical): the tile repeats infinitely with no seams. Any motif crossing an
edge continues on the OPPOSITE edge at the matching position — right↔left and top↔
bottom — so it rejoins perfectly when tiled. No motif cut flat at an edge.

PATTERN:
Motif [MOTIF], style [STYLE], layout [LAYOUT], density [DENSITY], scale [SCALE]. Even
all-over distribution. Background field solid [BACKGROUND COLOR]; motif palette [HEX],
[HEX], [HEX].

CONSTRAINTS:
- MUST: edge-continuous on all four sides; even distribution; one consistent
  background + palette; one rendering style; full bleed.
- MUST NOT: add a border/frame/margin/vignette; place a single centered hero; cut
  motifs at an edge without continuation; render a product/mockup/scene; use
  trademarks or text; use [FORBIDDEN].
- Quality: "high".
```

---

## Iteration Plan

1. "Seam test failed — when tiled 2×2 the [edge] shows a hard line. Continue the motifs across that edge to the opposite side."
2. "There's a dead zone in the [region] — redistribute motifs for even all-over coverage at [DENSITY]."
3. "It rendered a border/frame — remove it; the artwork must bleed off all four edges."
4. "Scale is off for [PRODUCT] — make the motif [larger/smaller] relative to the tile."

---

## Verification

- [ ] **Seam test:** repeat the tile 2×2 in an editor — no visible seams or grid lines on any edge.
- [ ] Motifs that exit one edge re-enter the opposite edge at the matching position.
- [ ] No border, frame, margin, vignette, or centered hero subject.
- [ ] Even all-over distribution per density/layout; no dead zones.
- [ ] One consistent background color + palette; one rendering style.
- [ ] Flat swatch only — no product/mockup/scene; no trademarks; no stray text.
- [ ] `quality="high"`.
