---
title: "Retirement Account Tax Optimization — Pre-Tax / Roth / Taxable Allocation and Conversion-Ladder Scenarios"
category: finance/tax-planning
description: "Optimize across pre-tax, Roth, and taxable accounts with bracket-fill Roth-conversion-ladder logic, asset-location analysis, and RMD/IRMAA/NIIT interaction checks — modeling current-vs-future marginal-rate scenarios as comparison, not advice."
techniques:
  - NE-11
  - NE-10
  - QA-01
  - QA-02
  - OC-04
difficulty: advanced
tags:
  - roth-conversion
  - conversion-ladder
  - asset-location
  - rmd
  - irmaa
  - bracket-fill
updated: "2026-06-08"
related_prompts:
  - domain-finance/personal-finance-planning/finance_retirement_projection_model.md
  - domain-finance/personal-finance-planning/finance_tax_aware_withdrawal_sequencing.md
  - domain-finance/tax-planning/finance_multi_year_tax_projection.md
  - domain-finance/tax-planning/finance_charitable_giving_tax_strategy.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not tax, legal, investment, or accounting advice. Conversion, contribution, and withdrawal decisions depend on individual circumstances and changing law; filing, the pro-rata rule, RMD calculations, and reliance must be confirmed with a qualified tax/financial professional (CPA/EA/CFP/tax attorney). Verify all brackets, contribution limits, RMD ages/factors, IRMAA tiers, and NIIT thresholds against current tax law as of the analysis date and the applicable federal and state jurisdiction.**

## Objective

Produce an auditable analysis of how to allocate and convert assets across pre-tax (Traditional 401k/IRA), Roth, and taxable accounts that (1) compares the value of a deduction now vs tax-free growth later under current-vs-future marginal-rate scenarios, (2) models a bracket-fill Roth-conversion ladder, (3) applies asset-location logic, and (4) screens RMD, IRMAA, NIIT, and pro-rata interactions — so the user and their professional can compare options. This prompt analyzes; it does not direct contributions, conversions, or filings.

## When to Use

- Deciding Traditional vs Roth contributions in a given year.
- Planning Roth conversions during low-income years (early retirement, gap years, pre-RMD window).
- Designing a multi-year conversion ladder to "fill" lower brackets before RMDs and Social Security begin.
- Locating asset classes across account types for tax efficiency.
- Stress-testing the future-RMD tax "bomb" of a large pre-tax balance.

## Inputs / Context Required

```
<retirement_tax_context>
Jurisdiction: Federal — filing status [single/MFJ/MFS/HoH]; State [name] (state Roth/pension treatment varies)
Current-year picture (user-supplied; do NOT assume):
  Taxable ordinary income (excl. conversions):  [input]
  Marginal ordinary rate:                         [input current-year figure; verify]
  Bracket breakpoints (to fill):                  [input current-year thresholds; verify]
  Standard deduction:                             [input; verify]
  IRMAA tiers (Medicare premium surcharges):      [input current-year tiers; verify — 2-yr MAGI lookback]
  NIIT threshold:                                 [input; verify]
Ages: current age; spouse age; RMD-begin age [verify current law]
ACCOUNT BALANCES (user-supplied):
  Pre-tax (Traditional 401k/IRA):  $ ; basis (non-deductible contributions, if any): $
  Roth (IRA/401k):                  $ ; contributions vs earnings; 5-year-clock status
  Taxable brokerage:                $ ; embedded unrealized gains: $
Pro-rata exposure: any non-deductible (after-tax) IRA basis across ALL Traditional/SEP/SIMPLE IRAs? (yes/no)
Expected future income: pensions, Social Security (claim age), other.
Planning horizon and goals (bequest vs spend-down; charitable intent).
</retirement_tax_context>
```

## Constraints

### Must
- Frame the core trade as **marginal rate now vs marginal rate later** (NE-11/NE-10):
  - Roth (or conversion) wins when the future marginal rate ≥ current rate (or to buy tax-rate insurance/diversification).
  - Traditional/deduction wins when the future rate is expected lower.
  - Show the breakeven and treat future rates as a scenario range, not a point estimate.
