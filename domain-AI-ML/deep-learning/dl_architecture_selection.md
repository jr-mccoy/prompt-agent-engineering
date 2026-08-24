---
title: "Deep Learning Architecture Selection"
category: AI-ML/deep-learning
description: "Choose an architecture family (MLP, CNN, RNN/TCN, Transformer, or hybrid) that fits the data structure, task, and compute budget — with documented tradeoffs and a baseline-first plan."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - CM-02
  - DS-06
difficulty: intermediate
tags:
  - architecture
  - model-selection
  - compute-budget
  - inductive-bias
  - baselines
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/deep-learning/dl_transfer_learning_plan.md
  - domain-AI-ML/deep-learning/dl_learning_rate_optimizer_selection.md
  - domain-AI-ML/deep-learning/dl_regularization_strategy.md
---

# Deep Learning Architecture Selection

**Objective:** Recommend an architecture family and a concrete starting configuration matched to the data's structure, the task type, the dataset size, and the compute/latency budget — choosing the *weakest sufficient* inductive bias and starting from a baseline rather than the largest model that fits in memory.

**When to Use:**
- Starting a new modeling effort and unsure whether the data wants an MLP, CNN, sequence model, or Transformer.
- A current architecture is overkill (slow, data-hungry) or underkill (can't fit the signal) for the problem.
- Deciding between a from-scratch architecture and a pretrained backbone.

**When NOT to Use:**
- A strong pretrained backbone for the modality already exists and transfer is obviously the play (go to `dl_transfer_learning_plan.md`).
- The bottleneck is data quality or leakage, not architecture (audit data first).
- Pure tabular problems where gradient-boosted trees usually beat deep nets — confirm a tree baseline first.

## Inputs / Context

Provide what you can:
- **Framework & version** — PyTorch / TensorFlow / JAX and version (APIs and defaults differ; state it).
- **Task type** — classification, regression, sequence labeling, generation, ranking, dense prediction (segmentation/detection).
- **Data structure** — tabular, image, audio, text, time series, graph, multimodal; input shapes; sequence lengths.
- **Dataset size** — labeled examples; class balance; whether more data is obtainable.
- **Compute & latency budget** — training hardware (GPU/TPU count, memory), max training time, inference latency/throughput SLA, deployment target (cloud/edge).
- **Existing baselines** — any current metric to beat.

## Constraints

**Must:**
- Match the architecture's inductive bias to the data's structure (locality → CNN, order/long-range dependency → sequence model/Transformer, no structure → MLP).
- Respect the stated compute and latency budget — reject configurations that cannot train or serve within it.
- Recommend a baseline before the headline model and define the gate it must clear.

**Must Not:**
- Fabricate parameter counts, FLOPs, or expected accuracy as established fact — present them as order-of-magnitude estimates and label them as such.
- Default to a Transformer because it is fashionable when data is small or structure is local.
- Ignore the data-size/model-capacity relationship (large attention models need either lots of data or pretraining).

**Instructions:**

1. **Restate the problem as (data structure × task × budget).** Name the three axes explicitly; the recommendation must follow from them, not from defaults.

2. **Map structure to inductive bias.** Locality/translation-invariance → CNN; sequential/temporal order → RNN/GRU/LSTM, TCN, or Transformer; permutation-invariant sets/graphs → GNN/DeepSets; no exploitable structure → MLP. State the bias each family encodes and why it fits (or doesn't).

3. **Set the baseline.** Propose the simplest credible model (e.g., logistic/linear, small MLP, or GBM for tabular) and the metric/threshold it establishes. The deep model must beat this to justify its cost.

4. **Size to the data and budget.** Estimate whether the dataset can support the candidate's capacity from scratch, or whether pretraining/transfer is required. Tie depth/width/sequence-handling to the memory and latency budget.

5. **Shortlist 2–3 candidates and score them.** Build a comparison across: fit-to-structure, data efficiency, compute cost (train + inference), latency, ecosystem/maturity, and team familiarity.

6. **Recommend a starting configuration.** Give a concrete first model (family, rough depth/width, key hyperparameters to set vs sweep) and an explicit fallback if it underperforms.

7. **Define the decision review point.** State what evidence (baseline gap closed, scaling behavior, overfitting signature) would trigger switching families.

**Output Format:**

A markdown report:
- **Problem Framing** — data structure × task × budget, one line each
- **Candidate Comparison** — table: Architecture | Fit-to-structure | Data efficiency | Train cost | Inference latency | Verdict
- **Recommendation** — chosen family + starting config + why
- **Baseline & Gate** — the simpler model and the bar the deep model must clear
- **Switch Triggers** — conditions that would change the recommendation

## Verification

- [ ] The recommendation is justified by data structure, task, and budget — not by popularity.
- [ ] A concrete baseline and a numeric/qualitative gate are specified.
- [ ] Compute and latency feasibility is checked against the stated budget.
- [ ] At least two candidates are compared on the same axes.
- [ ] Any quantitative estimate (params, FLOPs, accuracy) is labeled as an estimate, not a fact.
- [ ] Framework + version was requested or used to ground API-specific notes.

## False-Positive Prevention

❌ **DON'T:**
- Recommend a Transformer for a small tabular dataset because it is "state of the art" elsewhere.
- Claim an architecture "will reach X% accuracy" — that depends on data you cannot see.
- Conflate "bigger" with "better fit" — capacity beyond what the data supports just overfits or wastes compute.
- Skip the tree/linear baseline and jump straight to a deep net for tabular data.

✅ **DO:**
- Choose the weakest inductive bias that captures the signal; escalate only if the baseline shows it's needed.
- Tie model capacity to dataset size and recommend transfer when data is scarce.
- Present accuracy/cost figures as estimates with the assumptions that produced them.
- Make the deep model earn its place by beating an explicit baseline.

## Example Output

```markdown
## Architecture Selection: Defect Detection on Conveyor Camera Frames

### Problem Framing
- **Data structure:** images, 1024×768 RGB, ~12k labeled frames, strong spatial locality.
- **Task:** binary classification (defect / no defect), mild class imbalance (~8% defects).
- **Budget:** single A10 GPU, <50 ms inference on edge, train within 1 day.

### Candidate Comparison
| Architecture | Fit-to-structure | Data efficiency | Train cost | Inference latency | Verdict |
|---|---|---|---|---|---|
| MLP on flattened pixels | Poor (ignores locality) | Low | Low | Low | Reject |
| Small CNN from scratch | Good | Medium (12k is borderline) | Medium | Low | Backup |
| Pretrained CNN (ResNet-ish), fine-tuned | Good | High (transfer) | Low–Medium | ~Low | **Recommend** |
| ViT from scratch | Good but data-hungry | Low at this scale | High | Medium | Reject |

### Recommendation
Fine-tune a pretrained convolutional backbone (ImageNet-initialized), replace the head for binary output, freeze early blocks initially. ~Tens of millions of params (estimate). Locality bias + transfer fits 12k images far better than a from-scratch ViT.

### Baseline & Gate
Baseline: pretrained backbone as fixed feature extractor + logistic head. Gate: the fine-tuned model must beat this baseline's PR-AUC by a margin larger than the validation noise band before added complexity is justified.

### Switch Triggers
- If defects are too small/local for whole-frame classification → move to a detection/segmentation architecture.
- If transfer underperforms a from-scratch small CNN → revisit backbone choice and augmentation.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** framing → bias mapping → baseline → sizing → shortlist → recommendation.
- **RT-02 (Multi-Dimensional Analysis Framework):** candidates scored across structure-fit, data efficiency, cost, latency.
- **RT-05 (Evidence-Based Reasoning):** recommendation tied to the stated data/task/budget.
- **CM-02 (Constraint Specification):** compute and latency budget govern feasibility.
- **DS-06 (Prioritization & Severity Guidance):** candidates ranked to a single recommendation with switch triggers.

**Related Prompts:**
- `dl_transfer_learning_plan.md` — once a pretrained backbone is the chosen family.
- `dl_learning_rate_optimizer_selection.md` — set up training for the chosen architecture.
- `dl_regularization_strategy.md` — control capacity once the family is fixed.
