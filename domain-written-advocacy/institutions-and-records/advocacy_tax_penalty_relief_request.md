---
title: "Tax Penalty Relief Request — Ask a Tax Authority to Remove or Reduce a Penalty"
category: advocacy
description: "[SELF-SUBMIT] Help an individual taxpayer draft THEIR OWN written request asking a tax authority to remove or reduce a penalty on a notice — quoting the notice verbatim, stating the circumstances and compliance history factually, and mapping them to relief criteria the user has read in the authority's OWN published guidance rather than to rules supplied from memory. Screens for enforcement action, professional-representation triggers, and deadlines first. Does NOT cite tax code, name or describe relief programmes as rules, state eligibility, deadlines, or interest treatment, compute tax, predict the outcome, or invent notice details. Distinct from advocacy_fee_waiver_request (private-sector goodwill) and domain-legal/tax/ (professional-side). Not tax or legal advice."
techniques:
  - CM-01
  - CM-02
  - DS-21
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - tax
  - penalty-relief
  - self-submit
  - government
updated: "2026-09-24"
related_prompts:
  - domain-written-advocacy/financial-hardship/advocacy_fee_waiver_request.md
  - domain-written-advocacy/institutions-and-records/advocacy_benefits_denial_appeal.md
  - domain-written-advocacy/cross-cutting/advocacy_correspondence_log_builder.md
  - domain-written-advocacy/financial-hardship/advocacy_payment_arrangement_proposal.md
---

**Purpose:** Help you write **your own** request asking a tax authority to remove or reduce a penalty shown on a notice — for filing late, paying late, or a similar penalty. It quotes the notice exactly, sets out what happened and your compliance history as plain facts, and connects them to the relief criteria **you have read in the authority's own published guidance** — because relief categories, their names, and their conditions differ by country and change, and a letter built on a remembered rule can be refused on a technicality.

**When to use:** You have a written notice showing a penalty, the underlying tax is correct or has been corrected, and something specific explains the lateness — or your record before this was clean.

**When NOT to use:** You disagree with the **tax itself**, not the penalty → that is an assessment dispute; route to a tax professional. The notice mentions levy, garnishment, seizure, lien, or court → the Boundary & Routing Block, first. You run a business with payroll or sales-tax penalties → route to a tax professional; those carry different stakes. A private company charged you a fee → `../financial-hardship/advocacy_fee_waiver_request.md`.

---

## Boundary & Routing Block

Use a different pathway if:
- **The notice mentions enforcement — levy, garnishment, seizure, lien, a final notice, or a court** → contact a **tax professional, legal aid, or a low-income taxpayer service** now `[VERIFY: locate a free or low-cost taxpayer assistance service in your jurisdiction from an official government source]`. A relief letter does not pause enforcement unless the authority says it does.
- **The notice gives a response deadline** → **act on the date printed on the notice.** Whether other deadlines exist is a question for a tax professional, not this prompt.
- **You dispute the tax owed, or the return itself was wrong** → correct the return or dispute the assessment first, through the route the authority names; penalty relief is a separate request.
- **Fraud, undisclosed income, or foreign accounts are involved** → route to a tax professional or attorney before writing anything.
- **You cannot pay the underlying balance** → ask separately about payment options; see `../financial-hardship/advocacy_payment_arrangement_proposal.md` for the shape, and the authority's own published options.

This prompt is educational support for preparing your own correspondence. It is not a substitute for a tax professional or an attorney.

---

## Scope Boundary — Read First

This **drafts your own written penalty relief request for you to send**. It is **not tax advice, legal advice, a legal filing, or a substitute for a tax professional or your jurisdiction's law.** It will **not** cite a tax code section, regulation, or manual provision; name a relief programme or describe its conditions as if they were rules; tell you whether you qualify; state a response deadline, a statute of limitations, or how interest is treated if a penalty is removed; calculate tax, penalty, or interest; tell you whether the authority applied the penalty correctly; predict the outcome; name a taxpayer advocate or ombudsman office from memory; or invent a notice number, tax year, amount, or date. Tax rules **vary by country, state, and year and change frequently.** Where such a concept appears it is flagged *verify with the tax authority's own published guidance*.

---

## Core Principles

