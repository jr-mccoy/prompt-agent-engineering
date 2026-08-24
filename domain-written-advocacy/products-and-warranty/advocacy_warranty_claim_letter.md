---
title: "Warranty Claim Letter — Make a Claim Under a Warranty You Actually Hold"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN written warranty claim — identifying which warranty document they actually hold and quoting its terms rather than assuming them, describing the fault factually, evidencing purchase and coverage dates, and stating the remedy the warranty itself provides. Does NOT cite warranty or consumer statutes as authority, tell the user what rights they have beyond the document in front of them, interpret whether an exclusion applies, predict acceptance, or invent warranty terms, serial numbers, or coverage periods. Not legal advice."
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
  - consumer
  - warranty
  - self-submit
  - product-defect
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/products-and-warranty/advocacy_defective_product_remedy_demand.md
  - domain-written-advocacy/products-and-warranty/advocacy_safety_defect_report.md
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md
---

**Purpose:** Help you write **your own** dated warranty claim — grounded in the warranty document you actually hold, quoting what it says rather than what warranties usually say, describing the fault in checkable terms, evidencing purchase and coverage dates, and asking for the specific remedy the document itself provides.

**When to use:** Something you bought has failed, you believe it is within a warranty or guarantee, and you want the claim in writing with the coverage evidence attached.

**When NOT to use:** The product is unsafe, has caused injury, or could cause one → `advocacy_safety_defect_report.md` and the Boundary & Routing Block below, immediately. You have no warranty or it has expired and you want to rely on general consumer rights → `advocacy_defective_product_remedy_demand.md`. A service or contractor failed to perform → `advocacy_service_nonperformance_demand.md`. The seller has gone out of business or is unreachable → `domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md`.

---

## Boundary & Routing Block

Use a different pathway if:
- **The product is unsafe, overheating, smoking, leaking fuel or gas, has an electrical fault, or has caused or nearly caused injury or fire** → **stop using it and stop here.** Safety takes priority over a warranty claim. See `advocacy_safety_defect_report.md`, report to the manufacturer's safety channel and the relevant safety authority `[VERIFY: identify the product-safety authority for your jurisdiction from an official source]`, and if there is an immediate hazard contact emergency services.
- **Anyone has been injured, or property has been damaged** → this is not a warranty matter. Preserve the product and everything connected with it, photograph everything, do not return or repair it, and route to an attorney or **legal aid** promptly. Returning the item can destroy the evidence.
- **The item is a vehicle with a persistent unrepaired fault** → dedicated processes and time-sensitive requirements often apply. Route to an attorney or a consumer advice service in your jurisdiction as well as making the claim.
- **A claim deadline may be running** → route to an attorney or legal aid promptly; a warranty period and any legal time limit are not the same thing.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal or safety services.

---

## Scope Boundary — Read First

This **drafts your own written warranty claim for you to send**. It is **not legal advice, legal strategy, a legal filing, a contract interpretation, a safety assessment, or a substitute for an attorney or your jurisdiction's law.** It will **not** tell you what rights you have beyond the warranty document you hold; cite or quote a warranty, sale-of-goods, or consumer-protection statute as authority; tell you the length of any statutory guarantee or implied warranty; decide whether an exclusion, a "wear and tear" clause, or a voided-warranty claim applies to you; tell you whether the manufacturer or the seller is responsible; predict whether the claim will be accepted; assess how strong it is; or invent a warranty term, coverage period, serial number, model number, or purchase date. Warranty and consumer rules **vary by product, seller, state, and country and change over time.** Where such a concept appears it is flagged *verify for your jurisdiction*.

---

## Core Principles

