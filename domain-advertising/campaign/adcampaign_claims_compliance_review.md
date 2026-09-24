---
title: "Ad Claims Compliance Review — Substantiation, Disclosures, and Restricted Categories Before Launch"
category: advertising/campaign
description: "Pre-launch review of ad copy, scripts, and visuals: extract every express and implied claim, match each to the substantiation file, flag disclosure needs (material connections, pricing and offer terms, typicality of results), flag restricted or sensitive categories (supplements and health, financial products, and similar) and platform-policy questions, and produce a severity-ranked findings table with a counsel queue. Regulatory rules are never asserted — they are raised as questions for counsel or the platform's current policy. Distinct from the legal domain (counsel's opinion), quality_slop_ad_copy (persuasiveness scoring), and the image prompts' visual rules."
techniques:
  - RT-05
  - DS-06
  - OC-09
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - advertising
  - claims-review
  - substantiation
  - compliance
  - campaign
  - disclosures
updated: "2026-09-24"
related_prompts:
  - domain-advertising/campaign/adcampaign_copy_variant_matrix.md
  - domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md
  - domain-professional-writing/content-quality/quality_slop_ad_copy.md
---

# Ad Claims Compliance Review

**Objective:** Before anything launches, find every claim an ad makes — including the
ones it makes by implication — and show whether the advertiser can back it, what it
needs to disclose, and what must go to counsel, so that legal review is spent on the
real questions instead of on reading every variant.

**When to Use:**
- A copy matrix, UGC script, or asset set is ready and has claim flags on it.
- The product is in a category platforms or regulators treat as sensitive — health,
  supplements, financial products, weight, age-restricted goods.
- Creators, testimonials, or "results" appear in the creative.
- A previous ad was rejected or drew a complaint and nobody knew which line did it.

**When NOT to use:**
- You need a legal opinion on whether a claim is lawful — that is counsel's job;
  this prompt prepares the queue for them. `domain-legal/`.
- You want copy scored for persuasiveness —
  `domain-professional-writing/content-quality/quality_slop_ad_copy.md`.
- You need a whole compliance programme assessed —
  `domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md`.

## Inputs / Context

1. **Every asset to review**: copy cells, scripts, on-screen text, visuals, landing
   page headline.
2. **The substantiation file**: each study, test log, dataset, review export, or
   price record, with date and scope.
3. **Product category and markets** (jurisdictions) the ads will run in.
4. **Creator and testimonial relationships**: who was paid, gifted, or employed.
5. **Offer terms**: price, discount basis, trial conditions, cancellation.
6. **Who counsel is**, and what they need to receive.

## Method

1. **Extract claims.** For each asset, list express claims verbatim and implied
   claims in plain words ("Dinner in 20 minutes" implies typical prep time for a
   typical user). Visuals count: a before/after image claims a result.
2. **Classify each claim.** Objective (testable: numbers, speed, comparison,
   "clinically"), subjective (opinion, puffery), testimonial, pricing/offer, or
   category-sensitive (health, body, money, safety, environment).
3. **Match to substantiation.** For each objective claim: which item in the file
   supports it, does its scope match (same product version, population, conditions,
   date), and does the wording go beyond it. Record "none" plainly.
4. **Flag disclosure needs as questions.** Material connection for creators and
   testimonials; typicality where a result is shown; offer terms for "free",
   "half price", "trial"; any qualifying condition a reasonable viewer would need.
   Phrase each as "counsel to confirm required disclosure and placement."
5. **Flag restricted-category and platform-policy questions.** For each sensitive
   claim, the question to check against the platform's current policy and to put
   to counsel for each market. Do not state the rule.
6. **Rank findings.** High: objective or category-sensitive claim with no or
   mismatched substantiation, or a missing material-connection disclosure. Medium:
   scope stretch, qualifier missing, offer terms unclear. Low: wording that invites
   misreading. Each with a recommended fix that stays within the evidence.
7. **Build the counsel queue.** Only the questions that need a legal answer, each
   with the asset, the claim, the evidence, and the markets — so counsel reviews
   issues, not ads.
8. **State what the review cannot do.** It does not clear anything; it prepares.

## Output Format

