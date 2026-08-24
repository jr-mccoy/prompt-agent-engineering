---
title: "GCP BigQuery Analytics Pipeline for Firebase Apps"
category: cloud-infrastructure
description: "Set up a Firebase Analytics to BigQuery export pipeline for deep user analytics, including export configuration, schema understanding, retention cohort analysis, funnel queries, revenue tracking, scheduled reports, and cost control with partitioned tables."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
  - DS-02
  - RT-05
difficulty: intermediate
tags:
  - gcp
  - bigquery
  - firebase
  - analytics
  - sql
  - cohort-analysis
  - funnel-analysis
  - revenue
  - solo-developer
  - android
updated: "2026-02-11"
---

# GCP BigQuery Analytics Pipeline for Firebase Apps

**Objective:** Set up a complete Firebase Analytics to BigQuery export pipeline so you can run real SQL queries against your user event data. Firebase's built-in analytics dashboard is useful for surface-level metrics, but BigQuery export unlocks retention cohort analysis, multi-step funnel debugging, revenue-per-user calculations, and custom engagement scoring that the dashboard cannot do. This guide covers the full pipeline from enabling export through writing production queries to scheduling automated reports.

**When to Use:** Use this prompt when Firebase Analytics dashboard is no longer enough. Specifically: when you need to answer questions like "what percentage of users who completed onboarding on day 1 are still active on day 7," "where exactly are users dropping off in my purchase funnel," "which user acquisition channel produces the highest lifetime value," or "what does my daily/weekly/monthly active user trend actually look like." If you are making product decisions based on gut feeling because the dashboard does not slice data the way you need, this is your next step.

---

## Context Gathering

Before setting up the analytics pipeline, gather the following:

1. **Firebase Project Details**
   - What is your Firebase project ID?
   - Are you on the Blaze plan? (Required for BigQuery export)
   - What Firebase SDKs are integrated? (Analytics, Crashlytics, Remote Config)
   - What is your app's primary platform? (Android, iOS, Web, or multi-platform)

2. **Current Analytics State**
   - Are you logging custom events beyond the automatic ones?
   - What are your most important user actions? (sign_up, purchase, level_complete, etc.)
   - Do you have user properties set up? (subscription_status, user_tier, etc.)
   - Approximate daily active users?

3. **Analytics Questions You Need Answered**
   - What retention windows matter? (Day 1, Day 7, Day 30?)
   - What funnels do you need to track? (Onboarding, purchase, feature adoption?)
   - Do you track revenue events? (in_app_purchase, ad_revenue, subscription?)
   - What engagement metrics define a "good" user for your product?

4. **Technical Constraints**
   - What is your BigQuery budget for query costs?
   - Do you need real-time analytics or is daily sufficient?
   - Who needs access to the analytics? (Just you, or stakeholders?)
   - Do you need dashboards or is raw SQL output sufficient?

---

## Instructions

### CRITICAL: Verification Requirements

Before relying on any analytics data, verify these requirements:

1. **Firebase Blaze plan is active** -- BigQuery export is not available on the Spark plan
2. **Firebase Analytics SDK is integrated** in your app and sending events (check Firebase Console > Analytics > DebugView)
3. **BigQuery API is enabled** in your GCP project
4. **BigQuery export is linked** in Firebase Console > Project Settings > Integrations > BigQuery
5. **At least 24 hours have passed** since enabling export before querying data (export is not retroactive for most event types)
6. **You have verified events are flowing** by checking the `analytics_XXXXXX.events_*` tables in BigQuery Console
7. **Acceptable null result:** If your app is brand new with few users, cohort and funnel queries will return sparse data. This is not a pipeline error -- it means you need more users before the analysis is statistically meaningful.

### False-Positive Prevention

- **DO NOT** assume BigQuery export includes historical data from before you enabled it. Export begins from the moment you turn it on. Intraday tables may include some same-day data.
- **DO NOT** run `SELECT *` queries against unpartitioned event tables. Firebase event tables can grow to gigabytes quickly, and BigQuery charges $6.25 per TB scanned.
- **DO NOT** confuse `event_date` (string in YYYYMMDD format) with `event_timestamp` (microseconds since epoch). Mixing these up silently produces wrong results.
- **DO NOT** treat Firebase's automatically collected events as a complete picture. Events like `first_open`, `session_start`, and `screen_view` are approximations with known edge cases (e.g., `first_open` may not fire if the app is installed but not opened for days).
- **DO** use `_TABLE_SUFFIX` to filter date-sharded tables and avoid scanning unnecessary data.
- **DO** create views or saved queries for your most-used analyses so you do not accidentally run expensive full-table scans.
- **DO** check the `event_params` RECORD field structure before assuming a parameter exists for all events. Not every event carries the same parameters.
- **DO** validate cohort retention numbers against Firebase dashboard numbers for a sanity check before building dashboards on top of your queries.

---

### Phase 1: Export Setup

#### Step 1: Enable BigQuery Export in Firebase Console

