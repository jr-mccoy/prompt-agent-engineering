---
title: "Async LMS Module Designer"
category: education-teaching/instructor/higher-ed-corporate
description: "Design a fully asynchronous online module ready to drop into Canvas, Blackboard, Brightspace, or Moodle — with sequenced content, embedded checks, discussion structure, and accessibility baseline."
techniques:
  - ST-02
  - CM-02
  - OC-01
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - higher-education
  - online-learning
  - asynchronous
  - lms
  - canvas
  - blackboard
  - course-design
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_online_course_conversion.md
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_lecture_to_active_learning.md
  - domain-education-teaching/instructor/ed-tech/teaching_lms_course_shell_setup.md
---

# Async LMS Module Designer

## Objective

Produce a single self-contained asynchronous module learners can complete on their own, structured for direct paste into Canvas / Blackboard / Brightspace / Moodle. Output includes module overview page, sequenced learning items, embedded knowledge checks, a discussion or artifact submission, and an accessibility baseline.

## When to Use

- Building or rebuilding a unit in an online course
- Adding an async component to a hybrid or HyFlex course
- Faculty new to LMS authoring needing a complete, structured first module
- Replacing a static PDF reading pack with an actually-designed module
- Preparing OER (open educational resource) module for sharing

## When NOT to Use

- Converting whole in-person course — start with `hecorp_online_course_conversion.md`
- Single short skill — use `hecorp_microlearning_module.md`
- Live class plan — use `teaching_lesson_plan_generator.md` or `hecorp_lecture_to_active_learning_converter.md`

---

## Inputs Needed

- **Course title and target population:** [Undergrad / grad / professional / corporate]
- **Module topic:** [Specific scope]
- **Module-level learning objectives:** [3–5 measurable]
- **Time budget for learner:** [Total hours of seat time the module should fill]
- **Module placement:** [Week N of M; what comes before/after]
- **LMS:** [Canvas / Blackboard / Brightspace / Moodle / D2L / other]
- **Available media:** [Recorded lectures, readings, simulations, datasets — list what exists vs. what must be created]
- **Assessment weight:** [Graded? % of course grade?]
- **Accessibility floor:** [Captions required, alt text required, screen-reader expectations]

---

## Instructions

### Step 1: Anchor the Module With Outcomes-First Design

State 3–5 module learning objectives in measurable form. For each, specify:

| Objective | Bloom level | Evidence (what learner produces) | Assessment item |
|-----------|------------|----------------------------------|-----------------|

If an objective has no evidence path, it's aspirational — cut or rewrite.

### Step 2: Estimate Cognitive Load Budget

Use this rough planning heuristic (independent of any specific institution's policy — confirm against your program's expectations):

- Reading: ~5–8 pages/hour for technical text, ~10–15 pages/hour for narrative
- Recorded video: 1× real time + 0.5× for note-taking
- Discussion post: 30–60 min for substantive original + 2 replies
- Quiz: 1–2 min per item
- Project work: scope to estimated effort

Total must fit within stated learner time budget. If over, cut content.

### Step 3: Map the Module to LMS Item Types

Translate your design to native LMS items:

| Design intent | Canvas item | Blackboard item | Brightspace item | Moodle item |
|---------------|-------------|------------------|------------------|-------------|
| Module overview page | Page | Item / Folder description | HTML topic | Page |
| Recorded lecture | Page with embed | Item with video | Topic with video | Lesson / Page |
| Reading | File or external URL | File / URL | File / URL | Resource / URL |
| Knowledge check | Quiz (auto-graded) | Test | Quiz | Quiz |
| Discussion | Discussion | Discussion Board | Discussion | Forum |
| Submission | Assignment | Assignment | Assignment | Assignment |
| Reflection | Quiz (essay) or Assignment | Journal | Reflection | Assignment / Journal |

### Step 4: Author the Module Overview Page

Module overview should answer for the learner, before they start, in this order:

1. **What you'll be able to do** — objectives in plain language
2. **Why it matters** — connection to course, role, or upcoming work
3. **How long this will take** — time budget and breakdown
4. **What you'll do** — ordered list of items in the module
5. **How you'll be graded** — weight, criteria, due dates
6. **Where to get help** — instructor email, support hours, tech help

Write this page as final HTML/Markdown ready to paste.

### Step 5: Sequence Learning Items

Use the **Hook → Frame → Content → Practice → Apply → Reflect** pattern:

| Item # | Type | Title | Estimated time | Purpose |
|--------|------|-------|----------------|---------|
| 1 | Page | Welcome & overview | 5 min | Hook + frame |
| 2 | Reading or video | First exposure to concept | 30 min | Content |
| 3 | Quiz | Knowledge check (low-stakes) | 10 min | Retrieval |
| 4 | Reading or video | Application examples | 25 min | Content |
| 5 | Activity | Worked problem walkthrough | 20 min | Practice |
| 6 | Discussion | Apply concept to learner's context | 60 min | Apply |
| 7 | Quiz or assignment | Module assessment | 30 min | Evidence |
| 8 | Page | Reflection prompt | 10 min | Consolidate |

### Step 6: Author Embedded Knowledge Checks

Write 5–10 low-stakes auto-graded items that learners take during the module (not at the end). Each item:

- Tied to a stated objective
- One clear answer (or defensible "select all")
- Distractors that match named misconceptions, not random
- Brief feedback per option ("Correct because..." / "This misses X because...")
- Allow multiple attempts; show feedback after each

### Step 7: Design the Discussion or Artifact

If discussion: write the prompt, model response expectations, and reply criteria. Avoid:
- "Post your thoughts on X" (no scaffolding)
- "Reply to two peers" (no quality criteria)

Better:
- A specific stance/decision/application prompt
- Required components (claim + evidence + alternative)
- Reply criteria (extend, complicate, or constructively challenge — not "I agree")

If artifact: provide template, rubric, and exemplar.

### Step 8: Write the Module Assessment

Aligned to the objectives table from Step 1. Include:
- Item-to-objective map
- Rubric or answer key
- Time-to-complete estimate
- Re-take or revision policy

### Step 9: Accessibility Baseline

Apply minimum:

- [ ] Every video has accurate captions (not auto-only)
- [ ] Every image has alt text (or marked decorative)
- [ ] Headings are real headings, not bold text
- [ ] Color is not the sole carrier of meaning
- [ ] Tables have headers
- [ ] Links have descriptive text (not "click here")
- [ ] PDFs are tagged or have HTML alternative
- [ ] Time limits on quizzes are extendable for accommodation
- [ ] Reading level reasonable for population (or scaffolded if not)

### Step 10: Instructor Presence & Pacing Cues

Async ≠ instructor-absent. Specify instructor presence:

- Welcome announcement at module open (template provided)
- Mid-module nudge or summary post on day N
- Discussion presence — read all, reply to ~20%, summarize patterns
- Closing announcement with what's next

### Step 11: Pre-Launch QA Checklist

- [ ] All due dates set and consistent across items
- [ ] All links work (not previews of unpublished items)
- [ ] Quiz settings (attempts, time, feedback timing) match policy
- [ ] Module is published; items are published
- [ ] Test as a student (use student view or test account)
- [ ] Accessibility checker run

---

## Output Format

1. Module objectives table with assessment alignment
2. Cognitive load budget vs. learner time budget
3. LMS item-type mapping for chosen platform
4. Module overview page (paste-ready)
5. Sequenced item list with times and purposes
6. Knowledge check items with feedback
7. Discussion prompt or artifact template + rubric
8. Module assessment + key/rubric
9. Accessibility audit results
10. Instructor presence plan
11. Pre-launch QA checklist

---

## False-Positive Prevention

❌ **DON'T:**
- Dump readings and a final quiz and call it a module
- Write knowledge-check distractors that are obviously wrong
- Set discussion as "post and reply to two" without quality criteria
- Forget captions and alt text — accessibility is non-optional
- Skip the student-view test before publishing
- Confuse seat-time estimates with actual learner effort

✅ **DO:**
- Lead with measurable objectives
- Sequence Hook → Frame → Content → Practice → Apply → Reflect
- Build retrieval into the module, not just at the end
- Make instructor presence explicit even when async
- Test as a student before opening to learners

---

## Quality Indicators

- [ ] 3–5 measurable objectives with assessment paths
- [ ] All items mapped to LMS item types
- [ ] Module overview page complete
- [ ] At least one mid-module retrieval check
- [ ] Discussion or artifact has explicit criteria
- [ ] Accessibility baseline met
- [ ] Pre-launch QA passes

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-02** | Outcomes → load budget → sequence → author → QA pipeline. |
| **CM-02** | Constrains design to learner time budget and accessibility floor. |
| **OC-01** | LMS item table and overview-page template enforce paste-ready output. |
| **DS-02** | Multi-LMS mapping accounts for platform-specific item types. |
| **QA-01** | Pre-launch checklist and student-view test verify release-readiness. |
