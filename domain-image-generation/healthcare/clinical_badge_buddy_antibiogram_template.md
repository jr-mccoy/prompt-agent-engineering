---
title: "Clinical Badge Buddy - Antibiotic Spectrum / Antibiogram (Template)"
category: medical-education
description: "Template-driven image generation prompt for creating printable clinician badge buddy antibiotic spectrum / coverage reference cards driven by the user's local antibiogram and stewardship guidance"
tags:
  - medical
  - clinician
  - badge-buddy
  - pocket-card
  - antibiotics
  - antibiogram
  - antimicrobial-stewardship
  - infectious-disease
  - template
  - image-generation
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - ./nursing_badge_buddy_critical_drips.md
  - ./clinical_badge_buddy_lab_values.md
  - ./clinical_badge_buddy_acls_codes.md
  - ./clinical_badge_buddy_med_dosing_template.md
---

# Clinical Badge Buddy - Antibiotic Spectrum / Antibiogram (Template)

**Purpose:** Generate a printable, **template-driven** antibiotic spectrum / coverage reference card (badge buddy) that **you fill in** from your **local antibiogram** and antimicrobial-stewardship guidance. It produces the *layout and typesetting* only — it ships with placeholders, not coverage claims — so each unit can render a card that reflects its own organisms, susceptibilities, and empiric-therapy recommendations.

**Format:** Two-sided badge buddy, 4.5" x 2.75" landscape, lamination-ready

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) for the 8 print-ready techniques used in this prompt.
- [nursing_badge_buddy_critical_drips.md](./nursing_badge_buddy_critical_drips.md) for a fully-populated example badge buddy.
- [clinical_badge_buddy_lab_values.md](./clinical_badge_buddy_lab_values.md), [clinical_badge_buddy_acls_codes.md](./clinical_badge_buddy_acls_codes.md), [clinical_badge_buddy_med_dosing_template.md](./clinical_badge_buddy_med_dosing_template.md)

> **⚠ CLINICAL SAFETY — THIS IS A BLANK TEMPLATE:** Antibiotic coverage and susceptibility are **local and time-sensitive.** Resistance patterns differ by institution, unit, and year, and empiric recommendations are set by your stewardship program. This card ships with **placeholders, not coverage claims.** Every organism, drug, coverage mark, and empiric recommendation must come from your **local antibiogram and stewardship guidance.** The image model must typeset your supplied content **exactly** — it must never assert, infer, "improve," or fill in any spectrum or susceptibility. See the **Anti-Fabrication / Clinical Content** section.

---

## How to Use This Template

Choose ONE of two layouts and populate it from your local antibiogram:

- **Layout 1 — Coverage matrix** (drug rows x organism columns), good for "what covers what."
- **Layout 2 — Drug-class summary boxes**, good for "key spectrum + one caution per drug class."

Replace placeholders:
- `[DRUG]` / `[CLASS]` — antibiotic name or class
- `[ORG1]`…`[ORGn]` — organism / category column headers (e.g., GPC, GNR, Pseudomonas, Anaerobes, MRSA, ESBL)
- coverage mark — use a neutral text symbol you define (e.g., `Y` = typically covers per local antibiogram, `N` = does not, `V` = variable/check). **Define your legend; the model must not assign marks itself.**
- `[EMPIRIC]` — your stewardship empiric recommendation for a syndrome
- `[NOTE]` — one key caution (renal dose, C. diff risk, allergy cross-reactivity)

Keep all content **exactly** as your source states it. Run the validation + verification checklists before printing.

---

## Image Generation Prompt (Production-Ready, Template)

