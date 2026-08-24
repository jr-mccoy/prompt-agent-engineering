---
title: "GCP Cloud Run Backend for Firebase Android Apps"
category: cloud-infrastructure
description: "Design and deploy a Cloud Run backend to complement Firebase when Cloud Functions are not enough, covering containerization, auto-scaling, cost optimization, and the decision framework for when to graduate from Functions to Cloud Run."
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
  - cloud-run
  - firebase
  - docker
  - containers
  - backend
  - auto-scaling
  - solo-developer
  - android
updated: "2026-02-11"
---

# GCP Cloud Run Backend for Firebase Android Apps

**Objective:** Design, containerize, and deploy a Cloud Run backend service that complements your existing Firebase setup. This guide covers the decision of when Cloud Functions are no longer sufficient, how to build a proper containerized backend, configure auto-scaling for cost efficiency, and integrate with your existing Firebase services (Auth, Firestore, Cloud Storage) from Cloud Run.

**When to Use:** Use this prompt when your Cloud Functions are hitting execution time limits (60s for v1, 540s for v2), you need a custom runtime or system dependency, you want WebSocket or server-sent events support, your function cold starts are unacceptable for user-facing endpoints, or you need a traditional HTTP server pattern with middleware, routing, and persistent connections. This is the natural next step when Firebase Cloud Functions start feeling like a constraint rather than a convenience.

---

## Context Gathering

Before migrating to or adding Cloud Run, gather the following:

1. **Current Architecture**
   - What Cloud Functions do you currently have?
   - Which ones are hitting limits (timeout, memory, cold start)?
   - What Firebase services are they interacting with?
   - What is your current monthly Cloud Functions cost?

2. **Requirements for Cloud Run**
   - What language/framework do you want to use? (Express, Fastify, Flask, Go, etc.)
   - Do you need WebSocket or long-lived connections?
   - Do you need background processing longer than 9 minutes?
   - Do you need custom system libraries (FFmpeg, ImageMagick, Puppeteer)?

3. **Traffic Patterns**
   - What is your expected requests per second?
   - Are there traffic spikes (marketing campaigns, viral moments)?
   - What is your acceptable cold start latency?
   - Is traffic concentrated in specific hours/timezones?

4. **Integration Needs**
   - Does the backend need Firebase Auth verification?
   - Does it need to read/write Firestore?
   - Does it need Cloud Storage access?
   - Any external APIs or databases?

---

## Instructions

### CRITICAL: Verification Requirements

Before deploying to Cloud Run, verify:

1. **Your container starts and responds to HTTP requests** on the port specified by the `PORT` environment variable (Cloud Run sets this automatically)
2. **Your container passes a health check** within the startup timeout (default 300s, you should respond faster)
3. **Firebase Admin SDK is initialized** without a service account key file (Cloud Run uses the default compute service account)
4. **Your service account has the correct IAM roles** for Firestore, Cloud Storage, or any other GCP service you access
5. **You have tested locally with Docker** before deploying to Cloud Run
6. **Acceptable null result:** If your traffic is truly minimal (under 100 requests/day), Cloud Functions may still be the better choice. Cloud Run is not always an upgrade -- it is a different tool.

### False-Positive Prevention

- **DO NOT** migrate to Cloud Run just because it sounds more professional. Cloud Functions are perfectly fine for most solo developer workloads.
- **DO NOT** set `min-instances` to anything above 0 during development. That costs money 24/7.
- **DO NOT** use Cloud Run for scheduled jobs that run once a day -- Cloud Scheduler + Cloud Functions is simpler and cheaper.
- **DO NOT** store secrets in your Docker image or environment variables. Use Secret Manager.
- **DO** use Cloud Run's `--allow-unauthenticated` only for truly public endpoints. Put Firebase Auth verification in your code.
- **DO** set `max-instances` to prevent runaway scaling and surprise bills.
- **DO** test cold start time with your actual container before relying on it for user-facing requests.

---

### Phase 1: Cloud Functions vs Cloud Run Decision Framework

#### When to Stay with Cloud Functions

