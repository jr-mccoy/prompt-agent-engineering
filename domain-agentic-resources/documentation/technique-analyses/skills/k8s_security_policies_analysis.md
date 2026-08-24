# Technique Analysis: k8s-security-policies

**Resource Type:** Skill
**Path:** `skills/cloud-infrastructure/k8s-security-policies/`
**Date Analyzed:** 2025-12-22
**Category:** Cloud Infrastructure - Kubernetes Security
**Bundled Resources:** 1 asset (network-policy-template.yaml: 178 lines), 1 reference (rbac-patterns.md: 188 lines)
**Total Knowledge:** ~701 lines (335 in SKILL.md + 366 in bundled resources)
**Complexity:** 5/5 (Production-grade security with defense-in-depth, compliance mapping, policy enforcement)

---

## Resource Summary

**Purpose:** Enable Claude to implement comprehensive Kubernetes security including NetworkPolicy, Pod Security Standards, RBAC, OPA Gatekeeper, and service mesh security for production-grade clusters.

**Key Innovation:** Defense-in-depth architecture + compliance framework mapping + tiered security standards + template library

**Architecture:**
- **SKILL.md (335 lines):** Pod Security Standards, NetworkPolicies, RBAC, OPA Gatekeeper, Istio security, best practices, compliance
- **assets/network-policy-template.yaml (178 lines):** 8 production-ready network policy templates
- **references/rbac-patterns.md (188 lines):** 5 RBAC patterns, ServiceAccount best practices, troubleshooting

**Use Case:** When securing Kubernetes clusters, implementing network isolation, configuring RBAC, enforcing pod security standards, achieving compliance (CIS, NIST), or implementing admission control.

---

## Identified Techniques

### Technique 1: Security Tier Classification
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Define security tiers from least to most restrictive with clear progression
- **Example from resource:**
```markdown
## Pod Security Standards

### 1. Privileged (Unrestricted)
pod-security.kubernetes.io/enforce: privileged

### 2. Baseline (Minimally restrictive)
pod-security.kubernetes.io/enforce: baseline

### 3. Restricted (Most restrictive)
pod-security.kubernetes.io/enforce: restricted
```
- **Maps to existing:** NEW - **DS-61: Security Tier Classification**
- **Effectiveness:** Clear progression: Privileged (unrestricted) → Baseline (minimal restrictions) → Restricted (maximum security). Enables gradual tightening. Labels in parentheses provide context (Unrestricted, Minimally restrictive, Most restrictive).

### Technique 2: Default Deny + Selective Allow Pattern
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Start with default deny, then add selective allow policies
- **Example from resource:**
```yaml
# Template 1: Default Deny All (Start Here)
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress

# Template 2: Allow DNS (Essential)
# Template 3: Frontend to Backend
# Template 4: Allow Ingress Controller
...
```
- **Maps to existing:** NEW - **DS-62: Default Deny + Selective Allow Pattern**
- **Effectiveness:** Defense-in-depth security architecture. Template 1 blocks everything, Templates 2-8 add back required access. Comment "Start Here" guides order. Comment "Essential" on DNS shows it's always needed.

### Technique 3: Template Library Organization
- **Category:** IT (Interaction Techniques) - NEW (variation of IT-23)
- **Pattern:** Organize templates by use case with priority comments
- **Example from resource:**
```yaml
# Template 1: Default Deny All (Start Here)
# Template 2: Allow DNS (Essential)
# Template 3: Frontend to Backend
# Template 4: Allow Ingress Controller
# Template 5: Allow Monitoring (Prometheus)
# Template 6: Allow External HTTPS
# Template 7: Database Access
# Template 8: Cross-Namespace Communication
```
- **Maps to existing:** NEW - **DS-63: Template Library Organization**
- **Effectiveness:** 8 templates cover common patterns. Comments guide priority: (Start Here) → (Essential) → specific use cases. Users can copy templates 1-2 plus whatever fits their architecture (3-8).

