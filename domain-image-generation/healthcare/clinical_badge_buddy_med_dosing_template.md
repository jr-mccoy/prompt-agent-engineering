---
title: "Clinical Badge Buddy - Medication Dosing (Template)"
category: medical-education
description: "Template-driven image generation prompt for creating printable clinician badge buddy medication-dosing reference cards that the user fills with their own institution-verified drugs and doses"
tags:
  - medical
  - clinician
  - badge-buddy
  - pocket-card
  - medication-dosing
  - pharmacy
  - template
  - reference-card
  - image-generation
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - ./nursing_badge_buddy_critical_drips.md
  - ./clinical_badge_buddy_lab_values.md
  - ./clinical_badge_buddy_acls_codes.md
  - ./clinical_badge_buddy_antibiogram_template.md
---

# Clinical Badge Buddy - Medication Dosing (Template)

**Purpose:** Generate a printable, fully **template-driven** medication-dosing reference card (badge buddy) that **you fill in** with your own institution-verified drugs, doses, routes, and frequencies. This prompt produces the *layout and typesetting* only — it ships with placeholders, not real doses, so it can be safely reused across services (e.g., your unit's PRN list, common antiemetics, anticoagulant reversal, weight-based pressors) by swapping in your verified content.

**Format:** Two-sided badge buddy, 4.5" x 2.75" landscape, lamination-ready

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) for the 8 print-ready techniques used in this prompt.
- [nursing_badge_buddy_critical_drips.md](./nursing_badge_buddy_critical_drips.md) for a fully-populated example badge buddy.
- [clinical_badge_buddy_lab_values.md](./clinical_badge_buddy_lab_values.md), [clinical_badge_buddy_acls_codes.md](./clinical_badge_buddy_acls_codes.md), [clinical_badge_buddy_antibiogram_template.md](./clinical_badge_buddy_antibiogram_template.md)

> **⚠ CLINICAL SAFETY — THIS IS A BLANK TEMPLATE:** This card intentionally contains **no real medication doses.** Every drug, dose, unit, route, and frequency is a placeholder you must replace with values from your **institution-verified source** (pharmacy formulary, order set, or protocol). Doses are patient-, indication-, weight-, renal/hepatic-, and route-specific. The image model must typeset your placeholders or your supplied values **exactly** — it must never invent, fill in, "complete," round, or "correct" a dose. See the **Anti-Fabrication / Clinical Content** section.

---

## How to Use This Template

1. Decide your card's topic (e.g., "Common PRN meds," "Anticoagulant reversal," "Adult vasopressor starting doses").
2. Replace each placeholder field in the BOX assignments below:
   - `[DRUG]` — drug name (generic; add brand in parentheses if useful)
   - `[DOSE]` — dose with units (e.g., `4 mg`, `0.05 mcg/kg/min`)
   - `[ROUTE]` — IV / IM / PO / SubQ / etc.
   - `[FREQ]` — frequency / interval (e.g., `q6h PRN`, `once`)
   - `[MAX]` — max dose / max per 24h (optional)
   - `[NOTE]` — one key caution (renal adjust, monitor, contraindication)
3. Keep doses **exactly** as your verified source states them — do not let the model paraphrase.
4. Run the validation + verification checklists before printing.

---

## Image Generation Prompt (Production-Ready, Template)

