---
title: "Programmatic Accreditation Self-Study Builder (Parameterized)"
category: education-teaching/program/accreditation-review
description: "Build a programmatic-accreditation self-study (ABET, AACSB, CAEP, CCNE, ACPE, NAEYC, NASAD, NASM, etc.) — parameterized by accreditor — translating program evidence into criterion-aligned response sections with outcomes evidence, continuous improvement loop, and action plan."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - QA-01
  - QA-02
difficulty: advanced
tags:
  - education
  - accreditation
  - self-study
  - programmatic-accreditation
  - abet
  - aacsb
  - caep
  - ccne
  - acpe
  - higher-ed
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/program/accreditation-review/program_accreditation_self_study_he.md
  - domain-education-teaching/program/accreditation-review/program_accreditation_self_study_meded.md
  - domain-education-teaching/program/accreditation-review/program_accreditation_evidence_compiler.md
  - ../program-outcomes-assessment/teaching_outcomes_to_assessment_mapper.md
---

# Programmatic Accreditation Self-Study Builder

**Objective:** Build the program-level self-study narrative for a specialized / programmatic accreditor (engineering, business, education, nursing, pharmacy, early childhood, art/design/music, etc.) — parameterized by accreditor — translating program evidence into criterion-aligned response sections with student-outcomes evidence, continuous-improvement loops, and action plans.

## When to Use
- ✅ ABET (engineering, computing, applied science, technology) self-study
- ✅ AACSB business accreditation reaffirmation
- ✅ CAEP / state educator preparation accreditation
- ✅ CCNE or ACEN nursing accreditation
- ✅ ACPE pharmacy accreditation
- ✅ NAEYC, NASAD, NASM, NAAB, NCATE-successor, or other specialized accreditors
- ❌ Regional accreditation (use `teaching_accreditation_self_study_he.md`)
- ❌ Med-ed accreditation (use `teaching_accreditation_self_study_meded.md`)

## Inputs Required
- **Accreditor:** name + organizational acronym (ABET, AACSB, CAEP, CCNE, ACPE, NAEYC, NASAD, NASM, NAAB, etc.)
- **Accreditor's current criteria version**
- **Program identity:** specific program/degree being accredited, credential awarded, enrollment, faculty count
- **Criteria/standards in scope:** which sections of the self-study are being drafted
- **Student outcomes data:** program outcomes attainment evidence (multi-year)
- **Continuous improvement evidence:** prior cycles' improvements and their results
- **Curriculum map / outcomes assessment plan** with documented results
- **Faculty data:** credentials, qualifications, scholarly/professional activity, intellectual contributions
- **Resources data:** financial, facilities, library, technology, advising
- **Student data:** admissions, progression, completion, post-graduation
- **Prior accreditation feedback** (if any)

## Constraints

**Must:**
- Honor the accreditor's actual structure (ABET Criteria 1-8 + Program Criteria; AACSB Standards 1-15 by area; CAEP Standards 1-5; CCNE Standards I-IV)
- Quote criterion/standard language verbatim with verification flag
- Show multi-year outcomes data (most programmatic accreditors require 3+ years)
- Demonstrate continuous improvement: action → measure → result → next action
- Map curriculum to outcomes with depth coding
- Address faculty qualifications per accreditor-specific definitions
- Include action plan for identified weaknesses

**Must Not:**
- Invent criterion text or standard numbers
- Substitute regional accreditation responses for programmatic
- Hide outcomes underperformance (accreditors expect honest reporting with plans)
- Skip the continuous-improvement loop (this is often the most-scrutinized section)
- Generate responses without supplied evidence
- Confuse different accreditors' terminology

## Instructions

1. **Confirm accreditor.** Echo: accreditor, version, criteria/standards in scope.

