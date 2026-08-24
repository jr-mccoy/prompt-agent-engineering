---
title: "iOS Local Data Security Audit"
category: mobile-development
description: "Audit local data security across Keychain, Data Protection, UserDefaults, Core Data, file system, and clipboard to identify sensitive data exposure risks and remediation steps"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
difficulty: advanced
tags:
  - ios
  - swift
  - security
  - keychain
  - data-protection
updated: "2026-03-20"
---

# iOS Local Data Security Audit

**Objective:** Audit all local data storage mechanisms in an iOS app — Keychain, Data Protection API, UserDefaults, Core Data/SwiftData, file system, pasteboard, and caches — to identify sensitive data stored insecurely, missing encryption, improper protection classes, and data leakage vectors, then provide prioritized remediation guidance.

**When to Use:** Use this prompt during security reviews, before App Store submission for sensitive apps (finance, healthcare, enterprise), when preparing for penetration testing, after a security incident, or when compliance requirements (HIPAA, PCI-DSS, SOC 2) mandate data-at-rest security audits.

**Prompt Type:** Comprehensive (350-500 lines)

---

## Context Gathering

Before beginning the audit, gather context:

1. **Data Sensitivity:**
   - "What types of sensitive data does the app handle (credentials, PII, financial, health, tokens)?"
   - "Are there specific compliance requirements (HIPAA, PCI-DSS, GDPR, SOC 2)?"

2. **Current Security Posture:**
   - "Has a security audit been done before? Are there known findings?"
   - "Is there a security-focused abstraction layer for storage, or do features access storage APIs directly?"

3. **Threat Model:**
   - "What is the threat model? (Casual attacker, jailbroken device, physical access, state-level adversary)"
   - "Does the app support managed devices (MDM) or shared devices?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Confirm data sensitivity** - Not all data in UserDefaults is sensitive. Verify what's actually stored before flagging.
2. **Check the full storage path** - Data might be encrypted at a higher level even if the storage API itself doesn't encrypt.
3. **Verify protection class appropriateness** - `completeUntilFirstUserAuthentication` is appropriate for background-fetched data. Not everything needs `complete`.
4. **Assess real-world exploitability** - A finding on a non-jailbroken device with full disk encryption is different from one exploitable via backup extraction.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**An app that stores non-sensitive preferences in UserDefaults and credentials in Keychain is doing the right thing.** Don't flag appropriate storage choices as vulnerabilities.

### False-Positive Prevention

- ❌ Do NOT flag UserDefaults for non-sensitive data (UI preferences, feature flags, onboarding state)
- ❌ Do NOT flag Core Data as insecure if it stores non-sensitive content data
- ❌ Do NOT require Keychain for data that has no sensitivity
- ❌ Do NOT flag file caching as a vulnerability without checking what's cached
- ✅ DO verify what data is actually written to each storage location
- ✅ DO check if there's an encryption wrapper around standard storage APIs
- ✅ DO consider the device passcode as the first line of defense for Data Protection
- ✅ DO assess the threat model before assigning severity

---

### Phase 1: Storage Mechanism Inventory

#### 1.1 Keychain Usage Audit

**Scan for Keychain interactions:**

```swift
// Direct Keychain API usage
SecItemAdd(_:_:)
SecItemCopyMatching(_:_:)
SecItemUpdate(_:_:)
SecItemDelete(_:)

// Keychain wrapper libraries
import KeychainAccess       // kishikawakatsumi/KeychainAccess
import SwiftKeychainWrapper // jrendel/SwiftKeychainWrapper
import Valet                // Square/Valet

// What to check for each Keychain item:

// 1. Access control (kSecAttrAccessControl)
let access = SecAccessControlCreateWithFlags(
    nil,
    kSecAttrAccessibleWhenUnlockedThisDeviceOnly,  // Protection class
    .biometryCurrentSet,                           // Biometric requirement
    nil
)

// 2. Protection class (kSecAttrAccessible)
kSecAttrAccessibleWhenUnlocked                    // Available when unlocked
kSecAttrAccessibleWhenUnlockedThisDeviceOnly      // + no backup migration
kSecAttrAccessibleAfterFirstUnlock                // Available after first unlock
kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly  // + no backup migration
kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly   // Requires passcode, device-only
// DEPRECATED:
kSecAttrAccessibleAlways                          // NEVER USE — available even when locked

// 3. Keychain sharing (kSecAttrAccessGroup)
// Check if items are shared across apps unintentionally
```

