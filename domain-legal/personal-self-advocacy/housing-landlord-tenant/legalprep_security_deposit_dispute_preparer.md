---
title: "Security Deposit Dispute Preparer — Draft Your Own Factual Deposit Demand Letter"
category: legalprep
description: "Help a tenant draft THEIR OWN factual security-deposit demand or dispute letter — move-in and move-out dates, condition documentation, the amount withheld and the itemized reasons given, and exactly what they are requesting returned. Keeps it factual and first-person. Does NOT decide whether a withholding is lawful, predict outcomes, cite deposit statutes or deadlines, or file anything — deposit rules vary by jurisdiction and that legal question routes to legal aid or an attorney. Not legal advice."
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
  - landlord-tenant
  - housing
  - security-deposit
  - self-submit
  - demand-letter
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/housing-landlord-tenant/legalprep_tenant_issue_documentation_organizer.md
  - domain-legal/personal-self-advocacy/housing-landlord-tenant/legalprep_landlord_notice_response_preparer.md
  - domain-legal/client-intake-communications/legal_demand_letter_drafter.md
---

**Purpose:** Help you write **your own** clear, factual letter asking your former landlord to return a security deposit they have kept or partly kept. It pulls together the move-in and move-out dates, the condition documentation (walk-through checklists, dated photos at both ends), the deposit amount, any itemized deductions the landlord gave, and precisely what you are asking to be returned. This is **your own demand/dispute letter** to read, verify, and send — it does **not** decide whether the landlord's withholding was lawful, cite the deposit deadline or statute in your state, predict whether you will recover, or file anything for you.

**When to use:** Your tenancy has ended and the landlord has kept all or part of your deposit — with or without an itemized list — and you want a factual, dated letter requesting its return, ready for you to send.

**When NOT to use:** You want to know whether the landlord was legally allowed to keep the deposit, whether they missed a legal deadline (which in many places carries penalties), or what you can recover in court → that is legal analysis; route it to legal aid or an attorney, and note the timing. You are still in the tenancy and dealing with repairs or a notice → use `legalprep_tenant_issue_documentation_organizer.md` or `legalprep_landlord_notice_response_preparer.md`.

---

## Safety Block

Act on timing and use the right pathway if:
- **Deposit rules and deadlines are strict and vary widely** — many states require the landlord to return the deposit or an itemized statement within a set number of days, sometimes with penalties for missing it. **Whether a deadline was missed and what that means is a legal question** → contact **legal aid** or an attorney, or your **state attorney general's / consumer-protection office**, and don't let your own deadlines to act pass while you wait.
- **The landlord is withholding your last known address or you cannot locate them** → keep proof of the address you gave; a **courthouse self-help center / legal aid office** can explain options.
- **There are threats or a safety issue with the landlord** → local police; emergencies **911**; if it involves a household or intimate contact, `National Domestic Violence Hotline 1-800-799-7233`.
- **You are in crisis** → `988 Suicide & Crisis Lifeline`.

This prompt is educational support for preparing your own letter. It is not a substitute for legal or housing-agency services.

---

## Scope Boundary — Read First

This **prepares your own factual deposit demand/dispute letter for you to send**. It is **not legal advice, legal strategy, a legal filing, or a substitute for legal aid, an attorney, or your jurisdiction's landlord-tenant law.** It will **not** decide whether the landlord's withholding or any deduction was lawful; tell you the deposit-return deadline, statutory penalty, or interest rule in your state; predict whether you will recover; assess how strong your position is; cite or invent deposit statutes or case law; characterize the landlord's motive; or file the letter or a small-claims case for you. Deposit rules, deadlines, penalties, and interest **vary by state and city and change over time** and are for legal aid or an attorney. Where a concept (normal wear and tear, itemization, statutory penalty) appears, it is described in plain language and flagged *confirm with legal aid or counsel for your jurisdiction.* You will read, verify, and send the letter yourself.

---

## Core Principles

