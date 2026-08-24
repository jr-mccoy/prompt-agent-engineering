# Agent Authoring Patterns

Design patterns and templates for creating Claude Code agents.

## Key Files

| File | Purpose |
|------|---------|
| `AGENT_QUICK_START.md` | 5-step agent creation process |
| `AGENT_PATTERN_INDEX.md` | Agent design patterns catalog |
| `AGENT_USE_CASE_LOOKUP.md` | Pattern selection by use case |
| `AGENT_QUALITY_RUBRIC.md` | Quality scoring system |

## Quick Start

1. Read `AGENT_QUICK_START.md` for the process overview
2. Choose patterns from `AGENT_PATTERN_INDEX.md`
3. Use the templates in this directory
4. Validate with `AGENT_QUALITY_RUBRIC.md`

## Agent Structure

```yaml
---
name: agent-name
model: opus|sonnet|haiku|inherit
role: Brief role description
---

# Agent Name

## Capabilities
- List of capabilities

## Instructions
Detailed instructions...
```

## Related Resources

- [`domain-agentic-resources/agents/`](../../domain-agentic-resources/agents/) - Browse existing agents
- [`authoring/skill-patterns/`](../skill-patterns/) - Skill creation patterns
- [`authoring/command-patterns/`](../command-patterns/) - Command creation patterns
- [`authoring/system-patterns/`](../system-patterns/) - Agentic system design patterns (multi-agent, gated; the guided factory is `agentic-system-factory/`)
