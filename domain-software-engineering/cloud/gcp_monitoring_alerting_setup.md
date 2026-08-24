---
title: "GCP Cloud Monitoring and Alerting Setup for Firebase/Android Backend"
category: cloud-infrastructure
description: "Set up comprehensive Cloud Monitoring for a Firebase and Android backend, covering uptime checks for Cloud Functions HTTP endpoints, latency and error rate alerting, custom dashboards, notification channels for Slack/Discord/email, alert policies, and practical on-call strategy for solo developers."
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
  - monitoring
  - alerting
  - cloud-monitoring
  - firebase
  - cloud-functions
  - uptime-checks
  - dashboards
  - slack
  - discord
  - solo-developer
  - android
updated: "2026-02-11"
---

# GCP Cloud Monitoring and Alerting Setup for Firebase/Android Backend

**Objective:** Build a complete monitoring and alerting system for your Firebase and Android backend so you know when things break before your users tell you. This guide covers uptime checks for HTTP endpoints, latency monitoring for Cloud Functions and Cloud Run, error rate alerting, custom dashboards that show you what matters, notification routing to Slack, Discord, or email, and a practical on-call strategy designed for a solo developer who cannot afford to watch dashboards all day.

**When to Use:** Use this prompt when you have deployed Cloud Functions, Cloud Run services, or any HTTP endpoints that real users depend on. Also use it when you have experienced an outage that you discovered only because a user complained, when your app is approaching launch and you need confidence that you will catch problems quickly, or when you want to sleep at night knowing that if something breaks at 3 AM, your phone will buzz instead of your users churning silently. Monitoring is the difference between "we had a 5-minute incident" and "we lost users for 3 days because we didn't notice."

---

## Context Gathering

Before setting up monitoring, gather the following:

1. **Service Inventory**
   - What Cloud Functions do you have? (List names and trigger types: HTTP, Firestore, Pub/Sub, scheduled)
   - Do you have Cloud Run services? (List names and URLs)
   - Do you have any other HTTP endpoints? (App Engine, external APIs you depend on)
   - What Firebase services are critical? (Firestore, Auth, Cloud Storage, FCM)

2. **Reliability Requirements**
   - What is your acceptable downtime? (99% = ~7 hours/month, 99.9% = ~43 min/month)
   - What response times do your users expect? (Under 500ms, under 2s, etc.)
   - What error rate is acceptable? (Under 0.1%, under 1%, under 5%)
   - Which endpoints are user-facing vs background/internal?

3. **Notification Preferences**
   - Where do you want alerts? (Email, Slack, Discord, SMS, PagerDuty)
   - What hours are you available? (24/7, business hours only)
   - How quickly do you need to respond? (Minutes for critical, hours for warning)
   - Do you have separate channels for critical vs informational alerts?

4. **Current Monitoring State**
   - Have you set up any monitoring already?
   - Are you using Firebase Performance Monitoring in your Android app?
   - Do you check Cloud Functions logs manually?
   - Have you experienced outages you missed?

---

## Instructions

### CRITICAL: Verification Requirements

Before configuring monitoring, verify these requirements:

1. **Cloud Monitoring API is enabled** (`monitoring.googleapis.com`) in your GCP project
2. **Your service account has the Monitoring Editor role** (`roles/monitoring.editor`) for creating alert policies and dashboards
3. **At least one notification channel is verified** and tested (send a test notification before relying on it for real alerts)
4. **Your Cloud Functions and Cloud Run services are deployed and running** (you cannot create uptime checks for endpoints that do not exist)
5. **You understand the billing implications** -- Cloud Monitoring is free for GCP metrics but custom metrics, synthetic monitors, and log-based metrics above free tier quotas cost extra
6. **Acceptable null result:** If you just deployed a service and create an uptime check, it may show as "failing" for the first 1-2 check cycles while the monitoring system initializes. Wait 5 minutes before debugging.

### False-Positive Prevention

- **DO NOT** set alert thresholds so tight that normal traffic variation triggers alerts. A 200ms latency threshold on a Cloud Function that normally varies between 100ms and 300ms will generate constant noise.
- **DO NOT** alert on single data point violations. Use conditions like "violates for 5 minutes" or "3 of 5 checks fail" to filter out transient spikes.
- **DO NOT** create uptime checks that hit endpoints with side effects (writes, emails, payments). Use dedicated health check endpoints or GET-only endpoints.
- **DO NOT** send all alerts to SMS. SMS fatigue from non-critical alerts will make you ignore the critical ones.
- **DO NOT** monitor everything at the same priority level. A failing payment endpoint is not the same severity as a slow analytics query.
- **DO** test your notification channels with actual test alerts before trusting them.
- **DO** create a dedicated health check endpoint (`/health` or `/_health`) for uptime monitoring that does not require authentication.
- **DO** set up graduated alert severity (warning vs critical) with different notification channels.
- **DO** include "alert fatigue" review in your monthly maintenance -- if you are ignoring alerts, they need to be tuned or removed.

