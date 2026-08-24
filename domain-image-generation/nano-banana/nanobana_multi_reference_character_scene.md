---
title: "Nano Banana — Multi-Reference Character Scene"
category: image-generation/character
description: "Place a character into a new scene using Nano Banana's 14-reference role-separated allocation for maximum identity consistency."
techniques:
  - ST-01
  - ST-02
  - SV-13
  - SV-15
difficulty: advanced
tags:
  - nano-banana
  - character-consistency
  - multi-reference
  - scene-generation
  - google
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/NANO_BANANA_GUIDE.md
  - domain-image-generation/gpt-image-2/gptimage2_character_consistency_anchor.md
  - domain-image-generation/gpt-image-2/gptimage2_multi_reference_composite.md
---

# Nano Banana — Multi-Reference Character Scene

**Objective:** Place a known character into a new scene using the full reference-image allocation system. The character's identity is locked via a role-separated reference pack (face, body, outfit, style), and the scene is controlled via object and environment references. Use case: children's book illustrations, comic sequences, brand mascot campaigns, episodic content.

**Why Nano Banana:** Google's models explicitly separate character references from object references from style references, giving the prompt author fine-grained control over what each reference contributes. Nano Banana 2 offers 10 object + 4 character slots; Nano Banana Pro offers 6 object + 5 character + 3 style slots.

**API parameters:**
- `model="gemini-3.1-flash-image"` (Nano Banana 2) or `"gemini-3-pro-image"` (Pro)
- Pass reference images via the `image` parameter
- `quality="high"`, `n=1`

---

## Inputs

### Character Inputs (from Character Bible)
- `[CHARACTER NAME]` — stable name used in every prompt
- `[CHARACTER BIBLE]` — 5–10 durable visual traits (hair, eyes, build, marks, outfit)
- `[REFERENCE PACK]` — 3–4 character reference images (front, three-quarter, profile, full-body)

### Scene Inputs
- `[SCENE]` — setting description
- `[ACTION]` — what the character is doing
- `[EMOTION]` — facial expression
- `[CAMERA]` — shot type, angle, focal length feel
- `[LIGHTING]` — time of day, direction, quality
- `[STYLE]` — canonical rendering style (must match the reference pack)

### Optional Environment References
- `[SCENE REF]` — photo or illustration of the target environment
- `[STYLE REF]` — color grade / rendering mood reference

---

## Constraints (Must / Must Not)

**Must:**
- Pass character reference images in the CHARACTER slots (not object slots).
- Restate the full character bible (5–10 traits) in every scene prompt.
- State the canonical style commitment.
- Change ONE major dimension per generation (scene OR outfit OR expression).
- Include a failure condition for identity drift.

**Must Not:**
- Mix character references with object references in the same slots.
- Use near-duplicate reference images — each must show a distinct view.
- Allow the model to redesign the character to fit the scene's aesthetic.
- Bundle multiple changes (new scene + new outfit + new expression) in one prompt.

---

## Reference Allocation

### Using Nano Banana 2 (10 object + 4 character)

| Slot | Role | Image |
|------|------|-------|
| Char 1 | Face reference (front) | Neutral front-view headshot |
| Char 2 | Face reference (three-quarter) | Three-quarter view showing facial depth |
| Char 3 | Body reference (full-body) | Full-body showing proportions and outfit |
| Char 4 | Profile reference | Side view showing nose, chin, ear, hair silhouette |
| Obj 1 | Scene/environment | Photo or illustration of the target setting |
| Obj 2 | Scene detail | Key prop or architectural element |
| Obj 3–10 | (Available for additional objects, props, or scene elements) | |

### Using Nano Banana Pro (6 object + 5 character + 3 style)

| Slot | Role | Image |
|------|------|-------|
| Char 1–4 | Face and body references | Same as Nano Banana 2 |
| Char 5 | Expression reference | Key expression for this scene |
| Obj 1–2 | Scene/environment | Setting and key prop |
| Obj 3–6 | (Available for additional scene elements) | |
| Style 1 | Color grade target | Reference image for the tonal mood |
| Style 2 | Rendering exemplar | Example of the canonical illustration style |
| Style 3 | (Available for mood/atmosphere reference) | |

