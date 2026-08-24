---
name: android-firebase-sync-validator
description: Validates that Android app data properly syncs to Firebase (Realtime Database, Firestore, and Cloud Functions) by analyzing app features, identifying sync requirements, verifying cloud infrastructure completeness, and automatically correcting issues. Creates and maintains a persistent map of data points and their cloud rules. Use this skill when working with Android Firebase apps, troubleshooting sync issues, auditing Firebase rules, ensuring data protection, or when users mention "Firebase sync validation", "check Firebase rules", "Firebase data not syncing", "validate cloud functions", or "audit Firebase security".
metadata:
  tags:
    - android
    - firebase
    - mobile
    - security
    - sync
    - validator
  updated: "2026-04-11"
---
# Android Firebase Sync Validator

Comprehensive validation and automatic correction of Firebase cloud infrastructure for Android apps. Ensures all app data that should sync to Firebase is properly captured by Realtime Database rules, Firestore rules, and Cloud Functions.

## Purpose

This skill prevents data loss and security vulnerabilities by ensuring:
- All app data requiring cloud sync is properly configured in Firebase
- Firebase Security Rules adequately protect user data
- Cloud Functions correctly process all expected data events
- Cloud infrastructure matches app feature requirements

Creates a persistent sync map on first run to avoid starting from scratch on subsequent runs, enabling efficient incremental validation.

## When to Use This Skill

Use this skill when you need to:
- Validate Firebase sync configuration for an Android app
- Audit Firebase Realtime Database rules, Firestore rules, and Cloud Functions
- Ensure all app features have proper cloud infrastructure support
- Troubleshoot Firebase sync issues or data not appearing in cloud
- Verify Firebase security rules adequately protect user data
- Document the relationship between app code and Firebase infrastructure
- Automatically fix incomplete or incorrect Firebase configurations

## When NOT to Use This Skill

Do NOT use this skill when:
- Working with non-Firebase backends (use appropriate backend validation skill)
- App doesn't sync data to cloud (local-only apps)
- Working with iOS apps (use iOS-specific Firebase validator)
- Only need to generate Firebase config from scratch (use firebase-config-generator)

## Prerequisites

- Android app codebase with Firebase integration
- Firebase configuration files in repository (google-services.json, database rules, Firestore rules, Cloud Functions code)
- Python 3.8+
- Access to Firebase project configuration

## Quick Start

### Step 1: Analyze App Features and Data Models

**Purpose:** Understand what app features exist and what data should sync to Firebase.

**Skip if:** You've recently created a sync map and app features haven't changed significantly.

**Procedure:**
1. Scan the Android codebase for Firebase SDK usage:
   - Look for Firebase Realtime Database references (`DatabaseReference`, `FirebaseDatabase`)
   - Look for Firestore references (`FirebaseFirestore`, `CollectionReference`, `DocumentReference`)
   - Look for data models annotated or used with Firebase
   - Identify all data paths being read from or written to Firebase

2. Analyze app features to determine sync requirements:
   - Review Activity/Fragment files to understand feature scope
   - Identify user data, shared data, and app state
   - Determine data privacy and sharing requirements
   - Map features to data models

3. Use the analysis script:
```bash
python scripts/analyze_data_models.py /path/to/android/app \
  --output .firebase-sync-validator/app_analysis.json
```

**Expected output:**
```json
{
  "data_models": [
    {
      "name": "User",
      "file": "app/src/main/java/com/example/models/User.kt",
      "firebase_paths": ["/users/{uid}"],
      "sync_type": "firestore",
      "privacy": "private"
    }
  ],
  "features": [
    {
      "name": "User Profile",
      "files": ["UserProfileActivity.kt"],
      "data_dependencies": ["User", "UserPreferences"]
    }
  ]
}
```

**Validation:**
- [ ] All Firebase SDK usages identified
- [ ] All data models mapped to Firebase paths
- [ ] App features catalogued with data dependencies
- [ ] Privacy requirements documented

### Step 2: Create or Load Sync Map

