# Education & Teaching: Comprehensive Guide

> Part of the [Non-Coding Quick Start](../NON_CODING_QUICK_START.md) system.
> This domain covers lesson planning, curriculum design, assessment creation, educational materials, and teaching methodology.

---

## Program-Level Curriculum Design (New, 2026-05-15)

If you are a **curriculum director, dean, program coordinator, accreditation liaison, instructional coach lead, CTE administrator, residency program director, or institutional assessment officer** — start with the subdirectories below. They contain **45 new prompts** for program-level work (vs. the classroom/course-level prompts that fill the rest of this domain):

- **[`curriculum-design/`](curriculum-design/)** (18 prompts) — Curriculum maps, scope-and-sequence (K-12 / HE / workforce), backward program design, standards alignment audit + crosswalks, competency frameworks, vertical/horizontal alignment, progression maps, milestones, remediation pathways, advanced unit design, learning objectives writer, Bloom's calibrator
- **[`program-outcomes-assessment/`](program-outcomes-assessment/)** (8 prompts) — PSLO/ISLO/CSLO architecture, outcomes-to-assessment mapper, assessment blueprints, program gap analysis, signature assignments, capstones, rubric alignment, CBME-style evidence design
- **[`accreditation-program-review/`](accreditation-program-review/)** (5 prompts) — Parameterized self-study builders for regional HE (HLC/MSCHE/SACSCOC/WSCUC/NWCCU), programmatic (ABET/AACSB/CAEP/CCNE/ACPE/etc.), and med-ed (LCME/ACGME/COCA/CODA); program review cycle designer; evidence compiler
- **[`faculty-development/`](faculty-development/)** (5 prompts) — Multi-semester FD plan, PLC design, instructional coaching program, assessment-literacy curriculum, faculty onboarding
- **[`program-evaluation-analytics/`](program-evaluation-analytics/)** (5 prompts) — Program evaluation framework (Kirkpatrick/CIPP/logic model), logic model designer, learning analytics interpreter, early warning system, PDSA continuous-improvement cycle

For **medical education program-level work** (CBME, EPAs, ACGME), see also [`../domain-healthcare-clinical/prompts/medical-education/curriculum-design/`](../domain-healthcare-clinical/prompts/medical-education/curriculum-design/) (4 prompts).

---

## Learner Guides (2026-05-13)

If you're a **college student, adult returning to school, or career changer**, start here — not the rest of this README:

- **[`guides/`](guides/)** — workflow guides for learners, with cross-domain prompt kits. Three audience folders:
  - [`guides/college-students/`](guides/college-students/) — essay arc, research paper arc, finals prep, STEM problem solving
  - [`guides/adult-returning/`](guides/adult-returning/) — cold start, working-learner time architecture, writing rust, imposter calibration, prior-learning articulation
  - [`guides/career-changers/`](guides/career-changers/) — credential pathway decision, self-study plan, portfolio while learning, proof-of-work for the pivot
  - [`guides/shared/`](guides/shared/) — andragogy principles, Socratic vs. direct mode, academic integrity, cross-domain prompt index

- **[`adult-learner/`](adult-learner/)** — 9 net-new prompts authored for adult learners specifically (cold-start, time architecture, writing-rust, imposter calibration, prior-learning articulation, skill-pivot plan, credential decision, portfolio-while-learning, andragogy-aware study workflow)

- **[`../PROMPT_INDEX_LEARNER_AUDIENCE.json`](../PROMPT_INDEX_LEARNER_AUDIENCE.json)** — programmatic audience tags across ~115 cross-domain learner-relevant prompts. Companion to [`guides/shared/prompt_index_for_learners.md`](guides/shared/prompt_index_for_learners.md).

The rest of this README covers the broader education domain (K-12, instructor-side, curriculum, assessment, etc.). Learners can scroll past those sections.

---

## When This Domain Applies

### Trigger Phrases

Route to this domain when the request mentions:

| Category | Trigger Phrases |
|----------|----------------|
| **Lesson Planning** | "lesson plan", "teaching", "classroom activity", "instructional design" |
| **Assessment** | "quiz", "test", "rubric", "assessment", "grading", "evaluation" |
| **Materials** | "worksheet", "handout", "study guide", "educational materials" |
| **Curriculum** | "curriculum", "unit plan", "scope and sequence", "learning objectives" |
| **Students** | "grade level", "students", "learners", "classroom", "differentiation" |
| **Standards** | "Common Core", "NGSS", "state standards", "learning outcomes" |

### User Personas

| Persona | Typical Needs |
|---------|--------------|
| **K-12 Teachers** | Lesson plans, worksheets, assessments, differentiation strategies |
| **College Instructors** | Syllabi, assignments, rubrics, lecture materials |
| **Curriculum Developers** | Unit plans, scope and sequence, standards alignment |
| **Tutors** | Targeted practice, concept explanations, progress assessment |
| **Homeschool Parents** | Comprehensive lesson plans, age-appropriate activities |
| **Corporate Trainers** | Training modules, skill assessments, learning activities |

### Out of Scope

- **Academic research methodology** → domain-research-academic
- **Student counseling/mental health** → Professional support
- **Administrative tasks** → General productivity
- **Coding education specifically** → domain-learning-coding/

---

## Domain-Specific Considerations

### What Makes Education Unique

Educational prompts operate in environments where:

1. **Learner Diversity** - Same content, different readiness levels, learning styles, and needs
2. **Developmental Appropriateness** - Age matters for vocabulary, complexity, and examples
3. **Standards Alignment** - External requirements constrain what must be taught
4. **Time Constraints** - Fixed class periods, semester lengths, curriculum pacing
5. **Assessment Balance** - Formative vs. summative, authentic vs. standardized
6. **Engagement Matters** - Learning requires attention and motivation
7. **Scaffolding is Key** - Building from known to unknown systematically

### The Educational Content Difference

| Dimension | Generic Content | Educational Content |
|-----------|-----------------|---------------------|
| **Audience** | Assumed capable adult | Specific developmental level |
| **Structure** | Logical flow | Pedagogical sequence (engage, explain, elaborate, evaluate) |
| **Assessment** | Optional | Integrated and aligned with objectives |
| **Differentiation** | One version | Multiple entry points and extensions |
| **Standards** | N/A | Explicitly aligned and referenced |
| **Timing** | Flexible | Designed for specific time constraints |

### Critical Success Factors

1. **Grade-Level Appropriateness** - Vocabulary, complexity, examples match learners
2. **Clear Learning Objectives** - What students will know/do by end
3. **Assessment Alignment** - Activities and assessments measure stated objectives
4. **Engagement Design** - Active learning, not passive receipt
5. **Differentiation** - Accommodations for diverse learners
6. **Time Realism** - Activities fit available class time
7. **Standards Connection** - Explicit alignment when required

### Common Failure Modes