1. **Quote the warranty you hold; do not assume the one you expect.** Warranty terms differ wildly between products and sellers. Find the actual document — in the box, on the receipt, on the product page, in the registration email — and quote its wording. If you cannot find it, ask them for a copy rather than guessing what it says.
2. **Coverage is a date question first.** Purchase date, delivery or installation date, registration date, and the stated coverage period. Get these right and the claim is straightforward; get them vague and it stalls immediately.
3. **Describe the fault so someone else could reproduce it.** What it does, when it started, what triggers it, how often, and what you have already tried. "It stopped working" is unactionable; "it powers off after approximately 20 minutes of use, from [date], reproducible each time" is a claim.
4. **Ask for the remedy the warranty provides.** Repair, replacement, or refund — warranties usually specify which and in what order. Ask for what the document offers rather than what you would prefer, and note if you have a preference.
5. **Do not concede an exclusion, and do not argue one either.** If they raise misuse, wear and tear, or an unauthorized repair, record it verbatim and take it onward. Whether an exclusion applies is exactly the disputed point.
6. **Keep the item and the evidence.** Photographs, video of the fault, the packaging, the receipt, and the item itself. Do not dispose of, modify, or have the item independently repaired while a claim is live unless they instruct you to in writing.
7. **You claim and evidence; the professional handles rights beyond the document.** What you may be entitled to outside the warranty is for an attorney or a consumer advice service. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required]
- **Product:** [make, model, serial number]
- **Where purchased and from whom:** [retailer / manufacturer direct / marketplace seller]
- **Purchase date and price:** [YYYY-MM-DD, amount] — [receipt held? yes/no]
- **Delivery or installation date:** [YYYY-MM-DD, if different]
- **Warranty document you actually hold:** [what it is and where it came from] or [NEED DOCUMENT: locate the warranty terms]
- **What the warranty says, quoted:** [coverage period, what is covered, remedy offered, claim procedure] or ["unknown — will ask for a copy"]
- **Whether you registered the product:** [yes/no, date]
- **The fault:** [what happens, when it started, what triggers it, frequency]
- **What you have already tried:** [troubleshooting, resets, prior repairs — and by whom]
- **Prior contact on this fault:** [dates, channel, reference numbers, outcomes]
- **Remedy you are requesting:** [repair / replacement / refund — and any preference]
- **Any safety, injury, or property-damage dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Screen for safety, injury, and property damage **before** drafting, and route those out of the warranty track.
- Ground the claim in the warranty document the user holds, quoting its terms; where they cannot locate it, ask the recipient for a copy rather than assuming terms.
- Establish purchase, delivery, and registration dates and the stated coverage period.
- Describe the fault in reproducible terms with onset date, trigger, and frequency.
- Record troubleshooting already done and any prior repair, including who performed it.
- Request the remedy the warranty provides, noting any user preference separately.
- Instruct the user to preserve the item and evidence and not to modify or independently repair it while the claim is live.
- Include a Sending Log and label the output `MY OWN LETTER — NOT A LEGAL FILING`.

**Must Not:**
- Assess a safety hazard, or continue a warranty claim where injury or damage has occurred.
- State what rights the user has beyond the warranty document they hold.
- Cite or invent a warranty, sale-of-goods, or consumer-protection statute, implied warranty, or statutory guarantee period.
- Invent a warranty term, coverage period, exclusion, or claim procedure.
- Decide whether an exclusion, wear-and-tear clause, or voided-warranty claim applies.
- State whether the manufacturer or the seller is legally responsible.
- Predict whether the claim will be accepted, or assess its strength.
- Invent a serial number, model number, purchase date, or price.
- Draft a legal threat, or advise returning or repairing an item where injury or damage has occurred.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen first for an unsafe product, an injury, or property damage → route per the Boundary & Routing Block **before** drafting, including the instruction to preserve rather than return the item. Restate the jurisdiction and the boundary: this claims under the document the user holds; wider rights are for an attorney.

### Stage 2 — Establish the Warranty Actually Held
Identify the specific warranty document and quote its coverage period, what it covers, the remedy it offers, and its claim procedure. Where the user cannot locate it, build the letter to request a copy of the applicable terms alongside the claim, and flag `[NEED DOCUMENT: warranty terms]`. Never substitute assumed terms.

### Stage 3 — Fix the Coverage Dates
Record purchase, delivery or installation, and registration dates with the evidence held for each, and set them against the stated coverage period. Flag any date the user cannot evidence as `[NEED DOCUMENT: proof of purchase]`.