1. **The notice is the anchor.** Quote the notice number, tax period, penalty type, and amount exactly as printed. A relief request that does not match the notice gets matched to the wrong account or returned.
2. **The authority's own guidance is the only rulebook.** Most tax authorities publish how they consider penalty relief. Read it, and quote the criteria you are relying on — by the authority's own heading or page — in your own words. The prompt does not supply criteria.
3. **Facts, dates, and documents — not hardship language.** "I was admitted to hospital on [date] and discharged on [date]; the return was filed on [date]" does more than a paragraph about a difficult year.
4. **Show the cause ended and you acted.** Relief requests are usually read for what happened, when it stopped, and how quickly you complied after. Include the compliance date.
5. **Record your history honestly.** A clean prior record is worth stating; prior penalties or relief should be recorded rather than omitted.
6. **Fix the underlying return first.** A penalty request on an unfiled return or unpaid balance is weaker and may not be considered — file and pay, or arrange to, before asking.
7. **Keep it separate from a tax dispute.** "Remove the penalty" and "the tax is wrong" are different requests to potentially different teams.

---

## Your Input

- **Your jurisdiction (country and state/province):** [required]
- **Notice details, verbatim:** [notice number/type, date, tax period, penalty description, amount]
- **Any response date printed on the notice:** [YYYY-MM-DD — act on it]
- **Any enforcement language on the notice?:** [if yes → Boundary & Routing Block]
- **Is the underlying return filed and the tax paid or arranged?:** [yes / no / partly]
- **What happened:** [factual cause, with start and end dates]
- **When you complied after the cause ended:** [filing date, payment date]
- **Documents supporting the cause:** [hospital record, death certificate, disaster notice, authority's own error letter]
- **Prior compliance history:** [prior penalties, prior relief granted, years filed on time]
- **The authority's published relief criteria you read:** [heading or page title, date read, your own summary] or [NOT YET READ]
- **Prior contact:** [date, channel, reference, outcome]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts, notice text, and documents the user supplies.
- Screen for enforcement language, fraud or undisclosed income, and an assessment dispute first, and route.
- Record the notice fields verbatim and tell the user to act on any printed date.
- Require the user to read the authority's own published relief guidance; where not yet read, direct them to find it `[VERIFY: the tax authority's own published penalty relief guidance]` before sending.
- Present any criteria as the user's own summary of the guidance they read, with where they read it.
- State the cause, its dates, and the compliance date factually, each matched to a document or `[NEED DOCUMENT:]`.
- Record compliance history, including prior penalties or relief.
- Include a Sending Log and label the output `MY OWN REQUEST — NOT A LEGAL FILING`.

**Must Not:**
- Cite a tax code section, regulation, manual, ruling, or programme name as authority.
- State relief criteria, eligibility, or that the user qualifies.
- State a deadline, limitations period, or interest consequence.
- Calculate any tax, penalty, or interest figure.
- Assert the penalty was wrongly applied.
- Name a taxpayer advocate, ombudsman, or assistance body from memory.
- Predict the outcome or assess the request's strength.
- Invent a notice number, tax period, amount, or date, or embellish the cause.

---

## Instructions

### Stage 1 — Screen and Frame
Screen for enforcement language, fraud or undisclosed income, and a dispute about the tax itself → route. Record any printed response date and tell the user to act on it. Confirm whether the return is filed and the balance paid or arranged.

### Stage 2 — Transcribe the Notice
Record notice number, date, tax period, penalty description, and amount exactly as printed. Flag anything the user cannot read off the notice `[NEED DOCUMENT: copy of the notice]`.

### Stage 3 — Anchor to the Authority's Own Guidance
Ask the user which published relief criteria they read and where. Record their own summary with the heading or page title and the date read. If they have not read it, stop and direct them to find it before sending.

### Stage 4 — Build the Factual Account
Lay out cause, start date, end date, compliance date, and the document for each. Add compliance history. Keep hardship description to facts.

### Stage 5 — Draft the Request and Close
Compose the user's dated letter against the notice, with a specific ask (remove or reduce the named penalty) and a request for a written decision with reasons. Add the Sending Log.

---

## Output Format

```markdown
MY OWN PENALTY RELIEF REQUEST — NOT A LEGAL FILING
From: [your name], [taxpayer ID as the notice shows it — last digits only if sending by email],
[address]. To: [the tax authority, at the address or channel printed on the notice].
Date: [YYYY-MM-DD]. Delivery: [method the notice specifies]. Keep a copy.
This is my own request. It does NOT cite tax law, claim that I qualify for relief, or dispute the
tax assessed.

