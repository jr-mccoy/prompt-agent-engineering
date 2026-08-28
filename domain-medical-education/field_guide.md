# Field Guide: Educator-Facing Medical Education Prompts

**Domain:** Health Professions Education (HPE) — Educator Tools  
**Audience:** Clinical faculty, preceptors, clerkship directors, simulation educators, curriculum designers, program directors, GME coordinators  
**Updated:** 2026-05-15

---

## Why This Subdomain Exists

Clinical educators design teaching materials in a discipline with its own frameworks, evidence base, and quality standards — distinct from both clinical practice and K-16 pedagogy. These prompts help educators apply validated HPE methods (PBL, TBL, OSCE, simulation, workplace-based assessment, CBME) without having to architect the structure from scratch.

---

## Core HPE Frameworks Reference

### Miller's Pyramid (1990)
The four-level competency hierarchy underlying most clinical assessment:
| Level | Descriptor | Assessment Method |
|-------|-----------|-------------------|
| Knows | Declarative knowledge | MCQ, oral exam (factual) |
| Knows How | Applied knowledge | MCQ (clinical vignette), oral exam (problem) |
| Shows How | Performance in controlled setting | OSCE, simulation, DOPS |
| Does | Performance in real practice | Workplace-based assessment (mini-CEX, CBD, EPA) |

**Implication for prompt use:** Identify the target pyramid level before selecting an assessment or teaching prompt. A checklist measures "shows how," not "does."

---

### Dreyfus Model of Skill Acquisition → Learner Level Taxonomy
| Stage | Example | Supervision Needed |
|-------|---------|-------------------|
| Novice | M1-M2 | Rule-based, close supervision |
| Advanced Beginner | M3-M4 | Pattern recognition emerging |
| Competent | Intern, PGY1-2 | Can handle routine, needs back-up |
| Proficient | PGY3-4, Fellow | Sees the whole picture |
| Expert | Attending | Intuitive, pattern-based |

**Implication:** PBL cases for M1s must differ radically from progressive-disclosure cases for residents. Learner level is a required input for every prompt in this subdomain.

---

### Competency-Based Medical Education (CBME) & EPA Framework
**Entrustable Professional Activities (EPAs):** Discrete units of clinical work that can be trusted to a learner at a given supervision level.

| EPA Supervision Level | Description |
|-----------------------|-------------|
| 1 – Not yet allowed | Observing only |
| 2 – Direct supervision required | Supervisor in room |
| 3 – Indirect supervision | Available nearby/by phone |
| 4 – Unsupervised | Practice independently |
| 5 – Supervising others | Teaches and oversees |

**ACGME Milestones:** 0-5 developmental scale per sub-competency, assessed by Clinical Competency Committee (CCC) semi-annually.

**CanMEDS Roles:** Physician, Communicator, Collaborator, Leader, Health Advocate, Scholar, Professional.

---

### Kirkpatrick Model (for evaluating faculty development)
| Level | What You Measure |
|-------|-----------------|
| 1 – Reaction | Did faculty like it? |
| 2 – Learning | Did knowledge/attitudes change? |
| 3 – Behavior | Did practice change? |
| 4 – Results | Did patient/learner outcomes improve? |

**Implication:** Faculty development modules should target Level 3 (behavior change), not just Level 1 satisfaction.

---

## Technique Combinations by Task Type

### Case & Scenario Creation
**Core stack:** `ED-01` (scaffolded disclosure) + `RT-03` (clinical reasoning chain) + `CM-02` (learner level context) + `QA-01` (verification)  
**Add for simulation:** `RP-02` (confederate character scripting)  
**Add for branching cases:** `OC-02` (structured branching format)

### Assessment Design
**Core stack:** `ED-04` (assessment alignment) + `ST-02` (structured output) + `QA-01` (verification) + `OC-01` (format control)  
**Add for WBA tools:** `CM-02` (context specificity for encounter type)  
**Add for rubrics:** `NE-01` (level-appropriate language for descriptors)

### Feedback & Coaching
**Core stack:** `NE-01` (emotionally calibrated) + `CM-02` (encounter context) + `ST-02` (structured output) + `QA-01` (verification)  
**Add for remediation:** `RT-03` (root cause chain from evidence to intervention)

### Pedagogical Design
**Core stack:** `ED-02` (retrieval practice / spaced learning) + `ED-01` (scaffolded learning) + `ST-02` (structured output) + `CM-02` (learner level)  
**Add for faculty development:** `QA-01` (Kirkpatrick-level verification)

---

## Domain-Specific Quality Standards

All prompts in this subdomain must meet these standards beyond the baseline Tier 1 requirements:

### 1. Learner Level Specification (Non-Negotiable)
Every prompt must require the educator to specify learner level. Outputs must be calibrated to that level. "Medical student" is not specific enough — M1 vs M4 requires fundamentally different cases, questions, and assessment standards.

### 2. Competency Framework Alignment
Every assessment or educational activity output must name the competency domain it addresses:
- ACGME Core Competency (Patient Care, Medical Knowledge, Practice-Based Learning, Interpersonal/Communication Skills, Professionalism, Systems-Based Practice)
- CanMEDS Role
- Specific milestone subcompetency (if ACGME) or EPA (if CBME program)

