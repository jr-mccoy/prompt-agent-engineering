---
title: "Consumer Complaint Documentation Organizer — Turn a Dispute into a Factual Record"
category: legalprep
description: "Help a consumer organize a dispute over a defective product, undelivered service, billing error, or deceptive practice into a clean, dated, factual record — what was purchased, when, from whom, what went wrong, the communications, and the resolution requested — for the user's own use, an agency complaint, or an attorney. Does NOT assess whether a practice was unlawful, predict outcomes, cite consumer-protection law, or draft a legal filing — those route to an attorney or agency. Not legal advice."
techniques:
  - DS-01
  - DS-21
  - ST-02
  - NE-25
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - consumer
  - complaint
  - refund
  - documentation
  - billing-dispute
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/consumer-scams/legalprep_scam_fraud_report_preparer.md
  - domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md
  - domain-legal/client-intake-communications/legal_demand_letter_drafter.md
  - domain-legal/litigation/legal_complaint_drafter.md
  - domain-legal/litigation/legal_settlement_value_range_analysis.md
---

**Purpose:** Help you turn a consumer dispute — a defective product, a service you paid for and never received, a billing or charge error, or a sales/advertising practice you believe was misleading — into one clean, dated, factual record. It captures what you bought, when, from whom, for how much, exactly what went wrong, every communication you have had, and the specific resolution you want. This record is reusable: you can keep it for yourself, attach it to a complaint to the FTC or your state attorney general, or hand it to an attorney. It organizes **your own information** — it does **not** tell you whether the seller broke any law, predict whether you will get your money back, or claim the record "proves" a deceptive or unfair practice.

**When to use:** You have a dispute with a merchant, seller, service provider, subscription, or platform and you want your facts in order before you complain, request a refund, dispute a charge, or talk to a lawyer or agency. Use one copy per transaction or dispute.

**When NOT to use:** You want to know whether the seller's conduct is illegal, whether you have a "case," or what a claim is worth → that is legal analysis; route it to an attorney or your state attorney general's consumer-protection office. You believe you were targeted by a scam or fraud (not just a bad transaction) → use `legalprep_scam_fraud_report_preparer.md`. You are ready to dispute a specific card charge or ask for a refund in writing → use `legalprep_refund_chargeback_dispute_preparer.md`. Money you have already lost may be time-sensitive → Safety Block first.

---

## Safety Block

Act quickly and use the right pathway if:
- **Money already left your account, or you gave card/bank details to someone you now doubt** → contact your bank or card issuer's fraud line **immediately** (the number on the back of your card); time limits to dispute are short. Then see `legalprep_scam_fraud_report_preparer.md`.
- **You believe this was a scam or fraud, not just a bad purchase** → report at `ReportFraud.ftc.gov` (FTC) and, for online crime, `ic3.gov` (FBI Internet Crime Complaint Center).
- **Your identity or account credentials may be compromised** → `IdentityTheft.gov` (FTC) for a recovery plan; change passwords; enable two-factor authentication.
- **You are being threatened, intimidated, or coerced over the dispute** → local police; emergencies **911**; if you are in personal danger and it involves a household or intimate contact, `National Domestic Violence Hotline 1-800-799-7233`.
- **You are in crisis** → `988 Suicide & Crisis Lifeline`.

This prompt is educational support for organizing your own records. It is not a substitute for legal, financial, or law-enforcement services.

---

## Scope Boundary — Read First

This **structures a factual consumer-dispute record from your own information and documents**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney, an agency, or your jurisdiction's consumer-protection law.** It will **not** decide whether the seller's conduct was unlawful, unfair, or deceptive; predict whether you will recover; assess how strong your dispute is; cite or invent consumer statutes, warranty standards, or case law; characterize the seller's motive; or draft a demand letter, agency complaint, or court pleading. Whether a practice is legally actionable — and what to do about it — **varies by state and country and changes over time** and is for an attorney or the relevant agency. Where a term (warranty, chargeback, deceptive practice) appears, it is explained in plain language and flagged *confirm with counsel or your state attorney general's office.*

---

## Core Principles

