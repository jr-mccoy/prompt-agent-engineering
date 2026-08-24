---
title: "Three-Statement Model Builder — Integrated, Balancing IS/BS/CF with Driver Assumptions"
category: finance/corporate-finance-fpa
description: "Build an integrated three-statement model where the income statement, balance sheet, and cash flow statement link and balance, with explicit driver assumptions, a debt/revolver plug, and disciplined handling of circular interest."
techniques:
  - NE-11
  - DS-02
  - QA-01
  - NE-10
  - ST-02
difficulty: advanced
tags:
  - three-statement-model
  - financial-modeling
  - fpa
  - balance-sheet
  - cash-flow
  - revolver
updated: "2026-06-08"
related_prompts:
  - domain-finance/corporate-finance-fpa/finance_driver_based_scenario_model.md
  - domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Build an integrated three-statement financial model in which the income statement (IS), balance sheet (BS), and cash flow statement (CF) are fully linked, the balance sheet balances in every forecast period, and a revolver/cash-sweep mechanism plugs any financing gap — while documenting every driver assumption and handling the circularity created by interest on debt that itself depends on cash flow.

---

## When to Use

- Standing up a forecast model for budgeting, fundraising, or a transaction (M&A, LBO, refinancing).
- Converting a single income-statement projection into a full integrated model that produces cash flow and a balancing balance sheet.
- Auditing an existing three-statement model that fails to balance or breaks when assumptions change.
- Preparing the operating model that feeds a DCF (`finance_dcf_model_builder.md`) or LBO (`finance_lbo_model_builder.md`).
- **Do not use** to produce audited financial statements, to replace a controller's close process, or as a substitute for a model built and tested in a live spreadsheet/system — this prompt produces the logic, structure, formulas, and a worked illustrative build, not a sign-off-ready file.

---

## Inputs / Context Required

```
<model_inputs>
Company name / entity:
Currency and reporting framework: [USD | EUR | ...] / [US GAAP | IFRS]
Forecast horizon: [e.g., 5 years annual, or 24 months]
Periodicity: [annual | quarterly | monthly]

HISTORICAL STATEMENTS (at least 1, ideally 3 periods — paste or transcribe):
- Income statement (revenue → net income)
- Balance sheet (full, balancing in history)
- Cash flow statement (indirect method preferred)

DRIVER ASSUMPTIONS (provide what is known; flag gaps):
- Revenue driver: [units × price | growth % | bookings → revenue | other]
- COGS / gross margin %:
- Operating expense drivers (fixed $ vs % of revenue):
- D&A: schedule or % of PP&E / capex
- Capex: $ or % of revenue; maintenance vs growth split
- Working capital: DSO (AR), DIO (inventory), DPO (payables), other accrual days
- Tax rate: [marginal/statutory; note NOLs]
- Debt: existing tranches (balance, rate, amortization), revolver limit and rate
- Dividends / distributions policy:
- Minimum cash balance (cash floor for revolver sweep):

CIRCULARITY PREFERENCE:
- Interest computed on: [opening balance | average balance] (average creates circularity)
- Circularity handling: [iterative | interest on opening balance to avoid circularity | copy-paste break]
</model_inputs>
```

---

## Constraints

### Must
- Link the three statements explicitly: net income flows from IS to the top of the CF (indirect method) and to retained earnings on the BS; CF ending cash ties to BS cash; D&A, capex, and working-capital changes reconcile between CF and BS.
- Drive the model from stated assumptions, not from forced/hardcoded outputs.
- Include a **balance-sheet balances check**: `Total Assets − Total Liabilities − Total Equity = 0` in every period; surface the check as a visible row.
- Implement a **financing plug** — a revolver draw when cash falls below the cash floor, and a cash sweep (revolver paydown) when excess cash exists.
- Address **circular interest**: interest depends on debt, debt depends on the cash shortfall, the cash shortfall depends on interest. State the chosen handling (iterative calculation, interest-on-opening-balance to break the loop, or a circularity switch) and its tradeoff.
- Build a cash flow statement using the indirect method, reconciling CFO + CFI + CFF to the change in cash on the BS.
- Present the model in a **base / upside / downside** range for the key drivers (NE-10), not a single point.
- Currency/framework flag: note any US GAAP vs IFRS treatment that changes the structure (e.g., operating-lease capitalization, interest paid classification in CFO vs CFF).

### Must Not
- Plug the balance sheet by forcing equity or by jamming the difference into an unlabeled line — the only legitimate plugs are cash and the revolver.
- Hardcode net income, ending cash, or retained earnings as inputs.
- Ignore the circularity (silently averaging the debt balance without a switch will produce a circular-reference error in a live model).
- Invent historical figures or fill working-capital days with "typical" numbers not supplied or derived from the user's history.
- Present the model as balancing without showing the balance check row.

