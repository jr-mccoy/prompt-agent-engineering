---
title: "Firebase Health Check"
category: mobile-development
description: "Periodic Firebase project health check — security rules review, cost trend analysis, performance monitoring, SDK version currency, deprecated API usage, and quota utilization"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - android
  - firebase
  - health-check
  - maintenance
  - cost-management
  - security
  - solo-developer
updated: "2026-02-11"
---

# Firebase Health Check

**Objective:** Conduct a periodic health check of a Firebase project — reviewing security rules for drift, analyzing cost trends, checking SDK version currency, identifying deprecated API usage, reviewing performance metrics, auditing quota utilization, and validating monitoring coverage — producing a health report with prioritized action items.

**When to Use:** Run this health check quarterly (recommended) or monthly (if costs are a concern). Also run it after major app updates, after Firebase SDK upgrades, after receiving any Firebase-related alerts, or when preparing for a significant traffic increase. This is preventive maintenance — catching issues before they become incidents saves time and money.

**Important context:** Firebase projects accumulate technical debt just like codebases. Security rules that were fine at launch may have gaps as features grow. Costs that were acceptable at 1,000 users may be alarming at 10,000. SDK versions fall behind. Monitoring gaps appear. This health check catches these slowly-building problems before they become crises.

---

## Context Gathering

Before starting the health check, gather:

1. **Project Basics:**
   - "What Firebase project are you reviewing (dev, staging, prod)?"
   - "When was the last health check performed?"
   - "Has anything significant changed since the last review (new features, SDK updates, user growth)?"

2. **Current Concerns:**
   - "Are there any cost anomalies or unexpected bills?"
   - "Any recent security incidents or vulnerability reports?"
   - "Any performance complaints from users?"
   - "Any deprecated API warnings in build logs?"

3. **Metrics Access:**
   - "Do you have access to the Firebase Console for this project?"
   - "Do you have GCP billing access?"
   - "Is BigQuery export enabled for analytics?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before flagging ANY issue, you MUST:**

1. **Compare against baselines** — A cost increase of 20% might be normal growth, not an anomaly. Always compare against previous periods and user growth rates.
2. **Check the actual impact** — An outdated SDK version is not critical if it's still supported and has no known vulnerabilities. Prioritize by actual risk.
3. **Verify before recommending changes** — Especially for security rules. Don't recommend tightening rules without understanding the app's access patterns.
4. **Account for the developer's capacity** — A solo developer can't fix everything at once. Prioritize the most impactful items.

### False-Positive Prevention

- ❌ Do NOT flag every SDK minor version as "outdated" — only flag versions with security issues or approaching end-of-support
- ❌ Do NOT alarm about cost increases that correlate with legitimate user growth
- ❌ Do NOT recommend security rules changes without understanding existing access patterns
- ❌ Do NOT flag services with zero usage — they cost nothing and can be ignored
- ✅ DO compare current metrics against previous health check baselines
- ✅ DO calculate cost-per-user trends, not just absolute costs
- ✅ DO prioritize security and cost issues over optimization opportunities
- ✅ DO provide specific remediation steps, not vague recommendations

---

### Section 1: Security Review

#### 1.1 Firestore Security Rules

- [ ] **Rules last updated:** [Date] — Is this more than 3 months ago?
- [ ] **All collections have explicit rules** (no open `allow read, write: if true`)
- [ ] **Authentication required** for all non-public data
- [ ] **Field-level validation** on write operations
- [ ] **No wildcard matches** that bypass intended access control
- [ ] **Rate limiting considered** for expensive operations
- [ ] **Rules tested** since last change (emulator or live)

**Quick audit checklist:**
```
For each top-level collection:
  Read access:  [ ] Authenticated only  [ ] Owner only  [ ] Public (with justification)
  Write access: [ ] Authenticated only  [ ] Owner only  [ ] Validated fields
  Delete access: [ ] Owner only  [ ] Admin only  [ ] Disabled
```

#### 1.2 Cloud Storage Security Rules

- [ ] **No public write access** unless intentional (user uploads with validation)
- [ ] **File type restrictions** enforced (if applicable)
- [ ] **File size limits** enforced
- [ ] **Path-based access control** (users can only access their own files)

#### 1.3 Authentication Configuration

- [ ] **Unused auth providers disabled** (reduce attack surface)
- [ ] **Account enumeration protection** enabled
- [ ] **Password requirements** are reasonable (if email/password auth)
- [ ] **App Check enforced** or planned for enforcement
- [ ] **Custom claims** used appropriately (not over-relied upon)

#### 1.4 API Key Security

