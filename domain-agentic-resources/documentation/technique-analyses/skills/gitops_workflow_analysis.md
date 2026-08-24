# Technique Analysis: gitops-workflow

**Resource Type:** Skill
**Path:** `skills/cloud-infrastructure/gitops-workflow/`
**Date Analyzed:** 2025-12-22
**Category:** Cloud Infrastructure - GitOps/CD
**Bundled Resources:** 2 references (argocd-setup.md: 135 lines, sync-policies.md: 132 lines)
**Total Knowledge:** ~553 lines (286 in SKILL.md + 267 in references)
**Complexity:** 4/5 (Production-grade GitOps implementation with multi-tool support)

---

## Resource Summary

**Purpose:** Enable Claude to implement complete GitOps workflows using ArgoCD and Flux CD for automated, declarative Kubernetes deployments with continuous reconciliation following OpenGitOps principles.

**Key Innovation:** Multi-tool comparison (ArgoCD vs Flux) + principle-driven guidance + environment-specific policies

**Architecture:**
- **SKILL.md (286 lines):** Core concepts, ArgoCD setup, Flux setup, progressive delivery, secret management
- **references/argocd-setup.md (135 lines):** Installation methods, SSO, RBAC, CLI configuration
- **references/sync-policies.md (132 lines):** Automated/manual sync, health checks, sync options

**Use Case:** When implementing GitOps practices, automating Kubernetes deployments, setting up declarative infrastructure management, configuring continuous reconciliation, or managing multi-cluster deployments.

---

## Identified Techniques

### Technique 1: Multi-Tool Comparison Pattern
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Present parallel implementations for different tools solving the same problem
- **Example from resource:**
```markdown
## ArgoCD Setup
### 1. Installation
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

## Flux CD Setup
### 1. Installation
flux bootstrap github --owner=org --repository=gitops-repo

## Sync Policies

### Auto-Sync Configuration
**ArgoCD:**
syncPolicy:
  automated:
    prune: true
    selfHeal: true

**Flux:**
spec:
  interval: 1m
  prune: true
  wait: true
```
- **Maps to existing:** NEW - **DS-53: Multi-Tool Comparison Pattern**
- **Effectiveness:** Enables tool-agnostic understanding. Users learn the concept (GitOps sync policies) and see how it's implemented in both ArgoCD and Flux. Helps choose the right tool for their context.

### Technique 2: Progressive Delivery Patterns
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Document specific progressive delivery strategies with quantitative configurations
- **Example from resource:**
```yaml
## Progressive Delivery

### Canary Deployment with ArgoCD Rollouts
strategy:
  canary:
    steps:
    - setWeight: 20
    - pause: {duration: 1m}
    - setWeight: 50
    - pause: {duration: 2m}
    - setWeight: 100

### Blue-Green Deployment
strategy:
  blueGreen:
    activeService: my-app
    previewService: my-app-preview
    autoPromotionEnabled: false
```
- **Maps to existing:** NEW - **DS-54: Progressive Delivery Patterns**
- **Effectiveness:** Provides specific rollout strategies with quantitative parameters (20% → 50% → 100%, pause durations). Not just "use canary" but "how to configure canary". Includes blue-green alternative.

### Technique 3: Principle-Driven Instructions
- **Category:** ST (Structural Techniques) - NEW
- **Pattern:** Start with foundational principles before implementation details
- **Example from resource:**
```markdown
## OpenGitOps Principles

1. **Declarative** - Entire system described declaratively
2. **Versioned and Immutable** - Desired state stored in Git
3. **Pulled Automatically** - Software agents pull desired state
4. **Continuously Reconciled** - Agents reconcile actual vs desired state

[Then proceed to implementation]
```
- **Maps to existing:** NEW - **ST-31: Principle-Driven Instructions**
- **Effectiveness:** Establishes the "why" before the "how". OpenGitOps principles provide decision-making framework. When implementation choices arise, refer back to principles. Example: Why use automated sync? Because of "Continuously Reconciled" principle.

