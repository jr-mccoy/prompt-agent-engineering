---
title: "GPT Image 2 — Multi-Reference Composite"
category: image-generation/composite
description: "Compose a single output from up to 16 indexed reference images using gpt-image-2's multi-reference support."
techniques:
  - ST-01
  - ST-02
  - SV-13
  - SV-15
difficulty: advanced
tags:
  - gpt-image-2
  - multi-reference
  - composite
  - image-edit
  - openai
updated: "2026-05-05"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-image-generation/gpt-image-2/gptimage2_character_consistency_anchor.md
  - domain-image-generation/nano-banana/nanobana_multi_reference_character_scene.md
  - domain-image-generation/nano-banana/nanobana_product_multi_angle_composite.md
---

# GPT Image 2 — Multi-Reference Composite

**Objective:** Combine up to 16 reference images into a single composite where each reference plays a specific role (subject identity, garment, scene, lighting, color grade, etc.). Used for virtual try-on, ad composites, set-design renders, and any case where you have multiple visual ingredients you want the model to combine deliberately.

**API parameters (recommended):**
- `model="gpt-image-2"`
- Endpoint: `/v1/images/edits` (multi-image variant)
- `image=[open("ref1.png", "rb"), open("ref2.png", "rb"), ...]` — up to 16
- `quality="high"` (recommended; composites need precise blending)
- `n=1`

---

## Inputs

For each reference image (1–16), provide:
- **Index** (1–16)
- **Role** (one of: subject identity / garment / scene / lighting / color grade / pose / object to insert / typography / mood / other)
- **One-sentence description**
- **What to take from it** (face? silhouette? color palette? lighting direction?)
- **What to ignore from it** (don't take its background; don't take its color grade)

---

## Reference Allocation Strategy

When you have 16 slots, allocate by purpose — don't dump random refs:

| Slots | Role |
|---|---|
| 1–3 | Subject identity (face, body, brand mark) |
| 4–6 | Garment / object reference |
| 7–9 | Scene / environment |
| 10–12 | Lighting / mood reference |
| 13–16 | Style / color grade reference |

**Empirical finding:** for character consistency, ~15 references dramatically outperform 2 — but only if each is allocated a distinct role. Don't waste slots on near-duplicates of the same view.

---

## Constraints (Must / Must Not)

**Must:**
- Index every reference (Image 1, Image 2, …) and state its role.
- For each ref, state both what to take AND what to ignore.
- Specify the four matching dimensions: lighting, perspective, scale, shadow direction.
- State which ref's lighting / color grade is the master (the rest yield to it).

**Must Not:**
- Provide more than one reference per role unless they show different angles of the same subject.
- Leave a reference's role undefined (the model will guess).
- Mix conflicting lighting references without naming a master.

---

## Production Prompt

```
REFERENCES (each indexed and described — what to take, what to ignore):

Image 1 — ROLE: subject identity (face).
Description: [one sentence].
TAKE: exact face, expression, hairstyle, skin tone, proportions.
IGNORE: background, clothing, lighting.

Image 2 — ROLE: subject identity (body / pose).
Description: [one sentence].
TAKE: body shape, posture, height, hand position.
IGNORE: clothing, background.

Image 3 — ROLE: garment.
Description: [one sentence].
TAKE: the [garment type]: silhouette, fabric, color, trim details.
IGNORE: the model wearing it, the photo's lighting.

Image 4 — ROLE: scene / environment.
Description: [one sentence].
TAKE: setting, props, depth, architectural details.
IGNORE: any people in it, any garments visible.

Image 5 — ROLE: lighting (MASTER).
Description: [one sentence].
TAKE: lighting direction, softness, color temperature, shadow falloff. This is the lighting master — the entire composite must conform to it.
IGNORE: composition, subject, color grade.

Image 6 — ROLE: color grade.
Description: [one sentence].
TAKE: color grade, saturation level, contrast curve, highlight/shadow color cast.
IGNORE: composition, subject.

[... up to Image 16, each with index, role, description, take, ignore ...]

TASK:
Composite a single image where:
- The subject is built from Images 1 and 2 (face from Image 1; body/pose from Image 2).
- The subject wears the garment from Image 3.
- The setting is the scene from Image 4.
- The entire image's lighting follows Image 5 (master).
- The entire image's color grade follows Image 6.

PLACEMENT AND GEOMETRY:
- The subject is positioned [where in the scene from Image 4 — e.g., "centered, three-quarter framing, standing on the left third"].
- Subject scale relative to the scene: [realistic — subject's height matches the architecture's implied scale].
- Camera angle: [match Image 4 / use a new specified angle].

MATCHING DISCIPLINE:
- Lighting: every element matches Image 5's lighting direction, softness, and color temperature.
- Perspective: every element conforms to Image 4's perspective and vanishing points.
- Scale: subject and props at realistic scale relative to each other.
- Shadow direction: consistent across the composite, from Image 5's master direction.
- Color grade: applied uniformly per Image 6.

PRESERVE LIST:
- The exact face from Image 1 — facial features, expression, skin tone, hairstyle.
- The exact garment from Image 3 — silhouette, fabric, color, trim.
- The exact setting from Image 4 — architectural details, props, depth.

CONSTRAINTS:
- Style commitment: photorealistic [or as specified].
- EXACT TEXT (if any): "[copy]" — [typography spec].
- Forbidden: any element not specified by the references; double-shadows from conflicting lighting; mismatched scale (e.g., subject's height inconsistent with door height in scene); watermarks; lorem ipsum.
- Format: [size], [orientation], quality high.

If the face from Image 1 is altered in any way, the output is incorrect. If lighting on the subject does not match Image 5, the output is incorrect. If the scale of the subject relative to the scene from Image 4 is implausible, the output is incorrect.
```

---

## Iteration Plan

1. "The subject's face has drifted from Image 1 — restore it to exactly match Image 1, preserving everything else from this current composite."
2. "Lighting on the subject's face doesn't match Image 5 — re-cast it from the same direction with the same softness."
3. "The garment from Image 3 is rendering too saturated — reduce saturation to match Image 6's color grade."

---

## Verification

- [ ] Every used reference has Index, Role, Description, TAKE, IGNORE.
- [ ] Exactly one reference is named the lighting MASTER.
- [ ] Exactly one reference is named the color-grade master (or stated to be Image 5).
- [ ] Matching discipline lists lighting, perspective, scale, shadow direction.
- [ ] Failure conditions specific to the most likely drift modes.
- [ ] `quality="high"`.
