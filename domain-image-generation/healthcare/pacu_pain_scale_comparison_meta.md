---
title: PACU Pain Scale Comparison — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
  - midjourney
updated: "2026-04-14"
tags:
  - pacu
  - image-generation
  - pain-assessment
  - reference-card
---

# Image Meta-Prompt: PACU Pain Scale Comparison

> Safety reminder: Assessment reference only — scale selection and action thresholds per facility protocol and provider order.

## What this meta-prompt produces

A **four-row side-by-side comparison** of pain assessment tools commonly used in PACU: Numeric Rating Scale (NRS) · Wong-Baker FACES (generic) · FLACC (pediatric / nonverbal) · CPOT (critically ill / nonverbal). Includes "when to use", "how to score", and "reassess" columns.

## INPUTS block

- **Scales to include:** {{default: NRS, Wong-Baker FACES, FLACC, CPOT}}
- **Age / population focus:** {{all ages / adult only / peds only}}
- **Canvas:** 11 × 8.5 inches landscape, 300 DPI.
- **Accent colors:** header teal #0f766e; alert amber #b45309 for "reassess at..." column.

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) flat print reference poster — NOT a UI mockup, NOT a web page, NOT a clinical app screenshot.

SUBJECT: side-by-side pain assessment scale comparison for post-anesthesia nurses.

PHYSICAL CONTEXT: 11x8.5 inch landscape poster for PACU wall or lanyard-clip reference. Flat print artwork. No software interface.

CRITICAL OUTPUT RULES:
- One image. Landscape 11:8.5.
- Pure white #FFFFFF background. No gradient. No shadow.
- Flat vector. No 3D. No bevel. No glow.
- High-contrast black text on white. Accent color only in header and stripe elements.
- No watermarks.

LAYOUT (enumerated, 4 rows x 5 columns):
- TITLE BAR top, full width. Fill: teal {{header accent}}. White bold 28pt text: "PACU Pain Assessment — Scale Comparison".
- COLUMN HEADERS (just below title): "Scale" | "When to use" | "How to score" | "Typical range" | "Reassess after intervention". 14pt bold black, white fill, 1pt black bottom border.
- ROW 1 — NRS (Numeric Rating Scale 0–10). Scale column shows the number 0–10 horizontal number line with labels "0 no pain" left and "10 worst" right.
- ROW 2 — Wong-Baker FACES. Scale column shows 6 simple line-drawing face glyphs, 0/2/4/6/8/10 labels under each. Glyphs are line drawings, not cartoons, no color inside.
- ROW 3 — FLACC (Face, Legs, Activity, Cry, Consolability). Scale column lists the five categories stacked with 0/1/2 scoring key.
- ROW 4 — CPOT (Critical-Care Pain Observation Tool). Scale column lists the 4 indicators stacked with 0/1/2 scoring key.
- Alternating row fills: white and light gray #F3F4F6.
- The "Reassess after intervention" cell in every row uses amber {{alert accent}} left-border stripe 3pt.
- FOOTER STRIP bottom, 9pt gray. Text: "Educational aid — scale selection and thresholds per facility protocol. Not a substitute for clinical judgment."

TYPOGRAPHY: sans-serif throughout. Title 28pt bold. Column headers 14pt bold. Body 12pt regular. Scale labels 11pt.

COLOR PALETTE (strict):
- Background white.
- Text black #111111.
- Title bar fill teal {{header accent}}.
- Row fill alt #F3F4F6.
- Warning stripe amber {{alert accent}}.
- Face glyphs: black outline only, no color fill.
- No other colors.

ALLOWED: clean grid, simple line-drawing face glyphs, a horizontal number line, stacked category labels, sans-serif text, accent stripes.

FORBIDDEN: colored face cartoons, emoji, 3D faces, photographic faces, gradient fills, drop shadow, bevel, glow, UI chrome, browser frames, spreadsheet gridlines/headers, app-screenshot styling, stock clip-art, watermarks.

VALIDATION CHECKLIST:
1. One image, 11x8.5 landscape, 300 DPI.
2. White background, flat, no gradient.
3. Four rows (NRS, FACES, FLACC, CPOT) in that order.
4. Face glyphs are simple black-outline line drawings, no fill color.
5. Every row's Reassess cell has amber left stripe.
6. Footer caveat present.
7. No UI elements.

CONTENT (use these exact scale facts, confirm against cited sources — do not invent numeric cutoffs beyond the standard ranges noted):
- NRS: 0–10 self-report; verbal or visual analog; for adults who can self-report; reassess per facility interval after intervention.
- Wong-Baker FACES: self-report, typically age 3+ or non-English-speaking adults; 0/2/4/6/8/10; reassess per facility interval.
- FLACC: observer-scored; peds / nonverbal; score 0–10 total across 5 categories; reassess per facility interval.
- CPOT: observer-scored; critically ill / nonverbal adults; 4 indicators, 0/1/2 each, total 0–8; reassess per facility interval.
```

---

## Model-specific notes

**Nano Banana** — produces the cleanest face glyphs when told "simple single-line drawing, no fill". Avoid wording like "emoji" or "icon".
**DALL·E 3** — tends to color the faces. Re-emphasize "black outline only, no color fill" in FORBIDDEN.
**Midjourney** — face glyphs come out stylized. Use `--style raw` and `--stylize 0`.

## Variants

- Pediatric-only version — drop CPOT, add revised FLACC age ranges per Drain's or Core Curriculum peds chapter.
- Language-accessible version — keep NRS and FACES; call out language-independence of FACES.
