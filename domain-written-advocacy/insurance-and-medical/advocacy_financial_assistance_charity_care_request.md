---
title: "Financial Assistance & Charity Care Request — Ask Before You Agree to Pay"
category: advocacy
description: "[SELF-SUBMIT] Help a person request a healthcare provider's financial assistance or charity care programme — asking for the policy and application form, submitting an income and household summary, and requesting a hold on billing and collection while the application is assessed. Emphasises asking before agreeing to instalments. Does NOT cite hospital assistance or nonprofit obligations as authority, state eligibility thresholds, promise reduction, predict outcomes, or invent income or policy details. Not legal, financial, or medical advice."
techniques:
  - CM-01
  - DS-01
  - ST-02
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - medical-billing
  - financial-assistance
  - self-submit
  - consumer
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/insurance-and-medical/advocacy_medical_bill_dispute.md
  - domain-written-advocacy/financial-hardship/advocacy_payment_arrangement_proposal.md
  - domain-written-advocacy/financial-hardship/advocacy_hardship_assistance_request.md
  - domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md
---

**Purpose:** Help you write **your own** dated request for a healthcare provider's financial assistance or charity care programme — asking for the written policy and the application form, submitting an income and household summary, and asking for billing and collection to be held while it is assessed. The core move is timing: asking **before** you agree to pay or to instalments.

**When to use:** You have a medical bill you cannot afford, or expect one, and you want to ask about reduction or waiver in writing with the record kept.

**When NOT to use:** You think the bill itself is wrong → `advocacy_medical_bill_dispute.md` first, or alongside; assistance on an inflated bill still leaves you paying too much. The bill is with a collector → validate the debt first via `domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md`, then ask about assistance. Assistance is refused and you need a payment plan → `../financial-hardship/advocacy_payment_arrangement_proposal.md`.

---

## Boundary & Routing Block

Use a different pathway if:
- **You are about to agree to a payment plan, sign a financing agreement, or put the bill on a credit card** → **ask about assistance first.** Once a bill is converted into an instalment agreement or a financing product, reduction is often much harder to obtain and the balance may have moved to a third party. This is the single most consequential piece of timing in this whole area.
- **Medical care is needed now** → do not defer or forgo treatment over a billing or assistance question. Seek care; the financial question is separate and can be addressed afterwards. If a condition is deteriorating, seek care immediately.
- **The account is with a collector, or is being reported adversely** → validate the debt first and route to an attorney or **legal aid**; assistance may still be available, but the collection position needs handling in parallel.
- **The bill relates to an injury where another party may be responsible, or a workplace injury** → route to an attorney before applying; how these bills are handled can affect a claim.
- **You are being pressured to sign anything to receive care or to leave the facility** → do not sign what you have not read. Ask for a copy and time to review, and route to an attorney or a patient advocate if pressed.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal, financial, or medical services.

---

## Scope Boundary — Read First

This **drafts your own written request for financial assistance for you to send**. It is **not legal advice, financial advice, medical advice, a legal filing, or a substitute for an attorney, a nonprofit counsellor, a patient advocate, or your jurisdiction's law.** It will **not** tell you whether you are eligible or what income thresholds apply; state that any facility is obliged to offer assistance, or what obligations attach to a facility's tax or nonprofit status; cite or quote a statute, regulation, or programme rule as authority; name a specific assistance programme, scheme, or foundation; state any deadline; tell you what reduction you might receive; predict whether the application will be approved; assess how strong it is; or invent an income figure, household size, policy provision, or bill amount. Assistance programmes and any rules behind them **vary by facility, state, and country and change over time.** Every programme detail must come from **the facility's own written policy**, which is what this letter asks for.

---

## Core Principles

