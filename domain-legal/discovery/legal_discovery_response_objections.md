---
title: "Discovery Responses and Objections (RFPs, Interrogatories, RFAs)"
category: legal/discovery
description: "Draft formal responses and objections to RFPs, interrogatories, and RFAs that comply with the specificity-of-objection requirement and preserve all available grounds without using boilerplate."
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
  - discovery
  - objections
  - rule-34
  - rule-33
  - rule-36
updated: "2026-05-08"
related_prompts:
  - domain-legal/discovery/legal_document_request_drafter.md
  - domain-legal/discovery/legal_interrogatory_drafter.md
  - domain-legal/discovery/legal_meet_and_confer_letter.md
  - domain-professional-writing/domain-specific/domain_writing_attorney_discovery.md
---

**Purpose:** Produce defensible discovery responses — RFPs, interrogatories, and RFAs — that comply with Rule 34/33/36 specificity-of-objection requirements, preserve grounds, signal what is being withheld, and avoid the boilerplate-objection traps that get sustained against the responder.

**When to use:** Responding to served discovery; supplementing prior responses; preparing for meet-and-confer or motion-to-compel briefing.

---

## Your Input

- **Court / venue and rule set:** [Federal / state]
- **Discovery to which we are responding:** [RFPs / Interrogatories / RFAs — paste each request and its number]
- **Client (responder):** [Plaintiff / defendant]
- **Position on each request:** [Objection grounds, partial response, full response, withholding, RFA admit/deny/qualify/lack-of-knowledge]
- **Privilege concerns:** [Attorney-client, work product, common-interest, state-specific privileges]
- **ESI / proportionality issues:** [Burden, accessibility, source]
- **Confidentiality / protective order status:** [In place / pending]
- **Documents being produced:** [Bates ranges by request, if known]
- **What we want preserved or signaled:** [E.g., reservation of rights to supplement, objection to definitions, scope dispute]

---

## Constraints

**Must:**
- For each request, provide a specific, individualized response.
- For each objection, state the **specific ground** with enough detail to permit assessment (Rule 34(b)(2)(B)–(C) and analogs require specificity; Rule 34(b)(2)(C) requires stating whether responsive material is being **withheld** on the basis of an objection).
- For RFP responses, state whether responsive documents are being produced, when, and in what format; identify any documents withheld on privilege with a privilege-log commitment.
- For interrogatory responses, comply with Rule 33(b)(3): answer separately and fully, in writing, under oath; verification at the end.
- For RFA responses, comply with Rule 36(a)(4): admit, deny, or state in detail why the responder cannot truthfully admit or deny; a denial must fairly respond to the substance.
- Object to **definitions and instructions** at the front, where they are objectionable, rather than re-objecting in every response.
- Include a **General Objections** section that is short and **narrowly preserved** — most general objections, repeated across every response, get treated as boilerplate and waived.
- Use **claw-back / inadvertent disclosure** language consistent with the protective order or Rule 502(d) order.

**Must Not:**
- Use boilerplate "objected to as overly broad, unduly burdensome, vague, ambiguous, calls for speculation" stacks. Most courts treat these as waived absent specificity.
- State an objection and then refuse to indicate whether anything is being withheld. Rule 34(b)(2)(C) requires the responder to state whether anything is withheld.
- Use a "subject to and without waiving the foregoing objections" preface and then produce documents — courts increasingly treat this as a sub silentio admission that the objection is performative.
- Deny an RFA evasively. A non-responsive denial can be sanctioned and used to shift fees under Rule 37(c)(2).
- Claim privilege without committing to a privilege log under Rule 26(b)(5).
- Refuse to answer an interrogatory by directing to "documents already produced" without specifying Bates ranges sufficient under Rule 33(d).

---

## Instructions

1. **Caption** in standard format. Title: "Defendant's Responses and Objections to Plaintiff's First {RFPs/Interrogatories/RFAs}."
2. **Preamble.** Identify the responder, the discovery to which it is responding, and the date served.
3. **General Objections (sparing).** A short list of preserved general objections (e.g., to definitions exceeding the scope of Rule 26; to the implication that any response waives privilege; to the time period to the extent it predates the relevant period). Avoid the 30-line litany.
4. **Objections to Definitions and Instructions.** State which definitions or instructions you object to and why.
5. **Individual Responses.**
   - **RFPs.** For each: state objections (specific). Then state whether documents are being produced, the format, and the timing. Identify whether responsive material is being withheld on objection. Commit to a privilege log for documents withheld on privilege.
   - **Interrogatories.** For each: state objections (specific). Then answer (in full, partially, or refuse and explain). If invoking Rule 33(d) business-records option, identify the records by Bates range with sufficient detail.
   - **RFAs.** For each: admit, deny, qualify (admit in part / deny in part), or state inability to admit or deny under Rule 36(a)(4) with detail.
