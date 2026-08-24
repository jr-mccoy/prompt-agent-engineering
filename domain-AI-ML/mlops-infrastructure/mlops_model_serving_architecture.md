---
title: "MLOps Model Serving Architecture"
category: AI-ML/mlops-infrastructure
description: "Choose and design a model serving pattern — online/batch/streaming, real-time vs async — driven by latency, throughput, freshness, and cost requirements, not defaults."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-02
  - DS-06
difficulty: advanced
tags:
  - model-serving
  - inference
  - latency
  - batch-vs-online
  - architecture
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_model_packaging_strategy.md
  - domain-AI-ML/mlops-infrastructure/mlops_feature_pipeline_design.md
  - domain-AI-ML/mlops-infrastructure/mlops_infra_cost_optimization.md
---

# MLOps Model Serving Architecture

**Objective:** Select a serving pattern (online real-time, online async, batch, or streaming) from the actual requirements — latency budget, throughput, prediction freshness, and cost ceiling — and design the architecture around it, so the system is shaped by its constraints rather than defaulting to a real-time REST endpoint.

**When to Use:**
- Deciding how a trained model will deliver predictions to consumers.
- An existing serving setup is over- or under-engineered (real-time endpoint for a nightly job, or batch for an interactive need).
- Latency, cost, or freshness requirements have changed and the pattern should be re-evaluated.

**When NOT to Use:**
- Packaging the model artifact itself (use `mlops_model_packaging_strategy.md`).
- Pure infra cost tuning of an already-chosen pattern (use `mlops_infra_cost_optimization.md`).

## Inputs / Context

Provide what you can; the design adapts to gaps:
- **Consumption pattern** — who calls predictions, how often, interactive vs background, request volume and shape (per-request vs bulk).
- **Latency budget** — the p50/p99 the consumer can tolerate, end to end.
- **Freshness requirement** — must predictions reflect data from seconds ago, or is yesterday fine?
- **Throughput** — peak requests/sec or records/run; burstiness.
- **Feature availability** — are features precomputed, looked up online, or computed at request time?
- **Cost ceiling & platform** — budget posture; serving platform (SageMaker / Vertex / Databricks / KServe / self-managed). Ask if unspecified.

## Constraints

**Must:**
- Derive the pattern from latency × freshness × throughput × cost — show the reasoning, not a default.
- State the latency budget as a number and design to the p99, not the average.
- Address feature retrieval at serving time, since train/serve skew is decided here, not just in training.

**Must Not:**
- Recommend real-time online serving when the consumer is a scheduled job (cost without benefit).
- Assume platform autoscaling magically meets the p99 SLA; state the scaling and cold-start behavior.
- Ignore the failure/fallback path; a serving design without a degraded mode is incomplete.

**Instructions:**

1. **Characterize the demand.** Establish call pattern, volume, burstiness, and whether consumption is interactive (human waiting) or background (machine consuming). This is the primary fork.

2. **Set the budgets explicitly.** Write the latency budget (p99), freshness requirement, throughput target, and cost ceiling as numbers. These are the axes the pattern is chosen against.

3. **Choose the pattern with reasoning.** Map the budgets to a pattern — batch (precompute, store, serve from cache), online real-time (sync request/response), online async (queue + callback), or streaming (event-driven scoring) — and justify against each rejected alternative.

4. **Design feature retrieval for the pattern.** Specify how features are fetched at inference and how that path matches training, to prevent train/serve skew. For online, address the online feature store / cache; for batch, the join.

5. **Design scaling and resource shape.** Specify instance/accelerator type, batching (request batching, micro-batching), autoscaling triggers, and cold-start handling against the p99.

6. **Design the failure and fallback path.** Define behavior on model error, timeout, or dependency outage (cached prediction, default/heuristic, fail-closed vs fail-open), and circuit-breaking.

