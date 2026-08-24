---
title: "Data Deletion Request — Ask an Organization to Erase Your Personal Data"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN written request that an organization delete the personal data it holds about them — identifying themselves to the required standard, scoping what is covered, naming any processors or third parties data was shared with, and asking for written confirmation of what was deleted and what was retained and why. Does NOT cite GDPR articles, CCPA sections, or any privacy statute as authority, state which law applies to the user, assert deadlines or exemptions, predict compliance, or invent a privacy contact address. Not legal advice."
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
  - data-deletion
  - self-submit
  - consumer
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/privacy-and-data/advocacy_data_access_request.md
  - domain-written-advocacy/privacy-and-data/advocacy_privacy_request_escalation.md
  - domain-written-advocacy/privacy-and-data/advocacy_data_broker_removal_request.md
  - domain-written-advocacy/accounts-and-billing/advocacy_account_closure_request.md
---

**Purpose:** Help you write **your own** dated request that an organization delete the personal data it holds about you. It works out how to identify yourself to the standard they will require, scopes what you are asking to be deleted, names the processors and third parties you know they shared data with, and asks for written confirmation of what was actually deleted — and what was kept, and on what stated basis.

**When to use:** You want an organization to erase your personal data, whether or not you are also closing an account, and you want the request and its response documented.

**When NOT to use:** You want to see what they hold before deciding → `advocacy_data_access_request.md` first; it is usually the stronger opening move. You want to stop marketing rather than delete everything → `advocacy_marketing_optout_do_not_sell_request.md`. You want your details removed from a people-search or data-broker site → `advocacy_data_broker_removal_request.md`. You want the account closed → `../accounts-and-billing/advocacy_account_closure_request.md` (send both; they are different requests). They ignored or refused a privacy request → `advocacy_privacy_request_escalation.md`.

---

## Boundary & Routing Block

Use a different pathway if:
- **You need the data as evidence in a dispute, claim, or legal matter** → **do not ask for it to be deleted.** Deletion can destroy evidence you may need, and in some circumstances requesting it during a dispute can itself cause problems. Request access instead (`advocacy_data_access_request.md`) and route to an attorney or **legal aid** before deleting anything.
- **The data concerns a matter with a safety dimension** — an abuser, a stalker, someone subject to a protective order, or an active harassment matter → deletion may remove records you need, and some removals can notify the other party. Route to `domain-legal/personal-self-advocacy/harassment-stalking/` and an advocate or attorney first.
- **You are asking on behalf of a child, a person you care for, or someone who has died** → authority to make the request is a legal question with a specific evidence requirement. Route to the organization's designated process and to an attorney.
- **The organization is a credit bureau, and the issue is inaccurate information** → deletion is the wrong instrument; that is a dispute. See `../financial-hardship/advocacy_credit_report_dispute.md`, and for fraud `domain-legal/personal-self-advocacy/identity-theft/`.
- **The data is intimate imagery shared without your consent** → there are dedicated removal pathways that work faster than a general deletion request. `[VERIFY: locate the current dedicated reporting service and the platform's own process from official sources.]`

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal services.

---

## Scope Boundary — Read First

This **drafts your own written deletion request for you to send**. It is **not legal advice, legal strategy, a legal filing, a regulatory complaint, or a substitute for an attorney, a data protection authority, or your jurisdiction's law.** It will **not** tell you which privacy law applies to you or to the organization; cite or quote GDPR articles, CCPA or CPRA sections, or any other privacy statute, regulation, or recital as authority; state the deadline an organization has to respond; tell you which exemptions it may rely on or whether a refusal is valid; tell you whether the organization is even covered by any privacy law; predict whether it will comply; assess how strong your request is; or invent a privacy contact address, data protection officer name, or web form URL. Privacy rights, who holds them, who must honour them, and on what timescale **vary enormously by state, country, sector, and the organization's own circumstances, and change over time.** Every legal instrument named in your letter must be one **you** have verified applies to you.

