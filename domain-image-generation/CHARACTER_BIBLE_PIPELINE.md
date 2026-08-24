---
title: "Character Bible Pipeline — Cross-Model Guide"
category: image-generation/workflow
description: "End-to-end workflow for building a character bible, generating a reference pack, and maintaining identity across scenes with any image model."
techniques:
  - ST-01
  - ST-02
  - SV-13
  - SV-15
difficulty: advanced
tags:
  - character-consistency
  - character-bible
  - reference-pack
  - cross-model
  - workflow
  - storybook
  - sequential-art
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/gpt-image-2/gptimage2_character_consistency_anchor.md
  - domain-image-generation/nano-banana/nanobana_multi_reference_character_scene.md
  - domain-image-generation/NANO_BANANA_GUIDE.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# Character Bible Pipeline — Cross-Model Guide

**Purpose:** A model-agnostic workflow for creating persistent characters in AI image generation. Covers building the character bible, generating the reference pack, managing identity across scenes, and recovering from drift. Works with gpt-image-2, Nano Banana 2/Pro, Midjourney, and Stable Diffusion.

**Use cases:** Children's book illustrations, comic/graphic novel sequences, brand mascot campaigns, episodic content, animated storyboards, game character look-dev.

---

## The 5-Step Pipeline

```
Step 1: Write the Character Bible (text)
    ↓
Step 2: Generate the Anchor Image (first render)
    ↓
Step 3: Build the Reference Pack (4-5 views)
    ↓
Step 4: Generate Scenes (use bible + refs every time)
    ↓
Step 5: Monitor and Re-Anchor (drift management)
```

---

## Step 1: Write the Character Bible

The character bible is a text document listing 5–10 **durable visual traits** that must persist across every image. These are facts about the character's appearance, not stylistic suggestions.

### Template

```
CHARACTER BIBLE — [CHARACTER NAME]

1. Hair: [color, length, style, parting, texture]
   Example: "Copper-red wavy hair, shoulder-length, center-parted, with a single curl
   that falls across the right temple."

2. Eyes: [color, shape, distinguishing features]
   Example: "Green eyes, almond-shaped, with visible gold flecks near the iris edge."

3. Skin: [tone, marks, freckles, scars]
   Example: "Warm medium-brown skin (#8B6914), scattered freckles across the nose bridge."

4. Build: [body type, height impression, proportions]
   Example: "Athletic, medium height, broad shoulders tapering to a narrow waist."

5. Face: [shape, cheekbones, chin, distinctive features]
   Example: "Oval face, high cheekbones, slightly pointed chin, wide smile."

6. Default outfit: [garment by garment, including colors and materials]
   Example: "Navy blue denim jacket (unbuttoned), white crew-neck t-shirt,
   dark gray chinos, worn brown leather boots."

7. Distinctive marks: [anything that must always be present]
   Example: "Small crescent-shaped scar above the left eyebrow.
   Silver ring on the right index finger."

8. Age impression: [apparent age range]
   Example: "Late twenties to early thirties."

9. Posture/bearing: [default body language]
   Example: "Slight forward lean, hands often in pockets, relaxed stance."

10. Canonical style: [the rendering style for this character]
    Example: "Watercolor children's book illustration, visible brushstrokes,
    warm color palette, soft edges."
```

### Bible Rules

- **Be specific, not aspirational.** "Brown hair" drifts. "Chestnut-brown (#6F4E37) straight hair, chin-length, blunt-cut" holds.
- **Use hex codes** for skin, hair, and eye color when precision matters.
- **Include at least one distinctive mark** — it's your drift detector. If the mark disappears, identity has drifted.
- **Lock the canonical style** — the rendering approach is part of the character's identity.
- **Don't describe personality** — the bible is visual-only. Personality emerges through action and expression in scene prompts.

---

## Step 2: Generate the Anchor Image

The anchor is the first "ground truth" render of the character. Every subsequent image is judged against it.

### Anchor Prompt Template

```
Generate a [CANONICAL STYLE] illustration of [CHARACTER NAME].

CHARACTER BIBLE:
[Paste the full 10-trait bible here.]

POSE: Standing neutral, arms relaxed at sides, facing the camera.
Expression: Calm, neutral — no strong emotion.
Background: Plain [white/light gray] — no environment.
Framing: Full-body, centered, with space around the figure.
Lighting: Soft, even, front-lit — no dramatic shadows.

CONSTRAINTS:
- This is the ANCHOR image — it defines [CHARACTER NAME]'s appearance.
- Every trait in the bible must be visible and accurate.
- The distinctive mark ([describe it]) must be clearly visible.
- Canonical style: [STYLE] — do not deviate.
- Quality: "high"
```

