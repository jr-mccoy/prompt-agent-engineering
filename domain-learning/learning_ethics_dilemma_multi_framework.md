---
title: "Ethics Dilemma, Multi-Framework — Five Secular Theories Side by Side and Where They Diverge"
category: learning/humanities
description: "Run one moral dilemma through five secular ethical theories (consequentialist, deontological, virtue, care, contractualist), each stated in its strongest form with its own decision procedure and internal variants, then locate the exact feature of the case where the verdicts part company and vary it to see which theory flips; teaches how the theories work and issues no verdict, distinct from the Scripture-grounded biblical_ethics_moral_question_framework.md and from reasoning_dialectical_synthesis.md, which resolves two positions into one."
techniques:
  - DS-01
  - RP-03
  - RT-02
  - QA-02
  - QA-04
difficulty: intermediate
tags:
  - ethics
  - moral-philosophy
  - normative-theories
  - dilemmas
  - self-study
  - humanities
updated: "2026-09-24"
reasoning:
  styles: [analytic, dialectical, comparative]
  stakes: low
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: not_applicable
  domain_complexity: single_domain
  collaboration: solo
  output_format: [structured, narrative]
  user_role: [individual, learner]
  mode: [audit, synthesize]
related_prompts:
  - domain-biblical-studies/theology-research/biblical_ethics_moral_question_framework.md
  - domain-reasoning-craft/reasoning-moves/reasoning_dialectical_synthesis.md
  - domain-reasoning-craft/reasoning-moves/reasoning_steelman_construction.md
---

# Ethics Dilemma, Multi-Framework — Where the Theories Diverge

**Objective:** Show a self-taught learner how the major secular ethical theories actually *work*. One dilemma is run through each theory's own decision procedure. The output locates the feature of the case that makes the verdicts diverge, and tests that feature by varying the case. The model does not issue a verdict. Instead the learner sees which theory their own intuition was quietly using.

**When to Use:**
- You are learning moral philosophy on your own and the theories feel like labels rather than tools.
- You have a classic case (trolley, lying to the murderer at the door, the drowning child) or one of your own, and want to see each theory reason about it.
- You notice you agree with "both sides" and want to find the precise point of disagreement.

**Not this prompt if…**
- You want the question answered from Scripture and the Christian tradition. Use `domain-biblical-studies/theology-research/biblical_ethics_moral_question_framework.md`. This prompt is deliberately secular.
- You want two opposing positions combined into one. Use `domain-reasoning-craft/reasoning-moves/reasoning_dialectical_synthesis.md`. This prompt keeps the theories apart on purpose.
- You want to probe the *case* itself as a thought experiment, asking whether it is coherent or which variable drives the intuition. Use `learning_philosophy_thought_experiment_probe.md`.
- You face a live decision with real consequences. Theories inform a decision but do not make it. Use `domain-decision-making/`. If it is a professional-ethics question in a clinical role, use `domain-psychology/supervision-professional/psychology_ethics_consultation_walkthrough.md`.

## Inputs / Context

1. **The dilemma**, stated as concretely as possible: who, what options, what is known.
2. **Your gut answer**, written before the analysis, with one line of why.
3. **Theories to include.** The default is all five. You may drop some or add one, such as a natural-law or Confucian role ethic. Added theories get the same treatment.
4. **What you have read**, so the explanation starts at the right level.

## Method

1. **Fix the case.** Restate the dilemma as a list of stipulated facts and options. Any fact a theory would need that the case does not give goes on an **open facts** list. Theories may not fill it silently.

2. **State each theory at full strength (DS-01, RP-03).** For each theory, give:
   - **What counts morally**: outcomes and welfare; duties, rights and respect for persons; character and what a virtuous agent would do; relationships and responsiveness to need; principles no one could reasonably reject.
   - **Its decision procedure**, applied step by step to this case.
   - **Its verdict**, and *which version* gives it. Name the internal splits that matter here: act vs. rule consequentialism; Kant's universal-law vs. humanity formulations, or Ross-style plural duties; Aristotelian vs. agent-based virtue; care ethics' particular vs. extended obligations; Scanlonian contractualism vs. Rawlsian contractarianism. If the versions disagree, report both verdicts.
   Each theory speaks as its best defender would, never as its critics describe it.

3. **Tabulate and locate the divergence (RT-02).** Put the verdicts side by side, then name the **divergence feature**: the one aspect of the case the theories weigh differently. Examples are doing vs. allowing, using someone as a means, partiality to the near, or aggregation of numbers. Usually there is one main feature. At most there are two.

4. **Vary the case (QA-02).** Build 2–3 variants that change *only* the divergence feature. For each, report which theories flip their verdict. A theory that never flips was not really responding to that feature, so correct step 3 if so.

5. **Strongest objection to each verdict.** One line per theory, taken from a rival theory or from a counterexample. This is where the learner sees each theory's cost.

6. **Mirror the learner's intuition (QA-04).** Compare their gut answer and stated reason with the table. Which theory's reasoning does it match? Did it survive the variants, or flip in a way that points to a different theory? Say what the learner would have to accept to keep their answer. Do not tell them whether it is right.

7. **Open facts.** List what would change a verdict if known, and which theory it would change.

## Output Format

