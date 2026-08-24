---
title: "Debt Issuance Analysis — Size, Tenor, Fixed/Float, Covenants, and All-In Cost"
category: finance/treasury-capital-markets
description: "Analyze a proposed debt issuance: right-size it, set tenor, choose fixed vs floating, evaluate covenants, and compute the true all-in cost including fees and OID across scenarios."
techniques:
  - NE-11
  - NE-10
  - QA-02
  - DS-02
  - RT-02
difficulty: advanced
tags:
  - debt-issuance
  - all-in-cost
  - covenants
  - fixed-vs-floating
  - refinancing
updated: "2026-06-08"
related_prompts:
  - domain-finance/treasury-capital-markets/finance_capital_structure_optimization.md
  - domain-finance/credit-lending/finance_covenant_design_aid.md
  - domain-finance/credit-lending/finance_debt_capacity_sizing.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or hedge-accounting advice.**

## Objective

Analyze a proposed debt issuance end to end: confirm the size against use of proceeds and capacity, set an appropriate tenor against the maturity profile, evaluate fixed vs floating rate exposure, assess the covenant package, and compute the **all-in cost** (coupon + fees + original issue discount, amortized to yield) — presented across rate scenarios so the decision is robust to market moves.

---

## When to Use

- Evaluating a term loan, bond, private placement, or revolver before launch.
- Comparing competing financing proposals (e.g., fixed bond vs. floating term loan).
- Refinancing decisions where the new all-in cost must beat the existing one net of fees.
- Pre-negotiation analysis of a covenant package's restrictiveness.
- **Do not use** to compute hedge-accounting treatment of any swap (route ASC 815 / IFRS 9 specifics to accounting) or to set the firm-wide target leverage (use `finance_capital_structure_optimization.md`).

---

## Inputs / Context Required

```
<debt_issuance_inputs>
Issuer:
Currency:                          [CCY]
Jurisdiction / governing law:      [tax-deductibility, withholding]
Instrument type:                   Term loan | Bond | Private placement | RCF | Other
Use of proceeds:                   [refi / capex / acquisition / GCP / dividend]

PROPOSED TERMS
- Principal (face) amount:
- Tenor (years) / amortization profile (bullet | sculpted | mortgage-style):
- Rate basis:                      Fixed coupon ___% | Floating = ref rate + margin ___bps
- Reference rate (if float):       [SOFR / EURIBOR / etc.] + current level + date
- Original issue discount (OID) / premium:
- Upfront fees (arrangement, underwriting, OID, legal/rating as % or $):
- Call schedule / prepayment penalties:
- Security (secured/unsecured), ranking:

COVENANTS (proposed)
- Financial maintenance covenants (max leverage, min coverage, min liquidity):
- Incurrence covenants / baskets:
- Negative covenants (liens, RP, asset sales):

CONTEXT
- Existing debt schedule (tranche, rate, maturity) for maturity-wall check:
- EBITDA / coverage for covenant headroom:
- Marginal tax rate:
- Rate-scenario assumptions to test (e.g., +/−100/200 bps):
</debt_issuance_inputs>
```

---

## Constraints

### Must
- Compute the **all-in cost** as a yield, not just the coupon: include upfront fees and OID amortized over the tenor.
  - Approximate all-in cost (pre-tax) ≈ `[Coupon × Face + (Fees + OID)/Tenor] ÷ Net Proceeds`; reconcile to an IRR-based YTM on the net cash flows.
- Show **after-tax** cost using the marginal tax rate (note deductibility limits).
- For **floating** instruments, model the rate path across **scenarios (NE-10)**; do not assume the current reference rate persists.
- Compare **fixed vs floating** on an apples-to-apples all-in basis across the rate scenarios; state the breakeven.
- Evaluate **tenor** against the existing maturity wall — flag concentration if this issuance stacks near other maturities.
- Assess **covenant headroom** at issuance and under a downturn (QA-02 stress).
- Trace every figure to an input; label illustrative figures.
- Flag currency/jurisdiction and "verify current reference-rate levels and spreads as of [date]."

### Must Not
- Quote the coupon as the cost of debt (ignores fees/OID).
- Assume the floating reference rate is constant.
- Invent market spreads, benchmark yields, or rating-based pricing.
- Ignore prepayment penalties when comparing to a refinancing alternative.
- Present covenant headroom only at issuance without a stress case.

---

## Instructions

1. **Confirm size and use of proceeds.** Tie principal to the stated use; cross-check against debt capacity (reference `finance_debt_capacity_sizing.md`). Flag over-raising (negative carry) or under-raising (re-access risk).

2. **Compute net proceeds.**

   ```
   Net Proceeds = Face Amount − OID − Upfront Fees
   Effective discount = (Face − Net Proceeds) / Face
   ```

3. **Compute all-in cost (pre-tax YTM).** Build the cash-flow vector (net proceeds in, coupon/amort out, principal at maturity) and solve for IRR:

   ```
   0 = Net Proceeds − Σ_t [ Coupon_t + Amort_t ] / (1 + y)^t − Principal_final / (1 + y)^n
   Solve for y = all-in pre-tax yield (YTM).
   Quick check: All-in ≈ [Annual Coupon + (Fees+OID)/Tenor] / Net Proceeds
   After-tax all-in = y × (1 − marginal tax rate)   [cap if deductibility limited]
   ```

4. **Model floating-rate scenarios (NE-10).** For a floating instrument, project the all-in cost under base/up/down reference-rate paths:

   ```
   Floating coupon_t = Reference rate_t + Margin
   All-in(float) computed per scenario using projected reference path.
   ```

