# Command Use Case Lookup

**Purpose:** Find the right pattern combinations for your command type
**Usage:** Identify your use case → Find recommended patterns → Build command

---

## Table of Contents

1. [How to Use This Guide](#how-to-use-this-guide)
2. [Use Case Categories](#use-case-categories)
3. [Development Workflows](#development-workflows)
4. [Security Operations](#security-operations)
5. [Testing Workflows](#testing-workflows)
6. [DevOps and Infrastructure](#devops-and-infrastructure)
7. [Migration and Modernization](#migration-and-modernization)
8. [Incident and Troubleshooting](#incident-and-troubleshooting)
9. [Documentation and Analysis](#documentation-and-analysis)
10. [Pattern Combination Reference](#pattern-combination-reference)

---

## How to Use This Guide

### Step 1: Identify Your Use Case Category

Find the category that best matches what you're building:

| Category | You want to... |
|----------|---------------|
| [Development Workflows](#development-workflows) | Build features, implement code |
| [Security Operations](#security-operations) | Scan, audit, harden systems |
| [Testing Workflows](#testing-workflows) | Generate tests, TDD, validation |
| [DevOps and Infrastructure](#devops-and-infrastructure) | Deploy, monitor, automate |
| [Migration and Modernization](#migration-and-modernization) | Upgrade, migrate, modernize |
| [Incident and Troubleshooting](#incident-and-troubleshooting) | Debug, respond, fix |
| [Documentation and Analysis](#documentation-and-analysis) | Document, analyze, report |

### Step 2: Find Your Specific Use Case

Look up the specific task within that category.

### Step 3: Apply Recommended Patterns

Use the pattern codes with `COMMAND_PATTERN_INDEX.md` for implementation details.

---

## Use Case Categories

### Quick Reference Matrix

| Use Case | Essential Patterns | Phases | Key Agents |
|----------|-------------------|--------|------------|
| Full-stack feature | OP-01, OP-02, OP-03, OP-05 | 4 | backend, frontend, db, test |
| Security scan | OP-01, VP-02, EHP-04 | 3 | security-auditor |
| TDD workflow | OP-01, VP-01, VP-05 | 6 | test-automator, code-reviewer |
| CI/CD setup | OP-01, CP-02, EHP-01 | 3 | deployment-engineer |
| Legacy migration | OP-01, OP-03, VP-03 | 5 | legacy-modernizer, test-automator |
| Incident response | OP-01, VP-02, EHP-04 | 5 | incident-responder, debugger |
| Code review | OP-01, VP-02, AIP-03 | 3 | code-reviewer |

---

## Development Workflows

### Full-Stack Feature Development

**Use Case:** Build complete features across frontend, backend, and database

**Pattern Combination:**
```
Orchestration: OP-01 + OP-02 + OP-03 + OP-05
Workflow:      WP-01 + WP-02 + WP-03 + WP-04
Agent:         AIP-01 + AIP-02 + AIP-04 + AIP-05
Validation:    VP-01 + VP-03
Error:         EHP-01 + EHP-03
Config:        CP-02 + CP-04
```

**Phase Structure:**
```
Phase 1: Architecture & Design (3 steps)
  - Database design → Backend architecture → Frontend design
Phase 2: Parallel Implementation (3 parallel steps)
  - Backend || Frontend || Database
  [Convergence point]
Phase 3: Integration & Testing (3 steps)
  - Contract tests → E2E tests → Security audit
Phase 4: Deployment (3 steps)
  - Infrastructure → Monitoring → Performance
```

**Key Agents:**
- `database-design::database-architect`
- `backend-development::backend-architect`
- `frontend-mobile-development::frontend-developer`
- `unit-testing::test-automator`
- `deployment-strategies::deployment-engineer`

**Example Commands:** `full-stack-feature`, `data-driven-feature`, `multi-platform`

---

### API Development

**Use Case:** Design and implement APIs with documentation

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03 + OP-04
Workflow:      WP-01 + WP-03 + WP-05
Agent:         AIP-01 + AIP-02 + AIP-03
Validation:    VP-01 + VP-03
Error:         EHP-02
Config:        CP-01 + CP-02
```

**Phase Structure:**
```
Phase 1: Design (2 steps)
  - API specification → Schema design
Phase 2: Implementation (2 steps)
  - Endpoint implementation → Validation logic
Phase 3: Testing & Documentation (2 steps)
  - Contract tests → API documentation
```

**Key Agents:**
- `backend-development::backend-architect`
- `unit-testing::test-automator`
- `documentation-generation::docs-architect`

**Example Commands:** `api-mock`, `component-scaffold`

---

### Code Refactoring

**Use Case:** Improve code quality while maintaining functionality

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-03 + WP-06
Agent:         AIP-01 + AIP-03 + AIP-04
Validation:    VP-01 + VP-03 + VP-05
Error:         EHP-02
Config:        CP-01 + CP-03
```

**Phase Structure:**
```
Phase 1: Analysis (2 steps)
  - Code analysis → Test coverage check
Phase 2: Refactoring (2-3 steps)
  - Apply refactoring → Verify tests pass → Repeat
Phase 3: Validation (2 steps)
  - Full test suite → Quality metrics
```

**Key Agents:**
- `comprehensive-review::code-reviewer`
- `unit-testing::test-automator`

**Example Commands:** `refactor-clean`, `tech-debt`

---

### Git Workflow Automation

**Use Case:** Automate commit, review, and PR processes

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-01 + WP-02 + WP-03 + WP-06
Agent:         AIP-01 + AIP-02 + AIP-04
Validation:    VP-01 + VP-02 + VP-04
Error:         EHP-01 + EHP-02
Config:        CP-01
```

**Phase Structure:**
```
Phase 1: Pre-Commit Review (2 steps)
  - Code quality assessment → Breaking change analysis
Phase 2: Testing (2 steps)
  - Test execution → Gap analysis
Phase 3: Commit (2 steps)
  - Change categorization → Message generation
Phase 4: PR Creation (2 steps)
  - Description generation → Metadata setup
```

**Key Agents:**
- `comprehensive-review::code-reviewer`
- `unit-testing::test-automator`
- `llm-application-dev::prompt-engineer`
- `documentation-generation::docs-architect`

**Example Commands:** `git-workflow`, `pr-enhance`

---

## Security Operations

### Security Scanning

**Use Case:** Identify vulnerabilities in code and dependencies

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-02 + WP-03
Agent:         AIP-01 + AIP-02 + AIP-03
Validation:    VP-02 + VP-03
Error:         EHP-04
Config:        CP-02 + CP-03 + CP-04
```

**Phase Structure:**
```
Phase 1: Scanning (3-4 steps)
  - SAST → DAST → Dependency scan → Secrets detection
Phase 2: Analysis (2 steps)
  - Threat modeling → Risk assessment
Phase 3: Reporting (1 step)
  - Consolidated report generation
```

**Key Agents:**
- `security-scanning::security-auditor`

**Example Commands:** `security-sast`, `security-dependencies`, `xss-scan`

---

### Security Hardening

**Use Case:** Implement security controls and remediate vulnerabilities

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03 + OP-04
Workflow:      WP-01 + WP-02 + WP-03 + WP-04
Agent:         AIP-01 + AIP-02 + AIP-03 + AIP-04
Validation:    VP-01 + VP-02 + VP-03
Error:         EHP-01 + EHP-04
Config:        CP-02 + CP-04
```

**Phase Structure:**
```
Phase 1: Assessment (3 steps)
  - Vulnerability scan → Threat modeling → Architecture review
Phase 2: Remediation (4 steps)
  - Critical fixes → Backend hardening → Frontend hardening → Mobile hardening
Phase 3: Controls (3 steps)
  - Auth enhancement → Infrastructure controls → Secrets management
Phase 4: Validation (3 steps)
  - Penetration testing → Compliance verification → Monitoring setup
```

**Key Agents:**
- `security-scanning::security-auditor`
- `backend-api-security::backend-security-coder`
- `frontend-mobile-security::frontend-security-coder`
- `deployment-strategies::deployment-engineer`

**Example Commands:** `security-hardening`, `compliance-check`

---

### Compliance Auditing

**Use Case:** Verify compliance with security frameworks

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-02 + WP-03
Agent:         AIP-01 + AIP-03
Validation:    VP-02 + VP-04
Error:         EHP-04
Config:        CP-02
```

**Phase Structure:**
```
Phase 1: Assessment (2 steps)
  - Framework mapping → Gap analysis
Phase 2: Evidence Collection (2 steps)
  - Control validation → Documentation review
Phase 3: Reporting (2 steps)
  - Findings report → Remediation plan
```

**Key Agents:**
- `security-scanning::security-auditor`
- `documentation-generation::docs-architect`

**Example Commands:** `compliance-check`

---

## Testing Workflows

### Test-Driven Development (TDD)

**Use Case:** Implement features using red-green-refactor cycle

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-01 + WP-02 + WP-03 + WP-06
Agent:         AIP-01 + AIP-02 + AIP-04
Validation:    VP-01 + VP-03 + VP-04 + VP-05
Error:         EHP-02
Config:        CP-01 + CP-03 + CP-04
```

**Phase Structure:**
```
Phase 1: Specification (2 steps)
  - Requirements analysis → Test architecture design
Phase 2: RED (2 steps)
  - Write failing tests → Verify failure
  [GATE: All tests must fail]
Phase 3: GREEN (2 steps)
  - Minimal implementation → Verify success
  [GATE: All tests must pass]
Phase 4: REFACTOR (2 steps)
  - Code refactoring → Test refactoring
Phase 5: Integration (2 steps)
  - Integration tests → Implementation
Phase 6: Review (2 steps)
  - Performance tests → Final review
```

**Key Agents:**
- `comprehensive-review::architect-review`
- `unit-testing::test-automator`
- `backend-development::backend-architect`
- `tdd-workflows::code-reviewer`

**Example Commands:** `tdd-cycle`, `tdd-red`, `tdd-green`, `tdd-refactor`

---

### Test Generation

**Use Case:** Generate comprehensive tests for existing code

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-03 + WP-05
Agent:         AIP-01 + AIP-02 + AIP-03
Validation:    VP-03
Error:         EHP-02
Config:        CP-01 + CP-03
```

**Phase Structure:**
```
Phase 1: Analysis (2 steps)
  - Code analysis → Edge case identification
Phase 2: Generation (2-3 steps)
  - Unit tests → Integration tests → E2E tests
Phase 3: Validation (2 steps)
  - Coverage analysis → Test execution
```

**Key Agents:**
- `unit-testing::test-automator`
- `comprehensive-review::code-reviewer`

**Example Commands:** `test-generate`

---

## DevOps and Infrastructure

### CI/CD Pipeline Setup

**Use Case:** Configure automated build, test, and deployment pipelines

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-02 + WP-03
Agent:         AIP-01 + AIP-02 + AIP-04
Validation:    VP-01 + VP-03
Error:         EHP-01 + EHP-03
Config:        CP-01 + CP-02
```

**Phase Structure:**
```
Phase 1: Design (2 steps)
  - Pipeline architecture → Stage definition
Phase 2: Implementation (3 steps)
  - Build configuration → Test integration → Deploy configuration
Phase 3: Validation (2 steps)
  - Pipeline testing → Documentation
```

**Key Agents:**
- `cicd-automation::deployment-engineer`
- `deployment-strategies::deployment-engineer`

**Example Commands:** `workflow-automate`, `typescript-scaffold`, `python-scaffold`

---

### Monitoring and Observability

**Use Case:** Set up monitoring, logging, and alerting

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-02 + WP-03
Agent:         AIP-01 + AIP-02 + AIP-04
Validation:    VP-03
Error:         EHP-03
Config:        CP-02
```

**Phase Structure:**
```
Phase 1: Design (2 steps)
  - Metrics definition → Dashboard design
Phase 2: Implementation (3 steps)
  - Metrics collection → Tracing setup → Log aggregation
Phase 3: Alerting (2 steps)
  - Alert rules → Runbook creation
```

**Key Agents:**
- `observability-monitoring::observability-engineer`
- `deployment-strategies::deployment-engineer`

**Example Commands:** `monitor-setup`, `slo-implement`

---

### Deployment Automation

**Use Case:** Automate deployment with safety controls

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-02 + WP-03 + WP-04
Agent:         AIP-01 + AIP-02 + AIP-04
Validation:    VP-01 + VP-03
Error:         EHP-01 + EHP-02 + EHP-03
Config:        CP-01 + CP-02 + CP-04
```

**Phase Structure:**
```
Phase 1: Preparation (2 steps)
  - Configuration validation → Pre-deploy checks
Phase 2: Deployment (2 steps)
  - Staged rollout → Health verification
Phase 3: Validation (2 steps)
  - Post-deploy testing → Monitoring setup
```

**Key Agents:**
- `deployment-strategies::deployment-engineer`
- `observability-monitoring::observability-engineer`

**Example Commands:** `config-validate`

---

## Migration and Modernization

### Legacy System Modernization

**Use Case:** Incrementally modernize legacy systems

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03 + OP-04
Workflow:      WP-01 + WP-02 + WP-03 + WP-04
Agent:         AIP-01 + AIP-02 + AIP-03 + AIP-05
Validation:    VP-01 + VP-03 + VP-04
Error:         EHP-01 + EHP-02 + EHP-03
Config:        CP-01 + CP-02 + CP-04
```

**Phase Structure:**
```
Phase 1: Assessment (3 steps)
  - Legacy analysis → Dependency mapping → Business impact
Phase 2: Test Coverage (3 steps)
  - Coverage analysis → Contract testing → Test data strategy
Phase 3: Migration (3 steps)
  - Infrastructure setup → Component modernization → Security hardening
Phase 4: Validation (2 steps)
  - Performance testing → Progressive rollout
Phase 5: Completion (2 steps)
  - Decommissioning → Documentation
```

**Key Agents:**
- `legacy-modernizer`
- `comprehensive-review::architect-review`
- `business-analytics::business-analyst`
- `unit-testing::test-automator`
- `deployment-strategies::deployment-engineer`

**Example Commands:** `legacy-modernize`, `code-migrate`

---

### Dependency Upgrades

**Use Case:** Safely upgrade dependencies and frameworks

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-02 + WP-03
Agent:         AIP-01 + AIP-03
Validation:    VP-01 + VP-03
Error:         EHP-01 + EHP-02
Config:        CP-01 + CP-02
```

**Phase Structure:**
```
Phase 1: Analysis (2 steps)
  - Dependency audit → Compatibility check
Phase 2: Upgrade (2-3 steps)
  - Staged upgrade → Test validation → Fix issues
Phase 3: Validation (2 steps)
  - Full test suite → Performance check
```

**Key Agents:**
- `legacy-modernizer`
- `unit-testing::test-automator`

**Example Commands:** `deps-upgrade`, `deps-audit`

---

## Incident and Troubleshooting

### Incident Response

**Use Case:** Coordinate rapid incident resolution

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03 + OP-04
Workflow:      WP-01 + WP-02 + WP-03 + WP-04
Agent:         AIP-01 + AIP-02 + AIP-03 + AIP-04
Validation:    VP-01 + VP-02
Error:         EHP-01 + EHP-02 + EHP-04
Config:        CP-02 + CP-04
```

**Phase Structure:**
```
Phase 1: Detection & Triage (3 steps)
  - Incident classification → Observability analysis → Initial mitigation
Phase 2: Investigation (3 steps)
  - Deep debugging → Security assessment → Performance analysis
Phase 3: Resolution (2 steps)
  - Fix implementation → Deployment validation
Phase 4: Communication (2 steps)
  - Stakeholder updates → Customer impact assessment
Phase 5: Postmortem (3 steps)
  - Blameless postmortem → Monitoring enhancement → System hardening
```

**Key Agents:**
- `incident-response::incident-responder`
- `observability-monitoring::observability-engineer`
- `error-debugging::debugger`
- `security-scanning::security-auditor`
- `application-performance::performance-engineer`
- `backend-development::backend-architect`
- `deployment-strategies::deployment-engineer`
- `content-marketing::content-marketer`
- `documentation-generation::docs-architect`

**Example Commands:** `incident-response`, `error-analysis`

---

### Debugging Workflows

**Use Case:** Systematically debug complex issues

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-01 + WP-03
Agent:         AIP-01 + AIP-02 + AIP-03
Validation:    VP-02
Error:         EHP-02 + EHP-04
Config:        CP-01
```

**Phase Structure:**
```
Phase 1: Information Gathering (2 steps)
  - Error analysis → Log investigation
Phase 2: Root Cause Analysis (2 steps)
  - Hypothesis generation → Verification
Phase 3: Resolution (2 steps)
  - Fix implementation → Validation
```

**Key Agents:**
- `error-debugging::debugger`
- `observability-monitoring::observability-engineer`

**Example Commands:** `smart-debug`, `smart-fix`, `error-trace`

---

## Documentation and Analysis

### Documentation Generation

**Use Case:** Generate comprehensive documentation from code

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-03 + WP-05
Agent:         AIP-01 + AIP-03
Validation:    VP-04
Config:        CP-01 + CP-02
```

**Phase Structure:**
```
Phase 1: Analysis (2 steps)
  - Code analysis → Structure mapping
Phase 2: Generation (2-3 steps)
  - API docs → Architecture docs → User guides
Phase 3: Review (1 step)
  - Documentation review
```

**Key Agents:**
- `documentation-generation::docs-architect`
- `comprehensive-review::code-reviewer`

**Example Commands:** `doc-generate`, `c4-architecture`

---

### Code Review and Analysis

**Use Case:** Comprehensive code quality review

**Pattern Combination:**
```
Orchestration: OP-01 + OP-03
Workflow:      WP-03
Agent:         AIP-01 + AIP-02 + AIP-03
Validation:    VP-02 + VP-04
Config:        CP-01 + CP-03
```

**Phase Structure:**
```
Phase 1: Analysis (3-4 steps)
  - Code quality → Security → Performance → Architecture
Phase 2: Reporting (2 steps)
  - Findings consolidation → Recommendations
```

**Key Agents:**
- `comprehensive-review::code-reviewer`
- `security-scanning::security-auditor`
- `application-performance::performance-engineer`

**Example Commands:** `ai-review`, `full-review`, `multi-agent-review`

---

## Pattern Combination Reference

### Essential Pattern Stacks by Command Type

#### Orchestration Commands
```
Required:  OP-01, OP-03, WP-03, AIP-01, AIP-04, VP-01
Optional:  OP-02, OP-05, WP-01, WP-02, WP-04, EHP-01
```

#### Security Commands
```
Required:  OP-01, VP-02, AIP-01, AIP-02
Optional:  WP-02, CP-03, EHP-04
```

#### Testing Commands
```
Required:  OP-01, VP-03, VP-05, WP-03, AIP-01
Optional:  WP-06, CP-04, EHP-02
```

#### DevOps Commands
```
Required:  OP-01, WP-03, AIP-01, EHP-01
Optional:  WP-02, CP-02, EHP-03
```

#### Migration Commands
```
Required:  OP-01, OP-03, VP-03, WP-03, EHP-01
Optional:  CP-04, EHP-02, WP-04
```

#### Incident Commands
```
Required:  OP-01, VP-02, WP-03, AIP-01, EHP-04
Optional:  WP-02, WP-04, EHP-01
```

### Pattern Code Quick Reference

| Code | Pattern Name |
|------|--------------|
| OP-01 | Multi-Phase Sequential |
| OP-02 | Parallel Agent Execution |
| OP-03 | Context Passing Chain |
| OP-04 | Domain-Specific Agent Selection |
| OP-05 | Milestone Convergence |
| WP-01 | Extended Thinking Introduction |
| WP-02 | Configuration Block |
| WP-03 | Success Criteria Definition |
| WP-04 | Coordination Notes Section |
| WP-05 | Input Arguments Handling |
| WP-06 | Reference Documentation |
| AIP-01 | Task Tool Invocation |
| AIP-02 | Composite Agent Paths |
| AIP-03 | Detailed Prompt Engineering |
| AIP-04 | Output Specification |
| AIP-05 | Conditional Agent Selection |
| VP-01 | Phase Gate Validation |
| VP-02 | Severity-Based Classification |
| VP-03 | Threshold-Based Validation |
| VP-04 | Validation Checkpoint Matrix |
| VP-05 | Continuous Validation Loop |
| EHP-01 | Rollback Procedures |
| EHP-02 | Failure Recovery Workflow |
| EHP-03 | Graceful Degradation |
| EHP-04 | Error Escalation Path |
| CP-01 | Flag-Based Configuration |
| CP-02 | Parameter Configuration |
| CP-03 | Threshold Configuration |
| CP-04 | Mode Selection |

---

## Related Resources

- **[COMMAND_PATTERN_INDEX.md](COMMAND_PATTERN_INDEX.md)** - Full pattern details
- **[COMMAND_QUICK_START.md](COMMAND_QUICK_START.md)** - 5-step creation process
- **[COMMAND_QUALITY_RUBRIC.md](COMMAND_QUALITY_RUBRIC.md)** - Quality scoring
- **[full_stack_feature.md](../../domain-agentic-resources/commands/orchestration/full_stack_feature.md)** - Example multi-agent command
- **[commands/README.md](../../domain-agentic-resources/commands/README.md)** - Existing commands index

---

**Document End**
