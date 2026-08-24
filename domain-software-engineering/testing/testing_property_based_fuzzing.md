---
title: "Property-Based and Fuzz Test Design"
category: testing
description: "Design property-based and fuzz tests: identify invariants, choose frameworks (Hypothesis, fast-check, proptest, jqwik, libFuzzer, AFL++), specify shrinking strategy, coverage-guided input generation, and CI integration."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - testing
  - property-based
  - fuzzing
  - hypothesis
  - fast-check
  - libfuzzer
  - afl
  - invariants
  - coverage-guided
updated: "2026-04-17"
related_prompts:
  - testing_unit_test_generation.md
  - testing_mutation_testing.md
  - testing_coverage_gap_analysis.md
---

# Property-Based and Fuzz Test Design

**Objective:** Identify candidate invariants and fuzz targets in a codebase, choose appropriate frameworks, design shrinking strategies, and integrate property-based and fuzz tests into CI with a triage plan for failures.

## When to Use

- Code with a clear **contract** (parser, serializer, data structure, algorithm, protocol handler).
- After a bug that example-based tests missed — the classic signal that invariants are worth more than example cases.
- Before shipping security-sensitive parsers, crypto, networking code, or anything that accepts untrusted input.
- When mutation testing reveals gaps that examples can't close.

**Do NOT use this prompt for:**
- UI / E2E tests (different failure modes).
- Performance tests (use `testing_performance_load_test_planning.md`).
- Contract tests between services (use `testing_contract_test_design.md`).

## Inputs / Context

Collect:
- **Language**: Python, JS/TS, Rust, Java/Kotlin, C/C++, Go, .NET.
- **Code type**: parser / serializer / stateful data structure / pure function / protocol handler.
- **Trust boundary**: is input attacker-controlled? (Drives fuzzing vs property-based choice.)
- **Existing test suite**: what's covered by examples, what's not.
- **CI budget**: time and compute for long-running property/fuzz jobs.
- **Coverage tooling**: SanitizerCoverage / gcov / llvm-cov availability for coverage-guided fuzzing.

## Must / Must Not

**Must:**
- Distinguish the two disciplines:
  - **Property-based testing**: invariants over structured, shrinkable inputs; hundreds to thousands of cases per run; CI-friendly.
  - **Fuzzing**: coverage-guided, byte-level mutation over untrusted inputs; long-running; crash-finding.
- Pick framework by language + code type:
  - Python: **Hypothesis** (property) / **Atheris** (fuzz).
  - JS/TS: **fast-check** (property) / **jsfuzz** (fuzz).
  - Rust: **proptest** / **quickcheck** (property), **cargo-fuzz** + libFuzzer (fuzz), **AFL++** for aggressive fuzzing.
  - Java/Kotlin: **jqwik** (property), **Jazzer** (fuzz).
  - C/C++: **RapidCheck** (property), **libFuzzer** + **AFL++** (fuzz) with sanitizers (ASan, UBSan, MSan).
  - Go: built-in **testing/quick** or **gopter** (property), built-in **go test -fuzz** (fuzz).
- For every invariant, state the **oracle** (how we know it held): round-trip, equivalence to a reference implementation, monotonicity, idempotence, closure, postcondition.
- Specify **shrinking strategy** — fail fast with minimized counter-examples.
- Define **seed corpus** for fuzzing (real inputs, edge cases, regression corpus from prior bugs).
- Specify **crash triage**: how failures get reduced, deduplicated, assigned, and regressed into the test suite.

**Must Not:**
- Recommend fuzzing without sanitizers (ASan, UBSan, MSan) for native code — you'll miss 90% of the bugs.
- Use property-based tests where examples are clearer (don't over-parametrize trivial logic).
- Use fuzzing where property-based tests are better (structured input, not byte soup).
- Ship fuzz tests without a **time/iteration budget** and a **timeout per input**.
- Omit the **regression corpus** — every crash becomes a fixed-input test so we never regress.
- Treat a green property run as proof of correctness; it's evidence, not proof.

## Instructions

1. **Identify candidate targets**:
   - Pure functions with non-trivial input domains.
   - Serializers / deserializers (round-trip property).
   - Parsers / validators (never-crash invariant; accept-reject invariants).
   - State machines (legal-transition invariants).
   - Data structures (structural invariants after every operation).
   - Binary protocols / network handlers (fuzz candidates).
2. **Choose the discipline per target** — property-based for structured invariants, fuzzing for byte-level untrusted input.
3. **Design invariants** — list each as `for all inputs X satisfying P, the postcondition Q holds`.
4. **Select framework** and state the **generator / strategy** for input shape.
5. **Define seed corpus** (fuzzing only) — regressions + realistic inputs.
6. **Specify CI integration**:
   - Property: run every PR with fixed time budget (e.g., 30s per property).
   - Fuzzing: nightly / continuous with OSS-Fuzz or self-hosted.
   - Triage: how crashes land in an issue tracker.

## Output Format

```
# Property-Based & Fuzz Test Plan — <Module>

## Target Inventory
| Target | Type | Discipline | Framework | Invariant(s) |
|--------|------|-----------|-----------|--------------|
| parse(input) | parser | Fuzz + PBT | Atheris + Hypothesis | never crashes; round-trip with serialize(); grammar invariants |
| Stack.push/pop | data struct | PBT | Hypothesis | stack invariants (size, LIFO order, idempotent pop on empty) |
...

## Per-Target Detail

### parse(input) — Fuzz + PBT
- **PBT invariants**:
  - `parse(serialize(x)) == x` for all valid `x` (round-trip).
  - `parse` returns Ok or Err but never panics for any input.
- **PBT generator**: structured AST generator in Hypothesis.
- **Fuzz target**: byte-level input to `parse`.
- **Seed corpus**: `tests/corpus/parse/` seeded with regression crashes.
- **Sanitizers**: ASan + UBSan.
- **Budget**: 10 min per PR; 8 hours nightly.
- **Triage**: minimized crashes → `bugs/fuzz/` + regression case added.

...

## CI Integration
- Property tests: every PR, `pytest` / `npm test` run with fixed seed budget.
- Fuzz: nightly job, OSS-Fuzz integration or self-hosted, timeout 4h per target.
- Failure gating: property tests are required; fuzz failures file issues, don't block PR.

## Out of Scope
<what this plan will NOT catch>
```

## Verification (Self-Check)

Before emitting:

1. Every candidate target has a **discipline** justified (PBT vs fuzz vs both).
2. Every invariant states the **oracle** — how we know it held.
3. Native-code fuzz targets list **sanitizers**.
4. Fuzz budget (time, iterations, per-input timeout) is specified.
5. Seed corpus policy is stated.
6. Confidence per target (High if invariants obvious; Medium if contract unclear).

## False-Positive Prevention

Rule out:

- **"Property test failing"** — Some properties fail because the generator is too aggressive; verify the input is legal before declaring a bug.
- **"Fuzz found a crash"** — Panic on clearly-invalid input is fine for `parse()` that returns `Result`, but a **C panic / segfault** is always a bug.
- **"Flaky property"** — Properties should be deterministic given a seed. If flaky, fix the generator, don't skip.
- **"Coverage plateau means done"** — Plateau can mean generator is stuck in a local maximum; mutate corpus.
- **"100k iterations, no crash, must be safe"** — Fuzzing finds **classes** of bugs, not all bugs; don't over-claim.

If you did not inspect actual invariants (just file / module names), cap confidence at **Medium** and flag for review.

## Techniques Applied

ST-01, ST-02, ST-03, RT-02, RT-05, CM-02, QA-01.