---

### Phase 1: Monitoring Foundation

#### Step 1: Enable Required APIs

```bash
export PROJECT_ID="your-project-id"

# Enable Cloud Monitoring API
gcloud services enable monitoring.googleapis.com \
  --project=$PROJECT_ID

# Enable Cloud Logging API (for log-based metrics)
gcloud services enable logging.googleapis.com \
  --project=$PROJECT_ID

# Enable Cloud Error Reporting (auto-groups errors)
gcloud services enable clouderrorreporting.googleapis.com \
  --project=$PROJECT_ID

# Verify all are enabled
gcloud services list --enabled --project=$PROJECT_ID \
  --filter="name:(monitoring OR logging OR clouderrorreporting)"
```

#### Step 2: Create Health Check Endpoints

Before setting up uptime checks, make sure your services have endpoints specifically designed for health monitoring.

```typescript
// For Cloud Functions v2 (HTTP trigger)
// functions/src/health.ts
import { onRequest } from 'firebase-functions/v2/https';
import { getFirestore } from 'firebase-admin/firestore';

const db = getFirestore();

/**
 * Health check endpoint for monitoring.
 * Tests:
 * 1. Function is running (if you can read this, it works)
 * 2. Firestore connectivity (optional but recommended)
 * 3. Response time (measured by the uptime check)
 */
export const health = onRequest(
  {
    region: 'us-central1',
    memory: '128MiB',
    timeoutSeconds: 10,
    // Allow unauthenticated access for uptime checks
    invoker: 'public',
  },
  async (req, res) => {
    const checks: Record<string, string> = {
      function: 'ok',
      timestamp: new Date().toISOString(),
    };

    try {
      // Quick Firestore connectivity check
      const startMs = Date.now();
      await db.collection('_health').doc('ping').get();
      checks.firestore = `ok (${Date.now() - startMs}ms)`;
    } catch (error) {
      checks.firestore = 'error';
      // Return 503 if Firestore is down -- this triggers an uptime alert
      res.status(503).json({
        status: 'degraded',
        checks,
        error: 'Firestore connectivity failed',
      });
      return;
    }

    res.status(200).json({
      status: 'healthy',
      checks,
    });
  }
);
```

```typescript
// For Cloud Run backend
// src/routes/health.ts
import { Router } from 'express';
import { getFirestore } from 'firebase-admin/firestore';

const router = Router();
const db = getFirestore();

router.get('/health', async (req, res) => {
  const checks: Record<string, string> = {
    server: 'ok',
    uptime: `${process.uptime().toFixed(0)}s`,
    timestamp: new Date().toISOString(),
  };

  try {
    const startMs = Date.now();
    await db.collection('_health').doc('ping').get();
    checks.firestore = `ok (${Date.now() - startMs}ms)`;
  } catch {
    checks.firestore = 'error';
    res.status(503).json({ status: 'degraded', checks });
    return;
  }

  res.status(200).json({ status: 'healthy', checks });
});

export default router;
```

#### Step 3: Understand GCP Monitoring Metrics

Key built-in metrics you get for free:

| Service | Metric | What It Tells You |
|---------|--------|-------------------|
| Cloud Functions | `cloudfunctions.googleapis.com/function/execution_count` | How many times the function ran |
| Cloud Functions | `cloudfunctions.googleapis.com/function/execution_times` | How long each execution took (latency) |
| Cloud Functions | `cloudfunctions.googleapis.com/function/user_memory_bytes` | Memory usage per invocation |
| Cloud Functions | `cloudfunctions.googleapis.com/function/active_instances` | Current number of running instances |
| Cloud Run | `run.googleapis.com/request_count` | HTTP requests received |
| Cloud Run | `run.googleapis.com/request_latencies` | Response time distribution |
| Cloud Run | `run.googleapis.com/container/instance_count` | Running container instances |
| Cloud Run | `run.googleapis.com/container/cpu/utilization` | CPU usage percentage |
| Cloud Run | `run.googleapis.com/container/memory/utilization` | Memory usage percentage |
| Firestore | `firestore.googleapis.com/document/read_count` | Document reads |
| Firestore | `firestore.googleapis.com/document/write_count` | Document writes |
| Cloud Storage | `storage.googleapis.com/api/request_count` | API requests to storage |

---

### Phase 2: Uptime Checks

Uptime checks ping your endpoints from multiple global locations and alert you when they fail.

#### Step 1: Create Uptime Checks via gcloud

