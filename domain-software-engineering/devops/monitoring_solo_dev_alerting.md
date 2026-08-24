---
title: "Solo Developer Alerting Strategy"
category: devops
description: "Design a sustainable 3-tier alerting system for a single developer managing production applications. Covers P1/P2/P3 alert classification, threshold tuning to prevent notification fatigue, channel routing (SMS/Slack/email), and on-call sustainability practices that prevent burnout."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DS-06  # Prioritization Guidance
  - CM-02  # Constraint Specification
difficulty: intermediate
tags:
  - monitoring
  - alerting
  - solo-developer
  - android
  - devops
  - on-call
  - notification-fatigue
  - firebase
updated: "2026-02-11"
related_prompts:
  - domain-software-engineering/mobile/android/targeted-reviews/firebase_incident_response.md
  - domain-software-engineering/mobile/android/targeted-reviews/firebase_cost_monitor_setup.md
  - domain-software-engineering/mobile/android/targeted-reviews/firebase_health_check.md
  - domain-software-engineering/devops/devops_monitoring_strategy.md
---

# Solo Developer Alerting Strategy

**Objective:** Design and implement a 3-tier alerting system for a single developer managing one or more production applications. The system must distinguish between "wake me up now" emergencies (P1), "check this in the morning" degradations (P2), and "review this next week" trends (P3), with notification channel routing, threshold tuning, and explicit fatigue prevention mechanisms -- all built around the constraint that there is exactly one person who will receive and respond to every alert.

## When to Use

- Use when: You are a solo developer launching or operating a production application and need to set up monitoring alerts
- Use when: Your current alerting is either too noisy (alert fatigue) or too quiet (missing real issues)
- Use when: You want to establish sustainable on-call practices for one person
- Use when: Transitioning from "I check the dashboard manually" to automated alerting
- Do not use when: You have a team with on-call rotation (use standard SRE alerting practices)
- Do not use when: You need to set up the monitoring infrastructure itself (this guide assumes monitoring tools are already in place)

**Important context:** The fundamental challenge of solo developer alerting is not technical -- it is psychological. With a team, you share the cognitive load. Alone, every alert is your problem. The most dangerous failure mode is not "I missed an alert" but "I stopped caring about alerts because 90% of them were noise." This guide prioritizes alert quality (signal-to-noise ratio) over alert coverage (catching everything). A solo developer who responds effectively to 5 real alerts per week will outperform one who is numb to 50 noisy alerts per day.

---

## Context Gathering

Before designing your alerting system, gather:

1. **Application Landscape:**
   - "How many production applications do you maintain?"
   - "What services does each app depend on? (Firebase, REST APIs, databases, CDNs)"
   - "What is the revenue model? (Ads, subscriptions, in-app purchases, free)"
   - "What are your SLA commitments, if any?"

2. **Current Monitoring:**
   - "What monitoring tools are in place? (Firebase Crashlytics, Performance Monitoring, Google Cloud Monitoring, Uptime Robot, Better Stack, etc.)"
   - "What alerts do you currently receive? How many per day/week?"
   - "Which alerts have you actually acted on in the last month?"
   - "Which alerts do you routinely ignore?"

3. **Personal Schedule:**
   - "What are your working hours?"
   - "Are you willing to be woken up for production issues? Under what conditions?"
   - "Do you have designated 'off' periods where someone else covers? (Even if the answer is 'no')"
   - "What devices do you always have with you? (Phone, watch, laptop)"

4. **Communication Channels:**
   - "What notification channels are available? (SMS, phone call, Slack, Discord, email, push notification)"
   - "Which channels reach you fastest in each context? (Working, sleeping, weekend)"
   - "Do you have a status page for users?"

5. **Risk Tolerance:**
   - "What is the maximum acceptable downtime before users notice?"
   - "What financial loss per hour of downtime?"
   - "Are there regulatory requirements for incident response time?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before adding ANY new alert, you MUST answer these three questions:**

1. **Is this actionable?** -- If the alert fires, is there a specific action you can take? If not, it is a metric to watch, not an alert to receive.
2. **Does this require immediate action?** -- If it can wait until morning or next week, it should not wake you up. Classify the tier correctly.
3. **Would you act differently based on this alert?** -- If the answer is "I'd check the dashboard," then you do not need the alert -- you need a better dashboard.

**The goal is NOT to alert on everything that could go wrong. The goal is to alert on the minimum set of conditions where your intervention changes the outcome.**

