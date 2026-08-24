# Model Optimization & Efficiency

Making a model small enough, fast enough, or cheap enough to deploy — compression, hardware choice, serving-side inference optimization, and the routing decision that avoids the problem by sending easy work to a cheaper model.

**11 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Inference cost or latency is the binding constraint.
- A model must fit on-device or inside a fixed memory budget.
- LLM serving is expensive and you need to know which lever applies.

**Not here:**
- The constraint is training cost rather than inference — [`../deep-learning/dl_distributed_training_plan.md`](../deep-learning/dl_distributed_training_plan.md).
- The question is how much accelerator capacity to buy — [`../mlops-infrastructure/mlops_gpu_capacity_planning.md`](../mlops-infrastructure/mlops_gpu_capacity_planning.md).
- The lever is prompt-level token reduction → [`../genai-llm-engineering/genai_llm_cost_latency_optimization.md`](../genai-llm-engineering/genai_llm_cost_latency_optimization.md).

## Prompts


**Decide the approach**

| Prompt | Use it to |
|---|---|
| [`mlopt_compression_tradeoff_analysis.md`](mlopt_compression_tradeoff_analysis.md) | Compare compression options (quantization, pruning, distillation, architecture swap, and their combinations) across the size / latency / accuracy / cost frontier for a stated deployment target, and recommend the option that meets the budget at the least accuracy cost — with every figure flagged for measurement. |
| [`mlopt_hardware_accelerator_selection.md`](mlopt_hardware_accelerator_selection.md) | Choose the right compute (CPU / GPU / TPU / NPU / inference accelerator) for training or serving a given workload and budget — scoring candidates on fit, throughput-per-dollar, memory ceiling, and ecosystem support, with the assumptions made explicit and verifiable. |
| [`mlopt_model_routing_cascade_design.md`](mlopt_model_routing_cascade_design.md) | Route requests across models of different cost — deciding whether difficulty can be judged before or only after inference, pricing the router's own cost and errors, and measuring end-to-end quality rather than the escalated-only subset. |

**Compress the model**

| Prompt | Use it to |
|---|---|
| [`mlopt_quantization_plan.md`](mlopt_quantization_plan.md) | Design a quantization plan — PTQ vs QAT, precision per layer (int8/fp16/bf16), calibration, and an accuracy-recovery + validation protocol that pairs every speed/size gain with its measured quality cost. |
| [`mlopt_quantization_aware_training.md`](mlopt_quantization_aware_training.md) | Plan quantization-aware training when post-training quantization has failed — diagnosing why it failed before adding training cost, matching the QAT setup to the target runtime's actual arithmetic, and validating on task quality per slice rather than on aggregate accuracy. |
| [`mlopt_pruning_strategy.md`](mlopt_pruning_strategy.md) | Design a pruning strategy — structured vs unstructured, schedule, sparsity targets, and fine-tune recovery — that measures real wall-clock speedup on the target runtime, not just nominal sparsity, and pairs each gain with its accuracy cost. |
| [`mlopt_knowledge_distillation_plan.md`](mlopt_knowledge_distillation_plan.md) | Design a teacher→student distillation plan — student capacity, distillation objectives, temperature, transfer data, and evaluation — that pairs the efficiency gain of the smaller student with its measured accuracy cost versus both the teacher and a from-scratch baseline. |

**Optimize serving**

| Prompt | Use it to |
|---|---|
| [`mlopt_inference_latency_optimization.md`](mlopt_inference_latency_optimization.md) | Reduce single-request inference latency through profiling-driven levers — batching, graph compilation, kernel/operator fusion, caching, and precision — with a measurement plan that isolates the real bottleneck and pairs each gain with its accuracy/correctness cost. |
| [`mlopt_throughput_batching_optimization.md`](mlopt_throughput_batching_optimization.md) | Maximize serving throughput (requests/sec, tokens/sec) under a fixed latency SLA via dynamic batching, concurrency, and GPU-utilization tuning — measuring the throughput/latency frontier and the cost-per-request, not just peak utilization. |
| [`mlopt_llm_inference_serving_optimization.md`](mlopt_llm_inference_serving_optimization.md) | Optimize LLM serving throughput and latency — separating the prefill and decode phases because they bottleneck on different resources, sizing KV cache as the real capacity constraint, and choosing among continuous batching, speculative decoding, and parallelism against the measured limit. |
| [`mlopt_edge_deployment_optimization.md`](mlopt_edge_deployment_optimization.md) | Optimize a model for edge / mobile / embedded deployment — size, memory ceiling, power, and thermal limits — under hard on-device constraints, pairing each optimization with its accuracy cost and an on-device (not host) measurement plan. |

## Conventions

- **Prefix:** `mlopt_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/model-optimization-efficiency`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- Serving architecture and topology → [`../mlops-infrastructure/mlops_model_serving_architecture.md`](../mlops-infrastructure/mlops_model_serving_architecture.md).
- Cost attribution and budgeting → [`../mlops-infrastructure/mlops_cost_attribution_showback.md`](../mlops-infrastructure/mlops_cost_attribution_showback.md).
