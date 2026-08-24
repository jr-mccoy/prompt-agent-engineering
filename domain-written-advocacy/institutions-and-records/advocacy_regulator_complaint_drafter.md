---
title: "Regulator Complaint Drafter — Take a Matter to an External Body"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft a complaint to an external body — regulator, ombudsman, licensing authority, or consumer protection office — that they identify themselves, with the internal process exhausted, a dated history with proof, the organization's final position quoted, and a stated desired outcome. Does NOT name bodies or supply their details, state jurisdiction or eligibility, cite regulation, state deadlines, assess the merits, or predict whether any body will act. Not legal advice."
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
  - regulator
  - complaint
  - escalation
  - self-submit
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-written-advocacy/cross-cutting/advocacy_correspondence_log_builder.md
  - domain-written-advocacy/insurance-and-medical/advocacy_external_review_request.md
  - domain-written-advocacy/privacy-and-data/advocacy_privacy_request_escalation.md
---

**Purpose:** Help you draft **your own** complaint to an external body — a sector regulator, an ombudsman or dispute scheme, a licensing authority, or a consumer protection office — once the organization's internal process is exhausted. It assembles the dated history with proof, quotes the organization's final position, states what you want to happen, and organizes it in the form these bodies actually work from.

**When to use:** You have been through the organization's complaints process, have its final response or been unable to obtain one, and you have identified the correct external body for your matter.

**When NOT to use:** The internal process is not exhausted → `advocacy_escalation_ladder_designer.md` first; most bodies require it. It is an insurance coverage decision → `../insurance-and-medical/advocacy_external_review_request.md`. It is a privacy request → `../privacy-and-data/advocacy_privacy_request_escalation.md`. You want compensation through a court → route to an attorney; a complaint to a regulator is not a claim.

---

## Boundary & Routing Block

Use a different pathway if:
- **You have not identified the correct body, or are unsure whether one exists** → **do this before drafting.** Which body covers a matter depends on the sector, the jurisdiction, and often whether the organization is a member of a scheme. Filing with the wrong body wastes months and can consume a time limit. `[VERIFY: identify the correct body, confirm it covers this organization and this type of matter, and obtain its current process and any time limit — from that body's own official site.]`
- **A complaint or claim time limit may be running** → external bodies commonly impose time limits running from the final response, and a court claim has its own separate limits. **Confirm both before drafting**: the body's from its own site, and any legal limit from an attorney or **legal aid**.
- **You want compensation, damages, or a court remedy** → a regulator complaint is generally not a compensation route, and some bodies will not consider a matter that is in litigation. Route to an attorney to advise which track fits before filing.
- **The matter involves a crime, fraud, or an immediate safety risk** → the appropriate authority or emergency service comes first, not a regulator complaint.
- **You are complaining about a professional's conduct in a matter still live** — a clinician, attorney, or licensed professional currently acting for you → consider the effect on that relationship and route to advice first.

This prompt is educational support for preparing your own complaint. It is not a substitute for legal services.

---

## Scope Boundary — Read First

This **organizes your own complaint to an external body you have identified**. It is **not legal advice, legal strategy, a legal filing, a compensation claim, or a substitute for an attorney or your jurisdiction's law.** It will **not** name a regulator, ombudsman, dispute scheme, licensing authority, or consumer protection office, or supply its address, portal, form, or URL; tell you which body has jurisdiction over your matter, or whether you are eligible to complain to it; cite, quote, or number any statute, regulation, licence condition, or scheme rule as authority; state any time limit or expected timescale; tell you whether the organization breached anything; assess the merits of your complaint or how strong it is; predict whether the body will investigate, act, uphold, or award anything; or invent a reference number, date, or the content of a response. Which bodies exist, what they cover, and how they work **vary by sector, state, and country and change over time** — all of it must be verified by **you** from the body's own official source.

---

## Core Principles

1. **Identify the body before you draft anything.** The commonest failure here is a well-written complaint sent to a body that does not cover the matter. Confirm coverage, eligibility, and time limits first.
2. **Exhaustion is usually the gate.** Most bodies expect the organization's internal process to be complete, and many require a final response or a stated waiting period. Establish where you stand before filing.
3. **The chronology is the complaint.** Dated, with proof of sending, and the organization's responses quoted. These bodies assess a documented sequence, and a narrative without dates is very hard for them to work with.
4. **Quote the final position; do not characterize it.** "Their final response of [date] states: '[quote]'" is what a caseworker needs. "They fobbed me off repeatedly" is not, and it makes the file harder to use.
5. **State the outcome you want, specifically.** A refund of a stated amount, a correction, a service completed, an apology, a policy change. Bodies differ in what they can provide — ask for something concrete and let them tell you what is possible.
6. **Use their form, and attach your record.** Most bodies have a form that governs. This document supports it — it does not replace it, and substituting a letter for a required form causes delay.
7. **You complain and document; the body decides.** Whether anything was breached, and whether they can help, is theirs to determine. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Sector:** [financial / insurance / telecom / energy / water / healthcare / professional services / retail / other]
- **The organization complained about:** [name, and any registration or licence number shown]
- **Have you identified the correct external body?:** [if no → Boundary & Routing Block, first]
- **Has it confirmed it covers this organization and matter?:** [yes/no]
- **Its stated time limit, from its own site:** [what and from when]
- **Internal complaint history:** [each step: date sent, to whom, channel, proof, response, date]
- **Final response:** [date, and its content verbatim] or ["none received; last contact [date]"]
- **What the complaint is about, factually:** [what happened, with dates]
- **What you want to happen:** [specific outcome]
- **Documents you hold:** [correspondence, contracts, statements, records, delivery proof]
- **Any litigation, compensation claim, crime, or safety dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction and sector; use only the facts the user supplies.
- Require the user to have identified and verified the body **before** drafting, flagged `[VERIFY:]`, and refuse to name one.
- Establish internal exhaustion and the final response, or record its absence with dates.
- Direct the user to confirm the body's time limit from its own site, and any legal limit from an attorney.
- Build a dated chronology with proof of sending for each step.
- Quote the organization's responses and final position verbatim.
- State one specific desired outcome.
- Note that the body's own form usually governs and this document supports it.
- Include a Sending Log and label the output `MY OWN COMPLAINT — NOT A LEGAL FILING`.

