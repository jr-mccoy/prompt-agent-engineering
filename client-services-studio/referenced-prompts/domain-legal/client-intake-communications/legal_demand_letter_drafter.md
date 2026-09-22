---
title: "Pre-Litigation Demand Letter Drafter"
category: legal/client-intake-communications
description: "Draft a pre-litigation demand letter with numbered factual recitation, legal-claim summary tied to elements, specific cure requested (monetary calculation or behavioral change), reasonable deadline, leverage facts, preservation-of-rights / non-waiver language, and tone calibrated to the recipient — sized to the controlling jurisdiction and statutory notice prerequisites (e.g., UCC §2-607, FDCPA, state lemon law, pre-suit notice statutes)."
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
  - client-communication
  - demand-letter
  - pre-litigation
  - settlement
  - notice
updated: "2026-05-11"
related_prompts:
  - domain-legal/client-intake-communications/legal_new_matter_intake_summary.md
  - domain-legal/client-intake-communications/legal_engagement_letter_drafter.md
  - domain-legal/litigation/legal_complaint_drafter.md
  - domain-legal/in-house-legalops/legal_matter_summary_for_executive.md
---

**Purpose:** Draft a pre-litigation demand that (a) creates a record of notice for any later litigation, (b) satisfies any statutory notice prerequisite, (c) gives the recipient a concrete cure path, and (d) preserves the sender's rights and leverage. Output is a sendable letter, not a memo.

**When to use:** Pre-suit demand on contract / consumer / employment / property / IP claims; statutory notice (UCC §2-607 breach-of-warranty notice, FDCPA validation, state lemon-law notice, state pre-suit notice statutes for construction defect / professional negligence / open meetings / tort claims against public entities); pre-complaint settlement overture; cease-and-desist.

---

## Your Input

