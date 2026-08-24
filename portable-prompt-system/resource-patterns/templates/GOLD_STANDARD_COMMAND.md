# Gold Standard Command Template

**Purpose:** Fully annotated example demonstrating all best practices
**Quality Score:** 92/100 (Exemplary tier)
**Use:** Study this example, then adapt patterns for your commands

---

## About This Template

This template shows a production-ready command with annotations explaining:
- Why each section exists
- Which patterns are being used
- Common variations
- What to customize

**Annotations use this format:**
```
<!-- ANNOTATION: Explanation of the element -->
```

**Pattern references use this format:**
```
<!-- PATTERN: [Code] - Pattern Name -->
```

---

# API Migration Command

<!--
ANNOTATION: Command title should be clear and action-oriented
Format: [Action] [Target] or [Domain] [Action]
Examples: API Migration, Security Hardening, Full-Stack Feature
-->

Orchestrate a comprehensive API migration from legacy endpoints to modern RESTful/GraphQL APIs with zero-downtime transition, automated testing, and gradual traffic shifting.

<!--
ANNOTATION: One-line description immediately after title
- States what the command orchestrates
- Includes key outcomes (zero-downtime, automated testing)
- Gives context for scope (legacy to modern)
-->

<!-- PATTERN: WP-01 - Extended Thinking Introduction -->
[Extended thinking: This workflow implements a strangler fig pattern for API migration, gradually routing traffic from legacy endpoints to new implementations. The approach ensures continuous operation during migration while providing comprehensive testing at each phase. By coordinating specialized agents for analysis, implementation, testing, and deployment, we minimize risk while maximizing migration velocity. The workflow emphasizes contract testing to prevent breaking changes and uses feature flags for instant rollback capability.]

<!--
ANNOTATION: Extended thinking block
- 3-5 sentences explaining methodology
- Notes key design decisions (strangler fig pattern)
- Highlights important principles (zero-downtime, contract testing)
- Explains coordination approach

SCORING: +4 points in Documentation category
-->

<!-- PATTERN: WP-02 - Configuration Block -->
## Configuration

### Supported Flags
<!-- ANNOTATION: Boolean options that modify behavior -->
- `--dry-run`: Analyze and plan only, no implementation
- `--skip-legacy-tests`: Skip legacy endpoint testing (use with caution)
- `--parallel-migrate`: Migrate multiple endpoints simultaneously
- `--force-cutover`: Skip gradual traffic shifting (high risk)
- `--preserve-legacy`: Keep legacy endpoints after migration
- `--generate-docs`: Auto-generate API documentation

### Parameters
<!-- ANNOTATION: Named parameters with valid values -->
- `api_style`: Target API style
  - Values: `"rest"`, `"graphql"`, `"grpc"`
  - Default: `"rest"`
- `traffic_shift_increment`: Percentage for gradual shifts
  - Values: `5`, `10`, `25`, `50`
  - Default: `10`
- `rollback_threshold`: Error rate triggering rollback
  - Values: `0.1` to `5.0` (percentage)
  - Default: `1.0`
- `compatibility_mode`: Backward compatibility level
  - Values: `"strict"`, `"relaxed"`, `"none"`
  - Default: `"strict"`

### Modes
<!-- ANNOTATION: Different operational approaches -->
- `quick`: Essential migration, minimal validation (~2 hours)
- `standard`: Balanced migration with testing (~8 hours, default)
- `comprehensive`: Full migration with extensive validation (~24 hours)

<!--
ANNOTATION: Configuration section provides:
- Flags for boolean options (6 flags)
- Parameters for variable values (4 parameters)
- Modes for different approaches (3 modes)

SCORING: +10 points in Configuration category
-->

---

<!-- PATTERN: OP-01 - Multi-Phase Sequential -->
## Phase 1: Discovery and Analysis

<!--
ANNOTATION: Phase naming convention
- Descriptive name (not "Phase 1")
- Indicates purpose (Discovery and Analysis)
- Helps readers understand what happens here
-->

### 1. Legacy API Inventory
<!-- PATTERN: AIP-01 - Task Tool Invocation -->
<!-- PATTERN: AIP-02 - Composite Agent Paths -->
- Use Task tool with subagent_type="backend-development::backend-architect"
<!--
ANNOTATION: Agent selection
- Uses composite path for specialization
- backend-development = category
- backend-architect = specialist
-->

