---
title: "Android Firebase Integration"
category: mobile-development
description: ""
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android Firebase Integration

**Objective:** Integrate Firebase services (Authentication, Firestore, Cloud Messaging, Analytics, Crashlytics) into an Android application with proper initialization, security rules, and clean architecture patterns.

**When to Use:** Use this prompt when adding Firebase services to an Android app for authentication, real-time database, push notifications, analytics, or crash reporting. Best used when setting up a new project or adding Firebase to an existing app.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

Before integrating Firebase, gather essential context:

1. **Services Needed:**
   - "Which Firebase services do you need (Auth, Firestore, FCM, Analytics, Crashlytics)?"
   - "Do you have a Firebase project already created?"
   - "Is the `google-services.json` file in the project?"

2. **Authentication:**
   - "What auth providers are needed (email/password, Google, Apple, phone)?"
   - "Do you need anonymous authentication?"

3. **Architecture:**
   - "How should Firebase integrate with your existing architecture?"
   - "Do you need real-time listeners or one-time fetches?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing Firebase setup** - Check for existing Firebase initialization, services, and configuration in the codebase.
2. **Verify Firebase project configuration** - Confirm google-services.json is configured and Firebase services are enabled in console.
3. **Follow security best practices** - Configure proper security rules; don't leave databases open.
4. **Provide specific, working code** - All code samples MUST include file paths (e.g., `data/firebase/FirestoreUserRepository.kt`) and be copy-paste ready.
5. **Include proper error handling** - Handle Firebase exceptions appropriately with user feedback.

**Security rules are critical.** Never deploy with open read/write access to Firebase databases.

### Quality Requirements

- ❌ Do NOT leave security rules open (read/write: true) in production
- ❌ Do NOT generate Firebase code without proper offline persistence configuration
- ❌ Do NOT skip error handling for network failures
- ❌ Do NOT mix multiple Firebase project configurations without clear separation
- ✅ DO provide appropriate security rules alongside code
- ✅ DO configure offline persistence and caching properly
- ✅ DO include proper Auth state handling
- ✅ DO specify exact file paths for all code changes

---

### Phase 1: Firebase Setup

#### 1.1 Dependencies

```kotlin
// build.gradle.kts (Project)
plugins {
    id("com.google.gms.google-services") version "4.4.0" apply false
    id("com.google.firebase.crashlytics") version "2.9.9" apply false
}

// build.gradle.kts (App)
plugins {
    id("com.google.gms.google-services")
    id("com.google.firebase.crashlytics")
}

dependencies {
    // Firebase BoM
    implementation(platform("com.google.firebase:firebase-bom:32.7.0"))

    // Core services
    implementation("com.google.firebase:firebase-analytics-ktx")
    implementation("com.google.firebase:firebase-crashlytics-ktx")

    // Authentication
    implementation("com.google.firebase:firebase-auth-ktx")

    // Firestore
    implementation("com.google.firebase:firebase-firestore-ktx")

    // Cloud Messaging
    implementation("com.google.firebase:firebase-messaging-ktx")
}
```

#### 1.2 Initialization

```kotlin
@HiltAndroidApp
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Firebase initializes automatically via ContentProvider
        // Configure Crashlytics
        FirebaseCrashlytics.getInstance().apply {
            setCrashlyticsCollectionEnabled(!BuildConfig.DEBUG)
        }
    }
}
```

---

### Phase 2: Authentication

#### 2.1 Auth Repository

