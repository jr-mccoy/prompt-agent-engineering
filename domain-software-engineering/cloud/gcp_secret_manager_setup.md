---
title: "GCP Secret Manager Setup for API Keys and Credentials"
category: cloud-infrastructure
description: "Implement GCP Secret Manager to replace hardcoded API keys and credentials, covering Cloud Functions integration, Kotlin/Android access patterns, secret rotation strategy, IAM access control, audit logging, and versioning for solo developers."
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
  - secret-manager
  - security
  - api-keys
  - credentials
  - iam
  - cloud-functions
  - kotlin
  - android
  - solo-developer
updated: "2026-02-11"
---

# GCP Secret Manager Setup for API Keys and Credentials

**Objective:** Migrate all hardcoded API keys, database credentials, third-party tokens, and sensitive configuration values into GCP Secret Manager. This guide covers the complete lifecycle: inventorying your existing secrets, migrating them out of source code and environment variables, accessing them securely from Cloud Functions and Kotlin/Android code, setting up automatic rotation, configuring IAM for least-privilege access, and enabling audit logging so you know exactly who accessed what and when.

**When to Use:** Use this prompt the moment you realize you have an API key committed to Git, a password in a `.env` file that gets copied between machines, a credential stored in plain text in Firebase Remote Config, or any secret that would be a problem if someone saw it. Also use it when you are preparing to open-source a repository, onboarding a contractor, or passing a security review. Solo developers often defer secret management because "only I have access" -- until they accidentally push to a public repo, lose a laptop, or need to rotate a compromised key at 2 AM.

---

## Context Gathering

Before migrating to Secret Manager, gather the following:

1. **Current Secret Inventory**
   - What API keys do you have? (Stripe, SendGrid, OpenAI, Maps, etc.)
   - Where are they stored now? (Source code, `.env` files, Firebase Remote Config, Cloud Function env vars)
   - Which services use which secrets?
   - Do any secrets have expiration dates or rotation requirements?

2. **Architecture Details**
   - What GCP services need access to secrets? (Cloud Functions, Cloud Run, App Engine)
   - Do you have a CI/CD pipeline that needs secrets? (GitHub Actions, Cloud Build)
   - Does your Android app need any secrets directly? (API keys for Maps, analytics)
   - What environments do you have? (dev, staging, production)

3. **Access Patterns**
   - How often are secrets read? (Every function invocation, once at startup, on-demand)
   - Do you need secrets in multiple regions?
   - Who else might need access? (Contractors, co-founders, CI/CD service accounts)

4. **Compliance Needs**
   - Do you need audit trails for secret access? (SOC 2, HIPAA, PCI)
   - Do any secrets require automatic rotation? (Database passwords, API keys with expiry)
   - Are there secrets that must never leave a specific environment?

---

## Instructions

### CRITICAL: Verification Requirements

Before migrating secrets, verify these requirements:

1. **Secret Manager API is enabled** in your GCP project (`secretmanager.googleapis.com`)
2. **Your service account has the `roles/secretmanager.secretAccessor` role** for reading secrets
3. **Your admin account has `roles/secretmanager.admin`** for creating and managing secrets
4. **You have tested secret access** from your local development environment before deploying
5. **You have a backup of all current secrets** before migrating (store temporarily in a password manager, not a file)
6. **Your application handles missing secrets gracefully** with clear error messages rather than silent failures
7. **Acceptable null result:** If a secret version is in the DISABLED state, accessing it returns an error. This is expected behavior, not a bug -- it means someone intentionally disabled that version.

### False-Positive Prevention

