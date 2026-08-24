# Firestore Security Rules Patterns

Quick reference for common Firestore security rules patterns used in Android apps.

## Basic Structure

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Rules go here
  }
}
```

## Authentication Patterns

### Require Any Authentication
```
match /publicData/{document} {
  allow read: if request.auth != null;
}
```

### Require Specific User
```
match /users/{userId} {
  allow read, write: if request.auth.uid == userId;
}
```

### Require Email Verification
```
match /verifiedContent/{document} {
  allow read: if request.auth != null && request.auth.token.email_verified;
}
```

### Require Custom Claims (Admin)
```
match /adminPanel/{document} {
  allow read, write: if request.auth.token.admin == true;
}
```

## Data Access Patterns

### Private (Owner Only)
```
match /users/{userId}/private/{document} {
  allow read, write: if request.auth.uid == userId;
}
```

### Shared (Group Members)
```
match /groups/{groupId} {
  allow read: if request.auth.uid in resource.data.members;
  allow write: if request.auth.uid in resource.data.admins;
}
```

### Public Read, Private Write
```
match /posts/{postId} {
  allow read: if request.auth != null;
  allow create: if request.auth != null;
  allow update, delete: if request.auth.uid == resource.data.authorId;
}
```

## Data Validation Patterns

### Required Fields
```
match /posts/{postId} {
  allow create: if request.resource.data.keys().hasAll(['title', 'content', 'authorId', 'createdAt']);
}
```

### Field Types
```
match /posts/{postId} {
  allow create: if request.resource.data.title is string
    && request.resource.data.content is string
    && request.resource.data.authorId is string
    && request.resource.data.createdAt is timestamp
    && request.resource.data.likesCount is int;
}
```

### Field Length/Range
```
match /posts/{postId} {
  allow create: if request.resource.data.title.size() >= 3
    && request.resource.data.title.size() <= 200
    && request.resource.data.content.size() <= 10000
    && request.resource.data.likesCount >= 0;
}
```

### Immutable Fields
```
match /posts/{postId} {
  allow update: if !request.resource.data.diff(resource.data).affectedKeys().hasAny(['authorId', 'createdAt']);
}
```

### Server Timestamp
```
match /posts/{postId} {
  allow create: if request.resource.data.createdAt == request.time;
  allow update: if request.resource.data.updatedAt == request.time;
}
```

## Advanced Patterns

### Cross-Document Reference
```
match /comments/{commentId} {
  allow create: if exists(/databases/$(database)/documents/posts/$(request.resource.data.postId));
}
```

### Member List Validation
```
match /groups/{groupId} {
  allow read: if request.auth.uid in get(/databases/$(database)/documents/groups/$(groupId)).data.members;
}
```

### Rate Limiting
```
match /posts/{postId} {
  allow create: if request.auth != null
    && request.time > resource.data.lastPostTime + duration.value(1, 'm');
}
```

### Conditional Update
```
match /posts/{postId} {
  allow update: if request.resource.data.status == 'published'
    && resource.data.status == 'draft'
    && request.auth.uid == resource.data.authorId;
}
```

## Common Android Use Cases

### User Profile
```
match /users/{userId} {
  allow read: if request.auth != null;
  allow create: if request.auth.uid == userId
    && request.resource.data.keys().hasAll(['displayName', 'email', 'photoURL', 'createdAt'])
    && request.resource.data.displayName is string
    && request.resource.data.displayName.size() >= 2
    && request.resource.data.email is string
    && request.resource.data.photoURL is string
    && request.resource.data.createdAt == request.time;
  allow update: if request.auth.uid == userId
    && !request.resource.data.diff(resource.data).affectedKeys().hasAny(['email', 'createdAt']);
}
```

### Chat Messages
```
match /chats/{chatId}/messages/{messageId} {
  allow read: if request.auth.uid in get(/databases/$(database)/documents/chats/$(chatId)).data.participants;
  allow create: if request.auth.uid in get(/databases/$(database)/documents/chats/$(chatId)).data.participants
    && request.resource.data.senderId == request.auth.uid
    && request.resource.data.text is string
    && request.resource.data.text.size() > 0
    && request.resource.data.text.size() <= 5000
    && request.resource.data.timestamp == request.time;
}
```

### Following/Followers
```
match /users/{userId}/following/{followingId} {
  allow read: if request.auth != null;
  allow create: if request.auth.uid == userId;
  allow delete: if request.auth.uid == userId;
}

match /users/{userId}/followers/{followerId} {
  allow read: if request.auth != null;
  // Followers are managed by Cloud Functions
  allow write: if false;
}
```

### Notifications
```
match /users/{userId}/notifications/{notificationId} {
  allow read: if request.auth.uid == userId;
  allow update: if request.auth.uid == userId
    && request.resource.data.diff(resource.data).affectedKeys().hasOnly(['read']);
  // Notifications are created by Cloud Functions
  allow create, delete: if false;
}
```

## Testing Patterns

### Test Setup
```javascript
import { assertFails, assertSucceeds } from '@firebase/rules-unit-testing';

test('user can read own profile', async () => {
  const db = getFirestore({ uid: 'user123' });
  await assertSucceeds(db.collection('users').doc('user123').get());
});

test('user cannot read other profiles', async () => {
  const db = getFirestore({ uid: 'user123' });
  await assertFails(db.collection('users').doc('user456').get());
});
```
