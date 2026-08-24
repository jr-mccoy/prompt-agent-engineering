# Example 07: Full Workflow Integration

**Goal:** Demonstrate complete integration of agents, skills, and commands working together for an end-to-end feature development workflow.

**Time Estimate:** 60 minutes

**Concepts Covered:**
- Command orchestrating multiple agents
- Agents referencing skills for detailed procedures
- Full lifecycle from requirements to deployment
- Integration patterns across all resource types

---

## Scenario

**Task:** Build a complete "Feature Development" workflow that:
1. Uses a command for orchestration
2. Invokes specialized agents for each phase
3. Agents leverage skills for detailed procedures
4. Produces a fully tested, documented, deployed feature

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    /feature-development COMMAND                  │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ Phase 1: Requirements                                      │ │
│  │  └── business-analyst agent                                │ │
│  │       └── References: requirements-gathering skill         │ │
│  └────────────────────────────────────────────────────────────┘ │
│                              │                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ Phase 2: Design                                            │ │
│  │  └── backend-architect agent                               │ │
│  │       └── References: api-design-patterns skill            │ │
│  └────────────────────────────────────────────────────────────┘ │
│                              │                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ Phase 3: Implementation (PARALLEL)                         │ │
│  │  ├── python-pro agent                                      │ │
│  │  │    └── References: async-python-patterns skill          │ │
│  │  ├── frontend-developer agent                              │ │
│  │  │    └── References: react-patterns skill                 │ │
│  │  └── database-architect agent                              │ │
│  │       └── References: postgresql-optimization skill        │ │
│  └────────────────────────────────────────────────────────────┘ │
│                              │                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ Phase 4: Testing                                           │ │
│  │  └── test-automator agent                                  │ │
│  │       └── References: pytest-patterns skill                │ │
│  └────────────────────────────────────────────────────────────┘ │
│                              │                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ Phase 5: Deployment                                        │ │
│  │  └── deployment-engineer agent                             │ │
│  │       └── References: kubernetes-deployment skill          │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Component Inventory

### Command (Orchestration Layer)

| Component | Purpose |
|-----------|---------|
| `/feature-development` | Main orchestration command |

### Agents (Execution Layer)

| Agent | Phase | Expertise |
|-------|-------|-----------|
| `business-analyst` | 1 | Requirements elicitation |
| `backend-architect` | 2 | API and system design |
| `python-pro` | 3 | Python implementation |
| `frontend-developer` | 3 | React frontend |
| `database-architect` | 3 | Database design |
| `test-automator` | 4 | Test generation |
| `deployment-engineer` | 5 | K8s deployment |

### Skills (Knowledge Layer)

| Skill | Used By | Provides |
|-------|---------|----------|
| `requirements-gathering` | business-analyst | User story templates, acceptance criteria |
| `api-design-patterns` | backend-architect | REST/GraphQL patterns, OpenAPI |
| `async-python-patterns` | python-pro | AsyncIO patterns, FastAPI best practices |
| `react-patterns` | frontend-developer | Component patterns, state management |
| `postgresql-optimization` | database-architect | Query optimization, indexing |
| `pytest-patterns` | test-automator | Test fixtures, mocking patterns |
| `kubernetes-deployment` | deployment-engineer | K8s manifests, Helm charts |

---

## Full Command Implementation

