---
title: "Footnote and MD&A Red Flag Scanner"
category: finance/financial-statement-analysis
description: "Systematically scan financial statement footnotes and MD&A for accounting red flags: related-party transactions, off-balance-sheet arrangements, revenue policy changes, significant estimates, and auditor signals."
techniques:
  - DS-04
  - AG-02
  - DT-02
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - footnotes
  - mda
  - red-flags
  - accounting-policy
  - related-party
updated: "2026-06-08"
related_prompts:
  - domain-finance/financial-statement-analysis/finance_quality_of_earnings_review.md
  - domain-finance/financial-statement-analysis/finance_financial_statement_anomaly_detector.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Conduct a structured review of financial statement footnotes, MD&A disclosures, and auditor communications to surface accounting red flags — including related-party transactions, off-balance-sheet arrangements, policy changes that affect comparability, aggressive estimates, and auditor signals — producing a prioritized flag register with confidence ratings and recommended follow-up.

---

## When to Use

- Equity research: initiating coverage or updating a thesis after annual/quarterly filing.
- M&A financial due diligence: footnote review before QoE engagement.
- Credit analysis: annual review of a borrower's 10-K or Annual Report.
- Short-thesis construction: hunting for accounting anomalies.
- Audit planning or internal audit: risk-scoping annual procedures.
- **Do not use** without access to the actual filing text — surface-level summaries are insufficient; the red flags live in the detail.

---

## Inputs / Context Required

```
<footnote_data>
Company name / ticker:
Filing type: 10-K | 10-Q | Annual Report | Other
Period(s) covered:
Accounting framework: US GAAP | IFRS
Auditor: [name; Big Four / other]
Audit opinion type: Unqualified | Qualified | Adverse | Disclaimer | Going concern

PASTE RELEVANT FOOTNOTE AND MD&A SECTIONS:
Priority sections to paste (if full filing is too long):
1. Summary of Significant Accounting Policies
2. Revenue recognition policy
3. Related party transactions
4. Commitments and contingencies
5. Off-balance-sheet arrangements / variable-interest entities (VIEs)
6. Significant estimates and judgments (or Critical Accounting Estimates in MD&A)
7. Segment information
8. Debt and credit facilities
9. Subsequent events
10. Going concern / substantial doubt language (if any)
11. Auditor's report (including PCAOB Critical Audit Matters if applicable)
12. MD&A: Liquidity and capital resources section
13. Any other footnotes the user flags as unusual

Prior year comparisons (optional but valuable):
[Paste same sections from prior 10-K if you want year-over-year policy comparison]
</footnote_data>
```

---

## Constraints

### Must
- Apply a **skeptical default stance** (AG-02): assume each disclosure merits scrutiny; do not assume absence of a flag means the item is clean.
- Organize findings by risk category (see Output Format), not by footnote number.
- Assign each flag: **Severity** (High / Medium / Low) and **Confidence** (High / Medium / Low).
- For every flag, state: (a) what was found verbatim or paraphrased, (b) why it is a flag, (c) what the benign explanation is, and (d) what additional diligence would resolve it.
- Explicitly check for auditor signals: going-concern language, qualified opinions, material weaknesses (ICFR), PCAOB Critical Audit Matters that overlap with the financial statement flags.
- Distinguish between US GAAP and IFRS disclosure requirements where they differ (e.g., IFRS 8 vs. ASC 280 for segment reporting; IAS 24 vs. ASC 850 for related parties).
- Require that related-party transactions be tested against the "arm's-length" standard as disclosed; note where the company asserts but does not demonstrate arm's-length terms.
- Apply the **confirmation-bias guardrail**: for each flag, explicitly state at least one benign alternative explanation.

### Must Not
- Fabricate footnote text or paraphrase it in a way that changes meaning — quote or closely paraphrase the supplied text.
- Classify a disclosure as a "red flag" solely because it is unusual for the analyst — unusual does not equal problematic; require a specific mechanism by which the item could harm investors or creditors.
- Present a flag as confirmed manipulation without direct evidence; use "warrants investigation," "elevated risk," or "inconsistent with X."
- Omit the going-concern / auditor-opinion check even if the user did not explicitly provide the auditor's report — note its absence as a data limitation.

---

## Instructions

