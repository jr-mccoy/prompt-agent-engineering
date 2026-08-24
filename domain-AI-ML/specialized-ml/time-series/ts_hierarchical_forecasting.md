---
title: "Hierarchical & Grouped Forecasting"
category: AI-ML/specialized-ml/time-series
description: "Forecast across an aggregation hierarchy (e.g. SKU → category → region → total) and reconcile the levels into a coherent set, choosing among bottom-up, top-down, middle-out, and optimal (MinT) reconciliation based on where the signal lives in the structure."
techniques:
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - time-series
  - forecasting
  - hierarchical
  - reconciliation
  - coherence
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/time-series/ts_forecasting_model_selection.md
  - domain-AI-ML/specialized-ml/time-series/ts_backtesting_design.md
  - domain-AI-ML/specialized-ml/time-series/ts_probabilistic_forecasting.md
---

# Hierarchical & Grouped Forecasting

**Objective:** Recommend how to forecast a collection of related series organized in an aggregation hierarchy or cross-product of groupings, and how to reconcile those forecasts so they are *coherent* — child forecasts sum exactly to their parents at every level. The recommendation must identify the structure (strict hierarchy vs grouped/cross-sectional), locate where the signal is strongest (leaf vs aggregate), choose a reconciliation method matched to that diagnosis, and defer the final empirical choice to rolling-origin backtesting at every level of interest.

**When to Use:**
- You forecast many series that aggregate (products roll up to categories, stores to regions, regions to a national total).
- Stakeholders consume forecasts at multiple levels and need them to agree (the sum of store forecasts must equal the regional forecast).
- You suspect aggregate series are smoother/more predictable than noisy leaf series and want to borrow strength across levels.

**When NOT to Use:**
- You forecast a single series with no aggregation structure — use `ts_forecasting_model_selection.md`.
- Leaf series are dominated by zeros/sporadic demand — handle the leaf method first via `ts_intermittent_demand_forecasting.md`, then reconcile.
- You only need calibrated uncertainty for one series — see `ts_probabilistic_forecasting.md`.

## Inputs / Context

Provide what you can:
- **Hierarchy definition** — the levels and how they nest (strict tree vs grouped/cross-product of attributes such as product × geography).
- **Series count per level** — how many leaves, intermediate nodes, and the single (or few) top aggregates.
- **Signal location** — which levels look stable vs noisy; intermittency or sparsity at the leaf.
- **Consumption levels** — which level(s) decisions are actually made at.
- **Data volume & history length** per level.
- **Forecast horizon** and frequency.
- **Coherence requirement** — hard (must sum exactly) vs soft (approximate is acceptable).

## Constraints

**Must:**
- Establish a naive baseline (e.g. seasonal-naive) at every level and require any approach to beat it level by level.
- State the hierarchy/grouping structure explicitly and confirm forecasts are coherent after reconciliation.
- Evaluate accuracy at each level of interest, not just the top or bottom.
- Defer the bottom-up-vs-reconciliation decision to rolling-origin backtesting across levels.

**Must Not:**
- Fabricate accuracy numbers or quote reconciliation-method win rates from memory; reason from the user's structure and mark unknowns as "measure on your data."
- Assume bottom-up is universally best — noisy leaves can poison aggregates.
- Ship a recommendation whose child forecasts do not sum to their parents.
- Reconcile point forecasts and silently imply the intervals are coherent too.

**Instructions:**

1. **Characterize the structure.** Determine whether it is a strict hierarchy (single parent per node) or a grouped/cross-sectional structure (a node belongs to multiple aggregation paths). State the summing matrix conceptually: which leaves compose which aggregates.
2. **Locate the signal.** For each level, note whether the series is smooth and seasonal (aggregate) or noisy/intermittent (leaf). Signal location drives method choice more than fashion.
3. **List candidate reconciliation methods.** Bottom-up (forecast leaves, sum up), top-down (forecast the total, disaggregate by proportions — historical or forecast-proportion), middle-out (forecast a chosen middle level, then go up and down), and optimal reconciliation (MinT / trace minimization that combines base forecasts from all levels using their error covariance).
4. **Match method to diagnosis.** Bottom-up when leaves carry real signal; top-down when only the aggregate is reliable and shares are stable; middle-out when a meaningful intermediate level is the sweet spot; MinT when you have base forecasts at all levels and want a statistically coherent combination.
5. **Choose the base forecasting model per level.** Reconciliation sits on top of base forecasts — pick the per-level model via `ts_forecasting_model_selection.md` before reconciling.
6. **Design the backtest.** Use rolling-origin evaluation and report accuracy at each level of interest, plus a coherence check confirming sums hold post-reconciliation.
7. **Decide and document.** Recommend a primary method with a fallback, the levels to evaluate, and the metric per level. Mark all empirical claims as to-be-measured.

