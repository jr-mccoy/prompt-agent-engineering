---
title: "Validating Non-Deterministic and Multi-Variant System Outputs"
category: testing
description: "Testing strategies for systems that produce multiple valid outputs including invariant-based testing, statistical properties, reproducibility via seeding, and variant distinctness verification"
tags:
  - testing
  - non-deterministic
  - variants
  - property-based-testing
  - reproducibility
  - scheduling
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DS-02  # Metric Specification
  - QA-02  # Adversarial Stress-Test
  - DS-03  # Tool and Methodology Suggestions
difficulty: advanced
version: "1.0"
updated: 2026-03-04
related_prompts:
  - testing_constraint_logic_edge_cases.md
  - testing_schedule_validity_oracle.md
  - algorithms_multi_criteria_schedule_optimization.md
---

# Validating Non-Deterministic and Multi-Variant System Outputs

**Objective:** Establish testing strategies for systems that produce multiple valid outputs per input — verifying structural invariants, statistical properties, reproducibility, and variant quality — without relying on exact output comparison.

**When to Use:** Use this prompt when testing a system that generates multiple schedule variants, optimization solutions, or any output where the same input can produce different valid results across runs. Standard assertion-based testing fails here because `assertEqual(actual, expected)` is meaningless when multiple outputs are correct.

**Instructions:**

1. **Non-Determinism Source Inventory**

   Identify every source of non-determinism in the system:

   | Source | Type | Example | Controllable? |
   |--------|------|---------|---------------|
   | Random seed | Algorithmic | Randomized worker selection order | Yes (set seed) |
   | Set/dict iteration | Language | Python `set` iteration order | Yes (sort before use) |
   | Floating-point comparison | Numeric | Fairness scores differ by ε | Yes (use tolerance) |
   | Thread scheduling | OS | Worker threads produce results in varying order | Partially (deterministic mode) |
   | Timestamp-based IDs | System | UUIDs or time-based variant IDs | Yes (mock clock) |

   **Classify each source:**
   - **Controlled:** Can be made deterministic via seed or configuration
   - **Incidental:** Shouldn't affect output but does due to implementation (e.g., set ordering)
   - **Inherent:** Multiple valid solutions exist by design (the system is meant to produce variants)

2. **Invariant Specification**

   Define properties that MUST hold regardless of which variant is selected:

   ```python
   def validate_invariants(schedule, config):
       """These must hold for EVERY variant."""
       errors = []

       # Structural invariants
       for day in config.schedule_days:
           for role in config.required_roles:
               if schedule.assignment(day, role) is None:
                   errors.append(f"Missing assignment: {day}/{role}")

       # Constraint invariants
       for worker in schedule.assigned_workers:
           dates = schedule.dates_for(worker)
           for i in range(len(dates) - 1):
               gap = (dates[i+1] - dates[i]).days
               if gap < config.min_gap:
                   errors.append(f"{worker}: gap {gap} < {config.min_gap}")

       # Roster invariants
       for day, worker in schedule.all_assignments():
           if day in config.unavailable_dates(worker):
               errors.append(f"{worker} assigned on unavailable {day}")
           if worker not in config.roster:
               errors.append(f"Unknown worker: {worker}")

       return errors
   ```

   **Core invariant categories:**
   - **Coverage:** Every required slot has an assignment
   - **Constraint compliance:** All hard constraints satisfied
   - **Roster validity:** Only rostered, available, qualified workers assigned
   - **Score plausibility:** Fairness/coverage scores are within [0, 1]

3. **Property-Based Testing Setup**

   ```python
   from hypothesis import given, settings, strategies as st

   # Strategy: generate valid configurations
   config_strategy = st.builds(
       ScheduleConfig,
       num_workers=st.integers(3, 15),
       num_days=st.integers(7, 60),
       min_gap=st.integers(1, 4),
       max_per_week=st.integers(1, 5),
       num_variants=st.integers(1, 5),
   )

   @given(config=config_strategy)
   @settings(max_examples=100, deadline=30000)  # 30s per example
   def test_all_variants_satisfy_invariants(config):
       result = scheduler.generate(config)
       if result.is_feasible:
           for variant in result.variants:
               errors = validate_invariants(variant, config)
               assert errors == [], f"Invariant violations: {errors}"
   ```

   **Run at least 100 random configurations.** Track:
   - How many are feasible vs infeasible
   - Any invariant violations found
   - Longest generation time (detect performance regressions)

4. **Reproducibility via Seeding**

   ```python
   def test_seed_produces_identical_output():
       config = load_config("test_config.yaml")

       result_a = scheduler.generate(config, seed=42)
       result_b = scheduler.generate(config, seed=42)

       # Same seed → identical output (variant order, assignments, scores)
       assert result_a.variants == result_b.variants
       assert result_a.scores == result_b.scores

   def test_different_seeds_may_differ():
       config = load_config("test_config.yaml")

       result_a = scheduler.generate(config, seed=42)
       result_b = scheduler.generate(config, seed=99)

       # Both valid, but may differ
       for variant in result_a.variants + result_b.variants:
           assert validate_invariants(variant, config) == []
   ```

   **Verify:**
   - Is the seed threaded through ALL sources of randomness?
   - Does the seed control set/dict iteration order?
   - Is the seed logged with results for debugging? ("This schedule was generated with seed 42")

