---
title: "Android Room Database Migration Safety Audit"
category: mobile/android/targeted-reviews
description: "Android Room Database Migration Safety Audit."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - migration
  - mobile
  - reviews
  - room
  - safety
updated: "2026-03-19"
related_prompts: []
---

# Android Room Database Migration Safety Audit

**Objective:** Conduct a safety-focused audit of Room database migrations to prevent data loss, corruption, and app crashes during schema updates, analyzing migration completeness, data preservation, rollback capabilities, and testing coverage.

**When to Use:** Use this prompt before releasing app updates with schema changes, after adding new entities or columns, when planning major database refactoring, during post-incident analysis of migration failures, or as part of release QA process.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual migration path** - Don't flag based on pattern matching alone. Verify that the suspected issue actually causes data loss or crashes.
2. **Check for existing safeguards** - Search for migration tests, backup logic, or recovery mechanisms that may already address the concern.
3. **Understand the context** - Consider WHY specific migration approaches are chosen. Some destructive migrations are intentional for development.
4. **Confirm actual data loss risk** - Test migrations with real or representative data before flagging.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `Migration_3_4.kt:15`).

**Finding NO issues is an acceptable outcome.** If migrations are safe and well-tested, say so with confidence. Don't manufacture data loss concerns.

### False-Positive Prevention

- ❌ Do NOT flag fallbackToDestructiveMigration without checking if it's debug-only
- ❌ Do NOT flag auto-migration as unsafe without understanding its guarantees
- ❌ Do NOT assume migration gaps without checking for skip migrations
- ❌ Do NOT report theoretical data loss without testing actual migration scenarios
- ✅ DO test migrations with Room's MigrationTestHelper
- ✅ DO verify migration coverage from the oldest supported version
- ✅ DO check for proper NOT NULL and DEFAULT handling
- ✅ DO consider data backup strategies alongside migration safety

---

### 1. Migration Coverage Analysis

Evaluate migration completeness:

* **Migration Chain Integrity:**
  - Verify migration exists for every version increment
  - Check for "skip" migrations (e.g., 10→15) and their safety
  - Assess fallbackToDestructiveMigration usage (should be disabled in production)
  - Review auto-migration applicability and limitations

* **Version History:**
  - Review complete migration history from version 1 to current
  - Identify any gaps or missing migrations
  - Check schema version in production vs. development
  - Assess migration debt (pending consolidation opportunities)

* **Multi-Path Migrations:**
  - Check if users can upgrade from any old version
  - Review migration ordering for complex paths
  - Assess migration composition for large jumps
  - Verify all upgrade paths are tested

### 2. Individual Migration Review

Analyze each migration for safety:

* **Column Operations:**
  - Adding columns: Check for appropriate default values
  - Removing columns: Verify data is truly unused or migrated
  - Renaming columns: Check for proper ALTER TABLE syntax
  - Type changes: Assess data conversion safety

* **Table Operations:**
  - Creating tables: Check foreign key references exist
  - Dropping tables: Verify data backup or migration
  - Renaming tables: Check all references updated
  - Composite operations: Assess atomicity

* **Index Operations:**
  - Adding indexes: Check column existence first
  - Removing indexes: Assess query performance impact
  - Recreating indexes: Verify covering indexes maintained
  - Unique constraints: Check for data conflicts before adding

* **Foreign Key Operations:**
  - Adding constraints: Verify referential integrity exists
  - Removing constraints: Assess orphan record handling
  - Cascade behavior: Check delete/update cascades

### 3. Data Preservation

Evaluate data safety during migration:

* **Non-Destructive Migrations:**
  - Check that existing data is preserved
  - Verify no data truncation on type changes
  - Assess data transformation correctness
  - Review default value assignments

* **Data Transformation:**
  - Check data mapping correctness
  - Verify nullable to non-null conversions have defaults
  - Assess date/time format conversions
  - Review string encoding changes

* **Large Data Handling:**
  - Check for batch processing in large migrations
  - Assess migration timeout risks
  - Review memory usage during migration
  - Verify no ANR risk from long migrations

### 4. Transaction and Atomicity

Analyze migration transaction handling:

* **Transaction Boundaries:**
  - Review if migrations are transactional
  - Check for partial migration recovery
  - Assess multi-statement migration atomicity
  - Verify rollback on failure

* **Failure Recovery:**
  - Check behavior on migration exception
  - Review database state after failed migration
  - Assess user experience on migration failure
  - Verify app doesn't crash loop

### 5. SQLCipher Considerations

For encrypted databases:

* **Encrypted Migration:**
  - Check migration works with SQLCipher
  - Review PRAGMA cipher_migrate usage if upgrading SQLCipher
  - Assess key availability during migration
  - Verify encryption maintained after migration

* **Cipher Version Upgrades:**
  - Check SQLCipher version compatibility
  - Review cipher settings preservation
  - Assess migration from older cipher versions
  - Verify no unencrypted state during migration

### 6. Testing Assessment

Evaluate migration testing:

* **Test Coverage:**
  - Review MigrationTestHelper usage
  - Check for tests of each migration
  - Assess multi-version upgrade tests
  - Verify edge case coverage

* **Schema Validation:**
  - Check schema export enabled (exportSchema = true)
  - Review schema JSON files in version control
  - Assess schema comparison in CI/CD
  - Verify Room schema validation

* **Production Database Testing:**
  - Check for testing with production data snapshots
  - Review migration testing on various schema versions
  - Assess performance testing of large migrations
  - Verify crash reporting for migration failures

### 7. Auto-Migration Review

For Room's auto-migration feature:

* **Auto-Migration Suitability:**
  - Check if changes are auto-migration compatible
  - Review @AutoMigration annotations
  - Assess auto-migration spec customizations
  - Verify auto-migration doesn't hide issues

* **Auto-Migration Limitations:**
  - Check for unsupported operations
  - Review column renames and deletions
  - Assess complex type changes
  - Verify data transformations work

### 8. Rollback and Recovery

Evaluate recovery options:

* **Rollback Capability:**
  - Check if migrations are reversible
  - Review rollback migration definitions
  - Assess data recovery on downgrade
  - Verify app version compatibility

* **Backup Strategy:**
  - Check for pre-migration backup
  - Review backup storage location
  - Assess backup restoration process
  - Verify backup encryption

---

## Expected Output

Provide a comprehensive Room migration safety audit report including:

### 1. Executive Summary
- Overall migration safety rating
- Schema version current state
- Critical migration issues
- Test coverage assessment

### 2. Migration Chain Analysis

| From | To | Type | Data Safe | Tested | Issues |
|------|-----|------|-----------|--------|--------|
| [Version] | [Version] | [Manual/Auto] | [Yes/Risk/No] | [Yes/No] | [Count] |

### 3. Risk Assessment Matrix

| Migration | Risk Level | Impact | Mitigation |
|-----------|------------|--------|------------|
| [Version] | [Critical/High/Medium/Low] | [Description] | [Action] |

### 4. Detailed Findings

For each issue:
- **Location:** Migration file and operation
- **Issue:** Description
- **Impact:** Data loss/corruption/crash risk
- **Severity:** Critical/High/Medium/Low
- **Current Migration:** Problematic code
- **Safe Migration:** Corrected version
- **Test Case:** How to verify fix

### 5. Test Coverage Gap Analysis

| Version Range | Migration Test | Data Test | Performance Test | Status |
|---------------|----------------|-----------|------------------|--------|
| [Range] | [Yes/No] | [Yes/No] | [Yes/No] | [Gap/OK] |

### 6. Prioritized Recommendations

Ordered by data safety impact.

---

## Example Output

