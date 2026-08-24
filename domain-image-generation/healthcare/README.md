# Healthcare Image Generation Prompts

Prompts in this folder generate healthcare visuals: bedside reference cards, patient-education handouts, and clinical/medical education diagrams.

> **Clinical-safety convention (load-bearing):** Every prompt here is **anti-fabrication first**. The image model **renders user-supplied, institution-verified content** — it must never invent, guess, round, or "improve" any clinical value (doses, lab ranges, drug names, units, anatomy labels, decision criteria). Template prompts use `[PLACEHOLDERS]` and a single clearly-labeled EXAMPLE fill. Every prompt ends with a verification checklist requiring clinician / subject-matter-expert sign-off before clinical, patient, or instructional use. Image models are **not** anatomically or numerically reliable; high-stakes clinical-grade illustration may require a professional medical illustrator.

## Clinician Reference Cards (badge buddies)
Print-ready, lamination-friendly quick-reference cards.
- [nursing_badge_buddy_critical_drips.md](./nursing_badge_buddy_critical_drips.md) — ICU/critical-care IV drip dosing & titration
- [clinical_badge_buddy_lab_values.md](./clinical_badge_buddy_lab_values.md) — common lab value normal ranges (CBC/BMP/CMP/coags/ABG/cardiac)
- [clinical_badge_buddy_acls_codes.md](./clinical_badge_buddy_acls_codes.md) — adult ACLS / code-blue algorithms & code drugs
- [clinical_badge_buddy_med_dosing_template.md](./clinical_badge_buddy_med_dosing_template.md) — fully template-driven dosing card (fill with your verified content)
- [clinical_badge_buddy_antibiogram_template.md](./clinical_badge_buddy_antibiogram_template.md) — antibiotic spectrum/coverage card (template-driven by local antibiogram)

## Patient Education
Plain-language, health-literacy-friendly handouts (8.5×11, clinician-reviewed before distribution).
- [pacu_infographic_image_prompt.md](./pacu_infographic_image_prompt.md) — PACU patient infographic
- [patient_education_condition_infographic.md](./patient_education_condition_infographic.md) — explain a condition to patients
- [patient_discharge_instructions_visual.md](./patient_discharge_instructions_visual.md) — visual discharge-instructions sheet
- [patient_medication_guide_visual.md](./patient_medication_guide_visual.md) — "how to take your medication" visual
- [patient_anatomy_explainer_diagram.md](./patient_anatomy_explainer_diagram.md) — simple patient-friendly anatomy explainer

## Clinical & Medical Education Diagrams
Labeled instructional diagrams (expert-verified before instructional use).
- [medical_anatomy_physiology_diagram.md](./medical_anatomy_physiology_diagram.md) — labeled anatomy/physiology diagram
- [medical_procedure_step_diagram.md](./medical_procedure_step_diagram.md) — step-by-step illustrated procedure sequence
- [medical_pathophysiology_mechanism_diagram.md](./medical_pathophysiology_mechanism_diagram.md) — disease-mechanism flow diagram
- [medical_clinical_algorithm_flowchart.md](./medical_clinical_algorithm_flowchart.md) — clinical decision / triage flowchart

## Model Notes
These prompts lead with **gpt-image-2** (OpenAI — strongest in-image text) and **Nano Banana Pro** (`gemini-3-pro-image` — near-perfect text + exact fonts) for text-dense clinical cards; DALL-E 3 / Midjourney / Stable Diffusion are listed as legacy and flagged unreliable for exact in-image numbers/text. See the parent guides:
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 print-ready constraint techniques used here
- [IMAGE_MODEL_SELECTION_GUIDE.md](../IMAGE_MODEL_SELECTION_GUIDE.md) — choosing the right model

## Related Resources
- [Healthcare & Clinical domain guide](../../domain-healthcare-clinical/README.md)
- [Non-coding healthcare skills](../../domain-agentic-resources/skills/non-coding/healthcare/)
- [Psychology specialty resources](../../domain-psychology/)
