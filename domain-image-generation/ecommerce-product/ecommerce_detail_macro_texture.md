---
title: "E-commerce — Detail Macro / Texture Shot"
category: image-generation/product
description: "Macro/close-up shot emphasizing material, texture, stitching, finish, or a key feature — the 'feel the quality' listing image."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: intermediate
tags:
  - ecommerce
  - product-photography
  - macro
  - detail
  - texture
  - material
  - gpt-image-2
  - nano-banana
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/ecommerce-product/README.md
  - domain-image-generation/ecommerce-product/ecommerce_white_background_product.md
  - domain-image-generation/ecommerce-product/ecommerce_flat_lay_styled.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# E-commerce — Detail Macro / Texture Shot

**Objective:** Generate a macro/close-up image that makes the buyer feel the product's quality — emphasizing material, texture, stitching, weave, grain, finish, or a single key feature at high magnification with sharp micro-detail and controlled, raking light that reveals surface character.

**Why gpt-image-2 (primary):** Macro work lives or dies on accurate material rendering and light response. gpt-image-2 renders matte/glossy/brushed/woven surfaces convincingly and lets you specify the exact feature in focus, the raking-light angle, and the shallow depth of field that isolates the detail.

**Why Nano Banana 2 (alternate):** When the exact texture must match a real sample, pass the real product/material photo in an object slot so the model reproduces the true weave/grain/finish rather than inventing one. Screen several light angles at 512px, then render the winner at 2K.

**API parameters:**

gpt-image-2 (hero macro):
- `model="gpt-image-2"`
- `size="1024x1024"` or `1536x1024`
- `quality="high"` (mandatory — micro-detail is the entire point)
- `n=4` while exploring light angles

Nano Banana 2 (texture-locked / screening):
- `model="gemini-3.1-flash-image"`
- Screening: `size="512x512"`, `n=6`, `quality="standard"`
- Production: `size="2048x2048"`, `n=1`, `quality="high"`

---

## Inputs

- `[PRODUCT]` — the product
- `[FEATURE]` — the specific detail to emphasize (e.g., "the double-needle stitching at the seam", "the brushed-aluminum bezel", "the leather grain and edge paint")
- `[MATERIALS]` — the material and finish at this detail
- `[PRODUCT COLOR]` — color + hex at the detail
- `[LIGHT CHARACTER]` — raking/grazing to reveal texture / soft for smooth finish
- `[BACKGROUND]` — soft-blurred product body / clean dark / clean light
- `[REFERENCE IMAGES]` — real material sample (Nano Banana path)

---

## Constraints (Must / Must Not)

**Must:**
- Fill the frame with the [FEATURE] at high magnification — this is a close-up, not a full product shot.
- Render micro-detail sharply: individual stitches, weave threads, grain, machining marks, finish texture.
- Use directional/raking light to reveal surface relief and texture (unless the finish is meant to read smooth).
- Keep the focal plane on the feature; allow shallow depth of field to fall off naturally behind it.
- Preserve true material color and finish character.

**Must Not:**
- Invent a texture that isn't the product's real material (when a reference is provided, match it).
- Over-smooth or plasticize the surface (kills the "quality" signal).
- Add text, callout labels, or measurement annotations.
- Show the whole product (that's the catalog/hero shot, not this).
- Introduce distracting props or busy backgrounds.

---

## Production Prompt — gpt-image-2

```
SCENE:
Extreme close-up macro product photography. The frame is filled with [FEATURE] of a [PRODUCT] at high magnification. Lighting: [LIGHT CHARACTER] — raking/grazing light from a low angle to reveal surface relief, texture, and material character. Background: [BACKGROUND], softly out of focus.

SUBJECT:
[FEATURE], shown in sharp micro-detail. Material: [MATERIALS]. Render the surface authentically — [for textile: individual threads and weave; for leather: grain and edge paint; for metal: brushed grain or machining marks; for matte plastic: fine diffuse texture]. The focal plane sits on the feature; depth of field is shallow so detail falls off naturally just behind it.

KEY DETAILS:
- Color at this detail: [PRODUCT COLOR] exact hex.
- Finish character: [matte diffuses / glossy carries a soft specular / brushed shows directional grain / woven shows thread structure].
- Crisp, tactile micro-detail — the buyer should feel they could touch it and sense the quality.

USE CASE:
Secondary e-commerce listing image — the "feel the quality / see the craftsmanship" shot. Communicates material premium-ness and build detail.

CONSTRAINTS:
- Style commitment: photorealistic macro product photography. Tactile and authentic — not over-smoothed, not plasticized.
- Forbidden: text, callout labels, measurement annotations, the full product silhouette, distracting props, busy backgrounds.
- Format: square 1024×1024 [or landscape 1536×1024].

If the surface looks plasticized/over-smoothed, if the whole product is shown, or if any annotation appears, the output is INCORRECT.
```

---

## Production Prompt — Nano Banana 2 (Texture-Locked)

```
REFERENCES:
Object Image 1: real photo of [PRODUCT]'s [FEATURE] / material sample.
- TAKE: exact texture, weave/grain/finish, color, surface relief.
- IGNORE: the original framing and background.

TASK:
Create an extreme close-up macro product photograph filling the frame with [FEATURE] of [PRODUCT] at high magnification.

MATERIAL: [MATERIALS] — reproduce the exact texture from the reference (do not invent a different weave/grain).

LIGHTING: [LIGHT CHARACTER] — low raking/grazing light to reveal surface relief and texture.

FOCUS: Focal plane on the feature; shallow depth of field falling off naturally behind it. Background: [BACKGROUND], softly out of focus.

COLOR: [PRODUCT COLOR] exact at this detail.

CONSTRAINTS:
- MUST: match the reference texture exactly; sharp tactile micro-detail; true material color and finish.
- MUST NOT: invent a different texture, over-smooth/plasticize, show the whole product, add text/callouts/annotations, or use distracting props.
- If the texture differs from the reference, the output is INCORRECT.
- Quality: "high" (use "standard" + 512x512 to screen light angles first)
```

---

## Iteration Plan

1. "The surface looks plasticized — increase the micro-texture and use lower raking light to reveal relief."
2. "Too much of the product is visible — push in tighter so only [FEATURE] fills the frame."
3. "The depth of field is too deep — make it shallower so the detail isolates from the background."
4. "The color shifted under the raking light — restore it to [PRODUCT COLOR] exact hex."
5. "The texture doesn't match the real material — match the [weave/grain] in the reference exactly."

---

## Verification

- [ ] Frame is filled with the [FEATURE] at high magnification (not the whole product).
- [ ] Micro-detail is sharp and tactile (stitches/weave/grain/machining visible).
- [ ] Light reveals surface relief (raking) unless a smooth finish is intended.
- [ ] Shallow depth of field isolates the feature.
- [ ] True material color (exact hex) and finish character preserved.
- [ ] No text, callouts, annotations, or distracting props.
- [ ] Texture matches the reference (Nano Banana path).
- [ ] `quality="high"` for production pass.
