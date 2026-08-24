# Endocrinology Guide

## Trigger Phrases

Use this guide when requests include terms like:
- "diabetes regimen", "A1c", "insulin adjustment", "hypoglycemia risk"
- "thyroid function", "TSH/T4 interpretation", "thyroid nodule follow-up"
- "adrenal insufficiency", "steroid taper", "Cushing workup"
- "electrolyte/endocrine axis", "calcium/PTH", "pituitary disorder"
- "metabolic syndrome", "obesity pharmacotherapy"

## Recommended Prompt Map (Existing + New)

### Existing prompts to route first
- `domain-healthcare-clinical/prompts/medicine_chronic_disease_management_planner.md`
- `domain-healthcare-clinical/prompts/medicine_preventive_care_screening_advisor.md`
- `domain-healthcare-clinical/prompts/medicine_lab_diagnostic_interpreter.md`
- `domain-healthcare-clinical/prompts/medicine_renal_hepatic_dose_adjustment.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_decision_support.md`
- `domain-healthcare-clinical/prompts/medicine_medication_reconciliation.md`

### New prompts to add when repeated demand appears
- **Diabetes Intensification and Safety Prompt** (A1c trend, hypoglycemia risk, adherence barriers)
- **Thyroid Diagnostic Pathway Prompt** (biochemical pattern recognition + imaging/lab follow-through)
- **Adrenal/Pituitary Red-Flag Evaluator Prompt** (critical endocrine emergency checkpoints)

## When Not to Use

Do **not** use this guide as primary routing when:
- The core request is acute emergency triage outside endocrine scope.
- The request is direct-to-patient medication dosing instructions.
- The dominant problem is infectious deterioration or psychiatric crisis.
- The task is billing/coding-focused without endocrine reasoning needs.

## Required Safety Cautions and Escalation Boundaries

- Treat all outputs as support for clinician review, not autonomous management.
- Require escalation flags for:
  - severe hypoglycemia or hyperglycemic crisis concern
  - adrenal crisis concern
  - myxedema/coma or thyroid storm concern
  - severe electrolyte derangements with symptoms
- Never provide unsupervised insulin or high-risk hormone titration instructions.
- Require comorbidity and interaction checks (CKD, liver disease, cardiac disease, pregnancy, concurrent steroids/antipsychotics).
- Escalate to endocrinology or emergency evaluation when instability, severe symptoms, or high-risk endocrine emergencies are suspected.
