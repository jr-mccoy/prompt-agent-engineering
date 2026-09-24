---
title: "Stipulated Protective Order Drafter"
category: legal/discovery
description: "Draft a negotiated (stipulated) confidentiality protective order — designation tiers including attorneys'-eyes-only, access lists, expert-disclosure procedure, source-code protocol, Rule 502(d) clawback, sealing interface, and end-of-case disposition — distinct from a contested motion for protective order and from domestic-violence or harassment protective orders."
techniques:
  - DT-01
  - OC-04
  - QA-02
  - DS-33
difficulty: advanced
tags:
  - legal
  - discovery
  - protective-order
  - confidentiality
  - attorneys-eyes-only
  - keep-trade-secrets-private-in-lawsuit
  - sharing-confidential-documents-with-other-side
updated: "2026-09-24"
related_prompts:
  - domain-legal/discovery/legal_privilege_review_protocol.md
  - domain-legal/discovery/legal_meet_and_confer_letter.md
  - domain-legal/contracts-transactional/legal_nda_mutual_drafter.md
---

# Stipulated Protective Order Drafter

**Objective:** Produce a proposed stipulated protective order the court will sign and both sides can live with through trial: designation tiers matched to what is actually sensitive in the case, precise access rules per tier, a workable challenge procedure, an expert/consultant disclosure mechanism, a source-code or restricted-data protocol when needed, a non-waiver/clawback order, and a clear interface with the court's separate sealing standard — plus a negotiation memo showing where your draft departs from the court's model form.

> **Scope guard — attorney-facing.** For litigation counsel negotiating a confidentiality order in civil discovery. "Protective order" here means a Rule 26(c)-type discovery order, **not** a domestic-violence, harassment, or stalking restraining order — for those, see `domain-legal/divorce/legal_domestic_violence_protective_order_petition.md` (attorney) or `domain-legal/personal-self-advocacy/harassment-stalking/legalprep_protective_order_preparation_organizer.md` (self-represented).

## When to Use

- Discovery will involve trade secrets, pricing, customer data, personnel files, health or financial information, or source code, and no order is in place.
- Opposing counsel sent a draft order and you need to mark it up with reasons.
- An existing order lacks a tier (e.g., AEO) or a protocol (e.g., source code) the case now needs.

