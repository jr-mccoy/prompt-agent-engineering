---
title: "Lease Accounting Analysis — ASC 842 / IFRS 16 Classification and Measurement"
category: finance/accounting-controllership
description: "Analyze a lease under ASC 842 (US GAAP) or IFRS 16: confirm a lease exists, classify (finance vs operating under GAAP; single lessee model under IFRS 16), measure the lease liability and right-of-use asset, and map the P&L geography — with the key GAAP-vs-IFRS lessee divergence flagged."
techniques:
  - NE-11
  - DT-02
  - QA-05
  - RT-05
  - QA-04
difficulty: advanced
tags:
  - asc-842
  - ifrs-16
  - lease-accounting
  - right-of-use-asset
  - lease-liability
  - classification
updated: "2026-06-08"
related_prompts:
  - domain-finance/accounting-controllership/finance_technical_accounting_memo_writer.md
  - domain-finance/accounting-controllership/finance_revenue_recognition_asc606_memo.md
  - domain-finance/financial-statement-analysis/finance_footnote_red_flag_scanner.md
  - domain-finance/field_guide.md
---

**Informational only — not accounting, audit, or tax advice. Verify all standard references against current authoritative guidance (FASB ASC / IASB IFRS).**

## Objective

Produce a defensible lease-accounting analysis under **ASC 842 (US GAAP)** or **IFRS 16 (IFRS)**: confirm the arrangement is (or contains) a lease, determine the lease term and discount rate, classify the lease (finance vs operating under US GAAP; a single on-balance-sheet model for lessees under IFRS 16), measure the lease liability and right-of-use (ROU) asset, and map the resulting income-statement geography — with the **key lessee divergence between the two frameworks flagged explicitly**.

---

## When to Use

- Accounting for a new or modified lease (real estate, equipment, vehicles, embedded leases in supply/service contracts).
- Determining day-one ROU asset and lease liability and the subsequent expense pattern.
- Resolving whether an arrangement is a lease vs a service contract (control of an identified asset).
- Comparing how the same lease hits the P&L under US GAAP vs IFRS for a dual-reporting entity.
- **Do not use** to assert a final auditable conclusion without independent technical review, or to invent specific ASC/IFRS paragraph numbers or thresholds — cite the standard and require confirmation.

---

## Inputs / Context Required

```
<lease_context>
Entity / reporting framework: US GAAP (ASC 842) | IFRS (IFRS 16)
Role: Lessee | Lessor
Asset under lease (description):
Lease commencement date:

LEASE TERMS:
- Non-cancellable base term:
- Renewal / termination / purchase options (and likelihood — reasonably certain?):
- Fixed payments (amount and frequency):
- Variable payments (index/rate-based vs usage-based — note which):
- Residual value guarantee (if any):
- Initial direct costs / lease incentives:

RATES:
- Rate implicit in the lease (if determinable):
- Incremental borrowing rate (IBR) — and basis:

EXEMPTIONS:
- Short-term (≤12 months, no purchase option) election?
- Low-value asset election? (IFRS 16 lessee only)

CONTROL TEST INPUTS (lease vs service):
- Is there an identified asset (explicit/implicit, no substantive substitution right)?
- Does the customer obtain substantially all economic benefits AND direct the use?
</lease_context>
```

---

## Constraints