### Technique 4: Compliance Framework Mapping
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Map technical controls to compliance framework requirements
- **Example from resource:**
```markdown
## Compliance Frameworks

### CIS Kubernetes Benchmark
- Use RBAC authorization
- Enable audit logging
- Use Pod Security Standards
- Configure network policies
- Implement secrets encryption at rest

### NIST Cybersecurity Framework
- Implement defense in depth
- Use network segmentation
- Configure security monitoring
- Implement access controls
```
- **Maps to existing:** NEW - **DS-64: Compliance Framework Mapping**
- **Effectiveness:** Shows which controls satisfy which compliance requirements. CIS Kubernetes Benchmark has specific requirements, NIST has broader categories. Enables compliance-driven security (need CIS compliance? implement these 6 controls).

### Technique 5: Policy Enforcement Layer Documentation
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Document admission control with policy-as-code (ConstraintTemplate + Constraint)
- **Example from resource:**
```yaml
## Policy Enforcement with OPA Gatekeeper

### ConstraintTemplate
kind: ConstraintTemplate
targets:
  - target: admission.k8s.gatekeeper.sh
    rego: |
      violation[{"msg": msg}] {
        # Policy logic in Rego
      }

### Constraint
kind: K8sRequiredLabels
parameters:
  labels: ["app", "environment"]
```
- **Maps to existing:** NEW - **DS-65: Policy Enforcement Layer Documentation**
- **Effectiveness:** Shows runtime policy enforcement (not just configuration). ConstraintTemplate defines the rule (Rego language), Constraint applies it to specific resources. Enables automated policy enforcement at admission time.

### Technique 6: Service Mesh Security Integration
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Document integration with service mesh for additional security layer
- **Example from resource:**
```markdown
## Service Mesh Security (Istio)

### PeerAuthentication (mTLS)
mtls:
  mode: STRICT

### AuthorizationPolicy
rules:
  - from:
    - source:
        principals: ["cluster.local/ns/production/sa/frontend"]
```
- **Maps to existing:** NEW - **DS-66: Service Mesh Security Integration**
- **Effectiveness:** Shows layered security: NetworkPolicy (network layer) + Istio mTLS (transport layer) + AuthorizationPolicy (application layer). Defense-in-depth with multiple enforcement points.

### Technique 7: Resource-Scoped Permissions
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** RBAC with resourceNames for fine-grained access to specific resources
- **Example from resource:**
```yaml
### Pattern 4: Secret Reader (ServiceAccount)
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get"]
  resourceNames: ["app-secrets"]  # Specific secret only
```
- **Maps to existing:** NEW - **DS-67: Resource-Scoped Permissions**
- **Effectiveness:** Least-privilege pattern. Not just "read all secrets" but "read this one secret". Prevents lateral movement (compromised app can only access its own secret, not others).

### Technique 8: Troubleshooting Command Sequences
- **Category:** DS (Domain-Specific) - EXISTING
- **Pattern:** Diagnostic command → Fix command
- **Example from resource:**
```markdown
**NetworkPolicy not working:**
kubectl get nodes -o wide
kubectl describe networkpolicy <name>

**RBAC permission denied:**
kubectl auth can-i list pods --as system:serviceaccount:default:my-sa
kubectl auth can-i '*' '*' --as system:serviceaccount:default:my-sa
```
- **Maps to existing:** DS-59 (from gitops-workflow analysis)
- **Effectiveness:** Shows investigation workflow. NetworkPolicy: check CNI support → describe policy. RBAC: test specific permission → test all permissions.

### Technique 9: Best Practices Enumeration
- **Category:** DS (Domain-Specific) - EXISTING
- **Pattern:** Numbered lists of security best practices
- **Example from resource:**
```markdown
## Best Practices

1. **Implement Pod Security Standards** at namespace level
2. **Use Network Policies** for network segmentation
3. **Apply least-privilege RBAC** for all service accounts
...
10. **Regular security scanning** of images

## Security Best Practices (RBAC)

1. **Use Roles over ClusterRoles** when possible
2. **Specify resourceNames** for fine-grained access
...
10. **Document role purposes** in metadata
```
- **Maps to existing:** DS-58 (from gitops-workflow analysis)
- **Effectiveness:** 10 best practices in main SKILL.md + 10 best practices in RBAC patterns = 20 total. Consolidates security tribal knowledge.

