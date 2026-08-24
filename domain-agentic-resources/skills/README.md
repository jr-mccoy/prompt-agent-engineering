<!-- INVENTORY_COUNTS: {"categories": {"accessibility": 2, "backend-development": 13, "blockchain-web3": 16, "business": 3, "cicd-automation": 4, "cloud-infrastructure": 14, "content-creation": 5, "creative": 2, "data-engineering": 10, "developer-tools": 35, "devops": 3, "document-processing": 7, "education": 2, "financial-records": 4, "framework-migration": 4, "game-development": 2, "healthcare": 11, "languages": 18, "llm-application-dev": 10, "marketing": 41, "ml-ai": 4, "mobile-development": 36, "observability": 5, "other": 2, "payments": 4, "research": 2, "security": 36, "seo-marketing": 4, "skills": 3, "testing-qa": 18, "web-development": 8, "writing": 2}, "date": "2026-08-24", "total": 330, "type": "skills"} -->

# Claude Code Skills Index

**Comprehensive index of 330 Claude Code skills organized by domain.**

## Overview

This directory contains **330 specialized skills** for Claude Code. Skills are modular knowledge packages that use progressive disclosure - loading detailed information only when needed to optimize context usage.

### Quick Stats

- **Total Skills:** 330
- **Categories:** 32

### Recently Added (2026-05-05)

Three external skill collections were ingested and placed under their domain categories:

- **Trail of Bits Skills Marketplace** (73 skills) → `security/` (audit, static analysis, supply-chain, semgrep, yara, trailmark code-graph), `blockchain-web3/` (per-chain vulnerability scanners, audit-prep, dimensional analysis), `testing-qa/` (fuzzing — aflpp, libfuzzer, libafl, ossfuzz, ruzzy, atheris, address-sanitizer, mutation-testing, property-based-testing, harness-writing, coverage-analysis, wycheproof), `languages/` (c-review, modern-python, fp-check), `developer-tools/` (skill-improver, designing-workflow-skills, second-opinion, ask-questions-if-underspecified, devcontainer-setup, git-cleanup, dwarf-expert, debug-buttercup, differential-review, claude-in-chrome-troubleshooting), `other/` (interpreting-culture-index, let-fate-decide).
- **Android Skills (Google)** (7 skills) → `mobile-development/` with `android-` prefix: edge-to-edge, navigation-3, r8-analyzer, play-billing-upgrade, migrate-xml-to-compose, agp-9-upgrade, xr-jetpack-compose-glimmer.
- **Marketing Skills (Corey Haines)** (40 skills) → `marketing/`: SEO, CRO, content, copy, paid-ads, analytics, lifecycle, and growth skills built around a shared `product-marketing-context` foundation document.

Seven new prompt-engineering techniques (AG-37 through AG-43) were registered in `techniques/MASTER_TECHNIQUE_INDEX.md` based on patterns these skills introduce: Description-as-Trigger Discipline, Sibling-Skill Cross-Reference, Foundation Context Document Pattern, Numbered Phase Discipline, External-Model Second Opinion, Tool-Call Scale Test, and Iterative Skill-Improver Loop.
- **Skills with Bundled Resources:** 55 (32%)

### Progressive Disclosure Architecture

Skills use a three-tier loading system for efficient context management:

1. **Metadata** (name + description) - Always loaded (~100 words)
2. **SKILL.md body** - Loaded when skill triggers (<5k words)
3. **Bundled resources** - Loaded as needed by Claude (scripts, references, assets)

This architecture minimizes context window usage while maximizing capability.

## Table of Contents

