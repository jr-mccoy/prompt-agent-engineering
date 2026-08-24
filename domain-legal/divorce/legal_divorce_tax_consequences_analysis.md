---
title: "Divorce Tax Consequences Analysis"
category: legal/divorce
description: "Analyze the federal and state tax consequences of a divorce: filing status by year, §1041 nonrecognition on interspousal property transfers, post-TCJA alimony treatment (no deduction/inclusion for instruments executed after 2018), child-related credits and dependency allocation, sale-of-home exclusion, retirement-transfer mechanics (QDRO vs. IRA), basis carryover, and the tax cost embedded in each division option."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - CM-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - tax
  - alimony
  - property-transfer
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_property_division_and_equalization_proposal.md
  - domain-legal/divorce/legal_spousal_support_alimony_analysis.md
  - domain-legal/divorce/legal_retirement_division_and_qdro_framework.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
  - domain-legal/custody/legal_child_support_calculation_framework.md
---

**Purpose:** Surface the tax consequences that should shape a divorce settlement — filing status, the tax-free vs. taxable nature of transfers and support, dependency/credit allocation, the embedded tax cost of each asset — so the division is evaluated on after-tax value. Output is a tax-issue memo flagging items that require a CPA/tax advisor for computation, not tax-return preparation or definitive tax advice.

**When to use:** Structuring property division and support; comparing settlement options on an after-tax basis; allocating dependency exemptions/credits; deciding home sale vs. retention; before signing the MSA.

---

## Your Input

- **Jurisdiction:** [State (for state income/transfer tax); note federal rules apply nationally]
- **Timing:** [Year(s) of separation, divorce finalization, and any instrument execution dates — critical for alimony treatment]
- **Filing facts:** [Marital status as of Dec 31 of each relevant year; who maintains the household; dependents]
- **Support terms:** [Proposed spousal support amount/duration; child support; date of the instrument]
- **Property transfers:** [Assets moving between spouses; basis and built-in gain for each]
- **Residence:** [Home equity, basis, ownership/use history; sale vs. retention plan]
- **Retirement transfers:** [Plans being divided; QDRO vs. IRA transfer]
- **Children:** [Number, ages, who they live with, dependency/credit allocation desired]
- **Carryovers:** [NOLs, capital-loss carryforwards, passive losses, prior-year credits]

---

## Constraints

**Must:**
- Determine **filing status** for each relevant tax year based on marital status as of December 31 and head-of-household eligibility.
- Apply **§1041**: transfers of property between spouses incident to divorce are generally **nonrecognition** events with **carryover basis** — the receiving spouse inherits the basis and the built-in gain `[CITE: …]`.
- Apply the **post-TCJA alimony rule**: for divorce/separation instruments **executed after December 31, 2018**, alimony is **neither deductible by the payor nor includible by the payee**; pre-2019 instruments may retain old treatment unless modified to adopt the new rule `[CITE: …]`. Use the instrument execution date.
- Note **child support is never deductible or taxable**, and address **dependency, Child Tax Credit, and child-care credit** allocation (custodial-parent default; Form 8332 release) `[CITE: …]`.
- Address the **§121 home-sale exclusion** (ownership/use tests; effect of divorce and post-divorce sale) `[CITE: …]`.
- Distinguish **QDRO retirement transfers** (penalty exception, taxable to payee on distribution) from **IRA transfers incident to divorce** (nontaxable if properly titled).
- Compute **after-tax / embedded-tax value** for each divisible asset so options are compared on a like basis; mark amounts requiring computation `[NEED CPA COMPUTATION]`.
- Use placeholders `[CITE: ...]`, `[NEED CPA COMPUTATION]`, `[NEED: ...]` for unsupplied authority, computations, or facts.

