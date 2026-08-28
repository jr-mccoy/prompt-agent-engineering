---
title: "Curriculum Map Builder (Course → Outcome → Standard → Assessment Matrix)"
category: education-teaching/program/curriculum-design
description: "Build an evidence-traceable program curriculum map linking courses or modules to program outcomes, external standards or competencies, and assessment evidence, with Introduced–Developed–Mastered depth coding, progression analysis, and gap, redundancy, and assessment-alignment audits."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - QA-01
  - QA-02
difficulty: "intermediate"
tags:
  - education
  - curriculum-design
  - curriculum-mapping
  - alignment
  - outcomes-assessment
  - standards-alignment
  - accreditation
  - k12
  - higher-ed
  - workforce
  - medical-education
updated: "2026-07-20"
related_prompts:
  - "../program-outcomes-assessment/teaching_program_outcomes_framework.md"
  - "../program-outcomes-assessment/teaching_outcomes_to_assessment_mapper.md"
  - "../program-outcomes-assessment/teaching_program_gap_analysis.md"
  - "teaching_standards_alignment_audit.md"
  - "teaching_vertical_alignment_auditor.md"
---

# Curriculum Map Builder

## Objective

Produce a complete, evidence-traceable program-level curriculum map that links every course, module, phase, rotation, grade band, or training segment in scope to:

1. the program outcomes it intentionally develops;
2. the external standards, competencies, or credential requirements it addresses; and
3. the assessments that generate evidence of learner achievement.

Code each defensible linkage by developmental depth—**Introduced (I), Developed (D), or Mastered (M)**—and distinguish evidence-supported mappings from provisional inferences. Then audit the map for gaps, weak progression, unsupported mastery claims, excessive redundancy, overloaded courses, orphan assessments, and outcomes that lack valid evidence.

The final product must be usable for curriculum design, faculty coordination, program review, continuous improvement, and accreditation documentation.

## When to Use

Use this prompt when:

- building the master curriculum map for a new program;
- documenting an existing curriculum for accreditation or program review;
- checking whether program outcomes are intentionally introduced, developed, and mastered;
- identifying standards or competencies that are missing, weakly represented, or excessively repeated;
- coordinating curriculum responsibilities across faculty, departments, clinical sites, grades, phases, or training units;
- linking assessments to program outcomes and standards;
- preparing evidence for curriculum committees, advisory boards, accrediting bodies, or continuous-improvement processes; or
- comparing the intended curriculum with the assessed curriculum.

Do not use this prompt as the primary tool for:

- writing or revising the program outcomes themselves; use `teaching_program_outcomes_framework.md`;
- conducting a detailed audit against one specific standards framework without building a full program map; use `teaching_standards_alignment_audit.md`;
- analyzing cross-grade or cross-year vertical progression as the sole task; use `teaching_vertical_alignment_auditor.md`; or
- designing individual assessments in detail; use an assessment-design or assessment-blueprint prompt.

## Sector Adaptation

Adapt terminology and evidence expectations to the sector selected by the user.

| Sector | Typical Curriculum Units | Typical Outcome Labels | Typical Standards or Competencies | Typical Assessment Evidence |
|---|---|---|---|---|
| K–12 | grade, course, unit, quarter, subject strand | standards-based outcomes, graduate profile competencies | state standards, CCSS, NGSS, AP, IB | common assessments, projects, performance tasks, exams, portfolios |
| Higher Education | course, module, semester, clinical, internship | PLO, PSLO, SLO, graduate attribute | disciplinary standards, licensure expectations, ABET, AACSB, CAEP, CCNE | exams, capstones, practica, portfolios, theses, direct-assessment rubrics |
| Workforce / CTE / Apprenticeship | course, training block, OJT phase, work process, credential module | occupational competencies, employability skills, program outcomes | O*NET, industry credentials, registered-apprenticeship work processes | demonstrations, skills checks, supervisor validation, credential exams, work products |
| Medical Education | course, block, clerkship, rotation, phase, residency experience | competencies, milestones, EPAs, program outcomes | ACGME, AAMC EPAs, specialty milestones, licensure expectations | OSCEs, simulation, workplace-based assessment, direct observation, exams, portfolios |

