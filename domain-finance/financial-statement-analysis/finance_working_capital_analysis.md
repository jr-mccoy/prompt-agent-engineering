---
title: "Working Capital and Cash Conversion Cycle Analysis"
category: finance/financial-statement-analysis
description: "Compute the cash conversion cycle and working-capital efficiency metrics, attribute changes to specific drivers, and assess the funding implications for operations and free cash flow."
techniques:
  - NE-11
  - DS-02
  - DS-04
  - QA-01
  - OC-01
difficulty: intermediate
tags:
  - working-capital
  - cash-conversion-cycle
  - dso
  - dpo
  - inventory
updated: "2026-06-08"
related_prompts:
  - domain-finance/financial-statement-analysis/finance_cash_flow_quality_analyzer.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/financial-statement-analysis/finance_liquidity_solvency_stress_check.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Compute the cash conversion cycle (CCC) and its component metrics (DSO, DIO, DPO), build a multi-period trend table, attribute changes to specific business or accounting drivers, quantify the cash funding impact of working-capital movements, and benchmark against industry norms where peer data is provided.

---

## When to Use

- Diagnosing why a profitable business has poor cash flow.
- Credit analysis: assessing operating liquidity and short-term funding requirements.
- Supply-chain or operations review: identifying inefficiencies in collections, inventory management, or payables management.
- Pre-acquisition diligence: estimating a normalized working-capital target for purchase-price adjustments.
- FP&A: modeling cash requirements for a revenue growth plan.
- **Do not use** without at least two periods of balance-sheet and income-statement data — a single-period CCC is a snapshot, not an insight.

---

## Inputs / Context Required

```
<wc_data>
Company name / ticker:
Periods: [minimum 2 periods; 3–5 preferred]
Accounting framework: US GAAP | IFRS
Industry / business model: [e.g., manufacturing, retail, SaaS, distribution, healthcare]

INCOME STATEMENT DATA (per period):
- Net Revenue (or Net Sales)
- Cost of Goods Sold (or Cost of Revenue)

BALANCE SHEET DATA (per period, end-of-period):
- Accounts Receivable, net
- Inventory (if applicable)
- Other current assets (prepaid expenses, etc.)
- Accounts Payable
- Accrued Liabilities
- Deferred Revenue (current portion)
- Any other significant operating current asset or liability

ADDITIONAL CONTEXT (if available):
- Gross-to-net revenue adjustments (returns, rebates) that affect AR but not revenue
- Vendor payment term changes disclosed in MD&A
- Customer payment term changes or concentrations
- Seasonal patterns (fiscal year end timing vs. peak season)
- Recent M&A that changed the WC profile
- Management-disclosed WC target or normalized WC as a % of revenue
- Peer or industry benchmark data (optional)
</wc_data>
```

---

## Constraints

### Must
- Compute all three CCC components using the precise formulas:
  - **Days Sales Outstanding (DSO)** = `Accounts Receivable, net ÷ Net Revenue × 365`
  - **Days Inventory Outstanding (DIO)** = `Inventory ÷ COGS × 365` (use COGS as the denominator, not revenue, to capture inventory turns correctly)
  - **Days Payable Outstanding (DPO)** = `Accounts Payable ÷ COGS × 365` (same base as DIO for consistency)
  - **Cash Conversion Cycle (CCC)** = `DSO + DIO − DPO`
- Compute the **Net Working Capital (NWC)** and **Operating Working Capital (OWC)**:
  - NWC = Current Assets − Current Liabilities
  - OWC = AR + Inventory + Other Operating Current Assets − AP − Accrued Liabilities (exclude cash, short-term debt, current portion of long-term debt, and deferred revenue from the operating WC definition; deferred revenue is a non-cash liability)
  - OWC as % of Revenue = OWC ÷ Revenue × 100
- Compute the **cash funding impact** of WC changes: Cash Impact = −(ΔOperating WC), i.e., a WC increase consumes cash.
- Offer average vs. period-end balance comparisons for DSO and DIO when the business is seasonal: `DSO_avg = AR ÷ (Revenue ÷ 365)` using average AR `= (AR_beginning + AR_ending) ÷ 2`.
- Flag any metric that moves more than 5 days in a single period (material shift requiring explanation).
- State the **efficiency benchmark** for the stated industry if peer data is provided; if not, note that the analysis is self-referential (trend vs. trend) and a peer comparison requires additional data.
- Note that deferred revenue is excluded from OWC because it represents an obligation to deliver goods/services, not a cash obligation — but it does affect the cash cycle and should be discussed separately.

### Must Not
- Use revenue as the denominator for DIO — this produces an incorrect inventory turnover figure for gross-margin businesses.
- Average DSO/DIO/DPO across periods without noting that period-end figures are used (point-in-time, not trailing average unless stated).
- Invent industry benchmarks not in the supplied data.
- Classify deferred revenue as a cash-reducing current liability in OWC without disclosing the treatment.
- Present a single-period CCC as the conclusion — require multi-period context.

