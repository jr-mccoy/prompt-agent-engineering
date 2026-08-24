---
title: "Marketing Opt-Out & Do-Not-Sell Request — Stop the Contact and the Sharing"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN written request to stop marketing contact and to stop personal data being sold or shared for advertising — covering every channel and identifier, suppression rather than deletion of the contact record, affiliates and partners, and written confirmation. Does NOT cite marketing, telemarketing, or privacy statutes as authority, state which law applies or what timescale is required, predict compliance, or invent registry names or contact addresses. Not legal advice."
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
  - marketing
  - opt-out
  - self-submit
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/privacy-and-data/advocacy_data_deletion_request.md
  - domain-written-advocacy/privacy-and-data/advocacy_data_broker_removal_request.md
  - domain-written-advocacy/privacy-and-data/advocacy_privacy_request_escalation.md
  - domain-written-advocacy/privacy-and-data/advocacy_data_access_request.md
---

**Purpose:** Help you write **your own** dated request that an organization stop contacting you for marketing and stop selling or sharing your personal data for advertising. It covers every channel they might use, every identifier they might hold you under, the affiliates and partners they may have passed you to, and asks for written confirmation — including the point most opt-outs miss: that they suppress your contact details rather than delete them, so you are not simply re-added from the next data purchase.

**When to use:** You want the marketing to stop, or you want to stop your data being sold or shared for advertising, and you want a dated record of having asked.

**When NOT to use:** You want all your data erased → `advocacy_data_deletion_request.md`. You want your listing off a people-search site → `advocacy_data_broker_removal_request.md`. You want to know what they hold and who they shared it with → `advocacy_data_access_request.md` first. The contact is a debt collector → `domain-legal/personal-self-advocacy/debt-collection/`, which is a different request with different consequences. The contact is harassment or from someone dangerous → `domain-legal/personal-self-advocacy/harassment-stalking/`.

---

## Boundary & Routing Block

Use a different pathway if:
- **The contact is from a debt collector about a debt** → that is not marketing, and asking a collector to stop contacting you can have consequences for the account. See `domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md` and route to an attorney or **legal aid**.
- **The contact is threatening, obsessive, or from someone who has targeted you personally** → this is not a marketing matter. See `domain-legal/personal-self-advocacy/harassment-stalking/`, and if you are in immediate danger contact emergency services.
- **You suspect the contact is a scam or phishing attempt** → do not reply, do not confirm your identifiers, and do not use any unsubscribe link in the message. Replying confirms your details are live. See `domain-legal/personal-self-advocacy/consumer-scams/` and report through official channels.
- **The organization is one you have an account with and the messages are service or transactional notices** → opting out of marketing may not stop those, and stopping them may not be in your interest. Ask them to distinguish the two rather than requesting a blanket stop.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal services.

---

## Scope Boundary — Read First

This **drafts your own written marketing opt-out and do-not-sell request for you to send**. It is **not legal advice, legal strategy, a legal filing, a regulatory complaint, or a substitute for an attorney, a regulator, or your jurisdiction's law.** It will **not** tell you which marketing, telemarketing, email, or privacy law applies to you or the organization; cite, quote, or number any statute, regulation, or rule as authority; state the timescale in which marketing must stop; tell you whether an exemption applies or whether continued contact would be unlawful; state that any registry or preference service exists or supply its name or address from memory; predict whether the organization will comply; assess how strong your request is; or invent a privacy contact, unsubscribe address, or partner name. Marketing and data-sharing rules **vary by channel, state, country, and sector and change over time.** Any registry or legal instrument named in your letter must be one **you** have verified exists and applies.

---

## Core Principles