**Purpose:** Establish a persistent mapping between app data, code locations, and Firebase infrastructure.

**Skip if:** This is not the first run and sync map exists at `.firebase-sync-validator/sync_map.json`.

**Procedure:**

**First run - Create new sync map:**
1. Generate initial sync map from analysis:
```bash
python scripts/validate_sync_coverage.py \
  --app-analysis .firebase-sync-validator/app_analysis.json \
  --create-map .firebase-sync-validator/sync_map.json
```

2. Sync map will contain:
   - Data points requiring cloud sync
   - Code locations (files and line numbers)
   - Expected Firebase paths
   - Required security rules
   - Required Cloud Functions
   - Coverage status (complete/incomplete/missing)

**Subsequent runs - Load existing sync map:**
1. Load and update sync map:
```bash
python scripts/validate_sync_coverage.py \
  --app-analysis .firebase-sync-validator/app_analysis.json \
  --sync-map .firebase-sync-validator/sync_map.json \
  --update-map
```

**Sync map structure:**
```json
{
  "version": "1.0",
  "last_updated": "2025-12-29T10:30:00Z",
  "data_points": [
    {
      "id": "user_profile_data",
      "data_model": "User",
      "code_location": {
        "file": "app/src/main/java/com/example/models/User.kt",
        "lines": [15, 42]
      },
      "firebase_paths": {
        "firestore": "users/{uid}",
        "rtdb": null
      },
      "required_rules": {
        "firestore": ["allow read: if request.auth.uid == uid", "allow write: if request.auth.uid == uid"]
      },
      "required_functions": ["onUserCreate", "onUserUpdate"],
      "coverage_status": {
        "firestore_rules": "complete",
        "rtdb_rules": "n/a",
        "cloud_functions": "incomplete"
      }
    }
  ]
}
```

**Validation:**
- [ ] Sync map created/loaded successfully
- [ ] All data points from analysis included
- [ ] Code locations accurate
- [ ] Firebase paths properly formatted

### Step 3: Validate Firebase Infrastructure Coverage

**Purpose:** Verify that Firebase Realtime Database rules, Firestore rules, and Cloud Functions adequately cover all sync requirements.

**Procedure:**
1. Point the validator to your Firebase configuration files:
```bash
python scripts/validate_sync_coverage.py \
  --sync-map .firebase-sync-validator/sync_map.json \
  --rtdb-rules database.rules.json \
  --firestore-rules firestore.rules \
  --functions-dir functions/src \
  --output .firebase-sync-validator/coverage_report.json
```

2. The validator checks:
   - **RTDB Rules:** All paths have appropriate read/write rules with auth checks
   - **Firestore Rules:** All collections/documents have security rules matching privacy requirements
   - **Cloud Functions:** All required data events have corresponding functions
   - **Security:** Auth requirements, data validation, privacy protection

**Expected output on success:**
```
✓ Firebase infrastructure validation passed

Coverage Summary:
  Firestore Rules: 15/15 data points covered (100%)
  RTDB Rules: 8/8 data points covered (100%)
  Cloud Functions: 12/12 required functions found (100%)

Security Validation:
  ✓ All rules require authentication
  ✓ No overly permissive rules found
  ✓ Data validation present for user inputs
```

**Expected output on failure:**
```
✗ Firebase infrastructure validation failed: 5 issues found

Issues:

[CRITICAL] Missing Firestore rule for: users/{uid}/privateData
  Data: UserPrivateData
  Location: app/src/main/java/com/example/models/UserPrivateData.kt:25
  Required: allow read, write: if request.auth.uid == uid
  Current: No rule found

[HIGH] Insufficient RTDB rule for: /messages/{chatId}
  Data: ChatMessage
  Location: app/src/main/java/com/example/chat/ChatActivity.kt:112
  Required: Multi-user access with member validation
  Current: allow read, write: if auth != null (too permissive)

[MEDIUM] Missing Cloud Function: onUserDelete
  Data: User
  Required for: Cascade delete of user data
  Location: Referenced in app/src/main/java/com/example/settings/DeleteAccountActivity.kt:89

[LOW] RTDB rule lacks data validation: /posts/{postId}/content
  Data: Post.content
  Current: Allows any data type
  Recommended: Add content.length validation

[INFO] Cloud Function exists but may be outdated: onMessageCreate
  Function: functions/src/messaging.ts:45
  Reason: App code expects 'read_by' field but function doesn't populate it
```

