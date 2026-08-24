# Realtime Database Security Rules Patterns

Quick reference for common RTDB security rules patterns used in Android apps.

## Basic Structure

```json
{
  "rules": {
    // Rules go here
  }
}
```

## Authentication Patterns

### Require Any Authentication
```json
{
  "rules": {
    "publicData": {
      ".read": "auth != null",
      ".write": "auth != null"
    }
  }
}
```

### Require Specific User
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

### Require Email Verification
```json
{
  "rules": {
    "verifiedContent": {
      ".read": "auth != null && auth.token.email_verified == true"
    }
  }
}
```

### Require Custom Claims (Admin)
```json
{
  "rules": {
    "adminPanel": {
      ".read": "auth != null && auth.token.admin == true",
      ".write": "auth != null && auth.token.admin == true"
    }
  }
}
```

## Data Access Patterns

### Private (Owner Only)
```json
{
  "rules": {
    "users": {
      "$userId": {
        "private": {
          ".read": "auth.uid == $userId",
          ".write": "auth.uid == $userId"
        }
      }
    }
  }
}
```

### Shared (Group Members)
```json
{
  "rules": {
    "groups": {
      "$groupId": {
        ".read": "root.child('groups').child($groupId).child('members').child(auth.uid).exists()",
        ".write": "root.child('groups').child($groupId).child('admins').child(auth.uid).exists()"
      }
    }
  }
}
```

### Public Read, Private Write
```json
{
  "rules": {
    "posts": {
      "$postId": {
        ".read": "auth != null",
        ".write": "auth.uid == data.child('authorId').val() || !data.exists()"
      }
    }
  }
}
```

## Data Validation Patterns

### Required Fields
```json
{
  "rules": {
    "posts": {
      "$postId": {
        ".validate": "newData.hasChildren(['title', 'content', 'authorId'])"
      }
    }
  }
}
```

### Field Types and Length
```json
{
  "rules": {
    "users": {
      "$userId": {
        "displayName": {
          ".validate": "newData.isString() && newData.val().length >= 2 && newData.val().length <= 50"
        },
        "age": {
          ".validate": "newData.isNumber() && newData.val() >= 13 && newData.val() <= 120"
        },
        "email": {
          ".validate": "newData.isString() && newData.val().matches(/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}$/i)"
        }
      }
    }
  }
}
```

### Immutable Fields
```json
{
  "rules": {
    "posts": {
      "$postId": {
        "authorId": {
          ".validate": "!data.exists() || data.val() == newData.val()"
        },
        "createdAt": {
          ".validate": "!data.exists() || data.val() == newData.val()"
        }
      }
    }
  }
}
```

### Server Timestamp
```json
{
  "rules": {
    "posts": {
      "$postId": {
        "timestamp": {
          ".validate": "newData.val() == now"
        }
      }
    }
  }
}
```

## Advanced Patterns

### Cross-Path Reference
```json
{
  "rules": {
    "comments": {
      "$commentId": {
        ".write": "root.child('posts').child(newData.child('postId').val()).exists()"
      }
    }
  }
}
```

### Cascade Read Access
```json
{
  "rules": {
    "groups": {
      "$groupId": {
        "messages": {
          ".read": "root.child('groups').child($groupId).child('members').child(auth.uid).exists()",
          "$messageId": {
            ".write": "root.child('groups').child($groupId).child('members').child(auth.uid).exists()"
          }
        }
      }
    }
  }
}
```

### Incremental Counter
```json
{
  "rules": {
    "posts": {
      "$postId": {
        "likes": {
          "$userId": {
            ".write": "auth.uid == $userId && (!data.exists() || data.val() == false) && newData.val() == true"
          }
        },
        "likesCount": {
          ".validate": "newData.isNumber() && (newData.val() == data.val() + 1 || newData.val() == data.val() - 1)"
        }
      }
    }
  }
}
```

## Common Android Use Cases

