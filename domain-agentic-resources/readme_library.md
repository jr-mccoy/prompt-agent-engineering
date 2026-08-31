# Claude Code Resources

This directory contains **agents**, **skills**, and **commands** for Claude Code - specialized AI capabilities that extend Claude's functionality for software development workflows.

---

## ⚠️ Important: This is the Implementation Library

**This directory (`domain-agentic-resources/`) contains production-ready resources you can USE immediately.**

| Directory | Purpose | Contains |
|-----------|---------|----------|
| **`domain-agentic-resources/`** (this) | 📚 **Implementation Library** | 132 skills, 128 agents, 71 commands ready to use |
| **`authoring/skill-patterns/`** | 📐 **Skill Authoring System** | Design patterns, templates, quality rubrics for creating skills |

### Quick Decision Tree

```
┌─────────────────────────────────────────────────────────────────┐
│                    What do you want to do?                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  USE an existing resource?                                       │
│  ├── Find a skill    → domain-agentic-resources/skills/            │
│  ├── Find an agent   → domain-agentic-resources/agents/            │
│  └── Find a command  → domain-agentic-resources/commands/          │
│                                                                  │
│  CREATE a new resource?                                          │
│  ├── Create a skill  → authoring/skill-patterns/AGENT_SKILL_QUICK_START.md  │
│  ├── Create an agent → domain-agentic-resources/AGENT_QUICK_START.md│
│  └── Create a command→ domain-agentic-resources/COMMAND_QUICK_START.md│
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Why two directories?**
- `authoring/skill-patterns/` = Design patterns and authoring guides (the "how to build")
- `domain-agentic-resources/` = Production implementations (the "what's built")

This separation keeps authoring documentation focused while keeping implementations browsable.

---

## Quick Navigation

| Resource | Purpose | Start Here |
|----------|---------|------------|
| **[CLAUDE.md](CLAUDE.md)** | 📘 Complete navigation guide | First-time users |
| **[MASTER_INDEX.md](master_index.md)** | 🔍 Searchable index of all 361 resources | Finding specific resources |
| **[agents/README.md](agents/README.md)** | 🤖 128 agents with model assignments | Browse agents |
| **[skills/README.md](skills/README.md)** | 🎓 132 skills with bundled resources | Browse skills |
| **[commands/README.md](commands/README.md)** | ⚙️ 71 commands with orchestration | Browse commands |
| **AGENT_QUICK_START.md** | 🛠️ Create new agents (5-step process) | Creating agents |
| **COMMAND_QUICK_START.md** | 🛠️ Create new commands (5-step process) | Creating commands |

## Overview

**Total Resources:**
- **128 Agents** - Parallel workers with model optimization (Opus/Sonnet/Haiku/Inherit)
- **132 Skills** - Domain containers with progressive disclosure and bundled resources
- **71 Commands** - Standalone orchestrators (legacy structure) + workflow commands

**Source Repositories:**
- [wshobson/agents](https://github.com/wshobson/agents) - 67 plugin-based agents, skills, and commands
- [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) - 25 production-ready skills

## Architecture

### Three Frameworks

This repository documents three different architectural frameworks:

**1. Anthropic Official** ([Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/authoring/skill-patterns/overview))
- **Skills only** with `SKILL.md` + YAML frontmatter
- Three-level loading: Metadata → Instructions → Resources
- No separate agents or commands primitives

**2. Daniel Miessler Framework** ([Blog Post](https://danielmiessler.com/blog/when-to-use-skills-vs-commands-vs-agents))
- **Skills** = Domain containers (e.g., `skills/blogging/`)
- **Commands** = Workflows inside skills at `skills/{domain}/workflows/`
- **Agents** = Parallel workers that invoke skills/commands

**3. This Repository (wshobson/agents)** - Alternative Structure
- **Agents** in `agents/` directory (matches framework)
- **Skills** in `skills/` directory (matches framework)
- **Commands** in `commands/` directory (standalone, not nested)

**⚠️ For new resources:** Follow Daniel Miessler's canonical framework with commands nested in `skills/{domain}/workflows/`

### Resource Relationships

```
AGENTS (parallel workers)
  ↓ invoke
