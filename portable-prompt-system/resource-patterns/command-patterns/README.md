> **Portable-bundle note:** These authoring patterns assume the Claude Code ecosystem (e.g., the Task tool, `subagent_type`, `.claude/` settings). Any references to the source repository's `domain-agentic-resources/` library or `domain-*` example resources are **illustrative** — those files are not included in this bundle. The patterns, indexes, rubrics, and templates here are fully usable on their own to author new skills, agents, and commands.

# Command Authoring Patterns

Design patterns and templates for creating multi-agent orchestration commands.

## Key Files

| File | Purpose |
|------|---------|
| `COMMAND_QUICK_START.md` | Command creation process |
| `COMMAND_PATTERN_INDEX.md` | Command design patterns catalog |
| `COMMAND_USE_CASE_LOOKUP.md` | Pattern selection by use case |
| `COMMAND_QUALITY_RUBRIC.md` | Quality scoring system |

## Quick Start

1. Read `COMMAND_QUICK_START.md` for the process overview
2. Choose patterns from `COMMAND_PATTERN_INDEX.md`
3. Use the templates in this directory
4. Validate with `COMMAND_QUALITY_RUBRIC.md`

## Command Structure

Commands orchestrate multiple agents:

```markdown
# /command-name

## Workflow
1. Agent A: Initial analysis
2. Agent B: Implementation
3. Agent C: Validation
4. Agent D: Documentation

## Validation Gates
- Gate 1: Analysis complete
- Gate 2: Tests passing
- Gate 3: Review approved
```

## Related Resources

- `domain-agentic-resources/commands/` - Browse existing commands
- [`authoring/agent-patterns/`](../agent-patterns/) - Agent creation patterns
