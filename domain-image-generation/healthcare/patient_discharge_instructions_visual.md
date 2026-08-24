---
title: "Patient Discharge Instructions Visual Sheet - Image Generation Prompt"
category: medical-education
description: "Template-driven image generation prompt for a visual discharge-instructions handout (medications, activity, follow-up, and warning signs / when to call). Low-health-literacy friendly: large type, simple icons, high contrast. The model renders clinician-supplied content only."
tags:
  - medical
  - patient-education
  - discharge-instructions
  - health-literacy
  - handout
  - plain-language
  - image-generation
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - ./patient_education_condition_infographic.md
  - ./patient_medication_guide_visual.md
  - ./patient_anatomy_explainer_diagram.md
  - ./pacu_infographic_image_prompt.md
---

# Patient Discharge Instructions Visual Sheet - Image Generation Prompt

**Purpose:** Generate a single-page visual discharge sheet a patient takes home: what medicines to take, what activity is allowed or restricted, when the follow-up appointment is, and the warning signs that mean "call us" or "go to the ER." Built for low health literacy — large type, simple pictograms, high contrast, and a clearly dominant warning-signs block.

> **Educational aid, not medical advice.** This sheet supports the discharge conversation with a licensed clinician. It does not replace professional medical advice, and the clinician's verbal and charted instructions govern. All content must be supplied and approved by a clinician before it is given to a patient.

**Format:** 8.5 x 11 inch portrait handout, single side, 300 DPI (2550 x 3300 px), print-ready and screen-readable.

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core techniques used here
- [patient_education_condition_infographic.md](./patient_education_condition_infographic.md) — condition explainer
- [patient_medication_guide_visual.md](./patient_medication_guide_visual.md) — detailed single-medication guide
- [patient_anatomy_explainer_diagram.md](./patient_anatomy_explainer_diagram.md) — simple labeled anatomy diagram

---

## How To Use This Template

1. **Pull the discharge details** for this specific encounter from the chart / discharge order, confirmed by the discharging clinician.
2. **Fill the `[PLACEHOLDERS]`** in the prompt below. Keep each line short and concrete.
3. **Generate** (see Model-Specific Notes — gpt-image-2 or Nano Banana Pro first for dense text).
4. **Have the discharging clinician sign off** on the rendered sheet before it goes home with the patient.

The EXAMPLE fill is illustrative only. **Replace it** before any real use.

---

## Image Generation Prompt (Production-Ready, Template)

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a one-page VISUAL DISCHARGE INSTRUCTIONS SHEET for a patient going home.

IMPORTANT REAL-WORLD CONTEXT:
This is a take-home discharge sheet.
It is printed on plain paper and given to a patient or caregiver at discharge.
The reader may be tired, in pain, on medication, older, or have low health literacy.
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
If any medicine, dose, restriction, date, or warning sign not listed below appears, the output is incorrect.

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

