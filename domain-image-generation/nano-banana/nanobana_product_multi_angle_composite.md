---
title: "Nano Banana 2 — Product Multi-Angle Composite"
category: image-generation/product
description: "Generate a multi-angle product composite leveraging Nano Banana 2's 10 object reference slots for maximum product fidelity."
techniques:
  - ST-01
  - ST-02
  - SV-11
  - SV-13
  - SV-15
difficulty: intermediate
tags:
  - nano-banana
  - nano-banana-2
  - product-photography
  - multi-angle
  - e-commerce
  - composite
  - google
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/NANO_BANANA_GUIDE.md
  - domain-image-generation/gpt-image-2/gptimage2_product_hero_shot.md
  - domain-image-generation/gpt-image-2/gptimage2_multi_reference_composite.md
---

# Nano Banana 2 — Product Multi-Angle Composite

**Objective:** Generate a multi-angle product composite where every view of the product is geometrically consistent, using Nano Banana 2's 10 object reference slots to lock shape, finish, color, logo placement, and proportions from multiple angles simultaneously.

**Why Nano Banana 2:** 10 object reference slots (vs. gpt-image-2's 16 undifferentiated refs) means you can feed the model dedicated angle references — front, back, side, top, detail — and the model knows each is an object reference, not a style or character cue. The 512px screening pass lets you test 6–20 candidates cheaply before committing to a high-resolution render.

**API parameters:**
- `model="gemini-3.1-flash-image"`
- Screening: `size="512x512"`, `n=6`, `quality="standard"`
- Production: `size="2048x2048"` or target aspect ratio, `n=1`, `quality="high"`

---

## Inputs

- `[PRODUCT NAME]` — the product being photographed
- `[PRODUCT DESCRIPTION]` — materials, finish, colors, key features, logo placement
- `[REFERENCE IMAGES]` — 3–8 photos of the actual product from different angles
- `[COMPOSITE FORMAT]` — grid layout (e.g., 2×3 for 6 angles) or single hero shot
- `[BACKGROUND]` — studio (white/gray seamless), lifestyle (contextual), transparent
- `[USE CASE]` — e-commerce listing, product page, social media, pitch deck, catalog

---

## Constraints (Must / Must Not)

**Must:**
- Pass all product reference images in OBJECT slots (not character or style slots).
- Maintain exact product proportions, colors, and finish across all views.
- Each angle in the composite must show a distinct, useful view of the product.
- Logo/branding must be legible and correctly placed in every view where it's visible.
- Lighting must be physically consistent across all panels.

**Must Not:**
- Mix product references with scene/environment references in the same object slots without clear separation.
- Use near-duplicate angles — each reference must provide genuinely new geometric information.
- Allow the model to "improve" or redesign the product (add details, change proportions, modify colors).
- Generate angles that are physically impossible (e.g., showing the bottom and top simultaneously in one panel without a mirror).
- Use motion blur or dynamic angles for e-commerce product shots.

---

## Reference Allocation (10 Object Slots)

| Slot | Role | Image | What the Model Takes |
|------|------|-------|---------------------|
| Obj 1 | Front view | Straight-on front, neutral lighting | Shape outline, logo, front details |
| Obj 2 | Back view | Straight-on back | Back panel, ports, labels, regulatory marks |
| Obj 3 | Left side | 90° left profile | Side thickness, button placement, profile shape |
| Obj 4 | Right side | 90° right profile | Side details, port locations |
| Obj 5 | Three-quarter front | 45° front-left or front-right | Depth, front-to-side transition, 3D form |
| Obj 6 | Three-quarter back | 45° back-left or back-right | Back-to-side transition |
| Obj 7 | Top-down | Directly overhead | Top surface, footprint shape |
| Obj 8 | Detail shot | Close-up of key feature | Texture, finish quality, small details |
| Obj 9 | Scale reference | Product next to a known object | Real-world size impression |
| Obj 10 | (Available) | Packaging, accessory, or second detail | Supporting context |

**You don't need all 10.** For most products, 4–6 references (front, back, three-quarter, top, detail) are sufficient. Use additional slots only when the product has complex geometry or multiple key features.

---

## Production Prompt — Multi-Angle Grid

```
REFERENCES:
Object Images 1–[N]: Product reference photos for [PRODUCT NAME].

- Image O1 (front): straight-on front view.
  TAKE: front face shape, logo, color, surface finish, front-panel details.
  IGNORE: background, lighting.

- Image O2 (back): straight-on back view.
  TAKE: back panel layout, ports, labels, regulatory marks.
  IGNORE: background.

- Image O3 (three-quarter): 45° view showing depth.
  TAKE: 3D form, edge transitions, how front meets side.
  IGNORE: background, reflections.

- Image O4 (top-down): overhead view.
  TAKE: top surface, footprint shape, top details.
  IGNORE: background.

- Image O5 (detail): close-up of [KEY FEATURE].
  TAKE: texture, finish, micro-details at this feature.
  IGNORE: surrounding context.

[Add O6–O10 as needed for additional angles or details.]

PRODUCT IDENTITY — [PRODUCT NAME]:
1. Material: [primary material, finish — matte/glossy/brushed/textured]
2. Color: [primary color, hex if precise, secondary colors]
3. Dimensions impression: [compact/medium/large, rough proportions]
4. Logo: [location, size relative to surface, color]
5. Key features: [buttons, ports, screens, textures, unique design elements]
6. Distinctive details: [anything that must be visible in every applicable angle]

TASK:
Generate a [COMPOSITE FORMAT] product composite showing [PRODUCT NAME]
from [N] angles on a [BACKGROUND] background.

LAYOUT:
[Columns] × [Rows] grid, [reading order].
Thin neutral gutters ([color], [width]px). No text labels or angle names.
Each panel shows the product at the same scale relative to the frame.

ANGLES (one per panel):
1) Front — straight-on, product centered
2) Three-quarter — 45° showing front and [left/right] side
3) Side profile — 90° showing thickness and side details
4) Back — straight-on back panel
5) Top-down — overhead showing footprint
6) Detail — close-up of [KEY FEATURE]

LIGHTING:
Studio lighting — soft key from upper [left/right] at 45°.
Even fill to minimize harsh shadows.
[White/gray] seamless background.
Same lighting angle and intensity in every panel.

STYLE:
Commercial product photography. Clean, sharp, undistorted.
[Photorealistic / studio-lit / catalog-quality].

PRESERVE (every panel):
- Exact product shape and proportions from references.
- Material finish: [matte/glossy/brushed] — no finish changes between angles.
- Color accuracy: [primary color hex] — no color shifts.
- Logo placement, size, and legibility where the logo is visible.
- [DISTINCTIVE DETAILS] — must appear in every applicable panel.

CONSTRAINTS:
- If the product shape, proportions, or colors differ from the reference images,
  the output is INCORRECT.
- If the logo is visible but illegible or misplaced, the output is INCORRECT.
- If the lighting direction is inconsistent between panels, the output is INCORRECT.
- Same product scale in every panel — don't make one angle appear larger than another.
- No text, labels, or annotations in the composite.
- Quality: "high"
```

---

## Production Prompt — Single Hero Shot

For a single hero shot rather than a multi-angle grid:

```
REFERENCES:
Object Images 1–[N]: Product reference photos for [PRODUCT NAME].
[Same TAKE/IGNORE allocation as above.]

PRODUCT IDENTITY — [PRODUCT NAME]:
[Same identity block as above.]

TASK:
Generate a single hero product photograph of [PRODUCT NAME].

COMPOSITION:
[PRODUCT NAME] positioned [center / rule-of-thirds / lower-third] of frame.
Camera angle: [three-quarter front / straight-on / slightly elevated].
Focal length feel: [85mm — slight compression] / [50mm — natural].
Product fills [40-60]% of frame width.
Shallow depth of field — product razor-sharp, background softly blurred.

ENVIRONMENT:
[Studio: white seamless / gray gradient / black dramatic]
OR
[Lifestyle: [describe the surface and context — marble counter, wooden desk, etc.]]
[1-2 contextual props that reinforce the use case, never competing with the product.]

LIGHTING:
[Studio: soft key upper-left 45°, white bounce fill, rim light from behind]
OR
[Lifestyle: natural window light from [direction], practical lights as accent]
Color temperature: [daylight / warm / cool].

STYLE:
[Commercial product photography / editorial / lifestyle / dramatic / minimal].

CONSTRAINTS:
- Product identity lock: shape, finish, color, logo from references.
- If any product detail differs from references, the output is INCORRECT.
- Quality: "high"
```

---

## Screening Workflow

1. **Screen at 512px** — Generate 6 candidates at `quality="standard"`, `size="512x512"`.
2. **Evaluate** — Check product shape consistency, logo accuracy, lighting uniformity, and angle coverage.
3. **Select** — Pick the best candidate.
4. **Refine** — Tighten the prompt based on the winning candidate's strengths and weaknesses.
5. **Produce** — Generate the final version at `quality="high"`, full resolution.

**What to check in screening:**
- Does the product look like the same object in every panel?
- Is the logo correctly placed and legible?
- Is the material finish consistent (not matte in one panel, glossy in another)?
- Are the angles genuinely different and useful?
- Is the lighting direction physically consistent?

---

## Iteration Plan

1. "The product color in panel 3 reads [wrong shade] — match to reference image O1's exact [correct color]."
2. "The logo in the three-quarter view is distorted — restore correct proportions from reference O1."
3. "The material finish appears glossy in the side view but matte in the front — normalize to [correct finish]."
4. "Panels 2 and 6 show nearly the same angle — replace panel 6 with a [bottom/detail/back] view."
5. "The product appears larger in panel 4 than in panel 1 — equalize scale across all panels."

---

## Verification

- [ ] All product reference images passed in OBJECT slots (not character or style slots).
- [ ] Product identity maintained across all panels (shape, color, finish, logo).
- [ ] Each panel shows a genuinely distinct angle.
- [ ] Lighting direction consistent across all panels.
- [ ] Logo legible and correctly placed in every applicable view.
- [ ] Material finish consistent (no matte-to-glossy drift).
- [ ] Product scale uniform across panels.
- [ ] No text, labels, or annotations in the composite.
- [ ] Background is clean and consistent.
- [ ] `quality="high"` set for production pass.
