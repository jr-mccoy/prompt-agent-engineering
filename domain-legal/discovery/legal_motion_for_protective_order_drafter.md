---
title: "Motion for Protective Order Drafter"
category: legal/discovery
description: "Draft a contested motion for protective order (or to quash/modify a subpoena) against overbroad discovery, an improper deposition, or an unduly burdensome subpoena — good cause shown with specific facts, conferral certification, proportionality analysis, and a narrowly framed alternative order — distinct from the stipulated confidentiality order and from written objections."
techniques:
  - RT-05
  - NE-23
  - CM-03
  - QA-01
difficulty: advanced
tags:
  - legal
  - discovery
  - protective-order
  - motion-to-quash
  - proportionality
  - other-side-asking-for-too-much
  - stop-a-deposition
updated: "2026-09-24"
related_prompts:
  - domain-legal/discovery/legal_discovery_response_objections.md
  - domain-legal/discovery/legal_meet_and_confer_letter.md
  - domain-legal/regulatory-compliance/legal_subpoena_or_cid_response_strategy.md
---

# Motion for Protective Order Drafter

**Objective:** Produce a motion that wins on the record rather than on adjectives: a precise statement of the discovery at issue, a conferral certification that shows real effort, good cause established through declarations with concrete facts about burden, harm, or impropriety, a proportionality analysis tied to the factors in the operative rule, and a proposed order that asks for the narrowest relief that solves the problem.

> **Scope guard — attorney-facing.** For litigation counsel seeking relief from discovery served on a client (party or nonparty). It does not draft a stipulated confidentiality order or restraining order. A self-represented recipient of a subpoena should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

## When to Use

- Requests, interrogatories, or a deposition notice seek plainly disproportionate, harassing, or privileged material and conferral has failed.
- A deposition of a senior executive, an opposing lawyer, or a repeat deponent is noticed and a lesser alternative exists.
- A nonparty client received a subpoena imposing undue burden or seeking protected material (motion to quash or modify).
- You need a confidentiality order entered over the other side's objection.

**Not this prompt if:**
- The parties agree on a confidentiality order — use `domain-legal/discovery/legal_protective_order_drafter.md`.
- You only need to serve written objections and responses — use `domain-legal/discovery/legal_discovery_response_objections.md`.
- You are the requesting party seeking to force production — use `domain-legal/discovery/legal_motion_to_compel_drafter.md`.

## Inputs

- **Jurisdiction and court (required):** Court, judge, operative rules (e.g., FRCP 26(b)(1), 26(c), 45(d)(3), or state analogs), local rules on discovery motions (pre-motion letter or conference, joint-statement format, page limits) `[VERIFY]`.
- **The discovery at issue:** Verbatim requests, notice, or subpoena, with service date and compliance date.
- **Conferral record:** Letters, emails, call dates, participants, and each side's final position.
- **Good-cause facts:** Who can attest to burden (hours, cost, systems), confidentiality harm, harassment, or duplication — and what documents support it.
- **Case context:** Claims and defenses, what discovery has already been produced, the discovery cutoff.
- **Relief sought:** Forbid, limit scope, set conditions (time, place, method, confidentiality), shift cost, or require an alternative (interrogatory, 30(b)(6), lower-level witness first).

## Method

**Ground rules:** Do not invent case names (including "apex" or attorney-deposition authority), holdings, or quotations; use `[CITE: proposition]` / `[NEED HOLDING: …]`. Do not state filing deadlines, page limits, or conferral requirements not supplied — `[VERIFY: …]`. Draft for the stated forum only; if the motion concerns a subpoena, confirm which court must hear it `[VERIFY: compliance-court rule]`.

