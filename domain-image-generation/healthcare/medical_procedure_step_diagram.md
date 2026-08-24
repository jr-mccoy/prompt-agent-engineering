---
title: "Step-by-Step Illustrated Procedure Diagram - Image Generation Prompt"
category: medical-education
description: "Template-driven image generation prompt for creating an enumerated, step-by-step illustrated clinical procedure sequence (e.g., sterile technique, device insertion) where the user supplies every step from expert-verified sources"
tags:
  - medical
  - procedure
  - diagram
  - step-by-step
  - sterile-technique
  - skills-training
  - image-generation
updated: "2026-06-23"
---

# Step-by-Step Illustrated Procedure Diagram - Image Generation Prompt

**Purpose:** Generate a clean, flat, enumerated step-by-step procedure diagram (e.g., hand hygiene, sterile gloving, IV/central-line insertion, foley insertion, wound dressing) for skills training. Each panel illustrates one step; all step content and order come ONLY from expert-verified source material. The image model lays out and renders supplied steps — it does not invent steps, sequence, or technique.

**Format:** Single flat print artwork, panel sequence (default 2 columns x N rows, landscape or portrait), skills-lab poster / handout / slide ready (default 2400 x 3000 px portrait at 300 DPI; adjustable).

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core techniques used in this prompt
- [medical_anatomy_physiology_diagram.md](medical_anatomy_physiology_diagram.md) — labeled anatomy/physiology diagrams
- [medical_pathophysiology_mechanism_diagram.md](medical_pathophysiology_mechanism_diagram.md) — disease-mechanism flow diagrams
- [medical_clinical_algorithm_flowchart.md](medical_clinical_algorithm_flowchart.md) — clinical decision / triage flowcharts
- [pacu_infographic_image_prompt.md](pacu_infographic_image_prompt.md) — clinical workflow infographic

---

> ⚠️ **MEDICAL-SAFETY NOTICE — READ BEFORE USE**
> Image models are **NOT clinically or anatomically reliable.** They invent steps, drop critical safety actions, depict wrong technique, and render hands/devices incorrectly. This prompt is a **layout-and-rendering tool**, not a source of clinical procedure truth. **Every step, its order, and the depicted technique must be supplied by the user from expert-verified sources (institutional protocol, current clinical guideline, vetted skills curriculum) and must be checked by a subject-matter expert (clinician, educator, infection-prevention/skills-lab specialist) before any instructional use.** For high-stakes or clinical-grade illustration (competency assessment, accredited training, patient-facing), commission a **professional medical illustrator** and validate against the governing protocol.

---

## Image Generation Prompt (Production-Ready) — TEMPLATE

Replace every `[PLACEHOLDER]` with your own expert-verified content before generating. A worked EXAMPLE follows the template.

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a step-by-step illustrated procedure diagram for [PROCEDURE — e.g., "sterile gloving"].

IMPORTANT REAL-WORLD CONTEXT:
This is a skills-training reference for [AUDIENCE — e.g., "nursing students in a skills lab"].
It is printed as a poster / handout or shown on a slide.
It must show a clear ordered sequence with one step per panel.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT a photorealistic clinical photo.
This image represents flat, labeled, panel-based instructional artwork.

CONTENT AUTHORITY (CRITICAL):
- Render ONLY the steps listed below, in EXACTLY the order given.
- Do NOT invent, add, merge, reorder, or omit any step.
- Do NOT add technique details, equipment, or safety actions not explicitly listed.
- If a step cannot be illustrated faithfully, render the step's panel with its number and text plus a callout "ILLUSTRATION PENDING EXPERT VERIFICATION" rather than guessing the depiction.

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY ONE IMAGE.
- The image must be a SINGLE flat rectangle.
- Orientation: [PORTRAIT / LANDSCAPE].
- NO rounded outer corners (panels may use sharp 90-degree corners only).
- NO drop shadows.
- NO gradients (flat color fills only).
- NO photorealistic rendering of skin, hands, blood, or wounds.
- NO background scene beyond the artwork edges.

