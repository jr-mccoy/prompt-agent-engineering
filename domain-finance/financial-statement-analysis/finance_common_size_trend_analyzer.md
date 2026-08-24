---
title: "Common-Size and Multi-Period Trend Analyzer"
category: finance/financial-statement-analysis
description: "Convert financial statements to common-size format and perform multi-period trend analysis, flagging directional shifts, inflection points, and structural changes with driver attribution."
techniques:
  - NE-11
  - DS-04
  - DS-02
  - QA-01
  - CM-01
difficulty: intermediate
tags:
  - financial-statements
  - trend-analysis
  - common-size
  - income-statement
  - balance-sheet
updated: "2026-06-08"
related_prompts:
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/financial-statement-analysis/finance_quality_of_earnings_review.md
  - domain-finance/financial-statement-analysis/finance_dupont_decomposition.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Convert two or more periods of income statement, balance sheet, and/or cash flow statement data into common-size format, compute period-over-period and compounded growth rates, and produce a structured narrative identifying directional shifts, inflection points, and structural margin or mix changes requiring further investigation.

---

## When to Use

- Comparing a company's cost structure or balance-sheet composition across periods (2–10 years).
- Screening for structural margin deterioration or improvement before deeper ratio or quality-of-earnings work.
- Benchmarking a company's common-size profile against a peer or industry composite (when peer data is provided).
- Building the "historical context" section of an investment memo, credit memo, or management presentation.
- **Do not use** as a substitute for quality-of-earnings analysis (revenue recognition timing, accruals) — use `finance_quality_of_earnings_review.md` for that.

---

## Inputs / Context Required

Paste the following between the delimiters below. The more complete the data, the richer the output.

```
<financial_data>
Company name and ticker (if public):
Reporting currency and unit (e.g., USD millions):
Accounting framework: US GAAP | IFRS | Other
Fiscal year end:

INCOME STATEMENT (provide at minimum 3 periods; 5+ preferred):
[Paste or transcribe line items with period labels as columns]

BALANCE SHEET (same periods):
[Paste or transcribe]

CASH FLOW STATEMENT (same periods, if available):
[Paste or transcribe]

Peer/industry benchmarks (optional):
[If available, paste a representative peer common-size profile or industry median]

Context notes (optional):
[Acquisitions, divestitures, accounting-standard changes, restatements, segment changes]
</financial_data>
```

---

## Constraints

### Must
- Show the common-size formula explicitly for every base used:
  - Income statement: `Line item % = Line item ÷ Net Revenue × 100`
  - Balance sheet — assets side: `Line item % = Line item ÷ Total Assets × 100`
  - Balance sheet — liabilities & equity: `Line item % = Line item ÷ Total Assets × 100` (same base for comparability)
  - Cash flow: `Line item % = Line item ÷ Net Revenue × 100` (or ÷ Operating Cash Flow for the investing/financing section — state which base)
- Compute period-over-period percentage change: `Δ% = (Current − Prior) ÷ |Prior| × 100`
- Compute CAGR where ≥ 3 periods: `CAGR = (End Value ÷ Start Value)^(1 ÷ n) − 1`
- Flag every line item that moves more than a defined threshold in a single period (suggest 200 bps for margin lines, 10% for absolute revenue/asset lines — adjust if user specifies otherwise).
- Distinguish between mix effects and rate effects when margin shifts are present (e.g., gross margin decline could be product-mix shift vs. input-cost increase vs. pricing pressure).
- Note US GAAP vs. IFRS differences where they affect line-item comparability (e.g., IFRS allows interest paid in CFO or CFF; GAAP locks interest paid in CFO).
- If data spans an accounting-standard change or restatement, flag the discontinuity explicitly and do not mechanically compute YoY growth across the break.
- All stated numbers must trace to the user-supplied data. Do not interpolate or impute missing periods.

### Must Not
- Invent line items, period values, or benchmarks not in the supplied data.
- Present a common-size figure without showing its numerator and base.
- Treat a single-period anomaly as a confirmed trend — require at least two consecutive periods to call a direction.
- Assign causation without user-supplied evidence (state "consistent with" or "may reflect" rather than "caused by").
- Omit a material line item (>5% of revenue or assets in any period) from the output tables.

---

## Instructions

1. **Confirm inputs and set baselines.**
   - Verify the accounting framework and flag any framework-switching across periods.
   - Identify the anchor period (earliest) and terminal period (most recent).
   - Note any structural discontinuities: M&A, divestitures, restatements, segment changes, standard adoptions. Mark the relevant column(s) with `[†]` and explain in a footnote.

2. **Build common-size income statement.**
   - Create a table: rows = line items, columns = periods + common-size % per period.
   - Base = Net Revenue. If net revenue includes excise taxes or pass-through items, note and normalize.
   - Flag all items with single-period moves > 200 bps.