```
TASK: Generate TWO SEPARATE FLAT PRINT ARTWORK IMAGES representing a clinician BADGE BUDDY insert worn behind a hospital ID badge.

IMPORTANT REAL-WORLD CONTEXT:
These are badge buddies.
They are worn BEHIND a clinician's ID badge.
They must be LANDSCAPE (wider than tall).
They are quick-glance antibiotic-coverage references built from a LOCAL antibiogram.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT an illustration.

These images represent the literal ink-on-paper artwork sent directly to a printer.

CRITICAL CONTENT RULE (READ FIRST):
This is a TEMPLATE. Fields may contain PLACEHOLDERS like [DRUG], [ORG1], [EMPIRIC], [NOTE].
Typeset EVERY field EXACTLY as written.
If a field is a placeholder, render the placeholder text verbatim (e.g., "[ORG1]").
Coverage marks (Y / N / V) are supplied by the user; do NOT add, change, infer, or "improve" any coverage mark.
Do NOT assert which drug covers which organism. You are typesetting only. You are NOT a clinical source.

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY TWO IMAGES.
- Image 1 = BADGE BUDDY A (FRONT - coverage matrix).
- Image 2 = BADGE BUDDY B (BACK - empiric recommendations + cautions).
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
LAYOUT - THIS IS THE MOST IMPORTANT PART
================================================

CARD A (FRONT) = COVERAGE MATRIX:
- A clean printed table (NOT a spreadsheet UI).
- LEFT COLUMN: drug/class rows (one per row).
- TOP ROW: organism/category column headers.
- CELLS: a single supplied coverage mark per cell (Y / N / V or your legend).
- ALLOWED: thin solid rules between rows/columns, bold header row, bold left column.
- FORBIDDEN: Excel-style heavy cell boxes, sheet tabs, software UI styling.
- Recommended size: up to 6 drug rows x up to 5 organism columns.

CARD B (BACK) = EMPIRIC + CAUTIONS:
- EXACTLY 2 ROWS x 3 COLUMNS = 6 BOXES.
- ALL BOXES equal width/height, evenly spaced, aligned.
- One topic per box (a syndrome's empiric rec, or a drug-class caution).
- No box spans rows/columns; no empty boxes; no combined topics.
- Boxes read left-to-right, top-to-bottom.

================================================
DESIGN SYSTEM (STRICT)
================================================

ALL SHAPES:
- Rectangular only
- Sharp 90-degree corners only
- Solid fills only
- No transparency
- No gradients

LEGEND (CARD A):
- Print the supplied legend exactly, e.g.:
  Y = covers (per local antibiogram)  N = no  V = variable/check
- Do NOT invent additional legend meanings.

TYPOGRAPHY ONLY - NO ICON GRAPHICS.
Allowed symbols (text only): the supplied coverage marks (e.g., Y / N / V), slash, en-dash

================================================
TYPOGRAPHY
================================================

- Header row / drug names: Bold, 7-9 pt
- Cells / details: Regular, 6.5-7.5 pt
- Minimum text size: 6.5 pt
- Clean clinical sans-serif
- High contrast black text on light fill

================================================
HEADER (BOTH CARDS)
================================================

Solid rectangle at top (not a "card top")

Fill: Solid forest green #1F5C3A
Text (white):
ANTIBIOTIC COVERAGE (LOCAL)
Quick Reference

Orientation label (plain text):
FRONT - COVERAGE MATRIX (card A)
BACK - EMPIRIC + CAUTIONS (card B)

================================================
FOOTER (BOTH CARDS)
================================================

Solid rectangle at bottom

Fill: Solid forest green #1F5C3A
Text (white, 6.5 pt):
Based on local antibiogram - verify against current stewardship guidance before use

================================================
BADGE BUDDY A (FRONT) - COVERAGE MATRIX
================================================
(TEMPLATE - replace placeholders with values from YOUR local antibiogram;
typeset placeholders and supplied coverage marks verbatim. Do NOT assign marks.)

COLUMN HEADERS (top row):
Drug \ Organism | [ORG1] | [ORG2] | [ORG3] | [ORG4] | [ORG5]

ROWS (one drug/class per row, supply a mark for each cell):
[DRUG/CLASS 1] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V]
[DRUG/CLASS 2] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V]
[DRUG/CLASS 3] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V]
[DRUG/CLASS 4] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V]
[DRUG/CLASS 5] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V]
[DRUG/CLASS 6] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V] | [Y/N/V]

LEGEND (print exactly as you define it):
Y = covers (per local antibiogram)  N = no  V = variable/check

================================================
BADGE BUDDY B (BACK) - EMPIRIC + CAUTIONS
================================================
Category focus: [SERVICE/UNIT empiric therapy + class cautions]

2 ROWS x 3 COLUMNS - EXACT ASSIGNMENT
(TEMPLATE - replace placeholders with YOUR stewardship guidance;
typeset placeholders verbatim if left blank):

BOX 1:
EMPIRIC: [SYNDROME 1]
First line: [EMPIRIC]
Alt / PCN allergy: [EMPIRIC]
Note: [NOTE]

BOX 2:
EMPIRIC: [SYNDROME 2]
First line: [EMPIRIC]
Alt / PCN allergy: [EMPIRIC]
Note: [NOTE]

BOX 3:
EMPIRIC: [SYNDROME 3]
First line: [EMPIRIC]
Alt / PCN allergy: [EMPIRIC]
Note: [NOTE]

BOX 4:
CLASS CAUTION: [CLASS]
[NOTE - e.g., renal dose / monitoring]
[NOTE - e.g., C. diff risk]

BOX 5:
CLASS CAUTION: [CLASS]
[NOTE - e.g., allergy cross-reactivity]
[NOTE - e.g., interaction]

BOX 6:
STEWARDSHIP REMINDERS
- De-escalate on cultures
- Source control
- Reassess at 48-72h
- [LOCAL NOTE]

================================================
FINAL VALIDATION CHECK
================================================

- Two images only
- Landscape orientation
- Card A = coverage matrix (printed table, not spreadsheet UI)
- Card B = 2 rows x 3 columns, equal-sized boxes, one topic per box
- Every field + coverage mark typeset EXACTLY as supplied; placeholders verbatim
- NO coverage mark added, changed, or inferred by the model
- Flat print artwork
- Solid colors only
- No gradients
- No rounded corners
- No UI or mockup styling
- Optimized for instant badge-level glance
```

