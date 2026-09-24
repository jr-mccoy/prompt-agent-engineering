---
title: "Proof of Claim Drafter"
category: legal/bankruptcy-restructuring
description: "Draft a creditor's proof of claim package — claim amount build-up, secured / priority / unsecured classification with the basis for each, supporting-documentation checklist, and an attachment narrative — while flagging bar-date, perfection, and setoff issues for verification and never inventing a priority category or a filing deadline."
techniques:
  - ST-03
  - CM-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - legal
  - bankruptcy
  - proof-of-claim
  - claims
  - priority
  - secured-claims
  - creditor-rights
updated: "2026-09-24"
reasoning:
  styles: [analytic, evidential, taxonomic]
  stakes: high
  horizon: days
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: regulated
  collaboration: solo_or_team
  output_format: structured
  user_role: [lawyer]
  mode: [document, audit]
related_prompts:
  - domain-legal/bankruptcy-restructuring/legal_chapter_11_plan_analysis.md
  - domain-legal/bankruptcy-restructuring/legal_automatic_stay_motion_set.md
  - domain-finance/accounting-controllership/finance_receivables_aging_triage.md
  - domain-legal/contracts-transactional/legal_payment_terms_and_late_fee_review.md
---

# Proof of Claim Drafter

**Objective:** Prepare a creditor's proof of claim that will survive objection: an amount that reconciles to the petition date, a classification (secured, priority, administrative-expense candidate, general unsecured) with the statutory basis for each portion, the documentation the rules require attached or explained, and a short attachment narrative. The drafter also surfaces issues that change the claim's value — perfection defects, setoff and recoupment rights, reclamation or goods-delivered-before-petition administrative claims, and guarantor recovery — and marks the bar date and every rule reference for verification.

**When to use:**
- A customer, borrower, tenant, or counterparty has filed and you represent a creditor.
- Reviewing a client-prepared claim before filing.
- Amending a claim after the schedules, plan, or a claim objection changes the picture.

**Distinct from:**
- `domain-finance/accounting-controllership/finance_receivables_aging_triage.md` — the AR team's collection triage; this prompt turns the receivable into a legally classified claim.
- `domain-legal/personal-self-advocacy/debt-collection/` — consumer debtors responding to collectors; the opposite side and a different reader.
- Claim *objections* — this prompt drafts the creditor's claim; it notes predictable objections but does not draft the objection.

**Audience:** Creditors' counsel and supervised paralegals.

---

## Your Input

- **Case:** [Debtor name, case number, district, chapter, petition date]
- **Bar date(s):** [General bar date and any governmental-unit bar date from the notice — paste the notice text; do not estimate]
- **Creditor:** [Name, entity type, notice address, whether scheduled by the debtor and in what amount / as disputed?]
- **Underlying obligation:** [Contract, note, lease, invoices, judgment — paste key terms: interest, fees, late charges, attorney-fee clause]
- **Petition-date balance build-up:** [Principal, pre-petition interest, fees, charges — with dates]
- **Collateral / security:** [Security agreement, financing statement, mortgage, possessory lien — perfection details and collateral value]
- **Goods or services delivered shortly before petition:** [Dates and values — relevant to administrative-priority and reclamation analysis]
- **Setoff / recoupment:** [Amounts the creditor owes the debtor]
- **Guarantors / co-obligors:** [Names and instruments]
- **Payments received in the pre-petition period:** [Dates and amounts — preference exposure affects strategy]

---

## Constraints

### Must
- Build the amount **as of the petition date**; separate principal, pre-petition interest, and fees. Post-petition interest and fees are claimed only where the Code permits (e.g., oversecured claims) and flagged `[VERIFY]`.
- Classify each portion with its **statutory basis**: secured (to the extent of collateral value), priority (name the specific priority category and why the facts fit it), administrative-expense candidate (flag that it usually requires a separate request, not the proof of claim alone), general unsecured.
- Produce a **documentation checklist** matched to the claim type — writings the claim is based on, evidence of perfection for secured claims, itemization for consumer-credit claims, escrow and arrearage statements for home-mortgage claims `[VERIFY: current Rule 3001 requirements and official form attachments]`.
- Flag **predictable objections** (amount, classification, timeliness, documentation) and pre-empt each in the narrative.
- Identify whether the creditor's **filing submits it to the court's jurisdiction** in a way that matters for any pending litigation or jury right `[NEED HOLDING: controlling authority in this circuit]`.
- Mark the bar date as `[VERIFY from notice]` unless pasted from the notice.

### Must Not
- Invent priority categories, dollar caps on priority amounts, or time windows for administrative claims. Mark `[VERIFY: §507 subsection + current cap]`.
- Claim a secured status the perfection facts do not support; an unperfected lien is exposed to the trustee's avoiding powers.
- Include post-petition interest or attorney fees on an undersecured or unsecured claim without flagging that they are generally not allowable.
- Fabricate account histories or fill gaps in the build-up; missing data becomes `[NEED: …]`.
- Treat the proof of claim as the vehicle for an administrative-expense request without flagging the separate motion.

---

## Instructions

