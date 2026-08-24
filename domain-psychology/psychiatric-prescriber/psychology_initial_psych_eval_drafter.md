---
title: "Initial Psychiatric Evaluation Drafter (90792)"
category: psychology/psychiatric-prescriber
description: "Draft an initial psychiatric diagnostic evaluation note billable as 90792 (with medical services): CC/HPI, ROS, full histories, MSE, risk, workup, DSM-5-TR formulation, initial medication plan, and informed-consent documentation."
techniques:
  - ST-04
  - DT-01
  - DS-02
  - QA-04
  - CM-02
difficulty: advanced
intended_use: model-testing
tags:
  - psychiatric-evaluation
  - 90792
  - mental-status-exam
  - psychopharmacology
  - informed-consent
  - diagnostic-formulation
updated: "2026-06-08"
related_prompts:
  - domain-psychology/psychiatric-prescriber/psychology_med_management_progress_note.md
  - domain-psychology/psychiatric-prescriber/psychology_depression_med_algorithm_reasoner.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
---

# Initial Psychiatric Evaluation Drafter (90792)

## Objective

Generate a complete initial psychiatric diagnostic evaluation note suitable for billing CPT **90792** (psychiatric diagnostic evaluation **with** medical services), authored from the perspective of a prescriber (psychiatrist, psychiatric-mental-health NP, or supervised physician associate). The note must:

1. Document chief complaint, history of present illness, and a psychiatric review of systems.
2. Capture past psychiatric, medical, family, social, developmental, and substance-use histories.
3. Record a structured mental status examination (MSE) and a risk assessment.
4. Document the medical workup ordered (labs, vitals, EKG where indicated) consistent with the "medical services" requirement of 90792.
5. Produce a diagnostic formulation with DSM-5-TR descriptors and ICD-10-CM codes.
6. State an initial medication plan with named class and representative generic agent, starting dose, titration intent, monitoring, and **documented informed consent**.
7. Specify follow-up interval and a risk-reassessment hook.

## When to Use

- At a new patient's first prescriber visit when a diagnostic evaluation with medical decision-making is performed.
- When transferring a patient into a prescribing panel and a fresh psychiatric baseline is required.
- When re-establishing care after a lapse long enough to warrant a full re-evaluation.

## Inputs / Context Required

- **Referral source and reason** and the presenting concern in the patient's words.
- **Symptom history**: onset, course, severity, prior episodes, functional impact.
- **Past psychiatric history**: prior diagnoses, hospitalizations, suicide attempts, prior trials (agent, dose, duration, response, reason discontinued).
- **Medical history**, current medications, allergies, and relevant systems (cardiac, hepatic, renal, thyroid, seizure, pregnancy/lactation status).
- **Family psychiatric history** including medication response in first-degree relatives where known.
- **Social/developmental history**: living situation, supports, trauma, legal, occupational, substance.
- **Substance-use history**: agents, frequency, quantity, last use, withdrawal history.
- **Baseline measures**: PHQ-9, GAD-7, PCL-5, MDQ, AUDIT/DAST as applicable; vitals; weight/BMI.
- `[clinician input required: collateral information and prior records reviewed]`
- `[clinician input required: pregnancy/lactation status and reproductive plans if applicable]`

## Constraints

### Must

- Output sections in order: **Visit/Billing Header**, **CC**, **HPI**, **Psychiatric ROS**, **Past Psychiatric History**, **Substance History**, **Medical History / Meds / Allergies**, **Family History**, **Social & Developmental History**, **Mental Status Examination**, **Risk Assessment**, **Medical Workup / Labs Ordered**, **Diagnostic Formulation**, **DSM-5-TR / ICD-10 Diagnoses**, **Initial Medication Plan**, **Informed Consent**, **Follow-Up & Risk-Reassessment**, **Billing**, **Attestation/Signature**.
- Document at least one element justifying the "medical services" component of 90792 (e.g., medical ROS, labs ordered, EKG decision, medication initiation with monitoring).
- For each proposed agent: name the class AND a representative generic agent, starting dose, target/titration plan, and baseline + ongoing monitoring (labs, vitals, weight, EKG where class-indicated).
- Note black-box warnings and key drug-interaction cautions relevant to the proposed agent (e.g., antidepressant suicidality warning in patients < 25; QTc with certain agents; serotonin-syndrome combinations).
- Document informed consent: risks, benefits, alternatives (including no medication), and patient questions addressed.
- Anchor reasoning to a recognized framework by name where natural (APA Practice Guidelines; for youth, AACAP).
- Include a supervisor/collaborating-prescriber co-sign line when the author is a trainee or operates under collaborative practice.

