---
title: "In-Person to Online Course Conversion"
category: education-teaching/instructor/higher-ed-corporate
description: "Convert an existing in-person course (semester or quarter) into an online or hybrid version with realistic faculty workload, assessment-aligned redesign, and a release-ready module sequence."
techniques:
  - ST-02
  - CM-02
  - DS-02
  - OC-01
  - QA-01
difficulty: advanced
tags:
  - higher-education
  - online-learning
  - course-design
  - hybrid
  - hyflex
  - faculty-development
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_async_lms_module_designer.md
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_lecture_to_active_learning.md
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_syllabus_course_designer.md
  - domain-education-teaching/instructor/ed-tech/teaching_blended_hyflex_lesson_designer.md
---

# In-Person to Online Course Conversion

## Objective

Convert a full in-person course into an online (fully async, sync, or hybrid) version. Output is a redesigned syllabus, week-by-week module map, conversion decisions per assessment and activity, faculty workload estimate, and a phased build plan.

## When to Use

- Faculty asked (or required) to put a course online for the first time
- Refresh of a course that was rapidly converted during emergency remote teaching
- Building a hybrid or HyFlex version where some sections are online
- Department-level course redesign where master sections will be shared across instructors

## When NOT to Use

- Single module, not whole course — use `hecorp_async_lms_module_designer.md`
- Just converting one lecture — use `hecorp_lecture_to_active_learning_converter.md`
- Single hybrid lesson — use `edtech_blended_hyflex_lesson_designer.md`

---

## Inputs Needed

