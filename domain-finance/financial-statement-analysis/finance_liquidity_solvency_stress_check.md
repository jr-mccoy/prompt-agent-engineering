---
title: "Liquidity and Solvency Stress Check"
category: finance/financial-statement-analysis
description: "Stress-test a company's liquidity position and solvency against revenue, margin, and interest-rate shocks — incorporating Altman Z-Score awareness and a covenant-headroom projection under downside scenarios."
techniques:
  - NE-10
  - NE-11
  - QA-02
  - DS-02
  - RT-02
difficulty: intermediate
tags:
  - liquidity
  - solvency
  - stress-test
  - altman-z-score
  - covenants
updated: "2026-06-08"
related_prompts:
  - domain-finance/financial-statement-analysis/finance_cash_flow_quality_analyzer.md
  - domain-finance/financial-statement-analysis/finance_working_capital_analysis.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Assess a company's near-term liquidity and medium-term solvency by computing standard liquidity and leverage ratios, projecting cash runway under base and stressed scenarios, applying the Altman Z-Score as a solvency signal, and testing covenant headroom — with the goal of determining whether the company can service its obligations through a plausible adverse scenario.

---

## When to Use

- Credit analysis: annual or quarterly borrower review.
- Equity research: assessing downside risk and potential distress scenarios.
- M&A diligence: assessing whether the target has near-term funding risk.
- FP&A or treasury: testing whether the company can withstand a macro downturn.
- Early warning: proactive identification of covenant breach risk before it materializes.
- **Do not use** the Altman Z-Score as the sole solvency judgment — it is a screening tool with documented limitations for non-manufacturing, non-US, and financial companies. Treat it as one signal among several.

---

## Inputs / Context Required

```
<stress_data>
Company name / ticker:
Industry: [SIC or brief description; Altman Z-Score variant depends on this]
Most recent fiscal year end:
Accounting framework: US GAAP | IFRS

BALANCE SHEET (most recent period; prior year helpful):
- Cash and cash equivalents
- Short-term investments / marketable securities
- Accounts receivable, net
- Inventory (if applicable)
- Total current assets
- Total current liabilities (including current portion of LTD)
- Total Assets
- Total Liabilities
- Retained earnings / (accumulated deficit)
- Total Shareholders' Equity (book value)
- Short-term debt / current portion of long-term debt
- Long-term debt
- Total debt (short + long term)

INCOME STATEMENT (most recent fiscal year; prior year helpful):
- Net Revenue
- EBITDA (or EBIT + stated D&A)
- EBIT (Operating Income)
- Net Income
- Interest Expense (gross)
- Tax Expense

CASH FLOW (most recent period):
- Cash From Operations (CFO)
- Capital Expenditures
- Free Cash Flow (if reported; else compute as CFO − Capex)

DEBT / COVENANT DETAILS (paste from footnotes if available):
- Revolving credit facility: total capacity, drawn amount, termination date
- Term loan maturities
- Key financial covenants: [e.g., "Maximum Net Leverage Ratio: 4.0x"; "Minimum Interest Coverage: 2.5x"]
- Any covenant waivers or amendments in the last 12 months

MARKET DATA (optional, required for Altman Z-Score):
- Market capitalization (as of a stated date)
- Share price and shares outstanding

STRESS ASSUMPTIONS (user may customize; defaults stated below):
- Stress scenario revenue decline: default −20%
- Stress scenario EBITDA margin compression: default −300 bps
- Stress scenario interest rate increase: default +200 bps on floating-rate debt
- Severe scenario revenue decline: default −35%
</stress_data>
```

---

## Constraints

### Must
- Compute the following ratios with formulas shown:
  - Current Ratio = `Current Assets ÷ Current Liabilities`
  - Quick Ratio = `(Cash + Short-term investments + AR) ÷ Current Liabilities`
  - Cash Ratio = `Cash + Short-term investments ÷ Current Liabilities`
  - Net Debt = `Total Debt − Cash and cash equivalents`
  - Net Leverage = `Net Debt ÷ EBITDA`
  - Gross Leverage = `Total Debt ÷ EBITDA`
  - Interest Coverage (EBITDA) = `EBITDA ÷ Interest Expense`
  - Interest Coverage (EBIT) = `EBIT ÷ Interest Expense`
  - Debt-to-Assets = `Total Debt ÷ Total Assets`
  - Debt-to-Equity = `Total Debt ÷ Total Equity`
  - Debt-to-Capital = `Total Debt ÷ (Total Debt + Total Equity)`
