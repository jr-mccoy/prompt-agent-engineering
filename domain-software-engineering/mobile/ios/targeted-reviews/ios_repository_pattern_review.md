---
title: "iOS Repository Pattern Review"
category: mobile-development
description: "Review repository layer for protocol abstractions, async data source coordination, caching strategies, and error propagation in iOS applications."
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
  - architecture
  - repository-pattern
  - data-layer
updated: "2026-03-19"
---

# iOS Repository Pattern Review

**Objective:** Audit the repository layer implementation for clean protocol abstractions, correct async data source coordination between local and remote sources, caching coherency, and structured error propagation that surfaces actionable information to callers.

**When to Use:** Apply when reviewing data layer code, introducing new repository types, refactoring networking/persistence layers, or investigating data consistency bugs between local cache and remote API responses.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What networking library is used (URLSession, Alamofire, custom)?
2. What local persistence is used (Core Data, SwiftData, UserDefaults, file system)?
3. Are repositories injected via protocol or concrete type?
4. Is there a shared caching strategy or per-repository caching?

## Instructions

### CRITICAL: Verification Requirements

- Every repository must be defined as a protocol with an async concrete implementation
- Data source coordination must handle offline-first, remote-first, or cache-then-network explicitly
- Error types must preserve upstream context (HTTP status, persistence error, network error)
- Caching invalidation must be deterministic, not time-based only

### False-Positive Prevention

- ❌ Do NOT flag repositories without caching if the data is inherently non-cacheable (e.g., one-time auth tokens)
- ✅ DO flag repositories that cache user-mutable data without invalidation hooks
- ❌ Do NOT flag concrete repository usage in composition roots — DI containers may resolve concretely
- ✅ DO flag concrete repository usage in view models or use cases
- ❌ Do NOT flag simple pass-through repositories with a single data source — not every repo needs coordination
- ✅ DO flag repositories that silently swallow remote errors and return stale cache without signaling staleness

1. **Protocol Abstraction**

```swift
// BAD: View model depends on concrete repository
class OrdersViewModel {
    let repo = OrdersRepository() // untestable, tightly coupled
}

// GOOD: Protocol-based injection
protocol OrdersRepositoryProtocol: Sendable {
    func fetchOrders() async throws -> [Order]
}

final class OrdersRepository: OrdersRepositoryProtocol {
    func fetchOrders() async throws -> [Order] { ... }
}

class OrdersViewModel {
    private let repo: OrdersRepositoryProtocol
    init(repo: OrdersRepositoryProtocol) { self.repo = repo }
}
```

2. **Async Data Source Coordination**

```swift
// BAD: No coordination — cache and remote run independently
func getProducts() async throws -> [Product] {
    if let cached = cache.get() { return cached }
    return try await api.fetchProducts()
}

// GOOD: Cache-then-network with update
func getProducts() -> AsyncStream<[Product]> {
    AsyncStream { continuation in
        if let cached = cache.get() {
            continuation.yield(cached)
        }
        do {
            let remote = try await api.fetchProducts()
            cache.set(remote)
            continuation.yield(remote)
        } catch {
            if cache.get() == nil {
                continuation.finish(throwing: error)
            }
        }
        continuation.finish()
    }
}
```

3. **Error Propagation**

```swift
// BAD: Errors lose context
func fetchUser() async throws -> User {
    do {
        return try await api.getUser()
    } catch {
        throw AppError.generic // upstream context lost
    }
}

// GOOD: Errors preserve context
enum RepositoryError: Error {
    case network(URLError)
    case decoding(DecodingError)
    case persistence(CoreDataError)
    case notFound(resourceId: String)
}

func fetchUser(id: String) async throws(RepositoryError) -> User {
    do {
        return try await api.getUser(id: id)
    } catch let error as URLError {
        throw .network(error)
    } catch let error as DecodingError {
        throw .decoding(error)
    }
}
```

4. **Cache Coherency**

```swift
// BAD: Time-based only, no invalidation on mutation
class ProductCache {
    private var data: [Product]?
    private var timestamp: Date?
    func get() -> [Product]? {
        guard let ts = timestamp, Date().timeIntervalSince(ts) < 300 else { return nil }
        return data
    }
}

// GOOD: Invalidation on mutation + time-based fallback
class ProductCache {
    private var data: [Product]?
    private var timestamp: Date?

    func get(maxAge: TimeInterval = 300) -> [Product]? {
        guard let ts = timestamp, Date().timeIntervalSince(ts) < maxAge else { return nil }
        return data
    }

    func invalidate() { data = nil; timestamp = nil }
    func set(_ products: [Product]) { data = products; timestamp = Date() }
}

// Repository invalidates on writes
func updateProduct(_ product: Product) async throws {
    try await api.update(product)
    cache.invalidate()
}
```

## Expected Output

```
## Repository Pattern Review Report

### Summary
- **Repositories reviewed:** N
- **Abstraction violations:** N
- **Coordination issues:** N
- **Error propagation gaps:** N
- **Cache coherency risks:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Impact:** ...
- **Recommendation:** ...
```

## Example Output

```
## Repository Pattern Review Report

### Summary
- **Repositories reviewed:** 6
- **Abstraction violations:** 2
- **Coordination issues:** 1
- **Error propagation gaps:** 3
- **Cache coherency risks:** 1

### Findings

#### [Critical] Concrete Dependency — CheckoutViewModel.swift:L23
- **Issue:** `PaymentRepository()` instantiated directly in view model.
- **Impact:** Cannot substitute mock in tests; tightly coupled to network layer.
- **Recommendation:** Inject `PaymentRepositoryProtocol` via initializer.

#### [Warning] Silent Stale Cache — ProductRepository.swift:L67
- **Issue:** Remote fetch failure returns cached data without staleness indicator.
- **Impact:** User sees outdated prices without knowing data is stale.
- **Recommendation:** Return `CacheResult<[Product]>` with `.stale(data, age)` case.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Breaks review into abstraction, coordination, errors, caching
- **RT-02 (Role-Based Task Framing):** Reviewer acts as iOS data layer architect
- **RT-04 (Constraint-Based Refinement):** Enforces protocol-first and deterministic invalidation
- **AG-02 (Automated Guardrails):** Prevents false flags on valid simple repositories

## Related Prompts

- `ios_core_data_query_review.md` — Persistence layer efficiency
- `ios_swift_concurrency_safety_review.md` — Async safety in repository implementations
- `ios_dependency_injection_scope_review.md` — DI lifecycle for repository instances

## Customization Guide

- **GraphQL backends:** Add checks for query deduplication and normalized cache (Apollo)
- **Offline-first apps:** Emphasize local-write-first with sync queue patterns
- **Microservice backends:** Add checks for repository fan-out and partial failure handling