1. **Triage the filing for high-priority areas.**
   - Auditor opinion: any language beyond unqualified? Any going-concern doubt? Note PCAOB Critical Audit Matters.
   - Material weakness or significant deficiency in ICFR? Flag immediately as High Severity.
   - Subsequent events: any material event after period end that reframes the statements?

2. **Revenue recognition and policy review.**
   - Is the policy clear, specific, and consistent with industry norms?
   - Has the policy changed vs. prior year? If so: (a) was the change disclosed? (b) was the cumulative catch-up disclosed? (c) does the change inflate current-period earnings?
   - Look for: bill-and-hold language, multiple-element arrangement complexity, estimated variable consideration (refund reserves, rebates) with aggressive estimates, principal vs. agent judgments that gross up revenue.

3. **Related-party transaction scan.**
   - List every disclosed related party and transaction.
   - For each: volume, terms, basis for arm's-length assertion (or absence of assertion).
   - Flags: transactions with officers/directors at non-market rates; loans to related parties; asset transfers that could shift losses off the consolidated entity; revenue from entities in which management has an interest.

4. **Off-balance-sheet and VIE scan.**
   - Operating leases: pre-ASC 842/IFRS 16, off-balance-sheet leases were a classic flag; post-adoption, look for sale-leaseback arrangements at suspicious valuations.
   - VIE disclosures: what entities are consolidated? What is the primary-beneficiary determination? Any entities where consolidation is discretionary?
   - Guarantees, contingent liabilities, letters of credit, take-or-pay contracts disclosed in commitments footnote — quantify the unrecognized exposure.
   - Securitization or receivables sale: does the company transfer AR off balance sheet? If so, test whether it meets derecognition criteria (ASC 860 / IFRS 9).

5. **Significant estimates and judgments.**
   - Identify: revenue variable consideration, allowance for doubtful accounts, inventory NRV write-downs, goodwill and intangible impairment, pension/OPEB assumptions, litigation reserves, deferred tax valuation allowance.
   - For each: is the estimate consistent with external data? Has it moved in a direction that favors reported earnings? Compare to prior-year disclosure.
   - Flag if management changed an estimate without disclosing the reason or quantifying the impact.

6. **Accounting-policy change and restatement check.**
   - Any retrospective or prospective accounting-policy changes? Impact disclosed?
   - Any prior-period adjustments or restatements? Scope and cause?
   - Any "error corrections" (vs. estimate revisions)?

7. **Debt and liquidity disclosure review.**
   - Read the debt footnote: maturity schedule, covenant terms, any covenant waiver or amendment in the period.
   - Read MD&A Liquidity section: is the discussion consistent with the cash flow statement? Does management identify adequate liquidity sources for the next 12 months?
   - Flag: going-concern indicators not formalized as a going-concern opinion (substantial doubt language without explicit going-concern), reliance on revolving credit for operating liquidity, debt covenants with thin headroom.

8. **Segment reporting completeness.**
   - Does the number of reportable segments align with internal management reporting? Aggregation of operating segments into a single "one segment" can mask poor performance in individual units.
   - Are inter-segment transfers disclosed and priced at arm's length?
   - Has segmentation changed? If so, was the restatement of prior-period segment data provided?

9. **Adversarial stress-test (QA-02).**
   - "What is the worst interpretation of each high-severity flag?" State it explicitly.
   - "What would a short seller say about this filing?" Apply that lens to the top 3 flags.
   - "What would make us wrong about each flag?" State the disconfirming evidence.

10. **Verification pass (QA-01).**
    - Confirm: every flag cites a specific disclosed item, not a general concern.
    - Confirm: benign explanation stated for every flag.
    - Confirm: severity and confidence assignments are internally consistent (a High Severity / Low Confidence flag requires a different action than High Severity / High Confidence).

---

## Output Format