<!-- PATTERN: AIP-03 - Detailed Prompt Engineering -->
- Prompt: "Analyze and inventory all legacy API endpoints for: $ARGUMENTS.

  Document the following for each endpoint:
  1) HTTP method and path pattern
  2) Request/response schemas with data types
  3) Authentication and authorization requirements
  4) Rate limiting and throttling configuration
  5) Downstream dependencies and integrations
  6) Current traffic volume and patterns
  7) Known issues or technical debt

  Generate comprehensive inventory including:
  - Endpoint catalog with full specifications
  - Dependency graph showing service relationships
  - Traffic analysis with peak usage patterns
  - Risk assessment for each endpoint migration

  Consider backward compatibility requirements and identify
  breaking change risks."

<!--
ANNOTATION: Prompt structure
- Starts with action verb (Analyze)
- References $ARGUMENTS
- Has numbered requirements (7 items)
- Specifies output format (4 deliverables)
- Notes constraints (backward compatibility)
-->

<!-- PATTERN: AIP-04 - Output Specification -->
- Expected output:
  - Complete endpoint catalog (JSON schema)
  - Service dependency graph (Mermaid diagram)
  - Traffic analysis report
  - Migration risk matrix with scores (1-10)
- Context: Initial discovery, no prior context needed

<!--
ANNOTATION: Output specification
- Lists all expected deliverables
- Specifies format where relevant (JSON, Mermaid)
- Notes context requirements
-->

---

### 2. Contract Analysis and Specification
- Use Task tool with subagent_type="backend-development::backend-architect"
- Prompt: "Create formal API contracts for legacy endpoints in: $ARGUMENTS.

  For each endpoint from the inventory:
  1) Generate OpenAPI 3.0 specification
  2) Define JSON Schema for request/response bodies
  3) Document error response formats
  4) Specify header requirements
  5) Create example requests and responses

  Validate contracts against actual endpoint behavior.
  Identify undocumented behaviors and edge cases."

<!-- PATTERN: OP-03 - Context Passing Chain -->
- Expected output:
  - OpenAPI specification file
  - JSON Schema definitions
  - Contract validation report
  - Edge case documentation
- Context from previous: Endpoint catalog from Step 1

<!--
ANNOTATION: Context passing
- Explicitly references output from Step 1
- Creates chain of dependent information
- Allows agent to build on previous work

SCORING: +6 points in Workflow Structure category
-->

---

### 3. Migration Strategy Design
- Use Task tool with subagent_type="comprehensive-review::architect-review"
- Prompt: "Design migration strategy for API endpoints in: $ARGUMENTS.

  Using the endpoint inventory and contracts:
  1) Prioritize endpoints by risk and business impact
  2) Group endpoints for batch migration
  3) Define traffic shifting strategy per endpoint
  4) Plan rollback procedures for each group
  5) Design monitoring and alerting requirements
  6) Create timeline with milestones

  Consider dependencies between endpoints and ensure
  migration order respects service relationships."

- Expected output:
  - Prioritized migration roadmap
  - Endpoint grouping with rationale
  - Traffic shifting plan
  - Rollback playbook
  - Monitoring requirements
- Context from previous:
  - Endpoint catalog from Step 1
  - API contracts from Step 2

---

<!-- PATTERN: VP-01 - Phase Gate Validation -->
### PHASE GATE: Phase 1 → Phase 2

Before proceeding to Implementation:
- [ ] All endpoints inventoried and cataloged
- [ ] Contracts validated against actual behavior
- [ ] Migration strategy approved
- [ ] Rollback procedures documented
- [ ] Monitoring requirements defined

**GATE**: Do not proceed until strategy review complete

<!--
ANNOTATION: Phase gate
- Explicit checkpoint between phases
- Checklist of required completions
- Clear blocking condition

SCORING: +6 points in Validation category
-->

---

## Phase 2: New API Implementation

### 4. API Schema and Types
- Use Task tool with subagent_type="backend-development::backend-architect"
- Prompt: "Design new API schema and types for: $ARGUMENTS.

  Based on migration strategy and legacy contracts:
  1) Design modern RESTful/GraphQL schema
  2) Define TypeScript/Python type definitions
  3) Create validation schemas (Zod/Pydantic)
  4) Design pagination and filtering patterns
  5) Plan versioning strategy (URL/header based)

  Ensure new schema supports all legacy functionality
  while improving developer experience."

