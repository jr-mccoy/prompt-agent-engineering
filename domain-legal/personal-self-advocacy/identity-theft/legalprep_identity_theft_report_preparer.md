---
title: "Identity-Theft Documentation & Report Preparer (Build Your Own Factual Recovery Record)"
category: legalprep
description: "Help an identity-theft victim document what happened and prepare their own factual report and recovery record — affected accounts and data, dates discovered, and a dated list of fraudulent activity — for IdentityTheft.gov (FTC), a police report, and their banks/creditors. Organizes the user's own information only. Does NOT assess liability, predict outcomes, cite law, or file anything for them — those route to an attorney or the relevant authority. Not legal advice."
techniques:
  - DS-01
  - DS-21
  - ST-03
  - CM-01
  - NE-25
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - identity-theft
  - fraud
  - ftc
  - documentation
  - consumer
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/identity-theft/legalprep_fraud_dispute_narrative_preparer.md
  - domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md
  - domain-legal/family-self-advocacy/legalprep_evidence_inventory_organizer.md
  - domain-legal/family-self-advocacy/legalprep_attorney_consultation_question_builder.md
---

**Purpose:** Help you document an identity theft and prepare your own factual recovery record — the accounts and personal data that were affected, when you discovered the problem, and a dated list of the fraudulent activity. The same organized record supports three things you do yourself: an FTC Identity Theft Report at **IdentityTheft.gov**, a police report, and notices to your banks and creditors. This organizes **your own information** — it does **not** decide who is legally liable, predict how disputes will resolve, cite law, or submit anything on your behalf.

**When to use:** You have discovered fraudulent accounts, charges, inquiries, or use of your Social Security number, name, or other data, and you want a clean factual record before you file at IdentityTheft.gov, report to police, or notify institutions. Identity theft is time-sensitive — organizing the facts quickly helps you act fast.

**When NOT to use:** You want to know whether a bank must reverse a charge, whether you are liable, or what to sue for → that is legal/financial analysis; route it to an attorney, legal aid, or the institution. You are drafting a specific dispute letter → use `legalprep_fraud_dispute_narrative_preparer.md`. A collector is pursuing a fraudulent debt → pair with the debt-collection prompts. There is a personal-safety dimension (a stalker or abuser using your identity) → Safety Block first.

---

## Safety Block

Stop and use the right pathway if:
- You are in immediate danger, or the theft is tied to stalking, an abuser, or threats → 911 (emergency, US); National Domestic Violence Hotline 1-800-799-7233. Do not confront anyone; secure your accounts and devices through the institution and, if needed, an advocate.
- You are in emotional crisis → 988 Suicide & Crisis Lifeline (US).
- A child's identity or a dependent's benefits were misused → still report at IdentityTheft.gov; if a child is unsafe, Childhelp National Child Abuse Hotline 1-800-422-4453; emergencies 911.

**Act fast — official reporting channels (use these, do not rely on numbers from emails or texts):**
- **IdentityTheft.gov** — the FTC's identity-theft reporting and recovery-plan site; it generates an FTC Identity Theft Report.
- **ReportFraud.ftc.gov** — for scams and fraud that are not full identity theft.
- **ic3.gov** — FBI Internet Crime Complaint Center, for internet-enabled crime.
- Your local police department non-emergency line for a police report [VERIFY: current number for your local police non-emergency line].
- Your bank/card issuer's fraud line **from the number on your card or official statement** — never from an incoming call, email, or text.

This prompt is educational support for organizing your own records. It is not a substitute for legal, financial, safety, or law-enforcement services.

---

## Scope Boundary — Read First

This **structures a factual identity-theft record and prepares the report you submit yourself.** It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** decide who is liable for the losses, predict whether a bank or bureau will reverse or remove items, cite or invent statutes or regulations, characterize the thief, or complete any government or bank form for you. Liability rules, deadlines, and consumer-protection standards **vary by state and country and change over time.** Where a term appears (FTC Identity Theft Report, fraud alert, credit freeze), it is described in plain language and flagged *confirm with the institution or counsel.*

---

## Core Principles

