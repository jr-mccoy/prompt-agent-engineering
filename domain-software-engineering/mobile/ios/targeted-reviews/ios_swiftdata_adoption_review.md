---
title: "iOS SwiftData Adoption Review"
category: mobile-development
description: "Review SwiftData adoption for model macro usage, query optimization, relationship modeling, undo/redo support, and CloudKit compatibility."
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
  - swiftdata
  - persistence
updated: "2026-03-19"
---

# iOS SwiftData Adoption Review

**Objective:** Audit SwiftData implementations for correct @Model macro usage, efficient @Query declarations, proper relationship modeling with cascade rules, undo/redo manager integration, and CloudKit sync compatibility to ensure data integrity and performance.

**When to Use:** Apply when adopting SwiftData in a new project, migrating from Core Data, reviewing query performance, or enabling CloudKit sync with SwiftData models.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. Is this a new SwiftData project or migrating from Core Data?
2. What iOS deployment target (iOS 17.0 has known SwiftData bugs; 17.2+ recommended)?
3. Is CloudKit sync required via ModelConfiguration?
4. How many @Model types and what relationship complexity?

## Instructions

### CRITICAL: Verification Requirements

- @Model classes must use value types for stored properties where possible
- @Query must be declared with sort descriptors and predicates — not filtered in-memory post-fetch
- Inverse relationships must be defined to prevent orphaned records
- CloudKit-synced models must only use CloudKit-compatible types

### False-Positive Prevention

- ❌ Do NOT flag @Model with reference type properties if they are also @Model types (valid relationships)
- ✅ DO flag @Model with non-Codable reference type stored properties (will crash at runtime)
- ❌ Do NOT flag missing @Relationship macro when SwiftData can infer the inverse
- ✅ DO flag missing explicit delete rules on relationships with dependent data
- ❌ Do NOT flag @Transient properties — these are intentionally excluded from persistence
- ✅ DO flag computed properties mistakenly expected to persist (they don't)

1. **@Model Macro Usage**

```swift
// BAD: Non-codable type and unclear persistence intent
@Model
class UserProfile {
    var name: String
    var avatar: UIImage // UIImage is not Codable — runtime crash
    var formattedName: String { name.uppercased() } // computed — not persisted (OK but may confuse)
    var cachedData: NSCache<NSString, NSData> // reference type, not persistable
}

// GOOD: Clean model with proper types
@Model
class UserProfile {
    var name: String
    @Attribute(.externalStorage) var avatarData: Data?
    @Transient var cachedAvatar: UIImage? = nil // explicitly transient

    var formattedName: String { name.uppercased() } // clearly computed

    init(name: String, avatarData: Data? = nil) {
        self.name = name
        self.avatarData = avatarData
    }
}
```

2. **@Query Optimization**

```swift
// BAD: Fetches all, then filters in memory
struct OrderListView: View {
    @Query var allOrders: [Order] // fetches every order

    var activeOrders: [Order] {
        allOrders.filter { $0.status == .active } // in-memory filter on full dataset
    }
}

// GOOD: Predicate and sort at query level
struct OrderListView: View {
    @Query(
        filter: #Predicate<Order> { $0.status == .active },
        sort: [SortDescriptor(\.createdAt, order: .reverse)]
    )
    var activeOrders: [Order]
}
```

3. **Relationship Modeling**

```swift
// BAD: No inverse, no delete rule — orphaned children on parent delete
@Model
class Department {
    var name: String
    var employees: [Employee]? // no relationship macro, no delete rule
}

@Model
class Employee {
    var name: String
    // no reference back to department
}

// GOOD: Explicit relationship with inverse and delete rule
@Model
class Department {
    var name: String
    @Relationship(deleteRule: .cascade, inverse: \Employee.department)
    var employees: [Employee]?

    init(name: String) { self.name = name }
}

@Model
class Employee {
    var name: String
    var department: Department?

    init(name: String, department: Department? = nil) {
        self.name = name
        self.department = department
    }
}
```

4. **CloudKit Compatibility**

```swift
// BAD: Types not compatible with CloudKit sync
@Model
class Note {
    var title: String
    @Attribute(.unique) var slug: String // unique constraints not supported in CloudKit
    var tags: Set<String> // Set not supported — use Array
    var priority: Int8 // Int8 not supported — use Int
}

// GOOD: CloudKit-compatible types
@Model
class Note {
    var title: String
    var slug: String // remove unique constraint for CloudKit
    var tags: [String] // Array instead of Set
    var priority: Int // standard Int

    init(title: String, slug: String, tags: [String] = [], priority: Int = 0) {
        self.title = title
        self.slug = slug
        self.tags = tags
        self.priority = priority
    }
}

// Configuration
let config = ModelConfiguration(cloudKitDatabase: .private("iCloud.com.app.notes"))
let container = try ModelContainer(for: Note.self, configurations: config)
```

## Expected Output

```
## SwiftData Adoption Review Report

### Summary
- **@Model types reviewed:** N
- **Model definition issues:** N
- **Query efficiency issues:** N
- **Relationship issues:** N
- **CloudKit compatibility issues:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Recommendation:** ...
```

## Example Output

```
## SwiftData Adoption Review Report

### Summary
- **@Model types reviewed:** 8
- **Model definition issues:** 2
- **Query efficiency issues:** 3
- **Relationship issues:** 1
- **CloudKit compatibility issues:** 2

### Findings

#### [Critical] Non-Codable Property — MediaItem.swift:L12
- **Issue:** `var thumbnail: UIImage` stored on @Model class. UIImage is not Codable.
- **Recommendation:** Store as `Data` with `@Attribute(.externalStorage)` and provide computed UIImage accessor.

#### [Warning] Missing Delete Rule — Project.swift:L8
- **Issue:** `var tasks: [Task]?` relationship has no explicit delete rule. Deleting a Project leaves orphaned Tasks.
- **Recommendation:** Add `@Relationship(deleteRule: .cascade, inverse: \Task.project)`.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates model, query, relationship, CloudKit concerns
- **RT-02 (Role-Based Task Framing):** Reviewer acts as SwiftData adoption specialist
- **RT-04 (Constraint-Based Refinement):** Enforces type safety and CloudKit compatibility rules
- **AG-02 (Automated Guardrails):** Prevents false flags on transient properties and inferred relationships

## Related Prompts

- `ios_core_data_query_review.md` — Core Data query patterns (for comparison/migration)
- `ios_core_data_migration_safety_audit.md` — Migration from Core Data to SwiftData
- `cloudkit_data_model_design.md` — CloudKit-specific data modeling

## Customization Guide

- **Core Data migration:** Add side-by-side comparison of Core Data and SwiftData equivalent patterns
- **Testing:** Add ModelContainer in-memory configuration for unit test isolation
- **Multi-platform:** Add cross-platform type compatibility checks (macOS, watchOS, visionOS)