- Expected output:
  - New API schema design
  - Type definitions (TypeScript/Python)
  - Validation schemas
  - Versioning strategy document
- Context from previous: API contracts from Step 2

---

<!-- PATTERN: OP-02 - Parallel Agent Execution -->
### 5. Backend Implementation (PARALLEL)
- Use Task tool with subagent_type="python-development::python-pro"
  (or `"golang-pro"` / `"nodejs-expert"` based on stack)

<!-- PATTERN: AIP-05 - Conditional Agent Selection -->
<!--
ANNOTATION: Conditional selection
- Notes stack-dependent agent choice
- Provides alternatives
- Allows technology-agnostic command
-->

- Prompt: "Implement new API endpoints for: $ARGUMENTS.

  Using the new schema design:
  1) Create endpoint handlers with proper routing
  2) Implement request validation
  3) Add authentication/authorization middleware
  4) Implement business logic with proper error handling
  5) Add structured logging and metrics
  6) Write unit tests with >80% coverage

  Follow 12-factor app principles and ensure
  observability is built in from the start."

- Expected output:
  - Endpoint implementation code
  - Middleware implementations
  - Unit test suite
  - Logging and metrics setup
- Context from previous: New API schema from Step 4

---

### 6. Contract Test Implementation (PARALLEL)
- Use Task tool with subagent_type="unit-testing::test-automator"
- Prompt: "Create contract tests for new API endpoints in: $ARGUMENTS.

  Using legacy contracts as baseline:
  1) Implement Pact/Dredd contract tests
  2) Create request/response validators
  3) Test all documented edge cases
  4) Verify backward compatibility
  5) Generate test coverage report

  Ensure 100% contract coverage for all endpoints."

- Expected output:
  - Contract test suite
  - Compatibility validation report
  - Test coverage report
- Context from previous:
  - API contracts from Step 2
  - New implementation from Step 5

---

### 7. Documentation Generation (PARALLEL)
- Use Task tool with subagent_type="documentation-generation::docs-architect"
- Prompt: "Generate comprehensive API documentation for: $ARGUMENTS.

  Create documentation including:
  1) OpenAPI/Swagger specification
  2) Interactive API explorer (Redoc/Swagger UI)
  3) Migration guide for consumers
  4) Code examples in multiple languages
  5) Changelog from legacy to new API

  Ensure documentation is developer-friendly and
  includes all edge cases and error scenarios."

- Expected output:
  - OpenAPI specification
  - Interactive documentation
  - Migration guide
  - Code examples
  - Changelog
- Context from previous: New API schema from Step 4

---

<!-- PATTERN: OP-05 - Milestone Convergence -->
### CONVERGENCE CHECKPOINT

Steps 5, 6, and 7 can run in parallel but must complete before Phase 3:
- [ ] Backend implementation complete with tests
- [ ] Contract tests passing
- [ ] Documentation generated

<!--
ANNOTATION: Convergence point
- Explicitly marks where parallel work must complete
- Lists required completions
- Blocks Phase 3 until all ready

SCORING: +3 points in Validation category
-->

---

## Phase 3: Integration and Testing

### 8. Integration Testing
- Use Task tool with subagent_type="unit-testing::test-automator"
- Prompt: "Execute comprehensive integration testing for: $ARGUMENTS.

  Test the following scenarios:
  1) End-to-end request flows
  2) Authentication and authorization
  3) Rate limiting and throttling
  4) Error handling and recovery
  5) Performance under load
  6) Timeout and retry behavior

  Compare behavior with legacy endpoints to ensure
  functional parity."

- Expected output:
  - Integration test suite
  - Performance benchmarks
  - Legacy comparison report
  - Issues and gaps identified
- Context from previous: All Phase 2 outputs
- **GATE**: Block if critical issues found

---

### 9. Security Audit
- Use Task tool with subagent_type="security-scanning::security-auditor"
- Prompt: "Perform security audit on new API implementation for: $ARGUMENTS.

  Assess the following:
  1) OWASP API Security Top 10 compliance
  2) Authentication and authorization implementation
  3) Input validation and sanitization
  4) Rate limiting and DDoS protection
  5) Data exposure and information leakage
  6) Injection vulnerabilities

  Generate remediation plan for any findings."

