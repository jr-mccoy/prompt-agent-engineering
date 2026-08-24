---
title: "Refund & Chargeback Dispute Preparer — Draft Your Own Factual Request to a Merchant or Card Issuer"
category: legalprep
description: "Help a consumer draft THEIR OWN factual refund request to a merchant or dispute (chargeback) request to a card issuer or bank — the transaction details, what went wrong, what they have already tried, and exactly what they are requesting. Keeps it factual and first-person. Does NOT decide whether the charge is legally disputable, predict whether the dispute will be granted, cite card-network rules or law, or file it for the user — those route to the issuer or an attorney. Not legal advice."
techniques:
  - DS-01
  - ST-02
  - ST-03
  - CM-01
  - NE-25
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - refund
  - chargeback
  - self-submit
  - billing-dispute
  - consumer
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/consumer-scams/legalprep_consumer_complaint_documentation_organizer.md
  - domain-legal/personal-self-advocacy/consumer-scams/legalprep_scam_fraud_report_preparer.md
  - domain-legal/client-intake-communications/legal_demand_letter_drafter.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Help you write **your own** clear, factual request to get your money back — either a refund request to the merchant or a dispute (chargeback) request to your card issuer or bank. It pulls together the exact transaction details, what went wrong, what you already tried with the seller, and precisely what you are asking for and by when. This is **your own first-person message** to read, verify, and submit — it does **not** decide whether the charge qualifies for a chargeback under card-network rules or law, predict whether your dispute will be granted, or file it for you.

**When to use:** You paid for something that was defective, never delivered, not as described, charged incorrectly, double-billed, or charged after you cancelled — and you want a factual refund request for the merchant and/or a dispute request for your card issuer or bank, ready for you to submit.

**When NOT to use:** You want to know whether you are legally entitled to a refund, whether the chargeback "will win," or what card-network rules require → route that to your issuer or an attorney. You believe the whole transaction was a scam or fraud → use `legalprep_scam_fraud_report_preparer.md` and call your bank now (Safety Block). You just want your facts organized before deciding → use `legalprep_consumer_complaint_documentation_organizer.md`.

---

## Safety Block

Act quickly and use the right pathway if:
- **The charge is unauthorized, or you think you were scammed** → contact your bank or card issuer's fraud line **immediately** (number on the back of your card); dispute windows are short. Then see `legalprep_scam_fraud_report_preparer.md` and report at `ReportFraud.ftc.gov` / `ic3.gov`.
- **Your card or account may be compromised** → ask the issuer to freeze/reissue the card; change online passwords; see `IdentityTheft.gov`.
- **A deadline is near** — many issuers require disputes within a set number of days of the statement → contact the issuer **now**; do not wait to perfect the letter. *(Exact deadlines vary — confirm with your issuer.)*
- **You are being threatened or pressured over the charge** → local police; emergencies **911**.
- **You are in crisis** → `988 Suicide & Crisis Lifeline`.

This prompt is educational support for preparing your own request. It is not a substitute for legal, banking, or law-enforcement services.

---

## Scope Boundary — Read First

This **prepares your own factual refund or dispute request for you to submit** to a merchant or card issuer. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney, your card issuer, or your jurisdiction's law.** It will **not** decide whether the charge is legally disputable or chargeback-eligible; predict whether the merchant or issuer will grant it; assess how strong the dispute is; cite or invent card-network rules, the Fair Credit Billing Act, or other statutes; characterize the merchant's motive; or submit the request for you. Whether you are entitled to a refund or chargeback — and the rules and deadlines that apply — **vary by issuer, network, state, and country and change over time** and are for your issuer or an attorney. You will read, verify, and submit the request yourself.

---

## Core Principles

