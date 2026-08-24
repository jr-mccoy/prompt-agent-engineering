---
title: "Cash Flow Forecasting Model — Direct/Indirect Forecast, Liquidity Buffer, and Variance Loop"
category: finance/treasury-capital-markets
description: "Build a rolling cash-flow forecast (direct receipts/disbursements and indirect reconciliation) with a target liquidity buffer, scenario ranges, and a forecast-to-actual variance loop that improves accuracy over time."
techniques:
  - NE-11
  - NE-10
  - QA-01
  - DS-02
  - RT-05
difficulty: intermediate
tags:
  - cash-flow-forecast
  - liquidity
  - treasury
  - working-capital
  - variance-analysis
updated: "2026-06-08"
related_prompts:
  - domain-finance/treasury-capital-markets/finance_liquidity_runway_covenant_analysis.md
  - domain-finance/treasury-capital-markets/finance_investment_policy_statement_builder.md
  - domain-finance/risk-management/finance_liquidity_risk_analysis.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or hedge-accounting advice.**

## Objective

Build an auditable rolling cash-flow forecast that combines a short-horizon **direct method** (line-by-line receipts and disbursements) with a longer-horizon **indirect method** (reconciled from projected P&L and balance-sheet movements), establishes a target **minimum liquidity buffer**, expresses the forecast as a scenario range rather than a single line, and installs a **variance loop** so each actual period recalibrates the next forecast.

---

## When to Use

- Treasury building a 13-week direct cash forecast plus a 12-month indirect forecast.
- FP&A integrating a cash view into the operating plan and covenant monitoring.
- Pre-financing diligence — demonstrating cash discipline to lenders or investors.
- Turnaround / restructuring where short-dated liquidity is the binding constraint.
- **Do not use** as a substitute for an audited statement of cash flows, a bank-confirmed daily position, or a formal solvency opinion; this produces a forecasting framework and flags, not a verified cash balance.

---

## Inputs / Context Required

```
<cash_forecast_inputs>
Entity / group name:
Reporting currency:               [e.g., USD]
Other operating currencies:       [list; note if multi-currency consolidation is needed]
Jurisdiction(s):                  [for tax/payroll/withholding timing]
Forecast horizons:                Short = 13 weeks (direct) | Long = 12 months (indirect)
Forecast cadence:                 [weekly roll | monthly roll]

OPENING POSITION
- Opening cash & cash equivalents (by currency, by account/entity):
- Undrawn committed facilities (RCF availability, by facility):
- Restricted / trapped cash (note locations and restrictions):

DIRECT INPUTS (short horizon)
- AR aging + collection assumptions (DSO, expected timing by bucket):
- AP aging + payment terms (DPO, scheduled runs):
- Payroll calendar and amounts:
- Tax payment calendar (VAT/GST, income tax, payroll tax):
- Debt service schedule (interest + amortization dates):
- Capex commitments with timing:
- Known one-offs (settlements, dividends, M&A):

INDIRECT INPUTS (long horizon)
- Projected P&L (revenue, EBITDA) by month:
- Working-capital drivers (DSO/DPO/DIO assumptions):
- D&A, deferred items, non-cash charges:
- Planned financing (draws, repayments, issuance):

POLICY
- Target minimum cash / liquidity buffer (amount or # days):
- Concentration / counterparty limits on cash holdings (if any):
</cash_forecast_inputs>
```

---

## Constraints

### Must
- Produce **both** views and reconcile them: a direct 13-week forecast and an indirect 12-month forecast that tie to the same opening cash.
- Anchor on **days cash on hand** and the **minimum liquidity buffer**:
  - `Days Cash on Hand = (Cash + Undrawn Committed Facilities) ÷ (Average Daily Cash Operating Outflow)`
  - `Liquidity Headroom = (Cash + Undrawn Committed Facilities) − Minimum Buffer`
