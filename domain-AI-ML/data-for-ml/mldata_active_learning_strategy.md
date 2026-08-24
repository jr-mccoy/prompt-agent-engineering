---
title: "Active Learning Strategy"
category: AI-ML/data-for-ml
description: "Design an active learning loop that spends labelling budget where it changes the model — checking first that labelling is the binding constraint, choosing an acquisition strategy against the failure it must fix, and guarding the biased-pool problem the loop creates."
techniques:
  - ST-02
  - DS-02
  - CM-02
  - QA-12
  - RT-10
difficulty: advanced
tags:
  - active-learning
  - labeling-budget
  - acquisition-function
  - cold-start
  - sampling-bias
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_weak_supervision_strategy.md
  - domain-AI-ML/data-for-ml/mldata_labeling_guideline_designer.md
  - domain-AI-ML/data-for-ml/mldata_sampling_bias_audit.md
  - domain-AI-ML/model-evaluation-validation/mleval_error_analysis_slicing.md
---

# Active Learning Strategy

**Objective:** Design a labelling loop that spends budget where it actually changes the model — establishing first that label quantity is the binding constraint, choosing an acquisition strategy against the specific failure being fixed, and controlling the biased labelled pool that active learning necessarily creates.

**When to Use:**
- Unlabelled data is plentiful, labelling is expensive, and the labelling budget is the constraint.
- Error analysis has identified underperforming slices and you need labels concentrated there.
- An existing labelling process selects examples at random and you suspect that wastes budget.

**When NOT to Use:**
- Labelling is cheap relative to the value of the model — random sampling is simpler, unbiased, and often enough.
- Labels can be derived programmatically from existing signals — use `mldata_weak_supervision_strategy.md`.
- The bottleneck is label *quality* or annotator disagreement rather than quantity — more of the same labels will not help; use `mldata_labeling_guideline_designer.md`.

## Inputs / Context

- **Current model performance and its gaps** — overall and per slice, since acquisition should target a named gap.
- **Labelling cost and throughput** — cost per label, annotator capacity, and turnaround per batch.
- **Unlabelled pool** — size, and how well it represents deployment traffic.
- **Retraining cost and cadence** — active learning requires repeated retraining, which is often the real cost.
- **Label latency** — the delay between selecting an example and having its label, which sets the loop's clock.
- **Existing labelled set** — size and how it was sampled, since the loop inherits its biases.

## Constraints

**Must:**
- Establish that labelling volume is the binding constraint before designing the loop — compare against a learning curve, since a model on a plateau will not improve with more labels of the same kind.
- Choose the acquisition strategy against a named failure: uncertainty sampling for boundary refinement, diversity for coverage gaps, expected-model-change for efficiency, or targeted slice sampling for a specific weakness.
- Maintain a **randomly sampled held-out set that the loop never touches**, since the actively labelled pool is biased by construction and cannot serve as an unbiased evaluation set.
- State the cold-start plan — most acquisition strategies need a model good enough to be informative, and the first rounds must be random or stratified.
- Track and report the labelled pool's drift away from the deployment distribution over rounds.

**Must Not:**
- Evaluate the model on the actively acquired labels; they over-represent hard and boundary cases and will understate real performance.
- Assert acquisition-strategy comparison results or labelling-efficiency figures from memory; mark quantities `[measure on your data]`.
- Run uncertainty sampling from a model too weak to have meaningful uncertainty; early rounds will chase noise.
- Ignore that active learning concentrates labels on hard cases, which raises annotator disagreement and slows throughput — budget for it.
- Let the loop run without a stopping rule.

**Instructions:**

1. **Verify labelling is the constraint.** Plot a learning curve on the existing labelled set. If performance has plateaued, more labels of the same kind will not help and the problem lies in features, architecture, or label quality — say so and stop.

2. **Name the failure being fixed.** "Overall accuracy" is too vague to guide acquisition. Name a slice, a confusion pair, or a coverage gap; the acquisition strategy follows from it.