| Scenario | Cloud Functions | Why |
|----------|:-------------:|-----|
| Simple CRUD API endpoints | Best choice | Less infrastructure to manage |
| Firestore triggers (onCreate, onUpdate) | Only option | Cloud Run cannot be a Firestore trigger |
| Auth triggers (onCreate, onDelete) | Only option | Cloud Run cannot be a Firebase Auth trigger |
| Scheduled tasks under 9 minutes | Better choice | Cloud Scheduler integration is simpler |
| Low traffic (< 1000 req/day) | Better choice | Zero cost at low volume, no container maintenance |
| Pub/Sub event handlers | Good choice | Native integration, simpler setup |

#### When to Move to Cloud Run

| Scenario | Cloud Run | Why |
|----------|:---------:|-----|
| Execution > 9 minutes | Required | Cloud Functions v2 maxes at 540s; Cloud Run allows up to 60 min |
| Custom system dependencies | Required | Need FFmpeg, Puppeteer, ImageMagick, etc. |
| WebSocket / SSE support | Required | Cloud Functions do not support persistent connections |
| Complex middleware stacks | Better choice | Express/Fastify middleware patterns work naturally |
| gRPC endpoints | Better choice | Native gRPC support in Cloud Run |
| Container reuse matters | Better choice | More predictable warm instances |
| Multi-route API server | Better choice | One container with routing vs dozens of functions |
| GPU processing | Required | Cloud Run supports GPU (L4) for ML inference |

#### Cost Comparison: Cloud Functions v2 vs Cloud Run

| Metric | Cloud Functions v2 | Cloud Run | Notes |
|--------|-------------------|-----------|-------|
| **Free tier** | 2M invocations, 400K GB-s | 2M requests, 360K GB-s | Similar |
| **CPU pricing** | $0.0000100/GHz-s | $0.00002400/vCPU-s | Cloud Run slightly cheaper per compute |
| **Memory pricing** | $0.0000025/GB-s | $0.00000250/GiB-s | Roughly equivalent |
| **Requests** | $0.40/million | $0.40/million | Same |
| **Min instances** | $0 (scale to zero) | $0 (scale to zero) | Both support this |
| **Cold start** | 1-10s typical | 1-5s typical | Cloud Run often faster with optimized images |
| **Max timeout** | 540s (v2) | 3600s (default), up to 3600s | Cloud Run wins for long tasks |

**Bottom line for solo developers:** If you are under the free tier, both cost $0. The question is whether Cloud Functions' constraints are blocking you, not whether Cloud Run is cheaper.

---

### Phase 2: Building Your Cloud Run Container

#### Option A: TypeScript/Node.js with Express

```dockerfile
# Dockerfile
FROM node:20-slim AS builder

WORKDIR /app

# Install dependencies first (Docker cache optimization)
COPY package.json package-lock.json ./
RUN npm ci --only=production

# Copy source
COPY tsconfig.json ./
COPY src/ ./src/

# Build TypeScript
RUN npm run build

# Production stage
FROM node:20-slim

WORKDIR /app

# Copy built application
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY package.json ./

# Cloud Run sets PORT env var automatically
ENV PORT=8080
ENV NODE_ENV=production

# Run as non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser

EXPOSE 8080

CMD ["node", "dist/server.js"]
```

