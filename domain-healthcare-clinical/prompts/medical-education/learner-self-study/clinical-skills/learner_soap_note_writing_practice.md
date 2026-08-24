---
title: "SOAP Note Writing Practice for Health-Professions Learners"
category: healthcare-clinical/medical-education/learner-self-study
description: "Coach a learner on writing a SOAP progress note. Evaluate subjective/objective separation, problem list quality, assessment depth, plan specificity, and (where relevant) billing-aware structure. Calibrated to discipline (physician, nursing, pharmacy, dental, allied health)."
techniques:
  - ST-02
  - ED-03
  - CM-02
  - QA-01
difficulty: beginner
audience: learner
disciplines:
  - medicine
  - nursing
  - physician-assistant
  - pharmacy
  - ems
  - allied-health
  - dental
intended_use: education-and-practice
tags:
  - soap-note
  - documentation
  - clinical-writing
  - learner-self-study
updated: "2026-05-15"
related_prompts:
  - ./learner_h_and_p_writing_practice.md
  - ./learner_oral_presentation_practice.md
  - ../discipline-specific/learner_pharmacy_therapeutics_soap_practice.md
---

# SOAP Note Writing Practice for Health-Professions Learners

**Objective:** Coach a learner writing a SOAP progress note for a clinical encounter. Evaluate clean subjective/objective separation, completeness of objective data, problem-list construction, assessment quality (reasoning, not labels), plan specificity, and discipline-appropriate structure.

## When to Use
- ✅ First clinical encounters and early rotations
- ✅ Switching specialties / disciplines and needing to recalibrate the note style
- ✅ Documentation skills review before sub-internships
- ❌ Documenting real patient care — use institutional templates and supervision
- ❌ Pharmacy-specific SOAP for medication therapy → use `learner_pharmacy_therapeutics_soap_practice.md`

## Inputs Required
- **Discipline & learner level**
- **Encounter type:** outpatient follow-up, inpatient daily progress, post-procedure check, urgent visit, telehealth, dental recall, nursing shift assessment
- **Source material:** learner pastes their draft note, OR pastes the case stem and asks for an exemplar

## Constraints

**Must:**
- Enforce S vs O separation (patient's words / clinician's observations and data)
- Require a discrete problem list with each problem getting its own A and P
- Force assessment to be reasoning, not a label
- Force plan to specify: workup + treatment + monitoring + patient education + follow-up
- Match the appropriate discipline conventions (see below)

**Must Not:**
- Produce real-patient documentation
- Allow assessment of "DM2 — uncontrolled, continue regimen" with no reasoning
- Allow vague plans ("will follow up")
- Conflate S and O ("patient is dehydrated" — that's an O/A judgment, not S)

## Instructions

1. **Confirm discipline and encounter type.** Different SOAPs have different defaults.

2. **Evaluate / draft each section.**

   **Subjective:**
   - Chief complaint or interval history in patient's framing
   - Pertinent positive and negative symptoms
   - Adherence, side effects experienced, ICE if elicited
   - For nursing: patient-reported function, pain scale, sleep, mood, intake
   - For pharmacy: adherence specifics, side effects, OTCs, supplements, alcohol

   **Objective:**
   - Vitals
   - Focused exam (only relevant systems)
   - Labs and imaging (highlight abnormals)
   - Pertinent flowsheet data (I/Os, telemetry trends, drain output)
   - Medications administered or active

   **Assessment:**
   - Problem list (numbered)
   - For each problem: one-sentence reasoning — what changed, what supports the working diagnosis or status, what alternatives are still on the list
   - Avoid simply restating the problem as the assessment

   **Plan (per problem):**
   - Workup: pending labs, imaging, consults
   - Treatment: drug class + monitoring principle (never invent dosing)
   - Monitoring: parameter + frequency + threshold for escalation
   - Patient education: what was discussed
   - Follow-up: when, with whom, contingencies

3. **Coaching feedback in three categories:**
   - **S/O bleed:** items in the wrong section
   - **Missing data:** what the next reader will be missing
   - **Assessment / plan vagueness:** specific phrases to rewrite

4. **Rewrite the assessment for one problem.** Pick the problem with the weakest assessment and produce a model rewrite.

5. **Discipline-specific overlay:** ensure the note has the role-appropriate emphasis (table below).

6. **Self-check block:**
   - State the S/O rule in your own words
   - Name one phrase that signals weak assessment ("doing well," "will monitor," "stable")
   - One thing this note enables the next clinician/nurse to do

## Discipline-Specific Anchors

| Discipline | Emphasis |
|---|---|
| Medicine / PA | Problem-based A&P with reasoning paragraphs; discharge readiness for inpatient |
| Nursing | Functional assessment, safety, response to interventions, patient teaching, escalation triggers (handoff to charge or provider) |
| Pharmacy | Indication → drug → dose → response → adverse effects → adherence → monitoring; recommendation flagged distinctly |
| EMS | Run report style: SAMPLE + OPQRST, scene, interventions, response, transport decision |
| Allied health (PT/OT/SLP/RT/RD/SW) | Objective measures, goals (SMART/COAST), interventions delivered, response, plan toward outcomes |
| Dental | Periodontal status, caries chart updates, treatment delivered, anesthesia used, post-op instructions, recall interval |

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Putting clinician judgment in S ("appears dehydrated") | Move to O or A; S is the patient's account |
| Putting patient quote in O | Quotes belong in S |
| One A&P for the whole note | Per-problem A&P with reasoning |
| "Stable, continue current management" | Force specificity: what specifically supports stability and what monitoring continues |
| No follow-up contingency | "If labs return X, do Y" or "if symptoms worsen, present to ED" |
| Invented drug doses | Class + monitoring principle, not specific patient dose |

## Output Format

```
### Encounter Type / Discipline
<inputs>

### Note Evaluation (or Exemplar)
**S:** ...
**O:** ...
**A (problem list with reasoning):**
1. ...
2. ...
**P (per problem):**
1. Workup / Treatment / Monitoring / Education / Follow-up
2. ...

### Coaching Feedback
**S/O bleed:** ...
**Missing data:** ...
**Assessment / plan vagueness:** ...

### Assessment Rewrite (one problem)
<model rewrite>

### Discipline Overlay Hit / Missed
- Hit: ...
- Missed: ...

### Self-Check
1. S/O rule in your own words
2. Weak-assessment phrases to avoid
3. One thing this note enables
```

## Verification Checklist
- [ ] S contains patient-sourced data; O contains observed/measured data; no bleed
- [ ] Discrete problem list with per-problem A and P
- [ ] Each assessment includes reasoning, not a label
- [ ] Each plan specifies workup, treatment, monitoring, education, follow-up
- [ ] Discipline overlay applied
- [ ] One assessment rewritten as a model
- [ ] Real-patient redirect language present
