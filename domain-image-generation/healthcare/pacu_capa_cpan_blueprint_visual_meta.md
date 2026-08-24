---
title: PACU CAPA/CPAN Blueprint Domain Weight Visual — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
updated: "2026-05-15"
tags:
  - pacu
  - image-generation
  - capa
  - cpan
  - blueprint
---

# Image Meta-Prompt: CAPA/CPAN Blueprint Domain Weight Visual

> Safety reminder: Domain weights are user-pasted from the official ABPANC blueprint. This meta-prompt does not invent weights. The visual is a study-planning aid, not endorsed by ABPANC.

## What this meta-prompt produces

A **flat horizontal bar chart** (preferred) or ring chart (variant) showing the candidate's CAPA or CPAN blueprint domain weights. Designed for 8.5 × 5.5 portrait pocket card or 11 × 8.5 landscape study-plan companion.

## INPUTS block

- **Exam:** {{CAPA | CPAN}}
- **Domain list with weights (candidate pastes from ABPANC official source):** {{verbatim — we never fabricate}}
- **Format preference:** {{horizontal bar (default) | ring chart variant}}
- **Color tokens:**
  - **Bar fill:** teal #0f766e (gradient across bars is forbidden; use single solid teal)
  - **Domain labels:** dark slate #1f2937

---

## READY-TO-PASTE IMAGE PROMPT (horizontal bar chart)

```
Generate one (1) flat horizontal bar chart — NOT a dashboard widget, NOT a chart UI library screenshot, NOT a 3D rendering.

SUBJECT: {CAPA | CPAN} blueprint domain weights — flat horizontal bar chart.

PHYSICAL CONTEXT: 11x8.5 landscape print-ready study aid (or 8.5x5.5 pocket card variant). Flat print artwork.

CRITICAL OUTPUT RULES:
- One image, requested dimensions, 300 DPI.
- Pure white #FFFFFF background. No gradient. No shadow.
- Flat vector. No 3D. No bevel. No glow.
- High-contrast sans-serif text.
- No watermarks.
- Domain weights MUST come from user-pasted input exactly. NO invented weights.

LAYOUT (enumerated):
- TITLE BAR top, full width. Fill teal {{bar fill}}. White bold 20pt: "{CAPA | CPAN} Blueprint — Candidate-Provided Domain Weights".
- SUBTITLE 11pt dark slate: "Weights are user-pasted from the current ABPANC blueprint at study-plan time. Verify against current ABPANC source."
- HORIZONTAL BAR CHART, centered:
  - Y-axis (left): domain labels, 11pt regular, left-aligned. Each domain takes one row.
  - X-axis (bottom): percentage scale 0–{max user weight rounded up to nearest 10}, tick labels 10pt.
  - Bars: solid teal {{bar fill}} fill. Height ~25px. Length = weight percentage scaled to chart width.
  - Each bar has a 10pt label at its right end showing the exact weight percentage from user input ("18%", "22%" etc.).
- LEGEND not needed (single color).
- FOOTER STRIP bottom. 9pt gray. Text: "Weights from ABPANC blueprint as pasted by candidate on {{date}}. Verify against current source. Study aid only — not endorsed by ABPANC."

TYPOGRAPHY: sans-serif throughout. Title 20pt bold. Subtitle 11pt. Domain labels 11pt regular. Axis labels 10pt. Bar weight labels 10pt regular. Footer 9pt gray.

COLOR PALETTE (strict):
- Background white.
- Text black or dark slate.
- Title bar teal, white text.
- Bars teal {{bar fill}}, solid.
- Axes black 1pt.
- No other colors.

ALLOWED: horizontal bar chart, axis with tick labels, bar-end weight labels, footer caveat.

FORBIDDEN: 3D bars, gradient fills, chart library UI styling, animated transitions, drop shadow, bevel, glow, icons, emoji, photographic elements, watermarks. NO invented domain weights. NO comparisons to "average" or "national" benchmarks. NO pass-rate overlays.

VALIDATION CHECKLIST:
1. One image, requested dimensions, 300 DPI.
2. Title + subtitle present.
3. Each domain from user input is a single horizontal bar with weight label.
4. Weights match user input exactly.
5. Footer caveat present.
6. No 3D / dashboard / chart-library styling.
```

---

## Ring chart variant (alternative)

For a 5–7 domain blueprint where compact visual is preferred. Same constraints:

```
SUBJECT: flat ring chart showing {CAPA | CPAN} blueprint domain weights from user paste.

LAYOUT:
- TITLE BAR top: same as bar-chart variant.
- RING CHART centered: outer ring, ~60% of canvas. No 3D. Each segment colored from a 5–7-step teal-to-light-teal monochrome palette (no rainbow). Segment arc length proportional to weight.
- Inside ring: total "100%" label in 14pt.
- LEGEND on right: domain name + weight percentage, 11pt.
- FOOTER: same caveat.

FORBIDDEN: 3D ring, donut UI dashboard, exploded slices, drop shadow on segments, pull-out highlight, segment hover styling.
```

---

## Model-specific notes

**Nano Banana** — bar charts render reliably with single solid fill; verify bar-end labels match user input.
**DALL·E 3** — at risk of inventing weights if not all are pasted; if any are missing, paste them as zeros and adjust visual rather than letting model fill in.
**Midjourney** — not recommended for precise chart visualizations.

## Variants

- B&W print version: replace teal with crosshatch pattern for bars.
- Combined CAPA + CPAN: two charts stacked on 11x8.5 portrait for candidates dual-prepping.
- Weak-area-overlay version: secondary bars in amber showing candidate's practice-test accuracy per domain alongside the weight bars — only if candidate pasted both inputs.

## Caution

The toolkit explicitly does not maintain a baseline of ABPANC blueprint weights. The candidate is responsible for sourcing the current blueprint and pasting it accurately. If the candidate has not pasted the full domain list, the chart is incomplete, not approximated.
