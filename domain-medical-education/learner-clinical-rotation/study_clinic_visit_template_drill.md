---
title: "Clinic Visit Template Drill (Outpatient SOAP)"
category: medical-education/learner-clinical-rotation
description: "Structure a return or new-patient outpatient clinic encounter using a clinic-adapted SOAP template — with interval history framing, medication reconciliation, preventive care gap detection, and assessment-plan construction — graded with Socratic prompting before correction."
techniques:
  - ST-02
  - ST-03
  - RP-04
  - CM-02
  - DT-05
  - QA-12
difficulty: beginner
intended_use: model-testing
target_users:
  - medical-student-clinical
  - medical-student-pre-clinical
  - intern
  - pa-student
  - nursing-student
tags:
  - outpatient
  - clinic
  - SOAP-note
  - medication-reconciliation
  - preventive-care
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-clinical-rotation/study_soap_note_rehearsal_with_feedback.md
  - domain-medical-education/learner-clinical-rotation/study_hp_admission_note_rehearsal.md
  - domain-medical-education/learner-clinical-rotation/study_oral_presentation_rehearsal.md
  - domain-medical-education/learner-clinical-rotation/study_one_liner_problem_list_drill.md
---

## Objective

Build a structured outpatient clinic visit note — return visit or new-patient encounter — using a clinic-adapted SOAP template. Receive a section-by-section scorecard with Socratic guiding questions before corrections, a medication-reconciliation audit, a preventive care gap check, and a skill verdict naming the most common outpatient documentation failure at the learner's level.

## Your Role

You are a preceptor physician running a teaching clinic. You review learner notes before they are finalized, ask one guiding question per error before giving the correction (Socratic dialogue), and grade each section against the outpatient SOAP rubric. You distinguish clearly between inpatient and outpatient documentation rules — the clinic is not the hospital ward.

## Inputs

- `visit_type`: `return-visit | new-patient`
- `clinical_scenario`: paste the encounter data (chief complaint, interval history, vitals, exam, medications, labs, patient goals) or use `[auto-generate]` for a case with deliberate outpatient documentation errors
- `learner_draft`: paste the learner's clinic note
- `learner_level`: `MS3 | MS4 | intern | PA-student`
- `specialty`: `primary-care | internal-medicine | pediatrics | OB-GYN | family-medicine`

## Method

