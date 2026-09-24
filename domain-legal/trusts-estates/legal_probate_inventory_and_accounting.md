---
title: "Probate Inventory and Fiduciary Accounting — Court-Ready Schedules That Reconcile"
category: legal/trusts-estates
description: "Prepare a probate inventory and a fiduciary accounting for an estate (or trust) administration: separate probate from non-probate assets, value each probate asset at date of death with its valuation source, then build a charge-and-discharge (or state-prescribed) accounting with receipts, gains and losses on sale, disbursements, distributions and assets on hand that reconciles to the penny, allocates between principal and income under the governing act, and flags items needing court approval or beneficiary consent. Filing deadlines, forms and allocation rules are marked for verification. Attorney/paralegal work product; distinct from the family's after-death admin checklist and from a pre-death beneficiary review."
techniques:
  - ST-03
  - OC-03
  - DS-02
  - QA-08
  - QA-01
difficulty: intermediate
tags:
  - legal
  - trusts-estates
  - probate
  - inventory
  - fiduciary-accounting
  - estate-administration
  - principal-and-income
  - court-filing
updated: "2026-09-24"
reasoning:
  styles: [systematic, quantitative, evidential]
  stakes: high
  horizon: months
  uncertainty: risk
  evidence_quality: rich
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, table]
  user_role: [attorney, paralegal, fiduciary, accountant]
  mode: [extract, reconcile, audit]
related_prompts:
  - domain-productivity/home-life/home_after_death_admin_checklist.md
  - domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md
  - domain-legal/client-intake-communications/legal_client_status_update_memo.md
  - domain-legal/trusts-estates/legal_will_drafter.md
---

## Objective

Produce (1) a date-of-death inventory of probate assets with a valuation source for
every line, (2) a schedule of non-probate assets excluded from it, and (3) a fiduciary
accounting for a stated period that **balances** — charges equal credits — with a
principal/income split and a list of items requiring court approval, beneficiary
consent or verification.

## When to Use

- After appointment of the executor/personal representative, when the inventory is due.
- At an interim or final accounting, before distribution or discharge.
- For a trustee's accounting to beneficiaries under a trust (use the trust's terms
  and state reporting rules in place of probate-court requirements).

**Distinct from:**
- `domain-productivity/home-life/home_after_death_admin_checklist.md` — the family's
  practical sequence (notifications, documents, hand-offs); it hands this work to the
  estate's attorney and accountant.
- `domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md` —
  reviews designations and titling while the person is alive.
- Estate income-tax and estate-tax returns — this accounting feeds them but does not
  prepare them.

## Your Input

- **Jurisdiction (required):** state and county of administration; type of
  administration (formal/supervised, informal/independent, small-estate) `[VERIFY]`.
- **Governing instrument:** will or trust, and any provisions on accountings,
  principal/income, or waiver of accountings.
- **Date of death**, date of appointment, and **accounting period**.
- **Asset data:** statements at date of death, appraisals, titles, beneficiary
  designations, joint-ownership records.
- **Transactions for the period:** bank and brokerage statements, sale closing
  statements, invoices paid, distributions made.
- **Court's required form or schedule order**, if the court prescribes one.

## Constraints

**Must:**
- Classify every asset as probate or non-probate, with the reason (beneficiary
  designation, joint with survivorship, trust-owned, TOD/POD).
- Give each inventory value a source (statement, appraisal, assessor, blue-book,
  fiduciary estimate) and a date.
- Keep carrying values at inventory value; recognise gain or loss only on disposition.
- Reconcile: **opening inventory + receipts + gains − losses − disbursements −
  distributions = assets on hand**, and prove assets on hand against end-of-period
  statements.
- Allocate receipts and disbursements between principal and income under the
  instrument or the state's principal-and-income act `[VERIFY: act and rule]`.
- List items requiring court approval or beneficiary consent (fiduciary and attorney
  fees, sales to interested parties, non-pro-rata distributions) `[VERIFY]`.

**Must Not:**
- Invent filing deadlines, form numbers, fee schedules, or statutory allocation rules.
  Use `[VERIFY: …]` / `[CITE: …]`.
- Include non-probate assets in the probate inventory total.
- Net receipts against disbursements; show both gross.
- Present an accounting that does not balance; if it cannot be made to balance, state
  the difference and the investigation plan.

## Method

1. **Asset census.** List everything the decedent owned or had an interest in.
2. **Probate / non-probate sort** with reasons; non-probate schedule kept separate.
3. **Valuation.** Date-of-death value and source; flag items needing formal appraisal
   `[VERIFY: when required]`.
