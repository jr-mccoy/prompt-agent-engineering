---
title: "Endocrinology Guide"
category: healthcare-clinical/guides
description: "Endocrinology routing guide: trigger phrases, the existing prompts to route first, when not to use this guide, and the required safety cautions and escalation boundaries."
techniques:
  - CM-03
  - CM-09
  - DS-36
  - IT-26
difficulty: intermediate
tags:
  - endocrinology
  - diabetes
  - escalation
updated: "2026-10-06"
---

# Endocrinology Guide

> **Medical disclaimer — read before use.** This prompt is a decision-support and
> teaching aid for **licensed clinicians**. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

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

## False-Positive Prevention

When using this guide:

❌ **DON'T:**
- Follow the prompt-map links as written; they point at the domain's `prompts/` root while the files now sit in subfolders (care-plans/, interpretation/, pharmacology/, reasoning/), so resolve each one before use.
- Send a hyperglycemic-crisis or adrenal-crisis case to a chronic-management prompt because "insulin adjustment" or "steroid taper" matched; this map omits the acute-care DKA and HHS prompts, so search for them.
- Accept a "biochemical pattern" call on TSH/free T4 or calcium/PTH in the routed output when the reporting lab's reference ranges and interfering exposures (biotin, steroids, amiodarone, albumin for calcium) were not supplied.

✅ **DO:**
- Check the routed output against each comorbidity on this guide's interaction line (CKD, liver disease, cardiac disease, pregnancy, concurrent steroids/antipsychotics) and list the ones not supplied.
- Confirm every insulin or hormone figure in the routed output came from the clinician's input or carries `[VERIFY: current guideline/label]`.
- Note that the three proposed prompts under "New prompts to add" do not yet exist in the registry.
