---
title: "API Quota Strategy & Rate Limiting Review"
category: software-engineering/electron-smart-tv
description: "Review YouTube Data API v3 quota consumption patterns, daily budget allocation strategy, per-endpoint cost accuracy, and defensive mechanisms that prevent quota exhaustion from disrupting the user experience."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - QA-01  # Chain-of-Verification
difficulty: intermediate
tags:
  - youtube-api
  - quota-management
  - rate-limiting
  - api-budget
  - cost-optimization
  - defensive-programming
updated: "2026-02-19"
related_prompts:
  - domain-software-engineering/electron-smart-tv/youtube_cache_manager_correctness_review.md
  - domain-software-engineering/electron-smart-tv/network_resilience_offline_graceful_degradation.md
---

# API Quota Strategy & Rate Limiting Review

**Objective:** Review the YouTube Data API v3 quota consumption strategy for correctness of per-call cost calculations, daily budget allocation across operations, defensive suspension when approaching limits, quota reset handling, and optimization opportunities to maximize content freshness within the 10,000-unit daily budget.

---

## When to Use

- Use when: The app uses YouTube Data API v3 with the standard 10,000-unit daily quota
- Use when: Users report quota exhaustion before end of day (content stops refreshing)
- Use when: Adding new API-dependent features (more channels, richer metadata, new search)
- Use when: Optimizing refresh strategy to balance freshness vs. quota cost
- Don't use when: The app uses a different API with different quota semantics

---

## Inputs / Context

**Required:**
- Cache manager code containing YouTube API calls
- Quota tracking implementation (running tally, budget checks)
- List of whitelisted channels (count affects quota budget per channel)
- Environment configuration: `YT_QUOTA_LIMIT`, `YT_REFRESH_INTERVAL_MIN`, `YT_MAX_PAGES_PER_CHANNEL`

**Optional:**
- YouTube Data API quota documentation (for verification of unit costs)
- Historical quota usage data or logs
- Google Cloud Console quota dashboard screenshots
- Channel update frequency estimates (how often channels post new content)

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Verify every API call's quota cost against YouTube Data API v3 official documentation
- Calculate the worst-case daily quota consumption for the current channel list and refresh settings
- Verify that quota tracking is accurate (no missed increments, no double-counting)
- Confirm the app gracefully serves cached content when quota is exhausted

**Must Not:**
- Use outdated quota cost figures — YouTube has changed costs over time; verify against current documentation
- Assume the daily quota resets at midnight local time (it resets at midnight Pacific Time)
- Recommend reducing refresh frequency without calculating the actual quota impact
- Suggest applying for higher quota without first verifying the current budget is used efficiently

---

## Steps

1. **Catalog all API calls and their costs**
   - List every YouTube Data API endpoint called by the application
   - For each endpoint, document:
     - Method and parts parameter (e.g., `playlistItems.list(part=snippet)`)
     - Quota cost per call (from YouTube API documentation)
     - How many calls per channel per refresh cycle
     - How many calls per day (refresh interval × channels × pages)

   Reference costs (verify against current YouTube docs):
   | Endpoint | Cost per Call |
   |----------|--------------|
   | `channels.list` | 1 unit |
   | `playlistItems.list` | 1 unit |
   | `videos.list` | 1 unit |
   | `search.list` | 100 units |

2. **Calculate daily quota budget**
   - Compute worst-case daily usage:
     ```
     refreshes_per_day = 24 * 60 / YT_REFRESH_INTERVAL_MIN
     calls_per_refresh = channels × (1 channel lookup + pages × 1 playlistItems + ceil(new_videos/50) × 1 videos.list)
     daily_quota = refreshes_per_day × calls_per_refresh
     ```
   - Compare against `YT_QUOTA_LIMIT` (default 10,000)
   - Identify the largest quota consumer (usually the endpoint called most frequently)
   - Calculate headroom: how many manual force-refreshes can be triggered before exhaustion?

3. **Audit quota tracking accuracy**
   - Trace where quota is incremented: before the API call (optimistic) or after (pessimistic)?
   - Check if failed API calls (network error, 403, 500) still consume quota at Google's end but aren't tracked locally
   - Verify that batch calls (e.g., `videos.list` with 50 IDs) are counted as 1 unit, not 50
   - Check if the quota tally persists across app restarts (stored in cache file? in-memory only?)
   - Verify daily reset logic: does it use Pacific Time? Does it handle timezone correctly?

