---
title: "Board Finance Package Builder — Results, Forecast, KPIs, and Risks for Board Review"
category: finance/corporate-finance-fpa
description: "Assemble a board-grade finance package: results vs plan with variance commentary, updated forecast and cash runway, a KPI scorecard, and a prioritized risk register — concise, decision-oriented, and traceable to source."
techniques:
  - OC-01
  - DS-06
  - RT-05
  - DS-02
  - QA-04
difficulty: intermediate
tags:
  - board-package
  - board-reporting
  - kpi-scorecard
  - fpa
  - cash-runway
  - executive-communication
updated: "2026-06-08"
related_prompts:
  - domain-finance/corporate-finance-fpa/finance_budget_variance_investigator.md
  - domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Assemble a board-grade finance package that a board can use to make decisions: a tight results-vs-plan section with variance commentary, an updated forecast with cash runway, a focused KPI scorecard with trends and targets, and a prioritized risk register with mitigations. The package must be concise, decision-oriented, free of vanity metrics, and every number traceable to source.

---

## When to Use

- Preparing the quarterly (or monthly) board/finance-committee package.
- Standardizing a recurring board finance section that is currently ad hoc or bloated.
- A first board meeting post-financing where reporting expectations are being set.
- Investor/lender update packages that follow a similar structure.
- **Do not use** to produce audited statements, legal/governance materials, or the full strategy deck; this is the finance section and its supporting commentary.

---

## Inputs / Context Required

```
<board_package_inputs>
Company / stage (seed, growth, late, public-style governance):
Period covered: [Q_/FY_] | Reporting currency:
Audience: [board | finance committee | lenders | investors]

FINANCIALS:
- Results for the period: actual vs plan vs prior year (P&L summary, cash)
- Variance commentary inputs (or run finance_budget_variance_investigator.md first)
- Updated forecast (current rolling forecast) and prior forecast for comparison
- Cash balance, burn/FCF, and runway (months of cash)

KPIs:
- The KPIs the board cares about with definitions, targets, and history
  (e.g., ARR, NRR, gross margin, CAC payback, churn, units, utilization)

RISKS:
- Known risks/issues with likelihood, impact, owner, and mitigation status

CONTEXT:
- Decisions/approvals being sought from the board this meeting
- Prior board's open action items
</board_package_inputs>
```

---

## Constraints

### Must
- Lead with a **one-page executive summary**: the 3–5 things the board must know, decisions sought, and headline numbers.
- Present results as **actual vs plan vs prior year** with a short, causal variance commentary (RT-05 — evidence-based, no hand-waving).
- Show the **updated forecast vs prior forecast** (what changed and why), not just the new number.
- Report **cash runway** explicitly (DS-02):
  ```
  Monthly net burn = (Beginning cash − Ending cash) / months   (for cash-burning companies)
  Cash runway (months) = Current cash / Monthly net burn        (state at current burn)
  ```
- Use a **KPI scorecard** with defined metrics, target, actual, trend (▲/▼), and RAG status; every KPI must have a precise definition (DS-02).
- Include a **prioritized risk register** (DS-06): risk, likelihood, impact, owner, mitigation, status — ranked, not exhaustive.
- Keep it **decision-oriented and concise**: separate the headline from the appendix; avoid vanity metrics.
- Make every figure **traceable to source** (which report/model it came from).
- Acknowledge forecast uncertainty and key assumptions (QA-04).

### Must Not
- Bury the headline in pages of detail or include vanity metrics that don't drive decisions.
- Present KPIs without definitions or targets (a metric without a target is decoration).
- Show a new forecast without explaining the change from the prior forecast.
- Omit cash runway for a cash-consuming company.
- Invent figures, KPI values, or risk assessments; require them as inputs.
- Use a RAG/status color without a stated threshold for what triggers it.

---

## Instructions

1. **Draft the executive summary first.** The 3–5 must-knows, the decisions/approvals requested, and headline financials. Write it last-mile-first so a busy director gets the picture in 60 seconds.

2. **Results vs plan vs prior year (RT-05).** Summarize the P&L and cash. For each material variance, give a one-line, evidence-backed cause (pull from the variance investigator). Distinguish one-time from recurring.

3. **Forecast bridge.** Show prior forecast → current forecast with the drivers of the change (volume, pricing, cost, timing). Present base and a downside (runway-relevant).

4. **Cash and runway (DS-02).** State cash, net burn/FCF, and runway in months at current burn; note the next financing trigger if relevant. For profitable companies, show FCF and leverage/liquidity headroom instead.

