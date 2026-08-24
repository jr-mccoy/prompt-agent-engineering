---
title: "Android 2FA Security & Bypass Prevention Review"
category: mobile/android/targeted-reviews
description: "Android 2FA Security & Bypass Prevention Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - 2fa
  - android
  - bypass
  - mobile
  - reviews
  - security
updated: "2026-03-19"
related_prompts: []
---

# Android 2FA Security & Bypass Prevention Review

**Objective:** Conduct a targeted security review of two-factor authentication implementation in Android applications, analyzing TOTP/HOTP generation, backup codes, recovery flows, bypass vulnerabilities, and secure storage of 2FA secrets.

**When to Use:** Use this prompt when implementing or auditing 2FA features, before security compliance audits, when users report 2FA bypass issues, during penetration testing preparation, or when reviewing authentication flows for financial or sensitive apps.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual code path** - Don't flag based on pattern matching alone. Follow the data flow from source to sink.
2. **Check for existing protections** - Search the codebase for sanitization, validation, or framework-provided security that may exist elsewhere.
3. **Understand the context** - Consider WHY the code is written this way. Framework constraints, library APIs, and architectural decisions may make seemingly risky patterns safe.
4. **Confirm actual exploitability** - Can this actually be exploited? What would an attacker need to do?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `AuthRepository.kt:142`).

**Finding NO issues is an acceptable outcome.** Do not manufacture findings to fill a report. If the implementation is secure, say so with confidence.

### False-Positive Prevention

