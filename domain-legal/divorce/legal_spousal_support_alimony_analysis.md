---
title: "Spousal Support / Alimony Analysis"
category: legal/divorce
description: "Analyze spousal support/alimony under the controlling state's framework: identify the support type (temporary, rehabilitative, durational/limited, permanent, reimbursement), apply the statutory factors or any guideline/formula, assess entitlement, amount, and duration, address modifiability and termination triggers (cohabitation, remarriage, retirement), and integrate the post-TCJA tax treatment — producing a support-position memo with a defensible range."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - RP-01
  - CM-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - spousal-support
  - alimony
  - maintenance
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_financial_affidavit_and_disclosure_builder.md
  - domain-legal/divorce/legal_divorce_tax_consequences_analysis.md
  - domain-legal/divorce/legal_temporary_orders_pendente_lite_motion.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
  - domain-legal/divorce/legal_divorce_postjudgment_modification_and_enforcement.md
---

**Purpose:** Determine the likely spousal-support/alimony/maintenance outcome under the controlling state's law — type, amount, duration, modifiability, and termination — and frame the client's position with a defensible range. Output is an internal support-analysis memo to drive negotiation or trial, not advice to the client and not a guaranteed result.

**When to use:** Assessing support entitlement or exposure; preparing temporary or final support positions; evaluating the other side's demand; structuring support in an MSA; preparing for a support hearing.

---

## Your Input

- **Jurisdiction:** [State; the state's support statute, factor list, and any guideline/formula `[CITE: …]` `[NEED GUIDELINE: …]`]
- **Support type sought:** [Temporary/pendente lite; rehabilitative; durational/limited; permanent; reimbursement]
- **Marriage facts:** [Length of marriage; marital standard of living]
- **Income/earning capacity:** [Each party's income, earning capacity, employability, education, health, age]
- **Need & ability:** [Recipient's need; payor's ability to pay; both budgets]
- **Contributions:** [Homemaking, support of the other's career/education, career sacrifice]
- **Other support:** [Child support interaction; property division providing income]
- **Termination facts:** [Cohabitation, remarriage, retirement, anticipated changes]
- **Tax:** [Instrument execution date — drives post-TCJA treatment]

---

## Constraints

**Must:**
- Identify the **support types** the state recognizes and which fits the facts; do not assume "permanent" or "lifetime."
- Apply the state's **statutory factors** and any **guideline/formula** (some states have a presumptive temporary-support formula and discretionary permanent support) `[CITE: …]` `[NEED GUIDELINE: …]`.
- Tie amount to **need and ability to pay** and the **marital standard of living**, shown from the budgets.
- Address **duration**, including any **length-of-marriage thresholds** or **duration formulas** the state uses.
- Address **modifiability** (modifiable vs. non-modifiable) and **termination triggers** (death, remarriage, cohabitation, retirement) under the state's rule.
- Integrate the **post-TCJA tax treatment** (post-2018 instruments: not deductible/includible) into the net effect and the negotiation.
- Present a **range** (low/likely/high) given the discretionary nature of support, with confidence.
- Use placeholders `[CITE: ...]`, `[NEED GUIDELINE: ...]`, `[NEED: ...]` for unsupplied authority, formulas, or facts.

**Must Not:**
- Invent the state's factor list, guideline formula, duration rules, or case law.
- Assume permanent/lifetime support where the state disfavors or has abolished it.
- Present a single figure where the determination is discretionary.
- Ignore the tax treatment when stating the net effect.
- Double-count business income already capitalized in valuation (double-dip) without addressing it.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Type selection.** Identify which support type(s) the state recognizes and which fits; explain why.
2. **Framework.** State the statutory factors and any guideline/formula `[CITE: …]`.
3. **Amount.** Apply need/ability and the marital standard of living from the budgets; apply any formula; show inputs.
4. **Duration.** Apply length-of-marriage thresholds or duration formulas; state the expected term.
5. **Modifiability & termination.** State whether the award is modifiable and the termination triggers (remarriage, cohabitation, retirement) under the state's rule.
6. **Tax integration.** Apply the post-TCJA treatment; state the net (after-tax) effect on both parties.
7. **Double-dip check.** If business income drove valuation, address whether the same income can fund support.
8. **Range & position.** Provide low/likely/high outcomes with confidence and a recommended position.

---

## Output Format

```markdown
# SPOUSAL SUPPORT / ALIMONY ANALYSIS — PRIVILEGED WORK PRODUCT
**State:** {…} [CITE: …]   **Marriage length:** {…}   **Instrument date (tax):** {…}

## 1. Support Type
- Recognized types: {…}; best fit: {…}; reason: {…}

## 2. Framework
- Statutory factors: {…} [CITE: …]; guideline/formula: {…} [NEED GUIDELINE: …]

## 3. Amount
- Recipient need: {$/mo}; payor ability: {$/mo}; marital standard: {…}; formula result (if any): {$}

## 4. Duration
- Length-of-marriage threshold / duration rule: {…}; expected term: {…}

## 5. Modifiability & Termination
- Modifiable: {yes/no}; terminates on: {death / remarriage / cohabitation / retirement} per {state rule [CITE: …]}

## 6. Tax Integration (post-TCJA)
- Treatment: {not deductible/includible — post-2018}; net effect: payor {…}, payee {…}

## 7. Double-Dip Check
- {Business income capitalized in value also funding support? resolution}

## 8. Range & Recommended Position
| Scenario | Amount | Duration | Confidence |
|---|---|---|---|
| Low | {$} | {…} | {…} |
| Likely | {$} | {…} | {…} |
| High | {$} | {…} | {…} |
- Recommended position: {…}
```

---

## Verification

- [ ] State-recognized support types identified; best fit selected with reasons.
- [ ] Statutory factors and any guideline/formula applied with inputs shown.
- [ ] Amount tied to need, ability, and the marital standard of living.
- [ ] Duration addressed with the state's thresholds/formula.
- [ ] Modifiability and termination triggers stated per the state's rule.
- [ ] Post-TCJA tax treatment integrated into the net effect.
- [ ] Double-dip addressed where business income is involved.
- [ ] Range (low/likely/high) with confidence and a recommended position.
- [ ] No invented factors, formulas, duration rules, or case law.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Assuming permanent/lifetime alimony | Identify the state's recognized types; many disfavor or have ended permanent support |
| Inventing a support formula or factor list | Apply the state's actual factors/guideline [CITE]/[NEED GUIDELINE] |
| Stating one amount where support is discretionary | Present low/likely/high with confidence |
| Ignoring the marital standard of living | Anchor need and amount to the established standard |
| Applying pre-TCJA deductibility to a post-2018 award | Use the current rule; integrate the after-tax net |
| Counting business income for both value and support | Address the double-dip and resolve it |
| Omitting termination triggers | State remarriage/cohabitation/retirement effects per the state |
| Treating a temporary-support formula as the permanent result | Distinguish guideline temporary support from discretionary final support |
| Ignoring earning capacity / imputation | Address employability and any imputed income |
| Inventing duration thresholds | Use [CITE]/[NEED] for the state's duration rules |
