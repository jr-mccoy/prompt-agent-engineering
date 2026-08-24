---
title: "Covenant Headroom Monitor — Compliance Tracking and Downside Headroom Projection"
category: finance/credit-lending
description: "Track covenant compliance against actuals, project forward headroom under base/downside/severe cases, and flag periods at risk of breach — with transparent arithmetic and no invented financials or thresholds."
techniques:
  - NE-11
  - DS-02
  - RT-05
  - QA-02
  - NE-10
difficulty: intermediate
tags:
  - covenant-monitoring
  - headroom
  - compliance
  - breach-projection
  - portfolio-monitoring
  - downside-case
updated: "2026-06-08"
related_prompts:
  - domain-finance/credit-lending/finance_covenant_design_aid.md
  - domain-finance/credit-lending/finance_watchlist_early_warning.md
  - domain-finance/credit-lending/finance_credit_memo_builder.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, credit, or lending advice. Covenant compliance determinations must be made by qualified credit officers against executed loan documents.*

## Objective

Monitor a borrower's covenant compliance: compute the current covenant ratios against the executed covenant levels, calculate headroom for each test, and project forward headroom under base, downside, and severe cases to flag periods where a breach is likely. All metrics are computed from user-supplied actuals and projections; no figures or covenant levels are invented.

## When to Use

- Quarterly covenant compliance testing against actual results
- Forward-looking breach risk assessment ahead of a soft quarter
- Portfolio monitoring across multiple facilities
- Amendment or waiver preparation when headroom is thin
- Feeding breach-risk signals into a watchlist process (`finance_watchlist_early_warning.md`)

## Inputs / Context Required

Provide as much as available; missing items are flagged, not invented.

**Covenant terms (from loan documents)**
- Each financial covenant, its definition, level by test period, and step-down schedule
- Test frequency, measurement period (e.g., LTM), and add-back/netting rules
- Equity-cure rights and any grace provisions

**Actuals**
- Reported financials for the test period (EBITDA, debt, interest, principal, cash, capex, rents)
- Prior-period actuals for trend

**Projections**
- Base-case forward projections through the next 4-8 test periods
- Downside and severe-case driver assumptions (or ask the model to apply stated haircuts)

**Context**
- Reporting currency, accounting framework, any pending add-back disputes

## Constraints

### Must
- Compute each covenant ratio with formula -> inputs -> result (NE-11).
- Calculate headroom as both absolute and percentage terms.
- Use only the executed covenant levels supplied; never assume a level.
- Project forward under base / downside / severe with internally consistent drivers (RT-05).
- Run a quality cross-check (QA-02): confirm the covenant definition used matches the supplied loan-document definition (add-backs, netting, period).
- Flag any test period where projected headroom is negative or below a stated trigger band.

### Must Not
- Invent covenant levels, actuals, or projection figures.
- Apply add-backs not permitted by the supplied definition.
- Net cash beyond the supplied cap.
- Declare "compliant" without showing the arithmetic.
- Treat a base-case pass as sufficient when the downside breaches.

## Instructions

1. **Reconstruct each covenant calculation per definition.** Pull the numerator and denominator components per the supplied definition, applying only permitted, capped add-backs and netting.
```
Net Leverage   = (Total Debt - min(Cash, Cash Cap)) / (LTM EBITDA + permitted add-backs)
FCCR           = (EBITDA - Unfinanced Capex - Cash Taxes) / (Interest + Principal + Rents)
Interest Cover = EBITDA / Cash Interest
Min Liquidity  = Cash + Available Revolver
```

2. **Compute current headroom.** For each covenant:
```
For a MAX covenant (e.g., leverage):
  Headroom (abs) = Covenant Level - Actual Ratio
  Headroom (%)   = (Covenant Level - Actual Ratio) / Covenant Level

For a MIN covenant (e.g., FCCR, liquidity):
  Headroom (abs) = Actual Ratio - Covenant Level
  Headroom (%)   = (Actual Ratio - Covenant Level) / Covenant Level
```
A positive headroom = compliant; negative = breach.

3. **Compute the breach-driver sensitivity.** For each covenant, solve for the EBITDA (or driver) level that produces zero headroom — the breach threshold:
```
Breach EBITDA (leverage covenant) = (Total Debt - Cash) / Covenant Level
EBITDA cushion to breach = Actual EBITDA - Breach EBITDA   (and as %)
```

4. **Project forward headroom.** For the next 4-8 test periods, project each covenant ratio under base / downside / severe cases (respecting step-downs), and compute headroom each period.

5. **Flag at-risk periods.** Mark any period where projected headroom is negative or within a stated thin-headroom band (e.g., <10%). Note whether an equity cure could remedy it and the cure cost.

6. **Quality cross-check.** Confirm the definition used matches the loan document; flag any add-back or netting assumption.

## Output Format

### Current-Period Compliance
| Covenant | Definition Type | Covenant Level | Actual | Headroom (abs) | Headroom (%) | Status |
|---|---|---|---|---|---|---|
| Net Leverage | MAX | X.Xx | X.Xx | ±X.Xx | ±X% | Compliant/Breach |
| FCCR | MIN | X.Xx | X.Xx | ±X.Xx | ±X% | ... |
| Min Liquidity | MIN | $ | $ | ±$ | ±X% | ... |

### Breach-Driver Sensitivity
```
Net Leverage covenant:
  Breach EBITDA = (Total Debt - Cash) / Covenant Level = $X
  Actual EBITDA = $Y | EBITDA cushion to breach = $Z (X%)
```

### Forward Headroom Projection
| Covenant | Period | Covenant Level | Base Headroom % | Downside Headroom % | Severe Headroom % | Flag |
|---|---|---|---|---|---|---|
| Net Leverage | Q+1 | X.Xx | X% | X% | X% | [at risk?] |
| Net Leverage | Q+2 | X.Xx (step-down) | X% | X% | X% | ... |

### At-Risk Periods & Cure Analysis
| Period | Covenant | Projected Breach Case | Equity Cure Available? | Estimated Cure Cost |
|---|---|---|---|---|
| ... | ... | downside/severe | yes/no | $ |

### Definition Cross-Check Notes
[Add-backs applied, netting cap used, period basis — confirm matches loan document]

## Verification

- [ ] Each covenant ratio shows formula -> inputs -> result.
- [ ] Headroom is reported in absolute and percentage terms with correct MAX/MIN polarity.
- [ ] Covenant levels match the supplied loan-document levels (none assumed).
- [ ] Only permitted, capped add-backs and netting were applied.
- [ ] Breach-driver (EBITDA-to-breach) sensitivity is computed per covenant.
- [ ] Forward projection respects step-downs and uses internally consistent downside/severe drivers.
- [ ] At-risk periods are flagged with cure availability and cost.
- [ ] Definition cross-check is documented.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Reporting "compliant" off base case while downside breaches | Forward headroom shown for base/downside/severe; at-risk periods flagged |
| Applying generous add-backs to manufacture headroom | Only supplied, capped add-backs permitted; assumptions flagged |
| Assuming a covenant level not in the documents | Levels must be supplied; missing levels block the calculation |
| Ignoring step-downs that tighten future tests | Step-down schedule applied period-by-period |
| Wrong polarity (MAX vs MIN) inverting headroom sign | Definition type tagged per covenant; sign convention verified |
| Treating an equity cure as costless | Cure cost and frequency cap quantified |
| Netting cash beyond the cap | Netting cap from definition enforced |
