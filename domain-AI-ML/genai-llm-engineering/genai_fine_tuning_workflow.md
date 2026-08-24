---
title: "LLM Fine-Tuning Workflow (SFT / LoRA / QLoRA)"
category: AI-ML/genai-llm-engineering
description: "Run a disciplined fine-tuning workflow for LLMs — data prep, method choice (full SFT vs LoRA vs QLoRA), training, evaluation against a held-out set, and an honest is-it-worth-it gate."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - fine-tuning
  - lora
  - qlora
  - sft
  - llm-training
  - evaluation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_finetune_vs_rag_vs_prompt_decision.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_evaluation_design.md
  - domain-AI-ML/genai-llm-engineering/genai_synthetic_data_with_llms.md
---

# LLM Fine-Tuning Workflow (SFT / LoRA / QLoRA)

**Objective:** Produce a step-by-step fine-tuning plan for an LLM — from training-data curation through method selection (full supervised fine-tuning vs LoRA vs QLoRA), hyperparameter and compute planning, training, and evaluation against a held-out set — with an explicit gate that decides whether fine-tuning actually beat the simpler prompt/RAG baseline it must justify itself against.

**When to Use:**
- You've already decided (or strongly suspect) fine-tuning is warranted and need a rigorous plan to execute.
- You need to adapt an open-weights model to a specific style, format, or domain behavior that prompting can't reliably hold.
- You must justify fine-tuning's cost and maintenance to a reviewer with numbers.

**When NOT to Use:**
- You haven't decided whether fine-tuning is even the right tool (use `genai_finetune_vs_rag_vs_prompt_decision.md` first).
- The goal is injecting fresh/changing knowledge (RAG usually fits better than fine-tuning).
- You only need an eval program design (use `genai_llm_evaluation_design.md`).

## Inputs / Context

State the base model + provider + version. Provide what you can:
- **Objective** — what behavior change is wanted (style, format adherence, domain task, tool-use pattern).
- **Data** — how many examples exist, their source/quality, label process, and licensing/PII status.
- **Baseline** — current prompt/RAG performance the fine-tune must beat, on a defined metric.
- **Constraints** — compute budget, hosting (can you serve a custom model?), latency, update cadence.
- **Eval** — the held-out set and metric that will judge success (or note that it must be built).

## Constraints

**Must:**
- Require a frozen held-out evaluation set, built and reserved before training, with the baseline measured on it first.
- Justify the method (full SFT / LoRA / QLoRA) against compute, model size, data volume, and serving constraints.
- Treat data quality and deduplication as the primary lever; specify the curation and leakage check.

**Must Not:**
- Claim fine-tuning improved performance without comparing to the prompt/RAG baseline on the same held-out set.
- Reuse training examples in evaluation, or let synthetic eval data overlap training (cross-link `genai_synthetic_data_with_llms.md`).
- Invent expected accuracy gains, loss curves, or required example counts from memory — frame these as to-be-measured ranges.

**Instructions:**

1. **Restate the objective as a measurable target.** Convert "make it better at X" into a metric and a held-out set, and record the prompt/RAG baseline on that set. The fine-tune must beat this to ship.

2. **Curate and format the training data.** Specify the instruction/response schema for the base model, dedup, quality filtering, balance across behaviors, and a train/val/test split. Run a leakage check so eval examples never appear in training. Note PII/licensing handling.

3. **Choose the method.** Compare full SFT (max capacity, max compute, full checkpoint to serve), LoRA (adapter, far cheaper, mergeable), and QLoRA (quantized base, fits smaller GPUs). Tie the choice to model size, GPU budget, data volume, and whether you can host adapters. State the rejected options.

4. **Plan hyperparameters and compute.** Specify starting ranges for learning rate, epochs (watch overfitting on small sets), batch/accumulation, LoRA rank/alpha/target modules — framed as starting points to tune on the validation set, with compute/time estimates to verify against current hardware/pricing.

5. **Train with monitoring.** Track training and validation loss, watch for overfitting/divergence, checkpoint, and define early-stopping. Note that low loss ≠ good downstream behavior — eval is the arbiter.

6. **Evaluate against the held-out set and baseline.** Run the frozen eval; compare fine-tuned vs baseline with confidence intervals/significance. Include regression checks for general capabilities (catastrophic forgetting) and a qualitative review of failures.