## Required Inputs

### Core Inputs

The following are required before a populated curriculum map can be produced:

1. **Sector**
   - K–12
   - Higher Education
   - Workforce / CTE / Apprenticeship
   - Medical Education
   - Other, specified by the user

2. **Program identity**
   - program name;
   - credential, grade span, degree, certificate, or training pathway;
   - map scope; and
   - version or academic year, if applicable.

3. **Curriculum-unit inventory**
   - course, module, phase, rotation, grade, or training-segment ID;
   - title;
   - sequence position;
   - brief description, syllabus excerpt, topic list, or official catalog description; and
   - prerequisite or progression relationship, if relevant.

4. **Program-outcome inventory**
   - official outcome ID;
   - full outcome statement; and
   - any approved performance indicators or subcompetencies.

### Conditional Inputs

These are required only when included in the requested map:

5. **External standards or competency framework**
   - official framework name and version;
   - native code for each standard or competency; and
   - official or user-supplied text.

6. **Assessment inventory**
   - assessment ID or name;
   - host course or curriculum unit;
   - assessment type;
   - outcomes or standards currently claimed;
   - scoring method or rubric, when available;
   - direct or indirect evidence classification; and
   - stakes or decision use, when known.

### Optional Inputs

- syllabi;
- course objectives;
- lesson or module outlines;
- assessment blueprints;
- rubrics;
- accreditation criteria;
- faculty mapping decisions;
- prior curriculum maps;
- learner progression data;
- program-review findings;
- modality or delivery-site information;
- credit hours or instructional time; and
- planned curriculum revisions.

## Missing-Input Protocol

Apply the following rules before mapping:

1. **Do not populate a curriculum map without the actual curriculum-unit list and program-outcome list.**
2. If either core list is missing, identify the missing input and request it.
3. A blank template may be supplied while waiting, but it must not contain invented mappings.
4. If standards are not supplied, omit the populated standards matrix and label it **Not in scope—standards list not supplied**.
5. If assessments are not supplied, create an assessment-inventory gap table rather than inventing assessments.
6. If descriptions, syllabi, or assessment evidence are incomplete, continue only with clearly labeled provisional mappings.
7. Never convert missing information into an assumed fact.

## Non-Negotiable Constraints

### Must

- Use the program’s official IDs whenever supplied.
- Produce a **Course × Outcome Matrix**.
- Produce a **Course × Standard Matrix** when standards are in scope.
- Produce a **Course × Assessment Evidence Matrix** when assessment information is available.
- Code every populated curriculum linkage as **I**, **D**, or **M**.
- Record the evidence basis for every populated linkage.
- Distinguish direct evidence from indirect evidence.
- Identify gaps, weak progression, unsupported mastery claims, and redundancy.
- Preserve the full wording of supplied outcomes and standards in reference tables.
- Maintain consistent IDs across every matrix, audit table, recommendation, and inference log.
- Separate verified facts from inferences and recommendations.
- Make every recommendation traceable to a specific finding.

### Must Not

- Invent courses, curriculum content, outcomes, standards, competencies, assessments, rubrics, or evidence.
- Infer detailed coverage solely from a course title.
- force a linkage unsupported by the supplied materials.
- treat a topic mention as evidence of intentional instruction.
- treat intentional instruction as evidence of assessed proficiency.
- code **M** without summative or consequential evidence of independent performance.
- equate frequent coverage with strong progression.
- count indirect measures alone as proof of mastery.
- hide conflicting evidence.
- silently change the wording, numbering, or meaning of official outcomes or standards.

## Core Mapping Model

Use a two-part code for each populated curriculum linkage:

1. **Depth Code**
   - I = Introduced
   - D = Developed
   - M = Mastered

2. **Evidence-Basis Code**
   - E1 = Direct documentary evidence
   - E2 = Corroborated evidence
   - INF = Inferred, pending verification

Recommended cell notation:

- `I-E1`
- `D-E1`
- `M-E1`
- `I-E2`
- `D-E2`
- `M-E2`
- `I-INF`
- `D-INF`

Do not use `M-INF`. Mastery may not be assigned solely by inference.

### Evidence-Basis Definitions

| Code | Meaning | Acceptable Basis |
|---|---|---|
| E1 | Direct documentary evidence | explicit syllabus objective, approved curriculum document, named assessment, rubric criterion, official mapping decision, or documented performance requirement |
| E2 | Corroborated evidence | multiple consistent sources support the linkage, but no single source explicitly states the full relationship |
| INF | Provisional inference | limited evidence suggests a likely linkage that must be verified by the user or responsible faculty |

## Depth-Coding Rules

### I — Introduced

Assign **I** only when the curriculum unit provides intentional initial instruction or structured exposure to the outcome, standard, or competency.

Typical indicators:

- the concept or skill is explicitly taught;
- foundational language, models, or procedures are introduced;
- learners receive guided examples or demonstrations;
- formative checks may occur;
- performance is highly scaffolded; and
- independent proficiency is not yet expected.

Do not assign **I** merely because a topic appears in a reading list, lecture title, catalog description, or incidental discussion.

### D — Developed

Assign **D** when learners repeatedly practice, apply, integrate, or refine the outcome with feedback and increasing independence.

Typical indicators:

- structured practice occurs across more than one task or context;
- feedback is provided;
- complexity or independence increases;
- both formative and summative assessment may be present;
- learners are expected to demonstrate partial or progressing proficiency; and
- the curriculum deliberately builds toward later independent performance.

### M — Mastered

Assign **M** only when the curriculum unit requires independent, summatively evaluated performance at the program’s expected exit, credential, promotion, or completion standard.

Required indicators:

- a named direct assessment evaluates the outcome or competency;
- the assessment requires independent or appropriately supervised performance;
- criteria or rubric elements are aligned to the outcome;
- the result contributes to a consequential decision, such as course completion, progression, graduation, certification, entrustment, or credentialing; and
- the expected performance level is consistent with program completion.

A course may reinforce an outcome after mastery, but reinforcement must not be mislabeled as a new mastery point unless the course independently assesses exit-level performance.

## Direct and Indirect Evidence Rules

Classify each assessment source as:

- **Direct evidence:** learner work or observed performance demonstrates the outcome.
- **Indirect evidence:** perceptions, self-report, satisfaction, completion, or proxy indicators suggest learning but do not directly demonstrate it.

Examples of direct evidence:

- performance task;
- exam items mapped to the outcome;
- OSCE or simulation;
- clinical or workplace observation;
- portfolio artifact scored with a rubric;
- capstone;
- demonstration;
- thesis or project defense;
- credential examination; or
- validated work product.

Examples of indirect evidence:

- course grades without outcome-level analysis;
- learner self-assessment;
- alumni survey;
- employer survey;
- attendance;
- course-completion rate; or
- satisfaction survey.

Indirect evidence may supplement a mastery claim but may not independently establish **M**.

## Workflow

### Phase 1: Scope and Input Validation

1. Identify the sector, program, credential or grade span, map purpose, and map boundary.
2. Confirm which curriculum units are included and excluded.
3. Confirm the official program-outcome list.
4. Confirm whether standards or external competencies are in scope.
5. Confirm whether assessment evidence is available.
6. Identify missing, conflicting, outdated, or duplicate inputs.
7. Create an **Input Readiness Table** before mapping.

#### Input Readiness Table