If any gradient, shadow, photorealistic render, reordered step, or invented step appears, the output is incorrect.

================================================
PHYSICAL SIZE & CANVAS
================================================

- Size: [WIDTH] x [HEIGHT] inches (default 8 x 10 portrait)
- Resolution: [PIXELS] at 300 DPI (default 2400 x 3000 px)
- Background: Solid white (#FFFFFF) ONLY. No texture, vignette, or fade.

================================================
PANEL GRID LAYOUT (MOST IMPORTANT)
================================================

- EXACTLY [N] PANELS arranged in a [ROWS] x [COLUMNS] grid (e.g., 3 rows x 2 columns = 6 panels).
- ONE STEP PER PANEL.
- ALL PANELS: equal width, equal height, evenly spaced, perfectly aligned, sharp corners.
- Panels read in order: [READING ORDER — e.g., "left-to-right, top-to-bottom"].
- Each panel contains, top-to-bottom:
  1. A bold step number badge: "STEP 1", "STEP 2", ...
  2. A simple flat illustration of that step (schematic, not photorealistic).
  3. A short instruction caption (the step text, verbatim from the list).
- A directional arrow (simple solid triangle) between consecutive panels showing flow.

================================================
ENUMERATED STEPS (RENDER EXACTLY THESE, IN ORDER — NO MORE, NO LESS)
================================================

STEP 1: [verbatim step text] | Illustrate: [what the panel should show]
STEP 2: [verbatim step text] | Illustrate: [what the panel should show]
STEP 3: [verbatim step text] | Illustrate: [what the panel should show]
STEP 4: [verbatim step text] | Illustrate: [what the panel should show]
STEP 5: [verbatim step text] | Illustrate: [what the panel should show]
STEP 6: [verbatim step text] | Illustrate: [what the panel should show]
[continue for every step — number them all; the panel count MUST equal the step count]

DO NOT add any step not in this list.
DO NOT reorder, merge, or omit any step.

================================================
TITLE, KEY-POINTS & WARNING (OPTIONAL BUT RECOMMENDED)
================================================

- Top title band (solid [HEX], white text): "[PROCEDURE NAME] — Step by Step"
- Optional "KEY POINTS" strip (verbatim from your list): [short critical reminders]
- Optional "SAFETY / STERILITY" callout (red band) with verbatim warnings: [warnings]

================================================
TYPOGRAPHY
================================================

- Title: bold, ~22 pt
- Step number badge: bold, ~14 pt
- Caption text: regular, ~11-13 pt, minimum 10 pt
- Clean clinical sans-serif (Roboto, Open Sans, or similar)
- High contrast dark text on light panels

================================================
DESIGN SYSTEM (STRICT)
================================================

- Solid fills only, no gradients, no transparency.
- Sharp 90-degree corners on all panels, bands, and badges.
- Illustration style: simple flat schematic line art with solid color fills (gloves, tray, catheter, hands shown as clean shapes — NOT photoreal).
- Allowed graphic elements: panels, step badges, schematic illustrations, captions, directional arrows, title/key-points/warning bands.
- Forbidden: photographic content, 3D depth, glossy realism, gore/graphic wound realism, decorative scenery, watermark text, invented or reordered steps.

================================================
FINAL VALIDATION CHECK
================================================

- One image only
- [Orientation] orientation
- Panel count EXACTLY equals the step count (count them)
- Steps in the exact listed order, none invented, none omitted, none merged
- One step per panel, equal-sized panels, sharp corners
- Directional arrows show correct flow
- Flat schematic artwork, solid fills only
- No gradients, no shadows, no rounded outer corners
- No photorealistic skin/hands/wounds
- Title present; key-points/warning bands present if specified
```

---

## EXAMPLE FILL — REPLACE WITH EXPERT-VERIFIED CONTENT

> The following is an **illustrative example only**, to show the shape of a completed template. **Do not treat these steps as authoritative or complete.** Confirm every step, its order, and the technique against your institution's current protocol, and have a subject-matter expert review before instructional use.

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a step-by-step illustrated procedure diagram for HAND HYGIENE (alcohol-based hand rub).

AUDIENCE: nursing students in a skills lab. Printed as a wall poster.

PANEL GRID: EXACTLY 6 PANELS in a 3 rows x 2 columns grid, read left-to-right, top-to-bottom.

ENUMERATED STEPS (EXAMPLE — VERIFY AGAINST YOUR PROTOCOL/GUIDELINE):
STEP 1: Apply a palmful of product to cupped hands | Illustrate: hand dispensing rub into cupped palm
STEP 2: Rub hands palm to palm | Illustrate: two palms together
STEP 3: Rub palm over back of each hand, fingers interlaced | Illustrate: palm over opposite hand back
STEP 4: Rub palm to palm with fingers interlaced | Illustrate: interlaced fingers
STEP 5: Rub backs of fingers against opposing palms | Illustrate: backs of fingers in opposite palm
STEP 6: Rub each thumb clasped in opposite palm; rub until dry | Illustrate: rotational thumb rub

TITLE: "HAND HYGIENE — Step by Step"
KEY POINTS: "Cover all surfaces; continue until hands are dry."
SAFETY CALLOUT (red): "EXAMPLE — REPLACE WITH EXPERT-VERIFIED CONTENT. Follow current institutional protocol."

[All CRITICAL OUTPUT RULES, DESIGN SYSTEM, and FINAL VALIDATION CHECK from the template above still apply.]
```

---

## Simplified Prompt (If Full Prompt Misbehaves)

```
Create ONE flat, step-by-step illustrated procedure diagram for [PROCEDURE].

CRITICAL RULES:
- [Portrait/Landscape], white background, [N] equal panels in a [R x C] grid, one step per panel
- Each panel: "STEP n" badge + simple flat schematic illustration + verbatim caption
- Arrows between panels in reading order
- Sharp corners, NO gradients, NO shadows, NO photorealistic skin/hands/wounds
- This is a FLAT TRAINING DIAGRAM, not a mockup or clinical photo

RENDER ONLY THESE STEPS, IN ORDER (do not invent, reorder, merge, or omit):
1. [STEP] 2. [STEP] 3. [STEP] 4. [STEP] 5. [STEP] 6. [STEP]

Title bar: "[PROCEDURE] — Step by Step".
If panels ≠ steps, or steps are reordered/invented, it is WRONG.
```

---

## Why This Prompt Works

This prompt applies the 8 core techniques from [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md):

1. **Terminology Steering** — "flat panel-based instructional artwork" instead of "render"/"photo," steering away from photorealistic clinical imagery.
2. **Grid Forcing + Enumerated Slots** — explicit panel grid plus the **enumerated STEP list**; panel count must equal step count, locking sequence and preventing dropped or invented steps.
3. **Constraint Redundancy** — "no invented/reordered steps," "no gradients," "no photorealism" repeat in the content-authority block, design system, and validation check.
4. **Negative Space Control** — solid white background, no scene, no depth.
5. **Allowed vs. Forbidden Distinction** — allows panels, badges, schematic illustrations, arrows; forbids photographic content, gore realism, and reordered steps.
6. **Physical Context Anchoring** — "skills-lab poster/handout for [audience]" sets density and reading flow.
7. **Deliverables Locking** — EXACTLY ONE IMAGE, locked orientation/dimensions, locked panel count = step count.
8. **Validation Checklist** — final self-audit including a panel-vs-step count check.

---

## Anti-Fabrication / Expert-Review Section

**Why this matters most for procedures:** A dropped or reordered step in a sterile or insertion procedure is a patient-safety hazard. Image models silently merge steps, omit safety actions (e.g., a pause/timeout, a sterility check), and depict incorrect technique with convincing polish.

**Rules enforced by this prompt:**
- The model renders **only** the enumerated steps, **in order**; panel count must equal step count.
- Steps must not be merged, reordered, or invented.
- Un-illustratable steps become a flagged placeholder, never a guessed depiction.
- No photorealism (which can make wrong technique look authoritative).

**Required workflow:**
1. Source every step and its order from the governing protocol / current guideline / vetted skills curriculum.
2. Fill the template verbatim; mark uncertain depictions explicitly.
3. Generate.
4. **Expert review (mandatory):** a clinician/educator/skills-lab or infection-prevention specialist confirms step content, order, completeness (no missing safety/sterility actions), and depicted technique.
5. For competency assessment, accredited training, or patient-facing use, route to a **professional medical illustrator** and validate against the protocol.

**Verification Checklist (complete before instructional use):**
- [ ] Every step was sourced from an expert-verified protocol/guideline (not the model)
- [ ] Panel count equals step count; steps appear in the correct order
- [ ] No step merged, omitted, reordered, or invented
- [ ] No critical safety/sterility step is missing
- [ ] Depicted technique matches the governing protocol
- [ ] No photorealistic or graphic/gore rendering
- [ ] Captions match the source step text verbatim
- [ ] **Steps, order, and depicted technique verified by a subject-matter expert before instructional use**
- [ ] For high-stakes/clinical-grade use: professional medical illustrator engaged

---

## Model-Specific Notes

For step diagrams, **text-caption accuracy and reliable panel layout are the key model differentiators.** Lead with the models strongest at in-image text and multi-panel grids.

### gpt-image-2 (OpenAI, flagship) — RECOMMENDED for step diagrams
- Set `quality="high"` for legible step badges and captions.
- Map to the 5-section structure (Scene / Subject / Key Details / Use Case / Constraints): enumerated steps under Key Details, print/anti-fabrication block under Constraints.
- Strong at multi-panel layouts with distinct text per panel — well suited to 4–9 step grids.
- Do NOT pass `input_fidelity` (disabled). See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md).

