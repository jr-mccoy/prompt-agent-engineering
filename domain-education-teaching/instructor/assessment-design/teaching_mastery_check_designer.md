---
title: "Mastery Check Designer"
category: education-teaching/assessment
description: "Design a binary pass/retry mini-assessment for a single skill — with a mastery threshold, a parallel retry version, and a teacher note on what 'not yet' means instructionally."
techniques:
  - ST-01
  - QA-04
  - DS-01
  - OC-01
  - QA-11
difficulty: beginner
tags:
  - assessment
  - mastery
  - formative-assessment
  - mastery-based-grading
  - standards-based
  - retry
  - competency
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/assessment/assessment_quiz_to_reteach_plan.md
  - domain-education-teaching/assessment/assessment_item_difficulty_calibrator.md
  - domain-education-teaching/teaching_exit_ticket_generator.md
  - domain-education-teaching/assessment/assessment_standards_based_grading_converter.md
---

# Mastery Check Designer

## Objective

Produce a short, focused mastery check for a single skill — with a clearly defined pass/retry threshold, a parallel retry version (same construct, different surface), and a teacher guide on what to do instructionally when students don't pass.

## When to Use

- Standards-based or mastery-based grading systems
- Competency checkpoints before students advance to the next skill
- After a reteach to verify that understanding shifted
- When you want a lightweight, low-stakes instrument (not a full test)
- When the question is binary: "Can the student do this specific thing?"

## When NOT to Use

- When you're assessing multiple objectives at once — use `assessment_test_blueprint_table_of_specs.md`
- When you need diagnostic detail about *why* they didn't pass — use `assessment_short_answer_item_writer.md` or `assessment_hinge_question_designer.md`
- For holistic performance assessment — use `assessment_performance_task_designer.md`

---

## Inputs Needed

- **Single skill or objective:** [SWBAT + one observable skill — e.g., "SWBAT solve two-step linear equations with integer coefficients"]
- **Grade / level:** [e.g., Grade 7, Algebra I]
- **Number of items:** [Typical: 4–6 for most skills]
- **Mastery threshold:** [e.g., 4/5 correct, or 3/4, or 80% — state your preference or accept a recommendation]
- **Format:** [MC / short answer / calculation / fill-in / combination]
- **How retry is triggered:** [Any non-pass / 2 consecutive non-passes / teacher judgment]

---

## Instructions

### Step 1: Confirm the Skill Is Checkable

Write a one-sentence operationalization: "A student who has mastered this skill will, when shown [type of problem/prompt], [what they will do correctly, every time, without scaffolding]."

If the skill can't be completed in this sentence (too broad, too vague, depends on other skills), flag it and suggest how to narrow it.

### Step 2: Design Version A — Primary Check (4–6 items)

Design the check so:
- All items target the exact skill stated (no tangential concepts)
- Item 1 is slightly more straightforward (reduces test anxiety, confirms the skill is present)
- Items 2–4 vary the surface (different numbers, contexts, or representations — not different skills)
- Item 5–6 (if included) applies the skill in a slightly different context (still the same skill, not a harder skill)

```
MASTERY CHECK — VERSION A
─────────────────────────────────────────────
Skill: [Exact statement]
Items: [N]
Estimated time: [N minutes]
Materials needed: [Calculator / ruler / reference sheet / none]

ITEMS:

1. [Item text]
   Answer: [Correct answer]
   Credit: [Full/partial criteria if applicable]

2. [Item text]
   Answer: [...]

3. [Item text]
   Answer: [...]

4. [Item text]
   Answer: [...]

[5–6 if included]
```

### Step 3: Set the Mastery Threshold

```
MASTERY THRESHOLD
─────────────────────────────────────────────
Pass threshold: [N/N correct] — [% equivalent]

Rationale: [Why this threshold? e.g., "4/5 requires consistent performance
across varied surface features, not lucky single-item success.
One error is permitted for transcription/computation errors that don't
indicate conceptual gaps."]

What counts as passing on constructed-response items:
[If not pure MC — what constitutes a full-credit response]

Notes on scoring edge cases:
[e.g., "Accept any equivalent form of the answer" / "Partial credit is not
sufficient for a pass — all-or-nothing for this skill"]
```

### Step 4: Design Version B — Retry Check

Produce a parallel version with different surface features but identical construct demand:

```
MASTERY CHECK — VERSION B (RETRY)
─────────────────────────────────────────────
Skill: [Same exact statement as Version A]
Construction principle: Different numbers / contexts / representations — NOT a different skill or easier items.

ITEMS:

1. [Item text — parallel structure to Version A Item 1, different values]
   Answer: [...]

2–4. [...]

Equivalence check: [Confirm that each Version B item maps to the corresponding
Version A item at the same difficulty level]
```

### Step 5: Teacher Guide — What "Not Yet" Means

```
TEACHER GUIDE: RESPONDING TO "NOT YET"
─────────────────────────────────────────────

WHAT A NON-PASS USUALLY REVEALS:
[Based on the skill, what are the 2–3 most common reasons students don't pass?
Be specific — not "doesn't understand" but "reverses the operation order" / "misapplies the rule to this step"]

IMMEDIATE NEXT STEP (before retry):
[What to do before giving Version B — a specific reteach move, activity, or conversation.
Not "review the notes" — a concrete instructional action.]

IF SECOND ATTEMPT ALSO FAILS:
[Escalation option — small group pull, modified approach, prerequisite check using
`assessment_diagnostic_quiz_knowledge_map.md`]

SCHEDULING NOTE:
[Recommended wait time between attempt and retry — e.g., "Allow at least one additional
practice session before retry" / "Same-day retry acceptable for computation skills"]
```

---

## Output Format

1. Skill operationalization statement
2. Mastery Check Version A (4–6 items with answers)
3. Mastery threshold with rationale
4. Mastery Check Version B (parallel retry)
5. Teacher guide (not-yet response, immediate next step, escalation)

---

## False-Positive Prevention

❌ **DON'T:**
- Include items that test a different skill (even a related one) — this is a check of one thing
- Set the threshold at 100% unless the skill genuinely requires zero error (safety-critical operations)
- Write a Version B that is easier than Version A — it must be equivalent, not a "gimme pass"
- Write a "not yet" guide that just says "reteach the concept" — name the specific instructional move
- Use this check as a grade in a traditional grading system without allowing retries

✅ **DO:**
- Operationalize the skill so tightly that every item clearly belongs
- Vary the surface across items (not the construct) so passing requires real consistency
- Justify the threshold — don't pick 80% arbitrarily
- Make Version B visually and structurally distinguishable so students see it as a fresh start
- Specify a concrete next step before retry — the check isn't useful without a response plan

---

## Quality Indicators

- [ ] Single skill stated precisely and operationalized
- [ ] Items vary surface features, not skill demands
- [ ] Mastery threshold stated with rationale
- [ ] Version B is parallel in difficulty to Version A
- [ ] Teacher guide names specific instructional moves, not generic re-teaching

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-01** | Skill operationalization anchors all design decisions. |
| **QA-04** | Mastery threshold defined upfront; outcome evaluated against it. |
| **DS-01** | Item design governed by skill taxonomy (what "mastery" means for this type of skill). |
| **OC-01** | Standard check template applied to both versions for consistency. |
| **QA-11** | Binary pass/retry logic with explicit threshold and escalation path. |