### False-Positive Prevention

- Do NOT set thresholds based on zero tolerance (e.g., "alert if ANY error occurs") -- baseline noise will drown out real signals
- Do NOT create alerts for conditions you cannot fix (e.g., "third-party API is slow") -- monitor these, but only alert if YOUR response to their slowness requires action
- Do NOT duplicate alerts across multiple tools for the same condition -- one source of truth per alert
- Do NOT set P1 alerts for anything that has a workaround or graceful degradation -- if the app still works, it is P2 at most
- Do NOT alert on metrics without context (e.g., "CPU is high") -- alert on user impact ("response time > 5s for > 5 minutes")
- DO base thresholds on historical data, not gut feeling -- use percentile analysis of normal operation
- DO require sustained conditions, not spikes (e.g., "error rate > 5% for 10 minutes" not "error rate > 5% once")
- DO include "alert on absence" -- if you stop receiving data, that itself is an alert (monitoring is broken)
- DO review and prune alerts quarterly -- alerts that never fire or always fire should be removed or recalibrated
- DO test your alerts by intentionally triggering them at least once

---

### Phase 1: Alert Tier Design

Define three tiers of alerts with clear boundaries and escalation criteria.

#### Tier 1 (P1): Wake Up Now

**Purpose:** Something is happening that will get worse if you do not act immediately. User-facing impact is occurring NOW or imminent. Financial loss is active.

**Criteria -- ALL of these must be true for P1:**
1. Users are currently affected OR will be within minutes
2. No automated recovery or graceful degradation is handling it
3. Your intervention will meaningfully change the outcome
4. The impact grows the longer you wait

```markdown
## P1 Alert Definitions

### Application Down
- **Condition:** App health endpoint returns non-200 for > 3 consecutive checks (5 min)
- **Why P1:** All users affected, revenue impact immediate
- **Action:** Check status page, identify root cause, invoke outage runbook
- **Channel:** SMS + phone call

### Security Breach Detected
- **Condition:** Anomalous authentication pattern (>10x normal signups in 1 hour)
  OR Firebase security rule violation spike (>100 denials in 10 minutes)
- **Why P1:** Data exposure risk, potential regulatory implications
- **Action:** Invoke security breach runbook
- **Channel:** SMS + phone call

### Cost Spike (Runaway)
- **Condition:** Firebase/cloud billing exceeds 3x daily average OR
  budget threshold crossed
- **Why P1:** Unbounded financial exposure
- **Action:** Identify and stop the cost source
- **Channel:** SMS

### Data Loss Detected
- **Condition:** Database document count drops >10% in 1 hour OR
  backup verification fails
- **Why P1:** Irreversible data loss possible
- **Action:** Freeze writes, investigate, restore from backup
- **Channel:** SMS + phone call

### Critical Crash Spike
- **Condition:** Crash-free rate drops below 95% (from Crashlytics)
  AND affects latest app version AND > 100 users affected
- **Why P1:** Massive user impact, likely needs hotfix or rollback
- **Action:** Assess crash, prepare hotfix, consider staged rollout halt
- **Channel:** SMS
```

**P1 Budget:** Target 0-2 P1 alerts per month. If you are getting more, your thresholds are too sensitive or your system has fundamental stability issues.

#### Tier 2 (P2): Check This Morning

**Purpose:** Something is degraded but not critical. Users may notice but the app still works. The issue will not significantly worsen overnight.

**Criteria for P2:**
1. Service is degraded but functional
2. The issue is not actively getting worse (or is getting worse slowly)
3. A few hours of delay in response will not materially change the outcome
4. There is a workaround or graceful degradation in place