```
# Claims review — [campaign]   Markets: [...]   Reviewer: [...]   Date: [...]

## Claims register
| ID | Asset | Claim (verbatim / implied) | Type | Substantiation | Scope match | Finding |
|---|---|---|---|---|---|---|

## Disclosure questions (for counsel)
| ID | Asset | Situation | Question |
|---|---|---|---|

## Category & platform-policy questions
| ID | Claim | Question for current platform policy | Question for counsel (per market) |
|---|---|---|---|

## Findings (ranked)
| Sev | ID | Issue | Fix within the evidence |
|---|---|---|---|

## Counsel queue
[numbered, self-contained questions]

## This review does not
Clear any claim as lawful; state regulatory requirements; replace counsel or platform review.
```

## Verification

- [ ] Every asset has at least its express claims extracted, and visuals were reviewed.
- [ ] Implied claims are written out in plain words.
- [ ] Every objective claim shows a substantiation item or "none".
- [ ] Scope match is checked, not assumed.
- [ ] No regulatory rule, agency, or penalty is stated as fact.
- [ ] Every creator or testimonial with a relationship has a disclosure question.
- [ ] The counsel queue is self-contained.

## False-Positive Prevention

1. **Do not assert the law.** "This violates [regulation]" or "supplements may not
   claim…" are removed; each becomes a counsel question.
2. **Do not name enforcement bodies as authority.** Which regulator applies varies by
   market and product; it is counsel's call.
3. **Puffery is not a free pass.** Whether a line is opinion or an objective claim
   is often the question itself — flag borderline lines rather than waving them through.
4. **A study is not substantiation for every wording.** Check population, dose or
   version, conditions, and date against the claim as worded.
5. **Visuals claim things.** A transformed body, a rising graph, or a lab coat are
   claims and go in the register.
6. **Do not soften a claim into vagueness to pass.** The fix is a claim the evidence
   supports, or removal — not an evasive rewording that implies the same thing.
7. **Do not clear.** The output never says "compliant" or "approved."

## Example

**Input:** Meal-kit copy matrix C1–C4 and the standing-desk UGC script. Substantiation:
review-platform export (12,400 reviews, avg 4.6, 2026-09-01); ops note "prep times
15–35 min"; desk test log (raise < 5 s, lab, 2026-08-12). Creator: paid, product gifted.
Markets: [two markets].

```
## Claims register
| M1 | C1 | "Dinner in 20 minutes" / typical prep ≈ 20 min | Objective | Ops note 15–35 min | Partial — 20 is not typical | High |
| M2 | C2 | "12,400 families rate us 4.6★" | Objective | Export: 12,400 reviews | No — reviews ≠ families | High |
| D1 | UGC b3 | "Goes up in about five seconds" | Objective | Test log < 5 s (lab) | Yes, lab conditions | Low |
| D2 | UGC | Creator is paid + gifted | Testimonial | — | — | High (disclosure) |

## Disclosure questions
| D2 | UGC | Paid, gifted creator | Required disclosure form and placement per market? |
| M3 | All | "half price" first box | Required offer-terms disclosure and landing-page match? |

## Findings
| High | M2 | Count substituted | "4.6★ from 12,400 reviews" |
| High | M1 | Time overstated | "Recipes from 15 minutes" or range |
| High | D2 | Disclosure undecided | Counsel queue Q1 |

## Counsel queue
1. D2: creator paid and gifted; spoken + on-screen disclosure proposed — adequate in [markets]?
2. M3: "half price first box" — what offer terms must appear in-ad vs landing page?
```

M2 closes the loop the copy matrix opened: the review-count substitution flagged
there is a High here, with a fix that stays inside the evidence.

## Techniques Used

- **RT-05 Evidence-Based Reasoning** — each claim matched to a dated item in the file.
- **DS-06 Prioritization and Severity Guidance** — High/Medium/Low findings.
- **OC-09 Capability Boundary Specification** — the "this review does not" block.
- **QA-05 Citation Requirements** — no claim stands without its source.
- **QA-01 Self-Verification** — the checklist before handing to counsel.

## Related Prompts

- `adcampaign_copy_variant_matrix.md` and `adcampaign_ugc_video_script_beats.md` — the claim flags this review clears.
- `domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md` — programme-level compliance.
- `domain-professional-writing/content-quality/quality_slop_ad_copy.md` — persuasiveness, not compliance.
