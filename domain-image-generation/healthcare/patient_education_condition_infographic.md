---
title: "Patient Education Condition Infographic - Image Generation Prompt"
category: medical-education
description: "Template-driven image generation prompt for a plain-language patient handout explaining a medical condition (what it is, symptoms, when to seek help). Low-health-literacy friendly: large type, simple icons, high contrast. The model renders clinician-supplied content only."
tags:
  - medical
  - patient-education
  - infographic
  - health-literacy
  - handout
  - plain-language
  - image-generation
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - ./patient_discharge_instructions_visual.md
  - ./patient_medication_guide_visual.md
  - ./patient_anatomy_explainer_diagram.md
  - ./pacu_infographic_image_prompt.md
---

# Patient Education Condition Infographic - Image Generation Prompt

**Purpose:** Generate a single-page, plain-language patient handout that explains a medical condition to a patient or caregiver: what it is, the common symptoms, how it is managed, and when to seek help. Designed for low health literacy — large legible type, short sentences, simple pictograms, high contrast.

> **Educational aid, not medical advice.** This handout is a teaching tool to support a conversation with a licensed clinician. It does not diagnose, treat, or replace professional medical advice. All clinical content must be supplied and approved by a clinician before patient distribution.

**Format:** 8.5 x 11 inch portrait handout, single side, 300 DPI (2550 x 3300 px), print-ready and screen-readable.

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core techniques used here
- [patient_discharge_instructions_visual.md](./patient_discharge_instructions_visual.md) — visual discharge sheet
- [patient_medication_guide_visual.md](./patient_medication_guide_visual.md) — how-to-take-your-medication visual
- [patient_anatomy_explainer_diagram.md](./patient_anatomy_explainer_diagram.md) — simple labeled anatomy diagram

---

## How To Use This Template

