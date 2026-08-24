---
title: "E-commerce — Variant Grid (Color / Size Consistency)"
category: image-generation/product
description: "A consistent grid of color/size/style variants of the same product — identical framing, lighting, and scale across every cell."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-11
  - SV-13
  - SV-15
  - SV-17
difficulty: advanced
tags:
  - ecommerce
  - product-photography
  - variants
  - color-grid
  - consistency
  - swatches
  - gpt-image-2
  - nano-banana
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/ecommerce-product/README.md
  - domain-image-generation/ecommerce-product/ecommerce_white_background_product.md
  - domain-image-generation/nano-banana/nanobana_product_multi_angle_composite.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# E-commerce — Variant Grid (Color / Size Consistency)

**Objective:** Generate a single composite grid showing the same product in multiple color/size/style variants, where every cell shares identical framing, camera angle, lighting, scale, and background — so only the variant attribute changes. The product geometry and finish must be locked across all cells; only the specified attribute (color/size/material) varies.

**Why gpt-image-2 (primary, one-pass grid):** gpt-image-2 has the strongest one-pass multi-panel consistency — it can render all variants in a single grid with shared lighting and scale, which is exactly what a variant grid needs. Use it when you want the whole grid generated coherently in one render.

**Why Nano Banana 2 (alternate, reference-locked per cell):** When the base product geometry must be pixel-locked to a real reference, `gemini-3.1-flash-image` lets you pass the product in object slots and re-generate each color variant against the locked geometry — and screen the full set cheaply at 512px before committing. Its role-separated reference slots keep "the product" distinct from "the variant attribute."

**API parameters:**

gpt-image-2 (one-pass grid):
- `model="gpt-image-2"`
- `size="1024x1024"` (square grid) or `1536x1024` for a wide row of variants
- `quality="high"`
- `n=4` to get several consistent grid candidates

Nano Banana 2 (reference-locked variants + screening):
- `model="gemini-3.1-flash-image"`
- Screening: `size="512x512"`, `n=6`, `quality="standard"`
- Production: `size="2048x2048"`, `n=1`, `quality="high"`

---

## Inputs

- `[PRODUCT]` — the base product (geometry that stays constant)
- `[MATERIALS]` — finish (constant across variants unless material is the variant)
- `[VARIANT ATTRIBUTE]` — what changes: color / size / material / pattern
- `[VARIANT LIST]` — the exact variants, each with name + hex if color (e.g., "Midnight #1A1A2E, Sand #D9C5A0, Forest #2E4034")
- `[GRID LAYOUT]` — columns × rows (e.g., 3×2 for 6 variants) or single row
- `[BACKGROUND]` — pure white #FFFFFF / light gray seamless
- `[CAMERA ANGLE]` — the single shared angle for all cells
- `[REFERENCE IMAGES]` — base product photo (Nano Banana path)

---

## Constraints (Must / Must Not)

**Must:**
- Lock product geometry, proportions, camera angle, scale, framing, and lighting identically across every cell.
- Vary ONLY the [VARIANT ATTRIBUTE]; everything else is constant.
- Render each color variant at its exact hex.
- Keep equal margins and consistent gutters; every cell is the same size.
- Maintain a uniform, clean background across all cells.

**Must Not:**
- Let the camera angle, scale, or lighting drift between cells.
- "Improve" or redesign the product per cell (add/remove features).
- Render variant name labels or text in the grid (unless explicitly requested as captions).
- Mix in variants not on the list, or skip listed variants.
- Allow color bleed/inaccuracy — each hex must read true.

---

## Production Prompt — gpt-image-2 (One-Pass Grid)

```
SCENE:
A clean product variant grid on a [BACKGROUND] background. A [GRID LAYOUT] grid with even cells, equal margins, and thin neutral gutters. Identical soft, even studio lighting in every cell — same key direction and intensity throughout. No text, no labels.

SUBJECT:
The SAME [PRODUCT] shown once per cell, each cell identical in geometry, proportions, camera angle ([CAMERA ANGLE]), scale, and framing. The ONLY thing that changes between cells is the [VARIANT ATTRIBUTE].

VARIANTS (one per cell, in order):
[VARIANT LIST — e.g.:
1) Midnight — render the product in #1A1A2E
2) Sand — render the product in #D9C5A0
3) Forest — render the product in #2E4034
... one cell per listed variant]

KEY DETAILS:
- Material finish: [MATERIALS] — constant across all cells (unless material is the variant attribute).
- Each color variant uses its exact hex — no approximations, no color bleed.
- Every cell: same product at the same scale, same angle, same lighting, same shadow treatment.

USE CASE:
E-commerce variant selector / swatch grid / category overview. Buyers compare options at a glance, so consistency across cells is critical.

CONSTRAINTS:
- Style commitment: clean commercial catalog product photography, consistent across the grid.
- The product geometry, proportions, angle, scale, and lighting must be identical in every cell — only the [VARIANT ATTRIBUTE] differs.
- Forbidden: per-cell redesigns, text/labels in the grid, props, drifting camera angle or scale, inaccurate hex colors.
- Background uniform across all cells.
- Format: square 1024×1024 [or wide 1536×1024 for a single row].

If any cell shows a different angle, scale, or product geometry — or if any color hex is wrong — the output is INCORRECT.
```

---

## Production Prompt — Nano Banana 2 (Reference-Locked Variants)

```
REFERENCES:
Object Images 1–[N]: base product reference photos for [PRODUCT].
- TAKE: exact product geometry, proportions, finish, logo placement.
- IGNORE: original background, lighting, and original color (color will be set per variant).

PRODUCT IDENTITY — [PRODUCT] (constant across all variants):
- Geometry/proportions: locked from references.
- Material finish: [MATERIALS].
- Logo/branding: [location and appearance].
- Camera angle for every cell: [CAMERA ANGLE].

TASK:
Generate a [GRID LAYOUT] variant grid on a [BACKGROUND] background. The same product appears once per cell; only the [VARIANT ATTRIBUTE] changes.

VARIANTS (one per cell, in order):
[VARIANT LIST with names + exact hex]

LAYOUT:
[Columns] × [Rows], even cells, equal margins, thin neutral gutters. Same product scale and lighting in every cell. No text or labels.

CONSTRAINTS:
- MUST: lock geometry/proportions/angle/scale/lighting across all cells from references; vary only [VARIANT ATTRIBUTE]; exact hex per color variant.
- MUST NOT: redesign the product per cell, drift the angle/scale, add text/labels/props, or render inaccurate colors.
- If any cell's geometry, angle, scale, or color is wrong, the output is INCORRECT.
- Quality: "high" (use "standard" + 512x512 to screen the full set first)
```

---

## Iteration Plan

1. "Cell 3's camera angle drifted — make all cells use the identical [CAMERA ANGLE]."
2. "The Sand variant reads too yellow — correct it to exactly #D9C5A0."
3. "The product appears slightly larger in cell 5 — equalize scale across all cells."
4. "The lighting is harder in the right column — normalize key direction and intensity across the whole grid."
5. "Remove the variant name text that appeared in the gutters — the grid should have no labels."

---

## Verification

- [ ] Product geometry/proportions identical in every cell.
- [ ] Camera angle, scale, framing, and lighting identical across cells.
- [ ] Only the [VARIANT ATTRIBUTE] changes between cells.
- [ ] Every color variant matches its exact hex.
- [ ] Equal cell sizes, equal margins, consistent gutters.
- [ ] Uniform clean background across all cells.
- [ ] No per-cell redesigns, text/labels, or props (unless captions requested).
- [ ] All listed variants present; none added or skipped.
- [ ] `quality="high"` for production pass.