- **Jurisdiction:** [State whose substantive law governs; forum likely if suit follows; lawyer's bar admission for that state]
- **Practice area:** [Contract / tort / consumer / employment / IP / property / construction / etc.]
- **Posture:** [Pre-suit / post-breach with cure period running / responding to recipient's prior position / final pre-filing demand]
- **Sender:** [Client (and counsel name, firm, bar number)]
- **Recipient:** [Name, business form, role in the dispute, counsel if represented (note no-contact rule MRPC 4.2 if represented)]
- **Factual chronology:** [Dated events, communications, transactions, witnesses, supporting documents]
- **Operative contract / statute / duty:** [Quoted contract language; statutory citation; common-law duty]
- **Elements of the claim:** [Each element of the asserted claim under the governing law]
- **Cure requested:** [Monetary amount with itemized calculation; behavioral change; contract performance; combination]
- **Deadline:** [Date or "within {N} days of receipt"; statutory deadline if applicable]
- **Statutory notice prerequisite triggered:** [E.g., UCC §2-607 reasonable-time notice; FDCPA validation; state lemon law written notice; state pre-suit notice statute]
- **Leverage facts:** [Regulatory exposure; insurance involvement; fee-shifting statute; public-record / reputation exposure; treble-damages or attorney-fees provision]
- **Tone calibration:** [Cooperative / firm / adversarial — based on recipient audience]
- **Settlement-discussion framing:** [Whether to invoke FRE 408 / state equivalent; pre-litigation communications may or may not be covered]

---

## Constraints

**Must:**
- Identify the **governing jurisdiction** and the substantive law on which the claim rests.
- Confirm whether the recipient is **represented by counsel**; if yes, under MRPC 4.2 the letter must be addressed to counsel, not the represented person directly.
- Recite facts in **numbered paragraphs**, date-stamped, with each material fact tied to a document or witness where available.
- State the **legal claim** with the elements satisfied by the recited facts. Case citations are not required unless persuasive value warrants; statutory citations should be included where the claim is statutory.
- State the **cure requested** with specificity: a monetary amount with itemized calculation (principal, interest, statutory damages, fees, costs); a behavioral change with specific acts; or a contract-performance demand with specific contractual obligations.
- State a **deadline** that is reasonable for the claim type, or the statutory deadline if one applies (e.g., UCC §2-607 "reasonable time"; FDCPA 30-day validation; state lemon-law-specific notice periods; state pre-suit notice waiting periods).
- Include **leverage facts** that are accurate and supportable — fee-shifting statute citation, regulatory exposure, treble damages, attorney-fee provisions.
- Include **preservation-of-rights / non-waiver** language: no waiver of any claim, right, or remedy; reservation of all rights at law and in equity.
- For statutory-notice letters, explicitly invoke the statute and quote / paraphrase the required content.
- Calibrate **tone** to the recipient — cooperative where ongoing relationship matters, firm where litigation is likely.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for any statute, rule, deadline, or fact not supplied.

**Must Not:**
- Invent contract terms, statutory citations, case citations, dollar amounts, dates, witness names, or recipient counsel.
- Threaten criminal prosecution to gain advantage in a civil matter (MRPC 4.4 / state-specific extortion rules); do not threaten bar complaints, disciplinary proceedings, or administrative complaints as leverage where state rule prohibits.
- Contact a represented person directly when counsel is known (MRPC 4.2).
- Use language that asserts a falsehood or misleads recipient (MRPC 4.1).
- Demand amounts not supported by the supplied facts.
- Assume FRE 408 / state-equivalent settlement-privilege protection automatically; the letter may be discoverable for purposes other than to prove liability, and pre-litigation status may affect coverage.
- Insert generic "consult counsel" disclaimers — this is the demand.

---

## Instructions

1. **Letterhead, date, transmission method.** Method matters for proof of notice (certified mail return-receipt, email with confirmation, hand-delivery, statutory required method).
2. **Recipient block.** Address to recipient or recipient's counsel if represented. If statutory notice requires a specific officer / agent for service / registered agent, address accordingly.
3. **Re line.** Matter short title; reference any prior correspondence.
4. **Representation statement.** Sender represents Client in connection with the matter.
5. **Statutory notice header (if applicable).** Caption the letter as the statutory notice ("Notice Pursuant to {Statute}") and quote the statute's required content.
6. **Factual recitation.** Numbered paragraphs. One material fact per paragraph. Dates, parties, document references. Quote contract language where relied on. Where helpful, attach copies of key documents as exhibits.
7. **Legal claim.** Identify the claim (e.g., breach of contract, breach of express warranty under UCC §2-313, FDCPA §1692e, state UDAP violation). Walk through the elements and tie facts to each.
8. **Cure requested.** Itemized:
   - **Monetary:** principal; interest (statutory or contractual rate); statutory multipliers if available; attorney's fees if recoverable; costs. Show the math.
   - **Behavioral:** specific actions with deadlines and verification (cease, retract, return, repair, replace, deliver, disgorge).
   - **Contract performance:** identify the unperformed obligation and the conforming performance.
9. **Deadline.** Specific date or "within {N} days of the date of this letter / receipt." For statutory notices, the statutory period; for contract cures, the contract's cure period if one applies; otherwise, reasonable to the claim type.
10. **Leverage.** Accurate statements of consequences: fee-shifting under {statute [CITE: …]}; treble damages under {statute [CITE: …]}; insurance-notice obligations; regulatory reporting; public-record consequences. Avoid threats of criminal/disciplinary action absent rule-compliant basis.
11. **Preservation of rights.** Non-waiver; all rights reserved; continued accrual of damages and interest; this letter does not constitute an election of remedies.
12. **Settlement framing (optional).** If invoking FRE 408 / state equivalent, label the letter or a designated section as a settlement communication; recognize that protection is rule-dependent and not automatic.
13. **Closing and signature.** Counsel's name, bar number, firm, contact; client copy line.

---

## Output Format

```markdown
[FIRM LETTERHEAD]
{Date}

VIA {Certified Mail RRR No. ____ / Email / Hand Delivery / [statutorily required method]}

{Recipient Name or Counsel}
{Address}

Re: {Matter Short Title} — {Demand for {Cure} / Notice Pursuant to {Statute}}

Dear {Recipient or Counsel}:

This firm represents {Client} in connection with the above-referenced matter. {If statutory notice: This letter constitutes notice pursuant to {Statute [CITE: …]}, which requires {summary of statutory content}.}

FACTS

1. {Date — event with document/witness anchor}
2. {Date — event}
3. {Date — operative contract / communication; quote relied-upon language}
4. {Date — breach / harmful conduct}
5. {Date — harm and damages incurred}
{continue numbered, chronological}

LEGAL CLAIM

{Client}'s claim against {Recipient} is for {claim, e.g., breach of contract / breach of express warranty under UCC §2-313 / violation of {statute [CITE: …]}}. The elements are satisfied as follows:
- {Element 1} — established by {paragraphs N–N above}.
- {Element 2} — established by {paragraphs N–N above}.
- {Element 3} — established by {paragraphs N–N above}.

DEMAND

{Client} demands the following cure:
A. Payment in the amount of ${total}, itemized as follows:
   - Principal: ${…}
   - Pre-demand interest at {rate} from {date} to {date}: ${…}
   - Statutory damages under {statute [CITE: …]}: ${…}
   - Attorney's fees recoverable under {fee-shifting basis [CITE: …]}: ${…} [if applicable]
   - Costs: ${…}
B. {Behavioral action — specific act, deadline, verification method}.
C. {Contract performance — identify obligation and conforming performance}.

DEADLINE

{Client} requires the above cure to be effected by {specific date / within {N} days of receipt}. {If statutory: This is the statutory period under {statute [CITE: …]}.} {If contractual: This is the contract's cure period at Section {…}.}

LEVERAGE / CONSEQUENCES OF NON-COMPLIANCE

Should {Recipient} fail to cure within the time stated, {Client} will pursue available remedies, which may include:
- Filing suit in {forum}, seeking the damages set out above plus accruing interest;
- Recovery of attorney's fees and costs under {fee-shifting authority [CITE: …]};
- {Treble / statutory multiplier} damages under {statute [CITE: …]};
- {Regulatory complaint with {agency}} / {insurance-claim notice} / {other accurate consequence}.

PRESERVATION OF RIGHTS

Nothing in this letter is or shall be construed as a waiver of any claim, right, or remedy of {Client}, all of which are expressly reserved. {Client}'s damages continue to accrue. This letter is not an election of remedies.

{Optional: This letter is a confidential communication made in furtherance of settlement discussions, subject to Federal Rule of Evidence 408 / {state equivalent [CITE: …]}, and is not admissible to prove liability for or invalidity of the claim.}

We are available to discuss resolution. Please direct all communications regarding this matter to the undersigned.

Sincerely,

{Attorney Name}
{Bar No.}, {Firm}
{Address, phone, email}

cc: {Client}
Enclosures: {Exhibit A — {document}; Exhibit B — {document}}
```

---

## Verification

- [ ] Jurisdiction's substantive law identified; statutory citations used where the claim is statutory.
- [ ] Recipient correctly addressed — to counsel if recipient is represented (MRPC 4.2).
- [ ] Factual recitation in numbered paragraphs with dates and document/witness anchors.
- [ ] Legal claim walks through elements and ties to recited facts.
- [ ] Cure requested is specific: monetary amount with itemized calculation, behavioral acts, or identified contract performance.
- [ ] Deadline is statutory where statute applies, contractual where contract applies, otherwise reasonable for claim type.
- [ ] Leverage statements are accurate and supportable; no threats of criminal/disciplinary action to gain advantage.
- [ ] Preservation-of-rights / non-waiver language present.
- [ ] Statutory-notice content quoted or paraphrased where the letter serves as statutory notice.
- [ ] Transmission method appropriate to create a record (and statutorily compliant where required).
- [ ] No invented contract terms, citations, dollar amounts, dates.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Demanding a round number without itemization | Show the math: principal, interest (with rate and dates), statutory damages, fees, costs |
| Conclusory legal claim ("you breached the contract") | Identify the operative contract term, the breaching conduct, and the elements of the claim with fact citations |
| Threatening criminal prosecution / bar complaint as leverage | Remove — many states' rules prohibit such threats to gain civil advantage |
| Writing directly to a represented person | MRPC 4.2 — address counsel; if uncertain whether represented, inquire |
| Treating the letter as automatically FRE 408 / state-privileged | Settlement-rule protection is rule-dependent; pre-litigation framing affects analysis; do not assume |
| Statutory-notice letter that fails to quote / paraphrase the statute's required content | Many statutes require specific content (UCC §2-607 "reasonable time" notice, FDCPA validation rights, state pre-suit statutes); identify and include |
| Deadline shorter than statute or contract allows | Match the statutory or contractual cure period or it is unenforceable as notice |
| Citing fee-shifting where none exists | American rule is default; identify the specific statute or contract clause |
| Demanding treble or punitive damages without statutory basis | Identify the specific multiplier statute and confirm the claim qualifies |
| No transmission method that creates proof of receipt | Use certified mail RRR, email with read-receipt, or statutorily required method |
| Naming the wrong recipient officer / registered agent for service-style statutory notice | Identify the correct service agent per state corporate records |
| Including settlement-only privilege framing while also using the letter to threaten | Tone calibration matters; pick a posture |