```typescript
// src/server.ts
import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import { initializeApp, applicationDefault } from 'firebase-admin/app';
import { getFirestore } from 'firebase-admin/firestore';
import { getAuth } from 'firebase-admin/auth';
import { getStorage } from 'firebase-admin/storage';

// Initialize Firebase Admin — no key file needed on Cloud Run
// It uses the default service account automatically
const firebaseApp = initializeApp({
  credential: applicationDefault(),
  storageBucket: `${process.env.GCP_PROJECT}.appspot.com`,
});

const db = getFirestore(firebaseApp);
const auth = getAuth(firebaseApp);
const storage = getStorage(firebaseApp);

const app = express();

// Middleware
app.use(helmet());
app.use(cors({ origin: true }));
app.use(express.json({ limit: '10mb' }));

// Health check endpoint (Cloud Run uses this)
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'healthy', timestamp: new Date().toISOString() });
});

// Firebase Auth middleware
async function verifyFirebaseToken(
  req: express.Request,
  res: express.Response,
  next: express.NextFunction
) {
  const authHeader = req.headers.authorization;
  if (!authHeader?.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Missing or invalid authorization header' });
  }

  try {
    const token = authHeader.split('Bearer ')[1];
    const decodedToken = await auth.verifyIdToken(token);
    (req as any).uid = decodedToken.uid;
    (req as any).email = decodedToken.email;
    next();
  } catch (error) {
    return res.status(401).json({ error: 'Invalid or expired token' });
  }
}

// Example: Protected endpoint that reads Firestore
app.get('/api/profile', verifyFirebaseToken, async (req, res) => {
  try {
    const uid = (req as any).uid;
    const doc = await db.collection('users').doc(uid).get();

    if (!doc.exists) {
      return res.status(404).json({ error: 'Profile not found' });
    }

    res.json({ profile: doc.data() });
  } catch (error) {
    console.error('Error fetching profile:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Example: Long-running endpoint (why you might need Cloud Run)
app.post('/api/generate-report', verifyFirebaseToken, async (req, res) => {
  try {
    const uid = (req as any).uid;

    // This might take 2-5 minutes — impossible in Cloud Functions v1
    const report = await generateComprehensiveReport(uid);

    // Save to Cloud Storage
    const bucket = storage.bucket();
    const file = bucket.file(`reports/${uid}/${Date.now()}.pdf`);
    await file.save(report, { contentType: 'application/pdf' });

    const [url] = await file.getSignedUrl({
      action: 'read',
      expires: Date.now() + 24 * 60 * 60 * 1000, // 24 hours
    });

    res.json({ reportUrl: url });
  } catch (error) {
    console.error('Error generating report:', error);
    res.status(500).json({ error: 'Report generation failed' });
  }
});

async function generateComprehensiveReport(uid: string): Promise<Buffer> {
  // Your long-running report generation logic here
  // This is where Cloud Run shines over Cloud Functions
  return Buffer.from('report-placeholder');
}

// Start server
const PORT = parseInt(process.env.PORT || '8080', 10);
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server listening on port ${PORT}`);
});
```

```json
// package.json
{
  "name": "my-cloud-run-backend",
  "version": "1.0.0",
  "scripts": {
    "build": "tsc",
    "start": "node dist/server.js",
    "dev": "ts-node-dev --respawn src/server.ts"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^4.18.2",
    "firebase-admin": "^12.0.0",
    "helmet": "^7.1.0"
  },
  "devDependencies": {
    "@types/cors": "^2.8.17",
    "@types/express": "^4.17.21",
    "ts-node-dev": "^2.0.0",
    "typescript": "^5.4.0"
  }
}
```

#### Option B: Python with FastAPI

```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Cloud Run sets PORT automatically
ENV PORT=8080

# Run as non-root
RUN useradd -r appuser
USER appuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

```python
# main.py
import os
from fastapi import FastAPI, Depends, HTTPException, Header
from firebase_admin import initialize_app, credentials, firestore, auth
import firebase_admin

# Initialize Firebase Admin
firebase_admin.initialize_app()
db = firestore.client()

app = FastAPI(title="My Android App Backend")

async def verify_firebase_token(authorization: str = Header(...)):
    """Verify Firebase ID token from Authorization header."""
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    token = authorization.split("Bearer ")[1]
    try:
        decoded = auth.verify_id_token(token)
        return decoded
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/api/profile")
async def get_profile(decoded_token: dict = Depends(verify_firebase_token)):
    uid = decoded_token["uid"]
    doc = db.collection("users").document(uid).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Profile not found")
    return {"profile": doc.to_dict()}
```

---

### Phase 3: Build, Test, and Deploy

#### Step 1: Test Locally with Docker

```bash
# Build the container locally
docker build -t my-backend:local .

# Run locally (simulating Cloud Run)
# Mount your service account key for local Firebase Admin access
docker run -p 8080:8080 \
  -e GOOGLE_APPLICATION_CREDENTIALS=/app/sa-key.json \
  -e GCP_PROJECT=my-android-app-prod \
  -v $HOME/.config/gcloud/application_default_credentials.json:/app/sa-key.json:ro \
  my-backend:local

# Test health endpoint
curl http://localhost:8080/health

# Test with a Firebase token (get one from your Android app or Firebase Auth REST API)
curl -H "Authorization: Bearer YOUR_FIREBASE_ID_TOKEN" \
  http://localhost:8080/api/profile
```