| Input Category | Status | Source Supplied | Usable for Mapping? | Action Needed |
|---|---|---|---|---|
| Program identity | Complete / Partial / Missing | | Yes / No | |
| Curriculum-unit list | Complete / Partial / Missing | | Yes / No | |
| Program outcomes | Complete / Partial / Missing | | Yes / No | |
| Standards or competencies | Complete / Partial / Not in scope | | Yes / No | |
| Assessment inventory | Complete / Partial / Missing | | Yes / No | |
| Syllabi or descriptions | Complete / Partial / Missing | | Yes / No | |

### Phase 2: Normalize the Source Inventories

Create four reference tables before building matrices.

#### A. Curriculum-Unit Inventory

| Unit ID | Unit Title | Sequence | Description Source | Prerequisites | Evidence Quality | Notes |
|---|---|---|---|---|---|---|

#### B. Program-Outcome Inventory

| Outcome ID | Full Official Outcome | Performance Indicators | Source | Notes |
|---|---|---|---|---|

#### C. Standards or Competency Inventory

| Standard ID | Full Official Text | Framework | Version | Source | Notes |
|---|---|---|---|---|---|

#### D. Assessment Inventory

| Assessment ID | Assessment Name | Host Unit | Type | Direct / Indirect | Scoring Method | Stakes | Source |
|---|---|---|---|---|---|---|---|

Normalization rules:

- retain official IDs and wording;
- create temporary IDs only when the user’s materials lack them;
- label temporary IDs as **working IDs**;
- do not merge distinct outcomes merely because they overlap;
- identify duplicates or near-duplicates for user review;
- preserve framework-native standard codes; and
- record source location when available.

### Phase 3: Establish Mapping Decisions

For each curriculum unit, determine:

1. Which program outcomes are intentionally addressed?
2. What evidence supports each linkage?
3. What depth is justified: I, D, or M?
4. Which standards or competencies are intentionally addressed?
5. Which assessments produce evidence for each linked outcome or standard?
6. Is the evidence direct or indirect?
7. Is the linkage evidence-based or inferred?

Use a **Mapping Decision Log** before or alongside the master matrices.

| Linkage ID | Unit ID | Target Type | Target ID | Depth | Evidence Basis | Source | Rationale | Verification Needed? |
|---|---|---|---|---|---|---|---|---|

Target Type must be one of:

- Program Outcome
- Standard
- Competency
- Assessment Evidence

### Phase 4: Build Matrix A — Curriculum Unit × Program Outcome

- Rows: curriculum units in sequence.
- Columns: official program outcomes.
- Cells: approved two-part mapping code, such as `I-E1`, `D-E2`, or `M-E1`.
- Blank cell: no defensible linkage.

Do not use a symbol in a cell unless the Mapping Decision Log contains the supporting record.

### Phase 5: Build Matrix B — Curriculum Unit × Standard or Competency

Build this matrix only when the user supplies the applicable standards or competency list.

- Rows: curriculum units.
- Columns: native standard or competency codes.
- Cells: depth plus evidence-basis code.
- Blank cell: no defensible linkage.

If the standards list is too large for one readable matrix:

1. provide a summary matrix by domain or strand;
2. provide detailed domain-specific matrices; and
3. preserve a complete standard-level audit table.

### Phase 6: Build Matrix C — Assessment Evidence Crosswalk

Every assessment record must show what it measures and what level of evidence it can support.

| Unit ID | Assessment ID | Assessment Name | Outcome IDs | Standard / Competency IDs | Direct / Indirect | Highest Defensible Depth | Scoring Evidence | Alignment Status |
|---|---|---|---|---|---|---|---|---|

Alignment Status must be one of:

- Aligned
- Partially Aligned
- Unaligned
- Insufficient Evidence
- Verification Required

Rules:

- an assessment may support more than one outcome only when the task and scoring criteria genuinely address each one;
- course grades alone do not establish outcome-level evidence;
- a claimed mastery assessment must include direct evidence and aligned scoring criteria;
- identify assessments that are present but not mapped to an outcome;
- identify outcomes that have no direct assessment evidence; and
- identify standards that are taught but never assessed when assessment is expected.

