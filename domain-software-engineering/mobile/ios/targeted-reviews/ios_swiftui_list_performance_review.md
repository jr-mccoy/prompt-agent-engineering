---
title: "iOS SwiftUI List Performance Review"
category: mobile-development
description: "Review LazyVStack/List performance for cell identity stability, prefetching, onAppear/onDisappear correctness, and pagination implementation."
techniques:
  - ST-01
  - RT-02
  - AG-02
  - AG-12
difficulty: advanced
tags:
  - ios
  - swift
  - code-review
  - swiftui
  - performance
  - lists
updated: "2026-03-19"
---

# iOS SwiftUI List Performance Review

**Objective:** Audit SwiftUI list implementations for smooth scrolling by reviewing cell identity stability, lazy loading correctness, prefetching strategies, onAppear/onDisappear side effect management, and pagination implementation to prevent jank, excessive memory use, and data loading gaps.

**When to Use:** Apply when reviewing any scrollable content with more than ~50 items, investigating scroll hitches, or when memory grows unbounded during scrolling. Critical for feeds, search results, and data-heavy table views.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. How many items are typically displayed (10s, 100s, 1000s)?
2. Are cells homogeneous or heterogeneous (mixed content types)?
3. Is data paginated from a backend API or loaded entirely in memory?
4. Do cells contain images, async content, or complex subviews?

## Instructions

### CRITICAL: Verification Requirements

- Cell identity must use stable, unique identifiers — not array indices or hashable value types
- LazyVStack/LazyHStack must be used inside ScrollView for large data sets, not VStack
- onAppear must not trigger redundant network requests on rapid scroll
- Pagination must prefetch before the user reaches the end of current data

### False-Positive Prevention

- ❌ Do NOT flag VStack for small, bounded lists (< 20 items) — laziness overhead may not be worth it
- ✅ DO flag VStack for unbounded or large data sets
- ❌ Do NOT flag List over LazyVStack when platform features (swipe actions, edit mode) are needed
- ✅ DO flag List used purely for performance when LazyVStack with custom styling would suffice
- ❌ Do NOT flag onAppear triggers for items that genuinely need loading
- ✅ DO flag onAppear triggers that re-fetch already loaded and cached data

1. **Cell Identity Stability**

```swift
// BAD: Index-based identity causes full cell rebuild on insert/delete
ForEach(Array(items.enumerated()), id: \.offset) { index, item in
    ItemRow(item: item)
}

// BAD: Value-based identity unstable when content changes
ForEach(items, id: \.name) { item in // name can change
    ItemRow(item: item)
}

// GOOD: Stable unique identifier
ForEach(items, id: \.id) { item in // UUID is immutable
    ItemRow(item: item)
}
// Or with Identifiable conformance:
ForEach(items) { item in
    ItemRow(item: item)
}
```

2. **Lazy Loading Correctness**

```swift
// BAD: Non-lazy stack for large data set
ScrollView {
    VStack { // creates ALL 10,000 cells immediately
        ForEach(items) { item in
            ItemRow(item: item)
        }
    }
}

// GOOD: Lazy stack with pinned headers
ScrollView {
    LazyVStack(spacing: 8, pinnedViews: [.sectionHeaders]) {
        ForEach(sections) { section in
            Section(header: SectionHeader(title: section.title)) {
                ForEach(section.items) { item in
                    ItemRow(item: item)
                }
            }
        }
    }
}
```

3. **onAppear Side Effect Management**

```swift
// BAD: Refetches data on every appear (scroll in/out triggers repeatedly)
struct ItemRow: View {
    let item: Item
    @State private var detail: Detail?

    var body: some View {
        VStack { /* ... */ }
            .onAppear {
                Task { detail = try await api.fetchDetail(item.id) } // fires every scroll
            }
    }
}

// GOOD: Load once with guard
struct ItemRow: View {
    let item: Item
    @State private var detail: Detail?
    @State private var hasLoaded = false

    var body: some View {
        VStack { /* ... */ }
            .task(id: item.id) { // cancelled and restarted only if id changes
                guard !hasLoaded else { return }
                detail = try? await api.fetchDetail(item.id)
                hasLoaded = true
            }
    }
}
```

4. **Pagination Prefetching**

```swift
// BAD: Load next page only when last item appears — visible loading gap
.onAppear {
    if item == items.last {
        loadNextPage()
    }
}

// GOOD: Prefetch threshold before reaching end
.onAppear {
    let thresholdIndex = items.index(items.endIndex, offsetBy: -5, limitedBy: items.startIndex) ?? items.startIndex
    if items.firstIndex(where: { $0.id == item.id })! >= thresholdIndex {
        loadNextPage()
    }
}

// BETTER: Dedicated pagination view model
@Observable class PaginatedList<T: Identifiable> {
    private(set) var items: [T] = []
    private var currentPage = 0
    private var isLoading = false

    func onItemAppear(_ item: T) {
        guard !isLoading,
              let index = items.firstIndex(where: { $0.id == item.id }),
              index >= items.count - 5 else { return }
        loadNextPage()
    }
}
```

## Expected Output

```
## SwiftUI List Performance Review Report

### Summary
- **List components reviewed:** N
- **Identity stability issues:** N
- **Lazy loading violations:** N
- **onAppear side effect issues:** N
- **Pagination gaps:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Impact:** ...
- **Recommendation:** ...
```

## Example Output

```
## SwiftUI List Performance Review Report

### Summary
- **List components reviewed:** 5
- **Identity stability issues:** 1
- **Lazy loading violations:** 1
- **onAppear side effect issues:** 2
- **Pagination gaps:** 1

### Findings

#### [Critical] Non-Lazy Stack — SearchResults.swift:L28
- **Issue:** `VStack` used inside `ScrollView` for search results that can return 500+ items.
- **Impact:** All 500 cells created on initial load; ~200ms hang on main thread.
- **Recommendation:** Replace with `LazyVStack`.

#### [Warning] Redundant Fetch — MessageCell.swift:L42
- **Issue:** `.onAppear` fetches read receipt status every time cell scrolls into view.
- **Recommendation:** Use `.task(id:)` with a loaded guard or cache read receipts in repository.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates identity, laziness, side effects, pagination
- **RT-02 (Role-Based Task Framing):** Reviewer acts as SwiftUI scroll performance expert
- **AG-02 (Automated Guardrails):** Prevents false flags on small bounded lists
- **AG-12 (Performance-Aware Review):** Focuses on frame budget and memory impact

## Related Prompts

- `ios_swiftui_view_update_review.md` — General view redraw optimization
- `ios_core_animation_hitch_review.md` — Rendering layer hitches during scroll
- `ios_core_data_query_review.md` — Efficient data fetching for list backing stores

## Customization Guide

- **Image-heavy lists:** Add async image loading checks (AsyncImage, phase handling, cache headers)
- **Diffable data sources:** Add section snapshot and NSDiffableDataSourceSnapshot review if UIKit hybrid
- **Infinite scroll:** Add end-of-content detection and empty state handling checks
