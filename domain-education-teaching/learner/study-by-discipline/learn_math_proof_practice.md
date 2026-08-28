---
title: "Math Proof Practice"
category: education-teaching/learner/study-by-discipline
description: "Generates proof-construction practice with step-level prompts: produces a claim to prove, guides through proof strategy selection, prompts each logical step without giving it away, flags common logical errors for the proof type, and provides a self-evaluation rubric for assessing proof quality."
techniques:
  - ST-01
  - ST-02
  - ED-03
  - NE-04
  - QA-01
difficulty: advanced
tags:
  - mathematics
  - proof-writing
  - logic
  - mathematical-reasoning
  - proof-strategy
  - self-evaluation
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner/study-by-discipline/learn_math_drill_sequencer.md
  - domain-education-teaching/learner/memory-and-recall/learn_feynman_teach_back_coach.md
  - domain-education-teaching/learner/self-assessment/learn_error_correction_cycle.md
---

## Objective

Guide a mathematics learner through proof construction as an active practice — not passive reading. Produce a claim to prove, elicit the proof strategy through questioning, prompt each logical step without revealing it, flag common logical errors specific to this proof type, and evaluate the completed proof against a structured rubric.

## When to Use

- When preparing for proof-based exams (real analysis, abstract algebra, discrete math, topology, number theory)
- When a learner can follow a proof when reading it but cannot produce one independently
- When proof attempts consistently fail at the same structural point (e.g., always missing the base case, never considering the contrapositive)
- When a learner wants to practice a specific proof technique (induction, contradiction, contrapositive, direct, epsilon-delta)

**Do not use** for computational mathematics where proof is not required. For problem-solving practice in computational courses, use `learnstudy_math_drill_sequencer.md`. This prompt specializes in **argumentation and logical structure**, not calculation.

## Instructions

1. **Collect inputs.**
   - Ask: "Which proof technique(s) do you want to practice? (Direct proof, induction, contradiction, contrapositive, existence, uniqueness, epsilon-delta, biconditional — or 'any')"
   - Ask: "Which course/area? (Discrete math, real analysis, abstract algebra, number theory, topology, combinatorics)"
   - Ask: "What difficulty level? (1 = familiar claim with straightforward proof, 2 = moderate with one insight required, 3 = challenging with non-obvious strategy)"

2. **Generate the claim to prove.**
   - State the claim precisely, with all quantifiers explicit (∀, ∃, ∈, ⊆, →)
   - Include a brief context statement if the claim requires background (e.g., "where n ∈ ℤ⁺ and we use the standard divisibility definition")
   - For Level 3 difficulty, include a deliberate surface misdirection — a claim that looks like it should use one strategy but is easier with another

3. **Run the proof scaffolding sequence.**
   Do NOT give the proof. Instead, guide through these steps:

   **Step 1 — Strategy identification:**
   "What proof strategy will you use? Options: direct, induction, contradiction, contrapositive, construction, cases. Explain why this strategy fits this claim."
   (Wait for learner to respond before continuing)

   **Step 2 — Setup:**
   "State your assumptions explicitly. What are you given? What are you trying to show?"
   If the strategy is induction: "State your base case and your inductive hypothesis before you begin."
   If contradiction: "What do you assume for contradiction? State it precisely."

   **Step 3 — Step-level prompting:**
   For each logical step the proof requires, ask a guiding question rather than stating the step:
   - "What do you know about [key object] from your assumptions?"
   - "You've shown X. What needs to be true next to reach your conclusion?"
   - "Is there a theorem or definition you can apply to the expression you have now?"
   Adjust prompts based on where the learner gets stuck — push further back in the chain if they're stuck early.

   **Step 4 — Conclusion check:**
   "Have you proven exactly what was claimed? Restate the claim and check each quantifier is handled."

4. **Flag common logical errors for the proof type.**
   After the learner has attempted the proof (or after revealing the model proof), show the 3–4 most common logical errors for this proof type with explicit examples.

5. **Provide a self-evaluation rubric.**
   Ask the learner to score their own proof attempt against the rubric before seeing the model proof.

6. **Reveal the model proof.**
   Present a complete, well-structured model proof with annotation:
   - Each step labeled with the rule/definition it uses
   - Key insight highlighted (the non-obvious step that makes the proof work)
   - If the claim admits multiple valid proofs, show the most elegant and note an alternative

## Output Format

