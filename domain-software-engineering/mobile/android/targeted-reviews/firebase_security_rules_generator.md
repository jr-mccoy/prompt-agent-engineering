---
title: "Firebase Security Rules Generator"
category: mobile-development
description: "Generate production-grade Firestore security rules from a data model description — role-based access control via custom claims, field-level validation, rate limiting patterns, document-level permissions, and helper functions"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - android
  - firebase
  - firestore
  - security-rules
  - rbac
  - authorization
  - solo-developer
updated: "2026-02-11"
---

# Firebase Security Rules Generator

**Objective:** Generate production-grade Firestore security rules from a data model description — covering role-based access control via custom claims (admin/editor/viewer), field-level validation, rate limiting patterns, document-level ownership permissions, and reusable helper functions — producing a complete `firestore.rules` file that protects data without blocking legitimate access.

**When to Use:** Use this prompt when starting a new Firebase project and need security rules beyond the default locked-down or wide-open modes, when adding new collections that need access control, when implementing role-based permissions for a team-facing feature, or when auditing existing rules that are either too permissive or too restrictive. Critical because insecure rules are the #1 cause of data breaches in Firebase apps, and overly strict rules are the #1 cause of "it works in emulator but not production" bugs.

**Important context:** Firestore security rules are the ONLY server-side authorization layer for direct client access. Unlike traditional backends where you control every endpoint, Firestore clients talk directly to the database. If your rules are wrong, any user with your Firebase config (which is public) can read or write any data. There is no "fix it later" — rules must be correct from day one.

---

## Context Gathering

Before generating security rules, gather essential context:

1. **Data Model:**
   - "What collections and subcollections does your Firestore database have?"
   - "What is the document ID strategy for each collection (auto-ID, user UID, custom)?"
   - "Which fields are required vs optional in each document?"
   - "What are the data types and valid ranges for each field?"

2. **Access Patterns:**
   - "Who can read each collection (anyone, authenticated users, owners only, admins)?"
   - "Who can create, update, and delete documents in each collection?"
   - "Are there fields that should never be writable by the client (server-only fields)?"
   - "Do you need role-based access (admin, editor, viewer)?"

3. **User Roles:**
   - "What roles exist in your app (e.g., admin, editor, viewer, free, premium)?"
   - "How are roles assigned (custom claims, Firestore document, both)?"
   - "Are there operations that only admins can perform?"
   - "Do roles ever need to be checked across collections (e.g., organization membership)?"

4. **Existing Rules:**
   - "Do you have existing security rules? Are they working correctly?"
   - "Have you experienced any 'permission denied' errors in production?"
   - "Are you currently using `allow read, write: if true` anywhere (wide-open rules)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY security rules, you MUST:**

1. **Map every collection's access pattern** — For each collection, explicitly define who can read, create, update, and delete. Never leave a collection without rules.
2. **Verify custom claims are set server-side** — Custom claims MUST be set via Admin SDK (Cloud Functions), never from the client. If the developer plans to set claims from the client, stop and redesign.
3. **Test both the allow and deny cases** — For every rule, consider both "does a legitimate user get access?" and "is a malicious user blocked?" A rule that blocks everyone is as bad as one that allows everyone.
4. **Check for write validation** — Every field that accepts user input must have type and range validation in the rules. Don't trust client-side validation alone.
5. **Ensure no wide-open rules remain** — Search for `allow read, write: if true` or `allow read, write: if request.auth != null` without further conditions. These are almost always too permissive.

