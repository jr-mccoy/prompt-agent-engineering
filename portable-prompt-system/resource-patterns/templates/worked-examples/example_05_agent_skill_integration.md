# Example 05: Agent + Skill Integration

**Goal:** Demonstrate how an agent leverages a bundled skill for enhanced capability.

**Time Estimate:** 25 minutes

**Concepts Covered:**
- Agent referencing skills
- Progressive skill disclosure
- Knowledge augmentation pattern

---

## Scenario

**Task:** Create a Kubernetes troubleshooting agent that uses a bundled skill for diagnostic procedures.

The agent provides the persona and reasoning; the skill provides detailed checklists and procedures.

---

## Step 1: Understand the Integration Pattern

### How Agents and Skills Work Together

```
┌─────────────────────────────────────────────┐
│                   AGENT                      │
│  • Identity and persona                      │
│  • Behavioral traits                         │
│  • Response approach                         │
│  • Decision making                           │
│                    │                         │
│                    ▼                         │
│  "Reference kubernetes-troubleshooting skill │
│   for detailed diagnostic procedures"        │
└─────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│                   SKILL                      │
│  • Detailed checklists                       │
│  • Step-by-step procedures                   │
│  • Reference commands                        │
│  • Bundled scripts                           │
│  • Best practice resources                   │
└─────────────────────────────────────────────┘
```

### Why Integrate?

| Concern | Agent Handles | Skill Provides |
|---------|---------------|----------------|
| Identity | ✅ Expert persona | — |
| Reasoning | ✅ Problem analysis | — |
| Detailed Steps | — | ✅ Procedures |
| Reference Data | — | ✅ Commands, scripts |
| Updates | — | ✅ Versioned resources |

---

## Step 2: Create the Skill

First, create the skill that the agent will reference:

### Skill Structure

```
kubernetes-troubleshooting/
├── SKILL.md              # Main skill file
├── procedures/
│   ├── pod-crashloop.md
│   ├── node-not-ready.md
│   └── network-issues.md
├── scripts/
│   ├── health-check.sh
│   └── log-collector.sh
└── references/
    └── common-errors.md
```

### SKILL.md Content

```markdown
---
skill_name: kubernetes-troubleshooting
version: 1.0.0
description: Comprehensive Kubernetes cluster troubleshooting procedures and diagnostic commands
category: cloud-infrastructure
related_skills:
  - helm-chart-scaffolding
  - terraform-infrastructure
prerequisites:
  - kubectl CLI access
  - Cluster admin permissions for full diagnostics
---

# Kubernetes Troubleshooting Skill

## Quick Reference

### Health Check Commands
```bash
# Cluster health
kubectl get nodes
kubectl get cs
kubectl cluster-info

# Pod status
kubectl get pods -A | grep -v Running
kubectl describe pod <pod-name> -n <namespace>
kubectl logs <pod-name> -n <namespace> --previous
```

## Diagnostic Procedures

### Pod Issues
- **CrashLoopBackOff** → See [pod-crashloop.md](procedures/pod-crashloop.md)
- **ImagePullBackOff** → Check image name, registry access, pull secrets
- **Pending** → Check resource requests, node selectors, affinity rules

### Node Issues
- **NotReady** → See [node-not-ready.md](procedures/node-not-ready.md)
- **DiskPressure** → Clean up logs, images; expand storage
- **MemoryPressure** → Review pod memory limits; add nodes

### Network Issues
- **Service not reachable** → See [network-issues.md](procedures/network-issues.md)
- **DNS failures** → Check CoreDNS pods, verify DNS policy

## Bundled Scripts

- `scripts/health-check.sh` - Comprehensive cluster health check
- `scripts/log-collector.sh` - Collect logs for support tickets

## Common Error Reference

See [common-errors.md](references/common-errors.md) for error messages and solutions.
```

---

## Step 3: Create the Agent

Now create the agent that references this skill:

### Agent File

