---
title: "Clinical Badge Buddy - ACLS / Code Blue Quick Reference"
category: medical-education
description: "Image generation prompt for creating printable clinician badge buddy reference cards for ACLS / code blue algorithms (arrest rhythms, code drug doses, H's & T's)"
tags:
  - medical
  - clinician
  - badge-buddy
  - pocket-card
  - acls
  - code-blue
  - resuscitation
  - emergency
  - image-generation
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - ./nursing_badge_buddy_critical_drips.md
  - ./clinical_badge_buddy_lab_values.md
  - ./clinical_badge_buddy_med_dosing_template.md
  - ./clinical_badge_buddy_antibiogram_template.md
---

# Clinical Badge Buddy - ACLS / Code Blue Quick Reference

**Purpose:** Generate printable reference cards (badge buddies) for clinicians and code-team members containing ACLS / code blue algorithm essentials: shockable vs. non-shockable arrest rhythms, code drug doses, and the reversible causes (H's & T's), for quick recall during resuscitation.

**Format:** Two-sided badge buddy, 4.5" x 2.75" landscape, lamination-ready

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) for the 8 print-ready techniques used in this prompt.
- [nursing_badge_buddy_critical_drips.md](./nursing_badge_buddy_critical_drips.md) for a sibling print-ready badge buddy.
- [clinical_badge_buddy_lab_values.md](./clinical_badge_buddy_lab_values.md), [clinical_badge_buddy_med_dosing_template.md](./clinical_badge_buddy_med_dosing_template.md), [clinical_badge_buddy_antibiogram_template.md](./clinical_badge_buddy_antibiogram_template.md)

> **⚠ CLINICAL SAFETY:** ACLS algorithms and drug doses are governed by current guidelines (e.g., AHA/ERC) and your institution's code policy, and they are periodically updated. This is an **adult ACLS** reference; pediatric (PALS), neonatal (NRP), and obstetric arrest use different doses and algorithms. The example content below reflects commonly-taught adult ACLS at the time of authoring and is provided to make the template usable — it is **NOT a substitute for current certification or your code policy.** Confirm every dose, interval, and step against the **current guideline edition and your institutional code protocol** before printing. The image model must render only the content you supply; it must never invent or alter a dose or step.

---

## Image Generation Prompt (Production-Ready)

