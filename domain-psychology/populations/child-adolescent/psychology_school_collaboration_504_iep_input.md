---
title: "School Collaboration: 504/IEP Mental-Health Input"
category: psychology/populations/child-adolescent
description: "Structured mental-health clinician input for a 504 Plan or IEP meeting that translates diagnosis and functional impairment into educational-impact language and proposes evidence-based accommodations, within the bounds of clinician scope and FERPA/release authorization."
techniques:
  - ST-04
  - RT-02
  - DS-02
  - CM-02
  - QA-04
  - ED-04
difficulty: intermediate
intended_use: model-testing
tags:
  - 504-plan
  - IEP
  - IDEA
  - school-collaboration
  - accommodations
  - functional-impairment
  - release-of-information
  - educational-impact
updated: "2026-06-08"
related_prompts:
  - domain-psychology/intake-assessment/psychology_pediatric_intake_with_caregiver.md
  - domain-psychology/populations/child-adolescent/psychology_adolescent_intake_with_developmental_lens.md
  - domain-psychology/populations/child-adolescent/psychology_pediatric_anxiety_protocol_session_plan.md
  - domain-psychology/documentation/psychology_collateral_contact_note.md
---

# School Collaboration: 504/IEP Mental-Health Input

## Objective

Produce a clinician's mental-health input document for a student's 504 Plan (Section 504 of the Rehabilitation Act) or IEP (Individualized Education Program under IDEA) meeting that:

