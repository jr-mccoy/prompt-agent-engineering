---
title: "LLM Observability & Tracing Design"
category: AI-ML/genai-llm-engineering
description: "Design observability for an LLM application — request/span tracing, token and cost accounting, latency, and online quality signals — so production behavior is debuggable, attributable, and evaluable in prod."
techniques:
  - ST-02
  - DS-02
  - RT-09
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - observability
  - tracing
  - cost
  - latency
  - eval-in-prod
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_llm_cost_latency_optimization.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_retrieval_quality_debug.md
  - domain-AI-ML/genai-llm-engineering/genai_guardrails_design.md
---

# LLM Observability & Tracing Design

**Objective:** Design the observability layer for an LLM application — end-to-end traces with spans for each step (retrieval, prompt assembly, model call, tool calls, guards), token/cost and latency accounting, and online quality signals — so any production response can be reconstructed, attributed to a cause, and evaluated in prod rather than only offline.

**When to Use:**
- Taking an LLM feature to production and needing to debug, cost-track, and quality-monitor it.
- Production answers are sometimes bad and you can't reconstruct what happened.
- Cost or latency is creeping and you need attribution by step/model/feature.

**When NOT to Use:**
- You're optimizing cost/latency and already have the data (use `genai_llm_cost_latency_optimization.md`).
- You need to debug a single RAG answer with traces in hand (use `genai_rag_retrieval_quality_debug.md`).

## Inputs / Context

State the model + provider + version. Provide what you can:
- **App architecture** — the steps a request flows through (retrieval, tools, guards, model calls, retries).
- **What you can't currently answer** — the debugging/cost/quality questions that are hard today.
- **Scale & constraints** — request volume, PII/logging-policy limits, retention, existing telemetry stack (OpenTelemetry, etc.).
- **Quality signals available** — user feedback (thumbs), downstream conversion, abstention/guard trips.

## Constraints

**Must:**
- Define a trace per request with a span per pipeline step, carrying inputs/outputs (privacy-permitting), latency, and status.
- Account for token usage and cost per call and aggregate by model, feature, and tenant.
- Capture online quality signals and enable eval-in-prod (sampling responses for offline scoring), with PII handling specified.