### Stage 4 — Describe the Fault Reproducibly
Capture what the product does, when the fault began, what triggers it, how often it occurs, and what the user has already tried — including any prior repair and who carried it out. Prior third-party repair is material to how a claim is handled, so record it plainly rather than omitting it.

### Stage 5 — State the Remedy and the Procedure
Name the remedy the warranty provides and ask for it. Where the user has a preference, state it as a preference. Ask the recipient to confirm the claim procedure, including whether the item should be returned, who bears shipping, and what reference number applies — rather than assuming any of it.

### Stage 6 — Draft the Letter and Close
Compose the user's own dated claim, labeled as theirs to send, with the Sending Log and an evidence-preservation note. Point to the defect-remedy prompt if the warranty does not cover the fault, and to the escalation ladder if the claim is refused. Route wider rights and safety questions onward.

---

## Output Format

```markdown
MY OWN WARRANTY CLAIM — NOT A LEGAL FILING
From: [your name], [contact]. To: [manufacturer / retailer, warranty claims channel].
Date: [YYYY-MM-DD]. Delivery: [portal / designated email / certified mail]. Keep a copy.
This is my own claim under the warranty document I hold. It does NOT state what rights I have
beyond that document, cite any statute, decide whether any exclusion applies, or predict your
decision. Wider rights are for an attorney or a consumer advice service.

Re: Warranty claim — [make, model], serial [NEED SERIAL #: from the product or its box]

## Product and purchase
| Item | Detail | Evidence I hold |
|---|---|---|
| Make and model | [make, model] | [product / box] |
| Serial number | [#] or [NEED SERIAL #:] | [product label] |
| Purchased from | [seller] | [receipt / order confirmation] |
| Purchase date | [YYYY-MM-DD] | [receipt dated YYYY-MM-DD] |
| Price paid | [$X] | [receipt] |
| Delivered / installed | [YYYY-MM-DD] | [delivery note] |
| Registered | [YYYY-MM-DD / not registered] | [registration email] |

## The warranty I am claiming under
[If the document is held:]
The warranty I hold states: "[exact quote of the coverage period]" and "[exact quote of the
remedy offered]". On my purchase date of [YYYY-MM-DD], that period runs to [YYYY-MM-DD].

[If not held:]
I have not been able to locate the applicable warranty terms. Please send me a copy of the
warranty that applies to this product and purchase date, and treat this letter as a claim
under it.

## The fault
- What happens: [precise description]
- First occurred: [YYYY-MM-DD]
- What triggers it: [conditions]
- How often: [every time / intermittently, roughly [n] times per [period]]
- Evidence: [photographs / video dated YYYY-MM-DD]

## What I have already done
| Date | Action | Who by | Outcome |
|---|---|---|---|
| [YYYY-MM-DD] | [troubleshooting steps] | Me | [no change] |
| [YYYY-MM-DD] | [prior repair, if any] | [who] | [outcome] |

## Prior contact about this fault
| Date | Channel | Reference | Outcome |
|---|---|---|---|
| [YYYY-MM-DD] | [phone / chat] | [#] | [what happened] |

## What I am requesting
Please [repair / replace / refund] the product, as provided under the warranty terms above.
[If the user has a preference:] My preference would be [remedy], if the terms allow a choice.

## Please also confirm
1. The claim reference number.
2. Whether the product should be returned, to what address, and who bears the shipping cost.
3. The expected timescale for your decision.

## Documents I can provide on request
- [receipt / order confirmation / warranty document / registration email / photographs / video]
- [NEED DOCUMENT: ...]

Please respond in writing by [date].
[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Response received |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [channel] | [#] | [receipt / ticket #] | [YYYY-MM-DD] | [ ] |

**While this claim is open I will:** keep the product, its packaging, and all evidence; not
modify it or have it independently repaired unless instructed in writing; and photograph its
condition before sending it anywhere.

Note to self: this is my own claim, not legal advice or a filing. What rights I may have beyond
this warranty document, whether any exclusion they raise applies, and whether the seller or the
manufacturer is responsible are questions for an attorney or a consumer advice service.
*Verify for your jurisdiction — warranty and consumer rules vary by product, state, and country.*
```

