---
title: "Marital Settlement Agreement Drafter"
category: legal/divorce
description: "Draft a comprehensive marital settlement agreement (MSA / property settlement agreement) resolving a dissolution: recitals and disclosure acknowledgments, property division and debt allocation, separate-property confirmation, spousal support terms (amount, duration, modifiability, termination, tax), retirement division with QDRO hooks, tax provisions, custody/parenting and child-support integration or incorporation, dispute resolution, and enforcement/merger language — sized to the controlling state and ready for incorporation into the judgment."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - settlement-agreement
  - msa
  - property-division
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_post_mediation_term_sheet_and_mou_drafter.md
  - domain-legal/divorce/legal_property_division_and_equalization_proposal.md
  - domain-legal/divorce/legal_spousal_support_alimony_analysis.md
  - domain-legal/divorce/legal_retirement_division_and_qdro_framework.md
  - domain-legal/divorce/legal_divorce_tax_consequences_analysis.md
  - domain-legal/custody/legal_parenting_plan_drafter.md
---

**Purpose:** Draft a complete, signable marital settlement agreement that resolves all economic and (by integration or incorporation) parenting issues, recites the disclosures and consideration that make it enforceable, and is structured for incorporation into the dissolution judgment. Output is a full agreement, not a memo.

**When to use:** Memorializing a settlement reached in mediation or negotiation; converting a term sheet into a definitive agreement; preparing the dispositive document for an uncontested or settled dissolution.

---

## Your Input

- **Jurisdiction:** [State; whether the state requires the MSA to merge into or survive the judgment; local rules]
- **Property regime:** [Community / equitable distribution]
- **Parties & disclosure:** [Names; confirmation that financial disclosures were exchanged]
- **Property division terms:** [Asset/debt allocation and equalization from the division proposal]
- **Separate property:** [Items confirmed separate to each party]
- **Spousal support terms:** [Amount, duration, modifiability, termination triggers, tax treatment, security]
- **Retirement division:** [Plans, percentages, QDRO responsibility]
- **Tax provisions:** [Filing status, dependency allocation, §1041, indemnification]
- **Children:** [Parenting plan and child-support terms to integrate or incorporate by reference]
- **Dispute resolution:** [Mediation/arbitration clause; attorney-fee provision for enforcement]
- **Misc:** [Insurance, name restoration, mutual releases, execution formalities]

---

## Constraints

**Must:**
- Recite **exchange of financial disclosures** and each party's acknowledgment, plus voluntariness and (if applicable) advice of counsel — these support enforceability.
- State whether the agreement **merges into or survives** the judgment per the state's rule (this affects modifiability and enforcement remedies) `[CITE: …]`.
- Allocate **every asset and debt**, confirm **separate property**, and state the **equalization** mechanics with deadlines and security.
- State **spousal support** with amount, duration, **modifiability (modifiable vs. non-modifiable)**, termination triggers, **tax treatment (post-TCJA)**, and security.
- Provide **retirement-division** terms with a QDRO-preparation responsibility and a hold-harmless for plan-acceptance issues.
- Include **tax provisions**: filing status for the transition year, dependency/credit allocation (Form 8332 where needed), §1041 acknowledgment, and indemnification for undisclosed liabilities.
- For children, **incorporate the parenting plan and child-support order**, and recite that child support and custody remain **modifiable and subject to the court's continuing jurisdiction** (parties cannot bargain away the child's right to support or the court's best-interests authority).
- Include **dispute-resolution, default/enforcement, mutual-release, and integration/merger** clauses, and **execution formalities** (signatures, notarization as required).
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for unsupplied authority, terms, or figures.

**Must Not:**
- Purport to make **child support or custody non-modifiable** or to oust the court's continuing jurisdiction over children.
- Invent statutory citations, figures, or terms not supplied.
- Omit the disclosure recital or the merger/survival election.
- Allocate retirement without addressing the QDRO and plan acceptance.
- Apply pre-TCJA alimony tax treatment to a post-2018 agreement.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Recitals & disclosures.** Parties, marriage/separation dates, disclosure exchange, voluntariness, counsel, consideration.
2. **Merger/survival election.** State the treatment per the state's rule.
3. **Property division.** Allocate assets and debts; confirm separate property; set equalization terms (amount, deadline, security).
4. **Spousal support.** Amount, duration, modifiability, termination triggers, tax treatment, security.
5. **Retirement.** Division percentages; QDRO preparation responsibility and cost; hold-harmless.
6. **Tax provisions.** Filing status, dependency/Form 8332, §1041 acknowledgment, indemnification.
7. **Children.** Incorporate parenting plan and child support; recite continuing jurisdiction and modifiability.
8. **Dispute resolution & enforcement.** Mediation/arbitration; default; attorney-fee shifting for enforcement.
9. **General provisions.** Mutual releases, insurance, name restoration, integration, governing law, severability, execution.

