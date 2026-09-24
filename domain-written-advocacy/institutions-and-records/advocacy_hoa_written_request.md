---
title: "HOA Written Request — Respond to a Violation, Contest a Fine, or Ask the Association to Act"
category: advocacy
description: "[SELF-SUBMIT] Help a homeowner or unit owner draft THEIR OWN letter to a homeowners', condominium, or owners' association or its managing agent — responding to a violation notice or fine, asking for a maintenance or common-area repair, requesting association records, or seeking an architectural or modification approval — anchored to the association's OWN governing documents quoted by section, with a request for a hearing or board review where the documents provide one. Screens liens, foreclosure, collections, and litigation to an attorney first. Does NOT cite property or association statutes as authority, interpret governing documents, state whether a fine is enforceable, advise withholding assessments, predict outcomes, or invent rule text. Distinct from domain-legal/personal-self-advocacy/housing-landlord-tenant/ (renters) and advocacy_service_nonperformance_demand (contractors). Not legal advice."
techniques:
  - CM-01
  - CM-02
  - RT-05
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - hoa
  - housing
  - self-submit
  - community-association
updated: "2026-09-24"
related_prompts:
  - domain-written-advocacy/cross-cutting/advocacy_correspondence_log_builder.md
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-written-advocacy/products-and-warranty/advocacy_service_nonperformance_demand.md
  - domain-legal/personal-self-advocacy/housing-landlord-tenant/legalprep_landlord_notice_response_preparer.md
---

**Purpose:** Help you write **your own** letter to your homeowners', condo, or owners' association — or the management company acting for it — in one of four situations: you received a **violation notice or fine** and want to respond; the association has **not done something it is responsible for** (a repair, a common-area problem); you want **association records**; or you need an **architectural or modification approval**. Every letter is anchored to the association's own governing documents, quoted by section, because in this relationship those documents — not general knowledge about HOAs — are what the board reads against.

**When to use:** You own in an association, the matter is still at the letter stage, and you have (or can get) a copy of the declaration, bylaws, and rules.

**When NOT to use:** You rent from an owner → `domain-legal/personal-self-advocacy/housing-landlord-tenant/`. The dispute is with a contractor the association hired to work inside your unit and you contracted with them yourself → `../products-and-warranty/advocacy_service_nonperformance_demand.md`. A neighbour, not the association, is the problem → ask the association to act under its rules, or route harassment to `domain-legal/personal-self-advocacy/harassment-stalking/`.

---

## Boundary & Routing Block

Use a different pathway if:
- **The notice mentions a lien, foreclosure, collections, an attorney for the association, or a lawsuit** → route to an attorney or **legal aid** now. These can put the home itself at risk, and a letter is not a substitute.
- **The letter from the association states a hearing or response date** → **act on that date.** Whether it is the only relevant date is a question for an attorney.
- **The matter involves a disability accommodation** → the request can be made in writing here, but whether a rule must be modified is a legal question; route to an attorney or a fair-housing service `[VERIFY: identify the correct body from an official source]`.
- **You are tempted to withhold assessments until they fix something** → do not. Withholding can create the arrears that lead to liens. Keep paying and dispute in writing.
- **Water, structural, electrical, or gas hazards** → report to the association immediately and, where there is danger, to emergency services first; the letter records it afterwards.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal services.

---

## Scope Boundary — Read First

This **drafts your own letter to your association for you to send**. It is **not legal advice, a legal filing, an interpretation of your governing documents, or a substitute for an attorney or your jurisdiction's law.** It will **not** cite a common-interest, condominium, or property statute as authority; tell you what a governing-document provision means or whether the association followed it; state whether a fine, lien, or rule is enforceable; state notice, hearing, or records-response periods; tell you who is responsible for a repair; name a housing or ombudsman body; predict the board's decision; or invent rule text, section numbers, fine amounts, or dates. Association rules **vary by association, state, and country, and statutes change.** Where such a concept appears it is flagged *verify with your governing documents and an attorney*.

---

## Core Principles

