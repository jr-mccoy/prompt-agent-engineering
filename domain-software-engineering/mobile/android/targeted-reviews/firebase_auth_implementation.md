---
title: "Firebase Auth Implementation"
category: mobile-development
description: "Design and implement Firebase Authentication — provider selection matrix, account linking, custom claims RBAC, session management, re-authentication flows, and security hardening for Android apps"
techniques: [ST-01, ST-02, RT-02, CM-01, DS-06]
difficulty: intermediate
tags: [android, firebase, authentication, security, rbac, solo-developer]
updated: "2026-02-11"
---

# Firebase Auth Implementation

**Objective:** Design and implement a production-grade Firebase Authentication system for an Android app — covering provider selection and configuration, account linking strategy for multi-provider users, custom claims for role-based access control (RBAC), session management and token refresh, re-authentication flows for sensitive operations, and security hardening — producing an authentication architecture specification with Kotlin implementation code and TypeScript Cloud Functions for custom claims.

**When to Use:** Use this prompt when starting a new Firebase project that requires user authentication, when adding new auth providers to an existing app, when implementing role-based permissions, when users report being unexpectedly logged out or experiencing auth-related errors, or when preparing for a security audit of your auth implementation. Authentication is the foundation of your app's security — mistakes here compromise everything built on top.

**Important context:** Firebase Authentication handles the hard parts of auth (OAuth flows, token management, session persistence) but leaves critical decisions to the developer: which providers to support, how to handle account linking, how to implement authorization (not just authentication), and how to protect sensitive operations with re-authentication. This prompt covers the decisions Firebase docs leave to you.

---

## Context Gathering

Before designing the auth system, gather essential context:

1. **User Base:**
   - "Who are your users (consumers, business users, internal team, mixed)?"
   - "What auth methods do your users expect (email/password, Google, Apple, phone)?"
   - "Do you need anonymous authentication for try-before-signup flows?"
   - "What is your expected user count (now and in 12 months)?"

2. **Authorization Requirements:**
   - "Do you have different user roles (admin, editor, viewer, free, premium)?"
   - "Which features or data are restricted by role?"
   - "Do roles change frequently or are they set at registration?"
   - "Do you need organization/team-level permissions?"

3. **Security Requirements:**
   - "Are there sensitive operations that require re-authentication (delete account, change email, payment)?"
   - "Do you need multi-factor authentication?"
   - "Are there compliance requirements (HIPAA, SOC2, GDPR)?"
   - "Do you need audit logging for auth events?"

4. **Current State:**
   - "Is this a new project or adding auth to an existing app?"
   - "If existing, what auth issues have you encountered?"
   - "Are you using Firestore security rules that depend on auth state?"
   - "Do you have any Cloud Functions that verify auth?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY auth flow, you MUST:**

1. **Understand the difference between authentication and authorization** — Firebase Auth tells you WHO the user is. It does NOT tell you what they can do. Authorization (permissions, roles) must be implemented separately via custom claims and security rules.
2. **Plan for account linking from day one** — If a user signs up with email and later tries to sign in with Google using the same email, Firebase will throw an error by default. You must handle this.
3. **Never store roles in Firestore alone** — Firestore documents can be read by clients. Custom claims are embedded in the ID token and verified server-side. Use custom claims for authorization decisions.
4. **Set custom claims from server-side only** — Custom claims can only be set via the Admin SDK (Cloud Functions or a secure server). Never expose claim-setting logic to the client.
5. **Test token refresh behavior** — ID tokens expire after 1 hour. Custom claims only propagate after token refresh. Your app must handle this gracefully.

### False-Positive Prevention