```markdown
# Room Migration Safety Audit Report

## Executive Summary
- **Safety Rating:** At Risk - 2 migrations could cause data loss
- **Current Schema Version:** 65
- **Total Migrations:** 64 (62 manual, 2 auto)
- **Critical Issues:** 2 | High: 3 | Medium: 5 | Low: 4
- **Test Coverage:** 45% (29 of 64 migrations tested)

## Critical Findings

### CRITICAL-1: New NOT NULL Column Without Default
**Severity:** Critical
**Impact:** Migration crash for existing users

**Location:** Migration_62_63.kt

**Current Migration:**
```kotlin
val MIGRATION_62_63 = object : Migration(62, 63) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // CRITICAL: Adding NOT NULL column without default to table with existing data
        database.execSQL(
            "ALTER TABLE todos ADD COLUMN syncStatus TEXT NOT NULL"
        )
        // Crash! Existing rows have no value for syncStatus
    }
}
```

**Error Message:**
```
android.database.sqlite.SQLiteException: Cannot add a NOT NULL column
with default value NULL
```

**Safe Migration:**
```kotlin
val MIGRATION_62_63 = object : Migration(62, 63) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // CORRECT: Add column with default value
        database.execSQL(
            "ALTER TABLE todos ADD COLUMN syncStatus TEXT NOT NULL DEFAULT 'PENDING'"
        )

        // Or: Add as nullable first, populate, then make NOT NULL
        // This is needed for more complex default logic
    }
}
```

**Alternative for Complex Defaults:**
```kotlin
val MIGRATION_62_63 = object : Migration(62, 63) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // Step 1: Add nullable column
        database.execSQL(
            "ALTER TABLE todos ADD COLUMN syncStatus TEXT"
        )

        // Step 2: Populate with computed defaults
        database.execSQL("""
            UPDATE todos SET syncStatus = CASE
                WHEN lastSyncedAt IS NULL THEN 'PENDING'
                WHEN lastModifiedAt > lastSyncedAt THEN 'PENDING'
                ELSE 'SYNCED'
            END
        """)

        // Step 3: Recreate table with NOT NULL constraint
        // (SQLite doesn't support ALTER COLUMN)
        database.execSQL("""
            CREATE TABLE todos_new (
                id TEXT PRIMARY KEY NOT NULL,
                title TEXT NOT NULL,
                syncStatus TEXT NOT NULL,
                ...
            )
        """)
        database.execSQL("""
            INSERT INTO todos_new SELECT * FROM todos
        """)
        database.execSQL("DROP TABLE todos")
        database.execSQL("ALTER TABLE todos_new RENAME TO todos")
    }
}
```

---

### CRITICAL-2: Column Removal Without Data Migration
**Severity:** Critical
**Impact:** Silent data loss - user data permanently deleted

**Location:** Migration_58_59.kt

**Current Migration:**
```kotlin
val MIGRATION_58_59 = object : Migration(58, 59) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // CRITICAL: Dropping column with user data!
        // SQLite doesn't support DROP COLUMN, so this recreates the table
        // But the old 'notes' column data is lost forever!

        database.execSQL("""
            CREATE TABLE shopping_items_new (
                id TEXT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                isPurchased INTEGER NOT NULL
                -- 'notes' column removed - DATA LOST!
            )
        """)
        database.execSQL("""
            INSERT INTO shopping_items_new (id, name, quantity, isPurchased)
            SELECT id, name, quantity, isPurchased FROM shopping_items
        """)
        database.execSQL("DROP TABLE shopping_items")
        database.execSQL("ALTER TABLE shopping_items_new RENAME TO shopping_items")
    }
}
```

**Impact:**
- User's shopping item notes permanently deleted
- No warning or confirmation
- Cannot be recovered

**Safe Migration (if column truly needs removal):**
```kotlin
val MIGRATION_58_59 = object : Migration(58, 59) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // Option 1: Migrate data to new location
        database.execSQL("""
            INSERT INTO shopping_item_notes (itemId, note, createdAt)
            SELECT id, notes, CURRENT_TIMESTAMP
            FROM shopping_items
            WHERE notes IS NOT NULL AND notes != ''
        """)

        // Option 2: Keep column but mark as deprecated
        // (Safer - no data loss, clean up later)
        database.execSQL("""
            ALTER TABLE shopping_items ADD COLUMN notes_deprecated TEXT
        """)
        database.execSQL("""
            UPDATE shopping_items SET notes_deprecated = notes
        """)

        // Now safe to recreate table without notes column
    }
}
```

---

### HIGH-1: Missing Migration Test Coverage
**Severity:** High
**Impact:** Undiscovered migration bugs in production

**Location:** Migrations 45-55

**Current State:**
```kotlin
// No migration tests exist for versions 45-55
// These migrations added:
// - Foreign key constraints
// - Index changes
// - Column type changes

