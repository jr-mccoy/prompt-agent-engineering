---
title: "iOS Core Data Migration Safety Audit"
category: mobile-development
description: "Audit Core Data migration chain for lightweight migration eligibility, custom migration policies, mapping model correctness, and migration testing strategy."
techniques:
  - ST-01
  - RT-02
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - code-review
  - core-data
  - migration
  - data-safety
updated: "2026-03-19"
---

# iOS Core Data Migration Safety Audit

**Objective:** Audit the Core Data migration chain for lightweight migration eligibility, custom policy correctness, mapping model completeness, and testing strategy to prevent data loss or crashes when users update from any previously shipped app version.

**When to Use:** Apply before every app release that includes Core Data model changes, when adding custom migration policies, or when investigating post-update crashes or missing data reports from users.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. How many versioned .xcdatamodel files exist in the project?
2. Are migrations lightweight-only or do any require custom NSEntityMigrationPolicy?
3. What is the oldest supported app version users can update from?
4. Is there a migration testing strategy (unit tests, on-device QA)?

## Instructions

### CRITICAL: Verification Requirements

- Every model version must have a clear migration path to the current version (chain or direct)
- Lightweight migration eligibility must be verified for each step (attribute renames need renaming ID)
- Custom migration policies must handle partial failure and rollback
- Migration must be tested from every supported source version to current

### False-Positive Prevention

- ❌ Do NOT flag adding optional attributes as needing custom migration — this is lightweight-eligible
- ✅ DO flag adding required attributes without default values in migration
- ❌ Do NOT flag simple attribute type changes that Core Data auto-converts (Int16 -> Int32)
- ✅ DO flag attribute type changes that lose precision (Double -> Int, String -> Date)
- ❌ Do NOT flag renamed entities/attributes with proper renaming identifiers set
- ✅ DO flag renamed entities/attributes WITHOUT renaming identifiers — Core Data treats as delete + add

1. **Lightweight Migration Eligibility**

```swift
// BAD: Attribute rename without renaming identifier — causes data loss
// Model V1: Entity "User" has attribute "userName"
// Model V2: Entity "User" has attribute "displayName"
// No renaming identifier set — Core Data deletes userName, creates empty displayName

// GOOD: Set renaming identifier in model editor
// Model V2: "displayName" attribute has Renaming ID = "userName"
// Core Data performs lightweight rename, preserving data

// Verify in code:
let description = NSPersistentStoreDescription()
description.shouldMigrateStoreAutomatically = true
description.shouldInferMappingModelAutomatically = true
```

2. **Custom Migration Policy**

```swift
// BAD: Custom policy without error handling or validation
class SplitNameMigration: NSEntityMigrationPolicy {
    override func createDestinationInstances(
        forSource sInstance: NSManagedObject,
        in mapping: NSEntityMapping,
        manager: NSMigrationManager
    ) throws {
        let fullName = sInstance.value(forKey: "fullName") as! String // force unwrap crashes
        let parts = fullName.split(separator: " ")
        let dest = NSEntityDescription.insertNewObject(
            forEntityName: "User", into: manager.destinationContext
        )
        dest.setValue(String(parts[0]), forKey: "firstName")
        dest.setValue(String(parts[1]), forKey: "lastName") // crashes if no space in name
    }
}

// GOOD: Defensive custom policy
class SplitNameMigration: NSEntityMigrationPolicy {
    override func createDestinationInstances(
        forSource sInstance: NSManagedObject,
        in mapping: NSEntityMapping,
        manager: NSMigrationManager
    ) throws {
        let fullName = sInstance.value(forKey: "fullName") as? String ?? ""
        let parts = fullName.split(separator: " ", maxSplits: 1)

        let dest = NSEntityDescription.insertNewObject(
            forEntityName: "User", into: manager.destinationContext
        )
        dest.setValue(parts.first.map(String.init) ?? "", forKey: "firstName")
        dest.setValue(parts.count > 1 ? String(parts[1]) : "", forKey: "lastName")

        manager.associate(sourceInstance: sInstance, withDestinationInstance: dest, for: mapping)
    }
}
```

3. **Migration Chain Verification**