- Apply **three scenarios** (NE-10): Base (as reported), Stress (moderate adverse), Severe (deep adverse). State all assumptions explicitly.
- Compute the **Altman Z-Score** where applicable:
  - For publicly traded manufacturing companies: Z' = 1.2X1 + 1.4X2 + 3.3X3 + 0.6X4 + 1.0X5
    - X1 = (Current Assets − Current Liabilities) ÷ Total Assets (Working Capital / Total Assets)
    - X2 = Retained Earnings ÷ Total Assets
    - X3 = EBIT ÷ Total Assets
    - X4 = Market Cap ÷ Book Value of Total Liabilities
    - X5 = Net Revenue ÷ Total Assets
    - Zones: Z' > 2.99 = Safe; 1.81–2.99 = Gray; < 1.81 = Distress
  - For private companies (Z'' model): replace X4 with Book Equity / Total Liabilities; adjusted thresholds: > 2.6 safe, 1.1–2.6 gray, < 1.1 distress.
  - For non-manufacturing companies: Z' can be applied but with lower reliability; flag this explicitly.
  - State the variant used and the limitation.
- Compute **cash runway**: months of operating expenses covered by current liquidity = `(Cash + Undrawn revolver capacity) ÷ (Monthly Cash Operating Expenses)`
  - Monthly Cash Operating Expenses ≈ (Revenue − EBITDA) ÷ 12 as an approximation (state this).
- Apply the **adversarial stress-test** (QA-02): "What is the most plausible scenario in which this company faces a liquidity crisis within 18 months?"
- Note US GAAP vs. IFRS: operating lease liabilities now appear on the balance sheet under both ASC 842 / IFRS 16; clarify whether stated debt figures include operating lease liabilities.

### Must Not
- Present the Altman Z-Score as a definitive prediction of default — it is a probabilistic screening tool calibrated on historical data; false positives and negatives exist.
- Apply the manufacturing-company Altman model without adjustment to financial services companies, REITs, or start-ups.
- Assume the revolving credit facility is fully available without checking for financial covenant restrictions on availability.
- Invent covenant terms not supplied by the user — if covenants are not provided, note the limitation.

---

## Instructions

1. **Compute base-case liquidity and leverage ratios.**
   - Apply all formulas listed in Constraints.
   - Flag any ratio that fails standard thresholds: Current Ratio < 1.0x, Quick Ratio < 0.5x, Interest Coverage < 2.0x, Net Leverage > 5.0x (thresholds are contextual — note industry norms).

2. **Compute the Altman Z-Score.**
   - Identify the correct variant (public manufacturing / private / non-manufacturing).
   - Compute each variable (X1–X5).
   - Compute Z-score and state the zone.
   - Note limitations for the specific company type.

3. **Estimate cash runway.**
   - Available liquidity = Cash + Cash equivalents + Undrawn revolving credit (if disclosed).
   - Monthly cash burn approximation = (Revenue − EBITDA) ÷ 12 (note: this approximates only operating costs, not debt service or capex).
   - Full cash runway = Available liquidity ÷ (Monthly cash burn + Monthly capex + Monthly debt service).
   - Note that this is an approximation; an actual 13-week cash flow model would be required for precision.

4. **Apply scenario stress tests (NE-10).**
   - For each scenario, re-estimate: Revenue, EBITDA, Interest Expense (if floating-rate), Net Debt (assuming FCF used to pay down or build debt).
   - Recompute: Net Leverage, Interest Coverage, Cash Balance at year-end.
   - Flag covenant breach in any scenario.

5. **Test covenant headroom (if covenants provided).**
   - For each disclosed covenant, compute headroom in the base case: `Headroom = Covenant Limit − Actual Metric` (or vice versa for minima).
   - Project forward under the stress scenario: does the company breach?
   - Compute the "cushion" in percentage terms: how much further could EBITDA decline before breach?

6. **Adversarial stress-test (QA-02).**
   - State the most plausible single-event or macro scenario that causes a liquidity crisis.
   - Example: "If revenue declines 25% and the revolver is frozen due to covenant breach, available liquidity drops to $X M — insufficient to cover debt service of $Y M over the next 12 months."

7. **Summary assessment.**
   - Assign an overall liquidity/solvency rating: **Strong / Adequate / Stressed / At Risk / Distressed**.
   - State the single most important watch variable.

