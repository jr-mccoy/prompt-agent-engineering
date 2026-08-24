---
title: "Lab Report Feedback (CER-Anchored)"
category: education-teaching/grading-feedback
description: "Generate feedback on a student lab report keyed to CER components — claim, evidence, reasoning — plus procedure, data quality, and limitations, naming a single highest-leverage revision rather than rewriting the report."
techniques:
  - CM-01  # Context Framing
  - ST-02  # Sequential Steps
  - DS-01  # Framework Application (CER as scientific argument)
  - OC-01  # Output Templates
  - QA-02  # Adversarial Verification
difficulty: intermediate
tags:
  - grading
  - feedback
  - lab-report
  - science
  - cer
  - middle-school
  - high-school
  - revision
updated: "2026-05-10"
related_prompts:
  - domain-education-teaching/subject-pedagogy/teachsubj_science_cer_scaffold.md
  - domain-education-teaching/grading-feedback/grading_essay_feedback_by_rubric_criterion.md
  - domain-education-teaching/learner-math-science/learnsci_lab_report_scaffold.md
---

# Lab Report Feedback (CER-Anchored)

## Objective

Produce feedback on a single student lab report that addresses the CER components (claim, evidence, reasoning) plus the procedural, data-quality, and limitations components — without rewriting the student's report. Output names what's working, locates the highest-leverage revision, and gives the student a specific next move.

## When to Use

- Returning lab reports that will be revised
- Conferring prep before a one-on-one
- Calibrating feedback across a class
- Building toward stronger CER over the year

## When NOT to Use

- Whole-class trends across many reports — produce a class memo separately
- Designing the lab itself — use `teachsubj_science_cer_scaffold.md`
- Coaching a student through writing a report from scratch — use `learnsci_lab_report_scaffold.md`

---

## Inputs Needed

- **Student lab report (full text):** [...]
- **The lab assignment / investigation question:** [...]
- **Data the student collected:** [If reported in the lab; otherwise note]
- **Rubric used:** [If any]
- **Grade / course:** [...]
- **Stage:** [Draft / final / revision check]
- **Tier of CER scaffolding the student worked from:** [Heavy / medium / light]
- **Feedback length cap:** [...]

---

## Instructions

### Step 1: Read the Whole Report for Coherence

Before commenting on parts, summarize internally:

- What was the investigation question?
- What did the student claim?
- Does the report tell a coherent story from question → procedure → data → claim?

If the report is incoherent at the whole-document level, that's the first feedback point — not the per-component issues.

### Step 2: Score the Components

Score each component:

| Component | Score | Quoted evidence from the report |
|-----------|-------|--------------------------------|
| Investigation question framing | | |
| Procedure (replicable, controlled) | | |
| Data quality (precision, units, organization) | | |
| Claim (answers the question, defensible) | | |
| Evidence (specific data cited, pattern named) | | |
| Reasoning (named principle, connection to data) | | |
| Limitations / sources of error | | |

For each component, identify a quote from the student's report that justifies the score. No score without quoted evidence.

### Step 3: Identify the Highest-Leverage Revision

Across the components, name **one** revision that would most strengthen the report. Common high-leverage moves:

- "The claim is missing a direction or magnitude — strengthen it"
- "Evidence is described but not quoted from your data table — pull specific numbers"
- "Reasoning names the principle but doesn't connect it to your specific data"
- "Limitations are absent — every lab report needs them"
- "Procedure is so vague another student couldn't replicate it — add measurable detail"

### Step 4: Write the Feedback

Use this structured template:

```
ONE-SENTENCE READ: What your report argues, in my words: [paraphrase]

CER QUICK SCAN
- CLAIM: [Quote student's claim]
  Working: [What's there]
  Not yet: [What rubric expects at one level higher]

- EVIDENCE: [Quote student's evidence]
  Working: [What's there]
  Not yet: [What rubric expects at one level higher]

- REASONING: [Quote student's reasoning]
  Working: [What's there]
  Not yet: [What rubric expects at one level higher]

PROCEDURE / DATA / LIMITATIONS
[1–2 sentences about each, only if there's a meaningful note]

YOUR NEXT MOVE (one revision):
[Verb + object move that targets the highest-leverage revision]
[Where in the report to start: page or section + brief rationale]
```

Hard rules:
- Quote the student's text for every component comment
- Don't write rewritten claim, evidence, or reasoning prose
- Don't pile on every issue — name the one
- Connect the revision to the rubric language, not personal judgment

### Step 5: Pattern-Matched Next Moves

Match the next move to the diagnosis:

| Diagnosis | Next move |
|-----------|-----------|
| Claim is descriptive, not directional | "Sharpen your claim by adding direction or magnitude. What does the data say happened?" |
| Evidence is paraphrase, not specific data | "Quote two specific data points from your table. Show the trend with numbers." |
| Reasoning is "because the data show" | "Name the scientific principle. Why, mechanistically, does [IV] cause [DV]?" |
| Procedure is vague | "Re-read step ___. Could a classmate replicate it without asking you a question?" |
| Limitations missing | "Add a section: 'What sources of error could affect our claim?' List ≥2." |
| Data table unclear or missing units | "Add units to all columns. Re-organize so the trend is visible." |

### Step 6: Counter-Evidence Push (Advanced)

For students past basic CER, prompt:

- "Is there an alternate explanation for your data? How would you address it?"
- "If this lab were extended, what's the next investigation?"

This pushes the report toward fuller scientific argument.

### Step 7: Self-Check Before Output

- [ ] Did I quote the student's text for each CER component?
- [ ] Did I identify a single highest-leverage revision?
- [ ] Did I avoid rewriting any component?
- [ ] Is the next move a verb-object action the student can do?
- [ ] Did I avoid generic "good job" or "needs work"?

---

## Output Format

1. One-sentence read of what the report argues
2. CER quick scan with quoted evidence per component
3. Procedure / data / limitations notes
4. Highest-leverage revision identified
5. Pattern-matched next move
6. (Optional) Counter-evidence prompt
7. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Rewrite claim, evidence, or reasoning sentences for the student
- Pile on every issue across the report
- Praise generically without naming what worked
- Skip limitations as a feedback target — that's a frequent gap
- Treat reasoning as "the student wrote because" — push for named principle

✅ **DO:**
- Quote student text for every component
- Name one highest-leverage revision
- Match the next move to diagnosis
- Push toward counter-evidence for advanced students
- Connect feedback to rubric language, not subjective response

---

## Quality Indicators

- [ ] All CER components addressed with quoted evidence
- [ ] Highest-leverage revision named and justified
- [ ] No teacher-rewritten prose
- [ ] Next move is verb-first and student-executable
- [ ] Limitations and procedure addressed when relevant
- [ ] Counter-evidence offered for advanced students

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Lab, rubric, and CER tier anchor feedback depth and language. |
| **ST-02** | Seven-step sequence: read → score → choose → write → match → push → check. |
| **DS-01** | CER framework structures the feedback into named components. |
| **OC-01** | Component-by-component template enforces reusable structure. |
| **QA-02** | Self-check stress-tests for rewriting, generic comments, and missing limitations. |
