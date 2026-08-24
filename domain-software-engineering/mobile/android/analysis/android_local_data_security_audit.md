---
title: "Android Local Data Security Audit"
category: mobile-development
description: "Audits how an Android app stores data locally — database encryption, Keystore usage, SharedPreferences/DataStore, file storage, backups, and logging hygiene — to surface at-rest data-exposure risks."
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
  - domain-software-engineering/mobile/android/analysis/android_authentication_security_audit.md
  - domain-software-engineering/mobile/android/analysis/android_cloud_backend_security_audit.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_sqlcipher_key_management_review.md
---


# Android Local Data Security Audit

**Objective:** Conduct a comprehensive security audit of local data storage, database encryption, keystore usage, and on-device data protection to identify vulnerabilities that could lead to data exposure, tampering, or theft on rooted or compromised devices.

**When to Use:** Use this prompt before publishing an app to production, after implementing local storage features, when handling sensitive user data (PII, financial data, health data), during security audits, or when preparing for compliance reviews (GDPR, HIPAA, PCI-DSS).

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning the security audit, gather context:

1. **Data Sensitivity:**
   - "What types of sensitive data does this app store locally (user credentials, PII, financial data, health records, tokens)?"
   - "Are there compliance requirements (GDPR, HIPAA, PCI-DSS, SOC2)?"

2. **Storage Mechanisms:**
   - "What storage mechanisms are used (Room, SQLite, SharedPreferences, DataStore, files)?"
   - "Is database encryption already implemented? If so, what library (SQLCipher, Android Keystore)?"

3. **Threat Model:**
   - "What is the expected threat model (casual attacker, rooted device, physical access, malware)?"
   - "Are there specific attack vectors you're concerned about?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual data flow** - Don't flag based on pattern matching alone. Verify that the suspected vulnerability actually exposes sensitive data.
2. **Check for existing protections** - Search for EncryptedSharedPreferences, Keystore, SQLCipher, or other encryption that may already protect the data.
3. **Understand the context** - Consider WHAT data is being stored and its actual sensitivity level. Not all local storage needs encryption.
4. **Confirm actual exploitability** - Can this actually be exploited? Root access, backup extraction, or device theft scenarios?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `UserPreferences.kt:67`).

**Finding NO issues is an acceptable outcome.** If local data security is properly implemented, say so with confidence. Don't manufacture security concerns.

### False-Positive Prevention

