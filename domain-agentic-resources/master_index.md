<!-- INVENTORY_COUNTS: {"agents_categories": {"architecture": 6, "backend": 8, "business": 2, "business-operations": 11, "cloud-infrastructure": 9, "code-quality": 4, "creative": 2, "database": 4, "deployment": 1, "devops": 6, "documentation": 5, "education": 2, "frontend-mobile": 22, "healthcare": 2, "languages": 21, "ml-ai": 6, "orchestration": 2, "research": 2, "security": 4, "seo-marketing": 12, "testing": 5, "web-development": 5, "writing": 2}, "agents_total": 143, "commands_categories": {"accessibility": 2, "architecture": 2, "business": 3, "code-quality": 5, "creative": 3, "data-analysis": 1, "database": 2, "deployment": 2, "devops": 8, "documentation": 1, "education": 3, "framework-migration": 3, "git-workflows": 3, "healthcare": 4, "mobile-development": 12, "multi-agent": 8, "orchestration": 9, "other": 18, "performance": 3, "research": 3, "security": 6, "testing": 6, "troubleshooting": 5, "writing": 3}, "commands_total": 115, "date": "2026-08-24", "skills_categories": {"accessibility": 2, "backend-development": 13, "blockchain-web3": 16, "business": 3, "cicd-automation": 4, "cloud-infrastructure": 14, "content-creation": 5, "creative": 2, "data-engineering": 10, "developer-tools": 35, "devops": 3, "document-processing": 7, "education": 2, "financial-records": 4, "framework-migration": 4, "game-development": 2, "healthcare": 11, "languages": 18, "llm-application-dev": 10, "marketing": 41, "ml-ai": 4, "mobile-development": 36, "observability": 5, "other": 2, "payments": 4, "research": 2, "security": 36, "seo-marketing": 4, "skills": 3, "testing-qa": 18, "web-development": 8, "writing": 2}, "skills_total": 330, "total_resources": 588, "type": "master"} -->

# Claude Code Resources Master Index

**Quick searchable reference for all 588 resources in this directory.**

**Last Updated:** 2026-08-24
**Total Resources:** 588 (143 agents + 330 skills + 115 commands)

---

## Quick Navigation

