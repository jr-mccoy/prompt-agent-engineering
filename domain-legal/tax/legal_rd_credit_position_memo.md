---
title: "R&D Credit Position Memo (IRC §41)"
category: legal/tax
description: "Counsel-grade position memo supporting (or stress-testing) a research credit claim under IRC §41 — business-component-level application of the four-part test, exclusions, qualified research expense build (wages, supplies, contract research), funded-research and substantiation analysis, refund-claim specificity, and the examination posture — with every percentage, form requirement, and §174 interaction marked for verification."
techniques:
  - RT-05
  - DS-01
  - QA-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - tax
  - rd-credit
  - section-41
  - qualified-research-expenses
  - substantiation
  - tax-controversy
  - development-costs
updated: "2026-09-24"
reasoning:
  styles: [analytic, evidential, adversarial]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: small_team
  output_format: [memo, matrix]
  user_role: [lawyer, analyst]
  mode: [audit, document]
related_prompts:
  - domain-finance/tax-planning/finance_rd_and_credits_mapping.md
  - domain-legal/tax/legal_tax_research_memo.md
  - domain-legal/tax/legal_irs_idr_response.md
  - domain-legal/contracts-transactional/legal_sow_drafter.md
---

# R&D Credit Position Memo (IRC §41)

**Objective:** Produce a position memo that would hold up in an examination: the credit applied **business component by business component**, each one tested against the four-part test with contemporaneous evidence, the statutory exclusions screened, qualified research expenses traced from payroll, supply, and contractor records to the components they support, funded-research risk resolved from the contracts, and the refund-claim or return-disclosure requirements checked. The memo names the weakest components and recommends whether to claim, reduce, or drop them.

**When to use:**
- Before filing an original or amended return (refund claim) that includes the research credit.
- Reviewing a third-party credit study before relying on it.
- Preparing for an examination or responding to an IDR on the credit.

**Distinct from:**
- `domain-finance/tax-planning/finance_rd_and_credits_mapping.md` — screens which activities and incentives might qualify, for planning and for routing to a tax professional; this memo is the tax professional's defensible legal position, with evidence mapping and exam posture.
- `legal_irs_idr_response.md` (this folder) — the procedural response to an IDR; use this memo as the substantive backbone of that response.
- `legal_transfer_pricing_position_paper.md` (this folder) — cross-border pricing of R&D services; flag interaction where a foreign affiliate funds the research.

**Audience:** Tax counsel, tax-controversy attorneys, and credit-study reviewers.

---

## Your Input

- **Taxpayer and years:** [Entity, tax years, controlled-group members]
- **Filing posture:** [Original return / amended return refund claim / under exam / payroll-tax offset election for eligible small business `[VERIFY]`]
- **Business components:** [Products, processes, software, techniques, formulas, inventions — list each with its description]
- **Evidence per component:** [Design docs, test logs, version control history, lab notebooks, meeting notes — describe what exists and when created]
- **QRE data:** [Employees with roles, wages, time allocation method; supplies; contractor invoices and contracts]
- **Contracts:** [Customer contracts (for funded research), contractor agreements (for contract research), grants]
- **Computation method:** [Regular credit / alternative simplified credit; base-period data]
- **§174 treatment for the years:** [How research expenditures were capitalized or deducted — the regime has changed repeatedly `[VERIFY: §174 / §174A for the year]`]
- **Credit study:** [If one exists — paste methodology and findings]

---

## Constraints

### Must
- Apply the test at the **business-component level** (and apply the shrinking-back rule where the whole component fails) `[VERIFY: §41(d)(2)]`.
- Test all four parts separately for each component: §174-eligible expenditure, technological information (hard sciences), business component (new or improved function, performance, reliability, quality), and process of experimentation for substantially all activities `[VERIFY: §41(d)(1) and regulations]`.
- Screen **exclusions**: after commercial production, adaptation, duplication, surveys and routine testing, foreign research, social sciences, funded research, and internal-use software rules `[VERIFY: §41(d)(4) and internal-use software regulations]`.
- Trace **QREs** to components: wages (by qualified services), supplies, and contract research (at the statutory percentage `[VERIFY]`), each with the allocation method disclosed.
- Resolve **funded research** from contract terms: who bears the risk of failure and who retains substantial rights.
- Check **refund-claim specificity** requirements if claiming by amended return `[VERIFY: current IRS requirements for research credit refund claims]` and current **form** requirements `[VERIFY: current Form 6765 and instructions]`.
- Rate each component **Strong / Supportable / Weak / Drop** and state why.

