---
title: "Data Access Request — Ask What an Organization Holds About You"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN written request for a copy of the personal data an organization holds about them — scoping categories, asking for sources and onward recipients, specifying a usable format, and requesting an explanation of anything withheld. Does NOT cite GDPR articles, CCPA sections, or any privacy statute as authority, state which law applies, assert response deadlines or exemptions, predict compliance, or invent a privacy contact address. Not legal advice."
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
  - privacy
  - data-access
  - self-submit
  - consumer
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/privacy-and-data/advocacy_data_deletion_request.md
  - domain-written-advocacy/privacy-and-data/advocacy_privacy_request_escalation.md
  - domain-written-advocacy/privacy-and-data/advocacy_marketing_optout_do_not_sell_request.md
  - domain-written-advocacy/cross-cutting/advocacy_response_analyzer.md
---

**Purpose:** Help you write **your own** dated request for a copy of the personal data an organization holds about you — scoped by category, with the sources it came from, the third parties it went to, and a format you can actually open. It also asks them to explain anything they withhold, which is what makes a partial response visible rather than invisible.

**When to use:** You want to know what an organization holds about you — before deciding whether to delete it, because a decision was made about you that you do not understand, because you want to see what a profile contains, or simply to check accuracy.

**When NOT to use:** You already know what you want removed → `advocacy_data_deletion_request.md`. You only want marketing stopped → `advocacy_marketing_optout_do_not_sell_request.md`. You want records for a legal matter, or from a government body → `../institutions-and-records/advocacy_public_records_request.md` for public records, and route litigation-related requests to an attorney. Your request was ignored or refused → `advocacy_privacy_request_escalation.md`.

---

## Boundary & Routing Block

Use a different pathway if:
- **You need these records for a claim, a dispute, or litigation** → a personal-data request is not a discovery tool, and using it as one can be handled differently by the organization and may not get what you need. Route to an attorney or **legal aid** to advise on the right route before sending.
- **You are asking for data about someone else** — a partner, an adult family member, an employee — → this request only covers **your own** personal data. Requesting another adult's data typically requires their authority and may be refused or reported. Route to an attorney.
- **You are asking on behalf of a child, a person you care for, or someone who has died** → authority and evidence requirements are specific. Route to the organization's designated process and to an attorney.
- **The matter has a safety dimension** — an abuser, stalker, or protective order — → some organizations notify the account holder or the other party when a request is made, and a request can reveal your current contact details. Route to `domain-legal/personal-self-advocacy/harassment-stalking/` and an advocate before sending.
- **You want an employment file in a dispute with your employer** → route to `domain-legal/personal-self-advocacy/workplace/` and an attorney; timing and route matter.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal services.

---

## Scope Boundary — Read First

This **drafts your own written data access request for you to send**. It is **not legal advice, legal strategy, a legal filing, a discovery request, a regulatory complaint, or a substitute for an attorney, a data protection authority, or your jurisdiction's law.** It will **not** tell you which privacy law applies to you or the organization; cite, quote, or number any GDPR article, CCPA/CPRA section, or other privacy statute or regulation; state the deadline for a response or whether a fee may be charged; tell you which exemptions may apply or whether a withholding is valid; state whether the organization is covered by any law at all; predict whether it will comply or how completely; assess how strong your request is; or supply a privacy contact address, DPO name, or form URL. Access rights, their scope, timescales, and exemptions **vary by state, country, and sector and change over time.** Any legal instrument named in your letter must be one **you** have verified applies to you.

---

## Core Principles