- Express every horizon as **base / upside / downside** (NE-10); never a single deterministic line.
- Show formula → inputs → result for each computed metric (NE-11).
- Separate **committed** vs **discretionary** outflows so the downside can defer the discretionary set.
- Flag the **lowest projected liquidity point** ("liquidity trough") in each scenario, with its date.
- Install a **variance loop**: define how prior-period actual vs forecast feeds the next roll, and track a forecast-accuracy metric (MAPE on net cash flow).
- Flag **currency and jurisdiction**: trapped cash, repatriation friction, and FX translation should be visible, not buried.
- Name the relevant **bias** (optimism/anchoring on collections timing) and require a disconfirming check.

### Must Not
- Invent collection rates, tax dates, or facility availability not in the inputs.
- Treat undrawn facilities as cash without noting drawdown conditions/covenants that gate access.
- Net trapped/restricted cash into available liquidity without disclosure.
- Present a single-point cash trough as precise; show the scenario band.
- Assume revolver headroom survives a covenant breach (a breach can freeze draws).

---

## Instructions

1. **Set the opening position.**
   - Sum cash by account/entity/currency; separate restricted/trapped cash explicitly.
   - State available liquidity = unrestricted cash + undrawn committed facilities (note draw conditions).

2. **Build the direct 13-week forecast.**
   - Roll receipts from AR aging and collection timing; roll disbursements from AP, payroll, tax, debt service, capex.
   - Tag each outflow **Committed** or **Discretionary**.
   ```
   Net Weekly Cash Flow = Total Receipts − Total Disbursements
   Ending Cash (week n) = Ending Cash (week n−1) + Net Weekly Cash Flow (n)
   ```

3. **Build the indirect 12-month forecast.**
   ```
   CFO ≈ EBITDA − Cash Taxes − Cash Interest − ΔNet Working Capital
   ΔNWC = ΔAR + ΔInventory − ΔAP   (increase in AR/Inv uses cash; increase in AP sources cash)
   Net Change in Cash = CFO + CFI (capex, M&A) + CFF (draws − repay − dividends)
   ```
   - Derive AR/AP/inventory movements from DSO/DPO/DIO assumptions; state each assumption.

4. **Reconcile direct ↔ indirect.**
   - The 13-week direct ending cash for the overlapping weeks should reconcile to the indirect monthly trajectory. Explain residual differences (timing vs accrual).

5. **Compute liquidity metrics (NE-11).**
   ```
   Average Daily Cash Operating Outflow = (Trailing or projected annual cash opex) ÷ 365
   Days Cash on Hand = (Cash + Undrawn Committed Facilities) ÷ Avg Daily Cash Outflow
   Liquidity Headroom = (Cash + Undrawn Committed Facilities) − Minimum Buffer
   ```

6. **Scenario the forecast (NE-10).**
   - **Base:** input assumptions as stated.
   - **Downside:** stress collections (e.g., DSO +10–15 days), defer none of the committed outflows, slip one large receipt.
   - **Upside:** collections accelerate, discretionary capex deferred.
   - Identify the **liquidity trough** (lowest ending cash and its date) per scenario.

7. **Stress the access assumption.**
   - Test the case where the revolver is unavailable (covenant trip or market stress). Recompute days cash on hand on unrestricted cash only.

8. **Install the variance loop (RT-05).**
   - For each closed period: `Variance = Actual Net Cash Flow − Forecast Net Cash Flow`.
   - Track `MAPE = mean(|Variance| ÷ |Forecast|)` over the trailing rolls.
   - Specify the recalibration rule (e.g., persistent collection slippage → raise DSO assumption).

9. **Bias check.**
   - Name the optimism/anchoring risk on collection timing; state one disconfirming test (e.g., back-test last 4 weeks of forecast collections vs actual).

10. **Verification pass (QA-01).**
    - Re-add each week's ending-cash chain; confirm opening cash ties across both methods.

---

## Output Format

