---
title: "10-K / 10-Q Teardown — Drivers, Risks, and Changes vs. Prior Filings"
category: finance/investing-research
description: "Systematically dissect a 10-K or 10-Q to extract the real operating drivers, surface buried risks and accounting choices, and isolate every material change versus the prior comparable filing — with each finding traced to a section reference."
techniques:
  - DT-02
  - RT-05
  - DS-04
  - QA-01
  - DS-06
difficulty: intermediate
tags:
  - 10-k
  - 10-q
  - filing-analysis
  - disclosure
  - red-flags
  - mda
updated: "2026-06-08"
related_prompts:
  - domain-finance/investing-research/finance_earnings_review_analyzer.md
  - domain-finance/investing-research/finance_management_quality_assessment.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or tax advice.*

## Objective

Perform a structured teardown of a 10-K (annual) or 10-Q (quarterly) filing that (1) extracts the true revenue, margin, and cash-flow drivers from the MD&A and segment notes, (2) surfaces buried risks, accounting-policy choices, and disclosure changes, and (3) isolates every material change versus the prior comparable filing (year-over-year for a 10-K; sequential and year-over-year for a 10-Q). Every finding is tied to a specific filing section so a reviewer can verify it.

## When to Use

- Initiating coverage and needing a ground-truth read of the disclosures
- Post-earnings deep dive after the press release and call
- Detecting changes in language, risk factors, or accounting policy between filings
- Credit or covenant monitoring requiring a disclosure-level read
- Validating or challenging a model's assumptions against the source document

## Inputs / Context Required

**The filing(s)**
- The target 10-K or 10-Q (full text, or the key sections: MD&A, financial statements, notes, risk factors)
- The prior comparable filing for change detection (prior 10-K for annual; prior-year 10-Q and most recent 10-Q for quarterly)
- Filing period-end dates and reporting currency

**Context**
- Accounting framework (US GAAP / IFRS) and any recent standard adoptions
- Segment structure and the company's stated KPIs
- Any specific focus area (e.g., revenue recognition, going-concern, related-party, off-balance-sheet)

**Optional**
- The earnings press release and call transcript for cross-checking tone vs. filing
- Known prior restatements or SEC comment letters

## Constraints

### Must
- Tie every extracted figure and finding to a specific section (MD&A, Note X, Item 1A Risk Factors, etc.) so it is verifiable (RT-05, QA-01).
- Detect and report changes versus the prior comparable filing: new/removed/edited risk factors, accounting-policy changes, segment realignments, and KPI redefinitions (DS-04).
- Separate as-reported figures from any non-GAAP/adjusted figures the company presents; reconcile if a reconciliation is provided.
- Rank findings by materiality/severity (DS-06).
- Flag accounting choices that flatter results (revenue-recognition timing, capitalization vs. expensing, reserve releases, useful-life extensions) without asserting impropriety absent evidence.

### Must Not
- Invent figures, segment data, or risk-factor language not present in the filing. Mark gaps `[NOT DISCLOSED]`.
- Assert fraud or manipulation; describe what changed and why it warrants attention, deferring judgment to evidence.
- Treat non-GAAP metrics as equivalent to GAAP without noting the adjustments.
- Confuse a change in disclosure wording with a change in underlying economics — distinguish the two.

## Instructions

1. **Index the filing.** Map the sections present (Business, Risk Factors, MD&A, Financial Statements, Notes, Controls). Note period-end dates and currency.

2. **Extract the operating drivers (MD&A + segments).** For revenue, margin, and cash flow, pull the company's own stated drivers and the supporting figures. Decompose growth where disclosed:
```
Reported revenue growth = Organic volume + Price/mix + FX + M&A + Other (one-time)
   → attribute each component to the disclosed figure; mark [NOT DISCLOSED] where the company does not break it out
```

3. **Reconcile GAAP vs. non-GAAP.** List each non-GAAP metric, the adjustments to reach it, and whether the adjustments are recurring in nature. Note add-backs that recur every period (a yellow flag).

4. **Read the cash-flow statement against earnings.** Compare net income to cash from operations and free cash flow:
```
FCF = CFO − Capex
Accruals quality (heuristic) = (Net Income − CFO) / Avg Total Assets
   Persistently large positive gap (NI >> CFO) warrants investigation of receivables, inventory, or revenue timing
```