- Do NOT recommend phone authentication as the primary method without noting its cost ($0.01-0.06 per verification) and usability limitations
- Do NOT flag anonymous authentication as a security risk if it is used intentionally for onboarding flows with proper data migration on sign-up
- Do NOT recommend storing user roles in Firestore documents as the primary authorization mechanism — custom claims exist for this purpose
- Do NOT assume `currentUser` is always non-null — it can be null during app startup, after sign-out, and after token expiration
- Do NOT flag re-authentication prompts as poor UX — they are a security requirement for sensitive operations
- DO verify that account linking is handled for every combination of supported providers
- DO check that custom claims are propagated and the token is refreshed before checking roles
- DO ensure security rules use `request.auth.token` for custom claims, not client-provided fields
- DO verify that error messages do not leak information (e.g., "no account with this email" reveals account existence)
- DO confirm that auth state listeners are properly cleaned up to prevent memory leaks

---

### Phase 1: Provider Selection

#### 1.1 Provider Selection Matrix

| Provider | Best For | Setup Complexity | Cost | User Friction |
|----------|---------|-----------------|------|---------------|
| **Email/Password** | Universal fallback, business apps | Low | Free | Medium (create password) |
| **Google Sign-In** | Android apps (pre-installed) | Medium (SHA-1 config) | Free | Low (one tap) |
| **Apple Sign-In** | iOS apps (required by App Store) | Medium (Apple Developer setup) | Free | Low |
| **Phone/SMS** | Markets where email is uncommon | Low | $0.01-0.06/SMS | Medium (wait for code) |
| **Anonymous** | Try-before-signup, guest access | None | Free | None (invisible) |
| **GitHub/Twitter** | Developer-focused apps | Medium (OAuth app setup) | Free | Low |
| **Custom (OIDC/SAML)** | Enterprise SSO integration | High | Free | Varies |

#### 1.2 Provider Decision Framework

```
Is your app consumer-facing?
├─ YES
│  ├─ Android-primary? → Google Sign-In + Email/Password
│  ├─ iOS-primary? → Apple Sign-In + Email/Password
│  ├─ Both platforms? → Google + Apple + Email/Password
│  └─ Need onboarding flow? → Add Anonymous auth
│
├─ Business/Enterprise?
│  ├─ Has corporate SSO? → Custom OIDC/SAML + Email fallback
│  └─ No SSO? → Email/Password + Google Sign-In
│
└─ Developer-focused?
   └─ GitHub + Google + Email/Password
```

#### 1.3 Provider Configuration Checklist

For each selected provider:

```
Provider: [Name]
Status: [Enabled in Firebase Console / Needs configuration]
SHA-1 fingerprint registered: [Yes / No / N/A]
OAuth client ID configured: [ID or N/A]
Redirect URI configured: [URI or N/A]
Tested on: [Emulator / Device / Both]
Error handling implemented: [Yes / No]
```

---

### Phase 2: Implementation

#### 2.1 Auth State Management

**Kotlin: Proper auth state observation with Compose:**

```kotlin
@HiltViewModel
class AuthViewModel @Inject constructor(
    private val auth: FirebaseAuth
) : ViewModel() {

    sealed class AuthState {
        object Loading : AuthState()
        object Unauthenticated : AuthState()
        data class Authenticated(
            val user: FirebaseUser,
            val roles: Set<String>
        ) : AuthState()
    }

    val authState: StateFlow<AuthState> = callbackFlow {
        val listener = FirebaseAuth.AuthStateListener { firebaseAuth ->
            val user = firebaseAuth.currentUser
            if (user == null) {
                trySend(AuthState.Unauthenticated)
            } else {
                // Force token refresh to get latest custom claims
                user.getIdToken(false).addOnSuccessListener { result ->
                    val roles = extractRoles(result.claims)
                    trySend(AuthState.Authenticated(user, roles))
                }.addOnFailureListener {
                    trySend(AuthState.Authenticated(user, emptySet()))
                }
            }
        }
        auth.addAuthStateListener(listener)
        awaitClose { auth.removeAuthStateListener(listener) }
    }.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), AuthState.Loading)

    private fun extractRoles(claims: Map<String, Any>): Set<String> {
        val roles = mutableSetOf<String>()
        if (claims["admin"] == true) roles.add("admin")
        if (claims["premium"] == true) roles.add("premium")
        // Add more roles as needed
        return roles
    }
}
```

#### 2.2 Google Sign-In Implementation

