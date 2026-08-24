---
title: "Container Security Analysis and Hardening"
category: devops
description: "Analyze container security for vulnerabilities and compliance with defense-in-depth approach"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
  - DS-06
difficulty: advanced
tags:
  - containers
  - docker
  - security
  - vulnerability
  - compliance
  - hardening
updated: "2026-03-19"
---

# Container Security Analysis and Hardening

**Objective:** Analyze container configurations, images, and runtime environments for security vulnerabilities and compliance issues, providing actionable remediation guidance for defense-in-depth container security.

**When to Use:** Use this prompt when auditing container security posture, preparing for production deployments, responding to security findings, implementing container security policies, or establishing security baselines for containerized applications.

**Instructions:**

1. **Image Security Analysis**
   - Check for known vulnerabilities (CVEs) in base images and dependencies
   - Review image provenance and supply chain security
   - Analyze image signing and verification
   - Check for secrets or credentials in image layers
   - Review image size and attack surface
   - Verify image scanning integration in CI/CD

2. **Build-Time Security**
   - Review Dockerfile security practices
   - Check for multi-stage builds to minimize attack surface
   - Analyze package installation security
   - Review build argument handling
   - Check for unnecessary tools and utilities
   - Verify .dockerignore completeness

3. **Runtime Security Configuration**
   - Analyze container privileges and capabilities
   - Review user namespace configurations
   - Check for read-only filesystem usage
   - Review resource limitations (CPU, memory, PIDs)
   - Analyze network isolation and policies
   - Check for seccomp and AppArmor profiles

4. **Orchestration Security (Kubernetes)**
   - Review Pod Security Standards compliance
   - Analyze RBAC configurations
   - Check for service account security
   - Review network policies
   - Analyze admission controller usage
   - Check for runtime security tools (Falco, etc.)

5. **Secret Management**
   - Review secrets injection methods
   - Check for secrets in environment variables vs. volumes
   - Analyze external secrets management integration
   - Review secret rotation capabilities
   - Check for secrets encryption at rest

6. **Monitoring and Detection**
   - Review runtime threat detection capabilities
   - Analyze audit logging configuration
   - Check for anomaly detection
   - Review incident response procedures
   - Analyze forensic capabilities

7. **Compliance and Governance**
   - Check against CIS Docker/Kubernetes benchmarks
   - Review compliance requirements (SOC2, PCI-DSS, HIPAA)
   - Analyze policy enforcement mechanisms
   - Check for vulnerability management processes

**Expected Output:** A comprehensive container security assessment including:
- Vulnerability scan results summary
- Security misconfiguration findings
- Compliance gap analysis
- Prioritized remediation recommendations
- Secure configuration examples
- Security architecture recommendations

**Example Output:**

```markdown
## Container Security Assessment Report

### Application: payment-service
### Assessment Date: 2024-01-15

#### Executive Summary
- **Overall Security Score**: 4.5/10 (Critical improvements needed)
- **Critical Vulnerabilities**: 3
- **High Vulnerabilities**: 12
- **Compliance Status**: Non-compliant with CIS benchmarks

---

### Vulnerability Assessment

#### Image Scan Results: payment-service:v1.2.3

| Severity | Count | Notable CVEs |
|----------|-------|--------------|
| Critical | 3 | CVE-2023-44487 (HTTP/2 DoS), CVE-2023-4911 (glibc) |
| High | 12 | CVE-2023-38545 (curl), CVE-2023-39417 (PostgreSQL) |
| Medium | 28 | Various |
| Low | 45 | Various |

**Immediate Actions Required**:

1. **Rebuild with updated base image**:
```dockerfile
# Current (VULNERABLE)
FROM node:18.17.0

# Recommended (PATCHED)
FROM node:18.19.0-slim
```

2. **Update critical dependencies**:
```json
{
  "dependencies": {
    "pg": "^8.11.3",  // CVE-2023-39417 fixed
  }
}
```

---

### Security Misconfigurations

#### Finding 1: Container Running as Root (CRITICAL)
**Risk**: Container escape could lead to host compromise
**Evidence**:
```yaml
# Current deployment - No security context
containers:
  - name: payment-service
    image: payment-service:v1.2.3
```

**Remediation**:
```yaml
containers:
  - name: payment-service
    image: payment-service:v1.2.3
    securityContext:
      runAsNonRoot: true
      runAsUser: 1000
      runAsGroup: 1000
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
          - ALL
```

**Dockerfile changes**:
```dockerfile
FROM node:18.19.0-slim

# Create non-root user
RUN groupadd -g 1000 appgroup && \
    useradd -r -u 1000 -g appgroup appuser

WORKDIR /app
COPY --chown=appuser:appgroup . .

