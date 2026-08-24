---
title: "Plugin Architecture Review for Constraint Systems"
category: code-analysis/architecture
description: "Review and improve a plugin-based constraint system for extensibility, isolation, composability, and fault tolerance"
tags:
  - architecture
  - plugin-system
  - constraints
  - extensibility
  - scheduling
  - design-patterns
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DS-01  # Framework Application
  - RT-05  # Evidence-Based Reasoning
  - CM-02  # Constraint Specification
  - DS-06  # Prioritization Guidance
difficulty: intermediate
version: "1.0"
updated: 2026-03-04
related_prompts:
  - architecture_coupling_cohesion_analysis.md
  - architecture_design_pattern_identification.md
  - algorithms_constraint_satisfaction_scheduling.md
---

# Plugin Architecture Review for Constraint Systems

**Objective:** Evaluate a plugin-based constraint system for clear interface contracts, fault isolation, composability, and ease of extension — ensuring new constraint types can be added without modifying engine code.

**When to Use:** Use this prompt when reviewing a scheduling, rules engine, or validation system that supports user-defined or plugin-based constraints. Particularly relevant when the constraint system needs to be extended by users who are not the core engine developers.

**Instructions:**

1. **Plugin Contract Analysis**

   Identify the constraint plugin interface:
   ```python
   # What does the interface look like?
   class ConstraintPlugin(ABC):
       @abstractmethod
       def evaluate(self, assignment, state) -> bool:
           """Return True if assignment satisfies this constraint."""
           pass

       @abstractmethod
       def name(self) -> str:
           pass
   ```

   **Verify:**
   - Is the interface documented with type hints and docstrings?
   - Is the `state` parameter read-only from the plugin's perspective?
   - What does `evaluate` receive: the single proposed assignment, or the full schedule state?
   - Does the interface support both hard constraints (pass/fail) and soft constraints (score)?
   - Is the interface stable across versions? Are breaking changes versioned?

2. **Registration and Discovery**

   How are plugins loaded?

   | Method | Pros | Cons |
   |--------|------|------|
   | Explicit import in code | Simple, clear | Requires code change to add plugin |
   | Config-driven loading | Users can enable/disable via YAML | Harder to debug load failures |
   | Entry-points / setuptools | Standard Python packaging | Requires install step |
   | Directory scanning | Drop a file to add a constraint | Import errors are silent |

   **Verify:**
   - Can a plugin be added without modifying any engine source file?
   - Is plugin loading order deterministic?
   - Are load failures reported with actionable error messages?
   - Is there a plugin validation step at load time (interface conformance check)?

3. **Isolation and Fault Tolerance**

   **What happens when a plugin misbehaves?**

   | Failure Mode | Expected Behavior | Common Bug |
   |-------------|-------------------|------------|
   | Plugin raises exception | Caught, logged, constraint treated as violated | Uncaught exception crashes engine |
   | Plugin returns wrong type | Type check, clear error | Engine treats non-bool as truthy |
   | Plugin enters infinite loop | Timeout after N seconds | Engine hangs forever |
   | Plugin modifies shared state | State is immutable/copied | Plugin corrupts other constraints |

   **Verify:**
   - Are plugin calls wrapped in try/except?
   - Is there a timeout mechanism for constraint evaluation?
   - Is the schedule state passed to plugins immutable or a defensive copy?

4. **State Access Encapsulation**

   What can plugins see and do?

   ```python
   # GOOD: Plugin receives a frozen view
   class ConstraintContext:
       """Read-only view of schedule state for plugins."""
       @property
       def assignments(self) -> FrozenDict:  # Cannot modify
           ...
       @property
       def roster(self) -> Tuple[Worker, ...]:  # Immutable
           ...

   # BAD: Plugin receives the engine's mutable state
   def evaluate(self, assignment, engine_state):
       engine_state.assignments[date] = None  # Plugin can corrupt state!
   ```

   **Verify:**
   - Can a plugin access internals it shouldn't (database connections, other plugins' state)?
   - Is there a clear boundary between "what the plugin can read" and "what it can write"?

5. **Constraint Composability**

   When multiple constraints apply to the same assignment:

   ```
   Composability Questions:
   ├── Ordering: Does evaluation order matter?
   │   ├── If constraint A prunes a domain, does constraint B see the pruned domain?
   │   └── Are constraints guaranteed to be commutative?
   │
   ├── Conflicts: Can two plugins create contradictory rules?
   │   ├── Plugin A: "Worker must have >= 2 day gap"
   │   ├── Plugin B: "Worker must work >= 3 days per week"
   │   └── Together: May be unsatisfiable for small rosters
   │
   └── Dependencies: Can one constraint depend on another's result?
       └── Should constraints declare ordering dependencies?
   ```

   **Verify:**
   - Is constraint evaluation order configurable or fixed?
   - Does the engine detect unsatisfiable constraint combinations?
   - Can plugins declare conflicts with other plugins?

