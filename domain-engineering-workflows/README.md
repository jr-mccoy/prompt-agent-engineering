# Domain: Engineering Workflows

**Purpose:** Prompts for engineering project management, sprint planning, debugging workflows, task completion verification, and continuous improvement.

---

## What This Domain Covers

Engineering process and workflow prompts:

1. **Workflows** - Sprint planning, debugging, postmortems, code reviews
2. **Tasks** - Task sorting, prioritization, breakdown
3. **Improvement** - Refactoring guidance, technical debt
4. **AI Patterns** - AI-assisted development patterns
5. **AI-Native Rollouts** - Team / org-level AI adoption design (review systems, tiered rollouts, delegation practice, project memory, bottleneck migration)

---

## Directory Structure

```
domain-engineering-workflows/
├── workflows/                # Sprint planning, debugging, postmortems
├── ai-patterns/              # AI-assisted development patterns
├── ai-native-rollouts/       # Team/org AI adoption design
├── done-definition/          # Done gates, stop policies, convergent agentic loops
└── README.md
```

---

## File Count

| Subdirectory | Count | Description |
|--------------|-------|-------------|
| `workflows/` | ~18 | Sprint planning, debugging, reviews, specification & delegation |
| `ai-patterns/` | ~23 | AI-assisted development patterns |
| `ai-native-rollouts/` | 7 | Ambient code review, tiered rollout, ship-by-delegation, delegation brief, project memory, bottleneck migration |
| `done-definition/` | 6 | Done-definition pipeline: task-to-gate translation, stop policy, convergent loops, false-done hardening, domain gate baselines, troubleshooting |
| **Total** | **~54** | |

---

## Key Patterns

### Sprint Planning
- Backlog grooming
- Story point estimation
- Sprint scope definition
- Risk identification

### Debugging Workflows
- Root cause analysis
- Systematic debugging steps
- Issue reproduction
- Fix verification

### Improvement Workflows
- Repository-wide audit planning and phased implementation roadmaps
- Prompt quality normalization and metadata governance
- Refactoring and maintainability modernization

Key improvement prompt:
- `domain-software-engineering/improvement/improvement_repo_audit_master_prompt.md` - Master prompt for full-repo quality/structure audits with phased execution planning

---

## When to Use This Domain

Use these prompts when you need to:
- Plan sprints or iterations
- Debug issues systematically
- Verify task completion
- Run postmortems
- Prioritize engineering work

**Do NOT use for:**
- Code analysis (use domain-software-engineering)
- Business strategy (use domain-business-strategy)
- Personal productivity (use domain-productivity)

---

*Migrated from: `prompts/engineering/`*