### Phase 7: Audit Outcome Progression

For every program outcome, calculate:

- number of I linkages;
- number of D linkages;
- number of M linkages;
- number of direct assessments;
- number of indirect assessments;
- sequence of first introduction, development, and mastery;
- whether mastery occurs at an appropriate point in the program; and
- whether evidence quality is sufficient.

#### Outcome Status Rules

| Status | Rule |
|---|---|
| Gap | No I, D, or M linkage |
| Introduced Only | One or more I linkages, no D or M |
| Developed but Not Mastered | One or more D linkages, no M |
| Unsupported Mastery | M is claimed without adequate direct assessment evidence |
| Late Introduction | First intentional introduction occurs too near the expected mastery point |
| Progression Break | I and M are present, but no meaningful D phase exists |
| Redundant Development | Four or more D linkages with no M linkage, unless the program provides a documented rationale |
| Fragile Mastery | Exactly one M point with limited evidence or no earlier development |
| Strong Progression | At least one defensible I, one defensible D, and one evidence-supported M in a logical sequence |
| Sustained Mastery | Evidence-supported mastery is demonstrated and later reinforced or reassessed appropriately |

Do not apply numeric thresholds mechanically when program structure provides a valid reason. Note justified exceptions.

### Phase 8: Audit Standards or Competency Coverage

For every supplied standard or competency, calculate:

- I, D, and M counts;
- number of direct assessments;
- courses or units responsible for coverage;
- earliest and latest mapped point;
- evidence quality; and
- coverage status.

Use the same status categories when applicable, but distinguish:

- **Program outcome mastery**, which normally requires program-level evidence; and
- **standard coverage**, which may require instruction, assessment, or mastery depending on the framework.

Do not assume every external standard requires an M-level designation. Use the framework’s expectations when supplied.

### Phase 9: Audit Curriculum Units

For every curriculum unit, calculate:

- number of outcomes touched at I, D, and M;
- number of standards or competencies touched;
- number of assessments;
- number of mastery claims;
- number of inferred linkages;
- evidence density; and
- potential overload or underalignment.

#### Course or Unit Status Rules

| Status | Indicative Rule | Interpretation |
|---|---|---|
| Unmapped | No defensible outcome linkage | Unit may be outside program purpose or documentation is missing |
| Thin | Only one minor or introductory linkage and no clear role in progression | Reassess necessity, documentation, or integration |
| Right-Sized | Coherent set of linkages supported by instruction and assessment | Maintain, with routine review |
| Over-Stretched | More than eight meaningful outcome linkages, numerous standards, or multiple unsupported mastery claims | Scope may exceed realistic instructional and assessment capacity |
| Assessment-Heavy | Many assessments with unclear distinct purposes or repeated evidence claims | Consolidate or clarify assessment roles |
| Inference-Heavy | A substantial proportion of mappings are INF | Obtain stronger documentation before relying on the map |

Treat the “more than eight outcomes” threshold as a review trigger, not an automatic defect.

### Phase 10: Audit Assessment Alignment

Identify:

- **orphan assessments:** assessments linked to no program outcome;
- **unevidenced outcomes:** outcomes with no assessment evidence;
- **indirect-only outcomes:** outcomes supported only by indirect evidence;
- **unsupported mastery claims:** M cells lacking a valid direct assessment;
- **overloaded assessments:** one assessment claimed as evidence for too many outcomes without corresponding rubric dimensions;
- **duplicative assessments:** repeated assessments generating equivalent evidence without a clear progression purpose;
- **misplaced assessments:** assessments occurring before adequate development; and
- **scoring gaps:** tasks appear aligned, but the rubric or scoring method does not measure the claimed outcome.

### Phase 11: Generate Findings and Recommendations

