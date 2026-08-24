---
title: "Helm Chart Review and Best Practices"
category: devops
description: "Analyze Helm charts for security, maintainability, and best practices compliance"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
  - QA-01
difficulty: intermediate
tags:
  - helm
  - kubernetes
  - charts
  - templating
  - deployment
  - packaging
updated: "2026-03-19"
---

# Helm Chart Review and Best Practices

**Objective:** Analyze Helm charts for security, maintainability, configurability, and adherence to best practices to enable reliable and consistent Kubernetes deployments.

**When to Use:** Use this prompt when creating new Helm charts, reviewing chart pull requests, preparing charts for public distribution, auditing existing charts, or establishing Helm standards for your organization.

**Instructions:**

1. **Chart Structure Analysis**
   - Review Chart.yaml metadata completeness
   - Check directory structure conventions
   - Analyze templates organization
   - Review helper templates (_helpers.tpl)
   - Check for required files (NOTES.txt, values.schema.json)

2. **Values Configuration Review**
   - Analyze values.yaml organization and defaults
   - Check for values.schema.json validation
   - Review configuration flexibility and overridability
   - Analyze sensitive value handling
   - Check for proper defaults (images, resources, replicas)

3. **Template Quality Analysis**
   - Review template syntax and readability
   - Check for proper use of template functions
   - Analyze conditional logic patterns
   - Review loop implementations (range)
   - Check for template reusability

4. **Security Configuration**
   - Check for secure default configurations
   - Review RBAC templates if present
   - Analyze SecurityContext defaults
   - Check for secrets management patterns
   - Review network policy templates

5. **Kubernetes Best Practices**
   - Check for resource requests/limits in defaults
   - Review probe configurations
   - Analyze label and annotation patterns
   - Check for proper selector configurations
   - Review update strategy defaults

6. **Documentation and Usability**
   - Review README documentation completeness
   - Check NOTES.txt post-installation guidance
   - Analyze values documentation
   - Review example configurations
   - Check for CHANGELOG maintenance

7. **Testing and Validation**
   - Check for chart tests
   - Review CI/CD integration
   - Analyze linting configuration
   - Check for template testing patterns

**Expected Output:** A comprehensive Helm chart review including:
- Chart structure assessment
- Security vulnerability findings
- Configuration improvement recommendations
- Template quality issues with fixes
- Documentation gaps
- Complete corrected examples

**Example Output:**

```markdown
## Helm Chart Review Report

### Chart: my-application (v1.2.0)

#### Summary
- **Structure Score**: 7/10
- **Security Score**: 5/10 (Critical defaults missing)
- **Usability Score**: 6/10 (Documentation gaps)
- **Best Practices**: 65% compliance

---

### Critical Issues

#### Issue 1: Missing Security Context Defaults (HIGH)
**File**: templates/deployment.yaml
**Problem**: No security context defined by default

**Current**:
```yaml
spec:
  containers:
    - name: {{ .Chart.Name }}
      image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
```

**Recommended** (templates/deployment.yaml):
```yaml
spec:
  {{- with .Values.podSecurityContext }}
  securityContext:
    {{- toYaml . | nindent 8 }}
  {{- end }}
  containers:
    - name: {{ .Chart.Name }}
      image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
      {{- with .Values.securityContext }}
      securityContext:
        {{- toYaml . | nindent 12 }}
      {{- end }}
```

**values.yaml additions**:
```yaml
podSecurityContext:
  runAsNonRoot: true
  fsGroup: 1000

securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  runAsGroup: 1000
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
```

#### Issue 2: No Resource Defaults (HIGH)
**File**: values.yaml
**Problem**: Missing resource requests/limits leads to QoS issues

**Current**: No resources section

**Recommended**:
```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 512Mi
```

#### Issue 3: Using :latest Image Tag (MEDIUM)
**File**: values.yaml
**Problem**: Default tag is "latest" causing non-reproducible deployments

**Current**:
```yaml
image:
  repository: myapp
  tag: latest