```
# Dilemma — [short name]

## The case, fixed
Stipulated: … | Options: … | Open facts: …
Your gut answer (as given): …

## Five theories
### [Theory] — version: [...]
What counts: … | Procedure applied: … | Verdict: … | Internal split: …
(repeat for each theory)

## Side by side
| Theory (version) | Verdict | Decisive consideration |

## Divergence feature
[one feature, why the theories weigh it differently]

## Variants
| Variant (changes only …) | Theories that flip |

## Strongest objection to each verdict
- [Theory]: …

## Your intuition
Matches: [theory] because … | Under the variants: … | To hold it, you must accept: …

## Open facts that would change a verdict
- [fact] → changes [theory]'s verdict because …
```

## Verification

- [ ] The learner's gut answer was recorded before the analysis.
- [ ] Each theory is stated as its defenders state it, with a named version.
- [ ] Where versions of a theory split on this case, both verdicts are shown.
- [ ] A single divergence feature is named, and the variants change only that feature.
- [ ] At least one theory flips under the variants, or step 3 was revised.
- [ ] No overall verdict is issued. The intuition mirror describes and does not grade.
- [ ] No quotation is attributed to a philosopher unless the learner supplied it.

## False-Positive Prevention

1. **Caricatured theories.** "Consequentialism means the ends justify any means" and "care ethics means be nice" are the errors to catch. Each theory is stated as its strongest defender would state it.
2. **One version standing in for the family.** Reporting "the Kantian verdict" when the formulations disagree hides the most instructive part of the case.
3. **False unanimity.** Five theories agreeing on an easy case teaches nothing. If they all agree, say so and ask the learner for a harder variant.
4. **Covert verdict.** Ordering the theories so the last one sounds like the answer, or calling one "more intuitive". Keep the ordering fixed and the tone level.
5. **Silent fact-filling.** A consequentialist verdict that assumes a probability the case never gave. Put it on the open-facts list.
6. **Invented quotations.** Put words in a philosopher's mouth only if the learner supplied the text. Paraphrase the view instead.
7. **Treating the variants as the lesson.** The variants test the divergence claim. The lesson is the divergence feature itself.

## Example Output

```
# Dilemma — Lying to the murderer at the door

## The case, fixed
Stipulated: a friend hides in your house; a man intending to kill them asks where they are.
Options: tell the truth / lie / refuse to answer. Open facts: whether refusal is safe.
Your gut answer: lie — "a life outweighs a rule."

## Five theories (one shown in full; the others follow the same shape)
### Care ethics — version: particularist (Noddings-style)
What counts: responsiveness to this friend, who depends on you | Procedure: identify who is
in your care and what they need from you now | Verdict: lie | Internal split: extended-care
views also weigh the murderer as a person, but do not reverse the verdict here.

## Side by side
| Theory (version) | Verdict | Decisive consideration |
| Act consequentialism | Lie | Expected deaths avoided |
| Kant (universal law, as in his 1797 essay) | Do not lie | Lying cannot be universalised; it wrongs humanity generally |
| Kant (humanity formula, many later Kantians) | Lie permitted | The murderer forfeits the claim to the truth |
| Virtue (Aristotelian) | Lie | A practically wise and loyal person protects the friend |
| Care | Lie | Responsibility to the particular person in your care |
| Contractualist (Scanlon) | Lie | No one could reasonably reject a principle permitting lies to would-be murderers |

## Divergence feature
Whether the wrongness of lying depends on the listener's standing. Only strict universal-law Kantianism says it does not.

## Variants
| Variant | Theories that flip |
| The murderer is a lawful officer serving an unjust law | Contractualism splits; care holds |
| Refusal is known to be safe | Consequentialism, virtue and care move to "refuse" |

## Strongest objection to each verdict
- Act consequentialism: licenses any lie with better expected results, which erodes trust.
- Kant (universal law): demands you help a murderer, which is the standard reductio.
- Kant (humanity): "forfeiting" the claim to truth needs a theory of forfeiture that Kant does not supply here.
- Virtue: "what the wise person would do" is silent until you already know the answer.
- Care: privileges the near; a stranger hiding there gets less protection.
- Contractualist: depends on who counts as able to "reasonably reject".

## Your intuition
Matches act consequentialism, but it would also permit lying to spare feelings. To hold your
reason as stated, you must accept that. If you would not, your intuition may be contractualist.

## Open facts that would change a verdict
- Refusal is safe → consequentialism, virtue and care all move from "lie" to "refuse".
```

## Techniques Used

- **DS-01 (Framework Application):** each theory's own decision procedure is applied to the fixed case.
- **RP-03 (Multi-Persona Debate):** each theory speaks through its strongest defender, not a narrator.
- **RT-02 (Multi-Dimensional Analysis):** the side-by-side table and the divergence feature.
- **QA-02 (Adversarial Stress-Test):** the variants and the strongest objection test each verdict.
- **QA-04 (Uncertainty Acknowledgment):** open facts are listed rather than filled, and no verdict is claimed.

## Related Prompts

- `domain-biblical-studies/theology-research/biblical_ethics_moral_question_framework.md`: the Scripture-grounded counterpart.
- `domain-reasoning-craft/reasoning-moves/reasoning_dialectical_synthesis.md`: when you want the positions combined, not compared.
- `domain-reasoning-craft/reasoning-moves/reasoning_steelman_construction.md`: build the strongest form of any one theory's case.
