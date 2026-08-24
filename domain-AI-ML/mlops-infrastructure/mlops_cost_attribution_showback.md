---
title: "ML Cost Attribution & Showback"
category: AI-ML/mlops-infrastructure
description: "Attribute shared ML training, serving, storage, and data-pipeline spend back to teams, models, and products in a multi-tenant environment — tagging strategy, allocation of un-taggable shared cost, showback vs chargeback, and a per-model cost view built only from observed billing data."
techniques:
  - ST-02
  - DS-02
  - RT-05
  - NE-13
  - CM-02
difficulty: advanced
tags:
  - cost-attribution
  - showback
  - finops
  - tagging
  - multi-tenant
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_infra_cost_optimization.md
  - domain-AI-ML/ai-product-leadership/aipm_roi_business_case.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_serving_architecture.md
---

# ML Cost Attribution & Showback

**Objective:** Build a defensible cost-attribution model that maps shared ML spend — training, serving, storage, data pipelines — to the teams, models, and products that drive it, with an explicit, documented method for allocating cost that cannot be directly tagged.

**When to Use:**
- A shared ML platform's bill must be broken down per team/model/product for showback or chargeback.
- Leadership asks "what does each model actually cost us?" and no one can answer with evidence.
- Untagged or shared resources (clusters, feature stores, gateways) make naive per-resource billing impossible.

**When NOT to Use:**
- The goal is to *reduce* spend (rightsizing, spot, batching, quantization) — use `mlops_infra_cost_optimization.md`.
- You need a forward-looking cost forecast / unit-economics model — use `mlops_cost_budget_forecasting.md`.

## Inputs / Context

- **Billing data** — cloud/vendor cost export by service, with whatever tags/labels exist today.
- **Resource inventory** — clusters, GPUs, endpoints, storage, pipelines, gateways — and which are dedicated vs shared.
- **Tenancy map** — which teams/models/products use which resources, and any usage signals (GPU-hours, requests, tokens, rows).
- **Allocation question** — the unit of attribution: team, model, product, or all three.
- **Showback vs chargeback** — whether costs are informational or actually billed internally.
- **Tagging maturity** — current label coverage and gaps.

## Constraints

**Must:**
- Separate directly-attributable cost (dedicated, tagged) from shared cost requiring an allocation key.
- Define the allocation key for each shared resource (GPU-hours, request count, token volume, storage GB, row count) and justify it from usage.
- Produce a per-model (and per-team/product) cost view that reconciles to the total bill.
- State whether the output is showback (informational) or chargeback (internally billed) and the implications.
- Surface tagging gaps and the allocation method used to cover them.

**Must Not:**
- Invent cost figures, usage volumes, GPU-hours, or unit prices — every number must trace to the supplied billing/usage data; mark gaps `UNKNOWN — confirm from billing export`.
- Present an allocated estimate as a precise measured cost; label allocated portions as allocated.

**Instructions:**

1. **Inventory and tag-audit.** List resources, classify dedicated vs shared, and record current tag coverage and gaps.
2. **Pull direct costs.** Sum all directly-attributable (tagged, dedicated) spend per team/model/product.
3. **Choose allocation keys.** For each shared/un-taggable resource, pick a driver-based key (GPU-hours, requests, tokens, GB, rows) that reflects actual consumption; justify it.
4. **Allocate shared cost.** Distribute shared spend by the chosen keys; show the math so it's auditable.
5. **Reconcile.** Confirm direct + allocated equals the total bill (no leakage, no double-count).
6. **Build the per-model view.** Assemble the per-model/team/product breakdown with direct vs allocated split visible.
7. **Frame showback vs chargeback.** State the governance model and translate the cost view into terms a non-technical owner can act on.

**Output Format:**

A markdown attribution report: Resource & Tag Inventory · Direct Cost Table · Shared-Cost Allocation Keys (table with justification) · Per-Model/Team/Product Cost View (direct vs allocated) · Reconciliation Check · Showback/Chargeback Framing. Unknowns marked.

## Verification

- [ ] Dedicated/tagged cost is separated from shared cost.
- [ ] Each shared resource has an allocation key justified by usage data.
- [ ] Direct + allocated reconciles to the total bill with no leakage or double-count.
- [ ] The per-model view shows the direct-vs-allocated split.
- [ ] Showback vs chargeback is stated explicitly.
- [ ] Every number traces to supplied billing/usage data; gaps are UNKNOWN.

## False-Positive Prevention

❌ **DON'T:**
- Attribute a shared GPU cluster's full bill to the team with the most *jobs* — job count isn't consumption; a few long training runs can dwarf many short ones, so an unjustified key misallocates the largest line item.
- Present allocated cost as if it were metered ("Model X costs $4,200/mo") when most of it was apportioned by an estimate — that overstated precision drives bad budget decisions.
- Let untagged spend silently land in an "other/shared" bucket and ignore it — the unallocated remainder is often the biggest number and quietly defeats the whole exercise.
- Double-count a resource used by two products by charging each the full amount — allocation must split, not duplicate, or the per-model view won't reconcile to the bill.

✅ **DO:**
- Pick consumption-based allocation keys (GPU-hours, tokens, requests, GB) and justify each from observed usage.
- Label allocated portions as *allocated* and show the apportionment math so owners can audit it.
- Reconcile direct + allocated to the total and force the unallocated remainder toward zero with explicit keys.
- Split shared cost proportionally across all consumers so the breakdown sums to the actual bill.

## Example Output

```markdown
## ML Cost Attribution — June (showback)

### Resource & Tag Inventory
- Dedicated, tagged: fraud-train cluster (team=fraud). Coverage: 100%.
- Shared, untagged: inference gateway, feature store, shared A100 pool. Coverage gap: ~38% of spend.

### Direct Cost Table (from billing export)
| owner | direct cost |
|---|---|
| fraud (dedicated train cluster) | $X (from export) |
| recsys (dedicated endpoints) | $Y (from export) |

### Shared-Cost Allocation Keys
| shared resource | key | justification |
|---|---|---|
| shared A100 pool | GPU-hours per model | reflects actual compute consumed |
| inference gateway | request count | gateway cost scales with calls |
| feature store storage | storage GB per team | storage billed by volume held |

### Per-Model/Team/Product Cost View
| model | direct | allocated | total | note |
|---|---|---|---|---|
| fraud-scoring | $X | $A (GPU-hrs) | $X+$A | allocated portion = apportioned |
| recsys-ranker | $Y | $B (requests) | $Y+$B | |

### Reconciliation Check
- Direct + allocated = total bill (delta = 0). Unallocated remainder: UNKNOWN — confirm full tag coverage.

### Showback/Chargeback Framing
- Showback: distributed to teams monthly for visibility, not billed. In plain terms: "fraud-scoring drove ~N% of the shared GPU pool this month, mostly via long retraining runs."
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Sequences inventory → direct → keys → allocate → reconcile → frame.
- **DS-02 (Metric Specification):** Forces driver-based allocation keys (GPU-hours, tokens, requests, GB).
- **RT-05 (Evidence-Based Reasoning):** Ties every figure to the billing/usage export, not estimates.
- **NE-13 (Technical-to-Business Translation):** Frames the per-model cost view for non-technical owners.
- **CM-02 (Constraint Specification):** Encodes reconciliation and the no-fabrication clause.

**Related Prompts:**
- `mlops_infra_cost_optimization.md` — once costs are attributed, reduce the biggest line items.
- `aipm_roi_business_case.md` — feed per-model cost into the ROI/business case.
- `mlops_model_serving_architecture.md` — serving design choices that drive the costs being attributed.
