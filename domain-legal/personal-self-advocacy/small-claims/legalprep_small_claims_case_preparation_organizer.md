---
title: "Small-Claims Case Preparation Organizer (Organize Your Facts, Evidence, and Amount)"
category: legalprep
description: "Help someone bringing or facing a small-claims matter organize the facts, parties, dates, evidence, and the specific amount at issue, with a 'what to bring' checklist. Organizes the user's own information only. Does NOT draft the court claim form or pleading, assess the merits, predict the outcome, or cite law — filing mechanics route to the court self-help center and legal questions to legal aid or an attorney. Not legal advice."
techniques:
  - DS-01
  - DS-21
  - ST-02
  - CM-01
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - small-claims
  - court-preparation
  - evidence
  - documentation
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/small-claims/legalprep_small_claims_hearing_preparation_and_testimony_practice.md
  - domain-legal/family-self-advocacy/legalprep_evidence_inventory_organizer.md
  - domain-legal/family-self-advocacy/legalprep_case_chronology_builder.md
  - domain-legal/family-self-advocacy/legalprep_court_process_explainer.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Help you organize a small-claims matter — the facts of what happened, who the parties are, the key dates, the evidence you have, and the specific dollar amount at issue — into one clean package, with a "what to bring" checklist for the courthouse. This gets your own materials in order **before** you deal with the court's forms. It organizes **your own information** — it does **not** fill out the court's claim form, decide whether your claim is good, predict whether you will win, or tell you what the law is.

**When to use:** You are considering or have decided to file a small-claims case, or you have been served with one and need to organize your side. You want your facts, dates, evidence, and the amount straight before you go to the court's self-help center for the actual forms and filing.

**When NOT to use:** You want the court claim form drafted, want to know the filing fee, deadline, service rules, or dollar limit, or want to know whether you should file → those are filing mechanics and legal questions; the **court self-help center** handles procedure and forms, and legal aid or an attorney handles whether-and-what. You want to know if your claim will win or what it is "worth" → that is legal assessment; route to legal aid or an attorney. You want to prepare for the hearing itself → use `legalprep_small_claims_hearing_preparation_and_testimony_practice.md`.

---

## Safety Block

Stop and use the right pathway if:
- The dispute involves threats, violence, stalking, or an abuser → 911 (emergency, US); National Domestic Violence Hotline 1-800-799-7233. Do not confront the other party; route to the court's protective-order process and, if needed, an advocate.
- You are in crisis → 988 Suicide & Crisis Lifeline (US).