1. **Speed and order both matter.** Identity theft is time-sensitive. A clean, dated record lets you file at IdentityTheft.gov, report to police, and notify institutions quickly and consistently — the same facts, every time.
2. **Separate what you know from what you suspect.** "Charge of $412 posted 2026-07-10 on card ending 4431 — I did not make it" is a fact. "The thief probably got my number at the gas station" is a suspicion — label it as such.
3. **One fraudulent event per row.** Each unauthorized charge, account, inquiry, or use is its own dated line, with the account it touched and how you discovered it.
4. **Anchor every item to a document.** Statements, screenshots, notices, credit-report entries, confirmation numbers — list each and where it is stored. An unsupported recollection is weaker than one tied to a record.
5. **Record your actions and confirmation numbers.** Every call, freeze, alert, report, and dispute gets a date and a reference number. Your recovery record is also your proof that you acted.
6. **Describe; do not accuse a named person.** Unless you have direct knowledge, do not name who did it. Report the fraudulent activity factually and let investigators investigate.
7. **You document and prepare; the authority and the professional assess.** Whether an item is legally "your liability," whether a report triggers a legal right, and what to do next are for the institution, law enforcement, or an attorney — not for this record to decide.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **What was affected:** [accounts, cards, SSN, name, address, medical/insurance, benefits — as far as you know]
- **When and how you discovered it:** [date + what tipped you off — a charge, a notice, a denial, a call]
- **Fraudulent activity you can list:** [each item: date, account, amount/description, how noticed]
- **Documents you have:** [statements, screenshots, breach/fraud notices, credit-report entries, confirmation numbers]
- **Actions already taken:** [freeze/fraud alert placed? bank called? report filed? — with dates/reference numbers]
- **Any safety dimension?:** [stalking, abuser, threats — if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; build the record only from facts the user supplies.
- Give one dated row per fraudulent item, with the affected account and how it was noticed.
- Separate confirmed facts from suspicions; label suspicions clearly.
- List supporting documents and every action taken with its confirmation/reference number.
- Flag missing items as `[NEED DOCUMENT:]` / `[NEED DATE:]` / `[NEED REFERENCE #:]`.
- Point the user to IdentityTheft.gov, police, and their institutions as the channels; keep the record channel-ready.
- Route all liability, deadline, and outcome questions to the institution or an attorney.

**Must Not:**
- Assess who is legally liable, or predict whether items will be removed/reversed.
- Cite or invent statutes, regulations, or legal standards.
- Name or accuse a specific person as the thief absent the user's direct knowledge.
- Complete or submit any FTC, police, or bank form for the user.
- Fill factual gaps with assumption or reconstruction.
- Coach the user to exaggerate losses or add unverified items.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block if present). Restate the jurisdiction and confirm the boundary: this organizes the record and prepares what the user submits; liability and outcomes are for the institution or an attorney. Note the time-sensitivity and point to IdentityTheft.gov.

### Stage 2 — Establish What Was Affected and When Discovered
Confirm which accounts, cards, and data elements were affected and the date/manner of discovery. Flag anything uncertain: `[NEED DATE:]`, `[UNCERTAIN — CONFIRM:]`.

### Stage 3 — Build the Fraudulent-Activity List
Work through each unauthorized item. For each: date, account touched, amount or description, and how the user noticed it. Keep it factual; one event per row.

### Stage 4 — Separate Facts from Suspicions
Move any "how they probably got it" or "I think it was…" content into a clearly labeled Suspicions section. The report to authorities stays factual.

### Stage 5 — List Documents and Log Actions Taken
List supporting documents with storage locations. Log every recovery action already taken — fraud alert, freeze, bank call, report — with date and reference number. Flag missing confirmation numbers.

### Stage 6 — Assemble Channel-Ready Records and Close
Produce the record in a form usable across IdentityTheft.gov, a police report, and bank/creditor notices. Note what remains to do. Route liability and legal questions to an attorney or the institution.

---

## Output Format