---

## Instructions

1. **Set up the driver block (DS-02).** List every driver with its definition, unit, and source. Separate assumption cells (blue) from calculations conceptually. Derive working-capital days from history where possible:
   ```
   DSO = Accounts Receivable / Revenue × Days_in_period
   DIO = Inventory / COGS × Days_in_period
   DPO = Accounts Payable / COGS × Days_in_period
   ```

2. **Build the income statement.** Forecast each line from drivers:
   ```
   Revenue_t      = driver (units × price, or Revenue_t-1 × (1 + growth))
   COGS_t         = Revenue_t × (1 − gross_margin%)
   Gross Profit_t = Revenue_t − COGS_t
   OpEx_t         = fixed_$ + (Revenue_t × variable%)
   EBITDA_t       = Gross Profit_t − OpEx_t
   D&A_t          = from PP&E roll-forward (Step 5)
   EBIT_t         = EBITDA_t − D&A_t
   Interest_t     = from debt schedule (Step 6) — CIRCULAR if on average balance
   Pretax_t       = EBIT_t − Interest_t + Interest income_t
   Tax_t          = max(0, Pretax_t) × tax_rate   (apply NOL logic if relevant)
   Net Income_t   = Pretax_t − Tax_t
   ```

3. **Build the working-capital schedule.** Convert days back to balances:
   ```
   AR_t        = DSO × Revenue_t / Days
   Inventory_t = DIO × COGS_t / Days
   AP_t        = DPO × COGS_t / Days
   ΔNWC_t      = (AR_t − AR_t-1) + (Inv_t − Inv_t-1) − (AP_t − AP_t-1) + Δother
   ```

4. **Build the equity roll-forward.**
   ```
   Retained Earnings_t = Retained Earnings_t-1 + Net Income_t − Dividends_t
   Total Equity_t      = Paid-in Capital_t + Retained Earnings_t + Other (AOCI, etc.)
   ```

5. **Build the PP&E / D&A roll-forward.**
   ```
   PP&E_gross_t = PP&E_gross_t-1 + Capex_t
   D&A_t        = depreciation per schedule (or % of opening net PP&E)
   PP&E_net_t   = PP&E_net_t-1 + Capex_t − D&A_t
   ```

6. **Build the debt schedule and the revolver plug.** Compute pre-financing cash, then size the revolver:
   ```
   Cash before revolver_t = Beginning Cash_t + CFO_t + CFI_t + CFF_excl_revolver_t
   Cash shortfall_t       = max(0, Minimum Cash − Cash before revolver_t)
   Revolver draw_t        = Cash shortfall_t
   Cash sweep (paydown)_t = min(Revolver balance_t-1,
                                max(0, Cash before revolver_t − Minimum Cash))
   Revolver balance_t     = Revolver balance_t-1 + Revolver draw_t − Cash sweep_t
   Interest_t             = Σ(tranche rate × balance) + revolver rate × revolver balance
   ```
   State the balance convention (opening vs average) and the circularity handling explicitly.

7. **Build the cash flow statement (indirect).**
   ```
   CFO_t = Net Income_t + D&A_t ± non-cash items − ΔNWC_t
   CFI_t = −Capex_t ± asset sales / acquisitions
   CFF_t = ΔDebt_t + Revolver Δ_t − Dividends_t ± equity issuance/buyback
   Ending Cash_t = Beginning Cash_t + CFO_t + CFI_t + CFF_t
   ```

8. **Assemble the balance sheet and run the check.**
   ```
   Cash_t (from CF) | AR_t | Inventory_t | PP&E_net_t | other assets
   AP_t | accrued | Debt_t | Revolver_t | other liabilities
   Equity_t (from roll-forward)
   BALANCE CHECK_t = Total Assets_t − (Total Liabilities_t + Total Equity_t)   → must = 0
   ```

9. **Handle circularity (QA-01 + state the switch).** If interest is on average balance, the loop is: interest → net income → cash → revolver → debt → interest. Offer three resolutions and pick one: (a) enable iterative calculation with a circularity ON/OFF switch and a hardcode-break cell; (b) compute interest on the opening balance to remove the loop entirely (small accuracy cost); (c) one-pass copy-paste of the debt balance. Default recommendation: opening-balance interest for robustness unless precision is required.

10. **Run scenarios (NE-10).** Toggle the key drivers (growth, margin, capex, DSO) to base/upside/downside and confirm the balance check holds and the revolver behaves (draws in downside, sweeps in upside).

11. **Verification pass (QA-01).** Re-derive ending cash two ways (from CF and from the BS roll); confirm they tie. Confirm retained earnings ties to cumulative net income less dividends. Confirm the balance check is zero in every period and every scenario.

