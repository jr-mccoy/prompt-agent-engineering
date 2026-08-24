---
title: "iOS Data Retention Policy Design"
category: mobile-development
description: "Design data retention and lifecycle management policies for iOS apps including storage limits, cache eviction, user data deletion, and privacy compliance."
techniques:
  - ST-01
  - RT-02
difficulty: intermediate
tags:
  - ios
  - swift
  - data-retention
  - privacy
updated: "2026-03-20"
---

# iOS Data Retention Policy Design

**Objective:** Design a comprehensive data retention and lifecycle management policy for an iOS app covering storage budgets, cache eviction strategies, user data deletion (right-to-be-forgotten), iCloud storage management, and App Store privacy compliance.

**When to Use:** Use when designing the data layer of any app that stores user data locally, caches media, or syncs with cloud services. Essential for apps subject to GDPR, CCPA, HIPAA, or COPPA. Also valuable when users report "this app uses too much storage."

**Prompt Type:** Modular (200-300 lines)

---

## Context Gathering

Before designing retention policies, gather essential context:

1. **Data Inventory:**
   - "What data does the app store locally (user content, caches, logs, analytics)?"
   - "What data is synced to cloud services?"
   - "What third-party SDKs store data on device?"

2. **Regulatory:**
   - "Is the app subject to GDPR, CCPA, HIPAA, COPPA, or other regulations?"
   - "Does the app target the EU or California?"
   - "Is there a legal requirement for data retention duration?"

3. **User Expectations:**
   - "Do users expect their data to persist indefinitely or is it ephemeral?"
   - "Is there a premium tier with different storage limits?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before designing ANY retention policy, you MUST:**

1. **Audit all data storage locations** - Local files, UserDefaults, Keychain, SwiftData, CloudKit, third-party SDKs.
2. **Classify data by sensitivity** - PII, PHI, financial, behavioral, cached, transient.
3. **Define retention periods per data class** - With legal and product justification.
4. **Implement right-to-delete** - Complete account/data deletion must be possible per Apple's App Store requirement.

### False-Positive Prevention

- ❌ Do NOT store sensitive data in UserDefaults (not encrypted)
- ❌ Do NOT retain analytics data indefinitely on device
- ❌ Do NOT forget to clear data on account deletion (including Keychain, caches, and CloudKit)
- ❌ Do NOT assume iOS will manage your storage automatically
- ✅ DO classify every data type with a retention period
- ✅ DO implement automatic cleanup for expired data
- ✅ DO provide users visibility into storage usage
- ✅ DO test account deletion flow end-to-end

---

### Phase 1: Data Classification

#### 1.1 Data Inventory Matrix

```markdown
| Data Type | Storage Location | Sensitivity | Retention | Size Impact | Encrypted |
|-----------|-----------------|-------------|-----------|-------------|-----------|
| User profile | SwiftData | PII | Until deletion | Minimal | At rest |
| Auth tokens | Keychain | Credential | Session/refresh | Minimal | Yes |
| Cached images | FileManager/Caches | Low | 7 days | High | No |
| Search history | UserDefaults | Behavioral | 30 days | Low | No |
| Analytics events | SQLite queue | Behavioral | Until upload | Low | No |
| Downloaded media | FileManager/Documents | User content | Until user deletes | Very High | Optional |
| Crash logs | FileManager/tmp | Diagnostic | 48 hours | Low | No |
| CloudKit records | iCloud | Varies | Sync policy | Shared quota | Apple managed |
```

#### 1.2 Storage Budget

```markdown
| Category | Budget | Eviction Strategy |
|----------|--------|-------------------|
| App binary + assets | ~50MB | Managed by App Store |
| User-created content | Unlimited (user's storage) | User manages |
| Image cache | 200MB max | LRU eviction |
| Network response cache | 50MB max | TTL-based |
| Logs and diagnostics | 10MB max | FIFO rotation |
| Temporary files | 0 (clean on use) | Immediate cleanup |
| **Total managed cache** | **260MB max** | Automatic |
```

---

### Phase 2: Retention Implementation

#### 2.1 Cache Management

