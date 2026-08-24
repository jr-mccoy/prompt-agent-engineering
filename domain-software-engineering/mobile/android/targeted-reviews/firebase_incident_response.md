---
title: "Firebase Incident Response for Solo Developers"
category: mobile-development
description: "Pre-written runbooks for the four most common Firebase incidents: cost spikes, security breaches, service outages, and data corruption. Includes detection, response, communication templates, and post-incident review procedures designed for a single developer managing Firebase infrastructure."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - CM-01  # Explicit Context Framing
  - QA-02  # Adversarial Thinking
difficulty: intermediate
tags:
  - firebase
  - incident-response
  - solo-developer
  - android
  - runbooks
  - cost-management
  - security
updated: "2026-02-11"
related_prompts:
  - domain-software-engineering/mobile/android/targeted-reviews/firebase_cost_monitor_setup.md
  - domain-software-engineering/mobile/android/targeted-reviews/firebase_cost_optimization.md
  - domain-software-engineering/mobile/android/targeted-reviews/firebase_health_check.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_firebase_security_rules_audit.md
  - domain-software-engineering/mobile/android/targeted-reviews/firebase_security_rules_generator.md
  - domain-software-engineering/devops/monitoring_solo_dev_alerting.md
---

# Firebase Incident Response for Solo Developers

**Objective:** Establish pre-written incident response runbooks for the four most common Firebase emergencies (cost spike, security breach, service outage, data corruption), including detection criteria, step-by-step response procedures, user communication templates, and post-incident review processes -- all designed for a single developer who cannot rely on an on-call team.

## When to Use

- Use when: Setting up incident response procedures for a Firebase-backed app before incidents occur (proactive)
- Use when: A Firebase incident is currently happening and you need a step-by-step response guide (reactive)
- Use when: You have experienced a Firebase incident and want to conduct a structured post-incident review
- Use when: Preparing for a production launch and need emergency procedures documented
- Do not use when: The issue is a general Firebase configuration task (use `firebase_health_check.md` instead)
- Do not use when: You are optimizing Firebase costs proactively (use `firebase_cost_optimization.md` instead)

**Important context:** As a solo developer, you do not have the luxury of a dedicated incident response team, a SRE on call, or a communications department. This means your runbooks must be pre-written, your responses semi-automated, and your decision-making streamlined. The most dangerous scenario is not the incident itself but the panic-driven response where you make things worse. These runbooks are designed to eliminate decision fatigue during a crisis by giving you an exact playbook to follow.

---

## Context Gathering

Before creating your runbooks, gather:

1. **Firebase Project Details:**
   - "What Firebase services are you using? (Authentication, Firestore, Realtime Database, Cloud Functions, Storage, Hosting, Cloud Messaging?)"
   - "What is your Firebase billing plan? (Spark/free, Blaze/pay-as-you-go)"
   - "Have you set up Firebase budget alerts? At what thresholds?"

2. **User Base:**
   - "How many active users do you have (DAU/MAU)?"
   - "Do you have a user communication channel? (In-app messaging, email list, status page, social media)"
   - "Are there SLA commitments to users or business stakeholders?"

3. **Data Sensitivity:**
   - "What types of user data does Firebase store? (PII, health data, financial data, authentication tokens)"
   - "Do you have data residency requirements?"
   - "Is the data backed up? How frequently? Where?"

4. **Current Monitoring:**
   - "Do you have Firebase Performance Monitoring enabled?"
   - "Do you have Crashlytics enabled?"
   - "Do you have budget alerts configured in Google Cloud Console?"
   - "Where do alerts go? (Email, SMS, Slack, PagerDuty?)"

5. **Recovery Resources:**
   - "Do you have access to Firebase console on mobile? (For responding outside work hours)"
   - "Do you have `gcloud` and `firebase` CLI tools installed locally?"
   - "Do you have a recent Firestore/RTDB export that could serve as a backup?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before executing ANY incident response action, you MUST:**

1. **Confirm the incident is real** -- False alarms from monitoring tools happen. Verify the issue exists by checking Firebase Console directly before taking action.
2. **Assess the blast radius** -- Determine how many users are affected and which features are impacted before deciding on response severity.
3. **Check if the issue is self-resolving** -- Some Firebase transient errors resolve within minutes. Wait 5 minutes and re-check before escalating.
4. **Document before acting** -- Note the timestamp, what you observed, and what you plan to do. Incident amnesia is real.
5. **Prefer reversible actions** -- Disabling a feature flag is reversible. Deleting data is not. Always choose the reversible option first.

