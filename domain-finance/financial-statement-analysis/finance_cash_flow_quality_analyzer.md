---
title: "Cash Flow Quality Analyzer"
category: finance/financial-statement-analysis
description: "Decompose operating, investing, and financing cash flows, reconcile CFO to net income, identify non-cash items and working-capital movements, and test free cash flow durability across base and stress scenarios."
techniques:
  - NE-11
  - DS-04
  - QA-01
  - NE-10
  - RT-02
difficulty: intermediate
tags:
  - cash-flow
  - free-cash-flow
  - fcf
  - operating-cash-flow
  - working-capital
updated: "2026-06-08"
related_prompts:
  - domain-finance/financial-statement-analysis/finance_quality_of_earnings_review.md
  - domain-finance/financial-statement-analysis/finance_working_capital_analysis.md
  - domain-finance/financial-statement-analysis/finance_liquidity_solvency_stress_check.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Decompose the statement of cash flows into its operating, investing, and financing components; reconcile CFO to reported net income; isolate non-cash add-backs and working-capital drivers; define and compute free cash flow under multiple definitions; and stress-test FCF durability against revenue, margin, and capex shocks to assess whether the business generates or consumes cash through its operating cycle.

---

## When to Use

- Credit analysis: verifying whether EBITDA converts to cash before covenant testing.
- Equity research: testing whether earnings-based valuation is supported by actual cash generation.
- M&A diligence: adjusting for working-capital targets and normalized capex.
- FP&A / treasury: understanding sources and uses of cash ahead of a financing decision.
- **Do not use** without the actual statement of cash flows — do not reconstruct CFO from accrual-basis income statement alone, as the reconciling items are the core of the analysis.

---

## Inputs / Context Required

```
<cash_flow_data>
Company name / ticker:
Periods: [recommend 3–5 years]
Accounting framework: US GAAP | IFRS
Method: Direct | Indirect (most filers use indirect)

STATEMENT OF CASH FLOWS (paste multi-period; use column format):
[All line items from CFO, CFI, CFF sections, including opening/closing cash]

INCOME STATEMENT (same periods):
[At minimum: Revenue, Gross Profit, EBIT, Net Income]

BALANCE SHEET (working capital section, same periods):
[Accounts receivable, inventory, other current assets, accounts payable, accrued liabilities, deferred revenue]

CONTEXT:
- Capex breakdown (maintenance vs. growth) if disclosed
- Capitalized software or customer acquisition costs (if in CFI)
- Major non-recurring cash items (litigation payments, acquisition costs paid)
- Lease treatment: operating vs. finance leases (ASC 842 / IFRS 16); cash paid for operating leases shows in CFO under both frameworks
- Industry and business model (asset-heavy manufacturing vs. asset-light SaaS, etc.)
</cash_flow_data>
```

---

## Constraints

### Must
- Compute all of the following FCF definitions and state the formula for each:
  - **Levered FCF** = CFO − Total Capex
  - **Unlevered FCF (FCFF)** = EBIT × (1 − Tax Rate) + D&A − ΔWorking Capital − Total Capex
  - **Owner Earnings FCF** = Net Income + D&A − Maintenance Capex ± ΔWorking Capital (Buffett-style; requires maintenance capex estimate)
  - **Adjusted FCF** = Levered FCF − Capitalized software/CAC (if management capitalizes operating costs)
- Show the CFO-to-Net-Income bridge in a step-by-step table.
- Separate maintenance capex from growth capex where disclosed; where not disclosed, apply the most conservative assumption and state it.
- Under IFRS: note that interest paid and dividends received may appear in CFO or CFF/CFI depending on policy; adjust comparisons accordingly.
- Compute FCF yield if market cap or enterprise value is provided: FCF Yield = Levered FCF ÷ Market Cap.
- Apply three scenarios (NE-10): **Base** (as reported), **Stress** (revenue down X%, capex normalized), **Normalized** (strip non-recurring cash items, normalize working capital).
- State the **recency-bias risk**: if the most recent period is unusually strong or weak, flag it and use a multi-year average for durability conclusions.

### Must Not
- Use EBITDA as a proxy for cash flow without computing the actual CFO-to-EBITDA gap.
- Estimate maintenance capex from thin air — use management disclosure, depreciation as a proxy, or peer data; in all cases state the source and the limitation.
- Call FCF "high quality" if it is driven primarily by working-capital releases (inventory/AR liquidation) that are not sustainable.
- Report only the most recent year — FCF analysis requires a minimum of three periods to assess durability.
- Confuse cash paid for operating leases (GAAP: in CFO; IFRS: policy choice) with debt repayment; flag the treatment.

---

## Instructions

1. **Map the cash flow statement structure.**
   - Identify whether the filer uses the indirect method (start with net income, add non-cash items, then WC changes) or direct method (rare; show gross cash receipts and payments).
   - Under indirect method, verify the reconciliation logic: Net Income → CFO must account for all non-cash items and WC movements.
   - Flag any unusually large or unexplained reconciling items.

