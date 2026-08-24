# Integration Patterns: How Skills, Agents, and Commands Compose

**Purpose:** This guide explains how the three resource types in the agentic system work together, when to use each, and how to design multi-resource workflows.

**Audience:** Resource authors creating skills, agents, or commands who need to understand the composition model.

---

## Table of Contents

1. [Resource Type Overview](#resource-type-overview)
2. [Composition Model](#composition-model)
3. [Decision Tree: Which Resource Type?](#decision-tree-which-resource-type)
4. [Context Passing Mechanisms](#context-passing-mechanisms)
5. [Dependency Management](#dependency-management)
6. [Worked Examples](#worked-examples)
7. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
8. [Quick Reference](#quick-reference)

---

## Resource Type Overview

The agentic system uses three complementary resource types, each serving a distinct purpose:

### Skills: Knowledge Packages

**What they are:** Modular, discoverable, self-describing capabilities with bundled resources.

**Key characteristics:**
- Progressive disclosure (metadata → instructions → resources)
- Bundled assets (scripts, references, templates)
- Reusable across agents and sessions
- Loaded on-demand when triggered

**Structure:**
```
skill-name/
├── SKILL.md           # Metadata + instructions
├── scripts/           # Executable automation
├── references/        # Deep documentation
└── assets/            # Templates, files
```

**Best for:**
- Detailed procedural knowledge
- Bundled scripts and templates
- Domain expertise that multiple agents need
- Capabilities requiring versioned resources

### Agents: Specialized Identities

**What they are:** Persistent AI personas with model assignments optimized for specific domains.

**Key characteristics:**
- Model tier assignment (Opus/Sonnet/Haiku/Inherit)
- Behavioral traits and expertise definition
- Proactive or passive activation
- Can reference skills for detailed procedures

**Structure:**
```yaml
---
name: agent-name
description: Expert [domain] specializing in [expertise]. Use PROACTIVELY for [scenarios].
model: sonnet
---

[Agent persona and capability definition]
```

**Best for:**
- Specialized reasoning and decision-making
- Tasks requiring specific model capabilities
- Persistent identity across interactions
- Cost optimization through model selection

### Commands: Workflow Orchestration

**What they are:** Multi-phase workflows that coordinate multiple agents to complete end-to-end processes.

**Key characteristics:**
- Phase-based structure (3-6 phases typical)
- Agent coordination with Task tool
- Context passing between phases
- Validation gates and success criteria

**Structure:**
```markdown
# Command Name

[Extended thinking about methodology]

## Phase 1: [Name]
### 1. [Step]
- Use Task tool with subagent_type="agent-name"
- Prompt: "[Instructions]"
- Expected output: [Deliverables]

## Phase 2: [Name]
...

## Success Criteria
- ✅ [Criterion 1]
```

**Best for:**
- End-to-end processes (requirements → deployment)
- Multi-domain coordination
- Workflows with validation gates
- Processes requiring parallel execution

---

## Composition Model

Resources compose in a layered architecture where higher-level resources orchestrate lower-level ones:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        COMMAND LAYER                                 │
│  Orchestrates end-to-end workflows across multiple agents            │
│                                                                      │
│  /feature-development ─┬─→ Phase 1: Requirements                    │
│                        ├─→ Phase 2: Design                          │
│                        ├─→ Phase 3: Implementation (parallel)        │
│                        ├─→ Phase 4: Testing                         │
│                        └─→ Phase 5: Deployment                      │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         AGENT LAYER                                  │
│  Specialized identities with model assignments and expertise         │
│                                                                      │
│  backend-architect ──────────────────────┐                          │
│  python-pro ────────────────────────────┼────→ Execute tasks         │
│  test-automator ────────────────────────┼────→ Apply expertise       │
│  deployment-engineer ───────────────────┘────→ Reference skills      │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         SKILL LAYER                                  │
│  Knowledge packages with bundled resources and procedures            │
│                                                                      │
│  api-design-patterns ────────────┐                                   │
│  async-python-patterns ─────────┼────→ Provide procedures            │
│  pytest-patterns ───────────────┼────→ Supply templates              │
│  kubernetes-deployment ─────────┘────→ Execute scripts               │
└─────────────────────────────────────────────────────────────────────┘
```

### Composition Patterns

#### Pattern 1: Agent References Skill

An agent explicitly references a skill for detailed procedures:

```markdown
# In agent definition:

## Skill Integration

**Reference kubernetes-troubleshooting skill for:**
- Detailed step-by-step diagnostic procedures
- Pre-built health check scripts
- Common error message lookup
```

#### Pattern 2: Command Invokes Agent with Skill Reference

A command instructs an agent to use a specific skill:

```markdown
# In command definition:

### 3. Backend Implementation
- Use Task tool with subagent_type="python-pro"
- Prompt: "Implement backend for feature: $ARGUMENTS.

  Reference async-python-patterns skill for:
  - AsyncIO patterns
  - FastAPI best practices
  - Dependency injection patterns

  Generate production-ready Python code."
```

#### Pattern 3: Skill Provides Resources for Agent Execution

Skills bundle resources that agents execute:

```
kubernetes-troubleshooting/
├── SKILL.md                    # Procedures
├── scripts/
│   ├── health-check.sh         # Agent can execute
│   └── log-collector.sh        # Agent can execute
└── references/
    └── common-errors.md        # Agent can reference
```

Agent execution flow:
```
Agent receives task
    ↓
Agent recognizes need for skill
    ↓
Agent loads SKILL.md
    ↓
Agent executes scripts/health-check.sh
    ↓
Agent references common-errors.md
    ↓
Agent provides diagnosis
```

---

## Decision Tree: Which Resource Type?

Use this decision tree to determine the appropriate resource type:

```
START: You want to create a reusable resource
│
├─→ Does it coordinate MULTIPLE specialized tasks across phases?
│   │
│   YES → Does it require 3+ distinct phases with validation gates?
│   │      │
│   │      YES → CREATE A COMMAND
│   │      │     Examples: /feature-development, /security-hardening
│   │      │
│   │      NO → Could a single agent handle it with skill references?
│   │           │
│   │           YES → CREATE AN AGENT + reference existing skills
│   │           NO → CREATE A COMMAND (simpler, 2-3 phases)
│   │
│   NO ↓
│
├─→ Does it require a PERSISTENT IDENTITY with specific model capabilities?
│   │
│   YES → Is model selection (Opus/Sonnet/Haiku) important for this task?
│   │      │
│   │      YES → CREATE AN AGENT
│   │      │     Examples: security-auditor (Opus), mermaid-expert (Haiku)
│   │      │
│   │      NO → Does it need proactive activation for specific scenarios?
│   │           │
│   │           YES → CREATE AN AGENT (with activation criteria)
│   │           NO → Consider a SKILL with detailed expertise
│   │
│   NO ↓
│
├─→ Does it need BUNDLED RESOURCES (scripts, templates, references)?
│   │
│   YES → Will multiple agents potentially use these resources?
│   │      │
│   │      YES → CREATE A SKILL
│   │      │     Examples: helm-chart-scaffolding, kubernetes-troubleshooting
│   │      │
│   │      NO → Is it reusable across sessions/projects?
│   │           │
│   │           YES → CREATE A SKILL
│   │           NO → Consider embedding in agent or using a prompt
│   │
│   NO ↓
│
├─→ Is it DOMAIN KNOWLEDGE that should be loaded on-demand?
│   │
│   YES → CREATE A SKILL
│   │     Examples: api-design-patterns, pci-compliance
│   │
│   NO ↓
│
└─→ Is it a ONE-TIME INSTRUCTION without need for reuse?
    │
    YES → CREATE A PROMPT
    │     Use AI_AGENT_QUICK_START.md or NON_CODING_QUICK_START.md
    │
    NO → Reconsider: You likely need a SKILL
```

### Quick Decision Matrix

| Question | Yes → Use | No → Check Next |
|----------|-----------|-----------------|
| Multi-phase workflow with validation gates? | Command | ↓ |
| Requires specific model (Opus/Sonnet/Haiku)? | Agent | ↓ |
| Needs bundled scripts/templates/references? | Skill | ↓ |
| Reusable domain knowledge? | Skill | ↓ |
| One-time instruction? | Prompt | Skill |

### Comparison Table

| Aspect | Prompt | Skill | Agent | Command |
|--------|--------|-------|-------|---------|
| **Reusability** | None | High | High | High |
| **Bundled Resources** | No | Yes | No | No |
| **Model Selection** | N/A | No | Yes | Via agents |
| **Multi-phase** | No | No | No | Yes |
| **Progressive Disclosure** | No | Yes | No | No |
| **Proactive Activation** | No | Optional | Yes | No |
| **Coordination** | None | None | Task tool | Multi-agent |
| **Typical Complexity** | Low | Medium | Medium | High |

---

## Context Passing Mechanisms

Context flows between resources through several mechanisms:

### 1. Phase-to-Phase Context (Commands)

Commands pass context explicitly between phases:

```markdown
## Phase 1: Requirements Analysis

### 1. Gather Requirements
- Expected output: Requirements specification with acceptance criteria

## Phase 2: Design

### 2. System Architecture
- Prompt: "Design architecture based on requirements..."
- **Context from previous:** Requirements specification from Step 1
- Expected output: Architecture design

## Phase 3: Implementation

### 3. Backend Implementation
- Prompt: "Implement backend following architecture..."
- **Context from previous:**
  - Requirements specification from Step 1
  - Architecture design from Step 2
```

**Best practices:**
- Explicitly list what context each step needs
- Reference specific outputs, not entire phases
- Consider what information agents actually need

### 2. Skill References (Agents)

Agents reference skills for detailed procedures:

```markdown
# Agent definition

## Response Approach

1. **Gather symptoms** - Understand the issue
2. **Check cluster health** - Run health checks using skill's scripts
3. **Reference procedures** - Load relevant procedure from kubernetes-troubleshooting skill
4. **Execute diagnostics** - Follow step-by-step procedure
```

**Best practices:**
- Reference skills by name in agent definition
- Specify which skill resources to use
- Let agents decide when to load skill content

### 3. Prompt Instructions (Command → Agent)

Commands instruct agents via detailed prompts:

```markdown
### 3. Security Assessment
- Use Task tool with subagent_type="security-auditor"
- Prompt: "Perform comprehensive security assessment on: $ARGUMENTS.

  Using the architecture design from Phase 2, analyze:
  1) Authentication and authorization flows
  2) Data protection mechanisms
  3) Input validation and sanitization

  Reference the security-audit-patterns skill for:
  - OWASP Top 10 checklist
  - CVSS scoring guidelines

  Generate security report with prioritized findings."
```

**Best practices:**
- Include necessary context in the prompt
- Reference skills the agent should use
- Specify expected output format

### 4. Convergence Points (Parallel Execution)

When commands run steps in parallel, they must converge:

```markdown
## Phase 3: Implementation (PARALLEL)

### 3a. Backend Implementation
- Expected output: FastAPI application code

### 3b. Frontend Implementation
- Expected output: React components

### 3c. Database Implementation
- Expected output: Migration scripts, queries

---
### CONVERGENCE: Steps 3a-3c must complete before Phase 4
---

## Phase 4: Integration Testing

### 4. Integration Verification
- **Context from previous:** All Phase 3 outputs
- Prompt: "Verify integration between backend, frontend, and database..."
```

**Best practices:**
- Mark parallel steps clearly
- Define explicit convergence points
- Aggregate outputs for next phase

---

## Dependency Management

### Skill Dependencies

Skills can declare dependencies on other skills:

```yaml
---
name: full-stack-deployment
description: Deploy full-stack applications to Kubernetes
prerequisites:
  - kubectl CLI installed
  - Helm v3+ installed
related_skills:
  - helm-chart-scaffolding
  - kubernetes-troubleshooting
  - docker-build-patterns
---
```

**Dependency types:**
- **prerequisites:** External tools/access needed
- **related_skills:** Other skills that complement this one
- **bundled resources:** Internal dependencies (scripts/, references/)

### Agent Dependencies

Agents may depend on skills for detailed procedures:

```markdown
## Skill Integration

**Required skills:**
- kubernetes-troubleshooting - For diagnostic procedures
- prometheus-patterns - For metrics analysis

**Optional skills:**
- helm-chart-scaffolding - When deploying via Helm
```

### Command Dependencies

Commands orchestrate agents that may use skills:

```
Command: /full-stack-feature
│
├── Phase 1: business-analyst agent
│   └── Uses: requirements-gathering skill
│
├── Phase 2: backend-architect agent
│   └── Uses: api-design-patterns skill
│
├── Phase 3:
│   ├── python-pro agent
│   │   └── Uses: async-python-patterns skill
│   ├── frontend-developer agent
│   │   └── Uses: react-patterns skill
│   └── database-architect agent
│       └── Uses: postgresql-optimization skill
│
├── Phase 4: test-automator agent
│   └── Uses: pytest-patterns skill
│
└── Phase 5: deployment-engineer agent
    └── Uses: kubernetes-deployment skill
```

### Managing Circular Dependencies

**Rule:** Resources should form a directed acyclic graph (DAG).

**Avoid:**
```
skill-a references skill-b
skill-b references skill-c
skill-c references skill-a  ← CIRCULAR!
```

**Solution:** Extract shared functionality into a lower-level skill:
```
skill-a references shared-utils
skill-b references shared-utils
skill-c references shared-utils
```

---

## Worked Examples

### Example 1: Simple Skill Usage

**Scenario:** You need to troubleshoot Kubernetes pod issues.

**Resource chain:** Skill only

```
User: "My pod keeps crashing with OOMKilled"
         │
         ▼
┌─────────────────────────────┐
│ kubernetes-troubleshooting  │
│        SKILL                │
├─────────────────────────────┤
│ SKILL.md provides:          │
│ - Quick diagnosis steps     │
│ - Common OOMKilled causes   │
│                             │
│ references/common-errors.md:│
│ - Memory limit analysis     │
│ - Resource quota checking   │
│                             │
│ scripts/log-collector.sh:   │
│ - Collect relevant logs     │
└─────────────────────────────┘
         │
         ▼
Resolution: Increase memory limits
```

**Why this works:** Single-domain problem with established procedures. No need for agent identity or multi-phase orchestration.

---

### Example 2: Agent + Skill Integration

**Scenario:** You need expert security analysis of a codebase.

**Resource chain:** Agent → Skill

```
User: "Review security of the authentication module"
         │
         ▼
┌─────────────────────────────┐
│    security-auditor         │
│         AGENT               │
├─────────────────────────────┤
│ Model: Opus (critical task) │
│ Expertise: DevSecOps        │
│ Activation: PROACTIVE       │
│                             │
│ References skill:           │
│ └── security-audit-patterns │
└─────────────────────────────┘
         │
         │ Loads skill for procedures
         ▼
┌─────────────────────────────┐
│  security-audit-patterns    │
│         SKILL               │
├─────────────────────────────┤
│ references/owasp-top-10.md  │
│ references/cvss-scoring.md  │
│ scripts/sast-runner.sh      │
│ assets/report-template.md   │
└─────────────────────────────┘
         │
         ▼
Comprehensive security report with CVSS scores
```

**Why this works:** Security analysis requires expert reasoning (agent) plus detailed checklists and tooling (skill). Opus model ensures thorough analysis.

---

### Example 3: Command Orchestrating Multiple Agents

**Scenario:** You need to implement a complete feature from requirements to deployment.

**Resource chain:** Command → Agents → Skills

```
User: "/feature-development implement user authentication with OAuth2"
         │
         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    /feature-development COMMAND                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Phase 1: Requirements                                               │
│  ┌──────────────────┐    ┌─────────────────────┐                    │
│  │ business-analyst │───▶│ requirements-       │                    │
│  │     AGENT        │    │ gathering SKILL     │                    │
│  └──────────────────┘    └─────────────────────┘                    │
│           │                                                          │
│           ▼ Requirements specification                               │
│                                                                      │
│  Phase 2: Design                                                     │
│  ┌──────────────────┐    ┌─────────────────────┐                    │
│  │backend-architect │───▶│ api-design-patterns │                    │
│  │     AGENT        │    │       SKILL         │                    │
│  └──────────────────┘    └─────────────────────┘                    │
│           │                                                          │
│           ▼ API specification + Architecture                         │
│                                                                      │
│  Phase 3: Implementation (PARALLEL)                                  │
│  ┌──────────────────┐    ┌─────────────────────┐                    │
│  │   python-pro     │───▶│ async-python        │                    │
│  │     AGENT        │    │ -patterns SKILL     │                    │
│  └──────────────────┘    └─────────────────────┘                    │
│                                                                      │
│  ┌──────────────────┐    ┌─────────────────────┐                    │
│  │frontend-developer│───▶│ react-patterns      │                    │
│  │     AGENT        │    │       SKILL         │                    │
│  └──────────────────┘    └─────────────────────┘                    │
│                                                                      │
│  ┌──────────────────┐    ┌─────────────────────┐                    │
│  │database-architect│───▶│ postgresql-         │                    │
│  │     AGENT        │    │ optimization SKILL  │                    │
│  └──────────────────┘    └─────────────────────┘                    │
│           │                                                          │
│           ▼ CONVERGENCE: All implementations complete                │
│                                                                      │
│  Phase 4: Testing                                                    │
│  ┌──────────────────┐    ┌─────────────────────┐                    │
│  │  test-automator  │───▶│ pytest-patterns     │                    │
│  │     AGENT        │    │       SKILL         │                    │
│  └──────────────────┘    └─────────────────────┘                    │
│           │                                                          │
│           ▼ Tests passing, coverage met                              │
│                                                                      │
│  Phase 5: Deployment                                                 │
│  ┌──────────────────┐    ┌─────────────────────┐                    │
│  │deployment-       │───▶│ kubernetes-         │                    │
│  │engineer AGENT    │    │ deployment SKILL    │                    │
│  └──────────────────┘    └─────────────────────┘                    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
         │
         ▼
Feature deployed with tests, documentation, and monitoring
```

**Why this works:** End-to-end feature development requires multiple domains (business, backend, frontend, database, testing, deployment), each with specialized agents using domain-specific skills. Command provides orchestration and validation gates.

---

### Example 4: Skill Creating Other Skills (Meta-Skill)

**Scenario:** You need to create a new skill using best practices.

**Resource chain:** Skill → Generated Skill

```
User: "Create a skill for validating Helm charts"
         │
         ▼
┌─────────────────────────────┐
│      skill-creator          │
│        META-SKILL           │
├─────────────────────────────┤
│ SKILL.md provides:          │
│ - Skill structure templates │
│ - Quality checklist         │
│ - Naming conventions        │
│                             │
│ assets/:                    │
│ - SKILL_TEMPLATE.md         │
│ - quality-rubric.md         │
│                             │
│ scripts/:                   │
│ - validate-skill.py         │
└─────────────────────────────┘
         │
         │ Generates
         ▼
┌─────────────────────────────┐
│   helm-chart-validation     │
│      GENERATED SKILL        │
├─────────────────────────────┤
│ SKILL.md                    │
│ scripts/validate-chart.sh   │
│ references/chart-errors.md  │
│ assets/values-template.yaml │
└─────────────────────────────┘
```

**Why this works:** Meta-skills codify the process of creating other resources, ensuring consistency and quality across the system.

---

### Example 5: Conditional Agent Selection in Commands

**Scenario:** A command needs different agents based on detected technology.

**Resource chain:** Command → Conditional Agent Selection

```markdown
# In command definition:

### 3. Backend Implementation
- **If Python detected:** Use Task tool with subagent_type="python-pro"
- **If Node.js detected:** Use Task tool with subagent_type="nodejs-expert"
- **If Go detected:** Use Task tool with subagent_type="go-developer"

- Prompt: "Implement backend for feature: $ARGUMENTS.

  Detect primary backend language from:
  - package.json → Node.js
  - requirements.txt/pyproject.toml → Python
  - go.mod → Go

  Reference appropriate patterns skill for the detected stack."
```

**Why this works:** Commands can adapt to project context by conditionally selecting agents and skills based on detected technology.

---

## Anti-Patterns to Avoid

### Anti-Pattern 1: Monolithic Skills

**Bad:** One skill that tries to do everything.

```
# DON'T: all-in-one-devops skill with 50+ procedures
```

**Good:** Focused skills that compose.

```
# DO:
kubernetes-troubleshooting/
helm-chart-scaffolding/
docker-build-patterns/
```

### Anti-Pattern 2: Agent Without Skill References

**Bad:** Agent contains all procedural knowledge inline.

```markdown
# DON'T: 3000-line agent with embedded procedures
```

**Good:** Agent references skills for detailed procedures.

```markdown
# DO: Agent with "Reference kubernetes-troubleshooting skill for diagnostic procedures"
```

### Anti-Pattern 3: Commands Without Validation Gates

**Bad:** Linear workflow with no checkpoints.

```markdown
# DON'T: Phase 1 → Phase 2 → Phase 3 → Phase 4 (no gates)
```

**Good:** Explicit validation between phases.

```markdown
# DO: Phase 1 → [GATE] → Phase 2 → [GATE] → Phase 3
```

### Anti-Pattern 4: Circular Skill Dependencies

**Bad:** Skills that reference each other in a cycle.

**Good:** Directed acyclic graph of dependencies.

### Anti-Pattern 5: Missing Context Passing

**Bad:** Agent steps without knowing what prior steps produced.

```markdown
# DON'T: Step 3 with no "Context from previous"
```

**Good:** Explicit context requirements.

```markdown
# DO: Step 3 with "Context from previous: API spec from Step 1, Schema from Step 2"
```

---

## Quick Reference

### When to Create Each Type

| Situation | Create |
|-----------|--------|
| Need bundled scripts/templates | Skill |
| Need specific model (Opus/Haiku) | Agent |
| Need multi-phase orchestration | Command |
| Need domain expertise | Skill |
| Need persistent identity | Agent |
| Need parallel execution | Command |
| Need validation gates | Command |
| One-time task | Prompt |

### Composition Checklist

- [ ] Skills are focused (one coherent problem)
- [ ] Agents reference skills for detailed procedures
- [ ] Commands explicitly pass context between phases
- [ ] Parallel steps have convergence points
- [ ] Dependencies form a DAG (no cycles)
- [ ] Validation gates between command phases
- [ ] Model selection matches task criticality

### File Locations

| Resource | Location |
|----------|----------|
| Skills | `domain-agentic-resources/skills/{category}/{skill-name}/` |
| Agents | `domain-agentic-resources/agents/{category}/` |
| Commands | `domain-agentic-resources/commands/{category}/` |
| Skill authoring | `authoring/skill-patterns/` |
| Agent authoring | `authoring/agent-patterns/` |
| Command authoring | `authoring/command-patterns/` |

---

## Related Documentation

- [Skill Pattern Index](skill-patterns/SKILL_PATTERN_INDEX.md) - Creating skills
- [Agent Quick Start](agent-patterns/AGENT_QUICK_START.md) - Creating agents
- [Command Quick Start](command-patterns/COMMAND_QUICK_START.md) - Creating commands
- [Worked Examples](templates/worked-examples/) - Full integration examples
- [Gold Standard Skill](skill-patterns/templates/GOLD_STANDARD_SKILL.md) - Annotated skill example
- [Gold Standard Agent](templates/GOLD_STANDARD_AGENT.md) - Annotated agent example
- [Gold Standard Command](templates/GOLD_STANDARD_COMMAND.md) - Annotated command example

---

**Last Updated:** 2026-01-29
**Part of:** Documentation Infrastructure (Phase 1.1)
