---
name: firebase-project-scaffolding
description: "Scaffold a new Firebase project with production-grade defaults including auth-required security rules, cost budget alerts, App Check configuration, Emulator Suite setup, CI/CD pipeline for rules deployment, and multi-environment support. Use this skill when creating a new Firebase project, initializing Firebase in an Android app, setting up Firebase infrastructure from scratch, or when a developer mentions 'new Firebase project', 'Firebase init', 'Firebase setup', or 'production Firebase config'."
metadata:
  tags:
    - firebase
    - scaffolding
    - setup
    - solo-developer
    - android
  updated: "2026-02-12"
---

# Firebase Project Scaffolding

Scaffold a new Firebase project with production-grade defaults. Takes a developer from zero to a secure, cost-monitored, multi-environment Firebase setup — avoiding the common pitfall of starting with open security rules and no cost protection that leads to security incidents and surprise bills.

## Purpose

Most Firebase projects start with the default configuration that is intentionally permissive for development convenience — open security rules, no cost alerts, no App Check, single environment. This skill creates a production-ready Firebase foundation from the start. It takes more setup time upfront but prevents the security incidents ($70K+ breaches documented), surprise bills, and "it works on my machine" problems that plague Firebase projects launched without proper infrastructure.

## When to Use This Skill

Use this skill when you need to:
- Create a new Firebase project for a production Android app
- Set up Firebase infrastructure for the first time
- Replace an insecure Firebase setup with production-grade configuration
- Create development/staging/production environment separation
- Set up CI/CD for Firebase security rules and Cloud Functions

## When NOT to Use This Skill

Do NOT use this skill when:
- You need to migrate between Firebase projects (use migration guides)
- You already have a production Firebase setup and need to audit it (use firebase-security-auditor)
- You need to optimize Firebase costs on an existing project (use firebase-cost-analyst)
- You are using Firebase only for Analytics/Crashlytics (no backend services — simpler setup)

## Prerequisites

- Google account
- `firebase` CLI installed (`npm install -g firebase-tools`)
- `gcloud` CLI installed (for GCP budget alerts)
- Android project ready for Firebase SDK integration
- A domain you control (for App Check and App Links, optional but recommended)

## Step 1: Create Firebase Projects (Multi-Environment)

### 1.1 Project Creation

Create three projects for environment isolation:

```bash
# Development project
firebase projects:create yourapp-dev --display-name "YourApp (Dev)"

# Staging project
firebase projects:create yourapp-staging --display-name "YourApp (Staging)"

# Production project
firebase projects:create yourapp-prod --display-name "YourApp (Production)"
```

### 1.2 Enable Billing (Blaze Plan)

Each project needs the Blaze (pay-as-you-go) plan for Cloud Functions and extensions:

```bash
# Link to billing account (do this in Firebase Console)
# Console → Project Settings → Billing → Upgrade to Blaze
# IMPORTANT: Set budget alerts BEFORE enabling Blaze (Step 2)
```

### 1.3 Directory Structure

```
firebase/
├── .firebaserc                    # Project aliases (dev/staging/prod)
├── firebase.json                  # Firebase configuration
├── firestore.rules               # Firestore security rules
├── firestore.indexes.json        # Firestore composite indexes
├── storage.rules                 # Cloud Storage security rules
├── remoteconfig.template.json    # Remote Config template
├── functions/                     # Cloud Functions
│   ├── src/
│   ├── package.json
│   └── tsconfig.json
├── emulators/                     # Emulator data
│   └── seed-data/                # Import data for development
└── .github/
    └── workflows/
        └── firebase-deploy.yml   # CI/CD for rules and functions
```

### 1.4 Project Aliases

```json
// .firebaserc
{
  "projects": {
    "dev": "yourapp-dev",
    "staging": "yourapp-staging",
    "prod": "yourapp-prod"
  }
}
```

## Step 2: Budget Alerts (Before Anything Else)

Set up budget alerts BEFORE enabling services:

```bash
# Using gcloud CLI for each project
for PROJECT in yourapp-dev yourapp-staging yourapp-prod; do
  gcloud billing budgets create \
    --billing-account=YOUR_BILLING_ACCOUNT_ID \
    --display-name="${PROJECT} Budget Alert" \
    --budget-amount=50.00 \
    --threshold-rule=percent=0.01 \
    --threshold-rule=percent=0.05 \
    --threshold-rule=percent=0.50 \
    --threshold-rule=percent=1.0 \
    --threshold-rule=percent=1.5 \
    --all-updates-rule-monitoring-notification-channels=YOUR_CHANNEL_ID \
    --filter-projects=projects/${PROJECT} \
    --project=${PROJECT}
done
```

Budget alert thresholds:
- **1% ($0.50):** Confirms billing is working — should trigger quickly
- **5% ($2.50):** Normal development usage
- **50% ($25):** Investigation needed
- **100% ($50):** Action required — review usage immediately
- **150% ($75):** Emergency — consider disabling services

## Step 3: Security Rules (Locked by Default)

### 3.1 Firestore Rules

