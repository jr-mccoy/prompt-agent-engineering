---
title: "Children's Book Character Design Sheet (Turnaround)"
category: image-generation/childrens-illustration
description: "Create a character design / turnaround sheet for a recurring children's-book character: multiple views, expressions, and a locked design reference for the whole book."
techniques:
  - ST-01
  - ST-02
  - SV-13
  - SV-15
difficulty: advanced
tags:
  - childrens-illustration
  - character-design
  - turnaround
  - model-sheet
  - character-consistency
  - gpt-image-2
  - nano-banana
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/childrens-illustration/childrens_book_illustration_spread.md
  - domain-image-generation/childrens-illustration/childrens_consistent_style_series.md
  - domain-image-generation/CHARACTER_BIBLE_PIPELINE.md
  - domain-image-generation/gpt-image-2/gptimage2_character_consistency_anchor.md
  - domain-image-generation/nano-banana/nanobana_multi_reference_character_scene.md
---

# Children's Book Character Design Sheet (Turnaround)

**Objective:** Produce a single character **design sheet** (a.k.a. model sheet / turnaround) for a recurring picture-book character: front, three-quarter, side, and back views plus an expression strip, all at consistent scale against a plain background. This sheet becomes the **reference pack** every illustrator (human or model) uses to keep the character on-model across every spread.

> **Audience boundary:** This is for authors/illustrators building a book character — illustrating *for* children, not teaching them.

**Why model choice matters:** A turnaround is the canonical multi-view consistency task. **gpt-image-2** excels at one-pass multi-panel sheets and follows verbose design briefs well. **Nano Banana 2/Pro** is the better choice if you will keep regenerating views as a role-separated reference pack (4–5 character slots) and want a style slot to lock the render.

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `/v1/images/generations`, `quality="high"`, `size="1536x1024"`, `n=1` (or `n=4` to pick the cleanest sheet)
- Nano Banana path: `model="gemini-3-pro-image"` (Pro) or `"gemini-3.1-flash-image"` (NB2); generate each view, then store as the reference pack; `quality="high"`

---

## Inputs

- `[CHARACTER NAME]` — stable name used everywhere
- `[CHARACTER BIBLE]` — 5–10 durable visual traits (hair, eyes, skin, build, face, default outfit, distinctive marks, age impression, posture)
- `[SPECIES/TYPE]` — human child / animal / creature / object-with-a-face
- `[STYLE]` — canonical illustration style for the book
- `[VIEWS]` — which views to include (default: front, three-quarter, side, back)
- `[EXPRESSIONS]` — which expressions for the strip (e.g., happy, surprised, sad, curious)
- `[SCALE NOTE]` — height/proportion reference (e.g., "head-to-body ratio ~1:3.5 for a young child feel")

---

## Constraints (Must / Must Not)

**Must:**
- Render all views at **the same height and scale** along a shared baseline, like a real model sheet.
- Use a **plain neutral background** (no scene), even, soft, frontal lighting.
- Keep the **default outfit identical** across every view and expression.
- Include at least one **distinctive mark** in every view (the drift detector).
- Enumerate every identity feature concretely (no "cute hair" — give color, shape, parting).

**Must Not:**
- Add scene backgrounds, dramatic poses, or props (this is identity reference, not a story image).
- Let proportions or outfit change between views.
- Bundle expressions into the turnaround poses (keep the expression strip separate).
- Use a different render style for any panel than the canonical `[STYLE]`.

---

## Production Prompt — gpt-image-2 path (one-pass sheet)

```
SCENE:
A character DESIGN SHEET (turnaround / model sheet) for [CHARACTER NAME], a [SPECIES/TYPE] character in a children's picture book. Plain neutral background (#F2F0EB). No environment, no props.

LAYOUT:
A single sheet with two rows:
- TOP ROW — turnaround at identical scale on a shared baseline: [VIEWS — front view, three-quarter view, side/profile view, back view], left to right, evenly spaced, same height.
- BOTTOM ROW — expression strip: head-and-shoulders of [CHARACTER NAME] showing [EXPRESSIONS — e.g., happy, surprised, sad, curious], evenly spaced.

CHARACTER BIBLE (must be identical in every panel):
- Age impression: [age / young-child feel]
- Proportions: [SCALE NOTE — e.g., head-to-body ~1:3.5]
- Hair: [color, length, exact style, parting, texture]
- Eyes: [color, shape]
- Skin: [tone]
- Face: [shape, cheeks, chin]
- Default outfit: [garment by garment, colors, materials] — identical in every view
- Footwear: [shoes / barefoot]
- Distinctive marks: [freckles / patch / accessory] — visible in every view

USE CASE:
Canonical reference sheet for [CHARACTER NAME]. Every future spread in the book will be generated from this sheet. Identity must be locked.

CONSTRAINTS:
- Style: [STYLE] — canonical for the whole book; identical across all panels.
- Same height, same scale, shared baseline for all turnaround views.
- Plain neutral background, even soft frontal lighting, no shadows that hide identity features.
- Outfit, proportions, and distinctive marks identical across every panel.
- Age-appropriate, friendly design.
- Format: landscape, quality="high".

If any view differs in scale, outfit, proportions, or distinctive marks, or if the style varies between panels, the sheet is incorrect.
```

---

## Production Prompt — Nano Banana path (build the reference pack view by view)

```
TASK: Generate the [VIEW — front / three-quarter / side / back] view of [CHARACTER NAME] for a children's-book character reference pack.

[For views after the first, pass the front view as Char 1:]
REFERENCE (Char 1): the established front view of [CHARACTER NAME].
TAKE: face, hair, skin, eye color, outfit, proportions, distinctive marks.
CHANGE only: camera angle (now [VIEW]).
[Nano Banana Pro: Style 1 = the front view's render — TAKE the style, IGNORE composition.]

CHARACTER BIBLE — [CHARACTER NAME] (restated):
[full 5–10 trait bible, including SCALE NOTE]

VIEW SPEC:
- Single figure, full body, [VIEW], standing neutral on a shared baseline, same scale as the front view.
- Plain neutral background (#F2F0EB). Even, soft, frontal lighting. No props, no scene.

STYLE: [STYLE] — canonical, identical to the front view.

CONSTRAINTS:
- MUST: identical outfit, proportions, and distinctive marks to the front view; same scale.
- MUST NOT: add scene/props; change the style; alter proportions.
- Quality: "high".

If the outfit, proportions, distinctive marks, or style differ from the front view, the output is incorrect.
```

For the expression strip on Nano Banana, generate a 4-panel head-and-shoulders grid passing the front view as Char 1 and listing the `[EXPRESSIONS]`.

---

## Iteration Plan

1. "The side view's proportions don't match the front view's `[SCALE NOTE]` — restore identical height and head-to-body ratio."
2. "The outfit changed color in the back view — restore the exact default outfit from the front view."
3. "The distinctive `[mark]` is missing in the three-quarter view — it must appear in every view."
4. "Panel styles differ — unify all panels to the canonical `[STYLE]`."
5. "Expressions read too adult/intense — soften to friendly, age-appropriate `[EXPRESSIONS]`."

---

## Verification

- [ ] All turnaround views at identical scale on a shared baseline.
- [ ] Plain neutral background, even lighting, no scene/props.
- [ ] Default outfit identical across every view and the expression strip.
- [ ] Distinctive mark(s) visible in every view.
- [ ] Proportions match the `[SCALE NOTE]` consistently.
- [ ] Canonical `[STYLE]` identical across all panels.
- [ ] Sheet stored as the reusable reference pack (front + three-quarter + side at minimum) per CHARACTER_BIBLE_PIPELINE.md.
