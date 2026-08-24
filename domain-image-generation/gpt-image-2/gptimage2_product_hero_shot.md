---
title: "GPT Image 2 — Product Hero Shot"
category: image-generation/product
description: "Clean e-commerce product hero with realistic contact shadow and legible labels."
techniques:
  - ST-01
  - ST-02
  - SV-13
  - SV-17
difficulty: beginner
tags:
  - gpt-image-2
  - product-photography
  - ecommerce
  - hero-shot
  - openai
updated: "2026-05-05"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# GPT Image 2 — Product Hero Shot

**Objective:** Generate a clean, e-commerce-ready hero image of a single product with a realistic contact shadow, accurate label legibility, and no studio mockup artifacts.

**API parameters (recommended):**
- `model="gpt-image-2"`
- `size="1024x1024"` for square; `1536x1024` for landing-page hero
- `quality="medium"` (use `high` if the label has small/dense text)
- `n=4` if you need shot variations
- `background="opaque"` if you'll be doing downstream extraction

---

## Inputs

- `[PRODUCT]` — what it is (e.g., "12oz matte black canister of cold-brew concentrate")
- `[MATERIALS]` — finish: matte / glossy / brushed / matte-with-soft-touch coating
- `[LABEL TEXT]` — verbatim copy that must appear on the product (if any)
- `[BRAND PALETTE]` — hex codes for primary/secondary brand colors
- `[BACKGROUND]` — solid color hex / soft gradient (allowed for products) / textured surface
- `[CAMERA ANGLE]` — front-on / three-quarter / top-down

---

## Constraints (Must / Must Not)

**Must:**
- Treat the product as the only hero element. No additional props unless explicitly listed.
- Include a believable, soft contact shadow (not a hard drop shadow).
- Render label text verbatim with the text-rendering contract.
- Match brand palette exactly via hex codes.

**Must Not:**
- Add lifestyle props, hands, or human elements.
- Add gradients on the product itself unless the brand palette specifies one.
- Render lorem-ipsum, faux-Latin, or invented copy on the label.
- Place the product mid-air without contact shadow (looks fake).

---

## Production Prompt

```
SCENE:
Studio-style product photography on a [BACKGROUND]. Single soft key light from the upper left, weak fill from the right, no harsh specular highlights. The product sits on a flat surface — believable contact shadow directly beneath it.

SUBJECT:
A single [PRODUCT], shot at [CAMERA ANGLE]. Centered with generous negative space on all sides for downstream cropping. Product fills approximately 60% of the frame.

KEY DETAILS:
- Material finish: [MATERIALS]. Render the surface response to light correctly — matte should diffuse, glossy should have a soft highlight only on the upper edge, brushed should show subtle directional grain.
- Brand palette: primary [HEX], secondary [HEX]. Use these exact hex values, not approximations.
- Label area: clean, fully visible, no warping. Exact copy below.
- Contact shadow: soft, directionally consistent with the key light, fading naturally — not a hard cast shadow.

USE CASE:
E-commerce product detail page hero. The image will be used at full size on a product page and cropped to a thumbnail. Must be production-ready without retouching.

CONSTRAINTS:
- Style commitment: photorealistic studio product photography. Not a 3D render. Not a stylized illustration.
- EXACT TEXT on label (verbatim, no extra characters): "[LABEL TEXT]" — [font style: e.g., bold sans-serif], [hex color], centered on the front face, 100% readable at full resolution.
- Preserve: the product's geometry, label legibility, and material finish character.
- Forbidden: lifestyle props, human hands, additional products, watermarks, drop shadows that float (use contact shadows only), invented copy on the label.
- Format: square 1024×1024 [or landscape 1536×1024 if specified].

If any label text is misspelled or any extra props appear, the output is incorrect.
```

---

## Iteration Plan

1. "Tighten the framing — the product should fill 70% of the frame instead of 60%."
2. "Soften the key light — the highlight on the upper edge is too bright."
3. "Adjust the brand palette: the [secondary color] should read more [warmer / cooler / more saturated]."

---

## Verification

- [ ] EXACT TEXT in quotes for any label copy.
- [ ] Both hex codes specified.
- [ ] Single product, no props.
- [ ] Soft contact shadow specified (not floating drop shadow).
- [ ] `quality="high"` if label has small text.
- [ ] No invented copy.
