---
title: "Mobile App Security Review"
category: mobile-development
description: "$ apktool d app-release.apk"
tags:
  - mobile-development
  - review
  - security
updated: "2026-03-19"
---

# Mobile App Security Review

**Objective:** Conduct a comprehensive security audit of mobile applications (iOS, Android, React Native, Flutter) to identify vulnerabilities, data exposure risks, insecure authentication patterns, and compliance issues with mobile security best practices.

**When to Use:** Use this prompt before production releases, after security incidents, during compliance audits (PCI-DSS, HIPAA, GDPR), penetration testing preparation, or regular security reviews. Essential for apps handling sensitive user data, financial transactions, or healthcare information.

**Instructions:**

1. **Data Storage Security:**
   * Review how sensitive data is stored locally
   * **iOS:** Check for Keychain usage, NSUserDefaults misuse, file protection attributes
   * **Android:** Verify EncryptedSharedPreferences, KeyStore usage, file permissions
   * **React Native/Flutter:** Assess secure storage libraries (react-native-keychain, flutter_secure_storage)
   * Check for data stored in:
     - Shared Preferences / UserDefaults (should not contain secrets)
     - SQLite databases (must be encrypted for sensitive data)
     - Files (check encryption, file permissions)
     - Cache directories (temporary data exposure)
     - Logs (no sensitive data logging)
   * Verify encryption algorithms used (AES-256 recommended)
   * Check for hardcoded encryption keys (critical vulnerability)

2. **Authentication and Authorization:**
   * Review authentication implementation:
     - OAuth 2.0 / OpenID Connect compliance
     - JWT token storage and handling
     - Biometric authentication (Face ID, Touch ID, fingerprint) implementation
     - Session management and timeout
   * Check for common authentication vulnerabilities:
     - Hardcoded credentials
     - Weak password policies
     - Missing brute force protection
     - Token storage in insecure locations
     - Missing token refresh mechanisms
     - Insecure "remember me" implementations
   * Verify authorization checks:
     - Client-side vs. server-side authorization
     - Role-based access control (RBAC)
     - Proper permission checks before sensitive operations

3. **Network Security:**
   * Review network communication:
     - HTTPS enforcement (no HTTP traffic)
     - Certificate pinning implementation
     - TLS/SSL version and cipher suites
     - Network security configuration (Android)
     - App Transport Security (iOS)
   * Check for API security issues:
     - API key exposure in code or repositories
     - Authentication headers properly implemented
     - Request signing and validation
     - Rate limiting and throttling
   * Evaluate WebView security:
     - JavaScript injection risks
     - File access restrictions
     - Mixed content handling
   * Check for insecure communication channels:
     - Deep links without validation
     - URL scheme vulnerabilities
     - Insecure IPC (Inter-Process Communication)

4. **Code Security:**
   * Review for hardcoded secrets:
     - API keys, tokens, passwords in source code
     - Secrets in resource files, strings.xml, Info.plist
     - Environment variables in committed files
     - Git history scanning for exposed secrets
   * Check for code obfuscation:
     - **iOS:** Strip debug symbols, bitcode
     - **Android:** ProGuard/R8 configuration
     - **React Native:** Hermes bytecode, jscrambler
     - **Flutter:** Obfuscation in release builds
   * Evaluate root/jailbreak detection
   * Check for anti-tampering mechanisms
   * Review reverse engineering protection

5. **Input Validation and Injection:**
   * Check for SQL injection vulnerabilities
   * Review input sanitization for all user inputs
   * Check for XSS vulnerabilities in WebViews
   * Evaluate command injection risks
   * Check path traversal vulnerabilities
   * Review proper use of parameterized queries
   * Assess input length and format validation

6. **Platform-Specific Security:**
   * **iOS:**
     - App Transport Security (ATS) configuration
     - Keychain access control and sharing
     - Face ID / Touch ID implementation security
     - Pasteboard security (sensitive data exposure)
     - Background snapshot security
     - Siri integration data exposure
     - iCloud sync security
   * **Android:**
     - Exported components security (activities, services, receivers)
     - Content provider security
     - Permissions usage and justification
     - SafetyNet / Play Integrity API integration
     - WebView hardening
     - Backup configuration (android:allowBackup)
     - Intent security and validation