3. **Choose the acquisition strategy for that failure.**
   - *Uncertainty sampling* — refines a boundary the model is unsure about. Vulnerable to outliers and label noise.
   - *Diversity / representativeness* — fills coverage gaps. Better in early rounds and for novel regions.
   - *Expected model change / gradient-based* — efficient, more expensive to compute.
   - *Targeted slice sampling* — when error analysis has already named the weak slice; the simplest and often the strongest option.
   - *Hybrid* — uncertainty within a diversity-constrained candidate pool, which mitigates the outlier problem.

4. **Plan the cold start.** The first rounds use random or stratified sampling until the model is informative enough for the chosen strategy. State the round at which the strategy switches and what triggers it.

5. **Set the batch size against label latency and retraining cost.** Small batches are more informative per label but require more retrains; large batches waste some budget on now-redundant examples. Choose from the real cost of a retrain and the annotator turnaround, not from convention.

6. **Protect evaluation.** Hold out a randomly sampled set fixed at the start, never fed by the loop. All reported performance comes from it. Without this, the loop generates its own increasingly favourable evaluation set and nobody notices.

7. **Guard the biased pool.** Track how the labelled pool's distribution diverges from the deployment distribution each round. Reserve a fraction of each batch — say a fixed minority — for random sampling to slow the drift and keep the pool usable for other purposes later.

8. **Handle the annotation consequence.** Actively selected examples are harder, so agreement falls and throughput drops. Plan for adjudication on the ambiguous cases and expect a lower labels-per-hour rate than random sampling produced.

9. **Set the stopping rule.** Stop when held-out performance gains per batch fall below a stated threshold, when the target slice reaches its goal, or when budget is exhausted. Write it down in advance.

**Output Format:**

A markdown strategy:
- **Constraint Check** — learning curve evidence that labels are the bottleneck.
- **Target Failure** — the named slice, confusion pair, or gap.
- **Acquisition Strategy** — chosen, with the reason and its known weakness.
- **Cold-Start Plan** — rounds, switch trigger.
- **Batch Sizing** — derived from latency and retraining cost.
- **Protected Evaluation Set** — construction and size.
- **Pool-Drift Guard** — random reserve fraction, drift tracking.
- **Annotation Impact** — expected agreement and throughput change, adjudication plan.
- **Stopping Rule** — the condition, stated in advance.

## Verification

- [ ] A learning curve establishes that labels are the binding constraint.
- [ ] The target failure is named specifically, not as overall accuracy.
- [ ] The acquisition strategy matches the failure and its weakness is stated.
- [ ] A cold-start plan exists with an explicit switch trigger.
- [ ] Batch size is derived from label latency and retraining cost.
- [ ] A randomly sampled evaluation set is held out and never fed by the loop.
- [ ] Pool drift is tracked and a random reserve fraction is specified.
- [ ] Annotation throughput and agreement impact are planned for.
- [ ] A stopping rule is written before the loop starts.
- [ ] No efficiency or strategy-comparison figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Start an active learning loop without checking the learning curve — if the model has plateaued, the loop buys expensive labels that change nothing.
- Evaluate on actively acquired labels; they are deliberately hard, so measured performance drops and the loop appears to be making things worse.
- Run uncertainty sampling in round one; a weak model's uncertainty is noise, and the loop will spend its first batches on outliers.
- Let the labelled pool drift indefinitely toward boundary cases — it becomes unusable for training anything else, including the next model.
- Assume annotator throughput holds; harder examples take longer and produce more disagreement.
- Run the loop until the budget runs out; without a stopping rule you cannot tell success from exhaustion.

✅ **DO:**
- Prove labels are the constraint before building the machinery.
- Name the specific failure, and let it choose the acquisition strategy.
- Start random, switch on an explicit trigger, and say what the trigger is.
- Freeze a random evaluation set at the start and report only from it.
- Reserve part of every batch for random sampling to keep the pool honest.
- Budget for lower throughput and plan adjudication for the ambiguous cases the loop will surface.

