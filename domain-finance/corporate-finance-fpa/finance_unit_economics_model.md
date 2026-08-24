---
title: "Unit Economics Model — Contribution Margin, CAC Payback, Cohort Retention, and LTV/CAC"
category: finance/corporate-finance-fpa
description: "Build or critique unit economics: contribution margin per unit/customer, CAC and CAC payback, cohort retention curves, LTV, and the LTV/CAC ratio — with honest accounting for blended-vs-paid CAC and survivorship."
techniques:
  - NE-11
  - DS-02
  - NE-10
  - QA-02
  - DS-04
difficulty: intermediate
tags:
  - unit-economics
  - ltv-cac
  - contribution-margin
  - cohort-analysis
  - cac-payback
  - retention
updated: "2026-06-08"
related_prompts:
  - domain-finance/corporate-finance-fpa/finance_breakeven_operating_leverage.md
  - domain-finance/corporate-finance-fpa/finance_driver_based_scenario_model.md
  - domain-finance/corporate-finance-fpa/finance_cost_structure_optimization.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Build or critique a unit-economics model that establishes whether each unit/customer is profitable and how fast acquisition costs are recovered — computing contribution margin, CAC and CAC payback, cohort retention curves, lifetime value (LTV), and the LTV/CAC ratio — while avoiding the common distortions (blended vs paid CAC, gross-revenue vs contribution-margin LTV, survivorship in cohort curves).

---

## When to Use

- Validating that a business has healthy unit economics before scaling spend.
- Diagnosing why a growing business is not generating profit (CAC payback too long, retention weak).
- Subscription/SaaS, marketplace, e-commerce, or any acquire-and-retain model.
- Pressure-testing a plan's LTV/CAC claims in diligence or a board package.
- **Do not use** as a full company P&L or valuation; unit economics is a building block, not the whole model.

---

## Inputs / Context Required

```
<unit_economics_inputs>
Business / model type: [SaaS subscription | transactional | marketplace | e-commerce]
Currency:
Unit definition: [a customer | an account | an order | a seat] — state precisely

REVENUE & MARGIN per unit:
- Average revenue per unit/customer per period (ARPU / AOV)
- Variable/COGS per unit (hosting, support, payment fees, fulfillment, COGS)
- Gross margin %

ACQUISITION:
- Total sales & marketing spend (period); how it's attributed
- New customers acquired (period)
- Paid vs organic split (to separate paid CAC from blended CAC)

RETENTION / COHORTS:
- Cohort retention data (% of a cohort active over time) OR churn rate per period
- Revenue retention / expansion (net revenue retention) if applicable
- Discount rate for LTV present-valuing (optional; state if used)

CONTEXT:
- Contract length / billing frequency; expansion/upsell dynamics
- Data window (how many periods of cohort history exist)
</unit_economics_inputs>
```

---

## Constraints

### Must
- Define the **unit precisely** (DS-02) and keep it consistent across every metric.
- Build LTV on **contribution margin**, not gross revenue (NE-11):
  ```
  Contribution margin/unit = ARPU × Gross margin %  − variable cost not in COGS (support, payments)
  CAC (paid)   = Paid S&M spend / Customers acquired from paid channels
  CAC (blended)= Total S&M spend / All customers acquired (incl. organic)  ← report BOTH
  CAC payback (months) = CAC / (Monthly contribution margin per customer)
  ```
- Compute **LTV from cohort retention**, not a single churn point estimate, where data allows:
  ```
  Simple LTV = (Contribution margin/period) / Churn rate         (constant-churn approximation)
  Cohort LTV = Σ_t [ Retention_t × Contribution margin_t / (1+r)^t ]   (preferred; r optional)
  LTV/CAC ratio = LTV / CAC      (state which CAC — paid or blended)
  ```
- Report **both paid and blended CAC**; flag if a healthy ratio depends on organic acquisition that may not scale.
- Use **cohort curves** (DS-04 — pattern recognition): show retention by cohort age; identify whether curves flatten (a stable retained base) or decay to zero.
- Address **survivorship and immaturity** (QA-02): young cohorts haven't churned yet; don't extrapolate early retention as lifetime. State the data window.
- Present LTV/CAC and payback as a **range** (NE-10) under conservative/base/optimistic retention.
- State benchmark heuristics cautiously (e.g., LTV/CAC ~3x, payback <12 months are common rules of thumb, not laws) — never assert them as the company's required threshold without context.

### Must Not
- Use gross-revenue LTV (overstates value; LTV must be contribution-margin-based).
- Report only blended CAC when paid CAC is materially worse (hides scaling risk).
- Extrapolate immature cohort retention into a lifetime value.
- Present a single LTV/CAC point as precise; retention assumptions dominate the result.
- Invent retention curves, churn, or CAC; require data or label assumptions.
- Quote "3x LTV/CAC" as a universal pass/fail threshold without context.