1. **The transaction is the anchor.** Every dispute starts with a specific purchase: what, when, from whom, how much, and how you paid. Pin those down first; everything else hangs on them.
2. **Describe what went wrong; do not label it.** "Ordered on [date]; item never arrived after 6 weeks; three follow-up emails unanswered" — not "this is a scam" or "they committed fraud." Facts travel; labels invite argument and are for a professional.
3. **Communications are the spine of the record.** Every call, email, chat, and letter — with dates, who you spoke to, and what was said — shows what you tried and how the seller responded.
4. **Amounts and dates precisely.** The purchase amount, any partial refund, shipping, fees, and the dates of each are the facts an agency, bank, or court cares about most. Approximate only when you must, and flag it.
5. **Keep the seller's identity concrete.** Legal name, storefront/brand name, website, address, order/account number, and any salesperson name. A dispute against "some website" is far weaker than one tied to a named entity.
6. **State the resolution you want, plainly.** Refund of $X, replacement, cancellation, corrected bill, or removal of a charge — a specific ask, stated, not argued.
7. **You document and prepare; the professional assesses.** You assemble the facts; whether the conduct was unlawful and what remedy the law provides is for an attorney or agency. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **What you purchased:** [product/service description]
- **From whom:** [seller legal/brand name, website, storefront, address if known]
- **Date of purchase and amount:** [YYYY-MM-DD; total paid; how you paid]
- **Order / account / invoice number:** [if any]
- **What went wrong:** [in your own words — defective / not delivered / billed wrong / misleading claim]
- **Communications so far:** [dates, channel, who, what was said/promised]
- **Documents you have:** [receipt, order confirmation, listing/ad, photos, emails, chat logs, statements]
- **Resolution you want:** [refund $X / replacement / cancellation / corrected bill / other]
- **Any safety, money-loss, or fraud dimension?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; build the record only from facts the user supplies.
- Anchor to the specific transaction: item, seller, date, amount, payment method, order number.
- Log every communication with date, channel, participant, and what was said.
- State amounts and dates precisely; flag imprecise ones as `[NEED DATE:]` / `[APPROX: ...]`.
- List supporting documents; flag missing items as `[NEED DOCUMENT:]`.
- Keep every entry factual; strip motive, opinion, and legal labels.
- Route all questions about legality, remedies, and case strength to an attorney or agency.

**Must Not:**
- State legal conclusions ("this is fraud / a deceptive practice / a breach of warranty under the law").
- Assess how strong the dispute is or predict whether the user will recover.
- Cite or invent consumer-protection statutes, warranty standards, or case law.
- Characterize the seller, attribute motive, or apply labels to their conduct.
- Draft a demand letter, agency complaint, or court pleading (route to the appropriate prompt or an attorney).
- Fill factual gaps with assumption or reconstruction (flag `[NEED …:]`).
- Coach the user to exaggerate the loss, the promises made, or the seller's conduct.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any money-loss, fraud, or safety dimension (route to Safety Block — especially "call your bank now" if funds left an account). Restate the dispute type and jurisdiction. Confirm the boundary: this organizes the facts; whether the conduct was unlawful is for an attorney or agency.

### Stage 2 — Anchor the Transaction
Capture the item/service, the seller's concrete identity, the purchase date, total amount, payment method, and any order/account/invoice number. Flag any missing anchor as `[NEED DOCUMENT:]` or `[NEED DATE:]`.

### Stage 3 — Describe What Went Wrong (Facts, Not Labels)
Have the user describe the problem in plain factual terms. Rewrite any sentence containing a legal label ("this is fraud," "deceptive," "illegal") or motive attribution into observable fact: what was promised, what was delivered, what is missing or defective.

### Stage 4 — Build the Communication Log
Lay every contact in date order: date, channel (phone/email/chat/letter), who you dealt with, what you asked, and what they said or promised. Note anything a representative committed to and whether it happened. Flag gaps as `[NEED DATE:]`.

### Stage 5 — Index Supporting Documents
List every document: receipt, order confirmation, the listing or advertisement as it appeared, photos of a defect, emails, chat transcripts, bank/card statements showing the charge. Note storage location and status; flag items to obtain as `[NEED DOCUMENT:]`.

### Stage 6 — State the Resolution Requested and Package
Record the specific resolution the user wants, and the reasonable deadline they have in mind (stated, not asserted as a legal right). Assemble the full record under the header. Note that this record can feed a refund/chargeback request, an agency complaint, or an attorney handoff. Route legality and remedy questions out.

---

## Output Format

