---
title: "Build vs Buy vs Fine-Tune Decision"
category: AI-ML/problem-framing-scoping
description: "Decide between building a custom model, buying a managed API, or fine-tuning an open-source model — from a practitioner and engineering view, with a weighted decision matrix and total-cost reasoning."
techniques:
  - ST-01
  - RT-02
  - DS-06
  - CM-02
  - RP-02
difficulty: advanced
tags:
  - build-vs-buy
  - fine-tuning
  - decision-matrix
  - cost-of-ownership
  - problem-framing
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/problem-framing-scoping/mlframe_is_this_an_ml_problem.md
  - domain-AI-ML/problem-framing-scoping/mlframe_feasibility_risk_assessment.md
  - domain-AI-ML/problem-framing-scoping/mlframe_data_readiness_assessment.md
---

# Build vs Buy vs Fine-Tune Decision

**Objective:** Evaluate, on weighted criteria, whether to build a custom model from scratch, buy a managed/hosted API, or fine-tune an open-source model — producing a recommendation backed by a decision matrix and a total-cost-of-ownership view, not a one-axis price comparison.

**When to Use:**
- ML is confirmed warranted and the question is how to source the capability.
- A managed API would work but data sensitivity, cost-at-scale, or control are concerns.
- A team is debating "just use the API" versus "fine-tune our own."

**When NOT to Use:**
- You haven't confirmed ML is the right approach (use `mlframe_is_this_an_ml_problem.md`).
- The choice is purely a model-architecture question within "build" — out of scope here.

## Inputs / Context

Provide what you can:
- **The capability needed** and required quality bar.
- **Data** — volume, sensitivity (PII/regulated), whether you can legally send it to a third party.
- **Scale** — request volume now and projected; latency requirements.
- **Team capability** — ML/MLOps skills and headcount available.
- **Control needs** — customization, IP ownership, on-prem/data-residency, vendor lock-in tolerance.
- **Budget & timeline** — what you can spend (build + run) and how soon you need it.

## Constraints

**Must:**
- Score all three options against the same weighted criteria (quality, time-to-value, total cost, control/lock-in, data/privacy fit, maintenance burden, scalability).
- Use total cost of ownership (build, run, monitor, retrain, on-call, vendor fees over time), not just upfront or per-call price.
- State the conditions under which the recommendation would flip (e.g., volume crossover, data-residency requirement).

**Must Not:**
- Invent vendor prices, latency numbers, or accuracy figures — mark them as inputs to obtain.
- Recommend fine-tuning without confirming sufficient, legally-usable, representative data exists.
- Treat "build" as always-best for control or "buy" as always-cheapest without the TCO crossover.

**Instructions:**