**Not this prompt if:**
- The parties cannot agree and you must move the court — use `domain-legal/discovery/legal_motion_for_protective_order_drafter.md`.
- You are designing the privilege review workflow itself — use `domain-legal/discovery/legal_privilege_review_protocol.md` (this prompt drafts only the order's clawback provision).
- You need a pre-litigation confidentiality contract between businesses — use `domain-legal/contracts-transactional/legal_nda_mutual_drafter.md`.

## Inputs

- **Jurisdiction and court (required):** Court, judge, and whether the court or judge has a model/default protective order or standing order on confidentiality and sealing `[VERIFY]`. If a model form exists, supply it — the draft starts from it.
- **Case profile:** Claims, parties (competitors? individuals?), and the categories of sensitive information each side will produce.
- **Your client's position:** Producing-heavy or receiving-heavy; in-house counsel access needs; competitive-decision-maker concerns.
- **Special data:** Source code, regulated personal data (health, financial, biometric, minors), export-controlled data, cross-border data.
- **Experts/consultants:** Whether any are likely to be employees or consultants of competitors.
- **Opposing draft (if any):** Paste it.

## Method

**Ground rules:** Do not invent the court's model-order text, sealing standard, or case law on AEO or prosecution bars — use `[CITE: …]` / `[VERIFY: …]`. Draft only for the stated court. Every departure from a supplied model form is listed and justified.

1. **Inventory the sensitive information.** Classify each category by harm if disclosed to the other side's business people (none / moderate / severe) and by regulatory overlay.
2. **Choose tiers conditionally.** Default: one CONFIDENTIAL tier. Add HIGHLY CONFIDENTIAL – ATTORNEYS' EYES ONLY only when severe-harm categories exist; add a RESTRICTED – SOURCE CODE tier only when code will be produced. Do not add tiers the case does not need — each adds designation fights.
3. **Define access per tier.** Outside counsel and staff; a limited number of designated in-house counsel (and whether they may see AEO); retained experts after disclosure; the court and its personnel; court reporters; vendors; mock jurors under confidentiality undertakings; authors/recipients of the document.
4. **Draft the expert/consultant disclosure procedure.** What is disclosed (CV, current and recent engagements), the objection window `[VERIFY or negotiate]`, and who bears the burden of moving if the parties disagree.
5. **Draft designation mechanics.** How to mark documents, native files, deposition testimony (with a post-transcript designation window), and inadvertent failure to designate; a prohibition on blanket designation.
6. **Draft the challenge procedure.** Written challenge, conferral, and which party must move and bears the burden `[VERIFY: court's practice]`; material stays protected pending resolution.
7. **Add conditional protocols.** Source code (stand-alone review computer, location, printing limits, logs); regulated data (minimum-necessary production, de-identification, breach notice); prosecution bar or acquisition bar only if the case justifies it — flag as contested.
8. **Draft the clawback order.** Non-waiver order under Federal Rule of Evidence 502(d) (or the state analog `[VERIFY]`), return/sequester/destroy procedure, and no requirement to prove reasonable precautions if the court permits `[VERIFY]`.
9. **Draft the sealing interface.** State expressly that designation under the order does not itself justify sealing; filing parties follow the court's sealing rule `[VERIFY: local rule]`; the designating party bears the burden to support sealing.
10. **Draft duration and disposition.** Survival after termination; return or destruction within a set period after final disposition; counsel's archival copy of pleadings and work product.
11. **Stress-test from the other side.** For each provision favoring your client, write the likely objection and whether the court's model form would side with it; produce the negotiation memo.

## Output Format

```markdown
# Stipulated Protective Order Package — {Caption}

## 1. Sensitive-Information Inventory
| Category | Producing party | Harm if disclosed (N/M/S) | Regulatory overlay | Tier |

## 2. [PROPOSED] STIPULATED PROTECTIVE ORDER (draft)
1. Purposes and Limitations
2. Definitions
3. Scope
4. Duration
5. Designating Protected Material
6. Challenging Designations
7. Access to and Use of Protected Material (by tier)
8. Disclosure of Experts and Consultants
9. {Source Code Protocol — if applicable}
10. {Regulated Data Handling — if applicable}
11. Protected Material Subpoenaed or Ordered Produced in Other Litigation
12. Unauthorized Disclosure
13. Non-Waiver and Clawback (FRE 502(d) or analog [VERIFY])
14. Filing Under Seal
15. Final Disposition
16. Miscellaneous — including that nothing restricts a party's use of its own documents or information, and that the order does not bar disclosures to a government agency required by law or protected whistleblower reporting `[VERIFY: jurisdiction-specific carve-outs]`
Exhibit A — Acknowledgment and Agreement to Be Bound

## 3. Negotiation Memo
| Provision | Departure from model form | Reason | Likely objection | Fallback |

## 4. Verification Items
```

## Verification

- [ ] Jurisdiction lock: court's model order, sealing rule, and 502(d)/analog addressed for the stated forum, each `[VERIFY]` unless supplied.
- [ ] Citation discipline: no invented model-form language or case law on AEO, prosecution bars, or sealing.
- [ ] Scope discipline: discovery confidentiality only — no restraining-order content, no privilege-review workflow.
- [ ] Every tier is justified by at least one inventory row.
- [ ] Access rules stated for every tier, including in-house counsel and experts.
- [ ] Sealing section says designation alone does not justify sealing.
- [ ] Clawback provision includes return/sequester/destroy mechanics.
- [ ] Every departure from a supplied model form appears in the negotiation memo.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Three tiers by default in a case with no trade secrets | Tier only what the inventory justifies |
| Treating the protective order as authority to file under seal | Separate sealing standard; designating party must support sealing |
| Omitting deposition-testimony designation | Include a post-transcript designation window and interim treatment |
| Prosecution bar inserted without case-specific basis | Flag as contested; include only with a stated reason |
| Ignoring the court's model form | Start from it; justify every deviation in the memo |
| Confusing a discovery protective order with a restraining order | Scope guard routes the latter elsewhere |

## Example

**Input sketch:** Federal trade-secret case; plaintiff Veridian Coatings (fictional) and defendant Tallis Polymers are direct competitors. Plaintiff will produce formulation data; defendant will produce customer pricing and some source code for its mixing-control software. The judge has a model order with two tiers and no source-code protocol.

**Output (abridged):**

> **Inventory (excerpt).** Formulation data — Plaintiff — Severe — none — AEO. Customer pricing — Defendant — Severe — none — AEO. Mixing-control source code — Defendant — Severe — export screen `[VERIFY]` — RESTRICTED – SOURCE CODE.
>
> **§ 9 Source Code Protocol (excerpt).** Source code will be made available on a stand-alone, non-networked computer at the producing party's outside counsel's office. The receiving party may request printouts of no more than a reasonable number of consecutive pages `[negotiate]`, which will be designated RESTRICTED – SOURCE CODE…
>
> **§ 14 Filing Under Seal (excerpt).** A party's designation of material under this Order does not by itself establish that the material may be filed under seal. A party seeking to file Protected Material must comply with `[VERIFY: local sealing rule]`, and the Designating Party bears the burden of supporting the sealing request.
>
> **Negotiation memo row.** § 9 — model order has no source-code tier — needed because defendant's control software is at issue — likely objection: plaintiff wants printouts without a page cap — fallback: cap per request with a stipulated process to exceed it.