- **DO NOT** store secrets in your Android app's `BuildConfig` or `local.properties` and think they are safe. APKs can be decompiled and every string literal extracted in seconds.
- **DO NOT** use Firebase Remote Config for actual secrets. Remote Config values are fetched over HTTPS but are readable by anyone with the Firebase config object (which is in your app's source).
- **DO NOT** create one giant secret with all your keys in a JSON blob. Use individual secrets so you can rotate, version, and audit them independently.
- **DO NOT** give `roles/secretmanager.admin` to service accounts that only need to read secrets. Admin can delete secrets.
- **DO NOT** log secret values. Ever. Not even in debug mode. Log the secret name and version, never the payload.
- **DO** use the latest version alias (`latest`) during development but pin specific versions in production for predictability.
- **DO** test secret rotation in a development environment before enabling it in production.
- **DO** set up secret expiration notifications before the secret actually expires and breaks your production service.

---

### Phase 1: Secret Inventory

Before migrating anything, you need a complete picture of what secrets exist and where they live.

#### Step 1: Audit Your Codebase

```bash
# Search for common secret patterns in your codebase
# Run these from your project root

# API keys (look for common patterns)
grep -rn "api[_-]key\|apikey\|API_KEY" --include="*.ts" --include="*.js" --include="*.kt" --include="*.java" --include="*.py" --include="*.env*" .

# Passwords and tokens
grep -rn "password\|passwd\|secret\|token\|credential" --include="*.ts" --include="*.js" --include="*.kt" --include="*.env*" .

# Hardcoded strings that look like keys (long alphanumeric strings)
grep -rn "sk_live_\|pk_live_\|sk_test_\|AIza\|ghp_\|AKIA\|xox[bpas]-" --include="*.ts" --include="*.js" --include="*.kt" --include="*.env*" .

# Check Firebase config files
grep -rn "apiKey\|authDomain\|databaseURL\|storageBucket" --include="*.json" --include="*.ts" .

# Check environment variable references
grep -rn "process\.env\.\|System\.getenv\|os\.environ" --include="*.ts" --include="*.js" --include="*.kt" --include="*.py" .

# Check .gitignore to see what is already excluded
cat .gitignore | grep -i "env\|secret\|key\|credential"
```

#### Step 2: Classify Your Secrets

Create a secret inventory (this table is your migration checklist):

```markdown
| Secret Name | Current Location | Service Using It | Rotation Needed | Priority |
|-------------|-----------------|-------------------|-----------------|----------|
| STRIPE_SECRET_KEY | .env file | Cloud Functions | Every 90 days | HIGH |
| STRIPE_WEBHOOK_SECRET | .env file | Cloud Functions | On compromise | HIGH |
| OPENAI_API_KEY | Cloud Function env var | Cloud Functions | On compromise | HIGH |
| SENDGRID_API_KEY | hardcoded in code | Cloud Functions | On compromise | CRITICAL |
| DATABASE_URL | .env file | Cloud Run | On password change | HIGH |
| MAPS_API_KEY | AndroidManifest.xml | Android app | Rotate yearly | MEDIUM |
| FIREBASE_ADMIN_KEY | sa-key.json | Local development | N/A (use ADC) | MEDIUM |
| SLACK_WEBHOOK_URL | Cloud Function env var | Cloud Functions | On compromise | LOW |
```

**Priority classification:**
- **CRITICAL:** Secret is hardcoded in source code that is or could be committed to Git
- **HIGH:** Secret is in `.env` files or Cloud Function environment variables with no rotation strategy
- **MEDIUM:** Secret is somewhat protected but not in Secret Manager
- **LOW:** Secret exposure has limited blast radius (e.g., Slack webhook)

#### Step 3: Enable Secret Manager API

```bash
export PROJECT_ID="your-project-id"

# Enable the Secret Manager API
gcloud services enable secretmanager.googleapis.com \
  --project=$PROJECT_ID

# Verify it is enabled
gcloud services list --enabled --project=$PROJECT_ID \
  --filter="name:secretmanager.googleapis.com"
```

---

### Phase 2: Migration from Hardcoded Secrets

#### Step 1: Create Secrets in Secret Manager

```bash
# Create secrets one by one with descriptive names
# Convention: SERVICE_PURPOSE (e.g., stripe_secret_key, openai_api_key)

# Create the secret (the container)
gcloud secrets create stripe-secret-key \
  --replication-policy="automatic" \
  --labels="service=stripe,environment=production,owner=backend" \
  --project=$PROJECT_ID

# Add the secret value (the actual key)
echo -n "sk_live_your_actual_stripe_key_here" | \
  gcloud secrets versions add stripe-secret-key \
  --data-file=- \
  --project=$PROJECT_ID

# Repeat for each secret
gcloud secrets create openai-api-key \
  --replication-policy="automatic" \
  --labels="service=openai,environment=production,owner=backend" \
  --project=$PROJECT_ID

echo -n "sk-your_actual_openai_key_here" | \
  gcloud secrets versions add openai-api-key \
  --data-file=- \
  --project=$PROJECT_ID

gcloud secrets create sendgrid-api-key \
  --replication-policy="automatic" \
  --labels="service=sendgrid,environment=production,owner=backend" \
  --project=$PROJECT_ID

echo -n "SG.your_actual_sendgrid_key_here" | \
  gcloud secrets versions add sendgrid-api-key \
  --data-file=- \
  --project=$PROJECT_ID

gcloud secrets create stripe-webhook-secret \
  --replication-policy="automatic" \
  --labels="service=stripe,environment=production,owner=backend" \
  --project=$PROJECT_ID

echo -n "whsec_your_webhook_secret_here" | \
  gcloud secrets versions add stripe-webhook-secret \
  --data-file=- \
  --project=$PROJECT_ID
```

#### Step 2: Verify Secrets Were Created

```bash
# List all secrets
gcloud secrets list --project=$PROJECT_ID

# Check a specific secret's metadata (does NOT show the value)
gcloud secrets describe stripe-secret-key --project=$PROJECT_ID

# List versions of a secret
gcloud secrets versions list stripe-secret-key --project=$PROJECT_ID

# Verify you can read the secret value (do this once for verification, then delete from terminal history)
gcloud secrets versions access latest \
  --secret=stripe-secret-key \
  --project=$PROJECT_ID
```

#### Step 3: Batch Migration Script

For migrating many secrets at once from a `.env` file:

```bash
#!/bin/bash
# migrate-env-to-secret-manager.sh
# Reads a .env file and creates secrets in Secret Manager
# Usage: ./migrate-env-to-secret-manager.sh .env production

ENV_FILE=$1
ENVIRONMENT=${2:-production}
PROJECT_ID="your-project-id"

if [ ! -f "$ENV_FILE" ]; then
  echo "Error: File $ENV_FILE not found"
  exit 1
fi

echo "Migrating secrets from $ENV_FILE to Secret Manager..."
echo "Environment: $ENVIRONMENT"
echo "Project: $PROJECT_ID"
echo ""

while IFS='=' read -r key value; do
  # Skip comments and empty lines
  [[ "$key" =~ ^#.*$ ]] && continue
  [[ -z "$key" ]] && continue

  # Convert KEY_NAME to key-name for Secret Manager naming
  secret_name=$(echo "$key" | tr '[:upper:]_' '[:lower:]-')

  echo "Creating secret: $secret_name"

  # Create the secret (ignore error if it already exists)
  gcloud secrets create "$secret_name" \
    --replication-policy="automatic" \
    --labels="environment=$ENVIRONMENT,migrated=true" \
    --project=$PROJECT_ID 2>/dev/null

  # Add the version
  echo -n "$value" | gcloud secrets versions add "$secret_name" \
    --data-file=- \
    --project=$PROJECT_ID

  echo "  -> Created version 1 for $secret_name"
done < "$ENV_FILE"

echo ""
echo "Migration complete. Verify with: gcloud secrets list --project=$PROJECT_ID"
echo "IMPORTANT: Delete the .env file and clear your terminal history."
```

---

### Phase 3: Cloud Functions Integration

#### TypeScript: Accessing Secrets in Cloud Functions

```typescript
// functions/src/config/secrets.ts
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';

const client = new SecretManagerServiceClient();
const projectId = process.env.GCP_PROJECT || process.env.GCLOUD_PROJECT || '';

// Cache secrets in memory to avoid repeated API calls
const secretCache = new Map<string, { value: string; expiry: number }>();
const CACHE_TTL_MS = 5 * 60 * 1000; // 5 minutes

/**
 * Retrieve a secret from Secret Manager with caching.
 * Secrets are cached in memory for 5 minutes to reduce API calls and latency.
 */
export async function getSecret(secretName: string, version: string = 'latest'): Promise<string> {
  const cacheKey = `${secretName}:${version}`;

  // Check cache first
  const cached = secretCache.get(cacheKey);
  if (cached && cached.expiry > Date.now()) {
    return cached.value;
  }

  // Fetch from Secret Manager
  const name = `projects/${projectId}/secrets/${secretName}/versions/${version}`;

  try {
    const [response] = await client.accessSecretVersion({ name });
    const payload = response.payload?.data;

    if (!payload) {
      throw new Error(`Secret ${secretName} version ${version} has no payload`);
    }

    const value = typeof payload === 'string' ? payload : payload.toString('utf8');

    // Cache the result
    secretCache.set(cacheKey, {
      value,
      expiry: Date.now() + CACHE_TTL_MS,
    });

    return value;
  } catch (error: any) {
    // Provide clear error messages for common issues
    if (error.code === 5) { // NOT_FOUND
      throw new Error(
        `Secret "${secretName}" not found in project "${projectId}". ` +
        `Verify the secret exists: gcloud secrets list --project=${projectId}`
      );
    }
    if (error.code === 7) { // PERMISSION_DENIED
      throw new Error(
        `Permission denied accessing secret "${secretName}". ` +
        `Grant roles/secretmanager.secretAccessor to the Cloud Functions service account.`
      );
    }
    throw error;
  }
}

/**
 * Pre-load multiple secrets at once during function cold start.
 * Call this in your function initialization to warm the cache.
 */
export async function preloadSecrets(secretNames: string[]): Promise<void> {
  await Promise.all(secretNames.map(name => getSecret(name)));
}

/**
 * Clear the secret cache. Call this after rotation or when you need fresh values.
 */
export function clearSecretCache(): void {
  secretCache.clear();
}
```

```typescript
// functions/src/index.ts
import { onRequest } from 'firebase-functions/v2/https';
import { onDocumentCreated } from 'firebase-functions/v2/firestore';
import { getSecret, preloadSecrets } from './config/secrets';
import Stripe from 'stripe';

// Option A: Cloud Functions v2 native secret binding (recommended)
// Secrets are mounted as environment variables automatically
export const processPayment = onRequest(
  {
    region: 'us-central1',
    memory: '256MiB',
    // Bind secrets directly -- Cloud Functions reads them at cold start
    secrets: ['stripe-secret-key', 'stripe-webhook-secret'],
  },
  async (req, res) => {
    // Access via environment variable (name is uppercased with hyphens to underscores)
    const stripeKey = process.env.STRIPE_SECRET_KEY;
    if (!stripeKey) {
      res.status(500).json({ error: 'Payment service configuration error' });
      return;
    }

    const stripe = new Stripe(stripeKey, { apiVersion: '2024-12-18.acacia' });
    // ... process payment
    res.json({ status: 'ok' });
  }
);

// Option B: Programmatic access with the Secret Manager client
// Use this when you need dynamic secret selection or custom caching
export const sendEmail = onRequest(
  { region: 'us-central1', memory: '256MiB' },
  async (req, res) => {
    const sendgridKey = await getSecret('sendgrid-api-key');

    // Use the secret
    const sgMail = require('@sendgrid/mail');
    sgMail.setApiKey(sendgridKey);
    // ... send email
    res.json({ status: 'sent' });
  }
);

// Option C: Preload secrets at cold start for Firestore triggers
let openaiKey: string | null = null;

export const onUserCreated = onDocumentCreated(
  'users/{userId}',
  async (event) => {
    // Lazy initialization: load secret on first invocation
    if (!openaiKey) {
      openaiKey = await getSecret('openai-api-key');
    }

    // Use the secret for AI-powered welcome message
    // ...
  }
);
```

#### Cloud Functions v2 Secret Binding (Recommended Approach)

```bash
# Deploy a Cloud Function with secret bindings
# The secret is automatically available as an environment variable

gcloud functions deploy processPayment \
  --gen2 \
  --runtime=nodejs20 \
  --trigger-http \
  --allow-unauthenticated \
  --region=us-central1 \
  --memory=256MB \
  --set-secrets="STRIPE_SECRET_KEY=stripe-secret-key:latest,STRIPE_WEBHOOK_SECRET=stripe-webhook-secret:latest" \
  --project=$PROJECT_ID

# Format: ENV_VAR_NAME=secret-name:version
# version can be: latest, 1, 2, etc.
# The function's service account needs secretmanager.secretAccessor role
```

#### Cloud Run Secret Integration

```bash
# For Cloud Run services, mount secrets as environment variables or files

# As environment variables:
gcloud run deploy my-backend \
  --image=$REGION-docker.pkg.dev/$PROJECT_ID/images/my-backend:latest \
  --region=us-central1 \
  --set-secrets="STRIPE_KEY=stripe-secret-key:latest,DB_PASSWORD=database-password:latest" \
  --project=$PROJECT_ID

# As mounted files (useful for certificate files, JSON credentials):
gcloud run deploy my-backend \
  --image=$REGION-docker.pkg.dev/$PROJECT_ID/images/my-backend:latest \
  --region=us-central1 \
  --set-secrets="/secrets/tls/cert.pem=tls-certificate:latest,/secrets/tls/key.pem=tls-private-key:latest" \
  --project=$PROJECT_ID
```

---

### Phase 4: Kotlin/Android Access Patterns

Android apps should never contain production secrets directly. Instead, use these patterns:

#### Pattern 1: Proxy Through Cloud Functions (Recommended)

```kotlin
// The Android app never sees the third-party API key.
// It calls your Cloud Function, which holds the secret.

// In your Android app:
class AiService(private val functions: FirebaseFunctions) {

    /**
     * Call your Cloud Function which has the OpenAI key in Secret Manager.
     * The Android app only needs the Firebase project config (which is public).
     */
    suspend fun generateSuggestion(prompt: String): String {
        val data = hashMapOf(
            "prompt" to prompt,
            "maxTokens" to 500
        )

        return try {
            val result = functions
                .getHttpsCallable("generateAiSuggestion")
                .call(data)
                .await()

            val response = result.data as Map<*, *>
            response["suggestion"] as String
        } catch (e: FirebaseFunctionsException) {
            when (e.code) {
                FirebaseFunctionsException.Code.UNAUTHENTICATED ->
                    throw IllegalStateException("User must be signed in")
                FirebaseFunctionsException.Code.RESOURCE_EXHAUSTED ->
                    throw IllegalStateException("Rate limit exceeded, try again later")
                else -> throw e
            }
        }
    }
}

// In your Cloud Function (TypeScript):
// The OpenAI key lives in Secret Manager, never touches the Android app
```

```typescript
// functions/src/ai-proxy.ts
import { onCall, HttpsError } from 'firebase-functions/v2/https';
import { getSecret } from './config/secrets';

export const generateAiSuggestion = onCall(
  {
    region: 'us-central1',
    memory: '256MiB',
    // Rate limiting: max 10 calls per user per minute
    enforceAppCheck: true,  // Verify requests come from your real app
  },
  async (request) => {
    // Verify the user is authenticated
    if (!request.auth) {
      throw new HttpsError('unauthenticated', 'User must be signed in');
    }

    const { prompt, maxTokens } = request.data;

    // Get the secret -- your Android app never sees this key
    const openaiKey = await getSecret('openai-api-key');

    // Call OpenAI
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${openaiKey}`,
      },
      body: JSON.stringify({
        model: 'gpt-4o-mini',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: maxTokens || 500,
      }),
    });

    const data = await response.json();
    return { suggestion: data.choices[0].message.content };
  }
);
```

#### Pattern 2: Build-Time Restricted API Keys for Android

Some API keys must be in the Android app (Google Maps, Firebase config). For these, use API key restrictions:

```kotlin
// In your Android app's build.gradle.kts:
android {
    defaultConfig {
        // These keys are restricted by API, package name, and SHA-1 fingerprint
        // They are NOT truly secret -- they are restricted to be useless outside your app
        buildConfigField("String", "MAPS_API_KEY",
            "\"${project.findProperty("MAPS_API_KEY") ?: ""}\"")
    }
}
```

```bash
# Restrict the Maps API key in GCP Console so even if extracted, it is useless:
# GCP Console → APIs & Services → Credentials → [Your API Key]
#
# Application restrictions:
#   → Android apps
#   → Add your package name + SHA-1 fingerprint
#
# API restrictions:
#   → Restrict key
#   → Select only: Maps SDK for Android
#
# This means even if someone extracts the key from your APK,
# it only works from your specific app package with your signing key.