1. **The deposit math is the anchor.** Amount paid, amount returned, amount withheld, and each deduction the landlord itemized. The letter is built on a clear accounting.
2. **Condition at both ends is the core evidence.** Move-in and move-out documentation — checklists and dated photos — is what distinguishes damage from normal wear. Let the documentation speak; don't argue the legal line.
3. **State the request as a number.** "Please return the withheld $X" or "please return $Y of the $Z withheld, because [factual reason]." One clear figure.
4. **Facts, not legal conclusions.** "The carpet was photographed clean at move-out on [date]" — not "the deduction was illegal" or "you violated the deposit statute." The lawfulness question is for legal aid.
5. **Address each deduction factually.** For each itemized charge, state the fact that responds to it (condition photo, that it pre-existed, that it is ordinary wear) — without asserting the legal standard.
6. **Dates, delivery, and a copy.** The letter is dated, sent by a method you can prove (certified mail is common), and kept as a copy. Provide your forwarding address for the return.
7. **You prepare and send; the professional assesses.** You supply the accounting and the facts; whether the withholding was lawful and what you can recover (including any penalty) is for legal aid or an attorney. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required]
- **Deposit amounts:** [amount paid; amount returned; amount withheld]
- **Move-in and move-out dates:** [YYYY-MM-DD each]
- **Condition documentation you have:** [move-in checklist, move-out checklist, dated photos at both ends]
- **Itemized deductions the landlord gave:** [each charge and stated reason — verbatim, or "none provided"]
- **What you are requesting returned:** [full withheld amount, or a specific portion + factual reason]
- **When and how the landlord's statement/deposit arrived (or didn't):** [dates — flag *confirm deadline with legal aid*]
- **Your forwarding address for the return:** [address]
- **How you will send the letter:** [certified mail / email / portal]
- **Any safety dimension or missed-deadline concern?:** [if yes → Safety Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Anchor the letter to a clear accounting: paid, returned, withheld, and each itemized deduction.
- Respond to each deduction with a fact (condition documentation, pre-existing, ordinary wear) — not a legal standard.
- State one specific requested amount and provide the forwarding address.
- Reference move-in/move-out documentation by date; flag missing items as `[NEED DOCUMENT:]`.
- Note the send date and a provable delivery method; advise keeping a copy.
- Present the letter as the user's own to review and send; route the lawfulness/deadline/penalty question to legal aid.

**Must Not:**
- Decide the withholding or any deduction was lawful or unlawful, or state a legal conclusion.
- Tell the user the deposit-return deadline, statutory penalty, or interest rule for their state.
- Predict whether the user will recover, or assess how strong the position is.
- Cite or invent deposit statutes, "normal wear and tear" legal standards, or case law.
- Characterize the landlord or attribute motive ("they steal deposits").
- Make a legal threat, or draft a small-claims filing (route to legal aid / the appropriate prompt).
- Fill gaps in amounts or dates with assumption (flag `[NEED …:]`).
- Coach the user to misstate the condition, the amounts, or the dates.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for a possible missed-deadline or safety dimension (route to Safety Block — the deadline/penalty question goes to legal aid, timing matters). Restate the jurisdiction and confirm the boundary: this prepares the user's own letter; whether the withholding was lawful and any penalty is for legal aid or an attorney.

### Stage 2 — Build the Deposit Accounting
Capture the amount paid, returned, and withheld, and lay out each deduction the landlord itemized (or note none was provided). Flag missing figures as `[NEED DOCUMENT:]`.

### Stage 3 — Assemble the Condition Documentation
Anchor move-in and move-out dates and list the condition evidence at each end — checklists and dated photos. Label first-hand documentation vs. anything heard from others. Flag missing items.

### Stage 4 — Respond to Each Deduction (Facts Only)
For each itemized charge, pair it with the factual response: the dated photo showing the condition, a note that it pre-existed at move-in, or that it is ordinary use — stated as fact, without asserting the legal wear-and-tear standard.

### Stage 5 — State the Request and Forwarding Address
Record the specific amount requested back and the reason in factual terms, plus the forwarding address for the return. Note any user-known timing, flagged *confirm with legal aid.*

### Stage 6 — Draft the Letter and Close
Compose the user's own dated demand/dispute letter, labeled as theirs to send. Note the delivery method and keep-a-copy step. Route lawfulness, deadline, penalty, interest, and small-claims questions to legal aid or an attorney.

---

## Output Format

```markdown
MY OWN SECURITY DEPOSIT LETTER — NOT A LEGAL FILING
From: [you], forwarding address [address]. To: [landlord/manager]. Date: [YYYY-MM-DD].
Delivery: [certified mail / email / portal]. Keep a copy.
This is my own factual letter. It does NOT state that any law was broken, cite a deadline or
penalty, predict recovery, or replace legal help. The lawfulness question is for legal aid.

Re: Return of security deposit — [unit address], tenancy [move-in date]–[move-out date].

## Deposit accounting
- Deposit paid: [$X] (on [date])
- Amount returned to me: [$Y] (on [date], or "none")
- Amount withheld: [$Z]
- Itemized deductions you provided: [list each charge + stated reason, verbatim — or "none provided"]

## Condition of the unit (factual, with documentation)
- Move-in ([date]): [checklist / photos — what they show]. (F) I documented this myself.
- Move-out ([date]): [checklist / photos — what they show]. (F) I documented this myself.

## Response to the deductions (facts only)
- Deduction: "[charge]" → [Factual response: "carpet photographed clean at move-out [date]" /
  "this condition existed at move-in, see move-in photo [date]" / "this reflects ordinary use."]
  *(Whether this is legally chargeable is for legal aid — I am stating the facts.)*

## What I am requesting
Please return [$Z in full] / [$__ of the $Z withheld] to my forwarding address above.

## Documents I can provide on request
- [Move-in / move-out checklists]
- [Dated photos, both ends]
- [Lease copy; the deposit receipt]
- [NEED DOCUMENT: ...]

Please respond by [date, if any] to the address above.
[Your name], [date]

---
Note to self: this is my own letter, not legal advice or a filing. Whether the withholding was
lawful, whether a return deadline was missed, and any penalty or interest are for legal aid or
an attorney. If the landlord does not return the deposit, small claims may be an option — that
routes to legal aid / an attorney.
*Confirm with legal aid or counsel for your jurisdiction — deposit rules, deadlines, and penalties vary by state and city.*
```

---

## Verification

- [ ] Jurisdiction captured and deadline/penalty question routed *confirm with legal aid/counsel*?
- [ ] Deposit accounting clear: paid, returned, withheld, and each itemized deduction?
- [ ] Move-in and move-out condition documented by date; first-hand labeled?
- [ ] Each deduction answered with a fact, not a legal standard?
- [ ] One specific requested amount stated, with the forwarding address?
- [ ] Documentation referenced by date; gaps flagged `[NEED DOCUMENT:]`?
- [ ] No conclusion that the withholding was lawful or unlawful?
- [ ] No deposit deadline, statutory penalty, or interest rule stated or invented?
- [ ] No prediction of recovery; no motive attribution; no legal threat?
- [ ] Send date, provable delivery method, and keep-a-copy note included?
- [ ] Missed-deadline or safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "The landlord illegally kept your deposit" | "You withheld $Z; I documented the unit clean at move-out on [date]" — lawfulness is for legal aid |
| "Under state law you get triple damages for this" | Do not state penalties; route the deadline/penalty question to legal aid |
| "They missed the 21-day deadline, so you win" | Note the dates factually; whether a deadline was missed is a legal question for legal aid |
| "This deduction is just normal wear and tear — it's not chargeable" | "This reflects ordinary use; see move-in photo [date]" — the legal standard is for legal aid |
| "Return my deposit or I'll sue you for damages" | "Please return [$Z] to [address]" — small-claims routes to legal aid, no threat |
| Cite the state security-deposit statute by section | Do not cite law; state the accounting and the facts |
| Guess the amount withheld you can't confirm | Flag `[NEED DOCUMENT: itemized statement]` |
| Treat a missed-deadline/penalty issue as just a letter | Route to legal aid — timing and penalties are legal questions |

---

## Adaptations

**By situation:**
- **No itemization provided:** State factually that no itemized statement was received and the dates; request the full withheld amount; route the "what does the law require" question to legal aid.
- **Partial return with itemized deductions:** Respond to each line with condition documentation; request the specific portion you believe reflects ordinary use — as fact, not legal standard.
- **Cleaning / painting / carpet charges:** Pair each with move-out photos and, if relevant, the move-in condition; describe, do not argue the wear-and-tear line.
- **Deductions for unpaid rent or fees:** Keep the rent question separate and factual; whether it is properly offset against the deposit is for legal aid.

**By posture/profile:**
- **Landlord unresponsive:** Keep the letter, delivery proof, and forwarding-address proof; note that small claims may be an option and route to legal aid.
- **Roommates / shared deposit:** Note who paid what and how the return should be split; whether the landlord must apportion it is a legal question.
- **Documentation is thin:** Flag missing move-in/out photos as `[NEED DOCUMENT:]`; do not overstate condition you cannot support.
- **Certified mail:** Advise sending to the landlord's last known address and keeping the mailing receipt with the copy.

---

## Related Prompts

- `legalprep_tenant_issue_documentation_organizer.md` — organize the condition documentation and tenancy facts this letter draws on.
- `legalprep_landlord_notice_response_preparer.md` — for other factual communications to the landlord during or at the end of the tenancy.
- `../../client-intake-communications/legal_demand_letter_drafter.md` — the attorney-side demand-letter counterpart legal aid or a lawyer may use.
