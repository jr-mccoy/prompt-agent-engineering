---
title: "Research-Methods Semester Syllabus Designer"
category: science/teaching-research-methods
description: "Build a semester research-methods syllabus aligned to a specific discipline and Open Science, with measurable outcomes, a week-by-week craft sequence, hands-on assignments (preregistration, reproduction), and a constructively-aligned outcome-to-assessment map."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - RT-03
  - QA-01
  - DS-02
difficulty: advanced
tags:
  - research-methods
  - syllabus-design
  - open-science
  - constructive-alignment
  - preregistration
  - reproducibility
  - assessment-map
  - graduate-education
updated: "2026-06-26"
related_prompts:
  - domain-science/teaching-research-methods/science_undergraduate_lab_course_designer.md
  - domain-science/teaching-research-methods/science_journal_club_facilitation_guide.md
  - domain-science/methods-foundations/science_research_question_refiner.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Research-Methods Semester Syllabus Designer

**Objective:** Produce a semester-length research-methods syllabus that teaches the actual craft of doing science in a named discipline — question formulation, design, power and sample size, preregistration, analysis, reproducibility, ethics, peer review, and communication — with Open Science woven in as the default rather than an add-on. Every topic maps to a measurable outcome and an assessment via constructive alignment, and the major assignments make students *practice* the craft (write a preregistration, reproduce a published result) rather than only read about it.

**When to use:** You are designing or revising a graduate or advanced-undergraduate research-methods course and want it grounded in your discipline's real practices and in current Open-Science norms, with assessment that actually measures the methodological skills you intend.

**Required inputs:**
- **Discipline.** Field and sub-area, and the dominant study type(s) (experimental, observational, computational, field, mixed).
- **Level / audience.** Graduate vs. advanced undergraduate, prior stats/methods background, program/lab context, class size.
- **Term structure.** Number of weeks, sessions/week, session length.

**Optional inputs:**
- **Program or accreditation outcomes** the course must satisfy.
- **Prerequisite courses** (especially statistics/programming) so topics aren't duplicated or assumed.
- **Tooling expectations** (R/Python, OSF, Git, reference manager) the program standardizes on.
- **A published paper or dataset** in-field to anchor the reproduction assignment.
- **Capstone / thesis pipeline** the course feeds, so the syllabus produces usable thesis preparation.

**Constraints — Must:**
- Tailor topics, examples, and study types to the named discipline; do not produce a generic, field-agnostic methods outline.
- Cover the research-craft spine: question formulation, design and controls, power/sample size, preregistration, analysis and inference, reproducibility, research ethics/integrity, peer review, and scientific communication.
- Make Open Science the default — preregistration, data/code sharing, transparent reporting, and reproducibility appear as recurring expectations, not a single isolated week.
- Include at least two craft-practice assignments where students *produce* methodological artifacts (e.g., a preregistration; a reproduction of a published result), not just summarize readings.
- State outcomes as measurable behaviors and constructively align each to topics and to a specific assessment via an explicit outcome-to-assessment map (Biggs).
- Cross-reference the relevant `domain-science/` prompts as the working tools behind topics and assignments rather than re-teaching their content.

**Constraints — Must Not:**
- Do not invent institutional/course requirements, papers, or citations the user hasn't supplied. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not assign specific named readings, textbooks, or datasets the user did not provide; use `[user-supplied: reading on X]` placeholders.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in any drafted syllabus, outcome, or assignment text.
- Do not present statistical procedures, reporting standards, or ethics rules as discipline-universal when they are field-specific; attribute them.
- Do not duplicate generic syllabus mechanics (grading policy boilerplate, late-work rules, accommodation statements) — note where `domain-education-teaching/` covers them and keep this output on research craft.

**Instructions:**