```
// firestore.rules
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // DEFAULT: Deny all access
    match /{document=**} {
      allow read, write: if false;
    }

    // Users collection: Users can only access their own data
    match /users/{userId} {
      allow read: if request.auth != null && request.auth.uid == userId;
      allow create: if request.auth != null && request.auth.uid == userId
                    && request.resource.data.keys().hasAll(['displayName', 'email', 'createdAt'])
                    && request.resource.data.displayName is string
                    && request.resource.data.displayName.size() <= 100
                    && request.resource.data.createdAt == request.time;
      allow update: if request.auth != null && request.auth.uid == userId
                    && !request.resource.data.diff(resource.data).affectedKeys().hasAny(['createdAt', 'uid']);
      allow delete: if false; // Soft-delete via Cloud Function

      // User's private subcollections
      match /settings/{settingId} {
        allow read, write: if request.auth != null && request.auth.uid == userId;
      }
    }

    // Public content: Anyone authenticated can read, only owner can write
    match /items/{itemId} {
      allow read: if request.auth != null;
      allow create: if request.auth != null
                    && request.resource.data.ownerId == request.auth.uid
                    && request.resource.data.createdAt == request.time
                    && request.resource.data.size() < 500000; // 500KB limit
      allow update: if request.auth != null
                    && resource.data.ownerId == request.auth.uid
                    && !request.resource.data.diff(resource.data).affectedKeys().hasAny(['ownerId', 'createdAt']);
      allow delete: if request.auth != null
                    && resource.data.ownerId == request.auth.uid;
    }

    // Admin-only collection (managed via Cloud Functions)
    match /admin/{document=**} {
      allow read, write: if false; // Only accessible via Admin SDK in Cloud Functions
    }
  }
}
```

### 3.2 Storage Rules

```
// storage.rules
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    // Default: deny all
    match /{allPaths=**} {
      allow read, write: if false;
    }

    // User profile images: owner only, image files only, max 5MB
    match /users/{userId}/profile/{fileName} {
      allow read: if request.auth != null;
      allow write: if request.auth != null
                   && request.auth.uid == userId
                   && request.resource.contentType.matches('image/.*')
                   && request.resource.size < 5 * 1024 * 1024;
    }

    // User uploads: owner only, max 20MB
    match /users/{userId}/uploads/{fileName} {
      allow read: if request.auth != null && request.auth.uid == userId;
      allow write: if request.auth != null
                   && request.auth.uid == userId
                   && request.resource.size < 20 * 1024 * 1024;
    }
  }
}
```

## Step 4: App Check Configuration

```bash
# Enable App Check for each project
firebase appcheck:enable --project yourapp-prod

# Register Android app with Play Integrity provider
# (Done in Firebase Console → App Check → Register)
# Select: Play Integrity for production, Debug for development
```

In your Android app:
```kotlin
// Application.onCreate()
FirebaseAppCheck.getInstance().installAppCheckProviderFactory(
    if (BuildConfig.DEBUG) {
        DebugAppCheckProviderFactory.getInstance()
    } else {
        PlayIntegrityAppCheckProviderFactory.getInstance()
    }
)
```

## Step 5: Emulator Suite Setup

```json
// firebase.json
{
  "emulators": {
    "auth": { "port": 9099 },
    "firestore": { "port": 8080 },
    "functions": { "port": 5001 },
    "storage": { "port": 9199 },
    "ui": { "enabled": true, "port": 4000 },
    "pubsub": { "port": 8085 }
  },
  "firestore": {
    "rules": "firestore.rules",
    "indexes": "firestore.indexes.json"
  },
  "storage": {
    "rules": "storage.rules"
  },
  "functions": {
    "source": "functions"
  }
}
```

```bash
# Start emulators with seed data
firebase emulators:start --import=emulators/seed-data

# Export data after making changes (for re-import later)
firebase emulators:export emulators/seed-data
```

## Step 6: CI/CD Pipeline

```yaml
# .github/workflows/firebase-deploy.yml
name: Deploy Firebase
on:
  push:
    branches: [main]
    paths:
      - 'firestore.rules'
      - 'storage.rules'
      - 'functions/**'
      - 'firestore.indexes.json'

jobs:
  test-rules:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm install -g firebase-tools
      - run: firebase emulators:exec --only firestore "npm test" --project yourapp-dev

  deploy-staging:
    needs: test-rules
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm install -g firebase-tools
      - run: cd functions && npm ci
      - run: firebase deploy --only firestore:rules,storage:rules,functions --project yourapp-staging
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production  # Requires manual approval
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm install -g firebase-tools
      - run: cd functions && npm ci
      - run: firebase deploy --only firestore:rules,storage:rules,functions --project yourapp-prod
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}
```

## Step 7: Android Integration

```kotlin
// app/build.gradle.kts — use flavor-specific google-services.json
android {
    flavorDimensions += "environment"
    productFlavors {
        create("dev") {
            dimension = "environment"
            applicationIdSuffix = ".dev"
        }
        create("staging") {
            dimension = "environment"
            applicationIdSuffix = ".staging"
        }
        create("prod") {
            dimension = "environment"
        }
    }
}

// Place google-services.json per flavor:
// app/src/dev/google-services.json     → yourapp-dev project
// app/src/staging/google-services.json → yourapp-staging project
// app/src/prod/google-services.json    → yourapp-prod project
```

## Scaffolding Completion Checklist

- [ ] Three Firebase projects created (dev, staging, prod)
- [ ] Budget alerts configured on all projects (before enabling Blaze)
- [ ] Blaze plan enabled on all projects
- [ ] Firestore security rules: deny-by-default with auth-required access
- [ ] Storage security rules: deny-by-default with file type and size limits
- [ ] App Check configured with Play Integrity (prod) and Debug (dev)
- [ ] Emulator Suite configured for local development
- [ ] Seed data created for local development
- [ ] CI/CD pipeline deploys rules and functions with staging gate
- [ ] Android app configured with per-flavor google-services.json
- [ ] Production deploy requires manual approval

## Related Skills

- `firebase-rules-testing` - Automated testing for the security rules created here
- `android-quarterly-maintenance` - Quarterly review of the Firebase setup
