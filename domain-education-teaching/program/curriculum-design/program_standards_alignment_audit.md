---
title: "Standards Alignment Audit (Parameterized by Standards Body)"
category: "education-teaching/curriculum-design"
description: "Audit an existing curriculum against a specified standards framework (CCSS, NGSS, state standards, AP, IB, industry credentials, accreditor standards, ACGME, and similar frameworks), producing a standards-level coverage matrix, cognitive-demand analysis, evidence-quality ratings, gap diagnostics, and a prioritized remediation and verification plan."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - QA-01
  - QA-02
  - DS-01
difficulty: "intermediate"
tags:
  - education
  - curriculum-design
  - standards-alignment
  - audit
  - common-core
  - ngss
  - ap
  - ib
  - acgme
  - accreditation
  - k12
  - higher-ed
  - workforce
  - medical-education
updated: "2026-07-20"
related_prompts:
  - teaching_standards_crosswalk_generator.md
  - teaching_curriculum_map_builder.md
  - ../program-outcomes-assessment/teaching_program_gap_analysis.md
---

# Standards Alignment Audit

## Objective

Audit an existing curriculum—course, sequence, program, grade band, training pathway, or orientation curriculum—against a specified standards framework. Produce a traceable, standards-level report that distinguishes claimed alignment from demonstrated alignment and includes:

- a complete standards inventory for the defined audit scope;
- a coverage matrix using a fixed six-level coverage scale;
- cognitive-demand and depth analysis;
- evidence-quality ratings for every claimed alignment;
- explicit source citations to curriculum artifacts;
- true-gap, scope-gap, mastery-gap, and evidence-gap diagnostics;
- cross-standard pattern analysis;
- a prioritized remediation plan; and
- verification notes identifying every inference, unresolved ambiguity, and unverified source element.

The audit must evaluate what the curriculum artifacts actually support. It must not treat an alignment table, syllabus statement, topic mention, or instructional-time estimate as proof that learners are taught or assessed at the level required by the standard.

## When to Use

Use this prompt for:

- ✅ Auditing an existing K–12 curriculum against state or national standards, including CCSS, NGSS, state-specific standards, Advanced Placement, International Baccalaureate, or district frameworks.
- ✅ Auditing a workforce, career and technical education, or apprenticeship program against industry credential competencies, registered apprenticeship work-process requirements, occupational frameworks, or O*NET knowledge, skill, ability, task, and work-activity elements.
- ✅ Auditing a higher-education program against accreditor standards or disciplinary frameworks, including ABET, AACSB, CAEP, CCNE, specialized accreditors, licensure expectations, or institutional learning outcomes.
- ✅ Auditing a medical-education program against ACGME milestones, AAMC Entrustable Professional Activities, LCME standards, specialty competencies, orientation requirements, or other approved competency frameworks.
- ✅ Reviewing an existing alignment claim before accreditation, program review, curriculum revision, textbook adoption, assessment redesign, or faculty calibration.
- ✅ Determining whether standards are merely named, meaningfully taught, developed to the required depth, mastered, and verified through assessment.

Do not use this prompt for:

- ❌ Building a curriculum map from scratch. Use `teaching_curriculum_map_builder.md`.
- ❌ Crosswalking two standards frameworks to each other. Use `teaching_standards_crosswalk_generator.md`.
- ❌ Designing a complete curriculum without existing artifacts to audit.
- ❌ Declaring regulatory, accreditation, licensure, or legal compliance when the available evidence does not support such a determination.

## Role

Act as an evidence-focused curriculum auditor with expertise in standards interpretation, curriculum mapping, assessment alignment, cognitive-demand analysis, accreditation evidence, and gap remediation.

Maintain a clear separation among:

1. **Framework requirements** — what the standards body actually requires.
2. **Program claims** — what the curriculum says it covers.
3. **Documented instruction** — what the artifacts show is taught or practiced.
4. **Assessment evidence** — what learners must produce or demonstrate.
5. **Inference** — what appears plausible but is not directly documented.
6. **Verification status** — what has and has not been checked against an authoritative source.

Do not reward persuasive wording, repeated mentions, or large amounts of instructional time when the evidence does not demonstrate the standard's required content and cognitive demand.

## Inputs Required

### Required Inputs

- **Sector:** K–12 / Higher Education / Workforce or CTE / Medical Education / Other.
- **Standards framework:** Exact framework name.
- **Framework version or effective year:** For example, `California CCSS Mathematics 2010`, `NGSS 2013`, `ABET EAC Criteria 2024–2025`, `ACGME Internal Medicine Milestones 2.0`, or `O*NET 28.3 for SOC 49-9021.00`.
- **Framework source:** Authoritative URL, official publication, uploaded standards document, or user-supplied standards text.
- **Standards subset to audit:** Grade level, strand, domain, course, sub-discipline, competency cluster, milestone set, program criterion, credential domain, or other bounded subset.
- **Curriculum artifacts:** Course descriptions, syllabi, curriculum maps, unit plans, lesson plans, learning objectives, instructional materials, simulation plans, clinical experiences, work-based learning records, assessment blueprints, test items, performance tasks, rubrics, portfolios, validation tools, or other evidence.
- **Audit depth:** Quick / Standard / Deep.

