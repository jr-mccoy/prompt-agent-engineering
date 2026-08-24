---
title: "Multi-Year Tax Projection — Marginal/Effective Rate Modeling Across Income & Deduction Scenarios"
category: finance/tax-planning
description: "Build a multi-year tax projection that models federal and state liability across income, deduction, and timing scenarios — with marginal vs. effective rate math, bracket-fill visibility, AMT/NIIT/phaseout interactions, and year-over-year smoothing opportunities."
techniques:
  - NE-11
  - NE-10
  - DS-02
  - QA-01
  - OC-04
difficulty: intermediate
tags:
  - tax-projection
  - marginal-rate
  - effective-rate
  - multi-year
  - bracket-fill
  - amt
  - niit
updated: "2026-06-08"
related_prompts:
  - domain-finance/tax-planning/finance_capital_gains_harvesting_analysis.md
  - domain-finance/tax-planning/finance_retirement_account_tax_optimization.md
  - domain-finance/personal-finance-planning/finance_tax_aware_withdrawal_sequencing.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not tax, legal, or accounting advice. Tax rules change and depend on individual circumstances; filing, estimated-payment, and reliance decisions must be made with a qualified tax professional (CPA / EA / tax attorney).**

**Verify all brackets, standard-deduction amounts, AMT exemption/phaseout, NIIT and phaseout thresholds against current tax law as of the date of use and the applicable federal and state jurisdiction. These change annually.**

## Objective

Build an auditable multi-year (typically 3–5 year) tax projection that shows the full computation chain — gross income → adjustments → deductions → taxable income → tax by bracket → credits → additional taxes (AMT/NIIT) → total liability and effective rate — under multiple income/deduction/timing scenarios, surfacing where income "fills" brackets and where smoothing across years reduces total multi-year tax.

## When to Use

- Planning around a known income spike or trough (bonus, business sale, sabbatical, retirement year).
- Deciding whether to accelerate or defer income/deductions across a year boundary.
- Estimating quarterly tax payments and avoiding underpayment exposure.
- Sizing Roth conversions, harvesting, or charitable bunching against available bracket room (links to sibling prompts).
- Stress-testing a plan against AMT, NIIT, and deduction/credit phaseouts.

## Inputs / Context Required

```
<tax_projection_inputs>
Taxpayer profile:
- Filing status; dependents; ages (for credits/RMD relevance)
- State of residence (and any part-year/multistate flags)
- Projection horizon: ___ years (Year 1 = ____)

Per-year income (provide for each projection year, by scenario where it varies):
- Wages / W-2; self-employment income; pass-through (K-1) income
- Interest, ordinary dividends, qualified dividends
- Short-term and long-term capital gains
- Retirement distributions (pre-tax), Social Security, pension
- Other (rental, royalties, etc.)

Deductions / adjustments per year:
- Itemized components (SALT, mortgage interest, charitable, medical) vs. standard
- Above-the-line adjustments (HSA, SE tax 1/2, retirement contributions)
- Credits expected (child/dependent, education, energy, etc.)

Current-year parameters (USER-SUPPLIED — do not assume):
- Federal ordinary brackets and standard deduction [input; verify]
- LTCG/qualified-dividend rate breakpoints [input; verify]
- AMT exemption, phaseout, 26%/28% breakpoint [input; verify]
- NIIT rate (3.8%) and MAGI threshold [input; verify]
- Additional Medicare 0.9% threshold [input; verify]
- SALT cap, phaseout ranges for relevant credits/deductions [input; verify]
- State brackets / flat rate [input; verify]
</tax_projection_inputs>
```

## Constraints

### Must
- Show the bracket-by-bracket tax computation for each year — not just a blended rate (NE-11).
- Report BOTH marginal rate (rate on the next dollar) and effective rate (total tax ÷ total income) for each year.
- Run at least three scenarios (NE-10): e.g., base, income-acceleration, income-deferral — or low/expected/high.
- Compute AMT in parallel with regular tax and report the higher; flag years where AMT binds.
- Compute NIIT and Additional Medicare tax where MAGI/wage thresholds are exceeded.
- Flag deduction/credit phaseouts triggered by income level in each scenario.
- Sum total multi-year tax per scenario so smoothing trade-offs are visible (a strategy can lower one year but raise lifetime tax).
- Carry a jurisdiction flag; compute state tax separately and note interaction (e.g., SALT cap, state treatment of cap gains).

### Must Not
- Assert specific current-year brackets, standard deduction, AMT exemption, or NIIT thresholds from memory.
- Collapse marginal and effective rate into one number, or describe a bracket as taxing all income at that rate.
- Recommend a filing position; frame as projected scenarios for professional review.
- Ignore AMT, NIIT, or phaseouts when income is high enough to trigger them.
- Present single-year savings without the multi-year total.

## Instructions

**Step 1 — Build the per-year income stack and classify each income type.** Separate ordinary income from preferential-rate income (LTCG/qualified dividends), because they stack and are taxed at different schedules.

