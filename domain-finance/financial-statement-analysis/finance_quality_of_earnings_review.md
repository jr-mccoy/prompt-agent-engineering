---
title: "Quality of Earnings Review"
category: finance/financial-statement-analysis
description: "Assess earnings quality by examining accruals, one-time items, revenue recognition timing, capitalization choices, and cash conversion — distinguishing durable from manufactured earnings."
techniques:
  - NE-11
  - QA-02
  - DS-04
  - AG-02
  - QA-04
difficulty: advanced
tags:
  - quality-of-earnings
  - accruals
  - revenue-recognition
  - earnings-quality
  - due-diligence
updated: "2026-06-08"
related_prompts:
  - domain-finance/financial-statement-analysis/finance_cash_flow_quality_analyzer.md
  - domain-finance/financial-statement-analysis/finance_footnote_red_flag_scanner.md
  - domain-finance/financial-statement-analysis/finance_financial_statement_anomaly_detector.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Systematically assess the quality and durability of reported earnings by analyzing the accrual ratio, one-time item classification, revenue recognition policies, capitalization and amortization choices, and the relationship between net income and operating cash flow — producing a structured QoE score and a prioritized list of items requiring further diligence.

---

## When to Use

- M&A financial due diligence (buy-side QoE workstream).
- Equity research underwriting a new coverage initiation.
- Credit analysis to assess whether EBITDA covenants are backed by cash.
- FP&A or audit planning — assessing whether management's adjusted metrics are credible.
- **Do not use** as a replacement for a full forensic accounting investigation or a formal QoE report from a licensed CPA firm; this prompt produces an analytical framework and flags, not an audited opinion.

---

## Inputs / Context Required

```
<qoe_data>
Company name / ticker:
Period(s) under review (suggest 3–5 years):
Accounting framework: US GAAP | IFRS
Purpose: M&A due diligence | Equity research | Credit | Internal

FINANCIAL STATEMENTS (paste or transcribe):
- Income statement (multi-period, including management-adjusted / non-GAAP if available)
- Balance sheet (multi-period)
- Cash flow statement (direct or indirect method; multi-period)
- Segment reporting (if available)

DISCLOSURES (paste relevant sections):
- Revenue recognition policy (from Notes)
- Capitalization policy (R&D, software development, customer acquisition costs)
- Significant estimates and judgments (from Notes or MD&A)
- Any disclosed restatements or accounting-policy changes
- Management commentary on "adjusted" or "non-GAAP" metrics and reconciliation

Context:
- Industry (SIC or NAICS or brief description)
- Recent M&A activity
- Major contract or customer concentration issues
</qoe_data>
```

---

## Constraints

### Must
- Lead with an **accrual ratio** calculation (both balance-sheet method and cash-flow method) as the anchor metric.
  - Balance-sheet accrual ratio = `(Net Operating Assets_t − Net Operating Assets_t-1) ÷ Average Net Operating Assets`
  - Where: Net Operating Assets = Total Assets − Cash − Total Liabilities + Total Debt
  - CF-method accrual ratio = `(Net Income − CFO − CFI) ÷ Average Net Operating Assets`
  - Interpretation: higher (more positive) accrual ratio → lower earnings quality.
- Compute the **cash conversion of earnings**: `CFO ÷ Net Income`; interpret relative to 1.0x benchmark.
- Identify and quantify every line item management classifies as "non-recurring" or excludes from adjusted metrics; require that such exclusions be justified against a three-year recurrence test.
- Flag revenue recognition risks per the five-step ASC 606 / IFRS 15 framework where relevant.
- Distinguish between **legitimate accounting flexibility** (policy choices within GAAP) and **aggressive use** of that flexibility.
- Apply adversarial stance (**AG-02**): default to skepticism on management adjustments; require positive evidence of non-recurrence before accepting an exclusion.
- Note US GAAP vs. IFRS differences that affect comparability (e.g., R&D expensing under GAAP vs. development-cost capitalization under IAS 38; interest paid classification in CFO/CFF).
- State confidence level (High / Medium / Low) for each QoE flag.
- Include an aggregate QoE score with a defined scale (see Output Format).
- Name the analytical bias risk most relevant to this company type (e.g., recency bias for a high-growth company where recent quarters dominate perception).