```
TASK: Generate TWO SEPARATE FLAT PRINT ARTWORK IMAGES representing a clinician BADGE BUDDY insert worn behind a hospital ID badge.

IMPORTANT REAL-WORLD CONTEXT:
These are badge buddies.
They are worn BEHIND a clinician's ID badge.
They must be LANDSCAPE (wider than tall).
They are quick-glance medication-dosing references.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT an illustration.

These images represent the literal ink-on-paper artwork sent directly to a printer.

CRITICAL CONTENT RULE (READ FIRST):
This is a TEMPLATE. The fields below may contain PLACEHOLDERS like [DRUG], [DOSE], [ROUTE], [FREQ].
Typeset EVERY field EXACTLY as written.
If a field is a placeholder, render the placeholder text verbatim (e.g., "[DOSE]").
Do NOT fill in, complete, guess, invent, round, or "correct" any drug name, dose, unit, route, or frequency.
You are typesetting only. You are NOT a clinical source.

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
- One drug per box.
- No box may span multiple rows or columns.
- No empty boxes (if you have fewer than 6 drugs, render the placeholder fields as-is).
- No combined drugs.

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
- Optional thin left-edge color bar per drug category
- NO rounded corners

ALLOWED (structured layouts):
- Aligned label/value lines inside a box
- Thin divider rule between drug name and details
- Typographic hierarchy (drug name bold, details regular)

FORBIDDEN (software appearance):
- Excel-like cell grid with heavy borders
- Spreadsheet sheet tabs or headers
- Any software interface styling

TYPOGRAPHY ONLY - NO ICON GRAPHICS.
Allowed symbols (text only): slash, en-dash, x (for "times")

================================================
TYPOGRAPHY
================================================

- Drug name: Bold, 8-9 pt
- Dose / route / freq / note: Regular, 6.5-7.5 pt
- Minimum text size: 6.5 pt
- Clean clinical sans-serif
- High contrast black text on light fill

================================================
HEADER (BOTH CARDS)
================================================

Solid rectangle at top (not a "card top")

Fill: Solid slate blue #2F4858
Text (white):
[CARD TITLE - e.g., MEDICATION DOSING]
Quick Reference

Orientation label (plain text):
FRONT (card A)
BACK (card B)

================================================
FOOTER (BOTH CARDS)
================================================

Solid rectangle at bottom

Fill: Solid slate blue #2F4858
Text (white, 6.5 pt):
Verify against current orders/protocol before clinical use

================================================
BADGE BUDDY A (FRONT)
================================================
Category focus: [CATEGORY A - e.g., COMMON PRN MEDS]

2 ROWS x 3 COLUMNS - EXACT ASSIGNMENT
(TEMPLATE - replace bracketed placeholders with YOUR institution-verified values;
typeset placeholders verbatim if left blank):

BOX 1:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

BOX 2:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

BOX 3:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

BOX 4:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

BOX 5:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

BOX 6:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

================================================
BADGE BUDDY B (BACK)
================================================
Category focus: [CATEGORY B - e.g., WEIGHT-BASED / HIGH-ALERT MEDS]

2 ROWS x 3 COLUMNS - EXACT ASSIGNMENT
(TEMPLATE - replace bracketed placeholders with YOUR institution-verified values;
typeset placeholders verbatim if left blank):

BOX 1:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

BOX 2:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

BOX 3:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

BOX 4:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

BOX 5:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

BOX 6:
[DRUG]
[DOSE] [ROUTE]
[FREQ]
Max: [MAX]
Note: [NOTE]

================================================
FINAL VALIDATION CHECK
================================================

- Two images only
- Landscape orientation
- 2 rows x 3 columns per card
- Equal-sized boxes
- One drug per box
- Every field typeset EXACTLY as supplied; placeholders rendered verbatim (no invented doses)
- Flat print artwork
- Solid colors only
- No gradients
- No rounded corners
- No UI or mockup styling
- Optimized for instant badge-level glance
```

---

## Worked Example (EXAMPLE — REPLACE WITH YOUR INSTITUTION'S VERIFIED VALUES)

The block below shows how a single box looks when filled in. These are illustrative, conservative, commonly-accepted examples **for layout demonstration only** — they are **NOT a dosing standard** and must be replaced with your institution-verified values:

```
BOX 1:
ONDANSETRON (Zofran)               <- EXAMPLE
4 mg IV                            <- EXAMPLE
q6h PRN nausea                     <- EXAMPLE
Max: per institution               <- EXAMPLE
Note: QT prolongation caution      <- EXAMPLE
```

Do not copy the example into a clinical card without confirming it against your own formulary/order set.

---