```markdown
---
name: kubernetes-troubleshooter
description: Expert Kubernetes troubleshooter specializing in cluster diagnostics, pod failures, and network issues. Uses kubernetes-troubleshooting skill for detailed procedures. Use PROACTIVELY for K8s issues, cluster problems, or deployment failures.
model: sonnet
---

You are an expert Kubernetes troubleshooter specializing in diagnosing and resolving cluster issues across development, staging, and production environments.

## Purpose

Expert Kubernetes operations engineer with deep knowledge of container orchestration, cluster administration, and cloud-native troubleshooting. Diagnoses issues from application layer (pods) through platform layer (nodes, networking) to infrastructure layer (cloud provider). Uses structured diagnostic procedures from the kubernetes-troubleshooting skill.

## Capabilities

### Cluster Diagnostics
- Cluster health assessment and monitoring analysis
- Node status evaluation and resource utilization
- Control plane component verification
- etcd health and performance analysis
- API server performance troubleshooting

### Pod Troubleshooting
- CrashLoopBackOff root cause analysis
- OOMKilled investigation and memory profiling
- ImagePullBackOff and registry connectivity
- Init container failures and dependency issues
- Liveness/readiness probe optimization

### Network Troubleshooting
- Service discovery and DNS resolution
- Ingress controller configuration
- Network policy debugging
- Pod-to-pod connectivity verification
- Load balancer integration issues

### Resource Management
- Resource quota and limit analysis
- Node capacity planning
- PersistentVolume troubleshooting
- StorageClass configuration issues
- Horizontal Pod Autoscaler tuning

## Skill Integration

**Reference kubernetes-troubleshooting skill for:**
- Detailed step-by-step diagnostic procedures
- Pre-built health check scripts
- Common error message lookup
- Best practice checklists

When encountering specific issues, load the relevant procedure from the skill's `procedures/` directory for systematic resolution.

## Behavioral Traits

- Follows structured diagnostic methodology (observe, hypothesize, test)
- Starts with least invasive checks before impactful operations
- Documents all diagnostic steps and findings
- Considers impact on production workloads
- Escalates appropriately when issues exceed scope
- Validates fixes before closing issues

## Response Approach

1. **Gather symptoms** - Understand error messages, timing, affected resources
2. **Check cluster health** - Run health checks using skill's scripts
3. **Isolate scope** - Determine if issue is pod, node, namespace, or cluster-wide
4. **Reference procedures** - Load relevant procedure from kubernetes-troubleshooting skill
5. **Execute diagnostics** - Follow step-by-step procedure
6. **Identify root cause** - Correlate findings to determine cause
7. **Implement fix** - Apply resolution, starting with least impactful
8. **Verify resolution** - Confirm issue resolved and no side effects
9. **Document** - Record findings and resolution for future reference

## Example Interactions

- "My pods keep restarting with CrashLoopBackOff"
- "Nodes are showing NotReady status in my cluster"
- "Service isn't reachable from other pods"
- "Pod is stuck in Pending state"
- "Getting OOMKilled errors in my deployment"
- "Ingress isn't routing traffic correctly"
- "PersistentVolumeClaim stuck in Pending"
- "Horizontal Pod Autoscaler not scaling"
```

---

## Step 4: How They Work Together

### Interaction Flow

```
User: "My pods keep restarting with CrashLoopBackOff"

Agent (kubernetes-troubleshooter):
1. Recognizes this as a pod troubleshooting issue
2. Applies response approach steps 1-4
3. References kubernetes-troubleshooting skill
4. Loads procedures/pod-crashloop.md
5. Follows procedure systematically
6. Uses scripts/log-collector.sh if needed
7. Identifies root cause
8. Provides resolution
```

### Sample Resolution Using Integration

```markdown
## Diagnosis: CrashLoopBackOff for pod `api-server-xyz`

### Step 1: Gather Symptoms
- Pod restarts every 30 seconds
- Last restart reason: Error (exit code 1)
- Started after latest deployment

### Step 2: Cluster Health (from skill scripts)
```bash
# Running health-check.sh
✅ Nodes: 3/3 Ready
✅ Control plane: Healthy
✅ DNS: CoreDNS running
```

### Step 3: Scope Isolation
- Issue limited to `api-server` deployment
- Other pods in namespace running normally

### Step 4: Procedure from kubernetes-troubleshooting skill

**Following: procedures/pod-crashloop.md**

1. ✅ Check current pod status
   ```bash
   kubectl describe pod api-server-xyz -n production
   ```
   Result: Container exiting with code 1

2. ✅ Check previous container logs
   ```bash
   kubectl logs api-server-xyz -n production --previous
   ```
   Result: "Error: DATABASE_URL environment variable not set"

3. ✅ Check environment variables
   ```bash
   kubectl get pod api-server-xyz -n production -o yaml | grep -A 20 env
   ```
   Result: DATABASE_URL missing from env

### Root Cause
Missing `DATABASE_URL` environment variable after ConfigMap update.

### Resolution
```bash
# Update deployment with missing env var
kubectl set env deployment/api-server DATABASE_URL=postgres://...
```

### Verification
- Pod now running without restarts
- Application responding to health checks
```

---

## Key Integration Points

### 1. Skill Reference in Agent Description

```markdown
description: Expert Kubernetes troubleshooter... Uses kubernetes-troubleshooting skill for detailed procedures.
```

### 2. Explicit Skill Integration Section

```markdown
## Skill Integration

**Reference kubernetes-troubleshooting skill for:**
- Detailed step-by-step diagnostic procedures
- Pre-built health check scripts
- Common error message lookup
```

### 3. Response Approach References Skill

```markdown
4. **Reference procedures** - Load relevant procedure from kubernetes-troubleshooting skill
```

---

## Benefits of Integration

| Benefit | Description |
|---------|-------------|
| **Separation of Concerns** | Agent handles reasoning; skill provides procedures |
| **Maintainability** | Update procedures without changing agent |
| **Versioning** | Skill versions can evolve independently |
| **Reusability** | Same skill used by multiple agents |
| **Resource Bundling** | Scripts, templates in skill directory |

---

## Files Referenced

- **Agent Pattern Reference:** [AGENT_PATTERN_INDEX.md](../../agent-patterns/AGENT_PATTERN_INDEX.md)
- **Skill Pattern Reference:** [../../skill-patterns/SKILL_PATTERN_INDEX.md](../../skill-patterns/SKILL_PATTERN_INDEX.md)
- **Skills Directory:** ../../skills/