### Technique 10: Bundled Templates with Placeholders
- **Category:** IT (Interaction Techniques) - EXISTING
- **Pattern:** Ready-to-use templates with placeholder variables
- **Example from resource:**
```yaml
# Template files with <namespace> placeholder
metadata:
  name: default-deny-all
  namespace: <namespace>
```
- **Maps to existing:** IT-23 (Bundled Templates)
- **Effectiveness:** Users copy template, replace `<namespace>`, deploy. 8 templates cover common patterns. Zero-config for standard use cases.

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Security Tier Classification (DS-61)

**Description:** Define explicit security tiers (typically 3-5 levels) progressing from least to most restrictive, with clear labels indicating restriction level.

**Implementation:**
```markdown
## Security Tiers

### Tier 1: [Name] ([Restriction level description])
[Least restrictive configuration]

### Tier 2: [Name] ([Restriction level description])
[Medium restriction configuration]

### Tier 3: [Name] ([Restriction level description])
[Most restrictive configuration]
```

**Use case:**
- Kubernetes Pod Security Standards (Privileged, Baseline, Restricted)
- Data classification (Public, Internal, Confidential, Restricted)
- Access control levels (None, Read-Only, Read-Write, Admin)
- Network security zones (DMZ, Internal, Restricted, Isolated)

**Why it's novel:** Explicit progression enables gradual tightening. Start with Tier 1, incrementally move to Tier 3 as maturity increases. Labels in parentheses provide context (Unrestricted → Minimally restrictive → Most restrictive). Prevents binary thinking (secure vs insecure) in favor of graduated approach.

**Proposed category:** DS (Domain-Specific - Security)
**Proposed code:** DS-61

---

### Pattern 2: Default Deny + Selective Allow Pattern (DS-62)

**Description:** Start with default deny policy that blocks everything, then add selective allow policies for required access. Defense-in-depth security architecture.

**Implementation:**
```yaml
# Step 1: Default deny all
policy:
  default: DENY

# Step 2: Selectively allow required access
policy:
  allow:
    - [specific requirement 1]
    - [specific requirement 2]
```

**Use case:**
- Kubernetes NetworkPolicies (deny all → allow DNS → allow specific communication)
- Firewall rules (block all → allow SSH → allow HTTPS → allow specific services)
- API authorization (deny all → allow authenticated users → allow specific roles)
- File permissions (chmod 000 → chmod 440 for specific users)

**Why it's novel:** Security-first architecture. Everything blocked by default, only explicitly allowed traffic passes. Prevents forgotten edge cases (what if we don't think about X? → it's blocked). Comments guide order: "(Start Here)" on deny-all, "(Essential)" on critical allows.

**Proposed category:** DS (Domain-Specific - Security)
**Proposed code:** DS-62

---

### Pattern 3: Template Library Organization (DS-63)

**Description:** Organize templates by use case with priority annotations (Start Here, Essential, Optional) and numbered ordering.

**Implementation:**
```markdown
# Template 1: [Name] (Start Here)
# Template 2: [Name] (Essential)
# Template 3: [Name] ([Use case])
# Template 4: [Name] ([Use case])
```

**Use case:**
- Network policy templates (deny-all, DNS, frontend-backend, ingress, monitoring, external, database, cross-namespace)
- Dockerfile templates (base, builder, runtime, security-hardened)
- CI/CD pipeline templates (lint, test, build, deploy, rollback)
- Terraform module templates (VPC, ECS, RDS, S3, monitoring)

**Why it's novel:** Not just a list of templates, but guided selection. Numbering shows order (1 → 2 → 3...). Priority annotations guide which are mandatory vs optional. Users can quickly identify: "Use templates 1-2 always, then add 3-8 as needed."

**Proposed category:** DS (Domain-Specific - Configuration)
**Proposed code:** DS-63

---

### Pattern 4: Compliance Framework Mapping (DS-64)

**Description:** Map technical security controls to specific compliance framework requirements (CIS, NIST, SOC2, HIPAA, etc.).

