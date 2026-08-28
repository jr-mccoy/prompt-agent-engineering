---
title: "Higher-Ed Program Scope & Sequence (Course Sequencing & Prerequisites)"
category: education-teaching/program/curriculum-design
description: "Design a higher-education program's scope and sequence — courses by term across the credential length, with prerequisites, gateway courses, capstone placement, credit-hour distribution, and Quality Matters or accreditor-aligned coherence checks."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - ED-01
  - QA-01
difficulty: advanced
tags:
  - education
  - curriculum-design
  - scope-and-sequence
  - higher-ed
  - course-sequencing
  - prerequisites
  - capstone
  - gateway-courses
  - accreditation
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/program/curriculum-design/program_curriculum_map_builder.md
  - domain-education-teaching/program/curriculum-design/program_backward_program_design.md
  - domain-education-teaching/program/outcomes-assessment/program_program_outcomes_framework.md
  - domain-education-teaching/program/curriculum-design/program_course_design_he.md
---

# Higher-Ed Program Scope & Sequence

**Objective:** Design a higher-education program's full course sequence — by term across the credential length — with prerequisite logic, gateway-course identification, capstone placement, credit-hour distribution, GE/major/elective balance, and a coherence audit against PSLOs.

## When to Use
- ✅ Designing a new degree program (associate, bachelor, master, certificate)
- ✅ Restructuring an existing program after PSLO revision
- ✅ Aligning the sequence to accreditor requirements (regional or programmatic)
- ✅ Designing a coherent stackable-credential pathway
- ✅ Compressing or extending a program (e.g., 3-year bachelor, accelerated MSN)
- ❌ Designing one course (use `teaching_course_design_he.md`)
- ❌ K-12 scope and sequence (use `teaching_scope_sequence_k12.md`)
- ❌ Workforce / apprenticeship sequencing (use `teaching_scope_sequence_workforce.md`)

## Inputs Required
- **Institution and program name; credential awarded**
- **Total credits / units required** (and accreditor-mandated minimums)
- **Term structure:** semester / quarter / trimester; number of terms per year; expected program duration
- **Credit categories:** general education, major core, major electives, free electives, capstone — with required minima
- **PSLOs:** the program student learning outcomes the sequence must produce
- **Existing course catalog** (optional): list with codes, titles, credit hours, prerequisites
- **Accreditor requirements:** specific course or content requirements (e.g., ABET-required engineering science, AACSB-required business core)
- **Partner-institution articulation requirements** (e.g., transfer alignment, 2+2 design)
- **Modality:** in-person / online / hybrid / hyflex
- **Cohort vs. self-paced enrollment**
- **Population constraints:** working adults, traditional students, international students, prerequisites learners commonly arrive with

## Constraints

**Must:**
- Total credits = required total (within accreditor and institutional limits)
- Every PSLO covered at I, D, and M depth across the sequence
- Every prerequisite course precedes its dependents in time
- Gateway courses (typically high-DFW, foundational for the major) placed early with adequate support
- Capstone in final term (after prerequisite Master-depth courses)
- Credit-hour distribution honors GE/major/elective requirements
- Pacing fits expected program duration with realistic per-term credit loads
- Accreditor course/content requirements explicit and mapped

**Must Not:**
- Generate a sequence that exceeds the credit limit or omits required courses
- Place gateway courses without identifying the support resources (tutoring, supplemental instruction, advising touchpoints)
- Put capstone before its prerequisite Master-depth courses
- Ignore articulation requirements (transfer credit, 2+2 alignment)
- Invent course codes; use provided codes or mark as "TBD code" for proposed courses
- Stack too many high-difficulty courses in one term

## Instructions

1. **Confirm inputs.** Echo back: program, credential, total credits, term structure, duration, credit categories, PSLOs, accreditor requirements, modality, population.

2. **Build the credit-hour budget.**

| Category | Required Credits | % of Total |
|---|---|---|
| General Education | | |
| Major Core | | |
| Major Electives | | |
| Free Electives | | |
| Capstone | | |
| **Total** | | 100% |

3. **Inventory existing courses (or design proposed ones).**
   - For each: code, title, credits, category (GE/Core/Elective/Capstone), prerequisites, PSLOs touched (I/D/M).
   - Tag courses as Required / Optional / Proposed.

4. **Identify gateway courses.**
   - Foundational courses with disproportionate impact on student progression (often math, writing, intro-to-major).
   - Identify support resources required for high-success rates.

5. **Sequence by term.**
   - Allocate per term: total credit load (typically 12-18 UG, 9-12 grad), course mix (≥1 gateway in early terms; balance between high-cognitive-load courses; avoid stacking labs).
   - Honor prerequisites: dependent courses follow prerequisites by ≥1 term.
   - Front-load gateway and foundational courses; mid-program for major core; final terms for capstone and integrative work.