**Keychain Audit Table:**

| Item Stored | Protection Class | ThisDeviceOnly | Biometric Guard | Access Group | Finding |
|------------|-----------------|----------------|-----------------|-------------|---------|
| Auth token | [Class] | [Yes/No] | [Yes/No] | [Group] | [OK/Issue] |
| User password | [Class] | [Yes/No] | [Yes/No] | [Group] | [OK/Issue] |
| API key | [Class] | [Yes/No] | [Yes/No] | [Group] | [OK/Issue] |

#### 1.2 Data Protection Classes

**Check file protection attributes:**

```swift
// File protection levels
FileProtectionType.complete                      // Locked = encrypted, no background access
FileProtectionType.completeUnlessOpen            // Files can stay open in background
FileProtectionType.completeUntilFirstUserAuthentication  // Default — available after first unlock
FileProtectionType.none                          // No encryption — RED FLAG for sensitive data

// How to check:
let attributes = try FileManager.default.attributesOfItem(atPath: path)
let protection = attributes[.protectionKey] as? FileProtectionType

// How to set:
try data.write(to: url, options: .completeFileProtection)
try FileManager.default.setAttributes(
    [.protectionKey: FileProtectionType.complete],
    ofItemAtPath: path
)

// Entitlements check:
// com.apple.developer.default-data-protection = NSFileProtectionComplete
```

**Data Protection Assessment:**

| Storage Location | Protection Level | Contains Sensitive Data | Appropriate |
|-----------------|-----------------|----------------------|------------|
| App Documents/ | [Level] | [Yes/No — what] | [Yes/No] |
| App Library/ | [Level] | [Yes/No — what] | [Yes/No] |
| App Caches/ | [Level] | [Yes/No — what] | [Yes/No] |
| App tmp/ | [Level] | [Yes/No — what] | [Yes/No] |
| Shared container | [Level] | [Yes/No — what] | [Yes/No] |

#### 1.3 UserDefaults Audit

**Scan for sensitive data in UserDefaults:**

```swift
// RED FLAGS — sensitive data in UserDefaults:
UserDefaults.standard.set(token, forKey: "authToken")       // Should be Keychain
UserDefaults.standard.set(password, forKey: "userPassword")  // Should be Keychain
UserDefaults.standard.set(ssn, forKey: "socialSecurity")     // Should be Keychain
UserDefaults.standard.set(cardNumber, forKey: "creditCard")  // Should be Keychain

// ACCEPTABLE — non-sensitive preferences:
UserDefaults.standard.set(true, forKey: "hasCompletedOnboarding")
UserDefaults.standard.set("dark", forKey: "themePreference")
UserDefaults.standard.set(Date(), forKey: "lastSyncDate")

// Also check App Groups UserDefaults:
UserDefaults(suiteName: "group.com.app.shared")?.set(data, forKey: key)

// Check for UserDefaults backed by plist files (readable in iTunes backups):
// ~/Library/Preferences/com.app.bundle.plist
```

| UserDefaults Key | Value Type | Sensitive | Storage Appropriate | Finding |
|-----------------|-----------|-----------|-------------------|---------|
| [Key] | [Type] | [Yes/No] | [Yes/No] | [OK/Move to Keychain] |

---

### Phase 2: Database and Cache Security

#### 2.1 Core Data / SwiftData Security

**Audit persistent store security:**

```swift
// Core Data store encryption check:
let description = NSPersistentStoreDescription()

// Check for encryption:
description.setOption(
    FileProtectionType.complete as NSObject,
    forKey: NSPersistentStoreFileProtectionKey
)

// Check what's stored in the database:
// Scan entity attributes for sensitive fields
// - Passwords, tokens, PII in plain text
// - Health data, financial data
// - Biometric template data

// SwiftData:
let config = ModelConfiguration(
    // Check: isStoredInMemoryOnly
    // Check: cloudKitDatabase (sync security)
)
// SwiftData inherits file protection from container

// SQLite file location:
// Application Support/Model.sqlite — check protection class
```

**Database Content Audit:**

| Entity | Sensitive Attributes | Encrypted | Protection Class | Finding |
|--------|---------------------|-----------|-----------------|---------|
| [Entity] | [Attribute list] | [Yes/No] | [Class] | [OK/Issue] |

