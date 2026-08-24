---
title: "Clinical Badge Buddy - Lab Value Normal Ranges"
category: medical-education
description: "Image generation prompt for creating printable clinician badge buddy reference cards for common laboratory value normal ranges (CBC, BMP/CMP, coags, ABG, cardiac markers)"
tags:
  - medical
  - clinician
  - badge-buddy
  - pocket-card
  - lab-values
  - laboratory
  - reference-card
  - image-generation
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - ./nursing_badge_buddy_critical_drips.md
  - ./clinical_badge_buddy_acls_codes.md
  - ./clinical_badge_buddy_med_dosing_template.md
  - ./clinical_badge_buddy_antibiogram_template.md
---

# Clinical Badge Buddy - Lab Value Normal Ranges

**Purpose:** Generate printable reference cards (badge buddies) for clinicians (nurses, residents, students, PAs, NPs) containing common laboratory value normal ranges grouped by panel (CBC, BMP/CMP, coags, ABG, cardiac markers) for quick bedside glance.

**Format:** Two-sided badge buddy, 4.5" x 2.75" landscape, lamination-ready

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) for the 8 print-ready techniques used in this prompt.
- [nursing_badge_buddy_critical_drips.md](./nursing_badge_buddy_critical_drips.md) for a sibling print-ready badge buddy.
- [clinical_badge_buddy_acls_codes.md](./clinical_badge_buddy_acls_codes.md), [clinical_badge_buddy_med_dosing_template.md](./clinical_badge_buddy_med_dosing_template.md), [clinical_badge_buddy_antibiogram_template.md](./clinical_badge_buddy_antibiogram_template.md)

> **⚠ CLINICAL SAFETY:** Reference (normal) ranges vary by laboratory, assay, analyzer, patient age, sex, and pregnancy status. **Reference ranges differ between institutions.** The example values below are conservative, commonly-published adult ranges provided to make the template usable — they are **NOT a clinical standard**. Replace every value with **your own laboratory's reported reference ranges** before printing. See the **Anti-Fabrication / Clinical Content** section. The image model must render only the values you supply; it must never invent, "round," or "correct" a lab range.

---

## Image Generation Prompt (Production-Ready)

