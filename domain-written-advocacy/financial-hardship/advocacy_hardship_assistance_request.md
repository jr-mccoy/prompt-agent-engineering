---
title: "Hardship Assistance Request — Ask a Lender or Servicer for Temporary Relief"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN written request for temporary hardship assistance — forbearance, deferment, reduced payments, or a hold on collection activity — stating the cause, its expected duration, what they can sustain, and asking for the programme's terms in writing before accepting. Does NOT cite lending or servicing regulation as authority, state what a lender must offer, tell the user what a programme will do to their credit file or balance, predict approval, or invent programme names or figures. Not legal or financial advice."
techniques:
  - CM-01
  - DS-01
  - DS-21
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - financial-hardship
  - forbearance
  - self-submit
  - consumer
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/financial-hardship/advocacy_payment_arrangement_proposal.md
  - domain-written-advocacy/financial-hardship/advocacy_fee_waiver_request.md
  - domain-written-advocacy/financial-hardship/advocacy_interest_rate_reduction_request.md
  - domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md
---

**Purpose:** Help you write **your own** dated request to a lender, servicer, or creditor for temporary hardship assistance — a pause, a reduction, a deferral, or a hold on collection while circumstances change. It states what happened, how long you expect it to last, what you can realistically sustain in the meantime, and asks for the full terms of anything offered **in writing before you accept it**.

**When to use:** Something has changed — job loss, reduced hours, illness, a death, a separation, a disaster — and you cannot maintain payments for a period you expect to be temporary, and you want the request and any offer documented.

**When NOT to use:** The difficulty is permanent rather than temporary, or debts across several creditors are unmanageable → see the Boundary & Routing Block; a nonprofit credit counsellor is the better first call. You want a permanently lower rate → `advocacy_interest_rate_reduction_request.md`. You want a specific instalment plan on an arrears balance → `advocacy_payment_arrangement_proposal.md`. A collector is pursuing you and you are unsure the debt is yours → `domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md` first.

---

## Boundary & Routing Block

Use a different pathway if:
- **The difficulty is not temporary, or debts across several creditors are unmanageable together** → a single hardship letter will not address it, and the sequence in which you approach creditors and options matters. Speak to a **nonprofit credit counselling service** `[VERIFY: locate an accredited nonprofit service in your jurisdiction from an official or government source — do not rely on a name from memory, and be aware that paid "debt relief" firms advertise heavily alongside genuine nonprofits]`.
- **You are considering bankruptcy, insolvency, or a formal debt procedure, or one has been suggested to you** → that is a legal decision with long consequences and strict ordering. Route to an attorney, **legal aid**, or a nonprofit credit counsellor before making arrangements with individual creditors, because some arrangements affect later options.
- **The debt is secured against your home or vehicle, and repossession or foreclosure has been mentioned** → this is time-critical and dedicated help usually exists. Route immediately to an attorney, legal aid, or a housing counselling service `[VERIFY: locate the appropriate service for your jurisdiction from an official government source]`. Do not rely on correspondence alone while a process is running.
- **You are being sued, or have received a court document about a debt** → route to an attorney or legal aid immediately; deadlines in court documents are strict and a hardship letter does not address them.
- **The stress is affecting your health or safety** → financial distress is a recognised risk factor. Speak to someone. `[VERIFY: locate the current crisis support line for your country from an official source.]` If you are in immediate danger, contact emergency services.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal, financial, or counselling services.

---

## Scope Boundary — Read First

This **drafts your own written hardship request for you to send**. It is **not legal advice, financial advice, debt counselling, a legal filing, or a substitute for an attorney, a nonprofit credit counsellor, or your jurisdiction's law.** It will **not** tell you what assistance a lender is required to offer, or that any programme exists; cite or quote a lending, servicing, mortgage, or consumer-protection regulation as authority; name a specific hardship programme, government scheme, or relief option; tell you how any arrangement will affect your credit file, your balance, the interest you will pay, or your later options; tell you whether to prioritise one debt over another; predict whether the request will be approved; assess how strong your case is; or invent a programme name, figure, income amount, or account detail. What is available **varies by lender, product, state, and country and changes over time.** Where a concept appears it is flagged *verify with your lender and a nonprofit counsellor*.

