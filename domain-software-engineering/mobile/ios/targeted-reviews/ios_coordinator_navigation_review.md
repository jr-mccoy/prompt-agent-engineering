---
title: "iOS Coordinator Navigation Review"
category: mobile-development
description: "Review Coordinator/Router patterns for memory management, deep link routing, NavigationPath type safety, and modal lifecycle correctness."
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
  - navigation
  - coordinator-pattern
updated: "2026-03-19"
---

# iOS Coordinator Navigation Review

**Objective:** Audit navigation architecture for memory leak prevention in coordinator/router patterns, deep link routing completeness, NavigationPath type safety, and correct modal presentation/dismissal lifecycle to prevent orphaned view controllers or broken navigation stacks.

**When to Use:** Apply when reviewing navigation refactors, adding deep link support, migrating from UIKit navigation to SwiftUI NavigationStack, or investigating navigation-related memory leaks and broken back-stack states.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. Is the app using UIKit coordinators, SwiftUI NavigationStack, or a hybrid approach?
2. Does the app support deep linking or Universal Links?
3. Are modal flows (sheets, full-screen covers) managed by coordinators or inline?
4. What is the expected navigation depth and branching complexity?

## Instructions

### CRITICAL: Verification Requirements

- Coordinators must not retain child coordinators after their flow completes
- NavigationPath mutations must only use Hashable/Codable types registered with navigationDestination
- Deep link routing must handle every registered URL pattern or explicitly reject unknown patterns
- Modal presentation must pair every present with a dismiss path

### False-Positive Prevention

- ❌ Do NOT flag view-local @State navigation (sheets, alerts) as needing coordinator management for simple cases
- ✅ DO flag multi-step modal flows without coordinator oversight
- ❌ Do NOT flag NavigationLink with value: as problematic — this is the modern pattern
- ✅ DO flag NavigationLink(destination:) in NavigationStack contexts — deprecated pattern
- ❌ Do NOT flag coordinators holding strong references to their parent's navigation controller if they don't own it
- ✅ DO flag coordinators holding strong references to child coordinators without cleanup on completion

1. **Memory Management**

```swift
// BAD: Child coordinator never released
class ParentCoordinator {
    var children: [Coordinator] = []

    func showSettings() {
        let child = SettingsCoordinator()
        children.append(child)
        child.start() // child never removed from array on completion
    }
}

// GOOD: Cleanup on child completion
class ParentCoordinator {
    var children: [Coordinator] = []

    func showSettings() {
        let child = SettingsCoordinator()
        children.append(child)
        child.onFinish = { [weak self] in
            self?.children.removeAll { $0 === child }
        }
        child.start()
    }
}
```

2. **NavigationPath Type Safety**

```swift
// BAD: Unregistered type in NavigationPath
@Observable class Router {
    var path = NavigationPath()
    func showProfile(_ user: User) {
        path.append(user) // User not registered with navigationDestination
    }
}

// GOOD: All types registered
struct ContentView: View {
    @State private var router = Router()
    var body: some View {
        NavigationStack(path: $router.path) {
            HomeView()
                .navigationDestination(for: User.self) { user in
                    ProfileView(user: user)
                }
                .navigationDestination(for: Settings.self) { settings in
                    SettingsView(settings: settings)
                }
        }
    }
}
```

3. **Deep Link Routing**

```swift
// BAD: Partial deep link handling — unknown paths silently ignored
func handle(url: URL) {
    if url.path == "/profile" { showProfile() }
    // /settings, /orders, etc. silently dropped
}

// GOOD: Exhaustive routing with fallback
enum DeepLink: String, CaseIterable {
    case profile = "/profile"
    case settings = "/settings"
    case orders = "/orders"
}

func handle(url: URL) -> Bool {
    guard let link = DeepLink(rawValue: url.path) else {
        logger.warning("Unhandled deep link: \(url.path)")
        return false
    }
    switch link {
    case .profile: router.push(.profile)
    case .settings: router.push(.settings)
    case .orders: router.push(.orders)
    }
    return true
}
```

4. **Modal Lifecycle**

```swift
// BAD: No dismiss path for presented modal
struct CheckoutView: View {
    @State private var showPayment = false
    var body: some View {
        Button("Pay") { showPayment = true }
            .sheet(isPresented: $showPayment) {
                PaymentView() // no way to dismiss from PaymentView
            }
    }
}

// GOOD: Dismiss path provided
struct CheckoutView: View {
    @State private var showPayment = false
    var body: some View {
        Button("Pay") { showPayment = true }
            .sheet(isPresented: $showPayment) {
                PaymentView(onComplete: { showPayment = false })
            }
    }
}
```

## Expected Output

```
## Coordinator Navigation Review Report

### Summary
- **Navigation components reviewed:** N
- **Memory management issues:** N
- **Type safety violations:** N
- **Deep link coverage gaps:** N
- **Modal lifecycle issues:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Recommendation:** ...
```

## Example Output

```
## Coordinator Navigation Review Report

### Summary
- **Navigation components reviewed:** 8
- **Memory management issues:** 1
- **Type safety violations:** 2
- **Deep link coverage gaps:** 4 unhandled paths
- **Modal lifecycle issues:** 1

### Findings

#### [Critical] Coordinator Leak — OnboardingCoordinator.swift:L34
- **Issue:** `OnboardingCoordinator` appended to parent's `children` array but never removed on flow completion.
- **Recommendation:** Add `onFinish` callback that removes coordinator from parent's array.

#### [Warning] Unregistered Navigation Type — OrderRouter.swift:L18
- **Issue:** `OrderDetail` pushed to `NavigationPath` but no `.navigationDestination(for: OrderDetail.self)` registered.
- **Recommendation:** Register destination in the NavigationStack root or verify type is handled.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates memory, type safety, routing, modal lifecycle
- **RT-02 (Role-Based Task Framing):** Reviewer acts as iOS navigation architecture specialist
- **RT-04 (Constraint-Based Refinement):** Enforces exhaustive routing and paired present/dismiss
- **AG-02 (Automated Guardrails):** Prevents false flags on simple view-local navigation

## Related Prompts

- `ios_dependency_injection_scope_review.md` — Navigation-scoped DI lifecycles
- `ios_universal_link_deep_link_review.md` — Universal Link routing implementation
- `ios_observable_state_management_review.md` — Router state management

## Customization Guide

- **UIKit-only apps:** Focus on UINavigationController push/pop balance and coordinator child cleanup
- **SwiftUI-only apps:** Focus on NavigationPath, navigationDestination registration, and sheet lifecycle
- **Tab-based apps:** Add tab coordinator orchestration and cross-tab deep link routing checks
