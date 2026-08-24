---
title: "Credit Report Dispute — Challenge an Inaccurate Entry on Your File"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN written dispute of an inaccurate credit-report entry — identifying the specific entry, stating precisely what is wrong and what the correct fact is, listing supporting documents, and sending to both the bureau and the furnisher. Distinguishes inaccuracy from accurate-but-unwanted. Does NOT cite credit-reporting statutes as authority, state investigation deadlines, name bureaus or supply their addresses, promise removal, predict outcomes, or invent entry details. Not legal or financial advice."
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
  - financial-hardship
  - credit-reporting
  - self-submit
  - consumer
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/financial-hardship/advocacy_goodwill_adjustment_request.md
  - domain-legal/personal-self-advocacy/identity-theft/legalprep_fraud_dispute_narrative_preparer.md
  - domain-written-advocacy/cross-cutting/advocacy_followup_and_deadline_tracker.md
  - domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md
---

**Purpose:** Help you write **your own** dated dispute of an entry on your credit report that is **inaccurate** — wrong balance, wrong dates, wrong status, an account that is not yours, a duplicate, or something already settled. It pins the entry, states exactly what is wrong and what the correct fact is, lists what you can produce, and goes to both the bureau reporting it and the company that supplied it.

**When to use:** You have obtained your report, an entry is factually wrong, and you want a documented dispute rather than a portal click with no record.

**When NOT to use:** The entry is accurate and you want it removed as a courtesy → `advocacy_goodwill_adjustment_request.md`; disputing accurate information is the wrong process. The entry results from identity theft or fraud → `domain-legal/personal-self-advocacy/identity-theft/legalprep_fraud_dispute_narrative_preparer.md`, which has a different and stronger route. A collector is reporting a debt you do not recognize → validate the debt first via `domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md`.

---

## Boundary & Routing Block

Use a different pathway if:
- **The entry is accurate** → do not dispute it. An accuracy dispute over correct information is the wrong process, does not correct anything, and misrepresents your position. If you want it reconsidered as a courtesy, use `advocacy_goodwill_adjustment_request.md`.
- **The entry arises from identity theft or fraud** → there is a distinct and generally stronger route, and using the ordinary dispute process can be slower and weaker. See `domain-legal/personal-self-advocacy/identity-theft/`, and report through the official channels first.
- **You are unsure whether the debt is yours at all** → validate it with the collector before disputing the report entry; the two processes serve different purposes. See `domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md`.
- **Someone has offered to fix your credit for a fee** → paid credit repair advertises heavily and frequently charges for disputes you can make yourself, sometimes disputing accurate entries on your behalf. Route to a **nonprofit credit counselling service** `[VERIFY: locate an accredited nonprofit service in your jurisdiction from an official or government source]`.
- **The inaccuracy is connected to litigation, a court judgment, or bankruptcy** → route to an attorney or **legal aid**; those entries have their own routes and consequences.
- **You are being denied credit, housing, or employment because of the entry** → the timing may matter and there may be a specific process attached to the adverse decision. Route to an attorney or legal aid promptly as well as disputing.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal or financial services.

---

## Scope Boundary — Read First

This **drafts your own written credit-report dispute for you to send**. It is **not legal advice, financial advice, credit repair, a legal filing, or a substitute for an attorney, a nonprofit credit counsellor, or your jurisdiction's law.** It will **not** tell you what rights you have; cite, quote, or number any credit-reporting statute, section, or regulation as authority; state how long an investigation takes or must take, or any deadline; name a credit bureau or reporting agency, or supply its address, portal, or dispute URL; tell you how long information stays on a report; tell you what effect an entry or its removal has on a score; tell you whether an entry will be removed or predict any outcome; assess how strong your dispute is; or invent an entry, balance, date, account number, or reporting company. Credit-reporting systems, the agencies involved, and the applicable rules **vary by country and state and change over time** — the bureaus and their current dispute processes must be ones **you** identify from official sources.

---

## Core Principles