```markdown
# Feature Development

Orchestrate complete feature development from requirements through deployment using specialized agents with skill augmentation.

[Extended thinking: This workflow implements a comprehensive feature development lifecycle. Each phase is handled by a specialized agent with access to domain-specific skills for detailed procedures and best practices. The workflow ensures quality through validation gates while maximizing efficiency with parallel execution where possible. Skills provide the "how" while agents provide the "reasoning" for a complete, professional implementation.]

## Configuration

### Supported Flags
- `--skip-requirements`: Start from existing requirements
- `--skip-deploy`: Stop after testing phase
- `--tdd`: Use Test-Driven Development approach
- `--dry-run`: Plan only, no implementation

### Parameters
- `stack`: Technology stack
  - Values: `"React/FastAPI/PostgreSQL"`, `"Next.js/Django/MongoDB"`
  - Default: Auto-detect from project
- `deployment_target`: Deployment platform
  - Values: `"kubernetes"`, `"docker-compose"`, `"serverless"`
  - Default: `"kubernetes"`

---

## Phase 1: Requirements Analysis

### 1. Requirements Gathering
- Use Task tool with subagent_type="business-analytics::business-analyst"
- Prompt: "Analyze and document requirements for feature: $ARGUMENTS.

  Reference requirements-gathering skill for:
  - User story template format
  - Acceptance criteria patterns
  - Edge case identification checklist

  Deliverables:
  1) User stories with acceptance criteria
  2) Technical requirements derived from user needs
  3) Non-functional requirements (performance, security)
  4) Edge cases and error scenarios
  5) Dependencies and prerequisites

  Generate complete requirements specification."

- Expected output:
  - User stories with acceptance criteria
  - Technical requirements document
  - Edge case matrix
  - Dependency map
- Skill reference: requirements-gathering (user-story-template.md, acceptance-criteria.md)

---

### PHASE GATE: Requirements → Design

- [ ] All user stories have acceptance criteria
- [ ] Technical requirements documented
- [ ] Edge cases identified
- [ ] Stakeholder sign-off (if applicable)

---

## Phase 2: Design

### 2. System Design
- Use Task tool with subagent_type="backend-development::backend-architect"
- Prompt: "Design system architecture for feature: $ARGUMENTS.

  Using requirements from Phase 1, create:
  1) API design (endpoints, request/response schemas)
  2) Database schema design
  3) Component architecture
  4) Integration points
  5) Security considerations

  Reference api-design-patterns skill for:
  - REST API best practices
  - OpenAPI specification format
  - Authentication patterns

  Generate architecture design document with diagrams."

- Expected output:
  - API specification (OpenAPI format)
  - Database schema design
  - Architecture diagram (Mermaid)
  - Component specifications
- Context from previous: Requirements specification
- Skill reference: api-design-patterns (rest-best-practices.md, openapi-template.yaml)

---

### PHASE GATE: Design → Implementation

- [ ] API specification complete
- [ ] Database schema designed
- [ ] Architecture approved
- [ ] Security reviewed

---

## Phase 3: Implementation (PARALLEL)

### ⚡ PARALLEL EXECUTION BLOCK

### 3a. Backend Implementation
- Use Task tool with subagent_type="python-development::python-pro"
- Prompt: "Implement backend for feature: $ARGUMENTS.

  Using API specification from Phase 2:
  1) Implement FastAPI endpoints
  2) Create Pydantic models
  3) Implement business logic
  4) Add input validation
  5) Implement error handling

  Reference async-python-patterns skill for:
  - AsyncIO patterns
  - FastAPI best practices
  - Dependency injection patterns

  Generate production-ready Python code."

- Expected output:
  - FastAPI application code
  - Pydantic models
  - Business logic modules
  - Unit tests (if --tdd)
- Context from previous: API specification, database schema
- Skill reference: async-python-patterns (asyncio-patterns.md, fastapi-best-practices.md)

---

### 3b. Frontend Implementation
- Use Task tool with subagent_type="frontend-mobile-development::frontend-developer"
- Prompt: "Implement frontend for feature: $ARGUMENTS.

  Using API specification from Phase 2:
  1) Create React components
  2) Implement state management
  3) Add API integration
  4) Implement form handling
  5) Add error handling and loading states

  Reference react-patterns skill for:
  - Component composition patterns
  - State management approaches
  - Custom hook patterns

  Generate production-ready React code."

- Expected output:
  - React components
  - State management setup
  - API integration layer
  - Component tests
- Context from previous: API specification, UI requirements
- Skill reference: react-patterns (component-patterns.md, state-management.md)

---

### 3c. Database Implementation
- Use Task tool with subagent_type="database-design::database-architect"
- Prompt: "Implement database layer for feature: $ARGUMENTS.

  Using database schema from Phase 2:
  1) Create migration scripts
  2) Implement optimized queries
  3) Add necessary indexes
  4) Create database access layer
  5) Implement connection pooling

  Reference postgresql-optimization skill for:
  - Index selection strategies
  - Query optimization patterns
  - Migration best practices

  Generate database implementation."

- Expected output:
  - Migration scripts
  - Query implementations
  - Index definitions
  - Database access layer
- Context from previous: Database schema design
- Skill reference: postgresql-optimization (indexing-guide.md, query-patterns.md)

---

### ⏳ CONVERGENCE CHECKPOINT

All implementation tasks must complete:

| Component | Status | Skill Used |
|-----------|--------|------------|
| Backend | ⬜ | async-python-patterns |
| Frontend | ⬜ | react-patterns |
| Database | ⬜ | postgresql-optimization |

---

## Phase 4: Testing

### 4. Test Generation and Execution
- Use Task tool with subagent_type="unit-testing::test-automator"
- Prompt: "Generate and execute comprehensive tests for: $ARGUMENTS.

  Using implementations from Phase 3:
  1) Generate unit tests for all components
  2) Create integration tests for API endpoints
  3) Implement E2E tests for critical flows
  4) Run all tests and collect coverage
  5) Identify and address gaps

  Reference pytest-patterns skill for:
  - Fixture patterns
  - Mocking strategies
  - Test organization

  Target: 80% line coverage, 75% branch coverage."

- Expected output:
  - Unit test suite
  - Integration tests
  - E2E tests
  - Coverage report
  - Test execution results
- Context from previous: All Phase 3 implementations
- Skill reference: pytest-patterns (fixtures.md, mocking.md, test-organization.md)
- **GATE**: Block if coverage below threshold

---

### PHASE GATE: Testing → Deployment

- [ ] All unit tests passing
- [ ] Integration tests passing
- [ ] E2E tests passing
- [ ] Coverage meets thresholds
- [ ] No critical bugs

---

## Phase 5: Deployment

### 5. Kubernetes Deployment
- Use Task tool with subagent_type="deployment-strategies::deployment-engineer"
- Prompt: "Deploy feature to Kubernetes for: $ARGUMENTS.

  Using tested code from Phase 4:
  1) Create/update Kubernetes manifests
  2) Configure Helm chart if applicable
  3) Set up horizontal pod autoscaling
  4) Configure health checks
  5) Implement blue-green deployment
  6) Set up monitoring and alerts

  Reference kubernetes-deployment skill for:
  - Manifest best practices
  - Helm chart patterns
  - Health check configuration

  Execute deployment with rollback capability."

- Expected output:
  - Kubernetes manifests
  - Helm chart (if applicable)
  - Deployment verification
  - Monitoring dashboard
  - Rollback plan
- Context from previous: All tested implementations
- Skill reference: kubernetes-deployment (manifest-patterns.md, helm-best-practices.md)

---

## Integration Visualization

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ COMMAND: /feature-development                                               │
│                                                                             │
│  Phase 1          Phase 2          Phase 3              Phase 4   Phase 5  │
│  ┌─────┐          ┌─────┐          ┌─────┐              ┌─────┐   ┌─────┐  │
│  │REQ  │─────────▶│DSGN │─────────▶│IMPL │─────────────▶│TEST │──▶│DPLY │  │
│  └─────┘          └─────┘          └─────┘              └─────┘   └─────┘  │
│     │                │                │                    │         │     │
│     ▼                ▼                ▼                    ▼         ▼     │
│  ┌─────────┐     ┌─────────┐     ┌─────────┐          ┌─────────┐ ┌─────┐ │
│  │business │     │backend- │     │python   │          │test-    │ │dploy│ │
│  │-analyst │     │architect│     │-pro     │(parallel)│automator│ │-eng │ │
│  └────┬────┘     └────┬────┘     │frontend │          └────┬────┘ └──┬──┘ │
│       │               │          │database │               │         │     │
│       ▼               ▼          └─────────┘               ▼         ▼     │
│  ┌─────────┐     ┌─────────┐     ┌─────────┐          ┌─────────┐ ┌─────┐ │
│  │require- │     │api-     │     │async-py │          │pytest-  │ │k8s- │ │
│  │ments    │     │design   │     │react    │          │patterns │ │dply │ │
│  │skill    │     │skill    │     │pg-opt   │          │skill    │ │skill│ │
│  └─────────┘     └─────────┘     └─────────┘          └─────────┘ └─────┘ │
│                                                                             │
│  [AGENTS]         [AGENTS]        [AGENTS]             [AGENTS]  [AGENTS] │
│  [SKILLS]         [SKILLS]        [SKILLS]             [SKILLS]  [SKILLS] │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Success Criteria

### Phase Completion
- ✅ Requirements documented with acceptance criteria
- ✅ Architecture designed and approved
- ✅ All components implemented
- ✅ All tests passing with coverage thresholds
- ✅ Successfully deployed to target environment

### Quality Gates
- ✅ All phase gates passed
- ✅ Skills referenced for best practices
- ✅ Agents produced expected outputs
- ✅ Context correctly passed between phases

### Integration Verification
- ✅ Backend, Frontend, Database work together
- ✅ E2E tests verify full flow
- ✅ Deployment verified with health checks

---

## Key Integration Patterns

### 1. Command → Agent → Skill Chain

```markdown
# In command:
- Use Task tool with subagent_type="python-development::python-pro"
- Prompt: "...Reference async-python-patterns skill for..."