```

**Recommended**:
```yaml
image:
  repository: myapp
  # Use Chart.AppVersion as default
  tag: ""
  pullPolicy: IfNotPresent

# In deployment.yaml:
image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
```

---

### Structure Improvements

#### Issue 4: Missing values.schema.json
**Problem**: No schema validation for values

**Recommended** (values.schema.json):
```json
{
  "$schema": "https://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["image", "service"],
  "properties": {
    "replicaCount": {
      "type": "integer",
      "minimum": 1,
      "default": 1
    },
    "image": {
      "type": "object",
      "required": ["repository"],
      "properties": {
        "repository": {
          "type": "string",
          "description": "Container image repository"
        },
        "tag": {
          "type": "string",
          "description": "Container image tag"
        },
        "pullPolicy": {
          "type": "string",
          "enum": ["Always", "IfNotPresent", "Never"],
          "default": "IfNotPresent"
        }
      }
    },
    "service": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": ["ClusterIP", "NodePort", "LoadBalancer"],
          "default": "ClusterIP"
        },
        "port": {
          "type": "integer",
          "minimum": 1,
          "maximum": 65535
        }
      }
    }
  }
}
```

#### Issue 5: Incomplete _helpers.tpl
**Current**: Basic name and labels only

**Recommended additions** (_helpers.tpl):
```yaml
{{/*
Create chart name and version for chart label.
*/}}
{{- define "myapp.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "myapp.labels" -}}
helm.sh/chart: {{ include "myapp.chart" . }}
{{ include "myapp.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "myapp.selectorLabels" -}}
app.kubernetes.io/name: {{ include "myapp.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "myapp.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "myapp.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}

{{/*
Return the appropriate apiVersion for ingress
*/}}
{{- define "myapp.ingress.apiVersion" -}}
{{- if semverCompare ">=1.19-0" .Capabilities.KubeVersion.GitVersion }}
{{- print "networking.k8s.io/v1" }}
{{- else }}
{{- print "networking.k8s.io/v1beta1" }}
{{- end }}
{{- end }}
```

---

### Template Quality Improvements

#### Issue 6: Hardcoded Probe Paths
**Current**:
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: http
```

**Recommended**:
```yaml
# values.yaml
probes:
  liveness:
    enabled: true
    path: /health/live
    initialDelaySeconds: 15
    periodSeconds: 20
    failureThreshold: 3
  readiness:
    enabled: true
    path: /health/ready
    initialDelaySeconds: 5
    periodSeconds: 10
    failureThreshold: 3
  startup:
    enabled: false
    path: /health/live
    initialDelaySeconds: 10
    periodSeconds: 10
    failureThreshold: 30

# deployment.yaml
{{- if .Values.probes.liveness.enabled }}
livenessProbe:
  httpGet:
    path: {{ .Values.probes.liveness.path }}
    port: http
  initialDelaySeconds: {{ .Values.probes.liveness.initialDelaySeconds }}
  periodSeconds: {{ .Values.probes.liveness.periodSeconds }}
  failureThreshold: {{ .Values.probes.liveness.failureThreshold }}
{{- end }}
```

#### Issue 7: Missing HPA Template
**Recommended** (templates/hpa.yaml):
```yaml
{{- if .Values.autoscaling.enabled }}
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: {{ include "myapp.fullname" . }}
  labels:
    {{- include "myapp.labels" . | nindent 4 }}
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: {{ include "myapp.fullname" . }}
  minReplicas: {{ .Values.autoscaling.minReplicas }}
  maxReplicas: {{ .Values.autoscaling.maxReplicas }}
  metrics:
    {{- if .Values.autoscaling.targetCPUUtilizationPercentage }}
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: {{ .Values.autoscaling.targetCPUUtilizationPercentage }}
    {{- end }}
    {{- if .Values.autoscaling.targetMemoryUtilizationPercentage }}
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: {{ .Values.autoscaling.targetMemoryUtilizationPercentage }}
    {{- end }}
{{- end }}
```

---

### Documentation Improvements

#### Issue 8: Incomplete README
**Recommended README.md structure**:

```markdown
# My Application Helm Chart

## Description
Brief description of what this chart deploys.

## Prerequisites
- Kubernetes 1.19+
- Helm 3.2+
- PV provisioner (if using persistence)

## Installing the Chart

```bash
helm repo add myrepo https://charts.example.com
helm install my-release myrepo/myapp
```

## Configuration

### Image Configuration
| Parameter | Description | Default |
|-----------|-------------|---------|
| `image.repository` | Image repository | `myapp` |
| `image.tag` | Image tag | `Chart.AppVersion` |
| `image.pullPolicy` | Pull policy | `IfNotPresent` |

### Service Configuration
| Parameter | Description | Default |
|-----------|-------------|---------|
| `service.type` | Service type | `ClusterIP` |
| `service.port` | Service port | `80` |

### Resource Configuration
| Parameter | Description | Default |
|-----------|-------------|---------|
| `resources.requests.cpu` | CPU request | `100m` |
| `resources.requests.memory` | Memory request | `128Mi` |

## Examples

### Production Configuration
```yaml
replicaCount: 3

resources:
  requests:
    cpu: 500m
    memory: 512Mi
  limits:
    cpu: 1000m
    memory: 1Gi

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
```

## Upgrading

### From 1.x to 2.x
- Breaking change: `foo` renamed to `bar`
```

---

### Testing Recommendations

#### Add Chart Tests (templates/tests/test-connection.yaml):
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: "{{ include "myapp.fullname" . }}-test-connection"
  labels:
    {{- include "myapp.labels" . | nindent 4 }}
  annotations:
    "helm.sh/hook": test
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['{{ include "myapp.fullname" . }}:{{ .Values.service.port }}/health']
  restartPolicy: Never
```

#### CI Configuration (.github/workflows/chart-test.yaml):
```yaml
name: Chart Testing

on:
  pull_request:
    paths:
      - 'charts/**'

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: azure/setup-helm@v3
      - run: helm lint charts/myapp

  template:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: azure/setup-helm@v3
      - run: helm template charts/myapp

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: helm/chart-testing-action@v2
      - run: ct lint-and-install --charts charts/myapp
```

---

### Recommended Chart Structure

```
myapp/
├── Chart.yaml
├── Chart.lock
├── values.yaml
├── values.schema.json
├── README.md
├── CHANGELOG.md
├── .helmignore
├── templates/
│   ├── NOTES.txt
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── serviceaccount.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── ingress.yaml
│   ├── hpa.yaml
│   ├── pdb.yaml
│   └── tests/
│       └── test-connection.yaml
└── ci/
    └── test-values.yaml
```

### Best Practices Checklist

| Practice | Status | Priority |
|----------|--------|----------|
| values.schema.json | FAIL | High |
| Security context defaults | FAIL | High |
| Resource defaults | FAIL | High |
| Complete _helpers.tpl | WARN | Medium |
| README documentation | WARN | Medium |
| NOTES.txt | PASS | - |
| Chart tests | FAIL | Medium |
| Linting in CI | FAIL | Medium |
| CHANGELOG | FAIL | Low |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- OC-03 (Markdown Table Specification)
- DS-03 (Tool and Methodology Suggestions)

**Related Prompts:**
- devops_kubernetes_manifest_review.md - For K8s manifest patterns
- devops_dockerfile_optimization.md - For container images
- devops_cicd_pipeline_analysis.md - For chart CI/CD
- devops_gitops_workflow.md - For GitOps deployment

**Customization Guide:**
- **For Library Charts**: Focus on reusable templates, no resources, comprehensive _helpers.tpl
- **For Operator Charts**: Include CRD templates, RBAC, webhook configurations
- **For Umbrella Charts**: Focus on dependencies, values propagation, subcharts
- **For Public Charts**: Emphasize documentation, examples, schema validation, extensive testing