```kotlin
interface AuthRepository {
    val currentUser: Flow<FirebaseUser?>
    val isAuthenticated: Boolean

    suspend fun signInWithEmail(email: String, password: String): Result<FirebaseUser>
    suspend fun signUpWithEmail(email: String, password: String): Result<FirebaseUser>
    suspend fun signInWithGoogle(idToken: String): Result<FirebaseUser>
    suspend fun signOut()
    suspend fun resetPassword(email: String): Result<Unit>
}

class FirebaseAuthRepository @Inject constructor(
    private val auth: FirebaseAuth
) : AuthRepository {

    override val currentUser: Flow<FirebaseUser?> = callbackFlow {
        val listener = FirebaseAuth.AuthStateListener { auth ->
            trySend(auth.currentUser)
        }
        auth.addAuthStateListener(listener)
        awaitClose { auth.removeAuthStateListener(listener) }
    }

    override val isAuthenticated: Boolean
        get() = auth.currentUser != null

    override suspend fun signInWithEmail(email: String, password: String): Result<FirebaseUser> =
        runCatching {
            auth.signInWithEmailAndPassword(email, password).await().user
                ?: throw Exception("Sign in failed")
        }

    override suspend fun signUpWithEmail(email: String, password: String): Result<FirebaseUser> =
        runCatching {
            auth.createUserWithEmailAndPassword(email, password).await().user
                ?: throw Exception("Sign up failed")
        }

    override suspend fun signInWithGoogle(idToken: String): Result<FirebaseUser> =
        runCatching {
            val credential = GoogleAuthProvider.getCredential(idToken, null)
            auth.signInWithCredential(credential).await().user
                ?: throw Exception("Google sign in failed")
        }

    override suspend fun signOut() {
        auth.signOut()
    }

    override suspend fun resetPassword(email: String): Result<Unit> =
        runCatching {
            auth.sendPasswordResetEmail(email).await()
        }
}
```

#### 2.2 DI Module

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object FirebaseModule {

    @Provides
    @Singleton
    fun provideFirebaseAuth(): FirebaseAuth = Firebase.auth

    @Provides
    @Singleton
    fun provideFirestore(): FirebaseFirestore = Firebase.firestore

    @Provides
    @Singleton
    fun provideAuthRepository(auth: FirebaseAuth): AuthRepository =
        FirebaseAuthRepository(auth)
}
```

---

### Phase 3: Firestore

#### 3.1 Firestore Data Source

```kotlin
class FirestoreDataSource @Inject constructor(
    private val firestore: FirebaseFirestore
) {
    private val itemsCollection = firestore.collection("items")

    fun observeItems(userId: String): Flow<List<ItemDto>> = callbackFlow {
        val subscription = itemsCollection
            .whereEqualTo("userId", userId)
            .orderBy("createdAt", Query.Direction.DESCENDING)
            .addSnapshotListener { snapshot, error ->
                if (error != null) {
                    close(error)
                    return@addSnapshotListener
                }

                val items = snapshot?.documents?.mapNotNull { doc ->
                    doc.toObject(ItemDto::class.java)?.copy(id = doc.id)
                } ?: emptyList()

                trySend(items)
            }

        awaitClose { subscription.remove() }
    }

    suspend fun getItem(id: String): ItemDto? =
        itemsCollection.document(id).get().await()
            .toObject(ItemDto::class.java)

    suspend fun createItem(item: ItemDto): String {
        val docRef = itemsCollection.add(item.toMap()).await()
        return docRef.id
    }

    suspend fun updateItem(id: String, updates: Map<String, Any>) {
        itemsCollection.document(id).update(updates).await()
    }

    suspend fun deleteItem(id: String) {
        itemsCollection.document(id).delete().await()
    }
}

@Keep
data class ItemDto(
    val id: String = "",
    val userId: String = "",
    val title: String = "",
    val content: String = "",
    @ServerTimestamp
    val createdAt: Timestamp? = null,
    @ServerTimestamp
    val updatedAt: Timestamp? = null
) {
    fun toMap(): Map<String, Any?> = mapOf(
        "userId" to userId,
        "title" to title,
        "content" to content,
        "createdAt" to FieldValue.serverTimestamp(),
        "updatedAt" to FieldValue.serverTimestamp()
    )
}
```

---

### Phase 4: Cloud Messaging

#### 4.1 FCM Service

```kotlin
class AppFirebaseMessagingService : FirebaseMessagingService() {

