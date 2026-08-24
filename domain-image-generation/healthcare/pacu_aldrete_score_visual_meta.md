---
title: PACU Aldrete / Modified Aldrete / PADSS Score Visual — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
updated: "2026-05-15"
tags:
  - pacu
  - image-generation
  - aldrete
  - padss
  - discharge-criteria
---

# Image Meta-Prompt: PACU Discharge Scoring Reference Card

> Safety reminder: Reference visual only. Actual discharge thresholds and protocols are facility-specific and per provider order. The visual leaves protocol-specific values as `{{per facility protocol}}` placeholders.

## What this meta-prompt produces

A **flat-print scoring reference card** showing the criteria categories of Aldrete, Modified Aldrete, and/or PADSS scoring systems. Designed for 8.5 × 5.5 portrait pocket card (front + back) or 11 × 8.5 portrait single-page reference.

## INPUTS block

- **Scoring system to render:** {{Aldrete | Modified Aldrete | PADSS | all three}}
- **Criteria categories (per scoring system — candidate confirms current standard against facility resource):** {{paste in the categories from the facility's reference}}
- **Format:** {{pocket card 8.5x5.5 portrait | single-page reference 11x8.5 portrait}}
- **Color tokens:**
  - **Heading band:** teal #0f766e
  - **Criteria category labels:** dark slate #1f2937
  - **Score-value cells:** light gray #f3f4f6
  - **Caveat text:** dark gray #4b5563

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) flat reference card — NOT a UI assessment tool, NOT a screenshot, NOT a clinical decision-support widget, NOT a checklist app.

SUBJECT: PACU discharge scoring reference — {{system(s)}} categories with score-value cells.

PHYSICAL CONTEXT: 8.5x5.5 portrait pocket card (or 11x8.5 portrait single-page reference). Flat print artwork suitable for printing and laminating.

CRITICAL OUTPUT RULES:
- One image, portrait, requested dimensions, 300 DPI.
- Pure white #FFFFFF background. No gradient. No shadow.
- Flat vector. No 3D. No bevel. No glow.
- High-contrast sans-serif text.
- No watermarks.
- All numeric thresholds shown as placeholders or as the user-supplied values — never invented.

LAYOUT (enumerated):
- TITLE BAND top, full width. Fill teal {{heading band}}. White bold 18pt: "{{Aldrete | Modified Aldrete | PADSS}} — PACU Reference".
- SUBTITLE 11pt dark slate: "Discharge scoring criteria — values per facility protocol."
- CRITERIA TABLE: rows = criterion categories (e.g., Activity, Respiration, Circulation, Consciousness, O2 Saturation for Aldrete; add Surgical Bleeding, Pain, PONV for PADSS as applicable). Use only the categories supplied in inputs.
- Each row has 4 columns:
  - Column 1 (~30%): Criterion category name, 11pt bold.
  - Column 2 (~25%): Score value "2" — descriptor cell — 10pt regular. Light gray background.
  - Column 3 (~25%): Score value "1" — descriptor cell — 10pt regular. Light gray background.
  - Column 4 (~20%): Score value "0" — descriptor cell — 10pt regular. Light gray background.
- All descriptor text must come from the user-supplied input. If a descriptor was not supplied, render the cell as "{{per facility protocol}}" in italics — never invent a descriptor.
- DISCHARGE THRESHOLD STRIP at the bottom of the criteria table: 30px tall, white background, dark text 11pt bold:
  - "Discharge readiness: {{per facility protocol — typically a sum threshold; do not invent}}".
- FOOTER STRIP bottom. 9pt gray. Text: "Reference aid only. Discharge decisions per facility protocol and provider order. Verify scoring tool version with facility."

TYPOGRAPHY: sans-serif throughout. Title 18pt bold. Subtitle 11pt. Criterion labels 11pt bold. Cell descriptors 10pt regular. Threshold strip 11pt bold. Footer 9pt gray.

COLOR PALETTE (strict):
- Background white.
- Text black or dark slate.
- Title band teal {{heading}}, white text.
- Cells light gray fill, dark text.
- No other colors.

ALLOWED: tabular layout, score-value columns, threshold strip, footer caveat.

FORBIDDEN: 3D card, dashboard styling, animated transitions, scoring widget UI, calculator UI, emoji, icons inside cells, photographic elements, drop shadow, gradient, bevel, glow, watermarks. NO invented numeric thresholds. NO invented descriptors.

VALIDATION CHECKLIST:
1. One image, requested dimensions, 300 DPI.
2. Title band with system name + reference framing.
3. Criteria table with 4 columns (Category / 2 / 1 / 0).
4. Every cell either contains user-supplied descriptor OR shows "{{per facility protocol}}" placeholder.
5. Discharge threshold strip shows "{{per facility protocol}}" if not user-supplied.
6. Footer caveat present.
7. No invented numbers anywhere.
```

---

## Model-specific notes

**Nano Banana** — tabular reference cards render cleanly; ensure descriptor cells aren't auto-completed with model-generated descriptors. Validate that any blank cell renders as a literal `{{per facility protocol}}` placeholder.
**DALL·E 3** — strong on the tabular format but at risk of inventing descriptors; prefer pasting descriptors explicitly in the inputs.
**Midjourney** — not recommended for tabular reference cards.

## Variants

- Pocket card front (Aldrete) + back (PADSS): two 8.5x5.5 images.
- Single-page 11x8.5 reference combining Aldrete + PADSS as stacked tables.
- Modified Aldrete only — single 8.5x5.5 with the modified criteria categories.

## Caution

This visual is intentionally **descriptor-empty** unless the candidate provides facility-validated descriptors. The toolkit does not invent threshold numbers or descriptors that could be mis-applied at the bedside.
