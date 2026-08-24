---
title: "Provisional vs. Rule-Out vs. Deferred Diagnosis Decision Aid"
category: psychology/diagnostic-formulation
description: "Guide the clinician through deciding when to assign provisional, rule-out, or deferred diagnostic status rather than a confirmed diagnosis"
techniques:
  - DT-02
  - QA-04
  - RT-02
  - ST-04
difficulty: intermediate
intended_use: model-testing
tags:
  - diagnostic-status
  - provisional-diagnosis
  - rule-out
  - deferred-diagnosis
  - DSM-5-TR
  - ICD-10-CM
  - diagnostic-reasoning
updated: "2026-06-08"
related_prompts:
  - domain-psychology/diagnostic-formulation/psychology_dsm5_differential_generator.md
  - domain-psychology/diagnostic-formulation/psychology_icd10_crosswalk_assistant.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# Provisional vs. Rule-Out vs. Deferred Diagnosis Decision Aid

## Objective

Help clinicians determine the appropriate diagnostic certainty status — **Provisional**, **Rule Out (R/O)**, or **Deferred (799.9 / Z03.89)** — for each candidate diagnosis at a given evaluation point. The decision aid maps the evidential threshold for each status, documents the conditions under which each is appropriate, and generates a structured diagnostic status block for the clinical record. All diagnostic status assignments require clinician judgment and attestation.

## When to Use

- Initial evaluation where diagnostic picture is incomplete but documentation cannot wait
- Complex presentations where one or more diagnoses require further assessment before confirmation
- When ordered testing (labs, neuropsychological evaluation, collateral information) has not yet returned
- Treatment planning that requires a billing diagnosis before full criterion confirmation is possible
- Supervision, case consultation, or peer review preparation requiring explicit diagnostic reasoning trails
- Audit situations where the basis for a provisional or deferred status must be documented

Not appropriate as a substitute for the DSM-5-TR differential generation process — use `psychology_dsm5_differential_generator.md` first to build the candidate list, then apply this decision aid to assign status to each candidate.

## Inputs / Context Required

- **Candidate diagnosis or diagnoses from the differential:** [clinician input required]
- **Available clinical data:** what has been gathered (MSE, intake interview, structured measures, collateral, records)
- **Pending clinical data:** what has been ordered or planned but not yet available
- **Evaluation purpose:** initial intake, re-evaluation, medication management, court-ordered, disability, return after lapse
- **Timeline constraints:** when must a working diagnosis appear in the record (e.g., treatment plan due date, insurance authorization deadline)
- **Setting:** outpatient, inpatient, forensic — coding conventions differ
- **Prior diagnoses on record:** confirmed, provisional, or documented by previous providers

## Constraints

### Must
- Distinguish among the four diagnostic certainty levels: **Confirmed**, **Provisional**, **Rule Out (R/O)**, and **Deferred**
- Apply DSM-5-TR conventions: Provisional is an official specifier that appears after the diagnosis name (e.g., "Major Depressive Disorder, single episode, moderate [Provisional]"); Rule Out and Deferred are documentation conventions rather than DSM-5-TR coded specifiers
- Provide the explicit evidential threshold that justifies each status — not just the label
- Flag when a provisional or deferred status must be re-evaluated and set a documentation timeline
- Apply ICD-10-CM outpatient coding convention: outpatient records should reflect the highest degree of certainty; signs/symptoms are coded when a diagnosis is not confirmed; deferred does not appear as a billable ICD-10-CM diagnosis
- Note when a provisional diagnosis has a billing code (the full diagnosis code is used with the provisional specifier in clinical documentation) vs. when coding should fall back to a symptom or Z code
- Include a re-evaluation trigger field for every non-confirmed diagnosis: what event or information will move the status to confirmed or dismissed

### Must Not
- Assign "Rule Out" or "Deferred" as ICD-10-CM billing codes — these are documentation conventions and do not translate to specific diagnostic codes for outpatient billing
- Suggest that "Provisional" means uncertain enough to avoid treatment planning — provisional diagnoses drive treatment; they are not a reason to withhold intervention
- Treat deferred as a permanent state — deferred diagnoses require a documented timeline for re-evaluation
- Omit the re-evaluation trigger; open-ended provisional status without a review plan is a documentation quality problem

