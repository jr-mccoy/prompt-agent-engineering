---
title: "Financial Statement Anomaly Detector"
category: finance/financial-statement-analysis
description: "Detect anomalies, internal inconsistencies, and potential manipulation signals across the income statement, balance sheet, and cash flow statement — using Beneish M-Score methodology and a structured cross-statement reconciliation."
techniques:
  - DS-04
  - AG-02
  - QA-02
  - NE-11
  - QA-04
difficulty: advanced
tags:
  - anomaly-detection
  - beneish
  - earnings-manipulation
  - forensic-accounting
  - cross-statement
updated: "2026-06-08"
related_prompts:
  - domain-finance/financial-statement-analysis/finance_quality_of_earnings_review.md
  - domain-finance/financial-statement-analysis/finance_footnote_red_flag_scanner.md
  - domain-finance/financial-statement-analysis/finance_cash_flow_quality_analyzer.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Apply a structured forensic lens to a company's financial statements — computing the Beneish M-Score indices, performing cross-statement consistency checks, scanning for common manipulation patterns, and producing a prioritized anomaly register with severity ratings, confidence levels, and disconfirming evidence requirements. The output is an analytical flag report, not an opinion on fraud.

---

## When to Use

- Short-thesis development: screening for potential earnings manipulation before taking a position.
- Equity research: anomaly check before publishing a new coverage initiation.
- M&A due diligence: forensic-screen the target's financials before commissioning a formal QoE.
- Credit underwriting: detecting financial reporting risk in a new borrower.
- Internal audit / risk management: systematic annual screening of financial reporting quality.
- **Do not use** as a substitute for a formal forensic accounting investigation or a legal proceeding. Beneish M-Score flags are statistical signals with known false-positive rates — they identify companies warranting further scrutiny, not companies that have engaged in fraud.

---

## Inputs / Context Required

```
<anomaly_data>
Company name / ticker:
Two consecutive fiscal years are the minimum for Beneish; three years preferred.
Accounting framework: US GAAP | IFRS
Industry: [Important — some sectors (financial services, real estate, exploration-stage) have known limitations with the standard Beneish model]

INCOME STATEMENT (periods t and t-1; t-2 if available):
- Net Revenue (Net Sales)
- Cost of Goods Sold
- Gross Profit
- Selling, General & Administrative (SG&A)
- Depreciation & Amortization
- EBIT / Operating Income
- Interest Expense
- Pre-Tax Income (EBT)
- Tax Expense
- Net Income

BALANCE SHEET (periods t and t-1):
- Cash and cash equivalents
- Accounts Receivable, net
- Inventory
- Current Assets (total)
- PP&E, gross
- Accumulated Depreciation
- PP&E, net
- Total Assets
- Current Liabilities (total)
- Long-Term Debt
- Total Liabilities
- Shareholders' Equity

CASH FLOW STATEMENT (periods t and t-1):
- Cash From Operations (CFO)
- Depreciation & Amortization (as add-back in CFO reconciliation)
- Capital Expenditures (Capex)

ADDITIONAL CONTEXT:
- Any known restatements, policy changes, or acquisitions during the periods
- Auditor name and opinion
- Industry gross margin typical range (if known)
</anomaly_data>
```

---

## Constraints

### Must
- Compute all 8 Beneish M-Score indices with formulas:
  - **DSRI** (Days Sales Receivable Index) = (AR_t / Revenue_t) ÷ (AR_{t-1} / Revenue_{t-1}) — measures AR growth relative to revenue
  - **GMI** (Gross Margin Index) = Gross Margin_{t-1} ÷ Gross Margin_t — declining margin = GMI > 1
  - **AQI** (Asset Quality Index) = (1 − (CA_t + PP&E_t) / TA_t) ÷ (1 − (CA_{t-1} + PP&E_{t-1}) / TA_{t-1}) — rising non-productive assets
  - **SGI** (Sales Growth Index) = Revenue_t ÷ Revenue_{t-1}
  - **DEPI** (Depreciation Index) = (Dep_{t-1} / (Dep_{t-1} + PP&E_net_{t-1})) ÷ (Dep_t / (Dep_t + PP&E_net_t)) — slowing depreciation rate = DEPI > 1
  - **SGAI** (SGA Index) = (SGA_t / Revenue_t) ÷ (SGA_{t-1} / Revenue_{t-1})
  - **LVGI** (Leverage Index) = ((LTD_t + CL_t) / TA_t) ÷ ((LTD_{t-1} + CL_{t-1}) / TA_{t-1})
  - **TATA** (Total Accruals to Total Assets) = (Net Income_t − CFO_t) / TA_t (note: original Beneish uses working-capital-based accruals; the cash-flow version is shown here as the more robust variant)