### User Profile
```json
{
  "rules": {
    "users": {
      "$userId": {
        ".read": "auth != null",
        ".write": "auth.uid == $userId",
        ".validate": "newData.hasChildren(['displayName', 'email'])",
        "displayName": {
          ".validate": "newData.isString() && newData.val().length >= 2 && newData.val().length <= 50"
        },
        "email": {
          ".validate": "newData.isString() && newData.val().matches(/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}$/i)"
        },
        "photoURL": {
          ".validate": "newData.isString()"
        },
        "bio": {
          ".validate": "newData.isString() && newData.val().length <= 500"
        }
      }
    }
  }
}
```

### Chat Messages
```json
{
  "rules": {
    "chats": {
      "$chatId": {
        ".read": "root.child('chats').child($chatId).child('participants').child(auth.uid).exists()",
        "messages": {
          "$messageId": {
            ".write": "root.child('chats').child($chatId).child('participants').child(auth.uid).exists()",
            ".validate": "newData.hasChildren(['senderId', 'text', 'timestamp'])",
            "senderId": {
              ".validate": "newData.val() == auth.uid"
            },
            "text": {
              ".validate": "newData.isString() && newData.val().length > 0 && newData.val().length <= 5000"
            },
            "timestamp": {
              ".validate": "newData.val() == now"
            }
          }
        }
      }
    }
  }
}
```

### Presence System
```json
{
  "rules": {
    "presence": {
      "$userId": {
        ".read": "auth != null",
        ".write": "auth.uid == $userId",
        "status": {
          ".validate": "newData.isString() && (newData.val() == 'online' || newData.val() == 'offline' || newData.val() == 'away')"
        },
        "lastSeen": {
          ".validate": "newData.val() == now"
        }
      }
    }
  }
}
```

### Notifications
```json
{
  "rules": {
    "notifications": {
      "$userId": {
        "$notificationId": {
          ".read": "auth.uid == $userId",
          ".write": "false",
          "read": {
            ".write": "auth.uid == $userId",
            ".validate": "newData.isBoolean()"
          }
        }
      }
    }
  }
}
```

### Rate Limiting
```json
{
  "rules": {
    "posts": {
      "$userId": {
        ".write": "!root.child('rateLimits').child(auth.uid).child('lastPost').exists() || root.child('rateLimits').child(auth.uid).child('lastPost').val() < (now - 60000)"
      }
    },
    "rateLimits": {
      "$userId": {
        "lastPost": {
          ".write": "auth.uid == $userId",
          ".validate": "newData.val() == now"
        }
      }
    }
  }
}
```

## Security Anti-Patterns

### ❌ Allow All
```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

### ❌ Auth-Only Check (Too Permissive)
```json
{
  "rules": {
    "users": {
      ".read": "auth != null",
      ".write": "auth != null"
    }
  }
}
```

### ❌ No Validation
```json
{
  "rules": {
    "data": {
      "$key": {
        ".write": "auth != null"
        // Missing .validate rules
      }
    }
  }
}
```

## Testing Patterns

### Test Setup
```javascript
import { assertFails, assertSucceeds } from '@firebase/rules-unit-testing';

test('user can write own data', async () => {
  const db = getDatabase({ uid: 'user123' });
  await assertSucceeds(db.ref('users/user123').set({ name: 'Test' }));
});

test('user cannot write other user data', async () => {
  const db = getDatabase({ uid: 'user123' });
  await assertFails(db.ref('users/user456').set({ name: 'Test' }));
});
```

## Performance Tips

1. **Index your data** - Use `.indexOn` for queries:
```json
{
  "rules": {
    "posts": {
      ".indexOn": ["timestamp", "authorId"]
    }
  }
}
```

2. **Shallow queries** - Structure data to minimize reads
3. **Denormalize** - Duplicate data for faster access
4. **Limit rule complexity** - Simple rules evaluate faster