**Implementation:**
```markdown
## Compliance Frameworks

### [Framework Name] (e.g., CIS Benchmark)
- [Control 1] → [Technical implementation]
- [Control 2] → [Technical implementation]
...

### [Framework Name] (e.g., NIST CSF)
- [Category 1] → [Technical controls that satisfy it]
- [Category 2] → [Technical controls that satisfy it]
```

**Use case:**
- Kubernetes security (CIS Benchmark, NIST, SOC2)
- Cloud security (AWS CIS, Azure CIS, GCP CIS)
- Application security (OWASP Top 10, PCI-DSS)
- Data protection (GDPR, HIPAA, CCPA)

**Why it's novel:** Bridges compliance (business requirement) and implementation (technical control). Instead of "be compliant" → "implement these 6 controls for CIS compliance". Enables compliance-driven development (need SOC2? here's the checklist).

**Proposed category:** DS (Domain-Specific - Compliance)
**Proposed code:** DS-64

---

### Pattern 5: Policy Enforcement Layer Documentation (DS-65)

**Description:** Document admission control / policy-as-code systems (OPA, Kyverno, etc.) showing ConstraintTemplate (policy definition) + Constraint (policy application).

**Implementation:**
```markdown
## Policy Enforcement

### Policy Definition
[ConstraintTemplate with policy logic]

### Policy Application
[Constraint specifying what resources to enforce]
```

**Use case:**
- Kubernetes admission control (OPA Gatekeeper, Kyverno, Pod Security Admission)
- Cloud policy enforcement (AWS SCPs, Azure Policy, GCP Organization Policies)
- Infrastructure-as-code validation (Checkov, tfsec, Sentinel)
- API gateway policies (Kong, Apigee, AWS API Gateway)

**Why it's novel:** Shows *runtime* policy enforcement, not just configuration. ConstraintTemplate = "what is the rule?" (Rego/CEL logic). Constraint = "where to apply it?" (which namespaces/resources). Enables automated compliance enforcement at admission time.

**Proposed category:** DS (Domain-Specific - Policy Enforcement)
**Proposed code:** DS-65

---

### Pattern 6: Service Mesh Security Integration (DS-66)

**Description:** Document integration with service mesh for layered security (network layer + transport layer + application layer).

**Implementation:**
```markdown
## Network Layer Security
[NetworkPolicy configuration]

## Transport Layer Security (Service Mesh)
[mTLS configuration]

## Application Layer Authorization (Service Mesh)
[AuthorizationPolicy configuration]
```

**Use case:**
- Kubernetes security (NetworkPolicy + Istio mTLS + AuthorizationPolicy)
- Microservices security (API Gateway + mTLS + JWT validation)
- Zero-trust architecture (network isolation + identity verification + authorization)

**Why it's novel:** Shows defense-in-depth with multiple enforcement points. Layer 1: NetworkPolicy blocks network traffic. Layer 2: mTLS encrypts and authenticates. Layer 3: AuthorizationPolicy checks service identity. If one layer fails, others still provide protection.

**Proposed category:** DS (Domain-Specific - Service Mesh Security)
**Proposed code:** DS-66

---

### Pattern 7: Resource-Scoped Permissions (DS-67)

**Description:** Fine-grained RBAC using resourceNames to limit access to specific resources by name, not just resource type.

**Implementation:**
```yaml
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get"]
  resourceNames: ["specific-secret-name"]  # Not all secrets, just this one
```

**Use case:**
- Kubernetes RBAC (access to specific Secret, ConfigMap, PVC)
- AWS IAM (access to specific S3 bucket, DynamoDB table)
- File permissions (access to specific files in directory)
- Database permissions (access to specific tables, not all tables)

**Why it's novel:** Moves from type-based access (all Secrets) to instance-based access (this Secret). Least-privilege pattern prevents lateral movement. Compromised app can only access `app1-secret`, not `app2-secret`, even though both are Secrets.

**Proposed category:** DS (Domain-Specific - RBAC)
**Proposed code:** DS-67

---

