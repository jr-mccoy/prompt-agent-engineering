---
title: "DOK Item Generator (All 4 Levels)"
category: education-teaching/instructor/assessment-items
description: "Generate a coordinated set of items at all 4 Depth of Knowledge levels on a single standard — recall, skill/concept, strategic thinking, and extended thinking — with item-design analysis showing why each item lives at its DOK."
techniques:
  - CM-01  # Context Framing
  - ST-02  # Sequential Steps
  - DS-01  # Framework Application (Webb's Depth of Knowledge)
  - OC-01  # Output Templates
  - QA-02  # Adversarial Verification
difficulty: intermediate
tags:
  - assessment
  - dok
  - depth-of-knowledge
  - item-writing
  - rigor
  - middle-school
  - high-school
  - test-design
updated: "2026-05-10"
related_prompts:
  - domain-education-teaching/instructor/assessment-design/teaching_test_blueprint_table_of_specs.md
  - domain-education-teaching/instructor/assessment-items/teaching_blooms_question_stem_bank.md
  - domain-education-teaching/instructor/assessment-items/teaching_mc_item_writer_with_distractors.md
---

# DOK Item Generator (All 4 Levels)

## Objective

Produce a coordinated set of items targeting one standard at all four Webb's Depth of Knowledge levels: DOK 1 (recall), DOK 2 (skill/concept), DOK 3 (strategic thinking), DOK 4 (extended thinking). Output includes the items themselves, the answer keys, and an analysis explaining why each item lives at its DOK level — the analysis is what makes the set defensible.

## When to Use

- Building rigor across an assessment that will measure depth, not just breadth
- Auditing existing items for DOK accuracy (item drift between intended and actual DOK is common)
- Training teachers in DOK leveling
- Building tasks for higher-order thinking that don't accidentally collapse to recall

## When NOT to Use

- Building a full test blueprint — use `assessment_test_blueprint_table_of_specs.md`
- Building a question stem bank by Bloom's level — use `assessment_blooms_question_stem_bank.md`
- Single MC item with distractors — use `assessment_mc_item_writer_with_distractors.md`

---

## Inputs Needed

- **Subject and grade:** [...]
- **Standard targeted:** [Code + text]
- **Available content / data the items can reference:** [Texts, datasets, scenarios]
- **Item type allowed at each DOK:** [MC / SR / ER / performance]
- **Time constraint per item:** [Influences DOK 4 design]
- **Use case:** [Test bank / classroom diagnostic / state-aligned practice]

---

## Instructions

### Step 1: Confirm DOK Definitions

Use Webb's framing, not Bloom's. Output the working definitions:

| DOK | Definition | Cognitive demand |
|-----|-----------|------------------|
| 1 | Recall and reproduction | Recite, identify, recognize. One-step. |
| 2 | Skill / concept | Apply known procedure or concept. Multi-step but routine. |
| 3 | Strategic thinking | Reason; justify; non-routine; multiple paths possible. |
| 4 | Extended thinking | Investigate; synthesize across sources; sustained over time. |

DOK is about **the cognitive work the item demands**, not about how hard the content is. A hard recall item is still DOK 1.

### Step 2: Draft DOK 1 (Recall) Item

Properties:
- One-step
- Answer is in memory or directly stated
- No interpretation required
- Often has a single right answer

Output:

```
ITEM: [...]
ANSWER: [...]
DOK 1 ANALYSIS: This is DOK 1 because [the cognitive work is recall — students retrieve a fact directly without applying it].
```

### Step 3: Draft DOK 2 (Skill / Concept) Item

Properties:
- Multi-step but procedure is known
- Apply a concept to a familiar context
- Some interpretation, but path is determined

Output:

```
ITEM: [...]
ANSWER: [...]
DOK 2 ANALYSIS: This is DOK 2 because [the student applies a known procedure / explains a concept in a routine way].
```

Distinguish from DOK 1: this item has more than one cognitive step, or requires interpretation, but the steps are determined by the content.

### Step 4: Draft DOK 3 (Strategic Thinking) Item

Properties:
- Multi-step AND requires reasoning that the student must construct
- Multiple defensible approaches or solutions possible
- Justification or evidence required
- Non-routine — student decides the path

Common DOK 3 moves: justify, defend, predict with evidence, draw inferences from data, propose a solution and explain it, compare across cases.

Output:

```
ITEM: [...]
EXPECTED RESPONSE FEATURES: [Not a single right answer — describe what a defensible response includes]
DOK 3 ANALYSIS: This is DOK 3 because [the student must reason — choose a path, defend a claim, justify with evidence].
```

