# Firebase Security Rules Best Practices

## Overview

Firebase Security Rules provide server-side security for Firebase Realtime Database and Cloud Firestore. Rules determine who has read and write access to your database and how data is structured.

## Core Principles

### 1. Default Deny

Always start with denying all access, then explicitly grant access:

**Firestore:**
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Default deny
    match /{document=**} {
      allow read, write: if false;
    }

    // Explicit grants below
  }
}
```

**RTDB:**
```json
{
  "rules": {
    ".read": false,
    ".write": false
  }
}
```

### 2. Require Authentication

Never allow unauthenticated access unless absolutely necessary:

**Firestore:**
```
allow read, write: if request.auth != null;
```

**RTDB:**
```json
".read": "auth != null",
".write": "auth != null"
```

### 3. Principle of Least Privilege

Grant minimum necessary permissions:
- Private data: Only owner can access
- Shared data: Only members can access
- Public data: Authenticated users can read, owner can write

## Privacy Patterns

### Private Data (User-Owned)

**Firestore:**
```
match /users/{userId} {
  allow read, write: if request.auth.uid == userId;
}

match /users/{userId}/privateData/{document} {
  allow read, write: if request.auth.uid == userId;
}
```

**RTDB:**
```json
{
  "rules": {
    "users": {
      "$userId": {
        ".read": "auth.uid == $userId",
        ".write": "auth.uid == $userId"
      }
    }
  }
}
```

### Shared Data (Group Access)

**Firestore:**
```
match /groups/{groupId} {
  allow read: if request.auth.uid in resource.data.members;
  allow write: if request.auth.uid in resource.data.admins;
}

match /groups/{groupId}/messages/{messageId} {
  allow read: if request.auth.uid in get(/databases/$(database)/documents/groups/$(groupId)).data.members;
  allow create: if request.auth.uid in get(/databases/$(database)/documents/groups/$(groupId)).data.members;
  allow update, delete: if request.auth.uid == resource.data.authorId;
}
```

**RTDB:**
```json
{
  "rules": {
    "groups": {
      "$groupId": {
        ".read": "root.child('groups').child($groupId).child('members').child(auth.uid).exists()",
        "messages": {
          "$messageId": {
            ".write": "root.child('groups').child($groupId).child('members').child(auth.uid).exists()"
          }
        }
      }
    }
  }
}
```

### Public Data (Read-Only for Most)

**Firestore:**
```
match /posts/{postId} {
  allow read: if request.auth != null;
  allow create: if request.auth != null;
  allow update, delete: if request.auth.uid == resource.data.authorId;
}
```

**RTDB:**
```json
{
  "rules": {
    "posts": {
      "$postId": {
        ".read": "auth != null",
        ".write": "auth.uid == data.child('authorId').val()"
      }
    }
  }
}
```

## Data Validation

### Validate Data Structure

**Firestore:**
```
match /users/{userId} {
  allow create: if request.auth.uid == userId
    && request.resource.data.keys().hasAll(['name', 'email', 'createdAt'])
    && request.resource.data.name is string
    && request.resource.data.email is string
    && request.resource.data.createdAt is timestamp;

  allow update: if request.auth.uid == userId
    && request.resource.data.diff(resource.data).affectedKeys()
        .hasOnly(['name', 'profilePicture', 'bio']);
}
```

**RTDB:**
```json
{
  "rules": {
    "users": {
      "$userId": {
        ".validate": "newData.hasChildren(['name', 'email'])",
        "name": {
          ".validate": "newData.isString() && newData.val().length > 0 && newData.val().length <= 100"
        },
        "email": {
          ".validate": "newData.isString() && newData.val().matches(/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}$/i)"
        }
      }
    }
  }
}
```

### Prevent Field Tampering

**Firestore:**
```
match /posts/{postId} {
  // Don't allow changing authorId or createdAt
  allow update: if request.auth.uid == resource.data.authorId
    && !request.resource.data.diff(resource.data).affectedKeys().hasAny(['authorId', 'createdAt']);
}
```

### Validate Data Types and Ranges

**Firestore:**
```
match /products/{productId} {
  allow create: if request.resource.data.price is number
    && request.resource.data.price >= 0
    && request.resource.data.price <= 1000000
    && request.resource.data.name is string
    && request.resource.data.name.size() >= 3
    && request.resource.data.name.size() <= 200;
}
```

## Security Anti-Patterns

### ❌ DON'T: Allow All Access

```
// NEVER DO THIS
allow read, write: if true;
```

### ❌ DON'T: Trust Client Data for Authorization

```
// NEVER DO THIS - client can set isAdmin to true
allow write: if request.resource.data.isAdmin == true;