#### 2.2 Cache Security

**Audit caching mechanisms:**

```swift
// URLCache — may cache sensitive API responses
let cache = URLCache.shared
// Check: Is sensitive data being cached?
// Check: Cache policy on requests with auth headers

// Image caches
// Kingfisher, SDWebImage, Nuke — may cache user profile photos, documents
// Check: Cache location and protection class

// NSCache / in-memory caches
// Generally OK — cleared on memory pressure and app termination
// Check: Not written to disk as a persistence strategy

// WebView caches
// WKWebView stores cookies, cache, local storage
// Check: WKWebsiteDataStore for sensitive web content
```

#### 2.3 Temporary File Security

**Audit temporary file handling:**

```swift
// Temp directory usage
let tmpDir = FileManager.default.temporaryDirectory
// Files here survive app restart but not device restart
// Check: Sensitive files cleaned up after use

// Check for sensitive data in:
// - Export files (PDFs, CSVs with user data)
// - Decrypted file copies
// - Image processing intermediates
// - Debug logs

// Pattern: Write-Use-Delete
let tempURL = tmpDir.appendingPathComponent(UUID().uuidString)
try sensitiveData.write(to: tempURL, options: .completeFileProtection)
defer { try? FileManager.default.removeItem(at: tempURL) }
// Process file...
```

---

### Phase 3: Data Leakage Vectors

#### 3.1 Clipboard / Pasteboard Security

**Audit pasteboard usage:**

```swift
// Check for sensitive data copied to pasteboard:
UIPasteboard.general.string = password       // RED FLAG
UIPasteboard.general.string = creditCard     // RED FLAG
UIPasteboard.general.string = otp            // Acceptable with expiration

// Mitigation: Local-only pasteboard with expiration
let pasteboard = UIPasteboard(name: .init("com.app.secure"), create: true)
pasteboard?.setItems([[kUTTypePlainText as String: otp]],
    options: [.localOnly: true,
              .expirationDate: Date().addingTimeInterval(60)])

// Check: Do password fields set .isSecureTextEntry = true?
// Secure text entry prevents system clipboard learning

// iOS 16+: Check for UIPasteControl adoption for paste permission
```

#### 3.2 Snapshot / Background Image

**Audit background snapshot protection:**

```swift
// iOS takes a snapshot when app enters background
// This snapshot is visible in app switcher

// Check: Is sensitive data visible in background snapshot?
// Mitigation patterns:

// 1. Blur overlay
func applicationDidEnterBackground(_ application: UIApplication) {
    let blurView = UIVisualEffectView(effect: UIBlurEffect(style: .regular))
    blurView.frame = window!.bounds
    blurView.tag = 999
    window?.addSubview(blurView)
}

// 2. Placeholder view
// 3. Hide sensitive fields in sceneDidEnterBackground

// SwiftUI:
.onChange(of: scenePhase) { phase in
    if phase == .background { showSecurityOverlay = true }
}
```

#### 3.3 Logging and Debug Data

**Audit for sensitive data in logs:**

```swift
// RED FLAGS:
print("User token: \(token)")                    // Console log
os_log("Password: %@", password)                 // System log
Logger().info("API key: \(apiKey)")              // Unified logging
NSLog("Credit card: %@", cardNumber)             // NSLog persists!

// Check for:
// - Sensitive data in os_log / Logger calls
// - Network request/response logging that includes auth headers
// - Crash report symbolication that includes user data
// - Analytics events with PII

// GOOD: Redacting sensitive data
Logger().info("Auth result: \(result, privacy: .private)")
```

#### 3.4 Backup Security

**Audit iTunes/Finder backup exposure:**

```swift
// Files in Documents/ and Library/ are included in backups by default
// Exclude sensitive files from backup:
var url = sensitiveFileURL
var resourceValues = URLResourceValues()
resourceValues.isExcludedFromBackup = true
try url.setResourceValues(resourceValues)

// Check: Keychain items with ThisDeviceOnly prevent backup migration
// Check: Core Data stores with sensitive data — are they excluded from backup?
// Check: Are encryption keys stored separately from encrypted data?
```

---

### Phase 4: Findings and Remediation

**CHECKPOINT:** Present security findings summary.

