---
title: "Engagement Letter Drafter"
category: legal/client-intake-communications
description: "Draft a client engagement letter (representation agreement) with scope, fee provisions, conflicts disclosure and waiver where applicable, communication norms, termination provisions, file-retention period, and dispute-resolution clauses — calibrated to the controlling state-bar rules (MRPC 1.5, 1.7, 1.8, 1.16) and the practice-area fee structure."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - client-intake
  - engagement-letter
  - representation-agreement
  - fee-agreement
  - scope
updated: "2026-05-11"
related_prompts:
  - domain-legal/client-intake-communications/legal_new_matter_intake_summary.md
  - domain-legal/client-intake-communications/legal_client_status_update_memo.md
  - domain-legal/litigation/legal_complaint_drafter.md
  - domain-legal/in-house-legalops/legal_matter_summary_for_executive.md
---

**Purpose:** Draft a client-facing engagement letter that defines the representation, satisfies the state's MRPC-derived fee-agreement and conflict-disclosure requirements, and is ready for client signature. Output is a deliverable, not a memo.

**When to use:** After intake and conflicts clearance; when expanding scope of an existing engagement; when re-papering an engagement after a material change in fee structure or scope.

---

## Your Input

- **Jurisdiction:** [State governing the lawyer-client relationship — state-bar rules vary, e.g., flat-fee trust handling, contingency caps, advance-fee labels]
- **Practice area:** [Litigation / transactional / regulatory / family / criminal / etc.]
- **Posture:** [Pre-dispute / suit filed / appeal / transactional / advisory]
- **Firm / lawyer:** [Firm name, primary attorney, bar number; any supervising attorney]
- **Client:** [Name, business form; decision-maker(s) with authority to bind]
- **Scope:** [Specific tasks included; carve-outs (e.g., excludes appeal, excludes counterclaims, excludes related agency proceeding)]
- **Fee structure chosen:** [Hourly / flat / contingency / hybrid / statutory — with rates, percentages, increments]
- **Advance / retainer:** [Amount, replenishment trigger, trust vs. operating treatment per state rule]
- **Expenses:** [Pass-through expenses; markup policy; threshold requiring approval]
- **Conflicts to disclose / waivers needed:** [Concurrent client conflict, former client conflict, business-transaction conflict — if any]
- **Communication norms:** [Frequency, channels, response-time expectations, designated client contact]
- **Termination:** [Conditions for client and lawyer termination]
- **File-retention period:** [Per state rule, often 5–7+ years; method of return / destruction]
- **Dispute resolution:** [Fee arbitration availability per state bar; mediation / arbitration of fee/malpractice disputes — note state-specific limits on pre-dispute malpractice arbitration clauses]
- **Electronic signature:** [E-sign permitted in jurisdiction; platform]

---

## Constraints

**Must:**
- State the **jurisdiction's** governing rules-of-professional-conduct framework (e.g., "the {State} Rules of Professional Conduct").
- Define **scope** with specificity and explicit carve-outs (what is NOT included).
- State fees and expenses in a form that satisfies **MRPC 1.5** reasonableness factors and the state's writing requirements (contingencies require a signed writing per MRPC 1.5(c); some states require written fee agreements above a dollar threshold or for all matters).
- For contingency: state the percentage, the base (gross vs. net of expenses), the order of deductions, expense responsibility on no-recovery, and any state-imposed cap or schedule.
- For flat fee: state what the flat fee covers, what triggers earning, and trust-handling per the state's rule (some states require flat fees be held in trust until earned).
- For hourly: state rates by timekeeper, billing increment, billing cycle, advance retainer treatment (trust vs. operating), replenishment trigger.
- Identify **client decision-maker** with binding authority (entity client: officer; minor: guardian; co-clients: each signer).
- Address **conflicts disclosure and informed-consent waiver** where any concurrent, former-client, or business-transaction conflict exists (MRPC 1.7 / 1.9 / 1.8).
- Address **termination** rights for both client and lawyer, and the lawyer's obligations on termination under MRPC 1.16 (reasonable notice, file return, refund of unearned fees).
- Address **file retention** with the period (jurisdiction-specific) and post-termination delivery / destruction policy.
- Address **fee-dispute resolution**, including availability of state-bar fee arbitration where applicable.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for any state-specific citation or fact not supplied.

