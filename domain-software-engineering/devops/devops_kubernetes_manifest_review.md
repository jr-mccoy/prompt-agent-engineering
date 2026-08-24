---
title: "Kubernetes Manifest Review and Best Practices"
category: devops
description: "Analyze Kubernetes manifests for security, resource optimization, and reliability patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
  - QA-01
difficulty: intermediate
tags:
  - kubernetes
  - k8s
  - containers
  - security
  - yaml
  - deployment
updated: "2026-03-19"
---

# Kubernetes Manifest Review and Best Practices

**Objective:** Analyze Kubernetes manifests (YAML configurations) for security vulnerabilities, resource optimization, reliability patterns, and adherence to production best practices.

**When to Use:** Use this prompt when deploying applications to Kubernetes, reviewing pull requests containing K8s manifests, auditing cluster configurations, preparing for production deployments, or establishing Kubernetes standards for your organization.

**Instructions:**

1. **Security Configuration Analysis**
   - Check for SecurityContext settings (runAsNonRoot, readOnlyRootFilesystem)
   - Review Pod Security Standards/Policies compliance
   - Analyze network policies for proper segmentation
   - Check for secrets management (avoid plaintext secrets)
   - Verify RBAC configurations for least privilege
   - Review service account usage and token mounting

2. **Resource Management Review**
   - Verify resource requests and limits are defined
   - Check for appropriate CPU and memory allocations
   - Analyze QoS class implications (Guaranteed, Burstable, BestEffort)
   - Review LimitRange and ResourceQuota applicability
   - Check for Vertical Pod Autoscaler compatibility

3. **Reliability and Availability**
   - Verify liveness and readiness probes are configured
   - Check startup probes for slow-starting containers
   - Review replica counts and PodDisruptionBudgets
   - Analyze pod anti-affinity rules for high availability
   - Check for proper termination grace periods
   - Review update strategy (RollingUpdate, Recreate)

4. **Networking Configuration**
   - Review Service type and exposure patterns
   - Check Ingress configurations and TLS settings
   - Analyze service mesh integration if applicable
   - Review DNS and service discovery patterns
   - Check for headless services where appropriate

5. **Storage and State Management**
   - Review PersistentVolumeClaim configurations
   - Check storage class appropriateness
   - Analyze stateful vs stateless patterns
   - Review volume mount paths and permissions
   - Check for emptyDir size limits

6. **Operational Excellence**
   - Verify proper labeling and annotation conventions
   - Check for namespace isolation
   - Review ConfigMap and Secret mounting patterns
   - Analyze logging and monitoring integration
   - Check for proper image pull policies
   - Verify container image tags (avoid :latest)

7. **Scalability Patterns**
   - Review HorizontalPodAutoscaler configurations
   - Check scaling metrics and thresholds
   - Analyze pod topology spread constraints
   - Review node affinity/anti-affinity rules
   - Check for cluster autoscaler compatibility

**Expected Output:** A comprehensive Kubernetes manifest review including:
- Security vulnerability assessment with severity ratings
- Resource optimization recommendations
- Reliability improvement suggestions
- Production readiness checklist
- Corrected manifest examples
- Architecture recommendations

**Example Output:**

```markdown
## Kubernetes Manifest Review Report

### Deployment: payment-service

#### Summary
- **Security Score**: 4/10 (Critical issues found)
- **Reliability Score**: 6/10 (Missing probes and PDB)
- **Resource Score**: 5/10 (No limits defined)
- **Production Readiness**: NOT READY

---

### Critical Issues

#### Issue 1: Container Running as Root (CRITICAL)
**File**: deployment.yaml, Line 24
**Problem**: No security context defined; container runs as root by default
**Risk**: Container escape could lead to node compromise

**Current**:
```yaml
containers:
  - name: payment-service
    image: payment:v1.2.3
```

**Recommended**:
```yaml
containers:
  - name: payment-service
    image: payment:v1.2.3
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

#### Issue 2: No Resource Limits (HIGH)
**File**: deployment.yaml, Line 24
**Problem**: Missing resource requests and limits
**Risk**: Pod can consume unlimited resources, affecting other workloads

**Recommended**:
```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

#### Issue 3: Missing Health Probes (HIGH)
**File**: deployment.yaml
**Problem**: No liveness, readiness, or startup probes defined
**Risk**: Kubernetes cannot detect unhealthy pods; traffic routed to failing instances

**Recommended**:
```yaml
livenessProbe:
  httpGet:
    path: /health/live
    port: 8080
  initialDelaySeconds: 15
  periodSeconds: 20
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /health/ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
  failureThreshold: 3

