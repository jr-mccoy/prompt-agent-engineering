---
title: "Revenue Recognition Memo — ASC 606 / IFRS 15 Five-Step Analysis"
category: finance/accounting-controllership
description: "Produce an IRAC-style technical accounting memo applying the ASC 606 / IFRS 15 five-step revenue model to a specific contract or revenue stream — covering variable consideration, significant financing, principal-vs-agent, and over-time vs point-in-time recognition, with GAAP-vs-IFRS divergences flagged."
techniques:
  - NE-11
  - DT-02
  - QA-05
  - RT-05
  - QA-04
difficulty: advanced
tags:
  - asc-606
  - ifrs-15
  - revenue-recognition
  - technical-memo
  - performance-obligations
  - variable-consideration
updated: "2026-06-08"
related_prompts:
  - domain-finance/accounting-controllership/finance_technical_accounting_memo_writer.md
  - domain-finance/accounting-controllership/finance_accrual_deferral_logic_builder.md
  - domain-finance/financial-statement-analysis/finance_quality_of_earnings_review.md
  - domain-finance/field_guide.md
---

**Informational only — not accounting, audit, or tax advice. Verify all standard references against current authoritative guidance (FASB ASC / IASB IFRS).**

## Objective

Produce a rigorous, IRAC-structured technical accounting memo that applies the **ASC 606 (US GAAP) / IFRS 15 (IFRS)** five-step revenue-recognition model to a specific contract, customer arrangement, or revenue stream — reaching a defensible conclusion on *what* revenue to recognize, *when*, and *how much* — and explicitly flagging the few real divergences between US GAAP and IFRS so the conclusion is correct under the entity's framework.

---

## When to Use

- Documenting the accounting position for a new, complex, or modified customer contract (multi-element, SaaS, licensing, milestone, usage-based).
- Supporting a revenue-policy decision before an audit or for a SOX control file.
- Resolving whether revenue is recognized over time or at a point in time, gross or net, now or deferred.
- Training: stepping through the five-step model on a worked example.
- **Do not use** to assert a final auditable conclusion without independent technical review, or to invent specific ASC/IFRS paragraph numbers — cite the standard and require the user to confirm the exact subsection.

---

## Inputs / Context Required

```
<revrec_context>
Entity / reporting framework: US GAAP (ASC 606) | IFRS (IFRS 15)
Revenue stream / contract name:
Period(s) affected:

CONTRACT FACTS (paste the relevant terms):
- Parties and what is promised (goods, services, licenses, support, updates):
- Total contract value and payment terms / schedule:
- Term / duration; renewal or cancellation rights:
- Variable elements (discounts, rebates, refunds, penalties, bonuses, usage fees):
- Acceptance / return / warranty provisions:
- Whether the entity is principal or agent (who controls the good/service; inventory & pricing risk):
- Any financing element (payment timing vs delivery — advance or extended):
- Modifications / change orders (if any):

ENTITY CONTEXT:
- Standalone selling prices (SSP) for each promised item (or method to estimate):
- Practical expedients elected (if any):
- Materiality threshold:
</revrec_context>
```

---

## Constraints

### Must
- Walk the **five steps in order** and reach a sub-conclusion at each:
```
Step 1 — Identify the contract with the customer
Step 2 — Identify the performance obligations (distinct goods/services)
Step 3 — Determine the transaction price
Step 4 — Allocate the transaction price to the performance obligations
Step 5 — Recognize revenue as/when each performance obligation is satisfied
```
- Address, where relevant: **variable consideration** (and the constraint — include only amounts highly probable / not subject to significant reversal), **significant financing component**, **principal vs agent** (control of the specified good/service before transfer), **noncash consideration**, and **consideration payable to a customer**.
- For Step 5, determine **over-time vs point-in-time**: over-time if (a) the customer simultaneously receives and consumes the benefits, (b) the entity creates/enhances an asset the customer controls, or (c) the asset has no alternative use AND the entity has an enforceable right to payment for performance to date. Otherwise point-in-time (control transfer indicators: present right to payment, legal title, physical possession, risks/rewards, customer acceptance).
- Use **IRAC discipline**: Issue → Facts → Analysis (under the standard) → Conclusion → Financial-statement impact.
- Flag **GAAP-vs-IFRS divergences** accurately. The standards are largely converged; note the real differences only, e.g.:
  - **Collectibility** is a Step-1 gating threshold under both, but the subsequent accounting for amounts received before the contract criteria are met can differ in mechanics.
  - **Licensing of IP / sales-based or usage-based royalties** — guidance is closely aligned but application nuances exist; cite the licensing guidance and confirm.
  - **Impairment of contract assets / costs** follows the credit-loss model (ASC 326) under US GAAP vs IFRS 9 under IFRS — different impairment models.
  - **Interim disclosure** requirements differ.
- Add a line: *"Verify the specific paragraph references against current FASB ASC 606 / IASB IFRS 15 (and any subsequent amendments) as of [date]."*
- State a **confidence level** and list judgments that materially affect the conclusion.

### Must Not
- Invent ASC or IFRS paragraph numbers, sub-paragraph letters, effective dates, or thresholds not supplied or independently known to be correct — cite the standard by title/number and flag for confirmation.
- Recognize variable consideration without applying the constraint.
- Default a long-dated payment arrangement to "no financing component" without testing significance.
- Assume principal treatment (gross) without a control analysis.
- Treat ASC 606 and IFRS 15 as identical on impairment of contract assets — they use different impairment models.
- Conclude over-time recognition without satisfying one of the three criteria explicitly.

---

## Instructions

1. **Frame the Issue.** State the precise revenue question (timing, amount, gross/net, over-time/point-in-time, or a combination).

