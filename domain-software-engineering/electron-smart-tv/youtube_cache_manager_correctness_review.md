---
title: "YouTube Cache Manager Correctness & Edge Case Review"
category: software-engineering/electron-smart-tv
description: "Review a JSON-backed YouTube cache manager for data integrity, incremental refresh correctness, quota accounting accuracy, cache eviction edge cases, and concurrent access safety."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - QA-01  # Chain-of-Verification
difficulty: advanced
tags:
  - caching
  - youtube-api
  - data-integrity
  - json-database
  - quota-management
  - edge-cases
updated: "2026-02-19"
related_prompts:
  - domain-software-engineering/electron-smart-tv/api_quota_strategy_rate_limiting_review.md
  - domain-software-engineering/electron-smart-tv/network_resilience_offline_graceful_degradation.md
---

# YouTube Cache Manager Correctness & Edge Case Review

**Objective:** Analyze a JSON-backed YouTube cache manager for correctness of incremental refresh logic, checkpoint integrity, quota tracking accuracy, cache eviction behavior, and resilience to crashes, partial writes, and concurrent access from scheduled refreshes and renderer IPC requests.

---

## When to Use

- Use when: Building or modifying a local JSON cache that stores YouTube video metadata for offline search
- Use when: The cache uses checkpoint-based incremental fetching (`last_seen_video_id`) to minimize API calls
- Use when: A quota tracking system gates API usage and you need to verify its accounting is correct
- Use when: Cache reads and writes can be triggered by both scheduled background tasks and user-initiated IPC calls
- Don't use when: Reviewing a simple in-memory cache with no persistence or quota concerns

---

## Inputs / Context

**Required:**
- Cache manager source file(s) (e.g., `youtube-cache-manager.js`)
- IPC handlers that invoke cache operations (`youtube-force-refresh`, `youtube-clear-cache`, `youtube-cache-health`)
- Environment configuration for cache behavior (`YT_REFRESH_INTERVAL_MIN`, `YT_MAX_PAGES_PER_CHANNEL`, `YT_CACHE_SIZE_LIMIT_MB`, `YT_QUOTA_LIMIT`)

**Optional:**
- YouTube Data API wrapper or HTTP client code used by the cache manager
- Channel whitelist configuration
- Sample cache file (or its schema/structure)

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Trace the complete data flow for each cache operation: read, write, refresh, evict, clear
- Verify that quota tracking matches actual API calls made (no off-by-one, no missed decrements)
- Check that the cache file can survive a crash at any point during a write cycle without corruption
- Analyze what happens when scheduled refresh and IPC-triggered refresh race against each other

**Must Not:**
- Assume the file system write is atomic — `JSON.stringify` + `fs.writeFile` is NOT atomic on most platforms
- Ignore the distinction between `search.list` (100 units), `playlistItems.list` (1 unit), and `videos.list` (1 unit) quota costs
- Report normal cache misses as bugs — a cold cache with no data is expected on first run
- Flag incremental refresh as incorrect because it doesn't re-fetch all historical videos

---

## Steps

1. **Map the cache data model**
   - Document the JSON schema: what fields exist per channel, per video, and at the top level
   - Identify the checkpoint mechanism (`last_seen_video_id` or equivalent) and how it determines which videos are "new"
   - Check the token/cursor-based pagination model for playlist walking
   - Verify the tokenization scheme for offline search (how titles, descriptions, tags are indexed)

2. **Audit incremental refresh correctness**
   - Trace the refresh flow: channel → uploads playlist ID → walk pages → hydrate with `videos.list`
   - Verify that the checkpoint is updated AFTER successful persistence, not before
   - Check what happens when a video is deleted from YouTube after being cached
   - Check what happens when the uploads playlist order changes (YouTube does not guarantee stable ordering)
   - Verify the `YT_MAX_PAGES_PER_CHANNEL` cap is correctly enforced and doesn't skip the checkpoint update

3. **Verify quota accounting**
   - List every YouTube API call the manager makes and its unit cost:
     - `channels.list` (parts: contentDetails) → 1 unit
     - `playlistItems.list` (per page) → 1 unit
     - `videos.list` (per batch of up to 50 IDs) → 1 unit
   - Verify the running tally increments BEFORE the API call (optimistic) or AFTER success (pessimistic)
   - Check the tally against `YT_QUOTA_LIMIT` — does it correctly suspend refreshes?
   - Verify the daily quota reset logic (YouTube resets at midnight Pacific Time)
   - Check what happens if the app restarts mid-day — does the quota tally persist or reset?

4. **Analyze persistence safety**
   - Identify how the cache is written to disk (`fs.writeFile`, `fs.writeFileSync`, write-then-rename, etc.)
   - Check if a crash during write can produce a truncated or empty JSON file
   - Verify if a backup/temp file strategy is used (write to `.tmp`, rename to `.json`)
   - Check what happens on startup if the cache file is corrupt or empty — does the manager recover gracefully?
   - Verify that `JSON.parse` errors are caught and handled