SKILLS (domain containers)
  ↓ contain
COMMANDS (workflow tasks)
```

**See:** [CLAUDE.md](CLAUDE.md) for complete architecture explanation and examples

## Directory Structure

```
domain-agentic-resources/
├── README.md (this file)
├── agents/
│   ├── README.md (agent index and guide)
│   ├── architecture/ (9 agents)
│   ├── backend/ (3 agents)
│   ├── cloud-infrastructure/ (2 agents)
│   ├── code-quality/ (3 agents)
│   ├── database/ (3 agents)
│   ├── deployment/ (3 agents)
│   ├── devops/ (6 agents)
│   ├── documentation/ (4 agents)
│   ├── frontend-mobile/ (5 agents)
│   ├── languages/ (15 agents)
│   ├── ml-ai/ (4 agents)
│   ├── orchestration/ (5 agents)
│   ├── security/ (5 agents)
│   ├── seo-marketing/ (4 agents)
│   ├── testing/ (2 agents)
│   └── business-operations/ (6 agents)
├── skills/
│   ├── README.md (skill index and guide)
│   ├── accessibility/ (2 skills)
│   ├── backend-development/ (3 skills)
│   ├── blockchain-web3/ (4 skills)
│   ├── cicd-automation/ (4 skills)
│   ├── cloud-infrastructure/ (4 skills)
│   ├── content-creation/ (5 skills)
│   ├── data-engineering/ (3 skills)
│   ├── developer-tools/ (8 skills)
│   ├── devops/ (3 skills)
│   ├── document-processing/ (7 skills)
│   ├── framework-migration/ (2 skills)
│   ├── infrastructure-as-code/ (3 skills)
│   ├── languages/ (15 skills)
│   ├── llm-application-dev/ (4 skills)
│   ├── mobile-development/ (2 skills)
│   ├── observability/ (4 skills)
│   ├── payments/ (2 skills)
│   ├── security/ (4 skills)
│   ├── testing-qa/ (5 skills)
│   └── web-development/ (4 skills)
├── commands/
│   ├── README.md (command index and guide)
│   ├── accessibility/ (1 command)
│   ├── architecture/ (2 commands)
│   ├── code-quality/ (2 commands)
│   ├── database/ (1 command)
│   ├── deployment/ (3 commands)
│   ├── devops/ (5 commands)
│   ├── documentation/ (1 command)
│   ├── framework-migration/ (1 command)
│   ├── git-workflows/ (3 commands)
│   ├── orchestration/ (3 commands)
│   ├── performance/ (2 commands)
│   ├── security/ (4 commands)
│   ├── testing/ (2 commands)
│   └── troubleshooting/ (3 commands)
└── documentation/
    ├── AGENT_GUIDE.md (how to use agents)
    ├── SKILL_GUIDE.md (how to use skills)
    ├── COMMAND_GUIDE.md (how to use commands)
    ├── INTEGRATION_WITH_PROMPTS.md (how these relate to existing prompts)
    ├── TECHNIQUE_ANALYSIS.md (prompting techniques found in agents/skills)
    └── FUTURE_PROCESSING_INSTRUCTIONS.md (instructions for analyzing and indexing)