### Must Not
- Treat a credit study's conclusions as evidence; the evidence is the underlying contemporaneous documentation.
- Invent credit rates, contract-research percentages, payroll-offset caps, or base computations.
- Use high-level project descriptions as a substitute for component-level analysis.
- Accept time allocations reconstructed from interviews alone without flagging their weakness.
- Ignore the §174 interaction for the year; it affects taxable income and the credit's net benefit.
- Cite cases not supplied; use `[CITE: …]` / `[NEED HOLDING: …]`.

---

## Instructions

1. **List business components** and group supporting activities under each.
2. **Four-part test per component** with evidence references; note the uncertainty that existed at the outset and how experimentation resolved it.
3. **Exclusions screen** per component; apply internal-use software rules where relevant.
4. **Shrinking-back** where a component fails at the top level.
5. **Funded-research review** of each customer and contractor agreement.
6. **QRE build** — wages, supplies, contract research — traced to components with allocation methodology.
7. **Computation cross-check** (method selected, base data availability) — flag only; do not compute rates from memory.
8. **Filing and disclosure requirements** — form, refund-claim content, statements.
9. **Exam posture** — which components the IRS will attack first, the documents it will request, and the fallback.
10. **Recommendation** — claim / reduce / drop per component, and the documentation to create going forward.

---

## Output Format

```markdown
# Research Credit Position Memo — {Taxpayer}, Tax Year(s) {…}
**Posture:** {original / refund claim / exam}  |  **Privileged & Confidential — prepared at the direction of counsel**

## 1. Summary and Recommendation
| Component | Rating | QREs claimed | Recommendation |
## 2. Component Analysis
### Component: {name}
| Test | Result | Evidence (doc, date) | Weakness |
|---|---|---|---|
| §174 expenditure | | | |
| Technological in nature | | | |
| Permitted purpose | | | |
| Process of experimentation | | | |
**Exclusions:** {…}  **Shrinking-back:** {…}
## 3. Funded-Research Review
| Contract | Risk of failure borne by | Substantial rights retained by | Conclusion |
## 4. QRE Build
| Category | Amount | Component | Allocation method | Evidence quality |
## 5. Computation and §174 Interaction   ([VERIFY] items)
## 6. Filing / Refund-Claim Requirements   ([VERIFY] items)
## 7. Examination Posture
## 8. Documentation Going Forward
```

---

## Worked Example

**Input (abridged):** SaaS company, tax year 2025, amended-return refund claim. Components claimed: (A) new real-time fraud-scoring engine; (B) migration of the billing system to a new cloud provider; (C) customer-specific integration built under a fixed-fee contract. Evidence: Git history and design docs for A; migration runbook for B; SOW for C. Wages allocated by engineer interviews.

**Output (excerpt):**

> **A — Fraud-scoring engine: Supportable → Strong if logs added.** Uncertainty about achievable latency with the chosen model architecture is documented in design docs; Git history shows iterative model and pipeline alternatives evaluated. If the engine serves only internal fraud operations, internal-use software rules apply and raise the bar `[VERIFY: internal-use software regulations]`; the memo must establish third-party interaction or meet the heightened test.
>
> **B — Cloud migration: Drop.** Runbook shows configuration and adaptation of known methods; no technological uncertainty about capability or method is documented. Likely excluded as adaptation / routine.
>
> **C — Customer integration: Weak.** SOW is fixed-fee (taxpayer bears risk of failure) but grants the customer exclusive ownership of deliverables — the taxpayer may not retain substantial rights, making the research funded. Recommend drop unless the SOW or course of dealing shows retained rights.
>
> **QRE evidence:** interview-based allocations are the weakest link; pair them with Git commit attribution and sprint records before filing. **Refund claim:** confirm the claim identifies each component, the individuals, and the information sought, as currently required `[VERIFY]`.

---

## Verification

- [ ] Jurisdiction lock: federal credit (plus any state credit flagged separately).
- [ ] Four-part test applied per business component with evidence citations.
- [ ] Exclusions and internal-use software rules screened.
- [ ] Funded-research conclusion drawn from contract terms.
- [ ] QREs traced to components with allocation method and evidence quality.
- [ ] §174 interaction and form / refund-claim requirements marked `[VERIFY]`.
- [ ] No rates, percentages, or caps invented.
- [ ] Each component rated with a claim / reduce / drop recommendation.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Project-level analysis ("the platform qualifies") | Apply the test per business component; shrink back if needed |
| Relying on the credit study's narrative as proof | Cite contemporaneous documents; the study is not evidence |
| Treating any engineering work as "experimentation" | Show uncertainty at the outset and an evaluative process of alternatives |
| Missing funded research in customer contracts | Read risk-of-failure and rights terms in every relevant contract |
| Stating the contract-research percentage or credit rate from memory | Mark `[VERIFY]`; compute only from supplied rules |
| Ignoring internal-use software rules | Determine whether the software is internal-use and apply the heightened test |
| Filing a refund claim without the required specificity | Check current IRS requirements before filing |
