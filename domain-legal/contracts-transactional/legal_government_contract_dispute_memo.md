---
title: "Government Contract Dispute Memo — REA vs. Certified Claim, Entitlement, Quantum, and Termination for Convenience"
category: legal/contracts-transactional
description: "Attorney-facing memo for a contractor (or agency counsel) on a federal government-contract dispute — whether to pursue a request for equitable adjustment or a certified Contract Disputes Act claim, entitlement theories, quantum method, notice and release defenses, termination-for-convenience settlement posture, forum election, and false-claims exposure — distinct from commercial termination economics and from subcontract flow-down review."
techniques:
  - DT-01
  - RT-03
  - CM-02
  - QA-05
  - QA-12
difficulty: advanced
tags:
  - legal
  - government-contracts
  - contract-disputes-act
  - equitable-adjustment
  - termination-for-convenience
  - government-wont-pay
  - contract-terminated-by-agency
updated: "2026-09-24"
related_prompts:
  - domain-legal/contracts-transactional/legal_subcontractor_flow_down_check.md
  - domain-legal/contracts-transactional/legal_termination_economics_provider_side.md
  - domain-legal/regulatory-compliance/legal_voluntary_disclosure_decision_memo.md
---

# Government Contract Dispute Memo — REA vs. Certified Claim, Entitlement, Quantum, and Termination for Convenience

> **Scope guard — attorney-facing only.** This prompt is for government-contracts counsel for a contractor, subcontractor sponsor, or agency. It does not advise a small business owner without counsel on filing a claim. If the person running it is unrepresented, stop and route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

> **No-fabrication rule.** Do not state the claim-certification dollar threshold, certification wording, contracting-officer decision periods, appeal windows, the claim-submission limitations period, or cost-principle text from memory — mark each `[VERIFY: current statute / FAR provision]`. Do not quote contract clauses not supplied. No invented board or court decisions; use `[CITE: …]` / `[NEED HOLDING: …]`.

## When to Use

- A federal contractor has absorbed extra cost or time from government action (changed work, defective specifications, delay, differing site conditions) and counsel must decide how to seek recovery.
- The government terminated the contract for convenience and a settlement proposal is due, or it terminated for default and conversion to convenience is at issue.
- A request for equitable adjustment has stalled and counsel is deciding whether to convert it into a certified claim.

**Not this prompt if:**
- The dispute is under a commercial (non-government) contract — use `domain-legal/contracts-transactional/legal_termination_economics_provider_side.md`.
- The question is whether prime-contract clauses flowed down to a subcontract — use `domain-legal/contracts-transactional/legal_subcontractor_flow_down_check.md`.
- Counsel has found possible overbilling or a false statement and must decide on disclosure — use `domain-legal/regulatory-compliance/legal_voluntary_disclosure_decision_memo.md` before any claim is submitted.
- The contract is with a state or local government — procurement codes differ; use this structure only with state rules supplied.

## Inputs

- **Jurisdiction (required):** Federal (and which agency) or state/local; the contract's disputes clause; available forums.
- **Contract:** Type (fixed-price, cost-reimbursement, time-and-materials, IDIQ order); relevant clauses as incorporated (changes, differing site conditions, suspension of work, termination, disputes, notice) — quoted.
- **Events:** Chronology of government direction, contractor notices, contracting-officer communications, and modifications signed (with any release language).
- **Cost data:** Actual incurred costs with accounting-system source; estimates; overhead and profit rates; subcontractor claims.
- **Status:** REA submitted? Claim submitted? Contracting-officer final decision issued (date received)? Termination notice (date, type)?
- **Compliance posture:** Any known billing, pricing, or disclosure issues.

## Method

1. **Jurisdiction lock.** Confirm the disputes statute and forum options for the contract. For federal contracts, identify the agency board and court options and note that the forum choice after a final decision is generally binding `[VERIFY: election doctrine]`.
2. **Classify the ask.** REA (negotiation, no final-decision clock, preparation costs may be treated differently) versus certified claim (written demand, sum certain, submitted to the contracting officer for decision, certified if above the threshold `[VERIFY: current certification threshold and required wording]`). Recommend REA-first or claim-now based on the relationship, the limitations clock `[VERIFY: claim-submission period and accrual]`, and interest running from claim receipt.
3. **Entitlement theories.** For each: constructive change (government direction beyond the contract; who directed; authority), defective specifications, differing site conditions (type and notice), government delay or suspension, superior knowledge, breach of the duty to cooperate. For each, list elements `[CITE]`, the supporting evidence, and the government's best defense.
4. **Notice and release defenses.** Check each clause's notice requirement against the chronology; assess prejudice arguments. Check every bilateral modification for release or accord-and-satisfaction language that may bar the claim.
5. **Quantum.** Select a method — actual cost, modified total cost, jury verdict — and explain why; flag total-cost approaches as disfavoured and requiring justification. Add unabsorbed-overhead claims only where the facts show government-caused standby and inability to take other work `[CITE]`. Separate allowable claim-preparation costs from unallowable claim-prosecution costs `[VERIFY: cost principle]`.
6. **Termination for convenience (if applicable).** Settlement proposal content and deadline `[VERIFY]`; recoverable categories — costs incurred on terminated work, reasonable profit on work performed (not anticipated profit on unperformed work), settlement expenses, subcontractor settlements; loss-contract adjustment. For a default termination: grounds, excusable delay, whether the default was proper; conversion to convenience if not.
7. **False-claims and fraud exposure check.** Every figure must be supportable; flag any amount that cannot be traced to records. Inflated or unsupported claims can trigger statutory fraud provisions and forfeiture `[VERIFY]` — this check is mandatory before certification.
8. **Procedural path.** Timeline from submission through final decision (or deemed denial) `[VERIFY: decision periods]`, appeal windows to each forum `[VERIFY]`, the duty to continue performance pending resolution, and interest.
9. **Recommendation.** Path, forum preference, settlement range logic, and immediate actions (notices to send, records to preserve, figures to validate).

