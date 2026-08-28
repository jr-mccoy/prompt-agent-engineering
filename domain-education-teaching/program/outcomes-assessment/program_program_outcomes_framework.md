---
title: "Program Outcomes Framework (PSLO / ISLO / CSLO / PLO Architecture)"
category: education-teaching/program-outcomes-assessment
description: "Design a coherent program-outcomes architecture — Institutional Student Learning Outcomes, Program Student Learning Outcomes, and Course-Level Outcomes — with parent–child relationships, coverage mapping, and assessment-evidence alignment."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-01
  - OC-03
  - QA-01
  - QA-02
difficulty: advanced
tags:
  - education
  - program-outcomes
  - learning-outcomes
  - pslo
  - islo
  - cslo
  - higher-ed
  - k12
  - workforce
  - accreditation
updated: "2026-05-15"
related_prompts:
  - teaching_outcomes_to_assessment_mapper.md
  - teaching_program_gap_analysis.md
  - ../curriculum-design/teaching_competency_framework_designer.md
  - ../curriculum-design/teaching_learning_objectives_writer_blooms.md
  - ../curriculum-design/teaching_curriculum_map_builder.md
---

# Program Outcomes Framework (PSLO / ISLO / CSLO / PLO Architecture)

**Objective:** Design a three-tier program-outcomes architecture: top-level Institutional Student Learning Outcomes (ISLOs) or graduate-profile competencies, mid-level Program Student Learning Outcomes (PSLOs / PLOs), and course- or unit-level Student Learning Outcomes (CSLOs) — with explicit parent–child relationships, assessment-evidence pointers, and a coverage matrix showing which mid-level outcomes roll up to which top-level outcomes.

## When to Use
- ✅ Building a new program's outcomes architecture before course design
- ✅ Retrofitting a program for accreditation that requires PSLO–ISLO mapping
- ✅ Auditing whether an existing PSLO set adequately covers an ISLO
- ✅ Designing K-12 graduate-profile rollup from grade-band outcomes
- ✅ Workforce-program outcomes architecture rolling up to industry-credential competencies
- ❌ Writing course-level learning objectives in detail (use `teaching_learning_objectives_writer_blooms.md`)
- ❌ Building the curriculum-to-outcomes mapping matrix itself (use `teaching_curriculum_map_builder.md`)

## Inputs Required
- **Sector:** K-12 / Higher Education / Workforce-CTE / Medical Education
- **Institution / program name**
- **Existing top-level outcomes** (ISLOs / graduate profile / industry framework): paste if available
- **Program mission and audience:** who the program serves, what it commits to
- **Number of PSLOs/PLOs desired:** typically 5-8
- **Existing courses or modules** (optional): list with brief description
- **Accreditation body** (if applicable): for outcomes-language conventions
- **Time horizon:** typically program completion (4-year degree, 2-year apprenticeship, K-12 graduation)

## Constraints

**Must:**
- Write every outcome at every tier in observable, measurable form
- Show parent–child relationships in a roll-up matrix
- Confirm every ISLO/top-level outcome is supported by at least one PSLO
- Confirm every PSLO is supported by at least one CSLO or course (if course list provided)
- Use sector-appropriate outcome verbs (HE: PSLO often starts with "Graduates will…"; K-12: "Students will…"; workforce: "Upon completion, learners will…")
- Tag each PSLO with the highest Bloom's level it targets (graduation-level performance)

**Must Not:**
- Repeat the same outcome at multiple tiers (the relationship should be roll-up, not duplication)
- Write PSLOs so generic they could apply to any program ("communicate effectively" without disciplinary context)
- Mix outcomes (long-term, integrative) with objectives (lesson-level, discrete) at the program tier
- Include dispositions without operational indicators
- Generate more than ~10 PSLOs (operational limit for assessment plans)
- Invent institutional or accreditor language; cite or flag for verification

## Instructions

1. **Establish or confirm the top tier.**
   - If user provided ISLOs / graduate profile / industry framework, list them as-is with source citation.
   - If not, draft 4-6 top-tier outcomes derived from the program mission. Mark as "DRAFT — institution must ratify."

2. **Draft PSLOs (5-8).**
   - Each PSLO should be:
     - **Disciplinary:** specific to the program's field
     - **Graduation-level:** the integrated performance expected at completion
     - **Observable:** an external evaluator could score evidence of it
     - **Bloom's-tagged:** typically Apply / Analyze / Evaluate / Create at graduation
   - Use prefix conventions for the sector: "Graduates will…" (HE), "Upon program completion, learners will…" (workforce), "By the end of [grade band], students will…" (K-12).

3. **Build PSLO-to-ISLO roll-up matrix.**
   - For each PSLO, mark which ISLOs it contributes to.
   - Every ISLO must have ≥1 PSLO mapped. Every PSLO must map to ≥1 ISLO.
   - Flag orphans in either direction.

4. **Sketch course-level mapping (if course list provided).**
   - For each course, indicate which PSLOs it touches and at what depth: Introduce / Develop / Master (I-D-M).
   - Every PSLO must have ≥1 course at Master depth.

5. **Identify evidence for each PSLO.**
   - Name 2-4 evidence types per PSLO that can produce graduation-level performance signal (capstone, portfolio, performance task, internship evaluation, licensure exam, external review).

