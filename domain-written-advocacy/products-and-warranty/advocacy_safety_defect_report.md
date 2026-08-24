---
title: "Product Safety Defect Report — Report a Dangerous Product to the Manufacturer and the Authority"
category: advocacy
description: "[SELF-SUBMIT] Help a person report a product they believe is unsafe — to the manufacturer or retailer and to a product-safety authority they identify themselves — with an evidence-preservation-first sequence, a factual hazard description, and identifiers a recall or investigation would need. Puts safety and evidence preservation ahead of any refund or claim. Does NOT assess whether a product is dangerous, name safety authorities or supply their contact details, cite safety regulations, predict a recall, or advise returning an item that has caused harm. Not legal advice."
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
  - consumer
  - product-safety
  - self-submit
  - safety
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/products-and-warranty/advocacy_warranty_claim_letter.md
  - domain-written-advocacy/products-and-warranty/advocacy_defective_product_remedy_demand.md
  - domain-written-advocacy/institutions-and-records/advocacy_regulator_complaint_drafter.md
  - domain-written-advocacy/cross-cutting/advocacy_correspondence_log_builder.md
---

**Purpose:** Help you report a product you believe is unsafe — to the manufacturer or retailer, and to a product-safety authority **you** identify — in a way that preserves evidence, records the hazard factually, and supplies the identifiers a recall or investigation actually needs. The order of operations here matters more than the wording: stop using it, make it safe, preserve it, photograph it, then report.

**When to use:** A product has overheated, caught fire, given a shock, collapsed, released fumes, contained something it should not, or otherwise done something you believe is dangerous — whether or not anyone was hurt.

**When NOT to use:** There is a fire, gas leak, or someone is injured right now → emergency services, immediately; nothing here comes first. You want a refund and the product is merely faulty rather than dangerous → `advocacy_defective_product_remedy_demand.md`. Someone has been injured or property damaged → read the Boundary & Routing Block; you can still report, but an attorney comes into it before you part with the item.

---

## Boundary & Routing Block

**Before anything else:**
- **If there is an immediate hazard right now** — active fire, smoke, a gas smell, an electrical fault you can see arcing, or anyone unwell from fumes → **contact emergency services immediately.** Nothing in this prompt comes before that.
- **If anyone has been injured, or property has been damaged** → **do not return, repair, discard, or send the product anywhere**, including to the manufacturer, until you have spoken to an attorney or **legal aid**. Companies frequently offer a refund in exchange for the item being returned. Returning it can leave you without the single piece of evidence that matters. Photograph everything, keep the item, keep the packaging, keep the receipt, and get advice before agreeing to send it back.
- **If a child, an older person, or anyone medically vulnerable was exposed** → seek medical advice even if they seem unharmed, and note the date and what was said. Some exposures present late.

Use a different pathway if:
- **You want compensation for an injury** → that is a legal claim, not a safety report. Route to an attorney or legal aid; the two run separately and the report does not replace advice.
- **The product is a medicine, medical device, or food** → these have their own dedicated reporting systems, distinct from general product safety. `[VERIFY: identify the correct reporting body for that product category in your jurisdiction from an official government source.]`
- **The product is a vehicle or vehicle part** → vehicle safety usually has a separate authority and a separate recall system. `[VERIFY: identify it for your jurisdiction from an official source.]`

This prompt is educational support for preparing your own report. It is not a substitute for legal, medical, safety, or emergency services.

---

## Scope Boundary — Read First

This **helps you record and report a product-safety concern in your own words**. It is **not legal advice, legal strategy, a legal filing, a safety or engineering assessment, medical advice, or a substitute for an attorney, a qualified professional, a safety authority, or emergency services.** It will **not** tell you whether a product is actually dangerous, defective, or non-compliant; assess a hazard, diagnose a cause, or say whether a product met any standard; name a product-safety authority, recall database, or reporting portal, or supply its address or URL; cite or quote a product-safety regulation, standard, or directive; tell you whether a recall exists or predict whether one will follow; tell you whether you have a claim or what it is worth; assess how strong your report is; or invent a model number, batch code, serial number, or incident date. Product-safety authorities, their remit, and their reporting routes **vary by country, state, and product category and change over time** — every body must be one **you** locate from an official government source.

---

## Core Principles

