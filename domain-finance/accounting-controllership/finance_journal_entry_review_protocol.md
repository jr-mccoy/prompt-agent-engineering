---
title: "Journal Entry Review Protocol — Completeness, Accuracy, and Segregation of Duties"
category: finance/accounting-controllership
description: "Run a structured journal-entry review: test completeness, accuracy, authorization, support, and period cutoff; enforce preparer/reviewer segregation of duties; risk-rank manual and top-side entries; and flag fraud-risk patterns (round numbers, period-end, unusual accounts)."
techniques:
  - ST-02
  - DT-02
  - QA-01
  - RT-03
  - DS-06
difficulty: intermediate
tags:
  - journal-entry-review
  - segregation-of-duties
  - manual-entries
  - top-side-entries
  - fraud-risk
  - completeness
updated: "2026-06-08"
related_prompts:
  - domain-finance/accounting-controllership/finance_accrual_deferral_logic_builder.md
  - domain-finance/accounting-controllership/finance_sox_internal_controls_designer.md
  - domain-finance/accounting-controllership/finance_account_reconciliation_protocol.md
  - domain-finance/field_guide.md
---

**Informational only — not accounting, audit, or tax advice. Verify all standard references against current authoritative guidance (FASB ASC / IASB IFRS).**

## Objective

Provide a disciplined protocol for reviewing journal entries — manual, recurring, and top-side — that tests each entry for completeness, accuracy, authorization, adequate support, correct accounts, and proper period cutoff; enforces segregation of duties between preparer and reviewer; risk-ranks entries so review effort targets the riskiest items; and surfaces fraud-risk indicators — producing a documented, defensible JE review that withstands SOX and audit scrutiny.

---

## When to Use

- Month-end review of manual and top-side journal entries before the period locks.
- Designing or running a JE-review key control for SOX.
- Investigating a population of entries (e.g., post-close adjustments) for anomalies.
- Standardizing review rigor across a team so high-risk entries get appropriate scrutiny.
- **Do not use** to conclude that fraud has or has not occurred — JE review surfaces risk indicators for investigation, not a fraud determination.

---

## Inputs / Context Required

```
<je_context>
Entity / framework: US GAAP | IFRS
Period:
ERP / GL system:
Population scope: all manual JEs | top-side only | specific accounts | full population sample

ENTRY DATA (per entry, paste or summarize):
- JE number / description:
- Preparer and approver (names/roles):
- Date entered vs effective period date:
- Accounts and amounts (debits/credits):
- Source / support attached (calc, invoice, contract, schedule):
- Entry type: standard recurring | accrual/deferral | reclass | top-side / consolidation | correction:

REVIEW PARAMETERS:
- Materiality / review threshold:
- High-risk accounts (reserves, revenue, manual cash, suspense, intercompany):
- SoD policy (preparer ≠ approver requirement):
</je_context>
```

---

## Constraints

### Must
- Test each entry against the **core review criteria**:
  - **Completeness** — debits = credits; all required entries present (no missing accruals).
  - **Accuracy** — amounts agree to support; correct calculation.
  - **Authorization** — approved by someone with authority, at the right level.
  - **Support** — adequate documentation attached (calc, source document, schedule).
  - **Account validity** — correct GL accounts; no inappropriate use of suspense/clearing.
  - **Period / cutoff** — effective date in the correct period; flag entries dated near or after period end.
- Enforce **segregation of duties**: preparer ≠ approver; flag any self-approved entry.
- **Risk-rank** entries and concentrate review on high-risk items:
```
HIGH risk:  manual, top-side/consolidation, post-close, to reserves/revenue/suspense,
            round-number, period-end-dated, unusual or rarely-used accounts, by senior/management
MED  risk:  manual reclasses, accruals above threshold, intercompany
LOW  risk:  system-generated recurring, immaterial, fully-supported standard entries
```
- Flag **fraud-risk indicators** (RT-03 — pattern stress test): round-dollar amounts, entries just below approval thresholds, entries to seldom-used accounts, entries posted at period-end or after close, entries by individuals outside their normal scope, debits/credits to revenue or reserves lacking support, manual entries to cash.
- Distinguish a **review finding** (must fix: unbalanced, unsupported, unauthorized) from a **review observation** (process note) from a **risk indicator** (warrants inquiry, not necessarily an error).
- Document **preparer and reviewer sign-off** (different individuals) and the disposition of each finding.

### Must Not
- Conclude fraud — surface indicators for investigation only.
- Pass an entry that is unbalanced, unsupported, or self-approved.
- Invent support, approver names, or amounts not supplied.
- Apply a single review depth to all entries — risk-rank and target effort.
- Treat a round-number or period-end entry as automatically improper — it is an indicator requiring inquiry, not proof.
- Allow the same person to be preparer and reviewer.

