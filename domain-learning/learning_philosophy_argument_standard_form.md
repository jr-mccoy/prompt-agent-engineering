---
title: "Philosophy Argument in Standard Form — Numbered Premises, Then a Validity Test and a Soundness Test"
category: learning/humanities
description: "Reconstruct a philosophical argument from a passage into standard form (numbered premises, marked sub-conclusions, one conclusion), with charitably added premises flagged, then run two separate tests: validity (can the premises be true and the conclusion false? named form or counterexample) and soundness (a per-premise accept / reject / suspend verdict); strictly the standard-form move, distinct from the Toulmin map (reasoning_argument_map_toulmin.md), the premise-by-premise support audit (reasoning_premise_audit.md), and recall drilling (learn_humanities_argument_recall.md)."
techniques:
  - RT-01
  - CM-02
  - QA-11
  - QA-02
difficulty: intermediate
tags:
  - philosophy
  - logic
  - argument-reconstruction
  - validity
  - self-study
  - humanities
updated: "2026-09-24"
reasoning:
  styles: [analytic, deductive, structural]
  stakes: low
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: single_domain
  collaboration: solo
  output_format: [structured]
  user_role: [individual, learner]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_argument_map_toulmin.md
  - domain-reasoning-craft/reasoning-moves/reasoning_premise_audit.md
  - domain-education-teaching/learner/study-by-discipline/learn_humanities_argument_recall.md
---

# Philosophy Argument in Standard Form

**Objective:** Teach the one move that most philosophy reading depends on. The learner takes a passage of prose argument and writes it as numbered premises leading to a conclusion. They then ask two separate questions: *does the conclusion follow?* (validity) and *are the premises true?* (soundness). Nothing more. The output is a reconstruction the learner can test, not an essay about the argument.

**When to Use:**
- You are reading philosophy on your own (Descartes' *cogito*, Anselm's ontological argument, Hume on miracles, Singer on famine) and cannot tell whether you disagree with the *logic* or with a *premise*.
- A commentator says an argument is "invalid" or "unsound" and you want to check that for yourself.
- You want to write down an argument before objecting to it, so you object to the argument as given and not a paraphrase.

**Not this prompt if…**
- You want the argument's claim, data, warrant, backing, qualifier and rebuttal mapped. Use `domain-reasoning-craft/reasoning-moves/reasoning_argument_map_toulmin.md`. Toulmin maps practical argument and does not test deductive validity.
- You want each premise classified (factual, definitional, value, methodological), its support tested and its fragility stated. Use `domain-reasoning-craft/reasoning-moves/reasoning_premise_audit.md`. This prompt's soundness test is deliberately a one-line verdict per premise. Take any premise marked *suspend* to the premise audit.
- You want to memorise arguments for an exam through retrieval drills. Use `domain-education-teaching/learner/study-by-discipline/learn_humanities_argument_recall.md`.
- You want to probe a thought experiment the argument relies on. Use `learning_philosophy_thought_experiment_probe.md`.

## Inputs / Context

1. **The passage**, verbatim, with author, work and section.
2. **Your own attempt** at a reconstruction, even a rough one. The learner tries first.
3. **The conclusion as you understand it**, in one sentence.

## Method

Two constraints hold throughout (CM-02):
- **Charity:** where two readings are possible, reconstruct the one that makes the argument stronger, and say so.
- **Fidelity:** every premise must be traceable to the passage, or be marked `[added]`.

1. **Find the conclusion.** Quote the sentence that states it, or write it if it is implicit and mark it `[implicit]`. Check it against the learner's one-sentence version and note any difference.

2. **Extract the stated premises.** Quote each supporting claim and restate it as a single declarative proposition: one claim per premise, no rhetorical questions, and terms used in the same sense throughout.

3. **Order into standard form (RT-01).** Number premises P1, P2… and intermediate conclusions C1, C2…, each showing which lines it follows from: `C1 (from P1, P2)`. The final conclusion is last.

4. **Validity test (QA-11: pass/fail).**
   - If the argument has a recognisable valid form (modus ponens, modus tollens, hypothetical or disjunctive syllogism, a categorical syllogism), name the form. That is a **pass**.
   - Otherwise, **search for a counterexample (QA-02)**: a situation in which every premise is true and the conclusion is false. If one exists the argument is **invalid**. State the counterexample.
   - If it is invalid, add the **minimum premise** that would make it valid, mark it `[added]`, and re-run the test. An argument that needs a large or implausible added premise is informative, and saying so is the finding.
   - Each step is tested separately. Report the verdict per inference, not only for the whole argument.

5. **Soundness test (only if valid).** For each premise, including `[added]` premises, give one verdict:
   - **Accept**: you and most careful readers would grant it. One line of reason.
   - **Reject**: there is a clear counterexample or a known false case. Give it in one line.
   - **Suspend**: it is contested, and the argument's fate turns on it. Take it to `reasoning_premise_audit.md`.
   The argument is **sound** only if it is valid and every premise is *accept*. Any *reject* makes it unsound. Any *suspend* makes the result **undetermined**, with the pivotal premise named.

