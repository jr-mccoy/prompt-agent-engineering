---
title: "iOS Keychain & Biometric Authentication Review"
category: mobile-development
description: "Review Keychain Services usage for access control flags, kSecAttrAccessible values, LAContext biometric integration, and Secure Enclave key management."
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
  - security
  - keychain
  - biometrics
updated: "2026-03-19"
---

# iOS Keychain & Biometric Authentication Review

**Objective:** Audit Keychain Services implementation for correct access control flags, appropriate kSecAttrAccessible protection levels, LAContext biometric authentication integration, and Secure Enclave key management to prevent credential exposure and ensure authentication reliability.

**When to Use:** Apply when reviewing authentication flows, credential storage, biometric unlock features, or when conducting security audits for App Store review or compliance requirements.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What types of credentials are stored (tokens, passwords, encryption keys, certificates)?
2. Is biometric authentication (Face ID / Touch ID) used for app unlock or transaction confirmation?
3. Are Keychain items shared across apps via Keychain Access Groups?
4. Is the Secure Enclave used for cryptographic key generation?

## Instructions

### CRITICAL: Verification Requirements

- Sensitive credentials must use kSecAttrAccessibleWhenUnlockedThisDeviceOnly or stricter
- Biometric-protected items must use SecAccessControl with .biometryCurrentSet (not .biometryAny)
- LAContext evaluation must check canEvaluatePolicy before evaluatePolicy
- Keychain queries must handle errSecItemNotFound and errSecAuthFailed gracefully

### False-Positive Prevention

- ❌ Do NOT flag kSecAttrAccessibleAfterFirstUnlock for push notification tokens — they need background access
- ✅ DO flag kSecAttrAccessibleAfterFirstUnlock for user passwords or API secrets
- ❌ Do NOT flag .biometryAny if the app intentionally allows re-enrolled biometrics (e.g., convenience feature)
- ✅ DO flag .biometryAny for high-security operations (payment, account deletion)
- ❌ Do NOT flag missing Secure Enclave for symmetric keys — Secure Enclave only supports EC keys
- ✅ DO flag Secure Enclave key generation without kSecAttrTokenIDSecureEnclave

1. **Keychain Access Control**

```swift
// BAD: Default accessibility — accessible when unlocked, persists across device transfer
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrAccount as String: "auth_token",
    kSecValueData as String: tokenData
    // Missing kSecAttrAccessible — defaults to kSecAttrAccessibleWhenUnlocked
    // Token migrates to new device on backup restore
]

// GOOD: Strict accessibility — this device only, unlocked only
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrAccount as String: "auth_token",
    kSecValueData as String: tokenData,
    kSecAttrAccessible as String: kSecAttrAccessibleWhenUnlockedThisDeviceOnly
]
SecItemAdd(query as CFDictionary, nil)
```

2. **Biometric Access Control**

```swift
// BAD: .biometryAny allows access after biometric re-enrollment (potential unauthorized access)
let access = SecAccessControlCreateWithFlags(
    nil,
    kSecAttrAccessibleWhenUnlockedThisDeviceOnly,
    .biometryAny, // attacker re-enrolls their face, accesses existing keychain items
    nil
)

// GOOD: .biometryCurrentSet invalidates on biometric change
var error: Unmanaged<CFError>?
guard let access = SecAccessControlCreateWithFlags(
    nil,
    kSecAttrAccessibleWhenUnlockedThisDeviceOnly,
    .biometryCurrentSet, // item inaccessible if biometrics change
    &error
) else {
    // handle error
    return
}

let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrAccount as String: "payment_credentials",
    kSecValueData as String: credentialData,
    kSecAttrAccessControl as String: access
]
```

3. **LAContext Usage**

