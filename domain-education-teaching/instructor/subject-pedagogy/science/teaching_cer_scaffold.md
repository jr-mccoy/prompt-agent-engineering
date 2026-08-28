---
title: "Science Claim-Evidence-Reasoning Scaffold"
category: education-teaching/subject-pedagogy
description: "Build CER scaffolds at three tiers (heavy, medium, light) for a specific science task — pushing students from sentence frames to independent argument from evidence over the year."
techniques:
  - CM-01  # Context Framing
  - ST-02  # Sequential Steps
  - DS-01  # Framework Application (CER as scientific argument)
  - OC-01  # Output Templates
  - QA-02  # Adversarial Verification
difficulty: intermediate
tags:
  - science
  - cer
  - claim-evidence-reasoning
  - argumentation
  - scaffolding
  - middle-school
  - high-school
  - writing-in-science
updated: "2026-05-10"
related_prompts:
  - domain-education-teaching/subject-pedagogy/teachsubj_science_lab_activity_designer.md
  - domain-education-teaching/learner-math-science/learnsci_lab_report_scaffold.md
  - domain-education-teaching/grading-feedback/grading_lab_report_feedback.md
---

# Science CER Scaffold (Three-Tier)

## Objective

Produce three tiered CER (Claim, Evidence, Reasoning) scaffolds — heavy, medium, and light — for a specific science task. Output includes the prompt students respond to, the per-tier scaffold, an exemplar response at each tier's expected ceiling, and a teacher-facing rubric. Designed to enable a year-long arc from heavy support to independent argument.

## When to Use

- Mid-year transitions where you want to reduce scaffolding
- Differentiating CER work within one class
- Aligning CER expectations across a grade-level team
- After a lab or after analysis of secondary data

## When NOT to Use

- Designing the lab itself — use `teachsubj_science_lab_activity_designer.md`
- Single student feedback on a CER — use `grading_lab_report_feedback.md`
- Student-facing self-coaching — use `learnsci_lab_report_scaffold.md`

---

## Inputs Needed

- **Grade level:** [6–12]
- **Task type:** [Lab data analysis / data table interpretation / claim about a phenomenon / counter-argument]
- **Disciplinary core idea:** [Standard or topic]
- **Investigation question or claim space:** [What students are arguing about]
- **Data students will use:** [Brief description — table, graph, observations]
- **Where students are in the year:** [Beginning / mid / end — informs which tier should be the "default"]

---

## Instructions

### Step 1: Articulate the Claim Space

Specify:
- The investigation question or prompt
- What a defensible claim looks like (multiple defensible claims may exist; name them)
- What an indefensible claim looks like (claim not supported by the data)

Without this, the scaffold will accept any claim, which trains students to write CER as fill-in-the-blank.

### Step 2: Specify the Evidence That Counts

Identify the specific data students must cite:

- Which numbers from the data table are relevant
- Which observations are relevant
- Which patterns (trend, comparison, threshold) the evidence should show
- What does NOT count as evidence (opinion, prior knowledge stated as data, claims about why)

### Step 3: Name the Reasoning Principle

State the scientific principle students must invoke. This is the step CER most often skips.

Example: "Because metals conduct heat through delocalized electrons, the metal handle reached higher temperatures faster than the wooden handle."

If students could give "good" reasoning without naming the principle, the prompt is weak.

### Step 4: Build the Heavy-Scaffold Tier

This tier is for early-year, ELL beginning levels, or students new to CER. Provide:

```
PROMPT: [Question]

Step 1 — Claim
A claim is one sentence that answers the question. Use this frame:
"Based on the data, ___ (DV) [increased / decreased / stayed the same] when ___ (IV) [increased / decreased]."
Your claim: ___

Step 2 — Evidence
Evidence is the specific data. Use this frame:
"Our data show that when [IV value], the [DV] was ___. When [different IV value], the [DV] was ___. This means [pattern]."
Your evidence: ___

Step 3 — Reasoning
Reasoning explains why using the science. Use this frame:
"This happens because [scientific principle name]. [Sentence connecting principle to the data pattern]."
Vocabulary you can use: [list 4–6 key terms]
Your reasoning: ___
```

