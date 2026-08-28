---
title: "Program Gap Analysis (Taught vs. Required Coverage)"
category: education-teaching/program/outcomes-assessment
description: "Diagnose gaps between what a program currently delivers and what is required (by standards, accreditor, employer demand, or stated outcomes) — producing a severity-ranked gap table with root-cause hypotheses and fill plans."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - QA-02
  - DS-02
difficulty: advanced
tags:
  - education
  - program-evaluation
  - gap-analysis
  - audit
  - accreditation
  - k12
  - higher-ed
  - workforce
  - medical-education
updated: "2026-05-15"
related_prompts:
  - ../curriculum-design/teaching_standards_alignment_audit.md
  - ../curriculum-design/teaching_curriculum_map_builder.md
  - domain-education-teaching/program/outcomes-assessment/program_outcomes_to_assessment_mapper.md
  - ../accreditation-program-review/teaching_program_review_cycle_designer.md
---

# Program Gap Analysis

**Objective:** Diagnose gaps between what a program currently delivers and what is required — by standards, accreditor, employer/labor market, program-stated outcomes, or learner-need data. Produce a severity-ranked gap table with root-cause hypotheses, fill-plan options, and an implementation sequence.

## When to Use
- ✅ Preparing for accreditation self-study (gap analysis informs the action plan)
- ✅ Post program review when a gap was named but not specified
- ✅ After standards revision (new standards arrived; what gaps emerged?)
- ✅ Employer-feedback-driven review (employers report graduates lack X)
- ✅ Equity audit (gap between intended and experienced curriculum for sub-populations)
- ❌ Auditing alignment to a single standards framework (use `teaching_standards_alignment_audit.md`)
- ❌ Identifying coverage in a curriculum map (use `teaching_curriculum_map_builder.md`)

## Inputs Required
- **Program identity**
- **Reference (what should be delivered):** standards, accreditor criteria, employer-demand data, stated outcomes, learner-need data
- **Current state (what is delivered):** curriculum artifacts, assessment evidence, course descriptions, graduation data
- **Sub-populations of concern** (optional): equity audit framing
- **Gap-analysis purpose:** accreditation / continuous improvement / employer-response / equity

## Constraints

**Must:**
- Specify the reference precisely (which standards, which version, which employer survey, which labor-market source)
- Distinguish gap types: **content gap** (topic not taught), **depth gap** (taught but not mastered), **evidence gap** (claimed taught but no evidence), **equity gap** (delivered unevenly across populations), **alignment gap** (taught but not connected to outcomes), **modality gap** (available in one modality, demanded in another)
- Rank by severity: high (blocks accreditation, employability, or equity) / medium / low
- Hypothesize root cause (curriculum, staffing, materials, scheduling, assessment, policy)
- Propose fill plans with cost/effort estimate

**Must Not:**
- Treat every difference as a gap (some differences are intentional scope decisions)
- Use anecdotes as evidence (require data or named source)
- Recommend "more rigor" without specifics
- Confuse desire-state with requirement (stakeholder wishes ≠ accreditor requirements)

## Instructions

1. **Confirm reference and scope.** Echo what counts as the required-state and the source.

2. **Inventory current state.** From curriculum artifacts, list what is delivered.

3. **Compare reference to current state.** For each required element:
   - Delivered? (yes / partial / no)
   - Evidence of delivery (cited artifact)
   - Depth (Introduced / Developed / Mastered)
   - Coverage across populations (uniform / uneven)

4. **Classify gaps.** Tag each gap with the gap type(s).

5. **Hypothesize root cause.** For each gap, name the most likely structural cause and the evidence supporting that hypothesis.

6. **Rank by severity.**
   - High: blocks accreditation, licensure pass, employability, equity commitment
   - Medium: limits program quality but not blocking
   - Low: aspirational improvement

7. **Propose fill plans.** For each gap, 1-3 options ranging from minimal-cost to comprehensive.

8. **Sequence implementation.** Recommended order considering dependencies, cost, and timeline.

## Output Format

### Section 1: Analysis Identity
- Program, reference source(s), current-state artifacts, sub-populations in scope, purpose

### Section 2: Gap Inventory

| # | Required Element | Reference Source | Currently Delivered? | Evidence | Depth | Population Coverage | Gap Type(s) | Severity |
|---|---|---|---|---|---|---|---|---|

### Section 3: Root-Cause Hypotheses

| Gap # | Hypothesized Cause | Supporting Evidence |
|---|---|---|

### Section 4: Fill Plans

For each gap (especially High-severity):

**Gap #[N]: [name]**

| Option | Description | Cost/Effort | Time to Implement | Trade-offs |
|---|---|---|---|---|
| Minimal | | | | |
| Moderate | | | | |
| Comprehensive | | | | |

**Recommended:** [Option, with rationale]

### Section 5: Implementation Sequence

| Sequence | Gap # | Action | Dependencies | Estimated Completion |
|---|---|---|---|---|

### Section 6: Verification Notes
- Inferred items
- Items requiring data collection before fill plan finalization

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Treating every program variance from reference as a gap | Some variance is intentional scope decision | Verify with program: is this a gap or a design choice? |
| Using anecdote as evidence | Single complaint ≠ systemic gap | Require pattern data or named source |
| Recommending "improve rigor" | Unactionable | Specify what to add, where, at what depth, measured how |
| Single fill plan per gap | Leaders need options at different cost points | Provide minimal/moderate/comprehensive options |
| Ignoring equity dimension | A program may deliver well on average but unevenly across populations | Always check coverage across sub-populations |
| Confusing accreditor "expectations" with "requirements" | Accreditors distinguish required vs. recommended | Tag severity based on actual requirement language |
| Ignoring dependencies in sequencing | Some fixes require predecessor fixes | Build sequence respecting dependencies |

## Verification Checklist

- [ ] Reference precisely specified
- [ ] Current-state inventory based on artifacts (not assumption)
- [ ] Every gap tagged with type(s)
- [ ] Severity ranked with reasoning
- [ ] Root cause hypothesized with evidence
- [ ] Fill plans offer multiple options
- [ ] Implementation sequence respects dependencies
- [ ] Equity dimension assessed
- [ ] Verification notes flag inferences
