---
title: "Easement Drafter — Scope, Term, Maintenance, Indemnity and Recordable Form"
category: legal/real-estate
description: "Draft an express easement agreement (access, utility, drainage, parking, construction/temporary, or reciprocal) from a declared grantor or grantee posture: parties and burdened/benefitted parcels, appurtenant vs. in gross, precise easement area tied to an exhibit, permitted and excluded uses, exclusivity, term and termination, relocation, maintenance and cost sharing, insurance and indemnity, lender subordination, and a recordable form checklist with every local formality marked for verification. Attorney work product; distinct from a title review that identifies the need for an easement."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - real-estate
  - easement
  - drafting
  - access
  - utility
  - recording
  - covenants-running-with-land
updated: "2026-09-24"
reasoning:
  styles: [constructive, systematic, adversarial]
  stakes: high
  horizon: days
  uncertainty: risk
  evidence_quality: rich
  domain_complexity: regulated
  collaboration: small_team
  output_format: [document, checklist]
  user_role: [attorney, paralegal]
  mode: [draft, audit]
related_prompts:
  - domain-legal/real-estate/legal_title_commitment_review.md
  - domain-legal/real-estate/legal_purchase_agreement_redline.md
  - domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md
---

## Objective

Produce a complete, recordable-ready draft easement agreement tailored to the stated
purpose and posture, with a drafter's notes table explaining each posture-sensitive
choice, and a recording checklist whose local formalities are marked `[VERIFY]` for
confirmation with the county recorder and title company.

## When to Use

- Curing a title objection (access to a landlocked parcel, relocating a utility strip).
- A development needs utility, drainage, parking or construction access across a
  neighbour's land.
- Converting an informal or prescriptive arrangement into a written, recorded easement.
- Drafting a reciprocal easement between adjoining owners in a small project (for a
  full multi-parcel REA with operating covenants, use this as a starting skeleton only).

**Distinct from:**
- `domain-legal/real-estate/legal_title_commitment_review.md` — identifies easement
  problems in a commitment; this prompt drafts the instrument that fixes them.
- `domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md` —
  redlines contractual indemnity/limitation clauses; use it to stress-test §8 below if
  the counter-party pushes back.

## Your Input

- **Jurisdiction (required):** state and county where both parcels lie.
- **Posture (required):** Grantor (burdened owner) / Grantee (benefitted owner or
  utility) / Mutual.
- **Purpose:** access (pedestrian/vehicular/truck), utility (type), drainage, parking,
  construction/temporary, signage, or reciprocal.
- **Parcels:** legal descriptions or tax IDs of burdened and benefitted parcels, and a
  surveyor's description or plat of the easement area (or a placeholder).
- **Consideration** and any payment terms.
- **Existing encumbrances:** mortgages on the burdened parcel (lender consent or
  subordination), existing easements in the same area.
- **Business terms:** exclusivity, term, relocation, maintenance split, insurance levels.

## Constraints

**Must:**
- State whether the easement is appurtenant (runs with the benefitted parcel) or in
  gross, and draft running-with-the-land and successors-and-assigns language to match.
- Define the easement area only by reference to an exhibit legal description and
  drawing; never by informal description alone.
- Specify permitted uses and excluded uses (e.g. no parking in an access easement, no
  above-ground facilities in a utility strip).
- Address exclusivity, term and termination (including abandonment and merger), and
  relocation at the burdened owner's cost and election, with standards.
- Allocate construction, maintenance, repair and replacement, and restoration after
  work; include a cost-sharing formula where shared.
- Include insurance, indemnity, lender consent/subordination where a mortgage exists,
  and a dispute mechanism.
- Produce a recording checklist with every formality marked `[VERIFY]`.

**Must Not:**
- Invent statutes, recording requirements (margins, font, preparer statements,
  cover sheets, transfer-tax forms), or case law. Use `[VERIFY: …]` / `[CITE: …]`.
