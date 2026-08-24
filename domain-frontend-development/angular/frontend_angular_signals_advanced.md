---
title: "Angular Signals Advanced Analysis"
category: frontend-development/angular
description: "Audit advanced Angular signals usage — signal/computed/effect correctness, signal-based components, RxJS interop, zoneless change detection, and migration away from zone.js patterns."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - angular
  - signals
  - computed
  - effects
  - rxjs-interop
  - zoneless
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/angular/frontend_angular_architecture.md
  - domain-frontend-development/angular/frontend_angular_reactive_patterns.md
  - domain-frontend-development/angular/frontend_angular_testing.md
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
---

# Angular Signals Advanced Analysis

**Objective:** Audit an Angular application's advanced signals usage — `signal`/`computed`/`effect` correctness, signal-based components, RxJS interop, zoneless change detection, and migration from zone.js patterns — and recommend specific, evidence-backed fixes.

**When to Use:**
- Use when: A codebase mixes signals with zone.js-era patterns (`async` pipe everywhere, manual `ChangeDetectorRef.markForCheck()`) and you want to assess migration health.
- Use when: `effect()` is being used for derived state or to write signals, causing redundant runs or subtle loops.
- Use when: RxJS and signals are bridged with `toSignal`/`toObservable` and you need to confirm the boundary is correct (subscriptions, initial values, cleanup).
- Use when: The app targets (or is migrating to) zoneless change detection and you need to find code that still relies on zone.js to trigger updates.
- Don't use when: The app is fully zone.js-based with no signals adoption and no migration intent — there is nothing signal-specific to audit.

## Instructions

