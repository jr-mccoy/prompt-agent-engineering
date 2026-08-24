# Data Routing Decision Tree

## Choosing the Right Backend for Each Data Type

Use this decision tree to determine whether a given data type should be stored in Room (local only), Firebase Realtime Database, Cloud Firestore, or a combination.

```
Does this data need to sync across devices/users?
│
├── NO → Room only
│   Examples: app settings, notification history, local caches,
│   device-specific preferences, location reminder geofences
│
└── YES → Does it need sub-second real-time updates?
    │
    ├── YES → Firebase Realtime Database + Room cache
    │   Examples: chat messages, typing indicators, presence/online
    │   status, live counters, real-time collaboration cursors
    │
    │   Why RTDB: Lower latency for frequent small updates,
    │   efficient fan-out, optimized for real-time listeners
    │
    └── NO → Does it need complex queries (filtering, sorting, pagination)?
        │
        ├── YES → Cloud Firestore + Room cache
        │   Examples: calendar events (date range queries), tasks
        │   (filter by status/priority), shopping lists (shared with
        │   ordering), user profiles (search by field), leaderboards
        │
        │   Why Firestore: Rich query support, compound indexes,
        │   collection group queries, server-side pagination,
        │   strong consistency, offline persistence built-in
        │
        └── NO → Cloud Firestore + Room cache (default)
            Firestore is the default choice for synced data that
            doesn't need sub-second updates. It scales better,
            has richer querying, and integrates with Cloud Functions.
```

## Decision Matrix

| Question | Room Only | RTDB + Room | Firestore + Room |
|----------|-----------|-------------|------------------|
| Needs cross-device sync? | No | Yes | Yes |
| Needs sub-second updates? | N/A | Yes | No |
| Needs complex queries? | Yes (local) | No | Yes |
| Needs offline editing? | Yes | Limited | Yes |
| Write frequency | Any | High (>1/sec) | Low-Medium |
| Data structure | Relational | JSON tree | Document/Collection |
| Consistency model | Strong (local) | Eventual | Strong |
| Cost model | Free (local) | Per connection + bandwidth | Per read/write/storage |

## Feature-to-Backend Mapping Template

For each feature in your app, fill in this table:

| Feature | Data Type | Source of Truth | Cache | Sync Direction | Conflict Strategy |
|---------|-----------|----------------|-------|----------------|-------------------|
| Messaging | Messages | RTDB | Room | Bidirectional | Server-wins (ordered) |
| Messaging | Typing status | RTDB | None | Bidirectional | Last-write-wins |
| Calendars | Events | Firestore | Room | Bidirectional | Last-write-wins |
| Tasks | Task items | Firestore | Room | Bidirectional | Last-write-wins |
| Shopping | Lists + items | Firestore | Room | Bidirectional | Merge (union items) |
| Weather | Forecasts | External API | Room (TTL) | One-way (pull) | Replace on refresh |
| Location | Geofences | Room | Room | None | N/A (local only) |
| Gamification | Scores | Firestore | Room | Bidirectional | Max-wins |
| Gamification | Achievements | Firestore | Room | Bidirectional | OR-merge (earned=true) |
| Profile | User data | Firestore | Room | Bidirectional | Last-write-wins |
| Settings | Preferences | Room/DataStore | N/A | None | N/A (local only) |
| Notifications | History | Room | N/A | None | N/A (local only) |

## Cost Implications

### RTDB Pricing
- Charged per GB stored + GB downloaded
- Simultaneous connections matter (100K free, then $0.06/GB)
- Best for: small, frequently-changing data (presence, typing, counters)
- Avoid for: large documents, complex queries, data you read infrequently

### Firestore Pricing
- Charged per document read/write/delete + storage
- Free tier: 50K reads, 20K writes, 20K deletes per day
- Best for: structured data read occasionally, complex queries
- Avoid for: very high-frequency writes (>1/sec per document), real-time counters

### Room (Local)
- Free — no server costs
- Storage limited by device
- Best for: caching, offline access, device-local data
- Avoid for: data that needs cross-device availability (obviously)

## Anti-Patterns

### Using RTDB for Everything
RTDB has no native complex querying. Filtering tasks by status, date range, and priority requires client-side filtering or denormalized indexes. Use Firestore for query-heavy data.

### Using Firestore for Chat Messages
Firestore charges per read. A chat room with 100 messages read by 50 users = 5,000 reads per view. RTDB charges per bandwidth, which is cheaper for this pattern.

### Skipping Room Cache
Even with Firestore's built-in offline persistence, Room provides faster local queries, complex joins, and FTS (full-text search). Use Room as the primary read source for UI.

### Single Repository for All Data
Don't put Room, RTDB, and Firestore access in one god repository. Each feature should have its own repository that internally uses the appropriate backend.