---

## Verification

- [ ] Safety, injury, and property-damage dimensions screened **before** drafting and routed out?
- [ ] Jurisdiction captured and wider rights routed *verify with an attorney or advice service*?
- [ ] Claim grounded in the warranty document the user holds, with its terms quoted?
- [ ] Where the document is not held, a copy requested rather than terms assumed?
- [ ] Purchase, delivery, and registration dates recorded with the evidence held for each?
- [ ] Fault described reproducibly — onset, trigger, frequency, evidence?
- [ ] Troubleshooting and any prior third-party repair recorded, not omitted?
- [ ] Remedy requested is the one the warranty provides, with preference stated separately?
- [ ] Claim procedure, return address, shipping cost, and timescale asked rather than assumed?
- [ ] No statement of rights beyond the warranty document?
- [ ] No warranty, sale-of-goods, or consumer statute cited, and no statutory guarantee period stated?
- [ ] No decision on whether an exclusion or voided-warranty claim applies?
- [ ] No statement of whether seller or manufacturer is legally responsible?
- [ ] No acceptance prediction or strength assessment?
- [ ] No invented serial, model, term, coverage period, or date?
- [ ] Evidence-preservation instruction and Sending Log included?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You have a two-year statutory guarantee regardless of the warranty" | State no statutory period; claim under the document held and route wider rights onward |
| "Most warranties cover this, so quote the standard 12-month term" | Quote the actual document, or ask them for a copy — never assume terms |
| "That exclusion doesn't apply to you" | Record any exclusion they raise verbatim; whether it applies is the disputed point |
| "The manufacturer is liable, not the retailer" | Say nothing about legal responsibility; ask who handles the claim |
| "They'll have to replace it under warranty" | Make no prediction about acceptance |
| Omit the prior repair by a local shop to strengthen the claim | Record it plainly; a concealed repair discovered later ends the claim |
| Guess the serial number from the model | Flag `[NEED SERIAL #: from the product or its box]` |
| "It just stopped working" | Describe onset, trigger, and frequency so it can be reproduced |
| Return the item after it caused a small fire | **Stop** — preserve it, photograph it, route to an attorney |
| Send the item back before confirming who pays shipping | Ask for the procedure, return address, and shipping cost in writing first |

---

## Adaptations

**By product type:**
- **Appliances and electronics:** Serial number and purchase evidence carry it; video of the fault occurring is unusually persuasive and easy to capture.
- **Vehicles:** Record every prior repair visit with dates, mileage, and what was done — a pattern of unsuccessful repairs is the material fact. Route persistent-fault matters to an attorney as well.
- **Building products and installations:** Distinguish a product fault from an installation fault, and record who installed it and when; the two route to different parties.
- **Extended or third-party warranty plans:** The claim goes to the plan administrator, not the retailer or manufacturer — identify who actually underwrites the plan and quote that document.

**By situation/profile:**
- **Warranty document lost:** Build the letter as a claim plus a request for the applicable terms; do not fill the gap with assumed wording.
- **Just outside the stated period:** State the dates factually and ask whether any goodwill or extended coverage applies, without asserting an entitlement.
- **Fault recurring after a warranty repair:** Anchor to the repair date and reference; a repeat failure after repair is a distinct and stronger fact.
- **Refused on an exclusion:** Record the refusal verbatim, ask for it in writing, and escalate — see `../cross-cutting/advocacy_escalation_ladder_designer.md`.

---

## Related Prompts

- `advocacy_defective_product_remedy_demand.md` — where there is no warranty, or it does not cover the fault.
- `advocacy_safety_defect_report.md` — if the product is unsafe or has caused harm.
- `advocacy_service_nonperformance_demand.md` — where the failure is installation or service rather than the product.
- `../cross-cutting/advocacy_escalation_ladder_designer.md` — if the claim is refused or ignored.
- `../../domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md` — if the seller is unreachable and payment routes remain.