```swift
// BAD: No migration path from V1 -> V3 (only V2 -> V3 exists)
// Users on V1 who skipped V2 update will crash

// GOOD: Staged migration manager for iOS 17+
let container = NSPersistentContainer(name: "App")

if #available(iOS 17, *) {
    let v1toV2 = NSLightweightMigrationStage(["AppV1", "AppV2"])
    let v2toV3 = NSCustomMigrationStage(
        migratingFrom: NSManagedObjectModel.makeManagedObjectModel(for: ["AppV2"]),
        to: NSManagedObjectModel.makeManagedObjectModel(for: ["AppV3"])
    )
    v2toV3.willMigrateHandler = { migrationManager, currentStage in
        // custom transformation logic
    }

    let schema = NSManagedObjectModelReference(/* ... */)
    container.persistentStoreDescriptions.first?.setOption(
        true as NSNumber, forKey: NSPersistentHistoryTrackingKey
    )
}
```

4. **Migration Testing**

```swift
// BAD: No migration tests — discovered in production
// "It works on my device" — only tested clean install

// GOOD: Test migration from each supported version
final class MigrationTests: XCTestCase {
    func testV1ToCurrentMigration() throws {
        // Copy V1 seeded store from test bundle
        let sourceURL = Bundle(for: Self.self).url(forResource: "TestStore_V1", withExtension: "sqlite")!
        let testURL = FileManager.default.temporaryDirectory.appendingPathComponent("test.sqlite")
        try FileManager.default.copyItem(at: sourceURL, to: testURL)

        // Attempt migration
        let container = NSPersistentContainer(name: "App")
        let desc = NSPersistentStoreDescription(url: testURL)
        desc.shouldMigrateStoreAutomatically = true
        desc.shouldInferMappingModelAutomatically = true
        container.persistentStoreDescriptions = [desc]

        let expectation = expectation(description: "migration")
        container.loadPersistentStores { _, error in
            XCTAssertNil(error)
            expectation.fulfill()
        }
        wait(for: [expectation], timeout: 30)

        // Validate data integrity
        let request = NSFetchRequest<NSManagedObject>(entityName: "User")
        let users = try container.viewContext.fetch(request)
        XCTAssertEqual(users.count, 50) // same as V1 seed
        XCTAssertFalse(users.contains { ($0.value(forKey: "firstName") as? String)?.isEmpty ?? true })
    }
}
```

## Expected Output

```
## Core Data Migration Safety Audit Report

### Summary
- **Model versions reviewed:** N
- **Migration paths verified:** N of N required
- **Lightweight eligibility issues:** N
- **Custom policy risks:** N
- **Missing test coverage:** N version pairs

### Findings
#### [Severity] Issue — File/Model Version
- **Issue:** ...
- **Data risk:** None / Partial loss / Full loss
- **Recommendation:** ...
```

## Example Output

```
## Core Data Migration Safety Audit Report

### Summary
- **Model versions reviewed:** 5 (V1-V5)
- **Migration paths verified:** 3 of 4 required
- **Lightweight eligibility issues:** 1
- **Custom policy risks:** 1
- **Missing test coverage:** 2 version pairs (V1->V5, V2->V5)

### Findings

#### [Critical] Missing Renaming ID — AppModel V3 -> V4
- **Issue:** `Product.sku` renamed to `Product.productCode` without renaming identifier.
- **Data risk:** Full loss of SKU data for all products on migration.
- **Recommendation:** Set renaming identifier on `productCode` to `sku` in model V4.

#### [Warning] Force Unwrap in Policy — AddressMigration.swift:L23
- **Issue:** `sInstance.value(forKey: "zip") as! String` force unwraps. 12% of records have nil zip.
- **Data risk:** Migration crash for affected users.
- **Recommendation:** Use optional binding with empty string default.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates eligibility, policies, chain, testing
- **RT-02 (Role-Based Task Framing):** Reviewer acts as Core Data migration safety expert
- **AG-02 (Automated Guardrails):** Prevents false flags on valid lightweight changes

## Related Prompts

- `ios_core_data_query_review.md` — Post-migration query efficiency
- `ios_swiftdata_adoption_review.md` — SwiftData migration considerations
- `cloudkit_migration_strategy.md` — CloudKit schema evolution alongside Core Data

## Customization Guide

- **SwiftData projects:** Add ModelContainer migration stage verification
- **CloudKit sync:** Add CKRecord schema compatibility checks alongside Core Data model changes
- **Large databases:** Add migration performance benchmarking (time to migrate 100K records)
