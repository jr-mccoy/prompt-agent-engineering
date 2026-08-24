---
title: "iOS Combine Pipeline Review"
category: mobile-development
description: "Review Combine pipelines for subscription lifecycle management, AnyCancellable leak prevention, error type propagation, and thread scheduling correctness."
techniques:
  - ST-01
  - RT-02
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - code-review
  - combine
  - reactive
  - concurrency
updated: "2026-03-19"
---

# iOS Combine Pipeline Review

**Objective:** Audit Combine pipeline implementations for subscription lifecycle management, AnyCancellable storage and leak prevention, correct error type propagation through operator chains, and thread scheduling to ensure publishers and subscribers execute on appropriate threads.

**When to Use:** Apply when reviewing Combine-based networking, state management, or event processing code. Essential when investigating memory leaks from retained subscriptions, unexpected thread crashes, or swallowed errors in reactive chains.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. Is Combine used for networking, state observation, UI binding, or all three?
2. Are there long-lived subscriptions (timers, WebSocket, NotificationCenter)?
3. What is the cancellable storage pattern (Set<AnyCancellable>, individual properties)?
4. Is the project migrating from Combine to async/await?

## Instructions

### CRITICAL: Verification Requirements

- Every .sink or .assign subscription must store its AnyCancellable
- Long-lived subscriptions must be explicitly cancelled on deallocation or scope exit
- Error types must not be erased to Never unless errors are genuinely handled
- UI-bound subscribers must receive values on the main thread

### False-Positive Prevention

- ❌ Do NOT flag `.eraseToAnyPublisher()` as always bad — it is needed for type-erased APIs
- ✅ DO flag `.eraseToAnyPublisher()` in the middle of a chain where concrete types would enable optimization
- ❌ Do NOT flag `receive(on: DispatchQueue.main)` in view models — this is correct for UI updates
- ✅ DO flag `receive(on: DispatchQueue.main)` applied too early in a chain (before heavy computation)
- ❌ Do NOT flag `.store(in: &cancellables)` with Set<AnyCancellable> — this is the standard pattern
- ✅ DO flag .sink without storing the returned AnyCancellable at all

1. **Subscription Lifecycle**

```swift
// BAD: Cancellable not stored — subscription immediately cancelled
func loadData() {
    URLSession.shared.dataTaskPublisher(for: url)
        .map(\.data)
        .decode(type: User.self, decoder: JSONDecoder())
        .sink(
            receiveCompletion: { _ in },
            receiveValue: { user in self.user = user }
        )
    // AnyCancellable returned but not stored — immediately deallocated, subscription cancelled
}

// GOOD: Store cancellable
private var cancellables = Set<AnyCancellable>()

func loadData() {
    URLSession.shared.dataTaskPublisher(for: url)
        .map(\.data)
        .decode(type: User.self, decoder: JSONDecoder())
        .sink(
            receiveCompletion: { _ in },
            receiveValue: { [weak self] user in self?.user = user }
        )
        .store(in: &cancellables)
}
```

2. **Error Propagation**

```swift
// BAD: Error silently replaced with empty value — failures invisible
func searchPublisher(query: String) -> AnyPublisher<[Result], Never> {
    api.search(query)
        .replaceError(with: []) // search failures silently return empty
        .eraseToAnyPublisher()
}

// GOOD: Propagate errors to caller
func searchPublisher(query: String) -> AnyPublisher<[Result], APIError> {
    api.search(query)
        .mapError { APIError.network($0) }
        .eraseToAnyPublisher()
}

// Or handle with explicit error state
func searchPublisher(query: String) -> AnyPublisher<Swift.Result<[Result], APIError>, Never> {
    api.search(query)
        .map { Swift.Result.success($0) }
        .catch { Just(.failure(APIError.network($0))) }
        .eraseToAnyPublisher()
}
```

3. **Thread Scheduling**

```swift
// BAD: Heavy computation on main thread
URLSession.shared.dataTaskPublisher(for: url)
    .map(\.data)
    .receive(on: DispatchQueue.main) // switches to main BEFORE decoding
    .decode(type: LargePayload.self, decoder: JSONDecoder()) // blocks main thread
    .sink(receiveCompletion: { _ in }, receiveValue: { self.data = $0 })
    .store(in: &cancellables)

// GOOD: Heavy work on background, UI update on main
URLSession.shared.dataTaskPublisher(for: url)
    .map(\.data)
    .decode(type: LargePayload.self, decoder: JSONDecoder()) // on URLSession's background queue
    .receive(on: DispatchQueue.main) // switch to main only for UI update
    .sink(receiveCompletion: { _ in }, receiveValue: { [weak self] in self?.data = $0 })
    .store(in: &cancellables)
```

4. **Memory Leaks in Closures**

```swift
// BAD: Strong self capture in long-lived subscription
NotificationCenter.default.publisher(for: .userDidUpdate)
    .sink { _ in
        self.refreshProfile() // strong capture — self never deallocated
    }
    .store(in: &cancellables)

// GOOD: Weak self capture
NotificationCenter.default.publisher(for: .userDidUpdate)
    .sink { [weak self] _ in
        self?.refreshProfile()
    }
    .store(in: &cancellables)
```

## Expected Output

```
## Combine Pipeline Review Report

### Summary
- **Pipelines reviewed:** N
- **Subscription lifecycle issues:** N
- **Error propagation gaps:** N
- **Thread scheduling issues:** N
- **Memory leak risks:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Recommendation:** ...
```

## Example Output

```
## Combine Pipeline Review Report

### Summary
- **Pipelines reviewed:** 16
- **Subscription lifecycle issues:** 2
- **Error propagation gaps:** 3
- **Thread scheduling issues:** 1
- **Memory leak risks:** 2

### Findings

#### [Critical] Dropped Cancellable — SyncManager.swift:L45
- **Issue:** `.sink` return value not stored. Remote config fetch subscription immediately cancelled.
- **Recommendation:** Store in `cancellables` set or assign to dedicated property.

#### [Warning] Strong Capture — NotificationHandler.swift:L78
- **Issue:** Strong `self` captured in NotificationCenter subscription. Subscription lives until app termination.
- **Recommendation:** Use `[weak self]` capture list in `.sink` closure.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates lifecycle, errors, threading, memory
- **RT-02 (Role-Based Task Framing):** Reviewer acts as Combine reactive programming expert
- **AG-02 (Automated Guardrails):** Prevents false flags on standard patterns like .store(in:)

## Related Prompts

- `ios_swift_concurrency_safety_review.md` — Async/await concurrency patterns
- `ios_observable_state_management_review.md` — State management with @Published
- `ios_background_task_review.md` — Background execution scheduling

## Customization Guide

- **Migration to async/await:** Add side-by-side comparison of Combine pipelines and async equivalents
- **Custom publishers:** Add checks for demand management and backpressure handling
- **Testing:** Add XCTestExpectation patterns for testing Combine pipelines
