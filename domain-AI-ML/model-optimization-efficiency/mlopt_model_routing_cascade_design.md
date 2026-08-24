---
title: "Model Routing and Cascade Design"
category: AI-ML/model-optimization-efficiency
description: "Route requests across models of different cost — deciding whether difficulty can be judged before or only after inference, pricing the router's own cost and errors, and measuring end-to-end quality rather than the escalated-only subset."
techniques:
  - RT-10
  - DS-02
  - RT-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - model-routing
  - cascade
  - cost-optimization
  - difficulty-estimation
  - tiered-serving
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-optimization-efficiency/mlopt_llm_inference_serving_optimization.md
  - domain-AI-ML/model-evaluation-validation/mleval_selective_prediction_abstention.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_cost_latency_optimization.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_knowledge_distillation_plan.md
---

# Model Routing and Cascade Design

**Objective:** Serve most traffic with a cheap model and the rest with an expensive one without losing quality — deciding whether request difficulty can be judged *before* inference (routing) or only *after* (cascade), pricing the router itself, and evaluating the composed system rather than either model alone.

**When to Use:**
- A large model serves all traffic and much of it looks easy enough for something smaller.
- Cost or latency must fall and quality must not, so a single model swap is unacceptable.
- Quality varies sharply by request type and a single model is over-provisioned for the common case.

**When NOT to Use:**
- One model already meets both cost and quality targets — routing adds moving parts for nothing.
- The decision is when to defer to a human — use `../model-evaluation-validation/mleval_selective_prediction_abstention.md`.
- A distilled single model would meet the bar — use `mlopt_knowledge_distillation_plan.md`; one model is simpler to operate than three.

## Inputs / Context

- **Model tiers available** — quality, cost, and latency for each, measured on the same evaluation set.
- **Traffic difficulty distribution** — evidence that a meaningful fraction is genuinely easy.
- **Quality bar** — the end-to-end level the composed system must hold.
- **Latency budget** — including the worst path, where a request goes through both tiers.
- **Difficulty predictability** — whether difficulty is apparent from the input alone.
- **Cost ratio between tiers** — since a small ratio makes the whole exercise marginal.

## Constraints

**Must:**
- Distinguish **routing** (decide before inference from the input) from **cascade** (run cheap, then decide from its output whether to escalate). They have different latency profiles and different failure modes, and the choice follows from whether difficulty is visible in the input.
- Price the router itself — its inference cost, its latency, and the cost of its mistakes. A router that is nearly as expensive as the small model erases the saving.
- Report **end-to-end quality on all traffic**, never the escalated subset alone; the composed system's quality is what users get.
- Model the worst-case latency path: a cascade that escalates pays both models' latency plus the decision.
- State the cost saving **net of** router cost, escalation rate, and any quality loss expressed in its own units.

**Must Not:**
- Assert routing accuracy, cost savings, or escalation rates from memory; mark quantities `[measure on your traffic]`.
- Use the small model's own confidence as the cascade signal without validating it — small models are frequently confidently wrong, which is exactly the case that must escalate.
- Report only cost savings; a saving with unstated quality loss is not a result.
- Ignore that the traffic mix shifts, moving the escalation rate and the saving with it.
- Treat a cascade as strictly safe — an unescalated wrong answer from the cheap tier is a system error, not a cheap-tier error.

**Instructions:**

1. **Verify the difficulty spread.** Evaluate the cheap model on real traffic and measure what fraction it handles at the required quality. If that fraction is small, the saving is small and the complexity is not worth it — a legitimate stopping point.

2. **Decide routing versus cascade.** Can difficulty be judged from the input alone? Route — one model runs, latency is predictable. Only from the output? Cascade — the cheap model always runs, and escalated requests pay both. This decision is forced by the task; it is not a preference.

3. **Design the decision signal.**
   - *Routing:* a lightweight classifier or heuristic on input features — length, complexity, request type, user segment.
   - *Cascade:* the cheap model's confidence, an uncertainty estimate, a conformal set size, or an output-based verifier.
   Validate the signal against actual difficulty: does it identify the cases the cheap model gets wrong? An unvalidated signal is the design's central risk.

