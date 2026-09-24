---
title: "Zoning Use Analysis — Permitted, Conditional or Prohibited, with Variance and Special-Permit Posture"
category: legal/real-estate
description: "Analyse whether a proposed use of a specific parcel is permitted by right, permitted with conditions or a special/conditional-use permit, allowed as a legal nonconforming use, or prohibited — working only from the ordinance text, map and overlay provisions the user supplies — then test dimensional and parking standards, identify the relief pathway (use or area variance, special permit, rezoning, text amendment) with its approval standard and procedural steps marked for verification, and state the residual risk. Attorney work product; distinct from private restrictions (title) and from non-legal site selection."
techniques:
  - ST-02
  - RT-02
  - QA-04
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - real-estate
  - zoning
  - land-use
  - variance
  - special-permit
  - nonconforming-use
  - entitlements
updated: "2026-09-24"
reasoning:
  styles: [analytic, hierarchical, evidential]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, memo]
  user_role: [attorney, land_use_counsel, developer_counsel]
  mode: [diagnose, plan]
related_prompts:
  - domain-legal/research/legal_statutory_interpretation.md
  - domain-legal/research/legal_research_plan.md
  - domain-legal/real-estate/legal_title_commitment_review.md
  - domain-legal/real-estate/legal_purchase_agreement_redline.md
---

## Objective

Deliver a zoning memo that answers one question — *can this use operate on this
parcel, and if not, what relief is needed and how hard is it to get?* — with every
conclusion anchored to quoted ordinance text supplied by the user, and every
procedural step, standard or deadline that was not supplied marked `[VERIFY]`.

## When to Use

- Pre-acquisition or pre-lease diligence where the deal depends on a specific use.
- A client wants to change or expand a use (e.g. add a drive-through, convert
  warehouse to assembly, add residential units).
- A zoning enforcement notice alleges an unpermitted use and you need the first-pass
  analysis before responding.

**Distinct from:**
- `domain-legal/real-estate/legal_title_commitment_review.md` — *private* use
  restrictions (covenants, declarations, easements); a use can be zoning-permitted and
  still barred by a recorded restriction, and the reverse. Run both.
- `domain-legal/research/legal_statutory_interpretation.md` — general interpretive
  method; use it when a single definition in the ordinance is genuinely contested.
- Non-legal site selection, market feasibility or building-code compliance — this
  prompt does not determine building, fire or accessibility code compliance.

## Your Input

- **Jurisdiction (required):** municipality/county and state. State enabling law and
  local procedure govern relief standards.
- **Parcel:** address, parcel ID, zoning district, overlay districts, and a copy or
  excerpt of the zoning map designation.
- **Ordinance text (required):** use table, definitions, district regulations,
  supplemental use standards, parking, nonconforming-use provisions, and the relief
  provisions. If a section is not supplied, the analysis of that element is `[VERIFY]`.
- **Proposed use:** described in operational terms (activities, hours, occupancy,
  customers, outdoor components, accessory elements).
- **Existing conditions:** current and historical use, prior permits or approvals,
  certificates of occupancy, any enforcement history.
- **Client objective and timeline.**

## Constraints

**Must:**
- Classify the use under the ordinance's own definitions before consulting the use
  table; quote the definition relied on and address plausible competing classifications.
- State the use-table result per district and overlay, and apply the stricter rule
  where they conflict unless the ordinance says otherwise.
- Separate **use** questions from **dimensional** questions (setbacks, height, lot
  coverage, FAR, parking, loading, buffers).
- For each relief pathway, state the approval standard only from supplied text or as
  `[VERIFY: standard under local ordinance / state enabling law]`, and list procedural
  steps (application, notice, hearing, decision-maker, appeal period) likewise.
- Rate the likelihood of each pathway qualitatively with the reasons, and state what
  would change the rating.

**Must Not:**
- Invent ordinance sections, use-table entries, hearing notice periods, appeal
  deadlines, approval standards, or case law. Use `[CITE: …]` and `[VERIFY: …]`.
- Assume a use variance is available; some jurisdictions restrict or prohibit use
  variances `[VERIFY]`.
- Treat a prior approval or long-standing use as a vested right without the
  ordinance's nonconforming-use provisions and the permit history.
- Predict a board's vote with numeric probability.

## Method

1. **Frame the question.** Parcel, district(s), overlays, proposed use in operational
   terms.
2. **Classify the use.** Match to ordinance definitions; list candidate classifications
   and choose, with reasons. If the ordinance has an unlisted-use or similar-use
   provision, apply it.
3. **Use-table result.** Permitted by right / permitted with standards / conditional
   or special use / prohibited — per district and overlay.
4. **Supplemental standards.** Use-specific standards (separation distances, hours,
   screening, drive-through stacking) — pass/fail/unknown for each.
5. **Accessory uses.** Test each accessory component separately (outdoor seating,
   storage, signage) and confirm it qualifies as accessory under the definition.
6. **Nonconforming status.** If the use is not permitted, test whether an existing
   nonconforming use can continue, expand or change under the ordinance, including
   abandonment/discontinuance rules.
