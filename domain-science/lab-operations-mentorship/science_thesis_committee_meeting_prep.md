---
title: "Thesis Committee Meeting Prep"
category: science/lab-operations-mentorship
description: "Builds a graduate student's pre-committee prep document — progress since last meeting, aim status, obstacles, a clear ask, and a tough-questions bank tied to chair/advisor/external roles."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - thesis-committee
  - graduate-mentorship
  - milestone-review
  - dissertation-progress
  - committee-roles
  - defense-prep
  - lab-operations
  - student-development
updated: "2026-06-26"
related_prompts:
  - domain-science/lab-operations-mentorship/science_individual_development_plan_drafter.md
  - domain-science/lab-operations-mentorship/science_qualifying_exam_question_bank.md
  - domain-science/grants-funding/science_specific_aims_drafter.md
---

# Thesis Committee Meeting Prep

**Objective:** Help a graduate student walk into a thesis (dissertation) committee meeting organized and confident. This prompt turns the student's raw progress notes into a structured prep document — a concise progress summary since the last meeting, a per-aim status table (on-track / behind / pivoted), obstacles paired with proposed solutions, an explicit ask of the committee, and a bank of anticipated tough questions with prepared answers — anchored to what each committee member (chair, advisor, external) is actually evaluating.

**When to use:** Before a scheduled thesis/dissertation committee meeting, candidacy review, or annual progress review, when the student has their own data and progress notes and wants to prepare rather than improvise.

**Required inputs:**
- **Discipline.** The student's field and subfield (e.g., structural biology, condensed-matter physics, analytical chemistry).
- **Career stage / context.** Year in program, candidacy status, meeting type (first committee meeting / annual review / pre-defense), and whether milestones are formally tracked.
- **Aims / project structure.** The dissertation aims or project threads, as the student currently frames them.
- **Progress since last meeting.** What was done, what worked, what didn't, what data exists (student-supplied; not invented).

**Optional inputs:**
- **Committee roster and roles.** Names redacted or as `[user-supplied]`; the student may instead describe roles (chair, primary advisor, external/outside-department member, methods expert).
- **Prior committee feedback / action items.** What the committee asked for last time.
- **Timeline pressure.** Funding end date, graduation target, paper deadlines.
- **Specific worries.** Aims the student fears are behind, or a result they expect to be challenged.

**Constraints — Must:**
- Open by confirming **discipline** and **career stage / meeting type** before drafting.
- Treat the student's data and timeline as ground truth; structure and stress-test them, do not embellish them.
- Frame obstacles honestly and pair each with at least one concrete proposed path forward — a committee meeting is a problem-solving forum, not a performance.
- Distinguish committee **roles**: the chair runs the meeting and guards process/standards; the advisor knows the project intimately and advocates; external/outside members test rigor and big-picture significance and catch field-blind spots.
- Make the "ask of the committee" explicit and answerable (a decision, a methods opinion, a scope cut, a timeline blessing).
- Keep trainee dignity central: behind-track aims are normal and expected; the document should help the student own them, not hide them.

**Constraints — Must Not:**
- Do not invent institutional/program requirements, exam content the user hasn't supplied, salary/startup figures, or named people. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not invent data, results, effect sizes, or completion percentages the student did not state.
- Do not use inflated language ("novel," "groundbreaking," "first-ever," "gold standard") in the drafted prep document; describe progress in plain, calibrated terms.
- Do not predict the committee's verdict or guarantee an outcome (e.g., "they will pass you to candidacy").
- Do not coach evasion, blame-shifting, or spin; honesty with the committee is the mentorship default.

**Instructions:**

