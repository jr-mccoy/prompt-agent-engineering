---
title: "Budget Variance Investigator — Budget-vs-Actual Variance Decomposition with Root-Cause Isolation"
category: finance/corporate-finance-fpa
description: "Decompose budget-vs-actual variances into price/volume/mix and rate/efficiency drivers, separate one-time from recurring causes, and produce a prioritized, evidence-based variance commentary."
techniques:
  - NE-11
  - DS-04
  - RT-05
  - DS-06
  - QA-04
difficulty: intermediate
tags:
  - variance-analysis
  - budget-vs-actual
  - fpa
  - price-volume-mix
  - root-cause
  - management-reporting
updated: "2026-06-08"
related_prompts:
  - domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md
  - domain-finance/corporate-finance-fpa/finance_board_finance_package_builder.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Investigate budget-vs-actual (or forecast-vs-actual) variances by decomposing each material variance into its mathematical drivers (price, volume, mix, rate, efficiency, FX, timing), isolating one-time from recurring root causes, and producing a prioritized variance commentary that distinguishes signal from noise and recommends whether each driver should change the forward forecast.

---

## When to Use

- Monthly/quarterly close — explaining why actuals differed from plan for management or the board.
- Mid-year reforecast prep — deciding which variances are structural (carry forward) vs one-time.
- Cost-center or P&L-owner reviews where line owners must defend variances.
- Diagnosing a missed quarter — separating demand misses from execution misses.
- **Do not use** to assign blame, to produce GAAP adjustments, or as a substitute for operational/system-level root-cause investigation; this isolates financial drivers and frames the questions for operators.

---

## Inputs / Context Required

```
<variance_inputs>
Entity / cost center / P&L:
Period: [month / quarter / YTD]
Comparison basis: Budget | Prior forecast | Prior year
Currency:

DATA (paste; budget and actual at line level — the more granular, the better):
- P&L by line: Budget vs Actual (revenue, COGS lines, opex lines)
- For revenue: units/volume and price by product/segment (budget vs actual) if available
- For COGS: input cost rates and quantities if available
- Headcount budget vs actual (for comp variances)
- FX rates assumed in budget vs actual (if multi-currency)
- Known one-time items (settlements, true-ups, accruals, catch-ups)

CONTEXT:
- Materiality threshold (e.g., flag variances > $X or > Y%)
- Any reorganizations, reclassifications, or accounting changes in the period
- Seasonality pattern
</variance_inputs>
```

---

## Constraints

### Must
- Compute each material variance as **$ and %**, and flag against the stated materiality threshold (DS-06).
- Decompose revenue variances using **price / volume / mix** where the data supports it:
  ```
  Volume variance = (Actual Qty − Budget Qty) × Budget Price
  Price variance   = (Actual Price − Budget Price) × Actual Qty
  Mix variance     = Σ[(Actual mix% − Budget mix%) × (Budget unit margin − Avg budget unit margin)] × Total actual qty
  ```
- Decompose cost variances into **rate (price of input) vs efficiency/usage (quantity of input)**:
  ```
  Rate variance       = (Actual rate − Budget rate) × Actual quantity
  Efficiency variance = (Actual quantity − Budget quantity) × Budget rate
  ```
- Classify each root cause as **one-time vs recurring** using a stated test (e.g., will it repeat next period? did it appear before?), and state the forward-forecast implication.
- Separate **timing** variances (phasing — will reverse) from **permanent** variances (will not).
- Distinguish a **favorable variance that is actually bad** (e.g., under-spend on a growth investment) and an **unfavorable variance that is actually fine** (e.g., revenue-driven variable cost increase).
- Require evidence (RT-05) for each attributed cause; mark unsupported attributions as hypotheses to confirm.
- State confidence (High/Med/Low) and acknowledge what cannot be explained from the data (QA-04).

### Must Not
- Sum price, volume, and mix variances that do not reconcile to the total revenue variance (force a tie-out).
- Attribute a variance to a cause without evidence or a clearly labeled hypothesis flag.
- Treat every favorable variance as good or every unfavorable variance as bad.
- Invent volume, price, or rate detail not supplied (decompose only to the granularity the data allows).
- Carry a one-time item into the forward forecast.

---

## Instructions

1. **Rank by materiality (DS-06).** Compute $ and % variance for every line; sort descending by absolute $ impact; apply the materiality threshold. Focus effort on the vital few.

2. **Reconcile the bridge (NE-11).** Build a budget→actual bridge so all drivers sum to the total variance:
   ```
   Budget [metric] + Σ(driver variances) = Actual [metric]   (must reconcile)
   ```

3. **Decompose revenue (price/volume/mix).** Where unit data exists, split volume, price, and mix; confirm the three sum to the total revenue variance. Where only $ is available, say so and stop at the line level.

