---
title: "GitOps Workflow Design and Implementation"
category: devops
description: "Design GitOps workflows for declarative and auditable infrastructure delivery"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
difficulty: intermediate
tags:
  - gitops
  - argocd
  - flux
  - kubernetes
  - deployment
  - automation
updated: "2026-03-19"
---

# GitOps Workflow Design and Implementation

**Objective:** Design and implement GitOps workflows for declarative infrastructure and application delivery, ensuring consistent, auditable, and automated deployments across environments.

**When to Use:** Use this prompt when implementing continuous deployment with GitOps principles, setting up ArgoCD or Flux, designing multi-environment promotion strategies, or establishing GitOps standards for your organization.

**Instructions:**

1. **Repository Structure Design**
   - Design mono-repo vs. multi-repo strategy
   - Define directory structure for environments/applications
   - Review branching strategy for GitOps
   - Analyze secret management integration
   - Check for proper separation of config and code

2. **Deployment Strategy**
   - Design environment promotion workflow
   - Review sync policies and automation levels
   - Analyze deployment wave/ordering patterns
   - Check for dependency management
   - Review rollback and recovery procedures

3. **ArgoCD/Flux Configuration**
   - Review Application/HelmRelease definitions
   - Analyze sync options and retry configurations
   - Check for resource pruning policies
   - Review health check configurations
   - Analyze multi-cluster deployment patterns

4. **Security and Access Control**
   - Review repository access controls
   - Analyze RBAC for GitOps operators
   - Check for secrets management (Sealed Secrets, SOPS, External Secrets)
   - Review audit logging and compliance
   - Analyze network policies for GitOps operators

5. **Automation and Integration**
   - Design image update automation
   - Review CI/CD integration points
   - Analyze notification and alerting setup
   - Check for drift detection and reconciliation
   - Review progressive delivery integration

6. **Observability and Troubleshooting**
   - Review sync status monitoring
   - Analyze deployment metrics collection
   - Check for proper error reporting
   - Review debugging capabilities

**Expected Output:** A comprehensive GitOps implementation guide including:
- Repository structure recommendations
- ArgoCD/Flux configuration examples
- Environment promotion workflows
- Secret management strategies
- Monitoring and alerting setup
- Implementation checklist

**Example Output:**

```markdown
## GitOps Implementation Guide

### Platform: Kubernetes Multi-Environment
### Tools: ArgoCD + Kustomize + Sealed Secrets

---

### Repository Structure

#### Recommended: App-of-Apps Pattern

```
gitops-config/
├── README.md
├── bootstrap/                    # Initial cluster setup
│   ├── argocd/
│   │   ├── install.yaml
│   │   └── argocd-cm.yaml
│   └── sealed-secrets/
│       └── controller.yaml
│
├── apps/                         # Application definitions
│   ├── root.yaml                 # Root app-of-apps
│   ├── dev/
│   │   └── apps.yaml             # Dev environment apps
│   ├── staging/
│   │   └── apps.yaml
│   └── production/
│       └── apps.yaml
│
├── base/                         # Base Kustomize configs
│   ├── api-gateway/
│   │   ├── kustomization.yaml
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── configmap.yaml
│   ├── payment-service/
│   └── order-service/
│
├── overlays/                     # Environment-specific configs
│   ├── dev/
│   │   ├── kustomization.yaml
│   │   ├── namespace.yaml
│   │   └── patches/
│   │       └── replicas.yaml
│   ├── staging/
│   │   ├── kustomization.yaml
│   │   └── patches/
│   └── production/
│       ├── kustomization.yaml
│       ├── patches/
│       └── secrets/              # Sealed Secrets
│           └── db-credentials.yaml
│
└── infrastructure/               # Cluster infrastructure
    ├── monitoring/
    ├── ingress/
    └── cert-manager/
```

---

### ArgoCD Configuration

#### Root Application (App of Apps)
```yaml
# apps/root.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: root
  namespace: argocd
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: https://github.com/org/gitops-config
    targetRevision: HEAD
    path: apps
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

#### Environment Applications
```yaml
# apps/production/apps.yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: production-apps
  namespace: argocd
spec:
  generators:
    - git:
        repoURL: https://github.com/org/gitops-config
        revision: HEAD
        directories:
          - path: overlays/production/*
  template:
    metadata:
      name: 'prod-{{path.basename}}'
      labels:
        environment: production
    spec:
      project: production
      source:
        repoURL: https://github.com/org/gitops-config
        targetRevision: HEAD
        path: '{{path}}'
      destination:
        server: https://kubernetes.default.svc
        namespace: production
      syncPolicy:
        automated:
          prune: false          # Manual prune in prod
          selfHeal: true
        syncOptions:
          - CreateNamespace=true
          - PrunePropagationPolicy=foreground
          - PruneLast=true
```