### Technique 4: Repository Structure Templates
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Provide directory structure templates showing organizational patterns
- **Example from resource:**
```markdown
### 2. Repository Structure

gitops-repo/
├── apps/
│   ├── production/
│   │   ├── app1/
│   │   │   ├── kustomization.yaml
│   │   │   └── deployment.yaml
│   │   └── app2/
│   └── staging/
├── infrastructure/
│   ├── ingress-nginx/
│   ├── cert-manager/
│   └── monitoring/
└── argocd/
    ├── applications/
    └── projects/
```
- **Maps to existing:** NEW - **DS-55: Repository Structure Templates**
- **Effectiveness:** Shows *where* to put things, not just *what* to create. Separates apps (application code) from infrastructure (cluster services) from argocd (GitOps config). Enables consistent organization.

### Technique 5: Sync Policy Configuration
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Comprehensive configuration documentation for sync behavior
- **Example from resource:**
```yaml
syncPolicy:
  automated:
    prune: true      # Delete resources not in Git
    selfHeal: true   # Reconcile manual changes
    allowEmpty: false
  retry:
    limit: 5
    backoff:
      duration: 5s
      factor: 2
      maxDuration: 3m
```
- **Maps to existing:** NEW - **DS-56: Sync Policy Configuration**
- **Effectiveness:** Each configuration option has inline comment explaining what it does. Covers automated sync, retry policies, backoff strategies. Shows complete policy structure, not just individual options.

### Technique 6: Health Assessment Customization
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Custom health check scripts for domain-specific resource types
- **Example from resource:**
```yaml
resource.customizations.health.MyCustomResource: |
  hs = {}
  if obj.status ~= nil then
    if obj.status.conditions ~= nil then
      for i, condition in ipairs(obj.status.conditions) do
        if condition.type == "Ready" and condition.status == "False" then
          hs.status = "Degraded"
          hs.message = condition.message
          return hs
        end
        if condition.type == "Ready" and condition.status == "True" then
          hs.status = "Healthy"
          hs.message = condition.message
          return hs
        end
      end
    end
  end
  hs.status = "Progressing"
  hs.message = "Waiting for status"
  return hs
```
- **Maps to existing:** NEW - **DS-57: Health Assessment Customization**
- **Effectiveness:** Shows how to define "healthy" for custom resources. Lua script template with status mapping (Degraded, Healthy, Progressing). Enables GitOps for CRDs (Custom Resource Definitions).

### Technique 7: Reference Pointers with Context
- **Category:** IT (Interaction Techniques) - EXISTING (variation)
- **Pattern:** Inline pointers to bundled references with contextual guidance
- **Example from resource:**
```markdown
**Reference:** See `references/argocd-setup.md` for detailed setup

**Reference:** See `references/sync-policies.md`
```
- **Maps to existing:** IT-20 (Reference Pointers) - variation with context
- **Effectiveness:** Doesn't just say "see reference" but provides specific file path. Appears at logical points in the flow (after basic setup → detailed setup reference).

### Technique 8: Best Practices Enumeration
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Numbered lists of best practices consolidating tribal knowledge
- **Example from resource:**
```markdown
## Best Practices

1. **Use separate repos or branches** for different environments
2. **Implement RBAC** for Git repositories
3. **Enable notifications** for sync failures
4. **Use health checks** for custom resources
5. **Implement approval gates** for production
6. **Keep secrets out of Git** (use External Secrets)
7. **Use App of Apps pattern** for organization
8. **Tag releases** for easy rollback
9. **Monitor sync status** with alerts
10. **Test changes** in staging first
```
- **Maps to existing:** NEW - **DS-58: Best Practices Enumeration**
- **Effectiveness:** Consolidates 10 best practices learned from production experience. Bold key phrase + explanation. Appears in multiple sections (main guide has 10, argocd-setup has 10, sync-policies has 10). Total: 30 best practices across skill.

### Technique 9: Troubleshooting Command Sequences
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Show diagnostic commands followed by fix commands
- **Example from resource:**
```markdown
## Troubleshooting

**Sync failures:**
argocd app get my-app
argocd app sync my-app --prune

**Out of sync status:**
argocd app diff my-app
argocd app sync my-app --force
```
- **Maps to existing:** NEW - **DS-59: Troubleshooting Command Sequences**
- **Effectiveness:** Problem → Investigation → Fix pattern. First command diagnoses (`argocd app get`, `argocd app diff`), second command fixes (`sync --prune`, `sync --force`). Teaches debugging workflow.