7. **Third-Party Dependencies:**
   * Review all third-party libraries and SDKs
   * Check for known vulnerabilities (CVE databases)
   * Verify library versions are up-to-date
   * Assess permissions requested by third-party SDKs
   * Review analytics and crash reporting data collection
   * Check for suspicious or malicious packages
   * Evaluate supply chain security

8. **Privacy and Compliance:**
   * **GDPR Compliance:**
     - Consent management
     - Right to deletion
     - Data portability
     - Privacy policy accessibility
   * **CCPA Compliance:**
     - Do Not Sell disclosure
     - Opt-out mechanisms
   * **COPPA (Children's apps):**
     - Parental consent
     - Age-appropriate content
   * **HIPAA (Healthcare apps):**
     - PHI protection
     - Encryption requirements
     - Audit logging
   * Data collection and usage transparency
   * Location data handling
   * Camera and microphone permissions justification
   * Contacts and photo library access

9. **Cryptography:**
   * Review cryptographic implementations:
     - Strong algorithms (AES-256, RSA 2048+, SHA-256+)
     - No deprecated algorithms (MD5, SHA-1, DES, 3DES)
     - Proper key management
     - Secure random number generation
     - No custom/homegrown cryptography
   * Check for common crypto mistakes:
     - ECB mode usage (insecure)
     - Hardcoded initialization vectors (IV)
     - Static salts for hashing
     - Weak key derivation functions

10. **Session Management:**
    * Review session handling:
      - Secure session token generation
      - Session timeout implementation
      - Logout functionality completeness
      - Token invalidation on logout
      - Concurrent session handling
    * Check for session fixation vulnerabilities
    * Evaluate "remember me" security
    * Review session storage security

11. **Binary Protection:**
    * Check for debug builds in production
    * Verify code signing and provisioning
    * Review entitlements and permissions
    * Check for developer options enabled
    * Verify proper release configuration
    * Assess anti-debugging measures

12. **Secure Communication Patterns:**
    * Review deep linking security:
      - URL scheme validation
      - Universal links / App links implementation
      - Deep link hijacking protection
    * Check push notification security:
      - Sensitive data in notifications
      - Notification payload validation
    * Evaluate clipboard security:
      - Sensitive data exposure via clipboard
      - Clipboard monitoring risks

13. **Logging and Error Handling:**
    * Check for sensitive data in logs:
      - Passwords, tokens, PII in console logs
      - Stack traces with sensitive information
      - Debug logging in production builds
    * Review error message verbosity
    * Check for information disclosure in errors
    * Evaluate crash reporting data exposure

14. **Biometric Authentication:**
    * Review biometric implementation security
    * Check for fallback authentication
    * Verify proper use of platform APIs
    * Assess local vs. server-side biometric validation
    * Review biometric data handling

15. **Payment Security (if applicable):**
    * **PCI-DSS Compliance:**
      - No storage of CVV/CVC
      - Encryption of card data
      - Secure payment gateway integration
    * Review in-app purchase security
    * Check for payment data leakage
    * Evaluate receipt validation (iOS, Android)

**Expected Output:** A comprehensive mobile security audit report including:

1. **Executive Summary:**
   - Overall security posture (Critical/High Risk/Medium Risk/Low Risk)
   - Total vulnerabilities by severity (Critical/High/Medium/Low)
   - Compliance status (GDPR, CCPA, HIPAA, PCI-DSS as applicable)
   - Immediate action items
   - Risk assessment summary

2. **Critical Vulnerabilities:**
   - Detailed description of each critical issue
   - Proof of concept or exploitation scenario
   - Affected code locations
   - Potential impact assessment
   - Immediate remediation steps

3. **Detailed Findings by Category:**
   - For each security area:
     - Security assessment (Secure/Needs Improvement/Vulnerable)
     - Specific vulnerabilities identified
     - Code examples showing issues
     - Severity rating and CVSS score if applicable
     - Remediation recommendations with code examples
     - Best practices to implement

4. **Compliance Assessment:**
   - GDPR compliance checklist
   - CCPA requirements
   - Industry-specific compliance (HIPAA, PCI-DSS, etc.)
   - Gaps and required actions

5. **Remediation Roadmap:**
   - **Phase 1: Critical (Immediate - 1 week):**
     - Security vulnerabilities that could lead to data breaches
     - Hardcoded secrets and credentials
     - Unencrypted sensitive data storage
   - **Phase 2: High Priority (1-2 weeks):**
     - Authentication/authorization issues
     - Network security improvements
     - Input validation gaps
   - **Phase 3: Medium Priority (1 month):**
     - Code obfuscation
     - Third-party dependency updates
     - Enhanced logging and monitoring
   - **Phase 4: Low Priority (Ongoing):**
     - Security enhancements
     - Additional hardening measures

6. **Code Examples:**
   - Vulnerable code snippets
   - Secure implementation alternatives
   - Before/after comparisons
   - Platform-specific security patterns

7. **Testing Recommendations:**
   - Security testing tools to use (MobSF, Frida, Burp Suite)
   - Penetration testing scope
   - Automated security scanning
   - Regular security audit schedule

**Example Output:**

```
# Mobile App Security Review Report

## Executive Summary
- **Overall Security Posture:** HIGH RISK - Critical vulnerabilities identified
- **Critical Issues:** 3
- **High Priority Issues:** 7
- **Medium Priority Issues:** 12
- **Low Priority Issues:** 5
- **Compliance Status:**
  - GDPR: ⚠️ Partially Compliant (gaps identified)
  - PCI-DSS: ❌ Non-Compliant (critical issues)

**Immediate Actions Required:**
1. Remove hardcoded API keys from source code (CRITICAL)
2. Implement encryption for local database (CRITICAL)
3. Fix insecure token storage (CRITICAL)

## Critical Vulnerabilities

### CRITICAL-1: Hardcoded API Keys and Secrets
**Severity:** Critical (CVSS 9.8)
**Risk:** Complete API access compromise, data breach, financial loss

**Location:**
- `src/config/apiConfig.js:12` (React Native)
- `ios/AppName/AppDelegate.swift:45` (iOS)
- `android/app/src/main/java/com/app/MainActivity.kt:78` (Android)

**Vulnerable Code:**
```javascript
// src/config/apiConfig.js
export const API_CONFIG = {
  baseUrl: 'https://api.example.com',
  apiKey: 'sk_live_<REDACTED_EXAMPLE_NOT_A_REAL_KEY>',
  secretKey: 'whsec_<REDACTED_EXAMPLE_NOT_A_REAL_KEY>',
  stripePublicKey: 'pk_live_<REDACTED_EXAMPLE_NOT_A_REAL_KEY>'
};
```

**Impact:**
- Attackers can extract keys via reverse engineering
- Full access to API without authentication
- Potential financial fraud via Stripe keys
- Data exfiltration
- Unauthorized operations

**Evidence:**
```bash
# Keys found in decompiled APK
$ apktool d app-release.apk
$ grep -r "sk_live" app-release/
> res/values/strings.xml:    <string name="api_key">sk_live_&lt;REDACTED_EXAMPLE&gt;</string>
```

**Remediation:**

**Step 1: Immediate - Revoke compromised keys**
```bash
# Revoke all exposed keys immediately
1. Log into Stripe dashboard → API Keys → Revoke
2. Generate new keys
3. Update server-side configuration
```

**Step 2: Implement secure key management**
```javascript
// SECURE APPROACH 1: Backend Proxy (Recommended)
// Never store secret keys in mobile apps
// Use backend to make authenticated API calls

// src/services/apiService.js
export const processPayment = async (paymentDetails) => {
  // Call your backend, which securely stores the API key
  const response = await fetch('https://yourbackend.com/api/payment', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${userAuthToken}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(paymentDetails)
  });
  return response.json();
};