**Must Not:**
- Apply pre-TCJA alimony deductibility to a post-2018 instrument (a frequent, costly error).
- Treat a §1041 transfer as a taxable event, or ignore the carryover basis/built-in gain.
- Treat pre-tax retirement dollars as equal to after-tax cash.
- Allocate the dependency/credit to a parent without addressing the custodial-parent default and Form 8332.
- Provide definitive tax computations or return positions — flag for the CPA.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Filing status timeline.** Determine status by year; assess head-of-household eligibility and the year the divorce is final.
2. **Property transfers (§1041).** Confirm nonrecognition; record carryover basis and built-in gain for each transferred asset; flag assets whose tax cost is large relative to value.
3. **Support taxation.** Apply the alimony rule using the instrument execution date; confirm child support is tax-neutral.
4. **Children's tax benefits.** Allocate dependency, CTC, and child-care credit; address Form 8332 release and head-of-household.
5. **Home.** Apply §121 exclusion analysis to retention vs. sale; note basis and gain.
6. **Retirement.** Distinguish QDRO vs. IRA transfer; note taxation and penalty exception.
7. **Carryovers.** Allocate NOLs, capital-loss, and passive-loss carryforwards between the spouses.
8. **After-tax comparison.** Restate each settlement option on an after-tax basis; flag computations for the CPA.

---

## Output Format

```markdown
# DIVORCE TAX CONSEQUENCES ANALYSIS — Case No. {____}
**State:** {…}   **Key dates:** separation {}, instrument executed {}, final {}

## 1. Filing Status by Year
| Year | Marital status 12/31 | Filing status | HOH eligible? |
|---|---|---|---|
| {…} | {…} | {…} | {…} |

## 2. Property Transfers (§1041)
| Asset | FMV | Basis | Built-in gain | Tax-cost note |
|---|---|---|---|---|
| {…} | {$} | {$} | {$} | [NEED CPA COMPUTATION] |
- Nonrecognition; carryover basis to receiving spouse [CITE: …].

## 3. Support Taxation
- Alimony (instrument executed {date}): {deductible/includible — pre-2019} OR {neither deductible nor includible — post-2018} [CITE: …]
- Child support: not deductible, not taxable.

## 4. Children's Tax Benefits
- Dependency / CTC / child-care credit allocation: {…}; Form 8332 release: {…}; HOH: {…}

## 5. Home (§121)
- Ownership/use tests; exclusion available: {…}; retention vs. sale tax effect: {…}

## 6. Retirement Transfers
- QDRO: penalty exception; taxable to payee on distribution. IRA: nontaxable transfer incident to divorce.

## 7. Carryovers
- NOL / capital-loss / passive-loss allocation: {…}

## 8. After-Tax Settlement Comparison
| Option | Pre-tax split | After-tax split | Note |
|---|---|---|---|
| {…} | {…} | {…} | [NEED CPA COMPUTATION] |
```

---

## Verification

- [ ] Filing status determined per year by Dec-31 marital status; HOH addressed.
- [ ] §1041 nonrecognition and carryover basis/built-in gain applied to transfers.
- [ ] Alimony treatment keyed to the instrument execution date (post-2018 vs. pre-2019).
- [ ] Child support confirmed tax-neutral; dependency/CTC/Form 8332 allocated.
- [ ] §121 home-sale exclusion analyzed for retention vs. sale.
- [ ] QDRO vs. IRA transfer distinguished with taxation noted.
- [ ] Carryovers allocated.
- [ ] Options restated after-tax; computations flagged for the CPA.
- [ ] No invented rates or definitive computations; correct alimony rule applied.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating alimony as deductible on a post-2018 instrument | Apply the TCJA rule by execution date: post-2018 = no deduction/inclusion [CITE] |
| Treating a §1041 interspousal transfer as taxable | Nonrecognition with carryover basis; the gain travels with the asset |
| Ignoring built-in gain when comparing assets | Compute embedded tax; compare options after-tax |
| Equating pre-tax 401(k) dollars with cash | Discount retirement for future tax; note QDRO/IRA mechanics |
| Allocating the child dependency without Form 8332 | Custodial parent is the default; a release on Form 8332 is required to shift it |
| Treating child support as deductible/taxable | Child support is tax-neutral |
| Assuming the home-sale exclusion is automatic | Apply §121 ownership/use tests and the divorce-specific rules |
| Providing definitive tax numbers | Flag computations [NEED CPA COMPUTATION] for the tax advisor |
| Ignoring carryforwards in the estate | Allocate NOL/capital-loss/passive-loss carryovers |
| Inventing federal or state tax rates | Use placeholders and defer quantification to the CPA |
