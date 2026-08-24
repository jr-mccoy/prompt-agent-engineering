---
title: "Android Authentication Security Audit"
category: mobile-development
description: "Conducts comprehensive security audit of authentication flows, 2FA, and session management to identify account takeover vulnerabilities"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-02
difficulty: advanced
tags:
  - android
  - mobile-development
  - security
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_cloud_backend_security_audit.md
  - domain-software-engineering/mobile/android/analysis/android_local_data_security_audit.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_2fa_security_bypass_review.md
---


# Android Authentication Security Audit

**Objective:** Conduct a comprehensive security audit of authentication flows, two-factor authentication (2FA), email verification, session management, and account security to identify vulnerabilities that could lead to account takeover, credential theft, or unauthorized access.

**When to Use:** Use this prompt before publishing apps with user accounts, after implementing authentication features, when adding 2FA or email verification, during security audits, or when investigating suspicious account activity. Essential for any app handling user credentials or sensitive account operations.

**Prompt Type:** Comprehensive (450-550 lines)

---

## Context Gathering

Before beginning the security audit, gather context:

1. **Authentication Methods:**
   - "What authentication methods are implemented (email/password, social login, biometric, magic link)?"
   - "Is 2FA/MFA implemented? What factors (TOTP, SMS, email, push notification)?"
   - "What authentication provider is used (Firebase Auth, custom backend, Auth0, AWS Cognito)?"

2. **Account Features:**
   - "What account management features exist (registration, password reset, email change, account deletion)?"
   - "Are there different user roles or permission levels?"
   - "Is there email verification? Phone verification?"

3. **Session Management:**
   - "How are sessions managed (JWT, session cookies, custom tokens)?"
   - "What is the expected session lifetime?"
   - "Are there multiple device/session requirements?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual authentication flow** - Don't flag based on pattern matching alone. Verify that the suspected vulnerability actually compromises authentication.
2. **Check for existing protections** - Search for server-side validation, token verification, or security libraries that may already protect the flow.
3. **Understand the context** - Consider WHY specific authentication approaches are used. OAuth, Firebase Auth, and custom implementations have different security models.
4. **Confirm actual exploitability** - Can this actually be exploited? What would an attacker need to do?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `LoginViewModel.kt:78`).

**Finding NO issues is an acceptable outcome.** If authentication is properly implemented, say so with confidence. Don't manufacture security concerns.

### False-Positive Prevention

- ❌ Do NOT flag Firebase/OAuth standard flows as insecure without evidence
- ❌ Do NOT flag client-side validation without checking server-side enforcement
- ❌ Do NOT assume missing protections without searching the full auth flow
- ❌ Do NOT report theoretical attacks without demonstrating exploitability
- ✅ DO trace the complete authentication flow from UI to backend
- ✅ DO understand the security guarantees of auth libraries (Firebase, Auth0)
- ✅ DO check for proper token storage and transmission
- ✅ DO verify session management and logout behavior

---

### Phase 1: Authentication Flow Discovery

#### 1.1 Identify Authentication Implementations

**Search for authentication patterns:**

```kotlin
// Firebase Authentication
FirebaseAuth.getInstance()
signInWithEmailAndPassword()
signInWithCredential()
createUserWithEmailAndPassword()
sendPasswordResetEmail()
sendEmailVerification()

// Custom Authentication
LoginRepository
AuthRepository
AuthService
TokenManager
SessionManager

// Biometric Authentication
BiometricPrompt
BiometricManager
KeyguardManager
FingerprintManager (deprecated)

// OAuth/Social Login
GoogleSignIn
GoogleSignInClient
FacebookLogin
LoginManager
signInWithGoogle()
signInWithFacebook()
```

**Authentication Method Inventory:**

| Method | Provider | 2FA Support | Status |
|--------|----------|-------------|--------|
| Email/Password | [Firebase/Custom] | [Yes/No] | [Active/Deprecated] |
| Google Sign-In | [Firebase/Direct] | [Inherits] | [Active/Deprecated] |
| Biometric | [BiometricPrompt] | [N/A] | [Active/Deprecated] |
| [Other] | [Provider] | [Yes/No] | [Status] |