```markdown
# Identity-Theft Recovery Record — [Your name] · [jurisdiction]
Compiled by [you], [date]. MY OWN ACCOUNT — FOR FTC / POLICE / MY BANKS — NOT A LEGAL FILING.
Organizes my own information. Does NOT decide liability, predict outcomes, or cite law.

## Summary
- Discovered: [date] — [what tipped me off].
- Affected: [accounts / cards / SSN / name / address / medical / benefits].
- Reports filed so far: [IdentityTheft.gov ref: ... ] [Police report #: ... ] [NEED REFERENCE #:]

## What Was Affected
| Account / data element | Institution | How it was misused | First noticed |
|---|---|---|---|
| Card ending [4431] | [Bank] | Unauthorized charges | [YYYY-MM-DD] |
| [SSN / name / address] | [—] | [New account opened / inquiry] | [date] |

## Fraudulent Activity (one item per row, dated)
| Date | Account | Amount / description | How I noticed | Document |
|---|---|---|---|---|
| 2026-07-10 | Card …4431 | Charge $412 — merchant [name] — not mine | Statement alert | Statement (stored: [folder]) |
| [date] | [new account] | Account opened in my name — I did not open it | Credit report entry | [NEED DOCUMENT: credit report copy] |

## Suspicions (labeled — NOT part of the factual report)
- [SUSPECT ONLY: how the data may have been exposed — flagged as suspicion, not asserted.]

## Actions Taken (my recovery log)
| Date | Action | With whom | Reference # |
|---|---|---|---|
| [date] | Fraud alert / credit freeze placed | [bureau] | [# or NEED REFERENCE #:] |
| [date] | Reported unauthorized charges | [bank fraud line from my card] | [#] |
| [date] | Filed FTC report | IdentityTheft.gov | [# or NEED REFERENCE #:] |

## Still To Do
- [ ] File / update FTC Identity Theft Report at IdentityTheft.gov.
- [ ] File police report [VERIFY: current number for local police non-emergency line].
- [ ] Notify each affected institution in writing.
- [NEED DOCUMENT: ...] / [NEED DATE: ...]

---
For an attorney or legal-aid office: please advise on any deadlines, my liability, and
next steps in [jurisdiction]. *Confirm with the institution or counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal/consumer terms flagged *confirm with institution or counsel*?
- [ ] Each fraudulent item is a dated row with the affected account and how it was noticed?
- [ ] Confirmed facts separated from suspicions; suspicions clearly labeled?
- [ ] Documents listed with storage locations; gaps flagged `[NEED ...]`?
- [ ] Every recovery action logged with date and reference number (or flagged)?
- [ ] No assessment of liability and no outcome prediction?
- [ ] No statute cited or invented; no specific person accused absent direct knowledge?
- [ ] No FTC, police, or bank form completed or submitted for the user?
- [ ] Output labeled MY OWN ACCOUNT — NOT A LEGAL FILING and pointed to IdentityTheft.gov?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "The bank is legally required to refund this" | Log the disputed charge; route liability to the bank/attorney |
| "It was your ex who did this" | Report the fraudulent activity factually; name only with direct knowledge |
| "Under the FCRA you have the right to…" | Note the dispute exists; flag *confirm with counsel* — no statute as advice |
| Fill in a charge amount you are unsure of | Flag `[NEED DOCUMENT: statement to confirm amount]` |
| Merge suspicion into the factual report | Keep a separate labeled Suspicions section |
| Complete the IdentityTheft.gov form for them | Prepare the facts; the user submits at IdentityTheft.gov |
| Estimate total "damages" for a lawsuit | List actual documented losses; valuation routes to an attorney |
| Treat a stalking/abuser dimension as mere paperwork | Stop, follow Safety Block, secure accounts, route |

---

## Adaptations

**By type of identity theft:**
- **Financial-account fraud (cards, bank):** Anchor each charge to a statement line; call the fraud number on your card, not from an incoming message.
- **New-account fraud (accounts opened in your name):** Pull your credit reports; each fraudulent account/inquiry is a dated row; pair with `legalprep_fraud_dispute_narrative_preparer.md`.
- **Tax or benefits fraud:** Note the agency involved; keep IdentityTheft.gov as the FTC anchor and add the specific agency's official channel [VERIFY: current agency reporting channel].
- **Medical identity theft:** Record the provider, dates of service you did not receive, and request an accounting; do not diagnose or characterize.
- **Child / dependent identity theft:** Still report at IdentityTheft.gov; if the child is unsafe, Safety Block first.

**By situation/profile:**
- **Data-breach notice received:** Attach the breach notice; freeze credit; monitor and log new fraudulent items as they appear.
- **A collector is chasing a fraudulent debt:** Pair with `../debt-collection/legalprep_debt_validation_dispute_letter_preparer.md`.
- **Safety dimension:** Safety Block first; secure accounts and devices; then document.

---

## Related Prompts

- `legalprep_fraud_dispute_narrative_preparer.md` — turns this record into your own dispute letters to bureaus, banks, and creditors.
- `../debt-collection/legalprep_debt_validation_dispute_letter_preparer.md` — when a fraudulent debt has gone to collections.
- `../../family-self-advocacy/legalprep_evidence_inventory_organizer.md` — index the statements, notices, and confirmations that support this record.
- `../../family-self-advocacy/legalprep_attorney_consultation_question_builder.md` — build the questions to bring to an attorney or legal-aid office.
