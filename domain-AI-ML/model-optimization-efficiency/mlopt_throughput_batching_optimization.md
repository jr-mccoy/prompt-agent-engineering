---
title: "ML Throughput & Batching Optimization"
category: AI-ML/model-optimization-efficiency
description: "Maximize serving throughput (requests/sec, tokens/sec) under a fixed latency SLA via dynamic batching, concurrency, and GPU-utilization tuning — measuring the throughput/latency frontier and the cost-per-request, not just peak utilization."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-02
  - QA-12
difficulty: advanced
tags:
  - throughput
  - dynamic-batching
  - concurrency
  - gpu-utilization
  - serving-optimization
  - latency-sla
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-optimization-efficiency/mlopt_inference_latency_optimization.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_hardware_accelerator_selection.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_compression_tradeoff_analysis.md
---

# ML Throughput & Batching Optimization

**Objective:** Maximize serving throughput (requests/sec or tokens/sec) for a model **subject to a fixed latency SLA**, by tuning dynamic/continuous batching, concurrency, and accelerator utilization — and characterizing the throughput-vs-latency frontier and the resulting cost-per-request, so a throughput gain is never claimed at the silent expense of tail latency or accuracy.

**When to Use:**
- A service is accelerator-bound and you want to serve more traffic per GPU/instance without breaching the latency SLA.
- You need to size a fleet and want the throughput each instance can sustain at the SLA.
- You suspect low accelerator utilization and want to batch/parallelize without hurting p95/p99.

**When NOT to Use:**
- Single-request latency is the binding constraint and batching would hurt it (use `mlopt_inference_latency_optimization.md`).
- The model cannot fit or run efficiently on the hardware at all (use `mlopt_hardware_accelerator_selection.md`).
- You need to shrink the model first (use `mlopt_compression_tradeoff_analysis.md`).

## Inputs / Context

Provide what you can:
- **Target hardware + runtime/server** — accelerator model, inference server, and whether it supports dynamic or continuous (in-flight) batching. *Ask the user if unspecified.*
- **Framework + version** — model framework and serving stack.
- **Latency SLA** — the binding percentile (often p95/p99) and the ceiling; throughput is maximized *under* this.
- **Workload profile** — request rate, burstiness, request-size distribution (sequence length / image size), arrival pattern.
- **Accuracy bar** — the metric and budget, since some throughput levers (aggressive padding, precision) can affect outputs.
- **Cost basis** — instance cost, to compute cost-per-request/token.

## Constraints

**Must:**
- Treat the latency SLA as a hard ceiling; report throughput only at SLA-compliant tail latency, never peak throughput at unbounded latency.
- Ask for target hardware + runtime/server and framework + version; tie batching levers to what the server actually supports.
- Pair throughput gains with their tail-latency cost and (for output-altering levers) accuracy cost, plus cost-per-request.

**Must Not:**
- Quote specific throughput/utilization numbers as measured — mark figures as estimates to verify under the user's load on their hardware.
- Equate high GPU utilization with high goodput — utilization can be high while serving inefficient batches.
- Ignore request-size heterogeneity (padding waste) when proposing static batching.

**Instructions:**

1. **Fix the SLA and define goodput.** State the binding latency percentile/ceiling and define throughput as SLA-compliant goodput (requests/tokens served within SLA), not raw QPS. This is the optimization target.

2. **Characterize the workload.** Capture request-rate, burstiness, and size distribution; heterogeneous sizes drive the choice between static, dynamic, and continuous batching and reveal padding waste.

3. **Choose the batching strategy.** Static batching for uniform shapes; dynamic (queue-and-form) batching with a max-batch + max-delay for bursty/uniform; continuous/in-flight batching for autoregressive/variable-length generation. Justify against the server's capabilities.

4. **Tune the batch/delay/concurrency knobs.** Define max batch size, batch-formation timeout, and the number of concurrent model instances/replicas; explain the tension — larger batches raise throughput but also tail latency.

5. **Map the throughput–latency frontier.** Require a sweep: for each batch/concurrency setting, record goodput and p95/p99. The chosen operating point is the max goodput where p99 ≤ SLA.

6. **Tune utilization without overcommit.** Address memory headroom, queue depth, and avoiding accelerator OOM or queueing collapse under bursts; note that pushing utilization to 100% often spikes tail latency.

