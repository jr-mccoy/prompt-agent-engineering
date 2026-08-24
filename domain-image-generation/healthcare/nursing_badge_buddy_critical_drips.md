---
title: "Nursing Badge Buddy - Critical Care Drips"
category: medical-education
description: "Image generation prompt for creating printable nursing badge buddy reference cards for ICU/critical care medication drips"
tags:
  - medical
  - nursing
  - badge-buddy
  - pocket-card
  - icu
  - critical-care
  - vasopressors
  - image-generation
updated: "2026-01-28"
---

# Nursing Badge Buddy - Critical Care Drips

**Purpose:** Generate printable reference cards (badge buddies) for ICU/critical care nurses containing common IV drip medications, dosing, and titration parameters.

**Format:** Two-sided badge buddy, 4.5" x 2.75" landscape, lamination-ready

**See Also:** [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) for the techniques used in this prompt.

---

## Image Generation Prompt (Production-Ready)

```
TASK: Generate TWO SEPARATE FLAT PRINT ARTWORK IMAGES representing nursing BADGE BUDDY inserts worn behind a nurse's name badge.

IMPORTANT REAL-WORLD CONTEXT:
These are badge buddies.
They are worn BEHIND a nurse's ID badge.
They must be LANDSCAPE (wider than tall).
They are quick-glance clinical references.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT an illustration.

These images represent the literal ink-on-paper artwork sent directly to a printer.

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
- No empty boxes.
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

TYPOGRAPHY ONLY - NO ICON GRAPHICS.
Allowed symbols (text only): up-arrow, down-arrow, star, warning-triangle

================================================
TYPOGRAPHY
================================================

- Drug name: Bold, 8-9 pt
- Dosing/details: Regular, 7-8 pt
- Minimum text size: 6.5 pt
- Clean clinical sans-serif
- High contrast black text

================================================
HEADER (BOTH CARDS)
================================================

Solid rectangle at top (not a "card top")

Fill: Solid navy #1E3A5F
Text (white):
CRITICAL DRIPS
Quick Reference

Orientation label (plain text):
FRONT (card A)
BACK (card B)

================================================
FOOTER (BOTH CARDS)
================================================

Solid rectangle at bottom

Fill: Solid navy #1E3A5F
Text (white, 7 pt):
Verify orders before administration

================================================
BADGE BUDDY A (FRONT)
================================================
Category focus: VASOPRESSORS + BP CONTROL

2 ROWS x 3 COLUMNS - EXACT ASSIGNMENT:

BOX 1:
LEVOPHED (norepinephrine)
8 mg/250 mL
BP greater than HR effect
Start: 0.05
Titrate: 0.02 q3 min
Max: 1 mcg/kg/min
First line septic/cardiogenic/hypovolemic shock

BOX 2:
EPINEPHRINE
10 mg/250 mL
Increases BP and HR
Start: 0.05
Titrate: 0.05 q3 min
Max: 2 mcg/kg/min
Low dose = HR greater than BP

BOX 3:
NEOSYNEPHRINE (phenylephrine)
50 mg/250 mL
Increases BP only
Start: 0.5
Titrate: 0.1 q3 min
Max: 3 mcg/kg/min
May cause bradycardia

BOX 4:
VASOPRESSIN
Increases BP
Fixed: 0.01-0.03 units/min
(No titration)

BOX 5:
DOPAMINE
400 mg/250 mL D5W
Renal: 0.5-3
HR>BP: 3-10
BP&HR: 10-20

BOX 6:
CARDENE (nicardipine)
BP control
Start: 5 mg/hr
Range: 5-15 mg/hr
Max: 15 mg/hr

================================================
BADGE BUDDY B (BACK)
================================================
Category focus: SEDATION + ANTIARRHYTHMICS

2 ROWS x 3 COLUMNS - EXACT ASSIGNMENT:

BOX 1:
PROPOFOL (Diprivan)
10 mg/mL
5-50 mcg/kg/min
(Max 100 MD order)
INTUBATED PATIENTS ONLY

BOX 2:
PRECEDEX (dexmedetomidine)
Start: 0.2
Max: 1.4 mcg/kg/hr
Watch for Bradycardia
Watch for Hypotension

BOX 3:
AMIODARONE
Bolus: 150 mg / 10 min
1 mg/min x 6 hr
then 0.5 mg/min x 18 hr

BOX 4:
CARDIZEM (diltiazem)
100 mg/100 mL
A-fib / flutter / SVT
5-15 mg/hr
Max: 15 mg/hr

BOX 5:
LIDOCAINE
V-fib / pulseless V-tach
Bolus: 1 mg/kg / 2 min
Maintenance: 1-4 mg/min

BOX 6:
CLEVIPREX (clevidipine)
BP control
Start: 2 mg/hr
Max: 21 mg/hr

================================================
FINAL VALIDATION CHECK
================================================

- Two images only
- Landscape orientation
- 2 rows x 3 columns per card
- Equal-sized boxes
- One drug per box
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
Create TWO flat rectangular images for a nursing badge buddy (worn behind ID badge).

CRITICAL RULES:
- Landscape orientation (wider than tall)
- 4.5 x 2.75 inches each
- EXACTLY 2 rows x 3 columns grid
- One medication per box (6 total per image)
- Sharp corners only - NO rounded corners
- Solid colors only - NO gradients
- NO shadows, NO 3D effects
- This is FLAT PRINT ARTWORK, not a mockup

IMAGE 1 - FRONT (Vasopressors):
Header: "CRITICAL DRIPS - Quick Reference - FRONT" (navy blue)
Box 1: Levophed - 8mg/250mL, Start 0.05, Max 1
Box 2: Epinephrine - 10mg/250mL, Start 0.05, Max 2
Box 3: Neosynephrine - 50mg/250mL, Start 0.5, Max 3
Box 4: Vasopressin - Fixed 0.01-0.03 units/min
Box 5: Dopamine - 400mg/250mL, Renal/HR/BP dosing
Box 6: Cardene - 5-15mg/hr, Max 15
Footer: "Verify orders before administration" (navy blue)

IMAGE 2 - BACK (Sedation/Antiarrhythmics):
Header: "CRITICAL DRIPS - Quick Reference - BACK" (navy blue)
Box 1: Propofol - 5-50 mcg/kg/min, intubated only
Box 2: Precedex - Start 0.2, Max 1.4
Box 3: Amiodarone - Bolus 150mg, then 1mg/min x 6hr
Box 4: Cardizem - 5-15mg/hr for A-fib
Box 5: Lidocaine - Bolus 1mg/kg, Maint 1-4mg/min
Box 6: Cleviprex - 2-21mg/hr
Footer: "Verify orders before administration" (navy blue)

If output has rounded corners or gradients, it is WRONG.
```

