# Agency Agents: Role-Based AI Personas

A sophisticated collection of **51 AI agent personalities** designed for collaborative, autonomous development workflows. Unlike task-focused prompts, these agents have persistent identities with personality traits, memory systems, and orchestration capabilities.

## Overview

Agency Agents are designed for **multi-agent orchestration**—where specialized agents collaborate through coordinated pipelines with quality gates, handoff protocols, and retry logic.

### Key Differentiators from Standard Prompts

| Aspect | Standard Prompts | Agency Agents |
|--------|------------------|---------------|
| **Focus** | Single task execution | Persistent role identity |
| **Identity** | Expert role assignment | Personality + Memory + Experience |
| **Workflow** | One-shot execution | Pipeline coordination |
| **Quality** | Output verification | Evidence-based decision gates |
| **Learning** | None | Memory architecture for patterns |

---

## Directory Structure

```
agency-agents/
├── design/                    # 6 agents
│   ├── design_brand_guardian.md
│   ├── design_ui_designer.md
│   ├── design_ux_architect.md
│   ├── design_ux_researcher.md
│   ├── design_visual_storyteller.md
│   └── design_whimsy_injector.md      ⭐ Unique personality system
│
├── engineering/               # 7 agents
│   ├── engineering_ai_engineer.md
│   ├── engineering_backend_architect.md
│   ├── engineering_devops_automator.md
│   ├── engineering_frontend_developer.md
│   ├── engineering_mobile_app_builder.md
│   ├── engineering_rapid_prototyper.md
│   └── engineering_senior_developer.md
│
├── marketing/                 # 8 agents
│   ├── marketing_app_store_optimizer.md
│   ├── marketing_content_creator.md
│   ├── marketing_growth_hacker.md
│   ├── marketing_instagram_curator.md
│   ├── marketing_reddit_community_builder.md
│   ├── marketing_social_media_strategist.md
│   ├── marketing_tiktok_strategist.md
│   └── marketing_twitter_engager.md
│
├── product/                   # 3 agents
│   ├── product_feedback_synthesizer.md
│   ├── product_sprint_prioritizer.md
│   └── product_trend_researcher.md
│
├── project-management/        # 5 agents
│   ├── project_experiment_tracker.md
│   ├── project_manager_senior.md       ⭐ Spec-to-task conversion
│   ├── project_shepherd.md
│   ├── project_studio_operations.md
│   └── project_studio_producer.md
│
├── spatial-computing/         # 5 agents
│   ├── spatial_macos_metal_engineer.md
│   ├── spatial_terminal_integration.md
│   ├── spatial_visionos_engineer.md
│   ├── spatial_xr_cockpit_specialist.md
│   └── spatial_xr_interface_architect.md
│
├── specialized/               # 3 agents
│   ├── agents_orchestrator.md          ⭐ Pipeline manager
│   ├── data_analytics_reporter.md
│   └── specialized_lsp_index_engineer.md
│
├── support/                   # 7 agents
│   ├── support_analytics_reporter.md
│   ├── support_executive_summary.md
│   ├── support_finance_tracker.md
│   ├── support_infrastructure_maintainer.md
│   ├── support_legal_compliance.md
│   ├── support_responder.md
│   └── support_workflow_optimizer.md
│
└── testing/                   # 7 agents
    ├── testing_api_tester.md
    ├── testing_evidence_collector.md   ⭐ Screenshot-based QA
    ├── testing_performance_benchmarker.md
    ├── testing_reality_checker.md      ⭐ Quality gate enforcement
    ├── testing_results_analyzer.md
    ├── testing_tool_evaluator.md
    └── testing_workflow_optimizer.md
```

---

## Agent File Structure

Each agent follows a consistent structure with YAML frontmatter:

```markdown
---
name: Agent Name
description: Brief description of the agent's specialization
color: [color for UI representation]
---

# [Agent Name] Agent Personality

## 🧠 Your Identity & Memory
- **Role**: Specific specialization
- **Personality**: 3-4 behavioral/emotional traits
- **Memory**: What the agent tracks and remembers
- **Experience**: Failure patterns that inform behavior

## 🎯 Your Core Mission
### Primary Mission: [Main Focus]
- Key responsibilities
- **Default requirement**: Non-negotiable standard

### Secondary/Tertiary Missions
- Supporting objectives

## 🚨 Critical Rules You Must Follow
- Behavioral guardrails
- Non-negotiable constraints

## 📋 Your Deliverables
- Concrete templates, code examples, frameworks

## 🔄 Your Workflow Process
- Step-by-step workflow

## 💭 Your Communication Style
- How the agent should communicate

## 🔄 Learning & Memory
- Pattern recognition areas
- Expertise building

## 🎯 Your Success Metrics
- Quantitative and qualitative success criteria
```

---

## Pipeline Orchestration

The **Agents Orchestrator** (`specialized/agents_orchestrator.md`) manages complete development workflows:

### Standard Pipeline Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENTS ORCHESTRATOR                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: Project Analysis                                       │
│  Agent: project-manager-senior                                   │
│  Output: Task list from specification                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 2: Technical Architecture                                 │
│  Agent: design-ux-architect                                      │
│  Output: CSS foundation, layout systems, component patterns      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 3: Development-QA Loop (Per Task)                         │
│                                                                  │
│   ┌──────────────┐     ┌──────────────┐                         │
│   │  Developer   │────▶│  EvidenceQA  │                         │
│   │   Agent      │     │    Agent     │                         │
│   └──────────────┘     └──────────────┘                         │
│          ▲                    │                                  │
│          │    FAIL            │ PASS                             │
│          └────────────────────┼─────────▶ Next Task              │
│          (max 3 retries)      │                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 4: Final Integration                                      │
│  Agent: testing-reality-checker                                  │
│  Output: Production readiness certification                      │
│  Default: "NEEDS WORK" unless proven otherwise                   │
└─────────────────────────────────────────────────────────────────┘
```

### Decision Logic

```
FOR each task in task_list:
    1. Spawn appropriate Developer agent
    2. Developer implements task
    3. Spawn EvidenceQA agent
    4. EvidenceQA validates with screenshots

    IF QA_RESULT == PASS:
        Mark task complete
        Continue to next task

    IF QA_RESULT == FAIL:
        IF retry_count < 3:
            Loop back to Developer with QA feedback
            retry_count++
        ELSE:
            Mark task as blocked
            Escalate with detailed report

AFTER all tasks complete:
    Spawn testing-reality-checker for final validation
```

---

## Key Agents Deep Dive

### Agents Orchestrator
**File:** `specialized/agents_orchestrator.md`

The pipeline manager that coordinates all other agents. Key capabilities:
- Autonomous workflow execution
- Quality gate enforcement
- Retry logic with escalation
- Cross-agent context handoff
- Progress tracking and reporting

**Launch Command:**
```
Please spawn an agents-orchestrator to execute complete development pipeline
for project-specs/[project]-setup.md. Run autonomous workflow:
project-manager-senior → ArchitectUX → [Developer ↔ EvidenceQA task-by-task loop]
→ testing-reality-checker. Each task must pass QA before advancing.
```

### Whimsy Injector
**File:** `design/design_whimsy_injector.md`

Unique agent for injecting personality and delight into brand experiences:
- **Personality Spectrum**: Adapts voice across professional/casual/error/success contexts
- **Whimsy Taxonomy**: Subtle, Interactive, Discovery, Contextual categories
- **Micro-Interaction Library**: Ready-to-use CSS animations
- **Playful Microcopy**: Error messages, loading states, success messages
- **Gamification Systems**: Achievement unlocks, Easter eggs

### Reality Checker
**File:** `testing/testing_reality_checker.md`

The final quality gate that prevents "fantasy approvals":
- **Default stance**: "NEEDS WORK" unless proven otherwise
- **Evidence required**: Screenshots, not assertions
- **Automatic FAIL triggers**: Perfect scores without proof, claims that don't match reality
- **Realistic expectations**: First implementations typically need 2-3 revision cycles

### Senior Project Manager
**File:** `project-management/project_manager_senior.md`

Converts specifications into actionable development tasks:
- Quotes EXACT requirements (no luxury feature additions)
- Creates 30-60 minute implementable tasks
- Includes acceptance criteria
- Prevents scope creep

---

## Naming Convention

Agency agents use **hyphenated lowercase** naming:

```
{domain}-{role-descriptor}.md

