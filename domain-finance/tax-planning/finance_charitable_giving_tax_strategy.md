---
title: "Charitable Giving Tax Strategy Modeler — DAF, Appreciated Stock, Bunching, and QCD Scenarios"
category: finance/tax-planning
description: "Model charitable-giving strategies — appreciated-stock donation vs cash, donor-advised-fund bunching above the standard deduction, qualified charitable distributions from IRAs, and AGI-limit interactions — as after-tax scenario comparison, not advice."
techniques:
  - NE-11
  - NE-10
  - QA-01
  - QA-02
  - DS-02
difficulty: intermediate
tags:
  - charitable-giving
  - donor-advised-fund
  - appreciated-stock
  - bunching
  - qcd
  - itemized-deductions
updated: "2026-06-08"
related_prompts:
  - domain-finance/tax-planning/finance_capital_gains_harvesting_analysis.md
  - domain-finance/tax-planning/finance_multi_year_tax_projection.md
  - domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not tax, legal, or accounting advice. Charitable deduction rules, AGI limits, substantiation requirements, and QCD rules change and depend on individual circumstances; appraisal, filing, and reliance decisions must be made with a qualified tax professional (CPA/EA/tax attorney). Verify all deduction percentages, AGI limits, standard-deduction amounts, and QCD age/limit rules against current tax law as of the analysis date and the applicable federal and state jurisdiction.**

## Objective

Produce an auditable comparison of charitable-giving structures that (1) computes the after-tax cost of each giving method, (2) models bunching above the standard deduction across years, (3) compares donating appreciated stock vs cash vs selling-then-giving, (4) screens QCD eligibility, and (5) checks AGI-limit and AMT/phaseout interactions — so the user and their tax professional can compare options. This prompt analyzes; it does not direct gifts or filings.

## When to Use

- A donor wants to maximize the tax efficiency of planned giving.
- Deciding between donating appreciated securities vs cash.
- Evaluating a donor-advised fund (DAF) to bunch several years of giving into one itemizing year.
- An IRA owner of QCD-eligible age considering qualified charitable distributions to satisfy RMDs tax-efficiently.
- A high-income year (liquidity event, bonus, Roth conversion) where a large deduction is valuable.

## Inputs / Context Required

```
<charitable_context>
Jurisdiction: Federal — filing status [single/MFJ/MFS/HoH]; State [name] (state deduction rules vary; some have none)
Current-year income (user-supplied; do NOT assume):
  AGI:                                          [input]
  Marginal ordinary rate:                       [input current-year figure; verify]
  Standard deduction for status:                [input current-year figure; verify]
  Other itemizable deductions (SALT capped, mortgage interest, etc.): [input]
  AMT exposure flag:                            yes | no | unknown
Giving intent:
  Annual giving amount (typical):               $
  Planned multi-year horizon for bunching:      [# years]
ASSETS available to give (repeat):
  Asset: cash | publicly-traded appreciated stock | restricted/illiquid | IRA (for QCD)
  For stock: cost basis, current FMV, holding period (>1yr = long-term needed for FMV deduction)
  For IRA: owner age (QCD eligibility age must be verified), RMD amount this year
Charity type: public charity (50%/60%-type) | private foundation (lower AGI limits) | DAF (treated as public-charity gift)
</charitable_context>
```

## Constraints

### Must
- Compute the **after-tax cost of giving** for each method (NE-11): `After-tax cost = Gift amount − Tax benefit`, where the tax benefit only exists to the extent itemizing **exceeds** the standard deduction.
- Model the **standard-vs-itemize threshold** explicitly: a charitable deduction yields zero marginal federal benefit if total itemized deductions stay below the standard deduction — this is the core bunching insight.
- Compare **appreciated-stock donation** vs **sell-then-donate cash**:
  - Donating long-term appreciated stock to a public charity/DAF: deduct **fair market value** (subject to AGI %) AND avoid the capital-gains tax on the appreciation.
  - Selling then donating: realize cap-gains tax first, donate the net — strictly worse for appreciated stock held long-term, all else equal.
- Apply **AGI-limit** awareness: cash to public charities and FMV stock to public charities have different AGI ceilings; private-foundation gifts are lower; excess carries forward (commonly 5 years). Mark all percentages `[input current-year figure; verify]`.
- Screen **QCD**: a qualified charitable distribution from an IRA (owner of eligible age) can satisfy RMDs and is **excluded from income** (not a deduction) — often better than deducting because it lowers AGI directly (helping IRMAA, NIIT, and phaseouts). Mark age/limit `[verify]`.
- Run NE-10 scenarios: annual giving (no bunching) vs bunched DAF year + standard-deduction years; cash vs appreciated stock; with/without QCD.
- Verify arithmetic (QA-01) and show formula → inputs → result throughout.

### Must Not
- Assert current-year standard-deduction, AGI-limit %, QCD age/limit, or bracket figures from memory — require user input or mark `[input current-year figure; verify]`.
- Recommend a specific gift ("donate X to a DAF") — present after-tax scenarios; the decision routes to the user and professional.
- Claim a deduction benefit when itemized deductions do not exceed the standard deduction.
- Treat appreciated-stock FMV deduction as available for short-term holdings (short-term/ordinary-income property is generally limited to basis).
- Ignore that a QCD is an income exclusion, not an itemized deduction (it helps even non-itemizers and lowers AGI-linked thresholds).

## Instructions