startupProbe:
  httpGet:
    path: /health/live
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 10
  failureThreshold: 30
```

#### Issue 4: Using :latest Tag (MEDIUM)
**File**: deployment.yaml, Line 25
**Problem**: Image tag `:latest` or missing tag
**Risk**: Non-reproducible deployments, unexpected updates

**Recommended**: Use specific version tags
```yaml
image: payment:v1.2.3@sha256:abc123...
```

---

### Security Checklist

| Check | Status | Severity |
|-------|--------|----------|
| runAsNonRoot | FAIL | Critical |
| readOnlyRootFilesystem | FAIL | High |
| allowPrivilegeEscalation: false | FAIL | High |
| Drop all capabilities | FAIL | High |
| Resource limits defined | FAIL | High |
| Secrets from external store | WARN | Medium |
| Network policy defined | FAIL | Medium |
| Service account token disabled | FAIL | Medium |
| Image pull policy: Always | PASS | - |
| No privileged containers | PASS | - |

---

### Reliability Checklist

| Check | Status | Notes |
|-------|--------|-------|
| Liveness probe | FAIL | Required for auto-restart |
| Readiness probe | FAIL | Required for traffic management |
| Startup probe | FAIL | Recommended for slow starts |
| Replicas >= 2 | FAIL | Currently 1 |
| PodDisruptionBudget | FAIL | Required for safe updates |
| Pod anti-affinity | FAIL | Pods may land on same node |
| terminationGracePeriodSeconds | WARN | Using default 30s |

---

### Production-Ready Manifest

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-service
  namespace: payments
  labels:
    app: payment-service
    version: v1.2.3
    team: payments
spec:
  replicas: 3
  selector:
    matchLabels:
      app: payment-service
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: payment-service
        version: v1.2.3
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
    spec:
      serviceAccountName: payment-service
      automountServiceAccountToken: false
      securityContext:
        runAsNonRoot: true
        fsGroup: 1000
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchLabels:
                    app: payment-service
                topologyKey: kubernetes.io/hostname
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: ScheduleAnyway
          labelSelector:
            matchLabels:
              app: payment-service
      containers:
        - name: payment-service
          image: payment:v1.2.3
          imagePullPolicy: Always
          securityContext:
            runAsNonRoot: true
            runAsUser: 1000
            runAsGroup: 1000
            readOnlyRootFilesystem: true
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL
          ports:
            - containerPort: 8080
              name: http
              protocol: TCP
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /health/live
              port: http
            initialDelaySeconds: 15
            periodSeconds: 20
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /health/ready
              port: http
            initialDelaySeconds: 5
            periodSeconds: 10
            failureThreshold: 3
          startupProbe:
            httpGet:
              path: /health/live
              port: http
            initialDelaySeconds: 10
            periodSeconds: 10
            failureThreshold: 30
          env:
            - name: LOG_LEVEL
              value: "info"
          envFrom:
            - configMapRef:
                name: payment-config
          volumeMounts:
            - name: tmp
              mountPath: /tmp
      volumes:
        - name: tmp
          emptyDir:
            sizeLimit: 100Mi
      terminationGracePeriodSeconds: 60
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: payment-service-pdb
  namespace: payments
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: payment-service
```

---

### Additional Recommendations

1. **Add Network Policy**: Restrict ingress/egress to required services only
2. **External Secrets**: Use External Secrets Operator or Sealed Secrets
3. **Horizontal Pod Autoscaler**: Configure based on CPU/memory or custom metrics
4. **Service Mesh**: Consider Istio/Linkerd for mTLS and observability
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- OC-03 (Markdown Table Specification)
- DS-06 (Prioritization and Severity Guidance)
- RT-05 (Evidence-Based Reasoning)

**Related Prompts:**
- devops_dockerfile_optimization.md - For container image optimization
- devops_helm_chart_review.md - For Helm chart analysis
- devops_infrastructure_as_code_review.md - For IaC patterns
- devops_container_security.md - For deeper container security

**Customization Guide:**
- **For StatefulSets**: Add guidance on volumeClaimTemplates, ordered deployment, headless services
- **For DaemonSets**: Focus on node selectors, tolerations, update strategies
- **For Jobs/CronJobs**: Emphasize completion policies, backoff limits, concurrency
- **For Multi-Cluster**: Add federation, GitOps, and cross-cluster networking considerations
- **For Service Mesh**: Include Istio/Linkerd annotations, traffic policies, mTLS configuration