```kotlin
class SignInViewModel @Inject constructor(
    private val auth: FirebaseAuth,
    @ApplicationContext private val context: Context
) : ViewModel() {

    sealed class SignInResult {
        object Success : SignInResult()
        data class NeedsLinking(val email: String, val pendingCredential: AuthCredential) : SignInResult()
        data class Error(val message: String) : SignInResult()
    }

    private val _signInResult = MutableSharedFlow<SignInResult>()
    val signInResult: SharedFlow<SignInResult> = _signInResult.asSharedFlow()

    // Credential Manager approach (modern, recommended)
    suspend fun signInWithGoogle(credential: GetCredentialResponse) {
        try {
            val googleIdToken = when (val cred = credential.credential) {
                is CustomCredential -> {
                    if (cred.type == GoogleIdTokenCredential.TYPE_GOOGLE_ID_TOKEN_CREDENTIAL) {
                        GoogleIdTokenCredential.createFrom(cred.data).idToken
                    } else throw IllegalArgumentException("Unexpected credential type")
                }
                else -> throw IllegalArgumentException("Unexpected credential type")
            }

            val firebaseCredential = GoogleAuthProvider.getCredential(googleIdToken, null)
            val result = auth.signInWithCredential(firebaseCredential).await()

            if (result.additionalUserInfo?.isNewUser == true) {
                // First-time user: trigger welcome flow, set default claims
                createUserProfile(result.user!!)
            }

            _signInResult.emit(SignInResult.Success)
        } catch (e: FirebaseAuthUserCollisionException) {
            // Account exists with different provider — needs linking
            val email = e.email ?: "unknown"
            val pendingCredential = e.updatedCredential
            if (pendingCredential != null) {
                _signInResult.emit(SignInResult.NeedsLinking(email, pendingCredential))
            } else {
                _signInResult.emit(SignInResult.Error("Account exists with different sign-in method"))
            }
        } catch (e: Exception) {
            _signInResult.emit(SignInResult.Error(e.message ?: "Sign-in failed"))
        }
    }

    private suspend fun createUserProfile(user: FirebaseUser) {
        val profile = hashMapOf(
            "displayName" to (user.displayName ?: ""),
            "email" to (user.email ?: ""),
            "photoUrl" to (user.photoUrl?.toString() ?: ""),
            "createdAt" to FieldValue.serverTimestamp(),
            "provider" to user.providerData.map { it.providerId }
        )
        FirebaseFirestore.getInstance()
            .document("users/${user.uid}")
            .set(profile)
            .await()
    }
}
```

#### 2.3 Account Linking

```kotlin
// Handle account linking when user has multiple providers for same email
suspend fun linkAccounts(
    email: String,
    pendingCredential: AuthCredential
) {
    // Step 1: Find which providers are already linked to this email
    val providers = auth.fetchSignInMethodsForEmail(email).await()
        .signInMethods ?: emptyList()

    // Step 2: Sign in with existing provider
    // (You need to prompt the user to sign in with their existing method)
    // After successful sign-in with existing provider:

    // Step 3: Link the pending credential
    auth.currentUser?.linkWithCredential(pendingCredential)?.await()

    // Now the user can sign in with either provider
}

// Unlink a provider (e.g., user wants to remove Google Sign-In)
suspend fun unlinkProvider(providerId: String) {
    val user = auth.currentUser ?: throw IllegalStateException("Not signed in")

    // Safety: ensure user has at least one other sign-in method
    if (user.providerData.size <= 2) { // 1 = firebase, 1 = provider
        throw IllegalStateException("Cannot unlink last sign-in method")
    }

    user.unlink(providerId).await()
}
```

#### 2.4 Anonymous to Permanent Account Migration

```kotlin
// Convert anonymous user to permanent account (preserves UID and data)
suspend fun upgradeAnonymousAccount(credential: AuthCredential): Result<FirebaseUser> {
    val user = auth.currentUser
        ?: return Result.failure(IllegalStateException("Not signed in"))

    if (!user.isAnonymous) {
        return Result.failure(IllegalStateException("User is not anonymous"))
    }

    return try {
        val result = user.linkWithCredential(credential).await()
        // UID is preserved — all Firestore data keyed to this UID remains accessible
        Result.success(result.user!!)
    } catch (e: FirebaseAuthUserCollisionException) {
        // An account already exists with this credential
        // You need to decide: merge data or ask user to sign in with existing account
        Result.failure(e)
    }
}
```

