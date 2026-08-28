---
title: "Firebase Analytics Strategy"
category: mobile-development
description: "Design a Firebase Analytics implementation — core events, naming conventions, custom dimensions, funnel definition, BigQuery export, and avoiding the over-instrumentation trap"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - CM-02
  - DS-06
difficulty: beginner
tags:
  - android
  - firebase
  - analytics
  - data-driven
  - mobile-development
  - solo-developer
updated: "2026-02-11"
---

# Firebase Analytics Strategy

**Objective:** Design a focused Firebase Analytics implementation for an Android app — identifying 5-7 core events (not everything), establishing consistent naming conventions, defining custom parameters and user properties, building funnels for critical user flows, planning BigQuery export for advanced analysis, and avoiding the over-instrumentation trap — producing an analytics plan that drives actionable decisions without drowning in data.

**When to Use:** Use this prompt when setting up analytics for a new app, when your current analytics implementation is noisy and unhelpful, when you're about to launch and need to know what to measure, or when you're making product decisions and realize you don't have the data to support them. Critical because data-driven decisions require good data from day one — retrofitting analytics after launch means losing months of baseline data.

**Important context:** The biggest analytics mistake solo developers make is tracking everything. Firebase Analytics automatically tracks dozens of events (screen views, sessions, app updates, OS updates, etc.). Your job is NOT to add more events — it's to add the 5-7 events that tell you whether your business is working. If you can't explain why you're tracking something and what you'd do differently based on the data, don't track it.

---

## Context Gathering

Before designing the analytics strategy, gather essential context:

1. **App and Business Model:**
   - "What does your app do and what is its core value proposition?"
   - "How does it monetize (free, freemium, subscription, ads, paid)?"
   - "What is the single most important action a user can take in your app?"
   - "What does a 'successful' user look like after 7 days? After 30 days?"

2. **Current State:**
   - "Is Firebase Analytics already integrated?"
   - "Are you logging any custom events currently?"
   - "Do you have BigQuery export enabled?"
   - "What questions about your users can you NOT answer today?"

3. **Key Questions to Answer:**
   - "What do you most want to know about how users use your app?"
   - "What product decisions are you trying to make right now?"
   - "What would cause you to change your roadmap?"
   - "How do you currently decide what to build next?"

4. **Technical Context:**
   - "What screens or features are most important to your app's value?"
   - "Do you have a subscription or purchase flow?"
   - "Do you have an onboarding flow?"
   - "Are there distinct user segments (free vs. paid, casual vs. power user)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY analytics event, you MUST:**

1. **Verify it's actionable** — For every event, answer: "If this number goes up or down, what would I do differently?" If you can't answer that, don't track it.
2. **Check if Firebase already tracks it** — Firebase automatically tracks: `first_open`, `session_start`, `screen_view`, `app_update`, `os_update`, `in_app_purchase`, and more. Don't duplicate automatic events.
3. **Keep the event count low** — 5-7 custom events is the target. More than 15 custom events and you'll never look at most of them.
4. **Use consistent naming** — All events and parameters must follow a documented naming convention. Inconsistency makes analysis impossible.
5. **Respect user privacy** — Never log personally identifiable information (PII) in events or parameters. Firebase prohibits this.

### False-Positive Prevention

- ❌ Do NOT recommend tracking every button tap and screen view — this creates noise, not insight
- ❌ Do NOT suggest event names that contain PII (email addresses, user IDs in event names, etc.)
- ❌ Do NOT duplicate events Firebase already tracks automatically
- ❌ Do NOT create events without clear parameters — `click` means nothing without context
- ❌ Do NOT recommend BigQuery export if the developer won't actually query it
- ✅ DO focus on events that map to business outcomes (retention, monetization, engagement)
- ✅ DO provide the specific question each event answers
- ✅ DO keep the total custom event count under 10
- ✅ DO include the decision each metric drives
- ✅ DO recommend starting with fewer events and adding more only when needed

---

### Phase 1: Define What Matters

#### 1.1 The Core Metrics Framework

Every app should track these universal metrics (most are built into Firebase):

