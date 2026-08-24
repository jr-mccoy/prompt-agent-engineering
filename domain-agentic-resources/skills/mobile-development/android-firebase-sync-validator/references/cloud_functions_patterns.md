# Cloud Functions Patterns for Android Apps

## Overview

Cloud Functions for Firebase enable server-side logic that responds to Firebase events and HTTP requests. Common use cases for Android apps include data validation, cascade operations, notifications, and integrations.

## Firestore Triggers

### onCreate Pattern

Execute logic when a document is created:

```typescript
import * as functions from 'firebase-functions';
import * as admin from 'firebase-admin';

export const onUserCreate = functions.firestore
  .document('users/{userId}')
  .onCreate(async (snap, context) => {
    const userId = context.params.userId;
    const userData = snap.data();

    // Initialize user defaults
    await snap.ref.update({
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      photoURL: userData.photoURL || '/default-avatar.png',
      followersCount: 0,
      followingCount: 0
    });

    // Create related collections
    await admin.firestore()
      .collection('users').doc(userId)
      .collection('settings').doc('privacy')
      .set({
        profileVisibility: 'friends',
        showEmail: false,
        showPhone: false
      });

    // Send welcome notification
    await admin.firestore()
      .collection('notifications').add({
        userId: userId,
        type: 'welcome',
        title: 'Welcome to the app!',
        message: 'Thanks for joining us.',
        read: false,
        createdAt: admin.firestore.FieldValue.serverTimestamp()
      });

    return null;
  });
```

### onUpdate Pattern

Execute logic when a document is updated:

```typescript
export const onUserUpdate = functions.firestore
  .document('users/{userId}')
  .onUpdate(async (change, context) => {
    const before = change.before.data();
    const after = change.after.data();
    const userId = context.params.userId;

    // Detect meaningful changes
    const changedFields = Object.keys(after).filter(
      key => before[key] !== after[key]
    );

    if (changedFields.length === 0) {
      return null; // No changes
    }

    // Audit log
    await admin.firestore().collection('auditLogs').add({
      userId: userId,
      action: 'user_updated',
      changedFields: changedFields,
      before: before,
      after: after,
      timestamp: admin.firestore.FieldValue.serverTimestamp()
    });

    // Handle specific field changes
    if (changedFields.includes('displayName')) {
      // Update denormalized data
      await updateUserDisplayName(userId, after.displayName);
    }

    return null;
  });

async function updateUserDisplayName(userId: string, newName: string): Promise<void> {
  const batch = admin.firestore().batch();

  // Update all posts by this user
  const postsSnap = await admin.firestore()
    .collection('posts')
    .where('authorId', '==', userId)
    .get();

  postsSnap.docs.forEach(doc => {
    batch.update(doc.ref, { authorName: newName });
  });

  await batch.commit();
}
```

### onDelete Pattern

Execute cleanup when a document is deleted:

```typescript
export const onUserDelete = functions.firestore
  .document('users/{userId}')
  .onDelete(async (snap, context) => {
    const userId = context.params.userId;

    // Cascade delete user data
    const batch = admin.firestore().batch();

    // Delete user's posts
    const postsSnap = await admin.firestore()
      .collection('posts')
      .where('authorId', '==', userId)
      .get();

    postsSnap.docs.forEach(doc => batch.delete(doc.ref));

    // Delete user's comments
    const commentsSnap = await admin.firestore()
      .collection('comments')
      .where('authorId', '==', userId)
      .get();

    commentsSnap.docs.forEach(doc => batch.delete(doc.ref));

    // Delete user's settings
    const settingsSnap = await admin.firestore()
      .collection('users').doc(userId)
      .collection('settings')
      .get();

    settingsSnap.docs.forEach(doc => batch.delete(doc.ref));

    await batch.commit();

    // Delete from Authentication
    try {
      await admin.auth().deleteUser(userId);
    } catch (error) {
      console.error('Error deleting auth user:', error);
    }

    // Remove from any groups
    await removeUserFromGroups(userId);

    return null;
  });
```

## Realtime Database Triggers

### RTDB onCreate Pattern