8. **Verification pass (QA-01).**
   - Recompute Net Debt from stated figures.
   - Recompute Interest Coverage from EBITDA and Interest Expense.
   - Confirm Altman Z-Score arithmetic (each Xi and weighted sum).

---

## Output Format

```
## Liquidity and Solvency Stress Check — [Company Name]
Period: [FY__ or as of __] | Framework: [US GAAP / IFRS]
Industry: [stated] | Purpose: [credit review / equity research / internal]
Prepared: [date] | Data: user-supplied

---

### Section 1: Base-Case Ratios

**Liquidity**

| Ratio          | Formula                                        | Value  | Threshold  | Signal |
|----------------|------------------------------------------------|--------|------------|--------|
| Current Ratio  | Current Assets ÷ Current Liabilities           | 1.45x  | >1.5x pref | ⚠ Below |
| Quick Ratio    | (Cash+STI+AR) ÷ Current Liabilities            | 0.82x  | >1.0x pref | ⚠ Below |
| Cash Ratio     | (Cash+STI) ÷ Current Liabilities               | 0.30x  | >0.2x OK   | ✓      |
| Cash Runway    | Liquidity ÷ Monthly Op. Burn + Debt Service    | 14 mo  | >12 mo pref| ✓      |

**Solvency / Leverage**

| Ratio                | Formula                         | Value  | Threshold   | Signal |
|----------------------|---------------------------------|--------|-------------|--------|
| Net Debt             | Total Debt − Cash               | $560M  |             |        |
| Net Leverage         | Net Debt ÷ EBITDA               | 2.8x   | <3.5x typic | ✓      |
| Gross Leverage       | Total Debt ÷ EBITDA             | 3.1x   |             | ✓      |
| Interest Cov. (EBITDA)| EBITDA ÷ Interest Expense     | 8.3x   | >3.0x min   | ✓      |
| Interest Cov. (EBIT) | EBIT ÷ Interest Expense         | 5.4x   | >2.0x min   | ✓      |
| Debt / Assets        | Total Debt ÷ Total Assets       | 30.8%  |             | Moderate|
| Debt / Equity        | Total Debt ÷ Equity             | 85.4%  |             | Moderate|
| Debt / Capital       | Debt ÷ (Debt + Equity)          | 46.1%  | <50% typical| ✓      |

---

### Section 2: Altman Z-Score

**Variant applied:** [Public Manufacturing / Private / Non-manufacturing — state which and why]

Formulas:
- X1 = (Current Assets − Current Liabilities) ÷ Total Assets = WC/TA
- X2 = Retained Earnings ÷ Total Assets
- X3 = EBIT ÷ Total Assets
- X4 = Market Cap ÷ Book Value of Total Liabilities (public) OR Book Equity ÷ Total Liabilities (private)
- X5 = Net Revenue ÷ Total Assets

| Variable | Value  | Weight | Contribution |
|----------|--------|--------|--------------|
| X1       | 0.142  | 1.2    | 0.171        |
| X2       | 0.071  | 1.4    | 0.099        |
| X3       | 0.115  | 3.3    | 0.380        |
| X4       | 1.23   | 0.6    | 0.738        |
| X5       | 1.00   | 1.0    | 1.000        |
| **Z-Score** | — | — | **2.39**   |

**Zone: Gray (1.81–2.99)** — Not in immediate distress zone but not comfortably in safe zone. Monitoring warranted.

**Limitation:** This company is [non-manufacturing / private / financial services — as applicable]; the original Altman model was calibrated on manufacturing firms. Treat as a directional screening signal, not a precise probability of default.

---

### Section 3: Scenario Stress Tests

**Scenario Assumptions:**

| Parameter                   | Base    | Stress     | Severe      |
|-----------------------------|---------|------------|-------------|
| Revenue change              | —       | −20%       | −35%        |
| EBITDA margin compression   | —       | −300 bps   | −600 bps    |
| Rate increase (floating debt)| —      | +200 bps   | +200 bps    |
| Capex                       | $72M    | $72M (held)| $72M (held) |
| Rationale                   | As reported | Moderate recession | Severe sector shock |

**Scenario Results:**

| Metric                     | Base    | Stress  | Severe  |
|----------------------------|---------|---------|---------|
| Revenue ($M)               | 1,320   | 1,056   | 858     |
| EBITDA ($M)                | 231     | 169     | 105     |
| EBITDA Margin              | 17.5%   | 16.0%   | 12.2%   |
| Interest Expense ($M)      | 28      | 33 (+5 rate) | 33 |
| Interest Coverage (EBITDA) | 8.3x    | 5.1x    | 3.2x    |
| Net Leverage (x)           | 2.8x    | 3.9x ⚠  | 6.3x ⚠⚠|
| Covenant: Net Leverage ≤4.0x| ✓ 2.8x | ⚠ 3.9x  | ✗ BREACH 6.3x |
| Covenant: Coverage ≥2.5x   | ✓ 8.3x | ✓ 5.1x  | ✓ 3.2x  |
| Cash balance (yr-end est.) | $120M   | $65M    | ($18M) ⚠|
| Months cash runway         | 14      | 8       | <0 ⚠⚠  |

---

### Section 4: Covenant Headroom Analysis (Base Case)

| Covenant                     | Limit  | Actual | Headroom | EBITDA Decline to Breach |
|------------------------------|--------|--------|----------|--------------------------|
| Net Leverage ≤ 4.0x          | 4.0x   | 2.8x   | 1.2x     | −30% EBITDA decline       |
| Interest Coverage ≥ 2.5x     | 2.5x   | 8.3x   | 5.8x     | −70% EBITDA decline       |

**Net Leverage covenant is the binding constraint.** A 30% EBITDA decline would trigger breach — the stress scenario (−27% EBITDA decline) is close to the boundary.

---

### Section 5: Adversarial Stress Scenario

**Most plausible liquidity crisis path (18-month horizon):**
A 25% revenue decline (within the stress scenario range) combined with a covenant breach on the Net Leverage ratio would: (1) trigger a technical default allowing lenders to accelerate the term loan, (2) freeze revolver availability, and (3) leave the company with only $65M cash against $120M in accelerated maturities. This would require either an emergency equity raise at distressed terms or a covenant amendment/waiver. The probability is moderate if the macro environment deteriorates; the margin compression trend (EBIT −2.6 pp over two years) makes the company increasingly vulnerable.

**Disconfirming scenario:** If revenue stabilizes and management reduces capex by $20M (from $72M to $52M), stress-scenario FCF improves by ~$20M and covenant headroom widths. This is the key management lever to watch.

---

### Section 6: Overall Assessment

**Liquidity/Solvency Rating: Adequate (with stress risk)**

| Dimension             | Rating  | Key Finding |
|-----------------------|---------|-------------|
| Near-term liquidity   | Adequate | Current ratio slightly below 1.5x; 14-month runway |
| Interest service      | Strong  | 8.3x EBITDA coverage; well above minimums |
| Leverage              | Moderate | 2.8x Net Leverage; highest in peer set |
| Covenant cushion      | Thin    | Net Leverage covenant breached in severe scenario |
| Solvency (Altman)     | Gray zone | Z-Score 2.39; warrants monitoring |
| Trend                 | Deteriorating | Leverage rising, margins declining |

**Single most important watch variable:** Net Leverage covenant headroom — a further EBITDA decline of 30% triggers breach.
```

