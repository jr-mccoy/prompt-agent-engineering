---
title: "Firebase Emulator Suite Setup"
category: mobile-development
description: "Configure Firebase Emulator Suite for local development — all services setup, firebase.json config, seed data import/export, CI integration with GitHub Actions, security rules testing automation, and data seeding scripts"
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
  - emulator-suite
  - local-development
  - testing
  - solo-developer
updated: "2026-02-11"
---

# Firebase Emulator Suite Setup

**Objective:** Configure the Firebase Emulator Suite for complete local development — covering all services (Auth, Firestore, Cloud Functions, Storage, Hosting), firebase.json emulator configuration, seed data import and export workflows, CI integration with GitHub Actions, security rules testing automation, and data seeding scripts — producing a local development environment that mirrors production Firebase behavior without incurring costs, risking production data, or requiring network access.

**When to Use:** Use this prompt when starting a new Firebase project and want a professional local development setup from day one, when you are tired of testing against production or staging Firebase (and the costs and risks that come with it), when you need to run automated tests against Firebase services in CI/CD, when you want to develop offline (on a plane, in a coffee shop with bad WiFi), or when you need repeatable test data that resets between test runs. Critical because developing directly against production Firebase is the fastest way to corrupt real user data, hit billing surprises, and create flaky tests that depend on network state.

**Important context:** The Firebase Emulator Suite runs local versions of Firebase services on your machine. These emulators are NOT simplified mocks — they implement the actual Firebase behavior including security rules evaluation, Firestore query semantics, Cloud Functions triggers, and Auth token verification. This means your local tests are highly representative of production behavior. The main limitations are: emulators do not support Firebase Extensions, some advanced Firestore features (like TTL policies), or cross-project operations. For a solo developer, the emulator suite eliminates the need for a separate staging Firebase project in most cases.

---

## Context Gathering

Before configuring the Emulator Suite, gather essential context:

1. **Firebase Services Used:**
   - "Which Firebase services does your app use (Auth, Firestore, RTDB, Functions, Storage, Hosting)?"
   - "Are you using Cloud Functions 1st gen, 2nd gen, or both?"
   - "Do your Cloud Functions call external APIs?"
   - "Are you using Firebase Extensions?"

2. **Current Development Workflow:**
   - "How do you currently test Firebase interactions (against production, staging, or mocks)?"
   - "Do you have a separate Firebase project for development?"
   - "Are you running any automated tests that interact with Firebase?"
   - "Do you develop offline frequently?"

3. **Testing Requirements:**
   - "Do you have Firestore security rules that need testing?"
   - "Do you need to test Cloud Functions triggers (Firestore onCreate, Auth onCreate, etc.)?"
   - "Do you need repeatable test data for development?"
   - "Are you running tests in CI/CD (GitHub Actions, GitLab CI, etc.)?"

4. **Environment:**
   - "What is your development OS (macOS, Linux, Windows)?"
   - "Do you have Java 11+ installed (required for emulators)?"
   - "What Node.js version are you running (required for Cloud Functions emulator)?"
   - "How much RAM does your development machine have (emulators use 500MB-2GB)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before relying on emulators for testing, you MUST:**

1. **Verify emulator parity with production** — The emulators replicate most Firebase behavior, but not all. Test critical flows against a real Firebase project at least once before launch. Known differences include: no support for Firebase Extensions, no TTL policies, simplified Auth token verification, and no cross-project operations.
2. **Point your app at emulators, not production** — If your app connects to production Firebase while the emulators are running, you will modify production data. Always verify the emulator connection is active before testing.
3. **Keep security rules in sync** — The Firestore and Storage emulators load rules from local files. If you edit rules in the Firebase Console but not locally, your tests will pass against outdated rules.
4. **Export data before stopping emulators** — Emulator data is ephemeral. When you stop the emulators, all data is lost unless you export it. Set up an export workflow or use seed scripts.
5. **Test with emulators AND production** — Emulators are for development speed and safety. Always do a final integration test against a real Firebase project before releasing.

### False-Positive Prevention

- Do NOT develop against production Firebase when emulators can do the job — you risk corrupting real data and incurring costs
- Do NOT assume emulator tests guarantee production behavior — always verify critical paths against real Firebase
- Do NOT hardcode emulator ports if they conflict with other services on your machine
- Do NOT forget to check `useEmulator()` calls are only active in debug/test builds — shipping these to production will break your app
- Do NOT skip security rules testing — "it works in the emulator without rules" is not a valid test
- DO use environment-aware configuration that automatically connects to emulators in development
- DO export seed data and commit it to source control for reproducible development environments
- DO test security rules with the emulator's built-in rules testing library
- DO configure CI to run the full emulator suite for automated testing
- DO keep your local `firestore.rules` and `storage.rules` files as the source of truth