```typescript
export const onMessageCreate = functions.database
  .ref('/chats/{chatId}/messages/{messageId}')
  .onCreate(async (snapshot, context) => {
    const message = snapshot.val();
    const chatId = context.params.chatId;
    const messageId = context.params.messageId;

    // Update last message in chat
    await admin.database()
      .ref(`/chats/${chatId}/lastMessage`)
      .set({
        text: message.text,
        senderId: message.senderId,
        timestamp: message.timestamp
      });

    // Increment unread count for recipients
    const chatSnap = await admin.database()
      .ref(`/chats/${chatId}`)
      .once('value');

    const chat = chatSnap.val();
    const recipients = Object.keys(chat.members || {})
      .filter(uid => uid !== message.senderId);

    const updates: {[key: string]: any} = {};
    recipients.forEach(recipientId => {
      updates[`/chats/${chatId}/unreadCount/${recipientId}`] =
        admin.database.ServerValue.increment(1);
    });

    await admin.database().ref().update(updates);

    // Send push notifications
    await sendMessageNotifications(recipients, message);

    return null;
  });
```

## Data Validation Pattern

Server-side validation for sensitive operations:

```typescript
export const validatePurchase = functions.https.onCall(async (data, context) => {
  // Require authentication
  if (!context.auth) {
    throw new functions.https.HttpsError(
      'unauthenticated',
      'User must be authenticated'
    );
  }

  const userId = context.auth.uid;
  const productId = data.productId;
  const quantity = data.quantity;

  // Validate input
  if (!productId || typeof productId !== 'string') {
    throw new functions.https.HttpsError(
      'invalid-argument',
      'Product ID is required'
    );
  }

  if (!quantity || quantity < 1 || quantity > 100) {
    throw new functions.https.HttpsError(
      'invalid-argument',
      'Quantity must be between 1 and 100'
    );
  }

  // Check product exists
  const productSnap = await admin.firestore()
    .collection('products')
    .doc(productId)
    .get();

  if (!productSnap.exists) {
    throw new functions.https.HttpsError(
      'not-found',
      'Product not found'
    );
  }

  const product = productSnap.data()!;

  // Check stock
  if (product.stock < quantity) {
    throw new functions.https.HttpsError(
      'failed-precondition',
      'Insufficient stock'
    );
  }

  // Check user balance
  const userSnap = await admin.firestore()
    .collection('users')
    .doc(userId)
    .get();

  const user = userSnap.data()!;
  const totalCost = product.price * quantity;

  if (user.balance < totalCost) {
    throw new functions.https.HttpsError(
      'failed-precondition',
      'Insufficient balance'
    );
  }

  // Process purchase
  const batch = admin.firestore().batch();

  // Deduct stock
  batch.update(productSnap.ref, {
    stock: admin.firestore.FieldValue.increment(-quantity)
  });

  // Deduct balance
  batch.update(userSnap.ref, {
    balance: admin.firestore.FieldValue.increment(-totalCost)
  });

  // Create order
  const orderRef = admin.firestore().collection('orders').doc();
  batch.set(orderRef, {
    userId: userId,
    productId: productId,
    quantity: quantity,
    totalCost: totalCost,
    status: 'confirmed',
    createdAt: admin.firestore.FieldValue.serverTimestamp()
  });

  await batch.commit();

  return { orderId: orderRef.id, success: true };
});
```

## Denormalization Pattern

Keep related data in sync:

```typescript
export const onPostUpdate = functions.firestore
  .document('posts/{postId}')
  .onUpdate(async (change, context) => {
    const before = change.before.data();
    const after = change.after.data();

    // Only update if title or content changed
    if (before.title === after.title && before.content === after.content) {
      return null;
    }

    const postId = context.params.postId;

    // Update denormalized post data in comments
    const commentsSnap = await admin.firestore()
      .collection('comments')
      .where('postId', '==', postId)
      .get();

    const batch = admin.firestore().batch();

    commentsSnap.docs.forEach(doc => {
      batch.update(doc.ref, {
        postTitle: after.title,
        postSnippet: after.content.substring(0, 200)
      });
    });

    await batch.commit();

    return null;
  });
```

## Aggregation Pattern

Maintain counts and aggregates:

```typescript
export const onCommentCreate = functions.firestore
  .document('posts/{postId}/comments/{commentId}')
  .onCreate(async (snap, context) => {
    const postId = context.params.postId;

    // Increment comment count on post
    await admin.firestore()
      .collection('posts')
      .doc(postId)
      .update({
        commentCount: admin.firestore.FieldValue.increment(1),
        lastCommentAt: admin.firestore.FieldValue.serverTimestamp()
      });

    return null;
  });

export const onCommentDelete = functions.firestore
  .document('posts/{postId}/comments/{commentId}')
  .onDelete(async (snap, context) => {
    const postId = context.params.postId;

    // Decrement comment count on post
    await admin.firestore()
      .collection('posts')
      .doc(postId)
      .update({
        commentCount: admin.firestore.FieldValue.increment(-1)
      });

    return null;
  });
```

