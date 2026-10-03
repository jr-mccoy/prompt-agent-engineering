# Domain: Software Engineering

**Purpose:** Prompts for code analysis, testing, DevOps, cloud infrastructure, API design, and mobile development.

---

## What This Domain Covers

All technical prompts related to building and maintaining software:

1. **Analysis** - Security, performance, quality, architecture review
2. **Testing** - Unit tests, E2E tests, accessibility, test strategies
3. **DevOps** - CI/CD, Docker, infrastructure as code
4. **Cloud** - AWS, GCP, Azure, serverless
5. **API** - REST, GraphQL design and review
6. **Mobile** - iOS, Android, React Native, Flutter
7. **Algorithms** - Algorithm design and complexity analysis
8. **Vibe Coding Rescue** - Diagnose and rescue AI-assisted projects that have hit a wall
9. **Data Engineering** - Pipeline correctness, dimensional models, data quality placement, backfills, data incidents

---

## Directory Structure

```
domain-software-engineering/
├── analysis/
│   ├── security/             # Vulnerability analysis, OWASP, STRIDE, threat modeling, detection/hunting/vuln-mgmt/SOC triage
│   ├── performance/          # Bottleneck identification, optimization, scalability
│   ├── quality/              # Complexity, duplication, style, documentation
│   ├── architecture/         # Design patterns, layers, coupling, agentic context design
│   ├── evolution/            # Tech debt, code churn, refactoring priority
│   ├── database/             # Schema design, query optimization, migrations
│   └── integration/          # Cross-system integration validation
├── testing/                  # Unit, integration, E2E, mutation, a11y, flaky tests
├── devops/                   # CI/CD, Docker, K8s, Terraform, Helm, GitOps, LLM Ops
├── cloud/                    # AWS, GCP, Azure, serverless, cost optimization, FinOps
├── data-engineering/         # Pipeline design review, dimensional models, DQ tests, backfills, data downtime
├── api/                      # REST, GraphQL, OpenAPI, versioning
├── mobile/                   # iOS, Android, React Native, Flutter
├── algorithms/               # Data structures, scheduling, constraint satisfaction
├── dotnet/                   # ASP.NET Core, EF Core, NuGet
├── java-spring/              # Spring Boot, Spring Security, JVM, Maven/Gradle
├── embedded/                 # Firmware, IoT protocols, embedded systems
├── electron-smart-tv/        # Electron apps, smart-TV / 10-ft UI
├── localization/             # i18n, pseudo-localization, ICU, translation workflow
├── vibe-coding-rescue/       # Wall diagnosis, rules file, task decomposition, AI-code audit, handoff briefing
└── README.md
```

---

## File Count

_Last refreshed: 2026-04-17 (security, cloud, data-engineering rows: 2026-10-03)_