<!-- PATTERN: VP-02 - Severity-Based Classification -->
- Expected output:
  - Security audit report with CVSS scores
  - Vulnerability findings (Critical/High/Medium/Low)
  - Remediation plan
  - Compliance checklist
- Context from previous: Backend implementation from Step 5
- **GATE**: Block deployment if Critical or High findings

<!--
ANNOTATION: Severity classification
- Findings categorized by severity
- Clear blocking conditions based on severity
- Enables risk-based decision making
-->

---

### 10. Load Testing
- Use Task tool with subagent_type="application-performance::performance-engineer"
- Prompt: "Conduct load testing for new API endpoints in: $ARGUMENTS.

  Test scenarios:
  1) Baseline performance under normal load
  2) Peak traffic simulation
  3) Sustained high load
  4) Burst traffic patterns
  5) Degradation behavior under overload

  Compare with legacy endpoint performance baselines."

<!-- PATTERN: VP-03 - Threshold-Based Validation -->
- Expected output:
  - Load test results
  - Performance comparison report
  - Capacity recommendations
  - Bottleneck analysis
- Context from previous:
  - Traffic analysis from Step 1
  - Backend implementation from Step 5
- **GATE**: Verify P95 latency within 110% of legacy baseline

<!--
ANNOTATION: Threshold validation
- Specific numeric threshold (110% of baseline)
- Clear pass/fail criteria
- Prevents performance regressions
-->

---

## Phase 4: Deployment and Migration

### 11. Infrastructure Setup
- Use Task tool with subagent_type="deployment-strategies::deployment-engineer"
- Prompt: "Configure deployment infrastructure for: $ARGUMENTS.

  Set up the following:
  1) API gateway configuration with routing rules
  2) Feature flags for traffic control
  3) Blue-green deployment configuration
  4) Monitoring and alerting dashboards
  5) Logging and tracing integration
  6) Auto-scaling policies

  Ensure infrastructure supports gradual traffic shifting
  and instant rollback."

- Expected output:
  - API gateway configuration
  - Feature flag setup
  - Deployment manifests (K8s/Docker)
  - Monitoring dashboards
  - Auto-scaling policies
- Context from previous: All implementation and test results

---

### 12. Gradual Traffic Migration
- Use Task tool with subagent_type="deployment-strategies::deployment-engineer"
- Prompt: "Execute gradual traffic migration for: $ARGUMENTS.

  Migration process:
  1) Deploy new API alongside legacy
  2) Route $TRAFFIC_SHIFT_INCREMENT% traffic to new API
  3) Monitor error rates and latency
  4) If stable, increase traffic percentage
  5) Repeat until 100% on new API
  6) Keep legacy in standby for rollback period

  Implement automatic rollback if error rate exceeds
  $ROLLBACK_THRESHOLD%."

- Expected output:
  - Deployment status report
  - Traffic shifting logs
  - Monitoring metrics
  - Rollback readiness confirmation
- Context from previous: Infrastructure setup from Step 11

---

### 13. Legacy Decommissioning
- Use Task tool with subagent_type="deployment-strategies::deployment-engineer"
- Prompt: "Plan and execute legacy API decommissioning for: $ARGUMENTS.

  Decommissioning steps:
  1) Verify 30+ days at 100% new API traffic
  2) Confirm no legacy traffic
  3) Archive legacy code and documentation
  4) Remove legacy infrastructure
  5) Update DNS and routing
  6) Communicate sunset to consumers

  Document all decommissioned endpoints and
  preserve historical data."

- Expected output:
  - Decommissioning checklist
  - Archive documentation
  - Consumer notification templates
  - Final migration report
- Context from previous: Traffic migration status from Step 12

---

<!-- PATTERN: WP-03 - Success Criteria Definition -->
## Success Criteria

### Technical Criteria
- ✅ All endpoints migrated with 100% contract test coverage
- ✅ Performance within 110% of legacy baseline (P95 latency)
- ✅ Zero critical security vulnerabilities
- ✅ Error rate below 0.1% post-migration
- ✅ All integration tests passing

### Process Criteria
- ✅ Zero-downtime migration achieved
- ✅ Gradual traffic shifting completed without rollbacks
- ✅ Consumer migration guides delivered
- ✅ Documentation complete and published