6. **Compare with the learner's attempt.** Did they miss a premise, merge two premises, or put the conclusion in the premises (circularity)? Name the single biggest difference.

## Output Format

```
# Standard form — [author, work, section]

Conclusion: "[quote]" (or [implicit]) | Your version: … | Difference: …

## Reconstruction
P1. …                         ("[quote]")
P2. …                         ("[quote]")
P3. … [added]                 (needed for validity; see test)
C1. … (from P1, P2)
C.  … (from C1, P3)

## Validity test
| Inference | Form / counterexample | Verdict |
| P1, P2 ⊢ C1 | [form] | Pass |
| C1, P3 ⊢ C | [form or counterexample] | Pass / Fail |
Added premises and why: …

## Soundness test
| Premise | Accept / Reject / Suspend | One-line reason |
Result: sound / unsound (P_) / undetermined, turns on P_

## Your reconstruction vs. this one
Biggest difference: …
```

## Verification

- [ ] The learner's own attempt was collected first.
- [ ] Every premise quotes the passage or is marked `[added]` or `[implicit]`.
- [ ] Each premise is a single declarative claim, with key terms used in the same sense throughout.
- [ ] Validity was tested for each inference, by a named form or a stated counterexample.
- [ ] Soundness was assessed only after validity passed, including for added premises.
- [ ] No warrant, backing, qualifier or premise-type classification appears. Those belong to the sibling prompts.
- [ ] The result names the pivotal premise when it is undetermined.

## False-Positive Prevention

1. **Invalid is not the same as false.** An invalid argument can have a true conclusion. Report the verdict on the argument, never on the conclusion.
2. **Uncharitable reconstruction.** Making an argument invalid by leaving out a premise the author obviously assumed. Add the minimal premise and mark it.
3. **Over-charitable reconstruction.** Adding a premise so strong that it assumes the conclusion. If the only premise that makes the argument valid is the conclusion restated, report *circular*.
4. **Equivocation hidden by paraphrase.** A key term ("nature", "cause", "free") that shifts meaning between premises makes an apparently valid form invalid. Hold each term fixed.
5. **Soundness by majority.** "Most philosophers accept P2" is not a reason. Give the one-line reason itself.
6. **Scope creep into sibling prompts.** Classifying premises, mapping warrants or building recall drills duplicates other prompts. Stop at the verdicts.
7. **Premise-counting as rigour.** Ten premises are not better than three. Aim for the fewest lines that keep every inference checkable.

## Example Output

```
# Standard form — Descartes, Meditations VI (argument for mind–body distinctness), reconstructed

Conclusion: "I am really distinct from my body" | Your version: "mind and body are different" |
Difference: Descartes claims *real* distinctness (they can exist apart), not just difference.

## Reconstruction
P1. Whatever I can clearly and distinctly conceive apart, God can create apart. ("…")
P2. I can clearly and distinctly conceive my mind existing apart from my body. ("…")
C1. God can create my mind apart from my body. (from P1, P2)
P3. If two things can be made to exist apart, they are really distinct. [added]
C.  My mind is really distinct from my body. (from C1, P3)

## Validity test
| Inference | Form | Verdict |
| P1, P2 ⊢ C1 | Universal instantiation + modus ponens | Pass |
| C1, P3 ⊢ C | Modus ponens | Pass |
Added: P3 states Descartes' definition of real distinction, which he uses but does not state in this passage.

## Soundness test
| Premise | Verdict | Reason |
| P1 | Suspend | Depends on theism and on conceivability implying possibility |
| P2 | Suspend | Conceiving the mind apart may reflect ignorance of how it depends on the body (Arnauld's objection) |
| P3 | Accept | It is the definition in use |
Result: undetermined, and it turns on P2. Take P2 to the premise audit.

## Your reconstruction vs. this one
You had P2 and C but not P1, so your version was invalid. The conceivability-to-possibility premise does the real work.
```

## Techniques Used

- **RT-01 (Chain-of-Thought):** premises and sub-conclusions show each inferential step and the lines it depends on.
- **CM-02 (Constraint Specification):** the charity and fidelity constraints govern every added premise.
- **QA-11 (Pass/Fail Test Harness):** validity per inference, and soundness per premise, reach explicit verdicts.
- **QA-02 (Adversarial Stress-Test):** the counterexample search attacks each inference.

## Related Prompts

- `domain-reasoning-craft/reasoning-moves/reasoning_argument_map_toulmin.md`: map practical argument structure (warrant, backing, qualifier).
- `domain-reasoning-craft/reasoning-moves/reasoning_premise_audit.md`: take a *suspend* premise here for a full support audit.
- `domain-education-teaching/learner/study-by-discipline/learn_humanities_argument_recall.md`: drill the reconstructed argument into memory.