## Simplified Prompt (If Full Prompt Misbehaves)

If the AI still generates mockups or UI-style output:

```
Create TWO flat rectangular images for a clinician medication-dosing badge buddy (worn behind ID badge).

CRITICAL RULES:
- Landscape orientation (wider than tall)
- 4.5 x 2.75 inches each
- EXACTLY 2 rows x 3 columns grid
- One drug per box (6 total per image)
- Sharp corners only - NO rounded corners
- Solid colors only - NO gradients
- NO shadows, NO 3D effects
- This is FLAT PRINT ARTWORK, not a mockup
- This is a TEMPLATE: typeset every field EXACTLY as written. Render placeholders like
  [DRUG]/[DOSE] verbatim. Do NOT fill in, guess, or change any dose.

IMAGE 1 - FRONT:
Header: "[CARD TITLE] - Quick Reference - FRONT" (slate blue)
Boxes 1-6: each = [DRUG] / [DOSE] [ROUTE] / [FREQ] / Max: [MAX] / Note: [NOTE]
Footer: "Verify against current orders/protocol before clinical use" (slate blue)

IMAGE 2 - BACK:
Header: "[CARD TITLE] - Quick Reference - BACK" (slate blue)
Boxes 1-6: each = [DRUG] / [DOSE] [ROUTE] / [FREQ] / Max: [MAX] / Note: [NOTE]
Footer: "Verify against current orders/protocol before clinical use" (slate blue)

If output has rounded corners or gradients, it is WRONG.
```

---

## Why This Prompt Works

This prompt uses the 8 proven print-ready image generation techniques (see [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md)):

1. **Terminology Steering** - "flat print artwork" instead of "card" to avoid UI associations
2. **Grid Forcing** - Explicit 2x3 grid with equal-sized boxes
3. **Enumerated Slots** - BOX 1, BOX 2, etc. keeps each drug's fields together and prevents reorganization
4. **Constraint Redundancy** - "no gradients" and "typeset verbatim / do not fill in" appear at multiple levels
5. **Negative Space Control** - Bans backgrounds, shadows, mockup staging
6. **Physical Context** - "worn behind clinician's ID badge" anchors real-world usage
7. **Deliverables Locking** - "EXACTLY TWO IMAGES" with specific dimensions
8. **Validation Checklist** - Final self-audit block, including a render-placeholders-verbatim check

---

## Anti-Fabrication / Clinical Content

**The image model RENDERS supplied clinical content. It does NOT generate medical facts.**

- This is a **blank template**. It deliberately contains placeholders (`[DRUG]`, `[DOSE]`, `[ROUTE]`, `[FREQ]`, `[MAX]`, `[NOTE]`) and **no real doses**.
- The model must **typeset placeholders verbatim** and must **never fill in, complete, guess, invent, round, or "correct"** any drug name, dose, unit, route, or frequency.
- All clinical content is **supplied by you** from your institution-verified source (formulary, order set, pharmacy protocol). Doses are patient-, indication-, weight-, renal/hepatic-, and route-specific — a "common" dose is not a substitute for your verified value.
- The single Worked Example box is labeled "EXAMPLE — REPLACE WITH YOUR INSTITUTION'S VERIFIED VALUES" and is for **layout demonstration only**; it is not a dosing standard.
- High-alert medications (anticoagulants, insulin, opioids, sedatives, chemotherapy, concentrated electrolytes) carry the highest fabrication risk — double-verify these and consider a pharmacist co-sign.
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
Best-in-class text rendering — and best at faithfully reproducing bracketed placeholders without "helpfully" filling them in.
- Set `quality="high"` — required for legible 6.5-7.5 pt drug names and doses.
- The main prompt above maps cleanly onto its structure; keep the print constraints together as one block.
- `input_fidelity` is disabled in gpt-image-2 — do not pass it.
- Explicit grid enumeration and "if X appears, output is incorrect" language both work well.
- See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md) for full details.