```
Navigation Path:
Firebase Console → Project Settings (gear icon) → Integrations → BigQuery

Settings:
├── Link BigQuery: ENABLE
├── Select data to export:
│   ├── Google Analytics: ENABLE (this is the main one)
│   ├── Crashlytics: ENABLE (optional but useful)
│   ├── Cloud Messaging: OPTIONAL
│   ├── Performance Monitoring: OPTIONAL
│   └── Remote Config: OPTIONAL
├── Export location: Select your preferred BigQuery region
│   └── Recommendation: us-central1 (cheapest, most free tier friendly)
├── Frequency:
│   ├── Daily export: ENABLE (creates events_YYYYMMDD tables)
│   └── Streaming export: OPTIONAL (creates events_intraday_YYYYMMDD)
│       └── Note: Streaming export costs more but gives near-real-time data
└── Click LINK TO BIGQUERY
```

#### Step 2: Verify Export is Working

```bash
# Set your project
export PROJECT_ID="your-firebase-project-id"

# List datasets -- you should see an analytics_XXXXXX dataset
bq ls --project_id=$PROJECT_ID

# Example output:
#        datasetId
# -----------------------
#  analytics_123456789

# List tables in the analytics dataset (after 24 hours)
bq ls $PROJECT_ID:analytics_123456789

# Example output:
#         tableId          Type
# ------------------------ -------
#  events_20260201         TABLE
#  events_20260202         TABLE
#  events_intraday_20260203 TABLE

# Quick check: count events from yesterday
bq query --use_legacy_sql=false \
  "SELECT COUNT(*) as event_count
   FROM \`$PROJECT_ID.analytics_123456789.events_$(date -d 'yesterday' +%Y%m%d)\`"
```

#### Step 3: Enable Streaming Export (Optional)

Streaming export gives you access to today's events in near-real-time via `events_intraday_*` tables. It costs more because of BigQuery streaming insert pricing, but is valuable when you need same-day analytics.

```
Navigation Path:
Firebase Console → Project Settings → Integrations → BigQuery → Manage

Toggle: "Include streaming data" → ON

Cost impact:
├── Daily export only: Free (included with Blaze)
├── Streaming export: $0.01 per 200 MB streamed
├── For a solo dev app (~10K events/day): ~$0.01-0.05/day
└── Recommendation: Enable it. The cost is trivial.
```

---

### Phase 2: Schema Understanding

Understanding the Firebase Analytics BigQuery schema is critical. Every query you write depends on knowing how events, parameters, and user properties are structured.

#### Core Table Structure

Firebase exports one table per day using the naming pattern `events_YYYYMMDD`. Each row is one event.

```sql
-- Examine the schema of your events table
SELECT
  column_name,
  data_type,
  is_nullable
FROM
  `your-project.analytics_123456789.INFORMATION_SCHEMA.COLUMNS`
WHERE
  table_name = 'events_20260201'
ORDER BY
  ordinal_position;
```

#### Key Columns

| Column | Type | Description |
|--------|------|-------------|
| `event_date` | STRING | Date in YYYYMMDD format |
| `event_timestamp` | INTEGER | Microseconds since Unix epoch |
| `event_name` | STRING | Event name (e.g., `screen_view`, `purchase`) |
| `event_params` | RECORD (REPEATED) | Array of key-value pairs for event parameters |
| `user_id` | STRING | Your custom user ID (if set via `setUserId`) |
| `user_pseudo_id` | STRING | Firebase's anonymous device/session ID |
| `user_properties` | RECORD (REPEATED) | Array of key-value pairs for user properties |
| `user_first_touch_timestamp` | INTEGER | When the user first opened the app |
| `device` | RECORD | Device info (category, brand, model, os_version) |
| `geo` | RECORD | Geography (country, region, city) |
| `app_info` | RECORD | App version, install source |
| `traffic_source` | RECORD | UTM parameters, campaign info |
| `platform` | STRING | ANDROID, IOS, or WEB |

#### Extracting Event Parameters

Event parameters are stored as a repeated RECORD, which requires a special extraction pattern:

```sql
-- Extract a specific parameter from an event
-- This is the pattern you will use constantly
SELECT
  user_pseudo_id,
  event_name,
  event_timestamp,
  -- Extract string parameter
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'screen_name') AS screen_name,
  -- Extract integer parameter
  (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'engagement_time_msec') AS engagement_time_msec,
  -- Extract double/float parameter
  (SELECT value.double_value FROM UNNEST(event_params) WHERE key = 'score') AS score,
  -- Extract value that could be in multiple fields
  COALESCE(
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'currency'),
    'USD'
  ) AS currency
FROM
  `your-project.analytics_123456789.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260201' AND '20260207'
  AND event_name = 'screen_view'
LIMIT 100;
```

#### Extracting User Properties

```sql
-- Extract user properties
SELECT
  user_pseudo_id,
  (SELECT value.string_value FROM UNNEST(user_properties) WHERE key = 'subscription_status') AS subscription_status,
  (SELECT value.string_value FROM UNNEST(user_properties) WHERE key = 'user_tier') AS user_tier,
  (SELECT value.int_value FROM UNNEST(user_properties) WHERE key = 'lifetime_purchases') AS lifetime_purchases