### Technique 10: Environment-Specific Guidance
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Different recommendations for non-production vs production environments
- **Example from resource:**
```markdown
## Best Practices

1. Use automated sync for non-production
2. Require manual approval for production
...
8. Use prune with caution in production
9. Test sync policies in staging
```
- **Maps to existing:** NEW - **DS-60: Environment-Specific Guidance**
- **Effectiveness:** Acknowledges that production has different risk tolerance. "Automated sync for non-prod" enables fast iteration. "Manual approval for prod" prevents accidental changes. "Prune with caution in prod" prevents accidental deletions.

### Technique 11: App of Apps Pattern
- **Category:** DS (Domain-Specific) - EXISTING (domain pattern)
- **Pattern:** Meta-application that manages other applications
- **Example from resource:**
```yaml
### 4. App of Apps Pattern

apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: applications
spec:
  source:
    path: argocd/applications  # Points to directory of app definitions
  destination:
    namespace: argocd
```
- **Maps to existing:** DS-04 (Recursive structures) or Architecture pattern
- **Effectiveness:** Single root application manages all others. Bootstrap once, all apps sync automatically. Common GitOps pattern for organization.

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Multi-Tool Comparison Pattern (DS-53)

**Description:** Present parallel implementations for different tools solving the same problem, enabling tool-agnostic understanding and informed tool selection.

**Implementation:**
```markdown
## Problem: [Deployment Strategy]

### Tool 1: [ArgoCD]
[Implementation code]

### Tool 2: [Flux]
[Implementation code]

[Comparison guidance]
```

**Use case:**
- Infrastructure-as-code tools (Terraform vs Pulumi vs CDK)
- CI/CD platforms (GitHub Actions vs GitLab CI vs Jenkins)
- Monitoring solutions (Prometheus vs Datadog vs New Relic)
- Container orchestration (Kubernetes vs Docker Swarm vs Nomad)

**Why it's novel:** Teaches the *pattern* (GitOps sync), not the *tool* (ArgoCD only). Users understand the concept, then choose tool based on their context. Prevents tool lock-in in educational content.

**Proposed category:** DS (Domain-Specific - DevOps)
**Proposed code:** DS-53

---

### Pattern 2: Progressive Delivery Patterns (DS-54)

**Description:** Document specific progressive delivery strategies (canary, blue-green) with quantitative parameters (weights, pause durations).

**Implementation:**
```yaml
strategy:
  canary:
    steps:
    - setWeight: [20]%      # Traffic percentage
    - pause: {duration: [1m]}  # Observation window
    - setWeight: [50]%
    - pause: {duration: [2m]}
    - setWeight: [100]%
```

**Use case:**
- Kubernetes deployments (rollouts, canary, blue-green)
- Feature flag rollouts (1% → 10% → 50% → 100%)
- Database migrations (pilot → staged → full)
- Infrastructure changes (region-by-region rollout)

**Why it's novel:** Not just "use canary deployment" but "use these specific weights and pause durations". Quantitative guidance prevents guessing. Shows gradual rollout math.

**Proposed category:** DS (Domain-Specific - Deployment)
**Proposed code:** DS-54

---

### Pattern 3: Principle-Driven Instructions (ST-31)

**Description:** Start with foundational principles (3-5 core tenets) before implementation details, providing decision-making framework.

**Implementation:**
```markdown
## [Domain] Principles

1. **[Principle 1]** - [Description]
2. **[Principle 2]** - [Description]
3. **[Principle 3]** - [Description]
4. **[Principle 4]** - [Description]

[Implementation follows principles]
```

**Use case:**
- OpenGitOps principles (Declarative, Versioned, Pulled, Reconciled)
- Twelve-Factor App (Config in env, Stateless processes, etc.)
- REST API principles (Stateless, Cacheable, Uniform interface)
- Security principles (Least privilege, Defense in depth, Fail secure)

**Why it's novel:** Provides "why" before "how". When implementation choice arises, refer to principles. Example: "Why automated sync?" → "Continuously Reconciled principle". Principles guide decisions when docs don't have exact answer.

**Proposed category:** ST (Structural Techniques - Foundational)
**Proposed code:** ST-31

---

### Pattern 4: Repository Structure Templates (DS-55)

**Description:** Provide ASCII directory tree templates showing where to organize different types of content.