4. **Price the router.** Its own cost and latency, plus the cost of both error types: a hard request sent to the cheap tier (quality loss) and an easy request sent to the expensive tier (wasted cost). These are asymmetric and should be weighted accordingly.

5. **Set the threshold from the cost–quality trade.** Sweep it, and at each point record escalation rate, end-to-end quality, cost, and worst-case latency. Choose against the quality bar and the latency budget together, not against cost alone.

6. **Evaluate end to end.** The composed system on all traffic, per slice. A cascade can hold aggregate quality while degrading badly on a segment the cheap model handles poorly and the signal fails to flag — which is the specific failure this evaluation exists to catch.

7. **Model the latency profile.** p50 and p99 for routed, cheap-only, and escalated paths. Confirm the escalated path fits the budget, since that is the path a hard request takes and hard requests are often the ones users care most about.

8. **Plan for mix shift.** Traffic difficulty moves over time, changing escalation rate and cost. Monitor it and define what happens when the escalation rate drifts — a rising rate erodes the saving; a falling rate may mean the signal has stopped working.

9. **Design the failure behaviour.** What happens when the expensive tier is unavailable: serve the cheap answer with a marker, queue, or fail. This is a product decision.

**Output Format:**

A markdown design:
- **Difficulty Spread** — fraction of traffic the cheap tier handles at quality.
- **Routing vs Cascade** — the decision and what forced it.
- **Decision Signal** — mechanism and its validation against actual difficulty.
- **Router Cost** — inference cost, latency, and the two error costs.
- **Threshold Sweep** — table: Threshold | Escalation rate | End-to-end quality | Cost | Worst-case latency.
- **End-to-End Evaluation** — quality on all traffic, per slice.
- **Latency Profile** — p50/p99 per path.
- **Mix-Shift Monitoring** — signals and response.
- **Failure Behaviour** — when the expensive tier is unavailable.

## Verification

- [ ] The difficulty spread is measured, and a small spread is allowed to end the design.
- [ ] Routing versus cascade follows from whether difficulty is visible in the input.
- [ ] The decision signal is validated against cases the cheap model actually gets wrong.
- [ ] Router cost, latency, and both error costs are priced.
- [ ] The threshold sweep reports quality, cost, and latency together.
- [ ] End-to-end quality is reported on all traffic and per slice.
- [ ] The escalated path's latency is checked against the budget.
- [ ] Mix-shift monitoring and its response are defined.
- [ ] Failure behaviour for expensive-tier unavailability is specified.
- [ ] No savings or escalation figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Use the small model's raw confidence as the escalation signal without validating it — small models are confidently wrong precisely on the cases that must escalate, so the signal fails where it matters most.
- Report quality on escalated requests only; users experience the composed system, and the unescalated errors are invisible in that view.
- Quote a cost saving without netting off router cost and any quality loss — the gross number is not the result.
- Forget that a cascade's escalated path pays both models' latency; the hard requests take the slowest path.
- Assume the escalation rate is stable; traffic mix moves and the saving moves with it.
- Treat a cascade as risk-free because the expensive model is available — an unescalated wrong answer never reaches it.

✅ **DO:**
- Measure how much traffic the cheap tier genuinely handles before designing anything.
- Let the task decide routing versus cascade, based on whether difficulty is visible pre-inference.
- Validate the decision signal specifically against the cheap model's errors.
- Sweep the threshold and choose against quality, cost, and latency together.
- Evaluate end to end and per slice, and lead with the worst slice.
- Monitor escalation-rate drift in both directions and define the response to each.

## Example Output