**Must Not:**
- Invent party names, rates, percentages, retainer amounts, dates, or state rule citations.
- Include a **pre-dispute malpractice arbitration / liability-limiting clause** without verifying the state's specific rule (many states require independent-counsel advice or prohibit such clauses outright).
- Use a contingency structure in a **prohibited matter** (criminal defense; most domestic-relations matters per MRPC 1.5(d)).
- Label as "non-refundable" any fee that the state's rule treats as refundable on early termination — describe earning triggers instead.
- Use vague scope language ("such other services as may be required") in lieu of specific scope.
- Insert generic "consult counsel" disclaimers — the letter IS the engagement.

---

## Instructions

1. **Heading.** Firm letterhead placeholder; date; client name and address.
2. **Re line.** Matter short title.
3. **Opening.** Thank client; identify the lawyer / firm as counsel; identify the governing professional-conduct rules.
4. **Identification of client.** Who the client is (and who is NOT — e.g., when representing an entity, state that the firm represents the entity and not its constituents).
5. **Scope of representation.** Bulleted included tasks; bulleted carve-outs / excluded matters; conditions for expanding scope (written amendment).
6. **Fees.** Subsection matching the chosen structure (hourly / flat / contingency / hybrid / statutory), drafted to satisfy MRPC 1.5 and state-specific requirements.
7. **Expenses.** Pass-through categories; approval threshold; markup (or none).
8. **Retainer / advance fee.** Amount; trust vs. operating treatment per state rule; replenishment trigger; application to final invoice.
9. **Conflicts disclosure & informed-consent waiver.** Only if a conflict exists; describe the conflict in plain English, identify the affected interests, and request informed written consent.
10. **Client decision-maker & communication.** Designated contact; channels; response-time expectations; how the firm handles changes in decision-maker.
11. **Client cooperation.** Document production, truthful information, timely responses, no destruction of relevant materials.
12. **Termination.** Client's right to terminate at any time; lawyer's right to withdraw consistent with MRPC 1.16; consequences for fees earned and trust funds.
13. **File retention.** Period; post-termination return on request; destruction policy after period expires.
14. **Fee-dispute resolution.** Fee arbitration availability under the state-bar program; informal resolution first; preserve client's rights.
15. **No-guarantee statement.** Counsel cannot and does not guarantee outcomes.
16. **Severability, modification, entire-agreement.** Standard clauses.
17. **Signature block.** Lawyer, client (with decision-maker authority confirmed), electronic-signature compliance per state.

---

## Output Format

```markdown
[FIRM LETTERHEAD]
{Date}

{Client Name}
{Address}

Re: Engagement of {Firm Name} as Counsel — {Matter Short Title}

Dear {Client}:

Thank you for engaging {Firm} to represent you in the matter described below. This letter sets out the terms of our engagement. Our representation is governed by the {State} Rules of Professional Conduct.

1. CLIENT
   Our client is {Name and business form}. {If entity: We represent {Entity} and not its officers, directors, members, shareholders, or affiliates individually.} Decisions on behalf of the client will be made by {Decision-Maker(s) — name, role}.

2. SCOPE OF REPRESENTATION
   We will provide the following services:
   - {Included task}
   - {Included task}
   The following are NOT included and will require a separate written engagement:
   - {Carve-out}
   - {Carve-out}
   Scope changes must be confirmed in a written amendment.

3. FEES
   [Hourly]
   Our fees are based on time at the following rates: {Timekeeper — $rate/hr}. Time is billed in {increment} increments. Invoices issue {monthly} and are due {N} days from receipt.
   [Flat]
   The flat fee for the services in Section 2 is ${amount}. The fee is earned as follows: {trigger}. Per {State} rule [CITE: …], the fee will be {held in trust until earned / treated as earned on receipt}.
   [Contingency]
   The contingency fee is {N}% of the {gross / net} recovery. Expenses are {paid from recovery before / after fee calculation}. If there is no recovery, the client owes {no fees / expenses only / nothing}. This contingency complies with {State} contingency-fee requirements [CITE: …]. A copy of the closing statement will be provided per MRPC 1.5(c).
   [Hybrid / Statutory] {…}

4. EXPENSES
   Out-of-pocket expenses (filing fees, court reporters, experts, e-discovery hosting, travel) are passed through {at cost / with a {N}% administrative charge}. Expenses over ${threshold} require advance client approval.

5. ADVANCE FEE / RETAINER
   Client will deposit ${amount} as an advance. Per {State} rule [CITE: …], these funds will be held in {our IOLTA trust account / operating account} and applied to {monthly invoices / final invoice}. When the trust balance falls below ${threshold}, client will replenish to ${target} within {N} days.

6. CONFLICTS DISCLOSURE & WAIVER  [Include only if applicable]
   We disclose the following potential conflict: {plain-English description}. The interests potentially affected are: {…}. After considering this disclosure, client may consult independent counsel and, if client wishes to proceed, sign below to confirm informed consent under MRPC {1.7 / 1.9 / 1.8}.

7. COMMUNICATIONS
   Primary contact at {Firm}: {name}. Primary contact at client: {name}. We will respond to client communications within {N business days}. Material developments and decisions requiring client input will be communicated promptly.

8. CLIENT COOPERATION
   Client agrees to provide truthful and complete information, produce documents on request, preserve potentially relevant materials, and respond timely to communications and decision requests.

9. TERMINATION
   Client may terminate this engagement at any time by written notice. {Firm} may withdraw consistent with MRPC 1.16 (e.g., for non-payment, client refusal to follow advice, or other permitted grounds), upon reasonable notice. Upon termination, fees earned through the date of termination are due; any unearned funds in trust will be returned promptly.

10. FILE RETENTION
    After conclusion of the matter, {Firm} will retain the client file for {N} years per {State} rule [CITE: …]. Client may request the file at any time. After the retention period, the file may be destroyed without further notice.

11. FEE-DISPUTE RESOLUTION
    Any fee dispute will first be addressed by good-faith discussion. If unresolved, client may submit the dispute to the {State Bar} fee-arbitration program where available [CITE: …]. This provision does not limit any other right or remedy.

12. NO GUARANTEE
    {Firm} cannot and does not guarantee any particular outcome.

13. ENTIRE AGREEMENT
    This letter is the entire agreement on these terms and supersedes prior discussions. It may be modified only in writing signed by both parties.

Please sign and return this letter to confirm the engagement. We are pleased to be of service.

Sincerely,

{Attorney Name}                              ACKNOWLEDGED AND AGREED:
{Bar No.}, {Firm}
                                             _______________________________
                                             {Client / Decision-Maker}, {Title}
                                             Date: ____________
[Electronic signature per {State e-sign authority [CITE: …]} permitted.]
```