```
TASK: Generate TWO SEPARATE FLAT PRINT ARTWORK IMAGES representing a clinician BADGE BUDDY insert worn behind a hospital ID badge.

IMPORTANT REAL-WORLD CONTEXT:
These are badge buddies.
They are worn BEHIND a clinician's ID badge.
They must be LANDSCAPE (wider than tall).
They are quick-glance ACLS / code blue references.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT an illustration.

These images represent the literal ink-on-paper artwork sent directly to a printer.

CRITICAL CONTENT RULE:
Render ONLY the doses, intervals, rhythms, and steps supplied in the BOX assignments below.
Do NOT invent, add, remove, round, or "correct" any dose, interval, rhythm, or step.
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
- One topic per box.
- No box may span multiple rows or columns.
- No empty boxes.
- No combined topics.

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
- Optional thin top-edge color bar per box for grouping
  (suggested: red bar for SHOCKABLE topics, blue bar for NON-SHOCKABLE/causes)
- NO rounded corners

ALLOWED (structured layouts):
- Numbered step lists inside a box
- Aligned drug/dose columns
- Thin divider rules between items
- Typographic hierarchy (topic bold, detail regular)

FORBIDDEN (software appearance):
- Excel-like cell grid with heavy borders
- Flowchart with rounded UI nodes and connector shadows
- Any software interface styling

TYPOGRAPHY ONLY - NO ICON GRAPHICS.
Allowed symbols (text only): right-arrow, slash, en-dash, x (for "times")

================================================
TYPOGRAPHY
================================================

- Topic title: Bold, 8-9 pt
- Steps / doses: Regular, 6.5-7.5 pt
- Minimum text size: 6.5 pt
- Clean clinical sans-serif
- High contrast black text on light fill

================================================
HEADER (BOTH CARDS)
================================================

Solid rectangle at top (not a "card top")

Fill: Solid dark red #8C1D1D
Text (white):
ADULT ACLS / CODE BLUE
Quick Reference

Orientation label (plain text):
FRONT (card A)
BACK (card B)

================================================
FOOTER (BOTH CARDS)
================================================

Solid rectangle at bottom

Fill: Solid dark red #8C1D1D
Text (white, 6.5 pt):
Follow current guidelines and your code protocol - verify before use

================================================
BADGE BUDDY A (FRONT)
================================================
Category focus: ARREST RHYTHMS + CPR QUALITY

2 ROWS x 3 COLUMNS - EXACT ASSIGNMENT
(EXAMPLE content shown — replace with your current guideline / code protocol):

BOX 1:
SHOCKABLE: VF / pVT
1. CPR + attach defib
2. SHOCK
3. CPR 2 min, IV/IO
4. SHOCK -> Epi 1 mg q3-5 min
5. CPR 2 min
6. SHOCK -> Amiodarone 300 mg
   (2nd dose 150 mg)

BOX 2:
NON-SHOCKABLE: PEA / Asystole
1. CPR 2 min, IV/IO
2. Epi 1 mg q3-5 min ASAP
3. CPR 2 min
4. Treat reversible causes
   (see H's & T's)
- Do NOT shock PEA/asystole

BOX 3:
HIGH-QUALITY CPR
- Rate 100-120/min
- Depth 2-2.4 in (5-6 cm)
- Full recoil
- Minimize interruptions
- Compressions:Vent 30:2
  (10/min if advanced airway)
- Switch compressor q2 min

BOX 4:
DEFIBRILLATION
- Biphasic: device-specific
  (e.g., 120-200 J)
- Monophasic: 360 J
- Resume CPR immediately
  after shock
- Confirm rhythm at 2 min

BOX 5:
RHYTHM CHECK RULES
- Check rhythm q2 min
- Pulse check only if
  organized rhythm
- Shockable -> shock
- Non-shockable -> CPR + Epi

BOX 6:
ROSC - POST-ARREST
- Confirm pulse + BP
- Target SBP/MAP per protocol
- 12-lead ECG
- Targeted temp management
- Treat cause; consult/transfer

================================================
BADGE BUDDY B (BACK)
================================================
Category focus: CODE DRUGS + H's & T's + PERI-ARREST

2 ROWS x 3 COLUMNS - EXACT ASSIGNMENT
(EXAMPLE content shown — replace with your current guideline / code protocol):

BOX 1:
CODE DRUGS - ARREST
Epinephrine 1 mg IV/IO q3-5 min
Amiodarone 300 mg, then 150 mg
Lidocaine (alt) 1-1.5 mg/kg,
  then 0.5-0.75 mg/kg
Flush 20 mL + raise limb

BOX 2:
H's (reversible causes)
- Hypovolemia
- Hypoxia
- Hydrogen ion (acidosis)
- Hypo/Hyperkalemia
- Hypothermia
- (Hypoglycemia)

BOX 3:
T's (reversible causes)
- Tension pneumothorax
- Tamponade (cardiac)
- Toxins
- Thrombosis (pulmonary)
- Thrombosis (coronary)

BOX 4:
BRADYCARDIA (symptomatic)
- Atropine 1 mg IV q3-5 min
  (max 3 mg)
- If inadequate:
  Transcutaneous pacing OR
  Dopamine / Epinephrine infusion
  (per protocol)

BOX 5:
TACHYCARDIA (with pulse)
- Unstable -> synchronized
  cardioversion
- Stable narrow regular:
  Vagal -> Adenosine 6 mg,
  then 12 mg
- Stable wide: expert consult

BOX 6:
KEY REMINDERS
- IV/IO access early
- Capnography to confirm CPR
  quality / ROSC
- Assign clear roles
- Document times + doses
- Adult ACLS only (not PALS/NRP)

================================================
FINAL VALIDATION CHECK
================================================

- Two images only
- Landscape orientation
- 2 rows x 3 columns per card
- Equal-sized boxes
- One topic per box
- All doses/steps typeset EXACTLY as supplied (no invented content)
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
Create TWO flat rectangular images for a clinician ACLS badge buddy (worn behind ID badge).

CRITICAL RULES:
- Landscape orientation (wider than tall)
- 4.5 x 2.75 inches each
- EXACTLY 2 rows x 3 columns grid
- One topic per box (6 total per image)
- Sharp corners only - NO rounded corners
- Solid colors only - NO gradients
- NO shadows, NO 3D effects
- This is FLAT PRINT ARTWORK, not a mockup
- Render doses and steps EXACTLY as written; do NOT invent or change anything

IMAGE 1 - FRONT (Rhythms/CPR):
Header: "ADULT ACLS / CODE BLUE - FRONT" (dark red)
Box 1: Shockable VF/pVT algorithm
Box 2: Non-shockable PEA/Asystole algorithm
Box 3: High-quality CPR parameters
Box 4: Defibrillation energy
Box 5: Rhythm check rules
Box 6: ROSC / post-arrest care
Footer: "Follow current guidelines and your code protocol - verify before use" (dark red)

IMAGE 2 - BACK (Drugs/Causes/Peri-arrest):
Header: "ADULT ACLS / CODE BLUE - BACK" (dark red)
Box 1: Code drugs (Epi, Amiodarone, Lidocaine)
Box 2: H's reversible causes
Box 3: T's reversible causes
Box 4: Symptomatic bradycardia
Box 5: Tachycardia with pulse
Box 6: Key reminders (adult ACLS only)
Footer: "Follow current guidelines and your code protocol - verify before use" (dark red)

(Replace example content with YOUR current guideline edition and code protocol before printing.)
If output has rounded corners or gradients, it is WRONG.
```