Every recommendation must include:

1. the finding it addresses;
2. the specific outcome, standard, unit, or assessment involved;
3. the evidence supporting the finding;
4. the proposed action;
5. the suggested host course or curriculum unit, when appropriate;
6. the target depth or evidence level;
7. the rationale;
8. the priority; and
9. any verification or governance step required.

Do not recommend adding content automatically. Consider whether the better action is to:

- add instruction;
- add practice;
- add or strengthen assessment;
- move a learning experience earlier or later;
- consolidate duplicate coverage;
- clarify documentation;
- revise an outcome;
- revise a rubric;
- designate a responsible course or unit;
- remove an unsupported claim; or
- collect missing evidence.

## Analysis Heuristics

Use these as diagnostic prompts, not rigid rules.

### Progression Heuristics

- Does every mastery point have adequate prior development?
- Is an outcome introduced early enough to permit deliberate practice?
- Are there long gaps between development and mastery?
- Is mastery assessed more than once when the outcome is high stakes?
- Does complexity increase across the sequence?
- Are later courses genuinely advancing performance, or merely repeating the same level?

### Redundancy Heuristics

- Is the same outcome taught repeatedly at I level?
- Are multiple courses claiming the same D-level role without differentiated complexity?
- Are several assessments producing essentially the same evidence?
- Could repeated low-level coverage be consolidated to create room for deeper practice?
- Is redundancy intentional for safety, licensure, retrieval practice, spiral learning, or distributed practice?

### Evidence Heuristics

- Is the outcome visible in the assessment task?
- Is it visible in the scoring criteria?
- Does the assessment require the claimed level of independence?
- Does the evidence support the whole outcome or only one component?
- Is the assessment direct, indirect, or a mixture?
- Can an accreditor or reviewer trace the claim to a source?

### Equity and Accessibility Review

When relevant inputs are supplied, note whether:

- critical outcomes are assessed through only one modality;
- learners have multiple appropriate opportunities to demonstrate competence;
- accessibility accommodations preserve the construct being assessed;
- site, instructor, modality, or placement differences create unequal access to mastery opportunities; and
- hidden prerequisites or assumed prior knowledge disrupt progression.

Do not infer inequity without evidence. Label concerns as questions for review when documentation is insufficient.

## Output Format

Use the following sections in order.

### Section 1: Map Identity and Scope

Include:

- program name;
- sector;
- credential, grade span, or training pathway;
- map purpose;
- academic year or version;
- curriculum units in scope;
- outcomes in scope;
- standards or competency frameworks in scope;
- assessment-inventory status;
- source materials used; and
- known limitations.

### Section 2: Input Readiness and Source Quality

Provide the Input Readiness Table and summarize material limitations.

### Section 3: Normalized Reference Inventories

Provide:

1. Curriculum-Unit Inventory
2. Program-Outcome Inventory
3. Standards or Competency Inventory, when applicable
4. Assessment Inventory, when available

### Section 4: Coding Legend and Decision Rules

State:

- I, D, and M definitions;
- E1, E2, and INF definitions;
- direct and indirect evidence definitions;
- any sector-specific adaptations; and
- any user-approved exceptions.

### Section 5: Matrix A — Curriculum Unit × Program Outcome

| Curriculum Unit | PSLO-1 | PSLO-2 | PSLO-3 | … |
|---|---|---|---|---|
| Unit 1 | I-E1 | D-E1 |  |  |
| Unit 2 | D-E2 | D-E1 | I-INF |  |
| Unit 3 | M-E1 |  | D-E1 |  |

### Section 6: Matrix B — Curriculum Unit × Standard or Competency

Use the same structure with native standard or competency codes in the columns.

When standards are not in scope, state:

> Not in scope—no standards or competency list was supplied.

### Section 7: Matrix C — Assessment Evidence Crosswalk

