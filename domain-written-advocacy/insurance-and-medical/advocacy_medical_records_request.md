---
title: "Medical Records Request — Get a Copy of Your Own Health Records"
category: advocacy
description: "[SELF-SUBMIT] Help a patient (or a personal representative with documented authority) draft THEIR OWN written request for copies of their health records from a clinic, hospital, lab, imaging centre, or pharmacy — scoping record types and date range, naming the format and delivery method, asking the cost in advance, and asking for an explanation of anything withheld — plus an optional separate request to correct an entry. Does NOT cite health-privacy law, state access rights, response periods, or fee limits, state what may be withheld, advise on records of another adult without authority, predict compliance, or invent provider details. Distinct from advocacy_data_access_request (general organizational data) and psychology_records_request_response_decision_aid (the clinician's side). Not legal or medical advice."
techniques:
  - CM-01
  - CM-03
  - ST-02
  - ST-03
  - QA-01
difficulty: beginner
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - medical-records
  - health-privacy
  - self-submit
  - patient
updated: "2026-09-24"
related_prompts:
  - domain-written-advocacy/privacy-and-data/advocacy_data_access_request.md
  - domain-written-advocacy/insurance-and-medical/advocacy_insurance_claim_denial_appeal.md
  - domain-written-advocacy/cross-cutting/advocacy_followup_and_deadline_tracker.md
  - domain-psychology/practice-operations/psychology_records_request_response_decision_aid.md
---

**Purpose:** Help you write **your own** request for copies of your health records — scoped so the records office can actually fulfil it, with the format and delivery you want, a question about cost before they start, and a request to explain anything they hold back. It also drafts, as a **separate** letter, a request to correct an entry you believe is wrong.

**When to use:** You need your records for a new clinician, an insurance appeal, a second opinion, a move, or your own understanding, and a phone call to the front desk has not produced them.

**When NOT to use:** You want what a non-medical company holds about you → `../privacy-and-data/advocacy_data_access_request.md`. You are the clinician deciding how to respond to a request → `domain-psychology/practice-operations/psychology_records_request_response_decision_aid.md`. You want another adult's records and do not hold documented authority for them → the Boundary & Routing Block. You need records **urgently for ongoing care** → ask your treating clinician to request them clinician-to-clinician first; that is often faster.

---

## Boundary & Routing Block

Use a different pathway if:
- **Records are needed urgently for treatment** → ask the treating clinician's office to request them directly from the other provider now; send this letter as well if you also want your own copy.
- **You are requesting for someone else** — a parent, spouse, adult child, or a person who has died → you usually need documented authority (a power of attorney, guardianship, representative appointment, or estate role). What counts varies; the records office will say what it needs. Where authority is unclear or contested, route to an attorney.
- **The records relate to a minor aged near adulthood, or to mental-health, substance-use, reproductive, or genetic care** → special handling often applies. Ask the records office what applies; do not rely on this prompt for what may be withheld.
- **You believe records were altered, or they relate to a malpractice concern or litigation** → route to an attorney before corresponding.
- **The provider has closed or you cannot find who holds the records** → `[VERIFY: identify the correct body from an official source]` for record custodians in your jurisdiction.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal or medical services.

---

## Scope Boundary — Read First

This **drafts your own records request for you to send**. It is **not legal advice, medical advice, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** cite a health-privacy statute or regulation as authority; state that you have a right of access or its limits; state how long the provider has to respond; state what fee may be charged; state what the provider may withhold; interpret any record's clinical content; tell you whether an entry is clinically wrong; name a privacy regulator or complaint body; predict compliance; or invent a provider address, patient number, or date. Health-records rules **vary by country, state, provider type, and record type.** Where such a concept appears it is flagged *verify for your jurisdiction*.

---

## Core Principles

1. **Scope it so it can be searched.** Record types (visit notes, lab results, imaging reports, imaging files, discharge summaries, medication lists, billing records) and a date range. "Everything" gets delayed or truncated.
2. **Name the format and delivery.** Electronic or paper; portal, secure email, encrypted media, or post; imaging as reports, image files, or both. The office will default to whatever is easiest for it.
3. **Ask the cost before they start.** Ask for a fee estimate and whether the format you chose changes it. Do not assert a fee limit.
4. **Ask them to explain anything withheld.** Request that any record not provided be identified with the reason, so you know what is missing.
5. **Identity and authority, attached.** Include what identifies you to the records office — full name, date of birth, patient number — and, for a representative, the authority document. Missing identification is the most common reason for delay.
6. **Correction is a separate letter.** Asking for copies and asking for a change are handled differently; combining them slows both.

---

## Your Input

- **Your jurisdiction:** [required]
- **Provider and its records or release-of-information office:** [name; the address or form it designates]
- **Are records needed urgently for treatment?:** [if yes → Boundary & Routing Block]
- **Patient identifiers:** [full name, any former names, date of birth, patient/MRN number if known]
- **Requesting for yourself or as a representative?:** [if representative: authority document held]
- **Record types and date range:** [types; YYYY-MM-DD to YYYY-MM-DD]
- **Format and delivery:** [electronic/paper; portal/email/media/post; imaging reports/files]
- **Sensitive categories involved?:** [mental health / substance use / reproductive / genetic / minor]
- **Any entry you want corrected:** [record, date, the entry verbatim, what you believe is inaccurate and why — factual]
- **Prior contact:** [date, channel, reference, outcome]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Screen urgency, representative authority, sensitive categories, and litigation first, and route.
- Scope by record type and date range.
- State format and delivery explicitly, including imaging form.
- Ask for a fee estimate before processing.
- Ask for any withheld record to be identified with a reason.
- Draft any correction request as a separate letter quoting the entry verbatim.
- Include a Sending Log and label the output `MY OWN REQUEST — NOT A LEGAL FILING`.