```bash
# Create an uptime check for your Cloud Function health endpoint
gcloud monitoring uptime create \
  --display-name="Cloud Functions Health Check" \
  --resource-type=uptime-url \
  --hostname="us-central1-$PROJECT_ID.cloudfunctions.net" \
  --path="/health" \
  --protocol=https \
  --period=300 \
  --timeout=10s \
  --checker-type=STATIC_IP_CHECKERS \
  --project=$PROJECT_ID

# Create an uptime check for your Cloud Run service
gcloud monitoring uptime create \
  --display-name="Cloud Run Backend Health Check" \
  --resource-type=uptime-url \
  --hostname="my-backend-xxxxx-uc.a.run.app" \
  --path="/health" \
  --protocol=https \
  --period=300 \
  --timeout=10s \
  --checker-type=STATIC_IP_CHECKERS \
  --project=$PROJECT_ID

# List your uptime checks
gcloud monitoring uptime list-configs --project=$PROJECT_ID
```

#### Step 2: Create Uptime Checks via Console

```
Navigation Path:
GCP Console → Monitoring → Uptime checks → CREATE UPTIME CHECK

Configuration for Cloud Functions:
├── Protocol: HTTPS
├── Resource Type: URL
├── Hostname: us-central1-YOUR_PROJECT.cloudfunctions.net
├── Path: /health
├── Check frequency: 5 minutes (300s)
├── Timeout: 10 seconds
├── Regions: Leave all checked (global monitoring)
├── Response validation:
│   ├── Status code: 200
│   └── Content match (optional): "healthy"
└── Alert & Notification:
    ├── Create alert: YES
    ├── Alert name: "Cloud Functions Down"
    └── Notification channels: [Select your channels]

Configuration for Cloud Run:
├── Protocol: HTTPS
├── Resource Type: URL
├── Hostname: my-backend-xxxxx-uc.a.run.app
├── Path: /health
├── Check frequency: 5 minutes
├── Timeout: 10 seconds
└── (Same alert configuration as above)
```

#### Step 3: Uptime Check Recommendations for Solo Developers

| Endpoint | Check Frequency | Timeout | Alert After | Priority |
|----------|----------------|---------|-------------|----------|
| Main API health | 5 min | 10s | 2 failures | CRITICAL |
| Payment webhook | 5 min | 10s | 1 failure | CRITICAL |
| Cloud Run backend | 5 min | 10s | 2 failures | CRITICAL |
| Admin dashboard | 15 min | 30s | 3 failures | WARNING |
| Analytics endpoint | 15 min | 30s | 3 failures | LOW |

**Cost note:** Uptime checks are free for up to 100 checks. Each check from each region counts separately. A single endpoint checked every 5 minutes from 6 regions = 6 checks. With the recommended setup above (5 endpoints), you use ~30 of your 100 free checks.

---

### Phase 3: Alert Policies

Alert policies define conditions that trigger notifications. This is where you turn raw metrics into actionable alerts.

#### Alert Policy 1: Cloud Function Error Rate

```bash
# Create an alert policy for Cloud Function errors using gcloud
# Alert when error rate exceeds 5% for 5 minutes

gcloud monitoring policies create \
  --display-name="Cloud Functions High Error Rate" \
  --condition-display-name="Error rate > 5% for 5 min" \
  --condition-filter='
    resource.type = "cloud_function" AND
    metric.type = "cloudfunctions.googleapis.com/function/execution_count" AND
    metric.labels.status != "ok"
  ' \
  --condition-threshold-value=0.05 \
  --condition-threshold-comparison=COMPARISON_GT \
  --condition-threshold-duration=300s \
  --condition-threshold-aggregation-alignment-period=60s \
  --condition-threshold-aggregation-per-series-aligner=ALIGN_RATE \
  --notification-channels="projects/$PROJECT_ID/notificationChannels/YOUR_CHANNEL_ID" \
  --documentation="Cloud Functions error rate exceeded 5%. Check Cloud Logging for error details: https://console.cloud.google.com/logs?project=$PROJECT_ID" \
  --severity=CRITICAL \
  --project=$PROJECT_ID
```

#### Alert Policy 2: Cloud Function Latency

```json
// alert-policy-latency.json
// Create via: gcloud monitoring policies create --policy-from-file=alert-policy-latency.json
{
  "displayName": "Cloud Functions High Latency",
  "documentation": {
    "content": "Cloud Functions p95 latency exceeded 5 seconds for 10 minutes. This likely indicates cold starts, downstream service issues, or resource exhaustion. Check:\n1. Cloud Functions logs for slow operations\n2. Firestore latency if functions read/write Firestore\n3. External API response times\n4. Function memory settings (low memory = throttled CPU)",
    "mimeType": "text/markdown"
  },
  "conditions": [
    {
      "displayName": "p95 latency > 5s for 10 min",
      "conditionThreshold": {
        "filter": "resource.type = \"cloud_function\" AND metric.type = \"cloudfunctions.googleapis.com/function/execution_times\"",
        "aggregations": [
          {
            "alignmentPeriod": "300s",
            "perSeriesAligner": "ALIGN_PERCENTILE_95",
            "crossSeriesReducer": "REDUCE_MAX",
            "groupByFields": ["resource.label.function_name"]
          }
        ],
        "comparison": "COMPARISON_GT",
        "thresholdValue": 5000000000,
        "duration": "600s",
        "trigger": {
          "count": 1
        }
      }
    }
  ],
  "alertStrategy": {
    "autoClose": "1800s",
    "notificationRateLimit": {
      "period": "3600s"
    }
  },
  "combiner": "OR",
  "enabled": true,
  "severity": "WARNING"
}
```

