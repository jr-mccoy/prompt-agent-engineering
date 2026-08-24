---
title: "Weak Supervision Strategy"
category: AI-ML/data-for-ml
description: "Generate training labels programmatically from heuristics, existing signals, and domain rules — estimating labelling-function accuracy without ground truth, handling correlated sources honestly, and keeping a hand-labelled set the weak labels can never contaminate."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - QA-12
  - DS-02
difficulty: advanced
tags:
  - weak-supervision
  - labeling-functions
  - programmatic-labeling
  - label-noise
  - distant-supervision
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_active_learning_strategy.md
  - domain-AI-ML/data-for-ml/mldata_labeling_guideline_designer.md
  - domain-AI-ML/data-for-ml/mldata_annotation_quality_review.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# Weak Supervision Strategy

**Objective:** Produce training labels programmatically at a scale hand-labelling cannot reach — designing labelling functions with honest accuracy estimates, combining sources that are correlated rather than independent, and protecting a clean evaluation set the weak labels can never touch.

**When to Use:**
- Labels are needed at a volume hand-labelling cannot supply, and heuristics or existing signals carry real signal.
- Domain experts can state rules more readily than they can label thousands of examples one by one.
- Existing organizational signals — resolution codes, user actions, downstream outcomes — correlate with the target and are going unused.

**When NOT to Use:**
- Labels are already available at sufficient volume; weak supervision adds noise for nothing.
- No heuristic or proxy signal correlates with the target — the technique has nothing to build on.
- The constraint is which examples to label rather than how many — use `mldata_active_learning_strategy.md`.

## Inputs / Context

- **Target definition** — what the label means, precisely enough that a rule can be judged right or wrong about it.
- **Available signals** — heuristics, regexes, existing databases, downstream outcomes, user actions, other models.
- **Small hand-labelled set** — needed to estimate labelling-function accuracy; its size and provenance.
- **Class balance** — expected, since weak sources often fire disproportionately on one class.
- **Downstream model** — what will be trained on these labels and how tolerant it is of label noise.
- **Domain experts available** — who can propose and review rules.

## Constraints

**Must:**
- Estimate each labelling function's accuracy and coverage on a hand-labelled set, and report them per function rather than only in aggregate.
- Address **correlation between labelling functions explicitly** — sources derived from the same underlying signal are not independent votes, and treating them as such inflates confidence in exactly the cases where they are jointly wrong.
- Keep a hand-labelled evaluation set that no labelling function touches, and confirm no weak-labelled example leaks into it.
- Report the label-noise rate of the final weak labels, and state how the downstream training accounts for it.
- Check whether labelling functions systematically abstain or err on a subgroup, since weak supervision concentrates its errors rather than spreading them.

**Must Not:**
- Evaluate the downstream model on weak labels — that measures agreement with the heuristics, not correctness, and it will look excellent.
- Treat labelling functions as independent when they share a source; state the dependency and account for it.
- Assert accuracy figures for labelling functions from memory or intuition; every one is `[measure on the hand-labelled set]`.
- Use a signal that will not exist at inference time as a labelling function without checking that the resulting label is still valid — this is a leakage path disguised as supervision.
- Add labelling functions until agreement looks high; agreement among correlated rules is not accuracy.

**Instructions:**

1. **Pin the target definition.** Precisely enough that a rule can be judged correct or incorrect about a given example. Ambiguity here surfaces later as irreconcilable labelling-function disagreement that no aggregation model can resolve.

2. **Enumerate candidate sources by type.** Pattern heuristics; existing databases and knowledge bases (distant supervision); downstream outcomes and user actions; other models' outputs; and expert-stated rules. Recording the type matters because it predicts the correlation structure in step 4.

3. **Write labelling functions that abstain freely.** A function should vote only where it is confident and abstain elsewhere. High coverage with poor accuracy is worse than narrow coverage with high accuracy, because the aggregation step can work with abstention and cannot repair confident error.

4. **Map the correlation structure — the step that determines whether the aggregate is trustworthy.** Group functions by the underlying signal they derive from. Two regexes over the same field are one source wearing two hats. State which groups are genuinely independent, because independence is what makes agreement informative.