```

## What Are Agents, Skills, and Commands?

### Agents
**Specialized AI personas with deep domain expertise.** Each agent is optimized for specific tasks (architecture, security, deployment, etc.) and may use different Claude models based on task criticality.

**Example agents:**
- `python-architect` - Python application architecture and design patterns
- `security-auditor` - Code security analysis and vulnerability detection
- `kubernetes-architect` - Kubernetes deployment and orchestration

**Location:** `agents/<category>/<agent-name>.md`

### Skills
**Modular knowledge packages with progressive disclosure.** Skills bundle specialized knowledge, workflows, scripts, and reference materials that Claude loads only when needed.

**Structure of a skill:**
```
skill-name/
├── SKILL.md (core instructions)
├── scripts/ (executable Python/Bash code)
├── references/ (documentation loaded as needed)
└── assets/ (templates, icons, resources)
```

**Example skills:**
- `async-python-patterns` - AsyncIO and concurrent programming patterns
- `github-ops` - GitHub operations using gh CLI and API
- `kubernetes-manifests` - K8s YAML generation and best practices

**Location:** `skills/<category>/<skill-name>/`

### Commands
**Slash commands and development tools** for specific workflows like scaffolding, analysis, and automation.

**Example commands:**
- `/python-scaffold` - Create production-ready Python projects
- `/security-hardening` - Multi-agent security assessment
- `/full-stack-feature` - Coordinate 7+ agents for feature development

**Location:** `commands/<category>/<command-name>.md`

## How This Relates to Existing Prompts

The Prompting-guides repository contains **261+ AI prompts** organized by task type (code-analysis, testing, devops, etc.). Claude Code resources complement these:

**Existing Prompts:**
- General-purpose prompts for one-time analysis
- Executable immediately with context
- Examples: `security_vulnerability_analysis.md`, `testing_unit_test_generation.md`

**Claude Code Resources:**
- Persistent agent identities with model assignments
- Progressive disclosure (load knowledge only when needed)
- Bundled scripts and tools for repeated workflows
- Multi-agent orchestration capabilities

**Use Together:**
- Use **prompts** for ad-hoc analysis and one-time tasks
- Use **agents/skills** for ongoing development workflows with specialized tools
- Use **commands** for complex multi-step operations requiring orchestration

See `documentation/INTEGRATION_WITH_PROMPTS.md` for detailed mapping and usage patterns.

## Quick Start

### Finding Resources

**By Task Type:**
- Security analysis → `agents/security/`, `skills/security/`
- Python development → `agents/languages/python-*.md`, `skills/languages/python-*/`
- Kubernetes deployment → `agents/cloud-infrastructure/kubernetes-*.md`, `skills/cloud-infrastructure/kubernetes-*/`
- Testing automation → `agents/testing/`, `skills/testing-qa/`, `commands/testing/`

**By Resource Type:**
- Browse agents → `agents/README.md` (organized index)
- Browse skills → `skills/README.md` (categorized listing)
- Browse commands → `commands/README.md` (workflow-based index)

### Installation (For Use in Claude Code)

These resources are designed for **Claude Code**. To use them:

1. **Add marketplace** (for wshobson/agents):
   ```bash
   /plugin marketplace add wshobson/agents
   /plugin install <plugin-name>
   ```

2. **Add marketplace** (for daymade/claude-code-skills):
   ```bash
   /plugin marketplace add https://github.com/daymade/claude-code-skills
   /plugin install <skill-name>@daymade-skills
   ```

See individual READMEs in `agents/`, `skills/`, and `commands/` for detailed installation instructions.

## Creation Guides

### Creating New Resources

> **🔗 Note:** Skill creation guides are in the separate **[authoring/skill-patterns/](../authoring/skill-patterns/)** directory, which serves as the skill authoring system. Agent and command guides are in this directory.

| Resource Type | Guide | Location |
|--------------|-------|----------|
| **Agents** | AGENT_QUICK_START.md | This directory |
| **Skills** | AGENT_SKILL_QUICK_START.md | `authoring/skill-patterns/` (authoring system) |
| **Commands** | COMMAND_QUICK_START.md | This directory |

### Pattern Libraries

| Pattern Type | Guide | Location |
|-------------|-------|----------|
| **Agent Patterns** | AGENT_PATTERN_INDEX.md | This directory (40 patterns) |
| **Skill Patterns** | [SKILL_PATTERN_INDEX.md](../authoring/skill-patterns/SKILL_PATTERN_INDEX.md) | `authoring/skill-patterns/` (41 patterns) |
| **Command Patterns** | COMMAND_PATTERN_INDEX.md | This directory (29 patterns) |

### Use Case Lookups

| Resource Type | Guide | Location |
|--------------|-------|----------|
| **Agents** | AGENT_USE_CASE_LOOKUP.md | This directory |
| **Skills** | [SKILL_USE_CASE_LOOKUP.md](../authoring/skill-patterns/SKILL_USE_CASE_LOOKUP.md) | `authoring/skill-patterns/` |
| **Commands** | COMMAND_USE_CASE_LOOKUP.md | This directory |

### Quality Rubrics

| Rubric | File | Location |
|--------|------|----------|
| **Agent Quality** | AGENT_QUALITY_RUBRIC.md | This directory (100-point scale) |
| **Skill Quality** | [SKILL_QUALITY_RUBRIC.md](../authoring/skill-patterns/SKILL_QUALITY_RUBRIC.md) | `authoring/skill-patterns/` (100-point scale) |
| **Command Quality** | COMMAND_QUALITY_RUBRIC.md | This directory (100-point scale) |

### Gold Standard Templates

| Resource Type | Template | Location |
|--------------|----------|----------|
| **Agents** | GOLD_STANDARD_AGENT.md | This directory |
| **Skills** | [GOLD_STANDARD_SKILL.md](../authoring/skill-patterns/templates/GOLD_STANDARD_SKILL.md) | `authoring/skill-patterns/` |
| **Commands** | GOLD_STANDARD_COMMAND.md | This directory |

**See:** [Phase 1-5 Implementation Plan](#implementation-status) below for roadmap.

## Implementation Status

### ✅ Phase 1: Foundation (COMPLETE)
- [x] Created `CLAUDE.md` - Unified guide for claude-code-resources
- [x] Created `MASTER_INDEX.md` - Searchable index of all 361 resources
- [x] Updated `README.md` with architecture and navigation

### ✅ Phase 2: Agent Creation System (COMPLETE)
- [x] Extracted agent patterns from existing 128 agents
- [x] Created `AGENT_PATTERN_INDEX.md` (40 patterns across 6 categories)
- [x] Created `AGENT_QUICK_START.md` (5-step process)
- [x] Created `AGENT_USE_CASE_LOOKUP.md`
- [x] Created `AGENT_QUALITY_RUBRIC.md` (100-point scale)
- [x] Created `templates/GOLD_STANDARD_AGENT.md`

### ✅ Phase 3: Command Creation System (COMPLETE)
- [x] Extracted command patterns from existing 71 commands
- [x] Created `COMMAND_PATTERN_INDEX.md` (29 patterns across 6 categories)
- [x] Created `COMMAND_QUICK_START.md` (5-step process)
- [x] Created `COMMAND_USE_CASE_LOOKUP.md`
- [x] Created `COMMAND_QUALITY_RUBRIC.md` (100-point scale)
- [x] Created `templates/GOLD_STANDARD_COMMAND.md`

### 🚧 Phase 4: Templates & Examples (Pending)
- [ ] Create agent templates (Opus/Sonnet/Haiku/Inherit)
- [ ] Create command templates (orchestration patterns)
- [ ] Create 5-10 worked examples for each resource type

### 🚧 Phase 5: Integration & Testing (Pending)
- [ ] Cross-link all guides
- [ ] Test creation workflows end-to-end
- [ ] Update root `CLAUDE.md` with navigation
- [ ] Create contribution guide for new resources

**See:** `documentation/FUTURE_PROCESSING_INSTRUCTIONS.md` for complete analysis history

## Contributing

When adding new Claude Code resources:
1. Follow the category structure in `agents/`, `skills/`, or `commands/`
2. Update the appropriate README.md index
3. Document any new prompting techniques in analysis notes
4. Maintain consistency with existing naming conventions

## License

- **wshobson/agents**: MIT License
- **daymade/claude-code-skills**: MIT License
- See individual LICENSE files in source repositories

## Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Agent Skills Guide](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
- [wshobson/agents Repository](https://github.com/wshobson/agents)
- [daymade/claude-code-skills Repository](https://github.com/daymade/claude-code-skills)

---

**Repository:** jr-mccoy/prompt-agent-engineering
**Last Updated:** 2025-12-31
**Phase 1-3 Status:** ✅ COMPLETE (Agent & Command creation systems established)