---

### Phase 3: Custom Claims RBAC

#### 3.1 Role Architecture

Define roles and their permissions:

```
Role: admin
  Permissions: all (manage users, manage content, view analytics)
  Assignment: Manual by another admin via admin panel

Role: premium
  Permissions: premium features, ad-free, extended storage
  Assignment: Automatic on subscription verification

Role: editor
  Permissions: create/edit content, moderate comments
  Assignment: Manual by admin

Role: user (default)
  Permissions: read content, create own posts, basic features
  Assignment: Automatic on registration
```

#### 3.2 Cloud Function: Set Custom Claims

```typescript
// functions/src/auth/claims.ts
import { onCall, HttpsError } from "firebase-functions/v2/https";
import { onDocumentCreated } from "firebase-functions/v2/firestore";
import { getAuth } from "firebase-admin/auth";

// Set role via callable function (admin only)
export const setUserRole = onCall(
  { maxInstances: 5 },
  async (request) => {
    // Verify caller is an admin
    if (!request.auth?.token.admin) {
      throw new HttpsError(
        "permission-denied",
        "Only admins can set user roles"
      );
    }

    const { targetUid, role } = request.data;

    // Validate role
    const validRoles = ["admin", "premium", "editor", "user"];
    if (!validRoles.includes(role)) {
      throw new HttpsError("invalid-argument", `Invalid role: ${role}`);
    }

    // Safety: prevent removing your own admin role
    if (targetUid === request.auth.uid && role !== "admin") {
      throw new HttpsError(
        "failed-precondition",
        "Cannot remove your own admin role"
      );
    }

    // Build claims object
    const claims: Record<string, boolean> = {};
    claims[role] = true;
    if (role === "admin") {
      claims.editor = true;   // Admin inherits editor
      claims.premium = true;  // Admin inherits premium
    }

    await getAuth().setCustomUserClaims(targetUid, claims);

    // Log the change for audit trail
    const { getFirestore } = await import("firebase-admin/firestore");
    await getFirestore().collection("auditLog").add({
      action: "setUserRole",
      targetUid,
      role,
      performedBy: request.auth.uid,
      timestamp: new Date(),
    });

    return { success: true, role };
  }
);

// Auto-set default claims on user creation
export const onUserCreated = onDocumentCreated(
  "users/{userId}",
  async (event) => {
    const userId = event.params.userId;

    // Set default role
    await getAuth().setCustomUserClaims(userId, { user: true });

    console.log(`Default claims set for user ${userId}`);
  }
);

// Set premium on subscription verification
export const onSubscriptionVerified = onDocumentCreated(
  "subscriptions/{subscriptionId}",
  async (event) => {
    const data = event.data?.data();
    if (!data) return;

    const userId = data.userId;
    const currentUser = await getAuth().getUser(userId);
    const existingClaims = currentUser.customClaims || {};

    await getAuth().setCustomUserClaims(userId, {
      ...existingClaims,
      premium: true,
    });

    console.log(`Premium claims set for user ${userId}`);
  }
);
```

#### 3.3 Kotlin: Check Claims and Enforce Roles

```kotlin
// Force token refresh after role change to get new claims
suspend fun refreshUserClaims(): Map<String, Any> {
    val user = auth.currentUser ?: throw IllegalStateException("Not signed in")
    val tokenResult = user.getIdToken(true).await() // force refresh
    return tokenResult.claims
}

// Check role in app code
fun hasRole(claims: Map<String, Any>, role: String): Boolean {
    return claims[role] == true
}

// Composable guard for premium features
@Composable
fun PremiumGuard(
    authState: AuthViewModel.AuthState,
    content: @Composable () -> Unit
) {
    when {
        authState is AuthViewModel.AuthState.Authenticated &&
            authState.roles.contains("premium") -> {
            content()
        }
        authState is AuthViewModel.AuthState.Authenticated -> {
            UpgradePrompt()  // Show upgrade screen
        }
        else -> {
            SignInPrompt()   // Show sign-in screen
        }
    }
}
```