1. **Inventory Signal Usage**
   - List `signal()`, `computed()`, and `effect()` declarations and what each represents (source state, derived value, side effect).
   - Note signal-based component inputs (`input()`), model inputs (`model()`), and queries (`viewChild`/`contentChild` as signals) where used.
   - Flag places where component fields hold plain mutable values that drive the template but are not signals (and so won't trigger zoneless updates).

2. **Audit `computed` Correctness**
   - Confirm `computed()` is pure — it derives a value from signals and performs no side effects or writes.
   - Flag derived state implemented via `effect()` writing to another `signal()` where a `computed()` would be the correct, glitch-free choice.
   - Check that computeds read all the signals they logically depend on (no stale captures of plain variables).

3. **Audit `effect` Usage**
   - Confirm `effect()` is reserved for genuine side effects (logging, DOM/third-party sync, persistence) — not for deriving state.
   - Flag effects that write signals they also read (potential cycles) and confirm intended write-allowance semantics (verify current API for writing inside effects against current docs).
   - Verify cleanup via the provided `onCleanup` for subscriptions/timers, and confirm the effect's injection context / lifecycle is correct.
   - Flag effects doing heavy synchronous work that runs on every dependency change.

4. **Review Signal-Based Components**
   - Confirm signal `input()`s are read as signals (called as functions) and not treated as plain values.
   - For two-way binding, confirm `model()` is used correctly and the parent binding matches.
   - Confirm `OnPush` (or zoneless) compatibility: template state should flow through signals/inputs so change detection is driven correctly.

5. **Analyze RxJS Interop**
   - For `toSignal(obs$)`: confirm an `initialValue` / `requireSync` choice is made deliberately and the consuming template handles the initial state.
   - Confirm `toSignal` is created in an injection context (or given an explicit `injector`) so cleanup is tied to the right lifecycle.
   - For `toObservable(sig)`: confirm downstream operators expect signal-driven emissions and that this isn't reintroducing manual subscription management that signals were meant to remove.
   - Flag round-trips (signal → observable → signal) that add complexity without need.

6. **Assess Zoneless Readiness**
   - Identify code that depends on zone.js to trigger change detection: state mutated outside signals, `setTimeout`/`Promise`/event callbacks updating plain fields expected to refresh the view.
   - Confirm template-driving state is expressed as signals or signal inputs so updates propagate without zone.js.
   - Flag `NgZone.run`/`runOutsideAngular` usage that becomes irrelevant or incorrect under zoneless (verify against current docs for the target Angular version).

7. **Find Migration-from-zone.js Patterns**
   - Flag manual `markForCheck()`/`detectChanges()` calls that signals make unnecessary.
   - Flag `BehaviorSubject` + `async` pipe used purely as local component state where a `signal` is simpler.
   - Distinguish RxJS that should stay (streams, debouncing, cancellation, complex async orchestration) from RxJS used merely as a state container.

8. **CRITICAL: Verify findings before reporting**
   - For each finding, confirm the actual declaration and how the value drives the template before recommending a change. Assign a Confidence level:
     - **High:** The misuse is directly visible (e.g. an `effect` deriving state into a signal, a plain field driving the template under zoneless) and the fix is unambiguous.
     - **Medium:** The pattern is likely wrong but depends on lifecycle, injection context, or version-specific behavior you cannot fully see.
     - **Low:** A heuristic suggestion (e.g. "this `BehaviorSubject` could be a signal") needing author confirmation of how the stream is consumed elsewhere.
   - Do not state version-specific signal/zoneless API behavior as settled fact — note "verify against current docs for the target Angular version."

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Don't recommend replacing RxJS with signals where the stream provides real value (cancellation, debouncing, multi-step async, sharing) — signals are not a stream replacement.
- Don't flag every `effect()` as wrong; genuine side effects belong in effects.
- Don't claim a `computed` is missing a dependency without confirming what it actually reads.
- Don't assert "zoneless-ready" or "not ready" without checking how template state is mutated.
- Don't recommend removing `markForCheck()` until you confirm the surrounding state is signal-driven.
- Don't invent change-detection cycle counts or performance numbers.
- Don't state writing-inside-effects or `requireSync` semantics as fixed fact — phrase as "verify against current docs."

✅ **DO:**
- Distinguish derived state (`computed`) from side effects (`effect`) explicitly for each finding.
- Confirm signal inputs are invoked as functions in templates/TS.
- Cite the exact declaration, binding, or call site as evidence.
- For interop, confirm injection context and initial-value handling.
- Identify the smallest migration step (one component / one field) rather than a sweeping rewrite.
- Keep RxJS where it earns its complexity; recommend signals only for plain state.
- Prioritize by correctness risk (cycles, missed updates under zoneless) over stylistic modernization.

## Expected Output

A structured signals audit with a usage inventory, per-finding detail (severity, confidence, location, evidence, recommendation), zoneless-readiness assessment, and a prioritized remediation list.

- Signal usage inventory
- Per-finding analysis (computed/effect/interop/zoneless)
- Zoneless readiness summary
- Prioritized recommendations by correctness risk

### Output Format

```markdown
## Angular Signals Audit

### Summary
- Signals adoption: <none | partial | broad>
- Zoneless readiness: <ready | gaps | not started>
- Total findings: <n> (High: <n>, Medium: <n>, Low: <n>)

### Signal Usage Inventory
| Symbol | Kind | Role | Concern |
|--------|------|------|---------|
| ... | signal/computed/effect/input | source/derived/side-effect | ... |

### Findings
#### [SEVERITY] <Title>
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** <file:line / component>
- **Evidence:** <exact code construct>
- **Mechanism:** <why it's incorrect or costly>
- **Recommendation:** <specific fix>

### Zoneless Readiness
- <state-driving fields that still rely on zone.js, if any>

### Prioritized Recommendations
1. ...
```

## Example Output

```markdown
## Angular Signals Audit

### Summary
- Signals adoption: partial (inputs + some computeds; effects misused)
- Zoneless readiness: gaps (one plain field drives the template)
- Total findings: 4 (High: 2, Medium: 1, Low: 1)

### Signal Usage Inventory
| Symbol        | Kind     | Role           | Concern |
|---------------|----------|----------------|---------|
| count         | signal   | source         | OK |
| doubled       | effect→signal | derived   | Should be computed |
| user$         | toSignal | interop        | No initial value handling |
| this.total    | plain field | template state | Won't update under zoneless |

### Findings

#### [HIGH] Derived state computed via effect writing a signal
- **Severity:** High
- **Confidence:** High
- **Location:** components/counter.component.ts:18
- **Evidence:**
  ```ts
  doubled = signal(0);
  constructor() {
    effect(() => this.doubled.set(this.count() * 2));
  }
  ```
- **Mechanism:** Using an effect to derive state can produce glitches and extra change-detection passes, and bypasses the dependency graph that `computed` manages.
- **Recommendation:** `doubled = computed(() => this.count() * 2);` — pure, cached, glitch-free; delete the effect.

#### [HIGH] Plain field drives template under a zoneless target
- **Severity:** High
- **Confidence:** Medium
- **Location:** components/dashboard.component.ts:24
- **Evidence:** `setInterval(() => { this.total = compute(); }, 1000)` with `{{ total }}` in the template; app configured for zoneless change detection.
- **Mechanism:** Without zone.js, mutating a plain field does not schedule change detection — the view will not update.
- **Recommendation:** `total = signal(0)` and `this.total.set(compute())`. Verify against current docs for the target Angular version's zoneless API.

#### [MEDIUM] toSignal created without initial value or injection context handling
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** components/profile.component.ts:12
- **Evidence:** `user = toSignal(this.userService.user$);`
- **Mechanism:** Without an `initialValue` (or `requireSync`), the signal is `undefined` until the first emission; templates must handle that, and creation must be in an injection context for cleanup.
- **Recommendation:** Provide an explicit initial value or `requireSync` per the stream's guarantees, and ensure creation occurs in an injection context. Verify semantics against current docs.

#### [LOW] BehaviorSubject + async pipe used as local component state
- **Severity:** Low
- **Confidence:** Low
- **Location:** components/filter.component.ts:9
- **Evidence:** `private filter$ = new BehaviorSubject('all');` consumed only via `filter$ | async` in this component.
- **Mechanism:** A stream is overhead for simple local state with no async orchestration.
- **Recommendation:** Replace with `filter = signal('all')` if no other consumer needs the observable. Confirm the subject isn't subscribed elsewhere first.

### Zoneless Readiness
- One template-driving field (`this.total`) still mutated as a plain property — must become a signal before relying on zoneless.

### Prioritized Recommendations
1. Convert effect-derived state to `computed` (correctness + fewer CD passes).
2. Make the interval-updated field a signal so the view updates under zoneless.
3. Add explicit initial-value handling to the `toSignal` interop.
4. Replace the local-only `BehaviorSubject` with a signal.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Scopes the audit to signal correctness, signal-based components, RxJS interop, and zoneless migration in one sentence.
- **ST-02 (Structured Sequential Instructions):** Moves from inventory → computed/effect correctness → components → interop → zoneless readiness → migration patterns.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates correctness (cycles, glitches), change-detection behavior, interop boundaries, and zoneless readiness as separate dimensions.
- **RT-05 (Evidence-Based Reasoning):** Requires citing the exact declaration or call site and confirming how state drives the template before reporting.
- **DS-06 (Prioritization Guidance):** Orders fixes by correctness risk (missed updates, cycles) ahead of stylistic modernization.

## Related Prompts
- [frontend_angular_architecture.md](frontend_angular_architecture.md) - Position signals within the broader component/module architecture.
- [frontend_angular_reactive_patterns.md](frontend_angular_reactive_patterns.md) - Decide where RxJS stays versus where signals replace it.
- [frontend_angular_testing.md](frontend_angular_testing.md) - Test signal-driven and zoneless components after migration.
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Relate change-detection improvements to interaction metrics.