---

## Instructions

1. **Compute CCC components for each period.**
   - DSO, DIO (if inventory applies), DPO.
   - CCC = DSO + DIO − DPO.
   - Present in a trend table (see Output Format).
   - For service businesses with no inventory: CCC = DSO − DPO; note that DIO is not applicable.

2. **Compute Operating Working Capital (OWC).**
   - Define components explicitly. Exclude cash, short-term debt, current LTD, and deferred revenue (flag deferred revenue separately).
   - Compute OWC / Revenue % for each period.
   - Compute year-over-year change in OWC in dollar terms; this is the cash funding impact.

3. **Attribute changes to specific drivers.**
   - For each metric that moved > 5 days, offer a structured attribution:
     - DSO increase: possible causes — slower collections, aggressive year-end revenue recognition, customer financial stress, deliberate credit term extension, billing timing.
     - DIO increase: possible causes — demand slowdown, inventory build ahead of launch, input cost hedging, supply disruption response.
     - DPO decrease: possible causes — losing negotiating leverage, taking early payment discounts, vendor term changes.
   - Do not assign causation without supporting evidence from disclosures; use "consistent with" language.

4. **Quantify cash funding impact.**
   - If OWC increased by $X million, the business consumed $X million in operating cash.
   - Compute this as % of CFO: a WC build that exceeds 20% of CFO is a significant cash drain.
   - Extend to: at the revenue growth plan, how much additional WC funding is required? (WC requirement = OWC% × Revenue growth)

5. **Deferred revenue analysis (subscription / contract businesses).**
   - Track deferred revenue balance as a separate metric.
   - Rising deferred revenue = cash collected ahead of recognition (positive cash quality signal).
   - Declining deferred revenue alongside rising revenue = potential pull-forward.
   - Compute: Deferred Revenue Days = Deferred Revenue ÷ Revenue × 365.

6. **Benchmark against peers (if data provided).**
   - Side-by-side table: subject vs. peer median for DSO, DIO, DPO, CCC, OWC/Revenue.
   - Flag deviations > 5 days on any metric.

7. **Scenario: WC normalization impact.**
   - If the subject has a higher CCC than peers, estimate the cash release from normalizing to peer median.
   - Cash release = (Subject CCC − Peer CCC) ÷ 365 × Revenue.
   - This is relevant for M&A working-capital targets or restructuring initiatives.

8. **Verification pass (QA-01).**
   - Recompute DSO, DIO, DPO for the most recent period from raw data.
   - Confirm CCC = DSO + DIO − DPO arithmetically.
   - Verify OWC change ties to the working-capital line items in the cash flow statement (indirect method CFO).

---

## Output Format

