---
title: "Covenant Design Aid — Financial Covenant Selection, Headroom Sizing, Definitions"
category: finance/credit-lending
description: "Design a financial covenant package: select the right covenant types for the credit, size headroom off base/downside projections, and write precise definitions and test mechanics — methodology only, with no invented market norms or thresholds."
techniques:
  - NE-11
  - DS-02
  - CM-02
  - NE-10
  - OC-01
difficulty: advanced
tags:
  - covenants
  - covenant-design
  - headroom
  - loan-structure
  - definitions
  - maintenance-covenants
updated: "2026-06-08"
related_prompts:
  - domain-finance/credit-lending/finance_covenant_headroom_monitor.md
  - domain-finance/credit-lending/finance_credit_memo_builder.md
  - domain-finance/credit-lending/finance_debt_capacity_sizing.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, credit, or legal advice. Final covenant terms and definitions must be set by qualified credit and legal counsel.*

## Objective

Design a financial covenant package suited to a specific credit: select appropriate covenant types (leverage, coverage, liquidity, capex limits), size each covenant's headroom from the borrower's base and downside projections, and draft precise calculation definitions and test mechanics. The aid provides methodology and structure; it does not assert market-standard levels or invent thresholds — covenant levels are derived from the borrower's own projected metrics plus a stated cushion.

## When to Use

- Structuring covenants for a new term loan, revolver, or private-credit facility
- Re-cutting covenants at amendment, refinancing, or extension
- Translating a credit thesis into testable, enforceable covenant terms
- Building the covenant section of a credit memo (`finance_credit_memo_builder.md`)
- Sanity-checking a proposed covenant package for headroom adequacy

## Inputs / Context Required

Provide as much as available; missing items are flagged, not invented.

**Borrower projections**
- Base-case and downside projections (>=3 years): EBITDA, interest, scheduled principal, capex, cash
- Existing and pro-forma debt schedule, lease and rent obligations
- Working-capital profile and seasonality

**Facility & structure**
- Facility type, amount, tenor, amortization, security
- Lender risk appetite / target rating (state it; otherwise `[ASSUMED]`)
- Whether covenants are maintenance (tested periodically) or incurrence (tested at actions)

**Definition inputs**
- EBITDA add-back policy the lender will permit (state it; do not invent)
- Treatment of leases (operating vs. finance), cash netting caps, equity-cure rights
- Test frequency (quarterly / monthly) and grace/cure provisions desired