**Where procedure and questions go (official channels):**
- Your **courthouse self-help center** (or the court's small-claims clerk / self-help website) — for the claim form, filing fee, deadlines, service of process, and the dollar limit in your court.
- Your **legal aid** office or **state/local bar association** lawyer-referral service — for legal questions and whether you have a claim.
- `usa.gov` — to help locate your local court.

This prompt is educational support for organizing your own materials. It is not a substitute for legal or court services.

---

## Scope Boundary — Read First

This **organizes your facts, evidence, and the amount at issue.** It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney, the court self-help center, or your jurisdiction's law.** It will **not** draft or complete the court's claim form or any pleading, assess whether your claim is strong, predict the outcome, calculate what you are "owed" as a legal matter, cite or invent statutes or the court's dollar limit, or characterize the other party. Small-claims limits, forms, fees, service rules, and deadlines **vary by state and country and change over time** and are for the **court self-help center**; whether you have a claim is for **legal aid or an attorney.**

---

## Core Principles

1. **Organize the facts; the court and a professional handle the rest.** This is a preparation packet, not a court form. Forms and procedure come from the self-help center; merits come from legal aid or an attorney.
2. **Every fact dated and sourced.** Each event names what happened, when, and the document or record that backs it. No undated assertions.
3. **The amount is a sum of documented items, not a legal valuation.** List each dollar figure you are claiming and the receipt, invoice, estimate, or record behind it. The total is arithmetic on your documents — not an opinion about what the law entitles you to.
4. **Evidence is indexed and labeled.** Each document, photo, message, or receipt is listed with what it shows and where it is stored, ready to become an exhibit. Bring copies; keep originals.
5. **Neutral beats inflammatory.** "Paid [$X] on [date]; work not completed as described" — not "he scammed me." Neutral records read as more credible and are more useful.
6. **Gaps are flagged, not filled.** Missing receipts, dates, or a party's correct legal name are listed as items to obtain — never invented.
7. **You organize; the court self-help center and a professional assess.** Whether to file, on what basis, what form, and whether it will succeed are for the self-help center and legal aid or an attorney — not for this packet to decide.

---

## Your Input

- **Your jurisdiction (state/country) and court, if known:** [required]
- **Your role:** [bringing the claim / responding to one]
- **The parties:** [you; the other party — the correct legal name/business name if known; addresses if known]
- **What happened (facts, briefly):** [in your own words — what was agreed, what went wrong, dates]
- **Key dates:** [agreement, payment, breakdown, demand, being served — as known]
- **The amount at issue and how it breaks down:** [each item + the document behind it]
- **Evidence you have:** [contracts, receipts, invoices, photos, messages, estimates]
- **Any safety dimension?:** [if yes → Safety Block first]

---

## Constraints

**Must:**
- Require the jurisdiction; organize only from the facts the user supplies.
- Build a dated, sourced fact timeline and an indexed evidence list.
- Itemize the amount claimed, each line tied to its supporting document; total by arithmetic only.
- Produce a "what to bring" checklist (copies of evidence, list of witnesses, the amount breakdown).
- Flag missing items as `[NEED DOCUMENT:]` / `[NEED DATE:]` / `[NEED PARTY NAME:]`.
- Route forms, fees, deadlines, service, and the dollar limit to the court self-help center; route merits to legal aid or an attorney.

**Must Not:**
- Draft or complete the court claim form, pleading, or any filing.
- Assess whether the claim is strong, predict the outcome, or state what the user is legally owed.
- Cite or invent statutes, legal standards, or the court's dollar limit/deadlines.
- Characterize the other party or attribute motive.
- Fill factual gaps with assumptions.
- Coach the user to inflate the amount or add unsupported items.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block). Restate the jurisdiction and role (bringing vs. responding), and the boundary: this organizes materials; forms/procedure are for the self-help center, merits for legal aid or an attorney.

### Stage 2 — Identify the Parties Correctly
Capture your name and the other party's correct legal or business name and address as known. Flag an unknown or uncertain legal name as `[NEED PARTY NAME: confirm correct legal/business name — the self-help center can explain how]`.

### Stage 3 — Build the Dated Fact Timeline
Lay out what happened in order — agreement, performance, payment, breakdown, demand — each line dated and tied to its source document. Strip motive and editorializing.

### Stage 4 — Itemize the Amount at Issue
List each dollar figure claimed with the receipt/invoice/estimate behind it; total by arithmetic. Flag any figure without support `[NEED DOCUMENT:]`. Note that whether the law allows a given item is a question for legal aid.

### Stage 5 — Index the Evidence
List each piece of evidence with what it shows and where it is stored, ready to be copied as an exhibit. Note witnesses and what they directly observed. Flag missing evidence.

### Stage 6 — Build the "What to Bring" Checklist and Close
Assemble a courthouse checklist: copies of each exhibit, the itemized amount, the timeline, witness list, and a reminder to confirm forms/fees/date with the self-help center. Route merits and procedure appropriately.

---

## Output Format