1. **The transaction is the anchor.** Merchant name, date, amount, last four digits of the card / account, and the order or reference number. An issuer cannot act on a charge it cannot identify.
2. **State the reason factually, in plain terms.** "Item never delivered," "charged $89 but agreed price was $49," "billed after I cancelled on [date]" — a clear factual reason, not a legal argument.
3. **Show what you already tried with the merchant.** Most issuers and networks expect you to have contacted the seller first. Log the date you asked, how, and the response (or silence).
4. **Ask for one specific thing.** "Refund the full $89," "reverse the $40 overcharge," "cancel and refund the renewal" — a precise ask with a date, not a vague grievance.
5. **Attach the proof, listed.** Receipt, order confirmation, the listing as advertised, delivery tracking, cancellation confirmation, prior emails — each named and attached.
6. **Neutral and brief wins.** A short, factual, dated request is easier to process than a long, emotional one. Strip adjectives and accusations.
7. **You prepare and submit; the issuer decides.** You supply the facts and the ask; whether the dispute is granted, and under what rules, is for the issuer or an attorney. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Who you are asking:** [merchant / card issuer / bank]
- **The charge:** [merchant name, date, amount, card last four / account, order or reference #]
- **What went wrong:** [defective / not delivered / not as described / wrong amount / charged after cancellation / duplicate]
- **What you already tried with the merchant:** [date, channel, what you asked, response]
- **What you are requesting:** [full refund $X / partial reversal $X / cancellation + refund / correction]
- **Documents you have:** [receipt, confirmation, listing, tracking, cancellation proof, prior emails, statement line]
- **Any deadline you are aware of:** [statement date / return window — flag *confirm with issuer*]
- **Any fraud/unauthorized dimension?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; use only facts the user supplies.
- Anchor to the exact charge: merchant, date, amount, card last four/account, order/reference number.
- State a plain factual reason for the request; strip legal argument and motive.
- Log what the user already attempted with the merchant, with dates.
- State one specific requested resolution and any user-known deadline (flagged *confirm with issuer*).
- List and attach supporting documents; flag missing ones as `[NEED DOCUMENT:]`.
- Keep it first-person, factual, neutral; present it as the user's own to review and submit.

**Must Not:**
- Decide the charge is legally disputable or chargeback-eligible, or state a legal conclusion.
- Predict whether the merchant or issuer will grant the request, or assess its strength.
- Cite or invent card-network rules, the Fair Credit Billing Act, or other statutes.
- Characterize the merchant or attribute motive ("they steal from customers").
- Submit or file the dispute for the user.
- Fill gaps in the transaction details with assumption (flag `[NEED …:]`).
- Coach the user to misstate the reason, the amount, or what the merchant said.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for an unauthorized/fraud dimension and any near deadline (route to Safety Block — "call the issuer now" if either applies). Restate whether this is a merchant refund request or an issuer dispute, and the jurisdiction. Confirm the boundary: this prepares the request; eligibility and the outcome are for the issuer or an attorney.

### Stage 2 — Anchor the Charge
Capture the merchant name, transaction date, exact amount, card last four or account, and order/reference number. Flag any missing anchor as `[NEED DOCUMENT:]`.

### Stage 3 — State the Factual Reason
Have the user describe what went wrong in one or two plain factual sentences. Rewrite any legal argument ("this violates my rights") or motive claim into a factual statement of what was expected vs. what happened.

### Stage 4 — Show the Merchant Contact Attempt
Record what the user already did with the seller: date, channel, the request, and the response or lack of one. If they have not contacted the merchant and the channel expects it, note that as a step.

### Stage 5 — State the Ask and List Proof
Record the one specific resolution requested and any known deadline (flagged *confirm with issuer*). List every supporting document to attach; flag missing items.

### Stage 6 — Assemble the Request and Close
Compose the first-person request, labeled as the user's own. Note the two possible recipients (merchant vs. issuer) and that the user submits it themselves. Route eligibility, rules, and outcome questions to the issuer or an attorney.

---

## Output Format

```markdown
MY OWN REQUEST — REFUND / CHARGEBACK DISPUTE — NOT A LEGAL FILING
To: [merchant name] / [card issuer or bank]. From: [you], [date].
This is my own factual request. It does NOT state that any law or rule entitles me to this,
predict the outcome, or accuse the merchant. Eligibility and rules are for my issuer / an attorney.

## The charge
- Merchant: [name]
- Transaction date: [YYYY-MM-DD]
- Amount: [$X]
- Card ending: [####] / Account: [ref]
- Order / reference #: [number or NEED DOCUMENT:]

## What went wrong (factual)
[One or two plain sentences: what I paid for, what happened, e.g. "I ordered [item] on [date]
for $X. It was never delivered / arrived defective / was charged after I cancelled on [date]."]

## What I already did with the merchant
On [date] I contacted [merchant] by [email/phone/chat] and asked for [refund/correction].
Their response: [quote or "no response as of [date]"].

## What I am requesting
[Full refund of $X / reversal of the $Y overcharge / cancellation and refund of the renewal].
Requested by: [date, if any] *(I will confirm any applicable deadline with my issuer.)*

## Documents attached
- [Receipt / order confirmation]
- [Listing or advertised description]
- [Delivery tracking / cancellation confirmation]
- [Prior emails with the merchant]
- [Statement line showing the charge]
- [NEED DOCUMENT: ...]

---
I am submitting this request myself. If my card issuer asks me to confirm the dispute is
accurate, I will read that statement, verify the facts above, and submit it myself.
For an attorney or my issuer: please advise on eligibility, applicable rules, and deadlines.
*Confirm with your card issuer or counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and rule/deadline questions routed *confirm with issuer/counsel*?
- [ ] Charge anchored: merchant, date, amount, card last four/account, order number (or flagged)?
- [ ] Reason stated factually — no legal argument, no motive attribution?
- [ ] Prior merchant-contact attempt logged with date and response?
- [ ] One specific requested resolution stated; any known deadline flagged *confirm with issuer*?
- [ ] Supporting documents listed and attached; gaps flagged `[NEED DOCUMENT:]`?
- [ ] Written first-person, neutral, and labeled as the user's own to submit?
- [ ] No claim the charge is legally disputable or that the dispute "will win"?
- [ ] No card-network rule or statute cited or invented?
- [ ] Unauthorized/fraud dimension and near deadlines screened and routed (call issuer now)?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You're legally entitled to this chargeback under the FCBA" | State the facts and the ask; eligibility is for the issuer/attorney |
| "This dispute will definitely be approved" | Prepare the request; the outcome is the issuer's decision |
| "Cite Visa/Mastercard chargeback reason codes" | Do not cite network rules; the issuer applies them |
| "The merchant is a fraud that robs customers" | "Item was never delivered; charged $X on [date]" — no motive |
| Submit the dispute through the issuer's portal for the user | Prepare it; the user reviews and submits it |
| Invent an order number to fill the field | Flag `[NEED DOCUMENT: order confirmation]` |
| Change "$49" to "$490" to look worse | Use the exact amount from the statement |
| Treat an unauthorized charge as a routine refund | Stop, Safety Block, call the issuer's fraud line now |

---

## Adaptations

**By reason:**
- **Not delivered:** Center on the order date, promised delivery, and absence of tracking/receipt; attach any "shipped" claim vs. actual.
- **Not as described / defective:** Attach the listing as advertised and photos of what arrived; describe the difference factually.
- **Wrong or duplicate amount:** Show the agreed price vs. the charged amount, or the two identical charges with dates.
- **Charged after cancellation:** Attach the cancellation confirmation with its date and each charge that followed.
- **Free-trial / auto-renewal:** Show the sign-up terms as presented, the cancellation attempt, and the renewal charge.

**By recipient:**
- **Merchant first:** Keep it a polite, dated refund request; this also creates the "I tried the merchant" record an issuer may expect.
- **Card issuer / bank:** Emphasize the exact charge identifiers, the prior merchant contact, and the attached proof; ask the issuer about the applicable deadline and process.

**By situation/profile:**
- **Possible fraud:** Safety Block; route to `legalprep_scam_fraud_report_preparer.md`; call the fraud line.
- **Recurring small charges:** List each dated charge; a clean itemized list is easier for the issuer to reverse.
- **Deadline pressure:** Contact the issuer immediately; a phone dispute now plus this written follow-up beats a perfect letter sent late.

---

## Related Prompts

- `legalprep_consumer_complaint_documentation_organizer.md` — to organize the full dispute record this request draws on.
- `legalprep_scam_fraud_report_preparer.md` — if the charge is unauthorized or part of a scam.
- `../../client-intake-communications/legal_demand_letter_drafter.md` — the attorney-side demand-letter counterpart if you escalate through counsel.
- `../../litigation/legal_complaint_drafter.md` — the attorney-side pleading counterpart if the matter proceeds to court (e.g., small claims).
