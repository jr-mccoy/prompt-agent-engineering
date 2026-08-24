---
title: "Recommender Feedback-Loop & Bias Audit"
category: AI-ML/specialized-ml/recommender-systems
description: "Audit a recommender for popularity bias, position bias, and self-reinforcing feedback loops — where the system trains on data it generated, entrenching the head and starving discovery — with evidence-backed findings and mitigations."
techniques:
  - ST-02
  - RT-05
  - QA-12
  - DS-06
  - CM-02
difficulty: advanced
tags:
  - recommender-systems
  - feedback-loop
  - popularity-bias
  - position-bias
  - fairness
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_offline_evaluation.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_cold_start_strategy.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_objective_business_alignment.md
---

# Recommender Feedback-Loop & Bias Audit

**Objective:** Audit a deployed recommender for the three coupled distortions that arise when a system trains on the data its own recommendations generate — popularity bias, position bias, and self-reinforcing feedback loops — producing evidence-backed findings (not generic warnings), ranked by severity, with concrete mitigations and the metrics to monitor them.

**When to Use:**
- Recommendations feel "stuck" — the same popular items dominate; new/niche items rarely surface.
- Engagement metrics look healthy but catalog coverage and discovery are shrinking over time.
- Suspected rich-get-richer dynamics, filter bubbles, or unfair exposure across creators/sellers.

**When NOT to Use:**
- For one-off offline metric comparison (use `recsys_offline_evaluation.md`).
- For handling brand-new entities specifically (use `recsys_cold_start_strategy.md`).
- For a formal protected-attribute fairness audit with legal framing (route to a dedicated fairness prompt and cite a fairness definition).

## Inputs / Context

Provide what you can:
- **Exposure & engagement logs** — what was shown, at what position, and what was engaged, over time.
- **Catalog dynamics** — coverage over time (what fraction of items ever get impressions), Gini/concentration of exposure.
- **Training loop** — how often the model retrains on logged interactions, and whether any debiasing/propensity weighting exists.
- **Position logging** — rank of each impression (needed to estimate position bias).
- **Stakeholder concern** — discovery, creator/seller fairness, diversity, long-term retention.
- **Existing mitigations** — exploration slots, popularity damping, diversity rules already in place.

## Constraints

**Must:**
- Anchor each finding to evidence from the user's logs/metrics (e.g., exposure Gini, coverage trend, position-CTR curve) — not generic statements.
- Distinguish the three mechanisms: popularity bias (model favors popular), position bias (clicks driven by slot), feedback loop (training on self-generated data compounds both over time).
- Tie each finding to the long-term harm (collapsing diversity, unfair exposure, training on biased labels) and assign severity.

**Must Not:**
- Declare a feedback loop from a single snapshot — a loop is a *trend over retraining cycles*; require a temporal signal or mark it as suspected.
- Confuse legitimate popularity (genuinely better items) with popularity *bias* (exposure disproportionate to merit, amplified by exposure).
- Fabricate concentration or coverage numbers; reason from provided data and mark unknowns.

**Instructions:**

1. **Establish the exposure baseline.** Quantify how exposure is distributed across the catalog (concentration/Gini), and how coverage and head-share have trended over recent retraining cycles. A loop shows as worsening concentration over time.

2. **Test for popularity bias.** Compare an item's exposure to a merit estimate independent of exposure (e.g., conversion rate among those who saw it). Items with high exposure but mediocre per-impression merit signal bias, not quality.

3. **Test for position bias.** Examine the CTR-by-position curve. Steeply decaying CTR independent of item identity indicates clicks are driven by slot — meaning click labels overstate top-ranked items and understate lower ones.

4. **Trace the feedback loop.** Connect the dots: biased exposure → biased click labels → next model trains on them → amplifies exposure. Look for the compounding signature across retrain cycles (head share rising, coverage falling, new items decreasingly able to break in).

5. **Assess downstream harm.** Translate the dynamics into the harms the stakeholders care about: shrinking discovery, unfair creator/seller exposure, filter bubbles, and degraded long-term retention — separating these from healthy short-term engagement.

6. **Design mitigations.** Map each confirmed mechanism to a fix: propensity/IPS weighting or position-aware training for position bias; exploration budget and popularity damping for popularity bias; loop-breaking via debiased labels and diversity/coverage objectives.

7. **Specify monitoring.** Define ongoing metrics (exposure Gini, catalog coverage, new-item break-in rate, position-corrected CTR) so the loop is caught early, not after diversity has collapsed.

**Output Format:**

