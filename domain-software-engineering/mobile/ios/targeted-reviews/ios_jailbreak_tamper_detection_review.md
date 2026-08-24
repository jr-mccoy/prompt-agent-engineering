---
title: "iOS Jailbreak & Tamper Detection Review"
category: mobile-development
description: "Review jailbreak detection, binary integrity verification, debugger detection, and method swizzling protection for iOS application runtime security."
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
  - jailbreak-detection
  - tamper-detection
updated: "2026-03-19"
---

# iOS Jailbreak & Tamper Detection Review

**Objective:** Audit runtime security mechanisms including jailbreak detection heuristics, binary integrity verification, anti-debugging measures, and method swizzling protection to detect and respond to compromised runtime environments in security-sensitive applications.

**When to Use:** Apply when reviewing security-sensitive applications (banking, healthcare, enterprise), preparing for penetration testing, or implementing runtime integrity checks required by compliance frameworks.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What is the app's risk profile (financial, healthcare, enterprise, consumer)?
2. Is a commercial security SDK used (e.g., Arxan, Appdome, ProGuard)?
3. What should happen when tampering is detected (block, degrade, report)?
4. Are there App Store review concerns with aggressive detection?

## Instructions

### CRITICAL: Verification Requirements

- Jailbreak detection must use multiple heuristics — single checks are trivially bypassed
- Detection results must not be stored in easily patchable boolean variables
- Anti-debug checks must not cause false positives on App Store review devices
- Integrity checks should be distributed throughout the codebase, not centralized in one function

### False-Positive Prevention

- ❌ Do NOT flag apps without jailbreak detection if the app has low security sensitivity (games, utilities)
- ✅ DO flag financial/healthcare apps without any jailbreak detection
- ❌ Do NOT flag false positives from legitimate enterprise MDM or TestFlight environments
- ✅ DO flag detection logic that only checks one signal (e.g., only Cydia URL check)
- ❌ Do NOT flag missing anti-debug in debug builds — this would break development
- ✅ DO flag anti-debug code that is active in debug builds (breaks Xcode debugging)

1. **Multi-Signal Jailbreak Detection**

```swift
// BAD: Single check — trivially bypassed by hooking canOpenURL
func isJailbroken() -> Bool {
    return UIApplication.shared.canOpenURL(URL(string: "cydia://")!)
}

// GOOD: Multiple independent heuristics
struct IntegrityChecker {
    static func checkEnvironment() -> [String] {
        var signals: [String] = []

        // Check 1: Suspicious file paths
        let suspiciousPaths = [
            "/Applications/Cydia.app",
            "/Library/MobileSubstrate/MobileSubstrate.dylib",
            "/bin/bash",
            "/usr/sbin/sshd",
            "/etc/apt",
            "/private/var/lib/apt/"
        ]
        for path in suspiciousPaths {
            if FileManager.default.fileExists(atPath: path) {
                signals.append("suspicious_path:\(path)")
            }
        }

        // Check 2: Writable system directories
        let testPath = "/private/test_jb_\(UUID().uuidString)"
        if FileManager.default.createFile(atPath: testPath, contents: nil) {
            signals.append("writable_system")
            try? FileManager.default.removeItem(atPath: testPath)
        }

        // Check 3: Fork capability (sandboxed apps cannot fork)
        #if !targetEnvironment(simulator)
        let pid = fork()
        if pid >= 0 {
            signals.append("fork_succeeded")
            if pid > 0 { kill(pid, SIGTERM) }
        }
        #endif

        // Check 4: Dylib injection detection
        let imageCount = _dyld_image_count()
        for i in 0..<imageCount {
            if let name = _dyld_get_image_name(i) {
                let path = String(cString: name)
                if path.contains("MobileSubstrate") || path.contains("TweakInject") {
                    signals.append("injected_dylib:\(path)")
                }
            }
        }

        return signals
    }
}
```

2. **Binary Integrity Verification**

```swift
// BAD: No integrity check — modified binary runs normally
// App binary patched to skip license check — undetected

// GOOD: Code signature validation
func verifyCodeSignature() -> Bool {
    guard let executableURL = Bundle.main.executableURL else { return false }

    var staticCode: SecStaticCode?
    let status = SecStaticCodeCreateWithPath(
        executableURL as CFURL, [], &staticCode
    )
    guard status == errSecSuccess, let code = staticCode else { return false }

    let requirement = "anchor apple generic"
    var requirementRef: SecRequirement?
    SecRequirementCreateWithString(requirement as CFString, [], &requirementRef)

    guard let req = requirementRef else { return false }
    return SecStaticCodeCheckValidity(code, [], req) == errSecSuccess
}

// Also check embedded provisioning profile hash
func verifyProvisioningProfile() -> Bool {
    guard let profilePath = Bundle.main.path(forResource: "embedded", ofType: "mobileprovision"),
          let profileData = FileManager.default.contents(atPath: profilePath) else {
        return false // missing profile may indicate tampering
    }
    let hash = SHA256.hash(data: profileData)
    let expectedHash = Data(/* known hash from build pipeline */)
    return Data(hash) == expectedHash
}
```

