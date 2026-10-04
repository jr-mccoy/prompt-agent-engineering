---
title: "Negotiation Analytics Scorecard — Outcomes vs. Targets, Concessions, Value Created, and Process Across a Portfolio of Deals"
category: negotiation/craft
description: "Score a set of concluded negotiations — your own, or a team's — on named metrics computed the same way every time: bargaining-range capture against reservation point and target, concession depth and reciprocity, value created beyond the single-issue split, walk-away quality, and a process-quality score that is kept separate from the result. Segments by counterpart type only when the sample supports it, tags every estimate by confidence, and names how each metric can be gamed. Counters the most common portfolio-review failure: judging negotiators by headline savings or win rate, which rewards soft targets and punishes the good no-deal."
techniques:
  - QA-17
  - NE-11
  - DS-02
  - QA-21
  - RT-02
difficulty: advanced
tags:
  - negotiation
  - negotiation-analytics
  - scorecard
  - concession-tracking
  - value-creation
  - portfolio-review
  - how-did-we-do-in-our-negotiations
  - are-we-leaving-money-on-the-table
  - review-our-deals
updated: "2026-10-03"
reasoning:
  styles: [analytic, evaluative, reflective, counterfactual]
  stakes: low
  horizon: months
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: [matrix, structured]
  user_role: [executive, founder, sales, individual]
  mode: [audit, synthesize]
related_prompts:
  - domain-negotiation/after-the-deal/negotiation_post_negotiation_debrief.md
  - domain-negotiation/craft/negotiation_pattern_library_builder.md
  - domain-sales-customer/sales/sales_deal_qualification_scorecard.md
---

# Negotiation Analytics Scorecard — Outcomes vs. Targets, Concessions, Value Created, and Process

**Objective:** One debrief tells you about one negotiation. A scorecard tells you whether you — or a team of buyers, account executives, or recruiters — are getting better, where the money is actually leaking, and whether the numbers you report reflect skill or soft targets. This prompt takes eight or more concluded negotiations, computes a fixed set of named metrics for each one, rolls them up, and separates **outcome quality** (what you got) from **process quality** (how well you prepared and conducted it), because a strong result from a weak process is luck that will not repeat.

It is the quantitative complement to `craft/negotiation_pattern_library_builder.md`, which extracts situation → move → outcome patterns in words. The scorecard supplies the numbers that tell the library where to look.

**When to use:**
- Quarterly or annual review of your own negotiations, or a team's.
- A procurement, sales, or recruiting function reports "savings" or "win rate" and you suspect those numbers flatter or punish the wrong people.
- You want to know whether you concede too early, too much, or without getting anything back.
- Before setting next year's targets, to see how ambitious last year's actually were.

**When NOT to use:**
- You are reviewing **one** concluded negotiation — use `after-the-deal/negotiation_post_negotiation_debrief.md`, which goes deeper on a single deal than any scorecard can.
- You have fewer than eight concluded negotiations with at least a target and a reservation point written down — accumulate records first; the metrics are noise below that.
- You want to qualify or forecast **open** sales deals — that is `domain-sales-customer/sales/sales_deal_qualification_scorecard.md`.
- You want qualitative patterns of what works in which situation — `craft/negotiation_pattern_library_builder.md`.

**Audience:** Individuals who negotiate often, and leads of procurement, sales, recruiting, or partnerships teams reviewing a portfolio of deals.

---

## Inputs / Context

1. **Deal records, one row per negotiation** (8 minimum, 20+ for segmenting): date, counterpart type, issue(s) negotiated, your opening, target, reservation point (walk-away), final outcome or "no deal", and the main non-price terms gained or given.
2. **When target and reservation point were set** — before first contact, during, or reconstructed afterward.
3. **Concession log** where available: each move by each side, in order.
4. **Your valuation of non-price terms** (payment terms, scope, warranty, start date, exclusivity) in the deal's currency, with how the figure was arrived at.
5. **Process notes**: was BATNA written down, interests mapped, a concession plan made?
6. **Reporting use**: is the scorecard for self-improvement, coaching, or performance evaluation? This changes which gaming risks matter.

---

## Constraints

### Must
- Compute every metric with the stated formula, the same way for every deal, and show the inputs.
- Tag every reservation point, target, counterpart estimate, and non-price valuation **known / inferred / guessed**. Reconstructed targets are **guessed**.
- Keep outcome quality and process quality as separate scores; never blend them into one number.
- Report **n** beside every aggregate and segment; suppress segment comparisons with n < 5.
- Steelman the negotiator whose numbers look worst: name the deal context (market shift, weak BATNA, inherited terms) that would make the result reasonable before calling it a skill gap.
- Name at least one way each headline metric can be gamed in this reporting use.

### Must Not
- Use savings off the supplier's opening quote or the customer's list price as a performance measure — the counterpart controls that anchor.
- Count a no-deal as failure without checking whether the best available offer was below the reservation point.
- Average percentages across deals of very different size without also reporting the value-weighted figure.
- Treat a target set after the outcome was known as a real target.

---

## Instructions