---

### Phase 2: Credential Security Analysis

#### 2.1 Password Handling

**Check password security practices:**

```kotlin
// CRITICAL: Sending password in plain text to logs
Log.d("Login", "Password: $password")

// CRITICAL: Storing password locally
prefs.putString("password", password)

// CRITICAL: Weak password validation
fun isValidPassword(password: String): Boolean {
    return password.length >= 4  // TOO WEAK
}

// SECURE: Strong password validation
fun isValidPassword(password: String): Boolean {
    val hasMinLength = password.length >= 12
    val hasUppercase = password.any { it.isUpperCase() }
    val hasLowercase = password.any { it.isLowerCase() }
    val hasDigit = password.any { it.isDigit() }
    val hasSpecial = password.any { !it.isLetterOrDigit() }
    return hasMinLength && hasUppercase && hasLowercase && hasDigit && hasSpecial
}

// Check password transmission
// CRITICAL: HTTP instead of HTTPS
val request = Request.Builder()
    .url("http://api.example.com/login")  // NOT HTTPS!
    .post(body)
    .build()
```

**Password Security Checklist:**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Minimum length ≥ 12 | [Yes/No] | [Current: N] |
| Complexity requirements | [Yes/No] | [Details] |
| Never stored locally | [Yes/No] | [Location if stored] |
| Never logged | [Yes/No] | [Log location if found] |
| HTTPS only | [Yes/No] | [Endpoints] |
| Rate limiting | [Yes/No] | [Limit details] |

#### 2.2 Credential Exposure Analysis

**Search for credential leaks:**

```kotlin
// Check for credentials in:
// 1. BuildConfig / gradle.properties
buildConfigField("String", "API_KEY", "\"hardcoded_key\"")  // CRITICAL

// 2. strings.xml or other resources
<string name="api_secret">secret_value</string>  // CRITICAL

// 3. Source code
private const val CLIENT_SECRET = "abc123"  // CRITICAL

// 4. Network interceptors/logging
HttpLoggingInterceptor().apply {
    level = HttpLoggingInterceptor.Level.BODY  // Logs all request bodies including passwords
}

// 5. Crash reports
Crashlytics.setCustomKey("auth_token", token)  // HIGH RISK
```

---

### Phase 3: Two-Factor Authentication (2FA) Review

#### 3.1 2FA Implementation Assessment

**Identify 2FA mechanisms:**

```kotlin
// TOTP (Time-based One-Time Password)
GoogleAuthenticator
TOTPGenerator
generateTOTP()
verifyTOTP()

// SMS Verification
sendSmsCode()
verifySmsCode()
PhoneAuthProvider  // Firebase

// Email Verification Codes
sendEmailCode()
verifyEmailCode()

// Push Notification 2FA
sendPushChallenge()
verifyPushResponse()

// Biometric as 2FA
BiometricPrompt
setUserAuthenticationRequired(true)
```

**2FA Security Analysis:**

```kotlin
// CRITICAL: TOTP secret stored insecurely
prefs.putString("totp_secret", totpSecret)  // Should be encrypted

// CRITICAL: No rate limiting on code verification
fun verifyCode(code: String): Boolean {
    return code == expectedCode  // No attempt tracking!
}

// SECURE: Rate-limited verification with lockout
fun verifyCode(userId: String, code: String): VerificationResult {
    val attempts = getFailedAttempts(userId)
    if (attempts >= MAX_ATTEMPTS) {
        return VerificationResult.LockedOut(getLockoutRemainingTime(userId))
    }

    if (code != expectedCode) {
        incrementFailedAttempts(userId)
        return VerificationResult.Failed(MAX_ATTEMPTS - attempts - 1)
    }

    resetFailedAttempts(userId)
    return VerificationResult.Success
}

// CRITICAL: SMS code too short or predictable
val smsCode = Random.nextInt(1000, 9999).toString()  // Only 4 digits!

// SECURE: Cryptographically random code
val smsCode = SecureRandom().nextInt(900000) + 100000  // 6 digits
```

