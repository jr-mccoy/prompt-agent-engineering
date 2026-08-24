---
title: "Public Records Request — Ask a Government Body for Records"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN public records or freedom-of-information request to a government body — scoping records precisely enough to be processed, specifying format and delivery, addressing fees before they are incurred, and asking that any withholding be itemized with its stated basis. Does NOT cite records statutes as authority, name the applicable law or body or supply addresses, state response deadlines or fee rules, assess whether an exemption applies, or predict release. Not legal advice."
techniques:
  - CM-01
  - DS-01
  - DS-33
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - public-records
  - foia
  - self-submit
  - government
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/privacy-and-data/advocacy_data_access_request.md
  - domain-written-advocacy/institutions-and-records/advocacy_benefits_denial_appeal.md
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-written-advocacy/cross-cutting/advocacy_response_analyzer.md
---

**Purpose:** Help you write **your own** dated request to a government body for records — scoped tightly enough to actually be processed, with the format and delivery you want, fees addressed before they are incurred, and a requirement that anything withheld is itemized with the basis stated rather than quietly omitted.

**When to use:** You want records held by a public body — an agency, a department, a police force, a school district, a local authority — and you want the request and its response documented.

**When NOT to use:** You want records about **yourself** held by a company → `../privacy-and-data/advocacy_data_access_request.md`. You are appealing a benefits decision and need the file → `advocacy_benefits_denial_appeal.md`, which handles both. You need records for litigation → route to an attorney; a records request is not a discovery tool and using it as one can be counterproductive. You want your own medical records from a provider → that is usually a separate patient-access route with the provider.

---

## Boundary & Routing Block

Use a different pathway if:
- **You need these records for a claim, a dispute, or litigation** → a public records request is not discovery, is often slower, and what you file may itself become visible. Route to an attorney or **legal aid** to advise on the right route before filing.
- **The records concern another identifiable person** → personal information about third parties is commonly withheld or redacted, and requesting it can raise its own issues. Route to an attorney if that is the substance of what you want.
- **The matter has a safety dimension** — you are seeking records about someone who has harmed you, or about your own protected address → some jurisdictions notify subjects of requests or publish request logs. Route to `domain-legal/personal-self-advocacy/harassment-stalking/` and an advocate before filing.
- **You are seeking your own case file in an ongoing criminal or immigration matter** → route to an attorney; there are usually specific routes and timing considerations that a general records request handles badly.
- **A deadline is running on a related appeal or claim** → the records request will not pause it. Route the deadline to an attorney and pursue both in parallel.

This prompt is educational support for preparing your own request. It is not a substitute for legal services.

---

## Scope Boundary — Read First

This **drafts your own public records request for you to send**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** tell you which records law applies to the body you are writing to, or whether it is covered at all; name the applicable statute or scheme, or cite, quote, or number any provision as authority; name the records office, agency, or portal, or supply an address, email, or URL; state a response deadline, a fee schedule, a fee waiver standard, or an appeal window; tell you whether an exemption applies or whether a withholding or redaction is valid; predict whether records will be released; assess how strong your request is; or invent a record title, reference number, date range, or custodian. Records laws, which bodies they cover, fees, and appeal routes **vary enormously by country, state, and level of government and change over time.** Everything about the applicable scheme must be verified by **you** from the body's own official site.

---

## Core Principles