FROM
  `your-project.analytics_123456789.events_*`
WHERE
  _TABLE_SUFFIX = '20260207'
  AND event_name = 'session_start'
LIMIT 100;
```

#### Commonly Available Automatic Events

| Event Name | What It Means | Key Parameters |
|------------|--------------|----------------|
| `first_open` | First app launch after install | `previous_os`, `system_app` |
| `session_start` | New session began (30min timeout) | `session_id`, `session_number` |
| `screen_view` | User viewed a screen | `firebase_screen`, `firebase_screen_class` |
| `user_engagement` | App was in foreground | `engagement_time_msec` |
| `app_update` | App was updated | `previous_app_version` |
| `os_update` | OS was updated | `previous_os_version` |
| `in_app_purchase` | IAP completed | `product_id`, `price`, `currency`, `quantity` |
| `ad_impression` | Ad was shown | `ad_platform`, `ad_source`, `ad_unit_name`, `value` |

---

### Phase 3: Essential Queries

These are the queries that answer the product questions you actually care about. Each one is designed to be copy-paste ready with minimal modification.

#### Query 1: Retention Cohort Analysis (Day 1 / Day 7 / Day 30)

This is the single most important query for understanding whether your product is working. It groups users by their first-open week, then checks what percentage came back on subsequent days.

```sql
-- Retention cohort analysis: weekly cohorts with D1, D7, D14, D30 retention
WITH user_first_open AS (
  SELECT
    user_pseudo_id,
    DATE(TIMESTAMP_MICROS(user_first_touch_timestamp)) AS cohort_date,
    DATE_TRUNC(DATE(TIMESTAMP_MICROS(user_first_touch_timestamp)), WEEK) AS cohort_week
  FROM
    `your-project.analytics_123456789.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN
      FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
      AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
    AND event_name = 'first_open'
  GROUP BY
    user_pseudo_id, cohort_date, cohort_week
),
user_activity AS (
  SELECT
    user_pseudo_id,
    DATE(TIMESTAMP_MICROS(event_timestamp)) AS activity_date
  FROM
    `your-project.analytics_123456789.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN
      FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
      AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
    AND event_name IN ('session_start', 'user_engagement')
  GROUP BY
    user_pseudo_id, activity_date
)
SELECT
  f.cohort_week,
  COUNT(DISTINCT f.user_pseudo_id) AS cohort_size,
  ROUND(COUNT(DISTINCT CASE
    WHEN DATE_DIFF(a.activity_date, f.cohort_date, DAY) = 1
    THEN f.user_pseudo_id END) * 100.0 / COUNT(DISTINCT f.user_pseudo_id), 1) AS day_1_pct,
  ROUND(COUNT(DISTINCT CASE
    WHEN DATE_DIFF(a.activity_date, f.cohort_date, DAY) = 7
    THEN f.user_pseudo_id END) * 100.0 / COUNT(DISTINCT f.user_pseudo_id), 1) AS day_7_pct,
  ROUND(COUNT(DISTINCT CASE
    WHEN DATE_DIFF(a.activity_date, f.cohort_date, DAY) = 14
    THEN f.user_pseudo_id END) * 100.0 / COUNT(DISTINCT f.user_pseudo_id), 1) AS day_14_pct,
  ROUND(COUNT(DISTINCT CASE
    WHEN DATE_DIFF(a.activity_date, f.cohort_date, DAY) = 30
    THEN f.user_pseudo_id END) * 100.0 / COUNT(DISTINCT f.user_pseudo_id), 1) AS day_30_pct
FROM user_first_open f
LEFT JOIN user_activity a
  ON f.user_pseudo_id = a.user_pseudo_id
  AND a.activity_date >= f.cohort_date
