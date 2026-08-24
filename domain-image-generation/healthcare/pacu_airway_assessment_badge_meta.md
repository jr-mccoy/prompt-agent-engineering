---
title: PACU Airway Assessment Badge Buddy — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
updated: "2026-04-14"
tags:
  - pacu
  - image-generation
  - airway
  - badge-buddy
---

# Image Meta-Prompt: Airway Rapid Assessment Badge Buddy

> Safety reminder: Rapid-assessment aid only — escalate per facility protocol; not a substitute for full airway evaluation and provider-directed management.

## What this meta-prompt produces

A **pocket-size badge buddy** (lanyard-clip card) listing the rapid PACU airway assessment landmarks and escalation triggers. Designed for double-sided print at 3.375 × 2.125 inches (credit-card / ID-badge size).

## INPUTS block

- **Side A title:** {{e.g., "PACU Airway — Look / Listen / Feel"}}
- **Side B title:** {{e.g., "When to Escalate"}}
- **Canvas per side:** 3.375 × 2.125 inches landscape, 600 DPI (small-format print benefits from higher DPI).
- **Accent color:** red #b91c1c for escalation elements; teal #0f766e for assessment elements.

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate two (2) images — a SIDE A and a SIDE B of a single badge-buddy card. Output them as two separate images of equal dimensions, labeled "Side A" and "Side B" in their corners (corner label 7pt gray, not intrusive).

SUBJECT: double-sided badge-buddy reference card for post-anesthesia airway assessment.

PHYSICAL CONTEXT: credit-card-size (3.375x2.125 inch) lanyard-clip ID badge insert. Printed flat on card stock, laminated, worn at the waist. Flat print artwork. NOT a digital card. NOT a UI card component.

CRITICAL OUTPUT RULES:
- Two images, each 3.375x2.125 landscape, 600 DPI.
- Pure white #FFFFFF background. No gradient. No shadow. No drop-shadow card effect (this is print, not UI).
- Flat vector. No 3D. No bevel. No glow.
- High information density — every millimeter earns its place.
- No watermarks. No logos.

SIDE A LAYOUT (enumerated, 2x3 grid):
- HEADER STRIP across top, 12% of card height. Fill teal {{assessment accent}}. White bold 11pt text: "{{Side A title}}".
- BOX 1 (top-left, 1/3 width x 40% height): "LOOK" — 3 bullets: airway patent? chest rise? cyanosis?
- BOX 2 (top-center): "LISTEN" — 3 bullets: breath sounds bilateral? stridor? gurgling?
- BOX 3 (top-right): "FEEL" — 2 bullets: air movement at mouth/nose? chest expansion equal?
- BOX 4 (bottom-left): "MONITORS" — 3 bullets: SpO2 trend? EtCO2 if present? RR?
- BOX 5 (bottom-center): "PATIENT" — 3 bullets: arousable? can follow command? protecting airway?
- BOX 6 (bottom-right): "ACT" — 3 bullets in teal text: reposition; O2; call.
- FOOTER STRIP 6% of card height at bottom. Fill light gray. 6pt text: "Educational aid — per facility protocol."

SIDE B LAYOUT (enumerated, 1-column stacked):
- HEADER STRIP across top. Fill red {{escalation accent}}. White bold 11pt text: "{{Side B title}}".
- ROW 1 (red left stripe 3pt): "SpO2 < threshold per protocol → O2, reposition, call anesthesia".
- ROW 2 (red left stripe 3pt): "Stridor / gurgling → suction, reposition, call anesthesia".
- ROW 3 (red left stripe 3pt): "Not responding / not protecting airway → rapid response + anesthesia".
- ROW 4 (red left stripe 3pt): "Sustained apnea → bag-mask, call anesthesia, activate code criteria per facility".
- ROW 5 (red left stripe 3pt): "New facial / neck swelling post thyroid / neck surgery → emergency airway pathway per facility".
- FOOTER STRIP same as Side A.

TYPOGRAPHY: sans-serif throughout. Header 11pt bold white. Box titles 9pt bold. Bullets 7pt. Footer 6pt.

COLOR PALETTE (strict):
- Background white.
- Text black.
- Assessment header teal {{assessment accent}}.
- Escalation header and stripes red {{escalation accent}}.
- Light gray #F3F4F6 for footer fill.
- No other colors.

ALLOWED: dense bullet lists, thin black box dividers, colored header strips, colored left stripes, tiny footer caveat.

FORBIDDEN: icons, emoji, photographic elements, gradient fills, drop shadow, bevel, glow, 3D, UI card mockup styling (no tilt, no glow behind card, no staged lifestyle composite), watermarks, stock imagery.

VALIDATION CHECKLIST (must pass before returning):
1. Two images, each 3.375x2.125 landscape, 600 DPI.
2. Side A: 2x3 grid exactly; header teal; 6 labeled boxes.
3. Side B: 5 stacked red-stripe rows; header red.
4. All text crisp and legible at printed badge size.
5. No UI / mockup / staging / 3D / gradient / drop shadow.
6. Footer caveat on both sides.
7. Corner "Side A" / "Side B" markers present, 7pt gray.
```

---

## Model-specific notes

**Nano Banana** — best choice for badge-buddy density. The explicit 2x3 grid on Side A is critical.
**DALL·E 3** — can struggle with small-font legibility. Consider generating at 2x dimensions and scaling down in print.
**Midjourney** — poor fit for dense text cards; use only for layout scaffold.

## Variants

- Peds version — adjust MONITORS row (EtCO2 + trend), add weight-based caveat.
- Post-thyroid airway card — add neck swelling / voice change / subcutaneous emphysema as a first-screen escalation.