**Finding that a collection needs no custom rules (e.g., it's only accessed via Cloud Functions with Admin SDK) is an acceptable outcome.**

### False-Positive Prevention

- ❌ Do NOT generate overly permissive rules just to "make it work" — debug the real access issue instead
- ❌ Do NOT use `allow read, write: if true` in any production rule, ever
- ❌ Do NOT validate field types only on create but skip on update — both need validation
- ❌ Do NOT assume `request.auth != null` is sufficient access control — it only means the user is logged in, not that they have permission
- ❌ Do NOT put business logic in security rules that belongs in Cloud Functions — rules should be simple and fast
- ✅ DO separate read/write into granular operations (get, list, create, update, delete)
- ✅ DO use helper functions to keep rules DRY and readable
- ✅ DO validate all user-writable fields for type, length, and allowed values
- ✅ DO test rules with the Firebase Emulator Suite before deploying
- ✅ DO include comments explaining the "why" behind each rule

---

### Phase 1: Role Architecture

#### 1.1 Custom Claims vs Firestore Document Roles

| Approach | How It Works | Pros | Cons | Best For |
|----------|-------------|------|------|----------|
| **Custom Claims** | Set via Admin SDK, stored in auth token | Fast (no extra reads), checked in rules natively | Requires Cloud Function to set, 1000-byte limit, propagation delay | Primary role (admin/editor/viewer) |
| **Firestore Document** | Role stored in `users/{uid}.role` | Easy to update, no size limit, queryable | Requires document read in every rule check, costs reads | Secondary roles, org membership |
| **Hybrid** | Claims for primary role, Firestore for granular permissions | Best of both, flexible | More complex to maintain | Apps with organizations/teams |

**Recommendation for solo developers:** Start with custom claims for the primary role. Add Firestore-based roles only when you need organization-level or resource-level permissions.

#### 1.2 Setting Custom Claims (Cloud Function)

```typescript
import { onCall, HttpsError } from "firebase-functions/v2/https";
import { getAuth } from "firebase-admin/auth";

// Only callable by existing admins
export const setUserRole = onCall(async (request) => {
  // Verify the caller is an admin
  if (!request.auth?.token?.role || request.auth.token.role !== "admin") {
    throw new HttpsError("permission-denied", "Only admins can set roles");
  }

  const { targetUid, role } = request.data;

  // Validate role
  const validRoles = ["admin", "editor", "viewer"];
  if (!validRoles.includes(role)) {
    throw new HttpsError("invalid-argument", `Invalid role: ${role}`);
  }

  // Set custom claim
  await getAuth().setCustomUserClaims(targetUid, { role });

  // Also update Firestore for queryability
  await getFirestore().doc(`users/${targetUid}`).update({ role });

  return { success: true, uid: targetUid, role };
});

// Bootstrap: Set first admin (run once, then disable or protect)
export const bootstrapAdmin = onCall(async (request) => {
  if (!request.auth) {
    throw new HttpsError("unauthenticated", "Must be logged in");
  }

  // Check if any admin exists
  const admins = await getFirestore()
    .collection("users")
    .where("role", "==", "admin")
    .limit(1)
    .get();

  if (!admins.empty) {
    throw new HttpsError("already-exists", "Admin already exists");
  }

  // First user becomes admin
  await getAuth().setCustomUserClaims(request.auth.uid, { role: "admin" });
  await getFirestore().doc(`users/${request.auth.uid}`).update({ role: "admin" });

  return { success: true };
});
```

#### 1.3 Role Permission Matrix

Define what each role can do before writing rules:

```markdown
| Operation | Admin | Editor | Viewer | Owner | Unauthenticated |
|-----------|-------|--------|--------|-------|-----------------|
| Read own profile | ✅ | ✅ | ✅ | ✅ | ❌ |
| Read any profile | ✅ | ❌ | ❌ | — | ❌ |
| Update own profile | ✅ | ✅ | ✅ | ✅ | ❌ |
| Create content | ✅ | ✅ | ❌ | — | ❌ |
| Update own content | ✅ | ✅ | ❌ | ✅ | ❌ |
| Update any content | ✅ | ❌ | ❌ | — | ❌ |
| Delete own content | ✅ | ✅ | ❌ | ✅ | ❌ |
| Delete any content | ✅ | ❌ | ❌ | — | ❌ |
| Manage users | ✅ | ❌ | ❌ | — | ❌ |
| View analytics | ✅ | ✅ | ❌ | — | ❌ |
```

---

### Phase 2: Helper Functions Library

Build reusable helper functions that keep your rules clean and maintainable.

#### 2.1 Authentication and Role Helpers

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // ──────────────────────────────────────
    // HELPER FUNCTIONS
    // ──────────────────────────────────────

    // Authentication checks
    function isAuthenticated() {
      return request.auth != null;
    }

    function isOwner(userId) {
      return isAuthenticated() && request.auth.uid == userId;
    }

    // Role checks (via custom claims)
    function hasRole(role) {
      return isAuthenticated() && request.auth.token.role == role;
    }

    function isAdmin() {
      return hasRole("admin");
    }

    function isEditor() {
      return hasRole("editor");
    }

    function isViewer() {
      return hasRole("viewer");
    }

    function isEditorOrAbove() {
      return isAdmin() || isEditor();
    }

    function isViewerOrAbove() {
      return isAdmin() || isEditor() || isViewer();
    }

    // Document ownership check
    function isDocOwner() {
      return isAuthenticated() && resource.data.ownerId == request.auth.uid;
    }

    function willBeDocOwner() {
      return isAuthenticated() && request.resource.data.ownerId == request.auth.uid;
    }
```

#### 2.2 Field Validation Helpers

```javascript
    // ──────────────────────────────────────
    // FIELD VALIDATION HELPERS
    // ──────────────────────────────────────

    // Check if the incoming data has exactly the expected fields
    function hasAllFields(fields) {
      return request.resource.data.keys().hasAll(fields);
    }

    function hasOnlyFields(fields) {
      return request.resource.data.keys().hasOnly(fields);
    }

    // Type validators
    function isString(field) {
      return request.resource.data[field] is string;
    }

    function isNumber(field) {
      return request.resource.data[field] is number;
    }

    function isBool(field) {
      return request.resource.data[field] is bool;
    }

    function isTimestamp(field) {
      return request.resource.data[field] is timestamp;
    }

    function isList(field) {
      return request.resource.data[field] is list;
    }

    function isMap(field) {
      return request.resource.data[field] is map;
    }

    // String validators
    function isNonEmptyString(field) {
      return isString(field) && request.resource.data[field].size() > 0;
    }

    function isStringWithMaxLength(field, maxLen) {
      return isString(field) && request.resource.data[field].size() <= maxLen;
    }

    function isStringInRange(field, minLen, maxLen) {
      return isString(field)
        && request.resource.data[field].size() >= minLen
        && request.resource.data[field].size() <= maxLen;
    }

    // List validators
    function isListWithMaxSize(field, maxSize) {
      return isList(field) && request.resource.data[field].size() <= maxSize;
    }

    // Enum validator
    function isOneOf(field, allowedValues) {
      return request.resource.data[field] in allowedValues;
    }

    // Timestamp validators
    function isServerTimestamp(field) {
      return request.resource.data[field] == request.time;
    }

    // Check that specific fields were not changed on update
    function fieldNotChanged(field) {
      return request.resource.data[field] == resource.data[field];
    }
```

#### 2.3 Rate Limiting Helpers

```javascript
    // ──────────────────────────────────────
    // RATE LIMITING HELPERS
    // ──────────────────────────────────────

    // Simple rate limit: check if a document was created recently
    // Requires a "lastWriteAt" timestamp field on the document
    function notRateLimited(minSeconds) {
      return !exists(/databases/$(database)/documents/rateLimits/$(request.auth.uid))
        || get(/databases/$(database)/documents/rateLimits/$(request.auth.uid))
            .data.lastWriteAt < request.time - duration.value(minSeconds, 's');
    }

    // Check document creation count (requires a counter document)
    function underDailyLimit(collection, maxCount) {
      return !exists(/databases/$(database)/documents/dailyCounts/$(request.auth.uid + '_' + collection))
        || get(/databases/$(database)/documents/dailyCounts/$(request.auth.uid + '_' + collection))
            .data.count < maxCount;
    }
```

---

### Phase 3: Collection Rules Patterns

#### 3.1 User Profiles Collection

```javascript
    // ──────────────────────────────────────
    // COLLECTION RULES
    // ──────────────────────────────────────

    // USERS COLLECTION
    // Document ID = Firebase Auth UID
    // Roles: owner can read/update own profile, admin can read/update any profile
    match /users/{userId} {
      // Anyone authenticated can read basic profile info
      // (For public profiles — restrict to isOwner(userId) || isAdmin() for private)
      allow get: if isAuthenticated();

      // Only admins can list all users
      allow list: if isAdmin();

      // Users create their own profile on signup
      allow create: if isOwner(userId)
        && hasAllFields(["displayName", "email", "createdAt", "updatedAt"])
        && hasOnlyFields(["displayName", "email", "photoUrl", "createdAt", "updatedAt", "preferences"])
        && isStringInRange("displayName", 1, 100)
        && isString("email")
        && isServerTimestamp("createdAt")
        && isServerTimestamp("updatedAt");

      // Users can update their own profile (except email and createdAt)
      // Admins can update any profile
      allow update: if (isOwner(userId) || isAdmin())
        && fieldNotChanged("email")
        && fieldNotChanged("createdAt")
        && isServerTimestamp("updatedAt")
        && isStringInRange("displayName", 1, 100);

      // Only admins can delete user profiles
      allow delete: if isAdmin();

      // User's private settings subcollection
      match /settings/{settingId} {
        allow read, write: if isOwner(userId);
      }
    }
```

#### 3.2 Content Collection with Ownership

```javascript
    // POSTS / CONTENT COLLECTION
    // Document ID = auto-generated
    // Owner can CRUD their own, editors can create/update, admins can do anything
    match /posts/{postId} {
      // Published posts readable by anyone authenticated
      // Draft posts readable only by owner or admin
      allow get: if isAuthenticated()
        && (resource.data.status == "published"
            || isDocOwner()
            || isAdmin());

      // List queries — published posts only (unless admin)
      allow list: if isAuthenticated()
        && (resource.data.status == "published" || isAdmin());

      // Editors and above can create posts
      allow create: if isEditorOrAbove()
        && willBeDocOwner()
        && hasAllFields(["title", "content", "ownerId", "status", "createdAt", "updatedAt"])
        && isStringInRange("title", 1, 200)
        && isStringWithMaxLength("content", 50000)
        && isOneOf("status", ["draft", "published"])
        && isServerTimestamp("createdAt")
        && isServerTimestamp("updatedAt");

      // Owner or admin can update
      allow update: if (isDocOwner() || isAdmin())
        && fieldNotChanged("ownerId")
        && fieldNotChanged("createdAt")
        && isServerTimestamp("updatedAt")
        && isStringInRange("title", 1, 200)
        && isStringWithMaxLength("content", 50000)
        && isOneOf("status", ["draft", "published", "archived"]);

      // Owner or admin can delete
      allow delete: if isDocOwner() || isAdmin();

      // Comments subcollection
      match /comments/{commentId} {
        allow read: if isAuthenticated();

        allow create: if isAuthenticated()
          && willBeDocOwner()
          && hasAllFields(["text", "ownerId", "createdAt"])
          && isStringInRange("text", 1, 2000)
          && isServerTimestamp("createdAt");

        // Only comment owner or admin can update/delete
        allow update: if isDocOwner()
          && fieldNotChanged("ownerId")
          && fieldNotChanged("createdAt");

        allow delete: if isDocOwner() || isAdmin();
      }
    }
```

#### 3.3 Shared/Team Collection

```javascript
    // ORGANIZATIONS COLLECTION (team/shared access)
    // Demonstrates Firestore-document-based role checking
    match /organizations/{orgId} {
      // Helper: check org membership
      function isOrgMember() {
        return isAuthenticated()
          && exists(/databases/$(database)/documents/organizations/$(orgId)/members/$(request.auth.uid));
      }

      function getOrgRole() {
        return get(/databases/$(database)/documents/organizations/$(orgId)/members/$(request.auth.uid)).data.role;
      }

      function isOrgAdmin() {
        return isOrgMember() && getOrgRole() == "admin";
      }

      function isOrgEditor() {
        return isOrgMember() && (getOrgRole() == "admin" || getOrgRole() == "editor");
      }

      // Organization document
      allow get: if isOrgMember();
      allow list: if isAdmin(); // Only super-admins list all orgs
      allow create: if isAuthenticated(); // Any authenticated user can create an org
      allow update: if isOrgAdmin();
      allow delete: if isAdmin(); // Only super-admins delete orgs

      // Organization members subcollection
      match /members/{memberId} {
        allow read: if isOrgMember();
        allow create: if isOrgAdmin();
        allow update: if isOrgAdmin();
        allow delete: if isOrgAdmin() || isOwner(memberId); // Members can remove themselves
      }

      // Organization content (inherits org-level access)
      match /items/{itemId} {
        allow read: if isOrgMember();
        allow create: if isOrgEditor();
        allow update: if isOrgEditor();
        allow delete: if isOrgAdmin();
      }
    }
```

#### 3.4 Rate-Limited Collection

```javascript
    // FEEDBACK / PUBLIC SUBMISSIONS
    // Rate-limited to prevent abuse
    match /feedback/{feedbackId} {
      allow read: if isAdmin();

      // Anyone authenticated can submit feedback, but rate-limited
      allow create: if isAuthenticated()
        && willBeDocOwner()
        && hasAllFields(["message", "ownerId", "createdAt", "type"])
        && isStringInRange("message", 10, 5000)
        && isOneOf("type", ["bug", "feature", "general"])
        && isServerTimestamp("createdAt")
        && notRateLimited(60); // Max 1 submission per minute

      allow update, delete: if false; // Feedback is immutable
    }

    // Rate limit tracking collection (written by Cloud Function or rules)
    match /rateLimits/{userId} {
      allow read: if isOwner(userId);
      allow write: if false; // Only writable by Cloud Functions
    }

    match /dailyCounts/{countId} {
      allow read: if isAuthenticated()
        && countId.matches(request.auth.uid + '_.*');
      allow write: if false; // Only writable by Cloud Functions
    }
```

#### 3.5 Closing the Rules

```javascript
    // ──────────────────────────────────────
    // CATCH-ALL: Deny everything not explicitly allowed
    // ──────────────────────────────────────
    // This is implicit in Firestore (deny by default),
    // but it's good practice to document it.
    // Any collection not matched above is automatically denied.

  } // end match /databases/{database}/documents
} // end service cloud.firestore
```

---

### Phase 4: Field Validation Patterns

#### 4.1 Common Validation Patterns

| Field Type | Validation Rule | Example |
|-----------|----------------|---------|
| Display name | Non-empty string, 1-100 chars | `isStringInRange("displayName", 1, 100)` |
| Email | String, non-empty (format validated by Auth) | `isNonEmptyString("email")` |
| URL | String, max 2048 chars | `isStringWithMaxLength("url", 2048)` |
| Tags | List, max 20 items, each string | `isListWithMaxSize("tags", 20)` |
| Status enum | String, one of allowed values | `isOneOf("status", ["active", "inactive"])` |
| Count/number | Number, non-negative | `isNumber("count") && request.resource.data.count >= 0` |
| Server timestamp | Must equal request.time | `isServerTimestamp("createdAt")` |
| Immutable field | Must not change on update | `fieldNotChanged("ownerId")` |
| Optional field | Validate only if present | `!("photoUrl" in request.resource.data) \|\| isStringWithMaxLength("photoUrl", 2048)` |

#### 4.2 Complex Validation Example

```javascript
// A document with multiple validation requirements
match /products/{productId} {
  allow create: if isEditorOrAbove()
    // Required fields
    && hasAllFields(["name", "price", "category", "ownerId", "createdAt", "updatedAt"])
    // No extra fields allowed
    && hasOnlyFields(["name", "price", "category", "description", "tags",
                       "imageUrl", "ownerId", "status", "createdAt", "updatedAt"])
    // Field validations
    && isStringInRange("name", 1, 200)
    && isNumber("price") && request.resource.data.price >= 0 && request.resource.data.price <= 999999
    && isOneOf("category", ["electronics", "clothing", "food", "services", "other"])
    && (!("description" in request.resource.data) || isStringWithMaxLength("description", 5000))
    && (!("tags" in request.resource.data) || isListWithMaxSize("tags", 20))
    && (!("imageUrl" in request.resource.data) || isStringWithMaxLength("imageUrl", 2048))
    && willBeDocOwner()
    && isOneOf("status", ["draft", "active"])
    && isServerTimestamp("createdAt")
    && isServerTimestamp("updatedAt");
}
```

---

### Phase 5: Testing Strategy

#### 5.1 Testing with Firebase Emulator

```typescript
// tests/firestore-rules.test.ts
import {
  initializeTestEnvironment,
  assertFails,
  assertSucceeds,
  RulesTestEnvironment,
} from "@firebase/rules-unit-testing";
import { doc, getDoc, setDoc, updateDoc, deleteDoc, serverTimestamp } from "firebase/firestore";
import fs from "fs";

