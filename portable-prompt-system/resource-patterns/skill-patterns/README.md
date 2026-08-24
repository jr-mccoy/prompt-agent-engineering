> **Portable-bundle note:** These authoring patterns assume the Claude Code ecosystem (e.g., the Task tool, `subagent_type`, `.claude/` settings). Any references to the source repository's `domain-agentic-resources/` library or `domain-*` example resources are **illustrative** — those files are not included in this bundle. The patterns, indexes, rubrics, and templates here are fully usable on their own to author new skills, agents, and commands.

# Agent Skills Authoring System

> **Comprehensive guide for AI agents to create high-quality Agent Skills.**
>
> This system enables AI agents to build modular, discoverable, production-grade skills that extend agent capabilities.

---

## ⚠️ Important: This is the Authoring System, Not the Implementation Library

**This directory (`authoring/skill-patterns/`) contains design guides for CREATING new skills.**

| Directory | Purpose | Contains |
|-----------|---------|----------|
| **`authoring/skill-patterns/`** (this) | 📐 **Authoring System** | Design patterns, templates, quality rubrics for creating skills |
| **`domain-agentic-resources/`** | 📚 **Implementation Library** | Production skills, agents, and commands ready to use |

**Use this directory when:** You want to **build a new skill** from scratch
**Use `domain-agentic-resources/` when:** You want to **find and use an existing skill**

### Quick Decision

```
"I need to USE a skill" → Go to domain-agentic-resources/skills/
"I need to CREATE a skill" → Stay here (authoring/skill-patterns/)
"I need to CREATE an agent" → Go to authoring/agent-patterns/AGENT_QUICK_START.md
"I need to CREATE a command" → Go to authoring/command-patterns/COMMAND_QUICK_START.md
```

---

## Quick Navigation

| Resource | Purpose | When to Use |
|----------|---------|-------------|
| [**SKILL_PATTERN_INDEX.md**](SKILL_PATTERN_INDEX.md) | 5-step skill building process and 41 patterns | Starting any new skill |
| [**SKILL_PATTERN_INDEX.md**](SKILL_PATTERN_INDEX.md) | 41 patterns for skill design | Deep dive on specific patterns |
| [**SKILL_USE_CASE_LOOKUP.md**](SKILL_USE_CASE_LOOKUP.md) | Pattern selection by user need | Finding right patterns quickly |
| [**SKILL_QUALITY_RUBRIC.md**](SKILL_QUALITY_RUBRIC.md) | 100-point scoring system | Validating skill quality |
| [**templates/GOLD_STANDARD_SKILL.md**](templates/GOLD_STANDARD_SKILL.md) | Annotated example skill | Learning by example |

---

## What is an Agent Skill?

An **Agent Skill** is a modular, self-describing capability that an AI agent can:
- **Discover** through metadata matching
- **Load** when relevant to the task
- **Execute** with specialized knowledge and tools

Skills transform general-purpose AI agents into domain experts on-demand.

### Skill Architecture

```
skill-name/
├── SKILL.md              # Required: Metadata + Instructions
├── scripts/              # Optional: Executable automation
├── references/           # Optional: Deep documentation
└── assets/               # Optional: Templates and resources
```

### Progressive Disclosure

Skills use three-tier loading for context efficiency:

```
Tier 1: Metadata (always loaded) ─────────── ~100 words
        └─ name + description for matching

Tier 2: SKILL.md body (on activation) ────── <5k words
        └─ Core instructions for execution

Tier 3: Bundled resources (on demand) ────── Unlimited
        └─ scripts/, references/, assets/
```

---

## How to Use This System

### Decision Tree: Creating vs Using Skills

```
User Request
│
├─→ "Create a skill for..."
│   │
│   └─→ USE THIS SYSTEM
│       1. Read SKILL_PATTERN_INDEX.md
│       2. Classify skill type
│       3. Select patterns from USE_CASE_LOOKUP.md
│       4. Build using patterns from PATTERN_INDEX.md
│       5. Validate with QUALITY_RUBRIC.md
│
├─→ "Help me with [task]..."
│   │
│   └─→ FIND EXISTING SKILL
│       1. Search domain-agentic-resources/skills/
│       2. Match task to skill description
│       3. Load and execute skill
│
└─→ "How do skills work?"
    │
    └─→ REFERENCE THIS DOCUMENTATION
        1. Read this README for overview
        2. Study GOLD_STANDARD_SKILL.md for examples
        3. Review PATTERN_INDEX.md for techniques
```

---

## Skill Types and Templates

| Type | Description | Primary Patterns |
|------|-------------|-----------------|
| **WORKFLOW** | Multi-step sequential processes | SP-02, WP-01, WP-02 |
| **TOOL** | Technology/tool mastery | SP-03, IP-02, RP-02 |
| **DOMAIN** | Domain expertise | SP-04, QP-05, QP-06 |
| **CREATION** | Generate artifacts | SP-05, RP-03, MG-02 |
| **ANALYSIS** | Troubleshoot/diagnose | SP-06, WP-04, QP-05 |
| **INTEGRATION** | External connections | IP-01, IP-03, IP-04 |
| **META** | Create other skills | MG-01, MG-02, QP-01 |

---

## Quick Start: 5 Steps

### Step 1: Classify
What type of skill is this? (WORKFLOW, TOOL, DOMAIN, CREATION, ANALYSIS, INTEGRATION, META)

### Step 2: Structure
Choose organization pattern based on type (see SKILL_PATTERN_INDEX.md).

### Step 3: Build
Create SKILL.md with:
- YAML frontmatter (name, description)
- Markdown body (instructions)