```markdown
## P2 Alert Definitions

### Elevated Error Rate
- **Condition:** API error rate > 5% for > 30 minutes
  (but app is still functional overall)
- **Why P2:** Degraded experience but not down
- **Action:** Investigate error source, check third-party dependencies
- **Channel:** Slack/Discord notification

### Performance Degradation
- **Condition:** 95th percentile response time > 3x baseline for > 1 hour
- **Why P2:** Slow but working
- **Action:** Check for inefficient queries, increased load, or backend issues
- **Channel:** Slack/Discord notification

### Crash Rate Elevated (Moderate)
- **Condition:** Crash-free rate 95-98% (normally >99%)
  OR new crash signature appearing in Crashlytics
- **Why P2:** Users impacted but not at crisis level
- **Action:** Investigate crash, plan fix for next release
- **Channel:** Slack/Discord notification

### Firebase Quota Warning
- **Condition:** Usage at 80% of free tier quota
  OR spending at 60% of daily budget
- **Why P2:** Not an emergency yet, but heading there
- **Action:** Review usage patterns, optimize if needed
- **Channel:** Slack/Discord notification

### Certificate/Token Expiration
- **Condition:** SSL cert, API key, or auth token expires in < 14 days
- **Why P2:** No impact yet, but will become P1 if ignored
- **Action:** Renew before expiration
- **Channel:** Slack/Discord notification

### Dependency Health Warning
- **Condition:** Third-party API returning errors intermittently
  OR dependency status page shows degradation
- **Why P2:** May need to activate fallback
- **Action:** Monitor and prepare fallback if needed
- **Channel:** Slack/Discord notification
```

**P2 Budget:** Target 3-7 P2 alerts per week. If you are getting more than 2 per day, tighten thresholds or fix the underlying instability.

#### Tier 3 (P3): Weekly Review

**Purpose:** Trends, minor issues, and informational data that informs engineering decisions but requires no immediate action.

**Criteria for P3:**
1. No user impact currently
2. May indicate future issues if trends continue
3. Useful for weekly planning and prioritization
4. Can be batch-processed during scheduled review time

```markdown
## P3 Alert Definitions (Delivered as Weekly Digest)

### Trend: Increasing Error Rate
- **Condition:** Week-over-week error rate increase > 20%
- **Action:** Add to next sprint investigation queue

### Trend: Slow Performance Drift
- **Condition:** Month-over-month p95 latency increase > 15%
- **Action:** Schedule performance review

### Trend: Growing Storage Usage
- **Condition:** Storage growth rate will exceed quota in < 90 days
- **Action:** Plan cleanup or upgrade

### Minor: Deprecated API Warnings
- **Condition:** Logs contain deprecation warnings from dependencies
- **Action:** Schedule dependency update

### Minor: Low-Volume Crash Signatures
- **Condition:** New crash types affecting < 10 users
- **Action:** Triage and prioritize

### Informational: User Growth/Decline
- **Condition:** DAU/MAU change > 20% week-over-week
- **Action:** Investigate cause (marketing, churn, viral, etc.)

### Informational: Cost Forecast
- **Condition:** Projected monthly cost based on current trajectory
- **Action:** Review for budget planning
```

**P3 Budget:** One digest per week. If you find yourself ignoring the digest, reduce its contents to only the metrics you actually act on.

---

### Phase 2: Threshold Tuning

Set alert thresholds based on data, not intuition.

#### 2.1 Establish Baselines

```bash
# Collect 30 days of baseline data for key metrics
# Example using Google Cloud Monitoring MQL (Monitoring Query Language)

# Error rate baseline
fetch https_lb_rule
| metric 'loadbalancing.googleapis.com/https/request_count'
| filter status >= 500
| align rate(1m)
| every 1h
| group_by [], [value_count_mean: mean(val())]

# Latency baseline
# Firebase Performance Monitoring: Dashboard > Network requests
# Export 30-day p50, p95, p99 data

# Crash rate baseline
# Crashlytics: Dashboard > Crash-free users > 30-day trend
```

#### 2.2 Calculate Thresholds

```markdown
## Threshold Calculation Method

For each metric:
1. Collect 30 days of data at the granularity you plan to alert on
2. Calculate the statistical distribution (mean, p50, p95, p99)
3. Set P1 threshold at: p99 + 50% margin (catches truly abnormal conditions)
4. Set P2 threshold at: p95 + 25% margin (catches concerning but not critical conditions)
5. Validate by checking how many times each threshold would have fired in the last 30 days

### Example: API Error Rate
- 30-day mean: 0.3%
- p95: 1.2%
- p99: 3.8%
- P1 threshold: > 5% for > 10 minutes (would have fired 0 times in 30 days)
- P2 threshold: > 2% for > 30 minutes (would have fired 2 times in 30 days)

### Example: Response Time (p95)
- 30-day mean p95: 450ms
- p95 of p95: 1200ms
- p99 of p95: 2800ms
- P1 threshold: p95 > 5000ms for > 5 minutes (absolute functional limit)
- P2 threshold: p95 > 1500ms for > 1 hour (degraded but functional)
```

#### 2.3 Anti-Flap Configuration