**Must Not:**
- Log raw prompts/outputs containing PII without a redaction/retention policy.
- Track only aggregate latency/cost without per-step attribution (you won't be able to localize regressions).
- Treat user thumbs-up as ground-truth quality without acknowledging its bias and sparsity.

**Instructions:**

1. **Map the request lifecycle.** List every step a request passes through (input guard, retrieval, rerank, prompt assembly, model call(s), tool calls, output guard, retries) — these become spans.

2. **Define the trace schema.** Specify the trace ID propagation, per-span fields (step, start/end, latency, status, input/output refs, token counts, model+version), and how multi-step/agentic flows nest. Align to OpenTelemetry conventions if a stack exists.

3. **Instrument cost and tokens.** Capture prompt/completion tokens and cost per call; tag with model, feature, prompt version, and tenant so cost is attributable and regressions in token usage are visible.

4. **Instrument latency.** Record per-span latency and time-to-first-token; expose p50/p95/p99 by step and model so the slow stage is identifiable.

5. **Capture quality signals.** Wire user feedback (thumbs, edits, regenerations), abstention/guard trips, and downstream outcomes. Note each signal's bias (thumbs are sparse and skewed) and don't treat any single one as truth.

6. **Enable eval-in-prod.** Sample production traces, run the offline judges/rubrics (cross-link the eval harness) on the sample, and trend quality over time — catching drift that offline eval misses.

7. **Handle privacy and retention.** Specify redaction of PII in logged inputs/outputs, retention windows, access controls, and what is stored vs referenced. Make this explicit, not implicit.

8. **Define dashboards and alerts.** Specify the views (cost/feature, latency/step, quality trend, guard-trip rate, error/retry rate) and alert thresholds, plus the path from an alert to a trace to a root cause.

**Output Format:**

A markdown observability spec:
- **Request Lifecycle / Span Map** — steps as spans
- **Trace Schema** — fields per span + trace propagation + nesting for agentic flows
- **Cost & Token Accounting** — captured fields + aggregation dimensions
- **Latency Metrics** — per-step percentiles + TTFT
- **Quality Signals** — signals captured + each one's bias caveat + eval-in-prod sampling
- **Privacy & Retention** — redaction, retention, access
- **Dashboards & Alerts** — views + thresholds + alert→trace→root-cause path

## Verification

- [ ] Every pipeline step is a span; a single response can be fully reconstructed from its trace.
- [ ] Token/cost is captured per call and attributable by model, feature, and tenant.
- [ ] Latency is reported per step (percentiles + TTFT), not just end-to-end.
- [ ] Quality signals are captured with their bias caveats; eval-in-prod sampling is defined.
- [ ] A PII redaction and retention policy is explicit.
- [ ] Alerts route to a trace that supports root-cause analysis.

## False-Positive Prevention

❌ **DON'T:**
- Log only the final response; without per-step spans you can't tell whether retrieval, the model, or a guard caused a bad answer.
- Treat thumbs-up rate as the quality metric — it's sparse, biased, and easily gamed by UI placement.
- Track total cost only; without per-feature/per-model tags a cost spike is unattributable.
- Store raw prompts/outputs with PII and figure out redaction later.

✅ **DO:**
- Trace each step as a span and propagate a request ID end-to-end.
- Pair sparse user signals with sampled eval-in-prod scoring for a fuller quality picture.
- Tag cost/tokens by model, feature, and prompt version so regressions are attributable.
- Specify redaction and retention up front, before logging real traffic.

## Example Output

```markdown
## Observability: RAG Support Assistant (model: <provider/model vX>)

### Span Map
input-guard -> retrieve -> rerank -> assemble-prompt -> model-call -> output-guard -> respond
(retries nest under model-call; tool calls nest as child spans)

### Trace Schema
trace_id propagated via header. Per span: name, t_start/t_end, latency_ms, status,
input_ref/output_ref (redacted store), tokens_in/out, model+version, prompt_version, tenant_id.

### Cost & Token Accounting
Per model-call: prompt/completion tokens + $ cost. Aggregate by model, feature, prompt_version,
tenant. Daily cost-per-feature dashboard; alert on >30% day-over-day token growth.

### Latency
Per-span p50/p95/p99 + TTFT. Current: retrieve p95 120ms, model-call p95 2.1s (dominant).

### Quality Signals
Thumbs (sparse, ~4% response rate — caveat noted), regenerate rate, abstention rate, guard trips.
Eval-in-prod: sample 1% of traces nightly, run faithfulness + correctness judges, trend weekly.

### Privacy & Retention
PII redacted in stored inputs/outputs; raw retained 7 days, redacted 90 days; access role-gated.

### Dashboards & Alerts
Views: cost/feature, latency/step, quality trend, guard-trip rate, error/retry. Alert: faithfulness
sample drops >0.05 week-over-week -> page on-call; click-through to offending traces.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** lifecycle → schema → cost → latency → quality → privacy → dashboards.
- **DS-02 (Metric Specification):** token, cost, latency, and quality signals are precisely defined.
- **RT-09 (Root Cause Explanation):** traces enable alert→span→cause analysis.
- **CM-02 (Constraint Specification):** privacy/retention and alert thresholds bound the design.
- **QA-01 (Self-Verification):** eval-in-prod sampling continuously checks production quality.

**Related Prompts:**
- `genai_llm_cost_latency_optimization.md` — act on the cost/latency the traces surface.
- `genai_rag_retrieval_quality_debug.md` — use captured traces to debug bad answers.
- `genai_guardrails_design.md` — guard trips are a key observability signal.