```
TASK: Generate TWO SEPARATE FLAT PRINT ARTWORK IMAGES representing a clinician BADGE BUDDY insert worn behind a hospital ID badge.

IMPORTANT REAL-WORLD CONTEXT:
These are badge buddies.
They are worn BEHIND a clinician's ID badge.
They must be LANDSCAPE (wider than tall).
They are quick-glance laboratory reference cards.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT an illustration.

These images represent the literal ink-on-paper artwork sent directly to a printer.

CRITICAL CONTENT RULE:
Render ONLY the lab values, units, and ranges supplied in the BOX assignments below.
Do NOT invent, add, remove, round, or "correct" any number, unit, or range.
Treat every clinical value as fixed literal text to typeset exactly as written.

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY TWO IMAGES.
- Image 1 = BADGE BUDDY A (FRONT).
- Image 2 = BADGE BUDDY B (BACK).
- Each image must be a SINGLE flat rectangle.
- Orientation: LANDSCAPE (horizontal).
- NO rounded outer corners.
- NO drop shadows.
- NO gradients of any kind.
- NO lighting, gloss, bevel, or depth effects.
- NO background beyond the artwork edges.

If any gradient, shadow, or rounded corner appears, the output is incorrect.

================================================
PHYSICAL SIZE & CANVAS
================================================

Badge buddy size:
- 4.5 inches wide x 2.75 inches tall
- Landscape orientation
- Resolution: 1350 x 825 px at 300 DPI
- Edge-to-edge artwork (this IS the printed insert)

Background:
- Solid white (#FFFFFF) ONLY
- No texture
- No vignette
- No fade

================================================
GRID LAYOUT - THIS IS THE MOST IMPORTANT PART
================================================

EACH BADGE BUDDY MUST USE A STRICT GRID:

- EXACTLY 2 ROWS x 3 COLUMNS
- TOTAL OF 6 BOXES PER CARD
- ALL BOXES MUST BE:
  - Equal width
  - Equal height
  - Evenly spaced
  - Perfectly aligned
- One lab panel per box.
- No box may span multiple rows or columns.
- No empty boxes.
- No combined panels.

Boxes should read left-to-right, top-to-bottom.

================================================
DESIGN SYSTEM (STRICT)
================================================

ALL SHAPES:
- Rectangular only
- Sharp 90-degree corners only
- Solid fills only
- No transparency
- No gradients

BOXES:
- Light neutral fill (very light gray or white)
- Thin solid divider lines OR consistent spacing between boxes
- Optional thin top-edge color bar per panel for grouping
- NO rounded corners

ALLOWED (structured layouts):
- Aligned label/value columns inside a box
- Thin divider rules between rows of values
- Typographic hierarchy (panel name bold, values regular)

FORBIDDEN (software appearance):
- Excel-like cell grid with heavy borders
- Spreadsheet sheet tabs or headers
- Any software interface styling

TYPOGRAPHY ONLY - NO ICON GRAPHICS.
Allowed symbols (text only): less-than, greater-than, en-dash, slash

================================================
TYPOGRAPHY
================================================

- Panel name: Bold, 8-9 pt
- Lab label + range: Regular, 6.5-7.5 pt
- Minimum text size: 6.5 pt
- Clean clinical sans-serif
- High contrast black text on light fill

================================================
HEADER (BOTH CARDS)
================================================

Solid rectangle at top (not a "card top")

Fill: Solid teal #14746F
Text (white):
LAB VALUES
Quick Reference

Orientation label (plain text):
FRONT (card A)
BACK (card B)

================================================
FOOTER (BOTH CARDS)
================================================

Solid rectangle at bottom

Fill: Solid teal #14746F
Text (white, 6.5 pt):
Verify against your lab's reference ranges before clinical use

================================================
BADGE BUDDY A (FRONT)
================================================
Category focus: HEMATOLOGY + CHEMISTRY

2 ROWS x 3 COLUMNS - EXACT ASSIGNMENT
(EXAMPLE values shown — replace with your lab's verified ranges):

BOX 1:
CBC
WBC 4.5-11.0 K/uL
Hgb 12-16 (F) / 13.5-17.5 (M) g/dL
Hct 36-46 (F) / 41-53 (M) %
Plt 150-400 K/uL

BOX 2:
BMP - ELECTROLYTES
Na 135-145 mmol/L
K 3.5-5.0 mmol/L
Cl 98-107 mmol/L
CO2 22-29 mmol/L

BOX 3:
BMP - RENAL / GLUCOSE
BUN 7-20 mg/dL
Cr 0.6-1.3 mg/dL
Glucose 70-99 mg/dL (fasting)
Ca 8.5-10.5 mg/dL

BOX 4:
LFTs (CMP)
AST 10-40 U/L
ALT 7-56 U/L
Alk Phos 44-147 U/L
T. Bili 0.1-1.2 mg/dL

BOX 5:
PROTEINS / MAGNESIUM
Albumin 3.5-5.0 g/dL
T. Protein 6.0-8.3 g/dL
Mg 1.7-2.2 mg/dL
Phos 2.5-4.5 mg/dL

BOX 6:
COAGULATION
PT 11-13.5 sec
INR 0.8-1.1
aPTT 25-35 sec
Fibrinogen 200-400 mg/dL

================================================
BADGE BUDDY B (BACK)
================================================
Category focus: ABG + CARDIAC + ADDITIONAL

2 ROWS x 3 COLUMNS - EXACT ASSIGNMENT
(EXAMPLE values shown — replace with your lab's verified ranges):

BOX 1:
ABG
pH 7.35-7.45
PaCO2 35-45 mmHg
PaO2 80-100 mmHg
HCO3 22-26 mmol/L
SaO2 95-100 %

BOX 2:
CARDIAC MARKERS
Troponin: per local assay cutoff
BNP < 100 pg/mL
NT-proBNP age-dependent
(Use your assay's reference)

BOX 3:
LIPIDS
T. Chol < 200 mg/dL
LDL < 100 mg/dL
HDL > 40 (M) / > 50 (F) mg/dL
Trig < 150 mg/dL

BOX 4:
GLYCEMIC / THYROID
HbA1c < 5.7 %
TSH 0.4-4.0 mIU/L
Free T4 0.8-1.8 ng/dL

BOX 5:
ADDITIONAL CHEM
Lactate 0.5-2.2 mmol/L
Ammonia 15-45 ug/dL
Lipase 10-140 U/L
Amylase 30-110 U/L

BOX 6:
URINE / MISC
Urine SG 1.005-1.030
Urine pH 4.5-8.0
ESR 0-22 (M) / 0-29 (F) mm/hr
CRP < 1.0 mg/dL

================================================
FINAL VALIDATION CHECK
================================================

- Two images only
- Landscape orientation
- 2 rows x 3 columns per card
- Equal-sized boxes
- One lab panel per box
- All values typeset EXACTLY as supplied (no invented numbers)
- Flat print artwork
- Solid colors only
- No gradients
- No rounded corners
- No UI or mockup styling
- Optimized for instant badge-level glance
```