1. **Ask before you agree to anything.** Before instalments, before financing, before a card payment. Converting the bill changes who holds it and what can be reduced.
2. **Ask for the written policy, not just the form.** The policy states the criteria, the evidence, the timeframe, and the appeal route. The form alone tells you none of that, and applying blind to unstated criteria is how applications get declined for fixable reasons.
3. **Assistance is frequently not offered unless asked.** Many people pay bills in full that would have been reduced or waived. Asking costs a letter.
4. **Apply even if you think you earn too much.** Thresholds vary widely, some programmes account for the bill's size relative to income, and some operate discretion. This prompt cannot tell you the threshold — the policy can.
5. **Ask for a hold on billing and collection while it is assessed.** Explicitly, in writing, with confirmation. Accounts move toward collection during assessment unless someone stops it.
6. **Be complete and accurate about income and household.** Applications are commonly declined for missing evidence rather than ineligibility. Supply what the policy asks for; never overstate or understate.
7. **You apply and document; the facility decides.** Eligibility is theirs to determine against their own policy. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Provider / facility:** [name, and whether hospital, clinic, or physician group]
- **Patient and account identifiers:** [account #, medical record #, name]
- **Date(s) of service:** [YYYY-MM-DD]
- **Amount billed:** [$X] · **Amount outstanding:** [$Y]
- **Have you agreed a payment plan or financing yet?:** [if yes → Boundary & Routing Block]
- **Do you think the bill is correct?:** [if no → dispute it as well, see related prompt]
- **Insurance status:** [insured / uninsured / underinsured — and what the insurer paid]
- **Household size:** [number of people supported]
- **Household income:** [amount, sources, period]
- **Other significant medical bills:** [amounts, providers]
- **Assets or savings, if the policy asks:** [only what their policy requires]
- **Evidence you can supply:** [pay stubs, tax return, benefit award, bank statements, unemployment record]
- **Any collector, injury claim, or pressure to sign?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the figures the user supplies.
- Screen **first** for an existing payment plan or financing agreement, and for a collector, injury claim, or pressure to sign, and route each.
- State that the user should ask about assistance before agreeing to any payment arrangement.
- Make the request cover both the **written policy** and the application form.
- Ask for a hold on billing and collection during assessment, confirmed in writing.
- Present income and household as a clear summary from the user's own figures, with evidence listed.
- Advise applying even where the user believes they may earn too much, since thresholds are unknown to this prompt.
- Note that a disputed bill should be disputed as well as being the subject of an assistance request.
- Include a Sending Log and label the output `MY OWN REQUEST — NOT A LEGAL FILING`.

**Must Not:**
- State eligibility, income thresholds, percentages, or what reduction might be granted.
- State that any facility is obliged to offer assistance, or invoke tax or nonprofit status as an obligation.
- Cite or invent a statute, regulation, or programme rule.
- Name a specific assistance programme, scheme, charity, or foundation.
- State any deadline or assessment timeframe.
- Predict approval or the size of any reduction, or assess how strong the application is.
- Invent an income figure, household size, asset, bill amount, or policy provision.
- Advise overstating or understating income, household, or assets.
- Advise deferring or forgoing care.
- Advise agreeing to instalments or financing before assistance has been asked about.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen **first** for an already-agreed payment plan or financing, a collector, an injury or workplace claim, and any pressure to sign → route per the Boundary & Routing Block. Reinforce that care must not be deferred over a billing question. Restate the jurisdiction and the boundary: the facility determines eligibility against its own policy.

### Stage 2 — Check Whether the Bill Is Also Disputed
Establish whether the user believes the bill is correct. Where it is not, note that the dispute and the assistance request are separate and should both proceed — assistance calculated on an inflated bill still leaves the user paying too much. Point to the dispute prompt.

### Stage 3 — Request the Policy and the Form
Build the request for the facility's **written financial assistance policy** — criteria, evidence required, how the decision is made, the timeframe, and any appeal route — together with the application form. Note that applying without the policy risks a declinature on a fixable evidence point.

### Stage 4 — Assemble the Income and Household Summary
Build a clear summary from the user's own figures: household size, income by source, other medical obligations, and any assets the policy requires. Flag missing figures as `[NEED AMOUNT:]`. Do not adjust anything, in either direction.

### Stage 5 — Ask for the Hold
Add an explicit request that billing and collection activity be held while the application is assessed, with written confirmation. Add a request to be told what happens if the application is declined and what alternatives exist.

### Stage 6 — Draft the Request and Close
Compose the user's own dated request, labeled as theirs to send, with the Sending Log. Include the instruction not to agree to instalments or financing until the assistance decision is received. Route eligibility, legal, and collection questions onward.

---

## Output Format

```markdown
MY OWN FINANCIAL ASSISTANCE REQUEST — NOT A LEGAL FILING
From: [your name], [contact]. To: [facility, financial assistance / patient financial services].
Date: [YYYY-MM-DD]. Delivery: [designated address / portal / certified mail]. Keep a copy.
This is my own request. It does NOT state that you are obliged to offer assistance, claim any
eligibility, cite any law or programme rule, state any deadline, or predict your decision.
Eligibility is for you to determine against your own written policy.

Re: Request for financial assistance — account [NEED ACCOUNT #:], patient [name],
date(s) of service [YYYY-MM-DD]

## The account
- Patient: [name] · Account / medical record number: [#]
- Date(s) of service: [YYYY-MM-DD]
- Amount billed: [$X] · Amount outstanding: [$Y]
- Insurance status: [insured — insurer paid $Z / uninsured / underinsured]

## What I am requesting
1. A copy of your **written financial assistance / charity care policy**, including:
   - The criteria you apply
   - The evidence you require
   - How and by whom the decision is made
   - The timeframe for a decision
   - Any appeal or reconsideration route
2. The application form and instructions for submitting it.
3. Consideration of my account for assistance.

## My household and income
| Item | Detail |
|---|---|
| Household size | [n] people |
| Household income | [$X] per [month/year] |
| Sources | [employment / benefits / pension / other] |
| Other outstanding medical bills | [$X across [n] providers] |
| [NEED AMOUNT: ...] | |

Evidence I can supply on request or with the form:
- [pay stubs / most recent tax return / benefit award letter / bank statements / unemployment record]

I will complete your own form and supply whatever evidence your policy requires.

## Please also confirm
1. **That billing and collection activity on this account are on hold while my application is
   assessed**, and confirm this in writing.
2. What happens if my application is not approved, and what alternatives you offer.
3. Whether assistance can be applied to amounts already billed as well as future care.

I have not agreed to a payment plan or financing on this account and would like the assistance
decision before I do.

Please respond in writing by [date].
[Your name], account [#], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Hold confirmed? |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [dept] | [#] | [receipt] | [YYYY-MM-DD] | [ ] |

Note to self: this is my own request, not legal or financial advice, and eligibility is theirs to
determine. **I will not agree to a payment plan, financing, or a card payment until I have the
assistance decision** — converting the bill makes reduction harder and may move it to a third
party. If I also believe the bill is wrong, I will dispute it separately: assistance on an
inflated bill still leaves me paying too much. A billing question does not delay my care.
*Verify with the facility's own written policy — assistance programmes vary by facility, state, and country.*
```

---

## Verification

- [ ] Existing payment plan or financing screened **first**, with the ask-before-agreeing point made?
- [ ] Collector, injury/workplace claim, and pressure-to-sign screened and routed?
- [ ] Do-not-defer-care note included?
- [ ] Jurisdiction captured and eligibility left to the facility's own policy?
- [ ] Request covers the **written policy** as well as the form, including criteria, evidence, timeframe, and appeal route?
- [ ] Income and household summarized from the user's own figures, unadjusted, with gaps flagged?
- [ ] Hold on billing and collection requested explicitly, with written confirmation?
- [ ] Apply-even-if-you-think-you-earn-too-much guidance given?
- [ ] Disputed bill noted as requiring a separate dispute alongside?
- [ ] No eligibility, threshold, percentage, or reduction figure stated?
- [ ] No claim that the facility is obliged to offer assistance, and no tax/nonprofit status invoked?
- [ ] No statute, regulation, or programme rule cited or invented?
- [ ] No specific programme, scheme, charity, or foundation named?
- [ ] No deadline, approval prediction, or strength assessment?
- [ ] No figures invented or adjusted in either direction?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Nonprofit hospitals are required to offer charity care" | State no obligation; ask for their written policy |
| "You'll qualify — that's under 200% of the poverty line" | State no threshold or eligibility; the policy states the criteria |
| "You probably earn too much to bother applying" | Encourage applying; thresholds vary and this prompt does not know them |
| "Expect around a 70% reduction" | Predict no reduction or outcome |
| "Set up the payment plan now and apply for assistance after" | **Ask first** — converting the bill makes reduction harder |
| Request only the application form | Request the written policy too; criteria and evidence live there |
| Omit the request for a collection hold | Ask explicitly and get it in writing |
| Round the household income down to improve the chances | Never adjust the user's figures in either direction |
| Apply for assistance on a bill the user thinks is wrong, and stop there | Dispute the bill as well; assistance on an inflated bill still overpays |
| Suggest delaying a procedure until the assistance decision | Never advise deferring care; the financial question is separate |

---

## Adaptations

**By facility type:**
- **Hospital or health system:** Usually has a formal written policy and a dedicated department; ask for both the policy and the department's direct contact.
- **Physician group or specialist billing separately:** Each biller may run its own arrangement or none; ask each separately, since one episode of care often produces several bills.
- **Clinic or community provider:** May operate a sliding scale rather than a formal programme; ask what exists rather than naming anything.
- **Ambulance or emergency transport:** Frequently billed separately and often overlooked entirely; ask them directly whether assistance exists.

**By situation/profile:**
- **Uninsured:** Ask whether an uninsured or self-pay discount applies in addition to assistance — these are commonly separate reductions.
- **Insured but with a large balance:** Ask whether assistance applies to patient responsibility after insurance; many programmes do.
- **Several providers from one episode:** Apply to each biller; assistance from one does not carry to another.
- **Already declined:** Ask for the reason in writing and whether reconsideration or appeal exists — declines are frequently evidence-related and fixable.

---

## Related Prompts

- `advocacy_medical_bill_dispute.md` — dispute the bill's accuracy alongside applying for assistance.
- `../financial-hardship/advocacy_payment_arrangement_proposal.md` — once assistance is decided and a balance remains.
- `../financial-hardship/advocacy_hardship_assistance_request.md` — for non-medical creditors affected by the same difficulty.
- `../../domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md` — if the bill is already with a collector.