### Must
- **Step 0 — Is it a lease?** A contract is or contains a lease if it conveys the right to control the use of an **identified asset** for a period in exchange for consideration: (a) identified asset (no substantive supplier substitution right), (b) customer obtains substantially all economic benefits, and (c) customer directs the use. If not a lease → service contract (different accounting).
- Determine the **lease term**: non-cancellable period + renewal options the lessee is **reasonably certain** to exercise (and periods covered by a termination option not reasonably certain to be exercised).
- Determine the **discount rate**: rate implicit in the lease if readily determinable; otherwise the lessee's **incremental borrowing rate (IBR)**.
- Measure the **lease liability** and **ROU asset**:
```
Lease liability = present value of lease payments not yet paid
   PV = Σ [ Payment_t ÷ (1 + r)^t ]   (r = discount rate; t = period)
ROU asset (initial) = Lease liability
   + lease payments made at/before commencement
   + initial direct costs
   − lease incentives received
   + estimated dismantling/restoration costs (if applicable)
```
- **Classification — state the framework divergence explicitly:**
  - **US GAAP (ASC 842), lessee:** dual model — classify as **finance** OR **operating**. Both are on balance sheet (ROU asset + lease liability). Finance if any criterion is met: transfer of ownership; reasonably certain purchase option; lease term = major part of remaining economic life; PV of payments = substantially all of fair value; specialized asset with no alternative use. Otherwise operating.
  - **IFRS 16, lessee:** **single model** — essentially all leases are on balance sheet and accounted for like finance leases (no operating/finance distinction for lessees). **This is THE key divergence — state it.**
- **P&L geography:**
  - **Operating lease (US GAAP):** single straight-line lease expense.
  - **Finance lease (US GAAP) / all lessee leases (IFRS 16):** front-loaded — interest on the liability + straight-line amortization of the ROU asset (total expense higher in early years).
- Address **exemptions**: short-term lease (≤12 months, no purchase option) — both frameworks permit expensing; **low-value asset exemption — IFRS 16 lessee only** (no equivalent recognition exemption in ASC 842).
- For **variable payments**: index/rate-based are included (using the rate at commencement, remeasured on changes); usage/performance-based are excluded and expensed as incurred.
- Use **IRAC discipline** (Issue → Facts → Analysis → Conclusion → FS impact) and a line: *"Verify paragraph references against current ASC 842 / IFRS 16 as of [date]."*

### Must Not
- Invent ASC/IFRS paragraph numbers, the bright-line percentages (do not present specific "75%/90%" thresholds as the standard's text — ASC 842 removed explicit bright lines; use the qualitative "major part" / "substantially all" criteria and note any policy thresholds are the entity's election), or effective dates not independently known to be correct.
- Apply the US GAAP operating/finance distinction to an IFRS 16 lessee — IFRS 16 uses a single model.
- Use the coupon/stated rate when the implicit rate is not determinable — use IBR and state its basis.
- Include usage-based variable payments in the initial liability.
- Treat the low-value exemption as available under US GAAP.
- Conclude "service contract" without failing the identified-asset/control test explicitly.

### Allowed
- Present a structured amortization schedule and the dual-framework P&L comparison.

---

## Instructions

1. **Issue + Facts.** State the question (classification, measurement, expense pattern, or lease-vs-service) and marshal the terms.

2. **Lease-vs-service test.** Apply the identified-asset + control criteria. If it fails, stop and account as a service contract (note conclusion).

3. **Lease term.** Build the term from the non-cancellable period plus reasonably-certain renewals; document the reasonably-certain judgment.

