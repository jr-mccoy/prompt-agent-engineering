---
title: "Biopsychosocial Intake Assessment Note Drafter"
category: psychology/documentation
description: "Compile a complete biopsychosocial intake assessment from clinician interview notes, including HPI, full history, MSE, formulation, provisional diagnoses, and initial plan."
techniques:
  - ST-04
  - DT-02
  - RT-02
  - QA-04
  - CM-02
  - DS-04
difficulty: advanced
tags:
  - intake
  - biopsychosocial
  - initial-evaluation
  - cpt-90791
  - cpt-90792
  - mental-status-exam
  - provisional-diagnosis
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
---

# Biopsychosocial Intake Assessment Note Drafter

## Objective

Convert a clinician's intake interview notes into a complete, structurally faithful biopsychosocial intake assessment that:

1. Covers all domains expected by accreditation bodies (Joint Commission / CARF) and by Medicaid/commercial payers for **CPT 90791** (psychiatric diagnostic eval) or **90792** (with medical services).
2. Synthesizes the data into a five-P case formulation (Presenting / Predisposing / Precipitating / Perpetuating / Protective).
3. Yields provisional ICD-10 diagnoses with rule-outs and the reasoning that supports each.
4. Produces an initial plan: modality, frequency, focus areas, referrals, immediate safety actions.

## When to Use

- First clinical encounter for outpatient mental health, psychiatry, IOP/PHP, SUD, or integrated-care settings.
- Re-intake after a long lapse in care or when transferring between programs.
- Generating a structured baseline for measurement-based care.

## Inputs / Context

Provide what is available; gaps will be flagged.

- **Demographics:** age, gender identity, pronouns, sex assigned at birth, race/ethnicity, primary language, immigration status if relevant, sexual orientation, relationship status, household composition, education, employment, insurance, legal status.
- **Referral source and reason for referral.**
- **HPI (history of present illness):** symptom onset, course, frequency, intensity, duration, triggers, prior episodes, what helped/didn't, current functional impact (work, school, relationships, self-care).
- **Past psychiatric history:** prior diagnoses, prior providers, prior medications (with response and side effects), prior hospitalizations / ED visits / IOP-PHP / residential, prior therapy modalities, longest period of stability.
- **Substance-use history:** age of first use, current substances, last use, frequency/quantity, route, withdrawal history, prior treatment, AUDIT/DAST scores if administered.
- **Risk history:** SI/HI/NSSI/SA history (lifetime and current), prior attempts (method, lethality, intent), exposure to suicide, access to means.
- **Trauma history:** what occurred, age, perpetrator relationship, disclosure history, current trauma symptoms (PCL-5 if administered). Use the client's chosen language; do not press for detail not offered.
- **Medical history:** active medical diagnoses, surgeries, current medications and supplements, allergies, last physical, PCP, head injuries, seizures, thyroid, pregnancy status, cardiac history.
- **Family psychiatric and SU history.**
- **Developmental history:** prenatal, milestones, learning, ADHD/ASD evaluation, IEP/504, adverse childhood experiences (ACE count if obtained).
- **Social history:** family of origin, relational history, current supports, friendships, faith / spirituality / community, hobbies.
- **Cultural formulation:** identity dimensions, cultural conceptualization of distress, psychosocial stressors, cultural factors in clinician-client relationship, immigration / acculturation if relevant.
- **Strengths and protective factors.**
- **Mental Status Exam observations** during the interview.
- **Outcome measures administered:** PHQ-9, GAD-7, PCL-5, AUDIT, DAST, MDQ, ASRS, C-SSRS, etc., with scores.
- **Collateral info reviewed** (records, prior providers, family report) with ROI status.

## Constraints

### Must