**Cushion policy**
- Target headroom cushion vs. base case (e.g., 25-35% on leverage; state the lender's policy or use `[ASSUMED]`)

## Constraints

### Must
- Show covenant-sizing arithmetic explicitly (NE-11): formula -> projected metric -> applied cushion -> covenant level.
- Derive every covenant level from the borrower's own projections plus a stated cushion — never from invented market norms.
- Write a precise calculation definition for each covenant (numerator, denominator, periods, add-backs).
- Manage the constraint tension (CM-02) between protection (tight covenants) and operating flexibility (room to perform); state the trade-off explicitly.
- Size headroom against the downside case, not only the base case.
- Flag every assumed cushion, add-back, or threshold with `[ASSUMED]`.

### Must Not
- Assert "market-standard" covenant levels or cushions as fact.
- Invent borrower projection figures or lease/working-capital data.
- Set a covenant tighter than the base case (immediate breach) or so loose it never triggers.
- Omit the definition mechanics — an undefined covenant is unenforceable.
- Confuse maintenance and incurrence covenant test triggers.

## Instructions

1. **Select covenant types for the credit.** From the credit profile, choose the covenants that bind the actual risks (e.g., cash-flow-lending -> leverage + coverage; asset-based -> borrowing-base + fixed-charge). Justify each selection against a specific risk.

2. **Compute base and downside projected metrics.** For each candidate covenant, calculate the borrower's projected value each test period:
```
Leverage ratio        = Total Net Debt / EBITDA
Interest Coverage     = EBITDA / Cash Interest
Fixed-Charge Coverage = (EBITDA - Unfinanced Capex - Cash Taxes) / (Interest + Principal + Rents)
DSCR                  = CFADS / (Interest + Scheduled Principal)
Minimum Liquidity     = Cash + Available Revolver
```

3. **Size headroom and set the covenant level.** Apply the stated cushion to the projected metric:
```
Max Leverage Covenant = Base-Case Leverage x (1 + cushion%)         # e.g., 4.0x x 1.30 = 5.2x
Min Coverage Covenant = Base-Case Coverage x (1 - cushion%)         # e.g., 2.5x x 0.80 = 2.0x
Headroom %            = |Covenant Level - Projected Metric| / Projected Metric
```
Verify the level is NOT breached in the base case and IS protective in the downside.

4. **Set step-downs / build-ups.** Where amortization deleverages the credit, schedule covenant tightening over time; show the schedule.

5. **Draft calculation definitions.** For each covenant, write: numerator and denominator components, measurement period (e.g., LTM), permitted add-backs (capped, stated), netting caps, and pro-forma adjustment rules.

6. **Specify test mechanics.** Test frequency, reporting deadlines, compliance certificate requirement, equity-cure rights and limits, grace periods, and cross-default linkage.

7. **State the protection/flexibility trade-off.** For the package as a whole, note where tighter terms were chosen for protection and where flexibility was granted, and why.

## Output Format

### Covenant Selection Rationale
| Covenant | Risk It Addresses | Maintenance / Incurrence |
|---|---|---|
| Max Leverage | over-borrowing / cash-flow risk | maintenance |
| Min FCCR | debt-service capacity | maintenance |
| Min Liquidity | runway / refinancing | maintenance |
| Capex limit / RP basket | cash leakage | incurrence |

### Headroom Sizing (per covenant)
```
Covenant: Max Net Leverage
  Base-case projected leverage (Y1): X.Xx
  Cushion applied: [ASSUMED] %
  Covenant level set: X.Xx
  Headroom (base): X% | Downside projected: X.Xx | Headroom (downside): X%
```

### Covenant Levels by Period (base / downside / severe)
| Covenant | Level Y1 | Level Y2 | Level Y3 | Base Y1 | Downside Y1 | Severe Y1 |
|---|---|---|---|---|---|---|
| Max Net Leverage | X.Xx | X.Xx | X.Xx | X.Xx | X.Xx | X.Xx |
| Min FCCR | X.Xx | X.Xx | X.Xx | X.Xx | X.Xx | X.Xx |
| Min Liquidity | $ | $ | $ | $ | $ | $ |

### Calculation Definitions
| Covenant | Numerator | Denominator | Period | Add-Backs (capped) | Netting |
|---|---|---|---|---|---|
| Net Leverage | Total Debt - Cash (cap $X) | LTM EBITDA + add-backs | LTM | [stated, capped] | [cap] |

### Test Mechanics
- Frequency: [quarterly/monthly] | Reporting deadline: [days]
- Compliance certificate: [required]
- Equity cure: [permitted? limit? frequency cap?]
- Grace period / cross-default: [stated]

### Protection vs. Flexibility Trade-off
[Where the package is tight and why; where flexibility was granted and why]

## Verification

- [ ] Every covenant level is derived from a projected metric plus a stated cushion — not a market norm.
- [ ] Sizing arithmetic is shown: formula -> projected metric -> cushion -> level.
- [ ] No covenant is breached in the base case; all are protective in the downside.
- [ ] Each covenant has a complete calculation definition (numerator, denominator, period, add-backs, netting).
- [ ] Maintenance vs. incurrence classification is correct for each covenant.
- [ ] Test mechanics (frequency, certificate, cure, grace) are specified.
- [ ] All assumed cushions/add-backs/thresholds are flagged `[ASSUMED]`.
- [ ] The protection/flexibility trade-off is stated explicitly.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Citing "market-standard" covenant levels | Levels derived from borrower projections + stated cushion; norms not invented |
| Covenant breaches in the base case | Hard check: base-case headroom must be positive |
| Covenant so loose it never triggers | Downside-case test required; covenant must bind in stress |
| Undefined EBITDA add-backs inflating headroom | Add-backs must be capped and stated; uncapped add-backs flagged |
| Conflating maintenance and incurrence tests | Each covenant classified explicitly with its trigger |
| Omitting equity-cure abuse risk | Cure rights capped in frequency and amount; flagged if uncapped |
| Inventing lease or working-capital figures | Definitions reference supplied data only; gaps flagged |