6. **PSLO coverage check.**
   - Build PSLO × term grid showing depth (I/D/M) by term.
   - Confirm every PSLO has I in early terms, D in mid terms, M in late terms.
   - Confirm capstone touches every PSLO at M depth.

7. **Accreditor requirement mapping.**
   - For each accreditor-required course/content, identify which course satisfies it.
   - Flag unsatisfied requirements explicitly.

8. **Articulation and pathway considerations.**
   - For transfer-friendly programs: which courses in the first 60 credits align with the major's typical articulation agreements?
   - For stackable credential designs: which course clusters award an embedded certificate?

9. **Audit the design.**
   - Total credits = required
   - All PSLOs M-covered by capstone
   - All prerequisites precede dependents
   - All accreditor-required courses included
   - Per-term credit load reasonable
   - Gateway courses supported

10. **Produce the output.**

## Output Format

### Section 1: Design Identity
- Program, credential, total credits, term structure, duration, modality, population

### Section 2: Credit-Hour Budget Table

### Section 3: Course Inventory

| Code | Title | Credits | Category | Prerequisites | PSLOs (I/D/M) |
|---|---|---|---|---|---|

### Section 4: Term-by-Term Sequence

**Term 1 (Fall Year 1)**

| Course Code | Title | Credits | PSLOs (depth) | Notes |
|---|---|---|---|---|

**Term 2 (Spring Year 1)** … (repeat for all terms)

**Term [Final] (Capstone Term)**

| Course Code | Title | Credits | PSLOs (depth) | Notes |
|---|---|---|---|---|

### Section 5: PSLO × Term Coverage

|  | T1 | T2 | T3 | … | Capstone |
|---|---|---|---|---|---|
| PSLO-1 | I | D | D | | M |
| PSLO-2 | | I | D | M | M |

### Section 6: Accreditor Requirements Map

| Requirement | Source (Accreditor + Standard) | Satisfied by Course | Status |
|---|---|---|---|

### Section 7: Gateway Courses & Support Plan

| Course | Term | Historical DFW Rate (if known) | Support Resources |
|---|---|---|---|

### Section 8: Articulation / Pathway Notes
- Transfer-friendly course identification
- Stackable credential embedding
- Bridge / co-requisite course design

### Section 9: Design Audit

| Audit Question | Result | Notes |
|---|---|---|
| Total credits = required | Pass / Fail | |
| All PSLOs M-covered by capstone | Pass / Fail | |
| All prerequisites precede dependents | Pass / Fail | |
| All accreditor-required content included | Pass / Fail | |
| Per-term credit load reasonable | Pass / Fail | |
| Gateway support plan present | Pass / Fail | |
| Credit category minima met | Pass / Fail | |

### Section 10: Verification Notes
- Proposed-course codes flagged as TBD
- Accreditor requirements flagged for verification against current published criteria
- Articulation agreements that should be confirmed

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Gateway course in Term 1 with no support | High DFW rates damage retention; predictable failure | Place gateway courses with identified tutoring, SI, advising touchpoints |
| Capstone before Master-depth prerequisites | Capstone becomes superficial without prerequisite mastery | Ensure all PSLOs reach M before capstone term |
| Ignoring credit-load realism | 20-credit terms produce attrition | Standard UG load is 15; high-load justified only with reduced course difficulty |
| Inventing accreditor requirements | Each accreditor (ABET, AACSB, CCNE, etc.) has specific course/content rules | Cite accreditor's published standards; flag for verification |
| Sequence works on paper but ignores modality | Online-only programs need different sequencing (cohort vs. self-paced) | Honor modality; cohort sequencing differs from self-paced |
| All electives lumped together | Electives can encode breadth vs. depth options | Distinguish guided electives (concentration / minor) from free electives |
| Missing GE distribution requirements | Most regional accreditors have GE breadth requirements (humanities, sciences, social sciences, etc.) | Honor GE distribution as well as total GE credit count |
| Ignoring articulation | Transfer students may not be able to enter the sequence cleanly | Build transfer-friendly entry points or mark as non-articulating with rationale |

## Verification Checklist

- [ ] Total credits = required
- [ ] All credit categories meet minima
- [ ] Every PSLO has I, D, M coverage across the sequence
- [ ] Capstone in final term after M-depth prerequisites
- [ ] Every prerequisite precedes its dependents
- [ ] Gateway courses identified with support plan
- [ ] Per-term credit load 12-18 UG or 9-12 grad (justified deviations)
- [ ] Accreditor-required content mapped to courses
- [ ] Articulation considerations addressed
- [ ] Verification notes list unverified items
