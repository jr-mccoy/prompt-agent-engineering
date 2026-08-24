---
title: PACU Algorithm Flowchart — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
  - midjourney
  - stable-diffusion
updated: "2026-04-14"
tags:
  - pacu
  - image-generation
  - flowchart
  - algorithm
---

# Image Meta-Prompt: PACU Algorithm Flowchart

> Safety reminder: Visual decision support only — bedside clinical judgment and facility protocol override rendered content.

## What this meta-prompt produces

A ready-to-paste prompt that generates a **print-ready decision-tree flowchart** for a PACU scenario. Designed to pair with `skills/pacu-algorithm-flowchart-designer/` — paste its plain-text branch list into the INPUTS block and this meta-prompt produces the image prompt.

## INPUTS block (fill in before pasting to image generator)

- **Algorithm title:** {{e.g., "PACU Post-Op Desaturation"}}
- **Entry trigger (top box text):** {{e.g., "SpO2 < 92% in PACU adult"}}
- **Decision nodes (ordered, with Yes/No labels):** {{paste from algorithm skill output}}
- **Action nodes (with reassess interval):** {{paste from algorithm skill output}}
- **Escalation nodes (role + trigger):** {{paste from algorithm skill output}}
- **Canvas orientation:** landscape
- **Canvas size:** 11 × 8.5 inches (US letter landscape), 300 DPI
- **Accent color:** {{e.g., teal #0f766e for decisions; amber #b45309 for caution; red #b91c1c for escalate}}

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) image only. Single print-ready flat vector infographic — NOT a UI mockup, NOT a screenshot, NOT a dashboard.

SUBJECT: clinical decision-tree flowchart titled "{{Algorithm title}}" for post-anesthesia nurses.

PHYSICAL CONTEXT: this is an 11x8.5 inch landscape poster intended for print and for laminated bedside reference. It is a flat print artwork. It is NOT a web page, NOT a software interface, NOT a slide from a presentation deck. No browser chrome. No window frames. No mouse cursor. No UI buttons.

CRITICAL OUTPUT RULES (obey exactly):
- Output ONE image. Landscape orientation. 11:8.5 aspect ratio.
- Pure white (#FFFFFF) background. No gradient. No shadow. No paper texture. No photographic elements.
- Flat vector style. No 3D. No drop shadow. No glow. No embossing. No beveling.
- High-contrast black text on white. Accent color only in box fills and arrow heads.
- All text is crisp, sans-serif, legible at printed poster scale.
- No watermarks. No logos. No stock-image attributions.

LAYOUT (enumerated):
- BOX 1 (top center, large): the entry trigger. Text: "{{Entry trigger}}". Rounded rectangle. Fill: light gray #E5E7EB. Border: 2pt black.
- DIAMOND 1 (below BOX 1): first decision node. Diamond shape. Fill: {{decision accent}}. White text. Label the outgoing arrows "Yes" and "No".
- RECTANGLES for action nodes. Fill: white. Border: 2pt black. Always include the reassess interval text inside (e.g., "Apply O2 → reassess in 5 min").
- HEXAGONS for escalation nodes. Fill: {{escalate accent}}. White bold text. Include role (e.g., "Call anesthesia") and trigger ("because SpO2 < 88% x 2 min").
- Arrows: solid black, 2pt, with clear arrowheads. Label every arrow with its condition.
- Max tree depth: 4 levels. Do not exceed.

TYPOGRAPHY:
- Title at top: 36pt bold sans-serif.
- Node text: 14pt sans-serif; wrap to fit; max 3 lines per node.
- Arrow labels: 12pt sans-serif italic.

COLOR PALETTE (strict):
- Background: white #FFFFFF.
- Text: black #111111.
- Decision node: {{decision accent, e.g., #0f766e}}.
- Action node: white fill, black border.
- Escalation node: {{escalate accent, e.g., #b91c1c}}.
- No other colors. No gradients. No gradient fills. No photographic fills.

ALLOWED: clean geometric shapes (rectangle, rounded rectangle, diamond, hexagon, circle), straight lines with arrowheads, sans-serif typography, flat accent fills.

FORBIDDEN: gradient fills, drop shadows, 3D extrusion, icons inside nodes, emoji, photographic elements, stock imagery, watermarks, web UI chrome, browser frames, cursor, dashboard widgets, paper texture, grunge effects, handwriting styles.

FOOTER (small, bottom-right): "Educational aid — verify against facility protocol." 9pt gray #6B7280.

VALIDATION CHECKLIST (the generator must confirm before returning):
1. Exactly one image, 11x8.5 landscape, 300 DPI.
2. White background, no gradient, no shadow.
3. Title present at top as specified.
4. Entry trigger in BOX 1 exactly as provided.
5. All decision nodes as diamonds with Yes/No arrow labels.
6. All action nodes with reassess interval inside.
7. All escalation nodes as hexagons with role + trigger.
8. Tree depth ≤ 4.
9. No UI elements, no browser chrome, no drop shadow, no 3D, no icons inside nodes.
10. Footer caveat present.

CONTENT (fill these literal strings into the layout):
Entry trigger text: "{{Entry trigger}}"
Decision/action/escalation nodes (in order with their outgoing labels): {{paste plain-text branch list from pacu-algorithm-flowchart-designer}}
```

---

## Model-specific notes

**Nano Banana** — strong with flat vector and strict color palettes. Keep the VALIDATION CHECKLIST as the last block so it gates the output.

**DALL·E 3** — tends to add soft gradients. Repeat "flat, no gradient, no shadow" in the ALLOWED and FORBIDDEN blocks (already done). If it still drifts, regenerate with explicit "pure flat cel-shading, single solid fill per shape".

**Midjourney** — weaker with literal text placement. Use `--style raw` and lower `--stylize` (e.g., `--stylize 50`). Expect to iterate on node text; may need post-editing in a vector tool.

**Stable Diffusion (SDXL)** — text is unreliable. Treat output as structural scaffold only and overlay real text in a vector tool afterwards. Add `(flat vector, infographic:1.3)` to positive prompt; add `(gradient:1.3), (3d:1.3), (drop shadow:1.3), (ui:1.3)` to negative prompt.

## When to use a different meta-prompt

- Three-column lookup table → `pacu_vital_signs_range_chart_meta.md`
- Scale comparison → `pacu_pain_scale_comparison_meta.md`
- Timeline → `pacu_post_op_timeline_infographic_meta.md`
