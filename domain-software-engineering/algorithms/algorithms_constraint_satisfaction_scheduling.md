---
title: "Constraint Satisfaction & Backtracking Audit for Scheduling Systems"
category: algorithms
description: "Audit and improve constraint-satisfaction-based scheduling engines by verifying model completeness, search correctness, reversible propagation, variable and value ordering, infeasibility handling, optimization behavior, testing coverage, and performance."
tags:
  - algorithms
  - constraint-satisfaction
  - backtracking
  - scheduling
  - optimization
  - csp
  - constraint-propagation
  - infeasibility-analysis
  - algorithm-audit
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DS-01  # Framework Application
  - DS-02  # Metric Specification
  - DS-03  # Tool and Methodology Suggestions
  - QA-01  # Chain-of-Verification
difficulty: advanced
version: "2.0"
updated: "2026-07-20"
related_prompts:
  - algorithms_data_structure_selection.md
  - algorithms_heap_priority_queue.md
  - algorithms_multi_criteria_schedule_optimization.md
  - testing_constraint_logic_edge_cases.md
  - performance_scheduling_algorithm_optimization.md
---

# Constraint Satisfaction & Backtracking Audit for Scheduling Systems

## Objective

Audit and improve a constraint-satisfaction-based scheduling engine for:

- **model correctness** — the implemented variables, domains, and constraints accurately represent the scheduling problem;
- **search completeness** — the engine does not incorrectly discard valid schedules;
- **state integrity** — assignments, counters, domains, caches, and derived state are fully restored after backtracking;
- **constraint propagation correctness** — pruning removes only values that cannot participate in a valid solution;
- **termination reliability** — satisfiable, unsatisfiable, interrupted, and budget-exhausted searches terminate with distinct outcomes;
- **optimization validity** — hard constraints remain inviolable while soft constraints are evaluated consistently;
- **diagnostic quality** — failures identify actionable bottlenecks or conflicting requirements;
- **performance** — the engine avoids unnecessary search without sacrificing correctness.

The audit must distinguish among:

1. **incorrect models**;
2. **incorrect search implementations**;
3. **correct but inefficient search**;
4. **genuinely infeasible scheduling instances**;
5. **search-budget exhaustion without proof of infeasibility**; and
6. **valid schedules that are feasible but suboptimal under the stated soft constraints**.

---

## When to Use

Use this prompt when building, reviewing, debugging, testing, or optimizing a scheduling system that assigns workers, resources, rooms, vehicles, instructors, machines, or other entities to dated or timed slots subject to constraints.

Applicable domains include:

- healthcare on-call scheduling;
- nurse and clinician staffing;
- retail shift scheduling;
- emergency-services rotations;
- manufacturing and machine scheduling;
- transportation and vehicle assignment;
- classroom, examination, and instructor scheduling;
- maintenance scheduling;
- volunteer rostering;
- field-service dispatch;
- sports officiating;
- project-resource allocation; and
- any scheduling problem modeled through constraint satisfaction, recursive backtracking, branch-and-bound, or related search methods.

Typical constraints include:

- availability;
- qualifications;
- minimum rest or spacing;
- maximum workload;
- role compatibility;
- assignment conflicts;
- paired or grouped assignment patterns;
- sequence rules;
- locked assignments;
- coverage requirements;
- fairness targets;
- preferences;
- weekend or holiday rotation;
- continuity requirements; and
- domain-specific safety rules.

---

## Role

Act as a senior algorithms engineer specializing in:

- constraint satisfaction problems;
- scheduling and rostering;
- recursive backtracking;
- branch-and-bound;
- forward checking;
- arc consistency;
- reversible state mutation;
- infeasibility diagnosis;
- combinatorial optimization;
- algorithm instrumentation;
- property-based testing; and
- performance analysis.

Review the actual implementation rather than evaluating only the intended algorithm.

Do not assume that function names, comments, documentation, or variable names accurately describe runtime behavior. Trace the relevant code paths and verify what the engine actually does.

---

## Input Contract

Analyze all supplied materials that are relevant to the scheduler, including any of the following:

### Required or strongly preferred inputs

- scheduling source code;
- constraint-checking functions;
- assignment and unassignment logic;
- recursive search or backtracking functions;
- domain-construction logic;
- scoring or objective functions;
- input schemas;
- representative roster data;
- unavailable-date data;
- qualification data;
- locked or pre-scheduled assignments;
- expected output examples;
- known failure cases;
- test files;
- logs;
- performance measurements; and
- previously generated schedules.

### Useful problem-definition details

- scheduling horizon;
- number of workers or resources;
- number and type of slots per day;
- role definitions;
- hard constraints;
- soft constraints;
- fairness rules;
- pattern constraints;
- expected solver behavior;
- whether one solution or multiple variants are required;
- acceptable runtime;
- memory limitations;
- target platform;
- available libraries; and
- whether deterministic output is required.

### When information is missing

Do not invent missing business rules.

Instead:

1. identify the missing information;
2. state the narrowest assumption necessary to continue;
3. label conclusions that depend on that assumption;
4. distinguish confirmed behavior from inferred behavior; and
5. continue the audit wherever the available evidence permits.

Do not stop the entire review merely because some optional configuration or domain context is unavailable.

---

## Audit Modes

Determine which mode the request requires.

### Mode A — Architecture and logic audit

Use when the user wants findings and recommendations without code changes.

### Mode B — Debugging audit

Use when the user reports incorrect schedules, missing solutions, hangs, constraint violations, or inconsistent output.

### Mode C — Performance audit

Use when the scheduler is believed to be correct but is too slow, memory-intensive, or unpredictable.

### Mode D — Implementation audit and repair

Use when the user wants specific code changes, patches, refactoring, or replacement algorithms.

### Mode E — Validation audit

Use when the user wants evidence that the scheduler is correct across satisfiable, unsatisfiable, and boundary cases.

If the requested mode is not explicit, perform a combined correctness-and-performance audit, with correctness taking priority.

---

# Core Audit Principles

## 1. Correctness Before Performance

Do not recommend performance optimizations until the following have been evaluated:

- hard-constraint completeness;
- domain correctness;
- assignment validity;
- propagation soundness;
- backtrack restoration;
- terminal-state validation; and
- infeasibility handling.

A fast scheduler that omits valid solutions or emits invalid schedules is not an improvement.

---

## 2. Separate Hard Constraints from Soft Constraints

Hard constraints determine whether a schedule is valid.

Soft constraints determine how desirable one valid schedule is relative to another.

A soft constraint must not accidentally become a hard constraint because:

- a score threshold rejects candidates;
- a heuristic excludes values instead of reordering them;
- a fairness preference removes workers from a domain;
- an optimization cutoff is applied incorrectly;
- a cached score is stale; or
- a tie-breaking rule prevents alternatives from being explored.

Likewise, a hard safety or legality constraint must not be treated as a penalty that the solver may violate.

---

## 3. Distinguish Pruning from Ordering

A heuristic may change the order in which variables or values are explored without changing the set of possible solutions.

A pruning rule removes possibilities from the search space.

Audit each mechanism according to its actual effect:

| Mechanism | Intended Effect | Completeness Risk |
|---|---|---:|
| Variable ordering | Chooses which unassigned slot to explore next | Low if every variable remains reachable |
| Value ordering | Chooses candidate order for a selected variable | Low if every domain value remains reachable |
| Forward checking | Removes values that immediately conflict | Moderate if restoration or logic is incorrect |
| Arc consistency | Removes unsupported domain values | Moderate if constraint semantics are incorrect |
| Branch-and-bound | Removes branches that cannot beat the incumbent | High if bounds are invalid |
| Hard filtering | Removes values that violate required constraints | High if the constraint is misimplemented |
| Beam search | Keeps only a limited number of branches | Intentionally incomplete |
| Random sampling | Explores only selected alternatives | Intentionally incomplete |
| Early acceptance | Stops after an acceptable solution | Complete only for first-solution search, not optimization |
| Timeout or node cap | Stops search after a budget is exhausted | Does not prove infeasibility |

---

## 4. Use Evidence-Based Findings

Every material finding should include:

- the affected code path, function, or component;
- the triggering condition;
- the expected behavior;
- the observed or logically demonstrated behavior;
- the consequence;
- the confidence level;
- a reproduction or test method; and
- a recommended correction.