**2FA Checklist:**

| Factor | Implementation | Secure Storage | Rate Limited | Expiration |
|--------|---------------|----------------|--------------|------------|
| TOTP | [Yes/No] | [Encrypted/Plain] | [N/A] | [30s standard] |
| SMS | [Yes/No] | [N/A] | [Yes/No] | [Minutes] |
| Email Code | [Yes/No] | [N/A] | [Yes/No] | [Minutes] |
| Push | [Yes/No] | [N/A] | [Yes/No] | [Minutes] |

#### 3.2 2FA Bypass Vulnerabilities

**Check for bypass vectors:**

```kotlin
// CRITICAL: 2FA can be skipped via direct API call
@POST("/api/login")
suspend fun login(
    @Body credentials: LoginRequest
): AuthResponse  // Returns token without 2FA check!

// CRITICAL: 2FA check only on client side
if (user.has2FAEnabled) {
    navigateTo2FAScreen()  // Can be bypassed by calling API directly
}

// CRITICAL: 2FA remembered indefinitely
prefs.putBoolean("2fa_verified_${deviceId}", true)  // Never expires!

// SECURE: Time-limited 2FA trust
fun is2FATrusted(deviceId: String): Boolean {
    val trustExpiry = prefs.getLong("2fa_trust_expiry_$deviceId", 0)
    return System.currentTimeMillis() < trustExpiry
}

// CRITICAL: Backup codes stored insecurely or reusable
backupCodes.forEach { code ->
    if (input == code) return true  // Codes should be single-use!
}
```

---

### Phase 4: Email Verification Security

#### 4.1 Email Verification Flow

**Analyze email verification implementation:**

```kotlin
// Firebase Email Verification
user.sendEmailVerification()
user.isEmailVerified

// Custom Email Verification
fun sendVerificationEmail(email: String) {
    val token = generateVerificationToken()
    emailService.send(email, "Verify: ${baseUrl}/verify?token=$token")
}

// Check verification token security
// CRITICAL: Predictable token
val token = UUID.randomUUID().toString()  // UUID v4 is acceptable
val token = "${userId}_${timestamp}"  // PREDICTABLE - CRITICAL!

// CRITICAL: Token never expires
fun verifyEmail(token: String): Boolean {
    val email = tokenStore.get(token)  // No expiration check!
    return email != null
}

// SECURE: Time-limited token verification
fun verifyEmail(token: String): VerificationResult {
    val record = tokenStore.get(token) ?: return VerificationResult.InvalidToken

    if (System.currentTimeMillis() > record.expiresAt) {
        tokenStore.remove(token)
        return VerificationResult.Expired
    }

    markEmailVerified(record.userId)
    tokenStore.remove(token)  // Single use
    return VerificationResult.Success
}
```

**Email Verification Checklist:**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Token cryptographically random | [Yes/No] | [Generation method] |
| Token expiration (≤ 24 hours) | [Yes/No] | [Expiry time] |
| Single-use tokens | [Yes/No] | |
| Rate limiting on send | [Yes/No] | [Limit] |
| Verified status enforced server-side | [Yes/No] | |

#### 4.2 Account Enumeration Prevention

**Check for account enumeration vulnerabilities:**