1. **Stop using it, and stop others using it.** Unplug it, isolate it, and tell anyone else in the household. This precedes reporting, refunds, and everything else.
2. **Preserve the item — especially if you might want a remedy.** The instinct is to send it back for a refund. If it caused harm, that instinct costs you the evidence. Get advice before parting with it.
3. **Photograph before you touch anything more.** The item, the damage, the surroundings, the labels, the packaging, the batch code, the plug or connector. Dated, from several angles, before anything is cleaned up or made safe if it is safe to do so.
4. **Report what happened, not what caused it.** "The unit emitted smoke from the rear vent after approximately 20 minutes and the casing was too hot to touch" is a report. "The capacitor failed due to inadequate thermal design" is a conclusion you are not in a position to draw, and it weakens a report by making it arguable.
5. **Identifiers are what make a report usable.** Model, batch, serial, date code, retailer, purchase date. A safety authority or manufacturer works from these to find whether other units are affected — without them a report cannot be actioned.
6. **Report to both, separately.** The manufacturer or retailer, and the safety authority. They do different things: one may remedy your unit, the other may look at every unit. Do not let one substitute for the other.
7. **Your report is one data point in a pattern.** You may never hear an outcome, and that does not mean it did nothing. Report accurately and completely, and let the pattern do its work.

---

## Your Input

