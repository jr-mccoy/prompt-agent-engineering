---
title: "DCF Model Auditor — Methodology, Assumption Reasonableness, and Sensitivity Review"
category: finance/valuation
description: "Audit an existing DCF model for methodological soundness, assumption reasonableness, input-sensitivity errors, and logical consistency — producing a ranked finding log and corrective action items."
techniques:
  - QA-01
  - QA-02
  - NE-11
  - AG-02
  - DS-02
difficulty: advanced
tags:
  - dcf
  - valuation
  - model-audit
  - assumption-review
  - sensitivity
  - financial-modeling
updated: "2026-06-08"
related_prompts:
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/valuation/finance_terminal_value_sanity_check.md
  - domain-finance/valuation/finance_wacc_builder.md
  - domain-finance/valuation/finance_valuation_sensitivity_scenario.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Conduct a systematic, adversarial audit of an existing discounted cash flow model — examining methodology, individual assumptions, internal consistency, and sensitivity handling — and produce a ranked finding log that distinguishes fatal flaws from material concerns from best-practice gaps.

## When to Use

- Pre-investment-committee review of a DCF prepared by an analyst or counterparty
- Fairness-opinion or transaction-support review requiring an independent check
- Quality-control pass before a board or management presentation
- CFA study or training exercise examining a model for common errors
- Challenging a sell-side or buy-side DCF embedded in a research report or deal memo

## Inputs / Context Required

Supply the full model (or a structured summary); auditor findings will be bounded to what is provided. Missing sections are flagged as gaps.

**Model materials**
- Projection tables (income statement, free cash flow, all explicit-period years)
- WACC build (all components with stated sources)
- Terminal value calculation (method used, inputs)
- Equity-value bridge (EV → equity value → per share)
- Assumption register (if one exists)
- Sensitivity or scenario analysis (if any)

**Context**
- Company name and industry
- Date the model was prepared (to assess rate/market inputs for that date)
- Accounting framework (US GAAP / IFRS)
- Purpose of the model (investment decision, fairness, internal planning, etc.)
- Auditor's target: full audit, or focus on specific area (e.g., WACC only, terminal value only)

## Constraints

### Must
- Evaluate every WACC component against reasonable market-rate benchmarks for the stated model date; flag components that appear stale or unsourced.
- Test the WACC > g condition mathematically; flag if violated.
- Check the FCF formula used (FCFF vs. FCFE) for correctness and consistency with the discount rate applied.
- Calculate the TV-as-%-of-EV ratio; mandate additional scrutiny if >75%.
- Check internal consistency of scenarios: growth rates, margins, and capex assumptions must be coherent within each scenario.
- Rank every finding as: **Critical** (mathematical error or assumption outside defensible range), **Material** (meaningful valuation impact, questionable method), or **Minor** (best-practice gap, disclosure improvement).
- For each Critical and Material finding, quantify the directional impact on the DCF output where calculable.

### Must Not
- Invent substitute inputs; flag what is wrong and state what correct inputs should look like without fabricating specific numbers.
- Pass over an undisclosed assumption as if it were a stated fact.
- Conclude "the model is correct" in the absence of a complete inputs disclosure.
- Treat the audit as confirmation of the model's conclusion; maintain AG-02 skeptical stance throughout.

## Instructions

**Step 1 — Reconstruct the FCFF / FCFE formula and check correctness**

Identify the FCF formula embedded in the model. Compare to canonical forms:

```
FCFF = EBIT × (1 − Tax Rate) + D&A − ΔWorking Capital − Capex
     = Net Income + D&A + Interest × (1 − t) − ΔWC − Capex

FCFE = Net Income + D&A − ΔWorking Capital − Capex + Net Borrowing
```

Common errors to detect:
- Using EBITDA as a cash-flow proxy (omits capex and WC)
- Wrong sign on ΔWC (WC increase is a cash outflow, not inflow)
- Omitting taxes on EBIT (arriving at pre-tax NOPAT)
- Mixing FCFF and FCFE components then discounting at WACC