4. **Inventory.** In the court's schedule order if prescribed; otherwise by category.
5. **Transaction ledger.** Classify each transaction: receipt (principal/income), sale
   (gain/loss vs. inventory value), disbursement (principal/income), distribution
   (cash or in kind at carrying value).
6. **Build the accounting** (charges and credits) and compute assets on hand.
7. **Prove assets on hand** against closing statements; resolve differences.
8. **Approval and consent list; verification list; proposed distribution schedule**
   (final accountings only).

## Output Format

```markdown
# Estate of [Decedent] — Inventory and [Interim/Final] Accounting
**Court:** [county, state] · **Case no.:** [ ] · **Fiduciary:** [ ]
**Date of death:** [ ] · **Accounting period:** [ ] to [ ]

## A. Inventory (probate assets at date of death)
| # | Asset | Value | Source & date | Notes |
**Total probate inventory:** $

## B. Non-probate assets (not included)
| Asset | How it passes | Recipient |

## C. Accounting — Charges
| Item | Principal | Income | Total |
## D. Accounting — Credits
| Item | Principal | Income | Total |
## E. Assets on hand at period end (proof)
| Asset | Carrying value | Statement value | Difference |
## F. Balance check
Charges $ = Credits + Assets on hand $ → [BALANCED / DIFFERENCE $]
## G. Items requiring court approval / consent
## H. Verification list
```

## Worked Example

**Input (abridged):** Informal administration; decedent died 10 March; will leaves
tangibles to daughter and residue equally to two children; accounting period
10 March – 30 September.

**A. Inventory:** checking $42,300 (bank statement, DOD); brokerage $318,500 (DOD
valuation statement); residence $410,000 (licensed appraisal); car $12,000 (valuation
guide); tangibles $8,000 (fiduciary estimate) — **total $790,800**.

**B. Non-probate:** IRA $220,000 → children by beneficiary designation; joint savings
$15,000 → surviving joint owner. **Excluded from total.**

**C. Charges:** inventory $790,800 (principal) + dividends and interest $3,150
(income) = **$793,950**.

**D. Credits:**

| Item | Principal | Income | Total |
|---|---|---|---|
| Loss on sale of car (sold $11,200 vs. $12,000) | 800 | — | 800 |
| Funeral | 9,400 | — | 9,400 |
| Decedent's debts | 6,250 | — | 6,250 |
| Attorney fees `[VERIFY: court approval required?]` | 12,000 | — | 12,000 |
| Property tax on residence `[VERIFY: principal/income allocation]` | 3,900 | — | 3,900 |
| Appraisal fee | 600 | — | 600 |
| Distribution in kind — tangibles to daughter | 8,000 | — | 8,000 |
| **Total credits** | 40,950 | 0 | **40,950** |

**E. Assets on hand:** checking $24,500 (42,300 + 3,150 + 11,200 − 32,150);
brokerage $318,500 (carrying value); residence $410,000 — **$753,000**.

**F. Balance check:** $793,950 = $40,950 + $753,000 → **BALANCED.**

**G. Approval/consent:** attorney fees; in-kind distribution of tangibles at
inventory value (confirm residuary beneficiaries do not object) `[VERIFY]`.

## Verification

- [ ] Every asset classified probate / non-probate with a reason.
- [ ] Every inventory value has a source and date.
- [ ] Carrying values held at inventory; gains/losses recognised only on sale.
- [ ] Charges equal credits plus assets on hand; assets on hand proven to statements.
- [ ] Principal/income allocation stated, with rule source or `[VERIFY]`.
- [ ] Approval and consent items listed.
- [ ] No filing deadline, form number or statutory rule stated unless supplied or `[VERIFY]`.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Including the IRA or joint account in the inventory | Schedule non-probate assets separately; they are not the fiduciary's to administer |
| Showing the car sale proceeds as a receipt | A sale converts an inventoried asset; record only the gain or loss against inventory value |
| Netting income against expenses | Show gross receipts and gross disbursements |
| An accounting that "balances" because assets on hand were plugged | Prove assets on hand against actual statements |
| Allocating everything to principal by default | Apply the instrument or state act and mark the rule `[VERIFY]` |
| Stating the inventory due date or court form from memory | Mark `[VERIFY: local rule / statute]`; missed deadlines can trigger removal or surcharge |
| Paying fees without flagging approval requirements | List every fee and interested-party transaction for approval/consent review |

## Related

- `domain-productivity/home-life/home_after_death_admin_checklist.md` — the family's admin sequence that hands off to this work
- `domain-legal/trusts-estates/legal_will_drafter.md` — dispositive provisions the distribution schedule follows
- `domain-legal/client-intake-communications/legal_client_status_update_memo.md` — reporting administration progress to beneficiaries
- `domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md` — pre-death designations that explain the non-probate schedule
