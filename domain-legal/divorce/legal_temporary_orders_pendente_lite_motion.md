---
title: "Temporary Orders / Pendente Lite Motion Drafter"
category: legal/divorce
description: "Draft a motion for temporary (pendente lite) orders in a dissolution: temporary spousal and child support, temporary custody and parenting time, exclusive use and possession of the residence, payment of interim expenses and debts, interim attorney's fees, and status-quo/restraining provisions — supported by a declaration and a financial affidavit, sized to the controlling state's standards and local rules."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - divorce
  - family-law
  - temporary-orders
  - pendente-lite
  - motion
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_divorce_petition_complaint_drafter.md
  - domain-legal/divorce/legal_financial_affidavit_and_disclosure_builder.md
  - domain-legal/divorce/legal_spousal_support_alimony_analysis.md
  - domain-legal/custody/legal_temporary_and_emergency_custody_motion.md
  - domain-legal/custody/legal_child_support_calculation_framework.md
---

**Purpose:** Draft a pendente lite motion that preserves the status quo and provides for the family's needs while the dissolution is pending — interim support, custody/parenting time, use of the residence, expense and debt allocation, and fees — with the supporting declaration and financial affidavit the court will require. Output is a filing-ready motion package, not a memo.

**When to use:** Early in a dissolution when interim relief is needed; in response to the other party's temporary-orders motion; when support, housing, or parenting arrangements must be set before trial.

---

## Your Input

