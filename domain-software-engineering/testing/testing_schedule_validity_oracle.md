---
title: "Schedule Validity Oracle: Independent Correctness Verification"
category: testing
description: "Build an independent validation function that verifies schedule correctness without using the solver's own constraint evaluation, covering structural, constraint, fairness, and domain invariants"
tags:
  - testing
  - validation
  - oracle
  - scheduling
  - correctness
  - independent-verification
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DS-02  # Metric Specification
  - QA-02  # Adversarial Stress-Test
  - RT-05  # Evidence-Based Reasoning
  - DT-01  # Hierarchical Task Breakdown
difficulty: advanced
version: "1.0"
updated: 2026-03-04
related_prompts:
  - testing_constraint_logic_edge_cases.md
  - testing_nondeterministic_variant_validation.md
  - ../algorithms/algorithms_constraint_satisfaction_scheduling.md
  - algorithms_multi_criteria_schedule_optimization.md
---

# Schedule Validity Oracle: Independent Correctness Verification

**Objective:** Build an independent validation function — completely separate from the scheduling solver — that can verify whether any schedule (solver-produced, hand-crafted, or imported) satisfies all structural, constraint, and domain requirements for a given configuration.

**When to Use:** Use this prompt when you need confidence that generated schedules are correct independently of the solver that produced them. Without a separate oracle, a bug in constraint evaluation may produce a schedule that the solver considers "valid" by its own (buggy) rules. This is the foundational testing layer for any scheduling system.

**Instructions:**

### 1. Oracle Architecture

The oracle is a pure function with no dependency on the solver:

```python
def validate_schedule(
    schedule: Schedule,
    config: ScheduleConfig,
    roster: Roster,
) -> ValidationResult:
    """
    Independent validation of a schedule against its configuration.

    CRITICAL: This function must NOT import or call any code from
    the solver/engine. It implements constraint checks from scratch
    using only the schedule data and configuration.
    """
    errors = []
    warnings = []

    errors.extend(check_structural_validity(schedule, config))
    errors.extend(check_hard_constraints(schedule, config, roster))
    warnings.extend(check_soft_constraints(schedule, config, roster))
    warnings.extend(check_fairness_metrics(schedule, config, roster))

    return ValidationResult(
        is_valid=len(errors) == 0,
        errors=errors,
        warnings=warnings,
    )
```

**Design principles:**
- Oracle lives in a separate module/package from the solver
- Oracle does NOT import any solver code (enforced by import checks in CI)
- Oracle reads only the final schedule output and the configuration
- Oracle implements each constraint check from the specification, not from the solver code

### 2. Structural Validity Layer

Check the schedule's basic structure:

```python
def check_structural_validity(schedule, config):
    errors = []

    # Every day in the horizon has an entry
    for day in config.date_range():
        if day not in schedule.days:
            errors.append(StructuralError(
                f"Missing day: {day}",
                severity="critical",
            ))

    # Every required role is assigned on each day
    for day in schedule.days:
        for role in config.required_roles:
            assignment = schedule.get(day, role)
            if assignment is None:
                errors.append(StructuralError(
                    f"Unfilled slot: {day}/{role}",
                    severity="critical",
                ))

    # No worker appears twice on the same day (unless multi-shift)
    for day in schedule.days:
        workers_today = schedule.workers_on(day)
        if not config.allow_multi_shift:
            duplicates = [w for w in workers_today if workers_today.count(w) > 1]
            if duplicates:
                errors.append(StructuralError(
                    f"Duplicate assignment on {day}: {set(duplicates)}",
                    severity="critical",
                ))

    # All assigned workers exist in roster
    for day, role, worker in schedule.all_assignments():
        if worker not in roster:
            errors.append(StructuralError(
                f"Unknown worker '{worker}' assigned on {day}",
                severity="critical",
            ))

    return errors
```

### 3. Hard Constraint Compliance Layer

**Implement each hard constraint independently from the solver's implementation:**