5. **Estimate accuracy and coverage per function** on the hand-labelled set. Report a table. Functions below the class prior are harmful and should be dropped or inverted rather than kept for coverage.

6. **Choose the aggregation method.** Majority vote is simple and assumes independence and equal accuracy — usually both false. A learned label model weights by estimated accuracy and can model dependencies, at the cost of complexity. Choose explicitly, and state which assumption you are accepting.

7. **Measure the resulting label noise** on the held-out hand-labelled set, overall and per class. Then decide how the downstream model handles it: noise-robust loss, confidence weighting, or filtering low-confidence weak labels out entirely.

8. **Check for a leakage path.** For any function using a downstream outcome or a signal unavailable at inference, confirm the label it produces is still the label you want, and that the feature set does not also contain that signal. This is where weak supervision most often produces a model that evaluates beautifully and fails in production.

9. **Check subgroup behaviour.** Report coverage and accuracy per subgroup. A rule set that abstains on one population produces a model trained mostly on the others.

10. **Plan the improvement loop.** Which functions to revise first — usually the highest-coverage, lowest-accuracy ones — and when to stop adding rules.

**Output Format:**

A markdown strategy:
- **Target Definition** — precise enough to adjudicate a rule.
- **Source Inventory** — table: Function | Type | Underlying signal | Coverage | Accuracy | Verdict.
- **Correlation Groups** — which functions share a signal; which groups are independent.
- **Aggregation** — method chosen, assumption accepted.
- **Resulting Label Noise** — overall and per class, measured on held-out hand labels.
- **Downstream Handling** — noise-robust loss, weighting, or filtering.
- **Leakage Check** — functions using unavailable-at-inference signals, and the verdict.
- **Subgroup Coverage** — coverage and accuracy per subgroup.
- **Improvement Loop** — revision order and stopping condition.

## Verification

- [ ] The target definition is precise enough to judge a rule right or wrong.
- [ ] Accuracy and coverage are measured per function on a hand-labelled set.
- [ ] Correlation groups are identified; independence is asserted only where justified.
- [ ] The aggregation method's assumption is stated explicitly.
- [ ] Label noise is measured on held-out hand labels, per class.
- [ ] The downstream model's handling of that noise is specified.
- [ ] Every function using an inference-time-unavailable signal is checked for leakage.
- [ ] Coverage and accuracy are reported per subgroup.
- [ ] The evaluation set is confirmed free of weak labels.
- [ ] No labelling-function accuracies are asserted from intuition.

## False-Positive Prevention

❌ **DON'T:**
- Evaluate the trained model on weak labels — you will measure how well it learned the heuristics, which is high by construction and tells you nothing about correctness.
- Treat five regexes over the same text field as five independent votes; they are one signal, and their agreement is not evidence.
- Keep a low-accuracy function because it adds coverage — below the class prior it actively degrades the aggregate.
- Use a downstream resolution outcome as a label without checking whether that outcome is caused by the thing you are predicting, or by the intervention that followed it.
- Report only aggregate label accuracy when a subgroup has almost no coverage — that subgroup's training signal is effectively random.
- Add rules until agreement rises; correlated rules agree with each other, not with the truth.

✅ **DO:**
- Define the target sharply enough that rule disagreement is informative rather than definitional.
- Let functions abstain; narrow and accurate beats broad and noisy.
- Group functions by underlying signal before trusting any agreement statistic.
- Measure accuracy per function against hand labels and drop the ones below the prior.
- Trace every outcome-derived signal for leakage before it becomes a label.
- Report subgroup coverage and treat a low-coverage group as a training-data gap.

## Example Output

