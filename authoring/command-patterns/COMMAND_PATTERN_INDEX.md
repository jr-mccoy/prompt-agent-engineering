# Command Pattern Index

**Total Patterns:** 29 patterns across 6 categories
**Last Updated:** 2025-12-31
**Status:** Complete

---

## Table of Contents

1. [Overview](#overview)
2. [Pattern Categories](#pattern-categories)
3. [Orchestration Patterns (OP-01 to OP-05)](#orchestration-patterns-op)
4. [Workflow Patterns (WP-01 to WP-06)](#workflow-patterns-wp)
5. [Agent Invocation Patterns (AIP-01 to AIP-05)](#agent-invocation-patterns-aip)
6. [Validation Patterns (VP-01 to VP-05)](#validation-patterns-vp)
7. [Error Handling Patterns (EHP-01 to EHP-04)](#error-handling-patterns-ehp)
8. [Configuration Patterns (CP-01 to CP-04)](#configuration-patterns-cp)
9. [Pattern Combinations](#pattern-combinations)
10. [Quick Reference](#quick-reference)

---

## Overview

Command patterns are reusable design structures extracted from 70+ existing commands. Commands orchestrate multi-agent workflows to execute complex, multi-phase operations. Unlike agents (specialized identities) or skills (knowledge packages), commands coordinate entire development processes.

### What Commands Do

| Aspect | Description |
|--------|-------------|
| **Purpose** | Multi-step orchestration of specialized agents |
| **Scope** | End-to-end workflows (architecture → deployment) |
| **Coordination** | Sequential and parallel agent execution |
| **Duration** | Long-running processes with multiple phases |

### Pattern Architecture

```
Command Structure:
├── Extended Thinking (reasoning context)
├── Configuration (options and flags)
├── Phase 1: Foundation
│   ├── Agent Invocation (Task tool)
│   ├── Expected Output
│   └── Context Passing
├── Phase 2: Implementation
│   ├── Parallel Agent Execution
│   └── Validation Gate
├── Phase N: Completion
│   ├── Final Validation
│   └── Success Criteria
├── Error Handling
│   └── Rollback Procedures
└── Coordination Notes
```

---

## Pattern Categories

| Category | Code | Count | Purpose |
|----------|------|-------|---------|
| Orchestration | OP | 5 | Multi-phase workflow coordination |
| Workflow | WP | 6 | Process structure and flow control |
| Agent Invocation | AIP | 5 | Calling specialized agents |
| Validation | VP | 5 | Quality gates and verification |
| Error Handling | EHP | 4 | Recovery and rollback |
| Configuration | CP | 4 | Options and customization |

---

## Orchestration Patterns (OP)

Patterns for coordinating multi-phase workflows with multiple agents.

### OP-01: Multi-Phase Sequential

**Description:** Organize command execution into named phases with clear progression.

**When to Use:**
- Complex workflows requiring distinct stages
- Tasks with dependencies between stages
- Operations needing explicit handoff points

**Implementation:**
```markdown
## Phase 1: Assessment and Planning

### 1. Initial Analysis
- Use Task tool with subagent_type="analyst"
- Prompt: "Analyze the target system..."
- Expected output: Analysis report

### 2. Risk Evaluation
- Use Task tool with subagent_type="risk-assessor"
- Context from previous: Analysis report
- Expected output: Risk matrix

## Phase 2: Implementation

### 3. Core Implementation
- Use Task tool with subagent_type="developer"
- Context from previous: Risk matrix, analysis
- Expected output: Implementation code
```

**Real Examples:**
- `full-stack-feature.md` - 4 phases: Architecture, Implementation, Testing, Deployment
- `security-hardening.md` - 4 phases: Assessment, Remediation, Controls, Validation
- `tdd-cycle.md` - 6 phases: Specification, RED, GREEN, REFACTOR, Integration, Improvement

**Best Practices:**
- Use 3-6 phases for most workflows
- Name phases descriptively (not just "Phase 1")
- Include phase purpose in header
- Number steps sequentially across phases

---

### OP-02: Parallel Agent Execution

**Description:** Execute multiple agents simultaneously within a phase when tasks are independent.

**When to Use:**
- Independent subtasks within a phase
- Performance optimization needed
- Multiple domains requiring simultaneous work

**Implementation:**
```markdown
## Phase 2: Parallel Implementation

### 4. Backend Service Implementation
- Use Task tool with subagent_type="backend-architect"
- Prompt: "Implement backend services..."
- Expected output: Backend code, API endpoints

### 5. Frontend Implementation (PARALLEL)
- Use Task tool with subagent_type="frontend-developer"
- Prompt: "Implement frontend application..."
- Expected output: React components, state management

### 6. Database Implementation (PARALLEL)
- Use Task tool with subagent_type="database-architect"
- Prompt: "Implement database layer..."
- Expected output: Migration scripts, optimized queries

[Note: Steps 4-6 can run simultaneously but must converge for Phase 3]
```

**Real Examples:**
- `full-stack-feature.md` - Backend, Frontend, Database in parallel
- `multi-platform.md` - Web, Mobile, Desktop implementations parallel

**Best Practices:**
- Mark parallel tasks explicitly
- Ensure no dependencies between parallel tasks
- Define convergence point
- Consider resource constraints

---

### OP-03: Context Passing Chain

**Description:** Pass output from one agent as context to the next agent in sequence.

**When to Use:**
- Sequential dependencies between tasks
- Building on previous analysis/work
- Maintaining continuity across phases

**Implementation:**
```markdown
### 1. Requirements Analysis
- Use Task tool with subagent_type="analyst"
- Prompt: "Analyze requirements for: $ARGUMENTS"
- Expected output: Requirements specification

### 2. Architecture Design
- Use Task tool with subagent_type="architect"
- Prompt: "Design architecture based on requirements..."
- **Context from previous:** Requirements specification
- Expected output: Architecture design

### 3. Implementation Planning
- Use Task tool with subagent_type="planner"
- Prompt: "Create implementation plan..."
- **Context from previous:** Requirements specification, Architecture design
- Expected output: Implementation roadmap
```

**Real Examples:**
- `git-workflow.md` - Review → Test → Commit → Push chain
- `incident-response.md` - Detection → Investigation → Resolution chain
- `legacy-modernize.md` - Assessment → Testing → Migration chain

**Best Practices:**
- Explicitly name context sources
- Accumulate context through phases
- Reference specific outputs, not entire phases
- Keep context focused and relevant

---

### OP-04: Domain-Specific Agent Selection

**Description:** Select specialized agents based on task domain and requirements.

**When to Use:**
- Tasks requiring domain expertise
- Technology-specific implementations
- When quality depends on specialization

**Implementation:**
```markdown
### Backend Implementation
- Use Task tool with subagent_type="python-development::python-pro"
  (or "golang-pro" / "nodejs-expert" based on stack)
- Prompt: "Implement backend services using [detected/specified stack]..."

### Security Audit
- Use Task tool with subagent_type="security-scanning::security-auditor"
- Prompt: "Perform security assessment..."

### Performance Optimization
- Use Task tool with subagent_type="application-performance::performance-engineer"
- Prompt: "Optimize performance..."
```

**Agent Selection Matrix:**

| Domain | Agent Type | Use Case |
|--------|-----------|----------|
| Backend | `backend-development::backend-architect` | Architecture design |
| Backend | `python-development::python-pro` | Python implementation |
| Frontend | `frontend-mobile-development::frontend-developer` | React/Vue/Angular |
| Security | `security-scanning::security-auditor` | Vulnerability scanning |
| Testing | `unit-testing::test-automator` | Test generation |
| DevOps | `deployment-strategies::deployment-engineer` | CI/CD, infrastructure |
| Database | `database-design::database-architect` | Schema design |
| Performance | `application-performance::performance-engineer` | Optimization |

**Best Practices:**
- Match agent to specific task domain
- Use composite agent paths for precision
- Consider technology stack in selection
- Document agent selection rationale

---

### OP-05: Milestone Convergence

**Description:** Define convergence points where parallel work must complete before proceeding.

**When to Use:**
- After parallel execution phases
- Before integration or validation
- When subsequent work depends on all parallel outputs

**Implementation:**
```markdown
## Phase 2: Parallel Implementation

### 4-6. [Parallel tasks as shown in OP-02]

---
### CONVERGENCE CHECKPOINT
All parallel tasks must complete before Phase 3:
- [ ] Backend services implemented
- [ ] Frontend components built
- [ ] Database migrations ready
---

## Phase 3: Integration & Testing

### 7. API Contract Testing
- Use Task tool with subagent_type="test-automator"
- **Context from previous:** All Phase 2 outputs
- Prompt: "Create contract tests validating integration..."
```

**Real Examples:**
- `full-stack-feature.md` - Convergence after Backend/Frontend/DB parallel work
- `legacy-modernize.md` - Convergence before progressive rollout

**Best Practices:**
- Explicitly mark convergence points
- List required completions as checklist
- Block progression until convergence
- Validate all outputs before proceeding

---

## Workflow Patterns (WP)

Patterns for structuring command flow and process control.

### WP-01: Extended Thinking Introduction

**Description:** Begin commands with extended thinking block providing reasoning context.

**When to Use:**
- Complex orchestration requiring explanation
- When AI needs context for decision-making
- Commands with non-obvious design choices

**Implementation:**
```markdown
[Extended thinking: This workflow coordinates multiple specialized
agents to deliver a complete full-stack feature from architecture
through deployment. It follows API-first development principles,
ensuring contract-driven development where the API specification
drives both backend implementation and frontend consumption. Each
phase builds upon previous outputs, creating a cohesive system with
proper separation of concerns, comprehensive testing, and
production-ready deployment.]
```

**Real Examples:**
- `full-stack-feature.md` - Explains API-first approach
- `security-hardening.md` - Explains defense-in-depth strategy
- `incident-response.md` - Explains ICS methodology

**Best Practices:**
- Keep to 3-5 sentences
- Explain methodology and approach
- Highlight key design decisions
- Note important coordination aspects

---

### WP-02: Configuration Block

**Description:** Define configurable options at the command start.

**When to Use:**
- Commands with variable behavior
- When different modes are needed
- For optional feature enablement

**Implementation:**
```markdown
## Configuration

### Coverage Thresholds
- Minimum line coverage: 80%
- Minimum branch coverage: 75%
- Critical path coverage: 100%

### Supported Flags
- `--skip-tests`: Skip automated test execution
- `--draft-pr`: Create PR as draft
- `--no-push`: Perform checks but don't push
- `--conventional`: Enforce Conventional Commits

### Configuration Options
- `stack`: Technology stack ("React/FastAPI/PostgreSQL")
- `deployment_target`: Cloud platform (AWS/GCP/Azure)
- `testing_depth`: "comprehensive" | "essential"
```

**Real Examples:**
- `tdd-cycle.md` - Coverage thresholds, refactoring triggers
- `git-workflow.md` - Supported flags for workflow modes
- `incident-response.md` - Severity levels, incident types

**Best Practices:**
- Group related options
- Provide sensible defaults
- Document valid values
- Explain impact of each option

---

### WP-03: Success Criteria Definition

**Description:** Define explicit success criteria for command completion.

**When to Use:**
- All commands (this is essential)
- Quality-focused workflows
- When validation is required

**Implementation:**
```markdown
## Success Criteria

- ✅ All API contracts validated through contract tests
- ✅ Frontend and backend integration tests passing
- ✅ E2E tests covering critical user journeys
- ✅ Security audit passed with no critical vulnerabilities
- ✅ Performance metrics meeting defined SLOs
- ✅ Observability stack capturing all key metrics
- ✅ Documentation complete for all components
- ✅ CI/CD pipeline with automated quality gates
- ✅ Zero-downtime deployment capability verified
```

**Real Examples:**
- `full-stack-feature.md` - 10 success criteria
- `security-hardening.md` - 10 security-focused criteria
- `tdd-cycle.md` - 7 TDD discipline criteria

**Best Practices:**
- Make criteria measurable
- Cover all critical aspects
- Use checkboxes for tracking
- Include both technical and process criteria

---

### WP-04: Coordination Notes Section

**Description:** Document agent coordination and communication requirements.

**When to Use:**
- Multi-agent workflows
- When handoffs need explanation
- For complex coordination requirements

**Implementation:**
```markdown
## Coordination Notes

- Each phase builds upon outputs from previous phases
- Parallel tasks in Phase 2 can run simultaneously but must converge for Phase 3
- Maintain traceability between requirements and implementations
- Use correlation IDs across all services for distributed tracing
- Document all architectural decisions in ADRs
- Ensure consistent error handling and API responses across services
- Security-auditor agent coordinates with domain-specific agents for fixes
- All code changes undergo security review before implementation
```

**Real Examples:**
- `full-stack-feature.md` - 6 coordination notes
- `security-hardening.md` - 6 security coordination notes
- `incident-response.md` - Incident command structure

**Best Practices:**
- Explain inter-agent communication
- Document feedback loops
- Specify context sharing requirements
- Note timing dependencies

---

### WP-05: Input Arguments Handling

**Description:** Define how command arguments are processed and used.

**When to Use:**
- All commands accepting input
- When arguments drive behavior
- For variable target specification

**Implementation:**
```markdown
## Requirements and Argument Handling

### Input Parameters
- `$ARGUMENTS`: Primary input describing the task/target
- `$PROJECT_ROOT`: Absolute path to project root
- `$CONTEXT_TYPE`: Granularity level (minimal, standard, comprehensive)

### Argument Processing
Feature to implement: $ARGUMENTS

Parse $ARGUMENTS to identify:
- Primary task description
- Affected components/services
- Special requirements or constraints
- Technology stack preferences
```

**Real Examples:**
- `context-save.md` - Explicit parameter definitions
- `smart-debug.md` - Argument parsing instructions
- `full-stack-feature.md` - Arguments as feature description

**Best Practices:**
- Document all input parameters
- Show where arguments are used
- Provide examples of valid inputs
- Handle missing arguments gracefully

---

### WP-06: Reference Documentation

**Description:** Include reference workflows, examples, or best practices.

**When to Use:**
- Complex workflows needing examples
- When patterns should be followed
- For educational value

**Implementation:**
```markdown
## Reference Workflows

### Workflow 1: Project Onboarding Context Capture
1. Analyze project structure
2. Extract architectural decisions
3. Generate semantic embeddings
4. Store in vector database
5. Create markdown summary

### Best Practices Reference

- **Commit Frequency**: Commit early and often, ensure atomicity
- **Branch Naming**: `(feature|bugfix|hotfix)/<ticket>-<description>`
- **PR Size**: Keep PRs under 400 lines for effective review
- **Review Response**: Address comments within 24 hours

### Anti-Patterns to Avoid

- Writing implementation before tests
- Skipping the refactor phase
- Writing multiple features without tests
- Ignoring failing tests
```

**Real Examples:**
- `context-save.md` - Reference workflows
- `git-workflow.md` - Best practices reference
- `tdd-cycle.md` - Anti-patterns section

**Best Practices:**
- Include 2-3 reference workflows
- Document common anti-patterns
- Provide concrete examples
- Link to external resources when helpful

---

## Agent Invocation Patterns (AIP)

Patterns for calling specialized agents within commands.

### AIP-01: Task Tool Invocation

**Description:** Standard pattern for invoking agents via the Task tool.

**When to Use:**
- All agent invocations within commands
- When specialized processing is needed
- For subagent delegation

**Implementation:**
```markdown
### Step Name
- Use Task tool with subagent_type="category::agent-name"
- Prompt: "Detailed instructions for what the agent should do..."
- Expected output: Description of deliverables
- Context: Previous outputs this step needs
```

**Complete Example:**
```markdown
### 1. Security Vulnerability Scanning
- Use Task tool with subagent_type="security-scanning::security-auditor"
- Prompt: "Perform comprehensive security assessment on: $ARGUMENTS.
  Execute SAST analysis with Semgrep/SonarQube, DAST scanning with
  OWASP ZAP, dependency audit with Snyk/Trivy, secrets detection
  with GitLeaks/TruffleHog. Generate SBOM for supply chain analysis.
  Identify OWASP Top 10 vulnerabilities, CWE weaknesses, and CVE exposures."
- Expected output: Detailed vulnerability report with CVSS scores,
  exploitability analysis, attack surface mapping, secrets exposure report
- Context: Initial baseline for all remediation efforts
```

**Best Practices:**
- Always specify subagent_type
- Write detailed, specific prompts
- Define expected outputs clearly
- Include context requirements

---

### AIP-02: Composite Agent Paths

**Description:** Use hierarchical agent paths for precise specialization.

**When to Use:**
- When generic agent types are too broad
- For technology-specific expertise
- When domain + specialization needed

**Implementation:**
```markdown
### Composite Path Format
subagent_type="category::specialist"

### Examples:
- "backend-development::backend-architect" - Architecture design
- "python-development::python-pro" - Python implementation
- "unit-testing::test-automator" - Test automation
- "security-scanning::security-auditor" - Security analysis
- "deployment-strategies::deployment-engineer" - DevOps/deployment
- "frontend-mobile-security::frontend-security-coder" - Frontend security
- "observability-monitoring::observability-engineer" - Monitoring setup
```

**Agent Category Reference:**

| Category | Specialists |
|----------|-------------|
| `backend-development` | backend-architect, backend-security-coder |
| `python-development` | python-pro |
| `frontend-mobile-development` | frontend-developer |
| `frontend-mobile-security` | frontend-security-coder, mobile-security-coder |
| `security-scanning` | security-auditor |
| `unit-testing` | test-automator |
| `deployment-strategies` | deployment-engineer |
| `database-design` | database-architect, sql-pro |
| `application-performance` | performance-engineer |
| `incident-response` | incident-responder |
| `observability-monitoring` | observability-engineer |
| `error-debugging` | debugger |
| `documentation-generation` | docs-architect |
| `content-marketing` | content-marketer |
| `business-analytics` | business-analyst |
| `data-engineering` | data-engineer |

**Best Practices:**
- Use most specific agent available
- Match agent to task requirements
- Document why specific agent chosen
- Consider fallback agents

---

### AIP-03: Detailed Prompt Engineering

**Description:** Write comprehensive, structured prompts for agent invocation.

**When to Use:**
- All agent prompts
- Complex multi-part tasks
- When precise output needed

**Implementation:**
```markdown
- Prompt: "Analyze the legacy codebase at $ARGUMENTS. Document
  technical debt inventory including:
  1) Outdated dependencies
  2) Deprecated APIs
  3) Security vulnerabilities
  4) Performance bottlenecks
  5) Architectural anti-patterns

  Generate a modernization readiness report with:
  - Component complexity scores (1-10)
  - Dependency mapping
  - Database coupling analysis

  Identify quick wins vs complex refactoring targets."
```

**Prompt Structure:**
1. **Action verb** - What to do (Analyze, Implement, Design, Review)
2. **Target** - What to act on ($ARGUMENTS, specific component)
3. **Requirements** - Numbered list of specific tasks
4. **Output format** - What deliverables to produce
5. **Constraints** - Any limitations or requirements

**Best Practices:**
- Start with clear action verb
- Use numbered lists for multiple requirements
- Specify output format
- Include constraints and context
- Reference $ARGUMENTS appropriately

---

### AIP-04: Output Specification

**Description:** Define expected outputs from each agent invocation.

**When to Use:**
- All agent invocations
- When output feeds next step
- For validation purposes

**Implementation:**
```markdown
### Output Specification Patterns

#### Simple Output
- Expected output: Security audit report

#### Structured Output
- Expected output: Detailed vulnerability report with CVSS scores,
  exploitability analysis, attack surface mapping, secrets exposure report

#### Formatted Output
- Expected output: JSON with structure:
  {
    "issues": [],
    "summary": {"critical": 0, "high": 0, "medium": 0, "low": 0},
    "recommendations": []
  }

#### Multi-part Output
- Expected output:
  1. Test specification
  2. Acceptance criteria
  3. Edge case matrix
```

**Best Practices:**
- Be specific about format
- Include all components expected
- Specify data structure when needed
- Align with next step's requirements

---

### AIP-05: Conditional Agent Selection

**Description:** Select different agents based on context or configuration.

**When to Use:**
- Technology-agnostic commands
- When stack varies
- For flexible workflows

**Implementation:**
```markdown
### Conditional Selection Based on Stack
- Use Task tool with subagent_type="python-development::python-pro"
  (or "golang-pro" / "nodejs-expert" based on stack)
- Prompt: "Implement backend services using the detected/specified
  technology stack..."

### Conditional Selection Based on Task Type
- Use Task tool with subagent_type:
  - For API development: "backend-development::backend-architect"
  - For database work: "database-design::database-architect"
  - For infrastructure: "deployment-strategies::deployment-engineer"

### Configuration-Driven Selection
Based on $CONFIG.stack:
- "python": Use python-pro
- "go": Use golang-pro
- "node": Use nodejs-expert
- default: Use backend-architect
```

**Best Practices:**
- Document selection criteria
- Provide clear options
- Handle default case
- Consider user override

---

## Validation Patterns (VP)

Patterns for quality gates and verification within commands.

### VP-01: Phase Gate Validation

**Description:** Require validation before proceeding to next phase.

**When to Use:**
- Between major phases
- Before irreversible actions
- For quality assurance

**Implementation:**
```markdown
### 4. Verify Test Failure
- Use Task tool with subagent_type="code-reviewer"
- Prompt: "Verify that all tests are failing correctly. Ensure
  failures are for the right reasons (missing implementation,
  not test errors). Confirm no false positives."
- Output: Test failure verification report
- **GATE**: Do not proceed until all tests fail appropriately

---
### PHASE GATE: Phase 2 → Phase 3
Before proceeding to Implementation:
- [ ] All requirements analyzed
- [ ] Architecture design approved
- [ ] Risk assessment complete
- [ ] Test strategy defined
---
```

**Real Examples:**
- `tdd-cycle.md` - RED/GREEN/REFACTOR gates
- `git-workflow.md` - Pre-push validation gate
- `security-hardening.md` - Remediation before controls

**Best Practices:**
- Mark gates explicitly with **GATE**
- List specific conditions
- Block progression until met
- Document gate purpose

---

### VP-02: Severity-Based Classification

**Description:** Classify issues by severity for prioritized handling.

**When to Use:**
- Issue identification workflows
- Security and quality analysis
- Triage processes

**Implementation:**
```markdown
## Severity Classification

### Severity Levels
- **P0/CRITICAL**: Immediate action required, blocks deployment
- **P1/HIGH**: Must fix before release, significant impact
- **P2/MEDIUM**: Should fix, moderate impact
- **P3/LOW**: Nice to fix, minimal impact

### Classification Output
Generate report with severity levels:
{
  "critical": [/* blocking issues */],
  "high": [/* significant issues */],
  "medium": [/* moderate issues */],
  "low": [/* minor issues */]
}

### Severity-Based Actions
- P0/CRITICAL: Stop workflow, escalate immediately
- P1/HIGH: Fix before proceeding to next phase
- P2/MEDIUM: Track for resolution, may proceed
- P3/LOW: Document for future improvement
```

**Real Examples:**
- `incident-response.md` - P0-P3 severity levels
- `git-workflow.md` - Critical/High/Medium/Low issues
- `security-hardening.md` - CVSS-based severity

**Best Practices:**
- Use consistent severity scale
- Define clear criteria for each level
- Specify actions per severity
- Include escalation paths

---

### VP-03: Threshold-Based Validation

**Description:** Define numeric thresholds for pass/fail decisions.

**When to Use:**
- Coverage requirements
- Performance benchmarks
- Quality metrics

**Implementation:**
```markdown
## Validation Thresholds

### Coverage Thresholds
- Minimum line coverage: 80%
- Minimum branch coverage: 75%
- Critical path coverage: 100%

### Performance Thresholds
- P95 latency: < 200ms
- Error rate: < 0.1%
- Throughput: > 1000 req/s

### Quality Thresholds
- Cyclomatic complexity: < 10
- Method length: < 20 lines
- Class length: < 200 lines
- Duplicate code blocks: < 3 lines

### Validation
- [ ] Coverage exceeds 80% line coverage
- [ ] No P95 latency regression > 10%
- [ ] All complexity metrics within limits
```

**Real Examples:**
- `tdd-cycle.md` - Coverage thresholds
- `git-workflow.md` - Test coverage > 80%
- `legacy-modernize.md` - Performance within 110% baseline

**Best Practices:**
- Define specific numeric values
- Justify threshold selection
- Allow configuration override
- Report actual vs threshold

---

### VP-04: Validation Checkpoint Matrix

**Description:** Comprehensive checklist for phase validation.

**When to Use:**
- Complex phase transitions
- Multi-aspect validation
- Audit trail requirements

**Implementation:**
```markdown
## Validation Checkpoints

### RED Phase Validation
- [ ] All tests written before implementation
- [ ] All tests fail with meaningful error messages
- [ ] Test failures are due to missing implementation
- [ ] No test passes accidentally

### GREEN Phase Validation
- [ ] All tests pass
- [ ] No extra code beyond test requirements
- [ ] Coverage meets minimum thresholds
- [ ] No test was modified to make it pass

### REFACTOR Phase Validation
- [ ] All tests still pass after refactoring
- [ ] Code complexity reduced
- [ ] Duplication eliminated
- [ ] Performance improved or maintained
- [ ] Test readability improved
```

**Real Examples:**
- `tdd-cycle.md` - RED/GREEN/REFACTOR checklists
- `git-workflow.md` - Success criteria checklist
- `incident-response.md` - Immediate/Long-term success

**Best Practices:**
- Use checkbox format
- Group by phase/category
- Include both process and technical items
- Make items verifiable

---

### VP-05: Continuous Validation Loop

**Description:** Run validation after each change, not just at gates.

**When to Use:**
- Iterative development workflows
- When changes must maintain invariants
- TDD and continuous testing

**Implementation:**
```markdown
## Continuous Validation

### After Each Change
1. Run affected unit tests
2. Verify coverage not decreased
3. Check no new linting errors
4. Validate no security regressions

### Validation Loop
```
Make Change → Run Tests → Check Coverage → Lint → Proceed
     ↑                                        |
     └────────── Fix Issues ←─────────────────┘
```

### Automated Validation
Configure pre-commit hooks:
- Run tests on changed files
- Check formatting
- Scan for secrets
- Validate commit message
```

**Real Examples:**
- `tdd-cycle.md` - Tests after each refactoring
- `git-workflow.md` - Pre-commit validation
- `security-hardening.md` - Continuous security validation

**Best Practices:**
- Automate validation where possible
- Keep validation fast
- Provide clear feedback
- Don't skip validation steps

---

## Error Handling Patterns (EHP)

Patterns for handling failures and recovery.

### EHP-01: Rollback Procedures

**Description:** Define explicit rollback steps for failure recovery.

**When to Use:**
- Deployment commands
- State-changing operations
- When recovery is critical

**Implementation:**
```markdown
## Rollback Procedures

### In Case of Issues After Merge

1. **Immediate Revert**: Create revert PR
   ```bash
   git revert <commit-hash>
   git push origin HEAD
   ```

2. **Feature Flag Disable**: If using feature flags
   - Disable flag in LaunchDarkly/Unleash
   - Verify traffic routed to fallback

3. **Hotfix Branch**: For critical issues
   ```bash
   git checkout main
   git checkout -b hotfix/<issue>
   # Apply fix
   git push -u origin hotfix/<issue>
   ```

4. **Communication**: Notify team
   - Post in #incidents channel
   - Update status page

5. **Root Cause Analysis**: Document
   - Use postmortem template
   - Schedule review meeting
```

**Real Examples:**
- `git-workflow.md` - Git revert procedures
- `legacy-modernize.md` - Traffic rollback
- `incident-response.md` - Comprehensive rollback

**Best Practices:**
- Order by speed/impact
- Include specific commands
- Cover communication
- Plan for various failure types

---

### EHP-02: Failure Recovery Workflow

**Description:** Define recovery steps when a phase fails.

**When to Use:**
- Multi-phase workflows
- When partial completion possible
- For graceful degradation

**Implementation:**
```markdown
## Failure Recovery

### If TDD Discipline Is Broken
1. **STOP** immediately
2. Identify which phase was violated
3. Rollback to last valid state
4. Resume from correct phase
5. Document lesson learned

### If Security Scan Fails
1. Categorize findings by severity
2. Block deployment for CRITICAL/HIGH
3. Generate remediation report
4. Assign owners for each finding
5. Re-run scan after fixes

### If Deployment Fails
1. Automatic rollback triggered
2. Capture deployment logs
3. Identify failure point
4. Fix and retry OR escalate
5. Update runbook with learnings
```

**Real Examples:**
- `tdd-cycle.md` - TDD discipline recovery
- `incident-response.md` - Incident recovery
- `deployment-*.md` - Deployment recovery

**Best Practices:**
- Define recovery for each phase
- Include immediate actions
- Plan for partial failures
- Document learnings

---

### EHP-03: Graceful Degradation

**Description:** Define fallback behavior when components fail.

**When to Use:**
- Complex multi-agent workflows
- When partial success is acceptable
- For resilient operations

**Implementation:**
```markdown
## Graceful Degradation

### If Agent Unavailable
- Primary: Use specialized agent (e.g., python-pro)
- Fallback: Use general agent (e.g., backend-architect)
- Last resort: Skip optional step, document gap

### If External Service Fails
- Retry with exponential backoff (3 attempts)
- Use cached results if available
- Skip non-critical integrations
- Log degradation for review

### If Validation Partially Fails
- Continue with passing components
- Track failed validations
- Require manual approval for exceptions
- Generate exception report
```

**Best Practices:**
- Define primary and fallback paths
- Set clear degradation boundaries
- Log all degradations
- Require review of exceptions

---

### EHP-04: Error Escalation Path

**Description:** Define escalation procedures for unrecoverable errors.

**When to Use:**
- Critical failures
- When human intervention needed
- For security incidents

**Implementation:**
```markdown
## Error Escalation

### Escalation Levels

**Level 1: Automated Recovery**
- Retry failed operation
- Use fallback agent
- Apply cached results

**Level 2: Manual Intervention**
- Alert on-call engineer
- Pause workflow
- Await human decision

**Level 3: Incident Response**
- Page incident commander
- Activate war room
- Begin incident protocol

### Escalation Triggers

| Trigger | Level | Action |
|---------|-------|--------|
| Transient failure | 1 | Auto-retry |
| Persistent failure | 2 | Alert human |
| Security breach | 3 | Incident response |
| Data loss risk | 3 | Immediate escalation |
| SLA violation | 2 | Alert + remediation |
```

**Real Examples:**
- `incident-response.md` - Full escalation matrix
- `security-hardening.md` - Security escalation
- `smart-fix.md` - Debug escalation

**Best Practices:**
- Define clear escalation levels
- Specify triggers for each level
- Include contact information
- Document escalation history

---

## Configuration Patterns (CP)

Patterns for command customization and options.

### CP-01: Flag-Based Configuration

**Description:** Use command-line style flags for options.

**When to Use:**
- Boolean options
- Mode selection
- Optional features

**Implementation:**
```markdown
## Supported Flags

- `--skip-tests`: Skip automated test execution (use with caution)
- `--draft-pr`: Create PR as draft for work-in-progress
- `--no-push`: Perform all checks but don't push to remote
- `--squash`: Squash commits before pushing
- `--conventional`: Enforce Conventional Commits format strictly
- `--trunk-based`: Use trunk-based development workflow
- `--feature-branch`: Use feature branch workflow (default)
- `--incremental`: Process one test at a time
- `--suite`: Process entire test suite at once

### Flag Processing
Parse $ARGUMENTS for flags:
- If `--skip-tests`: Skip Phase 2 (Testing)
- If `--draft-pr`: Create PR with draft status
- If `--no-push`: Stop before push step
```

**Real Examples:**
- `git-workflow.md` - 7 workflow flags
- `tdd-cycle.md` - `--incremental` and `--suite` modes
- `legacy-modernize.md` - Migration strategy flags

**Best Practices:**
- Use `--kebab-case` naming
- Document each flag's effect
- Indicate defaults
- Warn about risky flags

---

### CP-02: Parameter Configuration

**Description:** Accept named parameters for variable values.

**When to Use:**
- Required inputs
- Variable values (not boolean)
- Technology/environment specification

**Implementation:**
```markdown
## Configuration Options

- `stack`: Specify technology stack
  - Examples: "React/FastAPI/PostgreSQL", "Next.js/Django/MongoDB"
  - Default: Detect from project

- `deployment_target`: Cloud platform
  - Values: "AWS", "GCP", "Azure", "on-premises"
  - Default: "AWS"

- `testing_depth`: Test coverage level
  - Values: "comprehensive", "essential"
  - Default: "comprehensive"

- `compliance`: Compliance frameworks to validate
  - Values: ["GDPR", "HIPAA", "SOC2", "PCI-DSS"]
  - Default: []

### Parameter Usage
```
/command stack="React/Django" deployment_target="GCP" testing_depth="essential"
```
```

**Real Examples:**
- `full-stack-feature.md` - Stack, deployment, compliance options
- `context-save.md` - Context type, storage format
- `security-hardening.md` - Scanning depth, compliance frameworks

**Best Practices:**
- Use descriptive names
- Document valid values
- Provide sensible defaults
- Show example usage

---

### CP-03: Threshold Configuration

**Description:** Allow customization of validation thresholds.

**When to Use:**
- Quality gates
- Performance requirements
- Project-specific standards

**Implementation:**
```markdown
## Configurable Thresholds

### Coverage Thresholds (defaults)
- `min_line_coverage`: 80% (can override)
- `min_branch_coverage`: 75% (can override)
- `critical_path_coverage`: 100% (cannot override)

### Performance Thresholds
- `max_latency_p95`: 200ms
- `max_error_rate`: 0.1%
- `min_throughput`: 1000 req/s

### Override Syntax
```
/command min_line_coverage=70 max_latency_p95=300
```

### Threshold Validation
```python
thresholds = {
    'min_line_coverage': config.get('min_line_coverage', 80),
    'min_branch_coverage': config.get('min_branch_coverage', 75),
}
if actual_coverage < thresholds['min_line_coverage']:
    fail("Coverage below threshold")
```
```

**Best Practices:**
- Document default values
- Allow reasonable overrides
- Protect critical thresholds
- Validate threshold values

---

### CP-04: Mode Selection

**Description:** Support different operational modes.

**When to Use:**
- Different workflow approaches
- Speed vs thoroughness tradeoffs
- Different use case variants

**Implementation:**
```markdown
## Operational Modes

### Scanning Depth Modes
- `quick`: Fast scan, common vulnerabilities only (~5 minutes)
- `standard`: Balanced scan, most vulnerabilities (~30 minutes)
- `comprehensive`: Full scan, all checks (~2 hours)

### Development Modes
- `--incremental`: Test-by-test development
  1. Write ONE failing test
  2. Make ONLY that test pass
  3. Refactor if needed
  4. Repeat

- `--suite`: Batch test development
  1. Write ALL tests for feature
  2. Implement code to pass ALL
  3. Refactor entire module

### Migration Modes
- `--parallel-systems`: Keep both systems running (gradual)
- `--big-bang`: Full cutover after validation (faster)
- `--by-feature`: Migrate complete features
- `--database-first`: Prioritize database modernization
```

**Real Examples:**
- `security-hardening.md` - Scanning depth modes
- `tdd-cycle.md` - Incremental vs suite mode
- `legacy-modernize.md` - Migration strategy modes

**Best Practices:**
- Clearly differentiate modes
- Document tradeoffs
- Set sensible default mode
- Allow mode combinations when appropriate

---

## Pattern Combinations

Common combinations of patterns for specific command types.

### Orchestration Command Pattern Stack

For full-featured orchestration commands:
```
OP-01 (Multi-Phase) + OP-03 (Context Passing) + OP-05 (Convergence)
WP-01 (Extended Thinking) + WP-02 (Configuration) + WP-03 (Success Criteria)
AIP-01 (Task Invocation) + AIP-02 (Composite Paths) + AIP-04 (Output Spec)
VP-01 (Phase Gates) + VP-04 (Checkpoint Matrix)
EHP-01 (Rollback) + EHP-02 (Recovery)
CP-02 (Parameters) + CP-04 (Modes)
```

### Security Command Pattern Stack

For security-focused commands:
```
OP-01 (Multi-Phase) + OP-04 (Domain Agents)
WP-02 (Configuration) + WP-03 (Success Criteria)
AIP-02 (Composite Paths) + AIP-03 (Detailed Prompts)
VP-01 (Phase Gates) + VP-02 (Severity Classification)
EHP-04 (Escalation)
CP-01 (Flags) + CP-03 (Thresholds)
```

### Testing Command Pattern Stack

For test-focused commands:
```
OP-01 (Multi-Phase) + OP-03 (Context Passing)
WP-01 (Extended Thinking) + WP-03 (Success Criteria) + WP-06 (Reference)
AIP-01 (Task Invocation) + AIP-04 (Output Spec)
VP-01 (Phase Gates) + VP-03 (Thresholds) + VP-05 (Continuous)
EHP-02 (Recovery)
CP-01 (Flags) + CP-03 (Thresholds) + CP-04 (Modes)
```

---

## Quick Reference

### Pattern Code Lookup

| Code | Pattern Name | Category |
|------|--------------|----------|
| OP-01 | Multi-Phase Sequential | Orchestration |
| OP-02 | Parallel Agent Execution | Orchestration |
| OP-03 | Context Passing Chain | Orchestration |
| OP-04 | Domain-Specific Agent Selection | Orchestration |
| OP-05 | Milestone Convergence | Orchestration |
| WP-01 | Extended Thinking Introduction | Workflow |
| WP-02 | Configuration Block | Workflow |
| WP-03 | Success Criteria Definition | Workflow |
| WP-04 | Coordination Notes Section | Workflow |
| WP-05 | Input Arguments Handling | Workflow |
| WP-06 | Reference Documentation | Workflow |
| AIP-01 | Task Tool Invocation | Agent Invocation |
| AIP-02 | Composite Agent Paths | Agent Invocation |
| AIP-03 | Detailed Prompt Engineering | Agent Invocation |
| AIP-04 | Output Specification | Agent Invocation |
| AIP-05 | Conditional Agent Selection | Agent Invocation |
| VP-01 | Phase Gate Validation | Validation |
| VP-02 | Severity-Based Classification | Validation |
| VP-03 | Threshold-Based Validation | Validation |
| VP-04 | Validation Checkpoint Matrix | Validation |
| VP-05 | Continuous Validation Loop | Validation |
| EHP-01 | Rollback Procedures | Error Handling |
| EHP-02 | Failure Recovery Workflow | Error Handling |
| EHP-03 | Graceful Degradation | Error Handling |
| EHP-04 | Error Escalation Path | Error Handling |
| CP-01 | Flag-Based Configuration | Configuration |
| CP-02 | Parameter Configuration | Configuration |
| CP-03 | Threshold Configuration | Configuration |
| CP-04 | Mode Selection | Configuration |

### Pattern Selection by Command Type

| Command Type | Essential Patterns | Recommended Patterns |
|--------------|-------------------|---------------------|
| Orchestration | OP-01, OP-03, WP-03, AIP-01 | OP-02, OP-05, WP-01, VP-01 |
| Security | OP-01, VP-02, AIP-02, EHP-04 | WP-02, CP-03, VP-01 |
| Testing | OP-01, VP-03, VP-05, WP-03 | WP-06, CP-04, EHP-02 |
| Deployment | OP-01, EHP-01, VP-01, CP-02 | OP-03, WP-04, EHP-03 |
| Migration | OP-01, OP-03, EHP-01, CP-04 | VP-03, WP-03, EHP-02 |
| Code Quality | OP-01, VP-02, AIP-03, WP-03 | OP-03, VP-04, CP-01 |

---

## Related Resources

- **[COMMAND_QUICK_START.md](COMMAND_QUICK_START.md)** - 5-step command creation process
- **[COMMAND_USE_CASE_LOOKUP.md](COMMAND_USE_CASE_LOOKUP.md)** - Find patterns by use case
- **[COMMAND_QUALITY_RUBRIC.md](COMMAND_QUALITY_RUBRIC.md)** - 100-point quality scoring
- **[full_stack_feature.md](../../domain-agentic-resources/commands/orchestration/full_stack_feature.md)** - Example multi-agent command
- **[agents/README.md](../../domain-agentic-resources/agents/README.md)** - Available agents to invoke
- **[skills/README.md](../../domain-agentic-resources/skills/README.md)** - Available skills to reference

---

**Document End**

**Total Patterns:** 29
**Categories:** 6
**Generated:** 2025-12-31