**Validation:**
- [ ] All Firebase config files found
- [ ] Coverage report generated
- [ ] Issues clearly identified with severity levels
- [ ] Code locations provided for all issues

### Step 4: Review and Approve Fixes

**Purpose:** Generate automatic fixes for identified issues and allow user review before applying.

**Freedom level:** High
- User must approve all changes before they're applied
- Script generates fixes but doesn't modify files automatically
- User can customize generated fixes

**Procedure:**
1. Generate fixes for identified issues:
```bash
python scripts/fix_sync_issues.py \
  --coverage-report .firebase-sync-validator/coverage_report.json \
  --rtdb-rules database.rules.json \
  --firestore-rules firestore.rules \
  --functions-dir functions/src \
  --preview-only \
  --output .firebase-sync-validator/proposed_fixes/
```

2. Review proposed fixes:
   - Each fix is generated as a separate file in `proposed_fixes/`
   - Diff shows what will be added/changed
   - Explanation provided for each fix

**Example proposed fix:**
```
File: proposed_fixes/firestore_rules_001.diff

Issue: Missing Firestore rule for users/{uid}/privateData
Severity: CRITICAL

Proposed Change:
=================================================================
--- firestore.rules (current)
+++ firestore.rules (proposed)
@@ line 45 @@

+    // Rule for user private data - ensures only owner can access
+    match /users/{uid}/privateData {
+      allow read, write: if request.auth != null && request.auth.uid == uid;
+
+      // Validate data structure
+      allow write: if request.resource.data.keys().hasAll(['email', 'phone'])
+                   && request.resource.data.email is string
+                   && request.resource.data.phone is string;
+    }

Explanation:
- Restricts read/write access to authenticated user who owns the data
- Validates that required fields (email, phone) are present and have correct types
- Prevents unauthorized access to private user data
- Matches privacy requirement from UserPrivateData model
=================================================================
```

**Validation:**
- [ ] All proposed fixes reviewed
- [ ] Explanations are clear and match requirements
- [ ] No unintended side effects identified
- [ ] Security implications understood

### Step 5: Apply Approved Fixes

**Purpose:** Apply approved fixes to Firebase configuration files.

**Safety constraints:**
- Backups created before any modifications
- Changes applied incrementally with validation
- Rollback available if issues occur

**Procedure:**
1. Create backups:
```bash
python scripts/fix_sync_issues.py \
  --coverage-report .firebase-sync-validator/coverage_report.json \
  --rtdb-rules database.rules.json \
  --firestore-rules firestore.rules \
  --functions-dir functions/src \
  --create-backups .firebase-sync-validator/backups/
```

2. Apply fixes:
```bash
python scripts/fix_sync_issues.py \
  --coverage-report .firebase-sync-validator/coverage_report.json \
  --rtdb-rules database.rules.json \
  --firestore-rules firestore.rules \
  --functions-dir functions/src \
  --apply-fixes \
  --fixes-dir .firebase-sync-validator/proposed_fixes/
```

3. The script will:
   - Apply each fix one at a time
   - Validate syntax after each change
   - Report success/failure for each fix
   - Update sync map with new coverage status

**Expected output:**
```
Applying fixes...

[1/5] Applying firestore_rules_001.diff
  ✓ Fix applied successfully
  ✓ Syntax validation passed
  ✓ Sync map updated

[2/5] Applying rtdb_rules_001.diff
  ✓ Fix applied successfully
  ✓ Syntax validation passed
  ✓ Sync map updated

[3/5] Applying cloud_function_001.diff
  ✓ Fix applied successfully
  ✓ Syntax validation passed
  ✓ Function onUserDelete created
  ✓ Sync map updated

All fixes applied successfully!

Updated coverage:
  Firestore Rules: 15/15 (100%) ⬆️ +1
  RTDB Rules: 8/8 (100%) ⬆️ +1
  Cloud Functions: 12/12 (100%) ⬆️ +1

Backups stored in: .firebase-sync-validator/backups/2025-12-29_103045/
```

