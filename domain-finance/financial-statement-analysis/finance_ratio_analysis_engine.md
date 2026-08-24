---
title: "Financial Ratio Analysis Engine"
category: finance/financial-statement-analysis
description: "Compute and interpret the full ratio set (liquidity, profitability, leverage, efficiency, valuation) with formulas shown, trend context, and peer/industry benchmarking."
techniques:
  - NE-11
  - DS-02
  - DS-04
  - QA-01
  - RT-02
difficulty: intermediate
tags:
  - ratio-analysis
  - financial-statements
  - liquidity
  - profitability
  - leverage
  - efficiency
  - valuation
updated: "2026-06-08"
related_prompts:
  - domain-finance/financial-statement-analysis/finance_dupont_decomposition.md
  - domain-finance/financial-statement-analysis/finance_common_size_trend_analyzer.md
  - domain-finance/financial-statement-analysis/finance_peer_benchmarking_builder.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or tax advice.*

## Objective

Compute the complete ratio set across five dimensions — liquidity, profitability, leverage, efficiency, and valuation — with each ratio showing its formula, inputs drawn from stated financials, calculated result, year-over-year trend, and interpretation against peer/industry context the user provides. Flag ratios that deviate materially from trend or peers and require deeper investigation.

## When to Use

- Initiating coverage of a company or sector
- Quarterly earnings review to track ratio trajectory
- Credit underwriting or covenant monitoring
- Investment screening before deeper thesis work
- Internal management review of financial health KPIs

## Inputs / Context Required

- **Financial statements:** Income statement, balance sheet, and cash flow statement for at least 2 periods (3 preferred for trend); specify reporting currency and period-end dates.
- **Accounting framework:** US GAAP or IFRS (affects lease treatment, goodwill impairment, revenue recognition timing — note differences where material).
- **Peer / industry benchmarks:** Provide at least one peer set or name the industry; if none available, state "no benchmarks provided" and the model will note ratios cannot be contextualized.
- **Share price and shares outstanding:** Required for valuation ratios; if unavailable, omit the valuation section.
- **Adjustments:** Any known non-recurring items, restructuring charges, or restatements to exclude.
- **Focus area (optional):** If only certain ratio groups are needed, specify.

## Constraints

### Must
- Show the formula in symbolic notation before each calculated ratio (NE-11).
- Derive every input from the stated financial data — cite the specific line item (e.g., "Net Income from IS, FY2024: $X").
- Flag when a ratio is not calculable due to missing inputs rather than estimating.
- Note accounting-framework differences where they affect ratio comparability (e.g., IFRS 16 operating lease capitalization inflates EBITDA-based leverage vs. pre-ASC-842 US GAAP treatment).
- Apply a disconfirming check: after computing ratios, explicitly test whether any individually strong ratio is contradicted by weakness in another dimension.
- Name the bias guardrail in the analysis: anchoring on the most recent period; require a full-cycle view.

### Must Not
- Invent peer benchmarks, industry medians, or index thresholds not supplied by the user.
- Present a ratio interpretation without the supporting calculation trace.
- Conclude a company is "healthy" or "distressed" based on a single ratio in isolation.
- Adjust financial figures without stating the adjustment and its rationale explicitly.

## Instructions

1. **Parse and organize inputs.** Extract each required line item from the stated financials and list it in a data table with source annotation (statement, line, period). Flag any line items needed but missing.

2. **Compute the liquidity ratio group.** For each ratio:
   - State the formula symbolically.
   - Substitute the extracted values.
   - Show the arithmetic result to two decimal places.
   - Note the year-over-year change (direction and magnitude).
   - Compare to peer benchmark if provided; flag if deviation > 20% of peer median.

   Ratios:
   - Current Ratio = Current Assets / Current Liabilities
   - Quick Ratio = (Cash + Short-Term Investments + Net Receivables) / Current Liabilities
   - Cash Ratio = (Cash + Cash Equivalents) / Current Liabilities
   - Operating Cash Flow Ratio = CFO / Current Liabilities

3. **Compute the profitability ratio group.**

   Ratios:
   - Gross Margin = Gross Profit / Revenue
   - Operating Margin = EBIT / Revenue
   - EBITDA Margin = EBITDA / Revenue  [note: EBITDA = EBIT + D&A]
   - Net Margin = Net Income / Revenue
   - Return on Assets (ROA) = Net Income / Average Total Assets
   - Return on Equity (ROE) = Net Income / Average Shareholders' Equity
   - Return on Invested Capital (ROIC) = NOPAT / Average Invested Capital
     where NOPAT = EBIT × (1 − Effective Tax Rate)
     and Invested Capital = Total Equity + Total Debt − Excess Cash