#### Application with Health Checks
```yaml
# apps/dev/api-gateway.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: dev-api-gateway
  namespace: argocd
  annotations:
    notifications.argoproj.io/subscribe.on-sync-succeeded.slack: deployments
    notifications.argoproj.io/subscribe.on-sync-failed.slack: deployments
spec:
  project: development
  source:
    repoURL: https://github.com/org/gitops-config
    targetRevision: HEAD
    path: overlays/dev/api-gateway
  destination:
    server: https://kubernetes.default.svc
    namespace: dev
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - Validate=true
      - CreateNamespace=true
      - ServerSideApply=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
  # Custom health checks
  ignoreDifferences:
    - group: apps
      kind: Deployment
      jsonPointers:
        - /spec/replicas  # Managed by HPA
```

---

### Environment Promotion Workflow

#### Promotion Strategy: PR-Based

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│     Dev     │────▶│   Staging   │────▶│ Production  │
│  (auto)     │     │  (auto)     │     │  (manual)   │
└─────────────┘     └─────────────┘     └─────────────┘
      │                   │                    │
      ▼                   ▼                    ▼
   main:dev/        main:staging/        main:production/

Promotion = PR from source env to target env
```

#### Kustomize Base Configuration
```yaml
# base/api-gateway/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - deployment.yaml
  - service.yaml
  - configmap.yaml
  - hpa.yaml
  - pdb.yaml

commonLabels:
  app.kubernetes.io/name: api-gateway
  app.kubernetes.io/managed-by: argocd

images:
  - name: api-gateway
    newName: ghcr.io/org/api-gateway
    newTag: latest  # Overridden per environment
```

#### Environment Overlay
```yaml
# overlays/production/api-gateway/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: production

resources:
  - ../../../base/api-gateway
  - sealed-secret.yaml

commonAnnotations:
  environment: production

images:
  - name: api-gateway
    newName: ghcr.io/org/api-gateway
    newTag: v1.2.3  # Specific version for prod

replicas:
  - name: api-gateway
    count: 5

patches:
  - path: patches/resources.yaml
  - path: patches/hpa.yaml

configMapGenerator:
  - name: api-gateway-config
    behavior: merge
    literals:
      - LOG_LEVEL=info
      - ENVIRONMENT=production
```

#### Resource Patches
```yaml
# overlays/production/api-gateway/patches/resources.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-gateway
spec:
  template:
    spec:
      containers:
        - name: api-gateway
          resources:
            requests:
              cpu: 500m
              memory: 512Mi
            limits:
              cpu: 1000m
              memory: 1Gi
```

---

### Secret Management with Sealed Secrets

#### Creating Sealed Secrets
```bash
# Create secret locally
kubectl create secret generic db-credentials \
  --from-literal=username=admin \
  --from-literal=password=supersecret \
  --dry-run=client -o yaml > secret.yaml

# Seal the secret (can be safely committed)
kubeseal --format=yaml \
  --controller-namespace=kube-system \
  --controller-name=sealed-secrets \
  < secret.yaml > sealed-secret.yaml

# Remove plaintext secret
rm secret.yaml
```

#### Sealed Secret Resource
```yaml
# overlays/production/api-gateway/sealed-secret.yaml
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: db-credentials
  namespace: production
spec:
  encryptedData:
    username: AgBy8hCi... # Encrypted
    password: AgA3Kx9p... # Encrypted
  template:
    metadata:
      name: db-credentials
      namespace: production
    type: Opaque
```

#### Alternative: External Secrets Operator
```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
  namespace: production
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: ClusterSecretStore
  target:
    name: db-credentials
    creationPolicy: Owner
  data:
    - secretKey: username
      remoteRef:
        key: production/api-gateway/database
        property: username
    - secretKey: password
      remoteRef:
        key: production/api-gateway/database
        property: password
```

---

### Image Update Automation

#### ArgoCD Image Updater
```yaml
# Install ArgoCD Image Updater
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: argocd-image-updater
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://argoproj.github.io/argo-helm
    chart: argocd-image-updater
    targetRevision: 0.9.1
    helm:
      values: |
        config:
          registries:
            - name: GitHub Container Registry
              prefix: ghcr.io
              api_url: https://ghcr.io
              credentials: pullsecret:argocd/ghcr-creds
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
```

#### Application with Auto-Update
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: dev-api-gateway
  namespace: argocd
  annotations:
    # Auto-update image in dev
    argocd-image-updater.argoproj.io/image-list: api=ghcr.io/org/api-gateway
    argocd-image-updater.argoproj.io/api.update-strategy: latest
    argocd-image-updater.argoproj.io/api.allow-tags: regexp:^[0-9]+\.[0-9]+\.[0-9]+$
    argocd-image-updater.argoproj.io/write-back-method: git
    argocd-image-updater.argoproj.io/git-branch: main
spec:
  # ... rest of application spec
```