```markdown
## Weak Supervision: Support-Ticket Escalation Prediction
Target: will this ticket require escalation to tier-3 within 48 hours?

### Target Definition
"Escalation" means a tier-3 assignment recorded in the ticketing system within 48 hours of
creation — **excluding** escalations triggered solely by SLA-timer expiry, which reflect queue
depth rather than ticket difficulty. Pinning this exclusion was the single most useful step
here: without it, three of the rules below would have been silently learning queue depth.

### Source Inventory
| Function | Type | Underlying signal | Coverage | Accuracy | Verdict |
|---|---|---|---|---|---|
| LF1 keyword: "urgent/outage/down" | pattern | ticket text | `[measure]` | `[measure]` | — |
| LF2 keyword: error codes 5xx | pattern | ticket text | `[measure]` | `[measure]` | — |
| LF3 customer tier = enterprise | database | CRM | `[measure]` | `[measure]` | — |
| LF4 >3 replies in first hour | behavioural | ticket events | `[measure]` | `[measure]` | — |
| LF5 product area = billing-integrations | database | CRM | `[measure]` | `[measure]` | — |
| LF6 agent set priority = P1 | **human judgment** | agent action | `[measure]` | `[measure]` | **leakage check** |

### Correlation Groups
| Group | Functions | Independent? |
|---|---|---|
| Ticket text | LF1, LF2 | **Not independent of each other** — one signal, two patterns |
| CRM attributes | LF3, LF5 | Not independent of each other |
| Ticket behaviour | LF4 | Independent of the above |
| Agent judgment | LF6 | Independent, but see leakage |

Effectively **three** independent signals, not six. Majority vote over six functions would
double-count text and double-count CRM, and would be most confident precisely where both text
rules fire together — which is the case where they are jointly wrong.

### Aggregation
**Learned label model with the correlation groups declared**, not majority vote. Assumption
accepted: within-group dependence is modelled; across-group independence is assumed. Majority
vote was rejected because its equal-weight, independent-vote assumption is false on both counts
here and would systematically over-weight text.

### Resulting Label Noise
Measured on the held-out hand-labelled set, overall and per class `[measure]`. Expect higher
noise on the positive class — escalation is the minority outcome and most functions are tuned
to fire on it.

### Downstream Handling
Confidence-weighted loss using the label model's per-example probability, plus filtering out
examples where no function fires (rather than defaulting them to the majority class, which
would teach the model the prior instead of the task).

### Leakage Check
- **LF6 (agent set P1)** — the agent's priority setting frequently *causes* the tier-3
  assignment rather than predicting difficulty. Using it as a label teaches the model to
  predict agent behaviour. **Dropped as a labelling function.** It is also excluded from the
  feature set, where its presence would have been a straightforward leak.
- **LF4 (reply count in first hour)** — available at prediction time only if prediction happens
  after that hour. Confirmed the deployment predicts at the 1-hour mark, so it is valid. Had
  prediction been at ticket creation, this would have been a leak.

### Subgroup Coverage
| Segment | Coverage | Note |
|---|---|---|
| English tickets | `[measure]` | LF1/LF2 are English-only patterns |
| **Non-English tickets** | `[measure — expected near zero]` | **gap: labels here come only from CRM and behaviour** |
| Enterprise customers | `[measure]` | LF3 fires by definition |
| SMB customers | `[measure]` | — |

Non-English tickets are the finding: two of three independent signal groups are English-only, so
that population is trained on a materially weaker label set. Either add non-English patterns or
scope the model to English and say so.

### Improvement Loop
Revise highest-coverage/lowest-accuracy first. Stop adding functions when held-out label noise
stops falling for two consecutive rounds — not when agreement among functions rises, which
correlated rules can do indefinitely without getting closer to the truth.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** target definition precedes function design, which precedes correlation analysis, which precedes aggregation.
- **RT-02 (Multi-Dimensional Analysis Framework):** function × signal type × coverage × accuracy × subgroup is the analysis grid.
- **CM-02 (Constraint Specification):** the clean-evaluation-set and declared-correlation rules bound what the aggregate may claim.
- **QA-12 (False Positives Identification):** rejects agreement among correlated rules as evidence, and catches outcome-derived leakage.
- **DS-02 (Metric Specification):** coverage, accuracy, and label noise are defined as measured quantities against hand labels.

**Related Prompts:**
- `mldata_active_learning_strategy.md` — where to spend the hand-labelling budget that this strategy still requires.
- `mldata_labeling_guideline_designer.md` — producing the hand-labelled set these estimates depend on.
- `mldata_annotation_quality_review.md` — validating that hand-labelled set before it becomes the yardstick.
- `mldata_data_leakage_detector.md` — the general leakage check behind the outcome-derived-signal trap.
