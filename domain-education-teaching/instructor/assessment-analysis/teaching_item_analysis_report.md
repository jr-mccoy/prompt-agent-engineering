---
title: "Item Analysis Report"
category: education-teaching/assessment
description: "Take class quiz results and produce a diagnostic item analysis — difficulty indices, distractor frequency patterns, items to flag, student error clusters, and a prioritized reteach agenda — designed for classroom teachers, not psychometricians."
techniques:
  - ST-01
  - RT-02
  - QA-05
  - AG-02
  - DS-01
difficulty: intermediate
tags:
  - assessment
  - item-analysis
  - data-driven
  - diagnostic
  - reteach
  - formative-assessment
  - instructional-response
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/assessment/assessment_quiz_to_reteach_plan.md
  - domain-education-teaching/assessment/assessment_item_difficulty_calibrator.md
  - domain-education-teaching/assessment/assessment_diagnostic_quiz_knowledge_map.md
  - domain-education-teaching/assessment/assessment_mastery_check_designer.md
---

# Item Analysis Report

## Objective

Convert raw quiz or test results into an item-by-item diagnostic report — flagging items that are too easy or too hard, surfacing distractor patterns, clustering students by error type, and delivering a prioritized reteach agenda — without requiring statistical software or psychometric expertise.

## When to Use

- After administering any scored quiz or test with defined correct answers
- When you want to make grading data instructionally useful, not just a score report
- PLC/grade-level team analysis of common formative assessments
- When a class performed unexpectedly well or poorly and you want to understand why
- Before planning reteach so you're responding to actual errors, not assumptions

## When NOT to Use

- Before administering an assessment — use `assessment_item_difficulty_calibrator.md` for pre-administration estimates
- For holistic rubric scoring — this prompt works with scored right/wrong data
- For qualitative analysis of open-ended responses — this handles structured item data

---

## Inputs Needed

- **Quiz / test items:** [Paste the questions, OR describe as "Items 1–10, Science Quiz Unit 4"]
- **Topics per item:** [e.g., Item 1 = photosynthesis, Item 2 = cell structure — needed for reteach agenda]
- **Class results data:** [Choose one format:]
  - **Option A:** Score-per-student table: Student | Q1 | Q2 | Q3 … (1=correct, 0=wrong)
  - **Option B:** Item summary: Q1: 18/24 correct; Q2: 9/24 correct…
  - **Option C:** Distractor data: Q1: A=3, B=18(key), C=2, D=1
  - **Option D:** Describe verbally — "Most students got Q3 wrong; about half chose answer B"
- **Number of students:** [N]
- **Learning objectives (optional):** [For objective-level summary]

---

## Instructions

### Step 1: Per-Item Difficulty Index

For each item, calculate (or estimate from described data) the p-value:

```
ITEM DIFFICULTY ANALYSIS
─────────────────────────────────────────────
Item | Topic | # Correct | # Students | p-value | Difficulty Flag
─────────────────────────────────────────────
Q1   | [Topic] | [N] | [N] | [p] | [Easy/Medium/Hard/Flag]
Q2   | ...
...
─────────────────────────────────────────────

Flagging criteria used:
• p > .90 → "Too Easy" — flag for possible removal or replacement
• p < .25 → "Very Hard" — flag for investigation (bad item or untaught content?)
• p .25–.45 → "Hard" — note, but may be intentional
• p .45–.75 → "Medium" — target zone for most formative items
• p .75–.90 → "Easy" — acceptable as confidence builders
```

### Step 2: Distractor Frequency Analysis (For MC Items)

For any item where distractor data is available or estimable:

```
DISTRACTOR FREQUENCY ANALYSIS — ITEM [N]: [Topic]
─────────────────────────────────────────────
Option | Text / Description | # Chose | % | Role | Interpretation
─────────────────────────────────────────────
A      | [text]             | [N]     | [%] | [Key/Distractor] | [What this pull means]
B(key) | [text]             | [N]     | [%] | Key             |
C      | [text]             | [N]     | [%] | Distractor | [Misconception if identifiable]
D      | [text]             | [N]     | [%] | Distractor | [...]

DISTRACTOR NOTE:
• If a distractor pulls more students than the key → "Dominant distractor" — flag
• If a distractor pulls <5% → "Non-functional" — may be too obviously wrong
• If one distractor pulls > [N]% → [Named misconception if identifiable]
```