- Model a **bracket-fill conversion ladder**: each year, convert an amount that fills the current bracket up to a chosen breakpoint without spilling into the next bracket (or IRMAA tier / NIIT crossing).
  ```
  Conversion headroom to a target breakpoint = max(0, Target breakpoint − Taxable income)
  Spillover check: conversion that crosses a higher bracket / IRMAA tier / NIIT threshold raises the MARGINAL cost.
  ```
- Apply the **pro-rata rule (Form 8606)**: if any pre-tax IRA basis (after-tax contributions) exists, a conversion is partly taxable in proportion — you cannot convert "only the after-tax dollars." Flag this and the backdoor-Roth interaction.
- Apply **asset-location** logic (DS-02): tax-inefficient assets (taxable bonds, REITs, high-turnover) generally favor tax-deferred/Roth; tax-efficient assets (broad equity index, qualified dividends, municipals) favor taxable; highest-expected-growth assets often favor Roth (tax-free growth).
- Screen **RMD / IRMAA / NIIT** interactions and the **5-year Roth-conversion clock** (each conversion has its own 5-year aging for penalty-free access of converted principal) — mark ages/limits `[verify]`.
- Use OC-04 conditional logic: if pro-rata basis exists → handle differently; if near an IRMAA cliff → cap conversion below the tier; if RMDs have begun → RMD cannot be converted and must come out first.
- Show formula → inputs → result and verify arithmetic (QA-01).

### Must Not
- Assert current-year brackets, contribution limits, RMD ages/factors, IRMAA tiers, or NIIT thresholds from memory — require user input or mark `[input current-year figure; verify]`.
- Recommend a specific action ("convert $X," "go all Roth") — present scenarios; the decision routes to the user and professional.
- Ignore the pro-rata rule when IRA basis exists, or present a "convert just the after-tax part" path.
- Treat a Roth conversion as free of an IRMAA two-year-lookback Medicare premium effect.
- Assume future tax rates equal current rates without testing a higher-rate and lower-rate scenario.

## Instructions

**Step 1 — Now-vs-later marginal-rate frame.**
```
Current marginal rate = [input]
Future marginal rate scenarios (NE-10): LOW (spend-down, no pension), BASE, HIGH (large RMDs + Social Security + survivor single-filer).
Decision lean per scenario:
  future ≥ current → favor Roth/conversion; future < current → favor Traditional. State breakeven.
```

**Step 2 — Bracket-fill conversion-ladder model.**
```
For each ladder year:
  Headroom = Target breakpoint − projected taxable income
  Suggested conversion (illustrative) = min(Headroom, pre-tax balance to convert)
  Tax cost = Conversion × marginal rate in that band (compute by tranche if it crosses bands)
  IRMAA check: does conversion push MAGI over a tier? (2-yr lookback hits future Medicare premiums)
  NIIT check: does it push MAGI over the NIIT threshold for taxable-account income?
Project pre-tax balance decline and future-RMD reduction across the ladder.
```

**Step 3 — Pro-rata rule check (OC-04).**
```
If aggregate non-deductible IRA basis B and total pre-tax IRA value V:
  Taxable % of any conversion = (V − B) / V
  → cannot isolate after-tax dollars; conversion is blended. Flag backdoor-Roth pro-rata trap.
```

**Step 4 — Asset-location grid (DS-02).**

| Asset class | Tax characteristic | Preferred location | Rationale |
|---|---|---|---|
| Broad equity index | low turnover, qualified div, LTCG | Taxable / Roth | tax-efficient; Roth if highest growth |
| Taxable bonds / REITs | ordinary income | Pre-tax (deferred) | shelter ordinary income |
| Municipal bonds | federally tax-exempt | Taxable | exemption wasted in deferred accounts |
| High-growth / high-conviction | large future gains | Roth | tax-free growth maximized |

