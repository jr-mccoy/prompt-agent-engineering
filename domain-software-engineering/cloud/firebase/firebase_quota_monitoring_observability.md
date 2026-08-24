---
title: "Firebase Quota Monitoring & Observability Analysis"
category: cloud/firebase
description: "Verify that Firebase 429 errors, quota usage, and rate-limit hotspots are instrumented and monitored"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - firebase
  - firestore
  - rtdb
  - monitoring
  - observability
  - quota
  - http-429
  - alerting
updated: "2026-02-28"
related_prompts:
  - domain-software-engineering/cloud/firebase/firebase_rate_limit_retry_backoff.md
  - domain-software-engineering/cloud/firebase/firebase_hot_document_contention.md
  - domain-software-engineering/devops/devops_monitoring_observability.md
---

# Firebase Quota Monitoring & Observability Analysis

**Objective:** Verify that the application properly instruments, logs, and monitors Firebase quota usage, 429 errors, and `RESOURCE_EXHAUSTED` responses so that rate-limiting hotspots can be identified and resolved before they impact users.

**When to Use:** Use when you don't know which Firebase operation is causing rate limiting, when 429 errors appear sporadically, or when reviewing an app's production readiness for Firebase-dependent features.

**Instructions:**

1. **Check error handling and logging for Firebase operations**
   - For each Firebase call site, verify that errors are caught (not swallowed silently).
   - Check whether `RESOURCE_EXHAUSTED`, `unavailable`, and HTTP 429 errors are logged with context:
     - Operation type (read, write, listen, transaction)
     - Collection/document path
     - Timestamp
     - Client identifier or user ID
     - Retry attempt number (if applicable)
   - Flag call sites where errors are caught but not logged, or where only generic "error occurred" messages are logged.

2. **Verify structured logging for rate-limit events**
   - Check whether the app uses structured logging (JSON format with consistent fields) for Firebase errors.
   - Verify that rate-limit errors are distinguishable from other errors in log queries.
   - Check for error categorization that separates:
     - Quota errors (429 / `RESOURCE_EXHAUSTED`)
     - Contention errors (`ABORTED` in transactions)
     - Permission errors (`PERMISSION_DENIED`)
     - Transient errors (`UNAVAILABLE`)

3. **Assess monitoring and alerting**
   - Check for monitoring dashboards that track:
     - Firebase operation count by type (reads, writes, deletes)
     - Error rate by error code (429 rate specifically)
     - Operation latency (p50, p95, p99)
     - Active listener count
     - Concurrent connections (RTDB)
   - Verify alerting thresholds exist for:
     - 429 error rate exceeding baseline
     - Quota usage approaching limits (e.g., 80% threshold)
     - Latency spikes
   - Check Firebase console alerting configuration.

4. **Evaluate client-side vs server-side visibility**
   - Determine whether rate-limit errors from client SDKs are reported to a central system (e.g., Sentry, Crashlytics, custom analytics).
   - Check whether Cloud Functions log Firebase errors with sufficient context.
   - Assess whether there's a way to correlate client-side 429 errors with server-side metrics.

5. **Check quota awareness in the codebase**
   - Look for code or configuration that references Firebase's documented limits:
     - Firestore: 10,000 writes/sec per database, 1 write/sec/doc, 1 million concurrent connections
     - RTDB: 200K concurrent connections (Blaze), 1,000 writes/sec, 100 MB/sec download
   - Check whether there are comments, constants, or configuration referencing these limits.
   - Verify that rate-limiting logic (if any) is calibrated to documented limits.

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT flag apps that use Firebase's built-in console monitoring as "having no monitoring" — but note if it's the only monitoring.
- ❌ Do NOT require enterprise-grade observability for small/early-stage apps.
- ❌ Do NOT flag logging in development/debug mode as production monitoring.
- ❌ Do NOT flag Firebase client SDK internal error handling as "silent error swallowing."
- ✅ DO check whether monitoring actually covers the specific error codes (429, RESOURCE_EXHAUSTED).
- ✅ DO verify that alerts have reasonable thresholds (not so sensitive they alert constantly, not so loose they miss real issues).
- ✅ DO distinguish between "has logging" and "has actionable monitoring" — logging without dashboards or alerts has limited value.

**Expected Output:** A monitoring gap analysis with:

- Current monitoring coverage (what's instrumented vs what's not)
- Specific gaps that prevent identifying rate-limit sources
- Recommended instrumentation with code examples
- Dashboard and alerting recommendations

**Example Output:**