let testEnv: RulesTestEnvironment;

beforeAll(async () => {
  testEnv = await initializeTestEnvironment({
    projectId: "test-project",
    firestore: {
      rules: fs.readFileSync("firestore.rules", "utf8"),
      host: "127.0.0.1",
      port: 8080,
    },
  });
});

afterAll(async () => {
  await testEnv.cleanup();
});

afterEach(async () => {
  await testEnv.clearFirestore();
});

describe("User profiles", () => {
  test("authenticated user can read any profile", async () => {
    // Seed data
    await testEnv.withSecurityRulesDisabled(async (context) => {
      const db = context.firestore();
      await setDoc(doc(db, "users", "user1"), {
        displayName: "Test User",
        email: "test@example.com",
        createdAt: serverTimestamp(),
        updatedAt: serverTimestamp(),
      });
    });

    // Test as authenticated user
    const alice = testEnv.authenticatedContext("alice");
    const db = alice.firestore();
    await assertSucceeds(getDoc(doc(db, "users", "user1")));
  });

  test("unauthenticated user cannot read profiles", async () => {
    const unauthed = testEnv.unauthenticatedContext();
    const db = unauthed.firestore();
    await assertFails(getDoc(doc(db, "users", "user1")));
  });

  test("user can only update own profile", async () => {
    await testEnv.withSecurityRulesDisabled(async (context) => {
      const db = context.firestore();
      await setDoc(doc(db, "users", "alice"), {
        displayName: "Alice",
        email: "alice@example.com",
        createdAt: serverTimestamp(),
        updatedAt: serverTimestamp(),
      });
    });

    // Alice updates her own profile — should succeed
    const alice = testEnv.authenticatedContext("alice");
    await assertSucceeds(
      updateDoc(doc(alice.firestore(), "users", "alice"), {
        displayName: "Alice Updated",
        updatedAt: serverTimestamp(),
      })
    );

    // Bob tries to update Alice's profile — should fail
    const bob = testEnv.authenticatedContext("bob");
    await assertFails(
      updateDoc(doc(bob.firestore(), "users", "alice"), {
        displayName: "Hacked",
        updatedAt: serverTimestamp(),
      })
    );
  });

  test("admin can update any profile", async () => {
    await testEnv.withSecurityRulesDisabled(async (context) => {
      const db = context.firestore();
      await setDoc(doc(db, "users", "user1"), {
        displayName: "User",
        email: "user@example.com",
        createdAt: serverTimestamp(),
        updatedAt: serverTimestamp(),
      });
    });

    const admin = testEnv.authenticatedContext("admin-uid", {
      role: "admin",
    });
    await assertSucceeds(
      updateDoc(doc(admin.firestore(), "users", "user1"), {
        displayName: "Updated by Admin",
        updatedAt: serverTimestamp(),
      })
    );
  });

  test("cannot change email on update", async () => {
    await testEnv.withSecurityRulesDisabled(async (context) => {
      const db = context.firestore();
      await setDoc(doc(db, "users", "alice"), {
        displayName: "Alice",
        email: "alice@example.com",
        createdAt: serverTimestamp(),
        updatedAt: serverTimestamp(),
      });
    });

    const alice = testEnv.authenticatedContext("alice");
    await assertFails(
      updateDoc(doc(alice.firestore(), "users", "alice"), {
        email: "newemail@example.com",
        updatedAt: serverTimestamp(),
      })
    );
  });
});

