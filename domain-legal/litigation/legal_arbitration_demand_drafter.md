---
title: "Arbitration Demand Drafter — AAA / JAMS Demand with Claim Recitation and Relief"
category: legal/litigation
description: "Attorney-facing drafter for a demand for arbitration before an administering institution such as AAA or JAMS — clause-driven pre-filing checks (conditions precedent, delegation, carve-outs, rule set and fee regime), a demand that tracks the institution's filing requirements, a claim-by-claim statement, and a relief section — distinct from a court complaint and from a pre-suit demand letter."
techniques:
  - IPC-07
  - ST-03
  - CM-02
  - QA-01
  - QA-12
difficulty: intermediate
tags:
  - legal
  - litigation
  - arbitration
  - arbitration-demand
  - aaa-jams
  - contract-says-arbitration
  - start-arbitration-claim
updated: "2026-09-24"
related_prompts:
  - domain-legal/litigation/legal_complaint_drafter.md
  - domain-legal/client-intake-communications/legal_demand_letter_drafter.md
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
---

# Arbitration Demand Drafter — AAA / JAMS Demand with Claim Recitation and Relief

> **Scope guard — attorney-facing only.** This prompt is for counsel initiating an arbitration on a client's behalf. It does not advise an individual consumer or employee whether to arbitrate or how to file on their own. If the person running it is unrepresented, stop and route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

> **No-fabrication rule.** Quote the arbitration clause only from the text supplied. Do not state institutional rule numbers, filing fees, fee-shifting protocols, limitation periods, or emergency-relief procedures from memory — mark them `[VERIFY: current {institution} {rule set} rule / fee schedule]`. Do not invent case names or statutory cites; use `[CITE: …]` / `[NEED PIN: …]`.

## When to Use

- A contract dispute (commercial, employment, consumer, construction) is subject to an arbitration clause and the client is ready to initiate.
- Counsel wants a pre-filing check of the clause before choosing between arbitration and a court filing.
- A multi-step dispute clause (negotiation → mediation → arbitration) needs its earlier steps confirmed before the demand is served.

**Not this prompt if:**
- The dispute belongs in court — use `domain-legal/litigation/legal_complaint_drafter.md`.
- You are sending a pre-proceeding demand letter to prompt settlement — use `domain-legal/client-intake-communications/legal_demand_letter_drafter.md`.
- You are negotiating or redlining the arbitration clause itself — use `domain-legal/contracts-transactional/legal_contract_review_full_redline.md`.

## Inputs

- **Jurisdiction (required):** Governing law of the contract; seat or place of arbitration; whether federal arbitration law, state arbitration law, or both govern `[VERIFY]`; any international convention if parties are in different countries.
- **Arbitration clause (verbatim):** Plus any incorporated rules reference, delegation language, carve-outs, class or collective waivers, confidentiality, arbitrator-number and qualification terms, and fee-allocation terms.
- **Institution and rule set:** Named institution and rule set (commercial, consumer, employment, construction, streamlined/expedited, international) — or "clause is silent."
- **Parties:** Claimant and respondent legal names, addresses, counsel; any non-signatories you want to bind.
- **Facts and chronology:** Key events with dates and documents.
- **Claims and relief:** Causes of action; amount claimed (sum certain or range) with basis; non-monetary relief; interest, fees, and costs basis (contract or statute).
- **Conditions precedent:** Notice, negotiation, or mediation steps taken, with dates.
- **Urgency:** Whether interim or emergency relief is needed.

## Method

1. **Clause parse.** Break the clause into: scope ("arising out of" vs. "relating to"), delegation of arbitrability, carve-outs (injunctive relief, small claims, IP), institution and rules, seat, arbitrator number and qualifications, class/collective waiver, fee allocation, confidentiality, and pre-arbitration steps. Quote each component.
2. **Arbitrability check.** For each claim, is it within scope? If arbitrability is disputed, does the clause delegate it to the arbitrator? Flag non-signatory issues.
3. **Conditions precedent.** Confirm each required pre-arbitration step was completed and documented; if not, the demand may be premature. Flag contractual notice periods.
4. **Rule set and fee regime.** Identify which institutional rules apply (the clause may specify a version, or rules in effect at filing may govern `[VERIFY]`), whether consumer or employment protocols shift fees to the business `[VERIFY]`, and the filing fee band for the amount claimed `[VERIFY: current fee schedule]`.
5. **Timing.** Contractual limitation periods and statutory limitations `[VERIFY]`; whether filing the demand stops the clock under the governing law `[VERIFY]`. State the latest safe filing date only as `[VERIFY]`.
6. **Pleading strategy.** Decide how detailed the statement of claims should be: institutional rules typically require only a brief statement of the nature of the dispute, but a fuller statement can frame the case for the arbitrator. Recommend a level and explain the trade-off (early persuasion vs. locking in theories and previewing evidence).
7. **Draft the demand.** Caption per institution; parties and counsel; the arbitration agreement (quote clause, attach contract); nature of the dispute; claims, each with elements and supporting facts; relief (amount with calculation basis, interest, fees and costs with their contractual or statutory basis, non-monetary relief); requested hearing locale; arbitrator number and qualifications per the clause; any request for interim or emergency relief under the applicable rules `[VERIFY]`.
8. **Filing packet.** Institution filing form, contract copy, fee, proof of service on respondent in the manner the rules require `[VERIFY]`, and any required notice to a consumer or employee.

