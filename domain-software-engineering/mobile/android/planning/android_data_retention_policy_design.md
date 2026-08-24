---
title: "Data Retention Policy Design"
category: mobile-development
description: "Design a data retention policy for an Android app — what data to keep and for how long, automated deletion, user data requests, Firebase TTL policies, and regulatory requirements"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - android
  - data-retention
  - privacy
  - compliance
  - firebase
  - mobile-development
  - solo-developer
updated: "2026-02-12"
---

# Data Retention Policy Design

**Objective:** Design a comprehensive data retention policy for an Android application — defining retention periods for each category of data (user content, analytics, logs, backups), implementing automated deletion mechanisms, handling user data deletion requests, configuring Firebase TTL policies, and ensuring compliance with regulatory requirements (GDPR, CCPA) — producing both a policy document and technical implementation plan.

**When to Use:** Use this prompt when launching a new app and need to define data lifecycle policies, when preparing for GDPR/CCPA compliance, when your Firestore costs are growing and you need to purge old data, when users request data deletion and you need a systematic process, or when optimizing Firebase costs by removing stale data.

**Sequence Map:** Use after concept and data-model definition; use before production launch/compliance review.

**Important context:** Data retention is both a legal obligation and a cost optimization opportunity. GDPR requires data minimization (don't keep data longer than necessary for the stated purpose). CCPA gives users the right to request deletion. Meanwhile, Firebase charges for stored data — keeping data indefinitely means perpetually growing costs. A good retention policy balances legal compliance, user trust, business needs, and infrastructure costs.

---

## Context Gathering

1. **Data Types:**
   - "What categories of data does your app store (user profiles, content, messages, analytics, logs)?"
   - "Which data is stored locally (Room, DataStore) vs. remotely (Firestore, Storage, RTDB)?"
   - "Do you have backup systems? Where are backups stored?"
   - "Do you export data to BigQuery or other analytics systems?"

2. **Business Requirements:**
   - "Are there business reasons to retain data beyond the minimum (analytics, audit trails, legal holds)?"
   - "Do users have the ability to delete their accounts currently?"
   - "How often do you receive data deletion requests?"

3. **Regulatory:**
   - "Do you have EU users (GDPR)? California users (CCPA)? Other regulated jurisdictions?"
   - "Is your app subject to industry-specific regulations (HIPAA, COPPA, financial regulations)?"

---

## Instructions

### Step 1: Data Inventory and Classification

Categorize all data by retention needs:

| Data Category | Examples | Storage | Business Need | Legal Basis | Suggested Retention |
|---------------|----------|---------|--------------|-------------|-------------------|
| **Account Data** | Email, name, profile photo | Firebase Auth + Firestore | Core service | Contract | Until account deletion + 30 days |
| **User Content** | Posts, comments, files | Firestore + Storage | Core service | Contract | Until user deletes or account deletion |
| **Analytics Events** | Screen views, button clicks | Firebase Analytics | Product improvement | Legitimate interest | 14 months (Firebase default) |
| **Crash Reports** | Stack traces, device info | Crashlytics | App stability | Legitimate interest | 90 days |
| **Server Logs** | API requests, errors | Cloud Functions logs | Debugging, security | Legitimate interest | 30 days |
| **Authentication Logs** | Login attempts, IP addresses | Firebase Auth / custom | Security, fraud | Legitimate interest | 90 days |
| **Billing Records** | Purchase history, receipts | Play Billing + your DB | Legal requirement | Legal obligation | 7 years (tax) |
| **Support Communications** | Email threads, in-app messages | Email / support tool | Customer service | Legitimate interest | 2 years after resolution |
| **Marketing Consents** | Opt-in records, consent timestamps | Firestore | GDPR compliance | Legal obligation | Duration of consent + 3 years |
| **Backup Data** | Database snapshots | Cloud Storage / GCS | Disaster recovery | Legitimate interest | 30 days rolling |
| **Derived Analytics** | Cohort data, aggregated metrics | BigQuery | Business intelligence | Legitimate interest | Indefinite (anonymized) |
| **Deleted Account Data** | Anonymized/purged records | Firestore (tombstone) | Audit trail | Legitimate interest | 30 days post-deletion |

### Step 2: Retention Schedule

Design a retention schedule with clear rules:

```
ACTIVE DATA (user has active account):
├── User profile → Retained while account active
├── User content → Retained while account active (user can delete individual items)
├── Analytics → 14 months (Firebase default, configurable to 2/14/26/38/50 months)
├── Crash reports → 90 days
├── Server logs → 30 days
├── Auth logs → 90 days
└── Billing records → 7 years (legal requirement)

ACCOUNT DELETION (user requests account deletion):
├── Day 0: Mark account for deletion, disable login
├── Day 0-7: Grace period (user can reactivate)
├── Day 7: Begin data purge
│   ├── Delete user profile from Firestore
│   ├── Delete user content from Firestore + Storage
│   ├── Delete Firebase Auth record
│   ├── Delete FCM tokens
│   └── Request Analytics data deletion (via Google API)
├── Day 30: Verify all data deleted, remove tombstone record
└── Day 30+: Billing records retained per legal requirement (anonymized)

INACTIVE ACCOUNTS (no login for extended period):
├── 12 months inactive → Send re-engagement email
├── 18 months inactive → Send account inactivity warning
├── 24 months inactive → Disable account, begin deletion process
└── Follow same deletion timeline as user-requested deletion
```

### Step 3: Technical Implementation

**Automated Firestore TTL (Time-To-Live):**

```
// Firestore TTL policy (configured in Firebase Console or via CLI)
// Automatically deletes documents after expiration

// For documents with an 'expiresAt' field:
firebase firestore:databases:update default \
  --ttl-field="expiresAt" \
  --collection-group="server_logs"

// In your Cloud Function when creating log entries:
const logEntry = {
  message: "API request",
  timestamp: admin.firestore.FieldValue.serverTimestamp(),
  expiresAt: admin.firestore.Timestamp.fromDate(
    new Date(Date.now() + 30 * 24 * 60 * 60 * 1000) // 30 days
  ),
};
```

**Scheduled Cleanup Cloud Function:**

```typescript
// functions/src/cleanup.ts
import { onSchedule } from 'firebase-functions/v2/scheduler';
import { getFirestore } from 'firebase-admin/firestore';

export const dailyCleanup = onSchedule('every 24 hours', async (event) => {
  const db = getFirestore();
  const now = new Date();

  // Delete expired auth logs (>90 days)
  const authLogCutoff = new Date(now.getTime() - 90 * 24 * 60 * 60 * 1000);
  const expiredAuthLogs = await db.collection('auth_logs')
    .where('timestamp', '<', authLogCutoff)
    .limit(500) // Batch to avoid timeout
    .get();

  const batch = db.batch();
  expiredAuthLogs.docs.forEach(doc => batch.delete(doc.ref));
  await batch.commit();

  // Process pending account deletions
  const pendingDeletions = await db.collection('deletion_queue')
    .where('scheduledDate', '<=', now)
    .where('status', '==', 'pending')
    .get();

  for (const deletion of pendingDeletions.docs) {
    await processAccountDeletion(deletion.data().userId);
    await deletion.ref.update({ status: 'completed', completedAt: now });
  }
});
```

**User Account Deletion Flow:**

```kotlin
// Android - Account deletion request
class AccountDeletionViewModel @Inject constructor(
    private val auth: FirebaseAuth,
    private val firestore: FirebaseFirestore,
) : ViewModel() {

    fun requestAccountDeletion() {
        viewModelScope.launch {
            val userId = auth.currentUser?.uid ?: return@launch

            // 1. Create deletion queue entry (processed by Cloud Function)
            firestore.collection("deletion_queue").add(mapOf(
                "userId" to userId,
                "requestedAt" to FieldValue.serverTimestamp(),
                "scheduledDate" to Timestamp(Date(System.currentTimeMillis() + 7 * 24 * 60 * 60 * 1000L)), // 7-day grace
                "status" to "pending"
            )).await()

            // 2. Disable the account immediately
            // (Cloud Function handles actual deletion after grace period)

            // 3. Sign out the user
            auth.signOut()
        }
    }
}
```

### Step 4: Policy Document

Produce a data retention policy document for your privacy policy:

```markdown
## Data Retention

We retain your personal data only as long as necessary for the purposes
described in this privacy policy. Specific retention periods:

| Data | Retention Period | Basis |
|------|-----------------|-------|
| Account information | Until you delete your account | Service delivery |
| User-created content | Until you delete it or your account | Service delivery |
| Usage analytics | 14 months | Product improvement |
| Crash reports | 90 days | App stability |
| Purchase records | 7 years | Tax and legal requirements |

**Account Deletion:** You can delete your account at any time from
Settings → Account → Delete Account. After a 7-day grace period,
all your data will be permanently deleted within 30 days, except
purchase records required for legal compliance.

**Inactive Accounts:** Accounts inactive for 24 months may be deleted
after notice.
```

---

## Expected Output

1. **Data Inventory Table** — all data categories with retention periods and justification
2. **Retention Schedule** — clear timeline for each data lifecycle stage
3. **Technical Implementation Plan** — Firestore TTL, Cloud Functions, cleanup jobs
4. **Account Deletion Flow** — user-facing flow and backend processing
5. **Policy Document Text** — ready for inclusion in privacy policy
6. **Cost Impact Estimate** — projected storage savings from retention enforcement

---

## CRITICAL: Verification Requirements

- [ ] Every data category has a defined retention period with justification
- [ ] Billing/tax records are retained for the legally required period (typically 7 years)
- [ ] User account deletion is achievable within 30 days
- [ ] Automated cleanup jobs are scheduled and tested
- [ ] Backup systems respect retention policies (backups are purged too)
- [ ] Analytics data retention is configured in Firebase Console
- [ ] Privacy policy accurately reflects the retention schedule
