---
name: helm-chart-scaffolding
description: Design, organize, and manage Helm charts for templating and packaging Kubernetes applications with reusable configurations. Use when creating Helm charts, packaging Kubernetes applications, or implementing templated deployments.
metadata:
  tags:
    - chart
    - cloud
    - helm
    - infrastructure
    - k8s
    - kubernetes
    - scaffolding
  updated: "2026-04-11"
---
# Helm Chart Scaffolding

Comprehensive guidance for creating, organizing, and managing Helm charts for packaging and deploying Kubernetes applications.

## Purpose

This skill provides step-by-step instructions for building production-ready Helm charts, including chart structure, templating patterns, values management, and validation strategies.

## When to Use This Skill

Use this skill when you need to:
- Create new Helm charts from scratch
- Package Kubernetes applications for distribution
- Manage multi-environment deployments with Helm
- Implement templating for reusable Kubernetes manifests
- Set up Helm chart repositories
- Follow Helm best practices and conventions

## Helm Overview

**Helm** is the package manager for Kubernetes that:
- Templates Kubernetes manifests for reusability
- Manages application releases and rollbacks
- Handles dependencies between charts
- Provides version control for deployments
- Simplifies configuration management across environments

## Step-by-Step Workflow

### 1. Initialize Chart Structure

**Create new chart:**
```bash
helm create my-app
```

**Standard chart structure:**
```
my-app/
├── Chart.yaml           # Chart metadata
├── values.yaml          # Default configuration values
├── charts/              # Chart dependencies
├── templates/           # Kubernetes manifest templates
│   ├── NOTES.txt       # Post-install notes
│   ├── _helpers.tpl    # Template helpers
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── serviceaccount.yaml
│   ├── hpa.yaml
│   └── tests/
│       └── test-connection.yaml
└── .helmignore         # Files to ignore
```

### 2. Configure Chart.yaml

**Chart metadata defines the package:**

```yaml
apiVersion: v2
name: my-app
description: A Helm chart for My Application
type: application
version: 1.0.0      # Chart version
appVersion: "2.1.0" # Application version

# Keywords for chart discovery
keywords:
  - web
  - api
  - backend

# Maintainer information
maintainers:
  - name: DevOps Team
    email: devops@example.com
    url: https://github.com/example/my-app

# Source code repository
sources:
  - https://github.com/example/my-app

# Homepage
home: https://example.com

# Chart icon
icon: https://example.com/icon.png

# Dependencies
dependencies:
  - name: postgresql
    version: "12.0.0"
    repository: "https://charts.bitnami.com/bitnami"
    condition: postgresql.enabled
  - name: redis
    version: "17.0.0"
    repository: "https://charts.bitnami.com/bitnami"
    condition: redis.enabled
```

**Reference:** See `assets/Chart.yaml.template` for complete example

### 3. Design values.yaml Structure

**Organize values hierarchically:**

```yaml
# Image configuration
image:
  repository: myapp
  tag: "1.0.0"
  pullPolicy: IfNotPresent

# Number of replicas
replicaCount: 3

# Service configuration
service:
  type: ClusterIP
  port: 80
  targetPort: 8080

# Ingress configuration
ingress:
  enabled: false
  className: nginx
  hosts:
    - host: app.example.com
      paths:
        - path: /
          pathType: Prefix

# Resources
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"

# Autoscaling
autoscaling:
  enabled: false
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 80

# Environment variables
env:
  - name: LOG_LEVEL
    value: "info"

# ConfigMap data
configMap:
  data:
    APP_MODE: production

# Dependencies
postgresql:
  enabled: true
  auth:
    database: myapp
    username: myapp

redis:
  enabled: false
```

**Reference:** See `assets/values.yaml.template` for complete structure

### 4. Create Template Files

**Use Go templating with Helm functions:**

**templates/deployment.yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-app.fullname" . }}
  labels:
    {{- include "my-app.labels" . | nindent 4 }}
