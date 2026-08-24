---
title: "Firebase to Apple Services Migration"
category: mobile-development
description: "Migrate Firebase services to Apple equivalents covering Auth to Sign in with Apple, Firestore to CloudKit, Crashlytics to MetricKit, Remote Config to CloudKit KV, and FCM to APNs"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
difficulty: advanced
tags:
  - ios
  - android
  - migration
  - firebase
  - cloudkit
  - apns
  - sign-in-with-apple
  - crashlytics
updated: "2026-03-19"
---

# Firebase to Apple Services Migration

**Objective:** Map Firebase services used on Android to their Apple-native equivalents, providing side-by-side implementation patterns for authentication, cloud database, crash reporting, remote configuration, and push notifications. This enables teams to decide whether to keep Firebase on iOS or migrate to Apple-native services.

**When to Use:** When migrating from Android to iOS and evaluating whether to continue using Firebase (which works on iOS) or switch to Apple-native services. This prompt covers both options with trade-offs for each decision.

**Prompt Type:** Comprehensive (~350 lines)

## Context Gathering

1. Which Firebase services does the Android app use? (Auth, Firestore, Realtime DB, Crashlytics, Analytics, Remote Config, Cloud Messaging, Storage, Functions)
2. Is there a strong reason to move away from Firebase on iOS? (cost, privacy, Apple ecosystem preference)
3. Does the app use Firebase server-side? (Cloud Functions, Admin SDK)
4. What authentication methods are supported? (email/password, Google, Facebook, phone)
5. How much data is in Firestore? What is the query complexity?
6. Are Firebase Analytics custom events used for product decisions?

## Instructions

### CRITICAL: Verification Requirements

- Every Firebase service MUST be mapped to either an Apple equivalent OR continued Firebase iOS SDK usage
- Trade-offs MUST be documented for each migration decision
- Apple service implementations MUST follow current Apple SDK best practices
- Data migration strategies MUST be provided for services being switched

### False-Positive Prevention

- ❌ DO NOT assume Apple services are always better — Firebase often provides superior DX
- ✅ DO present both options (keep Firebase on iOS vs. migrate to Apple) with clear trade-offs
- ❌ DO NOT assume CloudKit can replace all Firestore functionality
- ✅ DO note CloudKit's limitations (no server-side triggers, different query model, Apple-only)
- ❌ DO NOT assume APNs alone replaces FCM's topic subscription and analytics
- ✅ DO recommend keeping FCM for cross-platform push if the backend already supports it
- ❌ DO NOT forget that Sign in with Apple is REQUIRED if the app offers any third-party login
- ✅ DO add Sign in with Apple alongside existing providers, even if keeping Firebase Auth

### Step 1: Service Mapping Overview

| Firebase Service | Apple Equivalent | Recommendation | Effort |
|-----------------|-----------------|----------------|--------|
| Firebase Auth | Sign in with Apple + AuthenticationServices | Keep Firebase + add Apple Sign-In | Low |
| Firestore | CloudKit | Keep Firebase unless Apple-only | High |
| Crashlytics | MetricKit + OSLog | Keep Crashlytics (superior) | Medium |
| Analytics | App Analytics (App Store Connect) | Keep Firebase Analytics | Low |
| Remote Config | CloudKit Key-Value | Keep Firebase or use custom | Medium |
| Cloud Messaging (FCM) | APNs | Keep FCM (wraps APNs) | Low |
| Cloud Storage | CloudKit Assets | Keep Firebase Storage | Medium |
| Cloud Functions | No equivalent | Keep Firebase Functions | N/A |

### Step 2: Authentication

**Kotlin (Firebase Auth — Android):**
```kotlin
class AuthRepository @Inject constructor(
    private val firebaseAuth: FirebaseAuth
) {
    val currentUser: Flow<FirebaseUser?> = callbackFlow {
        val listener = FirebaseAuth.AuthStateListener { auth ->
            trySend(auth.currentUser)
        }
        firebaseAuth.addAuthStateListener(listener)
        awaitClose { firebaseAuth.removeAuthStateListener(listener) }
    }

    suspend fun signInWithGoogle(idToken: String): Result<FirebaseUser> {
        return try {
            val credential = GoogleAuthProvider.getCredential(idToken, null)
            val result = firebaseAuth.signInWithCredential(credential).await()
            Result.success(result.user!!)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    suspend fun signInWithEmail(email: String, password: String): Result<FirebaseUser> {
        return try {
            val result = firebaseAuth.signInWithEmailAndPassword(email, password).await()
            Result.success(result.user!!)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}
```