---

## Core Principles

1. **Ask access first if you are unsure what they hold.** A deletion request is blunt. An access request tells you what exists, where it came from, and who it went to — which makes any subsequent deletion request precise and much harder to answer vaguely.
2. **Identify yourself to the standard they will require, and no further.** Organizations must be able to match you to a record and will refuse otherwise. Provide account identifiers and the identity evidence their published process asks for — but do not volunteer a passport scan or full identity documents to an unverified email address.
3. **Scope the request explicitly.** All personal data, or a defined category — marketing profile, call recordings, location history, biometric or inferred data, a specific account. A scoped request is answered; an unscoped one is often narrowed by the recipient without telling you.
4. **Ask about onward recipients.** Data shared with processors, advertising partners, analytics providers, or affiliates is frequently the part that survives. Ask them to identify recipients and to pass the deletion request on.
5. **Expect retention, and ask them to explain it.** Organizations commonly retain some data — this is normal. What matters is that they state **what** they kept and **why**, in writing. Do not assert in advance that no retention is permitted; ask them to specify.
6. **Name a legal basis only if you have verified it applies to you.** This prompt will not tell you which law covers you. If you have confirmed one applies, you may cite it in your own words as *your* stated basis. Otherwise ask under the organization's own privacy policy, which is always available to you.
7. **You request and record; the professional assesses the response.** Whether a refusal or an exemption is valid is for an attorney or the relevant data protection authority. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country of residence):** [required — determines which rights may exist]
- **Where the organization operates or is established, if known:** [may differ from yours]
- **Organization:** [name]
- **Their designated privacy channel:** [privacy email / web form / postal address from their privacy policy] or [NEED CHANNEL: locate it in their privacy policy]
- **Your identifiers with them:** [account #, registered email, username, phone, name variants used]
- **Identity evidence their process asks for:** [what their published process requires] or ["unknown"]
- **Scope of deletion requested:** [all personal data / named categories]
- **Categories you specifically want covered:** [marketing profile, call recordings, location, biometric, inferred/derived data, backups]
- **Third parties you know they shared with:** [names, if any]
- **Whether you have an open account with them:** [yes/no — and whether you are closing it]
- **Any legal basis you have personally verified applies to you:** [named, or "none — asking under their privacy policy"]
- **Any dispute, evidence, safety, or third-party dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Screen for evidence, dispute, and safety dimensions before drafting, and route deletion away where data may be needed.
- Recommend an access request first where the user does not know what is held.
- Direct the user to the organization's designated privacy channel from its own privacy policy, flagging `[NEED CHANNEL:]` if unknown.
- Provide identifiers sufficient for matching, while cautioning against over-disclosing identity documents.
- State the deletion scope explicitly, by category where the user has named categories.
- Ask the organization to identify onward recipients and pass the request on.
- Ask it to state what was deleted, what was retained, and its stated reason for retention.
- Cite a legal basis **only** where the user says they have personally verified it applies, and render it as the user's own stated basis.
- Include a Sending Log and label the output `MY OWN REQUEST — NOT A LEGAL FILING`.

**Must Not:**
- State which privacy law applies to the user or the organization.
- Cite, quote, paraphrase, or number any GDPR article, CCPA/CPRA section, or other privacy statute, regulation, or recital.
- State a response deadline, or that one exists.
- State which exemptions apply, or whether a refusal or a retention is valid.
- Assert that the organization must comply, or is covered by any law.
- Predict whether the organization will comply, or how long it will take.
- Supply a privacy contact address, DPO name, or web form URL from memory.
- Advise sending identity documents to an unverified address.
- Recommend deletion where the user may need the data as evidence.
- Draft a legal threat, or a regulatory complaint as part of the request.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for an active dispute or claim where the data may be evidence, a safety dimension, a request on behalf of another person, a credit-bureau accuracy issue, or intimate imagery → route per the Boundary & Routing Block **before** drafting. Restate the jurisdiction and the boundary: this drafts a request; which law applies is for the user to verify or an attorney to advise.

### Stage 2 — Consider Access First
Where the user does not know what the organization holds, recommend an access request as the opening move and explain why: it identifies categories, sources, and recipients, which turns a vague deletion request into a specific one. Proceed to deletion only if the user still wants it now.

### Stage 3 — Locate the Channel and Set the Identity Position
Direct the user to the organization's privacy policy for its designated privacy channel; flag `[NEED CHANNEL:]` if unknown. Establish which identifiers to supply for matching, and what identity evidence their published process requires — cautioning against volunteering full identity documents unprompted or to an unverified address.

### Stage 4 — Scope the Request
Define what is being asked for: all personal data, or named categories. Prompt for commonly-overlooked categories — marketing and advertising profiles, call recordings, location history, biometric or inferred data, and data held in backups. Record which the user wants covered.

### Stage 5 — Address Onward Recipients and Retention
Add a request that the organization identify who it shared the data with and pass the deletion request to them. Add a request that it state, in writing, what it deleted, what it retained, and its stated reason for each retention — without asserting in advance what it may or may not keep.

### Stage 6 — Draft the Request and Close
Compose the user's own dated request, labeled as theirs to send, with the Sending Log. Where the user has verified a legal basis, render it as their own stated basis in their own words; otherwise ask under the organization's privacy policy. Point to the escalation prompt if ignored or refused. Route validity questions to an attorney or the relevant authority.

---

## Output Format

```markdown
MY OWN DATA DELETION REQUEST — NOT A LEGAL FILING
From: [your name], [contact]. To: [organization, designated privacy channel]. Date: [YYYY-MM-DD].
Delivery: [privacy email / web form / certified mail]. Keep a copy and any reference number.
This is my own request. It does NOT state which law applies to you or to me, cite any statute or
article, assert a deadline or an exemption, or predict your response. I have not taken legal
advice in preparing it.

Re: Request for deletion of my personal data — [account / identifier]

## Who I am
- Name: [name] (also held as: [name variants], if any)
- Registered email / username: [identifiers]
- Account number: [#] or [NEED ACCOUNT #:]
- Other identifiers you may hold me under: [phone / customer ref / address]

I am the individual the data relates to. If you need further verification to match me to your
records, please tell me specifically what you require and through which secure channel, and I
will provide it. I am not attaching identity documents to this message.

## What I am asking you to do
Please delete the personal data you hold about me.

Scope: [all personal data you hold about me] / [the following categories:]
- [ ] Account and profile data
- [ ] Marketing and advertising profiles, including inferred or derived attributes
- [ ] Call recordings and support transcripts
- [ ] Location history
- [ ] Biometric data
- [ ] Data held in backups and archives
- [ ] [other category]

## Basis for my request
[If the user has personally verified a law applies:]
I am making this request under [law the user has verified], which I understand applies to me
as a resident of [jurisdiction].

[If not:]
I am making this request under your published privacy policy and your own stated process for
deletion requests.

## Onward recipients
Please also:
1. Tell me which processors, affiliates, advertising or analytics partners, and other third
   parties you have shared my personal data with.
2. Pass this deletion request on to them, and tell me that you have done so.

## What I am asking you to confirm in writing
1. What personal data you deleted, by category, and the date of deletion.
2. What personal data you have retained, by category.
3. Your stated reason for retaining each category.
4. The recipients you notified.

Please respond in writing to [your contact] by [date you are requesting].

[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response requested by | Response received |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [channel] | [#] | [screenshot / receipt] | [YYYY-MM-DD] | [ ] |

Note to self: this is my own request, not legal advice or a filing. Which privacy law applies to
me, what deadline (if any) applies, whether any exemption or retention they claim is valid, and
whether they are covered at all are questions for an attorney or my data protection authority —
not for this letter. The date above is the date **I** requested, not a legal deadline.
*Verify for your jurisdiction — privacy rights vary by state, country, and sector, and change over time.*
```

---

## Verification

- [ ] Jurisdiction captured; evidence, dispute, safety, and third-party dimensions screened and routed?
- [ ] Access request recommended first where the user does not know what is held?
- [ ] Designated privacy channel taken from their privacy policy, or flagged `[NEED CHANNEL:]`?
- [ ] Identifiers sufficient for matching, with over-disclosure of identity documents cautioned against?
- [ ] Deletion scope stated explicitly, with overlooked categories prompted?
- [ ] Onward recipients addressed, with a request to pass the deletion on?
- [ ] Confirmation requested of what was deleted, what retained, and the stated reason?
- [ ] **No GDPR article, CCPA/CPRA section, or any privacy statute cited, quoted, numbered, or paraphrased?**
- [ ] No statement of which law applies to the user or the organization?
- [ ] No response deadline asserted, and the requested date labeled as the user's own?
- [ ] No statement about exemptions, or whether a refusal or retention would be valid?
- [ ] No prediction of compliance or timing, and no strength assessment?
- [ ] No privacy contact address, DPO name, or form URL supplied from memory?
- [ ] Legal basis included only where the user verified it, rendered as their own stated basis?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Under GDPR Article 17 you have the right to erasure" | Cite nothing; if the user verified a law applies, render it as *their* stated basis in their own words |
| "They have 30 days to respond under CCPA" | State no deadline; the date in the letter is the one the user is requesting |
| "They can't refuse — no exemption applies here" | Ask them to state what they retained and why; validity is for an attorney or the authority |
| "Send it to privacy@[company].com" | `[NEED CHANNEL: locate the designated privacy channel in their privacy policy]` |
| "You're covered because you live in California" | Do not determine coverage; the user verifies which law applies to them |
| "Attach a scan of your passport so they can verify you" | Ask them what they require and through which secure channel; do not volunteer documents |
| "Delete everything" with no scope | Scope by category, or the recipient narrows it silently |
| Recommend deletion while a dispute is live | Stop — deletion can destroy evidence; request access and route to an attorney |
| "They'll have to comply within a month" | Make no prediction about compliance or timing |
| Treat a credit-report inaccuracy as a deletion request | Route to the credit-report dispute prompt; deletion is the wrong instrument |

---

## Adaptations

**By organization type:**
- **Online platform or app:** Ask specifically about data held by the platform versus by advertisers and analytics partners, and whether deletion of the account is the same as deletion of the data — they are frequently not.
- **Retailer or marketplace:** Ask about order history, saved payment methods, marketing profiles, and any data passed to sellers or delivery partners.
- **Employer or former employer:** Employment records are commonly retained for stated reasons; ask what is retained and why rather than asserting it must go. Route employment-law questions to an attorney.
- **Healthcare or financial provider:** Retention is common in these sectors; ask them to state what they keep and why. Do not assert what they may or may not retain.

**By situation/profile:**
- **Also closing the account:** Send both letters, reference each in the other, and track them separately — different teams handle them.
- **You do not know what they hold:** Send the access request first; the deletion request afterwards can then name specific categories.
- **Data shared widely with partners:** Make the onward-recipient question the centre of the request; that is usually where data survives.
- **Evidence, dispute, or safety dimension:** Boundary & Routing Block first; do not delete what you may need.

---

## Related Prompts

- `advocacy_data_access_request.md` — find out what they hold before asking for deletion.
- `advocacy_privacy_request_escalation.md` — if the request is ignored, refused, or only partly answered.
- `advocacy_data_broker_removal_request.md` — for people-search sites and data brokers specifically.
- `advocacy_marketing_optout_do_not_sell_request.md` — if you want the marketing stopped rather than everything deleted.
- `../accounts-and-billing/advocacy_account_closure_request.md` — closing the account, which is a separate request.