---

## Output Format

```
## Three-Statement Model — [Entity]   (illustrative figures below)
Currency: USD | Framework: US GAAP | Horizon: FY1–FY5 | Circularity: interest on opening balance

### Driver Assumptions
| Driver              | FY1   | FY2   | FY3   | Basis / Source            |
|---------------------|-------|-------|-------|---------------------------|
| Revenue growth %    | 12%   | 10%   | 8%    | mgmt plan (illustrative)  |
| Gross margin %      | 55%   | 55%   | 56%   | 3-yr hist avg             |
| OpEx % of revenue   | 38%   | 37%   | 36%   | hist + leverage           |
| Capex % of revenue  | 6%    | 5%    | 5%    | maintenance + growth      |
| DSO / DIO / DPO     | 55/40/35 | ...| ...   | derived from history      |
| Tax rate            | 25%   | 25%   | 25%   | statutory                 |

### Income Statement (illustrative, $M)
| Line          | FY1  | FY2  | FY3  |
|---------------|------|------|------|
| Revenue       | 112  | 123  | 133  |
| COGS          | (50) | (55) | (59) |
| Gross Profit  | 62   | 68   | 74   |
| OpEx          | (43) | (46) | (48) |
| EBITDA        | 19   | 22   | 26   |
| D&A           | (7)  | (8)  | (8)  |
| EBIT          | 12   | 14   | 18   |
| Interest      | (3)  | (3)  | (2)  |
| Pretax        | 9    | 11   | 16   |
| Tax           | (2)  | (3)  | (4)  |
| Net Income    | 7    | 8    | 12   |

### Cash Flow (illustrative, $M)
| Line              | FY1  | FY2  | FY3  |
|-------------------|------|------|------|
| Net Income        | 7    | 8    | 12   |
| + D&A             | 7    | 8    | 8    |
| − ΔNWC            | (4)  | (3)  | (2)  |
| CFO               | 10   | 13   | 18   |
| − Capex           | (7)  | (6)  | (7)  |
| CFI               | (7)  | (6)  | (7)  |
| ΔDebt / Revolver  | (1)  | (2)  | (3)  |
| − Dividends       | 0    | 0    | 0    |
| CFF               | (1)  | (2)  | (3)  |
| Net Δ Cash        | 2    | 5    | 8    |

### Balance Sheet Check (illustrative)
| Check               | FY1 | FY2 | FY3 |
|---------------------|-----|-----|-----|
| Total Assets        | 180 | 188 | 201 |
| Total Liab + Equity | 180 | 188 | 201 |
| BALANCE CHECK       | 0   | 0   | 0   |  ✓

### Revolver Behavior by Scenario
| Scenario  | Driver delta             | Peak Revolver | Balance check |
|-----------|--------------------------|---------------|---------------|
| Base      | as above                 | $4M           | 0 ✓           |
| Upside    | +3pt growth, +1pt margin | $0 (sweep)    | 0 ✓           |
| Downside  | −5pt growth, −2pt margin | $14M          | 0 ✓           |

### Circularity Note
Interest computed on opening debt balance to avoid a circular reference; if average-balance
precision is required, enable iterative calculation with a circularity ON/OFF switch and a
hardcode-break cell. State the choice in the model documentation.
```

---

## Verification

- [ ] Net income flows from IS to CF and to retained earnings on the BS.
- [ ] Ending cash on the CF equals cash on the BS in every period.
- [ ] D&A, capex, and working-capital changes reconcile between CF and BS roll-forwards.
- [ ] Balance check = 0 in every period and every scenario.
- [ ] Only cash and the revolver act as plugs; equity is never forced.
- [ ] Revolver draws when cash < floor; cash sweep pays it down when excess cash exists.
- [ ] Circularity handling stated, with its accuracy tradeoff.
- [ ] No hardcoded net income, ending cash, or retained earnings.
- [ ] US GAAP vs IFRS structural differences noted where relevant.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Claiming the model "balances" without proof | Show the explicit balance-check row (Assets − Liab − Equity = 0) in every period and scenario |
| Hiding a plug in an unlabeled line | Only cash and the revolver may plug; any other balancing entry is an error to be located |
| Silently averaging debt balances (circular-ref error in a live model) | State the circularity handling and its tradeoff; default to opening-balance interest unless precision demanded |
| Treating illustrative output numbers as real | All Output Format figures are labeled illustrative; real builds trace every cell to a stated input or history |
| Forcing equity to make it balance | Retained earnings = prior RE + NI − dividends; never overridden to balance |
| Assuming working-capital days when not supplied | Derive DSO/DIO/DPO from history or flag the gap; do not insert "typical" days |