2. **Build the CFO-to-Net Income bridge.**
   - Tabulate: Net Income → + D&A → + SBC → + Amortization of intangibles → + Deferred taxes → + Other non-cash items → ± Working Capital Changes → = CFO.
   - Compute the CFO / Net Income ratio for each period.
   - Compute the D&A / Capex ratio: if > 1.0x, depreciation exceeds reinvestment (potential under-investment signal); if < 1.0x, growing asset base or capital-intensive growth.

3. **Decompose working capital movements.**
   - Break down: ΔAR, ΔInventory, ΔOther Current Assets, ΔAP, ΔAccrued Liabilities, ΔDeferred Revenue.
   - Classify each as: structural driver (business model change), cyclical driver (seasonal), or one-time driver (credit-term change, collection push at year-end).
   - Compute: NE-11 formula — Operating WC = AR + Inventory + Other Current Assets − AP − Accrued Liabilities (exclude cash, short-term debt, current portion of LTD, deferred revenue). Flag if WC / Revenue is trending up (WC is consuming cash) or down (WC is releasing cash).

4. **Compute and reconcile free cash flow.**
   - Compute all FCF definitions listed in Constraints.
   - Build a reconciliation table from Net Income to each FCF definition.
   - If management reports a custom "Free Cash Flow," reconcile it to Levered FCF and flag any deductions they omit (e.g., excluding acquisition capex).

5. **Decompose investing and financing cash flows.**
   - CFI: separate recurring capex from acquisitions, investments, divestitures. Flag large one-time CFI items.
   - CFF: decompose into debt issuance/repayment, equity issuance/repurchase, dividends. Assess whether net CFF is sustainably funded by CFO or requires external capital.
   - Compute: **Net Debt Change** = Net borrowings − Debt repayments. Is the company levering up or deleveraging?

6. **Test FCF durability with scenarios (NE-10).**

   | Scenario | Assumption | Adjusted CFO | Capex | Levered FCF |
   |---|---|---|---|---|
   | As Reported | Actual | — | — | — |
   | Normalized | Strip WC one-timers, normalize capex to avg 3-yr | — | — | — |
   | Stress | Revenue −15%, margin −200 bps, capex held flat | — | — | — |

7. **Identify FCF sustainability drivers.**
   - Is FCF growing because of genuine operating cash generation, or because of: (a) working-capital liquidation, (b) capex deferral, (c) favorable timing of large cash items?
   - Compute FCF as % of revenue and as % of EBITDA over the full period.
   - Flag if FCF-to-EBITDA conversion ratio < 40% in a non-capital-intensive business (typical range 50–80% for healthy companies).

8. **Verification pass (QA-01).**
   - Recompute Levered FCF = CFO − Capex from raw figures in the supplied statements.
   - Confirm that the CFO-to-Net Income bridge items sum to match the reported difference.
   - Confirm that beginning + CFO + CFI + CFF = ending cash balance (or flag if not, as this indicates a mis-paste).

---

## Output Format

