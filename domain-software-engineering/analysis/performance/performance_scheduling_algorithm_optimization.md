---
title: "Performance Optimization for Schedule Generation Algorithms"
category: code-analysis/performance
description: "Profile and optimize schedule generation performance including constraint evaluation hotspots, pruning strategies, caching, parallelization, and solver selection"
tags:
  - performance
  - optimization
  - scheduling
  - backtracking
  - profiling
  - constraint-satisfaction
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - DS-02  # Metric Specification
  - DS-03  # Tool and Methodology Suggestions
  - RT-05  # Evidence-Based Reasoning
  - DS-06  # Prioritization Guidance
  - RT-07  # Cascade Effect Analysis
difficulty: advanced
version: "1.0"
updated: 2026-03-04
related_prompts:
  - ../../algorithms/algorithms_constraint_satisfaction_scheduling.md
  - performance_bottleneck_identification.md
  - performance_code_optimization_suggestions.md
---

# Performance Optimization for Schedule Generation Algorithms

**Objective:** Profile and optimize the performance of a constraint-satisfaction-based schedule generator, identifying computation hotspots, implementing pruning strategies, and determining when to switch from pure Python backtracking to compiled solvers.

**When to Use:** Use this prompt when schedule generation takes too long — more than a few seconds for typical configurations, or when generation time scales poorly with roster size or schedule horizon length. Schedule generation with backtracking can be exponentially slow without proper optimization.

**Instructions:**

### 1. Performance Baseline

Establish benchmarks before optimizing:

| Configuration | Workers | Days | Constraints | Expected Time | Actual Time |
|--------------|---------|------|-------------|---------------|-------------|
| Minimal | 5 | 7 | gap=2 only | < 0.1s | ? |
| Typical | 10 | 30 | gap+weekly+conflict | < 2s | ? |
| Moderate | 15 | 60 | all constraints | < 10s | ? |
| Stress | 25 | 90 | all constraints, tight | < 30s | ? |
| Maximum | 50 | 90 | all constraints | < 60s | ? |

```python
import time

def benchmark_generation(config_path, iterations=5):
    config = load_config(config_path)
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        result = scheduler.generate(config)
        elapsed = time.perf_counter() - start
        times.append(elapsed)
    return {
        "median": sorted(times)[len(times)//2],
        "p95": sorted(times)[int(len(times)*0.95)],
        "max": max(times),
    }
```

**Key question:** Does generation time scale linearly, quadratically, or exponentially with roster size?

### 2. Profiling Constraint Evaluation

The #1 performance hotspot in backtracking schedulers:

```python
# Profile with cProfile
import cProfile
cProfile.run('scheduler.generate(config)', 'schedule_profile')

# Analyze with pstats
import pstats
p = pstats.Stats('schedule_profile')
p.sort_stats('cumulative').print_stats(20)

# Look for:
# - constraint.evaluate() taking > 50% of total time
# - eligibility checking called millions of times
# - deep recursion in backtracking
```

**Common hotspots in scheduling engines:**

| Hotspot | Why It's Slow | Fix |
|---------|-------------|-----|
| Constraint evaluation per assignment | Called O(workers × slots × constraints) | Cache eligibility; batch evaluate |
| Domain recomputation | Recalculating eligible workers from scratch | Incremental domain maintenance |
| Deep backtracking | Exploring doomed branches | Forward checking, arc consistency |
| Variant generation | Generating N variants sequentially | Parallelize or generate from perturbation |
| Fairness score recalculation | Recomputed from scratch after each assignment | Incremental counter update |

### 3. Pruning Strategies

Reduce the search space before exploring it:

```
Pruning Effectiveness (typical scheduling):

No pruning:          Search space ≈ W^S (workers^slots)
                     10 workers, 30 slots = 10^30 states

Forward checking:    Prunes ~60-80% of branches
                     After assigning day 1, remove violating options for days 2-3

Arc consistency:     Prunes ~80-95% of branches
                     Propagates constraints transitively

Domain-specific:     Additional ~20-50% on top of AC
  - Assign weekends first (most constrained days)
  - Assign qualified-only roles first
  - Skip already-assigned slots
```

**Constraint ordering for early pruning:**
1. Check cheapest constraints first (availability lookup = O(1))
2. Check most restrictive constraints next (weekly limit prunes many candidates)
3. Check expensive constraints last (conflict check = O(workers²))

### 4. Caching and Memoization

```python
# Cache eligibility checks
from functools import lru_cache

class EligibilityCache:
    """Cache worker eligibility for a given schedule state."""

    def __init__(self):
        self._cache = {}
        self._state_hash = None

    def is_eligible(self, worker, day, role, state):
        state_hash = hash(state)  # Must be hashable
        if state_hash != self._state_hash:
            self._cache.clear()
            self._state_hash = state_hash

        key = (worker, day, role)
        if key not in self._cache:
            self._cache[key] = self._evaluate(worker, day, role, state)
        return self._cache[key]
```

**What to cache:**
- Worker eligibility for a specific (day, role) — changes only when nearby assignments change
- Weekly counts — maintain incrementally, don't recount from scratch
- Constraint violations — cache per (worker, day) pair, invalidate on assignment