- Output all of the following labeled sections, in order: **Identifying Information**, **Referral Source / Chief Complaint**, **HPI**, **Past Psychiatric History**, **Substance Use History**, **Risk History**, **Trauma History**, **Medical History / Medications**, **Family History**, **Developmental History**, **Social / Relational History**, **Cultural Formulation**, **Strengths / Protective Factors**, **Mental Status Exam**, **Outcome Measures**, **Five-P Formulation**, **Provisional Diagnoses**, **Risk Stratification**, **Initial Plan**, **Billing**.
- The Five-P Formulation must be a single coherent narrative paragraph that integrates predisposing, precipitating, perpetuating, and protective factors and links them to the presenting problem.
- Provisional diagnoses must include ICD-10 code, full descriptor, and a 1-2 sentence rationale citing specific criteria met by the data; rule-outs must be listed with what would confirm or refute each.
- Risk stratification uses a named framework (Columbia C-SSRS levels, or stratification: low / moderate / high with explicit rationale citing static, dynamic, and protective factors).
- Initial Plan specifies modality, frequency, primary treatment targets, referrals (with provider type, rationale, urgency), immediate safety actions, and date for treatment-plan completion.
- Billing block includes CPT 90791 or 90792, total face-to-face minutes, ICD-10 codes, and one-sentence medical-necessity statement.

### Must Not

- Do not assign a diagnosis the data don't support; if criteria aren't clearly met, list as rule-out or deferred.
- Do not omit any of the labeled sections; if a section has no data, write `[deferred: rationale]` or `[clinician input required: ...]`.
- Do not paraphrase trauma details the client did not disclose; honor what was offered.
- Do not soften or omit risk content; risk history is a required section.
- Do not import demographic assumptions (e.g., assuming pronouns or relationship structure not stated by client).
- Do not fabricate; gaps are flagged.

## Instructions

1. Identify and list missing inputs by domain. Decide which can be deferred to a follow-up appointment vs which must be obtained before discharge (e.g., risk history cannot be deferred).
2. For each section, draft using the data provided; preserve client's own words for chief complaint and trauma narrative.
3. Compile MSE as a paragraph with all standard elements; avoid "WNL" — describe what was observed.
4. Compile outcome-measure scores in a table with date, score, and clinical interpretation.
5. Write the Five-P Formulation as an integrative paragraph; do not regurgitate the history.
6. Generate provisional diagnoses with ICD-10 codes and rationales tied to data. Add rule-outs.
7. Stratify risk using Columbia or comparable framework with explicit rationale.
8. Write the Initial Plan: modality, frequency, primary targets, referrals, safety actions, treatment-plan completion date (typically within 1–3 sessions).
9. Append billing block.
10. Run verification.

## Output Format