| Subdirectory | Count | Description |
|--------------|-------|-------------|
| `analysis/security/` | 29 | Security vulnerability prompts (OWASP, SQLi, XSS, auth, threat modeling) and security operations (detection engineering, threat hunting, vulnerability management, SOC triage) |
| `analysis/performance/` | 8 | Performance bottlenecks, profiling, optimization |
| `analysis/quality/` | 8 | Complexity, duplication, style, documentation coverage |
| `analysis/architecture/` | 27 | Design patterns, layers, coupling, context/agentic-system architecture |
| `analysis/evolution/` | 6 | Tech debt, code churn, refactoring priority |
| `analysis/database/` | 8 | Schema design, query optimization, migrations, indexing |
| `analysis/integration/` | 1 | Cross-system integration validation (e.g., Firebase) |
| `testing/` | 16 | Unit, integration, E2E, mutation, accessibility, visual regression, flaky tests |
| `devops/` | 21 | CI/CD, Docker, Kubernetes, Terraform, Helm, GitOps, LLM Ops |
| `cloud/` | 25 | AWS, GCP, Azure, serverless, security, cost optimization, FinOps (allocation, bill-spike investigation, commitments) |
| `data-engineering/` | 5 | Pipeline idempotency/late data/exactly-once review, dimensional model review, data quality test strategy, incremental load and backfill, data downtime postmortem |
| `api/` | 6 | REST, GraphQL, OpenAPI, versioning, rate limiting |
| `mobile/` | 255 | iOS, Android, React Native, Flutter, cross-platform |
| `algorithms/` | 10 | Data structures, scheduling, constraint satisfaction |
| `dotnet/` | 4 | ASP.NET Core, EF Core, NuGet |
| `java-spring/` | 4 | Spring Boot, Spring Security, JVM, Maven/Gradle |
| `embedded/` | 8 | Firmware, IoT protocols, embedded systems |
| `electron-smart-tv/` | 10 | Electron apps, smart-TV / 10-ft UI |
| `localization/` | 8 | i18n, pseudo-localization, ICU, translation workflow |
| `vibe-coding-rescue/` | 5 | Wall diagnosis, rules file design, stuck-task decomposition, AI-generated-code security audit, engineer handoff briefing |
| **Total** | **467** | _(excluding README files and the top-level review report)_ |

---

## Exemplar Prompts (Gold Standard)

These prompts demonstrate best practices and can serve as templates for new prompts:

| Prompt | Why It's Exemplary |
|--------|-------------------|
| [`security_vulnerability_analysis.md`](analysis/security/security_vulnerability_analysis.md) | Masterclass in false-positive prevention with comprehensive "DO NOT" section |
| [`testing_unit_test_generation.md`](testing/testing_unit_test_generation.md) | AAA pattern, mutation testing integration, coverage rating framework |
| [`quality_code_complexity_analysis.md`](analysis/quality/quality_code_complexity_analysis.md) | Multi-dimensional analysis with clear severity ratings |

---

## Key Patterns

### Security Analysis
```
Analyze [codebase/file] for:
- OWASP Top 10 vulnerabilities
- Authentication/authorization flaws
- Input validation issues
- Secrets exposure
```

### Performance Review
```
Identify performance bottlenecks:
- Database query optimization
- Memory usage patterns
- Algorithmic complexity
- Caching opportunities
```

### Architecture Assessment
```
Review architecture for:
- SOLID principle adherence
- Coupling and cohesion
- Scalability concerns
- Technical debt
```

---

## AI Coding Agent Usage Notes (ChatGPT/Codex/Claude Code)

These files are **prompts, not executable skills**. They work best when you give an AI coding agent explicit execution constraints and artifacts.

### Add this context before running any prompt
- Repository root path and relevant subdirectories
- Stack/tooling (`package.json`, `pyproject.toml`, `go.mod`, etc.)
- Definition of done (tests, lint, security checks, performance budget)
- Change constraints (files to avoid, backward-compatibility requirements)

### Prompt hardening pattern
For higher-quality agent output, prepend these clauses:
1. **Evidence clause**: require file paths, line numbers, and concrete snippets
2. **Action clause**: require a sequenced plan with smallest-safe-first changes
3. **Validation clause**: require exact commands and expected pass/fail criteria
4. **Risk clause**: require assumptions, uncertainty, and rollback guidance

### Recommended output contract
Ask the agent to return:
- Findings grouped by severity (Critical/High/Medium/Low)
- Proposed patch list (`file -> change summary`)
- Verification commands and results
- Deferred items and open questions

## When to Use This Domain

Use these prompts when you need to:
- Find security vulnerabilities
- Optimize code performance
- Review code quality
- Design or review APIs
- Set up DevOps pipelines
- Work with cloud infrastructure
- Review data pipelines, warehouse models, and data quality
- Develop mobile applications

**Do NOT use for:** Non-coding tasks (use domain-business-strategy, domain-productivity, etc.)

---

*Migrated from: `prompts/coding/`*
