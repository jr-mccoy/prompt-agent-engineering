---
title: "Fine-Tuning Strategy (Full vs Partial vs Adapter)"
category: AI-ML/deep-learning
description: "Decide between full, partial (last-k layers), and adapter/PEFT fine-tuning of a deep network based on data budget, domain distance, compute, and serving constraints — with a forgetting-aware validation plan."
techniques:
  - RT-02
  - ST-02
  - CM-02
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - fine-tuning
  - peft
  - adapters
  - catastrophic-forgetting
  - compute-budget
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/deep-learning/dl_transfer_learning_plan.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_quantization_plan.md
  - domain-AI-ML/deep-learning/dl_regularization_strategy.md
---

# Fine-Tuning Strategy (Full vs Partial vs Adapter)

**Objective:** Choose the fine-tuning *depth* for a pretrained deep network — full fine-tuning, partial (top-k layers), or parameter-efficient adapters (e.g., LoRA-style, bottleneck adapters) — by weighing data budget, domain distance, compute/memory, multi-task serving needs, and catastrophic-forgetting risk, then specify a validation plan that detects forgetting and overfitting. For LLM-specific instruction/PEFT recipes, cross-link the GenAI/LLM fine-tuning workflow.

**When to Use:**
- A backbone is already chosen and you must decide how many parameters to update.
- Compute/memory limits make full fine-tuning expensive and you're weighing PEFT.
- You need to serve several task variants from one base model (favoring adapters).

**When NOT to Use:**
- You haven't chosen a backbone or freezing schedule yet (`dl_transfer_learning_plan.md`).
- This is an LLM instruction-tuning/RLHF task — use the GenAI/LLM fine-tuning workflow (cross-link) for tokenizer, dataset, and PEFT specifics.
- The goal is post-training compression, not adaptation (`mlopt_quantization_plan.md`).

## Inputs / Context

Provide what you can:
- **Framework & version**, base model size, and the target task/data budget (labeled count, balance).
- **Domain distance** between pretraining and target.
- **Compute & memory budget** for training; **serving constraints** (latency, model count, storage).
- **Number of downstream tasks/variants** to support from one base.
- **Validation protocol** and any reference benchmark for the base model's original capability (to detect forgetting).

## Constraints

**Must:**
- Tie the depth choice to data budget, domain distance, compute, and multi-task serving — not to a single factor.
- Include a catastrophic-forgetting check when the base model's original capabilities must be preserved.
- Specify storage/serving implications (adapters add small per-task deltas; full FT duplicates the whole model).

**Must Not:**
- Recommend full fine-tuning on a small target set without flagging the overfitting/forgetting risk.
- Quote PEFT method accuracy parity as a fact for the user's task — frame as a hypothesis to measure against a full-FT or frozen baseline.
- Ignore that adapters can underperform when domain distance is large and the base lacks relevant features.

**Instructions:**

1. **Score the decision factors.** Rate data budget, domain distance, compute/memory, and multi-task serving need. These jointly point to a depth.

2. **Map factors to depth.** Small data + near domain → adapters or last-k partial. Large data + far domain → fuller fine-tuning. Many tasks from one base → adapters (cheap per-task deltas). Tight train memory → PEFT.

3. **Specify the partial-FT cut.** If partial, choose which layers to unfreeze (typically top blocks + head) and the discriminative LRs.

4. **Specify the adapter design.** If PEFT, choose the adapter type, where it's inserted, rank/bottleneck size (illustrative starting point), and which base weights stay frozen.

5. **Plan the forgetting + overfitting checks.** Define a held-out probe of the base model's original capability (if it matters) and the target val protocol; both must hold.

6. **Account for serving.** State storage and latency consequences: adapter deltas per task vs full model copies; whether adapters merge at inference.

7. **Set the comparison baseline.** Require comparing the chosen depth against at least a frozen-feature baseline and, where feasible, a partial-FT or full-FT reference, with intervals.

**Output Format:**

A markdown report:
- **Decision-Factor Scores** — table: Factor | Rating | Implication.
- **Recommended Depth** — full / partial / adapter + rationale.
- **Configuration** — layers to update or adapter spec (illustrative).
- **Forgetting & Overfitting Checks.**
- **Serving Implications.**
- **Baseline Comparison Plan.**

## Verification

- [ ] Depth choice reflects data budget, domain distance, compute, and serving — not one factor alone.
- [ ] A catastrophic-forgetting check is included when base capability must be preserved.
- [ ] Serving/storage implications of the chosen depth are stated.
- [ ] A comparison baseline (frozen and/or full-FT) is specified with intervals.
- [ ] PEFT parity claims are framed as hypotheses to measure, not facts.

## False-Positive Prevention

❌ **DON'T:**
- Full-fine-tune a large base on a small target set without flagging forgetting/overfitting.
- Assume LoRA-style adapters always match full FT — parity is task-dependent and must be measured.
- Pick adapters for a far-domain task where the base simply lacks the needed features.
- Forget that full FT duplicates the entire model per task at serving time.

✅ **DO:**
- Map the depth to the joint factor scores, not a single rule of thumb.
- Probe the base model's original capability to detect forgetting.
- Compare the chosen depth to frozen and (where feasible) full-FT baselines with CIs.
- Account for per-task storage/latency when serving many variants.

## Example Output

```markdown
## Fine-Tuning Depth: Domain QA Adapter on a Mid-Size Encoder (8k labeled pairs)

### Decision-Factor Scores
| Factor | Rating | Implication |
|---|---|---|
| Data budget | Small-medium (8k) | Favors PEFT/partial |
| Domain distance | Near | Adapters viable |
| Compute/memory | Limited | Favors PEFT |
| Multi-task serving | 4 variants from one base | Strongly favors adapters |

### Recommended Depth
Adapter/PEFT (bottleneck adapters) over full fine-tuning.

### Configuration (illustrative)
Insert bottleneck adapters in each transformer block, rank ~16; freeze base; train adapters + head.

### Forgetting & Overfitting Checks
Probe base on its original task suite (must not regress); target val via stratified split with early stopping.

### Serving Implications
~MBs of adapter weights per task vs duplicating the full base ×4; adapters can stay modular.

### Baseline Comparison Plan
Compare adapters vs frozen-feature head and a partial-FT (top-2 blocks) reference; report metric with 95% CIs.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** scores depth across data/domain/compute/serving.
- **ST-02 (Structured Sequential Instructions):** score → map → configure → check → compare.
- **CM-02 (Constraint Specification):** compute, memory, and serving constraints drive the choice.
- **DS-06 (Prioritization & Severity Guidance):** orders depth options by fit and risk.
- **QA-01 (Self-Verification):** checklist enforces forgetting checks and baseline comparisons.

**Related Prompts:**
- `dl_transfer_learning_plan.md` — choose the backbone and freezing schedule first.
- `mlopt_quantization_plan.md` — compress the adapted model for serving.
- `dl_regularization_strategy.md` — regularize when fine-tuning on a small target set.
```