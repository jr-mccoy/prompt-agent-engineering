---
title: "RAI Sustainability & Carbon Assessment"
category: AI-ML/responsible-ai-governance
description: "Estimate and reduce the compute and carbon footprint of training and serving an ML system using measured inputs and stated assumptions, never invented energy or emissions figures."
techniques:
  - ST-02
  - DS-02
  - RT-05
  - QA-12
  - DS-06
difficulty: intermediate
tags:
  - sustainability
  - carbon-footprint
  - compute-efficiency
  - inference-cost
  - responsible-ai
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_inference_latency_optimization.md
  - domain-AI-ML/responsible-ai-governance/rai_model_card_authoring.md
---

# RAI Sustainability & Carbon Assessment

**Objective:** Estimate the energy and carbon footprint of training and serving an ML system from measured or user-supplied inputs, identify where the footprint concentrates (often serving, not training), and recommend reductions ranked by impact vs effort — with every figure traceable to an input or a clearly stated assumption, never invented.

**When to Use:**
- When assessing the environmental cost of a model, especially large or high-traffic ones.
- To decide whether efficiency work (smaller model, quantization, batching) is worth it.
- To report footprint in a model card or sustainability disclosure.

**When NOT to Use:**
- As a precise certified carbon accounting deliverable — this is an engineering estimate; route formal accounting to specialists.
- For pure latency/cost optimization without an environmental lens — use `mlopt_inference_latency_optimization.md`.

## Inputs / Context

- **Training profile** — hardware type/count, training wall-clock hours, number of runs/experiments, region (grid carbon intensity).
- **Serving profile** — requests/day, compute per request, hardware, utilization, region — and the expected service lifetime.
- **Measured energy** — power draw or utility/cloud energy reports if available (preferred over estimates).
- **Grid carbon intensity** — for the region(s), if known (ask the user; do not assume a global default).
- **Reduction levers available** — model size choices, quantization/distillation, batching, caching, scheduling, region choice.

## Constraints

**Must:**
- Base every estimate on a measured input or an explicitly stated assumption, and show the calculation path.
- Assess BOTH training and serving, and identify which dominates over the service lifetime (serving often dominates).
- Rank reduction levers by estimated impact vs effort, and state the accuracy/quality tradeoff of each.

**Must Not:**
- Invent energy-per-GPU-hour, grid carbon-intensity figures, or model-specific emissions numbers from memory — require user input or mark as an assumption with a placeholder to fill.
- Report a single point estimate without an uncertainty range when inputs are estimated.
- Claim a reduction "halves carbon" without showing the calculation and its assumptions.

**Instructions:**

1. **Gather and label inputs.** Collect training and serving profiles; mark each value as measured vs estimated vs missing. Request grid carbon intensity rather than assuming one.

2. **Estimate training footprint.** Compute energy from hardware × hours × utilization (and run count, including failed/experiment runs), then carbon via the stated grid intensity. Show the path; give a range.

3. **Estimate serving footprint over lifetime.** Compute per-request energy × volume × service lifetime, then carbon. This is frequently the larger term — make the comparison explicit.

4. **Identify the dominant contributor.** State whether training or serving dominates over the lifetime, since it changes where reduction effort should go.

5. **Enumerate reduction levers.** For each (smaller/distilled model, quantization, batching, caching, autoscaling, lower-carbon region/scheduling), estimate the footprint reduction and the accuracy/latency tradeoff.

6. **Rank levers by impact vs effort.** Prioritize high-impact, low-tradeoff reductions; flag those that degrade quality unacceptably.

7. **State uncertainty and what would tighten it.** Give ranges, name the most sensitive assumptions, and what measurement would reduce uncertainty.

8. **Recommend reporting.** Suggest what to record (with assumptions) in the model card or disclosure.

**Output Format:**

