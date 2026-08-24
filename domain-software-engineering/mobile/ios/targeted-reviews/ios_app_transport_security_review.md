---
title: "iOS App Transport Security Review"
category: mobile-development
description: "Review ATS configuration for exception justifications, certificate pinning implementation, TLS version requirements, and network security posture."
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
  - networking
  - ats
updated: "2026-03-19"
---

# iOS App Transport Security Review

**Objective:** Audit App Transport Security configuration for justified exceptions, correct certificate pinning implementation, minimum TLS version enforcement, and overall network security posture to prevent man-in-the-middle attacks and ensure App Store compliance.

**When to Use:** Apply when reviewing Info.plist network configuration, adding new API endpoints, preparing for App Store submission, or auditing network security after a penetration test finding.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. Does the Info.plist contain any ATS exceptions?
2. Is certificate pinning implemented (URLSession delegate, TrustKit, Alamofire)?
3. Does the app communicate with third-party APIs or CDNs that may require exceptions?
4. Is the app subject to compliance requirements (HIPAA, PCI DSS, SOC 2)?

## Instructions

### CRITICAL: Verification Requirements

- NSAllowsArbitraryLoads must be false (or absent) in production builds
- Every ATS exception domain must have a documented justification
- Certificate pinning must pin to intermediate or leaf certificates, not root CAs alone
- TLS 1.2 must be the minimum version; TLS 1.0/1.1 exceptions must be flagged

### False-Positive Prevention

- ❌ Do NOT flag NSAllowsArbitraryLoadsInWebContent for apps that display user-provided URLs in WKWebView
- ✅ DO flag NSAllowsArbitraryLoadsInWebContent if the app only loads its own content
- ❌ Do NOT flag ATS exceptions for local development domains (localhost, 192.168.*)
- ✅ DO flag ATS exceptions for local domains that ship in release builds
- ❌ Do NOT flag missing cert pinning for non-sensitive endpoints (public content, images)
- ✅ DO flag missing cert pinning for authentication and payment endpoints

1. **ATS Exception Audit**

```xml
<!-- BAD: Blanket ATS disable — all connections insecure -->
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>

<!-- GOOD: Targeted exception with minimum security -->
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSExceptionDomains</key>
    <dict>
        <key>legacy-api.partner.com</key>
        <dict>
            <key>NSExceptionMinimumTLSVersion</key>
            <string>TLSv1.2</string>
            <key>NSExceptionRequiresForwardSecrecy</key>
            <false/>
            <!-- Justification: Partner API does not support PFS. Migration planned Q3 2026. -->
        </dict>
    </dict>
</dict>
```

2. **Certificate Pinning**

```swift
// BAD: No certificate validation — trusts any valid cert
func urlSession(_ session: URLSession, didReceive challenge: URLAuthenticationChallenge,
                completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
    completionHandler(.performDefaultHandling, nil) // system default — no pinning
}

// GOOD: Pin to leaf certificate public key
func urlSession(_ session: URLSession, didReceive challenge: URLAuthenticationChallenge,
                completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
    guard let serverTrust = challenge.protectionSpace.serverTrust,
          let serverCert = SecTrustCopyCertificateChain(serverTrust)?.first else {
        completionHandler(.cancelAuthenticationChallenge, nil)
        return
    }

    let serverPublicKey = SecCertificateCopyKey(serverCert)
    let serverKeyData = SecKeyCopyExternalRepresentation(serverPublicKey!, nil)! as Data
    let serverKeyHash = SHA256.hash(data: serverKeyData)

    let pinnedHashes: [Data] = [
        Data(base64Encoded: "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=")! // current cert
        // Include backup pin for rotation
    ]

    if pinnedHashes.contains(where: { Data(serverKeyHash) == $0 }) {
        completionHandler(.useCredential, URLCredential(trust: serverTrust))
    } else {
        completionHandler(.cancelAuthenticationChallenge, nil)
    }
}
```

3. **TLS Version Enforcement**

```swift
// BAD: Allowing TLS 1.0 connections
let config = URLSessionConfiguration.default
config.tlsMinimumSupportedProtocolVersion = .TLSv10 // vulnerable to BEAST, POODLE

// GOOD: Enforce minimum TLS 1.2
let config = URLSessionConfiguration.default
config.tlsMinimumSupportedProtocolVersion = .TLSv12
// TLS 1.3 preferred when server supports it (automatic with default config)
```

4. **Debug vs Release Configuration**

```swift
// BAD: ATS disabled for debugging, shipped in release
// Info.plist has NSAllowsArbitraryLoads = YES in all configurations

// GOOD: Conditional configuration
#if DEBUG
// Development: use Charles proxy — ATS exception in Debug.xcconfig only
// INFOPLIST_KEY_NSAppTransportSecurity_NSAllowsArbitraryLoads = YES
#endif

// Or: Separate Info.plist for Debug and Release
// Debug-Info.plist: NSAllowsArbitraryLoads = YES
// Release-Info.plist: no exceptions
```

## Expected Output

```
## App Transport Security Review Report

### Summary
- **ATS exceptions found:** N
- **Unjustified exceptions:** N
- **Certificate pinning coverage:** N of N sensitive endpoints
- **TLS version issues:** N
- **Debug-only leak risks:** N

### Findings
#### [Severity] Issue — File:Line or Info.plist
- **Issue:** ...
- **Security impact:** ...
- **Recommendation:** ...
```

## Example Output

```
## App Transport Security Review Report

### Summary
- **ATS exceptions found:** 3
- **Unjustified exceptions:** 1
- **Certificate pinning coverage:** 1 of 3 sensitive endpoints
- **TLS version issues:** 0
- **Debug-only leak risks:** 1

### Findings

#### [Critical] Blanket ATS Disable — Info.plist
- **Issue:** `NSAllowsArbitraryLoads = true` in production Info.plist.
- **Security impact:** All network connections allowed over HTTP. MitM attack surface for all API calls.
- **Recommendation:** Remove blanket disable. Add targeted exceptions only for required domains.

#### [Warning] Missing Cert Pinning — PaymentService.swift
- **Issue:** Payment API endpoint `api.payments.com` uses default certificate validation without pinning.
- **Security impact:** Compromised CA could issue fraudulent certificate for payment domain.
- **Recommendation:** Implement public key pinning with backup pin for certificate rotation.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates ATS config, pinning, TLS, debug leaks
- **RT-02 (Role-Based Task Framing):** Reviewer acts as iOS network security specialist
- **AG-02 (Automated Guardrails):** Prevents false flags on valid web content exceptions

## Related Prompts

- `ios_keychain_biometric_review.md` — Credential storage security
- `ios_data_protection_review.md` — Data-at-rest protection
- `ios_jailbreak_tamper_detection_review.md` — Runtime security checks

## Customization Guide

- **Enterprise proxy environments:** Add managed certificate trust store checks
- **SDK integrations:** Audit third-party SDK ATS requirements and exception domains
- **Certificate rotation:** Add pinning rotation plan and backup pin verification