### Step 5: Build the Medium-Scaffold Tier

For mid-year students. Reduce frames; keep prompts:

```
PROMPT: [Question]

CLAIM (1–2 sentences): What does your data show? Answer the question directly.
[Word bank if helpful: 2–4 terms]

EVIDENCE: Quote specific numbers from your data table. Show the trend or comparison.
[Reminder: include at least two specific data points]

REASONING: Why does the evidence support the claim? Name the scientific principle and explain the connection.
[Reminder: name the principle. "Because" alone is not reasoning.]
```

### Step 6: Build the Light-Scaffold Tier

For end-of-year independence. Minimal scaffolding:

```
PROMPT: [Question]

Construct a CER response. Defend a claim with evidence from the data and reasoning that names and applies the relevant scientific principle.

[Optional reminder line about counter-evidence: "If alternate explanations exist, address them."]
```

At this tier, students are expected to handle structure independently.

### Step 7: Write Exemplar Responses

Produce a "meets" exemplar for each tier:

| Tier | Claim | Evidence | Reasoning |
|------|-------|----------|-----------|
| Heavy | [Frame-completed example] | [...] | [...] |
| Medium | [...] | [...] | [...] |
| Light | [Independent paragraph] | | |

Exemplars should be authentic-sounding for the grade level, not idealized.

### Step 8: Teacher Rubric

Provide a single rubric usable across tiers, scoring each component 0–3:

| Component | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| Claim | Missing or off-topic | Partial; doesn't fully answer | Answers the question; correct direction | Precise, defensible, addresses scope |
| Evidence | None or irrelevant | Generic reference to data | Specific data with units | Specific data + pattern explicitly named |
| Reasoning | Missing or "because the data show" | Mentions science but disconnected | Names principle; connects to evidence | Names principle; connects clearly; addresses limits or counter-evidence |

### Step 9: Counter-Evidence and Argument Extension (Light tier and beyond)

For students past the heavy/medium tiers, add an optional fourth component:

```
COUNTER-EVIDENCE / REBUTTAL:
"A reasonable alternate explanation might be ___. However, [data point or principle] makes that less likely because ___."
```

This extends CER toward full scientific argument.

### Step 10: Self-Check

- [ ] Are the three tiers genuinely different in support, not just labeled?
- [ ] Do exemplars match the ceiling of each tier?
- [ ] Does the rubric apply across tiers without ambiguity?
- [ ] Is the reasoning principle named so students can't slip past it?
- [ ] Does the heavy scaffold over-support without doing the thinking for the student?

---

## Output Format

1. Claim space (defensible vs. indefensible)
2. Evidence specification
3. Reasoning principle
4. Heavy-scaffold tier with frames
5. Medium-scaffold tier
6. Light-scaffold tier
7. Exemplar responses per tier
8. Cross-tier rubric
9. (Optional) Counter-evidence extension
10. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Make all three tiers structurally identical with cosmetic differences
- Let "evidence" mean "I noticed something" — require specific data
- Accept "because" as reasoning — require named principle
- Train students to fill blanks without thinking — heavy scaffold should still demand decisions
- Score across tiers with different rubrics — students should see the same expectations

✅ **DO:**
- Differentiate tiers by genuine reduction of structural support
- Require named scientific principles in reasoning
- Anchor exemplars to grade-appropriate language
- Use one rubric for all tiers
- Add counter-evidence as the next move past light

---

## Quality Indicators

- [ ] Three tiers are genuinely differentiated
- [ ] Reasoning principle is named and required
- [ ] Exemplars represent realistic ceiling per tier
- [ ] Rubric is consistent across tiers
- [ ] Counter-evidence extension is provided for advanced students
- [ ] Heavy scaffold does not substitute for thinking

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Grade, task type, and year-position anchor tier defaults. |
| **ST-02** | Ten-step build moves from claim space → tiers → exemplars → rubric. |
| **DS-01** | CER framework structures the scaffold; counter-evidence extends to full argument. |
| **OC-01** | Three-tier templates and cross-tier rubric enforce reusable, fading structure. |
| **QA-02** | Self-check stress-tests for cosmetic-only tiering and unnamed reasoning. |