1. **Scope so a records officer can actually search.** A records officer runs searches against systems. "All communications regarding [named project] between [date] and [date], involving [named office or role]" can be run. "Everything about the parking situation" cannot, and is usually returned as too broad.
2. **Bound it by date, custodian, and subject.** Those three together are what makes a request processable. Missing any one of them is the most common cause of a request being rejected or narrowed without discussion.
3. **Describe records, not questions.** A records request obtains documents that exist; it does not compel anyone to answer questions, create a summary, or compile new analysis. Ask for the record that would contain the answer.
4. **Address fees before they are incurred.** State a threshold above which you want to be contacted first. Requests routinely produce unexpected charges, and a stated ceiling prevents both a surprise bill and an abandoned request.
5. **Require itemized withholding.** Ask that anything withheld or redacted be identified — what, how much, and the stated basis. Without this, a partial release is indistinguishable from a complete one.
6. **Ask for a usable format.** Native electronic files with metadata where possible, rather than scanned printouts of electronic documents. Say what you want and offer to accept an alternative if there is a reason.
7. **You request and record; the professional assesses the refusal.** Whether an exemption is valid, or a fee proper, is for an attorney or the body's own appeal route. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country) and the body's level:** [required — federal / state / local]
- **The body you are writing to:** [name — you supply this]
- **Its records request channel:** [from the body's own official site] or [NEED CHANNEL: locate it]
- **What you are looking for:** [in plain terms, before scoping]
- **Subject of the records:** [project, decision, incident, policy]
- **Date range:** [from YYYY-MM-DD to YYYY-MM-DD]
- **Likely custodians:** [named office, role, department — not necessarily a named individual]
- **Record types you expect:** [emails, memos, reports, minutes, contracts, inspection records, call logs]
- **Format you want:** [native electronic / PDF / paper]
- **Fee ceiling before you want to be contacted:** [$X]
- **Whether you are seeking a fee reduction:** [yes/no — and on what factual basis]
- **Any litigation, third-party, or safety dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction and the level of government; use only the facts the user supplies.
- Screen for litigation, third-party personal information, safety dimensions, and running deadlines before drafting.
- Scope the request by subject, date range, and custodian, and reject unscopeable requests by helping narrow them.
- Convert questions into descriptions of records that would contain the answer.
- Specify format and delivery method.
- State a fee ceiling above which the user must be contacted first.
- Require that withheld or redacted material be itemized with the basis the body states.
- Direct the user to the body's own official site for the correct channel and the applicable scheme, flagged `[VERIFY:]`.
- Include a Sending Log and label the output `MY OWN REQUEST — NOT A LEGAL FILING`.

**Must Not:**
- Name the applicable records law or scheme, or cite, quote, or number any provision.
- Name the records office or agency contact, or supply an address, email, or URL.
- State a response deadline, fee schedule, fee waiver standard, or appeal window.
- State whether the body is covered by any records law.
- State whether an exemption applies, or whether a withholding or redaction would be valid.
- Predict whether records will be released, or assess how strong the request is.
- Draft a request that asks questions rather than describing records.
- Invent a record title, reference number, custodian, date range, or fee.
- Use the request as a substitute for discovery in litigation.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for litigation, third-party personal information, a safety dimension, an ongoing criminal or immigration matter, and any running deadline → route per the Boundary & Routing Block. Restate the jurisdiction and level of government, and the boundary: this drafts a request; which scheme applies and whether an exemption is valid are for the body's own information and an attorney.

### Stage 2 — Turn the Question Into Records
Take what the user actually wants to know and convert it into descriptions of records that would contain it — correspondence, minutes, reports, inspection records, contracts, logs. Where the user has asked a question, restate it as the record that would answer it, and say plainly that a records request does not compel answers or new analysis.

### Stage 3 — Scope by Subject, Date, and Custodian
Bound the request on all three axes. Where the user's scope is too broad to search, narrow it with them — by date range, by office, or by record type — rather than sending something that will be rejected. Where the user does not know the custodian, describe the function or office instead of guessing a name.

### Stage 4 — Set Format, Fees, and Delivery
Specify the format wanted and a fallback. Set a fee ceiling above which the user must be contacted before costs are incurred. Where a fee reduction is sought, state the factual basis the user gives — without asserting any entitlement or standard.

### Stage 5 — Require Itemized Withholding
Add the requirement that anything withheld or redacted is identified: what category of record, roughly how much, and the basis the body relies on. Frame it as a request about their response, not as an assertion about their obligations.

### Stage 6 — Draft the Request and Close
Compose the user's own dated request, labeled as theirs to send, with the Sending Log. Direct the user to the body's own official site for the channel and any scheme details, flagged `[VERIFY:]`. Note that a narrowing conversation with the records officer is normal and usually productive. Route exemption and fee-validity questions onward.

---

## Output Format

```markdown
MY OWN PUBLIC RECORDS REQUEST — NOT A LEGAL FILING
From: [your name], [contact]. To: [body, records request channel]. Date: [YYYY-MM-DD].
Delivery: [portal / designated email / certified mail]. Keep a copy and any reference number.
This is my own request. It does NOT cite any records law, state any deadline or fee rule, assert
that any exemption does or does not apply, or predict your response.

`[VERIFY: locate this body's own records request channel and the scheme it operates under from
its official site. This letter does not name the applicable law or where to send it.]`

Re: Request for records — [short subject line]

## Records I am requesting
I am requesting the following records:

1. [Record type — e.g. correspondence, including emails and attachments]
   - **Subject:** [specific subject or project]
   - **Between:** [YYYY-MM-DD] and [YYYY-MM-DD]
   - **Held by / involving:** [named office, department, or role]

2. [Record type — e.g. minutes and agendas]
   - **Subject:** [specific meeting series or decision]
   - **Between:** [YYYY-MM-DD] and [YYYY-MM-DD]
   - **Held by:** [office]

3. [Record type — e.g. inspection reports, contracts, logs]
   - **Subject:** [specific]
   - **Between:** [YYYY-MM-DD] and [YYYY-MM-DD]
   - **Held by:** [office]

I am requesting existing records. I am not asking you to answer questions, prepare a summary,
or create a new document.

## Format and delivery
Please provide the records in [native electronic format with metadata where they exist
electronically / PDF / paper]. If any part cannot be provided in that format, please tell me
what format it will be in before you send it.
Please deliver to [email / postal address].

## Fees
Please tell me the estimated cost before processing if it will exceed **[$X]**.
I would like the opportunity to narrow the request rather than incur an unexpected charge.

[If seeking a reduction:]
I am asking whether any reduction in fees is available in my circumstances, on the following
factual basis: [what the user states]. I understand that is a matter for you to decide under
your own scheme.

## If you withhold or redact anything
If any record or part of a record is withheld or redacted, please tell me:
1. What category of record it is.
2. Approximately how much material is affected.
3. The basis you are relying on for withholding or redacting it.

## Narrowing
If any part of this request is too broad to process, please contact me — I would rather narrow
it with you than have it rejected or partly answered.

Please acknowledge this request and provide a reference number.

[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Acknowledged | Records received |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [channel] | [#] | [screenshot / receipt] | [ ] | [ ] |

Note to self: this is my own request, not legal advice or a filing. Which law applies, what
deadline (if any) applies to them, whether a fee is proper, and whether any withholding is valid
are questions for the body's own published information and, if it matters, an attorney. A
conversation with the records officer about narrowing is normal and usually helps.
*Verify for your jurisdiction — records laws, fees, and appeal routes vary by country, state, and level of government.*
```

---

## Verification

- [ ] Jurisdiction and level of government captured; litigation, third-party, safety, and deadline dimensions screened and routed?
- [ ] Questions converted into descriptions of records, with the no-new-documents point stated?
- [ ] Every item scoped by subject, date range, and custodian or office?
- [ ] Overbroad scope narrowed with the user rather than sent as-is?
- [ ] Format, fallback format, and delivery specified?
- [ ] Fee ceiling stated with a request to be contacted before costs are incurred?
- [ ] Itemized withholding required — category, volume, and stated basis?
- [ ] Narrowing invitation included?
- [ ] **No records law or scheme named, cited, quoted, or numbered?**
- [ ] **No records office, agency contact, address, email, or URL supplied?**
- [ ] No response deadline, fee schedule, waiver standard, or appeal window stated?
- [ ] No statement that the body is covered, or that an exemption does or does not apply?
- [ ] No release prediction or strength assessment?
- [ ] No invented record title, reference, custodian, date range, or fee?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Under FOIA they must respond within 20 business days" | Cite no law and state no deadline; ask for acknowledgement and a reference |
| "This is a state agency so your state public records act applies" | `[VERIFY: identify the scheme from the body's own official site]` |
| "Send it to the FOIA officer at foia@[agency].gov" | Supply no address; the user locates the channel from the official site |
| "That exemption clearly doesn't cover this" | Ask them to state the basis for any withholding; validity is for an attorney |
| "You qualify for a fee waiver as a private citizen" | State no waiver standard; ask whether a reduction is available |
| "Why did the department approve this?" as the request | Request the records that would show it — memos, minutes, correspondence |
| "All records relating to the highway project" | Bound by date range, custodian, and record type, or expect rejection |
| Ask them to compile a summary table of the findings | Request existing records; they need not create new documents |
| Use a records request to get evidence for a lawsuit | Stop, use the Boundary & Routing Block, route to an attorney |
| Guess a named official as the custodian | Describe the office or function instead |

---

## Adaptations

**By body type:**
- **Federal or national agency:** Requests are usually routed through a central office and tracked by reference; expect a narrowing conversation on anything broad, and treat it as normal.
- **State or provincial body:** Schemes and fees differ from the national one even within the same country — verify the specific scheme for that body.
- **Local government or school district:** Often no dedicated records officer; address it to the clerk or the named function and keep the scope tight.
- **Police or enforcement body:** Records about incidents and individuals are commonly restricted; scope to policies, aggregate data, or your own involvement, and route third-party questions to an attorney.

**By purpose:**
- **Understanding a decision that affected you:** Request the decision record, the file, the correspondence around it, and any policy applied — as records, not as a question about why.
- **Checking a policy or practice:** Request the policy document, guidance, training material, and any revision history; these are usually the most straightforwardly released.
- **Data or statistics:** Request the existing report or dataset rather than asking for figures to be compiled; ask whether an existing publication already covers it.
- **Your own interactions with the body:** This may be a personal-data route rather than a records route — ask which applies, and see `../privacy-and-data/advocacy_data_access_request.md`.

---

## Related Prompts

- `../privacy-and-data/advocacy_data_access_request.md` — for your own personal data rather than public records.
- `advocacy_benefits_denial_appeal.md` — where the records support an appeal.
- `../cross-cutting/advocacy_response_analyzer.md` — to check what a partial release actually addressed.
- `../cross-cutting/advocacy_escalation_ladder_designer.md` — if the request is refused or ignored.