---

### Phase 1: Installation and Configuration

#### 1.1 Prerequisites

```bash
# Check Java version (11+ required)
java -version
# If not installed: brew install openjdk@17 (macOS) or apt install openjdk-17-jdk (Linux)

# Check Node.js version (18+ recommended for Cloud Functions)
node --version
# If not installed: use nvm (recommended) or direct install

# Install Firebase CLI
npm install -g firebase-tools

# Verify installation
firebase --version
# Should be 13.0.0 or later

# Login to Firebase (required for initial setup, not for emulator use)
firebase login

# Initialize Firebase in your project (if not already done)
firebase init
# Select: Firestore, Functions, Storage, Hosting, Emulators
```

#### 1.2 firebase.json Emulator Configuration

```json
{
  "firestore": {
    "rules": "firestore.rules",
    "indexes": "firestore.indexes.json"
  },
  "functions": [
    {
      "source": "functions",
      "codebase": "default",
      "ignore": [
        "node_modules",
        ".git",
        "firebase-debug.log",
        "firebase-debug.*.log",
        "*.local"
      ],
      "predeploy": [
        "npm --prefix \"$RESOURCE_DIR\" run lint",
        "npm --prefix \"$RESOURCE_DIR\" run build"
      ]
    }
  ],
  "storage": {
    "rules": "storage.rules"
  },
  "hosting": {
    "public": "public",
    "ignore": [
      "firebase-debug.log",
      "firebase-debug.*.log",
      "*.local"
    ]
  },
  "emulators": {
    "auth": {
      "port": 9099,
      "host": "0.0.0.0"
    },
    "functions": {
      "port": 5001,
      "host": "0.0.0.0"
    },
    "firestore": {
      "port": 8080,
      "host": "0.0.0.0"
    },
    "storage": {
      "port": 9199,
      "host": "0.0.0.0"
    },
    "hosting": {
      "port": 5000,
      "host": "0.0.0.0"
    },
    "ui": {
      "enabled": true,
      "port": 4000,
      "host": "0.0.0.0"
    },
    "singleProjectMode": true
  }
}
```

**Configuration notes:**
- `host: "0.0.0.0"` allows connections from Android emulators and physical devices on the same network. Use `"127.0.0.1"` if you only need local access.
- `singleProjectMode: true` ensures all emulators share the same project context.
- Port numbers are defaults — change them if they conflict with other services.
- The UI emulator on port 4000 provides a web dashboard for inspecting data, auth users, and function logs.

#### 1.3 Port Conflict Resolution

```markdown
## Default Ports and Alternatives

| Service | Default Port | Alternative | Check If In Use |
|---------|-------------|-------------|-----------------|
| Emulator UI | 4000 | 4040 | lsof -i :4000 |
| Hosting | 5000 | 5050 | lsof -i :5000 |
| Functions | 5001 | 5051 | lsof -i :5001 |
| Firestore | 8080 | 8180 | lsof -i :8080 |
| Auth | 9099 | 9199 | lsof -i :9099 |
| Storage | 9199 | 9299 | lsof -i :9199 |

Common conflicts:
- Port 5000: AirPlay Receiver on macOS (disable in System Settings → General → AirDrop & Handoff)
- Port 8080: Many web servers, Spring Boot default
- Port 9099: Some security tools
```

---

### Phase 2: Service Setup

#### 2.1 Android App Emulator Connection