#### Step 2: Push to Artifact Registry

```bash
export PROJECT_ID="my-android-app-prod"
export REGION="us-central1"
export SERVICE_NAME="my-backend"

# Create Artifact Registry repository (one-time)
gcloud artifacts repositories create cloud-run-images \
  --repository-format=docker \
  --location=$REGION \
  --description="Cloud Run container images" \
  --project=$PROJECT_ID

# Configure Docker to use Artifact Registry
gcloud auth configure-docker $REGION-docker.pkg.dev

# Tag and push
docker tag my-backend:local \
  $REGION-docker.pkg.dev/$PROJECT_ID/cloud-run-images/$SERVICE_NAME:latest

docker push \
  $REGION-docker.pkg.dev/$PROJECT_ID/cloud-run-images/$SERVICE_NAME:latest
```

#### Step 3: Deploy to Cloud Run

```bash
# Deploy with solo-developer-optimized settings
gcloud run deploy $SERVICE_NAME \
  --image=$REGION-docker.pkg.dev/$PROJECT_ID/cloud-run-images/$SERVICE_NAME:latest \
  --region=$REGION \
  --project=$PROJECT_ID \
  --platform=managed \
  --port=8080 \
  --memory=512Mi \
  --cpu=1 \
  --timeout=300 \
  --concurrency=80 \
  --min-instances=0 \
  --max-instances=3 \
  --cpu-throttling \
  --execution-environment=gen2 \
  --set-env-vars="GCP_PROJECT=$PROJECT_ID,NODE_ENV=production" \
  --service-account=$SERVICE_NAME-sa@$PROJECT_ID.iam.gserviceaccount.com \
  --allow-unauthenticated

# The --allow-unauthenticated flag means Cloud Run itself does not gate access.
# Your code must verify Firebase tokens for protected endpoints.
# If ALL endpoints need auth, use --no-allow-unauthenticated and
# configure IAM invoker instead.
```

#### Step 4: Create a Dedicated Service Account

```bash
# Create a service account specifically for this Cloud Run service
gcloud iam service-accounts create $SERVICE_NAME-sa \
  --display-name="Cloud Run Backend Service Account" \
  --project=$PROJECT_ID

# Grant only the permissions it needs (least privilege)
# Firestore access
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_NAME-sa@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/datastore.user"

# Cloud Storage access
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_NAME-sa@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectAdmin"

# Secret Manager access (if using secrets)
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_NAME-sa@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"

# Firebase Auth token verification (needed to verify ID tokens)
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_NAME-sa@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/firebase.sdkAdminServiceAgent"
```

---

### Phase 4: Auto-Scaling Configuration for Solo Developers

#### Understanding Cloud Run Scaling

```
Request arrives
│
├─→ Is there a warm instance with capacity?
│   ├── Yes → Route to existing instance (fast, ~10ms)
│   └── No → Start new instance (cold start, 1-5s)
│       └── Is max-instances reached?
│           ├── Yes → Queue request (may timeout)
│           └── No → Create new instance
│
└─→ No requests for a while?
    └── Scale to min-instances (0 for solo devs = free)
```

#### Recommended Scaling Settings by Stage

| Setting | Development | Pre-Launch | Launched | Growing |
|---------|------------|------------|----------|---------|
| `min-instances` | 0 | 0 | 0 or 1 | 1-2 |
| `max-instances` | 1 | 3 | 5 | 10 |
| `concurrency` | 80 | 80 | 80 | 80-250 |
| `cpu` | 1 | 1 | 1 | 1-2 |
| `memory` | 256Mi | 512Mi | 512Mi | 512Mi-1Gi |
| `cpu-throttling` | Yes | Yes | Maybe | No |
| **Monthly cost (idle)** | $0 | $0 | $0-$15 | $15-$60 |

#### Key Scaling Parameters Explained