---

## Why This Prompt Works

This prompt uses proven image generation techniques:

1. **Terminology Steering** - "flat print artwork" instead of "card" to avoid UI associations
2. **Grid Forcing** - Explicit 2x3 grid with equal-sized boxes
3. **Enumerated Slots** - BOX 1, BOX 2, etc. prevents content reorganization
4. **Constraint Redundancy** - "no gradients" appears 3+ times
5. **Negative Space Control** - Bans backgrounds, shadows, mockup staging
6. **Physical Context** - "worn behind nurse's ID badge" anchors real-world usage
7. **Deliverables Locking** - "EXACTLY TWO IMAGES" with specific dimensions
8. **Validation Checklist** - Final self-audit block

See [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) for detailed explanations.

---

## Medication Content Reference

### VASOPRESSORS (Goal: MAP 65-75 or SBP 90-100)

| Drug | Concentration | Effect | Start | Titrate | Max |
|------|---------------|--------|-------|---------|-----|
| **Levophed** (norepinephrine) | 8mg/250mL | BP > HR | 0.05 mcg/kg/min | 0.02 q3min | 1 mcg/kg/min |
| **Epinephrine** | 10mg/250mL | BP & HR | 0.05 mcg/kg/min | 0.05 q3min | 2 mcg/kg/min |
| **Neosynephrine** (phenylephrine) | 50mg/250mL | BP only | 0.5 mcg/kg/min | 0.1 q3min | 3 mcg/kg/min |
| **Vasopressin** | - | BP | 0.01-0.03 units/min (fixed) | - | - |
| **Dopamine** | 400mg/250mL D5W | Varies | Renal: 0.5-3 | HR>BP: 3-10 | BP&HR: 10-20 |

### ANTIHYPERTENSIVES (Goal: SBP<180, DBP<105)

| Drug | Start | Range | Max |
|------|-------|-------|-----|
| **Cardene** (nicardipine) | 5mg/hr | 5-15mg/hr | 15mg/hr |
| **Cleviprex** (clevidipine) | 2mg/hr | - | 21mg/hr |

### SEDATIVES

| Drug | Concentration | Dosing | Notes |
|------|---------------|--------|-------|
| **Propofol** (Diprivan) | 10mg/mL | 5-50 mcg/kg/min (max 100 w/ MD order) | INTUBATED ONLY |
| **Precedex** (dexmedetomidine) | - | Start 0.2, Max 1.4 mcg/kg/hr | Can cause bradycardia & hypotension |

### ANTIARRHYTHMICS

| Drug | Indication | Dosing |
|------|------------|--------|
| **Amiodarone** | Various | Bolus: 150mg/10min, then 1mg/min x 6hr, then 0.5mg/min x 18hr |
| **Cardizem** (diltiazem) | A-fib, A-flutter, SVT | 5-15mg/hr, Max 15mg/hr |
| **Lidocaine** | V-fib, pulseless V-tach | Bolus: 1mg/kg/2min, Maint: 1-4mg/min |

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

### DALL-E 3
Add: `"Graphic design flat lay, reference card design, typography-focused, print material, flat 2D"`

### Midjourney
```
flat print artwork, nursing badge buddy, critical care medications,
2x3 grid layout, landscape format, clinical typography,
--ar 16:10 --v 6 --style raw --s 25
--no badge lanyard clip holder 3d mockup photo gradient shadow rounded corners
```

### Stable Diffusion
Negative prompt: `"badge, lanyard, clip, holder, 3d, mockup, photo, gradient, shadow, rounded corners, depth, lighting, gloss, bevel, perspective"`

### ChatGPT / GPT-4o / GPT-5
The main prompt above is optimized for these models. Key elements:
- Explicit grid enumeration works well
- "If X appears, the output is incorrect" language is effective
- Physical context anchoring helps constrain the output

---

## Troubleshooting

### Problem: Still getting mockups/3D renders
**Add:** `"Top-down flat view only. This IS the card surface, not an image OF a card."`

### Problem: Rounded corners appearing
**Add:** `"Rounded corners = rendering error. All corners must be sharp 90-degree angles."`

### Problem: Content merged or reorganized
**Verify:** Each BOX assignment is explicit and numbered. Add: `"Do NOT combine medications. Do NOT reorganize. Follow BOX assignments exactly."`

### Problem: Gradients appearing
**Add:** `"SOLID colors ONLY. Any gradient in any element means the output is incorrect."`

### Problem: Only one image generated
**Add:** `"Generate EXACTLY 2 images. NOT 1. NOT 3. EXACTLY 2 separate images."`

---

*Updated: 2026-01-28 - Revised with proven image generation techniques from empirical testing*