---

## Instructions

1. **Define the unit and contribution margin (DS-02, NE-11).** State the unit; compute contribution margin per unit per period (revenue × GM% less variable serving costs). This — not gross revenue — drives LTV.

2. **Compute CAC, paid and blended.** Attribute S&M spend; divide by customers acquired. Report paid CAC (marginal cost to acquire the next customer) and blended CAC (includes free organic). Note the dependence on organic mix.

3. **Compute CAC payback.** Months to recover CAC from monthly contribution margin. Shorter payback = faster capital recycling and less financing risk.

4. **Build cohort retention (DS-04).** Plot retention by cohort age. Identify whether curves flatten to a stable plateau or decay toward zero. Use actual cohort data; state how many periods exist.

5. **Compute LTV (NE-11, NE-10).** Prefer cohort-based LTV summing retained contribution margin over time (optionally discounted). Provide the constant-churn approximation as a cross-check. Produce conservative/base/optimistic LTV using different retention assumptions.

6. **Compute LTV/CAC and interpret.** Show LTV/CAC for both paid and blended CAC. Interpret with payback together — a high LTV/CAC with a 24-month payback still strains cash.

7. **Stress and survivorship (QA-02).** Flag immature cohorts; show LTV if early retention does not hold. Test whether the unit economics still work if organic acquisition shrinks (paid CAC dominates).

8. **Verification (QA-01).** Confirm LTV uses contribution margin; confirm CAC is reported both ways; confirm cohort LTV doesn't extrapolate beyond data without flagging; state the swing assumption (almost always retention).

---

## Output Format

```
## Unit Economics — [Company], unit = [a customer]
Model: [SaaS] | Currency: [USD] | Cohort data window: [n] months
NOTE: figures below are ILLUSTRATIVE.

### Per-Unit Economics
| Metric | Value | Formula |
|--------|-------|---------|
| ARPU / month | $100 | input |
| Gross margin % | 75% | input |
| Variable serving cost (support, payments) | $8 | input |
| Contribution margin / month | $67 | 100×75% − 8 |
| Paid CAC | $900 | paid S&M / paid customers |
| Blended CAC | $600 | total S&M / all customers |
| CAC payback (paid) | 13.4 months | 900 / 67 |
| CAC payback (blended) | 9.0 months | 600 / 67 |

### Cohort Retention (illustrative)
| Cohort age (mo) | 1 | 3 | 6 | 12 | 24 |
|-----------------|---|---|---|----|----|
| Retention %     |100| 88| 78| 68 | 60* |
*24-mo only partially observed → flagged as immature, not extrapolated.

### LTV & LTV/CAC (range)
| Scenario | Retention assumption | Cohort LTV | LTV/CAC (paid) | LTV/CAC (blended) |
|----------|----------------------|------------|----------------|-------------------|
| Conservative | curve decays to 0 by mo 36 | $1,500 | 1.7x | 2.5x |
| Base | plateau at 55% | $2,400 | 2.7x | 4.0x |
| Optimistic | plateau at 65% + expansion | $3,200 | 3.6x | 5.3x |

### Read
- Blended economics look healthy; PAID economics are marginal (1.7–3.6x; 13-mo payback).
- The favorable blended ratio depends on organic acquisition — scaling risk if organic doesn't grow with spend.
- Retention plateau is the swing assumption; conservative case is barely above 1.5x on paid CAC.

### Survivorship Note
24-month retention is partially observed; LTV does not assume retention beyond the data window holds indefinitely.

(Rule-of-thumb heuristics like ~3x LTV/CAC and <12-mo payback are common references, not a pass/fail law for this company.)
```

---

## Verification

- [ ] Unit defined precisely and used consistently across all metrics.
- [ ] LTV built on contribution margin, not gross revenue.
- [ ] Both paid and blended CAC reported; organic dependence flagged.
- [ ] CAC payback computed in months.
- [ ] LTV computed from cohort retention where data allows; constant-churn cross-check shown.
- [ ] Immature cohorts flagged; no extrapolation beyond the data window without disclosure.
- [ ] LTV/CAC and payback presented as a range across retention assumptions.
- [ ] Swing assumption (retention) identified; benchmarks framed as heuristics.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Gross-revenue LTV | LTV must use contribution margin; gross-revenue LTV systematically overstates value |
| Reporting only blended CAC | Report paid CAC too; a ratio that works only on blended CAC hides scaling risk |
| Extrapolating young cohorts | Flag immature cohorts; do not project unobserved lifetime retention |
| Single precise LTV/CAC | Retention dominates; present a range and name retention as the swing assumption |
| Quoting "3x" as a hard threshold | Treat LTV/CAC and payback heuristics as references, not company-specific pass/fail lines |
| Ignoring payback when LTV/CAC looks good | Read payback and LTV/CAC together; long payback strains cash even at high LTV/CAC |
