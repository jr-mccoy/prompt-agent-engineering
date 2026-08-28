---
title: "OSCE Station Designer"
category: medical-education/educator-simulation-design
description: "Design complete OSCE stations with student-facing task card, SP instructions, process checklist with critical fail items, global rating scale with behavioral anchors, standard-setting method guidance, station administration notes, and program learning outcome linkage for formative or summative clinical skills assessment."
techniques:
  - ST-02
  - CM-02
  - OC-01
  - QA-01
  - ED-04
difficulty: advanced
tags:
  - osce
  - assessment
  - clinical-skills
  - examiner-guide
  - standard-setting
  - competency-assessment
updated: "2026-05-15"
related_prompts:
  - ../meded_standardized_patient_scenario_writer.md
  - ../meded_clinical_skills_checklist_designer.md
  - ../meded_assessment_rubric_builder.md
---

# OSCE Station Designer

**Objective:** Design a complete, assessment-ready OSCE station — from student task card and SP instructions through examiner checklist, global rating scale, critical fail items, and standard-setting guidance — calibrated to a specified learner level, competency domain, and Miller's pyramid level.

## When to Use
- ✅ Designing a new OSCE station for a summative clinical skills examination
- ✅ Building a formative OSCE circuit for structured clinical skills feedback
- ✅ Retrofitting an existing clinical encounter into a standardized, scorable station
- ✅ Aligning an assessment station to a specific ACGME milestone, CanMEDS role, or EPA
- ❌ When a single checklist item (rather than a full station) is needed — use a clinical skills checklist designer instead
- ❌ When the competency being assessed is purely knowledge-based and requires no clinical performance — OSCE stations assess performance (Miller's "Shows" or "Does" levels); knowledge-based assessment belongs in written examination formats
- ❌ When the station will be the sole determinant of pass/fail for program completion — single-station high-stakes decisions require psychometric analysis and external expert review that exceed this prompt's scope; this prompt produces a structurally sound station that requires content expert review before summative deployment

## Inputs Required
- **Learner level:** M1, M2, M3, M4, Resident PGY-1 to PGY-3, Fellow, or Advanced Practice Learner
- **Competency domain:** Patient Care, Medical Knowledge, Interpersonal and Communication Skills, Professionalism, Practice-Based Learning, or Systems-Based Practice (ACGME); or equivalent CanMEDS role / EPA number
- **Miller's pyramid level:** Knows (written test), Knows How (written case), Shows How (OSCE), Does (clinical workplace) — confirm this station is designed for "Shows How"
- **Clinical skill / task:** the specific performance being assessed (e.g., "conduct a focused cardiovascular history and communicate findings to the patient," "obtain informed consent for a lumbar puncture," "manage an acute asthmatic exacerbation as team leader")
- **SP or manikin:** specify whether this station uses a live standardized patient, a task trainer/manikin, or a hybrid (SP with task trainer embedded)
- **Station time:** specify allotted student time (common: 8, 10, 12, 15, 20 minutes)
- **Program learning outcome this station serves:** which institutional or program-level outcome this station is designed to assess
- **Assessment purpose:** formative (feedback-oriented) or summative (pass/fail with standard-setting)

## Constraints

**Must:**
- Write the student task card and SP/examiner instructions as entirely separate documents — students never see SP or examiner materials
- Write checklist items that describe directly observable behaviors only — no items requiring examiner inference
- Include at least 2 critical fail items: behaviors whose absence constitutes automatic station failure regardless of overall checklist score
- Include a global rating scale with behavioral anchors for all five levels (1-5)
- Include standard-setting guidance specifying which method is appropriate for this program size and context, with the rationale
- Include station administration notes: props, equipment, room setup, timing signals, and re-standardization procedure for between-student intervals

**Must Not:**
- Mix process checklist items with global rating criteria — these measure different constructs and must remain separate instruments
- Write checklist items that require the examiner to infer internal states or intentions (e.g., "student was compassionate") — every item must describe a specific, observable action
- Omit standard-setting guidance — a checklist without a defined pass score is an incomplete assessment instrument
- Apply the same scoring standard to different learner levels — explicitly calibrate the pass standard, checklist content, and critical fail items to the specified learner level
- Write a station that could be fully completed by memorization alone — OSCE stations assess clinical performance; if a student can pass by reciting, the station tests the wrong Miller's level

## Instructions

1. **Collect inputs from the educator.**
   - Confirm: learner level, competency domain, Miller's pyramid level (confirm "Shows How"), clinical skill/task, SP or manikin, station time, program learning outcome, and assessment purpose (formative vs. summative).
   - Ask: Will an examiner be present in the room during the station, or will the SP complete the checklist? (This affects checklist item wording — what an SP can observe differs from what a trained examiner can observe.)
   - Ask: Is this station part of a circuit? If so, what other stations precede and follow it — this determines how much warm-up or carryover fatigue effects should be considered in station design.
   - Ask: Is there a physical examination component? If yes, specify which system — physical examination stations require a separate "SP-reported physical findings" script that must be written alongside the main scenario.

2. **Write the Station Overview.**
   - Station name, competency domain, Miller's pyramid level, learner level, allocated time.
   - One-sentence educational rationale: why this task was selected for OSCE assessment (what the circuit committee agreed was important to assess in a performance format).
   - Program learning outcome linkage: which institutional outcome this station operationalizes.

3. **Write the Student-Facing Task Card.**
   - Written in second person, present tense — this is what the student reads outside the station door.
   - Include:
     a. Patient name, age, sex, and one-sentence reason for visit (enough to orient but not enough to perform before entering)
     b. What the student is asked to do (explicit task instruction, e.g., "Please take a focused history of this patient's chest pain and explain your initial assessment to the patient before leaving the room")
     c. What the student is NOT asked to do (exclusions, e.g., "You do not need to perform a physical examination")
     d. Resources available in the room (e.g., stethoscope, blood pressure cuff, reference cards — or "no reference materials")
     e. Time allocated
   - The task card should be readable in under 60 seconds.

4. **Write the SP / Actor Instructions (Separate from Student Card).**
   - Patient character overview: who this person is, why they are here, what they want from the encounter.
   - Opening line: verbatim first words the SP says when the student enters.
   - Response guide: how the SP responds to the student's history-taking questions (what to volunteer, what to withhold, what requires direct inquiry).
   - Emotional cues with behavioral anchors: specify triggers and behavioral displays (not internal states).
   - Hidden history with unlock conditions: what sensitive information is disclosed only if directly asked, with the exact question type that unlocks disclosure.
   - Post-encounter behavior: what the SP does during the post-encounter examiner scoring interval (remain in role, exit room, complete self-rating if applicable).

5. **Write the Examiner Process Checklist.**
   - Write 15-25 binary items (observed / not observed), organized by category.
   - Each item must:
     a. Describe one directly observable behavior — subject is "student," verb is observable action
     b. Be scorable in real time without requiring replay or inference
     c. Be mutually exclusive — no two items should score the same behavior
   - Categories to cover (select those applicable to the station's clinical task):
     - Introduction and patient identification (e.g., "Student introduced themselves by name and role")
     - History-taking technique (e.g., "Student asked at least one open-ended question before transitioning to focused questions")
     - Clinical content coverage (e.g., "Student asked about onset, duration, and character of the symptom")
     - Physical examination (if applicable, per system)
     - Communication behaviors (e.g., "Student used language the patient could understand without technical jargon")
     - Professionalism (e.g., "Student washed hands or used hand sanitizer before physical contact")
     - Closure (e.g., "Student summarized findings and explained next steps before leaving the room")
   - Flag exactly 2-4 items as **Critical Fail Items** — if not observed, the student fails the station regardless of total checklist score. Critical fail items must be behaviors where absence represents a patient safety risk or fundamental professional failure (e.g., failure to wash hands before invasive procedure, failure to verify patient identity, failure to obtain consent before physical examination).

6. **Write the Global Rating Scale.**
   - Five-point scale with behavioral anchors for each level.
   - Anchors must describe observable performance characteristics, not adjectives alone:
     - 1 (Unacceptable): Specific description of what unacceptable performance looks like for this station
     - 2 (Below expectations): Specific description
     - 3 (Borderline — minimally acceptable): This is the most important anchor; write it in the most specific behavioral terms, as it defines the pass standard
     - 4 (Meets expectations): Specific description
     - 5 (Exceeds expectations): Specific description
   - Note: the global rating scale is holistic and should not be derived mechanically from the checklist score; it represents the examiner's overall gestalt assessment.

7. **Write the Standard-Setting Guidance.**
   - Specify the recommended standard-setting method for this station and rationale:
     - **Angoff Method:** Best for large programs (>100 students) with item-level difficulty data; requires panel of content experts who estimate the probability that a "minimally competent" student would pass each checklist item.
     - **Borderline Group Method:** Best for small programs (<50 students per cohort); examiners identify students at the borderline of competence during the OSCE and the mean score of borderline students becomes the cut score.
     - **Borderline Regression Method:** Best for stations with both checklist and global rating scores; regression of global rating on checklist score predicts the checklist score associated with the borderline global rating — most statistically robust for mixed-format stations.
     - **Modified Angoff with Global Rating Anchor:** Appropriate for new stations without prior score data; uses the Level 3 global rating anchor as the operational definition of minimally acceptable performance.
   - Write a brief implementation note explaining how to operationalize the recommended method for this specific station.
   - Write a remediation trigger note: at what score (or which critical fail) does the educator review the student's performance and initiate a skills improvement conversation?

8. **Write the Station Administration Notes.**
   - **Props and equipment list:** every physical item that must be in the room at station start (list precisely — omissions cause mid-exam chaos).
   - **Room setup description:** patient position (seated, supine, on exam table), furniture arrangement, lighting requirements, camera placement if recorded.
   - **Pre-station SP re-standardization procedure:** what the SP does between students to return to role-start conditions (e.g., reassume starting emotional state, replace tissues in box, close the gown).
   - **Timing signals:** specify what signals the start and end of the student encounter (bell, light, verbal, digital timer) and what signals the post-encounter examiner scoring interval.
   - **Examiner briefing note:** one paragraph describing what the examiner observes for at this station and common scoring errors to avoid.

9. **Write the Linkage to Program Learning Outcome.**
   - Name the program learning outcome this station assesses.
   - Write a one-sentence statement explaining what evidence of competence this station provides in the context of the broader curriculum.
   - Specify what other assessment evidence (e.g., in-training evaluation reports, written examination scores, simulation log) should triangulate with this station score before a competence decision is made — a single OSCE station is never sufficient evidence for a high-stakes competence determination.

10. **Deliver the complete station package.**
    - Organize output as five separate labeled documents: Station Overview, Student Task Card, SP Instructions, Examiner Checklist, Administration Notes and Standard-Setting Guide.
    - Add a brief quality assurance note: recommend that a content expert (clinician with expertise in the assessed domain) and an education expert (assessment specialist) review all materials before first administration.

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Mixing process checklist items with global rating criteria in the same instrument | Checklist items measure discrete, observable behaviors (process); global rating measures overall holistic competence (gestalt) — combining them produces a construct-invalid instrument |
| Checklist items requiring examiner inference ("student was empathic," "student was thorough") | Every item must describe a directly observable action: "Student acknowledged the patient's emotional response before continuing with history-taking" |
| Omitting standard-setting guidance | A checklist without a defined pass score is an incomplete assessment instrument; standard-setting is not optional for summative stations |
| Applying the same station to M3 and PGY-2 learners without recalibration | Miller's "Shows How" standard differs by training level; an M3 OSCE standard for history-taking differs from a residency standard; calibrate checklist content, critical fail items, and pass score separately |
| Writing critical fail items for minor communication lapses | Critical fail items must represent patient safety risks or fundamental professional failures — not suboptimal but not catastrophic behaviors |
| Global rating anchors written as adjectives only ("good," "excellent," "poor") | Every anchor level must describe observable performance characteristics specific to this station's clinical task |

## Output Format

The output should be organized as five clearly labeled documents:

### DOCUMENT 1: Station Overview
- Station name, competency domain, Miller's level, learner level, time allocation, educational rationale, program learning outcome linkage

### DOCUMENT 2: Student Task Card (Student-Facing)
- Patient name/age/sex, reason for visit, explicit task instruction, exclusions, resources available, time limit

### DOCUMENT 3: SP / Actor Instructions (SP Reference)
- Character overview, opening line, response guide, emotional cue behavioral anchors, hidden history with unlock conditions, post-encounter behavior

### DOCUMENT 4: Examiner Process Checklist
- Checklist items organized by category (15-25 binary items)
- Critical fail items flagged
- Global rating scale (1-5) with behavioral anchors
- Scoring instructions (how to combine checklist score and global rating for pass/fail determination)

### DOCUMENT 5: Administration Notes and Standard-Setting Guide
- Props and equipment list
- Room setup description
- SP re-standardization procedure
- Timing signal protocol
- Examiner briefing paragraph
- Recommended standard-setting method with implementation note
- Remediation trigger specification

---

## Example Output Snippet

The following is an example of a **partial Examiner Process Checklist** for an M3 OSCE station assessing informed consent for a lumbar puncture:

---

**Examiner Process Checklist — Informed Consent for Lumbar Puncture**

*Instructions: Mark each item "Observed" (1) or "Not Observed" (0). Score in real time during the encounter. Critical Fail items are marked [CF] — if not observed, student fails this station regardless of total score.*

**Introduction and Patient Orientation**
- [ ] 1. Student introduced themselves by name and role before beginning (1/0)
- [ ] 2. Student confirmed patient's name before proceeding (1/0)
- [ ] **[CF] 3. Student explained that they were asking for the patient's consent before performing any part of the procedure (1/0)**

**Disclosure of Procedure Purpose and Process**
- [ ] 4. Student explained why the lumbar puncture was recommended in language the patient could understand (1/0)
- [ ] 5. Student described what the procedure involves, including patient positioning (1/0)
- [ ] 6. Student described the expected duration of the procedure (1/0)

**Risk Disclosure**
- [ ] 7. Student disclosed post-procedure headache as a risk (1/0)
- [ ] 8. Student disclosed infection as a risk (1/0)
- [ ] 9. Student disclosed nerve injury or bleeding as risks (1/0)
- [ ] **[CF] 10. Student disclosed the option to refuse consent without affecting ongoing care (1/0)**

**Questions and Confirmation**
- [ ] 11. Student asked if the patient had questions before asking for consent (1/0)
- [ ] 12. Student confirmed patient's understanding using teach-back or equivalent ("Can you tell me in your own words what I've explained?") (1/0)
- [ ] 13. Student asked for the patient's decision before concluding the encounter (1/0)

**Global Rating**
- 5 — Exceeds expectations: Consent discussion was patient-centered, thorough, and responsive to the patient's questions; all risks disclosed with appropriate depth; patient appeared fully informed and respected throughout
- 4 — Meets expectations: All required elements disclosed; minor gaps in depth or responsiveness to patient questions; patient appeared adequately informed
- 3 — Borderline: Essential elements present but significant gaps in risk disclosure or failure to verify understanding; examiner would not be confident the patient was fully informed
- 2 — Below expectations: Multiple significant omissions; consent discussion incomplete or poorly organized
- 1 — Unacceptable: Failed to obtain consent, failed to disclose major risks, or patient appeared confused or coerced

---

## Verification Checklist
- [ ] Learner level explicitly specified and checklist content calibrated to that level's expected performance standard
- [ ] Competency framework alignment named (ACGME domain / CanMEDS role / EPA number) and reflected in station overview
- [ ] Student task card and SP instructions are separate documents with no overlap of content
- [ ] All checklist items describe directly observable behaviors — no inference required
- [ ] At least 2 critical fail items specified with patient-safety or professionalism rationale
- [ ] Global rating scale has behavioral anchors at all 5 levels, with Level 3 written in the most specific behavioral terms
- [ ] Standard-setting method specified with rationale and implementation note
- [ ] Station administration notes include complete props list, SP re-standardization procedure, and timing signal protocol
