---
title: "Bloom's Taxonomy Calibrator (Revised Taxonomy + Webb's DOK Audit)"
category: education-teaching/curriculum-design
description: "Audit a set of existing learning objectives, assessment items, or curriculum components against the Revised Bloom's Taxonomy and Webb's Depth of Knowledge, flagging miscalibration and producing a recalibrated set with rewrite recommendations."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - QA-01
  - QA-02
  - OC-03
difficulty: intermediate
tags:
  - education
  - curriculum-design
  - blooms-taxonomy
  - depth-of-knowledge
  - learning-objectives
  - audit
  - k12
  - higher-ed
  - workforce
  - medical-education
updated: "2026-05-15"
related_prompts:
  - teaching_learning_objectives_writer_blooms.md
  - teaching_standards_alignment_audit.md
  - ../program-outcomes-assessment/teaching_assessment_blueprint_builder.md
---

# Bloom's Taxonomy Calibrator (Revised Taxonomy + Webb's DOK Audit)

**Objective:** Audit a supplied set of objectives, assessment items, or curriculum components against the Revised Bloom's Taxonomy (Anderson & Krathwohl 2001) and Webb's Depth of Knowledge (DOK 1-4), identify miscalibration between stated level and actual cognitive demand, and produce a recalibrated set with concrete rewrite suggestions.

## When to Use
- ✅ Auditing a course's learning objectives before writing assessments
- ✅ Reviewing assessment items to confirm they target the cognitive level claimed
- ✅ Checking whether a curriculum overall is balanced or skewed toward low-level cognition
- ✅ Preparing accreditation evidence that demonstrates cognitive rigor
- ✅ Calibrating teacher-written test items to state-standard DOK expectations
- ❌ Writing new objectives from scratch (use `teaching_learning_objectives_writer_blooms.md`)
- ❌ Diagnosing assessment item quality unrelated to cognitive level (use rubric or test-development prompts)

## Inputs Required
- **Object of audit:** learning objectives / assessment items / activity prompts / rubric criteria — specify which
- **Item list:** the actual text of each item (paste in)
- **Stated level for each item** (if claimed): e.g., "Apply" or "DOK 2"
- **Sector and context:** K-12 grade and subject / HE course level / workforce role / medical learner level
- **Target balance** (optional): e.g., "should be 30% Remember-Understand, 50% Apply-Analyze, 20% Evaluate-Create"
- **Standards framework** (optional): for K-12, DOK targets often embedded in standards

## Constraints

**Must:**
- Use the Revised Taxonomy verbs (2001), not the original 1956 forms
- Tag each item with both Bloom's level AND Webb's DOK level — they are independent axes
- For every miscalibrated item, propose a specific rewrite (not just "raise the level")
- Distinguish between *stated* level (what the author claimed) and *actual* level (what the item really demands)
- Report distribution before and after recalibration

