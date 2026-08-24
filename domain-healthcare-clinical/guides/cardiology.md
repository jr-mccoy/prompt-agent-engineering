# Cardiology Guide

## Trigger Phrases

Use this guide when requests include terms like:
- "chest pain workup", "ACS rule-out", "troponin trend"
- "heart failure", "HFrEF", "HFpEF", "volume status", "GDMT titration"
- "atrial fibrillation", "rate vs rhythm", "CHA2DS2-VASc", "HAS-BLED"
- "syncope", "palpitations", "arrhythmia risk"
- "anticoagulation decisions", "DOAC vs warfarin"
- "cardiac risk stratification", "perioperative cardiac risk"

## Recommended Prompt Map (Existing + New)

### Existing prompts to route first
- `domain-healthcare-clinical/prompts/medicine_heart_failure_titration_advisor.md`
- `domain-healthcare-clinical/prompts/medicine_anticoagulation_decision_support.md`
- `domain-healthcare-clinical/prompts/medicine_emergency_triage_decision_support.md`
- `domain-healthcare-clinical/prompts/medicine_lab_diagnostic_interpreter.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_decision_support.md`
- `domain-healthcare-clinical/prompts/medicine_drug_interaction_checker.md`
- `domain-healthcare-clinical/prompts/medicine_renal_hepatic_dose_adjustment.md`

### New prompts to add when repeated demand appears
- **Cardiology ACS Risk Stratifier Prompt** (HEART/TIMI-style framing + disposition options)
- **Arrhythmia Evaluation and Monitoring Prompt** (symptom timeline, trigger analysis, ambulatory monitoring options)
- **Valvular Disease Progression Review Prompt** (echo trend synthesis + follow-up timing)

## When Not to Use

Do **not** use this guide as primary routing when:
- The request is primarily psychiatric, behavioral, or psychotherapy-focused.
- The request is patient-facing direct medical advice without clinician mediation.
- The task requires real-time bedside emergency response rather than structured documentation or reasoning support.
- The dominant problem is non-cardiac (e.g., infectious source control, endocrine titration) and cardiology is secondary.

## Required Safety Cautions and Escalation Boundaries

- Treat all outputs as **clinical decision support**, not final medical decisions.
- Require explicit uncertainty language for diagnosis and disposition decisions.
- Always include immediate escalation triggers for:
  - ongoing ischemic chest pain
  - hemodynamic instability
  - malignant arrhythmia concern
  - syncope with high-risk features
- Never provide medication initiation or dose-change instructions without clinician oversight.
- Always prompt for contraindication checks (renal function, bleeding risk, drug-drug interactions, pregnancy when relevant).
- Escalate to cardiology/emergency evaluation when high-risk findings are present or data is incomplete for safe triage.
