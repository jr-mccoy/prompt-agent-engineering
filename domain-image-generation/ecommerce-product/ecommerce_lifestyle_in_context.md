---
title: "E-commerce — Lifestyle In-Context Shot"
category: image-generation/product
description: "Product shown in a real-use lifestyle scene that communicates scale, use case, and aspiration while keeping the product as the hero."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-15
  - SV-17
difficulty: intermediate
tags:
  - ecommerce
  - product-photography
  - lifestyle
  - in-context
  - secondary-image
  - gpt-image-2
  - nano-banana
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/ecommerce-product/README.md
  - domain-image-generation/ecommerce-product/ecommerce_white_background_product.md
  - domain-image-generation/ecommerce-product/ecommerce_detail_macro_texture.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# E-commerce — Lifestyle In-Context Shot

**Objective:** Generate a lifestyle product image showing the product in a believable real-use environment — establishing scale, use case, and aspiration — while the product stays the unmistakable hero. This is a secondary listing image (not the white-background main image), used to help buyers picture the product in their own life.

**Why gpt-image-2 (primary):** Lifestyle scenes need realistic environmental lighting, accurate product fidelity within a busy scene, and the product to remain clearly identifiable. gpt-image-2's labeled SCENE/SUBJECT split keeps the environment from overwhelming the product, and it holds product identity well against a detailed background.

**Why Nano Banana 2 (alternate):** When you have actual product reference photos and want the product geometry/finish locked precisely into a new environment, `gemini-3.1-flash-image` lets you pass the product in object reference slots and the scene in style/context slots, then screen many environment options at 512px before committing.

**API parameters:**

gpt-image-2 (hero lifestyle):
- `model="gpt-image-2"`
- `size="1536x1024"` (landscape for listing carousels and banners) or `1024x1024`
- `quality="high"`
- `n=4` while exploring environments; `n=1` once locked

Nano Banana 2 (reference-locked / screening):
- `model="gemini-3.1-flash-image"`
- Screening: `size="512x512"`, `n=8`, `quality="standard"`
- Production: `size="2048x2048"`, `n=1`, `quality="high"`

---

## Inputs

- `[PRODUCT]` — what it is + key visual identifiers
- `[PRODUCT COLOR]` — primary color + hex
- `[MATERIALS]` — finish
- `[ENVIRONMENT]` — the real-use setting (e.g., "sunlit modern kitchen counter", "trail at golden hour", "minimalist home office")
- `[USER CONTEXT]` — in use by hands / staged unused / mid-action
- `[TARGET BUYER VIBE]` — aesthetic cue (e.g., "warm domestic", "rugged outdoor", "clean Scandinavian")
- `[REFERENCE IMAGES]` — actual product photos (Nano Banana path)

---

## Constraints (Must / Must Not)

**Must:**
- Keep the product the clear hero — sharpest element, strongest visual weight, ~30–50% of frame.
- Place the product in a physically plausible position within the scene (resting on a real surface, held naturally).
- Use environmental lighting consistent with the setting (window light, golden hour, etc.) that still flatters the product.
- Communicate scale through context cues (a hand, a counter, a familiar nearby object).
- Preserve product color, finish, and any branding accurately.

**Must Not:**
- Let props or background compete with or obscure the product.
- Distort the product's proportions to fit the scene.
- Add visible logos of other brands, readable competitor packaging, or distracting clutter.
- Render uncanny hands or faces — keep people partial/peripheral (a hand, a torso) unless a full figure is requested.
- Add text overlays or promotional graphics (this is a photo, not an ad).

---

## Production Prompt — gpt-image-2

