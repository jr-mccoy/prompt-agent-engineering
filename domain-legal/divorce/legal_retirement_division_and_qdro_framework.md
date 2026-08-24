---
title: "Retirement Division and QDRO Framework"
category: legal/divorce
description: "Frame the division of retirement assets in divorce and structure the qualified domestic relations order (QDRO) or equivalent: classify each plan type (defined-benefit pension, defined-contribution, IRA, government/military), apply the marital-portion/coverture fraction, choose shared- vs. separate-interest and the valuation date, address survivor benefits, gains/losses, loans, and early-distribution tax, and produce a plan-specific QDRO drafting checklist."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - retirement
  - qdro
  - coverture
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_property_division_and_equalization_proposal.md
  - domain-legal/divorce/legal_marital_property_characterization_analysis.md
  - domain-legal/divorce/legal_divorce_tax_consequences_analysis.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
  - domain-legal/divorce/legal_financial_affidavit_and_disclosure_builder.md
---

**Purpose:** Determine how each retirement asset is divided and structure the order that effects the division — a QDRO for ERISA plans, a COAP/court order for federal/military plans, or a transfer incident to divorce for IRAs — so the division is enforceable, tax-efficient, and accepted by the plan administrator. Output is a retirement-division memo and a plan-specific QDRO drafting checklist, not the final QDRO (which the plan must pre-approve).

**When to use:** Dividing pensions, 401(k)/403(b), IRAs, or government/military retirement; drafting MSA retirement terms; preparing QDROs after judgment; reviewing the other side's proposed order.

---

## Your Input

