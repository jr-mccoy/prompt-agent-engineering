---
title: "CV Transfer Learning & Pretrained Backbone Selector"
category: AI-ML/specialized-ml/computer-vision
description: "Select a pretrained backbone and adaptation strategy (linear probe / partial fine-tune / full fine-tune) for a vision task with limited data, matching domain gap, data volume, and compute to the right approach."
techniques:
  - RT-02
  - CM-02
  - DS-02
  - RT-05
  - QA-12
difficulty: intermediate
tags:
  - computer-vision
  - transfer-learning
  - pretrained-models
  - fine-tuning
  - limited-data
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/computer-vision/cv_task_framing.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_augmentation_strategy.md
  - domain-AI-ML/model-evaluation-validation/mleval_eval_result_skepticism_audit.md
---

# CV Transfer Learning & Pretrained Backbone Selector

**Objective:** Recommend a pretrained backbone and an adaptation strategy — feature extraction (linear probe), partial fine-tuning, or full fine-tuning — for a vision task with limited labeled data, by reasoning explicitly about the domain gap to the pretraining data, the available data volume, the task type, and the compute budget, and by attaching a validation protocol that won't be fooled by the small dataset.

**When to Use:**
- Limited labeled data and you must lean on a pretrained model.
- Choosing among backbone families (CNN vs transformer, supervised-ImageNet vs self-supervised vs domain-specific pretraining).
- Deciding how much of the network to fine-tune given data and compute.

**When NOT to Use:**
- You have abundant in-domain data and train from scratch (different tradeoff).
- The task type is still undecided (use `cv_task_framing.md` first).

## Inputs / Context

- **Task type & output** — classification / detection / segmentation / keypoint (governs which pretrained heads/necks are reusable).
- **Domain gap** — how visually similar the target imagery is to common pretraining corpora (natural images vs medical/satellite/industrial/document/microscopy).
- **Labeled data volume** — per class, and total; how much unlabeled in-domain data exists (for self-supervised options).
- **Compute & latency budget** — training and inference constraints, deployment hardware.
- **Constraints** — license/availability of candidate weights, model-size limits.

## Constraints

**Must:**
- Match adaptation depth to data volume and domain gap: small data + small gap → linear probe / shallow fine-tune; larger data or larger gap → deeper fine-tune.
- Justify the backbone family by domain gap and task type, not popularity.
- Attach a validation protocol robust to small data (cross-validation, frozen-vs-fine-tuned comparison, and a check against an embedding-based baseline).

**Must Not:**
- Recommend full fine-tuning of a large backbone on a few hundred images without warning about overfitting and the linear-probe alternative.
- Assert that one backbone "beats" another from memory/benchmarks — reason from the user's domain gap and require empirical comparison on their data.
- Ignore the domain gap when picking ImageNet-supervised weights for a far-domain task (e.g., grayscale medical, multispectral satellite).

**Instructions:**

1. **Characterize the domain gap.** Place the target imagery on a spectrum from "close to natural-image pretraining" to "far domain", and note channel/modality mismatches that affect weight reuse.

2. **Inventory candidate backbones.** Lay out viable families — supervised-ImageNet CNNs/ViTs, self-supervised (e.g., contrastive/MAE-style) weights, and any domain-specific pretrained models — with their fit to the gap and task.

3. **Pick the adaptation strategy.** Cross data volume × domain gap to choose linear probe, partial (unfreeze top blocks), or full fine-tune; state discriminative learning-rate / freezing schedule at a conceptual level.

4. **Handle the head and modality.** Specify reusing vs reinitializing the task head, and any input-channel adaptation (e.g., grayscale or multispectral → adjust first conv).

5. **Plan data-efficiency levers.** Pair the choice with augmentation (cross-link), and consider self-supervised pretraining on unlabeled in-domain data when labels are very scarce.

6. **Define the comparison protocol.** Specify a small, fair bake-off: linear probe vs partial vs full on the same CV folds, with a simple embedding-kNN baseline, comparing on the deployment metric with intervals.

7. **Guard against small-data evaluation traps.** Require grouped/stratified CV, a held-out test untouched by selection, and skepticism toward a single suspiciously high score.