```markdown
# Consumer Dispute Record — [Your name] · [seller/brand] · [jurisdiction]
Purchase date: [date]. Amount: [$X]. Compiled by [you], [date].
FOR MY OWN USE / MY ATTORNEY / AN AGENCY COMPLAINT — NOT A LEGAL FILING.
Does NOT assess legality, predict recovery, or state that any law was broken.

## Transaction Anchor
- Item / service: [description]
- Seller: [legal/brand name] · [website/storefront] · [address if known]
- Order / account / invoice #: [number or NEED DOCUMENT:]
- Purchase date: [YYYY-MM-DD or NEED DATE:]
- Amount paid: [$X] · Payment method: [card ending ####, bank transfer, app, etc.]

## What Went Wrong (facts only)
1. [Factual, specific — what was promised, what was delivered, what is missing/defective. No labels.]
2. [...]

## Communication Log
| Date | Channel | Who I dealt with | What I asked | What they said / promised | Happened? |
|---|---|---|---|---|---|
| [YYYY-MM-DD] | Email | [name/dept] | [refund request] | [quote or summary] | [Yes/No/Pending] |

## Supporting Documents
| Item | Date | What it shows | Storage location | Status |
|---|---|---|---|---|
| Order confirmation | [date] | [item, price, seller] | [email folder] | Have it |
| Photo of defect | [date/EXIF] | [what is visible] | [photos folder] | Have it |
| Card statement line | [date] | [charge of $X to seller] | [statements folder] | [NEED DOCUMENT:] |

## Resolution I Am Requesting
- [Refund of $X / replacement / cancellation / corrected bill / removal of charge]
- Reasonable response window I have in mind: [e.g., 14 days] *(confirm any legal deadline with counsel/agency)*

## Gaps to Address
- [NEED DOCUMENT: receipt / listing screenshot / statement page]
- [NEED DATE: date of first complaint call]

---
For an attorney or my state attorney general's consumer-protection office:
please advise whether this conduct is actionable and what remedies apply.
*Confirm with counsel or the relevant agency for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel/agency*?
- [ ] Transaction anchored: item, seller identity, date, amount, payment method, order number (or flagged)?
- [ ] "What went wrong" kept factual — no legal labels, no motive attribution?
- [ ] Every communication logged with date, channel, participant, and content?
- [ ] Amounts and dates precise, or flagged `[NEED …:]` / `[APPROX:]`?
- [ ] Supporting documents indexed with storage location and status; gaps flagged?
- [ ] Specific requested resolution stated, not argued as a legal entitlement?
- [ ] No claim the record "proves" fraud, deception, or a warranty breach?
- [ ] No demand letter, agency complaint, or pleading drafted?
- [ ] All legality / remedy / case-strength questions routed to an attorney or agency?
- [ ] Any safety or money-loss dimension screened and routed (call-your-bank-now if relevant)?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This is a deceptive trade practice under the law" | "Ad said 'ships in 2 days'; item arrived after 6 weeks" — legality is for an attorney/agency |
| "They defrauded you — you'll definitely win a refund" | Organize the facts; recovery and case strength route to a professional |
| "Cite the FTC Act / state UDAP statute" | Do not cite law; note the issue and route to the state attorney general's office |
| "The seller obviously meant to rip you off" | Describe what was promised vs. delivered; motive is not a fact |
| Draft the agency complaint or demand letter here | Assemble the record; use `legalprep_refund_chargeback_dispute_preparer.md` or an attorney |
| Fill in an order number you don't have | Flag `[NEED DOCUMENT: order confirmation]` |
| Round "$847.19" up to "about a thousand" | Use the exact figure from the statement |
| Treat a live money-loss/fraud as routine paperwork | Stop, Safety Block, call the bank now, report to `ReportFraud.ftc.gov` |

---

## Adaptations

**By dispute type:**
- **Defective product:** Center the record on the item's condition — photos with timestamps, the listing as advertised, and the defect described observably (not "dangerous" or "fraudulent").
- **Service not delivered:** Anchor to the agreed scope and date, the payment, and the absence of delivery; log every follow-up.
- **Billing / charge error:** Attach the statement line, the expected amount vs. charged amount, and the date you first flagged it; pair with `legalprep_refund_chargeback_dispute_preparer.md`.
- **Misleading advertising / sales claim:** Capture the ad or listing exactly as it appeared (screenshot with date) alongside what was actually delivered — let the two documents speak.
- **Subscription / auto-renewal:** Record the sign-up date, the cancellation attempt(s) with dates, and every charge after cancellation.

**By situation/profile:**
- **Possible scam or fraud:** Safety Block first; route to `legalprep_scam_fraud_report_preparer.md` and your bank.
- **Small-dollar but repeated:** Keep each instance dated; a pattern record is stronger than a single vague complaint — but pattern *significance* is for a professional.
- **Elderly or vulnerable consumer:** Note if high-pressure or repeated contact occurred (factually); route to the state attorney general's office and, if applicable, adult-protective resources.

---

## Related Prompts

- `legalprep_scam_fraud_report_preparer.md` — when the dispute is (or may be) a scam/fraud you need to report to the FTC, FBI IC3, your bank, or a state AG.
- `legalprep_refund_chargeback_dispute_preparer.md` — to turn this record into your own factual refund or chargeback request to a merchant or card issuer.
- `../../client-intake-communications/legal_demand_letter_drafter.md` — the attorney-side demand-letter counterpart your lawyer may use.
- `../../litigation/legal_complaint_drafter.md` — if the matter proceeds to court (e.g., small claims), the attorney-side pleading counterpart.
- `../../litigation/legal_settlement_value_range_analysis.md` — the attorney-side tool for valuing a claim (valuation is for counsel, not this record).
