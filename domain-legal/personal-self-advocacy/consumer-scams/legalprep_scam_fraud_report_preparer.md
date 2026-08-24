---
title: "Scam & Fraud Report Preparer — Draft Your Own Factual Report to the FTC, FBI IC3, Bank, or State AG"
category: legalprep
description: "Help someone who believes they were scammed or defrauded draft THEIR OWN factual, first-person report to submit to ReportFraud.ftc.gov, the FBI's ic3.gov, their bank or card issuer, and/or their state attorney general — what happened, amounts, dates, and the accounts and contacts involved. Emphasizes contacting the bank fast. Does NOT state that conduct was legally fraud, predict recovery, cite law, or file anything for the user — those route to an attorney or the agency. Not legal advice."
techniques:
  - DS-01
  - ST-02
  - ST-03
  - NE-25
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - scam
  - fraud
  - self-submit
  - ftc-report
  - reporting
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/consumer-scams/legalprep_consumer_complaint_documentation_organizer.md
  - domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md
  - domain-legal/client-intake-communications/legal_demand_letter_drafter.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Help you write **your own** clear, factual report about a scam or fraud so you can submit it yourself to the right places — the FTC at `ReportFraud.ftc.gov`, the FBI's Internet Crime Complaint Center at `ic3.gov`, your bank or card issuer's fraud team, and/or your state attorney general's consumer-protection office. The report captures what happened in plain sequence, how much money was involved, the dates, and every account, phone number, email, website, or person connected to it. This is **your own first-person account** to read, verify, and submit — it does **not** decide that what happened was legally "fraud," predict whether you will get your money back, cite law, or submit anything on your behalf.

**When to use:** You believe you were targeted by a scam or fraud — a fake seller, an imposter, a phishing message, a wire or gift-card scam, a romance or investment scam, a tech-support scam, an unauthorized charge — and you want a factual report ready to submit yourself to an agency and your bank.

**When NOT to use:** You want to know whether it "counts as fraud" legally, whether you can sue, or what you can recover → that is legal analysis; route it to an attorney or the agency. It is an ordinary quality/billing dispute with a real, known merchant → use `legalprep_consumer_complaint_documentation_organizer.md`. You want to dispute a specific card charge → use `legalprep_refund_chargeback_dispute_preparer.md`. **Money just left your account → Safety Block first: call your bank now.**

---

## Safety Block

**Act fast — reporting is important, but stopping the loss comes first:**
- **Money just moved, or you gave out card/bank/login details** → contact your bank or card issuer's fraud line **immediately** (number on the back of your card or their official site). Ask them to stop, reverse, or flag the transaction and to protect your account. Speed matters — many reversals have short windows.
- **You sent a wire, gift cards, crypto, or a payment-app transfer** → tell the bank / wire service / gift-card issuer / app **right away**; ask about recall or freeze options.
- **Report the scam:** FTC at `ReportFraud.ftc.gov`; online crimes to the FBI at `ic3.gov`; your **state attorney general's** consumer-protection office; general guidance at `usa.gov`.
- **Your identity or credentials may be exposed** → `IdentityTheft.gov` for an FTC recovery plan; change passwords; turn on two-factor authentication.
- **You are being threatened, coerced, or pressured to send more money** → local police; emergencies **911**. Do not send more; do not confront the contact.
- **You are in crisis** → `988 Suicide & Crisis Lifeline`.

This prompt is educational support for organizing your own report. It is not a substitute for legal, banking, or law-enforcement services.

---

## Scope Boundary — Read First

This **prepares your own factual report for you to submit** to a bank or a fraud-reporting agency. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney, your bank, or law enforcement.** It will **not** conclude that what happened meets the legal definition of fraud or any crime; predict whether you will recover money; assess how strong a claim is; cite or invent statutes or legal standards; identify or accuse a specific real person as the culprit; or submit the report for you. Whether conduct is legally fraud — and what can be recovered — **varies by state and country and changes over time** and is for an attorney or the agency. You will read, verify, and submit the report yourself; any certification the channel requires (e.g., an accuracy attestation) is **yours to make**, not something this prompt asserts for you.

---

## Core Principles