```kotlin
/**
 * Connect Android app to Firebase emulators.
 *
 * CRITICAL: These connections must ONLY be active in debug builds.
 * Shipping useEmulator() calls to production will break your app.
 */
object FirebaseEmulatorConfig {

    // For Android emulator: use 10.0.2.2 (maps to host machine's localhost)
    // For physical device on same network: use your machine's IP address
    private const val EMULATOR_HOST = "10.0.2.2"

    fun connectToEmulators() {
        if (!BuildConfig.DEBUG) {
            // SAFETY: Never connect to emulators in release builds
            return
        }

        // Auth emulator
        Firebase.auth.useEmulator(EMULATOR_HOST, 9099)

        // Firestore emulator
        Firebase.firestore.useEmulator(EMULATOR_HOST, 8080)

        // Cloud Functions emulator
        Firebase.functions.useEmulator(EMULATOR_HOST, 5001)

        // Storage emulator
        Firebase.storage.useEmulator(EMULATOR_HOST, 9199)

        // Disable Firestore SSL for emulator (required)
        Firebase.firestore.firestoreSettings = firestoreSettings {
            host = "$EMULATOR_HOST:8080"
            isSslEnabled = false
            isPersistenceEnabled = false // Disable for clean test state
        }

        Log.d("Firebase", "Connected to Firebase emulators")
    }
}

// Call in Application.onCreate() BEFORE any Firebase operations
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Initialize Firebase
        FirebaseApp.initializeApp(this)

        // Connect to emulators in debug builds
        FirebaseEmulatorConfig.connectToEmulators()
    }
}
```

#### 2.2 Auth Emulator Setup

```kotlin
// Creating test users in the Auth emulator
// Option 1: Use the Emulator UI (http://localhost:4000 → Auth tab)
// Option 2: Create programmatically in a seed script
// Option 3: Create in your app's debug menu

class AuthEmulatorHelper {

    suspend fun createTestUser(
        email: String,
        password: String,
        displayName: String
    ): FirebaseUser? {
        return try {
            val result = Firebase.auth.createUserWithEmailAndPassword(email, password).await()
            result.user?.updateProfile(
                userProfileChangeRequest {
                    this.displayName = displayName
                }
            )?.await()
            result.user
        } catch (e: FirebaseAuthUserCollisionException) {
            // User already exists in emulator, sign in instead
            val result = Firebase.auth.signInWithEmailAndPassword(email, password).await()
            result.user
        }
    }

    // Pre-built test accounts
    suspend fun seedTestUsers() {
        createTestUser("admin@test.com", "password123", "Test Admin")
        createTestUser("user@test.com", "password123", "Test User")
        createTestUser("premium@test.com", "password123", "Premium User")
    }
}
```

#### 2.3 Firestore Emulator with Security Rules

The Firestore emulator evaluates your security rules exactly as production does. Your `firestore.rules` file is loaded automatically:

```
// firestore.rules
rules_version = '2';

service cloud.firestore {
  match /databases/{database}/documents {

    // Users collection — owner-only access
    match /users/{userId} {
      allow read, update: if request.auth != null && request.auth.uid == userId;
      allow create: if request.auth != null && request.auth.uid == userId;
      allow delete: if false; // Users can't delete their own document

      // User's private subcollection
      match /private/{document=**} {
        allow read, write: if request.auth != null && request.auth.uid == userId;
      }
    }

    // Tasks collection — owner access with field validation
    match /tasks/{taskId} {
      allow read: if request.auth != null
                  && resource.data.ownerId == request.auth.uid;
      allow create: if request.auth != null
                    && request.resource.data.ownerId == request.auth.uid
                    && request.resource.data.title is string
                    && request.resource.data.title.size() > 0
                    && request.resource.data.title.size() <= 200;
      allow update: if request.auth != null
                    && resource.data.ownerId == request.auth.uid
                    && request.resource.data.ownerId == request.auth.uid;
      allow delete: if request.auth != null
                    && resource.data.ownerId == request.auth.uid;
    }

    // Public content — anyone can read, only admins can write
    match /public/{document=**} {
      allow read: if true;
      allow write: if request.auth != null
                   && request.auth.token.admin == true;
    }
  }
}
```

#### 2.4 Cloud Functions Emulator