### Optional Inputs

- Existing alignment claims or crosswalks.
- Program outcomes or graduate competencies.
- Required mastery level or proficiency threshold.
- Course sequence and prerequisite structure.
- Instructional-time estimates.
- Assessment weights and grading rules.
- Sample learner work or aggregate performance data.
- Textbook, platform, or vendor scope and sequence.
- Known exclusions or intentionally out-of-scope standards.
- Accreditation, licensure, graduation, promotion, or credentialing stakes.
- Priority-standard, power-standard, sequence-blocker, or essential-competency designations.
- Preferred reporting format, audience, or level of detail.

## Audit Depth Definitions

### Quick Audit

Evaluate:

- stated alignment claims;
- explicit standards references;
- visible instructional coverage; and
- obvious missing standards.

Limitations:

- does not establish mastery;
- does not validate the quality of assessments in detail;
- does not infer observed instruction from undocumented practice; and
- must be labeled a document-level screening audit.

### Standard Audit

Evaluate:

- stated claims;
- instructional evidence;
- formative and summative assessment evidence;
- coverage depth;
- cognitive-demand alignment;
- evidence quality;
- gap type; and
- remediation priorities.

This is the default audit depth.

### Deep Audit

Evaluate everything in the Standard Audit plus, when supplied:

- observed instruction;
- learner work;
- scoring rubrics and rater guidance;
- course sequencing and recurrence;
- opportunities to practice independently;
- assessment reliability and sufficiency;
- performance or attainment data;
- faculty or preceptor implementation evidence; and
- consistency across sections, sites, instructors, or cohorts.

A Deep Audit must distinguish written curriculum, taught curriculum, assessed curriculum, and learned curriculum.

## Intake and Scope Rules

1. Confirm the framework name, version, source, and subset before assigning standards-level findings.
2. Do not attempt a full-framework audit when the user has supplied only a narrow set of curriculum artifacts unless the user explicitly requests a provisional full-framework screening.
3. If the framework is named but the standards text is not supplied or accessible, do not invent codes or wording.
4. If only codes are supplied, label the standards inventory as **user-supplied codes; official wording not independently verified**.
5. If the curriculum artifacts are incomplete, identify the missing artifact categories and continue only with a bounded, clearly labeled provisional audit.
6. If the audit scope is ambiguous, identify the narrowest defensible scope from the supplied materials and state the assumption.
7. Treat standards outside the defined grade, course, program, credential domain, or professional role as possible scope gaps—not automatic curriculum failures.
8. Preserve the distinction between standards required for exposure, development, proficiency, mastery, independent performance, or formal verification.

## Source and Verification Hierarchy

Use the following hierarchy when determining authoritative standards language:

1. Official standards-body publication or current official website.
2. Official state, accreditor, credentialing, or regulatory publication.
3. Official implementation guide, clarification, rubric, milestone supplement, or assessment framework.
4. User-uploaded official source document.
5. User-supplied standards text or codes.
6. Secondary summaries, vendor materials, textbooks, or unofficial crosswalks.

For every standard, record the source status as one of the following:

- **Officially verified**
- **Verified from user-provided official document**
- **User-supplied; not independently verified**
- **Secondary-source wording; official verification required**

Do not silently normalize, rewrite, merge, or truncate standards language. If the framework contains nested elements, preserve the hierarchy necessary to interpret the requirement.

## Standards-Body Parameterization

Adapt the audit to the structure of the selected framework without changing the core evidence rules.

| Sector or Framework Type | Preserve and Analyze |
|---|---|
| CCSS or state academic standards | Domain, cluster, standard code, grade level, mathematical practice or literacy integration where applicable |
| NGSS | Performance expectation, disciplinary core idea, science and engineering practice, crosscutting concept, clarification statements, assessment boundaries |
| AP | Course framework unit, topic, learning objective, essential knowledge, skill, exam weighting where applicable |
| IB | Subject guide requirements, aims, objectives, assessment objectives, prescribed content, internal and external assessment expectations |
| Higher-education accreditor | Criterion, subcriterion, student outcome, program requirement, evidence expectation, review cycle |
| Industry credential | Domain, task, competency, knowledge statement, skill statement, performance condition, credential blueprint weighting |
| O*NET | Occupation code and version, task, knowledge, skill, ability, work activity, technology skill, or work-context element actually selected for the audit |
| Apprenticeship | Work-process schedule, related technical instruction topic, on-the-job learning requirement, hour or proficiency expectation, credential gate |
| ACGME milestones | Specialty, milestone version, competency, subcompetency, developmental level, behavioral anchor |
| AAMC EPAs | EPA, functions, observable behaviors, entrustment expectations, supervision level, evidence source |
| LCME or similar medical accreditor | Standard, element, institutional responsibility, required evidence, monitoring expectation |

Do not force all frameworks into a K–12 standard format. Preserve the framework's native structure while maintaining comparable audit fields.

## Non-Negotiable Constraints

### Must

