# New Resource Checklist

**Purpose:** One-page checklist for adding any new prompt, skill, agent, or command to this repository.

---

## Pre-Flight Checks

Before creating, confirm:

- [ ] **Not a duplicate:** Searched existing resources and found no close match
- [ ] **Right resource type:** Chose between prompt/skill/agent/command (see decision guide below)
- [ ] **Clear use case:** Can describe in one sentence who uses this and why

---

## Technique Selection

- [ ] **Pick 3–5 techniques max.** More techniques = more complexity = harder to maintain.
- [ ] **Use canonical IDs only.** Reference [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md) for valid IDs.
- [ ] **Don't use deprecated IDs.** Check for "DEPRECATED" or "Merged into" notes.
- [ ] **Use [TECHNIQUE_PICKER_FAST.md](TECHNIQUE_PICKER_FAST.md)** to select by intent.

---

## Constraint Requirements

- [ ] **Include at least 2 "Must Not" constraints when relevant.**
  - Prevents hallucination: "Must not invent information"
  - Prevents scope creep: "Must not exceed specified scope"
  - Prevents format drift: "Must not deviate from output structure"

- [ ] **Constraints are testable.** Each constraint should be verifiable by reading the output.

---

## Verification / Done Definition

- [ ] **Define what "done" means.** Include at least one of:
  - Self-check checklist (minimum)
  - Explicit verification step (for important work)
  - Gate-based criteria (for critical work — see DD-04, QA-08)

- [ ] **Include evidence requirements.** Outputs should cite sources, file paths, or reasoning — not just assert conclusions.

---

## File Placement

| Resource Type | Destination |
|---------------|-------------|
| **Prompt (coding/technical)** | `domain-software-engineering/` subdirectory by topic |
| **Prompt (non-coding)** | Appropriate `domain-*/` directory |
| **Skill** | `domain-agentic-resources/skills/` |
| **Agent** | `domain-agentic-resources/agents/` |
| **Command** | `domain-agentic-resources/commands/` |

### Naming Convention

```
{category}_{specific_function}.md
```

Examples:
- `security_vulnerability_analysis.md`
- `performance_bottleneck_identification.md`
- `quality_code_complexity_analysis.md`

---

## Index/Lookup Updates

- [ ] **Update lookup docs only if needed.** Don't update if:
  - Resource fits existing category well
  - Existing examples cover the use case

- [ ] **Do update if:**
  - New category or subcategory added
  - Resource introduces novel technique combination
  - Significantly expands repository scope

---

## Quality Checklist

### Structure
- [ ] Has clear **Objective** (one sentence)
- [ ] Has **Inputs/Context** section
- [ ] Has **Constraints** (Must + Must Not)
- [ ] Has numbered **Steps**
- [ ] Has explicit **Output Format**
- [ ] Has **Verification** section

### Content
- [ ] Uses only canonical technique IDs
- [ ] Constraints are specific and testable
- [ ] Output format is explicit (not vague like "detailed report")
- [ ] Works standalone (doesn't require reading other docs first)

### Portability
- [ ] No platform-specific assumptions (unless explicitly labeled)
- [ ] No model-specific assumptions (unless in model-specific directory)
- [ ] Cross-platform compatible (paths, commands, formatting)

---

## Decision Guide: Resource Type

| Need | Create |
|------|--------|
| One-time task, no bundled resources | **Prompt** |
| Reusable capability with scripts/templates | **Skill** |
| Persistent identity with specific model tier | **Agent** |
| Multi-phase workflow with validation gates | **Command** |

**When in doubt:** Start with a prompt. Graduate to skill/agent/command if reuse pattern emerges.

---

## Final Check

Before committing:

- [ ] Template was used: [NEW_PROMPT_TEMPLATE.md](NEW_PROMPT_TEMPLATE.md)
- [ ] Technique IDs are canonical
- [ ] At least 2 Must-Not constraints (when relevant)
- [ ] Done/verification is defined
- [ ] File is in correct directory
- [ ] No unnecessary index updates

---

## Related Resources

- **Template:** [NEW_PROMPT_TEMPLATE.md](NEW_PROMPT_TEMPLATE.md)
- **Technique picker:** [TECHNIQUE_PICKER_FAST.md](TECHNIQUE_PICKER_FAST.md)
- **Full technique reference:** [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md)
- **Skill creation:** [skill-patterns/SKILL_PATTERN_INDEX.md](../resource-patterns/skill-patterns/SKILL_PATTERN_INDEX.md)
- **Agent creation:** [agent-patterns/AGENT_QUICK_START.md](../resource-patterns/agent-patterns/AGENT_QUICK_START.md)

---

**Last Updated:** 2026-01-31
