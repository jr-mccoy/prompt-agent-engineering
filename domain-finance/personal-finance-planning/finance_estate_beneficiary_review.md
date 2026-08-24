---
title: "Estate & Beneficiary Review — Analysis Checklist with Document Routing to an Attorney"
category: finance/personal-finance-planning
description: "Run a structured estate and beneficiary review that inventories documents, checks beneficiary designations and titling for consistency with intent, flags gaps and probate/tax exposures, and routes all document drafting and legal questions to a qualified attorney."
techniques:
  - DT-02
  - ST-02
  - DS-06
  - QA-04
  - NE-06
difficulty: intermediate
tags:
  - estate-planning
  - beneficiary-review
  - wills-trusts
  - titling
  - probate
  - document-routing
updated: "2026-06-08"
related_prompts:
  - domain-finance/personal-finance-planning/finance_insurance_needs_analysis.md
  - domain-finance/personal-finance-planning/finance_tax_aware_withdrawal_sequencing.md
  - domain-finance/personal-finance-planning/finance_net_worth_cashflow_diagnostic.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, tax, or legal advice. This prompt performs review and organization only. It does NOT draft, interpret, or validate legal documents. All document drafting, legal interpretation, and execution must be done by a qualified estate-planning attorney; tax questions by a CPA. Personal decisions depend on individual circumstances and jurisdiction.**

## Objective

Perform a structured estate and beneficiary review that: (1) inventories existing estate documents and account designations, (2) checks beneficiary designations and asset titling for consistency with stated intent, (3) flags gaps, conflicts, and probate/tax exposures by severity, and (4) routes every drafting, interpretation, and execution task to a qualified attorney — producing an organized review and question list, not legal advice or documents.

## When to Use

- A household wants to audit whether its estate documents and beneficiary designations are complete and consistent.
- After a life event (marriage, divorce, birth, death, large asset change) that may have outdated designations.
- Preparing organized information before meeting an estate attorney.
- Checking for the common "beneficiary overrides the will" mistake.

## Inputs / Context Required

```
<estate_review_inputs>
Jurisdiction (state/country):         [required — estate law and probate vary]
Documents in place (yes/no/unknown):
  Will:                               [ ]
  Revocable living trust:             [ ]
  Durable power of attorney (financial): [ ]
  Healthcare proxy / medical POA:     [ ]
  Living will / advance directive:    [ ]
Beneficiary designations:
  Retirement accounts (401k/IRA):     [primary / contingent named?]
  Life insurance:                     [primary / contingent named?]
  Transfer-on-death / payable-on-death accounts: [ ]
  Annuities / HSA:                    [ ]
Asset titling:
  Home and real estate:               [sole / joint / trust / TOD]
  Bank/brokerage:                     [titling]
Family:
  Spouse / partner:                   [ ]
  Minor children (guardianship need): [ ]
  Special-needs dependents:           [ ]
Stated intent:
  How the user WANTS assets distributed: [plain-language statement]
ASSUMPTIONS / NOTES:
  Approximate estate size (for tax-exposure flag — route specifics to attorney/CPA).
</estate_review_inputs>
```

## Constraints

### Must
- Require jurisdiction; estate, probate, and tax rules are jurisdiction-specific (QA-04).
- Inventory documents and designations systematically (DT-02, ST-02).
- Check beneficiary designations and titling against stated intent; flag where a designation would OVERRIDE the will/trust (NE-06).
- Flag gaps and exposures by severity (DS-06).
- Route ALL document drafting, interpretation, validity, and execution to a qualified attorney; tax questions to a CPA.
- Produce a question list for the attorney meeting.

### Must Not
- Draft, edit, or supply language for any will, trust, POA, or beneficiary form.
- Interpret whether a document is valid, enforceable, or sufficient.
- Assert estate-tax exemption amounts, thresholds, or rules as fact — mark "[verify with attorney/CPA; current-year]".
- Recommend a specific legal structure as "best" — surface options and route the decision.

## Instructions

**Step 1 — Document inventory (DT-02, ST-02)**

| Document | In place? | Last updated | Notes / gap |
|---|---|---|---|
| Will | | | |
| Revocable trust | | | |
| Financial POA | | | |
| Healthcare proxy | | | |
| Living will | | | |

Flag any missing core document as a gap (severity per Step 4).

**Step 2 — Beneficiary designation review (NE-06)**

| Account/policy | Primary beneficiary | Contingent | Consistent with intent? | Override risk |
|---|---|---|---|---|
| 401(k)/IRA | | | | |
| Life insurance | | | | |
| TOD/POD accounts | | | | |
| HSA/annuity | | | | |

Key check: **beneficiary designations and TOD/POD titling pass OUTSIDE the will and override it.** Flag any account whose designation conflicts with the stated intent or the will. Flag missing/outdated (e.g., ex-spouse still named) and missing contingent beneficiaries.

**Step 3 — Asset titling review**

Check how each major asset is titled (sole, joint with rights of survivorship, tenancy in common, trust, TOD) and whether the titling routes the asset as the user intends (probate vs. non-probate). Flag mismatches; route the fix to the attorney.

**Step 4 — Gap & exposure flags by severity (DS-06)**

| Severity | Finding | Why it matters | Route to |
|---|---|---|---|
| High | (e.g., no will + minor children = court-appointed guardian) | | Attorney |
| High | (e.g., ex-spouse still named beneficiary) | Override risk | Attorney + plan administrator |
| Medium | (e.g., no contingent beneficiaries) | | Attorney |
| Medium | (e.g., possible estate-tax exposure given size) | | Attorney + CPA |
| Low | (e.g., document older than ~5 yrs, review advised) | | Attorney |

**Step 5 — Special situations**

Flag (for attorney) special-needs planning (special-needs trust to preserve benefits), minor-children guardianship, blended-family conflicts, business-succession, and out-of-state property (ancillary probate).

**Step 6 — Attorney meeting question list**

Produce specific, organized questions the user should bring to the estate attorney (and CPA for tax). Do not answer them.

**Step 7 — Self-audit (NE-06)**

Confirm no document language was drafted; confirm every legal/tax item is routed; confirm beneficiary-override checks were performed.

## Output Format

### Document Inventory
[Step 1 table]

### Beneficiary Designation Review
[Step 2 table + override flags]

### Asset Titling Review
[Step 3]

### Gaps & Exposures by Severity
[Step 4 table]

### Special Situations
[Step 5]

### Questions for Your Attorney / CPA
[Step 6 list]

### Routing Note
[All drafting and legal interpretation → attorney; tax → CPA]

## Verification

- [ ] Jurisdiction captured.
- [ ] Document inventory complete with gap flags.
- [ ] Beneficiary designations checked against intent; override risks flagged.
- [ ] Asset titling reviewed for probate/non-probate routing.
- [ ] Findings ranked by severity.
- [ ] No document language drafted or interpreted.
- [ ] All legal/tax items routed to attorney/CPA; tax figures marked "[verify]".
- [ ] Attorney/CPA question list produced.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Drafting or "fixing" document language | Strictly review/organize only; route all drafting to an attorney |
| Asserting a will is valid/sufficient | Do not opine on validity; route to attorney |
| Missing the beneficiary-override trap | Mandatory check: designations/TOD override the will |
| Asserting estate-tax thresholds | Mark "[verify current-year with attorney/CPA]" |
| Recommending a structure as "best" | Surface options; route the decision to the attorney |
| Ignoring jurisdiction | Require it; probate/estate law varies by state/country |