3. **Build common-size balance sheet.**
   - Base = Total Assets for both sides. Present assets and liabilities/equity sections.
   - Flag composition shifts in working capital, long-term debt, and equity accounts.

4. **Build common-size cash flow statement (if provided).**
   - Base = Net Revenue for the full statement.
   - Highlight trends in CFO/Revenue, Capex/Revenue, FCF/Revenue (define FCF = CFO − Capex).

5. **Compute growth rates.**
   - Period-over-period % change for each line item.
   - CAGR (full period) for: Revenue, Gross Profit, EBIT/Operating Income, Net Income, Total Assets, Total Debt.
   - Present in a summary growth table.

6. **Identify inflection points and directional shifts.**
   - Scan for reversals: where a multi-period trend changes direction. Highlight these.
   - Scan for acceleration or deceleration in growth rates.
   - Scan for convergence or divergence between revenue growth and cost growth.

7. **Attribute and interpret key moves.**
   - For each flagged item, offer a structured hypothesis: "Gross margin contracted 310 bps in FY23, consistent with [raw material cost increase / lower-margin product mix / pricing pressure] — confirm against segment data and MD&A."
   - Apply the **anchoring-bias check**: avoid explaining every move as a variant of the most recent macro theme. State alternative hypotheses.

8. **Compare to peer/benchmark (if data provided).**
   - Side-by-side common-size comparison for the most recent period.
   - Flag where the subject deviates > 300 bps from the peer median on key margin lines.

9. **Verification pass (QA-01).** Before finalizing:
   - Recompute at least three common-size figures manually to confirm arithmetic.
   - Confirm that income statement common-size percentages sum correctly (COGS + Gross Profit = 100%; SG&A + D&A + EBIT + Other = EBIT line, etc.).
   - Confirm balance sheet balances (Assets = Liabilities + Equity) in each period.

---

## Output Format