**Implementation:**
```
project-repo/
├── [category-1]/
│   ├── [subcategory-a]/
│   │   ├── [file-type-1]
│   │   └── [file-type-2]
│   └── [subcategory-b]/
├── [category-2]/
│   ├── [subcategory-c]/
│   └── [subcategory-d]/
└── [category-3]/
```

**Use case:**
- GitOps repository structure (apps/, infrastructure/, argocd/)
- Monorepo organization (services/, libs/, tools/, docs/)
- Documentation structure (guides/, references/, tutorials/, api/)
- Data science projects (data/, notebooks/, models/, reports/)

**Why it's novel:** Shows *where* (directory structure), not just *what* (file contents). Prevents "where should I put this?" questions. Enables consistent organization across teams.

**Proposed category:** DS (Domain-Specific - Project Organization)
**Proposed code:** DS-55

---

### Pattern 5: Sync Policy Configuration (DS-56)

**Description:** Comprehensive configuration documentation with inline comments explaining each option.

**Implementation:**
```yaml
configSection:
  option1: value      # What this option does
  option2: value      # Why you'd enable this
  option3:
    suboption1: val   # Effect of this setting
    suboption2: val   # Trade-offs involved
```

**Use case:**
- GitOps sync policies (prune, selfHeal, retry)
- CI/CD pipeline configuration (triggers, caching, artifacts)
- Database connection pools (min, max, timeout, retry)
- API rate limiting (limit, window, burst, fallback)

**Why it's novel:** Configuration as documentation. Each option has inline comment. Shows complete policy structure (not just individual options). Includes retry/backoff strategies.

**Proposed category:** DS (Domain-Specific - Configuration)
**Proposed code:** DS-56

---

### Pattern 6: Health Assessment Customization (DS-57)

**Description:** Custom health check scripts (Lua, JavaScript, etc.) for domain-specific resource types, defining "healthy" programmatically.

**Implementation:**
```lua
health_check = function(obj)
  status = {}
  if obj.status.condition == "Ready" then
    status.health = "Healthy"
  else
    status.health = "Degraded"
  end
  status.message = obj.status.message
  return status
end
```

**Use case:**
- Kubernetes CRD health checks (ArgoCD, Flux)
- Service mesh health (Istio, Linkerd)
- Custom API health endpoints
- Infrastructure readiness checks (Terraform, Pulumi)

**Why it's novel:** Programmatic health definition for custom resources. Not just HTTP 200 = healthy. Supports complex status conditions. Template shows status mapping (Progressing → Healthy → Degraded).

**Proposed category:** DS (Domain-Specific - Health Checks)
**Proposed code:** DS-57

---

### Pattern 7: Best Practices Enumeration (DS-58)

**Description:** Numbered lists (typically 10 items) of best practices consolidating tribal knowledge, with bold key phrase + explanation.

**Implementation:**
```markdown
## Best Practices

1. **[Key action/principle]** - [Explanation/rationale]
2. **[Key action/principle]** - [Explanation/rationale]
...
10. **[Key action/principle]** - [Explanation/rationale]
```

**Use case:**
- Security best practices (OWASP top 10)
- API design best practices (REST, GraphQL)
- Database optimization best practices
- Code review best practices
- DevOps/SRE best practices

**Why it's novel:** Consolidates production experience into actionable list. Bold key phrase enables scanning. Number (10) provides complete but not overwhelming scope. Appears multiple times (main: 10, argocd: 10, sync: 10 = 30 total).

**Proposed category:** DS (Domain-Specific - Best Practices)
**Proposed code:** DS-58

---

### Pattern 8: Troubleshooting Command Sequences (DS-59)

**Description:** Show diagnostic command followed by fix command for common problems. Problem → Investigation → Fix pattern.

**Implementation:**
```markdown
**[Problem description]:**
[diagnostic command]  # Shows what's wrong
[fix command]         # Resolves the issue
```

**Use case:**
- Kubernetes debugging (get → describe → logs → exec)
- Git troubleshooting (status → diff → reset → clean)
- Database issues (EXPLAIN → CREATE INDEX → VACUUM)
- Network debugging (ping → traceroute → dig → telnet)

**Why it's novel:** Teaches debugging workflow, not just fix commands. First command gathers evidence, second command applies fix. Shows progression from diagnosis to resolution.