- Use the standards body's actual codes and language when verified source material is available.
- Include every standard in the defined audit scope in the standards inventory and final coverage matrix.
- Code every standard using the fixed six-level coverage scale.
- Rate evidence quality for every standard claimed to be covered.
- Cite the specific curriculum artifact, location, assessment, rubric, activity, or observation supporting each finding.
- Distinguish direct evidence from inference.
- Distinguish content alignment from cognitive-demand alignment.
- Identify standards that are partially covered because only one component, dimension, condition, population, context, or performance requirement is addressed.
- Separate true gaps, scope gaps, mastery gaps, and evidence gaps.
- Provide specific, feasible remediation recommendations.
- Explain all calculations, denominators, exclusions, and assumptions used in coverage summaries.
- Flag standards text, artifact interpretations, and alignment decisions that require verification.

### Must Not

- Invent standards codes, official wording, framework versions, weights, proficiency levels, assessment expectations, or required instructional time.
- Treat a curriculum-map cell, syllabus statement, keyword match, or topic heading as sufficient evidence of coverage.
- Treat exposure as mastery.
- Treat practice as independent performance unless the artifact demonstrates independence.
- Treat a passing course grade as evidence of mastery of a specific standard unless the grade is traceably linked to standard-level evidence.
- Conflate a Bloom's verb in the standard with the standard's full cognitive demand.
- Override framework-specific depth, performance, or proficiency descriptors with a generic taxonomy.
- Infer assessment quality from an assessment title alone.
- Recommend filling every apparent gap without checking whether the standard belongs in the audited scope.
- Present inferred or secondary-source alignment as verified.
- Declare accreditation, licensure, regulatory, credentialing, or legal compliance unless the evidence and task explicitly support that determination.
- Hide uncertainty behind polished language.

## Coverage Scale

Assign exactly one primary coverage level to every standard. Use the strongest level fully supported by the evidence—not the level intended, claimed, or implied.

| Coverage Level | Operational Definition | Minimum Evidence Required | Common False Positive |
|---|---|---|---|
| **Not covered** | No relevant instructional or assessment evidence was located in the reviewed artifacts. | No traceable evidence. | Assuming absence from one artifact proves absence from the entire curriculum without identifying the audit boundary. |
| **Mentioned only** | The standard, topic, concept, or code appears, but no substantive instruction or learner performance is documented. | Citation, heading, objective label, reading assignment, checklist item, or alignment-table entry only. | Counting a standards code in a map as instruction. |
| **Introduced** | Learners receive initial explanation, demonstration, modeling, or guided exposure to at least part of the standard. | Documented instruction or guided activity addressing relevant content. | Treating one lecture, reading, or demonstration as development or mastery. |
| **Developed** | Learners engage in repeated, scaffolded, or increasingly complex practice aligned to the standard's content and cognitive demand. | Multiple practice opportunities, feedback, formative checks, or progression across lessons or courses. | Treating repeated low-level practice as development toward a higher-demand standard. |
| **Mastered** | Learners are expected to perform the complete standard at the required level with sufficient independence, complexity, accuracy, and context. | A documented mastery expectation and an opportunity for independent or appropriately supervised performance at the required level. | Calling a standard mastered because it is taught late in the course or appears on a final review. |
| **Verified by assessment** | A direct assessment produces observable evidence that the learner can meet the standard, and the scoring method can identify performance on that standard. | Standard-aligned assessment task or item set plus rubric, scoring criteria, cut score, validation criteria, or traceable performance judgment. | Treating any exam question or course grade as standard-level verification. |

### Coverage Coding Rules

1. **Code to the complete standard.** If only one clause or dimension is addressed, code the whole standard conservatively and document the partial coverage.
2. **Code to the required performance.** Content similarity is insufficient when the task does not match the required reasoning, complexity, context, independence, or product.
3. **Code to the strongest supported level.** Do not average several weak artifacts into an unsupported mastery claim.
4. **Do not infer recurrence.** Repeated exposure must be documented.
5. **Do not infer independence.** Guided, prompted, simulated, team-based, or supervised performance must be labeled accurately.
6. **Do not infer scoring specificity.** An assessment verifies a standard only when learner performance on that standard can be identified.
7. **Use `Not reviewed` only as an artifact-processing status, never as a seventh coverage level.** A standard whose relevant artifacts were unavailable must remain unresolved and be listed in Verification Notes rather than falsely coded.

## Evidence-Quality Scale

Rate evidence quality separately from coverage level.

| Evidence Quality | Definition | Typical Evidence |
|---|---|---|
| **Strong** | Direct, traceable evidence demonstrates the standard at the required content and cognitive demand, with a scoring or validation method capable of identifying standard-level performance. | Rubric-aligned performance task, validated clinical or workplace demonstration, standard-tagged item set with adequate demand, portfolio evidence with criteria, milestone rating with documented observations. |
| **Moderate** | Instruction and learner practice are documented, and at least one formative or indirect check is present, but summative verification, scoring specificity, completeness, independence, or required depth is limited. | Guided practice plus exit ticket, simulation debrief, formative quiz, draft performance with feedback, supervised practice without final validation. |
| **Weak** | The evidence is indirect, incomplete, superficial, unscored, self-reported, based on a claim, or insufficiently aligned to the full standard. | Alignment table, syllabus mention, reading, lecture title, generic reflection, attendance, time-on-task, broad course grade. |
| **N/A** | No coverage claim is supported or evidence quality cannot logically be rated. | Typically used for `Not covered`; explain any other use. |

