---
title: "Multiple-Choice Item Writer with Distractor Analysis"
category: education-teaching/instructor/assessment-items
description: "Generate psychometrically defensible multiple-choice items — stem, key, and 3 distractors — each anchored to a specific objective, DOK level, and named misconception, with distractor rationale and item card."
techniques:
  - CM-01
  - ST-02
  - DS-01
  - OC-01
  - QA-02
difficulty: advanced
tags:
  - assessment
  - multiple-choice
  - item-writing
  - distractors
  - dok
  - blooms
  - test-design
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/instructor/assessment-design/teaching_assessment_rubric_builder.md
  - domain-education-teaching/instructor/response-cycle/teaching_misconception_diagnoser.md
  - domain-education-teaching/instructor/assessment-design/teaching_test_blueprint_table_of_specs.md
---

# Multiple-Choice Item Writer with Distractor Analysis

## Objective

Produce defensible multiple-choice items with stems that meet best-practice rules, exactly one defensible key, and distractors each tied to a specific named misconception. Each item ships with an item card capturing objective, DOK, key rationale, and distractor diagnostics.

## When to Use

- Building a unit test, common formative assessment, quiz, or item bank
- Test prep for standardized exams (SAT/ACT/AP/state)
- Replacing recall-heavy items with items that diagnose misconceptions
- Building items that yield instructional information from wrong answers

## When NOT to Use

- Constructed response or essay — use `teaching_assessment_rubric_builder.md`
- Performance task — use `assessment_performance_task_designer.md`
- Diagnostic of student errors after testing — use `teaching_misconception_diagnoser.md`

---

## Inputs Needed

- **Subject and topic:** [e.g., 7th grade math, ratio reasoning]
- **Learning objective(s):** [SWBAT… one per item or one per item set]
- **Number of items:** [N]
- **DOK level(s):** [1 Recall / 2 Skill-Concept / 3 Strategic / 4 Extended]
- **Format:** [Standard 4-option / 5-option / 2-tier with reasoning]
- **Use case:** [Formative / summative / item bank / test prep for specific exam]
- **Known student misconceptions (optional):** [List from prior data if available]

---

## Instructions

### Step 1: Item-Writing Rules (Apply to Every Item)

**Stem rules:**
- State a complete question or partial sentence; avoid trivia
- No negatives in stem unless absolutely necessary; if used, BOLD/underline the negative ("Which is NOT…")
- Avoid "all of the above" / "none of the above"
- No clue words that point to the key (length, grammar agreement, qualifiers like "always/never")
- No double-barrel questions

**Option rules:**
- Exactly one defensible key
- Distractors are plausible to a student who hasn't mastered the objective
- Options are parallel in length, structure, and grammar
- Distractors are mutually exclusive
- Order options logically (numerical: ascending; alphabetical otherwise) — never key-position bias

**Cognitive rules:**
- DOK level matches the verb in the objective
- For DOK 2+, item requires reasoning beyond recognition
- Reading load doesn't exceed grade level (unless reading is the construct)

### Step 2: Item Generation

For **each item**, output the following item card:

```
ITEM N
─────────────────────────────────────────────
Objective:        [SWBAT verb + content]
Standard:         [Code]
DOK:              [1 / 2 / 3 / 4]
Bloom's level:    [Verb category]
Item type:        [Single-answer MC, 4 options]

STEM:
[Full stem text — figure or table description if applicable]

OPTIONS:
A) [Text]
B) [Text]
C) [Text]
D) [Text]

KEY: [Letter]

KEY RATIONALE:
[Why this option is correct — the reasoning a student must use]

DISTRACTOR ANALYSIS:
| Option | Misconception/Error | Probability | Instructional Response |
|--------|--------------------|-------------|------------------------|
| [Wrong A] | [Specific error name] | High/Med/Low | [What to reteach] |
| [Wrong B] | | | |
| [Wrong C] | | | |

DIFFICULTY ESTIMATE: [Easy / Medium / Hard] — based on [reasoning]

ACCESSIBILITY NOTES:
- Reading level: [Estimated grade]
- Visual elements: [Described, alt text provided]
- ELL considerations: [Vocabulary that may be unfamiliar but is not the construct]
```

### Step 3: Distractor Discipline

For each distractor, name a **specific** misconception, error type, or partial reasoning. Vague distractors ("looks similar to the key") are not acceptable. Categories include:

- **Procedural error** (e.g., subtracted instead of added; flipped numerator and denominator)
- **Conceptual misconception** (e.g., longer decimal = larger number)
- **Reading/parsing error** (e.g., answered the question that wasn't asked)
- **Surface feature attractor** (e.g., used the most prominent number)
- **Partial knowledge** (e.g., correct concept, wrong final step)

If you can't name a specific misconception for a distractor, the distractor is too random and should be replaced.

### Step 4: Item Set Quality Audit

After generating N items, audit the set:

| Audit | Pass / Fix |
|-------|-----------|
| Key positions distributed roughly evenly across A/B/C/D | |
| DOK distribution matches request | |
| No two items test the same fact in the same way | |
| Reading load consistent with grade band | |
| Cumulative time estimate ≤ assessment window | |
| At least one item per stated objective | |
| Each distractor maps to a specific misconception | |

### Step 5: Optional — 2-Tier Items

If 2-tier format requested, each item has:
- Tier 1: standard MC question
- Tier 2: "Why did you choose your answer?" with 3–4 reasoning options
This format diagnoses whether right answers came from right reasons.

### Step 6: Bias and Fairness Check

For the full set:
- [ ] No items disadvantage students based on cultural references they may not share
- [ ] No items use proper nouns / contexts that could trigger stereotype threat
- [ ] Number/name diversity across items
- [ ] Visual representations don't depend on color alone
- [ ] No regional vocabulary if not the construct (e.g., "bodega" vs "corner store")

Flag and fix any concerns.

---

## Output Format

1. Item-writing parameters summary
2. N item cards in the standard format
3. Item set audit table
4. Bias and fairness check
5. Estimated total testing time
6. Suggested administration order (typically easy → hard, with confidence-building first item)

---

## False-Positive Prevention

❌ **DON'T:**
- Write distractors that are obviously wrong to anyone — they discriminate nothing
- Use "all of the above" or "none of the above"
- Write stems with grammatical clues to the key
- Test trivia unrelated to the objective
- Tag every distractor as "looks similar" without naming the misconception

✅ **DO:**
- Tie every distractor to a named, instructional misconception
- Write parallel-structured options
- Audit key positions for distribution
- Provide rationale not just for the key but for why each distractor exists
- Specify DOK and confirm the item actually requires that level

---

## Quality Indicators

- [ ] All items follow stem and option rules
- [ ] Every distractor has a named misconception
- [ ] DOK distribution matches request
- [ ] Key positions are distributed
- [ ] Each item maps to at least one stated objective
- [ ] Bias/fairness check completed
- [ ] Cumulative time fits the testing window

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Subject, objective, DOK, and use case anchor every item. |
| **ST-02** | Sequential rules → items → audit → bias check. |
| **DS-01** | DOK and Bloom's frameworks govern item design and distribution. |
| **OC-01** | Item card template enforces reproducible structure. |
| **QA-02** | Distractor analysis and item-set audit stress-test items before release. |
