---
title: "Self-Supervised Pretraining Plan"
category: AI-ML/deep-learning
description: "Plan self-supervised pretraining on unlabelled domain data — justifying it against cheaper transfer options, designing a pretext task whose invariances match the downstream one, and evaluating on downstream performance rather than on the pretext objective."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - QA-12
  - DS-02
difficulty: advanced
tags:
  - self-supervised
  - pretraining
  - representation-learning
  - contrastive
  - transfer
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/deep-learning/dl_transfer_learning_plan.md
  - domain-AI-ML/deep-learning/dl_fine_tuning_strategy.md
  - domain-AI-ML/deep-learning/dl_architecture_selection.md
  - domain-AI-ML/model-evaluation-validation/mleval_benchmark_design.md
---

# Self-Supervised Pretraining Plan

**Objective:** Decide whether to pretrain on unlabelled domain data and, if so, design it well — justifying the cost against cheaper transfer options, choosing a pretext task whose invariances match what the downstream task needs, and evaluating only on downstream performance.

**When to Use:**
- Unlabelled domain data is abundant while labels are scarce, and off-the-shelf pretrained models were trained on a visibly different distribution.
- Fine-tuning a public checkpoint underperforms and the gap looks like a domain mismatch rather than a capacity or data-quantity problem.
- Multiple downstream tasks will share one representation, which is what makes the pretraining cost amortizable.

**When NOT to Use:**
- A public pretrained model on a similar distribution works well enough — use `dl_transfer_learning_plan.md`; pretraining is expensive and often unnecessary.
- Labels are plentiful; supervised training on the target task will usually beat a self-supervised detour.
- Only one narrow downstream task exists and it is small — the cost will not amortize.

## Inputs / Context

- **Unlabelled data** — volume, and how well it matches the downstream deployment distribution.
- **Downstream tasks** — all of them, since the value of a shared representation scales with how many there are.
- **Downstream invariances required** — what the model should treat as the same, and crucially what it must *not*.
- **Baseline results** — supervised-from-scratch and public-checkpoint fine-tuning, both measured.
- **Compute budget** — pretraining is the expensive step; state what is available.
- **Modality** — images, text, audio, time series, tabular; available pretext tasks differ sharply.

## Constraints

**Must:**
- Establish both baselines — from scratch and public-checkpoint fine-tuning — before committing to pretraining. Without them the pretraining result is uninterpretable.
- Choose a pretext task whose induced invariances **match the downstream task's needs**, and explicitly list any invariance that would destroy downstream signal.
- Evaluate on downstream task performance with limited labels, not on the pretext objective; pretext loss improves steadily while downstream performance does not necessarily follow.
- State the compute cost and the number of downstream tasks it must amortize across.
- Check that pretraining data does not contain downstream evaluation examples — this is a leakage path that inflates every result.

**Must Not:**
- Assert pretraining-scale rules, method-comparison results, or downstream-gain figures from memory; mark quantities `[measure on your data]`.
- Select augmentations by convention when a conventional one destroys a downstream-critical property — colour jitter on a task where colour is the label is the canonical example, and its equivalents exist in every modality.
- Report pretext-task metrics as evidence of representation quality.
- Compare a pretrained model against a from-scratch baseline trained with a different label budget or schedule.
- Continue pretraining because the loss is still falling, without downstream evidence that it is buying anything.

**Instructions:**

1. **Measure both baselines.** Supervised from scratch on available labels, and fine-tuning the best available public checkpoint. Report both across label budgets, since the entire case for pretraining is usually about the low-label regime.

2. **Justify the domain gap.** State concretely how the unlabelled domain data differs from what public checkpoints saw. If the gap is small, the pretraining case is weak and should be abandoned here rather than after the compute is spent.

3. **List required and forbidden invariances.** What must the representation treat as equivalent, and what must it never collapse? This list selects the pretext task and its augmentations, and is the step where most self-supervised plans go wrong.