Do not label a concern as a confirmed defect when it has not been demonstrated.

Use these evidence labels:

- **Confirmed defect** — directly demonstrated by code behavior, test failure, invalid output, or reproducible trace;
- **Probable defect** — strongly supported by code analysis but not yet executed;
- **Design risk** — currently valid behavior that is fragile or likely to fail under expansion;
- **Performance opportunity** — behavior appears correct but can likely be improved;
- **Insufficient evidence** — additional code, data, or runtime observation is needed.

---

## 5. Do Not Expose Hidden Chain-of-Thought

Perform detailed internal analysis, but report only:

- concise reasoning summaries;
- code-path evidence;
- state-transition descriptions;
- test results;
- calculations;
- decision tables; and
- actionable conclusions.

Do not provide private hidden reasoning or an unfiltered internal thought process.

---

# Phase 1 — Reconstruct the Scheduling Problem

Before judging the implementation, reconstruct the scheduling problem as it exists in code.

## 1.1 Identify the decision variables

Determine what one search variable represents.

Common forms include:

- one variable per `(date, role)` slot;
- one variable per shift;
- one variable per worker-day pair;
- one variable per weekend pattern;
- one variable per coverage block;
- one variable per task-resource pair; or
- a hybrid model containing both individual and grouped assignments.

Example:

```text
Variables:
├── V_{2026-08-03, Main}
├── V_{2026-08-03, Backup}
├── V_{2026-08-04, Main}
├── V_{2026-08-04, Backup}
└── ...
```

For each variable, document:

- unique identifier;
- date or time interval;
- role;
- required cardinality;
- assignment type;
- whether it can be pre-assigned;
- whether it belongs to a larger pattern; and
- which other variables constrain it.

### Audit questions

- Does each required schedule slot have a corresponding variable?
- Are any variables duplicated?
- Are optional and required slots distinguished?
- Are multi-day patterns represented explicitly or reconstructed through several independent variables?
- Can variable identity change during search?
- Are date, shift, and role boundaries represented consistently?
- Are locked assignments included in the model before search begins?

---

## 1.2 Identify the domains

For each variable, determine the complete initial domain.

Example:

```text
D(V_{Monday, Main}) =
    all workers
    minus unavailable workers
    minus unqualified workers
    minus workers prohibited from the role
    minus values ruled out by locked assignments
```

Document whether the domain is:

- computed once;
- recomputed dynamically;
- copied per recursion level;
- reduced through propagation;
- represented as a set, list, bitset, mask, generator, or query;
- ordered by a heuristic; and
- restored after backtracking.

### Audit questions

- Does the initial domain contain every legally eligible value?
- Does it exclude every value that is already impossible?
- Are availability boundaries inclusive or exclusive as intended?
- Are date and time-zone conversions consistent?
- Are qualifications checked for the correct effective date?
- Are locked assignments reflected in neighboring domains?
- Can a candidate be removed because of a soft preference?
- Can stale domain data survive a configuration change?
- Are domains copied deeply enough to prevent aliasing?

---

## 1.3 Enumerate all hard constraints

Construct a hard-constraint inventory.

For each constraint, record:

| Field | Required Information |
|---|---|
| Constraint name | Stable descriptive name |
| Business rule | Plain-language requirement |
| Formal rule | Predicate, equation, or logical expression |
| Scope | Variables or assignments affected |
| Evaluation timing | Domain build, assignment, propagation, terminal validation |
| State dependencies | Counters, history, locked assignments, neighboring slots |
| Symmetry | Directional or bidirectional |
| Boundary semantics | Inclusive/exclusive date and count behavior |
| Failure behavior | Reject value, prune domain, backtrack, abort |
| Tests | Positive, negative, and boundary cases |

Possible hard constraints include:

- availability;
- role qualification;
- no duplicate worker in simultaneous roles;
- minimum assignment gap;
- mandatory rest period;
- maximum assignments per day;
- maximum assignments per week;
- maximum consecutive work periods;
- no overlapping shifts;
- locked assignment preservation;
- conflict-pair restrictions;
- required worker pairing;
- prohibited worker pairing;
- weekend block consistency;
- holiday pattern consistency;
- shift-sequence rules;
- certification validity;
- age, license, or legal requirements;
- minimum staffing coverage;
- seniority or supervision coverage;
- mutually exclusive assignments;
- continuity requirements;
- location-travel feasibility;
- skill-mix requirements; and
- domain-specific safety rules.

### Constraint completeness check

Compare constraints across:

1. written requirements;
2. configuration files;
3. data-validation rules;
4. domain-construction logic;
5. assignment checks;
6. propagation logic;
7. terminal validation;
8. score calculations;
9. test cases; and
10. generated schedule outputs.

Flag any rule that appears in one layer but not the others.

---

## 1.4 Enumerate all soft constraints

Construct a separate soft-constraint inventory.

Possible soft constraints include:

- equal total assignment counts;
- equal first-role and second-role counts;
- weekday/weekend parity;
- holiday rotation fairness;
- preferred days;
- disliked days;
- worker pairing preferences;
- continuity;
- distance between assignments;
- distance between weekend assignments;
- avoidance of consecutive assignments;
- workload smoothing;
- historical fairness;
- preference satisfaction;
- schedule stability;
- minimal deviation from a prior schedule;
- minimal use of PRN or overtime staff; and
- weighted organizational priorities.

For each soft constraint, document:

- score direction;
- weight;
- scale;
- normalization;
- tie-breaking behavior;
- whether the score is incremental or calculated at completion;
- whether partial-state scores are admissible;
- whether the score can reject a branch;
- whether the score depends on historical data; and
- whether competing objectives are combined or lexicographically ordered.

---

## 1.5 Produce the CSP model map

Represent the reconstructed problem using CSP terminology.

```text
Constraint Satisfaction Problem:
├── Variables
│   ├── One variable per schedule slot or assignment block
│   └── Grouped variables for inseparable patterns where applicable
│
├── Domains
│   ├── Initially eligible workers or resources
│   ├── Reduced by hard eligibility rules
│   └── Dynamically reduced by propagation
│
├── Hard Constraints
│   ├── Unary constraints
│   │   ├── Availability
│   │   └── Qualification
│   ├── Binary constraints
│   │   ├── Same-day exclusion
│   │   ├── Spacing
│   │   └── Pair conflicts
│   ├── Global constraints
│   │   ├── Weekly assignment limits
│   │   ├── Coverage
│   │   └── Fairness bounds when truly mandatory
│   └── Pattern constraints
│       ├── Weekend rotations
│       └── Multi-day sequence rules
│
└── Soft Constraints
    ├── Fairness
    ├── Preference satisfaction
    ├── Assignment spacing quality
    ├── Weekend/weekday balance
    └── Historical rotation quality
```

Rate model completeness as:

- **Complete**;
- **Mostly complete with minor omissions**;
- **Materially incomplete**;
- **Internally inconsistent**; or
- **Unable to determine from supplied evidence**.

---

# Phase 2 — Trace the Search Lifecycle

Map the actual search process from initialization to termination.

## 2.1 Search lifecycle map

Document the sequence:

```text
Input validation
    ↓
Problem normalization
    ↓
Locked-assignment insertion
    ↓
Initial domain construction
    ↓
Initial consistency check
    ↓
Variable selection
    ↓
Value ordering
    ↓
Tentative assignment
    ↓
State update
    ↓
Constraint checking
    ↓
Propagation
    ↓
Dead-end detection
    ↓
Recursive descent
    ↓
Solution validation
    ↓
Score evaluation
    ↓
Backtrack or accept
    ↓
Termination classification
```

Identify where each of the following occurs:

- assignment insertion;
- assignment removal;
- counter increment;
- counter decrement;
- domain pruning;
- domain restoration;
- cache invalidation;
- score update;
- score rollback;
- incumbent update;
- solution copy;
- failure recording;
- timeout checking; and
- termination signaling.

---

## 2.2 Reference search structure

Compare the implementation against a logically correct search structure.