## Multi-Technique Combinations

### Combination 1: Defense-in-Depth Security (DS-61 + DS-62 + DS-66)

**Pattern:** Security tiers → Default deny → Layered enforcement

**Example:**
1. Pod Security Standard: Restricted (DS-61) - tightest pod security
2. NetworkPolicy: Default deny all → Allow specific (DS-62) - network isolation
3. Service Mesh: mTLS + AuthorizationPolicy (DS-66) - transport + app layer security

**Why effective:** Multiple security layers. Pod security prevents privileged containers, NetworkPolicy blocks network access, Service Mesh adds identity-based authorization. Attacker must bypass all three layers.

---

### Combination 2: Compliance-Driven Security (DS-64 + DS-61 + DS-65)

**Pattern:** Compliance framework → Security tiers → Policy enforcement

**Example:**
1. CIS Benchmark requirement (DS-64): "Use Pod Security Standards"
2. Implement Restricted tier (DS-61): `pod-security.kubernetes.io/enforce: restricted`
3. Enforce with OPA Gatekeeper (DS-65): Admission control prevents non-compliant pods

**Why effective:** Compliance requirement → Technical implementation → Automated enforcement. CIS says "use Pod Security Standards" → Choose Restricted tier → OPA blocks violations. Audit-ready security.

---

### Combination 3: Template-Based Security Deployment (DS-63 + DS-62 + DS-67)

**Pattern:** Template library → Default deny → Fine-grained permissions

**Example:**
1. Template 1: Default deny all (DS-62, DS-63)
2. Template 2: Allow DNS (DS-63)
3. Template 7: Database access with resourceNames (DS-63, DS-67)

**Why effective:** Production-ready security in minutes. Copy templates 1-2 (mandatory), add template 7 (database access), replace placeholders, deploy. Zero-config security for standard architectures.

---

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md

**7 new techniques to add:**

1. **DS-61: Security Tier Classification** - Define explicit security tiers from least to most restrictive
2. **DS-62: Default Deny + Selective Allow Pattern** - Start with deny-all, add specific allows
3. **DS-63: Template Library Organization** - Organize templates by use case with priority annotations
4. **DS-64: Compliance Framework Mapping** - Map technical controls to compliance requirements
5. **DS-65: Policy Enforcement Layer Documentation** - Admission control with policy-as-code
6. **DS-66: Service Mesh Security Integration** - Layered security (network + transport + app)
7. **DS-67: Resource-Scoped Permissions** - RBAC with resourceNames for fine-grained access

### For USE_CASE_LOOKUP.md

**Add to existing sections:**

**"Security & Compliance":**
- DS-61: Security Tier Classification (define security levels)
- DS-62: Default Deny + Selective Allow (security-first architecture)
- DS-64: Compliance Framework Mapping (map controls to CIS, NIST, SOC2)
- DS-65: Policy Enforcement Layer (OPA, Kyverno, policy-as-code)
- DS-66: Service Mesh Security (mTLS, AuthorizationPolicy, defense-in-depth)
- DS-67: Resource-Scoped Permissions (least-privilege RBAC)

**"Configuration & Templates":**
- DS-63: Template Library Organization (organize by priority and use case)

### For AI_AGENT_QUICK_START.md

**Example: Building a Security Implementation Skill**

```markdown
## Use Case: Kubernetes Security

**Goal:** Guide teams through production-grade Kubernetes security

**Techniques:**
1. DS-61: Security Tier Classification - Pod Security Standards (Privileged/Baseline/Restricted)
2. DS-62: Default Deny + Selective Allow - NetworkPolicy security architecture
3. DS-63: Template Library Organization - 8 network policy templates with priorities
4. DS-64: Compliance Framework Mapping - Map to CIS Benchmark and NIST
5. DS-65: Policy Enforcement Layer - OPA Gatekeeper for automated enforcement
6. DS-66: Service Mesh Security - Istio mTLS and AuthorizationPolicy
7. DS-67: Resource-Scoped Permissions - Fine-grained RBAC with resourceNames
8. DS-58: Best Practices Enumeration - 20 security best practices

**Structure:**
- SKILL.md: Standards, NetworkPolicies, RBAC, enforcement, compliance
- assets/network-policy-template.yaml: 8 production-ready templates
- references/rbac-patterns.md: 5 RBAC patterns, ServiceAccount best practices
```