USER appuser
CMD ["node", "server.js"]
```

#### Finding 2: Secrets in Environment Variables (HIGH)
**Risk**: Secrets visible in container inspection, process listing
**Evidence**:
```yaml
env:
  - name: DATABASE_PASSWORD
    value: "hardcoded-password-123"  # CRITICAL!
  - name: API_KEY
    valueFrom:
      configMapKeyRef:  # Should be secretKeyRef
        name: app-config
        key: api-key
```

**Remediation**:
```yaml
# Use Kubernetes Secrets with volume mounting
volumes:
  - name: secrets
    secret:
      secretName: payment-secrets
      defaultMode: 0400

containers:
  - name: payment-service
    volumeMounts:
      - name: secrets
        mountPath: /secrets
        readOnly: true
    env:
      - name: DATABASE_PASSWORD_FILE
        value: /secrets/database-password
```

**Better: Use External Secrets Operator**:
```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: payment-secrets
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: ClusterSecretStore
  target:
    name: payment-secrets
  data:
    - secretKey: database-password
      remoteRef:
        key: prod/payment-service/database
        property: password
```

#### Finding 3: Missing Network Policies (HIGH)
**Risk**: Lateral movement within cluster possible
**Evidence**: No NetworkPolicy resources defined

**Remediation**:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: payment-service-policy
  namespace: payments
spec:
  podSelector:
    matchLabels:
      app: payment-service
  policyTypes:
    - Ingress
    - Egress
  ingress:
    # Allow traffic from API gateway only
    - from:
        - namespaceSelector:
            matchLabels:
              name: api-gateway
          podSelector:
            matchLabels:
              app: api-gateway
      ports:
        - protocol: TCP
          port: 8080
  egress:
    # Allow DNS
    - to:
        - namespaceSelector: {}
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53
    # Allow database access
    - to:
        - namespaceSelector:
            matchLabels:
              name: databases
          podSelector:
            matchLabels:
              app: postgresql
      ports:
        - protocol: TCP
          port: 5432
```

#### Finding 4: No Resource Limits (MEDIUM)
**Risk**: Container can consume unlimited resources, DoS risk
**Evidence**: No resources section in deployment

**Remediation**:
```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
    # Limit PIDs to prevent fork bombs
```

**Add LimitRange for namespace**:
```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
  namespace: payments
spec:
  limits:
    - default:
        memory: "512Mi"
        cpu: "500m"
      defaultRequest:
        memory: "256Mi"
        cpu: "250m"
      type: Container
```

---

### CIS Benchmark Compliance

#### Docker CIS Benchmark v1.5.0

| Control | Status | Finding |
|---------|--------|---------|
| 4.1 Create user for container | FAIL | Running as root |
| 4.5 Enable Content Trust | FAIL | Not enabled |
| 4.6 Add HEALTHCHECK | WARN | Missing in Dockerfile |
| 4.9 Use COPY instead of ADD | PASS | - |
| 4.10 Do not store secrets | FAIL | Found in env vars |
| 5.1 AppArmor profile | FAIL | Not configured |
| 5.2 SELinux context | FAIL | Not configured |
| 5.7 Limit memory | FAIL | No limits set |
| 5.9 Set on-failure restart | PASS | - |
| 5.10 Limit PIDs | FAIL | No limit |

#### Kubernetes CIS Benchmark v1.8.0

| Control | Status | Finding |
|---------|--------|---------|
| 5.1.1 RBAC least privilege | WARN | Overly permissive |
| 5.1.3 Minimize wildcard use | FAIL | Wildcards in RBAC |
| 5.2.2 Minimize privileged | PASS | No privileged pods |
| 5.2.3 Minimize root | FAIL | Running as root |
| 5.2.6 Minimize added capabilities | FAIL | No drop ALL |
| 5.4.1 Use secrets for sensitive data | FAIL | Using configmap |
| 5.7.1 Use namespaces | PASS | Proper isolation |
| 5.7.2 Use network policies | FAIL | None defined |

---

### Secure Container Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Security Layers                              │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Ingress    │  │   Mutual     │  │   Network    │          │
│  │   Gateway    │──│    TLS       │──│   Policies   │          │
│  │   (HTTPS)    │  │  (Istio)     │  │              │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                           │                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    Pod Security                          │    │
│  │  ┌─────────────────────────────────────────────────┐    │    │
│  │  │  Security Context                                │    │    │
│  │  │  - runAsNonRoot: true                           │    │    │
│  │  │  - readOnlyRootFilesystem: true                 │    │    │
│  │  │  - capabilities: drop ALL                       │    │    │
│  │  │  - seccompProfile: RuntimeDefault               │    │    │
│  │  └─────────────────────────────────────────────────┘    │    │
│  │                                                          │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │    │
│  │  │ Secrets  │  │ Resource │  │ Service  │              │    │
│  │  │ (Volume) │  │ Limits   │  │ Account  │              │    │
│  │  └──────────┘  └──────────┘  └──────────┘              │    │
│  └─────────────────────────────────────────────────────────┘    │
│                           │                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │    Image     │  │   Runtime    │  │    Audit     │          │
│  │   Scanning   │──│   Security   │──│   Logging    │          │
│  │   (Trivy)    │  │   (Falco)    │  │              │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