**What NOT to cache:**
- Full schedule states (too much memory)
- Results that change with every assignment (no cache benefit)

### 5. Parallelization Opportunities

```
Parallelizable Tasks:
├── Variant generation (independent schedules)
│   └── Each variant can be generated in its own thread/process
│
├── Scoring (after generation)
│   └── Score each variant independently
│
├── Export (after scoring)
│   └── Each format exported independently
│
NOT parallelizable:
├── Single-schedule backtracking (inherently sequential)
│   └── BUT: portfolio approach — run different heuristics in parallel, take first to finish
│
└── Constraint propagation (dependencies between constraints)
```

```python
from concurrent.futures import ProcessPoolExecutor

def generate_variants_parallel(config, num_variants=5):
    """Generate variants in parallel using different seeds."""
    with ProcessPoolExecutor(max_workers=min(num_variants, os.cpu_count())) as executor:
        futures = [
            executor.submit(generate_single, config, seed=i)
            for i in range(num_variants)
        ]
        return [f.result() for f in futures]
```

### 6. When to Switch Solvers

| Indicator | Stay with Python Backtracking | Switch to OR-Tools/CP-SAT |
|-----------|------------------------------|--------------------------|
| Roster size | ≤ 20 workers | > 20 workers |
| Schedule horizon | ≤ 60 days | > 60 days |
| Constraint density | Sparse (2-3 types) | Dense (5+ types, tight) |
| Generation time | < 10 seconds | > 30 seconds |
| Infeasibility rate | Low | High (many unsatisfiable configs) |

```python
# OR-Tools CP-SAT solver integration sketch
from ortools.sat.python import cp_model

def solve_with_cpsat(config, roster):
    model = cp_model.CpModel()

    # Variables: x[w][d][r] = 1 if worker w assigned to day d role r
    x = {}
    for w in roster.workers:
        for d in config.days:
            for r in config.roles:
                x[w, d, r] = model.NewBoolVar(f'x_{w}_{d}_{r}')

    # Constraints map directly from config
    # ... (each plugin constraint becomes a CP-SAT constraint)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 30
    status = solver.Solve(model)
```

### 7. Performance Regression Testing

```python
import pytest

@pytest.mark.benchmark
def test_generation_performance_typical(benchmark):
    """Generation time must stay under 2 seconds for typical config."""
    config = load_config("benchmarks/typical_10_30.yaml")
    result = benchmark(scheduler.generate, config)
    assert benchmark.stats["median"] < 2.0

@pytest.mark.benchmark
def test_generation_scales_linearly():
    """Doubling roster should at most 4x generation time."""
    time_10 = measure_generation(workers=10, days=30)
    time_20 = measure_generation(workers=20, days=30)
    assert time_20 < time_10 * 4  # Quadratic acceptable, exponential not
```

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Optimize before profiling — measure first, then fix the actual hotspot
- Recommend OR-Tools for every project — the integration cost is significant and only justified for large instances
- Flag Python as "too slow" without benchmarking — pure Python backtracking is fast enough for most scheduling needs (< 20 workers)
- Recommend parallelization for a single-schedule generation — backtracking is inherently sequential; parallelize at the variant level instead
- Cache everything — cache invalidation bugs are worse than the performance problem they solve

✅ **DO:**
- Establish baseline benchmarks before making any changes
- Profile with realistic configs, not toy examples
- Measure both median and worst-case (P95) generation times
- Track performance regressions in CI
- Consider the user's perception: 5 seconds with a progress bar feels faster than 2 seconds with a frozen UI

## Expected Output

1. **Baseline Benchmarks** — Table of generation times across configuration sizes
2. **Profile Analysis** — Top 5 hotspots with percentage of total time
3. **Pruning Assessment** — Current pruning effectiveness and recommended improvements
4. **Caching Opportunities** — What to cache, expected hit rate, invalidation strategy
5. **Parallelization Plan** — Which tasks to parallelize and expected speedup
6. **Solver Decision** — Whether to stay with backtracking or switch to CP-SAT, with rationale
7. **Performance Tests** — Benchmark tests for CI integration

## Quality Checklist

- [ ] Baseline benchmarks established for at least 3 configuration sizes
- [ ] Profiling data collected with realistic configurations
- [ ] Top hotspot identified with evidence
- [ ] At least one optimization recommendation with expected improvement
- [ ] Performance regression test proposed

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focuses on schedule generation performance
- **ST-02** (Structured Sequential Instructions) — Systematic from baseline to regression testing
- **DS-02** (Metric Specification) — Defines target times and scaling thresholds
- **DS-03** (Tool and Methodology Suggestions) — Recommends cProfile, OR-Tools, pytest-benchmark
- **RT-05** (Evidence-Based Reasoning) — Requires profiling data, not guesses
- **DS-06** (Prioritization Guidance) — Ranks optimizations by impact
- **RT-07** (Cascade Effect Analysis) — Traces how one slow component cascades through generation

## Related Prompts

- `algorithms_constraint_satisfaction_scheduling.md` — The algorithm being optimized
- `performance_bottleneck_identification.md` — General performance bottleneck identification
- `performance_code_optimization_suggestions.md` — General optimization suggestions
- `architecture_gui_background_computation.md` — How slow generation affects the GUI
