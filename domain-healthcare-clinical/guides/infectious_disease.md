# Infectious Disease Guide

## Trigger Phrases

Use this guide when requests include terms like:
- "sepsis", "septic shock", "lactate", "source control"
- "antibiotic selection", "de-escalation", "broad-spectrum coverage"
- "culture interpretation", "blood cultures", "resistance pattern"
- "antimicrobial stewardship", "duration of therapy"
- "hospital-acquired infection", "MDRO", "infection prevention"

## Recommended Prompt Map (Existing + New)

### Existing prompts to route first
- `domain-healthcare-clinical/prompts/medicine_sepsis_recognition_framework.md`
- `domain-healthcare-clinical/prompts/medicine_antibiotic_stewardship_advisor.md`
- `domain-healthcare-clinical/prompts/medicine_lab_diagnostic_interpreter.md`
- `domain-healthcare-clinical/prompts/medicine_drug_interaction_checker.md`
- `domain-healthcare-clinical/prompts/medicine_renal_hepatic_dose_adjustment.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_decision_support.md`

### New prompts to add when repeated demand appears
- **ID Syndrome-Based Empiric Therapy Prompt** (site-specific differential + local resistance context)
- **Culture De-escalation Decision Prompt** (timeline-to-culture synthesis + narrowing strategy)
- **Outbreak/Cluster Investigation Prompt** (case definition, exposure mapping, control actions)

## When Not to Use

Do **not** use this guide as primary routing when:
- The task is purely non-clinical policy writing without patient-care implications.
- The request is a one-off patient education rewrite with no infectious decision-making component.
- The main need is psychiatric crisis assessment or cardiology hemodynamics.
- The user asks for direct patient-specific prescribing without licensed clinician review.

## Required Safety Cautions and Escalation Boundaries

- Never present empiric antibiotic choices as definitive treatment recommendations.
- Require red-flag escalation language for:
  - hypotension or organ dysfunction consistent with sepsis/shock
  - concern for meningitis, necrotizing infection, or rapidly progressive illness
  - immunocompromised hosts with instability
- Force explicit checks for allergies, renal/hepatic function, drug interactions, and pregnancy/lactation when relevant.
- Include stewardship guardrails: reassess at 24–72 hours, narrow by cultures, justify duration.
- Escalate to urgent ID/emergency care when severe infection signals, diagnostic uncertainty with deterioration, or high-risk host factors are present.
