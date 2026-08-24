---
title: "LLM Inference Serving Optimization"
category: AI-ML/model-optimization-efficiency
description: "Optimize LLM serving throughput and latency — separating the prefill and decode phases because they bottleneck on different resources, sizing KV cache as the real capacity constraint, and choosing among continuous batching, speculative decoding, and parallelism against the measured limit."
techniques:
  - RT-02
  - DS-02
  - RT-10
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - llm-serving
  - kv-cache
  - continuous-batching
  - speculative-decoding
  - inference-optimization
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-optimization-efficiency/mlopt_throughput_batching_optimization.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_model_routing_cascade_design.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_cost_latency_optimization.md
  - domain-AI-ML/mlops-infrastructure/mlops_gpu_capacity_planning.md
---

# LLM Inference Serving Optimization

**Objective:** Raise throughput and lower latency for LLM serving by first identifying which of the two phases — prefill or decode — is actually binding, then choosing techniques against that specific limit rather than applying a general list of optimizations.

**When to Use:**
- LLM serving cost or latency is unacceptable and you need to know which lever to pull.
- Throughput is well below expectation and the cause is unclear.
- Choosing a serving configuration — batching policy, parallelism, cache sizing — for a new deployment.

**When NOT to Use:**
- The right answer is a smaller model or a cheaper route for easy requests — use `mlopt_model_routing_cascade_design.md`.
- The concern is prompt-level token reduction, caching, or model choice — use `../genai-llm-engineering/genai_llm_cost_latency_optimization.md`.
- The model is not autoregressive — use `mlopt_throughput_batching_optimization.md`.

## Inputs / Context

- **Traffic shape** — input and output token length distributions, both of which matter and matter differently.
- **Latency requirements** — time-to-first-token and inter-token latency separately, since users experience them differently.
- **Hardware** — accelerator memory, memory bandwidth, and interconnect if the model is sharded.
- **Model characteristics** — parameter count, architecture, attention structure, and precision.
- **Concurrency profile** — simultaneous requests at peak, and session length where conversations are multi-turn.
- **Current measured throughput and utilization** — including memory utilization, which is usually the real limit.

## Constraints

**Must:**
- Separate **prefill** (processing the prompt, compute-bound, parallel over tokens) from **decode** (generating tokens one at a time, memory-bandwidth-bound). They bottleneck on different resources, and an optimization for one frequently does nothing for the other.
- Treat **KV cache memory as the primary capacity constraint** in most deployments — it grows with batch size, sequence length, and concurrency, and it is what actually limits how many requests fit, not compute.
- Measure before optimizing: which phase dominates for this traffic shape, and whether the limit is memory capacity, memory bandwidth, or compute.
- Report time-to-first-token and inter-token latency separately; a single "latency" number conflates two different user experiences with different fixes.
- State the quality implication of any technique that changes outputs, and confirm which are output-preserving.

**Must Not:**
- Assert throughput figures, speedup ratios, or memory formulas from memory; mark quantities `[measure on your hardware]` or `[compute for your architecture]`.
- Recommend larger batches without checking KV cache headroom — this is the fastest route to out-of-memory under load.
- Apply decode-phase optimizations to a prefill-dominated workload, or the reverse; the traffic shape decides which matter.
- Treat speculative decoding as free — it trades extra compute for latency and its benefit depends heavily on acceptance rate for your traffic.
- Report average latency only; the tail is what breaks the user experience and the SLO.

**Instructions:**

1. **Profile the traffic shape.** Input and output token length distributions. A workload of long prompts and short completions is prefill-dominated; short prompts with long generations is decode-dominated. Many deployments contain both and need to be handled separately rather than averaged.

2. **Identify the binding resource.** Compute utilization, memory-bandwidth utilization, and memory capacity, measured under realistic load. Decode is typically memory-bandwidth-bound, so a low compute utilization number is expected and is not by itself a problem to fix.

3. **Compute the KV cache budget.** Cache size scales with layers, heads, sequence length, batch size, and precision. Work out the maximum concurrent sequences that fit in remaining memory after weights. **This number, not compute, usually sets serving capacity** — and knowing it changes which optimizations are worth attempting.

