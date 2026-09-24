---
title: "Section 363 Sale Strategy Memo"
category: legal/bankruptcy-restructuring
description: "Strategy memo for a sale of estate assets outside a plan under Bankruptcy Code §363 — sale-versus-plan choice, stalking-horse terms and bid protections, bidding procedures, free-and-clear analysis lien by lien, credit-bid issues, good-faith purchaser protection, contract assumption and assignment, and the sale order terms each constituency will fight over — with every rule reference and deadline marked for verification."
techniques:
  - ST-01
  - RT-02
  - CM-02
  - QA-02
difficulty: advanced
tags:
  - legal
  - bankruptcy
  - section-363
  - distressed-ma
  - stalking-horse
  - bidding-procedures
  - free-and-clear
updated: "2026-09-24"
reasoning:
  styles: [strategic, adversarial, structural]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: regulated
  collaboration: small_team
  output_format: [memo, structured]
  user_role: [lawyer]
  mode: [plan, decide]
related_prompts:
  - domain-legal/bankruptcy-restructuring/legal_chapter_11_plan_analysis.md
  - domain-legal/corporate-ma/legal_due_diligence_findings_memo.md
  - domain-finance/mergers-acquisitions/finance_deal_financing_structure_analysis.md
  - domain-finance/valuation/finance_precedent_transactions_analysis.md
---

# Section 363 Sale Strategy Memo

**Objective:** Advise the client (debtor, stalking-horse bidder, secured lender, or committee) on how a §363 sale should be run and where it will be contested: whether a sale outside a plan is justified, what stalking-horse protections the court is likely to approve, how bidding procedures should be structured, whether each lien and interest can be stripped under the free-and-clear standard, how credit bidding interacts with the auction, what the purchaser needs in the sale order, and which contracts must be assumed and assigned with what cure. The memo ends with a sale timeline and an objection map.

**When to use:**
- Planning a going-concern sale early in a case (or pre-filing, as a prepackaged sale path).
- Representing a prospective stalking-horse bidder negotiating an asset purchase agreement and bid protections.
- Committee or lender counsel deciding whether to object to procedures or to the sale.

**Distinct from:**
- `domain-legal/corporate-ma/legal_due_diligence_findings_memo.md` — ordinary M&A diligence; §363 sales add court approval, free-and-clear, and auction mechanics.
- `domain-finance/valuation/finance_precedent_transactions_analysis.md` — values the business; this memo uses value to test the process and the lien waterfall.
- `legal_chapter_11_plan_analysis.md` (this folder) — confirmation of a plan; flag here if the sale dictates plan terms (sub rosa plan risk).

**Audience:** Restructuring and distressed-M&A counsel.

---

## Your Input

- **Client and role:** [Debtor / stalking horse / secured lender / committee / other bidder]
- **Case:** [Debtor, district, circuit, chapter, petition date, DIP financing terms and milestones]
- **Assets:** [Substantially all / a division / specific assets; IP, real property, contracts, licences, permits]
- **Liens and interests:** [Each lien holder, amount, priority, perfection status, disputes; non-lien interests such as successor-liability claims, rights of first refusal]
- **Valuation and marketing:** [Pre-petition marketing process, banker, indications of interest, value range]
- **Proposed stalking-horse APA terms:** [Price, form of consideration, credit-bid component, break-up fee, expense reimbursement, overbid minimum, deadlines]
- **Contracts and leases:** [Key contracts, anti-assignment clauses, cure amounts claimed, counterparty consent issues]
- **Milestones and liquidity:** [DIP milestones, cash runway, why speed matters]
- **Local rules / complex-case procedures:** [Paste any local guidelines on sale motions and bid protections]
- **Controlling authority supplied:** [Circuit cases on business justification, bid protections, credit bidding, free-and-clear, sub rosa plans]

---

## Constraints

### Must
- Articulate the **business justification** for selling outside a plan and the evidence that will prove it (melting ice cube, marketing history, lack of alternatives).
- Analyze **bid protections** against the standard the controlling circuit applies (e.g., business judgment vs. benefit to the estate) `[NEED HOLDING: circuit standard]`; express the break-up fee and expense reimbursement as a percentage of purchase price and flag if outside customary ranges *as supplied by the user or local guidelines* — do not assert a market range from memory.
- Test **free-and-clear** lien by lien against the statutory alternatives (consent, non-bankruptcy law permits, price exceeds liens, bona fide dispute, compellable to accept money) `[VERIFY: §363(f)(1)–(5)]`, and separately address non-lien "interests" such as successor liability.
- Address **credit bidding**: the secured creditor's right, any cause to limit it, and disputes over lien validity that affect the credit-bid amount `[VERIFY: §363(k)]`.
- Address **good-faith purchaser** findings and their effect on appellate review `[VERIFY: §363(m)]`, including insider or collusion issues `[VERIFY: §363(n)]`.
- Plan **assumption and assignment**: cure amounts, adequate assurance of future performance, anti-assignment provisions, and non-assignable licences.
- Flag **sub rosa plan** risk where the sale allocates proceeds, releases claims, or dictates plan terms.
- Provide a **timeline** with every notice and objection period marked `[VERIFY: Rules 2002, 6004, 6006 and local rules]`.