| Unit ID | Assessment ID | Assessment Name | Outcome IDs | Standard / Competency IDs | Direct / Indirect | Highest Defensible Depth | Scoring Evidence | Alignment Status |
|---|---|---|---|---|---|---|---|---|

### Section 8: Mapping Decision Log

| Linkage ID | Unit ID | Target Type | Target ID | Depth | Evidence Basis | Source | Rationale | Verification Needed? |
|---|---|---|---|---|---|---|---|---|

### Section 9: Column-Wise Audit — Program Outcomes

| Outcome ID | I Count | D Count | M Count | Direct Assessments | Indirect Assessments | First Touch | Mastery Point | Status | Recommendation |
|---|---:|---:|---:|---:|---:|---|---|---|---|

### Section 10: Column-Wise Audit — Standards or Competencies

| Standard ID | I Count | D Count | M Count | Direct Assessments | Units Responsible | Status | Recommendation |
|---|---:|---:|---:|---:|---|---|---|

When standards are not in scope, state that explicitly.

### Section 11: Row-Wise Audit — Curriculum Units

| Unit ID | I Count | D Count | M Count | Outcomes Touched | Standards Touched | Assessments | Inferred Linkages | Status | Recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|

### Section 12: Assessment-Alignment Audit

| Finding Type | Assessment or Outcome | Host Unit | Evidence | Risk | Recommended Action | Priority |
|---|---|---|---|---|---|---|

### Section 13: Progression Findings

Organize findings under:

- strong progressions;
- gaps;
- introduced-only outcomes or standards;
- developed-but-not-mastered outcomes;
- unsupported mastery claims;
- progression breaks;
- fragile mastery points;
- late introductions;
- intentional spiraling; and
- questionable redundancy.

### Section 14: Recommendations and Action Plan

| Priority | Finding | Recommended Action | Responsible Role or Group | Target Unit | Target Depth or Evidence | Dependencies | Verification Method |
|---|---|---|---|---|---|---|---|

Use priority labels:

- Critical
- High
- Moderate
- Low

### Section 15: Inference and Verification Log

Include every `INF` linkage.

| Linkage ID | Provisional Mapping | Reason for Inference | Missing Evidence | Verification Owner | Verification Question |
|---|---|---|---|---|---|

### Section 16: Executive Summary

Summarize:

- overall map completeness;
- strongest areas;
- most consequential gaps;
- outcomes lacking mastery evidence;
- assessment-alignment risks;
- major redundancy concerns;
- number of inferred linkages requiring verification; and
- highest-priority actions.

Do not present inferred linkages as settled findings.

## Recommendation Standards

Recommendations must be:

- specific;
- evidence-linked;
- feasible within the mapped program structure;
- sector appropriate;
- explicit about whether the change concerns instruction, practice, assessment, documentation, or sequencing;
- cautious about adding new curriculum requirements;
- clear about verification needs; and
- written so a curriculum committee can act on them.

Weak recommendation:

> Improve coverage of PSLO-3.

Strong recommendation:

> Add a D-level, rubric-scored application task for PSLO-3 in `NURS-320` before the existing M-level capstone assessment in `NURS-490`. Current evidence shows an I-level introduction in `NURS-210` and a mastery claim in `NURS-490`, but no documented opportunity for guided practice with feedback.

## False-Positive Prevention

