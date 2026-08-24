---
title: "Liquidity Runway & Covenant Analysis — Runway Months, Covenant Headroom, and Maturity Walls"
category: finance/treasury-capital-markets
description: "Project liquidity runway in months against the minimum-cash buffer, covenant thresholds, and the debt maturity wall across base and stress scenarios, identifying the binding constraint and its date."
techniques:
  - NE-11
  - NE-10
  - QA-02
  - QA-01
  - RT-05
difficulty: intermediate
tags:
  - liquidity-runway
  - covenant-headroom
  - maturity-wall
  - cash-burn
  - stress-testing
updated: "2026-06-08"
related_prompts:
  - domain-finance/treasury-capital-markets/finance_cash_flow_forecasting_model.md
  - domain-finance/credit-lending/finance_covenant_headroom_monitor.md
  - domain-finance/risk-management/finance_liquidity_risk_analysis.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or hedge-accounting advice.**

## Objective

Project how long available liquidity lasts (runway, in months) and test it against three potential binding constraints — the minimum-cash buffer, financial covenants, and the debt maturity wall — across base and stress scenarios, then identify which constraint binds first, on what date, and what cushion exists before it.

---

## When to Use

- Pre-revenue or cash-burning companies tracking months of runway.
- Lender or board reporting on liquidity adequacy and covenant compliance.
- Pre-refinancing planning where a maturity wall is approaching.
- Distress/turnaround monitoring where the binding constraint must be identified.
- **Do not use** as a solvency opinion, a going-concern conclusion, or a covenant-cure recommendation requiring legal review of the credit agreement.

---

## Inputs / Context Required

```
<liquidity_runway_inputs>
Entity:
Reporting currency:                [CCY]
Jurisdiction:                      [trapped-cash / repatriation notes]
As-of date:

LIQUIDITY
- Unrestricted cash & equivalents:
- Undrawn committed facilities (availability, expiry, draw conditions):
- Restricted / trapped cash (excluded):

BURN / CASH FLOW
- Net monthly cash burn (or net cash flow) — recent run-rate:
- Path of burn (improving? worsening? seasonal?):
- Known step-changes (hiring, capex, contract starts):

COVENANTS
- Maintenance covenants: max leverage, min coverage, min liquidity, min EBITDA:
- Test frequency (quarterly/monthly) and next test date:
- Current covenant metric values:

DEBT MATURITIES
- Schedule: tranche, amount, maturity date:
- Refinancing assumptions (if any committed):

POLICY
- Minimum-cash buffer (amount or # months):
- Stress assumptions to apply (burn +X%, revenue −Y%, facility unavailable):
</liquidity_runway_inputs>
```

---

## Constraints

### Must
- Compute **runway in months** from available liquidity and net burn:
  - `Cash Runway (months) = Available Liquidity ÷ Net Monthly Cash Burn`
  - Use a forward burn path, not a single trailing month, where the path is known.
- Test **three constraints** and report the **binding one** (earliest date among them):
  1. Buffer: month when usable cash hits the minimum-cash floor.
  2. Covenant: next test date where a covenant would breach on the projected trajectory.
  3. Maturity: the date of the next material maturity vs. projected liquidity to meet it.
- Present **base and stress scenarios (NE-10)**; stress at minimum must include burn acceleration and a facility-unavailable case.
- Show **covenant headroom** with formula → inputs → result for each maintenance covenant.
- Apply an **adversarial stress (QA-02)** and state the date and cushion of the first binding constraint.
- Exclude restricted/trapped cash; track undrawn facilities separately with draw conditions.
- Flag currency/jurisdiction effects on cash availability.