GROUP BY f.cohort_week
HAVING cohort_size >= 10  -- Exclude tiny cohorts that are not meaningful
ORDER BY f.cohort_week DESC;
```

**What healthy retention looks like for mobile apps:**

| Retention Day | Poor | Average | Good | Excellent |
|---------------|------|---------|------|-----------|
| Day 1 | < 20% | 20-30% | 30-40% | > 40% |
| Day 7 | < 8% | 8-15% | 15-25% | > 25% |
| Day 30 | < 3% | 3-8% | 8-15% | > 15% |

#### Query 2: Multi-Step Funnel Analysis

Track where users drop off in a critical flow (e.g., onboarding, purchase).

```sql
-- Funnel analysis: Onboarding completion funnel
-- Customize the event names to match your app's flow
WITH funnel_events AS (
  SELECT
    user_pseudo_id,
    event_name,
    event_timestamp,
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'screen_name') AS screen_name
  FROM
    `your-project.analytics_123456789.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN
      FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
      AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
    AND event_name IN (
      'first_open',           -- Step 1: Installed and opened
      'tutorial_begin',       -- Step 2: Started tutorial
      'tutorial_complete',    -- Step 3: Finished tutorial
      'sign_up',              -- Step 4: Created account
      'first_action_complete' -- Step 5: Completed key action
    )
),
user_funnel AS (
  SELECT
    user_pseudo_id,
    MAX(CASE WHEN event_name = 'first_open' THEN 1 ELSE 0 END) AS step_1_open,
    MAX(CASE WHEN event_name = 'tutorial_begin' THEN 1 ELSE 0 END) AS step_2_tutorial_start,
    MAX(CASE WHEN event_name = 'tutorial_complete' THEN 1 ELSE 0 END) AS step_3_tutorial_done,
    MAX(CASE WHEN event_name = 'sign_up' THEN 1 ELSE 0 END) AS step_4_signup,
    MAX(CASE WHEN event_name = 'first_action_complete' THEN 1 ELSE 0 END) AS step_5_action
  FROM funnel_events
  GROUP BY user_pseudo_id
)
SELECT
  'Step 1: App Opened' AS funnel_step,
  COUNT(*) AS users,
  ROUND(COUNT(*) * 100.0 / COUNT(*), 1) AS pct_of_total,
  NULL AS drop_off_pct
FROM user_funnel WHERE step_1_open = 1

UNION ALL

SELECT
  'Step 2: Tutorial Started',
  COUNTIF(step_2_tutorial_start = 1),
  ROUND(COUNTIF(step_2_tutorial_start = 1) * 100.0 /
    (SELECT COUNT(*) FROM user_funnel WHERE step_1_open = 1), 1),
  ROUND((1 - COUNTIF(step_2_tutorial_start = 1) * 1.0 /
    (SELECT COUNT(*) FROM user_funnel WHERE step_1_open = 1)) * 100, 1)
FROM user_funnel WHERE step_1_open = 1

UNION ALL

SELECT
  'Step 3: Tutorial Completed',
  COUNTIF(step_3_tutorial_done = 1),
  ROUND(COUNTIF(step_3_tutorial_done = 1) * 100.0 /
    (SELECT COUNT(*) FROM user_funnel WHERE step_1_open = 1), 1),
  ROUND((1 - COUNTIF(step_3_tutorial_done = 1) * 1.0 /
    NULLIF(COUNTIF(step_2_tutorial_start = 1), 0)) * 100, 1)
FROM user_funnel WHERE step_1_open = 1

UNION ALL

SELECT
  'Step 4: Signed Up',
  COUNTIF(step_4_signup = 1),
  ROUND(COUNTIF(step_4_signup = 1) * 100.0 /
    (SELECT COUNT(*) FROM user_funnel WHERE step_1_open = 1), 1),
  ROUND((1 - COUNTIF(step_4_signup = 1) * 1.0 /
    NULLIF(COUNTIF(step_3_tutorial_done = 1), 0)) * 100, 1)
FROM user_funnel WHERE step_1_open = 1

UNION ALL

SELECT
  'Step 5: First Action Done',
  COUNTIF(step_5_action = 1),
  ROUND(COUNTIF(step_5_action = 1) * 100.0 /
    (SELECT COUNT(*) FROM user_funnel WHERE step_1_open = 1), 1),
  ROUND((1 - COUNTIF(step_5_action = 1) * 1.0 /
    NULLIF(COUNTIF(step_4_signup = 1), 0)) * 100, 1)
FROM user_funnel WHERE step_1_open = 1

ORDER BY funnel_step;
```

#### Query 3: Revenue Per User (ARPU / ARPPU)