- ❌ Do NOT flag all SharedPreferences usage as insecure (non-sensitive data doesn't need encryption)
- ❌ Do NOT flag based solely on storage mechanism without understanding data sensitivity
- ❌ Do NOT assume missing encryption without searching for security wrappers
- ❌ Do NOT report theoretical attacks requiring unrealistic attacker capabilities
- ✅ DO understand the Android security model and app sandbox protections
- ✅ DO differentiate between rooted and non-rooted device security
- ✅ DO check for existing encryption layers before flagging
- ✅ DO consider compliance requirements (HIPAA, PCI-DSS) when assessing risk

---

### Phase 1: Storage Mechanism Discovery

#### 1.1 Identify All Local Storage Usage

**Search for storage patterns in the codebase:**

```kotlin
// Room Database Indicators
@Database
@Entity
@Dao
Room.databaseBuilder()
Room.inMemoryDatabaseBuilder()

// SQLite Direct Usage
SQLiteDatabase
SQLiteOpenHelper
rawQuery()
execSQL()

// SharedPreferences
getSharedPreferences()
PreferenceManager.getDefaultSharedPreferences()
SharedPreferences.Editor
.edit().putString()
.commit() / .apply()

// DataStore (Proto and Preferences)
DataStore<Preferences>
preferencesDataStore
ProtoDataStore
Context.dataStore

// File Storage
openFileOutput()
openFileInput()
File()
FileOutputStream
FileInputStream
getFilesDir()
getExternalFilesDir()
getCacheDir()

// Encrypted Storage
EncryptedSharedPreferences
EncryptedFile
MasterKey
SQLCipher
```

**Storage Inventory Table:**

| Storage Type | Location | Encryption | Sensitivity | Risk Level |
|--------------|----------|------------|-------------|------------|
| Room DB | [Path] | [Yes/No] | [High/Medium/Low] | [Critical/High/Medium/Low] |
| SharedPreferences | [Name] | [Yes/No] | [High/Medium/Low] | [Critical/High/Medium/Low] |
| Files | [Directory] | [Yes/No] | [High/Medium/Low] | [Critical/High/Medium/Low] |

---

### Phase 2: Database Security Analysis

#### 2.1 Room/SQLite Encryption Assessment

**Check for unencrypted database storage:**

```kotlin
// VULNERABLE: Unencrypted Room database
Room.databaseBuilder(context, AppDatabase::class.java, "app_database")
    .build()

// SECURE: SQLCipher encryption with Room
val passphrase = getOrCreatePassphrase()
val factory = SupportFactory(passphrase)
Room.databaseBuilder(context, AppDatabase::class.java, "app_database")
    .openHelperFactory(factory)
    .build()

// SECURE: SQLCipher with proper key management
val masterKey = MasterKey.Builder(context)
    .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
    .build()
```

**Encryption Quality Checklist:**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Database encrypted | [Yes/No] | |
| Encryption library | [SQLCipher/None/Custom] | [Version] |
| Key derivation | [PBKDF2/Argon2/None] | [Iterations] |
| Key storage | [Keystore/File/Hardcoded] | |
| Key per-device | [Yes/No] | |

#### 2.2 Sensitive Data in Database

**Identify sensitive columns and tables:**

```kotlin
// HIGH RISK: Storing credentials in plain text
@Entity
data class User(
    @PrimaryKey val id: Int,
    val email: String,
    val password: String,      // CRITICAL: Never store plaintext passwords
    val authToken: String,     // HIGH: Tokens should be encrypted
    val creditCardNumber: String // CRITICAL: PCI-DSS violation
)

// MEDIUM RISK: PII without encryption
@Entity
data class Profile(
    @PrimaryKey val id: Int,
    val fullName: String,      // PII - consider encryption
    val ssn: String,           // CRITICAL: Must be encrypted
    val dateOfBirth: String,   // PII - GDPR relevant
    val address: String        // PII - location data
)
```

**Sensitive Data Classification:**

| Table | Column | Data Type | Sensitivity | Encrypted | Compliance |
|-------|--------|-----------|-------------|-----------|------------|
| [Table] | [Column] | [PII/Financial/Health/Auth] | [Critical/High/Medium] | [Yes/No] | [GDPR/HIPAA/PCI] |

#### 2.3 Database Query Security

**Check for SQL injection vulnerabilities:**

```kotlin
// VULNERABLE: String concatenation in queries
@Query("SELECT * FROM users WHERE email = '" + email + "'")
fun findUserByEmail(email: String): User?

// VULNERABLE: Raw query with concatenation
database.rawQuery("SELECT * FROM users WHERE id = $userId", null)

// SECURE: Parameterized queries
@Query("SELECT * FROM users WHERE email = :email")
fun findUserByEmail(email: String): User?

// SECURE: Room handles parameterization
@Query("SELECT * FROM users WHERE id = :userId AND role = :role")
fun findUser(userId: Int, role: String): User?
```

---

### Phase 3: SharedPreferences/DataStore Security

#### 3.1 SharedPreferences Analysis

**Identify sensitive data in preferences:**

```kotlin
// CRITICAL: Storing sensitive data in plain SharedPreferences
prefs.edit()
    .putString("auth_token", token)        // HIGH RISK
    .putString("password", password)        // CRITICAL
    .putString("api_key", apiKey)          // HIGH RISK
    .putBoolean("is_logged_in", true)      // LOW RISK
    .apply()

// SECURE: Using EncryptedSharedPreferences
val masterKey = MasterKey.Builder(context)
    .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
    .build()

val securePrefs = EncryptedSharedPreferences.create(
    context,
    "secure_prefs",
    masterKey,
    EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
    EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
)
```

**SharedPreferences Security Checklist:**

| Preference File | Keys Stored | Sensitivity | Encrypted | MODE |
|-----------------|-------------|-------------|-----------|------|
| [Name] | [Key list] | [High/Medium/Low] | [Yes/No] | [PRIVATE/WORLD_*] |

#### 3.2 DataStore Security

**Evaluate DataStore implementation:**

```kotlin
// Check for sensitive data in Preferences DataStore
val AUTH_TOKEN = stringPreferencesKey("auth_token")  // Should use encrypted storage

// Proto DataStore - check protobuf definitions for sensitive fields
message UserPreferences {
    string auth_token = 1;    // HIGH RISK if not encrypted
    string password = 2;      // CRITICAL
    bool remember_me = 3;     // LOW RISK
}
```

---

### Phase 4: Android Keystore Analysis

#### 4.1 Keystore Usage Assessment

**Identify Keystore implementations:**

```kotlin
// SECURE: Proper Keystore usage
val keyGenerator = KeyGenerator.getInstance(
    KeyProperties.KEY_ALGORITHM_AES,
    "AndroidKeyStore"
)

val keyGenSpec = KeyGenParameterSpec.Builder(
    "my_key_alias",
    KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT
)
    .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
    .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
    .setUserAuthenticationRequired(true)           // Biometric required
    .setUserAuthenticationValidityDurationSeconds(30)
    .setInvalidatedByBiometricEnrollment(true)
    .setRandomizedEncryptionRequired(true)         // Prevent IV reuse
    .build()

// Check for weak configurations
.setUserAuthenticationRequired(false)              // MEDIUM RISK: No auth required
.setInvalidatedByBiometricEnrollment(false)        // LOW RISK: Key survives re-enrollment
```

**Keystore Configuration Assessment:**

| Key Alias | Algorithm | Purpose | Auth Required | Biometric Bound | StrongBox |
|-----------|-----------|---------|---------------|-----------------|-----------|
| [Alias] | [AES/RSA] | [Encrypt/Sign] | [Yes/No] | [Yes/No] | [Yes/No] |

#### 4.2 Key Management Security

**Check for common key management issues:**

```kotlin
// CRITICAL: Hardcoded encryption keys
private val ENCRYPTION_KEY = "my_secret_key_123"  // NEVER DO THIS

// CRITICAL: Key derivation from weak sources
val key = password.toByteArray()  // Weak key derivation

// CRITICAL: Storing keys in code or assets
val keyFromAssets = assets.open("encryption_key.txt").readBytes()

// SECURE: Key generated and stored in Keystore
val secretKey = keyStore.getKey("my_key_alias", null) as SecretKey
```

---

### Phase 5: File Storage Security

#### 5.1 Internal Storage Analysis

**Check file permissions and locations:**

```kotlin
// Check for world-readable/writable files
openFileOutput("data.txt", Context.MODE_WORLD_READABLE)  // CRITICAL: Deprecated & dangerous

// Verify internal storage usage
context.filesDir          // /data/data/package/files - SECURE
context.cacheDir          // /data/data/package/cache - SECURE for temp data

// Check for sensitive file content
File(context.filesDir, "user_data.json")  // What's being stored?
```

#### 5.2 External Storage Analysis

**Identify external storage vulnerabilities:**

```kotlin
// HIGH RISK: Sensitive data on external storage
val externalFile = File(getExternalFilesDir(null), "sensitive_data.txt")

// CRITICAL: Scoped storage bypass attempts
Environment.getExternalStorageDirectory()  // Deprecated, requires permissions

// Check MediaStore usage for sensitive content
contentResolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values)
```

**File Storage Audit:**

| File Path | Content Type | Sensitivity | Encrypted | External | Risk |
|-----------|--------------|-------------|-----------|----------|------|
| [Path] | [Type] | [High/Medium/Low] | [Yes/No] | [Yes/No] | [Level] |

#### 5.3 Encrypted File Usage

**Evaluate EncryptedFile implementation:**

```kotlin
// SECURE: Using Jetpack Security EncryptedFile
val masterKey = MasterKey.Builder(context)
    .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
    .build()

val encryptedFile = EncryptedFile.Builder(
    context,
    file,
    masterKey,
    EncryptedFile.FileEncryptionScheme.AES256_GCM_HKDF_4KB
).build()

// Writing encrypted content
encryptedFile.openFileOutput().use { outputStream ->
    outputStream.write(sensitiveData)
}
```

---

### Phase 6: Backup and Export Security

#### 6.1 Android Backup Configuration

**Check AndroidManifest.xml backup settings:**

```xml
<!-- CRITICAL: Uncontrolled backup can expose data -->
<application
    android:allowBackup="true"
    android:fullBackupContent="@xml/backup_rules">

<!-- backup_rules.xml - check exclusions -->
<full-backup-content>
    <exclude domain="sharedpref" path="secure_prefs.xml"/>
    <exclude domain="database" path="encrypted.db"/>
    <exclude domain="file" path="secrets/"/>
</full-backup-content>

<!-- Android 12+ data extraction rules -->
<data-extraction-rules>
    <cloud-backup>
        <exclude domain="database" path="sensitive.db"/>
    </cloud-backup>
    <device-transfer>
        <exclude domain="sharedpref" path="auth_tokens.xml"/>
    </device-transfer>
</data-extraction-rules>
```

**Backup Security Checklist:**

| Setting | Value | Risk | Recommendation |
|---------|-------|------|----------------|
| allowBackup | [true/false] | [Level] | [Action] |
| fullBackupContent | [defined/undefined] | [Level] | [Action] |
| dataExtractionRules | [defined/undefined] | [Level] | [Action] |

#### 6.2 Export and Share Functionality

**Identify data export vulnerabilities:**

```kotlin
// Check for unencrypted export features
fun exportUserData(): File {
    val exportFile = File(getExternalFilesDir(null), "export.json")
    exportFile.writeText(gson.toJson(userData))  // Is this encrypted?
    return exportFile
}

// Check share intents for sensitive data
val shareIntent = Intent(Intent.ACTION_SEND).apply {
    type = "application/json"
    putExtra(Intent.EXTRA_STREAM, exportUri)
    // Are permissions properly set?
}
```

---

### Phase 7: Logging and Debug Security

#### 7.1 Sensitive Data in Logs

**Search for sensitive data logging:**

```kotlin
// CRITICAL: Logging sensitive data
Log.d("Auth", "User password: $password")
Log.i("API", "Auth token: $token")
Log.e("Payment", "Card number: $cardNumber")

// Check Timber usage
Timber.d("User credentials: email=$email, password=$password")

// Check for crash reporting with sensitive data
Crashlytics.log("User session: $sessionToken")
```

#### 7.2 Debug Configuration

**Check for debug vulnerabilities:**

```kotlin
// Check BuildConfig
if (BuildConfig.DEBUG) {
    // What debug features are enabled?
}

// Check for debuggable flag in production
android:debuggable="true"  // CRITICAL in production

// Check for WebView debugging
WebView.setWebContentsDebuggingEnabled(true)  // CRITICAL in production
```

---

### Phase 8: Findings Summary

**CHECKPOINT:** Present security audit findings summary.

```markdown
## Local Data Security Audit Summary

### Overall Security Posture: [Critical/High/Medium/Low Risk]

### Storage Inventory
| Storage Type | Count | Encrypted | Unprotected Sensitive Data |
|--------------|-------|-----------|---------------------------|
| Databases | [N] | [N/N] | [Yes/No] |
| SharedPreferences | [N] | [N/N] | [Yes/No] |
| Files | [N] | [N/N] | [Yes/No] |

### Critical Findings
1. **[Finding]** - [Brief description and impact]
2. **[Finding]** - [Brief description and impact]

### High-Priority Findings
1. **[Finding]** - [Brief description and impact]

### Questions Before Detailed Report
1. [Clarifying question about data handling requirements]
2. [Question about compliance requirements]

**Shall I proceed with the detailed security report and remediation guidance?**
```

---

### Phase 9: Detailed Security Report

```markdown
# Local Data Security Audit Report: [App Name]

## Executive Summary

### Security Score: [A/B/C/D/F]

| Dimension | Score | Assessment |
|-----------|-------|------------|
| Database Encryption | [1-10] | [Encrypted/Partial/None] |
| Keystore Usage | [1-10] | [Proper/Partial/Missing] |
| Credential Storage | [1-10] | [Secure/Vulnerable] |
| File Security | [1-10] | [Secure/Vulnerable] |
| Backup Protection | [1-10] | [Protected/Exposed] |
| Logging Hygiene | [1-10] | [Clean/Leaking] |

### Compliance Status
| Standard | Status | Critical Issues |
|----------|--------|-----------------|
| GDPR | [Compliant/Non-Compliant] | [Issues] |
| HIPAA | [N/A/Compliant/Non-Compliant] | [Issues] |
| PCI-DSS | [N/A/Compliant/Non-Compliant] | [Issues] |

---

## Detailed Findings

### 1. Database Security

#### Finding: [Title]
**Severity:** [Critical/High/Medium/Low]
**Location:** [file:line]

**Vulnerable Code:**
```kotlin
[Code snippet showing vulnerability]
```

**Attack Scenario:**
1. Attacker gains physical access to device or extracts backup
2. [Step 2]
3. [Step 3]
4. Result: [Impact]

**Impact:**
- [Business impact]
- [User impact]
- [Compliance impact]

**Remediation:**
```kotlin
[Secure code example]
```

**Verification:**
- [ ] Implement fix
- [ ] Verify with adb shell to check file permissions
- [ ] Test with rooted device/emulator

---

### 2. Credential Storage

[Repeat finding format for each issue]

---

### 3. Keystore Implementation

[Repeat finding format for each issue]

---

## Remediation Roadmap

### Immediate (Before Release)

| Fix | Current State | Target State | Effort |
|-----|---------------|--------------|--------|
| Encrypt database | Plaintext SQLite | SQLCipher + Keystore | [Hours] |
| Move tokens to encrypted storage | SharedPreferences | EncryptedSharedPreferences | [Hours] |
| Remove sensitive logs | Logging credentials | No sensitive data in logs | [Hours] |

### Short-term (Sprint 1-2)

| Improvement | Rationale | Approach |
|-------------|-----------|----------|
| Implement proper key rotation | Key compromise recovery | [Approach] |
| Add biometric protection for sensitive ops | Defense in depth | [Approach] |
| Configure backup exclusions | Prevent data exposure via backup | [Approach] |

### Long-term

| Improvement | Benefit | Complexity |
|-------------|---------|------------|
| Column-level encryption for PII | Granular data protection | Medium |
| StrongBox Keystore usage | Hardware-backed security | Low |
| Data classification system | Systematic protection | High |

---

## Testing Recommendations

### Manual Testing
1. **Rooted device test:** Extract and examine database files
2. **Backup extraction:** Use adb backup and examine contents
3. **Log analysis:** Check logcat for sensitive data exposure
4. **Memory dump:** Check for plaintext secrets in memory

### Automated Testing
```bash
# Extract APK and check for hardcoded secrets
apktool d app.apk
grep -r "password\|secret\|key\|token" ./app/

# Check database encryption
adb shell run-as com.your.package cat databases/app.db | file -

# Check SharedPreferences
adb shell run-as com.your.package cat shared_prefs/*.xml
```

### Tools
- **drozer:** Android security assessment framework
- **Frida:** Dynamic instrumentation toolkit
- **objection:** Runtime mobile exploration
- **MobSF:** Mobile Security Framework for static analysis

---

## Implementation Examples

### SQLCipher with Keystore Integration

```kotlin
class SecureDatabaseFactory(private val context: Context) {

    private val masterKey by lazy {
        MasterKey.Builder(context)
            .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
            .build()
    }

    fun createDatabase(): AppDatabase {
        val passphrase = getOrCreateDatabaseKey()
        val factory = SupportFactory(passphrase)

        return Room.databaseBuilder(
            context,
            AppDatabase::class.java,
            "secure_database"
        )
            .openHelperFactory(factory)
            .build()
    }

    private fun getOrCreateDatabaseKey(): ByteArray {
        val prefs = EncryptedSharedPreferences.create(
            context,
            "db_key_prefs",
            masterKey,
            EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
            EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
        )

        return prefs.getString("db_key", null)?.let {
            Base64.decode(it, Base64.DEFAULT)
        } ?: generateNewKey().also { key ->
            prefs.edit()
                .putString("db_key", Base64.encodeToString(key, Base64.DEFAULT))
                .apply()
        }
    }

    private fun generateNewKey(): ByteArray {
        return ByteArray(32).apply {
            SecureRandom().nextBytes(this)
        }
    }
}
```

### Secure Token Storage

```kotlin
class SecureTokenStorage(context: Context) {

    private val masterKey = MasterKey.Builder(context)
        .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
        .build()

    private val securePrefs = EncryptedSharedPreferences.create(
        context,
        "secure_token_storage",
        masterKey,
        EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
        EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
    )

    fun storeAuthToken(token: String) {
        securePrefs.edit()
            .putString(KEY_AUTH_TOKEN, token)
            .putLong(KEY_TOKEN_TIMESTAMP, System.currentTimeMillis())
            .apply()
    }

    fun getAuthToken(): String? {
        val timestamp = securePrefs.getLong(KEY_TOKEN_TIMESTAMP, 0)
        val age = System.currentTimeMillis() - timestamp

        // Invalidate tokens older than 24 hours
        if (age > TimeUnit.HOURS.toMillis(24)) {
            clearTokens()
            return null
        }

        return securePrefs.getString(KEY_AUTH_TOKEN, null)
    }

    fun clearTokens() {
        securePrefs.edit().clear().apply()
    }

    companion object {
        private const val KEY_AUTH_TOKEN = "auth_token"
        private const val KEY_TOKEN_TIMESTAMP = "token_timestamp"
    }
}
```
```

---

## Severity Ratings

- **Critical**: Data exposure with immediate exploitability (plaintext passwords, unencrypted PII database, hardcoded secrets)
- **High**: Significant vulnerabilities requiring specific conditions (sensitive data in logs, weak encryption, missing backup protection)
- **Medium**: Defense-in-depth issues (missing biometric binding, suboptimal key configuration)
- **Low**: Minor improvements and hardening recommendations

---

## Expected Output

1. **Storage Inventory** - Complete catalog of all local storage mechanisms
2. **Encryption Assessment** - Database and file encryption status with key management review
3. **Vulnerability Report** - All security issues with locations and severity
4. **Compliance Mapping** - GDPR, HIPAA, PCI-DSS relevance for each finding
5. **Remediation Code** - Production-ready secure implementation examples
6. **Testing Guide** - Manual and automated testing procedures

---

## Techniques Used

- **ST-01** (Clear Objective): Focused local data security audit objective
- **ST-02** (Sequential Instructions): Phased discovery and analysis process
- **RT-02** (Multi-Dimensional Analysis): Storage type, encryption, sensitivity, compliance
- **RT-05** (Evidence-Based Reasoning): Code examples and file references
- **DS-01** (Framework Application): OWASP Mobile Top 10, GDPR, HIPAA, PCI-DSS
- **ST-03** (Output Format Templates): Structured report with tables
- **OC-05** (Severity Classification): Critical/High/Medium/Low ratings
- **NE-02** (Phased Workflow): Clear checkpoints between analysis phases
- **AG-05** (Concrete Deliverable Templates): Production-ready code examples

---

## Related Prompts

- [android_authentication_security_audit.md](android_authentication_security_audit.md) - Auth flow security
- [android_cloud_backend_security_audit.md](android_cloud_backend_security_audit.md) - Cloud sync security
- [android_privacy_compliance.md](../publishing/android_privacy_compliance.md) - GDPR/CCPA compliance
- [security_cryptography_encryption_review.md](../../../analysis/security/security_cryptography_encryption_review.md) - General encryption review

---

## Customization Guide

### For Financial Apps (PCI-DSS)
- Emphasize payment card data protection
- Check for PAN storage and encryption
- Verify key management meets PCI requirements
- Review data retention policies

### For Healthcare Apps (HIPAA)
- Focus on PHI (Protected Health Information)
- Verify encryption of health records
- Check access logging requirements
- Review data sharing mechanisms

### For Apps with Biometric Data
- Check BiometricPrompt implementation
- Verify biometric data never leaves device
- Review fallback authentication security
- Check for biometric spoofing protections

### For Offline-First Apps
- Emphasize offline data encryption
- Review sync queue security
- Check for data integrity during sync
- Verify conflict resolution doesn't expose data