- **Jurisdiction & regime:** [State; community/equitable; the state's marital-portion rule]
- **Plans at issue:** [For each: plan name, type (DB pension / DC 401(k)/403(b) / IRA / government (FERS/CSRS/state) / military), participant, balance or accrued benefit, vesting]
- **Service/marriage dates:** [Marriage date; separation/valuation date; participant's service start; total vs. marital service]
- **Coverture inputs:** [Service during marriage vs. total service for DB plans]
- **Division target:** [Percentage or dollar split of the marital portion]
- **Survivor benefit:** [Whether the alternate payee should receive a survivor annuity (DB)]
- **Loans/gains:** [Outstanding plan loans; treatment of post-valuation gains/losses]
- **Plan rules:** [Whether the plan has a model QDRO and its acceptance requirements]

---

## Constraints

**Must:**
- Classify **each plan by type** and apply the correct division vehicle: **QDRO** for ERISA private plans, **COAP** for federal civil service, the **military (USFSPA, 10/10 rule)** order for military, plan-specific orders for state/government plans, and a **transfer incident to divorce** for IRAs (no QDRO needed).
- Apply the **marital-portion rule** — for DB pensions, the **coverture fraction** (marital service ÷ total service) and the state's accrual approach (time-rule vs. frozen-benefit) `[CITE: …]`.
- Choose **shared-interest vs. separate-interest** for DB plans and explain the survivor-benefit consequences.
- Address **survivor benefits** (QPSA/QJSA election) and the cost allocation.
- Address **gains/losses** between valuation and segregation for DC plans, and **outstanding loans**.
- Flag the **tax treatment**: a QDRO distribution to the alternate payee avoids the participant's early-withdrawal penalty and is taxable to the payee; an **IRA transfer incident to divorce** is nontaxable if done correctly `[CITE: …]`.
- Require **plan pre-approval** of the order and conformity to any **model QDRO**.
- Use placeholders `[CITE: ...]`, `[NEED PLAN RULE: ...]`, `[NEED: ...]` for unsupplied authority, plan terms, or figures.

**Must Not:**
- Use a QDRO for an IRA (IRAs divide by transfer incident to divorce, not QDRO).
- Ignore the coverture fraction and split the entire (including premarital) pension.
- Omit the survivor-benefit election (a common, costly QDRO failure).
- Assume a draft QDRO is enforceable without plan administrator pre-approval.
- Invent benefit amounts, coverture figures, or plan rules.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Inventory and classify.** For each plan, identify type and the correct division vehicle.
2. **Marital portion.** For DB plans, compute the coverture fraction and state the accrual approach; for DC plans/IRAs, identify the marital balance as of the valuation date.
3. **Division target.** Apply the percentage/dollar split to the marital portion.
4. **Shared vs. separate interest.** Choose for DB plans; explain survivor-benefit and timing consequences.
5. **Survivor benefits.** Specify QPSA/QJSA treatment and cost allocation.
6. **Gains/losses & loans.** Specify treatment of post-valuation investment experience and outstanding loans for DC plans.
7. **Tax.** Note the QDRO penalty exception, taxation to the payee, and the nontaxable IRA transfer mechanics.
8. **QDRO drafting checklist.** Per plan: required identifying data, division method, dates, survivor election, and plan pre-approval step; reference any model QDRO.

---

## Output Format

```markdown
# RETIREMENT DIVISION & QDRO FRAMEWORK — Case No. {____}
**State / regime:** {…}   **Marriage:** {date}   **Valuation:** {date}

## 1. Plan Inventory & Vehicle
| Plan | Type | Vehicle | Participant | Balance/Accrued | Notes |
|---|---|---|---|---|---|
| {401(k)} | DC/ERISA | QDRO | {…} | {$} | loan: {…} |
| {Pension} | DB/ERISA | QDRO | {…} | {benefit} | coverture below |
| {IRA} | IRA | Transfer incident to divorce | {…} | {$} | no QDRO |
| {Military/FERS} | Gov't | {USFSPA order / COAP} | {…} | {…} | [NEED PLAN RULE] |

## 2. Marital Portion / Coverture
- DB: coverture = marital service {} ÷ total service {} = {%}; accrual approach: {time-rule/frozen} [CITE: …]
- DC/IRA: marital balance as of {valuation date} = {$}

## 3. Division Target
- Alternate payee receives {%/$} of the marital portion of each plan.

## 4. Shared vs. Separate Interest (DB)
- {Choice} — consequences: {survivor/timing}

## 5. Survivor Benefits
- QPSA/QJSA: {election}; cost allocation: {…}

## 6. Gains/Losses & Loans (DC)
- Gains/losses from valuation to segregation: {allocated}; loans: {treatment}

## 7. Tax Notes
- QDRO distribution: penalty exception; taxable to payee. IRA: nontaxable transfer incident to divorce [CITE: …].

## 8. QDRO Drafting Checklist (per plan)
- [ ] Plan/administrator identifying data ; [ ] Division method & dates ; [ ] Survivor election ; [ ] Model-QDRO conformity ; [ ] **Plan pre-approval before entry**
```

---

## Verification

- [ ] Each plan classified and matched to the correct division vehicle (QDRO vs. COAP vs. military order vs. IRA transfer).
- [ ] Coverture fraction applied for DB pensions; marital balance set for DC/IRA.
- [ ] Shared vs. separate interest chosen for DB plans with survivor consequences explained.
- [ ] Survivor benefit (QPSA/QJSA) addressed and cost allocated.
- [ ] Gains/losses and loans addressed for DC plans.
- [ ] Tax treatment noted (QDRO penalty exception/taxation; nontaxable IRA transfer).
- [ ] Plan pre-approval step included in the checklist.
- [ ] No invented benefit amounts, coverture figures, or plan rules.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Using a QDRO to divide an IRA | IRAs divide by transfer incident to divorce, not a QDRO |
| Splitting the entire pension including premarital service | Apply the coverture fraction to isolate the marital portion |
| Omitting the survivor-benefit election | Specify QPSA/QJSA treatment; omission can forfeit the benefit |
| Assuming a draft QDRO is enforceable | Require plan administrator pre-approval and model-QDRO conformity |
| Ignoring post-valuation gains/losses on DC plans | Specify whether the payee shares in investment experience |
| Overlooking outstanding plan loans | Address loan treatment in the division |
| Treating the QDRO distribution as penalty-free to the participant | The exception runs to the alternate payee; clarify taxation |
| Inventing the coverture numerator/denominator | Use service dates supplied; flag missing data [NEED] |
| Using a private-plan QDRO for federal/military retirement | Use COAP/USFSPA orders for government and military plans |
| Ignoring the military 10/10 rule for direct pay | Note the rule's effect on direct payment from DFAS |