### Nano Banana Pro (gemini-3-pro-image, recommended)
Near-perfect text rendering and exact-font control.
- Name an exact font and weight (e.g., "Roboto Bold for drug names; Roboto Regular for details").
- Emphasize these are **flat print artwork** (ink-on-paper), not a UI mockup — the Thinking process otherwise biases toward realism/3D.
- Reinforce in a system prompt: "Render bracketed placeholders verbatim; never complete or invent a dose." This curbs its tendency to "finish" partial content.
- Use Markdown structure and ALL-CAPS `MUST`/`NEVER` for constraints; specify hex colors (`#2F4858`).
- See [NANO_BANANA_GUIDE.md](../NANO_BANANA_GUIDE.md).

### DALL-E 3 (legacy)
Add: `"Graphic design flat lay, reference card design, typography-focused, print material, flat 2D"`. May mangle or "auto-complete" placeholders — verify carefully or prefer gpt-image-2 / Nano Banana Pro.

### Midjourney (legacy)
```
flat print artwork, clinician medication dosing badge buddy template,
2x3 grid layout, landscape format, clinical typography,
--ar 16:10 --v 6 --style raw --s 25
--no badge lanyard clip holder 3d mockup photo gradient shadow rounded corners
```
Note: Midjourney does not reliably render exact text/placeholders — not recommended for a dosing card; prefer a text-faithful model.

### Stable Diffusion (legacy)
Negative prompt: `"badge, lanyard, clip, holder, 3d, mockup, photo, gradient, shadow, rounded corners, depth, lighting, gloss, bevel, perspective"`. Not recommended for precise dose text.

---

## Troubleshooting

### Problem: The model "filled in" placeholders with real-looking doses
**Critical fix:** `"This is a blank template. Render [DRUG], [DOSE], [ROUTE], [FREQ] EXACTLY as written, including the square brackets. Do NOT replace placeholders with any drug or number."` Re-generate and confirm no placeholder was completed. Discard any card where the model invented a dose.

### Problem: Still getting mockups/3D renders
**Add:** `"Top-down flat view only. This IS the card surface, not an image OF a card."`

### Problem: Rounded corners appearing
**Add:** `"Rounded corners = rendering error. All corners must be sharp 90-degree angles."`

### Problem: Supplied doses altered, dropped, or "corrected"
**Add:** `"Typeset every value EXACTLY as written. Do NOT change, round, reorder, or omit any number, unit, route, or frequency."` Then re-check the output against your source line-by-line.

### Problem: Content merged or reorganized
**Verify:** Each BOX assignment is explicit and numbered. Add: `"Do NOT combine drugs. Do NOT reorganize. Follow BOX assignments exactly."`

### Problem: Gradients appearing
**Add:** `"SOLID colors ONLY. Any gradient in any element means the output is incorrect."`

### Problem: Only one image generated
**Add:** `"Generate EXACTLY 2 images. NOT 1. NOT 3. EXACTLY 2 separate images."`

---

## Verification Checklist (Before Printing)

- [ ] Every drug, dose, unit, route, and frequency cross-checked against **your institution's formulary / order set / pharmacy protocol** before printing
- [ ] Confirmed the dose matches the intended indication, route, and patient population (adult vs. peds; weight-based vs. fixed)
- [ ] Renal/hepatic and high-alert cautions verified and noted where relevant
- [ ] No placeholder was auto-completed and no dose invented or altered by the image model (line-by-line comparison to source)
- [ ] All EXAMPLE content removed/replaced with verified institutional values
- [ ] Footer present: "Verify against current orders/protocol before clinical use"
- [ ] Card dated and labeled with its source so it can be retired when the formulary/protocol changes
- [ ] Two images, landscape, 2x3 grid, flat print artwork, no gradients/shadows/rounded corners
- [ ] Reviewed and approved by a qualified clinician/pharmacist before distribution

---

*Updated: 2026-06-23 — Template-driven clinician dosing badge buddy with placeholder-preserving anti-fabrication and clinical-accuracy verification.*
