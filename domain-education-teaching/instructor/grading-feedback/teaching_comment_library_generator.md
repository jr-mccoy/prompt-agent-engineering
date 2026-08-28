---
title: "Reusable Comment Library Generator"
category: education-teaching/instructor/grading-feedback
description: "Build a personal comment library indexed by rubric criterion and severity tier — so high-leverage feedback can be deployed quickly across a stack while staying specific enough to drive revision."
techniques:
  - CM-01
  - ST-02
  - DS-01
  - OC-01
  - QA-02
difficulty: intermediate
tags:
  - grading
  - feedback
  - comment-bank
  - rubric
  - efficiency
  - reusable
  - middle-school
  - high-school
updated: "2026-05-10"
related_prompts:
  - domain-education-teaching/instructor/grading-feedback/teaching_essay_feedback_by_rubric.md
  - domain-education-teaching/instructor/grading-feedback/teaching_speed_grading_triage.md
  - domain-education-teaching/instructor/assessment-design/teaching_assessment_rubric_builder.md
---

# Reusable Comment Library Generator

## Objective

Produce a teacher's reusable comment library, indexed by rubric criterion and severity tier (working / approaching / not-yet), with placeholders for personalization. Output enables fast feedback across a stack while preventing the failure mode of generic-canned-comment feedback that students learn to ignore.

## When to Use

- High grading volume teachers wanting to standardize their feedback
- PLCs aligning feedback language across a course
- Building a year-one comment library to refine over time
- Onboarding new teachers to a department's feedback standards

## When NOT to Use

- Single essay feedback for one student — use `grading_essay_feedback_by_rubric_criterion.md`
- Triage protocol for a stack — use `grading_speed_grading_triage.md`
- Building the rubric itself — use `teaching_assessment_rubric_builder.md`

---

## Inputs Needed

- **Subject and grade:** [...]
- **Genre / task type:** [What kind of work this library will comment on — argument essay, lab report, math problem set, presentation, project]
- **Rubric or criteria the library will index:** [List of criteria with brief descriptors]
- **Personalization placeholders allowed:** [E.g., {student_name}, {quoted_student_text}, {specific_data}]
- **Tone / register:** [Direct / warm / mix]
- **Length range per comment:** [Brief / standard / extended; default: 1–3 sentences]
- **How comments will be used:** [In-margin / end-of-piece / digital comment bank]

---

## Instructions

### Step 1: Confirm Criteria and Tiers

For each rubric criterion, the library will produce comments at three severity tiers:

| Tier | When to use |
|------|-------------|
| **Working / strength** | The student is doing the criterion well; name what specifically |
| **Approaching / partial** | The student is partway there; name the gap and the next move |
| **Not yet / significant gap** | The criterion is missing or substantially off; redirect and re-anchor |

Output a planning grid:

| Criterion | Working comments | Approaching comments | Not-yet comments |
|-----------|------------------|---------------------|------------------|

### Step 2: Comment Anatomy

Every comment in the library should have this structure:

```
[Specific move named] + [{personalization placeholder}] + [next-move guidance, if not "working" tier]
```

Examples:

- *Working:* "Your claim sharpens the question — when you write {quoted_text}, you take a position rather than describing one."
- *Approaching:* "Your claim is descriptive: {quoted_text}. To strengthen, name what you're arguing about it, not just what it's about."
- *Not yet:* "I can't find a claim that takes a position. Look at where you set up your argument — try writing one sentence that says what you think, not what others think."

### Step 3: Generate Comments by Criterion × Tier

For each criterion, generate 3–5 comments at each tier. Vary:

