---
title: "GPT Image 2 — Character Consistency Anchor + Reuse"
category: image-generation/character
description: "Establish a character anchor in one image, then reuse the character across multiple scenes/poses/outfits without identity drift."
techniques:
  - ST-01
  - ST-02
  - SV-13
  - SV-15
difficulty: advanced
tags:
  - gpt-image-2
  - character-consistency
  - storybook
  - sequential-art
  - openai
updated: "2026-05-05"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-image-generation/gpt-image-2/gptimage2_multi_reference_composite.md
  - domain-image-generation/CHARACTER_BIBLE_PIPELINE.md
  - domain-image-generation/nano-banana/nanobana_multi_reference_character_scene.md
---

# GPT Image 2 — Character Consistency Anchor + Reuse

**Objective:** Create a stable character anchor in one image, then reuse that character across multiple subsequent scenes (different settings, poses, outfits, expressions) without identity drift. Use case: children's books, comic strips, brand mascots, episodic content, character look-dev.

**API parameters:**
- `model="gpt-image-2"`
- Anchor generation: `/v1/images/generations`, `quality="high"`, `n=1`
- Reuse / scene generation: `/v1/images/edits`, pass the anchor (and optionally additional refs), `quality="high"`, `n=1`

---

## Inputs

### Anchor inputs (Phase 1)
- `[CHARACTER NAME]` — give the character a stable name (used in every subsequent prompt)
- `[VISUAL DESIGN]` — concrete description: age, body type, hair color/style, eye color, skin tone, distinctive markings
- `[DEFAULT OUTFIT]` — if the character has a recurring outfit
- `[STYLE]` — illustration / painterly / photorealistic / 3D-render / pixel-art

### Reuse inputs (Phase 2, per scene)
- `[CHARACTER NAME]` — same as anchor
- `[SCENE]` — new setting
- `[ACTION]` — what the character is doing in this scene
- `[OUTFIT]` — same as anchor (default) or different (e.g., for sequence with costume change)
- `[EMOTION]` — facial expression for this scene

---

## Constraints (Must / Must Not)

**Must:**
- Phase 1 anchor: include a single, clean, full-body or three-quarter view of the character against a plain background.
- Phase 1 anchor: enumerate every distinctive identity feature (hair shape, eye color, distinctive marks).
- Phase 2 reuse: pass the anchor as a reference image (Image 1).
- Phase 2 reuse: restate the full preserve list every turn.
- Phase 2 reuse: change one major dimension at a time (scene, outfit, OR expression — not all three).

**Must Not:**
- Generate different scenes from text alone after the anchor is set — always pass the anchor reference.
- Allow the model to "redesign" the character to fit a new scene's style.
- Bundle multiple changes (new scene + new outfit + new expression) in one turn.
- Vary the character's name across prompts.

---

## Phase 1 — Anchor Production Prompt

```
SCENE:
A clean three-quarter view of [CHARACTER NAME] against a plain neutral [HEX e.g., #F2F0EB] background. No environmental context. This is a character anchor — purely for establishing identity.

SUBJECT:
[CHARACTER NAME], full body visible from head to feet, three-quarter angle (slightly turned, not fully front-on, not fully profile). Eyes facing the viewer, neutral expression.

KEY DETAILS — character design (this is what must persist across all future scenes):
- Age: [age range].
- Body type: [build and height impression].
- Skin: [skin tone, with hex if specifying].
- Hair: [color, length, exact style — e.g., "shoulder-length wavy auburn, side-parted on the left, slight cowlick at the crown"].
- Eyes: [color, shape — e.g., "warm hazel, almond-shaped"].
- Distinctive marks: [freckles / scar / birthmark / specific facial feature — be concrete].
- Default outfit: [DEFAULT OUTFIT — describe garment-by-garment with colors and materials].
- Footwear: [shoes / boots / barefoot].

USE CASE:
Character anchor for a [book / series / brand]. This image will be used as reference input for every future scene featuring [CHARACTER NAME]. Identity must be locked.

CONSTRAINTS:
- Style commitment: [STYLE]. Whatever style is used here will be the canonical style for [CHARACTER NAME] across all subsequent images.
- Background: plain [HEX]. No environmental detail. No props.
- Lighting: even, soft, frontal. No dramatic shadows that would obscure identity features.
- Forbidden: dramatic poses, scene props, environmental backgrounds, expressive emotion, dynamic action — this is the IDENTITY ANCHOR, not a story illustration.
- Format: portrait or square, [size], `quality="high"`.

If any identity feature listed under KEY DETAILS is rendered ambiguously or omitted, the anchor is incorrect.
```

