---
title: "Android Data Layer & Persistence Analysis"
category: mobile-development
description: "Analyzes an Android app's data layer and persistence strategy: Room schema and migration posture, DataStore vs SharedPreferences usage, caching and single-source-of-truth, repository boundaries, and offline behavior."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - android
  - data-layer
  - persistence
  - room
  - datastore
  - caching
  - analysis
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_networking_layer_analysis.md
  - domain-software-engineering/mobile/android/analysis/android_concurrency_threading_analysis.md
  - domain-software-engineering/mobile/android/implementation/android_data_layer_implementation.md
---

# Android Data Layer & Persistence Analysis

**Objective:** Analyze an Android app's data layer and persistence strategy at the portfolio level — storage-mechanism selection (Room, DataStore, SharedPreferences, files), Room schema design and migration posture, repository boundaries and single-source-of-truth discipline, caching and freshness strategy, and offline/sync behavior — reporting correctness, durability, and maintainability risks with `file:line` evidence and prioritized fixes. This is broader than the narrow Room reviews in `targeted-reviews/`.

**When to Use:** Use this when the app has grown multiple ad-hoc storage paths, when data goes stale or out of sync between screens, before a schema-heavy feature or a migration, when SharedPreferences usage has sprawled, or to establish a coherent data-layer strategy. For a single Room query or migration, use the targeted Room reviews instead.

---

## Context Gathering

1. **Mechanisms:** "Which storage is used — Room, DataStore (Preferences/Proto), SharedPreferences, files, in-memory caches?"
2. **Architecture:** "Repository pattern? Single source of truth (DB-backed) or network-direct?"
3. **Offline:** "Is offline use supported? Any sync between local and remote?"
4. **Symptoms:** "Any stale-data, migration-crash, or 'two screens disagree' issues?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the real storage paths** — find each persistence mechanism and where it's read/written; cite `file:line`.
2. **Confirm impact** — duplicate caches are a problem only if they can diverge; a missing migration matters only if the schema actually changed.
3. **Respect intentional simplicity** — a small app reading network-direct without a DB cache may be fine; don't impose single-source-of-truth where it adds no value.
4. **Separate durability from style** — a migration gap that loses data is a defect; a naming preference is not.

**A coherent, durable data layer is an acceptable outcome.** Don't over-engineer recommendations.

### False-Positive Prevention

- ❌ Do NOT flag SharedPreferences for genuinely simple, non-sensitive flags (migration to DataStore is a nice-to-have, not a defect).
- ❌ Do NOT demand Room where a few key-value settings suffice.
- ❌ Do NOT flag network-direct reads as wrong when offline/caching isn't a requirement.
- ❌ Do NOT flag `fallbackToDestructiveMigration` if it's intentional for non-critical/cache data.
- ✅ DO flag missing/incorrect Room migrations that can crash or lose user data.
- ✅ DO flag multiple competing caches that can diverge.
- ✅ DO flag sensitive data stored unencrypted (cross-reference the local-data security audit).

---

### Phase 1: Persistence Inventory

| Mechanism | Used For | Read/Write Sites | Sensitive? |
|-----------|----------|------------------|------------|
| Room | | | |
| DataStore (Pref/Proto) | | | |
| SharedPreferences | | | |
| Files / `assets` / cache dir | | | |
| In-memory caches | | | |

Note overlaps (the same datum persisted in more than one place).

---

### Phase 2: Room Schema & Migration Posture

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Missing migration | CRITICAL | Schema/version changes without a corresponding `Migration` (crash/data loss) |
| Destructive fallback on real data | HIGH | `fallbackToDestructiveMigration` over user-critical tables |
| No schema export / migration tests | MEDIUM | `exportSchema` off; migrations untested |
| Indexing & relations | MEDIUM | Missing indices on queried columns; N+1 via relations |
| Type/converter risks | LOW | Fragile `TypeConverter`s; storing JSON blobs that should be columns |
| Main-thread DB access | HIGH | `allowMainThreadQueries` or synchronous DAO calls on UI thread |

---

### Phase 3: Source-of-Truth & Caching Strategy

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Competing caches | HIGH | Same data cached in DB + memory + prefs that can diverge |
| No single source of truth | MEDIUM | UI reads network and DB inconsistently; stale screens |
| Cache invalidation | MEDIUM | No freshness/TTL strategy; stale data never refreshed |
| Reactive consistency | MEDIUM | Writes not propagated via `Flow`/observers (screens don't update) |
| Repository boundary leaks | MEDIUM | DAOs/`SharedPreferences`/Retrofit used directly from UI/ViewModel |
| Over-fetch/over-store | LOW | Persisting data never read back |

---

### Phase 4: Offline, Durability & Integrity

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Offline correctness | MEDIUM | Reads/writes assume connectivity; no queued/local-first path |
| Write durability | HIGH | Critical writes not transactional/atomic; partial-write corruption risk |
| Conflict handling | MEDIUM | Local/remote conflicts unhandled on sync (cross-ref offline-conflict review) |
| Backup exposure | MEDIUM | Sensitive persisted data included in auto-backup (cross-ref manifest audit) |
| Migration of prefs/files | LOW | Format changes to prefs/files without a migration path |

---

## Output Format

```markdown
## Android Data Layer & Persistence Analysis Report

### Persistence Map
| Data | Mechanism(s) | Source of truth | Risk |
|------|--------------|-----------------|------|

### Findings (severity-ordered)
**[SEVERITY] Area: title** — Location `file:line` · Risk (durability/staleness/maintainability) · Fix

### Strategy Recommendations
- Source-of-truth model, caching/freshness policy, mechanism consolidation.

### Prioritized Remediation (P1/P2/P3)

### What's Already Solid
```

---

## Expected Output

1. **Persistence map** (mechanisms and source-of-truth).
2. **Severity-rated findings** (migrations, caches, durability) with locations and fixes.
3. **Data-layer strategy recommendations.**
4. **Prioritized remediation.**

---

## Techniques Used

- **ST-01** (Clear Objective): Data-layer/persistence scope.
- **ST-02** (Structured Sequential Instructions): Inventory → Room → source-of-truth → durability.
- **RT-02** (Multi-Dimensional Analysis): Durability + freshness + maintainability.
- **RT-05** (Evidence-Based Reasoning): Read/write site citations.
- **DS-06** (Prioritization Guidance): Severity ordering.

---

## Related Prompts

- [android_networking_layer_analysis.md](android_networking_layer_analysis.md) - The remote half of the data flow
- [android_concurrency_threading_analysis.md](android_concurrency_threading_analysis.md) - Threading behind DB/IO access
- [android_data_layer_implementation.md](../implementation/android_data_layer_implementation.md) - Implement the recommended data layer