```markdown
## Local Data Security Audit Results

### Risk Summary

| Severity | Count | Category |
|----------|-------|----------|
| Critical | [N] | [Details] |
| High | [N] | [Details] |
| Medium | [N] | [Details] |
| Low | [N] | [Details] |
| Info | [N] | [Details] |

### Top Critical Findings

1. **[Finding]** - [Location] - [Impact]
2. **[Finding]** - [Location] - [Impact]

### Remediation Priority

| Finding | Severity | Effort | Recommended Fix |
|---------|----------|--------|----------------|
| [Finding] | [Sev] | [Hours/Days] | [Fix description] |

**Shall I provide detailed remediation code examples?**
```

---

## Expected Output

1. **Storage Inventory** - Complete map of all local data storage with sensitivity classification
2. **Keychain Audit** - Protection class and access control assessment for all Keychain items
3. **Data Protection Review** - File protection levels for all storage locations
4. **Leakage Vector Analysis** - Clipboard, snapshot, logging, and backup exposure assessment
5. **Prioritized Findings** - All issues ranked by severity with remediation guidance

---

## Example Interaction

**User:** Audit the local data security of our iOS healthcare app. We handle patient data and need HIPAA compliance.

**Agent:** I'll conduct a comprehensive local data security audit focused on PHI (Protected Health Information) handling. Let me scan all storage mechanisms.

*[Agent audits Keychain, UserDefaults, Core Data, file system, and leakage vectors]*

**Agent:**

## Local Data Security Audit — Healthcare App

### Critical Findings (Immediate Action Required)

1. **Patient SSN stored in UserDefaults** — `PatientProfileManager.swift:45`
   - `UserDefaults.standard.set(patient.ssn, forKey: "lastPatientSSN")`
   - **Impact:** SSN visible in plaintext backup, no encryption at rest
   - **Fix:** Move to Keychain with `kSecAttrAccessibleWhenUnlockedThisDeviceOnly`

2. **Core Data store has no file protection** — `PersistenceController.swift:23`
   - Patient records, diagnoses, and medication data stored without `NSPersistentStoreFileProtectionKey`
   - **Impact:** Data accessible on locked device after first unlock
   - **Fix:** Set `FileProtectionType.complete` on persistent store

3. **API auth token logged in production** — `NetworkService.swift:112`
   - `Logger().info("Request headers: \(request.allHTTPHeaderFields)")`
   - **Impact:** Bearer token visible in device Console logs
   - **Fix:** Redact auth headers or remove header logging in production

### Medium Findings

4. **Background snapshot shows patient data** — No blur/overlay on backgrounding
5. **Patient photos cached without protection** — `ImageCache/` directory uses default protection class

**Shall I provide remediation code for each finding?**

---

## Techniques Used

- **ST-01** (Clear Objective): Focused data-at-rest security audit
- **ST-02** (Sequential Instructions): Phased audit from inventory through remediation
- **RT-02** (Multi-Dimensional Analysis): Six storage mechanisms, four leakage vectors
- **RT-04** (Best Practice Review): iOS security best practices and compliance requirements

---

## Related Prompts

- [ios_authentication_security_audit.md](ios_authentication_security_audit.md) - Authentication and session security
- [ios_cloud_backend_security_audit.md](ios_cloud_backend_security_audit.md) - Cloud and network security
- [ios_codebase_health_assessment.md](ios_codebase_health_assessment.md) - Overall codebase evaluation

---

## Customization Guide

### For HIPAA Compliance
- Require encryption at rest for all PHI (Protected Health Information)
- Verify audit logging for PHI access
- Check for BAA (Business Associate Agreement) compliance in third-party SDKs
- Ensure device passcode requirement is enforced via MDM or app logic
- Verify PHI is excluded from backups or backups are encrypted

### For Financial / PCI-DSS Apps
- Check that cardholder data is never stored locally (or stored per PCI-DSS requirements)
- Verify no PAN (Primary Account Number) in logs, caches, or pasteboard
- Check for secure keyboard usage on payment input fields
- Verify tokenization is used instead of raw card storage

### For Enterprise / MDM Apps
- Check for managed app configuration data handling
- Verify Open-In restrictions (managed vs unmanaged document flow)
- Assess per-app VPN integration for data-in-transit
- Check Data Protection entitlements in provisioning profile

### For Apps with Offline Mode
- Audit offline data cache encryption
- Check credential storage duration for offline auth
- Verify offline data sync queue doesn't expose sensitive data in plaintext
- Assess auto-lock behavior and data protection implications