7. **Define versioning and rollout.** State how a new model version is rolled out (canary/shadow/blue-green) and pinned, and how rollback works within the SLA.

8. **State observability.** Specify what is monitored at serving time (latency, error rate, prediction distribution, feature freshness) to catch degradation.

**Output Format:**

A markdown design doc:
- **Demand Profile** — call pattern, volume, interactive vs background.
- **Budgets** — latency p99, freshness, throughput, cost ceiling (as numbers).
- **Pattern Decision** — chosen pattern + table: Pattern | Fits? | Why rejected/chosen.
- **Architecture** — components, feature retrieval path, request flow (text/ASCII diagram).
- **Scaling & Resources** — instance/accelerator, batching, autoscaling, cold-start.
- **Failure & Fallback** — degraded modes, circuit breaking.
- **Rollout & Observability** — versioning strategy + monitored signals.

## Verification

- [ ] The pattern choice is justified against each rejected alternative, tied to the budgets.
- [ ] The latency budget is a number and the design targets p99, not average.
- [ ] Feature retrieval at serving time is specified and matched to the training path.
- [ ] Scaling behavior (including cold start) is shown to meet the p99 under peak load.
- [ ] A failure/fallback path and a version rollback path are both defined.

## False-Positive Prevention

❌ **DON'T:**
- Default to a real-time REST endpoint because it is familiar, when the consumer is a nightly batch job.
- Quote average latency as proof of meeting an SLA defined on p99.
- Assume features will "just be available" online and let serving compute them differently than training did.
- Call a design done without a fallback for model/dependency failure.

✅ **DO:**
- Choose batch/precompute when freshness tolerates it — it is usually far cheaper and simpler than online.
- Size and load-test against p99 at peak, including cold-start, before committing the pattern.
- Make the serving feature path use the same code/definitions as training (or an online store fed by it).
- Specify a degraded mode (cached/heuristic) and a sub-SLA rollback for bad versions.

## Example Output

```markdown
## Serving Architecture — Product Recommendations (platform: Vertex AI)

### Demand Profile
- Called on every product-page load; interactive (user waiting). ~4k req/s peak, bursty at promotions.

### Budgets
- Latency p99 < 80ms end-to-end. Freshness: features ≤ 5 min old acceptable. Throughput: 4k req/s. Cost ≤ $6k/mo.

### Pattern Decision
| Pattern | Fits? | Why |
|---|---|---|
| Batch precompute | Partial | Catalog too large × users for full precompute; long-tail users missed. |
| Online real-time | Chosen | Meets interactive p99 with cached candidates + light reranker. |
| Streaming | No | No event-trigger; request-driven. |

### Architecture
page load → API → online feature store (Redis) → reranker model (GPU-less, ONNX) → response.
Candidate generation precomputed nightly (batch); online step only reranks ~200 candidates.

### Scaling & Resources
- CPU instances, request batching to 32, HPA on QPS; min replicas warm to avoid cold start at promo spikes.

### Failure & Fallback
- Feature store miss → popularity fallback. Model timeout (>60ms) → cached prior recs. Circuit-break at 5% error.

### Rollout & Observability
- Shadow new version 24h, then 10% canary. Monitor p99, error rate, rec-distribution drift, feature freshness.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** demand → budgets → pattern → features → scaling → failure.
- **RT-02 (Multi-Dimensional Analysis Framework):** pattern chosen across latency/freshness/throughput/cost.
- **CM-02 (Constraint Specification):** the four budgets are the binding constraints.
- **DS-02 (Metric Specification):** budgets are stated as numbers, designed to p99.
- **DS-06 (Prioritization & Severity Guidance):** the pattern decision table ranks fit by constraint.

**Related Prompts:**
- `mlops_model_packaging_strategy.md` — the artifact this architecture serves.
- `mlops_feature_pipeline_design.md` — the feature path that prevents train/serve skew here.
- `mlops_infra_cost_optimization.md` — tune the chosen pattern's cost.