### False-Positive Prevention

- Do NOT assume a cost spike is an attack -- it could be a viral feature, a botched migration script, or a monitoring tool polling too aggressively
- Do NOT shut down all Firebase services in response to one service having issues -- this causes a self-inflicted outage
- Do NOT delete Security Rules thinking you are "locking things down" -- empty rules in Firestore default to DENY ALL, which will break your app for every user
- Do NOT push a Firebase Rules update without testing -- a bad rule push can lock out all users or expose all data
- Do NOT communicate "we were hacked" to users without confirming a breach actually occurred -- this creates legal liability
- DO verify budget alerts against actual Firebase Console billing before panicking
- DO check the Google Cloud Status Dashboard before assuming the issue is on your side
- DO take screenshots of dashboards and error messages as evidence before making changes
- DO test Security Rules changes in the Firebase Emulator before deploying
- DO have a rollback plan for every action you take during an incident

---

### Phase 1: Incident Classification

When an incident is detected, classify it immediately using this decision tree:

```
ALERT RECEIVED
│
├─→ Is it about MONEY? (Budget alert, unexpected charges)
│   └─→ TYPE: COST SPIKE → Go to Phase 2
│
├─→ Is it about UNAUTHORIZED ACCESS? (Suspicious auth, data exfiltration)
│   └─→ TYPE: SECURITY BREACH → Go to Phase 3
│
├─→ Is it about SERVICE UNAVAILABILITY? (Errors, timeouts, app crashes)
│   └─→ TYPE: SERVICE OUTAGE → Go to Phase 4
│
└─→ Is it about DATA INTEGRITY? (Missing data, corrupted records, inconsistencies)
    └─→ TYPE: DATA CORRUPTION → Go to Phase 5
```

#### Severity Levels

| Level | Criteria | Response Time | Communication |
|-------|----------|---------------|---------------|
| **SEV-1 (Critical)** | All users affected, data at risk, cost unbounded | Immediate (wake up) | Status page + email within 30 min |
| **SEV-2 (Major)** | Many users affected, degraded service | Within 1 hour | Status page within 2 hours |
| **SEV-3 (Minor)** | Few users affected, workaround available | Within 4 hours | No external communication needed |
| **SEV-4 (Informational)** | No user impact, monitoring anomaly | Next business day | Internal note only |

---

### Phase 2: Cost Spike Runbook

**Trigger:** Firebase budget alert fires, or you notice unexpected charges in Google Cloud Billing.

#### Step 2.1: Assess the Damage (5 minutes)

```bash
# Check current billing status
gcloud billing accounts describe $(gcloud billing accounts list --format="value(name)" --limit=1)

# Check Firebase usage for the last 24 hours
# Go to: Firebase Console > Usage and billing > Usage
# Or: Google Cloud Console > Billing > Reports

# Identify which service is causing the spike
# Common culprert services:
# - Firestore: reads/writes/deletes
# - Realtime Database: bandwidth/connections
# - Cloud Functions: invocations/compute time
# - Storage: bandwidth/operations
# - Authentication: phone auth (SMS costs)
```

#### Step 2.2: Stop the Bleeding (15 minutes)

**If cost is from Firestore/RTDB reads (most common):**

```javascript
// Option A: Deploy rate-limiting Cloud Function
// functions/src/rateLimit.ts
exports.rateLimiter = functions.firestore
  .document('{collection}/{document}')
  .onRead(async (snap, context) => {
    // Log excessive reads for investigation
    const collection = context.params.collection;
    console.warn(`High read volume detected on: ${collection}`);
  });

// Option B: Emergency Security Rules (TEMPORARY)
// Restrict reads to authenticated users with rate limit
// Firestore rules:
// rules_version = '2';
// service cloud.firestore {
//   match /databases/{database}/documents {
//     match /{document=**} {
//       allow read: if request.auth != null
//                   && request.time > timestamp.date(2026, 1, 1);
//       allow write: if request.auth != null;
//     }
//   }
// }
```

**If cost is from Cloud Functions (runaway function):**

