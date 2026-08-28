---
title: "Program Competency Framework (ACGME Six Core Competencies)"
category: medical-education/educator-curriculum-design
description: "Build a program-specific competency framework grounded in the ACGME six core competencies (Patient Care, Medical Knowledge, Professionalism, Interpersonal & Communication Skills, Practice-Based Learning, Systems-Based Practice) with specialty-specific sub-competencies, observable performance indicators, and program-defined integrative competencies."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - CM-01
  - QA-01
difficulty: advanced
tags:
  - medical-education
  - acgme
  - core-competencies
  - residency
  - competency-framework
  - milestones
updated: "2026-05-15"
related_prompts:
  - curric_cbme_implementation_program.md
  - curric_residency_curriculum_mapper.md
  - curric_epa_implementation_designer.md
  - ../../../../domain-education-teaching/program/curriculum-design/program_competency_framework_designer.md
---

# Program Competency Framework (ACGME Six Core Competencies)

**Objective:** Build a program-specific competency framework anchored in the ACGME six core competencies (Patient Care, Medical Knowledge, Professionalism, Interpersonal & Communication Skills, Practice-Based Learning and Improvement, Systems-Based Practice) with specialty-specific sub-competencies (Milestones), observable performance indicators, and any program-defined integrative competencies that extend the standard framework.

## When to Use
- ✅ Documenting a residency or fellowship program's competency framework for ACGME submission
- ✅ Operationalizing program-specific extensions of the ACGME framework
- ✅ Onboarding new faculty and learners to the program's competency structure
- ✅ Auditing program competency framework against ACGME requirements
- ❌ Designing assessment for individual competencies (use `curric_epa_implementation_designer.md` or evidence-design prompts)
- ❌ Building CBME implementation (use `curric_cbme_implementation_program.md`)
- ❌ Building the curriculum map (use `curric_residency_curriculum_mapper.md`)

## Inputs Required
- **Specialty and program identity** (PGY years, learner count, training sites)
- **ACGME Milestones version** for the specialty (with verbatim language)
- **Program mission and graduate profile**
- **Specialty-specific or program-specific competencies** beyond the standard six
- **Existing framework documentation** (if revising)

## Constraints

**Must:**
- Use ACGME's six core competencies as the top-level structure (do not rename or replace)
- Use specialty Milestones language verbatim (with verification flag)
- Add program-specific integrative competencies only as additions, not replacements
- Provide observable performance indicators for each sub-competency
- Address each core competency at all five Milestone progression levels (where applicable)
- Cite ACGME Common Program Requirements and specialty-specific Program Requirements

**Must Not:**
- Rename or replace the six ACGME core competencies
- Invent specialty Milestone language
- Conflate the six core competencies with sub-competencies (Milestones)
- Treat the framework as the full assessment system (assessment evidence is separate)
- Skip the program mission alignment

## Instructions

1. **Confirm inputs.** Echo specialty, Milestones version, mission, program-specific additions.

2. **State the six core competencies verbatim.**

   1. **Patient Care** — Compassionate, appropriate, effective patient care for the treatment of health problems and the promotion of health
   2. **Medical Knowledge** — About established and evolving biomedical, clinical, epidemiological, and social-behavioral sciences
   3. **Practice-Based Learning and Improvement** — Investigation and evaluation of patient care, appraisal and assimilation of scientific evidence, and improvements in patient care
   4. **Interpersonal and Communication Skills** — Effective information exchange and teaming with patients, families, and other health professionals
   5. **Professionalism** — Commitment to carrying out professional responsibilities, adherence to ethical principles, and sensitivity to a diverse patient population
   6. **Systems-Based Practice** — Awareness of and responsiveness to the larger context and system of health care, plus ability to call on system resources to provide optimal care

   (Cite ACGME Common Program Requirements for verbatim verification.)

3. **For each core competency, populate specialty sub-competencies (Milestones).**
   - Use the specialty's published Milestones document (cite version)
   - List each sub-competency with verbatim language and ACGME-assigned ID
   - Group sub-competencies by core competency

4. **For each sub-competency, provide observable performance indicators across the five levels.**
   - Level 1 (Critical Deficiencies / Foundational)
   - Level 2 (Advanced Beginner)
   - Level 3 (Competent)
   - Level 4 (Proficient / Aspirational)
   - Level 5 (Aspirational / Expert)
   - Use ACGME's published descriptors verbatim where available

5. **Add program-specific integrative competencies** (only if user requests).
   - These extend, not replace, the ACGME six
   - Examples: Health equity competence, Quality improvement leadership, Health systems research, Interprofessional team leadership
   - For each: definition, rationale, mapping to ACGME core competencies it crosses

6. **Map to program mission.**
   - For each core competency: how does the program emphasize this in alignment with mission?
   - Are program-specific integrative competencies aligned to mission?

7. **Address program-specific contexts.**
   - Underserved patient populations
   - Specific clinical environments (rural, urban, safety-net, etc.)
   - Research / scholarship emphasis
   - Global health / international rotations

8. **Audit framework.**

## Output Format

### Section 1: Framework Identity
- Specialty, program, Milestones version, mission

### Section 2: ACGME Six Core Competencies (Verbatim)

[Six competency statements with citation]

### Section 3: Specialty Sub-Competencies (Milestones) by Core Competency

**Patient Care:**

| Sub-Competency ID | Statement (verbatim) | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |
|---|---|---|---|---|---|---|

(Repeat for each core competency)

### Section 4: Program-Specific Integrative Competencies (if applicable)

| Program Competency | Definition | Rationale | Crosses ACGME Cores |
|---|---|---|---|

### Section 5: Mission Alignment

| Core Competency | Mission-Driven Emphasis | Curriculum Mechanism |
|---|---|---|

### Section 6: Program-Specific Contexts
- Patient populations
- Clinical environments
- Research/scholarship emphasis
- Other

### Section 7: Framework Audit

| Audit Question | Result |
|---|---|
| ACGME six core competencies preserved verbatim | Pass / Fail |
| Specialty Milestones language verbatim | Pass / Fail |
| Sub-competencies organized by core competency | Pass / Fail |
| Five levels addressed per sub-competency | Pass / Fail |
| Program-specific competencies are additions, not replacements | Pass / Fail |
| Mission alignment shown | Pass / Fail |

### Section 8: Verification Notes
- ACGME core competency language version
- Specialty Milestones version + date
- Items requiring source verification

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Renaming core competencies | ACGME structure is mandated | Preserve verbatim; add program-specific competencies as additions |
| Inventing Milestone language | Specialty Milestones are published documents | Use verbatim from specialty's current document |
| Mixing core competencies with sub-competencies | They operate at different levels | Sub-competencies live under core competencies |
| Treating five levels as PGY years | Levels are progression markers, not time-based | Most learners progress through levels at variable rates |
| Skipping mission alignment | Framework becomes disconnected from program identity | Show how program emphasizes each core in mission-driven ways |
| Generic level descriptors | Doesn't aid CCC decisions | Use specialty Milestones' specific descriptors |
| Confusing competencies with assessment | Framework defines what; assessment system measures it | Keep framework separate from assessment design |

## Verification Checklist

- [ ] Six core competencies preserved verbatim
- [ ] Specialty Milestones version cited
- [ ] All sub-competencies grouped by core competency
- [ ] Five levels per sub-competency
- [ ] Program-specific additions clearly marked
- [ ] Mission alignment shown
- [ ] Program-specific context addressed
- [ ] No invented ACGME or specialty language
