---
title: "Practice Test Generator"
category: education-teaching/learner/exam-prep
description: "Produces a full-format, standalone practice test: mixed question types, point values, timing guidance, answer key, and a post-test self-score rubric — suitable for printing or independent use."
techniques:
  - ST-01
  - ST-03
  - ED-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - practice-test
  - exam-simulation
  - mixed-format
  - answer-key
  - timed-practice
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner/memory-and-recall/learn_retrieval_drill_designer.md
  - domain-education-teaching/learner/self-assessment/learn_self_quiz_loop.md
  - domain-education-teaching/learner/self-assessment/learn_knowledge_tester.md
---

## Objective

Generate a complete, standalone practice exam — not an interactive quiz session — that the learner can print or use independently, simulate real exam conditions, self-score using the included answer key, and use to diagnose performance by topic area.

## When to Use

- 3–10 days before an exam, when simulating exam conditions produces the highest benefit
- When the learner needs a full-length practice run, not a topic-by-topic drill
- When the exam has a specific format (MCQ, short answer, essay, calculation) that should be replicated
- When past performance on practice tests is needed to calibrate actual readiness

**Do not use** as an interactive tutoring session — this generates a document, not a conversation. For an interactive quiz with immediate feedback, use `teaching_study_knowledge_tester.md`. For targeted topic drills, use `learnstudy_retrieval_drill_designer.md`.

## Instructions

1. **Collect exam specifications.**
   - Ask: "What subject and exam type? (class exam, licensing, certification, standardized test)"
   - Ask: "What topics are covered? (list them)"
   - Ask: "What question types does the real exam use? (MCQ, short answer, essay, calculation, case-based, matching, SATA — select all that apply)"
   - Ask: "How many questions and/or how much time does the real exam allow?"
   - Ask: "Are there any topic weighting guidelines? (e.g., 'thermodynamics is 30% of the exam')"
   - Ask: "What difficulty level should this practice test target? (same as real exam / harder / easier)"

2. **Set question count and point distribution.**
   - Match or approximate real exam proportions
   - If unknown, use this default distribution for a 50-question MCQ exam:
     - Knowledge/recall: 30% of questions
     - Application: 40% of questions
     - Analysis/synthesis: 30% of questions
   - For mixed-format exams: distribute question types in the proportions given

3. **Write questions at three cognitive levels.**

   **Level 1 (Knowledge/Recall):** Directly tests whether a fact or definition is remembered
   - "What is the term for...?" / "Which of the following correctly defines...?"

   **Level 2 (Application):** Requires applying a concept to a new scenario
   - "A patient presents with... What is the most likely diagnosis?" / "Calculate the..."

   **Level 3 (Analysis/Synthesis):** Requires reasoning across multiple concepts or evaluating claims
   - "Which of the following best explains why...?" / "A researcher finds... What conclusion is supported by this finding?"

4. **For each question, write:**
   - The question stem (with any necessary scenario setup)
   - For MCQ: 4 answer choices (one clearly correct; distractors based on common misconceptions — not obviously wrong)
   - For short answer: point value (e.g., 3 points) and components expected in the answer
   - For calculation: given values and unit requirements
   - For essay: the prompt and word limit

5. **Write an answer key section.**
   - For MCQ: correct answer letter + 1-sentence explanation of why it is correct AND why the most plausible distractor is wrong
   - For short answer: model answer with point allocation per component
   - For essay: scoring rubric with 3–5 criteria and descriptors for full/partial/no credit
   - For calculation: full worked solution with intermediate steps

6. **Add a performance analysis grid.**
   - Table mapping each question to its topic and cognitive level
   - Learner fills in: got it right / wrong / guessed
   - After scoring: totals by topic and by cognitive level → reveals pattern of where points were lost

7. **Include timing guidance.**
   - State recommended time per question type
   - Mark with ⏱ any question that commonly takes learners longer than average

## Output Format

```
# Practice Test: [Exam Name]
Time allowed: [N min] | Total points: [N] | Topics: [list]

---
## SECTION A — [Question Type] ([N questions, N points each])

1. [Question stem]
   A) ...
   B) ...
   C) ...
   D) ...

[Continue through all sections]

---
## [Separator — answer key below this line]

## ANSWER KEY

### Section A
1. [Letter]. [Explanation. Why correct answer is correct. Why best distractor is wrong.]

## Performance Analysis Grid
| Q# | Topic | Level | My Answer | Correct? |
|---|---|---|---|---|

## Score Summary
- Total: ___/[N]
- By topic: [table]
- By cognitive level: [table]
```

