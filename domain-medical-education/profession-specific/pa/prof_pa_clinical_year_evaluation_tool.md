---
title: "PA Clinical Year Rotation Evaluation Tool — PAEA Competencies + EOR Blueprint + Procedural Logbook Audit"
category: medical-education/profession-specific/pa
difficulty: advanced
intended_use: model-testing
description: "Author a clinical-year preceptor evaluation tool for a PA student rotation (family medicine, internal medicine, surgery, peds, OB/GYN, emergency medicine, behavioral health, elective). Cover PAEA core competencies (medical knowledge, interpersonal skills, clinical and technical, professionalism, practice-based learning, systems-based practice), EOR-exam-aligned topic exposure, procedural logbook audit, and entrustment ratings tied to PA-CAT and ARC-PA-required learning outcomes. Output is preceptor-facing one-page tool + rotation-specific competency rubric."
techniques:
  - ST-02
  - ST-03
  - DT-05
  - DS-01
  - RT-05
  - QA-16
target_users:
  - pa-student
  - clinical-educator
  - program-director
  - curriculum-designer
tags:
  - pa-clinical-year
  - rotation-evaluation
  - paea
  - eor
  - arc-pa
  - educator-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/profession-specific/pa/prof_pa_pance_blueprint_drill.md
  - domain-medical-education/profession-specific/nursing/prof_rn_clinical_evaluation_tool.md
---

## Objective

Build a preceptor-facing rotation evaluation tool that scores a PA student against PAEA core competencies, audits exposure to EOR-blueprint topics, and reviews the procedural logbook. Output is a one-page tool + rotation-specific addendum + a remediation-trigger block.

## Your Role

PA program assessment-faculty / clinical coordinator. You write to ARC-PA (Accreditation Review Commission on Education for the Physician Assistant) Standards and PAEA EOR blueprint expectations. Preceptors are practicing PAs / MDs / DOs who may not be familiar with PA-specific assessment language — clarity and observable behaviors are prioritized over jargon.

## Inputs

- `rotation`: free text (e.g., "family medicine," "internal medicine," "general surgery," "pediatrics," "OB/GYN," "emergency medicine," "behavioral health," "elective: ortho")
- `rotation_length_weeks`: integer (typically 4–8)
- `eor_exam`: `PAEA-EOR | program-developed-EOR | no-EOR`
- `competency_framework`: `PAEA-core-competencies | NCCPA-competencies | program-defined`
- `entrustment_scale`: `5-level-O-CON-DS-IS-AP | 4-level | 3-level-binary-with-distance` (default 5-level Chen entrustment scale for PA: Observe-Only / Co-activity / Direct Supervision / Indirect Supervision / Autonomous Practice)
- `procedural_logbook_required`: boolean (default true)
- `setting`: `outpatient | inpatient | OR | ED | hybrid`
- `failing_threshold_required`: boolean (default true)

## Method

1. **Lock the framework (CM-02).** Select the competency set:
   - **PAEA Core:** Medical Knowledge, Interpersonal & Communication Skills, Patient Care (Clinical & Technical), Professionalism, Practice-Based Learning & Improvement, Systems-Based Practice — 6 domains.
   - **NCCPA:** maps similarly but uses slightly different language.
   - **Program-defined:** preceptor pastes the program's 4–8 domain list.

2. **Build entrustment scale (DS-01 Chen-style for PA):**
   - **O — Observe only:** student observes; preceptor performs.
   - **CON — Co-activity:** student performs with preceptor performing concurrent steps.
   - **DS — Direct supervision:** student performs; preceptor in the room, immediately available.
   - **IS — Indirect supervision:** student performs; preceptor available (same building, on-call).
   - **AP — Autonomous practice (in-rotation only):** student performs; preceptor reviews after.
   *Note: AP rating in PA student context is for the rotation, not actual independent practice — final entrustment for practice is post-graduation.*

3. **Per competency domain, write rotation-specific behavioral anchors (DT-05).** Each domain × rotation gets a 1-line anchor at each entrustment level. Example for Patient Care in family medicine:
   - O: "Observes well-child visit; takes notes."
   - CON: "Performs HEENT exam with preceptor performing GU portion."
   - DS: "Performs full physical with preceptor in the room; preceptor confirms findings."
   - IS: "Performs visit, presents to preceptor, who briefly verifies; staff sees own patients next door."
   - AP: "Student manages routine visit independently; preceptor reviews note and concurs."