**Output Format:**

A markdown recommendation:
- **Domain-Gap Assessment** — placement + modality notes.
- **Backbone Candidates** — table: Backbone Family | Pretraining | Fit to Gap | Task Suitability | Size/Latency
- **Adaptation Strategy** — chosen depth + freezing/LR rationale + head/channel handling.
- **Data-Efficiency Levers** — augmentation + optional self-supervised step.
- **Comparison Protocol** — the bake-off + baselines + intervals.
- **Small-Data Eval Guards** — CV scheme + golden test + skepticism note.

## Verification

- [ ] Adaptation depth is matched to data volume and domain gap, with the linear-probe option considered.
- [ ] Backbone choice is justified by domain gap and task type, not benchmark recall.
- [ ] Head reuse/reinit and any channel adaptation are specified.
- [ ] A fair comparison protocol with baselines and intervals is defined.
- [ ] Small-data evaluation traps (selection on test, no grouping) are explicitly guarded.

## False-Positive Prevention

❌ **DON'T:**
- Full-fine-tune a 100M-param backbone on 300 images and trust the result — it will overfit; a linear probe is often stronger.
- Assume ImageNet-supervised features transfer to far domains (X-ray, SAR, microscopy) without testing; self-supervised or domain-pretrained weights frequently win there.
- Declare backbone A > backbone B from leaderboard memory instead of measuring on the user's data.
- Select the backbone/strategy by peeking at the test set.

✅ **DO:**
- Scale fine-tuning depth to data volume and gap; start frozen and unfreeze as data allows.
- Test feature transferability empirically (linear probe = a fast probe of representation fit).
- Run a same-folds bake-off with a kNN-on-embeddings baseline and report confidence intervals.
- Keep a golden test set untouched until the final choice is locked.

## Example Output

```markdown
## Transfer Strategy: Defect Classification on PCB Macro Photos (~800 labeled, 6 classes)

### Domain-Gap Assessment
Close-to-moderate gap: RGB macro photos share texture statistics with natural images but with repetitive structured backgrounds and tiny defects. No channel mismatch.

### Backbone Candidates
| Family | Pretraining | Fit to Gap | Task Suitability | Size/Latency |
|---|---|---|---|---|
| ResNet-50 | Supervised ImageNet | Good | Strong baseline | medium |
| ConvNeXt-Tiny | Supervised ImageNet | Good | Strong, efficient | medium |
| ViT-B (MAE) | Self-supervised | Good; data-efficient features | needs more data to FT | large |

### Adaptation Strategy
800 images, moderate gap → **partial fine-tune**: freeze stem + early blocks, fine-tune top 1–2 stages + new 6-way head, discriminative LR (low for backbone, higher for head). Reinitialize head; no channel change.

### Data-Efficiency Levers
Augmentation: random crop/scale, brightness, small rotation (PCB orientation varies) — flips OK (no orientation semantics). Optional: MAE-style self-supervised pretrain on ~50k unlabeled board photos before fine-tuning.

### Comparison Protocol
5-fold stratified CV: linear probe vs partial FT vs full FT on ConvNeXt-Tiny and ResNet-50, plus kNN-on-frozen-embeddings baseline. Compare macro-F1 with 95% CIs.

### Small-Data Eval Guards
Group folds by board panel (panels share defects → leakage). Hold out a final test panel set untouched. Treat any single fold >0.97 macro-F1 as a leakage signal to investigate.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** backbones/strategies weighed across gap, data, task, compute.
- **CM-02 (Constraint Specification):** data volume, compute, and license act as governing constraints.
- **DS-02 (Metric Specification):** comparison protocol fixes the metric and intervals.
- **RT-05 (Evidence-Based Reasoning):** transferability claims require measurement, not benchmark recall.
- **QA-12 (False Positives Identification):** guards small-data overfitting and selection-on-test traps.

**Related Prompts:**
- `cv_task_framing.md` — task type constrains which pretrained necks/heads are reusable.
- `cv_augmentation_strategy.md` — the primary data-efficiency lever paired with transfer.
- `mleval_eval_result_skepticism_audit.md` — interrogate suspiciously strong small-data results.
