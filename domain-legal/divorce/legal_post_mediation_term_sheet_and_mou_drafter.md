---
title: "Post-Mediation Term Sheet and MOU Drafter"
category: legal/divorce
description: "Memorialize what was agreed at a divorce or custody mediation before it evaporates: a term sheet or memorandum of understanding with the binding-vs-nonbinding intent stated explicitly under the jurisdiction's rule, every agreed term captured concretely (property, equalization, support, parenting terms), an open-items register, conditions precedent (disclosure confirmation, appraisal true-ups, QDRO review, attorney review), and enforceability traps flagged — bridging to the full MSA and parenting-plan drafting."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - CM-02
  - DS-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - mediation
  - settlement
  - term-sheet
  - mou
  - drafting
updated: "2026-06-10"
related_prompts:
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
  - domain-legal/divorce/legal_divorce_settlement_and_mediation_prep.md
  - domain-legal/divorce/legal_retirement_division_and_qdro_framework.md
  - domain-legal/custody/legal_parenting_plan_drafter.md
  - domain-legal/custody/legal_custody_settlement_and_mediation_prep.md
---

**Purpose:** Capture a mediated agreement in writing at or immediately after the session — as a term sheet or memorandum of understanding — so the deal survives the drive home. The central drafting decision is **binding intent**: in many states a signed mediation MOU is an enforceable contract (and may be incorporated into the decree), while in others it is a non-binding framework until a formal agreement is executed; the document must say which one it is, expressly, under the governing rule `[CITE: …]`. Captures both financial and parenting terms (child-related terms remain subject to best-interests review and are never non-modifiable). Output is a draft for counsel review — the bridge to `legal_marital_settlement_agreement_drafter.md` and `legal_parenting_plan_drafter.md`, not a substitute for them.

**When to use:** Agreement (full or partial) reached at mediation and counsel needs it memorialized before the parties leave or shortly after; a mediator's summary needs conversion into a signed term sheet; a partial agreement should be locked in while open issues continue.

---

## Your Input

- **Jurisdiction:** [State; rule on enforceability of mediated settlement agreements / signed MOUs `[CITE: …]`; any statutory formalities (signatures, recitals, attorney certification) for enforceability]
- **Binding intent:** [Do the parties intend this document to be binding now, or non-binding until a formal MSA is executed?]
- **Mediation context:** [Date, mediator, who attended, full or partial agreement, court deadline or pending trial date]
- **Agreed financial terms:** [Property allocation item-by-item, equalization amount and payment terms, spousal support (amount/duration/modifiability), child support figure and guideline basis, debt allocation, fees]
- **Agreed parenting terms (if any):** [Legal custody, schedule, holidays, transportation, ROFR — or route to parenting-plan drafting]
- **Open items:** [Issues not resolved, issues parked for later, terms agreed "in principle" but not specified]
- **Conditions:** [Anything the deal depends on — disclosure confirmation, appraisal, refinance approval, QDRO pre-approval, attorney review period]
- **Mediation confidentiality:** [Whether the governing rule affects what the term sheet can recite `[CITE: …]`]

---

## Constraints

**Must:**
- State **binding intent expressly and conspicuously**: either "this is a binding agreement enforceable upon signing" or "this is a non-binding summary of terms; no party is bound until a formal agreement is executed" — under the jurisdiction's rule `[CITE: …]`. Silence is the trap.
- Identify the jurisdiction's **enforceability formalities** for mediated agreements (signatures of parties and/or counsel, specific recitals, incorporation language) and satisfy or flag them `[NEED: …]`.
- Capture every agreed term **concretely**: numbers, dates, deadlines, who pays, who signs, what account, what happens on default — "the parties will divide the retirement fairly" is not a term.
- Maintain an **open-items register** distinguishing (a) unresolved issues, (b) agreed-in-principle terms needing specification, and (c) conditions precedent — so partial agreement doesn't masquerade as full agreement.
- State **conditions precedent** expressly (disclosure confirmation, appraisal true-up, lender approval, QDRO pre-approval, attorney review window) and what happens if a condition fails.
- Keep **child-related terms modifiable**: recite that custody and child support remain subject to the court's best-interests and guideline review and cannot be made non-modifiable; flag any guideline deviation for required findings `[NEED GUIDELINE: …]`.
- Note **merger/incorporation posture**: whether the agreement will be incorporated into the decree, merged, or survive as an independent contract — and what the parties intend `[CITE: …]`.
- Flag **enforceability traps** in the deal as struck: terms dependent on third parties (lenders, plan administrators), tax assumptions, missing default remedies, ambiguous deadlines.
- Respect **mediation confidentiality**: the term sheet recites the agreement, not the negotiation `[CITE: …]`.
- Mark every figure or rule not supplied with `[CITE: …]`, `[NEED: …]`, `[NEED GUIDELINE: …]`.