4. **Build EOR-blueprint exposure audit (RT-05).** For the rotation's PAEA EOR (or program EOR), list the blueprint topic areas with checkboxes for `cases-seen` count. Example for family medicine EOR: HTN management, T2DM, URI, low back pain, depression screening, well-child, contraception, COPD, geriatric assessment. Threshold: minimum 2 cases per high-yield topic.

5. **Build procedural logbook audit.** Rotation-specific. Examples:
   - Surgery: minimum suturing (3 simple, 1 layered), sterile gowning/gloving (5), Foley/NG (2 each), surgical first-assist (5).
   - EM: laceration repair (5), I&D (2), splinting (3), LP attempt (1), procedural sedation (1 observation).
   - OB/GYN: pelvic exam (5), Pap (3), prenatal visit (5), labor monitoring (2), delivery observation (2).
   - Each procedure: count + entrustment-level achieved.

6. **Build remediation trigger block (QA-16).** Name what triggers:
   - Mid-rotation re-baseline: any DS rating still required at midpoint when IS expected.
   - Failure of rotation: any O-only rating in core domains at end-of-rotation; failed EOR; safety concern.
   - Probation: failed first attempt at EOR with passing clinical evaluation.

## Output Format

```
PA CLINICAL YEAR ROTATION EVALUATION
Rotation: [...]   Length: [...] wks   Setting: [...]
Competency framework: [...]   Entrustment scale: [...]
EOR exam: [...]   Logbook required: [...]

>>> ENTRUSTMENT SCALE

O — Observe only: [...]
CON — Co-activity: [...]
DS — Direct supervision: [...]
IS — Indirect supervision: [...]
AP — Autonomous practice (rotation-context only): [...]

>>> COMPETENCY MATRIX

═══ Domain 1: [Medical Knowledge / Patient Care / etc.]
  Rotation-specific anchors:
    O: [...]
    CON: [...]
    DS: [...]
    IS: [...]
    AP: [...]
  Mid-rotation expected: [level]    End-of-rotation expected: [level]
  Rating: ☐O  ☐CON  ☐DS  ☐IS  ☐AP
  Specific behavior evidence (cite + date): __________

═══ Domain 2: [...]
  [same structure]

[repeat for 4–8 domains]

>>> EOR BLUEPRINT EXPOSURE AUDIT

[Rotation-specific blueprint topics from PAEA blueprint]
| Topic area | Min cases | Cases seen | Cases co-managed | Cases independently managed | Notes |
| [topic 1] | 2 | __ | __ | __ | __ |
| ...

Gaps identified: __________
Make-up plan: __________

>>> PROCEDURAL LOGBOOK

| Procedure | Required count | Performed | Entrustment achieved | Preceptor sig |
| [proc 1] | [N] | __ | ☐O ☐CON ☐DS ☐IS ☐AP | __ |
| ...

Logbook complete: ☐ Yes ☐ No → Plan: __________

>>> NARRATIVE COMMENTARY

Strengths (specific behaviors observed):
  • [...]

Areas for growth (behaviors to develop next rotation):
  • [...]

Plan for improvement (REQUIRED if any rating is O at end, or DS in core domain):
  Concern: [...]
  Targeted behaviors next rotation: [...]
  Resources: [...]
  Notification: ☐ Verbal ☐ Written ☐ Learning contract

>>> REMEDIATION TRIGGERS

Triggered if any of:
  • Any "O" rating at end of rotation in core domain
  • Failed EOR exam (program threshold)
  • Logbook incomplete at end of rotation
  • Safety concern (regardless of other ratings)
  • Professionalism concern (regardless of other ratings)

>>> SIGNATURES

Student: __________ Date: ____
Primary preceptor: __________ Date: ____
Program-designated clinical coordinator (if remediation triggered): __________ Date: ____
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `rotation` | Drives competency anchors and EOR blueprint |
| `rotation_length_weeks` | Adjusts expected entrustment level at end |
| `eor_exam` | Toggles EOR audit section |
| `competency_framework` | PAEA vs NCCPA vs program-defined |
| `entrustment_scale` | 5-level Chen vs 4-level vs 3-level |
| `procedural_logbook_required` | Toggles logbook section |
| `setting` | OR-heavy rotations weight procedural skills; ED rotations weight rapid decision-making; primary care weights longitudinal management |
| `population_overlay` | Peds adds growth/development; OB adds maternal-fetal; geri adds polypharmacy and functional assessment |

## Verification Checklist

- [ ] Entrustment scale has 5 named levels with one-line definitions.
- [ ] Every competency domain has a rotation-specific anchor at *every* entrustment level (not just two).
- [ ] Anchors are *behavioral* (observable actions), not affective.
- [ ] Mid-rotation expected level differs from end-of-rotation level (or is explicitly stated as equal).
- [ ] EOR blueprint topics listed match the actual PAEA EOR blueprint for the rotation (no invented topics).
- [ ] Procedural logbook lists rotation-appropriate procedures with required minimums.
- [ ] Remediation triggers are criterion-referenced (named rating thresholds), not "preceptor discretion."
- [ ] Plan-for-improvement section is conditionally required, not always populated.
- [ ] No invented PA-program policies; ARC-PA standards or program-stated thresholds cited.
- [ ] No "consult with course director if unsure" boilerplate without naming the threshold.

## Worked Example (compact)

**Input:** rotation = `emergency medicine`, rotation_length_weeks = 5, eor_exam = `PAEA-EOR`, competency_framework = `PAEA-core-competencies`, entrustment_scale = `5-level-O-CON-DS-IS-AP`, procedural_logbook_required = true, setting = `ED`, failing_threshold_required = true.

**Output (excerpt):**

```
═══ Domain 1: Patient Care (Clinical & Technical)

