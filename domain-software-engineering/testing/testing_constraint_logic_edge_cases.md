---
title: "Constraint Logic Edge Case Testing for Scheduling Systems"
category: testing
description: "Generate and verify edge case tests for constraint-based scheduling including constraint interactions, boundary conditions, infeasibility detection, and evaluation order dependence"
tags:
  - testing
  - constraints
  - scheduling
  - edge-cases
  - property-based-testing
  - hypothesis
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DS-03  # Tool and Methodology Suggestions
  - QA-02  # Adversarial Stress-Test
  - DT-02  # Specific Focus Areas
  - RT-05  # Evidence-Based Reasoning
difficulty: advanced
version: "1.0"
updated: 2026-03-04
related_prompts:
  - testing_unit_test_generation.md
  - testing_schedule_validity_oracle.md
  - ../algorithms/algorithms_constraint_satisfaction_scheduling.md
  - testing_nondeterministic_variant_validation.md
---

# Constraint Logic Edge Case Testing for Scheduling Systems

**Objective:** Generate a comprehensive test suite targeting the edge cases specific to constraint-based scheduling — including constraint interactions, boundary semantics, infeasibility detection, and evaluation order dependence — that generic unit test generation misses.

**When to Use:** Use this prompt when testing a scheduling engine with plugin-based or rule-based constraints (minimum gap, weekly limits, qualifications, conflicts). Standard test generation covers individual function correctness; this prompt targets the emergent behavior of constraint combinations and the specific failure modes of scheduling logic.

**Instructions:**

1. **Constraint Taxonomy Review**

   For each constraint type in the system, document:

   | Constraint | Boundary Semantics | Scope | Stateful? |
   |-----------|-------------------|-------|-----------|
   | Minimum Gap (N days) | Is day N included? (`>=N` or `>N`?) | Per-worker | Yes (depends on prior assignments) |
   | Weekly Limit (max M) | Does it count the current assignment? | Per-worker per week | Yes (accumulated count) |
   | Window Restriction | Pre/post period boundary inclusive? | Per-worker per period | Yes (relative to period) |
   | Attribute Conflict | Checked per-day or per-shift? | Per-day pair | No (only current assignments) |
   | Qualification | Valid at assignment time or schedule time? | Per-worker per role | Potentially (if certs expire) |

   **For each constraint, answer:** If the boundary condition is off-by-one, would the resulting schedule look plausible but be wrong?

2. **Single Constraint Edge Cases**

   For EACH constraint type, generate tests for:

   **a. Off-by-one on counts/days:**
   ```python
   # Minimum gap = 2 days
   # Worker assigned Monday. Is Wednesday (2 days later) allowed?
   def test_gap_exactly_at_minimum():
       schedule = {date(2025,1,6): "Alice"}  # Monday
       # date(2025,1,8) = Wednesday, gap = 2
       assert constraint.is_satisfied("Alice", date(2025, 1, 8))  # Should this pass?

   def test_gap_one_less_than_minimum():
       schedule = {date(2025,1,6): "Alice"}  # Monday
       # date(2025,1,7) = Tuesday, gap = 1
       assert not constraint.is_satisfied("Alice", date(2025, 1, 7))
   ```

   **b. Empty/minimal roster:**
   ```python
   def test_single_worker_roster():
       # Only one worker available — can they fill all slots?
       # Weekly limit may make this impossible

   def test_empty_roster():
       # Zero workers — should report infeasibility immediately
   ```

   **c. Horizon shorter than constraint window:**
   ```python
   def test_gap_larger_than_schedule():
       # min_gap = 7 days, schedule is only 5 days
       # Worker can only be assigned once — is this handled?
   ```

   **d. Constraint applies to zero slots:**
   ```python
   def test_weekly_limit_on_week_with_no_eligible_days():
       # All days in a week are holidays — weekly limit is irrelevant
       # Does the constraint still evaluate correctly?
   ```