### Step 4: Resource
Add bundled resources as needed:
- scripts/ for automation
- references/ for documentation
- assets/ for templates

### Step 5: Validate
Score against QUALITY_RUBRIC.md (target: 75+).

---

## Pattern Quick Reference

### Always Apply These Patterns

| Pattern | What It Does |
|---------|--------------|
| SP-01 | Progressive disclosure (defer detail) |
| SP-08 | Link related skills |
| MP-01 | Include trigger phrases in description |
| MP-02 | Use third-person voice |
| RP-06 | Use relative paths only |

### Apply Based on Type

| Skill Type | Key Patterns |
|------------|--------------|
| WORKFLOW | SP-02 (numbered steps), WP-01 (skip conditions), WP-02 (validation) |
| TOOL | SP-03 (task-based), IP-02 (CLI patterns), RP-02 (named references) |
| DOMAIN | SP-04 (knowledge org), QP-05 (edge cases), QP-06 (safety) |
| CREATION | SP-05 (input-output), RP-03 (templates), MG-02 (scaffolding) |
| ANALYSIS | SP-06 (investigation), WP-04 (branching), QP-05 (edge cases) |
| INTEGRATION | IP-01 (API docs), IP-03 (errors), IP-04 (rate limits) |
| META | MG-01 (self-exemplifying), MG-02 (templates), QP-01 (validation) |

---

## Quality Standards

### Minimum Bar (Must Pass)

- [ ] Name matches folder name
- [ ] Description describes WHAT and WHEN
- [ ] SKILL.md valid (YAML frontmatter + markdown)
- [ ] All referenced files exist
- [ ] No hardcoded secrets or absolute paths
- [ ] Instructions are agent-executable

### Quality Bar (Should Pass)

- [ ] SKILL.md < 500 lines
- [ ] "When to Use" and "When NOT to Use" sections
- [ ] Related Skills section
- [ ] Edge cases documented

### Target Score: 75/100

Use [SKILL_QUALITY_RUBRIC.md](SKILL_QUALITY_RUBRIC.md) for detailed scoring.

---

## Example Skills to Study

From `domain-agentic-resources/skills/`:

| Skill | Type | Notable Patterns |
|-------|------|-----------------|
| `helm-chart-scaffolding` | WORKFLOW | Steps, templates, validation |
| `github-ops` | INTEGRATION | API docs, operations, errors |
| `skill-creator` | META | Self-exemplifying, scripts, validation |
| `cloudflare-troubleshooting` | ANALYSIS | Investigation, diagnostics, issues |
| `pdf-creator` | CREATION | Input-output, scripts |

---

## Integration with Prompt System

This skill authoring system complements the prompt creation system:

| System | Purpose | Entry Point |
|--------|---------|-------------|
| **Prompt System** | Create one-off prompts | `AI_AGENT_QUICK_START.md` |
| **Skill System** | Create reusable capabilities | `authoring/skill-patterns/SKILL_PATTERN_INDEX.md` |

**When to create a skill vs prompt:**
- **Skill:** Reusable across sessions, needs bundled resources, complex workflow
- **Prompt:** One-time use, no external resources needed, simple structure

---

## Files in This Directory

```
authoring/skill-patterns/
├── README.md                        # This file: Overview and navigation
├── SKILL_PATTERN_INDEX.md       # Main guide: 5-step process
├── SKILL_PATTERN_INDEX.md           # Pattern catalog: 41 patterns
├── SKILL_USE_CASE_LOOKUP.md         # Pattern selection: By user need
├── SKILL_QUALITY_RUBRIC.md          # Quality scoring: 100-point scale
└── templates/
    └── GOLD_STANDARD_SKILL.md       # Annotated example skill
```

---

## Related Resources

> **🔗 See Also:** The [domain-agentic-resources/](../../../domain-agentic-resources/) directory contains the **implementation library** with production-ready skills you can use immediately.

| Resource | Location | Purpose |
|----------|----------|---------|
| **Implementation Library** | `domain-agentic-resources/` | 📚 All agents, skills, commands |
| Existing Skills | `domain-agentic-resources/skills/` | Production skills to use |
| Agent Creation Guide | `authoring/agent-patterns/AGENT_QUICK_START.md` | Create new agents |
| Command Creation Guide | `authoring/command-patterns/COMMAND_QUICK_START.md` | Create new commands |
| Skills Index | `domain-agentic-resources/skills/README.md` | Browse skill catalog |
| Skill Creator Skill | `domain-agentic-resources/skills/developer-tools/skill-creator/` | Meta-skill for creation |
| Technique Analyses | `domain-agentic-resources/documentation/technique-analyses/skills/` | Pattern analysis |

---

## Contribution

When adding new patterns or improving this system:

1. **New Pattern:** Add to SKILL_PATTERN_INDEX.md with:
   - Clear code (SP-XX, MP-XX, etc.)
   - Description and implementation
   - When to use
   - Example from real skill

2. **New Use Case:** Add to SKILL_USE_CASE_LOOKUP.md with:
   - User intent pattern
   - Recommended skill type
   - Pattern combination
   - Template structure

3. **Quality Criteria:** Update SKILL_QUALITY_RUBRIC.md with:
   - New criteria and points
   - Scoring examples
   - Common deductions

---

## Version History

- **v1.0.0** (2025-12-23): Initial system release
  - 5-step skill building process
  - 41 documented patterns across 7 categories
  - 100-point quality rubric
  - Complete annotated example

---

**Start building skills:** [SKILL_PATTERN_INDEX.md](SKILL_PATTERN_INDEX.md)
