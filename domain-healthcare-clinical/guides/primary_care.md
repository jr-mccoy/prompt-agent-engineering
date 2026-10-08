---
title: "Primary Care Guide"
category: healthcare-clinical/guides
description: "Primary care routing guide: trigger phrases, the existing prompts to route first, when not to use this guide, and the required safety cautions and escalation boundaries."
techniques:
  - CM-03
  - CM-09
  - DS-36
  - IT-26
difficulty: intermediate
tags:
  - primary-care
  - care-gaps
  - care-coordination
  - escalation
updated: "2026-10-06"
---

# Primary Care Guide

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
- "preventive visit", "annual wellness", "screening recommendations"
- "chronic disease follow-up", "multimorbidity management", "medication reconciliation"
- "care gaps", "risk factor modification", "shared decision-making"
- "transition of care", "post-discharge follow-up", "care coordination"
- "patient education", "adherence barriers", "health maintenance plan"

## Recommended Prompt Map (Existing + New)

### Existing prompts to route first
- `domain-healthcare-clinical/prompts/medicine_preventive_care_screening_advisor.md`
- `domain-healthcare-clinical/prompts/medicine_chronic_disease_management_planner.md`
- `domain-healthcare-clinical/prompts/medicine_medication_reconciliation.md`
- `domain-healthcare-clinical/prompts/medicine_care_coordination_transitions.md`
- `domain-healthcare-clinical/prompts/medicine_patient_education_adapter.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_history_elicitation.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_documentation.md`

### New prompts to add when repeated demand appears
- **Primary Care Visit Agenda Optimizer Prompt** (problem prioritization for time-limited visits)
- **Multimorbidity Tradeoff Planner Prompt** (benefit/burden balancing across conditions)
- **Longitudinal Preventive Care Tracker Prompt** (screening/vaccine cadence + follow-up logic)

## When Not to Use

Do **not** use this guide as primary routing when:
- The patient scenario is unstable and requires emergency triage as the first priority.
- The request is narrowly specialist (e.g., acute cardiogenic shock, severe psychosis) needing specialty workflows first.
- The user seeks direct diagnosis/treatment orders without clinician oversight.
- The task is administrative-only and unrelated to clinical reasoning or care planning.

## Required Safety Cautions and Escalation Boundaries

- Keep guidance in decision-support mode, not directive medical advice.
- Require explicit escalation triggers for red flags discovered in routine care (chest pain, neurologic deficits, severe dyspnea, suicidality, sepsis signs).
- Always include medication safety checks (interactions, allergies, renal/hepatic considerations, duplication).
- Require social-context and access barriers review, with escalation to care coordination/social work when safety or adherence is threatened.
- Escalate to specialist or emergency care when complexity exceeds outpatient safety boundaries or urgent instability is suspected.

## False-Positive Prevention

When using this guide:

❌ **DON'T:**
- Route through the prompt-map paths unchecked; several of these files moved into `care-plans/`, `communication/`, `pharmacology/`, `reasoning/` and `workflow/`, so resolve each before use.
- Mark a care gap closed in the routed output because a screening was "discussed"; closure needs the test, its date and result, or a documented decline.
- Let screening intervals or vaccine schedules in the output come from memory; they change often, so tag them `[VERIFY: current USPSTF/ACIP]`.

✅ **DO:**
- Check the medication-safety line against the actual med list: count the drugs reviewed and the duplications, interactions and renal/hepatic flags found, and say if any drug was skipped.
- Confirm that a red flag surfacing in routine care (chest pain, neurologic deficit, suicidality, sepsis signs) moves the output to escalation instead of staying on the visit agenda.
- Check that each social or access barrier recorded in the input appears somewhere in the plan.
