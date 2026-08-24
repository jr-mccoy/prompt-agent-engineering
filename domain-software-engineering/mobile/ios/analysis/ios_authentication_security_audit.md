---
title: "iOS Authentication Security Audit"
category: mobile-development
description: "Audit authentication security covering Sign in with Apple, biometric authentication (Face ID/Touch ID), session management, token storage, and OAuth flows for iOS apps"
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
  - authentication
  - biometric
updated: "2026-03-20"
---

# iOS Authentication Security Audit

**Objective:** Audit the authentication and session security of an iOS app covering Sign in with Apple implementation, biometric authentication (Face ID / Touch ID), session lifecycle management, token storage and refresh, and OAuth/OIDC flows to identify vulnerabilities, compliance gaps, and hardening opportunities.

**When to Use:** Use this prompt during security reviews of apps handling user authentication, before launching a new auth flow, when adding biometric authentication, when integrating Sign in with Apple, or when investigating unauthorized access incidents.

**Prompt Type:** Comprehensive (350-500 lines)

---

## Context Gathering

Before beginning the audit, gather context:

1. **Authentication Methods:**
   - "What authentication methods does the app support (email/password, social login, Sign in with Apple, biometric, SSO)?"
   - "Is there a backend authentication service (custom, Firebase Auth, Auth0, AWS Cognito)?"

2. **Session Management:**
   - "How are sessions managed (JWT, opaque tokens, server sessions)?"
   - "What are the token lifetimes (access token, refresh token)?"

3. **Security Requirements:**
   - "Are there specific security requirements (MFA, biometric enforcement, session timeout)?"
   - "Is the app subject to regulatory requirements (SOC 2, HIPAA, PSD2)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the full auth flow** - Don't flag individual components without understanding how they connect end-to-end.
2. **Verify actual token handling** - Check what's stored, where, and how it's transmitted — not just what the API documentation says.
3. **Test error paths** - Authentication security is often weakest in error handling, token expiration, and edge cases.
4. **Check server-side validation** - Client-side auth checks alone are insufficient. Verify the server validates tokens.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**A well-implemented authentication system with standard patterns is secure.** Don't flag OAuth libraries or Apple's auth frameworks for theoretical attacks that require unrealistic threat models.

### False-Positive Prevention

