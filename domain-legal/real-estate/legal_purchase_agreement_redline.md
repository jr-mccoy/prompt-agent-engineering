---
title: "Purchase and Sale Agreement Redline — Buyer or Seller Posture with Risk-Tiered Comments"
category: legal/real-estate
description: "Redline a commercial or investment real estate purchase and sale agreement (PSA) from a declared buyer or seller posture: deposit and its hard/soft status, due-diligence period and termination right, title and survey objection mechanics, seller deliveries, representations and their survival and cap, conditions to closing, casualty and condemnation, prorations, default remedies, 1031 cooperation and assignment — each comment tiered Critical / Material / Clean-up with a primary ask, fallback and walkaway. Attorney work product; distinct from the buyer's non-legal offer strategy in domain-specialized-fields and from general commercial-contract redlines."
techniques:
  - ST-02
  - CM-02
  - DS-06
  - OC-03
  - QA-01
difficulty: advanced
tags:
  - legal
  - real-estate
  - purchase-agreement
  - psa
  - redline
  - due-diligence
  - title
  - closing
  - buying-commercial-property
updated: "2026-09-24"
reasoning:
  styles: [analytic, adversarial, systematic]
  stakes: high
  horizon: weeks
  uncertainty: risk
  evidence_quality: rich
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, redline]
  user_role: [attorney, paralegal, in_house_counsel]
  mode: [audit, draft, negotiate]
related_prompts:
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
  - domain-legal/contracts-transactional/legal_negotiation_position_paper.md
  - domain-legal/real-estate/legal_title_commitment_review.md
  - domain-specialized-fields/real-estate/realestate_buyer_offer_strategy.md
---

## Objective

Produce a posture-calibrated redline of a real estate purchase and sale agreement
(PSA) in which every comment is tied to a clause, tiered by risk, and carries a
three-rung position ladder (primary / fallback / walkaway), plus a short issues memo
the supervising attorney can send to the client.

## When to Use

- A commercial, industrial, retail, multifamily, land or investment-property PSA has
  arrived (or you are drafting the first turn) and you represent one side.
- A letter of intent has been signed and you need to check the PSA honours it.
- Re-trading after diligence findings: you need to see which clauses give leverage.

**Distinct from:**
- `domain-specialized-fields/real-estate/realestate_buyer_offer_strategy.md` — the
  buyer's and agent's *pricing and contingency packaging* before an offer; it
  expressly leaves drafting the agreement to an attorney. This prompt is that attorney.
- `domain-legal/contracts-transactional/legal_contract_review_full_redline.md` — a
  general commercial-contract redline; it has no model of deposits, title/survey
  objections, prorations, casualty, or recording-driven closing mechanics.
- `domain-legal/real-estate/legal_title_commitment_review.md` — the title objection
  letter itself; this prompt drafts the PSA *mechanics* that the objection runs on.
- Residential form contracts promulgated by a state real estate commission or board
  are usually not negotiated clause-by-clause; use this prompt only for addenda and
  riders in that setting.

## Your Input

- **Jurisdiction (required):** state/province where the property sits, and the PSA's
  governing-law clause if different.
- **Posture (required):** Buyer / Seller. If you cannot say, stop — a neutral redline
  is not a redline.
- **Property type and deal size:** e.g. single-tenant NNN retail, $8.2M.
- **The PSA** (full text) and the **LOI / term sheet**, if any.
- **Client priorities:** certainty of close, speed, price protection, financing
  dependence, 1031 exchange, tenant-occupied vs. vacant.
- **Known facts:** leases in place, environmental history, lender involved, any
  existing title commitment or survey.
- **House positions:** firm or client playbook, if any.

## Constraints

**Must:**
- Tie every comment to a clause number and quote the operative text.
- Tier each comment: **Critical** (walk-away or economic exposure), **Material**
  (shifts risk meaningfully), **Clean-up** (drafting, definitions, cross-references).
- Give a primary ask, a fallback and a walkaway for every Critical and Material
  comment, with proposed replacement language.