6. **Verification** for interrogatories.
7. **Signature block** with bar number and certification placeholders.

---

## Output Format (RFP example shown; adapt for interrogatories or RFAs)

```markdown
{COURT CAPTION}

{RESPONDER}'S RESPONSES AND OBJECTIONS TO {ISSUING PARTY}'S FIRST REQUESTS FOR PRODUCTION

{Responder} responds and objects to {Issuing Party}'s First Requests for Production as follows:

GENERAL OBJECTIONS
1. {Responder} objects to the definition of {term} to the extent it purports to require production of materials outside {Responder}'s possession, custody, or control.
2. {Responder} objects to any instruction that purports to enlarge {Responder}'s obligations under {Federal Rule 26 / state analog}.
3. Production is made subject to the {Protective Order entered on {date}} / {Rule 502(d) order entered on {date}}; inadvertent production of privileged material does not waive privilege.

OBJECTIONS TO DEFINITIONS AND INSTRUCTIONS
- {term} — {specific objection with reason}
- {instruction} — {specific objection with reason}

RESPONSES

REQUEST FOR PRODUCTION NO. 1: {request quoted}

Response: {Responder} objects to this Request to the extent it seeks documents protected by the attorney-client privilege or the work-product doctrine; documents withheld on these grounds will be identified on a privilege log. {Responder} further objects to the time period to the extent it extends before {date}, which is prior to {accrual / formation / relevant event}.

Subject to and without waiving the foregoing objections, {Responder} will produce non-privileged documents responsive to this Request and within {Responder}'s possession, custody, or control on a rolling basis beginning {date}, to be substantially completed by {date}, in the format set forth in the parties' ESI Protocol.

Documents are being withheld on the basis of: (a) the attorney-client privilege and work-product doctrine; (b) the temporal limitation stated above. No other documents are being withheld on the basis of objection.

REQUEST FOR PRODUCTION NO. 2: {…}

Response: {…}

Dated: {date}                       /s/ {counsel}

CERTIFICATE OF SERVICE
{...}
```

For interrogatories, add a verification page:

```markdown
VERIFICATION

I, {name}, {title} at {Responder}, state under penalty of perjury that the foregoing answers to interrogatories are true and correct based on my personal knowledge and on information supplied to me by employees and agents of {Responder} in the regular course of business.

Executed on {date}.

___________________
{name}, {title}
```

---

## Verification

- [ ] Each objection states a specific ground with enough detail to be assessed.
- [ ] No bare "overbroad / burdensome / vague" stack.
- [ ] Each RFP response states whether responsive material is being withheld on the basis of objection.
- [ ] Privilege-log commitment present for any privilege withholding.
- [ ] Interrogatory answers are verified.
- [ ] RFA responses comply with Rule 36(a)(4): admit, deny, qualify, or detailed inability statement.
- [ ] Rule 33(d) business-records option, if used, identifies records by Bates range with sufficient detail.
- [ ] Production timing and format stated for RFPs.
- [ ] No "subject to and without waiving" use that vacates the prior objections.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Boilerplate objection stack repeated for every request | Replace with specific, individualized objections |
| Failing to state whether anything is being withheld | Rule 34(b)(2)(C) requires it; courts compel a clear statement |
| Privilege objection without log commitment | State that withheld documents will be logged under Rule 26(b)(5) |
| RFA denial that does not address the substance | Rule 36(a)(4) requires the denial to fairly respond |
| RFA "lack of knowledge" without describing the reasonable inquiry | Detail the inquiry conducted before claiming inability |
| Pointing to "documents already produced" without Bates range | Rule 33(d) requires sufficient specification |
| Producing on a rolling basis without committing to a substantial completion date | Commit to a date; courts increasingly require it |
| Asserting work-product without identifying the anticipated litigation | Specify the litigation and the anticipating party |
| Using definitions to narrow the request without saying so | Object to the definition expressly |