---

## Verification

- [ ] Jurisdiction's professional-conduct rules identified.
- [ ] Client identified — including entity-vs-individual distinction where applicable.
- [ ] Scope stated with specific included tasks AND specific carve-outs.
- [ ] Fee section matches chosen structure and satisfies MRPC 1.5 / state writing requirements.
- [ ] Contingency, if used, is in a permitted matter and includes percentage, base, expense treatment, and writing signed by client per MRPC 1.5(c).
- [ ] Flat-fee handling complies with the state's earning / trust rule.
- [ ] Advance / retainer treatment (trust vs. operating) is correct per state rule.
- [ ] Conflicts waiver included only when a conflict exists and is described in plain English.
- [ ] Termination addresses both client right and lawyer withdrawal under MRPC 1.16.
- [ ] File-retention period and post-termination return / destruction stated.
- [ ] Fee-dispute / fee-arbitration provision present and consistent with state bar program.
- [ ] No pre-dispute malpractice limitation absent verified state-rule compliance.
- [ ] No invented rates, percentages, retainer amounts, or citations.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Vague scope ("and such other services as may arise") | Replace with specific included tasks and explicit carve-outs; require written amendment to expand |
| Labeling a flat fee "non-refundable" in a state that requires it be held in trust until earned | Use earning triggers; describe trust handling per state rule [CITE: …] |
| Contingency clause that does not state the base (gross vs. net) and order of expense deduction | Specify both; clients have prevailed on ambiguity grounds |
| Contingency in a prohibited matter (criminal, most domestic relations) | MRPC 1.5(d) — re-evaluate fee structure |
| Pre-dispute malpractice arbitration clause inserted by default | Many states require independent-counsel advice or prohibit; remove unless verified |
| Conflict "waiver" with no description of the actual conflict | MRPC 1.7 requires informed consent — describe the conflict, the affected interests, and recommend independent counsel |
| Representing an entity but treating individuals as the client | State entity-only representation explicitly; an "upjohn-style" clarification may be needed |
| Termination clause silent on unearned funds | State that unearned trust funds will be returned promptly |
| File-retention period left blank or pulled from another state | Use the controlling state's rule [CITE: …]; 5–7+ years is common but varies |
| Advance fee deposited in operating instead of trust where state requires trust | Trust account is the default for unearned funds in most states |
| Missing client decision-maker identification on entity engagements | Identify the officer with binding authority and confirm by signature |
| Including a fee arbitration clause that strips client of access to the state-bar program | Programs are typically client-elective; do not waive client's option |