3. **Constraint Interaction Matrix**

   Build a pairwise test matrix:

   ```
   Interaction Risk Matrix:
                    Gap    Weekly   Window   Conflict   Qual
   Gap              —      HIGH     MED      LOW        LOW
   Weekly Limit   HIGH      —       MED      LOW        LOW
   Window Restr.  MED      MED       —       LOW        MED
   Conflict       LOW      LOW      LOW       —         MED
   Qualification  LOW      LOW      MED      MED         —
   ```

   **For each HIGH-risk pair, write a specific test:**

   ```python
   def test_gap_plus_weekly_limit_conflict():
       """Gap=2 + weekly_limit=1 with 3 workers for 7 days.
       Each worker can work at most once per week with 2-day spacing.
       Week has 7 days. 3 workers × 1/week = 3 assignments max.
       But with gap=2, assignments must be spaced: Mon, Wed, Fri (3 slots).
       Exactly satisfiable — no room for error."""
       config = Config(gap=2, weekly_limit=1, workers=3, days=7)
       result = scheduler.generate(config)
       assert result.is_complete()  # All 7 days filled? Or only 3?
   ```

4. **Infeasibility Detection Tests**

   Construct at minimum 5 provably unsatisfiable configurations:

   | # | Configuration | Why Unsatisfiable |
   |---|--------------|-------------------|
   | 1 | 2 workers, 7 days, max 1/week | Need 7 workers for 7 days |
   | 2 | 3 workers, 5 days, gap=4 | Each worker can fill at most 2 days (Mon+Fri), need 5 |
   | 3 | Workers A,B share conflict attribute, only role needs 2/day | Cannot pair A and B |
   | 4 | All workers unavailable on Wednesday | Wednesday slot unfillable |
   | 5 | Worker needs qualification X, no one has it | Role is impossible to fill |

   **For each:**
   - Does the engine report infeasibility (not a partial schedule, not a hang)?
   - Is the error message specific? ("Cannot fill Wednesday: no qualified workers available")
   - How long does infeasibility detection take? (Should be fast, not exponential search)

5. **Constraint Evaluation Order Tests**

   ```python
   def test_constraint_order_independence():
       """Verify that reordering constraint evaluation doesn't change results."""
       config = standard_test_config()

       # Run with constraints in original order
       result_a = scheduler.generate(config, constraint_order=["gap", "weekly", "conflict"])

       # Run with constraints reversed
       result_b = scheduler.generate(config, constraint_order=["conflict", "weekly", "gap"])

       # Both should produce valid schedules (may differ, but both valid)
       assert validate_schedule(result_a)
       assert validate_schedule(result_b)
   ```

   **Why this matters:** If constraints prune domains, the order of pruning can affect which solutions are found. The engine should find valid solutions regardless of order (even if different solutions).

6. **Property-Based Testing with Hypothesis**

   ```python
   from hypothesis import given, strategies as st

   @given(
       num_workers=st.integers(min_value=1, max_value=20),
       num_days=st.integers(min_value=1, max_value=90),
       min_gap=st.integers(min_value=1, max_value=7),
       max_per_week=st.integers(min_value=1, max_value=7),
   )
   def test_schedule_invariants(num_workers, num_days, min_gap, max_per_week):
       """Any generated schedule must satisfy all constraints."""
       config = build_config(num_workers, num_days, min_gap, max_per_week)
       result = scheduler.generate(config)

       if result.is_feasible:
           # Every assignment satisfies gap constraint
           for worker in result.workers:
               dates = result.assignments_for(worker)
               for i in range(len(dates) - 1):
                   assert (dates[i+1] - dates[i]).days >= min_gap

           # Weekly limits respected
           for worker in result.workers:
               for week in result.weeks:
                   count = result.count_in_week(worker, week)
                   assert count <= max_per_week
   ```

   **Key properties to test:**
   - All hard constraints satisfied in every variant
   - Coverage: if feasible, required roles are filled
   - Fairness metrics match independent recalculation
   - No worker assigned on their unavailable dates