| Common Mistake | Why It Is Wrong | Required Correction |
|---|---|---|
| Treating a syllabus mention as mastery | Mention does not demonstrate independent performance | Code M only when a named direct assessment and aligned scoring evidence support mastery |
| Coding every course at M for every outcome it touches | Inflates coverage and hides the actual developmental sequence | Use I–D–M according to the learning and assessment role of each unit |
| Inferring content from course titles | Titles are too broad or misleading to establish intentional coverage | Use descriptions, objectives, syllabi, assessments, or faculty-verified decisions |
| Treating a topic mention as introduction | Incidental exposure is not intentional instruction | Require evidence of planned teaching or guided learning activity |
| Treating frequent coverage as strong coverage | Repetition may remain shallow and never reach independent performance | Analyze depth, sequence, assessment, and complexity—not frequency alone |
| Assigning M from indirect evidence | Perceptions and course grades do not directly demonstrate the outcome | Require direct learner-performance evidence |
| Mapping standards that were not supplied | Standards codes and wording must be authoritative | Request the official list or omit the populated standards matrix |
| Inventing assessments to complete the map | Fabricated evidence undermines accreditation credibility | Mark the assessment gap and recommend evidence collection or assessment design |
| Linking one assessment to many outcomes without rubric support | Broad claims may exceed what the task actually measures | Verify distinct task and scoring components for each claimed outcome |
| Ignoring sequencing | A map can appear complete while expecting mastery before adequate practice | Audit the order of I, D, and M across the program |
| Treating all redundancy as waste | Some repetition is intentional and educationally necessary | Distinguish deliberate spiraling, safety reinforcement, and distributed practice from accidental duplication |
| Hiding inferred mappings | Unmarked inference creates false certainty | Use INF and include every inferred linkage in the verification log |
| Changing official wording for convenience | Paraphrase can alter scope and accreditation meaning | Preserve official outcome and standard wording in reference tables |

## Quality-Control Checklist

### Inputs and Scope

- [ ] Program identity and map purpose are stated.
- [ ] Curriculum-unit list is complete or limitations are explicit.
- [ ] Official program outcomes are supplied and preserved verbatim.
- [ ] Standards or competency framework is identified by name and version when in scope.
- [ ] Assessment inventory status is explicit.
- [ ] Missing inputs are not replaced with inventions.

### Mapping Integrity

- [ ] Every populated matrix cell has a corresponding Mapping Decision Log entry.
- [ ] Every populated linkage includes both a depth code and evidence-basis code.
- [ ] No `M-INF` code is used.
- [ ] Every M claim has a named direct assessment.
- [ ] Every M claim has aligned scoring or rubric evidence, or is flagged as unsupported.
- [ ] Official IDs are used consistently.
- [ ] Blank cells represent no defensible linkage, not missing analysis.

### Matrix Completion

- [ ] Matrix A—Curriculum Unit × Program Outcome—is complete.
- [ ] Matrix B—Curriculum Unit × Standard or Competency—is complete when standards are in scope.
- [ ] Matrix C—Assessment Evidence Crosswalk—is complete when assessment data are available.
- [ ] Large standards frameworks are divided into readable domain-level matrices without losing standard-level detail.

### Audit Completion

- [ ] Every program outcome appears in the column-wise audit.
- [ ] Every supplied standard or competency appears in the standards audit.
- [ ] Every curriculum unit appears in the row-wise audit.
- [ ] Gaps are identified.
- [ ] Introduced-only and developed-but-not-mastered items are identified.
- [ ] Unsupported mastery claims are identified.
- [ ] Progression breaks and late introductions are identified.
- [ ] Redundancy is analyzed for intent before being labeled wasteful.
- [ ] Orphan assessments and unevidenced outcomes are identified.
- [ ] Indirect-only evidence is distinguished from direct evidence.

### Recommendations and Traceability

- [ ] Every recommendation cites a specific mapped finding.
- [ ] Recommendations identify the target unit and intended depth or evidence change when applicable.
- [ ] Recommendations distinguish curriculum changes from documentation fixes.
- [ ] Recommendations are prioritized.
- [ ] All inferred mappings appear in the Inference and Verification Log.
- [ ] The executive summary does not overstate provisional findings.

## Final Instruction

Create the most complete map justified by the supplied evidence. Prefer an explicit blank, limitation, or verification flag over a speculative linkage. The purpose is not to make the curriculum appear fully aligned; the purpose is to produce an accurate, auditable representation of where outcomes and standards are intentionally taught, developed, assessed, and demonstrated.
