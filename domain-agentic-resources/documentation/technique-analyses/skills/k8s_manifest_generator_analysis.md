# Technique Analysis: k8s-manifest-generator

**Resource Type:** Skill
**Path:** `skills/cloud-infrastructure/k8s-manifest-generator/`
**Category:** Cloud Infrastructure
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 2 references, 3 assets (2,664 total lines)

## Overview

This skill provides comprehensive guidance for generating production-ready Kubernetes manifests (Deployments, Services, ConfigMaps, Secrets, PVCs). It demonstrates sophisticated knowledge organization patterns with multi-tiered templates, progressive complexity scaffolding, and extensive reference documentation.

**Bundled Resources Analysis:**
- **SKILL.md:** 512 lines - Step-by-step workflow, patterns, troubleshooting
- **deployment-spec.md:** 754 lines - Complete Deployment API reference with best practices
- **service-spec.md:** 725 lines - Complete Service API reference with networking details
- **deployment-template.yaml:** 204 lines - Production-ready deployment template
- **service-template.yaml:** 172 lines - 7 service templates for different scenarios
- **configmap-template.yaml:** 297 lines - 7 ConfigMap templates with usage examples

**Total Knowledge:** 2,664 lines of production-grade Kubernetes guidance

---

## Identified Techniques

### Technique 1: Progressive Complexity Scaffolding (DS-51)

**Category:** DS (Domain-Specific)
**Pattern:** Start with minimal working examples, then progressively layer in production concerns
**Mapping:** NEW technique

**Implementation:**

The skill teaches K8s manifest creation in layers:

**Layer 1 - Minimal Working Example:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: myapp:1.0.0
```

**Layer 2 - Add Health & Resources:**
```yaml
# Previous content +
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
livenessProbe:
  httpGet:
    path: /health
    port: 8080
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
```

**Layer 3 - Add Security:**
```yaml
# Previous content +
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
```

**Layer 4 - Add High Availability:**
```yaml
# Previous content +
replicas: 3
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1
    maxUnavailable: 0
affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
    - weight: 100
      podAffinityTerm:
        labelSelector:
          matchLabels:
            app: my-app
        topologyKey: kubernetes.io/hostname
```

**Effectiveness:**
- Prevents overwhelming users with full complexity upfront
- Each layer solves one production concern (reliability, security, availability)
- User can stop at any layer based on their requirements
- Natural learning progression from development to production

---

### Technique 2: Multi-Tiered Template Library (DS-50)

**Category:** DS (Domain-Specific)
**Pattern:** Provide templates at different abstraction levels for different user needs
**Mapping:** NEW technique

**Implementation:**

**Tier 1 - Quick Examples (in SKILL.md):**
- Simple, inline examples for immediate understanding
- 10-20 lines each
- Copy-paste ready

**Tier 2 - Complete References (references/ directory):**
- Full API specifications with all fields explained
- 700+ lines each
- Educational, comprehensive

**Tier 3 - Production Templates (assets/ directory):**
- Battle-tested, production-ready templates
- 200-300 lines with extensive comments
- Ready for customization

**Example - Service templates organized by use case:**
1. ClusterIP (internal only)
2. LoadBalancer (external access)
3. NodePort (direct node access)
4. Headless (StatefulSet)
5. Multi-port with metrics
6. Session affinity
7. ExternalName

**Effectiveness:**
- Users can choose appropriate abstraction level
- Quick start → Deep learning → Production deployment
- Reduces cognitive load by separation of concerns

---

### Technique 3: Resource Specification Encyclopedia (DS-53)

**Category:** DS (Domain-Specific)
**Pattern:** Comprehensive field-by-field documentation with use cases, best practices, and gotchas
**Mapping:** NEW technique

**Implementation:**

From `deployment-spec.md`:

```markdown
#### Replica Management

**`replicas`** (integer, default: 1)
- Number of desired pod instances
- Best practice: Use 3+ for production high availability
- Can be scaled manually or via HorizontalPodAutoscaler