# Get your app's SHA-1 fingerprint:
keytool -list -v -keystore ~/.android/debug.keystore -alias androiddebugkey \
  -storepass android

# For release keystore:
keytool -list -v -keystore your-release.keystore -alias your-alias
```

#### Pattern 3: Server-Side Secret Access from Kotlin Backend

If you have a Kotlin backend (Ktor, Spring Boot) running on Cloud Run:

```kotlin
// build.gradle.kts
dependencies {
    implementation("com.google.cloud:google-cloud-secretmanager:2.31.0")
}

// src/main/kotlin/config/SecretManager.kt
import com.google.cloud.secretmanager.v1.SecretManagerServiceClient
import com.google.cloud.secretmanager.v1.SecretVersionName
import java.util.concurrent.ConcurrentHashMap

object SecretManager {
    private val client: SecretManagerServiceClient by lazy {
        SecretManagerServiceClient.create()
    }

    private val cache = ConcurrentHashMap<String, CachedSecret>()

    private data class CachedSecret(
        val value: String,
        val expiry: Long
    )

    private const val CACHE_TTL_MS = 5 * 60 * 1000L // 5 minutes

    /**
     * Access a secret from GCP Secret Manager with in-memory caching.
     */
    fun getSecret(
        projectId: String,
        secretId: String,
        version: String = "latest"
    ): String {
        val cacheKey = "$secretId:$version"
        val cached = cache[cacheKey]

        if (cached != null && cached.expiry > System.currentTimeMillis()) {
            return cached.value
        }

        val secretVersionName = SecretVersionName.of(projectId, secretId, version)
        val response = client.accessSecretVersion(secretVersionName)
        val value = response.payload.data.toStringUtf8()

        cache[cacheKey] = CachedSecret(
            value = value,
            expiry = System.currentTimeMillis() + CACHE_TTL_MS
        )

        return value
    }

