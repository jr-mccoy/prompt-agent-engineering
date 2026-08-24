---
title: PACU Drains & Tubes Reference — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
updated: "2026-04-14"
tags:
  - pacu
  - image-generation
  - drains
  - tubes
---

# Image Meta-Prompt: PACU Drains & Tubes Quick-Reference Poster

> Safety reminder: Reference visual — drain and tube management defers to surgeon / facility protocol; output ranges and "normal" descriptions are illustrative only.

## What this meta-prompt produces

A **single-page landscape poster** showing common PACU drains/tubes side-by-side with: stylized line-drawing glyph · purpose · normal appearance · what to watch for · what to do. Designed for 11 × 8.5 inch wall print.

## INPUTS block

- **Devices to include (default 6):** {{JP drain, Hemovac, chest tube, Foley catheter, NG tube, epidural catheter}}
- **Canvas:** 11 × 8.5 inches landscape, 300 DPI.
- **Accent color:** teal #0f766e header; amber #b45309 for "watch-for" column stripe.

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) flat reference poster — NOT a photograph, NOT a stock medical render, NOT a UI.

SUBJECT: side-by-side reference of PACU drains and tubes with stylized glyph, purpose, normal, watch-for, and action.

PHYSICAL CONTEXT: 11x8.5 inch landscape poster for PACU wall. Flat line-drawing medical infographic. No photography.

CRITICAL OUTPUT RULES:
- One image. Landscape 11:8.5.
- Pure white #FFFFFF background. No gradient, no shadow, no photographic texture.
- Flat line-art glyphs — black outlines, minimal flat fills.
- High-contrast sans-serif text.
- No watermarks.

LAYOUT (enumerated, 6 rows x 5 columns):
- TITLE BAR top. Fill teal {{header accent}}. White bold 24pt: "PACU Drains & Tubes — Rapid Reference".
- COLUMN HEADERS row: "Device" | "Glyph" | "Purpose" | "Normal" | "Watch-For → Do".
- ROW 1 — JP (Jackson-Pratt) drain. Glyph: simple line drawing of a bulb reservoir with tubing. Purpose: closed-suction surgical drainage. Normal: serosanguinous, gradually decreasing. Watch-for: sudden bright red / sudden increase / no output when expected → notify surgeon.
- ROW 2 — Hemovac. Glyph: spring-compressed round reservoir with tubing. Purpose: closed-suction, higher volume than JP. Normal: serosanguinous, volume per post-op time. Watch-for: rapid filling / accordion fully expanded (loss of suction) → re-compress, notify surgeon.
- ROW 3 — Chest tube. Glyph: rigid tube to 3-chamber collection system with water-seal indicator. Purpose: air / fluid drainage from pleural space. Normal: tidaling in water-seal chamber with respiration; output per surgeon. Watch-for: continuous bubbling in water-seal (air leak) / sudden stop of tidaling / > facility threshold output → notify surgeon, keep system below chest.
- ROW 4 — Foley catheter. Glyph: catheter with balloon in bladder outline + collection bag. Purpose: urinary drainage / output monitoring. Normal: clear yellow, > {{per facility}} mL/kg/hr or per order. Watch-for: no output / gross hematuria / clots → bladder scan / irrigate per order / notify.
- ROW 5 — NG tube. Glyph: tube via nasopharynx into stomach outline + collection canister. Purpose: gastric decompression or feeding. Normal: green/brown gastric, pH per source. Watch-for: bright red / coffee-ground / displacement (coughing, voice change) → hold feeds, verify placement per protocol, notify.
- ROW 6 — Epidural catheter. Glyph: catheter taped at back with pump icon (simple rectangle labeled PUMP). Purpose: regional analgesia. Normal: catheter intact, dressing clean, block level per protocol, pain controlled. Watch-for: dressing wet / new motor block / hemodynamic change / catheter dislodgement → stop infusion per protocol, notify anesthesia.
- Alternating row fills: white and light gray #F3F4F6.
- "Watch-For → Do" column has amber {{watch accent}} left stripe 3pt on every row.
- FOOTER STRIP at bottom. 9pt gray. Text: "Educational aid — device management and output thresholds per surgeon / facility protocol. Not a substitute for orders."

TYPOGRAPHY: sans-serif throughout. Title 24pt bold. Headers 13pt bold. Body 10pt. Glyph labels 9pt.

COLOR PALETTE (strict):
- Background white.
- Text black.
- Title bar teal {{header}}.
- Row alt #F3F4F6.
- Watch stripe amber {{watch}}.
- Glyph fill: minimal — black outlines with optional light gray fill inside reservoirs.
- No other colors.

ALLOWED: clean line-drawing glyphs, labeled columns, accent stripes, sans-serif text.

FORBIDDEN: photographic devices, 3D medical render, skin tone rendering, drop shadow, gradient, bevel, glow, UI chrome, stock product photos, watermarks, branded device logos (Bard, etc.).

VALIDATION CHECKLIST:
1. One image, 11x8.5 landscape, 300 DPI.
2. Six rows in the order: JP, Hemovac, Chest Tube, Foley, NG, Epidural.
3. Glyph column shows flat line-drawings; no photographs; no branded logos.
4. Every Watch-For row has amber left stripe.
5. Footer caveat present.
6. No UI / 3D / gradient / shadow.
```

---

## Model-specific notes

**Nano Banana** — reliably produces line-drawing medical glyphs without branding. Specify "no brand name, generic stylized device".
**DALL·E 3** — occasionally labels glyphs with brand-like text ("BARD"); explicitly ban brand names in FORBIDDEN.
**Midjourney** — photorealistic by default; not ideal for this use case unless aggressively style-raw'd.

## Variants

- Orthopedic-heavy unit — swap NG for wound VAC.
- Thoracic-heavy unit — double chest-tube row (small-bore vs. large-bore).