```markdown
# Small-Claims Preparation Packet — [Your name] · [jurisdiction/court]
Prepared by [you], [date]. MY OWN PREPARATION — NOT A COURT FILING.
Organizes my facts, evidence, and amount. Does NOT draft the claim form, assess the claim,
predict the result, or cite law.

## 1. Parties
- Me: [name, address].
- Other party: [correct legal / business name — NEED PARTY NAME: confirm] [address].
- My role: [bringing the claim / responding].

## 2. Fact Timeline (dated, sourced, factual)
| Date | Event (facts only) | Source / document |
|---|---|---|
| 2026-04-02 | Agreed [work/goods] for [$amount]. | Written agreement / text |
| 2026-04-15 | Paid [$amount]. | Receipt / bank record |
| 2026-05-01 | [What went wrong]. | Photos / message |

## 3. Amount at Issue (itemized — arithmetic only)
| Item claimed | Amount | Supporting document |
|---|---|---|
| [Refund of payment] | [$X] | Receipt (stored: [folder]) |
| [Cost to redo / repair] | [$Y] | Estimate / invoice [NEED DOCUMENT:] |
| **Total claimed** | **[$X+Y]** | (sum of the above) |
*Whether each item is legally recoverable is for legal aid or an attorney.*

## 4. Evidence Index
| Exhibit | Date | What it shows | Storage | Copy for court? |
|---|---|---|---|---|
| A — [contract] | [date] | [factual description] | [folder] | [ ] |
| B — [receipt] | [date] | [payment of $X] | [folder] | [ ] |

## 5. Witnesses
| Person (name/initials) | What they directly observed | Contact status |
|---|---|---|

## 6. Gaps to Obtain
- [NEED DOCUMENT: ...] / [NEED DATE: ...] / [NEED PARTY NAME: ...]

## 7. What to Bring / Confirm at the Self-Help Center
- [ ] Copies of every exhibit (A, B, …) — bring copies, keep originals.
- [ ] The itemized amount and the timeline.
- [ ] Witness list.
- [ ] Confirm with the court self-help center: correct claim form, filing fee, deadline,
      how to serve the other party, and the dollar limit for this court.

---
For the court self-help center: forms, fees, deadlines, service, and the dollar limit.
For legal aid or an attorney: whether I have a claim and what it may be worth.
*Confirm procedure with the self-help center and merits with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction/court and role captured; procedure routed to the self-help center and merits to legal aid/attorney?
- [ ] Parties identified with correct legal/business name (or flagged `[NEED PARTY NAME:]`)?
- [ ] Fact timeline dated, sourced, and neutral throughout?
- [ ] Amount itemized, each line tied to a document, total by arithmetic only?
- [ ] No statement of what the user is legally owed and no outcome prediction?
- [ ] Evidence indexed with what it shows and storage; gaps flagged `[NEED ...]`?
- [ ] "What to bring / confirm" checklist present, pointing forms/fees/deadline/limit to the self-help center?
- [ ] No court claim form, pleading, or filing drafted?
- [ ] No statute, standard, or dollar limit cited or invented; no characterization of the other party?
- [ ] Output labeled MY OWN PREPARATION — NOT A COURT FILING?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You have a strong breach-of-contract claim" | Organize the facts; route merits to legal aid/attorney |
| Fill out the court's claim form | Organize materials; the self-help center handles the form |
| "The limit is $10,000 and your deadline is 30 days" | Route the limit and deadline to the self-help center |
| "You're legally owed $5,000 in damages" | Itemize documented amounts; recoverability routes to a professional |
| "He defrauded you" | "Paid $X; work not completed as described" — no motive/label |
| Add "pain and suffering" with no basis | List documented items; flag anything unsupported `[NEED DOCUMENT:]` |
| Guess the other party's legal name | Flag `[NEED PARTY NAME:]`; the self-help center explains how to confirm |
| Treat a threat/violence dimension as paperwork | Stop, Safety Block, route to the protective-order process |

---

## Adaptations

**By role:**
- **Bringing the claim:** Foreground the itemized amount and the evidence that supports each item; confirm the correct defendant name with the self-help center.
- **Responding to a claim:** Organize your side of the facts and your evidence; pair with `legalprep_small_claims_hearing_preparation_and_testimony_practice.md`; route any counterclaim question to the self-help center/legal aid.

**By dispute type:**
- **Unpaid debt / loan:** Anchor to the loan record and payment history; each missed payment is a dated line.
- **Goods / services not as agreed:** Anchor to the agreement, payment, and photos/estimates of the problem.
- **Security deposit / property:** Anchor to the lease, the deposit record, move-in/out photos, and the itemized deductions in dispute.

**By situation/profile:**
- **Evidence is mostly digital:** Keep originals; bring clean printed copies as exhibits; note file dates.
- **Safety dimension:** Safety Block first; route to the court's protective process; do not confront.

---

## Related Prompts

- `legalprep_small_claims_hearing_preparation_and_testimony_practice.md` — prepare to present this packet and answer questions at the hearing.
- `../../family-self-advocacy/legalprep_evidence_inventory_organizer.md` — build the exhibit index that feeds Section 4.
- `../../family-self-advocacy/legalprep_case_chronology_builder.md` — build the dated timeline that feeds Section 2.
- `../../family-self-advocacy/legalprep_court_process_explainer.md` — a plain-language explainer of court roles and process (confirm specifics with the self-help center).
- `../../litigation/legal_complaint_drafter.md` — the attorney-side pleading counterpart (for context; not for self-drafting).
