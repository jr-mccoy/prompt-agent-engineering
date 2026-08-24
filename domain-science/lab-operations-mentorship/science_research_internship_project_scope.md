---
title: "Research Internship Project Scope Designer"
category: science/lab-operations-mentorship
description: "Scope a genuinely completable 8–12 week research internship project with a bounded question, realistic output, derisking fallback, and an explicit definition of success."
techniques:
  - ST-01
  - RT-01
  - RT-03
  - QA-02
  - DS-02
  - NE-10
difficulty: advanced
tags:
  - research-internship
  - project-scoping
  - derisking
  - milestones
  - realistic-outputs
  - definition-of-success
  - go-no-go
  - mentoring
updated: "2026-06-26"
related_prompts:
  - domain-science/lab-operations-mentorship/science_undergraduate_research_mentoring_plan.md
  - domain-science/lab-operations-mentorship/science_lab_culture_charter.md
  - domain-science/methods-foundations/science_research_question_refiner.md
---

# Research Internship Project Scope Designer

**Objective:** Scope an 8–12 week research internship project that an intern can actually finish. The scope sets a well-bounded question, a realistic output, a derisked fallback milestone if the main aim stalls, a weekly milestone plan, required onboarding and skills, and an explicit statement of what success looks like — including what a partial result still yields.

**When to use:** A mentor is designing a summer or short-term internship and wants to resist over-scoping, so the intern leaves with a real, completable contribution rather than a fragment of an over-ambitious aim.

**Required inputs:**
- **Discipline.** Field/subfield and the core methods involved.
- **Career stage / context.** Mentor's role; the intern's background, prior skills, and what the internship is for (experience, credit, decision about the field, conversion pipeline).
- **Duration and effort.** Number of weeks (target 8–12) and hours per week.

**Optional inputs:**
- A candidate aim or dataset/system the intern would work on (`[user-supplied]` if not given).
- Access, compute, equipment, sample, or approval constraints that affect feasibility.
- Required safety/ethics/onboarding training and its lead time.
- The intern's stated goals and any output venue (poster, report, demo, internal talk).

**Constraints — Must:**
- Bound the central question so it is completable in the stated weeks at the intern's level.
- Include a derisked fallback milestone reachable even if the primary aim stalls.
- Lay out weekly milestones with a built-in go/no-go checkpoint.
- State an explicit definition of success and what a partial success still produces.
- Account for onboarding/training lead time inside the weekly plan, not as an afterthought.

**Constraints — Must Not:**
- Do not invent institutional policies, named people, or commitments. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not scope toward a publication or a finished product as the success bar for a short internship.
- Do not use inflated language ("novel," "groundbreaking," "first-ever," "gold standard") in the drafted scope.
- Do not assume access, data, compute, or approvals are in place — surface them as prerequisites.

**Instructions:**

1. **Confirm parameters and intent.** Restate discipline, mentor role, intern background, weeks, and hours. State what the internship is *for*, since that shapes a reasonable output.
2. **Frame and bound the question.** Turn a broad aim into one tractable question with a clear endpoint; reference the research-question refiner if it needs sharpening. Sanity-check feasibility against time, access, and skill level.
3. **Define the primary output.** Specify the concrete deliverable (characterized result, working analysis/pipeline, validated protocol, demo, report) sized to the weeks available.
4. **Design the derisking fallback.** Identify the most likely failure points and define a fallback milestone the intern can still reach and present if the main aim stalls (e.g., a characterized negative result, a reusable tool, a scoped pilot).
5. **Set onboarding and skill prerequisites.** List required training, accesses, and skills with lead times; place them at the start of the timeline as gates.
6. **Lay out weekly milestones.** Map weeks 1–N: onboarding → setup/pilot → core execution → analysis → output. Mark a mid-project go/no-go checkpoint where mentor and intern decide whether to continue the primary aim or pivot to the fallback.
7. **Write the definition of success.** State full success, the go/no-go criteria, and what partial success still yields for both the intern (skills, artifact) and the lab (data, tool, narrowed question).
8. **Add supervision, check-ins, and supports.** Specify meeting cadence and purpose, how the intern raises blockers, and well-being/professional resources, routing personal/mental-health needs to professional support and tying to the lab charter where one exists.

**Output format (locked):**

```
## Internship Project Scope — One-Pager
Discipline: [...] | Mentor role: [...] | Intern background: [...] | Duration: [n] wks | Hours/week: [...]
Purpose of internship: [...]

## Bounded Question
Question: [...] | Endpoint: [...] | Feasibility check (time/access/skill): [...]

## Primary Output
Deliverable: [...]

## Derisking Fallback
Likely failure points: [...] | Fallback milestone (still presentable): [...]

## Prerequisites (onboarding / access / skills)
- [ ] [item] — lead time [...]  (gate)

## Weekly Milestones
Wk 1–2 — Onboarding & setup: [...]
Wk 3–N — Core execution: [...]
Mid-project GO/NO-GO (wk [n]): continue primary aim vs. pivot to fallback — criteria: [...]
Final wks — Analysis & output: [...]

## Definition of Success
Full success: [...] | Go/no-go criteria: [...]
Partial success yields — intern: [...] | lab: [...]

## Supervision, Check-Ins & Supports
Cadence/purpose: [...] | Raising blockers: [...] | Resources/well-being: [user-supplied]

## Open Items Requiring [user-supplied] Input
[...]
```

**Reporting-standard alignment:** No formal reporting standard governs internship scoping; this aligns to CIMER mentoring competencies (aligning expectations, fostering independence) and mentor–mentee compact practice, with go/no-go milestone discipline drawn from staged project-management and derisking practice.

**Verification checklist (before delivering):**
- [ ] Discipline, mentor role, intern background, weeks, and hours are restated; purpose of the internship stated.
- [ ] The central question is bounded with a clear endpoint and a feasibility check.
- [ ] A derisked fallback milestone is defined and remains presentable on its own.
- [ ] Onboarding/training lead times are placed inside the weekly plan as gates.
- [ ] Weekly milestones include a mid-project go/no-go checkpoint with explicit criteria.
- [ ] Definition of success names full, partial, and go/no-go outcomes for both intern and lab.
- [ ] No publication-as-bar; no assumed access/compute/approvals.
- [ ] No invented commitments; gaps marked `[user-supplied]`; no inflated language.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Over-scoping | An aim that only "succeeds" with a polished or publishable result | Size output to weeks; require an explicit partial-success outcome |
| No fallback | A single-path plan that fails entirely if the aim stalls | Mandate a derisked fallback milestone and a go/no-go checkpoint |
| Ignored onboarding | A plan that starts core work in week 1 despite training needs | Place training/access lead times at the front of the timeline as gates |
| Assumed access | Scope that presumes data, compute, samples, or approvals exist | List each as a prerequisite marked `[user-supplied]` |
| Vague success | "Make progress" as the bar | Write full / partial / go-no-go criteria the mentor and intern can check |