- ❌ Do NOT flag standard OAuth/OIDC flows as insecure without identifying specific deviations
- ❌ Do NOT flag biometric auth as weak just because it falls back to passcode (that's by design)
- ❌ Do NOT flag Apple's authentication frameworks for vulnerabilities in Apple's implementation
- ❌ Do NOT require MFA for apps where single-factor authentication meets the risk profile
- ✅ DO check that tokens are stored in Keychain, not UserDefaults or files
- ✅ DO verify that biometric auth protects real credentials, not just a UI gate
- ✅ DO check error handling paths for auth bypass opportunities
- ✅ DO assess the complete session lifecycle (creation, validation, refresh, revocation)

---

### Phase 1: Sign in with Apple Audit

#### 1.1 Implementation Assessment

**Verify Sign in with Apple integration:**

```swift
// Check ASAuthorizationController configuration
let provider = ASAuthorizationAppleIDProvider()
let request = provider.createRequest()
request.requestedScopes = [.fullName, .email]

// CRITICAL CHECKS:

// 1. Identity token validation
// The identityToken MUST be validated server-side
func authorizationController(controller: ASAuthorizationController,
                             didCompleteWithAuthorization authorization: ASAuthorization) {
    guard let credential = authorization.credential as? ASAuthorizationAppleIDCredential else { return }

    // ✅ GOOD: Send token to server for validation
    let identityToken = credential.identityToken  // JWT — validate server-side
    let authorizationCode = credential.authorizationCode  // Exchange server-side

    // ❌ BAD: Trust client-side without server validation
    let userId = credential.user  // Don't trust this alone
}

// 2. Credential state monitoring
// App MUST check credential state on launch
func checkAppleIDCredentialState() {
    let provider = ASAuthorizationAppleIDProvider()
    provider.getCredentialState(forUserID: savedUserID) { state, error in
        switch state {
        case .authorized: break     // Still valid
        case .revoked:              // User revoked — MUST log out
            self.forceLogout()
        case .notFound:             // No credential — re-authenticate
            self.promptLogin()
        case .transferred:          // Account transferred
            self.handleTransfer()
        }
    }
}

// 3. Real user indicator
// Check for fraud prevention
credential.realUserStatus  // .likelyReal, .unknown, .unsupported
```

**Sign in with Apple Audit Table:**

| Check | Status | Finding |
|-------|--------|---------|
| Server-side token validation | [Yes/No] | [Details] |
| Credential state checked on launch | [Yes/No] | [Details] |
| Revocation handled (force logout) | [Yes/No] | [Details] |
| Authorization code exchanged server-side | [Yes/No] | [Details] |
| Real user status utilized | [Yes/No] | [Details] |
| Private relay email handled | [Yes/No] | [Details] |
| Nonce used for replay prevention | [Yes/No] | [Details] |

#### 1.2 Account Linking

**Check for account linking vulnerabilities:**

```swift
// RISK: Trusting email from Apple ID without verification
// Apple may provide a private relay email (xyz@privaterelay.appleid.com)
// Or user's real email — both must be handled

// RISK: Account takeover via email reuse
// If another user signs up with same email via different method,
// ensure accounts aren't automatically merged without verification

// CHECK: Is the Apple user identifier (credential.user) stored
// as the primary identifier, not the email?
```

---

### Phase 2: Biometric Authentication Audit

#### 2.1 LAContext Configuration

**Audit biometric authentication setup:**

```swift
// Check LAContext usage
let context = LAContext()

// CRITICAL: What does biometric auth actually protect?

// ❌ BAD: Biometric as UI gate only
func authenticateWithBiometric() {
    context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, ...) { success, _ in
        if success {
            self.showMainScreen()  // Just hides the login screen
            // Token is already accessible without biometric!
        }
    }
}

// ✅ GOOD: Biometric protects Keychain access
func authenticateWithBiometric() {
    // Token stored with biometric access control
    let query: [String: Any] = [
        kSecClass: kSecClassGenericPassword,
        kSecAttrAccount: "authToken",
        kSecUseAuthenticationContext: context,
        // Keychain item REQUIRES biometric to read
    ]
    // SecItemCopyMatching will trigger biometric prompt
}

// Check: Biometric policy selection
.deviceOwnerAuthenticationWithBiometrics  // Biometric only
.deviceOwnerAuthentication                // Biometric OR passcode fallback

// Check: Biometric invalidation
context.evaluatedPolicyDomainState  // Detect biometric enrollment changes
// If biometrics change, should tokens be invalidated?
```

#### 2.2 Keychain Access Control with Biometrics

**Verify Keychain biometric integration:**

```swift
// Check SecAccessControl flags
let accessControl = SecAccessControlCreateWithFlags(
    nil,
    kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly,
    [.biometryCurrentSet],  // Invalidates if biometrics change
    nil
)

// Flag options to audit:
.biometryCurrentSet     // Re-auth required if biometrics change (MORE SECURE)
.biometryAny            // Any enrolled biometric works, even new ones (LESS SECURE)
.userPresence           // Biometric or passcode
.devicePasscode         // Passcode only

// CRITICAL: Check if .biometryCurrentSet is used for high-value items
// Using .biometryAny means an attacker who adds their fingerprint gets access
```

| Protected Item | Access Control | Invalidation Policy | Fallback | Finding |
|---------------|---------------|-------------------|----------|---------|
| Auth token | [Flags] | [CurrentSet/Any] | [Passcode/None] | [OK/Issue] |
| Encryption key | [Flags] | [CurrentSet/Any] | [Passcode/None] | [OK/Issue] |

#### 2.3 Biometric Error Handling

**Audit error handling for biometric failures:**

```swift
// Check all LAError cases are handled
switch error.code {
case .authenticationFailed:  // Biometric didn't match
    // Should: increment failure counter, consider lockout
case .userCancel:            // User tapped Cancel
    // Should: offer alternative auth
case .userFallback:          // User tapped "Enter Password"
    // Should: present password entry
case .biometryNotAvailable:  // Hardware not available
    // Should: fall back to password
case .biometryNotEnrolled:   // No biometrics enrolled
    // Should: prompt enrollment or fall back
case .biometryLockout:       // Too many failures
    // Should: require passcode, then re-enable biometric
case .passcodeNotSet:        // No device passcode
    // Should: require passcode setup for security
}

// RED FLAG: Ignoring errors or defaulting to "allow access"
case .authenticationFailed:
    break  // Silently fails — user might still access app
```

---

### Phase 3: Session Management Audit

#### 3.1 Token Storage

**Verify token storage security:**

```swift
// WHERE are tokens stored?
// ✅ Keychain with appropriate protection class
// ❌ UserDefaults (plaintext in plist backup)
// ❌ File system without encryption
// ❌ In-memory only (lost on app restart — poor UX but secure)
// ❌ Hardcoded or embedded in app bundle

// Check: Token types and their storage
// Access token (short-lived) → Keychain or secure memory
// Refresh token (long-lived) → Keychain with biometric protection
// ID token (identity claims) → Keychain
// API keys → Keychain or secure config (NOT source code)
```

| Token Type | Storage Location | Protection | Lifetime | Finding |
|-----------|-----------------|-----------|----------|---------|
| Access token | [Location] | [Level] | [Duration] | [OK/Issue] |
| Refresh token | [Location] | [Level] | [Duration] | [OK/Issue] |
| ID token | [Location] | [Level] | [Duration] | [OK/Issue] |

#### 3.2 Token Lifecycle

**Audit token refresh and expiration handling:**

```swift
// CHECK: Token refresh flow
// 1. Access token expires
// 2. App detects 401 or token expiration
// 3. Refresh token used to obtain new access token
// 4. If refresh fails → force re-authentication

// RED FLAGS:
// - No token expiration checking
// - Infinite refresh token lifetime
// - Refresh token stored less securely than auth token
// - No retry limit on refresh attempts
// - Race condition: multiple concurrent refreshes

// GOOD PATTERN: Token refresh with queue
class TokenManager {
    private var isRefreshing = false
    private var pendingRequests: [(Result<Token, Error>) -> Void] = []

    func validToken() async throws -> Token {
        if let token = currentToken, !token.isExpired {
            return token
        }
        return try await refreshToken()
    }
}
```

#### 3.3 Session Termination

**Verify proper session cleanup:**

```swift
// CHECK: What happens on logout?
func logout() {
    // ✅ Must clear:
    // - Access token from Keychain
    // - Refresh token from Keychain
    // - Session cookies
    // - Cached user data
    // - In-memory user state
    // - Push notification token (server-side deregistration)

    // ✅ Must notify server:
    // - Revoke refresh token server-side
    // - Invalidate server session

    // ✅ Must handle:
    // - Background tasks using old credentials
    // - Pending network requests with old tokens
    // - Shared keychain items (if app group)

    // ❌ RED FLAGS:
    // - Only clearing UI state without clearing tokens
    // - Not revoking server-side session
    // - Tokens remaining accessible after "logout"
}
```

| Cleanup Action | Implemented | Location | Finding |
|---------------|------------|----------|---------|
| Clear access token | [Yes/No] | [File:Line] | [OK/Issue] |
| Clear refresh token | [Yes/No] | [File:Line] | [OK/Issue] |
| Revoke server session | [Yes/No] | [File:Line] | [OK/Issue] |
| Clear cached user data | [Yes/No] | [File:Line] | [OK/Issue] |
| Clear cookies | [Yes/No] | [File:Line] | [OK/Issue] |

---

### Phase 4: OAuth / OIDC Flow Audit

#### 4.1 OAuth Implementation

**Audit OAuth flow security:**

```swift
// Check: Which OAuth flow is used?
// ✅ Authorization Code + PKCE (recommended for mobile)
// ❌ Implicit flow (tokens in URL — deprecated for mobile)
// ❌ Resource Owner Password Credentials (sends password to client)

// PKCE Implementation Check:
// 1. Code verifier generated (43-128 chars, cryptographically random)
let codeVerifier = generateCryptographicRandom(length: 64)

// 2. Code challenge derived
let codeChallenge = sha256(codeVerifier).base64URLEncoded
// Method MUST be S256, not plain

// 3. Auth request includes challenge
var components = URLComponents(string: "https://auth.example.com/authorize")!
components.queryItems = [
    URLQueryItem(name: "response_type", value: "code"),
    URLQueryItem(name: "client_id", value: clientID),
    URLQueryItem(name: "redirect_uri", value: redirectURI),
    URLQueryItem(name: "code_challenge", value: codeChallenge),
    URLQueryItem(name: "code_challenge_method", value: "S256"),
    URLQueryItem(name: "state", value: generateState()),  // CSRF protection
]

// 4. Token exchange includes verifier
// POST to token endpoint with code + code_verifier

// CHECK: Is ASWebAuthenticationSession used? (recommended)
let session = ASWebAuthenticationSession(
    url: authURL,
    callbackURLScheme: "myapp",  // Must use custom scheme or universal link
    completionHandler: { callbackURL, error in
        // Extract authorization code from callback
    }
)
session.prefersEphemeralWebBrowserSession = true  // Don't share cookies
```

#### 4.2 Redirect URI Security

**Verify redirect URI handling:**

```swift
// CHECK: Redirect URI scheme
// ✅ Universal Links (https://app.example.com/callback) — most secure
// ⚠️ Custom URL scheme (myapp://callback) — can be hijacked by another app
// ❌ HTTP scheme — insecure

// If using custom scheme:
// - Is the scheme unique enough to prevent hijacking?
// - Is the state parameter validated to prevent CSRF?
// - Is the authorization code used only once?

// CHECK: URL scheme declaration in Info.plist
// Another app could register the same scheme and intercept the callback
```

#### 4.3 Token Validation

**Verify token validation practices:**

```swift
// JWT validation checks (if using JWTs):
// ✅ Signature verification (server-side preferred)
// ✅ Issuer (iss) validation
// ✅ Audience (aud) validation
// ✅ Expiration (exp) check
// ✅ Not-before (nbf) check
// ✅ Token type validation

// ❌ RED FLAGS:
// - Parsing JWT without signature verification
// - Trusting JWT claims client-side for authorization decisions
// - Not checking token expiration before use
// - Using symmetric signing for client-issued tokens
```

---

### Phase 5: Findings and Remediation

**CHECKPOINT:** Present authentication security findings.

```markdown
## Authentication Security Audit Results

### Risk Summary

| Severity | Count | Category |
|----------|-------|----------|
| Critical | [N] | [Categories] |
| High | [N] | [Categories] |
| Medium | [N] | [Categories] |
| Low | [N] | [Categories] |

### Auth Flow Security Score

| Component | Score (1-10) | Key Issues |
|-----------|-------------|------------|
| Sign in with Apple | [Score] | [Summary] |
| Biometric Auth | [Score] | [Summary] |
| Session Management | [Score] | [Summary] |
| OAuth/OIDC | [Score] | [Summary] |
| Token Storage | [Score] | [Summary] |

### Critical Findings

1. **[Finding]** - [Location] - [Impact] - [Fix]

**Shall I provide detailed remediation guidance?**
```

---

## Expected Output

1. **Sign in with Apple Assessment** - Token validation, credential state, account linking review
2. **Biometric Security Report** - LAContext config, Keychain integration, error handling audit
3. **Session Management Review** - Token storage, lifecycle, refresh, and termination analysis
4. **OAuth/OIDC Compliance** - Flow type, PKCE, redirect URI, and token validation assessment
5. **Prioritized Findings** - All vulnerabilities ranked with remediation steps

---

## Example Interaction

**User:** Audit the authentication security of our iOS banking app. We support Sign in with Apple, Face ID, and username/password with our OAuth backend.

**Agent:** I'll audit all authentication flows end-to-end. Let me trace each auth path.

*[Agent traces Sign in with Apple, biometric, and OAuth flows]*

**Agent:**

## Authentication Security Audit — Banking App

### Critical Findings

1. **Biometric auth is UI-only gate** — `BiometricManager.swift:34`
   - Face ID success just sets `isAuthenticated = true` and shows the main tab
   - Auth token is stored in Keychain **without** biometric access control
   - **Impact:** Token accessible without biometric on jailbroken device
   - **Fix:** Store token with `SecAccessControlCreateWithFlags` using `.biometryCurrentSet`

2. **Sign in with Apple token not validated server-side** — `AppleAuthHandler.swift:67`
   - `credential.user` is sent to backend as the user identifier
   - Identity token JWT is never forwarded for server-side signature verification
   - **Impact:** Client could send fabricated user ID to backend
   - **Fix:** Send `identityToken` to server, validate JWT signature against Apple's public keys

3. **OAuth using implicit flow** — `OAuthManager.swift:12`
   - Access token returned in URL fragment, no PKCE
   - **Impact:** Token interception via URL scheme hijack
   - **Fix:** Migrate to Authorization Code + PKCE flow

### Medium Findings

4. **No credential state check on app launch** — Apple ID revocation not detected
5. **Refresh token has no expiration** — `TokenStore.swift:89` — infinite session lifetime

**Shall I provide the remediation implementation details?**

---

## Techniques Used

- **ST-01** (Clear Objective): Focused authentication security audit
- **ST-02** (Sequential Instructions): Phased audit across auth methods
- **RT-02** (Multi-Dimensional Analysis): Five auth components evaluated
- **RT-04** (Best Practice Review): Apple and OAuth security best practices

---

## Related Prompts

- [ios_local_data_security_audit.md](ios_local_data_security_audit.md) - Local data storage security
- [ios_cloud_backend_security_audit.md](ios_cloud_backend_security_audit.md) - Cloud and API security
- [ios_codebase_health_assessment.md](ios_codebase_health_assessment.md) - Overall codebase evaluation

---

## Customization Guide

### For Financial / PSD2 Compliance
- Require strong customer authentication (SCA) with two factors
- Verify transaction signing with biometric confirmation
- Check for dynamic linking (amount + payee in auth prompt)
- Audit session timeout requirements (5-minute idle for payments)

### For Enterprise SSO
- Check SAML/OIDC integration with identity providers
- Verify certificate pinning for SSO endpoints
- Audit managed device compliance checks
- Check for conditional access policy enforcement

### For Passwordless Auth
- Verify passkey (FIDO2/WebAuthn) implementation via ASAuthorizationPlatformPublicKeyCredentialProvider
- Check passkey syncing via iCloud Keychain
- Audit fallback mechanisms when passkey is unavailable
- Verify attestation handling

### For Multi-Factor Authentication
- Verify TOTP implementation (time-based OTP)
- Check SMS OTP autofill integration (one-time code detection)
- Audit MFA enrollment flow security
- Verify MFA bypass is not possible via API manipulation