```bash
# List all functions and their invocation counts
gcloud functions list --project=YOUR_PROJECT_ID

# Disable the runaway function immediately
gcloud functions delete FUNCTION_NAME --project=YOUR_PROJECT_ID --quiet

# Or set max instances to 0 (less destructive)
gcloud functions deploy FUNCTION_NAME \
  --max-instances=0 \
  --project=YOUR_PROJECT_ID
```

**If cost is from phone authentication (SMS):**

```
1. Go to Firebase Console > Authentication > Settings
2. Temporarily disable phone authentication
3. Check for SMS pumping attack patterns (many failed verifications from same IP/region)
4. Enable App Check to block unauthorized API usage
```

#### Step 2.3: Set Billing Cap (If Not Already Set)

```bash
# Set a billing budget with auto-disable
# Google Cloud Console > Billing > Budgets & alerts
# Note: This can only ALERT, not auto-disable. For auto-disable:

# Create a Cloud Function that disables billing when budget exceeds threshold
# See: https://cloud.google.com/billing/docs/how-to/notify#cap_disable_billing_to_stop_usage
```

#### Step 2.4: Investigate Root Cause

```markdown
## Cost Spike Investigation Template

**Date detected:** [YYYY-MM-DD HH:MM]
**Service affected:** [Firestore / RTDB / Functions / Storage / Auth]
**Normal daily cost:** $[X]
**Spike cost:** $[Y] (X% increase)
**Duration of spike:** [start time] to [end time or ongoing]

### Possible Causes (check each):
- [ ] Viral user growth (legitimate traffic increase)
- [ ] Infinite loop in client code (check app release dates)
- [ ] Runaway Cloud Function (check function logs)
- [ ] Missing query index causing full collection scans
- [ ] Bot/scraping activity (check request patterns)
- [ ] Development/testing against production (check IP origins)
- [ ] SMS pumping attack on phone auth
- [ ] Third-party integration polling excessively

### Root Cause: [description]
### Resolution: [what you did]
### Prevention: [what to change to prevent recurrence]
```

---

### Phase 3: Security Breach Runbook

**Trigger:** Suspicious authentication activity, unauthorized data access, or security alert from Firebase.

#### Step 3.1: Contain the Breach (Immediate)

```bash
# 1. Revoke all active sessions (nuclear option -- use only if confirmed breach)
# Firebase Console > Authentication > Users > [select all compromised users]

# 2. Rotate all API keys
# Google Cloud Console > APIs & Services > Credentials
# Generate new keys, update app configuration

# 3. Lock down Security Rules (TEMPORARY emergency rules)
# This blocks ALL access except authenticated admin
```

```javascript
// EMERGENCY Firestore Rules (deploy only during active breach)
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      // Only allow admin SDK access (server-side)
      allow read, write: if false;
    }
  }
}

// EMERGENCY RTDB Rules
{
  "rules": {
    ".read": false,
    ".write": false
  }
}
```

**WARNING:** Emergency rules will break your app for ALL users. Only deploy if data exfiltration is actively occurring.

#### Step 3.2: Assess the Scope (30 minutes)

```bash
# Check authentication logs for anomalies
# Firebase Console > Authentication > Users
# Sort by "Last sign-in" and look for:
# - Unusual geographic locations
# - Bulk account creation
# - Password reset spikes

# Check Firestore/RTDB audit logs
gcloud logging read "resource.type=firestore_database" \
  --project=YOUR_PROJECT_ID \
  --freshness=24h \
  --format="table(timestamp, jsonPayload.methodName, jsonPayload.authInfo)"

# Check Cloud Functions logs for unauthorized invocations
gcloud functions logs read --limit=100 --project=YOUR_PROJECT_ID

# Check for data exfiltration
# Look for: bulk reads, unusual export operations, API key misuse
```

#### Step 3.3: Security Breach Assessment Template

```markdown
## Security Incident Assessment

**Date detected:** [YYYY-MM-DD HH:MM]
**Severity:** [SEV-1 / SEV-2 / SEV-3]
**Type:** [Unauthorized access / Data exfiltration / API key compromise / Account takeover]

### Scope
- Number of accounts affected: [N or unknown]
- Data types potentially exposed: [PII / auth tokens / user content / financial]
- Duration of exposure: [estimated start] to [detection time]

### Evidence
- [ ] Authentication anomalies documented
- [ ] Firestore/RTDB access logs reviewed
- [ ] Cloud Function invocation logs reviewed
- [ ] API key usage patterns checked
- [ ] Network traffic patterns analyzed

### Containment Actions Taken
1. [Action with timestamp]
2. [Action with timestamp]
3. [Action with timestamp]

### Regulatory Requirements
- [ ] GDPR notification required? (72-hour window for EU users)
- [ ] CCPA notification required? (California users)
- [ ] HIPAA notification required? (if health data involved)
- [ ] App store notification required?
```