describe("Role-based access", () => {
  test("only editors can create posts", async () => {
    // Viewer cannot create
    const viewer = testEnv.authenticatedContext("viewer-uid", { role: "viewer" });
    await assertFails(
      setDoc(doc(viewer.firestore(), "posts", "post1"), {
        title: "Test Post",
        content: "Content",
        ownerId: "viewer-uid",
        status: "draft",
        createdAt: serverTimestamp(),
        updatedAt: serverTimestamp(),
      })
    );

    // Editor can create
    const editor = testEnv.authenticatedContext("editor-uid", { role: "editor" });
    await assertSucceeds(
      setDoc(doc(editor.firestore(), "posts", "post1"), {
        title: "Test Post",
        content: "Content",
        ownerId: "editor-uid",
        status: "draft",
        createdAt: serverTimestamp(),
        updatedAt: serverTimestamp(),
      })
    );
  });
});
```

#### 5.2 Rules Testing Checklist

```markdown
For each collection, test:

## Positive tests (should SUCCEED)
- [ ] Authenticated user with correct role can read
- [ ] Owner can read their own documents
- [ ] Owner can create with valid data
- [ ] Owner can update with valid data
- [ ] Admin can perform admin-only operations
- [ ] Valid field types are accepted
- [ ] Optional fields can be omitted