5. **Mine the notes (DT-02).** Examine, at minimum: revenue recognition, segment detail, debt and maturities/covenants, leases, contingencies/litigation, related-party transactions, goodwill/intangibles and impairment triggers, stock-based comp, tax (rate drivers, valuation allowances), and any going-concern language.

6. **Change detection vs. prior filing (DS-04).** Compare to the prior comparable filing and report:
   - New, removed, or materially edited risk factors
   - Accounting-policy or estimate changes (useful lives, reserve methodology, segment definitions)
   - KPI redefinitions or disclosure removals
   - Language shifts in MD&A tone (qualifiers added/removed)

7. **Cross-check tone (if transcript provided).** Note where the filing's cautious language diverges from upbeat call commentary.

8. **Rank findings by severity (DS-06).** Classify each finding Critical / Elevated / Watch, with the section reference and recommended follow-up.

## Output Format

```
## FILING TEARDOWN: [Company] ([Ticker]) | [10-K / 10-Q] | Period: [date] | [GAAP/IFRS]
## Compared against: [prior filing & period]
```

### Driver Decomposition
| Metric | Reported | Disclosed drivers | Section ref |
|---|---|---|---|
| Revenue growth | [%] | Volume / Price / FX / M&A / [NOT DISCLOSED] | MD&A p.X |
| Gross / operating margin | [%] | … | MD&A / Note X |
| CFO vs. Net income | [$ / $] | gap drivers | Cash Flow Stmt |

### GAAP vs. Non-GAAP Reconciliation
| Non-GAAP metric | Adjustments | Recurring? | Section ref |
|---|---|---|---|

### Cash & Earnings Quality
```
FCF = CFO − Capex = [ ]
(NI − CFO)/Avg Assets = [ ]   → [interpretation]
```

### Notes Findings
| Area | Finding | Section ref | Flag |
|---|---|---|---|
| Revenue recognition | | Note X | |
| Debt / covenants | | Note X | |
| Contingencies / litigation | | Note X | |
| Related party | | Note X | |
| Goodwill / impairment | | Note X | |
| Tax | | Note X | |

### Changes vs. Prior Filing
| Change type | Prior | Current | Section ref | Why it matters |
|---|---|---|---|---|
| Risk factor added/removed | | | Item 1A | |
| Accounting policy / estimate | | | Note X | |
| KPI / segment redefinition | | | | |
| MD&A tone shift | | | MD&A | |

### Filing vs. Call Tone (if transcript provided)
| Topic | Filing language | Call language | Divergence note |
|---|---|---|---|

### Severity-Ranked Findings
| Priority | Finding | Section ref | Recommended follow-up |
|---|---|---|---|
| Critical | | | |
| Elevated | | | |
| Watch | | | |

## Verification

- [ ] Every figure and finding cites a specific filing section (MD&A page, Note number, Item 1A).
- [ ] Revenue growth is decomposed to the extent disclosed; undisclosed components are marked `[NOT DISCLOSED]`.
- [ ] Non-GAAP metrics are reconciled to GAAP with each adjustment noted as recurring or not.
- [ ] CFO is compared to net income; accruals gap is computed and interpreted.
- [ ] Risk factors, accounting policies, and KPIs are compared against the prior filing.
- [ ] Findings are ranked by severity, not listed arbitrarily.
- [ ] No fraud or manipulation is asserted absent evidence; findings describe what changed.
- [ ] GAAP/IFRS framework noted where it affects interpretation.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting manipulation from an accounting choice | Describe the choice and its effect; flag for follow-up, defer judgment to evidence |
| Treating non-GAAP "adjusted" figures as the real number | Reconcile to GAAP; flag recurring add-backs explicitly |
| Reading a wording change as an economic change (or vice versa) | Distinguish disclosure-language shifts from underlying-economics shifts |
| Inventing segment or driver breakouts the company didn't disclose | Mark `[NOT DISCLOSED]`; never estimate undisclosed splits as fact |
| Recency bias on the latest quarter | 10-Q analysis includes both sequential and year-over-year comparison |
| Missing buried risk in boilerplate | Notes mining is mandatory and itemized; new/removed risk factors flagged |
| Cherry-picking a single flattering line | Severity ranking forces holistic, prioritized synthesis |
