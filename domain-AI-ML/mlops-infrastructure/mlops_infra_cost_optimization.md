---
title: "MLOps Infra Cost Optimization"
category: AI-ML/mlops-infrastructure
description: "Reduce training and serving infrastructure cost without unacceptable loss of model quality or latency — by measuring spend, ranking levers, and gating each cut on a quality/SLA check."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - CM-02
  - RT-05
difficulty: advanced
tags:
  - cost-optimization
  - gpu-utilization
  - serving-cost
  - finops
  - latency-tradeoff
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_model_serving_architecture.md
  - domain-AI-ML/mlops-infrastructure/mlops_training_pipeline_orchestration.md
  - domain-software-engineering/cloud/cloud_cost_optimization.md
---

# MLOps Infra Cost Optimization

**Objective:** Cut training and serving infrastructure cost by first measuring where the money goes, then ranking concrete levers by (savings × safety), and gating every proposed cut on an explicit quality and latency check — so cost falls without an unacceptable drop in model quality or SLA compliance.

**When to Use:**
- ML infra spend (GPU training, serving fleet, storage) is high and growth is unexplained.
- Before scaling a workload, to right-size it first.
- A finance/FinOps request to reduce ML cost without "breaking the model."

**When NOT to Use:**
- Choosing the serving pattern from scratch (use `mlops_model_serving_architecture.md`).
- General (non-ML) cloud cost work (use `domain-software-engineering/cloud/cloud_cost_optimization.md`).

## Inputs / Context

Provide what you can; the analysis degrades gracefully:
- **Cost breakdown** — current spend split across training, serving, storage, and data movement (even rough).
- **Workload profile** — training frequency/duration, instance types, GPU utilization; serving QPS, instance count, idle %.
- **Quality & SLA bar** — the metric floor and latency p99 that must not be violated by any cut.
- **Utilization data** — GPU/CPU/memory utilization during training and serving; idle and over-provisioning signals.
- **Platform & commitments** — cloud/platform, existing reserved/committed-use or spot usage. Ask if unspecified.

## Constraints

**Must:**
- Quantify current spend by category before proposing cuts — no optimization without a baseline.
- Gate each lever on a quality floor (metric) and a latency SLA (p99) it must not violate.
- Rank levers by savings × safety, surfacing the cheap-and-safe wins first.

**Must Not:**
- Recommend a cut whose quality/latency impact is unknown without flagging the required test.
- Assume utilization is high; many GPU bills are dominated by idle/over-provisioned capacity — verify.
- Fabricate cost figures; if the breakdown is unknown, ask for it or mark estimates as estimates.

**Instructions:**

1. **Establish the cost baseline.** Break current spend into training, serving, storage, and data movement. Identify the dominant category — optimize where the money actually is.

2. **Measure utilization.** For training and serving, find GPU/CPU/memory utilization and idle time. Over-provisioning and idle capacity are usually the largest, safest savings.

3. **Set the guardrails.** State the quality floor (metric must stay ≥ X) and the latency SLA (p99 ≤ Y). Every lever is evaluated against these.

4. **Enumerate training levers.** Consider spot/preemptible instances with checkpointing, right-sizing instances, mixed precision, gradient accumulation, smaller/cheaper instances, reduced retrain frequency, and caching unchanged pipeline steps.

5. **Enumerate serving levers.** Consider autoscaling to demand (scale-to-zero where freshness allows), right-sizing instances, request batching, model compression (quantization/distillation/pruning), moving GPU→CPU where viable, and caching frequent predictions.

6. **Estimate savings and risk per lever.** For each, estimate the saving and classify the risk to quality/latency (none / needs-test / known-tradeoff). Distinguish free wins from quality-affecting changes.

7. **Rank and gate.** Order by savings × safety. For quality/latency-affecting levers, specify the exact test that must pass (eval on golden set within floor; load test at p99) before the cut is adopted.

8. **Plan monitoring.** Define cost and quality/latency monitoring after the change so a regression (or cost creep) is caught.

**Output Format:**

A markdown report:
- **Cost Baseline** — table: Category | Spend | % of total.
- **Utilization Findings** — training & serving idle/over-provisioning.
- **Guardrails** — quality floor + latency SLA.
- **Lever Inventory** — table: Lever | Est. saving | Risk | Gating test.
- **Ranked Recommendation** — ordered by savings × safety; free wins first.
- **Post-Change Monitoring** — cost + quality/latency signals.

## Verification

- [ ] A cost baseline by category exists and the dominant category is identified.
- [ ] Utilization/idle is measured, not assumed.
- [ ] A quality floor and a latency SLA are stated and applied to every lever.
- [ ] Each quality/latency-affecting lever names the test that must pass before adoption.
- [ ] Free/safe wins are separated from quality-affecting tradeoffs in the ranking.

## False-Positive Prevention

❌ **DON'T:**
- Recommend smaller instances or quantization without measuring the resulting quality/latency.
- Assume the GPU fleet is busy; bill it as utilized when much of it is idle.
- Quote a percentage saving without a baseline to apply it to.
- Treat scale-to-zero as free when cold-start would violate the latency SLA at the next request spike.

✅ **DO:**
- Start with idle/over-provisioning — usually the biggest saving with zero quality risk.
- Attach a concrete gating test (golden-set eval, p99 load test) to every quality/latency-affecting lever.
- Verify quantization/distillation keeps the metric above the floor before adopting it.
- Confirm spot/preemptible use is paired with checkpointing so interruptions don't waste a full run.

## Example Output

```markdown
## ML Infra Cost Optimization — Vision Pipeline (AWS, ~$42k/mo)

### Cost Baseline
| Category | Spend | % |
|---|---|---|
| Serving (GPU endpoints) | $24k | 57% |
| Training (on-demand A100) | $12k | 29% |
| Storage + data movement | $6k | 14% |

### Utilization Findings
- Serving GPUs at 22% avg utilization, never scale down off-peak. Training on-demand though jobs checkpoint.

### Guardrails
- Quality floor: mAP ≥ 0.81. Latency: p99 ≤ 120ms.

### Lever Inventory
| Lever | Est. saving | Risk | Gating test |
|---|---|---|---|
| Autoscale serving + scale-down off-peak | $9k/mo | none (freshness OK) | load test p99 at peak |
| Spot for training + existing checkpoints | $7k/mo | none | confirm checkpoint resume |
| INT8 quantize served model | $5k/mo | needs-test | mAP on golden set ≥ 0.81; p99 ≤ 120ms |
| Tier cold artifacts to cheaper storage | $3k/mo | none | n/a |

### Ranked Recommendation (savings × safety)
1. Spot training (free win, $7k). 2. Serving autoscale ($9k, load-test). 3. Storage tiering ($3k). 4. Quantization ($5k) ONLY if golden-set mAP holds.

### Post-Change Monitoring
- Daily cost by category; alert on >10% creep. Continuous mAP-on-canary and p99 dashboards.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** baseline → utilization → guardrails → levers → ranking.
- **RT-02 (Multi-Dimensional Analysis Framework):** levers weighed across saving, quality, latency, risk.
- **DS-06 (Prioritization & Severity Guidance):** levers ranked by savings × safety.
- **CM-02 (Constraint Specification):** quality floor and latency SLA bound every cut.
- **RT-05 (Evidence-Based Reasoning):** recommendations grounded in measured spend and utilization.

**Related Prompts:**
- `mlops_model_serving_architecture.md` — where serving-cost levers originate.
- `mlops_training_pipeline_orchestration.md` — caching/idempotency that reduces training cost.
- `domain-software-engineering/cloud/cloud_cost_optimization.md` — general cloud cost work.