---

## Simplified Prompt (If Full Prompt Misbehaves)

If the AI still generates mockups or UI-style output:

```
Create TWO flat rectangular images for a clinician badge buddy (worn behind ID badge).

CRITICAL RULES:
- Landscape orientation (wider than tall)
- 4.5 x 2.75 inches each
- EXACTLY 2 rows x 3 columns grid
- One lab panel per box (6 total per image)
- Sharp corners only - NO rounded corners
- Solid colors only - NO gradients
- NO shadows, NO 3D effects
- This is FLAT PRINT ARTWORK, not a mockup
- Render the lab values EXACTLY as written; do NOT invent or change any number

IMAGE 1 - FRONT (Hematology/Chemistry):
Header: "LAB VALUES - Quick Reference - FRONT" (teal)
Box 1: CBC (WBC, Hgb, Hct, Plt)
Box 2: BMP Electrolytes (Na, K, Cl, CO2)
Box 3: BMP Renal/Glucose (BUN, Cr, Glucose, Ca)
Box 4: LFTs (AST, ALT, Alk Phos, T. Bili)
Box 5: Proteins/Mg (Albumin, T. Protein, Mg, Phos)
Box 6: Coags (PT, INR, aPTT, Fibrinogen)
Footer: "Verify against your lab's reference ranges before clinical use" (teal)

IMAGE 2 - BACK (ABG/Cardiac/Additional):
Header: "LAB VALUES - Quick Reference - BACK" (teal)
Box 1: ABG (pH, PaCO2, PaO2, HCO3, SaO2)
Box 2: Cardiac (Troponin per local cutoff, BNP, NT-proBNP)
Box 3: Lipids (Chol, LDL, HDL, Trig)
Box 4: Glycemic/Thyroid (HbA1c, TSH, Free T4)
Box 5: Additional Chem (Lactate, Ammonia, Lipase, Amylase)
Box 6: Urine/Misc (SG, pH, ESR, CRP)
Footer: "Verify against your lab's reference ranges before clinical use" (teal)

(Replace every example range with YOUR lab's verified values before printing.)
If output has rounded corners or gradients, it is WRONG.
```

---

## Why This Prompt Works

This prompt uses the 8 proven print-ready image generation techniques (see [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md)):

1. **Terminology Steering** - "flat print artwork" instead of "card" to avoid UI associations
2. **Grid Forcing** - Explicit 2x3 grid with equal-sized boxes
3. **Enumerated Slots** - BOX 1, BOX 2, etc. prevents content reorganization (and keeps each panel's values together)
4. **Constraint Redundancy** - "no gradients" and "render values exactly" appear at multiple levels
5. **Negative Space Control** - Bans backgrounds, shadows, mockup staging
6. **Physical Context** - "worn behind clinician's ID badge" anchors real-world usage
7. **Deliverables Locking** - "EXACTLY TWO IMAGES" with specific dimensions
8. **Validation Checklist** - Final self-audit block, including a no-invented-numbers check

---

## Anti-Fabrication / Clinical Content

**The image model RENDERS supplied clinical content. It does NOT generate medical facts.**

- The model must **not invent, guess, "improve," round, or correct** any laboratory value, unit, range, or panel grouping.
- All clinical content is **supplied by you** from your institution's verified reference ranges (the lab report, LIS reference table, or institutional protocol).
- The EXAMPLE values in this prompt are clearly labeled "EXAMPLE values shown — replace with your lab's verified ranges." They are conservative, commonly-published adult ranges intended only to make the template usable. **They are not a clinical standard and must be replaced.**
- Reference ranges legitimately differ by laboratory, assay/analyzer, age, sex, and pregnancy status. Troponin and natriuretic-peptide cutoffs in particular are assay-specific — leave them as "per local assay cutoff" unless you have your own value.
- If you remove the example values and leave placeholders, the model should typeset the placeholders verbatim (e.g., `[ANALYTE] [RANGE] [UNITS]`) and must not fill them in.
- Treat the output as a **typesetting deliverable only**. Clinical correctness is established by you before printing, not by the model.

---

## Print Specifications

- **Size:** 4.5" x 2.75" (landscape, fits behind CR80 badge)
- **Resolution:** 300 DPI minimum (1350 x 825 px)
- **Color Mode:** CMYK for print
- **Stock:** 14pt cardstock recommended
- **Finish:** Gloss lamination, 5-10mil
- **Hole punch:** Centered, 0.25" from top edge

---

## Model-Specific Notes

### gpt-image-2 (OpenAI flagship, recommended for text-heavy cards)
Best-in-class text rendering for dense numeric content like lab ranges.
- Set `quality="high"` — required for legible 6.5-7.5 pt numbers and units.
- The main prompt above maps cleanly onto its structure; keep the print constraints together as one block.
- `input_fidelity` is disabled in gpt-image-2 — do not pass it.
- Explicit grid enumeration and "if X appears, output is incorrect" language both work well.
- See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md) for full details.