7. **Regression Test Pattern**

   For schedules that "used to work but broke":

   ```python
   # Golden-file pattern
   def test_regression_q1_2025_pacu():
       """Known-good schedule from Q1 2025 PACU deployment."""
       config = load_config("tests/fixtures/pacu_q1_2025.yaml")
       result = scheduler.generate(config, seed=42)
       expected = load_schedule("tests/fixtures/pacu_q1_2025_expected.json")

       # Don't compare exact assignments (may differ with algorithm changes)
       # Instead compare structural properties
       assert result.total_assignments == expected.total_assignments
       assert result.unfilled_slots == expected.unfilled_slots
       assert result.fairness_score >= expected.fairness_score * 0.95  # Within 5%
   ```

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag a schedule as "wrong" because it differs from a previous run — non-deterministic solvers may produce different valid schedules
- Report infeasibility as a "bug" when the configuration is genuinely unsatisfiable — the bug would be NOT reporting it
- Assume constraint violations in soft constraints are errors — soft constraints are preferences, not requirements
- Write tests that assert exact schedule output instead of structural invariants

✅ **DO:**
- Always distinguish hard constraint violations (bugs) from soft constraint violations (trade-offs)
- Test constraint boundary semantics with the exact boundary value (gap=N, test day N exactly)
- Include at least one infeasibility test per constraint type
- Use property-based testing for invariants that must hold across all valid configurations
- Test with realistic roster sizes, not just toy examples (10+ workers, 30+ days)

## Expected Output

1. **Constraint Taxonomy** — Table of all constraints with boundary semantics documented
2. **Single Constraint Tests** — At least 3 edge case tests per constraint type
3. **Interaction Matrix** — Pairwise risk assessment with tests for HIGH-risk pairs
4. **Infeasibility Tests** — 5+ unsatisfiable configurations with expected behavior
5. **Order Independence Tests** — Verification that constraint order doesn't affect validity
6. **Property-Based Tests** — Hypothesis strategies and invariant assertions
7. **Regression Fixtures** — Golden-file test pattern for known-good schedules

**Test Matrix Summary:**

| Constraint | Off-by-one | Empty Roster | Short Horizon | Interaction | Infeasible |
|-----------|-----------|-------------|--------------|-------------|------------|
| Gap | ✓ | ✓ | ✓ | ✓ (+ Weekly) | ✓ |
| Weekly | ✓ | ✓ | ✓ | ✓ (+ Gap) | ✓ |
| Window | ✓ | ✓ | ✓ | ✓ (+ Weekly) | ✓ |
| Conflict | ✓ | ✓ | — | ✓ (+ Qual) | ✓ |
| Qualification | ✓ | ✓ | — | ✓ (+ Conflict) | ✓ |

## Quality Checklist

- [ ] Every constraint type has boundary-value tests
- [ ] At least 3 constraint pairs are tested for interaction
- [ ] Infeasibility detection is tested (not just satisfiable cases)
- [ ] Property-based tests cover core invariants
- [ ] Tests assert invariants, not exact output

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focuses on scheduling-specific edge case testing
- **ST-02** (Structured Sequential Instructions) — Systematic from taxonomy to regression
- **RT-02** (Multi-Dimensional Analysis) — Single constraints, interactions, infeasibility, order, properties
- **DS-03** (Tool and Methodology Suggestions) — Recommends Hypothesis for property-based testing
- **QA-02** (Adversarial Stress-Test) — Constructs configurations designed to break constraints
- **DT-02** (Specific Focus Areas) — Enumerates the 5 canonical constraint edge case categories
- **RT-05** (Evidence-Based Reasoning) — Ties each test to specific constraint implementation details

## Related Prompts

- `testing_unit_test_generation.md` — General unit test generation (this prompt extends it for scheduling)
- `testing_schedule_validity_oracle.md` — Independent validation that complements these edge case tests
- `algorithms_constraint_satisfaction_scheduling.md` — The engine being tested
- `testing_nondeterministic_variant_validation.md` — Testing the variant generation layer

## Customization Guide

**For healthcare scheduling:**
- Add qualification expiration edge cases (cert expires mid-schedule)
- Test holiday rotation patterns (FSF/SFS) at year boundaries
- PRN workers: test when PRN workers are excluded from fairness calculations

**For retail scheduling:**
- Test part-time workers with variable availability across weeks
- Shift overlap constraints: opener/closer cannot be same person (add to interaction matrix)
- Peak-hour coverage: test that minimum staffing levels are met during rush periods

**For emergency services:**
- 24/48 rotation: test that the 48-hour off period is correctly enforced across week boundaries
- Mandatory rest: test that rest constraints interact correctly with callback/overtime rules
- Multi-station assignment: test that station qualification + rotation rules compose correctly