```swift
// BAD: No capability check before evaluation
let context = LAContext()
context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, localizedReason: "Unlock") { success, error in
    if success { self.unlockApp() }
    // No fallback if biometrics unavailable — silent failure
}

// GOOD: Check capability, provide fallback, handle errors
let context = LAContext()
context.localizedFallbackTitle = "Use Passcode"

var authError: NSError?
if context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &authError) {
    context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics,
                           localizedReason: "Authenticate to access your account") { success, error in
        DispatchQueue.main.async {
            if success {
                self.unlockApp()
            } else if let laError = error as? LAError {
                switch laError.code {
                case .userFallback: self.showPasscodeEntry()
                case .biometryLockout: self.showBiometryLockedAlert()
                case .userCancel: break // user dismissed
                default: self.showGenericAuthError()
                }
            }
        }
    }
} else {
    showPasscodeEntry() // device doesn't support biometrics or not enrolled
}
```

4. **Secure Enclave Key Management**

```swift
// BAD: Key generated in software — extractable
let attributes: [String: Any] = [
    kSecAttrKeyType as String: kSecAttrKeyTypeECSECPrimeRandom,
    kSecAttrKeySizeInBits as String: 256,
    // No Secure Enclave — key stored in software, extractable
]

// GOOD: Secure Enclave-backed key generation
let access = SecAccessControlCreateWithFlags(
    nil,
    kSecAttrAccessibleWhenUnlockedThisDeviceOnly,
    [.privateKeyUsage, .biometryCurrentSet],
    nil
)!

let attributes: [String: Any] = [
    kSecAttrKeyType as String: kSecAttrKeyTypeECSECPrimeRandom,
    kSecAttrKeySizeInBits as String: 256,
    kSecAttrTokenID as String: kSecAttrTokenIDSecureEnclave,
    kSecPrivateKeyAttrs as String: [
        kSecAttrIsPermanent as String: true,
        kSecAttrApplicationTag as String: "com.app.signing-key",
        kSecAttrAccessControl as String: access
    ]
]

var error: Unmanaged<CFError>?
guard let privateKey = SecKeyCreateRandomKey(attributes as CFDictionary, &error) else {
    // handle error
    return
}
```

## Expected Output

```
## Keychain & Biometric Review Report

### Summary
- **Keychain operations reviewed:** N
- **Access control issues:** N
- **Biometric integration issues:** N
- **LAContext issues:** N
- **Secure Enclave issues:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Security impact:** ...
- **Recommendation:** ...
```

## Example Output

```
## Keychain & Biometric Review Report

### Summary
- **Keychain operations reviewed:** 8
- **Access control issues:** 2
- **Biometric integration issues:** 1
- **LAContext issues:** 1
- **Secure Enclave issues:** 0

### Findings

#### [Critical] Weak Accessibility — AuthManager.swift:L34
- **Issue:** OAuth refresh token stored with default kSecAttrAccessibleWhenUnlocked. Persists across device transfers.
- **Security impact:** Token available on new device after iCloud restore without re-authentication.
- **Recommendation:** Use kSecAttrAccessibleWhenUnlockedThisDeviceOnly.

#### [Warning] biometryAny for Payment — PaymentAuth.swift:L56
- **Issue:** Payment credential protected with `.biometryAny`. Accessible after biometric re-enrollment.
- **Recommendation:** Use `.biometryCurrentSet` to invalidate on biometric change.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates access control, biometrics, LAContext, Secure Enclave
- **RT-02 (Role-Based Task Framing):** Reviewer acts as iOS security specialist
- **RT-04 (Constraint-Based Refinement):** Enforces minimum security levels per credential type
- **AG-02 (Automated Guardrails):** Prevents false flags on valid background-access tokens

## Related Prompts

- `ios_data_protection_review.md` — File-level data protection
- `ios_app_transport_security_review.md` — Network security configuration
- `ios_jailbreak_tamper_detection_review.md` — Runtime integrity checks

## Customization Guide

- **Enterprise apps:** Add Keychain Access Group sharing audit for multi-app suites
- **Financial apps:** Add PCI DSS compliance checks for payment credential storage
- **Healthcare apps:** Add HIPAA considerations for PHI stored in Keychain