1. **Timing check first.** Confirm the motion can be filed before the compliance or deposition date and whether filing stays the obligation in this forum `[VERIFY]`. If time is short, flag the need for an emergency or expedited procedure.
2. **Isolate the requests.** Group the challenged items by ground (overbreadth, burden, privilege/work product, confidentiality, harassment, duplication, improper deponent). Do not challenge everything; drop items where your ground is weak.
3. **Build the good-cause record.** For each ground, draft declaration paragraphs with specific, first-hand facts — hours, costs, systems, harm scenarios. Conclusory statements ("unduly burdensome") are replaced by numbers or marked `[NEED: fact from declarant]`.
4. **Apply proportionality factor by factor.** Importance of the issues, amount in controversy, relative access to information, resources, importance of the discovery to resolving issues, and burden versus benefit `[VERIFY: factor list in operative rule]`. Concede factors that cut against you and explain why the balance still favors relief.
5. **Anticipate the opposition.** List the three strongest arguments the requesting party will make and answer each in the brief (e.g., "the executive has unique first-hand knowledge").
6. **Draft the conferral certification.** Dates, participants, method, proposals made, and why impasse was reached — factual, not argumentative.
7. **Frame the narrowest effective relief.** Offer an alternative (date limit, custodian limit, sequencing, written deposition, cost-sharing) so the court has an easy middle path.
8. **Assemble the motion package.** Notice of motion, memorandum, declarations, conferral certification, and proposed order.

## Output Format

```markdown
# Motion for Protective Order Package — {Caption}

## 1. Timing and Forum Check
- Compliance / deposition date: {…} | Filing target: {…} | Stay effect: [VERIFY] | Hearing court: {…}

## 2. Challenge Map (internal)
| Item | Ground | Strength (H/M/L) | Evidence for good cause | Include? |

## 3. Notice of Motion (draft)
## 4. Memorandum
I. Introduction (relief requested in one paragraph)
II. Background (discovery at issue; conferral)
III. Legal Standard [CITE placeholders]
IV. Argument
   A. {Ground 1} — facts → rule → proportionality factors
   B. {Ground 2} ...
   C. The Requested Alternative Is Narrow and Workable
V. Conclusion
## 5. Declaration(s) — fact paragraphs by ground
## 6. Conferral Certification
## 7. [Proposed] Order
## 8. Anticipated Opposition and Responses
## 9. Verification Items
```

## Verification

- [ ] Jurisdiction lock: rule, local procedure, and hearing court tied to the stated forum; unknowns `[VERIFY]`.
- [ ] Citation discipline: every case or quotation is supplied or a placeholder.
- [ ] Scope discipline: only the items in the challenge map are contested; no relief requested beyond them.
- [ ] Timing check done; motion is filed before compliance or an emergency path is flagged.
- [ ] Each ground has declaration-level facts, not conclusions.
- [ ] Proportionality addressed factor by factor, including unfavorable factors.
- [ ] Conferral certification is dated and specific.
- [ ] Proposed order offers the narrowest effective relief.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| "Overbroad and unduly burdensome" with no numbers | Declaration facts: hours, cost, systems, custodians |
| Challenging every request to look thorough | Challenge map; drop weak items to protect credibility |
| All-or-nothing relief | Offer a narrower alternative the court can grant |
| Filing after the compliance date | Timing check is step 1 |
| Filing a subpoena motion in the wrong court | Confirm the compliance-court rule `[VERIFY]` |
| Inventing "apex doctrine" case law | `[CITE: …]`; standards vary by forum |

## Example

**Input sketch:** State-court products case; plaintiff noticed the deposition of the CEO of defendant Pellam Appliances (fictional) and served a request for "all communications concerning dishwasher safety" for 15 years. Conferral on 2026-09-02 and 2026-09-09 produced no agreement. Deposition set for 2026-10-06.

**Output (abridged):**

> **Challenge map.** CEO deposition — improper deponent/lack of unique knowledge — M — declaration: CEO has no involvement in product safety testing; safety VP does — Include. RFP 12 — overbreadth/burden — H — IT declaration: 15 years × 3,000 employees ≈ `[NEED: IT estimate]` documents; relevant product line launched 2019 — Include, but only as a date-and-custodian limit.
>
> **Argument IV.C (excerpt).** Pellam does not ask the Court to bar discovery on its safety practices. It asks that plaintiff first depose the Vice President of Product Safety and Pellam's corporate designee; if those depositions show the CEO holds unique, first-hand knowledge, plaintiff may renew the request `[CITE: forum authority on sequencing senior-executive depositions]`.
>
> **Proposed order (excerpt).** RFP 12 is limited to documents dated January 1, 2019 forward from the twelve custodians listed in Exhibit B.