- The phrasing (so the comment doesn't always start the same way)
- The diagnostic frame (sometimes "what's there," sometimes "what's missing," sometimes "what would lift this")
- The next-move specificity

Example output for "Argument criterion" in an argumentative essay:

```
WORKING TIER (3 variants)
1. Your argument has a position that isn't obvious — when you write {quoted_text}, you stake a claim others might disagree with. That's the move.
2. The argument escalates rather than restates. {quoted_text} pushes past your introduction's claim. Strong.
3. You qualify your claim with {quoted_text} — that's how careful arguments handle counter-evidence.

APPROACHING TIER (3 variants)
1. Your argument exists but stays at one level — {quoted_text}. To strengthen, push the claim past description: what's actually at stake?
2. The argument identifies an issue but doesn't yet defend a position. After {quoted_text}, what do you think should happen / be true / be done?
3. Your argument leans on assertion. After {quoted_text}, add one sentence answering "why should the reader believe this?"

NOT-YET TIER (3 variants)
1. I'm not finding a defensible claim. {quoted_text} describes the topic. What's your position on it?
2. The argument folds into summary — {quoted_text} rephrases what you read instead of taking a stance. Try a sentence beginning "I think ___ because ___."
3. Without a claim, the rest of the essay floats. Start by drafting one sentence: "My argument is that ___."
```

### Step 4: Personalization Discipline

Every comment must include at least one personalization placeholder. Comments that work without personalization train students to skim past them.

Acceptable placeholders:
- `{quoted_student_text}` — exact phrase from the student's work
- `{specific_section_or_paragraph}`
- `{student's data point or example}`
- `{student_name}` (sparingly)

The teacher fills these when deploying the comment. The library is a starting structure, not a final comment.

### Step 5: Anti-Generic Audit

Audit the library against generic-comment failure modes:

- [ ] No comment that works without a placeholder
- [ ] No vague language ("more support," "develop further," "elaborate") without a specific next move
- [ ] No comment that students would call "the comment everyone gets"
- [ ] No "good job" or "needs work" as the entire comment
- [ ] Each comment names a move, not a personal trait

### Step 6: Length Variants

Provide each comment in two lengths:

- **Brief** (1 sentence): For margin notes or speed-grading
- **Standard** (2–3 sentences): For end-of-piece comments

Example:
- Brief: "Claim is descriptive — push it to take a position, beginning at {quoted_text}."
- Standard: "Your claim describes the topic without taking a position — at {quoted_text}, you set up the question but don't answer it. Try drafting one sentence that says what you think, then re-build the rest of the introduction around it."

### Step 7: Cross-Reference Map

Map common student-error patterns to the comments that address them. This makes the library deployable, not just stored.

| Pattern in student work | Library comment(s) to consider |
|-------------------------|-------------------------------|
| Claim is restated topic | Approaching #1, Not-yet #1, #3 |
| Missing counter-claim | (cross-reference advanced rubric criterion) |
| Evidence is paraphrase, not quote | Evidence approaching #2 |

### Step 8: Update Cadence

Plan how the library evolves:

- After each major grading stack, capture 2–3 comments that worked particularly well
- Quarterly: prune comments that consistently get reused without leading to revision (those have become generic)
- Annually: full audit of the library against current rubrics

### Step 9: Self-Check

- [ ] Does every comment include a personalization placeholder?
- [ ] Are three severity tiers present per criterion?
- [ ] Are 3–5 variants per tier present?
- [ ] Are next-move actions specific?
- [ ] Are anti-generic checks passed?
- [ ] Is there a cross-reference map from error pattern → comment?

---

## Output Format

1. Planning grid (criteria × tiers)
2. Comment anatomy template
3. Library: 3–5 comments per criterion per tier
4. Length variants (brief and standard)
5. Cross-reference map (error pattern → comment)
6. Update cadence plan
7. Anti-generic audit
8. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Build comments that work without personalization placeholders
- Use vague language ("develop more," "support better") as the comment
- Build a single comment per criterion — students notice the repetition
- Skip the cross-reference map — that's what makes the library deployable
- Treat the library as static — it must evolve with student work

✅ **DO:**
- Require placeholders in every comment
- Generate 3–5 variants per criterion-tier
- Provide brief and standard lengths
- Map error patterns to comments
- Plan an update cadence

---

## Quality Indicators

- [ ] Three severity tiers per criterion
- [ ] 3–5 variants per tier
- [ ] Every comment has personalization placeholders
- [ ] Brief and standard length versions
- [ ] Cross-reference map from error pattern → comment
- [ ] Anti-generic audit passed
- [ ] Update cadence planned

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Subject, genre, rubric, and tone anchor every comment in the library. |
| **ST-02** | Nine-step build moves from criteria → comment generation → audit → evolution plan. |
| **DS-01** | Criterion × severity-tier matrix structures the library for retrieval. |
| **OC-01** | Comment-anatomy template enforces personalization and next-move discipline. |
| **QA-02** | Anti-generic audit + self-check stress-test for vague-comment failure modes. |