### Anchor Quality Check

Before proceeding, verify the anchor against the bible:
- [ ] Hair color, length, and style match the bible exactly.
- [ ] Eye color and shape match.
- [ ] Skin tone is accurate.
- [ ] Build and proportions match.
- [ ] Default outfit is correct (garment by garment).
- [ ] Distinctive mark(s) are visible.
- [ ] Canonical style is established.

**If the anchor doesn't match, regenerate.** Don't proceed with a flawed anchor — drift compounds.

---

## Step 3: Build the Reference Pack

Generate 3–5 additional views of the character from the anchor. The reference pack gives the model geometric information that a single front view can't provide.

### Required Views

| View | Purpose | Prompt Addition |
|------|---------|-----------------|
| Front (anchor) | Face, outfit, proportions | Already generated in Step 2 |
| Three-quarter | Facial depth, jaw, cheekbone | "Turned 45° to the [left/right], same expression" |
| Profile (side) | Nose, chin, ear, hair silhouette | "Turned 90° to the [left/right], looking forward" |
| Full-body (action) | Proportions in motion | "Walking forward, slight motion, full body visible" |
| Expression sheet | Key expressions | "4-panel grid: happy, surprised, thoughtful, determined" |

### Reference Pack Prompt

```
Using the attached anchor image of [CHARACTER NAME] as the identity reference:

Generate a [THREE-QUARTER / PROFILE / FULL-BODY] view of [CHARACTER NAME].

CHARACTER BIBLE:
[Paste the full bible — restated every time.]

TAKE from the anchor image: exact face, hair, skin, eye color, outfit, proportions,
distinctive marks.
CHANGE only: camera angle (now [describe the new angle]).

Background: Plain [white/light gray] — same as anchor.
Lighting: Same soft, even, front-lit as anchor.
Canonical style: [STYLE] — must match anchor.

CONSTRAINTS:
- If the face, hair color, eye color, or distinctive marks differ from the anchor,
  the output is INCORRECT.
- Do not redesign the outfit or proportions.
```

---

## Step 4: Generate Scenes

With the bible and reference pack established, place the character into scenes. The critical discipline: **restate the bible and pass the references every time.**

### Scene Prompt Template

```
[Pass reference pack images]

CHARACTER BIBLE — [CHARACTER NAME]:
[Paste the full 10-trait bible. Do not abbreviate. Do not say "same as before."]

NEW SCENE:
[CHARACTER NAME] is [ACTION] in [SETTING]. Expression: [EMOTION].

CAMERA: [Shot type, angle, focal length feel, depth of field.]
LIGHTING: [Time of day, direction, quality, practical sources.]

PRESERVE (restated every scene):
- [CHARACTER NAME]'s exact face from the reference pack.
- Hair: [restate from bible].
- Eyes: [restate from bible].
- Skin: [restate from bible].
- Build: [restate from bible].
- Distinctive marks: [restate from bible].
- Canonical style: [STYLE].

CHANGE (what's new):
- Setting: [SCENE].
- Action: [ACTION].
- Expression: [EMOTION].
- Outfit: [same as default / describe new outfit garment-by-garment].

CONSTRAINTS:
- Change ONE major dimension from the previous scene (new setting OR new outfit
  OR new expression — not all three).
- If [CHARACTER NAME]'s face, hair color, eye color, body type, or distinctive marks
  differ from the reference pack, the output is INCORRECT.
- If the canonical style shifts, the output is INCORRECT.
```

### The One-Change Rule

Each new scene should change **one major dimension** from the previous:
- New **setting** (same outfit, similar expression)
- New **outfit** (same setting, similar expression)
- New **expression/action** (same setting, same outfit)

Bundling all three changes at once maximizes drift risk.

---

## Step 5: Monitor and Re-Anchor

Identity drifts gradually. You won't notice it between consecutive images, but comparing Scene 15 to the anchor may reveal accumulated changes.

### Drift Detection

