---
title: "iOS Core Data Query Review"
category: mobile-development
description: "Review Core Data fetch request efficiency including predicate complexity, relationship faulting, batch size, NSFetchedResultsController usage, and background context patterns."
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
  - core-data
  - persistence
  - performance
updated: "2026-03-19"
---

# iOS Core Data Query Review

**Objective:** Audit Core Data fetch operations for efficiency by reviewing predicate complexity and indexing alignment, relationship faulting behavior, batch size tuning, NSFetchedResultsController correctness, and background context usage to prevent main thread blocking and excessive memory consumption.

**When to Use:** Apply when reviewing data-heavy screens, investigating main thread hangs during data loads, or auditing Core Data stack configuration. Essential for apps with 10K+ records or complex relationship graphs.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. How many records are typical for the largest entities (100s, 10Ks, 100Ks)?
2. Are fetch requests executed on the main context or background contexts?
3. Is NSFetchedResultsController used for table/collection view data sources?
4. Are there cross-store or cross-entity aggregate queries?

## Instructions

### CRITICAL: Verification Requirements

- Predicates filtering on non-indexed attributes must be flagged for datasets > 1K records
- Relationship traversal in predicates must use indexed foreign keys where possible
- Batch size must be set for any fetch that could return > 50 objects
- Background context fetches must not pass NSManagedObjects across thread boundaries

### False-Positive Prevention

- ❌ Do NOT flag missing batch size on fetches guaranteed to return < 20 results
- ✅ DO flag missing batch size on unbounded or large-result fetches
- ❌ Do NOT flag faulting as a problem — it is Core Data's designed behavior for memory management
- ✅ DO flag mass fault firing in tight loops (N+1 query pattern)
- ❌ Do NOT flag main context fetches for small, bounded queries with indexed predicates
- ✅ DO flag main context fetches for expensive queries (unindexed, large result set, complex predicates)

1. **Predicate Efficiency**

```swift
// BAD: String search without index on large dataset
let request = NSFetchRequest<Message>(entityName: "Message")
request.predicate = NSPredicate(format: "body CONTAINS[cd] %@", searchText)
// Full table scan on 100K+ messages

// GOOD: Indexed attribute with efficient predicate
let request = NSFetchRequest<Message>(entityName: "Message")
request.predicate = NSPredicate(format: "conversationId == %@ AND timestamp >= %@", conversationId, startDate as CVarArg)
// Uses indexed conversationId + timestamp for efficient lookup
request.fetchBatchSize = 20
request.sortDescriptors = [NSSortDescriptor(keyPath: \Message.timestamp, ascending: false)]
```

2. **Relationship Faulting (N+1 Problem)**

```swift
// BAD: N+1 fault firing in loop
let orders = try context.fetch(orderRequest) // fetches 200 orders
for order in orders {
    let customerName = order.customer?.name // fires fault per order = 200 additional queries
    print(customerName)
}

// GOOD: Prefetch relationships
let request = NSFetchRequest<Order>(entityName: "Order")
request.relationshipKeyPathsForPrefetching = ["customer"]
request.fetchBatchSize = 50
let orders = try context.fetch(request)
for order in orders {
    let customerName = order.customer?.name // already in memory
}
```

3. **Batch Size Configuration**

```swift
// BAD: Fetches all objects into memory at once
let request = NSFetchRequest<Product>(entityName: "Product")
request.predicate = NSPredicate(format: "category == %@", "electronics")
let products = try context.fetch(request) // 50K products materialized

// GOOD: Batch fetching for memory efficiency
let request = NSFetchRequest<Product>(entityName: "Product")
request.predicate = NSPredicate(format: "category == %@", "electronics")
request.fetchBatchSize = 20 // only 20 objects materialized at a time
request.fetchLimit = 100 // hard limit if only showing first page
```

4. **Background Context Usage**

```swift
// BAD: Heavy fetch on main context blocks UI
let products = try viewContext.fetch(expensiveRequest) // main thread blocked

// BAD: Passing managed objects across contexts
let bgContext = container.newBackgroundContext()
bgContext.perform {
    let objects = try bgContext.fetch(request)
    DispatchQueue.main.async {
        self.items = objects // CRASH: accessing bgContext objects on main thread
    }
}

// GOOD: Fetch on background, pass objectIDs to main
let bgContext = container.newBackgroundContext()
bgContext.perform {
    let objectIDs = try bgContext.fetch(request).map(\.objectID)
    DispatchQueue.main.async {
        self.items = objectIDs.compactMap {
            try? viewContext.existingObject(with: $0) as? Product
        }
    }
}
```

## Expected Output

```
## Core Data Query Review Report

### Summary
- **Fetch requests reviewed:** N
- **Predicate efficiency issues:** N
- **N+1 faulting risks:** N
- **Missing batch size:** N
- **Thread safety violations:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Impact:** Estimated query time / memory impact
- **Recommendation:** ...
```

## Example Output

```
## Core Data Query Review Report

### Summary
- **Fetch requests reviewed:** 14
- **Predicate efficiency issues:** 2
- **N+1 faulting risks:** 3
- **Missing batch size:** 5
- **Thread safety violations:** 1

### Findings

#### [Critical] Unindexed Search — ChatRepository.swift:L89
- **Issue:** `CONTAINS[cd]` predicate on `body` attribute across 150K Message records with no index.
- **Impact:** ~800ms main thread block per search keystroke.
- **Recommendation:** Add full-text search index or use `NSExpression` with `BEGINSWITH` on indexed prefix field.

#### [Warning] N+1 Faulting — OrderListViewModel.swift:L34
- **Issue:** Loop over 200 orders accessing `order.items.count` without prefetching `items` relationship.
- **Recommendation:** Add `relationshipKeyPathsForPrefetching = ["items"]` to fetch request.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates predicates, faulting, batching, threading
- **RT-02 (Role-Based Task Framing):** Reviewer acts as Core Data performance specialist
- **AG-02 (Automated Guardrails):** Prevents false flags on small fetches and normal faulting
- **AG-12 (Performance-Aware Review):** Focuses on query execution time and memory footprint

## Related Prompts

- `ios_core_data_migration_safety_audit.md` — Migration chain safety
- `ios_swiftdata_adoption_review.md` — SwiftData alternative patterns
- `ios_swift_concurrency_safety_review.md` — Async context safety

## Customization Guide

- **SwiftData migration:** Add comparison checks for equivalent SwiftData @Query patterns
- **CloudKit sync:** Add CKRecord <-> NSManagedObject sync efficiency checks
- **Large datasets (100K+):** Add NSBatchInsertRequest, NSBatchDeleteRequest usage verification
