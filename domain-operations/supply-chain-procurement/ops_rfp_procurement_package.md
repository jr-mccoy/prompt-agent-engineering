---
title: "Buyer-Side RFP Procurement Package — Requirements, an Evaluation Rubric Frozen Before Bids, a Fair Q&A Process, and Scoring"
category: operations/supply-chain-procurement
description: "Assemble the buyer's RFP package for goods or services: must-have vs. weighted requirements, a structured price form that makes bids comparable, pass/fail gates, an evaluation rubric and price formula fixed and dated before any bid is opened, a single-channel Q&A process with answers published to all bidders, independent scoring before consensus, and the award record."
techniques:
  - CM-03
  - DP-03
  - OC-03
  - QA-02
difficulty: intermediate
tags:
  - rfp
  - procurement
  - sourcing-event
  - evaluation-rubric
  - bid-scoring
  - buyer-side
  - getting-quotes
  - compare-bids-fairly
  - hire-a-vendor
updated: "2026-09-24"
related_prompts:
  - domain-operations/supply-chain-procurement/ops_supplier_selection_scorecard.md
  - domain-finance/treasury-capital-markets/finance_bank_relationship_rfp_framework.md
  - domain-professional-writing/business-writing/business_writing_proposal.md
---

# Buyer-Side RFP Procurement Package

**Objective:** Produce an RFP package a buyer can issue — requirements, price form,
timeline, Q&A rules, and an evaluation rubric locked before bids arrive — plus the
scoring and award record that shows the decision followed the published rules.

**When to Use:**
- You are buying a service or goods contract large enough that several suppliers
  should compete, and the choice will be questioned later.
- Past bids were impossible to compare because each supplier priced differently.
- A losing bidder, auditor, or board member may ask how the winner was chosen.
- **Not this prompt if** you are the **seller** responding to an RFP — use
  `domain-professional-writing/business-writing/business_writing_proposal.md`. For a
  banking-services RFP, use
  `domain-finance/treasury-capital-markets/finance_bank_relationship_rfp_framework.md`.
  To score already-received offers against sourcing strategy and TCO, use
  `ops_supplier_selection_scorecard.md`; to negotiate after selection, use
  `domain-negotiation/contexts/negotiation_vendor_procurement_buyside.md`. Public-sector
  and grant-funded procurement is governed by statute and policy — use this as a
  working draft and have your procurement officer or counsel confirm the rules.

## Inputs / Context

1. **What you are buying**: scope, locations, volumes, service levels, contract term.
2. **Who decides**: evaluation panel, approver, and anyone with a conflict of interest.
3. **Budget or price expectation**, if any (usually not disclosed to bidders).
4. **Mandatory conditions**: insurance, licences, certifications, security, legal terms.
5. **Candidate suppliers** or the market you will invite.
6. **Timeline constraints**: current contract end, notice periods, transition time.

## Method

1. **Scope and requirements (CM-03).** Separate **mandatory** (pass/fail) from
   **evaluated** (scored) requirements. Each requirement is testable from what a
   bidder submits. Put volumes and service levels in the RFP so every bid prices the
   same work.
2. **Structured price form.** One template every bidder must use: fixed fees by
   line, unit rates for variable work, assumed volumes, escalation, and what is
   excluded. Free-form pricing makes comparison impossible and invites disputes.
3. **Evaluation rubric, frozen before bids (DP-03).** Criteria and weights summing
   to 100; anchored descriptors for each score band; the price-scoring formula (e.g.
   `lowest price ÷ bidder price × price weight`); the pass/fail gates. Date and sign
   it, and store it before the submission deadline. Publishing the criteria and
   weights in the RFP is good practice and often required.
4. **Q&A process.** One named contact; questions in writing by a deadline; answers
   anonymized and **published to all bidders**; no side conversations with bidders
   during the event. A site visit, if any, is offered to all on the same terms.
5. **Timeline.** Issue, questions due, answers published, submissions due, evaluation,
   clarifications or presentations, award, notice to unsuccessful bidders, contract
   start with transition window.
6. **Evaluation (OC-03).** Check gates first. Each evaluator scores independently
   with written rationale; then a consensus session records final scores and any
   changes with reasons. Price is scored by formula, separately from the quality panel
   where practical.
7. **Stress-test the rubric before issue (QA-02).** Score two imaginary bids — a
   cheap, thin one and an expensive, excellent one. If the rubric picks a winner you
   would not accept, fix the weights now, not after bids arrive.
8. **Award record.** Scores, rationale, conflicts declared, approvals, and the
   debrief offered to unsuccessful bidders.

## Output Format