4. **Compute the leverage (solvency) ratio group.**

   Ratios:
   - Debt-to-Equity = Total Debt / Total Equity
   - Net Debt-to-EBITDA = (Total Debt − Cash) / EBITDA
   - Total Debt-to-Assets = Total Debt / Total Assets
   - Interest Coverage (EBIT/Interest Expense)
   - Fixed-Charge Coverage = (EBIT + Lease Payments) / (Interest Expense + Lease Payments)

5. **Compute the efficiency ratio group.**

   Ratios:
   - Asset Turnover = Revenue / Average Total Assets
   - Receivables Days (DSO) = (Accounts Receivable / Revenue) × 365
   - Inventory Days (DIO) = (Inventory / COGS) × 365
   - Payables Days (DPO) = (Accounts Payable / COGS) × 365
   - Cash Conversion Cycle (CCC) = DSO + DIO − DPO

6. **Compute the valuation ratio group** (requires share price input).

   Ratios:
   - Price-to-Earnings (P/E) = Share Price / Diluted EPS
   - EV/EBITDA = Enterprise Value / EBITDA
     where EV = Market Cap + Total Debt + Minority Interest − Cash
   - Price-to-Book (P/B) = Share Price / Book Value per Share
   - Price-to-Sales (P/S) = Market Cap / Revenue
   - Dividend Yield = Annual Dividend per Share / Share Price [if applicable]

7. **Synthesize across dimensions.** After computing all groups, write a cross-dimensional synthesis (3–5 sentences): identify the single most important concern, the strongest positive signal, and at least one ratio pair that appears to contradict each other. Apply the disconfirming check.

8. **Rank flags by materiality.** List up to five ratio flags in descending severity: [Critical / Elevated / Watch]. For each: ratio name, current value, benchmark/trend basis, and recommended follow-up.

## Output Format