```kotlin
// VULNERABLE: Different responses reveal account existence
fun login(email: String, password: String): LoginResult {
    val user = userRepository.findByEmail(email)
    if (user == null) {
        return LoginResult.Error("User not found")  // REVEALS USER EXISTS
    }
    if (!verifyPassword(password, user.passwordHash)) {
        return LoginResult.Error("Incorrect password")  // DIFFERENT MESSAGE
    }
    return LoginResult.Success(user)
}

// SECURE: Consistent error messages
fun login(email: String, password: String): LoginResult {
    val user = userRepository.findByEmail(email)
    val passwordValid = user?.let { verifyPassword(password, it.passwordHash) } ?: false

    if (user == null || !passwordValid) {
        delay(randomDelay())  // Prevent timing attacks
        return LoginResult.Error("Invalid email or password")  // SAME MESSAGE
    }
    return LoginResult.Success(user)
}

// VULNERABLE: Registration reveals existing accounts
fun register(email: String): RegistrationResult {
    if (userRepository.existsByEmail(email)) {
        return RegistrationResult.Error("Email already registered")  // REVEALS EXISTENCE
    }
    // ...
}

// SECURE: Consistent registration response
fun register(email: String): RegistrationResult {
    // Always return success, send different email content
    if (userRepository.existsByEmail(email)) {
        emailService.sendAccountExistsNotification(email)
    } else {
        emailService.sendVerificationEmail(email)
    }
    return RegistrationResult.Success("Check your email")
}
```

---

### Phase 5: Session Management Security

#### 5.1 Token Security

**Analyze token implementation:**

```kotlin
// JWT Token Analysis
// Check for weak signing algorithms
// CRITICAL: None algorithm or weak signature
val jwt = Jwts.builder()
    .setSubject(userId)
    .signWith(SignatureAlgorithm.NONE, "")  // NO SIGNATURE!

// CRITICAL: Weak secret key
val jwt = Jwts.builder()
    .signWith(SignatureAlgorithm.HS256, "secret")  // WEAK KEY

// SECURE: Strong key with RS256
val jwt = Jwts.builder()
    .setSubject(userId)
    .setIssuedAt(Date())
    .setExpiration(Date(System.currentTimeMillis() + TOKEN_EXPIRY))
    .signWith(SignatureAlgorithm.RS256, privateKey)
    .compact()

// Check token storage
// CRITICAL: Token in plain SharedPreferences
prefs.putString("auth_token", token)

// SECURE: Token in EncryptedSharedPreferences
securePrefs.edit().putString("auth_token", token).apply()

// Check token transmission
// CRITICAL: Token in URL parameters
val url = "https://api.example.com/data?token=$authToken"  // LOGGED IN HISTORY!

// SECURE: Token in Authorization header
.addHeader("Authorization", "Bearer $authToken")
```

**Token Security Checklist:**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Strong signing algorithm (RS256/ES256) | [Yes/No] | [Algorithm used] |
| Appropriate expiration (≤ 1 hour access) | [Yes/No] | [Expiry time] |
| Secure storage | [Yes/No] | [Storage method] |
| Refresh token rotation | [Yes/No] | |
| Token revocation support | [Yes/No] | |

#### 5.2 Session Lifecycle

**Check session management:**

```kotlin
// Session expiration
// CRITICAL: Sessions never expire
val token = generateToken(userId)  // No expiration!

// CRITICAL: Refresh tokens don't expire or rotate
fun refreshToken(refreshToken: String): TokenPair {
    val userId = validateRefreshToken(refreshToken)
    return TokenPair(
        accessToken = generateAccessToken(userId),
        refreshToken = refreshToken  // SAME REFRESH TOKEN - SHOULD ROTATE!
    )
}

// SECURE: Refresh token rotation
fun refreshToken(refreshToken: String): TokenPair {
    val tokenRecord = refreshTokenStore.validate(refreshToken)
        ?: throw InvalidTokenException()

    refreshTokenStore.revoke(refreshToken)  // Revoke old token

    return TokenPair(
        accessToken = generateAccessToken(tokenRecord.userId),
        refreshToken = generateRefreshToken(tokenRecord.userId)  // NEW TOKEN
    )
}

// Session invalidation on logout
// CRITICAL: Logout doesn't invalidate server-side
fun logout() {
    localTokenStorage.clear()  // Only clears locally!
}

// SECURE: Server-side token revocation
suspend fun logout() {
    api.revokeToken(currentToken)  // Revoke on server
    localTokenStorage.clear()
}

// Session invalidation on password change
// CRITICAL: Password change doesn't invalidate sessions
fun changePassword(oldPassword: String, newPassword: String) {
    validatePassword(oldPassword)
    updatePassword(newPassword)
    // Other sessions still valid!
}

// SECURE: Invalidate all sessions on password change
suspend fun changePassword(oldPassword: String, newPassword: String) {
    validatePassword(oldPassword)
    updatePassword(newPassword)
    api.revokeAllSessions(exceptCurrent = true)  // Revoke other sessions
    notifySessionsRevoked()
}
```