---

### Implementation Roadmap

#### Phase 1: Critical (Week 1)
1. Update base images to patch critical CVEs
2. Add security contexts to all deployments
3. Move secrets from env vars to Kubernetes Secrets

#### Phase 2: High Priority (Week 2-3)
1. Implement network policies
2. Configure resource limits
3. Enable image signing and verification
4. Deploy admission controller (Kyverno/OPA)

#### Phase 3: Hardening (Week 4-6)
1. Implement seccomp profiles
2. Deploy runtime security (Falco)
3. Configure audit logging
4. Establish vulnerability management process

---

### Recommended Tools

| Category | Tool | Purpose |
|----------|------|---------|
| Image Scanning | Trivy, Grype | Vulnerability detection |
| Runtime Security | Falco, Sysdig | Threat detection |
| Policy Enforcement | Kyverno, OPA/Gatekeeper | Admission control |
| Secrets | External Secrets, Vault | Secret management |
| Compliance | Kubescape, Polaris | CIS benchmarks |
| Network | Calico, Cilium | Network policies |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- OC-03 (Markdown Table Specification)
- DS-06 (Prioritization and Severity Guidance)
- DS-03 (Tool and Methodology Suggestions)
- DT-01 (Hierarchical Task Breakdown)

**Related Prompts:**
- devops_dockerfile_optimization.md - For secure Dockerfile patterns
- devops_kubernetes_manifest_review.md - For K8s security context
- code-analysis/security/security_owasp_top_10_analysis.md - For application security
- devops_infrastructure_as_code_review.md - For infrastructure security

**Customization Guide:**
- **For Regulated Industries**: Add HIPAA, PCI-DSS, SOC2 specific controls
- **For High-Security Environments**: Include hardware security modules, confidential computing
- **For Multi-Tenant Platforms**: Focus on tenant isolation, resource quotas, RBAC
- **For Edge Deployments**: Address air-gapped security, limited runtime monitoring


---

## Must / Must Not

**Must:**
- Cite concrete evidence for every finding (Dockerfile line, base image tag, runtime config, K8s securityContext field).
- Classify findings by CVSS-style severity: **Critical** (remote code exec, privilege escalation path), **High** (exploit vector with known CVE), **Medium** (hardening gap), **Low** / **Info**.
- Distinguish between **build-time** (image composition) and **runtime** (K8s / container runtime config) findings.
- Check for: non-root user, read-only rootfs, dropped capabilities, no privilege escalation, seccomp/AppArmor, image provenance (Sigstore / Cosign), SBOM, base image freshness, secret injection (not baked), network policy scope.
- Recommend specific fixes with the exact line change (Dockerfile, manifest, or policy).

**Must Not:**
- Flag a CVE without confirming the affected component is **present in the image AND reachable from the attack surface**.
- Recommend switching base images (distroless, Alpine, Chainguard) without acknowledging the migration cost and library-compatibility implications.
- Demand `readOnlyRootFilesystem: true` without confirming the app doesn't write to the rootfs at runtime.
- Recommend dropping **all** capabilities — most apps need at least a subset; name which.
- Invent security controls not supported by the runtime (e.g., seccomp profiles on a platform that doesn't support them).

## Verification (Self-Check)

Before reporting:

1. **Evidence anchored** — Every Critical/High finding points at a specific Dockerfile instruction, manifest key, or runtime flag.
2. **CVE relevance confirmed** — Only report CVEs for packages **present** in the image AND **called** at runtime (reachable code).
3. **Build-vs-runtime labeled** — Every finding tagged with where the fix belongs (Dockerfile / Helm / K8s manifest / runtime policy).
4. **Confidence** — High if inspected image directly, Medium if inspected Dockerfile only, Low if inspected deployment manifest only.
5. **Exploitability assessed** — Mark each Critical/High with exploitability: **Easy** / **Moderate** / **Hard** given the deployment surface.

## False-Positive Prevention

Rule out:

- **"CVE-XXXX in libXYZ"** — The library may be present but **unreachable** (not called by the app). Unreachable CVEs are Low, not Critical.
- **"Running as root"** — If running in a rootless runtime (Podman, Kata, gVisor), actual capability set may already be restricted.
- **"No readOnlyRootFilesystem"** — Some apps legitimately write caches to rootfs; recommend writable `emptyDir` volumes as the fix instead.
- **"No network policy"** — Platforms without CNI network policy support (some managed services) can't enforce them; recommend alternatives.
- **"Secrets in env vars"** — Env vars from K8s Secrets are often acceptable; only flag if secrets are in plain-text in the Dockerfile.
- **"Image is old"** — Age alone isn't a vulnerability; age + known unpatched CVE is.

Confidence must be **Medium** or higher to ship a Critical/High finding.
