# Deep Learning

Training neural networks and debugging them when they misbehave — architecture choice, the training-failure diagnostics, transfer and fine-tuning, distributed and mixed-precision training, and the three regimes (self-supervised, continual, mixture-of-experts) that change how training works rather than how it is tuned.

**15 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Choosing or debugging a neural training run.
- Loss will not fall, or falls and then diverges.
- Deciding between training from scratch, transferring, or pretraining on your own unlabelled data.

**Not here:**
- The model is an LLM being applied rather than trained — [`../genai-llm-engineering/`](../genai-llm-engineering/README.md).
- The problem is the data pipeline feeding the trainer — [`../data-for-ml/`](../data-for-ml/README.md).
- The concern is inference cost rather than training — [`../model-optimization-efficiency/`](../model-optimization-efficiency/README.md).

## Prompts


**Choose the architecture and regime**

| Prompt | Use it to |
|---|---|
| [`dl_architecture_selection.md`](dl_architecture_selection.md) | Choose an architecture family (MLP, CNN, RNN/TCN, Transformer, or hybrid) that fits the data structure, task, and compute budget — with documented tradeoffs and a baseline-first plan. |
| [`dl_transfer_learning_plan.md`](dl_transfer_learning_plan.md) | Choose a pretrained backbone and design a freezing/unfreezing schedule, head design, and discriminative learning rates for a target task with limited labeled data. |
| [`dl_fine_tuning_strategy.md`](dl_fine_tuning_strategy.md) | Decide between full, partial (last-k layers), and adapter/PEFT fine-tuning of a deep network based on data budget, domain distance, compute, and serving constraints — with a forgetting-aware validation plan. |
| [`dl_self_supervised_pretraining.md`](dl_self_supervised_pretraining.md) | Plan self-supervised pretraining on unlabelled domain data — justifying it against cheaper transfer options, designing a pretext task whose invariances match the downstream one, and evaluating on downstream performance rather than on the pretext objective. |
| [`dl_continual_learning_strategy.md`](dl_continual_learning_strategy.md) | Design incremental model updating without catastrophic forgetting — first testing whether full retraining is genuinely infeasible, then choosing among replay, regularization, and architectural isolation, and measuring retained performance on old tasks as the primary metric. |
| [`dl_mixture_of_experts_design.md`](dl_mixture_of_experts_design.md) | Decide whether sparse mixture-of-experts is worth its complexity and design it if so — separating parameter count from active compute, addressing routing collapse and load imbalance before training, and accounting for the memory cost that sparsity does not remove. |

**Debug the training run**

| Prompt | Use it to |
|---|---|
| [`dl_training_not_converging_debug.md`](dl_training_not_converging_debug.md) | Decision-tree triage for a model whose loss won't decrease: isolate the cause across data, learning rate, initialization, normalization, and code bugs using cheap discriminating tests. |
| [`dl_gradient_issue_debug.md`](dl_gradient_issue_debug.md) | Decision-tree triage for vanishing gradients, exploding gradients, and NaNs/infs: localize the bad layer/op, then prescribe clipping, init, normalization, or numerical-stability fixes. |
| [`dl_overfitting_diagnosis_remedies.md`](dl_overfitting_diagnosis_remedies.md) | Diagnose a train/validation gap, distinguish genuine overfitting from leakage, distribution shift, or a broken val set, and prescribe a ranked, single-variable remedy plan. |
| [`dl_learning_rate_optimizer_selection.md`](dl_learning_rate_optimizer_selection.md) | Choose an optimizer and a learning-rate schedule (warmup/decay), run an LR-range test to find a working band, and tune one variable at a time with reproducible runs. |
| [`dl_regularization_strategy.md`](dl_regularization_strategy.md) | Choose and tune a regularization stack — dropout, weight decay, data augmentation, early stopping, label smoothing — matched to the overfitting driver, applied one knob at a time. |

**Scale and reproduce**

| Prompt | Use it to |
|---|---|
| [`dl_distributed_training_plan.md`](dl_distributed_training_plan.md) | Choose among data, model, pipeline, and tensor parallelism for a training job by model/memory fit and interconnect; plan communication, sharding, and correctness checks against a single-device reference. |
| [`dl_mixed_precision_setup.md`](dl_mixed_precision_setup.md) | Enable AMP/fp16/bf16 safely: choose the dtype, configure loss scaling, keep numerically sensitive ops in fp32, and verify parity and stability against an fp32 reference. |
| [`dl_data_loading_bottleneck_audit.md`](dl_data_loading_bottleneck_audit.md) | Find and fix input-pipeline bottlenecks starving the accelerator: localize the stall (I/O, decode, augmentation, host-to-device copy, collate) via measurement, then prescribe targeted fixes. |
| [`dl_reproducibility_setup.md`](dl_reproducibility_setup.md) | Make DL training reproducible — seeds, deterministic ops, dataloader worker seeding, environment and data pinning — and document the residual sources of nondeterminism that cannot be removed. |

## Conventions

- **Prefix:** `dl_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/deep-learning`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- LLM fine-tuning as an application workflow → [`../genai-llm-engineering/genai_fine_tuning_workflow.md`](../genai-llm-engineering/genai_fine_tuning_workflow.md).
- Quantization-aware training → [`../model-optimization-efficiency/mlopt_quantization_aware_training.md`](../model-optimization-efficiency/mlopt_quantization_aware_training.md).