2. **For each criterion/standard:**

   a. **Quote criterion language verbatim** (verification flag).

   b. **Identify expected evidence types per the accreditor's guidance.**
      - ABET: Student Outcomes (typically 1-7) with assessment process and continuous improvement
      - AACSB: Standards in Strategic Management, Participants, Learning, Academic and Professional Engagement
      - CAEP: Content/Pedagogical Knowledge; Clinical Partnerships; Candidate Quality; Program Impact; Quality Assurance
      - CCNE: Mission/Governance; Institutional Commitment; Curriculum; Program Effectiveness

   c. **Build the response:**
      - **Claim:** What the program does
      - **Evidence:** Specific artifacts, data tables, results
      - **Analysis:** How evidence supports compliance
      - **Continuous Improvement:** Action history → results → next action
      - **Strengths:** What's working
      - **Action Plan:** For identified weaknesses

3. **Build the outcomes-attainment evidence table.**
   - For each program outcome: multi-year attainment data, target threshold, status, action if below target

4. **Build the curriculum-to-outcomes map** (typically a required artifact).
   - Course × outcome matrix with depth coding

5. **Build the faculty qualifications table** per accreditor's definitions.
   - ABET: Sufficient and qualified faculty (areas of expertise, professional engagement)
   - AACSB: Scholarly Academic / Practice Academic / Scholarly Practitioner / Instructional Practitioner ratios
   - CAEP: Provider quality assurance system
   - CCNE: Faculty academic and professional preparation

6. **Build the continuous-improvement narrative.**
   - For ABET especially: complete cycle of assessment → analysis → action → re-assessment
   - Show "closing the loop" with re-measurement after action

7. **Build the action plan.**
   - For each identified weakness: action, owner, timeline, measure

8. **Length and format audit.**

## Output Format

### Section 1: Self-Study Identity
- Accreditor, version, program, credential, criteria/standards in scope

### Section 2: Per-Criterion Response

For each:

**Criterion/Standard [N]: [Title]**

*Verbatim language (verification flag):*

> [text]

*Expected Evidence:*

[list per accreditor guidance]

*Response:*

| Element | Content |
|---|---|
| Claim | |
| Evidence | [artifacts + data + IDs] |
| Analysis | |
| Continuous Improvement | [cycle: action → result → next action] |
| Strengths | |
| Action Plan | |

### Section 3: Outcomes Attainment Evidence

| Program Outcome | Year N-2 | Year N-1 | Year N | Target | Status | Action if Below |
|---|---|---|---|---|---|---|

### Section 4: Curriculum-to-Outcomes Map

| Course | Outcome 1 | Outcome 2 | … |
|---|---|---|---|
| | I | D | M | … |

### Section 5: Faculty Qualifications (per accreditor)

[accreditor-specific table — see Instructions]

### Section 6: Continuous-Improvement Narrative
- Cycle examples with closed loops

### Section 7: Action Plan

| Weakness | Action | Owner | Timeline | Measure |
|---|---|---|---|---|

### Section 8: Response to Prior-Cycle Feedback

| Recommendation | Action | Evidence | Status |
|---|---|---|---|

### Section 9: Length/Format Audit

### Section 10: Verification Notes
- Criterion/standard language verification needed
- Evidence requiring institutional confirmation

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Mixing programmatic and regional accreditor structures | Different requirements; different criteria | Use the specific accreditor's structure |
| Single-year outcomes data | Most programmatic accreditors require multi-year trend | Provide 3+ years |
| No "closing the loop" | Continuous improvement is centerpiece; missing it is a major finding | Action → result → re-measure → next action explicit |
| Faculty qualifications by mismatched definition | Each accreditor defines qualified faculty differently | Honor the accreditor's specific definitions |
| Curriculum map without depth coding | Coverage without mastery is hidden | Use I/D/M (or accreditor-specific scheme) |
| Vague action plans | Accreditors require specific commitments | Action + owner + timeline + measure |
| Quoting outdated criterion versions | Misalignment | Cite current version with verification flag |

## Verification Checklist

- [ ] Accreditor identified with version
- [ ] Every criterion has claim + evidence + analysis + continuous improvement
- [ ] Outcomes attainment data multi-year
- [ ] Curriculum-to-outcomes map with depth
- [ ] Faculty qualifications by accreditor's definition
- [ ] Continuous-improvement cycle complete (closed loop)
- [ ] Action plan specific
- [ ] Prior-cycle feedback addressed
- [ ] Format/length within accreditor limits
- [ ] No invented criterion text
