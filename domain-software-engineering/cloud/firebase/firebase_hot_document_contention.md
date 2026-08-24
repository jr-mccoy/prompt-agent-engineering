---
title: "Firebase Hot Document Contention Detection"
category: cloud/firebase
description: "Find Firestore documents receiving excessive concurrent writes that cause contention and throughput bottlenecks"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - firebase
  - firestore
  - hot-document
  - contention
  - sharding
  - counters
  - write-throughput
updated: "2026-02-28"
related_prompts:
  - domain-software-engineering/cloud/firebase/firebase_rate_limit_retry_backoff.md
  - domain-software-engineering/cloud/firebase/firebase_write_coalescing_batching.md
  - domain-software-engineering/analysis/performance/performance_bottleneck_identification.md
---

# Firebase Hot Document Contention Detection

**Objective:** Identify Firestore documents that receive frequent concurrent writes (hot documents), which cause write contention, increased latency, and throughput limits per Firestore's documented 1 write/second/document sustained limit.

**When to Use:** Use when Firestore writes show increased latency or `ABORTED` / `RESOURCE_EXHAUSTED` errors, or when reviewing data models for scalability before launch.

**Instructions:**

1. **Map the Firestore data model**
   - Identify all document paths written to by the application (client-side and server-side).
   - For each document path, determine whether the path is unique per entity (e.g., `users/{uid}`) or shared/singleton (e.g., `config/global`, `counters/pageViews`).
   - Flag any document path that multiple clients or functions write to concurrently.

2. **Identify hot document anti-patterns**
   Scan for these specific patterns:

   a. **Global counters** — A single document incremented by many writers:
      - `increment()` on a shared document (e.g., `stats/global`, `counters/visits`)
      - Any `FieldValue.increment()` or `FieldValue.arrayUnion()` on a document written by multiple users

   b. **Last-sync / presence documents** — A single document updated by every client:
      - `lastSync`, `lastActive`, `heartbeat` fields on a shared document
      - Presence tracking that writes to a shared collection document

   c. **Queue-head documents** — A single document used as a queue pointer or lock:
      - Distributed lock patterns writing to the same document
      - Job queue status documents updated by multiple workers

   d. **Aggregation documents** — Real-time aggregation written to by transactions:
      - Running totals, averages, or counts in a single document
      - Leaderboard top-N in a single document updated by many players

   e. **Config/feature-flag documents** — Frequently updated shared configuration

3. **Estimate write frequency per document**
   - For each suspected hot document, trace all code paths that write to it.
   - Estimate writes/second under peak load (concurrent users × write frequency per user).
   - Flag any document exceeding **1 sustained write/second** (Firestore's documented limit).

4. **Evaluate existing mitigations**
   - Check if sharded counter patterns are already implemented.
   - Check if writes are debounced or batched before hitting the shared document.
   - Check if the data model uses subcollections or append-only patterns to distribute load.

5. **Recommend fixes for each hot document**
   - Provide specific sharding or data model alternatives.
   - Estimate the improvement (e.g., 10 shards = 10x write throughput).
   - Include migration path if data model changes are needed.

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT flag documents written by a single user at a time (e.g., `users/{uid}/profile`) — these aren't hot documents.
- ❌ Do NOT flag `increment()` calls on per-user or per-entity documents where contention is low.
- ❌ Do NOT flag documents only written by a single Cloud Function instance at a time.
- ❌ Do NOT flag batch-import or migration scripts that run one-time.
- ✅ DO verify the document is written to by **multiple concurrent writers** before flagging.
- ✅ DO estimate actual write frequency — a counter incremented once per hour is fine.
- ✅ DO check if sharded counter patterns are already in place before recommending them.

**Expected Output:** A report listing every hot document with:

- Document path pattern
- All code locations that write to it
- Estimated writes/second at peak
- Contention risk (Critical / High / Medium)
- Recommended fix with code example

**Example Output:**

```markdown
## Firestore Hot Document Contention Report

### Executive Summary
Found **4 hot documents** with sustained write rates exceeding Firestore's 1 write/sec/doc limit. The global analytics counter is the most critical, receiving an estimated **120 writes/second** at peak.

### Critical (Sustained >10 writes/sec)

#### 1. Global Page View Counter
**Document:** `counters/pageViews`
**Estimated Peak:** ~120 writes/sec
**Writers:**
- `src/analytics/tracker.ts:45` — Client-side, fires on every page navigation
- `functions/src/analytics.ts:23` — Cloud Function triggered on page_view events

**Current Code:**
```typescript
// Every page view writes to the same document
await updateDoc(doc(db, 'counters', 'pageViews'), {
  total: increment(1),
  lastUpdated: serverTimestamp(),
});
```

**Fix — Sharded Counter (10 shards = 10x throughput):**
```typescript
// Write to a random shard
const shardId = Math.floor(Math.random() * 10);
await updateDoc(doc(db, 'counters/pageViews/shards', `${shardId}`), {
  count: increment(1),
});

// Read: aggregate all shards
async function getTotalPageViews(): Promise<number> {
  const shards = await getDocs(collection(db, 'counters/pageViews/shards'));
  return shards.docs.reduce((total, shard) => total + shard.data().count, 0);
}
```

**Estimated Improvement:** 120 writes/sec → 12 writes/sec/shard (within limits)

### High (Sustained 2-10 writes/sec)

#### 2. User Presence Document
**Document:** `presence/online`
**Estimated Peak:** ~8 writes/sec
**Writers:**
- `src/presence/heartbeat.ts:22` — Every active client writes every 30 seconds

**Fix — Per-User Presence Documents:**
```typescript
// Instead of a shared document, write to per-user docs
await setDoc(doc(db, 'presence', currentUser.uid), {
  online: true,
  lastSeen: serverTimestamp(),
});

// Query online users
const onlineUsers = await getDocs(
  query(collection(db, 'presence'),
    where('online', '==', true),
    where('lastSeen', '>', thirtySecondsAgo)
  )
);
```

### Summary Table

| Document Path | Peak Writes/sec | Risk | Fix |
|--------------|----------------|------|-----|
| counters/pageViews | ~120 | Critical | Sharded counter (10 shards) |
| presence/online | ~8 | High | Per-user presence docs |
| config/featureFlags | ~3 | Medium | Cache + reduce write frequency |
| leaderboard/top10 | ~5 | High | Append-only + periodic aggregation |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — Focused on hot document detection
- ST-02 (Structured Sequential Instructions) — Systematic data model mapping
- RT-02 (Multi-Dimensional Analysis) — Covers counters, presence, queues, aggregation
- RT-05 (Evidence-Based Reasoning) — Requires write frequency estimates and code evidence
- DS-06 (Prioritization Guidance) — Ranked by writes/sec and contention risk
- QA-01 (Chain-of-Verification) — Verify concurrent writers before flagging
