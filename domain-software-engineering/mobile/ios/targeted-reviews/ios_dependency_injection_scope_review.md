---
title: "iOS Dependency Injection Scope Review"
category: mobile-development
description: "Review DI scopes for lifecycle correctness, Environment propagation, circular dependency detection, and test override completeness in iOS applications."
techniques:
  - ST-01
  - RT-02
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - code-review
  - dependency-injection
  - architecture
updated: "2026-03-19"
---

# iOS Dependency Injection Scope Review

**Objective:** Audit dependency injection configuration for lifecycle correctness (singleton vs transient vs scoped), SwiftUI Environment propagation completeness, circular dependency detection, and test override reliability to ensure predictable object graphs in production and testing.

**When to Use:** Apply when reviewing DI container setup, adding new injectable dependencies, debugging retain cycles caused by shared instances, or when tests fail due to missing or stale overrides.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What DI approach is used (manual init injection, @Environment, third-party container like Swinject/Factory)?
2. Are there singleton-scoped dependencies that hold mutable state?
3. How are dependencies overridden in unit and UI tests?
4. Is there a composition root or are dependencies resolved ad-hoc?

## Instructions

### CRITICAL: Verification Requirements

- Every injectable dependency must have a defined lifecycle scope (singleton, transient, scoped)
- SwiftUI @Environment values must be injected at the correct ancestor level
- No circular dependency chains in the object graph
- Every production dependency must be overridable in tests without conditional compilation

### False-Positive Prevention

- ❌ Do NOT flag singleton scope for truly stateless services (e.g., formatters, pure mappers)
- ✅ DO flag singleton scope for services holding mutable state shared across features
- ❌ Do NOT flag @Environment missing in previews — previews may use their own injection
- ✅ DO flag @Environment missing in the live app's view hierarchy
- ❌ Do NOT flag manual init injection as inferior to container-based DI — both are valid
- ✅ DO flag dependencies resolved via global static access (Service.shared) in non-composition-root code

1. **Lifecycle Scope Correctness**

```swift
// BAD: Singleton holds user-specific mutable state
class AuthService {
    static let shared = AuthService()
    var currentUser: User? // persists across logout/login
}

// GOOD: Scoped to authenticated session
class AuthenticatedSession {
    let user: User
    let tokenProvider: TokenProvider
}
// Created at login, discarded at logout — no stale state
```

2. **Environment Propagation**

```swift
// BAD: Environment value not injected — runtime crash
struct SettingsView: View {
    @Environment(\.userPreferences) var prefs
    var body: some View { Text(prefs.theme.name) }
}
// Parent never calls .environment(\.userPreferences, ...)

// GOOD: Environment injected at appropriate ancestor
@main
struct MyApp: App {
    @State private var prefs = UserPreferences.default
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.userPreferences, prefs)
        }
    }
}
```

3. **Circular Dependency Detection**

```swift
// BAD: Circular dependency
class ServiceA {
    let b: ServiceB
    init(b: ServiceB) { self.b = b }
}
class ServiceB {
    let a: ServiceA // cannot construct — infinite loop
    init(a: ServiceA) { self.a = a }
}

// GOOD: Break cycle with protocol or closure
class ServiceA {
    let fetchB: () -> ServiceBProtocol
    init(fetchB: @escaping () -> ServiceBProtocol) { self.fetchB = fetchB }
}
```

4. **Test Override Completeness**

```swift
// BAD: No way to override in tests
class AnalyticsService {
    func track(_ event: String) { /* real analytics call */ }
}
class ViewModel {
    let analytics = AnalyticsService() // hardcoded

}

// GOOD: Protocol-based injection with test override
protocol AnalyticsServiceProtocol {
    func track(_ event: String)
}
class ViewModel {
    private let analytics: AnalyticsServiceProtocol
    init(analytics: AnalyticsServiceProtocol = AnalyticsService()) {
        self.analytics = analytics
    }
}
// Test: ViewModel(analytics: MockAnalytics())
```

## Expected Output

```
## Dependency Injection Scope Review Report

### Summary
- **Dependencies reviewed:** N
- **Lifecycle scope issues:** N
- **Environment propagation gaps:** N
- **Circular dependencies:** N
- **Test override gaps:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Recommendation:** ...
```

## Example Output

```
## Dependency Injection Scope Review Report

### Summary
- **Dependencies reviewed:** 14
- **Lifecycle scope issues:** 2
- **Environment propagation gaps:** 1
- **Circular dependencies:** 0
- **Test override gaps:** 3

### Findings

#### [Critical] Singleton Mutable State — CartService.swift:L8
- **Issue:** `CartService.shared` holds `var items: [CartItem]` as singleton. State persists across user sessions.
- **Recommendation:** Scope to user session. Create new `CartService` at login, release at logout.

#### [Warning] Missing Environment — CheckoutFlow.swift:L22
- **Issue:** `@Environment(\.paymentConfig)` read in `CheckoutView` but never injected by any ancestor in the checkout navigation stack.
- **Recommendation:** Add `.environment(\.paymentConfig, config)` in `CheckoutCoordinator`.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates review into scope, propagation, cycles, testability
- **RT-02 (Role-Based Task Framing):** Reviewer acts as iOS architecture and testability expert
- **AG-02 (Automated Guardrails):** Prevents false flags on valid singletons and manual DI

## Related Prompts

- `ios_observable_state_management_review.md` — State ownership and observation
- `ios_coordinator_navigation_review.md` — Navigation-scoped dependency lifecycles
- `ios_tca_architecture_review.md` — Dependency management in TCA

## Customization Guide

- **Factory/Swinject users:** Add container registration audit and scope verification rules
- **Modular apps:** Check that module boundaries only expose protocols, not concrete types
- **SwiftUI-only apps:** Focus on @Environment and @EnvironmentObject propagation chains