## Scheduled Functions Pattern

Run periodic tasks:

```typescript
export const dailyCleanup = functions.pubsub
  .schedule('0 2 * * *') // 2 AM daily
  .timeZone('America/New_York')
  .onRun(async (context) => {
    const thirtyDaysAgo = admin.firestore.Timestamp.fromDate(
      new Date(Date.now() - 30 * 24 * 60 * 60 * 1000)
    );

    // Delete old notifications
    const oldNotificationsSnap = await admin.firestore()
      .collection('notifications')
      .where('createdAt', '<', thirtyDaysAgo)
      .where('read', '==', true)
      .get();

    const batch = admin.firestore().batch();
    oldNotificationsSnap.docs.forEach(doc => batch.delete(doc.ref));
    await batch.commit();

    console.log(`Deleted ${oldNotificationsSnap.size} old notifications`);

    return null;
  });
```

## Error Handling Pattern

Robust error handling and logging:

```typescript
export const processPayment = functions.https.onCall(async (data, context) => {
  try {
    // Validate authentication
    if (!context.auth) {
      throw new functions.https.HttpsError(
        'unauthenticated',
        'User must be authenticated'
      );
    }

    // Process payment
    const result = await processPaymentLogic(data, context.auth.uid);

    // Log success
    await admin.firestore().collection('paymentLogs').add({
      userId: context.auth.uid,
      status: 'success',
      amount: data.amount,
      timestamp: admin.firestore.FieldValue.serverTimestamp()
    });

    return result;

  } catch (error: any) {
    // Log error
    await admin.firestore().collection('paymentErrors').add({
      userId: context.auth?.uid || 'anonymous',
      error: error.message,
      stack: error.stack,
      data: data,
      timestamp: admin.firestore.FieldValue.serverTimestamp()
    });

    // Throw appropriate error
    if (error instanceof functions.https.HttpsError) {
      throw error;
    }

    throw new functions.https.HttpsError(
      'internal',
      'Payment processing failed',
      error
    );
  }
});
```

## Best Practices

### 1. Idempotency

Ensure functions can be safely retried:

```typescript
export const onOrderCreate = functions.firestore
  .document('orders/{orderId}')
  .onCreate(async (snap, context) => {
    const order = snap.data();
    const orderId = context.params.orderId;

    // Check if already processed (idempotency)
    if (order.processed) {
      console.log(`Order ${orderId} already processed`);
      return null;
    }

    // Process order
    await processOrder(order);

    // Mark as processed
    await snap.ref.update({ processed: true });

    return null;
  });
```

### 2. Batching

Use batched writes for efficiency:

```typescript
const batch = admin.firestore().batch();

// Add multiple operations
items.forEach(item => {
  const ref = admin.firestore().collection('items').doc(item.id);
  batch.set(ref, item);
});

// Execute all at once
await batch.commit();
```

### 3. Timeout Handling

Set appropriate timeouts:

```typescript
export const longRunningTask = functions
  .runWith({ timeoutSeconds: 540, memory: '2GB' })
  .https.onRequest(async (req, res) => {
    // Long-running logic
  });
```

### 4. Security

Always validate auth and input:

```typescript
export const secureFunction = functions.https.onCall(async (data, context) => {
  // Check authentication
  if (!context.auth) {
    throw new functions.https.HttpsError('unauthenticated', 'Not authenticated');
  }

  // Check authorization
  const userDoc = await admin.firestore()
    .collection('users')
    .doc(context.auth.uid)
    .get();

  if (!userDoc.data()?.isAdmin) {
    throw new functions.https.HttpsError('permission-denied', 'Not authorized');
  }

  // Validate input
  if (!data.requiredField) {
    throw new functions.https.HttpsError('invalid-argument', 'Missing field');
  }

  // Process request
});
```

## Resources

- [Cloud Functions Documentation](https://firebase.google.com/docs/functions)
- [Firestore Triggers](https://firebase.google.com/docs/functions/firestore-events)
- [RTDB Triggers](https://firebase.google.com/docs/functions/database-events)
- [Callable Functions](https://firebase.google.com/docs/functions/callable)