4. **Choose techniques against the identified limit.**
   - *Continuous / in-flight batching* — replaces finished sequences immediately instead of waiting for the whole batch. Large throughput gain in decode-dominated serving; output-preserving.
   - *Paged / block KV cache* — reduces fragmentation, raising effective concurrency at the same memory. Output-preserving.
   - *Prefix caching* — reuses KV for shared prefixes; strong where system prompts or conversation history repeat. Output-preserving.
   - *Speculative decoding* — a draft model proposes tokens a larger model verifies. Reduces latency when acceptance is high; costs extra compute; output-preserving when verification is exact.
   - *Quantization* — reduces weight and cache memory, raising concurrency. **Not output-preserving** — quality must be measured.
   - *Tensor / pipeline parallelism* — for models exceeding one device. Adds communication, and pipeline parallelism specifically hurts time-to-first-token.
   - *Chunked prefill* — interleaves prefill with decode so long prompts do not stall generation for other requests.

5. **Separate the two latency metrics.** Time-to-first-token is a prefill property; inter-token latency is a decode property. Measure and report both at p50 and p99, and set targets separately.

6. **Model the throughput–latency trade.** Larger effective batches raise throughput and raise inter-token latency. Plot the frontier for this workload and choose the operating point against the SLO rather than maximizing either.

7. **Verify quality for anything that changes outputs.** Quantization needs task-level evaluation, not perplexity alone. Confirm which chosen techniques are exactly output-preserving and which are not.

8. **Plan for the concurrency limit.** What happens when KV cache is exhausted: queue, evict and recompute, or reject. Preemption and recomputation are visible to users as stalls, so the policy is a product decision.

9. **Re-measure.** Optimizations interact — prefix caching changes the cache budget, which changes the batching frontier. State the re-measurement order.

**Output Format:**

A markdown optimization plan:
- **Traffic Shape** — input/output length distributions; prefill- or decode-dominated.
- **Binding Resource** — compute, memory bandwidth, or memory capacity, measured.
- **KV Cache Budget** — computed maximum concurrent sequences.
- **Technique Selection** — table: Technique | Targets which phase | Expected effect | Output-preserving? | Verdict.
- **Latency Targets** — TTFT and inter-token, p50 and p99, separately.
- **Throughput–Latency Frontier** — operating point and its justification.
- **Quality Verification** — for non-output-preserving techniques.
- **Concurrency-Limit Policy** — queue, evict, or reject.
- **Re-measurement Order** — how interactions are resolved.

## Verification

- [ ] Prefill and decode are analysed separately and the dominant phase is identified from traffic.
- [ ] The binding resource is measured, not assumed.
- [ ] The KV cache budget is computed and stated as the concurrency limit.
- [ ] Each technique names the phase it targets and whether it preserves outputs.
- [ ] TTFT and inter-token latency are reported separately at p50 and p99.
- [ ] The throughput–latency operating point is chosen against the SLO.
- [ ] Non-output-preserving techniques have a task-level quality check.
- [ ] The concurrency-limit policy is defined.
- [ ] No throughput figures or memory formulas are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Raise batch size to improve throughput without computing the KV cache headroom — this is the most common cause of production out-of-memory under load.
- Report low GPU compute utilization as waste in a decode-dominated workload; decode is memory-bandwidth-bound and low compute utilization is the expected signature.
- Apply speculative decoding without measuring acceptance rate on your traffic; a low acceptance rate makes it a net cost.
- Quote a single "latency" number — a fix that improves time-to-first-token may leave inter-token latency untouched, and users notice both.
- Adopt quantization on a perplexity check alone; task-level quality can degrade in ways perplexity does not surface.
- Optimize prefill for a workload where the prompts are short and the generations are long.

✅ **DO:**
- Profile the token-length distributions first; they determine which half of the problem you have.
- Compute the KV cache budget explicitly and treat it as the capacity number.
- Prefer output-preserving techniques — continuous batching, paged cache, prefix caching — before anything that trades quality.
- Report and target TTFT and inter-token latency separately at the tail.
- Measure acceptance rate before committing to speculative decoding.
- Re-measure after each change, since these optimizations interact through the same memory budget.

## Example Output