6. **Audit the architecture.**
   - Coverage: any ISLO with weak PSLO coverage? Any PSLO with no Master-depth course?
   - Granularity: are PSLOs at consistent granularity? (None should be much more specific or much broader than peers.)
   - Bloom's distribution: are PSLOs concentrated at low levels (red flag for a graduation outcome) or appropriately at upper levels?
   - Sector conventions: HE PSLO language vs. K-12 graduate-profile language vs. workforce competency-statement language.

7. **Produce the output** with all three sections: architecture, roll-up matrix, audit.

## Output Format

### Section 1: Program Outcomes Architecture

**Institution / Program:** [name]
**Sector:** [K-12 / HE / Workforce / Med-Ed]
**Accreditor (if applicable):** [body + standard reference]

**Top Tier — Institutional Student Learning Outcomes / Graduate Profile / Industry Framework:**

| ID | Outcome | Source |
|---|---|---|
| ISLO-1 | [text] | [Institutional / graduate profile doc / industry framework citation] |
| ISLO-2 | [text] | |

**Middle Tier — Program Student Learning Outcomes (PSLOs):**

| ID | PSLO | Bloom's | Evidence Types |
|---|---|---|---|
| PSLO-1 | [Graduates will…] | [level] | [evidence list] |
| PSLO-2 | … | | |

**Bottom Tier — Course-Level Student Learning Outcomes (CSLOs):**

For each course (if course list provided):

| Course | CSLO | Maps to PSLO(s) | Depth |
|---|---|---|---|
| [Course code] | [CSLO text] | [PSLO IDs] | I / D / M |

### Section 2: Roll-Up Matrix

**PSLO ↔ ISLO Matrix:**

| | ISLO-1 | ISLO-2 | ISLO-3 | ISLO-4 |
|---|---|---|---|---|
| PSLO-1 | ✓ | | ✓ | |
| PSLO-2 | | ✓ | | |
| PSLO-3 | ✓ | ✓ | | |

**Course ↔ PSLO Matrix (depth):**

| Course | PSLO-1 | PSLO-2 | PSLO-3 | … |
|---|---|---|---|---|
| [Course] | I | D | | |
| [Course] | | D | M | |

### Section 3: Architecture Audit

| Audit Question | Result | Notes |
|---|---|---|
| Every ISLO has ≥1 PSLO mapped | Pass / Fail | [list orphan ISLOs] |
| Every PSLO maps to ≥1 ISLO | Pass / Fail | [list orphan PSLOs] |
| Every PSLO has ≥1 course at Master depth (if courses listed) | Pass / Fail | [list PSLOs without Master coverage] |
| PSLO granularity is consistent | Pass / Fail | [list outliers] |
| PSLO Bloom's distribution skewed appropriately upper | Pass / Fail | [list low-Bloom's PSLOs] |
| All outcomes observable | Pass / Fail | [list non-observable] |
| Sector / accreditor language conventions followed | Pass / Fail | [notes] |

### Section 4: Recommendations

- **Add:** [PSLOs or CSLOs to add to fix coverage gaps]
- **Revise:** [outcomes needing rewrite for observability or granularity]
- **Retire:** [redundant or unsupported outcomes]
- **Verification needed:** [items requiring institutional or accreditor review]

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Treating PSLOs as longer course objectives | PSLOs are integrative graduation-level performance; objectives are lesson-level | PSLO: "Graduates will design and evaluate evidence-based interventions for community health"; Objective: "Will list 4 social determinants of health" |
| Duplicating outcomes at multiple tiers | ISLO and PSLO with identical text wastes the architecture | Tiers must differ in scope/integration; PSLO is disciplinary specification of the broader ISLO |
| PSLOs written without disciplinary content | "Communicate effectively" applies to every program | Add disciplinary specification: "Communicate technical findings to non-engineering stakeholders" |
| Skipping I-D-M depth coding | Coverage looks fine on paper but every course only Introduces | I-D-M reveals whether students actually reach Master depth somewhere |
| Inventing ISLOs without institutional grounding | ISLOs are institutionally ratified; you can't manufacture them | Use existing ISLO statements or mark draft outputs as "DRAFT — requires institutional ratification" |
| Too many PSLOs (>10) | Assessment plans become unmanageable | Cap at 8; merge or subsume overlapping outcomes |
| Confusing dispositions with outcomes | "Demonstrates ethical commitment" — not observable | Operationalize as observable behavior in context |
| Misciting accreditor outcome language | Different accreditors (HLC, MSCHE, SACSCOC, ABET, AACSB) use different terminology — assertion errors damage submissions | Use accreditor's actual language conventions; flag for verification |

## Verification Checklist

- [ ] 4-6 ISLOs (or graduate-profile / industry-framework top-tier elements)
- [ ] 5-8 PSLOs, each disciplinary and graduation-level
- [ ] Every ISLO mapped to ≥1 PSLO
- [ ] Every PSLO mapped to ≥1 ISLO
- [ ] CSLOs (if courses provided) map up cleanly with I-D-M depth
- [ ] Every PSLO has Master-depth coverage in at least one course
- [ ] Every PSLO has 2-4 evidence types named
- [ ] Sector / accreditor vocabulary used
- [ ] No outcome duplicated across tiers
- [ ] Bloom's distribution is graduation-appropriate (upper levels predominant in PSLOs)
- [ ] Outputs flagged as DRAFT where institutional/accreditor verification is required
