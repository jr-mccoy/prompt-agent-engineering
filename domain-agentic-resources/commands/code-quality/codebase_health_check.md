---
name: codebase_health_check
description: Orchestrate a comprehensive codebase health assessment across security, dependencies, code quality, architecture, and test coverage using multiple specialized agents
version: "1.0.0"
category: code-quality
tags: [audit, code-quality, dependencies, health, security, technical-debt, testing]
agents_used: [tech-debt-reducer, security-auditor, test-automator, backend-architect]
---

Perform a comprehensive health check on the codebase, coordinating specialized agents to assess security posture, dependency health, code quality, architectural integrity, and test coverage. Produce a unified health report with a composite score and prioritized action plan:

[Extended thinking: This command orchestrates multiple specialized agents in a structured sequence to produce a holistic view of codebase health. Phase 1 runs independent assessments in parallel for efficiency. Phase 2 synthesizes findings into a single report with a composite score. The health score uses weighted dimensions because not all problems are equal — a critical CVE matters more than a missing docstring. The output is designed to be actionable: every finding includes severity, location, and a recommended fix.]

## Phase 1: Parallel Assessment (run all tasks concurrently)

### 1. Dependency Health Assessment
- Use Task tool with subagent_type="Bash"
- Prompt: "Analyze the project's dependency manifests. For each detected ecosystem (package.json, requirements.txt, go.mod, Cargo.toml, Gemfile, etc.): (a) count direct vs transitive dependencies, (b) identify outdated packages with `npm outdated --json` / `pip list --outdated --format json` / equivalent, (c) run vulnerability scans with `npm audit --json` / `pip-audit` / equivalent, (d) check for packages with no license or copyleft licenses. Summarize findings as JSON with keys: ecosystem, total_deps, outdated_count, vulnerability_counts (by severity), license_issues."
- Expected output: JSON summary per ecosystem with vulnerability counts, outdated packages, and license flags
- Context: Use the dependency-audit skill guidance for scan commands

### 2. Security Posture Review
- Use Task tool with subagent_type="security-auditor"
- Prompt: "Perform a security review of the codebase at $ARGUMENTS. Focus on: (a) hardcoded secrets, API keys, or credentials in source files, (b) OWASP Top 10 vulnerability patterns (SQL injection, XSS, CSRF, insecure deserialization), (c) authentication and authorization implementation gaps, (d) insecure cryptographic practices, (e) missing security headers or CORS misconfigurations. For each finding, report: file path, line number, severity (critical/high/medium/low), description, and recommended fix."
- Expected output: Structured security findings with severity, location, and remediation
- Context: Full codebase access

### 3. Code Quality and Tech Debt Analysis
- Use Task tool with subagent_type="tech-debt-reducer"
- Prompt: "Analyze the codebase at $ARGUMENTS for technical debt and code quality issues. Assess: (a) top 10 most complex files by cyclomatic/cognitive complexity, (b) code duplication hotspots, (c) dead code and unused exports, (d) naming inconsistencies and code smells, (e) dependency coupling and circular references, (f) consistency of error handling patterns. Score each finding by impact (how much it affects development velocity) and cost (effort to fix). Classify into quadrants: fix-now, plan-sprint, fix-opportunistically, defer."
- Expected output: Prioritized tech debt inventory with impact/cost scoring
- Context: Full codebase access

### 4. Architecture Integrity Assessment
- Use Task tool with subagent_type="backend-architect"
- Prompt: "Review the architectural structure of the codebase at $ARGUMENTS. Evaluate: (a) adherence to stated architecture patterns (layered, hexagonal, microservices, etc.), (b) layer violations (e.g., presentation layer accessing database directly), (c) module boundary clarity and separation of concerns, (d) API surface area — are public interfaces minimal and well-defined?, (e) configuration management patterns, (f) observability readiness (logging, metrics, tracing hooks). Provide an architecture health summary with specific violation locations."
- Expected output: Architecture assessment with pattern compliance, violations, and improvement areas
- Context: Full codebase access, focus on structural organization

### 5. Test Coverage and Quality Assessment
- Use Task tool with subagent_type="test-automator"
- Prompt: "Assess the test suite health for the codebase at $ARGUMENTS. Evaluate: (a) test coverage percentage (run coverage tool if available), (b) ratio of unit/integration/e2e tests, (c) test execution time and any slow tests (>5s), (d) flaky test indicators (retry logic, timing-dependent assertions, shared mutable state), (e) critical paths missing test coverage (authentication, payment, data mutations), (f) test code quality (DRY, clear assertions, proper setup/teardown). Summarize coverage gaps and test suite health metrics."
- Expected output: Coverage metrics, test quality assessment, and gap analysis
- Context: Full codebase and test directory access

## Phase 2: Synthesis and Scoring

### 6. Compile Unified Health Report
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Synthesize the findings from all five assessments into a unified Codebase Health Report. Calculate a composite health score (0-100) using these weights:

  | Dimension | Weight | Scoring Criteria |
  |-----------|--------|-----------------|
  | Security | 30% | Deduct 25 per critical, 15 per high, 5 per medium, 1 per low |
  | Dependencies | 15% | Deduct 20 per critical CVE, 10 per high, 3 per outdated major version |
  | Code Quality | 20% | Based on complexity distribution, duplication %, dead code % |
  | Architecture | 20% | Based on layer violations, coupling score, pattern consistency |
  | Test Coverage | 15% | Based on coverage %, critical path coverage, test quality |

  Floor the score at 0. Format the report as:

  ```
  # Codebase Health Report
  **Project:** [name]
  **Date:** [date]
  **Overall Score:** [X]/100 — [Grade: A/B/C/D/F]

  ## Score Breakdown
  [Table with dimension, score, weight, weighted score]

  ## Critical Findings (Fix Immediately)
  [Top findings requiring immediate action]

  ## High Priority (This Sprint)
  [Findings to address in current sprint]

  ## Medium Priority (Next Sprint)
  [Scheduled improvements]

  ## Health Trends
  [If previous reports exist, show trend]

  ## Recommended Action Plan
  [Ordered list of actions with effort estimates]
  ```"
- Expected output: Complete health report with composite score and prioritized action plan
- Context: All outputs from steps 1-5

## Configuration Options

- `scope`: Full codebase (default) or specific directories
- `severity_threshold`: Minimum severity to include (default: low)
- `skip_dimensions`: Comma-separated dimensions to skip (e.g., "architecture,testing")
- `output_format`: markdown (default), json, or html
- `compare_to`: Path to previous health report for trend analysis

## Success Criteria

- All five assessment dimensions evaluated with specific findings
- Composite health score calculated with transparent methodology
- Every finding includes: severity, file location, description, and remediation
- Action plan is prioritized by impact-to-effort ratio
- Report is self-contained and shareable with the team
- No false positives in critical/high findings (verified by cross-referencing agents)

## Coordination Notes

- Phase 1 tasks are independent and should run in parallel for efficiency
- Phase 2 depends on all Phase 1 outputs being complete
- If a dimension assessment fails (e.g., no test suite exists), score that dimension as 0 and note it
- The security assessment should NOT trigger any destructive operations
- Keep the final report under 500 lines — link to detailed findings rather than inlining everything

## Rollback Procedures

This command is read-only and does not modify the codebase. No rollback needed.

Target codebase: $ARGUMENTS
