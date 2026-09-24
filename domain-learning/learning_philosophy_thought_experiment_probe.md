---
title: "Philosophy Thought Experiment Probe — What the Case Tests, Which Knob Drives the Intuition"
category: learning/humanities
description: "Interrogate a philosophical thought experiment (Chinese Room, Experience Machine, Mary's Room, Gettier cases, the violinist) as evidence: state the stipulations exactly, name the thesis it targets and the intuition it pumps, turn one knob at a time to find which feature drives that intuition and which are confounds, check that the case is coherent, and map where the intuition does and does not bear on the thesis; distinct from reasoning_counterfactual_analysis.md, which reasons causally about what would have happened in the actual world."
techniques:
  - RP-04
  - ED-03
  - RT-04
  - QA-02
difficulty: advanced
tags:
  - philosophy
  - thought-experiments
  - intuition-pumps
  - self-study
  - humanities
  - critical-thinking
updated: "2026-09-24"
reasoning:
  styles: [analytic, dialectical, counterfactual]
  stakes: low
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: not_applicable
  domain_complexity: single_domain
  collaboration: solo
  output_format: [structured, narrative]
  user_role: [individual, learner]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_counterfactual_analysis.md
  - domain-learning/learning_ethics_dilemma_multi_framework.md
  - domain-learning/learning_concept_explanation_audit.md
---

# Philosophy Thought Experiment Probe

**Objective:** Teach a self-taught reader to treat a thought experiment as an argument with moving parts rather than a story with an obvious moral. The probe finds what the case is built to test and what intuition it relies on. It then turns one feature at a time to see which one produces that intuition, and whether the intuition, once isolated, still supports the thesis.

**When to Use:**
- You met a famous case in a book or lecture (the Chinese Room, the Experience Machine, Mary's Room, the Ship of Theseus, a Gettier case, Thomson's violinist) and its conclusion felt either obvious or like a trick.
- You want to be able to reply to a thought experiment, not only restate it.
- You have invented a case of your own and want to know whether it tests what you think it does.

**Not this prompt if…**
- You want to know what *would have happened* in the real world if something had gone differently, for attribution, regret or policy. That is `domain-reasoning-craft/reasoning-moves/reasoning_counterfactual_analysis.md`, which reasons causally with the rest of the world held fixed. A thought experiment stipulates its world and tests a *concept or principle*, not an outcome.
- You want to run a moral case through the ethical theories. Use `learning_ethics_dilemma_multi_framework.md`, which applies theories to the case. This prompt interrogates the case itself.
- You want to reconstruct the argument the case is part of into numbered premises. Use `learning_philosophy_argument_standard_form.md` afterwards.

## Inputs / Context

1. **The case**, in the source's own words if possible, and where you found it.
2. **Your intuition**, recorded before probing: what you judge, and how strongly (1–5).
3. **What you take it to show**, if you have a view.
4. **Your background**, such as the book or course you are reading it in.

## Method

The probe is Socratic (RP-04, ED-03). At steps 3 and 4 ask for the learner's judgment on each variant *before* giving the analysis. Their intuitions are the data.

1. **Fix the stipulations.** List what the case stipulates, numbered. Separate these from what readers usually *assume* but the case does not say. An example: the Chinese Room stipulates rule-following, and readers assume the rulebook is feasible. Unstated assumptions often do the real work.

2. **Name the target and the pump.** State the target thesis being tested, the intuition the case is built to produce, and the bridge from intuition to verdict on the thesis ("if you judge X here, then thesis T is false because…"). If the source gives no bridge, reconstruct one and label it `[reconstructed]`.

3. **Turn the knobs, one at a time (QA-02).** Choose 3–5 features and vary each separately. Candidate knobs are scale, first vs. third person, vividness, the agent's knowledge, reversibility, a physical-contact or proximity detail, and a numerical quantity. For each variant, record the learner's intuition (1–5) and whether it moved.
   - A knob that moves the intuition but is **irrelevant to the target thesis** is a **confound**. Example: in trolley variants, physical contact may drive the intuition instead of the doing/allowing distinction.
   - A knob that moves the intuition and **is** what the thesis is about is the **driver**.
   - A knob that should matter to the thesis but does not move the intuition is a **blind spot**.

4. **Check coherence.** Is the case possible in the sense the argument needs, whether logically, nomologically or practically? Does the argument need more than conceivability? Flag any stipulation that is strained or smuggles in the conclusion.

5. **Map to real cases (RT-04).** Find one real or ordinary case with the same structure and ask whether the intuition transfers. If it does not transfer, find the structural difference, which is usually the confound from step 3.

6. **Standard replies, briefly.** Name the 2–3 best-known lines of reply to the case in the literature, and say which knob or coherence problem each one exploits. Name philosophers only when the attribution is secure. Otherwise describe the reply as a position (for example the "systems reply").