| Jump to | Count | Description |
|---------|-------|-------------|
| [**Agents**](#agent-index) | 143 | Parallel workers with model assignments |
| [**Skills**](#skill-index) | 330 | Domain containers with workflows |
| [**Commands**](#command-index) | 115 | Slash commands in `commands/` (workflow commands are a subset, not additional) |
| [**By Domain**](#domain-index) | 25+ | Resources grouped by domain |
| [**By Task**](#task-index) | 50+ | Resources grouped by common tasks |
| [**By Model**](#model-index) | 4 | Agents grouped by Opus/Sonnet/Haiku/Inherit |

---

## Architecture Quick Reference

### Canonical Framework

```
AGENTS (parallel workers) → invoke → SKILLS (domain containers) → contain → COMMANDS (workflows)
```

**Example:**
```
security-auditor agent
  └→ invokes security skill
      ├→ SKILL.md (routing + knowledge)
      └→ workflows/
          ├→ scan.md (command)
          ├→ audit.md (command)
          └→ harden.md (command)
```

### Repository Note

**⚠️ This repository** uses an alternative structure with standalone commands in `/commands/`. For new resources, follow the canonical framework with commands in `skills/{domain}/workflows/`.

---

## Agent Index

**Total:** 143 agents across 23 categories

### By Model Assignment

| Model | Count | Use For | Examples |
|-------|-------|---------|----------|
| **Opus 4.5** | 36 (28%) | Critical architecture, security, code review | architect-review, security-auditor, code-reviewer |
| **Sonnet 4.5** | 43 (34%) | Balanced development tasks | python-pro, backend-architect, frontend-developer |
| **Haiku 4.5** | 18 (14%) | Fast operations, quick tasks | code-formatter, quick-scaffolder |
| **Inherit** | 31 (24%) | User choice based on budget | Many utility agents |

### Quick Agent Lookup

**Architecture & Design**
- `architect-review` (Opus) - System architecture review
- `c4-component` (Sonnet) - C4 component diagrams
- `c4-container` (Sonnet) - C4 container diagrams
- `c4-context` (Sonnet) - C4 context diagrams
- `c4-code` (Sonnet) - C4 code-level documentation
- `code-reviewer` (Opus) - Comprehensive code review
- `security-auditor` (Opus) - Security audits

**Backend Development**
- `backend-architect` (Inherit) - Backend architecture
- `data-engineer` (Opus) - Data pipeline architecture
- `django-pro` (Opus) - Django expertise
- `fastapi-pro` (Opus) - FastAPI expertise
- `graphql-architect` (Opus) - GraphQL API design
- `microservices-architect` (Inherit) - Microservices patterns
- `python-pro` (Opus) - Python expertise
- `serverless-architect` (Inherit) - Serverless architecture
- `tdd-orchestrator` (Opus) - TDD workflow coordination

**Cloud & Infrastructure**
- `cloud-architect` (Opus) - Multi-cloud architecture
- `hybrid-cloud-architect` (Opus) - Hybrid cloud design
- `kubernetes-architect` (Opus) - Kubernetes expertise
- `terraform-specialist` (Opus) - Terraform IaC

**Languages (23 agents)**
- `blockchain-developer` (Opus) - Solidity/Web3
- `c-pro` (Opus) - C programming
- `cpp-pro` (Opus) - C++ programming
- `csharp-pro` (Sonnet) - C# programming
- `elixir-pro` (Inherit) - Elixir programming
- `go-expert` (Sonnet) - Go programming
- `golang-pro` (Opus) - Go expertise
- `java-pro` (Opus) - Java programming
- `kotlin-pro` (Sonnet) - Kotlin programming
- `lua-pro` (Inherit) - Lua programming
- `minecraft-bukkit-pro` (Opus) - Minecraft plugin development
- `perl-expert` (Inherit) - Perl programming
- `php-pro` (Inherit) - PHP programming
- `python-architect` (Sonnet) - Python architecture
- `python-pro` (Opus) - Python expertise
- `r-expert` (Inherit) - R programming
- `ruby-expert` (Inherit) - Ruby programming
- `ruby-on-rails-pro` (Sonnet) - Rails framework
- `rust-pro` (Opus) - Rust programming
- `scala-expert` (Inherit) - Scala programming
- `swift-expert` (Sonnet) - Swift programming
- `typescript-pro` (Opus) - TypeScript expertise
- `unity-developer` (Opus) - Unity game development

**DevOps & Deployment (16 agents)**
- `ci-cd-specialist` (Sonnet) - CI/CD pipelines
- `deployment-engineer` (Sonnet) - Deployment automation
- `devops-troubleshooter` (Haiku) - DevOps debugging
- `dx-optimizer` (Sonnet) - Developer experience
- `error-detective` (Sonnet) - Error investigation
- `incident-responder` (Haiku) - Incident response
- `legacy-modernizer` (Sonnet) - Legacy system migration
- `monorepo-architect` (Sonnet) - Monorepo management
- `network-engineer` (Sonnet) - Network configuration
- `observability-engineer` (Sonnet) - Monitoring & observability
- `performance-engineer` (Sonnet) - Performance optimization
- And 5 more...

**Security (2 agents)**
- `security-auditor` (Opus) - Comprehensive security audit
- `threat-modeling-expert` (Sonnet) - Threat modeling

**Testing (6 agents)**
- `code-reviewer` (Opus) - Code review
- `security-auditor` (Opus) - Security testing
- `test-automator` (Sonnet) - Test automation
- And 3 more...

**Frontend & Mobile (8 agents)**
- `android-developer` (Sonnet) - Android development
- `backend-architect` (Inherit) - Backend for mobile
- `flutter-expert` (Sonnet) - Flutter development
- `frontend-developer` (Sonnet) - Frontend development
- `frontend-security-coder` (Inherit) - Frontend security
- `ios-developer` (Sonnet) - iOS development
- `mobile-developer` (Sonnet) - Mobile development
- `ui-ux-designer` (Inherit) - UI/UX design

**Complete Agent Listing:** See `agents/README.md` for full index with descriptions.

---

## Skill Index

**Total:** 330 skills across 32 categories

### Skills with Bundled Resources

**32 skills (24%)** include bundled scripts, references, or assets:

**Cloud Infrastructure (12 skills)**
- `helm-chart-scaffolding` - Helm chart generation (1,515 lines bundled)
- `k8s-manifest-generator` - Kubernetes manifests (2,664 lines bundled)
- `k8s-security-policies` - K8s security (701 lines bundled)
- `gitops-workflow` - GitOps patterns (553 lines bundled)
- `terraform-module-library` - Terraform modules (314 lines bundled)
- And 7 more...

**Developer Tools (18 skills)**
- `github-ops` - GitHub operations (2,161 lines bundled)
- `skill-creator` - Meta-skill for skill creation (1,454 lines bundled)
- `session-history-finder` - History recovery (1,272 lines bundled)
- `repomix-safe-mixer` - Secure code mixing (570 lines bundled)
- `repomix-unmixer` - Code extraction (1,073 lines bundled)
- `statusline-generator` - Status line config (474 lines bundled)
- And 12 more...

**Document Processing (6 skills)**
- `ppt-creator` - PowerPoint generation (4,893 lines bundled)
- `pdf-creator` - PDF generation (340 lines bundled)
- `docs-cleaner` - Documentation cleanup (136 lines bundled)
- `markdown-tools` - Markdown conversion (555 lines bundled)
- `mermaid-tools` - Diagram extraction (298 lines bundled)
- `transcript-fixer` - Transcript editing (20,061 lines bundled!)

**LLM Application Development (11 skills)**
- `prompt-engineering-patterns` - Prompt patterns (1,750 lines bundled)
- `prompt-optimizer` - EARS methodology (1,014 lines bundled)
- `promptfoo-evaluation` - LLM evaluation (642 lines bundled)
- `llm-icon-finder` - Icon discovery (179 lines bundled)
- And 7 more...

**Testing & QA (1 skill)**
- `qa-expert` - Autonomous testing (5 skills bundled)

**Content Creation (5 skills)**
- `cli-demo-generator` - CLI demo videos (873 lines bundled)
- `video-comparer` - Video comparison (2,392 lines bundled)
- `teams-channel-post-writer` - Teams posts (189 lines bundled)
- `youtube-downloader` - Video download (680 lines bundled)

**Backend Development (10 skills)**
- `api-design-principles` - API design (665 lines bundled)

**Web Development (2 skills)**
- `ui-designer` - Design system extraction (477 lines bundled)
- `cloudflare-troubleshooting` - Cloudflare debugging (1,853 lines bundled)

**Complete Skill Listing:** See `skills/README.md` for full index with dependencies and resources.

---

## Command Counting Definition

- **Command:** any Markdown file under `domain-agentic-resources/commands/**/*.md`, excluding category `README.md` files.
- **Workflow command:** a command subtype (typically in orchestration/multi-agent categories). It is **included within** the command total and is never counted separately.


## Command Index

**Total:** 115 commands across 24 categories

### Standalone Commands (Legacy wshobson/agents)

**Orchestration (7 commands)**
- `/full-stack-feature` - Coordinates 7+ agents for feature development
- `/multi-agent-optimize` - System-wide optimization
- `/issue-resolution` - Issue investigation and resolution
- `/improve-agent` - Agent self-improvement
- `/context-save` - Save conversation context
- `/context-restore` - Restore conversation context
- `/standup-notes` - Generate standup notes

**Security (5 commands)**
- `/security-hardening` - Multi-agent security assessment
- `/compliance-check` - Compliance verification
- `/security-dependencies` - Dependency security scan
- `/security-scan` - Security vulnerability scan
- `/threat-model` - Threat modeling

**Testing (5 commands)**
- `/test-coverage` - Code coverage analysis
- `/tdd-workflow` - TDD workflow automation
- `/e2e-test-gen` - E2E test generation
- `/mutation-testing` - Mutation testing
- `/visual-regression` - Visual regression testing

**DevOps (8 commands)**
- `/docker-optimize` - Docker optimization
- `/k8s-deploy` - Kubernetes deployment
- `/ci-cd-setup` - CI/CD pipeline setup
- `/terraform-plan` - Terraform planning
- `/ansible-playbook` - Ansible automation
- And 3 more...

**Performance (3 commands)**
- `/multi-agent-review` - Performance review
- `/performance-audit` - Performance audit
- `/load-test` - Load testing

**Complete Command Listing:** See `commands/README.md` for full index.

### Workflow Commands (Canonical Framework)

**⚠️ Note:** In canonical framework, commands live in `skills/{domain}/workflows/`. This repository is being migrated.

**Expected structure (for reference):**
```
skills/security/workflows/
  ├─ scan.md
  ├─ audit.md
  └─ harden.md

skills/kubernetes/workflows/
  ├─ deploy.md
  ├─ scale.md
  └─ troubleshoot.md
```

---

## Domain Index

**Resources organized by domain:**

### Security
- **Agents:** security-auditor (Opus), threat-modeling-expert (Sonnet)
- **Skills:** security-scanning, threat-analysis, compliance-frameworks, k8s-security-policies (5+ skills)
- **Commands:** /security-hardening, /compliance-check, /security-scan, /threat-model

### Kubernetes & Cloud
- **Agents:** kubernetes-architect (Opus), cloud-architect (Opus), terraform-specialist (Opus)
- **Skills:** helm-chart-scaffolding, k8s-manifest-generator, k8s-security-policies, gitops-workflow, terraform-module-library (12+ skills)
- **Commands:** /k8s-deploy, /terraform-plan, /helm-package

### Python Development
- **Agents:** python-pro (Opus), python-architect (Sonnet)
- **Skills:** async-python-patterns, python-testing-patterns, python-performance-optimization (13+ skills)
- **Commands:** /python-scaffold, /python-test-gen

### Backend & APIs
- **Agents:** backend-architect (Inherit), graphql-architect (Opus), fastapi-pro (Opus), django-pro (Opus)
- **Skills:** api-design-principles, architecture-patterns, microservices-patterns (10+ skills)
- **Commands:** /api-scaffold, /graphql-schema-gen

### Frontend & Mobile
- **Agents:** frontend-developer (Sonnet), ios-developer (Sonnet), android-developer (Sonnet), flutter-expert (Sonnet)
- **Skills:** react-patterns, vue-patterns, mobile-patterns (4+ skills)
- **Commands:** /frontend-scaffold, /mobile-app-gen

### DevOps & Infrastructure
- **Agents:** devops-troubleshooter (Haiku), deployment-engineer (Sonnet), observability-engineer (Sonnet), ci-cd-specialist (Sonnet)
- **Skills:** incident-runbook-templates, monitoring-patterns (3+ skills)
- **Commands:** /ci-cd-setup, /docker-optimize, /ansible-playbook (8 commands)

### Testing & QA
- **Agents:** test-automator (Sonnet), code-reviewer (Opus)
- **Skills:** qa-expert, testing-patterns (1+ skills)
- **Commands:** /tdd-workflow, /test-coverage, /e2e-test-gen (5 commands)

### Documentation
- **Agents:** docs-architect (Sonnet), technical-writer (Inherit)
- **Skills:** ppt-creator, pdf-creator, docs-cleaner, markdown-tools, mermaid-tools (6+ skills)
- **Commands:** /docs-gen, /api-docs-gen

### LLM & AI Development
- **Agents:** prompt-engineer (Sonnet), llm-architect (Inherit)
- **Skills:** prompt-engineering-patterns, prompt-optimizer, promptfoo-evaluation, llm-icon-finder (11+ skills)
- **Commands:** /prompt-optimize, /llm-eval

### GitHub & Git
- **Agents:** github-specialist (Haiku)
- **Skills:** github-ops, git-workflows (2+ skills)
- **Commands:** /pr-create, /issue-triage

### Database
- **Agents:** database-architect (Opus), database-optimizer (Sonnet)
- **Skills:** sql-optimization, database-migration (3+ skills)
- **Commands:** /migration-gen, /db-optimize

---

## Task Index

**Find resources by common tasks:**

### Code Review
- **Primary:** code-reviewer agent (Opus)
- **Supporting:** architect-review agent (Opus), security-auditor agent (Opus)
- **Skills:** code-review-patterns
- **Commands:** /multi-agent-review

### Security Audit
- **Primary:** security-auditor agent (Opus)
- **Supporting:** threat-modeling-expert agent (Sonnet)
- **Skills:** security-scanning, threat-analysis, k8s-security-policies
- **Commands:** /security-hardening, /security-scan, /threat-model

### Kubernetes Deployment
- **Primary:** kubernetes-architect agent (Opus)
- **Skills:** helm-chart-scaffolding, k8s-manifest-generator, k8s-security-policies, gitops-workflow
- **Commands:** /k8s-deploy, /helm-package

### API Design
- **Primary:** graphql-architect agent (Opus) or backend-architect agent (Inherit)
- **Skills:** api-design-principles
- **Commands:** /api-scaffold, /graphql-schema-gen

### Testing
- **Primary:** test-automator agent (Sonnet)
- **Skills:** qa-expert, testing-patterns
- **Commands:** /tdd-workflow, /test-coverage, /e2e-test-gen, /mutation-testing

### Performance Optimization
- **Primary:** performance-engineer agent (Sonnet)
- **Skills:** python-performance-optimization, observability-patterns
- **Commands:** /performance-audit, /load-test

### Python Development
- **Primary:** python-pro agent (Opus) or python-architect agent (Sonnet)
- **Skills:** async-python-patterns, python-testing-patterns
- **Commands:** /python-scaffold

### Documentation
- **Primary:** docs-architect agent (Sonnet)
- **Skills:** ppt-creator, pdf-creator, docs-cleaner, markdown-tools
- **Commands:** /docs-gen, /api-docs-gen

### CI/CD Setup
- **Primary:** ci-cd-specialist agent (Sonnet)
- **Skills:** github-actions-templates, gitlab-ci-patterns
- **Commands:** /ci-cd-setup

### Database Work
- **Primary:** database-architect agent (Opus)
- **Skills:** sql-optimization, database-migration
- **Commands:** /migration-gen, /db-optimize

### Incident Response
- **Primary:** incident-responder agent (Haiku)
- **Skills:** incident-runbook-templates
- **Commands:** /issue-resolution

### GitHub Operations
- **Primary:** github-specialist agent (Haiku)
- **Skills:** github-ops
- **Commands:** /pr-create, /issue-triage

### Terraform/IaC
- **Primary:** terraform-specialist agent (Opus)
- **Skills:** terraform-module-library
- **Commands:** /terraform-plan

### Prompt Engineering
- **Primary:** prompt-engineer agent (Sonnet)
- **Skills:** prompt-engineering-patterns, prompt-optimizer
- **Commands:** /prompt-optimize

---

## Model Index

**Agents by model assignment (for cost optimization):**

### Opus 4.5 (36 agents - 28%)

**Use for:** Critical architecture, security audits, complex design decisions

**Cost:** High | **Speed:** Slow | **Quality:** Highest

**Agents:**
- architect-review, code-reviewer, security-auditor (Architecture/Security)
- kubernetes-architect, cloud-architect, terraform-specialist (Cloud)
- database-architect, data-engineer (Database)
- python-pro, graphql-architect, fastapi-pro, django-pro, tdd-orchestrator (Backend)
- blockchain-developer, c-pro, cpp-pro, golang-pro, java-pro, minecraft-bukkit-pro, rust-pro, typescript-pro, unity-developer (Languages)
- And 7 more...

**Total: 36 agents**

### Sonnet 4.5 (43 agents - 34%)

**Use for:** Balanced development tasks, feature implementation

**Cost:** Medium | **Speed:** Medium | **Quality:** High

**Agents:**
- backend-architect, frontend-developer, test-automator, deployment-engineer (Development)
- performance-engineer, observability-engineer, ci-cd-specialist (DevOps)
- python-architect, go-expert, kotlin-pro, swift-expert, csharp-pro, ruby-on-rails-pro (Languages)
- ios-developer, android-developer, flutter-expert, mobile-developer (Mobile)
- docs-architect, prompt-engineer, threat-modeling-expert (Specialized)
- c4-component, c4-container, c4-context, c4-code (Architecture docs)
- And 20 more...

**Total: 43 agents**

### Haiku 4.5 (18 agents - 14%)

**Use for:** Fast operations, quick scaffolding, simple validations

**Cost:** Low | **Speed:** Fast | **Quality:** Good

**Agents:**
- code-formatter, quick-scaffolder, syntax-checker (Quick ops)
- devops-troubleshooter, incident-responder (Fast response)
- github-specialist (Quick GitHub ops)
- And 12 more...

**Total: 18 agents**

### Inherit (31 agents - 24%)

**Use for:** User chooses model based on budget/performance needs

**Cost:** Variable | **Speed:** Variable | **Quality:** Variable

**Agents:**
- backend-architect, microservices-architect, serverless-architect (Backend)
- frontend-security-coder, mobile-security-coder, ui-ux-designer (Frontend/Mobile)
- llm-architect, technical-writer (Specialized)
- php-pro, ruby-expert, perl-expert, lua-pro, scala-expert, r-expert, elixir-pro (Languages)
- And 14 more...

**Total: 31 agents**

---

## Search Tips

### By Keyword

**Search this file with Ctrl+F / Cmd+F:**

- **Language:** Search "python", "java", "rust", etc.
- **Technology:** Search "kubernetes", "terraform", "docker", etc.
- **Task:** Search "security", "testing", "deployment", etc.
- **Model:** Search "Opus", "Sonnet", "Haiku"
- **Domain:** Search "backend", "frontend", "cloud", "mobile"

### By File Location

**For detailed information:**
- **Agents:** See `agents/README.md` (128 agents with full descriptions)
- **Skills:** See `skills/README.md` (132 skills with bundled resources)
- **Commands:** See `commands/README.md` (71 commands with orchestration details)

### By Architecture

**Understanding relationships:**
- **Integration:** See `documentation/INTEGRATION_WITH_PROMPTS.md`
- **Mapping:** See `documentation/PROMPT_RESOURCE_MAPPING.md`
- **Guide:** See `CLAUDE.md` (this directory's navigation guide)

---

## Quick Reference Cards

### New to Claude Code Resources?

**Start here:**
1. Read `CLAUDE.md` - Architecture and navigation
2. Browse `agents/README.md` - See available agents
3. Browse `skills/README.md` - See available skills
4. Read Daniel Miessler's post: [When to use skills vs commands vs agents](https://danielmiessler.com/blog/when-to-use-skills-vs-commands-vs-agents)

### Looking for Specific Functionality?

**Use this index:**
1. Search by domain (Security, K8s, Python, etc.)
2. Check task index (Code Review, Testing, Deployment, etc.)
3. Find appropriate resource type (Agent/Skill/Command)
4. Navigate to detailed README

### Creating New Resources?

**Follow creation guides:**
- **Agents:** `AGENT_QUICK_START.md` (to be created)
- **Skills:** `../authoring/skill-patterns/AGENT_SKILL_QUICK_START.md` ✅
- **Commands:** Place in `skills/{domain}/workflows/` (canonical framework)

### Cost Optimization?

**Use model index:**
1. Critical tasks → Opus agents
2. Balanced tasks → Sonnet agents
3. Quick tasks → Haiku agents
4. Flexible → Inherit agents

See `documentation/INTEGRATION_WITH_PROMPTS.md` for 40-60% cost savings strategies.

---

**Repository:** jr-mccoy/prompt-agent-engineering
**Directory:** domain-agentic-resources/
**Last Updated:** 2025-12-27
**Version:** 1.0.0