---

## Phase 2 — Scene Reuse Production Prompt

```
INPUT:
Image 1 — Character anchor for [CHARACTER NAME]. PRESERVE every identity feature exactly as shown:
- The exact face: [restate hair color/style, eye color, distinctive marks here].
- Body type and proportions.
- The default outfit (if not changed in this scene): [restate].

NEW SCENE:
[CHARACTER NAME] is in [SCENE], doing [ACTION]. Expression: [EMOTION].

KEY DETAILS:
- Setting: [SCENE — concrete environmental detail, time of day, lighting].
- Pose: [pose / framing — full body, three-quarter, close-up].
- Outfit: [OUTFIT — same as anchor OR describe the new outfit garment-by-garment].
- Camera angle and distance: [eye-level, medium shot / low-angle close-up / etc.].

PRESERVE (restated every turn):
- [CHARACTER NAME]'s exact face from Image 1: [hair, eyes, marks].
- Body type and proportions from Image 1.
- The character's canonical style ([STYLE]) — do not shift to a new visual style for this scene.

CHANGE (this is what's new in this scene):
- Setting: now [SCENE].
- Pose / action: [ACTION].
- Expression: [EMOTION].
- Outfit: [same / new outfit description].

CONSTRAINTS:
- Style commitment: [STYLE], identical to the anchor.
- Forbidden: redesigning the character; shifting the visual style; ambiguating identity features; adding distinctive marks or features not in the anchor.
- Format: [size], `quality="high"`.

If [CHARACTER NAME]'s face, hair, eye color, body type, or distinctive marks differ from Image 1, the output is incorrect. If the visual style shifts (e.g., from illustration to photoreal), the output is incorrect.
```

---

## Sequence Workflow (Multi-Scene)

For a multi-scene project (storybook, comic, ad sequence):

1. **Generate the anchor** (Phase 1) once. Save it.
2. For **each scene**, run Phase 2 with the anchor as Image 1.
3. **Don't try to generate Scene 5 from Scene 4 by passing Scene 4** — drift compounds. Always pass the **original anchor**.
4. Optionally pass **multiple anchors** (front, three-quarter, profile) as Images 1, 2, 3 for richer identity coverage — see [`gptimage2_multi_reference_composite.md`](gptimage2_multi_reference_composite.md).
5. If you change the outfit permanently mid-sequence, **regenerate a new anchor** in the new outfit and use that anchor going forward.

---

## Iteration Plan

1. "The hair color in this scene reads more [ash blond] than the anchor's [auburn] — restore to match Image 1's hair exactly."
2. "The face shape has slimmed compared to the anchor — restore facial proportions to match Image 1."
3. "The visual style has shifted to more photoreal than the anchor's [illustrated] style — restore the canonical [STYLE]."

---

## Verification

### Anchor (Phase 1)
- [ ] Plain background, no scene context.
- [ ] Three-quarter view, full body or full upper body.
- [ ] Neutral expression, even lighting.
- [ ] Every identity feature concretely described (hair, eyes, marks, outfit).
- [ ] Style commitment stated as canonical.

### Scene Reuse (Phase 2)
- [ ] Anchor passed as Image 1.
- [ ] Preserve list restates identity features (not just "preserve identity").
- [ ] Style commitment matches anchor's.
- [ ] Failure condition stated for identity drift and style drift.
- [ ] Single major change per turn (scene OR outfit OR expression).
