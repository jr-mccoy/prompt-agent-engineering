---
title: "Higher-Ed Accreditation Self-Study Builder (Parameterized by Regional Accreditor)"
category: education-teaching/accreditation-program-review
description: "Build a regional higher-ed accreditation self-study narrative — parameterized for HLC, MSCHE, SACSCOC, WSCUC, or NWCCU — translating institutional evidence into criterion-aligned response sections with strength/weakness assessment, evidence inventory, and quality-enhancement plan."
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
  - higher-ed
  - hlc
  - msche
  - sacscoc
  - wscuc
  - nwccu
  - regional-accreditation
updated: "2026-05-15"
related_prompts:
  - teaching_accreditation_self_study_programmatic.md
  - teaching_accreditation_evidence_compiler.md
  - teaching_program_review_cycle_designer.md
  - ../program-outcomes-assessment/teaching_program_gap_analysis.md
---

# Higher-Ed Accreditation Self-Study Builder

**Objective:** Build the institutional self-study narrative for a regional higher-ed accreditor — parameterized for HLC, MSCHE, SACSCOC, WSCUC, or NWCCU — translating institutional evidence into criterion-aligned response sections with strength/weakness assessment, evidence inventory cross-references, and a quality-enhancement / improvement plan.

## When to Use
- ✅ Preparing for an upcoming reaffirmation visit
- ✅ Drafting individual criterion-response sections of a self-study
- ✅ Auditing a draft self-study for criterion coverage and evidence sufficiency
- ✅ Building the response to a focused-visit or follow-up requirement
- ❌ Programmatic accreditation (use `teaching_accreditation_self_study_programmatic.md` — ABET, AACSB, CCNE, ACPE, etc.)
- ❌ Med-ed accreditation (use `teaching_accreditation_self_study_meded.md`)
- ❌ Compiling raw evidence without writing narrative (use `teaching_accreditation_evidence_compiler.md`)

## Inputs Required
- **Accreditor:** HLC / MSCHE / SACSCOC / WSCUC / NWCCU
- **Accreditor's current criteria version:** date / standards adoption year
- **Specific criteria or core components in scope:** which sections of the self-study are being drafted
- **Institutional identity:** type (R1/R2/M1/M2/D, community college, two-year, religious, etc.), control (public/private/nonprofit/for-profit), enrollment, sector
- **Evidence inventory:** institutional artifacts, data sources, policies, reports, prior accreditation cycles
- **Known gaps or focus areas** (from internal review, prior accreditor feedback, mock visits)
- **Submission deadline and review cycle**

## Constraints

