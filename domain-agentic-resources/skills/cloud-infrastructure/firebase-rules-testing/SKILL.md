---
name: firebase-rules-testing
description: "Automated Firebase security rules testing workflow covering test case generation from rules, emulator-based execution, access control validation for all user roles, common vulnerability checks, and coverage reporting. Use this skill when testing Firestore or RTDB security rules, when rules change before deployment, when auditing security rule coverage, or when a developer mentions 'rules test', 'security rules testing', 'emulator test', or 'rules coverage'."
metadata:
  tags:
    - firebase
    - security
    - testing
    - emulator
    - solo-developer
  updated: "2026-02-12"
---

# Firebase Rules Testing

Automated security rules testing for Firebase Firestore and Realtime Database. Generates test cases from security rules, runs them against the Firebase Emulator Suite, validates access control for all user roles, checks for common vulnerabilities, and produces a coverage report showing which rules paths are tested.

## Purpose

Security rules are the primary defense for Firebase databases. Untested rules lead to two failure modes: (1) rules that are too permissive — users can access data they shouldn't, or (2) rules that are too restrictive — legitimate operations fail in production. This skill provides a systematic testing approach that catches both problems before deployment.

## When to Use This Skill

Use this skill when you need to:
- Test new or modified Firestore/RTDB security rules before deployment
- Validate that rules correctly enforce access control for all user roles
- Check rules for common vulnerability patterns
- Set up automated rules testing in CI/CD
- Generate a rules coverage report
- Debug rules that are rejecting legitimate operations

## When NOT to Use This Skill

Do NOT use this skill when:
- You need to write security rules from scratch (use the security rules generator prompt first)
- You need a full security audit beyond just rules (use firebase-security-auditor agent)
- Your app does not use Firestore or RTDB (Cloud Functions auth is tested differently)

## Prerequisites

- Firebase project with Firestore or RTDB security rules
- Firebase CLI installed (`firebase-tools`)
- Node.js 18+ installed
- `@firebase/rules-unit-testing` package (v3+)

## Step 1: Test Environment Setup

### 1.1 Install Dependencies

```bash
# Initialize test project
npm init -y
npm install --save-dev @firebase/rules-unit-testing firebase-admin jest ts-jest typescript @types/jest
```

### 1.2 Jest Configuration

```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  testTimeout: 30000,  // Rules tests can be slow on first run
  setupFilesAfterSetup: ['./tests/setup.ts'],
};
```

### 1.3 Test Setup

```typescript
// tests/setup.ts
import { initializeTestEnvironment, RulesTestEnvironment } from '@firebase/rules-unit-testing';
import { readFileSync } from 'fs';

let testEnv: RulesTestEnvironment;

export async function getTestEnv(): Promise<RulesTestEnvironment> {
  if (!testEnv) {
    testEnv = await initializeTestEnvironment({
      projectId: 'test-project',
      firestore: {
        rules: readFileSync('firestore.rules', 'utf8'),
        host: 'localhost',
        port: 8080,
      },
    });
  }
  return testEnv;
}

afterAll(async () => {
  if (testEnv) {
    await testEnv.cleanup();
  }
});
```

## Step 2: Test Case Generation

### 2.1 Role-Based Test Matrix

For each collection/path in your rules, generate tests for:

| Role | Test | Expected |
|------|------|----------|
| **Unauthenticated** | Read collection | DENY |
| **Unauthenticated** | Write collection | DENY |
| **Authenticated (owner)** | Read own document | ALLOW |
| **Authenticated (owner)** | Update own document | ALLOW |
| **Authenticated (owner)** | Delete own document | ALLOW or DENY (per rules) |
| **Authenticated (non-owner)** | Read other's document | Depends on rules |
| **Authenticated (non-owner)** | Update other's document | DENY |
| **Admin (custom claim)** | Read any document | ALLOW |
| **Admin (custom claim)** | Update any document | ALLOW |

### 2.2 Firestore Test Implementation