4. **Choose the pretext task for the modality and invariances.**
   - *Contrastive / instance discrimination* — strong general representations; the augmentation set defines the invariances, so it must be designed against step 3.
   - *Masked prediction* — reconstruct hidden portions; well suited to sequences and to modalities where local context predicts the whole.
   - *Predictive / next-step* — natural for temporal data.
   - *Clustering-based* — useful where the natural grouping structure matters downstream.

5. **Design the augmentation or corruption set against the invariance list.** Each augmentation asserts "these two things are the same". Verify none of those assertions is false for the downstream task, and record the ones you deliberately excluded.

6. **Check for evaluation contamination.** Confirm no downstream test example appears in the pretraining corpus, including near-duplicates. Deduplicate across the boundary before pretraining, not after the numbers look good.

7. **Set the evaluation protocol.** Downstream performance at several label budgets — this is the only measurement that matters. Include linear probing (frozen representation) and full fine-tuning, since they answer different questions: probing measures representation quality, fine-tuning measures practical benefit.

8. **Define the stopping rule.** Stop when downstream performance at the target label budget plateaus across evaluation checkpoints — not when the pretext loss flattens, and not when the compute budget is exhausted.

9. **Amortize honestly.** State total pretraining cost and how many downstream tasks share the result. If the answer is one task, revisit whether this was the right choice.

**Output Format:**

A markdown plan:
- **Baselines** — table: Approach | Label budget | Downstream metric.
- **Domain-Gap Justification** — how the data differs, and why transfer is insufficient.
- **Invariance Requirements** — required vs forbidden.
- **Pretext Task** — chosen, with the fit to the invariance list.
- **Augmentation Set** — table: Augmentation | Invariance asserted | Downstream-safe?
- **Contamination Check** — deduplication across pretraining and evaluation data.
- **Evaluation Protocol** — label budgets, linear probe vs fine-tune.
- **Stopping Rule** — downstream-based.
- **Cost & Amortization** — compute cost, tasks sharing the representation.

## Verification

- [ ] Both baselines are measured before pretraining is committed to.
- [ ] The domain gap is stated concretely, not assumed.
- [ ] Required and forbidden invariances are listed before the pretext task is chosen.
- [ ] Every augmentation is checked against the forbidden list.
- [ ] Pretraining data is deduplicated against downstream evaluation data.
- [ ] Evaluation is on downstream tasks at multiple label budgets, both probed and fine-tuned.
- [ ] The stopping rule is based on downstream performance, not pretext loss.
- [ ] Compute cost and the number of amortizing tasks are stated.
- [ ] No scale rules or method-comparison figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Start pretraining without a measured public-checkpoint baseline — the most common outcome of that shortcut is spending heavily to match something that was already available.
- Copy a standard augmentation set into a domain where one of its invariances is false; asserting that colour, orientation, or scale does not matter is a claim about your task, not a default.
- Report falling pretext loss as progress; it falls reliably whether or not the representation is becoming useful.
- Evaluate only with full fine-tuning — that can mask a weak representation that the labelled data repaired, and you will not know which did the work.
- Compare against a from-scratch baseline that was given fewer epochs or a worse schedule; that is not a baseline, it is a foil.
- Leave near-duplicates between the pretraining corpus and the evaluation set — the resulting gain is contamination, and it is invisible in every downstream metric.

✅ **DO:**
- Measure from-scratch and transfer baselines first, across label budgets, and let them decide whether to proceed.
- Write the forbidden-invariance list before choosing augmentations, and check every augmentation against it.
- Evaluate downstream at several label budgets, with both linear probing and fine-tuning.
- Deduplicate across the pretraining/evaluation boundary before running anything.
- Stop on downstream plateau, and record the checkpoint that achieved it.
- State the amortization honestly, including when the answer is that it does not amortize.

## Example Output