### Must Not
- Invent financial figures, footnote text, or peer benchmarks not in the supplied data.
- Present an accrual ratio as definitively indicating fraud — it is a signal, not proof.
- Accept management's "adjusted" EBITDA without independently reconciling it to GAAP.
- Omit the cash conversion check even if CFO is not separately disclosed (request it or note the limitation).
- Apply a label like "earnings manipulation" without citing specific, named evidence from the supplied disclosures.

---

## Instructions

1. **Establish the accrual baseline.**
   - Compute BS-method and CF-method accrual ratios for each period.
   - Compute CFO ÷ Net Income for each period.
   - Plot the trend: is earnings quality improving or deteriorating?
   - Flag if accrual ratio > 10% in any period or if trend is rising.

2. **Assess revenue quality.**
   - Identify the revenue recognition policy from Notes. Map to ASC 606 / IFRS 15 five steps.
   - Test for "bill-and-hold" language, channel stuffing patterns (AR growing faster than revenue), or customer-acceptance provisions that could defer recognition.
   - Compute Days Sales Outstanding (DSO = AR ÷ Revenue × 365) — rising DSO with flat/declining revenue is a red flag.
   - Check for multi-element arrangement complexity (software, SaaS, bundled products) where standalone selling prices may be allocated aggressively.
   - For subscription/ARR businesses: reconcile deferred revenue change (BS) to revenue recognized — accelerated recognition with declining deferred revenue signals pull-forward.

3. **Analyze one-time / non-recurring items.**
   - List every item management excludes from adjusted metrics.
   - Apply the **three-year recurrence test**: if a similar charge appeared in ≥ 2 of the prior 3 years, classify it as recurring.
   - Restate EBIT/EBITDA adding back items that fail the recurrence test.
   - Distinguish between: (a) genuinely non-recurring (natural disaster, true one-time settlement) vs. (b) structural charges presented as exceptional (restructuring, stock compensation, M&A costs, legal settlements).

4. **Evaluate capitalization and amortization choices.**
   - Identify all capitalized items: software development (ASC 350-40), customer acquisition costs (ASC 340-40), internal-use software, R&D (IFRS only — IAS 38 development phase).
   - Compute capitalized amount as % of revenue and % of gross operating expenditure in each period.
   - Test whether capitalization rates are rising faster than revenue growth (signals shifting expenses off P&L).
   - Assess amortization lives: are they consistent with economic reality and peer practice?
   - For goodwill: US GAAP requires annual impairment test (ASC 350); IFRS same. Review for impairment lag indicators.

5. **Test operating leverage and cost quality.**
   - Does gross margin expansion result from genuine pricing/efficiency improvement or from capitalization policy changes?
   - Is SG&A growth below revenue growth due to operating leverage or to reclassifying SG&A as capex / other balance-sheet items?
   - Check for "cookie-jar" reserves: unusually large accruals in good years, released in bad years to smooth earnings.

6. **Evaluate management-adjusted metrics.**
   - Obtain the full non-GAAP reconciliation.
   - Independently recompute adjusted EBITDA from GAAP net income.
   - Note every adjustment and apply the recurrence test (Step 3).
   - Compare management's adjusted leverage (Debt / Adjusted EBITDA) to GAAP-based leverage.

7. **Stress-test (QA-02 adversarial pass).**
   - What is the most aggressive revenue assumption embedded in current earnings? What happens if it normalizes?
   - What is the maximum capitalization reversal that would result if the capitalization policy shifted to the most conservative peer?
   - If every recurring "non-recurring" charge were added back to costs, what is the restated margin?
   - State a disconfirming scenario: what evidence would convince you earnings quality is actually improving?

8. **Verification pass (QA-01).**
   - Recompute accrual ratios from raw balance-sheet data.
   - Confirm CFO ÷ Net Income arithmetic.
   - Verify that the adjusted EBITDA walkdown reconciles to GAAP (sum the bridge items and cross-check).

---

## Output Format