A markdown assessment:
- **Inputs & Provenance** — table: Value | Measured/Estimated/Missing | Source.
- **Training Footprint** — calculation path + range.
- **Serving Footprint (lifetime)** — calculation path + range.
- **Dominant Contributor** — training vs serving, with reasoning.
- **Reduction Levers** — table: Lever | Est. reduction | Tradeoff | Effort.
- **Ranked Recommendations**.
- **Uncertainty & Measurement Needs**.
- **INSUFFICIENT EVIDENCE** — the correct output when the inputs table is dominated by Missing. A footprint range assembled from defaults for hardware draw, PUE, and grid intensity has an uncertainty wider than the decisions it would inform. Name the unblocking datum: measured energy for a representative run, and the grid carbon intensity for the actual region and period.

## Verification

- [ ] Every figure is measured or a labeled assumption with a shown calculation.
- [ ] Both training and serving are estimated; the dominant one is identified.
- [ ] Grid carbon intensity is user-supplied, not assumed.
- [ ] Estimates carry ranges; sensitive assumptions are named.
- [ ] Each reduction lever states its accuracy/latency tradeoff.
- [ ] No emissions/energy figures are invented from memory.
- [ ] Where the dominant inputs are Missing, the assessment returns INSUFFICIENT EVIDENCE with measured energy and regional grid intensity named — a range is not manufactured from defaults.

## False-Positive Prevention

❌ **DON'T:**
- Quote a specific kgCO2 figure for a model from memory.
- Assume a global-average grid intensity when the deployment region's is knowable.
- Optimize training carbon while ignoring that serving dominates over the model's life.
- Claim a quantization saves 50% energy without showing the basis or the accuracy cost.

✅ **DO:**
- Derive figures from user inputs and show the math; give ranges.
- Ask for the region's grid intensity.
- Compare training vs lifetime serving before prioritizing.
- Pair each reduction estimate with its quality tradeoff.

## Example Output

```markdown
## Sustainability Assessment: Product-Search Ranking Model

### Inputs & Provenance
| Value | Status | Source |
|---|---|---|
| Training: 8×A100, 60h, 12 runs | Measured | MLflow logs |
| Serving: 40M req/day, 3ms GPU/req | Measured | Prod telemetry |
| Service lifetime | Estimate | 18 months (assumption) |
| Grid intensity | MISSING | NEEDS user input (region) |

### Training Footprint
8 GPUs × 60h × 12 runs × [GPU power, user to supply] × PUE → energy; × [grid intensity] → carbon. Range pending two missing inputs.

### Serving Footprint (lifetime)
40M/day × 3ms × 540 days × [GPU power] → energy; × [grid intensity]. Note: at this volume, lifetime serving energy likely exceeds total training energy by a large multiple — confirm once power figures supplied.

### Dominant Contributor
Provisionally SERVING dominates (high sustained volume vs one-off training). Reduction effort should target inference.

### Reduction Levers
| Lever | Est. reduction | Tradeoff | Effort |
|---|---|---|---|
| INT8 quantization | ~30–40% serving energy (to verify) | small NDCG drop | Low |
| Request batching | ~15–25% | +latency | Low |
| Cache hot queries | ~10–20% | staleness | Medium |
| Lower-carbon region | varies | data residency | Medium |

### Ranked Recommendations
1. Quantization (high impact, low effort) — validate accuracy first.
2. Batching where latency budget allows.

### Uncertainty & Measurement Needs
Most sensitive: GPU power draw and grid intensity (both missing). Measure actual power and obtain regional intensity to tighten the estimate.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** inputs → training → serving → dominant → levers → rank.
- **DS-02 (Metric Specification):** defines the energy/carbon calculation paths.
- **RT-05 (Evidence-Based Reasoning):** every figure tied to a measured input or labeled assumption.
- **QA-12 (False Positives Identification):** blocks invented emissions figures and assumed grid intensity.
- **DS-06 (Prioritization & Severity Guidance):** ranks reduction levers by impact vs effort.

**Related Prompts:**
- `mlopt_inference_latency_optimization.md` — engineering levers to reduce serving footprint.
- `rai_model_risk_assessment.md` — environmental cost as a governance consideration.
- `rai_model_card_authoring.md` — record the footprint estimate and assumptions.