- ❌ Do NOT flag framework-idiomatic code as problematic (e.g., standard BiometricPrompt patterns, Keystore usage)
- ❌ Do NOT flag based solely on keywords/patterns (e.g., seeing `SharedPreferences` without checking if it's EncryptedSharedPreferences)
- ❌ Do NOT assume missing protections without searching the codebase
- ❌ Do NOT report theoretical vulnerabilities that require unrealistic attack scenarios
- ✅ DO trace complete code flows before flagging
- ✅ DO check for server-side validation when reviewing client-side code
- ✅ DO understand Android security model and Keystore guarantees
- ✅ DO verify that reported issues are actually exploitable in context

---

### 1. 2FA Secret Generation & Storage

Analyze secret key management:

* **Secret Generation:**
  - Review random number generation (use SecureRandom)
  - Check secret length (minimum 160 bits for TOTP)
  - Assess entropy sources
  - Verify no predictable patterns

* **Secret Storage:**
  - Check for Android Keystore usage
  - Review EncryptedSharedPreferences implementation
  - Assess key protection (hardware-backed if available)
  - Verify secrets are not in plain SharedPreferences

* **Secret Transmission:**
  - Review QR code generation security
  - Check for secure secret sharing
  - Assess HTTPS enforcement for setup
  - Verify no logging of secrets

* **Secret Backup:**
  - Check if secrets are excluded from Android backup
  - Review backup encryption if allowed
  - Assess cloud backup security
  - Verify no plain-text export

### 2. TOTP/HOTP Implementation

Evaluate OTP algorithm implementation:

* **Algorithm Correctness:**
  - Review TOTP implementation (RFC 6238)
  - Check HOTP implementation (RFC 4226)
  - Assess time step configuration (30 seconds standard)
  - Verify SHA algorithm usage (SHA-1/SHA-256/SHA-512)

* **Time Synchronization:**
  - Check for time drift handling
  - Review time window tolerance
  - Assess NTP synchronization issues
  - Verify server-client time sync

* **Counter Management (HOTP):**
  - Review counter persistence
  - Check for counter resynchronization
  - Assess look-ahead window
  - Verify counter increment only on success

* **Code Validation:**
  - Check for constant-time comparison
  - Review brute-force protection
  - Assess rate limiting implementation
  - Verify replay attack prevention

### 3. Backup Codes

Analyze backup code implementation:

* **Generation:**
  - Review backup code entropy
  - Check for cryptographically secure generation
  - Assess code format (length, character set)
  - Verify uniqueness per user

* **Storage:**
  - Check server-side hashing of backup codes
  - Review salting implementation
  - Assess client-side storage (should be minimal)
  - Verify secure display to user

* **Redemption:**
  - Check single-use enforcement
  - Review code invalidation after use
  - Assess remaining code tracking
  - Verify rate limiting on attempts

* **Regeneration:**
  - Check regeneration triggers strong auth
  - Review old code invalidation
  - Assess user notification on regeneration
  - Verify audit logging

### 4. Recovery Flows

Evaluate account recovery security:

* **Recovery Email/SMS:**
  - Review recovery token generation
  - Check token expiration (short-lived)
  - Assess rate limiting
  - Verify no token in URL parameters

* **Identity Verification:**
  - Check KYC requirements for recovery
  - Review security questions (discouraged)
  - Assess support-assisted recovery
  - Verify recovery audit trail

* **2FA Removal:**
  - Check strong authentication before removal
  - Review cooling-off period
  - Assess notification on 2FA changes
  - Verify cannot disable during suspicious activity

* **Device Trust:**
  - Review trusted device management
  - Check device fingerprinting
  - Assess device limit enforcement
  - Verify device removal requires 2FA

### 5. Bypass Prevention

Identify common bypass vulnerabilities:

* **Race Conditions:**
  - Check for TOCTOU vulnerabilities
  - Review concurrent request handling
  - Assess session state management
  - Verify atomic 2FA verification

* **Session Handling:**
  - Check 2FA completion flag in session
  - Review session fixation prevention
  - Assess partial authentication state
  - Verify 2FA required for all protected resources

* **API Bypass:**
  - Check all API endpoints require 2FA when enabled
  - Review mobile vs web API parity
  - Assess legacy endpoint security
  - Verify internal APIs also protected

* **Parameter Tampering:**
  - Check for 2FA skip parameters
  - Review debug/test mode flags
  - Assess hidden admin bypasses
  - Verify feature flags are secure

* **Response Manipulation:**
  - Check for client-side 2FA enforcement
  - Review API response security
  - Assess JWT/token verification
  - Verify no front-end only checks

### 6. Rate Limiting & Lockout

Analyze brute-force protections:

* **Attempt Limiting:**
  - Check maximum attempts before lockout
  - Review attempt counter persistence
  - Assess per-IP vs per-account limiting
  - Verify exponential backoff

* **Lockout Policy:**
  - Check lockout duration (progressive)
  - Review unlock mechanisms
  - Assess admin override capability
  - Verify lockout notification to user

* **Bypass Detection:**
  - Check for distributed attack detection
  - Review IP rotation handling
  - Assess account enumeration prevention
  - Verify suspicious activity alerts

### 7. Biometric Integration

Evaluate biometric 2FA:

* **Biometric API Usage:**
  - Review BiometricPrompt implementation
  - Check CryptoObject binding
  - Assess authenticator types allowed
  - Verify proper error handling

* **Fallback Handling:**
  - Check fallback to OTP on biometric failure
  - Review device credential fallback security
  - Assess lockout on repeated failures
  - Verify no bypass via fallback

* **Biometric Binding:**
  - Check biometric invalidation on change
  - Review re-enrollment requirements
  - Assess multi-biometric support
  - Verify biometric is tied to secret

### 8. Push-Based 2FA

Analyze push notification 2FA:

* **Challenge-Response:**
  - Review challenge generation
  - Check challenge binding to session
  - Assess challenge expiration
  - Verify challenge uniqueness

* **Approval Flow:**
  - Check for "push bombing" prevention
  - Review approval rate limiting
  - Assess denial logging
  - Verify approval is cryptographically bound

* **Device Registration:**
  - Review secure device registration
  - Check push token rotation
  - Assess device attestation
  - Verify device binding to account

### 9. Security Audit Trail

Evaluate 2FA logging:

* **Event Logging:**
  - Check successful 2FA verification logged
  - Review failed attempt logging
  - Assess configuration change logging
  - Verify log integrity protection

* **Alerting:**
  - Check alerts on repeated failures
  - Review alerts on 2FA disable
  - Assess alerts on new device
  - Verify real-time alerting capability

---

## Expected Output

Provide a comprehensive 2FA security review including:

### 1. Executive Summary
- Overall 2FA implementation security rating
- Critical bypass vulnerabilities
- Compliance gaps (PCI DSS, SOC2, etc.)
- High-risk attack vectors

### 2. Vulnerability Assessment Matrix

| Category | Implementation | Bypass Risk | Compliance | Priority |
|----------|---------------|-------------|------------|----------|
| [Area] | [Status] | [Low/Medium/High/Critical] | [Pass/Fail] | [P0-P3] |

### 3. Detailed Findings

For each vulnerability:
- **Location:** Code/API endpoint
- **Issue:** Description of vulnerability
- **Attack Vector:** How it could be exploited
- **Severity:** Critical/High/Medium/Low
- **Current Code:** Vulnerable implementation
- **Recommended Fix:** Secure implementation

### 4. Compliance Checklist

Against relevant standards (NIST, PCI DSS, etc.).

### 5. Prioritized Remediation

Ordered by exploitability and impact.

---

## Example Output

```markdown
# 2FA Security & Bypass Prevention Review

## Executive Summary
- **Overall Security:** Poor - Critical bypass vulnerabilities found
- **Bypass Vulnerabilities:** 4 critical, 3 high severity
- **Compliance:** PCI DSS 8.3 - FAIL, NIST 800-63B - FAIL
- **Immediate Risk:** Account takeover possible via 2FA bypass

## Critical Findings

### CRITICAL-1: 2FA Bypass via Direct API Access
**Severity:** Critical
**CVSS:** 9.8 (Critical)
**Attack Vector:** Remote, unauthenticated

**Scenario:**
1. Attacker obtains valid username/password
2. Attacker calls authenticated endpoint directly
3. Server only checks 2FA on /login, not subsequent calls
4. Full account access without 2FA

**Location:** AuthInterceptor.kt

**Current Implementation:**
```kotlin
// VULNERABLE: Only checking 2FA on login screen, not API calls
class AuthInterceptor @Inject constructor(
    private val authRepository: AuthRepository
) : Interceptor {

    override fun intercept(chain: Interceptor.Chain): Response {
        val request = chain.request()

        // PROBLEM: Token is valid even without 2FA completion!
        val token = authRepository.getAccessToken()

        val authenticatedRequest = if (token != null) {
            request.newBuilder()
                .addHeader("Authorization", "Bearer $token")
                .build()
        } else {
            request
        }

        return chain.proceed(authenticatedRequest)
    }
}

// Login flow issues:
class LoginViewModel : ViewModel() {

    fun login(username: String, password: String) {
        viewModelScope.launch {
            val result = authApi.login(username, password)
            // PROBLEM: Token issued BEFORE 2FA verification!
            authRepository.saveToken(result.accessToken)

            if (result.requires2FA) {
                _navigateTo.emit(Screen.TwoFactor)
            } else {
                _navigateTo.emit(Screen.Home)
            }
        }
    }
}
```

**Attack Scenario:**
```kotlin
// Attacker can skip 2FA screen entirely
val api = Retrofit.Builder()
    .baseUrl("https://api.example.com")
    .build()
    .create(AppApi::class.java)

// Login gives token even with 2FA required
val loginResponse = api.login("victim@email.com", "password123")
val token = loginResponse.accessToken  // Token works without 2FA!

// Access protected resources directly
val sensitiveData = api.getSensitiveData(
    authorization = "Bearer $token"
)  // SUCCESS - 2FA bypassed!
```

**Recommended Fix:**
```kotlin
// SECURE: Use limited-scope token until 2FA complete
data class AuthTokens(
    val preAuthToken: String?,    // Limited scope, can only verify 2FA
    val accessToken: String?,     // Full access, only after 2FA
    val requires2FA: Boolean
)

class AuthRepository @Inject constructor(
    private val tokenStore: TokenStore
) {
    fun getPreAuthToken(): String? = tokenStore.preAuthToken
    fun getAccessToken(): String? = tokenStore.accessToken  // Only set after 2FA

    fun savePreAuthToken(token: String) {
        tokenStore.preAuthToken = token
        tokenStore.accessToken = null  // Clear any existing access token
    }

    fun promoteToAccessToken(accessToken: String) {
        tokenStore.preAuthToken = null
        tokenStore.accessToken = accessToken
    }
}

// Login flow:
class LoginViewModel @Inject constructor(
    private val authRepository: AuthRepository,
    private val authApi: AuthApi
) : ViewModel() {

    fun login(username: String, password: String) {
        viewModelScope.launch {
            val result = authApi.login(username, password)

            if (result.requires2FA) {
                // Save PRE-AUTH token only - limited scope
                authRepository.savePreAuthToken(result.preAuthToken)
                _navigateTo.emit(Screen.TwoFactor)
            } else {
                // No 2FA required, save full access token
                authRepository.promoteToAccessToken(result.accessToken)
                _navigateTo.emit(Screen.Home)
            }
        }
    }
}

// 2FA verification:
class TwoFactorViewModel @Inject constructor(
    private val authRepository: AuthRepository,
    private val authApi: AuthApi
) : ViewModel() {

    fun verify2FA(code: String) {
        viewModelScope.launch {
            val preAuthToken = authRepository.getPreAuthToken()
                ?: throw IllegalStateException("No pre-auth token")

            val result = authApi.verify2FA(
                preAuthToken = preAuthToken,
                code = code
            )

            // NOW we get the full access token
            authRepository.promoteToAccessToken(result.accessToken)
            _navigateTo.emit(Screen.Home)
        }
    }
}

// API interceptor:
class AuthInterceptor @Inject constructor(
    private val authRepository: AuthRepository
) : Interceptor {

    override fun intercept(chain: Interceptor.Chain): Response {
        val request = chain.request()

        // SECURE: Use access token (post-2FA) for all API calls
        val token = authRepository.getAccessToken()
            ?: throw UnauthorizedException("Authentication required")

        val authenticatedRequest = request.newBuilder()
            .addHeader("Authorization", "Bearer $token")
            .build()

        return chain.proceed(authenticatedRequest)
    }
}
```

---

### CRITICAL-2: TOTP Secret Stored in Plain SharedPreferences
**Severity:** Critical
**Attack Vector:** Device access, backup extraction

**Location:** TotpRepository.kt

**Current Implementation:**
```kotlin
// VULNERABLE: Plain text storage of TOTP secret
class TotpRepository @Inject constructor(
    @ApplicationContext private val context: Context
) {
    private val prefs = context.getSharedPreferences("totp", Context.MODE_PRIVATE)

    // CRITICAL: Secret stored in plain text!
    fun saveSecret(secret: String) {
        prefs.edit().putString("totp_secret", secret).apply()
    }

    fun getSecret(): String? {
        return prefs.getString("totp_secret", null)
    }
}

// Manifest doesn't exclude from backup
// <application
//     android:allowBackup="true"  // SECRET CAN BE EXTRACTED!
//     ...
```

**Attack Scenario:**
1. Attacker gains ADB access or extracts backup
2. Reads /data/data/com.app/shared_prefs/totp.xml
3. Gets TOTP secret in plain text
4. Generates valid OTPs indefinitely

**Recommended Fix:**
```kotlin
// SECURE: Use Android Keystore with EncryptedSharedPreferences
class TotpRepository @Inject constructor(
    @ApplicationContext private val context: Context
) {
    private val encryptedPrefs: SharedPreferences by lazy {
        val masterKey = MasterKey.Builder(context)
            .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
            .setRequestStrongBoxBacked(true)  // Hardware security if available
            .build()

        EncryptedSharedPreferences.create(
            context,
            "totp_secure",
            masterKey,
            EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
            EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
        )
    }

    // Secret is encrypted at rest
    fun saveSecret(secret: ByteArray) {
        encryptedPrefs.edit()
            .putString("totp_secret", Base64.encodeToString(secret, Base64.NO_WRAP))
            .apply()
    }

    fun getSecret(): ByteArray? {
        return encryptedPrefs.getString("totp_secret", null)?.let {
            Base64.decode(it, Base64.NO_WRAP)
        }
    }

    fun clearSecret() {
        encryptedPrefs.edit().remove("totp_secret").apply()
    }
}

// Backup rules: res/xml/backup_rules.xml
// <?xml version="1.0" encoding="utf-8"?>
// <full-backup-content>
//     <exclude domain="sharedpref" path="totp_secure.xml"/>
// </full-backup-content>

// AndroidManifest.xml
// <application
//     android:allowBackup="true"
//     android:fullBackupContent="@xml/backup_rules"
//     android:dataExtractionRules="@xml/data_extraction_rules"
//     ...
```

---

### CRITICAL-3: Race Condition in 2FA Verification
**Severity:** Critical
**Attack Vector:** Concurrent requests

**Location:** TwoFactorApi.kt (Backend) + TwoFactorViewModel.kt

**Scenario:**
1. Attacker captures pre-auth token
2. Sends 100 concurrent 2FA verification requests
3. Race condition allows multiple attempts within rate limit window
4. 6-digit OTP can be brute-forced (1 million possibilities)

**Current Implementation (Server-side concept):**
```kotlin
// VULNERABLE: Non-atomic check-and-increment
@RestController
class TwoFactorController(
    private val attemptRepository: AttemptRepository,
    private val totpService: TotpService
) {
    @PostMapping("/verify-2fa")
    fun verify2FA(@RequestBody request: Verify2FARequest): Response {
        val attempts = attemptRepository.getAttempts(request.preAuthToken)

        // RACE CONDITION: Check happens before increment
        if (attempts >= 5) {
            return Response.error("Too many attempts")
        }

        val isValid = totpService.verify(request.preAuthToken, request.code)

        // Another request could have verified in parallel!
        attemptRepository.incrementAttempts(request.preAuthToken)

        return if (isValid) {
            Response.success(generateAccessToken())
        } else {
            Response.error("Invalid code")
        }
    }
}
```

**Client-Side Rate Limiting (Insufficient):**
```kotlin
// VULNERABLE: Client-side rate limiting can be bypassed
class TwoFactorViewModel : ViewModel() {
    private var lastAttemptTime = 0L
    private var attempts = 0

    fun verify(code: String) {
        // PROBLEM: Attacker can bypass by calling API directly
        if (attempts >= 5) {
            _error.emit("Too many attempts")
            return
        }

        val now = System.currentTimeMillis()
        if (now - lastAttemptTime < 1000) {
            _error.emit("Please wait")
            return
        }

        // Attacker ignores this and calls API directly
        viewModelScope.launch {
            authApi.verify2FA(code)
        }
    }
}
```

**Recommended Fix (Server-side):**
```kotlin
// SECURE: Atomic operations with distributed locking
@Service
class TwoFactorService(
    private val redisTemplate: RedisTemplate<String, Int>,
    private val totpService: TotpService
) {
    companion object {
        const val MAX_ATTEMPTS = 5
        const val LOCKOUT_DURATION = 300L  // 5 minutes
    }

    fun verify2FA(preAuthToken: String, code: String): VerifyResult {
        val key = "2fa_attempts:$preAuthToken"

        // ATOMIC: Increment and check in one operation
        val attempts = redisTemplate.opsForValue().increment(key) ?: 1

        // Set expiry on first attempt
        if (attempts == 1L) {
            redisTemplate.expire(key, LOCKOUT_DURATION, TimeUnit.SECONDS)
        }

        if (attempts > MAX_ATTEMPTS) {
            // Progressive lockout
            val lockoutSeconds = LOCKOUT_DURATION * (attempts / MAX_ATTEMPTS)
            redisTemplate.expire(key, lockoutSeconds, TimeUnit.SECONDS)
            return VerifyResult.RateLimited(lockoutSeconds)
        }

        // Use constant-time comparison
        return if (totpService.verifyConstantTime(preAuthToken, code)) {
            redisTemplate.delete(key)
            VerifyResult.Success(generateAccessToken())
        } else {
            VerifyResult.InvalidCode(MAX_ATTEMPTS - attempts.toInt())
        }
    }
}

// Constant-time TOTP verification
class TotpService {
    fun verifyConstantTime(token: String, code: String): Boolean {
        val secret = getSecretForToken(token)
        val expectedCode = generateTOTP(secret, System.currentTimeMillis())

        // SECURE: Constant-time comparison prevents timing attacks
        return MessageDigest.isEqual(
            code.toByteArray(Charsets.UTF_8),
            expectedCode.toByteArray(Charsets.UTF_8)
        )
    }
}
```

---

### HIGH-1: Backup Codes Not Hashed
**Severity:** High
**Attack Vector:** Database breach

**Location:** BackupCodeRepository.kt

**Current Implementation:**
```kotlin
// VULNERABLE: Backup codes stored in plain text
@Entity(tableName = "backup_codes")
data class BackupCodeEntity(
    @PrimaryKey val code: String,  // PLAIN TEXT!
    val used: Boolean = false,
    val createdAt: Long = System.currentTimeMillis()
)

class BackupCodeRepository @Inject constructor(
    private val backupCodeDao: BackupCodeDao
) {
    suspend fun generateBackupCodes(): List<String> {
        val codes = (1..10).map {
            generateSecureCode()  // e.g., "XXXX-XXXX-XXXX"
        }

        // Storing plain text - if DB leaked, all codes exposed
        backupCodeDao.insertAll(codes.map { BackupCodeEntity(code = it) })

        return codes  // Show to user once
    }

    suspend fun validateBackupCode(code: String): Boolean {
        val entity = backupCodeDao.findByCode(code)  // Direct lookup!
        if (entity != null && !entity.used) {
            backupCodeDao.markUsed(code)
            return true
        }
        return false
    }
}
```

**Recommended Fix:**
```kotlin
// SECURE: Hash backup codes, store only hash
@Entity(tableName = "backup_codes")
data class BackupCodeEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val codeHash: String,  // Hashed with salt
    val salt: String,
    val used: Boolean = false,
    val createdAt: Long = System.currentTimeMillis()
)