---

## Why This Prompt Works

This prompt uses the 8 proven print-ready image generation techniques (see [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md)):

1. **Terminology Steering** - "flat print artwork" instead of "card" to avoid UI associations
2. **Grid Forcing** - Explicit 2x3 grid with equal-sized boxes
3. **Enumerated Slots** - BOX 1, BOX 2, etc. keeps each algorithm's steps together and ordered
4. **Constraint Redundancy** - "no gradients" and "render content exactly" appear at multiple levels
5. **Negative Space Control** - Bans backgrounds, shadows, mockup staging (and rounded flowchart nodes)
6. **Physical Context** - "worn behind clinician's ID badge" anchors real-world usage
7. **Deliverables Locking** - "EXACTLY TWO IMAGES" with specific dimensions
8. **Validation Checklist** - Final self-audit block, including a no-invented-content check

---

## Anti-Fabrication / Clinical Content

**The image model RENDERS supplied clinical content. It does NOT generate medical facts.**

- The model must **not invent, guess, "improve," round, or correct** any drug dose, interval, energy setting, rhythm name, or algorithm step.
- All clinical content is **supplied by you** from the current guideline edition (e.g., AHA/ERC ACLS) and your institution's code policy.
- The EXAMPLE content is clearly labeled "EXAMPLE content shown — replace with your current guideline / code protocol." It reflects commonly-taught adult ACLS at authoring time and is provided only to make the template usable. **It is not a substitute for current certification or your code policy and must be confirmed/replaced.**
- This is an **adult ACLS** card. Do not reuse these doses or sequences for pediatric (PALS), neonatal (NRP), or obstetric arrest — those use different algorithms and weight-based dosing.
- Guidelines change. Re-verify against the current edition each time you reprint, and date the card.
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
Best-in-class text rendering for dense step lists and doses.
- Set `quality="high"` — required for legible 6.5-7.5 pt numbered steps and drug doses.
- The main prompt above maps cleanly onto its structure; keep the print constraints together as one block.
- `input_fidelity` is disabled in gpt-image-2 — do not pass it.
- Explicit grid enumeration and "if X appears, output is incorrect" language both work well.
- See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md) for full details.

