# Authoring Guides

**Purpose:** Design patterns, templates, and quality standards for creating new prompts, skills, agents, and commands.

This directory contains the authoring system - everything you need to create high-quality resources for this repository.

## Directory Structure

```
authoring/
├── NEW_PROMPT_TEMPLATE.md    # Copy-paste template for new prompts
├── NEW_RESOURCE_CHECKLIST.md # Pre-commit checklist
├── TECHNIQUE_PICKER_FAST.md  # Fast technique selection by intent
│
├── skill-patterns/      # Patterns for creating skills (41 patterns)
│   ├── SKILL_PATTERN_INDEX.md         # Complete pattern catalog + 5-step skill building process
│   ├── SKILL_USE_CASE_LOOKUP.md       # Pattern selection by use case
│   ├── SKILL_QUALITY_RUBRIC.md        # 100-point quality scoring
│   └── templates/                     # Gold standard examples
│
├── agent-patterns/      # Patterns for creating agents
│   ├── AGENT_QUICK_START.md           # 5-step agent creation process
│   ├── AGENT_PATTERN_INDEX.md         # Agent design patterns
│   ├── AGENT_USE_CASE_LOOKUP.md       # Pattern selection guide
│   └── AGENT_QUALITY_RUBRIC.md        # Quality scoring
│
├── command-patterns/    # Patterns for creating commands
│   ├── COMMAND_QUICK_START.md         # Command creation guide
│   ├── COMMAND_PATTERN_INDEX.md       # Command design patterns
│   ├── COMMAND_USE_CASE_LOOKUP.md     # Pattern selection guide
│   └── COMMAND_QUALITY_RUBRIC.md      # Quality scoring
│
├── system-patterns/     # Patterns for designing agentic systems (the fourth authoring system)
│   ├── SYSTEM_QUICK_START.md          # 6-step system authoring process (incl. Gate 0)
│   ├── SYSTEM_PATTERN_INDEX.md        # 9 topologies + structural/safety/context/eval patterns
│   ├── SYSTEM_USE_CASE_LOOKUP.md      # Pattern selection by use case
│   ├── SYSTEM_QUALITY_RUBRIC.md       # 100-point quality scoring (3 research gates load-bearing)
│   └── templates/                     # Gate/eval/architecture templates + gold-standard design
│
├── templates/           # Gold standard resource examples
│
├── INTEGRATION_PATTERNS.md            # How skills, agents, and commands compose
└── agentic_development.md             # Comprehensive agentic development guide
```

## Understanding Resource Composition

Before creating resources, understand how they work together:

**Read first:** [`INTEGRATION_PATTERNS.md`](INTEGRATION_PATTERNS.md) - Explains:
- How skills, agents, and commands compose
- Decision tree for choosing resource type
- Context passing between resources
- 5 worked examples showing composition in action

**Quick decision guide:**
| Need | Create |
|------|--------|
| Bundled scripts/templates/references | Skill |
| Specific model tier (Opus/Sonnet/Haiku) | Agent |
| Multi-phase workflow with validation gates | Command |
| Reusable domain knowledge | Skill |
| Persistent identity with expertise | Agent |
| End-to-end process orchestration | Command |
| Production multi-agent system with enforced security/safety/eval gates | System (`system-patterns/`) |

---

## Non-Coding Authoring (Start Here First)

Before creating non-coding agents, skills, or commands, start with these templates in `domain-agentic-resources/documentation/templates/`:

1. `agent_non_coding_template.md`
2. `skill_non_coding_template.md`
3. `command_non_coding_template.md`

Use the template that matches your resource type **before** applying pattern indexes or quality rubrics.

---

## Quick Start by Resource Type

### Creating a Skill
1. For non-coding work, start with `../domain-agentic-resources/documentation/templates/skill_non_coding_template.md`
2. Choose patterns from `skill-patterns/SKILL_PATTERN_INDEX.md`
3. Use case guidance: `skill-patterns/SKILL_USE_CASE_LOOKUP.md`
4. Validate with `skill-patterns/SKILL_QUALITY_RUBRIC.md`
5. See examples in `templates/`

### Creating a Prompt
1. Copy template from `NEW_PROMPT_TEMPLATE.md`
2. Pick techniques using `TECHNIQUE_PICKER_FAST.md`
3. Validate with `NEW_RESOURCE_CHECKLIST.md`
4. For deep dive: `../AI_AGENT_QUICK_START.md` or `../NON_CODING_QUICK_START.md`

### Creating an Agent
1. For non-coding work, start with `../domain-agentic-resources/documentation/templates/agent_non_coding_template.md`
2. Then use `agent-patterns/AGENT_QUICK_START.md`
3. Choose patterns from `agent-patterns/AGENT_PATTERN_INDEX.md`
4. Use case guidance: `agent-patterns/AGENT_USE_CASE_LOOKUP.md`
5. Validate with `agent-patterns/AGENT_QUALITY_RUBRIC.md`
6. See examples in `../domain-agentic-resources/agents/`

### Creating a Command
1. For non-coding work, start with `../domain-agentic-resources/documentation/templates/command_non_coding_template.md`
2. Then use `command-patterns/COMMAND_QUICK_START.md`
3. Choose patterns from `command-patterns/COMMAND_PATTERN_INDEX.md`
4. Use case guidance: `command-patterns/COMMAND_USE_CASE_LOOKUP.md`
5. Validate with `command-patterns/COMMAND_QUALITY_RUBRIC.md`
6. See examples in `../domain-agentic-resources/commands/`

### Designing an Agentic System
1. Read `system-patterns/SYSTEM_QUICK_START.md` for the 6-step process
2. **Gate 0 first** — justify the agent (complexity ladder: function → workflow → agent → multi-agent)
3. Choose patterns from `system-patterns/SYSTEM_PATTERN_INDEX.md` (9 topologies + safety/eval patterns)
4. Use case guidance: `system-patterns/SYSTEM_USE_CASE_LOOKUP.md`
5. Validate with `system-patterns/SYSTEM_QUALITY_RUBRIC.md` (target ≥75; security/eval/governance gates are load-bearing)
6. Or run the **guided factory** end-to-end: `../agentic-system-factory/orchestrator_agentic_system.md`

## Naming Conventions

### Prompts
```
{category}_{specific_function}.md
# Examples:
# security_vulnerability_analysis.md
# performance_bottleneck_identification.md
```

### Skills
```
{skill-name}/           # kebab-case directory
├── SKILL.md            # Required metadata + instructions
├── scripts/            # Optional executable scripts
├── references/         # Optional reference docs
└── assets/             # Optional templates, JSON
```

### Agents
```
{domain}-{role-descriptor}.md
# Examples:
# security_vulnerability_scanner.md
# backend_api_architect.md
```

## Related Resources

- [`domain-software-engineering/`](../domain-software-engineering/) - Destination for software engineering prompts
- [`domain-business-strategy/`](../domain-business-strategy/) - Destination for business strategy prompts
- [`domain-agentic-resources/`](../domain-agentic-resources/) - Destination for new skills, agents, commands
- [`domain-AI-ML/agentic-ai-systems/`](../domain-AI-ML/agentic-ai-systems/) - Agent-design prompt library (`aiagent_*`) that `system-patterns/` orchestrates
- [`../agentic-system-factory/`](../agentic-system-factory/) - Guided factory that produces a production-ready agentic system from a use case
- [`techniques/`](../techniques/) - Technique reference for prompt building