```
## Common-Size and Trend Analysis — [Company Name]
Periods: [FY__ through FY__] | Framework: [US GAAP / IFRS] | Currency: [USD millions]
Prepared: [date] | Data source: user-supplied

---

### Section 1: Common-Size Income Statement

| Line Item              | FY[n-2]  | %    | FY[n-1]  | %    | FY[n]    | %    | CAGR   |
|------------------------|----------|------|----------|------|----------|------|--------|
| Net Revenue            | 1,000    | 100% | 1,150    | 100% | 1,320    | 100% | +14.9% |
| Cost of Goods Sold     | 620      | 62.0%| 730      | 63.5%| 858      | 65.0%| +17.7% |
| **Gross Profit**       | **380**  |**38.0%**|**420**|**36.5%**|**462**|**35.0%**|**+10.2%**|
| SG&A                   | 190      | 19.0%| 218      | 18.9%| 251      | 19.0%| +14.9% |
| D&A (if shown)         | 50       | 5.0% | 55       | 4.8% | 60       | 4.5% | +9.5%  |
| **EBIT / Op. Income**  | **140**  |**14.0%**|**147**|**12.8%**|**151**|**11.4%**|**+3.9%**|
| Interest Expense       | (18)     | (1.8%)| (22)   | (1.9%)| (28)   | (2.1%)|        |
| Pre-Tax Income         | 122      | 12.2%| 125      | 10.9%| 123      | 9.3% |        |
| Tax Expense            | 30       | 3.0% | 31       | 2.7% | 32       | 2.4% |        |
| **Net Income**         | **92**   |**9.2%**|**94**|**8.2%**|**91**|**6.9%**|**-0.5%**|

**Flagged moves (>200 bps single-period):**
- COGS %: +150 bps FY[n-1]→FY[n] → gross margin compression; +150 bps prior year → trend, not anomaly
- EBIT %: −140 bps FY[n-1]→FY[n] (operating deleverage on SG&A fixed component)

---

### Section 2: Common-Size Balance Sheet

| Line Item                  | FY[n-2]  | %    | FY[n-1]  | %    | FY[n]    | %    |
|----------------------------|----------|------|----------|------|----------|------|
| Cash & Equivalents         | 80       | 8.0% | 95       | 7.9% | 70       | 5.3% |
| Accounts Receivable        | 110      | 11.0%| 135      | 11.3%| 175      | 13.3%|
| Inventory                  | 95       | 9.5% | 120      | 10.0%| 145      | 11.0%|
| **Total Current Assets**   | **320**  |**32.0%**| ... | ...  | ...  | ...  |
| PP&E, net                  | 450      | 45.0%| 470      | 39.2%| 490      | 37.1%|
| Goodwill & Intangibles     | 200      | 20.0%| 210      | 17.5%| 210      | 15.9%|
| **Total Assets**           | **1,000**|**100%**|**1,200**|**100%**|**1,320**|**100%**|
| Accounts Payable           | 85       | 8.5% | 100      | 8.3% | 120      | 9.1% |
| Short-Term Debt            | 40       | 4.0% | 55       | 4.6% | 90       | 6.8% |
| **Total Current Liabilities**| 160   |16.0% | ...      | ...  | ...      | ...  |
| Long-Term Debt             | 200      | 20.0%| 240      | 20.0%| 310      | 23.5%|
| **Total Equity**           | **520**  |**52.0%**|**540**|**45.0%**|**480**|**36.4%**|

**Flagged moves:**
- AR %: +200 bps over two years → receivables growing faster than revenue; test DSO
- Short-term debt %: +280 bps in FY[n] — investigate refinancing risk, maturity schedule
- Equity %: declining — leverage is building; cross-reference with Debt/EBITDA ratio

---

### Section 3: Growth Rate Summary

| Metric           | FY[n-2]→[n-1] | FY[n-1]→[n] | Full-Period CAGR |
|------------------|----------------|-------------|-----------------|
| Net Revenue      | +15.0%         | +14.8%      | +14.9%          |
| Gross Profit     | +10.5%         | +10.0%      | +10.2%          |
| EBIT             | +5.0%          | +2.7%       | +3.9%           |
| Net Income       | +2.2%          | −3.2%       | −0.5%           |
| Total Assets     | +20.0%         | +10.0%      | +14.9%          |
| Total Debt       | +27.5%         | +28.1%      | +27.8%          |

**Key observation:** Revenue growth is healthy but earnings growth has decoupled (EBIT CAGR 3.9% vs. Revenue 14.9%). Debt growth (27.8% CAGR) outpaces asset growth (14.9%) → increasing leverage.

---

### Section 4: Inflection Points and Structural Observations

1. **Gross margin compression (multi-period, −300 bps total):** Consistent with [rising input costs / product mix shift toward lower-margin SKUs / pricing pressure]. Requires confirmation against segment or MD&A disclosure.

2. **EBIT margin deceleration sharper than gross margin:** SG&A holding steady in % terms, but interest burden growing — operating deleverage is financial, not operational.

3. **Working capital buildup:** AR and inventory both growing faster than revenue. Possible drivers: longer payment terms to customers, inventory build ahead of demand, or collection issues. Test via CCC analysis (`finance_working_capital_analysis.md`).

4. **Capital structure shift:** Equity declining as % of assets while debt grows — signals either leverage-funded growth or buybacks. Confirm via cash flow from financing.

---

### Section 5: Peer Comparison (if data provided)

| Metric (FY[n])   | Subject | Peer Median | Δ vs. Peer |
|------------------|---------|-------------|------------|
| Gross Margin %   | 35.0%   | 38.5%       | −350 bps ▼ |
| EBIT Margin %    | 11.4%   | 13.2%       | −180 bps ▼ |
| SG&A %           | 19.0%   | 18.1%       | +90 bps ▲  |
| Debt / Assets %  | 30.3%   | 22.0%       | +830 bps ▲ |

---

### Section 6: Analyst Notes and Follow-On Questions

- [ ] Confirm COGS drivers with segment/product disclosure
- [ ] Run DSO, DIO, DPO to explain working-capital trends
- [ ] Stress test the growing debt load under rate/revenue scenarios
- [ ] Check MD&A for management commentary on margin compression
- [ ] Verify whether any period includes an acquisition that distorts trend
```

---

## Verification

- [ ] Every common-size % has a visible numerator, denominator, and result.
- [ ] Income statement: revenue line = 100% in every period.
- [ ] Balance sheet: Total Assets = sum of components; Assets = Liabilities + Equity in each period.
- [ ] No period-over-period growth computed across a restatement or accounting-change break without a footnote.
- [ ] Flagged moves verified: each one states the bps change and the direction.
- [ ] CAGR formula applied correctly: `(End ÷ Start)^(1/n) − 1`; n = number of intervals, not periods.
- [ ] No benchmark figure cited that was not in the user-supplied data.
- [ ] All hypotheses stated as "consistent with" or "may reflect," not as confirmed causes.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Calling a one-period anomaly a "trend" | Require ≥ 2 consecutive periods moving in the same direction before calling a trend |
| Attributing margin compression to a single cause | Always offer ≥ 2 alternative drivers and note which requires corroboration |
| Computing YoY growth across a restatement break | Flag the break; suppress or footnote the growth calculation across it |
| CAGR sign errors when base is negative | If the start or end value is negative, CAGR is undefined; note this and use absolute ΔΔΔΔ instead |
| Treating peer deviation as a problem | Deviation from peer could reflect a deliberate strategic choice; state "deviation" not "underperformance" unless context confirms the latter |
| Missing a material line due to table truncation | Check: any line >5% of revenue or assets in any period must appear in the table |