5. **Check concurrent access safety**
   - Can a scheduled refresh and a user-triggered `youtube-force-refresh` run simultaneously?
   - If so, can they produce conflicting writes to the same cache file?
   - Is there a lock, mutex, or queue to serialize write operations?
   - Can a `youtube-clear-cache` call during an active refresh cause data loss or errors?
   - Check if renderer read requests (search, browse) can see a partially-updated cache

6. **Evaluate cache eviction and size management**
   - Verify the `YT_CACHE_SIZE_LIMIT_MB` enforcement: when is size checked, what is evicted?
   - Check the 90-day trim logic: are videos removed by upload date, cache insertion date, or last access?
   - Verify eviction doesn't remove videos that are currently being watched or searched
   - Check if eviction is gradual or all-at-once (thundering herd risk)

7. **CRITICAL: Verify findings before reporting**
   - Distinguish between theoretical race conditions and those actually reachable given Electron's single-threaded main process
   - Confirm that Node.js event loop behavior supports or prevents the concurrent access patterns you identify
   - Verify that reported edge cases can actually occur given the scheduling intervals and user interaction patterns

---

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag race conditions that cannot occur in Node.js single-threaded event loop unless async operations (file I/O, network) create genuine interleaving points
- Report missing `search.list` calls as a bug — the project intentionally avoids this expensive endpoint
- Flag an empty cache on first launch as a corruption issue
- Report that `JSON.stringify` is slow for large objects without measuring the actual cache size
- Flag checkpoint-based incremental fetching as "incomplete" because it doesn't re-fetch old videos

**DO:**
- Check for async interleaving points: every `await`, callback, or `.then()` is a point where another operation can start
- Verify that quota costs match the YouTube Data API v3 documentation, not assumptions
- Test the logic path for: first run (empty cache), normal refresh, quota exhausted, network error mid-refresh, corrupt file on startup
- Confirm that the cache health endpoint accurately reports: total videos, disk size, quota used, last refresh time, errors

---

## Expected Output

### Executive Summary
Brief assessment of cache manager correctness and risk areas for data integrity or quota overuse.

### Data Model Review
```
Cache Structure:
├── metadata (version, last_refresh, quota_used_today, quota_reset_date)
├── channels[]
│   ├── channel_id, uploads_playlist_id, last_seen_video_id
│   └── videos[]
│       ├── video_id, title, description, tags, tokens[]
│       ├── published_at, cached_at
│       └── thumbnail_url, duration
└── search_index (tokenized entries)
```

### Findings

#### Finding N: [Name]
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** `file:line`
- **Scenario:** [Specific sequence of events that triggers the issue]
- **Evidence:** [Code showing the problematic logic]
- **Impact:** [Data loss, quota waste, incorrect search results, crash]
- **Recommendation:** [Specific fix with code example]
- **What would change this assessment:** [Evidence that would modify severity]

### Edge Case Matrix
| Scenario | Expected Behavior | Actual Behavior | Status |
|----------|------------------|-----------------|--------|
| First run, empty cache | Fetch all channels fresh | ... | ... |
| Network failure mid-refresh | Preserve existing cache, retry later | ... | ... |
| Quota exhausted mid-refresh | Stop API calls, serve from cache | ... | ... |
| Crash during cache write | Recover from backup/previous version | ... | ... |
| Concurrent refresh + clear | Clear wins, refresh restarts | ... | ... |
| Cache file corrupt on startup | Re-initialize empty cache | ... | ... |

### Prioritized Recommendations
| # | Action | Severity | Data Integrity Impact |
|---|--------|----------|-----------------------|
| 1 | ...    | ...      | ...                   |

---

## Verification

**Quick self-check:**
- [ ] Every API call has been identified with its correct quota cost
- [ ] The checkpoint update timing has been verified (after write, not before)
- [ ] Crash-safety of file persistence has been evaluated
- [ ] Concurrent access scenarios have been analyzed considering Node.js event loop semantics
- [ ] Cache eviction logic has been traced end-to-end

**High-stakes option:**
After completing the analysis:
1. Simulate 30 days of usage: 8 channels, 3-hour refresh interval, 10,000 daily quota — does the quota tracking stay accurate?
2. What happens if the cache file grows to 500MB and the app starts up on a slow SD card (smart TV hardware)?
3. If YouTube changes a playlist's video order, does the checkpoint mechanism still work correctly?

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Targets specific cache correctness dimensions
- **ST-02 (Structured Sequential Instructions):** Systematic audit from data model through edge cases
- **RT-02 (Multi-Dimensional Analysis):** Each finding covers scenario, evidence, impact, and fix
- **RT-05 (Evidence-Based Reasoning):** Requires tracing actual code paths and API cost documentation
- **QA-01 (Chain-of-Verification):** Edge case matrix forces systematic scenario coverage

---

## Related Prompts

- [API Quota Strategy & Rate Limiting Review](api_quota_strategy_rate_limiting_review.md) - Deeper analysis of quota management
- [Network Resilience & Offline Graceful Degradation](network_resilience_offline_graceful_degradation.md) - How the cache serves content during network failures