**Step 5 — RMD / future-tax-bomb projection.**
```
Project pre-tax balance to RMD-begin age [verify] under no-conversion vs ladder.
Illustrative RMD = Balance / IRS life-expectancy factor [verify factor].
Show how RMDs stack with Social Security and pensions to raise the future marginal rate (the "tax bomb").
```

**Step 6 — Scenario comparison.**

| Scenario | Annual conversion | Tax cost now | IRMAA/NIIT crossed? | Future RMD reduction | Lifetime/illustrative tax delta |
|---|---|---|---|---|---|
| No conversion | 0 | 0 | — | none | baseline |
| Fill to lower breakpoint | | | | | |
| Fill to higher breakpoint | | | | | |
| Aggressive (multi-bracket) | | | | | |

**Step 7 — Adversarial stress-test (QA-02).**
- If future rates are LOWER than assumed, did converting overpay tax now (recency/anchoring on today's brackets)?
- Does a conversion cross an IRMAA cliff, adding two years of Medicare surcharges that erode the benefit?
- Does pre-tax IRA basis trigger the pro-rata rule, making a "backdoor"/conversion partly taxable unexpectedly?
- Survivor scenario: will a surviving spouse filing single face compressed brackets, raising the future rate?
- Does converting deplete taxable cash needed to PAY the conversion tax (paying tax from the IRA itself reduces the benefit and may incur penalties pre-59½)?
- State move: converting in a high-tax state vs a future low/no-tax state changes the answer.

## Output Format

```
## Retirement Account Tax Optimization
Jurisdiction: Federal [status] + State [name] | As of: [date] | Current-year figures: user-supplied/verify

### Now-vs-Later Rate Frame
[Step 1 — scenarios + breakeven]

### Conversion-Ladder Model
[Step 2 — per-year headroom, conversion, tax, IRMAA/NIIT flags]

### Pro-Rata Check
[Step 3 — taxable % if basis exists; backdoor flag]

### Asset-Location Grid
[Step 4 table]

### RMD / Future-Tax Projection
[Step 5 — no-conversion vs ladder; tax-bomb illustration]

### Scenario Comparison
[Step 6 table]

### Stress-Test Findings
[Step 7 — rate risk, IRMAA cliff, pro-rata, survivor, tax-payment source, state]

### Items to confirm with your professional
[pro-rata/Form 8606, current-year figures, RMD factors, IRMAA tiers, state treatment, 5-yr clocks]
```

## Verification

- [ ] Trade framed as current vs future marginal rate with a scenario range and breakeven.
- [ ] Conversion ladder fills brackets to a target breakpoint with spillover/tranche tax math shown.
- [ ] IRMAA two-year-lookback and NIIT crossings checked per conversion year.
- [ ] Pro-rata rule applied whenever IRA basis exists; backdoor-Roth trap flagged.
- [ ] Asset-location grid maps tax characteristic → preferred account.
- [ ] RMD future-tax-bomb projected (no-conversion vs ladder) with factor marked verify.
- [ ] 5-year conversion-clock noted for pre-59½ access.
- [ ] No current-year bracket, limit, RMD age/factor, IRMAA, or NIIT figure asserted from memory.
- [ ] State treatment and tax-payment-source addressed.
- [ ] Output frames scenarios, not a directive to convert.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Assuming future rate = current rate | Require LOW/BASE/HIGH future-rate scenarios and a breakeven before any conversion lean |
| Ignoring the IRMAA cliff on conversions | Per-year IRMAA check with two-year-lookback note; cap conversion below the tier in the model |
| "Convert only the after-tax dollars" | Pro-rata rule blends basis and pre-tax; show the taxable % formula and flag the backdoor trap |
| Treating Roth growth as a sure win | Win depends on future > current rate; present as rate insurance/diversification, not guaranteed savings |
| Paying conversion tax from the IRA | Stress-test flags that paying tax from the account (esp. pre-59½) erodes/penalizes the benefit |
| Asserting brackets/limits/RMD figures | All marked `[input current-year figure; verify with IRS/official source]` |
| Recommending "go all Roth" | Output is scenario comparison; the decision and pro-rata filing route to the professional |