- Check the PSA against the LOI and flag every departure, in either direction.
- Trace deposit status through every termination path: who gets the deposit, when it
  goes hard, and what notice formalities control.
- Mark every jurisdiction-specific rule you rely on (transfer-tax allocation custom,
  attorney-review periods, statutory disclosure duties, bulk-sale or withholding
  obligations, recording formalities) as `[VERIFY: …]` unless the user supplied it.

**Must Not:**
- Invent statutes, case names, recording or transfer-tax rules, or local customs. Use
  `[CITE: …]` and `[VERIFY: …]` placeholders.
- Assume a residential-consumer statute applies to a commercial deal, or vice versa.
- Redline economic terms (price, deposit amount) the client has already agreed unless
  the PSA departs from the agreement.
- Add generic "consult counsel" language; the user is counsel.

## Method

1. **Lock posture and priorities.** Restate side, property type, and the client's top
   three priorities. Every tiering decision refers back to them.
2. **LOI conformity pass.** Table each LOI term against the PSA clause that implements
   it; flag missing, changed or added terms.
3. **Deposit and termination map.** For each termination right (diligence, title,
   financing, casualty, condemnation, default, failure of condition) record the
   deadline, the notice requirement, and who receives the deposit. Flag any path where
   the deposit outcome is ambiguous.
4. **Due-diligence period.** Length, start trigger (effective date vs. delivery of
   seller materials), extension rights, access and insurance requirements, restoration
   and indemnity for entry, and whether silence means termination or approval.
5. **Title and survey mechanics.** Objection deadline, seller's cure election and
   deadline, mandatory-cure items (monetary liens, seller-created encumbrances),
   new-matter objections after the gap/bring-down, and the permitted-exceptions
   definition.
6. **Seller deliveries and estoppels.** List of documents, delivery deadline, tenant
   estoppel and SNDA thresholds and forms, and consequence of late delivery.
7. **Representations.** Scope, knowledge qualifier and whose knowledge, survival
   period, liability cap and floor, and whether a buyer's pre-closing knowledge of a
   breach waives the claim.
8. **Conditions to closing.** Bring-down of reps, title policy issuance, estoppels,
   financing (if any), and the remedy when a condition fails without default.
9. **Casualty and condemnation.** Materiality threshold, termination right, insurance
   proceeds and deductible assignment.
10. **Closing mechanics and prorations.** Closing date and extensions, deliveries,
    closing costs and transfer-tax allocation `[VERIFY: local custom]`, prorations
    (rents, CAM reconciliation, taxes, utilities, security deposits) and post-closing
    true-up.
11. **Default and remedies.** Buyer default (deposit as liquidated damages — flag
    enforceability as `[VERIFY]`), seller default (specific performance, cost
    reimbursement cap, lis pendens timing).
12. **Boilerplate that matters here.** Assignment (to affiliates, to a 1031
    intermediary), 1031 cooperation, confidentiality, brokers, notices, time of
    essence, and any jury-waiver or venue clause.
13. **Tier, ladder and draft.** Write the comments; then write the client memo that
    leads with Critical items only.

## Output Format

```markdown
# PSA Redline Memo — [Property], [Buyer/Seller] side
**Jurisdiction:** [state] · **Governing law:** [state] · **Draft reviewed:** [seller's draft dated …]
**Privileged & Confidential — Attorney Work Product**

## Client summary (Critical items only, ≤ 1 page)
1. …

## LOI conformity
| LOI term | PSA clause | Conforms? | Note |
|---|---|---|---|

## Deposit and termination map
| Termination right | Deadline / trigger | Notice form | Deposit goes to | Ambiguity? |
|---|---|---|---|---|

## Clause comments
### §[x.x] — [topic] — [Critical / Material / Clean-up]
**As drafted:** > [quote]
**Issue:** [effect on client]
**Primary:** [replacement language]
**Fallback:** [variant]
**Walkaway:** [what cannot be signed]

## Open verification items
| # | Item | Why it matters | Owner |
|---|---|---|---|
| 1 | [VERIFY: transfer-tax allocation custom in county] | | |
```

## Worked Example

