---
title: "Android Cloud Backend Security Audit"
category: mobile-development
description: "Conducts a comprehensive security audit of an Android app's cloud backend — Firestore/Realtime Database security rules, Cloud Functions authorization, data sync integrity, API security, and Cloud Storage access — to surface data-exposure and privilege-escalation risks."
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
  - domain-software-engineering/mobile/android/analysis/android_privacy_data_flow_audit.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_firebase_security_rules_audit.md
---


# Android Cloud Backend Security Audit

**Objective:** Conduct a comprehensive security audit of cloud database integration, data synchronization, cloud functions, and backend API security to identify vulnerabilities that could lead to data breaches, unauthorized access, data integrity issues, or service abuse.

**When to Use:** Use this prompt before publishing apps with cloud backends, after implementing Firebase/cloud integrations, when setting up data sync mechanisms, during security audits, or when preparing for production deployment. Essential for apps with user data stored in cloud databases.

**Prompt Type:** Comprehensive (500-600 lines)

---

## Context Gathering

Before beginning the security audit, gather context:

1. **Cloud Services:**
   - "What cloud platform is used (Firebase, AWS, GCP, Azure, custom backend)?"
   - "What cloud databases are used (Firestore, Realtime Database, DynamoDB, custom)?"
   - "Are cloud functions used (Firebase Functions, AWS Lambda, Cloud Functions)?"

2. **Sync Architecture:**
   - "How is data synchronized between device and cloud (real-time, periodic, on-demand)?"
   - "Is there offline-first functionality?"
   - "How are sync conflicts handled?"

3. **Data Model:**
   - "What types of data are stored in the cloud (user profiles, content, transactions)?"
   - "Are there multi-tenant or shared data scenarios?"
   - "What are the data ownership and access rules?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual data flow** - Don't flag based on pattern matching alone. Verify that the suspected vulnerability actually exposes data or allows unauthorized access.
2. **Check for existing protections** - Search for security rules, server-side validation, or Cloud Functions that may enforce security beyond client code.
3. **Understand the context** - Consider WHY certain access patterns exist. Some data is intentionally public or shared within groups.
4. **Confirm actual exploitability** - Can this actually be exploited? Test with real requests or Firebase Rules Playground.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `UserRepository.kt:89`, `firestore.rules:23`).

**Finding NO issues is an acceptable outcome.** If cloud security is properly configured, say so with confidence. Don't manufacture security concerns.

### False-Positive Prevention

- ❌ Do NOT flag public data paths as vulnerabilities without understanding the data model
- ❌ Do NOT flag client-side code patterns without checking server-side security rules
- ❌ Do NOT assume missing authentication without tracing the complete auth flow
- ❌ Do NOT report theoretical attacks without demonstrating actual exploitability
- ✅ DO test security rules with actual requests or emulators
- ✅ DO check Cloud Functions for server-side validation
- ✅ DO understand Firebase's security model and custom claims
- ✅ DO consider intentional sharing scenarios (families, teams, public content)

---

### Phase 1: Cloud Service Discovery

#### 1.1 Identify Cloud Integrations

**Search for cloud service patterns:**

```kotlin
// Firebase Core
FirebaseApp.initializeApp()
google-services.json
Firebase.* imports

// Firestore
FirebaseFirestore.getInstance()
collection()
document()
addSnapshotListener()
.set() / .update() / .delete()

// Realtime Database
FirebaseDatabase.getInstance()
getReference()
setValue()
addValueEventListener()

// Firebase Cloud Functions
FirebaseFunctions.getInstance()
httpsCallable()

// Firebase Storage
FirebaseStorage.getInstance()
storageRef.putFile()
storageRef.downloadUrl

// AWS Services
AWSMobileClient
DynamoDBMapper
CognitoIdentityProvider
LambdaInvokerFactory
S3Client

// Custom Backend
Retrofit
OkHttp
API calls
```

**Cloud Service Inventory:**

| Service | Purpose | Data Types | Security Rules |
|---------|---------|------------|----------------|
| Firestore | [Purpose] | [Data types] | [Configured/Missing] |
| Cloud Functions | [Purpose] | [Operations] | [Auth required/Open] |
| Cloud Storage | [Purpose] | [File types] | [Rules configured] |
| [Custom API] | [Purpose] | [Data types] | [Auth mechanism] |

