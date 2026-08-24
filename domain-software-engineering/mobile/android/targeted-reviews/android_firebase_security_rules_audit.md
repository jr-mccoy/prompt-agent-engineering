---
title: "Android Firebase Security Rules Audit"
category: mobile/android/targeted-reviews
description: "Android Firebase Security Rules Audit."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - firebase
  - mobile
  - reviews
  - rules
  - security
updated: "2026-03-19"
related_prompts: []
---

# Android Firebase Security Rules Audit

**Objective:** Conduct a comprehensive security audit of Firebase Realtime Database and Firestore security rules, analyzing authentication enforcement, data isolation, field-level protection, and vulnerability to common attack patterns.

**When to Use:** Use this prompt before production launch of Firebase-backed features, after security incidents, during compliance audits (GDPR, HIPAA), when adding new data paths, or as part of regular security review. Critical for any app storing sensitive user data in Firebase.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual data access path** - Don't flag based on pattern matching alone. Verify that the suspected rule gap actually allows unauthorized access.
2. **Check for server-side validation** - Search for Cloud Functions or server logic that may enforce additional security beyond rules.
3. **Understand the context** - Consider WHY certain paths may have specific access patterns. Some data is intentionally public or shared.
4. **Confirm actual exploitability** - Can this actually be exploited? Test with Firebase emulator or rules playground.
5. **Provide specific rule locations** - Every finding MUST include exact rule file paths and line numbers (e.g., `firestore.rules:45`).

**Finding NO issues is an acceptable outcome.** If Firebase security rules are properly configured, say so with confidence. Don't manufacture security concerns.

### False-Positive Prevention

- ❌ Do NOT flag intentionally public data as a security issue (e.g., app configuration, public content)
- ❌ Do NOT flag based solely on rule syntax without understanding the data model
- ❌ Do NOT assume missing validation without checking Cloud Functions
- ❌ Do NOT report theoretical issues without testing actual access scenarios
- ✅ DO test rules with Firebase Rules Playground before reporting
- ✅ DO understand the difference between Firestore and Realtime Database rule syntax
- ✅ DO check custom claims and their validation
- ✅ DO consider legitimate shared data access patterns (families, teams, organizations)

---

### 1. Authentication Enforcement

Verify all paths require authentication:

* **Public Access Check:**
  - Identify any paths readable without authentication
  - Check for write access without authentication
  - Assess intentional public data vs. misconfiguration
  - Verify no sensitive data in public paths

* **Auth Token Validation:**
  - Review auth != null checks on all paths
  - Check for proper auth.uid usage
  - Assess custom token claims validation
  - Verify email verification requirements

* **Anonymous Auth:**
  - Check if anonymous auth is allowed
  - Review permissions for anonymous users
  - Assess data migration on account linking
  - Verify anonymous user data isolation

### 2. Data Isolation

Evaluate user and tenant data separation:

* **User Data Isolation:**
  - Verify users can only access their own data
  - Check for proper ownership validation
  - Assess shared data access controls
  - Verify no cross-user data leakage

* **Family/Team Isolation:**
  - Check membership validation in rules
  - Review invitation/join access control
  - Assess role-based access within groups
  - Verify data isolation between groups

* **Path Traversal Prevention:**
  - Check for wildcard abuse
  - Review path variable validation
  - Assess parent/sibling access controls
  - Verify no directory traversal

### 3. Read Permission Analysis

Evaluate read access controls:

* **Sensitive Data Protection:**
  - Identify sensitive fields (PII, credentials, keys)
  - Check read restrictions on sensitive data
  - Assess query-based data exposure
  - Verify no sensitive data in list operations

* **Query Constraints:**
  - Review query limitations in rules
  - Check for data enumeration prevention
  - Assess pagination security
  - Verify indexed query requirements

* **Listener Security:**
  - Check real-time listener permissions
  - Review data change notification scope
  - Assess observer attack prevention
  - Verify no metadata leakage

### 4. Write Permission Analysis

Evaluate write access controls:

* **Data Validation:**
  - Check for data type validation
  - Review required field enforcement
  - Assess field length/size limits
  - Verify format validation (email, URL, etc.)

* **Field Protection:**
  - Identify fields users shouldn't modify (roles, timestamps)
  - Check for protected field enforcement
  - Assess computed field handling
  - Verify audit field protection

* **Batch/Transaction Security:**
  - Check multi-path write rules
  - Review transaction constraints
  - Assess atomic operation security
  - Verify no partial write exploits

### 5. Delete Permission Analysis

Evaluate delete access controls:

* **Delete Authorization:**
  - Check who can delete records
  - Review cascade delete handling
  - Assess soft vs. hard delete rules
  - Verify delete audit requirements

* **Data Retention:**
  - Check for deletion restrictions
  - Review regulatory retention rules
  - Assess archive before delete
  - Verify no accidental bulk delete

### 6. Rate Limiting and Abuse Prevention

Analyze abuse resistance:

* **Write Rate Limits:**
  - Check for timestamp-based rate limiting
  - Review write frequency restrictions
  - Assess quota enforcement
  - Verify DoS protection

* **Size Limits:**
  - Check document/node size limits
  - Review collection size restrictions
  - Assess storage quota rules
  - Verify no storage abuse

### 7. Realtime Database Specific

For Firebase Realtime Database:

* **Indexing Rules:**
  - Review .indexOn rules
  - Check query performance
  - Assess index security implications
  - Verify indexed paths are necessary

* **Validation Rules:**
  - Check .validate rules coverage
  - Review type validation
  - Assess business logic validation
  - Verify validation completeness

### 8. Firestore Specific

For Cloud Firestore:

* **Collection Group Queries:**
  - Check collection group security
  - Review cross-collection access
  - Assess subcollection permissions
  - Verify no data leakage via groups

* **Custom Claims:**
  - Review custom claim usage
  - Check claim validation
  - Assess claim refresh handling
  - Verify claim source integrity

---

## Expected Output

Provide a comprehensive Firebase security rules audit report including:

### 1. Executive Summary
- Overall security posture rating
- Authentication enforcement status
- Data isolation assessment
- Critical vulnerabilities count

### 2. Path Security Matrix

| Path | Auth Required | Isolation | Read | Write | Delete | Issues |
|------|---------------|-----------|------|-------|--------|--------|
| [Path] | [Yes/No] | [Method] | [Rules] | [Rules] | [Rules] | [Count] |

### 3. Vulnerability Assessment

| Vulnerability | Severity | Path | Exploit | Remediation |
|---------------|----------|------|---------|-------------|
| [Issue] | [Critical/High/Med/Low] | [Path] | [How] | [Fix] |

### 4. Detailed Findings

For each vulnerability:
- **Severity:** Critical/High/Medium/Low
- **Path:** Affected database path
- **Issue:** Description
- **Exploit Scenario:** How it could be attacked
- **Impact:** Data exposure/modification effect
- **Current Rules:** Problematic rules
- **Recommended Rules:** Secure version

### 5. Compliance Assessment

| Requirement | Status | Evidence | Action |
|-------------|--------|----------|--------|
| [Requirement] | [Met/Not Met] | [Where] | [If needed] |

### 6. Prioritized Remediation

Ordered by security impact.

---

## Example Output

```markdown
# Firebase Security Rules Audit Report

## Executive Summary
- **Security Posture:** At Risk - Multiple critical vulnerabilities
- **Authentication:** Mostly enforced, 2 public paths found
- **Data Isolation:** Weak - family membership not validated
- **Critical Issues:** 3 | High: 4 | Medium: 6 | Low: 5

## Critical Findings

### CRITICAL-1: Family Data Accessible to Any Authenticated User
**Severity:** Critical
**Impact:** Complete data breach - any user can read all family data

**Path:** /families/{familyId}/*

**Current Rules:**
```json
{
  "rules": {
    "families": {
      "$familyId": {
        // CRITICAL: Only checks if user is logged in!
        ".read": "auth != null",
        ".write": "auth != null"
      }
    }
  }
}
```

**Exploit Scenario:**
```javascript
// Any authenticated user can read ANY family's data
const attackerDb = firebase.database();
const victimFamilyId = "victim-family-123";

