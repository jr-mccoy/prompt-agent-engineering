---
title: "E-commerce — Styled Flat Lay"
category: image-generation/product
description: "Top-down styled flat lay arranging the product with complementary props on a styled surface — knolling-clean or organically styled."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-15
difficulty: intermediate
tags:
  - ecommerce
  - product-photography
  - flat-lay
  - top-down
  - styled
  - props
  - gpt-image-2
  - nano-banana
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/ecommerce-product/README.md
  - domain-image-generation/ecommerce-product/ecommerce_lifestyle_in_context.md
  - domain-image-generation/ecommerce-product/ecommerce_detail_macro_texture.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# E-commerce — Styled Flat Lay

**Objective:** Generate a top-down (overhead) flat lay that arranges the product with complementary props on a styled surface — either knolling-clean (precise right-angle grid) or organically styled (natural, editorial) — so the product reads as part of a curated, aspirational scene while remaining the hero.

**Why gpt-image-2 (primary):** Flat lays demand controlled composition (balance, negative space, prop hierarchy) and a true overhead camera. gpt-image-2's labeled prompt structure lets you specify the surface, the prop list, the arrangement logic, and the camera angle precisely — and it holds product fidelity within a multi-object composition.

**Why Nano Banana 2 (alternate):** Flat lays are highly iterative — you want to try many prop arrangements and color stories quickly. `gemini-3.1-flash-image` screens 8–20 layout candidates at 512px cheaply; pick the winning arrangement, then render at 2K. If you have a real product photo, pass it in an object slot to lock the hero.

**API parameters:**

gpt-image-2 (hero flat lay):
- `model="gpt-image-2"`
- `size="1024x1024"` (square is the flat-lay default) or `1536x1024` for banner crops
- `quality="high"`
- `n=4` while exploring arrangements

Nano Banana 2 (arrangement screening):
- `model="gemini-3.1-flash-image"`
- Screening: `size="512x512"`, `n=8`, `quality="standard"`
- Production: `size="2048x2048"`, `n=1`, `quality="high"`

---

## Inputs

- `[PRODUCT]` — the hero product
- `[PRODUCT COLOR]` — primary color + hex
- `[SURFACE]` — the styled background surface (e.g., "warm oak wood", "white marble", "linen textile", "concrete")
- `[PROPS]` — complementary items reinforcing the use case/category (e.g., "fresh coffee beans, a linen napkin, a brass spoon")
- `[ARRANGEMENT STYLE]` — knolling (precise grid, right angles) / organic (natural, editorial scatter)
- `[COLOR STORY]` — palette mood (e.g., "warm earthy neutrals", "cool monochrome")
- `[FRAME RESERVE]` — negative space left for copy/logo overlay later (top / left / none)

---

## Constraints (Must / Must Not)

**Must:**
- True overhead (90° top-down) camera with no perspective skew.
- Product is the clear hero — largest visual weight, most central or rule-of-thirds-anchored.
- Props are complementary and category-relevant, arranged with intentional balance and breathing room.
- Consistent, soft, even overhead lighting with gentle soft shadows for depth.
- Color story coheres across product, props, and surface.

**Must Not:**
- Tilt the camera or introduce vanishing-point perspective (it stops being a flat lay).
- Overcrowd the frame or let props out-weigh the product.
- Include readable competitor branding or off-palette clutter.
- Add text overlays (reserve negative space for later, but don't render copy).
- Distort product proportions or color.

---

## Production Prompt — gpt-image-2

```
SCENE:
A styled top-down flat lay on a [SURFACE] surface. True overhead camera at 90°, perfectly flat, no perspective skew. Soft, even overhead lighting with gentle soft shadows that add depth without harshness. Color story: [COLOR STORY] — product, props, and surface all cohere within this palette.

SUBJECT:
A single [PRODUCT] in [PRODUCT COLOR] is the hero — the largest and most central element. Arranged around it: [PROPS], placed in a [ARRANGEMENT STYLE] arrangement.
- If knolling: items aligned to right angles, evenly spaced, precise and clean.
- If organic: items styled naturally with editorial intention, overlapping slightly, with deliberate negative space.

KEY DETAILS:
- Product color [PRODUCT COLOR] exact hex; product fully sharp and undistorted.
- Props are category-relevant and reinforce the use case — they support, never compete with, the product.
- Balance the composition with intentional negative space. Reserve [FRAME RESERVE] of the frame as clean space for later copy/logo overlay (leave it empty, do not render text there).

USE CASE:
Secondary e-commerce listing image / category page hero / social-ready product styling. Aspirational and curated.

CONSTRAINTS:
- Style commitment: photorealistic styled flat-lay product photography. Editorial, clean.
- Camera must be true 90° overhead — no tilt, no perspective.
- Forbidden: text overlays, promotional badges, competitor logos or readable competitor packaging, overcrowding, off-palette clutter, product proportion distortion.
- Format: square 1024×1024 [or landscape 1536×1024].

If the camera shows perspective skew, if props out-weigh the product, or if any text overlay appears, the output is INCORRECT.
```

---

## Production Prompt — Nano Banana 2 (Arrangement Screening)

```
TASK: Create a styled top-down flat-lay product photograph.

A single [PRODUCT] in [PRODUCT COLOR] is the hero, arranged on a [SURFACE] surface with these complementary props: [PROPS]. Arrangement style: [ARRANGEMENT STYLE]. Color story: [COLOR STORY] — everything coheres within this palette.

CAMERA: True 90° overhead, perfectly flat, no perspective skew.

LIGHTING: Soft, even overhead light with gentle soft shadows for depth.

COMPOSITION: Product is the largest, most central element. Props support it with intentional balance and breathing room. Reserve [FRAME RESERVE] of the frame as clean negative space (leave empty — no text).

[If using a product reference photo: pass it in an OBJECT slot — TAKE exact product shape/color/finish; IGNORE its original background.]

CONSTRAINTS:
- MUST: true overhead camera, product as hero, coherent color story, [PRODUCT COLOR] exact, sharp undistorted product.
- MUST NOT: perspective tilt, overcrowding, competitor logos, off-palette clutter, text overlays, proportion distortion.
- If the camera shows perspective skew or props out-weigh the product, the output is INCORRECT.
- Quality: "high" (use "standard" + 512x512 to screen arrangements first)
```

---

## Iteration Plan

1. "There's a slight perspective tilt — make the camera a true flat 90° overhead."
2. "The props are crowding the product — remove [prop] and open up negative space around the hero."
3. "The color story is broken by [off-palette item] — swap it for something in the [COLOR STORY] palette."
4. "Move the arrangement so the [FRAME RESERVE] corner is clean for a logo overlay."
5. "Switch from organic to knolling — align everything to right angles with even spacing."

---

## Verification

- [ ] True 90° overhead camera, no perspective skew.
- [ ] Product is the clear hero (largest weight, central/anchored).
- [ ] Props complementary, balanced, with breathing room.
- [ ] Color story coheres across product, props, surface.
- [ ] Product color exact hex; sharp and undistorted.
- [ ] Reserved negative space is clean (no rendered text).
- [ ] No competitor logos, overcrowding, or off-palette clutter.
- [ ] `quality="high"` for production pass.