**Must Not:**
- Cite a health-privacy law or state access rights, response periods, fee limits, or withholding grounds.
- Interpret clinical content or state that an entry is clinically wrong.
- Draft a request for another adult's records without documented authority.
- Name a regulator or complaint body.
- Predict compliance or timing.
- Invent a provider address, patient number, or date.

---

## Instructions

### Stage 1 — Screen and Frame
Screen urgency (→ clinician-to-clinician), representative authority, sensitive categories, and litigation. Confirm jurisdiction.

### Stage 2 — Scope the Request
List record types and date range. Where the user needs records for a specific purpose, scope to it and say so — "for an insurance appeal of a claim dated [date]" helps the office find the right records.

### Stage 3 — Format, Delivery, and Cost
Record the format and delivery, and add a fee-estimate question.

### Stage 4 — Draft and Close
Compose the dated request with identification and any authority document listed as enclosed. If a correction is wanted, draft a second, separate letter: the entry verbatim, the factual inaccuracy, the supporting document, and a request that a statement of disagreement be added if they decline. Add Sending Logs.

---

## Output Format

```markdown
MY OWN RECORDS REQUEST — NOT A LEGAL FILING
From: [full name], DOB [YYYY-MM-DD], patient # [# or NEED ACCOUNT #:], [contact].
To: [provider], records / release-of-information office, [designated address or form].
Date: [YYYY-MM-DD]. Delivery: [method]. Keep a copy.
This is my own request. It does NOT cite law or state what you must provide or charge.

Re: Request for copies of my health records

## Records requested
| Record type | Date range |
|---|---|
| [visit notes] | [YYYY-MM-DD – YYYY-MM-DD] |
| [imaging — reports AND image files] | [...] |

## Format and delivery
[Electronic copy via [portal / secure email / encrypted media] — or paper by post to [address].]

## Also requested
1. A fee estimate before you begin, and whether the format above changes it.
2. If any record in scope is not provided, please identify it and tell me why.

Enclosed: [photo ID copy] [authority document, if a representative]
Please respond in writing by [date].
[Your name], [YYYY-MM-DD]

---
[OPTIONAL SEPARATE LETTER — MY OWN CORRECTION REQUEST]
Re: Request to correct an entry — record dated [YYYY-MM-DD]
The entry reads: "[verbatim]". I believe it is inaccurate because [factual reason], shown by
[document enclosed]. Please correct it, or if you decline, tell me why and add my statement of
disagreement (enclosed) to my record.

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Outcome |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [records office] | [#] | [receipt] | [YYYY-MM-DD] | [ ] |

Note to self: my access rights, timing, and fees are questions for an official source —
`[VERIFY: identify the correct body from an official source]`. *Verify for your jurisdiction.*
```

---

## Verification

- [ ] Urgency, representative authority, sensitive categories, and litigation screened and routed?
- [ ] Records scoped by type and date range?
- [ ] Format, delivery, and imaging form stated?
- [ ] Fee estimate requested; no fee limit asserted?
- [ ] Withheld records to be identified with reasons?
- [ ] Correction drafted separately, entry quoted verbatim, reason factual?
- [ ] No law, right, period, fee rule, or withholding ground asserted?
- [ ] No clinical interpretation?
- [ ] No regulator named; Sending Log included; no invented identifiers?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Under [privacy law] you must provide these within 30 days" | Ask for a response by a date you set; cite nothing |
| "You can only charge a reasonable cost-based fee" | Ask for a fee estimate before they begin |
| "Send me all my records" | Record types and a date range |
| "They can't withhold therapy notes from you" | Ask them to identify anything withheld and why |
| "This diagnosis is wrong" | Quote the entry; state the factual inaccuracy with a document; clinical judgement is the clinician's |
| Request a parent's records with no authority document | Stop — authority first; the office will say what it needs |
| "File a complaint with [named regulator]" | `[VERIFY: identify the correct body from an official source]` |
| Combine the copy request and correction in one letter | Two separate letters |

---

## Adaptations

**By purpose:**
- **Insurance appeal:** Scope to the dates and service in the denial, and ask for the notes and results that document it — see `advocacy_insurance_claim_denial_appeal.md`.
- **Changing clinicians:** Ask for summaries, medication lists, allergies, recent results, and imaging reports first; the full chart can follow.
- **Imaging for a second opinion:** Ask specifically for the image files in a viewable format, not just the report.

**By situation:**
- **No response:** Chase once with the original date and reference — `../cross-cutting/advocacy_followup_and_deadline_tracker.md`.
- **Portal shows only part of the record:** Say what the portal shows and ask for the rest in the scope above.

---

## Related Prompts

- `../privacy-and-data/advocacy_data_access_request.md` — the general-organization equivalent.
- `advocacy_insurance_claim_denial_appeal.md` — records are often the core of an appeal.
- `../cross-cutting/advocacy_followup_and_deadline_tracker.md` — chasing a request that stalls.
- `domain-psychology/practice-operations/psychology_records_request_response_decision_aid.md` — how the clinician's side sees the same request.