**Must Not:**
- Name a regulator, ombudsman, scheme, licensing authority, or consumer office, or supply its address, form, or URL.
- State which body has jurisdiction, or whether the user is eligible.
- Cite, quote, or number any statute, regulation, licence condition, or scheme rule.
- State any time limit or expected timescale.
- State whether the organization breached anything, or acted unlawfully or improperly.
- Assess the merits or strength of the complaint.
- Predict whether the body will investigate, act, uphold, or award anything.
- Characterize the organization or attribute motive.
- Invent a reference number, date, registration number, or the content of a response.
- Draft the complaint as a compensation claim, or where litigation is live without routing first.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for: an unidentified or unverified body; a running time limit; a compensation or court objective; live litigation; a crime or safety risk; and a live professional relationship → route each per the Boundary & Routing Block. Where the body is not yet identified and verified, **stop and route to that first.** Restate the jurisdiction and sector and the boundary.

### Stage 2 — Establish Exhaustion and the Final Position
Record whether the internal process is complete, whether a final response was issued, and what it says verbatim. Where no final response exists, record the last contact and the elapsed time — many bodies accept that as an alternative, but the user must confirm it from the body's own information.

### Stage 3 — Build the Chronology
Tabulate every step with date, what was sent or received, channel, reference number, and proof of sending. This is the document the caseworker reads first. Flag missing proof as `[NEED DOCUMENT:]` rather than asserting a step occurred.

### Stage 4 — State the Complaint Factually
Set out what happened in dated, factual terms tied to documents. Quote the organization's responses. Keep characterization out entirely — the sequence carries it, and a caseworker discounts adjectives.

### Stage 5 — State the Desired Outcome
Name one specific outcome. Note that bodies differ in what they can provide and that the user should ask what is within the body's power rather than assuming — framed as a question, not an assertion.

### Stage 6 — Assemble and Close
Compose the user's own dated complaint document with the chronology, the evidence index, and the Sending Log. State that the body's own form usually governs and this supports it. Route eligibility, merits, and legal questions onward.

---

## Output Format

```markdown
MY OWN COMPLAINT TO AN EXTERNAL BODY — NOT A LEGAL FILING
Prepared [YYYY-MM-DD]. This is my own factual record and complaint. It does NOT state that the
organization breached anything, cite any regulation or scheme rule, state any time limit, assess
my own case, or predict what the body will do.

## Before filing — my own checks
`[VERIFY, from the body's own official site: that it covers this organization and this type of
matter; that I am eligible to complain; its current form and process; and its time limit and when
it runs from. This document does not tell me which body to use or whether it can help.]`

- Body identified and coverage confirmed on: [YYYY-MM-DD]
- Its stated time limit: [what, from when]
- Its required form obtained: [ ]
- Internal process exhausted: [Yes — final response dated YYYY-MM-DD / No — see below]

## The organization
- Name: [organization] · Registration / licence number as shown: [#, if any]
- Sector: [sector] · My account or reference with them: [#]

## What the complaint is about
[Two or three factual sentences: what happened, when, and what remains unresolved.]

## Chronology
| # | Date | What happened | Channel | Reference | Proof I hold |
|---|---|---|---|---|---|
| 1 | [YYYY-MM-DD] | [the underlying event] | — | — | [document] |
| 2 | [YYYY-MM-DD] | I complained to [recipient] | [channel] | [#] | [receipt / sent copy] |
| 3 | [YYYY-MM-DD] | They responded | [channel] | [#] | [letter held] |
| 4 | [YYYY-MM-DD] | I escalated to [recipient] | [channel] | [#] | [receipt] |
| 5 | [YYYY-MM-DD] | Final response issued | [channel] | [#] | [letter held] |
| — | | [NEED DOCUMENT: proof of sending for step n] | | | |

## Their final position, verbatim
> "[exact quote from the final response]"

[or: No final response has been received. My last contact was on [YYYY-MM-DD] and I have had
no substantive reply in the [n] weeks since. I have confirmed with the body whether it will
accept a complaint on that basis.]

## What remains unresolved
- [point one — factual]
- [point two — factual]

## What I would like to happen
[One specific outcome — e.g. "A refund of $X" / "Correction of the record showing [Y]" /
"Completion of the work described in the quote of [date]" / "A review of the policy that
produced this outcome."]

I understand you may only be able to provide certain kinds of outcome. Please tell me what is
within your power in a matter of this kind.

## Evidence index
| # | Document | Date | What it establishes |
|---|---|---|---|
| 1 | [contract / statement / listing] | [YYYY-MM-DD] | [what was agreed or charged] |
| 2 | [my complaint letter] | [YYYY-MM-DD] | What I raised and when |
| 3 | [their final response] | [YYYY-MM-DD] | Their stated position |
| 4 | [NEED DOCUMENT: ...] | | |

---
## Sending Log
| Sent | To | Method | Reference # | Proof kept | Time limit | Acknowledged |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [body — VERIFY] | [their form / portal / mail] | [#] | [receipt] | [YYYY-MM-DD] | [ ] |

Note to self: this is my own complaint, not legal advice or a filing. **The body's own form
usually governs — this document supports it rather than replacing it.** Whether the organization
breached anything, whether this body can help, and whether a court claim would be a better route
are for the body itself and, if it matters, an attorney. A complaint to a regulator is generally
not a compensation route.
*Verify from the body's own official site — which bodies exist and what they cover varies by sector, state, and country.*
```