```
## Working Capital and Cash Conversion Cycle Analysis — [Company Name]
Periods: [FY__ through FY__] | Framework: [US GAAP / IFRS]
Industry: [stated industry] | Prepared: [date] | Data: user-supplied

---

### Section 1: CCC Trend Table

Formulas:
- DSO = AR ÷ Revenue × 365
- DIO = Inventory ÷ COGS × 365
- DPO = AP ÷ COGS × 365
- CCC = DSO + DIO − DPO

| Metric               | FY[n-2] | FY[n-1] | FY[n]  | Δ (last yr) | Trend   |
|----------------------|---------|---------|--------|-------------|---------|
| Revenue ($M)         | 1,000   | 1,150   | 1,320  | +14.8%      | ↑       |
| COGS ($M)            | 620     | 730     | 858    | +17.5%      | ↑       |
| AR, net ($M)         | 123     | 145     | 225    | +55%        | ↑↑ ⚠   |
| Inventory ($M)       | 95      | 120     | 145    | +20.8%      | ↑       |
| AP ($M)              | 85      | 100     | 120    | +20.0%      | ↑       |
| **DSO (days)**       | **45**  | **46**  | **62** | **+16 ⚠**  | Worsening |
| **DIO (days)**       | **56**  | **60**  | **62** | **+2**      | Stable |
| **DPO (days)**       | **50**  | **50**  | **51** | **+1**      | Stable |
| **CCC (days)**       | **51**  | **56**  | **73** | **+17 ⚠**  | Worsening |

**Flagged: DSO +16 days in one year. CCC expanded 22 days over two years.**

---

### Section 2: Operating Working Capital

| Metric                    | FY[n-2] | FY[n-1] | FY[n]  |
|---------------------------|---------|---------|--------|
| AR                        | 123     | 145     | 225    |
| Inventory                 | 95      | 120     | 145    |
| Other current assets      | 12      | 15      | 18     |
| Less: AP                  | (85)    | (100)   | (120)  |
| Less: Accrued liabilities | (45)    | (50)    | (60)   |
| **OWC ($M)**              | **100** | **130** | **208**|
| OWC / Revenue             | 10.0%   | 11.3%   | 15.8%  |
| **ΔOWC (cash impact)**    | —       | ($30M)  | ($78M) |
| ΔOWC as % of CFO          | —       | 18.8%   | 55.7% ⚠|

**FY[n]: WC consumed $78M of cash — 56% of CFO. This explains the declining FCF despite stable EBITDA.**

---

### Section 3: Driver Attribution

**DSO +16 days FY[n]:**
- AR grew 55% while revenue grew only 15% → significant collection lag
- Possible drivers: [customer payment delays / aggressive Q4 revenue recognition / deliberate credit extension to win deals]
- Requires: AR aging schedule, top customer payment behavior, any disclosed policy change

**DIO +2 days (stable):**
- Inventory growing roughly in line with COGS — no significant signal. Monitor for build-up if demand slows.

**DPO +1 day (stable):**
- Payables management holding steady — no leverage gain or loss detected.

---

### Section 4: Cash Funding Impact of Revenue Growth Plan

If revenue grows to $1,500M next year (assuming OWC% stays at 15.8%):
- Target OWC = $1,500M × 15.8% = $237M
- Current OWC = $208M
- **Incremental WC funding required: $29M**

If OWC% normalizes to prior-year level (11.3%):
- Target OWC = $1,500M × 11.3% = $170M
- **WC release: $38M** (positive cash impact)

---

### Section 5: Deferred Revenue (if applicable)

| Metric                     | FY[n-2] | FY[n-1] | FY[n]  |
|----------------------------|---------|---------|--------|
| Deferred Revenue ($M)      | 45      | 48      | 42     |
| Deferred Revenue Days      | 16.4    | 15.2    | 11.6   |
| Signal                     | Stable  | Stable  | ↓ declining |

**Deferred revenue declining while revenue grows → possible pull-forward or declining backlog.**

---

### Section 6: Peer Comparison (if data provided)

| Metric         | Subject | Peer Median | Subject vs. Peer |
|----------------|---------|-------------|------------------|
| DSO (days)     | 62      | 45          | +17 days ⚠       |
| DIO (days)     | 62      | 55          | +7 days ▲        |
| DPO (days)     | 51      | 48          | +3 days (slight benefit) |
| CCC (days)     | 73      | 52          | +21 days ⚠       |
| OWC / Revenue  | 15.8%   | 11.2%       | +460 bps ⚠       |

**WC normalization opportunity:** (73 − 52) ÷ 365 × $1,320M = **$75.9M cash release** if CCC normalizes to peer median.

---

### Section 7: Summary and Recommendations

**WC Health: Deteriorating (2/5)**

| Dimension       | Assessment |
|-----------------|------------|
| DSO             | Rising materially — investigate AR aging and recognition timing |
| DIO             | Stable — no immediate concern |
| DPO             | Stable — no leverage gain or loss |
| OWC / Revenue   | Rising sharply — WC is consuming operating cash |
| FCF Impact      | WC consumed 56% of CFO in FY[n] — primary FCF headwind |

**Recommended follow-up:**
- [ ] Obtain AR aging schedule and compare to prior year
- [ ] Review Q4 revenue concentration and any end-of-quarter deals with extended terms
- [ ] Assess deferred revenue trend for renewal health
- [ ] Model WC target for M&A normalization at peer-median OWC%
```

---

## Verification

- [ ] DSO = AR ÷ Revenue × 365, confirmed from raw data.
- [ ] DIO = Inventory ÷ COGS × 365 (COGS denominator, not revenue).
- [ ] DPO = AP ÷ COGS × 365 (same base as DIO).
- [ ] CCC = DSO + DIO − DPO, arithmetic confirmed.
- [ ] OWC components listed and summed; cash and financial items excluded.
- [ ] ΔOWC dollar change ties directionally to WC movements in the CFO section of the cash flow statement.
- [ ] No industry benchmark cited that was not in the user-supplied data.
- [ ] Driver attribution uses "consistent with" or "possible driver" language, not stated causes.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Using revenue as DIO denominator | DIO denominator must be COGS; using revenue understates DIO for high-gross-margin businesses |
| Calling rising DSO a collection failure | Rising DSO could reflect deliberate extension of credit terms to win enterprise customers; state as "consistent with" and list alternatives |
| Treating a single-period CCC as the conclusion | Multi-period trend is required; one bad year could be seasonal or one-time |
| Excluding deferred revenue from OWC as if irrelevant | Deferred revenue movements affect cash quality; analyze separately even if excluded from OWC definition |
| Normalizing WC to peer median without considering business-model differences | A SaaS company and a hardware distributor have structurally different WC profiles; benchmark only against like-model peers |
| Computing WC normalization cash release as a windfall | WC release typically requires operational change (faster collections, slower payments) — flag the operational levers required |