Check every 5–10 scenes:
1. **Side-by-side comparison** — put the latest output next to the original anchor.
2. **Distinctive mark check** — is the scar/ring/freckle pattern still present?
3. **Hair color check** — has it shifted hue? (Most common drift.)
4. **Style drift** — has the rendering approach changed subtly?

### Re-Anchoring Protocol

If drift is detected:
1. **Regenerate from the original references** — don't use recent outputs as references.
2. **Tighten the bible** — if a trait keeps drifting, add more specificity (hex codes, measurements, comparative descriptions).
3. **If the outfit changed permanently**, generate a new full-body reference in the new outfit and add it to the pack.
4. **If style drifted**, use a style reference image to re-lock the canonical look (Nano Banana Pro style slots are ideal for this).

### Re-Anchor Schedule

| Sequence Length | Re-Anchor Frequency |
|----------------|---------------------|
| 1–10 scenes | Check at scene 5 and 10 |
| 10–30 scenes | Every 10 scenes |
| 30+ scenes | Every 10 scenes + any time you notice something "off" |

---

## Model-Specific Implementation

### gpt-image-2
- **Reference method:** Pass anchor + reference pack as input images via `/v1/images/edits`
- **Slot allocation:** Up to 16 undifferentiated reference images
- **Strength:** Strong text understanding means verbose bibles work well
- **Weakness:** No role-separated slots — the model decides what to take from each reference
- **Prompt:** See `gpt-image-2/gptimage2_character_consistency_anchor.md`

### Nano Banana 2
- **Reference method:** 4 character slots + 10 object slots (role-separated)
- **Slot allocation:** Front in Char 1, three-quarter in Char 2, full-body in Char 3, profile in Char 4; scene environment in Obj 1-2
- **Strength:** Role separation means the model knows which reference controls identity vs. environment
- **Weakness:** Only 4 character slots — choose your most informative views
- **Prompt:** See `nano-banana/nanobana_multi_reference_character_scene.md`

### Nano Banana Pro
- **Reference method:** 5 character + 6 object + 3 style slots
- **Slot allocation:** Same as NB2 plus a 5th character slot for expression, and style slots for canonical look
- **Strength:** Style slots lock the rendering approach independently from identity
- **Weakness:** Fewer object slots for complex environments
- **Prompt:** See `nano-banana/nanobana_multi_reference_character_scene.md` (Pro variant)

### Midjourney
- **Reference method:** `--cref [URL]` for character reference, `--sref [URL]` for style
- **Slot allocation:** One character ref URL, one style ref URL, weight adjustable
- **Strength:** Very strong style consistency with `--sref`
- **Weakness:** Limited to URL-based references; less control over what the model takes from each reference
- **Bible adaptation:** Place key traits at the start of the prompt; Midjourney weighs early tokens more heavily

### Stable Diffusion (SDXL / SD3)
- **Reference method:** IP-Adapter, ControlNet, or LoRA fine-tuning
- **Slot allocation:** Depends on the pipeline configuration
- **Strength:** Full control via LoRA training on the character
- **Weakness:** Requires technical setup; not a prompt-only workflow
- **Bible adaptation:** For IP-Adapter, the bible informs the text prompt while the adapter handles visual consistency

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Bible too vague | Character looks different each time | Add hex codes, measurements, comparative descriptions |
| Bible not restated | Gradual drift after scene 5 | Copy-paste the full bible into every prompt — never abbreviate |
| Anchor was flawed | All subsequent images inherit the flaw | Regenerate the anchor before building more scenes |
| Using outputs as references | Drift compounds exponentially | Always reference the original pack, never recent outputs |
| Too many changes per scene | Identity shifts with the context | One-change rule: new setting OR outfit OR expression |
| Skipping re-anchor checks | Drift goes unnoticed for 20+ scenes | Schedule checks every 5-10 scenes |
| Style not locked | Rendering approach wanders | Include canonical style in the bible and restate it |

---

## Quick Checklist

Before generating any scene:
- [ ] Character bible written with 5–10 specific visual traits
- [ ] Anchor image generated and verified against bible
- [ ] Reference pack built (at least front + three-quarter + profile)
- [ ] Full bible pasted into the scene prompt (not abbreviated)
- [ ] Reference images passed in the correct slots for the model
- [ ] Only one major change from the previous scene
- [ ] Canonical style stated in the prompt
- [ ] Failure condition stated for identity drift