**Input (abridged):** Buyer posture; single-tenant NNN retail, $8.2M; buyer is
completing a 1031 exchange and needs certainty of close; seller's first draft.

**Selected output:**

| Termination right | Deadline / trigger | Notice form | Deposit goes to | Ambiguity? |
|---|---|---|---|---|
| Due diligence | 30 days after Effective Date | Written, per §14 | Buyer | **Yes** — §4.2 says silence = approval; §4.4 says buyer "may" terminate by notice. Silence outcome inconsistent |
| Title objection | 10 days after receipt of commitment *and* survey | Written | Buyer if seller elects not to cure | No |
| Seller default | — | — | Buyer, plus costs capped at $25,000 | No |

> **§4.2 — Due-diligence silence — Critical.** *As drafted:* "Buyer's failure to
> deliver a Termination Notice shall be deemed approval." *Issue:* combined with §3.1
> (deposit goes hard on expiry) and the 30-day period starting at the Effective Date
> rather than delivery of seller materials, the buyer can lose the diligence window
> to late seller deliveries. *Primary:* period runs from the later of the Effective
> Date and the date seller delivers every item on Exhibit D; deemed approval retained
> (buyer's certainty-of-close priority favours a clear rule). *Fallback:* one 15-day
> extension if Exhibit D items arrive after day 10. *Walkaway:* any period that can
> expire before Exhibit D items are delivered.

> **§11.1 — Transfer tax — Material.** Draft allocates 100% to buyer.
> `[VERIFY: customary allocation of state and local transfer tax in the county]` —
> if custom is seller-pays, this is an unannounced economic change from the LOI,
> which is silent.

**Client summary line:** "Two Critical items: the diligence clock can run out before
the seller hands over the documents, and the seller-default remedy caps your recovery
at $25,000 while your 1031 timeline makes a failed closing far more costly than that."

## Verification

- [ ] Jurisdiction and posture are stated at the top and every tier reflects them.
- [ ] Every LOI term is matched to a PSA clause or flagged as missing.
- [ ] The deposit outcome is stated for every termination path; ambiguities flagged.
- [ ] Every Critical and Material comment has primary, fallback and walkaway language.
- [ ] Title/survey objection, cure and new-matter mechanics are checked end to end.
- [ ] Rep survival, cap and knowledge qualifier are addressed together, not singly.
- [ ] Every jurisdiction-specific rule is supplied by the user or marked `[VERIFY]`;
      no statute, case or local custom is asserted from memory.
- [ ] The client summary contains only Critical items.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Neutral "balanced" comments that help neither side | Re-derive each comment from the declared posture and the client's top priorities |
| Reviewing diligence length without its start trigger | A 30-day period from the Effective Date with a 20-day delivery deadline is a 10-day period; always state the trigger |
| Treating the deposit as one question | Trace it through every termination path; the dangerous gaps are where two clauses give different answers |
| Tiering by clause type instead of consequence | A boilerplate notices clause is Critical if a termination right depends on it and it requires overnight courier to an outdated address |
| Asserting transfer-tax, disclosure or withholding rules as settled | These are jurisdiction- and deal-specific; mark `[VERIFY]` or `[CITE]` |
| Assuming liquidated-damages language is enforceable because it says so | Enforceability depends on local law; flag for verification rather than rely on it |
| Redlining agreed economics as if open | Only flag price/deposit/closing-date terms where the PSA departs from the LOI |
| Importing residential consumer protections into a commercial deal | Confirm the property and parties are within any statute before relying on it |

## Related

- `domain-legal/real-estate/legal_title_commitment_review.md` — the title objection that §5 of the method feeds
- `domain-legal/real-estate/legal_commercial_lease_abstract.md` — abstracting in-place leases for rent-roll and estoppel checks
- `domain-legal/contracts-transactional/legal_negotiation_position_paper.md` — turning the ladders into a negotiation plan
- `domain-legal/corporate-ma/legal_due_diligence_request_list.md` — the seller-deliveries list when the deal is an entity purchase
- `domain-specialized-fields/real-estate/realestate_buyer_offer_strategy.md` — the non-legal offer packaging that precedes the PSA