Rotation-specific anchors:
  O: Shadows preceptor; observes triage and primary assessment without performing.
  CON: Performs primary survey alongside preceptor; preceptor leads secondary survey.
  DS: Performs initial workup independently; preceptor in the room for disposition decisions.
  IS: Manages 1–2 lower-acuity patients (ESI 4–5) independently; presents to preceptor with disposition plan.
  AP: Manages multiple patients of mixed acuity; presents focused plans; preceptor reviews and signs.

Mid-rotation expected: DS    End-of-rotation expected: IS
Rating: ☐O ☐CON ☐DS ☐IS ☐AP
Evidence: __________

═══ Domain 2: Medical Knowledge

Rotation-specific anchors (EOR-aligned):
  O: Verbalizes broad differential without prompted refinement.
  CON: Identifies top 3 diagnoses with preceptor prompting on rare/dangerous can't-miss.
  DS: Independently generates focused differential covering can't-miss diagnoses for chief complaint.
  IS: Risk-stratifies (HEART, PERC, Wells, NEXUS) appropriately; selects targeted workup.
  AP: Anticipates next steps; recognizes when standard workup is insufficient.

Mid-rotation expected: DS    End-of-rotation expected: IS

>>> EOR BLUEPRINT EXPOSURE AUDIT (PAEA EM EOR)

| Topic | Min | Seen | Co-mgd | Indep | Notes |
| Chest pain (incl ACS r/o) | 5 | __ | __ | __ | |
| Abdominal pain | 5 | __ | __ | __ | |
| Headache (incl SAH r/o) | 2 | __ | __ | __ | |
| Sepsis / bacteremia | 2 | __ | __ | __ | |
| Trauma (any) | 3 | __ | __ | __ | |
| Pediatric fever | 2 | __ | __ | __ | |
| Psychiatric presentation | 2 | __ | __ | __ | |
| Toxicology / overdose | 2 | __ | __ | __ | |
| Stroke (incl tPA window) | 1 | __ | __ | __ | |
| EKG interpretation logged | 20 | __ | __ | __ | |

>>> PROCEDURAL LOGBOOK

| Procedure | Required | Performed | Entrustment | Sig |
| Laceration repair (simple) | 5 | __ | __ | __ |
| I&D abscess | 2 | __ | __ | __ |
| Splinting (any) | 3 | __ | __ | __ |
| Procedural sedation (observation) | 1 | __ | __ | __ |
| Intubation observation | 2 | __ | __ | __ |
| LP attempt | 1 | __ | __ | __ |

>>> REMEDIATION TRIGGERS

Triggered if any of:
  • EOR exam < 70 (program threshold)
  • Any "O" rating at end in Patient Care or Medical Knowledge
  • Logbook < 80% of required minimums
  • Safety event (med error / disposition error caught by preceptor)
  • Documented professionalism concern
```