### Nano Banana Pro (gemini-3-pro-image, recommended)
Near-perfect text rendering and exact-font control — strong for numeric reference cards.
- Name an exact font and weight (e.g., "Roboto, Bold for panel names; Roboto Regular for values").
- Emphasize these are **flat print artwork** (ink-on-paper), not a UI mockup — the Thinking process otherwise biases toward realism/3D.
- Use Markdown structure and ALL-CAPS `MUST`/`NEVER` for constraints; specify hex colors (`#14746F`).
- Put the no-fabrication rule in a system prompt for consistency across re-generations.
- See [NANO_BANANA_GUIDE.md](../NANO_BANANA_GUIDE.md).

### DALL-E 3 (legacy)
Add: `"Graphic design flat lay, reference card design, typography-focused, print material, flat 2D"`. Text density of lab panels often exceeds DALL-E 3's reliable rendering — prefer gpt-image-2 or Nano Banana Pro for accuracy.

### Midjourney (legacy)
```
flat print artwork, clinician badge buddy, laboratory reference values,
2x3 grid layout, landscape format, clinical typography,
--ar 16:10 --v 6 --style raw --s 25
--no badge lanyard clip holder 3d mockup photo gradient shadow rounded corners
```
Note: Midjourney does not reliably render exact numbers — verify every value or prefer a text-faithful model.

### Stable Diffusion (legacy)
Negative prompt: `"badge, lanyard, clip, holder, 3d, mockup, photo, gradient, shadow, rounded corners, depth, lighting, gloss, bevel, perspective"`. Not recommended for precise numeric text.

---

## Troubleshooting

### Problem: Still getting mockups/3D renders
**Add:** `"Top-down flat view only. This IS the card surface, not an image OF a card."`

### Problem: Rounded corners appearing
**Add:** `"Rounded corners = rendering error. All corners must be sharp 90-degree angles."`

### Problem: Numbers altered, dropped, or "corrected"
**Add:** `"Typeset every value EXACTLY as written. Do NOT change, round, reorder, or omit any number, unit, or range. If you cannot read a value, leave a blank line, do not invent one."` Then re-check the output against your source line-by-line.

### Problem: Content merged or reorganized
**Verify:** Each BOX assignment is explicit and numbered. Add: `"Do NOT combine panels. Do NOT reorganize. Follow BOX assignments exactly."`

### Problem: Gradients appearing
**Add:** `"SOLID colors ONLY. Any gradient in any element means the output is incorrect."`

### Problem: Only one image generated
**Add:** `"Generate EXACTLY 2 images. NOT 1. NOT 3. EXACTLY 2 separate images."`

---

## Verification Checklist (Before Printing)

- [ ] Every reference range cross-checked against **your laboratory's reported reference ranges / institutional protocol** before printing
- [ ] Units confirmed (conventional vs. SI as your lab reports them)
- [ ] Age/sex/pregnancy-specific ranges correct for your patient population
- [ ] Assay-specific values (troponin, BNP/NT-proBNP) match your local assay cutoffs
- [ ] All EXAMPLE values replaced with verified institutional values
- [ ] No value invented or altered by the image model (line-by-line comparison to source)
- [ ] Footer present: "Verify against your lab's reference ranges before clinical use"
- [ ] Two images, landscape, 2x3 grid, flat print artwork, no gradients/shadows/rounded corners
- [ ] Reviewed and approved by a qualified clinician/lab contact before distribution

---

*Updated: 2026-06-23 — Print-ready clinician badge buddy with anti-fabrication and clinical-accuracy verification.*