## Negative tests (should FAIL)
- [ ] Unauthenticated user cannot read
- [ ] Wrong role cannot perform restricted operation
- [ ] Non-owner cannot update/delete another's document
- [ ] Create with missing required fields fails
- [ ] Create with extra fields fails
- [ ] Update with invalid field types fails
- [ ] Update of immutable fields fails
- [ ] String exceeding max length fails
- [ ] Number outside valid range fails
- [ ] Invalid enum value fails
```

---

### Phase 6: Deployment and Monitoring

#### 6.1 Deployment Commands

```bash
# Deploy rules only (not functions, hosting, etc.)
firebase deploy --only firestore:rules

# Deploy to specific project
firebase deploy --only firestore:rules --project my-project-prod

# Dry run (validate without deploying)
firebase deploy --only firestore:rules --dry-run
```

#### 6.2 Monitoring Rule Denials

In the Firebase Console, go to **Firestore > Rules > Monitor** to see:
- Rule evaluation counts (allows vs denials)
- Which rules are being hit most
- Recent denial details (helpful for debugging)

Also check **Cloud Logging** for detailed rule evaluation logs:

```
resource.type="firestore_instance"
protoPayload.methodName="google.firestore.v1.Firestore.Write"
protoPayload.status.code!=0
```

#### 6.3 Common Deployment Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Rules deployed without testing | Random "permission denied" in production | Always test with Emulator Suite first |
| Missing `serverTimestamp()` on client | Rule requires `isServerTimestamp` but client sends `Date.now()` | Use `FieldValue.serverTimestamp()` in client code |
| Custom claims not propagated | User gets "permission denied" right after role change | Force token refresh: `user.getIdToken(true)` |
| Subcollection rules not matching | Subcollection accessible despite parent rules | Subcollection rules are independent; add explicit rules |
| `resource.data` in create rules | Error on create (no existing resource) | Use `request.resource.data` for incoming data |

---

## Expected Output

### Firestore Security Rules Specification

```markdown
# Security Rules: [App Name]

