---
title: "Undergraduate Authentic-Research Lab Course Designer"
category: science/teaching-research-methods
description: "Design a CURE-style undergraduate lab course built on an open research question and real measurement, with aligned learning outcomes, a skill-building weekly arc, and a calibrated process-plus-product rubric that credits negative results."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - QA-02
  - DS-02
difficulty: advanced
tags:
  - cure
  - authentic-research
  - lab-course-design
  - constructive-alignment
  - assessment-rubric
  - reproducibility
  - open-science
  - undergraduate
updated: "2026-06-26"
related_prompts:
  - domain-science/teaching-research-methods/science_research_methods_syllabus_designer.md
  - domain-science/teaching-research-methods/science_journal_club_facilitation_guide.md
  - domain-science/methods-foundations/science_research_question_refiner.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Undergraduate Authentic-Research Lab Course Designer

**Objective:** Convert a teaching goal into a Course-based Undergraduate Research Experience (CURE): a lab course organized around a genuinely open question with an unknown answer, real measurement on real samples, and meaningful student ownership — not a cookbook verification lab. The design ties learning outcomes, a skill-building weekly sequence, embedded reproducibility practices, and a calibrated rubric together through constructive alignment, so what students do, what they learn, and how they are graded all point at the same target.

**When to use:** You are designing or redesigning an undergraduate (or advanced-secondary) laboratory course and want students to do authentic research — generating data whose outcome neither they nor you know in advance — rather than reproducing a textbook result.

**Required inputs:**
- **Discipline.** The scientific field and sub-area (e.g., molecular biology, analytical chemistry, condensed-matter physics, freshwater ecology).
- **Level / audience.** Year, prior coursework, prior lab/quant experience, class size, and whether students work solo or in teams.
- **Open research question or theme.** The unknown-answer question or research thread the course will investigate. If absent, the prompt will help scope one but will not invent a specific scientific claim.
- **Course logistics.** Weeks, contact hours/week, and whether the course is a standalone lab or paired with a lecture.

**Optional inputs:**
- **Available instrumentation, reagents, samples, datasets, compute.**
- **Institutional/program learning outcomes or accreditation language** the course must map to.
- **Safety/biosafety/IRB/IACUC/field-permit context.**
- **TA/instructor support ratio** and budget constraints.
- **A reference dataset or prior cohort's data** for reproduction/calibration exercises.

**Constraints — Must:**
- Anchor the design to a question whose answer is genuinely unknown to instructor and students (the defining feature of a CURE), or explicitly help the user scope one before proceeding.
- State every learning outcome as an observable, assessable student behavior and align each outcome to at least one activity and one rubric criterion (constructive alignment, Biggs).
- Embed research rigor as taught content: at minimum controls, replication, pre-specification of what counts as a result, calibration of instruments, and a reproducibility practice (lab notebook / data-management plan / shareable analysis).
- Make the assessment rubric reward sound *process and reasoning*, including correctly executed studies that yield negative or null results, so students are not incentivized to fabricate or p-hack toward a "positive" finding.
- Include a feasibility and safety pass (time, cost, instrument access, hazard, ethics/permits) that flags anything the user must confirm.
- Use calibrated language in all drafted student-facing and outcome text.

**Constraints — Must Not:**
- Do not invent institutional/course requirements, papers, or citations the user hasn't supplied. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not assert a specific scientific result, dataset, instrument capability, or reagent availability the user did not provide.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in any drafted course materials, outcomes, or rubric language.
- Do not design a verification/cookbook lab and relabel it a CURE; if the question has a known textbook answer, say so and propose how to open it.
- Do not duplicate generic pedagogy mechanics (writing measurable objectives, rubric grain-size, grading logistics) — reference `domain-education-teaching/` for those and keep this output focused on research-craft content.

**Instructions:**