#### Step 3.4: Recovery

```bash
# 1. Deploy hardened Security Rules (tested in emulator first!)
firebase emulators:start --only firestore
# Run rule tests against emulator
firebase emulators:exec "npm test" --only firestore

# 2. Force password reset for affected users
# Firebase Admin SDK:
# admin.auth().updateUser(uid, { disabled: true })
# Then send password reset email

# 3. Deploy new API keys to the app
# Update google-services.json
# Push emergency app update

# 4. Enable Firebase App Check (if not already enabled)
# This prevents unauthorized API access
# Firebase Console > App Check > Register app
```

---

### Phase 4: Service Outage Runbook

**Trigger:** App errors spiking in Crashlytics, users reporting failures, or Firebase services returning errors.

#### Step 4.1: Determine If It Is You or Firebase (5 minutes)

```markdown
## Outage Triage Checklist

### Check Firebase/Google Status First
- [ ] Google Cloud Status: https://status.cloud.google.com/
- [ ] Firebase Status: https://status.firebase.google.com/
- If Google shows an outage: WAIT. Document the outage. Communicate to users.

### Check Your Configuration
- [ ] Did you recently deploy Security Rules?
- [ ] Did you recently deploy Cloud Functions?
- [ ] Did you recently update the app?
- [ ] Did you recently change Firebase Console settings?

### Check Crashlytics
- [ ] Are crashes concentrated in one feature?
- [ ] Did crashes start after a specific app version?
- [ ] Are crashes on specific Android versions?
```

#### Step 4.2: If the Issue Is On Your Side

```bash
# Rollback recent Security Rules deployment
firebase firestore:rules:rollback --project=YOUR_PROJECT_ID

# Rollback recent Cloud Functions deployment
# Deploy previous version
gcloud functions deploy FUNCTION_NAME \
  --source=gs://YOUR_BUCKET/previous-version.zip \
  --project=YOUR_PROJECT_ID

# If issue is in app code, push hotfix or enable kill switch
# Use Firebase Remote Config as a feature kill switch
```

```kotlin
// Emergency kill switch via Remote Config
class FeatureFlags @Inject constructor(
    private val remoteConfig: FirebaseRemoteConfig
) {
    fun isFeatureEnabled(feature: String): Boolean {
        // Remote Config can disable features server-side
        // without an app update
        return remoteConfig.getBoolean("feature_${feature}_enabled")
    }
}

// In your Activity/Fragment:
if (!featureFlags.isFeatureEnabled("sync")) {
    showMaintenanceMessage()
    return
}
```

#### Step 4.3: If the Issue Is Firebase-Side

```markdown
## Firebase Outage Response (When It Is Not Your Fault)

1. **Document:** Screenshot the status page, note the start time
2. **Communicate:** Post to your status page / send notification
3. **Degrade Gracefully:** Enable offline mode if your app supports it
4. **Monitor:** Check status page every 15 minutes
5. **Recover:** When Firebase recovers, verify your data integrity
6. **Review:** Check if any writes were lost during the outage

### Offline Mode Activation
If your app uses Firebase offline persistence, it should continue
working with cached data. If not, display a maintenance screen.
```

---

### Phase 5: Data Corruption Runbook

**Trigger:** Users report missing or incorrect data, data audit reveals inconsistencies, or backup comparison shows divergence.

#### Step 5.1: Isolate the Corruption (Immediate)

```bash
# 1. Identify which collections/paths are affected
# Firestore: Check collection document counts vs expected
firebase firestore:export gs://YOUR_BUCKET/emergency-backup-$(date +%Y%m%d)

# 2. Compare with last known good backup
# If you have scheduled exports:
gsutil ls gs://YOUR_BUCKET/backups/ | sort | tail -5

# 3. Stop writes to affected collections (temporary rule)
```

```javascript
// Temporary write-freeze for affected collection
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Freeze writes to corrupted collection
    match /affected_collection/{doc} {
      allow read: if request.auth != null;
      allow write: if false; // FROZEN during investigation
    }
    // All other collections normal
    match /{other_collection}/{doc} {
      allow read, write: if request.auth != null;
    }
  }
}
```