**Swift (Firebase Auth on iOS + Sign in with Apple):**
```swift
import FirebaseAuth
import AuthenticationServices

class AuthRepository: ObservableObject {
    @Published var currentUser: FirebaseAuth.User?

    private var authListener: AuthStateDidChangeListenerHandle?

    init() {
        authListener = Auth.auth().addStateDidChangeListener { _, user in
            self.currentUser = user
        }
    }

    // Keep Firebase Auth — works on iOS
    func signInWithEmail(email: String, password: String) async throws -> User {
        let result = try await Auth.auth().signIn(withEmail: email, password: password)
        return result.user
    }

    // REQUIRED: Sign in with Apple (App Store mandate)
    func signInWithApple(authorization: ASAuthorization) async throws -> User {
        guard let appleCredential = authorization.credential
            as? ASAuthorizationAppleIDCredential,
              let identityToken = appleCredential.identityToken,
              let tokenString = String(data: identityToken, encoding: .utf8)
        else {
            throw AuthError.invalidCredential
        }

        let credential = OAuthProvider.appleCredential(
            withIDToken: tokenString,
            rawNonce: currentNonce,
            fullName: appleCredential.fullName
        )
        let result = try await Auth.auth().signIn(with: credential)
        return result.user
    }
}

// SwiftUI Sign in with Apple button
struct SignInWithAppleButton: View {
    @Environment(\.colorScheme) var colorScheme

    var body: some View {
        SignInWithAppleButton(.signIn) { request in
            request.requestedScopes = [.fullName, .email]
        } onCompletion: { result in
            switch result {
            case .success(let authorization):
                Task { try await authRepo.signInWithApple(authorization: authorization) }
            case .failure(let error):
                print("Sign in with Apple failed: \(error)")
            }
        }
        .signInWithAppleButtonStyle(
            colorScheme == .dark ? .white : .black
        )
        .frame(height: 50)
    }
}
```

### Step 3: Crash Reporting

**Kotlin (Crashlytics — Android):**
```kotlin
// Automatic crash reporting + custom logging
FirebaseCrashlytics.getInstance().apply {
    setUserId(userId)
    setCustomKey("subscription_tier", "premium")
    log("User opened settings screen")
}

// Non-fatal error reporting
try {
    riskyOperation()
} catch (e: Exception) {
    FirebaseCrashlytics.getInstance().recordException(e)
}
```

**Swift (Option A: Keep Crashlytics on iOS — Recommended):**
```swift
import FirebaseCrashlytics

// Identical API on iOS
Crashlytics.crashlytics().setUserID(userId)
Crashlytics.crashlytics().setCustomValue("premium", forKey: "subscription_tier")
Crashlytics.crashlytics().log("User opened settings screen")

// Non-fatal
do {
    try riskyOperation()
} catch {
    Crashlytics.crashlytics().record(error: error)
}
```

**Swift (Option B: Apple-native MetricKit):**
```swift
import MetricKit

class CrashReporter: NSObject, MXMetricManagerSubscriber {
    func startMonitoring() {
        MXMetricManager.shared.add(self)
    }

    func didReceive(_ payloads: [MXDiagnosticPayload]) {
        for payload in payloads {
            // Process crash reports, hang diagnostics, disk writes
            if let crashDiagnostics = payload.crashDiagnostics {
                for crash in crashDiagnostics {
                    processCrash(crash)
                }
            }
        }
    }

    func didReceive(_ payloads: [MXMetricPayload]) {
        for payload in payloads {
            // App launch time, memory, CPU usage metrics
            processMetrics(payload)
        }
    }
}
```

> **Trade-off:** Crashlytics provides real-time crash reporting with stack traces and custom keys. MetricKit delivers diagnostic payloads up to 24 hours later with less detail. For production apps, Crashlytics is strongly recommended.

### Step 4: Push Notifications (FCM to APNs)

**Kotlin (FCM — Android):**
```kotlin
class MyFirebaseMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(message: RemoteMessage) {
        message.notification?.let { notification ->
            showNotification(notification.title, notification.body)
        }
        message.data.let { data ->
            handleDataPayload(data)
        }
    }

    override fun onNewToken(token: String) {
        sendTokenToServer(token)
    }
}
```

