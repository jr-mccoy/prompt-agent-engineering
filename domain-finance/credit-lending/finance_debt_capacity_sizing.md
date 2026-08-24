---
title: "Debt Capacity Sizing — Cash-Flow, Leverage, and Coverage-Constrained Sizing with Cushion"
category: finance/credit-lending
description: "Size a borrower's sustainable debt capacity using three independent constraints — leverage, debt-service coverage, and cash-flow sweep — take the binding (lowest) result, and apply a downside cushion; transparent arithmetic, no invented data."
techniques:
  - NE-11
  - DS-02
  - QA-02
  - RT-05
  - NE-10
difficulty: intermediate
tags:
  - debt-capacity
  - leverage
  - dscr
  - debt-sizing
  - cushion
  - sustainable-debt
updated: "2026-06-08"
related_prompts:
  - domain-finance/credit-lending/finance_covenant_design_aid.md
  - domain-finance/credit-lending/finance_five_cs_credit_analysis.md
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, credit, or lending advice. Final facility sizing must be set by qualified credit professionals.*

## Objective

Estimate a borrower's sustainable debt capacity by applying three independent sizing constraints — a target-leverage constraint, a minimum debt-service-coverage constraint, and a cash-flow-sweep / amortization constraint — computing each independently, taking the most binding (lowest) result, and applying a downside cushion. All inputs come from the user; the model shows every formula and never invents EBITDA, rates, or market multiples.

## When to Use

- Sizing a new term loan or acquisition financing
- Testing how much incremental debt a borrower can support
- Bounding a sponsor's proposed leverage against cash-flow reality
- Pre-work for a credit memo (`finance_credit_memo_builder.md`) or covenant design
- Stress-testing an existing capital structure for refinancing capacity

## Inputs / Context Required

Provide as much as available; missing items are flagged, not invented.

**Cash-flow inputs**
- EBITDA (LTM and base-case projection), maintenance capex, cash taxes, working-capital change
- CFADS definition the lender uses (state it)

**Existing structure**
- Existing debt balances, interest rates, scheduled amortization, lease/rent obligations, cash balance

**Sizing parameters**
- Target maximum leverage (Total Debt / EBITDA) — supplied by lender policy or `[ASSUMED]`
- Minimum required DSCR or FCCR — supplied or `[ASSUMED]`
- Assumed interest rate on new debt and amortization profile — supplied or `[ASSUMED]`
- Target tenor and any cash-sweep mechanics

**Cushion & scenario**
- Downside cushion policy (e.g., size to survive EBITDA -20%) — supplied or `[ASSUMED]`
- Downside / severe driver haircuts

## Constraints

### Must
- Compute each of the three sizing constraints independently with formula -> inputs -> result (NE-11).
- Take the BINDING (lowest) capacity across the three constraints as the sizing answer.
- Apply the stated downside cushion and re-test capacity under the downside case (RT-05).
- Cross-check (QA-02) that the resulting structure simultaneously satisfies all three constraints, not just the binding one.
- Flag every assumed rate, target, or cushion with `[ASSUMED]`.

### Must Not
- Invent EBITDA, interest rates, leverage targets, or coverage minimums.
- Present the leverage-based capacity as the answer when the coverage constraint is tighter.
- Size to the base case only when the cushion policy requires downside survival.
- Ignore existing debt or lease obligations in the coverage math.
- Treat capacity as a recommendation to lend the full amount.

## Instructions

1. **Establish CFADS.** Compute cash flow available for debt service per the stated definition:
```
CFADS = EBITDA - Maintenance Capex - Cash Taxes - ΔWorking Capital
```

2. **Constraint A — Leverage-based capacity.**
```
Total Debt Capacity (leverage) = Target Max Leverage x EBITDA
Incremental Capacity (leverage) = (Target Max Leverage x EBITDA) - Existing Debt
```

