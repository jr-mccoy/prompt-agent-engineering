# Firebase Rate Limit & Quota Management Prompts

Prompts for detecting and fixing Firebase Firestore and Realtime Database rate-limiting issues. Based on Firebase documented limits, HTTP 429 best practices, and common anti-patterns.

## Problem → Prompt Mapping

| # | Problem | Prompt | Difficulty |
|---|---------|--------|------------|
| 1 | Hit request quota / HTTP 429 — no retry or backoff | [firebase_rate_limit_retry_backoff.md](firebase_rate_limit_retry_backoff.md) | Intermediate |
| 2 | Hot document contention (global counters, shared docs) | [firebase_hot_document_contention.md](firebase_hot_document_contention.md) | Intermediate |
| 3 | Too many fine-grained writes (every keystroke, no batching) | [firebase_write_coalescing_batching.md](firebase_write_coalescing_batching.md) | Intermediate |
| 4 | N+1 reads and chatty client access patterns | [firebase_n_plus_one_read_patterns.md](firebase_n_plus_one_read_patterns.md) | Intermediate |
| 5 | Excessive real-time listeners (onSnapshot / RTDB .on()) | [firebase_excessive_listeners.md](firebase_excessive_listeners.md) | Intermediate |
| 6 | Thundering herd on startup / reconnection | [firebase_thundering_herd_prevention.md](firebase_thundering_herd_prevention.md) | Advanced |
| 7 | Bursty sync work done client-side instead of server | [firebase_bursty_sync_offloading.md](firebase_bursty_sync_offloading.md) | Advanced |
| 8 | RTDB concurrent connections / throughput limits | [firebase_rtdb_connection_scaling.md](firebase_rtdb_connection_scaling.md) | Advanced |
| 9 | No visibility into which operation causes rate limiting | [firebase_quota_monitoring_observability.md](firebase_quota_monitoring_observability.md) | Intermediate |

## Usage

Run any prompt against a codebase that uses Firebase. Each prompt will:

1. **Scan** the codebase for the specific anti-pattern
2. **Verify** findings before reporting (false-positive prevention built in)
3. **Prioritize** issues by severity and impact
4. **Provide** specific fixes with code examples

## Recommended Order

For a comprehensive Firebase rate-limit audit, run in this order:

1. **Monitoring first** (#9) — understand what you can see
2. **Retry/backoff** (#1) — ensure resilience basics are in place
3. **Hot documents** (#2) — find the worst write contention
4. **Write coalescing** (#3) — reduce unnecessary write volume
5. **N+1 reads** (#4) — fix chatty read patterns
6. **Excessive listeners** (#5) — reduce connection and read overhead
7. **Thundering herd** (#6) — prevent synchronized spikes
8. **Bursty offloading** (#7) — move heavy work server-side
9. **RTDB scaling** (#8) — plan for growth

## Firebase Documented Limits (Reference)

| Resource | Limit |
|----------|-------|
| Firestore writes per database | 10,000/sec |
| Firestore sustained writes per document | 1/sec |
| Firestore max concurrent connections | 1,000,000 |
| RTDB concurrent connections (Blaze) | 200,000 |
| RTDB write throughput | 1,000/sec |
| RTDB download bandwidth | 100 MB/sec |
| Firestore `in` query max IDs | 30 |
| Firestore batch write max operations | 500 |