#### 5.3 Multi-Device Session Management

**Evaluate multiple device handling:**

```kotlin
// Check for concurrent session limits
// CRITICAL: Unlimited concurrent sessions
fun createSession(userId: String): Session {
    return Session(userId, generateToken())  // No limit check!
}

// SECURE: Limit concurrent sessions
fun createSession(userId: String): Session {
    val activeSessions = sessionStore.getActiveSessions(userId)
    if (activeSessions.size >= MAX_SESSIONS) {
        sessionStore.revokeOldest(userId)  // Or reject new login
    }
    return Session(userId, generateToken())
}

// Check session visibility to user
// Users should be able to see and revoke active sessions
fun getActiveSessions(): List<SessionInfo> {
    return sessionStore.getSessionsForUser(currentUserId)
        .map { SessionInfo(it.deviceName, it.lastActive, it.location) }
}
```

---

### Phase 6: Password Reset Security

#### 6.1 Password Reset Flow

**Analyze password reset implementation:**

```kotlin
// CRITICAL: Predictable reset token
val resetToken = "${userId}_${System.currentTimeMillis()}"  // PREDICTABLE!

// CRITICAL: Reset token doesn't expire
fun validateResetToken(token: String): String? {
    return resetTokenStore.get(token)  // No expiration!
}

// CRITICAL: Token not invalidated after use
fun resetPassword(token: String, newPassword: String) {
    val userId = validateResetToken(token)
    updatePassword(userId, newPassword)
    // Token still valid for reuse!
}

// SECURE: Proper reset token handling
fun createResetToken(email: String): String? {
    val user = userRepository.findByEmail(email) ?: run {
        delay(randomDelay())  // Prevent timing attack
        return null
    }

    // Invalidate any existing reset tokens
    resetTokenStore.revokeForUser(user.id)

    val token = SecureRandom().let { random ->
        ByteArray(32).also { random.nextBytes(it) }
    }.let { Base64.encodeToString(it, Base64.URL_SAFE) }

    resetTokenStore.save(ResetToken(
        token = hash(token),
        userId = user.id,
        expiresAt = System.currentTimeMillis() + TimeUnit.HOURS.toMillis(1)
    ))

    return token
}

fun resetPassword(token: String, newPassword: String): Result {
    val record = resetTokenStore.findByHash(hash(token))
        ?: return Result.InvalidToken

    if (System.currentTimeMillis() > record.expiresAt) {
        resetTokenStore.delete(record.token)
        return Result.TokenExpired
    }

    updatePassword(record.userId, newPassword)
    resetTokenStore.delete(record.token)  // Single use
    revokeAllSessions(record.userId)  // Invalidate existing sessions
    return Result.Success
}
```

**Password Reset Checklist:**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Cryptographically random token | [Yes/No] | |
| Token expiration (≤ 1 hour) | [Yes/No] | [Expiry time] |
| Single-use tokens | [Yes/No] | |
| Rate limiting | [Yes/No] | |
| Invalidates existing sessions | [Yes/No] | |
| Consistent response (no enumeration) | [Yes/No] | |

---

### Phase 7: OAuth/Social Login Security

#### 7.1 OAuth Implementation Review

**Analyze OAuth flows:**