**Must Not:**
- Conflate Bloom's "Apply" with Webb's DOK 3 — they measure different things
- Assume verb alone determines level; the verb-object-condition combination determines cognitive demand
- Recommend wholesale rewrites without explaining the specific cognitive mismatch
- Inflate cognitive level of low-stakes items (basic vocabulary at Remember is appropriate; don't force it to Analyze)
- Score an item without considering the assessment context (what counts as "the answer")

## Instructions

1. **Receive the input list.** Number each item. Capture the stated level if provided.

2. **For each item, perform independent cognitive analysis** (do not anchor on the stated level):
   - Identify the verb(s) and object(s).
   - Ask: "What cognitive process does the learner actually have to do to produce a correct response?" — not what the author intended, but what the item demands.
   - Tag the Bloom's level using the verb-object pair.
   - Tag the Webb's DOK level using these tests:
     - **DOK 1:** Recall, rote procedure, single-step
     - **DOK 2:** Skill/concept, multi-step procedure, classify, compare on routine criteria
     - **DOK 3:** Strategic thinking, justify, support with evidence, non-routine problem
     - **DOK 4:** Extended thinking, multi-source synthesis, design/investigate over time

3. **Compare actual vs. stated level.**
   - MATCH: actual = stated
   - INFLATED: stated is higher than actual (most common error)
   - DEFLATED: stated is lower than actual (rare; usually means the author undersold the item)

4. **For each mismatched item, write a specific rewrite recommendation.**
   - Quote the original.
   - Identify the precise cognitive shortcut that makes the actual level lower (or the unintentional complexity that raises it).
   - Provide a rewritten version that hits the stated level.
   - If the stated level was wrong, suggest retagging instead of rewriting.

5. **Compute distribution.**
   - Tally actual Bloom's distribution and DOK distribution.
   - Compare to target balance if provided.
   - Identify gaps (levels with zero items) and concentrations (levels with disproportionate count).

6. **Produce a recalibration plan.**
   - Items to retag (level was misstated; item is fine)
   - Items to rewrite (level was right; item needs revision)
   - Items to add (to fill distribution gaps)
   - Items to retire (redundant or unalignable)

## Output Format

### Section 1: Item-by-Item Audit

| # | Item Text | Stated Bloom's | Actual Bloom's | Stated DOK | Actual DOK | Match | Recommendation |
|---|---|---|---|---|---|---|---|
| 1 | [quoted item] | Apply | Understand | 2 | 1 | INFLATED | Rewrite to require selection of procedure given novel context |
| 2 | … | | | | | | |

### Section 2: Cognitive Mismatch Diagnostics

For each INFLATED or DEFLATED item:

**Item #[N] — [stated level] claimed, [actual level] observed**
- **Original:** "[exact item text]"
- **Why mismatched:** [specific cognitive shortcut or unintended demand]
- **Rewrite:** "[proposed rewritten item]"
- **Resulting level:** [Bloom's + DOK]

### Section 3: Distribution Tables

**Before Recalibration (Actual):**

| Level | Bloom's Count | % | DOK Count | % |
|---|---|---|---|---|
| Remember / DOK 1 | | | | |
| Understand | | | | |
| Apply / DOK 2 | | | | |
| Analyze | | | | |
| Evaluate / DOK 3 | | | | |
| Create / DOK 4 | | | | |

**Target:** [target distribution if provided]

**After Recalibration (Projected):** [post-fix distribution]

### Section 4: Recalibration Plan

| Action | Item #s | Count | Effect on Distribution |
|---|---|---|---|
| Retag (level misstated) | [list] | | |
| Rewrite (level intended, item flawed) | [list] | | |
| Add new items (fill gap) | N/A — see suggested verbs | | |
| Retire (redundant or unfixable) | [list] | | |

### Section 5: Suggested New-Item Verbs for Gap Levels

For each level with zero or insufficient items, suggest 3-5 verb-object pairs appropriate to the topic and sector that would generate items at that level.

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Tagging verb alone without examining the object | "Analyze the diagram" is Analyze; "analyze whether 4+3=7" is Remember | Always evaluate the verb-object-condition triple |
| Treating Bloom's and DOK as the same scale | They are independent axes — an Apply-level item can be DOK 1 or DOK 3 depending on routine-ness | Tag both independently |
| Inflating low-stakes items to "look rigorous" | Foundational vocabulary at Remember level is legitimate and necessary | Preserve appropriate-level items; rigor = balance, not maxing every item |
| Anchoring on the author's stated level | Authors routinely misjudge their own items; that's why audits exist | Perform blind cognitive analysis first, compare to stated level second |
| Confusing difficulty with cognitive level | A hard recall item is still Remember-level; a moderate analysis item is still Analyze | Cognitive level = process required, not perceived difficulty |
| Recommending "raise the level" without rewriting | Authors can't act on vague advice | Provide the exact rewritten item text |
| Ignoring sector context | K-12 DOK targets, ACGME milestone language, and workforce performance standards all differ | Apply sector-appropriate verb sets and standards |
| Forcing items into Create level when topic doesn't support it | Create requires generation of novel work; not every objective needs to reach it | Accept a non-uniform distribution when topic warrants |

## Verification Checklist

- [ ] Every item has both Bloom's and DOK tags
- [ ] Mismatches are diagnosed with specific cognitive reason, not generic critique
- [ ] Every rewrite suggestion is concrete (full proposed text), not directional
- [ ] Distribution computed before and after recalibration
- [ ] Sector-appropriate verb bank used (K-12 / HE / workforce / med-ed)
- [ ] No fabricated standard codes
- [ ] Audit distinguishes retag vs. rewrite vs. add vs. retire
- [ ] Target distribution comparison shown if target was provided
