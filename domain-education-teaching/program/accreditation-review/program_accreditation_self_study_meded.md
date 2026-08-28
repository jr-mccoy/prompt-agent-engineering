---
title: "Medical Education Accreditation Self-Study Builder (Parameterized)"
category: education-teaching/program/accreditation-review
description: "Build a med-ed program self-study — parameterized for LCME, ACGME, COCA, or CODA — translating program evidence into element-aligned response sections with CQI data, learner outcomes, faculty/resource adequacy, and action plan."
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
  - medical-education
  - lcme
  - acgme
  - coca
  - coda
  - cqi
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/program/accreditation-review/program_accreditation_self_study_he.md
  - domain-education-teaching/program/accreditation-review/program_accreditation_self_study_programmatic.md
  - domain-education-teaching/program/accreditation-review/program_accreditation_evidence_compiler.md
  - domain-medical-education/educator-curriculum-design/curric_cbme_implementation_program.md
---

# Medical Education Accreditation Self-Study Builder

**Objective:** Build the program self-study for a medical / health-professions education accreditor — parameterized for LCME (MD-granting medical schools), ACGME (residency / fellowship programs), COCA (DO-granting medical schools), or CODA (dental education) — translating program evidence into element-aligned response sections with continuous-quality-improvement (CQI) data, learner outcomes, faculty / resource adequacy, and action plan.

## When to Use
- ✅ LCME self-study (Independent Student Analysis + Medical Education Program Self-Study)
- ✅ ACGME ADS update, self-study, or 10-Year Self-Study with Site Visit
- ✅ COCA pre-accreditation or reaffirmation
- ✅ CODA self-study for dental programs
- ✅ Specialty board accreditation if structured similarly
- ❌ Regional HE accreditation (use `teaching_accreditation_self_study_he.md`)
- ❌ Programmatic non-med accreditation (use `teaching_accreditation_self_study_programmatic.md`)

## Inputs Required
- **Accreditor:** LCME / ACGME / COCA / CODA / specialty board
- **Accreditor's current standards/elements version**
- **Program identity:** degree/certificate granted, program type (MD/DO/dental/residency specialty), class size, year of program
- **Elements/standards in scope**
- **Learner outcomes data:** USMLE/COMLEX/board pass rates, milestone achievement, match data, attrition, graduate practice patterns
- **Faculty data:** faculty count, faculty-to-learner ratios, faculty development activity
- **Curriculum and assessment evidence:** curriculum management, assessment system, milestone evaluations, EPA implementation status
- **Educational program quality data:** clerkship comparability, simulation use, longitudinal experiences, well-being initiatives
- **Resource adequacy data:** library, technology, clinical sites, financial
- **CQI process documentation:** Program Evaluation Committee (ACGME) or Curriculum Committee (LCME) minutes, action histories
- **Prior accreditor feedback**

## Constraints

**Must:**
- Use the accreditor's actual element/standard numbering and language verbatim (verification flag)
- Distinguish element-by-element required content (ACGME's annual ADS update vs. self-study narrative; LCME's Data Collection Instrument standards)
- Provide multi-year trend data (3-5 years typical)
- Show CQI / continuous improvement loops with action → measure → result
- Address learner mistreatment, well-being, DEI as standalone elements where required
- Address differential outcomes by demographic subgroups (LCME and ACGME both require)
- Honor specific program-level requirements (ACGME Program Requirements for the specialty)

**Must Not:**
- Invent element/standard text
- Treat hospital-level evidence as program-level (ACGME distinguishes clearly)
- Skip the differential-outcomes analysis (this has been a focus area)
- Generate responses without CQI evidence
- Conflate ACGME ADS update content with self-study narrative content
- Cite evidence not in the supplied inventory

## Instructions

1. **Confirm accreditor and version.** Echo: accreditor, element/standard version, elements in scope, program identity.

