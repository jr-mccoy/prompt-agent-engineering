---
title: PACU Orientee Shift Flow Map — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
updated: "2026-05-15"
tags:
  - pacu
  - image-generation
  - shift-flow
  - orientee
  - workflow
---

# Image Meta-Prompt: PACU Orientee Shift Flow Map

> Safety reminder: Flow map is a workflow visual — actual shift cadence varies by census, acuity, and surgical mix. Patient care decisions remain governed by facility protocols.

## What this meta-prompt produces

A **horizontal shift-flow diagram** showing the typical PACU shift cadence (huddle → handoff in → admit → recover → discharge → handoff out) with **orientee task callouts** organized by orientation week tier (Wk 1–2 / Wk 3–5 / Wk 6–N). Designed for 11 × 8.5 landscape print.

## INPUTS block

- **Orientee week tier focus:** {{Wk 1–2 | Wk 3–5 | Wk 6–N | all three tiers stacked}}
- **Facility shift-flow stages (if different from default):** {{paste if facility's flow has additional stages, e.g., pre-op holding handoff}}
- **Canvas:** 11 × 8.5 landscape, 300 DPI.
- **Color tokens:**
  - **Stage band:** teal #0f766e
  - **Wk 1–2 callouts:** light teal #14b8a6
  - **Wk 3–5 callouts:** amber #b45309
  - **Wk 6–N callouts:** dark teal #115e59

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) flat infographic — NOT a workflow software screenshot, NOT a Kanban board, NOT a process-mining UI.

SUBJECT: PACU shift flow diagram with orientee task callouts by orientation week tier.

PHYSICAL CONTEXT: 11x8.5 inch landscape print-ready workflow reference for PACU orientation room or break room. Flat print artwork.

CRITICAL OUTPUT RULES:
- One image. 11x8.5 landscape, 300 DPI.
- Pure white #FFFFFF background. No gradient. No shadow.
- Flat vector. No 3D. No bevel. No glow.
- High-contrast sans-serif text.
- No watermarks.

LAYOUT (enumerated):
- TITLE BAR top. Fill teal {{stage band}}. White bold 22pt: "PACU Shift Flow — Orientee Tasks by Week Tier".
- HORIZONTAL FLOW STRIP centered vertically: 6 stage boxes connected by 1pt arrows.
  - Box 1: "Pre-shift huddle"
  - Box 2: "Handoff in (OR → PACU)"
  - Box 3: "Admit phase"
  - Box 4: "Recover phase"
  - Box 5: "Discharge prep"
  - Box 6: "Handoff out"
- Each stage box: teal {{stage band}} fill, white text 11pt bold, ~110×60px.
- Arrows between boxes: black 2pt with arrowhead.
- THREE CALLOUT ROWS above and below the flow strip, one per week tier:
  - Above the flow strip: Wk 1–2 callouts (light teal background, 10pt dark text).
  - Below the flow strip: Wk 3–5 callouts (amber background, 10pt dark text).
  - Below that: Wk 6–N callouts (dark teal background, white 10pt text).
- Each callout: 1–2 sentences anchored to its stage box by a 1pt line. Maximum 1 callout per stage per tier (6 callouts per tier).
- LEGEND bottom-right: 3 color swatches with labels "Wk 1–2 (observation + co-task)", "Wk 3–5 (lead under shadow)", "Wk 6–N (independent under coverage)". 10pt.
- FOOTER STRIP bottom. 9pt gray. Text: "Typical shift flow. Cadence varies by census, acuity, and surgical mix. Educational aid only."

TYPOGRAPHY: sans-serif throughout. Title 22pt bold. Stage box labels 11pt bold. Callout text 10pt regular. Legend 10pt. Footer 9pt gray.

COLOR PALETTE (strict):
- Background white.
- Text black, dark slate, or white per fill contrast.
- Title bar teal, white text.
- Stage boxes teal, white text.
- Callout backgrounds: light teal (Wk 1–2), amber (Wk 3–5), dark teal (Wk 6–N).
- No other colors.

ALLOWED: horizontal flow with arrows, color-coded callouts, legend, footer caveat.

FORBIDDEN: 3D pipeline, BPMN swimlane software UI, dashboard, animation trails, drop shadow, gradient, bevel, glow, icons inside boxes, emoji, photographic elements, watermarks, hover popups.

VALIDATION CHECKLIST:
1. One image, 11x8.5 landscape, 300 DPI.
2. Six stage boxes connected by arrows.
3. Three callout tiers (Wk 1–2, Wk 3–5, Wk 6–N).
4. Maximum 1 callout per stage per tier (6 callouts per tier).
5. Legend with 3 color swatches.
6. Footer caveat present.
7. No 3D / dashboard styling.
```

---

## Model-specific notes

**Nano Banana** — flow strips with arrows render reliably; callouts above + below can collide if too long. Keep each callout to ≤ 2 sentences.
**DALL·E 3** — arrow direction sometimes inconsistent; check that all 5 arrows point left-to-right.
**Midjourney** — stylizes the flow; not recommended.

## Variants

- Ambulatory PACU variant: replace "Handoff out" with "Discharge to escort"; add Phase 2 stage.
- Single-tier focus: a 4-callout version for just one week tier (less crowded).
- Vertical / portrait variant for narrow walls.
