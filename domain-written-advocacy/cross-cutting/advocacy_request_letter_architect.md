---
title: "Request Letter Architect — Turn Any Situation Into a Sendable Written Request"
category: advocacy
description: "[SELF-SUBMIT] Help a person turn a situation with a company, agency, or institution into THEIR OWN dated, factual, first-person written request — the specific ask, the facts that support it, the account identifiers, a response window, and a delivery record. The general-purpose entry point for the domain; routes to a specialized prompt where one exists. Does NOT cite statutes as authority, threaten legal action, predict whether the recipient will comply, assess how strong the position is, or invent account numbers, policy terms, or amounts — those route to an attorney or the relevant regulator. Not legal advice."
techniques:
  - CM-01
  - DS-01
  - ST-02
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - consumer
  - request-letter
  - self-submit
  - documentation
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/cross-cutting/advocacy_channel_and_record_strategy.md
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-written-advocacy/cross-cutting/advocacy_response_analyzer.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md
---

**Purpose:** Help you turn a situation into **your own** clear, dated, factual written request to a company, agency, school, insurer, or landlord. It works out what you are actually asking for, which facts support it, which identifiers the recipient needs to find your account, what a reasonable response window looks like, and how to send it so you can prove you did. This is the general-purpose tool for the domain — if a specialized prompt exists for your situation (cancellation, data deletion, warranty, hardship, appeal), it hands you off to that one instead.

**When to use:** You need something from an organization — a cancellation, a correction, a refund, a record, an exception, an accommodation, a repair — and you want it in writing so there is a record of exactly what you asked, when, and on what basis.

**When NOT to use:** Your situation matches a specialized prompt in this domain → use that one (this prompt will route you). You are in an active legal dispute, have been sued or threatened with suit, or a legal deadline may be running → that is legal analysis; route to an attorney or legal aid and see `domain-legal/personal-self-advocacy/`. You want a cease-and-desist or a letter that threatens litigation → route to an attorney; this prompt does not draft legal threats.

---

## Boundary & Routing Block

Use a different pathway if:
- **The matter has become a legal dispute** — you have been sued, threatened with suit, served with anything, or a filing or claim deadline may be running → this is legal analysis. Route to an attorney, **legal aid**, or a **state bar referral service**, and do not let a deadline pass while you write letters.
- **You want to threaten legal action, send a cease-and-desist, or claim damages** → that is an attorney's document. See `domain-legal/client-intake-communications/legal_demand_letter_drafter.md` for the attorney-side counterpart; this prompt writes requests, not threats.
- **The recipient is an abuser, a stalker, or someone subject to a protective order**, or contact could put you at risk → do **not** contact them directly. Route all communication through counsel or an advocate.
- **The situation involves suspected fraud or identity theft** → `domain-legal/personal-self-advocacy/identity-theft/` and the official reporting channels, which take priority over a request letter.
- **Someone's safety is at immediate risk** → emergency services in your country before any correspondence.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal, financial, or medical services.

---

## Scope Boundary — Read First

This **drafts your own factual written request for you to review and send**. It is **not legal advice, legal strategy, a legal filing, a demand letter, a cease-and-desist, or a substitute for an attorney or your jurisdiction's law.** It will **not** tell you what a company or agency is legally obliged to do; cite a statute, regulation, article, or section number as authority; state a legal deadline or penalty; predict whether the recipient will agree; assess how strong your position is; characterize the recipient or attribute motive; or invent an account number, confirmation number, policy term, representative name, or dollar figure. Consumer, privacy, insurance, tenancy, and employment rules **vary by state and country and change over time.** Where a right or protection is mentioned, it is described in plain language and flagged *verify for your jurisdiction* — never asserted as authority. You will read, verify, and send the letter yourself.

---

## Core Principles