## Output Format

```markdown
# Arbitration Demand Package — {Claimant} v. {Respondent}
**Institution / rules:** {…} [VERIFY version]  |  **Seat:** {…}  |  **Latest safe filing date:** [VERIFY]  |  **Attorney Work Product (sections 1–3)**

## 1. Clause Parse
| Component | Clause text (quoted) | Effect |
## 2. Pre-Filing Checks
| Check | Status | Action needed |
(arbitrability · delegation · carve-outs · conditions precedent · limitations · fee regime · class waiver)
## 3. Pleading-Detail Recommendation
## 4. Demand for Arbitration (draft)
- Caption
- Parties and Counsel
- Arbitration Agreement
- Nature of the Dispute
- Statement of Claims (Claim 1 … n: elements → facts)
- Relief Requested (amount + basis; interest; fees/costs basis; other relief)
- Hearing Locale / Arbitrator Number and Qualifications
- Interim or Emergency Relief (if any)
- Signature block
## 5. Filing Packet Checklist
## 6. Verification Items
```

## Verification

- [ ] Jurisdiction lock: governing law, seat, and governing arbitration statute stated or `[VERIFY]`.
- [ ] Citation discipline: every rule, fee, and statute is supplied or `[VERIFY]` / `[CITE]`; the clause is quoted exactly.
- [ ] Scope discipline: each claim checked against clause scope and carve-outs; excluded claims flagged, not pleaded.
- [ ] Every condition precedent confirmed with a date or flagged as unmet.
- [ ] Relief amounts show a calculation basis; fee and cost claims name their contractual or statutory basis.
- [ ] Arbitrator number and qualifications match the clause.
- [ ] No filing deadline stated as settled.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Filing before completing a mediation or negotiation step | Check the clause's conditions precedent; premature demands invite a stay or dismissal |
| Assuming the institution's commercial rules apply | Consumer, employment, and construction rule sets and fee protocols differ — identify which governs |
| Pleading a carved-out claim (e.g., injunctive relief reserved for court) | Parse carve-outs and route those claims correctly |
| Copying a court complaint into the demand | Follow the institution's filing requirements; choose the detail level deliberately |
| Stating fee amounts or deadlines from memory | Mark `[VERIFY: current schedule / rule]` |
| Ignoring non-signatories | Flag whether each respondent is bound and on what theory `[CITE]` |

## Example

**Input (abridged):** Fictional Redstone Fabrication (claimant) v. Ashgrove Builders (respondent). Subcontract clause: "Any dispute arising out of this Subcontract shall first be submitted to mediation; if unresolved within 60 days, it shall be resolved by arbitration administered by the AAA under its Construction Industry Rules. Claims for injunctive relief may be brought in court." Mediation ended without settlement 70 days after it began. Claim: $312,000 unpaid on approved change orders plus contractual interest.

**Output (excerpt):**

> **Clause parse — conditions precedent.** Mediation requirement satisfied: submitted, and more than the 60-day window elapsed without resolution `[NEED: mediation termination letter]`.
>
> **Rule set.** Construction rules named expressly; confirm which version applies and whether the claim amount falls in a fast-track or large, complex case band `[VERIFY: current AAA Construction Rules and fee schedule]`.
>
> **Claim 1 — breach of subcontract (unpaid change orders).** Elements under the governing law `[VERIFY]`: contract; performance; approved change orders CO-7 through CO-11 totalling $312,000; non-payment after invoice. Relief: $312,000 plus interest at the contractual rate from each invoice due date `[NEED PIN: subcontract interest clause]`.
>
> **Carve-out.** No injunctive relief sought, so nothing to route to court.
