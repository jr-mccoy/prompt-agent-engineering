---
title: "Care Facility Comparison — Choosing a Specific Assisted-Living, Memory-Care, or Nursing Facility After the Arrangement Type Is Settled"
category: personal-development/major-decisions
description: "Compare two to five specific care facilities once the family has already decided the arrangement type (assisted living, memory care, skilled nursing): set must-haves from the parent's care level and wishes before any tour, gather evidence from official inspection records, unannounced visits and residents' families rather than the marketing tour, price the full cost trajectory including level-of-care increases, read the admission contract's exit and discharge terms with a professional, and end with a ranked choice plus a watch-list for the first 90 days; distinct from `personal_caring_for_aging_parent.md`, which decides the arrangement type, and `personal_major_purchase_research.md`, which compares goods rather than care."
techniques:
  - DT-05
  - RT-05
  - DS-06
  - CM-02
  - QA-12
difficulty: intermediate
tags:
  - caregiving
  - aging-parents
  - assisted-living
  - care-facilities
  - family
  - decision-quality
updated: "2026-09-24"
reasoning:
  styles: [evidential, comparative, multi-criteria, empathic]
  stakes: high
  horizon: months_to_years
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: [matrix, structured]
  user_role: [individual, family]
  mode: [decide, audit, assess]
related_prompts:
  - domain-personal-development/major-decisions/personal_caring_for_aging_parent.md
  - domain-personal-development/major-decisions/personal_major_purchase_research.md
  - domain-decision-making/tradeoff_multi_criteria_decision_analysis.md
---

# Care Facility Comparison

**Objective:** Choose among specific facilities of an already-chosen type on evidence the
parent would care about — safety record, staffing, how residents are actually treated, the
real cost over time, and whether the contract lets them stay as needs grow — rather than on
the tour, the lobby and the sales director's warmth.

**When to Use:**
- `personal_caring_for_aging_parent.md` (or your family's own discussion) has settled on
  assisted living, memory care or skilled nursing, and there are several candidate places.
- A hospital discharge planner has handed you a list and a short deadline.
- You are unhappy with a current facility and comparing alternatives.

**Not this prompt if:**
- You have not yet decided *what kind* of care — `personal_caring_for_aging_parent.md` first;
  comparing facilities before that decision anchors the family on whichever place toured best.
- You are choosing in-home care agencies or caregivers — the evidence sources and contract
  terms differ; adapt with care or start from `personal_major_purchase_research.md`'s structure.
- You need the legal or benefits mechanics (payment eligibility, contract enforceability,
  guardianship) — route to an elder-law attorney and a benefits specialist.
- There is a safety emergency or suspected abuse at a current facility — contact the facility's
  regulator or adult protective services and, if urgent, emergency services.

**Audience:** An adult child, spouse or sibling group choosing on behalf of, and ideally with,
the parent. The parent's own view is gathered wherever they can give it.

## Inputs / Context

1. **Arrangement type decided** and the care level (from the aging-parent prompt's L1–L5
   ladder) now and likely next.
2. **The parent's wishes and non-negotiables:** proximity to whom, faith or culture, food,
   privacy, pets, routines, language.
3. **Candidate facilities** (2–5) and how each was found.
4. **Budget and payment sources**, rough — flag every figure for professional verification.
5. **Family visiting pattern:** who visits, how often, from where.
6. **Deadline:** discharge date, waitlist offers, current-facility notice period.

## Method

1. **Write must-haves and deal-breakers before any tour (CM-02).** From care level and
   wishes: e.g. "memory care with a secured outdoor area", "can keep the cat", "within 30
   minutes of the sister who visits weekly". A facility failing a must-have is out, however
   good the tour.

2. **Build the comparison matrix (DT-05).** Assess every facility on the same criteria:

   | Criterion | What good evidence looks like |
   |---|---|
   | Inspection and complaint record | Official regulator reports — read the findings, not just the rating |
   | Staffing | Staff-to-resident ratio on nights and weekends; turnover; agency staff share (ask; verify where public) |
   | Care fit, now and next | Can they meet the next care level, or will your parent be discharged when needs rise? |
   | Daily life | Observed activities, meals, how staff speak to residents |
   | Location and visiting | Travel time for the most frequent visitor; visiting rules |
   | Full cost trajectory | Base fee plus level-of-care tiers, medication management, annual increases — "[verify in writing]" |
   | Contract terms | Deposit, notice, discharge grounds, what happens if funds run out |

3. **Gather evidence beyond the tour (RT-05).** For each facility: one scheduled tour, one
   unannounced visit at a different time (evening or weekend), a conversation with at least one
   resident's family member not supplied by the facility, and the official inspection history.
   Tag every cell with its source: *official record*, *observed*, *family report*, *facility claim*.

4. **Price the trajectory, not the entry fee.** Ask for the written fee schedule including
   care-level increments and the last three years' annual increases. Estimate cost at current
   level and next level. Every number is marked "[verify with facility in writing / benefits
   specialist]"; never fill a gap from memory or averages.

5. **Send the contract to a professional before signing.** List the clauses to ask an elder-law
   attorney about: discharge and transfer grounds, arbitration, deposit refunds, responsible-party
   signatures (whether an adult child becomes personally liable), what happens if payment source
   changes. This prompt flags; it does not interpret.

