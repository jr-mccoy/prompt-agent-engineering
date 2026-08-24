---
title: "Research Question Formulation — Convert a Fuzzy Interest into Answerable Questions"
category: research-academic/question-design
description: "Turn a fuzzy interest or topic into 3–5 well-scoped research questions that are specific enough to answer, ambitious enough to matter, and constrained enough to be feasible. Distinguishes the topic from the question, surfaces the implicit unit of analysis, and produces sub-questions that decompose the parent."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - research
  - question-design
  - scoping
  - literature-review
  - methodology
updated: "2026-05-10"
reasoning:
  styles: [analytic, decomposition, iterative]
  stakes: variable
  horizon: weeks_to_years
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: question_set_with_sub_questions
  user_role: [researcher, student, analyst, writer, founder, policy]
  mode: [audit, synthesize]
related_prompts:
  - domain-research-academic/research_literature_review_plan.md
  - domain-research-academic/research_hypothesis_generator.md
  - domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md
---

# Research Question Formulation

**Objective:** Convert a fuzzy interest, topic, or domain into 3–5 well-scoped research questions. Each question must be specific enough to answer, ambitious enough to matter, and constrained enough to be feasible within available resources. Surface the implicit unit of analysis (people? organizations? events? texts? policies?), the comparison being made (across time, across groups, against a counterfactual), and decompose each question into sub-questions whose answers would compose into the parent.

**When to use:**
- A researcher, student, analyst, or writer has a topic but not a question.
- A team is starting a research project and the framing is loose.
- A literature review is sprawling because the question is too broad.
- Project planning where the deliverable depends on a sharply-stated research question.
- Policy or strategy work that needs to be grounded in an answerable inquiry rather than a vague concern.

**When NOT to use:**
- The user already has a sharp question and just needs methodology. Skip to a methods prompt.
- The question is genuinely a meta-question ("what should we research?") — that's a different exercise (research agenda design).
- The user wants permission to research what they were going to research anyway. The exercise has no value if scope-tightening will be ignored.

**Audience:** Researchers, graduate students, policy analysts, journalists, founders pre-product-market-fit, anyone whose work product depends on a sharply-stated question.

---

## Inputs / Context

1. **The fuzzy interest.** A sentence or paragraph the user can write today. May be a topic, a problem, an itch, a discomfort with current consensus.
2. **Why this, why now.** The trigger. Important because the trigger often hides the actual question.
3. **Available resources.** Time, access (datasets, interview subjects, archives, expertise), money, collaborators.
4. **Deliverable.** What does the research produce? (Paper, memo, decision, product, policy recommendation, dissertation chapter.) The deliverable shapes the acceptable question.
5. **Audience for the deliverable.** Who reads / acts on it.
6. **Existing literature awareness.** What the user already knows about the field. Affects whether a question is "novel" or already-answered.

---

## Constraints

### Must
- Distinguish the **topic** (a subject area) from the **question** (a specific inquiry within the topic). Topics are not researchable; questions are.
- Each candidate question must specify: **what is being asked** (descriptive / explanatory / predictive / normative / design), **about what** (the unit of analysis), **compared to what** (cross-sectional, longitudinal, counterfactual, against a benchmark), and **bounded how** (population, time period, geography, scope).
- Generate 3–5 candidate questions, not one. Single-candidate framing locks in early commitments.
- For each candidate, decompose into 2–4 sub-questions whose answers compose into the parent.
- Tag each candidate question by type: descriptive (what is the case), explanatory (why is it the case), predictive (what will happen), evaluative (how good is it), design (how should we build / do X), normative (what should be done).
- Assess feasibility for each candidate against available resources. A great question with no feasible method is a research-impossible question.
- End with a recommendation: which question to pursue, why, and what the user gives up by not pursuing the others.

### Must Not
- Restate the topic as a question without sharpening ("topic: AI in education" → "question: how does AI affect education?" — still a topic).
- Smuggle the user's preferred conclusion into the question phrasing.
- Generate "questions" that are actually multi-question compounds ("How does X affect Y, and what should we do about it?" is two questions).
- Skip the unit of analysis. Without a unit, the question is not yet an empirical inquiry.
- Output a question that no methodology could plausibly answer within the user's resources.

---

## Instructions

### Step 1 — Capture the fuzzy interest verbatim
Write the user's interest in their own words. Don't sharpen yet.

### Step 2 — Distinguish topic from question
Name the topic explicitly. List 3–5 *different* questions that all live within that topic. The point is to show the user that a topic contains many distinct questions, and they need to choose.

