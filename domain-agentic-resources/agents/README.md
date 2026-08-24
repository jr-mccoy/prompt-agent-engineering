<!-- INVENTORY_COUNTS: {"categories": {"architecture": 6, "backend": 8, "business": 2, "business-operations": 11, "cloud-infrastructure": 9, "code-quality": 4, "creative": 2, "database": 4, "deployment": 1, "devops": 6, "documentation": 5, "education": 2, "frontend-mobile": 22, "healthcare": 2, "languages": 21, "ml-ai": 6, "orchestration": 2, "research": 2, "security": 4, "seo-marketing": 12, "testing": 5, "web-development": 5, "writing": 2}, "date": "2026-08-24", "total": 143, "type": "agents"} -->

# Claude Code Agents Index

**Comprehensive index of 143 specialized Claude Code agents organized by domain.**

## Overview

This directory contains **143 specialized AI agents** for Claude Code, each optimized for specific development tasks and domains. Agents are persistent identities with model assignments (Opus/Sonnet/Haiku) for optimal cost/performance balance.

### Quick Stats

- **Total Agents:** 143
- **Categories:** 23
- **Model Distribution:**
  - **HAIKU:** 15 agents (12.6%)
  - **Inherit (User Choice):** 25 agents (21.0%)
  - **OPUS:** 36 agents (30.3%)
  - **SONNET:** 43 agents (36.1%)

## Table of Contents