4. **Evaluate defensive quota mechanisms**
   - Check the threshold at which the app stops making API calls (e.g., 90% of budget)
   - Verify that the UI communicates quota status to the user (or silently falls back to cache)
   - Check if force-refresh IPC calls bypass the quota check (they shouldn't burn remaining quota if budget is low)
   - Verify that the quota check runs BEFORE the API call, not after
   - Check if the app distinguishes between "quota exhausted locally" and "403 quotaExceeded from Google"

5. **Identify optimization opportunities**
   - Check if `channels.list` is called on every refresh or if the uploads playlist ID is cached (it doesn't change)
   - Verify that `playlistItems.list` uses the `last_seen_video_id` checkpoint to minimize pages fetched
   - Check if `videos.list` batches IDs efficiently (up to 50 per call)
   - Look for redundant API calls: same data fetched multiple times per cycle
   - Evaluate if refresh interval could be adaptive (more frequent for channels that post often, less for dormant ones)

6. **Verify quota exhaustion experience**
   - When quota is exhausted, verify:
     - Cached content remains fully browsable and searchable
     - No API calls are attempted (no wasted 403 responses)
     - The next day's quota reset triggers a refresh automatically
     - The UI doesn't show "no content" or error states — it shows cached content normally
   - Check if manual `youtube-cache-health` IPC call reports quota status accurately

7. **CRITICAL: Verify findings before reporting**
   - Confirm quota costs against the actual YouTube Data API v3 documentation, not memory or assumptions
   - Calculate with the actual number of whitelisted channels, not a hypothetical number
   - Verify that reported "waste" is meaningful (saving 10 units/day on a 10,000 budget is irrelevant; saving 2,000 is significant)
   - Check if the current configuration is already within budget before suggesting optimizations

---

## False-Positive Prevention (MUST follow)

**DON'T:**
- Report quota costs from memory — verify against current YouTube Data API v3 quota documentation
- Flag efficient caching as "not using the API" — the entire point is to minimize API calls
- Report that `search.list` isn't used as a bug — the app intentionally avoids it (100 units per call)
- Suggest reducing channels as a quota optimization (that's a product decision, not an engineering one)
- Flag a 180-minute refresh interval as "too infrequent" without calculating the quota impact of more frequent refreshes

**DO:**
- Calculate the actual daily quota consumption with current settings and channel count
- Verify that channels.list results (uploads playlist ID) are cached persistently (it never changes for a channel)
- Check if the incremental checkpoint reduces the average pages fetched per channel per refresh
- Confirm that Google's 403 quotaExceeded response is handled and stops further calls immediately
- Verify the quota reset timing uses Pacific Time, not local time or UTC

---

## Expected Output

### Executive Summary
Daily quota budget assessment: current consumption, headroom, and efficiency rating.

### API Call Catalog
| Endpoint | Cost | Calls/Refresh | Calls/Day | Daily Cost | % of Budget |
|----------|------|---------------|-----------|------------|-------------|
| channels.list | 1 | ... | ... | ... | ... |
| playlistItems.list | 1 | ... | ... | ... | ... |
| videos.list | 1 | ... | ... | ... | ... |
| **Total** | | | | **...** | **...%** |

### Daily Budget Calculation
```
Channels: N
Refresh interval: M minutes → R refreshes/day
Per-refresh cost: C units
Daily consumption: R × C = X units / 10,000 budget
Headroom: Y units available for manual refreshes
```

### Findings

#### Finding N: [Name]
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** `file:line`
- **Evidence:** [Quota calculation or code showing the issue]
- **Impact:** [Quota wasted per day, premature exhaustion timing, tracking inaccuracy]
- **Recommendation:** [Specific fix with quota savings estimate]
- **What would change this assessment:** [Evidence that would modify severity]

### Quota Timeline (24-hour projection)
```
Hour 0 (midnight PT): Quota resets to 10,000
Hour 1: First refresh → -X units (remaining: ...)
Hour 4: Second refresh → -X units (remaining: ...)
...
Hour N: Quota exhausted → cache-only mode
```

### Prioritized Recommendations
| # | Action | Quota Savings/Day | Implementation Effort |
|---|--------|-------------------|----------------------|
| 1 | ...    | ...               | ...                  |

---

## Verification

**Quick self-check:**
- [ ] Every API endpoint's cost verified against YouTube Data API v3 documentation
- [ ] Daily quota consumption calculated for actual channel count and refresh settings
- [ ] Quota tracking accuracy verified (increments, resets, persistence across restarts)
- [ ] Exhaustion experience tested (cached content accessible, no API calls attempted)
- [ ] Optimization opportunities quantified with actual savings estimates

**High-stakes option:**
After completing the analysis:
1. If the user adds 5 more channels, will the quota budget still last the full day?
2. What is the maximum number of channels sustainable on 10,000 units/day with current refresh settings?
3. If the app crashes and restarts, does it know how much quota has already been used today?

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Targets YouTube API quota correctness and efficiency
- **ST-02 (Structured Sequential Instructions):** Systematic audit from API catalog through exhaustion testing
- **RT-02 (Multi-Dimensional Analysis):** Cost accuracy, budget allocation, tracking, defense, optimization
- **RT-05 (Evidence-Based Reasoning):** Requires calculations verified against API documentation
- **QA-01 (Chain-of-Verification):** Budget projection forces mathematical verification of claims

---

## Related Prompts

- [YouTube Cache Manager Correctness Review](youtube_cache_manager_correctness_review.md) - Cache integrity and checkpoint correctness
- [Network Resilience & Offline Graceful Degradation](network_resilience_offline_graceful_degradation.md) - Behavior when quota-exhausted