1. **Name every channel explicitly.** Email, SMS, phone, post, push notification, in-app message, and advertising shown to you on other platforms. An opt-out that says "marketing" is routinely read as "email only."
2. **Name every identifier they may hold you under.** Old email addresses, previous surnames, former addresses, second phone numbers. Organizations suppress by identifier, so an unnamed identifier keeps receiving.
3. **Ask for suppression, not deletion, of the contact record.** This is the counter-intuitive part. If they delete you entirely, nothing stops them re-adding you when they next buy a list. A suppression record is what keeps you off it. Ask explicitly for suppression.
4. **Separate marketing from service messages.** You may still want transactional notices — billing, security, service outages. Say which you want to keep, or a blanket request can switch off things you need.
5. **Address the sharing, not just the sending.** Stopping their emails does nothing about your data being sold or shared for advertising. Those are two distinct asks and both need stating.
6. **Chase the source, not just the symptom.** Ask where they obtained your details and which partners they passed them to. That is what lets you stop the next three organizations rather than this one.
7. **You request and record; the professional assesses continued contact.** Whether ongoing marketing after a request breaches anything is for an attorney or a regulator. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country of residence):** [required]
- **Organization:** [name]
- **Their designated privacy or preferences channel:** [from their privacy policy] or [NEED CHANNEL: locate it]
- **All identifiers they may hold you under:** [current and former emails, phone numbers, postal addresses, name variants, account #]
- **Channels you are receiving contact on:** [email / SMS / phone / post / push / in-app / ads elsewhere]
- **What you want to stop:** [all marketing / named channels only]
- **Service messages you want to keep:** [billing, security, outage notices] or ["none — stop everything"]
- **Do you also want to stop data being sold or shared for advertising?:** [yes/no]
- **Where you think they got your details:** [if known]
- **Prior opt-out attempts:** [date, method, whether contact continued]
- **Any debt collection, harassment, or suspected scam dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Screen for debt collection, harassment, and suspected scams before drafting.
- Enumerate every channel and every identifier the user supplies, and prompt for former ones.
- Ask explicitly for **suppression** of the contact record rather than deletion, and explain why in the letter.
- Separate marketing from service and transactional messages, recording which the user wants to keep.
- State the do-not-sell/do-not-share ask separately from the do-not-contact ask, where the user wants it.
- Ask where the organization obtained the user's details and which partners it shared them with.
- Record prior opt-out attempts with dates and methods.
- Include a Sending Log and label the output `MY OWN REQUEST — NOT A LEGAL FILING`.

**Must Not:**
- State which marketing, telemarketing, email, or privacy law applies to the user or the organization.
- Cite, quote, paraphrase, or number any statute, regulation, or rule.
- State a timescale in which marketing must stop, or that any deadline exists.
- State whether continued contact would be unlawful, or whether an exemption applies.
- Name a preference service, do-not-call registry, or opt-out scheme, or supply its address, from memory.
- Predict whether the organization will comply, or how completely.
- Supply a privacy contact, unsubscribe address, or partner name from memory.
- Advise clicking an unsubscribe link in a message the user believes may be a scam.
- Draft a legal threat, or a regulatory complaint as part of the request.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for debt-collection contact, harassment, or a suspected scam or phishing message → route per the Boundary & Routing Block. Where a scam is suspected, instruct the user not to reply or click any link in it. Restate the jurisdiction and the boundary: this drafts a request; lawfulness is for an attorney or a regulator.

### Stage 2 — Inventory Channels and Identifiers
List every channel the user is being contacted on and every identifier the organization may hold them under, prompting specifically for former email addresses, previous surnames, old postal addresses, and secondary phone numbers. Missing identifiers are the most common reason an opt-out only half works.

### Stage 3 — Separate Marketing From Service Messages
Establish which messages the user wants to keep — billing, security, service, delivery — and which to stop. Record this explicitly so a blanket request does not switch off something they need.

### Stage 4 — Add the Suppression and Sharing Asks
Frame the core request as suppression of the contact record rather than deletion, and say why in the letter itself. Where the user wants it, add the separate request to stop selling or sharing personal data for advertising, including with affiliates and partners.

### Stage 5 — Trace the Source and Recipients
Add requests that the organization state where it obtained the user's details and which third parties it has shared them with, and that it pass the opt-out on to those recipients. Record any prior opt-out attempts with dates, methods, and whether contact continued.

### Stage 6 — Draft the Request and Close
Compose the user's own dated request, labeled as theirs to send, with the Sending Log and a follow-up check date. Point to the escalation prompt if contact continues, and to the data-broker prompt if the source turns out to be a broker. Route lawfulness questions to an attorney or a regulator.

---

## Output Format

```markdown
MY OWN MARKETING OPT-OUT REQUEST — NOT A LEGAL FILING
From: [your name], [contact]. To: [organization, designated privacy/preferences channel].
Date: [YYYY-MM-DD]. Delivery: [privacy email / web form / certified mail]. Keep a copy.
This is my own request. It does NOT state which law applies to you or to me, cite any statute,
assert a timescale, state that continued contact would be unlawful, or predict your response.

Re: Marketing opt-out and do-not-sell/share request — [account / identifiers]

## Identifiers you may hold me under
Please apply this request to **all** of the following, not only the one this message came from:
- Name: [name] · Also held as: [former surnames / name variants]
- Email addresses: [current] · [former addresses]
- Phone numbers: [mobile] · [landline] · [former numbers]
- Postal addresses: [current] · [former addresses]
- Account number(s): [#] or [NEED ACCOUNT #:]

## What I am asking you to stop
Please stop contacting me for marketing purposes on **every** channel, including:
- [ ] Email   - [ ] SMS / text   - [ ] Telephone   - [ ] Post
- [ ] Push notifications   - [ ] In-app messages   - [ ] Targeted advertising shown to me elsewhere

## Messages I am NOT asking you to stop
[e.g. billing statements, payment reminders, security alerts, service outage notices,
delivery updates] / [None — please stop all contact.]

## Please suppress, rather than delete, my contact record
So that this request continues to be effective, please add my details to your **suppression
list** rather than deleting them. I understand that deleting my record entirely may allow my
details to be re-added if you later obtain them from another source.

[If the user also wants a full deletion, note that it is a separate request and reference it.]

## Do not sell or share my personal data for advertising
[If requested:]
Please also stop selling, sharing, or otherwise disclosing my personal data to third parties
for advertising or marketing purposes, and apply this to your affiliates and partners.

## Please also tell me
1. Where you obtained my details.
2. Which third parties, affiliates, or partners you have shared them with.
3. That you have passed this opt-out request on to those recipients.

## Prior requests
- [YYYY-MM-DD] — I opted out via [method]. Contact continued on [YYYY-MM-DD] via [channel].

## What I am asking you to confirm in writing
1. That all listed identifiers have been suppressed across all listed channels.
2. That my data is no longer sold or shared for advertising.
3. The recipients you have notified.

Please respond in writing to [your contact] by [date you are requesting].

[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response requested by | Contact stopped? |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [channel] | [#] | [screenshot / receipt] | [YYYY-MM-DD] | [ ] |

Check again on [YYYY-MM-DD] and log any contact received after this request, with date and channel.

Note to self: this is my own request, not legal advice or a filing. Which law applies, what
timescale (if any) applies, and whether continued contact would breach anything are questions for
an attorney or a regulator. If a preference service or registry exists for my jurisdiction, I
will find it from an official source rather than relying on a name I have been given.
*Verify for your jurisdiction — marketing and data-sharing rules vary by channel, state, and country.*
```

---

## Verification

- [ ] Jurisdiction captured; debt-collection, harassment, and scam dimensions screened and routed?
- [ ] Every channel enumerated, including push, in-app, and targeted advertising elsewhere?
- [ ] Every identifier listed, with former emails, names, addresses, and numbers prompted for?
- [ ] Suppression requested rather than deletion, with the reason stated in the letter?
- [ ] Marketing separated from service and transactional messages the user wants to keep?
- [ ] Do-not-sell/share stated as a separate ask where the user wanted it?
- [ ] Source and recipients requested, with a request to pass the opt-out on?
- [ ] Prior opt-out attempts recorded with dates and methods?
- [ ] **No statute, regulation, or rule cited, quoted, or numbered?**
- [ ] No statement of which law applies, or that continued contact would be unlawful?
- [ ] No timescale or deadline asserted?
- [ ] No preference service, registry, or opt-out scheme named or addressed from memory?
- [ ] No compliance prediction or strength assessment?
- [ ] No advice to click an unsubscribe link in a suspected scam message?
- [ ] Sending Log with a follow-up check date included, and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Under CAN-SPAM they must honour this within 10 business days" | Cite nothing and state no timescale; request a date of your own |
| "Register with the national Do Not Call list at [address]" | Name no registry from memory; *verify whether one exists for your jurisdiction from an official source* |
| "Continued contact after this is illegal" | State nothing about lawfulness; route continued contact to an attorney or a regulator |
| "Ask them to delete your record so they stop contacting you" | Ask for **suppression** — deletion can let you be re-added from a purchased list |
| "Opt out of marketing" with no channel list | Enumerate every channel; "marketing" is read as "email" |
| Apply the request only to the email that received the message | List every identifier, including former addresses and names |
| "Just click unsubscribe" on a message the user thinks is a scam | Do not reply or click; replying confirms the details are live |
| Stop all contact including billing and security alerts | Separate marketing from service messages the user needs |
| Treat collector contact as marketing to opt out of | Stop, use the Boundary & Routing Block, route to debt-collection prompts |
| "They'll stop within a month" | Make no prediction about compliance or timing |

---

## Adaptations

**By channel:**
- **Postal marketing:** Often driven by purchased lists — the source question matters most here, and a broker may be behind it. See `advocacy_data_broker_removal_request.md`.
- **Phone and SMS:** List every number including former ones; note the dates and times of calls received after the request, as that log is what an escalation rests on.
- **Targeted advertising elsewhere:** This is usually driven by sharing rather than sending — the do-not-sell/share ask is the relevant one, not the contact opt-out.
- **In-app and push:** Frequently controlled by in-app settings *and* a back-end profile; do both and say in the letter that you have changed the in-app settings.

**By situation/profile:**
- **Contact continues after opting out:** Log every message with date, channel, and identifier used; that log is the substance of the escalation.
- **You never gave them your details:** Make the source question the centre of the request; the answer tells you which broker or partner to write to next.
- **Also want everything deleted:** Send the deletion request separately, but keep the suppression request — explain in both letters that you want suppression retained.
- **Debt, harassment, or scam dimension:** Boundary & Routing Block first; do not treat any of these as marketing.

---

## Related Prompts

- `advocacy_data_broker_removal_request.md` — if the source turns out to be a data broker or people-search site.
- `advocacy_data_access_request.md` — to find out where they got your details and who they shared them with.
- `advocacy_data_deletion_request.md` — if you want everything erased rather than the contact stopped.
- `advocacy_privacy_request_escalation.md` — if contact continues after the request.