- **Your jurisdiction (state/country):** [required — safety authorities are national or state-level]
- **Is anyone injured, or is there an active hazard right now?:** [if yes → Boundary & Routing Block, before anything else]
- **Has anyone been injured, or property damaged, at any point?:** [if yes → attorney before returning the item]
- **Product:** [make, model, colour/variant]
- **Identifiers:** [serial #, batch or lot code, date code, barcode] or [NEED IDENTIFIER: from the product or its label]
- **Where and when purchased:** [retailer, YYYY-MM-DD, price, receipt held?]
- **What happened:** [factual account — what the product did, when, under what conditions]
- **Date and time of the incident:** [YYYY-MM-DD, HH:MM]
- **How the product was being used:** [normal use / as instructed / any modification or third-party accessory]
- **Who was present or exposed:** [and whether anyone is medically vulnerable]
- **Damage caused:** [to the product, to property, to anyone]
- **Photographs taken?:** [yes/no — of what]
- **Do you still have the item and packaging?:** [yes/no]
- **Prior similar incidents with the same product:** [dates]

---

## Constraints

**Must:**
- Screen for an active hazard, injury, and property damage **first**, before any drafting, and route per the Boundary & Routing Block.
- Instruct the user to stop using the product and prevent others using it.
- Instruct the user **not** to return, repair, or discard the item where injury or damage occurred, until advised by an attorney.
- Instruct the user to photograph the item, damage, labels, batch codes, and packaging before anything is altered, where safe to do so.
- Describe the incident factually — what happened, when, under what conditions — without diagnosing a cause.
- Capture product identifiers, flagging missing ones as `[NEED IDENTIFIER:]`.
- Record how the product was being used, including any modification or third-party accessory, honestly.
- Produce two separate reports: one to the manufacturer or retailer, one for a safety authority the user identifies.
- Flag every authority as `[VERIFY: ...]` and supply no names, addresses, or URLs.
- Include a Sending Log and label outputs `MY OWN REPORT — NOT A LEGAL FILING`.

**Must Not:**
- Assess whether the product is dangerous, defective, or non-compliant.
- Diagnose the cause of a failure, or attribute it to a component, design, or manufacturing step.
- State whether the product met or breached any standard, regulation, or certification.
- Name a product-safety authority, recall database, or reporting portal, or supply an address or URL.
- Cite or invent a safety regulation, standard, directive, or certification mark.
- State whether a recall exists, or predict that one will follow.
- Tell the user whether they have a claim, or what it is worth.
- Advise returning or surrendering the item where injury or property damage occurred.
- Give medical advice, or reassure the user that an exposure is harmless.
- Invent a model number, batch code, serial number, incident date, or the contents of a label.

---

## Instructions

### Stage 1 — Screen for Immediate Danger, Injury, and Damage
Ask first whether there is an active hazard, whether anyone is injured, and whether property was damaged. Route per the Boundary & Routing Block **before drafting anything**: emergency services for an active hazard; medical advice for any exposure; an attorney before the item goes anywhere if there was harm. Do not proceed to reporting until this is stated.

### Stage 2 — Make Safe and Preserve
Instruct the user to stop using the product, isolate it, and tell others in the household. Then: photograph the item, the damage, the surroundings, all labels and codes, and the packaging — dated, from several angles — before cleaning up or altering anything, where it is safe to do so. Confirm the item, packaging, and receipt are being retained.

### Stage 3 — Capture the Identifiers
Record make, model, variant, serial number, batch or lot code, date code, and barcode from the product and its packaging. These are what let a manufacturer or authority identify affected units. Flag anything unreadable or missing as `[NEED IDENTIFIER:]` rather than approximating.

### Stage 4 — Write the Factual Incident Account
Record what the product did, when, for how long it had been in use, under what conditions, and what was observed — in physical, observable terms. Record how it was being used, including any modification, repair, or third-party accessory, honestly; omitting these damages the report's value and surfaces later anyway. Do not diagnose a cause.

### Stage 5 — Build the Two Reports
Produce a report to the manufacturer or retailer requesting acknowledgement and asking what they will do, and a parallel factual record formatted for a safety authority. Do not name the authority: instruct the user to identify the correct one for their jurisdiction and product category from an official government source, flagged `[VERIFY:]`.

### Stage 6 — Log and Close
Set up the Sending Log for both reports, with reference numbers. Note that any remedy or claim runs separately, and that the item should not be surrendered for a refund where harm occurred without advice. Route claims, medical questions, and hazard assessment onward.

---

## Output Format

```markdown
MY OWN PRODUCT SAFETY REPORT — NOT A LEGAL FILING
Prepared [YYYY-MM-DD]. This is my own factual account. It does NOT state that the product is
dangerous, defective, or non-compliant, diagnose a cause, cite any standard or regulation, or
predict a recall. Hazard assessment is for a qualified professional; any claim is for an attorney.

## Immediate steps I have taken
- [ ] Stopped using the product and isolated it
- [ ] Told others in the household not to use it
- [ ] Photographed the item, damage, labels, batch codes, and packaging — dated [YYYY-MM-DD]
- [ ] Retained the item, packaging, and receipt
- [ ] [If anyone was exposed] Sought medical advice on [YYYY-MM-DD]
- [ ] [If injury or damage] Spoken to an attorney **before** agreeing to return the item

## Product identifiers
| Field | Detail |
|---|---|
| Make / brand | [make] |
| Model / variant | [model] |
| Serial number | [#] or [NEED IDENTIFIER: from the product label] |
| Batch / lot code | [#] or [NEED IDENTIFIER:] |
| Date code | [#] |
| Barcode | [#] |
| Purchased from | [retailer], [YYYY-MM-DD], [$X] |
| Receipt held | [Yes / No] |

## What happened (factual)
- Date and time: [YYYY-MM-DD, HH:MM]
- In use for: [n minutes/hours] before the incident
- Conditions: [plugged into / powered by / ambient conditions]
- What I observed: [precise physical description — what it did, in what order]
- Who was present: [people, and whether anyone is medically vulnerable]
- Damage: [to the product / to property / to a person]
- Prior similar incidents with this product: [dates, or none]

## How the product was being used
- Used as instructed: [Yes / No — detail]
- Any modification, repair, or third-party accessory: [detail, or none]

I am describing what I observed. I am not stating what caused it.

---

## Report 1 — To the manufacturer / retailer
> To: [manufacturer / retailer, safety or customer channel] · Date: [YYYY-MM-DD]
> Re: Safety concern — [make, model], serial [#], batch [#]
>
> I am reporting a safety concern with a product I purchased from [retailer] on [date].
>
> On [YYYY-MM-DD] at approximately [time], [factual account of what the product did].
> [Damage caused.] [Whether anyone was exposed or injured.]
>
> Product identifiers: model [#], serial [#], batch/lot [#], date code [#].
>
> I have stopped using the product and retained it, its packaging, and the receipt.
> I have photographs taken on [date].
>
> Please confirm:
> 1. A reference number for this report.
> 2. Whether you are aware of other reports of this behaviour in this model or batch.
> 3. What you intend to do, and what you would like me to do.
>
> [If harm occurred:] I am not returning the product at this stage.
>
> [Your name], [contact], [YYYY-MM-DD]

## Report 2 — Factual record for a product-safety authority
`[VERIFY: identify the product-safety authority covering my jurisdiction and this product
category — general consumer products, vehicles, medicines and medical devices, and food are
usually handled by different bodies — and its current reporting process, from an official
government source. This record does not tell me which body that is.]`

| Field | Detail |
|---|---|
| Reporter | [name, contact] |
| Product | [make, model, variant] |
| Identifiers | serial [#], batch [#], date code [#], barcode [#] |
| Purchased | [retailer], [YYYY-MM-DD] |
| Incident date/time | [YYYY-MM-DD, HH:MM] |
| What happened | [factual account] |
| Use conditions | [as instructed / modifications / accessories] |
| Injury | [none / detail] |
| Property damage | [none / detail] |
| Item retained | [Yes] |
| Photographs | [Yes, dated YYYY-MM-DD] |
| Reported to manufacturer | [YYYY-MM-DD], reference [#] |

---
## Sending Log
| Report | Sent | Method | Sent to | Reference # | Response received |
|---|---|---|---|---|---|
| Manufacturer | [YYYY-MM-DD] | [method] | [channel] | [#] | [ ] |
| Safety authority | [YYYY-MM-DD] | [method] | [VERIFY body] | [#] | [ ] |

Note to self: this is my own report, not legal, medical, or safety advice. Whether this product
is dangerous or non-compliant is for a qualified professional and the authority; whether I have
a claim is for an attorney. I will not surrender the item for a refund while harm is involved
without advice, and I may never be told the outcome — the report still matters.
*Verify for your jurisdiction — safety authorities and reporting routes vary by country and product category.*
```

---

## Verification

- [ ] Active hazard, injury, and property damage screened **first**, before any drafting?
- [ ] Emergency-services routing stated where there is an immediate hazard?
- [ ] Do-not-return instruction given where injury or property damage occurred, with attorney routing?
- [ ] Medical-advice routing given where anyone was exposed?
- [ ] Stop-using and isolate instruction included?
- [ ] Photograph-before-altering instruction included, with labels, codes, and packaging named?
- [ ] Product identifiers captured, with missing ones flagged `[NEED IDENTIFIER:]`?
- [ ] Incident described in observable physical terms, with **no** cause diagnosed?
- [ ] Use conditions, modifications, and third-party accessories recorded honestly?
- [ ] Two separate reports produced — manufacturer and authority?
- [ ] **No safety authority, recall database, or portal named, and no address or URL supplied?**
- [ ] No safety regulation, standard, directive, or certification cited?
- [ ] No statement that the product is dangerous, defective, or non-compliant?
- [ ] No recall claimed or predicted, and no claim value or strength assessed?
- [ ] No medical reassurance given?
- [ ] No invented model, batch, serial, date, or label contents?
- [ ] Sending Log covering both reports included?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Report it to the CPSC at saferproducts.gov" | `[VERIFY: identify the authority for your jurisdiction and product category from an official government source]` |
| "This is clearly a lithium battery thermal runaway" | "The unit became hot, then emitted smoke from the rear vent" — no cause diagnosis |
| "This product doesn't meet the applicable safety standard" | Cite no standard; describe what was observed |
| "Send it back to the manufacturer so they can investigate" | Where harm occurred, **do not return it** without attorney advice — it is the evidence |
| "There's probably a recall already — check the database" | State nothing about recalls; the user checks official sources |
| "You'd have a strong injury claim here" | Say nothing about claims or value; route to an attorney |
| "It's only a small burn, they'll be fine" | Give no medical reassurance; route to medical advice |
| Omit that a third-party charger was being used | Record it honestly; concealed conditions destroy a report's value |
| Read the batch code as probably matching the model number | Flag `[NEED IDENTIFIER: from the product label]` |
| Draft the report while a fire risk is still live | Stop — emergency services first, everything else after |

---

## Adaptations

**By product category:**
- **Powered goods and batteries:** Record charge state, charger used (original or third-party), how long in use, and ambient conditions; photograph the plug, connector, and any scorching.
- **Children's products and toys:** Record the child's age, what happened, and whether any part detached; note any small part recovered and keep it with the item.
- **Appliances and heaters:** Record installation date and installer, service history, and whether it was on a timer or thermostat; photograph the surroundings as well as the unit.
- **Medicines, devices, vehicles, food:** These have separate reporting systems — `[VERIFY: identify the correct body for that category]` rather than sending a general product report.

**By situation/profile:**
- **Nobody hurt, no damage:** The report is straightforward, and preserving the item is still worth doing until the manufacturer responds.
- **Injury or damage occurred:** Attorney before the item moves anywhere; the report can still be sent, and the item stays with you.
- **Item already returned before you realised:** Say so in the report, and supply the photographs, receipt, and any return reference — a report without the item is still useful to a pattern.
- **Recurring incidents with the same model:** Record every occurrence with dates; a repeat pattern from one household is itself significant to an investigator.

---

## Related Prompts

- `advocacy_warranty_claim_letter.md` — the remedy track, once safety is handled and evidence preserved.
- `advocacy_defective_product_remedy_demand.md` — for a faulty rather than dangerous product.
- `../institutions-and-records/advocacy_regulator_complaint_drafter.md` — once the correct authority is verified.
- `../cross-cutting/advocacy_correspondence_log_builder.md` — log both reports and every response.