### Step 3: Flag Items for Review

```
FLAGGED ITEMS
─────────────────────────────────────────────

TOO EASY (p > .90):
Items: [N, N…]
Notes: [Limited diagnostic value; may be worth removing or replacing]

DOMINANT DISTRACTOR (distractor chose more than key):
Items: [N, N…]
Notes: [Item may be poorly written, answer key may be wrong, or content was not taught]

POSSIBLE BAD ITEMS (ambiguous or flawed):
Items: [N, N…]
Indicators: [e.g., bimodal response, high omit rate, both B and C pulled equally]
Recommendation: [Review item wording / check answer key / discard from scoring]

VERY HARD (p < .25):
Items: [N, N…]
Notes: [Was this taught? Is this appropriate for the assessment purpose?]
```

### Step 4: Student Error Clusters

Group students by shared error patterns — not by total score:

```
STUDENT ERROR CLUSTERS
─────────────────────────────────────────────

CLUSTER 1: [Name this cluster by what students got wrong]
Students: [N students — list names if provided, otherwise count]
Pattern: Missed items [N, N, N] — all related to [concept/topic]
What this suggests: [Specific gap description]
Reteach priority: [High/Medium/Low]

CLUSTER 2: [Name — e.g., "Procedural errors in items 4, 7, 9"]
Students: [N]
Pattern: [...]
What this suggests: [...]

CLUSTER 3: [Name — e.g., "Single isolated errors — no clear pattern"]
Students: [N]
What this suggests: Careless errors or item-specific difficulty; may not require reteach

[MASTERY GROUP: Students who passed all or all-but-one — ready for extension]
Students: [N]
```

### Step 5: Prioritized Reteach Agenda

```
RETEACH AGENDA — RANKED BY IMPACT
─────────────────────────────────────────────

PRIORITY 1: [Topic/concept — most students missed this]
Items affected: [N, N]
Students affected: [N] ([%] of class)
Recommended response: [Specific reteach activity or approach]
Estimated time needed: [N minutes]

PRIORITY 2: [Topic/concept]
Items affected: [N]
Students affected: [N]
Recommended response: [...]
Estimated time needed: [...]

PRIORITY 3: [Topic — smaller group or lower-stakes gap]
Response: [Small-group pull / independent practice / peer tutoring]

EXTENSION PLAN (for mastery group):
[What students who mastered all content should do while others reteach]
```

---

## Output Format

1. Per-item difficulty table with p-values and flags
2. Distractor frequency analysis for MC items
3. Flagged items (too easy, dominant distractor, bad item, very hard)
4. Student error clusters
5. Prioritized reteach agenda

---

## False-Positive Prevention

❌ **DON'T:**
- Group students by total score and call that an "analysis" — error clusters reveal more than scores
- Treat a dominant distractor as automatically meaning a bad item — it may mean the content was not taught
- Flag p < .25 items as "bad" without first checking if the content was covered
- Reteach everything — prioritize by number of students affected and instructional stakes
- Treat a cluster analysis as diagnostic certainty — it points to where to look, not what to find

✅ **DO:**
- Investigate flagged items before discarding them from scoring
- Name error clusters by what students believed, not by their score (e.g., "reversed the rule" not "low scorers")
- Produce a reteach agenda ranked by impact, not by item order
- Identify a mastery group and plan an extension so reteach time doesn't waste those students
- Note when data is insufficient for confident interpretation and recommend follow-up

---

## Quality Indicators

- [ ] Every item has a p-value (calculated or estimated) with interpretation
- [ ] Distractor analysis provided for MC items where data is available
- [ ] Flagged items have specific next-step recommendations
- [ ] Error clusters named by concept, not by score tier
- [ ] Reteach agenda ranked and includes estimated time per priority
- [ ] Extension plan included for mastery-level students

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-01** | Structured pipeline: difficulty → distractors → flags → clusters → agenda. |
| **RT-02** | Multi-dimensional analysis: difficulty, distractor pull, and cluster pattern simultaneously. |
| **QA-05** | Comparative analysis across items using p-values and distractor frequency benchmarks. |
| **AG-02** | Synthesizes item-level data into class-level clusters and prioritized agenda. |
| **DS-01** | Topics mapped to objectives so the reteach agenda is aligned to learning goals. |