---

## Production Prompt

```
REFERENCES:
Character Images 1–4: Reference pack for [CHARACTER NAME].
- Image C1 (face front): neutral front-view headshot.
  TAKE: exact facial features, skin tone, eye color, hair from the front.
  IGNORE: background, clothing (unless outfit is canonical).

- Image C2 (face three-quarter): three-quarter view.
  TAKE: facial depth, cheekbone structure, jaw angle, ear shape.
  IGNORE: background, lighting.

- Image C3 (full-body): full-body showing proportions.
  TAKE: body type, height impression, posture, outfit details.
  IGNORE: background, expression.

- Image C4 (profile): side view.
  TAKE: nose shape, chin projection, ear position, hair silhouette.
  IGNORE: background, lighting.

[If using Nano Banana Pro, add:]
- Style Image S1 (color grade): [description].
  TAKE: color palette, saturation, contrast, shadow/highlight tint.
  IGNORE: composition, subject.

CHARACTER BIBLE — [CHARACTER NAME]:
1. Hair: [exact description — color, length, style, parting, texture]
2. Eyes: [color, shape, distinguishing features]
3. Skin: [tone, hex if precise, marks like freckles or scars]
4. Build: [body type, height impression, proportions]
5. Face: [shape, cheekbones, chin, distinctive features]
6. Default outfit: [garment by garment, colors, materials]
7. Distinctive marks: [anything that must always be present]
8. [Additional identity anchors as needed]

NEW SCENE:
[CHARACTER NAME] is [ACTION] in [SCENE]. Expression: [EMOTION].

CAMERA:
[Shot type] at [focal length feel], [angle].
[Depth of field], [focus point].
Subject positioned [where in the frame].

LIGHTING:
[Time of day], [direction], [quality].
[Practical light sources if relevant].

PRESERVE (restated every scene):
- [CHARACTER NAME]'s exact face from Character Images 1–4.
- Hair color, style, and silhouette from references.
- Eye color and shape from references.
- Body type and proportions from references.
- Distinctive marks: [list them].
- Canonical style: [STYLE] — do not shift rendering approach.

CHANGE (what's new in this scene):
- Setting: [SCENE].
- Action: [ACTION].
- Expression: [EMOTION].
- [Outfit: same as references / new outfit described garment-by-garment].

CONSTRAINTS:
- Style commitment: [STYLE], matching the reference pack.
- If [CHARACTER NAME]'s face, hair color, eye color, body type, or distinctive marks
  differ from the Character Images, the output is INCORRECT.
- If the visual style shifts from [STYLE], the output is INCORRECT.
- Quality: "high"
```

---

## Sequence Management (Multi-Scene)

When generating multiple scenes with the same character:

1. **Always pass the original reference pack** — don't pass Scene 4's output as the reference for Scene 5. Drift compounds.
2. **Change one dimension per scene** — new setting, OR new outfit, OR new expression. Not all three.
3. **Re-anchor every ~10 scenes** — compare the latest output to the original references. If drift is visible, regenerate the anchor.
4. **If the outfit changes permanently**, regenerate a new full-body reference in the new outfit and add it to the reference pack.
5. **If the style drifts**, use Nano Banana Pro with a style reference image in Style slot 1 to re-lock the canonical look.

---

## Iteration Plan

1. "The hair color in this scene reads [wrong color] — restore to match Character Image 1's [correct color]."
2. "The face shape has narrowed compared to the references — restore facial proportions to match Character Image 2."
3. "The style has drifted toward photorealism — restore to the canonical [STYLE] from the reference pack."
4. "The distinctive [mark/scar/feature] is missing — it must be visible in every scene."

---

## Verification

- [ ] Character reference images passed in CHARACTER slots (not object slots).
- [ ] Character bible restated in the prompt (not just "same character").
- [ ] Style commitment matches the reference pack's canonical style.
- [ ] Only one major change from the previous scene.
- [ ] Failure condition stated for identity drift and style drift.
- [ ] Output face matches references (hair, eyes, marks, proportions).
- [ ] `quality="high"` set.