**Must Not:**
- Leave binding intent ambiguous or implied — the most-litigated MOU defect.
- Invent enforceability rules, guideline figures, or statutory formalities for the state.
- Convert "agreed in principle" into specified terms the parties didn't actually reach.
- Draft child support or custody as non-modifiable, or waive child support in trade.
- Recite negotiation history, offers, or who-conceded-what (confidentiality and poison risk).
- Substitute this document for the full MSA or parenting plan — it bridges to them.
- Paper an agreement that depends on unconfirmed disclosure without a disclosure-confirmation condition.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Binding-intent decision.** Confirm with counsel whether the parties intend immediate binding effect; state the jurisdiction's rule on mediated-agreement enforceability `[CITE: …]`; draft the intent clause conspicuously (first substantive paragraph).
2. **Formalities check.** List the state's enforceability formalities (party signatures, counsel signatures, recitals, certification) and build them into the signature block; flag any that cannot be satisfied at the session `[NEED: …]`.
3. **Recitals.** Identify parties, counsel, mediator, mediation date, and the case caption; recite that the terms below were reached at mediation — without reciting the negotiation.
4. **Financial terms.** Draft each agreed term concretely: property allocation (item, recipient, transfer mechanics, deadline), equalization (amount, payment schedule, security, default remedy), spousal support (amount, duration, start date, modifiability, termination events), child support (guideline figure or deviation with findings flag), debts, fees.
5. **Parenting terms.** Capture agreed custody/schedule terms at term-sheet level with the modifiability recital; route full drafting to `legal_parenting_plan_drafter.md`.
6. **Conditions precedent.** Draft each condition with its deadline, who satisfies it, and the consequence of failure (term void, renegotiation, or whole-agreement contingency).
7. **Open-items register.** List unresolved issues and agreed-in-principle items needing specification, each with a process and date for resolution (next session, exchange, motion).
8. **Merger/incorporation clause.** State whether the parties intend incorporation into the decree, merger, or survival as a contract `[CITE: …]`.
9. **Trap scan.** Review the deal for enforceability traps: third-party dependencies, tax-assumption risk, missing default remedies, ambiguous dates, disclosure gaps — flag each with a fix.
10. **Bridge plan.** Close with the drafting path: who prepares the MSA/parenting plan, by when, and what happens if formal drafting stalls (does the term sheet control?).

---

## Output Format

```markdown
# {BINDING MEDIATED SETTLEMENT TERM SHEET / NON-BINDING MEMORANDUM OF UNDERSTANDING}
**Caption:** {court, case no.}   **Mediation date:** {date}   **Mediator:** {name}

## Binding Effect
{EXPRESS CLAUSE: binding upon signing per [CITE: …] / non-binding until formal agreement executed.}
Formalities required: {signatures / recitals / certification} [CITE: …]

## 1. Agreed Financial Terms
| # | Term | Specifics (amount / date / mechanics / default remedy) |
|---|---|---|
| 1 | Property: {item} | to {party}; transfer by {date} via {mechanism} |
| 2 | Equalization | {$} payable {schedule}; secured by {…}; on default {…} |
| 3 | Spousal support | {$}/mo for {duration} from {date}; {modifiable per [CITE]}; terminates on {events} |
| 4 | Child support | {guideline $ / deviation + findings} [NEED GUIDELINE: …]; remains modifiable |
| 5 | Debts / Fees | {allocation} |

## 2. Agreed Parenting Terms (term-sheet level)
- {Legal custody; schedule; holidays; transportation; ROFR} — subject to best-interests review; modifiable. Full plan: parenting-plan draft to follow.

## 3. Conditions Precedent
| Condition | Responsible | Deadline | If not satisfied |
|---|---|---|---|
| {Disclosure confirmation / appraisal / refinance / QDRO pre-approval / attorney review} | {…} | {date} | {term void / renegotiate / agreement contingent} |

## 4. Open Items
| Item | Status (unresolved / in-principle) | Resolution process | Date |
|---|---|---|---|

## 5. Merger / Incorporation
- {Incorporated into decree / merged / survives as contract} [CITE: …]

## 6. Drafting Bridge
- {Counsel} drafts {MSA / parenting plan} by {date}; pending execution, {this term sheet controls / does not bind}.

## Signatures
{Party} ____ {date}   {Party} ____ {date}
{Counsel} ____   {Counsel} ____   {Mediator (if required)} ____
```

---

## Verification

- [ ] Binding vs. non-binding intent stated expressly and conspicuously, tied to the jurisdiction's rule `[CITE: …]`.
- [ ] State enforceability formalities identified and satisfied or flagged.
- [ ] Every agreed term specified concretely — amounts, dates, mechanics, default remedies — no "fairly/reasonably" terms.
- [ ] Child support and custody recited as modifiable; deviations flagged for findings.
- [ ] Conditions precedent drafted with deadlines, owners, and failure consequences.
- [ ] Open-items register separates unresolved from agreed-in-principle; nothing unagreed drafted as agreed.
- [ ] Merger/incorporation posture stated.
- [ ] No negotiation history recited; mediation confidentiality respected.
- [ ] Enforceability traps scanned and flagged with fixes.
- [ ] No invented rules, guideline figures, or formalities — placeholders used.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Silence on binding intent | The express clause is the document's reason to exist; state it first |
| Assuming a signed MOU is non-binding everywhere (or binding everywhere) | State the jurisdiction's rule [CITE]; many states enforce signed mediated agreements as contracts |
| "The parties will divide the 401(k) equitably" | Specify: plan, percentage or amount, valuation date, QDRO responsibility, deadline |
| Drafting terms the parties only discussed | Open-items register; agreed-in-principle ≠ agreed |
| Making child support non-modifiable as part of the trade | Recite modifiability; guideline review survives party agreement |
| Omitting what happens when a condition fails | Each condition gets a consequence: term void, renegotiate, or contingent agreement |
| Reciting who conceded what during the session | Confidentiality; recite terms, not negotiation |
| Treating the term sheet as the final MSA | Bridge clause: who drafts the formal agreement, by when, and what controls meanwhile |
| Equalization payment with no security or default remedy | Add schedule, security, and default consequence |
| Ignoring merger vs. survival | State incorporation/merger intent — it controls future enforcement and modification paths |
| QDRO terms drafted without plan-administrator reality | Condition on QDRO pre-approval; cross-reference the QDRO framework prompt |
| Papering over unconfirmed disclosure | Disclosure-confirmation condition; concealment voids mediated agreements |
