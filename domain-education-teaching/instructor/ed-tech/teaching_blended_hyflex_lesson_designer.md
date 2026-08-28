---
title: "Blended / HyFlex Lesson Designer"
category: education-teaching/instructor/ed-tech
description: "Design a single blended or HyFlex lesson where in-person, sync online, and async learners get equivalent experience and outcomes — not 'in-person plus afterthoughts.'"
techniques:
  - ST-02
  - CM-02
  - DS-02
  - OC-01
  - QA-01
difficulty: advanced
tags:
  - blended-learning
  - hyflex
  - hybrid
  - online-learning
  - higher-education
  - secondary
  - lesson-design
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/instructor/lesson-planning/teaching_lesson_plan_generator.md
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_online_course_conversion.md
  - domain-education-teaching/instructor/ed-tech/teaching_class_slide_deck_designer.md
---

# Blended / HyFlex Lesson Designer

## Objective

Design a single lesson that simultaneously serves in-person, synchronous remote, and (often) asynchronous learners with equivalent learning experience — not a lecture broadcast with chat. Output is a single lesson plan with parallel tracks, shared artifacts, and an explicit equity test.

## When to Use

- Course offered as HyFlex (students choose modality per session)
- Hybrid course where some students are remote, some on-site
- Sync class with regular asynchronous viewers (recordings)
- Co-teaching across distance
- Anytime "we'll just stream the in-person class" has been failing

## When NOT to Use

- Single-modality lesson — use `teaching_lesson_plan_generator.md`
- Whole-course conversion — use `hecorp_online_course_conversion.md`
- Async-only module — use `hecorp_async_lms_module_designer.md`

---

## Inputs Needed

- **Subject and topic:** [...]
- **Population:** [Grade band / role; rough split across modalities]
- **Lesson length:** [...]
- **Modality split expected:** [% in-person / % sync remote / % async]
- **Tech stack:** [Conferencing tool, LMS, polling, shared docs, mics in room, second screen]
- **Room setup:** [Camera angle, mic coverage, board visibility]
- **Async expectations:** [Will async learners watch the recording? Submit equivalent work?]
- **Learning objectives:** [2–4 measurable]
- **Equity priority:** [Especially what async/remote learners must not lose]

---

## Instructions

### Step 1: Test the "Equivalent, Not Identical" Frame

HyFlex done badly: in-person learners get the real lesson; remote/async learners get a worse version.

Equivalent means: each modality has a path to the same objective, with comparable engagement, evidence, and feedback. Not necessarily identical activities.

State up front: how will I verify a remote/async learner had an equivalent experience?

### Step 2: Design Activities That Travel

The most common failure: an activity that only works in-person (e.g., "find a partner near you") leaves remote learners stranded. Audit every activity:

| Activity | In-person | Sync remote | Async |
|----------|-----------|-------------|-------|
| Hook | [How] | [How] | [How — recorded?] |
| Pair work | [How] | [Breakout? cross-modal pairing?] | [Discussion post / asynchronous pair?] |
| Discussion | [How] | [How — chat parity?] | [Threaded with prompt?] |
| Practice | [How] | [How] | [How] |
| Check for understanding | [How] | [How] | [How] |
| Synthesis | [How] | [How] | [How] |

Where a row has weak modality coverage, redesign before scheduling.

### Step 3: Choose a Cross-Modal Coordination Pattern

| Pattern | When to use |
|---------|-------------|
| **Single shared activity** — same task, all modalities use shared digital artifact | Most reliable; default |
| **Parallel tracks** — different activities with same objective | When tools differ widely |
| **Cross-modal pairing** — in-person paired with remote learner | Deliberately disrupts isolation; works at small scale |
| **Async leads sync** — async learners post first; sync builds on it | Async voices visible, not lost |

Pick one per major activity; don't switch mid-session.

### Step 4: Tech Reality Check

For each activity, what tech is required and what fails when?

| Activity | Required tech | Single-point-of-failure | Fallback |
|----------|---------------|--------------------------|----------|
| Live polling | Polling tool, internet | Polling tool down | Hand-raise / chat-vote / paper |
| Breakout discussion | Conferencing tool | Conferencing tool down | Pair in-person; remote uses chat |
| Shared whiteboard | Whiteboard app | App down | Camera on physical board + chat |
| Video clip | Streaming | Network lag | Pre-loaded; share link for individual viewing |

If a single failure breaks the whole lesson, redesign.

