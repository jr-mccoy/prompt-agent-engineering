---
title: "Debt Validation & Dispute Letter Preparer (Draft Your Own Letter to a Collector)"
category: legalprep
description: "Help someone contacted by a debt collector draft their own factual letter identifying the account, requesting validation of the debt and/or disputing it, and asking for communication in writing. Notes that a validation/dispute process exists and that legal questions (is the debt valid? is it time-barred?) route to legal aid or an attorney. Organizes the user's own letter only. Does NOT assert legal rights as conclusions, cite the statute as advice, or predict the result. Not legal advice."
techniques:
  - DS-01
  - ST-03
  - CM-01
  - NE-25
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - debt-collection
  - consumer
  - validation
  - dispute
  - fdcpa
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/debt-collection/legalprep_collection_harassment_documentation_log.md
  - domain-legal/personal-self-advocacy/identity-theft/legalprep_fraud_dispute_narrative_preparer.md
  - domain-legal/family-self-advocacy/legalprep_attorney_consultation_question_builder.md
  - domain-legal/family-self-advocacy/legalprep_communication_record_compiler.md
---

**Purpose:** Help you draft your own factual letter to a debt collector that (1) identifies the account they are contacting you about, (2) requests validation of the debt and/or disputes it, and (3) asks that further communication be in writing. A validation/dispute process exists in consumer debt-collection practice, and this helps you use it in your own words. This prepares **your own letter** — it does **not** tell you whether the debt is valid, whether it is time-barred, whether the collector broke the law, or what will happen next.

**When to use:** A collector has contacted you about a debt and you want to ask them to prove it is yours and owed in the stated amount, or to dispute it, and to move the conversation to writing — soon after contact, so any short response window is not missed.

**When NOT to use:** You want to know whether you actually owe the debt, whether it is past the statute of limitations, whether to pay, settle, or whether the collector's conduct was unlawful → those are legal questions; route them to legal aid or an attorney. You are being sued over the debt → that is a court matter; route to legal aid/an attorney and see `domain-legal/litigation/legal_complaint_drafter.md` (attorney-side) for context. The debt is fraudulent from identity theft → pair with `../identity-theft/legalprep_fraud_dispute_narrative_preparer.md`. The collector's contact feels harassing → also use `legalprep_collection_harassment_documentation_log.md`.

---

## Safety Block

Stop and use the right pathway if:
- You are being threatened with harm, or the collector's contact is tied to a stalker or abuser → 911 (emergency, US); National Domestic Violence Hotline 1-800-799-7233. Do not confront anyone.
- The financial stress has you in crisis → 988 Suicide & Crisis Lifeline (US).

**Where to take questions and complaints (official channels):**
- The **Consumer Financial Protection Bureau (CFPB)** complaint site and your **state attorney general's** consumer-protection office — for complaints about a collector.
- Your **courthouse self-help center / legal aid** office or **state/local bar association** lawyer-referral service — for legal questions (validity, statute of limitations, a lawsuit).
- If the debt is fraudulent: **IdentityTheft.gov** (FTC).

This prompt is educational support for organizing your own correspondence. It is not a substitute for legal or financial services.

---

## Scope Boundary — Read First

This **drafts your own factual validation/dispute letter.** It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** decide whether the debt is valid or owed, whether it is time-barred, whether the collector violated the law, or predict what the collector will do. It will **not** cite or interpret the debt-collection statute as advice. Consumer debt-collection rights, response windows, and limitation periods **vary by state and country and change over time.** The letter references that a validation/dispute process exists; whether and how it applies to your situation is *for legal aid or an attorney to confirm.*

---

## Core Principles