## Instructions

1. **Establish the diagnostic certainty framework**. Define the four levels for the clinician to apply:

   | Status | DSM-5-TR Definition | When to Apply | ICD-10-CM Billing Impact |
   |--------|---------------------|--------------|--------------------------|
   | **Confirmed** | All criterion sets met, exclusions cleared, clinician attests | Full criterion threshold met with available data; exclusions addressed | Apply full specific diagnosis code |
   | **Provisional** | Diagnosis appears likely but information is incomplete; strong clinical presumption | Criteria appear likely met; key collateral, records, or test data pending; OR presentation is classic but duration criterion is not yet met | Use full diagnosis code; add "(Provisional)" in clinical documentation; same ICD-10-CM code as confirmed |
   | **Rule Out (R/O)** | Diagnosis is on the differential and must be actively evaluated | Reasonable prior probability; specific evidence is needed to confirm or dismiss; diagnosis would materially change treatment if confirmed | Document R/O in clinical notes; bill from the confirmed diagnosis or symptoms; do not list R/O as primary billing code outpatient |
   | **Deferred (799.9 / Z03.89)** | Insufficient information to evaluate; diagnosis cannot yet be meaningfully assessed | Presentation too acute, chaotic, or compromised for full evaluation; or client has declined full history; or evaluation purpose precludes complete assessment | Bill using presenting symptoms or Z code (Z03.89 for encounter for observation); document timeline for re-evaluation |

2. **For each candidate diagnosis**, apply the decision algorithm in order:

   **Step 1 — Criterion A threshold check:** Is the primary symptom threshold (Criterion A for most DSM-5-TR disorders) met, partially met, or not yet assessable?
   - Met → proceed to Step 2
   - Partially met → consider Other Specified category or Provisional if progression is expected
   - Not yet assessable → consider Deferred or Rule Out depending on probability

   **Step 2 — Duration criterion check:** Is the required duration met, not yet met but likely, or unknown?
   - Met → proceed to Step 3
   - Not yet met but appears to be progressing toward threshold → Provisional (duration expected to be met)
   - Unknown → Rule Out if probability warrants active evaluation; Deferred if evaluation is premature

   **Step 3 — Exclusion hierarchy check:** Have medical and substance etiologies been addressed? Have hierarchical DSM-5-TR exclusions been evaluated?
   - Cleared → proceed to Step 4
   - Pending (e.g., awaiting TSH, CBC, tox screen, outside records) → Provisional with documented pending workup
   - Cannot be cleared yet → Rule Out if the alternative etiology is plausible

   **Step 4 — Impairment/distress criterion check:** Is the distress/impairment threshold met?
   - Met → Confirmed or Provisional based on steps 1–3
   - Absent → reconsider whether full diagnosis applies; consider subclinical formulation or Other Specified
   - Unclear → Provisional with re-evaluation trigger

   **Step 5 — Clinician confidence calibration:** After steps 1–4, what is the overall confidence level?
   - Strong (>80% confident diagnosis is correct) + criteria met + exclusions cleared → Confirmed
   - Moderate (50–80%) + criteria appear likely + key data pending → Provisional
   - Low–moderate (25–50%) + diagnosis is clinically consequential → Rule Out with specific evaluation plan
   - Insufficient data to assess meaningfully → Deferred

3. **Generate a diagnostic status block** for each candidate diagnosis with the following fields:
   - Candidate diagnosis (DSM-5-TR name)
   - Assigned status (Confirmed / Provisional / Rule Out / Deferred)
   - Rationale (which step(s) drove the status decision)
   - Pending information (what is outstanding)
   - Re-evaluation trigger (what will change the status)
   - Re-evaluation timeline (`[clinician input required]`)
   - ICD-10-CM coding approach for current documentation

