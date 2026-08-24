# Primary Care Guide

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