- **Jurisdiction:** [State; county; court; local rules and any temporary-orders form]
- **Property regime:** [Community / equitable distribution]
- **Moving party & posture:** [Petitioner/Respondent; whether responding to the other side's motion]
- **Relief sought:** [Temporary support (spousal/child), custody/parenting time, exclusive use of residence, expense/debt payment, insurance continuation, interim fees, status-quo/standing orders]
- **Income & expenses:** [Each party's income, the marital standard of living, monthly expenses, who pays what now]
- **Children & current schedule:** [Names/ages, current parenting arrangement, schools]
- **Residence facts:** [Ownership, occupancy, mortgage, safety considerations]
- **Support guideline model:** [State's temporary-support guideline or formula, if any]
- **Urgency/safety:** [DV, dissipation, lockout, utility shutoff, imminent harm]
- **Existing automatic orders:** [Whether the state's automatic temporary restraining/standing orders are already in effect]

---

## Constraints

**Must:**
- Identify the **state's standard for temporary relief** and any **temporary-support guideline/formula** `[NEED GUIDELINE: …]`; do not invent a formula.
- Anchor support requests to **income and the marital standard of living**, shown in the supporting financial affidavit.
- Note whether the state's **automatic temporary orders / standing orders** already govern (many states impose them on filing/service) and tailor the motion accordingly.
- Tie **exclusive use of the residence** to the state's standard (need, safety, children's stability) — not mere preference.
- Tie **temporary custody/parenting time** to the children's best interests and the existing schedule.
- Support the motion with a **declaration** (facts within personal knowledge) and a **financial affidavit**.
- Address **interim attorney's fees** under the state's need/ability-to-pay or fee-shifting standard `[CITE: …]`.
- Use placeholders `[CITE: ...]`, `[NEED GUIDELINE: ...]`, `[NEED: ...]` for unsupplied authority or facts.

**Must Not:**
- Invent support-guideline numbers, percentages, or formulas, or statutory standards.
- Request exclusive use of the residence on preference alone without a recognized basis.
- Seek temporary custody changes that disrupt the children's status quo without justification.
- Treat temporary orders as a final determination of property, support, or custody.
- Assume automatic orders are or are not in place — confirm.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Caption & relief summary.** Identify the motion and enumerate each form of interim relief sought.
2. **Standard.** State the legal standard for temporary relief and for each specific request (support, use of residence, fees) `[CITE: …]`.
3. **Temporary support.** Apply the state's temporary-support guideline/formula `[NEED GUIDELINE: …]` to the parties' incomes; show the calculation inputs; cross-reference the financial affidavit.
4. **Temporary custody & parenting time.** Propose an interim schedule consistent with the status quo and best interests; address transportation/exchanges.
5. **Exclusive use of residence.** State the basis (need, safety, children's stability); address mortgage/utilities responsibility.
6. **Expense, debt, and insurance allocation.** Allocate interim payment of recurring expenses, debt service, and continuation of health/auto insurance.
7. **Status-quo / restraining provisions.** Request preservation of assets, no dissipation, no canceling insurance, no incurring extraordinary debt (or note these are covered by automatic orders).
8. **Interim attorney's fees.** Address need and ability to pay `[CITE: …]`.
9. **Declaration & financial affidavit.** Draft the supporting declaration (personal-knowledge facts) and reference/attach the financial affidavit.
10. **Proposed order.** Provide a proposed order tracking the relief.

---

## Output Format

```markdown
{STATE} {COURT}, COUNTY OF {COUNTY}
In re the Marriage of {PETITIONER} and {RESPONDENT}   Case No. {____}

MOTION FOR TEMPORARY (PENDENTE LITE) ORDERS

Movant moves for temporary orders as follows: (1) temporary {spousal/child} support; (2) temporary custody and parenting time; (3) exclusive use and possession of the marital residence; (4) allocation of interim expenses, debts, and insurance; (5) interim attorney's fees; (6) status-quo/asset-preservation orders.

I. STANDARD. {Standard for temporary relief and for each request} [CITE: …].

II. TEMPORARY SUPPORT. Under {state temporary-support guideline/formula [NEED GUIDELINE: …]}, with Movant's income of {$} and Respondent's income of {$}, temporary support is {$/month}. {See Financial Affidavit.}

III. TEMPORARY CUSTODY & PARENTING TIME. Proposed interim schedule: {…}, consistent with the children's status quo and best interests. Exchanges: {…}.

IV. EXCLUSIVE USE OF RESIDENCE. Movant requests exclusive use because {need/safety/children's stability}. {Mortgage/utilities responsibility}.

V. EXPENSES, DEBTS, INSURANCE. {Allocation; continuation of health/auto insurance}.

VI. STATUS-QUO / PRESERVATION. {Request, or note coverage by automatic temporary orders}.

VII. INTERIM ATTORNEY'S FEES. {Need and ability to pay} [CITE: …].

WHEREFORE, Movant requests the Court grant the temporary orders set forth above.

DECLARATION OF {MOVANT}
I, {name}, declare under penalty of perjury: {numbered personal-knowledge facts supporting each request}.

[PROPOSED] ORDER ON TEMPORARY ORDERS
The Court orders: {tracking each granted item}.

Attachments: Financial Affidavit; {child-support worksheet}; {exhibits}.
```

---

## Verification

- [ ] Standard for temporary relief and each specific request stated [CITE].
- [ ] Temporary support computed via the state's guideline/formula with inputs shown; affidavit referenced.
- [ ] Interim custody/parenting schedule consistent with status quo and best interests.
- [ ] Exclusive use of residence tied to a recognized basis, not preference.
- [ ] Expense/debt/insurance allocation specified.
- [ ] Status-quo/preservation addressed (or automatic-order coverage noted).
- [ ] Interim fees addressed under need/ability-to-pay or fee-shifting [CITE].
- [ ] Supporting declaration (personal knowledge) and financial affidavit included.
- [ ] Proposed order tracks the relief.
- [ ] No invented guideline numbers, formulas, or statutory standards.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Inventing a temporary-support number or percentage | Apply the state's guideline/formula [NEED GUIDELINE]; show inputs |
| Requesting exclusive use of the home on preference alone | Tie to need, safety, or children's stability per the state's standard |
| Proposing an interim schedule that flips the status quo without cause | Preserve the existing arrangement absent a best-interests justification |
| Treating temporary orders as binding final determinations | State that temporary orders are without prejudice to final determination |
| Ignoring automatic temporary/standing orders already in effect | Confirm and tailor; do not duplicate or contradict |
| Omitting the supporting declaration or financial affidavit | Include both; courts require evidentiary support for temporary relief |
| Requesting fees without a need/ability-to-pay or fee-shifting basis | Cite the state's interim-fee standard [CITE] |
| Failing to address insurance continuation | Allocate health/auto insurance to prevent lapse |
| Inventing the legal standard | Use [CITE] placeholders for the state's standard |
| Ignoring a safety/DV factor in residence and parenting requests | Surface safety considerations and coordinate with any protective order |