```kotlin
// Google Sign-In Security
val gso = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
    .requestIdToken(getString(R.string.web_client_id))
    .requestEmail()
    .build()

// CRITICAL: Not verifying ID token on backend
fun handleGoogleSignIn(idToken: String) {
    // Sending raw ID token without backend verification!
    api.loginWithGoogle(idToken)
}

// SECURE: Backend verifies Google ID token
// Backend code should verify:
// 1. Token signature
// 2. Token expiration
// 3. Audience (aud) matches your client ID
// 4. Issuer (iss) is accounts.google.com

// Check for OAuth state parameter (CSRF protection)
// CRITICAL: No state parameter
val authUrl = "https://accounts.google.com/o/oauth2/auth?client_id=...&redirect_uri=..."

// SECURE: State parameter for CSRF protection
val state = SecureRandom().nextBytes(32).encodeBase64()
sessionStore.saveOAuthState(state)
val authUrl = "...&state=$state"

// On callback
fun handleOAuthCallback(code: String, state: String) {
    if (!sessionStore.validateAndConsumeState(state)) {
        throw SecurityException("Invalid OAuth state")
    }
    // Exchange code for token
}
```

#### 7.2 Deep Link Security for OAuth

**Check OAuth redirect URI security:**

```kotlin
// CRITICAL: Custom scheme can be hijacked
<intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <data android:scheme="myapp" android:host="oauth" />
</intent-filter>

// SECURE: App Links with verification
<intent-filter android:autoVerify="true">
    <action android:name="android.intent.action.VIEW" />
    <data
        android:scheme="https"
        android:host="yourapp.com"
        android:pathPrefix="/oauth/callback" />
</intent-filter>

// Verify incoming OAuth callbacks
fun handleOAuthDeepLink(intent: Intent) {
    val uri = intent.data ?: return

    // Verify the callback is from expected source
    if (uri.host != "yourapp.com") {
        Log.w("OAuth", "Unexpected OAuth callback host")
        return
    }

    val code = uri.getQueryParameter("code")
    val state = uri.getQueryParameter("state")

    if (!validateState(state)) {
        throw SecurityException("OAuth state mismatch")
    }

    exchangeCodeForToken(code)
}
```

---

### Phase 8: Biometric Authentication Security

#### 8.1 Biometric Implementation Review

**Analyze biometric authentication:**

```kotlin
// CRITICAL: Biometric only protects UI, not data
fun authenticateWithBiometric(onSuccess: () -> Unit) {
    biometricPrompt.authenticate(promptInfo, object : AuthenticationCallback() {
        override fun onAuthenticationSucceeded(result: AuthenticationResult) {
            onSuccess()  // Just proceeds without cryptographic binding!
        }
    })
}

// SECURE: Biometric-bound cryptographic key
val keyGenerator = KeyGenerator.getInstance(
    KeyProperties.KEY_ALGORITHM_AES,
    "AndroidKeyStore"
)

keyGenerator.init(
    KeyGenParameterSpec.Builder("biometric_key",
        KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT)
        .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
        .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
        .setUserAuthenticationRequired(true)
        .setUserAuthenticationParameters(
            0,  // Every use requires authentication
            KeyProperties.AUTH_BIOMETRIC_STRONG
        )
        .setInvalidatedByBiometricEnrollment(true)
        .build()
)

// Use with CryptoObject
val cipher = Cipher.getInstance("AES/GCM/NoPadding")
val secretKey = keyStore.getKey("biometric_key", null) as SecretKey
cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec)

val cryptoObject = BiometricPrompt.CryptoObject(cipher)
biometricPrompt.authenticate(promptInfo, cryptoObject)
```

**Biometric Security Checklist:**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Uses CryptoObject | [Yes/No] | |
| Key requires authentication | [Yes/No] | |
| Invalidated on biometric change | [Yes/No] | |
| Fallback mechanism secure | [Yes/No] | [Fallback type] |
| Strong biometrics only | [Yes/No] | |

---

### Phase 9: Findings Summary

**CHECKPOINT:** Present security audit findings summary.