**`revisionHistoryLimit`** (integer, default: 10)
- Number of old ReplicaSets to retain for rollback
- Set to 0 to disable rollback capability
- Reduces storage overhead for long-running deployments

#### Update Strategy

**`strategy.type`** (string)
- `RollingUpdate` (default): Gradual pod replacement
- `Recreate`: Delete all pods before creating new ones

**`strategy.rollingUpdate.maxSurge`** (int or percent, default: 25%)
- Maximum pods above desired replicas during update
- Example: With 3 replicas and maxSurge=1, up to 4 pods during update

**`strategy.rollingUpdate.maxUnavailable`** (int or percent, default: 25%)
- Maximum pods below desired replicas during update
- Set to 0 for zero-downtime deployments
- Cannot be 0 if maxSurge is 0
```

**Structure per field:**
1. Field name and type
2. Default value
3. What it does (technical)
4. Why you'd use it (practical)
5. Common values/patterns
6. Gotchas and constraints

**Effectiveness:**
- Users understand not just "how" but "why"
- Reduces trial-and-error
- Makes trade-offs explicit

---

### Technique 4: Cloud Provider Annotation Dictionary (DS-52)

**Category:** DS (Domain-Specific)
**Pattern:** Platform-specific configuration organized by cloud provider
**Mapping:** NEW technique

**Implementation:**

From `service-spec.md`:

```yaml
# AWS-specific annotations
annotations:
  service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
  service.beta.kubernetes.io/aws-load-balancer-scheme: "internet-facing"
  service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled: "true"
  service.beta.kubernetes.io/aws-load-balancer-ssl-cert: "arn:aws:acm:..."
  service.beta.kubernetes.io/aws-load-balancer-backend-protocol: "http"

# Azure-specific annotations
annotations:
  service.beta.kubernetes.io/azure-load-balancer-internal: "true"
  service.beta.kubernetes.io/azure-pip-name: "my-public-ip"

# GCP-specific annotations
annotations:
  cloud.google.com/load-balancer-type: "Internal"
  cloud.google.com/backend-config: '{"default": "my-backend-config"}'
```

**Effectiveness:**
- Users can quickly find platform-specific requirements
- Prevents mixing incompatible annotations
- Makes multi-cloud differences explicit

---

### Technique 5: Production Readiness Checklist Pattern (ST-31)

**Category:** ST (Structural)
**Pattern:** Multiple domain-specific checklists embedded at decision points
**Mapping:** NEW technique (different from general pre-implementation checklists)

**Implementation:**

**Production Deployment Checklist:**
```markdown
- [ ] Set resource requests and limits
- [ ] Implement all three probe types (startup, liveness, readiness)
- [ ] Use specific image tags (not :latest)
- [ ] Configure security context (non-root, read-only filesystem)
- [ ] Set replica count >= 3 for HA
- [ ] Configure pod anti-affinity for spread
- [ ] Set appropriate update strategy (maxUnavailable: 0 for zero-downtime)
- [ ] Use ConfigMaps and Secrets for configuration
- [ ] Add standard labels and annotations
- [ ] Configure graceful shutdown (preStop hook, terminationGracePeriodSeconds)
- [ ] Set revisionHistoryLimit for rollback capability
- [ ] Use ServiceAccount with minimal RBAC permissions
```

**Security Checklist:**
```markdown
- [ ] Run as non-root user
- [ ] Drop all capabilities
- [ ] Use read-only root filesystem
- [ ] Disable privilege escalation
- [ ] Set seccomp profile
- [ ] Use Pod Security Standards
```

**Testing Checklist:**
```markdown
- [ ] Manifest passes dry-run validation
- [ ] All required fields are present
- [ ] Resource limits are reasonable
- [ ] Health checks are configured
- [ ] Security context is set
- [ ] Labels follow conventions
- [ ] Namespace exists or is created
```

**Service Production Checklist:**
```markdown
- [ ] Service type appropriate for use case
- [ ] Selector matches pod labels
- [ ] Named ports used for clarity
- [ ] Session affinity configured if needed
- [ ] Traffic policy set appropriately
- [ ] Load balancer annotations configured (if applicable)
- [ ] Source IP ranges restricted (for public services)
- [ ] Health check configuration validated
- [ ] Monitoring annotations added
- [ ] Network policies defined
```

**Effectiveness:**
- Prevents common production mistakes
- Each checklist is context-specific (deployment vs service vs security)
- Actionable, binary checks
- Can be copy-pasted into PRs or runbooks

---

### Technique 6: Troubleshooting Decision Tree (DS-54)

**Category:** DS (Domain-Specific)
**Pattern:** Systematic diagnostic flows for common failure modes
**Mapping:** NEW technique

**Implementation:**

From SKILL.md:

```markdown
## Troubleshooting