class BackupCodeRepository @Inject constructor(
    private val backupCodeDao: BackupCodeDao
) {
    private val argon2 = Argon2Factory.create()

    suspend fun generateBackupCodes(): List<String> {
        val codes = (1..10).map { generateSecureCode() }

        val entities = codes.map { code ->
            val salt = generateSalt()
            val hash = hashCode(code, salt)
            BackupCodeEntity(codeHash = hash, salt = salt)
        }

        backupCodeDao.insertAll(entities)

        return codes  // Show to user ONCE, never store plain
    }

    suspend fun validateBackupCode(code: String): Boolean {
        // Must check ALL unused codes (can't lookup by hash directly)
        val unusedCodes = backupCodeDao.getUnusedCodes()

        for (entity in unusedCodes) {
            val candidateHash = hashCode(code, entity.salt)

            // Constant-time comparison
            if (MessageDigest.isEqual(
                    entity.codeHash.toByteArray(),
                    candidateHash.toByteArray()
                )) {
                backupCodeDao.markUsed(entity.id)
                return true
            }
        }
        return false
    }

    private fun hashCode(code: String, salt: String): String {
        return argon2.hash(
            iterations = 3,
            memory = 65536,
            parallelism = 1,
            password = code.toCharArray(),
            salt = salt.toByteArray()
        )
    }

    private fun generateSalt(): String {
        val bytes = ByteArray(16)
        SecureRandom().nextBytes(bytes)
        return Base64.encodeToString(bytes, Base64.NO_WRAP)
    }

    private fun generateSecureCode(): String {
        val chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"  // No confusing chars
        val random = SecureRandom()
        return (1..12).map { chars[random.nextInt(chars.length)] }
            .chunked(4)
            .joinToString("-") { it.joinToString("") }
    }
}
```

---

### HIGH-2: Biometric Fallback Bypass
**Severity:** High
**Attack Vector:** Repeated biometric failure, social engineering

**Location:** BiometricAuthManager.kt

**Current Implementation:**
```kotlin
// VULNERABLE: Weak fallback after biometric failure
class BiometricAuthManager @Inject constructor(
    private val context: Context
) {
    fun authenticate(
        onSuccess: () -> Unit,
        onError: (String) -> Unit
    ) {
        val biometricPrompt = BiometricPrompt(
            context as FragmentActivity,
            ContextCompat.getMainExecutor(context),
            object : BiometricPrompt.AuthenticationCallback() {
                override fun onAuthenticationSucceeded(result: AuthenticationResult) {
                    onSuccess()
                }

                override fun onAuthenticationError(errorCode: Int, errString: CharSequence) {
                    // PROBLEM: Falls back to device PIN after any error
                    if (errorCode == BiometricPrompt.ERROR_LOCKOUT ||
                        errorCode == BiometricPrompt.ERROR_LOCKOUT_PERMANENT) {
                        // Fallback to device credential - weaker!
                        authenticateWithDeviceCredential(onSuccess, onError)
                    }
                }

                override fun onAuthenticationFailed() {
                    // Just retry - no attempt counting
                }
            }
        )

        val promptInfo = BiometricPrompt.PromptInfo.Builder()
            .setTitle("Verify Identity")
            .setNegativeButtonText("Cancel")  // No device credential allowed here
            .build()

        biometricPrompt.authenticate(promptInfo)
    }

    private fun authenticateWithDeviceCredential(
        onSuccess: () -> Unit,
        onError: (String) -> Unit
    ) {
        // PROBLEM: Device PIN is much weaker than biometric
        val promptInfo = BiometricPrompt.PromptInfo.Builder()
            .setTitle("Enter PIN")
            .setAllowedAuthenticators(DEVICE_CREDENTIAL)  // PIN/Pattern/Password
            .build()

        biometricPrompt.authenticate(promptInfo)
    }
}
```

**Recommended Fix:**
```kotlin
// SECURE: Biometric bound to crypto operation, controlled fallback
class BiometricAuthManager @Inject constructor(
    private val context: Context,
    private val keyManager: BiometricKeyManager
) {
    fun authenticateFor2FA(
        onSuccess: (signature: ByteArray) -> Unit,
        onFallbackRequired: () -> Unit,
        onError: (BiometricError) -> Unit
    ) {
        // Get crypto object bound to biometric key
        val cryptoObject = try {
            keyManager.getCryptoObject()
        } catch (e: KeyPermanentlyInvalidatedException) {
            // Biometrics changed - require full re-enrollment
            onError(BiometricError.BiometricsChanged)
            return
        }

        val biometricPrompt = BiometricPrompt(
            context as FragmentActivity,
            ContextCompat.getMainExecutor(context),
            object : BiometricPrompt.AuthenticationCallback() {
                override fun onAuthenticationSucceeded(result: AuthenticationResult) {
                    // Use crypto object to sign challenge
                    val signature = result.cryptoObject?.signature
                        ?.let { keyManager.signChallenge(it) }
                        ?: run {
                            onError(BiometricError.CryptoError)
                            return
                        }
                    onSuccess(signature)
                }

                override fun onAuthenticationError(errorCode: Int, errString: CharSequence) {
                    when (errorCode) {
                        ERROR_LOCKOUT, ERROR_LOCKOUT_PERMANENT -> {
                            // Don't auto-fallback, require TOTP
                            onFallbackRequired()
                        }
                        ERROR_NEGATIVE_BUTTON, ERROR_USER_CANCELED -> {
                            onFallbackRequired()
                        }
                        else -> {
                            onError(BiometricError.Unknown(errString.toString()))
                        }
                    }
                }
            }
        )

        val promptInfo = BiometricPrompt.PromptInfo.Builder()
            .setTitle("Verify with Biometrics")
            .setSubtitle("Authenticate to access secure features")
            .setNegativeButtonText("Use OTP instead")
            // NO setAllowedAuthenticators with DEVICE_CREDENTIAL
            .setAllowedAuthenticators(BIOMETRIC_STRONG)
            .build()

        biometricPrompt.authenticate(promptInfo, cryptoObject)
    }
}