#### Step 5.2: Assess Corruption Scope

```markdown
## Data Corruption Assessment

**Date detected:** [YYYY-MM-DD HH:MM]
**Collections affected:** [list]
**Documents affected:** [count or estimate]
**Last known good state:** [backup date/time]

### Corruption Type
- [ ] Missing documents (deletions)
- [ ] Modified fields (wrong values)
- [ ] Duplicated documents
- [ ] Orphaned references (broken relationships)
- [ ] Schema violations (wrong field types)

### Root Cause Candidates
- [ ] Cloud Function bug (check deployment history)
- [ ] Client-side bug (check app release history)
- [ ] Race condition in concurrent writes
- [ ] Security Rules allowing unvalidated writes
- [ ] Manual edit in Firebase Console
- [ ] Third-party integration writing bad data
```

#### Step 5.3: Restore from Backup

```bash
# Firestore restore from export
gcloud firestore import gs://YOUR_BUCKET/backups/YYYY-MM-DD \
  --collection-ids=affected_collection \
  --project=YOUR_PROJECT_ID

# RTDB restore from backup
firebase database:set / --data @backup.json --project=YOUR_PROJECT_ID

# Selective restore (only corrupted documents)
# Use Admin SDK script to compare backup with current data
# and restore only changed documents
```

```python
# scripts/selective_restore.py
# Compare backup export with current Firestore state
# and restore only documents that differ

import firebase_admin
from firebase_admin import credentials, firestore
import json

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)
db = firestore.client()

def restore_collection(collection_name, backup_file):
    with open(backup_file) as f:
        backup_data = json.load(f)

    current_docs = {doc.id: doc.to_dict()
                    for doc in db.collection(collection_name).stream()}

    restored = 0
    for doc_id, backup_doc in backup_data.items():
        current = current_docs.get(doc_id)
        if current != backup_doc:
            db.collection(collection_name).document(doc_id).set(backup_doc)
            restored += 1
            print(f"Restored: {collection_name}/{doc_id}")

    print(f"Total restored: {restored} documents")
```

---

## Communication Templates

### Status Page Update Template

```markdown
## [Incident Type] - [Date]

**Status:** [Investigating | Identified | Monitoring | Resolved]
**Impact:** [Description of user impact]
**Last updated:** [HH:MM timezone]

### Timeline
- **HH:MM** - We detected [issue description].
- **HH:MM** - We identified the cause as [brief cause].
- **HH:MM** - We deployed a fix and are monitoring.
- **HH:MM** - Service restored. All systems operational.

### What happened
[1-2 sentences in plain language]

### What we are doing
[Current actions being taken]

### Next update
We will provide another update by [HH:MM timezone] or sooner if the situation changes.
```

### User Email Template (For Security/Data Incidents)

```markdown
Subject: Important Security Notice - [App Name]

Dear [User / valued user],

We are writing to let you know about a security incident that
affected [App Name] on [date].

**What happened:**
[Brief, honest description -- avoid technical jargon]

**What information was involved:**
[Specific data types that may have been affected]

**What we have done:**
- [Action 1 -- e.g., "Secured the affected systems"]
- [Action 2 -- e.g., "Reset authentication tokens"]
- [Action 3 -- e.g., "Enhanced monitoring"]

**What you should do:**
- Change your password at [link]
- [Additional recommended actions]
- Contact us at [support email] if you notice unusual activity

**How to reach us:**
[Contact information]

We take the security of your data seriously and apologize for
any concern this may cause.

Sincerely,
[Your name]
[App Name]
```

---

## Post-Incident Review Template

Conduct a post-incident review within 48 hours of resolution for SEV-1 and SEV-2 incidents.

