# Psychiatry Guide

## Trigger Phrases

Use this guide when requests include terms like:
- "psychiatric assessment", "mental status exam", "diagnostic clarification"
- "suicide risk", "self-harm", "homicidal ideation", "safety planning"
- "mania", "psychosis", "catatonia", "capacity evaluation"
- "substance use with psychiatric symptoms", "withdrawal risk"
- "medication adherence", "side effect burden", "shared decision-making in psych meds"

## Recommended Prompt Map (Existing + New)

### Existing prompts to route first
- `domain-healthcare-clinical/prompts/medicine_psychiatric_assessment_support.md`
- `domain-healthcare-clinical/prompts/medicine_addiction_medicine_assessment.md`
- `domain-healthcare-clinical/prompts/medicine_goals_of_care_conversation_guide.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_decision_support.md`
- `domain-healthcare-clinical/prompts/medicine_drug_interaction_checker.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_documentation.md`

### New prompts to add when repeated demand appears
- **Acute Psychiatric Risk Stratification Prompt** (self-harm/violence risk factors + protective factors)
- **Complex Psychopharmacology Review Prompt** (polypharmacy burden, side-effect-risk balancing)
- **Capacity and Consent Evaluation Prompt** (decision-specific capacity framework)

## When Not to Use

Do **not** use this guide as primary routing when:
- The request is psychotherapy technique coaching better suited to psychology-focused domains.
- The need is immediate emergency intervention rather than structured assessment support.
- The request asks for direct instructions to a patient in active crisis without licensed clinician involvement.
- The main task is non-psychiatric medical stabilization.

## Required Safety Cautions and Escalation Boundaries

- Always treat outputs as adjunctive and require licensed clinician judgment.
- Include immediate escalation instructions for:
  - active suicidal intent/plan or inability to maintain safety
  - active homicidal intent or escalating violence risk
  - severe psychosis, delirium concern, or inability to care for self
- Avoid deterministic language about diagnosis; require differential framing and uncertainty acknowledgment.
- Never provide medication start/stop/titration directives without supervising prescriber oversight.
- Require emergency pathway activation (local crisis resources/ED/emergency services) for imminent safety risks.
