---
title: "Android Concurrency & Threading Analysis"
category: mobile-development
description: "Analyzes an Android app's coroutine, Flow, and threading architecture for structured concurrency, dispatcher and main-safety discipline, scope and cancellation correctness, shared-state races, and Flow collection patterns."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-02
difficulty: advanced
tags:
  - android
  - concurrency
  - coroutines
  - flow
  - threading
  - structured-concurrency
  - analysis
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_performance_audit.md
  - domain-software-engineering/mobile/android/analysis/android_data_layer_persistence_analysis.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_coroutine_scope_review.md
---

# Android Concurrency & Threading Analysis

**Objective:** Analyze an Android app's concurrency and threading model at the codebase level — coroutine scope and lifecycle binding, dispatcher selection and main-safety, structured concurrency and cancellation, `Flow`/`StateFlow`/`SharedFlow` production and collection, shared mutable state and race conditions, and legacy threading (threads/handlers/RxJava bridges) — reporting correctness and performance risks with `file:line` evidence and fixes.

**When to Use:** Use this when the app shows ANRs, jank, intermittent data races, leaked coroutines, work that keeps running after a screen closes, or inconsistent `Flow` collection patterns; before scaling concurrency; or to standardize a threading model across modules. This is a **portfolio-level** analysis — for a single narrow scope, use `targeted-reviews/android_coroutine_scope_review.md`.

---

## Context Gathering

1. **Primitives:** "Coroutines/Flow, RxJava, threads/`Handler`/`Executor`, or a mix? Any legacy `AsyncTask`?"
2. **Architecture:** "Where does async work live (ViewModel, repository, use case, WorkManager)?"
3. **Symptoms:** "Any ANRs, jank, duplicated work, stale UI, or 'work won't stop' reports?"
4. **Dispatchers:** "Is there a centralized dispatcher provider, or `Dispatchers.*` used inline?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the real scope and dispatcher** — find where the coroutine is launched, on which scope and dispatcher; cite `file:line`.
2. **Confirm the hazard** — a `Dispatchers.IO` block is fine; main-thread blocking or an unscoped `GlobalScope` launch is not. Verify the actual thread/scope.
3. **Check existing safety** — `withContext`, `viewModelScope`, `repeatOnLifecycle`, or a fake/test dispatcher may already address an apparent issue.
4. **Distinguish correctness from style** — a race or leak is a defect; a stylistic dispatcher choice may not be.

**A sound concurrency model is an acceptable outcome.** Don't manufacture races.

### False-Positive Prevention

- ❌ Do NOT flag `Dispatchers.IO` for blocking I/O — that's its purpose.
- ❌ Do NOT flag `GlobalScope` in `Application`-lifetime work that is genuinely app-scoped and intentional (note it, but assess).
- ❌ Do NOT call a suspend function "blocking" — suspension is not thread-blocking.
- ❌ Do NOT flag `SharedFlow`/`StateFlow` replay/buffer choices without understanding the use case.
- ✅ DO flag main-thread blocking I/O / heavy CPU work.
- ✅ DO flag unscoped/leaked coroutines surviving their owner.
- ✅ DO flag shared mutable state mutated from multiple coroutines without synchronization.

---

### Phase 1: Concurrency Inventory

| Item | What to Locate |
|------|----------------|
| Scopes | `viewModelScope`, `lifecycleScope`, custom `CoroutineScope`, `GlobalScope` |
| Dispatchers | `Dispatchers.Main/IO/Default`, `withContext`, central provider vs inline |
| Async entry points | `launch`/`async`, `Flow` builders, callbacks-to-coroutine bridges |
| Flow usage | `StateFlow`/`SharedFlow`/cold `Flow`; collection sites and lifecycle awareness |
| Legacy threading | Raw `Thread`, `Handler`, `Executor`, RxJava, `AsyncTask` |
| Shared state | `var`/mutable collections accessed across coroutines |

---

### Phase 2: Structured Concurrency & Lifecycle

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Unscoped launch | HIGH | `GlobalScope.launch` / custom scope never cancelled → leaks |
| Wrong scope | HIGH | Long work in `viewModelScope` that should be `WorkManager`/app scope (or vice versa) |
| Cancellation ignored | MEDIUM | Non-cooperative cancellation; `isActive`/`ensureActive` missing in loops |
| Lifecycle collection | HIGH | `Flow` collected without `repeatOnLifecycle`/`flowWithLifecycle` (waste/leaks when backgrounded) |
| Exception handling | MEDIUM | No `CoroutineExceptionHandler`/supervisor where a child failure shouldn't cancel siblings |
| `runBlocking` misuse | HIGH | `runBlocking` on main thread or in production paths |

---

### Phase 3: Dispatcher & Main-Safety

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Main-thread blocking | CRITICAL | DB/file/network/heavy CPU on `Dispatchers.Main` |
| Missing main-safety | HIGH | Suspend functions that don't guarantee their own dispatcher (`withContext`) |
| Inline dispatchers | MEDIUM | `Dispatchers.*` hardcoded, blocking test injection (no provider) |
| Over-parallelization | LOW | Unbounded `async` fan-out exhausting threads |

---

### Phase 4: Flow Correctness & Shared State

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Race on shared state | HIGH | Mutable state mutated from multiple coroutines without `Mutex`/atomics/confinement |
| Hot-flow leaks | MEDIUM | `MutableStateFlow`/`SharedFlow` collected in a scope that never cancels |
| `stateIn`/`shareIn` scope | MEDIUM | Wrong sharing scope/started policy causing restarts or leaks |
| Backpressure/conflation | LOW | High-frequency emissions without `conflate`/`buffer` causing jank |
| Duplicate work | MEDIUM | Cold flows re-collected, triggering duplicate network/DB calls (no caching/sharing) |

---

## Output Format

```markdown
## Android Concurrency & Threading Analysis Report

### Concurrency Model Summary
| Aspect | Current | Assessment |
|--------|---------|------------|
| Scoping | | |
| Dispatcher discipline | | |
| Flow collection | | |
| Shared state | | |

### Findings (severity-ordered)
**[SEVERITY] Area: title** — Location `file:line` · Hazard (leak/race/ANR/jank) · Fix

### Prioritized Remediation (P1/P2/P3)

### What's Already Solid
```

---

## Expected Output

1. **Concurrency model summary.**
2. **Severity-rated findings** (leaks, races, main-safety) with locations and fixes.
3. **Prioritized remediation.**
4. **Affirmation** of correct patterns.

---

## Techniques Used

- **ST-01** (Clear Objective): Concurrency/threading scope.
- **ST-02** (Structured Sequential Instructions): Inventory → structure → dispatchers → flow/state.
- **RT-02** (Multi-Dimensional Analysis): Correctness + performance + lifecycle.
- **RT-05** (Evidence-Based Reasoning): Scope/dispatcher citations.
- **DS-06** (Prioritization Guidance): Severity ordering.
- **QA-02** (Edge Case Coverage): Cancellation, races, backgrounded collection.

---

## Related Prompts

- [android_performance_audit.md](android_performance_audit.md) - Jank/ANR performance angle
- [android_data_layer_persistence_analysis.md](android_data_layer_persistence_analysis.md) - Where async data work lands
- [android_coroutine_scope_review.md](../targeted-reviews/android_coroutine_scope_review.md) - Narrow, deep single-scope review