```
## Quality of Earnings Review — [Company Name]
Periods: [FY__ through FY__] | Framework: [US GAAP / IFRS]
Purpose: [M&A QoE / Equity Research / Credit / Internal]
Prepared: [date] | Data: user-supplied

---

### Overall QoE Assessment

**QoE Score: [X / 5]**
Scale: 5 = highest quality (cash-backed, minimal adjustments, conservative policy); 1 = lowest quality (high accruals, aggressive adjustments, policy choices inflating earnings)

| Dimension            | Rating (1–5) | Key Finding |
|----------------------|--------------|-------------|
| Accrual ratio trend  | 3            | Mildly elevated; rising over 3 years |
| Revenue quality      | 4            | Policy clear; DSO stable |
| One-time items       | 2            | Restructuring charges appear every year |
| Capitalization policy| 3            | Software capex rising faster than revenue |
| Cash conversion      | 3            | CFO/NI = 0.82x avg; declining |

**Overall QoE Score: 3.0 / 5 — Moderate concerns; flag for deeper diligence**

---

### Section 1: Accrual Analysis

**Formula:** BS Accrual Ratio = (NOA_t − NOA_t-1) ÷ Avg NOA
Where NOA = Total Assets − Cash − (Total Liabilities − Total Debt)

| Metric                    | FY[n-2] | FY[n-1] | FY[n]  | Signal |
|---------------------------|---------|---------|--------|--------|
| Net Operating Assets ($M) | 850     | 920     | 1,050  | ↑ rising |
| BS Accrual Ratio          | 7.2%    | 9.1%    | 12.4%  | ⚠ >10% flag |
| CF Accrual Ratio          | 5.8%    | 8.3%    | 11.1%  | ⚠ trending up |
| CFO / Net Income (x)      | 1.10    | 0.95    | 0.82   | ⚠ declining |

**Interpretation:** Both accrual measures rising; cash conversion of earnings declining. Earnings are increasingly accrual-based. Requires explanation in Steps 2–5.
**Confidence: High** — computed directly from stated balance-sheet and cash-flow figures.

---

### Section 2: Revenue Quality

| Test                        | Finding                              | Flag? |
|-----------------------------|--------------------------------------|-------|
| Revenue recognition policy  | 5-step ASC 606; point-in-time delivery | No |
| DSO trend                   | 45 → 51 → 62 days (rising)          | ⚠ Yes |
| Deferred revenue trend      | Declining despite ARR growth         | ⚠ Yes |
| Channel stuffing indicators | AR growing 38% vs revenue 15%       | ⚠ Yes |

**Risk: Medium–High.** Rising DSO and declining deferred revenue alongside faster AR growth is consistent with [customer payment stress / pull-forward of revenue / channel stuffing]. Requires confirmation via customer concentration analysis and collections data.
**Confidence: Medium** — pattern is present; causation requires management interview or diligence data room access.

---

### Section 3: Non-Recurring Items — Recurrence Test

| Item                        | FY[n-2] | FY[n-1] | FY[n]  | Recurrence? | Treatment |
|-----------------------------|---------|---------|--------|-------------|-----------|
| Restructuring charge        | $12M    | $8M     | $15M   | ✗ Recurring | Add back to cost base |
| M&A transaction costs       | $5M     | $22M    | $0     | Ambiguous   | Accept FY[n-1] exclusion; monitor |
| Litigation settlement       | $0      | $0      | $18M   | First occurrence | Conditionally accept |
| Stock-based compensation    | $30M    | $35M    | $42M   | ✗ Recurring | SBC is an economic cost; include in EBITDA |

**Restated Adjusted EBITDA (excl. recurrence-failed items):**
Management Adj. EBITDA FY[n]: $210M
Less: restructuring add-back reversal: ($15M)
Less: SBC (economic cost): ($42M)
**Restated EBITDA: $153M** vs management's $210M — a 27% gap.

---

### Section 4: Capitalization Policy

| Item                         | FY[n-2] | FY[n-1] | FY[n]  | As % Rev |
|------------------------------|---------|---------|--------|----------|
| Capitalized software dev ($M)| 18      | 28      | 42     | 3.2%     |
| Customer acq. costs (CAC) ($M)| 10     | 15      | 24     | 1.8%     |
| Total capex to P&L ($M shift)| 28      | 43      | 66     | 5.0%     |

**If expensed immediately, FY[n] EBIT impact: ($66M) pretax.**
Capitalization rate rising faster than revenue (capex/rev: 2.9% → 4.2% → 5.0%). Consistent with shifting operating costs off P&L. Amortization lives: software 3 years (assess vs. actual product lifecycle).

---

### Section 5: Adjusted Earnings Bridge

| Bridge Line                        | Amount  |
|------------------------------------|---------|
| Reported Net Income FY[n]          | $91M    |
| Add back: D&A                      | +$60M   |
| Add back: interest expense         | +$28M   |
| Add back: taxes                    | +$32M   |
| = EBITDA (GAAP)                    | $211M   |
| Mgmt adjustments (restructuring, M&A costs, litigation) | +$33M |
| = Management Adjusted EBITDA       | $244M   |
| Less: restructuring (recurring, reverse) | ($15M)|
| Less: SBC (economic cost, reverse) | ($42M) |
| = QoE-Restated EBITDA              | $187M   |
| Δ vs. Management Adj. EBITDA       | ($57M) / −23% |

---

### Section 6: Stress Scenarios

| Scenario         | Assumption                          | Restated EBITDA | Mgmt Adj. Leverage |
|------------------|-------------------------------------|-----------------|-------------------|
| Base (GAAP)      | No adjustments                      | $211M           | 2.4x Debt/EBITDA  |
| QoE-Restated     | Strip recurring charges + SBC       | $187M           | 2.7x              |
| Conservative     | QoE-restated + normalize capex rate | $145M           | 3.5x              |
| Bear             | Revenue decline 10% + margin compress| $105M          | 4.8x ⚠ covenant risk |

---

### Section 7: Summary Flags and Priority Actions

| Priority | Finding                          | Confidence | Action Required |
|----------|----------------------------------|------------|-----------------|
| 1 — High | Accrual ratio above 10%, rising  | High       | Reconcile to specific BS drivers; interview AR/inventory |
| 2 — High | Restructuring charges recurring  | High       | Reclassify as operating cost in model |
| 3 — Med  | Rising DSO / AR faster than rev  | Medium     | Customer aging report; collections interview |
| 4 — Med  | Capitalization rate increasing   | Medium     | Review software project list; assess amortization lives |
| 5 — Low  | SBC excluded from adj. EBITDA   | High       | Include as economic cost; standard restatement |

**Disconfirming scenario:** If management can demonstrate DSO increase is due to deliberate extension of payment terms to high-quality enterprise customers with clean aging, and the capex increase reflects identifiable products with >3-year revenue payback, QoE score could improve to 4/5.
```