### Step 5: Voice & Visibility Plan

Most-overlooked: ensuring remote learners can be seen and heard, not just spoken-to.

- Camera that captures the front + the class (not just instructor)
- Mic that picks up student voices (or dedicated student mic)
- Repeat in-person student questions for remote audio
- Remote video on a screen visible from the front (the "back row" of the room)
- Chat monitor (TA, co-teacher, or assigned student rotation)
- Async voices: how do they appear in the live session? (Pre-posted prompts read aloud, async questions answered)

### Step 6: Activity Templates That Work Across Modalities

**Think-pair-share, cross-modal:**
- All learners think (1 min, silent)
- Pair: in-person pair with neighbor; remote pair via breakout; async pairs via discussion thread; mix ratios as practical
- Share: shared doc captures one sentence per pair → instructor surfaces patterns

**Live worked example with parallel practice:**
- Instructor models on shared screen / doc-cam
- All learners attempt same problem in shared doc
- Instructor circulates digitally + physically
- Whole-group debrief

**Asynchronous-first reading:**
- All learners read & post one question pre-class
- Live session begins by addressing top 3 student questions
- Async catch-ups review the recording with same questions in mind

### Step 7: Async Rigor Plan

Async learners need equivalent rigor, not equivalent passivity.

- A recorded session alone is not equivalent — it's lecture-watching
- Pair the recording with a structured task they complete (problem, post, reflection, artifact)
- Set a deadline (within 48–72 hr typical) for the async track
- Ensure async submissions feed back into the next session

### Step 8: Assessment Equivalence

Ensure all learners can demonstrate the same objective:

- If you assess via in-class participation, build async parallel (post, artifact)
- Avoid surveillance proctoring as the integrity strategy — design assessments that are robust regardless of modality
- Use rubrics that don't privilege presence (e.g., not rewarding raised hands)

### Step 9: Run-Sheet

Produce a runnable run-sheet for the lead instructor:

```
00:00 — Open camera, share screen, post agenda in chat
00:01 — Welcome + frame, monitor chat for arrivals
00:05 — Hook (works for all modalities)
00:10 — Pair activity: in-person, breakout, async
00:18 — Reconvene; surface from shared doc
...
```

Include cues for: TA actions, chat monitor, transition signals.

### Step 10: Equity Audit

- [ ] Is the remote learner included by default, not exception?
- [ ] Does the async learner have an equivalent path to the same objective?
- [ ] Are camera/mic/captions ensuring sensory access?
- [ ] Are time-zone differences considered for sync sessions?
- [ ] Do norms protect remote learners' airtime?
- [ ] Is the recording captioned and posted promptly?

### Step 11: Post-Lesson Iteration

Triangulate signal:
- Quick poll across modalities (was the experience equivalent?)
- Submission patterns (are async submissions weaker / fewer?)
- Office-hours questions split (where do questions cluster?)
- Adjust activities or coordination pattern next session

---

## Output Format

1. Equivalent-not-identical frame statement
2. Activity-by-modality audit
3. Coordination pattern per activity
4. Tech reality check + fallbacks
5. Voice & visibility plan
6. Cross-modal activity templates
7. Async rigor plan
8. Assessment equivalence audit
9. Runnable run-sheet
10. Equity audit
11. Post-lesson iteration plan

---

## False-Positive Prevention

❌ **DON'T:**
- Treat the remote learner as the exception
- Assume "we'll figure it out" with the tech
- Let async = "watch the recording" with no task
- Skip captioning the recording
- Build activities that only work in-person
- Confuse equivalent with identical

✅ **DO:**
- Plan parallel modality paths
- Build a fallback for each tech-dependent activity
- Make remote learners visible and audible
- Pair async with structured tasks
- Audit for equity

---

## Quality Indicators

- [ ] Every activity has a modality-by-modality plan
- [ ] Coordination pattern is named per activity
- [ ] Tech failure modes have fallbacks
- [ ] Async path has rigorous task, not just recording
- [ ] Equity audit complete

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-02** | Frame → activity audit → coordination → tech → run-sheet pipeline. |
| **CM-02** | Equivalence constraint and tech-fallback requirement prevent in-person bias. |
| **DS-02** | Multi-modality routing with explicit per-modality activity plans. |
| **OC-01** | Run-sheet template enforces minute-by-minute output. |
| **QA-01** | Equity audit and post-lesson signal triangulation close the loop. |
