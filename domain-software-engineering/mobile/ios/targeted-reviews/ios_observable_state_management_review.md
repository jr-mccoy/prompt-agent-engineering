---
title: "iOS Observable State Management Review"
category: mobile-development
description: "Review @Observable and @ObservableObject usage for ownership correctness, excessive observation, state derivation, and view update granularity in SwiftUI applications."
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
  - swiftui
  - state-management
  - observation
updated: "2026-03-19"
---

# iOS Observable State Management Review

**Objective:** Audit SwiftUI state management for correctness and performance by reviewing @Observable/@ObservableObject ownership, observation scope, state derivation patterns, and view update granularity to prevent unnecessary re-renders and state inconsistencies.

**When to Use:** Apply during code reviews of SwiftUI features that introduce or modify view models, shared state objects, or any @Observable/@ObservableObject types. Particularly valuable when investigating unexpected view redraws, stale UI, or memory growth tied to observation.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What iOS deployment target is the project using? (Determines @Observable vs @ObservableObject availability)
2. Is the project using the Observation framework (@Observable) or the Combine-based (@ObservableObject) pattern?
3. Are there shared state objects accessed by multiple views or features?
4. What is the view hierarchy depth where state is passed or observed?

## Instructions

### CRITICAL: Verification Requirements

- Confirm every @Published / @Observable property is actually read by at least one view body
- Verify state ownership: exactly one source of truth per piece of state
- Check that derived state uses computed properties, not stored duplicates
- Validate that observation scope matches the minimum required view subtree

### False-Positive Prevention

- ❌ Do NOT flag @Published properties used only in Combine pipelines outside view bodies — these are valid non-view consumers
- ✅ DO flag @Published properties never read in any view body or Combine chain
- ❌ Do NOT flag @State for value types owned by a single view — this is correct ownership
- ✅ DO flag @StateObject / @State used for shared state that should be injected
- ❌ Do NOT flag @Observable classes with many properties if each property is read by different views — granular tracking handles this
- ✅ DO flag @ObservableObject classes with many @Published properties read in a single view body causing full redraws

1. **Ownership Correctness**
   - Verify each stateful property has a single owner and consumers use @Binding or @Environment

```swift
// BAD: Duplicate source of truth
struct ParentView: View {
    @State private var count = 0
    var body: some View {
        ChildView(count: count) // passes value, not binding
    }
}
struct ChildView: View {
    @State var count: Int // creates second source of truth
}

// GOOD: Single source of truth with binding
struct ParentView: View {
    @State private var count = 0
    var body: some View {
        ChildView(count: $count)
    }
}
struct ChildView: View {
    @Binding var count: Int
}
```

2. **Excessive Observation**
   - Check that views only observe the properties they render

```swift
// BAD: View observes entire object but reads one field
@Observable class UserProfile {
    var name: String = ""
    var avatar: Data = Data()
    var settings: Settings = .default
}
struct NameLabel: View {
    var profile: UserProfile // @Observable tracks all access — OK in Observation framework
    var body: some View { Text(profile.name) }
}

// BAD (ObservableObject): Redraws on ANY @Published change
class UserProfileVM: ObservableObject {
    @Published var name: String = ""
    @Published var avatar: Data = Data()
}
struct NameLabel: View {
    @ObservedObject var vm: UserProfileVM
    var body: some View { Text(vm.name) } // redraws when avatar changes too
}

// GOOD (ObservableObject): Split into focused view models
class NameVM: ObservableObject {
    @Published var name: String = ""
}
```

3. **State Derivation**
   - Ensure derived values are computed, not stored and manually synchronized

```swift
// BAD: Stored derived state
@Observable class CartViewModel {
    var items: [Item] = []
    var totalPrice: Decimal = 0 // manually updated — can drift

    func addItem(_ item: Item) {
        items.append(item)
        totalPrice = items.reduce(0) { $0 + $1.price }
    }
}

// GOOD: Computed derived state
@Observable class CartViewModel {
    var items: [Item] = []
    var totalPrice: Decimal {
        items.reduce(0) { $0 + $1.price }
    }
}
```

4. **View Update Granularity**
   - Confirm parent views do not force child redraws unnecessarily

```swift
// BAD: Inline closure recreates child identity every body eval
struct ListView: View {
    @State private var items: [Item] = []
    var body: some View {
        ForEach(items) { item in
            ItemRow(item: item, onTap: { handleTap(item) }) // new closure each time
        }
    }
}

// GOOD: Equatable conformance + stable references
struct ItemRow: View, Equatable {
    let item: Item
    let onTap: () -> Void
    static func == (lhs: Self, rhs: Self) -> Bool {
        lhs.item.id == rhs.item.id
    }
}
```

## Expected Output

```
## Observable State Management Review Report

### Summary
- **Files reviewed:** N
- **Ownership violations:** N (Critical / Warning)
- **Excessive observation sites:** N
- **Stored derived state instances:** N
- **Unnecessary redraw triggers:** N

### Findings

#### [Critical] Ownership Violation — FileName.swift:L##
- **Issue:** ...
- **Impact:** ...
- **Recommendation:** ...

#### [Warning] Excessive Observation — FileName.swift:L##
- **Issue:** ...
- **Recommendation:** ...

### Recommendations
1. ...
```

## Example Output

```
## Observable State Management Review Report

### Summary
- **Files reviewed:** 12
- **Ownership violations:** 2 (1 Critical / 1 Warning)
- **Excessive observation sites:** 3
- **Stored derived state instances:** 1
- **Unnecessary redraw triggers:** 2

### Findings

#### [Critical] Ownership Violation — ProfileEditor.swift:L45
- **Issue:** `@State var bio: String` in `ProfileEditor` duplicates `UserProfile.bio` instead of binding.
- **Impact:** Edits lost when parent redraws; UI shows stale data.
- **Recommendation:** Change to `@Binding var bio: String` and pass `$profile.bio` from parent.

#### [Warning] Excessive Observation — DashboardView.swift:L12
- **Issue:** `@ObservedObject var appState: AppState` observed, but only `appState.unreadCount` is read. 14 other @Published properties trigger redraws.
- **Recommendation:** Extract `unreadCount` into a focused `UnreadCountVM` or migrate to @Observable.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Breaks review into ownership, observation scope, derivation, and granularity
- **RT-02 (Role-Based Task Framing):** Positions reviewer as SwiftUI state management specialist
- **RT-04 (Constraint-Based Refinement):** Sets strict rules for ownership and derivation correctness
- **AG-02 (Automated Guardrails):** False-positive prevention list prevents over-flagging valid patterns

## Related Prompts

- `ios_swiftui_view_update_review.md` — Focused on body invalidation and redraw analysis
- `ios_tca_architecture_review.md` — State management in The Composable Architecture
- `ios_dependency_injection_scope_review.md` — DI and Environment-based state propagation

## Customization Guide

- **UIKit hybrid projects:** Add checks for KVO observation cleanup and NotificationCenter state sync
- **Observation framework only:** Remove @ObservableObject checks and focus on @Observable tracking granularity
- **Large teams:** Add naming convention checks for view models (e.g., `*ViewModel` suffix requirement)