    /**
     * Close the client when the application shuts down.
     */
    fun close() {
        client.close()
    }
}

// Usage in a Ktor route:
// val stripeKey = SecretManager.getSecret(projectId, "stripe-secret-key")
```

---

### Phase 5: Rotation Strategy

Secret rotation is the practice of periodically changing secret values so that a compromised key has a limited window of usefulness.

#### Rotation Workflow

```
Secret Rotation Lifecycle:
│
├── 1. CREATE new secret version
│   └── gcloud secrets versions add my-secret --data-file=-
│
├── 2. DEPLOY services with new version
│   └── Services start using the new version
│
├── 3. VERIFY new version works
│   └── Monitor for errors, test endpoints
│
├── 4. DISABLE old version
│   └── gcloud secrets versions disable my-secret --version=1
│
└── 5. DESTROY old version (after grace period)
    └── gcloud secrets versions destroy my-secret --version=1
```

#### Automated Rotation with Cloud Functions

```typescript
// functions/src/secret-rotation.ts
import { onSchedule } from 'firebase-functions/v2/scheduler';
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';

const client = new SecretManagerServiceClient();
const projectId = process.env.GCP_PROJECT || '';

/**
 * Check for secrets approaching expiration and send alerts.
 * Runs weekly. Actual rotation is manual for solo devs (safer).
 */