## Role Architecture
- **Primary roles:** [admin, editor, viewer via custom claims]
- **Assignment mechanism:** [Cloud Function `setUserRole`]
- **Bootstrap:** [First user gets admin via `bootstrapAdmin`]

## Permission Matrix
| Collection | Read | Create | Update | Delete |
|-----------|------|--------|--------|--------|
| users | Auth'd (get) / Admin (list) | Owner | Owner + Admin | Admin |
| posts | Auth'd (published) / Owner+Admin (draft) | Editor+ | Owner + Admin | Owner + Admin |
| comments | Auth'd | Auth'd | Owner | Owner + Admin |
| organizations | Members | Auth'd | Org Admin | Super Admin |
| feedback | Admin | Auth'd (rate-limited) | None | None |

## Validation Summary
| Collection | Required Fields | Validated Fields | Immutable Fields |
|-----------|----------------|-----------------|-----------------|
| [collection] | [fields] | [types + ranges] | [fields] |

## Helper Functions
| Function | Purpose | Used In |
|----------|---------|---------|
| isOwner(uid) | Check document ownership | users, posts |
| isEditorOrAbove() | Role hierarchy check | posts, products |
| notRateLimited(s) | Prevent abuse | feedback |

## Test Coverage
- [N] positive test cases
- [N] negative test cases
- All collections covered