```sql
-- Revenue analysis: ARPU and ARPPU by month
-- Works with in_app_purchase events and custom purchase events
WITH monthly_revenue AS (
  SELECT
    FORMAT_DATE('%Y-%m', DATE(TIMESTAMP_MICROS(event_timestamp))) AS month,
    user_pseudo_id,
    event_name,
    COALESCE(
      (SELECT value.double_value FROM UNNEST(event_params) WHERE key = 'value'),
      (SELECT CAST(value.int_value AS FLOAT64) FROM UNNEST(event_params) WHERE key = 'value'),
      0
    ) AS revenue_value,
    COALESCE(
      (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'currency'),
      'USD'
    ) AS currency
  FROM
    `your-project.analytics_123456789.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN
      FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 180 DAY))
      AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
    AND event_name IN ('in_app_purchase', 'purchase', 'subscription_renewal')
),
monthly_active AS (
  SELECT
    FORMAT_DATE('%Y-%m', DATE(TIMESTAMP_MICROS(event_timestamp))) AS month,
    COUNT(DISTINCT user_pseudo_id) AS mau
  FROM
    `your-project.analytics_123456789.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN
      FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 180 DAY))
      AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
    AND event_name = 'session_start'
  GROUP BY month
)
SELECT
  r.month,
  ma.mau AS monthly_active_users,
  COUNT(DISTINCT r.user_pseudo_id) AS paying_users,
  ROUND(COUNT(DISTINCT r.user_pseudo_id) * 100.0 / ma.mau, 2) AS conversion_rate_pct,
  ROUND(SUM(r.revenue_value), 2) AS total_revenue,
  ROUND(SUM(r.revenue_value) / ma.mau, 4) AS arpu,
  ROUND(SUM(r.revenue_value) / NULLIF(COUNT(DISTINCT r.user_pseudo_id), 0), 2) AS arppu
FROM monthly_revenue r
JOIN monthly_active ma ON r.month = ma.month
GROUP BY r.month, ma.mau
ORDER BY r.month DESC;
```

#### Query 4: Engagement Metrics (DAU / WAU / MAU and Stickiness)

```sql
-- Engagement: DAU, WAU, MAU, and DAU/MAU stickiness ratio
WITH daily_users AS (
  SELECT
    DATE(TIMESTAMP_MICROS(event_timestamp)) AS activity_date,
    user_pseudo_id
  FROM
    `your-project.analytics_123456789.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN
      FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY))
      AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
    AND event_name IN ('session_start', 'user_engagement')
  GROUP BY activity_date, user_pseudo_id
)
SELECT
  activity_date,
  -- DAU: unique users on this day
  COUNT(DISTINCT user_pseudo_id) AS dau,
  -- WAU: unique users in the 7-day window ending on this day
  COUNT(DISTINCT CASE
    WHEN activity_date BETWEEN
      DATE_SUB(d.activity_date, INTERVAL 6 DAY) AND d.activity_date
    THEN user_pseudo_id END) AS wau,
  -- MAU: unique users in the 30-day window ending on this day
  (SELECT COUNT(DISTINCT user_pseudo_id)
   FROM daily_users d2
   WHERE d2.activity_date BETWEEN
     DATE_SUB(d.activity_date, INTERVAL 29 DAY) AND d.activity_date
  ) AS mau,
  -- Stickiness: DAU/MAU ratio (higher = more engaged)
  ROUND(
    COUNT(DISTINCT user_pseudo_id) * 100.0 /
    NULLIF((SELECT COUNT(DISTINCT user_pseudo_id)
            FROM daily_users d2
            WHERE d2.activity_date BETWEEN
              DATE_SUB(d.activity_date, INTERVAL 29 DAY) AND d.activity_date), 0),
    1
  ) AS stickiness_pct