---

## Verification

- [ ] Accrual ratios computed using the same NOA definition in both the BS and CF methods.
- [ ] CFO ÷ Net Income arithmetic confirmed against stated figures.
- [ ] Every management adjustment listed and individually tested against the three-year recurrence test.
- [ ] Restated EBITDA bridge sums correctly from GAAP net income.
- [ ] No figure in output not traceable to the user-supplied financial statements or disclosures.
- [ ] Confidence levels assigned to each material flag.
- [ ] Disconfirming scenario stated explicitly.
- [ ] US GAAP vs. IFRS differences noted where they affect comparability.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Labeling accruals as fraud | Accrual ratio is a signal, not evidence of manipulation; state as "elevated accruals warrant investigation" |
| Accepting every management adjustment uncritically | Apply three-year recurrence test; reverse any adjustment where the item recurs in ≥ 2 of 3 prior years |
| Treating rising capitalization as always aggressive | Some capex acceleration reflects genuine investment; state "rising at a rate above revenue growth" and ask for product-specific validation |
| Calling DSO increase a red flag without alternatives | Rising DSO could reflect a deliberate shift to enterprise customers or seasonal patterns; state as "consistent with" and list alternatives |
| Overstating the EBITDA gap | Verify each bridge line independently; a sign error in the SBC add-back reversal can double-count |
| Applying GAAP tests to an IFRS filer | Note that IAS 38 permits development-cost capitalization where US GAAP requires expensing; adjust the comparison baseline accordingly |