1. **Define the bar and the constraints.** Pin the required quality, latency, scale, data-sensitivity, and control requirements. These set which options are even admissible (e.g., data that can't leave the org rules out many APIs).

2. **Establish the weighted criteria.** Choose and weight criteria for *this* decision (a regulated, high-volume use weights control/cost; a quick experiment weights time-to-value).

3. **Assess BUY (managed API).** Time-to-value, quality on your task (to test, not assume), per-call cost at projected volume, lock-in, and data-handling fit. Note the volume at which per-call cost dominates.

4. **Assess FINE-TUNE (OSS).** Whether you have enough representative, legally-usable data; the infra/MLOps to host and serve; the maintenance burden; and the control/cost benefits at scale.

5. **Assess BUILD (custom).** Only when the task is genuinely bespoke and APIs/OSS don't fit. Account for the full lifecycle cost and the team capability required.

6. **Compute TCO and crossover.** Project total cost for each over a realistic horizon and identify crossover points (e.g., API cheaper below X req/day, self-host cheaper above).

7. **Score the matrix and recommend.** Fill the weighted matrix, give the recommendation, and list the flip conditions and the inputs still needed to firm up the call.

**Output Format:**

A markdown decision brief:
- **Requirements & Admissibility** — which options are even viable and why.
- **Decision Matrix** — table: Criterion | Weight | Build | Buy | Fine-Tune (scored).
- **TCO & Crossover** — cost trajectory and the volume/condition crossover points.
- **Recommendation** — verdict + rationale.
- **Flip Conditions** — what would change it.
- **Inputs to Obtain** — prices/latency/quality numbers still needed.

## Verification

- [ ] All three options scored on the same weighted criteria.
- [ ] Data sensitivity/legality is checked against each option's admissibility.
- [ ] TCO (not just upfront/per-call) is computed with a crossover point.
- [ ] Fine-tune is only recommended where sufficient legal data is confirmed.
- [ ] Flip conditions are explicit.
- [ ] No vendor price/latency/accuracy is asserted as fact; unknowns are listed to obtain.

## False-Positive Prevention

❌ **DON'T:**
- Pick "buy" on per-call price without projecting total cost at scale — APIs can be cheap at low volume and ruinous at high volume.
- Recommend fine-tuning when the available data is too small, biased, or legally un-sendable to the base model's provider.
- Assume an API meets the quality bar without a spot evaluation on your actual task.
- Treat "build for control" as free — custom carries the largest lifetime maintenance and on-call cost.

✅ **DO:**
- Compute the volume crossover where self-hosting/fine-tuning beats per-call pricing.
- Verify data legality and residency before any option that sends data off-prem.
- Spot-test the candidate API/OSS model on representative inputs before scoring quality.
- Weight maintenance and MLOps capability honestly — a team that can't run model serving shouldn't self-host.

## Example Output

```markdown
## Build/Buy/Fine-Tune: Internal Document Classification (regulated docs)

### Requirements & Admissibility
Quality bar: high (compliance-sensitive). Data: cannot leave the corporate VPC (regulated).
→ Public managed APIs that require sending raw docs out are INADMISSIBLE unless a private/VPC
deployment exists. BUY only viable as a private-deployment vendor.

### Decision Matrix (1–5, weighted)
| Criterion | Weight | Build | Buy (private) | Fine-Tune OSS |
|---|---|---|---|---|
| Quality on task | 0.25 | 4 | 4 | 4 |
| Time-to-value | 0.15 | 2 | 4 | 3 |
| TCO at projected volume | 0.20 | 2 | 3 | 4 |
| Control / data residency | 0.20 | 5 | 3 | 5 |
| Maintenance burden | 0.10 | 2 | 4 | 3 |
| Scalability | 0.10 | 4 | 4 | 4 |
| Weighted score | | 3.05 | 3.55 | 3.95 |

### TCO & Crossover
At ~50k docs/day, fine-tuned OSS self-hosted is cheaper than private-API per-doc pricing past
~month 6 (illustrative; vendor quote needed). Below ~5k docs/day, BUY likely wins on TCO.

### Recommendation
Fine-tune an OSS classifier hosted in-VPC: meets residency, best TCO at projected volume, and
the team has MLOps capacity. Pilot a private-API BUY in parallel as a 4-week fallback.

### Flip Conditions
- If a labeled-data shortfall emerges → lean BUY (private) while collecting labels.
- If volume stays < 5k/day for 12 months → BUY is cheaper; stop self-hosting.

### Inputs to Obtain
Private-vendor per-doc quote; OSS model quality on a 500-doc labeled sample; serving infra cost.
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** drives to a single sourcing recommendation.
- **RT-02 (Multi-Dimensional Analysis Framework):** the weighted matrix is the core mechanism.
- **DS-06 (Prioritization & Severity Guidance):** criterion weights encode what matters most here.
- **CM-02 (Constraint Specification):** data residency/legality act as hard admissibility constraints.
- **RP-02 (Audience-Specific Framing):** TCO framing serves both eng and budget owners.

**Related Prompts:**
- `mlframe_is_this_an_ml_problem.md` — confirm ML is warranted before sourcing it.
- `mlframe_feasibility_risk_assessment.md` — surface execution risks for the chosen path.
- `mlframe_data_readiness_assessment.md` — confirm data suffices before choosing fine-tune.