---

## Worked Example (EXAMPLE — REPLACE WITH YOUR INSTITUTION'S VERIFIED VALUES)

Illustrative structure only — coverage marks below are placeholders to show layout, **NOT** real susceptibility data. Populate from your local antibiogram:

```
Drug \ Organism | GPC | MSSA | Pseudomonas | Anaerobes | GNR     <- EXAMPLE headers
Cefazolin       | [Y] | [Y]  | [N]         | [N]       | [V]     <- marks = YOU supply from antibiogram
Pip-tazo        | [Y] | [Y]  | [Y]         | [Y]       | [Y]     <- EXAMPLE structure, verify locally
Vancomycin      | [Y] | [Y]  | [N]         | [N]       | [N]     <- EXAMPLE structure, verify locally
```

Do not treat these marks as accurate — they exist only to demonstrate the grid. Replace every cell with your local antibiogram value.

---

## Simplified Prompt (If Full Prompt Misbehaves)

If the AI still generates mockups or UI-style output:

```
Create TWO flat rectangular images for a clinician antibiotic-coverage badge buddy (worn behind ID badge),
built from a LOCAL antibiogram.

CRITICAL RULES:
- Landscape orientation (wider than tall)
- 4.5 x 2.75 inches each
- Sharp corners only - NO rounded corners
- Solid colors only - NO gradients
- NO shadows, NO 3D effects
- This is FLAT PRINT ARTWORK, not a mockup
- This is a TEMPLATE: typeset every field and coverage mark EXACTLY as written.
  Render placeholders verbatim. Do NOT add, change, or infer any coverage mark or spectrum.

IMAGE 1 - FRONT (coverage matrix):
Header: "ANTIBIOTIC COVERAGE (LOCAL) - FRONT" (forest green)
Printed table: drug rows x organism columns, one supplied mark (Y/N/V) per cell, with legend.
Footer: "Based on local antibiogram - verify against current stewardship guidance before use" (forest green)

IMAGE 2 - BACK (empiric + cautions):
Header: "ANTIBIOTIC COVERAGE (LOCAL) - BACK" (forest green)
2x3 grid: Boxes 1-3 = empiric therapy by syndrome ([EMPIRIC]); Boxes 4-5 = class cautions ([NOTE]);
Box 6 = stewardship reminders.
Footer: "Based on local antibiogram - verify against current stewardship guidance before use" (forest green)

If output has rounded corners or gradients, it is WRONG.
```

