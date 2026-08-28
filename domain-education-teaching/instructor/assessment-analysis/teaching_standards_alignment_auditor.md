---
title: "Standards Alignment Auditor"
category: education-teaching/instructor/assessment-analysis
description: "Audit an existing assessment for alignment to stated standards — identifying misaligned items, over-tested standards, and uncovered standards — and produce a gap-repair list with replacement item suggestions."
techniques:
  - DS-01
  - QA-01
  - ST-01
  - QA-05
  - CM-01
difficulty: advanced
tags:
  - assessment
  - standards-alignment
  - test-design
  - curriculum-alignment
  - audit
  - gap-analysis
  - standards-based
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/instructor/assessment-design/teaching_test_blueprint_table_of_specs.md
  - domain-education-teaching/instructor/assessment-analysis/teaching_standards_based_grading_converter.md
  - domain-education-teaching/instructor/assessment-items/teaching_mc_item_writer_with_distractors.md
---

# Standards Alignment Auditor

## Objective

Take an existing assessment and systematically check whether each item actually measures its claimed standard — flagging misaligned items, identifying standards with no coverage or excess coverage, and producing a prioritized repair list with specific replacement or revision guidance.

## When to Use

- Reviewing an inherited or purchased assessment before using it
- Auditing your own assessment before a summative administration
- Curriculum alignment reviews at the department or grade-band level
- When test scores don't match classroom performance and you suspect alignment problems
- Before submitting an assessment for administrative or accreditation review

## When NOT to Use

- Building an assessment from scratch — use `assessment_test_blueprint_table_of_specs.md`
- Grading rubric alignment — use `teaching_assessment_rubric_builder.md`
- When no standards document exists (align to learning objectives instead, which this prompt can also handle)

---

## Inputs Needed

- **Assessment items:** [Paste all items as given to students, with their claimed standard tags if any]
- **Target standards:** [Paste the standards list OR describe — e.g., "CCSS Grade 5 Math NBT.1–NBT.7" / "NGSS MS-LS1" / "State ELA Grade 8 Reading Informational Text"]
- **Grade / course:** [e.g., Grade 8, AP US History]
- **Claimed alignment (if provided):** [Optional — if the assessment already has standard codes per item]
- **Assessment purpose:** [Formative / end-of-unit summative / benchmark / state-test prep]
- **Item weighting:** [Equal weight / some items worth more — specify if so]

---

## Instructions

### Step 1: Parse the Standards

Identify the target standards and organize them:

```
STANDARDS INVENTORY
─────────────────────────────────────────────
Standard [Code]: [Statement / description]
Type: [Major / Supporting / Additional — if known]
Expected assessment weight: [What proportion of items should address this, if specified]

[Repeat for each standard]
─────────────────────────────────────────────
Total standards: [N]
Major standards (if applicable): [N]
```

### Step 2: Map Each Item to Its Best-Fit Standard

For each item, determine which standard it most closely measures — regardless of what it's tagged as:

```
ITEM-TO-STANDARD MAP
─────────────────────────────────────────────
Item | Claimed Standard | Actual Best-Fit Standard | Alignment Rating | Notes
─────────────────────────────────────────────
Q1   | [Code or none]   | [Code]                   | Strong / Weak / Misaligned | [...]
Q2   | ...
...
─────────────────────────────────────────────

Alignment rating definitions:
• Strong: Item directly and specifically measures the stated standard at appropriate cognitive level
• Weak: Item is related to the standard but tests a surface feature, prerequisite, or tangential concept
• Misaligned: Item tests a different standard (specify which one it actually measures)
• Unmappable: Item can't be clearly linked to any target standard
```

### Step 3: Per-Item Alignment Analysis

For every item rated Weak, Misaligned, or Unmappable, produce a detailed finding:

```
ITEM [N] — ALIGNMENT FINDING
─────────────────────────────────────────────
Item text: "[Excerpt or description]"
Claimed standard: [Code + statement]
Finding: [Weak / Misaligned / Unmappable]

WHY THE ALIGNMENT FALLS SHORT:
[Specific reasoning — e.g., "This item tests vocabulary recall (knows the term) but the
standard requires applying the concept (uses the concept to solve a problem). That's a
Bloom's gap from Remember to Apply." OR "This item tests Standard Y, not Standard X."]

WHAT STANDARD THIS ITEM ACTUALLY MEASURES: [Code + statement, if applicable]

REPAIR OPTIONS:
Option 1: [Revise the item to better measure the claimed standard — specify what to change]
Option 2: [Re-tag the item to its actual standard and assess coverage accordingly]
Option 3: [Remove and replace — if the item can't be salvaged for this standard]
```

### Step 4: Standards Coverage Map

```
STANDARDS COVERAGE MAP
─────────────────────────────────────────────
Standard | Items that address it | Coverage rating | Notes
─────────────────────────────────────────────
[Code]   | [Item Ns] — [N items] | Strong / Adequate / Thin / Absent |
[Code]   | ...
─────────────────────────────────────────────

Coverage rating definitions:
• Strong: ≥3 items address this standard (appropriate for major standards)
• Adequate: 1–2 items address this standard (appropriate for supporting standards)
• Thin: Only 1 item, and it's rated Weak — this standard is nominally present but not well measured
• Absent: No items measure this standard
• Over-represented: More items than warranted given the standard's weight
```

### Step 5: Gap Repair Priority List

```
PRIORITY GAP REPAIRS
─────────────────────────────────────────────

CRITICAL GAPS (standards completely absent):
Standard [Code]: [Statement]
Impact: [Why this matters — what students could fail to demonstrate]
Replacement item suggestion: [Stem or description of the type of item needed]
Cognitive level needed: [Bloom's / DOK]

COVERAGE IMBALANCES (over-represented standards):
Standard [Code]: [N items — [N] more than needed]
Recommendation: [Remove [N] items / repurpose excess items to cover absent standards]

WEAK ALIGNMENT ITEMS (need revision):
Item [N]: [Brief description of needed revision]
Item [N]: [...]

UNMAPPABLE ITEMS:
Items [N, N]: [Recommendation — remove or re-anchor to a standard]

─────────────────────────────────────────────
SUMMARY:
• Items with strong alignment: [N] ([%])
• Items needing revision: [N]
• Standards fully covered: [N/N total]
• Standards absent: [N] — [list]
• Estimated revision effort: [Low / Medium / High]
```

---

## Output Format

1. Standards inventory
2. Item-to-standard map (full table)
3. Per-item alignment analysis for Weak/Misaligned/Unmappable items
4. Standards coverage map
5. Priority gap repair list with replacement item suggestions

---

## False-Positive Prevention

❌ **DON'T:**
- Rate alignment based on topic match alone — a fractions item doesn't automatically align to a fractions standard; the cognitive demand must match too
- Assume "claimed alignment = actual alignment" without checking
- Flag every Weak item as a crisis — some thin coverage is acceptable for supporting standards
- Recommend adding items without removing others, inflating test length
- Treat absence of a standard tag as automatically misaligned — some items may just be untagged

✅ **DO:**
- Check both topic and cognitive demand (Bloom's/DOK) to rate alignment
- Distinguish between "this item measures a different standard" vs. "this item measures this standard poorly"
- Prioritize gaps in major or high-stakes standards over minor supporting standards
- Provide specific, actionable repair options, not just flags
- Note when you're uncertain about alignment and recommend a subject-matter expert review

---

## Quality Indicators

- [ ] Every item rated for alignment with reasoning
- [ ] Coverage map identifies both absent and over-represented standards
- [ ] Repair list includes replacement item suggestions (not just "add an item")
- [ ] Alignment ratings distinguish between topic match and cognitive demand match
- [ ] Priority ranking helps the teacher focus on the most consequential gaps

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **DS-01** | Standards framework and Bloom's/DOK used to evaluate cognitive demand alignment. |
| **QA-01** | Systematic item-by-item verification against the stated standards. |
| **ST-01** | Structured pipeline: inventory → map → findings → coverage → repair list. |
| **QA-05** | Comparative analysis of coverage across all standards in the target set. |
| **CM-01** | Grade, purpose, and standards document frame the entire audit. |