---

## Output Format

```markdown
MARITAL SETTLEMENT AGREEMENT

This Agreement is made between {Party A} and {Party B}.

RECITALS
A. The parties were married on {date} and separated on {date}.
B. The parties have exchanged financial disclosures as required by {State} [CITE: …] and each acknowledges receipt and the opportunity to review.
C. Each party enters this Agreement voluntarily, {with the advice of independent counsel / having had the opportunity to consult counsel}.

1. MERGER/SURVIVAL. This Agreement shall {merge into / survive} the Judgment per {State} [CITE: …].

2. PROPERTY DIVISION.
   2.1 To {A}: {assets}. 2.2 To {B}: {assets}. 2.3 Debts: {allocation}. 2.4 Separate property confirmed: {…}. 2.5 Equalization: {Party} pays {$} by {date}, secured by {…}.

3. SPOUSAL SUPPORT. {Amount}/month for {duration}; {modifiable/non-modifiable}; terminates on {death/remarriage/cohabitation/{date}}; tax: {not deductible/includible — post-2018}; security: {…}.

4. RETIREMENT. {Plan} divided {%/$} to {payee} via QDRO prepared by {party} at {cost allocation}; parties hold each other harmless for plan-acceptance issues.

5. TAX. Transition-year filing: {…}; dependency/credits: {…} (Form 8332 where applicable); §1041 nonrecognition acknowledged; indemnification for undisclosed liabilities.

6. CHILDREN. The Parenting Plan ({attached as Exhibit __}) and child support of {$}/month are incorporated. Custody and child support remain subject to the Court's continuing jurisdiction and modification in the children's best interests.

7. DISPUTE RESOLUTION & ENFORCEMENT. {Mediation/arbitration}; the prevailing party in enforcement may recover attorney's fees.

8. GENERAL. Mutual releases; insurance; name restoration to {name}; entire agreement/integration; governing law {State}; severability; execution in counterparts.

{Signatures; notarization/acknowledgment as required}
Exhibits: {Parenting Plan; Asset/Debt Schedule; QDRO instructions}
```

---

## Verification

- [ ] Disclosure exchange, voluntariness, and consideration recited.
- [ ] Merger/survival election stated per the state's rule.
- [ ] Every asset and debt allocated; separate property confirmed; equalization with deadline/security.
- [ ] Spousal support complete (amount, duration, modifiability, termination, tax, security).
- [ ] Retirement division with QDRO responsibility and hold-harmless.
- [ ] Tax provisions (filing, dependency/Form 8332, §1041, indemnification) included.
- [ ] Parenting plan and child support incorporated; continuing jurisdiction and modifiability recited.
- [ ] Dispute-resolution, enforcement, release, integration clauses, and execution formalities present.
- [ ] No attempt to make child support/custody non-modifiable; no invented citations/figures.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Making child support or custody "non-modifiable" | Parties cannot oust the court's continuing jurisdiction over children; recite modifiability |
| Omitting the disclosure recital | Recite the exchange of disclosures; it supports enforceability |
| Skipping the merger vs. survival election | State it; it controls modifiability and enforcement remedies |
| Dividing retirement with no QDRO mechanism | Assign QDRO preparation, cost, and a plan-acceptance hold-harmless |
| Applying old alimony tax treatment to a post-2018 MSA | Recite the post-TCJA treatment |
| Leaving an asset or debt unallocated | Allocate everything; add a catch-all for after-discovered property |
| Equalization with no deadline or security | Set a payment date and security/default remedy |
| Omitting dependency/Form 8332 allocation | Allocate child tax benefits and require the release where needed |
| No enforcement/fee-shifting clause | Add default and prevailing-party fee provisions |
| Inventing statutory citations or figures | Use [CITE]/[NEED] placeholders |