- [ ] **Firebase API keys** not exposed in public repositories
- [ ] **API key restrictions** configured in GCP Console (HTTP referrer or app restrictions)
- [ ] **Server-side keys** not embedded in client code
- [ ] **No secrets in Cloud Functions environment** — use Secret Manager

---

### Section 2: Cost Analysis

#### 2.1 Current Spend Overview

```markdown
| Service | Last Month | This Month | Change | Cost/User |
|---------|-----------|------------|--------|-----------|
| Firestore | $[X] | $[X] | [+/- %] | $[X] |
| Cloud Functions | $[X] | $[X] | [+/- %] | $[X] |
| Cloud Storage | $[X] | $[X] | [+/- %] | $[X] |
| Authentication | $[X] | $[X] | [+/- %] | $[X] |
| Hosting | $[X] | $[X] | [+/- %] | $[X] |
| **Total** | **$[X]** | **$[X]** | **[+/- %]** | **$[X]** |
```

#### 2.2 Cost Health Indicators

| Indicator | Healthy | Warning | Critical |
|-----------|---------|---------|----------|
| Month-over-month cost growth | < user growth | 2x user growth | > 3x user growth |
| Cost per DAU | < $0.01 | $0.01-$0.05 | > $0.05 |
| Free tier headroom | > 50% | 10-50% | < 10% or exceeded |
| Firestore read/write ratio | > 5:1 | 2-5:1 | < 2:1 (too many writes) |
| Cloud Functions p95 duration | < 5s | 5-15s | > 15s |

#### 2.3 Cost Optimization Opportunities

Review each service for optimization:

**Firestore:**
- [ ] Any real-time listeners that could be one-time reads?
- [ ] Client-side caching implemented for frequently-read data?
- [ ] Unused indexes deleted?
- [ ] Document reads per query optimized (no N+1 patterns)?

**Cloud Functions:**
- [ ] Any functions running longer than necessary?
- [ ] Cold start times acceptable? (< 3 seconds)
- [ ] maxInstances set on all functions?
- [ ] Any functions that could be replaced by security rules?

**Cloud Storage:**
- [ ] Lifecycle policies configured for temporary files?
- [ ] Unused files cleaned up?
- [ ] Image compression applied before upload?

---

### Section 3: SDK and Dependency Currency

#### 3.1 Firebase SDK Version Check

```markdown
| SDK | Current Version | Latest Version | Status | Action |
|-----|----------------|---------------|--------|--------|
| Firebase BOM | [current] | [latest] | [OK/Update/Critical] | [None/Update/Urgent] |
| Firestore | [current] | [latest] | [OK/Update/Critical] | |
| Auth | [current] | [latest] | [OK/Update/Critical] | |
| Cloud Functions SDK | [current] | [latest] | [OK/Update/Critical] | |
| Analytics | [current] | [latest] | [OK/Update/Critical] | |
| Crashlytics | [current] | [latest] | [OK/Update/Critical] | |
| Cloud Messaging | [current] | [latest] | [OK/Update/Critical] | |
```

**Status definitions:**
- **OK:** Within 1 minor version of latest
- **Update:** More than 1 minor version behind, no known vulnerabilities
- **Critical:** Known security vulnerabilities or approaching end-of-support

#### 3.2 Deprecated API Usage

- [ ] **Check build warnings** for Firebase deprecation notices
- [ ] **Review release notes** for deprecated features since last SDK version
- [ ] **Check Cloud Functions runtime** version (Node.js version supported?)
- [ ] **Check for deprecated Firestore methods** (e.g., v8 vs v9 modular API)

---

### Section 4: Performance Review

#### 4.1 App Performance (Firebase Performance Monitoring)

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| App start time (cold) | [X]ms | < 3000ms | [OK/Warning/Critical] |
| App start time (warm) | [X]ms | < 1500ms | [OK/Warning/Critical] |
| Network request success rate | [X]% | > 99% | [OK/Warning/Critical] |
| Network request latency (p90) | [X]ms | < 1000ms | [OK/Warning/Critical] |
| Screen rendering (slow frames) | [X]% | < 5% | [OK/Warning/Critical] |

#### 4.2 Crashlytics Review

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Crash-free users (last 7 days) | [X]% | > 99.5% | [OK/Warning/Critical] |
| ANR-free users (last 7 days) | [X]% | > 99.5% | [OK/Warning/Critical] |
| Top crash issue | [Description] | Investigated | [Open/In Progress/Resolved] |
| New crash clusters since last check | [N] | 0 | [OK/Investigate] |

#### 4.3 Cloud Functions Performance

| Function | Invocations/day | p50 Duration | p95 Duration | Error Rate |
|----------|----------------|-------------|-------------|------------|
| [function1] | [N] | [X]ms | [X]ms | [X]% |
| [function2] | [N] | [X]ms | [X]ms | [X]% |

