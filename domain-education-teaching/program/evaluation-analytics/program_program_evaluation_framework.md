---
title: "Program Evaluation Framework Designer (Parameterized: Kirkpatrick / CIPP / Logic Model / Theory of Change)"
category: education-teaching/program/evaluation-analytics
description: "Design a program evaluation framework — parameterized by approach (Kirkpatrick four-level / CIPP / logic model / theory of change / utilization-focused) — with evaluation questions, indicators, methods, data sources, timeline, and reporting plan."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - education
  - program-evaluation
  - kirkpatrick
  - cipp
  - logic-model
  - theory-of-change
  - higher-ed
  - workforce
  - k12
  - medical-education
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/program/evaluation-analytics/program_logic_model_designer.md
  - domain-education-teaching/program/evaluation-analytics/program_continuous_improvement_cycle.md
  - domain-education-teaching/program/outcomes-assessment/program_program_gap_analysis.md
  - domain-education-teaching/program/accreditation-review/program_program_review_cycle_designer.md
---

# Program Evaluation Framework Designer

**Objective:** Design a complete program-evaluation framework — parameterized by approach: Kirkpatrick four-level / Stufflebeam CIPP (Context, Input, Process, Product) / logic-model / theory of change / utilization-focused evaluation — with evaluation questions, indicators, methods, data sources, timeline, ethics considerations, and reporting plan.

## When to Use
- ✅ Evaluating a new educational, training, or workforce program
- ✅ Designing the evaluation plan for grant-funded initiatives
- ✅ Building the evaluation infrastructure for continuous improvement
- ✅ Designing summative + formative evaluation for accreditation evidence
- ❌ Building a logic model only (use `teaching_logic_model_designer.md`)
- ❌ Designing a PDSA / continuous improvement cycle (use `teaching_continuous_improvement_cycle.md`)

## Inputs Required
- **Program identity** and goals
- **Evaluation approach** (Kirkpatrick / CIPP / logic model / theory of change / utilization-focused / hybrid)
- **Evaluation purpose:** formative (improvement) / summative (judgment) / both
- **Primary intended users** of the evaluation (program staff, funders, accreditors, board)
- **Available resources** (evaluator FTE, budget, data infrastructure)
- **Timeline:** annual cycle / project-length / multi-year
- **Ethics frame:** IRB, consent, data privacy

## Constraints

**Must:**
- Specify evaluation questions before methods
- For Kirkpatrick: design across all four levels (Reaction, Learning, Behavior, Results) — note typical Levels 3-4 underuse
- For CIPP: address Context, Input, Process, and Product dimensions
- For logic model: link inputs → activities → outputs → short/mid/long outcomes
- For theory of change: surface assumptions linking activities to long-term outcomes
- Pair every question with method, data source, and analysis approach
- Include utilization plan (who uses results, how, when)
- Address ethics (consent, privacy, equity-of-data)

**Must Not:**
- Use methods without justifying them against questions
- Default to surveys when other methods would produce stronger evidence
- Skip Kirkpatrick Levels 3-4 (behavior change, results) without explanation
- Generate evaluation that won't be used
- Skip equity dimension in indicators or sampling

## Instructions

1. **Confirm inputs.** Echo program, approach, purpose, users, resources, timeline.

2. **Structure by chosen approach:**

   **Kirkpatrick** (4 levels):
   - Level 1 — Reaction: participant satisfaction, engagement
   - Level 2 — Learning: knowledge, skills, attitudes acquired
   - Level 3 — Behavior: application in real context post-program
   - Level 4 — Results: organizational / system / learner outcomes

   **CIPP**:
   - Context: needs, problems, opportunities, assets
   - Input: program design, resources, plans
   - Process: implementation fidelity, quality
   - Product: outputs, outcomes, impacts

   **Logic model**:
   - Inputs → Activities → Outputs → Short-term outcomes → Mid-term outcomes → Long-term outcomes / impact
   - Plus assumptions and external factors

   **Theory of change**:
   - Long-term outcome / goal
   - Preconditions (must-be-true)
   - Pathway of change (causal logic)
   - Indicators and assumptions

3. **For each evaluation question, specify:**
   - Question
   - Indicator
   - Method (survey, interview, observation, document analysis, administrative data, performance assessment)
   - Data source
   - Sampling
   - Analysis approach
   - Threshold for "good enough"

4. **Build the timeline.**
   - When data collection occurs
   - When analysis
   - When reporting
   - When use

5. **Plan utilization.**
   - Who uses results
   - How decisions get made
   - What format and timing for reports
   - How findings feed continuous improvement

6. **Address ethics.**
   - Consent process
   - Privacy and confidentiality
   - Equity in sampling and reporting
   - IRB review status
   - Conflict of interest

7. **Audit.**

## Output Format

### Section 1: Framework Identity
- Program, approach, purpose, primary users, resources, timeline

### Section 2: Approach-Specific Structure

[Depending on approach — Kirkpatrick / CIPP / logic model / theory of change layout]

### Section 3: Evaluation Questions × Methods Matrix

| Question | Indicator | Method | Data Source | Sampling | Analysis | Threshold |
|---|---|---|---|---|---|---|

### Section 4: Timeline

| Phase | Timing | Activities | Owner |
|---|---|---|---|

### Section 5: Utilization Plan
- Users
- Decision-making process
- Report format and cadence
- Connection to continuous improvement

### Section 6: Ethics
- Consent
- Privacy / data security
- Equity considerations
- IRB / oversight

### Section 7: Resource Plan

| Resource | Required | Available | Status |
|---|---|---|---|

### Section 8: Framework Audit

| Audit Question | Result |
|---|---|
| Questions specified before methods | Pass / Fail |
| Methods justified by questions | Pass / Fail |
| Kirkpatrick Levels 3-4 addressed (if K) | Pass / Fail |
| Indicators measurable | Pass / Fail |
| Utilization plan present | Pass / Fail |
| Ethics addressed | Pass / Fail |
| Equity dimension included | Pass / Fail |

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Methods first, questions later | Wastes data collection | Always: question → method |
| Kirkpatrick stops at Level 2 | Misses real impact | Plan Levels 3-4 explicitly |
| Survey defaults | Limited evidence for complex outcomes | Match method to question; use mixed methods |
| Evaluation no one will use | Wasted effort | Build utilization plan; involve users in design |
| Skipping equity | Hides disparate impact | Disaggregate indicators by relevant subgroups |
| No ethics review | Risks privacy / consent harm | Build ethics plan; verify IRB status |
| Vague thresholds | Can't tell success from failure | Specify what counts as evidence of success |

## Verification Checklist

- [ ] Approach selected and structure honored
- [ ] Evaluation questions specified first
- [ ] Every question paired with method, source, analysis, threshold
- [ ] Timeline with phases
- [ ] Utilization plan with users
- [ ] Ethics addressed
- [ ] Equity dimension built in
- [ ] Resource plan realistic