```
## Footnote and MD&A Red Flag Report — [Company Name]
Filing: [10-K / 10-Q / Annual Report] for [period]
Framework: [US GAAP / IFRS] | Auditor: [name] | Opinion: [type]
Prepared: [date] | Source: user-supplied footnotes

---

### SUMMARY DASHBOARD

| Risk Category            | Flags Found | Highest Severity | Immediate Action? |
|--------------------------|-------------|------------------|-------------------|
| Auditor / ICFR signals   | 0           | —                | No                |
| Revenue recognition      | 2           | Medium           | Monitor           |
| Related-party            | 1           | High             | Investigate       |
| Off-balance-sheet / VIEs | 1           | Medium           | Quantify          |
| Significant estimates    | 3           | Medium           | Track             |
| Policy changes           | 1           | Low              | Note              |
| Debt / liquidity         | 2           | High             | Investigate       |
| Segment reporting        | 1           | Low              | Note              |
| **Total flags**          | **11**      | **High (2)**     |                   |

---

### SECTION 1: AUDITOR / ICFR SIGNALS

**Finding 1.1** | Severity: N/A | Confidence: High
- Observation: Unqualified opinion; no going-concern language; no material weakness.
- No PCAOB Critical Audit Matters overlap with financial-statement flags.
- Benign interpretation: Clean opinion is consistent with a well-controlled reporting environment.
- ✓ No flags in this category.

---

### SECTION 2: REVENUE RECOGNITION

**Finding 2.1 — Variable Consideration Reserve Reduction** | Severity: Medium | Confidence: Medium
- Observation: [Quote or paraphrase the relevant footnote text.]
- Flag mechanism: Refund reserve declined from $18M to $9M while revenue grew 15%; this release increased revenue by an estimated $9M (0.7% of revenue) without a disclosed business reason.
- Benign explanation: Actual return rates may have improved; product mix may have shifted to non-returnable categories.
- Follow-up required: Compare return rates to prior periods; obtain management's return-rate assumptions.

**Finding 2.2 — Principal vs. Agent Judgment (Gross vs. Net)** | Severity: Medium | Confidence: Low
- Observation: [Footnote text describing the principal/agent determination.]
- Flag mechanism: Company grosses up revenue for [marketplace / distribution service]; under a net presentation, revenue would be approximately $X lower and gross margin % higher. The gross presentation inflates absolute revenue but not gross profit dollars.
- Benign explanation: Gross presentation is correct if the company bears inventory/credit risk — which management asserts but does not quantify.
- Follow-up required: Assess inventory-risk evidence; compare to peer treatment.

---

### SECTION 3: RELATED-PARTY TRANSACTIONS

**Finding 3.1 — Revenue from CEO-Controlled Entity** | Severity: High | Confidence: High
- Observation: [Quote footnote: "During FY[n], the Company recognized $32M of revenue from Entity X, which is controlled by the CEO."]
- Flag mechanism: $32M = 2.4% of total revenue. Terms described as "arm's length" but no independent pricing evidence provided. Entity X's financial condition is undisclosed.
- Benign explanation: May be a legitimate commercial relationship; arm's length assertion may be accurate.
- Worst-case interpretation: Revenue from a related party is a channel for manufacturing earnings; without independent pricing evidence, cannot rule out above-market rates.
- Follow-up required: Obtain contract terms; independent pricing benchmark; entity X's financial statements if available.

---

### SECTION 4: OFF-BALANCE-SHEET / VIEs

**Finding 4.1 — Receivables Securitization Facility** | Severity: Medium | Confidence: Medium
- Observation: [Quote footnote text on AR securitization.]
- Flag mechanism: $85M of AR transferred to a special-purpose entity; derecognized under ASC 860. Retained interest not quantified. If the transfer fails derecognition criteria, AR and debt would both be understated.
- Benign explanation: ASC 860 derecognition is a standard treasury management tool; many investment-grade issuers use it.
- Follow-up required: Confirm true sale opinion exists; quantify retained interest; assess whether the SPE is consolidated under VIE guidance.

---

### SECTION 5: SIGNIFICANT ESTIMATES

**Finding 5.1 — Goodwill Impairment — Zero Write-down Despite Margin Compression** | Severity: Medium | Confidence: Medium
- Observation: [Footnote text: "As of [date], the fair value of all reporting units exceeded their carrying values; no impairment was recorded."]
- Flag mechanism: [Segment X] experienced a 400-bps margin decline and revenue miss vs. acquisition model; goodwill attributable to that acquisition is $420M (32% of total assets). No impairment despite deteriorating fundamentals.
- Benign explanation: Goodwill impairment test uses a DCF and market-comparables approach; near-term margin compression may not change the long-term value if management's projections remain achievable.
- Follow-up required: Obtain or estimate impairment headroom disclosure (ASC 350-20 requires disclosure of headroom for units at risk); assess reasonableness of long-term margin assumptions.

**Finding 5.2 — Deferred Tax Valuation Allowance Released** | Severity: Medium | Confidence: High
...

**Finding 5.3 — Allowance for Doubtful Accounts Declining** | Severity: Medium | Confidence: Medium
...

---

### SECTION 6: DEBT AND LIQUIDITY

**Finding 6.1 — Covenant Waiver Obtained Mid-Year** | Severity: High | Confidence: High
- Observation: [Quote footnote: "In October FY[n], the Company obtained a waiver from its lenders for the leverage covenant for the quarter ended September 30."]
- Flag mechanism: Mid-year covenant waiver indicates the company was in breach or expected breach. Waivers typically carry fees and tighter terms going forward; they are a leading indicator of financial stress.
- Benign explanation: Companies obtain waivers proactively even when breach is not imminent; may reflect conservative management.
- Worst-case interpretation: Cash flow deterioration is more severe than disclosed; waiver may have been necessary to avoid a technical default.
- Follow-up required: Read the waiver terms; model forward covenant compliance under stress; assess lender relationship quality.

---

### SECTION 7: PRIORITY ACTION LIST

| Priority | Finding | Severity | Confidence | Recommended Action |
|----------|---------|----------|------------|-------------------|
| 1 | Related-party revenue from CEO entity (3.1) | High | High | Independent pricing benchmark; entity X financials |
| 2 | Covenant waiver mid-year (6.1) | High | High | Obtain waiver terms; model covenant headroom forward |
| 3 | Variable consideration reserve release (2.1) | Medium | Medium | Obtain return-rate time series; management assumptions |
| 4 | Goodwill impairment — no charge vs. deterioration (5.1) | Medium | Medium | Impairment headroom disclosure; DCF assumptions |
| 5 | AR securitization derecognition (4.1) | Medium | Medium | True-sale opinion; SPE consolidation assessment |

---

### SECTION 8: DISCONFIRMING SCENARIO

Evidence that would reduce the overall risk assessment:
- Related-party transaction (Finding 3.1): Independent pricing study showing arm's-length terms, or Entity X's financial statements showing no financial dependence on the Company.
- Covenant waiver (Finding 6.1): Forward covenant model showing headroom rebuilt by Q2; lender relationship described as supportive in subsequent events.
- Goodwill (Finding 5.1): Disclosure of impairment headroom > 20% for the at-risk reporting unit.
```