6. **Plugin Testability**

   Can a constraint plugin be unit-tested without the full engine?

   ```python
   # GOOD: Plugin is testable in isolation
   def test_minimum_gap_constraint():
       plugin = MinimumGapConstraint(days=2)
       state = MockScheduleState(assignments={
           date(2025, 1, 1): "Alice",
           date(2025, 1, 3): None,  # Proposed slot
       })
       assert plugin.evaluate(Assignment("Alice", date(2025, 1, 3)), state) == False

   # BAD: Plugin requires full engine initialization to test
   def test_minimum_gap_constraint():
       engine = SchedulerEngine(config="full_config.yaml")
       engine.load_roster()
       engine.load_plugins()
       # ... 20 lines of setup just to test one constraint
   ```

   **Verify:**
   - Is there a mock/stub for the schedule state context?
   - Can individual plugins be instantiated with test configuration?
   - Are plugin-specific test fixtures provided?

7. **Extension Points Completeness**

   **What can't be expressed as a plugin?** Document the ceiling:

   | Capability | Plugin-able? | If Not, Why |
   |-----------|-------------|-------------|
   | New constraint type | Yes | Core purpose of plugin system |
   | New scoring metric | ? | May require engine changes |
   | Custom assignment strategy | ? | May bypass plugin interface |
   | New export format | ? | Separate extension point needed |
   | Custom day type | ? | May be config-only |

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag the absence of a timeout mechanism as critical if all built-in constraints are known to be fast — it's a robustness issue, not a correctness issue
- Recommend full sandboxing (subprocess isolation) for plugins in a single-user desktop application — the overhead isn't justified
- Flag "plugins can read full schedule state" as a security issue — in scheduling, constraints need to see the full picture to make decisions
- Insist on setuptools entry-points for an application that isn't distributed as a package

✅ **DO:**
- Check whether the plugin interface supports the distinction between hard and soft constraints
- Verify that adding a new constraint type doesn't require modifying any file in the engine's core directory
- Test what happens when a plugin is misconfigured (wrong parameters in YAML)
- Evaluate whether the plugin system's complexity is proportional to the number of expected plugins

## Expected Output

For each review area, provide:

```
Area: [Plugin Contract / Registration / Isolation / etc.]
Status: [Good / Needs Improvement / Critical]
Evidence: [Specific code paths or configuration that demonstrates the finding]
Impact: [What goes wrong if this isn't addressed]
Recommendation: [Specific fix with estimated effort]
```

**Summary table:**

| Area | Status | Priority | Effort |
|------|--------|----------|--------|
| Plugin Contract | ... | ... | ... |
| Registration | ... | ... | ... |
| Isolation | ... | ... | ... |
| State Access | ... | ... | ... |
| Composability | ... | ... | ... |
| Testability | ... | ... | ... |
| Extension Points | ... | ... | ... |

## Quality Checklist

- [ ] Plugin interface is documented with type information
- [ ] At least one "misbehaving plugin" scenario is tested
- [ ] Constraint composability conflicts are identified
- [ ] Plugin testability is verified with an isolation test example
- [ ] Extension ceiling is documented

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focuses review on plugin extensibility for constraint systems
- **ST-02** (Structured Sequential Instructions) — Systematic review from contract to completeness
- **RT-02** (Multi-Dimensional Analysis) — Evaluates contract, isolation, composability, testability
- **DS-01** (Framework Application) — Applies plugin architecture patterns to the constraint domain
- **RT-05** (Evidence-Based Reasoning) — Requires specific code paths and configuration references
- **CM-02** (Constraint Specification) — Defines what the plugin system must and must not allow
- **DS-06** (Prioritization Guidance) — Ranks issues by impact on plugin authors

## Related Prompts

- `architecture_coupling_cohesion_analysis.md` — General coupling analysis applicable to plugin boundaries
- `architecture_design_pattern_identification.md` — Identifying patterns (Strategy, Observer) in the plugin system
- `algorithms_constraint_satisfaction_scheduling.md` — The CSP engine that evaluates these plugin constraints
- `testing_constraint_logic_edge_cases.md` — Testing the constraints that plugins implement