### Operational Criteria
- ✅ Monitoring and alerting configured
- ✅ Runbooks created for common scenarios
- ✅ On-call team trained on new API
- ✅ Legacy decommissioning plan executed

<!--
ANNOTATION: Success criteria
- Organized by category (Technical, Process, Operational)
- Measurable where possible (110%, 0.1%)
- Covers all aspects of success

SCORING: +6 points in Validation category
-->

---

<!-- PATTERN: EHP-01 - Rollback Procedures -->
## Rollback Procedures

### Immediate Rollback (< 5 minutes)

1. **Feature Flag Rollback**
   ```bash
   # Disable new API traffic
   curl -X POST https://api.flagservice.io/flags/new-api/disable

   # Verify traffic routing
   curl https://api.example.com/health
   ```

2. **API Gateway Rollback**
   ```bash
   # Switch to legacy routing rules
   kubectl apply -f deployments/legacy-routing.yaml

   # Verify routing
   kubectl get virtualservice -o yaml
   ```

### Standard Rollback (< 30 minutes)

1. **Traffic Redistribution**
   - Gradually shift traffic back to legacy (25% increments)
   - Monitor error rates during shift
   - Complete when 100% on legacy

2. **Infrastructure Rollback**
   ```bash
   # Scale down new API
   kubectl scale deployment new-api --replicas=0

   # Verify legacy health
   kubectl get pods -l app=legacy-api
   ```

### Full Rollback (< 2 hours)

1. **Database Rollback** (if applicable)
   ```bash
   ./scripts/rollback-migration.sh --to-version=1.0.0
   ```

2. **State Cleanup**
   - Clear any cached new API responses
   - Reset feature flags to pre-migration state
   - Restore legacy configuration

### Communication Protocol

1. Post in #api-migration channel
2. Update status page
3. Notify affected consumers
4. Schedule postmortem within 48 hours

<!--
ANNOTATION: Rollback procedures
- Multiple tiers (immediate, standard, full)
- Specific commands provided
- Time estimates included
- Communication included

SCORING: +6 points in Error Handling category
-->

---

<!-- PATTERN: EHP-02 - Failure Recovery Workflow -->
## Error Handling

### If Contract Tests Fail
1. Identify failing contracts
2. Compare legacy vs new behavior
3. Fix implementation or update contracts
4. Re-run validation
5. Document any intentional behavior changes

### If Performance Degrades
1. Reduce traffic to new API (50% → 25% → 10%)
2. Analyze performance metrics
3. Identify bottleneck (database, compute, network)
4. Apply targeted optimization
5. Re-test before increasing traffic

### If Security Issues Found
1. **Critical/High**: Block deployment, immediate remediation
2. **Medium**: Track in backlog, fix within 7 days
3. **Low**: Document for future improvement
4. Re-audit after remediation

<!-- PATTERN: EHP-04 - Error Escalation Path -->
### Escalation Path

| Level | Trigger | Action | Contact |
|-------|---------|--------|---------|
| L1 | Error rate > 1% | Auto-rollback to 50% legacy | On-call engineer |
| L2 | Error rate > 5% | Full rollback, incident declared | Team lead |
| L3 | Data integrity issue | War room, all-hands | Engineering manager |

<!--
ANNOTATION: Error handling
- Specific recovery steps per failure type
- Escalation with clear triggers
- Contact information for accountability

SCORING: +9 points in Error Handling category
-->

---

<!-- PATTERN: WP-04 - Coordination Notes Section -->
## Coordination Notes

### Agent Coordination
- Discovery agents provide context for implementation agents
- Testing agents validate implementation agent outputs
- Deployment agents use testing results for go/no-go decisions

### Feedback Loops
- Contract test failures trigger implementation review
- Performance issues trigger optimization cycle
- Security findings block until resolved

### Timing Dependencies
- Phase 2 cannot start until Phase 1 gate passed
- Traffic migration cannot start until all tests pass
- Decommissioning requires 30-day stability period

### Context Accumulation
- Each phase builds on all previous phase outputs
- Maintain single source of truth for migration status
- Document all decisions for postmortem

<!--
ANNOTATION: Coordination notes
- Explains agent interaction
- Notes feedback loops
- Specifies timing dependencies

SCORING: +4 points in Documentation category
-->

---

<!-- PATTERN: WP-06 - Reference Documentation -->
## Reference Workflows