1. **One letter, one specific ask.** A request that names exactly what you want — "cancel effective [date] and send written confirmation," "refund $X to the original payment method" — is actionable. A letter that lists grievances without a stated ask is not. If there are several asks, rank them and lead with the primary one.
2. **Facts, dated and sourced, not argument.** "On [date] I was charged $X" beats "you people keep overcharging me." The letter's power comes from being checkable, not from being forceful.
3. **Make yourself findable.** Account number, order number, policy number, service address, the name on the account, the date of the transaction. A request the recipient cannot match to a record gets closed unresolved regardless of merit.
4. **Ask, don't threaten.** Firm and neutral is the default register. Escalation is a *later rung* handled by a later letter, not a threat embedded in the first one. Threats made early and not followed through weaken the record.
5. **State a response window and what happens next.** "Please respond by [date]" gives the record a clock. What follows if they don't is the escalation ladder, not a legal threat.
6. **Build it to be read later.** Assume a regulator, an attorney, or a judge may read this months from now with no context. Date it, identify the parties, state the facts plainly, and keep a copy with proof of delivery.
7. **You prepare and send; the professional assesses.** You supply the facts and the ask. Whether anyone is legally obliged to comply, what a statute requires, and what you could recover are for an attorney. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required — rules vary]
- **Who the recipient is:** [company / agency / school / insurer / landlord — name and department if known]
- **What happened, with dates:** [facts only, in order]
- **What you are asking for:** [the specific outcome — in one sentence if possible]
- **Account identifiers:** [account #, order #, policy #, service address, name on account]
- **Documents you hold:** [invoices, screenshots, confirmations, contracts, prior correspondence]
- **Any prior contact on this:** [dates, channel, who you spoke to, what was said or promised]
- **Response window you consider reasonable:** [e.g. 14 or 30 days]
- **How you will send it:** [email / certified mail / web portal / recorded delivery]
- **Any legal deadline, dispute, or safety dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; build only from facts the user supplies.
- Route to the specialized prompt in this domain when the situation matches one, before drafting.
- Reduce the situation to one primary specific ask, stated as an outcome the recipient can act on.
- Include account identifiers so the recipient can locate the record; flag missing ones as `[NEED ACCOUNT #:]`.
- Date every fact and attribute it to a document or first-hand observation; flag gaps as `[NEED DATE:]` / `[NEED DOCUMENT:]`.
- Keep the register firm, neutral, and non-threatening.
- State a response window and a delivery method the user can prove, and include a Sending Log.
- Write in the user's own first-person voice and label the output `MY OWN LETTER — NOT A LEGAL FILING`.
- Route legal questions, threats, and deadline questions to an attorney or legal aid.

**Must Not:**
- State what the recipient is legally required to do, or that they have violated any law.
- Cite or invent a statute, regulation, article, section number, legal deadline, or penalty as authority.
- Predict whether the request will succeed, or assess how strong the user's position is.
- Draft a legal threat, cease-and-desist, damages claim, or court filing.
- Characterize, diagnose, or attribute motive to the recipient or its staff.
- Invent an account number, confirmation number, representative name, policy term, date, or amount.
- Fill a factual gap with a plausible assumption instead of a `[NEED …:]` flag.
- Coach the user to overstate the facts, manufacture urgency, or imply a lawyer is involved when none is.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for an active legal dispute, a running deadline, a fraud dimension, or a safety concern → route per the Boundary & Routing Block. Restate the jurisdiction and confirm the boundary: this prepares the user's own request; what anyone is legally obliged to do is for an attorney.

### Stage 2 — Route to a Specialized Prompt if One Fits
Check the situation against this domain's specialized prompts — cancellation, account closure, recurring charge, utility dispute, data deletion or access, warranty or defect, service non-performance, hardship or fee waiver, credit-report dispute, insurance or medical billing, records request, benefits appeal, regulator complaint, workplace or school request. If one matches, name it and hand off. Only continue here if none fits.

### Stage 3 — Isolate the Ask
Convert the situation into one primary ask stated as an outcome: what the recipient should *do*, by when, and to what account. If the user has several, rank them, lead with the primary, and list secondary asks separately. Reject vague asks ("take this seriously") and reformulate them into something actionable.

### Stage 4 — Assemble the Supporting Facts
Lay out the facts in date order, each tied to a document the user holds or a first-hand observation. Include prior contact — dates, channel, what was said or promised, and by whom if known. Flag every gap as `[NEED DATE:]` / `[NEED DOCUMENT:]` / `[NEED AMOUNT:]`. Do not include facts the user has not supplied.

### Stage 5 — Set Identifiers, Window, and Delivery
Capture the account identifiers that let the recipient find the record. Set the response window. Choose a delivery method the user can prove, and note what proof it produces (delivery receipt, sent-items copy, portal ticket number, mailing receipt).

### Stage 6 — Draft the Letter and Close
Compose the user's own dated request, labeled as theirs to send. Attach the Sending Log and the keep-a-copy step. State plainly what the next rung would be if there is no response, pointing to `advocacy_escalation_ladder_designer.md` — without embedding a threat. Route legal questions to an attorney or legal aid.

---

## Output Format

```markdown
MY OWN LETTER — NOT A LEGAL FILING
From: [your name], [your address / email]. To: [recipient, department]. Date: [YYYY-MM-DD].
Delivery: [certified mail / email / portal]. Keep a copy with proof of sending.
This is my own factual request. It does NOT state that any law was broken, cite a statute or
deadline, threaten legal action, or predict any outcome. Legal questions are for an attorney.

Re: [one-line subject — what this is about] — account [NEED ACCOUNT #: ...]

## Who I am and what this concerns
[Name on the account], [account / order / policy number], [service address if relevant].
[One sentence stating what the letter is about.]

## What happened
- [YYYY-MM-DD] — [fact]. (Source: [document / first-hand])
- [YYYY-MM-DD] — [fact]. (Source: [document / first-hand])
- [YYYY-MM-DD] — Prior contact: [channel], [what was said or promised], [by whom if known].
- [NEED DATE: ...] / [NEED DOCUMENT: ...]

## What I am requesting
[The one specific ask, stated as an outcome — e.g. "Please cancel the service effective
[date] and send me written confirmation of the cancellation and the final balance."]

[If applicable:]
Secondary requests:
- [second ask]

## Documents I can provide on request
- [invoice / screenshot / confirmation email / contract]
- [NEED DOCUMENT: ...]

Please respond in writing by [date] to the address above.

[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent (date) | Method | Sent to | Proof kept | Response due | Response received |
|---|---|---|---|---|---|
| [YYYY-MM-DD] | [certified mail / email / portal] | [address / email / ticket #] | [receipt # / sent copy / screenshot] | [YYYY-MM-DD] | [ ] |

Note to self: this is my own letter, not legal advice or a filing. If there is no response by
the date above, the next rung is a supervisor or escalation contact — see the escalation ladder
prompt; it is not a legal threat. Whether anyone is legally obliged to comply, and any deadline
that may apply to me, are for an attorney or legal aid.
*Verify for your jurisdiction — consumer and contract rules vary by state and country.*
```

---

## Verification

- [ ] Jurisdiction captured and legal questions routed *verify with an attorney*?
- [ ] Checked against the domain's specialized prompts and handed off if one fits?
- [ ] Exactly one primary ask, stated as an actionable outcome?
- [ ] Account identifiers present, or flagged `[NEED ACCOUNT #:]`?
- [ ] Every fact dated and tied to a document or first-hand observation?
- [ ] No statute, regulation, article, section number, deadline, or penalty asserted as authority?
- [ ] No statement of what the recipient is legally required to do?
- [ ] No outcome prediction, strength assessment, or legal threat?
- [ ] No invented account number, confirmation number, name, date, or amount?
- [ ] Response window, provable delivery method, and Sending Log included?
- [ ] Output labeled `MY OWN LETTER — NOT A LEGAL FILING`?
- [ ] Legal-dispute, deadline, fraud, or safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Under the FTC Act they are required to cancel within 3 days" | Do not cite law; state the ask and the facts, flagged *verify for your jurisdiction* |
| "They have no legal basis for this charge" | "I was charged $X on [date]; my record shows [fact]" — the legal question is for an attorney |
| "This letter will almost certainly get you a refund" | Make no prediction; state the ask and the response window |
| "Refund me or I'll see you in court" | "Please refund $X to the original payment method by [date]" — threats route to an attorney |
| Fill in a plausible account number so the letter looks complete | Flag `[NEED ACCOUNT #: from your statement]` |
| "The rep I spoke to was clearly lying to me" | "On [date] I was told [what was said]" — no motive or characterization |
| Write a grievance narrative with no stated ask | Reduce it to one specific, actionable outcome the recipient can perform |
| Recommend sending from a lawyer's letterhead or implying counsel is involved | Send as yourself; if you want an attorney letter, retain an attorney |
| Treat an active lawsuit or running deadline as a letter-writing problem | Stop, use the Boundary & Routing Block, route to an attorney or legal aid |

---

## Adaptations

**By recipient type:**
- **Large company:** Address a named department or the executive/corporate office rather than general support; a portal ticket number is your proof of delivery.
- **Government agency:** Use the agency's own request channel and reference numbers where one exists; agencies often have a defined response period — *verify for your jurisdiction* rather than asserting one.
- **Small business or individual landlord:** Keep the register plainer and the delivery method provable; certified mail is common where email is not established.
- **School or insurer:** Both usually have a defined internal process with named steps — ask what the process is and where your request sits in it, rather than assuming.

**By situation/profile:**
- **You already phoned and were promised something:** Lead with a confirmation-of-what-was-said paragraph — date, channel, what was promised — then the ask. See `advocacy_channel_and_record_strategy.md`.
- **This is your second or third attempt:** Reference the prior letters by date and delivery proof; the pattern of non-response is itself part of the record.
- **Documentation is thin:** Flag gaps as `[NEED DOCUMENT:]` rather than asserting facts you cannot support. A short, checkable letter beats a long, unsupported one.
- **Legal or safety dimension:** Boundary & Routing Block first; do not send before routing.

---

## Related Prompts

- `advocacy_channel_and_record_strategy.md` — choose the channel and build a provable record from the start, including confirming a verbal exchange in writing.
- `advocacy_escalation_ladder_designer.md` — what to send at each rung if the first request goes unanswered.
- `advocacy_response_analyzer.md` — after they reply: what they actually committed to, and what they dodged.
- `../../domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md` — when the matter needs a professional or an authority rather than a letter.
- `../../domain-legal/client-intake-communications/legal_demand_letter_drafter.md` — the attorney-side demand-letter counterpart, for when a request is no longer the right instrument.