7. **Dimensional and parking.** Compute required parking and compare to the site; list
   dimensional nonconformities.
8. **Relief pathways.** For each gap: available relief, standard, decision-maker,
   procedural steps, typical record needed, and likelihood with reasons.
9. **Residual risks.** Private restrictions (cross-check title), pending ordinance
   amendments, moratoria, and neighbour-appeal exposure `[VERIFY]`.
10. **Recommendation and next steps**, including a zoning-verification letter request
    where the municipality issues them `[VERIFY]`.

## Output Format

```markdown
# Zoning Use Memo — [Proposed use] at [Parcel]
**Jurisdiction:** [municipality, state] · **District / overlays:** [ ] · **Ordinance version reviewed:** [date/amendment]

## Short answer
[Permitted / Conditional / Nonconforming-continuable / Prohibited] — [one paragraph]

## Use classification
| Candidate classification | Ordinance definition (quoted) | Fit | Chosen? |

## Use-table and standards
| Requirement | Source | Proposed use | Pass / Fail / Unknown |

## Dimensional and parking
| Standard | Required | Existing/proposed | Compliant? |

## Relief pathways
| Gap | Relief | Standard | Decision-maker | Steps & deadlines | Likelihood (reasons) |

## Residual risks
## Next steps and verification list
```

## Worked Example

**Input (abridged):** Proposed brewery with a 60-seat taproom in an existing
12,000 sq ft warehouse; district "I-1 Light Industrial"; user supplied the use table,
definitions of "Manufacturing, Light", "Brewery, Craft" and "Tavern", and the parking
table. Relief provisions not supplied.

**Use classification:**

| Candidate | Definition (quoted, abridged) | Fit | Chosen? |
|---|---|---|---|
| Brewery, Craft | "production of beer not exceeding [X] barrels annually, which may include an accessory tasting room" | Strong — production primary | **Yes** |
| Tavern | "establishment primarily engaged in the on-premises sale of alcoholic beverages" | Weak unless taproom revenue dominates | No — revisit if taproom exceeds accessory limits |

**Use table:** "Brewery, Craft" in I-1 = **C** (conditional use). Accessory tasting
room must not exceed 25% of gross floor area (supplied §__) → taproom 2,400 sq ft of
12,000 = **20% — pass**.

**Parking:** supplied table requires 1 space / 1,000 sq ft manufacturing + 1 / 3 seats
for tasting rooms → 9.6 + 20 = **30 spaces** (rounded up `[VERIFY: rounding rule]`);
site has 22 → **8-space shortfall**.

**Relief pathways:**

| Gap | Relief | Standard | Likelihood |
|---|---|---|---|
| Conditional use | Conditional-use permit | `[VERIFY: CUP criteria in ordinance]` | Moderate–favourable: use is listed as conditional, site is industrial, no residential adjacency on supplied map |
| 8-space shortfall | Area (parking) variance *or* shared-parking agreement if the ordinance allows | `[VERIFY: area-variance standard; shared-parking provision]` | Shared parking is the stronger path if permitted — it avoids the hardship showing |

**Residual risk:** confirm no recorded restriction on alcohol sales (title), and any
state or local alcohol-licensing distance rules `[VERIFY]` — separate from zoning.

## Verification

- [ ] Jurisdiction, district, overlays and ordinance version are stated.
- [ ] Use classification quotes the definition and addresses competing classifications.
- [ ] Use and dimensional questions are analysed separately.
- [ ] Parking and dimensional computations show the arithmetic.
- [ ] Every approval standard, procedure and deadline is quoted from supplied text or
      marked `[VERIFY]`; no ordinance section or case is invented.
- [ ] Likelihood ratings are qualitative with reasons and a "what would change this".
- [ ] Private restrictions and non-zoning licensing are flagged as separate checks.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Going straight to the use table with a colloquial label | Classify under the ordinance's definitions first; "brewery" and "tavern" can land in different rows |
| Treating an overlay as advisory | Overlays can add prohibitions or standards; apply them and state which controls |
| Assuming a use variance is available and routine | Availability and standard vary widely; mark `[VERIFY]` and prefer conditional-use or text-amendment paths where they fit |
| Treating "it's been used that way for years" as legal nonconforming status | Test lawful establishment, continuity and abandonment under the ordinance and permit history |
| Stating hearing notice periods or appeal deadlines from memory | Mark `[VERIFY]`; missed appeal periods are unrecoverable |
| Conflating zoning with building code or alcohol licensing | Name those as separate regulatory tracks and leave them out of the zoning conclusion |
| Giving a numeric approval probability | Use qualitative likelihood with reasons and the facts that would move it |

## Related

- `domain-legal/real-estate/legal_title_commitment_review.md` — private restrictions that can bar a zoning-permitted use
- `domain-legal/real-estate/legal_purchase_agreement_redline.md` — building a zoning or entitlement condition into the PSA
- `domain-legal/research/legal_statutory_interpretation.md` — contested ordinance definitions
- `domain-legal/research/legal_research_plan.md` — planning research into local procedure and state enabling law