---

### Phase 2: Database Security Rules Analysis

#### 2.1 Firestore Security Rules

**Analyze Firestore security rules:**

```javascript
// CRITICAL: Open access - anyone can read/write everything
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true;  // CRITICAL VULNERABILITY!
    }
  }
}

// CRITICAL: Authentication only, no authorization
match /users/{userId} {
  allow read, write: if request.auth != null;  // Any user can modify any user!
}

// VULNERABLE: Incomplete ownership check
match /posts/{postId} {
  allow read: if true;
  allow write: if request.auth.uid == resource.data.authorId;
  // Missing: allow create - authorId can be set to anything!
}

// SECURE: Proper ownership validation
match /users/{userId} {
  allow read: if request.auth != null && request.auth.uid == userId;
  allow write: if request.auth != null && request.auth.uid == userId;
}

match /posts/{postId} {
  allow read: if true;
  allow create: if request.auth != null
                && request.resource.data.authorId == request.auth.uid
                && request.resource.data.createdAt == request.time;
  allow update: if request.auth != null
                && resource.data.authorId == request.auth.uid
                && request.resource.data.authorId == resource.data.authorId;  // Can't change author
  allow delete: if request.auth != null
                && resource.data.authorId == request.auth.uid;
}
```

**Security Rules Checklist:**

| Collection | Read Rules | Write Rules | Issues |
|------------|------------|-------------|--------|
| users | [Rule] | [Rule] | [Issues] |
| [collection] | [Rule] | [Rule] | [Issues] |

#### 2.2 Realtime Database Rules

**Analyze Realtime Database rules:**

```json
// CRITICAL: Open access
{
  "rules": {
    ".read": true,
    ".write": true
  }
}

// VULNERABLE: Only checks authentication
{
  "rules": {
    "users": {
      "$uid": {
        ".read": "auth != null",
        ".write": "auth != null"
      }
    }
  }
}

// SECURE: Proper authorization
{
  "rules": {
    "users": {
      "$uid": {
        ".read": "auth != null && auth.uid == $uid",
        ".write": "auth != null && auth.uid == $uid"
      }
    },
    "posts": {
      "$postId": {
        ".read": true,
        ".write": "auth != null && (!data.exists() || data.child('authorId').val() == auth.uid)",
        ".validate": "newData.hasChildren(['title', 'content', 'authorId']) && newData.child('authorId').val() == auth.uid"
      }
    }
  }
}
```

#### 2.3 Data Validation Rules

**Check for data validation in security rules:**

```javascript
// CRITICAL: No data validation - malicious data accepted
match /users/{userId} {
  allow write: if request.auth.uid == userId;
  // No validation of data structure or content!
}

// SECURE: Comprehensive data validation
match /users/{userId} {
  allow write: if request.auth.uid == userId
    && request.resource.data.keys().hasOnly(['name', 'email', 'photoUrl', 'updatedAt'])
    && request.resource.data.name is string
    && request.resource.data.name.size() <= 100
    && request.resource.data.name.size() >= 1
    && request.resource.data.email is string
    && request.resource.data.email.matches('^[^@]+@[^@]+\\.[^@]+$')
    && (request.resource.data.photoUrl == null || request.resource.data.photoUrl.matches('^https://.*'))
    && request.resource.data.updatedAt == request.time;
}

// Validate nested data
match /orders/{orderId} {
  allow create: if request.auth != null
    && request.resource.data.userId == request.auth.uid
    && request.resource.data.items is list
    && request.resource.data.items.size() > 0
    && request.resource.data.items.size() <= 100
    && request.resource.data.total is number
    && request.resource.data.total > 0
    && request.resource.data.status == 'pending';
}
```

---

### Phase 3: Cloud Functions Security

#### 3.1 Cloud Functions Authentication

**Analyze cloud functions security:**