```python
def check_hard_constraints(schedule, config, roster):
    errors = []

    # Minimum gap — implemented from specification, NOT from solver code
    if config.has_constraint("minimum_gap"):
        min_gap = config.constraint_value("minimum_gap", "days")
        for worker in schedule.assigned_workers():
            dates = sorted(schedule.dates_for(worker))
            for i in range(len(dates) - 1):
                gap = (dates[i+1] - dates[i]).days
                if gap < min_gap:
                    errors.append(ConstraintError(
                        constraint="minimum_gap",
                        worker=worker,
                        detail=f"Gap of {gap} days between {dates[i]} and {dates[i+1]} "
                               f"(minimum: {min_gap})",
                    ))

    # Weekly limit
    if config.has_constraint("weekly_limit"):
        for limit_rule in config.weekly_limit_rules():
            for worker in schedule.assigned_workers():
                for week_start in config.week_starts():
                    week_end = week_start + timedelta(days=6)
                    count = schedule.count_in_range(
                        worker, week_start, week_end,
                        role=limit_rule.role if limit_rule.role != "any" else None,
                    )
                    if count > limit_rule.max_per_week:
                        errors.append(ConstraintError(
                            constraint="weekly_limit",
                            worker=worker,
                            detail=f"{count} assignments in week of {week_start} "
                                   f"(max: {limit_rule.max_per_week} for {limit_rule.role})",
                        ))

    # Availability
    for day, role, worker in schedule.all_assignments():
        if roster.is_unavailable(worker, day):
            errors.append(ConstraintError(
                constraint="availability",
                worker=worker,
                detail=f"Assigned on unavailable date {day}",
            ))

    # Qualification
    if config.has_constraint("qualification"):
        for day, role, worker in schedule.all_assignments():
            required_quals = config.qualifications_for_role(role)
            worker_quals = roster.qualifications(worker)
            missing = required_quals - worker_quals
            if missing:
                errors.append(ConstraintError(
                    constraint="qualification",
                    worker=worker,
                    detail=f"Missing qualifications for {role}: {missing}",
                ))

    # Attribute conflict
    if config.has_constraint("attribute_conflict"):
        for day in schedule.days:
            workers_today = schedule.workers_on(day)
            for i in range(len(workers_today)):
                for j in range(i+1, len(workers_today)):
                    if roster.has_conflict(workers_today[i], workers_today[j]):
                        errors.append(ConstraintError(
                            constraint="attribute_conflict",
                            detail=f"{workers_today[i]} and {workers_today[j]} "
                                   f"conflict on {day}",
                        ))

    return errors
```

### 4. Soft Constraint Compliance Layer

For soft constraints, the oracle doesn't flag violations as errors but verifies the violation count matches what the solver reported:

```python
def check_soft_constraints(schedule, config, roster):
    warnings = []

    # Recount soft constraint violations independently
    oracle_violations = count_soft_violations(schedule, config, roster)
    solver_violations = schedule.reported_soft_violations

    if oracle_violations != solver_violations:
        warnings.append(ScoringWarning(
            f"Soft violation count mismatch: oracle={oracle_violations}, "
            f"solver={solver_violations}",
        ))

    return warnings
```

### 5. Fairness Metric Verification

Recompute all fairness scores from scratch:

```python
def check_fairness_metrics(schedule, config, roster):
    warnings = []

    # Recompute fairness score
    counts = [schedule.assignment_count(w) for w in roster.active_workers()]
    mean = sum(counts) / len(counts) if counts else 0
    std = (sum((c - mean)**2 for c in counts) / len(counts)) ** 0.5 if counts else 0
    oracle_fairness = 1 - (std / mean) if mean > 0 else 0

    if abs(oracle_fairness - schedule.reported_fairness) > 0.001:
        warnings.append(ScoringWarning(
            f"Fairness score mismatch: oracle={oracle_fairness:.4f}, "
            f"solver={schedule.reported_fairness:.4f}",
        ))

    return warnings
```

### 6. Testing the Oracle Itself

The oracle must be tested before it can validate anything:

```python
def test_oracle_rejects_known_invalid():
    """Feed the oracle a schedule with a known violation."""
    config = Config(min_gap=2)
    schedule = Schedule({
        date(2025, 1, 6): {"main": "Alice"},  # Monday
        date(2025, 1, 7): {"main": "Alice"},  # Tuesday — gap=1, violation!
    })
    result = validate_schedule(schedule, config, roster)
    assert not result.is_valid
    assert any("minimum_gap" in e.constraint for e in result.errors)

def test_oracle_accepts_known_valid():
    """Feed the oracle a hand-crafted valid schedule."""
    config = Config(min_gap=2)
    schedule = Schedule({
        date(2025, 1, 6): {"main": "Alice"},   # Monday
        date(2025, 1, 8): {"main": "Bob"},      # Wednesday
        date(2025, 1, 10): {"main": "Alice"},   # Friday — gap=4, valid
    })
    result = validate_schedule(schedule, config, roster)
    assert result.is_valid

def test_oracle_catches_each_constraint_type():
    """One test per constraint type with a minimal violation."""
    # ... one test per constraint ensuring the oracle detects it
```

### 7. Integration Patterns

**a. Post-solve verification in production:**
```python
result = scheduler.generate(config)
for variant in result.variants:
    validation = validate_schedule(variant, config, roster)
    if not validation.is_valid:
        log.error(f"Solver produced invalid schedule: {validation.errors}")
        raise ScheduleValidationError(validation.errors)
```

**b. Pytest fixture:**
```python
@pytest.fixture
def validated_schedule(config, roster):
    result = scheduler.generate(config)
    schedule = result.variants[0]
    validation = validate_schedule(schedule, config, roster)
    assert validation.is_valid, f"Schedule invalid: {validation.errors}"
    return schedule
```

**c. CI gate:**
```yaml
# In CI pipeline
- name: Validate generated schedules
  run: python -m pytest tests/oracle/ -v --tb=short
```

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Import solver code in the oracle module — the entire point is independence
- Use the solver's `constraint.is_violated()` method in the oracle — implement checks from scratch
- Flag soft constraint violations as errors — they are warnings/trade-offs
- Report fairness score differences < 0.001 — floating-point precision variance is expected

✅ **DO:**
- Enforce oracle independence via import checks (linter rule or CI check)
- Test the oracle with both known-valid AND known-invalid schedules
- Include the oracle in the CI pipeline as a post-solve verification step
- Document every constraint check's specification source (config spec, not solver code)

## Expected Output

1. **Oracle Module** — Complete `validate_schedule()` function with all layers
2. **Constraint Check Inventory** — One independent check per constraint type
3. **Fairness Verification** — Independent recomputation of all scoring metrics
4. **Oracle Self-Tests** — Tests that verify the oracle correctly accepts/rejects known schedules
5. **Integration Guide** — How to wire the oracle into production, tests, and CI

## Quality Checklist

- [ ] Oracle module has zero imports from the solver/engine package
- [ ] Every hard constraint has an independent check in the oracle
- [ ] Oracle is tested with at least one known-invalid schedule per constraint
- [ ] Oracle is tested with at least one known-valid schedule
- [ ] Fairness scores are independently recomputed and compared

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focuses on building an independent validation oracle
- **ST-02** (Structured Sequential Instructions) — Layered from structural to domain validation
- **RT-02** (Multi-Dimensional Analysis) — Covers structural, constraint, soft, fairness, and domain layers
- **DS-02** (Metric Specification) — Defines pass/fail criteria with tolerances
- **QA-02** (Adversarial Stress-Test) — Tests the oracle itself with known violations
- **RT-05** (Evidence-Based Reasoning) — Ties each check to the specification, not solver code
- **DT-01** (Hierarchical Task Breakdown) — Decomposes oracle into independently testable sub-validators

## Related Prompts

- `testing_constraint_logic_edge_cases.md` — Edge cases that the oracle should also catch
- `testing_nondeterministic_variant_validation.md` — Uses the oracle to validate all variants
- `algorithms_constraint_satisfaction_scheduling.md` — The solver being independently validated
- `algorithms_multi_criteria_schedule_optimization.md` — Scoring metrics the oracle verifies
