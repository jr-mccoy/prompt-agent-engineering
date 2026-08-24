---
title: "Document Request (RFP) Drafter"
category: legal/discovery
description: "Draft Rule 34 (or state-analog) requests for production with definitions, instructions, and individually targeted requests organized by claim and theory; calibrated to proportionality and scope under the operative discovery rules."
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
  - rfp
  - document-requests
  - rule-34
updated: "2026-05-08"
related_prompts:
  - domain-legal/discovery/legal_interrogatory_drafter.md
  - domain-legal/discovery/legal_discovery_response_objections.md
  - domain-legal/discovery/legal_ediscovery_custodian_interview.md
---

**Purpose:** Produce a clean, defensible set of Rule 34 RFPs (or state analog) tied to specific claims and theories, with definitions/instructions calibrated to the proportionality standard, custodian/source coverage, and ESI realities.

**When to use:** Initial document requests, supplemental requests after deposition or document review surfaces new sources, training/evaluation tasks.

---

## Your Input

- **Court / venue:** [Federal / state, with rule]
- **Case caption and matter description:** [...]
- **Issuing party:** [Plaintiff / defendant]
- **Recipient:** [Specific party]
- **Claims, defenses, and theories the requests support:** [Issuing party's roadmap]
- **Known custodians or business systems:** [If known — drives definitions and instructions]
- **Time period:** [Default: from {date} to present; calibrate to limitations and accrual]
- **ESI plan / protocol status:** [Negotiated / pending / none]
- **Privilege protocol status:** [Clawback under Rule 502(d) / state analog — yes/no]
- **Scope priorities:** [What matters most to develop first]

---

## Constraints

**Must:**
- Preface with **definitions** of key terms (Defendant, Document, Communication, Concerning, Identify, Possession-Custody-or-Control, Electronic Data, Time Period) consistent with the controlling rules.
- Preface with **instructions** that comply with Rule 34's specificity-of-objection standard and the controlling ESI/proportionality rules.
- Group requests by **theory or claim**, not in random order.
- Each request must be **specific enough to permit a reasonable, targeted search**. Avoid catch-all language that triggers boilerplate refusal.
- Cover the **likely sources**: email, attachments, chat (Slack/Teams), text messages, custodial files, shared drives, ticketing/CRM systems, Bates'd hard-copy files, deletion logs.
- Include requests sufficient to **build a defensible chain of custody** for documents the issuing party will rely on at trial.
- Calibrate to **proportionality** — the number, scope, and burden should be defensible if challenged.

**Must Not:**
- Stack vague catch-all requests ("All documents relating to the lawsuit"). These get sustained objections.
- Demand "every document" without temporal or topical constraints.
- Use "any and all" boilerplate.
- Embed legal conclusions in the requests ("All documents showing Defendant's negligence"); use neutral descriptive language.
- Request privileged material (attorney-client communications between recipient and recipient's counsel concerning this matter).
- Skip ESI plan considerations for matters with substantial ESI.

---

## Instructions

1. **Caption** in the standard discovery format.
2. **Definitions.** Cover terms that recur. Tie to the recipient's organization (e.g., define "Defendant" to include its officers, directors, employees, agents acting within scope, and named subsidiaries) without overreaching.
3. **Instructions.** Time period; production format (load files, native format, OCR'd PDFs, hash values, metadata fields); privilege log requirements (per Rule 26(b)(5) or state analog); supplementation duty.
4. **Requests, organized by theory.** For each theory:
   - State the theory in the heading: "Requests Concerning {Theory: e.g., Defendant's Knowledge of Defect}".
   - Use targeted requests with date ranges and topic limits.
   - Use multiple narrow requests rather than one broad one where the topics differ in privilege exposure or custodian set.
5. **Catch-all backstop.** A single, narrowly framed catch-all at the end (if used) — e.g., "Documents identified, referenced, or relied upon in the responses to {specific other discovery}."

---

## Output Format

```markdown
{COURT CAPTION}

{ISSUING PARTY}'S FIRST REQUESTS FOR PRODUCTION OF DOCUMENTS TO {RECIPIENT} (NOS. 1–{N})

Pursuant to Federal Rule of Civil Procedure 34, {Issuing Party} requests that {Recipient} produce, within thirty (30) days of service, the documents and electronically stored information described below.

DEFINITIONS

1. "Defendant" means {recipient} and its officers, directors, employees, agents acting within the scope of their agency, and the following subsidiaries and affiliates: {list}.
2. "Document" has the meaning of "documents or electronically stored information" under Federal Rule of Civil Procedure 34(a)(1)(A) and includes {emails; chat messages including Slack and Microsoft Teams; SMS and other text messages; voicemails; calendar entries; contracts and amendments; meeting minutes; presentations; spreadsheets; databases and database exports; tickets and CRM records; logs; metadata}.
3. "Communication" means any transmittal of information.
4. "Concerning" means relating to, referring to, describing, evidencing, or constituting.
5. "Identify" {with respect to documents and persons, as appropriate}.
6. "Time Period" means the period from {start} to the present unless otherwise specified.
7. {…}

INSTRUCTIONS

1. Production format: {single-page TIFF with load file and OCR + native files for spreadsheets, audio/video, and other files where the native is necessary; metadata fields {sender, recipient, cc, bcc, date sent, date received, subject, file path, custodian, MD5 hash}}.
2. Privilege log: produce a log under Federal Rule of Civil Procedure 26(b)(5) for any document withheld or redacted on privilege grounds, with sufficient detail to permit assessment of the claim.
3. Supplementation: this request is continuing under Rule 26(e).
4. {…}

REQUESTS

I. Requests Concerning {Theory 1, e.g., Formation of the Agreement}

REQUEST FOR PRODUCTION NO. 1: All drafts of the {Agreement} exchanged between {Party A} and {Party B} during the Time Period.

REQUEST FOR PRODUCTION NO. 2: All Communications between {Party A} and {Party B} concerning the negotiation of the {Agreement} between {date} and {date}.

REQUEST FOR PRODUCTION NO. 3: {…}

II. Requests Concerning {Theory 2}

REQUEST FOR PRODUCTION NO. 10: {…}

III. Requests Concerning {Custodian Coverage / ESI Sources}

REQUEST FOR PRODUCTION NO. 20: All policies, retention schedules, and litigation-hold notices in effect during the Time Period concerning {topic}.

REQUEST FOR PRODUCTION NO. 21: Documents sufficient to identify the custodians, business units, and systems that would contain Documents responsive to these requests.

IV. Catch-Up

REQUEST FOR PRODUCTION NO. {N}: Documents identified, referenced, or relied upon in {Recipient}'s answers to {Issuing Party}'s First Set of Interrogatories.

Dated: {date}                       /s/ {counsel}

CERTIFICATE OF SERVICE
{...}
```

---

## Verification

- [ ] Definitions cover recurring terms without overreaching the recipient's possession-custody-or-control.
- [ ] Instructions specify production format, metadata fields, and privilege log requirements.
- [ ] Each request is specific enough to permit a targeted search.
- [ ] Requests grouped by theory or claim.
- [ ] Time period limited; no open-ended "all documents ever."
- [ ] No legal-conclusion phrasing inside the requests.
- [ ] No requests for privileged communications between recipient and its counsel.
- [ ] ESI sources (chat, mobile, CRM, ticketing) covered where applicable.
- [ ] Catch-up request is narrow, not generic.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| "All documents relating to the lawsuit" | Replace with claim-tied targeted requests |
| Forgetting chat / mobile / collaboration sources | Define Document to include these and address in instructions |
| Embedding legal conclusions ("documents proving negligence") | Use neutral descriptive language |
| Demanding metadata without specifying fields | Specify the metadata fields and the production format |
| Asking for "any and all" without temporal or topical limits | Always narrow with a time period and topic |
| Requesting privileged attorney-client material | Exclude or expressly carve out |
| Boilerplate definitions copied across matters without tailoring | Tailor definitions to the recipient's organizational structure |
| Skipping a request for retention policies and litigation-hold notices | These are foundational for ESI completeness assessment |
| Single mega-request that bundles different theories | Multiple narrower requests reduce objection surface |