---

### Section 5: Monitoring and Alerting Coverage

#### 5.1 Alert Configuration Check

| Alert | Configured | Channel | Working |
|-------|-----------|---------|---------|
| Budget alerts (GCP) | [Yes/No] | [Email/Slack] | [Verified/Unverified] |
| Crash spike alert | [Yes/No] | [Email] | [Verified/Unverified] |
| Error rate alert | [Yes/No] | [Email/Slack] | [Verified/Unverified] |
| Performance degradation | [Yes/No] | [Email] | [Verified/Unverified] |
| Auth anomaly (unusual signups) | [Yes/No] | [Email] | [Verified/Unverified] |

#### 5.2 Monitoring Gaps

- [ ] All production Cloud Functions have error alerting?
- [ ] Cost monitoring covers all services, not just total?
- [ ] Crash alerting sends notifications within 1 hour?
- [ ] Performance monitoring covers critical user flows?

---

### Section 6: Quota and Limits

#### 6.1 Firebase Quotas

| Quota | Limit | Current Usage | Headroom |
|-------|-------|--------------|----------|
| Firestore max document size | 1 MiB | [estimate] | [OK/Watch] |
| Firestore max writes/sec/doc | 1/sec | [estimate] | [OK/Watch] |
| Cloud Functions max instances | [configured] | [peak] | [OK/Watch] |
| Cloud Functions timeout | [configured] | [p99 duration] | [OK/Watch] |
| Storage max file size | [configured] | [largest file] | [OK/Watch] |
| Composite indexes | 200 max | [current] | [OK/Watch] |

---

## Expected Output

### Firebase Health Check Report

```markdown
# Firebase Health Check Report

## Project: [Project Name]
## Date: [Date]
## Reviewer: [You]
## Last Health Check: [Date or "First check"]

## Overall Health: [HEALTHY / NEEDS ATTENTION / CRITICAL]

## Executive Summary
- [1-2 sentence overall assessment]
- [Top priority action item]

## Section Scores

| Section | Score | Issues Found | Priority Items |
|---------|-------|-------------|----------------|
| Security | [Green/Yellow/Red] | [N] | [N] |
| Cost | [Green/Yellow/Red] | [N] | [N] |
| SDK Currency | [Green/Yellow/Red] | [N] | [N] |
| Performance | [Green/Yellow/Red] | [N] | [N] |
| Monitoring | [Green/Yellow/Red] | [N] | [N] |
| Quotas | [Green/Yellow/Red] | [N] | [N] |

## Action Items (Prioritized)

### Critical (Do This Week)
1. [Action item with specific steps]

### Important (Do This Month)
1. [Action item with specific steps]

### Nice to Have (Next Quarter)
1. [Action item with specific steps]

## Metrics Comparison

| Metric | Last Check | This Check | Trend |
|--------|-----------|------------|-------|
| Monthly cost | $[X] | $[X] | [↑/↓/→] |
| Cost/user | $[X] | $[X] | [↑/↓/→] |
| Crash-free rate | [X]% | [X]% | [↑/↓/→] |
| DAU | [N] | [N] | [↑/↓/→] |

## Next Health Check: [Date — 3 months from now]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Health check focus
- **ST-02** (Structured Sequential Instructions) - Systematic review process
- **RT-02** (Multi-Dimensional Analysis) - Security, cost, performance, monitoring dimensions
- **CM-01** (Explicit Context Framing) - Firebase project context
- **DS-06** (Prioritization Guidance) - Issue priority classification
- **QA-01** (Chain-of-Verification) - Baseline comparison and trend verification

---

## Related Prompts

- `firebase_cost_monitor_setup.md` - Set up cost monitoring referenced in this check
- `android_firebase_security_rules_audit.md` - Deep dive security rules audit
- `firebase_cloud_functions_design.md` - Functions architecture review
- `firestore_data_model_design.md` - Data model efficiency assessment
- `android_target_sdk_migration.md` - SDK migration planning

---

## Customization Guide

- **For projects with multiple environments:** Run this check on production first, then staging. Dev environments need less frequent checks (every 6 months).
- **For high-traffic apps (> 100K DAU):** Add a scalability section — check for approaching quotas, hot spots, and plan capacity for the next growth milestone.
- **For apps using Firebase Extensions:** Review extension versions, check for updates, and verify they're still needed (some may have been replaced by custom code).
- **For apps with Cloud Functions (Node.js):** Add Node.js runtime version check — Google deprecates older runtimes with notice. Running on a deprecated runtime blocks deployments.
- **For the first health check:** Focus on security and cost sections. Skip performance baselines (you'll establish them this time) and monitoring coverage (set up what's missing).