1. Confirms scope and authorization: valid release of information (ROI) on file, FERPA/HIPAA boundary respected, clinician contributing input — not determining eligibility (the school team decides).
2. Translates the student's diagnosis and clinical findings into educational-impact language: how the condition affects learning, attention, attendance, behavior, and social functioning in the school setting.
3. Distinguishes the 504 vs. IEP frame: 504 = reasonable accommodations for a disability that substantially limits a major life activity; IEP = specialized instruction for a qualifying disability that adversely affects educational performance (one of IDEA's 13 categories, e.g., Emotional Disturbance, Other Health Impairment).
4. Proposes specific, evidence-based, implementable accommodations/supports tied to documented impairments.
5. Recommends data, evaluations, or monitoring the team may consider.
6. Stays within clinician scope: does not write the plan, determine eligibility, or guarantee outcomes.

## When to Use

- When a school requests, or a caregiver consents to, mental-health clinician input for a 504 or IEP meeting.
- When a clinician needs to translate a treatment record into educationally relevant language and accommodation recommendations.
- For documenting the clinician's contribution as a collateral contact.

## When NOT to Use

- For conducting a psychoeducational or special-education eligibility evaluation (that is a separate, formal assessment).
- Without a valid release of information authorizing disclosure to the school.
- For legal advocacy or due-process representation — that is outside clinical scope.
- For students 18+ where the student (not caregiver) holds educational rights, unless the student authorizes.

## Inputs / Context Required

- **Student:** Initials/MRN, age, grade, school.
- **Authorization:** Valid ROI to the named school/district; date and scope; who holds educational rights (caregiver vs. student if 18+).
- **Meeting type:** 504 vs. IEP; initial vs. review/re-evaluation.
- **Clinical record:** Diagnosis(es), functional impairments, treatment, response, relevant measures (e.g., CBCL/TRF, SCARED, PHQ-A).
- **School-reported data (if available):** Teacher report, attendance, grades, discipline, existing accommodations and their effectiveness.
- **Caregiver/student goals** for the meeting.
- `[clinician input required: any safety considerations relevant to the school setting (e.g., suicidality, self-harm, elopement) and corresponding school safety supports]`

## Constraints

### Must

- Confirm and document a valid ROI before any disclosure; name the recipient and scope.
- Frame the input as clinician contribution; state explicitly that the 504/IEP team determines eligibility and the plan.
- Translate clinical findings into educational-impact terms (learning, attention, attendance, behavior, peer functioning), not raw clinical jargon.
- State whether a 504 or IEP frame applies and, for IEP, reference the relevant IDEA category as a clinical impression for the team's consideration (not a determination).
- Propose accommodations that are specific, measurable where possible, and implementable in a classroom.
- Note safety-relevant school supports when applicable (counselor access, check-in/check-out, re-entry plan after hospitalization, safety plan coordination).
- Flag gaps with `[clinician input required: ...]`; do not fabricate school data or test scores.

### Must Not

- Do not disclose protected information without a valid ROI; do not exceed the ROI's scope.
- Do not determine eligibility, write the plan, or promise specific services/outcomes.
- Do not over-disclose sensitive clinical content (e.g., trauma detail, family content) beyond what is educationally necessary.
- Do not recommend accommodations unsupported by the documented impairment.
- Do not fabricate teacher reports, attendance/discipline data, or evaluation results.

## 504 vs. IEP Frame Reference

| Dimension | Section 504 Plan | IEP (IDEA) |
|-----------|------------------|------------|
| Legal basis | Section 504 of the Rehabilitation Act / ADA | Individuals with Disabilities Education Act |
| Threshold | Disability substantially limiting a major life activity | Qualifying disability in 1 of 13 categories adversely affecting educational performance AND needing specialized instruction |
| What it provides | Reasonable accommodations/access | Specialized instruction + related services + measurable goals |
| Relevant categories | Broad (any qualifying impairment) | e.g., Emotional Disturbance; Other Health Impairment (often ADHD); Autism; Specific Learning Disability |
| Clinician role | Document impairment + recommend accommodations | Document impairment + impact + recommend supports for team to consider |

## Instructions

1. **Confirm authorization and scope.** Document the ROI, recipient, scope, and who holds educational rights.
2. **State the frame and role.** Identify 504 vs. IEP and explicitly position the clinician as contributing input, not deciding.
3. **Summarize relevant clinical findings** at the minimum necessary level: diagnosis and the functional impairments educationally relevant.
4. **Translate to educational impact.** For each impairment, describe how it shows up in the school setting (learning, attention, attendance, behavior, peers).
5. **Map impairments to accommodations.** Propose specific, implementable accommodations/supports; for IEP, note possible goal areas for the team.
6. **Address safety supports** if applicable (counselor access, re-entry plan, safety-plan coordination).
7. **Recommend data/monitoring** (teacher rating scales, progress monitoring, re-evaluation timing).
8. **Write the input document** using the output format below.
9. **Run verification.**

## Output Format

```
=== MENTAL-HEALTH CLINICIAN INPUT FOR 504 / IEP MEETING ===

Student: [Initials/MRN]    Age: [N]    Grade: [N]    School: [...]
Date: [YYYY-MM-DD]    Meeting type: [504 — initial/review | IEP — initial/review/re-eval]
Clinician: [Name, credentials, practice]

─────────────────────────────────────────
AUTHORIZATION & SCOPE
─────────────────────────────────────────
Valid ROI on file to [school/district]: [Yes — dated YYYY-MM-DD; scope: ...]
Educational rights held by: [Caregiver(s) / Student (age 18+) — authorized: Y/N]
Disclosure limited to minimum necessary for educational planning: [Confirmed]
Role statement: This input is a clinical contribution for the team's consideration. The 504/IEP team determines eligibility and finalizes the plan.

─────────────────────────────────────────
RELEVANT CLINICAL SUMMARY (minimum necessary)
─────────────────────────────────────────
Diagnosis(es) (educationally relevant): [DSM-5-TR + ICD-10-CM]
Treatment status: [In treatment since ...; modality; response]
Relevant measures: [CBCL/TRF, SCARED, PHQ-A, etc. — bands only]

─────────────────────────────────────────
EDUCATIONAL IMPACT (functional impairment → school setting)
─────────────────────────────────────────
| Impairment | How it presents at school | Domain affected |
|------------|---------------------------|-----------------|
| [e.g., anxiety/panic] | [avoidance, school refusal, test panic] | [Attendance/Learning] |
| [e.g., inattention] | [off-task, incomplete work, missed instructions] | [Attention/Learning] |
| [e.g., emotion dysregulation] | [escalation, shutdowns, peer conflict] | [Behavior/Social] |
[clinician input required: complete from record + school data]

─────────────────────────────────────────
FRAME RECOMMENDATION (for team consideration)
─────────────────────────────────────────
Suggested frame: [504 accommodations / IEP — possible IDEA category for team to consider: Emotional Disturbance / Other Health Impairment / Autism / SLD]
Rationale: [Substantial limitation vs. need for specialized instruction — clinical reasoning]

─────────────────────────────────────────
RECOMMENDED ACCOMMODATIONS / SUPPORTS
─────────────────────────────────────────
[Specific and implementable. Tie each to an impairment above.]
- [e.g., Preferential seating; extended time on tests] → addresses [...]
- [e.g., Scheduled breaks / access to counselor or calm space] → addresses [...]
- [e.g., Check-in/check-out; behavior support plan] → addresses [...]
- [e.g., Modified attendance/late-arrival plan during treatment] → addresses [...]
For IEP, possible goal areas for the team: [e.g., self-regulation, work completion, social skills]

─────────────────────────────────────────
SAFETY SUPPORTS (if applicable)
─────────────────────────────────────────
[Counselor access / re-entry plan after hospitalization / coordination with safety plan / crisis protocol] : [...]
Risk reassessment hook: [Clinician available for team consult; reassess at ...]

─────────────────────────────────────────
RECOMMENDED DATA / MONITORING
─────────────────────────────────────────
Teacher rating scales / progress monitoring: [...]
Re-evaluation / review timing suggestion: [...]
Additional evaluations the team may consider: [psychoeducational / OT / speech — as relevant]

─────────────────────────────────────────
COLLATERAL CONTACT NOTE
─────────────────────────────────────────
Documented as collateral contact in client chart: [Date; participants; ROI referenced]
(Note: clinician participation in a 504/IEP meeting is typically a non-billable collateral/coordination activity unless a payer-specific code applies — confirm with billing.)
```

## Verification

- [ ] Valid ROI confirmed and scope documented; minimum-necessary standard applied.
- [ ] Who holds educational rights documented (caregiver vs. 18+ student).
- [ ] Role statement present: clinician contributes input; team determines eligibility/plan.
- [ ] Clinical findings translated into educational-impact language, not raw jargon.
- [ ] 504 vs. IEP frame addressed; IDEA category, if any, offered for consideration (not determined).
- [ ] Each recommended accommodation tied to a documented impairment and implementable.
- [ ] Safety supports addressed when applicable, with a reassessment/consult hook.
- [ ] Data/monitoring and re-evaluation timing recommended.
- [ ] Documented as a collateral contact in the chart.
- [ ] Gaps flagged with `[clinician input required: ...]`; no fabricated school data or scores.
