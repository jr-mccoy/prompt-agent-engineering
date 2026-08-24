---
title: "Patient Anatomy Explainer Diagram - Image Generation Prompt"
category: medical-education
description: "Template-driven image generation prompt for a simple, patient-friendly labeled anatomy/body diagram to explain a procedure or condition. NOT a clinical-grade medical illustration. Large type, plain labels, high contrast. The model renders clinician-supplied labels only."
tags:
  - medical
  - patient-education
  - anatomy
  - diagram
  - health-literacy
  - plain-language
  - image-generation
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - ./patient_education_condition_infographic.md
  - ./patient_discharge_instructions_visual.md
  - ./patient_medication_guide_visual.md
  - ./pacu_infographic_image_prompt.md
---

# Patient Anatomy Explainer Diagram - Image Generation Prompt

**Purpose:** Generate a simple, friendly labeled body diagram to help a patient understand a procedure or condition ("here is your knee, and here is where the surgeon will work"). This is a **plain-language teaching diagram, not a clinical-grade or anatomically exhaustive medical illustration.** Built for low health literacy — clean simplified shapes, large plain-word labels, high contrast, minimal detail.

> **Educational aid, not medical advice.** This diagram is a simplified teaching aid to support a conversation with a licensed clinician. It is intentionally not anatomically precise and must not be used for clinical decision-making, measurement, or as a substitute for professional medical advice. All labels and the depicted region must be specified and approved by a clinician before patient use.

**Format:** 8.5 x 11 inch portrait handout, single side, 300 DPI (2550 x 3300 px), print-ready and screen-readable.

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core techniques used here
- [patient_education_condition_infographic.md](./patient_education_condition_infographic.md) — condition explainer (pair this diagram with it)
- [patient_discharge_instructions_visual.md](./patient_discharge_instructions_visual.md) — discharge sheet
- [patient_medication_guide_visual.md](./patient_medication_guide_visual.md) — medication guide

---

## How To Use This Template

1. **Decide the region and the labels** with the clinician: which body part to show, which 3-8 structures to label in plain words, and the one spot to highlight (the procedure/condition site).
2. **Fill the `[PLACEHOLDERS]`** below. Labels must be plain-language and clinician-approved.
3. **Generate** (see Model-Specific Notes — gpt-image-2 or Nano Banana Pro first for clean labels).
4. **Have a clinician confirm** the diagram is correct enough for teaching (right region, labels point to the right place, nothing misleading) before showing it to a patient.

The EXAMPLE fill is illustrative only. **Replace it** before any real use.

> **Why "simple, not clinical-grade"?** Image models cannot be trusted to render anatomically accurate internal structures. We deliberately constrain the output to a simplified, schematic, low-detail diagram whose only job is to orient the patient. Accuracy comes from the clinician-chosen labels and highlight, not from the model's anatomy knowledge.

---

## Image Generation Prompt (Production-Ready, Template)

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a SIMPLE, FRIENDLY, LABELED BODY DIAGRAM to help a patient understand a procedure or condition.

IMPORTANT REAL-WORLD CONTEXT:
This is a patient teaching diagram.
It is printed on plain paper and used while a clinician explains something to a patient or caregiver.
The reader may have low health literacy.
This is a SIMPLIFIED, schematic diagram - NOT a clinical-grade or photorealistic medical illustration.
Render ONLY the labels supplied below. Do not invent extra structures, labels, or medical text.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT a textbook anatomical plate.

This image represents the literal ink-on-paper artwork sent directly to a printer.

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY ONE IMAGE.
- The image must be a SINGLE flat rectangle.
- Orientation: PORTRAIT (taller than wide).
- NO rounded outer corners on the page.
- NO drop shadows.
- NO gradients of any kind.
- NO lighting, gloss, bevel, or depth/3D effects.
- NO background beyond the artwork edges.
- The diagram must be SIMPLE and SCHEMATIC: clean flat shapes, flat solid colors, thin outlines.
- DO NOT add, change, or invent any anatomy, labels, or medical content. Use ONLY the supplied labels.

If any gradient, shadow, rounded outer corner, or 3D/photoreal rendering appears, the output is incorrect.
If any anatomical label or structure not listed below appears, the output is incorrect.

================================================
PHYSICAL SIZE & CANVAS
================================================

Size:
- 8.5 inches wide x 11 inches tall (portrait)
- Resolution: 2550 x 3300 px at 300 DPI
- Edge-to-edge artwork (this IS the printed page)