// SECURE APPROACH 2: Environment variables (for less sensitive keys)
// .env (NOT committed to git - add to .gitignore)
API_BASE_URL=https://api.example.com
PUBLIC_API_KEY=pk_xxxxx  // Only public keys, never secret keys

// src/config/apiConfig.js
import Config from 'react-native-config';

export const API_CONFIG = {
  baseUrl: Config.API_BASE_URL,
  publicKey: Config.PUBLIC_API_KEY,
  // Secret keys should NEVER be in mobile app
};

// .gitignore
.env
.env.local
.env.production
```

**Step 3: Add secret scanning to CI/CD**
```yaml
# .github/workflows/security.yml
name: Security Scan
on: [push, pull_request]
jobs:
  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: TruffleHog Secret Scan
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: main
```

**Verification:**
```bash
# Verify no secrets in codebase
$ git secrets --scan
$ trufflehog filesystem . --json
```

### CRITICAL-2: Unencrypted Sensitive Data Storage
**Severity:** Critical (CVSS 8.5)
**Risk:** User PII and authentication tokens exposed in plain text

**Location:**
- `src/utils/storage.js:25` (React Native)
- User credentials stored in AsyncStorage without encryption

**Vulnerable Code:**
```javascript
// src/utils/storage.js
import AsyncStorage from '@react-native-async-storage/async-storage';

