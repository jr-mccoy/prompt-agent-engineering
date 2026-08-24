# Claude Code Resource Templates

**Purpose:** Templates and worked examples for creating agents, commands, and integrated workflows.

**Total Templates:** 8 templates + 7 worked examples

---

## Table of Contents

- [Agent Templates](#agent-templates)
- [Command Templates](#command-templates)
- [Gold Standard Examples](#gold-standard-examples)
- [Worked Examples](#worked-examples)
- [How to Use](#how-to-use)

---

## Agent Templates

Templates for creating agents by model tier. Each template includes:
- Complete structure with placeholders
- Pattern references
- Usage instructions
- Quality validation guidance

| Template | Model Tier | Best For |
|----------|------------|----------|
| [opus_critical_agent_template.md](agent-templates/opus_critical_agent_template.md) | Opus | Architecture, security, critical analysis |
| [sonnet_balanced_agent_template.md](agent-templates/sonnet_balanced_agent_template.md) | Sonnet | General development, balanced tasks |
| [haiku_fast_agent_template.md](agent-templates/haiku_fast_agent_template.md) | Haiku | Quick operations, diagram generation |
| [inherit_user_choice_agent_template.md](agent-templates/inherit_user_choice_agent_template.md) | Inherit | User-controlled, flexible tasks |

### Agent Template Selection Guide

```
Is the task security/architecture critical?
├── YES → Use opus_critical_agent_template.md
└── NO
    └── Is speed the priority?
        ├── YES → Use haiku_fast_agent_template.md
        └── NO
            └── Should user choose the model?
                ├── YES → Use inherit_user_choice_agent_template.md
                └── NO → Use sonnet_balanced_agent_template.md
```

---

## Command Templates

Templates for creating commands by workflow type. Each template includes:
- Multi-phase structure
- Agent invocation patterns
- Validation gates
- Error handling

| Template | Workflow Type | Best For |
|----------|---------------|----------|
| [multi_agent_orchestration_template.md](command-templates/multi_agent_orchestration_template.md) | Multi-phase parallel | Full-stack features, complex deployments |
| [sequential_workflow_template.md](command-templates/sequential_workflow_template.md) | Linear pipeline | Code review, git workflows |
| [parallel_execution_template.md](command-templates/parallel_execution_template.md) | Parallel tasks | Multi-component implementation |
| [validation_gate_template.md](command-templates/validation_gate_template.md) | Quality-focused | Security scanning, compliance |

### Command Template Selection Guide

```
Do tasks have dependencies between them?
├── YES → Does each step need the previous step's output?
│   ├── YES → Use sequential_workflow_template.md
│   └── NO → Use multi_agent_orchestration_template.md
└── NO → Are tasks completely independent?
    ├── YES → Use parallel_execution_template.md
    └── Is validation the main focus?
        └── YES → Use validation_gate_template.md
```

---

## Gold Standard Examples

Fully annotated examples showing all best practices:

| Example | Type | Score |
|---------|------|-------|
| [GOLD_STANDARD_AGENT.md](GOLD_STANDARD_AGENT.md) | Agent | 95/100 |
| [GOLD_STANDARD_COMMAND.md](GOLD_STANDARD_COMMAND.md) | Command | 92/100 |

These files include:
- Complete implementations
- `<!-- ANNOTATION: ... -->` comments explaining each section
- `<!-- PATTERN: ... -->` references to pattern index
- Scoring breakdown
- Adaptation guidance

---

## Worked Examples

Complete, step-by-step examples showing the creation process from start to finish:

### Agent Creation Examples

| # | Example | Focus | Time |
|---|---------|-------|------|
| 01 | [example_01_opus_security_agent.md](worked-examples/example_01_opus_security_agent.md) | Opus-tier security agent | 45 min |
| 02 | [example_02_haiku_diagram_agent.md](worked-examples/example_02_haiku_diagram_agent.md) | Haiku-tier diagram generator | 20 min |

### Command Creation Examples

| # | Example | Focus | Time |
|---|---------|-------|------|
| 03 | [example_03_sequential_testing_command.md](worked-examples/example_03_sequential_testing_command.md) | Sequential testing pipeline | 30 min |
| 04 | [example_04_parallel_analysis_command.md](worked-examples/example_04_parallel_analysis_command.md) | Parallel code analysis | 35 min |

### Integration Examples

| # | Example | Focus | Time |
|---|---------|-------|------|
| 05 | [example_05_agent_skill_integration.md](worked-examples/example_05_agent_skill_integration.md) | Agent + Skill integration | 25 min |
| 06 | [example_06_command_multi_agent.md](worked-examples/example_06_command_multi_agent.md) | Command + Multiple agents | 40 min |
| 07 | [example_07_full_workflow_integration.md](worked-examples/example_07_full_workflow_integration.md) | Complete agent + skill + command | 60 min |

---

## How to Use

### For Creating a New Agent

1. **Select template by model tier:**
   - Critical task? → `opus_critical_agent_template.md`
   - General task? → `sonnet_balanced_agent_template.md`
   - Quick task? → `haiku_fast_agent_template.md`
   - User-controlled? → `inherit_user_choice_agent_template.md`

2. **Study the gold standard:** Review `GOLD_STANDARD_AGENT.md`

3. **Follow worked example:** Work through `example-01` or `example-02`

4. **Validate:** Use [AGENT_QUALITY_RUBRIC.md](../agent-patterns/AGENT_QUALITY_RUBRIC.md)

### For Creating a New Command

1. **Select template by workflow:**
   - Complex multi-phase? → `multi_agent_orchestration_template.md`
   - Linear pipeline? → `sequential_workflow_template.md`
   - Independent tasks? → `parallel_execution_template.md`
   - Quality gates focus? → `validation_gate_template.md`

2. **Study the gold standard:** Review `GOLD_STANDARD_COMMAND.md`

3. **Follow worked example:** Work through `example-03` or `example-04`

4. **Validate:** Use [COMMAND_QUALITY_RUBRIC.md](../command-patterns/COMMAND_QUALITY_RUBRIC.md)

### For Integration Patterns

1. **Agent + Skill:** Study `example_05_agent_skill_integration.md`
2. **Command + Agents:** Study `example_06_command_multi_agent.md`
3. **Full workflow:** Study `example_07_full_workflow_integration.md`

---

## Related Resources

| Resource | Purpose |
|----------|---------|
| [AGENT_QUICK_START.md](../agent-patterns/AGENT_QUICK_START.md) | 5-step agent creation |
| [AGENT_PATTERN_INDEX.md](../agent-patterns/AGENT_PATTERN_INDEX.md) | 40 agent patterns |
| [AGENT_QUALITY_RUBRIC.md](../agent-patterns/AGENT_QUALITY_RUBRIC.md) | Agent scoring |
| [COMMAND_QUICK_START.md](../command-patterns/COMMAND_QUICK_START.md) | 5-step command creation |
| [COMMAND_PATTERN_INDEX.md](../command-patterns/COMMAND_PATTERN_INDEX.md) | 29 command patterns |
| [COMMAND_QUALITY_RUBRIC.md](../command-patterns/COMMAND_QUALITY_RUBRIC.md) | Command scoring |

---

**Last Updated:** 2026-01-02
**Phase:** 4 (Templates & Examples) Complete
