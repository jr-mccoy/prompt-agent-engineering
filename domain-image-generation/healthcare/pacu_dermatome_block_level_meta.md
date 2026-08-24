---
title: Spinal / Epidural Dermatome Map — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
updated: "2026-04-14"
tags:
  - pacu
  - image-generation
  - dermatome
  - regional-anesthesia
---

# Image Meta-Prompt: Spinal / Epidural Dermatome Map with Block-Level Zones

> Safety reminder: Anatomical reference only — block level assessment requires bedside exam (pinprick / temperature / motor) per facility protocol.

## What this meta-prompt produces

A **front-view stylized torso dermatome map** with labeled dermatome lines (C2 through S5) plus a side bar that maps block level to procedure type (e.g., T4 = thoracic; T10 = lower abdomen / cesarean; L1 = lower extremity). Designed for 8.5 × 11 inch portrait print.

## INPUTS block

- **Title:** {{e.g., "Spinal Dermatome Reference — PACU Block Level"}}
- **View:** front and back side-by-side in one image (default), or front-only.
- **Canvas:** 8.5 × 11 inches portrait, 300 DPI.
- **Accent color:** teal #0f766e for highlight bands.

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) flat anatomical reference poster — NOT a photograph, NOT a 3D medical render, NOT a UI mockup.

SUBJECT: stylized human torso dermatome map (front and back views side-by-side) with labeled dermatome lines C2 through S5, plus a side-bar that maps block level (T4, T6, T10, L1) to common surgical zones.

PHYSICAL CONTEXT: 8.5x11 inch portrait print-ready poster for PACU wall reference. Flat line-drawing medical illustration style. Not a photograph. Not a realistic render.

CRITICAL OUTPUT RULES:
- One image. Portrait 8.5:11.
- Pure white #FFFFFF background. No gradient. No shadow. No photographic texture.
- Flat line-art illustration. Black outlines, light flat fills only.
- No muscle rendering, no shading, no highlights, no 3D, no anatomical photography.
- High-contrast sans-serif labels.
- No watermarks.

LAYOUT (enumerated):
- TITLE BAR top, full width. Fill: teal {{accent}}. White bold 24pt text: "{{Title}}".
- MAIN AREA (middle, ~60% of canvas): two figures side-by-side — left is front torso, right is back torso. Stylized line drawing. Neutral adult form. No sexual characteristics emphasized. No facial detail.
- DERMATOME LINES drawn as thin horizontal curves across the torso at C2, C3, C4, C5, C6, C7, C8, T1-T12, L1-L5, S1-S5. Label each line with its dermatome code (e.g., "T4") in 10pt black sans-serif, placed just outside the body outline on the left of the front figure and the right of the back figure.
- KEY BLOCK LEVELS highlighted with a 3pt teal {{accent}} horizontal band across the dermatome line: T4 (nipple line), T6 (xiphoid), T10 (umbilicus), L1 (inguinal). Label these in bold 12pt.
- SIDE BAR right column (~25% of canvas width): "Block level → typical procedure" table. 5 rows:
  - T4 — thoracic procedures; cardiac reference level
  - T6 — upper abdominal
  - T10 — lower abdominal / cesarean section
  - L1 — lower extremity / inguinal
  - L4 — perineal / saddle block
  Each row has a small teal color swatch matching the highlighted band.
- BOTTOM CAPTION: "Block level is assessed by pinprick / temperature / motor testing per facility protocol. Educational reference only."

TYPOGRAPHY: sans-serif throughout. Title 24pt bold. Dermatome labels 10pt. Key-level labels 12pt bold. Side-bar rows 11pt. Caption 9pt gray #6B7280.

COLOR PALETTE (strict):
- Background white.
- Body outlines and text black #111111.
- Highlight bands and side-bar swatches teal {{accent}}.
- Flat light gray #F3F4F6 inside body outlines (optional, light fill only to separate figure from background).
- No other colors.

ALLOWED: clean line-drawing anatomy, labeled dermatome lines, color-coded highlight bands for key levels, side-bar mapping, sans-serif labels.

FORBIDDEN: photographic anatomy, 3D medical render, muscle shading, skin tone rendering, facial detail, sexual detail, gradient fills, drop shadow, bevel, glow, UI chrome, app staging, stock-medical-illustration watermarks.

VALIDATION CHECKLIST:
1. One image, 8.5x11 portrait, 300 DPI.
2. White background, flat line-art style.
3. Two figures side-by-side: front and back.
4. All dermatome lines C2–S5 labeled.
5. Key levels T4, T6, T10, L1 highlighted with teal band AND bold label.
6. Side-bar "block level → typical procedure" table present with 5 rows.
7. Caption at bottom present.
8. No photographic / 3D / shaded elements.
```

---

## Model-specific notes

**Nano Banana** — reliably produces line-drawing anatomy; be strict about "no 3D, no shading".
**DALL·E 3** — occasionally returns a muscle-shaded figure; repeat "flat line drawing, no muscle detail".
**Midjourney** — stylizes torsos. For this use case prefer Nano Banana or DALL·E.

## Variants

- Pediatric — adjust body proportions in prompt ("pediatric stylized torso outline"); add caveat "pediatric dermatomes are compressed — use weight and developmental stage guidance".
- Epidural coverage version — show catheter insertion zone and typical spread pattern, per source.