```markdown
## Cascade Design: Document Classification Service
Large model serves all traffic. Cost is the constraint; quality must not fall.

### Difficulty Spread
Evaluate the small model on a representative traffic sample:
| Segment | Small-model quality | Meets bar? |
|---|---|---|
| Standard forms (est. majority of traffic) | `[measure]` | `[assess]` |
| Scanned/low-quality images | `[measure]` | `[assess]` |
| Multi-language documents | `[measure]` | `[assess]` |
| Novel document types | `[measure]` | `[assess]` |

If the small model clears the bar on only a small share, stop here: the saving will not repay
the complexity of operating two tiers plus a router.

### Routing vs Cascade — forced by the task
Difficulty is **partly** visible pre-inference: image quality and page count are observable;
content novelty is not. **Hybrid chosen** — route obviously-hard requests (low image quality,
unusual page count) straight to the large model, and cascade the remainder. Pure routing would
misclassify content-novel documents as easy; pure cascade would waste a cheap-model pass on
documents already known to be hard.

### Decision Signal
- **Pre-inference route:** heuristic on image quality metrics and page count. Cheap, deterministic.
- **Cascade escalation:** **not raw small-model confidence.** Validated instead against the
  cases the small model actually gets wrong `[measure]` — small models on out-of-distribution
  documents are confidently wrong, so raw confidence fails exactly where escalation is needed.
  Candidate signals to compare: calibrated confidence, conformal set size, and an OOD score on
  the document embedding.

### Router Cost
| Component | Cost | Latency |
|---|---|---|
| Pre-inference heuristic | negligible | <1 ms |
| Escalation signal | `[measure]` | `[measure]` |
| **Error: hard → cheap tier** | quality loss on a real document | — |
| **Error: easy → large tier** | wasted inference cost | — |

The two errors are asymmetric: a wrongly-cheap document is a customer-visible error; a
wrongly-expensive one costs money. The threshold is weighted toward escalation accordingly.

### Threshold Sweep
| Threshold | Escalation rate | End-to-end quality | Cost vs baseline | Worst-case latency |
|---|---|---|---|---|
| Conservative | `[measure]` | `[measure]` | `[measure]` | `[measure]` |
| Balanced | `[measure]` | `[measure]` | `[measure]` | `[measure]` |
| Aggressive | `[measure]` | `[measure]` | `[measure]` | `[measure]` |

Choose against the quality bar **and** the latency budget together — the cheapest point that
clears quality may still breach the escalated-path latency budget.

### End-to-End Evaluation
Quality on **all** traffic, per slice, for the composed system:
| Slice | Large model only | Cascade (composed) | Delta |
|---|---|---|---|
| Standard forms | `[measure]` | `[measure]` | — |
| Scanned/low-quality | `[measure]` | `[measure]` | — |
| **Multi-language** | `[measure]` | `[measure]` | **watch** |
| **Novel types** | `[measure]` | `[measure]` | **watch** |

The two watch slices are where the small model is weakest and the escalation signal is least
reliable — the exact combination that produces an unescalated wrong answer. Aggregate quality
can look unchanged while one of these degrades materially.

### Latency Profile
| Path | p50 | p99 |
|---|---|---|
| Routed direct to large | `[measure]` | `[measure]` |
| Cheap only | `[measure]` | `[measure]` |
| **Escalated (both models)** | `[measure]` | `[measure]` — **must fit budget** |

### Mix-Shift Monitoring
- Escalation rate, daily. **Rising** erodes the saving and may signal incoming novel document
  types. **Falling** may mean the escalation signal has degraded and hard documents are being
  served cheaply — the more dangerous direction, because it looks like an improvement.
- Per-slice quality on a sampled audit, weekly.

### Failure Behaviour
When the large model is unavailable: serve the cheap-tier answer **flagged as low-confidence**
and queue the document for reprocessing. Do not fail the request — a flagged provisional answer
is more useful than an error, and the flag makes the degradation visible rather than silent.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** difficulty visibility routes the design to routing, cascade, or hybrid.
- **DS-02 (Metric Specification):** end-to-end quality on all traffic is the defined measure, with escalation rate and worst-path latency alongside.
- **RT-02 (Multi-Dimensional Analysis Framework):** threshold × escalation rate × quality × cost × latency is the sweep grid.
- **CM-02 (Constraint Specification):** the net-of-router-cost and all-traffic-evaluation rules bound what may be claimed.
- **QA-12 (False Positives Identification):** rejects raw small-model confidence as an escalation signal and escalated-only quality reporting.

**Related Prompts:**
- `mlopt_llm_inference_serving_optimization.md` — optimizing each tier's serving.
- `mlopt_knowledge_distillation_plan.md` — the single-model alternative that avoids the routing complexity.
- `../model-evaluation-validation/mleval_selective_prediction_abstention.md` — the human-deferral analogue of the same decision.
- `../genai-llm-engineering/genai_llm_cost_latency_optimization.md` — model-choice and prompt-level cost levers.