## Example Output

---

**Input:** General Chemistry II — Thermodynamics, Kinetics, Equilibrium — 30 questions — MCQ + 3 short answer — 75 minutes

---

# Practice Test: General Chemistry II
**Time allowed:** 75 minutes | **Total points:** 45 (30 MCQ × 1 pt + 3 short answer × 5 pts)
**Topics:** Thermodynamics, Kinetics, Equilibrium

*Instructions: Complete Section A (MCQ) before reading Section B. Do not use notes. Circle your answer for each MCQ. Show all work for short answer. Recommended time: 45 min Section A, 30 min Section B.*

---

## SECTION A — Multiple Choice (30 questions, 1 point each)

**Thermodynamics**

**1.** Which of the following reactions is predicted to be spontaneous at all temperatures?
- A) ΔH = +50 kJ, ΔS = −100 J/K
- B) ΔH = −50 kJ, ΔS = +100 J/K ← 
- C) ΔH = +50 kJ, ΔS = +100 J/K
- D) ΔH = −50 kJ, ΔS = −100 J/K

**2.** For a reaction at equilibrium at 25°C, ΔG equals:
- A) −RT ln K
- B) 0 ←
- C) ΔH − TΔS
- D) ΔG° + RT ln Q

**3.** A reaction has ΔH° = −120 kJ/mol and ΔS° = −250 J/mol·K. At what temperature (in K) does the reaction change from spontaneous to non-spontaneous?
- A) 240 K
- B) 360 K
- C) 480 K ←
- D) 600 K

**4.** ⏱ Which statement about entropy is incorrect?
- A) Entropy increases when a solid dissolves in a solvent
- B) Entropy increases when a gas is produced from a reaction between solids
- C) Entropy decreases when the temperature of a substance is raised ←
- D) Entropy increases during vaporization of a liquid

**Kinetics**

**5.** For the reaction A + 2B → C, doubling [A] while holding [B] constant doubles the reaction rate. Doubling [B] while holding [A] constant quadruples the rate. What is the overall reaction order?
- A) 1
- B) 2
- C) 3 ←
- D) 4

**6.** A first-order reaction has a rate constant k = 0.0693 min⁻¹. What is the half-life?
- A) 5 min
- B) 10 min ←
- C) 14.4 min
- D) 20 min

**7.** ⏱ A catalyst increases reaction rate by:
- A) Increasing the activation energy
- B) Providing an alternate pathway with lower activation energy ←
- C) Increasing the enthalpy of the reaction
- D) Shifting the equilibrium toward products

**8.** Which graph would be linear for a second-order reaction?
- A) ln[A] vs. time
- B) [A] vs. time
- C) 1/[A] vs. time ←
- D) [A]² vs. time

**Equilibrium**

**9.** For the reaction N₂(g) + 3H₂(g) ⇌ 2NH₃(g), if [N₂]=0.5, [H₂]=0.2, [NH₃]=0.1, and Kc=0.25 at this temperature, the reaction will:
- A) Proceed in the forward direction
- B) Proceed in the reverse direction ←
- C) Be at equilibrium
- D) Cannot be determined without temperature

**10.** Adding an inert gas at constant volume to a system at equilibrium will:
- A) Shift the equilibrium toward the side with more moles of gas
- B) Shift the equilibrium toward the side with fewer moles of gas
- C) Have no effect on the equilibrium position ←
- D) Increase Kc

*(Questions 11–30: additional MCQs covering mixed topics at increasing complexity — abbreviated in this example for length)*

---

## SECTION B — Short Answer (3 questions, 5 points each)

**Short Answer 1 (5 pts):**
For the gas-phase equilibrium: CO(g) + 3H₂(g) ⇌ CH₄(g) + H₂O(g), Kc = 3.92 at 1000 K.