```
# RFP package — [what is being bought]    Ref: [..]   Contact: [single role]

## 1. Scope and requirements
| # | Requirement | Mandatory / Evaluated | How the bidder evidences it |
## 2. Price form
| Line | Unit | Assumed volume | Rate | Annual total |
## 3. Pass/fail gates
## 4. Evaluation rubric (frozen [date], signed [roles])
| Criterion | Weight | 1–2 | 3 | 4–5 |
Price formula: [..]
## 5. Q&A rules
## 6. Timeline
| Milestone | Date |
## 7. Scoring summary
| Bidder | Gates | Criterion scores | Price score | Total | Rank |
## 8. Award record
```

## Verification

- [ ] Every requirement is either mandatory or evaluated, never both.
- [ ] One price form; bids that deviate are handled per a stated rule.
- [ ] Rubric weights sum to 100 and are dated before the submission deadline.
- [ ] Price formula is written down and applied arithmetically.
- [ ] Q&A answers go to all bidders; one contact is named.
- [ ] Evaluators score independently before consensus; conflicts declared.
- [ ] Totals add up from the criterion scores.

## False-Positive Prevention

1. **Rubric written after bids.** Any change to criteria or weights after opening
   bids looks — and often is — steering toward a preferred bidder.
2. **Requirements copied from the incumbent's proposal.** They lock in one supplier's
   approach and exclude better alternatives. Describe the outcome, not their method.
3. **Uncomparable pricing.** Without a common form and volumes, the "lowest" bid is
   whichever priced least of the scope.
4. **Private answers.** Answering one bidder's question by phone gives them an
   advantage and invalidates the process.
5. **Group-think scoring.** Scoring together from the start lets the loudest
   evaluator set every score. Independent first, consensus second.
6. **Price weight so high that quality is decorative.** Test with the thin-cheap bid.
7. **Treating this as legal advice.** Regulated or public procurement rules vary by
   jurisdiction and funding source; confirm them with the responsible officer.

## Example Output

```
# RFP package — Janitorial services, 3 office sites (120,000 sq ft)   Contact: Facilities buyer

## 1. Scope and requirements
| 1 | Nightly cleaning per spec A, 5 nights/wk              | Evaluated | method statement |
| 2 | Day porter, Site 1, 8 h/day                           | Evaluated | staffing plan    |
| 3 | General liability insurance ≥ stated limit            | Mandatory | certificate      |
| 4 | Two references for comparable sites                   | Mandatory | contacts         |
## 2. Price form
Monthly fixed fee per site; day-porter hourly rate × 2,080 h/yr; supplies included;
escalation cap per year stated. Annualized totals compared.
## 3. Pass/fail gates
Insurance certificate, references, signed price form. All three bidders passed.
## 4. Evaluation rubric (frozen 24 Sep, signed Facilities + Finance)
| Technical approach 30 | Staffing & supervision 20 | Quality program 15 | Price 30 | Transition 5 |
Price formula: lowest annual price ÷ bidder price × 30.
Stress test: thin bid at −20% price scored 71; excellent bid at +15% scored 86 → weights kept.
## 5. Q&A rules
Questions by 10 Oct via email to contact; anonymized answers to all bidders 15 Oct;
one site walk for all bidders 8 Oct.
## 6. Timeline
Issue 1 Oct | Questions 10 Oct | Answers 15 Oct | Bids due 29 Oct | Evaluation 1–12 Nov |
Award 15 Nov | Transition 1–31 Dec | Start 1 Jan
## 7. Scoring summary   (annual price: X $312k, Y $286k, Z $341k)
| X | pass | 24 / 16 / 12 / 4 | 27.5 | 83.5 | 2 |
| Y | pass | 18 / 12 / 9 / 3  | 30.0 | 72.0 | 3 |
| Z | pass | 27 / 18 / 13 / 5 | 25.2 | 88.2 | 1 |
## 8. Award record
Award to Z. Independent scores varied ≤3 points per criterion; consensus changes
recorded (Y quality 10 → 9: no supervisor inspection frequency stated). One evaluator
declared a prior employment link to X and did not score X. Debriefs offered to X and Y.
```

## Techniques Used

- **CM-03 Scope Definition** — mandatory vs. evaluated requirements and fixed volumes.
- **DP-03 Anchored Scoring Scales** — rubric bands and price formula fixed before bids.
- **OC-03 Markdown Table Specification** — price form and scoring summary as comparable tables.
- **QA-02 Adversarial Stress-Test** — thin-cheap vs. excellent-expensive dry run of the rubric.

## Related Prompts

- `ops_supplier_selection_scorecard.md` — TCO and supply-risk view of the shortlisted bids.
- `domain-finance/treasury-capital-markets/finance_bank_relationship_rfp_framework.md` — banking RFPs.
- `domain-professional-writing/business-writing/business_writing_proposal.md` — the seller's side.
- `domain-negotiation/contexts/negotiation_vendor_procurement_buyside.md` — negotiating after award.