### Step 3 — Surface the implicit unit of analysis
For each candidate question, ask: what would I be measuring or describing? Individuals, organizations, events, texts, transactions, policies, time periods? If the user resists naming a unit, the question isn't yet an empirical inquiry.

### Step 4 — Specify the comparison
What's being compared to what? Common structures:
- **Cross-sectional:** group A vs group B at a single time
- **Longitudinal:** the same population over time
- **Counterfactual:** observed world vs hypothetical alternative
- **Against benchmark:** observed value vs an expected / standard value
- **Mechanism:** what's the chain from cause to effect

A question without a comparison is usually a description, which is fine — but mark it as such.

### Step 5 — Bound the scope
For each candidate: population, time period, geography, scope of phenomenon. The bounding is what makes the question feasible.

### Step 6 — Tag question type
Each candidate gets one of: descriptive, explanatory, predictive, evaluative, design, normative. The type determines what methodology is appropriate.

### Step 7 — Decompose into sub-questions
For each candidate, write 2–4 sub-questions whose answers would compose into the parent. The sub-questions should be more answerable than the parent. (Same logic as `forecasting_super_forecaster_decomposition.md`, applied to research.)

### Step 8 — Feasibility check
For each candidate:
- Methodology that could plausibly answer it: [survey / interview / experiment / archival / literature synthesis / observation / computational / mixed]
- Resources required: [time, access, expertise, cost]
- Feasibility: [feasible / stretch / infeasible given resources]

### Step 9 — Audit each candidate against original interest
For each candidate, does it actually address what the user cared about? Sometimes sharpening drifts away from the original concern. If the candidate is a sharper question but a different question, name the drift.

### Step 10 — Recommendation
- Recommended question (with sub-questions)
- Why this one over the others
- What the user gives up by not pursuing the others (and whether those are recoverable later)
- The first concrete action the recommended question implies

---

## False-Positive Prevention

1. **Topic-as-question.** Restating the topic in question form ("How does climate change affect cities?") without specifying unit, comparison, or scope. The result reads researchable but isn't.
2. **Concealed multi-question.** Compound questions hide multiple research projects. Split them.
3. **Conclusion-loaded phrasing.** "How does X cause Y?" presupposes X causes Y. "What is the relationship between X and Y, if any?" is the honest version.
4. **Methodology-impossibility.** A question that no available methodology could plausibly answer is a poetry exercise, not research. Flag.
5. **Drift from interest.** Sharpening can drift the question away from what the user actually cared about. The original interest must remain visible.
6. **Novelty inflation.** Marking a question novel without checking the literature. The user may not yet have the literature awareness to know if the question has been answered. Flag with `[novelty unverified]`.
7. **Single-candidate lock-in.** Producing one question at a time prevents comparison. Always 3–5 candidates.
8. **Premature methodological binding.** Picking the question because the methodology is convenient. The question should drive the methodology, not vice versa — or, if the methodology must drive the question, surface that explicitly.

---

## Output Format

```
# Research question formulation — [user's topic]

## Original interest (verbatim)
> [User's words]

## Topic
[Named subject area]

## Trigger
[Why now]

## Resources
- Time: [...]
- Access: [...]
- Expertise: [...]
- Deliverable: [...]
- Audience: [...]

## Candidate questions

### Candidate 1
- **Question:** [sharply-stated]
- **Type:** [descriptive / explanatory / predictive / evaluative / design / normative]
- **Unit of analysis:** [...]
- **Comparison:** [structure]
- **Scope:** [population, time, geography]
- **Sub-questions:**
  1. [...]
  2. [...]
  3. [...]
- **Methodology candidates:** [...]
- **Feasibility:** [feasible / stretch / infeasible — why]
- **Drift from original interest:** [none / minor / major — describe]
- **Novelty:** [novel / partially answered / well-answered / `[unverified]`]

### Candidate 2
[Same structure]

### Candidate 3
[Same structure]

[etc., 3–5 total]

## Recommendation
- **Recommended:** Candidate [N]
- **Why:** [tradeoff against the others]
- **What's given up by not pursuing the others:** [recoverable later? yes / no]
- **First concrete action:** [...]
```

---

## Verification

- [ ] Topic and question are distinguished.
- [ ] 3–5 candidate questions generated.
- [ ] Each candidate has unit of analysis, comparison, scope, and type.
- [ ] Each candidate is decomposed into 2–4 sub-questions.
- [ ] Methodology + resource + feasibility assessed for each.
- [ ] Drift from original interest checked for each.
- [ ] Recommendation justifies the chosen question against alternatives.
- [ ] No topic-as-question framing in candidates.
- [ ] No compound questions.
- [ ] No conclusion-loaded phrasings.
