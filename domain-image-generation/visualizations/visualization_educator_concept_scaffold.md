---
title: "Educator Concept Scaffold Visualization Prompt"
category: educator
description: "Generate a structured, no-UI visualization prompt optimized for educator decision workflows."
tags:
  - visualization
  - no-ui
  - diagram
  - strategy
updated: "2026-04-21"
---

# Educator Concept Scaffold Visualization Prompt

**Purpose:** Produce one clean visualization prompt for educator use, with strict anti-mockup constraints and print/screen-safe clarity.

**Required intake:** Learner level, concept objective, misconceptions, vocabulary, and assessment expectation.

**Output requirement:** Exactly one flat visualization image prompt; no UI chrome, no device mockups, no staged photography.

---

## Intake Schema

Collect and confirm before generating:
1. Primary audience and decision owner.
2. Time horizon (historical snapshot, current-state, or future plan).
3. Must-include entities, metrics, or concepts.
4. Forbidden interpretations or visual metaphors.
5. Desired model target (Nano Banana / DALL·E / Midjourney / SDXL/Flux).

---

## Production Prompt Template

```text
TASK
Create EXACTLY ONE visualization as flat information artwork.

OUTPUT MEDIUM LOCK
- Output must be a single, static visualization image.
- Do not produce UI screens, app dashboards, slide mockups, posters in a room, or device renders.
- Straight-on, orthographic composition only.

REAL-WORLD CONTEXT ANCHOR
- This visual is reviewed in cross-functional planning meetings and exported into documentation.
- It must be readable when pasted into docs or printed on plain white paper.
- Prioritize information clarity over decorative style.

DELIVERABLE LOCK
- Exactly 1 image.
- Aspect ratio: 4:3 or 16:9 (choose based on content density).
- Solid light background (#FFFFFF or near-white only).
- Include title, legend, and source-note zone.

GRID FORCING + ENUMERATED SLOTS
- ZONE 1: Learning objective and grade band.
- ZONE 2: Core concept diagram (cause/effect or process chain).
- ZONE 3: Vocabulary bank with plain-language definitions.
- ZONE 4: Common misconception correction panel.
- ZONE 5: Quick-check prompts (3 items max).

CONSTRAINT REDUNDANCY (GLOBAL)
- No gradients.
- No shadows.
- No bevels.
- No glassmorphism.
- No gradients (repeat for reliability).
- No shadows (repeat for reliability).

NO-UI / NO-MOCKUP HARD CONSTRAINTS
- No browser chrome, no window frame, no widgets, no toggle switches.
- No phone, laptop, tablet, monitor, wall poster, or hand-holding scene.
- No photoreal desk setup, no perspective tilt, no depth-of-field camera effect.

NEGATIVE SPACE CONTROL
- Keep whitespace purposeful and rectangular.
- Avoid decorative background textures and ambient objects.
- No stickers, mascots, logos, watermarks, or branding unless explicitly requested.

ALLOWED VS FORBIDDEN
- Allowed: charts, arrows, tables, labeled icons, legend keys, annotation callouts.
- Forbidden: app UI kits, 3D interface cards, glossy infographics, ornamental effects.

MODEL-SPECIFIC TWEAKS
- Nano Banana / Nano Banana Pro: front-load hard constraints and repeat no-gradient/no-shadow rules twice.
- DALL·E / ChatGPT Images: specify explicit zones and typographic hierarchy to reduce layout drift.
- Midjourney: emphasize "flat diagram, orthographic, clean vector, no mockup" and add `--stylize 50` or lower.
- SDXL / Flux: use strong negative prompt equivalents for UI chrome, shadows, gradients, and photoreal staging.

FINAL VALIDATION CHECKLIST (must pass before finalizing)
- [ ] Exactly one visualization image generated.
- [ ] Output medium lock respected (not a UI screen/mockup/device).
- [ ] No gradients anywhere.
- [ ] No shadows anywhere.
- [ ] Physical context anchor reflected in content choices.
- [ ] Deliverable lock satisfied (single image + required zones).
- [ ] Labels, legend, and key relationships are readable.
```

## Notes

- Merge overlapping concepts when needed, but do not exceed five primary zones.
- Prefer concise labels and explicit directional flow arrows.
- If intake is ambiguous, request clarification before generation.