5. **Variant Distinctness Verification**

   When N variants are requested, verify they are meaningfully different:

   ```python
   def test_variants_are_distinct():
       result = scheduler.generate(config, num_variants=5)

       for i in range(len(result.variants)):
           for j in range(i + 1, len(result.variants)):
               diff = assignment_diff(result.variants[i], result.variants[j])
               assert diff > 0, f"Variants {i} and {j} are identical"

   def assignment_diff(schedule_a, schedule_b):
       """Count number of (day, role) slots with different assignments."""
       count = 0
       for day in schedule_a.days:
           for role in schedule_a.roles:
               if schedule_a.assignment(day, role) != schedule_b.assignment(day, role):
                   count += 1
       return count
   ```

   **Also verify:**
   - Minimum diff threshold: variants differing by only 1 assignment aren't meaningfully different
   - No duplicate variants in the output list
   - The number of returned variants matches the requested count (or is documented as "best effort")

6. **Score Monotonicity and Stability**

   ```python
   def test_variant_ranking_is_consistent():
       result = scheduler.generate(config)

       # Variants should be sorted by composite score (descending)
       scores = [v.composite_score for v in result.variants]
       assert scores == sorted(scores, reverse=True)

       # Score differences should be meaningful (not floating-point noise)
       for i in range(len(scores) - 1):
           if scores[i] != scores[i+1]:  # If ranked differently
               assert abs(scores[i] - scores[i+1]) > 1e-6  # Meaningful difference
   ```

   **Verify:**
   - Same config with same seed produces same ranking
   - Small config changes produce proportional score changes (no wild jumps)
   - Scores are not all identical (which would mean the scoring function is broken)

7. **Regression Oracle Pattern**

   For deterministic-mode runs, store expected output:

   ```python
   # Generate oracle once
   def create_oracle():
       config = load_config("regression_config.yaml")
       result = scheduler.generate(config, seed=42)
       save_oracle("tests/oracles/regression_seed42.json", result)

   # Test against oracle
   def test_regression_against_oracle():
       config = load_config("regression_config.yaml")
       result = scheduler.generate(config, seed=42)
       oracle = load_oracle("tests/oracles/regression_seed42.json")

       assert result.variants[0].assignments == oracle.variants[0].assignments
       assert abs(result.scores[0] - oracle.scores[0]) < 1e-10
   ```

   **Oracle maintenance rules:**
   - Update oracles ONLY when algorithm changes are intentional
   - Document WHY each oracle was updated in the commit message
   - Keep oracles small (one config per test scenario, not large production configs)

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Assert exact output equality for non-seeded runs — this is the #1 testing mistake for non-deterministic systems
- Flag variant diversity as a "bug" — multiple valid solutions is the intended behavior
- Report different scores across runs as "flaky tests" if different seeds are being used
- Require all N requested variants to be returned — for small configs, fewer than N distinct valid schedules may exist

✅ **DO:**
- Always test with a fixed seed first to establish a baseline
- Use invariant-based assertions, not output-comparison assertions
- Verify that the seed mechanism actually controls all non-determinism (run twice, compare)
- Test with both "easy" configs (many valid solutions) and "tight" configs (few valid solutions)
- Log the seed with every test run for reproducibility

## Expected Output

1. **Non-Determinism Inventory** — All sources classified as controlled/incidental/inherent
2. **Invariant Specification** — Complete list of properties that must always hold
3. **Property Test Results** — Pass rate across 100+ random configurations
4. **Reproducibility Report** — Seed mechanism verification (same seed → same output)
5. **Distinctness Analysis** — Variant diversity metrics and duplicate detection
6. **Score Stability Report** — Ranking consistency and score sensitivity
7. **Oracle Test Suite** — Regression fixtures for deterministic-mode runs

## Quality Checklist

- [ ] All sources of non-determinism are identified
- [ ] Core invariants are specified and tested
- [ ] Seed reproducibility is verified (same seed → same output)
- [ ] Variant distinctness is checked
- [ ] At least one regression oracle exists

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focuses on testing non-deterministic multi-variant output
- **ST-02** (Structured Sequential Instructions) — From source identification to regression oracles
- **RT-02** (Multi-Dimensional Analysis) — Invariants, reproducibility, distinctness, scoring, regression
- **DS-02** (Metric Specification) — Defines measurable thresholds for distinctness and score stability
- **QA-02** (Adversarial Stress-Test) — Tests edge cases: tight configs, duplicate variants, score ties
- **DS-03** (Tool and Methodology Suggestions) — Recommends Hypothesis for property-based testing

## Related Prompts

- `testing_constraint_logic_edge_cases.md` — Edge case testing for the constraints producing these variants
- `testing_schedule_validity_oracle.md` — Independent validation for any single variant
- `algorithms_multi_criteria_schedule_optimization.md` — Scoring and ranking being tested here
- `testing_unit_test_generation.md` — General test generation (this prompt extends it for non-deterministic systems)
