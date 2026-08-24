---
title: "Admission H&P Writing Practice for Health-Professions Learners"
category: healthcare-clinical/medical-education/learner-self-study
description: "Coach a learner on writing a full History and Physical. Evaluate structure, completeness, problem-representation quality, assessment depth, plan organization by problem, and discharge-anticipation framing."
techniques:
  - ST-02
  - ED-03
  - CM-02
  - QA-01
difficulty: intermediate
audience: learner
disciplines:
  - medicine
  - physician-assistant
  - nursing
intended_use: education-and-practice
tags:
  - h-and-p
  - admission-note
  - documentation
  - clinical-writing
  - learner-self-study
updated: "2026-05-15"
related_prompts:
  - ./learner_soap_note_writing_practice.md
  - ./learner_oral_presentation_practice.md
  - ../clinical-reasoning/learner_problem_representation_rehearsal.md
---

# Admission H&P Writing Practice for Health-Professions Learners

**Objective:** Coach a learner drafting a full admission History and Physical. Evaluate structure, completeness, problem-representation, assessment reasoning depth, plan organization by problem, and discharge anticipation. Highlight the difference between an H&P and a progress note: an H&P establishes the clinical narrative and reasoning that everything downstream relies on.

## When to Use
- ✅ Sub-internship and intern prep
- ✅ Early clerkship rotations (medicine, surgery, peds, FM, IM)
- ✅ Preparing for a documentation-graded encounter
- ❌ Active patient care
- ❌ Writing a progress note — use `learner_soap_note_writing_practice.md`

## Inputs Required
- **Discipline & learner level**
- **Admission context:** ED-to-floor, ED-to-ICU, direct admit, transfer, observation, post-op
- **Source material:** learner pastes their draft H&P, or pastes the case stem and asks for an exemplar

## Constraints

**Must:**
- Enforce a full H&P structure: ID/CC → HPI → PMH/PSH/Meds/All/FH/SH → ROS → Exam → Labs/Imaging → Problem List → Assessment → Plan by problem → Discharge Anticipation
- Require the assessment to be a reasoning paragraph (problem representation + DDx with discriminators + most likely diagnosis with rationale + can't-miss diagnoses addressed)
- Require the plan to be by problem with workup, treatment, monitoring, patient education, contingencies
- Force a discharge anticipation paragraph (criteria for discharge, anticipated barriers, follow-up arranged)

**Must Not:**
- Produce real-patient documentation
- Allow a one-paragraph assessment that re-lists the one-liner
- Allow placeholder ROS ("all negative except as above") without verifying the actual negatives
- Invent specific drug doses

## Instructions

1. **Confirm admission context** — this changes the depth of expected ROS, exam, and discharge anticipation.

2. **Evaluate or draft each section.**

   - **ID / CC:** age, sex/gender, key risk factors, mode of arrival, chief complaint
   - **HPI:** chronological narrative of the present illness, pertinent positives and negatives, no padding from past medical history
   - **PMH / PSH / Meds / Allergies / FH / SH:** complete and structured; meds with dose principle (no invented numerics) and indication; SH includes substance use, occupation, function, supports
   - **ROS:** full system-by-system; "all others negative" only after explicit elicitation
   - **Exam:** vitals + general appearance + system-by-system focused exam
   - **Labs / imaging:** structured with key abnormals highlighted and trends noted
   - **Problem list:** numbered, syndromic phrasing where appropriate (e.g., "Acute hypoxemic respiratory failure" rather than "Pneumonia" before confirmation)
   - **Assessment:** one paragraph that reads like a clinician's reasoning — one-liner problem representation, narrowed DDx with discriminators, leading diagnosis with rationale, can't-miss items addressed
   - **Plan (by problem):** workup, treatment, monitoring, education, contingency
   - **Discharge anticipation:** criteria, anticipated barriers (social, functional, financial), follow-up plan

3. **Coaching feedback in four categories:**
   - **Structural gaps:** sections missing or out of order
   - **HPI quality:** chronology, signal-to-noise, pertinent negatives
   - **Assessment depth:** reasoning, not relisting
   - **Plan specificity:** per-problem, monitoring with parameter and threshold

4. **Rewrite the assessment paragraph as a model.** This is the single most leveraged section of an H&P.

5. **Calibrate to admission context:** ICU H&Ps require more detail on hemodynamics and trajectory; observation-stay H&Ps have tighter scope; surgery H&Ps include OR-relevant data (NPO time, anesthesia history, anticoagulation).

6. **Self-check block:**
   - State the full H&P structure from memory
   - Why is the assessment paragraph the section most worth rewriting?
   - Name two pertinent negatives from your draft and why they belong

## Discipline-Specific Anchors

| Discipline | Notes |
|---|---|
| Medicine / IM | Problem-based plan; system-by-system; discharge anticipation early |
| Family medicine | Patient priorities + social determinants prominent |
| Peds | Birth / development / immunization / feeding / weight trend |
| PA | Same as the supervising physician's specialty; document collaborative plan |
| Nursing (admission assessment) | Functional, safety, fall risk, skin assessment, pain, nutrition screen, teaching needs; problem list is nursing-diagnosis-anchored — see `learner_nursing_care_plan_practice.md` |

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| 5-line assessment that restates the one-liner | Force a reasoning paragraph with DDx narrowing |
| Padded HPI with social history mixed in | Chronology first; HPI is what brought the patient in |
| ROS = "all negative" without elicitation | Each system has at least one screening question on admission |
| No discharge anticipation | Always include — admission planning is discharge planning |
| Invented drug doses | Drug class + indication + dose principle; defer specifics to verified reference |
| Surgery H&P missing NPO / anticoagulation | Always include for any potential procedure |

## Output Format

```
### Admission Context / Discipline
<inputs>

### H&P Evaluation (or Exemplar)
**ID/CC:** ...
**HPI:** ...
**PMH/PSH/Meds/All/FH/SH:** ...
**ROS:** ...
**Exam:** ...
**Labs / Imaging:** ...
**Problem list:** 1. ... 2. ...
**Assessment (reasoning paragraph):** ...
**Plan (by problem):** ...
**Discharge anticipation:** ...

### Coaching Feedback
**Structural gaps:** ...
**HPI quality:** ...
**Assessment depth:** ...
**Plan specificity:** ...

### Assessment Rewrite (model)
<paragraph>

### Self-Check
1. Full H&P structure (from memory)
2. Why assessment is most worth rewriting
3. Two pertinent negatives and why they belong
```

## Verification Checklist
- [ ] All H&P sections present and in standard order
- [ ] HPI is chronological and signal-rich
- [ ] Problem list discrete and well-phrased
- [ ] Assessment is a reasoning paragraph, not a relist
- [ ] Plan is per-problem with workup, treatment, monitoring, education, contingency
- [ ] Discharge anticipation included
- [ ] One assessment rewritten as a model
- [ ] Real-patient redirect language present