### Must Not
- Invent market percentages for break-up fees, overbid increments, or notice periods.
- Treat "free and clear" as automatic for every interest; each lien and interest needs a prong.
- Assume consent from silence without checking the controlling rule on deemed consent.
- Ignore consumer-privacy, antitrust, or regulatory approvals the sale may trigger — flag them.
- Cite cases not supplied; use `[CITE: …]` / `[NEED HOLDING: …]`.

---

## Instructions

1. **Frame the client's objective** and leverage (a stalking horse wants certainty and protections; a lender wants to credit bid or get paid; a committee wants value maximization and preserved causes of action).
2. **Sale vs. plan.** State the business justification and the evidence; score sub rosa plan exposure.
3. **Stalking-horse terms.** Break-up fee and expense reimbursement (as % of price), overbid minimum, matching rights, termination triggers; predict objections.
4. **Bidding procedures.** Qualified-bidder criteria, deposit, deadlines, auction format, credit-bid treatment, backup bidder, consultation parties.
5. **Free-and-clear table.** One row per lien or interest: holder, amount, prong relied on, risk.
6. **Credit bidding.** Amount, disputes, cause to cap, effect on chilling bidding.
7. **Contracts.** Assumption / assignment list with cure and adequate-assurance plan.
8. **Sale order terms.** Findings needed (good faith, adequate notice, free and clear, no successor liability, waiver of the stay of the order); which will be contested.
9. **Timeline** from procedures motion to closing, with verification flags.
10. **Objection map** by constituency and the recommended response.

---

## Output Format

```markdown
# §363 Sale Strategy Memo — In re {Debtor}
**Client role:** {…}  |  **District / circuit:** {…}  |  **Privileged & Confidential**

## 1. Executive Recommendation
## 2. Sale Outside a Plan — Justification and Sub Rosa Risk
## 3. Stalking-Horse Terms
| Term | Proposed | % of price | Objection risk | Recommended position |
## 4. Bidding Procedures
## 5. Free-and-Clear Analysis
| Lien / interest | Holder | Amount | §363(f) prong [VERIFY] | Risk |
## 6. Credit Bidding
## 7. Contracts and Leases
| Contract | Counterparty | Cure claimed | Anti-assignment issue | Adequate assurance plan |
## 8. Sale Order — Findings and Contested Terms
## 9. Timeline
| Step | Target date | Notice / objection period [VERIFY] |
## 10. Objection Map
| Constituency | Objection | Strength | Response |
## 11. Verification Items
```

---

## Worked Example

**Input (abridged):** Client: prospective stalking horse for a regional software company in Chapter 11. Proposed price $18M cash; break-up fee $720K; expense reimbursement cap $300K. First-lien lender claims $22M and has signalled it may credit bid. Second-lien holder claims $4M; committee alleges its lien is unperfected. DIP milestone requires sale order within 75 days. Key customer contracts contain anti-assignment clauses.

**Output (excerpt):**

> **3. Stalking-horse terms.** Break-up fee = 4.0% of price; with expense reimbursement, total protections up to 5.7%. Whether this is approvable depends on the circuit standard and any local guidelines — the user has not supplied either `[NEED HOLDING: circuit standard] [VERIFY: local complex-case guidelines]`. Recommend negotiating a fee paid only on a topping bid, not on a credit bid by the first lien, because the lender will object that protections chill its credit bid.
>
> **5. Free-and-clear.** First lien ($22M): price ($18M) does not exceed the lien, so the "price exceeds all liens" prong is unavailable; free-and-clear will rest on consent — make lender consent (or its credit-bid election) a closing condition. Second lien ($4M): committee's perfection challenge supports the "bona fide dispute" prong; proceeds attach to escrow pending resolution.
>
> **6. Credit bid.** First lien can bid up to the allowed amount of its claim; if the committee's challenge period is still open, the credit bid should be subject to that challenge — expect the committee to seek a cap for cause.
>
> **Objection map (excerpt):** Customer counterparties — anti-assignment clauses are generally unenforceable against assignment under the Code, but licences of certain IP may require consent under non-bankruptcy law `[NEED HOLDING: circuit test for non-assignable licences]`; budget for consent negotiations within the 75-day milestone.

---

## Verification

- [ ] Jurisdiction lock: circuit authority used or placeholders inserted; no out-of-circuit standard presented as controlling.
- [ ] Business justification and sub rosa exposure analyzed.
- [ ] Bid protections expressed as % of price; no market range asserted from memory.
- [ ] Every lien and interest mapped to a free-and-clear prong.
- [ ] Credit-bid amount and disputes addressed.
- [ ] Contracts listed with cure and adequate assurance.
- [ ] Sale order findings identified; timeline periods marked `[VERIFY]`.
- [ ] Citation discipline: no invented cases, holdings, or rule text.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Asserting a "market" break-up fee percentage | Compute the client's percentage; compare only to user-supplied or local-guideline ranges |
| Relying on the "price exceeds liens" prong when price is below the senior lien | Check arithmetic per lien; use consent, dispute, or another prong |
| Treating successor-liability claims as liens | Analyze non-lien interests separately and the sale order language needed |
| Ignoring the credit bid's effect on the auction | Model whether the lender's credit bid dominates cash bids and whether protections apply to it |
| Missing sub rosa plan terms (releases, proceeds allocation) | Flag any term that dictates plan outcomes |
| Assuming anti-assignment clauses are always overridden | Some licences need consent under non-bankruptcy law |
| Timeline built on assumed notice periods | Mark every period `[VERIFY]` against rules and local procedures |
