---
title: "Standards-Based Grading Converter"
category: education-teaching/assessment
description: "Convert a traditional points-based grading system into standards-based grading: identify priority standards, design proficiency scales, plan reassessment policy, and translate SBG marks back to a transcript grade if required."
techniques:
  - CM-01  # Context Framing
  - ST-02  # Sequential Steps
  - DS-01  # Framework Application (SBG / proficiency-scale design)
  - OC-01  # Output Templates
  - QA-01  # Verification
difficulty: advanced
tags:
  - assessment
  - standards-based-grading
  - sbg
  - proficiency-scale
  - grading
  - reassessment
  - middle-school
  - high-school
updated: "2026-05-10"
related_prompts:
  - domain-education-teaching/assessment/assessment_test_blueprint_table_of_specs.md
  - domain-education-teaching/teaching_standards_alignment_mapper.md
  - domain-education-teaching/teaching_assessment_rubric_builder.md
---

# Standards-Based Grading Converter

## Objective

Convert a traditional points-and-categories gradebook into a standards-based grading (SBG) system. Output identifies priority standards, defines a proficiency scale, builds an evidence-collection plan, sets reassessment policy, and (if required by the school) translates SBG marks back to a letter grade for the transcript.

## When to Use

- Teacher or department transitioning to SBG
- Auditing an existing SBG system that has drifted back toward points
- Designing a hybrid system where the school requires letter grades but the teacher wants standards-anchored evidence
- Preparing parent-communication materials about the change

## When NOT to Use

- Designing a single test blueprint — use `assessment_test_blueprint_table_of_specs.md`
- Mapping curriculum to standards — use `teaching_standards_alignment_mapper.md`
- Building one task's rubric — use `teaching_assessment_rubric_builder.md`

> **Scope note:** SBG implementation is shaped by district policy and labor-management agreements. This prompt produces a defensible design; verify all elements against local rules before adoption.

---

## Inputs Needed

- **Course / grade:** [...]
- **Standards or competencies:** [State, district, or course standards]
- **Current grading system:** [Categories, weights, common assessment types]
- **School/district SBG policy:** [Full SBG / hybrid required / prohibited; required reporting format]
- **Class size and grading load:** [Drives feasibility]
- **Stakeholder context:** [Are parents and students familiar with SBG?]
- **Time horizon for the change:** [Mid-year shift / next year / pilot period]

---

## Instructions

### Step 1: Audit the Current Grade

Output a one-page audit of the current grading:

| Category | Weight | What it actually measures | Evidence-validity concern |
|----------|--------|---------------------------|--------------------------|
| Homework | 20% | Often: completion + compliance | Doesn't measure learning; punishes for not yet learning |
| Tests | 50% | Often: one-shot recall | May not represent durable understanding |
| Projects | 20% | Mix: collaboration + content | Construct conflated |
| Participation | 10% | Often: compliance | Cultural and disability bias risk |

Identify what's currently being graded that isn't actually a standard.

### Step 2: Identify Priority Standards

Not every standard gets equal weight. Use a "Power Standards" lens:

| Test | Question |
|------|---------|
| Endurance | Will students need this in years to come? |
| Leverage | Does mastery support multiple disciplines? |
| Readiness | Is this prerequisite for the next course? |
| External demand | Does it appear on state assessment / college expectations? |

Reduce the standard list to a manageable number — typically 8–15 priority standards per semester per course. Other standards still get taught; they don't all get separately reported.

Output:

| Priority Standard | Why prioritized |
|-------------------|-----------------|

### Step 3: Design the Proficiency Scale

Use a 4-level scale (most common; adjust if district mandates different):

| Level | Label | Descriptor |
|-------|-------|-----------|
| 4 | Exceeds | Goes beyond the standard; applies to novel situations or extends |
| 3 | Meets | Demonstrates the standard as written; goal level |
| 2 | Approaches | Partial demonstration; specific gaps |
| 1 | Beginning | Significant gaps; needs substantial support |
| (Optional) IE | Insufficient evidence | Not enough work to determine |

