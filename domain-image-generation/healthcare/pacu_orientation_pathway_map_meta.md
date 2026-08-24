---
title: PACU Orientation Pathway Map — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
updated: "2026-05-15"
tags:
  - pacu
  - image-generation
  - orientation
  - pathway
  - timeline
---

# Image Meta-Prompt: PACU Orientation Pathway Map

> Safety reminder: Pathway map is a planning visual — actual orientation pace varies. Patient care decisions remain governed by facility orders.

## What this meta-prompt produces

A **horizontal orientation pathway timeline** from Week 0 to Week N, with theme bands, evaluation event markers, and end-of-week competency targets. Designed for 11 × 17 inch tabloid landscape or 8.5 × 14 legal landscape.

## INPUTS block

- **Orientation length:** {{N weeks}}
- **Per-week theme:** {{paste from `pacu_orientation_curriculum_designer.md` output}}
- **Evaluation events:** {{mid-orientation checkpoint week, end-of-phase sign-off week, final sign-off week}}
- **End-of-week competency target overall:** {{I / C / D / N per week}}
- **Canvas:** 17 × 11 tabloid landscape, 300 DPI.
- **Color tokens:**
  - **Stable theme weeks:** teal #0f766e
  - **Watch / transition weeks:** amber #b45309
  - **Evaluation event marker:** red #b91c1c (border only, not fill)

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) flat infographic — NOT a project Gantt chart, NOT a calendar UI, NOT a roadmap dashboard screenshot.

SUBJECT: horizontal PACU orientation pathway from Week 0 to Week N with theme bands, evaluation markers, and competency targets per week.

PHYSICAL CONTEXT: 17x11 tabloid landscape print-ready wall map for PACU educator office or break room. Flat print artwork.

CRITICAL OUTPUT RULES:
- One image. Tabloid 17x11 landscape.
- Pure white #FFFFFF background. No gradient. No shadow.
- Flat vector. No 3D. No bevel. No glow.
- High-contrast sans-serif text.
- No watermarks.

LAYOUT (enumerated):
- TITLE BAR top, full width. Fill teal {{stable accent}}. White bold 24pt: "PACU Phase 1 Orientation Pathway — {{N}} weeks".
- HORIZONTAL TIMELINE AXIS centered vertically, ~85% of canvas width. 6pt solid black line. Tick marks every week. Tick labels: "Wk 0", "Wk 1", ..., "Wk N" at 11pt below the axis.
- THEME BANDS above the axis, one band per week, height 60px:
  - Each band filled with the theme color (teal for stable weeks; amber for transition / high-load weeks per inputs).
  - White or dark text inside band, 10pt: the week's theme name in ≤ 5 words.
- COMPETENCY TARGET ROW below the axis: per-week target sign-off level (I / C / D / N) as a single bold letter in a circle. Circle filled per color token (teal for I, light teal for C, amber for D, gray for N).
- EVALUATION EVENT MARKERS: where evaluation events occur, place a red-bordered diamond marker on the axis with a callout above the band: 11pt label e.g. "Mid-orientation checkpoint", "End-of-phase sign-off", "Final sign-off".
- LEGEND bottom-left: 4 color swatches (I / C / D / N) + 1 diamond marker (Evaluation event). 10pt labels.
- FOOTER STRIP bottom. 9pt gray. Text: "Pathway is expected typical; actual orientation pace varies. Sign-off authority per facility orientation program. Educational aid only."

TYPOGRAPHY: sans-serif throughout. Title 24pt bold. Theme labels in bands 10pt regular. Tick labels 11pt. Competency circle tokens 12pt bold. Evaluation event labels 11pt. Legend 10pt. Footer 9pt gray.

COLOR PALETTE (strict):
- Background white.
- Text black or dark gray as appropriate for fill contrast.
- Title bar teal {{stable}}, white text.
- Theme bands: teal {{stable}} or amber {{watch}} per inputs.
- Competency circles: teal (I), light teal (C), amber (D), light gray (N).
- Evaluation markers: red {{escalate}} border, white fill — no other red on canvas.
- No other colors.

ALLOWED: horizontal axis, theme bands, competency circles, diamond evaluation markers, legend, footer caveat.

FORBIDDEN: 3D pathway, road or path metaphor with perspective, animation trails, Gantt bars with progress fills, UI chrome, calendar widgets, emoji, icons, drop shadow, gradient, bevel, glow, watermarks.

VALIDATION CHECKLIST:
1. One image, 17x11 tabloid landscape, 300 DPI.
2. Horizontal axis with Wk 0 → Wk N labels.
3. Theme band per week with ≤ 5-word label.
4. Competency target circle below each week.
5. Evaluation event markers diamond-bordered with callouts.
6. Legend with 4 competency tokens + 1 marker.
7. Footer caveat present.
8. No 3D / UI / dashboard styling.
```

---

## Model-specific notes

**Nano Banana** — long horizontal timelines render reliably on tabloid; for 12+ weeks consider extending to ledger 17x22 portrait flipped.
**DALL·E 3** — may compress with > 10 weeks; recommend tabloid 17x11.
**Midjourney** — stylizes pathways; not recommended.

## Variants

- New-grad pathway: identical template, longer pacing, fewer "compressed" theme bands.
- ICU-transfer pathway: shorter early-foundation bands, expanded mid-orientation PACU-distinctive bands.
- Vertical / portrait variant: rotate axis 90° for narrow-wall display.