**Proposed category:** DS (Domain-Specific - Troubleshooting)
**Proposed code:** DS-59

---

### Pattern 9: Environment-Specific Guidance (DS-60)

**Description:** Different recommendations for non-production vs production environments based on risk tolerance.

**Implementation:**
```markdown
**Non-production:**
- [Faster iteration, more automation, less gates]

**Production:**
- [Safety gates, manual approvals, careful automation]
```

**Use case:**
- Deployment automation (auto-sync dev, manual prod)
- Database migrations (auto staging, manual prod)
- Feature flags (100% in dev, gradual in prod)
- Monitoring alerts (noisy in dev, actionable in prod)

**Why it's novel:** Acknowledges different risk profiles. Dev/staging: fast feedback > safety. Production: safety > speed. Prevents one-size-fits-all recommendations that are either too risky (prod) or too slow (dev).

**Proposed category:** DS (Domain-Specific - Environment Management)
**Proposed code:** DS-60

---

## Multi-Technique Combinations

### Combination 1: Principles + Patterns (ST-31 + DS-54)

**Pattern:** Start with OpenGitOps principles → Apply to progressive delivery patterns

**Example:**
1. Principle: "Continuously Reconciled" (ST-31)
2. Implementation: Progressive delivery with automatic rollback on health degradation (DS-54)
3. Connection: Health checks enable automated reconciliation during rollout

**Why effective:** Principles justify pattern choices. "Why pause between canary stages?" → "To allow reconciliation to detect health degradation before proceeding."

---

### Combination 2: Multi-Tool + Best Practices (DS-53 + DS-58)

**Pattern:** Show ArgoCD and Flux implementations → Provide tool-agnostic best practices

**Example:**
1. ArgoCD sync policy (DS-53)
2. Flux sync policy (DS-53)
3. Best practice: "Use automated sync for non-production" (DS-58)
4. Applies to both tools

**Why effective:** Best practices transcend tool choice. Learn pattern once, apply to either tool.

---

### Combination 3: Structure + Policy + Troubleshooting (DS-55 + DS-56 + DS-59)

**Pattern:** Repository structure → Sync policies → Troubleshooting when things break

**Example:**
1. Repository structure template (DS-55): `gitops-repo/apps/production/my-app/`
2. Sync policy (DS-56): `automated: {prune: true, selfHeal: true}`
3. Troubleshooting (DS-59): Sync failure → `argocd app get` → `argocd app sync --prune`

**Why effective:** End-to-end workflow. Organize (structure) → Configure (policy) → Debug (troubleshooting). Covers full lifecycle.

---

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md

**8 new techniques to add:**

1. **DS-53: Multi-Tool Comparison Pattern** - Parallel implementations for different tools solving same problem
2. **DS-54: Progressive Delivery Patterns** - Canary/blue-green with quantitative parameters
3. **ST-31: Principle-Driven Instructions** - Foundational principles before implementation
4. **DS-55: Repository Structure Templates** - Directory tree templates for organization
5. **DS-56: Sync Policy Configuration** - Comprehensive config with inline comments
6. **DS-57: Health Assessment Customization** - Custom health check scripts for CRDs
7. **DS-58: Best Practices Enumeration** - Numbered lists of tribal knowledge (typically 10)
8. **DS-59: Troubleshooting Command Sequences** - Diagnostic → Fix command patterns
9. **DS-60: Environment-Specific Guidance** - Different recommendations for dev/prod

### For USE_CASE_LOOKUP.md

**Add to existing sections:**

**"Infrastructure & DevOps":**
- DS-53: Multi-Tool Comparison (compare IaC tools, CI/CD platforms)
- DS-54: Progressive Delivery (canary, blue-green deployments)
- DS-55: Repository Structure Templates (monorepo, GitOps structure)
- DS-56: Sync Policy Configuration (GitOps, CI/CD pipelines)
- DS-58: Best Practices Enumeration (DevOps, SRE practices)
- DS-60: Environment-Specific Guidance (dev vs prod policies)

**"Debugging & Troubleshooting":**
- DS-59: Troubleshooting Command Sequences (Kubernetes, Git, database debugging)

**"Teaching & Documentation":**
- ST-31: Principle-Driven Instructions (teach foundational principles first)

