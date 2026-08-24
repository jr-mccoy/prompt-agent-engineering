---
title: "iOS Swift Concurrency Safety Review"
category: mobile-development
description: "Review Swift Concurrency for actor isolation correctness, Sendable conformance, MainActor annotation, task cancellation, and data race prevention."
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
  - concurrency
  - async-await
  - sendable
updated: "2026-03-19"
---

# iOS Swift Concurrency Safety Review

**Objective:** Audit Swift Concurrency usage for actor isolation correctness, Sendable conformance completeness, appropriate MainActor annotations, structured task cancellation, and data race prevention to ensure thread safety under strict concurrency checking.

**When to Use:** Apply when enabling strict concurrency checking, reviewing async code, migrating from GCD to structured concurrency, or investigating intermittent crashes and data corruption that suggest data races.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What Swift concurrency checking level is set (minimal, targeted, complete, strict)?
2. Are there custom actors beyond MainActor?
3. Is the codebase migrating from GCD/OperationQueue or greenfield async/await?
4. Are there @unchecked Sendable conformances?

## Instructions

### CRITICAL: Verification Requirements

- All types crossing actor boundaries must conform to Sendable (or be verified as @unchecked Sendable)
- UI updates must occur on @MainActor — verify all view model published property mutations
- Every Task must have a cancellation path or documented reason for being non-cancellable
- No mutable shared state accessed outside actor isolation

### False-Positive Prevention

- ❌ Do NOT flag @unchecked Sendable on types that are internally synchronized (e.g., os_unfair_lock protected)
- ✅ DO flag @unchecked Sendable on types with unprotected mutable state
- ❌ Do NOT flag Task {} in SwiftUI .task modifier — it inherits view's actor context
- ✅ DO flag Task {} in non-isolated contexts where MainActor inheritance is assumed but not guaranteed
- ❌ Do NOT flag actors with synchronous methods — nonisolated methods on actors are valid
- ✅ DO flag nonisolated methods on actors that access actor-isolated state

1. **Actor Isolation**

```swift
// BAD: Mutable state outside actor isolation
class ImageCache {
    var cache: [URL: UIImage] = [:] // unprotected mutable state

    func store(_ image: UIImage, for url: URL) {
        cache[url] = image // data race if called from multiple tasks
    }
}

// GOOD: Actor-isolated state
actor ImageCache {
    private var cache: [URL: UIImage] = [:]

    func store(_ image: UIImage, for url: URL) {
        cache[url] = image // actor-serialized access
    }

    func image(for url: URL) -> UIImage? {
        cache[url]
    }
}
```

2. **Sendable Conformance**

```swift
// BAD: Non-Sendable type passed across actor boundary
class RequestContext {
    var headers: [String: String] = [:] // mutable, non-Sendable
}

func fetchData(context: RequestContext) async throws -> Data {
    // context crosses from caller's isolation to this function's — data race possible
    return try await URLSession.shared.data(from: url).0
}

// GOOD: Value type or immutable Sendable
struct RequestContext: Sendable {
    let headers: [String: String] // immutable — safe to send
}

// Or use @unchecked Sendable with internal synchronization
final class SynchronizedContext: @unchecked Sendable {
    private let lock = NSLock()
    private var _headers: [String: String] = [:]

    var headers: [String: String] {
        lock.withLock { _headers }
    }
}
```

3. **MainActor for UI Updates**

```swift
// BAD: Published property mutated off MainActor
class ProfileViewModel: ObservableObject {
    @Published var name: String = ""

    func load() async {
        let user = try? await api.fetchUser()
        name = user?.name ?? "" // mutation may happen off MainActor — UI update from background
    }
}

// GOOD: MainActor-isolated view model
@MainActor
class ProfileViewModel: ObservableObject {
    @Published var name: String = ""

    func load() async {
        let user = try? await api.fetchUser() // fetch suspends, resumes on MainActor
        name = user?.name ?? "" // guaranteed MainActor
    }
}
```

4. **Task Cancellation**

```swift
// BAD: Task ignores cancellation — continues expensive work
func processImages(_ urls: [URL]) async throws -> [UIImage] {
    var images: [UIImage] = []
    for url in urls {
        let data = try await URLSession.shared.data(from: url).0
        let image = UIImage(data: data)!
        images.append(image)
        // user navigated away but this keeps running
    }
    return images
}

// GOOD: Check for cancellation and support cooperative cancellation
func processImages(_ urls: [URL]) async throws -> [UIImage] {
    var images: [UIImage] = []
    for url in urls {
        try Task.checkCancellation() // throws if task was cancelled
        let (data, _) = try await URLSession.shared.data(from: url) // also checks cancellation
        if let image = UIImage(data: data) {
            images.append(image)
        }
    }
    return images
}

// In the caller:
let task = Task { try await processImages(urls) }
// On view disappear:
task.cancel()
```

## Expected Output

```
## Swift Concurrency Safety Review Report

### Summary
- **Async functions reviewed:** N
- **Actor isolation violations:** N
- **Sendable conformance issues:** N
- **MainActor annotation gaps:** N
- **Missing cancellation paths:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Race condition risk:** Low/Medium/High
- **Recommendation:** ...
```

## Example Output

```
## Swift Concurrency Safety Review Report

### Summary
- **Async functions reviewed:** 22
- **Actor isolation violations:** 2
- **Sendable conformance issues:** 4
- **MainActor annotation gaps:** 3
- **Missing cancellation paths:** 2

### Findings

#### [Critical] Data Race — NetworkCache.swift:L15
- **Issue:** `var responseCache: [URL: Data]` on plain class accessed from multiple async contexts without synchronization.
- **Race condition risk:** High — concurrent read/write causes undefined behavior.
- **Recommendation:** Convert `NetworkCache` to actor or protect with `OSAllocatedUnfairLock`.

#### [Warning] Missing MainActor — SearchViewModel.swift:L8
- **Issue:** Class not annotated `@MainActor` but has `@Published` properties mutated in `async` methods.
- **Recommendation:** Add `@MainActor` to class declaration.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates isolation, Sendable, MainActor, cancellation
- **RT-02 (Role-Based Task Framing):** Reviewer acts as Swift concurrency safety expert
- **RT-04 (Constraint-Based Refinement):** Enforces strict concurrency rules
- **AG-02 (Automated Guardrails):** Prevents false flags on valid @unchecked Sendable and nonisolated patterns

## Related Prompts

- `ios_combine_pipeline_review.md` — Combine threading and subscription safety
- `ios_background_task_review.md` — Background execution and async task management
- `ios_observable_state_management_review.md` — State management thread safety

## Customization Guide

- **Strict concurrency migration:** Add prioritized migration plan for resolving warnings incrementally
- **Server-side Swift:** Add Sendable checks for types shared between request handlers
- **Pre-iOS 17:** Add guidance for back-deploying async/await and actor patterns
