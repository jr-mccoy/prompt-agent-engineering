---
title: "Nano Banana 2 — Storyboard Grid → Veo Keyframes"
category: image-generation/storyboard
description: "Generate a storyboard grid optimized for feeding keyframes into Google Veo for video generation."
techniques:
  - ST-01
  - ST-02
  - SV-12
  - SV-13
  - SV-17
difficulty: intermediate
tags:
  - nano-banana
  - nano-banana-2
  - storyboard
  - veo
  - keyframes
  - video
  - google
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/NANO_BANANA_GUIDE.md
  - domain-image-generation/VIDEO_GENERATION_GUIDE.md
  - domain-image-generation/gpt-image-2/gptimage2_character_consistency_anchor.md
---

# Nano Banana 2 — Storyboard Grid → Veo Keyframes

**Objective:** Generate a multi-panel storyboard grid where each panel is optimized as a keyframe for Google Veo video generation. The still carries static decisions (identity, scene, camera, lighting, color); the downstream Veo prompt carries motion decisions.

**Why Nano Banana 2:** 512px screening for cheap candidate generation (6–20 candidates before committing), speed for iteration, official Veo pipeline pairing, and extreme aspect ratio support (1:4, 4:1) for vertical/horizontal storyboards.

**API parameters:**
- `model="gemini-3.1-flash-image"`
- Screening pass: `size="512x512"`, `n=6`, `quality="standard"`
- Production pass: `size="2048x2048"` or `"3840x2160"`, `n=1`, `quality="high"`

---

## Inputs

- `[CONTENT TYPE]` — ad, short film, product demo, explainer, music video, social clip
- `[DURATION]` — total video duration in seconds
- `[PANEL COUNT]` — number of panels (typically 4–9)
- `[GRID LAYOUT]` — columns × rows (e.g., 3×2 for 6 panels)
- `[CHARACTER]` — character bible or description (restate identity features)
- `[LOCATION]` — setting description with time of day and lighting
- `[PANEL BEATS]` — shot type + action for each panel
- `[COLOR GRADE]` — the consistent look across all panels
- `[DOWNSTREAM USE]` — "Veo keyframes" or "Veo ingredients" or "Veo start/end frames"

---

## Constraints (Must / Must Not)

**Must:**
- Each panel must work as a standalone still — clear subject, readable silhouette, stable framing.
- Character identity must be identical across all panels (restate bible).
- One consistent color grade across all panels.
- Leave compositional room for intended motion in each panel.
- State which panels are start frames, end frames, or mid-sequence references for Veo.

**Must Not:**
- No motion blur in any panel — these are frozen moments.
- No busy/cluttered backgrounds that confuse video models.
- No text, captions, or panel numbers (these interfere with Veo input).
- No dramatic camera angles unless the video will hold that angle.
- Don't bundle all visual changes into one panel — distribute progression across beats.

---

## Screening Pass Prompt (512px, 6 candidates)

```
TASK: Create a [PANEL COUNT]-panel storyboard grid for a [DURATION]-second [CONTENT TYPE].

LAYOUT:
[GRID LAYOUT] (e.g., 3 columns × 2 rows), left-to-right, top-to-bottom reading order.
Thin neutral gutters (#E0E0E0, 2px). No text, captions, or panel numbers.

CHARACTER:
[CHARACTER NAME] appears in all panels — identical face, hair, outfit, proportions.
Identity features (must persist across panels):
- Hair: [exact description]
- Eyes: [color, shape]
- Build: [body type]
- Outfit: [garment by garment]
- Distinctive marks: [if any]

LOCATION:
[LOCATION — detailed setting, time of day, weather, key environmental features].

PANEL BEATS:
1) [SHOT TYPE] — [what happens, subject position, expression]
2) [SHOT TYPE] — [what happens]
3) [SHOT TYPE] — [what happens]
4) [SHOT TYPE] — [what happens]
5) [SHOT TYPE] — [what happens]
6) [SHOT TYPE / HERO FRAME] — [the money shot]

COLOR GRADE:
[Describe: warm/cool, saturation level, contrast, highlight/shadow tint].
This grade applies uniformly to ALL panels.

CONSTRAINTS:
- Same character identity in every panel — no redesign between panels
- No motion blur — frozen moments
- No busy backgrounds — clear subject silhouettes
- Room for motion in each panel (don't crop tight against the frame edge)
- No text or labels
- Quality: "standard" (screening pass)
```

---

## Production Pass Prompt (2K/4K, single best)

After selecting the best candidate from the screening pass, tighten the prompt:

```
TASK: Create a [PANEL COUNT]-panel storyboard grid for a [DURATION]-second [CONTENT TYPE].
This is the PRODUCTION version — quality="high", final resolution.

[Repeat the full prompt from the screening pass, but add:]

REFINEMENTS FROM SCREENING:
- [Specific adjustment from the winning candidate: "Panel 3 needs wider framing
  to allow the camera to push in during the video segment"]
- [Another adjustment: "The lighting in panel 5 doesn't match the color grade —
  correct to match panels 1-4"]

DOWNSTREAM USE:
These panels feed into Google Veo as keyframes:
- Panel 1 = start frame for Segment 1
- Panel [N] = end frame for the final segment
- Panels 2-[N-1] = mid-sequence identity and style references
Each panel must work as a standalone, unambiguous still.

CONSTRAINTS:
- [Repeat all constraints from screening pass]
- Quality: "high"
- Size: [2048x2048 or 3840x2160]
```

---

## Veo Motion Prompt Template (Downstream)

After generating the storyboard, feed selected panels into Veo with a motion-only prompt:

```
[Pass Panel 1 as start frame, Panel N as end frame]

Smoothly transition from the start frame to the end frame over [DURATION] seconds.

MOTION:
- Subject: [CHARACTER NAME] [describes the action — walking, turning, reaching].
- Camera: [camera movement — dolly, pan, tilt, static, handheld drift].
- Environment: [environmental motion — wind, rain, passing traffic, flickering lights].

PRESERVE:
- The exact character identity from both frames.
- The color grade, lighting direction, and visual style.
- The scene layout and background composition.

TIMING:
- [Beat 1]: [0-2 seconds] — [what happens].
- [Beat 2]: [2-4 seconds] — [what happens].
- [Beat 3]: [4-6 seconds] — [what happens].

CONSTRAINTS:
- No identity drift between frames.
- No style shift (maintain the look from the storyboard).
- No added elements not present in the keyframes.
```

---

## Iteration Plan

1. "Panel 3 has a cluttered background — simplify to a clean wall with one practical light source."
2. "Character's hair color shifted between panels 2 and 4 — restore to [exact color] matching panel 1."
3. "The color grade is inconsistent — panels 5-6 are warmer than 1-4. Normalize to the grade in panel 1."
4. "Panel 6 (hero frame) is cropped too tight — the camera needs room to pull back in the video segment."

---

## Verification

### Storyboard Grid
- [ ] All panels show the same character with consistent identity features.
- [ ] One consistent color grade across all panels.
- [ ] No motion blur in any panel.
- [ ] No text, captions, or panel numbers.
- [ ] Each panel has a readable subject silhouette against a clean background.
- [ ] Compositional room exists for intended motion in each panel.
- [ ] Panel beats follow the shot breakdown (wide → medium → close-up progression or specified order).

### Veo Readiness
- [ ] Start and end frames are clearly different poses/positions of the same character.
- [ ] Lighting direction is physically consistent between start and end frames.
- [ ] The intended motion path is clear from the frame compositions.
- [ ] No elements in the frames that would confuse the video model (extreme patterns, ambiguous depth).