```
SCENE:
A [ENVIRONMENT], styled with a [TARGET BUYER VIBE] aesthetic. Natural environmental lighting appropriate to the setting — [describe: e.g., soft morning window light from the left / warm golden-hour sun]. The scene feels real and lived-in but uncluttered, with shallow depth of field so the background softly recedes.

SUBJECT:
A single [PRODUCT] in [PRODUCT COLOR], [MATERIALS] finish, [USER CONTEXT]. The product is the clear hero — the sharpest, most prominent element, occupying roughly 30–50% of the frame and placed naturally on/in the scene (resting on a real surface or held in a natural grip).

KEY DETAILS:
- Material finish: [MATERIALS] — render its light response correctly within the scene's lighting.
- Product color: [PRODUCT COLOR] exact hex — must not shift under the ambient color cast.
- Scale cue: include [a hand / the counter edge / a familiar nearby object] so the buyer understands the product's real size.
- 1–2 supporting props only, reinforcing the use case, never competing with the product.

USE CASE:
Secondary e-commerce listing image (lifestyle / in-context). Helps the buyer imagine owning and using the product. Not the white-background main image.

CONSTRAINTS:
- Style commitment: photorealistic lifestyle product photography. Natural, candid, editorial-clean.
- The product must remain razor-sharp and clearly identifiable; the background may be softly blurred but the product never is.
- Forbidden: text overlays, promotional badges, competitor logos or readable competitor packaging, uncanny faces, clutter that obscures the product, proportion distortion.
- People, if any, appear only as partial/peripheral elements (a hand or torso) unless a full figure is explicitly part of the use case.
- Format: landscape 1536×1024 [or square 1024×1024].

If the product is not the clear hero, if its proportions are distorted, or if any text overlay appears, the output is INCORRECT.
```

---

## Production Prompt — Nano Banana 2 (Reference-Locked)

```
REFERENCES:
Object Images 1–[N]: Product reference photos for [PRODUCT].
- TAKE: exact product shape, proportions, color, finish, logo placement.
- IGNORE: the original background and lighting from the reference photos.

PRODUCT IDENTITY — [PRODUCT]:
- Material: [MATERIALS]
- Color: [PRODUCT COLOR] (hex)
- Logo/branding: [location and appearance]
- Distinctive details that must survive into the new scene: [list]

TASK:
Place this exact product into a new lifestyle scene: a [ENVIRONMENT] with a [TARGET BUYER VIBE] aesthetic, [USER CONTEXT].

COMPOSITION:
Product is the hero — sharpest element, ~30–50% of frame, placed naturally on a real surface (or held in a natural grip). Shallow depth of field so the background softly recedes. Include [scale cue] so the buyer reads the real size.

LIGHTING:
Environmental light appropriate to the setting — [describe] — that still flatters the product. Product color must not shift under ambient cast.

CONSTRAINTS:
- MUST: preserve exact product shape, proportions, color [PRODUCT COLOR], and finish from references; product stays sharp hero.
- MUST NOT: distort proportions, redesign the product, add text overlays/badges, show competitor logos, render uncanny faces, or clutter the scene.
- If the product geometry/color differs from references, the output is INCORRECT.
- Quality: "high" (use "standard" + 512x512 to screen environments first)
```

---

## Iteration Plan

1. "The background is competing with the product — increase background blur and remove the [distracting prop]."
2. "The product reads too small in the scene — bring it forward so it fills ~40% of the frame."
3. "The ambient light is shifting the product color — correct it back to [PRODUCT COLOR] exact hex."
4. "The hand looks uncanny — replace it with a clean natural grip or crop to just the product on the surface."
5. "The vibe feels too cluttered/staged — simplify to 1 supporting prop and let the scene breathe."

---

## Verification

- [ ] Product is the clear hero: sharpest element, ~30–50% of frame.
- [ ] Product proportions, color (exact hex), and finish preserved.
- [ ] Believable placement in a physically plausible position.
- [ ] Scale cue present so buyers read real size.
- [ ] Environmental lighting flatters the product without shifting its color.
- [ ] ≤2 supporting props; none obscure or compete with the product.
- [ ] No text overlays, badges, competitor logos, or uncanny faces.
- [ ] `quality="high"` for production pass.