export const checkSecretExpiration = onSchedule(
  {
    schedule: 'every monday 09:00',
    timeZone: 'America/New_York',
    region: 'us-central1',
    memory: '256MiB',
  },
  async () => {
    // List all secrets
    const [secrets] = await client.listSecrets({
      parent: `projects/${projectId}`,
    });

    const alerts: string[] = [];

    for (const secret of secrets) {
      const secretName = secret.name || '';
      const labels = secret.labels || {};

      // Check if secret has a rotation_days label
      const rotationDays = parseInt(labels['rotation_days'] || '0', 10);
      if (rotationDays === 0) continue;

      // Get the latest version
      const [versions] = await client.listSecretVersions({
        parent: secretName,
        filter: 'state:ENABLED',
      });

      if (versions.length === 0) continue;

      const latestVersion = versions[0];
      const createTime = latestVersion.createTime;
      if (!createTime) continue;

      const createdAt = new Date(
        Number(createTime.seconds) * 1000
      );
      const daysSinceCreation = Math.floor(
        (Date.now() - createdAt.getTime()) / (1000 * 60 * 60 * 24)
      );

      if (daysSinceCreation > rotationDays * 0.8) {
        const shortName = secretName.split('/').pop();
        alerts.push(
          `Secret "${shortName}" is ${daysSinceCreation} days old ` +
          `(rotation policy: ${rotationDays} days). ` +
          `${daysSinceCreation >= rotationDays ? 'OVERDUE' : 'Due soon'}.`
        );
      }
    }

    if (alerts.length > 0) {
      const message = `Secret Rotation Alert:\n\n${alerts.join('\n')}`;
      console.warn(message);

      // Send notification (Slack, email, etc.)
      const webhookUrl = process.env.SLACK_WEBHOOK_URL;
      if (webhookUrl) {
        await fetch(webhookUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text: message }),
        });
      }
    } else {
      console.log('All secrets are within their rotation windows.');
    }
  }
);
```

#### Manual Rotation Commands

```bash
# Step 1: Generate or obtain the new secret value from the provider
# (e.g., generate a new Stripe API key in Stripe dashboard)

