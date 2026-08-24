# Command Creation Quick Start

**Purpose:** Create multi-agent orchestration commands in 5 steps
**Time:** 30-60 minutes per command
**Prerequisites:** Familiarity with agents and Task tool

> **Framework Note:** This guide describes a **multi-agent orchestration methodology** developed for this repository. Official Claude Code slash commands are simpler markdown prompt templates stored in `.claude/commands/`.
>
> This framework provides structure for documenting complex workflows, but the actual orchestration happens through manual execution of the described Task tool invocations.
>
> **Official Claude Code slash commands:**
> - Stored in `.claude/commands/` (project) or `~/.claude/commands/` (personal)
> - Simple markdown files that become `/project:command-name`
> - Support `$ARGUMENTS` keyword for parameter passing
> - Support the same YAML frontmatter as skills

---

## Table of Contents

1. [Overview](#overview)
2. [Quick Start Checklist](#quick-start-checklist)
3. [Step 1: Define Workflow Scope](#step-1-define-workflow-scope)
4. [Step 2: Design Phase Structure](#step-2-design-phase-structure)
5. [Step 3: Select and Configure Agents](#step-3-select-and-configure-agents)
6. [Step 4: Add Validation and Error Handling](#step-4-add-validation-and-error-handling)
7. [Step 5: Validate and Document](#step-5-validate-and-document)
8. [Templates](#templates)
9. [Common Mistakes](#common-mistakes)
10. [Examples](#examples)

---

## Overview

Commands are **multi-agent orchestration workflows** that coordinate specialized agents to execute complex, multi-phase operations. Unlike agents (specialized identities) or skills (knowledge packages), commands represent entire development processes.

### When to Create a Command

| Use Case | Create Command? |
|----------|----------------|
| Multi-phase workflow (3+ phases) | ✅ Yes |
| Coordinates multiple agents | ✅ Yes |
| End-to-end process (design → deploy) | ✅ Yes |
| Single-agent task | ❌ No (use agent directly) |
| Knowledge/reference lookup | ❌ No (use skill) |
| Simple single-step operation | ❌ No (use prompt) |

### Command vs Agent vs Skill

| Aspect | Command | Agent | Skill |
|--------|---------|-------|-------|
| **Purpose** | Orchestrate workflows | Specialized expertise | Knowledge package |
| **Scope** | End-to-end process | Single domain | Reference material |
| **Coordination** | Multiple agents | Single identity | Referenced by agents |
| **Invocation** | `/command-name` | Task tool subagent | Skill loading |
| **Duration** | Long-running | Per-task | Always available |

---

## Quick Start Checklist

Use this checklist for rapid command creation:

```
□ Step 1: Define Workflow Scope
  □ Identify workflow objective
  □ Map inputs and outputs
  □ Determine command category

□ Step 2: Design Phase Structure
  □ Break into 3-6 phases
  □ Identify parallel opportunities
  □ Define convergence points

□ Step 3: Select and Configure Agents
  □ Map agents to phases
  □ Write detailed prompts
  □ Define expected outputs
  □ Configure context passing

□ Step 4: Add Validation and Error Handling
  □ Add phase gates
  □ Define success criteria
  □ Create rollback procedures

□ Step 5: Validate and Document
  □ Add configuration options
  □ Write coordination notes
  □ Score against quality rubric (target: 75/100)
```

---

## Step 1: Define Workflow Scope

**Goal:** Clearly define what the command does and when to use it.

### 1.1 Identify Workflow Objective

Write a clear statement of what the command accomplishes:

```markdown
## Command Objective

[Command Name] orchestrates [workflow type] by coordinating
[agent types] to deliver [output/outcome] for [target/input].
```

**Examples:**
- "Full-stack-feature orchestrates feature development by coordinating backend, frontend, and database agents to deliver production-ready code for feature requests."
- "Security-hardening orchestrates security improvements by coordinating security, backend, and deployment agents to deliver hardened systems for vulnerable applications."

### 1.2 Map Inputs and Outputs

Define what the command receives and produces:

**Input Mapping:**
```markdown
## Inputs
- `$ARGUMENTS`: [Primary input - what the command acts on]
- `$CONFIG`: [Optional configuration parameters]

Example inputs:
- "/full-stack-feature implement user authentication with OAuth2"
- "/security-hardening scan and harden the payment service"
```

**Output Mapping:**
```markdown
## Outputs
- [Primary deliverable - code, reports, configurations]
- [Secondary artifacts - documentation, test results]
- [Validation reports - security scans, coverage reports]
```

### 1.3 Determine Command Category

Select the appropriate category based on primary function:

| Category | Description | Example Commands |
|----------|-------------|------------------|
| `orchestration/` | Complex multi-agent workflows | full-stack-feature, context-save |
| `security/` | Security scanning and hardening | security-hardening, compliance-check |
| `testing/` | Test generation and TDD | tdd-cycle, test-generate |
| `devops/` | Infrastructure and CI/CD | monitor-setup, workflow-automate |
| `troubleshooting/` | Debugging and incident response | incident-response, smart-fix |
| `code-quality/` | Review and refactoring | ai-review, refactor-clean |
| `framework-migration/` | Upgrades and migrations | legacy-modernize, deps-upgrade |
| `git-workflows/` | Git operations and PRs | git-workflow, pr-enhance |
| `performance/` | Performance analysis | performance-optimization |
| `documentation/` | Documentation generation | doc-generate |
| `deployment/` | Deployment and config | config-validate |
| `database/` | Database operations | cost-optimize |
| `architecture/` | Architecture design | c4-architecture |
| `accessibility/` | Accessibility compliance | accessibility-audit |
| `other/` | Miscellaneous commands | Various |

### Step 1 Output

```markdown
# [Command Name]

[One-line description of what the command does]

[Extended thinking: Explanation of the methodology, approach,
and key design decisions. 3-5 sentences explaining why this
workflow is structured this way and what principles it follows.]

## Inputs
- `$ARGUMENTS`: [Description]

## Outputs
- [Primary deliverable]
- [Secondary artifacts]
```

---

## Step 2: Design Phase Structure

**Goal:** Break the workflow into logical phases with clear handoffs.

### 2.1 Identify Phase Boundaries

Most commands follow this general structure:

```
Phase 1: Assessment/Planning (understand the problem)
Phase 2: Implementation (do the work)
Phase 3: Validation/Testing (verify the work)
Phase 4: Deployment/Completion (deliver the work)
```

**Guidelines:**
- Use 3-6 phases (most commands use 4)
- Each phase should have a clear purpose
- Name phases descriptively

### 2.2 Map Phase Dependencies

Determine how phases relate:

```
Sequential: Phase 1 → Phase 2 → Phase 3 → Phase 4
            (each phase depends on previous)

Parallel within phases:
Phase 1 → Phase 2 (Steps 4, 5, 6 parallel) → Phase 3 → Phase 4
          ↓
     Backend ─────┐
     Frontend ────┼─→ Convergence → Integration
     Database ────┘
```

### 2.3 Define Steps Within Phases

Each phase contains numbered steps:

```markdown
## Phase 1: Assessment and Planning

### 1. Requirements Analysis
[Agent invocation details]

### 2. Architecture Design
[Agent invocation details]

## Phase 2: Implementation

### 3. Backend Implementation
[Agent invocation details]

### 4. Frontend Implementation (PARALLEL)
[Agent invocation details]

### 5. Database Implementation (PARALLEL)
[Agent invocation details]

---
### CONVERGENCE: Steps 3-5 must complete before Phase 3
---

## Phase 3: Validation
...
```

### Step 2 Patterns

Reference these patterns from `COMMAND_PATTERN_INDEX.md`:

| Pattern | Code | Use When |
|---------|------|----------|
| Multi-Phase Sequential | OP-01 | Always (required) |
| Parallel Agent Execution | OP-02 | Independent tasks within phase |
| Context Passing Chain | OP-03 | Sequential dependencies |
| Milestone Convergence | OP-05 | After parallel work |

### Step 2 Output

Add phase structure to your command:

```markdown
## Phase 1: [Phase Name]

### 1. [Step Name]
- Use Task tool with subagent_type="[agent]"
- Prompt: "[instructions]"
- Expected output: [deliverables]

### 2. [Step Name]
- Use Task tool with subagent_type="[agent]"
- Prompt: "[instructions]"
- Context from previous: [what context needed]
- Expected output: [deliverables]

## Phase 2: [Phase Name]
...
```

---

## Step 3: Select and Configure Agents

**Goal:** Choose appropriate agents and configure their invocations.

### 3.1 Map Agents to Steps

Select the most appropriate agent for each step:

| Task Type | Recommended Agent | Composite Path |
|-----------|------------------|----------------|
| Architecture design | backend-architect | `backend-development::backend-architect` |
| Python implementation | python-pro | `python-development::python-pro` |
| Frontend development | frontend-developer | `frontend-mobile-development::frontend-developer` |
| Test automation | test-automator | `unit-testing::test-automator` |
| Security audit | security-auditor | `security-scanning::security-auditor` |
| DevOps/deployment | deployment-engineer | `deployment-strategies::deployment-engineer` |
| Database design | database-architect | `database-design::database-architect` |
| Performance analysis | performance-engineer | `application-performance::performance-engineer` |
| Incident response | incident-responder | `incident-response::incident-responder` |
| Documentation | docs-architect | `documentation-generation::docs-architect` |
| Code review | code-reviewer | `comprehensive-review::code-reviewer` |
| Observability | observability-engineer | `observability-monitoring::observability-engineer` |
| Legacy modernization | legacy-modernizer | `legacy-modernizer` |
| Business analysis | business-analyst | `business-analytics::business-analyst` |

### 3.2 Write Detailed Prompts

Use this structure for agent prompts:

```markdown
- Prompt: "[ACTION VERB] [TARGET] for: $ARGUMENTS.

  [SPECIFIC REQUIREMENTS - numbered list]:
  1) [First requirement]
  2) [Second requirement]
  3) [Third requirement]

  [OUTPUT SPECIFICATION]:
  Generate [output type] including:
  - [Output component 1]
  - [Output component 2]

  [CONSTRAINTS/CONTEXT]:
  Consider [relevant constraints].
  Reference [previous outputs] for context."
```

**Example Prompt:**
```markdown
- Prompt: "Perform comprehensive security assessment on: $ARGUMENTS.

  Execute the following analyses:
  1) SAST analysis with Semgrep/SonarQube
  2) DAST scanning with OWASP ZAP
  3) Dependency audit with Snyk/Trivy
  4) Secrets detection with GitLeaks/TruffleHog

  Generate detailed vulnerability report including:
  - CVSS scores for each finding
  - Exploitability analysis
  - Attack surface mapping
  - Prioritized remediation steps

  Consider OWASP Top 10, CWE weaknesses, and CVE exposures.
  Reference the architecture documentation for context."
```

### 3.3 Define Expected Outputs

Specify what each agent should produce:

```markdown
- Expected output: [Format] with [components]

Examples:
- Expected output: Detailed vulnerability report with CVSS scores,
  exploitability analysis, attack surface mapping

- Expected output: JSON with structure:
  {
    "issues": [],
    "summary": {"critical": 0, "high": 0, "medium": 0, "low": 0},
    "recommendations": []
  }

- Expected output:
  1. Architecture diagrams
  2. API specifications
  3. Database schema
  4. Security requirements
```

### 3.4 Configure Context Passing

Specify what context each step needs from previous steps:

```markdown
### 2. Architecture Design
- Use Task tool with subagent_type="backend-architect"
- Prompt: "Design backend architecture..."
- **Context from previous:** Requirements specification from Step 1
- Expected output: Architecture design

### 3. Implementation Planning
- Use Task tool with subagent_type="planner"
- Prompt: "Create implementation plan..."
- **Context from previous:**
  - Requirements specification from Step 1
  - Architecture design from Step 2
- Expected output: Implementation roadmap
```

### Step 3 Patterns

Reference these patterns from `COMMAND_PATTERN_INDEX.md`:

| Pattern | Code | Use When |
|---------|------|----------|
| Task Tool Invocation | AIP-01 | All agent calls |
| Composite Agent Paths | AIP-02 | Precise specialization needed |
| Detailed Prompt Engineering | AIP-03 | Complex requirements |
| Output Specification | AIP-04 | Always |
| Conditional Agent Selection | AIP-05 | Technology-agnostic commands |

### Step 3 Output

Complete the agent invocations:

```markdown
### 1. Security Vulnerability Scanning
- Use Task tool with subagent_type="security-scanning::security-auditor"
- Prompt: "Perform comprehensive security assessment on: $ARGUMENTS.
  Execute SAST analysis, DAST scanning, dependency audit, and
  secrets detection. Generate SBOM for supply chain analysis.
  Identify OWASP Top 10 vulnerabilities, CWE weaknesses, and
  CVE exposures."
- Expected output: Detailed vulnerability report with CVSS scores,
  exploitability analysis, attack surface mapping, secrets exposure
- Context: Initial baseline for all remediation efforts
```

---

## Step 4: Add Validation and Error Handling

**Goal:** Ensure quality through gates, criteria, and recovery procedures.

### 4.1 Add Phase Gates

Insert validation checkpoints between phases:

```markdown
### 4. Verify Test Failure
- Use Task tool with subagent_type="code-reviewer"
- Prompt: "Verify all tests fail correctly..."
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

### 4.2 Define Success Criteria

List explicit, measurable success criteria:

```markdown
## Success Criteria

### Technical Criteria
- ✅ All API contracts validated through contract tests
- ✅ Test coverage exceeds 80% line coverage
- ✅ No critical security vulnerabilities (CVSS 7+)
- ✅ Performance metrics within SLO thresholds
- ✅ All integration tests passing

### Process Criteria
- ✅ Documentation complete for all components
- ✅ Code review completed with no blocking issues
- ✅ CI/CD pipeline configured with quality gates
- ✅ Rollback procedures documented and tested

### Operational Criteria
- ✅ Monitoring and alerting configured
- ✅ Runbooks created for common scenarios
- ✅ On-call team briefed on changes
```

### 4.3 Create Rollback Procedures

Document recovery steps for failures:

```markdown
## Rollback Procedures

### In Case of Deployment Failure
1. **Immediate Rollback**
   ```bash
   kubectl rollout undo deployment/[name]
   ```

2. **Feature Flag Disable**
   - Disable flag in LaunchDarkly
   - Verify traffic routed to previous version

3. **Database Rollback** (if applicable)
   ```bash
   ./scripts/rollback-migration.sh [version]
   ```

4. **Communication**
   - Post in #incidents channel
   - Update status page
   - Notify stakeholders

5. **Root Cause Analysis**
   - Document in postmortem template
   - Schedule review within 48 hours
```

### 4.4 Add Error Handling

Define how to handle failures at each phase:

```markdown
## Error Handling

### If Security Scan Fails
1. Categorize findings by severity
2. Block deployment for CRITICAL/HIGH
3. Generate remediation report
4. Re-run scan after fixes

### If Tests Fail
1. Identify failing tests
2. Analyze root cause
3. Fix and re-run
4. Document any test modifications

### If Deployment Fails
1. Automatic rollback triggered
2. Capture deployment logs
3. Identify failure point
4. Fix and retry OR escalate
```

### Step 4 Patterns

Reference these patterns from `COMMAND_PATTERN_INDEX.md`:

| Pattern | Code | Use When |
|---------|------|----------|
| Phase Gate Validation | VP-01 | Between major phases |
| Severity Classification | VP-02 | Issue identification |
| Threshold Validation | VP-03 | Numeric requirements |
| Checkpoint Matrix | VP-04 | Complex validation |
| Rollback Procedures | EHP-01 | All deployment commands |
| Failure Recovery | EHP-02 | Multi-phase workflows |
| Graceful Degradation | EHP-03 | Resilient operations |
| Error Escalation | EHP-04 | Critical failures |

---

## Step 5: Validate and Document

**Goal:** Add configuration options, documentation, and validate quality.

### 5.1 Add Configuration Options

Define configurable parameters:

```markdown
## Configuration

### Flags
- `--skip-tests`: Skip test execution phase
- `--draft-pr`: Create PR as draft
- `--quick`: Use quick mode (reduced validation)
- `--comprehensive`: Use comprehensive mode (full validation)

### Parameters
- `stack`: Technology stack (e.g., "React/FastAPI/PostgreSQL")
- `deployment_target`: Cloud platform (AWS/GCP/Azure)
- `coverage_threshold`: Minimum test coverage (default: 80%)

### Modes
- `quick`: Fast execution, essential checks only
- `standard`: Balanced execution (default)
- `comprehensive`: Full execution, all checks
```

### 5.2 Write Coordination Notes

Document how agents work together:

```markdown
## Coordination Notes

- Each phase builds upon outputs from previous phases
- Parallel tasks in Phase 2 can run simultaneously but must
  converge for Phase 3
- Maintain traceability between requirements and implementations
- Use correlation IDs across all services for distributed tracing
- Document all architectural decisions in ADRs
- Ensure consistent error handling across services
- Security-auditor coordinates with domain agents for fixes
```

### 5.3 Add Extended Thinking

Add reasoning context at the command start:

```markdown
[Extended thinking: This workflow coordinates multiple specialized
agents to deliver [outcome]. It follows [methodology/approach],
ensuring [key principle]. Each phase builds upon previous outputs,
creating [result] with [quality attributes]. The workflow emphasizes
[important aspects] and ensures [guarantees].]
```

### 5.4 Validate Quality

Score your command against `COMMAND_QUALITY_RUBRIC.md`:

**Target Score: 75/100**

Quick validation checklist:
- [ ] Clear workflow objective (5 pts)
- [ ] Appropriate phase structure (10 pts)
- [ ] Correct agent selection (10 pts)
- [ ] Detailed prompts (15 pts)
- [ ] Output specifications (10 pts)
- [ ] Context passing configured (10 pts)
- [ ] Phase gates defined (10 pts)
- [ ] Success criteria listed (10 pts)
- [ ] Error handling documented (10 pts)
- [ ] Configuration options available (5 pts)
- [ ] Coordination notes included (5 pts)

### Step 5 Patterns

Reference these patterns from `COMMAND_PATTERN_INDEX.md`:

| Pattern | Code | Use When |
|---------|------|----------|
| Extended Thinking | WP-01 | All commands |
| Configuration Block | WP-02 | Configurable commands |
| Success Criteria | WP-03 | Always (required) |
| Coordination Notes | WP-04 | Multi-agent workflows |
| Input Arguments | WP-05 | All commands |
| Reference Documentation | WP-06 | Complex workflows |
| Flag Configuration | CP-01 | Boolean options |
| Parameter Configuration | CP-02 | Variable values |
| Threshold Configuration | CP-03 | Quality gates |
| Mode Selection | CP-04 | Different approaches |

---

## Templates

### Minimal Command Template

```markdown
# [Command Name]

[One-line description]

[Extended thinking: Brief explanation of approach and methodology.]

## Phase 1: [Assessment/Planning]

### 1. [Initial Analysis]
- Use Task tool with subagent_type="[agent]"
- Prompt: "[Detailed instructions for: $ARGUMENTS]"
- Expected output: [Deliverables]

## Phase 2: [Implementation]

### 2. [Core Implementation]
- Use Task tool with subagent_type="[agent]"
- Prompt: "[Instructions]"
- Context from previous: [Step 1 outputs]
- Expected output: [Deliverables]

## Phase 3: [Validation]

### 3. [Verification]
- Use Task tool with subagent_type="[agent]"
- Prompt: "[Instructions]"
- Context from previous: [Steps 1-2 outputs]
- Expected output: [Validation report]

## Success Criteria

- ✅ [Criterion 1]
- ✅ [Criterion 2]
- ✅ [Criterion 3]

Target: $ARGUMENTS
```

### Full Command Template

```markdown
# [Command Name]

[One-line description of what this command orchestrates]

[Extended thinking: Comprehensive explanation of the methodology,
approach, and key design decisions. Explain why this workflow is
structured this way and what principles it follows. 3-5 sentences.]

## Configuration

### Supported Flags
- `--flag1`: [Description]
- `--flag2`: [Description]

### Parameters
- `param1`: [Description] (default: [value])
- `param2`: [Description] (values: [options])

## Phase 1: [Phase Name]

### 1. [Step Name]
- Use Task tool with subagent_type="[category::agent]"
- Prompt: "[Action verb] [target] for: $ARGUMENTS.

  [Requirements]:
  1) [Requirement 1]
  2) [Requirement 2]
  3) [Requirement 3]

  [Output specification]:
  Generate [output type] including [components].

  [Constraints/context]."
- Expected output: [Detailed deliverables]
- Context: [Initial context]

### 2. [Step Name]
- Use Task tool with subagent_type="[category::agent]"
- Prompt: "[Instructions]"
- Context from previous: [Step 1 outputs]
- Expected output: [Deliverables]

## Phase 2: [Phase Name]

### 3. [Step Name]
- Use Task tool with subagent_type="[agent]"
- Prompt: "[Instructions]"
- Context from previous: [Previous outputs]
- Expected output: [Deliverables]

### 4. [Step Name] (PARALLEL)
- Use Task tool with subagent_type="[agent]"
- Prompt: "[Instructions]"
- Expected output: [Deliverables]

### 5. [Step Name] (PARALLEL)
- Use Task tool with subagent_type="[agent]"
- Prompt: "[Instructions]"
- Expected output: [Deliverables]

---
### CONVERGENCE: Steps 3-5 must complete before Phase 3
---

## Phase 3: [Phase Name]

### 6. [Step Name]
- Use Task tool with subagent_type="[agent]"
- Prompt: "[Instructions]"
- Context from previous: [All Phase 2 outputs]
- Expected output: [Deliverables]
- **GATE**: [Validation condition before proceeding]

## Phase 4: [Phase Name]

### 7. [Final Step]
- Use Task tool with subagent_type="[agent]"
- Prompt: "[Instructions]"
- Context from previous: [All previous outputs]
- Expected output: [Final deliverables]

## Success Criteria

### Technical Criteria
- ✅ [Criterion 1]
- ✅ [Criterion 2]

### Process Criteria
- ✅ [Criterion 3]
- ✅ [Criterion 4]

### Operational Criteria
- ✅ [Criterion 5]
- ✅ [Criterion 6]

## Rollback Procedures

### In Case of [Failure Type]
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Coordination Notes

- [Note 1]
- [Note 2]
- [Note 3]

Target: $ARGUMENTS
```

---

## Common Mistakes

### ❌ Mistakes to Avoid

1. **Too Few Phases**
   - Wrong: 2 phases for complex workflow
   - Right: 4-6 phases with clear boundaries

2. **Vague Prompts**
   - Wrong: "Review the code"
   - Right: "Review code for security vulnerabilities including SQL injection, XSS, and authentication bypass. Generate report with CVSS scores and remediation steps."

3. **Missing Context Passing**
   - Wrong: No context specified between steps
   - Right: Explicit "Context from previous: [specific outputs]"

4. **No Validation Gates**
   - Wrong: Linear workflow without checkpoints
   - Right: Gates between phases with clear conditions

5. **Generic Agent Selection**
   - Wrong: Always using "backend-architect"
   - Right: Using "security-scanning::security-auditor" for security tasks

6. **Missing Success Criteria**
   - Wrong: No defined success metrics
   - Right: Explicit, measurable success criteria

7. **No Error Handling**
   - Wrong: No rollback or recovery procedures
   - Right: Documented recovery for each failure type

8. **Monolithic Phases**
   - Wrong: One phase with 15 steps
   - Right: Multiple phases with 2-4 steps each

9. **Missing Output Specifications**
   - Wrong: "Expected output: Report"
   - Right: "Expected output: Security report with CVSS scores, exploitability analysis, and prioritized remediation steps"

10. **No Configuration Options**
    - Wrong: Hardcoded values throughout
    - Right: Configurable thresholds and modes

---

## Examples

### Example 1: Simple Security Scan Command

```markdown
# Security Scan

Orchestrate a basic security scan of the codebase.

[Extended thinking: This workflow performs essential security
checks using SAST and dependency scanning. It's designed for
quick validation before commits or PRs.]

## Phase 1: Analysis

### 1. Static Analysis
- Use Task tool with subagent_type="security-scanning::security-auditor"
- Prompt: "Perform SAST analysis on: $ARGUMENTS.
  Check for OWASP Top 10 vulnerabilities.
  Generate report with severity classifications."
- Expected output: SAST report with findings

### 2. Dependency Scan
- Use Task tool with subagent_type="security-scanning::security-auditor"
- Prompt: "Scan dependencies for known vulnerabilities.
  Check CVE databases. Identify outdated packages."
- Context from previous: SAST findings
- Expected output: Dependency vulnerability report

## Phase 2: Reporting

### 3. Generate Summary
- Use Task tool with subagent_type="documentation-generation::docs-architect"
- Prompt: "Create security summary report combining SAST
  and dependency findings. Prioritize by severity."
- Context from previous: Both reports from Phase 1
- Expected output: Consolidated security report

## Success Criteria

- ✅ No critical vulnerabilities (CVSS 9+)
- ✅ No high vulnerabilities in dependencies
- ✅ All findings documented with remediation steps

Target: $ARGUMENTS
```

### Example 2: Complex Migration Command

See [`full_stack_feature.md`](../../../domain-agentic-resources/commands/orchestration/full_stack_feature.md) for a multi-agent orchestration example.

---

## Quick Reference

### 5-Step Process Summary

| Step | Goal | Key Actions |
|------|------|-------------|
| 1 | Define Scope | Objective, inputs, outputs, category |
| 2 | Design Phases | 3-6 phases, dependencies, convergence |
| 3 | Configure Agents | Select agents, write prompts, outputs |
| 4 | Add Validation | Gates, criteria, rollback, error handling |
| 5 | Document | Configuration, coordination, extended thinking |

### Essential Patterns

| Pattern | Code | Required? |
|---------|------|-----------|
| Multi-Phase Sequential | OP-01 | ✅ Yes |
| Context Passing | OP-03 | ✅ Yes |
| Task Tool Invocation | AIP-01 | ✅ Yes |
| Output Specification | AIP-04 | ✅ Yes |
| Success Criteria | WP-03 | ✅ Yes |
| Phase Gates | VP-01 | ✅ Yes |
| Rollback Procedures | EHP-01 | Recommended |
| Extended Thinking | WP-01 | Recommended |
| Configuration | WP-02 | Recommended |

### File Naming Convention

```
commands/[category]/[action]-[target].md

Examples:
- commands/security/security-hardening.md
- commands/testing/tdd-cycle.md
- commands/orchestration/full-stack-feature.md
- commands/git-workflows/git-workflow.md
```

---

## Related Resources

- **[COMMAND_PATTERN_INDEX.md](COMMAND_PATTERN_INDEX.md)** - Complete pattern reference
- **[COMMAND_USE_CASE_LOOKUP.md](COMMAND_USE_CASE_LOOKUP.md)** - Find patterns by use case
- **[COMMAND_QUALITY_RUBRIC.md](COMMAND_QUALITY_RUBRIC.md)** - Quality scoring (target: 75/100)
- **Agents** - Available agents
- **Commands** - Existing commands index

---

**Document End**

**Next Step:** Use this guide to create your command, then validate with COMMAND_QUALITY_RUBRIC.md
