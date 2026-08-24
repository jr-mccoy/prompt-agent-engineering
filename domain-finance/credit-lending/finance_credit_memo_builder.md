---
title: "Credit Memo Builder — Facility, Rationale, Risk Rating, Structure, Covenants, Monitoring"
category: finance/credit-lending
description: "Assemble a full, committee-ready credit memorandum: borrower and facility summary, sources/uses, credit rationale, internal risk rating, repayment analysis, structure and covenant package, and ongoing monitoring plan — evidence-required and no invented data."
techniques:
  - DT-02
  - OC-01
  - AG-08
  - NE-11
  - AG-02
difficulty: advanced
tags:
  - credit-memo
  - underwriting
  - risk-rating
  - facility-structure
  - covenants
  - loan-approval
updated: "2026-06-08"
related_prompts:
  - domain-finance/credit-lending/finance_five_cs_credit_analysis.md
  - domain-finance/credit-lending/finance_covenant_design_aid.md
  - domain-finance/credit-lending/finance_debt_capacity_sizing.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, credit, or lending advice. A credit committee and qualified credit officers must review and approve any facility.*

## Objective

Produce a complete, committee-ready credit memorandum for a proposed facility, integrating borrower context, sources and uses, a defensible credit rationale, an internal risk rating on a stated scale, repayment and downside analysis, the proposed structure and covenant package, and a monitoring plan. Every conclusion is tied to supplied evidence; recommendations carry an explicit evidence basis and a skeptical default stance toward approval.

## When to Use

- Drafting a new-money or renewal credit memo for committee
- Documenting an annual review or amendment request
- Standardizing memo quality across a lending team
- Converting a completed 5-Cs analysis (`finance_five_cs_credit_analysis.md`) into a formal write-up
- Stress-testing a thin or overly favorable memo before submission

## Inputs / Context Required

Provide as much as available; missing items are flagged, not invented.

**Borrower & facility**
- Borrower legal name, entity type, ownership, industry / NAICS, jurisdiction, currency
- Facility: type (term / revolver / RCF / bridge), amount, tenor, purpose, pricing, amortization
- Sources and uses of the proposed transaction

**Financial package**
- Historical financials (>=3 years: IS, BS, CF), interim if available
- Management projections (label clearly as management vs. independent)
- Existing debt schedule, lease obligations, contingent liabilities
- Accounting framework (US GAAP / IFRS), auditor and opinion type

**Risk & structure**
- Internal risk-rating scale to use (state it; otherwise `[ASSUMED SCALE]`)
- Proposed collateral, guarantees, lien position, advance rates
- Proposed covenants (or request the model to propose from `finance_covenant_design_aid.md`)
- Sponsor / guarantor strength, prior relationship history

**Context**
- Industry outlook and key risks (supplied; not invented)
- Regulatory or concentration limits applicable to the lender

## Constraints

### Must
- Follow the fixed memo section order (see Output Format) so committees can navigate consistently (OC-01).
- Decompose the analysis into discrete reasoning steps: business -> financial -> repayment -> risk -> structure -> recommendation (DT-02).
- State the internal risk rating on the supplied scale only; never assert an agency-equivalent rating.
- Attach an explicit evidence basis to the recommendation (AG-08): each rationale point cites supplied data.
- Show repayment arithmetic (DSCR, FCCR, leverage) with formula -> inputs -> result.
- Present base / downside / severe stress for repayment capacity.
- Flag projections sourced from management as such, and stress them independently.
- Mark every gap with `[ASSUMED]` / `[MISSING]`.

### Must Not
- Invent financials, ratings, covenant market norms, collateral values, or industry statistics.
- Present management projections as the base case without independent downside testing.
- Recommend approval without a documented downside that the structure survives.
- Map the internal rating to an external agency scale.
- Omit the monitoring plan or the key risks section.

## Instructions

1. **Executive summary & recommendation (write last, place first).** One paragraph: who, what, how much, why, recommended decision, internal rating, and the single largest risk. Keep the recommendation conditional on the analysis below.

2. **Borrower & transaction overview.** Business description, ownership, sources and uses, facility terms.

3. **Financial analysis.** Summarize trend in revenue, margins, cash flow, and leverage. Reference the ratio engine (`finance_ratio_analysis_engine.md`) outputs where available.