### Nano Banana Pro (gemini-3-pro-image) — RECOMMENDED for step diagrams
- Near-perfect text rendering and native grid/multi-image layout (2x2, etc.) — ideal for panel sequences.
- Use a **system prompt** to lock "flat schematic panels, one step each, no photorealism, no reordering" across regenerations.
- Markdown-structured prompts parse natively; keep the enumerated step list intact.

### DALL-E 3 (legacy)
Add: `"Instructional step-by-step diagram, numbered flat panels, schematic line art, clear captions, no photorealism, white background"`. May struggle to keep panel count and captions exact — verify count and order.

### Midjourney (legacy)
```
flat step-by-step procedure diagram, [PROCEDURE], numbered panels in a grid, schematic line art,
flat color fills, clear captions, directional arrows, white background,
--ar 4:5 --v 6 --style raw --s 25
--no photorealistic 3d gloss shadow gradient rounded corners gore scenery
```
Note: Midjourney garbles in-image text and rarely respects exact panel counts — best for illustrations, with numbering/captions added in a layout tool.

### Stable Diffusion (legacy)
Negative prompt: `"photograph, 3d render, realistic skin, blood, gore, blurry, gradient, shadow, rounded corners, scenery, watermark, garbled text, merged panels"`. Poor at exact panels/captions — expect to assemble the sequence manually.

---

## Troubleshooting

### Problem: Steps dropped, merged, or reordered
**Add:** `"Panel count MUST equal the number of steps. Render every step, in the exact listed order, one per panel. Merging or reordering is a rendering error."`

### Problem: Photorealistic / graphic depiction
**Add:** `"Flat schematic line art ONLY. NOT a photo. NOT photorealistic. Hands, gloves, and devices are clean flat shapes, no realistic skin or blood."`

### Problem: Captions garbled or not matching source text
**Switch model** to gpt-image-2 or Nano Banana Pro, or add captions in a layout tool. Also: `"Each caption must read EXACTLY as written. Do not paraphrase."`

### Problem: Wrong reading order / arrows missing
**Add:** `"Panels read [order]. Add a solid arrow between each consecutive panel showing the flow."`

### Problem: Extra equipment or technique appears
**Add:** `"Show ONLY what each step's 'Illustrate' note specifies. Do not add equipment, steps, or actions not listed."`

---

*Updated: 2026-06-23 — Template-driven; step content, order, and technique require expert verification (image models are not clinically reliable).*
