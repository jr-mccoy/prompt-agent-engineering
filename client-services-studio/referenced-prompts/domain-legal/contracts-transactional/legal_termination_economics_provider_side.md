---
title: "Termination Economics — Provider Side"
category: legal/contracts-transactional
description: "Price the termination provisions of a services agreement from the provider's side: kill fee and its basis, notice period measured against bench cost, payment for work in progress, committed third-party costs, transition assistance obligations, and the asymmetries that make a mutual clause one-sided in effect."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - OC-03
difficulty: advanced
tags:
  - legal
  - contracts
  - termination
  - kill-fee
  - notice-period
  - transition-assistance
  - supplier-side
updated: "2026-09-21"
related_prompts:
  - domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md
  - domain-legal/contracts-transactional/legal_payment_terms_and_late_fee_review.md
  - domain-legal/contracts-transactional/legal_sow_drafter.md
  - domain-legal/contracts-transactional/legal_negotiation_position_paper.md
---

**Purpose:** Put a number on the termination provisions of a services agreement from
the provider's side. Not the clause language — that is covered elsewhere — but the
**economics**: what early termination costs you, what the notice period is worth
against your bench, what you are owed for work in progress and committed costs, and
what transition assistance you have agreed to provide for free.

**When to use:** Before signing, once the termination clause language is settled, and
whenever a client signals an early exit. Also use when a long engagement is being
renewed and the termination terms are being rolled forward unexamined.

**Why this exists as a separate prompt.** Termination is one of the five clause
families in `legal_contract_clause_redline_targeted.md`, which produces the drafting
positions. Do not duplicate that work. This prompt starts where it ends: given the
clause as it will be signed, what does termination actually cost the provider, and
which specific asks would change that number most? `kill fee` appears nowhere else in
this repository.

**This is not legal advice.** Enforceability of kill fees and liquidated-damages
provisions, construction as penalties, and mandatory notice requirements vary by
jurisdiction. This produces a costed position and questions for counsel.

---

## Inputs required

- The termination clause as drafted, both convenience and cause limbs
- Engagement value, duration, and delivery profile over time
- Your cost profile: committed subcontractors, licences, travel, reserved capacity
- Your bench position — from
  `domain-business-strategy/client-services/services_capacity_and_utilization_planner.md`
- Replacement lead time for work of this size
- Any transition or handover obligations elsewhere in the agreement

---

## Review sequence

### 1. Identify the four limbs, and check for asymmetry

| Limb | Question |
|---|---|
| Client terminates for convenience | Notice? Compensation? |
| Client terminates for cause | What counts as cause, and is there a cure period? |
| Provider terminates for convenience | Available at all? On what notice? |
| Provider terminates for cause | Does non-payment count? At what threshold? |

A clause that reads as mutual is frequently one-sided in effect. Common asymmetries
to flag:

- Client may terminate for convenience; provider may not
- "Cause" is defined broadly for the client and narrowly for the provider
- The provider's cure period is short; the client's is long or absent
- Non-payment is not listed as cause for the provider — check against
  `legal_payment_terms_and_late_fee_review.md`

### 2. Price the notice period against your bench

Notice is only worth what you can do with it.

```
Notice period (days)
Replacement lead time for work of this size (days)
Exposure = replacement lead time − notice period
```

A 30-day notice period against a 90-day replacement lead time leaves 60 days of
unfunded capacity. State that as money, at your floor rate from
`domain-finance/corporate-finance-fpa/finance_services_rate_floor_model.md`.

Then check the **effective** notice: if the engagement would naturally end in three
weeks, a 60-day notice clause delivers three weeks. Notice protects only work that
would otherwise have continued.

### 3. Establish the work-in-progress position

On termination, what are you paid for?

- Work performed but not yet invoiced — is it expressly payable?
- Work performed on a milestone not yet reached — is there a pro-rata provision, or
  do you lose the whole milestone?
- Is there an obligation to deliver the partial work product, and is that conditioned
  on payment?

The milestone question is the one that bites. A provider three weeks into a four-week
milestone, with no pro-rata provision, is paid nothing for those three weeks. Primary
ask: payment for work performed to the date of termination, evidenced by records,
with partial deliverables released on payment.

### 4. Recover committed third-party costs

List every cost you cannot cancel: subcontractor commitments, non-refundable
licences, travel, reserved capacity you have guaranteed to someone else. Check
whether the agreement makes these recoverable on termination for convenience. If it
does not, the exposure is yours, and it should shape what you commit to before
signature.

Cross-check with
`domain-finance/corporate-finance-fpa/finance_subcontractor_margin_model.md` — a
guaranteed subcontractor commitment that survives client termination is the sharpest
version of this risk.

### 5. Assess the kill fee

A kill fee compensates for termination for convenience. Common bases:

| Basis | Note |
|---|---|
| Percentage of remaining fee | Simplest; typically tapering with elapsed term |
| Fixed sum | Clean, easy to enforce, must be justifiable |
| Committed costs plus a margin | Most defensible as a genuine pre-estimate |
| Notice-period value | Effectively paid notice |

Two points for counsel. First, a sum that is not a genuine pre-estimate of loss may
be construed as a penalty and unenforceable in some jurisdictions — the
committed-costs-plus-margin basis is generally the most defensible. Second, where no
kill fee is agreed, ordinary damages may still be available; absence of a clause is
not necessarily absence of a remedy, but it converts a contractual entitlement into a
claim.

Where the client resists a kill fee, the fallback that often succeeds is a **longer
notice period**, which achieves much of the same economic effect and reads as less
adversarial.

### 6. Price the transition assistance obligation

This is the most commonly under-priced provision in services agreements. Check:

- What transition assistance is required — documentation, handover sessions,
  knowledge transfer, support to a successor supplier?
- Over what period?
- **At what rate?** If the clause is silent, the default assumption will be that it
  is included.
- Is it required even where the client terminated for convenience, or where the
  provider terminated for non-payment?

An obligation to provide "reasonable transition assistance" for up to ninety days at
no charge is a material unpriced liability, and it lands precisely when the
relationship is worst. Primary ask: transition assistance at standard rates, capped
in days, and conditional on the account being current.

### 7. Total the exposure and rank the asks

Sum the components, then rank the asks by money recovered per unit of negotiating
resistance. In most services agreements the ranking is:

1. Payment for work performed to termination, pro-rated across milestones — high
   value, low resistance
2. Transition assistance at standard rates with a cap — high value, low resistance
3. Recovery of committed third-party costs — moderate value, low resistance
4. Non-payment as provider cause for termination — moderate value, low resistance
5. Longer notice period — moderate value, moderate resistance
6. Kill fee — high value, high resistance

Leading with the kill fee is the common error; items 1 to 4 are usually conceded
without argument and frequently recover more.

---

## Output format

```markdown
# Termination economics — [agreement], provider side
**Engagement value:** [x] · **Term:** [x] · **Counsel review:** required

## Limbs and asymmetry
| Limb | Available? | Notice | Compensation | Asymmetry flag |
|---|---|---|---|---|

## Exposure
| Component | Amount | Basis |
|---|---|---|
| Unfunded capacity (lead time − effective notice) | | |
| Work performed, unpaid | | |
| Milestone in progress, no pro-rata | | |
| Committed third-party costs, unrecoverable | | |
| Unpriced transition assistance ([n] days × [rate]) | | |
| **Total exposure on day-one convenience termination** | | |

## Worst case by phase
| Terminated at | Exposure |
|---|---|
| Month 1 | |
| Mid-term | |
| Final milestone −1 week | |

## Asks, ranked
| # | Ask | Recovers | Expected resistance | Proposed wording |
|---|---|---|---|---|

## Questions for counsel
1. [penalty construction of the proposed kill fee under [governing law]]
2. [whether ordinary damages remain available absent a kill-fee clause]

## Walkaway
[the version of this clause that should not be signed, and why]
```

---

## Verification

- [ ] All four limbs are assessed and asymmetries named explicitly.
- [ ] Effective notice is used, not contractual notice.
- [ ] Exposure is computed at three points in the term, not just at signature.
- [ ] The milestone pro-rata position is checked.
- [ ] Every committed third-party cost is listed and its recoverability stated.
- [ ] Transition assistance is priced in days × rate, even where the clause is silent.
- [ ] Asks are ranked by value against resistance, not by importance to you.
- [ ] Penalty-construction risk is a question for counsel, not a conclusion.

**False-positive prevention.** The dominant failure is negotiating the kill fee and
ignoring transition assistance. The kill fee is visible, adversarial and often
resisted; unpriced transition assistance is invisible, rarely resisted, and in long
engagements frequently the larger number.

The second is computing exposure at signature only. Termination risk is not uniform
across a term: the worst point is typically deep into an unbilled milestone with
committed subcontractor costs in flight. Model at least three points.

The third is treating a mutual-looking clause as mutual. Read each limb separately
and ask what it takes for *you* to invoke it. A provider who cannot terminate for
non-payment has a payment clause with no enforcement behind it.

---

## Related

- `legal_contract_clause_redline_targeted.md` — the termination clause language itself
- `legal_payment_terms_and_late_fee_review.md` — whether non-payment is provider cause
- `legal_negotiation_position_paper.md` — taking these asks into the negotiation
- `../../domain-finance/corporate-finance-fpa/finance_services_rate_floor_model.md` — the rate exposure is valued at
- `../../domain-business-strategy/client-services/services_capacity_and_utilization_planner.md` — bench and replacement lead time