3. **Constraint B — Coverage-based capacity.** Solve for the debt service the borrower can support at the minimum DSCR, then back into a debt amount given rate and amortization:
```
Max Debt Service = CFADS / Min DSCR
Max Interest + Principal supportable = Max Debt Service
Implied Debt (annuity) = solve P from: Debt Service = P x [ r + amort_factor ]
   (state rate r, amortization profile; show the annuity/level-payment solve)
Incremental Capacity (coverage) = Implied Total Debt - Existing Debt
```
Include existing debt service in the coverage test; new capacity is incremental to it.

4. **Constraint C — Cash-flow-sweep / amortization capacity.** Size debt that fully amortizes (or sweeps to target) within tenor from projected CFADS:
```
Sweepable Cash per year = CFADS - Existing Mandatory Debt Service
Debt repayable over tenor = PV of sweepable cash at assumed rate
Incremental Capacity (sweep) = Debt repayable over tenor
```

5. **Take the binding constraint.** Capacity = min(A, B, C). Identify which constraint binds and why.

6. **Apply the downside cushion.** Re-run constraints under the downside EBITDA haircut; if the base-case capacity breaches the minimum DSCR or leverage in the downside, reduce capacity until the downside passes.

7. **Cross-check the structure.** Confirm the sized debt simultaneously satisfies leverage, coverage, and sweep constraints in the base case and survives the downside.

## Output Format

### CFADS Build
```
EBITDA                    $X
- Maintenance Capex       ($X)
- Cash Taxes              ($X)
- ΔWorking Capital        ($X)
= CFADS                   $X
```

### Three-Constraint Sizing
| Constraint | Formula | Result (Total Debt) | Incremental Capacity |
|---|---|---|---|
| A. Leverage | Target Leverage x EBITDA | $X | $X |
| B. Coverage | CFADS / Min DSCR -> debt | $X | $X |
| C. Sweep | PV of sweepable CFADS | $X | $X |
| **Binding (min)** | | **$X** | **$X** |
Binding constraint: [A/B/C] — [reason]

### Cushion Test (base / downside / severe)
| Metric @ sized debt | Base | Downside (EBITDA -X%) | Severe (EBITDA -X%) |
|---|---|---|---|
| Leverage | X.Xx | X.Xx | X.Xx |
| DSCR | X.XXx | X.XXx | X.XXx |
| Pass min DSCR? | yes/no | yes/no | yes/no |
| Cushioned capacity | $X | $X | $X |

### Cross-Check
- [ ] Leverage covenant satisfied at sized debt: X.Xx <= target
- [ ] DSCR satisfied at sized debt: X.XXx >= min
- [ ] Amortizes / sweeps within tenor: yes/no

### Sizing Conclusion
- Sustainable incremental debt capacity: **$X** (base) | **$X** (downside-cushioned)
- Assumptions flagged: [list `[ASSUMED]` items]

## Verification

- [ ] CFADS build is shown line-by-line.
- [ ] All three constraints are computed independently with formula -> inputs -> result.
- [ ] The binding (lowest) constraint is taken as the answer and named.
- [ ] Existing debt and lease service are included in the coverage math.
- [ ] Downside cushion is applied and the sized debt survives the downside.
- [ ] Cross-check confirms all three constraints hold at the sized amount.
- [ ] Every assumed rate/target/cushion is flagged `[ASSUMED]`.
- [ ] Output states capacity, not a recommendation to lend the maximum.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Reporting leverage capacity when coverage is tighter | Capacity = min of all three constraints; binding one named |
| Sizing to base case despite a downside-survival policy | Downside cushion test mandatory; capacity cut until downside passes |
| Omitting existing debt service from coverage | Existing mandatory service included; incremental capacity is residual |
| Inventing an interest rate or leverage target | Rates/targets supplied or flagged `[ASSUMED]`; not invented |
| Treating capacity as a lend recommendation | Output framed as capacity bound, subject to credit judgment |
| Ignoring amortization in the coverage solve | Debt-service annuity uses stated rate and amortization profile |
| Optimism bias in EBITDA projection | Base case independently stressed; downside drives cushion |
