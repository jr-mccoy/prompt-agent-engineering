---
title: PACU Phase 1 Timeline Infographic — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
updated: "2026-04-14"
tags:
  - pacu
  - image-generation
  - timeline
  - phase-1
---

# Image Meta-Prompt: PACU Phase 1 Timeline Infographic

> Safety reminder: Typical timeline only — actual progression is patient-specific and governed by assessment, not the clock.

## What this meta-prompt produces

A **horizontal timeline** showing Phase 1 PACU progression from admission through discharge criteria, with milestone markers for airway, pain, nausea, and readiness. Designed for 17 × 11 inch tabloid print or 11 × 8.5 landscape letter.

## INPUTS block

- **Time span:** {{default: "Arrival → Phase 2 readiness (typical: 60–120 min; varies)"}}
- **Surgery context (optional):** {{general anesthesia adult / spinal adult / peds / etc.}}
- **Canvas:** 11 × 8.5 inches landscape, 300 DPI (or 17×11 tabloid).
- **Accent colors:** 3-zone color strip — teal #0f766e (stable), amber #b45309 (watch), red #b91c1c (escalate).

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) flat infographic — NOT a dashboard, NOT a UI timeline widget, NOT an animated sequence screenshot.

SUBJECT: horizontal Phase 1 PACU timeline with milestone markers and per-milestone assessment cues.

PHYSICAL CONTEXT: 11x8.5 inch landscape print-ready infographic for PACU wall or orientation handout. Flat print artwork. Not a software timeline.

CRITICAL OUTPUT RULES:
- One image. Landscape 11:8.5.
- Pure white #FFFFFF background. No gradient. No shadow.
- Flat vector. No 3D. No bevel. No glow.
- High-contrast sans-serif text.
- No watermarks.

LAYOUT (enumerated):
- TITLE BAR top. Fill teal {{stable accent}}. White bold 26pt: "PACU Phase 1 Timeline — Typical Adult Progression".
- TIMELINE AXIS horizontal, ~70% of canvas width, centered vertically. 6pt solid black line with left arrow "Arrival" and right arrow "Phase 2 Ready". Tick marks at 0 / 15 / 30 / 45 / 60 / 75 / 90 / 105 / 120 minutes. Tick labels 11pt.
- ZONE STRIP above the axis, 30px tall, divided into 3 colored bands aligned to the axis:
  - 0–30 min band: teal {{stable accent}}, label "Stabilization".
  - 30–60 min band: teal lighter shade or keep teal; label "Monitoring / Titration".
  - 60+ min band: amber {{watch accent}} if not yet meeting criteria, transitioning to teal at discharge-ready criteria; label "Toward Discharge".
- MILESTONE MARKERS as circles on the axis at key points, with callouts above or below:
  - "Airway stable" (early, ~5–15 min): maintains own airway, O2 as ordered, SpO2 per goal.
  - "Pain addressed" (~10–30 min): first pain score, first dose titrated, reassess.
  - "Nausea managed" (~10–45 min): PONV assessed, antiemetic given per order if needed, reassess.
  - "Mobility initiated (as appropriate)" (~30–60 min): regional block resolving or ambulation prep.
  - "Aldrete or facility criteria met" (~60–120 min): per facility protocol.
  - "Report given, transfer" (after criteria met).
- CALLOUT BOXES for each milestone: 2-line callout anchored to the circle by a 1pt line. Format: "Milestone name" (bold 11pt) / "Assessment cue" (10pt regular). Alternate callouts above and below the axis to prevent overlap.
- LEGEND bottom-left: 3 color swatches — Stable (teal), Watch (amber), Escalate (red). 10pt labels.
- FOOTER STRIP bottom. 9pt gray. Text: "Timeline is typical; patient course varies. Discharge criteria and assessment intervals per facility protocol. Educational aid only."

TYPOGRAPHY: sans-serif throughout. Title 26pt bold. Tick labels 11pt. Milestone bold 11pt. Cue regular 10pt. Legend 10pt. Footer 9pt gray.

COLOR PALETTE (strict):
- Background white.
- Text black.
- Axis black.
- Stable teal {{stable}}.
- Watch amber {{watch}}.
- Escalate red {{escalate}} — used only in legend swatch and any "if not meeting" callout text.
- No other colors.

ALLOWED: horizontal timeline, milestone circles, line callouts, three-band zone strip, legend, footer caveat.

FORBIDDEN: 3D timeline, animated trails, dashboard widgets, progress bar UI, icons inside callouts, emoji, photographic elements, drop shadow, gradient, bevel, glow, UI chrome, watermarks.

VALIDATION CHECKLIST:
1. One image, 11x8.5 landscape, 300 DPI.
2. Horizontal axis with tick labels 0 through ≥120 min.
3. Three-band zone strip aligned to axis.
4. At least 6 milestone circles with callouts (Airway / Pain / Nausea / Mobility / Criteria / Transfer).
5. Legend present with 3 swatches.
6. Footer caveat "timeline varies" present.
7. No UI / 3D / dashboard styling.
```

---

## Model-specific notes

**Nano Banana** — clean horizontal timelines render reliably. Keep callout count to ~6 to avoid overlap.
**DALL·E 3** — may compress axis and overlap callouts; consider tabloid 17×11 canvas for more headroom.
**Midjourney** — stylizes timelines; not ideal for this precise infographic.

## Variants

- Peds version — add weight-based caveat in footer and replace Aldrete with Modified Aldrete or Steward Score per facility.
- Ambulatory / same-day surgery version — add a second "Phase 2 → Home" horizontal below the first, stacked.