```markdown
## Preventing Alert Flapping

Alert flapping (rapid on/off/on/off) is the #1 cause of alert fatigue.

### Required Anti-Flap Settings:
- **Evaluation window:** Minimum 5 minutes for P1, 15 minutes for P2
- **Recovery delay:** Alert must be clear for 2x the evaluation window before auto-resolving
- **Minimum duration:** Condition must persist for full evaluation window
- **Aggregation:** Use averages over the window, not point-in-time values

### Example Configuration (Google Cloud Monitoring):
| Setting | P1 | P2 |
|---------|----|----|
| Evaluation window | 5 min | 15 min |
| Consecutive failures | 3 checks | 5 checks |
| Recovery window | 10 min | 30 min |
| Notification cooldown | 30 min | 2 hours |
```

---

### Phase 3: Channel Routing

Route alerts to the right notification channel based on tier and context.

#### 3.1 Channel Assignment Matrix

```markdown
## Notification Channel Routing

| Tier | Working Hours | After Hours | Weekend |
|------|--------------|-------------|---------|
| **P1** | SMS + Slack | SMS + Phone Call | SMS + Phone Call |
| **P2** | Slack | Slack (quiet) | Suppress until Monday AM |
| **P3** | Email digest (weekly) | N/A | N/A |

### Channel Specifications:
- **SMS:** For P1 only. Must reach you even with Do Not Disturb enabled.
  Configure DND bypass for monitoring phone number.
- **Phone Call:** For P1 after-hours only. Repeated call if not acknowledged.
  Services: PagerDuty, Better Stack, or Twilio auto-call.
- **Slack/Discord:** For P2 during work hours. Use a dedicated #alerts channel.
  Mute notifications outside work hours.
- **Email:** For P3 weekly digest only. Single summary email, not individual alerts.
```

#### 3.2 Channel Configuration

```yaml
# Example: Better Stack (formerly Uptime) configuration
# betterstack.yml

escalation_policy:
  name: "Solo Dev Escalation"
  steps:
    - step: 1
      wait_before_escalating: 0
      targets:
        - type: "sms"
          phone: "+1XXXXXXXXXX"

    - step: 2
      wait_before_escalating: 5  # minutes
      targets:
        - type: "phone_call"
          phone: "+1XXXXXXXXXX"

    - step: 3
      wait_before_escalating: 15  # minutes
      targets:
        - type: "sms"
          phone: "+1XXXXXXXXXX"  # Repeat SMS as reminder

# P2 routing (Slack only)
# Use Slack webhook with no phone escalation

# P3 routing (Email digest)
# Configure weekly scheduled report
```

#### 3.3 DND Bypass Setup

```markdown
## Phone Do Not Disturb Configuration

### iOS:
1. Settings > Focus > Do Not Disturb
2. Allow Notifications From: [Monitoring phone number]
3. OR: Allow Repeated Calls (same number calls twice in 3 min)

### Android:
1. Settings > Sound > Do Not Disturb
2. Exceptions > Calls from: Starred contacts
3. Star your monitoring service phone number
4. OR: Allow repeat callers

### Key principle: Only P1 alerts should bypass DND.
P2 and P3 should NEVER interrupt sleep or personal time.
```

---

### Phase 4: Fatigue Prevention

Implement explicit mechanisms to prevent alert fatigue -- the single biggest threat to solo developer alerting.

#### 4.1 Alert Budget System

```markdown
## Weekly Alert Budget

Assign a maximum number of alerts per tier per week.
If you exceed the budget, the problem is your alerting, not your app.

| Tier | Weekly Budget | Action if Exceeded |
|------|-------------|-------------------|
| P1 | 0-2 | If >2, you have a stability problem. Fix the root cause. |
| P2 | 3-7 | If >7, raise thresholds. You are alerting on noise. |
| P3 | 1 digest | If digest is >20 items, reduce to top 10. |

### Monthly Alert Review:
Every month, run this analysis:
1. Count total alerts per tier
2. Count alerts that led to action vs alerts that were noise
3. Calculate signal-to-noise ratio: (actionable / total) x 100%
4. Target: >70% signal-to-noise ratio
5. If below 70%: tighten thresholds, remove noisy alerts, or consolidate
```

#### 4.2 Noise Reduction Techniques