```python
def search(state):
    if state.is_complete():
        if not state.validate_complete_schedule():
            return SearchResult.invalid_terminal_state()

        return SearchResult.solution(
            schedule=state.copy_schedule(),
            score=state.evaluate_complete_score(),
        )

    variable = select_unassigned_variable(state)

    if variable is None:
        return SearchResult.dead_end("No selectable variable")

    ordered_values = order_values(state, variable)

    if not ordered_values:
        return SearchResult.dead_end(
            reason="Selected variable has an empty domain",
            variable=variable,
        )

    for value in ordered_values:
        marker = state.create_restore_marker()

        try:
            if not state.is_assignment_consistent(variable, value):
                continue

            state.assign(variable, value)

            propagation_result = propagate(state, variable, value)

            if propagation_result.consistent:
                result = search(state)

                if result.is_solution:
                    return result

        finally:
            state.restore(marker)

    return SearchResult.dead_end(
        reason="All values exhausted",
        variable=variable,
    )
```

The implementation does not need to follow this exact structure. It must, however, preserve the same correctness guarantees.

---

## 2.3 Audit recursive control flow

Check for:

- missing base cases;
- base cases that accept incomplete schedules;
- base cases that fail to validate all hard constraints;
- recursion that does not advance the state;
- loops that repeatedly select the same variable;
- branches that return before restoration;
- branches that skip viable values;
- exceptions that bypass cleanup;
- mutable default arguments;
- global state shared across attempts;
- stale candidate iterators;
- generators invalidated by mutation;
- incorrect success propagation;
- incorrect failure propagation;
- overwritten solution objects;
- reference aliasing between working state and returned solution; and
- recursion-depth limitations.

---

# Phase 3 — Audit Variable Ordering

Evaluate how the next variable is selected.

## 3.1 Common variable-ordering strategies

| Heuristic | Description | Scheduling Benefit | Primary Risk |
|---|---|---|---|
| Sequential order | Assign variables in calendar or input order | Simple and deterministic | May defer hard decisions until deep in search |
| MRV | Select the variable with the fewest legal values | Detects likely dead ends early | Domain counts must be current |
| Degree heuristic | Select the variable constraining the most unassigned variables | Prioritizes structurally important slots | Requires accurate constraint graph |
| MRV + degree | Use MRV, then degree as a tie-breaker | Strong general-purpose CSP strategy | More selection overhead |
| Special-period first | Assign weekends, holidays, or rare roles first | Protects scarce coverage periods | Can be incomplete if special handling fixes choices prematurely |
| Pattern-first | Assign a multi-day block as one decision | Avoids incompatible partial patterns | Requires correct grouped-domain construction |
| Dynamic impact | Select the variable expected to cause the most pruning | Can reduce search dramatically | Expensive and sensitive to estimation quality |
| Randomized order | Randomly select among tied variables | Produces diverse variants | Reproducibility requires seeded randomness |

## 3.2 Audit questions

- Are variables assigned sequentially or dynamically?
- Are pre-assigned variables skipped correctly?
- Is the selected variable always unassigned?
- Does the selector ever return `None` while variables remain?
- Are domain sizes current after propagation?
- Are empty-domain variables detected before recursion?
- Are holidays, weekends, rare qualifications, or pattern-constrained slots prioritized?
- Does the variable heuristic only reorder search, or does it accidentally exclude variables?
- Are tie-breakers deterministic?
- Is seeded randomness available when reproducibility matters?
- Is heuristic overhead greater than its search reduction for the problem size?

## 3.3 Evaluation requirement

Do not recommend MRV, degree ordering, or pattern-first assignment merely because they are standard techniques.

Compare at least:

- current ordering;
- one plausible alternative; and
- the effect on nodes, backtracks, runtime, and solution quality.

---

# Phase 4 — Audit Value Ordering

Evaluate how candidate workers or resources are ordered for a selected variable.

## 4.1 Common value-ordering strategies

| Heuristic | Description | Scheduling Benefit |
|---|---|---|
| Fixed roster order | Uses input or alphabetical order | Deterministic and simple |
| Least constraining value | Selects the value that removes the fewest future options | Preserves flexibility |
| Most remaining availability | Prefers workers with more future eligible slots | Useful when future coverage is scarce |
| Scarcity protection | Avoids consuming workers needed for rare roles or dates | Protects specialized capacity |
| Fairness-first | Prefers workers with fewer assignments | Improves balance |
| Longest-since-assigned | Prefers workers with the largest assignment gap | Supports rotation fairness |
| Lowest incremental penalty | Selects value with the smallest soft-cost increase | Supports optimization |
| Randomized tie-break | Randomizes equivalent candidates | Produces schedule variants |

## 4.2 Audit questions

- Does candidate ordering include every value remaining in the domain?
- Are candidates sorted or filtered?
- Can a fairness heuristic accidentally remove a valid candidate?
- Are counts used by the ordering logic current?
- Are future availability estimates accurate?
- Does least-constraining-value analysis account for all affected neighbors?
- Are specialized workers protected from unnecessary use?
- Can deterministic roster order create systematic bias?
- Does randomized ordering use an explicit seed?
- Does value-order computation mutate the state?
- Does value ordering become stale after propagation?

## 4.3 Fairness caution

Fairness-based ordering is generally safe when it changes only candidate order.

It becomes completeness-threatening when the engine:

- considers only workers below a threshold;
- excludes workers who already exceed an average;
- refuses a feasible assignment because it worsens parity;
- uses a soft fairness cap as an absolute limit; or
- prunes a branch based on a non-admissible partial fairness score.

---

# Phase 5 — Audit Constraint Propagation

Determine whether the engine reduces future domains after each assignment.

## 5.1 Propagation strategies

```text
Propagation Strategies:
├── Full or generalized arc consistency
│   ├── Repeatedly removes unsupported values
│   ├── Can detect deep inconsistencies early
│   └── Has higher propagation cost
│
├── AC-3 for binary constraints
│   ├── Revises connected variable domains
│   ├── Re-enqueues affected arcs
│   └── Worst-case cost commonly expressed as O(ed³)
│
├── Forward checking
│   ├── Prunes direct future conflicts after an assignment
│   ├── Detects immediate domain wipeouts
│   └── Usually cheaper than full arc consistency
│
├── Scheduling-specific propagation
│   ├── Removes same-worker simultaneous assignments
│   ├── Removes assignments inside required rest or gap windows
│   ├── Enforces weekly or period capacity
│   ├── Propagates grouped patterns
│   └── Updates qualification and coverage implications
│
└── No proactive propagation
    ├── Checks constraints only when values are attempted
    ├── Can remain correct
    └── Often produces a much larger search tree
```

Complexity statements must be treated as theoretical guidance, not measured runtime guarantees.

---

## 5.2 Scheduling-specific propagation examples

After assigning Worker A to Monday Main:

- remove Worker A from Monday Backup if simultaneous dual-role assignment is prohibited;
- remove Worker A from conflicting overlapping shifts;
- remove Worker A from dates inside the minimum-gap window;
- update Worker A’s weekly count;
- remove Worker A from remaining slots in the week if a hard maximum is reached;
- update any minimum or maximum consecutive-day state;
- update grouped weekend or holiday pattern requirements;
- update pair-conflict implications;
- update required skill-mix coverage;
- update future domains that depend on location or travel time; and
- detect any domain that becomes empty.

Example:

```python
def propagate_assignment(state, variable, worker, trail):
    for neighbor in state.constraint_graph[variable]:
        if state.is_assigned(neighbor):
            continue

        for candidate in list(state.domains[neighbor]):
            if not state.has_support(
                variable=variable,
                value=worker,
                neighbor=neighbor,
                neighbor_value=candidate,
            ):
                trail.remove_domain_value(
                    state=state,
                    variable=neighbor,
                    value=candidate,
                )

                if not state.domains[neighbor]:
                    return PropagationResult(
                        consistent=False,
                        failed_variable=neighbor,
                        reason="Domain wipeout",
                    )

    return PropagationResult(consistent=True)
```

---

## 5.3 Propagation soundness

Propagation is **sound** only if every removed value is impossible in every completion of the current partial assignment.

Flag unsound pruning when a value is removed because it:

- is merely less fair;
- creates a temporarily unequal count;
- is not the preferred candidate;
- has a worse but still acceptable score;
- conflicts only with an assignment that may later be undone;
- violates a rule under an incorrect date boundary;
- appears incompatible because of stale state;
- lacks support because the support search is incomplete;
- is excluded by an invalid lower bound; or
- is removed from an aliased domain shared by another search branch.

## 5.4 Propagation completeness

Propagation does not need to discover every implied inconsistency to remain correct.

Distinguish:

- **sound but weak propagation** — correct, but may leave avoidable search;
- **sound and strong propagation** — correct and removes many impossible values;
- **unsound propagation** — may eliminate valid schedules;
- **incomplete restoration** — pruning may leak across branches.

## 5.5 Audit questions

- What event triggers propagation?
- Which variables are considered neighbors?
- Is the constraint graph complete?
- Are directional constraints propagated in the correct direction?
- Are binary and global constraints treated appropriately?
- Is propagation repeated until stable when required?
- Are empty domains detected immediately?
- Are assigned variables protected from inappropriate pruning?
- Are removed values recorded for restoration?
- Are transitive implications handled when the selected propagation method requires them?
- Can propagation mutate shared data outside the current search state?
- Is the propagation result distinguished from “no values were removed”?
- Does a return value such as `False` mean inconsistency, no change, or failure?

Pay particular attention to ambiguous boolean return values.

---

# Phase 6 — Audit State Mutation and Backtrack Restoration

State restoration is a critical correctness boundary.

## 6.1 State components that may require restoration

Do not audit domains alone.

Inventory every mutable search component:

- current assignments;
- unassigned-variable collection;
- domains;
- worker assignment counts;
- role-specific counts;
- weekday counts;
- weekend counts;
- weekly totals;
- monthly totals;
- consecutive-day counters;
- minimum-gap indexes;
- assignment history;
- pattern state;
- pair-conflict state;
- qualification caches;
- coverage counters;
- objective score;
- lower-bound estimates;
- incumbent metadata;
- candidate-order caches;
- constraint-check caches;
- failure explanations;
- randomized state, when branch reproducibility depends on it;
- temporary reservations;
- visited-state sets; and
- memoization tables whose validity depends on mutable state.

---

## 6.2 Snapshot-based restoration

```python
def try_assignment_with_snapshot(state, variable, value):
    snapshot = state.snapshot()

    try:
        state.assign(variable, value)

        result = state.propagate(variable, value)

        if not result.consistent:
            return False

        return True

    finally:
        if not state.branch_committed:
            state.restore(snapshot)
```

### Advantages

- conceptually simple;
- easier to verify;
- low risk of omitted restoration fields.

### Risks

- expensive deep copies;
- accidental shallow copies;
- shared nested objects;
- snapshot cost may dominate runtime;
- external or global state may remain outside the snapshot.

---

## 6.3 Trail or undo-log restoration

```python
def search_branch(state, variable, value):
    marker = state.trail.mark()

    try:
        state.assign(variable, value, trail=state.trail)

        propagation = propagate(
            state=state,
            variable=variable,
            value=value,
            trail=state.trail,
        )

        if not propagation.consistent:
            return False

        return search(state)

    finally:
        state.trail.rollback_to(marker, state)
```

### Advantages

- avoids copying the entire state;
- often faster for large problems;
- restoration cost is proportional to branch mutations.

### Risks

- every mutation must be recorded;
- repeated removals must be handled safely;
- counters and caches may be omitted;
- restoration order may matter;
- exceptions may bypass rollback if cleanup is not guaranteed;
- direct mutation outside trail-aware methods can corrupt sibling branches.

An undo log is not inherently incorrect. It is correct when all mutations are captured and rollback is verified.

---

## 6.4 Recompute-on-backtrack restoration

Some systems rebuild derived state from the remaining assignments rather than explicitly undoing every mutation.

This can be correct when:

- assignments are restored reliably;
- derived state is deterministic;
- rebuild logic is complete;
- rebuild cost is acceptable; and
- no stale cache survives the rebuild.

Audit the rebuild path with the same rigor as an undo log.

---

## 6.5 Restoration invariant

For each attempted branch:

```text
state_before
    ↓ assign
state_after_assignment
    ↓ propagate
state_after_propagation
    ↓ recurse or fail
state_before restored exactly
```

The required invariant is:

```python
canonicalize(state_after_backtrack) == canonicalize(state_before_branch)
```

Canonical comparison should include all semantically relevant state.

Object identity does not need to match unless identity itself affects behavior.

---

## 6.6 Required restoration test

Implement or specify a test equivalent to:

```python
def test_state_restores_exactly_after_failed_branch():
    state = build_known_state()
    before = state.canonical_snapshot()

    variable = select_test_variable(state)
    value = select_value_that_causes_failure(state, variable)

    marker = state.create_restore_marker()

    try:
        state.assign(variable, value)
        propagate(state, variable, value)
    finally:
        state.restore(marker)

    after = state.canonical_snapshot()

    assert after == before
```

Repeat the test for:

- immediate constraint rejection;
- propagation failure;
- deep recursive failure;
- timeout or cancellation;
- raised exception;
- successful solution return;
- branch-and-bound pruning; and
- repeated attempts of the same branch.

---

## 6.7 Restoration audit questions

- Is restoration guaranteed through `finally` or an equivalent mechanism?
- Can an early `return` skip unassignment?
- Can `continue` skip restoration?
- Can an exception escape before rollback?
- Are counters decremented exactly once?
- Are domain values restored exactly once?
- Are duplicates introduced during restoration?
- Are lists restored in a deterministic order?
- Are sets, heaps, or priority queues restored correctly?
- Are cached domain sizes invalidated?
- Are score deltas reversed?
- Is the incumbent solution copied rather than referenced?
- Are parent and child states aliased?
- Can a successful branch leave mutations when the engine later requests additional solutions?
- Is restoration still correct after nested propagation?

---

# Phase 7 — Audit Constraint Checking

## 7.1 Check timing

Determine where each hard constraint is enforced:

- initial validation;
- domain construction;
- pre-assignment check;
- post-assignment check;
- propagation;
- recursive entry;
- terminal validation; or
- output validation.

A constraint may be checked in more than one place intentionally.

Do not automatically classify repeated checks as redundant. Determine whether they serve different correctness boundaries.

## 7.2 Partial-state versus complete-state constraints

Classify each constraint as:

- evaluable on a single candidate;
- evaluable on a partial schedule;
- evaluable only after a period is complete;
- evaluable only on the final schedule; or
- incrementally maintainable through derived state.

Examples:

| Constraint | Earliest Reliable Evaluation |
|---|---|
| Worker unavailable on date | Before assignment |
| Same worker in two simultaneous roles | Before assignment |
| Minimum gap | Before assignment using assignment history |
| Weekly maximum | Before assignment or immediately afterward |
| Exact weekly minimum | At period boundary or with feasibility bounds |
| Overall fairness | Usually partial scoring plus final validation |
| Every worker receives one weekend before repeats | Requires cycle state or global sequence logic |
| Complete multi-day pattern | During grouped assignment or after all pattern variables are assigned |

## 7.3 Boundary audits

Explicitly test:

- first day of the scheduling horizon;
- last day of the scheduling horizon;
- week boundaries;
- month boundaries;
- year boundaries;
- daylight-saving transitions when time-based shifts are used;
- inclusive versus exclusive minimum-gap calculations;
- overnight shifts;
- zero-length or missing horizons;
- one-worker rosters;
- one-slot schedules;
- empty qualification groups;
- workers added or removed mid-horizon;
- qualifications expiring mid-horizon; and
- locked assignments outside or partly overlapping the horizon.

---

# Phase 8 — Audit Termination and Search Outcomes

The engine must represent search outcomes accurately.

## 8.1 Required outcome distinctions

At minimum, distinguish:

1. **Solution found**
2. **Optimal solution proven**, when optimization and proof are supported
3. **Feasible solution found, optimality not proven**
4. **No solution exists**, proven by exhaustive complete search or a sound infeasibility method
5. **Search budget exhausted**
6. **Timeout**
7. **Cancelled**
8. **Invalid input**
9. **Internal error**
10. **Partial schedule only**, when explicitly supported

Do not report “no solution” when the actual result is:

- timeout;
- maximum node count reached;
- recursion limit reached;
- random attempts exhausted;
- beam width exhausted;
- restart count exhausted;
- heuristic candidate list exhausted;
- optimization threshold not reached; or
- an exception was swallowed.

---

## 8.2 Termination audit questions

- Is there a complete base case?
- Is there a dead-end base case?
- Does every recursive branch either progress or terminate?
- Can the same state be revisited indefinitely?
- Are cyclic dependencies possible in propagation?
- Does AC-3 or another queue-based propagator terminate when no domains change?
- Are repeated queue entries bounded or deduplicated?
- Is there an iteration limit?
- Is the iteration limit diagnostic rather than silently treated as infeasibility?
- Is recursion depth safe for the maximum horizon?
- Is iterative search preferable on the target platform?
- Are cancellation and timeout checks placed frequently enough?
- Is a complete returned schedule independently validated before acceptance?