**"Custom Integrations":**
- DS-57: Health Assessment Customization (CRD health checks, custom APIs)

### For AI_AGENT_QUICK_START.md

**Example: Building a GitOps Implementation Skill**

```markdown
## Use Case: Infrastructure Automation

**Goal:** Guide teams through GitOps implementation

**Techniques:**
1. ST-31: Principle-Driven Instructions - Start with OpenGitOps principles
2. DS-53: Multi-Tool Comparison - Show both ArgoCD and Flux
3. DS-55: Repository Structure Templates - Provide standard directory layout
4. DS-56: Sync Policy Configuration - Document sync behavior comprehensively
5. DS-54: Progressive Delivery Patterns - Include canary/blue-green strategies
6. DS-58: Best Practices Enumeration - Consolidate production learnings
7. DS-59: Troubleshooting Command Sequences - Debug common issues
8. DS-60: Environment-Specific Guidance - Different policies for dev/prod

**Structure:**
- SKILL.md: Principles, basic setup, progressive delivery
- references/tool-setup.md: Detailed installation and configuration
- references/policies.md: Sync policies, health checks, best practices
```

### Key Insight: Production-Grade Documentation Pattern

**Observation:** This skill demonstrates **production-grade documentation** pattern:

1. **Principles** (OpenGitOps) → Foundation for decisions
2. **Multi-tool support** (ArgoCD + Flux) → Tool-agnostic understanding
3. **Structure templates** → Where to put things
4. **Configuration docs** → How to configure
5. **Best practices** (30 total) → What NOT to do
6. **Troubleshooting** → How to fix when broken
7. **Environment guidance** → Different rules for dev/prod

**Design principle:** Cover full lifecycle from first principles to production debugging.

**Comparison with other skills:**
- **helm-chart-scaffolding:** Focused on one tool (Helm)
- **k8s-manifest-generator:** Focused on one task (manifest generation)
- **gitops-workflow:** Covers full GitOps lifecycle, multiple tools, principles to debugging

This is **comprehensive domain coverage** vs **narrow tool coverage**.

### Application to Other Domains

**This pattern applies to:**
- Database administration (principles → PostgreSQL vs MySQL → schema design → troubleshooting)
- API development (REST principles → FastAPI vs Flask → structure → debugging)
- Frontend frameworks (component principles → React vs Vue → project structure → performance)
- Testing strategies (testing pyramid → Jest vs Pytest → organization → debugging)

**Anti-pattern:** Tool-specific tutorials without principles or troubleshooting. Good for getting started, bad for production.

---

## Summary

**gitops-workflow** demonstrates **production-grade documentation** using:
- Principle-driven instruction (OpenGitOps principles → implementation)
- Multi-tool comparison (ArgoCD and Flux side-by-side)
- Repository structure templates (where to organize)
- Comprehensive configuration docs (sync policies, health checks)
- Best practices enumeration (30 practices across 3 files)
- Troubleshooting sequences (diagnostic → fix)
- Environment-specific guidance (dev vs prod policies)

**Novel contribution:** Shows how to create **complete domain coverage** (principles → implementation → debugging) with **tool-agnostic understanding** (patterns > specific tools).

**Key metrics:**
- **Tools covered:** 2 (ArgoCD, Flux)
- **Best practices:** 30 (10 in main + 10 in argocd + 10 in sync-policies)
- **Principles documented:** 4 (OpenGitOps core principles)
- **Delivery strategies:** 2 (Canary, Blue-Green)
- **Total knowledge:** ~553 lines (comprehensive GitOps guide)

**Recommended applications:**
- Infrastructure-as-code guides (Terraform, Pulumi, CDK)
- CI/CD platform documentation (GitHub Actions, GitLab CI, Jenkins)
- Database administration guides (PostgreSQL, MySQL, MongoDB)
- API framework comparisons (FastAPI, Flask, Express, NestJS)
- Testing framework guides (Jest, Pytest, JUnit, RSpec)

---

## Analysis Metadata

- **Analyzer:** Claude (Task 2.2 Priority 2)
- **Review Status:** Complete
- **Priority:** High (Cloud infrastructure, production GitOps patterns)
- **Recommended for MASTER_TECHNIQUE_INDEX:** Yes (8 novel techniques)
- **Integration Complexity:** Medium (production-grade patterns require context)