// Instead, check server-side auth token
allow write: if request.auth.token.admin == true;
```

### ❌ DON'T: Use Weak Authentication Checks

```
// TOO WEAK
allow read, write: if request.auth != null;

// BETTER - verify ownership
allow read, write: if request.auth.uid == userId;
```

### ❌ DON'T: Expose Sensitive Data in Public Paths

```
// BAD - passwords in user profile
match /users/{userId} {
  allow read: if request.auth != null; // Anyone can read passwords!
}

// GOOD - separate sensitive data
match /users/{userId} {
  allow read: if request.auth != null;
}
match /users/{userId}/private/credentials {
  allow read: if request.auth.uid == userId;
}
```

## Performance Considerations

### Minimize Rule Complexity

Complex rules are slower to evaluate:

```
// SLOW - multiple get() calls
allow read: if request.auth.uid in get(/databases/$(database)/documents/groups/$(groupId)).data.members
  && get(/databases/$(database)/documents/users/$(request.auth.uid)).data.verified == true;

// FASTER - cache in custom claims
allow read: if request.auth.uid in resource.data.members
  && request.auth.token.verified == true;
```

### Use Wildcards Efficiently

```
// INEFFICIENT
match /users/{userId}/posts/{postId} {
  allow read: if request.auth.uid == userId;
}
match /users/{userId}/comments/{commentId} {
  allow read: if request.auth.uid == userId;
}

// BETTER
match /users/{userId}/{collection}/{document} {
  allow read: if request.auth.uid == userId;
}
```

## Testing Security Rules

### Use Firebase Emulator Suite

```bash
firebase emulators:start --only firestore
```

### Write Security Rules Unit Tests

```javascript
import { assertFails, assertSucceeds } from '@firebase/rules-unit-testing';

test('user can read own data', async () => {
  const db = getFirestore(myAuth);
  await assertSucceeds(db.collection('users').doc(myAuth.uid).get());
});

test('user cannot read other user data', async () => {
  const db = getFirestore(myAuth);
  await assertFails(db.collection('users').doc('otherUserId').get());
});
```

## Common Patterns Reference

### Pattern: Cascade Delete Protection

Prevent deleting parent if children exist:

**Firestore:**
```
match /groups/{groupId} {
  allow delete: if !exists(/databases/$(database)/documents/groups/$(groupId)/messages/$(messageId));
}
```

### Pattern: Rate Limiting

Prevent spam by limiting writes:

**Firestore:**
```
match /posts/{postId} {
  allow create: if request.auth != null
    && request.time > resource.data.lastPostTime + duration.value(1, 'm');
}
```

### Pattern: Conditional Visibility

Show data based on user role:

**Firestore:**
```
match /sensitiveData/{documentId} {
  allow read: if request.auth.token.role in ['admin', 'moderator'];
}
```

### Pattern: Audit Trail

Require audit fields on writes:

**Firestore:**
```
match /documents/{documentId} {
  allow update: if request.resource.data.modifiedBy == request.auth.uid
    && request.resource.data.modifiedAt == request.time;
}
```

## Resources

- [Firebase Security Rules Documentation](https://firebase.google.com/docs/rules)
- [Firestore Security Rules Reference](https://firebase.google.com/docs/firestore/security/rules-structure)
- [RTDB Security Rules Reference](https://firebase.google.com/docs/database/security)
- [Security Rules Testing](https://firebase.google.com/docs/rules/unit-tests)