```markdown
## LLM Serving Optimization: Customer Support Assistant

### Traffic Shape
| Metric | p50 | p95 |
|---|---|---|
| Input tokens (system prompt + history + query) | `[measure]` | `[measure]` |
| Output tokens | `[measure]` | `[measure]` |

Two distinct populations: multi-turn conversations with **long, highly repetitive** inputs
(the same system prompt and accumulating history) and short first-turn queries. The repetition
is the most exploitable property of this workload and it is invisible in an averaged profile.

### Binding Resource
| Resource | Utilization under peak load |
|---|---|
| Compute | `[measure — expect moderate]` |
| Memory bandwidth | `[measure — expect high during decode]` |
| **Memory capacity (weights + KV cache)** | `[measure — expect the binding limit]` |

Low compute utilization here is **not** the problem to solve. Decode is memory-bandwidth-bound
by nature, and reporting spare compute as waste would send the work in the wrong direction.

### KV Cache Budget
Compute from layers × heads × head-dim × 2 (K and V) × sequence length × precision, for your
architecture `[compute]`. Then: available memory − weights = cache budget → **maximum concurrent
sequences**. This is the concurrency limit. Every batching decision below is bounded by it, and
no throughput plan is meaningful until it is calculated.

### Technique Selection
| Technique | Phase | Expected effect | Output-preserving | Verdict |
|---|---|---|---|---|
| Continuous batching | decode | large throughput gain; replaces finished sequences immediately | **Yes** | **Adopt first** |
| Paged KV cache | both | raises effective concurrency at the same memory | **Yes** | **Adopt** |
| **Prefix caching** | prefill | large win — system prompt and history repeat across turns | **Yes** | **Adopt — highest leverage for this workload** |
| Chunked prefill | both | stops long prompts stalling other requests' generation | **Yes** | Adopt if TTFT tail is driven by head-of-line blocking |
| Speculative decoding | decode | latency gain **if acceptance is high** | Yes (exact verification) | **Measure acceptance first** — support replies are formulaic, so acceptance may be favourable |
| Quantization | both | more concurrency via smaller weights and cache | **No** | Hold — only if concurrency is still short after the above |
| Tensor parallelism | both | needed only if the model exceeds one device | Yes | N/A here |

The first four are output-preserving and target this workload's actual properties. Reaching for
quantization before exhausting them would trade quality for capacity that prefix caching can
supply for free.

### Latency Targets
| Metric | p50 target | p99 target |
|---|---|---|
| Time-to-first-token | `[set]` | `[set]` |
| Inter-token latency | `[set]` | `[set]` |

Separate targets because separate causes: TTFT is prefill (helped by prefix caching and chunked
prefill), inter-token is decode (helped by continuous batching and speculative decoding). A
single latency SLO would hide which half is failing.

### Throughput–Latency Frontier
Sweep effective batch size and plot throughput against p99 inter-token latency `[measure]`.
Choose the point that meets the inter-token SLO with headroom, not the throughput maximum —
the maximum sits where latency has already breached.

### Quality Verification
Only quantization changes outputs. If adopted, evaluate on **task-level support-reply quality**
— correctness, tone, and instruction adherence — not perplexity. Perplexity can hold while
instruction-following degrades, which is precisely the failure that matters here.

### Concurrency-Limit Policy
When the KV cache budget is exhausted: **queue with an admission bound**, do not evict. Eviction
forces recomputation, which appears to the user mid-conversation as a stall — worse than a
slightly longer initial wait. Reject with a clear retry signal beyond the admission bound.

### Re-measurement Order
1. Prefix caching → re-measure the cache budget (it frees substantial cache for repeated prefixes).
2. Continuous batching + paged cache → re-measure the throughput–latency frontier.
3. Speculative decoding acceptance rate → decide adopt or drop.
4. Only then reconsider quantization, against the concurrency still needed.
Each step changes the memory budget the next step is chosen against, so the order is not
arbitrary.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** phase × binding resource × technique × output-preservation is the selection grid.
- **DS-02 (Metric Specification):** TTFT and inter-token latency are specified as distinct metrics with separate targets.
- **RT-10 (Troubleshooting Decision Tree):** traffic shape and binding resource route to the applicable technique set.
- **CM-02 (Constraint Specification):** the KV-cache-budget-first and output-preservation rules bound the plan.
- **QA-12 (False Positives Identification):** rejects low compute utilization as waste in decode-bound serving.

**Related Prompts:**
- `mlopt_throughput_batching_optimization.md` — general batching for non-autoregressive models.
- `mlopt_model_routing_cascade_design.md` — when a smaller model should handle part of the traffic.
- `../genai-llm-engineering/genai_llm_cost_latency_optimization.md` — prompt-level and model-choice levers.
- `../mlops-infrastructure/mlops_gpu_capacity_planning.md` — the memory budget this optimization operates within.
