# Coding Agents

**Purpose:** Resources for Claude Code, Codex, and similar AI coding agents.

This directory contains skills, agents, commands, and personas designed to be loaded and executed by coding agents. These are NOT copy/paste prompts - they include structured metadata, scripts, and tooling integration.

## Directory Structure

```
domain-agentic-resources/
├── skills/           # 303 skills across 28 categories
│                     # Directory-based with SKILL.md + optional scripts/, references/, assets/
│
├── agents/           # 99 agents across 16 categories
│                     # Task-specific with model recommendations (Opus/Sonnet/Haiku)
│
├── commands/         # 80 commands across 17 categories
│                     # Multi-agent orchestration workflows
│
├── personas/         # 52 personas across 9 categories
│                     # Multi-agent pipeline identities with memory
│
├── documentation/    # Implementation guides and technique analysis
│
├── MASTER_INDEX.md   # Central reference for all resources
├── CLAUDE.md         # AI agent instructions for this section
└── README_library.md # Detailed library documentation
```

## Quick Start

### Finding a Skill
```
domain-agentic-resources/skills/{category}/{skill-name}/SKILL.md
```
Skills are directory-based with progressive disclosure. Start with SKILL.md, then explore bundled resources.

### Finding an Agent
```
domain-agentic-resources/agents/{category}/{agent-name}.md
```
Agents are single files with YAML metadata specifying model, role, and capabilities.

### Finding a Command
```
domain-agentic-resources/commands/{category}/{command-name}.md
```
Commands orchestrate multiple agents for complex workflows.

### Finding a Persona
```
domain-agentic-resources/personas/{category}/{persona-name}.md
```
Personas are persistent identities with memory for multi-agent pipelines.

### Non-Coding Authoring Templates (Use First)
For non-coding resource creation, start with:
- `documentation/templates/agent_non_coding_template.md`
- `documentation/templates/skill_non_coding_template.md`
- `documentation/templates/command_non_coding_template.md`

Use these templates first, then apply category-specific pattern/rubric docs.

## Key Differences

| Resource | Purpose | Structure |
|----------|---------|-----------|
| **Skills** | Reusable capabilities | Directory with SKILL.md + resources |
| **Agents** | Task-specific execution | Single file with model recommendation |
| **Commands** | Multi-agent orchestration | Workflow definition with agent coordination |
| **Personas** | Pipeline identities | Character with memory and learning |

## For General LLM Users

If you want to copy/paste prompts into ChatGPT or Claude chat, see the domain directories (e.g., [`domain-software-engineering/`](../domain-software-engineering/), [`domain-business-strategy/`](../domain-business-strategy/)) instead.

## Related Resources

- [`domain-software-engineering/`](../domain-software-engineering/) - Software engineering prompts for copy/paste
- [`domain-business-strategy/`](../domain-business-strategy/) - Business strategy prompts for copy/paste
- [`authoring/`](../authoring/) - Guides for creating new skills, agents, commands
- [`techniques/`](../techniques/) - Prompt engineering techniques reference