4. **Repayment analysis.** Quantify primary (cash flow) and secondary (collateral) repayment:
```
DSCR = CFADS / (Interest + Scheduled Principal)
   CFADS = EBITDA - Cash Taxes - Maintenance Capex - ΔWorking Capital (state definition)

FCCR = (EBITDA - Unfinanced Capex - Cash Taxes) / (Interest + Principal + Rents)

Leverage (pro forma) = (Existing Debt + New Facility) / EBITDA

Loan-to-Value = Facility Amount / Appraised Collateral Value
Collateral Coverage = (Advance Rate x Collateral Value) / Facility Amount
```

5. **Risk rating.** Assign the internal rating from the scorecard inputs and state the dimensions driving it. Show the binding constraint.

6. **Structure & covenant package.** Specify amortization, security, guarantees, and proposed covenants with headroom rationale (cross-reference `finance_covenant_design_aid.md`).

7. **Key risks & mitigants.** Enumerate top risks; for each, the mitigant and residual exposure. Apply a disconfirming check on the recommendation — what would make this credit fail?

8. **Stress testing.** Recompute repayment metrics under base / downside / severe scenarios with internally consistent assumptions.

9. **Monitoring plan.** Reporting frequency, covenant test dates, early-warning triggers (cross-reference `finance_watchlist_early_warning.md`).

## Output Format

```
## CREDIT MEMORANDUM — [Borrower] | [Date] | [Internal Rating: x of (scale)]

### 1. Executive Summary & Recommendation
[Who/what/how much/why | Recommendation | Rating | Largest risk]

### 2. Borrower & Transaction Overview
[Business, ownership, jurisdiction]
Sources & Uses:
| Sources | $ | Uses | $ |
|---|---|---|---|
| New facility | | Acquisition / refi / capex | |
| Equity / sponsor | | Fees & expenses | |
| **Total** | | **Total** | |

### 3. Financial Analysis
[Revenue, margin, cash flow, leverage trend — cite line items / periods]

### 4. Repayment Analysis
DSCR = CFADS / Debt Service = X.XXx
FCCR = ... = X.XXx
Pro-forma Leverage = X.Xx
LTV = X% | Collateral Coverage = X.Xx
Primary repayment source: [cash flow]
Secondary repayment source: [collateral / guarantee]

### 5. Internal Risk Rating
| Dimension | Assessment | Driver |
|---|---|---|
| ... | ... | ... |
**Rating: [x] on [scale]** — binding constraint: [name]

### 6. Structure & Covenant Package
| Term | Proposed |
|---|---|
| Amount / tenor / amortization | |
| Security / lien position | |
| Guarantees | |
| Financial covenants | [with headroom] |
| Pricing | |

### 7. Key Risks & Mitigants
| Risk | Mitigant | Residual Exposure |
|---|---|---|
| ... | ... | ... |
Disconfirming check: [what would make this credit fail]

### 8. Stress Testing
| Metric | Base | Downside | Severe |
|---|---|---|---|
| EBITDA | | | |
| DSCR | X.XXx | X.XXx | X.XXx |
| Leverage | X.Xx | X.Xx | X.Xx |
| Covenant headroom | | | |

### 9. Monitoring Plan
[Reporting cadence | Covenant test dates | Early-warning triggers]
```

## Verification

- [ ] All nine sections are present and in the fixed order.
- [ ] The recommendation cites specific supplied evidence; no unsupported assertions.
- [ ] Internal rating uses the stated scale only; no agency-equivalent claim.
- [ ] Repayment metrics show formula -> inputs -> result.
- [ ] Management projections are labeled and independently stressed.
- [ ] Base / downside / severe scenarios are present and internally consistent.
- [ ] Every gap is flagged `[ASSUMED]` / `[MISSING]`.
- [ ] Monitoring plan and key-risks sections are complete.
- [ ] Covenant package references headroom rationale, not invented market norms.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Recommending approval off management's base case | Independent downside required; structure must survive it |
| Asserting an agency-equivalent rating | Internal scale only; agency mapping prohibited |
| Presenting collateral coverage as repayment certainty | Primary (cash flow) and secondary (collateral) repayment stated separately |
| Citing "market-standard" covenants without source | Covenants justified by borrower headroom, not invented norms |
| Thin key-risks section to ease approval | Disconfirming check mandatory: state what makes the credit fail |
| Inventing industry tailwinds | Conditions sourced only from supplied data; gaps flagged |
| Omitting contingent liabilities | Debt and contingent-liability schedule required; absence flagged |