```bash
# Create the latency alert policy from JSON file
gcloud monitoring policies create \
  --policy-from-file=alert-policy-latency.json \
  --project=$PROJECT_ID
```

#### Alert Policy 3: Cloud Run Container Crash Loop

```json
// alert-policy-crash-loop.json
{
  "displayName": "Cloud Run Container Crash Loop",
  "documentation": {
    "content": "Cloud Run container instance count is fluctuating rapidly, indicating containers are crashing and restarting. Check:\n1. Cloud Run logs for crash/exit reasons\n2. Application startup errors\n3. Memory limits (OOMKilled)\n4. Health check endpoint timeout",
    "mimeType": "text/markdown"
  },
  "conditions": [
    {
      "displayName": "Container restarts > 5 in 10 min",
      "conditionThreshold": {
        "filter": "resource.type = \"cloud_run_revision\" AND metric.type = \"run.googleapis.com/container/startup_latencies\"",
        "aggregations": [
          {
            "alignmentPeriod": "600s",
            "perSeriesAligner": "ALIGN_COUNT",
            "crossSeriesReducer": "REDUCE_SUM",
            "groupByFields": ["resource.label.service_name"]
          }
        ],
        "comparison": "COMPARISON_GT",
        "thresholdValue": 5,
        "duration": "0s"
      }
    }
  ],
  "combiner": "OR",
  "enabled": true,
  "severity": "CRITICAL"
}
```

#### Alert Policy 4: Firestore High Read Rate (Cost Protection)

```json
// alert-policy-firestore-reads.json
{
  "displayName": "Firestore Read Rate Spike",
  "documentation": {
    "content": "Firestore document reads spiked above normal levels. This could indicate:\n1. A runaway listener or query in the app\n2. Sudden traffic increase\n3. Missing pagination on a collection read\n4. Bot or scraper traffic\n\nCheck Firebase Console > Firestore > Usage tab for details.",
    "mimeType": "text/markdown"
  },
  "conditions": [
    {
      "displayName": "Firestore reads > 10K/min for 10 min",
      "conditionThreshold": {
        "filter": "resource.type = \"firestore_database\" AND metric.type = \"firestore.googleapis.com/document/read_count\"",
        "aggregations": [
          {
            "alignmentPeriod": "60s",
            "perSeriesAligner": "ALIGN_RATE"
          }
        ],
        "comparison": "COMPARISON_GT",
        "thresholdValue": 166.67,
        "duration": "600s"
      }
    }
  ],
  "combiner": "OR",
  "enabled": true,
  "severity": "WARNING"
}
```

#### Alert Policy 5: Log-Based Alert for Application Errors

```bash
# Create a log-based metric for application errors
gcloud logging metrics create app-error-count \
  --description="Count of ERROR and CRITICAL log entries from Cloud Functions" \
  --log-filter='
    resource.type="cloud_function"
    severity>="ERROR"
    NOT textPayload:"HealthCheck"
  ' \
  --project=$PROJECT_ID

# Create an alert policy based on the log metric
gcloud monitoring policies create \
  --display-name="Application Error Spike" \
  --condition-display-name="Error log count > 10 in 5 min" \
  --condition-filter='
    resource.type = "cloud_function" AND
    metric.type = "logging.googleapis.com/user/app-error-count"
  ' \
  --condition-threshold-value=10 \
  --condition-threshold-comparison=COMPARISON_GT \
  --condition-threshold-duration=300s \
  --condition-threshold-aggregation-alignment-period=300s \
  --condition-threshold-aggregation-per-series-aligner=ALIGN_SUM \
  --notification-channels="projects/$PROJECT_ID/notificationChannels/YOUR_CHANNEL_ID" \
  --severity=CRITICAL \
  --project=$PROJECT_ID
```

#### Recommended Alert Configuration for Solo Developers

| Alert | Condition | Duration | Severity | Notification |
|-------|-----------|----------|----------|-------------|
| Endpoint down | Uptime check fails | 2 checks (10 min) | CRITICAL | Slack + Email + SMS |
| High error rate | > 5% errors | 5 minutes | CRITICAL | Slack + Email |
| High latency | p95 > 5s | 10 minutes | WARNING | Slack only |
| Container crash | > 5 restarts in 10min | Immediate | CRITICAL | Slack + Email + SMS |
| Firestore read spike | > 10K reads/min | 10 minutes | WARNING | Slack only |
| Error log spike | > 10 errors in 5 min | 5 minutes | CRITICAL | Slack + Email |
| Budget alert | 80% of monthly budget | N/A | WARNING | Email |
| Budget critical | 100% of monthly budget | N/A | CRITICAL | Slack + Email + SMS |