**Pods not starting:**
- Check image pull errors: `kubectl describe pod <pod-name>`
- Verify resource availability: `kubectl get nodes`
- Check events: `kubectl get events --sort-by='.lastTimestamp'`

**Service not accessible:**
- Verify selector matches pod labels: `kubectl get endpoints <service-name>`
- Check service type and port configuration
- Test from within cluster: `kubectl run debug --rm -it --image=busybox -- sh`

**ConfigMap/Secret not loading:**
- Verify names match in Deployment
- Check namespace
- Ensure resources exist: `kubectl get configmap,secret`
```

From `deployment-spec.md`:

```markdown
### Common Issues

**Pods not starting:**
\```bash
kubectl describe deployment <name>
kubectl get pods -l app=<app-name>
kubectl describe pod <pod-name>
kubectl logs <pod-name>
\```

**ImagePullBackOff:**
- Check image name and tag
- Verify imagePullSecrets
- Check registry credentials

**CrashLoopBackOff:**
- Check container logs
- Verify liveness probe is not too aggressive
- Check resource limits
- Verify application dependencies

**Deployment stuck in progress:**
- Check progressDeadlineSeconds
- Verify readiness probes
- Check resource availability
```

From `service-spec.md`:

```markdown
### Service not accessible

\```bash
# Check service exists
kubectl get service <service-name>

# Check endpoints (should show pod IPs)
kubectl get endpoints <service-name>

# Describe service
kubectl describe service <service-name>

# Check if pods match selector
kubectl get pods -l app=<app-name>
\```

**Common issues:**
- Selector doesn't match pod labels
- No pods running (endpoints empty)
- Ports misconfigured
- Network policy blocking traffic

### DNS resolution failing

\```bash
# Test DNS from pod
kubectl run debug --rm -it --image=busybox -- nslookup <service-name>

# Check CoreDNS
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl logs -n kube-system -l k8s-app=kube-dns
\```
```

**Effectiveness:**
- Symptom → Diagnostic commands → Likely causes
- Copy-pasteable commands
- Covers 80% of common issues
- Teaches debugging methodology

---

### Technique 7: Multi-Template Selection Guide (IT-29)

**Category:** IT (Interaction)
**Pattern:** Provide decision criteria for choosing between multiple templates
**Mapping:** NEW technique

**Implementation:**

**Service Type Selection:**

```markdown
### Choose the appropriate Service type:

**ClusterIP (internal only):**
Use cases:
- Internal microservice communication
- Database services
- Internal APIs
- Message queues

**NodePort:**
Use cases:
- Development/testing external access
- Small deployments without load balancer
- Direct node access requirements

Limitations:
- Limited port range (30000-32767)
- Must handle node failures
- No built-in load balancing across nodes

**LoadBalancer:**
Use cases:
- Production external access
- Automatic cloud integration
- Built-in load balancing

**ExternalName:**
Use cases:
- Accessing external services
- Service migration scenarios
- Multi-cluster service references
```