7. **Define the measurement & load protocol.** Specify a realistic load generator (matching arrival pattern and size distribution), warmup, steady-state window, and reporting of goodput + p50/p95/p99 + cost-per-request on the target hardware. Validate accuracy if any lever alters outputs.

8. **Set the operating point and fallback.** Pick the SLA-respecting max-goodput config; report cost-per-request. Define the fallback (compress model, add replicas, or change hardware) if goodput targets aren't met within SLA.

**Output Format:**

A markdown plan:
- **SLA & Goodput Definition** — binding percentile, ceiling, goodput metric
- **Workload Characterization** — rate, burstiness, size distribution
- **Batching Strategy** — choice + server-capability justification
- **Knob Settings** — max batch, timeout, concurrency/replicas
- **Throughput–Latency Frontier** — table: Config | Goodput (est.) | p95 | p99 | Within SLA?
- **Measurement & Load Protocol** — load shape, window, metrics, cost-per-request
- **Recommended Operating Point + Fallback**

## Verification

- [ ] Throughput is reported as SLA-compliant goodput at a stated tail-latency ceiling, not unbounded peak QPS.
- [ ] Target hardware/runtime/server and framework/version requested or used; batching mode matched to server support.
- [ ] A throughput–latency frontier sweep is required, not a single setting.
- [ ] Request-size heterogeneity and padding waste are addressed.
- [ ] Cost-per-request/token is reported alongside throughput.
- [ ] Accuracy is validated for any output-altering lever; a fallback exists.

## False-Positive Prevention

❌ **DON'T:**
- Report peak throughput measured while p99 latency blew past the SLA — that capacity is unusable.
- Read 95% GPU utilization as 95% useful work — heavy padding on variable-length requests wastes most of it.
- Use a synthetic uniform load to size a service that actually receives bursty, variable-size traffic.
- Crank batch size and concurrency to maximize QPS while ignoring the resulting tail-latency cliff.

✅ **DO:**
- Sweep the batch/concurrency space and pick the max goodput point where p99 ≤ SLA.
- Distinguish utilization from goodput; for variable-length workloads prefer continuous batching to cut padding waste.
- Drive load with a generator that matches the real arrival pattern and size distribution.
- Report cost-per-request so a throughput win that requires disproportionate hardware is exposed.

## Example Output

```markdown
## Throughput Optimization: LLM Chat Endpoint (target: 1x GPU, serving runtime vX)

### SLA & Goodput Definition
Binding: p99 time-to-first-token ≤ 800 ms AND p99 end-to-end ≤ 6 s. Goodput = completed generations/min within SLA.

### Workload Characterization
~40 req/s peak, bursty; prompt 50–2,000 tokens, output 20–500 tokens (highly variable).

### Batching Strategy
Continuous (in-flight) batching — variable-length generation makes static/dynamic batching pad-heavy and stall short requests behind long ones. Server supports it.

### Knob Settings
Max concurrent sequences = 32 (sweep 8–48); KV-cache memory budget reserved; 1 replica per GPU.

### Throughput–Latency Frontier
| Config (max seqs) | Goodput (est.) | p95 e2e | p99 e2e | Within SLA? |
|---|---|---|---|---|
| 8 | low | 3.1 s | 4.0 s | Yes |
| 32 | high | 5.2 s | 5.9 s | Yes |
| 48 | higher | 6.4 s | 7.8 s | No (p99 breach) |

### Measurement & Load Protocol
Replay 30 min of production-shaped traffic; 2 min warmup; report goodput + p50/p95/p99 + $/1k generations on target GPU.

### Recommended Operating Point + Fallback
Operate at max 32 sequences (max goodput within SLA). Fallback if traffic grows: add a replica or apply int8 weight quantization to fit a larger batch.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** SLA → workload → strategy → knobs → frontier → measurement → operating point.
- **RT-02 (Multi-Dimensional Analysis Framework):** trades throughput, tail latency, and cost simultaneously.
- **CM-02 (Constraint Specification):** the latency SLA is the hard ceiling on all throughput claims.
- **DS-02 (Metric Specification):** defines goodput and the percentile + cost metrics.
- **QA-12 (False Positives Identification):** guards against utilization-as-goodput and peak-QPS-over-SLA illusions.

**Related Prompts:**
- `mlopt_inference_latency_optimization.md` — when single-request latency, not aggregate throughput, binds.
- `mlopt_hardware_accelerator_selection.md` — when scaling out/up is the real lever.
- `mlopt_compression_tradeoff_analysis.md` — when a smaller model raises per-instance goodput.
```