4. **Discount rate.** Use the implicit rate if determinable; else IBR with stated basis (entity's borrowing cost for a similar-term, similar-security borrowing).

5. **Measure liability & ROU asset.** Compute PV of payments; build the ROU asset from the formula. Show the amortization schedule (opening liability, interest, payment, closing liability; ROU amortization).

6. **Classify.**
   - If **US GAAP**: test the five finance-lease criteria (qualitative). Finance if any met; else operating.
   - If **IFRS 16 lessee**: single model — no classification step; account like a finance lease.

7. **Map P&L geography.** Show the expense pattern per framework (straight-line vs front-loaded) and note the EBITDA effect (operating-lease expense is in opex; finance/IFRS 16 splits into amortization + interest, lifting EBITDA).

8. **Exemptions.** Apply short-term and (IFRS only) low-value exemptions if elected.

9. **GAAP-vs-IFRS divergence section.** State the single-model vs dual-model difference and the resulting P&L/EBITDA and ratio effects.

10. **Conclude + FS impact + entries.** Day-one and subsequent entries; balance-sheet and income-statement effects; disclosures.

11. **Verification (QA-04/QA-05).** Re-foot the amortization schedule (liability rolls to zero; interest = rate × opening balance); confirm classification matches framework; confirm no fabricated bright-line thresholds.

---

## Output Format

```
## Lease Accounting Analysis — [Asset]
Framework: [ASC 842 (US GAAP) | IFRS 16 (IFRS)] | Role: [Lessee/Lessor]
Commencement: [date] | Status: DRAFT — requires technical review
Confidence: [High / Medium / Low]

### Issue
[Classification / measurement / expense-pattern / lease-vs-service question.]

### Relevant Facts
[Term, payments, options, rates, costs/incentives.]

### Analysis
**Lease vs service:** identified asset [Y/N]; benefits [Y/N]; directs use [Y/N] → [Lease / Service]
**Lease term:** [base] + [reasonably-certain renewals] = [n] periods
**Discount rate:** [implicit / IBR — basis] = [r]%
**Measurement:**
| Item | Amount |
|------|--------|
| PV of lease payments (lease liability) | [illustrative] 432,000 |
| + payments at/before commencement | 10,000 |
| + initial direct costs | 5,000 |
| − incentives received | (8,000) |
| **ROU asset (initial)** | **439,000** |

**Classification:**
- US GAAP: [Finance / Operating] — criterion met: [which, or "none → operating"]
- IFRS 16 lessee: single model (accounted like finance lease — no classification)

**Amortization schedule (illustrative):**
| Yr | Opening liability | Interest | Payment | Closing liability | ROU amort. |
|----|-------------------|----------|---------|-------------------|------------|
| 1 | 432,000 | 21,600 | (100,000) | 353,600 | 87,800 |
| … | | | | | |

**P&L geography:**
| Framework / type | Expense pattern | EBITDA effect |
|------------------|-----------------|---------------|
| US GAAP operating | straight-line single lease expense | in opex (no EBITDA lift) |
| US GAAP finance / IFRS 16 lessee | interest + amortization (front-loaded) | lifts EBITDA |

### GAAP vs IFRS Divergence (lessee)
ASC 842 retains a dual model (operating/finance, both on balance sheet); IFRS 16 uses a single on-balance-sheet model. Resulting differences in expense pattern, EBITDA, and leverage optics noted.

### Conclusion + Financial-Statement Impact
[Day-one and subsequent entries; BS/IS effects; disclosures.]

### Key Judgments
[Reasonably-certain renewals, IBR basis, variable-payment treatment.]

Verify paragraph references against current ASC 842 / IFRS 16 as of [date].
```

---

## Verification

- [ ] Lease-vs-service test performed (identified asset + control).
- [ ] Lease term documents reasonably-certain renewal judgment.
- [ ] Discount rate is implicit-or-IBR with stated basis.
- [ ] Lease liability = PV of payments; ROU asset built per formula.
- [ ] Classification follows the correct framework (dual model GAAP / single model IFRS 16 lessee).
- [ ] P&L geography (straight-line vs front-loaded) stated, with EBITDA effect.
- [ ] Short-term / low-value (IFRS only) exemptions applied where elected.
- [ ] Amortization schedule foots: liability amortizes to zero; interest = rate × opening balance.
- [ ] GAAP-vs-IFRS lessee divergence flagged explicitly.
- [ ] No fabricated paragraph numbers or bright-line thresholds presented as standard text.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Applying the US GAAP operating/finance split to an IFRS 16 lessee | State explicitly: IFRS 16 lessees use a single model — no operating/finance distinction |
| Presenting specific bright-line percentages as ASC 842's text | ASC 842 removed explicit bright lines; use qualitative "major part"/"substantially all"; any numeric threshold is the entity's policy election |
| Fabricating ASC/IFRS paragraph numbers or effective dates | Cite the standard by title/number; flag exact subsections for confirmation against current guidance |
| Using the implicit rate when it is not determinable | Default to IBR and state its basis; do not assume implicit rate availability |
| Including usage-based variable payments in the initial liability | Only index/rate-based variable payments are included; usage-based are expensed as incurred |
| Offering the low-value exemption under US GAAP | The low-value recognition exemption is IFRS 16 lessee only; not available under ASC 842 |