```markdown
## Authentication Security Audit Summary

### Overall Security Posture: [Critical/High/Medium/Low Risk]

### Authentication Methods
| Method | Implementation | Security Level | Issues Found |
|--------|---------------|----------------|--------------|
| Email/Password | [Provider] | [Secure/Vulnerable] | [Count] |
| 2FA | [Type] | [Secure/Vulnerable] | [Count] |
| Social Login | [Providers] | [Secure/Vulnerable] | [Count] |
| Biometric | [Yes/No] | [Secure/Vulnerable] | [Count] |

### Critical Findings
1. **[Finding]** - [Brief description and impact]
2. **[Finding]** - [Brief description and impact]

### Session Management
- Token Type: [JWT/Custom]
- Expiration: [Duration]
- Secure Storage: [Yes/No]
- Revocation Support: [Yes/No]

**Shall I proceed with the detailed security report and remediation guidance?**
```

---

### Phase 10: Detailed Security Report

```markdown
# Authentication Security Audit Report: [App Name]

## Executive Summary

### Security Score: [A/B/C/D/F]

| Dimension | Score | Assessment |
|-----------|-------|------------|
| Password Security | [1-10] | [Details] |
| 2FA Implementation | [1-10] | [Details] |
| Session Management | [1-10] | [Details] |
| Token Security | [1-10] | [Details] |
| Account Recovery | [1-10] | [Details] |
| Social Login | [1-10] | [Details] |

### Attack Surface Summary
| Vector | Risk Level | Exploitability |
|--------|------------|----------------|
| Credential Theft | [Level] | [Easy/Medium/Hard] |
| Account Takeover | [Level] | [Easy/Medium/Hard] |
| 2FA Bypass | [Level] | [Easy/Medium/Hard] |
| Session Hijacking | [Level] | [Easy/Medium/Hard] |

---

## Detailed Findings

### Finding 1: [Title]
**Severity:** [Critical/High/Medium/Low]
**Category:** [Credential/Session/2FA/OAuth]
**Location:** [file:line]

**Vulnerable Code:**
```kotlin
[Code snippet]
```

**Attack Scenario:**
1. [Step 1]
2. [Step 2]
3. [Impact]

**Remediation:**
```kotlin
[Secure implementation]
```

---

## Remediation Roadmap

### Immediate (Before Release)

| Fix | Priority | Effort |
|-----|----------|--------|
| [Fix] | Critical | [Hours] |

### Short-term

| Improvement | Rationale | Effort |
|-------------|-----------|--------|
| [Improvement] | [Why] | [Hours/Days] |

---

## Implementation Examples

### Secure Authentication Flow

```kotlin
class SecureAuthRepository(
    private val api: AuthApi,
    private val tokenStorage: SecureTokenStorage,
    private val biometricKeyManager: BiometricKeyManager
) {
    suspend fun login(email: String, password: String): AuthResult {
        // Rate limiting check (client-side as backup)
        if (rateLimiter.isRateLimited()) {
            return AuthResult.RateLimited
        }

        return try {
            val response = api.login(LoginRequest(email, password))

            if (response.requires2FA) {
                return AuthResult.Requires2FA(response.tempToken)
            }

            tokenStorage.saveTokens(
                accessToken = response.accessToken,
                refreshToken = response.refreshToken
            )

            AuthResult.Success(response.user)
        } catch (e: HttpException) {
            when (e.code()) {
                401 -> AuthResult.InvalidCredentials
                429 -> AuthResult.RateLimited
                else -> AuthResult.Error(e.message())
            }
        }
    }

    suspend fun verify2FA(tempToken: String, code: String): AuthResult {
        return try {
            val response = api.verify2FA(Verify2FARequest(tempToken, code))

            tokenStorage.saveTokens(
                accessToken = response.accessToken,
                refreshToken = response.refreshToken
            )

            AuthResult.Success(response.user)
        } catch (e: HttpException) {
            when (e.code()) {
                401 -> AuthResult.Invalid2FACode
                429 -> AuthResult.RateLimited
                else -> AuthResult.Error(e.message())
            }
        }
    }

    suspend fun logout() {
        try {
            api.logout()  // Revoke server-side
        } finally {
            tokenStorage.clearAll()
        }
    }
}
```

### Secure Token Refresh

```kotlin
class TokenRefreshInterceptor(
    private val tokenStorage: SecureTokenStorage,
    private val tokenRefresher: TokenRefresher
) : Interceptor {

    private val mutex = Mutex()

    override fun intercept(chain: Interceptor.Chain): Response {
        val request = chain.request()
        val response = chain.proceed(addAuthHeader(request))

        if (response.code == 401) {
            response.close()

            // Thread-safe token refresh
            runBlocking {
                mutex.withLock {
                    // Check if another thread already refreshed
                    val currentToken = tokenStorage.getAccessToken()
                    if (currentToken != request.header("Authorization")?.removePrefix("Bearer ")) {
                        // Token was refreshed by another thread
                        return@runBlocking
                    }

                    try {
                        val newTokens = tokenRefresher.refresh(tokenStorage.getRefreshToken())
                        tokenStorage.saveTokens(newTokens.accessToken, newTokens.refreshToken)
                    } catch (e: Exception) {
                        tokenStorage.clearAll()
                        throw AuthenticationException("Session expired")
                    }
                }
            }

            return chain.proceed(addAuthHeader(request))
        }

        return response
    }

    private fun addAuthHeader(request: Request): Request {
        val token = tokenStorage.getAccessToken() ?: return request
        return request.newBuilder()
            .header("Authorization", "Bearer $token")
            .build()
    }
}
```
```

