---
title: "Transfer Learning Plan"
category: AI-ML/deep-learning
description: "Choose a pretrained backbone and design a freezing/unfreezing schedule, head design, and discriminative learning rates for a target task with limited labeled data."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - transfer-learning
  - pretrained-backbone
  - freezing
  - limited-data
  - fine-tuning
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/deep-learning/dl_fine_tuning_strategy.md
  - domain-AI-ML/deep-learning/dl_architecture_selection.md
  - domain-AI-ML/deep-learning/dl_regularization_strategy.md
---

# Transfer Learning Plan

**Objective:** For a target task with limited labeled data, select a pretrained backbone whose pretraining domain and architecture match the task, design the new head, and prescribe a staged freezing/unfreezing schedule with discriminative learning rates — plus a leakage- and domain-shift-aware validation plan so the transferred gains are real.

**When to Use:**
- Limited labeled data for the target task but a strong pretrained model exists for a related domain/modality.
- A from-scratch model overfits (per the diagnosis step) and transfer is the highest-leverage fix.
- You need a fast, data-efficient baseline before investing in custom architecture.

**When NOT to Use:**
- Plenty of in-domain labeled data and from-scratch is feasible (`dl_architecture_selection.md`).
- You already chose the backbone and only need the fine-tuning depth decision (`dl_fine_tuning_strategy.md`).
- LLM-specific instruction/PEFT tuning — cross-link to the GenAI/LLM fine-tuning workflow when that subdir is populated.

## Inputs / Context

Provide what you can:
- **Framework & version**, target modality and task, number of labeled target examples and class balance.
- **Candidate pretrained backbones** available and their pretraining domain (e.g., ImageNet, large text corpus, audio).
- **Domain distance** between pretraining data and target data (near vs far).
- **Compute/latency/size budget** for training and serving.
- **Validation protocol** and any known domain shift in the target data.

## Constraints

**Must:**
- Match backbone pretraining domain and architecture to the target; justify domain proximity.
- Stage the freeze/unfreeze schedule to the data budget (less data → freeze more, unfreeze gradually).
- Use a leakage- and shift-aware validation split so transfer gains are not artifacts.

**Must Not:**
- Quote a specific backbone's published accuracy as a guarantee for the target — frame as a starting hypothesis to measure.
- Unfreeze the whole backbone with a high LR on a few hundred examples (catastrophic forgetting/overfitting).
- Assume a far-domain backbone transfers without testing a frozen-feature baseline first.

**Instructions:**

1. **Assess domain proximity.** Judge how close the backbone's pretraining distribution is to the target. Near-domain favors deeper fine-tuning; far-domain favors frozen features + a trained head first.

2. **Shortlist and pick a backbone.** Compare 2–3 backbones on domain fit, size/latency budget, and tooling maturity; pick one and name the fallback.

3. **Design the head.** Specify the new task head (pooling, layers, output) and initialization; keep it small relative to the target data.

4. **Set the staged schedule.** Stage 1: freeze backbone, train head to convergence. Stage 2: unfreeze top blocks with a low LR. Stage 3 (if data allows): unfreeze more with discriminative (layer-wise) LRs, lowest near the input. Tie each stage to the data budget.

5. **Apply discriminative learning rates.** Lower LR for early/general layers, higher for the head; specify the ratio as a starting point to verify.

6. **Plan regularization for small data.** Add augmentation, weight decay, and early stopping sized to the limited target set; reference `dl_regularization_strategy.md`.

7. **Validate against transfer-specific failure modes.** Compare against a frozen-feature baseline, check for domain shift and leakage, and confirm the deeper schedule actually beats the frozen baseline before keeping it.

**Output Format:**

A markdown report:
- **Domain-Proximity Assessment** — near/far + implication.
- **Backbone Choice** — pick + comparison table + fallback.
- **Head Design.**
- **Freeze/Unfreeze Schedule** — staged, tied to data budget.
- **Discriminative LR Plan** — layer groups + relative LRs (illustrative).
- **Regularization for Small Data.**
- **Validation & Transfer Pitfall Checks.**

## Verification

- [ ] Backbone choice is justified by pretraining-domain proximity, not just popularity.
- [ ] The freeze/unfreeze schedule scales with the labeled-data budget.
- [ ] A frozen-feature baseline is specified as the gate before deeper fine-tuning.
- [ ] Validation is leakage- and domain-shift-aware.
- [ ] Any cited backbone metrics are framed as hypotheses to measure, not guarantees.

## False-Positive Prevention

❌ **DON'T:**
- Fully unfreeze a large backbone at a high LR on a few hundred labels — it forgets pretraining and overfits.
- Assume a far-domain backbone (e.g., natural images) transfers to a distant modality without a frozen-feature test.
- Trust a transfer "win" measured on a leaky or shifted val split.
- Treat the backbone's published benchmark score as the score you'll get on the target.

✅ **DO:**
- Start with frozen features + a trained head as the gate, then unfreeze gradually.
- Match backbone pretraining domain to the target and justify it.
- Use discriminative LRs (lower for general early layers).
- Validate on a leakage- and shift-aware split and beat the frozen baseline before going deeper.

## Example Output

```markdown
## Transfer Plan: Defect Detection on Factory Line (1.5k labeled images)

### Domain-Proximity Assessment
Natural-image pretraining (ImageNet) is moderately far from grayscale industrial textures → start frozen, unfreeze cautiously.

### Backbone Choice
| Backbone | Domain Fit | Size/Latency | Tooling | Verdict |
|---|---|---|---|---|
| Mid CNN (ImageNet) | Medium | Fits budget | Mature | Lead |
| Large ViT (ImageNet) | Medium | Too heavy | Mature | Fallback off |
| Small CNN (ImageNet) | Medium | Light | Mature | Fallback |

### Head Design
Global average pool → dropout(0.3) → linear(2). He-init head.

### Freeze/Unfreeze Schedule
S1: freeze backbone, train head. S2: unfreeze top 1–2 blocks at low LR. S3 skipped (only 1.5k labels).

### Discriminative LR Plan (illustrative)
Head 1e-3; top blocks 1e-4; rest frozen.

### Regularization for Small Data
Augmentation (flips/rotations/brightness), AdamW wd=1e-2, early stopping patience 8.

### Validation & Transfer Pitfall Checks
GroupKFold by production batch; compare to frozen-feature baseline; keep S2 only if it beats S1 on the untouched test set.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** proximity → backbone → head → staged schedule → validate.
- **RT-02 (Multi-Dimensional Analysis Framework):** backbone comparison across domain fit/size/tooling.
- **CM-02 (Constraint Specification):** data budget and serving limits bound the schedule.
- **DS-06 (Prioritization & Severity Guidance):** staged unfreezing ordered by risk/benefit.
- **QA-12 (False Positives Identification):** frozen-baseline gate and leakage/shift checks guard against false transfer wins.

**Related Prompts:**
- `dl_fine_tuning_strategy.md` — decide full vs partial vs adapter fine-tuning depth.
- `dl_architecture_selection.md` — when in-domain data is sufficient for from-scratch.
- `dl_regularization_strategy.md` — size regularization to the limited target set.
```