# Step 2: Add the new value as a new version
echo -n "sk_live_NEW_stripe_key_here" | \
  gcloud secrets versions add stripe-secret-key \
  --data-file=- \
  --project=$PROJECT_ID

# Step 3: Verify the new version was created
gcloud secrets versions list stripe-secret-key --project=$PROJECT_ID

# Output:
# NAME  STATE    CREATED              DESTROYED
# 2     enabled  2026-02-11T10:00:00  -
# 1     enabled  2026-01-01T10:00:00  -

# Step 4: Redeploy services that use this secret
# If using Cloud Functions v2 secret binding with "latest", just redeploy:
gcloud functions deploy processPayment \
  --gen2 \
  --runtime=nodejs20 \
  --trigger-http \
  --region=us-central1 \
  --set-secrets="STRIPE_SECRET_KEY=stripe-secret-key:latest" \
  --project=$PROJECT_ID

# Step 5: Verify the new key works (test a payment, check logs)

# Step 6: Disable the old version (after confirming new one works)
gcloud secrets versions disable stripe-secret-key \
  --version=1 \
  --project=$PROJECT_ID

# Step 7: After 30 days grace period, destroy the old version
gcloud secrets versions destroy stripe-secret-key \
  --version=1 \
  --project=$PROJECT_ID
```

#### Setting Rotation Labels for Tracking

```bash
# Add rotation policy labels to your secrets
gcloud secrets update stripe-secret-key \
  --update-labels="rotation_days=90,last_rotated=2026-02-11,owner=you@email.com" \
  --project=$PROJECT_ID

gcloud secrets update openai-api-key \
  --update-labels="rotation_days=180,last_rotated=2026-02-11,owner=you@email.com" \
  --project=$PROJECT_ID

gcloud secrets update sendgrid-api-key \
  --update-labels="rotation_days=365,last_rotated=2026-02-11,owner=you@email.com" \
  --project=$PROJECT_ID
```

---

### Phase 6: IAM Access Control

#### Principle of Least Privilege

```bash
# Secret Manager IAM Roles:
#
# roles/secretmanager.admin
#   Can: create, delete, update secrets and versions, manage IAM
#   Who: Your personal admin account only
#
# roles/secretmanager.secretAccessor
#   Can: Read secret values (versions)
#   Who: Service accounts that need to read secrets
#
# roles/secretmanager.secretVersionManager
#   Can: Create new versions, disable/enable/destroy versions
#   Who: CI/CD service account (for automated rotation)
#
# roles/secretmanager.viewer
#   Can: List secrets, see metadata (NOT values)
#   Who: Monitoring tools, audit systems

