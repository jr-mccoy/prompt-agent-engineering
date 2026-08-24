---
title: PACU Vital Signs Range Chart — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
  - midjourney
updated: "2026-04-14"
tags:
  - pacu
  - image-generation
  - vital-signs
  - reference-card
---

# Image Meta-Prompt: PACU Vital Signs Range Chart

> Safety reminder: Reference visual only — ranges and actions defer to facility protocol and provider orders.

## What this meta-prompt produces

A **3-column bedside reference chart**: Parameter | Acceptable Range | Action If Out-of-Range. Designed for 8.5 × 5.5 inch half-letter print, portrait.

## INPUTS block

- **Chart title:** {{e.g., "Phase 1 PACU Adult Vital Sign Guardrails"}}
- **Rows (each as triple):** {{Parameter; Acceptable Range; Action If Out-of-Range}}
  - Use textbook-sourced ranges or "per facility protocol".
  - Example: HR adult; 60–100 bpm per source; Trend + reassess; call anesthesia if sustained > threshold per protocol.
- **Surgery context (optional):** {{e.g., "post-general anesthesia, adult, non-cardiac"}}
- **Canvas:** 8.5 × 5.5 inches, portrait, 300 DPI.
- **Accent color:** {{e.g., teal #0f766e for header; amber #b45309 for the Action column's warning rows}}.

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) flat print reference chart — NOT a spreadsheet screenshot, NOT a dashboard, NOT a UI mockup.

SUBJECT: three-column vital-signs reference chart titled "{{Chart title}}" for post-anesthesia nurses.

PHYSICAL CONTEXT: 8.5x5.5 inch portrait half-letter print-ready artwork. Intended for lamination and clip to a badge lanyard or posting on a PACU wall. Flat print artwork. Not a web page. Not a software interface. No browser chrome.

CRITICAL OUTPUT RULES:
- One image. Portrait orientation. 8.5:5.5 aspect.
- Pure white #FFFFFF background. No gradient. No shadow. No photographic texture.
- Flat vector. No 3D. No bevel. No glow.
- Three columns, clearly delineated with thin 1pt black divider lines.
- All text crisp, sans-serif, high-contrast.
- No watermarks, no logos.

LAYOUT (enumerated):
- HEADER STRIP at top, full width. Fill: {{accent}}. White bold text 22pt. Text: "{{Chart title}}".
- COLUMN HEADERS row immediately below: "Parameter" | "Acceptable Range" | "Action If Out-of-Range". Bold 14pt black, white fill, 1pt black bottom border.
- DATA ROWS: alternating white and light gray #F3F4F6 fills for scan-ability. 12pt regular text.
- Every row in the ACTION column contains an explicit verb: "reassess", "apply O2", "notify anesthesia", "call MD", "document and recheck in N min". Use {{amber accent}} left-border stripe (3pt) for rows where action is "call / notify".
- FOOTER STRIP at bottom, full width. 9pt gray #6B7280. Text: "Educational aid — verify ranges and actions against current facility protocol and provider order. Not a substitute for clinical judgment."

ALLOWED: clean grid, aligned columns, sans-serif text, two flat accent colors.
FORBIDDEN: gradient fills, 3D, drop shadow, icons inside rows, emoji, photographic elements, spreadsheet chrome (no cell-selection highlights, no formula bar, no gridline header A/B/C/1/2/3), browser frames, mockup staging, paper texture.

TYPOGRAPHY: sans-serif throughout; title 22pt bold; column header 14pt bold; data 12pt regular.

COLOR PALETTE (strict):
- Background white #FFFFFF.
- Text black #111111.
- Header fill {{accent}}.
- Alternating row fill #F3F4F6.
- Left-border warning stripe {{amber accent}}.
- No other colors.

VALIDATION CHECKLIST (must pass before returning):
1. One image, 8.5x5.5 portrait, 300 DPI.
2. White background. No gradient, no shadow.
3. Three columns, thin black dividers.
4. Header strip at top with title; footer strip at bottom with caveat.
5. Every Action cell contains an action verb.
6. Warning rows have amber left stripe.
7. No UI elements, no spreadsheet chrome, no icons inside cells.

CONTENT ROWS (paste verbatim into the data rows, in order):
{{Parameter; Acceptable Range; Action If Out-of-Range — one triple per row}}
```

---

## Model-specific notes

**Nano Banana** — produces clean tabular artwork reliably. Keep strict column wording.
**DALL·E 3** — may round corners or add soft fills; repeat "flat, no gradient" in FORBIDDEN.
**Midjourney** — text placement is lossy. For final use, treat output as layout; re-type cells in a vector tool (Affinity, Illustrator, Figma).

## Variants

- Pediatric chart — change title and rows; footer caveat should add "pediatric ranges are weight-sensitive; verify per provider order".
- Post-spinal chart — add a Block Level row; see `pacu_dermatome_block_level_meta.md`.