---

## Verification

- [ ] Net Debt = Total Debt − Cash, confirmed from stated figures.
- [ ] Net Leverage = Net Debt ÷ EBITDA, confirmed arithmetically.
- [ ] Interest Coverage computed from EBITDA ÷ Interest Expense and separately EBIT ÷ Interest Expense.
- [ ] Altman Z-Score: each Xi computed and weighted sum verified.
- [ ] Scenario EBITDA computed from stated revenue × scenario margin assumption.
- [ ] Covenant breach determination cross-checked against stated covenant limit and scenario output.
- [ ] Cash runway denominator stated as an approximation; full 13-week model flagged as the precise alternative.
- [ ] Altman variant stated and limitations noted for the specific company type.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Altman Z-Score as a default prediction | It is a screening signal; gray zone does not mean 50/50 default probability; state the zone and the limitation |
| Stress scenario treated as the base case | Scenarios represent plausible but not certain outcomes; always present base, stress, and severe side by side |
| Assuming full revolver availability | Revolvers often have financial covenant restrictions; state that availability may be reduced in a stress scenario |
| Concluding solvency is fine because interest coverage is high | High coverage and high leverage can coexist; coverage tests the income statement; leverage tests the balance sheet; a covenant breach can trigger acceleration even with positive cash flow |
| Including operating lease liabilities in Net Debt without noting the framework | Post-ASC 842 / IFRS 16, operating leases are on balance sheet; clarify whether stated debt includes or excludes them |
| EBITDA as a proxy for cash available for debt service | EBITDA ignores capex, taxes, and working-capital changes; always note the distinction |
