---
title: "Workout & Restructuring Options — Distressed-Credit Option Analysis and Recovery"
category: finance/credit-lending
description: "Analyze distressed-credit workout and restructuring options — amend-and-extend, debt-for-debt/equity exchange, discounted payoff, forbearance, enforcement — comparing recovery, time, and execution risk against a liquidation baseline; no invented recoveries or legal advice."
techniques:
  - RT-03
  - NE-10
  - QA-02
  - DS-02
  - AG-02
difficulty: advanced
tags:
  - workout
  - restructuring
  - distressed-credit
  - recovery
  - amend-extend
  - liquidation
updated: "2026-06-08"
related_prompts:
  - domain-finance/credit-lending/finance_watchlist_early_warning.md
  - domain-finance/credit-lending/finance_pd_lgd_ead_framing.md
  - domain-finance/credit-lending/finance_credit_memo_builder.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, credit, legal, or restructuring advice. Workout decisions require qualified credit, legal, and restructuring counsel.*

## Objective

Analyze the realistic workout and restructuring options for a distressed credit — amend-and-extend, covenant waiver/forbearance, debt-for-debt or debt-for-equity exchange, discounted payoff (DPO), additional collateral/guarantees, and enforcement/liquidation — comparing each option's estimated recovery, time to resolution, and execution risk against a liquidation baseline. All recovery and value inputs are user-supplied; the model frames the options and the comparison logic, and does not invent recoveries, legal outcomes, or market clearing levels.

## When to Use

- A credit has breached covenants or defaulted and the lender must choose a path
- Comparing restructuring proposals against a hold-and-enforce alternative
- Estimating recovery ranges to inform reserves (`finance_pd_lgd_ead_framing.md`)
- Preparing a workout recommendation for credit committee
- Triaging a credit flagged by the early-warning system (`finance_watchlist_early_warning.md`)

## Inputs / Context Required

Provide as much as available; missing items are flagged, not invented.

**Exposure & structure**
- Outstanding balance, accrued interest, lien position, seniority, guarantees
- Collateral type and current value, advance/liquidation discounts
- Maturity, current covenant/default status, intercreditor terms

**Borrower situation**
- Cause of distress (liquidity vs. solvency), projected go-forward cash flow
- Sponsor support / willingness to inject capital
- Other creditors, capital structure seniority, pending events

**Option-specific inputs**
- For DPO: proposed payoff amount; for exchange: proposed new terms / equity stake
- Estimated liquidation value and timeline; recovery cost and discount rate

**Context**
- Jurisdiction and insolvency regime (affects enforcement timeline and priority) — verify against current law as of [date]
- Reporting currency

## Constraints

### Must
- Build a liquidation baseline first (RT-03): the recovery if the lender enforces today. Every option is measured against it.
- For each option, estimate recovery, time to resolution, and execution risk from supplied data (DS-02), showing the recovery arithmetic.
- Discount recoveries to present value at a stated rate (NE-10) so options with different timelines are comparable.
- Default to a skeptical stance (AG-02): treat borrower/sponsor promises as conditional; require evidence of capacity to perform.
- Cross-check (QA-02) that the recommended option's PV recovery exceeds the liquidation baseline, or state why a lower-recovery option is preferred (e.g., systemic/relationship reasons) explicitly.
- Flag jurisdiction-dependent assumptions and "verify against current law as of [date]."

### Must Not
- Invent recovery rates, liquidation values, legal outcomes, or market clearing prices.
- Present a restructuring as value-accretive without comparing PV recovery to the liquidation baseline.
- Treat a sponsor's capital-injection promise as committed without evidence.
- Provide legal advice on enforcement, priority, or insolvency mechanics — flag for counsel.
- Ignore intercreditor or priority constraints that cap the lender's recovery.

## Instructions

1. **Establish the liquidation baseline.** Estimate recovery from enforcement today:
```
Liquidation Recovery = (Collateral Value x Liquidation Discount) - Enforcement Costs
PV Liquidation Recovery = Liquidation Recovery / (1 + d)^t_liq
Baseline Recovery % = PV Liquidation Recovery / Total Exposure
```
Respect lien priority and intercreditor caps.