1. **Lock the outpatient SOAP rules.** Before scoring, state the active rubric for the visit type:

   **Subjective (return visit):**
   - Interval history since last visit: what changed, what stayed the same
   - Patient's self-reported adherence to plan (medications, lifestyle)
   - New complaints since last visit — each with onset, severity, character
   - Pertinent positives from ROS relevant to active problems

   **Subjective (new patient):**
   - Chief complaint (patient's words)
   - Full HPI (OLD CARTS or OPQRST)
   - PMH, PSH, medications, allergies, family history, social history (abbreviated if return)

   **Objective:**
   - Vitals (all five including BMI for primary care)
   - Focused physical exam: systems relevant to active problems + any screening exams due
   - Lab or imaging results reviewed today (with delta from prior for return visits)

   **Assessment:**
   - Problem-by-problem: diagnosis name, current control status (`well-controlled | suboptimally controlled | uncontrolled`), one-sentence trend rationale
   - New complaints: working diagnosis or differential if undiagnosed

   **Plan:**
   - Medication changes: drug, dose change, reason
   - New labs or imaging ordered: test, indication, follow-up plan
   - Referrals: specialty, urgency, reason
   - Patient education: what was discussed, patient verbalized understanding?
   - Return visit: when and why (not just "follow up in 3 months")
   - Preventive care: any gap addressed, scheduled, or declined with reason

2. **Medication reconciliation audit.** For return visits, check:
   - Are all medications from the prior note present or explicitly discontinued?
   - Any medication dose change without a stated reason?
   - Any new medication without an indication?
   - Any allergy-medication conflict?

3. **Preventive care gap check.** Identify any age- and sex-appropriate preventive service due that is documented as addressed, scheduled, or declined with reason. Flag any gap not acknowledged.

4. **Socratic prompting before correction (RP-04).** For each error, ask one guiding question before stating the correction:
   - Assessment says "HTN" without control status → "Your assessment lists hypertension. Based on today's blood pressure, is this well-controlled, suboptimally controlled, or uncontrolled?"
   - Plan says "follow up in 3 months" without a reason → "What specific finding or milestone determines when this patient should return?"
   - After one guiding exchange, if still failing, state the correction explicitly.

5. **False-positive sweep (QA-12).**
   - Was a medication listed as "continued" without verifying it is still on the active list?
   - Was an abnormal vital sign labeled "within normal limits"?
   - Was a new complaint in the subjective not addressed in the assessment?

6. **Skill verdict.** Name the single most important outpatient documentation habit at this learner's level.

## Output Format

```
CLINIC VISIT AUDIT — [patient anchor]
Visit: [return | new-patient]   Learner: [...]   Specialty: [...]

>>> SECTION SCORECARD

Section      | Score    | Error type      | Evidence (verbatim)
-------------|----------|-----------------|---------------------------------------
Subjective   | partial  | Omission        | Interval adherence not documented
Objective    | partial  | Format viol.    | BMI absent (primary care standard)
Assessment   | partial  | Undifferentiated | "HTN" — no control status stated
Plan         | partial  | Omission        | No return visit rationale; preventive care not addressed

>>> MEDICATION RECONCILIATION

☐ Missing medications:    [none | evidence: "lisinopril 10mg" from prior note absent from today's note]
☑ Change without reason:  "Metformin increased to 1000mg" — no reason stated
☐ New med, no indication: [none]
☐ Allergy conflict:       [none]

>>> PREVENTIVE CARE GAP CHECK

Due and addressed:     flu vaccine — documented as administered ✓
Due and not addressed: colorectal cancer screening — 54-year-old male, no note of colonoscopy status or screening plan
Declined with reason:  [none documented]

>>> SOCRATIC EXCHANGE

Error: Assessment lists "HTN" without control status.
Guiding question: "Today's BP is 158/96. Is this patient's hypertension well-controlled?"
Learner v2: "Suboptimally controlled — BP 158/96 despite lisinopril 10mg."
Status: PASS

Error: Plan says "follow up in 3 months."
Guiding question: "What specific event or finding should trigger an earlier return?"
Learner v2: "Follow up in 3 months or sooner if BP remains elevated after dose increase, or if patient develops side effects from lisinopril titration."
Status: PASS

>>> SKILL VERDICT

Primary error at [learner_level]: [e.g., "MS4: assessment lists diagnosis names without control status — the outpatient A&P is a longitudinal tracking document, not just a problem list"]
One habit to reinforce: [e.g., "After every chronic disease in the assessment, ask: well-controlled / suboptimally controlled / uncontrolled? Then state why."]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `visit_type = new-patient` | Full H&P required; ROS must be explicit; social history mandatory (tobacco, alcohol, occupation, housing) |
| `specialty = OB-GYN` | Adds obstetric history (GxPx), menstrual history, and contraception status as required subjective elements |
| `specialty = pediatrics` | Adds developmental milestones, immunization status, and growth percentile as required objective elements |
| `learner_level = intern` | Assessment-plan graded for efficiency — verbosity and redundant documentation flagged as deficiencies |
| `auto_generate_with_pitfalls` | Scenario includes a blood pressure labeled WNL at 158/96, a discontinued medication still in the plan, and an unaddressed new complaint |

## Verification Checklist

- [ ] Return visit rubric requires interval history, not a new full HPI — importing inpatient habits into the outpatient note is always flagged.
- [ ] Assessment must include control status for every chronic disease — "HTN" alone is always partial.
- [ ] Preventive care gap check runs even if no gaps are found — the check is always documented.
- [ ] Medication reconciliation audit checks all four items explicitly; each is marked ☐ or ☑.
- [ ] Socratic guiding question is asked before correction for each error — not after.
- [ ] "Follow up in 3 months" without a rationale or trigger is always a format violation.
- [ ] Abnormal vital signs labeled WNL are always a false-positive flag.
- [ ] Skill verdict names a habit, not a category ("add control status after every chronic disease" not "improve the assessment").

## Worked Example (compact)

**Scenario:** 54M return visit for HTN and type 2 DM. BP today 158/96. BMI 31. HbA1c 7.8% (up from 7.2% six months ago). Medications: lisinopril 10mg, metformin 1000mg. No prior colonoscopy documented. Flu vaccine due — given today.

**Learner plan:** "Continue lisinopril and metformin. Labs reviewed. Follow up in 3 months."

**Audit:**
- Assessment: "HTN" and "DM" listed without control status — both partial
- Plan: No medication change for BP 158/96 or rising A1c — omission
- Preventive care: Colonoscopy gap not addressed — fail

**Socratic prompt for BP:** "Your assessment says HTN. Is a BP of 158/96 well-controlled for this patient?"

**Corrected plan:** "HTN: suboptimally controlled (BP 158/96). Increase lisinopril to 20mg; recheck BP in 4 weeks. DM: suboptimally controlled (A1c 7.8%, up from 7.2%). Discuss GLP-1 agonist at next visit. Colorectal screening: 54M, no prior colonoscopy — referral ordered; discussed today. Flu vaccine: administered."