```typescript
// tests/firestore-rules.test.ts
import { getTestEnv } from './setup';
import { assertSucceeds, assertFails } from '@firebase/rules-unit-testing';
import { doc, getDoc, setDoc, updateDoc, deleteDoc, collection, getDocs } from 'firebase/firestore';

describe('Firestore Security Rules', () => {
  beforeEach(async () => {
    const testEnv = await getTestEnv();
    await testEnv.clearFirestore();
  });

  describe('/users/{userId}', () => {
    test('unauthenticated user cannot read any user document', async () => {
      const testEnv = await getTestEnv();
      const unauthed = testEnv.unauthenticatedContext();
      const userDoc = doc(unauthed.firestore(), 'users', 'user1');
      await assertFails(getDoc(userDoc));
    });

    test('authenticated user can read their own document', async () => {
      const testEnv = await getTestEnv();
      // Seed data
      await testEnv.withSecurityRulesDisabled(async (context) => {
        await setDoc(doc(context.firestore(), 'users', 'user1'), {
          displayName: 'Test User',
          email: 'test@example.com',
          createdAt: new Date(),
        });
      });

      const authed = testEnv.authenticatedContext('user1');
      const userDoc = doc(authed.firestore(), 'users', 'user1');
      await assertSucceeds(getDoc(userDoc));
    });

    test('authenticated user cannot read another user document', async () => {
      const testEnv = await getTestEnv();
      await testEnv.withSecurityRulesDisabled(async (context) => {
        await setDoc(doc(context.firestore(), 'users', 'user2'), {
          displayName: 'Other User',
          email: 'other@example.com',
          createdAt: new Date(),
        });
      });

      const authed = testEnv.authenticatedContext('user1');
      const userDoc = doc(authed.firestore(), 'users', 'user2');
      await assertFails(getDoc(userDoc));
    });

    test('user can create their own document with required fields', async () => {
      const testEnv = await getTestEnv();
      const authed = testEnv.authenticatedContext('user1');
      const userDoc = doc(authed.firestore(), 'users', 'user1');

      await assertSucceeds(setDoc(userDoc, {
        displayName: 'Test User',
        email: 'test@example.com',
        createdAt: new Date(), // serverTimestamp in real app
      }));
    });

    test('user cannot create document for another user', async () => {
      const testEnv = await getTestEnv();
      const authed = testEnv.authenticatedContext('user1');
      const userDoc = doc(authed.firestore(), 'users', 'user2');

      await assertFails(setDoc(userDoc, {
        displayName: 'Fake User',
        email: 'fake@example.com',
        createdAt: new Date(),
      }));
    });

    test('user cannot create document without required fields', async () => {
      const testEnv = await getTestEnv();
      const authed = testEnv.authenticatedContext('user1');
      const userDoc = doc(authed.firestore(), 'users', 'user1');

      await assertFails(setDoc(userDoc, {
        displayName: 'Test User',
        // Missing email and createdAt
      }));
    });

    test('user cannot update immutable fields (createdAt, uid)', async () => {
      const testEnv = await getTestEnv();
      await testEnv.withSecurityRulesDisabled(async (context) => {
        await setDoc(doc(context.firestore(), 'users', 'user1'), {
          displayName: 'Test User',
          email: 'test@example.com',
          createdAt: new Date(),
        });
      });

      const authed = testEnv.authenticatedContext('user1');
      const userDoc = doc(authed.firestore(), 'users', 'user1');

      await assertFails(updateDoc(userDoc, {
        createdAt: new Date(), // Immutable field
      }));
    });
  });

  describe('/items/{itemId}', () => {
    test('authenticated user can read any item', async () => {
      const testEnv = await getTestEnv();
      await testEnv.withSecurityRulesDisabled(async (context) => {
        await setDoc(doc(context.firestore(), 'items', 'item1'), {
          title: 'Test Item',
          ownerId: 'user2',
          createdAt: new Date(),
        });
      });

      const authed = testEnv.authenticatedContext('user1');
      await assertSucceeds(getDoc(doc(authed.firestore(), 'items', 'item1')));
    });

    test('owner can update their item', async () => {
      const testEnv = await getTestEnv();
      await testEnv.withSecurityRulesDisabled(async (context) => {
        await setDoc(doc(context.firestore(), 'items', 'item1'), {
          title: 'Test Item',
          ownerId: 'user1',
          createdAt: new Date(),
        });
      });

      const authed = testEnv.authenticatedContext('user1');
      await assertSucceeds(updateDoc(doc(authed.firestore(), 'items', 'item1'), {
        title: 'Updated Item',
      }));
    });

    test('non-owner cannot update item', async () => {
      const testEnv = await getTestEnv();
      await testEnv.withSecurityRulesDisabled(async (context) => {
        await setDoc(doc(context.firestore(), 'items', 'item1'), {
          title: 'Test Item',
          ownerId: 'user1',
          createdAt: new Date(),
        });
      });

      const authed = testEnv.authenticatedContext('user2');
      await assertFails(updateDoc(doc(authed.firestore(), 'items', 'item1'), {
        title: 'Hacked Item',
      }));
    });

    test('user cannot change item ownership', async () => {
      const testEnv = await getTestEnv();
      await testEnv.withSecurityRulesDisabled(async (context) => {
        await setDoc(doc(context.firestore(), 'items', 'item1'), {
          title: 'Test Item',
          ownerId: 'user1',
          createdAt: new Date(),
        });
      });

      const authed = testEnv.authenticatedContext('user1');
      await assertFails(updateDoc(doc(authed.firestore(), 'items', 'item1'), {
        ownerId: 'user2',
      }));
    });
  });

  describe('Vulnerability Checks', () => {
    test('default deny: unmatched paths are denied', async () => {
      const testEnv = await getTestEnv();
      const authed = testEnv.authenticatedContext('user1');

      // Try to access a collection that doesn't have explicit rules
      await assertFails(getDoc(doc(authed.firestore(), 'secretData', 'doc1')));
    });

    test('admin collection is denied even for authenticated users', async () => {
      const testEnv = await getTestEnv();
      const authed = testEnv.authenticatedContext('user1');
      await assertFails(getDoc(doc(authed.firestore(), 'admin', 'config')));
    });

    test('document size limit is enforced', async () => {
      const testEnv = await getTestEnv();
      const authed = testEnv.authenticatedContext('user1');

      // Create a very large document (>500KB)
      const largeContent = 'x'.repeat(600000);
      await assertFails(setDoc(doc(authed.firestore(), 'items', 'large'), {
        title: 'Large Item',
        content: largeContent,
        ownerId: 'user1',
        createdAt: new Date(),
      }));
    });
  });
});
```