1. **Dispute only what is actually inaccurate.** Accuracy is the ground the whole process stands on. If the entry is right, this is the wrong instrument and using it wastes the process.
2. **Name the entry so precisely it cannot be mistaken.** Reporting company, account number as shown, the field that is wrong, and where it appears on the report. Vague disputes get closed as unclear.
3. **State the correct fact, not just the objection.** "The balance is shown as $4,200; the correct balance is $0, settled on [date]" gives an investigator something to check. "This is wrong" does not.
4. **Dispute one entry at a time, clearly.** Where several entries are wrong, list each separately with its own correction. A single narrative covering five problems tends to be treated as one and half-resolved.
5. **Send to both the bureau and the furnisher.** The agency reporting it and the company that supplied it are different parties with different records, and disputing to only one is the most common reason a corrected entry reappears.
6. **Attach documents, and keep the originals.** Statements, settlement letters, payment confirmations, correspondence. Send copies; never send an original you cannot replace.
7. **Keep every reference number and re-check afterwards.** Corrections sometimes reverse when the furnisher next reports. Diary a re-check and hold the reference numbers.

---

## Your Input

- **Your jurisdiction (state/country):** [required — reporting systems differ]
- **Is the entry genuinely inaccurate?:** [if no → Boundary & Routing Block]
- **Does it arise from fraud or identity theft?:** [if yes → Boundary & Routing Block]
- **Which agency's report shows it:** [as named on your report — you supply this]
- **Reporting company (furnisher) as shown:** [name on the entry]
- **Account number as shown on the report:** [#, partial is normal]
- **The entry as reported:** [status, balance, dates, payment history as shown]
- **What is wrong:** [the specific field or fields]
- **The correct fact:** [what it should say]
- **Evidence you hold:** [statements, settlement letter, payment confirmation, correspondence]
- **When you obtained the report:** [YYYY-MM-DD]
- **Whether other agencies show the same entry:** [yes/no/unknown]
- **Prior disputes on this entry:** [when, to whom, outcome, reference #]
- **Any adverse decision, litigation, or paid credit-repair involvement?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Confirm the entry is genuinely inaccurate before drafting, and route accurate entries to the goodwill prompt.
- Screen for fraud, unverified debts, adverse decisions, litigation, and paid credit repair before drafting.
- Identify the entry precisely — reporting company, account number as shown, and the specific field.
- State both what is wrong **and** what the correct fact is.
- Handle multiple inaccurate entries as separate numbered items with separate corrections.
- Produce two versions: one to the reporting agency, one to the furnisher.
- Instruct the user to send copies and retain originals.
- Require the user to identify the agencies and their current dispute processes from official sources, flagged `[VERIFY:]`.
- Include a Sending Log with reference numbers and a re-check date, and label the output `MY OWN DISPUTE — NOT A LEGAL FILING`.

**Must Not:**
- Draft a dispute of an entry the user accepts is accurate.
- Cite, quote, or number any credit-reporting statute, section, or regulation.
- State any investigation deadline, response period, or reporting-retention period.
- Name a credit bureau or reporting agency, or supply an address, portal, or dispute URL.
- State what effect an entry or its removal has on a credit score.
- Promise or predict removal, correction, or any outcome.
- Assess how strong the dispute is.
- Recommend a credit repair company or paid dispute service.
- Invent an entry, balance, date, status, account number, or reporting company.
- Advise sending original documents.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Confirm first that the entry is genuinely inaccurate; if not, **stop and route to the goodwill prompt**. Then screen for fraud, an unverified debt, an adverse credit/housing/employment decision, litigation or bankruptcy, and paid credit-repair involvement → route per the Boundary & Routing Block. Restate the jurisdiction and the boundary.

### Stage 2 — Pin the Entry Precisely
Record the agency whose report shows it, the reporting company as named, the account number as shown, and the entry's current content — status, balance, dates, payment history. Flag anything the user cannot read off the report as `[NEED DOCUMENT: copy of your credit report]`.

### Stage 3 — State the Inaccuracy and the Correction
For each wrong field, state what is reported and what the correct fact is, with the date and the evidence that supports it. Where several entries are wrong, number them and keep each correction separate.

### Stage 4 — Assemble the Evidence
List the documents that support each correction and tie each to its numbered item. Instruct the user to send copies and keep originals. Flag documents the user believes exist but has not located as `[NEED DOCUMENT:]`.

### Stage 5 — Build Both Letters
Produce the dispute to the reporting agency and a parallel dispute to the furnisher, each with the same numbered items and corrections. Instruct the user to identify each agency and its current dispute process from official sources, flagged `[VERIFY:]`, rather than relying on any address supplied here.

### Stage 6 — Set the Tracking and Close
Set up the Sending Log with reference numbers for both letters and a re-check date to confirm the correction held and did not reverse. Route rights, adverse decisions, and fraud questions onward.

---

## Output Format

```markdown
MY OWN CREDIT REPORT DISPUTE — NOT A LEGAL FILING
From: [your name], [address as it appears on my report], [contact]. Date: [YYYY-MM-DD].
Delivery: [certified mail / the agency's own dispute channel]. Keep a copy of everything sent.
This is my own dispute of information I believe is inaccurate. It does NOT cite any law, state
any investigation deadline, promise removal, or predict any outcome. I am not disputing anything
I accept is accurate.

Report obtained on [YYYY-MM-DD] from [agency, as named on my report].

## Who I am
Name: [full name as on the report] · Date of birth: [as required by their process]
Current address: [address] · Previous address: [if the entry predates a move]
[Identifiers their process requires — supplied through their secure channel, not in this letter
where their process allows.]

## The entry I am disputing
| Field | Detail |
|---|---|
| Reporting company as shown | [name] |
| Account number as shown | [#, partial as displayed] |
| Where it appears | [section of the report] |

### Item 1
- **Reported as:** [status / balance / date, exactly as shown]
- **What is inaccurate:** [the specific field]
- **The correct fact:** [what it should say]
- **Evidence:** [document, dated YYYY-MM-DD]

### Item 2
- **Reported as:** [...]
- **What is inaccurate:** [...]
- **The correct fact:** [...]
- **Evidence:** [...]

## What I am asking you to do
Please investigate items 1 and 2 above and correct the entry to reflect the correct facts.
Please tell me in writing what you have done, and provide a reference number for this dispute.

## Documents enclosed (copies — I have retained the originals)
- [statement dated YYYY-MM-DD showing the correct balance]
- [settlement / payoff letter dated YYYY-MM-DD]
- [payment confirmation dated YYYY-MM-DD]
- [NEED DOCUMENT: ...]

[Your name], [YYYY-MM-DD]

---

## Second letter — to the reporting company (furnisher)
Same numbered items, addressed to [reporting company] rather than the agency:

> To: [reporting company, its designated disputes channel] · Date: [YYYY-MM-DD]
> Re: Inaccurate information reported about account [#]
>
> You are reporting information about my account that I believe is inaccurate. I have also
> raised this with [agency].
>
> Item 1 — Reported as [X]. The correct fact is [Y], evidenced by [document dated].
> Item 2 — Reported as [X]. The correct fact is [Y], evidenced by [document dated].
>
> Please correct what you report and confirm in writing what you have done.
>
> [Your name], [account #], [YYYY-MM-DD]

`[VERIFY: identify each credit reporting agency operating in my jurisdiction and its current
dispute process and address from official sources. This letter does not tell me who they are or
where to send it. If more than one agency shows the entry, I must dispute with each separately.]`

---
## Sending Log (keep with your copies)
| Sent | To | Method | Reference # | Proof kept | Response received | Corrected? |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [agency] | [certified mail] | [#] | [receipt] | [ ] | [ ] |
| [YYYY-MM-DD] | [furnisher] | [certified mail] | [#] | [receipt] | [ ] | [ ] |

**Re-check the report on [YYYY-MM-DD]** to confirm the correction was made and has not reversed.
Corrections sometimes revert when the reporting company next submits data.

Note to self: this is my own dispute, not legal or financial advice. What rights I have, how long
an investigation takes, and what any of this does to my score are not stated here. **No company
can lawfully do anything I cannot do myself here, and paid credit repair frequently charges for
exactly this letter** — if I want help I will use a nonprofit credit counselling service
`[VERIFY: locate an accredited nonprofit service in my jurisdiction from an official source]`.
*Verify for your jurisdiction — credit-reporting systems and rules vary by country and state.*
```

---

## Verification

- [ ] Entry confirmed genuinely inaccurate, with accurate entries routed to the goodwill prompt?
- [ ] Fraud, unverified debt, adverse decision, litigation, and paid credit-repair dimensions screened and routed?
- [ ] Jurisdiction captured and rights routed *verify with an attorney*?
- [ ] Entry pinned by reporting company, account number as shown, and location on the report?
- [ ] Each inaccuracy states both what is reported **and** the correct fact, with evidence?
- [ ] Multiple inaccuracies handled as separate numbered items?
- [ ] Both letters produced — agency and furnisher — with identical numbered items?
- [ ] Send-copies-keep-originals instruction included?
- [ ] **No credit bureau or agency named, and no address, portal, or URL supplied?**
- [ ] **No credit-reporting statute, section, or regulation cited, quoted, or numbered?**
- [ ] No investigation deadline, response period, or retention period stated?
- [ ] No score-effect claim, removal promise, outcome prediction, or strength assessment?
- [ ] No credit repair or paid dispute service recommended, and the paid-repair warning included?
- [ ] No invented entry, balance, date, status, account number, or company?
- [ ] Sending Log with reference numbers and a re-check date included?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Send it to Equifax, Experian and TransUnion at [addresses]" | `[VERIFY: identify the agencies in your jurisdiction and their current processes from official sources]` |
| "Under FCRA § 611 they have 30 days to investigate" | Cite nothing and state no deadline |
| "Dispute everything — some of it will drop off" | Dispute only what is genuinely inaccurate; that is the ground the process stands on |
| "This will take about 45 points off your file when removed" | Say nothing about score effects |
| "They'll almost certainly delete it if the furnisher doesn't respond" | Promise and predict nothing |
| Dispute only with the bureau | Dispute with **both** the bureau and the furnisher, or corrections commonly reappear |
| Send the original settlement letter as proof | Send copies; keep originals |
| "This is wrong, please fix it" | State what is reported and what the correct fact is, with evidence |
| "[Company] can clean this up for $79/month" | Recommend no paid repair; warn that it charges for this same letter |
| Dispute a fraudulent account through the ordinary route | Stop, use the Boundary & Routing Block, use the identity-theft route |

---

## Adaptations

**By inaccuracy type:**
- **Wrong balance or status:** Attach the statement or settlement letter showing the correct figure and date; this is the most straightforward correction.
- **Account not yours:** State plainly that you have no relationship with the company, and note whether the name or address is similar to yours — mixed files usually turn on that. If it looks like fraud, route to identity theft instead.
- **Duplicate entry:** Identify both entries by their reference and ask for the duplicate to be removed, specifying which is correct.
- **Dates wrong (opened, closed, first delinquency):** Date fields can matter more than they appear; state the correct dates with the evidence for each.

**By situation/profile:**
- **Same entry on several reports:** Dispute with each agency separately — a correction with one does not propagate. Track them as separate rows in the log.
- **Previously disputed and it came back:** Include the prior dispute date and reference and say it was corrected and has reverted; that history is material.
- **You were denied credit, housing, or a job because of it:** Route to an attorney promptly as well as disputing; there may be a process attached to that decision.
- **Paid credit repair already involved:** Check what has been disputed in your name — disputes of accurate entries made on your behalf can cause problems.

---

## Related Prompts

- `advocacy_goodwill_adjustment_request.md` — where the entry is accurate and you want it reconsidered.
- `../../domain-legal/personal-self-advocacy/identity-theft/legalprep_fraud_dispute_narrative_preparer.md` — where the entry results from fraud.
- `../../domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md` — validate the debt where you do not recognize it.
- `../cross-cutting/advocacy_followup_and_deadline_tracker.md` — track both letters and the re-check date.
