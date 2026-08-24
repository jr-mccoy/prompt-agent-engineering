# Technique Analysis: full-stack-feature

**Resource Type:** Command
**Path:** claude-code-resources/commands/orchestration/full-stack-feature.md
**Date Analyzed:** 2025-12-22

---

## Identified Techniques

### Technique 1: Multi-Phase Workflow Orchestration

- **Category:** AG (Agentic) + NEW
- **Pattern:** Sequential phases where each phase's output becomes the next phase's input context. Four distinct phases (Architecture → Implementation → Integration → Deployment) with 12 total steps.
- **Example from resource:**
```markdown
## Phase 1: Architecture & Design Foundation
### 1. Database Architecture Design
- Use Task tool with subagent_type="database-design::database-architect"
- Expected output: Entity relationship diagrams, table schemas...
- Context: Initial requirements and business domain model

### 2. Backend Service Architecture
- Context: Database schema from step 1, non-functional requirements
```
- **Maps to existing:** Partially maps to AG-07 (Pipeline Orchestration Patterns), but more sophisticated
- **Effectiveness:** Creates clear dependencies and context handoffs, ensuring each phase builds on validated previous work. Prevents rework by front-loading architecture decisions.

### Technique 2: Extended Thinking Blocks

- **Category:** NEW (Meta-cognitive documentation)
- **Pattern:** `[Extended thinking: ...]` blocks that explain the reasoning behind the workflow design, not visible to end users but guides the system
- **Example from resource:**
```markdown
[Extended thinking: This workflow coordinates multiple specialized agents to deliver a complete full-stack feature from architecture through deployment. It follows API-first development principles...]
```
- **Maps to existing:** NEW - Similar to RT-01 (Chain of Thought) but for workflow design rationale, not task execution
- **Effectiveness:** Provides context about WHY the workflow is structured this way, helps maintain design coherence when modifying the command

### Technique 3: Explicit Agent Specialization Assignment

- **Category:** AG (Agentic)
- **Pattern:** Each step explicitly names the specialized agent to use via subagent_type parameter, with domain::specialization format
- **Example from resource:**
```markdown
Use Task tool with subagent_type="database-design::database-architect"
Use Task tool with subagent_type="frontend-mobile-development::frontend-developer"
Use Task tool with subagent_type="python-development::python-pro" (or "golang-pro"/"nodejs-expert" based on stack)
```
- **Maps to existing:** AG-01 (Personality-First Role Definition), but more explicit about agent selection
- **Effectiveness:** Ensures the right expert handles each phase. Dynamic agent selection based on tech stack shows adaptability.

### Technique 4: Context Accumulation Pattern

- **Category:** NEW (Progressive context building)
- **Pattern:** Each step's "Context:" field lists specific outputs from previous steps, creating a chain of accumulating knowledge
- **Example from resource:**
```markdown
Step 1 Context: Initial requirements and business domain model
Step 2 Context: Database schema from step 1, non-functional requirements
Step 3 Context: API specifications from step 2, UI/UX requirements
```
- **Maps to existing:** Extends CM-04 (Summary-Expand Loop) with explicit dependency tracking
- **Effectiveness:** Prevents context loss in long workflows. Each agent knows exactly what information to consume from previous agents.

### Technique 5: API-First Design Enforcement

- **Category:** DS (Domain-Specific) + NEW
- **Pattern:** Forces API contract definition before implementation, with explicit mention in architecture phase
- **Example from resource:**
```markdown
Design backend service architecture... define API contracts (OpenAPI/GraphQL)
Frontend architecture based on the API contracts from previous step
Contract tests to validate API contracts between backend and frontend
```
- **Maps to existing:** NEW - Architectural pattern enforced through workflow ordering
- **Effectiveness:** Prevents frontend-backend integration issues by establishing contract first. Enables parallel development with clear interfaces.

### Technique 6: Parallel Execution with Convergence Points

- **Category:** AG (Agentic) + NEW
- **Pattern:** Phase 2 allows parallel implementation (backend, frontend, database) that must converge for Phase 3 testing
- **Example from resource:**
```markdown
## Phase 2: Parallel Implementation
### 4. Backend Service Implementation
### 5. Frontend Implementation
### 6. Database Implementation & Optimization
## Coordination Notes
- Parallel tasks in Phase 2 can run simultaneously but must converge for Phase 3
```
- **Maps to existing:** Extends AG-07 (Pipeline Orchestration) with parallelization
- **Effectiveness:** Maximizes development velocity while maintaining integration quality. Explicit convergence points ensure coordination.