**ConfigMap Selection (7 templates):**
1. Simple Key-Value Configuration → For environment variables
2. Configuration File → For YAML/properties files
3. Multiple Configuration Files → For complex apps (nginx + app config)
4. JSON Configuration → For JSON-based apps
5. Environment-Specific Configuration → For multi-environment deployments
6. Script Configuration → For init scripts, health checks
7. Prometheus Configuration → For monitoring setup

**Effectiveness:**
- Eliminates "which one do I use?" paralysis
- Clear decision criteria
- Shows trade-offs upfront

---

### Technique 8: Reference Documentation Pointers (IT-28)

**Category:** IT (Interaction)
**Pattern:** Use explicit "See references/..." pointers to load deeper documentation only when needed
**Mapping:** NEW technique

**Implementation:**

From SKILL.md:

```markdown
**Reference:** See `references/deployment-spec.md` for detailed deployment options

**Reference:** See `references/service-spec.md` for service types and networking

**Reference:** See `assets/configmap-template.yaml` for examples
```

**Progressive Loading Path:**
1. User reads SKILL.md (512 lines)
2. Gets working examples
3. If needs more details → Opens references/ (700+ lines each)
4. If needs production template → Opens assets/ (200-300 lines each)

**Effectiveness:**
- Prevents information overload
- User controls depth of learning
- Claude can load references on-demand
- Keeps main skill concise

---

### Technique 9: Quality-of-Service Automatic Classification (DS-55)

**Category:** DS (Domain-Specific)
**Pattern:** Explain how system automatically derives classifications from user configuration
**Mapping:** NEW technique

**Implementation:**

From `deployment-spec.md`:

```markdown
#### Resource Management

**QoS Classes (determined automatically):**

1. **Guaranteed**: requests = limits for all containers
   - Highest priority
   - Last to be evicted

2. **Burstable**: requests < limits or only requests set
   - Medium priority
   - Evicted before Guaranteed

3. **BestEffort**: No requests or limits set
   - Lowest priority
   - First to be evicted

**Best practices:**
- Always set requests in production
- Set limits to prevent resource monopolization
- Memory limits should be 1.5-2x requests
- CPU limits can be higher for bursty workloads
```

**Effectiveness:**
- Users understand consequences of their resource settings
- Makes implicit system behavior explicit
- Guides decision-making (production = Guaranteed)

---

### Technique 10: Anti-Pattern Warnings (ST-32)

**Category:** ST (Structural)
**Pattern:** Explicit "never do this" warnings with explanations
**Mapping:** NEW technique (extension of existing anti-pattern documentation)

**Implementation:**

**Image Tag Anti-Pattern:**
```markdown
**Best practices to apply:**
- Use specific image tags (never `:latest`)
```

**Security Anti-Patterns:**
```markdown
**Security considerations:**
- Never commit secrets to Git in plain text
- Use Sealed Secrets, External Secrets Operator, or Vault
```

**HostPath Anti-Pattern:**
```yaml
# HostPath (avoid in production)
- name: host-data
  hostPath:
    path: /data
    type: DirectoryOrCreate
```

**Effectiveness:**
- Prevents common mistakes
- Clear, actionable guidance
- Explains why (security, reliability, reproducibility)

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Progressive Complexity Scaffolding (DS-51)

**Description:** Build up from minimal working examples to production-grade configurations in discrete layers

**Implementation:**
1. Layer 1: Minimal working example (development)
2. Layer 2: Add observability (health checks, metrics)
3. Layer 3: Add security (non-root, read-only, capabilities)
4. Layer 4: Add high availability (replicas, anti-affinity)
5. Layer 5: Add performance tuning (resources, graceful shutdown)

**Use case:** Teaching complex infrastructure-as-code where full production templates are overwhelming

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-51

---

### Pattern 2: Multi-Tiered Template Library (DS-50)

**Description:** Provide same concept at multiple abstraction levels for different user needs

**Tiers:**
- Quick examples (10-20 lines, inline in docs)
- Complete references (700+ lines, comprehensive API docs)
- Production templates (200-300 lines, battle-tested)

**Use case:** Users at different skill levels or with different time constraints

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-50

