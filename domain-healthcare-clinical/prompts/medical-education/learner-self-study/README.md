# Learner-Facing Medical / Health-Professions Education Prompts

**Subdomain of:** `domain-healthcare-clinical/prompts/medical-education/`
**Audience:** Health-professions **learners themselves** (medical, nursing, PA, pharmacy, EMS, allied health, dental)
**Intended use:** Study, deliberate practice, rehearsal, self-assessment — **NOT real-time clinical decision support**
**Prompts:** 37 across 8 subdirectories
**Added:** 2026-05-15

---

## Boundary: Learner Tools vs. Real Patient Care

Every prompt in this directory:

- Carries frontmatter `audience: learner` and `intended_use: education-and-practice`
- Includes an explicit Must-Not clause: *"Do not produce content intended as real-time clinical decision support for an actual patient. This prompt is for study, rehearsal, and self-assessment only. If the user describes a real patient, redirect them to clinical resources / supervisor."*
- Uses **drug class** and **qualitative dose principle** language rather than patient-specific numerics — learners should defer to verified pharmacotherapy references for any actual dose
- Closes with **retrieval** (the learner reconstructs from memory), not re-reading

If you find yourself describing a real, live patient in front of you, **stop using this directory** and:
- Contact your supervisor, attending, preceptor, or pharmacist on duty
- Use your institutional clinical decision-support resources
- Use verified references (UpToDate, Lexicomp, current society guidelines, your institution's antibiogram and protocols)

---

## Who This Is For

| Persona | Primary Use |
|---|---|
| Medical / PA / NP student | Illness-script building, DDx drills, case walkthroughs, OSCE prep, oral presentation practice, SOAP / H&P, board-style review |
| Resident (PGY-1+) | Pre-rounding scaffold, oral presentation, handoff practice, code algorithm rehearsal, procedure prep, sub-specialty board prep |
| Nursing student / new RN | History-taking, care plans (NANDA/NIC/NOC), NCLEX-style reasoning, handoff (SBAR), simulation pre-brief |
| Pharmacy student / resident | Pharmacotherapy SOAP, drug-class mechanism explainer, microbiology drill, NAPLEX / BCPS prep, MTM case practice |
| EMS student (EMT / paramedic) | Protocol decision drill, code algorithm rehearsal, critical-event recognition, NREMT prep |
| Allied-health student (PT/OT/SLP/RT/RD/MSW/AuD) | Scope-and-reasoning drill, SOAP, goal writing (SMART/COAST), outcome measures, board prep |
| Dental student / hygiene student | Treatment-planning practice, oral history, perio chart interpretation, INBDE / NBDE prep |

---

## Directory Map

```
learner-self-study/
├── foundational-sciences/          # 6: anatomy, physio, pathophys, pharm, micro, immuno
├── clinical-reasoning/             # 6: illness scripts, DDx, schemas, problem rep, hypothesis workup, case walkthrough
├── clinical-skills/                # 6: history-taking, OSCE, exam checklist, oral pres, SOAP, H&P
├── exam-prep/                      # 4: board question review, distractor drill, qbank debrief, topic compressor
├── procedures-emergencies/         # 4: procedure prep, code algorithm, sim pre-brief, critical-event recognition
├── clinical-prep/                  # 3: pre-rounding, pre-clinic, handoff practice
├── study-planning/                 # 3: SRS deck, study plan, weekly review
└── discipline-specific/            # 5: nursing care plan, pharmacy SOAP, EMS protocol, dental tx plan, allied-health
```

---

## Trigger Phrases → Prompt File

### Foundational Sciences

| When a learner says... | Use this prompt |
|---|---|
| "Drill me on anatomy of [region]" / "spaced anatomy review" | [`foundational-sciences/learner_anatomy_drill_generator.md`](foundational-sciences/learner_anatomy_drill_generator.md) |
| "I don't get [Starling forces / V/Q / RAAS]" / "explain physiology concept" | [`foundational-sciences/learner_physiology_concept_clarifier.md`](foundational-sciences/learner_physiology_concept_clarifier.md) |
| "Build me the pathophys chain for [disease]" | [`foundational-sciences/learner_pathophysiology_chain_builder.md`](foundational-sciences/learner_pathophysiology_chain_builder.md) |
| "How do [ACE inhibitors / beta-blockers] work?" / "drug class mechanism" | [`foundational-sciences/learner_pharmacology_mechanism_explainer.md`](foundational-sciences/learner_pharmacology_mechanism_explainer.md) |
| "Quiz me on [Staph aureus / Pseudomonas]" / "bug drill" | [`foundational-sciences/learner_microbiology_bug_drill.md`](foundational-sciences/learner_microbiology_bug_drill.md) |
| "Explain hypersensitivity types / MHC / complement" | [`foundational-sciences/learner_immunology_concept_clarifier.md`](foundational-sciences/learner_immunology_concept_clarifier.md) |

### Clinical Reasoning

| When a learner says... | Use this prompt |
|---|---|
| "Build me an illness script for [disease]" / "atypical variants" | [`clinical-reasoning/learner_illness_script_builder.md`](clinical-reasoning/learner_illness_script_builder.md) |
| "Quiz me on differentials for [chief complaint]" | [`clinical-reasoning/learner_differential_diagnosis_drill.md`](clinical-reasoning/learner_differential_diagnosis_drill.md) |
| "Help me pick a reasoning schema for [chief complaint]" | [`clinical-reasoning/learner_clinical_reasoning_schema_practice.md`](clinical-reasoning/learner_clinical_reasoning_schema_practice.md) |
| "Sharpen my one-liner / problem representation" | [`clinical-reasoning/learner_problem_representation_rehearsal.md`](clinical-reasoning/learner_problem_representation_rehearsal.md) |
| "What's the next-best test for this DDx?" | [`clinical-reasoning/learner_hypothesis_driven_workup_drill.md`](clinical-reasoning/learner_hypothesis_driven_workup_drill.md) |
| "Walk me through an interactive case" | [`clinical-reasoning/learner_clinical_case_walkthrough.md`](clinical-reasoning/learner_clinical_case_walkthrough.md) |

### Clinical Skills

| When a learner says... | Use this prompt |
|---|---|
| "Be my standardized patient — let me practice history" | [`clinical-skills/learner_history_taking_rehearsal.md`](clinical-skills/learner_history_taking_rehearsal.md) |
| "Run me through an OSCE station" | [`clinical-skills/learner_osce_self_rehearsal.md`](clinical-skills/learner_osce_self_rehearsal.md) |
| "Give me a [knee / cardiac / abdominal] exam checklist" | [`clinical-skills/learner_physical_exam_checklist_generator.md`](clinical-skills/learner_physical_exam_checklist_generator.md) |
| "Coach my oral presentation for rounds" | [`clinical-skills/learner_oral_presentation_practice.md`](clinical-skills/learner_oral_presentation_practice.md) |
| "Critique my SOAP note" | [`clinical-skills/learner_soap_note_writing_practice.md`](clinical-skills/learner_soap_note_writing_practice.md) |
| "Critique my admission H&P" | [`clinical-skills/learner_h_and_p_writing_practice.md`](clinical-skills/learner_h_and_p_writing_practice.md) |

### Exam Prep

| When a learner says... | Use this prompt |
|---|---|
| "Coach me through this question I got wrong" | [`exam-prep/learner_board_style_question_review.md`](exam-prep/learner_board_style_question_review.md) |
| "Why do I keep falling for distractors?" | [`exam-prep/learner_distractor_analysis_drill.md`](exam-prep/learner_distractor_analysis_drill.md) |
| "Debrief my qbank session" / "remediation list" | [`exam-prep/learner_qbank_session_debriefer.md`](exam-prep/learner_qbank_session_debriefer.md) |
| "Compress this topic into a high-yield sheet" | [`exam-prep/learner_high_yield_topic_compressor.md`](exam-prep/learner_high_yield_topic_compressor.md) |

### Procedures & Emergencies

| When a learner says... | Use this prompt |
|---|---|
| "Pre-brief me before [paracentesis / LP / intubation]" | [`procedures-emergencies/learner_procedure_prep_briefing.md`](procedures-emergencies/learner_procedure_prep_briefing.md) |
| "Run an ACLS / PALS / NRP / ATLS rehearsal" | [`procedures-emergencies/learner_code_algorithm_rehearsal.md`](procedures-emergencies/learner_code_algorithm_rehearsal.md) |
| "Prep me mentally for my sim session" | [`procedures-emergencies/learner_simulation_pre_briefing.md`](procedures-emergencies/learner_simulation_pre_briefing.md) |
| "Drill me on recognizing [anaphylaxis / sepsis / tension pneumo]" | [`procedures-emergencies/learner_critical_event_recognition_drill.md`](procedures-emergencies/learner_critical_event_recognition_drill.md) |

### Clinical Prep

| When a learner says... | Use this prompt |
|---|---|
| "Help me pre-round on my inpatients" | [`clinical-prep/learner_pre_rounding_prep.md`](clinical-prep/learner_pre_rounding_prep.md) |
| "Help me pre-chart for clinic tomorrow" | [`clinical-prep/learner_pre_clinic_patient_prep.md`](clinical-prep/learner_pre_clinic_patient_prep.md) |
| "Practice handoff / sign-out / SBAR" | [`clinical-prep/learner_handoff_practice.md`](clinical-prep/learner_handoff_practice.md) |

### Study Planning

| When a learner says... | Use this prompt |
|---|---|
| "Turn these notes into Anki cards" | [`study-planning/learner_spaced_repetition_deck_generator.md`](study-planning/learner_spaced_repetition_deck_generator.md) |
| "Build me a study plan for [board exam]" | [`study-planning/learner_study_plan_designer.md`](study-planning/learner_study_plan_designer.md) |
| "End-of-week study review" | [`study-planning/learner_weekly_study_review.md`](study-planning/learner_weekly_study_review.md) |

### Discipline-Specific (workflow truly differs)

| When a learner says... | Use this prompt |
|---|---|
| "Write a NANDA care plan for this patient" | [`discipline-specific/learner_nursing_care_plan_practice.md`](discipline-specific/learner_nursing_care_plan_practice.md) |
| "Pharmacy SOAP / MTM recommendation" | [`discipline-specific/learner_pharmacy_therapeutics_soap_practice.md`](discipline-specific/learner_pharmacy_therapeutics_soap_practice.md) |
| "EMS protocol drill / NREMT scenario" | [`discipline-specific/learner_ems_protocol_decision_drill.md`](discipline-specific/learner_ems_protocol_decision_drill.md) |
| "Dental treatment plan practice" | [`discipline-specific/learner_dental_treatment_planning_practice.md`](discipline-specific/learner_dental_treatment_planning_practice.md) |
| "PT/OT/SLP/RT/RD/SW scope + plan" | [`discipline-specific/learner_allied_health_scope_and_reasoning_drill.md`](discipline-specific/learner_allied_health_scope_and_reasoning_drill.md) |

---

## Discipline Coverage Strategy

Most prompts take `discipline` and `learner_level` as inputs and adapt their output. For example, `learner_pharmacology_mechanism_explainer.md` with `discipline: nursing` emphasizes bedside monitoring parameters and escalation triggers; with `discipline: pharmacy` it emphasizes drug-by-drug nuance and interaction screen; with `discipline: ems` it emphasizes time-critical recognition.

**Five prompts in `discipline-specific/`** exist where the workflow itself differs — nursing care plans use NANDA/NIC/NOC (a different reasoning frame than physician A&P), pharmacotherapy SOAPs center the pharmacist's recommendation, EMS decisions hinge on protocol-vs-OLMC distinctions, dental treatment plans are phased differently, and allied-health practice has role-specific assessment frames and goal-writing conventions (SMART vs COAST vs NCP).

**Board exams** (USMLE Step 1/2/3, NCLEX, NAPLEX, PANCE, NREMT, NBDE, INBDE, BCPS, NPTE, NBCOT, Praxis SLP, NBRC, CDR, AuD boards, etc.) are handled by the `exam-prep/` and `study-planning/` prompts, which take `target_exam` as input rather than duplicating per-exam files.

---

## How the Prompts Are Built

Every learner-facing prompt:

1. **Calibrates to learner level** (M1 vs M3 vs PGY-1 vs P3 vs NCLEX-prep, etc.)
2. **Forces the learner to commit first** in deliberate-practice prompts (DDx, problem representation, board questions, workup) — the coach reveals their version only after the learner has tried
3. **Coaches with qualitative feedback**, not numeric scores
4. **Uses class-level pharmacology** and qualitative test characteristics — never invents specific patient-numeric drug doses, sensitivities, or specificities
5. **Anchors to discipline** when the role changes what matters (a nurse's monitoring focus vs a pharmacist's therapeutic recommendation vs a paramedic's protocol decision)
6. **Ends with retrieval**, not re-reading — recall under self-quiz consolidates the learning the rest of the session built up
7. **Redirects real-patient questions** to clinical resources and supervisors

These choices reflect the pedagogy of **deliberate practice + retrieval + interleaving + spaced retrieval** that the evidence base for medical education supports.

---

## Related (Educator-Facing) Counterparts

If you are an *educator* designing material for learners (rather than a learner using these tools yourself), see the educator-facing prompts in sibling directories:

| Learner tool | Educator counterpart |
|---|---|
| `learner_osce_self_rehearsal.md` | `case-scenario-design/meded_osce_station_designer.md` |
| `learner_clinical_case_walkthrough.md` | `case-scenario-design/meded_progressive_disclosure_case_designer.md` |
| `learner_board_style_question_review.md` | `assessment-tools/meded_nbme_style_mcq_writer.md` |
| `learner_simulation_pre_briefing.md` | `case-scenario-design/meded_simulation_scenario_designer.md` + `feedback-remediation/meded_debriefing_guide_designer.md` |
| `learner_physical_exam_checklist_generator.md` | `assessment-tools/meded_clinical_skills_checklist_designer.md` |

---

**Last updated:** 2026-05-15