```
# Proof Practice Session
Technique: [technique] | Area: [course area] | Difficulty: [1/2/3]

---

## Claim to Prove

**Claim:** [Precisely stated claim with all quantifiers]
**Context:** [Background definition if needed]

---

## Scaffolding

### Step 1 — Strategy
[Question about proof strategy]

### Step 2 — Setup
[Questions about assumptions and goal]

### Step 3 — Step-by-Step Prompts
[Guiding questions, one per logical step]

---

## Common Logical Errors: [Proof Type]

❌ Error type: [description]
   Example: [specific instance in a proof like this one]
   ✅ Correction: [what the correct step should look like]

---

## Self-Evaluation Rubric

Before reading the model proof, rate your proof attempt (1–4):

| Criterion | 1 (Missing) | 2 (Partial) | 3 (Present) | 4 (Excellent) | My score |
|---|---|---|---|---|---|
| Correct strategy | Wrong method | Correct but unjustified | Correct with rationale | + shows why other strategies wouldn't work | |
| Assumptions stated | Missing | Implicit | Explicit | Fully quantified | |
| Each step justified | Steps with no support | Some steps unjustified | Most steps have a reason | Every step cites rule/definition | |
| Conclusion matches claim | Proves something different | Close but missing a quantifier | Proves the claim | + notes edge cases | |
| Logical flow | Gaps or circular reasoning | One gap | Sound | No gaps, cleanly structured | |

Total: __/20

---

## Model Proof

[Complete annotated proof]

**Key insight:** [The non-obvious step that makes this proof work]
```

## Example Output

---

**Input:** Proof technique: Mathematical induction | Area: Discrete math | Difficulty: 2

---

# Proof Practice Session
Technique: Mathematical induction | Area: Discrete mathematics | Difficulty: 2

---

## Claim to Prove

**Claim:** For all n ∈ ℤ⁺ (positive integers), Σᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6.

**Context:** We use standard summation notation. The claim is that the sum of the squares of the first n positive integers equals the given closed form.

---

## Scaffolding

*(Do not read ahead. Answer each step before proceeding.)*

---

### Step 1 — Strategy

Mathematical induction is suggested. Before writing anything:
1. Why is induction the right strategy for this type of claim?
2. What does induction require you to prove? (Name the two parts — do not just say "base case and inductive step.")
3. Is there an alternative strategy (e.g., direct algebraic proof from the formula)? Why might induction be preferred here?

Write your answers before proceeding.

---

### Step 2 — Setup

State the following explicitly before writing a single line of proof:

- **What is n?** (Give the precise domain of the claim)
- **Inductive hypothesis P(k):** Write P(k) as a complete sentence: "Assume that for some k ∈ ℤ⁺, ..."
- **What must you prove in the inductive step?** Write P(k+1) as a complete sentence: "We want to show that ..."
- **What is your base case?** State P(1) as a complete sentence and confirm it is true by direct calculation.

---

### Step 3 — Step-by-Step Prompts for the Inductive Step

*(Follow these prompts in order — do not skip ahead.)*

**3a.** You want to show that Σᵢ₌₁^{k+1} i² = (k+1)(k+2)(2k+3)/6.
Write the left side by separating the (k+1)th term from the sum Σᵢ₌₁ᵏ i².

**3b.** You now have: Σᵢ₌₁ᵏ i² + (k+1)².
You know something about Σᵢ₌₁ᵏ i² from your inductive hypothesis. Apply it now.

**3c.** You should have: k(k+1)(2k+1)/6 + (k+1)².
Factor out the common term. What is the common factor?

**3d.** After factoring, simplify the expression inside the brackets. Can you write it as a product of two factors matching (k+2)(2k+3)? Show the algebra.

**3e.** State your conclusion explicitly: "Therefore, P(k+1) holds."

---

### Step 4 — Conclusion Check

Before writing your final conclusion:
1. Have you proven P(1) (base case)?
2. Have you proven P(k) → P(k+1) (inductive step)?
3. State the conclusion of the induction principle precisely — what does it now follow?

---

## Common Logical Errors: Mathematical Induction

❌ **Error 1: Assuming P(n) for all n in the inductive step.**
Example: Writing "Since we know the formula holds for all n, we can substitute n = k+1 directly."
This is circular — you assume what you're trying to prove.
✅ Correction: The inductive hypothesis assumes P(k) for a *specific* k, not for all n. Use P(k) only for that specific k.

❌ **Error 2: Forgetting to prove the base case.**
Example: Proving the inductive step for P(k) → P(k+1) without verifying P(1).
This is a common shortcut that invalidates the entire proof — induction without a base case proves nothing.
✅ Correction: Always prove P(1) (or P(0) or whatever the smallest case is) by direct calculation before the inductive step.

❌ **Error 3: Algebraic errors in the simplification step.**
Example: Failing to factor (k+1) correctly, leaving an expression that doesn't match the target formula.
This is often the location of failure even when the proof strategy is correct.
✅ Correction: Factor first, then expand the bracket, then compare to the target. Don't try to expand everything and hope it simplifies.

❌ **Error 4: Concluding "The formula holds" without invoking the principle of induction.**
Example: Ending with "Since P(k) → P(k+1), we are done."
The proof is incomplete without explicitly invoking the principle of mathematical induction to conclude P(n) for all n ∈ ℤ⁺.
✅ Correction: Final sentence must be: "By the principle of mathematical induction, P(n) holds for all n ∈ ℤ⁺."

---

## Self-Evaluation Rubric

Before reading the model proof, score your own attempt:

| Criterion | 1 (Missing) | 2 (Partial) | 3 (Present) | 4 (Excellent) | My score |
|---|---|---|---|---|---|
| Correct strategy (induction) | Used wrong method | Induction but wrong structure | Two-part structure correct | + explained why induction is appropriate here | /4 |
| Setup complete | Missing IH or base case | One present | Both IH and base case | Both fully quantified with P(k) and P(k+1) named | /4 |
| Inductive step — algebra | No useful progress | Factor attempted but wrong | Factored correctly | + showed the algebraic step clearly without skipping | /4 |
| Conclusion matches claim | Conclusion absent or wrong | Claimed "it works" without invoking induction | Invoked induction principle | + stated the domain (all n ∈ ℤ⁺) explicitly | /4 |
| Logical flow | Gaps or circular step | One unjustified step | All steps follow from previous | No gaps, clean proof structure | /4 |

**Total: ___/20**
- 18–20: Proof is essentially correct — focus on elegance
- 14–17: Structure is sound, but one step is weak — identify it and rework
- 10–13: Either the base case, inductive step, or conclusion has a structural error
- < 10: Return to a worked example of induction before attempting the next problem

---

## Model Proof

**Claim:** For all n ∈ ℤ⁺, Σᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6.

**Proof by mathematical induction.**

**Base case (n = 1):**
LHS: Σᵢ₌₁¹ i² = 1² = 1
RHS: 1(1+1)(2·1+1)/6 = 1·2·3/6 = 6/6 = 1
LHS = RHS. ✓ P(1) holds.

**Inductive step:**
Assume P(k) holds for some k ∈ ℤ⁺:
[Inductive hypothesis] Σᵢ₌₁ᵏ i² = k(k+1)(2k+1)/6

We want to show P(k+1): Σᵢ₌₁^{k+1} i² = (k+1)(k+2)(2k+3)/6.

**Starting from the LHS of P(k+1):**
Σᵢ₌₁^{k+1} i² = Σᵢ₌₁ᵏ i² + (k+1)²  [separate the last term]

= k(k+1)(2k+1)/6 + (k+1)²  [apply inductive hypothesis]

= (k+1)[k(2k+1)/6 + (k+1)]  [factor out (k+1)]

= (k+1)[(2k²+k)/6 + (6k+6)/6]  [common denominator]

= (k+1)(2k²+7k+6)/6  [combine numerators]

= (k+1)(k+2)(2k+3)/6  [factor the quadratic: 2k²+7k+6 = (k+2)(2k+3)]

= RHS of P(k+1). ✓

**Conclusion:** By the principle of mathematical induction, Σᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6 for all n ∈ ℤ⁺. □

---

**Key insight:** The critical step is factoring (k+1) out of both terms *before* trying to match the target expression. Learners who expand everything first create an algebraic mess that is harder to simplify. Factor first, then simplify the bracket.

**Alternative proof:** A direct proof using the telescoping identity k³ − (k−1)³ = 3k² − 3k + 1, summed from k=1 to n, also establishes this result without induction — though it requires knowing to use that identity.

---

## False-Positive Prevention

**❌ DON'T** let the learner read the model proof before attempting the scaffolding steps — the value is in the attempt, not the reading.

**✅ DO** require the learner to write down their proof strategy, setup, and at least one inductive step before revealing the model proof.

**❌ DON'T** accept "I can follow the proof" as equivalent to "I can produce a proof." Following a proof is a recognition task; producing one is a recall + generation task.

**✅ DO** distinguish these by having the learner close all notes and attempt to write the proof from the beginning after scaffolding is complete.

**❌ DON'T** use a difficulty-3 claim with a learner who has never successfully completed a proof of difficulty-1 in the same proof technique — the skill gap is too large.

**✅ DO** require one successful difficulty-1 proof before attempting difficulty-2 or 3. Proof skill is highly technique-specific — a learner who can write strong induction proofs may still fail contradiction proofs.

**❌ DON'T** score the proof only on whether the answer is "right" (true claim, valid conclusion). A structurally flawed proof of a true claim is not a valid proof.

**✅ DO** use the rubric to score structural correctness independent of whether the claim is true — a correct result via flawed reasoning is not acceptable in mathematics.

## Quality Criteria

- [ ] Claim is precisely stated with all quantifiers explicit
- [ ] Scaffolding elicits strategy and setup before any hints about steps
- [ ] Step-level prompts are questions (not answers) — never give the step directly
- [ ] Common logical errors are specific to this proof type (not generic "be careful")
- [ ] Self-evaluation rubric is completed before the model proof is revealed
- [ ] Model proof labels each step with the rule or definition it applies
- [ ] Key insight is identified (the non-obvious step, not just a restatement of the proof)

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective distinguishes proof production (active) from proof following (passive recognition) — the distinguishing skill gap
- **ST-02 (Structured Sequential Instructions):** Six-step process enforces strategy → setup → step-prompting → conclusion → errors → rubric → model proof order
- **ED-03 (Guided Discovery):** Step-level prompts are questions that lead the learner to derive each step — not hints that give it away
- **NE-04 (Good vs Bad Example Calibration):** Common logical error section pairs the wrong proof step with the correct alternative explicitly
- **QA-01 (Self-Verification):** Rubric requires self-scoring before model proof is read — separating self-assessment from answer-checking
