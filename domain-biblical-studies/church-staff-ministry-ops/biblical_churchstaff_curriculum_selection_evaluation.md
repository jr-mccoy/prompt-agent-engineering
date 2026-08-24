---
title: "Curriculum Selection & Evaluation — Assess Published Bible-Study Materials"
category: biblical-studies/church-staff-ministry-ops
description: "Evaluate published Bible-study curriculum materials against stated criteria — theological alignment, age-appropriateness, pedagogical quality, tradition fit, volunteer-friendliness, and cost — without fabricating product names, authors, reviews, or publisher claims."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-04
  - DS-02
difficulty: intermediate
tags:
  - curriculum
  - evaluation
  - church-staff
  - selection
  - published-materials
updated: "2026-06-25"
related_prompts:
  - domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md
  - domain-biblical-studies/study-methods-teaching/biblical_lesson_plan_builder.md
  - domain-biblical-studies/theology-research/biblical_commentary_evaluation.md
---

# Curriculum Selection & Evaluation

**Objective:** Help a church leader evaluate published Bible-study curriculum against explicit criteria so they can make an informed selection — without the model fabricating product names, author attributions, review summaries, or publisher claims.

> **STRONG-GUARD prompt.** Evaluating published materials tempts the model to assert product details, pricing, author credentials, or review summaries from memory. It must not. The user supplies the materials or descriptions; the model evaluates against stated criteria and flags every product-specific claim as verify-required.

**When to use:**
- You are choosing between curriculum options for your church or ministry.
- You want a structured rubric to compare materials against your needs.
- You have specific materials in hand and want an evaluation framework.

**When NOT to use:**
- You are designing your own curriculum from scratch — use `biblical_churchstaff_curriculum_scope_sequence.md`.
- You are building a single lesson — use `biblical_lesson_plan_builder.md`.

**Audience:** Pastors (P) and education directors/group leaders (G).

---

## Inputs / Context

1. **The materials to evaluate.** The user describes or pastes details about the curriculum options they are considering. The model does not suggest products by name from memory.
2. **Evaluation criteria.** The user's priorities: theological alignment (and with which tradition), age-appropriateness, pedagogical quality, volunteer-friendliness, cost, format (print/digital/video), and any other criteria.
3. **Context.** Group size, leader skill level, time per session, and any non-negotiables.
4. **Declared tradition (optional).** Shapes the theological-alignment criterion.

---

## Constraints

### Must
- Evaluate only the materials the user supplies or describes — never suggest products by name from memory.
- Build the evaluation rubric from the user's stated criteria.
- Score or rank each criterion with a brief rationale.
- Flag where a curriculum's theological stance on a contested issue diverges from the user's declared tradition (or from multiple traditions if no tradition is declared).
- Note practical concerns: leader prep time, cost per participant, format constraints, accessibility.

### Must Not
- Fabricate product names, ISBNs, authors, publishers, pricing, reviews, endorsements, or publication dates.
- Assert that a curriculum "teaches X" unless the user has supplied that information — the model evaluates what the user describes.
- Endorse or dismiss a curriculum based on the model's own theological preferences.

### Tradition-neutral stance (Must / Must Not)
- **Must:** evaluate theological alignment against the user's stated criteria, not the model's.
- **Must Not:** privilege any tradition's criteria as the default standard.

---

## Instructions

### Step 1 — Confirm criteria and context
Restate the user's evaluation criteria, priorities, group context, and tradition (if declared). Ask for any missing criteria.

### Step 2 — Build the rubric
Create a rubric with the user's criteria as rows and the curriculum options as columns. Define what "strong," "adequate," and "weak" mean for each criterion.

### Step 3 — Evaluate each option
For each curriculum the user has described, score against the rubric with a brief rationale per cell. Flag any product-specific claim the model is unsure about as verify-required.

### Step 4 — Comparative summary
Summarize strengths and weaknesses of each option relative to the user's priorities. Note which option best fits which criterion.

### Step 5 — Recommendation with caveats
Offer a recommendation based on the user's stated priorities, with caveats about what the user should verify independently (pricing, current edition, doctrinal details the model cannot confirm).

---

## Output Format

```
# Curriculum Evaluation — [ministry area]

## Criteria & priorities
[restated from user input]

## Rubric
| Criterion | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| [criterion] | [score + rationale] | [..] | [..] |

## Comparative summary
- Best for [criterion]: [option]
- Concerns: [..]

## Recommendation
[recommendation with verify-required caveats]
```

---

## Verification

- [ ] Only materials the user supplied are evaluated — no products suggested from memory.
- [ ] The rubric reflects the user's stated criteria, not the model's preferences.
- [ ] Product-specific claims are flagged verify-required where uncertain.
- [ ] Theological alignment is evaluated against the user's tradition, not a default.
- [ ] Practical concerns (prep time, cost, format) are addressed.

---

## False-Positive Prevention

DON'T:
- Name, recommend, or describe specific curriculum products from memory.
- Assert pricing, authorship, or theological positions of a product the user hasn't described.
- Evaluate theological alignment against an undeclared default tradition.

DO:
- Build the rubric from the user's criteria.
- Evaluate only what the user supplies.
- Flag every product-specific factual claim as verify-required.