## Step 3: Custom Claims Testing

```typescript
describe('Custom Claims (Admin)', () => {
  test('admin can read all users', async () => {
    const testEnv = await getTestEnv();
    await testEnv.withSecurityRulesDisabled(async (context) => {
      await setDoc(doc(context.firestore(), 'users', 'user2'), {
        displayName: 'Other User',
        email: 'other@example.com',
        createdAt: new Date(),
      });
    });

    // User with admin custom claim
    const admin = testEnv.authenticatedContext('admin1', {
      admin: true,
    });

    // If your rules check for custom claims like:
    // allow read: if request.auth.token.admin == true;
    // This test verifies admin access
  });
});
```

## Step 4: Running Tests

```bash
# Start emulators in background
firebase emulators:start --only firestore &

# Wait for emulators to start
sleep 5

# Run tests
npx jest --verbose

# Or run with coverage
npx jest --coverage

# Stop emulators
kill %1
```

### 4.1 CI Integration

```yaml
# .github/workflows/rules-test.yml
name: Test Firebase Rules
on:
  pull_request:
    paths:
      - 'firestore.rules'
      - 'storage.rules'
      - 'tests/**'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - uses: actions/setup-java@v4
        with: { java-version: '17', distribution: 'zulu' }
      - run: npm ci
      - run: npm install -g firebase-tools
      - run: firebase emulators:exec --only firestore "npx jest --ci --verbose"
        env:
          FIREBASE_PROJECT: test-project
```

## Step 5: Coverage Analysis

### 5.1 Rules Path Coverage

After running tests, analyze which rules paths are covered:

```
Coverage Report:
✅ /users/{userId} — read (owner): TESTED
✅ /users/{userId} — read (non-owner): TESTED
✅ /users/{userId} — create: TESTED
✅ /users/{userId} — update: TESTED
✅ /users/{userId} — delete: TESTED
✅ /users/{userId}/settings/{settingId}: TESTED
✅ /items/{itemId} — read: TESTED
✅ /items/{itemId} — create: TESTED
✅ /items/{itemId} — update (owner): TESTED
✅ /items/{itemId} — update (non-owner): TESTED
✅ /items/{itemId} — delete: TESTED
✅ /admin/{document} — read: TESTED
✅ Default deny: TESTED
⚠️ /items/{itemId} — create with admin claim: NOT TESTED
```

Target: 100% of rules paths with at least one ALLOW and one DENY test each.

## Vulnerability Checklist

Run these checks against every rules file:

- [ ] Default deny: unmatched paths return DENY
- [ ] All read operations require authentication (unless intentionally public)
- [ ] All write operations require authentication
- [ ] Users can only modify their own data (owner checks)
- [ ] Immutable fields cannot be changed (createdAt, ownerId, uid)
- [ ] Document size limits are enforced
- [ ] Field validation is present (type checks, length limits)
- [ ] Admin paths are inaccessible from client
- [ ] Wildcard rules (`{document=**}`) are not overly broad
- [ ] No `allow read, write: if true` in production rules

## Related Skills

- `firebase-project-scaffolding` - Initial setup that creates the rules being tested
- `firebase-security-auditor` - Agent for deep security review beyond rules