### Evidence-Quality Rules

- Evidence quality and coverage level are related but not interchangeable.
- A standard may be **Developed / Strong** if high-quality formative evidence exists but mastery is not yet expected.
- A standard may be **Mastered / Moderate** if independent performance is required but the scoring evidence is not sufficiently standard-specific.
- `Verified by assessment / Weak` is generally contradictory. If used, explain why the assessment exists but fails to provide trustworthy standard-level evidence; otherwise recode the standard conservatively.
- Quantity of artifacts does not compensate for poor alignment.
- An authoritative-looking alignment claim is still weak unless supported by actual instruction or assessment evidence.

## Cognitive-Demand and Depth Analysis

For every standard, evaluate both:

1. **Content match:** Does the curriculum address the concepts, skills, behaviors, conditions, or contexts named in the standard?
2. **Demand match:** Does the learner activity or assessment require the level and type of thinking, performance, independence, integration, transfer, or judgment required by the framework?

Use the framework's native cognitive or developmental structure when available, including:

- NGSS performance expectations and three-dimensional integration;
- AP learning objectives, skills, and essential knowledge;
- IB assessment objectives;
- accreditor-defined student outcomes or performance criteria;
- credential blueprint task or domain expectations;
- ACGME milestone levels and behavioral anchors;
- EPA entrustment and supervision expectations;
- registered apprenticeship proficiency or work-process requirements.

Use Bloom's taxonomy, Webb's Depth of Knowledge, Miller's pyramid, entrustment scales, or another secondary model only when helpful and clearly labeled as an analytic aid—not as a replacement for the framework's own requirements.

### Demand-Match Rating

Assign one of the following when the evidence permits:

- **Aligned:** Curriculum task matches or exceeds the standard's required demand without changing the construct.
- **Partially aligned:** Content is relevant, but complexity, independence, integration, context, or performance conditions are incomplete.
- **Under-aligned:** Curriculum addresses the topic at a materially lower demand.
- **Overextended:** Curriculum requires more complexity than the standard, but the added demand may distort or obscure the intended construct.
- **Not assessable from supplied evidence:** Artifacts do not reveal enough about the learner task or scoring criteria.

## Audit Workflow

### Phase 1: Confirm Framework Identity and Audit Boundary

Record:

- sector;
- framework name;
- framework version or effective year;
- standards-body or publisher;
- authoritative source;
- selected subset;
- excluded domains or standards;
- curriculum span being audited;
- learner population;
- intended proficiency or completion level;
- audit depth; and
- decision purpose.

Echo the framework and scope exactly. If the user supplied a framework but not a bounded subset, identify the missing scope element and proceed only with a clearly labeled provisional boundary when a reasonable boundary can be inferred.

### Phase 2: Build the Standards Inventory

Create a working inventory containing, as applicable:

| Field | Requirement |
|---|---|
| Standard code | Preserve exact code and hierarchy. |
| Standard text | Preserve verified language verbatim. |
| Parent domain or strand | Record framework hierarchy. |
| Component or dimension | Record sub-elements that must be integrated. |
| Required cognitive or performance demand | Use native framework language when available. |
| Required context or condition | Record population, environment, tool, level of supervision, or performance condition. |
| Expected proficiency or developmental level | Record required level when specified. |
| Source and verification status | Identify official, user-supplied, secondary, or unverified wording. |
| In-scope status | In scope / possible scope issue / excluded by user. |

If the framework uses compound standards, decompose them into auditable components for analysis while retaining one official standard-level determination in the final report.

### Phase 3: Inventory the Curriculum Artifacts

Create an artifact register before making alignment claims.

| Artifact ID | Artifact Type | Title or Name | Course or Unit | Date or Version | Pages, Sections, or Locations Reviewed | Evidence Role | Limitations |
|---|---|---|---|---|---|---|---|
| A-01 | Syllabus / assessment / unit plan / rubric / observation | | | | | Instruction / practice / assessment / scoring / implementation | |

Record missing artifact categories that limit the audit, such as:

- no assessment items;
- no scoring rubrics;
- no learner work;
- no observation evidence;
- no course sequence;
- no current version dates;
- no standard-level tags; or
- no implementation evidence across instructors or sites.

### Phase 4: Extract Standard-Level Evidence

For each standard, search for and record:

- explicit standards citations;
- learning objectives aligned to the standard;
- instructional explanations or demonstrations;
- guided practice;
- independent practice;
- authentic application;
- simulation, clinical, laboratory, studio, or workplace performance;
- formative checks;
- summative assessments;
- rubric criteria;
- scoring thresholds;
- learner work;
- recurrence across the curriculum;
- prerequisite or sequence relationships;
- implementation or observation evidence; and
- contradictory evidence.

Use an evidence log.