---

## Severity Ratings

- **Critical**: Direct account takeover possible (credential exposure, 2FA bypass, weak tokens)
- **High**: Significant security weakness (session fixation, enumeration, weak password policy)
- **Medium**: Defense-in-depth issues (missing rate limiting, suboptimal token expiry)
- **Low**: Minor improvements and hardening recommendations

---

## Expected Output

1. **Authentication Inventory** - All authentication methods and their security status
2. **2FA Assessment** - 2FA implementation quality and bypass vectors
3. **Session Security** - Token handling, storage, and lifecycle analysis
4. **Vulnerability Report** - All issues with severity and remediation
5. **Attack Scenarios** - Step-by-step exploitation for each vulnerability
6. **Secure Implementation** - Production-ready code examples

---

## Techniques Used

- **ST-01** (Clear Objective): Focused authentication security audit objective
- **ST-02** (Sequential Instructions): Phased authentication analysis process
- **RT-02** (Multi-Dimensional Analysis): Credentials, 2FA, sessions, OAuth, biometrics
- **RT-05** (Evidence-Based Reasoning): Code examples and attack scenarios
- **DS-01** (Framework Application): OWASP Authentication Cheat Sheet, NIST 800-63B
- **ST-03** (Output Format Templates): Structured report with tables
- **OC-05** (Severity Classification): Critical/High/Medium/Low ratings
- **AG-05** (Concrete Deliverable Templates): Production-ready secure code

---

## Related Prompts

- [android_local_data_security_audit.md](android_local_data_security_audit.md) - Credential storage security
- [android_cloud_backend_security_audit.md](android_cloud_backend_security_audit.md) - Backend auth validation
- [security_authentication_authorization_review.md](../../../analysis/security/security_authentication_authorization_review.md) - General auth review

---

## Customization Guide

### For Firebase Authentication Apps
- Emphasize Firebase Auth security rules
- Check Firebase ID token verification
- Review custom claims usage
- Verify email verification enforcement

### For Enterprise/B2B Apps
- Focus on SSO/SAML integration security
- Check MFA enforcement policies
- Review session timeout requirements
- Analyze audit logging completeness

### For Financial Apps
- Emphasize transaction authentication
- Check step-up authentication for sensitive ops
- Review session security for financial operations
- Verify PCI-DSS authentication requirements