1. **Confirm discipline, level, and the open question.** Restate the field, audience, and the unknown-answer question. If the supplied question has a known answer or no measurable outcome, flag it and propose 2-3 ways to make it genuinely open (new system, new variable, new sample set, replication-under-variation). Cross-reference `domain-science/methods-foundations/science_research_question_refiner.md` for scoping.
2. **Set learning outcomes.** Write 4-7 outcomes spanning conceptual understanding, technical skill, research reasoning (design, controls, uncertainty), reproducibility/data practice, and scientific communication. Each must be observable and assessable. (For the mechanics of outcome wording, defer to `domain-education-teaching/`.)
3. **Map the authentic-research arc.** Lay out the progression from scaffolded skill-building to student-owned investigation: technique onboarding → guided practice with known controls → student-designed sub-question → data collection → analysis → communication. Show where ownership transfers to students.
4. **Embed rigor as content.** For the arc, specify where students learn and apply: controls and blanks, replication and sample size, calibration, pre-specification of the analysis/criterion *before* seeing results, and confound awareness. Tie each to a week.
5. **Build reproducibility in.** Specify the notebook standard, raw-data retention, a simple data-management expectation, and at least one cross-team or cross-cohort reproduction/comparison activity. Reference `domain-science/methods-foundations/science_reproducibility_self_audit.md`.
6. **Design the assessment.** Create a rubric covering both process (design quality, execution, notebook/data integrity, reasoning, collaboration) and product (analysis, interpretation, communication). Explicitly credit correctly run studies with null/negative/inconclusive results. Calibrate each criterion with concrete level descriptors and align every criterion to an outcome.
7. **Run feasibility and safety.** Pressure-test against contact hours, cost, instrument/sample access, hazards, and ethics/permits (IRB/IACUC/biosafety/field). List blockers and `[user-supplied]` confirmations needed.
8. **Plan the weekly schedule.** Produce a week-by-week table (topic, student activity, rigor/reproducibility focus, assessed artifact) consistent with the arc and logistics.
9. **Surface assumptions and iteration hooks.** List what you assumed, what the user must confirm, and how the instructor will collect feedback to revise the next offering.

**Output format (locked):**

```
## Course Overview
- Discipline / level / audience:
- Open research question (and why its answer is genuinely unknown):
- Format & logistics (weeks, hours/week, team structure):

## Learning Outcomes
| # | Outcome (observable) | Category | Aligned activity | Aligned rubric criterion |
|---|---|---|---|---|

## Authentic-Research Arc
[Phase-by-phase progression from scaffolded skills to student-owned investigation; mark the ownership-transfer point]

## Embedded Rigor & Reproducibility Plan
- Controls / replication / sample size:
- Calibration:
- Pre-specification (criterion-before-results):
- Notebook & data-management standard:
- Reproduction / cross-team comparison activity:

## Weekly Schedule
| Week | Topic | Student activity | Rigor / reproducibility focus | Assessed artifact |
|---|---|---|---|---|

## Assessment Rubric (calibrated)
| Criterion | Aligned outcome | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|---|
[Include an explicit criterion or note crediting correctly executed null/negative/inconclusive results]

## Feasibility & Safety Check
- Time / cost / instrument & sample access:
- Hazards / ethics / permits (IRB / IACUC / biosafety / field):
- Blockers and [user-supplied] confirmations needed:

## Assumptions, Open Questions & Iteration Plan
- Assumptions made:
- [user-supplied] items to confirm:
- Feedback loop for next offering:
```

**Reporting-standard alignment:** No formal reporting standard; aligns to CURE (Course-based Undergraduate Research Experience) design + constructive alignment (Biggs) + Open-Science pedagogy and backward design.

**Verification checklist (before delivering):**
- [ ] The research question is genuinely open (unknown answer), not a textbook verification.
- [ ] Every learning outcome is observable and aligned to at least one activity and one rubric criterion.
- [ ] Controls, replication, calibration, and pre-specification appear explicitly as taught content.
- [ ] A reproducibility/data-management practice and a reproduction/comparison activity are embedded.
- [ ] The rubric credits correctly executed null/negative/inconclusive results.
- [ ] A feasibility and safety/ethics pass is present with blockers flagged.
- [ ] No fabricated requirements, papers, citations, results, or instrument/reagent claims; unknowns marked `[user-supplied]`.
- [ ] No banned hype terms in any drafted course-facing language.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Cookbook in disguise | A polished lab whose answer is already known in the textbook, dressed up as "research" | Require an unknown-answer question; if absent, scope one before designing |
| Outcome-activity drift | Outcomes listed, but activities/rubric measure something else | Enforce the alignment table; every outcome maps to an activity and a criterion |
| Positive-result bias | Rubric rewards "finding an effect," nudging students toward p-hacking/fabrication | Add explicit credit for sound process with null/negative results |
| Reproducibility as slogan | "Good notebooks" mentioned but never assessed | Tie notebook/data standard and a reproduction activity to graded artifacts |
| Feasibility blind spot | Elegant design that exceeds hours/budget/instrument access or skips permits | Mandatory feasibility + safety/ethics pass with blockers and `[user-supplied]` flags |