```typescript
// CRITICAL: No authentication check
export const deleteUser = functions.https.onCall(async (data, context) => {
  const { userId } = data;
  await admin.firestore().collection('users').doc(userId).delete();
  // Anyone can delete any user!
});

// VULNERABLE: Checks auth but not authorization
export const getUserData = functions.https.onCall(async (data, context) => {
  if (!context.auth) {
    throw new functions.https.HttpsError('unauthenticated', 'Not authenticated');
  }
  const { userId } = data;
  return await admin.firestore().collection('users').doc(userId).get();
  // Any authenticated user can read any user's data!
});

// SECURE: Proper authentication and authorization
export const getUserData = functions.https.onCall(async (data, context) => {
  if (!context.auth) {
    throw new functions.https.HttpsError('unauthenticated', 'Not authenticated');
  }

  const { userId } = data;

  // Users can only access their own data
  if (context.auth.uid !== userId) {
    throw new functions.https.HttpsError('permission-denied', 'Not authorized');
  }

  const userDoc = await admin.firestore().collection('users').doc(userId).get();
  if (!userDoc.exists) {
    throw new functions.https.HttpsError('not-found', 'User not found');
  }

  return userDoc.data();
});
```

#### 3.2 Cloud Functions Input Validation

**Check for input validation:**

```typescript
// CRITICAL: No input validation
export const updateProfile = functions.https.onCall(async (data, context) => {
  await admin.firestore()
    .collection('users')
    .doc(context.auth!.uid)
    .update(data);  // Accepts ANY data!
});

// CRITICAL: SQL/NoSQL injection potential
export const searchUsers = functions.https.onCall(async (data, context) => {
  const { query } = data;
  // If using raw queries, this could be dangerous
  return await admin.firestore()
    .collection('users')
    .where('name', '>=', query)
    .get();
});

// SECURE: Strict input validation
import * as yup from 'yup';

const updateProfileSchema = yup.object({
  name: yup.string().min(1).max(100).required(),
  bio: yup.string().max(500).optional(),
  photoUrl: yup.string().url().optional(),
}).noUnknown(true);

export const updateProfile = functions.https.onCall(async (data, context) => {
  if (!context.auth) {
    throw new functions.https.HttpsError('unauthenticated', 'Not authenticated');
  }

  let validatedData;
  try {
    validatedData = await updateProfileSchema.validate(data, { stripUnknown: true });
  } catch (error) {
    throw new functions.https.HttpsError('invalid-argument', 'Invalid input data');
  }

  await admin.firestore()
    .collection('users')
    .doc(context.auth.uid)
    .update({
      ...validatedData,
      updatedAt: admin.firestore.FieldValue.serverTimestamp(),
    });
});
```

#### 3.3 Cloud Functions Rate Limiting

**Check for abuse prevention:**

```typescript
// CRITICAL: No rate limiting - DoS and abuse possible
export const sendMessage = functions.https.onCall(async (data, context) => {
  await admin.firestore().collection('messages').add({
    ...data,
    senderId: context.auth!.uid,
    timestamp: admin.firestore.FieldValue.serverTimestamp(),
  });
  // Can be called millions of times!
});

// SECURE: Rate limiting implementation
const rateLimit = new Map<string, { count: number; resetTime: number }>();

function checkRateLimit(uid: string, limit: number, windowMs: number): boolean {
  const now = Date.now();
  const userLimit = rateLimit.get(uid);

  if (!userLimit || now > userLimit.resetTime) {
    rateLimit.set(uid, { count: 1, resetTime: now + windowMs });
    return true;
  }

  if (userLimit.count >= limit) {
    return false;
  }

  userLimit.count++;
  return true;
}

export const sendMessage = functions.https.onCall(async (data, context) => {
  if (!context.auth) {
    throw new functions.https.HttpsError('unauthenticated', 'Not authenticated');
  }

  if (!checkRateLimit(context.auth.uid, 60, 60000)) {  // 60 per minute
    throw new functions.https.HttpsError('resource-exhausted', 'Rate limit exceeded');
  }

  // Process message...
});
```

---

### Phase 4: Data Sync Security

#### 4.1 Sync Architecture Analysis

**Identify sync patterns:**