---

# Phase 9 — Audit Infeasibility Handling

## 9.1 Initial feasibility checks

Before deep search, identify inexpensive necessary-condition checks.

Examples:

### Coverage capacity

```text
Total required assignments
≤
Total maximum eligible assignment capacity
```

### Per-role capacity

```text
Required assignments for role R
≤
Total eligible capacity for role R
```

### Date-specific coverage

```text
Number of required slots on date D
≤
Number of mutually compatible eligible workers on date D
```

### Qualification capacity

```text
Required specialized slots
≤
Available qualified-worker capacity
```

### Period capacity

```text
Required assignments in week W
≤
Sum of eligible workers' remaining weekly capacity
```

### Pattern feasibility

```text
Required multi-day block
must have at least one worker combination eligible for every date and role in the block
```

Necessary-condition checks may prove infeasibility when violated, but passing them does not prove feasibility.

---

## 9.2 Common infeasibility scenarios

Test at least the following:

1. More required slots than total worker capacity
2. A required slot with an empty initial domain
3. Two simultaneous roles with only one eligible worker
4. Two mutually conflicting workers as the only qualified workers for paired roles
5. Minimum-gap requirements that eliminate all coverage
6. Weekly limits that make the horizon impossible to cover
7. Locked assignments that violate a hard constraint
8. Locked assignments that consume all feasible capacity for another required slot
9. A required multi-day pattern with no eligible worker pair
10. Every worker unavailable for a required date
11. Qualification expiration that removes all eligible workers mid-horizon
12. Mandatory fairness bounds that are mathematically impossible
13. Maximum-consecutive-day constraints that conflict with coverage
14. Geographic travel times that make consecutive assignments impossible
15. A worker conflict graph that prevents required simultaneous coverage
16. A schedule that is feasible only if a soft preference is violated

---

## 9.3 Infeasibility explanation

When possible, produce an actionable explanation rather than only returning `False`.

Possible diagnostic techniques include:

- first domain wipeout;
- most frequently failing constraint;
- deepest repeated conflict;
- minimal conflicting subset approximation;
- deletion filtering;
- constraint relaxation testing;
- assumption literals;
- unsatisfiable cores when supported by the solver;
- conflict-directed backjumping;
- nogood recording;
- required-capacity deficit calculation; and
- counterfactual analysis.

Example:

```text
No feasible schedule was found because:

- Saturday Main requires certification X.
- Only Alice and Bob hold certification X.
- Alice is unavailable Saturday.
- Bob is locked to Saturday Backup.
- The same worker cannot hold Main and Backup on the same date.

Conflicting requirements:
1. Saturday Main coverage
2. Saturday Backup locked to Bob
3. Same-day dual-role prohibition
4. Alice unavailable
```

Do not claim that a reported conflict set is minimal unless minimality was actually established.

---

## 9.4 Constraint-relaxation diagnostics

For diagnosis only, optionally test controlled relaxations such as:

- increase one weekly limit;
- reduce minimum gap by one day;
- remove one locked assignment;
- permit one preference violation;
- allow one additional qualified worker;
- separate a grouped weekend pattern;
- increase search budget; or
- disable one hard constraint at a time.

Clearly label relaxation results as diagnostic. Do not present a relaxed schedule as valid under the original rules.

---

# Phase 10 — Audit Soft Constraints and Optimization

## 10.1 Objective definition

Document the exact objective.

Examples:

### Weighted sum

```text
Total score =
    w1 × fairness_penalty
  + w2 × preference_penalty
  + w3 × weekend_imbalance
  + w4 × spacing_penalty
```

### Lexicographic objective

```text
1. Minimize hard-rule relaxations
2. Minimize uncovered required slots
3. Minimize maximum workload imbalance
4. Minimize total preference violations
5. Maximize assignment spacing
```

### Minimax fairness

```text
Minimize:
max_assignment_count - min_assignment_count
```

### Variance-based fairness

```text
Minimize:
Σ(worker_count - target_count)²
```

State whether lower or higher scores are better.

---

## 10.2 Audit objective consistency

Verify:

- all score components use compatible direction;
- weights reflect actual priority;
- large-scale components do not unintentionally dominate;
- the score is deterministic;
- partial scores are calculated correctly;
- incremental score updates match full recomputation;
- rollback restores the score;
- the final score is independently recomputed;
- locked assignments are treated consistently;
- historical counts are included exactly once;
- role-specific fairness is not hidden by total-count fairness;
- weekend fairness is not hidden by overall parity;
- tie-breaking is explicit; and
- impossible perfection does not cause endless search.

---

## 10.3 Branch-and-bound audit

When branch-and-bound is used, verify:

- the incumbent score is valid;
- the lower or upper bound is mathematically sound;
- the bound is optimistic in the required direction;
- pruning uses the correct inequality;
- equal-score branches are retained when alternative variants are needed;
- stale bounds are not reused after state changes;
- negative penalties or rewards do not invalidate assumptions;
- unassigned variables are accounted for correctly;
- the incumbent schedule is copied;
- proof of optimality is reported only after the search space is validly exhausted.

An invalid bound can make the algorithm fast but incomplete.

---

## 10.4 Feasibility versus optimization

Determine which behavior is intended:

- stop at the first feasible schedule;
- find several feasible variants;
- improve until a time limit;
- prove optimality;
- find a schedule below a target penalty;
- enumerate all schedules;
- enumerate all schedules up to symmetry;
- produce diverse near-optimal schedules.

Do not criticize first-solution termination when only one feasible schedule is required.

Do not call the first feasible schedule “optimal” unless optimization has been performed and proven.

---

# Phase 11 — Build the Verification Test Suite

The audit must include both satisfiable and unsatisfiable cases.

## 11.1 Unit tests for individual constraints

For every hard constraint, include:

- one clearly valid case;
- one clearly invalid case;
- one exact-boundary case;
- one case just inside the boundary;
- one case just outside the boundary; and
- one interaction case involving another constraint.

Example minimum-gap tests:

```text
Given min_gap = 2 full intervening days:

Assignment on Monday and Tuesday → invalid
Assignment on Monday and Wednesday → interpretation-dependent; verify specification
Assignment on Monday and Thursday → valid under a two-intervening-day rule
```

Do not assume the meaning of `min_gap`. Define whether it means:

- difference in calendar dates;
- number of unassigned intervening dates;
- elapsed hours;
- full rest periods; or
- excluded dates before and after an assignment.

---

## 11.2 State-restoration tests

Test:

- assignment followed by direct rejection;
- assignment followed by one domain removal;
- assignment followed by multiple domain removals;
- nested recursive failure;
- success followed by enumeration of another solution;
- timeout during propagation;
- exception during scoring;
- repeated assignment and rollback;
- restoration after branch-and-bound pruning; and
- restoration after grouped pattern assignment.

---

## 11.3 Differential tests

For small instances, compare the scheduler against a brute-force reference implementation.

```python
def brute_force_solutions(problem):
    for complete_assignment in enumerate_all_assignments(problem):
        if all_hard_constraints_hold(problem, complete_assignment):
            yield complete_assignment
```

Compare:

- whether at least one solution exists;
- the exact solution set when small enough;
- optimal objective value;
- number of feasible schedules;
- hard-constraint validity; and
- whether the audited engine omits valid solutions.

Differential testing is one of the strongest methods for detecting incomplete pruning or restoration defects.

---

## 11.4 Property-based tests

Generate many small randomized scheduling instances and verify invariants such as:

- every returned schedule satisfies every hard constraint;
- no returned assignment uses a value outside the original legal domain;
- locked assignments are preserved;
- search state is unchanged after a failed branch;
- repeated runs with the same seed are identical;
- adding an unavailable date never creates new assignments for that worker on that date;
- reducing a hard capacity limit cannot create new feasible schedules;
- removing a hard constraint cannot reduce the feasible solution set;
- adding a qualified worker cannot make a previously feasible instance infeasible;
- full score recomputation equals incremental scoring;
- disabling propagation does not change feasibility on small instances;
- alternate variable ordering does not change the feasible solution set; and
- alternate value ordering does not change the feasible solution set.