class BiometricKeyManager @Inject constructor() {
    companion object {
        const val KEY_ALIAS = "2fa_biometric_key"
    }

    fun generateKey() {
        val keyGenerator = KeyGenerator.getInstance(
            KeyProperties.KEY_ALGORITHM_AES,
            "AndroidKeyStore"
        )

        keyGenerator.init(
            KeyGenParameterSpec.Builder(
                KEY_ALIAS,
                KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT
            )
                .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                .setUserAuthenticationRequired(true)
                .setUserAuthenticationParameters(
                    0,  // Require auth for every use
                    KeyProperties.AUTH_BIOMETRIC_STRONG
                )
                .setInvalidatedByBiometricEnrollment(true)  // Invalidate if biometrics change
                .build()
        )

        keyGenerator.generateKey()
    }

    fun getCryptoObject(): BiometricPrompt.CryptoObject {
        val keyStore = KeyStore.getInstance("AndroidKeyStore").apply { load(null) }
        val key = keyStore.getKey(KEY_ALIAS, null) as SecretKey

        val cipher = Cipher.getInstance("AES/GCM/NoPadding")
        cipher.init(Cipher.ENCRYPT_MODE, key)

        return BiometricPrompt.CryptoObject(cipher)
    }
}
```

---

### MEDIUM-1: No 2FA Status Check on Sensitive Operations
**Severity:** Medium
**Attack Vector:** Session hijacking post-2FA

**Location:** TransactionViewModel.kt

**Current Implementation:**
```kotlin
// VULNERABLE: No step-up authentication for sensitive operations
class TransactionViewModel @Inject constructor(
    private val transactionApi: TransactionApi
) : ViewModel() {

    fun transferMoney(amount: Double, toAccount: String) {
        viewModelScope.launch {
            // PROBLEM: No re-verification for high-value transaction
            val result = transactionApi.transfer(
                TransferRequest(amount, toAccount)
            )
            _result.emit(result)
        }
    }
}
```

**Recommended Fix:**
```kotlin
// SECURE: Step-up authentication for sensitive operations
class TransactionViewModel @Inject constructor(
    private val transactionApi: TransactionApi,
    private val stepUpAuth: StepUpAuthManager
) : ViewModel() {

    fun transferMoney(amount: Double, toAccount: String) {
        viewModelScope.launch {
            // Check if step-up auth required
            if (amount > 1000 || !stepUpAuth.isRecentlyVerified()) {
                _requiresStepUp.emit(StepUpReason.HighValueTransaction(amount))
                return@launch
            }

            val result = transactionApi.transfer(
                TransferRequest(amount, toAccount),
                stepUpToken = stepUpAuth.getStepUpToken()
            )
            _result.emit(result)
        }
    }

    fun completeWithStepUp(code: String) {
        viewModelScope.launch {
            val verified = stepUpAuth.verify(code)
            if (verified) {
                // Retry the pending operation
                pendingTransfer?.let { transferMoney(it.amount, it.toAccount) }
            }
        }
    }
}

