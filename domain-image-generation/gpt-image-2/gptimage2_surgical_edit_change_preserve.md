---
title: "GPT Image 2 — Surgical Edit (Change / Preserve)"
category: image-generation/edit
description: "Generalized surgical edit pattern for gpt-image-2: object removal, replacement, lighting change, weather change, background swap, text translation, outfit change."
techniques:
  - ST-01
  - ST-02
  - SV-13
  - SV-15
difficulty: intermediate
tags:
  - gpt-image-2
  - editing
  - image-edit
  - change-preserve
  - openai
updated: "2026-05-05"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# GPT Image 2 — Surgical Edit (Change / Preserve)

**Objective:** Apply a single, surgical edit to an input image while preserving everything else. The pattern is general: object removal, object replacement, lighting change, weather change, background swap, text translation, and outfit change all use the same template — only the change/preserve sentences differ.

**API parameters (recommended):**
- `model="gpt-image-2"`
- Endpoint: `/v1/images/edits`
- `image=open("input.png", "rb")`
- `size` matches the input or your target output
- `quality="high"` (recommended for identity-sensitive edits)
- `n=1` (do edits one at a time; iterate sequentially)

**Note:** gpt-image-2 has `input_fidelity` disabled. If you need maximum likeness lock through a large scene edit, fall back to `gpt-image-1.5` with `input_fidelity="high"`.

---

## Inputs

- `[INPUT DESCRIPTION]` — one sentence describing the input image
- `[EDIT TYPE]` — `remove` / `replace` / `lighting` / `weather` / `background` / `text-translation` / `outfit`
- `[CHANGE]` — single concrete change
- `[PRESERVE LIST]` — everything that must NOT change (use the table below)
- `[FAILURE CONDITION]` — what counts as a wrong output

---

## Edit Type → Preserve List Cheat Sheet

| Edit type | What MUST be preserved |
|---|---|
| Object removal | Surrounding pixels, lighting direction, surfaces under/around the object, color grade |
| Object replacement | Camera angle, scale, contact shadows, surrounding objects, lighting direction |
| Lighting change | Subject identity, geometry, object placement, camera angle, composition |
| Weather change | Subject identity, geometry, camera angle, object positions, composition |
| Background swap | Subject identity, subject's existing lighting (or restate new lighting), pose |
| Text translation | Everything except the text being translated |
| Outfit change (try-on) | Face, body shape, pose, hair, expression, proportions, hands, lighting, background |

---

## Constraints (Must / Must Not)

**Must:**
- Apply exactly **one** change per turn. Bundling produces drift.
- Restate the full preserve list every turn (don't rely on prior-turn memory).
- Use the word **ONLY** in the change sentence.
- State a failure condition the model can self-check against.

**Must Not:**
- Bundle multiple edits into one prompt.
- Pass `input_fidelity` (no-op on gpt-image-2; use gpt-image-1.5 if you need it).
- Use vague preserve language ("keep most things the same") — enumerate the preserve list.

---

## Production Prompt (Generalized)

```
INPUT IMAGE:
[INPUT DESCRIPTION].

CHANGE:
[CHANGE — exactly one concrete change, prefixed with "Replace ONLY..." / "Remove ONLY..." / "Change ONLY..." / "Swap ONLY..."].

PRESERVE:
Everything else stays exactly the same — specifically:
- [Item 1 from preserve list]
- [Item 2]
- [Item 3]
- [Item 4]
- [Camera angle, lighting direction, color grade, composition — always include these unless the change targets them]

REALISM / MATCH:
The edited region must match the existing scene's lighting direction, shadow softness, color grade, and perspective. Contact shadows should be naturally consistent.

FAILURE CONDITION:
[FAILURE CONDITION — e.g., "If the subject's face changes in any way, the edit is incorrect." / "If the camera angle shifts or the room scale changes, the edit is incorrect."]
```

---

## Worked Examples

### A. Object removal

```
INPUT IMAGE:
A photograph of a wooden dining table with a coffee mug, a stack of books, and a small potted plant.

CHANGE:
Remove ONLY the small potted plant.

PRESERVE:
Everything else stays exactly the same — the table's wood grain, the coffee mug's exact position and label, the stack of books in their exact arrangement, the camera angle, the natural light coming from the left, the soft shadow under the mug.

REALISM / MATCH:
Where the potted plant was, render the underlying table surface plausibly — same wood grain pattern continuation, same lighting falloff.

FAILURE CONDITION:
If any other object moves, changes size, or changes color, the edit is incorrect.
```

### B. Outfit change (virtual try-on)

```
INPUT IMAGE:
A studio portrait of a woman wearing a navy hoodie, three-quarter framing, soft window light from the left.

CHANGE:
Replace ONLY the navy hoodie with a cream cable-knit sweater.

PRESERVE:
Everything else stays exactly the same — her exact face, facial features, skin tone, hairstyle, expression, body shape, pose, hands, the camera angle, the framing, the window-light direction, the shadow falloff, the background.

REALISM / MATCH:
The cream cable-knit must drape on her body realistically, with shadows consistent with the window light from the left. Color grade must match the rest of the image.

FAILURE CONDITION:
If her face, skin tone, hairstyle, expression, body shape, pose, or hands change in any way, the edit is incorrect.
```

### C. Lighting change

```
INPUT IMAGE:
An exterior photograph of a small bookstore at midday under flat overcast light.

CHANGE:
Change ONLY the lighting from midday overcast to golden-hour late afternoon.

PRESERVE:
Everything else stays exactly the same — the bookstore's exact architecture, signage, any visible text on the windows, surrounding plants and street objects, camera angle, all object positions.

REALISM / MATCH:
Render warm low-angle sunlight from the [left/right]. Long soft shadows in the consistent direction. Color grade shifts to warm; saturation slightly higher; sky gradient from warm horizon to deeper blue zenith.

FAILURE CONDITION:
If any signage, architecture, or object position changes, the edit is incorrect.
```

### D. Text translation

```
INPUT IMAGE:
A storefront sign in English reading "OPEN — Fresh Bread Daily".

CHANGE:
Translate ONLY the sign's text to French. Render exactly: "OUVERT — Pain Frais Tous les Jours".

PRESERVE:
Everything else stays exactly the same — the sign's exact materials, colors, typography family, weight, layout, hanging hardware, lighting, surrounding storefront, camera angle.

REALISM / MATCH:
The translated text must use the same typography family, weight, color, and approximate optical size as the original. Rendered verbatim with no extra characters.

FAILURE CONDITION:
If any element other than the sign's text changes, the edit is incorrect. If the translated text is misspelled or has extra characters, the edit is incorrect.
```

---

## Iteration Plan

If the first edit drifts:
1. **Tighten the preserve list.** Re-run with explicit enumeration of whatever drifted.
2. **Reduce the change scope.** "Replace ONLY the front of the hoodie, not the sleeves" — sometimes splitting helps.
3. **Restate the failure condition** with the specific drift you observed.

---

## Verification

- [ ] Exactly one change in the CHANGE block, prefixed with ONLY.
- [ ] Preserve list enumerated (not "everything else").
- [ ] Camera angle, lighting direction, and color grade explicitly preserved (unless change targets them).
- [ ] Realism / match block specifies how the edit blends.
- [ ] Failure condition stated.
- [ ] No bundling of multiple edits.
- [ ] No `input_fidelity` parameter passed.