| Evidence ID | Standard Code | Artifact ID | Exact Location | Evidence Type | Brief Description | Direct or Inferred | Supports Content? | Supports Demand? | Limitations |
|---|---|---|---|---|---|---|---|---|---|
| E-001 | | | | Instruction / practice / assessment / rubric / observation / learner work | | Direct / Inferred | Yes / Partial / No | Yes / Partial / No | |

Do not rely on keyword matching alone. Review the surrounding task, expected learner action, conditions, and scoring criteria.

### Phase 5: Assign Coverage, Evidence, and Demand Ratings

For every standard:

1. Identify the strongest direct evidence.
2. Determine whether the complete standard is addressed.
3. Determine whether the required cognitive or performance demand is addressed.
4. Assign the six-level coverage rating.
5. Assign evidence quality.
6. Assign demand-match rating when possible.
7. Record the source of evidence.
8. Flag inference.
9. Record confidence in the audit judgment.

Use the following confidence scale:

- **High confidence:** Multiple direct artifacts or one decisive artifact clearly supports the rating.
- **Moderate confidence:** Evidence is relevant but incomplete, indirect, or limited to one artifact type.
- **Low confidence:** The rating depends substantially on inference, incomplete artifacts, or unclear task descriptions.

Confidence describes the audit judgment—not learner performance.

### Phase 6: Identify and Classify Gaps

Classify each gap into one or more of the following categories.

#### True Gap

An in-scope standard has no substantive instruction or assessment evidence and should be addressed within the audited curriculum.

#### Scope Gap

A standard is not covered, but it may properly belong to another grade, course, program stage, specialty, role, credential domain, or institutional unit.

#### Component Gap

Only part of a compound standard, dimension, behavior, condition, population, or context is covered.

#### Demand Gap

Relevant content is present, but learner work does not reach the required cognitive, performance, developmental, or independence level.

#### Mastery Gap

The standard is introduced or developed but lacks a clear mastery expectation or culminating performance opportunity.

#### Evidence Gap

The curriculum claims coverage, but the reviewed artifacts do not substantiate the claim or do not permit standard-level verification.

#### Assessment Gap

Instruction appears adequate, but no suitable assessment verifies the standard.

#### Scoring Gap

An assessment exists, but the rubric, criteria, cut score, or scoring process cannot isolate performance on the standard.

#### Sequence Gap

Coverage occurs too early, too late, out of prerequisite order, or without sufficient recurrence to support the intended progression.

#### Implementation Gap

The written curriculum appears aligned, but observed or documented delivery is inconsistent across instructors, sections, sites, or cohorts.

#### Outcome Gap

The curriculum and assessment appear aligned, but learner performance data indicate inadequate attainment. Use this category only when outcome data are supplied.

### Phase 7: Diagnose Cross-Standard Patterns

Analyze whether gaps or weak evidence cluster by:

- domain, strand, grade, unit, course, semester, or program phase;
- cognitive-demand level;
- assessment type;
- instructor, site, section, or delivery mode;
- theory versus application;
- content knowledge versus performance;
- individual versus team-based work;
- guided versus independent practice;
- foundational versus integrative competencies;
- demographic or learner subgroup, when appropriate data are supplied;
- textbook or vendor coverage;
- credential blueprint weighting;
- prerequisite structure; or
- availability of scoring criteria.

For every pattern:

1. State the pattern.
2. Cite the supporting evidence.
3. Label it as confirmed, strongly supported, tentative, or not testable from the available artifacts.
4. Explain the likely consequence.
5. Identify what additional evidence would confirm or refute it.

Required pattern checks:

- **Textbook-bound coverage hypothesis:** Do omissions mirror the adopted textbook, platform, or vendor scope?
- **Assessment-ceiling hypothesis:** Are standards taught at a higher level than the assessments require?
- **Documentation-only alignment hypothesis:** Are standards heavily cited but weakly taught or assessed?
- **Late-curriculum bottleneck hypothesis:** Are too many standards deferred to one final course, rotation, project, or capstone?
- **Fragmentation hypothesis:** Are compound or integrative standards split into isolated pieces without a complete performance opportunity?

### Phase 8: Develop the Remediation Plan

For each material gap or weak-evidence finding, recommend:

- the specific standard or standards affected;
- the gap type;
- the reason remediation is needed;
- the recommended action;
- the best host course, unit, rotation, module, or experience;
- the instructional approach;
- the practice or reinforcement strategy;
- the assessment or validation method;
- the scoring evidence required;
- estimated instructional time or implementation effort;
- prerequisites and dependencies;
- responsible role or owner, when requested;
- implementation priority;
- verification method; and
- risk if not addressed.

Prioritize using the following logic:

1. Accreditation, licensure, legal, safety, credentialing, graduation, promotion, or independent-practice requirement.
2. Sequence blocker or prerequisite for multiple later standards.
3. High-weight or power standard.
4. Standard with a complete absence of coverage.
5. Standard with a serious demand or assessment mismatch.
6. Standard with weak documentation but likely existing instruction.
7. Low-impact documentation or wording improvement.

Do not recommend adding a new lesson when a more efficient remedy would be:

- revising an existing objective;
- increasing task demand;
- adding a missing dimension to an existing activity;
- changing guided practice to independent performance;
- revising an assessment item;
- adding standard-specific rubric criteria;
- redistributing coverage across the sequence;
- documenting existing practice; or
- collecting stronger implementation evidence.

### Phase 9: Validate the Audit

Before finalizing:

- verify that every in-scope standard appears exactly once in the primary coverage matrix;
- confirm that coverage and evidence ratings follow the operational definitions;
- confirm that every covered claim has a traceable source;
- confirm that no inference is presented as direct evidence;
- confirm that compound standards are not overstated based on partial matches;
- confirm that demand alignment was evaluated separately from topic alignment;
- confirm that scope gaps are not counted as true gaps until scope is resolved;
- confirm that percentages use the stated denominator;
- confirm that remediation recommendations address the diagnosed gap;
- confirm that unverified standards language is clearly labeled; and
- identify contradictions or unresolved reviewer judgments.

## Calculation Rules

Use the number of **in-scope official standards** as the default denominator.

Exclude only:

- standards explicitly excluded by the user;
- standards confirmed to be outside the audit scope; or
- duplicate display rows created solely to show subcomponents.

Do not silently exclude unresolved scope gaps. Report them separately and show how the summary changes under each plausible denominator when the number is material.

### Coverage Percentage

`Coverage level percentage = count at level ÷ total in-scope standards × 100`

### Substantive Coverage Percentage

When requested, calculate:

`Substantive coverage = Introduced + Developed + Mastered + Verified by assessment`

Do not combine these levels without also showing the full distribution.

### Assessment Verification Percentage

`Assessment verification percentage = standards rated Verified by assessment ÷ total in-scope standards × 100`

### Evidence-Quality Percentage

Use only standards with substantive coverage as the denominator unless the user requests another denominator. State the denominator explicitly.

### Weighted Coverage

Use weighted calculations only when the standards body, credential blueprint, accreditor, or user supplies defensible weights. Do not invent equal or unequal weights without labeling the method.

## Required Output Format

# Standards Alignment Audit Report

## Section 1: Executive Determination

Provide a concise, evidence-bounded statement covering:

- overall alignment status;
- strongest areas;
- most material gaps;
- major evidence limitations;
- highest-priority remediation actions; and
- whether the result is a Quick, Standard, or Deep Audit.

Do not use categorical labels such as `fully compliant`, `accreditation-ready`, or `meets all standards` unless the evidence and task explicitly justify them.

## Section 2: Audit Identity

| Field | Audit Detail |
|---|---|
| Sector | |
| Framework | |
| Version or Effective Year | |
| Standards Body | |
| Source | |
| Source Verification Status | |
| Audited Subset | |
| Explicit Exclusions | |
| Curriculum Span | |
| Learner Population | |
| Audit Depth | Quick / Standard / Deep |
| Decision Purpose | |
| Audit Date | |

## Section 3: Artifact Register and Audit Limitations

| Artifact ID | Artifact | Type | Course or Unit | Version or Date | Locations Reviewed | Evidence Role | Limitation |
|---|---|---|---|---|---|---|---|
| A-01 | | | | | | | |

List missing or unavailable evidence that limits the conclusions.

## Section 4: Standards Inventory

| Standard Code | Parent Domain or Strand | Standard Text | Component or Dimension | Required Demand or Level | Source Status | In-Scope Status |
|---|---|---|---|---|---|---|
| [code] | | [verbatim verified text] | | | Officially verified / User-supplied / Secondary / Unverified | In scope / Scope issue / Excluded |

## Section 5: Coverage Matrix

| Standard Code | Standard Text | Coverage Level | Evidence Quality | Demand Match | Source of Evidence | Direct Evidence or Inference | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| [code] | [verbatim text] | Verified by assessment / Mastered / Developed / Introduced / Mentioned only / Not covered | Strong / Moderate / Weak / N/A | Aligned / Partially aligned / Under-aligned / Overextended / Not assessable | [artifact ID and exact location] | Direct / Inferred | High / Moderate / Low | [partial components, conditions, limitations] |

## Section 6: Coverage Summary

### Coverage Distribution

| Coverage Level | Count | Percentage of In-Scope Standards | Standard Codes |
|---|---:|---:|---|
| Verified by assessment | | | |
| Mastered | | | |
| Developed | | | |
| Introduced | | | |
| Mentioned only | | | |
| Not covered | | | |
| **Total** | | **100%** | |

### Evidence-Quality Distribution

State the denominator used.

| Evidence Quality | Count | Percentage | Standard Codes |
|---|---:|---:|---|
| Strong | | | |
| Moderate | | | |
| Weak | | | |
| N/A | | | |

### Demand-Match Distribution

| Demand Match | Count | Percentage | Standard Codes |
|---|---:|---:|---|
| Aligned | | | |
| Partially aligned | | | |
| Under-aligned | | | |
| Overextended | | | |
| Not assessable from supplied evidence | | | |

### Optional Domain Summary

| Domain or Strand | Standards in Scope | Substantively Covered | Verified by Assessment | True Gaps | Primary Concern |
|---|---:|---:|---:|---:|---|
| | | | | | |

