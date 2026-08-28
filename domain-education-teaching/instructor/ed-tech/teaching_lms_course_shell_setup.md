---
title: "LMS Course Shell Setup Checklist"
category: education-teaching/instructor/ed-tech
description: "Stand up an LMS course shell (Canvas / Blackboard / Brightspace / Moodle) end-to-end before the term opens — navigation, modules, gradebook, communication, accessibility, and a student-view test."
techniques:
  - ST-02
  - CM-02
  - OC-01
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - lms
  - canvas
  - blackboard
  - brightspace
  - moodle
  - course-setup
  - higher-education
  - instructional-design
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_async_lms_module_designer.md
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_online_course_conversion.md
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_syllabus_course_designer.md
---

# LMS Course Shell Setup Checklist

## Objective

Stand up a release-ready LMS course shell — navigation, syllabus, modules, gradebook, communication tools, accessibility settings, and student-view test — before the first day of term. Output is a sequenced setup checklist with platform-specific notes and a pre-launch sign-off audit.

## When to Use

- Pre-term setup of a new course
- Reset of a course shell from a prior term (rolled-over content)
- Migrating a course between LMS platforms
- New instructor inheriting a course shell from a colleague
- Department-template course rollout to many sections

## When NOT to Use

- Designing the course content itself — use `hecorp_async_lms_module_designer.md` or `hecorp_online_course_conversion.md`
- Live class lesson plan — use `teaching_lesson_plan_generator.md`

---

## Inputs Needed

- **LMS:** [Canvas / Blackboard / Brightspace / Moodle / D2L / other]
- **Course title, term, section(s):** [...]
- **Roster source:** [SIS auto-populated / manual / hybrid]
- **Course-shell origin:** [Brand new / rolled-over / template / migrated]
- **Modality:** [In-person / hybrid / online]
- **Term length & key dates:** [Start, end, holidays, drop deadline, finals]
- **Instructional team:** [Lead, co-teachers, TAs, ID — who has what role]
- **Institutional template / required elements:** [Standard banner, required modules, branding, accessibility office requirements]
- **Integrations needed:** [Publisher tools, plagiarism checker, video platform, polling, grade passback]

---

## Instructions

### Step 1: Confirm Course Settings & Roster

Platform-agnostic:
- [ ] Course title and code correct
- [ ] Start date and end date correct
- [ ] Term mapped correctly
- [ ] Roster syncing from SIS (or manual roster verified)
- [ ] Section enrollments correct
- [ ] TA / co-instructor roles assigned with correct permissions
- [ ] Student access opens on intended date (not before, unless intended)
- [ ] Course visibility setting correct (open vs. closed to non-enrolled)

### Step 2: Set Course Navigation

Hide what you don't use; surface what you do. Default principle: ≤ 8 visible nav items.

| Common nav item | Show? | Reorder? |
|-----------------|-------|----------|
| Home | Yes | First |
| Syllabus | Yes | High |
| Modules | Yes (primary entry point) | High |
| Announcements | Yes | High |
| Discussions | Yes if used | Medium |
| Assignments | Yes if students use it (or hidden if Modules-only) | Medium |
| Grades | Yes | High |
| Files | Hide if Modules-organized | — |
| People | Yes | Low |
| External tool integrations | Yes if used | Low |

### Step 3: Configure the Home Page

Home is the first impression. Build:

- Welcome message (with instructor photo if comfortable)
- Current week / what's due now
- Where to start (link to Module 1 or Syllabus)
- How to get help
- Critical announcements pinned

Don't dump the syllabus on Home.

### Step 4: Upload & Configure the Syllabus

- Syllabus file or HTML page with required institutional elements
- Course-level learning outcomes
- Schedule / calendar
- Grading policy
- Policies (attendance, late work, academic integrity, accommodations)
- Required materials / textbooks
- Communication norms

(For full syllabus authoring, use `teaching_syllabus_course_designer.md`.)

### Step 5: Build Module Structure

Default pattern: one module per week or unit. For each module:

- Module title with date
- Overview page (objectives, time estimate, how to start)
- Sequenced items (readings, videos, quizzes, discussions, assignments)
- Module assessment (if any)
- Module wrap-up / reflection

(For module-level design, use `hecorp_async_lms_module_designer.md`.)

Lock or release modules per term schedule. Don't release everything on day 1 unless intended.

### Step 6: Configure the Gradebook