```typescript
// functions/src/index.ts
// Cloud Functions run locally with full trigger support

import { onDocumentCreated } from "firebase-functions/v2/firestore";
import { onCall } from "firebase-functions/v2/https";
import { onSchedule } from "firebase-functions/v2/scheduler";

// Firestore trigger — fires when a document is created in the emulator
export const onTaskCreated = onDocumentCreated(
  "tasks/{taskId}",
  async (event) => {
    const data = event.data?.data();
    if (!data) return;

    console.log(`New task created: ${data.title} by ${data.ownerId}`);

    // Update user's task count
    const userRef = event.data?.ref.firestore.doc(`users/${data.ownerId}`);
    await userRef?.update({
      taskCount: FieldValue.increment(1),
    });
  }
);

// Callable function — callable from Android app via emulator
export const completeTask = onCall(async (request) => {
  if (!request.auth) {
    throw new HttpsError("unauthenticated", "Must be logged in");
  }

  const { taskId } = request.data;
  const db = getFirestore();
  const taskRef = db.doc(`tasks/${taskId}`);
  const task = await taskRef.get();

  if (!task.exists) {
    throw new HttpsError("not-found", "Task not found");
  }

  if (task.data()?.ownerId !== request.auth.uid) {
    throw new HttpsError("permission-denied", "Not your task");
  }

  await taskRef.update({
    completedAt: FieldValue.serverTimestamp(),
    status: "completed",
  });

  return { success: true };
});

// Scheduled function — in the emulator, trigger manually via shell
export const dailyCleanup = onSchedule("every 24 hours", async () => {
  const db = getFirestore();
  const thirtyDaysAgo = new Date();
  thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);

  const oldTasks = await db
    .collection("tasks")
    .where("completedAt", "<", thirtyDaysAgo)
    .get();

  const batch = db.batch();
  oldTasks.docs.forEach((doc) => batch.delete(doc.ref));
  await batch.commit();

  console.log(`Cleaned up ${oldTasks.size} old completed tasks`);
});
```

#### 2.5 Storage Emulator

```
// storage.rules
rules_version = '2';

service firebase.storage {
  match /b/{bucket}/o {

    // User uploads — owner only, max 10MB, images only
    match /users/{userId}/uploads/{fileName} {
      allow read: if request.auth != null && request.auth.uid == userId;
      allow write: if request.auth != null
                   && request.auth.uid == userId
                   && request.resource.size < 10 * 1024 * 1024
                   && request.resource.contentType.matches('image/.*');
      allow delete: if request.auth != null && request.auth.uid == userId;
    }

    // Public assets — anyone can read, only admins can write
    match /public/{allPaths=**} {
      allow read: if true;
      allow write: if request.auth != null
                   && request.auth.token.admin == true;
    }
  }
}
```

---

### Phase 3: Data Seeding

#### 3.1 Seed Data Export and Import

```bash
# Start emulators
firebase emulators:start

# After creating test data via the app or Emulator UI, export it:
firebase emulators:export ./seed-data

# This creates a directory structure:
# seed-data/
#   auth_export/
#     accounts.json       # User accounts
#     config.json          # Auth config
#   firestore_export/
#     all_namespaces/      # All Firestore data
#     firestore_export.overall_export_metadata
#   storage_export/
#     buckets.json         # Storage metadata
#     blobs/               # Actual files

# Start emulators with seed data pre-loaded:
firebase emulators:start --import=./seed-data

# Auto-export on shutdown (so you never lose emulator data):
firebase emulators:start --import=./seed-data --export-on-exit=./seed-data
```

#### 3.2 Data Seeding Script

Create a TypeScript seeding script for reproducible test data:

```typescript
// scripts/seed-emulator.ts
import { initializeApp } from "firebase-admin/app";
import { getAuth } from "firebase-admin/auth";
import { getFirestore } from "firebase-admin/firestore";

// Connect to emulators
process.env.FIREBASE_AUTH_EMULATOR_HOST = "127.0.0.1:9099";
process.env.FIRESTORE_EMULATOR_HOST = "127.0.0.1:8080";
process.env.FIREBASE_STORAGE_EMULATOR_HOST = "127.0.0.1:9199";

const app = initializeApp({ projectId: "demo-project" });
const auth = getAuth(app);
const db = getFirestore(app);

interface TestUser {
  email: string;
  password: string;
  displayName: string;
  customClaims?: Record<string, unknown>;
}

const TEST_USERS: TestUser[] = [
  {
    email: "admin@test.com",
    password: "password123",
    displayName: "Admin User",
    customClaims: { admin: true },
  },
  {
    email: "premium@test.com",
    password: "password123",
    displayName: "Premium User",
    customClaims: { tier: "premium" },
  },
  {
    email: "free@test.com",
    password: "password123",
    displayName: "Free User",
    customClaims: { tier: "free" },
  },
];

async function seedUsers(): Promise<Map<string, string>> {
  const userIds = new Map<string, string>();

  for (const user of TEST_USERS) {
    try {
      const userRecord = await auth.createUser({
        email: user.email,
        password: user.password,
        displayName: user.displayName,
      });

      if (user.customClaims) {
        await auth.setCustomUserClaims(userRecord.uid, user.customClaims);
      }

      userIds.set(user.email, userRecord.uid);
      console.log(`Created user: ${user.email} (${userRecord.uid})`);
    } catch (error: unknown) {
      if ((error as { code?: string }).code === "auth/email-already-exists") {
        const existing = await auth.getUserByEmail(user.email);
        userIds.set(user.email, existing.uid);
        console.log(`User exists: ${user.email} (${existing.uid})`);
      } else {
        throw error;
      }
    }
  }

  return userIds;
}

async function seedFirestore(userIds: Map<string, string>): Promise<void> {
  const adminUid = userIds.get("admin@test.com")!;
  const premiumUid = userIds.get("premium@test.com")!;
  const freeUid = userIds.get("free@test.com")!;

  // Seed user profiles
  const users = [
    {
      uid: adminUid,
      data: {
        displayName: "Admin User",
        email: "admin@test.com",
        tier: "admin",
        taskCount: 0,
        createdAt: new Date(),
      },
    },
    {
      uid: premiumUid,
      data: {
        displayName: "Premium User",
        email: "premium@test.com",
        tier: "premium",
        taskCount: 0,
        createdAt: new Date(),
      },
    },
    {
      uid: freeUid,
      data: {
        displayName: "Free User",
        email: "free@test.com",
        tier: "free",
        taskCount: 0,
        createdAt: new Date(),
      },
    },
  ];

  for (const user of users) {
    await db.doc(`users/${user.uid}`).set(user.data);
    console.log(`Created user profile: ${user.data.email}`);
  }

  // Seed tasks for each user
  const taskTemplates = [
    { title: "Buy groceries", status: "pending", priority: "medium" },
    { title: "Review pull request", status: "pending", priority: "high" },
    { title: "Update documentation", status: "completed", priority: "low" },
    { title: "Fix login bug", status: "in_progress", priority: "high" },
    { title: "Deploy to staging", status: "pending", priority: "medium" },
  ];

  for (const user of users) {
    for (const task of taskTemplates) {
      await db.collection("tasks").add({
        ...task,
        ownerId: user.uid,
        createdAt: new Date(),
        completedAt: task.status === "completed" ? new Date() : null,
      });
    }
    // Update task count
    await db.doc(`users/${user.uid}`).update({ taskCount: taskTemplates.length });
    console.log(`Created ${taskTemplates.length} tasks for ${user.data.email}`);
  }

  // Seed public content
  await db.doc("public/announcements").set({
    title: "Welcome to the app!",
    body: "This is a test announcement for the emulator.",
    createdAt: new Date(),
    createdBy: adminUid,
  });
  console.log("Created public announcement");
}

async function main(): Promise<void> {
  console.log("Seeding Firebase emulators...");
  console.log("---");

  const userIds = await seedUsers();
  console.log("---");

  await seedFirestore(userIds);
  console.log("---");

  console.log("Seeding complete!");
  console.log(`Total users: ${TEST_USERS.length}`);
  console.log("Test credentials:");
  for (const user of TEST_USERS) {
    console.log(`  ${user.email} / ${user.password} (${user.displayName})`);
  }
}

main().catch(console.error);
```

#### 3.3 Package.json Scripts for Emulator Workflow

```json
{
  "scripts": {
    "emulators:start": "firebase emulators:start --import=./seed-data",
    "emulators:start-fresh": "firebase emulators:start",
    "emulators:start-persist": "firebase emulators:start --import=./seed-data --export-on-exit=./seed-data",
    "emulators:export": "firebase emulators:export ./seed-data",
    "emulators:seed": "ts-node scripts/seed-emulator.ts",
    "emulators:reset": "rm -rf seed-data && npm run emulators:start-fresh",
    "test:rules": "firebase emulators:exec --only firestore 'npm run test:rules:run'",
    "test:rules:run": "jest --config jest.rules.config.js",
    "test:functions": "firebase emulators:exec 'npm run test:functions:run'",
    "test:functions:run": "jest --config jest.functions.config.js"
  }
}
```

#### 3.4 .gitignore Entries for Emulator Data

```gitignore
# Firebase Emulator data (large binary blobs)
# Commit seed-data/ if you want reproducible environments
# .gitignore it if seed data is generated by scripts
seed-data/firestore_export/
seed-data/storage_export/blobs/

# Keep the auth export (small JSON, useful for reproducibility)
# !seed-data/auth_export/

# Firebase debug logs
firebase-debug.log
firebase-debug.*.log
ui-debug.log

# Emulator-generated files
firestore-debug.log
pubsub-debug.log
```

---