**Swift (APNs via Firebase on iOS — Recommended):**
```swift
import FirebaseMessaging
import UserNotifications

class NotificationManager: NSObject, UNUserNotificationCenterDelegate,
    MessagingDelegate {

    func configure() {
        UNUserNotificationCenter.current().delegate = self
        Messaging.messaging().delegate = self
    }

    func requestPermission() async -> Bool {
        let settings = try? await UNUserNotificationCenter.current()
            .requestAuthorization(options: [.alert, .badge, .sound])
        await UIApplication.shared.registerForRemoteNotifications()
        return settings ?? false
    }

    // FCM token management
    func messaging(
        _ messaging: Messaging,
        didReceiveRegistrationToken fcmToken: String?
    ) {
        guard let token = fcmToken else { return }
        Task { await sendTokenToServer(token) }
    }

    // Foreground notification display
    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification
    ) async -> UNNotificationPresentationOptions {
        return [.banner, .badge, .sound]
    }

    // Notification tap handling
    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        didReceive response: UNNotificationResponse
    ) async {
        let userInfo = response.notification.request.content.userInfo
        handleDeepLink(from: userInfo)
    }
}
```

### Step 5: Remote Config

**Kotlin (Firebase Remote Config):**
```kotlin
val remoteConfig = Firebase.remoteConfig
remoteConfig.setDefaultsAsync(R.xml.remote_config_defaults)

suspend fun fetchConfig() {
    remoteConfig.fetchAndActivate().await()
}

val featureEnabled: Boolean
    get() = remoteConfig.getBoolean("new_feature_enabled")
```

**Swift (Firebase Remote Config on iOS):**
```swift
import FirebaseRemoteConfig

class FeatureFlags {
    private let remoteConfig = RemoteConfig.remoteConfig()

    init() {
        remoteConfig.setDefaults(fromPlist: "RemoteConfigDefaults")
    }

    func fetch() async throws {
        let status = try await remoteConfig.fetchAndActivate()
        print("Config fetch status: \(status)")
    }

    var isNewFeatureEnabled: Bool {
        remoteConfig.configValue(forKey: "new_feature_enabled").boolValue
    }
}
```

## Expected Output

1. **Service-by-service decision matrix** (keep Firebase vs. migrate to Apple)
2. **Implementation code** for each migrated or continued service
3. **Data migration plan** for services being switched
4. **Trade-off documentation** for each decision

## Example Interaction

**User:** Our Android app uses Firebase Auth (Google + email), Firestore, Crashlytics, FCM, and Remote Config. Should we keep Firebase on iOS or go native?

**Assistant:**

| Service | Decision | Rationale |
|---------|----------|-----------|
| Auth | **Keep Firebase + add Apple Sign-In** | Firebase Auth works on iOS; Apple Sign-In is mandatory |
| Firestore | **Keep Firebase** | CloudKit lacks server triggers and cross-platform sync |
| Crashlytics | **Keep Firebase** | Superior real-time reporting vs MetricKit |
| FCM | **Keep Firebase** | FCM wraps APNs and shares backend infrastructure |
| Remote Config | **Keep Firebase** | No Apple equivalent with the same feature set |

**Bottom line:** Keep Firebase on iOS for all services. Add Sign in with Apple as a required authentication method.

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | Service-by-service migration analysis |
| **ST-02: Systematic Analysis Framework** | Decision matrix with trade-offs |
| **RT-02: Contextual Reference Integration** | Firebase iOS SDK and Apple framework docs |
| **DS-02: Output Specification Framework** | Decision matrix, implementation code, migration plan |

## Related Prompts

- `migration_platform_feature_mapping.md` — Broader platform API mapping
- `migration_play_billing_to_storekit.md` — In-app purchase migration
- `migration_android_to_ios_strategy.md` — Overall migration strategy

## Customization Guide

- **Privacy-First:** If privacy requirements mandate Apple-only services, migrate Auth to Apple Sign-In only, Firestore to CloudKit, and analytics to App Analytics.
- **Supabase/Appwrite:** If moving away from Firebase entirely, consider open-source BaaS alternatives that work on both platforms.
- **Hybrid:** Keep Firebase for backend services (Auth, Firestore, Functions) and use Apple services for device-level features (MetricKit for metrics, APNs for local notifications).
- **No Firebase:** If the iOS app must have zero Firebase dependencies, provide a complete Apple-native service mapping.