Background:
- Solid white (#FFFFFF) ONLY
- No texture, no vignette, no fade

Margins:
- Safe zone: 0.5 inch margin from all edges (keep all text inside)

================================================
LAYOUT ZONES (TOP TO BOTTOM) - MOST IMPORTANT
================================================

ZONE 1 - TITLE BANNER (top, ~10% height)
- Solid fill: calm teal #0F766E
- White text, left-aligned:
  - Line 1 (bold, 36pt): "Understanding [BODY PART / PROCEDURE / CONDITION, plain words]"
- Sharp rectangular corners.

ZONE 2 - DIAGRAM AREA (center, ~62% height)
- Solid white background.
- ONE simplified, schematic, flat illustration of: "[BODY REGION TO DRAW, e.g. 'a right knee, side view']"
- Style: clean cartoon-simple, flat fills, thin dark outlines, friendly and non-graphic. NO blood, NO open wounds, NO photoreal tissue.
- View/orientation: "[VIEW, e.g. 'side view, facing right']"
- LABELS: draw a thin straight leader line from each label to the structure it names. Labels are plain-language text (20pt). Use EXACTLY these labels, no more, no less:
  LABEL 1: "[PLAIN LABEL 1]"  -> points to "[WHAT IT POINTS TO]"
  LABEL 2: "[PLAIN LABEL 2]"  -> points to "[WHAT IT POINTS TO]"
  LABEL 3: "[PLAIN LABEL 3]"  -> points to "[WHAT IT POINTS TO]"
  LABEL 4: "[PLAIN LABEL 4]"  -> points to "[WHAT IT POINTS TO]"
- HIGHLIGHT: mark ONE spot clearly (a flat solid colored shape or simple star/arrow in orange #EA580C) at:
  "[HIGHLIGHT LOCATION, e.g. 'the inner side of the knee where the surgeon will work']"
  with a short callout label (bold, 20pt): "[HIGHLIGHT LABEL, e.g. 'Surgery area']"

ZONE 3 - PLAIN EXPLANATION (~18% height)
- Very light teal background #F0FDFA.
- Heading (bold, 24pt, dark teal #115E59): "What this shows"
- 2 to 4 short sentences (regular 20pt):
  "[PLAIN-LANGUAGE EXPLANATION SENTENCE 1]"
  "[PLAIN-LANGUAGE EXPLANATION SENTENCE 2]"

ZONE 4 - FOOTER NOTE (bottom, ~10% height)
- Light gray background #F3F4F6.
- Text (italic, 16pt, dark gray #374151):
  "This is a simple drawing to help explain things. It is not exact. Ask your care team any questions."

================================================
DESIGN SYSTEM (STRICT)
================================================

DIAGRAM STYLE (allowed):
- Simplified, schematic, flat 2-color or few-color shapes.
- Thin consistent dark outlines.
- Friendly, calm, non-graphic. Suitable for a nervous patient.

DIAGRAM STYLE (forbidden):
- NO photorealism, NO 3D rendering, NO shading/gradients.
- NO blood, gore, open wounds, or distressing detail.
- NO dense textbook-level internal anatomy.
- NO extra structures or labels beyond those supplied.

LABELS & LEADER LINES:
- Thin straight or simple elbow leader lines, dark gray.
- Each label points to exactly one structure. No crossing leader lines if avoidable.

TYPOGRAPHY:
- Clean legible sans-serif (Arial, Open Sans, or Verdana).
- Title: 36pt bold. Headings: 24pt bold. Labels/body: 20pt. Footer: 16pt.
- Minimum text size anywhere: 16pt.
- High contrast (minimum 7:1).

================================================
HEALTH-LITERACY RULES (NON-NEGOTIABLE)
================================================

- Plain-language labels at a 6th-grade reading level (use the supplied plain words, not Latin terms unless supplied).
- Short explanation sentences (aim under 15 words).
- Few labels (3 to 8) so the diagram stays uncluttered.
- One clearly highlighted "this is the spot" focus point.
- Generous white space around the diagram.

================================================
CONSTRAINTS (REPEATED)
================================================

- NO gradients - solid flat colors only
- NO rounded outer corners on the page
- NO shadows, 3D, or photoreal rendering
- NO blood, wounds, or graphic detail
- NO invented anatomy or labels; use only the supplied labels
- All text 16pt or larger
- High contrast (minimum 7:1)
- Print-ready: CMYK, 300 DPI, 0.5 inch safe margin

================================================
VISUAL HIERARCHY
================================================

1. Primary attention: The simplified diagram and its highlighted focus spot
2. Secondary attention: Title banner and plain labels
3. Tertiary attention: "What this shows" explanation
4. Background: Zone fills, footer disclaimer

================================================
FINAL VALIDATION CHECK
================================================

- One image only
- Portrait orientation (taller than wide)
- 4 zones in order: Title, Diagram, "What this shows", Footer note
- Diagram is SIMPLE/schematic/flat - not photoreal, not 3D, no blood
- Exactly the supplied labels appear, each on a leader line; nothing invented
- One clear orange highlight at the supplied focus spot
- Large plain-language type (16pt minimum), high contrast
- Sharp rectangular corners, flat print, solid colors, no gradients/shadows
- Footer disclaimer ("simple drawing... not exact") is present
```

---

## EXAMPLE Fill (Illustrative Only)

> **EXAMPLE — REPLACE WITH CLINICIAN-VERIFIED CONTENT.** Generic illustration only. Intentionally simplified and not anatomically exact; must not be distributed.

```
TITLE: "Understanding Your Knee Surgery"

DIAGRAM AREA:
[BODY REGION TO DRAW] = "a right knee, side view, simplified"
[VIEW] = "side view, facing right"
LABEL 1: "Thigh bone"      -> points to the upper bone
LABEL 2: "Kneecap"         -> points to the front of the joint
LABEL 3: "Shin bone"       -> points to the lower bone
LABEL 4: "Cushion (cartilage)" -> points to the space between the bones
HIGHLIGHT: orange star at "the inside of the knee joint"
HIGHLIGHT LABEL: "Surgery area"

WHAT THIS SHOWS:
- "Your knee is where your thigh bone and shin bone meet."
- "The surgeon will work at the orange spot to repair the cushion."

FOOTER NOTE (fixed text):
"This is a simple drawing to help explain things. It is not exact. Ask your care team any questions."
```

---

## Simplified Fallback Prompt (If Full Prompt Misbehaves)

```
Create ONE flat rectangular patient teaching diagram, 8.5 x 11 inches PORTRAIT.

RULES:
- Sharp corners only - NO rounded corners
- Solid flat colors only - NO gradients, NO shadows, NO 3D, NO photorealism, NO blood
- FLAT PRINT ARTWORK, not a mockup or textbook plate
- SIMPLE schematic drawing only (clean shapes, thin outlines)
- Large plain-language labels (16pt+), high contrast
- Render ONLY the labels I give you. Add NO extra anatomy or labels.

ZONES top to bottom:
1. Teal title banner: "Understanding [BODY PART/PROCEDURE]"
2. Diagram: simple flat drawing of [BODY REGION], [VIEW]; leader-line labels: [LABEL 1-4]; ONE orange highlight at [SPOT] labeled "[HIGHLIGHT LABEL]"
3. "What this shows": 2 short sentences [EXPLANATION]
4. Gray footer (fixed): "This is a simple drawing to help explain things. It is not exact. Ask your care team any questions."

If output is photoreal/3D, shows blood, has rounded corners or gradients, or adds any label I did not supply, it is WRONG.
```

---

## Why This Prompt Works

1. **Terminology Steering (SV-11)** — "flat print artwork" / "simple teaching diagram" and an explicit "NOT a textbook anatomical plate / NOT photorealistic" steer away from both UI tropes and over-detailed (and likely inaccurate) medical illustration.
2. **Grid Forcing + Enumerated Slots (SV-12)** — 4 fixed zones and enumerated LABEL slots (with what each points to) keep the diagram uncluttered and stop the model from inventing structures.
3. **Constraint Redundancy (SV-13)** — "no gradients," "simple/schematic, not photoreal," and "no invented anatomy" repeat across global rules, design system, and checklist.
4. **Negative Space Control (SV-14)** — solid white background, generous white space, edge-to-edge.
5. **Allowed vs. Forbidden Distinction (SV-15)** — explicitly lists allowed style (flat schematic, thin outlines) vs. forbidden (photoreal, 3D, blood, dense anatomy, extra labels). This is the load-bearing technique for keeping the diagram patient-friendly and non-misleading.
6. **Physical Context Anchoring (SV-16)** — "used while a clinician explains... reader may be nervous, low health literacy" drives simplicity, calm style, and few labels.
7. **Deliverables Locking (SV-17)** — EXACTLY ONE IMAGE, portrait, 8.5x11, 300 DPI.
8. **Validation Checklist (SV-18)** — final self-audit including a "simple/schematic, only supplied labels" check.

**Plus a health-literacy layer:** plain-word labels, 3-8 labels max to avoid clutter, one clear highlight ("this is the spot"), 16pt minimum type, and a permanent footer disclaimer telling the patient the drawing is simplified and to ask questions.

See [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md).

---

## Anti-Fabrication / Clinical Content

**Image models do not have reliable anatomical accuracy — this prompt is built around that limitation.**

- **Simplified by design.** The diagram is schematic, not precise. It exists to orient a patient, never to inform clinical decisions, measurements, or surgical planning.
- **Labels come from the clinician.** The model must use only the supplied plain-language labels and must not add, rename, or relabel structures.
- **No invented anatomy.** The model must not add extra organs, vessels, nerves, or structures "to look complete."
- **Clinician verifies placement.** A clinician must confirm the region is correct and that each label/highlight points to roughly the right place before patient use. If a leader line points to the wrong structure, regenerate.
- **Non-graphic.** No blood, wounds, or distressing detail — appropriate for a nervous or pediatric-caregiver audience.
- **Footer disclaimer is mandatory** and must read that the drawing is simple, not exact, and that the patient should ask their care team.

---

## Model-Specific Notes

### gpt-image-2 (OpenAI, recommended)
- Set `quality="high"` for clean labels and crisp leader lines.
- Map onto the 5-section structure (Scene / Subject / Key Details / Use Case / Constraints); put the "simple/schematic, not photoreal, only supplied labels" rules under CONSTRAINTS.
- Do not pass `input_fidelity` (disabled in gpt-image-2).
- Strong at honoring "simplified, flat, no photorealism" when stated explicitly and repeated.
- See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md).

### Nano Banana Pro (Gemini 3 Pro Image, also recommended)
- Excellent label text rendering; name a font (e.g., "Verdana") and keep labels short.
- Note the documented **realism bias** (its Thinking step pushes toward realism) — counter it: repeat "simple, flat, schematic, NOT photorealistic, NO 3D" and add it to a **system prompt**.
- Do not rely on Search grounding for anatomy — use only the supplied labels.

### DALL-E 3 (legacy)
Add: `"Simple flat schematic patient anatomy diagram, friendly cartoon-simple style, thin outlines, plain-language labels, no photorealism, no 3D, no blood, no gradients."` Verify label placement by hand.

### Midjourney (legacy)
```
flat print artwork, simple schematic patient anatomy diagram, friendly clean line style,
plain-language labels with leader lines, single highlighted area, portrait,
--ar 17:22 --v 6 --style raw --s 25
--no photorealistic 3d render blood gore textbook gradient shadow rounded corners device frame
```
Midjourney tends toward stylized realism — strong negatives needed; treat as exploratory.

### Stable Diffusion (legacy)
Negative prompt: `"photograph, photorealistic, 3d render, blood, gore, wound, dense anatomy, gradients, rounded corners, shadows, small text, watermark, device mockup"`
Hard to control label accuracy — use only with heavy clinician review.

---

## Troubleshooting

### Problem: Output is photoreal or 3D
**Add:** `"Simple flat schematic drawing only. Clean shapes, thin outlines, flat colors. NOT photorealistic. NOT 3D. NOT a textbook plate."`

### Problem: Model adds extra structures or labels
**Add:** `"Use ONLY my supplied labels. Count them. Do not add any organ, vessel, nerve, or label I did not list."`

### Problem: Diagram looks graphic or shows blood
**Add:** `"No blood, wounds, or graphic detail. Calm, friendly, reassuring. Suitable for a nervous patient."`

### Problem: Leader lines cross or point to the wrong spot
**Add:** `"Each label connects by a thin straight line to exactly one structure. Avoid crossing lines. Place each label near the part it names."`

### Problem: Highlight not clear
**Add:** `"Mark the focus spot with ONE bold orange shape or star and a short label. It should be the most eye-catching part of the diagram."`

### Problem: Rounded corners / gradients
**Add:** `"Sharp 90-degree page corners only. Solid flat fills only. Any gradient or rounded corner = incorrect."`

---

## Verification Checklist (Before Patient Distribution)

- [ ] **All medical content (region, labels, highlight, explanation) reviewed and approved by a clinician before patient use.**
- [ ] The diagram shows the correct body region and view.
- [ ] Each supplied label points to roughly the correct structure; no leader line is misleading.
- [ ] Only the supplied labels appear — no model-invented anatomy or text.
- [ ] The single highlight marks the intended procedure/condition spot.
- [ ] Style is simplified/schematic — not photoreal, not 3D, no blood or graphic detail.
- [ ] Labels are plain-language at ~6th-grade level; 3-8 labels max (uncluttered).
- [ ] All text is 16pt or larger and high-contrast.
- [ ] The footer disclaimer ("simple drawing... not exact... ask your care team") is present.
- [ ] The handout states it is an educational aid, not anatomically exact, and not a substitute for professional medical advice.
- [ ] EXAMPLE content has been fully replaced.
- [ ] One portrait image, sharp corners, flat print, no gradients/shadows.

---

*Updated: 2026-06-23 — Tier-1 patient-education image-generation prompt with anti-fabrication and health-literacy guardrails; deliberately constrained to simple, non-clinical-grade schematic diagrams.*