5. **Fixed vs floating comparison + breakeven.**

   ```
   Breakeven reference rate = level at which All-in(float) = All-in(fixed)
   If expected/forward path < breakeven → floating cheaper (but carries rate risk)
   Note: fixed transfers rate risk to the issuer's favor if rates rise; floating wins if rates fall/stable.
   ```
   Recommend based on cost AND the issuer's rate-risk tolerance and natural hedges.

6. **Tenor & maturity-wall check.** Overlay the new maturity on the existing schedule.

   ```
   Maturity concentration = (Debt maturing in any 12-mo window) / Total Debt
   Flag if this issuance pushes any window above a stated concentration threshold (illustrative caution ~ >30%).
   ```

7. **Covenant evaluation.** Assess each maintenance covenant's headroom at issuance:

   ```
   Leverage headroom = Covenant Max − Net Debt/EBITDA (post-issuance)
   Coverage headroom = (EBITDA / Interest, post-issuance) − Covenant Min
   ```
   Flag incurrence baskets and negative covenants that constrain future flexibility.

8. **Adversarial stress (QA-02).** Apply an EBITDA downturn and a rate-up shock (for floating). Recompute coverage, leverage, and covenant headroom. Identify the first covenant to breach and the cushion to it.

9. **Refinancing comparison (if applicable).** Compare new all-in cost to the existing instrument's remaining all-in cost **including** prepayment penalty and unamortized fees on the old debt.

   ```
   Refi NPV benefit = PV(interest savings) − Prepayment penalty − New issuance fees − Unamortized old fees
   ```

10. **Bias check + verification (QA-01).** Named pitfall: tail-risk blindness on floating-rate exposure (assuming today's low rate persists). Disconfirming check: re-run with reference rate at the trailing 5-year high. Then re-solve the all-in IRR and confirm net-proceeds arithmetic.

---

## Output Format

```
## Debt Issuance Analysis — [Issuer]
Instrument: [type] | Currency: [CCY] | Prepared: [date] | Data: user-supplied
(All figures illustrative unless traced to an input)

### Proceeds & All-In Cost
| Item                  | Value (illustrative) |
|-----------------------|----------------------|
| Face amount           | 500.0 |
| OID                   | (5.0) |
| Upfront fees          | (7.5) |
| Net proceeds          | 487.5 |
| Coupon / margin       | 6.25% fixed (or SOFR + 275) |
| All-in pre-tax YTM    | 6.62% |
| After-tax all-in      | 4.97% (at 25% tax) |

### Fixed vs Floating (across rate scenarios)
| Scenario (ref-rate path) | All-in Fixed | All-in Float | Cheaper |
|--------------------------|--------------|--------------|---------|
| Down −100 bps            | 6.62%        | 5.70%        | Float   |
| Base                     | 6.62%        | 6.65%        | ~Tie    |
| Up +100 bps              | 6.62%        | 7.60%        | Fixed   |
| Up +200 bps              | 6.62%        | 8.55%        | Fixed   |
Breakeven reference rate: ~[X]% (illustrative)

### Tenor & Maturity Wall
| Year | Existing maturities | + New issuance | 12-mo concentration |
|------|---------------------|----------------|---------------------|
| Y3   | 200                 | —              | 22% |
| Y5   | 150                 | 500 (new)      | ⚠ 41% — concentration flag |

### Covenant Headroom
| Covenant         | Limit | Post-issuance | Headroom | Stress (EBITDA −25%) |
|------------------|-------|---------------|----------|----------------------|
| Net Debt/EBITDA  | ≤4.0x | 3.2x          | 0.8x     | 4.3x ⚠ breach |
| EBITDA/Interest  | ≥3.0x | 4.5x          | 1.5x     | 3.1x (tight) |
| Min liquidity    | ≥50   | 120           | 70       | 65 |

### Refinancing Comparison (if applicable)
| Line                         | Value (illustrative) |
|------------------------------|----------------------|
| PV interest savings          | 18.0 |
| Less prepayment penalty      | (6.0) |
| Less new fees + unamortized old fees | (9.0) |
| Net refi benefit (NPV)       | +3.0 → proceed (marginal) |

### Recommendation
Size: confirmed vs use of proceeds. Tenor: [X]y — caution on Y5 maturity stacking.
Rate basis: [fixed/float] — rationale: cost across scenarios + issuer rate-risk tolerance.
Covenant flag: leverage covenant breaches under −25% EBITDA stress; negotiate cushion or step-down.
```

---

## Verification

- [ ] All-in cost computed as IRR on net cash flows, including fees and OID — not the coupon alone.
- [ ] After-tax cost shown with marginal tax rate and deductibility note.
- [ ] Floating rate modeled across scenarios; current reference rate not assumed constant.
- [ ] Fixed vs floating compared on all-in basis with a stated breakeven.
- [ ] Tenor checked against existing maturity wall; concentration flagged.
- [ ] Covenant headroom shown at issuance and under EBITDA stress; first breach identified.
- [ ] Refi comparison (if relevant) nets prepayment penalty and unamortized fees.
- [ ] No invented spreads, yields, or rating-based pricing.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Quoting coupon as cost of debt | All-in cost = IRR on net proceeds incl. fees + OID |
| Assuming floating rate stays low | Model scenarios; tail-risk check at trailing-high reference rate |
| Inventing market pricing | Use only user-supplied spreads/yields; verify current levels as of [date] |
| Covenant headroom only at issuance | Mandatory QA-02 downturn stress; identify first breach |
| Refi "saves money" ignoring penalties | Net prepayment penalty + unamortized old fees into NPV |
| Tenor chosen in isolation | Overlay on maturity wall; flag 12-month concentration |