---

## Why This Prompt Works

This prompt uses the 8 proven print-ready image generation techniques (see [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md)):

1. **Terminology Steering** - "flat print artwork" + "printed table, not spreadsheet UI" avoids software-screenshot drift
2. **Grid Forcing** - Card A locks the matrix dimensions; Card B locks a 2x3 grid
3. **Enumerated Slots** - Explicit rows/columns and BOX assignments prevent reorganization
4. **Constraint Redundancy** - "no gradients" and "do not infer coverage marks" appear at multiple levels
5. **Negative Space Control** - Bans backgrounds, shadows, mockup staging
6. **Physical Context** - "worn behind clinician's ID badge," "built from a local antibiogram" anchors usage
7. **Deliverables Locking** - "EXACTLY TWO IMAGES" with specific dimensions and distinct front/back roles
8. **Validation Checklist** - Final self-audit block, including a no-inferred-coverage-marks check

---

## Anti-Fabrication / Clinical Content

**The image model RENDERS supplied clinical content. It does NOT generate medical facts.**

- This is a **blank template**. It ships with placeholders (`[DRUG]`, `[ORG1]`, `[EMPIRIC]`, `[NOTE]`, coverage marks) and **no coverage claims**.
- The model must **typeset placeholders and supplied coverage marks verbatim** and must **never add, change, infer, "improve," or assert** which drug covers which organism, or what the empiric choice should be.
- All clinical content is **supplied by you** from your **local antibiogram** and antimicrobial-stewardship guidance. Susceptibility is local, unit-specific, and changes over time; published "textbook spectrum" is not a substitute for your antibiogram.
- The Worked Example marks are labeled "EXAMPLE — REPLACE WITH YOUR INSTITUTION'S VERIFIED VALUES" and exist only to demonstrate the grid. **They are not accurate susceptibility data.**
- Empiric recommendations, allergy cross-reactivity notes, and renal dosing are stewardship/pharmacy decisions — supply them from your verified source, do not let the model generate them.
- Treat the output as a **typesetting deliverable only**. Clinical correctness is established by you (with stewardship/ID/pharmacy input) before printing, not by the model.

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
Best-in-class text rendering — handles a small coverage matrix and faithfully reproduces bracketed placeholders/marks.
- Set `quality="high"` — required for legible matrix cells and 6.5-7.5 pt text.
- The main prompt above maps cleanly onto its structure; keep the print constraints together as one block.
- `input_fidelity` is disabled in gpt-image-2 — do not pass it.
- Explicit grid enumeration and "if X appears, output is incorrect" language both work well.
- See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md) for full details.

### Nano Banana Pro (gemini-3-pro-image, recommended)
Near-perfect text rendering and exact-font control — strong for table headers + cells.
- Name an exact font and weight (e.g., "Roboto Bold for header row and left column; Roboto Regular for cells").
- Emphasize these are **flat print artwork** (ink-on-paper), not a spreadsheet/UI mockup — the Thinking process otherwise biases toward realism and software styling.
- Reinforce in a system prompt: "Render supplied coverage marks verbatim; never infer or fill in a coverage mark." This curbs its tendency to "complete" a matrix.
- Use Markdown structure and ALL-CAPS `MUST`/`NEVER` for constraints; specify hex colors (`#1F5C3A`).
- See [NANO_BANANA_GUIDE.md](../NANO_BANANA_GUIDE.md).