Common pitfall: an item asks "explain" but the explanation is routine. That's still DOK 2. DOK 3 explanations require reasoning the student constructs.

### Step 5: Draft DOK 4 (Extended Thinking) Item

Properties:
- Sustained work over time (typically not single-test-item-sized)
- Investigate or synthesize across multiple sources
- Plan, execute, revise
- Often a multi-day task or performance assessment

DOK 4 examples:
- Conduct an investigation to address a question and report findings
- Synthesize across multiple texts to produce a research argument
- Design a solution to a real problem with constraints and revisions

Output:

```
TASK: [Multi-day or extended task description]
DELIVERABLES: [What students produce]
EXPECTED RESPONSE FEATURES: [Includes evidence of investigation, synthesis, revision]
DOK 4 ANALYSIS: This is DOK 4 because [the work spans multiple cognitive moves, synthesizes across sources, and is sustained over time].
```

If the task fits in 30 minutes, it's almost certainly not DOK 4 — flag for redesign.

### Step 6: Cross-DOK Audit

Audit your set with adversarial questions:

- [ ] DOK 1: Is this just retrieval? If a student must do anything beyond recall, it's not DOK 1.
- [ ] DOK 2: Is the procedure determined by the content? If the student decides the path, it's higher.
- [ ] DOK 3: Could the student succeed with a known procedure? If yes, it's DOK 2 in disguise.
- [ ] DOK 4: Is this sustained, investigative, synthetic? Or is it just a long DOK 3 item?

Common DOK drift:
- "Explain why" sounds DOK 3 but is often DOK 2 if the explanation is routine
- "Compare and contrast" can be DOK 2 (familiar comparison) or DOK 3 (constructed analysis) — depends on demand
- Multi-step problems are often DOK 2, not 3, if the steps are determined

### Step 7: Item Quality Checklist

Apply standard item-quality checks across all four:

- [ ] Stem is clear and free of unintended difficulty (vocabulary, ambiguous referents)
- [ ] Single best answer for selected-response items; clear rubric criteria for constructed-response
- [ ] Free of bias (cultural, gender, racial, regional)
- [ ] Free of cueing (giveaways in the stem)
- [ ] Reading level appropriate for the grade
- [ ] DOK target matches actual cognitive demand of the item

### Step 8: Sample Student Response (DOK 3 and 4)

For DOK 3 and DOK 4 items, generate a sample student response that would meet the standard. This:

- Helps the writer verify the item actually elicits the intended DOK
- Becomes part of the answer key / rubric calibration

### Step 9: Self-Check

- [ ] Is each item authentically at its claimed DOK?
- [ ] Are there no items that drift one level lower than claimed?
- [ ] Is the DOK 4 task actually extended, not just hard?
- [ ] Is the analysis paragraph for each item defensible?
- [ ] Are item-quality issues (bias, cueing, ambiguity) absent?

---

## Output Format

1. DOK working definitions
2. DOK 1 item + analysis
3. DOK 2 item + analysis
4. DOK 3 item + expected response features + analysis
5. DOK 4 task + deliverables + analysis
6. Cross-DOK audit
7. Item quality checklist
8. Sample student responses for DOK 3 and 4
9. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Treat DOK as a difficulty scale — DOK is about cognitive demand, not hardness
- Confuse Bloom's verbs with DOK levels — they don't map cleanly
- Label "explain" as DOK 3 when the explanation is routine
- Build a DOK 4 task that's just a long DOK 2 task
- Skip the analysis paragraph — that's the discipline that prevents DOK drift

✅ **DO:**
- Anchor each item with an analysis paragraph defending its DOK
- Stress-test for drift (DOK 3 collapsing to DOK 2 is the common failure)
- Make DOK 4 sustained, investigative, synthetic
- Apply item-quality checks across all levels
- Provide sample responses for higher-DOK items

---

## Quality Indicators

- [ ] All four DOK levels represented
- [ ] Each item has an analysis defending its DOK
- [ ] DOK 3 requires constructed reasoning, not routine explanation
- [ ] DOK 4 is genuinely extended, not just hard
- [ ] Cross-DOK audit completed
- [ ] Item-quality checks applied
- [ ] Sample responses provided for DOK 3 and 4

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Standard, grade, and use-case anchor item content and DOK targets. |
| **ST-02** | Nine-step build moves through all four DOK levels with analysis at each. |
| **DS-01** | Webb's DOK framework structures the items and the analysis discipline. |
| **OC-01** | Item-plus-analysis template enforces defensible DOK leveling. |
| **QA-02** | Cross-DOK audit and self-check stress-test for level drift and routine-explanation traps. |
