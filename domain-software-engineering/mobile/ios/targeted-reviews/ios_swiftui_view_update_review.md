---
title: "iOS SwiftUI View Update Review"
category: mobile-development
description: "Review view body invalidation for unnecessary redraws, state read scope, Equatable conformance, and @State vs @Binding ownership correctness."
techniques:
  - ST-01
  - RT-02
  - RT-04
  - AG-02
  - AG-12
difficulty: advanced
tags:
  - ios
  - swift
  - code-review
  - swiftui
  - performance
  - view-updates
updated: "2026-03-19"
---

# iOS SwiftUI View Update Review

**Objective:** Audit SwiftUI views for unnecessary body evaluations caused by broad state reads, missing Equatable conformance, incorrect state ownership, and identity instability to ensure minimal view recomputation and smooth 60/120fps rendering.

**When to Use:** Apply when investigating UI jank, excessive CPU usage during idle screens, or when Instruments shows frequent body evaluations. Essential for list-heavy screens and complex view hierarchies.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What SwiftUI version and deployment target (iOS 16 vs 17+ for Observation)?
2. Are there views with complex body computations (sorting, filtering, formatting)?
3. Is the app using @Observable (iOS 17+) or @ObservableObject?
4. Are there known performance issues on specific screens?

## Instructions

### CRITICAL: Verification Requirements

- Every view body must only read the state properties it actually renders
- Views with stable identity should conform to Equatable when body is expensive
- @State must only be used for view-private state; shared state uses @Binding or @Environment
- View identity must be stable across body re-evaluations (no inline closures or random IDs)

### False-Positive Prevention

- ❌ Do NOT flag simple views (< 5 subviews) for missing Equatable — overhead is negligible
- ✅ DO flag views with expensive body computations that lack Equatable
- ❌ Do NOT flag @Observable property reads — the framework tracks granularly
- ✅ DO flag @ObservableObject with multiple @Published properties read in a single large body
- ❌ Do NOT flag body evaluations triggered by actual state changes the user sees
- ✅ DO flag body evaluations triggered by state changes invisible to the user

1. **State Read Scope**

```swift
// BAD: Reads entire model, body re-evaluated on any change
struct HeaderView: View {
    @ObservedObject var viewModel: DashboardViewModel
    var body: some View {
        Text(viewModel.title) // also redraws when viewModel.items changes
    }
}

// GOOD: Narrow the read scope
struct HeaderView: View {
    let title: String // only redraws when title actually changes
    var body: some View {
        Text(title)
    }
}
// Parent: HeaderView(title: viewModel.title)
```

2. **Equatable Conformance**

```swift
// BAD: Expensive body re-evaluated even when inputs unchanged
struct ChartView: View {
    let dataPoints: [DataPoint]
    var body: some View {
        Canvas { context, size in
            // expensive path drawing for hundreds of points
            for point in dataPoints {
                let path = computePath(point, in: size)
                context.stroke(path, with: .color(.blue))
            }
        }
    }
}

// GOOD: Equatable skips body when data unchanged
struct ChartView: View, Equatable {
    let dataPoints: [DataPoint]

    static func == (lhs: Self, rhs: Self) -> Bool {
        lhs.dataPoints == rhs.dataPoints
    }

    var body: some View {
        Canvas { context, size in
            for point in dataPoints {
                let path = computePath(point, in: size)
                context.stroke(path, with: .color(.blue))
            }
        }
    }
}
```

3. **Identity Stability**

```swift
// BAD: Unstable identity causes full view teardown/rebuild
struct ItemList: View {
    let items: [Item]
    var body: some View {
        ForEach(items, id: \.self) { item in // value-based identity changes on mutation
            ItemRow(item: item)
        }
    }
}

// GOOD: Stable identity via unique ID
struct ItemList: View {
    let items: [Item]
    var body: some View {
        ForEach(items, id: \.id) { item in // stable UUID identity
            ItemRow(item: item)
        }
    }
}
```

4. **Avoiding Hidden Redraws**

```swift
// BAD: Inline closure creates new value every body evaluation
struct ParentView: View {
    @State private var count = 0
    var body: some View {
        ChildView(action: { print(count) }) // new closure each evaluation
    }
}

// BAD: Computed property in body forces redraw
struct FormView: View {
    @State private var text = ""
    var body: some View {
        let isValid = text.count > 3 // recomputed every body eval
        TextField("Name", text: $text)
        Button("Submit") {}.disabled(!isValid)
    }
}

// GOOD: Derive in a focused subview
struct SubmitButton: View {
    let textCount: Int
    var body: some View {
        Button("Submit") {}.disabled(textCount <= 3)
    }
}
```

## Expected Output

```
## SwiftUI View Update Review Report

### Summary
- **Views reviewed:** N
- **Unnecessary redraw sites:** N
- **Missing Equatable candidates:** N
- **Identity instability issues:** N
- **State ownership violations:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Impact:** Estimated extra body evaluations per second: N
- **Recommendation:** ...
```

## Example Output

```
## SwiftUI View Update Review Report

### Summary
- **Views reviewed:** 18
- **Unnecessary redraw sites:** 4
- **Missing Equatable candidates:** 2
- **Identity instability issues:** 1
- **State ownership violations:** 1

### Findings

#### [Critical] Broad State Read — FeedView.swift:L15
- **Issue:** `@ObservedObject var vm: FeedViewModel` read in body, but only `vm.feedItems` used. `vm.userProfile` and `vm.filters` changes also trigger body.
- **Impact:** ~30 extra body evaluations per scroll session from profile badge updates.
- **Recommendation:** Pass `vm.feedItems` as parameter or extract into focused sub-view.

#### [Warning] Missing Equatable — MapOverlay.swift:L8
- **Issue:** `MapOverlay` renders 500+ annotation pins. No Equatable conformance.
- **Recommendation:** Add Equatable comparing annotation count and bounding region.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates read scope, equatable, identity, hidden redraws
- **RT-02 (Role-Based Task Framing):** Reviewer acts as SwiftUI rendering performance expert
- **RT-04 (Constraint-Based Refinement):** Enforces minimal state reads and stable identity
- **AG-02 (Automated Guardrails):** Prevents false flags on simple views and @Observable
- **AG-12 (Performance-Aware Review):** Focuses on rendering frame budget impact

## Related Prompts

- `ios_observable_state_management_review.md` — State management correctness
- `ios_swiftui_list_performance_review.md` — List-specific performance
- `ios_core_animation_hitch_review.md` — Layer-level rendering performance

## Customization Guide

- **iOS 17+ only:** Remove @ObservableObject checks, focus on @Observable tracking boundaries
- **Instruments integration:** Add Self._printChanges() debugging instructions for body tracking
- **Accessibility:** Ensure Equatable checks don't skip accessibility property changes