**Must:**
- Honor the accreditor's actual criterion structure and language (cite for verification; do not paraphrase normative language)
- For each criterion response: a clear claim, evidence, analysis (how evidence supports claim), and reflection (strengths, areas for improvement)
- Cross-reference every claim to a specific evidence artifact (with the inventory ID, not just "as documented elsewhere")
- Address known gaps directly — do not paper over
- Use accreditor-appropriate tone (HLC's "Component" structure; MSCHE's "Standards and Requirements of Affiliation"; SACSCOC's "Principles of Accreditation" Sections; WSCUC's "Standards"; NWCCU's "Standards and Eligibility Requirements")
- Build a quality-enhancement / improvement plan with timelines, owners, measures

**Must Not:**
- Invent criterion text or core-component numbers; cite for verification
- Use vague "the institution demonstrates" without specific evidence
- Hide weaknesses (accreditors penalize discovered concealment more than acknowledged challenges)
- Generate text that exceeds page or word limits without flagging
- Cite evidence not in the supplied inventory
- Confuse one accreditor's structure with another's

## Instructions

1. **Confirm accreditor and version.** Echo: accreditor, criteria version, criteria in scope.

2. **For each criterion or core component being addressed:**

   a. **Restate the criterion language verbatim** (flag for verification — these change between adoption years).

   b. **Identify what evidence the criterion expects.** Each accreditor specifies expected evidence types or "required components."

   c. **Inventory available evidence from the user's supplied list.** Match to expected.

   d. **Write the response with this structure:**
      - **Claim:** What the institution does
      - **Evidence:** Specific artifacts (with inventory IDs)
      - **Analysis:** How evidence supports claim
      - **Reflection:** Strengths, areas for improvement, planned actions

   e. **Identify gaps** between expected evidence and inventory.

3. **Aggregate across criteria.**
   - Patterns: are weaknesses concentrated in one area (e.g., assessment of student learning, governance, financial)?
   - Cross-cutting themes the accreditor will surface

4. **Build the quality-enhancement / improvement plan.**
   - For each identified weakness: planned action, timeline, owner, measure
   - Tie to institutional strategic planning where possible

5. **Address known prior-cycle feedback** if provided.
   - Demonstrate response to prior recommendations / required follow-up

6. **Format for accreditor expectations.**
   - HLC: Assurance Argument with Component responses, evidence file references
   - MSCHE: Standards and Requirements of Affiliation responses, evidence inventory
   - SACSCOC: Compliance Certification + QEP (Quality Enhancement Plan)
   - WSCUC: Institutional Report aligned to Standards, Inventory of Educational Effectiveness Indicators
   - NWCCU: Mid-Cycle / Year-Seven Self-Evaluation aligned to Standards

7. **Length and word-limit checks.** Flag if sections exceed accreditor word/page limits.

## Output Format

### Section 1: Self-Study Identity
- Accreditor, criteria version, criteria in scope, institutional identity, deadline

### Section 2: Per-Criterion Response

For each criterion or core component:

**[Criterion Number]: [Criterion Title]**

*Criterion Language (verbatim — verify against current published version):*

> [criterion text]

*Expected Evidence Types* (per accreditor's guidelines):

- [evidence type 1]
- [evidence type 2]

*Response:*

**Claim:** [institutional claim of compliance]

**Evidence:** [specific artifacts with inventory IDs]

| Evidence Artifact | Inventory ID | Relevance |
|---|---|---|

**Analysis:** [how evidence supports claim]

**Reflection — Strengths:**
- [strength 1]
- [strength 2]

**Reflection — Areas for Improvement:**
- [area 1, with planned action]
- [area 2, with planned action]

**Gaps:** [any evidence the criterion expects that the inventory lacks]

### Section 3: Cross-Cutting Themes
- Patterns across criteria
- Areas of strength
- Areas of concern

### Section 4: Quality Enhancement / Improvement Plan

| Weakness Area | Planned Action | Owner | Timeline | Measure |
|---|---|---|---|---|

### Section 5: Response to Prior-Cycle Feedback (if applicable)

| Prior Recommendation | Action Taken | Evidence | Status |
|---|---|---|---|

### Section 6: Length / Format Audit

| Section | Word Count | Accreditor Limit | Status |
|---|---|---|---|

### Section 7: Verification Notes
- Criterion language requiring source verification
- Inventory items needing institutional confirmation
- Evidence cited that user should re-verify

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Paraphrasing criterion language | Accreditors use specific language; paraphrase introduces error | Quote verbatim with verification flag |
| "The institution demonstrates" without evidence | Empty assertion accreditors penalize | Specific evidence artifacts with IDs |
| Hiding weaknesses | Concealment is worse than acknowledgment | Acknowledge with planned action |
| Confusing accreditor structures | HLC ≠ MSCHE ≠ SACSCOC; structures are not interchangeable | Use the actual accreditor's structure |
| Citing evidence not in inventory | Manufactured evidence damages credibility | Only cite supplied inventory items |
| Exceeding word/page limits | Sections may be truncated or returned | Compute length; flag overages |
| Using last cycle's criteria version | Accreditors update; old versions misalign | Cite current published version with verification flag |
| Generic improvement plan | Vague plans don't address specific weaknesses | Action + owner + timeline + measure |

## Verification Checklist

- [ ] Accreditor and version specified
- [ ] Every criterion response has claim + evidence + analysis + reflection
- [ ] Evidence cross-referenced to inventory IDs
- [ ] Strengths AND areas for improvement named
- [ ] Gaps explicitly identified
- [ ] Quality-enhancement plan specific
- [ ] Prior-cycle feedback addressed (if applicable)
- [ ] Length/format checked against accreditor limits
- [ ] Criterion language flagged for verification
- [ ] No invented evidence or criterion text