1. **Confirm discipline, level, and term.** Restate field, dominant study types, audience background, and the week/session structure. Note prerequisites so you neither assume nor duplicate stats/programming content.
2. **Write learning outcomes.** Draft 5-8 measurable outcomes covering the research-craft spine and Open-Science practice. Each must be assessable. (For outcome-wording mechanics, defer to `domain-education-teaching/`.)
3. **Sequence the weeks.** Order topics so skills compound: framing and questions → design and controls → power/sample size → preregistration → data collection/management → analysis and inference → reproducibility → ethics/integrity → peer review → communication. Map each week to the `domain-science/` prompt(s) that operationalize it (e.g., `science_research_question_refiner.md`, `science_reproducibility_self_audit.md`).
4. **Weave Open Science throughout.** Mark, across multiple weeks, where preregistration, transparent reporting, data/code sharing, and reproducibility recur as expectations and graded behaviors.
5. **Design craft-practice assignments.** Specify 2-4 assignments where students produce artifacts: at minimum a preregistration and a reproduction-of-a-published-result. Define deliverable, scope, and the rigor each assesses (pre-specification, controls, reproducibility, calibrated claims).
6. **Build the outcome-to-assessment map.** Create a table linking each outcome to the week(s) that teach it and the assessment(s) that measure it, confirming nothing is taught-but-untested or tested-but-untaught.
7. **Set assessment weighting and integrity expectations.** Specify how assignments, participation, and exams (if any) combine, and state authorship/data-integrity/AI-use expectations as research-integrity content (route generic academic-honesty boilerplate to `domain-education-teaching/`).
8. **Surface assumptions and gaps.** List `[user-supplied]` items (readings, datasets, program outcomes), assumptions made, and how the instructor will revise after the first run.

**Output format (locked):**

```
## Course Identity
- Discipline / dominant study types:
- Level / audience / prerequisites:
- Term structure (weeks, sessions/week, length):

## Learning Outcomes
| # | Outcome (measurable) | Craft area | Open-Science element |
|---|---|---|---|

## Week-by-Week Schedule
| Week | Topic | Research-craft focus | Open-Science / rigor expectation | domain-science prompt(s) referenced | In-class / homework |
|---|---|---|---|---|---|

## Craft-Practice Assignments
| Assignment | Artifact produced | What it makes students do | Rigor assessed | Aligned outcome(s) |
|---|---|---|---|---|
[Must include a preregistration and a reproduction-of-a-result]

## Outcome-to-Assessment Map
| Outcome | Taught in week(s) | Assessed by | Weight |
|---|---|---|---|

## Assessment & Research-Integrity Expectations
- Weighting summary:
- Authorship / data integrity / AI-use (as research-integrity content):
- [Generic academic-policy boilerplate → see domain-education-teaching/]

## Assumptions & [user-supplied] Items
- Readings / datasets / program outcomes to supply:
- Assumptions made:
- Post-run revision plan:
```

**Reporting-standard alignment:** No formal reporting standard; aligns to constructive alignment (Biggs), Open-Science pedagogy (preregistration, FAIR data/code sharing, transparent reporting), and backward design. Discipline-specific reporting standards (e.g., field-appropriate guidelines) are attributed, never asserted as universal.

**Verification checklist (before delivering):**
- [ ] Topics and examples are tailored to the named discipline, not generic.
- [ ] The research-craft spine is fully covered (question → design → power → prereg → analysis → reproducibility → ethics → peer review → communication).
- [ ] Open Science recurs across multiple weeks as a graded expectation, not one isolated topic.
- [ ] At least two assignments produce methodological artifacts, including a preregistration and a reproduction.
- [ ] Every outcome is measurable and appears in the outcome-to-assessment map (taught and tested).
- [ ] Relevant `domain-science/` prompts are referenced as the working tools, not re-taught.
- [ ] No fabricated readings, datasets, papers, citations, or requirements; placeholders marked `[user-supplied]`.
- [ ] No banned hype terms in any drafted syllabus language.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Generic methods course | A polished syllabus that could belong to any field | Require discipline-specific study types, examples, and reporting norms |
| Open Science as a token week | One "Open Science" lecture, otherwise traditional | Mark recurring prereg/sharing/reproducibility expectations across weeks |
| Read-about vs. do | Assignments are reading summaries, not artifacts | Mandate a preregistration and a reproduction students actually produce |
| Alignment gap | Outcomes and assessments listed separately, never reconciled | Enforce the outcome-to-assessment map; flag taught-but-untested items |
| Invented readings | Plausible textbook/paper names filled in to look complete | Use `[user-supplied]` placeholders; never assert a specific source |
| Stats duplication/assumption | Re-teaching or silently assuming a prerequisite stats course | Confirm prerequisites up front; scope analysis topics accordingly |
