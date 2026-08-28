---
title: "Higher-Ed Course Design (Constructive Alignment, Biggs)"
category: education-teaching/program/curriculum-design
description: "Design a higher-education course using Biggs' constructive alignment — intended learning outcomes (ILOs) directly aligned with teaching/learning activities and assessment tasks — producing a full course shell including module sequence, assessment plan, workload computation, and accessibility review. Use whenever the user mentions course design, course redesign, syllabus creation, constructive alignment, ILOs, modality conversion, or aligning a course to program outcomes — even if they don't name Biggs explicitly."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - education
  - curriculum-design
  - course-design
  - constructive-alignment
  - biggs
  - higher-ed
  - syllabus
  - accessibility
  - workload
updated: "2026-07-18"
related_prompts:
  - domain-education-teaching/program/curriculum-design/program_scope_sequence_he.md
  - domain-education-teaching/program/curriculum-design/program_learning_objectives_writer_blooms.md
  - ../program-outcomes-assessment/teaching_outcomes_to_assessment_mapper.md
  - ../program-outcomes-assessment/teaching_assessment_blueprint_builder.md
---

# Higher-Ed Course Design (Constructive Alignment)

**Objective:** Design a complete higher-education course using Biggs' constructive alignment: intended learning outcomes (ILOs), teaching and learning activities (TLAs), and assessment tasks (ATs) are tightly aligned so that what is taught, what learners do, and what is assessed all point to the same demonstrable performance. Output: a course shell with module sequence, assessment plan, workload computation, accessibility review, and syllabus components.

**Key terms used throughout:**
- **PSLO** — Program Student Learning Outcome (program level; ILOs derive from these)
- **ILO** — Intended Learning Outcome (course level)
- **TLA** — Teaching/Learning Activity; **AT** — Assessment Task
- **Depth codes:** **I** = Introduce, **D** = Develop, **M** = Master — the level at which this course contributes to a given PSLO

## When to Use
- ✅ Designing a new university or college course
- ✅ Redesigning a course after PSLO revision or accreditation feedback
- ✅ Converting a course modality (in-person ↔ online ↔ hybrid)
- ✅ Aligning a course to a program-level curriculum map
- ❌ K-12 unit/lesson design (use unit planners in `domain-education-teaching/`)
- ❌ Workforce training design (use `teaching_scope_sequence_workforce.md`)
- ❌ Program-level scope and sequence (use `teaching_scope_sequence_he.md`)

## Inputs Required
- **Institution and course identity:** course code, title, credit hours, level (UG / grad)
- **Program PSLOs the course contributes to** (with depth: I / D / M)
- **Term length:** weeks, contact hours per week, expected out-of-class hours
- **Modality:** in-person / online / hybrid / hyflex / async / sync
- **Class size and population:** number of students, prerequisites learners arrive with, ELL or international proportion
- **Required materials, tools, platforms** (LMS, software, lab equipment)
- **Institutional policies:** late work, attendance, academic integrity, accommodations
- **Existing course materials** (optional): if redesigning, list current artifacts

### Handling Missing Inputs
Do not stall the whole design over minor gaps, but do not fabricate load-bearing inputs either.

| If missing... | Action |
|---|---|
| PSLOs | **Ask.** ILOs derive from PSLOs; without them the alignment chain has no anchor. If the user has none, offer to draft provisional PSLOs and label them clearly as provisional. |
| Credit hours or term length | **Ask.** Workload computation is impossible without them. |
| Modality | Ask; if unanswered, default to in-person and flag the assumption. |
| Class size, population, policies, materials | Assume sensible defaults (e.g., 30 students, standard institutional policies), state each assumption explicitly in Section 1, and mark it `[ASSUMED — confirm]`. |

For long courses (14+ weeks) or when many inputs are assumed, offer a **checkpoint**: deliver Sections 1–3 (identity, ILOs, assessment plan) first and confirm before building the full module sequence. Alignment errors caught at the ILO stage are cheap; caught at Module 12, they are not.

## Constraints

**Must:**
- Produce 4-8 ILOs at course level, observable and Bloom's-tagged
- For every ILO, identify TLAs and ATs — the alignment is mandatory in both directions (no ILO without an AT; no AT without an ILO)
- Compute realistic workload: contact hours + expected out-of-class hours per week, total over the term
- Distribute summative assessment weight to honor cognitive levels (Create-level ILOs warrant high-weight performance tasks; Remember-level ILOs warrant low-weight checks); weights sum to 100%
- Include formative assessment in every module, with feedback returned before the next related summative AT
- Address prerequisite gaps explicitly: identify assumed prior knowledge and provide a bridge (diagnostic in week 1, refresher materials, or scaffolded early modules)
- Address accessibility: alt text, captions, screen-reader compatibility, alternative-format options, sensory considerations
- Address academic integrity in the assessment design (not just policy mention)