### Phase 4: Security Rules Testing

#### 4.1 Rules Testing Setup

```typescript
// tests/firestore.rules.test.ts
import {
  initializeTestEnvironment,
  assertSucceeds,
  assertFails,
  RulesTestEnvironment,
} from "@firebase/rules-unit-testing";
import { readFileSync } from "fs";
import {
  doc,
  getDoc,
  setDoc,
  updateDoc,
  deleteDoc,
  collection,
  addDoc,
} from "firebase/firestore";

let testEnv: RulesTestEnvironment;

beforeAll(async () => {
  testEnv = await initializeTestEnvironment({
    projectId: "demo-test-project",
    firestore: {
      rules: readFileSync("firestore.rules", "utf8"),
      host: "127.0.0.1",
      port: 8080,
    },
  });
});

afterAll(async () => {
  await testEnv.cleanup();
});

beforeEach(async () => {
  await testEnv.clearFirestore();
});
```

#### 4.2 Security Rules Test Cases

```typescript
// tests/firestore.rules.test.ts (continued)

describe("Users collection", () => {
  test("user can read own profile", async () => {
    const userId = "user-123";

    // Seed data as admin
    await testEnv.withSecurityRulesDisabled(async (context) => {
      await setDoc(doc(context.firestore(), `users/${userId}`), {
        displayName: "Test User",
        email: "test@test.com",
        tier: "free",
      });
    });

    // Test as authenticated user
    const userContext = testEnv.authenticatedContext(userId);
    const userDoc = doc(userContext.firestore(), `users/${userId}`);
    await assertSucceeds(getDoc(userDoc));
  });

  test("user cannot read another user's profile", async () => {
    const userId = "user-123";
    const otherUserId = "user-456";

    await testEnv.withSecurityRulesDisabled(async (context) => {
      await setDoc(doc(context.firestore(), `users/${otherUserId}`), {
        displayName: "Other User",
        email: "other@test.com",
        tier: "premium",
      });
    });

    const userContext = testEnv.authenticatedContext(userId);
    const otherDoc = doc(userContext.firestore(), `users/${otherUserId}`);
    await assertFails(getDoc(otherDoc));
  });

  test("unauthenticated user cannot read any profile", async () => {
    await testEnv.withSecurityRulesDisabled(async (context) => {
      await setDoc(doc(context.firestore(), "users/user-123"), {
        displayName: "Test User",
      });
    });

    const unauthedContext = testEnv.unauthenticatedContext();
    const userDoc = doc(unauthedContext.firestore(), "users/user-123");
    await assertFails(getDoc(userDoc));
  });

  test("user cannot delete own profile", async () => {
    const userId = "user-123";

    await testEnv.withSecurityRulesDisabled(async (context) => {
      await setDoc(doc(context.firestore(), `users/${userId}`), {
        displayName: "Test User",
      });
    });

    const userContext = testEnv.authenticatedContext(userId);
    const userDoc = doc(userContext.firestore(), `users/${userId}`);
    await assertFails(deleteDoc(userDoc));
  });
});

describe("Tasks collection", () => {
  test("user can create task with own ID as owner", async () => {
    const userId = "user-123";
    const userContext = testEnv.authenticatedContext(userId);
    const tasksRef = collection(userContext.firestore(), "tasks");

    await assertSucceeds(
      addDoc(tasksRef, {
        title: "Test task",
        ownerId: userId,
        status: "pending",
        createdAt: new Date(),
      })
    );
  });

  test("user cannot create task with someone else as owner", async () => {
    const userId = "user-123";
    const userContext = testEnv.authenticatedContext(userId);
    const tasksRef = collection(userContext.firestore(), "tasks");

    await assertFails(
      addDoc(tasksRef, {
        title: "Spoofed task",
        ownerId: "someone-else",
        status: "pending",
      })
    );
  });

  test("task title must be 1-200 characters", async () => {
    const userId = "user-123";
    const userContext = testEnv.authenticatedContext(userId);
    const tasksRef = collection(userContext.firestore(), "tasks");

    // Empty title should fail
    await assertFails(
      addDoc(tasksRef, {
        title: "",
        ownerId: userId,
      })
    );

    // 201-character title should fail
    await assertFails(
      addDoc(tasksRef, {
        title: "x".repeat(201),
        ownerId: userId,
      })
    );

    // Valid title should succeed
    await assertSucceeds(
      addDoc(tasksRef, {
        title: "Valid task title",
        ownerId: userId,
      })
    );
  });
});

describe("Public collection", () => {
  test("anyone can read public content", async () => {
    await testEnv.withSecurityRulesDisabled(async (context) => {
      await setDoc(doc(context.firestore(), "public/announcement"), {
        title: "Hello",
        body: "World",
      });
    });

    const unauthedContext = testEnv.unauthenticatedContext();
    const publicDoc = doc(unauthedContext.firestore(), "public/announcement");
    await assertSucceeds(getDoc(publicDoc));
  });

  test("only admins can write public content", async () => {
    // Regular user cannot write
    const userContext = testEnv.authenticatedContext("user-123");
    const publicDoc = doc(userContext.firestore(), "public/announcement");
    await assertFails(setDoc(publicDoc, { title: "Hacked" }));

    // Admin can write
    const adminContext = testEnv.authenticatedContext("admin-123", {
      admin: true,
    });
    const adminDoc = doc(adminContext.firestore(), "public/announcement");
    await assertSucceeds(setDoc(adminDoc, { title: "Official" }));
  });
});
```