Write the descriptors in student-readable language. Avoid "I can ___ with no errors" (errors aren't the right unit).

### Step 4: Build Standard-Specific Proficiency Scales

For each priority standard, write what each level looks like specifically. Generic scales don't drive instruction. Example:

**Standard:** Construct a viable argument supported by reasoning and evidence.

| Level | What it looks like |
|-------|---------------------|
| 4 | Argument addresses counter-claims and limits of the evidence |
| 3 | Claim is supported with relevant evidence and explicit reasoning |
| 2 | Claim is present; evidence or reasoning is incomplete or implicit |
| 1 | Claim is absent or unsupported |

Output one scale per priority standard.

### Step 5: Evidence Collection Plan

For each priority standard, plan:

- How students will demonstrate the standard (assessment types)
- How many opportunities across the term (≥3 typical for SBG)
- Which assessments are practice (formative) vs. evidence (summative)

| Standard | Assessment opportunities | When |
|----------|-------------------------|------|

Hard rule: practice is not graded as evidence. SBG fails when homework/practice still drives the mark.

### Step 6: Determining-the-Mark Rules

Specify how a student's mark on a standard is determined across multiple evidence pieces:

| Method | When to use |
|--------|-------------|
| Most recent | When learning is expected to grow |
| Best evidence | When students are testing readiness |
| Trend / pattern | When evidence is consistent |
| Body of evidence (decision rule) | When student needs multiple confirming pieces |

The default for most teachers is "most recent + decision rule" — recent evidence weighted, with the teacher confirming durable mastery before reporting 4 or 3.

Avoid averaging — it hides growth and can punish early struggle.

### Step 7: Reassessment Policy

Build the policy with these elements:

- **Eligibility:** Who can reassess (typically: any student, any time, with prerequisites)
- **Prerequisite:** Evidence the student has done targeted work since the prior attempt (corrections, additional practice, conferring)
- **Logistics:** When (after-school window, before/after class), how (different items at the same level)
- **Cap or limit:** None ideally; if needed, transparent
- **Time bound:** Reassessment available within X weeks of original

The reassessment policy is what makes SBG feel different to students — show they can grow.

### Step 8: Behavior Reporting Separately

Behaviors students used to be graded on (homework completion, on-time submission, participation, group skills) move to a separate reporting strand. Build:

| Behavior | How tracked | Where reported |
|----------|------------|----------------|
| Homework completion | % completed | Behavior strand, not academic grade |
| On-time submission | Tracked, not graded | Communication to parents |
| Group collaboration | Self-assessment + teacher observation | Behavior strand |

This separation is the second hallmark of SBG. Behavior matters; it just doesn't distort the academic measure.

### Step 9: Translation to Letter Grade (If Required)

If the school requires letter grades, build a defensible translation:

| Standards mark profile | Letter |
|------------------------|--------|
| Most standards at 3+, no priority standard below 2 | A or B (specify cutoffs) |
| Most standards at 3, some 2s, all priority standards ≥2 | B |
| Mix of 2 and 3 | C |
| Multiple priority standards at 1 or IE | D / F |

Avoid arithmetic (averaging the 4-point scores); use decision rules. Document the translation so it's transparent.

### Step 10: Stakeholder Communication

Output drafts for:

- A parent letter explaining the shift, common questions, and how to read the report
- A student-facing intro lesson on the proficiency scale and reassessment policy
- A peer-teacher / department conversation outline

Resistance is real; transparent communication reduces it.

### Step 11: Self-Check

- [ ] Are priority standards reduced to a manageable number?
- [ ] Does each priority standard have a specific proficiency scale?
- [ ] Is practice separated from evidence?
- [ ] Does the determining rule reward growth, not penalize it?
- [ ] Is reassessment genuinely accessible?
- [ ] Are behaviors reported separately from learning?
- [ ] Is the letter-grade translation (if needed) defensible and documented?

---

## Output Format

1. Current-system audit
2. Priority standards list with rationale
3. Generic proficiency scale
4. Standard-specific proficiency scales
5. Evidence collection plan
6. Determining-the-mark rules
7. Reassessment policy
8. Behavior reporting plan
9. Letter-grade translation (if required)
10. Stakeholder communication drafts
11. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Average the 4-point scale to a percentage — that re-creates the failure mode
- Grade practice as evidence — that punishes early struggle
- Mix behavior into the academic mark
- Use generic scales that don't differ across standards
- Skip stakeholder communication — SBG fails when families don't understand

✅ **DO:**
- Reduce to a manageable priority-standards list
- Write standard-specific scales
- Use most-recent + decision-rule, not average
- Separate behavior from learning
- Build a transparent reassessment policy
- Communicate the change explicitly

---

## Quality Indicators

- [ ] Priority standards manageable in count
- [ ] Each priority standard has a specific 4-level scale
- [ ] Practice and evidence separated
- [ ] Reassessment policy is genuinely accessible
- [ ] Behavior strand exists and is reported separately
- [ ] Letter-grade translation (if required) is documented and decision-based
- [ ] Communication drafts address common parent questions

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Course, district policy, and stakeholder context anchor every translation choice. |
| **ST-02** | Eleven-step build moves from audit → priority → scale → policy → translation. |
| **DS-01** | Power-standards and proficiency-scale frameworks structure the conversion. |
| **OC-01** | Scale templates and evidence-plan tables enforce reusable structure. |
| **QA-01** | Self-check and audit verify the system against SBG anti-patterns before rollout. |