**Step 1 — Itemize-vs-standard baseline.**
```
Baseline itemized (no extra giving) = SALT(capped) + mortgage interest + other
If Baseline itemized < Standard deduction → marginal charitable benefit starts only on dollars
   that push total itemized ABOVE the standard deduction.
Marginal benefit zone = max(0, Standard deduction − Baseline itemized)  [first dollars give no benefit]
```

**Step 2 — After-tax cost per method (NE-11).**
```
Cash gift, itemizing:
  Deduction benefit = Deductible amount above standard × Marginal rate (+ state benefit if any)
  After-tax cost = Gift − benefit
Appreciated long-term stock to public charity/DAF:
  Deduction = FMV (subject to AGI %); ALSO avoided cap-gains tax = (FMV − basis) × cap-gains rate
  After-tax cost = FMV − (FMV deduction × marginal rate) − avoided cap-gains tax
Sell-then-donate (comparison):
  Cap-gains tax paid = (FMV − basis) × cap-gains rate ; donate net; deduct net amount
  → show this is generally costlier for LT appreciated stock.
```

**Step 3 — Bunching model (NE-10).**
```
Strategy A (annual): each year giving < standard → little/no benefit.
Strategy B (bunch N years into a DAF in Year 1):
  Year 1 itemized = baseline + (N × annual gift) → exceeds standard, benefit captured
  Years 2..N take the standard deduction; DAF grants out over time.
Compare total N-year tax over A vs B.
```

**Step 4 — QCD screen.**
```
If IRA owner ≥ QCD-eligible age [verify]:
  QCD up to annual limit [verify] goes directly to charity, EXCLUDED from income,
  counts toward RMD. Effect: lowers AGI (helps IRMAA/NIIT/phaseouts) without needing to itemize.
Compare QCD vs taking RMD + itemized cash gift.
```

**Step 5 — AGI-limit & carryforward check.**
```
Gift type AGI ceiling [verify %]; if gift > ceiling × AGI → excess carries forward (commonly 5 yrs).
Flag any year where the deduction is limited and a carryforward is created.
```

**Step 6 — Scenario comparison.**

| Scenario | Method | Deductible / excluded amount | Cap-gains avoided | Fed tax benefit | AGI effect | State | After-tax cost of giving |
|---|---|---|---|---|---|---|---|
| Annual cash | itemize? | | — | | | | |
| Bunch into DAF (cash) | itemize Y1 | | — | | | | |
| Appreciated stock to DAF | itemize Y1 | | yes | | | | |
| QCD (if eligible) | exclude | | n/a | | lowers AGI | | |

**Step 7 — Adversarial stress-test (QA-02).**
- Does the user actually itemize, or is the "deduction" worthless because they take the standard deduction?
- Is the donated stock long-term? Short-term/ordinary-income property limits the deduction to basis.
- Does a large FMV stock gift hit the AGI ceiling, deferring benefit to a carryforward (time value lost)?
- Would a QCD beat the deduction by lowering AGI-linked costs (IRMAA, NIIT, Social Security taxation)?
- AMT: does the giving year coincide with AMT, changing the marginal value of the deduction?
- Substantiation: appraisals for non-publicly-traded gifts, contemporaneous written acknowledgment — flag requirements (route to professional).

## Output Format

```
## Charitable Giving Tax Strategy Analysis
Jurisdiction: Federal [status] + State [name] | As of: [date] | Current-year figures: user-supplied/verify

### Itemize-vs-Standard Baseline
[Step 1 — marginal benefit zone]

### After-Tax Cost by Method
[Step 2 calcs: cash / appreciated stock / sell-then-donate]

### Bunching Model
[Step 3 — multi-year A vs B comparison]

### QCD Screen (if eligible)
[Step 4]

### AGI Limits & Carryforward
[Step 5 flags]

### Scenario Comparison
[Step 6 table]

### Stress-Test Findings
[Step 7 — itemize reality, holding period, AGI ceiling, QCD, AMT, substantiation]

### Items to confirm with your tax professional
[appraisal/substantiation, current-year limits, QCD eligibility, state treatment]
```

## Verification

- [ ] Itemize-vs-standard baseline computed; marginal-benefit zone identified.
- [ ] After-tax cost shown for cash, appreciated stock, and sell-then-donate with formulas.
- [ ] Appreciated-stock advantage (FMV deduction + avoided cap gains) demonstrated for long-term holdings only.
- [ ] Bunching modeled across multiple years (DAF in year 1, standard deduction in others).
- [ ] QCD screened as an income exclusion (not deduction); AGI-lowering benefits noted; age/limit marked verify.
- [ ] AGI ceilings and 5-year carryforward flagged where limits bind.
- [ ] No current-year standard-deduction, AGI %, QCD, or bracket figure asserted from memory.
- [ ] AMT-year and state treatment addressed.
- [ ] Output frames after-tax scenarios, not a directive to give.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Counting a deduction benefit for a non-itemizer | Compute the itemize-vs-standard threshold first; benefit applies only to dollars above the standard deduction |
| FMV deduction for short-term/ordinary-income property | Restrict FMV-deduction logic to long-term appreciated property; otherwise deduction limited to basis |
| Treating "sell then donate" as equal to donating stock | Show the cap-gains tax leakage; donating LT appreciated stock is generally superior |
| Ignoring AGI ceilings and carryforwards | Step 5 flags limited years; lost time value of a multi-year carryforward noted |
| Missing the QCD AGI-lowering advantage | QCD screen compares income exclusion vs deduction, including IRMAA/NIIT effects |
| Asserting current-year limits/thresholds | All marked `[input current-year figure; verify with IRS/official source]` |
| Recommending a specific gift | Output is scenario comparison; the decision and substantiation route to the professional |