// Attacker reads all victim's todos
attackerDb.ref(`/families/${victimFamilyId}/todos`).once('value')
  .then(snapshot => {
    console.log("Stolen data:", snapshot.val());
    // Returns all of victim family's todos!
  });

// Attacker can also WRITE to victim's data
attackerDb.ref(`/families/${victimFamilyId}/todos/malicious`).set({
  title: "Hacked!",
  description: "Your data is compromised"
});
```

**Recommended Rules:**
```json
{
  "rules": {
    "families": {
      "$familyId": {
        // SECURE: Validate family membership
        ".read": "auth != null && root.child('familyMembers').child($familyId).child(auth.uid).exists()",
        ".write": "auth != null && root.child('familyMembers').child($familyId).child(auth.uid).exists()",

        "todos": {
          "$todoId": {
            ".read": "auth != null && root.child('familyMembers').child($familyId).child(auth.uid).exists()",
            ".write": "auth != null && root.child('familyMembers').child($familyId).child(auth.uid).exists()",
            ".validate": "newData.hasChildren(['title', 'createdBy', 'createdAt'])"
          }
        }
      }
    },

    "familyMembers": {
      "$familyId": {
        // Only family members can see membership
        ".read": "auth != null && data.child(auth.uid).exists()",
        "$userId": {
          // Only self can update own membership (or family admin)
          ".write": "auth.uid == $userId || root.child('familyAdmins').child($familyId).child(auth.uid).val() == true"
        }
      }
    }
  }
}
```

---

### CRITICAL-2: Invitation Tokens Readable by Anyone
**Severity:** Critical
**Impact:** Anyone can steal invitation tokens and join any family

**Path:** /invitations/{invitationId}

**Current Rules:**
```json
{
  "invitations": {
    "$invitationId": {
      ".read": "auth != null",  // Any authenticated user!
      ".write": "auth != null"
    }
  }
}
```

**Exploit:**
```javascript
// Attacker lists all invitations
db.ref('/invitations').once('value').then(snap => {
  snap.forEach(invitation => {
    // Steal token and join the family!
    const token = invitation.val().token;
    const familyId = invitation.val().familyId;
    joinFamily(familyId, token);
  });
});
```

**Recommended Rules:**
```json
{
  "invitations": {
    "$invitationId": {
      // Only the inviter can read (to revoke)
      ".read": "auth != null && data.child('createdBy').val() == auth.uid",

      // Only the inviter can create
      ".write": "!data.exists() && newData.child('createdBy').val() == auth.uid",

      // Token validation is done server-side with Cloud Functions
      // Never expose tokens in client-readable paths!
    }
  },

  // Tokens stored separately, not client-accessible
  "invitationTokens": {
    ".read": false,
    ".write": false
    // Only Cloud Functions can access this path
  }
}
```

**Additional Fix - Use Cloud Function for invitation redemption:**
```typescript
// Cloud Function to redeem invitation
exports.redeemInvitation = functions.https.onCall(async (data, context) => {
  if (!context.auth) throw new Error("Unauthenticated");

  const token = data.token;
  const tokenDoc = await admin.database()
    .ref(`/invitationTokens/${token}`).once('value');

  if (!tokenDoc.exists()) {
    throw new Error("Invalid invitation");
  }

  const invitation = tokenDoc.val();
  if (invitation.expiresAt < Date.now()) {
    throw new Error("Invitation expired");
  }

  // Add user to family (server-side, trusted)
  await admin.database()
    .ref(`/familyMembers/${invitation.familyId}/${context.auth.uid}`)
    .set({ joinedAt: Date.now(), role: "member" });

  // Delete used token
  await tokenDoc.ref.remove();

  return { familyId: invitation.familyId };
});
```

---

### CRITICAL-3: No Email Verification Check
**Severity:** Critical
**Impact:** Unverified accounts can access all data

**Path:** All paths

**Current Rules:**
```json
{
  "rules": {
    // Only checks auth != null, not email verification
    ".read": "auth != null",
    ".write": "auth != null"
  }
}
```

**Problem:**
- Attacker creates account with victim's email
- Accesses data immediately without verifying email
- Can impersonate victim in some scenarios

**Recommended Rules:**
```json
{
  "rules": {
    // Require verified email for all access
    ".read": "auth != null && auth.token.email_verified == true",
    ".write": "auth != null && auth.token.email_verified == true",

    // Exception: User can read their own verification status
    "users": {
      "$userId": {
        ".read": "auth.uid == $userId"
      }
    }
  }
}
```

---

### HIGH-1: Users Can Modify Their Own Roles
**Severity:** High
**Impact:** Privilege escalation - users can make themselves admin

**Path:** /familyMembers/{familyId}/{userId}/role

**Current Rules:**
```json
{
  "familyMembers": {
    "$familyId": {
      "$userId": {
        // Users can write to their own membership entry
        ".write": "auth.uid == $userId"
      }
    }
  }
}
```

**Exploit:**
```javascript
// User promotes themselves to admin
db.ref(`/familyMembers/${familyId}/${userId}`).update({
  role: "admin"  // Now I'm admin!
});
```

**Recommended Rules:**
```json
{
  "familyMembers": {
    "$familyId": {
      "$userId": {
        // Self can update profile, but not role
        ".write": "auth.uid == $userId || root.child('familyAdmins').child($familyId).child(auth.uid).val() == true",

        "role": {
          // Only family admins can change roles
          ".write": "root.child('familyAdmins').child($familyId).child(auth.uid).val() == true && auth.uid != $userId",
          ".validate": "newData.val() == 'member' || newData.val() == 'admin'"
        },

        "displayName": {
          ".write": "auth.uid == $userId",
          ".validate": "newData.isString() && newData.val().length <= 50"
        },

        "profilePhoto": {
          ".write": "auth.uid == $userId"
        }
      }
    }
  }
}
```

---

### HIGH-2: No Data Validation on Todos
**Severity:** High
**Impact:** Malicious data injection, app crashes

**Path:** /families/{familyId}/todos/{todoId}

**Current Rules:**
```json
{
  "todos": {
    "$todoId": {
      ".write": "auth != null && root.child('familyMembers').child($familyId).child(auth.uid).exists()"
      // No validation of data structure!
    }
  }
}
```

**Exploit:**
```javascript
// Inject malicious/oversized data
db.ref(`/families/${familyId}/todos/malicious`).set({
  title: "A".repeat(1000000),  // 1MB title crashes app
  maliciousScript: "<script>stealData()</script>",
  __proto__: { polluted: true }  // Prototype pollution attempt
});
```

**Recommended Rules:**
```json
{
  "todos": {
    "$todoId": {
      ".write": "auth != null && root.child('familyMembers').child($familyId).child(auth.uid).exists()",

      ".validate": "newData.hasChildren(['title', 'createdBy', 'createdAt']) &&
                    newData.child('title').isString() &&
                    newData.child('title').val().length >= 1 &&
                    newData.child('title').val().length <= 500 &&
                    newData.child('createdBy').val() == auth.uid &&
                    newData.child('createdAt').isNumber()",

      "title": {
        ".validate": "newData.isString() && newData.val().length >= 1 && newData.val().length <= 500"
      },
      "description": {
        ".validate": "!newData.exists() || (newData.isString() && newData.val().length <= 5000)"
      },
      "dueDate": {
        ".validate": "!newData.exists() || newData.isNumber()"
      },
      "status": {
        ".validate": "newData.val() == 'pending' || newData.val() == 'completed' || newData.val() == 'archived'"
      },
      "priority": {
        ".validate": "newData.val() >= 1 && newData.val() <= 5"
      },
      // Prevent additional fields
      "$other": {
        ".validate": false
      }
    }
  }
}
```

---

### MEDIUM-1: Timestamp Manipulation Possible
**Severity:** Medium
**Impact:** Data integrity issues, incorrect ordering

**Path:** /families/{familyId}/messages/{messageId}

**Current Rules:**
```json
{
  "messages": {
    "$messageId": {
      ".write": "auth != null && membershipValid",
      // Client provides timestamp - can be manipulated
    }
  }
}
```

**Recommended Rules:**
```json
{
  "messages": {
    "$messageId": {
      ".write": "auth != null && membershipValid",
      "timestamp": {
        // Use server timestamp
        ".validate": "newData.val() == now"
      },
      "createdAt": {
        // Only set on create, can't be modified
        ".write": "!data.exists()",
        ".validate": "newData.val() == now"
      },
      "modifiedAt": {
        ".validate": "newData.val() == now"
      }
    }
  }
}
```

---

## Path Security Matrix

| Path | Auth | Isolation | Read | Write | Delete | Issues |
|------|------|-----------|------|-------|--------|--------|
| /families/{fid} | ✓ | ❌ None | Any auth user | Any auth user | Any | 1 Critical |
| /families/{fid}/todos | ✓ | ❌ None | Any auth user | Any auth user | Any | 1 Critical |
| /familyMembers/{fid} | ✓ | Partial | Any auth user | Self | Self | 1 High |
| /invitations | ✓ | ❌ None | Any auth user | Any | Any | 1 Critical |
| /users/{uid} | ✓ | ✓ Self | Self only | Self only | Self | 0 |
| /messages | ✓ | Partial | Family | Family | Author | 1 Medium |

## Vulnerability Summary

| Type | Critical | High | Medium | Low |
|------|----------|------|--------|-----|
| Data Exposure | 2 | 1 | 2 | 1 |
| Privilege Escalation | 0 | 1 | 0 | 0 |
| Data Injection | 0 | 1 | 1 | 2 |
| No Validation | 1 | 1 | 2 | 2 |

## Compliance Assessment

| Requirement | Status | Issue | Action |
|-------------|--------|-------|--------|
| Data Isolation | ❌ | Family data accessible | Add membership checks |
| Email Verification | ❌ | Not required | Add to all rules |
| Data Validation | ❌ | Missing on most paths | Add .validate rules |
| Audit Trail | ⚠️ | Partial | Add createdBy/modifiedBy |
| Rate Limiting | ❌ | None | Add timestamp checks |

## Remediation Priority

### Critical (Deploy Today)
1. Add family membership validation to ALL family paths
2. Secure invitation tokens (move to server-only path)
3. Add email verification requirement

### High Priority (This Week)
1. Protect role field from self-modification
2. Add data validation to all writable paths
3. Implement server timestamps

### Medium Priority (Sprint)
1. Add rate limiting rules
2. Implement audit fields protection
3. Add size limits to all string fields

### Low Priority (Backlog)
1. Add collection group query restrictions
2. Implement custom claims for roles
3. Add compliance logging
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Security rules focus
- **ST-02** (Structured Sequential Instructions) - Systematic path analysis
- **RT-02** (Multi-Dimensional Analysis) - Auth, isolation, validation
- **RT-05** (Evidence-Based Reasoning) - Exploit scenarios
- **ST-03** (Output Format Templates) - Security matrix tables
- **DS-06** (Prioritization Guidance) - Security severity ordering
- **QA-02** (Adversarial Stress-Test) - Attack scenario analysis
- **RP-01** (Expert Role) - Security auditor perspective

---

## Related Prompts

- `android_sync_architecture_review.md` - For sync implementation
- `android_e2e_encryption_review.md` - For client-side security
- `mobile_app_security_review.md` - For comprehensive security
- `android_2fa_security_bypass_review.md` - For auth security
- `security_vulnerability_analysis.md` - For general security

---

## Customization Guide

- **For Firestore:** Adjust syntax, add collection group rules, custom claims
- **For Healthcare (HIPAA):** Add PHI path protection, audit requirements
- **For Financial Apps:** Add PCI-DSS checks, transaction integrity
- **For Social Apps:** Add content moderation rules, reporting paths
- **For Enterprise:** Add tenant isolation, admin path protection