Re: Notice [#] dated [YYYY-MM-DD] — tax period [period] — penalty "[description as printed]" [$X]

## What I am asking
I ask you to consider removing [or reducing] the penalty shown above.

## What happened
| Date | Event | Document enclosed |
|---|---|---|
| [YYYY-MM-DD] | [cause began — e.g. hospital admission] | [discharge summary] |
| [YYYY-MM-DD] | [cause ended] | [...] |
| [YYYY-MM-DD] | Return filed / tax paid | [confirmation] |

## My compliance history
[e.g. "I have filed and paid on time for [n] prior periods. I have not previously received
relief." — or record prior penalties and relief honestly.]

## The guidance I read
I read your published guidance "[heading / page title]" on [YYYY-MM-DD]. My understanding of it,
in my own words, is: [user's own summary]. I have set out the facts above so you can consider them
against it.

Please send me a written decision with the reasons, and tell me what I can do if you do not grant
this request. If you need further documents, please tell me which.
[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Outcome |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [address on notice] | [#] | [receipt] | [date on notice] | [ ] |

Note to self: I will act on the date printed on the notice. Whether I qualify, and anything about
interest or deadlines, is for a tax professional — `[VERIFY: locate taxpayer assistance for my
jurisdiction from an official government source]`. *Verify with the tax authority's own guidance.*
```

---

## Verification

- [ ] Enforcement, fraud/undisclosed income, and tax-dispute dimensions screened and routed?
- [ ] Printed response date recorded and the user told to act on it?
- [ ] Notice fields transcribed verbatim?
- [ ] Relief criteria come only from the user's own reading of the authority's guidance, cited by heading and date?
- [ ] Cause, end date, and compliance date each matched to a document or `[NEED DOCUMENT:]`?
- [ ] Compliance history recorded honestly, including prior relief?
- [ ] No tax code, programme name, eligibility rule, deadline, or interest treatment asserted?
- [ ] No calculation of tax, penalty, or interest?
- [ ] No body named from memory; `[VERIFY:]` used?
- [ ] No outcome prediction; Sending Log included?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You qualify for first-time abatement under [programme]" | Quote the user's own summary of the guidance they read; state no eligibility |
| "Under section [#], reasonable cause requires…" | Cite no code; facts and dates only |
| "Interest will be removed along with the penalty" | Say nothing about interest; route to a tax professional |
| "Your penalty should be about $X less" | Calculate nothing; quote the notice amount |
| "Contact the [named advocate office]" | `[VERIFY: locate taxpayer assistance from an official source]` |
| "It was a very stressful year" | "Admitted [date], discharged [date]; filed [date]" with documents |
| Omit a penalty relieved two years ago | Record it; omissions undermine the request |
| Draft while the notice mentions a levy | Stop — tax professional or legal aid now |

---

## Adaptations

**By cause:**
- **Serious illness or death in the family:** Dates of the event and of recovery or bereavement period, and the filing date after; a clinical or official document for each.
- **Disaster or records destroyed:** The event date and location, what records were lost, and when replacements were obtained.
- **Relied on the authority's own wrong information:** The written answer you received, with its date and reference — a phone answer should be recorded with date, time, and any reference number.
- **Clean history, no specific cause:** State the history plainly and ask whether the authority's published guidance provides for relief on that basis — as a question.

**By situation:**
- **A preparer caused the lateness:** Record facts only; whether that affects relief is for a tax professional.
- **Refused once:** Ask what review route the decision letter names, and log it with `../cross-cutting/advocacy_correspondence_log_builder.md`.

---

## Related Prompts

- `../financial-hardship/advocacy_fee_waiver_request.md` — the private-sector equivalent for bank and card fees.
- `advocacy_benefits_denial_appeal.md` — the pattern for appealing a government decision once one is made.
- `../cross-cutting/advocacy_correspondence_log_builder.md` — to keep the record while the request is pending.
- `../financial-hardship/advocacy_payment_arrangement_proposal.md` — the shape of a budget-based instalment proposal.