---

## Instructions

1. **Scope the population.** Confirm what's in scope (all manual, top-side, sampled). Note any data limitations.

2. **Risk-rank each entry** using the criteria above; assign High/Med/Low. High-risk and all top-side/post-close entries get full review.

3. **Run the criteria tests** for each in-scope entry. Use this decision logic per entry:
```
Balanced (DR=CR)?            No → FINDING (unbalanced)
Authorized (approver≠preparer, right level)?  No → FINDING (authorization/SoD)
Supported (adequate docs)?   No → FINDING (unsupported)
Correct accounts?            No → FINDING (misclassification)
Correct period/cutoff?       No → FINDING (cutoff)
Any fraud-risk indicators?   Yes → RISK INDICATOR (inquire)
All clean → PASS
```

4. **SoD enforcement.** Build a preparer-vs-approver check; flag any overlap.

5. **Fraud-indicator scan (RT-03).** Run the population for round-dollar, threshold-skirting, off-hours/period-end, unusual-account, and out-of-scope-author patterns. Log indicators for inquiry.

6. **Disposition findings.** For each finding, record required action, owner, and resolution; for each indicator, record the inquiry and response.

7. **Sign-off.** Preparer (of the review) and an independent reviewer sign; different individuals.

8. **Verification (QA-01).** Confirm every in-scope entry was risk-ranked and tested; confirm no self-approved entry passed; confirm findings vs indicators are correctly distinguished.

---

## Output Format

```
## Journal Entry Review — [Entity], [Period]
Framework: [US GAAP/IFRS] | ERP: [system] | Scope: [population]
Status: REVIEW (surfaces risk indicators; not a fraud determination)

### Risk-Ranking Summary
| Risk tier | Count | Review depth |
|-----------|-------|--------------|
| High | 6 | Full review, all tested |
| Medium | 14 | Tested above threshold |
| Low | 120 | Analytic/sample |

### Entry Review Log
| JE# | Description | Preparer | Approver | Type | Risk | DR=CR? | Supported? | Cutoff OK? | Result |
|-----|-------------|----------|----------|------|------|--------|------------|-----------|--------|
| 1042 | Revenue accrual | J.Lee | M.Ortiz | Accrual | High | Yes | Yes | Yes | PASS |
| 1058 | Reserve adj. | A.Kim | A.Kim | Top-side | High | Yes | No | Yes | FINDING: self-approved + unsupported |
| 1071 | Reclass | T.Roy | M.Ortiz | Reclass | Med | Yes | Yes | Yes | PASS |

### Findings (must resolve)
| JE# | Finding | Action | Owner | Status |
|-----|---------|--------|-------|--------|
| 1058 | Self-approved, unsupported reserve adj. | Obtain support; re-approve by independent mgr | Controller | OPEN |

### Risk Indicators (inquire — not findings)
| JE# | Indicator | Inquiry | Response |
|-----|-----------|---------|----------|
| 1090 | Round $50,000 to suspense at period-end | Why suspense? clearing plan? | [pending] |

### Sign-Off
| Role | Name | Date |
|------|------|------|
| Review preparer | [name] | [date] |
| Reviewer (independent) | [name] | [date] |
```
*All entries, names, and amounts illustrative until populated from the GL.*

---

## Verification

- [ ] Every in-scope entry risk-ranked; high-risk and top-side/post-close fully tested.
- [ ] Each tested entry checked for balance, authorization, support, accounts, cutoff.
- [ ] SoD enforced; no self-approved entry passed.
- [ ] Fraud-risk indicators scanned and logged for inquiry (not concluded as fraud).
- [ ] Findings (must-fix) distinguished from observations and indicators.
- [ ] Each finding has action, owner, status.
- [ ] Review preparer and reviewer are different and both signed.
- [ ] No fabricated support, approvers, or amounts.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Concluding an entry is fraudulent | JE review surfaces risk indicators for inquiry; fraud is determined by investigation, not review |
| Treating every round-number or period-end entry as improper | Classify as a risk indicator requiring inquiry, not a finding; legitimate explanations exist |
| Passing a self-approved entry | Enforce preparer ≠ approver; any self-approval is an automatic finding |
| One-size-fits-all review depth | Risk-rank; concentrate effort on manual, top-side, post-close, and high-risk-account entries |
| Inventing support or approver identities | Use only supplied data; missing support is a finding, not an assumed value |
| Same person reviewing their own review | Independent reviewer sign-off required; different individuals |