```bash
# --min-instances=0
# Scale to zero when no traffic. You pay nothing when idle.
# Trade-off: First request after idle period gets a cold start (1-5s).
# For solo devs: Keep at 0 until you have paying users.

# --max-instances=3
# Never run more than 3 instances. This is your cost ceiling.
# 3 instances with 1 vCPU each = max 3 vCPUs running.
# At $0.00002400/vCPU-second, max hourly cost = $0.26/hour.
# Monthly worst case (24/7 at max): ~$189/month.
# Reality for solo dev: You will never sustain max instances.

# --concurrency=80
# Each instance handles up to 80 simultaneous requests.
# If you have 80 concurrent users, 1 instance is enough.
# If you have 240 concurrent users, 3 instances handle it.
# Default is 80, which is good for most Node.js/Python backends.

# --cpu-throttling
# CPU is only allocated during request processing.
# Between requests, CPU drops to near-zero (saves money).
# Downside: Background processing between requests is slow.
# For solo devs: Use this unless you need background work.
```

#### Cost Ceiling Calculator

```
Monthly cost ceiling formula:
  max_instances × cpu × $0.00002400/vCPU-s × seconds_per_month
  + max_instances × memory_gb × $0.00000250/GiB-s × seconds_per_month
  + requests × $0.40/million

Example (solo dev settings):
  CPU: 3 × 1 × $0.00002400 × 2,592,000s = $186.62
  Memory: 3 × 0.5 × $0.00000250 × 2,592,000s = $9.72
  Requests: 100,000 × $0.40/1,000,000 = $0.04
  THEORETICAL MAX: $196.38/month

  BUT with cpu-throttling and scale-to-zero:
  REALISTIC (10% utilization): ~$19.64/month
  REALISTIC (1% utilization): ~$1.96/month
  FREE TIER covers: ~$0/month for low traffic
```

---

### Phase 5: Connecting Cloud Run to Your Android App

#### From Your Kotlin/Android Code

```kotlin
// In your Android app, call Cloud Run just like any other API
// Use the Firebase ID token for authentication

class BackendApi(private val auth: FirebaseAuth) {

    // Use your Cloud Run service URL
    private val baseUrl = "https://my-backend-xxxxx-uc.a.run.app"

    // Or use a custom domain if you have one
    // private val baseUrl = "https://api.myapp.com"

    suspend fun getProfile(): ProfileResponse {
        val token = auth.currentUser?.getIdToken(false)?.await()?.token
            ?: throw IllegalStateException("User not authenticated")

        val client = OkHttpClient()
        val request = Request.Builder()
            .url("$baseUrl/api/profile")
            .header("Authorization", "Bearer $token")
            .build()

        return withContext(Dispatchers.IO) {
            client.newCall(request).execute().use { response ->
                if (!response.isSuccessful) {
                    throw ApiException("API call failed: ${response.code}")
                }
                Json.decodeFromString(response.body!!.string())
            }
        }
    }
}
```

#### Custom Domain Setup (Optional but Professional)

```bash
# Map a custom domain to your Cloud Run service
gcloud run domain-mappings create \
  --service=$SERVICE_NAME \
  --domain=api.myapp.com \
  --region=$REGION \
  --project=$PROJECT_ID

# This gives you DNS records to add at your domain registrar
# Cloud Run handles TLS certificates automatically via Let's Encrypt
```

---

### Phase 6: CI/CD for Cloud Run (Solo Developer Edition)

#### Simple GitHub Actions Deployment

```yaml
# .github/workflows/deploy-cloud-run.yml
name: Deploy to Cloud Run

on:
  push:
    branches: [main]
    paths:
      - 'backend/**'  # Only deploy when backend code changes

jobs:
  deploy:
    runs-on: ubuntu-latest

    permissions:
      contents: read
      id-token: write  # Required for Workload Identity Federation

    steps:
      - uses: actions/checkout@v4

      - id: auth
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: ${{ secrets.WIF_PROVIDER }}
          service_account: ${{ secrets.WIF_SERVICE_ACCOUNT }}

      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v2

      - name: Configure Docker
        run: gcloud auth configure-docker us-central1-docker.pkg.dev

      - name: Build and Push
        working-directory: backend
        run: |
          docker build -t us-central1-docker.pkg.dev/${{ secrets.GCP_PROJECT }}/cloud-run-images/my-backend:${{ github.sha }} .
          docker push us-central1-docker.pkg.dev/${{ secrets.GCP_PROJECT }}/cloud-run-images/my-backend:${{ github.sha }}

      - name: Deploy to Cloud Run
        run: |
          gcloud run deploy my-backend \
            --image=us-central1-docker.pkg.dev/${{ secrets.GCP_PROJECT }}/cloud-run-images/my-backend:${{ github.sha }} \
            --region=us-central1 \
            --project=${{ secrets.GCP_PROJECT }} \
            --min-instances=0 \
            --max-instances=3
```