---

### Phase 4: Custom Dashboards

Build dashboards that give you a single-pane view of your system health.

#### Dashboard 1: Solo Developer Overview Dashboard

```bash
# Create a monitoring dashboard via gcloud
# Save this JSON to a file and import it

cat > solo-dev-dashboard.json << 'DASHBOARD_EOF'
{
  "displayName": "Solo Dev System Overview",
  "mosaicLayout": {
    "columns": 12,
    "tiles": [
      {
        "xPos": 0, "yPos": 0, "width": 4, "height": 4,
        "widget": {
          "title": "Cloud Functions Invocations (24h)",
          "xyChart": {
            "dataSets": [{
              "timeSeriesQuery": {
                "timeSeriesFilter": {
                  "filter": "resource.type = \"cloud_function\" AND metric.type = \"cloudfunctions.googleapis.com/function/execution_count\"",
                  "aggregation": {
                    "alignmentPeriod": "3600s",
                    "perSeriesAligner": "ALIGN_SUM",
                    "groupByFields": ["resource.label.function_name"]
                  }
                }
              },
              "plotType": "STACKED_BAR"
            }],
            "timeshiftDuration": "0s"
          }
        }
      },
      {
        "xPos": 4, "yPos": 0, "width": 4, "height": 4,
        "widget": {
          "title": "Cloud Functions Latency p50/p95 (24h)",
          "xyChart": {
            "dataSets": [
              {
                "timeSeriesQuery": {
                  "timeSeriesFilter": {
                    "filter": "resource.type = \"cloud_function\" AND metric.type = \"cloudfunctions.googleapis.com/function/execution_times\"",
                    "aggregation": {
                      "alignmentPeriod": "300s",
                      "perSeriesAligner": "ALIGN_PERCENTILE_50"
                    }
                  }
                },
                "plotType": "LINE",
                "legendTemplate": "p50"
              },
              {
                "timeSeriesQuery": {
                  "timeSeriesFilter": {
                    "filter": "resource.type = \"cloud_function\" AND metric.type = \"cloudfunctions.googleapis.com/function/execution_times\"",
                    "aggregation": {
                      "alignmentPeriod": "300s",
                      "perSeriesAligner": "ALIGN_PERCENTILE_95"
                    }
                  }
                },
                "plotType": "LINE",
                "legendTemplate": "p95"
              }
            ]
          }
        }
      },
      {
        "xPos": 8, "yPos": 0, "width": 4, "height": 4,
        "widget": {
          "title": "Cloud Functions Error Rate (24h)",
          "xyChart": {
            "dataSets": [{
              "timeSeriesQuery": {
                "timeSeriesFilter": {
                  "filter": "resource.type = \"cloud_function\" AND metric.type = \"cloudfunctions.googleapis.com/function/execution_count\" AND metric.labels.status != \"ok\"",
                  "aggregation": {
                    "alignmentPeriod": "300s",
                    "perSeriesAligner": "ALIGN_RATE"
                  }
                }
              },
              "plotType": "LINE"
            }]
          }
        }
      },
      {
        "xPos": 0, "yPos": 4, "width": 6, "height": 4,
        "widget": {
          "title": "Firestore Read/Write Operations (24h)",
          "xyChart": {
            "dataSets": [
              {
                "timeSeriesQuery": {
                  "timeSeriesFilter": {
                    "filter": "resource.type = \"firestore_database\" AND metric.type = \"firestore.googleapis.com/document/read_count\"",
                    "aggregation": {
                      "alignmentPeriod": "300s",
                      "perSeriesAligner": "ALIGN_RATE"
                    }
                  }
                },
                "plotType": "LINE",
                "legendTemplate": "Reads/s"
              },
              {
                "timeSeriesQuery": {
                  "timeSeriesFilter": {
                    "filter": "resource.type = \"firestore_database\" AND metric.type = \"firestore.googleapis.com/document/write_count\"",
                    "aggregation": {
                      "alignmentPeriod": "300s",
                      "perSeriesAligner": "ALIGN_RATE"
                    }
                  }
                },
                "plotType": "LINE",
                "legendTemplate": "Writes/s"
              }
            ]
          }
        }
      },
      {
        "xPos": 6, "yPos": 4, "width": 6, "height": 4,
        "widget": {
          "title": "Uptime Check Status",
          "xyChart": {
            "dataSets": [{
              "timeSeriesQuery": {
                "timeSeriesFilter": {
                  "filter": "resource.type = \"uptime_url\" AND metric.type = \"monitoring.googleapis.com/uptime_check/check_passed\"",
                  "aggregation": {
                    "alignmentPeriod": "300s",
                    "perSeriesAligner": "ALIGN_FRACTION_TRUE",
                    "groupByFields": ["metric.label.check_id"]
                  }
                }
              },
              "plotType": "LINE"
            }]
          }
        }
      }
    ]
  }
}
DASHBOARD_EOF

# Create the dashboard
gcloud monitoring dashboards create \
  --config-from-file=solo-dev-dashboard.json \
  --project=$PROJECT_ID
```