```markdown
## Firebase Quota Monitoring & Observability Report

### Executive Summary
The application catches Firebase errors in **28 of 47 call sites** (60%), but only **4 call sites** (9%) log errors with sufficient context to identify rate-limit hotspots. No dedicated monitoring dashboard or alerting exists for Firebase quota metrics. When 429 errors occur, the team cannot determine which operation or document path is the cause.

### Monitoring Coverage Matrix

| Area | Instrumented | Logged w/Context | Dashboarded | Alerted |
|------|-------------|-----------------|-------------|---------|
| Firestore reads | Partial | ❌ | ❌ | ❌ |
| Firestore writes | Partial | ❌ | ❌ | ❌ |
| Firestore listeners | ❌ | ❌ | ❌ | ❌ |
| RTDB operations | ❌ | ❌ | ❌ | ❌ |
| Cloud Functions | ✅ | Partial | ❌ | ❌ |
| 429 / RESOURCE_EXHAUSTED | ❌ | ❌ | ❌ | ❌ |

### Critical Gaps

#### 1. Firebase Errors Caught But Not Logged with Context
**Location:** Multiple files (see table below)
**Issue:** Errors are caught with generic `catch(err)` blocks that log `"Firebase error"` without operation metadata.

**Current Pattern:**
```typescript
try {
  await updateDoc(doc(db, 'users', userId), data);
} catch (err) {
  console.error('Firebase error:', err); // No operation context
}
```

**Fix — Structured error logging with Firebase context:**
```typescript
import { FirestoreError } from 'firebase/firestore';

async function safeFirestoreOp<T>(
  operation: () => Promise<T>,
  context: { op: string; path: string; userId?: string }
): Promise<T> {
  try {
    return await operation();
  } catch (err) {
    const isQuotaError = err instanceof FirestoreError &&
      (err.code === 'resource-exhausted' || err.code === 'unavailable');

    // Structured log with full context
    logger.error({
      message: 'Firebase operation failed',
      errorCode: err instanceof FirestoreError ? err.code : 'unknown',
      isQuotaError,
      operation: context.op,
      documentPath: context.path,
      userId: context.userId,
      timestamp: new Date().toISOString(),
      retryable: isQuotaError,
    });

    // Report to monitoring service
    if (isQuotaError) {
      metrics.increment('firebase.quota_error', {
        operation: context.op,
        path: context.path,
      });
    }

    throw err;
  }
}

// Usage
await safeFirestoreOp(
  () => updateDoc(doc(db, 'users', userId), data),
  { op: 'updateDoc', path: `users/${userId}`, userId }
);
```

#### 2. No Dashboard or Alerting for Quota Metrics
**Issue:** The Firebase console shows aggregate metrics but there's no custom dashboard correlating 429 errors with specific operations or code paths.

**Recommendation — Cloud Monitoring dashboard:**
```yaml
# Alerting policy for Firebase quota errors
alertPolicies:
  - displayName: "Firebase 429 Error Rate"
    conditions:
      - conditionThreshold:
          filter: 'metric.type="logging.googleapis.com/user/firebase_quota_error"'
          comparison: COMPARISON_GT
          thresholdValue: 10
          duration: "300s"  # 5 minutes
          aggregations:
            - alignmentPeriod: "60s"
              perSeriesAligner: ALIGN_RATE
    notificationChannels:
      - projects/my-project/notificationChannels/slack-channel

  - displayName: "Firebase Operation Latency P99"
    conditions:
      - conditionThreshold:
          filter: 'metric.type="logging.googleapis.com/user/firebase_operation_latency"'
          comparison: COMPARISON_GT
          thresholdValue: 5000  # 5 seconds
          duration: "300s"
```

#### 3. Client-Side 429 Errors Not Reported Centrally
**Issue:** Client SDK 429 errors are logged to `console.error` but not reported to Crashlytics or a central error tracking service.

**Fix — Report to Crashlytics:**
```typescript
import { recordError } from 'firebase/crashlytics';

// In the error handler
if (isQuotaError) {
  recordError(err, {
    customKeys: {
      operation: context.op,
      path: context.path,
    },
  });
}
```

### Call Sites Without Error Handling

| File | Line | Operation | Error Handling |
|------|------|-----------|----------------|
| UserService.ts | 34 | updateDoc | Generic catch, no context |
| ChatService.ts | 67 | onSnapshot | No error callback |
| Analytics.ts | 12 | addDoc | No try/catch |
| SyncService.ts | 89 | setDoc | Silent catch (empty block) |

### Recommended Monitoring Stack

1. **Structured Logging:** Add Firebase operation wrapper with context (immediate)
2. **Error Tracking:** Report 429s to Crashlytics / Sentry (immediate)
3. **Custom Metrics:** Emit quota error counts and latency to Cloud Monitoring (this sprint)
4. **Dashboard:** Create Firebase operations dashboard with error rate panels (this sprint)
5. **Alerting:** Set up 429 rate and latency alerts (this sprint)
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — Focused on monitoring and observability gaps
- ST-02 (Structured Sequential Instructions) — Systematic coverage audit
- RT-02 (Multi-Dimensional Analysis) — Covers logging, dashboards, alerting, client/server
- RT-05 (Evidence-Based Reasoning) — Requires coverage percentages and specific gaps
- DS-06 (Prioritization Guidance) — Ranked by impact on debugging ability
