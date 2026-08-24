---
title: "Patient Medication Guide Visual - Image Generation Prompt"
category: medical-education
description: "Template-driven image generation prompt for a 'how to take your medication' visual handout (dose, timing, with/without food, side effects, missed dose). Low-health-literacy friendly: large type, simple icons, high contrast. The model renders clinician-supplied content only."
tags:
  - medical
  - patient-education
  - medication
  - health-literacy
  - handout
  - plain-language
  - image-generation
updated: "2026-06-23"
related_prompts:
  - ../IMAGE_GENERATION_GUIDE.md
  - ./patient_education_condition_infographic.md
  - ./patient_discharge_instructions_visual.md
  - ./patient_anatomy_explainer_diagram.md
  - ./nursing_badge_buddy_critical_drips.md
---

# Patient Medication Guide Visual - Image Generation Prompt

**Purpose:** Generate a single-page "how to take your medication" handout for one medicine: how much, when, with or without food, the common side effects to expect, and what to do if a dose is missed. Built for low health literacy — large type, time-of-day pictograms, high contrast, and a clearly dominant safety block.

> **Educational aid, not medical advice.** This handout supports a conversation with a pharmacist or prescriber and does not replace professional medical advice or the official medication label/leaflet. All content must be supplied and approved by a clinician or pharmacist before it is given to a patient.

**Format:** 8.5 x 11 inch portrait handout, single side, 300 DPI (2550 x 3300 px), print-ready and screen-readable.

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core techniques used here
- [patient_discharge_instructions_visual.md](./patient_discharge_instructions_visual.md) — full discharge sheet (lists all meds)
- [patient_education_condition_infographic.md](./patient_education_condition_infographic.md) — condition explainer
- [nursing_badge_buddy_critical_drips.md](./nursing_badge_buddy_critical_drips.md) — clinician-side drip reference (note: this guide is the patient-facing counterpart)

---

## How To Use This Template

1. **Pull the medication facts** from the official label / approved drug-information source for the exact product and strength, confirmed by a pharmacist or prescriber.
2. **Fill the `[PLACEHOLDERS]`** below. Use plain words; keep numbers exact.
3. **Generate** (see Model-Specific Notes — gpt-image-2 or Nano Banana Pro first for exact dose text).
4. **Have a pharmacist/prescriber sign off** on the rendered sheet before it reaches a patient.

The EXAMPLE fill is illustrative only. **Replace it** before any real use.

---

## Image Generation Prompt (Production-Ready, Template)

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a one-page "HOW TO TAKE YOUR MEDICINE" patient handout for ONE medication.

IMPORTANT REAL-WORLD CONTEXT:
This is a take-home medicine handout.
It is printed on plain paper and given to a patient or caregiver.
The reader may be older, on several medicines, or have low health literacy.
It must be readable at arm's length with large type and high contrast.
Render ONLY the text, numbers, and labels supplied below. Do not invent or add any medical facts.

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
- DO NOT add, change, or invent any medical content. Render every dose, time, and word verbatim.

If any gradient, shadow, or rounded outer corner appears, the output is incorrect.
If any dose, time, side effect, or instruction not listed below appears, the output is incorrect.

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

ZONE 1 - MEDICINE NAME BANNER (top, ~12% height)
- Solid fill: indigo #4338CA
- White text, left-aligned, with a simple flat pill/capsule icon on the right:
  - Line 1 (bold, 40pt): "[MEDICINE NAME]"
  - Line 2 (regular, 20pt): "Also called: [BRAND OR GENERIC ALTERNATE NAME] - [WHAT IT IS FOR, plain words]"
- Sharp rectangular corners.