### Key Insight: Defense-in-Depth Security Architecture

**Observation:** This skill demonstrates **defense-in-depth security** pattern:

1. **Security tiers** (Pod Security Standards) - Container security
2. **Default deny** (NetworkPolicy) - Network security
3. **Fine-grained RBAC** (resourceNames) - Access control security
4. **Policy enforcement** (OPA Gatekeeper) - Admission control security
5. **Service mesh** (Istio mTLS) - Transport security
6. **Compliance mapping** (CIS, NIST) - Audit readiness

**Design principle:** Multiple independent security layers. If one layer fails, others still provide protection.

**Comparison with single-layer security:**
- **Single layer:** Firewall only → bypass firewall = full access
- **Defense-in-depth:** Firewall + NetworkPolicy + RBAC + mTLS + Admission control → must bypass all 5 layers

**Attack scenario:**
1. Attacker compromises pod
2. **Layer 1 (Pod Security):** Can't escalate to root (runAsNonRoot: true)
3. **Layer 2 (NetworkPolicy):** Can't access other pods (default deny)
4. **Layer 3 (RBAC):** Can't read other secrets (resourceNames restriction)
5. **Layer 4 (mTLS):** Can't impersonate other services (identity verification)
6. **Layer 5 (OPA):** Can't create privileged pods (admission control blocks)

Result: Compromised pod has minimal blast radius.

### Application to Other Domains

**This pattern applies to:**
- Cloud security (Security Groups + IAM + KMS + CloudTrail + GuardDuty)
- Application security (WAF + Authentication + Authorization + Input validation + CSP)
- Database security (Network isolation + Auth + Encryption + Audit + Backup)
- API security (API Gateway + JWT + Rate limiting + WAF + Logging)

**Anti-pattern:** Single security control. Example: "We have a firewall, we're secure." Defense-in-depth assumes every layer can be breached.

---

## Summary

**k8s-security-policies** demonstrates **defense-in-depth security architecture** using:
- Security tier classification (Pod Security Standards: Privileged → Baseline → Restricted)
- Default deny + selective allow (NetworkPolicy security-first architecture)
- Template library organization (8 templates with priority annotations)
- Compliance framework mapping (CIS Benchmark, NIST)
- Policy enforcement layer (OPA Gatekeeper admission control)
- Service mesh security (Istio mTLS + AuthorizationPolicy)
- Resource-scoped permissions (RBAC with resourceNames)
- Best practices enumeration (20 security practices)

**Novel contribution:** Shows how to implement **multiple independent security layers** with **compliance-ready documentation** and **production-ready templates**.

**Key metrics:**
- **Security layers:** 6 (Pod Security, NetworkPolicy, RBAC, OPA, mTLS, AuthorizationPolicy)
- **Templates:** 8 (network policies covering common patterns)
- **RBAC patterns:** 5 (read-only, namespace-admin, deployment-manager, secret-reader, CI/CD)
- **Best practices:** 20 (10 general + 10 RBAC-specific)
- **Compliance frameworks:** 2 (CIS Kubernetes Benchmark, NIST CSF)
- **Total knowledge:** ~701 lines (comprehensive security guide)

**Recommended applications:**
- Cloud security architecture (AWS, Azure, GCP)
- Application security frameworks (OWASP implementation)
- Zero-trust architecture (network, identity, device)
- Compliance implementation (SOC2, ISO 27001, PCI-DSS)
- Infrastructure security (multi-tenant systems, SaaS platforms)

---

## Analysis Metadata

- **Analyzer:** Claude (Task 2.2 Priority 2)
- **Review Status:** Complete
- **Priority:** High (Production security, compliance, defense-in-depth)
- **Recommended for MASTER_TECHNIQUE_INDEX:** Yes (7 novel techniques)
- **Integration Complexity:** High (security patterns require careful implementation)