- [ ] Grading scheme (letter / percentage / points / mastery) set
- [ ] Assignment groups created (e.g., Quizzes, Papers, Participation)
- [ ] Group weights match syllabus
- [ ] Late policy configured (if used)
- [ ] Drop lowest score (if used)
- [ ] Total column visible to students or hidden (per policy)
- [ ] Grade-passback to SIS configured
- [ ] Test calculations with a dummy student to confirm math matches syllabus

A gradebook that contradicts the syllabus generates the most appeals.

### Step 7: Set Up Communication

- Announcements: pinned welcome, schedule for weekly opening message
- Inbox / messaging: norms posted (response time, what to use vs. email)
- Discussion forums: created and structured (Q&A forum, social forum, weekly forums)
- Office-hours signup tool (if used)
- Notification defaults nudge (link students to set their own)

### Step 8: Add Integrations

Per integration, configure and test:

- Publisher textbook tool (single sign-on, grade passback)
- Plagiarism checker (default settings, student visibility)
- Video platform (Panopto, Kaltura, Stream) — captions, sharing
- Polling tool (Poll Everywhere, Mentimeter) — roster sync
- Lockdown browser / proctor (only if used and disclosed in syllabus)

Test each end-to-end before students access.

### Step 9: Accessibility Pass

- [ ] Heading structure used (not bold-as-heading)
- [ ] Alt text on images
- [ ] Captions on videos (accurate, not auto-only)
- [ ] Color contrast passes
- [ ] Tables have headers
- [ ] Links have descriptive text
- [ ] PDFs tagged or HTML alternatives provided
- [ ] LMS accessibility checker run (e.g., Ally, Bb Ally, Brightspace Accessibility)
- [ ] DSO / accessibility office contacts posted

### Step 10: Student-View Test

This is the single most important step. Log in as a test student (or use student view):

- [ ] Home page renders correctly
- [ ] Syllabus visible
- [ ] Modules in correct order with correct release dates
- [ ] First module clickable end-to-end
- [ ] Sample assignment submission works
- [ ] Sample quiz attempt works
- [ ] Discussion post works
- [ ] Gradebook displays correctly
- [ ] Mobile view works
- [ ] Notifications fire as expected

Fix any issue found before opening to students.

### Step 11: Pre-Launch Communication

- Welcome email or LMS announcement scheduled to send on day 1
- Syllabus quiz (optional but recommended — confirms students read policies)
- "Where to start" instructions visible
- Emergency contact / help-desk pathway clear

### Step 12: Backup & Versioning

- Export course shell once stable (for backup)
- Document what's in this shell vs. last term (changelog)
- Note known issues for next iteration
- If migrating between LMS, validate item-by-item

### Step 13: Term-Open Daily Checks (First Week)

- Day 1: Confirm students can log in; respond to access tickets fast
- Day 2: Check assignment submissions are arriving; open Q&A forum
- Day 3: Read first discussion responses; intervene if confused
- End of week 1: Send check-in announcement; survey early friction

---

## Output Format

1. Course settings & roster confirmation
2. Navigation configuration
3. Home page content
4. Syllabus uploaded and linked
5. Module structure with release dates
6. Gradebook configuration with weights matching syllabus
7. Communication setup
8. Integrations configured & tested
9. Accessibility audit results
10. Student-view test results
11. Pre-launch communication scheduled
12. Backup & changelog
13. Term-open daily checks plan

---

## False-Positive Prevention

❌ **DON'T:**
- Open the shell without student-view testing
- Let the gradebook contradict the syllabus
- Release everything on day 1 if pacing matters
- Skip accessibility — it's not optional
- Assume integrations work — test each one
- Forget to schedule the welcome message

✅ **DO:**
- Verify settings, roster, and dates first
- Hide unused nav
- Make Home a navigation hub, not a content dump
- Sync gradebook with syllabus exactly
- Pass accessibility checker
- Test as a student
- Plan term-open daily checks

---

## Quality Indicators

- [ ] All settings verified (dates, roster, roles)
- [ ] Navigation pruned to essentials
- [ ] Modules sequenced with release dates
- [ ] Gradebook math matches syllabus
- [ ] Integrations tested
- [ ] Accessibility checker passes
- [ ] Student-view test passes
- [ ] Welcome announcement scheduled

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-02** | Settings → navigation → home → syllabus → modules → gradebook → communication → integrations → accessibility → student test → launch pipeline. |
| **CM-02** | Constrains nav-item count, gradebook consistency, and pre-launch sign-off. |
| **OC-01** | Numbered checklist enforces verifiable, paste-ready setup. |
| **DS-02** | Platform-agnostic structure with platform-specific notes per LMS. |
| **QA-01** | Student-view test verifies learner experience, not just instructor view. |