| Failure | Example | Prevention |
|---------|---------|------------|
| **Grade mismatch** | College vocabulary for 5th graders | Specify grade level, reading level targets |
| **Objective/assessment misalignment** | Teaching concepts, testing facts | Design assessment first, then instruction |
| **Time unrealism** | 45-minute activity for 30-minute period | Include time estimates, have backup plans |
| **No differentiation** | Same worksheet for all learners | Include scaffolds and extensions |
| **Passive learning** | Lecture-only design | Include active engagement strategies |
| **Missing scaffolding** | Jumping to complex without building blocks | Sequence from simple to complex |

---

## Recommended Techniques

### Core Techniques (Always Use)

| Technique | Application in Education | Example |
|-----------|-------------------------|---------|
| **CM-01 Context Framing** | Grade level, prior knowledge, time available | "7th grade, 45-minute period, have covered fractions" |
| **ST-02 Sequential Steps** | Lesson phases (engage, explore, explain, evaluate) | 5E model, gradual release |
| **OC-01 Output Templates** | Structured lesson plan format | Objectives, materials, procedure, assessment |
| **CM-02 Audience Adaptation** | Differentiation for varied learners | Scaffolds, extensions, accommodations |
| **QA-01 Verification** | Assessment alignment check | "Does this activity measure the objective?" |

### Situational Techniques

| Situation | Add Technique | Why |
|-----------|--------------|-----|
| Standards-based | DS-01 Framework | Apply Bloom's Taxonomy, Webb's DOK |
| Diverse learners | RT-02 Multi-Dimensional | Multiple modalities, learning styles |
| Complex concepts | RT-03 Tree of Thoughts | Misconception mapping, prerequisite chains |
| Assessment design | QA-02 Adversarial | Anticipate where students will struggle |
| Engagement | RT-04 Emotional Intelligence | Connect content to student interests/lives |

---

## Quality Indicators for Education

### What "Good" Looks Like

**A high-quality educational prompt output:**

1. **Clear, Measurable Objectives**
   - Written as "Students will be able to..." (SWBAT)
   - Observable and assessable
   - Aligned to standards when applicable

2. **Grade-Appropriate Content**
   - Vocabulary matches developmental level
   - Examples relevant to learners' experience
   - Complexity appropriate for prior knowledge

3. **Pedagogically Sound Sequence**
   - Activates prior knowledge
   - Builds from simple to complex
   - Includes practice with feedback
   - Provides opportunity for synthesis/application

4. **Built-in Assessment**
   - Checks for understanding throughout
   - Summative assessment aligned to objectives
   - Clear success criteria

5. **Differentiation Ready**
   - Scaffolds for struggling learners
   - Extensions for advanced learners
   - Multiple modalities when possible

### Learning Objective Quality Criteria

```markdown
## Strong Learning Objectives (Bloom's Aligned)

**Weak (Vague):**
- "Students will understand photosynthesis"
- "Students will learn about the Civil War"

**Strong (Observable, Measurable):**
- "Students will be able to diagram the process of photosynthesis, labeling inputs, outputs, and energy transformation"
- "Students will be able to analyze three causes of the Civil War and argue which was most significant using textual evidence"

**Bloom's Taxonomy Verbs by Level:**
- Remember: list, define, identify, recall
- Understand: explain, summarize, classify, compare
- Apply: use, implement, solve, demonstrate
- Analyze: differentiate, examine, compare, contrast
- Evaluate: judge, justify, critique, defend
- Create: design, construct, develop, formulate
```

### False-Positive Prevention for Education

**DON'T:**