(a) Write the Kc expression. [1 pt]
(b) If Q > Kc, in which direction will the reaction shift? [1 pt]
(c) If [CO] = 0.10 M, [H₂] = 0.30 M, [CH₄] = 0.20 M, [H₂O] = 0.15 M, calculate Q and state whether the system is at equilibrium, and if not, in which direction it will shift. [3 pts]

---

**Short Answer 2 (5 pts):**
A student runs a kinetics experiment on the decomposition of H₂O₂: 2H₂O₂(aq) → 2H₂O(l) + O₂(g). The following data are collected:

| [H₂O₂] (M) | Rate (M/s) |
|---|---|
| 0.100 | 1.8 × 10⁻³ |
| 0.200 | 3.6 × 10⁻³ |
| 0.400 | 7.2 × 10⁻³ |

(a) Determine the order of the reaction with respect to H₂O₂. Show your reasoning. [2 pts]
(b) Write the rate law and calculate the rate constant k with units. [2 pts]
(c) What concentration of H₂O₂ remains after 3 half-lives starting from 0.400 M? [1 pt]

---

**Short Answer 3 (5 pts):**
A reaction has ΔH° = +40 kJ/mol and ΔS° = +150 J/mol·K.

(a) Calculate ΔG° at 25°C (298 K). Is the reaction spontaneous at this temperature? [2 pts]
(b) At what temperature does the reaction become spontaneous? [1 pt]
(c) If this reaction is used in a heat pack, would it release or absorb heat? What does ΔH tell you about this practical application? [2 pts]

---

*(Do not read beyond this line until you have completed the test)*

---

## ANSWER KEY

### Section A — MCQ

**1. B** — ΔG = ΔH − TΔS. If ΔH < 0 and ΔS > 0, then ΔG is negative at all temperatures → always spontaneous. **Distractor D** (ΔH < 0, ΔS < 0) is spontaneous only at low temperatures, not all temperatures — a common mix-up.

**2. B** — At equilibrium, ΔG = 0 by definition. ΔG° ≠ 0; ΔG° = −RT ln K applies to standard conditions, not equilibrium. **Distractor A** (−RT ln K) equals ΔG°, not ΔG.

**3. C** — Crossover temperature = ΔH°/ΔS° = 120,000 J ÷ 250 J/K = 480 K. Students who forget to convert kJ → J get 480 ÷ 1000 = 0.48 K (distractor A) or another wrong value.

**4. C** — Entropy increases with temperature (more thermal motion). Decreasing entropy upon heating would violate the third law of thermodynamics.

**5. C** — Rate order in A = 1 (doubling A doubles rate), order in B = 2 (doubling B quadruples rate). Overall = 1 + 2 = 3.

**6. B** — t₁/₂ = 0.693/k = 0.693/0.0693 = 10 min. Common error: forgetting that ln(2) = 0.693 and using a different numerator.

**7. B** — Catalysts lower Ea by providing an alternate pathway; they do not shift equilibrium or change ΔH.

**8. C** — For second-order, the integrated rate law gives 1/[A] = kt + 1/[A]₀ → linear when 1/[A] is plotted vs. time.

**9. B** — Calculate Q: Q = [NH₃]² / ([N₂][H₂]³) = (0.1)² / (0.5 × (0.2)³) = 0.01 / (0.5 × 0.008) = 0.01/0.004 = 2.5. Since Q (2.5) > Kc (0.25), reaction shifts in reverse (toward reactants).

**10. C** — An inert gas at constant volume does not change the partial pressures (or molar concentrations) of the reactants or products → no effect on equilibrium.

---

### Section B — Short Answer Answer Key

**Short Answer 1:**

(a) Kc = [CH₄][H₂O] / ([CO][H₂]³) [1 pt]

(b) Q > Kc → reaction shifts in the reverse direction (toward reactants) [1 pt]

(c) Q = (0.20)(0.15) / ((0.10)(0.30)³) = 0.03 / (0.10 × 0.027) = 0.03 / 0.0027 = 11.1
Q = 11.1 > Kc = 3.92 → reaction will shift in the reverse direction [3 pts: 2 pts calculation + 1 pt direction]

**Short Answer 2:**

(a) Doubling [H₂O₂] doubles the rate → first order with respect to H₂O₂ [2 pts: 1 for ratio method, 1 for conclusion]