**Output Format:**

A markdown recommendation:
- **Structure Summary** — hierarchy/grouping, levels, series counts, summing relationships.
- **Signal Diagnosis** — where the predictable signal lives, per level.
- **Candidate Methods** — table of bottom-up / top-down / middle-out / MinT with fit notes.
- **Recommendation** — primary method + fallback, base model per level.
- **Coherence Plan** — how coherence is enforced and verified.
- **Backtest & Metrics** — rolling-origin design and per-level metrics.
- **Open Questions / Data to Gather** — unknowns to resolve before committing.

## Verification

- [ ] Hierarchy/grouping structure is stated explicitly with summing relationships.
- [ ] A naive baseline is set at every level of interest.
- [ ] Coherence is explicitly enforced and verified (children sum to parents).
- [ ] Accuracy is evaluated at each consumption level, not only top or bottom.
- [ ] No fabricated accuracy or reconciliation-win-rate numbers — empirical claims marked "measure on your data."

## False-Positive Prevention

❌ **DON'T:**
- Ship incoherent forecasts where child series do not sum to their parents and call the set "hierarchical."
- Assume bottom-up is always best — summing many noisy leaves can produce a worse aggregate than modeling the aggregate directly.
- Use historical proportions for top-down disaggregation when shares are drifting over time.
- Judge the system only at the top level while leaf-level decisions silently degrade.

✅ **DO:**
- Treat **incoherence** (children not summing to parents) as a hard failure and verify the summing constraint after reconciliation.
- Diagnose signal location and let it — not convention — drive bottom-up vs top-down vs MinT.
- Prefer optimal reconciliation (MinT) when you have credible base forecasts at multiple levels and want a principled combination.
- Backtest and report accuracy at every level decisions are actually made.

## Example Output

```markdown
## Structure Summary
- Grouped structure: Product (1,800 SKUs) × Region (12) rolling up to Category (40) and National total.
- Leaves: SKU×Region (≈14k series). Many SKU×Region cells are sparse.

### Signal Diagnosis
| Level | Character | Predictability |
|-------|-----------|----------------|
| National | smooth, strong yearly seasonality | high |
| Category | seasonal, moderate noise | medium |
| SKU×Region (leaf) | noisy, many zeros | low |

### Candidate Methods
| Method | Fit for this case |
|--------|-------------------|
| Bottom-up | risky — noisy leaves degrade aggregate |
| Top-down (forecast proportions) | shares drift; historical shares unsafe |
| Middle-out (Category) | promising — Category is reliable |
| MinT (optimal) | strong — combines all levels by error covariance |

### Recommendation
- Primary: MinT reconciliation over base forecasts at all levels.
- Fallback: Middle-out from Category.
- Base model per level via ts_forecasting_model_selection.md.

### Coherence Plan
- Apply summing matrix post-reconciliation; assert sum(children) == parent at every node.

### Backtest & Metrics
- Rolling-origin, 6 origins, horizon = 13 weeks.
- Metrics: MASE per level (National, Category, SKU×Region). Numbers TBD — measure on your data.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** orders the work from structure characterization → signal diagnosis → method match → reconciliation → backtest.
- **RT-02 (Multi-Dimensional Analysis Framework):** casts the model as a hierarchical-forecasting specialist reasoning about coherence and signal location.
- **DS-01 (Framework Application):** the candidate-methods table forces an explicit, criteria-based reconciliation choice.
- **CM-02 (Constraint Specification):** Must/Must Not block pins coherence and anti-fabrication as hard constraints.
- **DS-06 (Prioritization & Severity Guidance):** routes the final method pick to rolling-origin backtesting instead of asserting a winner.

**Related Prompts:**
- `ts_forecasting_model_selection.md` — picks the base model per level before reconciliation.
- `ts_backtesting_design.md` — designs the rolling-origin evaluation used to compare reconciliation methods.
- `ts_probabilistic_forecasting.md` — extends coherence to distributional forecasts, not just points.