# Agent prompt includes skill reference:
"Reference async-python-patterns skill for:
- AsyncIO patterns
- FastAPI best practices"

# Agent implementation uses skill knowledge
```

### 2. Parallel Execution with Skill References

Each parallel agent references its own skill:
```
Backend Agent → async-python-patterns skill
Frontend Agent → react-patterns skill
Database Agent → postgresql-optimization skill
```

### 3. Context Accumulation Through Phases

```
Phase 1 Output (Requirements)
    ↓
Phase 2 Input + Output (Design)
    ↓
Phase 3 Input + Output (Implementation)
    ↓
Phase 4 Input + Output (Testing)
    ↓
Phase 5 Input (Deployment)
```

---

## When to Use Full Integration

### Good Candidates
- ✅ End-to-end feature development
- ✅ Multi-domain projects (frontend + backend + database)
- ✅ Projects requiring best practices from multiple areas
- ✅ Processes with distinct phases and handoffs

### Overkill For
- ❌ Single-file changes
- ❌ Simple bug fixes
- ❌ One-domain tasks

---

## Files Referenced

- **Command Templates:** [../command-templates/](../command-templates/)
- **Agent Templates:** [../agent-templates/](../agent-templates/)
- **Agent Directory:** ../../agents/
- **Skills Directory:** ../../skills/
- **Pattern Indexes:** [../../AGENT_PATTERN_INDEX.md](../../agent-patterns/AGENT_PATTERN_INDEX.md), [../../COMMAND_PATTERN_INDEX.md](../../command-patterns/COMMAND_PATTERN_INDEX.md)