### Must Not
- Report runway from cash alone if committed facilities are available (and vice versa — don't count facilities that a breach would freeze).
- Average burn across dissimilar periods if a step-change is known.
- Treat a covenant as binding without checking the next actual test date and definitions.
- Present a single runway number as precise; show the scenario band.
- Assume a maturity will refinance without a committed facility.

---

## Instructions

1. **Establish available liquidity.**
   ```
   Available Liquidity = Unrestricted Cash + Undrawn Committed Facilities (accessible)
   (exclude restricted/trapped cash; note facility draw conditions/covenant gates)
   ```

2. **Define the burn path.** Use the forward run-rate; incorporate known step-changes and seasonality. State whether burn is improving or worsening.

3. **Compute base-case runway.**
   ```
   Cash-only runway (months)   = Unrestricted Cash ÷ Net Monthly Burn
   Total runway (months)       = Available Liquidity ÷ Net Monthly Burn
   Buffer-constrained runway   = (Available Liquidity − Minimum Buffer) ÷ Net Monthly Burn
   ```
   The buffer-constrained runway is the operationally relevant figure.

4. **Project covenant trajectory.** For each maintenance covenant, project the metric to each upcoming test date.
   ```
   Net Debt/EBITDA at test = (Debt − Cash projected) / EBITDA (trailing-12m projected)
   EBITDA/Interest, Min Liquidity, Min EBITDA — projected to each test date
   Covenant headroom = Limit − Projected metric (or Projected − Min, as applicable)
   Breach date = first test date where headroom < 0
   ```

5. **Overlay the maturity wall.** For each maturity, compare projected available liquidity at that date to the amount due.
   ```
   Maturity coverage = Projected Available Liquidity at maturity ÷ Amount Due
   Flag if coverage < 1.0x without a committed refinancing.
   ```

6. **Identify the binding constraint.** Take the earliest date among: buffer-exhaustion, first covenant breach, and an uncovered maturity. That is the binding constraint; report its date and cushion.

7. **Run stress scenarios (NE-10 / QA-02).**
   - **Base:** as input.
   - **Stress 1 — burn +25%:** recompute runway and covenant dates.
   - **Stress 2 — facility unavailable:** runway on unrestricted cash only.
   - **Stress 3 — revenue/EBITDA −20%:** recompute covenant trajectory (often binds before cash).
   Report the binding constraint and date per scenario.

8. **Recalibration note (RT-05).** State how the analysis should be re-run as actuals arrive (e.g., monthly roll updating burn and covenant metrics).

9. **Bias check + verification (QA-01).** Named pitfall: recency bias (extrapolating the best recent burn month). Disconfirming check: re-run runway on the worst trailing burn month. Confirm runway arithmetic and that excluded cash is excluded.

---

## Output Format

```
## Liquidity Runway & Covenant Analysis — [Entity]
Currency: [CCY] | As-of: [date] | Prepared: [date] | Data: user-supplied
(All figures illustrative unless traced to an input)

### Available Liquidity
| Component                    | Amount | Note |
|------------------------------|--------|------|
| Unrestricted cash            | 80.0   | illustrative |
| Undrawn committed facilities | 50.0   | gated by 4.0x leverage covenant |
| Less restricted/trapped      | (10.0) | excluded |
| Available liquidity          | 130.0  | illustrative |
| Minimum buffer (policy)      | 30.0   | input |

### Runway
| Measure                     | Months (illustrative) |
|-----------------------------|-----------------------|
| Net monthly burn (forward)  | 9.0 |
| Cash-only runway            | 8.9 |
| Total runway (incl. facility)| 14.4 |
| Buffer-constrained runway   | 11.1 ← operationally relevant |

### Covenant Trajectory
| Covenant         | Limit | Next test | Projected | Headroom | Breach date |
|------------------|-------|-----------|-----------|----------|-------------|
| Net Debt/EBITDA  | ≤4.0x | Q3        | 3.6x      | 0.4x     | Q4 (proj. 4.2x) ⚠ |
| EBITDA/Interest  | ≥3.0x | Q3        | 3.4x      | 0.4x     | none in window |
| Min liquidity    | ≥30   | monthly   | 70        | 40       | Month 11 |

### Maturity Wall
| Maturity | Amount | Date | Projected liquidity | Coverage | Flag |
|----------|--------|------|---------------------|----------|------|
| Term loan| 100    | M18  | 25                  | 0.25x    | ⚠ uncovered — refi required |

### Binding Constraint (earliest)
| Scenario              | Binding constraint | Date     | Cushion to it |
|-----------------------|--------------------|----------|---------------|
| Base                  | Covenant (leverage)| Q4       | 0.4x leverage |
| Stress: burn +25%     | Buffer             | Month 8  | — |
| Stress: facility unavail | Cash buffer     | Month 5  | — |
| Stress: EBITDA −20%   | Covenant (leverage)| Q3       | breach at test |

### Actions
| Priority | Finding | Action |
|----------|---------|--------|
| 1 | Leverage covenant breaches Q4 (base) | Pursue amendment/waiver or deleverage before test |
| 2 | M18 maturity uncovered | Launch refinancing now |
| 3 | Facility gated by covenant | A breach freezes the RCF — model without it |

**Disconfirming check:** Re-run runway on worst trailing burn month; if runway falls below the next covenant test date, base case is optimistic.
```

---

## Verification

- [ ] Runway computed three ways (cash-only, total, buffer-constrained); buffer-constrained highlighted.
- [ ] All three constraints (buffer, covenant, maturity) tested; binding one identified with date.
- [ ] Covenant headroom shown with formulas and projected to actual test dates.
- [ ] Maturity wall overlaid; uncovered maturities flagged.
- [ ] Base + stress scenarios (burn +, facility unavailable, EBITDA −) reported.
- [ ] Restricted/trapped cash excluded; facility draw conditions noted.
- [ ] Recency-bias disconfirming check applied.
- [ ] No figure untraceable to an input.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Counting a covenant-gated facility as runway | Model a facility-unavailable case; a breach can freeze draws |
| Single runway number presented as precise | Scenario band required; runway is uncertain |
| Extrapolating best recent burn | Recency-bias check on worst trailing month |
| Assuming a maturity refinances | Require committed facility; otherwise flag uncovered |
| Treating covenant as non-binding without test-date check | Project to actual test dates and definitions |
| Including trapped cash in runway | Exclude and disclose location/restriction |