## Deployment
- Rules file: `firestore.rules`
- Test file: `tests/firestore-rules.test.ts`
- Deploy command: `firebase deploy --only firestore:rules`
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Security rules generation focus with specific outcomes
- **ST-02** (Structured Sequential Instructions) - Phased approach from role design to deployment
- **RT-02** (Multi-Dimensional Analysis) - Security, usability, performance, and cost perspectives
- **CM-01** (Explicit Context Framing) - Firestore security model constraints and direct-client-access implications
- **DS-06** (Prioritization Guidance) - Custom claims vs Firestore roles decision, rule pattern selection

---

## Related Prompts

- `firestore_data_model_design.md` - Data model that rules protect
- `firebase_cloud_functions_design.md` - Cloud Functions for setting custom claims
- `firebase_auth_implementation.md` - Authentication that rules depend on
- `firebase_app_check_setup.md` - App Check that complements security rules
- `android_firebase_security_rules_audit.md` - Audit existing rules for vulnerabilities

---

## Customization Guide

- **For apps with no roles (single-user):** Strip out the role system entirely. Use only `isOwner()` checks. Most solo-developer apps with no team features don't need RBAC.
- **For apps with organizations/teams:** Expand the organization pattern with invite codes, pending membership states, and role inheritance between org-level and resource-level.
- **For apps with public content:** Add an `isPublic()` helper that checks `resource.data.visibility == "public"` and allow unauthenticated reads for public documents.
- **For apps with premium features:** Add a `isPremium()` helper based on custom claims or a subscription status field, and gate access to premium collections.
- **For apps migrating from wide-open rules:** Start by adding rules in "monitor mode" using the Firebase Console Rules Playground to verify they work before enforcing.