export const saveUserCredentials = async (username, password, token) => {
  try {
    // CRITICAL: Plain text storage!
    await AsyncStorage.setItem('username', username);
    await AsyncStorage.setItem('password', password);  // Never store passwords!
    await AsyncStorage.setItem('authToken', token);
    await AsyncStorage.setItem('user_email', email);
    await AsyncStorage.setItem('user_ssn', ssn);  // PII in plain text!
  } catch (error) {
    console.error('Storage error:', error);
  }
};
```

**Impact:**
- Anyone with device access can read data
- Malware can extract tokens and impersonate users
- PII exposure violates GDPR, CCPA
- Backup files contain plain text data
- Potential identity theft

**Attack Scenario:**
```bash
# Android - ADB access to AsyncStorage
$ adb shell
$ run-as com.yourapp
$ cd /data/data/com.yourapp/files/RKStorage
$ cat manifest.json
> {"username":"john.doe","password":"MyPassword123","authToken":"eyJhbG..."}

# iOS - Backup extraction
$ idevicebackup2 backup ./backup
$ sqlite3 backup/manifest.db "SELECT * FROM Files"
> NSUserDefaults.plist contains all plain text data
```

**Remediation:**

```javascript
// SECURE IMPLEMENTATION

// Install secure storage library
// npm install react-native-keychain react-native-encrypted-storage

// src/utils/secureStorage.js
import * as Keychain from 'react-native-keychain';
import EncryptedStorage from 'react-native-encrypted-storage';

/**
 * Use Keychain for authentication tokens (most secure)
 */
export const saveAuthToken = async (token) => {
  try {
    await Keychain.setGenericPassword('authToken', token, {
      service: 'com.yourapp.authtoken',
      accessible: Keychain.ACCESSIBLE.WHEN_UNLOCKED,
      securityLevel: Keychain.SECURITY_LEVEL.SECURE_HARDWARE,
    });
  } catch (error) {
    console.error('Keychain storage error:', error);
    throw error;
  }
};

export const getAuthToken = async () => {
  try {
    const credentials = await Keychain.getGenericPassword({
      service: 'com.yourapp.authtoken',
    });
    if (credentials) {
      return credentials.password;
    }
    return null;
  } catch (error) {
    console.error('Keychain retrieval error:', error);
    return null;
  }
};

/**
 * Use EncryptedStorage for other sensitive data
 */
export const saveUserData = async (userData) => {
  try {
    await EncryptedStorage.setItem(
      'user_data',
      JSON.stringify({
        email: userData.email,
        // NEVER store passwords or SSN on device
        // If absolutely necessary, use backend encryption
      })
    );
  } catch (error) {
    console.error('Encrypted storage error:', error);
    throw error;
  }
};

/**
 * NEVER store passwords on device - use tokens
 * NEVER store SSN or sensitive PII - fetch from backend when needed
 */
```

**iOS Native Implementation:**
```swift
// iOS - Keychain with proper security attributes
import Security

func saveToken(_ token: String) {
    let tokenData = token.data(using: .utf8)!

    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrAccount as String: "authToken",
        kSecValueData as String: tokenData,
        kSecAttrAccessible as String: kSecAttrAccessibleWhenUnlockedThisDeviceOnly
    ]

    SecItemDelete(query as CFDictionary)  // Delete old item
    let status = SecItemAdd(query as CFDictionary, nil)

    if status != errSecSuccess {
        print("Keychain error: \\(status)")
    }
}
```

**Android Native Implementation:**
```kotlin
// Android - EncryptedSharedPreferences
import androidx.security.crypto.EncryptedSharedPreferences
import androidx.security.crypto.MasterKeys