#### Dashboard 2: Quick Console Dashboard Setup

For a faster setup, create a dashboard through the Console:

```
Navigation Path:
GCP Console → Monitoring → Dashboards → CREATE DASHBOARD

Recommended Widgets for Solo Developers:

Row 1: Health Overview
├── Uptime Check Uptime (%) — Scorecard widget
├── Cloud Functions Invocations — Line chart, 24h
└── Error Count — Scorecard widget, last 1h

Row 2: Performance
├── Cloud Functions Latency (p50, p95) — Line chart, 24h
├── Cloud Run Request Latency — Line chart, 24h
└── Active Cloud Run Instances — Line chart, 24h

Row 3: Firebase
├── Firestore Read Rate — Line chart, 24h
├── Firestore Write Rate — Line chart, 24h
└── Cloud Storage Request Count — Line chart, 24h

Row 4: Resources
├── Cloud Functions Memory Usage — Line chart, 24h
├── Cloud Run CPU Utilization — Line chart, 24h
└── Cloud Run Memory Utilization — Line chart, 24h
```

---

### Phase 5: Notification Routing

#### Step 1: Set Up Notification Channels

```bash
# Create an email notification channel
gcloud monitoring channels create \
  --display-name="Personal Email" \
  --type=email \
  --channel-labels=email_address=you@example.com \
  --project=$PROJECT_ID

# List your notification channels to get their IDs
gcloud monitoring channels list --project=$PROJECT_ID \
  --format="table(name, displayName, type)"

# Example output:
# NAME                                                      DISPLAY_NAME     TYPE
# projects/my-project/notificationChannels/1234567890123456  Personal Email   email
```

#### Step 2: Set Up Slack Notifications

```bash
# Step 1: Create a Slack app and incoming webhook
# Go to: https://api.slack.com/apps
# Create New App → From scratch → Name it "GCP Alerts"
# Add feature: Incoming Webhooks → Activate → Add New Webhook
# Choose channel: #alerts (or create one)
# Copy the webhook URL

# Step 2: Create the notification channel in GCP
# Note: Slack integration through Monitoring requires the Slack app for Google Cloud
# Navigate: GCP Console → Monitoring → Alerting → Edit notification channels → Slack

# Alternative: Use a Cloud Function to bridge Monitoring → Slack webhook
```

```typescript
// functions/src/slack-alert-bridge.ts
// This Cloud Function receives alert notifications via Pub/Sub
// and forwards them to Slack with formatted messages

import { onMessagePublished } from 'firebase-functions/v2/pubsub';

interface AlertNotification {
  incident: {
    incident_id: string;
    resource_name: string;
    policy_name: string;
    condition_name: string;
    state: string;
    started_at: number;
    ended_at?: number;
    summary: string;
    url: string;
  };
}

export const slackAlertBridge = onMessagePublished(
  {
    topic: 'monitoring-alerts',
    region: 'us-central1',
    memory: '128MiB',
  },
  async (event) => {
    const notification: AlertNotification = event.data.message.json;
    const incident = notification.incident;

    const isResolved = incident.state === 'closed';
    const emoji = isResolved ? ':white_check_mark:' : ':rotating_light:';
    const color = isResolved ? '#36a64f' : '#ff0000';
    const status = isResolved ? 'RESOLVED' : 'FIRING';

    const slackMessage = {
      attachments: [
        {
          color,
          blocks: [
            {
              type: 'header',
              text: {
                type: 'plain_text',
                text: `${emoji} Alert ${status}: ${incident.policy_name}`,
              },
            },
            {
              type: 'section',
              fields: [
                {
                  type: 'mrkdwn',
                  text: `*Condition:*\n${incident.condition_name}`,
                },
                {
                  type: 'mrkdwn',
                  text: `*Resource:*\n${incident.resource_name}`,
                },
                {
                  type: 'mrkdwn',
                  text: `*Started:*\n<!date^${incident.started_at}^{date_short} {time}|${new Date(incident.started_at * 1000).toISOString()}>`,
                },
                {
                  type: 'mrkdwn',
                  text: `*Summary:*\n${incident.summary}`,
                },
              ],
            },
            {
              type: 'actions',
              elements: [
                {
                  type: 'button',
                  text: { type: 'plain_text', text: 'View in Console' },
                  url: incident.url,
                },
              ],
            },
          ],
        },
      ],
    };

    // Forward to Slack
    const slackWebhookUrl = process.env.SLACK_WEBHOOK_URL;
    if (slackWebhookUrl) {
      await fetch(slackWebhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(slackMessage),
      });
    }

    // Forward to Discord (webhook format is slightly different)
    const discordWebhookUrl = process.env.DISCORD_WEBHOOK_URL;
    if (discordWebhookUrl) {
      const discordMessage = {
        embeds: [{
          title: `${status}: ${incident.policy_name}`,
          description: incident.summary,
          color: isResolved ? 0x36a64f : 0xff0000,
          fields: [
            { name: 'Condition', value: incident.condition_name, inline: true },
            { name: 'Resource', value: incident.resource_name, inline: true },
          ],
          url: incident.url,
          timestamp: new Date(incident.started_at * 1000).toISOString(),
        }],
      };

      await fetch(discordWebhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(discordMessage),
      });
    }
  }
);
```