- Leave width, location or permitted vehicle class undefined for an access easement.
- Draft an indemnity broader than the posture supports (a grantor should not
  indemnify the grantee's use).
- Assume the grantor can grant free of an existing mortgage.

## Method

1. **Purpose statement.** One sentence; everything else must serve it.
2. **Posture choices.** List each term where grantor and grantee interests diverge
   (exclusivity, relocation, maintenance, term, indemnity) and choose for the posture.
3. **Draft the instrument** in the section order in the Output Format.
4. **Exhibit placeholders.** Exhibit A (burdened parcel), B (benefitted parcel),
   C (easement area description and drawing), with instructions for the surveyor.
5. **Lender joinder.** If the burdened parcel is mortgaged, add a consent and
   subordination joinder.
6. **Drafter's notes table.** Each choice, the alternative, and why.
7. **Recording checklist.**

## Output Format

```markdown
# [Access / Utility / …] Easement Agreement — Draft [n] ([Grantor/Grantee] draft)

[Recording block: prepared by / return to / parcel IDs — VERIFY local format]

1. Parties and Recitals
2. Grant of Easement (appurtenant / in gross; exclusive / non-exclusive)
3. Easement Area (Exhibit C)
4. Permitted Use; Excluded Uses
5. Construction; Standards of Work; Restoration
6. Maintenance, Repair, Replacement; Cost Sharing
7. Relocation
8. Insurance; Indemnity
9. Term; Termination; Abandonment
10. Mortgagee Consent and Subordination (if applicable)
11. Covenants Running with the Land; Successors and Assigns
12. Default; Notice and Cure; Self-Help; Dispute Resolution
13. Miscellaneous (governing law, amendments, estoppel certificates, counterparts)
Signature and acknowledgment blocks [VERIFY: acknowledgment form]
Exhibits A–C

## Drafter's notes
| § | Choice | Alternative | Why (posture) |

## Recording checklist
- [ ] [VERIFY: page/margin/format requirements — county recorder]
- [ ] [VERIFY: acknowledgment form and witness requirements — state]
- [ ] [VERIFY: transfer-tax or exemption filing, if any]
- [ ] Surveyor-sealed Exhibit C
- [ ] Mortgagee joinder executed
- [ ] Title company to insure easement as an appurtenant estate (grantee) [VERIFY]
```

## Worked Example

**Input (abridged):** Grantee posture; landlocked 2-acre parcel (benefitted) needs
vehicular access 24 ft wide over a neighbour's parcel (burdened) to a public road;
burdened parcel is mortgaged; one-time payment.

**Selected drafting:**

> **2. Grant.** Grantor grants to Grantee, for the benefit of the Benefitted Parcel, a
> perpetual, non-exclusive easement appurtenant for vehicular and pedestrian ingress
> and egress, including passenger vehicles, delivery trucks and emergency vehicles,
> over the Easement Area described in Exhibit C.

> **7. Relocation.** Grantor may relocate the Easement Area at Grantor's sole cost
> only if the relocated area (a) provides substantially equivalent access and width,
> (b) connects to the same public road, (c) is constructed to at least the existing
> standard before the original area is closed, and (d) is described in a recorded
> amendment in form reasonably acceptable to Grantee and its lender.

| § | Choice | Alternative | Why (grantee) |
|---|---|---|---|
| 2 | Perpetual, appurtenant | Term of years / in gross | Access to a landlocked parcel must pass with the land and survive sales and financings |
| 2 | Non-exclusive | Exclusive | Grantor will reject exclusivity over its own driveway; non-exclusive plus §4 no-obstruction covenant achieves the need |
| 7 | Relocation permitted with four conditions | No relocation | Absolute bar is likely a deal-breaker; conditions protect continuity |
| 10 | Mortgagee subordination joinder | None | Without it, a foreclosure could cut off the easement `[VERIFY: priority rules in state]` |

## Verification

- [ ] Purpose, posture and appurtenant/in-gross status are explicit.
- [ ] Easement area defined only by exhibit; width and vehicle class specified for access.
- [ ] Permitted and excluded uses both stated.
- [ ] Maintenance, cost sharing, relocation, term and termination addressed.
- [ ] Indemnity direction matches posture.
- [ ] Mortgagee consent/subordination included where the burdened parcel is encumbered.
- [ ] Every recording formality, acknowledgment form and statutory rule is `[VERIFY]`;
      no statute or case is invented.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Describing the area in words ("the existing driveway") | Tie to a surveyed exhibit; driveways move and words do not survive a dispute |
| Omitting appurtenant language, leaving the easement arguably personal | State appurtenance and running-with-the-land expressly |
| Ignoring the burdened parcel's mortgage | Obtain consent/subordination; flag priority rules as `[VERIFY]` |
| Silent maintenance, so nobody must repair | Allocate construction, maintenance, repair and replacement with a formula |
| Access easement with no vehicle class or width | Define both; a pedestrian path and a truck route are different easements |
| Stating recording formalities from memory | County and state requirements differ; mark every one `[VERIFY]` |
| Reciprocal indemnities in a one-way easement | The user of the easement indemnifies the owner of the burdened land, not the reverse |

## Related

- `domain-legal/real-estate/legal_title_commitment_review.md` — where the easement need usually surfaces
- `domain-legal/real-estate/legal_purchase_agreement_redline.md` — making a recorded easement a closing condition
- `domain-legal/real-estate/legal_zoning_use_analysis.md` — access and parking easements that satisfy zoning standards
- `domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md` — stress-testing indemnity and insurance language
