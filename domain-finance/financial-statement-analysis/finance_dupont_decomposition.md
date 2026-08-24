---
title: "DuPont ROE Decomposition"
category: finance/financial-statement-analysis
description: "Compute 3-step and 5-step DuPont ROE decompositions, attribute ROE changes to specific profit, efficiency, and leverage drivers, and produce a narrative interpretation with trend context."
techniques:
  - NE-11
  - DS-02
  - DS-04
  - QA-01
  - ST-02
difficulty: beginner
tags:
  - dupont
  - roe
  - return-on-equity
  - profitability
  - leverage
updated: "2026-06-08"
related_prompts:
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/financial-statement-analysis/finance_common_size_trend_analyzer.md
  - domain-finance/financial-statement-analysis/finance_peer_benchmarking_builder.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Decompose return on equity (ROE) using both the 3-step and 5-step DuPont frameworks, quantify the contribution of each driver (net profit margin, asset turnover, financial leverage; plus tax burden and interest burden in the 5-step), track the decomposition over multiple periods, and produce a plain-language narrative explaining what is causing ROE to rise, fall, or hold steady.

---

## When to Use

- Understanding *why* ROE is changing, not just *that* it is changing.
- Comparing ROE quality across companies (e.g., is Peer A's higher ROE from better operations or more leverage?).
- FP&A: explaining ROE trajectory to a CFO or board audience without requiring advanced financial background.
- Educational context: teaching financial statement analysis and the interplay between income statement and balance sheet.
- Screening: quickly diagnosing which of the three drivers is the primary ROE lever in a given company.
- **Do not use** as a standalone investment or credit signal — high ROE driven entirely by leverage requires a very different interpretation than ROE driven by high net margins.

---

## Inputs / Context Required

```
<dupont_data>
Company name:
Periods: [minimum 2; 3–5 preferred for trend]
Accounting framework: US GAAP | IFRS

INCOME STATEMENT (per period):
- Net Revenue (= Net Sales)
- EBT (Earnings Before Tax = Pre-Tax Income)
- EBIT (Earnings Before Interest and Tax = Operating Income)
- Net Income (after tax, after interest)
- Tax Expense

BALANCE SHEET (per period, end-of-period):
- Total Assets
- Total Equity (= Shareholders' Equity)

OPTIONAL (for richer context):
- Beginning-of-period Total Assets and Total Equity (for average-denominator versions)
- Peer ROE and its components for comparison
- Industry average ROE
</dupont_data>
```

---

## Constraints

### Must
- Show every formula explicitly before computing the result.
- Compute both the **3-Step DuPont** and the **5-Step DuPont** for every period provided.
- Use **average** denominators for asset turnover and equity multiplier where beginning-period data is available (average = (beginning + ending) ÷ 2); if beginning data is not provided, use ending-period values and note the limitation.
- Present a **period-over-period attribution table** showing how much of the change in ROE came from each component.
- Flag immediately if ROE is positive but the company reported a net loss — this indicates negative equity, which makes ROE arithmetically positive but economically meaningless; state this explicitly.
- Compute ROIC and ROA alongside ROE to provide context:
  - ROA = Net Income ÷ Average Total Assets
  - ROIC = NOPAT ÷ Invested Capital, where NOPAT = EBIT × (1 − Effective Tax Rate) and Invested Capital = Total Assets − Non-Interest-Bearing Current Liabilities (or = Total Equity + Total Debt − Cash, both definitions acceptable; state which is used)
- Include a brief glossary of each component for a non-specialist audience.

### Must Not
- Compute ROE as Net Income ÷ Ending Equity without flagging that this is an approximation — average equity is the preferred denominator.
- Present the 5-Step decomposition without explaining the tax-burden and interest-burden ratios in plain language.
- Omit the leverage analysis — a rising ROE that is entirely leverage-driven is a fundamentally different signal from one that is margin- or efficiency-driven.
- Invent any financial figures not supplied by the user.

---

## Instructions

1. **Define and compute 3-Step DuPont components.**

   **3-Step DuPont:**
   ```
   ROE = Net Profit Margin × Asset Turnover × Equity Multiplier

   Where:
   Net Profit Margin   = Net Income ÷ Net Revenue
   Asset Turnover      = Net Revenue ÷ Average Total Assets
   Equity Multiplier   = Average Total Assets ÷ Average Total Equity
   Check: ROE          = Net Income ÷ Average Total Equity
   ```

   Compute each component for each period. Verify that the product of the three components equals the directly computed ROE (within rounding).

2. **Define and compute 5-Step DuPont components.**

   **5-Step DuPont:**
   ```
   ROE = Tax Burden × Interest Burden × EBIT Margin × Asset Turnover × Equity Multiplier

   Where:
   Tax Burden        = Net Income ÷ EBT          (= 1 − Effective Tax Rate)
   Interest Burden   = EBT ÷ EBIT               (= 1 − Interest/EBIT; lower = more interest)
   EBIT Margin       = EBIT ÷ Net Revenue        (operating margin)
   Asset Turnover    = Net Revenue ÷ Average Total Assets
   Equity Multiplier = Average Total Assets ÷ Average Total Equity
   ```

   Verify: Tax Burden × Interest Burden = Net Income ÷ EBIT (= Net Profit Margin / EBIT Margin).
   Verify: product of all five = Net Income ÷ Average Total Equity = ROE.

3. **Build the period-over-period attribution table.**
   - For each period transition, compute the change in ROE (e.g., FY[n-1] to FY[n]).
   - For each of the three (or five) components, compute its "contribution" to the ROE change by holding all other components fixed at the prior-year level and varying only the one under examination. Sum the contributions (they will approximately equal the total ROE change; residual/interaction terms are small and should be noted).
   - Label each driver: growing margin, declining efficiency, increasing leverage, tax benefit, rising interest burden.

4. **Add ROIC and ROA context.**
   - ROA: is it growing or shrinking? Is ROE rising faster than ROA? If so, leverage is the driver.
   - ROIC: if ROIC > WACC, the company is creating value; if ROIC < WACC, it is destroying value. Note that WACC is not computable without additional data; flag if a cost-of-capital estimate is needed.
   - ROE vs. ROIC gap: a large gap indicates significant financial leverage. Quantify: `ROE − ROIC ≈ (ROIC − Net Cost of Debt) × Financial Leverage Effect`.

5. **Write the driver narrative.**
   - In 3–5 sentences, explain in plain language: what is the primary driver of the current ROE level and trend? Is this a high-quality or leverage-inflated ROE? What is the one most important thing to watch for the next period?

6. **Verification pass (QA-01).**
   - Confirm: 3-step product = directly computed ROE (within 0.1 percentage point).
   - Confirm: 5-step product = directly computed ROE (within 0.1 percentage point).
   - Confirm: attribution table contributions sum approximately to total ROE change.
   - Confirm: no figure in the output was not present in the user-supplied data.

---

## Output Format

```
## DuPont ROE Decomposition — [Company Name]
Periods: [FY__ through FY__] | Framework: [US GAAP / IFRS]
Denominator basis: Average equity / assets (or ending-period — state which)
Prepared: [date] | Data: user-supplied

---

### Component Glossary

| Component       | Definition                                  | What it tells you |
|-----------------|---------------------------------------------|-------------------|
| Net Profit Margin | Net Income ÷ Net Revenue                  | How much of each revenue dollar becomes profit |
| Asset Turnover  | Net Revenue ÷ Avg. Total Assets             | How efficiently assets generate revenue |
| Equity Multiplier | Avg. Total Assets ÷ Avg. Total Equity     | How much financial leverage is used |
| Tax Burden      | Net Income ÷ EBT                            | Proportion of pre-tax income retained after tax |
| Interest Burden | EBT ÷ EBIT                                  | Proportion of operating income retained after interest |
| EBIT Margin     | EBIT ÷ Net Revenue                          | Operating profitability before financing effects |

---

### 3-Step DuPont

Formulas:
- Net Profit Margin = Net Income ÷ Net Revenue
- Asset Turnover = Net Revenue ÷ Avg. Total Assets
- Equity Multiplier = Avg. Total Assets ÷ Avg. Total Equity
- ROE = Net Profit Margin × Asset Turnover × Equity Multiplier

| Component            | FY[n-2] | FY[n-1] | FY[n]  | Trend     |
|----------------------|---------|---------|--------|-----------|
| Net Revenue ($M)     | 1,000   | 1,150   | 1,320  |           |
| Net Income ($M)      | 92      | 94      | 91     |           |
| Avg. Total Assets    | 960     | 1,100   | 1,260  |           |
| Avg. Total Equity    | 515     | 530     | 510    |           |
| **Net Profit Margin**| **9.2%**| **8.2%**| **6.9%**| ↓ declining|
| **Asset Turnover**   | **1.04x**|**1.05x**|**1.05x**| → stable |
| **Equity Multiplier**| **1.86x**|**2.08x**|**2.47x**| ↑ rising |
| **ROE (3-step)**     | **17.8%**|**17.9%**|**17.9%**| → stable |
| ROE (direct check)   | 17.9%   | 17.7%   | 17.8%  | ✓ match   |

**Observation:** ROE appears stable, but this masks two opposing forces: net profit margin is declining while financial leverage is increasing. The margin decline is being fully offset by additional leverage.

---

### 5-Step DuPont

Additional Formulas:
- Tax Burden = Net Income ÷ EBT
- Interest Burden = EBT ÷ EBIT
- EBIT Margin = EBIT ÷ Net Revenue
- ROE = Tax Burden × Interest Burden × EBIT Margin × Asset Turnover × Equity Multiplier

| Component            | FY[n-2] | FY[n-1] | FY[n]  | Trend |
|----------------------|---------|---------|--------|-------|
| EBT ($M)             | 122     | 125     | 123    |       |
| EBIT ($M)            | 140     | 147     | 151    |       |
| **Tax Burden**       | **0.754**|**0.752**|**0.740**| ↓ slightly |
| **Interest Burden**  | **0.871**|**0.850**|**0.815**| ↓ declining |
| **EBIT Margin**      | **14.0%**|**12.8%**|**11.4%**| ↓ declining |
| **Asset Turnover**   | **1.04x**|**1.05x**|**1.05x**| → stable |
| **Equity Multiplier**| **1.86x**|**2.08x**|**2.47x**| ↑ rising |
| **ROE (5-step)**     | **17.8%**|**17.9%**|**17.8%**| → (stable) |
| 5-step check vs. direct ROE | ✓ | ✓ | ✓ | |

**5-step insight:** Interest burden is declining (more interest consumed from EBIT) as leverage rises. Tax burden also slightly declining. The equity multiplier is compensating for all three declining sub-drivers.

---

### Period-Over-Period Attribution: FY[n-1] → FY[n]

Change in ROE: 17.9% → 17.8% = −0.1 pp (approximately flat)

| Driver               | Direction | Contribution to ΔROE | Interpretation |
|----------------------|-----------|----------------------|----------------|
| Net Profit Margin    | ↓ −1.3 pp | −1.9 pp drag         | Primary headwind |
| Asset Turnover       | → flat    | ~0 pp                | Neutral |
| Equity Multiplier    | ↑ +0.39x  | +1.8 pp boost        | Offsetting margin decline |
| Residual/interaction | —         | ~0 pp                |                |
| **Net ROE change**   |           | **−0.1 pp**          | Margin decline offset by leverage |

---

### Return Metrics Comparison

| Metric    | FY[n-2] | FY[n-1] | FY[n]  | Signal |
|-----------|---------|---------|--------|--------|
| ROE       | 17.9%   | 17.7%   | 17.8%  | Stable (leverage-supported) |
| ROA       | 9.6%    | 8.5%    | 7.2%   | ↓ Declining — assets growing faster than income |
| ROIC (est.)| 14.2%  | 12.8%   | 11.1%  | ↓ Declining — watch vs. WACC |

**ROE–ROA gap widening: from 8.3 pp to 10.6 pp** — increasing leverage is responsible. ROE is becoming progressively more leverage-dependent.

---

### Narrative Interpretation

ROE has held near 18% over three years, but the underlying quality of that return has deteriorated. The net profit margin has declined 2.3 percentage points (from 9.2% to 6.9%), driven by operating margin compression (EBIT margin −2.6 pp) and rising interest expense (interest burden declining from 0.87x to 0.82x). Both drags are being fully offset by an expansion in financial leverage (equity multiplier +0.61x) as the company has used debt to fund growth.

The single most important watch point is ROA: at 7.2% and declining, if this rate drops below the company's cost of debt (estimate needed), incremental leverage will destroy equity value rather than create it. The current ROE stability is not a signal of improving fundamentals — it is a leverage-financed disguise for operating deterioration.

---

### ⚠ Interpretation Cautions

- ROE is not comparable across companies with very different leverage levels — always decompose before comparing.
- Negative equity makes ROE mathematically positive but economically misleading — always check equity sign.
- A rising equity multiplier may reflect share buybacks (reducing equity) as well as additional debt — check both components of equity change.
```

---

## Verification

- [ ] 3-step product (Margin × Turnover × Multiplier) equals directly computed ROE within 0.1 pp.
- [ ] 5-step product equals directly computed ROE within 0.1 pp.
- [ ] Attribution table contributions sum to approximately the total ROE change.
- [ ] Average denominators used where beginning-period data was provided; otherwise ending-period noted.
- [ ] ROA and ROIC computed from the same supplied figures.
- [ ] No figures in the output not traceable to user-supplied data.
- [ ] Narrative explicitly states whether ROE improvement/stability is margin-driven or leverage-driven.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Stable ROE = healthy business | Always check whether ROE stability is masking offsetting deterioration in margin vs. increasing leverage |
| High ROE = superior company | High ROE driven by the equity multiplier alone reflects leverage risk, not operational excellence |
| Negative equity making ROE positive | State explicitly: ROE is undefined / economically misleading when equity is negative |
| Rounding errors causing non-reconciliation | Accept ±0.2 pp rounding tolerance; flag material non-reconciliation (>0.5 pp) as a data or formula error |
| ROIC without WACC = incomplete | Always note that ROIC alone does not determine value creation; the comparison to cost of capital requires WACC, which is not computed here |