2. **Marshal the Facts.** Summarize the contract terms that drive the analysis; separate facts from assumptions.

3. **Step 1 — Contract exists?** Test the criteria: approval & commitment, identifiable rights, payment terms, commercial substance, and collectibility (probable). Conclude whether a contract exists for accounting purposes; if not, note the deposit/receipt accounting until criteria are met.

4. **Step 2 — Performance obligations.** Identify each promised good/service; test "distinct" (capable of being distinct AND distinct within the context of the contract). Combine non-distinct promises into a single obligation. List the resulting POs.

5. **Step 3 — Transaction price.** Start with fixed consideration; add variable consideration using expected-value or most-likely-amount, then apply the **constraint**. Assess significant financing component (advance/extended payment + significant timing gap). Address noncash and consideration payable to customer.

6. **Step 4 — Allocate.** Allocate transaction price to each PO based on relative **standalone selling price (SSP)**; document SSP source/estimation (adjusted market, expected cost plus margin, or residual where permitted). Allocate discounts and variable consideration to specific POs only where criteria are met.

7. **Step 5 — Recognize.** For each PO, determine over-time vs point-in-time using the criteria above. For over-time, select and justify a measure of progress (output or input method) and apply consistently.

8. **Apply principal-vs-agent** where a third party is involved: does the entity control the specified good/service before transfer? Principal → gross; agent → net (fee/commission).

9. **GAAP-vs-IFRS check.** Confirm the entity's framework and flag any divergence that changes the answer (impairment model, licensing nuance, interim disclosure).

10. **Conclude + impact.** State the conclusion per step, the dollar/timing impact, the entries, and the disclosure implications. Note confidence and key judgments.

11. **Verification (QA-04 / QA-05).** Re-trace allocation arithmetic (sum of allocated price = transaction price); confirm the constraint was applied; confirm every cited reference is to a real standard (no fabricated paragraph numbers).

---

## Output Format

```
## Revenue Recognition Memo — [Contract / Stream]
Framework: [ASC 606 (US GAAP) | IFRS 15 (IFRS)] | Period(s): [__]
Prepared: [date] | Status: DRAFT — requires technical review
Confidence: [High / Medium / Low]

### Issue
[The precise revenue question.]

### Relevant Facts
[Contract terms driving the analysis; assumptions labeled.]

### Analysis Under [ASC 606 / IFRS 15]
**Step 1 — Contract:** [criteria test → conclusion]
**Step 2 — Performance obligations:** 
| PO | Promise | Distinct? | Rationale |
|----|---------|-----------|-----------|
| 1 | [license] | Yes | capable + separable |
| 2 | [support] | Yes | distinct service |
**Step 3 — Transaction price:** 
| Component | Amount | Treatment |
|-----------|--------|-----------|
| Fixed fee | [illustrative] 1,000,000 | included |
| Usage rebate (variable) | (80,000) exp. value | constrained to (80,000) |
| Financing component | [test result] | [adjust / none] |
| **Transaction price** | **920,000** | |
**Step 4 — Allocation (by SSP):**
| PO | SSP | % | Allocated price |
|----|-----|---|-----------------|
| 1 | 700,000 | 70% | 644,000 |
| 2 | 300,000 | 30% | 276,000 |
| **Total** | 1,000,000 | 100% | **920,000** |
**Step 5 — Recognition:**
| PO | Over-time / Point-in-time | Criterion met | Measure of progress | Pattern |
|----|---------------------------|---------------|---------------------|---------|
| 1 | Point-in-time | control transfers at delivery | — | at go-live |
| 2 | Over-time | customer consumes benefits | time-elapsed | ratable over term |

**Principal vs Agent:** [control analysis → gross/net]

### GAAP vs IFRS Divergence
[Only real differences affecting this fact pattern; else "Largely converged; no divergence affects this conclusion."]
Note: contract-asset impairment follows ASC 326 (US GAAP) vs IFRS 9 (IFRS).

### Conclusion
[Per-step conclusion; revenue amount and timing.]

### Financial-Statement Impact & Entries
[Illustrative entries; deferred-revenue / contract-asset effects; disclosures.]

### Key Judgments & Open Items
[SSP estimation, variable-consideration constraint, financing significance, etc.]

Verify all paragraph references against current ASC 606 / IFRS 15 as of [date].
```

---

## Verification

- [ ] All five steps addressed in order, each with a sub-conclusion.
- [ ] Variable consideration estimated AND constrained.
- [ ] Significant financing component explicitly tested.
- [ ] Principal-vs-agent resolved via a control analysis where a third party is involved.
- [ ] Over-time vs point-in-time justified against the stated criteria.
- [ ] Allocation arithmetic ties: sum of allocated price = transaction price.
- [ ] GAAP-vs-IFRS divergences flagged accurately (or "no divergence" stated).
- [ ] No fabricated paragraph numbers, thresholds, or effective dates; standard cited by title/number.
- [ ] Confidence level and key judgments stated.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Fabricating ASC/IFRS paragraph numbers or thresholds | Cite standard by title/number only; flag the exact subsection for user confirmation against current guidance |
| Applying ASC 606 conclusions to an IFRS 15 filer without checking divergence | Confirm framework; flag the real differences (contract-asset impairment ASC 326 vs IFRS 9, licensing nuance, interim disclosure) |
| Recognizing the full variable amount | Always apply the constraint — include only amounts not subject to significant reversal |
| Defaulting to gross (principal) revenue | Require an explicit control analysis before concluding gross |
| Concluding over-time recognition by default | Must satisfy one of the three over-time criteria explicitly, or recognize at a point in time |
| Treating a long-dated payment as having no financing component | Test significance of the timing gap before excluding a financing component |