#### 4.3 Jest Configuration for Rules Tests

```javascript
// jest.rules.config.js
module.exports = {
  testMatch: ["**/tests/firestore.rules.test.ts"],
  transform: {
    "^.+\\.tsx?$": "ts-jest",
  },
  testTimeout: 30000, // Emulator tests can be slow
  verbose: true,
};
```

---

### Phase 5: CI Integration

#### 5.1 GitHub Actions Workflow

```yaml
# .github/workflows/firebase-tests.yml
name: Firebase Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  firebase-emulator-tests:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Set up Java (required for emulators)
        uses: actions/setup-java@v4
        with:
          distribution: "temurin"
          java-version: "17"

      - name: Install dependencies
        run: npm ci

      - name: Install Functions dependencies
        run: cd functions && npm ci

      - name: Build Functions
        run: cd functions && npm run build

      - name: Install Firebase CLI
        run: npm install -g firebase-tools

      - name: Run Firestore rules tests
        run: |
          firebase emulators:exec \
            --only firestore \
            --project demo-test-project \
            'npx jest --config jest.rules.config.js --forceExit'

      - name: Run Cloud Functions tests
        run: |
          firebase emulators:exec \
            --only firestore,functions,auth \
            --project demo-test-project \
            'npx jest --config jest.functions.config.js --forceExit'

      - name: Run integration tests with seed data
        run: |
          firebase emulators:exec \
            --import=./seed-data \
            --project demo-test-project \
            'npx jest --config jest.integration.config.js --forceExit'
```

#### 5.2 CI Optimization Tips

```yaml
# Cache Firebase emulator binaries to speed up CI
      - name: Cache Firebase emulators
        uses: actions/cache@v4
        with:
          path: ~/.cache/firebase/emulators
          key: ${{ runner.os }}-firebase-emulators-${{ hashFiles('firebase.json') }}
          restore-keys: |
            ${{ runner.os }}-firebase-emulators-

# The --project flag with "demo-" prefix creates a demo project
# that doesn't require Firebase authentication in CI
# This is the recommended approach for CI environments
```

#### 5.3 CI Environment Variables

```yaml
# .github/workflows/firebase-tests.yml (env section)
env:
  # Use demo project ID — no Firebase auth needed
  GCLOUD_PROJECT: demo-test-project
  # Disable Firebase CLI analytics in CI
  FIREBASE_CLI_EXPERIMENTS: ""
  # Suppress emulator UI in CI (not needed)
  FIREBASE_EMULATORS_UI: "false"
```

#### 5.4 Complete CI Test Matrix

```markdown
## CI Test Categories

| Test Suite | Emulators Needed | Config File | Purpose |
|-----------|-----------------|-------------|---------|
| Security rules | Firestore only | jest.rules.config.js | Validate access control |
| Cloud Functions | Firestore + Functions + Auth | jest.functions.config.js | Validate server logic |
| Integration | All services | jest.integration.config.js | End-to-end data flows |
| Seed data | All services + import | jest.seed.config.js | Verify seed scripts work |

## CI Run Time Budget

| Step | Expected Duration | If Exceeds |
|------|------------------|-----------|
| Install dependencies | 30-60s | Check npm cache |
| Build Functions | 10-30s | Check TypeScript config |
| Start emulators | 15-30s | Check Java version |
| Rules tests | 30-60s | Check test count |
| Functions tests | 30-120s | Check test timeout |
| Integration tests | 60-180s | Check seed data size |
| **Total** | **3-8 minutes** | Parallelize test suites |
```