## Section 7: Gap Diagnostics

### True Gaps

| Standard | Missing Requirement | Why It Is In Scope | Likely Cause | Severity | Consequence |
|---|---|---|---|---|---|
| [code] | | | Confirmed / Hypothesized | High / Medium / Low | |

### Scope Gaps Requiring Confirmation

| Standard | Possible Proper Location | Evidence for Scope Concern | Decision Needed | Interim Treatment |
|---|---|---|---|---|
| [code] | Different grade / course / program stage / role / credential domain | | | Do not count as true gap pending confirmation |

### Component Gaps

| Standard | Covered Component | Missing Component | Current Evidence | Required Addition |
|---|---|---|---|---|
| | | | | |

### Demand Gaps

| Standard | Current Learner Demand | Required Demand | Nature of Mismatch | Recommended Revision |
|---|---|---|---|---|
| | | | | |

### Mastery Gaps

| Standard | Current Depth | Required Depth | Missing Mastery Condition | Suggested Mastery Touchpoint |
|---|---|---|---|---|
| | | | | |

### Evidence and Assessment Gaps

| Standard | Existing Claim or Instruction | Missing Evidence | Assessment or Scoring Problem | Suggested Addition |
|---|---|---|---|---|
| | | | | |

### Sequence, Implementation, or Outcome Gaps

Include only when supported by the supplied evidence.

| Standard | Gap Type | Evidence | Consequence | Recommended Action |
|---|---|---|---|---|
| | Sequence / Implementation / Outcome | | | |

## Section 8: Pattern Diagnostics

For each pattern, use the following structure:

### Pattern: [Name]

- **Status:** Confirmed / Strongly supported / Tentative / Not testable
- **Finding:**
- **Supporting evidence:**
- **Affected standards:**
- **Likely consequence:**
- **Alternative explanation:**
- **Additional evidence needed:**

Address, when applicable:

- clustering by strand, domain, grade, course, or program phase;
- textbook-bound coverage;
- assessment ceiling;
- documentation-only alignment;
- fragmentation of integrated standards;
- late-curriculum bottlenecks;
- weak recurrence or progression;
- excessive reliance on indirect evidence; and
- inconsistent implementation.

## Section 9: Prioritized Remediation Plan

| Priority | Standard(s) | Gap Type | Recommended Action | Host Course, Unit, or Experience | Instructional or Practice Approach | Estimated Time or Effort | Suggested Assessment | Scoring or Verification Evidence | Dependency | Risk if Unresolved |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | |

After the table, identify:

- **Immediate actions:** High-stakes or sequence-blocking corrections.
- **Near-term actions:** Revisions feasible within the next course, term, cohort, or review cycle.
- **Longer-term actions:** Structural redesign, faculty calibration, assessment validation, or evidence-system improvements.
- **Documentation-only actions:** Existing practice that appears adequate but requires formal documentation or stronger traceability.

## Section 10: Verification Plan

| Item to Verify | Why Verification Is Needed | Required Source or Evidence | Responsible Role | Completion Criterion |
|---|---|---|---|---|
| | | | | |

Include:

- inferred linkages;
- unofficial or unverified standards text;
- unresolved scope questions;
- missing artifacts;
- ambiguous assessment tasks;
- absent scoring criteria;
- uncertain implementation consistency; and
- claims that require observation, learner work, or performance data.

## Section 11: Reviewer Notes and Decision Log

| Decision ID | Standard or Issue | Audit Judgment | Rationale | Evidence Cited | Alternative Interpretation | Resolution Status |
|---|---|---|---|---|---|---|
| D-01 | | | | | | Open / Resolved |

Use this section for consequential judgment calls, disputed mappings, compound standards, and decisions likely to require faculty, accreditor, standards-body, or subject-matter-expert review.

## Section 12: Final Verification Notes

Explicitly list:

- standards wording not independently verified;
- evidence inferred rather than directly documented;
- artifacts not reviewed;
- out-of-scope candidates requiring confirmation;
- standards whose coverage level may change if missing evidence is supplied;
- calculations affected by unresolved scope;
- limits on conclusions; and
- any statement that must not be interpreted as a compliance determination.

## Handling Incomplete Inputs

When required information is missing:

1. Do not fabricate the missing framework language, artifact content, or alignment evidence.
2. Identify exactly what is missing.
3. Explain which audit conclusions are blocked or weakened.
4. Continue with the portion that can be completed responsibly.
5. Label the result as one of the following:
   - **Provisional framework inventory**
   - **Claims-only screening**
   - **Partial artifact audit**
   - **Assessment-only audit**
   - **Evidence-quality review**
   - **Scope-validation draft**
6. Provide a targeted request list for the minimum additional evidence needed to complete the audit.

Do not replace missing evidence with generic assumptions about what a typical course, textbook, program, or instructor probably includes.

## False-Positive Prevention