# Grant Cloud Functions service account read-only access
export CF_SA="$PROJECT_ID@appspot.gserviceaccount.com"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$CF_SA" \
  --role="roles/secretmanager.secretAccessor" \
  --condition=None

# For more granular control: grant access to specific secrets only
gcloud secrets add-iam-policy-binding stripe-secret-key \
  --member="serviceAccount:$CF_SA" \
  --role="roles/secretmanager.secretAccessor" \
  --project=$PROJECT_ID

gcloud secrets add-iam-policy-binding openai-api-key \
  --member="serviceAccount:$CF_SA" \
  --role="roles/secretmanager.secretAccessor" \
  --project=$PROJECT_ID

# Grant Cloud Run service account access to its specific secrets
export CR_SA="my-backend-sa@$PROJECT_ID.iam.gserviceaccount.com"

gcloud secrets add-iam-policy-binding database-password \
  --member="serviceAccount:$CR_SA" \
  --role="roles/secretmanager.secretAccessor" \
  --project=$PROJECT_ID

# Grant CI/CD service account version management (for rotation)
export CICD_SA="github-actions-sa@$PROJECT_ID.iam.gserviceaccount.com"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$CICD_SA" \
  --role="roles/secretmanager.secretVersionManager"
```

#### Per-Secret Access Control Matrix

```markdown
| Secret | Cloud Functions SA | Cloud Run SA | CI/CD SA | Admin |
|--------|-------------------|-------------|----------|-------|
| stripe-secret-key | READ | - | VERSION | FULL |
| stripe-webhook-secret | READ | - | VERSION | FULL |
| openai-api-key | READ | - | VERSION | FULL |
| sendgrid-api-key | READ | - | VERSION | FULL |
| database-password | - | READ | VERSION | FULL |
| tls-certificate | - | READ | VERSION | FULL |
| slack-webhook-url | READ | READ | - | FULL |
```

---

### Phase 7: Audit Logging and Monitoring

#### Enable Data Access Audit Logs

```bash
# Enable audit logging for Secret Manager
# This logs every time a secret is read, created, or modified

# Create an audit config JSON
cat > audit-config.json << 'EOF'
{
  "auditConfigs": [
    {
      "service": "secretmanager.googleapis.com",
      "auditLogConfigs": [
        { "logType": "ADMIN_READ" },
        { "logType": "ADMIN_WRITE" },
        { "logType": "DATA_READ" },
        { "logType": "DATA_WRITE" }
      ]
    }
  ]
}
EOF

# Apply the audit config
gcloud projects set-iam-policy $PROJECT_ID audit-config.json \
  --format=json > /dev/null

# Note: The above approach merges with existing IAM policy.
# Alternatively, enable via Console:
# IAM & Admin → Audit Logs → Secret Manager API → Enable all log types
```

#### View Secret Access Logs

```bash
# Query audit logs for secret access
gcloud logging read \
  'resource.type="audited_resource" AND
   protoPayload.serviceName="secretmanager.googleapis.com"' \
  --project=$PROJECT_ID \
  --limit=20 \
  --format="table(timestamp, protoPayload.methodName, protoPayload.authenticationInfo.principalEmail, protoPayload.resourceName)"

# Filter for a specific secret
gcloud logging read \
  'resource.type="audited_resource" AND
   protoPayload.serviceName="secretmanager.googleapis.com" AND
   protoPayload.resourceName:"stripe-secret-key"' \
  --project=$PROJECT_ID \
  --limit=10

# Filter for access by a specific service account
gcloud logging read \
  'resource.type="audited_resource" AND
   protoPayload.serviceName="secretmanager.googleapis.com" AND
   protoPayload.authenticationInfo.principalEmail="my-project@appspot.gserviceaccount.com"' \
  --project=$PROJECT_ID \
  --limit=10
```

#### Alert on Suspicious Secret Access

```bash
# Create a log-based alert for unusual secret access patterns
# This alerts you if someone accesses secrets outside normal service account patterns

gcloud logging metrics create suspicious-secret-access \
  --description="Secret access by non-service-account principals" \
  --log-filter='
    resource.type="audited_resource" AND
    protoPayload.serviceName="secretmanager.googleapis.com" AND
    protoPayload.methodName="google.cloud.secretmanager.v1.SecretManagerService.AccessSecretVersion" AND
    NOT protoPayload.authenticationInfo.principalEmail:("gserviceaccount.com")
  ' \
  --project=$PROJECT_ID

# Create an alerting policy based on this metric
# (See gcp_monitoring_alerting_setup.md for detailed alerting setup)
```

---

## Expected Output

After following this guide, your secret management system should look like this:

```markdown
## Secret Manager Implementation Summary