2. **Enumerate viable options.** For this credit, list the workout options that are actually available given the cause of distress, capital structure, and collateral:
   - Amend-and-extend (maturity extension, repricing)
   - Forbearance / covenant waiver (temporary relief)
   - Debt-for-debt exchange (new money / PIK / payment deferral)
   - Debt-for-equity exchange (DDE)
   - Discounted payoff (DPO)
   - Additional collateral / guarantee / sponsor injection
   - Enforcement / liquidation (the baseline)

3. **Estimate each option's recovery.** For each, compute expected recovery and PV:
```
Option Recovery = Σ Expected Cash Flows under option
PV Option Recovery = Σ CF_t / (1 + d)^t
Recovery % = PV Option Recovery / Total Exposure
Uplift vs Baseline = PV Option Recovery - PV Liquidation Recovery
```

4. **Score time and execution risk.** For each option, estimate time to resolution and an execution-risk rating (borrower cooperation, other-creditor consent, legal/regulatory approval). Tag dependencies.

5. **Apply the skeptical disconfirming check.** For options relying on sponsor support or improved cash flow, ask: what evidence shows capacity to perform, and what is the recovery if it does not materialize (downside)?

6. **Rank and recommend.** Rank options by base-case PV recovery, then by downside-protected recovery and execution risk. Recommend the option with the best risk-adjusted recovery above the baseline; if the recommended option is below baseline, justify explicitly.

## Output Format

### Liquidation Baseline
```
Collateral Value x Liquidation Discount = $X
- Enforcement Costs                     = ($X)
= Liquidation Recovery                  = $X
PV @ d% over t_liq                      = $X
Baseline Recovery %                     = X% of $[exposure]
Priority / intercreditor cap notes      = [...]
```

### Option Comparison (base / downside / severe)
| Option | Base PV Recovery | Recovery % | Downside PV | Severe PV | Time | Execution Risk | Uplift vs Baseline |
|---|---|---|---|---|---|---|---|
| Liquidation (baseline) | $X | X% | $X | $X | t_liq | — | 0 |
| Amend & Extend | $X | X% | $X | $X | | low/med/high | +$X |
| Forbearance | $X | X% | $X | $X | | | +$X |
| Debt-for-Debt Exchange | $X | X% | $X | $X | | | +$X |
| Debt-for-Equity (DDE) | $X | X% | $X | $X | | | +$X |
| Discounted Payoff (DPO) | $X | X% | $X | $X | | | +$X |
| Additional Collateral/Injection | $X | X% | $X | $X | | | +$X |

### Disconfirming Check (sponsor / cash-flow-dependent options)
| Option | Performance Assumption | Evidence of Capacity | Recovery if Assumption Fails |
|---|---|---|---|
| ... | sponsor injects $X | [evidence/none] | $X |

### Recommendation
- **Recommended path:** [option] — PV recovery $X (X%), uplift +$X vs. baseline, execution risk [level].
- **Key dependencies:** [borrower consent / other creditors / legal — flag for counsel].
- **Jurisdiction note:** verify enforcement/priority against current law as of [date].

## Verification

- [ ] Liquidation baseline is built first with priority/intercreditor caps respected.
- [ ] Each option's recovery is computed from supplied data with arithmetic shown.
- [ ] Recoveries are PV-discounted at a stated rate for timeline comparability.
- [ ] Base / downside / severe recoveries are presented per option.
- [ ] Sponsor/cash-flow assumptions carry a disconfirming check with a fail-case recovery.
- [ ] Recommended option's PV recovery exceeds the baseline, or the exception is justified.
- [ ] No recovery rate, liquidation value, or legal outcome was invented.
- [ ] Jurisdiction-dependent items flagged "verify against current law as of [date]."

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Presenting a restructuring as accretive without a baseline | Liquidation baseline mandatory; every option measured against it |
| Comparing options with different timelines at face value | All recoveries PV-discounted at a stated rate |
| Treating a sponsor injection as committed | Disconfirming check requires evidence and a fail-case recovery |
| Inventing a liquidation or recovery value | Values supplied or flagged; not invented |
| Giving legal advice on priority/enforcement | Legal mechanics flagged for counsel; jurisdiction note attached |
| Ignoring intercreditor caps on recovery | Priority and intercreditor constraints applied to baseline and options |
| Optimism bias in go-forward cash flow | Downside and severe recoveries required for each option |