#### 3.4 Security Rules Using Custom Claims

```javascript
// firestore.rules
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Users can read their own profile, admins can read any
    match /users/{userId} {
      allow read: if request.auth.uid == userId
                  || request.auth.token.admin == true;
      allow write: if request.auth.uid == userId;
    }

    // Premium content restricted to premium users
    match /premiumContent/{docId} {
      allow read: if request.auth.token.premium == true
                  || request.auth.token.admin == true;
      allow write: if request.auth.token.admin == true
                   || request.auth.token.editor == true;
    }

    // Admin-only collection
    match /adminData/{docId} {
      allow read, write: if request.auth.token.admin == true;
    }

    // Audit log: write-only for functions, read for admins
    match /auditLog/{docId} {
      allow read: if request.auth.token.admin == true;
      allow write: if false; // Only Cloud Functions can write
    }
  }
}
```

---

### Phase 4: Security Hardening

#### 4.1 Re-Authentication for Sensitive Operations

```kotlin
// Re-authenticate before sensitive operations
suspend fun reauthenticateAndExecute(
    sensitiveAction: suspend () -> Unit
): Result<Unit> {
    val user = auth.currentUser
        ?: return Result.failure(IllegalStateException("Not signed in"))

    // Determine which provider to re-authenticate with
    val providerId = user.providerData
        .firstOrNull { it.providerId != "firebase" }
        ?.providerId

    return try {
        when (providerId) {
            GoogleAuthProvider.PROVIDER_ID -> {
                // Trigger Google Sign-In again for re-authentication
                // The caller must provide the credential from Google Sign-In
                throw ReauthenticationRequired(providerId)
            }
            EmailAuthProvider.PROVIDER_ID -> {
                // Prompt for password
                throw ReauthenticationRequired(providerId)
            }
            else -> {
                throw ReauthenticationRequired(providerId ?: "unknown")
            }
        }
    } catch (e: ReauthenticationRequired) {
        Result.failure(e)
    }
}

// After user provides credentials:
suspend fun completeReauthentication(
    credential: AuthCredential,
    sensitiveAction: suspend () -> Unit
): Result<Unit> {
    return try {
        auth.currentUser?.reauthenticate(credential)?.await()
        sensitiveAction()
        Result.success(Unit)
    } catch (e: FirebaseAuthInvalidCredentialsException) {
        Result.failure(IllegalArgumentException("Invalid credentials"))
    } catch (e: Exception) {
        Result.failure(e)
    }
}

class ReauthenticationRequired(val providerId: String) : Exception(
    "Re-authentication required with provider: $providerId"
)
```

#### 4.2 Sensitive Operations Requiring Re-Auth

| Operation | Why Re-Auth Required | Token Freshness |
|-----------|---------------------|-----------------|
| Delete account | Irreversible, Firebase requires it | < 5 minutes |
| Change email | Identity change | < 5 minutes |
| Change password | Credential change | < 5 minutes |
| Link new provider | Security-sensitive | < 5 minutes |
| Payment operations | Financial risk | App-defined |
| Export personal data | Privacy risk | App-defined |

#### 4.3 Session Management

```kotlin
// Token refresh handling
class TokenManager @Inject constructor(
    private val auth: FirebaseAuth
) {
    // ID tokens expire after 1 hour
    // Firebase SDK auto-refreshes, but you should handle edge cases

    suspend fun getValidToken(): String {
        val user = auth.currentUser
            ?: throw IllegalStateException("Not signed in")

        val tokenResult = user.getIdToken(false).await()

        // Check if token is about to expire (within 5 minutes)
        val expirationTime = tokenResult.expirationTimestamp
        val now = System.currentTimeMillis() / 1000
        if (expirationTime - now < 300) {
            // Force refresh
            return user.getIdToken(true).await().token
                ?: throw IllegalStateException("Failed to refresh token")
        }

        return tokenResult.token
            ?: throw IllegalStateException("No token available")
    }
}

// Sign out: clean up everything
suspend fun signOut() {
    // Clear any local caches
    FirebaseFirestore.getInstance().clearPersistence()

    // Sign out from Firebase
    auth.signOut()

    // Sign out from Google (if using Google Sign-In)
    // This prevents automatic re-sign-in
    val credentialManager = CredentialManager.create(context)
    credentialManager.clearCredentialState(ClearCredentialStateRequest())
}
```