---

### Pattern 3: Resource Specification Encyclopedia (DS-53)

**Description:** Document every field with: name, type, default, purpose, use cases, constraints, best practices

**Implementation:**
```markdown
**`fieldName`** (type, default: value)
- Technical description
- Practical use case
- Common values/patterns
- Constraints and gotchas
- Best practices
```

**Use case:** Complex APIs where field interactions and defaults aren't obvious

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-53

---

### Pattern 4: Cloud Provider Annotation Dictionary (DS-52)

**Description:** Platform-specific configuration organized by provider with examples

**Implementation:**
- AWS section with all AWS-specific annotations
- Azure section with all Azure-specific annotations
- GCP section with all GCP-specific annotations

**Use case:** Multi-cloud applications, platform migrations, cross-platform knowledge

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-52

---

### Pattern 5: Production Readiness Checklist Pattern (ST-31)

**Description:** Multiple context-specific checklists embedded at decision points (not just one pre-implementation checklist)

**Types:**
- Production deployment checklist
- Security checklist
- Testing checklist
- Service configuration checklist
- Performance tuning checklist

**Use case:** Complex systems with multiple production concerns

**Proposed category:** ST (Structural)
**Proposed code:** ST-31

---

### Pattern 6: Troubleshooting Decision Tree (DS-54)

**Description:** Symptom → Diagnostic commands → Likely causes for common failure modes

**Structure:**
```markdown
**Symptom:**
\```bash
diagnostic command 1
diagnostic command 2
\```

**Common causes:**
- Cause 1 with fix
- Cause 2 with fix
```

**Use case:** Complex distributed systems with multiple failure modes

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-54

---

### Pattern 7: Multi-Template Selection Guide (IT-29)

**Description:** Explicit decision criteria for choosing between multiple templates

**Structure:**
1. List all template options
2. For each: Use cases, limitations, when to use
3. Decision tree or comparison table

**Use case:** When multiple valid approaches exist for same problem

**Proposed category:** IT (Interaction)
**Proposed code:** IT-29

---

### Pattern 8: Reference Documentation Pointers (IT-28)

**Description:** "See references/..." pointers for on-demand loading of deeper documentation

**Implementation:**
- Main doc: Concise with working examples
- References: Comprehensive deep dives
- Explicit pointers: "See X for details on Y"

**Use case:** Progressive disclosure in documentation-heavy domains

**Proposed category:** IT (Interaction)
**Proposed code:** IT-28

---

### Pattern 9: Quality-of-Service Automatic Classification (DS-55)

**Description:** Explain how system automatically derives classifications from user inputs

**Example:** Kubernetes QoS classes based on resource requests/limits

**Use case:** Systems with implicit behavior based on explicit configuration

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-55

---

### Pattern 10: Anti-Pattern Warnings (ST-32)

**Description:** Explicit "never do this" statements with explanations why

**Implementation:**
- Clear "never" or "avoid in production" statements
- Brief explanation of consequences
- Alternative approach if applicable

**Use case:** Domains with common mistakes that have serious consequences

**Proposed category:** ST (Structural)
**Proposed code:** ST-32

---

## Multi-Technique Combinations

### Combination 1: Progressive Learning Pipeline

**Techniques:** DS-51 (Progressive Complexity) + IT-28 (Reference Pointers) + DS-50 (Multi-Tiered Templates)

**How they work together:**
1. User reads main SKILL.md with simple examples (progressive complexity)
2. Sees "Reference: deployment-spec.md for details" (reference pointers)
3. Opens reference to find comprehensive encyclopedia (multi-tiered templates)
4. Returns to SKILL.md with deeper understanding

**Effectiveness:** Natural learning progression without forced linearity

---

### Combination 2: Production Deployment Safety Net

**Techniques:** ST-31 (Production Checklists) + ST-32 (Anti-Pattern Warnings) + DS-53 (Specification Encyclopedia)