### Nano Banana Pro (gemini-3-pro-image, recommended)
Near-perfect text rendering and exact-font control — strong for ordered algorithm steps.
- Name an exact font and weight (e.g., "Roboto Bold for topic titles; Roboto Regular for steps").
- Emphasize these are **flat print artwork** (ink-on-paper), not a flowchart UI mockup — the Thinking process otherwise biases toward realism/3D and rounded nodes.
- Use Markdown structure and ALL-CAPS `MUST`/`NEVER` for constraints; specify hex colors (`#8C1D1D`).
- Put the no-fabrication rule in a system prompt for consistency across re-generations.
- See [NANO_BANANA_GUIDE.md](../NANO_BANANA_GUIDE.md).

### DALL-E 3 (legacy)
Add: `"Graphic design flat lay, reference card design, typography-focused, print material, flat 2D"`. The dense ordered steps often exceed DALL-E 3's reliable rendering — prefer gpt-image-2 or Nano Banana Pro.

### Midjourney (legacy)
```
flat print artwork, clinician ACLS badge buddy, code blue reference,
2x3 grid layout, landscape format, clinical typography,
--ar 16:10 --v 6 --style raw --s 25
--no badge lanyard clip holder 3d mockup photo gradient shadow rounded corners
```
Note: Midjourney does not reliably render exact ordered text — verify every step or prefer a text-faithful model.

### Stable Diffusion (legacy)
Negative prompt: `"badge, lanyard, clip, holder, 3d, mockup, photo, gradient, shadow, rounded corners, depth, lighting, gloss, bevel, perspective"`. Not recommended for precise step/dose text.

---

## Troubleshooting

### Problem: Still getting mockups/3D renders or flowchart nodes
**Add:** `"Top-down flat view only. This IS the card surface. No flowchart nodes, no connectors with shadows. Plain numbered text lists only."`

### Problem: Rounded corners appearing
**Add:** `"Rounded corners = rendering error. All corners must be sharp 90-degree angles."`

### Problem: Doses, intervals, or step order altered/dropped
**Add:** `"Typeset every dose, interval, and step EXACTLY as written, in the given order. Do NOT change, round, reorder, or omit anything. If you cannot read a value, leave a blank line, do not invent one."` Then re-check the output against your source line-by-line.

### Problem: Content merged or reorganized
**Verify:** Each BOX assignment is explicit and numbered. Add: `"Do NOT combine topics. Do NOT reorganize. Follow BOX assignments exactly."`

### Problem: Gradients appearing
**Add:** `"SOLID colors ONLY. Any gradient in any element means the output is incorrect."`

### Problem: Only one image generated
**Add:** `"Generate EXACTLY 2 images. NOT 1. NOT 3. EXACTLY 2 separate images."`

---

## Verification Checklist (Before Printing)

- [ ] Every dose, interval, energy setting, and step cross-checked against the **current guideline edition (e.g., AHA/ERC ACLS) and your institutional code protocol** before printing
- [ ] Confirmed this is the correct population (adult ACLS — NOT PALS/NRP/obstetric)
- [ ] Drug doses and sequences match current code-cart standards
- [ ] Defibrillation energies match your specific defibrillator's device-recommended settings
- [ ] All EXAMPLE content replaced/confirmed against verified current sources
- [ ] No dose, interval, or step invented or altered by the image model (line-by-line comparison to source)
- [ ] Footer present: "Follow current guidelines and your code protocol - verify before use"
- [ ] Card dated with the guideline edition so it can be retired when guidelines update
- [ ] Two images, landscape, 2x3 grid, flat print artwork, no gradients/shadows/rounded corners
- [ ] Reviewed and approved by a qualified clinician (e.g., code-team lead / educator) before distribution

---

*Updated: 2026-06-23 — Print-ready adult ACLS/code-blue badge buddy with anti-fabrication and clinical-accuracy verification.*