(b) Rate = k[H₂O₂]; k = Rate/[H₂O₂] = 1.8 × 10⁻³ / 0.100 = 1.8 × 10⁻² s⁻¹ [2 pts: 1 for rate law, 1 for k with units]

(c) After 3 half-lives: 0.400 × (1/2)³ = 0.400/8 = 0.050 M [1 pt]

**Short Answer 3:**

(a) ΔG° = ΔH° − TΔS° = 40,000 − 298(150) = 40,000 − 44,700 = −4,700 J/mol = −4.7 kJ/mol. Spontaneous at 25°C (ΔG° < 0) [2 pts]

(b) ΔG° = 0 when T = ΔH°/ΔS° = 40,000/150 = 267 K. Spontaneous above 267 K [1 pt]

(c) ΔH° = +40 kJ/mol means the reaction absorbs heat → endothermic. A heat pack requires heat release (exothermic), so this reaction is unsuitable for a conventional heat pack; it would be used in a cold pack instead. [2 pts: 1 for absorbs/endothermic, 1 for correct practical inference]

---

## Performance Analysis Grid

Fill in after scoring:

| Q# | Topic | Cognitive Level | My Answer | Correct? |
|---|---|---|---|---|
| 1 | Thermodynamics | Application | | |
| 2 | Thermodynamics | Knowledge | | |
| 3 | Thermodynamics | Application | | |
| 4 | Thermodynamics | Knowledge | | |
| 5 | Kinetics | Application | | |
| 6 | Kinetics | Application | | |
| 7 | Kinetics | Knowledge | | |
| 8 | Kinetics | Analysis | | |
| 9 | Equilibrium | Application | | |
| 10 | Equilibrium | Analysis | | |
| SA1 | Equilibrium | Application | | |
| SA2 | Kinetics | Application/Analysis | | |
| SA3 | Thermodynamics | Application | | |

## Score Summary (fill in)

- **Total MCQ:** ___/10 (shown) | Full test: ___/30
- **Short Answer:** ___/15
- **Grand Total:** ___/45

**By topic:**
- Thermodynamics: ___/[N]
- Kinetics: ___/[N]
- Equilibrium: ___/[N]

**By cognitive level:**
- Knowledge: ___/[N] → low score = content gaps
- Application: ___/[N] → low score = can't apply what you know
- Analysis: ___/[N] → low score = need deeper practice with reasoning

---

## False-Positive Prevention

**❌ DON'T** write MCQ distractors that are obviously absurd — distractors should reflect common, plausible misconceptions, not random wrong answers.

**✅ DO** base each distractor on a documented misconception or common calculation error for that topic.

**❌ DON'T** present this as a learning tool to be done with notes open — it simulates exam conditions.

**✅ DO** explicitly instruct the learner to complete the test under exam conditions before accessing the answer key.

**❌ DON'T** write all questions at the same cognitive level — a practice test that tests only recall will not prepare learners for application and analysis questions.

**✅ DO** distribute questions across three cognitive levels (approximately 30/40/30 knowledge/application/analysis).

**❌ DON'T** omit the performance analysis grid — scoring alone ("I got 23/30") does not identify which topics or question types to fix.

**✅ DO** include the grid so the learner can identify patterns, not just totals.

## Quality Criteria

- [ ] Question types match the real exam format
- [ ] Questions distributed across three cognitive levels (approximately 30/40/30)
- [ ] MCQ distractors are based on common misconceptions (not randomly wrong)
- [ ] Answer key explains why correct answer is correct AND why best distractor is wrong
- [ ] Short answer rubrics specify point allocation per component
- [ ] Performance analysis grid links each question to topic and cognitive level
- [ ] Test and answer key are separated with clear instruction to complete before reading key

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective distinguishes this from interactive tutoring — it generates a standalone exam artifact
- **ST-03 (Output Format Specification):** Complete test + answer key + analysis grid format matches a real exam document
- **ED-02 (Progressive Exercise Generation):** Questions scale from knowledge to application to analysis
- **RT-05 (Evidence-Based Reasoning):** Answer key explanations ground corrections in the underlying concept, not just "the answer is B"
- **QA-01 (Self-Verification):** Performance analysis grid enables the learner to verify topic and level coverage before treating the test as representative
