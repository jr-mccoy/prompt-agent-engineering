---
title: "Multi-Criteria Optimization for Schedule Variant Ranking"
category: algorithms
description: "Design, verify, and pressure-test scoring functions that rank schedule variants by fairness, coverage, balance, and gap minimization"
tags:
  - algorithms
  - optimization
  - scheduling
  - fairness
  - multi-criteria
  - scoring
  - pareto
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DS-02  # Metric Specification
  - RT-05  # Evidence-Based Reasoning
  - DS-06  # Prioritization Guidance
  - QA-02  # Adversarial Stress-Test
difficulty: advanced
version: "1.0"
updated: 2026-03-04
related_prompts:
  - algorithms_constraint_satisfaction_scheduling.md
  - algorithms_data_structure_selection.md
---

# Multi-Criteria Optimization for Schedule Variant Ranking

**Objective:** Design, verify, and stress-test the scoring functions used to rank schedule variants, ensuring metrics correctly capture fairness, coverage, balance, and gap minimization without producing counterintuitive or gameable results.

**When to Use:** Use this prompt when a scheduling system generates multiple valid schedule variants and must rank them by quality. Applicable whenever schedules are scored on fairness of assignment distribution, completeness of coverage, weekend/weekday balance, or spacing between assignments.

## Instructions

### 1. Metric Inventory

List every scoring dimension. For each, define:

| Dimension | Formula | Range | Unit | Direction |
|-----------|---------|-------|------|-----------|
| **Fairness** | 1 - (σ / μ) of assignment counts | [0, 1] | coefficient of variation | Higher = fairer |
| **Coverage** | filled_slots / required_slots | [0, 1] | ratio | Higher = better |
| **Balance** | 1 - \|weekend_ratio - target_ratio\| | [0, 1] | deviation | Higher = better |
| **Gap Score** | min(gaps) / target_min_gap | [0, 1+] | ratio | Higher = better (capped at 1) |

**Verify:**
- Is every metric normalized to a comparable scale?
- Do all metrics use the same direction convention (higher = better)?
- Are there metrics that can be undefined (division by zero when μ = 0)?

### 2. Individual Metric Verification

For each metric, trace through a **worked example** with a minimal schedule:

```
Example: 4 workers (A, B, C, D), 7 days, 1 role per day

Schedule Variant 1: A B C D A B C    → counts: A=2, B=2, C=2, D=1
Schedule Variant 2: A A B B C C D    → counts: A=2, B=2, C=2, D=1
Schedule Variant 3: A B A B A B C    → counts: A=3, B=3, C=1, D=0

Fairness (coefficient of variation):
  V1: μ=1.75, σ=0.43  → fairness = 1 - (0.43/1.75) = 0.75
  V2: μ=1.75, σ=0.43  → fairness = 0.75 (same counts, different distribution)
  V3: μ=1.75, σ=1.30  → fairness = 0.26

Question: V1 and V2 have identical fairness scores but V1 has better
spacing. Does the scoring system capture this distinction?
```

**For each metric, answer:**
- What is the worst possible input? What score does it produce?
- Can two schedules with the same score feel different to workers?
- Is the metric sensitive to roster size? (Does it work for 5 people and 50 people?)

### 3. Adversarial Schedule Tests

For each metric, construct a schedule that **scores high but is intuitively unfair:**

```
Adversarial Example — Fairness Metric:
  Workers: A, B, C, D (A is available all days, D only weekdays)
  Schedule: A=Mon,Sat,Sun  B=Tue  C=Wed  D=Thu,Fri
  Counts: A=3, B=1, C=1, D=2

  Fairness score may be reasonable (σ/μ ≈ 0.45) but A gets
  ALL weekend shifts. Is weekend burden captured by the fairness metric?
  If not, a separate weekend-balance metric is needed.
```

**For each metric, ask:** "What input would make this metric score a manifestly unfair schedule as optimal?" If you can construct such an input, the metric has a blind spot.

### 4. Composite Score Design

When combining metrics into a single score:

```python
# Weighted sum approach
composite = (w_fairness * fairness +
             w_coverage * coverage +
             w_balance * balance +
             w_gap * gap_score)

# Key questions:
# 1. Are weights normalized? (sum to 1.0)
# 2. What happens when one metric dominates?
# 3. Can a perfect coverage score mask terrible fairness?
```

**Weight Sensitivity Analysis:**
- Vary each weight by ±20% while holding others fixed
- Record how the top-ranked variant changes
- If rank order changes with a 5% weight shift, the ranking is brittle