| Metric | Source | What It Tells You | Action If Low |
|--------|--------|-------------------|---------------|
| **Daily Active Users (DAU)** | Firebase automatic | How many people use your app daily | Improve retention or acquisition |
| **Day-1 Retention** | Firebase automatic | First impression quality | Improve onboarding |
| **Day-7 Retention** | Firebase automatic | Core value delivery | Improve core feature |
| **Day-30 Retention** | Firebase automatic | Long-term stickiness | Add engagement loops |
| **Session Duration** | Firebase automatic | Engagement depth | Improve content/features |
| **Crash-Free Rate** | Crashlytics | Technical quality | Fix crashes |

**You get ALL of these for free.** No custom events needed.

#### 1.2 Identify Your 5-7 Core Custom Events

The custom events you add should answer business-specific questions. Use this framework:

```markdown
## Core Event Design

For each event, fill in:

Event: [name]
Question it answers: "[What will I learn from this data?]"
Decision it drives: "[If this number changes, I would...]"
Trigger: [When exactly this event fires]
Key parameters: [What context to include]
```

**Common event patterns by app type:**

**Freemium/Subscription App:**
1. `onboarding_completed` — Are users finishing setup?
2. `core_action_performed` — Are users getting value? (define YOUR core action)
3. `paywall_shown` — How often do users hit the upgrade prompt?
4. `subscription_started` — Conversion rate from free to paid
5. `feature_limit_reached` — Are free limits set correctly?
6. `share_initiated` — Is the app generating word-of-mouth?

**Ad-Supported App:**
1. `onboarding_completed` — Are users finishing setup?
2. `core_action_performed` — Are users engaging?
3. `content_consumed` — What content drives engagement?
4. `ad_interaction` — Ad engagement quality (supplemented by AdMob)
5. `session_milestone` — Do users stay long enough for ads to work?