- **Course title, level, credits:** [...]
- **Current in-person artifacts:** [Syllabus, slides, assignments, exams — what exists]
- **Target modality:** [Fully async / sync online / hybrid (specify split) / HyFlex]
- **Term length:** [16-week, 8-week, 10-week, 4-week intensive, etc.]
- **Class size & section count:** [...]
- **Faculty teaching load:** [How many other courses, overall workload context]
- **Build timeline:** [Months until launch]
- **Institutional policies / template:** [Course shell template, accessibility office, instructional design support — what's available]
- **LMS:** [Canvas / Blackboard / Brightspace / Moodle]
- **Synchronous tool:** [Zoom / Teams / etc., if any sync component]
- **Previous student outcomes:** [DFW rates, evaluation themes — if known]

---

## Instructions

### Step 1: Re-Anchor on Course-Level Outcomes

Don't port — re-derive. List 4–8 course learning outcomes and ask:
- Are these still right for an online context?
- Does each outcome have a corresponding assessment in the new design?

If the old outcomes are vague ("understand X"), rewrite measurable.

### Step 2: Modality Decision Per Outcome

For each outcome, decide where it best lives:

| Outcome | Best modality | Why |
|---------|---------------|-----|
| [Conceptual recall] | Async self-paced | Independent retrieval works well |
| [Application / problem-solving] | Async with practice + sync office hours | Needs feedback loop |
| [Discussion / debate] | Sync OR async with structure | Async discussion works with strong scaffolding |
| [Lab / hands-on] | Sync, hybrid, or kit-shipped home activity | Procedural skill needs setup |
| [Performance / presentation] | Sync or recorded submission | Needs evidence the learner did it |

If the institution requires a specific modality, work within it.

### Step 3: Build the Module Map

Translate weeks/units into modules:

| Week | Module title | Outcomes addressed | Async items | Sync activity | Assessment |
|------|--------------|--------------------|-------------|---------------|------------|
| 1 | Orientation & foundations | [LO1] | Welcome video, syllabus quiz, intro discussion | (if any) | Low-stakes quiz |
| 2 | [Topic] | [LO2] | Reading + recorded micro-lecture + practice set | Office hours / recitation | Module quiz |
| ... | | | | | |

Each module gets its own design pass via `hecorp_async_lms_module_designer.md`.

### Step 4: Convert the Assessment Plan

Decide for each assessment:

| Original assessment | Conversion option | New assessment | Integrity considerations |
|---------------------|-------------------|----------------|--------------------------|
| In-class proctored exam | Open-book + time-limited / oral exam / project | [...] | Cite sources, individual prompt variants, oral defense |
| In-class essay | Take-home with originality requirement | [...] | Process artifacts, drafts, in-process check-ins |
| Group project | Shared doc + recorded check-ins | [...] | Individual reflection portion |
| Lab practical | Recorded demo / kit-based / sim | [...] | Demonstrate procedure on camera |
| Participation | Discussion + low-stakes quizzing + peer review | [...] | Define what "counts" measurably |

Address academic integrity by design (assessment design, not surveillance) — multiple-prompt variants, process evidence, oral defenses, application questions.

### Step 5: Workload Estimate (Faculty)

Online conversion is heavier than in-person to build, often equal to teach. Estimate:

| Build task | Hours (rough) |
|------------|---------------|
| Re-anchored syllabus & policies | 6–10 |
| Per module (recorded, written, quizzed) | 8–15 |
| Assessments (write + rubric) | 3–6 each |
| LMS shell setup & item entry | 8–15 |
| Accessibility pass | 5–10 |
| Pilot review with ID/peer | 3–5 |

Multiply by module count. If total exceeds available time, scope down the conversion or push for course release.

### Step 6: Workload Estimate (Learners)

For each module, estimate learner hours and confirm consistency with stated credits and your program's expectations. If the module exceeds reasonable load for credit weight, cut.

### Step 7: Build Sequence (Phased)

Don't build all 15 modules in parallel. Phased plan:

| Phase | Build | Why |
|-------|-------|-----|
| Phase 1 (months out) | Module 1 (orientation) + module template | Sets pattern, debugs early |
| Phase 2 | Modules 2–4 | Apply lessons from phase 1 |
| Phase 3 | Modules 5–10 | Volume build |
| Phase 4 | Modules 11–end + final assessment | Tail of course |
| Phase 5 (pre-launch) | Accessibility, link check, student-view test | Release-ready |

Build the first module fully before mass-producing — patterns set early get replicated.

### Step 8: Communication & Presence Plan

Online students fail more often from disconnection than from content. Plan:

- Welcome announcement and video
- Weekly opening + closing announcement
- Discussion presence (read all, reply to ~20%, summarize patterns)
- Office hours (sync and/or async)
- Personalized outreach to students missing first week
- Mid-term feedback survey

### Step 9: Accessibility & Universal Design Baseline

(See `hecorp_async_lms_module_designer.md` Step 9 for module-level baseline.) Course-level adds:
- Tested with screen reader on at least one module
- All recordings captioned
- All PDFs tagged or with HTML alternatives
- Color and contrast audit
- Mobile-friendly check
- DSO / accessibility office reviewed

### Step 10: Pilot, Iterate, and QA

Before launch:
- ID or peer review of one full module
- Test as a student (full flow)
- Run accessibility checker
- Cross-reference syllabus, calendar, and LMS dates
- Pre-load Q&A for common student questions

After launch:
- Mid-term student feedback (specific, low-cost survey)
- Module-by-module retrospective
- Iteration plan for next term

### Step 11: Sustainability & Versioning

Plan for the second offering:
- Version control on slides, scripts, items
- Note where students struggled (signal for redesign)
- Annual review cadence
- Plan for handoff if another instructor will teach the master

---

## Output Format

1. Course outcomes table (re-anchored, measurable)
2. Modality decision per outcome
3. Module map (week-by-week)
4. Assessment conversion table with integrity notes
5. Faculty workload estimate
6. Learner load consistency check
7. Phased build plan
8. Communication & presence plan
9. Accessibility & UD baseline status
10. Pilot / QA / iteration plan
11. Sustainability & versioning plan

---

## False-Positive Prevention

❌ **DON'T:**
- Lift-and-shift the in-person course as PDFs and a final exam
- Try to build all modules at once
- Address integrity through surveillance instead of design
- Skip the welcome/presence plan — disconnection drives DFW
- Underestimate build time
- Forget accessibility until launch week

✅ **DO:**
- Re-anchor outcomes for the new modality
- Decide modality per outcome
- Phase the build, set the pattern with module 1
- Design assessments for integrity
- Plan instructor presence even in async
- Pilot one module fully before mass-producing

---

## Quality Indicators

- [ ] Outcomes re-anchored and measurable
- [ ] Modality decisions justified per outcome
- [ ] Module map covers full term
- [ ] Assessment conversions address integrity
- [ ] Faculty workload sums realistic
- [ ] Phased build plan in place
- [ ] Accessibility baseline addressed
- [ ] Pilot and QA plan present

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-02** | Outcomes → modality → modules → assessments → workload → build pipeline. |
| **CM-02** | Constrains build to stated timeline and learner load to credit weight. |
| **DS-02** | Multi-modality (async / sync / hybrid / HyFlex) routing keeps decisions explicit. |
| **OC-01** | Module-map and assessment-conversion tables enforce structured output. |
| **QA-01** | Pilot, accessibility audit, and mid-term feedback close the loop. |
