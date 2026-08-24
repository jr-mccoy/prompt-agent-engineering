---
title: "iOS Data Protection Review"
category: mobile-development
description: "Review Data Protection API usage for protection classes, Keychain accessibility levels, shared container security, and file-level encryption compliance."
techniques:
  - ST-01
  - RT-02
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - code-review
  - security
  - data-protection
  - encryption
updated: "2026-03-19"
---

# iOS Data Protection Review

**Objective:** Audit Data Protection API usage for correct file protection class assignment, Keychain accessibility alignment with data sensitivity, App Group shared container security, and compliance with platform encryption requirements to prevent data exposure on lost or compromised devices.

**When to Use:** Apply when reviewing file storage code, configuring App Group containers, preparing for security audits, or when handling sensitive data (PII, PHI, financial records) that requires at-rest encryption.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What types of sensitive data does the app store on disk (PII, health data, financial)?
2. Are App Groups used for sharing data with extensions or other apps?
3. Does the app need to access files while the device is locked (e.g., background downloads)?
4. What compliance requirements apply (HIPAA, PCI DSS, GDPR)?

## Instructions

### CRITICAL: Verification Requirements

- Sensitive files must use .completeProtection or .completeUnlessOpen — not .none
- Keychain accessibility must match the data sensitivity and access pattern
- App Group containers must not store unencrypted sensitive data accessible to extensions
- Database files (SQLite, Core Data) must have file protection attributes set

### False-Positive Prevention

- ❌ Do NOT flag .completeUntilFirstUserAuthentication for non-sensitive config files needed in background
- ✅ DO flag .completeUntilFirstUserAuthentication for passwords, tokens, or PII
- ❌ Do NOT flag shared container usage for non-sensitive data (widget display data, preferences)
- ✅ DO flag shared container storage of auth tokens or PII without additional encryption
- ❌ Do NOT flag .none protection for truly public, non-sensitive cache files
- ✅ DO flag .none protection on any file containing user data

1. **File Protection Classes**

```swift
// BAD: Sensitive file with no explicit protection — defaults vary by device state
let documentsURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
let healthDataURL = documentsURL.appendingPathComponent("health_records.json")
try data.write(to: healthDataURL)
// No protection class set — may be accessible when device is locked

// GOOD: Explicit protection class for sensitive files
let healthDataURL = documentsURL.appendingPathComponent("health_records.json")
try data.write(to: healthDataURL, options: .completeFileProtection)

// Or set via FileManager
try FileManager.default.setAttributes(
    [.protectionKey: FileProtectionType.complete],
    ofItemAtPath: healthDataURL.path
)

// Verify protection
let attrs = try FileManager.default.attributesOfItem(atPath: healthDataURL.path)
let protection = attrs[.protectionKey] as? FileProtectionType
assert(protection == .complete)
```

2. **Database File Protection**

```swift
// BAD: Core Data store with no file protection
let storeURL = documentsURL.appendingPathComponent("UserData.sqlite")
let description = NSPersistentStoreDescription(url: storeURL)
// No file protection options set

// GOOD: Protected Core Data store
let description = NSPersistentStoreDescription(url: storeURL)
description.setOption(
    FileProtectionType.complete as NSObject,
    forKey: NSPersistentStoreFileProtectionKey
)
container.persistentStoreDescriptions = [description]

// For SQLite directly
let dbPath = documentsURL.appendingPathComponent("app.db").path
sqlite3_open_v2(dbPath, &db, SQLITE_OPEN_READWRITE | SQLITE_OPEN_CREATE, nil)
try FileManager.default.setAttributes(
    [.protectionKey: FileProtectionType.complete],
    ofItemAtPath: dbPath
)
```

3. **App Group Container Security**

```swift
// BAD: Auth token in shared container without protection
let sharedDefaults = UserDefaults(suiteName: "group.com.app.shared")
sharedDefaults?.set(authToken, forKey: "token")
// Token accessible to all apps/extensions in group, no encryption

// GOOD: Encrypt sensitive data in shared containers
let sharedContainer = FileManager.default.containerURL(
    forSecurityApplicationGroupIdentifier: "group.com.app.shared"
)!

// Store non-sensitive widget display data in shared defaults
let sharedDefaults = UserDefaults(suiteName: "group.com.app.shared")
sharedDefaults?.set(unreadCount, forKey: "badge_count") // non-sensitive, OK

// Store sensitive data in Keychain with access group instead
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrAccount as String: "shared_token",
    kSecAttrAccessGroup as String: "TEAM_ID.com.app.shared",
    kSecValueData as String: tokenData,
    kSecAttrAccessible as String: kSecAttrAccessibleWhenUnlockedThisDeviceOnly
]
```

4. **Temporary File Cleanup**

```swift
// BAD: Sensitive data in tmp directory — no protection, no cleanup
let tmpFile = NSTemporaryDirectory() + "export.csv"
try sensitiveCSV.write(toFile: tmpFile, atomically: true, encoding: .utf8)
// File persists indefinitely with .none protection

// GOOD: Protected temporary file with cleanup
let tmpURL = FileManager.default.temporaryDirectory
    .appendingPathComponent(UUID().uuidString + ".csv")
try sensitiveCSV.write(to: tmpURL, atomically: true, encoding: .utf8)
try FileManager.default.setAttributes(
    [.protectionKey: FileProtectionType.complete],
    ofItemAtPath: tmpURL.path
)

defer {
    try? FileManager.default.removeItem(at: tmpURL)
}
// Use tmpURL for export, then cleaned up
```

## Expected Output

```
## Data Protection Review Report

### Summary
- **Files/stores reviewed:** N
- **Missing protection class:** N
- **Incorrect protection level:** N
- **Shared container risks:** N
- **Temporary file issues:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Data at risk:** Type of data exposed
- **Recommendation:** ...
```

## Example Output

```
## Data Protection Review Report

### Summary
- **Files/stores reviewed:** 11
- **Missing protection class:** 3
- **Incorrect protection level:** 1
- **Shared container risks:** 1
- **Temporary file issues:** 2

### Findings

#### [Critical] Unprotected Database — DataStore.swift:L45
- **Issue:** Core Data store containing user PII has no NSPersistentStoreFileProtectionKey set.
- **Data at risk:** Names, emails, addresses for all users.
- **Recommendation:** Add `.complete` file protection to store description.

#### [Warning] Token in Shared Defaults — WidgetDataProvider.swift:L12
- **Issue:** OAuth access token stored in UserDefaults(suiteName:) for widget access.
- **Data at risk:** Auth token readable by any extension in the app group.
- **Recommendation:** Use Keychain with shared access group instead of UserDefaults.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates file protection, database, containers, temp files
- **RT-02 (Role-Based Task Framing):** Reviewer acts as iOS data protection specialist
- **AG-02 (Automated Guardrails):** Prevents false flags on non-sensitive shared data

## Related Prompts

- `ios_keychain_biometric_review.md` — Keychain credential security
- `ios_app_transport_security_review.md` — Network data-in-transit security
- `ios_jailbreak_tamper_detection_review.md` — Device integrity verification

## Customization Guide

- **HIPAA compliance:** Add PHI-specific checks and Business Associate Agreement documentation requirements
- **Financial apps:** Add PCI DSS data storage requirements for cardholder data
- **Enterprise apps:** Add MDM profile enforcement checks for data protection policies