### Must Not

- Do not bill 90792 without documenting a medical-services element; if none performed, flag to use 90791 instead.
- Do not propose a medication without dosing, monitoring, and consent documentation.
- Do not omit risk assessment or reduce it to "denies SI."
- Do not fabricate labs, prior trials, or family history; flag gaps as `[clinician input required: ...]`.
- Do not assert a definitive diagnosis when the data support only a provisional or rule-out; use specifiers honestly.

## Instructions

1. Build the **Header** (date, patient identifiers, visit type, place of service, time if time-based coding used).
2. Write **CC** (patient's words) and a chronological **HPI** with onset, course, severity, modifying factors, and functional impact.
3. Complete a **Psychiatric ROS** across mood, anxiety, psychosis, trauma, OCD, eating, sleep, cognition, substance.
4. Document **Past Psychiatric History** with a prior-trials table (agent / dose / duration / response / why stopped) — this drives later medication selection.
5. Record **Substance History**, **Medical History/Meds/Allergies**, **Family History**, **Social/Developmental History**.
6. Document a structured **MSE** (appearance, behavior, speech, mood, affect, thought process/content, perception, cognition, insight, judgment).
7. Complete a **Risk Assessment** (SI/HI/self-harm, protective/risk factors, access to means; use C-SSRS framing if available) and state risk level + plan.
8. Document **Medical Workup** ordered: baseline labs by indicated agent (e.g., CBC, CMP, TSH, lipids, HbA1c/glucose, lithium level + renal/thyroid, valproate level + LFTs/CBC, EKG for QTc-prolonging agents), vitals, weight/BMI, pregnancy test if indicated.
9. Write the **Diagnostic Formulation** (biopsychosocial synthesis; differential reasoning).
10. List **DSM-5-TR/ICD-10** diagnoses with specifiers and Z-codes.
11. Draft the **Initial Medication Plan** with class + generic, dose, titration, monitoring, warnings, interactions; reference the named guideline.
12. Document **Informed Consent**, **Follow-Up/Risk-Reassessment**, **Billing**, and **Signature/Co-sign**.
13. Run verification.

## Output Format

```
=== INITIAL PSYCHIATRIC EVALUATION (90792) ===

VISIT / BILLING HEADER
Patient: [Initials/MRN]   DOB: [YYYY-MM-DD]   Date of service: [YYYY-MM-DD]
Visit type: Initial psychiatric diagnostic evaluation with medical services
Place of service: [11 office | 02/10 telehealth]   Prescriber: [Name, credentials, NPI]

CHIEF COMPLAINT
"[Patient's own words]"

HISTORY OF PRESENT ILLNESS
[Onset, course, severity, triggers, modifiers, functional impact, prior treatment in this episode.]

PSYCHIATRIC REVIEW OF SYSTEMS
Mood: [...] | Anxiety: [...] | Psychosis: [...] | Trauma: [...] | OCD: [...]
Eating: [...] | Sleep: [...] | Cognition: [...] | Substance: [...]

PAST PSYCHIATRIC HISTORY
Diagnoses: [...]   Hospitalizations: [...]   Suicide attempts/self-harm: [...]
Prior medication trials:
| Agent (generic) | Max dose | Duration | Response | Reason stopped |
|-----------------|----------|----------|----------|----------------|
| [...] | [...] | [...] | [Adequate/partial/none] | [SE/ineffective/cost] |

SUBSTANCE HISTORY
[Agent, frequency, quantity, last use, withdrawal history, tobacco, caffeine.]

MEDICAL HISTORY / MEDICATIONS / ALLERGIES
PMH: [cardiac, hepatic, renal, thyroid, seizure, metabolic] | Current meds: [...] | Allergies: [...]
Pregnancy/lactation status: [clinician input required if applicable]

FAMILY HISTORY
[Psychiatric dx in first-degree relatives; known medication responses.]

SOCIAL & DEVELOPMENTAL HISTORY
[Living situation, supports, trauma, occupational, legal, education, developmental.]

MENTAL STATUS EXAMINATION
Appearance/behavior: [...] | Speech: [...] | Mood: "[...]" | Affect: [...]
Thought process: [...] | Thought content: [SI/HI/delusions] | Perception: [...]
Cognition: [orientation/attention/memory] | Insight: [...] | Judgment: [...]

RISK ASSESSMENT
SI: [none/passive/active — plan/intent/means] | HI: [...] | Self-harm: [...]
C-SSRS severity (if administered): [...]   Risk factors: [...]   Protective: [...]
Means access: [firearms/meds]   Risk level: [low/moderate/high]   Action: [...]

MEDICAL WORKUP / LABS ORDERED
Vitals: BP [..] HR [..]  Weight/BMI: [..]
Labs ordered: [CBC, CMP, TSH, lipids, HbA1c, agent-specific levels]
EKG (QTc): [ordered/not indicated]   Pregnancy test: [ordered/N/A]

DIAGNOSTIC FORMULATION
[Biopsychosocial synthesis; differential reasoning; what supports/argues against leading dx.]

DSM-5-TR / ICD-10 DIAGNOSES
Primary: [F##.##] [Descriptor, specifiers]
Secondary: [F##.##] [...]   Rule-out: [...]   Z-codes: [...]

INITIAL MEDICATION PLAN
Framework referenced: [APA Practice Guideline / AACAP / other]
Agent: [Class] — [representative generic] [starting dose]
  Titration: [plan to target dose]
  Monitoring: [baseline + ongoing labs/vitals/weight/EKG]
  Black-box / key warnings: [e.g., antidepressant suicidality < 25; QTc; metabolic]
  Interaction cautions: [e.g., serotonergic combinations, CYP interactions]
Rationale: [diagnostic match, prior-trial logic, comorbidity, side-effect fit]

INFORMED CONSENT
Risks discussed: [...]   Benefits: [...]   Alternatives (incl. no medication): [...]
Patient questions addressed: [Yes]   Consent obtained: [Yes/Verbal/Written]

FOLLOW-UP & RISK-REASSESSMENT
Follow-up: [interval]   Labs return reviewed at: [...]
Risk-reassessment hook: [re-screen SI/C-SSRS at next visit and on dose change]
Crisis instructions provided: [988 / local crisis line] — patient verbalized understanding.

BILLING
CPT: 90792 (psychiatric diagnostic eval with medical services)
Add-on (if applicable): [interactive complexity 90785]
ICD-10 linked: [codes above]

ATTESTATION / SIGNATURE
Prescriber: __________________  Date: ________
Supervising / collaborating prescriber co-sign (if applicable): __________  Date: ________
```

## Verification

- [ ] All required sections present in order.
- [ ] A medical-services element documented to justify 90792 (else flagged to use 90791).
- [ ] HPI is chronological with severity and functional impact.
- [ ] Prior-trials table present with dose, duration, response, reason stopped.
- [ ] Structured MSE complete across all domains.
- [ ] Risk assessment includes SI/HI/self-harm, means access, risk level, and action — not just "denies SI."
- [ ] Labs/workup ordered are appropriate to the proposed agent.
- [ ] Diagnoses use DSM-5-TR descriptors + ICD-10 codes with honest specifiers/rule-outs.
- [ ] Medication plan names class + generic, dose, titration, monitoring, warnings, interactions.
- [ ] Informed consent documents risks, benefits, alternatives, and questions addressed.
- [ ] Follow-up interval and risk-reassessment hook specified.
- [ ] Billing block present; co-sign line present where applicable.
- [ ] Nothing fabricated; gaps flagged with `[clinician input required]`.