class StepUpAuthManager @Inject constructor(
    private val authApi: AuthApi
) {
    private var lastVerification: Long = 0
    private var stepUpToken: String? = null

    companion object {
        const val STEP_UP_VALIDITY_MS = 5 * 60 * 1000  // 5 minutes
    }

    fun isRecentlyVerified(): Boolean {
        return System.currentTimeMillis() - lastVerification < STEP_UP_VALIDITY_MS
    }

    suspend fun verify(code: String): Boolean {
        val result = authApi.verifyStepUp(code)
        if (result.isSuccess) {
            lastVerification = System.currentTimeMillis()
            stepUpToken = result.stepUpToken
        }
        return result.isSuccess
    }

    fun getStepUpToken(): String? = stepUpToken
}
```

---

## Vulnerability Assessment Matrix

| Category | Status | Bypass Risk | Compliance | Priority |
|----------|--------|-------------|------------|----------|
| Token Scope | ❌ Pre-auth = Full | Critical | PCI 8.3 FAIL | P0 |
| Secret Storage | ❌ Plain SharedPrefs | Critical | NIST FAIL | P0 |
| Rate Limiting | ❌ Race condition | Critical | SOC2 FAIL | P0 |
| Backup Codes | ❌ Not hashed | High | NIST FAIL | P1 |
| Biometric Fallback | ⚠️ Too permissive | High | - | P1 |
| Step-Up Auth | ❌ Missing | Medium | PCI FAIL | P2 |
| Audit Logging | ⚠️ Incomplete | Low | SOC2 WARN | P2 |
| Push 2FA | N/A | - | - | - |

## Remediation Priority

### Critical (Immediate - Stop the Presses)
1. Implement pre-auth vs access token separation
2. Move TOTP secrets to EncryptedSharedPreferences
3. Fix race condition in 2FA verification (server-side)

### High Priority (This Sprint)
1. Hash backup codes with Argon2
2. Restrict biometric fallback paths
3. Add attempt logging and alerting

### Medium Priority (Next Sprint)
1. Implement step-up authentication
2. Add 2FA status to JWT claims
3. Complete audit trail implementation

### Low Priority (Backlog)
1. Consider hardware security keys (FIDO2)
2. Add 2FA recovery via trusted contacts
3. Implement push-based 2FA option
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - 2FA security focus
- **ST-02** (Structured Sequential Instructions) - Systematic audit
- **RT-02** (Multi-Dimensional Analysis) - Generation, storage, verification, bypass
- **RT-05** (Evidence-Based Reasoning) - Attack scenarios with code
- **ST-03** (Output Format Templates) - Vulnerability matrix
- **DS-06** (Prioritization Guidance) - CVSS-based ordering
- **QA-02** (Edge Case Coverage) - Bypass scenarios

---

## Related Prompts

- `android_sqlcipher_key_management_review.md` - For secure key storage
- `android_e2e_encryption_review.md` - For cryptographic patterns
- `mobile_app_security_review.md` - For general mobile security
- `security_vulnerability_analysis.md` - For broader security review
- `android_process_death_recovery_review.md` - For 2FA state persistence

---

## Customization Guide

- **For Banking Apps:** Focus on step-up auth, transaction signing, session binding
- **For Healthcare Apps:** Add HIPAA compliance checks, audit requirements
- **For Enterprise Apps:** Focus on SSO integration, device trust policies
- **For Consumer Apps:** Focus on recovery flows, usability vs security balance
- **For Crypto/Wallet Apps:** Add hardware key support, multi-sig patterns