1. **Stop the bleeding before writing.** The single most valuable action is often the fastest: call the bank. Reporting is essential but secondary to freezing the loss.
2. **Tell it as a plain sequence.** A scam report is a story in order: first contact → what they asked → what you did → what happened → when you realized. Chronology is the backbone.
3. **Describe the conduct; don't legally label it.** "The caller said they were from my bank's fraud department and asked me to move money to a 'safe account'" — not "this was wire fraud." The facts are what agencies act on.
4. **Every identifier matters.** Phone numbers, emails, websites, usernames, wallet addresses, account numbers, names used, amounts, and timestamps — the more concrete identifiers, the more useful the report.
5. **Amounts and dates exact.** Each transfer, its date, amount, method, and destination, listed precisely. This is what the bank and agency need to trace and what determines deadlines.
6. **Report to more than one place.** The bank stops loss; the FTC and IC3 build the record and feed investigations; the state AG handles local consumer protection. Note each channel.
7. **You prepare and submit; the agency and bank assess.** You supply the facts; whether it is legally fraud, who did it, and what is recoverable is for professionals. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **What kind of scam/fraud you believe it was:** [in your own words]
- **How it started:** [call / text / email / social media / website / in person — date and channel]
- **What they asked you to do:** [pay / move money / give a code / install software / buy gift cards]
- **What you did and when:** [each action with date]
- **Money involved:** [each amount, date, method, and where it went]
- **Identifiers you have:** [phone #, email, website/URL, username, account/wallet #, names used]
- **Whether you have contacted your bank yet:** [yes/no — if no, Safety Block]
- **Documents you have:** [screenshots, messages, receipts, transfer confirmations, statements]
- **Any ongoing contact, threat, or pressure?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; build the report only from facts the user supplies.
- Put the "contact your bank now" step first whenever money moved or details were shared.
- Lay events in dated chronological order; log each money movement with amount, date, method, destination.
- Capture every identifier verbatim (numbers, emails, URLs, usernames, wallet/account numbers).
- Keep the account factual and first-person; strip legal labels and motive.
- Flag missing facts as `[NEED DATE:]` / `[NEED DOCUMENT:]` / `[NEED IDENTIFIER:]`.
- Name the channels to submit to (FTC ReportFraud, FBI IC3, bank, state AG) and route legal questions out.
- Present any certification the channel requires as **the user's own attestation to read and submit**.

**Must Not:**
- State a legal conclusion ("this is fraud / wire fraud / a crime under the law").
- Predict whether the user will recover money or assess how strong a claim is.
- Cite or invent statutes, elements of a crime, or legal standards.
- Name, identify, or accuse a specific real person as the perpetrator (record identifiers as facts, not accusations).
- Submit or file the report for the user, or assert an accuracy/penalty attestation on their behalf.
- Fill gaps in the sequence or amounts with assumption (flag `[NEED …:]`).
- Coach the user to inflate the loss or embellish the contact's statements.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for ongoing loss, threats, or pressure (route to Safety Block; if money moved and the bank has not been called, that is the first instruction). Restate the matter and jurisdiction. Confirm the boundary: this prepares the user's own report; whether it is legally fraud is for an attorney or the agency.

### Stage 2 — Build the Chronology
Walk the event from first contact to the moment the user realized something was wrong. Each step gets a date/time and a factual description of what was said and done. Flag gaps as `[NEED DATE:]`.

### Stage 3 — Itemize the Money
List every payment or transfer: amount, date, method (card, wire, app, gift card, crypto), and destination (account, wallet, recipient name as given). Total the loss factually. Flag anything uncertain.

### Stage 4 — Capture Identifiers
Record every identifier exactly as it appeared: phone numbers, emails, website URLs, social usernames, account/wallet numbers, and any names or titles the contact used. Record these as facts observed, not as accusations against a named real person.

### Stage 5 — Assemble the First-Person Report
Compose the user's own factual, first-person account in plain language, drawing only on Stages 2–4. Keep it neutral and specific. Insert `[NEED …:]` tokens for anything missing rather than guessing.

### Stage 6 — Route to the Channels and Close
List where to submit: the bank/card issuer (loss), `ReportFraud.ftc.gov`, `ic3.gov`, the state attorney general, and `IdentityTheft.gov` if credentials were exposed. Present any required accuracy attestation as the user's own to read and sign. Route "is this legally fraud / can I sue / what will I recover" to an attorney.

---

## Output Format

```markdown
MY OWN ACCOUNT — SCAM/FRAUD REPORT — NOT A LEGAL FILING
Prepared by [you], [date], for submission to: [bank] · ReportFraud.ftc.gov · ic3.gov · [state] AG.
This is my own factual account. It does NOT state that any law was broken, predict recovery,
or accuse a named person. Legal questions go to an attorney or the agency.

FIRST STEP (if not done): I have / have not yet contacted my bank/card issuer. [If not — do this first.]

## What happened (in order)
On [date/time], I was contacted by [call/text/email/site]. The contact [said/asked] [factual].
I [what I did] on [date]. Then [next step, date]. I realized something was wrong on [date] when [fact].
[NEED DATE: ...] where uncertain.

## Money involved
| Date | Amount | Method | Sent to (as given) |
|---|---|---|---|
| [YYYY-MM-DD] | [$X] | [wire / card / app / gift card / crypto] | [account / wallet / recipient name given] |
Total I believe I lost: [$X] [or NEED DOCUMENT: confirm from statements]

## Identifiers connected to the contact (facts, not accusations)
- Phone number(s): [as shown]
- Email(s): [as shown]
- Website / URL(s): [as shown]
- Username / handle(s): [as shown]
- Account / wallet number(s): [as shown]
- Name(s) or title(s) the contact used: [as given — recorded as stated to me, not verified]

## Documents I am attaching
- [Screenshots of messages, dated]
- [Transfer/receipt confirmations]
- [Bank/card statement lines showing the transactions]
- [NEED DOCUMENT: ...]

## What I am asking of each channel
- Bank/card issuer: stop/reverse/flag the transactions; protect my account.
- FTC / FBI IC3 / state AG: record this report for investigation and consumer protection.

---
Attestation (mine to read and submit myself): The reporting site may ask me to confirm the
information is true and accurate to the best of my knowledge. I will read that statement,
verify every fact above, and submit it myself.
For an attorney: please advise whether this is legally actionable and what I may recover.
*Confirm with counsel or the relevant agency for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal questions routed *confirm with counsel/agency*?
- [ ] "Contact your bank now" placed first whenever money moved or details were shared?
- [ ] Events laid in dated order; gaps flagged `[NEED DATE:]`?
- [ ] Every money movement itemized with amount, date, method, destination?
- [ ] Identifiers captured verbatim and recorded as facts, not accusations of a named person?
- [ ] Account written first-person, factual, neutral — no legal labels, no motive?
- [ ] No conclusion that conduct was legally "fraud" or a crime?
- [ ] No prediction of recovery or assessment of claim strength?
- [ ] Submission channels listed (bank, FTC ReportFraud, FBI IC3, state AG)?
- [ ] Any required attestation presented as the user's own to read and submit?
- [ ] Any ongoing threat, pressure, or crisis screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This was wire fraud, a federal crime" | "I moved $X by wire to the account they gave me on [date]" — the label is for the agency |
| "You'll get your money back once you report" | Report and call the bank; recovery is not promised — route to the bank/attorney |
| Name and accuse a specific real person as the scammer | Record the identifiers and names *as given to you*, marked unverified |
| Sign the accuracy/penalty attestation for the user | Present it as the user's own to read, verify, and submit |
| "Cite the federal wire-fraud statute" | Do not cite law; route legality to an attorney or the agency |
| Guess at a total loss you can't confirm | List the amounts you have; flag `[NEED DOCUMENT: statement]` |
| Write the report and submit it yourself | Prepare the report; the user reviews and submits it |
| Treat active pressure to pay more as routine | Stop, Safety Block, do not pay, contact police/911 if threatened |

---

## Adaptations

**By scam type:**
- **Imposter (bank / government / tech support):** Center the record on who they claimed to be, what they asked, and the channel; note that legitimate agencies do not demand gift cards or "safe-account" transfers (stated as general awareness, not legal advice).
- **Romance / investment scam:** Capture the platform, the contact's handles, every transfer, and the timeline of contact; these often involve crypto — record wallet addresses exactly.
- **Phishing / account takeover:** Emphasize `IdentityTheft.gov`, password changes, and two-factor; list which accounts were accessed and when.
- **Marketplace / fake seller:** Overlaps a consumer dispute — pair with `legalprep_consumer_complaint_documentation_organizer.md` and dispute the charge via `legalprep_refund_chargeback_dispute_preparer.md`.
- **Gift-card / wire / payment-app:** The itemized money table and immediate contact of the issuer/app are the priority.

**By situation/profile:**
- **Ongoing contact or threats:** Safety Block first; do not respond; preserve messages; involve police.
- **Elderly or vulnerable person:** Route to the state AG and consider adult-protective resources; keep the account factual and non-blaming.
- **Business / employer funds affected:** Note that the employer's own reporting and legal channels apply; route to the appropriate internal contact and counsel.

---

## Related Prompts

- `legalprep_consumer_complaint_documentation_organizer.md` — for organizing the underlying transaction facts before or alongside the report.
- `legalprep_refund_chargeback_dispute_preparer.md` — to dispute the specific charge(s) with your card issuer or merchant.
- `../../client-intake-communications/legal_demand_letter_drafter.md` — the attorney-side demand-letter counterpart if you pursue recovery through counsel.
- `../../litigation/legal_complaint_drafter.md` — the attorney-side pleading counterpart if the matter proceeds to court.
