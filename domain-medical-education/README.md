# Domain: Medical Education

**Purpose:** Health-professions education (HPE) — designing and running teaching
and assessment for clinicians in training, and the study tools those trainees use
on themselves.

**213 prompts across 14 tracks**, covering medicine, nursing, PA, pharmacy, EMS,
dental, and allied health.

> **This domain now holds all medical-education prompts in the repository.** It
> previously coexisted with `domain-healthcare-clinical/prompts/medical-education/`
> (67 prompts) — two homes for one discipline, mirroring each other structurally
> with no stated boundary between them. Those 67 have been merged in.

---

## The boundary that matters

This domain teaches and assesses clinicians. It does **not** advise on the care
of a real patient.

| You are… | Go to |
|---|---|
| Teaching, assessing, or remediating a learner | **this domain**, `educator-*` tracks |
| A student or resident studying, drilling, or rehearsing | **this domain**, `learner-*` tracks |
| Reasoning about an actual patient in front of you | [`domain-healthcare-clinical/`](../domain-healthcare-clinical/) |
| Designing a program, curriculum map, or accreditation self-study at institution scale | [`domain-education-teaching/program/`](../domain-education-teaching/program/) |
| Teaching outside the health professions | [`domain-education-teaching/`](../domain-education-teaching/) |
| Teaching research methods | [`domain-science/teaching-research-methods/`](../domain-science/teaching-research-methods/) |

**Every `learner-*` prompt is a study tool, not clinical decision support.** They
route real-patient questions to clinical resources and a supervisor.

---

## Educator tracks (79)

You are building something you hand to learners, or judging their performance.

| Track | Prompts | Holds |
|---|---|---|
| [`educator-case-writing/`](educator-case-writing/) | 16 | PBL, TBL, standardized-patient, virtual-patient, progressive-disclosure, board-style vignette, ethics, M&M, grand-rounds cases |
| [`educator-assessment-items/`](educator-assessment-items/) | 12 | NBME-style MCQs, distractors, EMI, oral-exam cases, blueprints, item analysis |
| [`educator-rubrics-wba/`](educator-rubrics-wba/) | 12 | Rubrics, clinical-skills checklists, workplace-based assessment, entrustment scales, EPA observation forms, milestone narratives |
| [`educator-simulation-design/`](educator-simulation-design/) | 13 | Simulation scenarios, OSCE stations, confederate scripts, debriefing (PEARLS, advocacy-inquiry, plus-delta) |
| [`educator-curriculum-design/`](educator-curriculum-design/) | 18 | CBME rollout, EPA implementation, ACGME competency frameworks, residency curriculum mapping, course maps, learning objectives, flipped classroom, lecture redesign, preceptor scripts, journal club, small-group facilitation, faculty development |
| [`educator-remediation/`](educator-remediation/) | 8 | Learner feedback, remediation plans by gap type, documentation and due process |

## Learner tracks (134)

You are the trainee, studying alone.

| Track | Prompts | Holds |
|---|---|---|
| [`learner-clinical-reasoning/`](learner-clinical-reasoning/) | 18 | Illness scripts, differentials, problem representation, hypothesis-driven workup, reasoning schemas, case walkthroughs, Bayesian drills |
| [`learner-foundational-sciences/`](learner-foundational-sciences/) | 22 | Anatomy, physiology, pathophysiology, pharmacology, microbiology, immunology, biochemistry |
| [`learner-osce-skills/`](learner-osce-skills/) | 14 | OSCE rehearsal, history taking, physical-exam checklists, breaking bad news, cross-cultural and difficult encounters |
| [`learner-clinical-rotation/`](learner-clinical-rotation/) | 16 | Pre-rounding, pre-clinic prep, handoffs, oral presentations, H&P and SOAP note practice |
| [`learner-boards/`](learner-boards/) | 16 | Board-style question review, distractor analysis, qbank debriefs, high-yield compression, dedicated-period schedules |
| [`learner-procedures/`](learner-procedures/) | 14 | Procedure pre-briefs, ACLS/PALS/NRP/ATLS drills, critical-event recognition, simulation pre-briefing |
| [`learner-study-systems/`](learner-study-systems/) | 13 | Spaced repetition, study plans, weekly review, concept maps, calibration self-quizzes |
| [`profession-specific/`](profession-specific/) | 21 | Nursing care plans, pharmacy therapeutics, EMS protocols, dental treatment planning, PA, allied health |

---

## Where to start

- **"I need a case for Thursday"** → [`educator-case-writing/`](educator-case-writing/)
- **"Write me exam items with real distractors"** → [`educator-assessment-items/`](educator-assessment-items/)
- **"How do I assess this in the workplace?"** → [`educator-rubrics-wba/`](educator-rubrics-wba/)
- **"A resident is struggling"** → [`educator-remediation/`](educator-remediation/)
- **"Roll out CBME / map our residency curriculum"** → [`educator-curriculum-design/`](educator-curriculum-design/)
- **"Build me an illness script"** → [`learner-clinical-reasoning/`](learner-clinical-reasoning/)
- **"Run me through an OSCE station"** → [`learner-osce-skills/`](learner-osce-skills/)
- **"Boards are in six weeks"** → [`learner-boards/`](learner-boards/)
- **"Coach me through a question I got wrong"** → [`learner-boards/boards_style_question_review.md`](learner-boards/boards_style_question_review.md)

Craft reference and competency frameworks: [`field_guide.md`](field_guide.md).