1. **Confirm the case posture.** Chapter, petition date, bar date(s) from the notice, whether the claim was scheduled and how (a claim scheduled as undisputed may or may not require filing depending on chapter `[VERIFY]`).
2. **Reconcile the amount** to the petition date. Show the arithmetic. Exclude post-petition amounts unless a basis exists and is flagged.
3. **Test security.** Identify the lien, its perfection method and date, and the collateral. Split the claim into secured (up to collateral value) and unsecured deficiency. Flag perfection timing within any avoidance look-back window `[VERIFY]`.
4. **Test priority.** For each portion arguably entitled to priority, name the category, the element facts, and any cap `[VERIFY]`. If none, say so.
5. **Screen administrative-expense and reclamation rights** for goods delivered shortly before the petition; note the separate procedure and deadline `[VERIFY]`.
6. **Address setoff and recoupment.** Setoff is subject to the stay and requires relief or agreement; recoupment within a single transaction may not. Flag which applies `[NEED HOLDING: circuit authority]`.
7. **Build the documentation checklist** and note each document as attached / to be obtained / unavailable with explanation.
8. **Draft the attachment narrative** (one to two pages): basis, computation, classification, reservation of rights (to amend, to assert administrative claims, setoff, and against guarantors).
9. **List predictable objections** and the response to each.

---

## Output Format

```markdown
# Proof of Claim Package — {Creditor} in re {Debtor}, Case No. {…} (Bankr. {district})
**Chapter:** {…}  |  **Petition date:** {…}  |  **Bar date:** {from notice / [VERIFY]}

## 1. Official Form Field Map
| Form field | Entry | Source document |

## 2. Petition-Date Amount Build-Up
| Component | Amount | Period | Basis (contract §) |
| **Total as of petition date** | | | |

## 3. Classification
| Portion | Amount | Class | Statutory basis | Facts supporting | [VERIFY] |
|---|---|---|---|---|---|
| Secured | | Secured | | | |
| Deficiency | | GUC | | | |
| {Priority} | | §507(a)(_) | | | [VERIFY: category + cap] |

## 4. Rights Not Captured by the Claim
- Administrative-expense request: {yes/no — basis — separate motion}
- Setoff / recoupment: {…}
- Guarantor recovery: {…}

## 5. Documentation Checklist
| Document | Required because | Status |

## 6. Attachment Narrative
{draft text}

## 7. Predictable Objections and Responses
| Objection | Response | Evidence |

## 8. Verification Items
```

---

## Worked Example

**Input (abridged):** Equipment lessor-lender; Chapter 11 debtor (manufacturer) filed 2026-06-02. Note balance $412,000 principal; $9,850 pre-petition interest; $4,100 late fees; attorney-fee clause. UCC-1 filed 2024-03-11 covering specified machinery; appraisal $300,000. Creditor also delivered $38,000 of replacement parts on 2026-05-20. Creditor owes debtor $6,200 in a volume rebate under a separate agreement. Bar date pasted from notice: 2026-09-15.

**Output (excerpt):**

> **2. Build-up.** $412,000 + $9,850 + $4,100 = **$425,950** as of 2026-06-02. Attorney fees incurred post-petition excluded: the claim is undersecured, so post-petition fees are generally not allowable `[VERIFY: §506(b) applies only to oversecured claims]`.
>
> **3. Classification.** Secured $300,000 (UCC-1 perfected well before any preference window `[VERIFY: look-back]`); general unsecured deficiency $125,950. No §507 priority identified for the note.
>
> **4. Rights not captured.** The $38,000 of parts delivered 13 days pre-petition is a candidate for administrative-expense treatment for goods received in the ordinary course shortly before filing `[VERIFY: §503(b)(9) window and whether "parts" are "goods"]` — this requires a separate request; the proof of claim should reserve it and not merge it into the GUC total. The $6,200 rebate arises under a separate agreement, so it is setoff (stay applies; seek relief or stipulation), not recoupment.
>
> **7. Predictable objection:** Debtor disputes the appraisal and argues a lower collateral value, enlarging the unsecured portion. Response: reserve right to amend; request valuation hearing timing aligned with plan confirmation.

---

## Verification

- [ ] Jurisdiction lock: district, chapter, and petition date stated; no out-of-circuit authority presented as controlling.
- [ ] Amount reconciles arithmetically to the petition date.
- [ ] Every classification has a statutory basis and element facts; priority categories and caps marked `[VERIFY]`.
- [ ] Secured status supported by perfection facts; deficiency computed.
- [ ] Administrative / reclamation rights flagged as separate procedures.
- [ ] Setoff vs. recoupment distinguished.
- [ ] Bar date taken from the notice or marked `[VERIFY from notice]`.
- [ ] Citation discipline: no invented cases, holdings, or rule text.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Claiming the full balance as secured | Secured only to the extent of collateral value; split off the deficiency |
| Adding post-petition interest and fees to an undersecured claim | Generally not allowable; include only for oversecured claims and flag |
| Folding a pre-petition goods administrative claim into the proof of claim total | It needs a separate request; reserve it in the narrative |
| Inventing a priority category to improve recovery | Name a specific §507 subsection with element facts or state "none" |
| Estimating the bar date from typical timelines | Take it from the notice; governmental-unit bar dates differ |
| Treating setoff as self-executing | Setoff is subject to the stay; recoupment analysis is separate |
| Ignoring the effect of filing a claim on pending litigation or jury rights | Flag and route to litigation counsel before filing |