- Compute the **M-Score**:
  - M-Score = −4.84 + 0.920×DSRI + 0.528×GMI + 0.404×AQI + 0.892×SGI + 0.115×DEPI − 0.172×SGAI + 4.679×TATA − 0.327×LVGI
  - Interpretation: M-Score > −1.78 → elevated manipulation probability; M-Score > −2.22 → moderate concern (Beneish's original thresholds — note: vary by study; state which threshold is applied)
- Apply adversarial skepticism (AG-02): treat M-Score > −1.78 as a flag requiring cross-statement verification, not as confirmed manipulation.
- Perform cross-statement consistency checks (see Instructions Step 3).
- Assign each finding: **Severity** (High / Medium / Low) and **Confidence** (High / Medium / Low).
- State the most important known limitation of the Beneish model for the specific company (industry, size, growth phase).
- Name the relevant analytical bias and apply a disconfirming check: "What is the most benign explanation for each flagged index?"
- Note US GAAP vs. IFRS differences: IFRS development-cost capitalization (IAS 38) increases AQI; IFRS 15 variable-consideration estimates affect DSRI; these are structural differences, not anomalies in themselves.

### Must Not
- Label any finding "fraud" or "manipulation" — use "elevated risk," "warrants investigation," or "inconsistent with stated metrics."
- Apply the standard manufacturing Beneish model without a stated caveat to financial services companies, REITs, insurance companies, or early-stage companies.
- Present the M-Score as a probability of fraud without the calibration context (original sample: ~70% sensitivity, ~75% specificity; significant false-positive rate).
- Omit the cross-statement checks — the M-Score alone is insufficient; consistency checks are required.

---

## Instructions

1. **Compute Beneish M-Score indices.**
   - Compute each of the 8 indices with the formula and the resulting value.
   - Flag individual indices that are in "manipulation-suggestive" territory:
     - DSRI > 1.465 (flagged in Beneish's original paper)
     - GMI > 1.193
     - AQI > 1.254
     - SGI > 1.607
     - DEPI > 1.083
     - SGAI > 1.054 (negative coefficient in model — increasing SGA is generally not a manipulation flag by itself)
     - LVGI > 1.111
     - TATA > 0.031
   - Note: these thresholds are from the Beneish (1999) paper; other calibrations exist; state the source.

2. **Compute the M-Score and interpret.**
   - Apply the weighted formula.
   - State the zone: > −1.78 (high concern), −2.22 to −1.78 (moderate concern), < −2.22 (lower concern).
   - Note the estimated sensitivity / specificity and the false-positive rate in plain language.

3. **Cross-statement consistency checks.**
   - **Revenue vs. AR:** Does AR growth track revenue growth? Significant AR outpacing revenue (DSRI flag) is a consistency concern.
   - **Revenue vs. CFO:** Is CFO growing at roughly the same pace as revenue? If revenue grew 20% and CFO grew 5%, the divergence needs explanation.
   - **Net Income vs. CFO:** Cash conversion = CFO / Net Income. Below 0.80x is flagged.
   - **D&A in CFO vs. D&A on Income Statement:** These should be identical (or reconcilable). A mismatch is a data error or a classification anomaly.
   - **Capex vs. PP&E change:** PP&E_t = PP&E_{t-1} + Capex_t − Depreciation_t ± Asset disposals ± Acquisitions. Compute the "unexplained PP&E change" — a large unexplained gap may indicate capitalization of expenses.
   - **Retained Earnings roll:** RE_t = RE_{t-1} + Net Income_t − Dividends_t. If this does not hold, there was either a restatement, a prior-period adjustment, or an error.
   - **Total Assets = Total Liabilities + Equity:** Verify the balance sheet balances in both periods.
   - **Tax rate consistency:** Effective tax rate = Tax Expense / Pre-Tax Income. Large swings in ETR without a disclosed explanation are a flag.

4. **Scan for common manipulation patterns beyond Beneish.**
   - **Round-number reporting:** Revenue or EPS clustered at round numbers in multiple periods — a statistical signal of potential smoothing (note: cannot be fully tested without a longer time series).
   - **Channel stuffing indicators:** AR days increasing sharply at fiscal year-end (compare Q4 vs. Q3 if quarterly data available).
   - **Accelerating revenue in final quarter:** Does Q4 revenue disproportionately exceed the quarterly average? (Requires quarterly data.)
   - **Declining allowance for doubtful accounts as % of AR:** Reserve declining while AR grows — may indicate under-provisioning.
   - **Unusually small COGS increase relative to revenue increase:** May indicate failure to expense inventory consumed.
   - **SG&A declining as % of revenue in a high-growth phase:** Could reflect legitimate leverage, or could indicate reclassification of operating expenses to capex.

5. **Adversarial stress-test (QA-02).**
   - "If this company were manipulating earnings, what would be the most likely mechanism given the flags identified?"
   - "What single piece of evidence would most quickly confirm or deny the primary flag?"
   - Apply the disconfirming lens: "What is the most benign explanation for the three most elevated flags?"

6. **Summarize and prioritize the anomaly register.**
   - Priority ranking: combine severity and confidence to identify the top 3–5 flags requiring immediate follow-up.
   - For each, state: what to look for in additional diligence, what question to ask management, and what data source would resolve it.

7. **Verification pass (QA-01).**
   - Recompute the M-Score from the stated indices and verify the weighted sum.
   - Confirm the retained earnings roll from supplied figures.
   - Confirm balance sheet balances in both periods.
   - Confirm D&A consistency between income statement and cash flow statement.

---

## Output Format

```
## Financial Statement Anomaly Detection — [Company Name]
Periods: t=[FY__] vs. t-1=[FY__] | Framework: [US GAAP / IFRS]
Industry: [stated] | Beneish model variant: [standard 8-factor / adjusted]
Prepared: [date] | Data: user-supplied

---

### SECTION 1: BENEISH M-SCORE INDICES

Formulas and results (t = FY[n], t-1 = FY[n-1]):

| Index | Formula | t-1 Component | t Component | Index Value | Flag Threshold | Flagged? |
|-------|---------|--------------|-------------|-------------|----------------|----------|
| DSRI  | (AR_t/Rev_t)÷(AR_t-1/Rev_t-1) | 0.126 | 0.170 | **1.35** | >1.465 | No (elevated) |
| GMI   | GM%_t-1 ÷ GM%_t | 36.5% | 35.0% | **1.04** | >1.193 | No |
| AQI   | (1−(CA+PPE)/TA)_t ÷ (1−(CA+PPE)/TA)_t-1 | 0.330 | 0.385 | **1.17** | >1.254 | No (elevated) |
| SGI   | Rev_t ÷ Rev_t-1 | — | — | **1.15** | >1.607 | No |
| DEPI  | DepRate_t-1 ÷ DepRate_t | 0.107 | 0.098 | **1.09** | >1.083 | ⚠ Yes |
| SGAI  | (SGA/Rev)_t ÷ (SGA/Rev)_t-1 | 0.190 | 0.190 | **1.00** | >1.054 | No |
| LVGI  | (LTD+CL)_t/TA_t ÷ (LTD+CL)_t-1/TA_t-1 | 0.361 | 0.419 | **1.16** | >1.111 | ⚠ Yes |
| TATA  | (NI−CFO)_t / TA_t | — | — | **0.039** | >0.031 | ⚠ Yes |

**M-Score Calculation:**
M = −4.84 + 0.920(1.35) + 0.528(1.04) + 0.404(1.17) + 0.892(1.15) + 0.115(1.09) − 0.172(1.00) + 4.679(0.039) − 0.327(1.16)

M = −4.84 + 1.242 + 0.549 + 0.473 + 1.026 + 0.125 − 0.172 + 0.182 − 0.379
**M-Score = −1.79**

**Zone: High Concern (> −1.78 threshold)**
Estimated sensitivity ~76%, specificity ~73% in original sample — substantial false-positive rate. This result flags for further investigation, not manipulation confirmation.

---

### SECTION 2: CROSS-STATEMENT CONSISTENCY CHECKS

| Check                                  | Expected                  | Actual Result       | Flag?  |
|----------------------------------------|---------------------------|---------------------|--------|
| Revenue vs. CFO growth                 | Roughly similar pace      | Rev +15%, CFO −12%  | ⚠ Yes |
| CFO / Net Income                       | >0.80x (healthy)          | 0.82x → 0.82x (borderline) | Monitor |
| D&A in CFO = D&A in income statement   | Match                     | $60M = $60M         | ✓      |
| PP&E roll: (Beg + Capex − Depr ± Disp = End) | Balance           | Gap = $0M           | ✓      |
| Retained Earnings roll: (Beg + NI − Divid = End) | Balance       | Gap = $0M           | ✓      |
| Balance sheet balances: Assets = L+E  | = in both periods         | ✓ both periods      | ✓      |
| Effective tax rate consistency         | <10 pp swing expected     | 24.6% → 26.0%       | ✓      |
| AR allowance as % of gross AR          | Stable or rising          | 6.2% → 4.8%         | ⚠ Declining |

---

### SECTION 3: ANOMALY REGISTER

**Finding 1: TATA Elevated — High Accruals Relative to Assets**
- Severity: High | Confidence: High
- Index: TATA = 0.039 (threshold 0.031)
- Mechanism: Net Income exceeds CFO by an amount that, relative to total assets, is above the Beneish threshold. Earnings are accrual-heavy.
- Benign explanation: Working-capital build for planned revenue growth; AR increase from legitimate enterprise deals.
- Disconfirming evidence: AR aging shows current receivables; WC explanation is consistent with disclosed customer additions.
- Follow-up: Obtain AR aging; compare DSO vs. peers; test AR growth against customer-count or contract-value data.

**Finding 2: Revenue vs. CFO Divergence**
- Severity: High | Confidence: High
- Revenue grew 15%; CFO declined 12% — a 27 pp divergence. This is the largest consistency concern.
- Benign explanation: Planned working-capital investment in AR for enterprise customers with longer payment terms.
- Worst-case: Revenue recognized ahead of cash collection; channel stuffing or pull-forward.
- Follow-up: Reconcile the CFO decline to specific WC movements; test AR aging; check quarterly AR pattern for Q4 spike.

**Finding 3: DEPI Flagged — Slowing Depreciation Rate**
- Severity: Medium | Confidence: Medium
- DEPI = 1.09 (threshold 1.083): depreciation as a % of gross PP&E has slowed, suggesting either (a) extension of useful lives or (b) shift in asset mix to longer-lived assets.
- Benign explanation: New assets (buildings, long-lived equipment) added in the period carry lower depreciation rates.
- Flagged concern: If management extended useful lives without disclosure, it would reduce D&A and inflate EBIT.
- Follow-up: Inspect useful-life policy in footnotes; compare to prior year policy disclosure; check for change in asset mix.

**Finding 4: AR Allowance Declining (6.2% → 4.8%)**
- Severity: Medium | Confidence: Medium
- Allowance for doubtful accounts declining as AR grows — may indicate under-provisioning.
- Benign explanation: Customer quality improved (shift to larger, lower-risk enterprise customers).
- Follow-up: Obtain write-off history; compare allowance % to peer standard; review collections aging.

**Finding 5: LVGI Flagged — Rising Leverage**
- Severity: Low | Confidence: High
- LVGI = 1.16 — leverage increasing. Consistent with known debt issuance; not a manipulation signal in isolation, but contributes to the M-Score.
- This is structural, not anomalous, given disclosed borrowing in the period. Low standalone concern.

---

### SECTION 4: ADVERSARIAL SCENARIO

**Most plausible mechanism if manipulation is occurring:**
Given TATA elevation, DSRI near-threshold, and CFO/Revenue divergence, the most consistent manipulation scenario is: revenue recognized in advance of cash collection (bill-and-hold or aggressive milestone billing), inflating reported revenue and AR while CFO lags. A secondary mechanism could involve slowing depreciation (DEPI flag) to pad EBIT.

**Single most diagnostic data point:** Quarterly AR pattern — a sharp spike in Q4 AR that reverses in Q1 is the clearest channel-stuffing / pull-forward signal. If Q4 AR is not disproportionate, the DSRI elevation is more likely explained by organic collection timing.

**Disconfirming evidence for the primary thesis:**
- AR aging showing >90% current (not past due) would significantly reduce the revenue-quality concern.
- CFO recovering in the next period to above prior-year levels (WC reversal) would confirm the build was temporary.
- Management disclosure of enterprise contract with extended payment terms from a named, large customer.

---

### SECTION 5: PRIORITY ACTIONS

| Priority | Finding | Severity | Confidence | Action |
|----------|---------|----------|------------|--------|
| 1 | Revenue vs. CFO divergence | High | High | Obtain AR aging; model CFO recovery; check quarterly AR |
| 2 | TATA elevation (accrual-heavy earnings) | High | High | Reconcile to WC drivers; compute accrual ratio per QoE framework |
| 3 | AR allowance declining | Medium | Medium | Compare to peer; obtain write-off history |
| 4 | DEPI flag (slowing depreciation) | Medium | Medium | Read useful-life footnote; compare to prior year |
| 5 | LVGI (leverage rising) | Low | High | Monitor; already incorporated in credit analysis |

---

### KNOWN LIMITATIONS OF THIS ANALYSIS

1. **Beneish model calibration:** Original sample was US manufacturing firms, 1982–1988 data. Application to [non-manufacturing / high-growth SaaS / IFRS filer] carries lower reliability.
2. **Single year of indices:** M-Score is more reliable when computed over multiple consecutive periods; a single elevated score has a higher false-positive rate.
3. **No quarterly data:** Seasonal or Q4-specific manipulations are not testable from annual data alone.
4. **IFRS differences:** Development-cost capitalization (IAS 38) increases AQI structurally; if the filer is IFRS, AQI elevation has a higher benign-explanation probability.
5. **This output is analytical, not forensic.** A formal investigation requires a qualified forensic accountant, access to the general ledger, and legal authority.
```

---

## Verification

- [ ] All 8 Beneish indices computed from stated raw figures, formula shown for each.
- [ ] M-Score weighted sum verified arithmetically.
- [ ] Cross-statement checks performed: retained earnings roll, PP&E roll, balance sheet balance, D&A consistency.
- [ ] CFO / Net Income computed and compared to prior year.
- [ ] Confidence level assigned to every finding.
- [ ] Benign explanation stated for every flagged index.
- [ ] Disconfirming evidence specified for the primary anomaly scenario.
- [ ] Limitation note states the Beneish model variant applied and the key industry/framework caveat.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Calling M-Score > −1.78 as "likely fraud" | State: "statistically elevated; warrants further investigation"; cite the false-positive rate |
| Applying standard Beneish to a financial company | Explicitly flag that the model is calibrated on manufacturing; apply with known reliability limitation |
| Single-index flag as a definitive finding | Require at least 2–3 corroborating signals before escalating severity to High |
| Treating revenue–CFO divergence as always suspicious | Fast-growing companies with enterprise contracts have structurally large WC builds; require the AR aging test before concluding |
| DEPI flag = manipulated depreciation | Slowing depreciation rate can reflect asset-mix shift to longer-lived assets; require useful-life footnote review |
| Ignoring IFRS vs. GAAP AQI difference | IFRS development-cost capitalization legitimately increases non-current assets (and therefore AQI); normalize before comparing to GAAP-calibrated Beneish thresholds |