### Workflow 1: Single Endpoint Migration
1. Analyze endpoint (Step 1)
2. Create contract (Step 2)
3. Implement new version (Step 5)
4. Test thoroughly (Steps 8-10)
5. Deploy with 10% traffic
6. Monitor for 24 hours
7. Increase to 100%

### Workflow 2: Batch Migration
1. Complete Phase 1 for all endpoints
2. Group by risk level
3. Migrate low-risk group first
4. Learn and adjust
5. Migrate medium-risk group
6. Migrate high-risk group last

### Anti-Patterns to Avoid

- ❌ Big-bang migration (all at once)
- ❌ Skipping contract tests
- ❌ Ignoring performance comparison
- ❌ No rollback plan
- ❌ Decommissioning too quickly

### Best Practices

- ✅ Start with lowest-risk endpoint
- ✅ Always have rollback ready
- ✅ Monitor extensively during migration
- ✅ Keep legacy available for 30+ days
- ✅ Communicate proactively with consumers

<!--
ANNOTATION: Reference material
- Provides example workflows
- Documents anti-patterns
- Lists best practices

SCORING: +4 points in Documentation category
-->

---

## Metrics and Monitoring

### Key Performance Indicators

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Error Rate | < 0.1% | > 1% |
| P50 Latency | < 50ms | > 100ms |
| P95 Latency | < 200ms | > 500ms |
| P99 Latency | < 500ms | > 1000ms |
| Throughput | > 1000 req/s | < 500 req/s |

### Dashboard Requirements

- Real-time traffic split visualization
- Error rate comparison (new vs legacy)
- Latency percentiles over time
- Request volume by endpoint
- Success rate by consumer

---

Target API migration: $ARGUMENTS

<!--
ANNOTATION: Final target reference
- Always end with $ARGUMENTS usage
- Reminds user what the command acts on
-->

---

## Quality Score Breakdown

This command scores **92/100**:

| Category | Score | Notes |
|----------|-------|-------|
| Workflow Structure | 19/20 | Strong phase organization, clear context flow |
| Agent Configuration | 18/20 | Good agent selection, detailed prompts |
| Validation & Gates | 14/15 | Comprehensive gates and criteria |
| Error Handling | 14/15 | Excellent rollback and escalation |
| Documentation | 14/15 | Thorough documentation |
| Configuration | 9/10 | Good flags and parameters |
| Bonus | 4/5 | Innovative pattern usage, reusable |

### Why This Scores High

1. **Clear Phase Structure** (4 phases, descriptive names)
2. **Explicit Context Passing** (every step references previous)
3. **Detailed Prompts** (action verbs, numbered requirements, outputs)
4. **Multiple Validation Gates** (between each phase)
5. **Comprehensive Error Handling** (tiered rollback, escalation)
6. **Rich Documentation** (extended thinking, coordination, references)
7. **Flexible Configuration** (flags, parameters, modes)

---

## Adapting This Template

### For Security Commands
- Emphasize VP-02 (Severity Classification)
- Add more EHP-04 (Escalation) detail
- Include compliance frameworks in success criteria

### For Testing Commands
- Add VP-05 (Continuous Validation) throughout
- Include WP-06 (Anti-patterns) section
- Add incremental mode in configuration

### For DevOps Commands
- Strengthen EHP-01 (Rollback) procedures
- Add infrastructure-specific configuration
- Include monitoring setup requirements

### For Simpler Commands
- Reduce to 3 phases
- Simplify configuration options
- Keep essential patterns only:
  - OP-01 (Multi-Phase)
  - AIP-01 (Task Invocation)
  - WP-03 (Success Criteria)
  - VP-01 (Phase Gates)
  - EHP-01 (Rollback)

---

## Related Resources

- **[COMMAND_PATTERN_INDEX.md](../command-patterns/COMMAND_PATTERN_INDEX.md)** - All patterns referenced
- **[COMMAND_QUICK_START.md](../command-patterns/COMMAND_QUICK_START.md)** - 5-step creation process
- **[COMMAND_QUALITY_RUBRIC.md](../command-patterns/COMMAND_QUALITY_RUBRIC.md)** - Full scoring criteria
- **[COMMAND_USE_CASE_LOOKUP.md](../command-patterns/COMMAND_USE_CASE_LOOKUP.md)** - Pattern selection

---

**Document End**
