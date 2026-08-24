---
title: "iOS TCA Architecture Review"
category: mobile-development
description: "Review The Composable Architecture (TCA) for reducer composition correctness, effect cancellation, dependency management, and testing completeness."
techniques:
  - ST-01
  - RT-02
  - RT-04
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - code-review
  - tca
  - composable-architecture
  - state-management
updated: "2026-03-19"
---

# iOS TCA Architecture Review

**Objective:** Audit TCA implementations for correct reducer composition, proper effect cancellation and lifecycle management, dependency injection via @Dependency, and testing coverage of state mutations and effects to ensure maintainable and predictable feature modules.

**When to Use:** Apply when reviewing TCA features, adding new reducers, investigating unexpected state mutations, or validating that effect lifecycles align with view lifecycles. Essential before merging any new TCA feature module.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What version of TCA is the project using (1.x with @Reducer macro or older)?
2. Are features composed using Scope or ifLet/forEach?
3. How are long-running effects (WebSocket, timers) managed?
4. What percentage of reducers have corresponding test coverage?

## Instructions

### CRITICAL: Verification Requirements

- Every reducer action that triggers an effect must handle the effect's response action
- Long-running effects must be cancelled when the parent feature is torn down
- All external dependencies must be declared via @Dependency, not captured from closures
- Every state mutation must be testable via TestStore

### False-Positive Prevention

- ❌ Do NOT flag `.none` returns in action handlers that intentionally perform no side effects
- ✅ DO flag `.none` returns where an effect response action is never handled (dead action)
- ❌ Do NOT flag large State structs if they represent a genuinely complex domain
- ✅ DO flag large State structs with fields that could be derived from other fields
- ❌ Do NOT flag @Dependency usage for lightweight values (UUID generators, date providers)
- ✅ DO flag direct `URLSession.shared` or other uncontrolled dependencies bypassing @Dependency

1. **Reducer Composition**

```swift
// BAD: Monolithic reducer handling unrelated concerns
@Reducer
struct AppFeature {
    struct State { var profile: ProfileState; var settings: SettingsState; var feed: FeedState }
    enum Action { case profile(ProfileAction); case settings(SettingsAction); case feed(FeedAction) }

    var body: some ReducerOf<Self> {
        Reduce { state, action in
            switch action {
            case .profile(.loadTapped):
                // 200 lines of profile logic mixed with settings and feed
            }
        }
    }
}

// GOOD: Composed child reducers
@Reducer
struct AppFeature {
    struct State { var profile: ProfileFeature.State; var settings: SettingsFeature.State }
    enum Action { case profile(ProfileFeature.Action); case settings(SettingsFeature.Action) }

    var body: some ReducerOf<Self> {
        Scope(state: \.profile, action: \.profile) { ProfileFeature() }
        Scope(state: \.settings, action: \.settings) { SettingsFeature() }
    }
}
```

2. **Effect Cancellation**

```swift
// BAD: Long-running effect never cancelled
@Reducer
struct TimerFeature {
    enum CancelID { case timer }

    var body: some ReducerOf<Self> {
        Reduce { state, action in
            switch action {
            case .startTapped:
                return .run { send in
                    for await _ in clock.timer(interval: .seconds(1)) {
                        await send(.tick)
                    }
                }
                // No cancellation ID — runs forever
            }
        }
    }
}

// GOOD: Cancellable with proper teardown
@Reducer
struct TimerFeature {
    enum CancelID { case timer }

    var body: some ReducerOf<Self> {
        Reduce { state, action in
            switch action {
            case .startTapped:
                return .run { send in
                    for await _ in clock.timer(interval: .seconds(1)) {
                        await send(.tick)
                    }
                }
                .cancellable(id: CancelID.timer)
            case .stopTapped, .delegate(.dismiss):
                return .cancel(id: CancelID.timer)
            }
        }
    }
}
```

3. **Dependency Management**

```swift
// BAD: Direct dependency access bypassing TCA
@Reducer
struct SearchFeature {
    var body: some ReducerOf<Self> {
        Reduce { state, action in
            switch action {
            case .searchTapped:
                return .run { send in
                    let results = try await URLSession.shared
                        .data(from: url) // uncontrolled, untestable
                    await send(.resultsLoaded(results))
                }
            }
        }
    }
}

// GOOD: @Dependency injection
@Reducer
struct SearchFeature {
    @Dependency(\.apiClient) var apiClient

    var body: some ReducerOf<Self> {
        Reduce { state, action in
            switch action {
            case .searchTapped:
                return .run { [apiClient] send in
                    let results = try await apiClient.search(state.query)
                    await send(.resultsLoaded(results))
                }
            }
        }
    }
}
```

4. **Testing Completeness**

```swift
// BAD: Test only checks final state, not intermediate mutations
@Test func testLogin() async {
    let store = TestStore(initialState: LoginFeature.State()) {
        LoginFeature()
    }
    await store.send(.loginTapped) // no assertion on state change
}

// GOOD: Assert every state mutation and effect
@Test func testLogin() async {
    let store = TestStore(initialState: LoginFeature.State()) {
        LoginFeature()
    } withDependencies: {
        $0.apiClient.login = { _ in .mock }
    }
    await store.send(.loginTapped) {
        $0.isLoading = true
    }
    await store.receive(\.loginResponse.success) {
        $0.isLoading = false
        $0.user = .mock
    }
}
```

## Expected Output

```
## TCA Architecture Review Report

### Summary
- **Reducers reviewed:** N
- **Composition issues:** N
- **Effect lifecycle issues:** N
- **Dependency violations:** N
- **Test coverage gaps:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Recommendation:** ...
```

## Example Output

```
## TCA Architecture Review Report

### Summary
- **Reducers reviewed:** 9
- **Composition issues:** 1
- **Effect lifecycle issues:** 2
- **Dependency violations:** 1
- **Test coverage gaps:** 3

### Findings

#### [Critical] Uncancelled Effect — ChatFeature.swift:L45
- **Issue:** WebSocket connection effect has no cancellation ID. Runs indefinitely even after navigating away.
- **Recommendation:** Add `.cancellable(id: CancelID.websocket)` and cancel in `.delegate(.dismiss)`.

#### [Warning] Missing Test — ProfileFeature.swift
- **Issue:** `ProfileFeature` has 8 actions but only 2 are tested. `.deleteAccount` path is untested.
- **Recommendation:** Add TestStore test covering `.deleteAccount` flow including confirmation and API call.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates composition, effects, dependencies, testing
- **RT-02 (Role-Based Task Framing):** Reviewer acts as TCA architecture expert
- **RT-04 (Constraint-Based Refinement):** Enforces cancellation, @Dependency, and test completeness
- **AG-02 (Automated Guardrails):** Prevents false flags on valid .none returns and large states

## Related Prompts

- `ios_observable_state_management_review.md` — Non-TCA state management
- `ios_swift_concurrency_safety_review.md` — Async safety in TCA effects
- `ios_dependency_injection_scope_review.md` — General DI patterns

## Customization Guide

- **Navigation in TCA:** Add checks for tree-based vs stack-based navigation state management
- **Large feature modules:** Add checks for feature decomposition signals (>300 line reducers)
- **Shared state:** Add checks for SharedState/PresentationState usage and synchronization