```kotlin
// Real-time sync listeners
firestore.collection("chats")
    .whereEqualTo("participants", userId)
    .addSnapshotListener { snapshots, error ->
        // Check: Is this query properly scoped?
        // Can a user receive data they shouldn't?
    }

// Offline persistence
FirebaseFirestore.getInstance().apply {
    firestoreSettings = FirebaseFirestoreSettings.Builder()
        .setPersistenceEnabled(true)  // Data cached locally
        .build()
}
// Check: Is sensitive data excluded from offline cache?

// Sync queue implementation
class SyncManager {
    private val pendingOperations = mutableListOf<SyncOperation>()

    fun queueOperation(operation: SyncOperation) {
        // Check: Are operations validated before sync?
        // Check: Is there conflict resolution?
        // Check: Are operations idempotent?
    }
}
```

#### 4.2 Conflict Resolution Security

**Analyze conflict handling:**

```kotlin
// CRITICAL: Last-write-wins without validation
fun syncDocument(localDoc: Document, remoteDoc: Document): Document {
    return if (localDoc.timestamp > remoteDoc.timestamp) {
        localDoc  // Could overwrite valid remote changes with malicious local data
    } else {
        remoteDoc
    }
}

// VULNERABLE: Client controls merge logic
fun mergeConflict(local: Map<String, Any>, remote: Map<String, Any>): Map<String, Any> {
    // Client-side merge can be manipulated
    return local + remote
}

// SECURE: Server-side conflict resolution
// Cloud Function handles conflict
export const resolveConflict = functions.https.onCall(async (data, context) => {
  const { documentId, localVersion, changes } = data;

  await admin.firestore().runTransaction(async (transaction) => {
    const doc = await transaction.get(
      admin.firestore().collection('documents').doc(documentId)
    );

    if (doc.data()?.version !== localVersion) {
      // Conflict detected - apply merge rules server-side
      throw new functions.https.HttpsError(
        'aborted',
        'Conflict detected',
        { currentVersion: doc.data()?.version }
      );
    }

    // Validate and apply changes
    const validatedChanges = validateChanges(changes, context.auth!.uid);

    transaction.update(doc.ref, {
      ...validatedChanges,
      version: admin.firestore.FieldValue.increment(1),
      lastModifiedBy: context.auth!.uid,
      lastModifiedAt: admin.firestore.FieldValue.serverTimestamp(),
    });
  });
});
```

#### 4.3 Data Integrity Verification

**Check for data integrity measures:**

```kotlin
// CRITICAL: No integrity verification
fun processServerData(data: Map<String, Any>) {
    // Directly uses data without verification
    saveLocally(data)
}

// SECURE: Data integrity verification
data class SyncedDocument(
    val id: String,
    val data: Map<String, Any>,
    val checksum: String,
    val signature: String,
    val serverTimestamp: Long
)

fun processServerData(document: SyncedDocument): Boolean {
    // Verify checksum
    val calculatedChecksum = calculateChecksum(document.data)
    if (calculatedChecksum != document.checksum) {
        Log.e("Sync", "Data integrity check failed - checksum mismatch")
        return false
    }

    // Verify server signature (for critical data)
    if (!verifyServerSignature(document)) {
        Log.e("Sync", "Data integrity check failed - invalid signature")
        return false
    }

    saveLocally(document)
    return true
}
```

---

### Phase 5: API Security

#### 5.1 API Authentication

**Analyze API authentication:**

```kotlin
// CRITICAL: No authentication
interface ApiService {
    @GET("users/{id}")
    suspend fun getUser(@Path("id") userId: String): User
    // No auth header!
}

// CRITICAL: API key in client code
@GET("data")
suspend fun getData(
    @Query("api_key") apiKey: String = BuildConfig.API_KEY  // Exposed in APK!
): Data

// SECURE: Bearer token authentication
interface ApiService {
    @GET("users/{id}")
    suspend fun getUser(
        @Path("id") userId: String,
        @Header("Authorization") auth: String
    ): User
}

// With interceptor
class AuthInterceptor(private val tokenProvider: TokenProvider) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val token = tokenProvider.getAccessToken()
            ?: throw AuthenticationException("Not authenticated")

        val request = chain.request().newBuilder()
            .addHeader("Authorization", "Bearer $token")
            .build()

        return chain.proceed(request)
    }
}
```