**By Category:**
- [Accessibility](#accessibility) (2 skills)
- [Backend Development](#backend-development) (13 skills)
- [Blockchain Web3](#blockchain-web3) (16 skills)
- [Business](#business) (3 skills)
- [Cicd Automation](#cicd-automation) (4 skills)
- [Cloud Infrastructure](#cloud-infrastructure) (14 skills)
- [Content Creation](#content-creation) (5 skills)
- [Creative](#creative) (2 skills)
- [Data Engineering](#data-engineering) (10 skills)
- [Developer Tools](#developer-tools) (35 skills)
- [Devops](#devops) (3 skills)
- [Document Processing](#document-processing) (7 skills)
- [Education](#education) (2 skills)
- [Financial Records](#financial-records) (4 skills)
- [Framework Migration](#framework-migration) (4 skills)
- [Game Development](#game-development) (2 skills)
- [Healthcare](#healthcare) (11 skills)
- [Languages](#languages) (18 skills)
- [Llm Application Dev](#llm-application-dev) (10 skills)
- [Marketing](#marketing) (41 skills)
- [Ml Ai](#ml-ai) (4 skills)
- [Mobile Development](#mobile-development) (36 skills)
- [Observability](#observability) (5 skills)
- [Other](#other) (2 skills)
- [Payments](#payments) (4 skills)
- [Research](#research) (2 skills)
- [Security](#security) (36 skills)
- [Seo Marketing](#seo-marketing) (4 skills)
- [Skills](#skills) (3 skills)
- [Testing Qa](#testing-qa) (18 skills)
- [Web Development](#web-development) (8 skills)
- [Writing](#writing) (2 skills)


## Source Attribution

These skills are sourced from:
- **[wshobson/agents](https://github.com/wshobson/agents)** - 107 skills (MIT License)
- **[daymade/claude-code-skills](https://github.com/daymade/claude-code-skills)** - 25 skills (MIT License)

## How to Use This Index

1. **Browse by category** to find skills for your domain
2. **Check bundled resources** to see what tools/references are included
3. **Review dependencies** to ensure you have required tools
4. **Install skills** by copying to your Claude Code skills directory
5. **Reference skills** in your prompts or let agents auto-invoke them

---

## Skills by Category

### Accessibility

**2 skills in this category**

#### `screen-reader-testing`

- **Path:** `skills/accessibility/screen-reader-testing/`
- **Description:** Test web applications with screen readers including VoiceOver, NVDA, and JAWS. Use when validating screen reader compatibility, debugging accessibility issues, or ensuring assistive technology support.
- **Resources:** SKILL.md only
- **Dependencies:** aws, go, java
- **When to use:** Use when building or improving testing infrastructure

#### `wcag-audit-patterns`

- **Path:** `skills/accessibility/wcag-audit-patterns/`
- **Description:** Conduct WCAG 2.2 accessibility audits with automated testing, manual verification, and remediation guidance. Use when auditing websites for accessibility, fixing WCAG violations, or implementing accessible design patterns.
- **Resources:** SKILL.md only
- **Dependencies:** aws, go, java, react
- **When to use:** Use when building or improving testing infrastructure

### Backend Development

**13 skills in this category**

#### `api-design-principles`

- **Path:** `skills/backend-development/api-design-principles/`
- **Description:** Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers. Use when designing new APIs, reviewing API specifications, or establishing API design standards.
- **Resources:** 2 references, 2 assets
- **Dependencies:** go, graphql, node, python, rest (+1 more)
- **When to use:** Use when designing or implementing APIs

#### `architecture-decision-records`

- **Path:** `skills/backend-development/architecture-decision-records/`
- **Description:** Write and maintain Architecture Decision Records (ADRs) following best practices for technical decision documentation. Use when documenting significant technical decisions, reviewing past architectural choices, or establishing decision processes.
- **Resources:** SKILL.md only
- **Dependencies:** aws, elasticsearch, git, github, go (+7 more)
- **When to use:** Use when working in this domain

#### `architecture-patterns`

- **Path:** `skills/backend-development/architecture-patterns/`
- **Description:** Implement proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design. Use when architecting complex backend systems or refactoring existing applications for better maintainability.
- **Resources:** SKILL.md only
- **Dependencies:** go, postgresql, python, redis, rest
- **When to use:** Use when applying design patterns or architectural patterns

#### `cqrs-implementation`

- **Path:** `skills/backend-development/cqrs-implementation/`
- **Description:** Implement Command Query Responsibility Segregation for scalable architectures. Use when separating read and write models, optimizing query performance, or building event-sourced systems.
- **Resources:** SKILL.md only
- **Dependencies:** azure, python
- **When to use:** Use when working in this domain

#### `event-store-design`

- **Path:** `skills/backend-development/event-store-design/`
- **Description:** Design and implement event stores for event-sourced systems. Use when building event sourcing infrastructure, choosing event store technologies, or implementing event persistence patterns.
- **Resources:** SKILL.md only
- **Dependencies:** aws, azure, go, kafka, postgresql (+2 more)
- **When to use:** Use when applying design patterns or architectural patterns

#### `fastapi-templates`

- **Path:** `skills/backend-development/fastapi-templates/`
- **Description:** Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. Use when building new FastAPI applications or setting up backend API projects.
- **Resources:** SKILL.md only
- **Dependencies:** docker, go, mongodb, postgresql, pytest (+2 more)
- **When to use:** Use when designing or implementing APIs

#### `hono-edge-patterns`

- **Path:** `skills/backend-development/hono-edge-patterns/`
- **Description:** Master Hono framework for building ultra-fast, lightweight web applications on edge runtimes. Use this skill when building APIs for Cloudflare Workers, Deno Deploy, Bun, Vercel Edge, or when users mention "Hono", "edge runtime", "Cloudflare Workers", "Deno Deploy", "ultrafast API", or "edge functions".
- **Resources:** 2 references, 2 assets
- **Dependencies:** java, next.js, node, npm, pnpm (+1 more)
- **When to use:** Use when setting up deployment pipelines

#### `microservices-patterns`

- **Path:** `skills/backend-development/microservices-patterns/`
- **Description:** Design microservices architectures with service boundaries, event-driven communication, and resilience patterns. Use when building distributed systems, decomposing monoliths, or implementing microservices.
- **Resources:** SKILL.md only
- **Dependencies:** graphql, grpc, kafka, python, rabbitmq (+2 more)
- **When to use:** Use when applying design patterns or architectural patterns

#### `openapi-spec-generation`

- **Path:** `skills/backend-development/openapi-spec-generation/`
- **Description:** Generate and maintain OpenAPI 3.1 specifications from code, design-first specs, and validation patterns. Use when creating API documentation, generating SDKs, or ensuring API contract compliance.
- **Resources:** SKILL.md only
- **Dependencies:** go, java, npm, python, rest
- **When to use:** Use when designing or implementing APIs

#### `projection-patterns`

- **Path:** `skills/backend-development/projection-patterns/`
- **Description:** Build read models and projections from event streams. Use when implementing CQRS read sides, building materialized views, or optimizing query performance in event-sourced systems.
- **Resources:** SKILL.md only
- **Dependencies:** azure, elasticsearch, go, python, rest
- **When to use:** Use when working in this domain

#### `saga-orchestration`

- **Path:** `skills/backend-development/saga-orchestration/`
- **Description:** Implement saga patterns for distributed transactions and cross-aggregate workflows. Use when coordinating multi-step business processes, handling compensating transactions, or managing long-running workflows.
- **Resources:** SKILL.md only
- **Dependencies:** python
- **When to use:** Use when applying design patterns or architectural patterns

#### `temporal-python-testing`

- **Path:** `skills/backend-development/temporal-python-testing/`
- **Description:** Test Temporal workflows with pytest, time-skipping, and mocking strategies. Covers unit testing, integration testing, replay testing, and local development setup. Use when implementing Temporal workflow tests or debugging test failures.
- **Resources:** SKILL.md only
- **Dependencies:** docker, git, github, pytest, python
- **When to use:** Use when building or improving testing infrastructure

#### `workflow-orchestration-patterns`

- **Path:** `skills/backend-development/workflow-orchestration-patterns/`
- **Description:** Design durable workflows with Temporal for distributed systems. Covers workflow vs activity separation, saga patterns, state management, and determinism constraints. Use when building long-running processes, distributed transactions, or microservice orchestration.
- **Resources:** SKILL.md only
- **Dependencies:** go, kafka, rest
- **When to use:** Use when applying design patterns or architectural patterns

### Blockchain Web3

**4 skills in this category**

#### `defi-protocol-templates`

- **Path:** `skills/blockchain-web3/defi-protocol-templates/`
- **Description:** Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and lending systems. Use when building decentralized finance applications or smart contract protocols.
- **Resources:** SKILL.md only
- **Dependencies:** go
- **When to use:** Use when working in this domain

#### `nft-standards`

- **Path:** `skills/blockchain-web3/nft-standards/`
- **Description:** Implement NFT standards (ERC-721, ERC-1155) with proper metadata handling, minting strategies, and marketplace integration. Use when creating NFT contracts, building NFT marketplaces, or implementing digital asset systems.
- **Resources:** SKILL.md only
- **Dependencies:** git
- **When to use:** Use when working in this domain

#### `solidity-security`

- **Path:** `skills/blockchain-web3/solidity-security/`
- **Description:** Master smart contract security best practices to prevent common vulnerabilities and implement secure Solidity patterns. Use when writing smart contracts, auditing existing contracts, or implementing security measures for blockchain applications.
- **Resources:** SKILL.md only
- **Dependencies:** aws, java, rust
- **When to use:** Use when implementing security measures or auditing

#### `web3-testing`

- **Path:** `skills/blockchain-web3/web3-testing/`
- **Description:** Test smart contracts comprehensively using Hardhat and Foundry with unit tests, integration tests, and mainnet forking. Use when testing Solidity contracts, setting up blockchain test suites, or validating DeFi protocols.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, java, node (+1 more)
- **When to use:** Use when building or improving testing infrastructure

### Cicd Automation

**4 skills in this category**

#### `deployment-pipeline-design`

- **Path:** `skills/cicd-automation/deployment-pipeline-design/`
- **Description:** Design multi-stage CI/CD pipelines with approval gates, security checks, and deployment orchestration. Use when architecting deployment workflows, setting up continuous delivery, or implementing GitOps practices.
- **Resources:** SKILL.md only
- **Dependencies:** azure, docker, git, github, gitlab (+4 more)
- **When to use:** Use when implementing security measures or auditing

#### `github-actions-templates`

- **Path:** `skills/cicd-automation/github-actions-templates/`
- **Description:** Create production-ready GitHub Actions workflows for automated testing, building, and deploying applications. Use when setting up CI/CD with GitHub Actions, automating development workflows, or creating reusable workflow templates.
- **Resources:** SKILL.md only
- **Dependencies:** aws, docker, git, github, gitlab (+5 more)
- **When to use:** Use when building or improving testing infrastructure

#### `gitlab-ci-patterns`

- **Path:** `skills/cicd-automation/gitlab-ci-patterns/`
- **Description:** Build GitLab CI/CD pipelines with multi-stage workflows, caching, and distributed runners for scalable automation. Use when implementing GitLab CI/CD, optimizing pipeline performance, or setting up automated testing and deployment.
- **Resources:** SKILL.md only
- **Dependencies:** docker, git, github, gitlab, kubernetes (+4 more)
- **When to use:** Use when building or improving testing infrastructure

#### `secrets-management`

- **Path:** `skills/cicd-automation/secrets-management/`
- **Description:** Implement secure secrets management for CI/CD pipelines using Vault, AWS Secrets Manager, or native platform solutions. Use when handling sensitive credentials, rotating secrets, or securing CI/CD environments.
- **Resources:** SKILL.md only
- **Dependencies:** aws, azure, docker, gcp, git (+7 more)
- **When to use:** Use when setting up deployment pipelines

### Cloud Infrastructure

**14 skills in this category**

#### `cost-optimization`

- **Path:** `skills/cloud-infrastructure/cost-optimization/`
- **Description:** Optimize cloud costs through resource rightsizing, tagging strategies, reserved instances, and spending analysis. Use when reducing cloud expenses, analyzing infrastructure costs, or implementing cost governance policies.
- **Resources:** SKILL.md only
- **Dependencies:** aws, azure, gcp, go, terraform
- **When to use:** Use when working in this domain

#### `firebase-project-scaffolding`

- **Path:** `skills/cloud-infrastructure/firebase-project-scaffolding/`
- **Description:** Scaffold a new Firebase project with production-grade defaults including auth-required security rules, cost budget alerts, App Check configuration, Emulator Suite setup, CI/CD pipeline for rules deployment, and multi-environment support. Use this skill when creating a new Firebase project, initializing Firebase in an Android app, setting up Firebase infrastructure from scratch, or when a developer mentions 'new Firebase project', 'Firebase init', 'Firebase setup', or 'production Firebase config'.
- **Resources:** SKILL.md only
- **Dependencies:** gcp, git, github, go, node (+2 more)
- **When to use:** Use when implementing security measures or auditing

#### `firebase-rules-testing`

- **Path:** `skills/cloud-infrastructure/firebase-rules-testing/`
- **Description:** Automated Firebase security rules testing workflow covering test case generation from rules, emulator-based execution, access control validation for all user roles, common vulnerability checks, and coverage reporting. Use this skill when testing Firestore or RTDB security rules, when rules change before deployment, when auditing security rule coverage, or when a developer mentions 'rules test', 'security rules testing', 'emulator test', or 'rules coverage'.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, java, jest, node (+2 more)
- **When to use:** Use when building or improving testing infrastructure

#### `gitops-workflow`

- **Path:** `skills/cloud-infrastructure/gitops-workflow/`
- **Description:** Implement GitOps workflows with ArgoCD and Flux for automated, declarative Kubernetes deployments with continuous reconciliation. Use when implementing GitOps practices, automating Kubernetes deployments, or setting up declarative infrastructure management.
- **Resources:** 2 references
- **Dependencies:** aws, git, github, go, kubernetes
- **When to use:** Use when setting up deployment pipelines

#### `helm-chart-scaffolding`

- **Path:** `skills/cloud-infrastructure/helm-chart-scaffolding/`
- **Description:** Design, organize, and manage Helm charts for templating and packaging Kubernetes applications with reusable configurations. Use when creating Helm charts, packaging Kubernetes applications, or implementing templated deployments.
- **Resources:** 1 scripts, 1 references, 2 assets
- **Dependencies:** aws, docker, git, github, go (+4 more)
- **When to use:** Use when setting up deployment pipelines

#### `hybrid-cloud-networking`

- **Path:** `skills/cloud-infrastructure/hybrid-cloud-networking/`
- **Description:** Configure secure, high-performance connectivity between on-premises infrastructure and cloud platforms using VPN and dedicated connections. Use when building hybrid cloud architectures, connecting data centers to cloud, or implementing secure cross-premises networking.
- **Resources:** SKILL.md only
- **Dependencies:** aws, azure, gcp, terraform
- **When to use:** Use when working in this domain

#### `istio-traffic-management`

- **Path:** `skills/cloud-infrastructure/istio-traffic-management/`
- **Description:** Configure Istio traffic management including routing, load balancing, circuit breakers, and canary deployments. Use when implementing service mesh traffic policies, progressive delivery, or resilience patterns.
- **Resources:** SKILL.md only
- **When to use:** Use when setting up deployment pipelines

#### `k8s-manifest-generator`

- **Path:** `skills/cloud-infrastructure/k8s-manifest-generator/`
- **Description:** Create production-ready Kubernetes manifests for Deployments, Services, ConfigMaps, and Secrets following best practices and security standards. Use when generating Kubernetes YAML manifests, creating K8s resources, or implementing production-grade Kubernetes configurations.
- **Resources:** 2 references, 3 assets
- **Dependencies:** aws, git, go, kubernetes, node
- **When to use:** Use when implementing security measures or auditing

#### `k8s-security-policies`

- **Path:** `skills/cloud-infrastructure/k8s-security-policies/`
- **Description:** Implement Kubernetes security policies including NetworkPolicy, PodSecurityPolicy, and RBAC for production-grade security. Use when securing Kubernetes clusters, implementing network isolation, or enforcing pod security standards.
- **Resources:** 1 references, 1 assets
- **Dependencies:** git, go, kubernetes, node, rest
- **When to use:** Use when implementing security measures or auditing

#### `linkerd-patterns`

- **Path:** `skills/cloud-infrastructure/linkerd-patterns/`
- **Description:** Implement Linkerd service mesh patterns for lightweight, security-focused service mesh deployments. Use when setting up Linkerd, configuring traffic policies, or implementing zero-trust networking with minimal overhead.
- **Resources:** SKILL.md only
- **Dependencies:** go, kubernetes, rust
- **When to use:** Use when implementing security measures or auditing

#### `mtls-configuration`

- **Path:** `skills/cloud-infrastructure/mtls-configuration/`
- **Description:** Configure mutual TLS (mTLS) for zero-trust service-to-service communication. Use when implementing zero-trust networking, certificate management, or securing internal service communication.
- **Resources:** SKILL.md only
- **Dependencies:** go, kubernetes, mysql, node, rest (+1 more)
- **When to use:** Use when working in this domain

#### `multi-cloud-architecture`

- **Path:** `skills/cloud-infrastructure/multi-cloud-architecture/`
- **Description:** Design multi-cloud architectures using a decision framework to select and integrate services across AWS, Azure, and GCP. Use when building multi-cloud systems, avoiding vendor lock-in, or leveraging best-of-breed services from multiple providers.
- **Resources:** SKILL.md only
- **Dependencies:** aws, azure, gcp, go, kafka (+6 more)
- **When to use:** Use when working in this domain

#### `service-mesh-observability`

- **Path:** `skills/cloud-infrastructure/service-mesh-observability/`
- **Description:** Implement comprehensive observability for service meshes including distributed tracing, metrics, and visualization. Use when setting up mesh monitoring, debugging latency issues, or implementing SLOs for service communication.
- **Resources:** SKILL.md only
- **Dependencies:** go, grpc, kubernetes, node
- **When to use:** Use when working in this domain

#### `terraform-module-library`

- **Path:** `skills/cloud-infrastructure/terraform-module-library/`
- **Description:** Build reusable Terraform modules for AWS, Azure, and GCP infrastructure following infrastructure-as-code best practices. Use when creating infrastructure modules, standardizing cloud provisioning, or implementing reusable IaC components.
- **Resources:** 1 references
- **Dependencies:** aws, azure, gcp, git, github (+2 more)
- **When to use:** Use when working in this domain

### Content Creation

**5 skills in this category**

#### `cli-demo-generator`

- **Path:** `skills/content-creation/cli-demo-generator/`
- **Description:** This skill should be used when users want to create animated CLI demos, terminal recordings, or command-line demonstration GIFs. It supports both manual tape file creation and automated demo generation from command descriptions. Use when users mention creating demos, recording terminal sessions, or generating animated GIFs of CLI workflows.
- **Resources:** 3 scripts, 2 references, 3 assets
- **Dependencies:** git, github, go, npm
- **When to use:** Use when working in this domain

#### `teams-channel-post-writer`

- **Path:** `skills/content-creation/teams-channel-post-writer/`
- **Description:** Creates educational Teams channel posts for internal knowledge sharing about Claude Code features, tools, and best practices. Applies when writing posts, announcements, or documentation to teach colleagues effective Claude Code usage, announce new features, share productivity tips, or document lessons learned. Provides templates, writing guidelines, and structured approaches emphasizing concrete examples, underlying principles, and connections to best practices like context engineering. Activates for content involving Teams posts, channel announcements, feature documentation, or tip sharing.
- **Resources:** 1 references, 1 assets
- **Dependencies:** git, go, react, rest, rust
- **When to use:** Use when working in this domain

#### `transcript-fixer`

- **Path:** `skills/content-creation/transcript-fixer/`
- **Description:** Corrects speech-to-text transcription errors in meeting notes, lectures, and interviews using dictionary rules and AI. Learns patterns to build personalized correction databases. Use when working with transcripts containing ASR/STT errors, homophones, or Chinese/English mixed content requiring cleanup.
- **Resources:** 52 scripts, 14 references, 2 other files
- **Dependencies:** python
- **When to use:** Use when applying design patterns or architectural patterns

#### `video-comparer`

- **Path:** `skills/content-creation/video-comparer/`
- **Description:** This skill should be used when comparing two videos to analyze compression results or quality differences. Generates interactive HTML reports with quality metrics (PSNR, SSIM) and frame-by-frame visual comparisons. Triggers when users mention "compare videos", "video quality", "compression analysis", "before/after compression", or request quality assessment of compressed videos.
- **Resources:** 1 scripts, 3 references, 1 assets, 1 other files
- **Dependencies:** go, python, rust
- **When to use:** Use when working in this domain

#### `youtube-downloader`

- **Path:** `skills/content-creation/youtube-downloader/`
- **Description:** Download YouTube videos and HLS streams (m3u8) from platforms like Mux, Vimeo, etc. using yt-dlp and ffmpeg. Use this skill when users request downloading videos, extracting audio, handling protected streams with authentication headers, or troubleshooting download issues like nsig extraction failures, 403 errors, or cookie extraction problems.
- **Resources:** 1 scripts, 1 references, 1 other files
- **Dependencies:** git, github, go, python, rest
- **When to use:** Use when working in this domain

### Data Engineering

**10 skills in this category**

#### `airflow-dag-patterns`

- **Path:** `skills/data-engineering/airflow-dag-patterns/`
- **Description:** Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment. Use when creating data pipelines, orchestrating workflows, or scheduling batch jobs.
- **Resources:** SKILL.md only
- **Dependencies:** aws, docker, pytest, python
- **When to use:** Use when building or improving testing infrastructure

#### `backtesting-frameworks`

- **Path:** `skills/data-engineering/backtesting-frameworks/`
- **Description:** Build robust backtesting systems for trading strategies with proper handling of look-ahead bias, survivorship bias, and transaction costs. Use when developing trading algorithms, validating strategies, or building backtesting infrastructure.
- **Resources:** SKILL.md only
- **Dependencies:** go, python
- **When to use:** Use when building or improving testing infrastructure

#### `data-quality-frameworks`

- **Path:** `skills/data-engineering/data-quality-frameworks/`
- **Description:** Implement data quality validation with Great Expectations, dbt tests, and data contracts. Use when building data quality pipelines, implementing validation rules, or establishing data contracts.
- **Resources:** SKILL.md only
- **Dependencies:** go, python
- **When to use:** Use when building or improving testing infrastructure

#### `data-storytelling`

- **Path:** `skills/data-engineering/data-storytelling/`
- **Description:** Transform data into compelling narratives using visualization, context, and persuasive structure. Use when presenting analytics to stakeholders, creating data reports, or building executive presentations.
- **Resources:** SKILL.md only
- **Dependencies:** go, python
- **When to use:** Use when working in this domain

#### `dbt-transformation-patterns`

- **Path:** `skills/data-engineering/dbt-transformation-patterns/`
- **Description:** Master dbt (data build tool) for analytics engineering with model organization, testing, documentation, and incremental strategies. Use when building data transformations, creating data models, or implementing analytics engineering best practices.
- **Resources:** SKILL.md only
- **Dependencies:** git, node
- **When to use:** Use when building or improving testing infrastructure

#### `kpi-dashboard-design`

- **Path:** `skills/data-engineering/kpi-dashboard-design/`
- **Description:** Design effective KPI dashboards with metrics selection, visualization best practices, and real-time monitoring patterns. Use when building business dashboards, selecting metrics, or designing data visualization layouts.
- **Resources:** SKILL.md only
- **Dependencies:** go, python
- **When to use:** Use when applying design patterns or architectural patterns

#### `ml-pipeline-workflow`

- **Path:** `skills/data-engineering/ml-pipeline-workflow/`
- **Description:** Build end-to-end MLOps pipelines from data preparation through model training, validation, and production deployment. Use when creating ML pipelines, implementing MLOps practices, or automating model training and deployment workflows.
- **Resources:** SKILL.md only
- **Dependencies:** aws, azure, gcp, go, kubernetes (+1 more)
- **When to use:** Use when setting up deployment pipelines

#### `postgresql`

- **Path:** `skills/data-engineering/postgresql/`
- **Description:** Design a PostgreSQL-specific schema. Covers best-practices, data types, indexing, constraints, performance patterns, and advanced features
- **Resources:** SKILL.md only
- **Dependencies:** go, mysql, postgresql, rest
- **When to use:** Use when applying design patterns or architectural patterns

#### `risk-metrics-calculation`

- **Path:** `skills/data-engineering/risk-metrics-calculation/`
- **Description:** Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementing risk limits, or building risk monitoring systems.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, python, rest
- **When to use:** Use when working in this domain

#### `spark-optimization`

- **Path:** `skills/data-engineering/spark-optimization/`
- **Description:** Optimize Apache Spark jobs with partitioning, caching, shuffle optimization, and memory tuning. Use when improving Spark performance, debugging slow jobs, or scaling data processing pipelines.
- **Resources:** SKILL.md only
- **Dependencies:** go, python
- **When to use:** Use when working in this domain

### Developer Tools

**24 skills in this category**

#### `auth-implementation-patterns`

- **Path:** `skills/developer-tools/auth-implementation-patterns/`
- **Description:** Master authentication and authorization patterns including JWT, OAuth2, session management, and RBAC to build secure, scalable access control systems. Use when implementing auth systems, securing APIs, or debugging security issues.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, graphql, java (+4 more)
- **When to use:** Use when implementing security measures or auditing

#### `bazel-build-optimization`

- **Path:** `skills/developer-tools/bazel-build-optimization/`
- **Description:** Optimize Bazel builds for large-scale monorepos. Use when configuring Bazel, implementing remote execution, or optimizing build performance for enterprise codebases.
- **Resources:** SKILL.md only
- **Dependencies:** docker, git, github, grpc, java (+6 more)
- **When to use:** Use when working in this domain

#### `changelog-automation`

- **Path:** `skills/developer-tools/changelog-automation/`
- **Description:** Automate changelog generation from commits, PRs, and releases following Keep a Changelog format. Use when setting up release workflows, generating release notes, or standardizing commit conventions.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, gitlab, go, java (+6 more)
- **When to use:** Use when working in this domain

#### `code-review-excellence`

- **Path:** `skills/developer-tools/code-review-excellence/`
- **Description:** Master effective code review practices to provide constructive feedback, catch bugs early, and foster knowledge sharing while maintaining team morale. Use when reviewing pull requests, establishing review standards, or mentoring developers.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, gitlab, go, java (+2 more)
- **When to use:** Use when working in this domain

#### `debugging-strategies`

- **Path:** `skills/developer-tools/debugging-strategies/`
- **Description:** Master systematic debugging techniques, profiling tools, and root cause analysis to efficiently track down bugs across any codebase or technology stack. Use when investigating bugs, performance issues, or unexpected behavior.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, java, jest (+3 more)
- **When to use:** Use when working in this domain

#### `dependency-audit`

- **Path:** `skills/developer-tools/dependency-audit/`
- **Description:** Audits project dependencies for security vulnerabilities, license compliance, outdated packages, and supply chain risks. Activates when reviewing dependencies, checking for CVEs, analyzing package.json/requirements.txt/go.mod/Cargo.toml, or planning dependency upgrades across any language ecosystem.
- **Resources:** 1 scripts, 2 references
- **Dependencies:** gh cli, git, github, go, graphql (+7 more)
- **When to use:** Use when implementing security measures or auditing

#### `e2e-testing-patterns`

- **Path:** `skills/developer-tools/e2e-testing-patterns/`
- **Description:** Master end-to-end testing with Playwright and Cypress to build reliable test suites that catch bugs, improve confidence, and enable fast deployment. Use when implementing E2E tests, debugging flaky tests, or establishing testing standards.
- **Resources:** SKILL.md only
- **Dependencies:** go, node, npm
- **When to use:** Use when building or improving testing infrastructure

#### `error-handling-patterns`

- **Path:** `skills/developer-tools/error-handling-patterns/`
- **Description:** Master error handling patterns across languages including exceptions, Result types, error propagation, and graceful degradation to build resilient applications. Use when implementing error handling, designing APIs, or improving application reliability.
- **Resources:** SKILL.md only
- **Dependencies:** go, java, python, rest, rust
- **When to use:** Use when designing or implementing APIs

#### `external-prompt-kit-ingestor`

- **Path:** `skills/developer-tools/external-prompt-kit-ingestor/`
- **Description:** Use this skill whenever an external prompt kit, prompt collection, or article-with-embedded-prompts is dropped into this repository (any markdown/PDF/text file containing one or more pasteable prompts that didn't originate here). Splits the source into individually structured Tier-1 prompt files, registers any net-new techniques in the master technique index, organizes outputs into the correct domain directory (creating new ones when justified), updates PROMPT_INDEX.json and PROMPT_INDEX.md, leaves a back-pointer in the source, and reports implications. Trigger phrases: "process this kit", "ingest this prompt collection", "we got a new prompt pack", "import these external prompts", "extract prompts from this article".
- **Resources:** 3 references
- **Dependencies:** go
- **When to use:** Use when working in this domain

#### `git-advanced-workflows`

- **Path:** `skills/developer-tools/git-advanced-workflows/`
- **Description:** Master advanced Git workflows including rebasing, cherry-picking, bisect, worktrees, and reflog to maintain clean history and recover from any situation. Use when managing complex Git histories, collaborating on feature branches, or troubleshooting repository issues.
- **Resources:** SKILL.md only
- **Dependencies:** git, go, npm, rest
- **When to use:** Use when working in this domain

#### `github-ops`

- **Path:** `skills/developer-tools/github-ops/`
- **Description:** Provides comprehensive GitHub operations using gh CLI and GitHub API. Activates when working with pull requests, issues, repositories, workflows, or GitHub API operations including creating/viewing/merging PRs, managing issues, querying API endpoints, and handling GitHub workflows in enterprise or public GitHub environments.
- **Resources:** 5 references
- **Dependencies:** gh cli, git, github, graphql, rest
- **When to use:** Use when designing or implementing APIs

#### `grounding-agent`

- **Path:** `skills/developer-tools/grounding-agent/`
- **Description:** Always-on cognitive guardrail that prevents blind instruction-following, scope drift, and unexamined assumptions during development sessions. Challenges both user instructions and AI-generated ideas against upstream/downstream impacts, project coherence, and reversibility before execution. Use this skill when working with users who give rapid-fire instructions, during complex multi-file changes, when scope feels like it's expanding, or when users mention 'stay grounded', 'check my thinking', 'am I going off track', 'does this make sense', or 'sanity check'.
- **Resources:** 2 references
- **Dependencies:** go, rest
- **When to use:** Use when designing or implementing APIs

#### `monorepo-management`

- **Path:** `skills/developer-tools/monorepo-management/`
- **Description:** Master monorepo management with Turborepo, Nx, and pnpm workspaces to build efficient, scalable multi-package repositories with optimized builds and dependency management. Use when setting up monorepos, optimizing builds, or managing shared dependencies.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, java, jest, next.js (+5 more)
- **When to use:** Use when working in this domain

#### `nx-workspace-patterns`

- **Path:** `skills/developer-tools/nx-workspace-patterns/`
- **Description:** Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or implementing affected commands.
- **Resources:** SKILL.md only
- **Dependencies:** aws, git, github, jest, node (+2 more)
- **When to use:** Use when working in this domain

#### `repomix-safe-mixer`

- **Path:** `skills/developer-tools/repomix-safe-mixer/`
- **Description:** Safely package codebases with repomix by automatically detecting and removing hardcoded credentials before packing. Use when packaging code for distribution, creating reference packages, or when the user mentions security concerns about sharing code with repomix.
- **Resources:** 2 scripts, 1 references
- **Dependencies:** aws, git, go, java, python
- **When to use:** Use when implementing security measures or auditing

#### `repomix-unmixer`

- **Path:** `skills/developer-tools/repomix-unmixer/`
- **Description:** Extracts files from repomix-packed repositories, restoring original directory structures from XML/Markdown/JSON formats. Activates when users need to unmix repomix files, extract packed repositories, restore file structures from repomix output, or reverse the repomix packing process.
- **Resources:** 1 scripts, 2 references
- **Dependencies:** git, github, go, python, rest
- **When to use:** Use when working in this domain

#### `session-history-finder`

- **Path:** `skills/developer-tools/session-history-finder/`
- **Description:** Finds and recovers content from Claude Code session history files. This skill should be used when searching for deleted files, tracking changes across sessions, analyzing conversation history, or recovering code from previous interactions. Triggers include mentions of "session history", "recover deleted", "find in history", "previous conversation", or ".claude/projects".
- **Resources:** 2 scripts, 2 references, 2 other files
- **Dependencies:** go, python
- **When to use:** Use when working in this domain

#### `skill-creator`

- **Path:** `skills/developer-tools/skill-creator/`
- **Description:** Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
- **Resources:** 4 scripts, 2 other files
- **Dependencies:** git, go, python, react, rest
- **When to use:** Use when working in this domain

#### `skills-search`

- **Path:** `skills/developer-tools/skills-search/`
- **Description:** This skill should be used when users want to search, discover, install, or manage Claude Code skills from the CCPM registry. Triggers include requests like "find skills for PDF", "search for code review skills", "install cloudflare-troubleshooting", "list my installed skills", "what does skill-creator do", or any mention of finding/installing/managing Claude Code skills or plugins.
- **Resources:** 1 other files
- **Dependencies:** npm, react, rest
- **When to use:** Use when working in this domain

#### `solo-dev-decision-log`

- **Path:** `skills/developer-tools/solo-dev-decision-log/`
- **Description:** Lightweight Architecture Decision Record (ADR) system for solo developers. Generates and maintains numbered markdown decision records in a decisions/ directory. Emphasizes speed (under 5 minutes per decision) and communication with your future self. Use this skill when making technology choices, architecture trade-offs, or any 'why did I do it this way?' decisions, or when a developer mentions 'ADR', 'decision log', 'why did I choose', 'document decision', or 'architecture decision'.
- **Resources:** SKILL.md only
- **Dependencies:** aws, git, github, go
- **When to use:** Use when working in this domain

#### `solo-dev-self-review`

- **Path:** `skills/developer-tools/solo-dev-self-review/`
- **Description:** Structured self-code-review workflow for solo developers who have no team reviewers. Provides checklists, perspective-switching techniques, diff-based review patterns, and blind spot detection to catch bugs the original author's brain glosses over. Use this skill when reviewing your own code before merging, after a vibe coding session, before a release, or when a developer mentions 'self review', 'no reviewer', 'solo developer', or 'review my own code'.
- **Resources:** SKILL.md only
- **Dependencies:** git, go
- **When to use:** Use when applying design patterns or architectural patterns

#### `sql-optimization-patterns`

- **Path:** `skills/developer-tools/sql-optimization-patterns/`
- **Description:** Master SQL query optimization, indexing strategies, and EXPLAIN analysis to dramatically improve database performance and eliminate slow queries. Use when debugging slow queries, designing database schemas, or optimizing application performance.
- **Resources:** SKILL.md only
- **Dependencies:** go, mysql, postgresql, python
- **When to use:** Use when working in this domain

#### `statusline-generator`

- **Path:** `skills/developer-tools/statusline-generator/`
- **Description:** Configures and customizes Claude Code statuslines with multi-line layouts, cost tracking via ccusage, git status indicators, and customizable colors. Activates for statusline setup, installation, configuration, customization, color changes, cost display, git status integration, or troubleshooting statusline issues.
- **Resources:** 2 scripts, 2 references
- **Dependencies:** git, java, rest
- **When to use:** Use when working in this domain

#### `turborepo-caching`

- **Path:** `skills/developer-tools/turborepo-caching/`
- **Description:** Configure Turborepo for efficient monorepo builds with local and remote caching. Use when setting up Turborepo, optimizing build pipelines, or implementing distributed caching.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, jest, node, npm
- **When to use:** Use when working in this domain

### Devops

**3 skills in this category**

#### `incident-runbook-templates`

- **Path:** `skills/devops/incident-runbook-templates/`
- **Description:** Create structured incident response runbooks with step-by-step procedures, escalation paths, and recovery actions. Use when building runbooks, responding to incidents, or establishing incident response procedures.
- **Resources:** SKILL.md only
- **Dependencies:** go, kubernetes, postgresql
- **When to use:** Use when working in this domain

#### `on-call-handoff-patterns`

- **Path:** `skills/devops/on-call-handoff-patterns/`
- **Description:** Master on-call shift handoffs with context transfer, escalation procedures, and documentation. Use when transitioning on-call responsibilities, documenting shift summaries, or improving on-call processes.
- **Resources:** SKILL.md only
- **Dependencies:** go, kubernetes, node, redis, rest
- **When to use:** Use when working in this domain

#### `postmortem-writing`

- **Path:** `skills/devops/postmortem-writing/`
- **Description:** Write effective blameless postmortems with root cause analysis, timelines, and action items. Use when conducting incident reviews, writing postmortem documents, or improving incident response processes.
- **Resources:** SKILL.md only
- **Dependencies:** go, java
- **When to use:** Use when working in this domain

### Document Processing

**7 skills in this category**

#### `config-progressive-disclosure`

- **Path:** `skills/document-processing/config-progressive-disclosure/`
- **Description:** Optimize user CLAUDE.md files by applying progressive disclosure principles. This skill should be used when users want to reduce CLAUDE.md bloat, move detailed content to references, extract reusable patterns into skills, or improve context efficiency. Triggers include "optimize CLAUDE.md", "reduce CLAUDE.md size", "apply progressive disclosure", or complaints about CLAUDE.md being too long.
- **Resources:** 1 references, 1 other files
- **Dependencies:** go
- **When to use:** Use when applying design patterns or architectural patterns

#### `docs-cleaner`

- **Path:** `skills/document-processing/docs-cleaner/`
- **Description:** Consolidates redundant documentation while preserving all valuable content. This skill should be used when users want to clean up documentation bloat, merge redundant docs, reduce documentation sprawl, or consolidate multiple files covering the same topic. Triggers include "clean up docs", "consolidate documentation", "too many doc files", "merge these docs", or when documentation exceeds 500 lines across multiple files covering similar topics.
- **Resources:** 1 references, 1 other files
- **Dependencies:** go, rest
- **When to use:** Use when working in this domain

#### `markdown-tools`

- **Path:** `skills/document-processing/markdown-tools/`
- **Description:** Converts documents to markdown (PDFs, Word docs, PowerPoint, Confluence exports) with Windows/WSL path handling. Activates when converting .doc/.docx/PDF/PPTX files to markdown, processing Confluence exports, handling Windows/WSL path conversions, or working with markitdown utility.
- **Resources:** 1 scripts, 1 references
- **Dependencies:** python
- **When to use:** Use when working in this domain

#### `mermaid-tools`

- **Path:** `skills/document-processing/mermaid-tools/`
- **Description:** Extracts Mermaid diagrams from markdown files and generates high-quality PNG images using bundled scripts. Activates when working with Mermaid diagrams, converting diagrams to PNG, extracting diagrams from markdown, or processing markdown files with embedded Mermaid code.
- **Resources:** 3 scripts, 1 references
- **Dependencies:** go, python
- **When to use:** Use when working in this domain

#### `ocr-pdf-creator`

- **Path:** `skills/document-processing/ocr-pdf-creator/`
- **Description:** Converts scanned or image-based PDF documents into searchable PDFs using OCR (Optical Character Recognition). This skill should be used when processing scanned textbook pages, frozen ink documents, photographed documents, or any PDF containing images of text rather than actual text. Triggers include "make PDF searchable", "OCR this PDF", "extract text from scanned PDF", "recognize text in PDF", "convert image PDF to text", "frozen ink", or "textbook page scan".
- **Resources:** 2 scripts, 1 references
- **Dependencies:** git, go, python, rest
- **When to use:** Use when working in this domain

#### `pdf-creator`

- **Path:** `skills/document-processing/pdf-creator/`
- **Description:** Create PDF documents from markdown with proper Chinese font support using weasyprint. This skill should be used when converting markdown to PDF, generating formal documents (legal, trademark filings, reports), or when Chinese typography is required. Triggers include "convert to PDF", "generate PDF", "markdown to PDF", or any request for creating printable documents.
- **Resources:** 2 scripts, 1 other files
- **Dependencies:** python
- **When to use:** Use when working in this domain

#### `ppt-creator`

- **Path:** `skills/document-processing/ppt-creator/`
- **Description:** Create professional slide decks from topics or documents. Generates structured content with data-driven charts, speaker notes, and complete PPTX files. Applies persuasive storytelling principles (Pyramid Principle, assertion-evidence). Supports multiple formats (Marp, PowerPoint). Use for presentations, pitches, slide decks, or keynotes.
- **Resources:** 1 scripts, 11 references
- **Dependencies:** go, python
- **When to use:** Use when working in this domain

### Framework Migration

**4 skills in this category**

#### `angular-migration`

- **Path:** `skills/framework-migration/angular-migration/`
- **Description:** Migrate from AngularJS to Angular using hybrid mode, incremental component rewriting, and dependency injection updates. Use when upgrading AngularJS applications, planning framework migrations, or modernizing legacy Angular code.
- **Resources:** SKILL.md only
- **Dependencies:** angular, go, java, react, rest
- **When to use:** Use when working in this domain

#### `database-migration`

- **Path:** `skills/framework-migration/database-migration/`
- **Description:** Execute database migrations across ORMs and platforms with zero-downtime strategies, data transformation, and rollback procedures. Use when migrating databases, changing schemas, performing data transformations, or implementing zero-downtime deployment strategies.
- **Resources:** SKILL.md only
- **Dependencies:** java, mysql, npm, postgresql, rest
- **When to use:** Use when setting up deployment pipelines

#### `dependency-upgrade`

- **Path:** `skills/framework-migration/dependency-upgrade/`
- **Description:** Manage major dependency version upgrades with compatibility analysis, staged rollout, and comprehensive testing. Use when upgrading framework versions, updating major dependencies, or managing breaking changes in libraries.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, java, npm, react (+2 more)
- **When to use:** Use when building or improving testing infrastructure

#### `react-modernization`

- **Path:** `skills/framework-migration/react-modernization/`
- **Description:** Upgrade React applications to latest versions, migrate from class components to hooks, and adopt concurrent features. Use when modernizing React codebases, migrating to React Hooks, or upgrading to latest React versions.
- **Resources:** SKILL.md only
- **Dependencies:** go, java, node, npm, react
- **When to use:** Use when building or improving testing infrastructure

### Game Development

**2 skills in this category**

#### `godot-gdscript-patterns`

- **Path:** `skills/game-development/godot-gdscript-patterns/`
- **Description:** Master Godot 4 GDScript patterns including signals, scenes, state machines, and optimization. Use when building Godot games, implementing game systems, or learning GDScript best practices.
- **Resources:** SKILL.md only
- **Dependencies:** go, node
- **When to use:** Use when applying design patterns or architectural patterns

#### `unity-ecs-patterns`

- **Path:** `skills/game-development/unity-ecs-patterns/`
- **Description:** Master Unity ECS (Entity Component System) with DOTS, Jobs, and Burst for high-performance game development. Use when building data-oriented games, optimizing performance, or working with large entity counts.
- **Resources:** SKILL.md only
- **Dependencies:** git, github
- **When to use:** Use when working in this domain

### Languages

**15 skills in this category**

#### `async-python-patterns`

- **Path:** `skills/languages/async-python-patterns/`
- **Description:** Master Python asyncio, concurrent programming, and async/await patterns for high-performance applications. Use when building async APIs, concurrent systems, or I/O-bound applications requiring non-blocking operations.
- **Resources:** SKILL.md only
- **Dependencies:** go, mongodb, postgresql, pytest, python
- **When to use:** Use when designing or implementing APIs

#### `bash-defensive-patterns`

- **Path:** `skills/languages/bash-defensive-patterns/`
- **Description:** Master defensive Bash programming techniques for production-grade scripts. Use when writing robust shell scripts, CI/CD pipelines, or system utilities requiring fault tolerance and safety.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, node, python
- **When to use:** Use when setting up deployment pipelines

#### `bats-testing-patterns`

- **Path:** `skills/languages/bats-testing-patterns/`
- **Description:** Master Bash Automated Testing System (Bats) for comprehensive shell script testing. Use when writing tests for shell scripts, CI/CD pipelines, or requiring test-driven development of shell utilities.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, node, npm
- **When to use:** Use when building or improving testing infrastructure

#### `go-concurrency-patterns`

- **Path:** `skills/languages/go-concurrency-patterns/`
- **Description:** Master Go concurrency with goroutines, channels, sync primitives, and context. Use when building concurrent Go applications, implementing worker pools, or debugging race conditions.
- **Resources:** SKILL.md only
- **Dependencies:** go
- **When to use:** Use when working in this domain

#### `javascript-testing-patterns`

- **Path:** `skills/languages/javascript-testing-patterns/`
- **Description:** Implement comprehensive testing strategies using Jest, Vitest, and Testing Library for unit tests, integration tests, and end-to-end testing with mocking, fixtures, and test-driven development. Use when writing JavaScript/TypeScript tests, setting up test infrastructure, or implementing TDD/BDD workflows.
- **Resources:** SKILL.md only
- **Dependencies:** java, jest, node, react, rest (+2 more)
- **When to use:** Use when building or improving testing infrastructure

#### `memory-safety-patterns`

- **Path:** `skills/languages/memory-safety-patterns/`
- **Description:** Implement memory-safe programming with RAII, ownership, smart pointers, and resource management across Rust, C++, and C. Use when writing safe systems code, managing resources, or preventing memory bugs.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, java, node (+1 more)
- **When to use:** Use when working in this domain

#### `modern-javascript-patterns`

- **Path:** `skills/languages/modern-javascript-patterns/`
- **Description:** Master ES6+ features including async/await, destructuring, spread operators, arrow functions, promises, modules, iterators, generators, and functional programming patterns for writing clean, efficient JavaScript code. Use when refactoring legacy code, implementing modern patterns, or optimizing JavaScript applications.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, java, rest
- **When to use:** Use when applying design patterns or architectural patterns

#### `nodejs-backend-patterns`

- **Path:** `skills/languages/nodejs-backend-patterns/`
- **Description:** Build production-ready Node.js backend services with Express/Fastify, implementing middleware patterns, error handling, authentication, database integration, and API design best practices. Use when creating Node.js servers, REST APIs, GraphQL backends, or microservices architectures.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, graphql, java (+5 more)
- **When to use:** Use when designing or implementing APIs

#### `python-packaging`

- **Path:** `skills/languages/python-packaging/`
- **Description:** Create distributable Python packages with proper project structure, setup.py/pyproject.toml, and publishing to PyPI. Use when packaging Python libraries, creating CLI tools, or distributing Python code.
- **Resources:** SKILL.md only
- **Dependencies:** aws, git, github, go, pytest (+1 more)
- **When to use:** Use when working in this domain

#### `python-performance-optimization`

- **Path:** `skills/languages/python-performance-optimization/`
- **Description:** Profile and optimize Python code using cProfile, memory profilers, and performance best practices. Use when debugging slow Python code, optimizing bottlenecks, or improving application performance.
- **Resources:** SKILL.md only
- **Dependencies:** go, pytest, python, rust
- **When to use:** Use when working in this domain

#### `python-testing-patterns`

- **Path:** `skills/languages/python-testing-patterns/`
- **Description:** Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. Use when writing Python tests, setting up test suites, or implementing testing best practices.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, mysql, postgresql (+2 more)
- **When to use:** Use when building or improving testing infrastructure

#### `rust-async-patterns`

- **Path:** `skills/languages/rust-async-patterns/`
- **Description:** Master Rust async programming with Tokio, async traits, error handling, and concurrent patterns. Use when building async Rust applications, implementing concurrent systems, or debugging async code.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, rust
- **When to use:** Use when applying design patterns or architectural patterns

#### `shellcheck-configuration`

- **Path:** `skills/languages/shellcheck-configuration/`
- **Description:** Master ShellCheck static analysis configuration and usage for shell script quality. Use when setting up linting infrastructure, fixing code issues, or ensuring script portability.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, gitlab
- **When to use:** Use when working in this domain

#### `typescript-advanced-types`

- **Path:** `skills/languages/typescript-advanced-types/`
- **Description:** Master TypeScript's advanced type system including generics, conditional types, mapped types, template literals, and utility types for building type-safe applications. Use when implementing complex type logic, creating reusable type utilities, or ensuring compile-time type safety in TypeScript projects.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, java
- **When to use:** Use when working in this domain

#### `uv-package-manager`

- **Path:** `skills/languages/uv-package-manager/`
- **Description:** Master the uv package manager for fast Python dependency management, virtual environments, and modern Python project workflows. Use when setting up Python projects, managing dependencies, or optimizing Python development workflows with uv.
- **Resources:** SKILL.md only
- **Dependencies:** docker, git, github, go, pytest (+2 more)
- **When to use:** Use when working in this domain

### Llm Application Dev

**10 skills in this category**

#### `embedding-strategies`

- **Path:** `skills/llm-application-dev/embedding-strategies/`
- **Description:** Select and optimize embedding models for semantic search and RAG applications. Use when choosing embedding models, implementing chunking strategies, or optimizing embedding quality for specific domains.
- **Resources:** SKILL.md only
- **Dependencies:** python
- **When to use:** Use when working in this domain

#### `langchain-architecture`

- **Path:** `skills/llm-application-dev/langchain-architecture/`
- **Description:** Design LLM applications using the LangChain framework with agents, memory, and tool integration patterns. Use when building LangChain applications, implementing AI agents, or creating complex LLM workflows.
- **Resources:** SKILL.md only
- **Dependencies:** pytest, python, react
- **When to use:** Use when applying design patterns or architectural patterns

#### `langchain-optimization`

- **Path:** `skills/llm-application-dev/langchain-optimization/`
- **Description:** Optimize LangChain applications for performance, cost, and reliability. Use when debugging slow chains, reducing token costs, profiling memory usage, improving agent reliability, or troubleshooting LangChain workflows. Triggers on "LangChain slow", "chain performance", "reduce LLM costs", "debug agent", "memory issues", "optimize chains".
- **Resources:** 2 scripts, 3 references, 1 assets
- **Dependencies:** pytest, python, redis
- **When to use:** Use when working in this domain

#### `llm-evaluation`

- **Path:** `skills/llm-application-dev/llm-evaluation/`
- **Description:** Implement comprehensive evaluation strategies for LLM applications using automated metrics, human feedback, and benchmarking. Use when testing LLM performance, measuring AI application quality, or establishing evaluation frameworks.
- **Resources:** SKILL.md only
- **Dependencies:** go, python
- **When to use:** Use when building or improving testing infrastructure

#### `llm-icon-finder`

- **Path:** `skills/llm-application-dev/llm-icon-finder/`
- **Description:** Finding and accessing AI/LLM model brand icons from lobe-icons library. Use when users need icon URLs, want to download brand logos for AI models/providers/applications (Claude, GPT, Gemini, etc.), or request icons in SVG/PNG/WEBP formats.
- **Resources:** 2 references
- **Dependencies:** git, github, go, java, npm (+1 more)
- **When to use:** Use when working in this domain

#### `prompt-engineering-patterns`

- **Path:** `skills/llm-application-dev/prompt-engineering-patterns/`
- **Description:** Master advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability in production. Use when optimizing prompts, improving LLM outputs, or designing production prompt templates.
- **Resources:** 1 scripts, 5 references, 2 assets
- **Dependencies:** python
- **When to use:** Use when working in this domain

#### `prompt-optimizer`

- **Path:** `skills/llm-application-dev/prompt-optimizer/`
- **Description:** Transform vague prompts into precise, well-structured specifications using EARS (Easy Approach to Requirements Syntax) methodology. This skill should be used when users provide loose requirements, ambiguous feature descriptions, or need to enhance prompts for AI-generated code, products, or documents. Triggers include requests to "optimize my prompt", "improve this requirement", "make this more specific", or when raw requirements lack detail and structure.
- **Resources:** 4 references, 1 other files
- **Dependencies:** go, rust
- **When to use:** Use when working in this domain

#### `promptfoo-evaluation`

- **Path:** `skills/llm-application-dev/promptfoo-evaluation/`
- **Description:** Configures and runs LLM evaluation using Promptfoo framework. Use when setting up prompt testing, creating evaluation configs (promptfooconfig.yaml), writing Python custom assertions, implementing llm-rubric for LLM-as-judge, or managing few-shot examples in prompts. Triggers on keywords like "promptfoo", "eval", "LLM evaluation", "prompt testing", or "model comparison".
- **Resources:** 1 references, 1 other files
- **Dependencies:** go, python
- **When to use:** Use when building or improving testing infrastructure

#### `rag-architecture`

- **Path:** `skills/llm-application-dev/rag-architecture/`
- **Description:** Design and optimize Retrieval-Augmented Generation (RAG) systems for production LLM applications. Covers end-to-end RAG architecture including chunking strategies, retrieval patterns, reranking, prompt engineering, and evaluation metrics. Use when building knowledge-grounded AI, document Q&A systems, or optimizing existing RAG quality. Triggers on "RAG", "chunking strategy", "retrieval evaluation", "MRR", "NDCG", "recall@k", "reranking", "document Q&A".
- **Resources:** SKILL.md only
- **Dependencies:** go, python
- **When to use:** Use when applying design patterns or architectural patterns

#### `vector-search-optimization`

- **Path:** `skills/llm-application-dev/vector-search-optimization/`
- **Description:** Implement and optimize vector database search for production systems. Covers vector DB implementations (Pinecone, Qdrant, pgvector, Weaviate, Elasticsearch), HNSW index tuning, quantization strategies, hybrid search with keyword fusion, and performance benchmarking. Use when building semantic search, tuning vector indexes, implementing hybrid search, or scaling to millions of vectors. Triggers on "vector database", "HNSW tuning", "quantization", "hybrid search", "RRF", "similarity search", "pgvector", "Pinecone", "Qdrant".
- **Resources:** SKILL.md only
- **Dependencies:** aws, elasticsearch, node, postgresql, python (+1 more)
- **When to use:** Use when working in this domain

### Marketing

**1 skills in this category**

#### `app-launch-campaign`

- **Path:** `skills/marketing/app-launch-campaign/`
- **Description:** End-to-end launch campaign orchestrator -- generates all assets, timeline, and day-by-day playbook for solo app developers launching on the Google Play Store with zero budget.
- **Resources:** SKILL.md only
- **Dependencies:** go, rust
- **When to use:** Use when working in this domain

### Mobile Development

**27 skills in this category**

#### `android-accessibility-testing`

- **Path:** `skills/mobile-development/android-accessibility-testing/`
- **Description:** Android-specific accessibility testing using ADB, Accessibility Scanner, TalkBack, and programmatic checks. Covers content descriptions, touch targets, color contrast, focus order, Compose semantics, and Play Store accessibility requirements. Use this skill when auditing app accessibility, fixing TalkBack issues, checking touch target sizes, verifying color contrast, or when a developer mentions 'accessibility', 'TalkBack', 'content description', 'touch target', 'a11y', or 'screen reader'.
- **Resources:** SKILL.md only
- **Dependencies:** go, node
- **When to use:** Use when building or improving testing infrastructure

#### `android-adb-operations`

- **Path:** `skills/mobile-development/android-adb-operations/`
- **Description:** Comprehensive ADB command reference and workflow guide for device management, app installation, debugging, log capture, file transfer, shell operations, intent testing, and screen capture. Use this skill when working with ADB, connecting devices, installing APKs, reading logcat, pushing/pulling files, testing deep links, capturing screenshots, or when a developer mentions 'adb', 'logcat', 'device not found', 'install APK', or 'wireless debugging'.
- **Resources:** SKILL.md only
- **Dependencies:** go, rest
- **When to use:** Use when building or improving testing infrastructure

#### `android-adb-profiling`

- **Path:** `skills/mobile-development/android-adb-profiling/`
- **Description:** ADB-based performance profiling workflows for CPU, memory, battery, network, and GPU rendering. Covers systrace/perfetto capture, dumpsys analysis, startup time measurement, and StrictMode configuration — all from the command line without Android Studio Profiler. Use this skill when profiling app performance, investigating jank, measuring startup time, debugging memory leaks, analyzing battery drain, or when a developer mentions 'dumpsys', 'systrace', 'perfetto', 'jank', 'frame drops', or 'memory leak'.
- **Resources:** SKILL.md only
- **Dependencies:** docker, go, java, python
- **When to use:** Use when working in this domain

#### `android-admob-mediation`

- **Path:** `skills/mobile-development/android-admob-mediation/`
- **Description:** Integrates Google AdMob with mediation adapters, UMP consent management for GDPR/CCPA, ad format selection (banner, interstitial, rewarded, native, app open), Compose ad wrappers, and subscriber ad suppression. Activates when implementing ads, ad mediation, consent management, or coordinating ad display with subscription entitlements in Android apps.
- **Resources:** 2 references
- **Dependencies:** go
- **When to use:** Use when working in this domain

#### `android-app-survey`

- **Path:** `skills/mobile-development/android-app-survey/`
- **Description:** Systematic survey methodology for mapping Android application structure, screens, features, navigation flows, and tech stack into a categorized feature map. Use this skill when performing a behavior audit survey, mapping app features to code, onboarding to an unfamiliar Android codebase, or when users mention 'survey the app', 'map the features', 'what screens does this app have', or 'understand app structure'.
- **Resources:** 1 references
- **Dependencies:** go, rest
- **When to use:** Use when working in this domain

#### `android-behavior-audit`

- **Path:** `skills/mobile-development/android-behavior-audit/`
- **Description:** Behavioral scrutiny methodology for evaluating whether Android app code behavior matches developer intent, with structured finding classification (Likely Bug, Suspicious Pattern, Design Question, Confirmed Correct) and calibrated confidence scoring. Use this skill when auditing app behavior against intent, identifying behavioral discrepancies, classifying code issues by confidence, or when users mention 'behavior audit', 'does this code make sense', 'behavioral scrutiny', or 'intent vs actual behavior'.
- **Resources:** 2 references
- **Dependencies:** go, rest
- **When to use:** Use when applying design patterns or architectural patterns

#### `android-behavior-fix-planning`

- **Path:** `skills/mobile-development/android-behavior-fix-planning/`
- **Description:** Fix planning and implementation methodology for resolving behavioral discrepancies in Android apps, including blast radius estimation, dependency ordering, minimal-change implementation, and post-fix verification. Use this skill when planning fixes for behavior audit findings, estimating fix complexity, ordering fix dependencies, or when users mention 'plan the fix', 'fix behavioral issues', 'implement audit fixes', or 'verify fix correctness'.
- **Resources:** 1 references
- **Dependencies:** go, rest
- **When to use:** Use when working in this domain

#### `android-behavior-trace`

- **Path:** `skills/mobile-development/android-behavior-trace/`
- **Description:** Deep code path tracing methodology for Android applications that follows user actions through all architectural layers (UI → ViewModel → Repository → Data → Network/Background) and produces a factual behavior catalog. Use this skill when tracing feature behavior across code layers, creating a behavior audit list, documenting what code actually does, or when users mention 'trace the code', 'what does this feature actually do', 'behavior catalog', or 'follow the code path'.
- **Resources:** 1 references
- **Dependencies:** react, rest
- **When to use:** Use when working in this domain

#### `android-crash-triage`

- **Path:** `skills/mobile-development/android-crash-triage/`
- **Description:** Systematic crash investigation workflow covering reproduction from stack traces, device/OS isolation, root cause analysis for ANRs, OOMs, and native crashes, and fix production with regression tests. Use this skill when triaging production crashes, investigating Crashlytics reports, diagnosing ANRs, debugging OOM errors, or when a developer mentions 'crash', 'ANR', 'stack trace', 'Crashlytics', or 'production issue'.
- **Resources:** SKILL.md only
- **Dependencies:** go
- **When to use:** Use when building or improving testing infrastructure

#### `android-deep-link-architect`

- **Path:** `skills/mobile-development/android-deep-link-architect/`
- **Description:** Design and validate deep link architecture covering App Links verification, intent filters, Navigation component integration, deferred deep links, and link testing automation. Use this skill when implementing deep linking, setting up App Links, configuring intent filters, handling deferred deep links, or when a developer mentions 'deep link', 'App Links', 'intent filter', 'assetlinks.json', or 'deferred deep link'.
- **Resources:** SKILL.md only
- **Dependencies:** go, node
- **When to use:** Use when building or improving testing infrastructure

#### `android-emulator-management`

- **Path:** `skills/mobile-development/android-emulator-management/`
- **Description:** Android emulator setup, configuration, snapshot management, headless CI execution, and multi-device testing. Covers avdmanager, emulator CLI, Gradle Managed Devices, CI-specific configurations, and emulator console commands. Use this skill when creating AVDs, configuring emulators for CI, managing snapshots, running headless emulators, setting up multi-device testing, or when a developer mentions 'emulator', 'AVD', 'headless', 'Gradle Managed Devices', or 'emulator not booting'.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, java, node (+2 more)
- **When to use:** Use when building or improving testing infrastructure

#### `android-firebase-sync-validator`

- **Path:** `skills/mobile-development/android-firebase-sync-validator/`
- **Description:** Validates that Android app data properly syncs to Firebase (Realtime Database, Firestore, and Cloud Functions) by analyzing app features, identifying sync requirements, verifying cloud infrastructure completeness, and automatically correcting issues. Creates and maintains a persistent map of data points and their cloud rules. Use this skill when working with Android Firebase apps, troubleshooting sync issues, auditing Firebase rules, ensuring data protection, or when users mention "Firebase sync validation", "check Firebase rules", "Firebase data not syncing", "validate cloud functions", or "audit Firebase security".
- **Resources:** 3 scripts, 4 references, 3 assets
- **Dependencies:** go, java, npm, python, rest
- **When to use:** Use when implementing security measures or auditing

#### `android-hilt-di`

- **Path:** `skills/mobile-development/android-hilt-di/`
- **Description:** Master Hilt dependency injection for Android including module design, scoping, ViewModel integration, and testing with Hilt. Use this skill when setting up dependency injection, creating Hilt modules, scoping dependencies, integrating with ViewModel, or when users mention "Hilt", "dependency injection", "@Inject", "@Module", "@Provides", "@HiltViewModel", "Dagger", or "DI setup".
- **Resources:** SKILL.md only
- **Dependencies:** go, java
- **When to use:** Use when building or improving testing infrastructure

#### `android-multi-source-data-layer`

- **Path:** `skills/mobile-development/android-multi-source-data-layer/`
- **Description:** Architectural patterns for Android apps that coordinate data across Room (local cache/offline), Firebase Realtime Database (real-time sync), and Firestore (structured queries) through a unified repository layer. Activates when designing or troubleshooting data layer architecture for apps using multiple Firebase backends with local caching, offline-first patterns, conflict resolution, or data routing decisions.
- **Resources:** 3 references
- **Dependencies:** java, rest
- **When to use:** Use when applying design patterns or architectural patterns

#### `android-play-billing-subscriptions`

- **Path:** `skills/mobile-development/android-play-billing-subscriptions/`
- **Description:** Implements Google Play Billing Library 7+ for in-app purchases and subscriptions. Covers BillingClient lifecycle, purchase flows, subscription state machine (active/grace period/on-hold/paused/cancelled/expired), server-side receipt validation via Cloud Functions, paywall UI in Compose, and testing with Play Console test tracks. Activates when implementing billing, subscriptions, paywalls, or in-app purchases for Android apps.
- **Resources:** 2 references
- **Dependencies:** go, rest
- **When to use:** Use when building or improving testing infrastructure

#### `android-quarterly-maintenance`

- **Path:** `skills/mobile-development/android-quarterly-maintenance/`
- **Description:** Comprehensive quarterly maintenance workflow covering dependencies, security, performance, Play Store compliance, Firebase costs, and technical debt. Use this skill when performing quarterly maintenance reviews, preparing for major releases, conducting end-of-quarter health checks, or when a solo Android developer mentions 'quarterly review', 'maintenance cycle', 'dependency updates', 'Play Store compliance check', 'Firebase cost review', or 'tech debt assessment'.
- **Resources:** SKILL.md only
- **Dependencies:** go, java, rest
- **When to use:** Use when implementing security measures or auditing

#### `android-release-pipeline`

- **Path:** `skills/mobile-development/android-release-pipeline/`
- **Description:** End-to-end Android release workflow covering version bumping, changelog generation, signing config verification, ProGuard/R8 rules validation, bundle generation, and Play Console upload preparation. Use this skill when preparing a release build, when automating the release process, when verifying release readiness, or when a developer mentions 'release build', 'version bump', 'Play Console upload', 'signing config', or 'changelog generation'.
- **Resources:** SKILL.md only
- **Dependencies:** git, go, java
- **When to use:** Use when working in this domain

#### `android-rich-notification-system`

- **Path:** `skills/mobile-development/android-rich-notification-system/`
- **Description:** Comprehensive Android notification system covering FCM integration, notification channels per feature, rich notifications with actions and media, geofence-triggered location reminders, in-app messaging, and Android 13+ runtime permission handling. Activates when implementing push notifications, local notifications, notification channels, geofence reminders, or handling POST_NOTIFICATIONS permission for apps with messaging, calendars, reminders, and alerts.
- **Resources:** 3 references
- **Dependencies:** git, go, java, rest
- **When to use:** Use when working in this domain

#### `android-room-database`

- **Path:** `skills/mobile-development/android-room-database/`
- **Description:** Master Room persistence library for Android including entity design, DAO patterns, migrations, type converters, and Flow/coroutines integration. Use this skill when working with local databases in Android, implementing data persistence, creating database migrations, or when users mention "Room database", "Room migration", "DAO", "Entity", "@Database", "type converter", or "database schema".
- **Resources:** SKILL.md only
- **Dependencies:** go, java, react
- **When to use:** Use when applying design patterns or architectural patterns

#### `android-screenshot-testing`

- **Path:** `skills/mobile-development/android-screenshot-testing/`
- **Description:** Screenshot-based UI testing for Android using ADB screen capture, Compose Preview Screenshot Testing, Paparazzi, and Roborazzi. Covers baseline capture, diff comparison, CI integration, and handling intentional UI changes. Use this skill when setting up visual regression testing, comparing UI across configurations, catching unintentional layout changes, or when a developer mentions 'screenshot testing', 'visual regression', 'Paparazzi', 'Roborazzi', or 'UI diff'.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, java
- **When to use:** Use when building or improving testing infrastructure

#### `android-testing-patterns`

- **Path:** `skills/mobile-development/android-testing-patterns/`
- **Description:** Master Android testing including unit tests, instrumented tests, Compose testing, and end-to-end testing with Espresso, MockK, and Robolectric. Use this skill when writing tests for Android apps, testing ViewModels, testing Compose UIs, or when users mention "unit test", "instrumented test", "Espresso", "Compose testing", "MockK", "Robolectric", "test coverage", or "Android testing".
- **Resources:** SKILL.md only
- **Dependencies:** go, java, node, rust
- **When to use:** Use when building or improving testing infrastructure

#### `iOS-APP-developer`

- **Path:** `skills/mobile-development/iOS-APP-developer/`
- **Description:** Develops iOS applications with XcodeGen, SwiftUI, and SPM. Triggers on XcodeGen project.yml configuration, SPM dependency issues, device deployment problems, code signing errors, camera/AVFoundation debugging, iOS version compatibility, or "Library not loaded @rpath" framework errors. Use when building iOS apps, fixing Xcode build failures, or deploying to real devices.
- **Resources:** 4 references, 1 other files
- **Dependencies:** git, github, go, rest, rust
- **When to use:** Use when setting up deployment pipelines

#### `jetpack-compose-patterns`

- **Path:** `skills/mobile-development/jetpack-compose-patterns/`
- **Description:** Master Jetpack Compose UI development with modern patterns including state management, navigation, theming, and Material 3 implementation. Use this skill when building Android UIs with Compose, implementing state hoisting, creating custom components, setting up navigation, or when users mention "Compose UI", "Compose state", "remember", "LaunchedEffect", "Material 3", or "Compose navigation".
- **Resources:** SKILL.md only
- **Dependencies:** go, react
- **When to use:** Use when applying design patterns or architectural patterns

#### `mobile-ui-element-audit`

- **Path:** `skills/mobile-development/mobile-ui-element-audit/`
- **Description:** Perform hyper-detailed, pixel-level audits of individual mobile UI elements analyzing visual design, interaction states, micro-animations, accessibility, engagement potential, and platform compliance. Produces scored assessments with prioritized improvement plans and exact implementation specifications. Use this skill when auditing a button, navigation bar, card, input, modal, list, header, or any specific UI element, or when a developer mentions 'UI audit', 'element review', 'polish this component', 'make this button better', 'improve this card', or 'pixel perfect'.
- **Resources:** 1 references
- **Dependencies:** go, react, rest
- **When to use:** Use when working in this domain

#### `mobile-ui-habit-loop-design`

- **Path:** `skills/mobile-development/mobile-ui-habit-loop-design/`
- **Description:** Design habit-forming engagement systems for mobile apps using the Hook Model, Fogg Behavior Model, gamification science, and behavioral psychology. Covers trigger design, core loop architecture, streak mechanics, variable rewards, progress systems, social proof, and retention features with implementation guidance. Use this skill when designing engagement loops, adding streaks or gamification, improving retention, implementing reward systems, or when a developer mentions 'habit loop', 'engagement', 'retention', 'streak', 'gamification', 'daily active users', 'hook model', or 'addictive'.
- **Resources:** 1 references
- **Dependencies:** git, github, go, react, rest
- **When to use:** Use when working in this domain

#### `mobile-ui-micro-interactions`

- **Path:** `skills/mobile-development/mobile-ui-micro-interactions/`
- **Description:** Design and implement delightful micro-interactions for mobile apps including touch feedback, transitions, loading states, celebration animations, haptic patterns, and state change animations. Covers both iOS (SwiftUI/UIKit) and Android (Compose/View) with production-ready code. Use this skill when designing animations, adding touch feedback, creating loading states, implementing pull-to-refresh, building celebration effects, or when a developer mentions 'micro-interaction', 'animation', 'haptic feedback', 'transition', 'pull-to-refresh', 'skeleton loading', or 'delight'.
- **Resources:** 1 references
- **Dependencies:** aws, rest
- **When to use:** Use when applying design patterns or architectural patterns

#### `react-native-architecture`

- **Path:** `skills/mobile-development/react-native-architecture/`
- **Description:** Build production React Native apps with Expo, navigation, native modules, offline sync, and cross-platform patterns. Use when developing mobile apps, implementing native integrations, or architecting React Native projects.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, node, react (+1 more)
- **When to use:** Use when applying design patterns or architectural patterns

### Observability

**5 skills in this category**

#### `distributed-tracing`

- **Path:** `skills/observability/distributed-tracing/`
- **Description:** Implement distributed tracing with Jaeger and Tempo to track requests across microservices and identify performance bottlenecks. Use when debugging microservices, analyzing request flows, or implementing observability for distributed systems.
- **Resources:** SKILL.md only
- **Dependencies:** aws, docker, elasticsearch, git, github (+7 more)
- **When to use:** Use when working in this domain

#### `grafana-dashboards`

- **Path:** `skills/observability/grafana-dashboards/`
- **Description:** Create and manage production Grafana dashboards for real-time visualization of system and application metrics. Use when building monitoring dashboards, visualizing metrics, or creating operational observability interfaces.
- **Resources:** SKILL.md only
- **Dependencies:** node, rest, terraform
- **When to use:** Use when working in this domain

#### `opentelemetry-setup`

- **Path:** `skills/observability/opentelemetry-setup/`
- **Description:** Master OpenTelemetry for implementing distributed tracing, metrics, and logging in cloud-native applications. Use this skill when setting up observability infrastructure, debugging distributed systems, or when users mention "OpenTelemetry", "OTel", "distributed tracing", "spans", "traces", "telemetry", "OTLP", or "observability".
- **Resources:** 1 scripts, 2 references, 2 assets
- **Dependencies:** docker, go, grpc, java, node (+3 more)
- **When to use:** Use when working in this domain

#### `prometheus-configuration`

- **Path:** `skills/observability/prometheus-configuration/`
- **Description:** Set up Prometheus for comprehensive metric collection, storage, and monitoring of infrastructure and applications. Use when implementing metrics collection, setting up monitoring infrastructure, or configuring alerting systems.
- **Resources:** SKILL.md only
- **Dependencies:** docker, git, github, kubernetes, node
- **When to use:** Use when working in this domain

#### `slo-implementation`

- **Path:** `skills/observability/slo-implementation/`
- **Description:** Define and implement Service Level Indicators (SLIs) and Service Level Objectives (SLOs) with error budgets and alerting. Use when establishing reliability targets, implementing SRE practices, or measuring service performance.
- **Resources:** SKILL.md only
- **Dependencies:** go
- **When to use:** Use when working in this domain

### Payments

**4 skills in this category**

#### `billing-automation`

- **Path:** `skills/payments/billing-automation/`
- **Description:** Build automated billing systems for recurring payments, invoicing, subscription lifecycle, and dunning management. Use when implementing subscription billing, automating invoicing, or managing recurring payment systems.
- **Resources:** SKILL.md only
- **Dependencies:** python, rest
- **When to use:** Use when working in this domain

#### `paypal-integration`

- **Path:** `skills/payments/paypal-integration/`
- **Description:** Integrate PayPal payment processing with support for express checkout, subscriptions, and refund management. Use when implementing PayPal payments, processing online transactions, or building e-commerce checkout flows.
- **Resources:** SKILL.md only
- **Dependencies:** java, python, rest, rust
- **When to use:** Use when working in this domain

#### `pci-compliance`

- **Path:** `skills/payments/pci-compliance/`
- **Description:** Implement PCI DSS compliance requirements for secure handling of payment card data and payment systems. Use when securing payment processing, achieving PCI compliance, or implementing payment card security measures.
- **Resources:** SKILL.md only
- **Dependencies:** git, go, java, python, rest
- **When to use:** Use when implementing security measures or auditing

#### `stripe-integration`

- **Path:** `skills/payments/stripe-integration/`
- **Description:** Implement Stripe payment processing for robust, PCI-compliant payment flows including checkout, subscriptions, and webhooks. Use when integrating Stripe payments, building subscription systems, or implementing secure checkout flows.
- **Resources:** SKILL.md only
- **Dependencies:** java, python
- **When to use:** Use when working in this domain

### Security

**7 skills in this category**

#### `attack-tree-construction`

- **Path:** `skills/security/attack-tree-construction/`
- **Description:** Build comprehensive attack trees to visualize threat paths. Use when mapping attack scenarios, identifying defense gaps, or communicating security risks to stakeholders.
- **Resources:** SKILL.md only
- **Dependencies:** go, node, python
- **When to use:** Use when implementing security measures or auditing

#### `gdpr-data-handling`

- **Path:** `skills/security/gdpr-data-handling/`
- **Description:** Implement GDPR-compliant data handling with consent management, data subject rights, and privacy by design. Use when building systems that process EU personal data, implementing privacy controls, or conducting GDPR compliance reviews.
- **Resources:** SKILL.md only
- **Dependencies:** git, go, java, python, rest
- **When to use:** Use when working in this domain

#### `sast-configuration`

- **Path:** `skills/security/sast-configuration/`
- **Description:** Configure Static Application Security Testing (SAST) tools for automated vulnerability detection in application code. Use when setting up security scanning, implementing DevSecOps practices, or automating code vulnerability detection.
- **Resources:** SKILL.md only
- **Dependencies:** docker, git, github, gitlab, go (+2 more)
- **When to use:** Use when building or improving testing infrastructure

#### `security-requirement-extraction`

- **Path:** `skills/security/security-requirement-extraction/`
- **Description:** Derive security requirements from threat models and business context. Use when translating threats into actionable requirements, creating security user stories, or building security test cases.
- **Resources:** SKILL.md only
- **Dependencies:** go, python, rest
- **When to use:** Use when building or improving testing infrastructure

#### `slsa-compliance`

- **Path:** `skills/security/slsa-compliance/`
- **Description:** Expert knowledge for SLSA (Supply-chain Levels for Software Artifacts) framework compliance. Provides guidance on SBOM generation, provenance attestation, and supply chain security levels. Use this skill when implementing SLSA requirements, generating SBOMs, creating provenance attestations, securing CI/CD pipelines, or when users mention "SLSA", "SBOM", "software supply chain", "provenance", "build attestation", "Sigstore", or "in-toto".
- **Resources:** 2 scripts, 4 references, 1 assets
- **Dependencies:** docker, git, github, gitlab, go (+1 more)
- **When to use:** Use when building or improving testing infrastructure

#### `stride-analysis-patterns`

- **Path:** `skills/security/stride-analysis-patterns/`
- **Description:** Apply STRIDE methodology to systematically identify threats. Use when analyzing system security, conducting threat modeling sessions, or creating security documentation.
- **Resources:** SKILL.md only
- **Dependencies:** azure, git, go, python, rest (+1 more)
- **When to use:** Use when implementing security measures or auditing

#### `threat-mitigation-mapping`

- **Path:** `skills/security/threat-mitigation-mapping/`
- **Description:** Map identified threats to appropriate security controls and mitigations. Use when prioritizing security investments, creating remediation plans, or validating control effectiveness.
- **Resources:** SKILL.md only
- **Dependencies:** aws, go, python, redis, rest
- **When to use:** Use when implementing security measures or auditing

### Testing Qa

**1 skills in this category**

#### `qa-expert`

- **Path:** `skills/testing-qa/qa-expert/`
- **Description:** This skill should be used when establishing comprehensive QA testing processes for any software project. Use when creating test strategies, writing test cases following Google Testing Standards, executing test plans, tracking bugs with P0-P4 classification, calculating quality metrics, or generating progress reports. Includes autonomous execution capability via master prompts and complete documentation templates for third-party QA team handoffs. Implements OWASP security testing and achieves 90% coverage targets.
- **Resources:** 2 scripts, 5 references, 1 assets, 1 other files
- **Dependencies:** go, python, rust
- **When to use:** Use when building or improving testing infrastructure

### Web Development

**8 skills in this category**

#### `astro-development`

- **Path:** `skills/web-development/astro-development/`
- **Description:** Master Astro for building fast, content-focused web applications with islands architecture, multi-framework integration, and optimal performance. Use this skill when building static sites, content-heavy websites, documentation, blogs, marketing pages, or when users mention "Astro", "islands architecture", "partial hydration", "content collections", or "static site generator".
- **Resources:** 2 references, 2 assets
- **Dependencies:** git, github, go, java, next.js (+7 more)
- **When to use:** Use when working in this domain

#### `cloudflare-troubleshooting`

- **Path:** `skills/web-development/cloudflare-troubleshooting/`
- **Description:** Investigate and resolve Cloudflare configuration issues using API-driven evidence gathering. Use when troubleshooting ERR_TOO_MANY_REDIRECTS, SSL errors, DNS issues, or any Cloudflare-related problems. Focus on systematic investigation using Cloudflare API to examine actual configuration rather than making assumptions.
- **Resources:** 2 scripts, 3 references
- **Dependencies:** git, github, go, python
- **When to use:** Use when designing or implementing APIs

#### `nextjs-app-router-patterns`

- **Path:** `skills/web-development/nextjs-app-router-patterns/`
- **Description:** Master Next.js 14+ App Router with Server Components, streaming, parallel routes, and advanced data fetching. Use when building Next.js applications, implementing SSR/SSG, or optimizing React Server Components.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, next.js, node (+1 more)
- **When to use:** Use when working in this domain

#### `qwik-development`

- **Path:** `skills/web-development/qwik-development/`
- **Description:** Master Qwik for building instant-loading web applications with resumability, fine-grained lazy loading, and zero hydration cost. Use this skill when building highly interactive apps requiring instant interactivity, e-commerce sites, dashboards, or when users mention "Qwik", "QwikCity", "resumability", "resumable apps", or "$" dollar sign functions.
- **Resources:** 2 references, 2 assets
- **Dependencies:** git, go, java, node, npm (+5 more)
- **When to use:** Use when working in this domain

#### `react-state-management`

- **Path:** `skills/web-development/react-state-management/`
- **Description:** Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. Use when setting up global state, managing server state, or choosing between state management solutions.
- **Resources:** SKILL.md only
- **Dependencies:** git, github, go, react, rest
- **When to use:** Use when working in this domain

#### `solid-development`

- **Path:** `skills/web-development/solid-development/`
- **Description:** Master SolidJS for building high-performance reactive web applications with fine-grained reactivity, no virtual DOM, and minimal overhead. Use this skill when building highly interactive applications, real-time dashboards, or when users mention "Solid", "SolidJS", "SolidStart", "createSignal", "createStore", "fine-grained reactivity", or "no virtual DOM".
- **Resources:** 2 references, 2 assets
- **Dependencies:** go, java, next.js, node, npm (+4 more)
- **When to use:** Use when building or improving testing infrastructure

#### `tailwind-design-system`

- **Path:** `skills/web-development/tailwind-design-system/`
- **Description:** Build scalable design systems with Tailwind CSS, design tokens, component libraries, and responsive patterns. Use when creating component libraries, implementing design systems, or standardizing UI patterns.
- **Resources:** SKILL.md only
- **Dependencies:** go, node, react
- **When to use:** Use when applying design patterns or architectural patterns

#### `ui-designer`

- **Path:** `skills/web-development/ui-designer/`
- **Description:** Extract design systems from reference UI images and generate implementation-ready UI design prompts. Use when users provide UI screenshots/mockups and want to create consistent designs, generate design systems, or build MVP UIs matching reference aesthetics.
- **Resources:** 3 assets
- **Dependencies:** go, npm, react
- **When to use:** Use when working in this domain

---

## Appendix: Skills with Bundled Resources

These skills include additional scripts, references, or assets beyond SKILL.md:

### api-design-principles
**Category:** Backend Development

**References:** (2 files)
- `rest_best_practices.md`
- `graphql_schema_design.md`

**Assets:** (2 files)
- `rest-api-template.py`
- `api_design_checklist.md`

### hono-edge-patterns
**Category:** Backend Development

**References:** (2 files)
- `deployment.md`
- `middleware.md`

**Assets:** (2 files)
- `wrangler.toml.example`
- `api_patterns.md`

### gitops-workflow
**Category:** Cloud Infrastructure

**References:** (2 files)
- `argocd_setup.md`
- `sync_policies.md`

### helm-chart-scaffolding
**Category:** Cloud Infrastructure

**Scripts:** (1 files)
- `validate-chart.sh`

**References:** (1 files)
- `chart_structure.md`

**Assets:** (2 files)
- `values.yaml.template`
- `Chart.yaml.template`

### k8s-manifest-generator
**Category:** Cloud Infrastructure

**References:** (2 files)
- `service_spec.md`
- `deployment_spec.md`

**Assets:** (3 files)
- `deployment-template.yaml`
- `service-template.yaml`
- `configmap-template.yaml`

### k8s-security-policies
**Category:** Cloud Infrastructure

**References:** (1 files)
- `rbac_patterns.md`

**Assets:** (1 files)
- `network-policy-template.yaml`

### terraform-module-library
**Category:** Cloud Infrastructure

**References:** (1 files)
- `aws_modules.md`

### cli-demo-generator
**Category:** Content Creation

**Scripts:** (3 files)
- `auto_generate_demo.py`
- `record_interactive.sh`
- `batch_generate.py`

**References:** (2 files)
- `vhs_syntax.md`
- `best_practices.md`

**Assets:** (3 files)
- `basic.tape`
- `interactive.tape`
- `batch-config.yaml`

### teams-channel-post-writer
**Category:** Content Creation

**References:** (1 files)
- `writing_guidelines.md`

**Assets:** (1 files)
- `post_template.md`

### transcript-fixer
**Category:** Content Creation

**Scripts:** (52 files)
- `fix_transcript_enhanced.py`
- `check_type_hints.py`
- `ensure_deps.py`
- `fix_transcription.py`
- `__init__.py`
- `generate_word_diff.py`
- `security.py`
- `logging_config.py`
- `db_migrations_cli.py`
- `migrations.py`
- ...and 42 more

**References:** (14 files)
- `quick_reference.md`
- `script_parameters.md`
- `dictionary_guide.md`
- `glm_api_setup.md`
- `sql_queries.md`
- `team_collaboration.md`
- `best_practices.md`
- `architecture.md`
- `file_formats.md`
- `installation_setup.md`
- ...and 4 more

**Other:** (2 files)
- `requirements.txt`
- `.gitignore`

### video-comparer
**Category:** Content Creation

**Scripts:** (1 files)
- `compare.py`

**References:** (3 files)
- `configuration.md`
- `video_metrics.md`
- `ffmpeg_commands.md`

**Assets:** (1 files)
- `template.html`

**Other:** (1 files)
- `.security-scan-passed`

### youtube-downloader
**Category:** Content Creation

**Scripts:** (1 files)
- `download_video.py`

**References:** (1 files)
- `po_token_setup.md`

**Other:** (1 files)
- `.security-scan-passed`

### dependency-audit
**Category:** Developer Tools

**Scripts:** (1 files)
- `audit_summary.sh`

**References:** (2 files)
- `vulnerability_databases.md`
- `license_compatibility_matrix.md`

### external-prompt-kit-ingestor
**Category:** Developer Tools

**References:** (3 files)
- `frontmatter-template.md`
- `technique-promotion-criteria.md`
- `ingestion-checklist.md`

### github-ops
**Category:** Developer Tools

**References:** (5 files)
- `api_reference.md`
- `issue_operations.md`
- `pr_operations.md`
- `best_practices.md`
- `workflow_operations.md`

### grounding-agent
**Category:** Developer Tools

**References:** (2 files)
- `grounding_checklist.md`
- `claude_md_snippet.md`

### repomix-safe-mixer
**Category:** Developer Tools

**Scripts:** (2 files)
- `scan_secrets.py`
- `safe_pack.py`

**References:** (1 files)
- `common_secrets.md`

### repomix-unmixer
**Category:** Developer Tools

**Scripts:** (1 files)
- `unmix_repomix.py`

**References:** (2 files)
- `validation_workflow.md`
- `repomix_format.md`

### session-history-finder
**Category:** Developer Tools

**Scripts:** (2 files)
- `analyze_sessions.py`
- `recover_content.py`

**References:** (2 files)
- `session_file_format.md`
- `workflow_examples.md`

**Other:** (2 files)
- `.security-scan-passed`
- `integration_summary.md`

### skill-creator
**Category:** Developer Tools

**Scripts:** (4 files)
- `quick_validate.py`
- `security_scan.py`
- `init_skill.py`
- `package_skill.py`

**Other:** (2 files)
- `LICENSE.txt`
- `.gitignore`

### skills-search
**Category:** Developer Tools

**Other:** (1 files)
- `.security-scan-passed`

### statusline-generator
**Category:** Developer Tools

**Scripts:** (2 files)
- `install_statusline.sh`
- `generate_statusline.sh`

**References:** (2 files)
- `ccusage_integration.md`
- `color_codes.md`

### config-progressive-disclosure
**Category:** Document Processing

**References:** (1 files)
- `progressive_disclosure_principles.md`

**Other:** (1 files)
- `.security-scan-passed`

### docs-cleaner
**Category:** Document Processing

**References:** (1 files)
- `value_analysis_template.md`

**Other:** (1 files)
- `.security-scan-passed`

### markdown-tools
**Category:** Document Processing

**Scripts:** (1 files)
- `convert_path.py`

**References:** (1 files)
- `conversion_examples.md`

### mermaid-tools
**Category:** Document Processing

**Scripts:** (3 files)
- `extract_diagrams.py`
- `extract-and-generate.sh`
- `puppeteer-config.json`

**References:** (1 files)
- `setup_and_troubleshooting.md`

### ocr-pdf-creator
**Category:** Document Processing

**Scripts:** (2 files)
- `batch_ocr.py`
- `ocr_pdf.py`

**References:** (1 files)
- `ocr_tools_reference.md`

### pdf-creator
**Category:** Document Processing

**Scripts:** (2 files)
- `batch_convert.py`
- `md_to_pdf.py`

**Other:** (1 files)
- `.security-scan-passed`

### ppt-creator
**Category:** Document Processing

**Scripts:** (1 files)
- `chartkit.py`

**References:** (11 files)
- `orchestration_data_charts.md`
- `orchestration_overview.md`
- `templates.md`
- `workflow.md`
- `rubric.md`
- `orchestration_pptx.md`
- `checklist.md`
- `style_guide.md`
- `vis_guide.md`
- `intake.md`
- ...and 1 more

### langchain-optimization
**Category:** Llm Application Dev

**Scripts:** (2 files)
- `chain_analyzer.py`
- `memory_profiler.py`

**References:** (3 files)
- `chain_patterns.md`
- `debugging_guide.md`
- `memory_strategies.md`

**Assets:** (1 files)
- `langchain_decision_tree.md`

### llm-icon-finder
**Category:** Llm Application Dev

**References:** (2 files)
- `icons_list.md`
- `developer_info.md`

### prompt-engineering-patterns
**Category:** Llm Application Dev

**Scripts:** (1 files)
- `optimize-prompt.py`

**References:** (5 files)
- `prompt_templates.md`
- `prompt_optimization.md`
- `chain_of_thought.md`
- `system_prompts.md`
- `few_shot_learning.md`

**Assets:** (2 files)
- `prompt_template_library.md`
- `few-shot-examples.json`

### prompt-optimizer
**Category:** Llm Application Dev

**References:** (4 files)
- `advanced_techniques.md`
- `ears_syntax.md`
- `domain_theories.md`
- `examples.md`

**Other:** (1 files)
- `.security-scan-passed`

### promptfoo-evaluation
**Category:** Llm Application Dev

**References:** (1 files)
- `promptfoo_api.md`

**Other:** (1 files)
- `.security-scan-passed`

### android-admob-mediation
**Category:** Mobile Development

**References:** (2 files)
- `consent_management_ump.md`
- `ad_format_decision_tree.md`

### android-app-survey
**Category:** Mobile Development

**References:** (1 files)
- `android_structure_conventions.md`

### android-behavior-audit
**Category:** Mobile Development

**References:** (2 files)
- `finding_examples.md`
- `android_behavior_patterns.md`

### android-behavior-fix-planning
**Category:** Mobile Development

**References:** (1 files)
- `fix_pattern_library.md`

### android-behavior-trace
**Category:** Mobile Development

**References:** (1 files)
- `android_layer_tracing_guide.md`

### android-firebase-sync-validator
**Category:** Mobile Development

**Scripts:** (3 files)
- `validate_sync_coverage.py`
- `fix_sync_issues.py`
- `analyze_data_models.py`

**References:** (4 files)
- `cloud_functions_patterns.md`
- `firebase_security_rules.md`
- `firestore_rules_patterns.md`
- `rtdb_rules_patterns.md`

**Assets:** (3 files)
- `sync_map.template.json`
- `firestore_rules.template`
- `rtdb_rules.template.json`

### android-multi-source-data-layer
**Category:** Mobile Development

**References:** (3 files)
- `conflict_resolution_strategies.md`
- `cache_invalidation_patterns.md`
- `data_routing_decision_tree.md`

### android-play-billing-subscriptions
**Category:** Mobile Development

**References:** (2 files)
- `play_billing_testing.md`
- `subscription_state_machine.md`

### android-rich-notification-system
**Category:** Mobile Development

**References:** (3 files)
- `notification_channel_registry.md`
- `android13_permission_handling.md`
- `fcm_message_patterns.md`

### iOS-APP-developer
**Category:** Mobile Development

**References:** (4 files)
- `camera_avfoundation.md`
- `xcodegen_full.md`
- `swiftui_compatibility.md`
- `testing_mainactor.md`

**Other:** (1 files)
- `.security-scan-passed`

### mobile-ui-element-audit
**Category:** Mobile Development

**References:** (1 files)
- `element_scoring_worksheets.md`

### mobile-ui-habit-loop-design
**Category:** Mobile Development

**References:** (1 files)
- `engagement_pattern_library.md`

### mobile-ui-micro-interactions
**Category:** Mobile Development

**References:** (1 files)
- `animation_timing_reference.md`

### opentelemetry-setup
**Category:** Observability

**Scripts:** (1 files)
- `validate_setup.sh`

**References:** (2 files)
- `semantic_conventions.md`
- `exporters.md`

**Assets:** (2 files)
- `docker-compose.example.yml`
- `instrumentation.example.ts`

### slsa-compliance
**Category:** Security

**Scripts:** (2 files)
- `sbom_generator.sh`
- `slsa_level_checker.py`

**References:** (4 files)
- `provenance_guide.md`
- `slsa_levels_explained.md`
- `ci_integration.md`
- `sbom_formats.md`

**Assets:** (1 files)
- `slsa_checklist.md`

### qa-expert
**Category:** Testing Qa

**Scripts:** (2 files)
- `init_qa_project.py`
- `calculate_metrics.py`

**References:** (5 files)
- `master_qa_prompt.md`
- `llm_prompts_library.md`
- `day1_onboarding.md`
- `google_testing_standards.md`
- `ground_truth_principle.md`

**Assets:** (1 files)
- `test_case_template.md`

**Other:** (1 files)
- `.security-scan-passed`

### astro-development
**Category:** Web Development

**References:** (2 files)
- `configuration.md`
- `islands_patterns.md`

**Assets:** (2 files)
- `content_schema.example.ts`
- `astro.config.example.mjs`

### cloudflare-troubleshooting
**Category:** Web Development

**Scripts:** (2 files)
- `check_cloudflare_config.py`
- `fix_ssl_mode.py`

**References:** (3 files)
- `ssl_modes.md`
- `common_issues.md`
- `api_overview.md`

### qwik-development
**Category:** Web Development

**References:** (2 files)
- `routing.md`
- `resumability.md`

**Assets:** (2 files)
- `vite.config.example.ts`
- `component_patterns.md`

### solid-development
**Category:** Web Development

**References:** (2 files)
- `reactivity.md`
- `stores.md`

**Assets:** (2 files)
- `vite.config.example.ts`
- `component_patterns.md`

### ui-designer
**Category:** Web Development

**Assets:** (3 files)
- `design_system.md`
- `app_overview_generator.md`
- `vibe_design_template.md`

---

## Appendix: Common Dependencies

Most frequently required tools and technologies:

| Dependency | Skills Using It |
|------------|----------------|
| go | 125 |
| python | 71 |
| git | 71 |
| rest | 66 |
| github | 54 |
| java | 49 |
| node | 45 |
| react | 29 |
| npm | 29 |
| aws | 24 |
| rust | 23 |
| kubernetes | 17 |
| docker | 16 |
| postgresql | 15 |
| pytest | 12 |
| azure | 11 |
| redis | 9 |
| gitlab | 9 |
| terraform | 8 |
| mysql | 7 |
| pnpm | 7 |
| yarn | 7 |
| gcp | 7 |
| jest | 7 |
| graphql | 6 |
| kafka | 5 |
| next.js | 5 |
| grpc | 5 |
| elasticsearch | 4 |
| mongodb | 4 |

*Last updated: 2026-04-20*