```
## Cash Flow Forecast — [Entity]
Reporting currency: [CCY] | Horizons: 13-week (direct) + 12-month (indirect)
Opening cash (unrestricted): [amount] | Undrawn committed facilities: [amount]
Restricted/trapped cash (excluded from available): [amount, locations]
Prepared: [date] | Data: user-supplied | All figures illustrative unless sourced

### Liquidity Summary
| Metric                         | Value        | Formula |
|--------------------------------|--------------|---------|
| Available liquidity            | $185M (illustrative) | Cash $60M + Undrawn RCF $125M |
| Minimum buffer (policy)        | $50M (illustrative)  | input |
| Liquidity headroom             | $135M (illustrative) | Available − Buffer |
| Avg daily cash outflow         | $2.1M (illustrative) | Annual cash opex ÷ 365 |
| Days cash on hand              | 88 days (illustrative) | Available ÷ Daily outflow |

### 13-Week Direct Forecast (condensed; illustrative)
| Week | Receipts | Committed Out | Discretionary Out | Net | Ending Cash |
|------|----------|---------------|-------------------|-----|-------------|
| W1   | 42       | (35)          | (4)               | 3   | 63          |
| ...  | ...      | ...           | ...               | ... | ...         |
| W7 (trough) | 28 | (40)         | (3)               | (15)| 41 ⚠ near buffer |
| W13  | 50       | (33)          | (5)               | 12  | 58          |

### 12-Month Indirect Forecast (condensed; illustrative)
| Month | EBITDA | ΔNWC | Cash Tax/Int | Capex | Financing | Net | Ending Cash |
|-------|--------|------|--------------|-------|-----------|-----|-------------|
| M1    | 18     | (6)  | (4)          | (5)   | 0         | 3   | 63          |
| ...   | ...    | ...  | ...          | ...   | ...       | ... | ...         |

### Scenario Range — Liquidity Trough
| Scenario | Trough Ending Cash | Trough Date | Days Cash @ Trough | Buffer Breach? |
|----------|--------------------|-------------|--------------------|----------------|
| Upside   | $58M (illustrative)| W10         | 99                 | No             |
| Base     | $41M (illustrative)| W7          | 70                 | No (near)      |
| Downside | $22M (illustrative)| W6          | 38                 | ⚠ Yes, draw RCF|
| Downside, RCF unavailable | $(8)M | W6  | n/a                | ⚠ Shortfall    |

### Variance Loop (trailing)
| Period | Forecast Net CF | Actual Net CF | Variance | MAPE (rolling) | Recalibration |
|--------|-----------------|---------------|----------|----------------|---------------|
| W-2    | 5               | 2             | (3)      | 14%            | Raise DSO +3d |

### Key Flags & Actions
| Priority | Finding | Action |
|----------|---------|--------|
| 1 | Downside trough breaches buffer at W6 | Pre-arrange RCF draw / defer discretionary capex |
| 2 | RCF-unavailable case shows shortfall | Confirm draw conditions & covenant headroom |

**Disconfirming check:** Back-test last 4 weeks of forecast collections vs actual; if collections consistently arrive ≥1 week late, base-case timing is optimistic.
```

---

## Verification

- [ ] Opening cash ties across direct and indirect methods.
- [ ] Direct ending-cash chain re-adds correctly week over week.
- [ ] Days cash on hand and liquidity headroom computed from stated formulas and inputs.
- [ ] Each scenario reports a dated liquidity trough.
- [ ] Undrawn facilities tested for the unavailable case (covenant/market stress).
- [ ] Restricted/trapped cash excluded from available liquidity and disclosed.
- [ ] Variance loop defines a concrete recalibration rule and tracks MAPE.
- [ ] Currency/jurisdiction effects (trapped cash, FX) made visible.
- [ ] No figure used that is not traceable to a stated input.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Counting undrawn revolver as guaranteed liquidity | Note drawdown conditions and that a covenant breach can freeze access; show an RCF-unavailable scenario |
| Presenting a single cash trough as precise | Report base/upside/downside trough with dates; cash forecasting is uncertain by nature |
| Optimistic collection timing (anchoring on best month) | Back-test recent forecast vs actual collections; widen DSO in downside |
| Treating trapped/restricted cash as spendable | Exclude from available liquidity; disclose location and restriction |
| Reconciliation gap dismissed as "rounding" | Explain direct vs indirect differences as timing vs accrual, not noise |
| Assuming working-capital release on demand | NWC swings depend on counterparties; do not assume instant inventory/AR conversion |