2. **For each element/standard:**

   a. **Quote element language verbatim** (verification flag).

   b. **Identify required evidence:**
      - LCME: comparability data across instructional sites, outcomes data, ISA data, curriculum management
      - ACGME: educational program elements, scholarly activity, well-being, evaluations, milestones, faculty supervision
      - COCA: similar to LCME with osteopathic-specific elements
      - CODA: dental-specific clinical and didactic standards

   c. **Build the response:**
      - **Compliance Statement:** Concise statement of how program meets element
      - **Evidence:** Specific artifacts, data with multi-year trends
      - **Analysis:** How evidence supports compliance
      - **CQI Activity:** Recent actions, measures, results
      - **Areas for Improvement:** Honest acknowledgment
      - **Action Plan:** For ongoing development

3. **Build the learner outcomes evidence tables.**
   - Board exam pass rates (3-5 years)
   - Match data (for MD/DO programs)
   - Milestone achievement (for ACGME)
   - Attrition / remediation rates
   - Graduate practice or further training data

4. **Build the differential outcomes analysis.**
   - Disaggregate by URiM, sex, age, IMG status, other relevant subgroups
   - Identify any gaps; show planned response

5. **Build the faculty evidence.**
   - Faculty-to-learner ratios
   - Faculty development participation
   - Scholarly activity (for academic accreditors)
   - Faculty diversity

6. **Build the CQI narrative.**
   - Show the loop: identified concern → action → measurement → result
   - For ACGME PEC: minutes, action items, follow-through evidence
   - For LCME Curriculum Committee: comparability monitoring, action history

7. **Address well-being, mistreatment, DEI as separate elements** (per accreditor requirements).

8. **Build the action plan.**

## Output Format

### Section 1: Self-Study Identity
- Accreditor, version, program type, degree, class size, elements in scope

### Section 2: Per-Element Response

**Element [N]: [Title]**

*Verbatim element language (verify):*

> [text]

*Required Evidence Types:*

[per accreditor]

*Response:*

| Element | Content |
|---|---|
| Compliance Statement | |
| Evidence | |
| Analysis | |
| CQI Activity | |
| Areas for Improvement | |
| Action Plan | |

### Section 3: Learner Outcomes Trends (multi-year)

| Outcome | Year N-4 | Year N-3 | Year N-2 | Year N-1 | Year N | Target | Status |
|---|---|---|---|---|---|---|---|

### Section 4: Differential Outcomes Analysis

| Outcome | Overall | URiM | Non-URiM | Other Subgroups | Gap? | Action |
|---|---|---|---|---|---|---|

### Section 5: Faculty Evidence

| Metric | Value | Benchmark | Status |
|---|---|---|---|

### Section 6: CQI Narrative
- Recent closed loops with evidence

### Section 7: Well-Being / Mistreatment / DEI Elements (per accreditor)

### Section 8: Action Plan

| Identified Area | Action | Owner | Timeline | Measure |
|---|---|---|---|---|

### Section 9: Response to Prior Feedback

### Section 10: Verification Notes

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Hospital-level data as program-level evidence | ACGME distinguishes clearly | Use program-specific data only |
| Skipping differential outcomes | Required focus area; missing it triggers findings | Disaggregate and report honestly |
| Single-year outcomes data | Trend data required | Multi-year tables |
| CQI without closed loops | Most-scrutinized section | Show action → measure → result |
| ACGME ADS content in self-study (or vice versa) | Different documents serve different functions | Match content to document |
| Generic well-being statement | Accreditors expect specific systems | Show program-specific well-being structures, monitoring |
| Confusing milestone levels with PGY levels | Milestones are competency levels; PGY is time-based | Use milestone language correctly |
| Skipping mistreatment data | Required reporting; concealment is worse than disclosure | Honest reporting with response plan |

## Verification Checklist

- [ ] Accreditor and version specified
- [ ] Every element response: compliance + evidence + analysis + CQI + improvement
- [ ] Multi-year outcomes trends
- [ ] Differential outcomes analysis
- [ ] Faculty evidence per accreditor metrics
- [ ] CQI closed loops shown
- [ ] Well-being / mistreatment / DEI addressed
- [ ] Action plan specific
- [ ] Prior-cycle feedback addressed
- [ ] No invented element text