**Validation:**
- [ ] All fixes applied without errors
- [ ] Syntax validation passed for all files
- [ ] Sync map updated with new coverage status
- [ ] Backups created and accessible

### Step 6: Verify and Deploy

**Purpose:** Final validation and deployment to Firebase.

**Procedure:**
1. Re-run validation to confirm all issues resolved:
```bash
python scripts/validate_sync_coverage.py \
  --sync-map .firebase-sync-validator/sync_map.json \
  --rtdb-rules database.rules.json \
  --firestore-rules firestore.rules \
  --functions-dir functions/src \
  --final-validation
```

2. Review the updated sync map:
```bash
cat .firebase-sync-validator/sync_map.json | jq '.data_points[] | select(.coverage_status | contains("incomplete"))'
```

3. If validation passes, deploy to Firebase:
```bash
# Deploy Firestore rules
firebase deploy --only firestore:rules

# Deploy RTDB rules
firebase deploy --only database

# Deploy Cloud Functions
cd functions && npm install && cd .. && firebase deploy --only functions
```

**Validation:**
- [ ] Final validation shows 100% coverage
- [ ] No remaining CRITICAL or HIGH severity issues
- [ ] Firebase deployment successful
- [ ] App tested with new rules (no access denied errors)

## Understanding the Sync Map

The sync map (`.firebase-sync-validator/sync_map.json`) is the persistent state that enables efficient incremental validation.

**Key benefits:**
- **Avoids re-scanning entire codebase** on every run
- **Tracks historical changes** to see coverage improvements over time
- **Documents intent** - explains why each Firebase rule/function exists
- **Enables regression detection** - alerts if coverage drops

**When sync map is updated:**
- First run: Created from scratch based on codebase analysis
- Subsequent runs: Updated when new data models or Firebase paths detected
- After fixes applied: Coverage status updated for each data point
- Manual updates: Can be edited to add context or fix incorrect mappings

**Sync map maintenance:**
1. Commit sync map to version control
2. Update when app features change
3. Review during code reviews
4. Regenerate if major refactoring occurs

## Troubleshooting and Constraints

Common Firebase sync issues with diagnosis, root causes, and resolution commands (4 issue types: missing sync map entry, overly permissive rules, missing cascade Cloud Function, out-of-date sync map after refactoring), edge cases and failure modes (5 scenarios), and safety constraints (NEVER/ALWAYS rules).

See [references/troubleshooting-and-constraints.md](references/troubleshooting-and-constraints.md)

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/analyze_data_models.py` | Analyzes Android codebase for Firebase usage and data models |
| `scripts/validate_sync_coverage.py` | Validates Firebase infrastructure coverage against sync requirements |
| `scripts/fix_sync_issues.py` | Generates and applies fixes for identified issues |
| `references/firebase_security_rules.md` | Firebase security rules best practices and patterns |
| `references/rtdb_rules_patterns.md` | Common Realtime Database rules patterns |
| `references/firestore_rules_patterns.md` | Common Firestore rules patterns |
| `references/cloud_functions_patterns.md` | Common Cloud Functions patterns for Android apps |
| `references/troubleshooting-and-constraints.md` | Common issues (4 types), edge cases (5 scenarios), and safety constraints |
| `assets/sync_map.template.json` | Template for sync map structure |
| `assets/rtdb_rules.template.json` | Template for Realtime Database rules |
| `assets/firestore_rules.template` | Template for Firestore security rules |

## Related Skills

- `firebase-config-generator` - Generate Firebase configuration from scratch
- `cloud-functions-creator` - Create Cloud Functions for specific use cases
- `security-audit` - General security audit for mobile apps