    override fun onNewToken(token: String) {
        // Send token to your server
        CoroutineScope(Dispatchers.IO).launch {
            sendTokenToServer(token)
        }
    }

    override fun onMessageReceived(message: RemoteMessage) {
        // Handle notification
        message.notification?.let { notification ->
            showNotification(notification.title, notification.body)
        }

        // Handle data payload
        message.data.isNotEmpty().let {
            handleDataMessage(message.data)
        }
    }

    private fun showNotification(title: String?, body: String?) {
        val notificationManager = getSystemService(NotificationManager::class.java)

        val notification = NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle(title)
            .setContentText(body)
            .setSmallIcon(R.drawable.ic_notification)
            .setAutoCancel(true)
            .build()

        notificationManager.notify(System.currentTimeMillis().toInt(), notification)
    }

    private suspend fun sendTokenToServer(token: String) {
        // Implement server registration
    }

    private fun handleDataMessage(data: Map<String, String>) {
        // Handle custom data payloads
    }

    companion object {
        const val CHANNEL_ID = "default_channel"
    }
}

// AndroidManifest.xml
<service
    android:name=".AppFirebaseMessagingService"
    android:exported="false">
    <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
    </intent-filter>
</service>
```

---

## Expected Output

### File Structure

```
firebase/
├── auth/
│   └── FirebaseAuthRepository.kt
├── firestore/
│   └── FirestoreDataSource.kt
├── messaging/
│   └── AppFirebaseMessagingService.kt
├── analytics/
│   └── AnalyticsTracker.kt
└── di/
    └── FirebaseModule.kt
```

### Implementation Checklist

- [ ] Firebase project configured with google-services.json
- [ ] Firebase BoM for version management
- [ ] Authentication with required providers
- [ ] Firestore data source with real-time listeners
- [ ] Cloud Messaging service for push notifications
- [ ] Analytics tracking for key events
- [ ] Crashlytics for crash reporting
- [ ] Security rules configured in Firebase Console

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for Firebase integration
- **ST-02** (Sequential Instructions): Service-by-service setup
- **RT-04** (Best Practice Review): Firebase SDK best practices
- **ST-03** (Output Format Templates): Repository and service templates

---

## Related Prompts

- [android_dependency_injection.md](android_dependency_injection.md) - DI for Firebase
- [android_data_layer_implementation.md](android_data_layer_implementation.md) - Integrate with data layer
- [android_background_work.md](android_background_work.md) - Background sync with Firebase

---

## Customization Guide

### For Offline Persistence

Enable Firestore offline:
```kotlin
Firebase.firestore.firestoreSettings = firestoreSettings {
    isPersistenceEnabled = true
    cacheSizeBytes = FirebaseFirestoreSettings.CACHE_SIZE_UNLIMITED
}
```

### For Multiple Auth Providers

Add provider-specific sign-in:
```kotlin
// Apple Sign-In
val provider = OAuthProvider.newBuilder("apple.com")
auth.startActivityForSignInWithProvider(activity, provider.build())

// Phone Auth
auth.verifyPhoneNumber(phoneNumber, timeout, activity, callbacks)
```

### For Custom Analytics

Track custom events:
```kotlin
class AnalyticsTracker @Inject constructor() {
    private val analytics = Firebase.analytics

    fun trackScreenView(screenName: String) {
        analytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW) {
            param(FirebaseAnalytics.Param.SCREEN_NAME, screenName)
        }
    }

    fun trackPurchase(itemId: String, price: Double) {
        analytics.logEvent(FirebaseAnalytics.Event.PURCHASE) {
            param(FirebaseAnalytics.Param.ITEM_ID, itemId)
            param(FirebaseAnalytics.Param.VALUE, price)
        }
    }
}
```
