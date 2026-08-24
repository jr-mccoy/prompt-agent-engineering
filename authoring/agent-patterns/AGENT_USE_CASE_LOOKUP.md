# Agent Use Case Lookup Guide

**Quick reference for selecting agent patterns based on your use case.**

---

## How to Use This Guide

1. **Find your use case** in the categories below
2. **Check recommended agent type** (Opus/Sonnet/Haiku/Inherit)
3. **Use the pattern combination** listed
4. **See example agent** for reference
5. **Build using [AGENT_QUICK_START.md](AGENT_QUICK_START.md)**

---

## Table of Contents

1. [Security & Compliance](#security--compliance)
2. [Architecture & Design](#architecture--design)
3. [Backend Development](#backend-development)
4. [Frontend & Mobile](#frontend--mobile)
5. [Cloud & Infrastructure](#cloud--infrastructure)
6. [DevOps & Operations](#devops--operations)
7. [Database & Data](#database--data)
8. [Testing & Quality](#testing--quality)
9. [Documentation](#documentation)
10. [Languages & Frameworks](#languages--frameworks)
11. [AI & Machine Learning](#ai--machine-learning)
12. [Business & Operations](#business--operations)
13. [Content & Marketing](#content--marketing)

---

## Security & Compliance

### Security Audit

**Use Case:** Comprehensive security audit of application/infrastructure

**Agent Type:** Opus (MAP-01)

**Pattern Combination:**
- MAP-01 (Critical Task Assignment)
- PP-01 (Expert Authority Persona)
- ACT-01 (Proactive Activation - Critical)
- DP-01 (Comprehensive Knowledge Base)
- DP-02 (Structured Response Approach)
- DP-03 (Capability Categorization)
- BP-01 (Quality-First Behavior)
- BP-04 (Security-Conscious Behavior)

**Example Agent:** `security-auditor`

**Key Characteristics:**
- DevSecOps integration
- OWASP standards
- Compliance frameworks (GDPR, HIPAA, SOC2)
- Vulnerability assessment
- Threat modeling

---

### Authentication Implementation

**Use Case:** Build OAuth2/OIDC authentication system

**Agent Type:** Opus (MAP-01) or Sonnet (MAP-02)

**Pattern Combination:**
- MAP-01 or MAP-02
- PP-03 (Technology Stack Specialist)
- ACT-01 or ACT-02
- TIP-03 (External Tool Integration)
- BP-04 (Security-Conscious)

**Example Agents:** `security-auditor`, `backend-security-coder`

---

### Compliance Documentation

**Use Case:** Create GDPR, HIPAA, or regulatory compliance docs

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-09 (Business Specialist Persona)
- ACT-02
- DP-01

**Example Agent:** `legal-advisor`

---

## Architecture & Design

### System Architecture Review

**Use Case:** Review system architecture for scalability, maintainability

**Agent Type:** Opus (MAP-01)

**Pattern Combination:**
- MAP-01
- PP-01 (Expert Authority)
- ACT-01 (Proactive - Critical)
- DP-01 + DP-02 + DP-03
- BP-01

**Example Agent:** `architect-review`

**Key Characteristics:**
- Clean architecture patterns
- Microservices expertise
- Event-driven systems
- DDD (Domain-Driven Design)

---

### API Design

**Use Case:** Design RESTful, GraphQL, or gRPC APIs

**Agent Type:** Opus (MAP-01) or Inherit (MAP-04)

**Pattern Combination:**
- MAP-01 or MAP-04
- PP-03 (Technology Stack)
- ACT-01 or ACT-02
- DP-01 + DP-02

**Example Agents:** `fastapi-pro`, `graphql-architect`, `backend-architect`

---

### Architecture Diagrams

**Use Case:** Create C4, system architecture, or ERD diagrams

**Agent Type:** Haiku (MAP-03) or Sonnet (MAP-02)

**Pattern Combination:**
- MAP-03 or MAP-02
- PP-07 (Creation Specialist)
- ACT-02
- DP-06 (Minimal Domain)

**Example Agents:** `mermaid-expert`, `c4-code`, `c4-component`

---

## Backend Development

### Python Development

**Use Case:** Build Python applications with modern practices

**Agent Type:** Opus (MAP-01)

**Pattern Combination:**
- MAP-01
- PP-03 (Technology Stack Specialist)
- ACT-01
- DP-01 + DP-02 + DP-05 (Year/Version Awareness)

**Example Agent:** `python-pro`

**Key Characteristics:**
- Python 3.12+ features
- Modern tooling (uv, ruff, pydantic)
- Async programming
- FastAPI, Django patterns

---

### FastAPI Development

**Use Case:** Build high-performance async APIs

**Agent Type:** Opus (MAP-01)

**Pattern Combination:**
- MAP-01
- PP-03 (Tech Stack) + PP-04 (Multi-Domain)
- ACT-01
- DP-01 + DP-02 + DP-05
- BP-02 (Performance-Conscious)

**Example Agent:** `fastapi-pro`

---

### Legacy Code Modernization

**Use Case:** Refactor legacy codebase, migrate frameworks

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-05 (Problem Solver) + PP-03 (Tech Stack)
- ACT-02
- BP-05 (Pragmatic)

**Example Agent:** `legacy-modernizer`

---

### Microservices Architecture

**Use Case:** Design/implement microservices

**Agent Type:** Opus (MAP-01) or Inherit (MAP-04)

**Pattern Combination:**
- MAP-01 or MAP-04
- PP-04 (Multi-Domain Integrator)
- ACT-01 or ACT-02
- DP-01 + DP-02

**Example Agents:** `backend-architect`, `graphql-architect`

---

## Frontend & Mobile

### React/Next.js Development

**Use Case:** Build modern React applications

**Agent Type:** Inherit (MAP-04)

**Pattern Combination:**
- MAP-04
- PP-03 (Technology Stack)
- ACT-02
- DP-01 + DP-05
- BP-03 (User-Centric)

**Example Agent:** `frontend-developer`

**Key Characteristics:**
- React 19, Next.js 15
- Server Components
- Performance optimization
- Accessibility

---

### Mobile App Development

**Use Case:** Build iOS, Android, or cross-platform apps

**Agent Type:** Inherit (MAP-04) or Opus (MAP-01)

**Pattern Combination:**
- MAP-04 or MAP-01
- PP-03
- ACT-02
- DP-01

**Example Agents:** `ios-developer`, `mobile-developer`, `flutter-expert`

---

### UI/UX Design

**Use Case:** Create interface designs, design systems

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-07 (Creation Specialist) or PP-03
- ACT-02
- BP-03 (User-Centric)

**Example Agent:** `ui-ux-designer`

---

## Cloud & Infrastructure

### Kubernetes Architecture

**Use Case:** Design K8s clusters, GitOps workflows

**Agent Type:** Opus (MAP-01)

**Pattern Combination:**
- MAP-01
- PP-04 (Multi-Domain Integrator)
- ACT-01
- DP-01 + DP-02 + DP-03
- TIP-02 (Agent Orchestration)

**Example Agent:** `kubernetes-architect`

**Key Characteristics:**
- EKS/AKS/GKE expertise
- GitOps (ArgoCD, Flux)
- Service mesh
- Platform engineering

---

### Cloud Architecture

**Use Case:** Design multi-cloud infrastructure

**Agent Type:** Opus (MAP-01) or Sonnet (MAP-02)

**Pattern Combination:**
- MAP-01 or MAP-02
- PP-04 (Multi-Domain)
- ACT-01
- DP-01 + DP-02 + DP-03

**Example Agents:** `cloud-architect`, `hybrid-cloud-architect`

---

### Terraform/IaC

**Use Case:** Create Terraform modules, infrastructure code

**Agent Type:** Opus (MAP-01)

**Pattern Combination:**
- MAP-01
- PP-03 (Tech Stack)
- ACT-01
- DP-01 + DP-02

**Example Agent:** `terraform-specialist`

---

### CI/CD Pipeline

**Use Case:** Build deployment pipelines, GitHub Actions

**Agent Type:** Haiku (MAP-03) or Sonnet (MAP-02)

**Pattern Combination:**
- MAP-03 or MAP-02
- PP-02 (Procedural Specialist)
- ACT-02
- TIP-05 (CLI/Command Execution)

**Example Agent:** `deployment-engineer`

---

## DevOps & Operations

### Debugging & Troubleshooting

**Use Case:** Debug errors, test failures, production issues

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-02 (Procedural Specialist) + PP-05 (Problem Solver)
- ACT-02
- BP-05 (Pragmatic)

**Example Agent:** `debugger`

---

### Incident Response

**Use Case:** Handle production incidents, outages

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-05 (Problem Solver)
- ACT-04 (Immediate Activation)
- DP-02 (Structured Response)

**Example Agent:** `incident-responder`

---

### Performance Optimization

**Use Case:** Optimize application/system performance

**Agent Type:** Inherit (MAP-04)

**Pattern Combination:**
- MAP-04
- PP-05 (Problem Solver) or PP-03
- ACT-02
- BP-02 (Performance-Conscious)

**Example Agent:** `performance-engineer`

---

### Observability Setup

**Use Case:** Implement monitoring, logging, tracing

**Agent Type:** Inherit (MAP-04)

**Pattern Combination:**
- MAP-04
- PP-04 (Multi-Domain)
- ACT-02
- TIP-03 (External Tool Integration)

**Example Agent:** `observability-engineer`

---

## Database & Data

### Database Architecture

**Use Case:** Design database schema, select technology

**Agent Type:** Opus (MAP-01)

**Pattern Combination:**
- MAP-01
- PP-01 (Expert Authority) + PP-04 (Multi-Domain)
- ACT-01
- DP-01 + DP-02

**Example Agent:** `database-architect`

---

### Database Optimization

**Use Case:** Optimize queries, indexes, performance

**Agent Type:** Inherit (MAP-04)

**Pattern Combination:**
- MAP-04
- PP-05 (Problem Solver) + PP-03
- ACT-02
- BP-02 (Performance-Conscious)

**Example Agent:** `database-optimizer`

---

### Data Engineering

**Use Case:** Build data pipelines, ETL, analytics

**Agent Type:** Opus (MAP-01)

**Pattern Combination:**
- MAP-01
- PP-04 (Multi-Domain)
- ACT-01
- DP-01 + DP-02

**Example Agent:** `data-engineer`

---

## Testing & Quality

### Test Automation

**Use Case:** Build comprehensive test suites, automation

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-06 (Quality Guardian) + PP-03
- ACT-02
- DP-01 + DP-04 (Example Interactions)
- BP-01 (Quality-First)

**Example Agent:** `test-automator`

---

### TDD Orchestration

**Use Case:** Implement TDD workflows, coordinate testing

**Agent Type:** Opus (MAP-01)

**Pattern Combination:**
- MAP-01
- PP-06 (Quality Guardian)
- ACT-01
- TIP-02 (Agent Orchestration)

**Example Agent:** `tdd-orchestrator`

---

### Code Review

**Use Case:** Review code for quality, security, performance

**Agent Type:** Opus (MAP-01)

**Pattern Combination:**
- MAP-01
- PP-06 (Quality Guardian) + PP-01
- ACT-01
- DP-01 + DP-03
- BP-01 + BP-04

**Example Agent:** `code-reviewer`

---

## Documentation

### Technical Documentation

**Use Case:** Create comprehensive technical docs, manuals

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-07 (Creation Specialist) or PP-08 (Educator)
- ACT-02
- DP-04 (Example Interactions)

**Example Agent:** `docs-architect`

---

### API Documentation

**Use Case:** Generate OpenAPI, SDK docs, developer portals

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-07 (Creation)
- ACT-02
- TIP-03 (External Tools)

**Example Agent:** `api-documenter`

---

### Tutorial Creation

**Use Case:** Create step-by-step tutorials, guides

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-08 (Educator)
- ACT-02
- DP-04

**Example Agent:** `tutorial-engineer`

---

### Diagram Generation

**Use Case:** Create flowcharts, sequences, ERDs

**Agent Type:** Haiku (MAP-03)

**Pattern Combination:**
- MAP-03
- PP-07 (Creation Specialist) + PP-10 (Minimalist)
- ACT-02
- DP-06 (Minimal Domain)

**Example Agent:** `mermaid-expert`

---

## Languages & Frameworks

### Advanced Language Expertise

**Use Case:** Master specific programming language (Rust, Go, Java, etc.)

**Agent Type:** Opus (MAP-01)

**Pattern Combination:**
- MAP-01
- PP-03 (Technology Stack Specialist)
- ACT-01
- DP-01 + DP-02 + DP-05 (Version Awareness)

**Example Agents:** `rust-pro`, `golang-pro`, `java-pro`, `typescript-pro`

---

### Framework Specialization

**Use Case:** Expert in specific framework (Django, FastAPI, React, etc.)

**Agent Type:** Opus (MAP-01) or Inherit (MAP-04)

**Pattern Combination:**
- MAP-01 or MAP-04
- PP-03
- ACT-01 or ACT-02
- DP-01 + DP-05

**Example Agents:** `django-pro`, `fastapi-pro`

---

### Shell Scripting

**Use Case:** Bash, POSIX shell automation

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-03
- ACT-02
- BP-05 (Pragmatic)

**Example Agents:** `bash-pro`, `posix-shell-pro`

---

## AI & Machine Learning

### LLM Application Development

**Use Case:** Build AI features, chatbots, RAG systems

**Agent Type:** Inherit (MAP-04)

**Pattern Combination:**
- MAP-04
- PP-03 (Tech Stack) + PP-04 (Multi-Domain)
- ACT-02
- DP-01

**Example Agent:** `ai-engineer`

---

### ML Engineering

**Use Case:** Build production ML systems, model serving

**Agent Type:** Inherit (MAP-04)

**Pattern Combination:**
- MAP-04
- PP-03 + PP-04
- ACT-02
- DP-01

**Example Agent:** `ml-engineer`

---

### Data Science

**Use Case:** Analytics, modeling, statistical analysis

**Agent Type:** Inherit (MAP-04)

**Pattern Combination:**
- MAP-04
- PP-01 (Expert) or PP-03
- ACT-02
- DP-01

**Example Agent:** `data-scientist`

---

### Prompt Engineering

**Use Case:** Design prompts, optimize AI systems

**Agent Type:** Inherit (MAP-04)

**Pattern Combination:**
- MAP-04
- PP-01 (Expert Authority)
- ACT-02
- DP-01

**Example Agent:** `prompt-engineer`

---

## Business & Operations

### Business Analysis

**Use Case:** KPI frameworks, analytics, strategic analysis

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-09 (Business Specialist)
- ACT-02
- DP-01

**Example Agent:** `business-analyst`

---

### Customer Support

**Use Case:** AI-powered support automation, chatbots

**Agent Type:** Haiku (MAP-03)

**Pattern Combination:**
- MAP-03
- PP-09 (Business) + PP-07 (Creation)
- ACT-02
- BP-03 (User-Centric)

**Example Agent:** `customer-support`

---

### HR & Legal

**Use Case:** HR policies, legal documentation, compliance

**Agent Type:** Sonnet (MAP-02)

**Pattern Combination:**
- MAP-02
- PP-09 (Business Specialist)
- ACT-02
- BP-01 (Quality-First)

**Example Agents:** `hr-pro`, `legal-advisor`

---

## Content & Marketing

### Content Creation

**Use Case:** Blog posts, marketing copy, content at scale

**Agent Type:** Haiku (MAP-03)

**Pattern Combination:**
- MAP-03
- PP-07 (Creation Specialist)
- ACT-02
- DP-06

**Example Agent:** `content-marketer`

---

### SEO Optimization

**Use Case:** SEO content, meta optimization, keyword strategy

**Agent Type:** Haiku (MAP-03) or Sonnet (MAP-02)

**Pattern Combination:**
- MAP-03 or MAP-02
- PP-07 (Creation) or PP-09 (Business)
- ACT-02

**Example Agents:** `seo-content-writer`, `seo-meta-optimizer`, `seo-keyword-strategist`

---

### Sales Automation

**Use Case:** Cold emails, proposals, sales scripts

**Agent Type:** Haiku (MAP-03)

**Pattern Combination:**
- MAP-03
- PP-07 (Creation) + PP-10 (Minimalist)
- ACT-02
- DP-06

**Example Agent:** `sales-automator`

---

## Pattern Combination Matrix

### By Task Criticality

| Criticality | Model | Persona | Activation | Domain | Behavior |
|-------------|-------|---------|------------|---------|----------|
| **Critical** | MAP-01 (Opus) | PP-01/PP-06 | ACT-01 | DP-01+DP-02+DP-03 | BP-01/BP-04 |
| **High** | MAP-02 (Sonnet) | PP-02/PP-03/PP-05 | ACT-02 | DP-01+DP-04 | BP-05 |
| **Medium** | MAP-02 (Sonnet) | PP-03/PP-07 | ACT-02 | DP-04 | BP-05 |
| **Low** | MAP-03 (Haiku) | PP-07/PP-10 | ACT-02/ACT-05 | DP-06 | - |
| **User Control** | MAP-04 (Inherit) | PP-03/PP-04 | ACT-02/ACT-05 | DP-01 | BP-03 |

### By Domain Type

| Domain | Model | Persona | Key Patterns |
|--------|-------|---------|--------------|
| **Security** | Opus | PP-01 | MAP-01+ACT-01+BP-04+DP-01+DP-02+DP-03 |
| **Architecture** | Opus | PP-01/PP-04 | MAP-01+ACT-01+DP-01+DP-02+DP-03 |
| **Development** | Sonnet/Inherit | PP-02/PP-03 | MAP-02/MAP-04+ACT-02+DP-01 |
| **Operations** | Sonnet | PP-02/PP-05 | MAP-02+ACT-02+BP-05 |
| **Creation** | Haiku | PP-07/PP-10 | MAP-03+ACT-02+DP-06 |
| **Business** | Sonnet/Haiku | PP-09 | MAP-02/MAP-03+ACT-02 |

---

## Quick Decision Guide

### Step 1: What are you building?

```
Security/Compliance → Opus + PP-01/PP-06 + ACT-01
Architecture/Design → Opus + PP-01/PP-04 + ACT-01
Advanced Language → Opus + PP-03 + ACT-01
Backend Development → Sonnet/Inherit + PP-03 + ACT-02
Frontend Development → Inherit + PP-03 + ACT-02
Testing/Quality → Sonnet + PP-06 + ACT-02
Debugging/Ops → Sonnet + PP-02/PP-05 + ACT-02
Documentation → Sonnet + PP-07/PP-08 + ACT-02
Diagrams/Visuals → Haiku + PP-07 + ACT-02
Content/Marketing → Haiku + PP-07 + ACT-02
```

### Step 2: Combine Patterns

Use the pattern combinations from the relevant section above.

### Step 3: Build with Quick Start

Follow [AGENT_QUICK_START.md](AGENT_QUICK_START.md) Step 4 to build your agent file.

---

## Next Steps

1. **Found your use case?** → Use the pattern combination listed
2. **Ready to build?** → Follow [AGENT_QUICK_START.md](AGENT_QUICK_START.md)
3. **Need pattern details?** → See [AGENT_PATTERN_INDEX.md](AGENT_PATTERN_INDEX.md)
4. **Want to validate?** → Use [AGENT_QUALITY_RUBRIC.md](AGENT_QUALITY_RUBRIC.md)
5. **See examples?** → Check [security_auditor.md](../../domain-agentic-resources/agents/security/security_auditor.md)

---

**Document Version:** 1.0
**Last Updated:** 2025-12-27
**Use Cases Covered:** 40+
**Pattern Combinations:** 15+ major combinations