---

## Verification

- [ ] Every flag cites a specific disclosed item, not a general concern; no invented footnote text.
- [ ] Severity and confidence assigned to every finding.
- [ ] Benign explanation stated for every flag — no one-sided indictment.
- [ ] Auditor opinion type and any PCAOB Critical Audit Matters reviewed and noted.
- [ ] Policy changes identified and prior-year comparison made if prior data provided.
- [ ] No flag labeled "manipulation" without direct supporting evidence from the filing.
- [ ] Follow-up actions are specific (what to obtain, what to test) not generic ("look into this").
- [ ] US GAAP vs. IFRS differences noted where they affect the disclosure standards being applied.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Flagging all related-party transactions as problematic | Related-party transactions are common and often legitimate; require a specific mechanism for harm (non-arm's length pricing, hidden liability) before flagging as High |
| Treating an aggressive estimate as manipulation | Estimates within GAAP range are permitted; flag as "warrants validation," not fraud |
| Missing flags due to scope limitation | If the user did not paste a footnote section, explicitly note the gap — do not assume absence means clean |
| Calling a qualified opinion definitive about fraud | Qualified opinions are sometimes for scope limitations or disagreements on a single item; characterize the qualification precisely |
| Flagging IFRS disclosures against GAAP standards | Apply the correct framework's disclosure rules to the filer; note where IFRS requires less disclosure than GAAP (e.g., no PCAOB CAMs under IAASB standards) |
| Anchoring on the first flag found and building a narrative | Each flag must be evaluated independently; confirmation bias can cause subsequent flags to be over-weighted if they fit the first narrative |