### Step 1 — Clean the records
Flag each row: target and reservation point set **before** first contact (usable), **during** (usable with caution), or **after** (exclude from range metrics, keep for process). Normalise direction so that "more is better" for every metric whether you were buying or selling.

### Step 2 — Bargaining-range capture
For each closed deal:
`Range capture = (outcome − reservation point) ÷ (target − reservation point)`.
0% = you landed on your walk-away; 100% = you hit target; above 100% suggests the target was soft. Report the distribution, not only the mean.

### Step 3 — Concession depth and reciprocity
`Concession depth = (your opening − outcome) ÷ (your opening − reservation point)` — the share of your room you gave away. From the concession log: `Reciprocity = number of your concessions ÷ number of theirs`, and note concessions given with nothing traded back. Depth above about 80% together with reciprocity above 1.5 is the signature of conceding to close.

### Step 4 — Value created
For multi-issue deals, value the non-price terms gained and given using input 4:
`Net value created = Σ value of terms gained − Σ value of terms given` beyond the price line. Count deals that stayed single-issue when other terms were available. Tag each valuation's confidence; a portfolio whose "value created" rests on guessed valuations is reported as such.

### Step 5 — Walk-away quality
Sort every no-deal into **good no-deal** (best offer was below reservation point — walking was correct) or **missed deal** (an offer at or above reservation point was declined or lost). Report `Walk-away rate = no-deals ÷ total negotiations` alongside the split; a zero walk-away rate across many deals usually means reservation points are not being held.

### Step 6 — Process-quality score
Score each deal 0–5, one point each: target set before contact; reservation point and BATNA written down; counterpart interests mapped; concession plan made; debrief done. Place each deal in the 2×2 of process (≥4 / ≤3) × outcome (range capture ≥50% / <50%).

### Step 7 — Roll up and segment
Portfolio medians and value-weighted figures for each metric. Segment by counterpart type, deal size band, or negotiator only where n ≥ 5 per segment. Name the single metric furthest from where it should be, and the segment it concentrates in.

### Step 8 — Gaming check
For the reporting use in input 6, list the gaming vectors: soft targets (range capture above 100% repeatedly), reservation points moved after the fact, splitting one negotiation into several, avoiding hard counterparts, valuing non-price terms generously. State which ones the data already shows signs of.

### Step 9 — Adversarial check
- Which conclusion depends most on guessed values, and how would it change if they were wrong by 30%?
- Is the "worst performer" simply the one assigned the weakest-BATNA deals?
- What would a sceptical finance reviewer say the scorecard overstates?

---

## False-Positive Prevention

1. **Savings off list price.** A 20% discount off a padded quote may be a worse result than 5% off a fair one. Range capture against your own reservation point is the measure you control.
2. **Soft targets as excellence.** Range capture regularly above 100% is evidence of unambitious targets, not brilliance.
3. **No-deals as losses.** Walking away from an offer below your reservation point is the scorecard working, not failing.
4. **Small-n segments.** Three deals with one counterpart type cannot show a pattern; report "insufficient n".
5. **Outcome blended with process.** A great number from no preparation is a warning, not a model to copy.
6. **Confident non-price valuations.** "Net-60 terms are worth $40k" is often a guess; tag it and test the conclusion without it.
7. **Hindsight targets.** A target reconstructed after the outcome is always nearly met.
8. **Ignoring deal size.** An unweighted average lets ten small wins hide one large loss.

---

## Output Format

```
# Negotiation scorecard — [scope], [period]   n = [..] ([..] closed, [..] no-deal)

## Data quality
| Deal | Target/RP set | Usable for range metrics | Confidence notes |

## Per-deal metrics
| Deal | Range capture | Concession depth | Reciprocity | Net value created | Process (0–5) | Quadrant |

## Portfolio roll-up
| Metric | Median | Value-weighted | n | Read |
Walk-away rate: [..] — good no-deals [..] / missed deals [..]

## Process × outcome
| | Outcome ≥50% | Outcome <50% |
| Process ≥4 | [deals] | [deals] |
| Process ≤3 | [deals] | [deals] |

## Segments (n ≥ 5 only)
| Segment | n | Range capture | Concession depth | Read |

## The one metric to fix
[Metric] — [where it concentrates] — [what it is costing, with confidence tag]

## Gaming check
| Vector | Signs in this data? |

## Adversarial check
- Most guess-dependent conclusion: [..] — if off by 30%: [..]
- Assignment effect: [..]
- What a sceptical reviewer would say is overstated: [..]
```

---

## Verification

- [ ] Every metric uses the stated formula and shows its inputs.
- [ ] Targets and reservation points are tagged by when they were set; after-the-fact ones are excluded from range metrics.
- [ ] Every estimate carries known / inferred / guessed.
- [ ] Outcome and process scores are reported separately and placed in the 2×2.
- [ ] No-deals are split into good no-deals and missed deals.
- [ ] Every aggregate shows n; no segment with n < 5 is compared.
- [ ] Median and value-weighted figures both reported.
- [ ] Gaming vectors named for this reporting use.
- [ ] No savings-off-list-price metric anywhere in the scorecard.
- [ ] No blended single "negotiation score".