spec:
  {{- if not .Values.autoscaling.enabled }}
  replicas: {{ .Values.replicaCount }}
  {{- end }}
  selector:
    matchLabels:
      {{- include "my-app.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "my-app.selectorLabels" . | nindent 8 }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
        imagePullPolicy: {{ .Values.image.pullPolicy }}
        ports:
        - name: http
          containerPort: {{ .Values.service.targetPort }}
        resources:
          {{- toYaml .Values.resources | nindent 12 }}
        env:
          {{- toYaml .Values.env | nindent 12 }}
```

### 5. Create Template Helpers

**templates/_helpers.tpl:**
```yaml
{{/*
Expand the name of the chart.
*/}}
{{- define "my-app.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "my-app.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "my-app.labels" -}}
helm.sh/chart: {{ include "my-app.chart" . }}
{{ include "my-app.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "my-app.selectorLabels" -}}
app.kubernetes.io/name: {{ include "my-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

### 6. Manage Dependencies

**Add dependencies in Chart.yaml:**
```yaml
dependencies:
  - name: postgresql
    version: "12.0.0"
    repository: "https://charts.bitnami.com/bitnami"
    condition: postgresql.enabled
```

**Update dependencies:**
```bash
helm dependency update
helm dependency build
```

**Override dependency values:**
```yaml
# values.yaml
postgresql:
  enabled: true
  auth:
    database: myapp
    username: myapp
    password: changeme
  primary:
    persistence:
      enabled: true
      size: 10Gi
```

### 7. Test and Validate

**Validation commands:**
```bash
# Lint the chart
helm lint my-app/

# Dry-run installation
helm install my-app ./my-app --dry-run --debug

# Template rendering
helm template my-app ./my-app

# Template with values
helm template my-app ./my-app -f values-prod.yaml

# Show computed values
helm show values ./my-app
```

**Validation script:**
```bash
#!/bin/bash
set -e

echo "Linting chart..."
helm lint .

echo "Testing template rendering..."
helm template test-release . --dry-run

echo "Checking for required values..."
helm template test-release . --validate

echo "All validations passed!"
```

**Reference:** See `scripts/validate-chart.sh`

### 8. Package and Distribute

**Package the chart:**
```bash
helm package my-app/
# Creates: my-app-1.0.0.tgz
```

**Create chart repository:**
```bash
# Create index
helm repo index .

# Upload to repository
# AWS S3 example
aws s3 sync . s3://my-helm-charts/ --exclude "*" --include "*.tgz" --include "index.yaml"
```

**Use the chart:**
```bash
helm repo add my-repo https://charts.example.com
helm repo update
helm install my-app my-repo/my-app
```

## Multi-Environment Configuration and Common Patterns

Multi-environment configuration (values-dev/staging/prod files with example `values-prod.yaml`), Hooks and Tests (pre-install Job hook, test-connection Pod, `helm test`), and Common Patterns (conditional resources, range iteration, file inclusion, global values) are in the reference file.

See [references/multi-environment-and-patterns.md](references/multi-environment-and-patterns.md)

## Best Practices

1. **Use semantic versioning** for chart and app versions
2. **Document all values** in values.yaml with comments
3. **Use template helpers** for repeated logic
4. **Validate charts** before packaging
5. **Pin dependency versions** explicitly
6. **Use conditions** for optional resources
7. **Follow naming conventions** (lowercase, hyphens)
8. **Include NOTES.txt** with usage instructions
9. **Add labels** consistently using helpers
10. **Test installations** in all environments

## Troubleshooting

**Template rendering errors:**
```bash
helm template my-app ./my-app --debug
```

**Dependency issues:**
```bash
helm dependency update
helm dependency list
```

**Installation failures:**
```bash
helm install my-app ./my-app --dry-run --debug
kubectl get events --sort-by='.lastTimestamp'
```

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/multi-environment-and-patterns.md` | Step 9 (multi-env values files + install command), Step 10 (pre-install hook + test-connection + helm test), Common Patterns 1–4 (conditional, range, file inclusion, global values) |
| `assets/Chart.yaml.template` | Chart metadata template |
| `assets/values.yaml.template` | Values structure template |
| `scripts/validate-chart.sh` | Validation script |
| `references/chart-structure.md` | Detailed chart organization |

## Related Skills

- `k8s-manifest-generator` - For creating base Kubernetes manifests
- `gitops-workflow` - For automated Helm chart deployments