```
## RATIO ANALYSIS: [Company Name] | [Period(s)] | [Framework: US GAAP / IFRS]

### Input Data Register
| Line Item             | Statement | Period(s)      | Value(s)   |
|-----------------------|-----------|----------------|------------|
| Revenue               | IS        | FY2023, FY2024 | $X, $Y     |
| ...                   | ...       | ...            | ...        |
| [FLAG] Missing item:  | —         | —              | Not provided — ratio [X] omitted |

---

### 1. Liquidity Ratios
| Ratio                  | Formula                                             | FY2024  | FY2023  | Δ YoY   | Peer Median | Flag?    |
|------------------------|-----------------------------------------------------|---------|---------|---------|-------------|----------|
| Current Ratio          | Current Assets / Current Liabilities                | X.XX    | X.XX    | ±X.XX   | X.XX        | [Watch]  |
| Quick Ratio            | (Cash + STI + Recv) / Current Liabilities           | X.XX    | X.XX    | ±X.XX   | X.XX        | —        |
| Cash Ratio             | Cash & Equiv / Current Liabilities                  | X.XX    | X.XX    | ±X.XX   | —           | —        |
| OCF Ratio              | CFO / Current Liabilities                           | X.XX    | X.XX    | ±X.XX   | —           | —        |
*Interpretation: [2–3 sentences on liquidity trend and peer gap]*

### 2. Profitability Ratios
| Ratio         | Formula                                  | FY2024 | FY2023 | Δ YoY | Peer | Flag? |
|---------------|------------------------------------------|--------|--------|-------|------|-------|
| Gross Margin  | Gross Profit / Revenue                   | XX.X%  | XX.X%  | ±Xpp  | XX%  | —     |
| Operating Margin | EBIT / Revenue                        | XX.X%  | XX.X%  | ±Xpp  | XX%  | —     |
| EBITDA Margin | (EBIT + D&A) / Revenue                   | XX.X%  | XX.X%  | ±Xpp  | XX%  | —     |
| Net Margin    | Net Income / Revenue                     | XX.X%  | XX.X%  | ±Xpp  | XX%  | —     |
| ROA           | Net Income / Avg Total Assets            | XX.X%  | XX.X%  | ±Xpp  | XX%  | —     |
| ROE           | Net Income / Avg Equity                  | XX.X%  | XX.X%  | ±Xpp  | XX%  | —     |
| ROIC          | NOPAT / Avg Invested Capital             | XX.X%  | XX.X%  | ±Xpp  | XX%  | —     |
*Interpretation: [2–3 sentences]*

### 3. Leverage Ratios
| Ratio                  | Formula                                          | FY2024 | FY2023 | Δ YoY | Peer | Flag? |
|------------------------|--------------------------------------------------|--------|--------|-------|------|-------|
| Debt/Equity            | Total Debt / Total Equity                        | X.Xx   | X.Xx   | ±X.Xx | X.Xx | —     |
| Net Debt/EBITDA        | (Total Debt − Cash) / EBITDA                     | X.Xx   | X.Xx   | ±X.Xx | X.Xx | —     |
| Total Debt/Assets      | Total Debt / Total Assets                        | XX.X%  | XX.X%  | ±Xpp  | XX%  | —     |
| Interest Coverage      | EBIT / Interest Expense                          | X.Xx   | X.Xx   | ±X.Xx | X.Xx | —     |
| Fixed-Charge Coverage  | (EBIT + Lease Pmts) / (Interest + Lease Pmts)   | X.Xx   | X.Xx   | ±X.Xx | —    | —     |
*Interpretation: [2–3 sentences]*

### 4. Efficiency Ratios
| Ratio           | Formula                              | FY2024  | FY2023  | Δ YoY   | Peer | Flag? |
|-----------------|--------------------------------------|---------|---------|---------|------|-------|
| Asset Turnover  | Revenue / Avg Total Assets           | X.Xx    | X.Xx    | ±X.Xx   | X.Xx | —     |
| DSO (days)      | (AR / Revenue) × 365                 | XX days | XX days | ±X days | XX   | —     |
| DIO (days)      | (Inventory / COGS) × 365             | XX days | XX days | ±X days | XX   | —     |
| DPO (days)      | (AP / COGS) × 365                    | XX days | XX days | ±X days | XX   | —     |
| CCC (days)      | DSO + DIO − DPO                      | XX days | XX days | ±X days | XX   | —     |
*Interpretation: [2–3 sentences]*

### 5. Valuation Ratios
| Ratio     | Formula                             | Current | Prior Period | Peer | Flag? |
|-----------|-------------------------------------|---------|--------------|------|-------|
| P/E       | Price / Diluted EPS                 | XX.Xx   | XX.Xx        | XX.Xx | —    |
| EV/EBITDA | EV / EBITDA                         | XX.Xx   | XX.Xx        | XX.Xx | —    |
| P/B       | Price / Book Value per Share        | XX.Xx   | XX.Xx        | XX.Xx | —    |
| P/S       | Mkt Cap / Revenue                   | XX.Xx   | XX.Xx        | XX.Xx | —    |
| Div Yield | Annual DPS / Price                  | X.X%    | X.X%         | X.X%  | —    |
*Interpretation: [2–3 sentences]*

---

### Cross-Dimensional Synthesis
[3–5 sentences: primary concern, strongest positive, contradicting ratio pair, disconfirming check result]

### Materiality-Ranked Flags
| Priority | Ratio | Value | Basis for Flag | Recommended Follow-Up |
|----------|-------|-------|----------------|-----------------------|
| 1. Critical   | ... | ... | ... | ... |
| 2. Elevated   | ... | ... | ... | ... |
| 3. Watch      | ... | ... | ... | ... |

### Accounting Framework Notes
[Note any GAAP/IFRS differences that affect ratio comparability for this company]
```

## Verification

- [ ] Every ratio shows its formula in symbolic form before the computed value.
- [ ] Every input value is cited to a specific financial statement line and period.
- [ ] No benchmark figures appear that were not provided by the user.
- [ ] Missing data is flagged with the ratio omitted — not estimated or assumed.
- [ ] Year-over-year delta is computed arithmetically, not approximated.
- [ ] Disconfirming check is performed: at least one contradicting signal is identified or confirmed absent.
- [ ] Accounting framework differences (GAAP vs. IFRS) noted where relevant.
- [ ] Cross-dimensional synthesis does not declare overall "health" from a single ratio.
- [ ] Flags are ranked by materiality, not listed arbitrarily.

## False-Positive Prevention

| Overclaim Risk | Guardrail |
|---|---|
| Declaring a company "financially healthy" because one ratio looks good | Require cross-dimensional review; a strong current ratio alongside deteriorating interest coverage is not health |
| Comparing ratios across GAAP and IFRS peers without adjustment | Flag the framework difference; note IFRS 16 lease capitalization, IFRS goodwill non-amortization vs. US GAAP as material distortions |
| Using single-period ratios to conclude trend | Trend requires at least two periods; flag if only one period provided |
| Treating industry "typical" ranges as authoritative thresholds | State that published ranges (e.g., current ratio > 2.0) are heuristics, not covenants; context determines adequacy |
| Normalizing for non-recurring items without user instruction | State the adjustment explicitly and label the resulting ratio "adjusted"; present the as-reported ratio separately |
| Interpreting a high P/E as overvaluation without growth context | High P/E may reflect high growth expectations; note this explicitly and defer to a fuller valuation analysis |