**Must Not:**
- Write ILOs the course cannot actually produce (more than the term length supports)
- Use vague, unobservable ILO verbs (*understand, know, appreciate, be familiar with, learn*) — use observable Bloom's-aligned verbs (*analyze, design, evaluate, construct, explain, apply*)
- Use unaligned assessments (e.g., MCQ for Create-level ILOs)
- Assign workload exceeding the credit-hour standard (default if unspecified: ~3 total hours/week/credit for UG, higher for grad — confirm the institution's own standard)
- Concentrate weight so one AT decides the course (a single AT above ~50% needs explicit justification)
- Use materials behind paywalls or in inaccessible formats without alternatives
- Ignore prerequisite gaps (assume mastery learners may not have)
- Generate a syllabus that omits institutional-policy elements

## Instructions

1. **Confirm course identity and PSLOs.**
   - Echo back: course code, credit hours, level, contributing PSLOs (with depth I/D/M).
   - Apply the Missing Inputs table above. If PSLOs are missing, request them — ILOs derive from PSLOs.

2. **Derive course ILOs from PSLOs.**
   - 4-8 ILOs, observable, Bloom's-tagged, aligned to PSLOs.
   - Each ILO contributes to ≥1 PSLO at the specified depth; the total set must honor the course's depth contribution (e.g., if the course is M-depth for PSLO-3, ≥1 ILO must demand Master-level performance of PSLO-3).
   - **Example — weak vs. strong ILO:**
     - ❌ "Students will understand statistical inference." (unobservable; no Bloom's level; no context)
     - ✅ "Given a real dataset and research question, select and justify an appropriate inferential test, execute it in R, and interpret the result for a non-technical audience. (Analyze/Evaluate; PSLO-2, D)"

3. **Design assessment tasks (ATs) before module activities** (Biggs' principle: start from the evidence of learning).
   - For each ILO, name 1-3 assessment evidence types that can produce signal *at the ILO's Bloom's level* (e.g., Create → project/portfolio/design artifact; Analyze → case analysis; Remember/Understand → quiz).
   - Build the summative plan: ATs with weighting (summing to 100%) and due weeks, spaced so no single week stacks multiple major deadlines.
   - Build the formative plan: weekly low-stakes checks aligned to module ILOs, each returning feedback before the related summative.

4. **Design teaching/learning activities (TLAs).**
   - For each ILO: what will learners DO to develop the capability? TLAs are active — practice, application, discussion, problem-solving, peer review, simulation. Lectures count as TLAs only when paired with active processing tasks.
   - Adapt TLAs to modality: async courses need structured asynchronous interaction (discussion protocols, peer review workflows) in place of live activities; hyflex TLAs must work for both rooms.

5. **Sequence modules.**
   - Typical term: 10-16 weeks of modules + assessment milestones.
   - Week 1 includes the prerequisite diagnostic/bridge if gaps were identified.
   - Foundational ILOs → integrative ILOs across the term.
   - Each module: title, week(s), ILOs in focus, TLAs, formative check, readings/materials, workload hours.

6. **Compute workload.**
   - Per module: contact + reading/prep + assignments + assessment time. Sum per week and over the term; confirm against the credit-hour standard. If over, trim or rebalance and say what was cut.

7. **Design accessibility and inclusion.**
   - Audit materials format (captions, alt text, screen-reader compatibility, dyslexia-friendly fonts where available).
   - Provide alternative-format paths (audio + text, multiple modes of demonstration).
   - Sensory considerations (lab safety, content warnings where appropriate).
   - Apply UDL principles: multiple means of engagement, representation, and action/expression — name where each appears in the design, not as a generic statement.

8. **Address academic integrity.**
   - Design assessments that are AI-resistant or AI-transparent per policy: performance tasks, in-class assessments, drafts-with-process-evidence, oral defenses.
   - State the course's AI-use stance per AT (prohibited / permitted-with-citation / integrated), and cite how the institutional integrity policy applies.

9. **Produce syllabus components.**
   - Course identity, description and rationale, ILOs (with PSLO mapping), required materials, assessment plan with weights and due dates, module schedule, policies (late work, attendance, integrity, accommodations, communication), accessibility statement.

10. **Audit the design.**
    - Complete the Section 10 audit table honestly — a "Fail" with a remediation note is more useful than a rubber-stamped "Pass."
    - For each Fail: state the specific gap, the fix, and apply the fix before final delivery if it is within scope; otherwise flag it as an open item for the user.
    - Verify bidirectional alignment: every ILO appears in ≥1 AT **and** every AT maps to ≥1 ILO (no orphan assessments).

## Output Format

### Section 1: Course Identity
- Code, title, credits, level, term length, contact hours, modality, class size, PSLO contributions (with depth)
- Assumptions made (each marked `[ASSUMED — confirm]`)

### Section 2: Course ILOs

| ILO # | ILO Text | Bloom's | Contributes to PSLO | Depth in PSLO (I/D/M) |
|---|---|---|---|---|

### Section 3: Assessment Plan

**Summative Assessments** (weights sum to 100%):

| AT # | Title | Format | Weight | Due Week | ILOs Assessed | AI-Use Stance | Integrity Considerations |
|---|---|---|---|---|---|---|---|

**Formative Assessments:** (per module — see module table; note feedback turnaround relative to related summatives)

### Section 4: Module Sequence

| Module # | Week(s) | Title | ILOs in Focus | TLAs | Formative Check | Readings/Materials | Workload (hours) |
|---|---|---|---|---|---|---|---|

### Section 5: ILO × TLA × AT Alignment Matrix

| ILO | TLAs (where developed) | ATs (where assessed) |
|---|---|---|
| ILO-1 | Modules 1-3 (problem sets, discussion) | AT-2 (midterm), AT-4 (project) |

Then confirm: every ILO has ≥1 AT; every AT maps to ≥1 ILO.

### Section 6: Workload Computation

| Component | Hours per Week | Total Hours Over Term |
|---|---|---|
| Contact | | |
| Reading / Prep | | |
| Assignments | | |
| Assessment prep + completion | | |
| **Total** | | |

| Credit-hour standard (institutional) | Expected total hours | Computed total | Match (Yes/No) |
|---|---|---|---|

### Section 7: Accessibility & Inclusion Plan
- Materials format audit (per material: format, barriers, alternative provided)
- Alternative format paths
- UDL principles applied (engagement, representation, action/expression — with locations in the design)
- Prerequisite bridge plan (diagnostic + refresher path)
- Accommodations statement

### Section 8: Academic Integrity Plan
- Assessment design choices for integrity
- AI-use policy per assessment
- Integrity policy citation

### Section 9: Syllabus Components Checklist
- [ ] Course identity (code, title, credits, term, instructor, contact)
- [ ] Course description and rationale
- [ ] ILOs with PSLO mapping
- [ ] Required materials with accessibility notes
- [ ] Assessment plan with weights
- [ ] Module schedule
- [ ] Late work, attendance, integrity, communication policies
- [ ] Accommodations statement
- [ ] Accessibility statement

### Section 10: Design Audit

| Audit Question | Result | Notes / Remediation |
|---|---|---|
| 4-8 ILOs, observable, Bloom's-tagged | Pass / Fail | |
| Bidirectional ILO ↔ AT alignment (no orphans either way) | Pass / Fail | |
| Every ILO has TLA coverage | Pass / Fail | |
| Workload matches credit-hour standard | Pass / Fail | |
| Assessment weights honor cognitive levels and sum to 100% | Pass / Fail | |
| Prerequisite gaps identified and bridged | Pass / Fail | |
| Accessibility addressed for all materials | Pass / Fail | |
| Academic integrity addressed in assessment design | Pass / Fail | |
| Formative assessment in every module, feedback before related summative | Pass / Fail | |
| Course depth contribution to PSLOs honored | Pass / Fail | |

For each Fail: gap → fix → status (fixed / open item for user).

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Designing module activities before assessments | Reverses Biggs' principle; produces unaligned activities | Define ATs first; design TLAs to develop the abilities the ATs measure |
| Vague ILO verbs ("understand", "appreciate") | Unobservable; can't be assessed or audited | Use observable Bloom's verbs with context and criteria |
| Lectures as primary TLA | Lectures alone don't develop performance | Pair lectures with active processing; reserve lecture for content delivery within an active framework |
| Workload exceeds credit-hour standard | Students don't have the hours; quality work suffers | Compute workload and trim or rebalance |
| MCQ for Create-level ILOs | Assessment can't produce signal at that level | Match assessment format to ILO Bloom's level |
| Orphan assessments (AT maps to no ILO) | Grades measure something the course never promised | Every AT must map to ≥1 ILO; cut or re-anchor orphans |
| No formative assessment | Students only learn their status at summatives; too late | Weekly low-stakes checks with feedback before related summatives |
| Boilerplate accessibility statement only | Compliance theater, not actual accessibility | Audit materials format and provide alternative paths |
| Treating AI as just an integrity problem | AI is transforming the assessment landscape; design must adapt | Design AI-aware assessments (in-class, performance, process-evidenced) and state a per-AT AI stance |
| Generating ILOs the course can't produce | Aspirational ILOs damage trust and PSLO data | Match ILO scope to term length and contact hours |
| Inventing missing load-bearing inputs (PSLOs, credits) | The entire alignment chain becomes fiction | Ask for blocking inputs; assume-and-flag only minor ones |

## Verification Checklist

- [ ] Course identity complete; all assumptions flagged
- [ ] 4-8 ILOs aligned to PSLOs with specified depth, observable verbs
- [ ] Bidirectional ILO ↔ TLA ↔ AT linkages verified
- [ ] Workload matches credit-hour standard
- [ ] Module sequence with formative + summative assessment
- [ ] Prerequisite bridge included where gaps exist
- [ ] Accessibility plan addresses materials, format, UDL
- [ ] Academic integrity addressed in assessment design (not policy alone)
- [ ] Syllabus components complete
- [ ] Design audit completed honestly; remediation listed for any Fail