```markdown
## Self-Supervised Pretraining: Industrial Defect Inspection
~4M unlabelled production-line images; ~9k labelled defect images across 7 defect classes.

### Baselines
| Approach | 1k labels | 4k labels | 9k labels |
|---|---|---|---|
| From scratch | `[measure]` | `[measure]` | `[measure]` |
| Public checkpoint fine-tuned | `[measure]` | `[measure]` | `[measure]` |

Both trained with the same schedule and budget — a from-scratch baseline given a worse schedule
would make pretraining look better than it is.

### Domain-Gap Justification
Public checkpoints are trained on natural photographs: varied lighting, arbitrary orientation,
colour as a salient object property. Our images are fixed-camera, fixed-lighting, top-down,
near-monochrome metal surfaces where defects are sub-millimetre texture deviations. The
mismatch is in exactly the properties that matter — a public representation encodes object
semantics we do not need and discards fine texture we depend on.

### Invariance Requirements
**Required (must treat as the same):**
- Position of the part within the frame (parts arrive at varying offsets).
- Small rotations up to the fixture tolerance.
- Sensor noise between camera units.

**Forbidden (must NOT collapse):**
- **Fine-grained texture** — the defect signal is texture.
- **Local contrast** — several defect classes differ only in contrast.
- **Scale** — defect size is a class-distinguishing property.

### Pretext Task
**Masked patch prediction**, not contrastive. Contrastive learning would require an augmentation
set that asserts invariances, and the three properties we must preserve are precisely the ones
standard augmentation sets destroy. Masked prediction forces the model to reconstruct fine
texture rather than to discard it, which aligns with the downstream signal.

### Augmentation Set
| Augmentation | Invariance asserted | Downstream-safe? |
|---|---|---|
| Random crop with fixed scale | position | **Yes** |
| Rotation ±5° | small rotation | **Yes** — within fixture tolerance |
| Gaussian noise, low σ | sensor noise | **Yes** |
| **Random resized crop** | scale | **NO — excluded.** Defect size is class-relevant |
| **Colour jitter / contrast** | colour and contrast | **NO — excluded.** Contrast is class-relevant |
| **Blur** | high-frequency detail | **NO — excluded.** Texture is the signal |

Three of the six most standard augmentations are excluded. Copying a default recipe here would
have trained the model to be invariant to the three things it must discriminate on — and the
pretext loss would have looked fine throughout.

### Contamination Check
The 9k labelled images were drawn from the same production line as the 4M unlabelled set.
**Near-duplicate risk is high** — consecutive frames of the same part. Deduplicate by
perceptual hash across the boundary and remove any unlabelled image within the duplicate
threshold of an evaluation image, **before** pretraining. Without this the downstream gain
would partly be memorization of the test set.

### Evaluation Protocol
Downstream defect classification at 500 / 1k / 4k / 9k labels. Both **linear probe** on frozen
features and **full fine-tuning**. The probe answers "is the representation good"; fine-tuning
answers "does this help in practice". Reporting only the latter would hide a weak representation
that 9k labels quietly repaired.

### Stopping Rule
Evaluate downstream at fixed pretraining checkpoints. Stop when the 1k-label probe result
plateaus across two consecutive checkpoints — the low-label regime is the entire justification,
so it is the regime the stopping rule watches. Pretext loss is monitored for sanity only and is
never the stopping signal.

### Cost & Amortization
Pretraining cost `[estimate on your cluster]`. Downstream tasks sharing the representation:
defect classification (7 classes), defect segmentation, and a planned anomaly-detection task on
the same line — **three tasks**, which is what makes the cost defensible. Were it only the
classifier, the honest recommendation would be to spend the same budget on more labels.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** baselines precede justification, which precedes pretext-task choice, so cost is committed only after the case is made.
- **RT-02 (Multi-Dimensional Analysis Framework):** invariance requirement × augmentation × downstream safety is the design grid.
- **CM-02 (Constraint Specification):** the forbidden-invariance list and downstream-only evaluation rule bound the design.
- **QA-12 (False Positives Identification):** rejects pretext loss as evidence and catches augmentation-induced destruction of downstream signal.
- **DS-02 (Metric Specification):** downstream performance at stated label budgets is the defined success measure.

**Related Prompts:**
- `dl_transfer_learning_plan.md` — the cheaper option that must be ruled out first.
- `dl_fine_tuning_strategy.md` — adapting the pretrained representation downstream.
- `dl_architecture_selection.md` — the architecture the pretext task must suit.
- `../model-evaluation-validation/mleval_benchmark_design.md` — designing the downstream evaluation properly.