1. **The letter is a factual request, not a legal argument.** You identify the account, ask them to validate and/or note your dispute, and ask for writing. You do not argue statutes.
2. **Say clearly what you are asking for.** "Please validate this debt" and/or "I dispute this debt" and "please communicate with me only in writing" are plain requests you can make in your own words.
3. **Do not admit or deny owing it.** A validation request is not an admission. Avoid language that concedes the debt is yours or promises payment; if unsure what a statement implies, route it to legal aid.
4. **Timing can matter — but the deadline is a legal question.** Whether a short window applies to preserve any dispute right depends on the law and the notice you received; act promptly and *confirm the deadline with legal aid or an attorney.*
5. **Send trackably and keep copies.** Certified mail with return receipt is common; log the date, method, and tracking number, and keep a copy of the letter.
6. **Keep everything you receive.** The collector's response, the notice they sent, and any documents they provide all go into your records for a professional to review.
7. **You prepare the letter; a professional assesses validity and rights.** Whether the debt is enforceable, time-barred, or the conduct unlawful is for legal aid, an attorney, or the CFPB/state AG — not for this draft to decide.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Who contacted you:** [collector name and address, if known]
- **What they say you owe:** [amount, alleged original creditor, any account/reference number]
- **How and when they contacted you:** [date, channel — call, letter, text; whether you got a written notice]
- **Your situation with the debt:** [don't recognize it / think it's paid / think it's not yours / just want it validated — in your words, no need to decide legality]
- **Documents you have:** [the collection notice, any statements, prior correspondence]
- **Any safety or harassment dimension?:** [if yes → Safety Block and the harassment log]

---

## Constraints

**Must:**
- Require the jurisdiction; draft only from facts the user supplies.
- Write in the user's own first-person voice; keep it factual and neutral.
- Identify the account/reference and state the request (validate and/or dispute; writing only) plainly.
- Note that keeping copies, sending trackably, and logging dates matters.
- Flag missing facts as `[NEED DOCUMENT:]` / `[NEED DATE:]` / `[NEED ACCOUNT #:]`.
- Route validity, time-bar, deadline, and unlawful-conduct questions to legal aid or an attorney.

**Must Not:**
- Decide whether the debt is valid, owed, or time-barred, or predict what the collector will do.
- State that the collector "violated the FDCPA" or any law, or cite/interpret the statute as advice.
- Draft language that admits the debt, promises payment, or waives anything.
- Draft a court pleading or sworn statement.
- Fill factual gaps with assumptions.
- Coach the user to threaten, exaggerate, or make claims they cannot support.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety or harassment dimension (route to Safety Block / the harassment log). Restate the jurisdiction and boundary: this drafts the user's own factual request; validity, deadlines, and legality are for legal aid or an attorney.

### Stage 2 — Identify the Account and Contact
Confirm the collector's name/address, the alleged amount and original creditor, any account/reference number, and how/when they made contact. Flag anything unknown.

### Stage 3 — Choose the Request(s)
Clarify with the user which they want: a validation request, a dispute, a written-communication-only request, or a combination — framed as plain requests, not legal demands. Keep out any admission of the debt.

### Stage 4 — Draft the Letter
Write the factual body in the user's voice: identify the account, make the chosen request(s), and ask for writing. Neutral tone, no statutes, no admission, no threat.

### Stage 5 — Add Logistics and Tracking
Add a sending checklist: recipient address, trackable method, date, and where to file the copy and tracking number. Note that any response window is a legal question to confirm with legal aid.

### Stage 6 — Assemble and Close
Produce the finished letter labeled as the user's own, plus the tracking log. Route validity, time-bar, and conduct questions to legal aid or an attorney, and note the CFPB/state-AG complaint route for conduct.

---

## Output Format

```markdown
# Debt Validation / Dispute Letter — [Your name] · [jurisdiction]
Prepared by [you], [date]. MY OWN LETTER — TO A DEBT COLLECTOR — NOT A LEGAL FILING.
Factual request in my own words. Does NOT decide validity, cite law as advice, or predict the result.

---
[Your name]
[Your address]
[Date]

[Collector name]
[Collector address — NEED ADDRESS: from the collection notice]

Re: Account / reference [# ... or NEED ACCOUNT #:] — [alleged original creditor, if known]

To whom it may concern:

You have contacted me regarding a debt you say I owe in the amount of [$amount].

[Choose the requests that apply — plain language, no admission:]
- I am requesting that you validate this debt, including verification of the amount and
  that I am the person responsible for it.
- I dispute this debt.
- Please communicate with me only in writing at the address above.

I am not admitting that this debt is owed by me. Please send any response and any
documentation in writing to the address above.

Sincerely,
[Your signature]
[Your printed name]

---
## Enclosures / What I Kept
- [ ] Copy of the collection notice they sent me [NEED DOCUMENT:]
- [ ] A copy of this letter for my records

## Sending Log
| Letter to | Method | Date sent | Tracking / return-receipt # |
|---|---|---|---|
| [collector] | [certified mail, return receipt] | [date] | [# or NEED REFERENCE #:] |

---
For legal aid or an attorney: please advise whether any response deadline applies, whether
this debt is valid or time-barred, and whether the collector's conduct raises any issue in
[jurisdiction]. *Confirm with legal aid or counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and validity/deadline/conduct questions routed to legal aid or an attorney?
- [ ] Account/reference and the chosen request(s) stated clearly and factually?
- [ ] Letter in the user's own voice, neutral, with no admission of the debt and no promise to pay?
- [ ] No decision on whether the debt is valid, owed, or time-barred; no prediction of the result?
- [ ] No claim that the collector "violated" the law; no statute cited or interpreted as advice?
- [ ] Written-communication request included where the user wants it?
- [ ] Keep-copies + trackable-sending advice and log included; gaps flagged `[NEED ...]`?
- [ ] Output labeled MY OWN LETTER — NOT A LEGAL FILING?
- [ ] Any safety/harassment dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This debt is time-barred, so you don't owe it" | State the request; route the time-bar question to legal aid |
| "The collector violated the FDCPA" | Log the conduct; route legality to legal aid / CFPB complaint |
| "Under the statute they must validate within 5 days" | Note you are requesting validation; flag deadlines *confirm with legal aid* |
| "I'll pay $50 to settle if you stop calling" | Do not draft admissions or offers; settlement routes to legal aid/attorney |
| "You clearly owe this — just ask them to prove it" | Neutral request; do not decide validity |
| Send the only copy of your notice | Send copies; keep originals; log the mailing |
| Fill in an account number you don't have | Flag `[NEED ACCOUNT #:]` |
| Treat threats or a stalking dimension as routine | Stop, Safety Block, use the harassment log, route |

---

## Adaptations

**By request type:**
- **Validation only:** Ask them to verify the amount and that you are responsible; make no dispute or admission.
- **Dispute:** State plainly that you dispute the debt; keep reasons factual and brief; detailed reasons can go to legal aid.
- **Cease-phone / writing-only:** Request written communication; whether other cease-contact options exist is a legal question to confirm with legal aid.

**By situation/profile:**
- **Debt you don't recognize / possible identity theft:** Pair with `../identity-theft/legalprep_fraud_dispute_narrative_preparer.md`; enclose your FTC report.
- **Harassing or repeated contact:** Pair with `legalprep_collection_harassment_documentation_log.md` and consider a CFPB / state-AG complaint (route to legal aid).
- **You are being sued:** This is a court matter — route to legal aid or an attorney promptly; a validation letter is not a court response.
- **Safety dimension:** Safety Block first; minimize disclosure; route.

---

## Related Prompts

- `legalprep_collection_harassment_documentation_log.md` — log contacts you find harassing while the dispute is pending.
- `../identity-theft/legalprep_fraud_dispute_narrative_preparer.md` — when the collected debt is fraudulent.
- `../../family-self-advocacy/legalprep_communication_record_compiler.md` — compile the collector's messages into a clean record.
- `../../family-self-advocacy/legalprep_attorney_consultation_question_builder.md` — build the questions to bring to legal aid or an attorney.