4. **Decompose costs (rate/efficiency).** Split variable cost variances into rate (input price) and efficiency (input usage). For fixed costs, identify whether the variance is spend (more/less spent) or timing (phasing).

5. **Classify each driver (DS-04 — pattern recognition).**
   ```
   For each driver, tag:
     - Recurring | One-time
     - Permanent | Timing (will reverse)
     - Controllable | Non-controllable (FX, market price)
     - Good | Bad direction (independent of favorable/unfavorable sign)
   ```

6. **Apply the recurrence test.** Did this item appear in prior periods? Is the underlying cause structural? If yes → recurring → adjust forward forecast. If genuinely one-time → exclude from run-rate.

7. **Evidence and hypotheses (RT-05).** For each cause, cite the supporting data point. Where the cause is inferred, label it a hypothesis and state the operational question that would confirm it (e.g., "Confirm with sales ops whether the Q3 unit shortfall was a pushed deal or a lost deal").

8. **Verification (QA-01).** Confirm all decomposition components tie to the total. Confirm one-time items are excluded from the implied run-rate. State the residual unexplained variance, if any.

---

## Output Format

```
## Budget Variance Investigation — [Entity], [Period]
Basis: [Budget vs Actual] | Currency: [USD] | Materiality: > $[x] or [y]%
NOTE: figures below are ILLUSTRATIVE.

### Variance Summary (ranked by $ impact)
| Line          | Budget | Actual | Var $ | Var % | F/U | Material? |
|---------------|--------|--------|-------|-------|-----|-----------|
| Revenue       | 1,000  | 940    | (60)  | (6%)  | U   | Yes       |
| COGS          | (450)  | (440)  | 10    | 2%    | F   | Yes       |
| S&M           | (180)  | (205)  | (25)  | (14%) | U   | Yes       |
| G&A           | (90)   | (88)   | 2     | 2%    | F   | No        |

### Revenue Bridge (price/volume/mix — illustrative)
| Driver           | $ impact | Note |
|------------------|----------|------|
| Budget revenue   | 1,000    |      |
| Volume variance  | (75)     | 5% fewer units than plan |
| Price variance   | +20      | realized price above plan |
| Mix variance     | (5)      | shift to lower-margin SKU |
| Actual revenue   | 940      | ties ✓ |

### Cost Variance (rate/efficiency — illustrative)
| Line | Rate var | Efficiency var | Timing | Total | Recurring? |
|------|----------|----------------|--------|-------|------------|
| COGS | +6 (cheaper input) | +4 (better yield) | 0 | +10 F | Recurring |
| S&M  | 0 | (10) overspend | (15) pulled-forward campaign | (25) U | (15) one-time, (10) recurring |

### Root-Cause Classification
| Driver | One-time/Recurring | Timing/Permanent | Good/Bad | Forecast action | Confidence |
|--------|--------------------|--------------------|----------|-----------------|------------|
| Volume shortfall | Recurring | Permanent | Bad | Lower fwd revenue | Med |
| Price realization | Recurring | Permanent | Good | Keep in fwd | High |
| S&M campaign pull-forward | One-time | Timing | Neutral | Exclude from run-rate | High |
| Input cost decline | Recurring | Permanent (verify) | Good | Keep, but monitor | Med |

### Implied Run-Rate (one-times stripped)
Reported actual EBIT variance: $([x]) U
Less one-time timing items: +$[x]
= Underlying run-rate variance: $([x]) U

### Open Questions for Operators
- [Hypothesis] Volume shortfall: pushed deals or lost deals? Confirm with sales ops.
- [Hypothesis] Input cost decline: durable supplier renegotiation or spot-price luck?

Unexplained residual: $[x] ([y]% of total) — pending data.
```

---

## Verification

- [ ] Every material variance computed in $ and % and flagged vs the threshold.
- [ ] Price/volume/mix decomposition sums to the total revenue variance.
- [ ] Rate/efficiency decomposition sums to the total cost variance.
- [ ] Each driver tagged one-time/recurring and timing/permanent.
- [ ] One-time items excluded from the implied run-rate.
- [ ] Favorable-but-bad and unfavorable-but-fine cases identified.
- [ ] Each attributed cause cites evidence or is flagged as a hypothesis.
- [ ] Residual unexplained variance disclosed.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Decomposition that doesn't reconcile to the total | Force price+volume+mix (and rate+efficiency) to tie to the total variance; show the tie-out |
| Treating a favorable variance as automatically good | Tag good/bad direction independently of F/U sign (e.g., under-spent growth investment is favorable but bad) |
| Carrying a one-time item into the forecast | Apply the recurrence test; strip one-times from the implied run-rate |
| Attributing causes without evidence | Require a data citation or an explicit hypothesis flag plus the question to confirm it |
| Over-decomposing beyond the data | Decompose only to the granularity the supplied data supports; otherwise stop at the line and say so |
| Confusing timing with permanent misses | Separate phasing (will reverse) from structural variances explicitly |