**Step 2 — Audit the WACC build**

For each component, apply the test shown:

| Component | Test |
|---|---|
| Risk-free rate | Is it the current (model date) sovereign yield? Not a trailing average. |
| Beta | Is it levered at the subject company's actual D/E, not a raw peer beta? |
| ERP | Is the source identified (Damodaran, Duff & Phelps, or stated)? Not an arbitrary round number. |
| Size / country premia | Are they justified by company size / domicile? Not applied generically. |
| Cost of debt | Is it the YTM on actual debt, not the coupon rate on old debt? |
| Capital weights | Are they market-value weights, not book-value? |
| Tax rate on debt shield | Is it the marginal (not effective) tax rate? |

Recompute WACC from stated inputs. If model's stated WACC ≠ recomputed WACC, flag as Critical.

**Step 3 — Review projection-period assumptions for reasonableness**

For each driver, test:
1. **Revenue growth:** Does the exit-period growth rate exceed the stated terminal growth rate? (creates discontinuity). Does it imply market share above 100% in the TAM? Is it consistent with the analyst's cited industry source?
2. **EBITDA margin trajectory:** Is a margin improvement documented with an operational mechanism (scale leverage, mix shift, cost reduction)? Or is it asserted without basis?
3. **D&A vs. Capex relationship:** Sustainable long-run D&A ≈ maintenance Capex for stable businesses. If D&A >> Capex persistently, the model implies no capital replacement — flag.
4. **Working capital:** Does the WC-as-%-revenue ratio change, and is the direction plausible (i.e., rapid growth typically requires WC investment)?
5. **Tax rate:** Is there an unexplained step-change in the tax rate? NOL utilization or rate changes should be disclosed.

**Step 4 — Audit the terminal value**

```
TV_PGM = FCFF_terminal × (1 + g) / (WACC − g)
TV_Exit = EBITDA_terminal × Exit Multiple
Implied g from Exit = WACC − FCFF_terminal / TV_Exit
```

Tests:
- Is WACC > g? If not: Critical finding, undefined / negative TV.
- Is g ≤ long-run nominal GDP growth for the relevant economy? Growth above GDP implies the company eventually dominates the global economy.
- Does the exit multiple have a stated reference? Peer median, long-run average, or comps are defensible; an arbitrary round number is not.
- Do the two TV methods agree within 20%? Material divergence signals a structural assumption conflict — identify it.
- What is TV as % of EV? Flag thresholds: >75% requires mandatory sensitivity; >90% is a Critical flag on projection-period quality.

**Step 5 — Check the equity bridge**

```
Equity Value = Enterprise Value − Net Debt − Minority Interest + Non-Operating Assets
Equity Value / Share = Equity Value / Diluted Shares Outstanding
```

Tests:
- Is net debt the balance-sheet figure at the valuation date (not a projected future date)?
- Are operating leases, pension deficits, and contingent liabilities included in net debt where material?
- Does diluted share count include in-the-money options, warrants, and convertibles (treasury-stock method)?
- Are non-operating assets (e.g., minority stakes, surplus real estate) disclosed and treated consistently?

**Step 6 — Assess scenario and sensitivity completeness**

- Are base / bull / bear scenarios present? If only base, flag as Material.
- Are scenario assumptions internally consistent (bull revenue cannot pair with bear margins if they are correlated)?
- Is there a sensitivity table on WACC and terminal growth rate at minimum?
- What is the break-even assumption (at which value does the model imply zero upside at current price)?

**Step 7 — Compile and rank findings**

For each finding:
- Assign severity: Critical / Material / Minor
- State the specific error or gap
- Quantify directional impact on equity value per share where calculable
- State the corrective action

**Step 8 — Adversarial stress-test of the audited model**