---

## 11.5 Metamorphic tests

Apply controlled transformations with predictable effects.

Examples:

- rename workers without changing attributes → equivalent feasibility and score;
- reorder roster input → equivalent feasibility unless tie-breaking intentionally changes the chosen schedule;
- reorder unavailable dates → identical result;
- duplicate a soft preference with zero weight → no effect;
- add an unconstrained unused worker → existing schedules remain feasible;
- shift all dates equally while preserving weekday relationships → equivalent structure when no absolute-date rules apply;
- convert equivalent date formats → identical normalized model;
- change random seed → feasibility remains unchanged even if the selected schedule changes.

---

## 11.6 Unsatisfiable-instance tests

At least one unsatisfiable configuration is required.

Prefer several categories:

- initial empty domain;
- global capacity deficit;
- locked-assignment conflict;
- spacing conflict;
- qualification deficit;
- pattern infeasibility;
- conflict-pair infeasibility;
- impossible exact fairness requirement; and
- search-budget exhaustion that must not be reported as proven infeasibility.

---

## 11.7 Terminal validation

Every returned schedule should pass an independent validator that is separate from the search-time checks.

```python
def validate_complete_schedule(problem, schedule):
    violations = []

    for constraint in problem.hard_constraints:
        result = constraint.validate_complete(problem, schedule)

        if not result.valid:
            violations.append(result)

    return ValidationReport(
        valid=not violations,
        violations=violations,
    )
```

The final validator should not rely exclusively on mutable counters maintained by the search.

Recompute critical facts directly from the completed schedule.

---

# Phase 12 — Instrument Performance

Add instrumentation before recommending optimization.

## 12.1 Required search metrics

Collect:

- total search nodes;
- assignments attempted;
- assignments accepted;
- immediate constraint rejections;
- propagation calls;
- values pruned;
- domain wipeouts;
- recursive calls;
- total backtracks;
- chronological backtracks;
- backjumps, if supported;
- maximum search depth;
- average branching factor;
- maximum branching factor;
- constraint checks by constraint type;
- time spent in variable selection;
- time spent in value ordering;
- time spent in constraint checking;
- time spent in propagation;
- time spent in state copying or rollback;
- time spent scoring;
- time to first feasible solution;
- time to best solution;
- total runtime;
- peak memory;
- number of solutions found;
- incumbent improvements;
- bound-based prunes;
- timeout or budget status; and
- random seed.

---

## 12.2 Recommended derived metrics

Calculate:

```text
Backtracks per slot =
    total_backtracks / required_slots
```

```text
Checks per attempted assignment =
    total_constraint_checks / assignments_attempted
```

```text
Average values pruned per propagation =
    propagation_pruned_values / propagation_calls
```

```text
Immediate rejection rate =
    immediate_rejections / assignments_attempted
```

```text
Search completion ratio =
    deepest_completed_depth / total_required_variables
```

```text
Propagation efficiency =
    dead_ends_detected_before_recursion / total_dead_ends
```

```text
Optimization improvement =
    first_solution_score - best_solution_score
```

Adjust score direction when higher values are better.

---

## 12.3 Benchmark corpus

Do not benchmark on only one schedule.

Use a corpus containing:

1. small easy satisfiable instance;
2. small difficult satisfiable instance;
3. small unsatisfiable instance;
4. medium representative instance;
5. large representative instance;
6. dense-constraint instance;
7. sparse-constraint instance;
8. many-qualification instance;
9. scarce-qualification instance;
10. many locked assignments;
11. high unavailability;
12. tight spacing limits;
13. optimization-heavy instance; and
14. historical production failure cases.

For each instance, record:

- input size;
- constraint density;
- satisfiability;
- expected result;
- runtime;
- nodes;
- backtracks;
- memory;
- first-solution score;
- best score;
- termination status; and
- seed.

---

## 12.4 Performance thresholds

Do not treat universal “healthy ranges” as correctness rules.

Thresholds depend on:

- roster size;
- number of slots;
- domain size;
- constraint density;
- schedule horizon;
- pattern complexity;
- optimization requirements;
- target hardware;
- implementation language;
- search strategy;
- expected variant count; and
- whether optimality must be proven.

Use provisional targets only when the user provides operational requirements.

Example baseline targets:

| Metric | Example Target | Interpretation |
|---|---:|---|
| Time to first feasible schedule | Under 5 seconds | Example operational goal, not universal |
| Total runtime | Under 30 seconds | Depends on optimization expectations |
| Peak memory | Within platform limit | Must be measured on target device |
| Hard-constraint violations | 0 | Mandatory |
| Incorrect infeasibility reports | 0 | Mandatory |
| State-restoration mismatches | 0 | Mandatory |
| Determinism with fixed seed | 100% | When deterministic mode is required |

When no target is supplied, report empirical measurements and relative comparisons instead of inventing pass/fail thresholds.

---

# Phase 13 — Identify Correctness and Performance Findings

## 13.1 Severity classification

Classify each finding:

### Critical

The engine may:

- emit an invalid schedule;
- omit valid schedules;
- corrupt state across branches;
- overwrite locked assignments;
- violate safety or legal constraints;
- hang indefinitely;
- report infeasibility incorrectly; or
- lose data.

### High

The engine:

- fails on common valid inputs;
- cannot distinguish timeout from infeasibility;
- contains an unsound optimization bound;
- has substantial restoration risk;
- cannot reliably complete expected workloads; or
- produces materially incorrect objective values.

### Medium

The engine:

- is correct under current conditions but fragile;
- has incomplete diagnostics;
- has poor test coverage;
- performs unnecessary search;
- relies on undocumented assumptions;
- has non-deterministic behavior without seed control; or
- has maintainability problems likely to cause future defects.

### Low

The issue affects:

- clarity;
- instrumentation;
- minor efficiency;
- logging;
- documentation;
- code organization; or
- uncommon edge cases with limited impact.

### Informational

The item is:

- a design observation;
- an optional enhancement;
- a future scaling concern; or
- a validated strength.

---

## 13.2 Finding format

Use this structure for every material finding:

```markdown
### Finding CSP-01 — Backtrack does not restore weekly assignment totals

**Severity:** Critical  
**Evidence level:** Confirmed defect  
**Affected component:** `assign_worker()`, `backtrack()`, `weekly_counts`  
**Trigger:** A candidate assignment passes initial checks but fails during deeper recursion.  
**Expected behavior:** The worker's weekly count returns to its pre-branch value.  
**Observed behavior:** The assignment is removed, but `weekly_counts[worker][week]` is not decremented.  
**Consequence:** Sibling branches incorrectly treat the worker as having reached the weekly limit, potentially eliminating valid schedules.  
**Reproduction:** Run the supplied three-day test case and compare canonical state before and after the failed branch.  
**Recommended correction:** Record the counter increment in the restoration trail or recompute weekly totals after rollback.  
**Verification test:** Add a state-equivalence assertion after recursive failure.
```

Do not group unrelated defects into one finding.

---

# False-Positive Prevention

## Do Not

- Do not flag arc-consistency propagation as redundant merely because a constraint is checked elsewhere.
- Do not assume duplicate checks are unnecessary without identifying their distinct lifecycle roles.
- Do not flag all in-place mutation as incorrect; verify whether mutation is fully reversible.
- Do not assume snapshot copying is correct; shallow copies may still leak state.
- Do not report sequential variable ordering as a defect solely because MRV exists.
- Do not report a high backtrack count as defective without comparing problem size, constraint density, and alternatives.
- Do not classify a soft-constraint calculation during search as inherently inefficient.
- Do not assume first-solution search should enumerate all schedules.
- Do not assume all-solutions enumeration is required for variant generation; controlled diversity may be sufficient.
- Do not interpret timeout or search-budget exhaustion as proof of infeasibility.
- Do not classify a valid but unfair schedule as invalid unless fairness is explicitly hard.
- Do not treat a temporarily imbalanced partial schedule as a final fairness failure.
- Do not assume a successful schedule proves search completeness.
- Do not infer correctness from function names or comments.
- Do not recommend stronger propagation without considering its runtime cost.
- Do not recommend caching without defining cache keys and invalidation rules.
- Do not recommend parallel search if shared mutable state is not isolated.
- Do not recommend external optimization libraries without considering platform constraints.
- Do not present a relaxed diagnostic schedule as valid under the original problem.
- Do not claim optimality without proof.
- Do not claim a conflict explanation is minimal unless minimality was established.
- Do not replace domain-specific requirements with generic scheduling assumptions.