#### 5.2 API Input Validation

**Check for input validation on API calls:**

```kotlin
// VULNERABLE: Sending raw user input
@POST("search")
suspend fun search(@Body query: SearchQuery): List<Result>

fun performSearch(userInput: String) {
    api.search(SearchQuery(query = userInput))  // No sanitization!
}

// SECURE: Input validation before API call
fun performSearch(userInput: String) {
    val sanitizedQuery = userInput
        .take(100)  // Limit length
        .replace(Regex("[^a-zA-Z0-9\\s]"), "")  // Remove special chars

    if (sanitizedQuery.isBlank()) {
        return
    }

    api.search(SearchQuery(query = sanitizedQuery))
}
```

#### 5.3 API Response Validation

**Check for response validation:**

```kotlin
// VULNERABLE: Trusting API response completely
fun displayUserProfile(response: UserResponse) {
    // What if response contains malicious HTML/script?
    webView.loadData(response.bio, "text/html", null)  // XSS!
}

// VULNERABLE: No certificate pinning
val client = OkHttpClient.Builder().build()  // Accepts any certificate

// SECURE: Certificate pinning
val client = OkHttpClient.Builder()
    .certificatePinner(
        CertificatePinner.Builder()
            .add("api.yourapp.com", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
            .build()
    )
    .build()
```

---

### Phase 6: Cloud Storage Security

#### 6.1 Storage Rules Analysis

**Analyze Firebase Storage rules:**

```javascript
// CRITICAL: Open access
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read, write: if true;  // Anyone can read/write!
    }
  }
}

// VULNERABLE: Authentication only
match /uploads/{fileName} {
  allow read, write: if request.auth != null;
  // Any authenticated user can access any file!
}

// SECURE: User-scoped storage with validation
match /users/{userId}/uploads/{fileName} {
  allow read: if request.auth != null && request.auth.uid == userId;
  allow write: if request.auth != null
    && request.auth.uid == userId
    && request.resource.size < 10 * 1024 * 1024  // 10MB limit
    && request.resource.contentType.matches('image/.*');  // Images only
}
```

#### 6.2 Secure File Upload

**Check file upload security:**

```kotlin
// CRITICAL: No file validation
fun uploadFile(file: File) {
    val ref = storage.reference.child("uploads/${file.name}")
    ref.putFile(Uri.fromFile(file))  // Any file type!
}

// VULNERABLE: Trusting file extension
fun uploadImage(file: File) {
    if (file.name.endsWith(".jpg") || file.name.endsWith(".png")) {
        // Can be bypassed by renaming malicious file
        upload(file)
    }
}

// SECURE: Validate file content
fun uploadImage(uri: Uri): Result<String> {
    // Check file size
    val fileSize = contentResolver.openInputStream(uri)?.available() ?: 0
    if (fileSize > MAX_FILE_SIZE) {
        return Result.failure(FileTooLargeException())
    }

    // Validate MIME type from content, not extension
    val mimeType = contentResolver.getType(uri)
    if (mimeType !in ALLOWED_MIME_TYPES) {
        return Result.failure(InvalidFileTypeException())
    }

    // Validate image can be decoded
    val options = BitmapFactory.Options().apply { inJustDecodeBounds = true }
    contentResolver.openInputStream(uri)?.use {
        BitmapFactory.decodeStream(it, null, options)
    }
    if (options.outWidth <= 0 || options.outHeight <= 0) {
        return Result.failure(InvalidImageException())
    }

    // Generate safe filename
    val safeFileName = "${UUID.randomUUID()}.${getExtension(mimeType)}"
    val ref = storage.reference
        .child("users/${auth.currentUser!!.uid}/uploads/$safeFileName")

    return try {
        ref.putFile(uri).await()
        val url = ref.downloadUrl.await().toString()
        Result.success(url)
    } catch (e: Exception) {
        Result.failure(e)
    }
}

companion object {
    private val ALLOWED_MIME_TYPES = setOf("image/jpeg", "image/png", "image/webp")
    private const val MAX_FILE_SIZE = 10 * 1024 * 1024  // 10MB
}
```

