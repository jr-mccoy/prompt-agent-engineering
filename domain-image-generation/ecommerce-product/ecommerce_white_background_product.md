---
title: "E-commerce — White Background Catalog Shot"
category: image-generation/product
description: "Clean white/seamless catalog product shot meeting Amazon/Shopify listing specs — pure white background, centered subject, no props or shadows."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: beginner
tags:
  - ecommerce
  - product-photography
  - white-background
  - amazon
  - shopify
  - catalog
  - gpt-image-2
  - nano-banana
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/ecommerce-product/README.md
  - domain-image-generation/ecommerce-product/ecommerce_variant_grid.md
  - domain-image-generation/gpt-image-2/gptimage2_product_hero_shot.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# E-commerce — White Background Catalog Shot

**Objective:** Generate a marketplace-compliant catalog image of a single product on a pure white (#FFFFFF) seamless background, centered, sharply lit, with the product filling 80–85% of the frame and a subtle contact shadow — ready to drop into an Amazon main image or Shopify listing without retouching.

**Why gpt-image-2 (primary):** Marketplace main images are unforgiving — they require true #FFFFFF background, accurate label text, and zero stylization. gpt-image-2's labeled-section prompts give precise control over background purity and the 95%+ text rendering keeps any on-pack copy legible. Use it for the hero/main listing image.

**Why Nano Banana 2 (alternate):** When you need to screen many framing/lighting options cheaply or batch-produce secondary catalog angles, `gemini-3.1-flash-image` lets you generate 6–20 candidates at 512px first, then commit one to a 2K render. Use it for fast iteration, not the single highest-fidelity main image.

**API parameters:**

gpt-image-2 (main image):
- `model="gpt-image-2"`
- `size="1024x1024"` (square is the marketplace default; Amazon requires the longest side ≥1600px for zoom — render at `2048x2048` if available)
- `quality="high"` (always high for catalog; small on-pack text demands it)
- `n=1` for the locked main image; `n=4` while exploring
- `background="opaque"` (you want true white baked in, not transparency)

Nano Banana 2 (screening / secondary angles):
- `model="gemini-3.1-flash-image"`
- Screening: `size="512x512"`, `n=6`, `quality="standard"`
- Production: `size="2048x2048"`, `n=1`, `quality="high"`

---

## Inputs

- `[PRODUCT]` — what it is (e.g., "stainless-steel insulated 750ml water bottle")
- `[MATERIALS]` — finish: matte / glossy / brushed / soft-touch / transparent
- `[PRODUCT COLOR]` — primary color + hex
- `[LABEL TEXT]` — verbatim on-pack copy that must appear (or "none")
- `[CAMERA ANGLE]` — front-on / slight three-quarter / straight-on with lid visible
- `[MARKETPLACE]` — Amazon / Shopify / Etsy / generic (drives spec)

---

## Constraints (Must / Must Not)

**Must:**
- Pure white background: true #FFFFFF, fully uniform edge-to-edge, no gray gradient or vignette.
- Single product, centered, filling 80–85% of the frame with even margins.
- Subtle, realistic contact shadow directly beneath the product (Amazon allows a soft natural shadow on the main image).
- Even, soft studio lighting — no blown highlights, no deep crushed shadows.
- On-pack text rendered verbatim and legible at full resolution.

**Must Not:**
- Add props, hands, packaging, logos-as-watermarks, text overlays, badges, or "best seller" graphics.
- Introduce off-white, cream, or gradient backgrounds (instant marketplace rejection).
- Float the product mid-air with a hard drop shadow.
- Crop the product against the frame edge — keep full clearance.
- Stylize, add bokeh, or apply an editorial color grade.

---

## Production Prompt — gpt-image-2 (Main Image)

```
SCENE:
Studio catalog photography on a pure white seamless background, #FFFFFF, uniform edge to edge with no gradient, no vignette, no visible horizon line. Soft, even, broad lighting from a large overhead softbox plus low fill — no harsh speculars, no blown highlights.

SUBJECT:
A single [PRODUCT], shot [CAMERA ANGLE], perfectly centered with equal margins on all sides. The product fills approximately 80–85% of the frame. A subtle, soft contact shadow sits directly beneath the product where it meets the surface — natural, not a hard cast shadow.

KEY DETAILS:
- Material finish: [MATERIALS]. Render light response correctly — matte diffuses, glossy carries a single soft highlight, brushed shows fine directional grain, transparent shows clean refraction with no muddy interior.
- Product color: [PRODUCT COLOR] — use this exact hex, no shifts.
- Sharp focus across the entire product, front to back. No depth-of-field blur — catalog images are fully sharp.

USE CASE:
[MARKETPLACE] catalog main listing image. The image must pass automated background-purity checks and be production-ready without retouching. It will be zoomed by buyers, so detail must hold at full resolution.

CONSTRAINTS:
- Style commitment: clean commercial catalog product photography. Not a 3D render. Not an illustration. Not lifestyle.
- EXACT TEXT on product (verbatim, no extra characters): "[LABEL TEXT]" — legible, undistorted, correctly placed on the pack. (If none: render no text on the product.)
- Background must be true #FFFFFF, fully uniform.
- Forbidden: props, human hands, packaging boxes, text overlays, promotional badges, watermarks, gradients, vignettes, color grading, bokeh, reflections of other objects.
- Format: square, longest side ≥1600px.

If the background is not pure white, if any prop appears, or if on-pack text is misspelled, the output is INCORRECT.
```

---

## Production Prompt — Nano Banana 2 (Screening / Secondary Angles)

```
TASK: Create a clean e-commerce catalog product photograph on a pure white background.

A single [PRODUCT] in [PRODUCT COLOR], [MATERIALS] finish, photographed [CAMERA ANGLE]. The product is centered and fills about 80–85% of the frame with even margins. A subtle soft contact shadow sits directly beneath it.

BACKGROUND: Pure white seamless, #FFFFFF, uniform edge to edge — no gradient, no gray, no vignette.

LIGHTING: Soft, even studio lighting from a large overhead softbox with low fill. No harsh highlights, no deep shadows. Product fully sharp front to back — no depth-of-field blur.

ON-PACK TEXT (verbatim, if any): "[LABEL TEXT]" — legible and undistorted.

CONSTRAINTS:
- MUST: true #FFFFFF background, single centered product, subtle contact shadow, [PRODUCT COLOR] exact, fully sharp.
- MUST NOT: props, hands, packaging, text overlays, badges, watermarks, gradients, bokeh, color grade.
- If the background is not pure white or any prop appears, the output is INCORRECT.
- Quality: "high" (use "standard" + 512x512 for the screening pass)
```

---

## Iteration Plan

1. "The background has a faint gray gradient in the corners — make it true uniform #FFFFFF edge to edge."
2. "The contact shadow is too dark and hard — soften it and reduce opacity so it reads as a gentle natural shadow."
3. "The product fills only ~65% of the frame — tighten so it fills 80–85% with even margins."
4. "There's a soft highlight blowing out on the [surface] — reduce the key light intensity so detail holds."
5. "The on-pack text is slightly warped on the curved surface — restore it flat and legible."

---

## Verification

- [ ] Background is true #FFFFFF, uniform, no gradient/vignette.
- [ ] Single product, centered, fills 80–85% of frame with even margins.
- [ ] Subtle, soft contact shadow (not floating, not hard cast).
- [ ] Product fully sharp — no depth-of-field blur.
- [ ] EXACT TEXT in quotes for any on-pack copy; verbatim and legible.
- [ ] No props, hands, badges, overlays, or watermarks.
- [ ] `quality="high"` for the production pass.
- [ ] Longest side ≥1600px for marketplace zoom compliance.
