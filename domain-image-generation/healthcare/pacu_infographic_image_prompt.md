---
title: "PACU Receiving Algorithm Infographic - Image Generation Prompt"
category: medical-education
description: "Image generation prompt for creating a medical pocket card infographic covering the first 15 minutes of PACU patient receiving protocol"
tags:
  - medical
  - infographic
  - clinical-workflow
  - pocket-card
  - pacu
  - nursing
  - image-generation
updated: "2026-01-28"
---

# PACU Receiving Algorithm Infographic - Image Generation Prompt

**Purpose:** Generate a professional medical reference infographic for PACU nurses covering the critical first 15 minutes of patient receiving workflow.

**Format:** 5x8 inch landscape pocket card, lamination-ready, clinical aesthetic

**See Also:** [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) for the techniques used in this prompt.

---

## Image Generation Prompt (Production-Ready)

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a medical pocket reference infographic for PACU (Post-Anesthesia Care Unit) nurses.

IMPORTANT REAL-WORLD CONTEXT:
This is a pocket card reference.
It will be printed on cardstock and laminated.
It is used in high-stress clinical situations.
It must be readable at arm's length in dim lighting.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT an illustration.

This image represents the literal ink-on-paper artwork sent directly to a printer.

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY ONE IMAGE.
- The image must be a SINGLE flat rectangle.
- Orientation: LANDSCAPE (horizontal).
- NO rounded outer corners on the overall card.
- NO drop shadows.
- NO gradients of any kind.
- NO lighting, gloss, bevel, or depth effects.
- NO background beyond the artwork edges.

If any gradient, shadow, or rounded outer corner appears, the output is incorrect.

================================================
PHYSICAL SIZE & CANVAS
================================================

Size:
- 5 inches wide x 8 inches tall (landscape when rotated for viewing)
- Wait - correction: 8 inches wide x 5 inches tall (landscape)
- Resolution: 2400 x 1500 px at 300 DPI
- Edge-to-edge artwork (this IS the printed content)