FROM daily_users d
WHERE activity_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY activity_date
ORDER BY activity_date DESC;
```

**Stickiness benchmarks:**

| DAU/MAU Ratio | Interpretation |
|---------------|----------------|
| < 10% | Low engagement -- users install and forget |
| 10-20% | Average for most apps |
| 20-30% | Good -- users have a reason to come back |
| 30-50% | Very strong (social apps, messaging) |
| > 50% | Exceptional (daily utility, gaming) |

#### Query 5: User Acquisition Channel Performance

```sql
-- Which acquisition channels bring the most valuable users?
WITH user_source AS (
  SELECT
    user_pseudo_id,
    traffic_source.source AS acquisition_source,
    traffic_source.medium AS acquisition_medium,
    traffic_source.name AS acquisition_campaign,
    DATE(TIMESTAMP_MICROS(user_first_touch_timestamp)) AS first_open_date
  FROM
    `your-project.analytics_123456789.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN
      FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
      AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
    AND event_name = 'first_open'
  GROUP BY
    user_pseudo_id, acquisition_source, acquisition_medium,
    acquisition_campaign, first_open_date
),
user_retention AS (
  SELECT
    user_pseudo_id,
    COUNT(DISTINCT DATE(TIMESTAMP_MICROS(event_timestamp))) AS active_days,
    MAX(DATE(TIMESTAMP_MICROS(event_timestamp))) AS last_active
  FROM
    `your-project.analytics_123456789.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN
      FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
      AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
    AND event_name IN ('session_start', 'user_engagement')
  GROUP BY user_pseudo_id
),
user_revenue AS (
  SELECT
    user_pseudo_id,
    SUM(COALESCE(
      (SELECT value.double_value FROM UNNEST(event_params) WHERE key = 'value'),
      0
    )) AS total_revenue
  FROM
    `your-project.analytics_123456789.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN
      FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
      AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
    AND event_name IN ('in_app_purchase', 'purchase')
  GROUP BY user_pseudo_id
)
SELECT
  COALESCE(s.acquisition_source, '(direct)') AS source,
  COALESCE(s.acquisition_medium, '(none)') AS medium,
  COUNT(DISTINCT s.user_pseudo_id) AS users_acquired,
  ROUND(AVG(r.active_days), 1) AS avg_active_days,
  ROUND(AVG(DATE_DIFF(r.last_active, s.first_open_date, DAY)), 1) AS avg_lifespan_days,
  ROUND(SUM(COALESCE(rev.total_revenue, 0)), 2) AS total_revenue,
  ROUND(SUM(COALESCE(rev.total_revenue, 0)) / COUNT(DISTINCT s.user_pseudo_id), 4) AS revenue_per_user,
  ROUND(COUNTIF(r.active_days >= 7) * 100.0 / COUNT(DISTINCT s.user_pseudo_id), 1) AS pct_retained_7d
FROM user_source s
LEFT JOIN user_retention r ON s.user_pseudo_id = r.user_pseudo_id
LEFT JOIN user_revenue rev ON s.user_pseudo_id = rev.user_pseudo_id
GROUP BY source, medium
HAVING users_acquired >= 5
ORDER BY revenue_per_user DESC;
```

---

### Phase 4: Scheduled Reports

Automate your most important queries so analytics insights arrive without you remembering to run them.

#### Option A: BigQuery Scheduled Queries

```bash
# Create a scheduled query that runs every Monday at 8:00 AM UTC
# This example runs the retention cohort analysis weekly

bq query \
  --use_legacy_sql=false \
  --destination_table=$PROJECT_ID:analytics_reports.weekly_retention \
  --display_name="Weekly Retention Cohort Report" \
  --schedule="every monday 08:00" \
  --replace=true \
  --project_id=$PROJECT_ID \
  "$(cat retention_cohort_query.sql)"
```

```bash
# Create a scheduled query via gcloud (more control over configuration)
# First, save your query to a file, then:

bq mk \
  --transfer_config \
  --project_id=$PROJECT_ID \
  --data_source=scheduled_query \
  --target_dataset=analytics_reports \
  --display_name="Daily Engagement Metrics" \
  --schedule="every day 07:00" \
  --params='{
    "query": "SELECT DATE(TIMESTAMP_MICROS(event_timestamp)) AS date, COUNT(DISTINCT user_pseudo_id) AS dau FROM `'$PROJECT_ID'.analytics_123456789.events_*` WHERE _TABLE_SUFFIX = FORMAT_DATE(\"%Y%m%d\", DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)) AND event_name = \"session_start\" GROUP BY date",
    "destination_table_name_template": "daily_dau_{run_date}",
    "write_disposition": "WRITE_TRUNCATE"
  }'
```

#### Option B: Cloud Functions Scheduled Report with Email

```typescript
// functions/src/weekly-analytics-report.ts
import { onSchedule } from 'firebase-functions/v2/scheduler';
import { BigQuery } from '@google-cloud/bigquery';
import * as nodemailer from 'nodemailer';

const bigquery = new BigQuery();

export const weeklyAnalyticsReport = onSchedule(
  {
    schedule: 'every monday 08:00',
    timeZone: 'America/New_York',
    region: 'us-central1',
    memory: '512MiB',
    timeoutSeconds: 120,
  },
  async () => {
    const projectId = process.env.GCP_PROJECT || '';
    const datasetId = 'analytics_123456789'; // Replace with your dataset

    // Run DAU/WAU/MAU query
    const [engagementRows] = await bigquery.query({
      query: `
        SELECT
          COUNT(DISTINCT CASE
            WHEN DATE(TIMESTAMP_MICROS(event_timestamp)) = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
            THEN user_pseudo_id END) AS yesterday_dau,
          COUNT(DISTINCT CASE
            WHEN DATE(TIMESTAMP_MICROS(event_timestamp)) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
            THEN user_pseudo_id END) AS wau,
          COUNT(DISTINCT CASE
            WHEN DATE(TIMESTAMP_MICROS(event_timestamp)) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
            THEN user_pseudo_id END) AS mau
        FROM \`${projectId}.${datasetId}.events_*\`
        WHERE _TABLE_SUFFIX BETWEEN
          FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
          AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
        AND event_name IN ('session_start', 'user_engagement')
      `,
      location: 'US',
    });

    const { yesterday_dau, wau, mau } = engagementRows[0];
    const stickiness = mau > 0 ? ((yesterday_dau / mau) * 100).toFixed(1) : '0';

    // Format email
    const report = `
Weekly Analytics Report — ${new Date().toLocaleDateString()}

Engagement Summary:
  Yesterday DAU: ${yesterday_dau}
  WAU (7-day): ${wau}
  MAU (30-day): ${mau}
  Stickiness (DAU/MAU): ${stickiness}%

View full dashboard: https://console.cloud.google.com/bigquery?project=${projectId}
    `.trim();

    // Send via your preferred method (nodemailer, SendGrid, Slack webhook, etc.)
    console.log('Weekly report generated:', report);

    // Example: Send to Slack webhook
    const slackWebhookUrl = process.env.SLACK_WEBHOOK_URL;
    if (slackWebhookUrl) {
      await fetch(slackWebhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: '```\n' + report + '\n```' }),
      });
    }
  }
);
```

#### Setting Up a Reporting Dataset

```bash
# Create a dedicated dataset for scheduled query results
bq mk \
  --dataset \
  --description="Automated analytics reports and materialized views" \
  --location=US \
  --default_table_expiration=7776000 \
  $PROJECT_ID:analytics_reports