```markdown
## Techniques to Reduce Alert Noise

### 1. Alert Grouping
Combine related alerts into a single notification.
- BAD: 5 separate alerts for 5 endpoints returning 500
- GOOD: 1 alert: "API error rate elevated across 5 endpoints"

### 2. Dependent Alert Suppression
If a downstream service is down, suppress alerts for everything that depends on it.
- BAD: Firebase down + 10 alerts for features that use Firebase
- GOOD: Firebase down + suppressed dependent alerts

### 3. Maintenance Windows
Suppress non-P1 alerts during scheduled maintenance.
- Deploy window: suppress P2/P3 for 30 minutes after deploy
- Database migration: suppress for duration of migration

### 4. Progressive Thresholds
Tighten thresholds during business hours, loosen during off-hours.
- Business hours P2: error rate > 2%
- Off-hours P2: error rate > 5% (higher threshold because lower impact)

### 5. One-Alert-Per-Incident
Once an incident is acknowledged, suppress duplicate alerts for the same issue.
- Use alert deduplication keys
- Suppress duplicates for 1 hour after acknowledgment
```

#### 4.3 Alert Audit Quarterly Review

```markdown
## Quarterly Alert Audit

Every quarter, review every alert definition:

### For each alert, answer:
1. Has this alert fired in the last 90 days?
   - If NO: Is it still relevant? Remove or recalibrate.

2. When it fired, did I take action?
   - If NO: Remove the alert. It is noise.

3. Was the action it prompted the right action?
   - If NO: Rewrite the alert or the runbook.

4. Could this alert be merged with another?
   - If YES: Consolidate to reduce volume.

5. Is the threshold still appropriate?
   - If baseline has changed: Recalculate using Phase 2 method.

### Audit Template:
| Alert Name | Times Fired (90d) | Times Acted On | S/N Ratio | Action |
|-----------|-------------------|----------------|-----------|--------|
| App down | 1 | 1 | 100% | Keep |
| Error rate P2 | 12 | 3 | 25% | Raise threshold |
| CPU warning | 8 | 0 | 0% | Remove |
| Cost alert | 2 | 2 | 100% | Keep |
```

---

### Phase 5: Sustainability

Design on-call practices that prevent burnout for a single person.

#### 5.1 Sustainable On-Call Practices

```markdown
## On-Call Sustainability for One Person

### Rule 1: Define "Off" Times
Even as a solo dev, you MUST have times when you are unreachable.
- Designate 1 day per week as "no alerts except P1"
- P1 alerts still reach you (app down, security breach)
- P2 and P3 are completely suppressed

### Rule 2: Automate First, Alert Second
Before creating an alert, ask: "Can I automate the response?"
- Auto-restart crashed processes
- Auto-scale on resource pressure
- Auto-rollback on deployment failure
- Auto-disable features via Remote Config on error threshold
- THEN alert only if automation fails

### Rule 3: Batch P2 Review
Do not check P2 alerts continuously throughout the day.
- Schedule two P2 review windows: 9 AM and 2 PM
- Outside those windows, P2 notifications are muted
- This preserves focus time for feature development

### Rule 4: Weekly P3 Review Session
Block 30 minutes on Friday for P3 digest review.
- Review trends
- Identify items that need to become P2 or P1
- Clean up resolved items
- Adjust thresholds based on the week's data

### Rule 5: Take Real Vacations
- For vacations > 3 days: deploy a freeze (no changes = fewer incidents)
- Set up automated responses for P1 (e.g., auto-disable features, maintenance page)
- If possible, arrange a fellow developer or freelancer as emergency backup
- Accept that some P2/P3 issues will wait until you return
```

#### 5.2 Automated Response Patterns

```kotlin
// Example: Auto-disable feature on error threshold via Remote Config
// This reduces the need for manual P1 response

class FeatureCircuitBreaker(
    private val remoteConfig: FirebaseRemoteConfig,
    private val crashlytics: FirebaseCrashlytics
) {
    private val errorCounts = mutableMapOf<String, AtomicInteger>()

    fun recordError(feature: String, error: Throwable) {
        val count = errorCounts.getOrPut(feature) { AtomicInteger(0) }
        val current = count.incrementAndGet()

        crashlytics.recordException(error)

        if (current >= getThreshold(feature)) {
            // Log that circuit breaker tripped
            crashlytics.log("Circuit breaker tripped for: $feature (errors: $current)")
            // Feature will be disabled on next Remote Config fetch
            // This is the ALERT trigger, not the auto-fix
        }
    }

    private fun getThreshold(feature: String): Int {
        return remoteConfig.getLong("circuit_breaker_${feature}_threshold").toInt()
            .coerceAtLeast(10) // Minimum 10 errors before tripping
    }
}
```