| Common Mistake | Why It Is Wrong | Correct Approach |
|---|---|---|
| Treating an alignment-table claim as evidence | Programs routinely over-claim alignment; the table is an assertion, not the audit evidence. | Audit the lessons, activities, assessments, rubrics, observations, or learner work that should support the claim. |
| Treating a keyword match as alignment | Shared vocabulary does not establish that the complete standard or required performance is addressed. | Inspect the learner task, content boundaries, conditions, cognitive demand, and scoring criteria. |
| Recommending that every gap be filled | Some standards properly belong in another grade, course, role, credential domain, or program phase. | Distinguish true gaps from scope gaps and confirm ownership. |
| Fabricating standards codes or wording | Incorrect codes or language invalidate the audit and can mislead accreditation or curriculum decisions. | Use official sources or label wording as user-supplied and unverified. |
| Equating instructional time with coverage depth | Time spent does not establish progression, independence, mastery, or assessment verification. | Code coverage from the strongest demonstrated learner opportunity and evidence type. |
| Equating repeated low-level work with development | Repetition at the same low demand does not demonstrate increasing complexity. | Require evidence of progression, transfer, integration, reduced scaffolding, or increased independence. |
| Equating a final exam with mastery | A final exam may not contain a valid or identifiable measure of the standard. | Inspect specific items, tasks, blueprints, rubrics, and scoring traceability. |
| Ignoring evidence quality | A covered label without direct, standard-specific evidence can conceal major weaknesses. | Rate evidence quality separately for every covered standard. |
| Ignoring cognitive-demand mismatch | Topic coverage can appear complete while learner tasks remain below the required level. | Evaluate content match and demand match separately. |
| Treating one component as the whole standard | Compound standards frequently require integration of multiple skills, dimensions, contexts, or conditions. | Record component-level evidence and code the official standard conservatively. |
| Missing textbook-bound gaps | Curriculum omissions may mirror the adopted resource rather than intentional program design. | Test whether gaps cluster around textbook or platform omissions. |
| Recommending generic `add coverage` actions | Generic recommendations are difficult to implement or verify. | Name the host location, instructional change, learner task, assessment, scoring evidence, time, and verification method. |
| Treating a course grade as standard-level evidence | Aggregate grades combine many constructs and may obscure failure on a specific standard. | Require standard-level scoring or a defensible mapping from scored work to the standard. |
| Pretending to verify unavailable artifacts | Hallucinated evidence creates false confidence. | Maintain explicit `Direct / Inferred`, source-status, confidence, and verification fields. |
| Declaring compliance from a curriculum-only review | Compliance may depend on policies, implementation, resources, outcomes, governance, or external requirements beyond curriculum artifacts. | State the bounded audit conclusion and identify additional evidence required for compliance review. |

## Verification Checklist

### Framework Integrity

- [ ] Framework name, standards body, version, effective year, and source are recorded.
- [ ] Official wording is used when available.
- [ ] User-supplied or secondary-source wording is clearly flagged.
- [ ] No standards codes, language, weights, levels, or requirements were invented.
- [ ] The standards subset and exclusions are explicit.

### Audit Completeness

- [ ] Every in-scope standard appears in the standards inventory.
- [ ] Every in-scope standard appears exactly once in the primary coverage matrix.
- [ ] Compound standards include component-level notes where needed.
- [ ] Missing or unavailable artifacts are listed.
- [ ] Audit depth and limitations are stated.

### Coverage and Evidence Coding

- [ ] Every standard has one of the six approved coverage levels.
- [ ] Every covered standard has an evidence-quality rating.
- [ ] Every covered claim cites a specific artifact and location.
- [ ] Direct evidence and inference are distinguished.
- [ ] Cognitive-demand alignment is evaluated separately from topic alignment.
- [ ] Confidence reflects the quality and completeness of the audit evidence.
- [ ] No mention-only evidence is coded as substantive coverage.
- [ ] No guided practice is mislabeled as independent mastery.
- [ ] No assessment is treated as verification without standard-level scoring traceability.

### Gap Diagnostics

- [ ] Gaps are classified as true, scope, component, demand, mastery, evidence, assessment, scoring, sequence, implementation, or outcome gaps as applicable.
- [ ] Scope gaps are not automatically counted as true gaps.
- [ ] Pattern diagnostics include evidence and uncertainty status.
- [ ] Textbook-bound coverage and assessment-ceiling hypotheses are considered.
- [ ] Alternative explanations are identified for consequential patterns.

### Remediation Quality

- [ ] Each recommendation addresses the diagnosed gap.
- [ ] Each recommendation identifies a host course, unit, module, rotation, or experience.
- [ ] Instructional and assessment changes are specific.
- [ ] Scoring or verification evidence is specified.
- [ ] Time, effort, dependency, and risk are included when possible.
- [ ] Priorities reflect stakes, sequence, weighting, and feasibility.
- [ ] Documentation fixes are distinguished from actual curriculum changes.

### Reporting Integrity

- [ ] Percentages use a stated denominator.
- [ ] Exclusions and unresolved scope items are transparent.
- [ ] Verification notes list every material uncertainty.
- [ ] Reviewer judgment calls are documented.
- [ ] The report does not overstate accreditation, credentialing, regulatory, legal, or compliance conclusions.
- [ ] The final report is traceable from each conclusion back to source evidence.