# The 7776000 seconds = 90 days expiration
# Old report tables are automatically deleted to save storage costs
```

#### Recommended Report Schedule

| Report | Frequency | Query | Destination Table |
|--------|-----------|-------|-------------------|
| Daily DAU | Daily 7 AM | DAU count | `analytics_reports.daily_dau` |
| Weekly retention | Monday 8 AM | Cohort retention | `analytics_reports.weekly_retention` |
| Weekly funnel | Monday 8 AM | Onboarding funnel | `analytics_reports.weekly_funnel` |
| Monthly revenue | 1st of month | ARPU/ARPPU | `analytics_reports.monthly_revenue` |
| Monthly acquisition | 1st of month | Channel performance | `analytics_reports.monthly_acquisition` |

---

### Phase 5: Cost Control

BigQuery charges $6.25 per TB of data scanned (on-demand pricing). Firebase event tables grow over time. Without cost controls, a carelessly written query can scan your entire event history and cost real money.

#### Strategy 1: Always Use _TABLE_SUFFIX Filters

```sql
-- BAD: Scans ALL event tables (could be months/years of data)
SELECT COUNT(*)
FROM `your-project.analytics_123456789.events_*`;

-- GOOD: Scans only the last 7 days
SELECT COUNT(*)
FROM `your-project.analytics_123456789.events_*`
WHERE _TABLE_SUFFIX BETWEEN
  FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY))
  AND FORMAT_DATE('%Y%m%d', CURRENT_DATE());

-- The _TABLE_SUFFIX filter is evaluated BEFORE scanning, so it actually
-- prevents BigQuery from reading the excluded tables. This is true
-- partition pruning, not just a WHERE clause filter.
```

#### Strategy 2: Create Materialized Views for Frequent Queries

```sql
-- Create a materialized view for daily active users
-- BigQuery automatically refreshes it and caches results
CREATE MATERIALIZED VIEW `your-project.analytics_reports.mv_daily_dau`
OPTIONS (
  enable_refresh = true,
  refresh_interval_minutes = 720  -- Refresh every 12 hours
)
AS
SELECT
  DATE(TIMESTAMP_MICROS(event_timestamp)) AS activity_date,
  COUNT(DISTINCT user_pseudo_id) AS dau,
  COUNTIF(event_name = 'first_open') AS new_users
FROM
  `your-project.analytics_123456789.events_*`
WHERE
  _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
  AND event_name IN ('session_start', 'user_engagement', 'first_open')
GROUP BY activity_date;
```

#### Strategy 3: Use BigQuery BI Engine for Dashboards

```bash
# Reserve 1 GB of BI Engine capacity (free tier)
# This caches your most-used tables in memory for instant queries
bq update \
  --reservation \
  --project_id=$PROJECT_ID \
  --location=US \
  --bi_reservation_size=1073741824
```

#### Strategy 4: Monitor Your BigQuery Costs

```sql
-- Check how much data your queries have scanned this month
-- Run this in BigQuery (it queries the INFORMATION_SCHEMA)
SELECT
  user_email,
  COUNT(*) AS query_count,
  ROUND(SUM(total_bytes_processed) / POW(1024, 4), 4) AS total_tb_scanned,
  ROUND(SUM(total_bytes_processed) / POW(1024, 4) * 6.25, 2) AS estimated_cost_usd
FROM
  `region-us`.INFORMATION_SCHEMA.JOBS
WHERE
  creation_time >= TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), MONTH)
  AND job_type = 'QUERY'
  AND state = 'DONE'
GROUP BY user_email
ORDER BY total_tb_scanned DESC;
```

#### Strategy 5: Set BigQuery Cost Controls

```bash
# Set a maximum bytes billed per query (prevents expensive accidents)
# 10 GB = $0.0625 maximum per query
bq query \
  --use_legacy_sql=false \
  --maximum_bytes_billed=10737418240 \
  "SELECT COUNT(*) FROM \`your-project.analytics_123456789.events_*\`
   WHERE _TABLE_SUFFIX = FORMAT_DATE('%Y%m%d', CURRENT_DATE())"

# Set a project-level custom quota (optional, via GCP Console)
# Navigation: IAM & Admin → Quotas → BigQuery API → Query usage per day
```

#### Cost Estimation Cheat Sheet

| Data Volume | Monthly Scans | Monthly Cost | Status |
|-------------|---------------|-------------|--------|
| < 1 GB events/day | < 100 GB/month | $0.00 (free tier: 1 TB) | Safe |
| 1-5 GB events/day | 100 GB - 500 GB/month | $0.00 - $0.50 | Safe |
| 5-20 GB events/day | 500 GB - 2 TB/month | $0.50 - $6.25 | Watch it |
| 20+ GB events/day | 2+ TB/month | $6.25+ | Use materialized views |

**For solo developers:** You are almost certainly in the "Safe" tier. Firebase Analytics for an app with under 100K DAU generates well under 1 GB per day of event data. The 1 TB free tier covers roughly 1,000 full-table scans of a 1 GB table. You would need to run hundreds of queries per day to exceed it.

---

## Expected Output

After following this guide, your analytics pipeline should produce:

```markdown
## BigQuery Analytics Pipeline Summary