```
=== INTAKE ASSESSMENT (Biopsychosocial) ===

Client: [Initials/MRN]
Date of Service: [YYYY-MM-DD]    Time In/Out: [HH:MM–HH:MM]    Duration: [N min]
Modality: [in-person | telehealth]    Location of clinician: [...]    Location of client: [...]
CPT: [90791 | 90792]    Provisional ICD-10: [...]

IDENTIFYING INFORMATION
[Age, gender identity, pronouns, sex assigned at birth, race/ethnicity, primary language, marital/partner status, household, education, employment, insurance, legal.]

REFERRAL SOURCE / CHIEF COMPLAINT
[Referral source, reason. Chief complaint in client's own words: "..."]

HISTORY OF PRESENT ILLNESS
[Onset, course, frequency, intensity, duration, triggers, prior episodes, what helped/didn't, functional impact across work/school/relationships/self-care.]

PAST PSYCHIATRIC HISTORY
[Prior diagnoses, providers, medications with response and side effects, hospitalizations/ED/IOP/PHP/residential, prior therapy modalities, longest period of stability.]

SUBSTANCE USE HISTORY
[Per substance: age of first use, current frequency/quantity, last use, route, withdrawal history. AUDIT/DAST scores if administered. Prior SUD treatment.]

RISK HISTORY
[SI lifetime and current; prior attempts (method, lethality, intent, year); HI; NSSI; exposure to suicide; access to means including firearms and lethal medications.]

TRAUMA HISTORY
[Client-disclosed events at the level of detail offered. PTSD symptoms if endorsed. PCL-5 score if administered. Honor language client used.]

MEDICAL HISTORY / MEDICATIONS
[Active dx; surgeries; current meds and supplements with doses; allergies; last physical; PCP name; head injuries; seizures; thyroid; pregnancy status; cardiac history; sleep / pain / GI as relevant.]

FAMILY HISTORY
[Psychiatric, suicide, substance use; relevant medical (e.g., thyroid, cardiac affecting psychotropic choice).]

DEVELOPMENTAL HISTORY
[Prenatal, milestones, learning, ADHD/ASD evaluation history, IEP/504, ACEs (count if obtained).]

SOCIAL / RELATIONAL HISTORY
[Family of origin; current relationships; supports; friendships; faith / spirituality / community; hobbies.]

CULTURAL FORMULATION
[Identity dimensions; cultural conceptualization of the problem; psychosocial stressors related to cultural context; immigration / acculturation if relevant; cultural factors in clinician-client relationship.]

STRENGTHS / PROTECTIVE FACTORS
[Specific strengths, supports, prior coping wins, reasons for living, treatment adherence history.]

MENTAL STATUS EXAM
[Appearance / behavior / motor activity / eye contact; speech rate-rhythm-volume; mood (quoted); affect (range, congruence, mobility); thought process; thought content (including SI/HI/NSSI/AH/VH/delusions screening); cognition (orientation, attention, memory grossly); insight; judgment.]

OUTCOME MEASURES
| Measure | Date | Score | Interpretation |
|---------|------|-------|----------------|
| PHQ-9   | YYYY-MM-DD | X | [Severity] |
| GAD-7   | YYYY-MM-DD | X | [Severity] |
| PCL-5   | YYYY-MM-DD | X | [Above/below cutoff] |
| C-SSRS  | YYYY-MM-DD | [Level / Yes-No items endorsed] | [Risk band] |
| AUDIT   | YYYY-MM-DD | X | [Risk zone] |
| Other   | YYYY-MM-DD | X | [...] |

FIVE-P FORMULATION
[Single integrative paragraph weaving Predisposing, Precipitating, Perpetuating, and Protective factors with the Presenting problem. Goes beyond restatement of history; explains why this client has this problem now.]

PROVISIONAL DIAGNOSES
- [F##.##] [Full descriptor] — Rationale: [criteria met by specific data points].
- [F##.##] [Full descriptor] — Rationale: [...]
Rule-outs:
- [F##.##] [Descriptor] — needs: [data point that would confirm/refute].
Deferred:
- [Deferred dx if criteria insufficient at this time]: [what's needed].

RISK STRATIFICATION
Method: [Columbia C-SSRS / SAD PERSONS / clinical stratification].
Static factors: [...]
Dynamic factors: [...]
Protective factors: [...]
Stratification: [Low / Moderate / High] with explicit rationale.
Imminent risk: [Yes / No] with rationale.
Disposition: [Outpatient with safety plan / Higher LOC / ED transfer / Crisis team activation].

INITIAL PLAN
- Modality: [individual psychotherapy / med management / family / group / IOP].
- Frequency: [weekly / biweekly / 2x weekly] with rationale.
- Primary treatment targets (provisional, to be finalized in treatment plan): [Target #1; Target #2; Target #3].
- Referrals: [Type — Provider — Rationale — Urgency — Date scheduled or to be scheduled by].
- Safety actions taken today: [safety plan completed / lethal-means counseling / warm handoff / ED transfer / collateral contact / mandated report initiated].
- Coordination: [PCP / school / case manager / family with ROI status and dates].
- Treatment plan to be completed by: [Date — typically within 1–3 sessions].

BILLING
CPT [90791 | 90792] x 1, [N] minutes face-to-face. ICD-10: [codes].
Medical necessity: [one-sentence justification].

Clinician: [name, credentials, license #, signature, date/time]
```

## Verification

- [ ] All 20 labeled sections present and in order.
- [ ] Identifying info uses client's stated pronouns and identity (not inferred).
- [ ] Risk history is documented even if "no prior SI/HI/NSSI/SA reported" — never blank.
- [ ] MSE is descriptive, not "WNL."
- [ ] Outcome measures table includes interpretation column.
- [ ] Five-P Formulation is integrative narrative, not a re-list of the history.
- [ ] Each provisional diagnosis has criteria-tied rationale; rule-outs include disconfirming data needed.
- [ ] Risk stratification names a method and gives explicit rationale.
- [ ] Initial Plan includes immediate safety actions and treatment-plan completion date.
- [ ] CPT 90791 vs 90792 chosen correctly (90792 only if MD/DO/NP/PA performing eval with E&M).
- [ ] All gaps flagged with bracketed prompts; nothing fabricated.