## Do

- Verify state restoration before optimizing search.
- Validate returned schedules independently.
- Test both satisfiable and unsatisfiable instances.
- Compare current search against a brute-force reference on small cases.
- Separate correctness findings from performance opportunities.
- Distinguish hard constraints, soft constraints, heuristics, and pruning rules.
- Trace all mutable state across assignment and rollback.
- Benchmark alternative variable and value orderings.
- Verify whether pruning is sound.
- Check that every eligible domain value remains reachable unless soundly pruned.
- Distinguish “no solution exists” from “no solution found within budget.”
- Report assumptions explicitly.
- Identify the smallest reproducible failure case available.
- Preserve existing correct domain-specific behavior.
- Prioritize low-risk correctness repairs before architectural rewrites.
- Provide tests that would fail before the repair and pass afterward.
- State whether each recommendation preserves search completeness.
- Consider target-device memory, recursion, and library limitations.

---

# Recommended Improvement Hierarchy

Prioritize recommendations in this order.

## Priority 1 — Correctness blockers

Examples:

- unsound pruning;
- incomplete restoration;
- missing hard constraints;
- invalid terminal acceptance;
- locked-assignment corruption;
- incorrect date boundaries;
- stale global counters;
- incomplete candidate exploration;
- false infeasibility reporting;
- branch-and-bound using invalid bounds.

## Priority 2 — Termination and observability

Examples:

- infinite loops;
- recursion-depth failure;
- missing timeout status;
- swallowed exceptions;
- no dead-end diagnostics;
- missing instrumentation;
- no deterministic seed.

## Priority 3 — Testability

Examples:

- no independent validator;
- no unsatisfiable tests;
- no state-equivalence tests;
- no brute-force differential tests;
- no property-based tests;
- no production-regression corpus.

## Priority 4 — Search efficiency

Examples:

- MRV;
- degree tie-breaking;
- least-constraining value;
- forward checking;
- stronger scheduling-specific propagation;
- incremental counters;
- trail-based rollback;
- branch-and-bound;
- conflict-directed backjumping;
- nogood recording;
- decomposition;
- symmetry breaking.

## Priority 5 — Optimization quality

Examples:

- corrected objective weights;
- lexicographic priorities;
- role-specific fairness;
- historical fairness;
- diverse near-optimal variants;
- improved bounds;
- score normalization.

## Priority 6 — Maintainability

Examples:

- explicit state object;
- constraint registry;
- typed result statuses;
- immutable configuration;
- separated validation and scoring;
- improved naming;
- centralized date arithmetic;
- structured logs.

---

# Algorithm and Architecture Recommendations

Recommend only techniques supported by observed needs.

## Possible improvements

### Forward checking

Use when direct assignment consequences are not currently propagated.

### MRV with degree tie-breaking

Use when difficult variables are discovered too late.

### Least-constraining-value ordering

Use when early worker selection frequently blocks later coverage.

### Grouped pattern variables

Use when multi-day or multi-role patterns must be assigned atomically.

### Trail-based reversible state

Use when full snapshots dominate runtime and mutation paths can be centralized.

### Immutable child states

Use when correctness and simplicity are more important than copy cost.

### Incremental constraint indexes

Use for frequently queried facts such as:

- worker assignments by date;
- weekly counts;
- qualification groups;
- occupied intervals;
- gap windows;
- role counts; and
- conflict adjacency.

### Conflict-directed backjumping

Use when failures can be attributed to a subset of prior assignments.

### Nogood recording

Use when the solver repeatedly encounters equivalent failed partial assignments.

### Symmetry breaking

Use when interchangeable workers or equivalent slots produce duplicate search branches.

Do not apply symmetry breaking when workers have distinct history, preferences, seniority, qualifications, or fairness state that makes them non-interchangeable.

### Decomposition

Use when the problem can be safely separated into:

- independent date ranges;
- independent role groups;
- pattern assignment followed by regular fill;
- feasibility phase followed by optimization; or
- master assignment followed by local repair.

Verify that cross-component constraints do not invalidate the decomposition.

### Memoization

Use only when the state can be represented by a complete, canonical, hashable key.

Do not cache results using a key that omits:

- counts;
- historical state;
- remaining domains;
- locked assignments;
- pattern state;
- score-relevant information; or
- other facts that affect future feasibility.

---

# Tool and Methodology Guidance

Depending on the environment, consider:

- unit-testing frameworks;
- property-based testing;
- profiling tools;
- deterministic random seeds;
- structured logging;
- trace visualizations;
- flame graphs;
- memory profilers;
- graph visualization for constraint graphs;
- brute-force reference solvers for small instances;
- SAT, SMT, CP-SAT, ILP, or MIP reference models;
- assertion-heavy debug builds; and
- canonical state serializers for restoration testing.

External solvers may be useful as reference implementations even when the production target cannot run them.

Do not require a library that is unavailable on the user's deployment platform.

When recommending a solver migration, compare:

- installation feasibility;
- architecture compatibility;
- licensing;
- target platform;
- model expressiveness;
- explainability;
- deterministic behavior;
- memory consumption;
- runtime;
- maintenance burden; and
- migration complexity.

---

# Expected Output

Produce the audit in the following order.

## 1. Executive Assessment

Include:

- overall correctness status;
- overall completeness status;
- overall performance status;
- highest-risk finding;
- whether valid schedules may be omitted;
- whether invalid schedules may be emitted;
- whether infeasibility is reported reliably;
- whether optimization claims are justified; and
- confidence level.

## 2. System Reconstruction

Document:

- scheduling horizon;
- variables;
- domains;
- state representation;
- search entry point;
- assignment lifecycle;
- terminal condition;
- requested solution type; and
- important assumptions.

## 3. CSP Model Map

Provide:

- variable inventory;
- domain-construction summary;
- hard-constraint inventory;
- soft-constraint inventory;
- constraint graph or dependency description;
- completeness assessment; and
- mismatches between requirements and implementation.

## 4. Search-Control Audit

Evaluate:

- recursive or iterative structure;
- base cases;
- variable selection;
- value ordering;
- branch traversal;
- success propagation;
- failure propagation;
- solution copying; and
- candidate completeness.

## 5. Constraint Propagation Analysis

Report:

- propagation strategy;
- affected neighbors;
- pruning logic;
- soundness;
- strength;
- domain wipeout handling;
- transitive behavior;
- restoration mechanism; and
- missing propagation opportunities.

## 6. State Restoration Audit

Provide:

- mutable-state inventory;
- restoration mechanism;
- confirmed restoration failures;
- aliasing risks;
- counter rollback results;
- score rollback results;
- exception-safety assessment;
- canonical state-equivalence test; and
- pass/fail conclusion.

## 7. Termination and Infeasibility Analysis

Report:

- termination states;
- timeout and budget behavior;
- unsatisfiable test results;
- initial capacity checks;
- dead-end diagnostics;
- conflict explanations;
- false-infeasibility risks; and
- distinction between proven infeasibility and incomplete search.

## 8. Optimization Audit

Report:

- objective definition;
- hard/soft separation;
- score consistency;
- incremental-scoring validity;
- branch-and-bound correctness;
- incumbent handling;
- optimality claims;
- fairness dimensions; and
- variant-generation behavior.

## 9. Verification Test Plan

Include:

- unit tests;
- boundary tests;
- satisfiable integration tests;
- unsatisfiable integration tests;
- restoration tests;
- differential tests;
- property-based tests;
- metamorphic tests;
- regression tests; and
- final-schedule validation.

## 10. Performance Profile

Provide:

- benchmark environment;
- benchmark instances;
- raw metrics;
- derived metrics;
- search-tree bottlenecks;
- time distribution;
- memory behavior;
- heuristic comparison;
- propagation comparison; and
- confidence limitations.

## 11. Findings

List each finding with:

- unique identifier;
- severity;
- evidence level;
- affected component;
- trigger;
- expected behavior;
- observed behavior;
- consequence;
- reproduction;
- correction; and
- verification test.

## 12. Prioritized Recommendations

Organize recommendations as:

1. correctness blockers;
2. termination and observability;
3. test coverage;
4. search efficiency;
5. optimization quality;
6. maintainability.