## Example Output

```markdown
## Active Learning: Contract-Clause Classifier (18 clause types)

### Constraint Check
Learning curve on the existing 12k labelled clauses: performance still rising at the current
size, with no plateau. **Labels are the constraint** — the loop is justified. Had the curve
flattened, the answer would have been better features or a different representation, not a
labelling programme.

### Target Failure
Not "accuracy". Error analysis names two things:
1. **Indemnity vs limitation-of-liability confusion** — the dominant confusion pair, and the
   costliest one for downstream review.
2. **Coverage gap on non-standard contract templates** (~6% of traffic, ~1% of labelled data).

These are different failures needing different acquisition, which is why "improve accuracy"
would have been the wrong specification.

### Acquisition Strategy
**Hybrid, split by failure:**
- 60% of each batch: **uncertainty sampling restricted to the indemnity/LoL confusion pair** —
  targeted rather than global, so budget goes to the named boundary.
- 25%: **diversity sampling within non-standard templates** — a coverage gap, not a boundary
  problem, so uncertainty would be the wrong tool.
- 15%: **random reserve** (see pool-drift guard).

Known weakness: uncertainty sampling will surface OCR-garbled clauses that are uncertain
because they are unreadable, not because they are informative. Mitigation: a readability
pre-filter on the candidate pool.

### Cold-Start Plan
Not applicable to the confusion-pair stream — the existing 12k model is already informative on
those two classes. The non-standard-template stream **starts random** for two rounds, because
the model has seen almost none of that population and its uncertainty there is meaningless.
Switch trigger: once ≥300 non-standard examples are labelled.

### Batch Sizing
Label latency ~4 days for a 500-clause batch. Retraining cost is modest. Batch of 500 chosen so
one retrain happens per fortnight — small enough to stay informative, large enough that the
annotator team is not idle waiting for the next selection.

### Protected Evaluation Set
2,000 clauses sampled **randomly** from deployment traffic, frozen before round one, never fed
by the loop. All reported numbers come from it. This is the single control preventing the loop
from grading its own homework.

### Pool-Drift Guard
15% of each batch is random. Tracked per round: the labelled pool's clause-type distribution
and template mix versus deployment traffic. If divergence exceeds a set bound, the random
fraction rises. Without this the pool becomes an indemnity-boundary corpus and is useless for
training the next model on anything else.

### Annotation Impact
Expected: lower agreement on the selected clauses, since they sit on the confusion boundary by
construction. Plan: **dual annotation with adjudication** on the uncertainty stream only;
single annotation remains adequate for the diversity and random streams. Expect fewer clauses
per annotator-hour than the historical rate — budget on that basis rather than on past
throughput.

### Stopping Rule
Stop when any of:
- Held-out indemnity/LoL F1 reaches the target, **or**
- Per-batch held-out gain falls below a stated threshold for two consecutive rounds, **or**
- Non-standard-template coverage reaches proportional representation, **or**
- Budget exhausted.
Written now, before round one, so "the budget ran out" cannot be mistaken for success later.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** constraint check precedes strategy, which precedes batching — so the loop is not built before it is justified.
- **DS-02 (Metric Specification):** the stopping rule and drift bound are specified as measured quantities in advance.
- **CM-02 (Constraint Specification):** the protected evaluation set and random reserve are hard constraints on the loop.
- **QA-12 (False Positives Identification):** rejects evaluating on acquired labels and running uncertainty sampling from an uninformative model.
- **RT-10 (Troubleshooting Decision Tree):** the named failure type selects the acquisition strategy.

**Related Prompts:**
- `mldata_weak_supervision_strategy.md` — when labels can be derived rather than bought.
- `mldata_labeling_guideline_designer.md` — for the adjudication and agreement work this loop intensifies.
- `mldata_sampling_bias_audit.md` — auditing the bias this loop deliberately introduces.
- `../model-evaluation-validation/mleval_error_analysis_slicing.md` — produces the named failure this targets.