**Productivity/Tool App:**
1. `onboarding_completed` — Are users finishing setup?
2. `first_value_moment` — When does the user first get value?
3. `core_action_performed` — Are users performing the key action?
4. `data_created` — Are users investing in the app (creating content they'd lose if they left)?
5. `export_or_share` — Are users getting output from the app?

#### 1.3 Naming Convention

Adopt a strict naming convention and document it. Firebase event names must be:
- Max 40 characters
- Alphanumeric + underscores only
- Must start with a letter

**Recommended convention:**

```
[object]_[action]
```

| Pattern | Examples |
|---------|----------|
| `object_action` | `task_created`, `profile_updated`, `photo_shared` |
| `flow_milestone` | `onboarding_completed`, `checkout_started` |
| `feature_engagement` | `search_used`, `filter_applied` |

**Naming rules:**
- Use `snake_case` (Firebase convention)
- Use past tense for completed actions: `task_created` not `create_task`
- Use present tense for ongoing states: `paywall_shown` not `showed_paywall`
- Be specific: `photo_shared` not `share` (share what? where?)
- Never abbreviate: `subscription_started` not `sub_start`

---

### Phase 2: Event Implementation

#### 2.1 Event Parameter Design

Each event should include 1-4 parameters that provide context:

```kotlin
// Example: Core action event with parameters
Firebase.analytics.logEvent("task_created") {
    param("task_type", taskType)           // "grocery", "todo", "reminder"
    param("has_due_date", hasDueDate)      // true/false
    param("source_screen", sourceScreen)   // "home", "quick_add", "widget"
    param("item_count", itemCount.toLong()) // number of items
}
```

**Parameter rules:**
- Max 25 custom parameters per event
- String values max 100 characters
- Parameter names max 40 characters, alphanumeric + underscores
- Never include PII (emails, phone numbers, precise location, device IDs)

**Standard parameters to include on most events:**

| Parameter | When to Include | Example Values |
|-----------|----------------|----------------|
| `source_screen` | When action can happen from multiple places | `"home"`, `"search"`, `"notification"` |
| `user_tier` | When free vs paid matters | `"free"`, `"premium"` |
| `content_type` | When there are different types | `"photo"`, `"text"`, `"video"` |
| `success` | When action can fail | `true`, `false` |

#### 2.2 User Properties

User properties segment your entire user base. Set sparingly (max 25 custom).

**Recommended user properties:**

| Property | Value Type | Example | Why Track |
|----------|-----------|---------|-----------|
| `user_tier` | String | `"free"` / `"premium"` | Segment all metrics by paid status |
| `signup_method` | String | `"google"` / `"email"` | Understand acquisition quality |
| `app_version_first` | String | `"2.3.0"` | Cohort analysis by version |
| `onboarding_completed` | Boolean | `true` / `false` | Segment by setup completion |

```kotlin
// Set user properties after relevant events
Firebase.analytics.setUserProperty("user_tier", "premium")
Firebase.analytics.setUserProperty("onboarding_completed", "true")
```

#### 2.3 Funnel Definition

Define 2-3 funnels for your most important user flows:

**Funnel 1: Onboarding**
```
Step 1: first_open (automatic)
Step 2: onboarding_step_completed (param: step = "profile")
Step 3: onboarding_step_completed (param: step = "preferences")
Step 4: onboarding_completed
Step 5: core_action_performed (first time)
```

**Funnel 2: Conversion (freemium)**
```
Step 1: feature_limit_reached
Step 2: paywall_shown
Step 3: subscription_started
```

**Funnel 3: Engagement loop**
```
Step 1: app_open (session_start)
Step 2: core_action_performed
Step 3: content_consumed / result_viewed
Step 4: share_initiated (optional)
```

---

### Phase 3: Implementation Checklist

#### 3.1 Android Implementation

```kotlin
// Initialize in Application class or MainActivity
// Firebase Analytics is auto-initialized — no setup needed

// Log a custom event
fun logCoreAction(actionType: String, screen: String) {
    Firebase.analytics.logEvent("core_action_performed") {
        param("action_type", actionType)
        param("source_screen", screen)
    }
}

// Set screen name for screen_view tracking
fun setCurrentScreen(activity: Activity, screenName: String) {
    Firebase.analytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW) {
        param(FirebaseAnalytics.Param.SCREEN_NAME, screenName)
        param(FirebaseAnalytics.Param.SCREEN_CLASS, activity::class.java.simpleName)
    }
}

// Disable analytics for debug builds (optional)
if (BuildConfig.DEBUG) {
    Firebase.analytics.setAnalyticsCollectionEnabled(false)
}
```

#### 3.2 DebugView Setup

Use Firebase DebugView to verify events in real-time during development:

```bash
# Enable debug mode on your test device
adb shell setprop debug.firebase.analytics.app com.your.package.name

# Disable when done
adb shell setprop debug.firebase.analytics.app .none.
```

Then open Firebase Console → Analytics → DebugView to see events in real-time.

#### 3.3 Data Safety Declaration

Firebase Analytics collects data that must be declared in the Play Store Data Safety section:

- **Device info** — Device model, OS version (Diagnostics)
- **App interactions** — Events, screen views (App activity)
- **Advertising ID** — If ad features enabled (Advertising)

---

### Phase 4: Analysis and Action

#### 4.1 Weekly Analytics Review (15 minutes)

```markdown
Every Monday, check:
1. DAU trend — Up, down, or flat vs last week?
2. Core action count — Are users doing the key thing?
3. Crash-free rate — Above 99%?
4. Retention (day-1, day-7) — Trending in the right direction?
5. One funnel — Where are users dropping off?
```

#### 4.2 BigQuery Export (Optional — When You Need It)

Enable BigQuery export when you need to:
- Run queries Firebase Console can't handle
- Build custom cohort analysis
- Correlate analytics with external data
- Create automated reports

**Setup:** Firebase Console → Project Settings → Integrations → BigQuery → Link

**Useful BigQuery queries:**

```sql
-- Daily active users by user property
SELECT
  event_date,
  user_properties.value.string_value AS user_tier,
  COUNT(DISTINCT user_pseudo_id) AS users
FROM `project.analytics_XXXXX.events_*`
CROSS JOIN UNNEST(user_properties) AS user_properties
WHERE user_properties.key = 'user_tier'
  AND _TABLE_SUFFIX BETWEEN '20260101' AND '20260131'
GROUP BY event_date, user_tier
ORDER BY event_date;

-- Conversion funnel
SELECT
  COUNT(DISTINCT IF(event_name = 'paywall_shown', user_pseudo_id, NULL)) AS saw_paywall,
  COUNT(DISTINCT IF(event_name = 'subscription_started', user_pseudo_id, NULL)) AS subscribed,
  SAFE_DIVIDE(
    COUNT(DISTINCT IF(event_name = 'subscription_started', user_pseudo_id, NULL)),
    COUNT(DISTINCT IF(event_name = 'paywall_shown', user_pseudo_id, NULL))
  ) AS conversion_rate
FROM `project.analytics_XXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20260101' AND '20260131';
```

**Cost warning:** BigQuery charges per query based on data scanned. Always use `_TABLE_SUFFIX` to limit date range. A full table scan of a year's data can cost $5-50+.

#### 4.3 Avoid the Vanity Metrics Trap

| Vanity Metric | Why It's Misleading | Better Alternative |
|---------------|--------------------|--------------------|
| Total downloads | Includes churned users | DAU or MAU |
| Total events | More events ≠ more engagement | Core actions per session |
| Average session duration | Inflated by background sessions | Median session duration |
| Page views | Can be inflated by navigation | Screen engagement time |
| "Users" without segmentation | Averages hide segments | Segment by user tier/cohort |

---

## Expected Output

### Firebase Analytics Strategy Document

```markdown
# Analytics Strategy: [App Name]

## Core Questions This Analytics Plan Answers
1. [Business question 1]
2. [Business question 2]
3. [Business question 3]

## Automatic Events (No Custom Code Needed)
- first_open, session_start, screen_view, app_update, in_app_purchase
- Used for: DAU, retention, session analysis

## Custom Events ([N] events)

| # | Event Name | Question Answered | Parameters | Trigger |
|---|-----------|-------------------|------------|---------|
| 1 | [event] | [question] | [params] | [when] |
| 2 | [event] | [question] | [params] | [when] |
| ... | | | | |

## User Properties ([N] properties)

| Property | Values | Segmentation Purpose |
|----------|--------|---------------------|
| [prop] | [values] | [why] |

## Funnels

### Funnel 1: [Name]
[Steps with expected conversion rates]

### Funnel 2: [Name]
[Steps with expected conversion rates]

## Naming Convention
[Documented naming rules]

## Weekly Review Checklist
[5-item checklist with where to find each metric]

## Data Safety Impact
[What to declare in Play Store Data Safety section]

## BigQuery: [Enabled/Deferred]
[Rationale for decision]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Analytics strategy focus
- **ST-02** (Structured Sequential Instructions) - Phased implementation process
- **RT-02** (Multi-Dimensional Analysis) - Multiple metric dimensions
- **CM-01** (Explicit Context Framing) - Firebase Analytics capabilities and limitations
- **CM-02** (Constraint Specification) - Event limits, naming rules, privacy requirements
- **DS-06** (Prioritization Guidance) - Core events vs nice-to-have

---

## Related Prompts

- `firestore_data_model_design.md` - Data model that generates analytics events
- `firebase_cost_monitor_setup.md` - Cost monitoring including BigQuery export costs
- `domain-productivity/reviews/reviews_solo_dev_weekly_operating_rhythm.md` - Weekly analytics review cadence
- `monetization_model_selector.md` - Monetization metrics to track
- `solo_dev_metrics_dashboard.md` - Dashboard design for key metrics (planned)

---

## Customization Guide

- **For subscription apps:** Expand the conversion funnel with trial start, trial end, renewal, and churn events. Track `subscription_status` as a user property.
- **For content/media apps:** Add content engagement events (content_started, content_completed, content_rated). Track content categories for recommendation insights.
- **For e-commerce apps:** Use Firebase's recommended e-commerce events (add_to_cart, begin_checkout, purchase) which integrate with Google Ads.
- **For games:** Track level progression, in-game currency, and session milestones. Firebase has game-specific event recommendations.
- **For apps not yet launched:** Start with just 3 events (onboarding_completed, core_action_performed, one monetization event). Add more only after you've looked at these for 2 weeks and know what questions remain unanswered.
