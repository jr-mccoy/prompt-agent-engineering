---
title: "Child Support Calculation Framework"
category: legal/custody
description: "Apply the controlling state's child-support guideline: identify the model (income-shares, percentage-of-obligor-income, or Melson), determine each parent's income (including self-employment, imputation for voluntary unemployment, and overtime/bonus treatment), apply parenting-time/shared-custody adjustments, add the mandatory add-ons (health insurance, childcare, extraordinary medical/education), and assess deviation factors — producing a worksheet-style computation with a defensible range and the inputs that drive it."
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
  - custody
  - family-law
  - child-support
  - guideline
  - income-determination
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_parenting_plan_drafter.md
  - domain-legal/custody/legal_custody_best_interests_analysis.md
  - domain-legal/divorce/legal_financial_affidavit_and_disclosure_builder.md
  - domain-legal/divorce/legal_divorce_tax_consequences_analysis.md
  - domain-legal/divorce/legal_divorce_postjudgment_modification_and_enforcement.md
---

**Purpose:** Apply the controlling state's child-support guideline to the parents' actual circumstances — identifying the model, determining income, applying parenting-time and add-on adjustments, and assessing deviations — to produce a worksheet-style computation and a defensible support range. Output is a computation framework and position memo; the guideline figure itself depends on the state's tables/software, which must be used for the final number.

**When to use:** Establishing or modifying child support; checking the other parent's proposed number; preparing the support worksheet for a parenting plan, MSA, or hearing.

---

## Your Input

- **Jurisdiction:** [State; the state's guideline model and worksheet/tables `[NEED GUIDELINE: …]` `[CITE: …]`]
- **Children:** [Number, ages, any special needs]
- **Parenting time:** [Overnights/percentage with each parent — drives shared-custody adjustments]
- **Each parent's income:** [Wages, self-employment net, bonus/overtime/commission, benefits, other support received]
- **Imputation facts:** [Voluntary unemployment/underemployment; earning capacity]
- **Add-ons:** [Health-insurance premium for the child, work-related childcare, extraordinary medical, education, travel for parenting time]
- **Other obligations:** [Support for other children, spousal support paid/received]
- **Deviation facts:** [High income above the table, special needs, shared expenses, or other recognized deviation grounds]

---

## Constraints

**Must:**
- Identify the state's **guideline model** — **income-shares**, **percentage-of-obligor-income**, or **Melson** — and apply that model's structure `[NEED GUIDELINE: …]` `[CITE: …]`.
- Determine **each parent's income** per the state's definition: include **self-employment net (with add-backs)**, treat **overtime/bonus/commission** per the state's rule, and address **imputation** for voluntary unemployment/underemployment based on earning capacity.
- Apply **parenting-time / shared-custody adjustments** where the model and overnights trigger them.
- Add the **mandatory add-ons** (the child's health-insurance premium, work-related childcare, extraordinary medical/educational, parenting-time travel) and allocate them per the guideline (often pro rata by income).
- Account for **other support obligations** (other children, spousal support) as the guideline directs.
- Identify **deviation factors** and the **above-guidelines (high-income)** treatment; note deviations require findings.
- Mark the **final figure** as requiring the state's official worksheet/calculator `[NEED GUIDELINE COMPUTATION]`; present inputs and a range, not a fabricated number.
- Use placeholders `[CITE: ...]`, `[NEED GUIDELINE: ...]`, `[NEED GUIDELINE COMPUTATION]`, `[NEED: ...]` for unsupplied authority, tables, or figures.

**Must Not:**
- Invent guideline percentages, table amounts, or the state's income definition.
- Use the wrong model (e.g., percentage-of-income math in an income-shares state).
- Count only W-2 wages and ignore self-employment, bonus, or imputed income.
- Omit mandatory add-ons or apply the wrong allocation.
- Treat child support as negotiable below guideline without a deviation finding (the child's right).
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Model & authority.** Identify the state's guideline model and worksheet/tables `[CITE: …]`.
2. **Income determination.** Compute each parent's guideline income from all sources; address self-employment add-backs and overtime/bonus treatment.
3. **Imputation.** If a parent is voluntarily unemployed/underemployed, address earning-capacity imputation.
4. **Parenting-time adjustment.** Apply shared-custody/overnight adjustments per the model.
5. **Add-ons.** Add health insurance, childcare, extraordinary medical/education, and travel; allocate per the guideline.
6. **Other obligations.** Account for other children and spousal support as directed.
7. **Deviation / high income.** Identify deviation grounds and above-guidelines treatment; note required findings.
8. **Worksheet & range.** Present the inputs in worksheet form, mark the final figure for the official calculator, and give a defensible range.

---

## Output Format

```markdown
# CHILD SUPPORT COMPUTATION FRAMEWORK — Case No. {____}
**State / model:** {income-shares / % of income / Melson} [CITE: …] [NEED GUIDELINE: …]

## 1. Income Determination
| | Parent A | Parent B |
|---|---|---|
| Wages | {$} | {$} |
| Self-employment net (+ add-backs) | {$} | {$} |
| Overtime/bonus/commission | {$} | {$} |
| Imputed (if applicable) | {$} | {$} |
| **Guideline income** | {$} | {$} |

## 2. Parenting Time / Shared-Custody Adjustment
- Overnights: A {} / B {}; adjustment: {…}

## 3. Add-Ons (allocated {pro rata by income})
| Add-on | Amount | A share | B share |
|---|---|---|---|
| Child health-insurance premium | {$} | {$} | {$} |
| Work-related childcare | {$} | {$} | {$} |
| Extraordinary medical/education | {$} | {$} | {$} |

## 4. Other Obligations
- Other children / spousal support: {treatment}

## 5. Deviation / High Income
- Grounds: {…}; above-guidelines treatment: {…}; findings required: {…}

## 6. Worksheet Result & Range
- Base guideline obligation: [NEED GUIDELINE COMPUTATION] (use {state} worksheet/calculator)
- Defensible range: {low–high}; key drivers: {income determination, overnights, add-ons}
```

---

## Verification

- [ ] Correct guideline model identified and applied.
- [ ] Each parent's income computed from all sources; self-employment and overtime/bonus addressed.
- [ ] Imputation addressed where voluntary unemployment/underemployment exists.
- [ ] Parenting-time/shared-custody adjustment applied per the model.
- [ ] Mandatory add-ons included and allocated correctly.
- [ ] Other support obligations accounted for.
- [ ] Deviation/high-income treatment identified with required findings.
- [ ] Final figure deferred to the official worksheet; inputs and range presented.
- [ ] No invented percentages, tables, or income definitions; no sub-guideline deal without a deviation.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Using percentage-of-income math in an income-shares state | Identify and apply the state's actual model [NEED GUIDELINE] |
| Counting only W-2 wages | Include self-employment net, bonus/overtime, and imputed income per the state's definition |
| Skipping imputation for a voluntarily unemployed parent | Address earning-capacity imputation |
| Omitting mandatory add-ons | Add health insurance, childcare, and extraordinary expenses; allocate per the guideline |
| Fabricating the guideline dollar amount | Defer the final number to the official worksheet/calculator [NEED GUIDELINE COMPUTATION] |
| Treating support as freely negotiable below guideline | Below-guideline requires a deviation finding; it is the child's right |
| Ignoring shared-custody overnight adjustments | Apply the model's parenting-time adjustment |
| Mishandling overtime/bonus | Follow the state's rule on variable income (average/include/exclude) |
| Inventing the state's income definition | Use [CITE]/[NEED] placeholders |
| Ignoring other-children/spousal-support offsets | Account for them as the guideline directs |
