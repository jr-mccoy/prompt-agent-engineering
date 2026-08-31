# Claude Agent Guide for Claude Code Resources

**Purpose:** This guide helps AI agents (like Claude Code) work effectively with the 478 Claude Code resources in this directory - specialized agents, skills, and commands designed for persistent development workflows.

---

## Repository Overview

This directory contains **Claude Code-specific resources** that complement the base prompting library:

**Total Claude Code Resources:**
- **128 Agents** - Specialized AI personas with model assignments (Opus/Sonnet/Haiku)
- **303 Skills** - Modular knowledge packages with progressive disclosure
- **71 Commands** - Multi-agent orchestration workflows

**Key Difference from Base Prompts:**
- **Base Prompts:** One-time, copy-paste, model-agnostic
- **Claude Code Resources:** Persistent, optimized, reusable across sessions

---

## Understanding Resource Composition

**THE KEY INSIGHT:** These resources form a hierarchical architecture with clear roles.

### Canonical Claude Code Architecture

According to [Daniel Miessler's framework](https://danielmiessler.com/blog/when-to-use-skills-vs-commands-vs-agents):

```
┌─────────────────────────────────────────┐
│  AGENTS (Parallel Workers)               │  Execute work concurrently
│  • Standalone markdown files            │  Location: ~/.claude/agents/
│  • Run tasks in parallel                │  Example: security-auditor.md
│  • Invoke skills and commands           │  Example: python-architect.md
└──────────────────┬──────────────────────┘
                   │ invokes
                   ↓
┌─────────────────────────────────────────┐
│  SKILLS (Domain Containers)              │  Organize related capabilities
│  • Self-contained modules               │  Location: ~/.claude/skills/{domain}/
│  • Include routing logic                │  Example: skills/blogging/SKILL.md
│  • Reference domain files               │  Example: skills/kubernetes/SKILL.md
│  • Contain workflows subdirectory       │
└──────────────────┬──────────────────────┘
                   │ contains
                   ↓
┌─────────────────────────────────────────┐
│  COMMANDS (Nested Workflows)             │  Task-specific prompts
│  • Nested inside skills                 │  Location: skills/{domain}/workflows/
│  • Task-specific prompts                │  Example: skills/blogging/workflows/write.md
│  • Part of skill structure              │  Example: skills/k8s/workflows/deploy.md
└─────────────────────────────────────────┘
```

### Key Principles

1. **Skills = Domain Containers**
   - Encapsulation: All blogging capabilities in `skills/blogging/`
   - Discoverability: Find everything for a domain in one place
   - Portability: Skills are self-contained, shareable modules

2. **Commands = Nested Tasks**
   - Live inside skills at `workflows/` subdirectory
   - Represent specific actions within a domain
   - Not standalone files (part of skill structure)

3. **Agents = Parallel Workers**
   - Standalone entities that can invoke skills/commands
   - Enable concurrent task execution
   - Can use multiple skills simultaneously

### Note on Repository Structure

**⚠️ Important:** The wshobson/agents repository in this directory uses an **alternative structure** where commands are standalone files in `/commands/` rather than nested in `skills/{domain}/workflows/`. This predates or diverges from Daniel's canonical framework.

**For new resources, follow Daniel's framework:**
- ✅ Create commands inside `skills/{domain}/workflows/`
- ✅ Keep skills as domain containers
- ✅ Use agents as parallel workers

### Composition Examples (Canonical Framework)

**Example 1: Security Workflow (Correct Structure)**
```
security-auditor agent (parallel worker)
  ├─→ invokes security skill (domain container)
  │   ├─→ SKILL.md (routing logic + domain knowledge)
  │   └─→ workflows/
  │       ├─→ scan.md (command: run SAST scan)
  │       ├─→ audit.md (command: comprehensive audit)
  │       └─→ harden.md (command: apply hardening)
  └─→ invokes threat-modeling skill
      ├─→ SKILL.md (threat analysis framework)
      └─→ workflows/
          ├─→ stride.md (command: STRIDE analysis)
          └─→ attack-tree.md (command: generate attack trees)
```

**Example 2: Blogging Workflow (Daniel's Example)**
```
writing-agent agent (parallel worker)
  └─→ invokes blogging skill (domain container)
      ├─→ SKILL.md (blogging knowledge + routing)
      ├─→ references/
      │   ├─→ style-guide.md
      │   └─→ seo-best-practices.md
      └─→ workflows/
          ├─→ write.md (command: write blog post)
          ├─→ edit.md (command: edit existing post)
          ├─→ publish.md (command: publish to platform)
          └─→ seo-optimize.md (command: optimize for SEO)
```

**Example 3: Kubernetes Management**
```
kubernetes-architect agent (parallel worker)
  ├─→ invokes k8s skill (domain container)
  │   ├─→ SKILL.md (K8s expertise + routing)
  │   ├─→ scripts/
  │   │   └─→ validate-manifests.sh
  │   ├─→ references/
  │   │   ├─→ best-practices.md
  │   │   └─→ security-guide.md
  │   └─→ workflows/
  │       ├─→ deploy.md (command: deploy application)
  │       ├─→ scale.md (command: scale deployment)
  │       ├─→ troubleshoot.md (command: diagnose issues)
  │       └─→ helm-package.md (command: create Helm chart)
  │
  └─→ invokes security skill
      └─→ workflows/
          └─→ scan-k8s.md (command: scan K8s configs)
```

### Alternative Structure (wshobson/agents Repository)

**⚠️ Legacy Pattern:** The existing repository uses standalone commands in `/commands/`, not nested in skills. This is an older/alternative pattern.

**Example from existing repository:**
```
/commands/orchestration/full-stack-feature.md (standalone command)
  ├─→ orchestrates backend-architect agent
  │   └─→ agent references api-design-principles skill
  ├─→ orchestrates database-architect agent
  └─→ orchestrates frontend-developer agent
```

**Migration Path:** New resources should follow Daniel's canonical framework with commands inside `skills/{domain}/workflows/`.

---

## Decision Tree: How to Handle User Requests

```
User makes a request
│
├─→ User asks to CREATE a new agent/skill/command?
│   ("Create an agent for...", "Build a skill that...", "Make a command for...")
│   │
│   ├─→ "Create an AGENT for..."
│   │   │
│   │   └─→ BUILD AGENT
│   │       1. Read ../authoring/agent-patterns/AGENT_QUICK_START.md
│   │       2. Classify: Which model tier? (Opus/Sonnet/Haiku/Inherit)
│   │       3. Select patterns from ../authoring/agent-patterns/AGENT_PATTERN_INDEX.md
│   │       4. Build persona with activation criteria
│   │       5. Validate with ../authoring/agent-patterns/AGENT_QUALITY_RUBRIC.md
│   │
│   ├─→ "Create a SKILL for..."
│   │   │
│   │   └─→ BUILD SKILL
│   │       1. Read ../authoring/skill-patterns/SKILL_PATTERN_INDEX.md
│   │       2. Classify skill type (WORKFLOW, TOOL, DOMAIN, etc.)
│   │       3. Select patterns from SKILL_PATTERN_INDEX.md
│   │       4. Build SKILL.md + resources
│   │       5. Validate with SKILL_QUALITY_RUBRIC.md
│   │
│   └─→ "Create a COMMAND for..."
│       │
│       └─→ BUILD COMMAND
│           1. Read ../authoring/command-patterns/COMMAND_QUICK_START.md
│           2. Design orchestration flow (sequential/parallel)
│           3. Select agents to coordinate
│           4. Add validation gates
│           5. Validate with ../authoring/command-patterns/COMMAND_QUALITY_RUBRIC.md
│
├─→ User needs HELP with a task?
│   ("Analyze my code...", "Help me with K8s...", "Review architecture...")
│   │
│   └─→ FIND & EXECUTE EXISTING RESOURCE
│       Decision: Start with which resource type?
│       │
│       ├─→ Simple, focused task?
│       │   │
│       │   ├─→ Check skills/ first (direct knowledge)
│       │   │   Example: "Generate Helm chart" → helm-chart-scaffolding skill
│       │   │
│       │   └─→ Then check agents/ (if needs persona/context)
│       │       Example: "Review architecture" → architect-review agent
│       │
│       ├─→ Complex, multi-faceted task?
│       │   │
│       │   ├─→ Check commands/ first (orchestration)
│       │   │   Example: "Complete security audit" → /security-hardening
│       │   │
│       │   └─→ Fall back to multiple agents
│       │       Example: security-auditor + threat-modeling-expert
│       │
│       └─→ Ongoing development workflow?
│           │
│           └─→ Use agent + skills combination
│               Example: python-architect agent
│                 → loads async-python-patterns skill
│                 → loads python-testing-patterns skill
│
└─→ User asks ABOUT agents/skills/commands?
    ("How do agents work?", "What's the difference between...", "Can you explain...")
    │
    └─→ REFERENCE DOCUMENTATION
        - Agents: agents/README.md, MASTER_INDEX.md (to be created)
        - Skills: skills/README.md, ../authoring/skill-patterns/ guides
        - Commands: commands/README.md
        - Integration: documentation/integration_with_prompts.md
```

---

## When to Use Which Resource Type

### Canonical Framework (Daniel Miessler)

#### Use a SKILL when:
✅ You need a **domain container** to organize related capabilities
✅ You want **encapsulation** (all blogging, K8s, security in one place)
✅ You need **routing logic** to direct between different workflows
✅ You want **self-contained, portable** modules

**Structure:**
```
skills/{domain}/
├── SKILL.md (routing + domain knowledge)
├── scripts/ (optional automation)
├── references/ (optional documentation)
└── workflows/ (commands for this domain)
```

**Examples:**
- "All blogging capabilities" → `skills/blogging/` skill container
- "Kubernetes expertise" → `skills/kubernetes/` skill container
- "Security operations" → `skills/security/` skill container

#### Use a COMMAND when:
✅ You need a **specific task** within a domain
✅ Task is **nested inside** a skill container
✅ You want **focused, single-purpose** prompts
✅ You're invoking this from an agent

**Location:** `skills/{domain}/workflows/{task}.md`

**Examples:**
- "Write blog post" → `skills/blogging/workflows/write.md`
- "Deploy to K8s" → `skills/kubernetes/workflows/deploy.md`
- "Run security scan" → `skills/security/workflows/scan.md`

#### Use an AGENT when:
✅ You need a **parallel worker** that can invoke skills/commands
✅ You want **concurrent execution** of multiple tasks
✅ You need a **persistent persona** for ongoing work
✅ You want to **orchestrate multiple skills** simultaneously

**Location:** `agents/{agent-name}.md` (standalone file)

**Examples:**
- "Security auditor" → `agents/security-auditor.md` (invokes security skill + threat-modeling skill)
- "Full-stack developer" → `agents/full-stack-dev.md` (invokes backend + frontend + database skills)
- "Python expert" → `agents/python-architect.md` (invokes python skill + testing skill)

### Key Differences

| Aspect | Skill | Command | Agent |
|--------|-------|---------|-------|
| **Purpose** | Domain container | Specific task | Parallel worker |
| **Location** | `skills/{domain}/` | `skills/{domain}/workflows/` | `agents/` |
| **Contains** | Routing + workflows | Single prompt | Invocation logic |
| **Invoked by** | Agents | Agents | User/System |
| **Scope** | Entire domain | One task | Multiple skills |

### Alternative Structure (wshobson/agents)

**⚠️ Note:** The existing repository has standalone commands in `/commands/`, which is an alternative pattern.

**Use standalone COMMAND (legacy) when:**
- Following wshobson/agents repository structure
- Creating multi-agent orchestration workflows
- Need complex validation gates between agents

**Migration recommendation:** Convert to canonical framework with commands in `skills/{domain}/workflows/`

---

## Resource Navigation Guide

### Quick Lookup by Task

| User Task | First Check | Second Check | Third Check |
|-----------|-------------|--------------|-------------|
| "Security audit" | commands/security/ | agents/security/ | skills/security/ |
| "Python help" | agents/languages/python-* | skills/languages/python-* | - |
| "Generate K8s manifests" | skills/cloud-infrastructure/k8s-* | agents/cloud-infrastructure/kubernetes-* | - |
| "Full feature development" | commands/orchestration/ | - | - |
| "API design review" | agents/backend/graphql-architect | skills/backend-development/api-design-principles | - |
| "Quick code format" | agents/code-quality/ (Haiku) | - | - |
| "GitHub operations" | skills/developer-tools/github-ops | - | - |
| "Performance optimization" | commands/performance/ | agents/devops/performance-engineer | skills/observability/ |

### Directory Structure

```
domain-agentic-resources/
├── CLAUDE.md (this file - navigation guide)
├── MASTER_INDEX.md (to be created - searchable index)
├── README.md (overview and stats)
│
├── agents/ (128 agents across 16 categories)
│   ├── README.md (comprehensive index)
│   ├── architecture/ (7 agents)
│   ├── backend/ (10 agents)
│   ├── cloud-infrastructure/ (6 agents)
│   ├── languages/ (23 agents)
│   └── ... (12 more categories)
│
├── skills/ (303 skills across 28 categories)
│   ├── README.md (comprehensive index)
│   ├── backend-development/ (10 skills)
│   ├── cloud-infrastructure/ (12 skills)
│   ├── developer-tools/ (18 skills)
│   └── ... (17 more categories)
│
├── commands/ (71 commands across 15 categories)
│   ├── README.md (comprehensive index)
│   ├── orchestration/ (7 commands)
│   ├── security/ (5 commands)
│   ├── testing/ (5 commands)
│   └── ... (12 more categories)
│
└── documentation/ (analysis and integration guides)
    ├── INTEGRATION_WITH_PROMPTS.md
    ├── PROMPT_RESOURCE_MAPPING.md
    └── ... (technique analyses)
```

---

## Model Assignment Strategy

**Understanding Model Tiers:**

| Model | Speed | Cost | Best For | Agent Examples |
|-------|-------|------|----------|----------------|
| **Opus 4.5** | Slow | High | Critical architecture, security, code review | architect-review, security-auditor, code-reviewer |
| **Sonnet 4.5** | Medium | Medium | Balanced development tasks | python-pro, backend-architect, frontend-developer |
| **Haiku 4.5** | Fast | Low | Quick operations, formatting, scaffolding | code-formatter, quick-test-generator |
| **Inherit** | User choice | Variable | User decides based on budget/needs | Many utility agents |

**Cost Optimization Pattern:**
```
Critical Path (Opus):
  └─→ Architectural decisions → architect-review
  └─→ Security audits → security-auditor
  └─→ Code review quality gates → code-reviewer

Balanced Work (Sonnet):
  └─→ Feature development → backend-architect
  └─→ Test generation → test-automator
  └─→ Documentation → docs-architect

Fast Operations (Haiku):
  └─→ Code formatting → code-formatter
  └─→ Quick scaffolding → project-scaffolder
  └─→ Simple validations → syntax-checker
```

**See:** `documentation/integration_with_prompts.md` for detailed cost analysis (40-60% savings)

---

## Integration with Base Prompt System

### Complementary Usage Patterns

**Pattern 1: Prompt → Agent → Skill**
```
1. Use base prompt for initial analysis
   Example: code-analysis/security/security_vulnerability_analysis.md

2. Activate agent for ongoing work
   Example: security-auditor agent (Opus)

3. Agent loads relevant skills
   Example: security-scanning skill
```

**Pattern 2: Skill-First for Specialized Tasks**
```
User: "Generate Helm chart"

Skip prompts/agents, go direct to skill:
  → helm-chart-scaffolding skill
  → Bundled templates + validation scripts
  → Production-ready output
```

**Pattern 3: Command for Complete Workflows**
```
User: "Build new feature with testing and deployment"

Use command orchestration:
  → /full-stack-feature command
  → Coordinates 7+ agents
  → Each agent uses relevant skills
  → Complete feature pipeline
```

### When to Use Base Prompts vs Claude Code Resources

**Use BASE PROMPTS when:**
- ✅ One-time analysis or evaluation
- ✅ Not using Claude Code environment
- ✅ Need portable, copy-paste solution
- ✅ Model-agnostic execution

**Use CLAUDE CODE RESOURCES when:**
- ✅ Persistent development workflow
- ✅ Need model optimization (Opus/Sonnet/Haiku)
- ✅ Want progressive disclosure (large knowledge bases)
- ✅ Require bundled scripts and tools
- ✅ Multi-agent coordination needed

---

## Common Workflows

### Workflow 1: Security Audit (Hybrid Approach)

```
Step 1: Initial scan (base prompt)
  → Use: code-analysis/security/security_vulnerability_analysis.md
  → Output: List of potential vulnerabilities

Step 2: Deep analysis (agent)
  → Activate: security-auditor agent (Opus)
  → Output: Comprehensive security report with context

Step 3: Automated scanning (skill)
  → Load: security-scanning skill
  → Output: CI/CD integration for ongoing monitoring

Step 4: Full hardening (command)
  → Run: /security-hardening command
  → Output: Multi-agent comprehensive assessment
```

### Workflow 2: Python Project Development

```
Step 1: Project setup (skill)
  → Use: python-project-scaffolding skill
  → Output: Project structure with best practices

Step 2: Ongoing development (agent)
  → Activate: python-architect agent (Sonnet)
  → Agent loads:
    - async-python-patterns skill
    - python-testing-patterns skill
    - python-performance-optimization skill

Step 3: Code review (agent)
  → Activate: code-reviewer agent (Opus)
  → Output: Architecture and quality feedback

Step 4: Full feature (command)
  → Run: /full-stack-feature command (if full-stack project)
  → Coordinates backend + frontend + testing
```

### Workflow 3: Kubernetes Deployment

```
Step 1: Manifest generation (skill)
  → Use: k8s-manifest-generator skill
  → Output: Production-ready YAML files

Step 2: Helm chart (skill)
  → Use: helm-chart-scaffolding skill
  → Output: Complete Helm chart with values

Step 3: Security hardening (skill)
  → Use: k8s-security-policies skill
  → Output: Security contexts and policies

Step 4: Architecture review (agent)
  → Activate: kubernetes-architect agent (Opus)
  → Reviews: Complete deployment architecture

Step 5: Full deployment (command - if exists)
  → Run: /k8s-deploy command
  → Coordinates all agents + validates + deploys
```

---

## Creation Guides

### Creating Agents

**Guide:** [`../authoring/agent-patterns/AGENT_QUICK_START.md`](../authoring/agent-patterns/AGENT_QUICK_START.md) ✅ Available now

**5-Step Process:**
1. **Classify Model Tier** - Opus/Sonnet/Haiku/Inherit based on criticality
2. **Define Persona** - Role, expertise, activation criteria
3. **Select Patterns** - From [`AGENT_PATTERN_INDEX.md`](../authoring/agent-patterns/AGENT_PATTERN_INDEX.md)
4. **Build Agent File** - Write agent markdown with metadata
5. **Validate Quality** - Score against [`AGENT_QUALITY_RUBRIC.md`](../authoring/agent-patterns/AGENT_QUALITY_RUBRIC.md)

### Creating Skills

**Guide:** `../authoring/skill-patterns/SKILL_PATTERN_INDEX.md` ✅ Available now

**5-Step Process:**
1. **Classify Type** - WORKFLOW/TOOL/DOMAIN/CREATION/ANALYSIS/INTEGRATION/META
2. **Structure** - Choose organization pattern
3. **Build SKILL.md** - YAML frontmatter + markdown body
4. **Add Resources** - scripts/, references/, assets/
5. **Validate Quality** - Score against SKILL_QUALITY_RUBRIC.md (target: 75+)

**Template:** `../authoring/skill-patterns/templates/GOLD_STANDARD_SKILL.md` ✅ Available now

### Creating Commands

**Guide:** [`../authoring/command-patterns/COMMAND_QUICK_START.md`](../authoring/command-patterns/COMMAND_QUICK_START.md) ✅ Available now

**5-Step Process:**
1. **Design Workflow** - Sequential/Parallel/Conditional orchestration
2. **Select Agents** - Which agents to coordinate
3. **Add Validation Gates** - Quality checks between phases
4. **Error Handling** - Rollback and recovery strategies
5. **Validate Quality** - Score against [`COMMAND_QUALITY_RUBRIC.md`](../authoring/command-patterns/COMMAND_QUALITY_RUBRIC.md)

---

## Key Resource Files

### Navigation & Discovery
| File | Purpose |
|------|---------|
| `MASTER_INDEX.md` | (To be created) Single-file searchable index of all 361 resources |
| `agents/README.md` | ✅ Comprehensive agent index with model assignments |
| `skills/README.md` | ✅ Comprehensive skill index with bundled resources |
| `commands/README.md` | ✅ Comprehensive command index with orchestration patterns |

### Integration & Mapping
| File | Purpose |
|------|---------|
| `documentation/integration_with_prompts.md` | ✅ How to use prompts + agents + skills + commands together |

### Creation & Quality
| File | Purpose |
|------|---------|
| `../authoring/agent-patterns/AGENT_QUICK_START.md` | ✅ 5-step agent creation process |
| `../authoring/agent-patterns/AGENT_PATTERN_INDEX.md` | ✅ Agent design patterns |
| `../authoring/agent-patterns/AGENT_QUALITY_RUBRIC.md` | ✅ 100-point quality scoring for agents |
| `../authoring/command-patterns/COMMAND_QUICK_START.md` | ✅ 5-step command creation process |
| `../authoring/command-patterns/COMMAND_PATTERN_INDEX.md` | ✅ Orchestration patterns |
| `../authoring/command-patterns/COMMAND_QUALITY_RUBRIC.md` | ✅ 100-point quality scoring for commands |
| `../authoring/skill-patterns/SKILL_PATTERN_INDEX.md` | ✅ 5-step skill creation process |
| `../authoring/skill-patterns/SKILL_PATTERN_INDEX.md` | ✅ 41 skill design patterns |
| `../authoring/skill-patterns/SKILL_QUALITY_RUBRIC.md` | ✅ 100-point quality scoring for skills |

### Analysis & Techniques
| File | Purpose |
|------|---------|
| `documentation/novel_techniques_comprehensive_candidates.md` | ✅ 451 novel techniques discovered from analysis |
| `documentation/technique-analyses/` | ✅ Individual technique analysis for 106 resources |

---

## Important Guidelines for AI Agents

### ✅ DO:

- **Search existing resources first** before creating new ones
- **Use composition** - agents can load skills, commands can orchestrate agents
- **Respect model assignments** - Opus for critical, Haiku for fast
- **Follow progressive disclosure** - don't load unnecessary resources
- **Combine resource types** for complex workflows (prompt → agent → skill → command)
- **Reference creation guides** when building new resources
- **Validate quality** using rubrics before delivery

### ❌ DON'T:

- Create new resources when existing ones would work (search first!)
- Mix up resource types (skill ≠ agent ≠ command)
- Ignore model tiers (cost optimization matters)
- Over-engineer simple tasks (don't orchestrate when one skill suffices)
- Skip quality validation
- Create standalone agents when a skill would suffice

---

## Quick Reference: Resource Selection

### By Complexity

| Complexity | Best Resource Type | Example |
|------------|-------------------|---------|
| Simple, focused | **Skill** | Generate Helm chart |
| Medium, contextual | **Agent** | Review architecture |
| Complex, multi-step | **Command** | Build full-stack feature |

### By Reusability

| Usage Pattern | Best Resource Type | Example |
|--------------|-------------------|---------|
| One-time | **Base Prompt** | Ad-hoc security scan |
| Repeated task | **Skill** | Generate K8s manifests |
| Ongoing workflow | **Agent** | Python development partner |
| Complete pipeline | **Command** | Feature development workflow |

### By Model Optimization

| Requirement | Best Resource Type | Example |
|------------|-------------------|---------|
| Model-agnostic | **Base Prompt** | Analysis prompts |
| Cost-optimized | **Agent** (Haiku) | Code formatting |
| Quality-critical | **Agent** (Opus) | Security audit |
| Mixed models | **Command** | Multi-agent orchestration |

---

## Summary

### Canonical Architecture (Daniel Miessler Framework)

**Remember the key hierarchy:**

```
AGENTS (parallel workers) invoke → SKILLS (domain containers) contain → COMMANDS (workflows)
```

**Core Principles:**
1. **Skills** = Domain containers (blogging, kubernetes, security)
2. **Commands** = Nested tasks inside skills at `workflows/` subdirectory
3. **Agents** = Parallel workers that invoke skills and commands

### Quick Decisions

🎯 **"Help me with [domain]"**
   → Invoke relevant **agent** (parallel worker)
   → Agent loads appropriate **skill** (domain container)
   → Skill routes to specific **command** (workflow task)

🔧 **"Create new resource"**
   - **Agent**: ../authoring/agent-patterns/AGENT_QUICK_START.md ✅
   - **Skill**: ../authoring/skill-patterns/SKILL_PATTERN_INDEX.md ✅
   - **Command**: ../authoring/command-patterns/COMMAND_QUICK_START.md ✅

📚 **"How does architecture work?"**
   → Read: Daniel Miessler's post + This CLAUDE.md

💡 **"One-time analysis"**
   → Use: Base prompts from parent directory

🔁 **"Ongoing workflow in specific domain"**
   → Create/Use: Agent that invokes skill

🎼 **"Complex task in domain"**
   → Add: Command to `skills/{domain}/workflows/`

### Repository Structure Note

**⚠️ Important:** This repository contains resources from wshobson/agents which uses an alternative structure:
- ✅ Agents are standalone (matches canonical framework)
- ✅ Skills are domain containers (matches canonical framework)
- ⚠️ Commands are standalone in `/commands/` (diverges from canonical framework)

**For new resources:**
- Follow Daniel's canonical framework
- Place commands in `skills/{domain}/workflows/`
- Keep skills as domain containers
- Keep agents as parallel workers

---

**Repository:** jr-mccoy/prompt-agent-engineering
**Last Updated:** 2025-12-27
**Version:** 1.0.0
