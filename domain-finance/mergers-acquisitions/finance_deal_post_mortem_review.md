---
title: "Deal Post-Mortem Review — Actuals vs. Deal Thesis, Synergy Targets, and Returns"
category: finance/mergers-acquisitions
description: "Run a structured post-acquisition post-mortem: reconcile realized performance against the underwriting thesis, decompose the variance into price, synergy, integration-cost, and market drivers, compute realized vs. underwritten returns, and extract lessons with a hindsight-bias guardrail."
techniques:
  - QA-02
  - NE-11
  - RT-05
  - DS-04
  - NE-06
difficulty: intermediate
tags:
  - post-mortem
  - deal-review
  - synergy-realization
  - variance-analysis
  - lessons-learned
  - m-and-a
updated: "2026-06-08"
related_prompts:
  - domain-finance/mergers-acquisitions/finance_integration_finance_plan.md
  - domain-finance/mergers-acquisitions/finance_synergy_estimation_framework.md
  - domain-finance/mergers-acquisitions/finance_ma_deal_model_builder.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals.**

## Objective

Conduct a disciplined post-acquisition post-mortem that compares realized outcomes against the original deal thesis: reconcile actual revenue, EBITDA, synergies, integration costs, and returns to the underwritten case; decompose the total variance into attributable drivers (price/multiple, synergy realization, integration cost, base-business performance, market/macro); compute realized vs. underwritten IRR/MOIC or ROIC; and extract evidence-based lessons while controlling for hindsight and survivorship bias.

## When to Use

- A scheduled 12/24/36-month review of a completed acquisition against its underwriting
- Diagnosing why a deal under- or over-performed its thesis
- Calibrating the deal team's synergy and price assumptions for future underwriting
- Board, investment-committee, or audit-committee deal-performance review
- Building the institutional feedback loop from realized deals back into the diligence process

## Inputs / Context Required

- Original underwriting: base-case revenue, EBITDA, synergy run-rate and phase-in, integration-cost budget, purchase price/multiple, projected returns (IRR/MOIC or expected ROIC)
- Actuals to date: realized revenue, EBITDA, synergies captured (gross and net), integration costs incurred, current net debt
- Time elapsed since close; current valuation or exit value if realized
- Market/macro context over the holding period (sector growth, rates, FX) — to separate controllable from market-driven variance
- Accounting framework (US GAAP / IFRS); reporting currency

## Constraints

### Must
- Reconcile actuals to the underwritten thesis line by line (NE-11); show underwritten, actual, and variance for revenue, EBITDA, synergies, integration cost, and net debt.
- Decompose total EBITDA/value variance into attributable drivers (DS-04, RT-05): base-business performance, synergy realization, integration-cost overrun, multiple change, and market/macro — variances must sum to the total (a reconciliation, not a list).
- Compute realized vs. underwritten returns (NE-11): IRR/MOIC for a sponsor deal, or ROIC vs. cost of capital for a strategic deal; show the formula.
- Separate controllable drivers (execution, synergy capture, integration discipline) from non-controllable (market, macro, FX).
- Apply a hindsight/outcome-bias guardrail (QA-02): judge the decision on the information available at underwriting, not only on the outcome; flag where a good process had a bad outcome and vice versa.
- Produce a self-audit of the underwriting itself (NE-06): which assumptions were systematically optimistic? Quantify the pattern across categories.
- Extract specific, evidence-tied lessons (RT-05) — each lesson references a quantified finding.

### Must Not
- Conclude "good deal / bad deal" on outcome alone without separating process quality from luck.
- Present a variance list that does not reconcile to the total (unattributed variance hides the real story).
- Attribute all underperformance to market conditions (self-serving) or all to the team (scapegoating) — quantify both.
- Ignore survivorship bias by reviewing only deals that closed; note if comparable killed deals would change the lesson.
- Treat realized return as the sole verdict if the holding period is incomplete; flag interim vs. terminal.

## Instructions

**Step 1 — Thesis reconciliation (NE-11)**