## Output Format

```markdown
# Government Contract Dispute Memo — {Contractor} / {Agency} — Contract No. {…}
**Contract type:** {…}  |  **Status:** {REA / claim / final decision received {date} / terminated {date}}  |  **Privileged & Confidential**

## 1. Forum and Statute (with election consequences) [VERIFY]
## 2. REA vs. Certified Claim Recommendation
## 3. Entitlement Analysis
| Theory | Elements [CITE] | Evidence | Government's best defense | Strength |
## 4. Notice and Release Review
| Event | Clause notice requirement (quoted) | Notice given? | Release language in mods? | Risk |
## 5. Quantum
| Element | Method | Amount | Source records | Allowability issue |
## 6. Termination Analysis (if applicable)
## 7. False-Claims / Certification Readiness Check
## 8. Procedural Timeline [VERIFY each deadline]
## 9. Recommendation and Immediate Actions
## 10. Verification Items
```

## Verification

- [ ] Jurisdiction lock: federal vs. state; disputes statute and forums named; each threshold and deadline `[VERIFY]`.
- [ ] Citation discipline: no board or court decision or FAR text asserted without a supplied source or `[CITE]` / `[VERIFY]`.
- [ ] Scope discipline: memo addresses the dispute, not bid-protest or suspension/debarment questions (flag if present).
- [ ] Every clause quoted comes from the supplied contract.
- [ ] Each entitlement theory has evidence and the government's best defense.
- [ ] Every quantum figure traces to a record; untraceable figures are flagged before any certification.
- [ ] Notice and release defenses checked against every signed modification.
- [ ] Termination recovery excludes anticipated profit on unperformed work.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating an REA as a claim (or vice versa) | Classify explicitly; only a proper claim starts the decision and appeal clock |
| Stating the certification threshold or wording from memory | `[VERIFY]`; defective certification has consequences for jurisdiction and timing |
| Ignoring release language in bilateral modifications | Review every modification; releases can bar the claim entirely |
| Pricing by total cost without justification | Use actual cost where records permit; explain any alternative method |
| Claiming anticipated profit on a convenience termination | Recover incurred costs and profit on work performed only |
| Certifying unsupported numbers to "open negotiations" | Run the false-claims check; every figure must be supportable |

## Example

**Input (abridged):** Federal fixed-price construction contract. Fictional contractor Blue Heron Builders encountered rock at depths the boring logs did not show; the contracting officer's representative directed blasting by email. Blue Heron sent written notice nine days after discovery. Cost: $1.1M actual, per job-cost ledger. A later bilateral modification for unrelated paving says "full and final settlement of all claims arising under this modification."

**Output (excerpt):**

> **Entitlement — differing site conditions (Type I).** Contract indications (boring logs) vs. conditions encountered; reasonable reliance; material difference; resulting cost `[CITE: elements]`. Strength: strong on the facts supplied.
>
> **Authority issue.** Direction came from the representative, not the contracting officer; check the representative's delegation letter and whether the contracting officer knew and acquiesced `[NEED: delegation letter]`.
>
> **Notice.** Written notice came nine days after discovery, after blasting was directed. Test the contract's notice clause `[VERIFY: clause and any "before the conditions are disturbed" requirement]`: whether the government had actual knowledge through its representative, and whether it can show prejudice from the delay `[CITE: notice-and-prejudice standard]`. Likely survivable on these facts; document it.
>
> **Release.** Paving modification's release is limited to claims "arising under this modification" — likely does not reach the rock claim, but quote it in full in the memo and flag.
>
> **Path.** Amount exceeds the likely certification threshold `[VERIFY]`. Recommend a certified claim now, given interest runs from receipt, after validating every ledger entry.