### Export Configuration
| Setting | Value |
|---------|-------|
| Firebase Project | my-android-app-prod |
| BigQuery Dataset | analytics_123456789 |
| Export Type | Daily + Streaming (intraday) |
| Region | US (multi-region) |
| First Data Available | 2026-02-02 |

### Key Metrics Dashboard (Last 7 Days)
| Metric | Value | Trend |
|--------|-------|-------|
| DAU (yesterday) | 847 | +12% WoW |
| WAU | 3,241 | +8% WoW |
| MAU | 8,920 | +15% MoM |
| Stickiness (DAU/MAU) | 9.5% | Stable |
| New Users (yesterday) | 124 | -5% WoW |

### Retention Cohort (Last 4 Weeks)
| Cohort Week | Size | D1 | D7 | D14 | D30 |
|-------------|------|-----|-----|------|------|
| Feb 3 - Feb 9 | 892 | 31.2% | 14.8% | -- | -- |
| Jan 27 - Feb 2 | 756 | 29.4% | 13.1% | 9.2% | -- |
| Jan 20 - Jan 26 | 810 | 28.8% | 12.5% | 8.7% | -- |
| Jan 13 - Jan 19 | 698 | 27.1% | 11.9% | 8.1% | 5.4% |

### Funnel Analysis: Onboarding
| Step | Users | % of Total | Drop-off |
|------|-------|-----------|----------|
| App Opened | 892 | 100% | -- |
| Tutorial Started | 714 | 80.0% | 20.0% |
| Tutorial Completed | 535 | 60.0% | 25.1% |
| Signed Up | 374 | 41.9% | 30.1% |
| First Action Done | 267 | 29.9% | 28.6% |

### Scheduled Reports
| Report | Schedule | Last Run | Status |
|--------|----------|----------|--------|
| Daily DAU | Daily 7 AM | Feb 10, 2026 | OK |
| Weekly Retention | Monday 8 AM | Feb 10, 2026 | OK |
| Monthly Revenue | 1st of month | Feb 1, 2026 | OK |

### BigQuery Cost This Month
| Metric | Value |
|--------|-------|
| Queries Run | 87 |
| Data Scanned | 4.2 GB |
| Free Tier Used | 0.4% of 1 TB |
| Estimated Cost | $0.00 |
```

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defined the specific analytics pipeline goal with concrete questions it should answer
- **ST-02 (Sequential Step-by-Step Instructions):** Phased approach from export setup through schema understanding to production queries and cost control
- **RT-02 (Multi-Dimensional Analysis):** Analyzed user behavior across retention, funnels, revenue, engagement, and acquisition dimensions
- **CM-01 (Contextual Framing):** All queries and examples tailored for solo developer with Firebase Android app
- **DS-06 (Prioritization and Severity Guidance):** Ordered queries by importance (retention first, then funnels, then revenue)
- **DS-02 (Metric Specification):** Concrete benchmarks for retention, stickiness, and cost thresholds
- **RT-05 (Evidence-Based Reasoning):** Included industry benchmarks for retention and engagement metrics

---

## Related Prompts

- `gcp_solo_dev_cost_management.md` -- Budget management including BigQuery cost monitoring
- `gcp_monitoring_alerting_setup.md` -- Monitoring your analytics pipeline health
- `cloud_gcp_best_practices.md` -- Broader GCP architecture including data pipelines
- `cloud_cost_optimization.md` -- General cost optimization strategies that apply to BigQuery
- `gcp_cloud_run_backend.md` -- Backend that generates the events your analytics pipeline tracks

---

## Customization Guide

- **For apps with < 1,000 DAU:** The retention and funnel queries will work but produce small sample sizes. Focus on funnel analysis (where are users dropping off) rather than cohort trends (which need larger numbers to be meaningful). Skip scheduled reports until you have enough data to act on.
- **For apps with revenue (IAP or subscriptions):** Add the revenue queries as your primary focus. LTV by acquisition channel should drive your marketing spend decisions. Add a scheduled monthly revenue report.
- **For multi-platform apps (Android + iOS + Web):** Add `platform` to your GROUP BY clauses to see retention and funnels broken down by platform. Platform-specific engagement patterns are common (e.g., web users churn faster than mobile).
- **For gaming apps:** Replace the generic engagement events with game-specific events (level_complete, achievement_unlocked, virtual_currency_spent). Gaming retention benchmarks are different -- Day 1 of 40%+ is expected for casual games.
- **For apps using Google Analytics 4 (not Firebase):** The BigQuery schema is nearly identical. Replace `analytics_XXXXXX` with your GA4 property's dataset name. The main difference is the `traffic_source` field structure.
- **For Looker Studio dashboards:** Connect Looker Studio directly to your BigQuery dataset or to the `analytics_reports` dataset containing scheduled query results. Use materialized views as the data source for faster dashboard loads.