#### 4.4 Security Checklist

- [ ] Error messages do not reveal whether an email is registered
- [ ] Password requirements enforced (Firebase default is 6 chars, consider custom validation)
- [ ] Account enumeration protection enabled in Firebase Console
- [ ] Authorized domains list is restricted (Firebase Console > Auth > Settings)
- [ ] Email verification is required before accessing sensitive features
- [ ] Custom claims are set server-side only (Cloud Functions)
- [ ] Security rules use `request.auth.token` for role checks, not client-provided data
- [ ] Re-authentication is required for sensitive operations
- [ ] Auth state listener is properly cleaned up to prevent memory leaks
- [ ] Anonymous user data is migrated on account upgrade (not orphaned)

---

### Phase 5: Testing

#### 5.1 Auth Testing Strategy

| Test Type | Tool | What to Test |
|-----------|------|-------------|
| Unit tests | JUnit + Mockk | ViewModel auth state logic, role extraction |
| Integration tests | Firebase Emulator Suite | Full auth flows, custom claims, security rules |
| E2E tests | Compose UI tests + Emulator | Sign-in/sign-out UI flows, error states |
| Security tests | Firebase Emulator + rules tests | Security rules with various auth states |

#### 5.2 Emulator-Based Auth Testing

```kotlin
// Configure Firebase Auth to use the emulator in debug builds
class FirebaseTestSetup {
    companion object {
        fun configureEmulators() {
            if (BuildConfig.DEBUG) {
                Firebase.auth.useEmulator("10.0.2.2", 9099)
                Firebase.firestore.useEmulator("10.0.2.2", 8080)
            }
        }
    }
}

// Test: Create user with custom claims in emulator
@Test
fun testPremiumUserAccess() = runTest {
    // The emulator allows setting claims directly via REST API
    // POST http://localhost:9099/identitytoolkit.googleapis.com/v1/accounts:signUp
    // Then set claims via Admin SDK in a test Cloud Function
}
```

#### 5.3 Security Rules Testing

```typescript
// tests/firestore.rules.test.ts
import { initializeTestEnvironment, assertFails, assertSucceeds } from
  "@firebase/rules-unit-testing";

describe("Firestore Security Rules", () => {
  let testEnv;

  beforeAll(async () => {
    testEnv = await initializeTestEnvironment({
      projectId: "test-project",
      firestore: { rules: readFileSync("firestore.rules", "utf8") },
    });
  });

  test("premium user can read premium content", async () => {
    const premiumUser = testEnv.authenticatedContext("user1", {
      premium: true,
    });
    const db = premiumUser.firestore();

    await assertSucceeds(
      db.collection("premiumContent").doc("doc1").get()
    );
  });

  test("free user cannot read premium content", async () => {
    const freeUser = testEnv.authenticatedContext("user2", {
      user: true,
    });
    const db = freeUser.firestore();

    await assertFails(
      db.collection("premiumContent").doc("doc1").get()
    );
  });

  test("non-admin cannot set user roles", async () => {
    const regularUser = testEnv.authenticatedContext("user3", {
      user: true,
    });
    const db = regularUser.firestore();

    await assertFails(
      db.collection("adminData").doc("roles").set({ admin: true })
    );
  });
});
```

---

## Verification Requirements

After completing the implementation, verify:

1. **Provider coverage** — Test sign-in with every configured provider on a real device (not just emulator).
2. **Account linking** — Test every combination of providers: sign up with A, try to sign in with B using the same email. Verify linking works.
3. **Custom claims propagation** — After setting a claim, verify the client receives it after `getIdToken(true)`. Check that security rules enforce the claim.
4. **Re-authentication** — Verify sensitive operations fail without re-authentication and succeed after.
5. **Session persistence** — Kill the app and reopen. Verify auth state is restored without requiring sign-in.
6. **Sign-out cleanup** — After sign-out, verify no cached data is accessible and Google Sign-In does not auto-restore the session.
7. **Error handling** — Disconnect the network and attempt sign-in. Verify graceful error messages.

---

## Expected Output

### Firebase Authentication Architecture

```markdown
# Firebase Auth Architecture: [App Name]

## Overview
- **Providers:** [List of enabled providers]
- **Roles:** [List of roles with descriptions]
- **Custom claims:** [List of claims]
- **Cloud Functions:** [Count] auth-related functions

## Provider Configuration
| Provider | Status | Configuration | Notes |
|----------|--------|--------------|-------|
| [Provider] | Enabled | [Details] | [Notes] |

## Role Matrix
| Role | Custom Claim | Permissions | Assignment Method |
|------|-------------|-------------|-------------------|
| [Role] | [Claim key] | [Permissions] | [How assigned] |

## Auth Flow Diagrams
[Flow for each provider: sign-in, sign-up, account linking]

## Security Rules Summary
[Which rules use which claims]

## Cloud Functions
| Function | Trigger | Purpose |
|----------|---------|---------|
| [Name] | [Trigger] | [Purpose] |

## Testing Checklist
- [ ] All providers tested on real device
- [ ] Account linking tested for all provider combinations
- [ ] Custom claims verified in security rules
- [ ] Re-authentication flows tested
- [ ] Offline behavior tested
- [ ] Sign-out cleanup verified

## Security Audit Results
| Check | Status | Notes |
|-------|--------|-------|
| [Check] | Pass/Fail | [Details] |
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on Firebase Authentication design and implementation, not general app security
- **ST-02** (Structured Sequential Instructions) — Phased approach: Provider Selection, Implementation, Custom Claims RBAC, Security Hardening, Testing
- **RT-02** (Multi-Dimensional Analysis) — Each auth decision analyzed across security, usability, cost, and implementation complexity
- **CM-01** (Explicit Context Framing) — Firebase Auth capabilities and limitations established upfront, distinguishing authentication from authorization
- **DS-06** (Prioritization Guidance) — Provider selection prioritized by user base characteristics, security measures prioritized by risk level

---

## Related Prompts

- `android_firebase_security_rules_audit.md` — Security rules that enforce the RBAC system designed here
- `firebase_cloud_functions_design.md` — Cloud Functions architecture including auth trigger functions
- `android_2fa_security_bypass_review.md` — Additional security layers beyond Firebase Auth
- `firestore_data_model_design.md` — Data model design that depends on auth structure for security rules
- `firebase_health_check.md` — Periodic review that includes auth configuration audit
- `firebase_security_rules_generator.md` — Generate security rules that use the custom claims defined here

---

## Customization Guide

- **For consumer social apps:** Prioritize Google and Apple Sign-In for frictionless onboarding. Add anonymous auth for browse-before-signup. Roles are typically simple (free/premium). Focus on account linking since users may sign in from different devices with different methods.
- **For B2B/SaaS apps:** Add custom OIDC/SAML for enterprise SSO. Implement organization-level roles (org admin, member, viewer). Custom claims should include `orgId` for tenant isolation. Security rules must scope all data access to the user's organization.
- **For healthcare apps:** Require email verification before any data access. Implement session timeout (sign out after inactivity). Add audit logging for every auth event. Consider HIPAA requirements for password complexity and session management.
- **For fintech apps:** Require re-authentication for all financial operations. Implement device binding (track and verify known devices). Consider phone verification as a second factor. Log all auth events for compliance audit trail.
- **For kids/family apps:** Implement COPPA-compliant auth (parental consent flows). Avoid email/password for child accounts. Consider parent-managed accounts with PIN-based access for children.