ZONE 2 - HOW MUCH & WHEN (~26% height) - the core dosing block
- Very light indigo background #EEF2FF.
- Heading (bold, 26pt, indigo #3730A3): "How much and when"
- Big dose statement (bold, 34pt, dark gray #111827): "[HOW MANY] [FORM], [HOW OFTEN]"
  (example shape: "1 tablet, 2 times a day")
- A row of up to 4 TIME-OF-DAY pictograms left to right, each a simple flat icon + label (20pt):
  TIME 1: "[sunrise icon] Morning: [yes/no or detail]"
  TIME 2: "[sun icon] Midday: [yes/no or detail]"
  TIME 3: "[sunset icon] Evening: [yes/no or detail]"
  TIME 4: "[moon icon] Bedtime: [yes/no or detail]"
- One plain line (20pt): "[ANY TIMING DETAIL, e.g. 'Take at the same times each day']"

ZONE 3 - WITH OR WITHOUT FOOD (~14% height), two side-by-side EQUAL columns
- LEFT column, light green #ECFDF5 if applicable OR gray #F3F4F6 if not:
  - Flat plate/food icon + heading (bold, 22pt): "With food?"
  - Text (20pt): "[WITH-FOOD INSTRUCTION, e.g. 'Take with a meal' or 'Food not required']"
- RIGHT column, light blue #EFF6FF:
  - Flat glass/water icon + heading (bold, 22pt): "Drinks & cautions"
  - Text (20pt): "[FLUID OR AVOIDANCE NOTE, e.g. 'Take with a full glass of water. Avoid alcohol.']"

ZONE 4 - SIDE EFFECTS (~18% height)
- White background.
- Heading (bold, 26pt, dark gray #111827): "What you might notice"
- A list of common, expected side effects, one per row, simple flat icon + label (20pt):
  SIDE EFFECT 1: "[COMMON SIDE EFFECT 1]"
  SIDE EFFECT 2: "[COMMON SIDE EFFECT 2]"
  SIDE EFFECT 3: "[COMMON SIDE EFFECT 3]"
- One plain note line (italic, 18pt): "[REASSURANCE/CONTEXT, e.g. 'These often improve after a few days.']"

ZONE 5 - MISSED DOSE + WHEN TO CALL (bottom, ~30% height), two stacked sub-bands
- SUB-BAND A - MISSED DOSE, amber background #FEF3C7 with a 3px amber border #B45309:
  - Heading (bold, 24pt, dark amber #92400E): "If you miss a dose"
  - Plain lines (20pt):
    "[MISSED-DOSE INSTRUCTION 1, e.g. 'Take it as soon as you remember.']"
    "[MISSED-DOSE INSTRUCTION 2, e.g. 'If it is almost time for the next dose, skip the missed one.']"
    "[MISSED-DOSE INSTRUCTION 3, e.g. 'Never take two doses at once.']"
- SUB-BAND B - WHEN TO CALL, alert red #B91C1C with a 4px red border #7F1D1D:
  - Heading (bold, 26pt, white): "Call your doctor or pharmacist if:"
  - White warning list (22pt), each line with a white warning-triangle symbol:
    "[SERIOUS SIGN 1]"
    "[SERIOUS SIGN 2]"
  - Final line (bold, 22pt, white): "Severe reaction or trouble breathing? Call [EMERGENCY NUMBER] now."

================================================
DESIGN SYSTEM (STRICT)
================================================

ALL SHAPES:
- Rectangular zones with sharp 90-degree corners.
- Solid fills only. No transparency. No gradients.
- The with/without-food columns must be EQUAL width and aligned.

PICTOGRAMS (allowed, simple only):
- Flat, 2-color, single-line-weight icons (pill/capsule, sunrise, sun, sunset, moon, plate, glass, warning-triangle).
- One concept per icon. No detail, no shading, no 3D.
- A pill icon must NOT depict a specific real-world pill color/shape unless that exact appearance is supplied (avoid implying a wrong product).
- Icons support ONLY the supplied labels. Do not invent icons or content.

TYPOGRAPHY:
- Clean legible sans-serif (Arial, Open Sans, or Verdana).
- Medicine name: 40pt bold. Big dose: 34pt bold. Headings: 22-26pt bold. Body/list: 20-22pt.
- Minimum text size anywhere: 18pt.
- High contrast: dark text on light fill, white text on saturated fill. Minimum 7:1.
- One idea per line. Short sentences.

================================================
HEALTH-LITERACY RULES (NON-NEGOTIABLE)
================================================

- Plain language at a 6th-grade reading level. Everyday words.
- Numbers written simply ("2 times a day", not "BID").
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
- NO invented medical content; reproduce all doses/times exactly
- All text 18pt or larger
- High contrast (minimum 7:1)
- Print-ready: CMYK, 300 DPI, 0.5 inch safe margin

================================================
VISUAL HIERARCHY
================================================

1. Primary attention: The big "How much and when" dose statement, and the red "When to call" band
2. Secondary attention: Medicine name banner, missed-dose amber band
3. Tertiary attention: With/without food, side effects
4. Background: Zone fills, separators, pictograms

================================================
FINAL VALIDATION CHECK
================================================

- One image only
- Portrait orientation (taller than wide)
- 5 zones in order: Name, How much & when, Food/drink (2 equal columns), Side effects, Missed dose + When to call
- Big dose statement is large and unmistakable
- Time-of-day pictograms present and labeled
- Large type (18pt minimum), high contrast
- Simple flat 2-color pictograms only
- Sharp rectangular corners, flat print, solid colors, no gradients/shadows
- Only supplied medical text appears; every dose and time matches exactly; nothing invented
- Red "When to call" band is highly prominent
```

---

## EXAMPLE Fill (Illustrative Only)

> **EXAMPLE — REPLACE WITH CLINICIAN-VERIFIED CONTENT.** Generic illustration only. Not validated for any patient or product; must not be distributed.

```
NAME BANNER:
[MEDICINE NAME] = "Metformin 500 mg"
Also called: "Glucophage - helps control blood sugar in type 2 diabetes"

HOW MUCH AND WHEN:
Big dose statement: "1 tablet, 2 times a day"
TIME 1: "Morning: Yes (with breakfast)"
TIME 2: "Midday: No"
TIME 3: "Evening: Yes (with dinner)"
TIME 4: "Bedtime: No"
Detail: "Take at the same times each day."

WITH OR WITHOUT FOOD:
With food?: "Take with a meal to lower stomach upset."
Drinks & cautions: "Drink water. Limit alcohol."

WHAT YOU MIGHT NOTICE:
SIDE EFFECT 1: "Upset stomach or loose stools"
SIDE EFFECT 2: "Gas or a metal taste"
SIDE EFFECT 3: "Less appetite"
Note: "These often improve after the first week."

IF YOU MISS A DOSE:
- "Take it as soon as you remember."
- "If it is almost time for the next dose, skip the missed one."
- "Never take two doses at once."

CALL YOUR DOCTOR OR PHARMACIST IF:
- "Muscle pain, very tired, or trouble breathing"
- "Vomiting that will not stop"
Final line: "Severe reaction or trouble breathing? Call 911 now."
```

---

## Simplified Fallback Prompt (If Full Prompt Misbehaves)

```
Create ONE flat rectangular medicine handout, 8.5 x 11 inches PORTRAIT.

RULES:
- Sharp corners only - NO rounded corners
- Solid colors only - NO gradients, NO shadows
- FLAT PRINT ARTWORK, not a mockup
- Very large type (18pt+), high contrast, plain language (6th-grade level)
- Render ONLY the text I give you. Reproduce all doses/times EXACTLY. Add NO medical facts.

ZONES top to bottom:
1. Indigo banner: "[MEDICINE NAME]" + "Also called / what it is for"
2. "How much and when": BIG dose line "[HOW MANY x HOW OFTEN]" + 4 time-of-day icons (Morning/Midday/Evening/Bedtime) [labels]
3. Two equal columns: "With food?" [note] and "Drinks & cautions" [note]
4. "What you might notice": side-effect rows [SIDE EFFECT 1-3]
5. Amber "If you miss a dose" [3 lines] + Red "Call your doctor or pharmacist if:" [2 signs] + "Severe reaction or trouble breathing? Call [NUMBER] now."

If output has rounded corners, gradients, or any dose/time/text I did not supply, it is WRONG.
```

---

## Why This Prompt Works

1. **Terminology Steering (SV-11)** — "flat print artwork" / "take-home medicine handout" avoids UI-card behaviors.
2. **Grid Forcing + Enumerated Slots (SV-12)** — 5 fixed zones, equal food/drink columns, enumerated TIME and SIDE EFFECT slots, and an oversized single dose statement prevent reorganization.
3. **Constraint Redundancy (SV-13)** — "no gradients," "reproduce doses exactly," and "no invented content" recur in global rules, design system, and checklist.
4. **Negative Space Control (SV-14)** — solid white background, edge-to-edge, no staging.
5. **Allowed vs. Forbidden Distinction (SV-15)** — simple flat pictograms allowed; realistic/branded pill imagery and non-supplied content forbidden (a deliberate safety choice to avoid implying the wrong product).
6. **Physical Context Anchoring (SV-16)** — "older, on several medicines, low health literacy" forces large type, plain numbers, time-of-day icons.
7. **Deliverables Locking (SV-17)** — EXACTLY ONE IMAGE, portrait, 8.5x11, 300 DPI.
8. **Validation Checklist (SV-18)** — final self-audit including dose-fidelity and content-fidelity checks.

**Plus a health-literacy layer:** 6th-grade plain language, "2 times a day" instead of "BID," one-idea-per-line, 18pt minimum, 7:1 contrast, and dual high-priority blocks (the big dose statement and the red "when to call" band).

See [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md).

---

## Anti-Fabrication / Clinical Content

**Medication errors are high-harm. The model must only typeset clinician/pharmacist-supplied content.**

- **No invented facts.** Dose, strength, frequency, food rules, side effects, missed-dose steps, and warning signs come only from the placeholders.
- **Exact numbers.** Never let the model round, reformat, or "simplify" a dose, strength, or frequency. Re-check every number on the output against the label/order.
- **No drug imagery that implies a product.** Pictograms stay generic; do not depict a specific pill color/shape unless that exact appearance is supplied — a wrong-looking pill can cause a real mix-up.
- **Product-specific.** Facts must match the exact product and strength dispensed; do not mix data from different formulations.
- **Defers to the label.** This handout supplements, and must not contradict, the official medication leaflet and the pharmacist's counseling.
- **No new advice.** The model must not add interactions, side effects, or warnings not in the fill.

---

## Model-Specific Notes

### gpt-image-2 (OpenAI, recommended for exact dose text)
- Set `quality="high"` — doses, frequencies, and warning signs must be exact and crisp.
- Map onto the 5-section structure (Scene / Subject / Key Details / Use Case / Constraints); place print + health-literacy + dose-fidelity rules under CONSTRAINTS.
- Do not pass `input_fidelity` (disabled in gpt-image-2).
- Keep the "reproduce all doses/times verbatim" line near the top.
- See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md).

### Nano Banana Pro (Gemini 3 Pro Image, also recommended)
- Strong at exact short strings (doses, times); name a font (e.g., "Verdana") for clean numerals.
- Use Markdown structure; the model parses it natively.
- Use a **system prompt** to lock "render only supplied text; never alter or invent doses, times, or side effects."
- Do not rely on Search grounding for drug facts — facts come from the placeholders.

### DALL-E 3 (legacy)
Add: `"How-to-take-your-medicine handout, flat 2D print, large legible type, time-of-day pictograms, no gradients."` Verify every number by hand.

### Midjourney (legacy)
```
flat print artwork, patient medication instructions handout, portrait,
large sans-serif type, simple flat time-of-day pictograms, stacked color zones,
--ar 17:22 --v 6 --style raw --s 25
--no 3d mockup photo gradient shadow rounded corners realistic pills device frame
```
Poor at exact text — layout exploration only, then re-typeset.

### Stable Diffusion (legacy)
Negative prompt: `"photograph, 3d render, realistic pills, gradients, rounded corners, shadows, small text, dense paragraphs, decorative, watermark, device mockup"`
Not recommended for exact doses.

---

## Troubleshooting

### Problem: Dose, strength, or frequency changed
**Add:** `"Reproduce the dose, strength, and frequency EXACTLY as written. Do not round, abbreviate, or reformat any number."`

### Problem: Model invents side effects or warnings
**Add:** `"List ONLY the side effects and warning signs I supplied. Count them. Any extra item = rendering error."`

### Problem: Realistic / branded pill picture appears
**Add:** `"Use a simple flat generic pill icon only. Do NOT draw a realistic, colored, or branded pill that could imply a specific product."`

### Problem: Big dose statement not prominent
**Add:** `"The 'How much and when' dose line must be the largest body text on the page, unmistakable at a glance."`

### Problem: 3D mockup / rounded corners / gradients
**Add:** `"This IS the flat printed page. Sharp 90-degree corners only. Solid fills only. No device, hand, shadow, or gradient."`

---

## Verification Checklist (Before Patient Distribution)

- [ ] **All medical content reviewed and approved by a clinician or pharmacist before patient distribution.**
- [ ] Medicine name, strength, dose, frequency, food rules, side effects, missed-dose steps, and warning signs match the label/order for the exact product dispensed.
- [ ] Every dose and time on the output was re-checked against the source (no rounding or reformatting).
- [ ] No content appears that was not in the supplied fill (no model-invented items).
- [ ] No realistic/branded pill image that could imply a specific product.
- [ ] Reading level is approximately 6th grade; numbers in plain words ("2 times a day").
- [ ] All text is 18pt or larger and high-contrast.
- [ ] Both the big dose statement and the red "When to call" band are prominent.
- [ ] Correct local emergency number is shown.
- [ ] The handout states it is educational and does not replace the official medication label or professional advice.
- [ ] EXAMPLE content has been fully replaced.
- [ ] One portrait image, sharp corners, flat print, no gradients/shadows.

---

*Updated: 2026-06-23 — Tier-1 patient-education image-generation prompt with anti-fabrication and health-literacy guardrails.*