### 3. Facilitator Guide Requirement
All case/scenario prompts (PBL, TBL, SP, simulation, progressive disclosure) must produce a facilitator guide alongside the learner-facing materials. Educator scaffolding is not optional.

### 4. Standard-Setting Guidance for Assessment Tools
Any assessment instrument (OSCE checklist, MCQ, oral exam, rubric) must include guidance on how to set a passing standard. A measurement instrument without a pass score is incomplete.

### 5. Validated Framework Grounding
Feedback, debriefing, and remediation prompts must explicitly reference a validated framework (R2C2, PEARLS, GAS, Pendleton, SMART goals) rather than ad-hoc structure.

---

## False-Positive Prevention: Domain-Wide Patterns

These errors apply across the entire medical education subdomain:

| ❌ Common Error | ✅ Correct Approach |
|---|---|
| Writing educational content that teaches facts rather than teaching how to learn | Focus on process: hypothesis generation, clinical reasoning steps, facilitation moves — not fact delivery |
| Generating fully finished products (complete case, complete rubric) without editing scaffolds | Output should be a structured template the educator can adapt — include annotation notes, editability cues |
| Treating "medical student" as a single learner level | Specify M1/M2/M3/M4 and calibrate cognitive demand accordingly |
| Designing assessment without addressing standard-setting | Include passing standard guidance or Angoff/Borderline method reference for every instrument |
| Creating formative tools with summative language (grades, pass/fail judgments) | Distinguish formative (coaching, forward-looking) from summative (judgment, decision-making) contexts |
| Conflating Miller's "Shows How" with "Does" | OSCE shows how in controlled conditions; WBA documents what learners actually do in clinical practice |
| Omitting psychological safety framing for simulation | Pre-briefing (fiction contract, confidentiality, learning focus) must precede every simulation scenario |
| Writing debriefing guides as post-scenario lectures | Debriefing is learner-generated; facilitators ask questions, not give answers |

---

## Common Failure Modes

Educators using these prompts should watch for:

1. **Level mismatch:** Case or question calibrated to wrong learner level. A PBL case for M3 students written at M1 complexity insults learners; at fellow complexity, it frustrates them.

2. **Missing facilitator guide:** Producing only learner-facing materials. Every case, scenario, and exercise requires a parallel educator guide with facilitation moves and common tangents.

3. **Omitting standard-setting:** Assessment instruments without passing criteria are unusable in high-stakes contexts. Always specify how the pass score is set.

4. **Conflating formative and summative:** Using summative language (grades, pass/fail) in a formative tool, or omitting judgment in a summative tool.

5. **One-size assessments:** Using a single OSCE checklist for M3 students AND residents. Calibration to level is required.

6. **Passive faculty development:** Designing a module that transmits information rather than practices the educator behavior. Kirkpatrick Level 3 (behavior change) requires active skill rehearsal.

---

---

## Routing Within This Subdomain

| Educator Need | Prompt |
|--------------|--------|
| Write a PBL case with trigger packets | `case-scenario-design/meded_pbl_case_writer.md` |
| Design TBL iRAT/tRAT + application exercise | `case-scenario-design/meded_tbl_application_exercise_designer.md` |
| Build a branching virtual patient | `case-scenario-design/meded_virtual_patient_case_builder.md` |
| Design a sequential progressive-disclosure case | `case-scenario-design/meded_progressive_disclosure_case_designer.md` |
| Write a standardized patient scenario | `case-scenario-design/meded_standardized_patient_scenario_writer.md` |
| Design an OSCE station | `case-scenario-design/meded_osce_station_designer.md` |
| Design a simulation scenario | `case-scenario-design/meded_simulation_scenario_designer.md` |
| Write NBME-style MCQs with distractor rationale | `assessment-tools/meded_nbme_style_mcq_writer.md` |
| Design an oral exam case | `assessment-tools/meded_oral_exam_case_designer.md` |
| Build a rubric with entrustment anchors | `assessment-tools/meded_assessment_rubric_builder.md` |
| Create mini-CEX, DOPS, CBD, or EPA forms | `assessment-tools/meded_workplace_based_assessment_tools.md` |
| Write milestone narratives for CCC | `assessment-tools/meded_milestone_narrative_writer.md` |
| Design a clinical skills checklist | `assessment-tools/meded_clinical_skills_checklist_designer.md` |
| Write specific feedback for a learner | `feedback-remediation/meded_learner_feedback_composer.md` |
| Design a remediation plan | `feedback-remediation/meded_remediation_plan_designer.md` |
| Design a debriefing guide | `feedback-remediation/meded_debriefing_guide_designer.md` |
| Write preceptor teaching scripts (OMP/SNAPPS) | `teaching-methods/meded_preceptor_teaching_script_writer.md` |
| Design a small-group facilitation guide | `teaching-methods/meded_small_group_facilitation_guide.md` |
| Design a journal club session | `teaching-methods/meded_journal_club_teaching_guide.md` |
| Redesign a lecture for active learning | `teaching-methods/meded_lecture_redesign_planner.md` |
| Design a flipped classroom module | `teaching-methods/meded_flipped_classroom_module_designer.md` |
| Design a faculty development module | `teaching-methods/meded_faculty_development_module_designer.md` |