Background:
- Solid white (#FFFFFF) ONLY
- No texture
- No vignette
- No fade

================================================
COLUMN LAYOUT - THIS IS THE MOST IMPORTANT PART
================================================

STRICT 5-COLUMN VERTICAL STRUCTURE:

All columns MUST be:
- Equal width (each = 20% of content area)
- Full height (minus header and footer)
- Separated by thin solid gray lines (#6B7280, 1px)
- Aligned perfectly

COLUMN 1 (leftmost): IMMEDIATE 0-2 MIN
- Background: Light red #FEE2E2
- Header text: "IMMEDIATE (0-2 Minutes)"

COLUMN 2: ANESTHESIA HANDOFF 2-5 MIN
- Background: Light amber #FEF3C7
- Header text: "ANESTHESIA HANDOFF (2-5 Minutes)"

COLUMN 3: FOCUSED ASSESSMENT 5-10 MIN
- Background: Light yellow #FEF9C3
- Header text: "FOCUSED ASSESSMENT (5-10 Minutes)"

COLUMN 4: VITALS & DOCUMENTATION ONGOING
- Background: Light blue #DBEAFE
- Header text: "VITALS & DOCUMENTATION (Ongoing)"

COLUMN 5 (rightmost): RED FLAGS
- Background: Light red #FEE2E2
- Border: Thick red border (3px solid #991B1B) around entire column
- Header text: "RED FLAGS - Do Not Wait" (in red #991B1B)

================================================
HEADER SECTION
================================================

Position: Top of image
Height: 15% of total height
Fill: Solid dark red #B91C1C
Text (white):
- Title: "PACU RECEIVING ALGORITHM" in bold, 18pt, all caps
- Subtitle: "First 15 Minutes | Phase I PACU" in 12pt
- Right side: "0-15 MIN" with simple clock icon

NO rounded corners on header.
Sharp rectangular edges only.

================================================
FOOTER SECTION
================================================

Position: Bottom of image
Height: 10% of total height
Fill: Solid green #15803D
Text (white):
- Header: "STABILIZATION GOALS (By 15 Minutes)" in bold, 12pt
- 7 checkbox items in 9pt:
  1. Airway maintained without intervention
  2. SpO2 94% or higher on 4L NC or less (or baseline)
  3. BP/HR within 20% of baseline
  4. Patient following commands
  5. Pain assessed, treatment initiated
  6. Surgical site checked, stable
  7. All lines/drains verified and documented
- Bottom tagline (italic, 8pt): "Remember: The first 15 minutes set the tone. Catch problems early - they only get worse."

NO rounded corners on footer.
Sharp rectangular edges only.

================================================
COLUMN 1 CONTENT: IMMEDIATE (0-2 MIN)
================================================

Starting element:
- Box labeled "PATIENT ARRIVES" (rectangular, no rounded corners)
- Arrow pointing down

Decision diamond:
- Text: "A - AIRWAY PATENT?"
- Below: "Look: Chest rise, color, position"
- Below: "Listen: Breath sounds, stridor"

Two branches:
- YES path: Green checkmark, "Continue", arrow down
- NO path: Red X, red alert box containing:
  "CALL ANESTHESIA NOW"
  "Jaw thrust, suction, O2 via NRB 15L"

Below flow, numbered checklist "DO FIRST - In order:":
1. Airway - Confirm patent, position head, apply O2 per orders
2. Breathing - Watch chest rise, count RR, SpO2 on
3. Circulation - BP, HR on monitor, palpate pulse
4. Handoff - Listen to anesthesia report (do not interrupt)

Each item has checkbox.

================================================
COLUMN 2 CONTENT: ANESTHESIA HANDOFF (2-5 MIN)
================================================

Subheader: "GET THIS INFORMATION:" in bold

Table with 2 columns and 6 rows:
| Must Know | Why It Matters |
|-----------|----------------|
| Airway difficulty? | Prepare for reintubation |
| Anesthesia type (GA/MAC/regional) | Recovery expectations |
| Opioids given (what/when/how much) | Sedation + pain timing |
| Fluids/blood/EBL | Volume status |
| Complications intra-op? | What to watch |
| Surgeon concerns? | Specific orders |

Bottom callout box (amber border 3px):
"NEVER let anesthesia leave until you have:"
- Checkbox: Stable vitals x 1 set
- Checkbox: Handoff complete
- Checkbox: Questions answered

================================================
COLUMN 3 CONTENT: FOCUSED ASSESSMENT (5-10 MIN)
================================================

Subheader: "LOOK FOR TROUBLE - The Big 5" in bold

Five assessment cards stacked vertically.
Each card contains:
- Check name | Normal range | Abnormal - Act

Card 1 - Airway:
Normal: Clear, no snoring
Abnormal-Act: Stridor/obstruction - jaw thrust, call anesthesia

Card 2 - Breathing:
Normal: RR 10-20, SpO2 94% or higher
Abnormal-Act: RR below 8 or SpO2 below 92% - stimulate, O2 up, call anesthesia

Card 3 - Circulation:
Normal: SBP within 20% baseline, HR 60-100
Abnormal-Act: SBP below 90 or above 180, HR below 50 or above 120 - fluid/meds per order, call provider

Card 4 - LOC:
Normal: Rousable, follows commands
Abnormal-Act: Unresponsive or combative - rule out hypoxia, call anesthesia

Card 5 - Surgical site:
Normal: Dressing dry/intact
Abnormal-Act: Expanding hematoma, saturated dressing - apply pressure, call surgeon

Below cards, "ALSO CHECK:" with checkboxes:
- IV patent, fluids running per order
- Foley draining (if present) - note color/amount
- Drains functioning - note output
- Pain level (when patient can respond)
- Nausea (treat early per orders)
- Temperature - warming if below 36C

================================================
COLUMN 4 CONTENT: VITALS & DOCUMENTATION (ONGOING)
================================================

Subheader: "Vital signs q5-15 min per facility protocol" in 10pt

Vital signs list:
- BP, HR, RR, SpO2, temp
- Pain score when responsive
- LOC (Aldrete or per facility tool)

"Chart immediately:" with 4 items:
- Arrival time
- Handoff received from (name)
- Initial assessment findings
- Interventions performed

================================================
COLUMN 5 CONTENT: RED FLAGS
================================================

Header: "RED FLAGS - Do Not Wait" in bold red (#991B1B)

Six alert boxes stacked vertically.
Each alert box has format:
- If You See: [condition]
- Do This Now: [action]

Alert 1:
- If You See: Stridor, airway obstruction
- Do This Now: Jaw thrust, suction, call anesthesia STAT

Alert 2:
- If You See: SpO2 below 90% not improving with O2
- Do This Now: Bag-mask ready, call anesthesia STAT

Alert 3:
- If You See: SBP below 80 or unresponsive to fluids
- Do This Now: Trendelenburg, call anesthesia + surgeon

Alert 4:
- If You See: Expanding neck/surgical hematoma
- Do This Now: Direct pressure, call surgeon STAT

Alert 5:
- If You See: Chest pain + new ECG changes
- Do This Now: 12-lead, call provider STAT

Alert 6:
- If You See: Uncontrolled agitation
- Do This Now: Rule out hypoxia first, then treat per orders

Emergency terms (STAT, NOW, CALL) in bold.

================================================
DESIGN SYSTEM (STRICT)
================================================

ALL SHAPES:
- Rectangular only
- Sharp 90-degree corners only (EXCEPT decision diamonds)
- Solid fills only
- No transparency
- No gradients

Tables:
- Alternating row backgrounds allowed (white and very light gray)
- Thin solid borders (1px gray)
- No 3D effects

Alert boxes:
- Sharp rectangular corners
- Thin colored border (3px max)
- Solid fill

TYPOGRAPHY:
- Clean sans-serif (Open Sans, Roboto, or similar)
- Body text: 9pt minimum
- Headers: 12-18pt
- Minimum readable: 7pt
- High contrast: dark text on light backgrounds

NO icons or graphics except:
- Simple geometric arrows
- Checkboxes (square)
- Decision diamonds
- Basic line separators

================================================
CONSTRAINTS (REPEATED)
================================================

- NO gradients - solid colors only
- NO rounded outer corners on card, header, or footer
- NO shadows or depth effects
- NO mockup styling
- NO decorative elements
- All text minimum 7pt
- High contrast: minimum 4.5:1 ratio
- Bleed area: 0.125" on all sides
- Safe zone: 0.25" margin from edges
- Print-ready: CMYK color space, 300 DPI

================================================
VISUAL HIERARCHY
================================================

1. Primary attention: Red flags column, emergency actions, time-based headers
2. Secondary attention: Section headers, "DO FIRST", "NEVER let anesthesia leave"
3. Tertiary attention: Normal ranges, supporting details
4. Background: Color zones, subtle borders, checklist items

================================================
FINAL VALIDATION CHECK
================================================

- One image only
- Landscape orientation (wider than tall)
- 5 equal-width columns
- Color-coded time zones (red, amber, yellow, blue, red)
- Sharp rectangular corners on outer edges
- Flat print artwork
- Solid colors only
- No gradients
- No shadows
- No mockup styling
- Optimized for high-stress rapid reference
```

---

## Simplified Prompt (If Full Prompt Misbehaves)

```
Create ONE flat rectangular infographic for PACU nurses.

CRITICAL RULES:
- Landscape orientation (8 inches wide x 5 inches tall)
- 5 equal-width columns
- Sharp corners only - NO rounded corners on outer edges
- Solid colors only - NO gradients
- NO shadows, NO 3D effects
- This is FLAT PRINT ARTWORK, not a mockup

LAYOUT:
- Header (top, dark red): "PACU RECEIVING ALGORITHM - First 15 Minutes"
- Column 1 (light red): IMMEDIATE 0-2min - Airway check flowchart
- Column 2 (light amber): HANDOFF 2-5min - What to get from anesthesia
- Column 3 (light yellow): ASSESSMENT 5-10min - The Big 5 checks
- Column 4 (light blue): DOCUMENTATION - Vitals and charting
- Column 5 (light red, red border): RED FLAGS - 6 emergency alerts
- Footer (green): Stabilization goals checklist

If output has rounded corners or gradients, it is WRONG.
```

---

## Why This Prompt Works

This prompt uses proven image generation techniques:

1. **Terminology Steering** - "flat print artwork" instead of "card" to avoid UI associations
2. **Column Layout Forcing** - Explicit 5-column structure with equal widths and exact content
3. **Constraint Redundancy** - "no gradients" and "no rounded corners" appear multiple times
4. **Negative Space Control** - Bans backgrounds, shadows, mockup staging
5. **Physical Context** - "pocket card in high-stress clinical situations" anchors real-world usage
6. **Deliverables Locking** - "EXACTLY ONE IMAGE" with specific dimensions
7. **Validation Checklist** - Final self-audit block
8. **Allowed vs Forbidden** - Clear distinction for tables (alternating rows OK) vs forbidden (3D effects)

See [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) for detailed explanations.

---

## Model-Specific Variations

### For DALL-E 3
Add: `"Professional medical infographic design, clinical reference card, hospital guidelines aesthetic, high-detail typography, flat 2D print material"`

### For Midjourney
```
flat print artwork, medical pocket card infographic, PACU receiving algorithm,
5-column layout with color-coded time zones, clinical flowcharts,
high information density, clean typography, hospital reference style,
--ar 8:5 --v 6 --style raw --s 25
--no 3d mockup photo gradient shadow rounded corners badge
```

### For Stable Diffusion
**Negative Prompt:** `"photograph, 3d render, realistic, blurry, watermark, gradients, rounded corners, shadows, decorative elements, artistic interpretation, abstract, depth, lighting, gloss, bevel, mockup"`

### For ChatGPT / GPT-4o / GPT-5
The main prompt above is optimized for these models. Key elements:
- Explicit column content enumeration works well
- "If X appears, the output is incorrect" language is effective
- Alert box content enumeration prevents merging

---

## Troubleshooting

### Problem: Getting 3D mockups
**Add:** `"This IS the card surface viewed flat. NOT a photo OF a card. NOT a mockup. Pure flat 2D artwork."`

### Problem: Rounded corners appearing
**Add:** `"Rounded corners = rendering error. All outer corners must be sharp 90-degree angles."`

### Problem: Columns merged or wrong width
**Add:** `"EXACTLY 5 columns. Each column EXACTLY 20% width. No column may be wider or narrower than others."`

### Problem: Gradients in backgrounds
**Add:** `"SOLID fills ONLY. Any gradient in any element means the output is incorrect."`

### Problem: Content missing from columns
**Verify:** Each column's content is explicitly enumerated. Add: `"Do NOT omit any content. Every item listed must appear."`

---

## Print Specifications

- **Size:** 8" x 5" (landscape)
- **Resolution:** 300 DPI minimum (2400 x 1500 px)
- **Color Mode:** CMYK for print
- **Stock:** 14pt C2S (coated two-sided) cardstock
- **Finish:** Gloss lamination, 10mil thickness
- **Corners:** May round 3mm radius for durability AFTER printing

**Color Values (CMYK equivalent):**
- Red #B91C1C: C15 M100 Y100 K10
- Green #15803D: C80 M20 Y100 K10
- Amber #D97706: C0 M45 Y100 K0
- Blue #2563EB: C85 M60 Y0 K0

---

## Usage Context

**Target Users:** PACU nurses, nurse practitioners, anesthesia residents
**Use Case:** Pocket reference during first 15 minutes of patient receiving
**Environment:** Clinical PACU bay, potentially dim lighting, high-stress situations
**Access Pattern:** Quick glance for confirmation, detailed scan for unfamiliar scenarios
**Lifecycle:** Laminated card worn on badge or kept in pocket

---

*Updated: 2026-01-28 - Revised with proven image generation techniques from empirical testing*