---

## Expected Output

### Emulator Suite Configuration Document

```markdown
# Emulator Suite Configuration: [App Name]

## Services Configured
| Service | Port | Status | Rules File |
|---------|------|--------|-----------|
| Auth | 9099 | Active | — |
| Firestore | 8080 | Active | firestore.rules |
| Functions | 5001 | Active | functions/src/index.ts |
| Storage | 9199 | Active | storage.rules |
| Hosting | 5000 | Active | public/ |
| Emulator UI | 4000 | Active | — |

## Quick Start Commands
| Command | Purpose |
|---------|---------|
| `npm run emulators:start` | Start with seed data |
| `npm run emulators:start-fresh` | Start clean (no data) |
| `npm run emulators:start-persist` | Start with auto-save on exit |
| `npm run emulators:seed` | Run seed script |
| `npm run test:rules` | Run security rules tests |
| `npm run test:functions` | Run Cloud Functions tests |

## Test Accounts
| Email | Password | Role | Custom Claims |
|-------|----------|------|--------------|
| admin@test.com | password123 | Admin | { admin: true } |
| premium@test.com | password123 | Premium | { tier: "premium" } |
| free@test.com | password123 | Free | { tier: "free" } |

## Seed Data Summary
| Collection | Document Count | Description |
|-----------|---------------|-------------|
| users | 3 | One per test account |
| tasks | 15 | 5 per user, various states |
| public | 1 | Test announcement |

## Security Rules Test Coverage
| Rule | Tests | Coverage |
|------|-------|---------|
| users read (own) | 2 | Allowed + Denied |
| users write (own) | 2 | Create + Update |
| users delete | 1 | Denied |
| tasks CRUD | 4 | Full owner validation |
| tasks validation | 2 | Title length |
| public read | 1 | Unauthenticated |
| public write | 2 | Admin vs regular |

## CI Pipeline
- **Platform:** GitHub Actions
- **Trigger:** Push to main, PR to main
- **Test suites:** Rules, Functions, Integration
- **Expected duration:** 3-8 minutes
- **Emulator caching:** Enabled
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Emulator Suite setup with explicit scope covering all services
- **ST-02** (Structured Sequential Instructions) - Phased setup from installation through CI integration
- **RT-02** (Multi-Dimensional Analysis) - Each Firebase service as a distinct emulator configuration, plus seeding, rules testing, and CI as cross-cutting concerns
- **CM-01** (Explicit Context Framing) - Emulator parity with production, limitations, and development workflow requirements
- **DS-06** (Prioritization Guidance) - Essential setup first (config, connection), then data seeding, then testing, then CI

---

## Related Prompts

- `firebase_security_rules_generator.md` - Generate the security rules that the emulator evaluates
- `firebase_cloud_functions_design.md` - Design functions that run in the Functions emulator
- `firestore_data_model_design.md` - Data model that seed scripts populate
- `firebase_security_rules_audit.md` - Audit rules using emulator test results
- `android_ci_cd_pipeline_design.md` - CI/CD pipeline that includes emulator test jobs

---

## Customization Guide

- **For apps using Realtime Database instead of Firestore:** Replace the Firestore emulator configuration with RTDB (`"database": { "port": 9000 }`). The seeding approach is the same but uses the RTDB admin API (`getDatabase()` instead of `getFirestore()`). Rules testing uses `@firebase/rules-unit-testing` with the `database` option instead of `firestore`.
- **For apps with Firebase Extensions:** The emulator suite does not support Extensions. For features that depend on Extensions (e.g., Resize Images, Translate Text), mock the Extension's behavior in a local Cloud Function that mimics the Extension's trigger and output.
- **For monorepo setups (Android + iOS + web):** Share the emulator configuration and seed data across platforms. The `firebase.json` and seed scripts are platform-agnostic. Each platform's test suite connects to the same emulator ports.
- **For apps with large seed data sets:** Instead of seeding programmatically on every start, export a comprehensive data set once and commit the `seed-data/` directory to source control. Use `--import=./seed-data` for fast startup. Regenerate the export when the data model changes.
- **For teams with multiple developers:** Each developer should run their own emulator instance on their machine. There is no need for a shared emulator server. Commit the `firebase.json` configuration and seed scripts so everyone has the same setup. Use the same port numbers across the team to simplify documentation and debugging.