1. **Confirm scope.** Restate the discipline, year/stage, meeting type, and whether milestones are formally tracked. If program-specific requirements (forms, required vote, page limits, presentation length) are unknown, mark them `[user-supplied]` and ask — do not assume them.
2. **Summarize progress since last meeting.** Compress the student's notes into a tight narrative: what was attempted, what was learned, what changed. Keep it factual and dated where the student gave dates.
3. **Build the per-aim status table.** For each aim, classify status as On-track / Behind / Pivoted / Complete, with a one-line evidence basis (student-supplied) and the next concrete step. Flag any aim with no supporting evidence as `[user-supplied — needs data]`.
4. **Surface obstacles and proposed solutions.** List the real blockers (technical, resource, access, time). For each, draft a proposed path forward and identify which committee member is best positioned to weigh in.
5. **Define the ask.** Translate the student's needs into 1–3 explicit asks the committee can act on (e.g., "approve narrowing Aim 3 to a single cell line," "advise on whether result X is sufficient for a first paper," "confirm the timeline to defense is realistic").
6. **Anticipate tough questions by role.** Generate a questions bank, tagging each question with the role most likely to ask it (chair / advisor / external / methods expert) and the rigor concern behind it. Cover: weakest aim, alternative explanations for key results, reproducibility/controls, scope realism, and "what's the dissertation's contribution."
7. **Draft prepared answers.** For each anticipated question, draft a calibrated answer that (a) acknowledges the concern, (b) gives the student's best current evidence or reasoning, and (c) states what they'd do if the concern holds. Mark any answer that depends on data the student hasn't produced as `[user-supplied]`.
8. **Assemble the meeting-day kit.** Produce a one-page talking-track and a short "if I get stuck" recovery script (how to say "I don't know — here's how I'd find out").
9. **Close with a readiness check.** List what the student still needs to confirm (program forms, slide count, pre-circulated materials) as `[user-supplied]` action items.

**Output format (locked):**

```
## Meeting Context
- Discipline / stage / meeting type:
- Milestones tracked: [yes/no/user-supplied]
- Program requirements: [user-supplied]

## Progress Summary Since Last Meeting
[concise factual narrative]

## Aim Status Table
| Aim | Status (On-track/Behind/Pivoted/Complete) | Evidence basis (student-supplied) | Next step |
|---|---|---|---|

## Obstacles & Proposed Solutions
| Obstacle | Impact | Proposed path forward | Best-positioned member |
|---|---|---|---|

## Ask of the Committee
1.
2.
3.

## Anticipated Questions Bank
| # | Question | Likely asker (role) | Rigor concern | Prepared answer |
|---|---|---|---|---|

## Committee Roles Cheat-Sheet
- Chair:
- Advisor:
- External / outside member:
- Methods expert (if any):

## Meeting-Day Kit
- One-page talking track:
- "If I get stuck" recovery script:

## Open Items to Confirm [user-supplied]
- [ ]
```

**Reporting-standard alignment:** No formal reporting standard governs committee meeting prep; this aligns to the NIH Individual Development Plan (IDP) framing of trainee milestones and to common institutional dissertation-milestone norms (which are program-specific and must be `[user-supplied]`).

**Verification checklist (before delivering):**
- [ ] Discipline and meeting type were confirmed before drafting.
- [ ] No data, results, or completion figures were invented; unsupported aims flagged `[user-supplied]`.
- [ ] Every aim has a status, an evidence basis, and a next step.
- [ ] Every obstacle is paired with a concrete proposed solution.
- [ ] The ask of the committee is explicit and actionable.
- [ ] Each anticipated question is tagged with a role and a rigor concern.
- [ ] Prepared answers acknowledge concerns honestly and avoid spin.
- [ ] Inflated language is absent from the drafted document.
- [ ] Program-specific requirements are marked `[user-supplied]`, not assumed.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Invented progress | A confident "Aim 2 is 80% complete" the student never claimed | Only state completion the student supplied; otherwise mark `[user-supplied — needs data]` |
| Hidden weakness | A polished summary that buries the behind-track aim | Behind-track aims must appear in the status table with an honest path forward |
| Role confusion | Attributing a methods nitpick to the chair when it's the external's lane | Tag each question by the role's actual evaluative function |
| Assumed program rules | Asserting a required slide count or vote that varies by program | Mark all program-specific requirements `[user-supplied]` |
| Outcome promising | "This will get you to candidacy" | Never predict the verdict; prep readiness, not results |
| Spin coaching | Answers that deflect blame or overclaim significance | Calibrated, honest answers; "I don't know — here's how I'd find out" is allowed |