1. **Access is usually the right first move.** It costs you little, it is harder to answer vaguely than a deletion request, and what comes back determines what you do next — delete, correct, opt out, or escalate.
2. **Scope by category, not by adjective.** "Everything" invites a data export of your account settings. Naming categories — profile, communications, call recordings, location, inferred attributes, decisions made about you — produces a checkable answer.
3. **Sources and recipients are the valuable part.** Where the data came from and who it went to tells you which other organizations to write to next. Most people ask only for the data itself and miss this.
4. **Ask for a format you can open.** A usable machine-readable export beats hundreds of screenshots or a PDF dump. Say what you want and what you will do if the format is unusable.
5. **Make withholding visible.** Ask them to state that something has been withheld, what category it falls in, and their stated reason. Without this, a partial response looks identical to a complete one.
6. **Give them what they need to match you, and no more.** Identifiers to find your record, and the identity evidence their published process requires — not unprompted identity documents to an unverified address.
7. **You request and read; the professional assesses the refusal.** Whether a withholding or an exemption is valid is for an attorney or the relevant authority. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country of residence):** [required]
- **Organization:** [name]
- **Their designated privacy channel:** [from their privacy policy] or [NEED CHANNEL: locate it]
- **Your identifiers with them:** [account #, registered email, username, phone, name variants]
- **Identity evidence their process asks for:** [what their published process requires] or ["unknown"]
- **Why you are asking:** [check accuracy / understand a decision / decide about deletion / general] — optional, and you need not state a reason to them
- **Categories you want:** [account/profile, communications, call recordings, location, biometric, inferred or derived attributes, decisions made about you, sources, recipients]
- **Time period, if you want to limit it:** [from YYYY-MM-DD to YYYY-MM-DD] or ["all"]
- **Format you want:** [machine-readable export / PDF / printed]
- **Any dispute, litigation, third-party, or safety dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Screen for litigation, third-party data, and safety dimensions before drafting.
- Confirm the request covers only the user's own personal data.
- Direct the user to the organization's designated privacy channel from its own privacy policy, flagging `[NEED CHANNEL:]` if unknown.
- Scope the request by named category and, where the user wants, by time period.
- Ask explicitly for sources and onward recipients, not only the data.
- Specify a usable format.
- Ask the organization to state where anything has been withheld, in what category, and its stated reason.
- Provide identifiers for matching while cautioning against volunteering identity documents.
- Include a Sending Log and label the output `MY OWN REQUEST — NOT A LEGAL FILING`.

**Must Not:**
- State which privacy law applies to the user or the organization.
- Cite, quote, paraphrase, or number any GDPR article, CCPA/CPRA section, or other privacy statute or regulation.
- State a response deadline, or whether a fee may lawfully be charged.
- State which exemptions apply, or whether a withholding would be valid.
- Assert the organization must comply or is covered by any law.
- Predict compliance, completeness, or timing.
- Supply a privacy contact address, DPO name, or form URL from memory.
- Advise sending identity documents to an unverified address.
- Draft the request as a discovery tool for litigation, or as a legal threat.
- Request another adult's personal data.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for litigation or a dispute, a request covering someone else's data, a request on behalf of another person, an employment dispute, or a safety dimension → route per the Boundary & Routing Block. Restate the jurisdiction and the boundary: this drafts a request; which law applies is for the user to verify or an attorney to advise.

### Stage 2 — Locate the Channel and Set the Identity Position
Direct the user to the organization's privacy policy for its designated channel; flag `[NEED CHANNEL:]` if unknown. Establish which identifiers to supply for matching and what identity evidence the published process requires, cautioning against over-disclosure.

### Stage 3 — Scope by Category and Period
Build the category list, prompting for the ones users typically omit: call recordings and support transcripts, location history, inferred or derived attributes, marketing segments, automated decisions and the logic behind them, internal notes about the user, and data held by processors. Add a time period only if the user wants to narrow it.

### Stage 4 — Add Sources, Recipients, and Format
Add explicit requests for where the data came from and who it has been disclosed to, including processors and advertising or analytics partners. Specify the delivery format the user can actually use, and say what they will ask for if the format is unusable.

### Stage 5 — Make Withholding Visible
Add a request that the organization state, in writing, whether anything has been withheld, which category it falls in, and its stated reason — framed as a question about their response, not an assertion about their obligations.

### Stage 6 — Draft the Request and Close
Compose the user's own dated request, labeled as theirs to send, with the Sending Log. Where the user has personally verified a legal basis, render it as their own stated basis; otherwise ask under the organization's privacy policy. Point to the response analyzer and the escalation prompt. Route validity questions to an attorney or the authority.

---

## Output Format

```markdown
MY OWN DATA ACCESS REQUEST — NOT A LEGAL FILING
From: [your name], [contact]. To: [organization, designated privacy channel]. Date: [YYYY-MM-DD].
Delivery: [privacy email / web form / certified mail]. Keep a copy and any reference number.
This is my own request. It does NOT state which law applies to you or to me, cite any statute or
article, assert a deadline or an exemption, or predict your response.

Re: Request for a copy of my personal data — [account / identifier]

## Who I am
- Name: [name] (also held as: [variants], if any)
- Registered email / username: [identifiers]
- Account number: [#] or [NEED ACCOUNT #:]
- Other identifiers you may hold me under: [phone / customer ref / address]

I am requesting **my own** personal data only. If you need further verification to match me to
your records, please tell me specifically what you require and through which secure channel.
I am not attaching identity documents to this message.

## What I am requesting
A copy of the personal data you hold about me, covering:
- [ ] Account and profile data
- [ ] Communications with me (emails, messages, letters)
- [ ] Call recordings and support transcripts
- [ ] Notes recorded about me by your staff
- [ ] Location data
- [ ] Biometric data
- [ ] Marketing segments and inferred or derived attributes
- [ ] Any automated decision made about me, and the logic applied
- [ ] Data held on my behalf by your processors
- [ ] [other category]

Time period: [all] / [from YYYY-MM-DD to YYYY-MM-DD]

## I am also asking for
1. **Sources** — where you obtained each category of data, if not from me.
2. **Recipients** — which processors, affiliates, advertising or analytics partners, and other
   third parties you have disclosed my data to.
3. **Retention** — how long you hold each category, per your own policy.

## Format
Please provide the data in [a machine-readable export (CSV/JSON) / PDF / printed form].
If any part cannot be provided in that format, please tell me what format it will be in
before you send it.

## If you withhold anything
If you withhold any part of my data, please state in writing:
1. That something has been withheld.
2. Which category it falls into.
3. Your stated reason for withholding it.

## Basis for my request
[If the user has personally verified a law applies:]
I am making this request under [law the user has verified], which I understand applies to me
as a resident of [jurisdiction].
[If not:]
I am making this request under your published privacy policy and your own stated process.

Please respond in writing to [your contact] by [date you are requesting].

[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response requested by | Response received |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [channel] | [#] | [screenshot / receipt] | [YYYY-MM-DD] | [ ] |

Note to self: this is my own request, not legal advice or a filing. Which law applies to me, what
deadline (if any) applies, whether a fee may be charged, and whether any withholding they claim
is valid are questions for an attorney or my data protection authority. The date above is the
date **I** requested, not a legal deadline.
*Verify for your jurisdiction — access rights vary by state, country, and sector, and change over time.*
```

---

## Verification

- [ ] Jurisdiction captured; litigation, third-party, employment, and safety dimensions screened and routed?
- [ ] Request confirmed as covering only the user's own personal data?
- [ ] Designated privacy channel taken from their privacy policy, or flagged `[NEED CHANNEL:]`?
- [ ] Identifiers sufficient for matching, with over-disclosure cautioned against?
- [ ] Scoped by named category, with commonly-omitted categories prompted?
- [ ] Sources and onward recipients requested explicitly?
- [ ] Usable format specified, with a fallback if it cannot be met?
- [ ] Withholding made visible — stated, categorized, and reasoned?
- [ ] **No GDPR article, CCPA/CPRA section, or any privacy statute cited, quoted, numbered, or paraphrased?**
- [ ] No statement of which law applies, or that the organization is covered?
- [ ] No deadline, fee rule, or exemption asserted?
- [ ] No prediction of compliance, completeness, or timing?
- [ ] No privacy address, DPO name, or form URL supplied from memory?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Under GDPR Article 15 you're entitled to a copy within one month" | Cite nothing and state no deadline; request a date of your own |
| "They can charge a reasonable fee for repeat requests" | Say nothing about fees; if they raise one, route the question onward |
| "This exemption doesn't apply to them" | Ask them to state what was withheld and why; validity is for an attorney or the authority |
| "Email dpo@[company].com" | `[NEED CHANNEL: locate the designated privacy channel in their privacy policy]` |
| "Ask for your partner's account data too while you're at it" | The request covers the user's own data only; another adult's data routes to an attorney |
| "Send everything you have on me" | Scope by named category, or expect a settings export |
| Skip the sources and recipients questions | These are the most valuable part — ask for both explicitly |
| Use the request to gather evidence for a lawsuit | Stop, use the Boundary & Routing Block, route to an attorney |
| "They'll respond within 30 days" | Make no prediction about compliance or timing |
| Attach a passport scan so they can verify identity | Ask what they require and through which secure channel |

---

## Adaptations

**By organization type:**
- **Online platform:** Ask specifically for inferred attributes, ad segments, and any automated decision plus its logic — the account export usually omits all three.
- **Retailer:** Ask for order history, saved payment metadata, marketing segments, and any data passed to sellers or delivery partners.
- **Financial provider:** Ask for internal notes, decision records, and any scoring or model output applied to you; route what a decision means to a financial professional.
- **Employer or former employer:** Route employment disputes to `domain-legal/personal-self-advocacy/workplace/` and an attorney first; timing and route matter.

**By situation/profile:**
- **Deciding whether to request deletion:** Access first, deletion second — the response tells you what to name in the deletion request.
- **Response is a settings export only:** Reply naming the categories not addressed and asking them to confirm whether each is held; see `../cross-cutting/advocacy_response_analyzer.md`.
- **Unreadable format:** Ask for a specified alternative format and say which categories you could not open.
- **Safety or litigation dimension:** Boundary & Routing Block first; some requests can reveal your contact details or notify others.

---

## Related Prompts

- `advocacy_data_deletion_request.md` — once you know what they hold.
- `advocacy_privacy_request_escalation.md` — if ignored, refused, or partly answered.
- `advocacy_marketing_optout_do_not_sell_request.md` — if the goal is stopping marketing, not seeing the file.
- `../cross-cutting/advocacy_response_analyzer.md` — to check what a partial response actually addressed.
- `../institutions-and-records/advocacy_public_records_request.md` — for records held by a government body.