4. **Address the billing documentation interface**:
   - For Provisional: document the full diagnosis name followed by "(Provisional)" in the clinical record; the corresponding ICD-10-CM code is the same as the confirmed diagnosis code — the provisional specifier is a documentation convention, not a separate code
   - For Rule Out: document in the assessment/plan section of the note; bill using the confirmed diagnosis codes or presenting symptoms; if no diagnosis is confirmed yet in outpatient, bill from the highest-certainty symptom codes (e.g., F32.9 for depressive symptoms not meeting full criteria, or R45.1/R45.2 for specific symptoms)
   - For Deferred: document the reason for deferral; bill from Z03.89 or presenting symptom codes; do not list "Diagnosis Deferred" as a primary billing code without an appropriate ICD-10-CM code to accompany it

5. **Set re-evaluation plan**:
   - Every non-confirmed diagnosis requires a documented plan for status change
   - The re-evaluation plan should specify: (a) what information will be gathered, (b) by whom, (c) by what date or session number, and (d) what status change is anticipated
   - Provisional diagnoses without a re-evaluation date are a documentation quality risk

## Output Format

### Diagnostic Status Summary Block

```
EVALUATION DATE: [clinician input required]
EVALUATION CONTEXT: [outpatient intake / inpatient admission / re-evaluation / forensic / medication management]
CLINICIAN: [clinician input required]
```

---

### Diagnostic Status Table

| Diagnosis (DSM-5-TR Term) | Status | Rationale | Pending Information | Re-evaluation Trigger | Re-evaluation Date | ICD-10-CM Billing Approach |
|--------------------------|--------|-----------|--------------------|-----------------------|--------------------|---------------------------|
| [Diagnosis 1] | [Confirmed / Provisional / Rule Out / Deferred] | [Step(s) that drove decision; e.g., "Criterion A met; duration threshold not yet met at 10 days; provisional pending 14-day mark"] | [e.g., TSH result; outside records; collateral interview] | [e.g., Duration criterion met at 2 weeks; outside records received] | [clinician input required] | [e.g., F32.1 (same as confirmed; note "(Provisional)" in chart)] |
| [Diagnosis 2] | | | | | | |
| [Diagnosis 3 — Rule Out] | Rule Out | [e.g., "Hypomanic episode cannot be ruled out without longitudinal mood history; would change treatment plan if confirmed"] | [Longitudinal mood history; collateral from family] | [Collateral interview completed; hypomanic episode confirmed or dismissed] | [clinician input required] | [Bill from confirmed depressive disorder code; document R/O in assessment] |

---

### Re-Evaluation Plan

| Diagnosis | Pending Action | Responsible Party | Target Date | Expected Status Change |
|-----------|---------------|-------------------|-------------|----------------------|
| [Diagnosis 1] | [e.g., Order TSH, CBC; review outside records] | [clinician / referring PCP] | [clinician input required] | Provisional → Confirmed or dismissed |
| [Diagnosis 2] | | | | |

---

### Billing Documentation Note

```
For outpatient billing (ICD-10-CM):
  - Confirmed diagnoses: code at highest specificity available
  - Provisional diagnoses: use corresponding confirmed-diagnosis ICD-10-CM code + note "(Provisional)" in documentation
  - Rule Out diagnoses: do NOT bill as primary diagnosis; bill from confirmed codes or symptom codes
  - Deferred diagnoses: bill from presenting symptom codes (R or F symptom codes) or Z03.89 as appropriate
  - Verify payer-specific requirements for provisional and unspecified codes

[Clinician confirmation required before applying any code to a claim]
```

---

### Verification Checklist

- [ ] Every candidate diagnosis has an explicit assigned status with documented rationale
- [ ] No diagnosis is left in an implied or ambiguous status — each is labeled one of: Confirmed, Provisional, Rule Out, Deferred
- [ ] Provisional diagnoses have a re-evaluation trigger and target date documented
- [ ] Rule Out diagnoses have a specific evaluation plan (what data, by whom, by when)
- [ ] Deferred diagnoses have a reason for deferral and a timeline for reassessment
- [ ] ICD-10-CM billing approach is specified for each status and reflects outpatient vs. inpatient coding conventions
- [ ] No "Rule Out" or "Deferred" label appears as a standalone ICD-10-CM billing code
- [ ] Provisional specifier noted as documentation convention, not a separate code
- [ ] All final diagnostic status assignments tagged `[Clinician confirmation required]`