**Step 2 — Compute taxable income.**
```
Total income          = Σ all income items
AGI                   = Total income − above-the-line adjustments
Deduction taken       = max(standard, itemized after SALT cap & limits)
Taxable income        = AGI − deduction − QBI deduction (if applicable)
Split: ordinary taxable income | preferential-rate taxable income
```

**Step 3 — Compute regular tax with explicit bracket fill.**
```
For each ordinary bracket [lo, hi] at rate r:
  income in bracket   = max(0, min(taxable ordinary income, hi) − lo)
  tax in bracket      = income in bracket × r
Ordinary tax          = Σ tax in bracket
Preferential tax: stack LTCG/QD on top of ordinary income; apply 0/15/20% breakpoints [verify]
Regular tax (pre-credit) = ordinary tax + preferential tax
Marginal rate = rate of the bracket the last ordinary dollar lands in
Effective rate = total tax / total income
```

**Step 4 — Compute AMT in parallel.**
```
AMTI                  = taxable income + AMT preference/adjustment items (state tax addback, ISO bargain element, etc.)
AMT base              = AMTI − AMT exemption (exemption phases out above threshold) [verify]
Tentative minimum tax = 26% × base up to breakpoint + 28% × excess [verify]
AMT due               = max(0, TMT − regular tax)
Flag year if AMT > 0 (AMT binds)
```

**Step 5 — Compute additional taxes & phaseouts.**
```
NIIT = 3.8% × min(net investment income, MAGI − threshold) [verify]
Additional Medicare = 0.9% × (wages+SE income over threshold) [verify]
Phaseout check: for each income-sensitive credit/deduction, compute the reduced amount at this scenario's income
```

**Step 6 — Assemble total liability and the multi-year view.**
```
Total tax (year) = max(regular tax, TMT via AMT) − credits + NIIT + Add'l Medicare + state tax
Multi-year total per scenario = Σ total tax across horizon
```

**Step 7 — Identify smoothing opportunities (OC-04 conditional logic).**
- Where does a year leave unused room below the next bracket / NIIT threshold / IRMAA tier? (room available to fill)
- Where does a year spill into a higher bracket, AMT, NIIT, or a phaseout? (income worth deferring)
- Compare lifetime total tax of acceleration vs. deferral, not just the single-year delta.

**Step 8 — Verification pass (QA-01).** Recompute one year's bracket-fill total independently; confirm effective rate = total tax / total income; confirm AMT = max(0, TMT − regular).

## Output Format

### Assumptions & Parameters
[All user-supplied current-year figures, dated, with jurisdiction]

### Per-Year Computation (each scenario)

| Line | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Total income | | | |
| AGI | | | |
| Deduction (std/itemized) | | | |
| Taxable income | | | |
| Ordinary tax (bracket fill) | | | |
| Preferential-rate tax | | | |
| AMT due (if binds) | | | |
| NIIT | | | |
| Add'l Medicare | | | |
| Credits | | | |
| State tax | | | |
| **Total tax** | | | |
| Marginal rate | | | |
| Effective rate | | | |

### Scenario Summary

| Scenario | Yr1 tax | Yr2 tax | Yr3 tax | Multi-year total | AMT years | Phaseouts triggered |
|---|---|---|---|---|---|---|
| Base | | | | | | |
| Acceleration | | | | | | |
| Deferral | | | | | | |

### Smoothing Opportunities
[Step 7 — bracket/threshold room, spillover years, lifetime-tax comparison]

## Verification

- [ ] Bracket-by-bracket computation shown; no flat-rate shortcut.
- [ ] Marginal AND effective rate reported per year.
- [ ] All current-year parameters user-supplied or marked `[input; verify]`.
- [ ] AMT computed in parallel; binding years flagged.
- [ ] NIIT and Additional Medicare applied where thresholds exceeded.
- [ ] Phaseouts evaluated at each scenario's income.
- [ ] Multi-year total computed per scenario (not just single-year deltas).
- [ ] State tax computed separately with jurisdiction flag.
- [ ] Independent recomputation of one year confirms the totals.
- [ ] Disclaimer present; filing/estimated payments routed to professional.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Describing a tax bracket as taxing all income at that rate | Always show bracket fill and report marginal ≠ effective rate |
| Single-year savings sold as the win | Report the multi-year total; a strategy can cut Year 1 but raise lifetime tax |
| Ignoring AMT on high-deduction/ISO years | Compute AMT in parallel every year; flag binding years |
| Missing NIIT / Additional Medicare | Compute both whenever MAGI/wage thresholds are crossed |
| Assuming deductions/credits are fixed | Re-evaluate phaseouts at each scenario's income level |
| Asserting current-year figures from memory | All brackets/thresholds must be user-supplied or `[input; verify]` |
| Anchoring on a target effective rate | Effective rate is an output, not a goal; the lever is bracket/threshold room across years |