#### 5.3 Health Dashboard (Check Instead of Alert)

```markdown
## Solo Dev Health Dashboard

Instead of alerting on everything, create a single dashboard
you check twice daily. Include:

### Top Section: Traffic Light Summary
- GREEN: All systems normal
- YELLOW: Degraded but functional (P2 conditions)
- RED: Outage or critical issue (P1 conditions)

### Metrics to Display:
1. Crash-free rate (last 24h)
2. API error rate (last 1h)
3. Active users (vs same time last week)
4. Firebase billing (today vs daily average)
5. p95 response time (last 1h)
6. Last successful backup (timestamp)

### Tools for Dashboard:
- Firebase Console (built-in dashboard)
- Google Cloud Monitoring (custom dashboards)
- Better Stack / Datadog / Grafana (advanced)
- Simple: A Slack channel with automated metric posts
```

---

## Expected Output

The alerting strategy should produce a complete alerting configuration document:

### Output Format

```markdown
# Alerting Strategy: [Project Name]
**Date:** [Date]
**Developer:** [Name]
**Monitoring Tools:** [list]

## Alert Inventory
### P1 Alerts ([N] alerts)
| Alert | Condition | Threshold | Channel | Runbook |
|-------|-----------|-----------|---------|---------|
[All P1 alerts defined]

### P2 Alerts ([N] alerts)
| Alert | Condition | Threshold | Channel | Review Window |
|-------|-----------|-----------|---------|---------------|
[All P2 alerts defined]

### P3 Metrics (Weekly Digest)
| Metric | Trend Threshold | Current Value | Status |
|--------|----------------|---------------|--------|
[All P3 metrics defined]

## Channel Routing Configuration
[Channel assignment matrix with configuration details]

## Threshold Calculations
[Baseline data and threshold derivation for each alert]

## Fatigue Prevention Settings
[Alert budget, noise reduction, quarterly review schedule]

## On-Call Schedule
[Working hours, review windows, off-times, vacation protocol]

## Dashboard Configuration
[Health dashboard layout and metrics]
```

---

## Customization Guide

- **For apps with revenue > $1K/month:** Add revenue-per-minute calculation to P1 criteria. Alert if estimated revenue loss exceeds $X based on error rate + active users.
- **For apps using Firebase only:** Simplify by using Firebase Crashlytics alerts for crash rate, Google Cloud Budget alerts for cost, and a single uptime monitor for availability. Three tools, not ten.
- **For apps with background sync / WorkManager:** Add "sync success rate" as a P2 metric. Background failures are invisible to users but indicate data staleness.
- **For apps in regulated industries (health, finance):** Add compliance-specific P1 alerts: audit log failures, encryption status, access pattern anomalies. These may be legally required.
- **For developers managing multiple apps:** Create a unified dashboard across all apps, but keep alert routing per-app. A P1 in your flagship app is not the same as a P1 in a hobby project.
- **For developers with a virtual assistant or freelancer backup:** Add an escalation step that notifies the backup person if you do not acknowledge a P1 within 15 minutes.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defines the 3-tier system as the core deliverable with specific alert budgets and channel routing.
- **ST-02 (Structured Sequential Instructions):** Five phases build from tier definitions through thresholds, routing, fatigue prevention, and sustainability.
- **RT-02 (Multi-Dimensional Analysis):** Each alert is analyzed across urgency (tier), accuracy (threshold), delivery (channel), and sustainability (fatigue impact).
- **DS-06 (Prioritization Guidance):** The 3-tier system with explicit budgets (0-2 P1/month, 3-7 P2/week) provides clear prioritization boundaries.
- **CM-02 (Constraint Specification):** The single-developer constraint shapes every recommendation -- no delegation, mandatory off-times, automation-first approach.

---

## Related Prompts

- [firebase_incident_response.md](../mobile/android/targeted-reviews/firebase_incident_response.md) - Runbooks triggered by P1 alerts from this system
- [firebase_cost_monitor_setup.md](../mobile/android/targeted-reviews/firebase_cost_monitor_setup.md) - Detailed Firebase cost monitoring that feeds P1 cost alerts
- [firebase_health_check.md](../mobile/android/targeted-reviews/firebase_health_check.md) - Regular health check that surfaces P2/P3 issues
- devops_monitoring_strategy.md - General monitoring strategy for teams (compare for solo adaptation)
