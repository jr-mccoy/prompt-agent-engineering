---
title: "Accreditation Evidence Compiler (Criteria + Raw Evidence → Response Drafts)"
category: education-teaching/accreditation-program-review
description: "Compile response narratives from accreditation criteria + raw evidence inputs — translating unstructured policies, reports, and data into accreditor-aligned response sections with evidence cross-references and gap surfacing."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - QA-01
  - QA-02
difficulty: advanced
tags:
  - education
  - accreditation
  - evidence-compilation
  - self-study
  - higher-ed
  - workforce
  - medical-education
updated: "2026-05-15"
related_prompts:
  - teaching_accreditation_self_study_he.md
  - teaching_accreditation_self_study_programmatic.md
  - teaching_accreditation_self_study_meded.md
  - teaching_program_review_cycle_designer.md
---

# Accreditation Evidence Compiler

**Objective:** Compile accreditation response narratives from raw evidence inputs — policies, data tables, reports, committee minutes, syllabi, assessment results — and a criterion or standard. Translate unstructured material into criterion-aligned narrative sections with explicit evidence cross-references, gap identification, and a follow-up data-request list for missing items.

## When to Use
- ✅ Drafting an individual criterion response from a stack of evidence
- ✅ Compiling a narrative for a single standard with multiple evidence sources
- ✅ Auditing whether supplied evidence supports a draft narrative
- ✅ Identifying what evidence is missing for a criterion
- ❌ Building the full self-study from scratch (use the self-study builders)
- ❌ Designing the review cycle (use the program review cycle designer)

## Inputs Required
- **Criterion / standard text** (verbatim, with version)
- **Evidence inventory:** list of artifacts with brief descriptions (policies, reports, syllabi, data tables, meeting minutes)
- **Expected evidence types** per accreditor guidance
- **Length / format constraints**
- **Existing draft narrative** (optional) if compiling for revision rather than initial draft

## Constraints

**Must:**
- Map each claim in the narrative to a specific evidence artifact
- Flag claims without supporting evidence as "evidence needed"
- Quote criterion verbatim
- Honor accreditor's expected response structure
- Surface gaps explicitly (do not paper over)
- Distinguish supplied evidence from inferred or aspirational claims

**Must Not:**
- Invent evidence not in the supplied inventory
- Quote evidence inaccurately
- Generate claims that supplied evidence does not support
- Skip the gaps list
- Substitute one accreditor's structure for another

## Instructions

1. **Confirm criterion and evidence inventory.** Echo back both.

2. **For each claim that the criterion expects to be made:**
   - Identify which evidence artifact(s) support it
   - Quote or paraphrase the relevant portion (with citation)
   - If no evidence supports the claim: flag as gap, recommend evidence type to gather

3. **Build the response narrative.**
   - Use the accreditor's expected structure
   - Embed evidence references (artifact IDs)
   - Maintain clear distinction between strengths and areas needing improvement

4. **Build the cross-reference table.**
   - Every claim → evidence artifact(s)

5. **Build the gap / follow-up list.**
   - Claims that should be made but lack evidence
   - Specific evidence to gather: data type, source, timeline

6. **Audit the draft.**
   - Every claim has citation
   - Inferred claims explicitly flagged
   - Gaps surfaced

## Output Format

### Section 1: Compilation Identity
- Criterion, accreditor, version, evidence inventory count, draft type (initial / revision)

### Section 2: Criterion Statement
> [verbatim text with version reference]

### Section 3: Response Narrative

[Drafted response, with evidence references inline: e.g., "(Evidence ID: POL-12, Faculty Handbook §3.4)"]

### Section 4: Evidence Cross-Reference Table

| Claim in Narrative | Evidence Artifact (ID) | Specific Section / Data |
|---|---|---|

### Section 5: Gaps & Follow-Up Data Requests

| Claim Needed | Evidence Type Needed | Source | Timeline |
|---|---|---|---|

### Section 6: Inferred / Aspirational Claims (flagged)

| Claim | Why It's Inferred | Evidence Needed to Substantiate |
|---|---|---|

### Section 7: Length / Format Check

| Section | Word Count | Limit | Status |
|---|---|---|---|

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Generating claims not in evidence | Damages credibility; risks misrepresentation | Cite supplied evidence only |
| Hiding gaps | Accreditors find gaps anyway | Surface explicitly with follow-up data request |
| Vague citations | Reviewers can't verify | Specific section / page / data point |
| Paraphrasing criterion language | Introduces error | Quote verbatim |
| Confusing inferred with evidenced | Inflates apparent compliance | Tag inferred claims distinctly |
| Substituting different accreditor structure | Mismatch with what reviewer expects | Honor specific accreditor's response structure |

## Verification Checklist

- [ ] Criterion quoted verbatim with version
- [ ] Every claim has evidence citation
- [ ] Inferred claims tagged
- [ ] Gaps explicitly listed with follow-up data request
- [ ] Accreditor structure honored
- [ ] Length within limits