1. **Gather clinician-verified content.** Pull every fact (condition name, definition, symptoms, warning signs) from a vetted patient-education source (e.g., your institution's approved materials, MedlinePlus, a specialty society) and have a clinician confirm it.
2. **Fill the `[PLACEHOLDERS]`** in the prompt below with that content. Keep every line short.
3. **Generate** with your chosen model (see Model-Specific Notes — lead with gpt-image-2 or Nano Banana Pro for dense text).
4. **Route the output to a clinician for sign-off** before printing or sharing with any patient.

The EXAMPLE fill is illustrative only. **Do not ship the example content to a patient** — replace it.

---

## Image Generation Prompt (Production-Ready, Template)

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a one-page PATIENT EDUCATION HANDOUT that explains a medical condition in plain language.

IMPORTANT REAL-WORLD CONTEXT:
This is a patient handout.
It will be printed on plain paper and handed to a patient or caregiver.
The reader may have low health literacy and may be stressed or older.
It must be readable at arm's length with large type and high contrast.
Render ONLY the text and labels supplied below. Do not invent or add any medical facts.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT an illustration of a scene.

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
- NO lighting, gloss, bevel, or depth effects.
- NO background beyond the artwork edges.
- DO NOT add, change, or invent any medical content. Render the supplied text verbatim.

If any gradient, shadow, or rounded outer corner appears, the output is incorrect.
If any medical word, symptom, or instruction not listed below appears, the output is incorrect.

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

The page is divided into 5 stacked horizontal zones, full width, with thin solid gray separators (#9CA3AF, 1px):

ZONE 1 - TITLE BANNER (top, ~12% height)
- Solid fill: calm blue #1D4ED8
- White text, left-aligned:
  - Line 1 (bold, 40pt): "[CONDITION NAME IN PLAIN WORDS]"
  - Line 2 (regular, 20pt): "What you need to know"
- Sharp rectangular corners.

ZONE 2 - WHAT IT IS (~20% height)
- White background.
- Section heading (bold, 26pt, dark blue #1E3A8A): "What is it?"
- Body: 2 to 4 short sentences, regular 20pt, dark gray #111827.
  "[PLAIN-LANGUAGE DEFINITION SENTENCE 1]"
  "[PLAIN-LANGUAGE DEFINITION SENTENCE 2]"
- Optional simple line pictogram on the right (a single flat 2-color icon, no detail).

ZONE 3 - COMMON SYMPTOMS (~26% height)
- Very light blue background #EFF6FF.
- Section heading (bold, 26pt, dark blue #1E3A8A): "What you might feel"
- A vertical list of symptom items. EACH item = one simple flat pictogram on the left + short label text (20pt) on the right.
- Enumerate EXACTLY the symptoms supplied below, one per row, in order. Do not add or remove rows.
  SYMPTOM 1: "[SYMPTOM 1]"
  SYMPTOM 2: "[SYMPTOM 2]"
  SYMPTOM 3: "[SYMPTOM 3]"
  SYMPTOM 4: "[SYMPTOM 4]"

ZONE 4 - HOW IT IS MANAGED (~22% height)
- White background.
- Section heading (bold, 26pt, dark blue #1E3A8A): "How it is treated"
- Numbered list (large numerals in blue circles, label text 20pt):
  1. "[MANAGEMENT POINT 1]"
  2. "[MANAGEMENT POINT 2]"
  3. "[MANAGEMENT POINT 3]"

ZONE 5 - WHEN TO GET HELP (bottom, ~20% height)
- Solid fill: alert red #B91C1C with a thick red border (4px, #7F1D1D).
- Heading (bold, 28pt, white): "Call your doctor or get help if:"
- White text warning list, large (22pt), each on its own line with a white warning-triangle symbol:
  - "[WARNING SIGN 1]"
  - "[WARNING SIGN 2]"
  - "[WARNING SIGN 3]"
- Final line (bold, 22pt, white): "If it is an emergency, call [EMERGENCY NUMBER] now."

================================================
DESIGN SYSTEM (STRICT)
================================================

ALL SHAPES:
- Rectangular zones with sharp 90-degree corners.
- Solid fills only. No transparency. No gradients.

PICTOGRAMS (allowed, simple only):
- Flat, 2-color, single-line-weight icons (like public-signage pictograms).
- One concept per icon. No fine detail, no shading, no 3D.
- Icons illustrate ONLY the supplied label they sit beside. Do not invent new symptom icons.

TYPOGRAPHY:
- Clean, highly legible sans-serif (Arial, Open Sans, or Verdana).
- Title: 40pt bold. Section headings: 26-28pt bold. Body and list text: 20-22pt.
- Minimum text size anywhere: 18pt (large by design — low health literacy).
- High contrast only: dark text on light fill, white text on saturated fill. Minimum 7:1 contrast.
- Short lines. No paragraph longer than 4 short sentences.

================================================
HEALTH-LITERACY RULES (NON-NEGOTIABLE)
================================================

- Plain language at a 6th-grade reading level. Use everyday words.
- Short sentences (aim under 15 words each).
- One idea per line.
- No medical jargon unless the supplied text includes it with a plain-word explanation.
- Generous white space between zones.

================================================
CONSTRAINTS (REPEATED)
================================================

- NO gradients - solid colors only
- NO rounded outer corners on the page or banner
- NO shadows or depth effects
- NO mockup or device staging
- NO invented medical content of any kind
- All text 18pt or larger
- High contrast (minimum 7:1)
- Print-ready: CMYK, 300 DPI, 0.5 inch safe margin

================================================
VISUAL HIERARCHY
================================================

1. Primary attention: "When to get help" red zone and warning signs
2. Secondary attention: Title banner and section headings
3. Tertiary attention: Symptom list and management steps
4. Background: Zone fills, separators, pictograms

================================================
FINAL VALIDATION CHECK
================================================

- One image only
- Portrait orientation (taller than wide)
- 5 stacked full-width zones in order: Title, What is it, Symptoms, How treated, When to get help
- Large type (18pt minimum), high contrast
- Simple flat 2-color pictograms only
- Sharp rectangular corners
- Flat print artwork, solid colors, no gradients, no shadows
- Only the supplied medical text appears; nothing invented
- Bottom red "When to get help" zone is the most prominent block
```

---

## EXAMPLE Fill (Illustrative Only)

> **EXAMPLE — REPLACE WITH CLINICIAN-VERIFIED CONTENT.** The text below is a generic illustration so you can see how the template reads when filled. It is NOT validated for any patient and must not be distributed.

```
[CONDITION NAME IN PLAIN WORDS]  =>  "High Blood Pressure (Hypertension)"

WHAT IS IT?
- "Blood pressure is the force of blood pushing on the walls of your blood vessels."
- "When it stays too high over time, it can quietly damage your heart, brain, and kidneys."

WHAT YOU MIGHT FEEL (often there are NO symptoms):
SYMPTOM 1: "Most people feel nothing at all"
SYMPTOM 2: "Sometimes: headaches"
SYMPTOM 3: "Sometimes: feeling dizzy"
SYMPTOM 4: "Sometimes: blurry vision"

HOW IT IS TREATED:
1. "Take your blood pressure medicine every day, even when you feel fine."
2. "Eat less salt and more fruits and vegetables."
3. "Move your body and check your pressure as your doctor asks."

WHEN TO GET HELP:
- "Chest pain or trouble breathing"
- "Sudden weakness, numbness, or trouble speaking"
- "A very bad headache that will not go away"
Final line: "If it is an emergency, call 911 now."
```

---

## Simplified Fallback Prompt (If Full Prompt Misbehaves)

```
Create ONE flat rectangular patient handout, 8.5 x 11 inches PORTRAIT.

RULES:
- Sharp corners only - NO rounded corners
- Solid colors only - NO gradients, NO shadows
- FLAT PRINT ARTWORK, not a mockup
- Very large type (18pt+), high contrast, plain language (6th-grade level)
- Render ONLY the text I give you. Add NO medical facts.

ZONES top to bottom:
1. Blue title banner: "[CONDITION NAME]" + "What you need to know"
2. "What is it?" - 2 short sentences: [DEFINITION]
3. "What you might feel" (light blue): simple icon + label rows: [SYMPTOM 1-4]
4. "How it is treated": numbered steps: [STEP 1-3]
5. Red zone "Call your doctor or get help if:": [WARNING 1-3] + "If it is an emergency, call [NUMBER] now."

If output has rounded corners, gradients, or any medical text I did not supply, it is WRONG.
```

---

## Why This Prompt Works

1. **Terminology Steering (SV-11)** — "flat print artwork" / "patient handout" avoids UI-card tropes (rounded corners, shadows).
2. **Grid Forcing + Enumerated Slots (SV-12)** — 5 fixed stacked zones and numbered symptom/step slots prevent the model from reorganizing or merging content.
3. **Constraint Redundancy (SV-13)** — "no gradients" and "no invented medical content" appear in global rules, design system, and the final checklist.
4. **Negative Space Control (SV-14)** — solid white background, no staging, edge-to-edge page.
5. **Allowed vs. Forbidden Distinction (SV-15)** — simple flat 2-color pictograms allowed; detailed/3D illustration and any non-supplied content forbidden.
6. **Physical Context Anchoring (SV-16)** — "handed to a patient or caregiver, possibly low health literacy, stressed or older" drives large type and high contrast.
7. **Deliverables Locking (SV-17)** — EXACTLY ONE IMAGE, portrait, 8.5x11, 300 DPI.
8. **Validation Checklist (SV-18)** — final self-audit, including a content-fidelity check.

**Plus a health-literacy layer:** 6th-grade reading level, short one-idea-per-line sentences, 18pt minimum type, 7:1 contrast, and the most safety-critical block ("When to get help") given top visual weight.

See [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) for technique details.

---

## Anti-Fabrication / Clinical Content

**The image model must not be a source of medical truth.** Its only job is to typeset clinician-supplied content into a legible layout.

- **No invented facts.** The model must not add symptoms, causes, treatments, warning signs, statistics, or numbers that are not in the placeholder fill.
- **Verbatim rendering.** Supplied text is rendered as-is. If a model paraphrases clinical content, regenerate or correct it.
- **Source discipline.** Every fact you put in the placeholders should trace to an approved patient-education source and be confirmed by a clinician.
- **No diagnosis or personalization.** The handout is general education, not advice tailored to one patient's chart.
- **Reading-level integrity.** Plain-language rewrites of supplied content should still be clinician-checked — simplifying can accidentally change meaning.

---

## Model-Specific Notes

### gpt-image-2 (OpenAI, recommended for dense patient text)
- Set `quality="high"` — this handout is text-heavy and must be perfectly legible.
- Map the prompt onto the 5-section structure (Scene / Subject / Key Details / Use Case / Constraints): put the print + health-literacy rules under CONSTRAINTS.
- Do not pass `input_fidelity` (disabled in gpt-image-2).
- Strong adherence to "render only supplied text" — keep the anti-fabrication line near the top.
- See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md).

### Nano Banana Pro (Gemini 3 Pro Image, also recommended)
- Best-in-class text rendering for many short lines; name an exact font (e.g., "Verdana") for crisp typography.
- Use Markdown structure (headings, dashed lists) — the model parses it natively.
- Use a **system prompt** to lock "render only supplied text; add no medical facts" across regenerations.
- Optional Search grounding exists, but **disable reliance on it for clinical facts** — facts must come from your placeholders, not the web.

### DALL-E 3 (legacy)
Add: `"Plain-language patient education handout, flat 2D print material, large legible type, simple pictograms, no gradients."` Expect to fix minor text errors by hand.

### Midjourney (legacy)
```
flat print artwork, plain-language patient education handout, portrait poster,
large sans-serif type, simple flat pictograms, stacked color zones,
--ar 17:22 --v 6 --style raw --s 25
--no 3d mockup photo gradient shadow rounded corners device frame
```
Midjourney renders long exact text poorly — use only for layout exploration, then re-typeset.

### Stable Diffusion (legacy)
Negative prompt: `"photograph, 3d render, gradients, rounded corners, shadows, small text, dense paragraphs, decorative, watermark, device mockup"`
Not recommended for accurate dense text.

---

## Troubleshooting

### Problem: Model invents extra symptoms or advice
**Add:** `"Render ONLY the symptom and instruction lines I supplied. Any extra medical text = rendering error. Count the rows and match my list exactly."`

### Problem: Text too small / paragraphs too dense
**Add:** `"Increase type size. Minimum 18pt. One idea per line. Break long sentences. Add white space."`

### Problem: Getting a 3D mockup or device frame
**Add:** `"This IS the flat printed page, not a photo of a page on a screen or desk. No device, no hand, no shadow."`

### Problem: Rounded corners / gradients appear
**Add:** `"Sharp 90-degree corners only. Solid fills only. Any rounded corner or gradient = incorrect output."`

### Problem: Red 'When to get help' zone is not prominent
**Add:** `"The red help zone must be the most visually dominant block on the page, with the largest warning text."`

---

## Verification Checklist (Before Patient Distribution)

- [ ] **All medical content reviewed and approved by a clinician before patient distribution.**
- [ ] Every symptom, treatment point, and warning sign traces to an approved, current source.
- [ ] No fact appears that was not in the clinician-supplied fill (no model-invented content).
- [ ] Reading level is approximately 6th grade; sentences are short and jargon-free.
- [ ] All text is 18pt or larger and high-contrast.
- [ ] The "When to get help" / warning-signs block is present and most prominent.
- [ ] The correct local emergency number is shown.
- [ ] The handout states it is educational and not a substitute for professional medical advice.
- [ ] EXAMPLE content has been fully replaced (no placeholder/sample text remains).
- [ ] One portrait image, sharp corners, flat print, no gradients/shadows.

---

*Updated: 2026-06-23 — Tier-1 patient-education image-generation prompt with anti-fabrication and health-literacy guardrails.*