5. **KPI scorecard (DS-02 + OC-01).** For each KPI: definition, target, current, prior, trend, RAG with stated thresholds. Keep to the vital few the board governs.

6. **Risk register (DS-06).** List the top risks ranked by likelihood × impact; each with owner, mitigation, and status (new/worsening/stable/improving). Include the disconfirming watch-item for the biggest risk.

7. **Asks and open items.** State the specific approvals/decisions sought and the status of prior board action items.

8. **Verification (QA-01).** Confirm headline numbers tie to the detailed statements and the model; confirm KPI definitions are consistent period-over-period; confirm runway math; state the key forecast assumption.

---

## Output Format

```
## Board Finance Package — [Company], [Period]
Currency: [USD] | Audience: [Board]
NOTE: figures below are ILLUSTRATIVE.

### 1. Executive Summary
- Revenue $[x] ([+/−]% vs plan); EBITDA $[x]; cash $[x]; runway [n] months.
- Headline 1: [e.g., revenue 6% below plan on volume; pricing held]
- Headline 2: [e.g., burn improved; runway extended to Q_]
- DECISIONS SOUGHT: [approve FY budget revision; authorize $X capex]

### 2. Results vs Plan vs Prior Year
| $M | Actual | Plan | Δ vs Plan | Prior Yr | Δ YoY | Commentary |
|----|--------|------|-----------|----------|-------|------------|
| Revenue | 940 | 1,000 | (60) | 820 | +15% | Volume miss (one deal pushed); price held |
| Gross profit | 500 | 540 | (40) | 430 | +16% | Margin in line |
| EBITDA | 90 | 120 | (30) | 70 | +29% | Revenue flow-through; S&M timing |

### 3. Forecast Bridge (prior → current)
| Driver | $M |
|--------|----|
| Prior FY EBITDA forecast | 130 |
| Volume reforecast | (20) |
| Cost actions | +5 |
| Current FY EBITDA forecast | 115 |
Downside (revenue −10%): EBITDA ~$[x]; runway impact [n] months.

### 4. Cash & Runway
| Metric | Value |
|--------|-------|
| Cash | $[x]M |
| Monthly net burn | $[y]M |
| Runway @ current burn | [n] months |
| Next financing trigger | [date/condition] |

### 5. KPI Scorecard
| KPI (definition) | Target | Current | Prior | Trend | RAG |
|------------------|--------|---------|-------|-------|-----|
| NRR (net rev retention) | 110% | 105% | 108% | ▼ | Amber |
| Gross margin | 58% | 57% | 56% | ▲ | Green |
| CAC payback (months) | <12 | 14 | 13 | ▼ | Amber |
RAG thresholds: Green ≥ target; Amber within 10% of target; Red > 10% below.

### 6. Risk Register (ranked)
| Risk | Likelihood | Impact | Owner | Mitigation | Status |
|------|-----------|--------|-------|------------|--------|
| Key-customer concentration | Med | High | CRO | Diversify pipeline | Worsening |
| Runway to next round | Med | High | CFO | Cost actions + raise timing | Stable |
| Hiring plan slip | High | Med | CPO | Recruiter add | Improving |
Watch-item: if top-customer renewal slips, runway shortens by ~[n] months.

### 7. Asks & Open Items
- Approve revised FY budget.
- Prior action items: [status].

### Sourcing
All figures tie to [GL/close pack] and [rolling forecast model] as of [date].
```

---

## Verification

- [ ] Executive summary leads with must-knows and decisions sought.
- [ ] Results shown vs plan and vs prior year with evidence-backed commentary.
- [ ] Forecast change explained (prior → current bridge), not just the new number.
- [ ] Cash runway computed and stated for cash-consuming companies.
- [ ] Every KPI has a definition, target, trend, and RAG with stated thresholds.
- [ ] Risk register ranked with owner, mitigation, and status.
- [ ] Headline numbers tie to source statements/model.
- [ ] Key forecast assumptions and uncertainty acknowledged.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Burying the headline / vanity metrics | Lead with a one-page summary and decisions sought; keep KPIs to the vital few the board governs |
| KPIs without targets or definitions | Every KPI requires a precise definition and target; a metric without a target is decoration |
| New forecast with no explanation | Show the prior→current bridge with the drivers of the change |
| Omitting runway for a burning company | Runway in months at current burn is mandatory; state the next financing trigger |
| RAG colors without thresholds | Define the threshold that triggers Green/Amber/Red |
| Untraceable numbers | Tie headline figures to named source reports/model and date |