7. **Run the worth-it gate.** Decide ship/iterate/abandon based on whether the gain over baseline justifies the training + serving + maintenance cost, including the cost of re-tuning when the base model updates.

8. **Plan maintenance.** Specify how the model is versioned, monitored in prod, and re-trained, and the trigger conditions for re-tuning.

**Output Format:**

A markdown workflow plan:
- **Target & Baseline** — metric, held-out set, current prompt/RAG number
- **Data Plan** — schema, curation, split, leakage check, PII/licensing
- **Method Decision** — table: Method | Fit | Cost | Rejected because
- **Training Plan** — starting hyperparameters (marked tunable), compute estimate (marked verify), monitoring
- **Evaluation Plan** — held-out comparison, forgetting check, significance
- **Worth-It Gate** — decision rule comparing gain to total cost
- **Maintenance Plan** — versioning, monitoring, re-tune triggers

## Verification

- [ ] A frozen held-out set exists and the prompt/RAG baseline is measured on it before training.
- [ ] A leakage check confirms no train/eval overlap (including synthetic data).
- [ ] The method choice is justified against model size, compute, data, and serving — with rejected alternatives.
- [ ] Hyperparameters and compute are framed as tunable/verify, not asserted.
- [ ] Evaluation compares against baseline with significance and includes a forgetting check.
- [ ] The worth-it gate weighs gain against training + serving + re-tuning cost.

## False-Positive Prevention

❌ **DON'T:**
- Report "loss went down, fine-tuning worked" — training loss says nothing about downstream task quality.
- Compare the fine-tuned model only to the *base* model; the real bar is your tuned prompt/RAG baseline.
- Use fine-tuning to inject knowledge that changes frequently — it bakes in a snapshot and goes stale.
- Train on a large noisy dataset assuming more is better; a smaller high-quality, deduplicated set usually wins.

✅ **DO:**
- Measure the prompt/RAG baseline on a frozen held-out set first and make the fine-tune beat it.
- Verify no train/eval contamination, especially with LLM-generated examples.
- Check general-capability regressions (forgetting), not just the target task.
- Account for the recurring cost of re-tuning when the base model version changes.

## Example Output

```markdown
## Fine-Tuning Plan: Support-Reply Style Adapter (base: <provider/open-weights vX>)

### Target & Baseline
Target: replies match our voice + always include a ticket-ID line, judged on a 0–3 rubric.
Held-out: 200 tickets, SME-scored. Prompt baseline: mean 2.1 (format-line compliance 78%).

### Data Plan
4,800 historical agent replies -> instruction/response pairs. Dedup near-identical (down to 3,900),
filter low-quality, balance across 6 ticket categories. Split 80/10/10. Leakage check: hash-match
eval tickets out of train. PII scrubbed.

### Method Decision
| Method | Fit | Cost | Rejected because |
|---|---|---|---|
| LoRA | Style adaptation, mergeable, 1 GPU | low | — chosen |
| QLoRA | Would fit smaller GPU | low | unnecessary; we have the VRAM |
| Full SFT | Overkill for style task | high | cost not justified vs LoRA |

### Training Plan
LR 1e-4–2e-4, 2–3 epochs (small set -> overfit risk), rank 16, alpha 32, target attn+MLP.
All starting points; tune on val loss + rubric. Compute: ~verify on current GPU pricing.

### Evaluation Plan
Run held-out rubric, fine-tuned vs prompt baseline, bootstrap CI. Forgetting check on a
general-instruction set. Qualitative review of bottom-decile replies.

### Worth-It Gate
Ship only if rubric mean > 2.5 AND format compliance > 95% AND gain holds with non-overlapping CI,
weighing adapter serving + quarterly re-tune cost.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** data → method → train → eval → gate in order.
- **RT-02 (Multi-Dimensional Analysis Framework):** method choice weighs compute, data, serving, capacity.
- **DS-02 (Metric Specification):** success is a metric on a frozen held-out set vs a baseline.
- **CM-02 (Constraint Specification):** compute, serving, and the worth-it gate constrain the plan.
- **QA-12 (False Positives Identification):** guards against loss-as-proxy and contamination false wins.

**Related Prompts:**
- `genai_finetune_vs_rag_vs_prompt_decision.md` — confirm fine-tuning is the right tool first.
- `genai_llm_evaluation_design.md` — build the held-out eval this workflow depends on.
- `genai_synthetic_data_with_llms.md` — generate training data without contaminating eval.