---

## Core Principles

1. **Ask early, and ask in writing.** Assistance options generally narrow as an account moves further into arrears. A request made before the first missed payment is a different conversation from one made after four, and the written record dates when you asked.
2. **State the cause, its start, and its expected duration.** "Hours reduced from 38 to 20 from [date]; my employer expects this to last until [date]" gives a servicer something to assess. "Things are difficult right now" does not.
3. **Offer what you can actually sustain, not what sounds cooperative.** A hardship arrangement you cannot meet fails twice — you default again, and the next request is harder. Build the figure from an honest budget and offer that.
4. **Ask for the full terms in writing before accepting anything.** This is the part people skip and regret. Interest during the period, what happens to deferred amounts, whether they capitalise, how it is reported, and what happens at the end. Ask all five, every time.
5. **Never assume how it will be reported or what it will cost.** Arrangements differ enormously between lenders and products. Ask the lender to state it and verify with a counsellor — do not accept a general assurance from anyone, including this prompt.
6. **Keep the paperwork ready but do not overshare.** Lenders usually ask for evidence — a termination letter, payslips, a benefit award. Have it ready; supply what their process asks for rather than volunteering a complete financial history unprompted.
7. **You request and document; the professional handles strategy.** Which debts to prioritise, whether an arrangement forecloses a better option, and whether a formal procedure fits are for a counsellor or an attorney. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required]
- **Lender / servicer and product:** [name, loan or card type]
- **Account identifiers:** [account #, loan #, name on account]
- **Is the debt secured on your home or vehicle?:** [if yes → Boundary & Routing Block]
- **Current status:** [up to date / [n] payments behind / in collections]
- **Normal payment:** [$X per period, due on [day]]
- **What changed:** [cause — job loss, reduced hours, illness, bereavement, separation, disaster]
- **When it started:** [YYYY-MM-DD]
- **How long you expect it to last:** [estimate, and what it depends on]
- **What you can sustain during the period:** [$X per period, or nothing for [n] months]
- **Evidence you can supply:** [termination letter, payslips, medical note, benefit award]
- **Other debts and creditors:** [list — if several are unmanageable → Boundary & Routing Block]
- **Prior contact on this:** [dates, channel, reference numbers, what was said]
- **Any court document, repossession threat, or health/safety concern?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Screen **first** for multi-creditor unmanageability, secured-debt repossession risk, court documents, insolvency questions, and health or safety concerns, and route each before drafting.
- State the cause, start date, and expected duration of the hardship.
- Base any offered payment on what the user says they can sustain, and say plainly that an unaffordable offer helps nobody.
- Ask for the full terms of any assistance in writing before acceptance, covering: interest during the period, treatment of deferred amounts, capitalisation, credit reporting, and what happens at the end.
- Ask the lender what evidence its process requires, rather than attaching a full financial history unprompted.
- Route credit-file, prioritisation, and strategy questions to a nonprofit counsellor or an attorney.
- Flag every support service as `[VERIFY: ...]` with no names or numbers from memory.
- Include a Sending Log and label the output `MY OWN REQUEST — NOT A LEGAL FILING`.

**Must Not:**
- State that any hardship programme exists, is required, or must be offered.
- Cite or invent a lending, servicing, mortgage, or consumer-protection regulation.
- Name a specific hardship programme, government scheme, or relief option.
- State how an arrangement will affect the user's credit file, balance, or total interest.
- Tell the user which debts to prioritise, or whether to pay one creditor over another.
- Advise stopping payments, or suggest that non-payment strengthens a request.
- Predict approval, terms, or duration, or assess how strong the case is.
- Recommend a specific debt-relief, consolidation, or settlement company.
- Invent an income figure, balance, payment amount, or account detail.
- Suggest an arrangement without the user confirming they can sustain it.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for: several creditors unmanageable together; a secured debt with repossession or foreclosure mentioned; any court document; a bankruptcy or insolvency question; and health or safety impact → route each per the Boundary & Routing Block **before** drafting. Restate the jurisdiction and the boundary: this drafts a request; strategy is for a nonprofit counsellor or an attorney.

### Stage 2 — Establish the Hardship Clearly
Capture the cause, its start date, its expected duration, and what the duration depends on. Keep it factual and specific — a servicer assesses a dated, bounded change far more readily than a general statement of difficulty. Flag missing dates as `[NEED DATE:]`.

### Stage 3 — Set the Sustainable Offer
Work from what the user says they can actually pay during the period — including nothing, where that is the truth. State explicitly that the figure must be one they can meet, because a failed arrangement narrows what comes next. Do not propose a figure the user has not confirmed.

### Stage 4 — Build the Questions That Must Be Answered Before Accepting
Assemble the five questions: interest during the period; what happens to deferred payments; whether they are capitalised; how the arrangement is reported to credit bureaus; and what happens at the end of the period. Frame all five as questions to the lender, never as assumed answers.

### Stage 5 — Prepare the Evidence Position
Ask the lender what its process requires and note what the user can supply. Caution against volunteering a complete financial history unprompted. Where the lender has a standard hardship form, ask for it rather than substituting a letter.

### Stage 6 — Draft the Request and Close
Compose the user's own dated request, labeled as theirs to send, with the Sending Log. Add the instruction not to accept any offer before the five questions are answered in writing and, where the amounts are significant, checked with a nonprofit counsellor. Route strategy, credit-file, and legal questions onward.

---

## Output Format

```markdown
MY OWN HARDSHIP ASSISTANCE REQUEST — NOT A LEGAL FILING
From: [your name], [contact]. To: [lender / servicer, hardship or collections channel].
Date: [YYYY-MM-DD]. Delivery: [portal / designated email / certified mail]. Keep a copy.
This is my own request. It does NOT state what you are required to offer, cite any regulation,
assume how any arrangement will be reported or what it will cost me, or predict your decision.
I understand nothing here is legal or financial advice.

Re: Request for temporary hardship assistance — account [NEED ACCOUNT #: from your statement]

## My account
- Name on account: [name] · Account: [#] · Product: [loan / card / mortgage / other]
- Normal payment: [$X per period], due [day]
- Current status: [up to date / [n] payments behind]

## What has changed
| Item | Detail |
|---|---|
| What happened | [job loss / hours reduced from X to Y / illness / bereavement / separation] |
| Start date | [YYYY-MM-DD] |
| Expected duration | [estimate] |
| What that depends on | [return to work / treatment ending / new role starting] |

## What I can sustain during this period
I can pay [$X per period] / [nothing] for approximately [n] months from [YYYY-MM-DD].

I have set this figure at what I believe I can actually meet. I would rather agree something
sustainable than agree a larger amount and default on it again.

## What I am asking for
Please tell me what temporary assistance is available on this account, and consider
[a reduced payment of $X / a pause of [n] months / a deferral / a hold on collection activity]
for the period above.

## Before I accept anything, please confirm in writing
1. Whether interest continues to accrue during the arrangement, and at what rate.
2. What happens to the payments that are reduced or paused — are they added to the end,
   spread over later payments, or due as a lump sum?
3. Whether any deferred interest or arrears is capitalised into the balance.
4. How the arrangement will be reported to credit reference agencies.
5. What happens at the end of the period, and what my payment will be then.

## Evidence
Please tell me what evidence your process requires and how to submit it securely.
I can provide: [termination letter / payslips / medical note / benefit award].
I am not attaching financial documents to this letter.

## Prior contact
| Date | Channel | Reference | What was said |
|---|---|---|---|
| [YYYY-MM-DD] | [phone] | [#] | [substance] |

Please respond in writing by [date].
[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Terms received in writing? |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [channel] | [#] | [receipt] | [YYYY-MM-DD] | [ ] |

**I will not accept any offer until all five questions above are answered in writing.**
Where the amounts are significant, I will check the answers with a nonprofit credit counsellor
`[VERIFY: locate an accredited nonprofit service in my jurisdiction from an official or
government source]` before agreeing.

Note to self: this is my own request, not legal or financial advice. What any arrangement does to
my credit file, my balance, and my later options — and which debts to prioritise — are questions
for a nonprofit credit counsellor or an attorney, not for this letter or for the lender's
salesperson.
*Verify for your jurisdiction — what is available varies by lender, product, state, and country.*
```

---

## Verification

- [ ] Multi-creditor, secured-debt, court-document, insolvency, and health/safety dimensions screened **first** and routed?
- [ ] Jurisdiction captured and strategy routed *verify with a nonprofit counsellor or attorney*?
- [ ] Cause, start date, expected duration, and what it depends on all stated?
- [ ] Offered payment based on what the user confirmed they can sustain, with the reasoning stated?
- [ ] All five pre-acceptance questions included — interest, deferred amounts, capitalisation, reporting, end of period?
- [ ] Evidence handled by asking what their process requires, without attaching a full financial history?
- [ ] No claim that any programme exists, is required, or must be offered?
- [ ] No lending, servicing, or mortgage regulation cited or invented?
- [ ] No specific programme, scheme, or relief option named?
- [ ] No statement about credit-file effect, balance effect, or total interest?
- [ ] No prioritisation advice, and no suggestion to stop paying?
- [ ] No approval prediction or strength assessment?
- [ ] No debt-relief, consolidation, or settlement company recommended?
- [ ] Every support service flagged `[VERIFY:]` with nothing from memory?
- [ ] Do-not-accept-before-written-terms instruction included?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You qualify for forbearance — they have to offer it" | Ask what is available; state no entitlement and name no programme |
| "This won't affect your credit score" | Ask them how it will be reported; never state the effect |
| "The interest is usually paused during hardship" | Ask whether interest accrues; assume nothing about terms |
| "Call the National Debt Helpline on [number]" | `[VERIFY: locate an accredited nonprofit service from an official source]` |
| "Stop paying and they'll take you more seriously" | Never advise stopping payment; it typically narrows the options |
| "Pay the credit card first and let the car loan slide" | Give no prioritisation advice; route to a nonprofit counsellor |
| Propose $300 a month because it sounds reasonable | Use only the figure the user confirmed they can sustain |
| "Sign the arrangement they offered on the phone" | Get all five answers in writing before accepting anything |
| "A debt consolidation loan would solve this" | Recommend no product or company; route to a nonprofit counsellor |
| Draft a hardship letter while a foreclosure notice is live | Stop, use the Boundary & Routing Block, get help immediately |

---

## Adaptations

**By product:**
- **Credit card or unsecured loan:** Ask specifically whether the arrangement closes the account or reduces the limit, and what happens to the rate afterwards.
- **Mortgage or secured loan:** Route to a housing counselling service or an attorney **alongside** the letter; secured debt has consequences correspondence cannot manage on its own.
- **Vehicle finance:** Ask what happens if the arrangement fails and on what timescale, and route the repossession question to an attorney rather than assuming.
- **Student or education loans:** Terms differ sharply between products and lenders; ask what is available on this specific loan rather than assuming any general option applies.

**By cause:**
- **Job loss or reduced hours:** State the date, the change in income, and whether a return is expected; a termination letter or revised contract is the usual evidence.
- **Illness or injury:** State the expected duration and what it depends on, without disclosing more medical detail than their process requires.
- **Bereavement or separation:** Note that account ownership or income may be changing and ask what documents they need; these often need a different team.
- **Disaster or emergency:** Ask whether any temporary measures apply to your area — as a question, not an assumption.

**By situation/profile:**
- **Not yet behind:** Say so; asking before default is materially different and worth stating in the letter.
- **Already several months behind:** Include the arrears figure, ask what options remain at this stage, and consider a counsellor first.
- **Several creditors:** Boundary & Routing Block — a counsellor should shape the order and the approach before individual letters go out.
- **Previous arrangement failed:** Say so plainly, say why, and set the new figure lower rather than repeating the one that failed.

---

## Related Prompts

- `advocacy_payment_arrangement_proposal.md` — a structured instalment offer on arrears, with a budget basis.
- `advocacy_fee_waiver_request.md` — to ask for fees charged during the difficulty to be waived.
- `advocacy_interest_rate_reduction_request.md` — for a permanent rate reduction rather than temporary relief.
- `advocacy_goodwill_adjustment_request.md` — to ask about a late mark already reported.
- `../../domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md` — if a collector is involved and the debt is unverified.