```bash
# Deploy the Slack/Discord bridge function
gcloud functions deploy slackAlertBridge \
  --gen2 \
  --runtime=nodejs20 \
  --trigger-topic=monitoring-alerts \
  --region=us-central1 \
  --memory=128MB \
  --set-env-vars="SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL,DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR/WEBHOOK/URL" \
  --project=$PROJECT_ID

# Create the Pub/Sub topic for alerts
gcloud pubsub topics create monitoring-alerts --project=$PROJECT_ID

# Create a Pub/Sub notification channel
gcloud monitoring channels create \
  --display-name="Pub/Sub → Slack/Discord Bridge" \
  --type=pubsub \
  --channel-labels=topic=projects/$PROJECT_ID/topics/monitoring-alerts \
  --project=$PROJECT_ID
```

#### Step 3: Notification Routing Strategy

```
Alert Severity → Notification Channel Routing:
│
├── CRITICAL (service is down, data loss risk, payment failures)
│   ├── Slack #alerts-critical
│   ├── Email (immediate)
│   ├── SMS (via Cloud Monitoring or PagerDuty)
│   └── Phone call (PagerDuty escalation, if configured)
│
├── WARNING (degraded performance, approaching limits)
│   ├── Slack #alerts-warning
│   └── Email (batched, daily digest)
│
├── INFORMATIONAL (scaling events, deployments, cost alerts)
│   └── Slack #alerts-info
│
└── RESOLVED (incident is over)
    ├── Same channel as the original alert
    └── Auto-closes after 30 minutes of resolution
```

---

### Solo Developer On-Call Strategy

As a solo developer, you cannot have a traditional on-call rotation. Here is a practical approach:

#### On-Call Philosophy for One Person

```
Solo Developer On-Call Rules:
│
├── Rule 1: Not everything is a 3 AM problem
│   ├── CRITICAL at 3 AM: Service is completely down → Wake up
│   ├── WARNING at 3 AM: Elevated errors → Check in the morning
│   └── INFO at 3 AM: Cost alert → Check in the morning
│
├── Rule 2: Automate recovery before alerting
│   ├── Cloud Run auto-restarts crashed containers
│   ├── Cloud Functions retry on failure (configure retry policy)
│   ├── Use circuit breakers so one failing endpoint does not cascade
│   └── Budget kill switch auto-disables billing at threshold
│
├── Rule 3: Reduce alert fatigue ruthlessly
│   ├── If you ignore an alert 3 times, tune or delete it
│   ├── Aggregate similar alerts (10 errors, not 10 separate alerts)
│   ├── Silence alerts during known maintenance windows
│   └── Review alert value monthly: "Did this alert lead to action?"
│
├── Rule 4: Set quiet hours with override
│   ├── 10 PM - 8 AM: Only CRITICAL alerts reach phone
│   ├── 8 AM - 10 PM: All alerts via Slack
│   └── Use phone DND with override for the alerting number
│
└── Rule 5: Document your runbooks
    ├── Each alert should link to a resolution guide
    ├── "If this alert fires, do X" in the alert documentation
    └── Future you at 3 AM will thank present you
```

#### Phone DND Configuration Tip

```
iPhone: Settings → Focus → Do Not Disturb
├── Allow calls from: Specific contacts
├── Add your alerting email/number to contacts
└── Enable "Repeated Calls" so 2 calls in 3 min break through

Android: Settings → Do Not Disturb
├── Exceptions → Calls → From starred contacts only
├── Star your alerting contact
└── Enable "Repeat callers" exception
```

#### Weekly Monitoring Review Checklist

```markdown
## Weekly Monitoring Review (15 minutes)

### Quick Checks
- [ ] Open Monitoring Dashboard → any anomalies this week?
- [ ] Check uptime percentage → target 99.9% (less than 10 min downtime)
- [ ] Review fired alerts → any false positives to tune?
- [ ] Check error rate trend → increasing, stable, or decreasing?

### Alert Health
- [ ] How many alerts fired this week?
- [ ] How many required action vs were noise?
- [ ] Any alerts that should be added based on this week's incidents?
- [ ] Any alerts that should be removed or tuned?

### Performance
- [ ] p95 latency trend → getting slower, faster, or stable?
- [ ] Cold start frequency → acceptable or need min-instances?
- [ ] Firestore read/write patterns → any unexpected spikes?
```

---

## Expected Output

After following this guide, your monitoring system should look like this:

```markdown
## Cloud Monitoring Setup Summary

### Uptime Checks
| Endpoint | URL | Frequency | Status | Uptime (30d) |
|----------|-----|-----------|--------|-------------|
| CF Health | /health (Cloud Functions) | 5 min | Passing | 99.95% |
| CR Backend | /health (Cloud Run) | 5 min | Passing | 99.98% |
| Payment Webhook | /webhook/stripe | 5 min | Passing | 100% |

### Alert Policies
| Alert | Condition | Severity | Fires Via | Last Fired |
|-------|-----------|----------|-----------|------------|
| Endpoint Down | Uptime fails 2x | CRITICAL | Slack + Email + SMS | Never |
| High Error Rate | > 5% for 5 min | CRITICAL | Slack + Email | Feb 8 (resolved) |
| High Latency | p95 > 5s for 10 min | WARNING | Slack | Feb 5 (resolved) |
| Firestore Spike | > 10K reads/min | WARNING | Slack | Never |
| Error Log Spike | > 10 errors/5 min | CRITICAL | Slack + Email | Feb 8 (resolved) |
| Budget 80% | Monthly budget 80% | WARNING | Email | Never |

### Notification Channels
| Channel | Type | Used For | Verified |
|---------|------|----------|----------|
| Personal Email | email | All severities | Yes |
| #alerts-critical | Slack (via bridge) | CRITICAL only | Yes |
| #alerts-warning | Slack (via bridge) | WARNING + INFO | Yes |
| Discord #alerts | Discord (via bridge) | All severities | Yes |

### Dashboard
| Dashboard | Widgets | Refresh | URL |
|-----------|---------|---------|-----|
| Solo Dev Overview | 8 widgets | Auto (1 min) | [Console Link] |

### Weekly Stats
| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| Uptime | 99.97% | 99.95% | Stable |
| Alerts fired | 2 | 5 | Improving |
| False positive alerts | 0 | 2 | Improving |
| p95 latency (CF) | 1.2s | 1.4s | Improving |
| p95 latency (CR) | 340ms | 380ms | Improving |
| Firestore reads/day | 8,200 | 7,500 | Normal growth |
```

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defined the monitoring goal as catching problems before users report them
- **ST-02 (Sequential Step-by-Step Instructions):** Phased approach from foundation through uptime checks, alerts, dashboards, and notification routing
- **RT-02 (Multi-Dimensional Analysis):** Covered monitoring across Cloud Functions, Cloud Run, Firestore, and application-level metrics
- **CM-01 (Contextual Framing):** All examples and thresholds calibrated for solo developer with Firebase/Android backend
- **DS-06 (Prioritization and Severity Guidance):** Clear severity classification (CRITICAL/WARNING/INFO) with different notification routing per level
- **DS-02 (Metric Specification):** Concrete threshold values for latency, error rates, and read counts
- **RT-05 (Evidence-Based Reasoning):** Alert thresholds based on typical Cloud Functions and Cloud Run performance characteristics

---

## Related Prompts

- `gcp_solo_dev_cost_management.md` -- Budget alerts complement operational monitoring
- `gcp_cloud_run_backend.md` -- The Cloud Run services you are monitoring
- `gcp_secret_manager_setup.md` -- Monitoring secret access patterns for security
- `gcp_bigquery_analytics_pipeline.md` -- Analytics pipeline health monitoring
- `cloud_gcp_best_practices.md` -- Broader GCP best practices including observability

---

## Customization Guide

- **For pre-launch projects with minimal traffic:** Skip the custom dashboard JSON and use the Console-based dashboard setup. Use only 2-3 uptime checks (health endpoint + most critical endpoint). Set wider alert thresholds (10% error rate, 10s latency) to avoid noise from small sample sizes. Skip the Slack bridge and use email-only notifications.
- **For launched products with paying users:** Tighten alert thresholds (1% error rate, 2s latency). Add uptime checks for every user-facing endpoint. Set up the Slack/Discord bridge for fast response. Consider adding a PagerDuty integration for phone call escalation on CRITICAL alerts. Add SLO monitoring (Service Level Objectives) in Cloud Monitoring.
- **For multi-service architectures:** Create separate dashboards per service. Use alert policy grouping to correlate related alerts (e.g., "Cloud Run latency spike + Firestore read spike" likely means Firestore is slow, not Cloud Run). Add cross-service dependency monitoring.
- **For teams growing beyond solo:** Create shared Slack channels for alerts. Set up a rotation using PagerDuty or Opsgenie. Create runbook documents for each alert policy. Add role-based dashboard access so non-engineers can see health status without alert configuration access.
- **For compliance-sensitive applications (healthcare, finance):** Enable audit logging for all monitoring configuration changes. Export alert history to BigQuery for compliance reporting. Add synthetic monitoring (scheduled probes that simulate user flows) in addition to simple uptime checks. Set up monitoring for monitoring itself (a meta-alert if the notification channel becomes unreachable).