---

## Expected Output

After following this guide, you should have:

```markdown
## Cloud Run Backend Deployment Summary

### Service Details
| Property | Value |
|----------|-------|
| Service Name | my-backend |
| Region | us-central1 |
| URL | https://my-backend-xxxxx-uc.a.run.app |
| Container Image | us-central1-docker.pkg.dev/my-project/cloud-run-images/my-backend:abc123 |
| Service Account | my-backend-sa@my-project.iam.gserviceaccount.com |

### Scaling Configuration
| Setting | Value | Rationale |
|---------|-------|-----------|
| Min instances | 0 | Scale to zero for cost savings |
| Max instances | 3 | Cost ceiling of ~$196/month theoretical max |
| Concurrency | 80 | Handles 240 concurrent users across 3 instances |
| CPU | 1 vCPU | Sufficient for API workloads |
| Memory | 512Mi | Enough for Node.js + Firebase Admin SDK |
| CPU throttling | Enabled | Saves cost between requests |

### Integration Points
| Integration | Status | Notes |
|-------------|--------|-------|
| Firebase Auth verification | Configured | Middleware validates ID tokens |
| Firestore read/write | Configured | Via firebase-admin SDK |
| Cloud Storage | Configured | For file uploads/downloads |
| Secret Manager | Configured | For API keys |

### Estimated Monthly Cost
| Traffic Level | Requests/month | Est. Cost | Notes |
|--------------|---------------|-----------|-------|
| Development | 1,000 | $0.00 | Within free tier |
| Pre-launch | 50,000 | $0.00 | Within free tier |
| Soft launch | 500,000 | $0.50-$2.00 | Barely above free tier |
| Growing | 2,000,000 | $5-$15 | Still very cheap |
```

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defined the specific purpose of adding Cloud Run to a Firebase architecture
- **ST-02 (Sequential Step-by-Step Instructions):** Phased approach from decision framework through deployment and CI/CD
- **RT-02 (Multi-Dimensional Analysis):** Compared Cloud Functions vs Cloud Run across cost, capability, and complexity dimensions
- **CM-01 (Contextual Framing):** All examples oriented toward solo Android developer with Firebase
- **DS-06 (Prioritization and Severity Guidance):** Clear decision framework for when to migrate vs stay with Functions
- **DS-02 (Metric Specification):** Concrete cost calculations, scaling formulas, and performance benchmarks
- **RT-05 (Evidence-Based Reasoning):** Cost comparisons backed by actual GCP pricing

---

## Related Prompts

- `cloud_serverless_function_analysis.md` — Deep analysis of Cloud Functions performance and optimization
- `gcp_solo_dev_cost_management.md` — Budget management for your Cloud Run costs
- `gcp_secret_manager_setup.md` — Secure secrets for your Cloud Run backend
- `gcp_monitoring_alerting_setup.md` — Monitor your Cloud Run service health
- `cloud_gcp_best_practices.md` — Broader GCP architecture patterns

---

## Customization Guide

- **For Python/FastAPI backends:** Use the Option B Dockerfile and FastAPI code. FastAPI has better async performance than Flask and auto-generates OpenAPI docs, which is helpful for solo developers who are also the API consumer.
- **For Go backends:** Go containers are tiny (10-20MB), start in under 100ms, and use minimal memory. If you are comfortable with Go, it is the best language for Cloud Run cold start performance.
- **For WebSocket support:** Add `--session-affinity` to your deploy command so that WebSocket connections stick to the same instance. Set `concurrency` lower (10-20) since WebSocket connections are long-lived.
- **For background processing:** Remove `--cpu-throttling` and use Cloud Tasks to send work to your Cloud Run service. This lets you process jobs after returning a response to the user.
- **For multi-region deployment:** Deploy the same container to multiple regions and use a Global External Application Load Balancer to route traffic. This is overkill for most solo developers but matters if you have a global user base.