### Secret Inventory
| Secret Name | Service | Versions | Last Rotated | Rotation Policy | Access |
|-------------|---------|----------|-------------|-----------------|--------|
| stripe-secret-key | Stripe | 2 (v1 disabled) | 2026-02-11 | 90 days | CF SA |
| stripe-webhook-secret | Stripe | 1 | 2026-02-11 | On compromise | CF SA |
| openai-api-key | OpenAI | 1 | 2026-02-11 | 180 days | CF SA |
| sendgrid-api-key | SendGrid | 1 | 2026-02-11 | 365 days | CF SA |
| database-password | PostgreSQL | 1 | 2026-02-11 | 90 days | CR SA |
| slack-webhook-url | Slack | 1 | 2026-02-11 | On compromise | CF SA, CR SA |

### IAM Configuration
| Principal | Role | Scope |
|-----------|------|-------|
| you@gmail.com | secretmanager.admin | Project-wide |
| PROJECT_ID@appspot.gserviceaccount.com | secretmanager.secretAccessor | Per-secret |
| my-backend-sa@PROJECT_ID.iam.gserviceaccount.com | secretmanager.secretAccessor | Per-secret |
| github-actions-sa@PROJECT_ID.iam.gserviceaccount.com | secretmanager.secretVersionManager | Project-wide |

### Audit Logging
| Log Type | Status | Alert |
|----------|--------|-------|
| ADMIN_READ | Enabled | No |
| ADMIN_WRITE | Enabled | Yes (any change) |
| DATA_READ | Enabled | Yes (non-SA access) |
| DATA_WRITE | Enabled | Yes (any change) |

### Migration Status
| Source | Secrets Migrated | Status |
|--------|-----------------|--------|
| Hardcoded in source | 1 (SendGrid) | COMPLETE |
| .env files | 3 (Stripe, OpenAI, DB) | COMPLETE |
| Cloud Function env vars | 1 (Slack) | COMPLETE |
| Firebase Remote Config | 0 | N/A |

### Cost
| Metric | Value |
|--------|-------|
| Active secret versions | 7 |
| Free tier allowance | 6 active versions, 10K access ops |
| Monthly access operations | ~2,000 |
| Estimated monthly cost | $0.00 (within free tier) |
```

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defined the migration goal from hardcoded secrets to managed, rotatable, auditable secrets
- **ST-02 (Sequential Step-by-Step Instructions):** Phased approach from inventory through migration, integration, rotation, and audit
- **RT-02 (Multi-Dimensional Analysis):** Addressed secrets from Cloud Functions, Cloud Run, Android, and CI/CD perspectives
- **CM-01 (Contextual Framing):** All examples oriented toward a solo developer managing multiple services
- **DS-06 (Prioritization and Severity Guidance):** Priority classification (CRITICAL/HIGH/MEDIUM/LOW) for secret migration order
- **DS-02 (Metric Specification):** Concrete free tier limits, rotation periods, and cost thresholds
- **RT-05 (Evidence-Based Reasoning):** IAM role recommendations based on GCP security best practices

---

## Related Prompts

- `gcp_cloud_run_backend.md` -- Cloud Run integration patterns that use Secret Manager
- `gcp_solo_dev_cost_management.md` -- Budget management including Secret Manager free tier tracking
- `gcp_monitoring_alerting_setup.md` -- Alerting on suspicious secret access patterns
- `cloud_security_review.md` -- Broader cloud security review that includes secret management
- `cloud_gcp_best_practices.md` -- GCP best practices including security posture

---

## Customization Guide

- **For projects with only 1-3 secrets:** Skip the batch migration script and use the individual `gcloud secrets create` commands. Skip the automated rotation checker -- use calendar reminders instead. The full IAM per-secret setup is also overkill; project-level `secretAccessor` on the service account is fine.
- **For projects with 10+ secrets:** Use the batch migration script. Organize secrets with consistent labels (service, environment, owner). Consider using secret resource IDs with environment prefixes (e.g., `prod-stripe-key`, `dev-stripe-key`) to separate environments cleanly.
- **For teams with multiple developers:** Add each developer's Google account with `secretmanager.viewer` role (can see secret names but not values). Use per-secret IAM bindings so developers only have access to secrets relevant to their work. Enable all audit log types and set up alerts for human secret access.
- **For CI/CD pipelines (GitHub Actions):** Use Workload Identity Federation instead of service account key files. Grant the CI/CD service account `secretVersionManager` for rotation automation and `secretAccessor` for reading secrets during deployment.
- **For compliance requirements (SOC 2, HIPAA):** Enable all four audit log types. Set up log sinks to export audit logs to a separate project for tamper resistance. Enforce 90-day rotation on all secrets. Document your secret management policy referencing this implementation.