### Technique 7: Comprehensive Success Criteria Specification

- **Category:** OT (Output Techniques) + DS (Domain-Specific)
- **Pattern:** Dedicated "Success Criteria" section with measurable, actionable checkpoints
- **Example from resource:**
```markdown
## Success Criteria
- All API contracts validated through contract tests
- Security audit passed with no critical vulnerabilities
- Performance metrics meeting defined SLOs
- Zero-downtime deployment capability verified
```
- **Maps to existing:** Maps to DS-02 (Metric Specification) + OC-04 (Conditional Output Logic)
- **Effectiveness:** Provides clear definition of done. Prevents premature completion and ensures quality gates.

### Technique 8: Configuration-Driven Workflow Customization

- **Category:** IT (Interaction Techniques) + NEW
- **Pattern:** Explicit configuration options that modify workflow behavior without changing the core orchestration
- **Example from resource:**
```markdown
## Configuration Options
- `stack`: Specify technology stack (e.g., "React/FastAPI/PostgreSQL")
- `deployment_target`: Cloud platform (AWS/GCP/Azure)
- `testing_depth`: Comprehensive or essential
- `compliance`: Specific compliance requirements (GDPR, HIPAA, SOC2)
```
- **Maps to existing:** NEW - Makes orchestration flexible without duplication
- **Effectiveness:** Single workflow handles multiple tech stacks and requirements. Reduces maintenance burden.

### Technique 9: Expected Output Specification

- **Category:** OT (Output Techniques)
- **Pattern:** Each step explicitly lists "Expected output:" with concrete deliverables
- **Example from resource:**
```markdown
Expected output: Entity relationship diagrams, table schemas, indexing strategy, migration scripts, data access patterns
Expected output: Service architecture diagram, OpenAPI specifications, authentication flows, caching architecture
```
- **Maps to existing:** ST-03 (Explicit Output Specification)
- **Effectiveness:** Agents know exactly what to deliver. Next agents know what to expect. Prevents incomplete handoffs.

### Technique 10: Quality Gate Integration Points

- **Category:** AG (Agentic) + DS (Domain-Specific)
- **Pattern:** Dedicated steps for security audit, contract testing, and performance optimization as quality gates
- **Example from resource:**
```markdown
### 7. API Contract Testing
### 8. End-to-End Testing
### 9. Security Audit & Hardening
### 12. Performance Optimization
```
- **Maps to existing:** AG-08 (Evidence-Based Decision Gates)
- **Effectiveness:** Forces quality validation at multiple points. Catches issues early before they compound.

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Extended Thinking Documentation

- **Description:** System-level reasoning blocks that explain workflow design rationale, not part of user-facing content
- **Implementation:** `[Extended thinking: explanation of why this workflow is structured this way]` at the beginning of complex workflows
- **Use case:** Complex orchestration commands where understanding the design philosophy helps maintain and modify the workflow
- **Example:**
```markdown
[Extended thinking: This workflow coordinates multiple specialized agents to deliver a complete full-stack feature from architecture through deployment. It follows API-first development principles, ensuring contract-driven development...]
```
- **Proposed category:** MP (Meta-Prompting Techniques)
- **Proposed code:** MP-05

### Pattern 2: Progressive Context Accumulation

- **Description:** Explicit chaining of context where each step's output feeds the next step's context, with transparent dependency tracking
- **Implementation:** Context field in each step that references specific outputs from numbered previous steps
- **Use case:** Multi-step workflows where context must build progressively without loss
- **Example:**
```markdown
Step 3 Context: API specifications from step 2, UI/UX requirements
Step 7 Context: API implementations from Phase 2
```
- **Proposed category:** CM (Context Management)
- **Proposed code:** CM-05

### Pattern 3: Architecture-First Enforcement

- **Description:** Workflow design that enforces architectural decisions before implementation by sequencing phases and requiring specific outputs
- **Implementation:** Separate Architecture phase that must complete before Implementation phase, with API contracts as mandatory output
- **Use case:** Large features where ad-hoc development leads to integration problems
- **Example:** Full workflow forces DB schema → API contract → Component architecture before any code
- **Proposed category:** DS (Domain-Specific - Software Development)
- **Proposed code:** DS-13

### Pattern 4: Parallel-Converge Orchestration