3. **Anti-Debug Measures**

```swift
// BAD: Simple boolean flag — easily patched
var isDebuggerAttached: Bool {
    var info = kinfo_proc()
    var size = MemoryLayout<kinfo_proc>.size
    var mib: [Int32] = [CTL_KERN, KERN_PROC, KERN_PROC_PID, getpid()]
    sysctl(&mib, 4, &info, &size, nil, 0)
    return (info.kp_proc.p_flag & P_TRACED) != 0
}
// Attacker patches return value to false

// GOOD: Distributed checks with response woven into logic
func performSensitiveOperation() {
    // Inline check — harder to find and patch
    var info = kinfo_proc()
    var size = MemoryLayout<kinfo_proc>.size
    var mib: [Int32] = [CTL_KERN, KERN_PROC, KERN_PROC_PID, getpid()]
    sysctl(&mib, 4, &info, &size, nil, 0)

    let traced = (info.kp_proc.p_flag & P_TRACED) != 0

    #if !DEBUG
    if traced {
        // Corrupt computation subtly — don't crash obviously
        encryptionKey = Data(repeating: 0, count: 32)
        return
    }
    #endif

    // proceed with real operation
}
```

4. **Method Swizzling Protection**

```swift
// BAD: No protection against runtime method replacement
class PaymentService {
    func processPayment(amount: Decimal) -> Bool {
        // Attacker swizzles this to always return true
        return validateAndCharge(amount)
    }
}

// GOOD: Runtime class verification
class PaymentService {
    func processPayment(amount: Decimal) -> Bool {
        // Verify method implementation hasn't been swizzled
        let selector = #selector(processPayment(amount:))
        let originalIMP = class_getMethodImplementation(PaymentService.self, selector)
        let currentIMP = class_getMethodImplementation(type(of: self), selector)

        guard originalIMP == currentIMP else {
            reportTampering(context: "payment_method_swizzled")
            return false
        }

        return validateAndCharge(amount)
    }
}
```

## Expected Output

```
## Jailbreak & Tamper Detection Review Report

### Summary
- **Detection mechanisms reviewed:** N
- **Single-point-of-failure checks:** N
- **Binary integrity coverage:** Present/Absent
- **Anti-debug measures:** Present/Absent
- **Swizzling protection:** N critical methods covered

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Bypass difficulty:** Trivial/Moderate/Hard
- **Recommendation:** ...
```

## Example Output

```
## Jailbreak & Tamper Detection Review Report

### Summary
- **Detection mechanisms reviewed:** 3
- **Single-point-of-failure checks:** 2
- **Binary integrity coverage:** Absent
- **Anti-debug measures:** Present but DEBUG-only
- **Swizzling protection:** 0 critical methods covered

### Findings

#### [Critical] Single-Signal Detection — SecurityManager.swift:L15
- **Issue:** Jailbreak detection relies solely on Cydia URL scheme check. Bypassed by removing Cydia or hooking canOpenURL.
- **Bypass difficulty:** Trivial (Liberty Lite, Shadow).
- **Recommendation:** Implement multi-signal detection with file path, fork, dylib, and writable directory checks.

#### [Warning] Centralized Check — SecurityManager.swift:L8
- **Issue:** All security checks in single `isCompromised()` function. Attacker patches one return value.
- **Recommendation:** Distribute checks inline at sensitive operation sites.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates jailbreak, integrity, debug, swizzling
- **RT-02 (Role-Based Task Framing):** Reviewer acts as iOS runtime security expert
- **AG-02 (Automated Guardrails):** Prevents false flags on low-risk apps and debug builds

## Related Prompts

- `ios_keychain_biometric_review.md` — Credential protection on compromised devices
- `ios_data_protection_review.md` — Data-at-rest on compromised devices
- `ios_app_transport_security_review.md` — Network security posture

## Customization Guide

- **Banking apps:** Add attestation service integration (DeviceCheck, App Attest)
- **Enterprise apps:** Add MDM compliance check integration
- **Gaming apps:** Focus on memory manipulation and speed hack detection