A markdown audit:
- **Bias & Loop Summary** — table: Finding | Mechanism | Confidence | Long-Term Harm | Severity.
- **Popularity Bias** — exposure-vs-merit evidence.
- **Position Bias** — CTR-by-position evidence and label-distortion implication.
- **Feedback Loop** — the compounding trend evidence (or why it's suspected, not confirmed).
- **Mitigations** — ranked, each mapped to a mechanism.
- **Monitoring Plan** — metrics + thresholds to track the loop going forward.
- **INSUFFICIENT EVIDENCE** — a first-class finding for the feedback-loop question specifically. A compounding trend in logged data is consistent with both a loop and genuinely shifting demand; separating them needs exposure the model did not choose. Name the unblocking datum: a randomized or unpersonalized exposure slice, however small, over a stated period.

## Verification

- [ ] Each finding cites specific log/metric evidence (Gini, coverage trend, position-CTR), not a generic claim.
- [ ] Popularity bias, position bias, and feedback loop are diagnosed as distinct mechanisms.
- [ ] Feedback-loop claims rest on a temporal/over-cycle trend, or are explicitly labeled suspected.
- [ ] Legitimate popularity is distinguished from popularity bias via a merit-vs-exposure comparison.
- [ ] Each mitigation maps to a confirmed mechanism and a monitoring metric.
- [ ] No fabricated concentration/coverage numbers.
- [ ] The feedback-loop finding is marked INSUFFICIENT EVIDENCE where no randomized or unpersonalized exposure exists, with that slice named as what would resolve it.

## False-Positive Prevention

❌ **DON'T:**
- Call high exposure of a popular item "bias" without checking whether its per-impression merit actually justifies it.
- Declare a feedback loop from one week's snapshot — a loop is a trend across retraining cycles, not a single concentration reading.
- Treat top-slot click rates as relevance — they're inflated by position; correct for it before judging the model.
- Recommend "just add diversity" without identifying which mechanism (popularity vs position vs loop) is actually driving the harm.

✅ **DO:**
- Separate merit from exposure: compare conversion-per-impression, not raw exposure, to detect true bias.
- Look for the compounding signature over time (rising head share, falling coverage, new items failing to break in).
- Correct click labels for position (IPS / position-aware models) before concluding the ranker prefers an item on quality.
- Map each mitigation to the specific mechanism it addresses and attach a monitoring metric so the fix is verifiable.

## Example Output

```markdown
## Feedback-Loop & Bias Audit: Marketplace Home Recommendations

### Bias & Loop Summary
| Finding | Mechanism | Confidence | Long-Term Harm | Severity |
|---|---|---|---|---|
| Top 1% of items take 48% of impressions, trending up from 39% over 6 retrains | Feedback loop | High | Discovery collapse; seller unfairness | Critical |
| High-exposure items have median per-impression conversion below catalog median | Popularity bias | High | Exposure ≠ merit | High |
| CTR at slot 1 ≈ 6× slot 10 independent of item swaps | Position bias | High | Click labels overstate top items | High |
| New sellers' items rarely break into top slots within 30 days | Loop symptom | Medium | Unfair new-entrant exposure | High |

### Popularity Bias
Bucketed items by exposure decile; the top decile's conversion-per-impression (0.018) is below the 4th–6th deciles (0.024). Exposure is outrunning merit → bias, not quality.

### Position Bias
Position-swap experiment logs show CTR(slot1)/CTR(slot10) ≈ 6.1 with item identity held out → clicks are slot-driven; training on raw clicks rewards whatever already ranks high.

### Feedback Loop
Head-share rose 39%→48% across 6 weekly retrains while catalog coverage fell 0.24→0.18. Biased exposure → biased clicks → next model amplifies. Confirmed by the over-cycle trend, not a snapshot.

### Mitigations (ranked)
1. Position-aware training (IPS-weight clicks by position propensity) — fixes label distortion at the root.
2. Exploration budget (2/20 slots Thompson-sampled) + popularity damping in the ranking label — breaks the loop.
3. Coverage/new-entrant objective term + creator-level exposure cap — addresses fairness harm.

### Monitoring Plan
Weekly: exposure Gini (alert if +0.03/cycle), catalog coverage (alert if -0.02/cycle), new-seller break-in rate, position-corrected CTR. Review at each retrain gate.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** baseline → popularity → position → loop → harm → mitigation → monitoring.
- **RT-05 (Evidence-Based Reasoning):** every finding anchored to a concentration/coverage/position statistic.
- **QA-12 (False Positives Identification):** separates legitimate popularity from popularity bias, and loops from snapshots.
- **DS-06 (Prioritization & Severity Guidance):** findings ranked by severity and long-term harm.
- **CM-02 (Constraint Specification):** exploration budget and exposure caps as governing constraints on the fix.

**Related Prompts:**
- `recsys_offline_evaluation.md` — the same biases explain the offline→online gap.
- `recsys_cold_start_strategy.md` — exploration and cold-item exposure that break the loop.
- `recsys_objective_business_alignment.md` — objective terms that resist short-term engagement traps.
