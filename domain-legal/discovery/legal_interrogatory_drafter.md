---
title: "Interrogatory Drafter"
category: legal/discovery
description: "Draft Rule 33 (or state-analog) interrogatories — including contention interrogatories — within the numerical limit, organized by theory, with definitions and instructions; counterpart to the existing discovery-response-objections prompt."
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
  - interrogatories
  - rule-33
  - contention-interrogatories
updated: "2026-05-08"
related_prompts:
  - domain-legal/discovery/legal_document_request_drafter.md
  - domain-legal/discovery/legal_discovery_response_objections.md
---

**Purpose:** Draft a defensible set of interrogatories that fits within the controlling numerical limit (25 in federal court absent leave), captures identification, fact, and contention information, and avoids common objections.

**When to use:** Initial discovery, supplementing after document review or deposition, contention interrogatories at end of fact discovery, training/evaluation tasks.

---

## Your Input

- **Court / venue and rule:** [Federal Rule 33 / state analog with numerical limit]
- **Issuing party / recipient:** [...]
- **Theories and claims:** [What the interrogatories support]
- **Existing pleadings:** [Recipient's complaint or answer; particularly affirmative defenses if recipient is a defendant]
- **Documents already exchanged:** [So requests can reference Bates ranges]
- **Known witnesses, custodians, systems:** [Identified targets]
- **Numerical limit:** [25 federal default; state limits vary; specify]
- **Subparts policy in this jurisdiction:** [How discrete-subparts are counted]
- **Strategic priorities:** [Identification, contention, computation of damages, affirmative-defense factual support]

---

## Constraints

**Must:**
- Stay within the numerical limit. Each "discrete subpart" usually counts separately under the controlling rule's interpretation.
- Lead with **identification** interrogatories: persons with knowledge, custodians, document custodians, witnesses to specific events.
- Include **fact** interrogatories on the operative events.
- Include **contention** interrogatories late in fact discovery: each fact supporting an asserted claim or defense; documents and witnesses for each contention.
- Include a **damages-computation** interrogatory if the recipient is the plaintiff (Rule 26(a)(1)(A)(iii) or analog provides initial-disclosure baseline; the interrogatory pushes for completeness).
- Include **affirmative-defense factual basis** interrogatories where the recipient is a defendant.
- Include **definitions and instructions** consistent with controlling rules and with the document-request set if both are served together.
- Reference Bates ranges where the answer can sensibly point to documents (Rule 33(d) option).

**Must Not:**
- Bundle disparate questions in one interrogatory to evade the count.
- Frame contention interrogatories so broadly they invite Rule 33(c)(2)-style objection ("premature contention").
- Demand legal-conclusion answers without factual content.
- Request information clearly outside Rule 26's proportional scope.
- Duplicate information already in initial disclosures unless seeking specificity.
- Use "any and all" or "every fact" boilerplate.

---

## Instructions

1. **Caption** in standard format.
2. **Definitions.** Mirror the document-request definitions if served together. Define "You / Your," "Person," "Identify," "Concerning," "Communication," "Time Period."
3. **Instructions.** State the duty to supplement; the option under Rule 33(d) to specify business records; the verification requirement; how subparts are counted (cross-reference the rule).
4. **Interrogatories**, grouped:
   - I. Identification (persons with knowledge; custodians; document sources)
   - II. Operative facts (event chronology, communications, decisions)
   - III. Damages and remedies
   - IV. Affirmative defenses (factual basis for each)
   - V. Contention interrogatories
5. Include **request for verification** under Rule 33(b)(5) (or analog).

---

## Output Format

```markdown
{COURT CAPTION}

{ISSUING PARTY}'S FIRST SET OF INTERROGATORIES TO {RECIPIENT} (NOS. 1–{N})

Pursuant to Federal Rule of Civil Procedure 33, {Issuing Party} requests that {Recipient} answer the following interrogatories under oath within thirty (30) days of service.

DEFINITIONS
1. "You" / "Your" means {Recipient}, its officers, directors, employees, and agents acting within the scope of their agency.
2. "Identify," when used with respect to a person, means to state the person's full name, last known address, telephone number, email address, and current employer and title.
3. "Identify," when used with respect to a document, means to state the document's title, date, author(s), recipient(s), Bates number if produced, and custodian(s).
4. {…}

INSTRUCTIONS
1. These interrogatories are continuing under Rule 26(e).
2. If You answer any interrogatory by reference to business records under Rule 33(d), specify the records (by Bates range) sufficient to permit the requesting party to locate the answer with no greater burden than the answering party.
3. Verification under Rule 33(b)(5) is required.
4. {…}

INTERROGATORIES

I. IDENTIFICATION

INTERROGATORY NO. 1: Identify each person with knowledge of the facts alleged in {paragraph(s) X–Y of Your {Complaint / Answer}}, and for each person describe in summary form the subjects on which the person has knowledge.

INTERROGATORY NO. 2: Identify each custodian of documents responsive to {Issuing Party}'s First Requests for Production, and for each custodian identify the systems and devices on which responsive documents may reside.

II. OPERATIVE FACTS

INTERROGATORY NO. 3: Describe in detail the events of {date}, identifying each person present, each communication that occurred, and each Document created or received in connection with those events.

INTERROGATORY NO. 4: {…}

III. DAMAGES AND REMEDIES

INTERROGATORY NO. 10: State each category of damages You seek, the amount or formula for each category, the documents You rely on to compute each category, and each person with knowledge of the computation.

IV. AFFIRMATIVE DEFENSES (when recipient is defendant)

INTERROGATORY NO. 15: For each affirmative defense asserted in Your Answer, state every fact on which You rely, identify each person with knowledge of those facts, and identify each Document supporting the defense.

V. CONTENTION INTERROGATORIES

INTERROGATORY NO. 20: State every fact on which You rely to support Your contention that {specific contention quoted from a pleading or response}, and identify each person with knowledge and each Document on which You rely.

INTERROGATORY NO. 21: {…}

Dated: {date}                       /s/ {counsel}

CERTIFICATE OF SERVICE
{...}
```

---

## Verification

- [ ] Total count of interrogatories within the numerical limit, treating discrete subparts under the controlling jurisdiction's approach.
- [ ] Identification interrogatories early; contention interrogatories late.
- [ ] Each contention interrogatory identifies a specific contention (often by quoting the pleading or prior response).
- [ ] Damages-computation interrogatory included where recipient is plaintiff.
- [ ] Affirmative-defense factual-basis interrogatories included where recipient is defendant.
- [ ] Definitions consistent with any contemporaneously served RFPs.
- [ ] Verification requirement noted.
- [ ] No "any and all" boilerplate; no embedded legal conclusions.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Bundling subparts to evade the count | Each discrete subpart usually counts separately; expect and budget for that |
| Broad contention interrogatory served too early | Some courts allow deferral as "premature contention"; serve late in fact discovery |
| Asking for "every fact" without specifying the contention | Quote the contention from the pleading or prior response |
| Requesting legal conclusions ("Why is your defense valid?") | Ask for facts and witnesses; conclusions can be objected to |
| Skipping the damages-computation interrogatory | Pushes plaintiffs past Rule 26(a)(1)(A)(iii) generalities |
| Forgetting the verification requirement | Rule 33(b)(5) requires verification by an officer or agent |
| Using definitions inconsistent with contemporaneously served RFPs | Mirror them; inconsistency invites objections |
| Demanding "all communications" in an interrogatory | Communications are usually better targeted by RFPs; use interrogatories for identifications and contentions |