// Untested migrations may silently fail or corrupt data
```

**Recommended Fix:**
```kotlin
@RunWith(AndroidJUnit4::class)
class MigrationTest {
    @get:Rule
    val helper = MigrationTestHelper(
        InstrumentationRegistry.getInstrumentation(),
        FamilyHubDatabase::class.java
    )

    @Test
    fun migrate45To46() {
        // Create database at version 45
        helper.createDatabase(TEST_DB, 45).apply {
            // Insert test data
            execSQL("""
                INSERT INTO calendar_events (id, title, startDate, endDate)
                VALUES ('1', 'Test Event', 1234567890, 1234567900)
            """)
            close()
        }

        // Run migration
        val db = helper.runMigrationsAndValidate(TEST_DB, 46, true, MIGRATION_45_46)

        // Verify data preserved
        db.query("SELECT * FROM calendar_events WHERE id = '1'").use { cursor ->
            assertTrue(cursor.moveToFirst())
            assertEquals("Test Event", cursor.getString(cursor.getColumnIndex("title")))
            // Verify new column has expected default
            assertNotNull(cursor.getString(cursor.getColumnIndex("newColumn")))
        }
    }

    @Test
    fun migrateAllVersions() {
        // Test upgrade from oldest supported to newest
        helper.createDatabase(TEST_DB, 1)
        helper.runMigrationsAndValidate(
            TEST_DB, 65, true,
            *ALL_MIGRATIONS.toTypedArray()
        )
    }
}
```

---

### HIGH-2: Foreign Key Without Cascade Creates Orphans
**Severity:** High
**Impact:** Orphaned records, constraint violations

**Location:** Migration_40_41.kt

**Current Migration:**
```kotlin
val MIGRATION_40_41 = object : Migration(40, 41) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // Adding foreign key without considering existing orphans
        database.execSQL("""
            CREATE TABLE todo_assignments_new (
                id TEXT PRIMARY KEY NOT NULL,
                todoId TEXT NOT NULL,
                assigneeId TEXT NOT NULL,
                FOREIGN KEY (todoId) REFERENCES todos(id),
                FOREIGN KEY (assigneeId) REFERENCES family_members(id)
            )
        """)

        // PROBLEM: What if todoId or assigneeId references deleted records?
        database.execSQL("""
            INSERT INTO todo_assignments_new SELECT * FROM todo_assignments
        """)
        // Crash! Foreign key constraint failed
    }
}
```

**Safe Migration:**
```kotlin
val MIGRATION_40_41 = object : Migration(40, 41) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // Step 1: Clean up orphaned records first
        database.execSQL("""
            DELETE FROM todo_assignments
            WHERE todoId NOT IN (SELECT id FROM todos)
               OR assigneeId NOT IN (SELECT id FROM family_members)
        """)

        // Step 2: Now safe to add foreign key constraints
        database.execSQL("""
            CREATE TABLE todo_assignments_new (
                id TEXT PRIMARY KEY NOT NULL,
                todoId TEXT NOT NULL,
                assigneeId TEXT NOT NULL,
                FOREIGN KEY (todoId) REFERENCES todos(id) ON DELETE CASCADE,
                FOREIGN KEY (assigneeId) REFERENCES family_members(id) ON DELETE SET NULL
            )
        """)

        database.execSQL("""
            INSERT INTO todo_assignments_new SELECT * FROM todo_assignments
        """)
        database.execSQL("DROP TABLE todo_assignments")
        database.execSQL("ALTER TABLE todo_assignments_new RENAME TO todo_assignments")
    }
}
```

---

### MEDIUM-1: Auto-Migration Used for Column Rename
**Severity:** Medium
**Impact:** Column rename not recognized, creates new column instead

**Location:** Auto-migration 64→65

**Current Configuration:**
```kotlin
@Database(
    version = 65,
    entities = [...],
    autoMigrations = [
        AutoMigration(from = 64, to = 65)  // Used for column rename
    ]
)
abstract class FamilyHubDatabase : RoomDatabase()

// Entity changed from:
@Entity data class Note(val updatedAt: Long)
// To:
@Entity data class Note(val modifiedAt: Long)