### DALL-E 3 (legacy)
Add: `"Graphic design flat lay, reference table design, typography-focused, print material, flat 2D"`. Small dense matrices often exceed DALL-E 3's reliable rendering and it may invent marks — prefer gpt-image-2 / Nano Banana Pro and verify.

### Midjourney (legacy)
```
flat print artwork, clinician antibiotic coverage badge buddy, printed reference table,
landscape format, clinical typography,
--ar 16:10 --v 6 --style raw --s 25
--no badge lanyard clip holder 3d mockup photo gradient shadow rounded corners spreadsheet
```
Note: Midjourney does not reliably render exact table text/marks — not recommended for a coverage card; prefer a text-faithful model.

### Stable Diffusion (legacy)
Negative prompt: `"badge, lanyard, clip, holder, 3d, mockup, photo, gradient, shadow, rounded corners, depth, lighting, gloss, bevel, perspective, spreadsheet"`. Not recommended for precise matrix text.

---

## Troubleshooting

### Problem: The model "filled in" the matrix with its own coverage marks
**Critical fix:** `"Coverage marks are supplied by me. Render only the marks I provide; render empty/placeholder cells verbatim (e.g., [Y/N/V]). Do NOT decide, infer, or add any coverage mark."` Discard any card where the model assigned marks itself.

### Problem: Output looks like a spreadsheet / software UI
**Add:** `"This is a printed reference table, NOT a spreadsheet. No heavy cell boxes, no sheet tabs, no gridlines that look like Excel. Thin rules only."`

### Problem: Still getting mockups/3D renders
**Add:** `"Top-down flat view only. This IS the card surface, not an image OF a card."`

### Problem: Rounded corners appearing
**Add:** `"Rounded corners = rendering error. All corners must be sharp 90-degree angles."`

### Problem: Supplied content altered, dropped, or "corrected"
**Add:** `"Typeset every field, header, mark, and note EXACTLY as written. Do NOT change, reorder, or omit anything."` Then re-check the output against your source cell-by-cell.

### Problem: Gradients appearing
**Add:** `"SOLID colors ONLY. Any gradient in any element means the output is incorrect."`

### Problem: Only one image generated
**Add:** `"Generate EXACTLY 2 images. NOT 1. NOT 3. EXACTLY 2 separate images."`

---

## Verification Checklist (Before Printing)

- [ ] Every organism, drug, coverage mark, and empiric recommendation cross-checked against **your current local antibiogram and antimicrobial-stewardship guidance** before printing
- [ ] Confirmed the antibiogram is current (resistance shifts year to year) and unit-appropriate
- [ ] Legend matches the marks used; no undefined symbols
- [ ] Empiric recs, allergy cross-reactivity, and renal-dosing notes verified with stewardship/pharmacy/ID
- [ ] No coverage mark, spectrum, or recommendation inferred, added, or altered by the image model (cell-by-cell comparison to source)
- [ ] All EXAMPLE marks removed/replaced with verified local values
- [ ] Footer present: "Based on local antibiogram - verify against current stewardship guidance before use"
- [ ] Card dated with the antibiogram year so it can be retired when a new antibiogram is published
- [ ] Two images, landscape, flat print artwork, no gradients/shadows/rounded corners, not spreadsheet-styled
- [ ] Reviewed and approved by antimicrobial stewardship / ID / pharmacy before distribution

---

*Updated: 2026-06-23 — Template-driven local-antibiogram coverage badge buddy with placeholder-preserving anti-fabrication and clinical-accuracy verification.*