---

### Phase 7: Sensitive Data Exposure

#### 7.1 Data Leakage in Cloud

**Check for sensitive data exposure:**

```kotlin
// CRITICAL: Logging cloud data
firestore.collection("users").document(userId).get()
    .addOnSuccessListener { doc ->
        Log.d("Firestore", "User data: ${doc.data}")  // Logs all user data!
    }

// CRITICAL: Returning sensitive fields
// Cloud Function returning too much data
export const getUser = functions.https.onCall(async (data, context) => {
  const user = await admin.firestore().collection('users').doc(data.userId).get();
  return user.data();  // Returns password hash, tokens, etc!
});

// SECURE: Filter sensitive fields
export const getUser = functions.https.onCall(async (data, context) => {
  const user = await admin.firestore().collection('users').doc(data.userId).get();
  const userData = user.data();

  // Return only safe fields
  return {
    id: user.id,
    name: userData?.name,
    photoUrl: userData?.photoUrl,
    createdAt: userData?.createdAt,
  };
});
```

#### 7.2 Client-Side Data Exposure

**Check for sensitive data in client:**

```kotlin
// CRITICAL: Storing cloud secrets in client
val FIREBASE_API_KEY = "AIza..."  // In client code, exposed in APK
val ADMIN_SECRET = "super_secret"  // Never put admin secrets in client!

// Check: What data is cached locally from cloud?
// Check: Is sensitive cloud data encrypted when cached?
// Check: Are cloud responses filtered before caching?
```

---

### Phase 8: Multi-Tenancy Security

#### 8.1 Tenant Isolation

**Check for tenant data isolation:**

```javascript
// CRITICAL: No tenant isolation
match /documents/{docId} {
  allow read, write: if request.auth != null;
  // All tenants can access all documents!
}

// VULNERABLE: Client-controlled tenant ID
match /tenants/{tenantId}/documents/{docId} {
  allow read, write: if request.auth != null
    && request.auth.token.tenantId == tenantId;
  // If tenantId in token can be manipulated...
}

// SECURE: Server-controlled tenant assignment
match /tenants/{tenantId}/documents/{docId} {
  allow read: if request.auth != null
    && exists(/databases/$(database)/documents/tenantMembers/$(request.auth.uid))
    && get(/databases/$(database)/documents/tenantMembers/$(request.auth.uid)).data.tenantId == tenantId;

  allow write: if request.auth != null
    && exists(/databases/$(database)/documents/tenantMembers/$(request.auth.uid))
    && get(/databases/$(database)/documents/tenantMembers/$(request.auth.uid)).data.tenantId == tenantId
    && get(/databases/$(database)/documents/tenantMembers/$(request.auth.uid)).data.role in ['admin', 'editor'];
}
```

---

### Phase 9: Findings Summary

**CHECKPOINT:** Present security audit findings summary.

```markdown
## Cloud Backend Security Audit Summary

### Overall Security Posture: [Critical/High/Medium/Low Risk]

### Cloud Services Security
| Service | Security Rules | Auth Required | Validation | Issues |
|---------|---------------|---------------|------------|--------|
| Firestore | [Configured/Open] | [Yes/No] | [Yes/No] | [Count] |
| Cloud Functions | [Auth checked] | [Yes/No] | [Yes/No] | [Count] |
| Cloud Storage | [Configured/Open] | [Yes/No] | [Type check] | [Count] |

### Critical Findings
1. **[Finding]** - [Brief description and impact]
2. **[Finding]** - [Brief description and impact]

### Data Sync Security
- Conflict Resolution: [Server/Client/None]
- Integrity Checks: [Yes/No]
- Offline Data Encrypted: [Yes/No]

**Shall I proceed with the detailed security report and remediation guidance?**
```

---

### Phase 10: Detailed Security Report