```
## Cash Flow Quality Analysis — [Company Name]
Periods: [FY__ through FY__] | Framework: [US GAAP / IFRS] | Method: Indirect
Prepared: [date] | Data: user-supplied

---

### Section 1: CFO-to-Net Income Bridge

| Item                          | FY[n-2] | FY[n-1] | FY[n]  |
|-------------------------------|---------|---------|--------|
| Net Income                    | 92      | 94      | 91     |
| + Depreciation & Amortization | 50      | 55      | 60     |
| + Stock-based compensation    | 22      | 28      | 35     |
| + Deferred taxes              | 5       | 3       | (2)    |
| + Other non-cash items        | 3       | 2       | 4      |
| ± Working capital changes     | (15)    | (22)    | (48)   |
|   of which: ΔAR               | (8)     | (14)    | (32)   |
|   of which: ΔInventory        | (5)     | (6)     | (10)   |
|   of which: ΔAP               | (2)     | (2)     | (6)    |
| **CFO (reported)**            | **157** | **160** | **140**|
| CFO / Net Income (x)          | 1.71x   | 1.70x   | 1.54x  |

**D&A / Capex (x):** 0.91 → 0.88 → 0.83 (declining — growing capex base)

---

### Section 2: Free Cash Flow — Multiple Definitions

**Levered FCF = CFO − Total Capex**
Formula: $140M − $72M = **$68M** (FY[n])

| FCF Definition     | Formula                                      | FY[n-2] | FY[n-1] | FY[n]  |
|--------------------|----------------------------------------------|---------|---------|--------|
| Levered FCF        | CFO − Capex                                  | 102     | 95      | 68     |
| FCFF               | EBIT(1−t) + D&A − ΔWC − Capex               | 118     | 110     | 82     |
| Adjusted FCF       | Levered FCF − Capitalized software/CAC       | 74      | 52      | 2      |
| FCF / Revenue (%)  |                                              | 10.2%   | 8.3%    | 5.2%   |
| FCF / EBITDA (%)   |                                              | 53%     | 46%     | 32%    |

**⚠ FCF/EBITDA declining to 32%: below healthy range for this industry (est. 50–70%). Primary driver: working capital consumption and rising capitalized costs.**

---

### Section 3: Working Capital Analysis

| WC Driver        | FY[n-2] | FY[n-1] | FY[n]  | Trend  | Classification |
|------------------|---------|---------|--------|--------|----------------|
| ΔAR (cash use)   | (8)     | (14)    | (32)   | ↑ worsening | Structural/investigate |
| ΔInventory       | (5)     | (6)     | (10)   | ↑ gradual | Monitor |
| ΔAP (benefit)    | 3       | 4       | 8      | ↑ improving | Structural (vendor terms) |
| Net WC impact    | (10)    | (16)    | (34)   | ↑ consuming | |

**AR surge ($32M cash use in FY[n]) is the primary FCF headwind.** Consistent with collection delays or aggressive year-end revenue recognition. Investigate AR aging.

---

### Section 4: CFI and CFF Decomposition

| CFI / CFF Item                | FY[n-2] | FY[n-1] | FY[n]  |
|-------------------------------|---------|---------|--------|
| Capex (maintenance est.)      | (35)    | (38)    | (42)   |
| Capex (growth est.)           | (20)    | (27)    | (30)   |
| Acquisitions                  | 0       | (85)    | 0      |
| **Total CFI**                 | **(55)**| **(150)**| **(72)**|
| Net debt issuance / (repay.)  | 20      | 85      | 70     |
| Share buybacks                | (15)    | (10)    | (5)    |
| Dividends paid                | (12)    | (12)    | (12)   |
| **Total CFF**                 | **(7)** | **63**  | **53** |

**Net debt raised FY[n]: $70M.** Company is funding WC consumption and growth capex with debt. CFO alone insufficient to cover capex + dividends.

---

### Section 5: Durability Scenarios

| Scenario      | Revenue | Margin Adj. | Capex | CFO est. | Levered FCF | FCF/Rev |
|---------------|---------|-------------|-------|----------|-------------|---------|
| As Reported   | $1,320M | —           | $72M  | $140M    | $68M        | 5.2%    |
| Normalized    | $1,320M | +WC strip   | $65M  | $172M    | $107M       | 8.1%    |
| Stress (−15% rev)| $1,122M | −200bps  | $72M  | $95M     | $23M        | 2.0%    |
| Severe (−25% rev)| $990M  | −400bps  | $72M  | $55M     | ($17M)      | neg.    |

**Under a moderate stress scenario, FCF remains positive but thin. Severe scenario produces negative FCF; at current capex + dividend run-rate, the company would require external financing.**

---

### Section 6: Summary Assessment

**FCF Quality: Moderate (3/5)**

| Factor                     | Assessment |
|----------------------------|------------|
| CFO conversion of earnings | Declining (1.54x vs. 1.71x; still above 1.0x) |
| WC trend                   | Deteriorating; AR the primary concern |
| Capex sustainability       | Growth-oriented; D&A/Capex < 1.0x — reinvestment positive |
| Financing dependence       | Elevated; net debt raised 3 consecutive years |
| FCF durability             | Positive in base; stressed in mild downturn |

**Key risks:** AR buildup, declining FCF/EBITDA conversion, and rising leverage from debt-funded operations. Validate with AR aging, customer payment terms, and capex project review.
```

---

## Verification

- [ ] CFO-to-Net Income bridge items sum to match reported difference between Net Income and CFO.
- [ ] Levered FCF = CFO − Capex, computed from raw figures in the statement.
- [ ] Opening cash + CFO + CFI + CFF = closing cash (within rounding); if not, flag as a data integrity issue.
- [ ] IFRS classification of interest paid / received noted if applicable.
- [ ] Each FCF definition has its formula stated before the result.
- [ ] Scenario assumptions are internally consistent (e.g., revenue decline flows through to reduced tax, not just revenue).
- [ ] No maintenance capex estimate presented without stating the source (management disclosure / depreciation proxy / peer data).
- [ ] Recency-bias flag applied if the most recent period is materially better or worse than the trailing average.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Calling a positive CFO "high quality" when WC changes dominate | Decompose WC; if WC release > 50% of CFO, flag as potentially unsustainable |
| Using EBITDA as CFO | Always compute the actual CFO-to-EBITDA gap; never substitute |
| Treating declining capex as positive | Capex decline could signal under-investment, not efficiency; check D&A/Capex and age of asset base |
| Confusing operating-lease payments with debt service | Under ASC 842 / IFRS 16, operating-lease payments appear in CFO; financing-lease payments in CFF — do not double-count as debt |
| Accepting management's FCF definition without reconciling | Always reconcile to Levered FCF; flag any items management excludes (e.g., acquisition capex) |
| Over-normalizing to make FCF look better | Every normalization must be directionally conservative, not optimistic; state each adjustment's directional impact |