// Auto-migration creates NEW column 'modifiedAt', doesn't migrate data!
```

**Recommended Fix:**
```kotlin
// Use manual migration for column renames
@Database(
    version = 65,
    entities = [...],
    autoMigrations = []  // Remove auto-migration
)
abstract class FamilyHubDatabase : RoomDatabase()

// Add manual migration
val MIGRATION_64_65 = object : Migration(64, 65) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // Proper column rename (requires table recreation in SQLite)
        database.execSQL("""
            CREATE TABLE notes_new (
                id TEXT PRIMARY KEY NOT NULL,
                content TEXT NOT NULL,
                modifiedAt INTEGER NOT NULL  -- New name
            )
        """)
        database.execSQL("""
            INSERT INTO notes_new (id, content, modifiedAt)
            SELECT id, content, updatedAt FROM notes
        """)
        database.execSQL("DROP TABLE notes")
        database.execSQL("ALTER TABLE notes_new RENAME TO notes")
    }
}
```

---

## Migration Chain Analysis

| From | To | Type | Data Safe | Tested | Issues |
|------|-----|------|-----------|--------|--------|
| 62 | 63 | Manual | ❌ No | No | 1 Critical |
| 58 | 59 | Manual | ❌ No | No | 1 Critical |
| 45-55 | Various | Manual | Unknown | No | Test gap |
| 64 | 65 | Auto | ⚠️ Risk | Yes | 1 Medium |
| 40 | 41 | Manual | ⚠️ Risk | Yes | 1 High |
| Others | - | Manual | ✓ Yes | Partial | Minor |

## Risk Assessment Matrix

| Migration | Risk | Impact | Mitigation |
|-----------|------|--------|------------|
| 62→63 | Critical | App crash on upgrade | Add default value |
| 58→59 | Critical | Data loss | Migrate data first |
| 40→41 | High | Constraint violations | Clean orphans first |
| 64→65 | Medium | Empty new column | Manual migration |
| 45-55 | Unknown | Unknown until tested | Add test coverage |

## Test Coverage Gap Analysis

| Range | Migration Test | Data Test | Stress Test | Status |
|-------|----------------|-----------|-------------|--------|
| 1-20 | ❌ | ❌ | ❌ | Critical Gap |
| 21-44 | Partial | ❌ | ❌ | Gap |
| 45-55 | ❌ | ❌ | ❌ | Critical Gap |
| 56-65 | ✓ | Partial | ❌ | Needs Work |

## Remediation Priority

### Critical (Before Next Release)
1. Fix Migration 62→63: Add default value
2. Fix Migration 58→59: Preserve data before removal
3. Test all migrations 45-55

### High Priority (This Sprint)
1. Add foreign key cleanup to Migration 40→41
2. Convert auto-migration 64→65 to manual
3. Add MigrationTestHelper for all versions

### Medium Priority (Next Sprint)
1. Add data preservation tests
2. Implement pre-migration backup
3. Add migration performance tests

### Low Priority (Backlog)
1. Document all migration decisions
2. Consolidate old migrations
3. Add migration monitoring/alerting
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Migration safety focus
- **ST-02** (Structured Sequential Instructions) - Systematic migration review
- **RT-02** (Multi-Dimensional Analysis) - Safety, testing, performance
- **RT-05** (Evidence-Based Reasoning) - Specific SQL examples
- **ST-03** (Output Format Templates) - Migration chain tables
- **DS-06** (Prioritization Guidance) - Data safety priority
- **QA-02** (Adversarial Stress-Test) - Failure scenario analysis

---

## Related Prompts

- `android_room_database_query_review.md` - For DAO/query optimization
- `android_sqlcipher_key_management_review.md` - For encrypted migrations
- `android_sync_architecture_review.md` - For sync-related schema changes
- `testing_unit_test_generation.md` - For migration test generation
- `mobile_app_security_review.md` - For security considerations

---

## Customization Guide

- **For Encrypted Databases:** Add SQLCipher version upgrade, cipher migration sections
- **For Large Databases:** Focus on batch migration, performance, timeout handling
- **For Multi-Module Apps:** Add cross-module schema dependency review
- **For CI/CD Integration:** Add automated migration testing pipeline review
- **For Rollback Planning:** Expand rollback and downgrade migration sections