For every recommendation, state:

- expected impact;
- completeness risk;
- implementation effort;
- regression risk;
- dependencies;
- validation method; and
- priority.

## 13. Final Verdict

Classify the scheduler as one of:

- **Correct and appropriate for current scale**
- **Correct but inefficient**
- **Correct under limited assumptions**
- **Likely correct but insufficiently tested**
- **Incorrect due to state-restoration defects**
- **Incorrect due to model or constraint defects**
- **Incomplete due to unsound pruning or search limits**
- **Unable to establish correctness from available evidence**

---

# Output Tables

## Constraint inventory

| ID | Constraint | Hard/Soft | Scope | Enforcement Point | Boundary Rule | Test Coverage | Status |
|---|---|---|---|---|---|---|---|

## Mutable-state inventory

| State Component | Modified By | Restored By | Restoration Method | Verified | Risk |
|---|---|---|---|---|---|

## Heuristic comparison

| Strategy | Nodes | Backtracks | First-Solution Time | Total Time | Best Score | Completeness |
|---|---:|---:|---:|---:|---:|---|

## Finding summary

| ID | Severity | Evidence | Component | Impact | Recommended Action |
|---|---|---|---|---|---|

## Recommendation roadmap

| Priority | Recommendation | Correctness Impact | Performance Impact | Effort | Regression Risk |
|---:|---|---|---|---|---|

---

# Quality Checklist

## Model

- [ ] Every required schedule slot is represented.
- [ ] Initial domains contain every legally eligible value.
- [ ] Initial domains exclude values that are already impossible.
- [ ] All hard constraints are enumerated.
- [ ] All soft constraints are separately enumerated.
- [ ] Locked assignments are represented consistently.
- [ ] Date and interval boundaries are explicitly defined.
- [ ] Pattern constraints are modeled without incompatible partial states.

## Search

- [ ] Every unassigned variable remains reachable.
- [ ] Every unpruned domain value remains reachable.
- [ ] Base cases are complete and correct.
- [ ] Complete schedules receive independent validation.
- [ ] Success and failure propagate correctly.
- [ ] Returned solutions are copied safely.
- [ ] Search-budget exhaustion is distinguished from infeasibility.

## Propagation

- [ ] Every pruning rule is sound.
- [ ] Domain wipeouts are detected.
- [ ] Propagation state is reversible.
- [ ] Constraint graph dependencies are complete.
- [ ] Global constraints are not incorrectly reduced to local checks.
- [ ] Propagation return values have unambiguous meanings.

## Restoration

- [ ] Assignments restore correctly.
- [ ] Domains restore correctly.
- [ ] Counts restore correctly.
- [ ] Caches restore or invalidate correctly.
- [ ] Scores restore correctly.
- [ ] Pattern state restores correctly.
- [ ] Restoration occurs on return, failure, timeout, and exception.
- [ ] Canonical state before and after rollback is identical.

## Infeasibility

- [ ] At least one unsatisfiable configuration is tested.
- [ ] Initial empty domains are detected.
- [ ] Capacity deficits are detected where possible.
- [ ] Locked-assignment conflicts are reported.
- [ ] Timeout is not reported as proof of infeasibility.
- [ ] Conflict explanations identify actionable requirements.

## Optimization

- [ ] Hard constraints cannot be traded for score.
- [ ] Objective direction is explicit.
- [ ] Score weights are documented.
- [ ] Incremental scores match full recomputation.
- [ ] Branch-and-bound bounds are valid.
- [ ] Optimality is claimed only when proven.
- [ ] Total fairness and role-specific fairness are evaluated separately where needed.

## Testing

- [ ] Every hard constraint has positive and negative tests.
- [ ] Boundary cases are tested.
- [ ] Restoration tests include deep recursive failure.
- [ ] Small instances are compared with brute force.
- [ ] Property-based invariants are defined.
- [ ] Production failures become regression tests.
- [ ] The final schedule is validated independently.

## Performance

- [ ] Search instrumentation is present.
- [ ] Benchmarks cover multiple problem classes.
- [ ] Measurements are made on the target platform when possible.
- [ ] Heuristic comparisons use identical inputs and seeds.
- [ ] Performance targets are not treated as universal constants.
- [ ] Correctness is revalidated after every optimization.

---

# Customization Guide

## Healthcare scheduling

Add or verify:

- active licensure;
- certification requirements;
- unit competencies;
- skill-mix requirements;
- charge or supervisory coverage;
- fatigue and mandatory-rest limits;
- weekend and holiday rotations;
- first-call and backup-call roles;
- locked leave;
- orientation or competency restrictions;
- PRN rules;
- overtime limits;
- consecutive-shift safety limits;
- post-call restrictions;
- multi-day call patterns;
- historical fairness;
- facility-specific policies; and
- regulatory or contractual requirements.

Treat safety, licensure, competency, and mandatory-rest rules as hard constraints unless the governing policy explicitly states otherwise.

For fixed weekend patterns such as alternating Main and Backup roles across Friday, Saturday, and Sunday, consider representing the entire weekend assignment as a grouped decision rather than three unrelated daily decisions.

---

## Retail scheduling

Add or verify:

- opener, closer, and mid-shift roles;
- minor-work restrictions;
- meal and rest breaks;
- minimum staffing by interval;
- role coverage;
- employee availability;
- maximum weekly hours;
- overtime thresholds;
- split-shift restrictions;
- opening-after-closing rest rules;
- manager coverage;
- part-time availability;
- weekend fairness; and
- preferred-hour targets.

Forward checking is often valuable because part-time availability can produce small, highly uneven domains.

---

## Emergency services

Add or verify:

- 24-on/48-off or related rotation patterns;
- mandatory recovery periods;
- maximum continuous duty;
- certification combinations;
- vehicle or station qualification;
- minimum crew composition;
- station transfer time;
- overtime limits;
- relief coverage;
- leave;
- training assignments;
- callback rules; and
- disaster or surge staffing.

Long-range rest and rotation rules may require global or pattern constraints rather than only local adjacent-day checks.

---

## Education scheduling

Add or verify:

- instructor qualifications;
- room capacity;
- room equipment;
- student-group conflicts;
- course sequence;
- examination spacing;
- instructor availability;
- campus travel time;
- shared-resource conflicts;
- required contact hours;
- accessibility requirements;
- maximum consecutive teaching periods; and
- fixed institutional events.

---

## Manufacturing scheduling

Add or verify:

- machine eligibility;
- setup times;
- changeover sequence;
- maintenance windows;
- job precedence;
- material availability;
- operator qualifications;
- batch constraints;
- machine capacity;
- processing duration;
- due dates;
- parallel-machine compatibility; and
- no-overlap constraints.

Interval-based or disjunctive scheduling models may be more appropriate than one-variable-per-calendar-slot models.

---

# Techniques Used

- **ST-01 — Clear Objective Statement:** Defines correctness, completeness, restoration, infeasibility, optimization, and performance as separate audit targets.
- **ST-02 — Structured Sequential Instructions:** Organizes the review from model reconstruction through testing, profiling, findings, and recommendations.
- **RT-02 — Multi-Dimensional Analysis:** Examines model semantics, search control, propagation, mutable state, termination, diagnostics, optimization, testing, and runtime behavior.
- **DS-01 — Framework Application:** Applies formal CSP concepts to real scheduling-engine implementations.
- **DS-02 — Metric Specification:** Defines raw and derived metrics for empirical performance analysis.
- **DS-03 — Tool and Methodology Suggestions:** Recommends differential testing, property-based testing, profiling, reversible-state techniques, and alternative solver models where appropriate.
- **QA-01 — Chain-of-Verification:** Requires independent schedule validation, rollback-equivalence testing, unsatisfiable cases, and evidence-linked findings.

---

# Related Prompts

- `algorithms_multi_criteria_schedule_optimization.md` — Score, compare, and rank feasible schedule variants.
- `algorithms_data_structure_selection.md` — Select representations for domains, assignments, counters, interval indexes, and constraint graphs.
- `algorithms_heap_priority_queue.md` — Review priority structures used for dynamic variable or candidate ordering.
- `testing_constraint_logic_edge_cases.md` — Build boundary, interaction, property-based, and regression tests for scheduling constraints.
- `performance_scheduling_algorithm_optimization.md` — Profile and optimize a scheduler after correctness has been established.
