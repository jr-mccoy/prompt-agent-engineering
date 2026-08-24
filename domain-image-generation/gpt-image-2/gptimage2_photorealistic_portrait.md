---
title: "GPT Image 2 — Photorealistic Candid Portrait"
category: image-generation/photography
description: "Editorial-grade candid photorealistic portrait using photography language and anti-gloss constraints."
techniques:
  - ST-01
  - ST-02
  - SV-13
  - SV-14
difficulty: intermediate
tags:
  - gpt-image-2
  - photorealism
  - portrait
  - editorial
  - photography
  - openai
updated: "2026-05-05"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# GPT Image 2 — Photorealistic Candid Portrait

**Objective:** Produce an editorial-grade, candid (un-posed-feeling) photorealistic portrait that does not have the "AI plasticky gloss" failure mode.

**When to use:**
- Editorial covers, longform article portraits, documentary-style imagery.
- Cases where you want the result to feel like an actual photograph, not a render.

**API parameters (recommended):**
- `model="gpt-image-2"`
- `size="1024x1536"` (portrait) or `"1536x1024"` (landscape)
- `quality="high"` (recommended for face fidelity)
- `n=1` (or `n=2` for two looks)

---

## Inputs

Fill in these placeholders before sending:

- `[SUBJECT]` — who: age range, gender presentation, ethnicity if relevant to the editorial intent, occupation/role
- `[SCENE]` — environment, time of day, weather, season
- `[ACTION]` — what the subject is doing (a verb, not a pose)
- `[FRAMING]` — full body / three-quarter / half / close-up; whether feet, hands, or eyes are critical
- `[EMOTIONAL TONE]` — contemplative / amused / determined / weary / focused (concrete, not "beautiful")
- `[USE CASE]` — e.g., "cover for a longform article on small fisheries"

---

## Constraints (Must / Must Not)

**Must:**
- State the word "photorealistic" literally.
- Use photography language: lens, lighting, film stock, framing.
- Demand real texture (pores, wrinkles, fabric weave, dust, salt, sweat, etc.).
- Specify scale and framing precisely (e.g., "full body, feet visible, hands naturally placed").

**Must Not:**
- Use "stunning", "masterpiece", "8K", "ultra-detailed", or other slop words.
- Use studio-polish words ("flawless skin", "glossy", "perfect") that trigger AI plastic gloss.
- Invent specific real people unless the user provides reference images.

---

## Production Prompt

```
SCENE:
[SCENE]. Natural ambient lighting consistent with the time of day described. Real environmental detail in the background — no studio backdrop, no artificial light spill.

SUBJECT:
[SUBJECT], [FRAMING]. The subject is mid-[ACTION] — this is candid, not posed. Gaze is [direction: down at the work / off to one side / mid-conversation / out of frame], not facing the camera unless the brief calls for it.

KEY DETAILS:
- Skin texture is real: visible pores, fine lines, slight imperfections. Not retouched.
- Clothing shows genuine wear consistent with the role: fabric weave, fold lines, weathering, stains where appropriate.
- Hair is naturally arranged — flyaways and asymmetry expected.
- Hands are believable: visible knuckles, nails, calluses where the role implies them.
- Environmental contact: the subject's clothing, hair, and skin react to the scene's wind, moisture, dust, or temperature.
- Emotional tone: [EMOTIONAL TONE].

USE CASE:
[USE CASE]. Editorial polish level. The image should feel like it was published in a magazine, not generated.

CONSTRAINTS:
- Style commitment: photorealistic. Shot like a 35mm film photograph on Kodak Portra 400, slight film grain visible at full resolution. Soft natural lighting, no harsh studio light.
- Lens feel: 50mm or 85mm, shallow depth of field with the subject in sharp focus and the background gently fallen-off (not heavily blurred).
- Composition: rule-of-thirds placement, not dead-center. Avoid symmetrical "passport photo" framing.
- Preserve: a candid, un-posed feel; honest unretouched textures.
- Forbidden: studio backdrop, ring-light catchlights, plasticky skin, perfectly-symmetrical faces, "AI hands" with extra/missing fingers, watermarks, in-image text.
- Format: portrait orientation [or landscape if specified].

If the skin looks plasticky or the hands have anatomical errors, the output is incorrect.
```

---

## Iteration Plan

If Phase 1 misses, refine with single-axis follow-ups:

1. "Make the lighting [warmer / cooler / more directional from the left]."
2. "Pull the framing back to [include feet / show more of the environment / tighten on the face]."
3. "Add more environmental wear to the clothing — [sweat / dust / salt residue / paint stains]."

---

## Verification

- [ ] "photorealistic" appears literally in the prompt.
- [ ] Photography language present (lens, film stock, lighting).
- [ ] Real-texture demand present (pores, fabric, environmental contact).
- [ ] No slop words.
- [ ] No "perfect / flawless / glossy" in the prompt.
- [ ] Hand and face failure conditions stated.
- [ ] `quality="high"` set.