```markdown
# Cloud Backend Security Audit Report: [App Name]

## Executive Summary

### Security Score: [A/B/C/D/F]

| Dimension | Score | Assessment |
|-----------|-------|------------|
| Database Rules | [1-10] | [Details] |
| Cloud Functions | [1-10] | [Details] |
| Storage Security | [1-10] | [Details] |
| API Security | [1-10] | [Details] |
| Data Sync | [1-10] | [Details] |
| Data Integrity | [1-10] | [Details] |

### Risk Summary
| Risk | Severity | Likelihood | Impact |
|------|----------|------------|--------|
| Unauthorized Data Access | [Level] | [High/Med/Low] | [Description] |
| Data Tampering | [Level] | [High/Med/Low] | [Description] |
| Service Abuse | [Level] | [High/Med/Low] | [Description] |

---

## Detailed Findings

### Finding 1: [Title]
**Severity:** [Critical/High/Medium/Low]
**Service:** [Firestore/Functions/Storage/API]
**Location:** [file or rule location]

**Vulnerable Configuration:**
```javascript
[Code or rule snippet]
```

**Attack Scenario:**
1. [Step 1]
2. [Step 2]
3. [Impact]

**Proof of Concept:**
```bash
# Example attack command
curl -X POST https://firestore.googleapis.com/...
```

**Remediation:**
```javascript
[Secure configuration]
```

---

## Secure Configuration Examples

### Complete Firestore Security Rules

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Helper functions
    function isAuthenticated() {
      return request.auth != null;
    }

    function isOwner(userId) {
      return isAuthenticated() && request.auth.uid == userId;
    }

    function isAdmin() {
      return isAuthenticated() &&
        get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == 'admin';
    }

    function isValidEmail(email) {
      return email.matches('^[^@]+@[^@]+\\.[^@]+$');
    }

    function isValidString(value, minLen, maxLen) {
      return value is string && value.size() >= minLen && value.size() <= maxLen;
    }

    // Users collection
    match /users/{userId} {
      allow read: if isOwner(userId) || isAdmin();

      allow create: if isOwner(userId)
        && request.resource.data.keys().hasOnly(['email', 'name', 'photoUrl', 'createdAt'])
        && isValidEmail(request.resource.data.email)
        && isValidString(request.resource.data.name, 1, 100)
        && request.resource.data.createdAt == request.time;

      allow update: if isOwner(userId)
        && request.resource.data.keys().hasOnly(['email', 'name', 'photoUrl', 'updatedAt'])
        && isValidEmail(request.resource.data.email)
        && isValidString(request.resource.data.name, 1, 100)
        && request.resource.data.updatedAt == request.time;

      allow delete: if isOwner(userId) || isAdmin();
    }

    // User private data (not accessible by admin)
    match /users/{userId}/private/{docId} {
      allow read, write: if isOwner(userId);
    }

    // Posts collection
    match /posts/{postId} {
      allow read: if resource.data.visibility == 'public'
        || (isAuthenticated() && resource.data.authorId == request.auth.uid);

      allow create: if isAuthenticated()
        && request.resource.data.authorId == request.auth.uid
        && isValidString(request.resource.data.title, 1, 200)
        && isValidString(request.resource.data.content, 1, 10000)
        && request.resource.data.createdAt == request.time;

      allow update: if isAuthenticated()
        && resource.data.authorId == request.auth.uid
        && request.resource.data.authorId == resource.data.authorId
        && request.resource.data.createdAt == resource.data.createdAt
        && request.resource.data.updatedAt == request.time;

      allow delete: if isAuthenticated()
        && resource.data.authorId == request.auth.uid;
    }
  }
}
```

### Secure Cloud Function Template