---

## Verification

- [ ] Body identified and coverage verified by the user **before** drafting, flagged `[VERIFY:]`?
- [ ] Time limit directed to the body's own site, and any legal limit to an attorney?
- [ ] Compensation/court objective, live litigation, crime/safety, and live professional relationship screened and routed?
- [ ] Internal exhaustion established, or its absence recorded with dates and elapsed time?
- [ ] Chronology dated with channel, reference, and proof of sending for each step?
- [ ] Organization's responses and final position quoted verbatim?
- [ ] One specific desired outcome stated, with a question about what the body can provide?
- [ ] Body's own form noted as governing, with this document supporting it?
- [ ] **No regulator, ombudsman, scheme, or authority named, and no address, form, or URL supplied?**
- [ ] No jurisdiction or eligibility determination?
- [ ] No statute, regulation, licence condition, or scheme rule cited or numbered?
- [ ] No time limit or timescale stated?
- [ ] No statement that the organization breached anything or acted improperly?
- [ ] No merits assessment, strength assessment, or prediction of what the body will do?
- [ ] No characterization or motive attribution?
- [ ] No invented reference, date, registration number, or response content?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "File with the Financial Ombudsman Service — they cover this" | `[VERIFY: identify the body and confirm coverage from its own official site]` |
| "You have six months from the final response" | State no time limit; the user confirms it from the body |
| "They breached the licence conditions for this sector" | State no breach; present the sequence and let the body assess |
| "The ombudsman will almost certainly award compensation" | Predict nothing about what any body will do |
| "This is a strong complaint" | Assess no merits |
| "They strung you along deliberately for months" | Present the dated sequence; adjectives are discounted by caseworkers |
| Send a letter instead of the body's required form | Use their form; this document supports it |
| File before the internal process is finished | Establish exhaustion first — it is usually the gate |
| Use a regulator complaint to seek damages | Route to an attorney; a complaint is generally not a compensation route |
| Assert a step occurred with no proof of sending | Flag `[NEED DOCUMENT:]` |

---

## Adaptations

**By body type:**
- **Ombudsman or dispute scheme:** These typically require a final response or a stated waiting period, and often can direct a specific remedy — ask what remedies are available in a matter of this kind.
- **Sector regulator:** Frequently concerned with patterns and compliance rather than individual redress; your complaint may inform supervision without producing a personal remedy. Say what you want anyway.
- **Licensing or professional body:** Concerned with conduct and standards; the chronology and the professional's own responses matter most, and the outcome is usually about conduct rather than money.
- **Consumer protection office:** Remit varies widely — some mediate, some only record. Ask what it does with a complaint before assuming an outcome.

**By situation/profile:**
- **No final response ever issued:** Record the elapsed time and every attempt with proof; confirm with the body whether it accepts complaints on that basis.
- **Several organizations involved:** Complain separately to the body covering each; one complaint rarely spans two regulated entities.
- **Already in litigation:** Many bodies will not consider a matter before a court. Route to an attorney before filing.
- **Very long history:** Add a one-paragraph summary above the chronology so a caseworker gets the shape immediately.

---

## Related Prompts

- `../cross-cutting/advocacy_escalation_ladder_designer.md` — exhaust the internal rungs first.
- `../cross-cutting/advocacy_correspondence_log_builder.md` — the running record this complaint draws on.
- `../insurance-and-medical/advocacy_external_review_request.md` — for insurance coverage decisions specifically.
- `../privacy-and-data/advocacy_privacy_request_escalation.md` — for privacy requests specifically.
