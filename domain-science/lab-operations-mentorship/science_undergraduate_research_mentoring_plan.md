---
title: "Undergraduate Research Mentoring Plan Designer"
category: science/lab-operations-mentorship
description: "Design a scaffolded semester or summer mentoring plan for an undergraduate researcher with a bounded first project, skill-building sequence, and gradual ownership."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - DS-02
  - NE-10
difficulty: advanced
tags:
  - undergraduate-research
  - mentoring-plan
  - scaffolding
  - skill-building
  - ownership-progression
  - cimer
  - check-ins
  - authorship-pathway
updated: "2026-06-26"
related_prompts:
  - domain-science/lab-operations-mentorship/science_lab_culture_charter.md
  - domain-science/lab-operations-mentorship/science_research_internship_project_scope.md
  - domain-science/methods-foundations/science_research_question_refiner.md
---

# Undergraduate Research Mentoring Plan Designer

**Objective:** Build a realistic, scaffolded mentoring plan for an undergraduate over a semester or summer. The plan gives the student a bounded first project, a sequenced path of skills, regular check-ins, clear expectations, a tangible output (poster or report), and a gradual increase in ownership — with ambition calibrated to the student's experience and the available time.

**When to use:** A mentor (PI, postdoc, grad student) is about to take on an undergraduate and wants a structured plan that supports a beginner rather than treating them as a junior grad student.

**Required inputs:**
- **Discipline.** Field/subfield and the core methods the student will touch.
- **Career stage / context.** Mentor's role; the undergraduate's year, prior research exposure, and relevant coursework or skills.
- **Timeframe and effort.** Semester vs. summer; hours per week; total weeks.

**Optional inputs:**
- A candidate project area or open question the lab wants explored (`[user-supplied]` if not given).
- The student's stated goals (grad school, skill-building, deciding on a field).
- Available outputs/venues (department poster session, internal report, group meeting talk).
- Safety/training prerequisites for the discipline.

**Constraints — Must:**
- Bound the first project so it is genuinely completable in the timeframe by a beginner.
- Scaffold: front-load training and structured tasks, then increase autonomy over the weeks.
- Schedule regular check-ins with named purposes (not just "meet weekly").
- Define a tangible output and a clear definition of success.
- Treat authorship as a possible, criteria-based outcome — not a promise and not assumed absent.

**Constraints — Must Not:**
- Do not invent institutional policies, named people, or commitments. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not over-scope: no plan that assumes a publishable result is the bar for success.
- Do not use inflated language ("novel," "groundbreaking," "first-ever," "gold standard") in the drafted plan.
- Do not assign unsupervised work on safety-critical procedures without naming required training as a gate.

**Instructions:**

1. **Confirm parameters.** Restate discipline, mentor role, student experience, timeframe, and weekly hours. Flag any mismatch between ambition and time before planning.
2. **Set learning goals.** Distinguish research-skill goals (technique, analysis, reading), professional goals (lab norms, communication, time management), and the student's own stated goals.
3. **Bound the first project.** Define one well-scoped question or task with a clear endpoint; reference the research-question refiner if the area needs sharpening. Include a fallback if the main task stalls.
4. **Sequence the skills.** List the skills the project requires and order them so the student builds capability before being asked to apply it independently. Mark any safety/training prerequisites as hard gates.
5. **Lay out a week-by-week plan.** Phase it: onboarding & training → guided execution → increasing independence → analysis → output preparation. Show where supervision tapers and ownership grows.
6. **Define check-ins and feedback.** Specify cadence, format, and purpose of meetings; how feedback is given; and how the student raises being stuck (normalize it). Tie to the lab charter where one exists.
7. **Specify the output and success definition.** Name the concrete deliverable (poster/report/talk) and state what full success looks like and what a partial result still yields (skills, characterized negative result, a usable protocol).
8. **Address authorship and next steps.** State the criteria under which the student could become an author, and describe possible continuations (next semester, honors thesis, internship) without committing the lab.
9. **List expectations and supports.** Summarize mutual expectations (mentor and student) and the resources, training, and well-being supports available, routing personal/mental-health needs to professional resources.

**Output format (locked):**

```
## Undergraduate Mentoring Plan
Discipline: [...] | Mentor role: [...] | Student stage: [...] | Timeframe: [...] | Hours/week: [...]

## Learning Goals
Research skills: [...] | Professional skills: [...] | Student's stated goals: [...]

## First Project (Bounded)
Question/task: [...] | Endpoint: [...] | Fallback if stalled: [...]

## Skills Checklist (sequenced)
- [ ] [skill] — build by week [n]  (gate: [training if any])
- [ ] ...

## Week-by-Week Plan
Phase 1 — Onboarding & Training (wk ...): [...]
Phase 2 — Guided Execution (wk ...): [...]
Phase 3 — Increasing Independence (wk ...): [...]
Phase 4 — Analysis & Output (wk ...): [...]

## Check-Ins & Feedback
Cadence/format/purpose: [...] | How to flag being stuck: [...]

## Output & Definition of Success
Deliverable: [...] | Full success: [...] | Partial success still yields: [...]

## Authorship & Next Steps
Authorship criteria: [...] | Possible continuations: [...]

## Expectations & Supports
Mentor commits to: [...] | Student commits to: [...] | Resources/well-being: [user-supplied]

## Open Items Requiring [user-supplied] Input
[...]
```

**Reporting-standard alignment:** No formal reporting standard governs undergraduate mentoring plans; this aligns to CIMER mentoring competencies (aligning expectations, assessing understanding, fostering independence, promoting professional development) and mentor–mentee compact practice, with CRediT criteria for the authorship pathway.

**Verification checklist (before delivering):**
- [ ] Discipline, mentor role, student experience, and timeframe are restated; ambition matched to time.
- [ ] The first project is bounded with a clear endpoint and a fallback.
- [ ] Skills are sequenced so capability precedes independent application; safety training is gated.
- [ ] The week-by-week plan shows supervision tapering and ownership increasing.
- [ ] Check-ins have named purposes and a normalized way to surface being stuck.
- [ ] A tangible output and an explicit success definition (including partial success) are present.
- [ ] Authorship is criteria-based, not promised or assumed absent.
- [ ] No invented commitments; gaps marked `[user-supplied]`; no inflated language.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Over-scoping | A plan whose success requires a publishable finding | Define completable output; state partial-success value |
| No scaffolding | "Independent project" handed to a beginner day one | Sequence training before autonomy; taper supervision visibly |
| Hollow check-ins | "Weekly meeting" with no purpose | Give each check-in a named function and a stuck-escalation path |
| Authorship over/under-promise | Guaranteeing a paper, or silently excluding the student | State explicit, criteria-based authorship conditions |
| Safety shortcut | Assigning hazardous work without training | Mark required training as a hard gate in the skills checklist |