---

### Notifications Configuration

```yaml
# ArgoCD Notifications ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-notifications-cm
  namespace: argocd
data:
  service.slack: |
    token: $slack-token
  service.webhook.github: |
    url: https://api.github.com
    headers:
      - name: Authorization
        value: token $github-token

  trigger.on-sync-succeeded: |
    - when: app.status.sync.status == 'Synced'
      send: [app-sync-succeeded]
  trigger.on-sync-failed: |
    - when: app.status.sync.status == 'Failed'
      send: [app-sync-failed]
  trigger.on-health-degraded: |
    - when: app.status.health.status == 'Degraded'
      send: [app-health-degraded]

  template.app-sync-succeeded: |
    message: |
      Application {{.app.metadata.name}} sync succeeded.
      Revision: {{.app.status.sync.revision}}
    slack:
      attachments: |
        [{
          "color": "#18be52",
          "title": "{{.app.metadata.name}} Sync Succeeded",
          "fields": [
            {"title": "Environment", "value": "{{.app.metadata.labels.environment}}", "short": true},
            {"title": "Revision", "value": "{{.app.status.sync.revision | substr 0 7}}", "short": true}
          ]
        }]

  template.app-sync-failed: |
    message: |
      Application {{.app.metadata.name}} sync failed!
    slack:
      attachments: |
        [{
          "color": "#E96D76",
          "title": "{{.app.metadata.name}} Sync Failed",
          "text": "{{.app.status.conditions | first | default dict | get \"message\" \"Unknown error\"}}",
          "fields": [
            {"title": "Environment", "value": "{{.app.metadata.labels.environment}}", "short": true}
          ]
        }]
```

---

### Multi-Cluster Setup

```yaml
# Register external clusters
apiVersion: v1
kind: Secret
metadata:
  name: production-cluster
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: cluster
type: Opaque
stringData:
  name: production
  server: https://production.k8s.example.com
  config: |
    {
      "bearerToken": "<token>",
      "tlsClientConfig": {
        "insecure": false,
        "caData": "<base64-encoded-ca>"
      }
    }
---
# ApplicationSet for multi-cluster
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: api-gateway-multicluster
  namespace: argocd
spec:
  generators:
    - clusters:
        selector:
          matchLabels:
            env: production
  template:
    metadata:
      name: 'api-gateway-{{name}}'
    spec:
      project: production
      source:
        repoURL: https://github.com/org/gitops-config
        targetRevision: HEAD
        path: overlays/production/api-gateway
      destination:
        server: '{{server}}'
        namespace: production
```

---

### Implementation Checklist

| Phase | Task | Priority | Status |
|-------|------|----------|--------|
| **Setup** | Install ArgoCD | High | Done |
| | Configure RBAC | High | Done |
| | Set up Sealed Secrets | High | In Progress |
| | Create repository structure | High | In Progress |
| **Configuration** | Define base configs | High | Pending |
| | Create environment overlays | High | Pending |
| | Configure ApplicationSets | Medium | Pending |
| | Set up notifications | Medium | Pending |
| **Automation** | Image updater for dev | Medium | Pending |
| | PR automation for promotions | Medium | Pending |
| **Security** | External secrets integration | High | Pending |
| | Network policies | Medium | Pending |
| **Monitoring** | Sync status dashboard | Medium | Pending |
| | Alert rules | Medium | Pending |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- DS-03 (Tool and Methodology Suggestions)
- DT-01 (Hierarchical Task Breakdown)

**Related Prompts:**
- devops_kubernetes_manifest_review.md - For K8s manifest best practices
- devops_cicd_pipeline_analysis.md - For CI integration
- devops_helm_chart_review.md - For Helm-based GitOps
- devops_infrastructure_as_code_review.md - For infrastructure GitOps

**Customization Guide:**
- **For Flux**: Replace ArgoCD examples with Flux HelmRelease and Kustomization CRDs
- **For Helm-based**: Use ArgoCD Helm source instead of Kustomize
- **For Monorepos**: Adjust path configurations for monorepo structures
- **For Multi-Tenant**: Add project isolation and RBAC per tenant
