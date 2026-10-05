# Claude Code Resources

This directory contains **agents**, **skills**, and **commands** for Claude Code - specialized AI capabilities that extend Claude's functionality for software development workflows.

---

## ⚠️ Important: This is the Implementation Library

**This directory (`domain-agentic-resources/`) contains production-ready resources you can USE immediately.**

| Directory | Purpose | Contains |
|-----------|---------|----------|
| **`domain-agentic-resources/`** (this) | 📚 **Implementation Library** | 340 skills, 147 agents, 119 commands, 57 personas ready to use |
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
| **[MASTER_INDEX.md](master_index.md)** | 🔍 Searchable index of all 606 agents, skills and commands | Finding specific resources |
| **[agents/README.md](agents/README.md)** | 🤖 147 agents with model assignments | Browse agents |
| **[skills/README.md](skills/README.md)** | 🎓 340 skills with bundled resources | Browse skills |
| **[commands/README.md](commands/README.md)** | ⚙️ 119 commands with orchestration | Browse commands |
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
│   ├── architecture/ (6 agents)
│   ├── backend/ (8 agents)
│   ├── business-operations/ (11 agents)
│   ├── cloud-infrastructure/ (9 agents)
│   ├── code-quality/ (4 agents)
│   ├── database/ (4 agents)
│   ├── deployment/ (3 agents)
│   ├── devops/ (6 agents)
│   ├── documentation/ (5 agents)
│   ├── frontend-mobile/ (22 agents)
│   ├── languages/ (21 agents)
│   ├── ml-ai/ (6 agents)
│   ├── non-coding/ (12 agents)
│   ├── orchestration/ (4 agents)
│   ├── security/ (4 agents)
│   ├── seo-marketing/ (12 agents)
│   ├── testing/ (5 agents)
│   └── web-development/ (5 agents)
├── skills/
│   ├── README.md (skill index and guide)
│   ├── accessibility/ (4 skills)
│   ├── backend-development/ (13 skills)
│   ├── blockchain-web3/ (16 skills)
│   ├── cicd-automation/ (4 skills)
│   ├── cloud-infrastructure/ (14 skills)
│   ├── content-creation/ (5 skills)
│   ├── data-engineering/ (10 skills)
│   ├── developer-tools/ (36 skills)
│   ├── devops/ (5 skills)
│   ├── document-processing/ (7 skills)
│   ├── financial-records/ (4 skills)
│   ├── framework-migration/ (4 skills)
│   ├── game-development/ (4 skills)
│   ├── languages/ (18 skills)
│   ├── llm-application-dev/ (11 skills)
│   ├── marketing/ (41 skills)
│   ├── ml-ai/ (4 skills)
│   ├── mobile-development/ (36 skills)
│   ├── non-coding/ (26 skills)
│   ├── observability/ (6 skills)
│   ├── other/ (2 skills)
│   ├── payments/ (4 skills)
│   ├── security/ (36 skills)
│   ├── seo-marketing/ (4 skills)
│   ├── testing-qa/ (18 skills)
│   └── web-development/ (8 skills)
├── commands/
│   ├── README.md (command index and guide)
│   ├── accessibility/ (2 commands)
│   ├── architecture/ (2 commands)
│   ├── code-quality/ (5 commands)
│   ├── data-analysis/ (3 commands)
│   ├── database/ (2 commands)
│   ├── deployment/ (2 commands)
│   ├── devops/ (8 commands)
│   ├── documentation/ (3 commands)
│   ├── framework-migration/ (3 commands)
│   ├── git-workflows/ (3 commands)
│   ├── mobile-development/ (12 commands)
│   ├── multi-agent/ (8 commands)
│   ├── non-coding/ (19 commands)
│   ├── orchestration/ (9 commands)
│   ├── other/ (18 commands)
│   ├── performance/ (3 commands)
│   ├── security/ (6 commands)
│   ├── testing/ (6 commands)
│   └── troubleshooting/ (5 commands)
├── personas/
│   ├── README.md (persona index and pipeline guide)
│   ├── design/ (7 personas)
│   ├── engineering/ (7 personas)
│   ├── marketing/ (8 personas)
│   ├── product/ (5 personas)
│   ├── project-management/ (5 personas)
│   ├── spatial-computing/ (6 personas)
│   ├── specialized/ (6 personas)
│   ├── support/ (6 personas)
│   └── testing/ (7 personas)
└── documentation/
    ├── TECHNIQUE_USAGE_MATRIX.csv
    ├── integration_with_prompts.md
    ├── novel_techniques_candidates.md
    ├── novel_techniques_comprehensive_candidates.md
    ├── policies/
    ├── resource_metadata_spec.md
    ├── technique-analyses/
    ├── technique_analysis_template.md
    └── templates/
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