| Metric | Underwritten | Actual | Variance | % Variance |
|---|---|---|---|---|
| Revenue (period) | | | | |
| EBITDA (period) | | | | |
| Synergies (run-rate, net) | | | | |
| Integration costs (cumulative) | | | | |
| Net debt (current) | | | | |

**Step 2 — Variance decomposition (DS-04, RT-05)**

```
Total EBITDA variance = Actual EBITDA − Underwritten EBITDA
Attribute to:
  + Base-business performance (organic vs. plan)
  + Synergy realization (captured vs. underwritten)
  − Integration-cost overrun (one-time vs. budget; if dragging EBITDA)
  ± Mix/pricing
  ± Market/macro (sector volume, FX) — non-controllable
CHECK: Σ attributed variances = Total variance  [required]
```

**Step 3 — Returns reconciliation (NE-11)**

```
Sponsor deal:
  Realized/Projected MOIC = Total equity proceeds (or current equity value) ÷ Equity invested
  Realized/Projected IRR = solve r in −Equity + Σ proceeds_t/(1+r)^t = 0
Strategic deal:
  Realized ROIC = After-tax operating profit attributable to deal ÷ Invested capital (price + integration)
  Compare ROIC to acquirer WACC/hurdle.
Show underwritten vs. realized side by side.
```

**Step 4 — Controllable vs. non-controllable split**

Classify each variance driver; subtotal controllable and non-controllable; state what share of the miss/beat was within the team's control.

**Step 5 — Underwriting self-audit (NE-06, QA-02)**

```
For each major assumption (revenue growth, synergy %, phase-in, multiple, integration cost):
  Was it optimistic / realistic / conservative vs. outcome?
  Is there a systematic pattern (e.g., synergies always overstated, phase-in always too fast)?
Hindsight guardrail: assess decision quality on information available at underwriting;
  flag good-process/bad-outcome and bad-process/good-outcome cases explicitly.
```

**Step 6 — Lessons (RT-05)**

Each lesson cites a quantified finding and proposes a specific change to future underwriting or integration (e.g., "haircut revenue synergies to 0 in base case — realized 15% of underwritten over 24 months").

## Output Format

### Thesis Reconciliation
[Step 1 table]

### Variance Decomposition
[Step 2 — attributed drivers that sum to total; bridge format]

### Returns Reconciliation
[Step 3 — underwritten vs. realized IRR/MOIC or ROIC vs. WACC]

### Controllable vs. Non-Controllable
[Step 4 — subtotals and share-of-miss within control]

### Underwriting Self-Audit
[Step 5 — assumption-by-assumption optimism pattern; process-vs-outcome flags]

### Lessons Learned

| Lesson | Quantified evidence | Change to future practice |
|---|---|---|

## Verification

- [ ] Thesis reconciled line by line with underwritten, actual, and variance.
- [ ] Variance decomposition sums to the total variance (reconciliation check present).
- [ ] Realized vs. underwritten returns computed with stated formulas.
- [ ] Controllable and non-controllable drivers separated and subtotaled.
- [ ] Underwriting assumptions audited for systematic optimism patterns.
- [ ] Hindsight/outcome-bias guardrail applied; process-vs-outcome cases flagged.
- [ ] Each lesson references a quantified finding and a specific practice change.
- [ ] Interim vs. terminal return status stated if holding period incomplete.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| "Good/bad deal" judged on outcome alone | Separate process quality from luck; flag good-process/bad-outcome and the reverse |
| Variance list that doesn't reconcile | Decomposition must sum to total variance; unattributed residual flagged and investigated |
| Blaming the market for all underperformance | Quantify controllable vs. non-controllable; state the in-control share explicitly |
| Hindsight bias rewriting the underwriting | Assess decisions on information available at the time, not only the result |
| Reviewing only closed deals (survivorship) | Note whether comparable killed deals would alter the lesson |
| Treating interim returns as the final verdict | Flag interim vs. terminal; incomplete holding periods not presented as closed cases |