```markdown
# Post-Incident Review: [Incident Title]

**Date of incident:** [YYYY-MM-DD]
**Duration:** [start time] to [resolution time] ([N] hours)
**Severity:** [SEV-1 / SEV-2 / SEV-3]
**Author:** [Your name]
**Review date:** [YYYY-MM-DD]

## Summary
[2-3 sentence summary of what happened and the impact]

## Timeline
| Time | Event |
|------|-------|
| HH:MM | [First detection signal] |
| HH:MM | [Investigation started] |
| HH:MM | [Root cause identified] |
| HH:MM | [Fix deployed] |
| HH:MM | [Service restored] |
| HH:MM | [Monitoring confirmed resolution] |

## Root Cause
[Detailed explanation of what actually went wrong]

## Impact
- **Users affected:** [N or percentage]
- **Features impacted:** [list]
- **Data affected:** [description]
- **Financial impact:** [cost of incident + response time]

## What Went Well
1. [Something that helped during the response]
2. [Something that worked as designed]

## What Went Poorly
1. [Something that made the response harder]
2. [Something that should have caught this earlier]

## Action Items
| Priority | Action | Owner | Due Date | Status |
|----------|--------|-------|----------|--------|
| P1 | [Immediate fix / prevention] | [You] | [Date] | [ ] |
| P2 | [Monitoring improvement] | [You] | [Date] | [ ] |
| P3 | [Process improvement] | [You] | [Date] | [ ] |

## Lessons Learned
- [Key takeaway 1]
- [Key takeaway 2]

## Recurrence Prevention
[What specific changes will prevent this exact incident from happening again]
```

---

## Expected Output

The analysis should produce a complete incident response playbook:

### Output Format

```markdown
# Firebase Incident Response Playbook
**Project:** [Project Name]
**Date Created:** [Date]
**Last Tested:** [Date or "Not yet tested"]

## Quick Reference Card
[One-page summary of all four runbooks with key commands]

## Runbook 1: Cost Spike Response
[Customized for your specific Firebase services and billing plan]

## Runbook 2: Security Breach Response
[Customized for your data types and regulatory requirements]

## Runbook 3: Service Outage Response
[Customized for your app architecture and offline capabilities]

## Runbook 4: Data Corruption Response
[Customized for your collections, backup schedule, and restore procedures]

## Communication Templates
[Pre-filled with your app name, support email, and status page URL]

## Post-Incident Review Template
[Ready to fill in during the next incident]

## Emergency Contacts & Links
- Firebase Console: [URL]
- Google Cloud Console: [URL]
- Status Page: [URL]
- Backup Location: [path]
- Emergency Rules File: [path]
```

---

## Customization Guide

- **For apps with no user communication channel:** Set up a simple status page using Firebase Hosting with a static HTML page you can update manually. Services like Instatus or Atlassian Statuspage have free tiers.
- **For apps with HIPAA requirements:** Add mandatory breach notification timelines (60 days for HIPAA). Ensure all incident documentation is stored in a HIPAA-compliant location. Never include PHI in incident communications.
- **For apps using Firebase Extensions:** Add a section to each runbook for checking extension health. Extensions can fail silently and cause data processing gaps.
- **For apps with multiple Firebase projects (dev/staging/prod):** Add environment verification to every runbook step. The most common solo-dev mistake is running destructive commands against the wrong project. Use `firebase use` to confirm the active project before every command.
- **For monetized apps:** Add revenue impact calculation to the post-incident review. Track "cost of downtime" as: (average revenue per minute) x (minutes of downtime) + (cost of incident response time).

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defines four specific runbooks as the deliverable, each with detection, response, communication, and review components.
- **ST-02 (Structured Sequential Instructions):** Each runbook follows a strict step-by-step sequence with time-boxed activities (5 minutes for assessment, 15 minutes for containment).
- **RT-02 (Multi-Dimensional Analysis):** Incidents are classified across type (cost/security/outage/data), severity (SEV-1 through SEV-4), and response urgency.
- **CM-01 (Explicit Context Framing):** The solo developer context shapes every recommendation -- no delegation, pre-written templates, semi-automated responses.
- **QA-02 (Adversarial Thinking):** False-Positive Prevention guards against panic-driven responses, self-inflicted outages from overly aggressive containment, and premature breach notifications.

---

## Related Prompts

- [firebase_cost_monitor_setup.md](firebase_cost_monitor_setup.md) - Set up proactive cost monitoring before incidents occur
- [firebase_cost_optimization.md](firebase_cost_optimization.md) - Reduce Firebase costs to prevent cost spikes
- [firebase_health_check.md](firebase_health_check.md) - Regular health check to catch issues before they become incidents
- [android_firebase_security_rules_audit.md](android_firebase_security_rules_audit.md) - Proactive security rules review
- [firebase_security_rules_generator.md](firebase_security_rules_generator.md) - Generate secure rules to prevent breaches
- [monitoring_solo_dev_alerting.md](../../../devops/monitoring_solo_dev_alerting.md) - Alerting strategy that feeds into these runbooks