Stacked full-width zones with thin solid gray separators (#9CA3AF, 1px):

ZONE 1 - HEADER (top, ~10% height)
- Solid fill: teal #0F766E
- White text, left-aligned:
  - Line 1 (bold, 36pt): "Going Home: Your Instructions"
  - Line 2 (regular, 18pt): "Name: [PATIENT NAME]   Date: [DISCHARGE DATE]"
- Sharp rectangular corners.

ZONE 2 - YOUR MEDICINES (~24% height)
- White background.
- Heading with a simple flat pill icon (bold, 26pt, dark teal #115E59): "Your medicines"
- A clean list, one medicine per row. Each row = simple pill icon + text (20pt):
  MED 1: "[MEDICINE 1] - [HOW MUCH] - [WHEN]"
  MED 2: "[MEDICINE 2] - [HOW MUCH] - [WHEN]"
  MED 3: "[MEDICINE 3] - [HOW MUCH] - [WHEN]"
- One short note line (italic, 18pt): "[STOP/START NOTE, e.g. 'Stop your old blood thinner']"

ZONE 3 - ACTIVITY (~20% height), split into two side-by-side columns of EQUAL width
- LEFT column, very light green background #ECFDF5:
  - Heading (bold, 24pt, green #166534) with a flat check icon: "You CAN"
  - Up to 3 short lines (20pt):
    "[ALLOWED ACTIVITY 1]"
    "[ALLOWED ACTIVITY 2]"
    "[ALLOWED ACTIVITY 3]"
- RIGHT column, very light red background #FEF2F2:
  - Heading (bold, 24pt, red #991B1B) with a flat no-entry icon: "Do NOT"
  - Up to 3 short lines (20pt):
    "[RESTRICTED ACTIVITY 1]"
    "[RESTRICTED ACTIVITY 2]"
    "[RESTRICTED ACTIVITY 3]"

ZONE 4 - FOLLOW-UP (~16% height)
- Very light blue background #EFF6FF.
- Heading with a flat calendar icon (bold, 26pt, dark blue #1E3A8A): "Your follow-up"
- Large, clear lines (22pt):
  "See: [PROVIDER / CLINIC]"
  "When: [DATE AND TIME]"
  "Where: [LOCATION]"
  "Call to confirm: [PHONE NUMBER]"

ZONE 5 - WHEN TO CALL / WARNING SIGNS (bottom, ~30% height)
- Solid fill: alert red #B91C1C with a thick red border (4px, #7F1D1D).
- Heading (bold, 28pt, white): "Call us or go to the ER if:"
- White warning list, large (22pt), each line preceded by a white warning-triangle symbol:
  - "[WARNING SIGN 1]"
  - "[WARNING SIGN 2]"
  - "[WARNING SIGN 3]"
  - "[WARNING SIGN 4]"
- Two final lines (bold, 22pt, white):
  "Questions? Call [CLINIC PHONE]."
  "Emergency? Call [EMERGENCY NUMBER] now."

================================================
DESIGN SYSTEM (STRICT)
================================================

ALL SHAPES:
- Rectangular zones with sharp 90-degree corners.
- Solid fills only. No transparency. No gradients.
- The two activity columns must be EQUAL width and aligned.

PICTOGRAMS (allowed, simple only):
- Flat, 2-color, single-line-weight icons (pill, check, no-entry, calendar, warning-triangle).
- One concept per icon. No detail, no shading, no 3D.
- Icons support ONLY the supplied labels. Do not invent new icons or content.

TYPOGRAPHY:
- Clean legible sans-serif (Arial, Open Sans, or Verdana).
- Header: 36pt bold. Section headings: 24-28pt bold. Body/list: 20-22pt.
- Minimum text size anywhere: 18pt.
- High contrast: dark text on light fill, white text on saturated fill. Minimum 7:1.
- One idea per line. Short sentences.

================================================
HEALTH-LITERACY RULES (NON-NEGOTIABLE)
================================================

- Plain language at a 6th-grade reading level. Everyday words.
- Short sentences (aim under 15 words).
- One idea per line; generous white space.
- No jargon unless the supplied text explains it in plain words.

================================================
CONSTRAINTS (REPEATED)
================================================

- NO gradients - solid colors only
- NO rounded outer corners
- NO shadows or depth effects
- NO mockup or device staging
- NO invented medical content
- All text 18pt or larger
- High contrast (minimum 7:1)
- Print-ready: CMYK, 300 DPI, 0.5 inch safe margin

================================================
VISUAL HIERARCHY
================================================

1. Primary attention: Red "Call us or go to the ER if" warning zone
2. Secondary attention: Medicines and Follow-up
3. Tertiary attention: Activity Can / Do NOT columns
4. Background: Zone fills, separators, pictograms

================================================
FINAL VALIDATION CHECK
================================================

- One image only
- Portrait orientation (taller than wide)
- 5 zones in order: Header, Medicines, Activity (2 equal columns), Follow-up, When to call
- Activity columns equal width, green CAN / red Do NOT
- Large type (18pt minimum), high contrast
- Simple flat 2-color pictograms only
- Sharp rectangular corners, flat print, solid colors, no gradients/shadows
- Only supplied medical text appears; nothing invented
- Red warning zone is the most prominent block
```

---

## EXAMPLE Fill (Illustrative Only)

> **EXAMPLE — REPLACE WITH CLINICIAN-VERIFIED CONTENT.** Generic illustration only. Not validated for any patient; must not be distributed.

```
HEADER: Name: "Jane Doe"   Date: "June 23, 2026"

YOUR MEDICINES:
MED 1: "Acetaminophen 500 mg - 2 tablets - every 6 hours as needed for pain"
MED 2: "Amoxicillin 500 mg - 1 capsule - 3 times a day until all are gone"
MED 3: "Docusate 100 mg - 1 capsule - twice a day while taking pain medicine"
Note: "Do not take any other medicine with acetaminophen in it."

ACTIVITY:
You CAN:
- "Walk short distances around your home"
- "Shower after 48 hours"
- "Do light daily tasks"
Do NOT:
- "Lift more than 10 pounds for 2 weeks"
- "Drive while taking pain medicine"
- "Soak in a bath or pool for 2 weeks"

FOLLOW-UP:
See: "Dr. Smith, General Surgery"
When: "July 1, 2026 at 10:00 AM"
Where: "Main Clinic, 2nd floor"
Call to confirm: "(555) 123-4567"

WHEN TO CALL / WARNING SIGNS:
- "Fever over 100.4 F (38 C)"
- "Redness, swelling, or pus at your wound"
- "Bleeding that will not stop"
- "Bad belly pain or vomiting"
Final lines: "Questions? Call (555) 123-4567." / "Emergency? Call 911 now."
```

---

## Simplified Fallback Prompt (If Full Prompt Misbehaves)

```
Create ONE flat rectangular discharge sheet, 8.5 x 11 inches PORTRAIT.

RULES:
- Sharp corners only - NO rounded corners
- Solid colors only - NO gradients, NO shadows
- FLAT PRINT ARTWORK, not a mockup
- Very large type (18pt+), high contrast, plain language (6th-grade level)
- Render ONLY the text I give you. Add NO medical facts.

ZONES top to bottom:
1. Teal header: "Going Home: Your Instructions" + Name/Date
2. "Your medicines": pill icon + rows [MED 1-3]
3. "Activity": two equal columns - green "You CAN" [3 lines], red "Do NOT" [3 lines]
4. "Your follow-up" (light blue): See / When / Where / Call to confirm
5. Red zone "Call us or go to the ER if:": [WARNING 1-4] + "Questions? Call [PHONE]." + "Emergency? Call [NUMBER] now."

If output has rounded corners, gradients, or any medical text I did not supply, it is WRONG.
```

---

## Why This Prompt Works

1. **Terminology Steering (SV-11)** — "flat print artwork" / "take-home discharge sheet" blocks UI-card behaviors.
2. **Grid Forcing + Enumerated Slots (SV-12)** — 5 fixed zones, two equal activity columns, and numbered MED/WARNING slots stop the model from merging or reordering content.
3. **Constraint Redundancy (SV-13)** — "no gradients" and "no invented content" repeat in global rules, design system, and checklist.
4. **Negative Space Control (SV-14)** — solid white background, edge-to-edge, no staging.
5. **Allowed vs. Forbidden Distinction (SV-15)** — simple flat pictograms allowed; detailed art and non-supplied content forbidden. The green-CAN / red-Do-NOT split is itself an allowed/forbidden visual.
6. **Physical Context Anchoring (SV-16)** — "tired, in pain, on medication, older" forces large type and high contrast.
7. **Deliverables Locking (SV-17)** — EXACTLY ONE IMAGE, portrait, 8.5x11, 300 DPI.
8. **Validation Checklist (SV-18)** — final self-audit including a content-fidelity check.

**Plus a health-literacy layer:** 6th-grade plain language, one-idea-per-line, 18pt minimum, 7:1 contrast, and the warning-signs block given the dominant position — the single most safety-critical part of any discharge sheet.

See [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md).

---

## Anti-Fabrication / Clinical Content

**The model typesets; it does not decide care.**

- **No invented details.** Medicines, doses, schedules, activity limits, follow-up dates, phone numbers, and warning signs come only from the placeholders.
- **Verbatim rendering.** Doses and dates are especially dangerous to paraphrase — render them exactly. Verify every number on the output against the order.
- **Encounter-specific.** Discharge instructions are unique to one patient and visit; do not reuse another patient's sheet as content.
- **Clinician governs.** If the rendered sheet and the discharge order disagree, the order wins — fix the sheet.
- **No new advice.** The model must not "helpfully" add generic post-op tips, drug interactions, or warning signs not in the fill.

---

## Model-Specific Notes

### gpt-image-2 (OpenAI, recommended for dense patient text)
- Set `quality="high"` — doses, dates, and warning signs must be exact and legible.
- Map onto the 5-section structure (Scene / Subject / Key Details / Use Case / Constraints); put print + health-literacy rules under CONSTRAINTS.
- Do not pass `input_fidelity` (disabled in gpt-image-2).
- Keep the anti-fabrication line high in the prompt so doses/dates are not paraphrased.
- See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md).

### Nano Banana Pro (Gemini 3 Pro Image, also recommended)
- Excellent at many short exact lines (doses, dates, phone numbers); name a font (e.g., "Verdana").
- Use Markdown lists; the model parses them natively.
- Use a **system prompt** to lock "render only supplied text; never invent doses, dates, or warning signs."
- Do not rely on Search grounding for any clinical fact — facts come from the placeholders.

### DALL-E 3 (legacy)
Add: `"Visual discharge instructions handout, flat 2D print, large legible type, simple pictograms, no gradients."` Verify all numbers by hand.

### Midjourney (legacy)
```
flat print artwork, patient discharge instructions sheet, portrait handout,
large sans-serif type, simple flat pictograms, stacked color zones, two-column activity panel,
--ar 17:22 --v 6 --style raw --s 25
--no 3d mockup photo gradient shadow rounded corners device frame
```
Poor at exact text — layout exploration only, then re-typeset.

### Stable Diffusion (legacy)
Negative prompt: `"photograph, 3d render, gradients, rounded corners, shadows, small text, dense paragraphs, decorative, watermark, device mockup"`
Not recommended for exact doses/dates.

---

## Troubleshooting

### Problem: Model invents extra medicines, warning signs, or post-op tips
**Add:** `"Render ONLY the medicines and warning lines I supplied. Count them. Any extra line = rendering error."`

### Problem: Doses or dates altered
**Add:** `"Reproduce every number and date EXACTLY as written. Do not round, reformat, or change any dose, time, or date."`

### Problem: Activity columns unequal or merged
**Add:** `"Two EQUAL-width columns side by side: green 'You CAN' on the left, red 'Do NOT' on the right. Do not merge them."`

### Problem: Warning zone not prominent
**Add:** `"The red 'Call us or go to the ER if' block must be the largest, most prominent zone with the biggest warning text."`

### Problem: 3D mockup / rounded corners / gradients
**Add:** `"This IS the flat printed page. Sharp 90-degree corners only. Solid fills only. No device, hand, shadow, or gradient."`

---

## Verification Checklist (Before Patient Distribution)

- [ ] **All medical content reviewed and approved by a clinician before patient distribution.**
- [ ] Every medicine, dose, schedule, activity limit, follow-up detail, and warning sign matches the discharge order exactly.
- [ ] No content appears that was not in the clinician-supplied fill (no model-invented items).
- [ ] All numbers and dates on the output were re-checked against the chart/order.
- [ ] Reading level is approximately 6th grade; short, jargon-free lines.
- [ ] All text is 18pt or larger and high-contrast.
- [ ] The "When to call / warning signs" block is present and most prominent.
- [ ] Correct clinic phone and local emergency number are shown.
- [ ] The sheet states it is educational and not a substitute for professional medical advice.
- [ ] EXAMPLE content has been fully replaced.
- [ ] One portrait image, sharp corners, flat print, no gradients/shadows.

---

*Updated: 2026-06-23 — Tier-1 patient-education image-generation prompt with anti-fabrication and health-literacy guardrails.*