- Assume grade level equals ability level (wide variation within grades)
- Ignore time constraints (activities must fit class period)
- Skip scaffolding (build bridges, don't assume leaps)
- Create assessments that don't match instruction
- Use vocabulary without considering reading level
- Design for "average" student only (differentiate)
- Forget engagement (content must connect to learners)
- Assume access to materials/technology

**DO:**

- Ask about specific learner context (IEPs, ELLs, mixed abilities)
- Include time estimates for all activities
- Provide scaffolds AND extensions
- Align assessments directly to stated objectives
- Check vocabulary against grade-level standards
- Include active learning strategies
- Connect to student interests and real-world applications
- Note required materials and alternatives

---

## Wave 1 Expansion (2026-05-09) — 30 New Prompts in 8 Subdirectories

A 30-prompt expansion organized into role-based subdirectories. Subject-pedagogy, assessment engineering, grading workflows, inclusive instruction, classroom operations, and learner-facing prompts (writing, math/science, study skills). Learner-facing prompts use a strict Socratic stance — they do not produce answers students could submit.

### `subject-pedagogy/` (6) — Subject-Specific Pedagogy

| Prompt | Description |
|--------|-------------|
| [`teachsubj_math_number_talks_designer.md`](subject-pedagogy/teachsubj_math_number_talks_designer.md) | 5–15 minute math number talk with anticipated strategies and teacher moves |
| [`teachsubj_math_three_act_task_builder.md`](subject-pedagogy/teachsubj_math_three_act_task_builder.md) | Complete 3-act math task — hook, info release, reveal, sequel |
| [`teachsubj_ela_close_reading_minilesson.md`](subject-pedagogy/teachsubj_ela_close_reading_minilesson.md) | 20–30 minute close reading with three reads and text-dependent questions |
| [`teachsubj_ela_writers_workshop_minilesson.md`](subject-pedagogy/teachsubj_ela_writers_workshop_minilesson.md) | 10–15 minute writer's workshop minilesson — one craft move |
| [`teachsubj_science_ngss_phenomenon_selector.md`](subject-pedagogy/teachsubj_science_ngss_phenomenon_selector.md) | NGSS anchoring phenomenon vetting and storyline arc |
| [`teachsubj_socialstudies_dbq_writer.md`](subject-pedagogy/teachsubj_socialstudies_dbq_writer.md) | Document-based question with sourced documents and rubric |

### `assessment/` (4) — Assessment Engineering

| Prompt | Description |
|--------|-------------|
| [`assessment_mc_item_writer_with_distractors.md`](assessment/assessment_mc_item_writer_with_distractors.md) | MC items with distractor analysis tied to named misconceptions |
| [`assessment_test_blueprint_table_of_specs.md`](assessment/assessment_test_blueprint_table_of_specs.md) | Test blueprint mapping items to objectives, DOK, and weights |
| [`assessment_performance_task_designer.md`](assessment/assessment_performance_task_designer.md) | Authentic performance task with GRASPS, rubric, and exemplar |
| [`assessment_anchor_paper_exemplar_generator.md`](assessment/assessment_anchor_paper_exemplar_generator.md) | Calibration anchor papers per rubric level for norming |

### `grading-feedback/` (3) — Grading Workflows

| Prompt | Description |
|--------|-------------|
| [`grading_essay_feedback_by_rubric_criterion.md`](grading-feedback/grading_essay_feedback_by_rubric_criterion.md) | Criterion-by-criterion essay feedback that quotes student evidence |
| [`grading_whole_class_feedback_memo.md`](grading-feedback/grading_whole_class_feedback_memo.md) | Single class-facing memo synthesizing patterns across a stack |
| [`grading_speed_grading_triage.md`](grading-feedback/grading_speed_grading_triage.md) | Triage protocol sorting stacks into deep/light/quick feedback tiers |

### `inclusive/` (4) — Inclusive Instruction

| Prompt | Description |
|--------|-------------|
| [`inclusive_ell_wida_scaffolding.md`](inclusive/inclusive_ell_wida_scaffolding.md) | WIDA-aligned scaffolds across 6 proficiency levels |
| [`inclusive_udl_lesson_redesign.md`](inclusive/inclusive_udl_lesson_redesign.md) | UDL audit and redesign across engagement, representation, action |
| [`inclusive_504_accommodation_menu.md`](inclusive/inclusive_504_accommodation_menu.md) | Categorized 504 accommodation menu with leverage/feasibility ranking |
| [`inclusive_dyslexia_structured_literacy_plan.md`](inclusive/inclusive_dyslexia_structured_literacy_plan.md) | Science-of-Reading-grounded structured literacy intervention plan |

### `classroom-ops/` (3) — Classroom Operations

| Prompt | Description |
|--------|-------------|
| [`classops_management_plan_and_norms.md`](classroom-ops/classops_management_plan_and_norms.md) | Year-long classroom management plan with norms, response continuum, restorative integration |
| [`classops_routines_and_transitions_designer.md`](classroom-ops/classops_routines_and_transitions_designer.md) | High-leverage routines with signal, sequence, re-teach protocol |
| [`classops_restorative_conversation_script.md`](classroom-ops/classops_restorative_conversation_script.md) | Structured restorative conversation script with 5 questions and follow-through |

### `learner-writing/` (5) — Learner Writing Coach (Socratic, No Rewriting)

| Prompt | Description |
|--------|-------------|
| [`learnwrite_thesis_with_critique.md`](learner-writing/learnwrite_thesis_with_critique.md) | Coach a student to develop their own thesis through diagnostic critique |
| [`learnwrite_outline_generator.md`](learner-writing/learnwrite_outline_generator.md) | Genre-specific essay skeleton; student fills every content slot |
| [`learnwrite_citation_helper.md`](learner-writing/learnwrite_citation_helper.md) | Format MLA/APA/Chicago citations from student-supplied source elements |
| [`learnwrite_revision_socratic_coach.md`](learner-writing/learnwrite_revision_socratic_coach.md) | Quote student text, ask diagnostic questions, never substitute prose |
| [`learnwrite_source_credibility_evaluator.md`](learner-writing/learnwrite_source_credibility_evaluator.md) | Lateral reading + SIFT + CRAAP walkthrough; student decides credibility |

### `learner-math-science/` (3) — Learner Math/Science Coach (Socratic, No Final Answer)

| Prompt | Description |
|--------|-------------|
| [`learnmath_socratic_step_by_step_solver.md`](learner-math-science/learnmath_socratic_step_by_step_solver.md) | Stepping-stone questions for stuck math problems; student computes |
| [`learnmath_error_analyzer_own_work.md`](learner-math-science/learnmath_error_analyzer_own_work.md) | Locate, classify, and plan fix for errors on returned math work |
| [`learnsci_lab_report_scaffold.md`](learner-math-science/learnsci_lab_report_scaffold.md) | Section-by-section lab report coaching using CER framework |

### `learner-study-skills/` (2) — Learner Study Skills

| Prompt | Description |
|--------|-------------|
| [`learnstudy_mistake_log_reviewer.md`](learner-study-skills/learnstudy_mistake_log_reviewer.md) | Surface patterns across an accumulated mistake log; prioritize practice |
| [`learnstudy_active_recall_from_notes.md`](learner-study-skills/learnstudy_active_recall_from_notes.md) | Convert student notes into multi-level active-recall questions for spaced retrieval |

---

## Wave 2 Expansion (2026-05-10) — 25 New Prompts Across 3 Subdirectories

Wave 2 deepens subject pedagogy (16), expands assessment engineering (5), and extends grading workflows (4). Subject-pedagogy prompts cover problem strings and error analysis in math, mentor-text and conferring moves in ELA, CER and inquiry in science, primary-source and civic-action work in social studies, and TBLT + comprehensible-input in world languages. Assessment prompts target portfolios, SBG conversion, PLC common formative cycles, DOK leveling, and Bloom's stem banks. Grading prompts focus on math process feedback, lab reports, presentation/video critique, and reusable comment libraries.

### `subject-pedagogy/` (+16) — Subject-Specific Pedagogy

| Prompt | Description |
|--------|-------------|
| [`teachsubj_math_problem_string_designer.md`](subject-pedagogy/teachsubj_math_problem_string_designer.md) | 4–6 problem string warm-up with anchor → helper → bridge → stretch sequence |
| [`teachsubj_math_error_analysis_task.md`](subject-pedagogy/teachsubj_math_error_analysis_task.md) | Student analyzes a fictional wrong solution; locate, explain, correct, generalize |
| [`teachsubj_math_manipulatives_lesson.md`](subject-pedagogy/teachsubj_math_manipulatives_lesson.md) | Concrete-Pictorial-Abstract lesson sequence with bridges between representations |
| [`teachsubj_ela_mentor_text_close_read.md`](subject-pedagogy/teachsubj_ela_mentor_text_close_read.md) | Mentor-text lesson teaching one named craft move; notice → name → try |
| [`teachsubj_ela_reading_conference_planner.md`](subject-pedagogy/teachsubj_ela_reading_conference_planner.md) | 5–7 minute 1:1 reading conference using research → decide → teach → link |
| [`teachsubj_ela_book_club_discussion_guide.md`](subject-pedagogy/teachsubj_ela_book_club_discussion_guide.md) | 4–6 week book-club facilitation with rotating roles and culminating cross-book task |
| [`teachsubj_ela_grammar_minilesson.md`](subject-pedagogy/teachsubj_ela_grammar_minilesson.md) | 10-minute single-concept grammar lesson grounded in mentor sentences and live revision |
| [`teachsubj_ela_phonics_scope_sequence.md`](subject-pedagogy/teachsubj_ela_phonics_scope_sequence.md) | K–2 structured-literacy / Science-of-Reading phonics scope and sequence |
| [`teachsubj_science_lab_activity_designer.md`](subject-pedagogy/teachsubj_science_lab_activity_designer.md) | Full hands-on lab with investigation question, procedure, data, safety, and CER |
| [`teachsubj_science_cer_scaffold.md`](subject-pedagogy/teachsubj_science_cer_scaffold.md) | Three-tier CER scaffold (heavy / medium / light) with cross-tier rubric |
| [`teachsubj_science_fair_mentor.md`](subject-pedagogy/teachsubj_science_fair_mentor.md) | Student-facing Socratic mentor for the full science-fair arc — never writes for the student |
| [`teachsubj_socialstudies_primary_source_analysis.md`](subject-pedagogy/teachsubj_socialstudies_primary_source_analysis.md) | Single-source deep analysis using sourcing, contextualization, close reading, corroboration |
| [`teachsubj_socialstudies_current_events_connector.md`](subject-pedagogy/teachsubj_socialstudies_current_events_connector.md) | Connect a unit to current news with parallel framing and climate-protective discussion |
| [`teachsubj_socialstudies_civic_action_project.md`](subject-pedagogy/teachsubj_socialstudies_civic_action_project.md) | 4–8 week student-led civic action project with non-partisan framing and stakeholder analysis |
| [`teachsubj_worldlang_communicative_task.md`](subject-pedagogy/teachsubj_worldlang_communicative_task.md) | Task-based language teaching with proficiency-targeted scaffolds and outcome-based assessment |
| [`teachsubj_worldlang_comprehensible_input_scaffold.md`](subject-pedagogy/teachsubj_worldlang_comprehensible_input_scaffold.md) | TPRS-style comprehensible-input lesson with circling, PQA, and reading extension |

### `assessment/` (+5) — Assessment Engineering

| Prompt | Description |
|--------|-------------|
| [`assessment_portfolio_assessment_designer.md`](assessment/assessment_portfolio_assessment_designer.md) | Portfolio system: inclusion criteria, student curation, reflection scaffolds, anchor calibration |
| [`assessment_standards_based_grading_converter.md`](assessment/assessment_standards_based_grading_converter.md) | Convert traditional points to SBG with proficiency scales and reassessment policy |
| [`assessment_common_formative_assessment_plc.md`](assessment/assessment_common_formative_assessment_plc.md) | PLC-built CFA with item bank, calibration, data-meeting protocol, and tiered response |
| [`assessment_dok_item_generator.md`](assessment/assessment_dok_item_generator.md) | Coordinated items at all 4 Webb's DOK levels with per-item analysis defending the level |
| [`assessment_blooms_question_stem_bank.md`](assessment/assessment_blooms_question_stem_bank.md) | Topic-anchored question-stem bank across all 6 Bloom's levels with escalation sequence |

### `grading-feedback/` (+4) — Grading Workflows

| Prompt | Description |
|--------|-------------|
| [`grading_math_work_feedback.md`](grading-feedback/grading_math_work_feedback.md) | Process + answer feedback on math work with pattern-matched next moves |
| [`grading_lab_report_feedback.md`](grading-feedback/grading_lab_report_feedback.md) | CER-anchored lab-report feedback with quoted evidence and one revision call |
| [`grading_presentation_video_feedback.md`](grading-feedback/grading_presentation_video_feedback.md) | Timestamped feedback on student presentations / videos with relational tone calibration |
| [`grading_comment_library_generator.md`](grading-feedback/grading_comment_library_generator.md) | Reusable comment library by criterion × severity tier with personalization placeholders |

---

## Wave 5 Expansion (2026-05-09) — 17 New Prompts in 3 Subdirectories

A 17-prompt expansion adding higher-education and corporate-training scope, ed-tech production prompts, and advising prompts. Compliance and graduation-tracking prompts deliberately do not assert specific regulatory or jurisdictional requirements — the user supplies the controlling authoritative source.

### `higher-ed-corporate/` (10) — Higher Education & Corporate Training

| Prompt | Description |
|--------|-------------|
| [`hecorp_lecture_to_active_learning_converter.md`](higher-ed-corporate/hecorp_lecture_to_active_learning_converter.md) | Convert a lecture into an active-learning session, preserving objectives |
| [`hecorp_async_lms_module_designer.md`](higher-ed-corporate/hecorp_async_lms_module_designer.md) | Async online module ready to drop into Canvas / Blackboard / Brightspace / Moodle |
| [`hecorp_microlearning_module.md`](higher-ed-corporate/hecorp_microlearning_module.md) | 5–15 minute single-skill microlearning with practice rep and job aid |
| [`hecorp_office_hours_prep.md`](higher-ed-corporate/hecorp_office_hours_prep.md) | Instructor / TA prep for office hours, including triage by attendance and a recap for non-attendees |
| [`hecorp_ta_discussion_section_prep.md`](higher-ed-corporate/hecorp_ta_discussion_section_prep.md) | Graduate TA prep for discussion / recitation section, with equity moves and grading protocol |
| [`hecorp_online_course_conversion.md`](higher-ed-corporate/hecorp_online_course_conversion.md) | Whole in-person course converted to online or hybrid with phased build plan |
| [`hecorp_corporate_onboarding_program.md`](higher-ed-corporate/hecorp_corporate_onboarding_program.md) | Multi-week 30/60/90-day onboarding program with manager, buddy, and feedback loops |
| [`hecorp_compliance_training_module.md`](higher-ed-corporate/hecorp_compliance_training_module.md) | Generic compliance module that anchors on user-supplied authoritative source — no invented citations |
| [`hecorp_performance_support_job_aid.md`](higher-ed-corporate/hecorp_performance_support_job_aid.md) | At-the-moment-of-need job aid (decision tree, checklist, script card) tested in situ |
| [`hecorp_train_trainer_guide.md`](higher-ed-corporate/hecorp_train_trainer_guide.md) | Prepare internal SMEs to deliver training reliably — content, facilitation, and design fidelity |

### `ed-tech/` (5) — Educational Technology Production

| Prompt | Description |
|--------|-------------|
| [`edtech_class_slide_deck_designer.md`](ed-tech/edtech_class_slide_deck_designer.md) | Cognitive-load-aware instructional slide deck with speaker-notes layer |
| [`edtech_instructional_video_script.md`](ed-tech/edtech_instructional_video_script.md) | 3–10 min instructional video script with two-column narration / on-screen plan |
| [`edtech_choice_board_designer.md`](ed-tech/edtech_choice_board_designer.md) | Student choice board / HyperDoc anchored on one objective with must-do floor |
| [`edtech_blended_hyflex_lesson_designer.md`](ed-tech/edtech_blended_hyflex_lesson_designer.md) | Blended / HyFlex lesson where in-person, sync, and async paths are equivalent |
| [`edtech_lms_course_shell_setup.md`](ed-tech/edtech_lms_course_shell_setup.md) | End-to-end LMS course-shell setup checklist with student-view test |

### `advising/` (2) — Advising & School Counseling

| Prompt | Description |
|--------|-------------|
| [`advising_graduation_tracker.md`](advising/advising_graduation_tracker.md) | High-school graduation tracker + intervention plan; user supplies jurisdiction's requirements |
| [`advising_course_selection_advisor.md`](advising/advising_course_selection_advisor.md) | One-on-one course-selection conversation with goals, constraints, scenarios, and fallback |

---

## Wave 6 Expansion (2026-05-11) — 30 New Learner-Facing Prompts Across 7 Subdirectories

A 30-prompt expansion focused entirely on learner-facing prompts — conversational coaching tools students use directly to build skills. All prompts touching graded work (writing, research, math/science) enforce a strict Socratic stance: the AI never writes theses, paragraphs, citations, final answers, or substitution prose. Time-management and language-learning prompts use a lighter, more direct approach appropriate to skill development.

### `learner-writing/` (+4) — Learner Writing Coach

| Prompt | Description |
|--------|-------------|
| [`learnwrite_counterargument_generator.md`](learner-writing/learnwrite_counterargument_generator.md) | Develop counterarguments to a thesis through Socratic questioning — student generates all objections and rebuttals |
| [`learnwrite_peer_review_template.md`](learner-writing/learnwrite_peer_review_template.md) | Structured peer review using specific criteria; coach quotes student text and asks diagnostic questions |
| [`learnwrite_annotated_bibliography_helper.md`](learner-writing/learnwrite_annotated_bibliography_helper.md) | Guide each annotation element (summary, credibility, relevance) without summarizing sources for the student |
| [`learnwrite_academic_integrity_self_check.md`](learner-writing/learnwrite_academic_integrity_self_check.md) | Pre-submission integrity audit using targeted self-examination questions — no AI rewriting |

### `learner-reading/` (+5) — Learner Reading Coach

| Prompt | Description |
|--------|-------------|
| [`learnread_annotation_coach.md`](learner-reading/learnread_annotation_coach.md) | Build active annotation habits across three layers: comprehension, analysis, personal connection |
| [`learnread_chapter_summary_tool.md`](learner-reading/learnread_chapter_summary_tool.md) | Identify main ideas and chapter structure through guided questions — student writes every summary |
| [`learnread_vocabulary_in_context_decoder.md`](learner-reading/learnread_vocabulary_in_context_decoder.md) | Decode unfamiliar words from context before consulting a dictionary; inference first |
| [`learnread_authors_craft_analyzer.md`](learner-reading/learnread_authors_craft_analyzer.md) | Analyze authorial craft choices through guided questioning — name the technique, find the evidence, argue the effect |
| [`learnread_book_report_scaffold.md`](learner-reading/learnread_book_report_scaffold.md) | Section-by-section book report scaffolding; student produces all content through guided questioning |

### `learner-math-science/` (+4) — Learner Math/Science Coach

| Prompt | Description |
|--------|-------------|
| [`learnmath_word_problem_decoder.md`](learner-math-science/learnmath_word_problem_decoder.md) | Decode word problems by identifying what's being asked, what's given, and what strategy fits — student solves |
| [`learnsci_experimental_design_helper.md`](learner-math-science/learnsci_experimental_design_helper.md) | Coach experimental design (question, hypothesis, variables, procedure) without writing any component for the student |
| [`learnsci_data_interpreter.md`](learner-math-science/learnsci_data_interpreter.md) | Guide student interpretation of data, graphs, and results through questions — student draws all conclusions |
| [`learnsci_concept_map_builder.md`](learner-math-science/learnsci_concept_map_builder.md) | Build concept map connections through Socratic questioning about relationships between terms |

### `learner-language/` (5 new) — L2 Language Learning

| Prompt | Description |
|--------|-------------|
| [`learnlang_daily_conversation_drill.md`](learner-language/learnlang_daily_conversation_drill.md) | Scenario-based L2 conversation drill; AI stays in target language with per-exchange feedback and single error pattern debrief |
| [`learnlang_topical_vocabulary_builder.md`](learner-language/learnlang_topical_vocabulary_builder.md) | Context-first L2 vocabulary: context sentence → inference → confirm → production → spaced recall gap-fill |
| [`learnlang_l2_grammar_explainer.md`](learner-language/learnlang_l2_grammar_explainer.md) | Grammar rule in 1–2 sentences with example pairs, tricky cases, comprehension check, and 5 practice prompts |
| [`learnlang_idiom_decoder.md`](learner-language/learnlang_idiom_decoder.md) | Context-first idiom decoding: inference before explanation → literal vs. figurative → register → student production |
| [`learnlang_pronunciation_coach_text.md`](learner-language/learnlang_pronunciation_coach_text.md) | Text-mode pronunciation coaching with IPA, plain phonetic spelling, articulation placement, and minimal pairs |

### `learner-research/` (4 new) — Research Skills Coach

| Prompt | Description |
|--------|-------------|
| [`learnresearch_question_refinement.md`](learner-research/learnresearch_question_refinement.md) | Diagnostic four-test research question critique (statement vs. question, scope, researchability, debatability) — AI never rewrites |
| [`learnresearch_keyword_search_strategy.md`](learner-research/learnresearch_keyword_search_strategy.md) | Build Boolean search strategies through concept extraction and synonym clustering — student constructs every query |
| [`learnresearch_source_synthesis_chart.md`](learner-research/learnresearch_source_synthesis_chart.md) | Map agreement, disagreement, and outliers across sources to identify themes — student summarizes and names all themes |
| [`learnresearch_interview_question_critique.md`](learner-research/learnresearch_interview_question_critique.md) | Five-test critique of interview questions (open/closed, leading language, double-barreled, vagueness, scope) — AI never rewrites |

### `learner-study-skills/` (+4) — Study Skills Coach

| Prompt | Description |
|--------|-------------|
| [`learnstudy_cornell_notes_converter.md`](learner-study-skills/learnstudy_cornell_notes_converter.md) | Convert raw notes to Cornell format; student identifies main points, generates cue questions, and writes summary from memory |
| [`learnstudy_feynman_teach_back_coach.md`](learner-study-skills/learnstudy_feynman_teach_back_coach.md) | Teach-back coaching using the Feynman technique; AI probes for gaps but never explains the concept itself |
| [`learnstudy_test_day_strategy.md`](learner-study-skills/learnstudy_test_day_strategy.md) | Direct test-day strategy tailored to format, point distribution, and anxiety vs. time-management diagnosis |
| [`learnstudy_finals_week_plan.md`](learner-study-skills/learnstudy_finals_week_plan.md) | Collaborative finals week schedule with triage matrix (weight × difficulty × deadline), session goals, and buffer time |

### `learner-time-discussion/` (4 new) — Time Management & Discussion Prep

| Prompt | Description |
|--------|-------------|
| [`learntime_assignment_tracker_planner.md`](learner-time-discussion/learntime_assignment_tracker_planner.md) | Full-capture weekly planner: brain dump → due dates + estimates → urgency triage → daily plan → first action today |
| [`learntime_big_project_decomposer.md`](learner-time-discussion/learntime_big_project_decomposer.md) | Break a multi-week project into phases, tasks, time estimates, and a backward-planned milestone calendar |
| [`learndisc_office_hours_question_prep.md`](learner-time-discussion/learndisc_office_hours_question_prep.md) | Convert vague confusion into specific, productive office-hours questions; AI never answers the academic content |
| [`learndisc_class_discussion_prep.md`](learner-time-discussion/learndisc_class_discussion_prep.md) | Prepare a specific claim, textual evidence, counterargument, and genuine question for class discussion |

---

## Maintenance

- [Prompt Maintenance Backlog](MAINTENANCE_BACKLOG.md)
- [Prompt Test Review](PROMPT_TEST_REVIEW.md)

---

## Prompts in This Domain (19)

### Core Teaching Prompts (Original)

| Prompt | Description | Best For |
|--------|-------------|----------|
| [`teaching_lesson_plan_generator.md`](teaching_lesson_plan_generator.md) | Create comprehensive, standards-aligned lesson plans with differentiation | Daily planning, substitute materials, observation prep |
| [`teaching_assessment_rubric_builder.md`](teaching_assessment_rubric_builder.md) | Design valid assessments with clear rubrics and scoring guides | Unit tests, performance tasks, project rubrics |
| [`teaching_differentiation_planner.md`](teaching_differentiation_planner.md) | Design differentiated instruction for diverse learners | Mixed-ability classrooms, IEP support, ELL adaptation |
| [`teaching_socratic_discussion_facilitator.md`](teaching_socratic_discussion_facilitator.md) | Design and facilitate discussion-based learning experiences | Seminars, critical thinking, text analysis |
| [`teaching_student_feedback_composer.md`](teaching_student_feedback_composer.md) | Create specific, actionable, growth-oriented student feedback | Report cards, written comments, feedback conversations |
| [`field_guide.md`](field_guide.md) | Prompt engineering techniques curated for educators | Learning about techniques for education prompts |

### Special Education & Student Support

| Prompt | Description | Best For |
|--------|-------------|----------|
| [`teaching_iep_goal_writer.md`](teaching_iep_goal_writer.md) | Generate SMART IEP and 504 plan goals with progress monitoring frameworks | Annual IEP goals, 504 plans, PLAAFP summaries, progress monitoring |
| [`teaching_behavior_support_planner.md`](teaching_behavior_support_planner.md) | Design behavior intervention plans, SEL activities, and restorative practice guides | Behavior plans, SEL integration, de-escalation, community building |

### Communication & Reporting

| Prompt | Description | Best For |
|--------|-------------|----------|
| [`teaching_parent_communication_composer.md`](teaching_parent_communication_composer.md) | Create professional, empathetic parent communications across multiple formats | Newsletters, conference prep, progress updates, behavior notices |
| [`teaching_report_card_comment_generator.md`](teaching_report_card_comment_generator.md) | Generate personalized, strengths-based report card comments by subject | End-of-term comments, progress reports, batch generation |

### Curriculum & Planning

| Prompt | Description | Best For |
|--------|-------------|----------|
| [`teaching_unit_curriculum_planner.md`](teaching_unit_curriculum_planner.md) | Design multi-week units using Understanding by Design backward design framework | Unit planning, scope and sequence, backward design |
| [`teaching_standards_alignment_mapper.md`](teaching_standards_alignment_mapper.md) | Map curriculum to standards, identify gaps, and generate crosswalk documents | Curriculum audits, standards mapping, vertical alignment |
| [`teaching_syllabus_course_designer.md`](teaching_syllabus_course_designer.md) | Design comprehensive higher-ed syllabi with AI policies and inclusive design | College course design, AI use policies, accreditation prep |
| [`teaching_project_based_learning_designer.md`](teaching_project_based_learning_designer.md) | Design authentic PBL units with driving questions and public products | Multi-week projects, inquiry learning, exhibitions |

### Daily Classroom Tools

| Prompt | Description | Best For |
|--------|-------------|----------|
| [`teaching_exit_ticket_generator.md`](teaching_exit_ticket_generator.md) | Create quick formative assessments aligned to Bloom's with data analysis guidance | End-of-lesson checks, misconception identification, instructional response |
| [`teaching_reading_level_adapter.md`](teaching_reading_level_adapter.md) | Adapt texts to multiple reading levels while preserving content and rigor | Differentiated reading, ELL adaptations, text sets |
| [`teaching_vocabulary_builder.md`](teaching_vocabulary_builder.md) | Design subject-specific vocabulary instruction with tiered words and multi-modal activities | Academic language, content vocabulary, ELL vocabulary support |
| [`teaching_substitute_plan_generator.md`](teaching_substitute_plan_generator.md) | Create comprehensive substitute plans for emergency and planned absences | Sub plans, emergency binder, long-term absence |


### Instructional Response Cycle

| Prompt | Description | Best For |
|--------|-------------|----------|
| [`teaching_preassessment_designer.md`](teaching_preassessment_designer.md) | Design objective-aligned pre-assessments with misconception coding and action-ready analysis | Unit launches, baseline checks, PLC prep |
| [`teaching_misconception_diagnoser.md`](teaching_misconception_diagnoser.md) | Diagnose error patterns with a misconception taxonomy and prioritize instructional response | Post-quiz analysis, data meetings, targeted grouping |
| [`teaching_reteach_intervention_planner.md`](teaching_reteach_intervention_planner.md) | Build time-boxed reteach interventions tied to objective gaps and reassessment gates | Intervention blocks, MTSS/RTI cycles, mastery recovery |
| [`teaching_small_group_rotation_planner.md`](teaching_small_group_rotation_planner.md) | Plan misconception-driven small-group rotations with station evidence and follow-up rules | Workshop rotations, station teaching, mixed-readiness support |

### Emerging Areas

| Prompt | Description | Best For |
|--------|-------------|----------|
| [`teaching_ai_literacy_lesson_designer.md`](teaching_ai_literacy_lesson_designer.md) | Design age-appropriate AI literacy lessons covering concepts, ethics, and critical evaluation | AI education K-12, digital citizenship, prompt engineering for students |

### Exemplar Prompts (Study These)

| Prompt | Location | What It Demonstrates |
|--------|----------|---------------------|
| `learning_code_refactoring_exercises.md` | [domain-learning-coding/](../domain-learning-coding/) | Excellent scaffolding, progressive difficulty |
| `learning_mini_lesson_generation.md` | [domain-learning-coding/](../domain-learning-coding/) | Structured lesson format, time-bounded |

### Related Education Resources

**Image Generation for Education:**
See `domain-image-generation/` for general image-generation guides. Worksheet-specific generators are not currently bundled in this repo.
- Writing prompts and graphic organizers

**Coding Education (17 prompts):**
Located in `domain-learning-coding/`
- Concept explanations
- Refactoring exercises
- Debugging practice
- Mini lesson generation

---

## Templates

### Template 1: Complete Lesson Plan

```markdown
# Lesson Plan: [Topic]

**Subject:** [Subject area]
**Grade Level:** [Grade(s)]
**Duration:** [Time - e.g., 45 minutes]
**Standards:** [Applicable standards - Common Core, NGSS, state]

---

## Learning Objectives

By the end of this lesson, students will be able to:
1. [Observable, measurable objective using Bloom's verb]
2. [Observable, measurable objective using Bloom's verb]

---

## Prior Knowledge Required

Students should already:
- [Prerequisite skill/knowledge 1]
- [Prerequisite skill/knowledge 2]

**Prerequisite Check:** [How you'll verify students are ready]

---

## Materials

**Teacher Materials:**
- [Item 1]
- [Item 2]

**Student Materials:**
- [Item 1 - per student or per group]
- [Item 2]

**Technology Requirements:** [If applicable]

---

## Lesson Procedure

### Engage (5-7 minutes)
**Purpose:** Activate prior knowledge, hook interest

**Activity:**
[Specific opening activity - question, video clip, demonstration, etc.]

**Teacher Actions:**
- [What teacher does]

**Student Actions:**
- [What students do]

**Transition:** [How to move to next phase]

---

### Explore (10-15 minutes)
**Purpose:** Students interact with concept before formal instruction

**Activity:**
[Hands-on exploration, inquiry task, or guided discovery]

**Teacher Actions:**
- [Circulate, observe, ask probing questions]
- [Note common misconceptions to address]

**Student Actions:**
- [Active engagement with materials/concepts]
- [Record observations/thinking]

**Differentiation:**
- Scaffold: [For struggling learners]
- Extension: [For advanced learners]

---

### Explain (10-12 minutes)
**Purpose:** Direct instruction, concept clarification

**Key Concepts:**
1. [Concept 1 with explanation]
2. [Concept 2 with explanation]

**Vocabulary:**
- [Term 1]: [Student-friendly definition]
- [Term 2]: [Student-friendly definition]

**Check for Understanding:**
- [Quick formative check - thumbs up, whiteboard response, etc.]

---

### Elaborate (10-15 minutes)
**Purpose:** Apply learning to new situations

**Activity:**
[Application task, problem-solving, or extension activity]

**Success Criteria:**
- [ ] [What successful completion looks like]

**Differentiation:**
- Scaffold: [Modified version for support]
- Extension: [Challenge version for advanced]

---

### Evaluate (5-10 minutes)
**Purpose:** Assess learning, provide closure

**Assessment:**
[Exit ticket, quiz, performance task - aligned to objectives]

**Closure:**
[Summary activity, reflection prompt, connection to next lesson]

---

## Assessment Alignment

| Objective | Formative Assessment | Summative Assessment |
|-----------|---------------------|---------------------|
| [Objective 1] | [How checked during lesson] | [How measured at end] |
| [Objective 2] | [How checked during lesson] | [How measured at end] |

---

## Differentiation Strategies

**For Struggling Learners:**
- [Specific accommodation 1]
- [Specific accommodation 2]

**For Advanced Learners:**
- [Specific extension 1]
- [Specific extension 2]

**For English Language Learners:**
- [Specific support 1]
- [Specific support 2]

---

## Reflection (Post-Lesson)

**What worked well:**
[To be filled after teaching]

**What to modify:**
[To be filled after teaching]

**Student misconceptions observed:**
[To be filled after teaching]
```

### Template 2: Assessment/Rubric Creation

```markdown
# Assessment: [Topic/Skill]

**Type:** [Formative/Summative]
**Subject:** [Subject]
**Grade Level:** [Grade]
**Time:** [Duration]
**Standards:** [Aligned standards]

---

## Objectives Assessed

This assessment measures:
1. [Objective 1]
2. [Objective 2]

---

## Assessment Items

### Section A: [Question Type - e.g., Multiple Choice]
**Objective Assessed:** [Which objective]
**Points:** [Value]

1. [Question]
   a) [Option - correct]
   b) [Option - common misconception]
   c) [Option - distractor]
   d) [Option - distractor]

   *Rationale for correct answer: [Why A is right]*
   *Common error: [Why students might choose B]*

[Continue questions...]

---

### Section B: [Question Type - e.g., Short Answer]
**Objective Assessed:** [Which objective]
**Points:** [Value]

1. [Question]

   **Exemplary Response:** [What an excellent answer includes]

   **Scoring Guide:**
   - 3 points: [Full credit criteria]
   - 2 points: [Partial credit criteria]
   - 1 point: [Minimal credit criteria]
   - 0 points: [No credit criteria]

---

### Section C: [Question Type - e.g., Extended Response/Performance]
**Objective Assessed:** [Which objective]
**Points:** [Value]

**Prompt:**
[Extended task description]

**Rubric:**

| Criterion | Exemplary (4) | Proficient (3) | Developing (2) | Beginning (1) |
|-----------|---------------|----------------|----------------|---------------|
| [Criterion 1] | [Description] | [Description] | [Description] | [Description] |
| [Criterion 2] | [Description] | [Description] | [Description] | [Description] |
| [Criterion 3] | [Description] | [Description] | [Description] | [Description] |

---

## Answer Key

[Complete answer key with explanations]

---

## Accommodations

**Extended Time:** [Which students, how much]
**Modified Version:** [What's different]
**Read Aloud:** [Which sections permitted]
```

### Template 3: Worksheet Generator

```markdown
# Worksheet: [Topic]

**Subject:** [Subject]
**Grade Level:** [Grade]
**Objective:** [What students will practice]
**Time:** [Estimated completion time]

---

## Instructions

[Clear, grade-appropriate instructions]

---

## Practice Problems

### Part 1: [Skill Level - Basic/Foundational]

[Problems 1-5: Entry-level practice]

### Part 2: [Skill Level - Intermediate]

[Problems 6-10: Application of skill]

### Part 3: [Skill Level - Challenge]

[Problems 11-15: Extension/complex application]

---

## Self-Check

**Check Your Understanding:**
After completing this worksheet, you should be able to:
- [ ] [Self-assessment item 1]
- [ ] [Self-assessment item 2]

**If you struggled with Part 1:** [Recommendation for review]
**If you completed Part 3 easily:** [Extension recommendation]

---

## Answer Key (Separate page or teacher version)

[Complete answers with work shown for complex problems]
```

---

## Worked Example

### Scenario: Creating a History Worksheet

**User says:** "I need a worksheet on the causes of World War I for my 10th grade class"

**Step 1: Classification**

- Task Type: CREATE
- Domain: Education/Teaching
- Specific Type: Worksheet creation

**Step 2: Context Gathering**

**Known:**
- Topic: Causes of WWI
- Grade: 10th
- Format: Worksheet

**Need to determine:**
- What aspect of WWI causes (MAIN, assassination, alliances)?
- How much time for completion?
- Prior knowledge (what have they already learned)?
- Standards alignment needed?
- Mix of question types?
- Purpose (formative check, homework, test prep)?

**Step 3: Apply Template**

Use **Template 3: Worksheet Generator** with history-specific adaptations

**Step 4: Build Prompt**

```markdown
# Create WWI Causes Worksheet

**Objective:** Create a worksheet assessing understanding of the causes of World War I

## Context

**Grade Level:** 10th grade (ages 15-16)
**Subject:** World History / US History
**Topic:** Causes of World War I

**Prior Knowledge:**
- Students have completed a unit on late 19th century imperialism
- Students have been introduced to the alliance system
- Students have learned about nationalism in Europe
- Most recent lesson covered the assassination of Archduke Franz Ferdinand

**Standards Alignment:**
[Specify state standards or Common Core RH.9-10 for history]

**Time:** 20-25 minutes completion time

## Requirements

**Content Coverage:**
- MAIN causes (Militarism, Alliances, Imperialism, Nationalism)
- The spark (assassination)
- How factors interconnected

**Question Types:**
- Multiple choice (4-5 questions) - basic recall and identification
- Matching (1 section) - alliances/countries
- Short answer (2-3 questions) - explain connections
- Document analysis (1 primary source excerpt) - historical thinking
- Extended response (1 question) - argue which cause was most significant

**Bloom's Levels:**
- 40% Remember/Understand (identify, describe)
- 40% Apply/Analyze (explain connections, interpret document)
- 20% Evaluate (argue, justify)

**Differentiation:**
- Include word bank option for struggling students
- Include extension question for advanced students
- Ensure reading level appropriate for 10th grade (Flesch-Kincaid 9-10)

## Output Format

1. Student worksheet (clean, printer-friendly)
2. Teacher answer key with:
   - Correct answers
   - Rationale for correct answers
   - Common misconceptions to watch for
   - Rubric for extended response

## Quality Criteria

- [ ] All MAIN causes addressed
- [ ] Questions progress from simple to complex
- [ ] Primary source is age-appropriate and relevant
- [ ] Extended response has clear rubric
- [ ] Answer key includes teaching notes
- [ ] Time estimate is realistic (test with reading time)
```

---

## Anti-Patterns for Education

### Mistake 1: Grade-Level Mismatch

**Problem:** Content too advanced or too simple for stated grade

**Bad:**
```
Create a worksheet on cell division for 5th grade:
"Analyze the role of cyclin-dependent kinases in regulating the G1/S checkpoint"
```

**Good:**
```
Create a worksheet on cell division for 5th grade:
"Draw a cell before and after it divides. Label the parts you can see."
(With scaffolding: diagram outline, word bank of parts)
```

---

### Mistake 2: Time Unrealism

**Problem:** Activities don't fit available time

**Bad:**
```
"Create a 45-minute lesson" that includes:
- 15-minute lecture
- 20-minute group project
- 15-minute presentations
- 10-minute assessment
```

**Good:**
```
"Create a 45-minute lesson with realistic timing:
- 5-min warm-up/hook
- 10-min direct instruction
- 15-min guided practice
- 10-min independent practice
- 5-min closure/exit ticket

Note: Built-in 2-minute transitions between phases"
```

---

### Mistake 3: Objective-Assessment Misalignment

**Problem:** Assessing different things than taught

**Bad:**
```
Objective: "Students will analyze the causes of the French Revolution"
Assessment: "List three facts about the French Revolution"
(Teaching analysis, testing recall)
```

**Good:**
```
Objective: "Students will analyze the causes of the French Revolution"
Assessment: "Read this primary source. Explain how it shows one cause of the French Revolution. Use evidence from the text."
(Teaching and testing analysis)
```

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                 EDUCATION QUICK REFERENCE                                  ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  ALWAYS SPECIFY:                                                          ║
║  □ Grade level (and actual abilities if different)                       ║
║  □ Time available                                                         ║
║  □ Prior knowledge assumed                                                ║
║  □ Standards alignment (if required)                                      ║
║  □ Differentiation needs (IEPs, ELLs, advanced)                          ║
║                                                                           ║
║  LEARNING OBJECTIVES MUST BE:                                             ║
║  □ Observable (can see/hear students doing it)                           ║
║  □ Measurable (can assess if achieved)                                   ║
║  □ Student-centered ("Students will be able to...")                      ║
║  □ Aligned to what you'll teach AND assess                               ║
║                                                                           ║
║  LESSON STRUCTURE (5E MODEL):                                             ║
║  1. Engage - Hook interest, activate prior knowledge                      ║
║  2. Explore - Students interact with concept                              ║
║  3. Explain - Direct instruction, clarification                           ║
║  4. Elaborate - Apply to new situations                                   ║
║  5. Evaluate - Check learning, provide closure                            ║
║                                                                           ║
║  DIFFERENTIATION CHECKLIST:                                               ║
║  □ Scaffold for struggling (word banks, graphic organizers, models)      ║
║  □ Extend for advanced (deeper questions, additional challenge)          ║
║  □ Multiple modalities (visual, auditory, kinesthetic)                   ║
║  □ ELL supports (visuals, simplified language, native language)          ║
║                                                                           ║
║  BLOOM'S QUICK VERBS:                                                     ║
║  Remember: list, define, identify, recall, name                           ║
║  Understand: explain, summarize, classify, compare                        ║
║  Apply: use, demonstrate, solve, implement                                ║
║  Analyze: compare, contrast, examine, differentiate                       ║
║  Evaluate: judge, justify, defend, critique                               ║
║  Create: design, develop, construct, produce                              ║
║                                                                           ║
║  WORKSHEET PROMPTS TO STUDY:                                              ║
║  • domain-image-generation/ (general image-gen guides)                    ║
║  • domain-learning-coding/ (scaffolded practice, mini lessons)           ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Field Guide

For comprehensive prompt engineering techniques specifically tailored to education:

| Field Guide | Purpose |
|-------------|---------|
| [`field_guide.md`](field_guide.md) | Detailed guide on prompt techniques for educators, instructional designers, and tutors |

---

## Related Resources

| Resource | Purpose |
|----------|---------|
| [NON_CODING_QUICK_START.md](../NON_CODING_QUICK_START.md) | Universal non-coding principles |
| [domain-learning-coding/](../domain-learning-coding/) | Coding education prompts |
| [domain-image-generation/](../domain-image-generation/) | Image generation guides |
| [PROMPT_QUALITY_STANDARDS.md](../PROMPT_QUALITY_STANDARDS.md) | Quality tier definitions |

---

## Quick Start

**For lesson planning:**
```
Use: teaching_lesson_plan_generator.md
Input: Subject, topic, grade, time, standards
Output: Complete lesson plan with 5E model
```

**For assessment creation:**
```
Use: teaching_assessment_rubric_builder.md
Input: Learning objectives, assessment type, grade
Output: Complete assessment with rubrics
```

**For differentiation:**
```
Use: teaching_differentiation_planner.md
Input: Learning objective, student population
Output: Tiered activities for all learners
```

**For IEP/504 goals:**
```
Use: teaching_iep_goal_writer.md
Input: Disability category, present levels, goal domain, grade
Output: SMART goals, benchmarks, accommodations, progress monitoring
```

**For parent communication:**
```
Use: teaching_parent_communication_composer.md
Input: Communication type, grade, key content, tone
Output: Drafted communication ready to personalize
```

**For unit planning:**
```
Use: teaching_unit_curriculum_planner.md
Input: Subject, topic, grade, duration, standards
Output: Complete backward design unit with scope and sequence
```

**For AI literacy:**
```
Use: teaching_ai_literacy_lesson_designer.md
Input: Grade band, focus area, tools available
Output: Age-appropriate AI literacy lesson with activities
```

---

*Document Version: 2.0*
*Created: 2026-01-26*
*Updated: 2026-02-20 - Added 13 new teaching prompts (IEP goals, parent communication, report cards, unit planning, reading level adaptation, exit tickets, substitute plans, behavior/SEL, AI literacy, syllabus design, PBL, vocabulary, standards alignment)*
*Domain: Education & Teaching*