Examples:
- design_whimsy_injector.md
- engineering_senior_developer.md
- testing_reality_checker.md
- project_manager_senior.md
```

This differs from standard prompts which use underscores (`category_function.md`).

---

## Agentic Techniques

These agents introduce 12 new prompt engineering techniques (AG-01 through AG-12):

| Code | Technique | Description |
|------|-----------|-------------|
| AG-01 | Personality-First Role Definition | Identity with traits, memory, experience |
| AG-02 | Skeptical Default Stance | Default to failure, require proof |
| AG-03 | Layered Mission Hierarchy | Primary/Secondary/Tertiary with defaults |
| AG-04 | Critical Rules as Guardrails | Behavioral directives that override |
| AG-05 | Concrete Deliverable Templates | Actual code, not placeholders |
| AG-06 | Memory & Learning Architecture | Pattern recognition over time |
| AG-07 | Pipeline Orchestration Patterns | Multi-agent coordination |
| AG-08 | Evidence-Based Decision Gates | Visual proof required |
| AG-09 | Anti-Pattern Embedding | Failure modes in identity |
| AG-10 | Emotional Context Spectrum | Personality across contexts |
| AG-11 | Taxonomy-Based Classification | Structured categorization |
| AG-12 | Quantitative Success Metrics | Measurable thresholds |

See `prompt-techniques/MASTER_TECHNIQUE_INDEX.md` for full documentation.

---

## When to Use Agency Agents vs. Standard Prompts

### Use Agency Agents When:
- Building multi-agent pipelines with handoffs
- Need persistent identity across interactions
- Require quality gates with evidence-based validation
- Want accumulated learning and pattern recognition
- Building autonomous workflows

### Use Standard Prompts When:
- Single task execution
- One-shot analysis or generation
- No need for agent coordination
- Simple input → output transformation

---

## Getting Started

### 1. Single Agent Usage

Spawn an individual agent for its specialty:

```
Please act as the Whimsy Injector agent. Read design/design_whimsy_injector.md
and help me add playful micro-interactions to my landing page.
```

### 2. Pipeline Execution

Use the orchestrator for complete workflows:

```
Please spawn an agents-orchestrator to manage development of my new feature.
Start with project-manager-senior for task breakdown, then coordinate
developer and QA agents for implementation.
```

### 3. Quality Gate Integration

Use testing agents for validation:

```
Please act as the Reality Checker. Review this implementation and provide
evidence-based assessment. Default to "NEEDS WORK" unless you see
overwhelming evidence of production readiness.
```

---

## Contributing

When adding new agents:

1. Follow the standard file structure (Identity, Mission, Rules, Deliverables, Workflow, Success Metrics)
2. Use hyphenated naming: `{domain}-{role}.md`
3. Include YAML frontmatter with name, description, color
4. Add concrete deliverables, not placeholders
5. Define clear success metrics with realistic expectations
6. Include failure patterns in the Experience section

---

## Related Resources

- `prompt-techniques/MASTER_TECHNIQUE_INDEX.md` - Complete technique catalog (AG-01 to AG-12)
- `meta/orchestration_patterns.md` - General orchestration patterns
- `skills/agentic_development.md` - Agentic development workflows

---

**Total Agents:** 51
**Domains:** 9
**Techniques Introduced:** 12 (AG-01 to AG-12)
**Last Updated:** 2025-12-08