7. **Verdict on the case as evidence.** After probing, how much support does the isolated intuition give the target thesis? Choose *strong*, *weakened by confound*, *depends on a contested stipulation*, or *does not bear on the thesis*. Compare this with the learner's starting view.

## Output Format

```
# Probe — [case name]

## Stipulations (as given)
1. … 2. …
Assumed but not stipulated: …

## Target and pump
Target thesis: … | Intuition pumped: … | Bridge: … [reconstructed?]
Your starting intuition: [judgment], strength [1–5]

## Knobs
| Knob | Variant | Your intuition (1–5) | Moved? | Driver / confound / blind spot |

## Coherence
Possible in the needed sense? … | Strained stipulations: …

## Real-world mapping
Parallel case: … | Transfers? … | Structural difference: …

## Standard replies
- [reply] → exploits [knob / coherence issue]

## Verdict on the case as evidence
[strong / weakened by confound / contested stipulation / does not bear]. Your starting view vs. now: …
```

## Verification

- [ ] The learner's starting intuition was recorded before any probing.
- [ ] Stipulations are separated from reader assumptions.
- [ ] The bridge from intuition to thesis is explicit, and labelled if reconstructed.
- [ ] Every knob varies one feature only, with the learner's judgment collected first.
- [ ] Each knob is classified as driver, confound or blind spot.
- [ ] Attributions to named philosophers are secure, or the reply is described as a position.
- [ ] The final verdict is about the case's evidential force, not about whether the thesis is true.

## False-Positive Prevention

1. **Retelling as probing.** Restating the case in fresh prose is not analysis. The knob table is the minimum deliverable.
2. **Several knobs at once.** A variant that changes two features cannot identify which one moved the intuition.
3. **Model intuitions as data.** The learner's judgments are the evidence. Report the model's reading only after theirs, and label it.
4. **Dismissal by impossibility.** "That could never happen" is not a refutation unless the argument needs real possibility. Check what kind of possibility it needs.
5. **Confusing the case with the thesis.** Showing that the case is flawed does not refute its thesis. It only removes one support for it.
6. **Invented literature.** Only cite a named reply and author when the attribution is secure.
7. **Counterfactual drift.** Asking what *would* happen causally ("the man would probably survive the fall") answers a different question. The case's stipulations fix the facts.

## Example Output

```
# Probe — Nozick's Experience Machine

## Stipulations (as given)
1. The machine gives any experiences you choose, indistinguishable from real ones.
2. Once plugged in, you will not know you are plugged in.
3. You plug in for life.
Assumed but not stipulated: the machine never fails; your loved ones are cared for.

## Target and pump
Target thesis: hedonism, meaning experience is all that matters for well-being.
Intuition pumped: you would not plug in. Bridge: if only experience mattered, refusing
would be irrational; refusing seems rational; so something beyond experience matters.
Your starting intuition: would not plug in, strength 4.

## Knobs
| Knob | Variant | You | Moved? | Class |
| Status quo | You are told you are *already* plugged in; unplug? | 2 | Yes | Confound: status-quo bias |
| Duration | Two years, then out | 3 | Slightly | Confound: irreversibility |
| Others | Loved ones also plug in | 4 | No | — |
| Reality of achievement | Your achievements would be real, but you would never learn this | 4 | No | Blind spot? |

## Coherence
Nomologically far-fetched, but the argument only needs conceivability. Stipulation 2 is doing heavy work.

## Real-world mapping
Parallel: choosing a comforting belief over an unpleasant truth. Transfers? Partly; the difference is reversibility.

## Standard replies
- The status-quo-bias reply (the "reversed" machine) → exploits the first knob
- The "fear of malfunction" reply → exploits an unstipulated assumption

## Verdict on the case as evidence
Weakened by confound: status-quo bias and irreversibility carry part of the intuition.
Your view moved from "refutes hedonism" to "weighs against it, less than it first seemed".
```

## Techniques Used

- **RP-04 (Socratic Dialogue):** the learner's judgment on each variant is asked for before the analysis.
- **ED-03 (Guided Discovery):** the learner finds the driver and confounds from their own shifting intuitions.
- **RT-04 (Analogical Reasoning):** real-world mapping tests whether the intuition transfers to a structurally similar case.
- **QA-02 (Adversarial Stress-Test):** knob-turning and the coherence check attack the case's evidential force.

## Related Prompts

- `domain-reasoning-craft/reasoning-moves/reasoning_counterfactual_analysis.md`: causal "what if" reasoning about the actual world.
- `domain-learning/learning_ethics_dilemma_multi_framework.md`: run a moral case through the theories once the case is sound.
- `domain-learning/learning_concept_explanation_audit.md`: check that you can explain what the case shows in plain words.