val masterKeyAlias = MasterKeys.getOrCreate(MasterKeys.AES256_GCM_SPEC)

val sharedPreferences = EncryptedSharedPreferences.create(
    "secure_prefs",
    masterKeyAlias,
    context,
    EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
    EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
)

sharedPreferences.edit()
    .putString("auth_token", token)
    .apply()
```

**Verification:**
```javascript
// Add unit tests
import { saveAuthToken, getAuthToken } from './secureStorage';

describe('Secure Storage', () => {
  it('should securely store and retrieve auth token', async () => {
    const testToken = 'test_token_xyz';
    await saveAuthToken(testToken);
    const retrieved = await getAuthToken();
    expect(retrieved).toBe(testToken);
  });

  it('should not expose token in AsyncStorage', async () => {
    // Verify token not in AsyncStorage
    const allKeys = await AsyncStorage.getAllKeys();
    expect(allKeys).not.toContain('authToken');
    expect(allKeys).not.toContain('password');
  });
});
```

### CRITICAL-3: Insecure HTTP Communication
**Severity:** Critical (CVSS 8.1)
**Risk:** Man-in-the-middle attacks, credential theft, data interception

**Location:**
- Multiple API calls using HTTP instead of HTTPS
- Missing certificate pinning
- Weak TLS configuration

[... detailed remediation for network security ...]

## High Priority Vulnerabilities

### HIGH-1: Insufficient Input Validation
[... details ...]

### HIGH-2: Missing Root/Jailbreak Detection
[... details ...]

[... more vulnerabilities ...]

## Compliance Assessment

### GDPR Compliance
**Status:** ⚠️ Partially Compliant

**Gaps Identified:**
1. ❌ No consent management for analytics
2. ❌ Missing data deletion functionality
3. ✅ Privacy policy accessible
4. ⚠️ Data minimization needs review
5. ❌ No data portability feature

**Required Actions:**
[... specific compliance steps ...]

## Remediation Roadmap

### Phase 1: Critical Fixes (This Week)
- [ ] Revoke and remove all hardcoded API keys
- [ ] Implement encrypted storage for sensitive data
- [ ] Enforce HTTPS for all network communication
- [ ] Add certificate pinning

### Phase 2: High Priority (Weeks 2-3)
- [ ] Implement comprehensive input validation
- [ ] Add root/jailbreak detection
- [ ] Fix authentication vulnerabilities
- [ ] Update vulnerable dependencies

[... more phases ...]

## Security Testing Tools Recommended

1. **Static Analysis:**
   - MobSF (Mobile Security Framework)
   - Semgrep with mobile security rules
   - Checkmarx / Veracode

2. **Dynamic Analysis:**
   - Burp Suite Mobile Assistant
   - Frida for runtime analysis
   - Objection for dynamic instrumentation

3. **Dependency Scanning:**
   - npm audit / yarn audit
   - Snyk
   - OWASP Dependency-Check

4. **Secret Scanning:**
   - TruffleHog
   - git-secrets
   - GitGuardian
```

**Techniques Used:**
- ST-01 (Clear Objective)
- ST-02 (Sequential Instructions)
- RT-02 (Multi-Dimensional Analysis)
- RT-04 (Best Practice Review)
- ST-03 (Structured Output Templates)
- OC-05 (Severity Classification)
- OC-07 (Risk Assessment)

**Related Prompts:**
- `ios_swift_architecture_review.md` - For iOS-specific security in architecture
- `android_kotlin_best_practices.md` - For Android-specific security patterns
- `react_native_performance_optimization.md` - For React Native specifics
- `flutter_widget_analysis.md` - For Flutter security considerations
- `security_vulnerability_analysis.md` - For general security analysis
- `code_quality_code_style_consistency.md` - For security linting rules

**Customization Guide:**
- For financial apps: Emphasize PCI-DSS compliance, payment security, fraud detection
- For healthcare apps: Focus on HIPAA compliance, PHI protection, audit logging
- For social apps: Emphasize privacy, data sharing controls, user consent
- For enterprise apps: Add MDM/MAM considerations, enterprise authentication (SAML, AD)
- For IoT-connected apps: Add device pairing security, BLE security, local network security
- For specific industries: Customize compliance requirements (FERPA for education, etc.)