After identifying findings, apply pressure tests:
- Apply the most aggressive defensible correction to each Critical finding simultaneously — what is the resulting equity value range?
- What is the maximum plausible equity value using the most favorable end of defensible assumption ranges?
- Which single finding, if corrected, changes the investment decision most?

## Output Format

### Audit Summary

| Metric | Model States | Auditor Finds | Status |
|---|---|---|---|
| FCF method | FCFF / FCFE | [correct / error] | [Pass / Flag] |
| WACC (as stated) | [%] | [%] recomputed | [Pass / Flag] |
| Terminal growth rate | [%] | WACC − g = [%] | [Pass / Flag] |
| TV as % of EV | [%] | — | [Pass / Flag if >75%] |
| Scenarios present | Yes / No | — | [Pass / Flag] |
| Sensitivity table | Yes / No | — | [Pass / Flag] |

### Finding Log

| # | Area | Finding | Severity | Directional Impact | Corrective Action |
|---|---|---|---|---|---|
| 1 | WACC | Beta is raw peer average, not relevered | Critical | WACC understated ~[x]bps → EV overstated | Relever beta at subject D/E; recompute WACC |
| 2 | Terminal value | g (3.5%) exceeds long-run GDP assumption (2.5%) | Material | TV overstated ~[x]% | Reduce g to long-run nominal GDP; document basis |
| 3 | Projection | D&A > Capex in all years; implies no capital replacement | Material | FCF overstated; unsustainable | Split maintenance vs. growth capex; align D&A |
| 4 | Bridge | Diluted shares use basic count, exclude in-the-money options | Minor | EPS overstated [x]% | Apply treasury-stock method for diluted count |
| … | … | … | … | … | … |

### Corrected Valuation Range (applying Critical corrections only)

| | Bear | Base | Bull |
|---|---|---|---|
| Equity Value / Share (original model) | | | |
| Equity Value / Share (Critical fixes applied) | | | |
| Change ($) | | | |
| Change (%) | | | |

### Most Sensitive Finding

> [Name the single finding with the largest impact on equity value per share and quantify: "Correcting the beta relevering reduces equity value per share by approximately $X–$Y, or X–Y%, based on the model's own WACC sensitivity table."]

## Verification

- [ ] FCFF / FCFE formula reconstructed from model cells and compared to canonical formula; sign convention on ΔWC confirmed.
- [ ] WACC recomputed from stated components; any discrepancy between stated and recomputed WACC flagged Critical.
- [ ] Beta correctly relevered at subject company D/E ratio.
- [ ] Risk-free rate and ERP are sourced and dated to model preparation date.
- [ ] WACC > g verified mathematically in all scenarios; violation is Critical.
- [ ] TV% of EV calculated; >75% triggers mandatory sensitivity disclosure.
- [ ] Exit multiple for TV has a stated, defensible reference.
- [ ] Equity bridge checked: net debt at valuation date, diluted share count, minority interest, non-operating assets.
- [ ] All findings ranked Critical / Material / Minor; Critical findings have quantified directional impact.
- [ ] Adversarial correction applied to Critical findings to produce a corrected valuation range.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Flagging a defensible assumption as an error because it differs from the auditor's preference | Apply the test: is the assumption outside a reasonable range for this industry and date? Document the basis for the range before flagging. |
| Calling a model "correct" because no arithmetic errors were found | Methodological errors (e.g., book-value WACC weights, unsupported exit multiple) are material even when arithmetic is clean. |
| Quantifying the impact of a Minor finding with the same emphasis as a Critical finding | Severity ranks and impact columns must be clearly differentiated; Minor findings do not drive the corrected range. |
| Criticizing g without stating what a defensible g would be | Every Critical/Material finding must include a corrective action with a basis. |
| Treating a model without sensitivity analysis as automatically invalid | Absence of sensitivity is a Material gap, not necessarily a Critical error in the base case; rank it correctly. |
| Overprecision in the "corrected" range | Corrected values should be expressed as ranges ($X–$Y), acknowledging that multiple corrections interact non-linearly. |
