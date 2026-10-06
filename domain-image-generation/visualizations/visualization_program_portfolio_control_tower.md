---
title: "Program Portfolio Control Tower Visualization Prompt"
category: program-management
description: "Generate a structured, no-UI visualization prompt optimized for program management decision workflows."
techniques:
  - SV-11
  - SV-12
  - SV-13
  - SV-14
  - SV-15
  - SV-16
  - SV-17
  - SV-18
tags:
  - visualization
  - no-ui
  - diagram
  - strategy
updated: "2026-10-06"
---

# Program Portfolio Control Tower Visualization Prompt

**Purpose:** Produce one clean visualization prompt for program management use, with strict anti-mockup constraints and print/screen-safe clarity.

**Required intake:** Portfolio scope, workstreams, milestones, status signals, and intervention thresholds.

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
- ZONE 1: Portfolio charter + horizon.
- ZONE 2: Workstream status grid.
- ZONE 3: Milestone timeline with dependencies.
- ZONE 4: Risk register summary.
- ZONE 5: Executive intervention queue.

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

## False-Positive Prevention

❌ **DON'T:**
- Let the model infer a workstream's RAG colour in ZONE 2 from its description — a green cell the program manager never set is fabricated assurance.
- Accept a ZONE 4 risk register showing probability × impact scores or risk counts that are not in the intake.
- Let the ZONE 5 queue include workstreams that have not breached the stated intervention thresholds, or omit ones that have.
- Draw ZONE 3 milestone markers with dates or dependency links the workstream plans do not contain.

✅ **DO:**
- Require a status signal per workstream in the intake; any workstream without one renders grey with "status not reported".
- Apply the intervention thresholds to each workstream's status signals yourself and confirm ZONE 5 lists exactly the ones that breach.
- Count the rows in the ZONE 2 grid against the workstreams named in the portfolio scope.