**By Category:**
- [Architecture](#architecture) (6 agents)
- [Backend](#backend) (8 agents)
- [Business](#business) (2 agents)
- [Business Operations](#business-operations) (11 agents)
- [Cloud Infrastructure](#cloud-infrastructure) (9 agents)
- [Code Quality](#code-quality) (4 agents)
- [Creative](#creative) (2 agents)
- [Database](#database) (4 agents)
- [Deployment](#deployment) (1 agents)
- [Devops](#devops) (6 agents)
- [Documentation](#documentation) (5 agents)
- [Education](#education) (2 agents)
- [Frontend Mobile](#frontend-mobile) (22 agents)
- [Healthcare](#healthcare) (2 agents)
- [Languages](#languages) (21 agents)
- [Ml Ai](#ml-ai) (6 agents)
- [Orchestration](#orchestration) (2 agents)
- [Research](#research) (2 agents)
- [Security](#security) (4 agents)
- [Seo Marketing](#seo-marketing) (12 agents)
- [Testing](#testing) (5 agents)
- [Web Development](#web-development) (5 agents)
- [Writing](#writing) (2 agents)


## Understanding Model Assignments

Each agent is assigned a specific Claude model for optimal performance:

- **Opus 4.5** - Critical architecture decisions, security audits, complex design
- **Sonnet 4.5** - Balanced tasks requiring intelligence and speed
- **Haiku 4.5** - Fast operational tasks, code generation, quick analyses
- **Inherit** - User chooses model based on budget and performance needs

## How to Use This Index

1. **Browse by category** to find agents for your domain
2. **Check model assignment** to understand cost/performance
3. **Review activation criteria** ('When to use') to know when to invoke
4. **Look for related agents** for multi-agent workflows
5. **Find related skills** for bundled knowledge packages

---

## Agents by Category

### Architecture

**6 agents in this category**

#### `architect-review`

- **Path:** `agents/architecture/architect_review.md`
- **Model:** OPUS
- **Description:** Master software architect specializing in modern architecture patterns, clean architecture, microservices, event-driven systems, and DDD. Reviews system designs and code changes for architectural integrity, scalability, and maintainability.
- **When to use:** Use PROACTIVELY for architectural decisions.

#### `solo-dev-architect`

- **Path:** `agents/architecture/solo_dev_architect.md`
- **Model:** OPUS
- **Description:** Architecture advisor calibrated for solo developer constraints. Makes recommendations optimized for maintainability-by-one-person rather than team scalability. Favors simplicity, convention over configuration, and proven technology unless complexity is justified by concrete requirements.
- **When to use:** Use PROACTIVELY for architecture decisions, technology selection, project structure, dependency evaluation, or when a solo developer asks "should I use X or Y?" or "how should I structure this?".

#### `c4-component`

- **Path:** `agents/architecture/c4_component.md`
- **Model:** SONNET
- **Description:** Expert C4 Component-level documentation specialist. Synthesizes C4 Code-level documentation into Component-level architecture, defining component boundaries, interfaces, and relationships. Creates component diagrams and documentation.
- **When to use:** Use when synthesizing code-level documentation into logical components.

#### `c4-container`

- **Path:** `agents/architecture/c4_container.md`
- **Model:** SONNET
- **Description:** Expert C4 Container-level documentation specialist. Synthesizes Component-level documentation into Container-level architecture, mapping components to deployment units, documenting container interfaces as APIs, and creating container diagrams.
- **When to use:** Use when synthesizing components into deployment containers and documenting system deployment architecture.

#### `c4-context`

- **Path:** `agents/architecture/c4_context.md`
- **Model:** SONNET
- **Description:** Expert C4 Context-level documentation specialist. Creates high-level system context diagrams, documents personas, user journeys, system features, and external dependencies. Synthesizes container and component documentation with system documentation to create comprehensive context-level architecture.
- **When to use:** Use when creating the highest-level C4 system context documentation.

#### `c4-code`

- **Path:** `agents/architecture/c4_code.md`
- **Model:** HAIKU
- **Description:** Expert C4 Code-level documentation specialist. Analyzes code directories to create comprehensive C4 code-level documentation including function signatures, arguments, dependencies, and code structure.
- **When to use:** Use when documenting code at the lowest C4 level for individual directories and code modules.

---

### Backend

**7 agents in this category**

#### `data-engineer`

- **Path:** `agents/backend/data_engineer.md`
- **Model:** OPUS
- **Description:** Build scalable data pipelines, modern data warehouses, and real-time streaming architectures. Implements Apache Spark, dbt, Airflow, and cloud-native data platforms.
- **When to use:** Use PROACTIVELY for data pipeline design, analytics infrastructure, or modern data stack implementation.

#### `django-pro`

- **Path:** `agents/backend/django_pro.md`
- **Model:** OPUS
- **Description:** Master Django 5.x with async views, DRF, Celery, and Django Channels. Build scalable web applications with proper architecture, testing, and deployment.
- **When to use:** Use PROACTIVELY for Django development, ORM optimization, or complex Django patterns.

#### `fastapi-pro`

- **Path:** `agents/backend/fastapi_pro.md`
- **Model:** OPUS
- **Description:** Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. Master microservices, WebSockets, and modern Python async patterns.
- **When to use:** Use PROACTIVELY for FastAPI development, async optimization, or API architecture.

#### `graphql-architect`

- **Path:** `agents/backend/graphql_architect.md`
- **Model:** OPUS
- **Description:** Master modern GraphQL with federation, performance optimization, and enterprise security. Build scalable schemas, implement advanced caching, and design real-time systems.
- **When to use:** Use PROACTIVELY for GraphQL architecture or performance optimization.

#### `backend-security-coder`

- **Path:** `agents/backend/backend_security_coder.md`
- **Model:** SONNET
- **Description:** Expert in secure backend coding practices specializing in input validation, authentication, and API security.
- **When to use:** Use PROACTIVELY for backend security implementations or security code reviews.

#### `backend-architect`

- **Path:** `agents/backend/backend_architect.md`
- **Model:** INHERIT
- **Description:** Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. Masters REST/GraphQL/gRPC APIs, event-driven architectures, service mesh patterns, and modern backend frameworks. Handles service boundary definition, inter-service communication, resilience patterns, and observability.
- **When to use:** Use PROACTIVELY when creating new backend services or APIs.

#### `temporal-python-pro`

- **Path:** `agents/backend/temporal_python_pro.md`
- **Model:** INHERIT
- **Description:** Master Temporal workflow orchestration with Python SDK. Implements durable workflows, saga patterns, and distributed transactions. Covers async/await, testing strategies, and production deployment.
- **When to use:** Use PROACTIVELY for workflow design, microservice orchestration, or long-running processes.

---

### Frontend Mobile

**22 agents in this category**

#### `android-behavior-auditor`

- **Path:** `agents/frontend-mobile/android_behavior_auditor.md`
- **Model:** OPUS
- **Description:** Expert Android behavioral analyst specializing in identifying discrepancies between actual code behavior and developer intent. Masters scrutiny of Compose UI flows, ViewModel state machines, Room data operations, Firebase sync patterns, and navigation graphs to detect silent failures, dead-end states, ambiguous UX flows, and partially implemented features. Classifies findings by confidence (Likely Bug >80%, Suspicious 40-80%, Design Question <40%).
- **When to use:** Use PROACTIVELY for pre-release behavior audits, "something feels wrong" investigations, intent-vs-actual-behavior analysis, or when preparing apps for closed/open testing.

#### `android-behavior-fix-planner`

- **Path:** `agents/frontend-mobile/android_behavior_fix_planner.md`
- **Model:** OPUS
- **Description:** Expert Android behavioral fix strategist specializing in minimal-change fix planning, blast radius estimation, dependency ordering, and verified implementation for resolving behavioral discrepancies identified in behavior audits. Masters surgical code modifications across Compose UI, ViewModel state, Room operations, Firebase patterns, and navigation flows with post-fix verification.
- **When to use:** Use PROACTIVELY for planning fixes from behavior audit findings, integrating developer clarifications into fix plans, implementing approved fixes with verification, or when resolving confirmed behavioral discrepancies.

#### `android-behavior-tracer`

- **Path:** `agents/frontend-mobile/android_behavior_tracer.md`
- **Model:** OPUS
- **Description:** Expert Android code path tracer specializing in exhaustive depth-first analysis that follows user actions through every architectural layer (UI, ViewModel, Repository, Data, Background) and produces factual behavior catalogs documenting what code actually does. Masters Compose state flows, coroutine tracing, Room query analysis, Firebase operation mapping, and WorkManager execution paths.
- **When to use:** Use PROACTIVELY for behavior audit tracing phases, documenting actual code behavior, building behavior catalogs, or when understanding exactly what happens when a user performs an action.

#### `android-monetization-architect`

- **Path:** `agents/frontend-mobile/android_monetization_architect.md`
- **Model:** OPUS
- **Description:** Expert Android monetization architect specializing in Google Play Billing Library, subscription lifecycle management, AdMob integration, paywall design, revenue optimization, and Play Store monetization policy compliance. Masters BillingClient implementation, server-side receipt validation, ad mediation, and subscription analytics.
- **When to use:** Use PROACTIVELY when implementing billing, subscriptions, ads, paywalls, or monetization strategy for Android apps.

#### `android-release-manager`

- **Path:** `agents/frontend-mobile/android_release_manager.md`
- **Model:** OPUS
- **Description:** Expert Android release manager specializing in beta testing strategy, staged rollouts, crash-free rate evaluation, Play Store compliance, and go/no-go release decisions. Masters Firebase App Distribution, Play Console test tracks, release automation with Fastlane/Gradle, version management, and Android App Bundle optimization.
- **When to use:** Use PROACTIVELY for beta launches, release preparation, staged rollout decisions, Play Store submissions, or release readiness assessments.

#### `mobile-ui-addiction-architect`

- **Path:** `agents/frontend-mobile/mobile_ui_addiction_architect.md`
- **Model:** OPUS
- **Description:** Expert in behavioral psychology and habit-forming product design who applies the Hook Model, Fogg Behavior Model, gamification science, and dopamine-driven design to create mobile UIs that users feel compelled to return to. Designs engagement loops, reward systems, retention mechanics, and emotional design patterns that make apps indispensable.
- **When to use:** Use PROACTIVELY for user retention strategy, engagement optimization, habit loop design, gamification implementation, or when building features that need to drive daily active usage.

#### `mobile-ui-competitive-teardown`

- **Path:** `agents/frontend-mobile/mobile_ui_competitive_teardown.md`
- **Model:** OPUS
- **Description:** Expert competitive UI analyst who performs systematic teardowns of competitor and best-in-class mobile apps, analyzing their UI patterns, engagement mechanics, visual design language, interaction patterns, and user flows to extract actionable insights. Produces detailed comparison matrices and implementation recommendations.
- **When to use:** Use PROACTIVELY for competitive analysis, app store research, design benchmarking, or when planning features by studying how top apps solve the same problem.

#### `mobile-ui-element-analyzer`

- **Path:** `agents/frontend-mobile/mobile_ui_element_analyzer.md`
- **Model:** OPUS
- **Description:** Hyper-detailed mobile UI element analyst who performs surgical, element-level analysis of any UI component — buttons, navigation bars, cards, inputs, modals, lists, headers, onboarding flows, etc. Produces pixel-level improvement plans covering visual design, interaction design, micro-animations, accessibility, and engagement optimization.
- **When to use:** Use PROACTIVELY for UI element reviews, component-level design improvements, or when a developer wants to perfect a specific UI element.

#### `mobile-ui-trend-researcher`

- **Path:** `agents/frontend-mobile/mobile_ui_trend_researcher.md`
- **Model:** OPUS
- **Description:** Expert mobile UI/UX trend analyst who researches current design trends, emerging interaction patterns, platform-specific innovations, and industry-leading app designs across iOS and Android. Synthesizes findings into actionable design recommendations with implementation guidance.
- **When to use:** Use PROACTIVELY for UI modernization, design trend research, competitive design analysis, or when planning a UI refresh or new app design.

#### `android-adb-specialist`

- **Path:** `agents/frontend-mobile/android_adb_specialist.md`
- **Model:** SONNET
- **Description:** Expert ADB operator who translates high-level developer intents ("test this deep link", "check memory usage", "capture logs for this crash") into precise ADB command sequences. Knows device quirks, manufacturer-specific behaviors, API-level differences, and when ADB alone is insufficient.
- **When to use:** Use PROACTIVELY when working with ADB commands, device debugging, logcat analysis, performance profiling via ADB, or device management tasks.

#### `android-api-level-migration-agent`

- **Path:** `agents/frontend-mobile/android_api_level_migration_agent.md`
- **Model:** SONNET
- **Description:** Expert Android API level migration specialist planning targetSdk and compileSdk version bumps by mapping required changes per API level, identifying behavior changes, deprecated APIs, new permission requirements, and generating comprehensive migration checklists with code changes.
- **When to use:** Use PROACTIVELY when upgrading targetSdkVersion, when Google Play enforces new API level requirements, or when planning annual SDK updates.

#### `android-app-surveyor`

- **Path:** `agents/frontend-mobile/android_app_surveyor.md`
- **Model:** SONNET
- **Description:** Systematic Android app structure mapper specializing in breadth-first discovery of screens, features, navigation flows, subsystems, and tech stack. Produces categorized feature maps for behavior audits, codebase onboarding, and pre-release inventory. Masters Compose navigation graphs, manifest parsing, dependency analysis, and feature grouping.
- **When to use:** Use PROACTIVELY for behavior audit survey phases, new codebase onboarding, feature inventory before testing, or app structure documentation.

#### `android-compose-converter`

- **Path:** `agents/frontend-mobile/android_compose_converter.md`
- **Model:** SONNET
- **Description:** Expert Android UI migration specialist converting View-based XML layouts to Jetpack Compose, handling RecyclerView to LazyList, ConstraintLayout to Compose equivalents, custom views, theme migration, and data binding to state management.
- **When to use:** Use PROACTIVELY when migrating from XML to Compose, converting individual screens, or planning incremental View-to-Compose migration strategies.

#### `android-dependency-update-agent`

- **Path:** `agents/frontend-mobile/android_dependency_update_agent.md`
- **Model:** SONNET
- **Description:** Expert Android dependency management specialist analyzing project dependency trees, identifying outdated libraries, checking for known CVEs, assessing breaking change risk, and producing prioritized update plans with migration notes.
- **When to use:** Use PROACTIVELY when updating dependencies, auditing dependency health, preparing for major library upgrades, or when dependency conflicts arise during builds.

#### `android-gradle-doctor`

- **Path:** `agents/frontend-mobile/android_gradle_doctor.md`
- **Model:** SONNET
- **Description:** Expert Android Gradle build system diagnostician who troubleshoots slow builds, dependency conflicts, configuration errors, memory issues, and task avoidance problems. Produces actionable fix plans with measured improvements.
- **When to use:** Use PROACTIVELY when builds are slow, Gradle sync fails, dependency resolution errors occur, or build configurations produce unexpected behavior.

#### `frontend-security-coder`

- **Path:** `agents/frontend-mobile/frontend_security_coder.md`
- **Model:** SONNET
- **Description:** Expert in secure frontend coding practices specializing in XSS prevention, output sanitization, and client-side security patterns.
- **When to use:** Use PROACTIVELY for frontend security implementations or client-side security code reviews.

#### `mobile-security-coder`

- **Path:** `agents/frontend-mobile/mobile_security_coder.md`
- **Model:** SONNET
- **Description:** Expert in secure mobile coding practices specializing in input validation, WebView security, and mobile-specific security patterns.
- **When to use:** Use PROACTIVELY for mobile security implementations or mobile security code reviews.

#### `ui-ux-designer`

- **Path:** `agents/frontend-mobile/ui_ux_designer.md`
- **Model:** SONNET
- **Description:** Create interface designs, wireframes, and design systems. Masters user research, accessibility standards, and modern design tools. Specializes in design tokens, component libraries, and inclusive design.
- **When to use:** Use PROACTIVELY for design systems, user flows, or interface optimization.

#### `flutter-expert`

- **Path:** `agents/frontend-mobile/flutter_expert.md`
- **Model:** INHERIT
- **Description:** Master Flutter development with Dart 3, advanced widgets, and multi-platform deployment. Handles state management, animations, testing, and performance optimization for mobile, web, desktop, and embedded platforms.
- **When to use:** Use PROACTIVELY for Flutter architecture, UI implementation, or cross-platform features.

#### `frontend-developer`

- **Path:** `agents/frontend-mobile/frontend_developer.md`
- **Model:** INHERIT
- **Description:** Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern frontend architecture. Optimizes performance and ensures accessibility.
- **When to use:** Use PROACTIVELY when creating UI components or fixing frontend issues.

#### `ios-developer`

- **Path:** `agents/frontend-mobile/ios_developer.md`
- **Model:** INHERIT
- **Description:** Develop native iOS applications with Swift/SwiftUI. Masters iOS 18, SwiftUI, UIKit integration, Core Data, networking, and App Store optimization.
- **When to use:** Use PROACTIVELY for iOS-specific features, App Store optimization, or native iOS development.

#### `mobile-developer`

- **Path:** `agents/frontend-mobile/mobile_developer.md`
- **Model:** INHERIT
- **Description:** Develop React Native, Flutter, or native mobile apps with modern architecture patterns. Masters cross-platform development, native integrations, offline sync, and app store optimization.
- **When to use:** Use PROACTIVELY for mobile features, cross-platform code, or app optimization.

---

### Database

**4 agents in this category**

#### `database-architect`

- **Path:** `agents/database/database_architect.md`
- **Model:** OPUS
- **Description:** Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and scalable database architectures. Masters SQL/NoSQL/TimeSeries database selection, normalization strategies, migration planning, and performance-first design. Handles both greenfield architectures and re-architecture of existing systems.
- **When to use:** Use PROACTIVELY for database architecture, technology selection, or data modeling decisions.

#### `database-admin`

- **Path:** `agents/database/database_admin.md`
- **Model:** SONNET
- **Description:** Expert database administrator specializing in modern cloud databases, automation, and reliability engineering. Masters AWS/Azure/GCP database services, Infrastructure as Code, high availability, disaster recovery, performance optimization, and compliance. Handles multi-cloud strategies, container databases, and cost optimization.
- **When to use:** Use PROACTIVELY for database architecture, operations, or reliability engineering.

#### `database-optimizer`

- **Path:** `agents/database/database_optimizer.md`
- **Model:** INHERIT
- **Description:** Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. Masters advanced indexing, N+1 resolution, multi-tier caching, partitioning strategies, and cloud database optimization. Handles complex query analysis, migration strategies, and performance monitoring.
- **When to use:** Use PROACTIVELY for database optimization, performance issues, or scalability challenges.

#### `sql-pro`

- **Path:** `agents/database/sql_pro.md`
- **Model:** INHERIT
- **Description:** Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques. Expert in performance tuning, data modeling, and hybrid analytical systems.
- **When to use:** Use PROACTIVELY for database optimization or complex analysis.

---

### Cloud Infrastructure

**8 agents in this category**

#### `cloud-architect`

- **Path:** `agents/cloud-infrastructure/cloud_architect.md`
- **Model:** OPUS
- **Description:** Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural patterns. Masters serverless, microservices, security, compliance, and disaster recovery.
- **When to use:** Use PROACTIVELY for cloud architecture, cost optimization, migration planning, or multi-cloud strategies.

#### `firebase-architecture-reviewer`

- **Path:** `agents/cloud-infrastructure/firebase_architecture_reviewer.md`
- **Model:** OPUS
- **Description:** Firebase architecture review agent evaluating overall Firebase project design including data model efficiency, service selection appropriateness, security posture, scalability bottlenecks, and cost trajectory. Produces architecture assessments with improvement recommendations.
- **When to use:** Use PROACTIVELY when designing new Firebase architectures, reviewing existing projects, or planning for scale.

#### `firebase-security-auditor`

- **Path:** `agents/cloud-infrastructure/firebase_security_auditor.md`
- **Model:** OPUS
- **Description:** Comprehensive Firebase security audit agent reviewing Firestore and RTDB security rules, exposed API keys in client code, App Check implementation, auth flow vulnerabilities, and Cloud Functions injection risks. Produces severity-rated security reports with remediation steps.
- **When to use:** Use PROACTIVELY for Firebase security audits, when setting up new Firebase projects, before launches, or when security incidents are suspected.

#### `hybrid-cloud-architect`

- **Path:** `agents/cloud-infrastructure/hybrid_cloud_architect.md`
- **Model:** OPUS
- **Description:** Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware). Masters hybrid connectivity, workload placement optimization, edge computing, and cross-cloud automation. Handles compliance, cost optimization, disaster recovery, and migration strategies.
- **When to use:** Use PROACTIVELY for hybrid architecture, multi-cloud strategy, or complex infrastructure integration.

#### `kubernetes-architect`

- **Path:** `agents/cloud-infrastructure/kubernetes_architect.md`
- **Model:** OPUS
- **Description:** Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration. Masters EKS/AKS/GKE, service mesh (Istio/Linkerd), progressive delivery, multi-tenancy, and platform engineering. Handles security, observability, cost optimization, and developer experience.
- **When to use:** Use PROACTIVELY for K8s architecture, GitOps implementation, or cloud-native platform design.

#### `terraform-specialist`

- **Path:** `agents/cloud-infrastructure/terraform_specialist.md`
- **Model:** OPUS
- **Description:** Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. Handles complex module design, multi-cloud deployments, GitOps workflows, policy as code, and CI/CD integration. Covers migration strategies, security best practices, and modern IaC ecosystems.
- **When to use:** Use PROACTIVELY for advanced IaC, state management, or infrastructure automation.

#### `firebase-cost-analyst`

- **Path:** `agents/cloud-infrastructure/firebase_cost_analyst.md`
- **Model:** SONNET
- **Description:** Firebase cost analysis agent examining usage patterns, producing cost reports with projections, optimization recommendations with estimated savings, alerts for cost anomalies, and free tier limit comparisons.
- **When to use:** Use PROACTIVELY when Firebase costs are increasing, when planning Firebase architecture, before launches expected to increase usage, or when budget alerts fire.

#### `network-engineer`

- **Path:** `agents/cloud-infrastructure/network_engineer.md`
- **Model:** SONNET
- **Description:** Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization. Masters multi-cloud connectivity, service mesh, zero-trust networking, SSL/TLS, global load balancing, and advanced troubleshooting. Handles CDN optimization, network automation, and compliance.
- **When to use:** Use PROACTIVELY for network design, connectivity issues, or performance optimization.

---

### Devops

**5 agents in this category**

#### `devops-troubleshooter`

- **Path:** `agents/devops/devops_troubleshooter.md`
- **Model:** SONNET
- **Description:** Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. Masters log analysis, distributed tracing, Kubernetes debugging, performance optimization, and root cause analysis. Handles production outages, system reliability, and preventive monitoring.
- **When to use:** Use PROACTIVELY for debugging, incident response, or system troubleshooting.

#### `dx-optimizer`

- **Path:** `agents/devops/dx_optimizer.md`
- **Model:** SONNET
- **Description:** Developer Experience specialist. Improves tooling, setup, and workflows.
- **When to use:** Use PROACTIVELY when setting up new projects, after team feedback, or when development friction is noticed.

#### `error-detective`

- **Path:** `agents/devops/error_detective.md`
- **Model:** SONNET
- **Description:** Search logs and codebases for error patterns, stack traces, and anomalies. Correlates errors across systems and identifies root causes.
- **When to use:** Use PROACTIVELY when debugging issues, analyzing logs, or investigating production errors.

#### `incident-responder`

- **Path:** `agents/devops/incident_responder.md`
- **Model:** SONNET
- **Description:** Expert SRE incident responder specializing in rapid problem resolution, modern observability, and comprehensive incident management. Masters incident command, blameless post-mortems, error budget management, and system reliability patterns. Handles critical outages, communication strategies, and continuous improvement. Use IMMEDIATELY for production incidents or SRE practices.

#### `observability-engineer`

- **Path:** `agents/devops/observability_engineer.md`
- **Model:** INHERIT
- **Description:** Build production-ready monitoring, logging, and tracing systems. Implements comprehensive observability strategies, SLI/SLO management, and incident response workflows.
- **When to use:** Use PROACTIVELY for monitoring infrastructure, performance optimization, or production reliability.

---

### Deployment

**1 agents in this category**

#### `deployment-engineer`

- **Path:** `agents/deployment/deployment_engineer.md`
- **Model:** HAIKU
- **Description:** Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. Masters GitHub Actions, ArgoCD/Flux, progressive delivery, container security, and platform engineering. Handles zero-downtime deployments, security scanning, and developer experience optimization.
- **When to use:** Use PROACTIVELY for CI/CD design, GitOps implementation, or deployment automation.

---

### Code Quality

**4 agents in this category**

#### `code-reviewer`

- **Path:** `agents/code-quality/code_reviewer.md`
- **Model:** OPUS
- **Description:** Elite code review expert specializing in modern AI-powered code analysis, security vulnerabilities, performance optimization, and production reliability. Masters static analysis tools, security scanning, and configuration review with 2024/2025 best practices.
- **When to use:** Use PROACTIVELY for code quality assurance.

#### `solo-dev-reviewer`

- **Path:** `agents/code-quality/solo_dev_reviewer.md`
- **Model:** OPUS
- **Description:** Code reviewer specifically calibrated for solo developers. Reviews with empathy for solo constraints (limited time, no team), focuses on high-impact issues over style nits, and explicitly calls out solo dev blind spots like missing error handling, hardcoded configuration, and untested edge cases. Provides a "ship it or hold it" verdict with clear rationale.
- **When to use:** Use PROACTIVELY when reviewing code before merge, after vibe coding sessions, before releases, or when a solo developer asks for code review.

#### `legacy-modernizer`

- **Path:** `agents/code-quality/legacy_modernizer.md`
- **Model:** SONNET
- **Description:** Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and backward compatibility.
- **When to use:** Use PROACTIVELY for legacy system updates, framework migrations, or technical debt reduction.

#### `tech-debt-reducer`

- **Path:** `agents/code-quality/tech_debt_reducer.md`
- **Model:** SONNET
- **Description:** Expert in identifying, quantifying, prioritizing, and systematically reducing technical debt across codebases.
- **When to use:** Use PROACTIVELY when reviewing legacy code, planning refactoring sprints, assessing code health, or creating tech debt reduction roadmaps.

---

### Testing

**5 agents in this category**

#### `tdd-orchestrator`

- **Path:** `agents/testing/tdd_orchestrator.md`
- **Model:** OPUS
- **Description:** Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination, and comprehensive test-driven development practices. Enforces TDD best practices across teams with AI-assisted testing and modern frameworks.
- **When to use:** Use PROACTIVELY for TDD implementation and governance.

#### `android-device-farm-operator`

- **Path:** `agents/testing/android_device_farm_operator.md`
- **Model:** SONNET
- **Description:** Manages emulator fleets and test execution across multiple Android configurations. Handles AVD creation, parallel test execution, result aggregation, Gradle Managed Devices, and Firebase Test Lab CLI. Recommends minimum viable device matrices based on app target audience.
- **When to use:** Use PROACTIVELY for multi-device testing, test matrix setup, CI emulator configuration, Firebase Test Lab usage, or when a developer needs to test across API levels and screen sizes.

#### `debugger`

- **Path:** `agents/testing/debugger.md`
- **Model:** SONNET
- **Description:** Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues.

#### `test-automator`

- **Path:** `agents/testing/test_automator.md`
- **Model:** SONNET
- **Description:** Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testing strategies with advanced CI/CD integration.
- **When to use:** Use PROACTIVELY for testing automation or quality assurance.

#### `performance-engineer`

- **Path:** `agents/testing/performance_engineer.md`
- **Model:** INHERIT
- **Description:** Expert performance engineer specializing in modern observability, application optimization, and scalable system performance. Masters OpenTelemetry, distributed tracing, load testing, multi-tier caching, Core Web Vitals, and performance monitoring. Handles end-to-end optimization, real user monitoring, and scalability patterns.
- **When to use:** Use PROACTIVELY for performance optimization, observability, or scalability challenges.

---

### Security

**3 agents in this category**

#### `security-auditor`

- **Path:** `agents/security/security_auditor.md`
- **Model:** OPUS
- **Description:** Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. Masters vulnerability assessment, threat modeling, secure authentication (OAuth2/OIDC), OWASP standards, cloud security, and security automation. Handles DevSecOps integration, compliance (GDPR/HIPAA/SOC2), and incident response.
- **When to use:** Use PROACTIVELY for security audits, DevSecOps, or compliance implementation.

#### `compliance-scanner`

- **Path:** `agents/security/compliance_scanner.md`
- **Model:** SONNET
- **Description:** App compliance scanning agent that examines Android codebases for data collection points, validates permission usage justification, checks privacy policy accuracy against actual data practices, and flags Play Store policy risks. Produces compliance reports with severity-rated findings.
- **When to use:** Use PROACTIVELY when preparing for app launches, during compliance audits, after adding new third-party SDKs, or when Play Store policy violations are suspected.

#### `ui-visual-validator`

- **Path:** `agents/security/ui_visual_validator.md`
- **Model:** SONNET
- **Description:** Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification. Masters screenshot analysis, visual regression testing, and component validation.
- **When to use:** Use PROACTIVELY to verify UI modifications have achieved their intended goals through comprehensive visual analysis.

---

### Documentation

**5 agents in this category**

#### `api-documenter`

- **Path:** `agents/documentation/api_documenter.md`
- **Model:** SONNET
- **Description:** Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. Create interactive docs, generate SDKs, and build comprehensive developer portals.
- **When to use:** Use PROACTIVELY for API documentation or developer portal creation.

#### `docs-architect`

- **Path:** `agents/documentation/docs_architect.md`
- **Model:** SONNET
- **Description:** Creates comprehensive technical documentation from existing codebases. Analyzes architecture, design patterns, and implementation details to produce long-form technical manuals and ebooks.
- **When to use:** Use PROACTIVELY for system documentation, architecture guides, or technical deep-dives.

#### `tutorial-engineer`

- **Path:** `agents/documentation/tutorial_engineer.md`
- **Model:** SONNET
- **Description:** Creates step-by-step tutorials and educational content from code. Transforms complex concepts into progressive learning experiences with hands-on examples.
- **When to use:** Use PROACTIVELY for onboarding guides, feature tutorials, or concept explanations.

#### `mermaid-expert`

- **Path:** `agents/documentation/mermaid_expert.md`
- **Model:** HAIKU
- **Description:** Create Mermaid diagrams for flowcharts, sequences, ERDs, and architectures. Masters syntax for all diagram types and styling.
- **When to use:** Use PROACTIVELY for visual documentation, system diagrams, or process flows.

#### `reference-builder`

- **Path:** `agents/documentation/reference_builder.md`
- **Model:** HAIKU
- **Description:** Creates exhaustive technical references and API documentation. Generates comprehensive parameter listings, configuration guides, and searchable reference materials.
- **When to use:** Use PROACTIVELY for API docs, configuration references, or complete technical specifications.

---

### Languages

**21 agents in this category**

#### `blockchain-developer`

- **Path:** `agents/languages/blockchain_developer.md`
- **Model:** OPUS
- **Description:** Build production-ready Web3 applications, smart contracts, and decentralized systems. Implements DeFi protocols, NFT platforms, DAOs, and enterprise blockchain integrations.
- **When to use:** Use PROACTIVELY for smart contracts, Web3 apps, DeFi protocols, or blockchain infrastructure.

#### `c-pro`

- **Path:** `agents/languages/c_pro.md`
- **Model:** OPUS
- **Description:** Write efficient C code with proper memory management, pointer arithmetic, and system calls. Handles embedded systems, kernel modules, and performance-critical code.
- **When to use:** Use PROACTIVELY for C optimization, memory issues, or system programming.

#### `cpp-pro`

- **Path:** `agents/languages/cpp_pro.md`
- **Model:** OPUS
- **Description:** Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms. Handles templates, move semantics, and performance optimization.
- **When to use:** Use PROACTIVELY for C++ refactoring, memory safety, or complex C++ patterns.

#### `golang-pro`

- **Path:** `agents/languages/golang_pro.md`
- **Model:** OPUS
- **Description:** Master Go 1.21+ with modern patterns, advanced concurrency, performance optimization, and production-ready microservices. Expert in the latest Go ecosystem including generics, workspaces, and cutting-edge frameworks.
- **When to use:** Use PROACTIVELY for Go development, architecture design, or performance optimization.

#### `java-pro`

- **Path:** `agents/languages/java_pro.md`
- **Model:** OPUS
- **Description:** Master Java 21+ with modern features like virtual threads, pattern matching, and Spring Boot 3.x. Expert in the latest Java ecosystem including GraalVM, Project Loom, and cloud-native patterns.
- **When to use:** Use PROACTIVELY for Java development, microservices architecture, or performance optimization.

#### `minecraft-bukkit-pro`

- **Path:** `agents/languages/minecraft_bukkit_pro.md`
- **Model:** OPUS
- **Description:** Master Minecraft server plugin development with Bukkit, Spigot, and Paper APIs. Specializes in event-driven architecture, command systems, world manipulation, player management, and performance optimization.
- **When to use:** Use PROACTIVELY for plugin architecture, gameplay mechanics, server-side features, or cross-version compatibility.

#### `python-pro`

- **Path:** `agents/languages/python_pro.md`
- **Model:** OPUS
- **Description:** Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. Expert in the latest Python ecosystem including uv, ruff, pydantic, and FastAPI.
- **When to use:** Use PROACTIVELY for Python development, optimization, or advanced Python patterns.

#### `rust-pro`

- **Path:** `agents/languages/rust_pro.md`
- **Model:** OPUS
- **Description:** Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. Expert in the latest Rust ecosystem including Tokio, axum, and cutting-edge crates.
- **When to use:** Use PROACTIVELY for Rust development, performance optimization, or systems programming.

#### `typescript-pro`

- **Path:** `agents/languages/typescript_pro.md`
- **Model:** OPUS
- **Description:** Master TypeScript with advanced types, generics, and strict type safety. Handles complex type systems, decorators, and enterprise-grade patterns.
- **When to use:** Use PROACTIVELY for TypeScript architecture, type inference optimization, or advanced typing patterns.

#### `unity-developer`

- **Path:** `agents/languages/unity_developer.md`
- **Model:** OPUS
- **Description:** Build Unity games with optimized C# scripts, efficient rendering, and proper asset management. Masters Unity 6 LTS, URP/HDRP pipelines, and cross-platform deployment. Handles gameplay systems, UI implementation, and platform optimization.
- **When to use:** Use PROACTIVELY for Unity performance issues, game mechanics, or cross-platform builds.

#### `bash-pro`

- **Path:** `agents/languages/bash_pro.md`
- **Model:** SONNET
- **Description:** Master of defensive Bash scripting for production automation, CI/CD pipelines, and system utilities. Expert in safe, portable, and testable shell scripts.

#### `haskell-pro`

- **Path:** `agents/languages/haskell_pro.md`
- **Model:** SONNET
- **Description:** Expert Haskell engineer specializing in advanced type systems, pure functional design, and high-reliability software.
- **When to use:** Use PROACTIVELY for type-level programming, concurrency, and architecture guidance.

#### `julia-pro`

- **Path:** `agents/languages/julia_pro.md`
- **Model:** SONNET
- **Description:** Master Julia 1.10+ with modern features, performance optimization, multiple dispatch, and production-ready practices. Expert in the Julia ecosystem including package management, scientific computing, and high-performance numerical code.
- **When to use:** Use PROACTIVELY for Julia development, optimization, or advanced Julia patterns.

#### `posix-shell-pro`

- **Path:** `agents/languages/posix_shell_pro.md`
- **Model:** SONNET
- **Description:** Expert in strict POSIX sh scripting for maximum portability across Unix-like systems. Specializes in shell scripts that run on any POSIX-compliant shell (dash, ash, sh, bash --posix).

#### `arm-cortex-expert`

- **Path:** `agents/languages/arm_cortex_expert.md`
- **Model:** INHERIT
- **Description:** >

#### `csharp-pro`

- **Path:** `agents/languages/csharp_pro.md`
- **Model:** INHERIT
- **Description:** Write modern C# code with advanced features like records, pattern matching, and async/await. Optimizes .NET applications, implements enterprise patterns, and ensures comprehensive testing.
- **When to use:** Use PROACTIVELY for C# refactoring, performance optimization, or complex .NET solutions.

#### `elixir-pro`

- **Path:** `agents/languages/elixir_pro.md`
- **Model:** INHERIT
- **Description:** Write idiomatic Elixir code with OTP patterns, supervision trees, and Phoenix LiveView. Masters concurrency, fault tolerance, and distributed systems.
- **When to use:** Use PROACTIVELY for Elixir refactoring, OTP design, or complex BEAM optimizations.

#### `javascript-pro`

- **Path:** `agents/languages/javascript_pro.md`
- **Model:** INHERIT
- **Description:** Master modern JavaScript with ES6+, async patterns, and Node.js APIs. Handles promises, event loops, and browser/Node compatibility.
- **When to use:** Use PROACTIVELY for JavaScript optimization, async debugging, or complex JS patterns.

#### `php-pro`

- **Path:** `agents/languages/php_pro.md`
- **Model:** INHERIT
- **Description:** Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features.
- **When to use:** Use PROACTIVELY for high-performance PHP applications.

#### `ruby-pro`

- **Path:** `agents/languages/ruby_pro.md`
- **Model:** INHERIT
- **Description:** Write idiomatic Ruby code with metaprogramming, Rails patterns, and performance optimization. Specializes in Ruby on Rails, gem development, and testing frameworks.
- **When to use:** Use PROACTIVELY for Ruby refactoring, optimization, or complex Ruby features.

#### `scala-pro`

- **Path:** `agents/languages/scala_pro.md`
- **Model:** INHERIT
- **Description:** Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing. Expert in Apache Pekko, Akka, Spark, ZIO/Cats Effect, and reactive architectures.
- **When to use:** Use PROACTIVELY for Scala system design, performance optimization, or enterprise integration.

---

### Ml Ai

**5 agents in this category**

#### `ai-engineer`

- **Path:** `agents/ml-ai/ai_engineer.md`
- **Model:** INHERIT
- **Description:** Build production-ready LLM applications, advanced RAG systems, and intelligent agents. Implements vector search, multimodal AI, agent orchestration, and enterprise AI integrations.
- **When to use:** Use PROACTIVELY for LLM features, chatbots, AI agents, or AI-powered applications.

#### `data-scientist`

- **Path:** `agents/ml-ai/data_scientist.md`
- **Model:** INHERIT
- **Description:** Expert data scientist for advanced analytics, machine learning, and statistical modeling. Handles complex data analysis, predictive modeling, and business intelligence.
- **When to use:** Use PROACTIVELY for data analysis tasks, ML modeling, statistical analysis, and data-driven insights.

#### `ml-engineer`

- **Path:** `agents/ml-ai/ml_engineer.md`
- **Model:** INHERIT
- **Description:** Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks. Implements model serving, feature engineering, A/B testing, and monitoring.
- **When to use:** Use PROACTIVELY for ML model deployment, inference optimization, or production ML infrastructure.

#### `mlops-engineer`

- **Path:** `agents/ml-ai/mlops_engineer.md`
- **Model:** INHERIT
- **Description:** Build comprehensive ML pipelines, experiment tracking, and model registries with MLflow, Kubeflow, and modern MLOps tools. Implements automated training, deployment, and monitoring across cloud platforms.
- **When to use:** Use PROACTIVELY for ML infrastructure, experiment management, or pipeline automation.

#### `prompt-engineer`

- **Path:** `agents/ml-ai/prompt_engineer.md`
- **Model:** INHERIT
- **Description:** Expert prompt engineer specializing in advanced prompting techniques, LLM optimization, and AI system design. Masters chain-of-thought, constitutional AI, and production prompt strategies.
- **When to use:** Use when building AI features, improving agent performance, or crafting system prompts.

---

### Orchestration

**2 agents in this category**

#### `prompt-kit-ingestor`

- **Path:** `agents/orchestration/prompt-kit-ingestor.md`
- **Model:** SONNET
- **Description:** Repository curator agent for absorbing external prompt kits, prompt collections, and articles-with-embedded-prompts into this prompting-guides repository.
- **When to use:** Use PROACTIVELY whenever a new external markdown/text file containing reusable prompts is added to the repo and the user wants it processed into Tier-1 structured prompts, technique-tagged, indexed, and organized. Invokes the external-prompt-kit-ingestor skill end-to-end and delivers an implications memo.
- **Related agents:** primary tool, when an ingested kit clearly should become its own skill, agent creation patterns, placement authority

#### `context-manager`

- **Path:** `agents/orchestration/context_manager.md`
- **Model:** INHERIT
- **Description:** Elite AI context engineering specialist mastering dynamic context management, vector databases, knowledge graphs, and intelligent memory systems. Orchestrates context across multi-agent workflows, enterprise AI systems, and long-running projects with 2024/2025 best practices.
- **When to use:** Use PROACTIVELY for complex AI orchestration.

---

### Business Operations

**9 agents in this category**

#### ``

- **Path:** `agents/business-operations/marketing_content_generator.md`
- **Model:** SONNET
- **Description:** Takes a topic/feature and produces platform-optimized content: blog post, tweet thread, Reddit post, and Product Hunt comment. Designed for solo Android developers who need marketing content without a marketing team.

#### `business-analyst`

- **Path:** `agents/business-operations/business_analyst.md`
- **Model:** SONNET
- **Description:** Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights. Build comprehensive KPI frameworks, predictive models, and strategic recommendations.
- **When to use:** Use PROACTIVELY for business intelligence or strategic analysis.

#### `hr-pro`

- **Path:** `agents/business-operations/hr_pro.md`
- **Model:** SONNET
- **Description:** Professional, ethical HR partner for hiring, onboarding/offboarding, PTO and leave, performance, compliant policies, and employee relations. Ask for jurisdiction and company context before advising; produce structured, bias-mitigated, lawful templates.

#### `legal-advisor`

- **Path:** `agents/business-operations/legal_advisor.md`
- **Model:** SONNET
- **Description:** Draft privacy policies, terms of service, disclaimers, and legal notices. Creates GDPR-compliant texts, cookie policies, and data processing agreements.
- **When to use:** Use PROACTIVELY for legal documentation, compliance texts, or regulatory requirements.

#### `payment-integration`

- **Path:** `agents/business-operations/payment_integration.md`
- **Model:** SONNET
- **Description:** Integrate Stripe, PayPal, and payment processors. Handles checkout flows, subscriptions, webhooks, and PCI compliance.
- **When to use:** Use PROACTIVELY when implementing payments, billing, or subscription features.

#### `customer-support`

- **Path:** `agents/business-operations/customer_support.md`
- **Model:** HAIKU
- **Description:** Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis, and omnichannel support experiences. Integrates modern support tools, chatbot platforms, and CX optimization with 2024/2025 best practices.
- **When to use:** Use PROACTIVELY for comprehensive customer experience management.

#### `sales-automator`

- **Path:** `agents/business-operations/sales_automator.md`
- **Model:** HAIKU
- **Description:** Draft cold emails, follow-ups, and proposal templates. Creates pricing pages, case studies, and sales scripts.
- **When to use:** Use PROACTIVELY for sales outreach or lead nurturing.

#### `quant-analyst`

- **Path:** `agents/business-operations/quant_analyst.md`
- **Model:** INHERIT
- **Description:** Build financial models, backtest trading strategies, and analyze market data. Implements risk metrics, portfolio optimization, and statistical arbitrage.
- **When to use:** Use PROACTIVELY for quantitative finance, trading algorithms, or risk analysis.

#### `risk-manager`

- **Path:** `agents/business-operations/risk_manager.md`
- **Model:** INHERIT
- **Description:** Monitor portfolio risk, R-multiples, and position limits. Creates hedging strategies, calculates expectancy, and implements stop-losses.
- **When to use:** Use PROACTIVELY for risk assessment, trade tracking, or portfolio protection.

---

### Seo Marketing

**12 agents in this category**

#### `seo-authority-builder`

- **Path:** `agents/seo-marketing/seo_authority_builder.md`
- **Model:** SONNET
- **Description:** Analyzes content for E-E-A-T signals and suggests improvements to build authority and trust. Identifies missing credibility elements.
- **When to use:** Use PROACTIVELY for YMYL topics.

#### `seo-content-auditor`

- **Path:** `agents/seo-marketing/seo_content_auditor.md`
- **Model:** SONNET
- **Description:** Analyzes provided content for quality, E-E-A-T signals, and SEO best practices. Scores content and provides improvement recommendations based on established guidelines.
- **When to use:** Use PROACTIVELY for content review.

#### `seo-content-writer`

- **Path:** `agents/seo-marketing/seo_content_writer.md`
- **Model:** SONNET
- **Description:** Writes SEO-optimized content based on provided keywords and topic briefs. Creates engaging, comprehensive content following best practices.
- **When to use:** Use PROACTIVELY for content creation tasks.

#### `content-marketer`

- **Path:** `agents/seo-marketing/content_marketer.md`
- **Model:** HAIKU
- **Description:** Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO optimization, and data-driven performance marketing. Masters modern content tools, social media automation, and conversion optimization with 2024/2025 best practices.
- **When to use:** Use PROACTIVELY for comprehensive content marketing.

#### `search-specialist`

- **Path:** `agents/seo-marketing/search_specialist.md`
- **Model:** HAIKU
- **Description:** Expert web researcher using advanced search techniques and synthesis. Masters search operators, result filtering, and multi-source verification. Handles competitive analysis and fact-checking.
- **When to use:** Use PROACTIVELY for deep research, information gathering, or trend analysis.

#### `seo-cannibalization-detector`

- **Path:** `agents/seo-marketing/seo_cannibalization_detector.md`
- **Model:** HAIKU
- **Description:** Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues. Suggests differentiation strategies.
- **When to use:** Use PROACTIVELY when reviewing similar content.

#### `seo-content-planner`

- **Path:** `agents/seo-marketing/seo_content_planner.md`
- **Model:** HAIKU
- **Description:** Creates comprehensive content outlines and topic clusters for SEO. Plans content calendars and identifies topic gaps.
- **When to use:** Use PROACTIVELY for content strategy and planning.

#### `seo-content-refresher`

- **Path:** `agents/seo-marketing/seo_content_refresher.md`
- **Model:** HAIKU
- **Description:** Identifies outdated elements in provided content and suggests updates to maintain freshness. Finds statistics, dates, and examples that need updating.
- **When to use:** Use PROACTIVELY for older content.

#### `seo-keyword-strategist`

- **Path:** `agents/seo-marketing/seo_keyword_strategist.md`
- **Model:** HAIKU
- **Description:** Analyzes keyword usage in provided content, calculates density, suggests semantic variations and LSI keywords based on the topic. Prevents over-optimization.
- **When to use:** Use PROACTIVELY for content optimization.

#### `seo-meta-optimizer`

- **Path:** `agents/seo-marketing/seo_meta_optimizer.md`
- **Model:** HAIKU
- **Description:** Creates optimized meta titles, descriptions, and URL suggestions based on character limits and best practices. Generates compelling, keyword-rich metadata.
- **When to use:** Use PROACTIVELY for new content.

#### `seo-snippet-hunter`

- **Path:** `agents/seo-marketing/seo_snippet_hunter.md`
- **Model:** HAIKU
- **Description:** Formats content to be eligible for featured snippets and SERP features. Creates snippet-optimized content blocks based on best practices.
- **When to use:** Use PROACTIVELY for question-based content.

#### `seo-structure-architect`

- **Path:** `agents/seo-marketing/seo_structure_architect.md`
- **Model:** HAIKU
- **Description:** Analyzes and optimizes content structure including header hierarchy, suggests schema markup, and internal linking opportunities. Creates search-friendly content organization.
- **When to use:** Use PROACTIVELY for content structuring.

---

## Quick Reference

### Agents by Model Assignment

**OPUS** (36 agents)

- `architect-review` (architecture)
- `solo-dev-architect` (architecture)
- `data-engineer` (backend)
- `django-pro` (backend)
- `fastapi-pro` (backend)
- `graphql-architect` (backend)
- `cloud-architect` (cloud-infrastructure)
- `firebase-architecture-reviewer` (cloud-infrastructure)
- `firebase-security-auditor` (cloud-infrastructure)
- `hybrid-cloud-architect` (cloud-infrastructure)
- ... and 26 more

**SONNET** (43 agents)

- `c4-component` (architecture)
- `c4-container` (architecture)
- `c4-context` (architecture)
- `backend-security-coder` (backend)
- `` (business-operations)
- `business-analyst` (business-operations)
- `hr-pro` (business-operations)
- `legal-advisor` (business-operations)
- `payment-integration` (business-operations)
- `firebase-cost-analyst` (cloud-infrastructure)
- ... and 33 more

**HAIKU** (15 agents)

- `c4-code` (architecture)
- `customer-support` (business-operations)
- `sales-automator` (business-operations)
- `deployment-engineer` (deployment)
- `mermaid-expert` (documentation)
- `reference-builder` (documentation)
- `content-marketer` (seo-marketing)
- `search-specialist` (seo-marketing)
- `seo-cannibalization-detector` (seo-marketing)
- `seo-content-planner` (seo-marketing)
- ... and 5 more

**INHERIT (User Choice)** (25 agents)

- `backend-architect` (backend)
- `temporal-python-pro` (backend)
- `quant-analyst` (business-operations)
- `risk-manager` (business-operations)
- `database-optimizer` (database)
- `sql-pro` (database)
- `observability-engineer` (devops)
- `flutter-expert` (frontend-mobile)
- `frontend-developer` (frontend-mobile)
- `ios-developer` (frontend-mobile)
- ... and 15 more

---

## Additional Resources

- [Skills Index](../skills/README.md) - 132 modular knowledge packages
- [Commands Index](../commands/README.md) - 71 multi-agent orchestration workflows
- [Integration Guide](../documentation/integration_with_prompts.md) - How agents relate to prompts
- Future Processing Instructions - Detailed analysis tasks

## Contributing

This index was automatically generated from agent file analysis. To update:

1. Modify agent files in their respective category directories
2. Run `python3 analyze_agents.py` to regenerate analysis
3. Run `python3 generate_agent_readme.py` to update this README

---

*Last updated: 2026-04-20*

**Source Repositories:**
- [wshobson/agents](https://github.com/wshobson/agents) - MIT License