1. **Their documents, quoted by section.** Quote the provision the notice cites, and any provision you rely on, with its section number and document name. Paraphrase invites disagreement about what it says.
2. **Ask for the process the documents describe.** Many associations' documents describe a hearing, a board review, or an appeal. Ask for it by referencing the section — do not assert it exists if you have not found it.
3. **Facts with photographs and dates.** Violation responses and repair requests are decided on what the board can see: dated photos, prior requests, the manager's replies.
4. **One matter per letter.** A fine response that also relitigates a parking dispute and a budget complaint gets the smallest item answered.
5. **The board are neighbours.** A firm, neutral tone preserves a relationship you will live inside for years. Threats and accusations of bad faith are refused here and routed to an attorney.
6. **Keep paying assessments.** Dispute in writing; do not self-help by withholding.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Which situation:** [violation or fine response / repair or action request / records request / architectural approval]
- **Association and managing agent, and the address or portal it designates:** [names]
- **Your unit/lot and account number:** [#]
- **The notice or decision, verbatim, if any:** [date, violation described, section cited, fine amount, any hearing date]
- **Governing-document provisions you rely on, quoted:** [document, section, exact text] or [NEED DOCUMENT: governing documents]
- **The facts:** [what, when, with photographs or records]
- **Prior requests and replies:** [date, channel, to whom, outcome]
- **Lien, foreclosure, collections, association attorney, or lawsuit?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction and the situation type; use only facts and document text the user supplies.
- Screen lien, foreclosure, collections, and litigation first, and route to an attorney.
- Quote the association's governing documents by document and section; flag `[NEED DOCUMENT:]` where the user lacks them and add a request for them.
- Ask for the hearing, review, or appeal the documents describe, referencing the section, or ask whether one exists.
- Attach dated evidence to each factual statement.
- Advise continuing to pay assessments.
- Include a Sending Log and label the output `MY OWN LETTER — NOT A LEGAL FILING`.

**Must Not:**
- Cite or invent a statute or state a notice, hearing, or records-response period.
- Interpret a governing-document provision or state whether the association complied.
- State whether a fine, rule, or lien is enforceable or valid.
- Assign legal responsibility for a repair.
- Advise withholding assessments.
- Accuse board members of bad faith or threaten legal action.
- Invent rule text, section numbers, amounts, or dates.

---

## Instructions

### Stage 1 — Screen and Frame
Screen lien, foreclosure, collections, association attorney, and litigation → attorney. Record any hearing or response date and tell the user to act on it. Confirm the situation type.

### Stage 2 — Anchor to the Documents
Quote the provision the association cited and any the user relies on, verbatim with section. Where the user lacks the documents, the first letter requests them.

### Stage 3 — Assemble the Facts
Build a dated fact list with evidence per item — photos, prior requests, replies. Keep to the one matter.

### Stage 4 — Draft the Ask
One specific ask per situation: withdraw or reduce the fine and schedule a hearing; complete the repair by a date; provide named records; approve the modification as described.

### Stage 5 — Close
Compose the dated letter with the Sending Log and a note on escalation.

---

## Output Format

```markdown
MY OWN LETTER TO THE ASSOCIATION — NOT A LEGAL FILING
From: [your name], owner of [unit/lot], account [#], [contact]. To: [board of directors, c/o
managing agent], at [designated address/portal]. Date: [YYYY-MM-DD]. Delivery: [method]. Keep a copy.
This is my own letter. It does NOT interpret the governing documents, cite law, or state whether
any rule or fine is enforceable. I continue to pay my assessments.

Re: [Response to violation notice dated YYYY-MM-DD / Request for repair / Records request /
Architectural approval request] — [unit/lot]

## The notice or matter
[Verbatim: "[violation as described]", citing [document, section]; fine [$X]; hearing date [if stated].]

## What the governing documents say
[Document], section [#]: "[exact quote]"   [or: NEED DOCUMENT: please send the current version]

## The facts
| Date | Fact | Evidence enclosed |
|---|---|---|
| [YYYY-MM-DD] | [e.g. the item cited was removed] | [dated photo] |

## What I am asking
[One ask — e.g. "Please withdraw the fine, or schedule the hearing described in section [#] before
any fine is confirmed." / "Please repair [item] by [date] and tell me in writing who will do it."]

Please respond in writing by [date].
[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Outcome |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [board c/o agent] | [#] | [receipt] | [YYYY-MM-DD] | [ ] |

Note to self: I will keep paying assessments and act on any date the association gives me.
Enforceability and my rights are questions for an attorney. *Verify with your governing documents.*
```

---

## Verification

- [ ] Lien, foreclosure, collections, and litigation screened and routed?
- [ ] Hearing or response date recorded and the user told to act on it?
- [ ] Governing documents quoted by document and section, or requested?
- [ ] Hearing or review requested by reference to a section, not asserted from memory?
- [ ] Each fact matched to dated evidence?
- [ ] One matter, one ask?
- [ ] Advice to keep paying assessments included; no withholding advice?
- [ ] No statute, period, interpretation, or enforceability statement?
- [ ] No accusation of bad faith or legal threat?
- [ ] Sending Log included; no invented rule text?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "State law requires a hearing before any fine" | Ask for the hearing section [#] describes, or ask whether one exists |
| "This fine is unenforceable" | Quote the provision and the facts; enforceability is for an attorney |
| "The HOA is responsible for this leak under the declaration" | Quote the provision; ask the association to confirm who will repair |
| "I'll withhold dues until this is fixed" | Keep paying; dispute in writing |
| "The board is acting in bad faith and I'll sue" | Firm, neutral ask; threats route to an attorney |
| "Rule 7.2 says…" with no document in hand | `[NEED DOCUMENT: governing documents]` and request them |
| One letter covering fine, parking, and budget | One matter per letter |
| "Records must be provided in 10 days" | Ask for them by a date you set; cite no period |

---

## Adaptations

**By situation:**
- **Violation or fine:** Address the specific violation as described; if it has been cured, say when with a dated photo. If you dispute that it occurred, state the facts, not a legal view.
- **Repair or action request:** Location, when first noticed, when first reported, what has happened since; ask who will repair and by when.
- **Records request:** Name the records specifically — minutes of a dated meeting, the current budget, a reserve study — and ask how and when they can be inspected or copied, and at what cost.
- **Architectural approval:** Describe the change with drawings or product details, quote the approval provision, and ask for a written decision with reasons.

**By escalation stage:**
- **Manager unresponsive:** Address the board directly, copying the manager, with the prior request dates — see `../cross-cutting/advocacy_escalation_ladder_designer.md`.

---

## Related Prompts

- `../cross-cutting/advocacy_correspondence_log_builder.md` — associations run on long timelines; keep the record.
- `../cross-cutting/advocacy_escalation_ladder_designer.md` — manager → board → external route.
- `../products-and-warranty/advocacy_service_nonperformance_demand.md` — if the dispute is with a contractor you hired.
- `domain-legal/personal-self-advocacy/housing-landlord-tenant/legalprep_landlord_notice_response_preparer.md` — the renter's equivalent for a formal notice.