```swift
// File: Core/Storage/CacheManager.swift

import Foundation

actor CacheManager {
    static let shared = CacheManager()

    private let fileManager = FileManager.default
    private let imageCacheBudget: Int64 = 200 * 1024 * 1024 // 200MB

    /// Evict expired and over-budget cache entries
    func performMaintenance() async {
        // 1. Remove expired items (TTL-based)
        removeExpiredItems(in: cacheDirectory, maxAge: 7 * 24 * 3600)

        // 2. Enforce size budget (LRU eviction)
        enforceStorageBudget(in: imageCacheDirectory, budget: imageCacheBudget)

        // 3. Clean tmp directory
        cleanTemporaryFiles()
    }

    private func removeExpiredItems(in directory: URL, maxAge: TimeInterval) {
        guard let contents = try? fileManager.contentsOfDirectory(
            at: directory,
            includingPropertiesForKeys: [.contentModificationDateKey],
            options: .skipsHiddenFiles
        ) else { return }

        let cutoff = Date().addingTimeInterval(-maxAge)
        for url in contents {
            if let date = try? url.resourceValues(forKeys: [.contentModificationDateKey]).contentModificationDate,
               date < cutoff {
                try? fileManager.removeItem(at: url)
            }
        }
    }

    private func enforceStorageBudget(in directory: URL, budget: Int64) {
        guard let contents = try? fileManager.contentsOfDirectory(
            at: directory,
            includingPropertiesForKeys: [.fileSizeKey, .contentAccessDateKey],
            options: .skipsHiddenFiles
        ) else { return }

        // Sort by last access (LRU)
        let sorted = contents.sorted { a, b in
            let dateA = (try? a.resourceValues(forKeys: [.contentAccessDateKey]).contentAccessDate) ?? .distantPast
            let dateB = (try? b.resourceValues(forKeys: [.contentAccessDateKey]).contentAccessDate) ?? .distantPast
            return dateA < dateB
        }

        var totalSize: Int64 = sorted.reduce(0) { sum, url in
            sum + Int64((try? url.resourceValues(forKeys: [.fileSizeKey]).fileSize) ?? 0)
        }

        // Remove oldest files until under budget
        for url in sorted {
            guard totalSize > budget else { break }
            let size = Int64((try? url.resourceValues(forKeys: [.fileSizeKey]).fileSize) ?? 0)
            try? fileManager.removeItem(at: url)
            totalSize -= size
        }
    }

    private var cacheDirectory: URL {
        fileManager.urls(for: .cachesDirectory, in: .userDomainMask)[0]
    }

    private var imageCacheDirectory: URL {
        cacheDirectory.appendingPathComponent("ImageCache", isDirectory: true)
    }

    private func cleanTemporaryFiles() {
        let tmp = fileManager.temporaryDirectory
        try? fileManager.contentsOfDirectory(at: tmp, includingPropertiesForKeys: nil)
            .forEach { try? fileManager.removeItem(at: $0) }
    }
}
```

#### 2.2 Account Deletion (Right to Delete)

```swift
// File: Core/Storage/AccountDeletionService.swift

actor AccountDeletionService {
    /// Complete data erasure -- required by App Store guidelines
    func deleteAllUserData() async throws {
        // 1. Delete server-side data
        try await deleteRemoteData()

        // 2. Delete local persistence (SwiftData/Core Data)
        try deleteLocalDatabase()

        // 3. Clear Keychain
        clearKeychain()

        // 4. Clear UserDefaults
        clearUserDefaults()

        // 5. Clear all caches
        await CacheManager.shared.clearAll()

        // 6. Delete CloudKit records (if applicable)
        try await deleteCloudKitData()

        // 7. Delete downloaded files
        deleteUserFiles()

        // 8. Reset analytics identity
        resetAnalytics()
    }

    private func clearKeychain() {
        let secClasses = [
            kSecClassGenericPassword,
            kSecClassInternetPassword,
            kSecClassCertificate,
            kSecClassKey,
            kSecClassIdentity
        ]
        for secClass in secClasses {
            SecItemDelete([kSecClass: secClass] as CFDictionary)
        }
    }

    private func clearUserDefaults() {
        guard let domain = Bundle.main.bundleIdentifier else { return }
        UserDefaults.standard.removePersistentDomain(forName: domain)
    }
}
```

---

### Phase 3: Privacy Compliance

**CHECKPOINT:** Verify all data types have retention periods and deletion paths.

```markdown
## Retention Policy Summary
| Data Class | Retention | Auto-Cleanup | Delete on Account Removal |
|-----------|-----------|-------------|--------------------------|
| User content | Permanent | No | Yes |
| Credentials | Session | On logout | Yes |
| Caches | 7 days | Yes (daily) | Yes |
| Analytics | Until upload | Yes | Yes |
| Logs | 48 hours | Yes | Yes |

**All data deletable on account removal?** [Yes/No]
```

#### 3.1 App Privacy Nutrition Label

```markdown
## Data Linked to User
| Data Type | Purpose | Linked to Identity |
|-----------|---------|-------------------|
| Email | Account | Yes |
| Name | Personalization | Yes |
| Usage data | Analytics | No (anonymized) |
| Crash data | Diagnostics | No |

## Data NOT Collected
- Location (unless feature requires)
- Contacts
- Browsing history
```

---

## Expected Output

A data retention policy document with classification matrix, storage budgets, cleanup implementation, account deletion flow, and privacy compliance checklist.

---

## Example Interaction

**User:** "Our photo journaling app stores photos locally and in iCloud. Users in EU. iOS 17+."

**Assistant:**

**Key policies:**
1. **Photos:** Stored in Documents/ (backed up by iOS). iCloud sync via CloudKit. No automatic deletion -- user controls lifecycle. Account deletion removes CloudKit records + local files.
2. **Thumbnails cache:** 100MB budget in Caches/ (not backed up). LRU eviction. Regenerated on demand.
3. **GDPR compliance:** Data export via Share Sheet (photos + metadata as JSON). Account deletion within 48 hours (immediate local, async CloudKit cleanup).
4. **Storage indicator:** Show "X MB used locally, Y MB in iCloud" in Settings.

---

## Techniques Used

- **ST-01** (Clear Objective): Design retention policy with compliance requirements
- **RT-02** (Multi-Dimensional Analysis): Covers classification, implementation, and compliance

---

## Related Prompts

- [ios_offline_first_architecture.md](ios_offline_first_architecture.md) - Offline data persistence design
- [ios_feature_specification.md](ios_feature_specification.md) - Feature-level data requirements

---

## Customization Guide

### For HIPAA-Compliant Apps
Add: encryption at rest (NSFileProtectionComplete), audit logging for all data access, BAA requirements for cloud storage, and automatic session timeout with data lock.

### For Children's Apps (COPPA)
Add: no persistent identifiers for users under 13, parental consent flow before any data collection, no behavioral analytics, automatic data deletion after 30 days of inactivity.