6. **Rank and decide (DS-06).** Must-haves first, then weight the rest with the parent's
   priorities (use `domain-decision-making/tradeoff_multi_criteria_decision_analysis.md` if the
   family disagrees on weights). Name the top choice, the fallback, and what would flip them.

7. **Write the 90-day watch-list.** What to observe after move-in (weight, hygiene, medication
   errors, mood, response to call bells, staff names known) and who checks, so a poor fit is
   caught early.

## Output Format

```
# Care facility comparison — [relationship; no identifying details]
Arrangement type: [...] · Care level now/next: [L_ / L_] · Decide by: [date]

## Must-haves and deal-breakers (set before tours)
## Screened out: [facility — failed must-have]

## Comparison matrix
| Criterion | Facility A | Facility B | Facility C |
(each cell: finding + source tag)

## Cost trajectory (all figures [verify in writing])
| Facility | Now | At next care level | Annual increase history | Deposit / refund |

## Contract questions for elder-law attorney
## Parent's view: [what they said, in their words where possible]
## Ranking: 1. ... 2. ... — what would flip it: ...
## 90-day watch-list: | Sign | Who checks | How often | Trigger for concern |
## Confidence: High / Medium / Low — [which cells rest on facility claims only]
```

## Verification

- [ ] Must-haves written before any tour and applied as a screen.
- [ ] Every facility assessed on the same criteria.
- [ ] Every cell carries a source tag; no cell rests only on the marketing tour where an official record exists.
- [ ] Each shortlisted facility had an unannounced visit and an independent family conversation.
- [ ] Cost shown at the next care level, not only today's; all figures marked for verification.
- [ ] The contract has gone, or is scheduled to go, to an elder-law attorney with a written question list.
- [ ] The parent's view is recorded.
- [ ] A 90-day watch-list names who checks.

## False-Positive Prevention

1. **The tour effect.** The facility with the best lobby and warmest sales director is not
   thereby the best care. Weight observed and official evidence above the tour.
2. **Entry-price anchoring.** A low base fee with steep care-level tiers can cost more within a
   year than a higher all-inclusive fee. Compare at the next care level.
3. **"They can handle anything."** Ask directly what needs would trigger discharge or transfer,
   and get it in the contract.
4. **Hand-picked references.** Families the facility introduces you to are a sample of the happiest.
   Find one independently.
5. **Rating without reading.** A headline rating hides whether the findings were paperwork or harm.
   Read the findings.
6. **Signing as "responsible party" unexamined.** That signature may create personal liability;
   ask the attorney before signing.
7. **Deciding for, not with.** Where the parent can express a preference, a technically better
   facility they refuse is not better. Record their view and weigh it.
8. **Deadline panic.** A discharge deadline is real but often negotiable; ask the discharge planner
   what extending looks like before accepting the first opening.

## Example Output

```
# Care facility comparison — father, 84; memory care
Care level now/next: L4 / L5 within ~1–2 yrs (per geriatrician) · Decide by: hospital discharge 10-14

## Must-haves: secured garden; within 30 min of daughter (visits 3×/wk); can meet L5 or has sister unit
## Screened out: Linden House — no L5 pathway; discharge to nursing home on decline

## Comparison matrix
| Inspection record | Oakview: 2 findings, both paperwork (official) | Brookside: 1 finding re medication errors, 2025 (official) |
| Night staffing | Oakview: 1:8 claimed (facility claim); calm at 20:30 visit (observed) | Brookside: 1:12 (facility claim); two call bells unanswered 6+ min (observed) |
| Care next level | Oakview: sister nursing unit on site (contract clause 9) | Brookside: "case by case" (facility claim) |
| Family view | Oakview: resident's son — "they know Dad's name and his jokes" (family report) | Brookside: not yet obtained |
| Travel for daughter | Oakview 22 min · Brookside 12 min |

## Cost trajectory [verify in writing]
| Oakview | [base] | [base + tier 3] | +4%, +5%, +6% | deposit refundable within 30 days |
| Brookside | [lower base] | [steeper tier] | not provided | non-refundable |

## Attorney questions: clause 14 arbitration; "responsible party" signature; Brookside deposit terms
## Parent's view: "Somewhere I can sit outside." Liked Oakview garden on tour.
## Ranking: 1. Oakview 2. Brookside — flips if Oakview's contract discharge terms are worse than clause 9 suggests
## 90-day watch-list: weight monthly (daughter asks nurse); bruising/hygiene each visit; medication chart weekly
## Confidence: Medium — Brookside family report missing; all costs pending written schedules
```

## Techniques Used

- **DT-05 Element-by-Element Assessment Matrix** — every facility on the same criteria.
- **RT-05 Evidence-Based Reasoning** — every cell tagged by source; tour claims ranked below records.
- **DS-06 Prioritization and Severity Guidance** — must-haves screen, then weighted ranking.
- **CM-02 Constraint Specification** — must-haves and deal-breakers fixed before touring.
- **QA-12 False Positives Identification** — the tour effect, entry-price anchoring and hand-picked references.

## Related Prompts

- `personal_caring_for_aging_parent.md` — decides the arrangement type this prompt shops for.
- `personal_major_purchase_research.md` — the walk-away discipline, applied here to care.
- `../../domain-decision-making/tradeoff_multi_criteria_decision_analysis.md` — formal weighting when siblings disagree.
- `../../domain-productivity/home-life/home_family_caregiving_coordination.md` — running visits, costs and updates after move-in.