**How they work together:**
1. Anti-patterns prevent obvious mistakes
2. Specification encyclopedia explains "why" for each setting
3. Production checklist ensures nothing was forgotten

**Effectiveness:** Multiple complementary safety mechanisms

---

### Combination 3: Multi-Cloud Decision Support

**Techniques:** DS-52 (Cloud Provider Dictionary) + IT-29 (Template Selection Guide) + DS-50 (Multi-Tiered Templates)

**How they work together:**
1. Selection guide helps choose service type
2. Cloud provider dictionary provides platform-specific annotations
3. Multi-tiered templates provide working examples at right abstraction level

**Effectiveness:** Reduces friction in multi-cloud scenarios

---

### Combination 4: Troubleshooting Workflow

**Techniques:** DS-54 (Troubleshooting Decision Tree) + DS-53 (Specification Encyclopedia) + IT-28 (Reference Pointers)

**How they work together:**
1. Decision tree diagnoses symptom
2. Points to relevant specification section
3. User loads reference docs for detailed field explanations

**Effectiveness:** Fast triage → Deep understanding

---

## Notes for Integration

### Impact on MASTER_TECHNIQUE_INDEX.md

**New Techniques to Add:**
- DS-50: Multi-Tiered Template Library
- DS-51: Progressive Complexity Scaffolding
- DS-52: Cloud Provider Annotation Dictionary
- DS-53: Resource Specification Encyclopedia
- DS-54: Troubleshooting Decision Tree
- DS-55: Quality-of-Service Automatic Classification
- IT-28: Reference Documentation Pointers
- IT-29: Multi-Template Selection Guide
- ST-31: Production Readiness Checklist Pattern
- ST-32: Anti-Pattern Warnings

**Total:** 10 novel techniques

---

### Key Insights

1. **Knowledge Encyclopedia Pattern:** This skill demonstrates a "production knowledge package" pattern where comprehensive domain knowledge is organized for on-demand access

2. **Multi-Level Abstraction:** Different users need different abstraction levels - provide all levels and let users choose

3. **Production-First Mindset:** Templates and examples are production-grade by default, not "toy examples that need hardening later"

4. **Platform Awareness:** Explicit handling of platform differences (AWS vs Azure vs GCP) prevents trial-and-error

5. **Safety Through Multiple Mechanisms:** Checklists + Anti-patterns + Best practices + Complete specs create overlapping safety nets

---

### Recommended Use Cases

**Use DS-51 (Progressive Complexity Scaffolding) when:**
- Teaching complex infrastructure concepts
- Users need to go from development to production
- Full production templates are overwhelming

**Use DS-50 (Multi-Tiered Templates) when:**
- Same concept applies to multiple user skill levels
- Users have different time constraints (quick start vs deep learning)

**Use DS-53 (Specification Encyclopedia) when:**
- Complex APIs with many fields and interactions
- Defaults and constraints aren't intuitive
- Users need to understand "why" not just "how"

**Use ST-31 (Production Checklists) when:**
- Multiple concerns must be addressed (security, performance, reliability)
- Common mistakes have serious production consequences
- System is too complex to remember all requirements

---

## Summary

The k8s-manifest-generator skill is a masterclass in **production knowledge packaging**. With 2,664 lines of bundled documentation across 5 files, it provides:

1. **Progressive disclosure** - From simple examples → complete references → production templates
2. **Multi-cloud awareness** - Platform-specific guidance without mixing concerns
3. **Safety mechanisms** - Checklists, anti-patterns, and best practices create overlapping guardrails
4. **Troubleshooting methodology** - Not just "what" but "how to diagnose"

The 10 novel techniques identified focus on **knowledge organization** rather than prompting structure, making this skill valuable for understanding how to package domain expertise for production use.

**Complexity Score:** 5/5 (Production-grade infrastructure knowledge with sophisticated organization)

**Novel Technique Count:** 10

**Primary Innovation:** Multi-tiered knowledge architecture (Quick Examples → Complete References → Production Templates) with explicit pointers for progressive disclosure