**Alternative: Pareto Ranking**
- Variant A dominates Variant B if A is ≥ B on all metrics and > on at least one
- Non-dominated variants form the Pareto front
- Advantage: no weight tuning. Disadvantage: may produce many incomparable variants

### 5. Cross-Metric Conflict Detection

Build a conflict matrix:

| | Fairness | Coverage | Balance | Gap |
|---------|----------|----------|---------|-----|
| **Fairness** | — | Low | Medium | Low |
| **Coverage** | Low | — | Low | High |
| **Balance** | Medium | Low | — | Medium |
| **Gap** | Low | High | Medium | — |

For each "Medium" or "High" conflict pair, document the tradeoff:
- **Coverage vs Gap:** Maximizing coverage may require assigning workers with minimal gaps, violating gap preferences
- **Fairness vs Balance:** Perfect weekend balance may require unequal total assignments

### 6. Dominance and Redundancy Check

Verify that:
- No variant in the output is dominated (strictly worse on all metrics than another variant)
- Variants labeled "distinct" actually differ by at least one assignment
- The top-ranked variant is not dominated by any lower-ranked variant
- Score differences between adjacent ranks are meaningful (not floating-point noise)

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag a composite scoring function as "arbitrary" without first understanding what the weights represent in the domain (e.g., coverage is non-negotiable in healthcare)
- Claim metrics are "redundant" just because they correlate on typical inputs — they may diverge on edge cases
- Recommend Pareto ranking as universally superior — it produces too many incomparable variants for end users who need a single best schedule
- Assume equal weights are always the right default

✅ **DO:**
- Always verify metrics with a worked numeric example (minimum 4 workers, 7 days)
- Test with adversarial inputs specifically designed to expose metric blind spots
- Check that the composite score is continuous (small input changes produce small score changes)
- Verify metric behavior at boundaries: empty schedule, fully-assigned schedule, single worker

## Expected Output

1. **Metric Specification Cards** — For each dimension: formula, range, worked example, worst-case input, known limitations
2. **Adversarial Test Results** — Schedules that expose metric blind spots, with recommendations
3. **Weight Sensitivity Report** — How rank order changes with weight perturbation
4. **Conflict Matrix** — Which metrics are in tension, with documented tradeoffs
5. **Dominance Audit** — Confirmation that no dominated variants appear in output
6. **Recommendations** — Specific improvements to scoring functions, ordered by impact

## Quality Checklist

- [ ] Every metric has an explicit formula with defined range
- [ ] At least one adversarial schedule is constructed per metric
- [ ] Weight sensitivity tested with ±20% variation
- [ ] Cross-metric conflicts identified and documented
- [ ] Worked example traces through composite scoring end-to-end

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focuses on scoring function design and verification
- **ST-02** (Structured Sequential Instructions) — Systematic walkthrough from individual metrics to composite scoring
- **RT-02** (Multi-Dimensional Analysis) — Evaluates fairness, coverage, balance, and gap dimensions
- **DS-02** (Metric Specification) — Explicit formulas with ranges and units for each dimension
- **RT-05** (Evidence-Based Reasoning) — Requires worked numeric examples, not abstract claims
- **DS-06** (Prioritization Guidance) — Ranks improvements by impact on scoring quality
- **QA-02** (Adversarial Stress-Test) — Constructs inputs designed to break each metric

## Related Prompts

- `algorithms_constraint_satisfaction_scheduling.md` — The CSP engine that produces the variants being scored
- `testing_schedule_validity_oracle.md` — Independent validation that scored schedules are actually valid
- `testing_nondeterministic_variant_validation.md` — Testing variant generation and ranking stability
- `performance_scheduling_algorithm_optimization.md` — Optimizing variant generation performance

## Customization Guide

**For healthcare scheduling:**
- Weekend/holiday burden is often the primary fairness concern (not total count)
- Add a "consecutive weekend" penalty metric — no worker should have back-to-back weekend assignments
- PRN workers should be excluded from fairness calculations or weighted differently

**For retail scheduling:**
- Peak-hour coverage is more important than total coverage — weight coverage by time-of-day
- Employee preference satisfaction may be an explicit metric (shift preferences)
- Part-time workers have different target assignment counts — normalize fairness by contracted hours

**For emergency services:**
- Rest compliance is a hard constraint, not a soft metric — ensure gap_score reflects mandatory rest
- Overtime fairness (cumulative hours, not just shift counts) may be the dominant metric
- Cross-training exposure: score how many different stations/roles each worker experiences