```typescript
import * as functions from 'firebase-functions';
import * as admin from 'firebase-admin';
import * as yup from 'yup';

// Initialize with least privilege
admin.initializeApp();

// Rate limiting (use Redis/Firestore in production)
const rateLimitStore = new Map<string, { count: number; resetTime: number }>();

function checkRateLimit(
  uid: string,
  action: string,
  limit: number,
  windowMs: number
): boolean {
  const key = `${uid}:${action}`;
  const now = Date.now();
  const record = rateLimitStore.get(key);

  if (!record || now > record.resetTime) {
    rateLimitStore.set(key, { count: 1, resetTime: now + windowMs });
    return true;
  }

  if (record.count >= limit) {
    return false;
  }

  record.count++;
  return true;
}

// Validation schemas
const createPostSchema = yup.object({
  title: yup.string().min(1).max(200).required(),
  content: yup.string().min(1).max(10000).required(),
  visibility: yup.string().oneOf(['public', 'private']).required(),
}).noUnknown(true);

// Secure function implementation
export const createPost = functions.https.onCall(async (data, context) => {
  // 1. Authentication
  if (!context.auth) {
    throw new functions.https.HttpsError('unauthenticated', 'Authentication required');
  }

  const uid = context.auth.uid;

  // 2. Rate limiting
  if (!checkRateLimit(uid, 'createPost', 10, 60000)) {
    throw new functions.https.HttpsError('resource-exhausted', 'Rate limit exceeded');
  }

  // 3. Input validation
  let validatedData;
  try {
    validatedData = await createPostSchema.validate(data, { stripUnknown: true });
  } catch (error) {
    throw new functions.https.HttpsError('invalid-argument', 'Invalid input');
  }

  // 4. Business logic
  const postRef = admin.firestore().collection('posts').doc();

  await postRef.set({
    ...validatedData,
    id: postRef.id,
    authorId: uid,
    createdAt: admin.firestore.FieldValue.serverTimestamp(),
    updatedAt: admin.firestore.FieldValue.serverTimestamp(),
  });

  // 5. Audit logging
  await admin.firestore().collection('auditLogs').add({
    action: 'createPost',
    userId: uid,
    resourceId: postRef.id,
    timestamp: admin.firestore.FieldValue.serverTimestamp(),
    ip: context.rawRequest.ip,
  });

  return { id: postRef.id };
});
```
```

---

## Severity Ratings

- **Critical**: Direct data breach possible (open database rules, no auth on functions)
- **High**: Significant access control issues (authorization bypass, IDOR)
- **Medium**: Defense-in-depth issues (missing rate limiting, weak validation)
- **Low**: Hardening recommendations and best practice improvements

---

## Expected Output

1. **Service Inventory** - All cloud services and their security configuration
2. **Security Rules Audit** - Database and storage rules analysis
3. **Cloud Functions Review** - Authentication, validation, and abuse prevention
4. **Sync Security** - Data synchronization and integrity analysis
5. **Vulnerability Report** - All issues with attack scenarios
6. **Secure Templates** - Production-ready security rules and function templates

---

## Techniques Used

- **ST-01** (Clear Objective): Focused cloud security audit objective
- **ST-02** (Sequential Instructions): Phased service analysis process
- **RT-02** (Multi-Dimensional Analysis): Rules, functions, storage, sync, integrity
- **RT-05** (Evidence-Based Reasoning): Code examples and attack scenarios
- **DS-01** (Framework Application): Firebase Security Best Practices, OWASP
- **ST-03** (Output Format Templates): Structured report with security rules
- **OC-05** (Severity Classification): Critical/High/Medium/Low ratings
- **AG-05** (Concrete Deliverable Templates): Production-ready security configurations

---

## Related Prompts

- [android_local_data_security_audit.md](android_local_data_security_audit.md) - Local data protection
- [android_authentication_security_audit.md](android_authentication_security_audit.md) - Auth security
- [android_offline_first_sync.md](../implementation/android_offline_first_sync.md) - Sync implementation
- [android_firebase_integration.md](../implementation/android_firebase_integration.md) - Firebase setup

---

## Customization Guide

### For Firebase-Only Apps
- Focus on Firestore/RTDB security rules
- Review Firebase Functions auth patterns
- Check Firebase Storage rules
- Analyze Firebase Auth configuration

### For Custom Backend Apps
- Emphasize API security
- Review authentication mechanisms
- Check rate limiting implementation
- Analyze data validation on server

### For Real-Time Sync Apps
- Focus on conflict resolution security
- Review real-time listener scoping
- Check for data race conditions
- Analyze offline queue security

### For Multi-Tenant Apps
- Emphasize tenant isolation
- Review cross-tenant access controls
- Check for tenant ID manipulation
- Analyze shared resource security