- **Description:** Explicit support for parallel agent execution with defined convergence points for synchronization
- **Implementation:** Phase allows parallel tasks with coordination notes explaining convergence requirements
- **Use case:** Maximizing development velocity while maintaining integration quality
- **Example:**
```markdown
## Phase 2: Parallel Implementation (steps 4-6 parallel)
## Phase 3: Integration & Testing (convergence required)
## Coordination Notes: Parallel tasks must converge for Phase 3
```
- **Proposed category:** AG (Agentic)
- **Proposed code:** AG-13

### Pattern 5: Configuration-Driven Orchestration

- **Description:** Single workflow with configuration parameters that modify behavior without changing core structure
- **Implementation:** Configuration Options section that adapts workflow to different tech stacks, platforms, and requirements
- **Use case:** Workflows that must support multiple technology stacks or deployment scenarios
- **Example:** Same workflow handles React/FastAPI, Next.js/Django, or other stacks via configuration
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-14

---

## Multi-Technique Combinations

**Technique Stack:** Extended Thinking (NEW) + Multi-Phase Orchestration (AG-07 extended) + Context Accumulation (NEW) + API-First Enforcement (NEW) + Parallel-Converge (NEW) + Success Criteria (DS-02/OC-04) + Configuration-Driven (NEW)

**Combination Purpose:** Create a production-ready, full-stack feature development workflow that:
1. Prevents common integration failures through architecture-first approach
2. Maximizes velocity through parallelization
3. Maintains quality through explicit quality gates
4. Supports multiple tech stacks through configuration
5. Ensures complete deliverables through success criteria

**Flow:**
1. Extended thinking explains overall philosophy
2. Configuration customizes for specific stack
3. Phase 1 forces architecture-first (DB → API → UI contracts)
4. Phase 2 enables parallel implementation with context from Phase 1
5. Phase 3 enforces convergence with quality gates (testing, security)
6. Phase 4 handles deployment with observability
7. Success criteria validate complete workflow

**Synergies:**
- Context accumulation + parallel execution = Efficient parallelization without context loss
- API-first + contract testing = Integration confidence without manual coordination
- Extended thinking + configuration = Maintainable flexibility
- Quality gates + success criteria = Multi-layer validation

---

## Notes for Integration

**Add to MASTER_TECHNIQUE_INDEX:**
- MP-05: Extended Thinking Documentation
- CM-05: Progressive Context Accumulation
- DS-13: Architecture-First Enforcement
- AG-13: Parallel-Converge Orchestration
- IT-14: Configuration-Driven Orchestration

**Update USE_CASE_LOOKUP:**
- Add "Feature Development" section with full-stack orchestration patterns
- Add "Multi-Agent Workflows" section referencing these novel patterns
- Update "Quality Assurance" section with quality gate integration patterns

**Cross-reference with prompts:**
- Related to: `engineering/engineering_delivery_sprint_planner.md` (project planning)
- Related to: `architecture/architecture_*.md` (architecture prompts)
- Related to: `testing/testing_*.md` (testing prompts)
- Maps to orchestration of multiple single-purpose prompts

**Documentation improvements:**
- AI_AGENT_QUICK_START.md should reference orchestration commands as advanced pattern
- Create guide on "When to use orchestration vs single prompts"
- Document the Extended Thinking pattern for command authors

**Best practices:**
- Use Extended Thinking for complex workflows to document design rationale
- Always specify expected outputs and context inputs for clean handoffs
- Build in quality gates at phase boundaries
- Use configuration instead of duplicating workflows for variations
- Define success criteria upfront, not after implementation

---

## Analysis Metadata

**Analyzer:** Claude (Task 2.2 implementation)
**Analysis Duration:** 25 minutes
**Confidence Level:** High
**Review Status:** Draft
**Priority for Integration:** High - This command demonstrates multiple novel patterns for multi-agent orchestration

---

## Quick Reference Checklist

- [x] Read complete resource file
- [x] Identify all techniques (compare against MASTER_TECHNIQUE_INDEX.md)
- [x] Flag novel patterns not in existing index (5 novel patterns identified)
- [x] Note technique combinations and stacks
- [x] Document specific examples with quotes
- [x] Assess effectiveness for use case
- [x] Identify related resources (agents/skills/commands/prompts)
- [x] Add integration recommendations
- [ ] Update TECHNIQUE_USAGE_MATRIX.csv row (will do in summary phase)
- [x] Mark analysis complete
