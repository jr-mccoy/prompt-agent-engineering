<!-- INVENTORY_COUNTS: {"categories": {"accessibility": 2, "architecture": 2, "business": 3, "code-quality": 5, "creative": 3, "data-analysis": 1, "database": 2, "deployment": 2, "devops": 8, "documentation": 1, "education": 3, "framework-migration": 3, "git-workflows": 3, "healthcare": 4, "mobile-development": 12, "multi-agent": 8, "orchestration": 9, "other": 18, "performance": 3, "research": 3, "security": 6, "testing": 6, "troubleshooting": 5, "writing": 3}, "date": "2026-08-24", "total": 115, "type": "commands"} -->

# Claude Code Commands Index

**Total Commands:** 115 across 24 categories

**Last Updated:** 2026-08-24

---

## Table of Contents

- [Overview](#overview)
- [What Are Commands?](#what-are-commands)
- [Command Categories](#command-categories)
- [Quick Reference by Category](#quick-reference-by-category)
  - [Accessibility (3)](#--accessibility)
  - [Architecture (3)](#--architecture)
  - [Code Quality (6)](#--code-quality)
  - [Database (3)](#--database)
  - [Deployment (3)](#--deployment)
  - [Devops (9)](#--devops)
  - [Documentation (2)](#--documentation)
  - [Framework Migration (4)](#--framework-migration)
  - [Git Workflows (4)](#--git-workflows)
  - [Mobile Development (13)](#--mobile-development)
  - [Multi Agent (9)](#--multi-agent)
  - [Orchestration (11)](#--orchestration)
  - [Other (20)](#--other)
  - [Performance (4)](#--performance)
  - [Security (7)](#--security)
  - [Testing (7)](#--testing)
  - [Troubleshooting (6)](#--troubleshooting)
- [Command Types](#command-types)
- [Usage Patterns](#usage-patterns)
- [Integration Guide](#integration-guide)

---

## Overview

Commands in Claude Code are **multi-agent orchestration workflows** that coordinate specialized agents to execute complex, multi-phase operations. Unlike simple prompts or single-purpose agents, commands represent entire development processes from architecture through deployment.

**Key Characteristics:**
- **Multi-phase workflows** with sequential agent coordination
- **Output handoffs** where each agent consumes previous results
- **Validation gates** ensuring quality at each phase
- **Domain specialization** with expert agents for each task

## Command Counting Definition

- **Command:** any Markdown file under `domain-agentic-resources/commands/**/*.md`, excluding category `README.md` files.
- **Workflow command:** a command subtype used for multi-step orchestration. Workflow commands are **not** added on top of command totals.


## What Are Commands?

Commands are slash commands (e.g., `/full-stack-feature`, `/security-hardening`) that trigger comprehensive workflows. They differ from agents and skills:

| Feature | Commands | Agents | Skills |
|---------|----------|--------|--------|
| **Purpose** | Multi-step orchestration | Specialized identity | Knowledge package |
| **Scope** | End-to-end workflows | Single domain expertise | Progressive disclosure |
| **Coordination** | Multiple agents | Single agent | Referenced by agents |
| **Duration** | Long-running process | Per-task invocation | Always available |
| **Example** | `/full-stack-feature` | `backend-architect` | `async-python-patterns` |

## Command Categories

Commands are organized into 15 categories based on their primary domain:

| Category | Count | Description |
|----------|-------|-------------|
| Other | 18 | Various development commands |
| Mobile Development | 12 | Various development commands |
| Orchestration | 9 | Various development commands |
| Devops | 8 | Various development commands |
| Multi Agent | 8 | Various development commands |
| Security | 6 | Various development commands |
| Testing | 6 | Various development commands |
| Code Quality | 5 | Various development commands |
| Troubleshooting | 5 | Various development commands |
| Healthcare | 4 | Various development commands |
| Business | 3 | Various development commands |
| Creative | 3 | Various development commands |
| Education | 3 | Various development commands |
| Framework Migration | 3 | Various development commands |
| Git Workflows | 3 | Various development commands |
| Performance | 3 | Various development commands |
| Research | 3 | Various development commands |
| Writing | 3 | Various development commands |
| Accessibility | 2 | Various development commands |
| Architecture | 2 | Various development commands |
| Database | 2 | Various development commands |
| Deployment | 2 | Various development commands |
| Data Analysis | 1 | Various development commands |
| Documentation | 1 | Various development commands |

## Quick Reference by Category

Jump to any category:

- **[Accessibility](#--accessibility)** - 3 commands
- **[Architecture](#--architecture)** - 3 commands
- **[Code Quality](#--code-quality)** - 6 commands
- **[Database](#--database)** - 3 commands
- **[Deployment](#--deployment)** - 3 commands
- **[Devops](#--devops)** - 9 commands
- **[Documentation](#--documentation)** - 2 commands
- **[Framework Migration](#--framework-migration)** - 4 commands
- **[Git Workflows](#--git-workflows)** - 4 commands
- **[Mobile Development](#--mobile-development)** - 13 commands
- **[Multi Agent](#--multi-agent)** - 9 commands
- **[Orchestration](#--orchestration)** - 11 commands
- **[Other](#--other)** - 20 commands
- **[Performance](#--performance)** - 4 commands
- **[Security](#--security)** - 7 commands
- **[Testing](#--testing)** - 7 commands
- **[Troubleshooting](#--troubleshooting)** - 6 commands

---

## Commands by Category

### 🔹 Orchestration

**11 commands**

### README

**Path:** `commands/orchestration/README.md`

**Syntax:** `/context-restore`

**Description:** > Commands for multi-agent coordination, context management, and full-stack feature development.

---

### context-restore

**Path:** `commands/orchestration/context_restore.md`

**Syntax:** `/context-restore`

**Description:** Expert Context Restoration Specialist focused on intelligent, semantic-aware context retrieval and...

---

### context-save

**Path:** `commands/orchestration/context_save.md`

**Syntax:** `/context-save`

**Description:** An elite context engineering specialist focused on comprehensive, semantic, and dynamically...

---

### full-stack-feature

**Path:** `commands/orchestration/full_stack_feature.md`

**Syntax:** `/full-stack-feature`

**Description:** Orchestrate full-stack feature development across backend, frontend, and infrastructure layers with API-first approach

**Orchestrates:** `backend-architect`, `database-architect`, `deployment-engineer`, `frontend-developer`, `performance-engineer`, `python-pro`, `security-auditor`, `sql-pro`, `test-automator`

---

### improve-agent

**Path:** `commands/orchestration/improve_agent.md`

**Syntax:** `/improve-agent`

**Description:** Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration.

---

### issue

**Path:** `commands/orchestration/issue.md`

**Syntax:** `/issue`

**Description:** You are a GitHub issue resolution expert specializing in systematic bug investigation, feature...

---

### multi-agent-optimize

**Path:** `commands/orchestration/multi_agent_optimize.md`

**Syntax:** `/multi-agent-optimize`

**Description:** The Multi-Agent Optimization Tool is an advanced AI-driven framework designed to holistically...

---

### solo-dev-retro

**Path:** `commands/orchestration/solo_dev_retro.md`

**Syntax:** `/solo-dev-retro`

**Description:** Solo developer retrospective that reviews the past sprint/week. Analyzes git history, VIBE-TODOs, decision log, and codebase health to produce a "state of the project" report with prioritized action items for the next sprint.

**Orchestrates:** `solo-dev-architect`, `solo-dev-reviewer`, `mobile-developer`

---

### solo-dev-sprint-plan

**Path:** `commands/orchestration/solo_dev_sprint_plan.md`

**Syntax:** `/solo-dev-sprint-plan`

**Description:** Sprint planning optimized for a team of one. Analyzes current project state, backlog, past velocity, and available capacity to produce a realistic 1-2 week plan using half-day estimates instead of story points.

**Orchestrates:** `solo-dev-architect`, `mobile-developer`

---

### standup-notes

**Path:** `commands/orchestration/standup_notes.md`

**Syntax:** `/standup-notes`

**Description:** You are an expert team communication specialist focused on async-first standup practices,...

---

### vibe-session

**Path:** `commands/orchestration/vibe_session.md`

**Syntax:** `/vibe-session`

**Description:** Structured vibe coding session from idea to committed working code. Defines scope, scaffolds fast, iterates to working state, drops VIBE-TODO markers, and ends with a clean commit and light review. Time-boxed to prevent scope creep.

**Orchestrates:** `vibe-coding-partner`, `solo-dev-reviewer`

---

### 🔹 Security

**7 commands**

### README

**Path:** `commands/security/README.md`

**Syntax:** `/compliance-check`

**Description:** > Commands for security scanning, compliance checking, and vulnerability analysis.

---

### android-pre-release-security-audit

**Path:** `commands/security/android_pre_release_security_audit.md`

**Syntax:** `/android-pre-release-security-audit`

**Description:** Android-specific security audit covering OWASP MASVS, Firebase security rules, local data protection, network security, authentication, billing security, location privacy, and Play Store data safety compliance

**Orchestrates:** `security-auditor`, `threat-modeling-expert`, `mobile-developer`

---

### compliance-check

**Path:** `commands/security/compliance_check.md`

**Syntax:** `/compliance-check`

**Description:** You are a compliance expert specializing in regulatory requirements for software systems including...

---

### security-dependencies

**Path:** `commands/security/security_dependencies.md`

**Syntax:** `/security-dependencies`

**Description:** You are a security expert specializing in dependency vulnerability analysis, SBOM generation, and...

---

### security-hardening

**Path:** `commands/security/security_hardening.md`

**Syntax:** `/security-hardening`

**Description:** Implement comprehensive security hardening with defense-in-depth strategy through multi-agent orchestration

**Orchestrates:** `backend-architect`, `backend-security-coder`, `deployment-engineer`, `devops-troubleshooter`, `domain-specific`, `frontend-security-coder`, `mobile-security-coder`, `security-auditor`

---

### security-sast

**Path:** `commands/security/security_sast.md`

**Syntax:** `/security_sast`

**Description:** SAST Security Plugin

---

### xss-scan

**Path:** `commands/security/xss_scan.md`

**Syntax:** `/xss-scan`

**Description:** You are a frontend security specialist focusing on Cross-Site Scripting (XSS) vulnerability...

---

### 🔹 Testing

**7 commands**

### README

**Path:** `commands/testing/README.md`

**Syntax:** `/tdd-cycle`

**Description:** > Commands for test-driven development, test generation, and comprehensive test automation.

---

### android-test-matrix

**Path:** `commands/testing/android_test_matrix.md`

**Syntax:** `/android-test-matrix`

**Description:** Configures and executes a test matrix across multiple Android API levels and screen configurations. Sets up emulators or Gradle Managed Devices, runs instrumented tests, aggregates results, and highlights device-specific failures.

**Orchestrates:** `android-device-farm-operator`, `test-automator`, `android-adb-specialist`

---

### tdd-cycle

**Path:** `commands/testing/tdd_cycle.md`

**Syntax:** `/tdd-cycle`

**Description:** Execute comprehensive Test-Driven Development workflow with strict red-green-refactor discipline

**Orchestrates:** `architect-review`, `backend-architect`, `code-reviewer`, `test-automator`

---

### tdd-green

**Path:** `commands/testing/tdd_green.md`

**Syntax:** `/tdd-green`

**Description:** Use Task tool with subagenttype="unit-testing::test-automator" to implement minimal passing code....

**Orchestrates:** `test-automator`

---

### tdd-red

**Path:** `commands/testing/tdd_red.md`

**Syntax:** `/tdd-red`

**Description:** Generate failing tests using Task tool with subagenttype="unit-testing::test-automator". "Generate...

**Orchestrates:** `test-automator`

---

### tdd-refactor

**Path:** `commands/testing/tdd_refactor.md`

**Syntax:** `/tdd-refactor`

**Description:** Use Task tool with subagent_type tdd-orchestrator to perform safe refactoring of the target code.

**Orchestrates:** `tdd-orchestrator`

---

### test-generate

**Path:** `commands/testing/test_generate.md`

**Syntax:** `/test-generate`

**Description:** You are a test automation expert specializing in generating comprehensive, maintainable unit tests...

---

### 🔹 Other

**20 commands**

### README

**Path:** `commands/README.md`

**Syntax:** `/full-stack-feature`

**Description:** <!-- INVENTORY_COUNTS: {"categories": {"accessibility": 1, "architecture": 1, "code-quality": 5, "database": 1, "deployment": 1, "devops": 8, "documentation": 1, "framework-migration": 3, "git-workflo...

---

### README

**Path:** `commands/other/README.md`

**Syntax:** `/api-mock`

**Description:** > Miscellaneous commands for various development tasks including scaffolding, debugging, and data pipelines.

---

### api-mock

**Path:** `commands/other/api_mock.md`

**Syntax:** `/api-mock`

**Description:** You are an API mocking expert specializing in creating realistic mock services for development,...

---

### code-explain

**Path:** `commands/other/code_explain.md`

**Syntax:** `/code-explain`

**Description:** You are a code education expert specializing in explaining complex code through clear narratives,...

---

### data-driven-feature

**Path:** `commands/other/data_driven_feature.md`

**Syntax:** `/data-driven-feature`

**Description:** Build features guided by data insights, A/B testing, and continuous measurement using specialized...

**Orchestrates:** `backend-architect`, `business-analyst`, `data-engineer`, `data-scientist`, `deployment-engineer`, `frontend-developer`, `ml-engineer`, `observability-engineer`

---

### debug-trace

**Path:** `commands/other/debug_trace.md`

**Syntax:** `/debug-trace`

**Description:** You are a debugging expert specializing in setting up comprehensive debugging environments,...

---

### deps-audit

**Path:** `commands/other/deps_audit.md`

**Syntax:** `/deps-audit`

**Description:** You are a dependency security expert specializing in vulnerability scanning, license compliance,...

---

### doc-generate

**Path:** `commands/other/doc_generate.md`

**Syntax:** `/doc-generate`

**Description:** You are a documentation expert specializing in creating comprehensive, maintainable documentation...

---

### error-analysis

**Path:** `commands/other/error_analysis.md`

**Syntax:** `/health`

**Description:** You are an expert error analysis specialist with deep expertise in debugging distributed systems,...

---

### error-trace

**Path:** `commands/other/error_trace.md`

**Syntax:** `/error-trace`

**Description:** You are an error tracking and observability expert specializing in implementing comprehensive error...

---

### feature-development

**Path:** `commands/other/feature_development.md`

**Syntax:** `/feature-development`

**Description:** Orchestrate end-to-end feature development from requirements to production deployment

**Orchestrates:** `architect-review`, `backend-architect`, `business-analyst`, `data-engineer`, `deployment-engineer`, `docs-architect`, `frontend-developer`, `observability-engineer`, `performance-engineer`, `security-auditor`
  _(+ 1 more agents)_

---

### full-review

**Path:** `commands/other/full_review.md`

**Syntax:** `/full-review`

**Description:** Orchestrate comprehensive multi-dimensional code review using specialized review agents

**Orchestrates:** `architect-review`, `code-reviewer`, `deployment-engineer`, `docs-architect`, `legacy-modernizer`, `performance-engineer`, `security-auditor`, `test-automator`

---

### ml-pipeline

**Path:** `commands/other/ml_pipeline.md`

**Syntax:** `/ml-pipeline`

**Description:** Design and implement a complete ML pipeline for $ARGUMENTS. This workflow orchestrates multiple agents.

---

### multi-platform

**Path:** `commands/other/multi_platform.md`

**Syntax:** `/multi-platform`

**Description:** Build and deploy the same feature consistently across web, mobile, and desktop platforms using...

**Orchestrates:** `api-documenter`, `architect-review`, `backend-architect`, `frontend-developer`, `ios-developer`, `mobile-developer`, `performance-engineer`, `test-automator`, `ui-ux-designer`

---

### pr-enhance

**Path:** `commands/other/pr_enhance.md`

**Syntax:** `/pr-enhance`

**Description:** You are a PR optimization expert specializing in creating high-quality pull requests that...

---

### python-scaffold

**Path:** `commands/other/python_scaffold.md`

**Syntax:** `/python-scaffold`

**Description:** You are a Python project architecture expert specializing in scaffolding production-ready Python...

---

### refactor-clean

**Path:** `commands/other/refactor_clean.md`

**Syntax:** `/refactor-clean`

**Description:** You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and...

---

### rust-project

**Path:** `commands/other/rust_project.md`

**Syntax:** `/rust-project`

**Description:** You are a Rust project architecture expert specializing in scaffolding production-ready Rust...

---

### smart-debug

**Path:** `commands/other/smart_debug.md`

**Syntax:** `/smart-debug`

**Description:** Process issue from $ARGUMENTS. Parse for error messages, stack traces, reproduction steps.

**Orchestrates:** `debugger`

---

### tech-debt

**Path:** `commands/other/tech_debt.md`

**Syntax:** `/tech-debt`

**Description:** You are a technical debt expert specializing in identifying, quantifying, and prioritizing...

---

### 🔹 Mobile Development

**13 commands**

### README

**Path:** `commands/mobile-development/README.md`

**Syntax:** `/android-gradle-upgrade`

**Description:** > Commands for Android and iOS project initialization, upgrades, and mobile-specific workflows.

---

### android-adb-health-check

**Path:** `commands/mobile-development/android_adb_health_check.md`

**Syntax:** `/android-adb-health-check`

**Description:** Quick device and app health check via ADB. Captures device state, app memory usage, running services, battery impact, and recent crash logs in a single report. Designed to run in under 60 seconds.

**Orchestrates:** `android-adb-specialist`, `mobile-developer`

---

### android-behavior-audit

**Path:** `commands/mobile-development/android_behavior_audit.md`

**Syntax:** `/android-behavior-audit`

**Description:** Orchestrate comprehensive Android app behavior audit across survey, deep code tracing, behavioral scrutiny, developer clarification, and fix planning to align actual code behavior with developer intent

**Orchestrates:** `android-app-surveyor`, `android-behavior-tracer`, `android-behavior-auditor`, `android-behavior-fix-planner`

---

### android-beta-launch

**Path:** `commands/mobile-development/android_beta_launch.md`

**Syntax:** `/android-beta-launch`

**Description:** Orchestrate comprehensive Android beta launch preparation across security, performance, Firebase validation, test coverage, and Play Store compliance with go/no-go release decision

**Orchestrates:** `android-release-manager`, `security-auditor`, `performance-engineer`, `tdd-orchestrator`, `test-automator`, `mobile-developer`

---

### android-daily-standup

**Path:** `commands/mobile-development/android_daily_standup.md`

**Syntax:** `/android-daily-standup`

**Description:** Morning startup command that reviews last session's changes, checks CI status, pulls latest crash reports, reviews support inbox, and suggests daily priorities based on impact and urgency

**Orchestrates:** `android-release-manager`, `mobile-developer`, `firebase-cost-analyst`

---

### android-gradle-upgrade

**Path:** `commands/mobile-development/android_gradle_upgrade.md`

**Syntax:** `/android-gradle-upgrade`

**Description:** Upgrade Android Gradle Plugin (AGP) and dependencies with compatibility verification and migration...

---

### android-init

**Path:** `commands/mobile-development/android_init.md`

**Syntax:** `/android-init`

**Description:** Initialize a modern Android project with MVVM architecture, Hilt dependency injection, Jetpack...

---

### android-monetization-setup

**Path:** `commands/mobile-development/android_monetization_setup.md`

**Syntax:** `/android-monetization-setup`

**Description:** Orchestrate complete Android monetization implementation including Google Play Billing, subscriptions, AdMob, paywalls, server-side verification, and policy compliance

**Orchestrates:** `android-monetization-architect`, `android-release-manager`, `mobile-developer`, `security-auditor`, `test-automator`

---

### android-ship-check

**Path:** `commands/mobile-development/android_ship_check.md`

**Syntax:** `/android-ship-check`

**Description:** Pre-release verification command that runs the full test suite, checks for regressions, validates ProGuard rules, verifies Play Store policy compliance, checks Firebase security rules, and produces a go/no-go report

**Orchestrates:** `android-release-manager`, `firebase-security-auditor`, `compliance-scanner`, `mobile-developer`, `test-automator`

---

### android-weekly-review

**Path:** `commands/mobile-development/android_weekly_review.md`

**Syntax:** `/android-weekly-review`

**Description:** Weekly review command that pulls metrics from Play Console, Firebase, and codebase to produce a weekly summary with key metrics, trend analysis, and next-week recommendations

**Orchestrates:** `android-release-manager`, `firebase-cost-analyst`, `mobile-developer`

---

### mobile-ui-addictiveness-audit

**Path:** `commands/mobile-development/mobile_ui_addictiveness_audit.md`

**Syntax:** `/mobile-ui-addictiveness-audit`

**Description:** Orchestrate a comprehensive audit of an app's engagement and habit-forming potential across behavioral psychology frameworks, analyzing triggers, core loops, reward systems, retention mechanics, and emotional design to produce an actionable engagement improvement plan

**Orchestrates:** `mobile-ui-addiction-architect`, `mobile-ui-element-analyzer`, `mobile-ui-competitive-teardown`

---

### mobile-ui-element-audit

**Path:** `commands/mobile-development/mobile_ui_element_audit.md`

**Syntax:** `/mobile-ui-element-audit`

**Description:** Orchestrate a comprehensive UI element audit across trend research, element-level analysis, engagement optimization, and implementation planning to transform specific mobile UI elements from functional to exceptional

**Orchestrates:** `mobile-ui-trend-researcher`, `mobile-ui-element-analyzer`, `mobile-ui-addiction-architect`

---

### mobile-ui-trend-report

**Path:** `commands/mobile-development/mobile_ui_trend_report.md`

**Syntax:** `/mobile-ui-trend-report`

**Description:** Generate a comprehensive mobile UI trend report covering visual design, interaction patterns, engagement mechanics, and platform-specific innovations with actionable recommendations tailored to the user's app category and tech stack

**Orchestrates:** `mobile-ui-trend-researcher`, `mobile-ui-competitive-teardown`, `mobile-ui-addiction-architect`

---

### 🔹 Devops

**9 commands**

### README

**Path:** `commands/devops/README.md`

**Syntax:** `/ai-assistant`

**Description:** > Commands for CI/CD automation, monitoring setup, dependency management, and infrastructure workflows.

---

### ai-assistant

**Path:** `commands/devops/ai_assistant.md`

**Syntax:** `/ai-assistant`

**Description:** You are an AI assistant development expert specializing in creating intelligent conversational...

---

### deps-audit

**Path:** `commands/devops/deps_audit.md`

**Syntax:** `/deps-audit`

**Description:** You are a dependency security expert specializing in vulnerability scanning, license compliance,...

---

### langchain-agent

**Path:** `commands/devops/langchain_agent.md`

**Syntax:** `/langchain-agent`

**Description:** You are an expert LangChain agent developer specializing in production-grade AI systems using...

---

### monitor-setup

**Path:** `commands/devops/monitor_setup.md`

**Syntax:** `/monitor-setup`

**Description:** You are a monitoring and observability expert specializing in implementing comprehensive monitoring...

---

### prompt-optimize

**Path:** `commands/devops/prompt_optimize.md`

**Syntax:** `/prompt-optimize`

**Description:** You are an expert prompt engineer specializing in crafting effective prompts for LLMs through...

---

### slo-implement

**Path:** `commands/devops/slo_implement.md`

**Syntax:** `/slo-implement`

**Description:** You are an SLO (Service Level Objective) expert specializing in implementing reliability standards...

---

### typescript-scaffold

**Path:** `commands/devops/typescript_scaffold.md`

**Syntax:** `/typescript-scaffold`

**Description:** You are a TypeScript project architecture expert specializing in scaffolding production-ready...

---

### workflow-automate

**Path:** `commands/devops/workflow_automate.md`

**Syntax:** `/workflow-automate`

**Description:** You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub...

---

### 🔹 Multi Agent

**9 commands**

### README

**Path:** `commands/multi-agent/README.md`

**Syntax:** `/README`

**Description:** **Purpose:** A complete system for scaling multi-agent architectures with simplicity. These prompts form a sequential workflow to diagnose, design, and operate multi-agent systems.

---

### multiagent-choke-point-analysis

**Path:** `commands/multi-agent/multiagent_choke_point_analysis.md`

**Syntax:** `/multiagent_choke_point_analysis`

**Description:** Coordination Choke Points

---

### multiagent-judge-criteria

**Path:** `commands/multi-agent/multiagent_judge_criteria.md`

**Syntax:** `/multiagent_judge_criteria`

**Description:** Judge Criteria

---

### multiagent-scale-diagnosis

**Path:** `commands/multi-agent/multiagent_scale_diagnosis.md`

**Syntax:** `/multiagent_scale_diagnosis`

**Description:** Scale or Fix First?

---

### multiagent-session-lifecycle

**Path:** `commands/multi-agent/multiagent_session_lifecycle.md`

**Syntax:** `/multiagent_session_lifecycle`

**Description:** Session Lifecycle

---

### multiagent-tool-diet

**Path:** `commands/multi-agent/multiagent_tool_diet.md`

**Syntax:** `/multiagent_tool_diet`

**Description:** Tool Diet

---

### multiagent-two-tier-templates

**Path:** `commands/multi-agent/multiagent_two_tier_templates.md`

**Syntax:** `/multiagent_two_tier_templates`

**Description:** Two-Tier Architecture Templates

---

### multiagent-verification-merge

**Path:** `commands/multi-agent/multiagent_verification_merge.md`

**Syntax:** `/multiagent_verification_merge`

**Description:** Verification + Merge Policy

---

### multiagent-worker-boundaries

**Path:** `commands/multi-agent/multiagent_worker_boundaries.md`

**Syntax:** `/multiagent_worker_boundaries`

**Description:** Worker Boundaries

---

### 🔹 Code Quality

**6 commands**

### README

**Path:** `commands/code-quality/README.md`

**Syntax:** `/ai-review`

**Description:** > Commands for code review, refactoring, technical debt analysis, and quality improvement.

---

### ai-review

**Path:** `commands/code-quality/ai_review.md`

**Syntax:** `/ai-review`

**Description:** You are an expert AI-powered code review specialist combining automated static analysis,...

---

### codebase-health-check

**Path:** `commands/code-quality/codebase_health_check.md`

**Syntax:** `/codebase-health-check`

**Description:** Orchestrate a comprehensive codebase health assessment across security, dependencies, code quality, architecture, and test coverage using multiple specialized agents

**Orchestrates:** `tech-debt-reducer`, `security-auditor`, `test-automator`, `backend-architect`

---

### context-restore

**Path:** `commands/code-quality/context_restore.md`

**Syntax:** `/context-restore`

**Description:** Expert Context Restoration Specialist focused on intelligent, semantic-aware context retrieval and...

---

### refactor-clean

**Path:** `commands/code-quality/refactor_clean.md`

**Syntax:** `/refactor-clean`

**Description:** You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and...

---

### tech-debt

**Path:** `commands/code-quality/tech_debt.md`

**Syntax:** `/tech-debt`

**Description:** You are a technical debt expert specializing in identifying, quantifying, and prioritizing...

---

### 🔹 Troubleshooting

**6 commands**

### README

**Path:** `commands/troubleshooting/README.md`

**Syntax:** `/error-analysis`

**Description:** > Commands for error analysis, incident response, and intelligent debugging.

---

### error-analysis

**Path:** `commands/troubleshooting/error_analysis.md`

**Syntax:** `/health`

**Description:** You are an expert error analysis specialist with deep expertise in debugging distributed systems,...

---

### error-trace

**Path:** `commands/troubleshooting/error_trace.md`

**Syntax:** `/error-trace`

**Description:** You are an error tracking and observability expert specializing in implementing comprehensive error...

---

### incident-response

**Path:** `commands/troubleshooting/incident_response.md`

**Syntax:** `/incident-response`

**Description:** Orchestrate multi-agent incident response with modern SRE practices for rapid resolution and learning

**Orchestrates:** `backend-architect`, `content-marketer`, `debugger`, `deployment-engineer`, `docs-architect`, `incident-responder`, `observability-engineer`, `performance-engineer`, `security-auditor`

---

### multi-agent-review

**Path:** `commands/troubleshooting/multi_agent_review.md`

**Syntax:** `/multi-agent-review`

**Description:** A sophisticated AI-powered code review system designed to provide comprehensive, multi-perspective...

---

### smart-fix

**Path:** `commands/troubleshooting/smart_fix.md`

**Syntax:** `/smart-fix`

**Description:** Multi-agent debugging pipeline using error-detective and debugger agents for intelligent issue resolution.

**Orchestrates:** `backend-architect`, `code-reviewer`, `database-optimizer`, `debugger`, `devops-troubleshooter`, `error-detective`, `golang-pro`, `performance-engineer`, `python-pro`, `rust-pro`
  _(+ 3 more agents)_

---

### 🔹 Framework Migration

**4 commands**

### README

**Path:** `commands/framework-migration/README.md`

**Syntax:** `/code-migrate`

**Description:** > Commands for codebase migration, legacy modernization, and dependency upgrades.

---

### code-migrate

**Path:** `commands/framework-migration/code_migrate.md`

**Syntax:** `/code-migrate`

**Description:** You are a code migration expert specializing in transitioning codebases between frameworks,...

---

### deps-upgrade

**Path:** `commands/framework-migration/deps_upgrade.md`

**Syntax:** `/deps-upgrade`

**Description:** You are a dependency management expert specializing in safe, incremental upgrades of project...

---

### legacy-modernize

**Path:** `commands/framework-migration/legacy_modernize.md`

**Syntax:** `/legacy-modernize`

**Description:** Orchestrate a comprehensive legacy system modernization using the strangler fig pattern, enabling...

**Orchestrates:** `architect-review`, `backend-architect`, `business-analyst`, `data-engineer`, `deployment-engineer`, `docs-architect`, `legacy-modernizer`, `performance-engineer`, `python-pro`, `security-auditor`
  _(+ 1 more agents)_

---

### 🔹 Git Workflows

**4 commands**

### README

**Path:** `commands/git-workflows/README.md`

**Syntax:** `/git-workflow`

**Description:** > Commands for Git workflow automation, PR management, and team onboarding.

---

### git-workflow

**Path:** `commands/git-workflows/git_workflow.md`

**Syntax:** `/git-workflow`

**Description:** Orchestrate a comprehensive git workflow from code review through PR creation, leveraging...

**Orchestrates:** `code-reviewer`, `deployment-engineer`, `docs-architect`, `prompt-engineer`, `test-automator`

---

### onboard

**Path:** `commands/git-workflows/onboard.md`

**Syntax:** `/onboard`

**Description:** You are an expert onboarding specialist and knowledge transfer architect with deep experience in...

---

### pr-enhance

**Path:** `commands/git-workflows/pr_enhance.md`

**Syntax:** `/pr-enhance`

**Description:** You are a PR optimization expert specializing in creating high-quality pull requests that...

---

### 🔹 Performance

**4 commands**

### README

**Path:** `commands/performance/README.md`

**Syntax:** `/ai-review`

**Description:** > Commands for performance optimization, profiling, and AI-powered code review.

---

### ai-review

**Path:** `commands/performance/ai_review.md`

**Syntax:** `/ai-review`

**Description:** You are an expert AI-powered code review specialist combining automated static analysis,...

---

### multi-agent-review

**Path:** `commands/performance/multi_agent_review.md`

**Syntax:** `/multi-agent-review`

**Description:** A sophisticated AI-powered code review system designed to provide comprehensive, multi-perspective...

---

### performance-optimization

**Path:** `commands/performance/performance_optimization.md`

**Syntax:** `/performance-optimization`

**Description:** Optimize application performance end-to-end using specialized performance and optimization agents

**Orchestrates:** `backend-architect`, `cloud-architect`, `database-optimizer`, `frontend-developer`, `mobile-developer`, `observability-engineer`, `performance-engineer`, `test-automator`

---

### 🔹 Accessibility

**3 commands**

### README

**Path:** `commands/accessibility/README.md`

**Syntax:** `/accessibility-audit`

**Description:** > Commands for comprehensive accessibility auditing and WCAG compliance verification.

---

### accessibility-audit

**Path:** `commands/accessibility/accessibility_audit.md`

**Syntax:** `/accessibility-audit`

**Description:** You are an accessibility expert specializing in WCAG compliance, inclusive design, and assistive...

---

### component-scaffold

**Path:** `commands/accessibility/component_scaffold.md`

**Syntax:** `/component-scaffold`

**Description:** You are a React component architecture expert specializing in scaffolding production-ready,...

---

### 🔹 Architecture

**3 commands**

### README

**Path:** `commands/architecture/README.md`

**Syntax:** `/c4-architecture`

**Description:** > Commands for software architecture documentation, analysis, and C4 model generation.

---

### c4-architecture

**Path:** `commands/architecture/c4_architecture.md`

**Syntax:** `/c4-architecture:c4-architecture`

**Description:** Generate comprehensive C4 architecture documentation for an existing repository/codebase using a...

**Orchestrates:** `c4-code`, `c4-component`, `c4-container`, `c4-context`

---

### data-pipeline

**Path:** `commands/architecture/data_pipeline.md`

**Syntax:** `/data-pipeline`

**Description:** You are a data pipeline architecture expert specializing in scalable, reliable, and cost-effective...

---

### 🔹 Database

**3 commands**

### README

**Path:** `commands/database/README.md`

**Syntax:** `/cost-optimize`

**Description:** > Commands for database optimization, cost analysis, and performance tuning.

---

### cost-optimize

**Path:** `commands/database/cost_optimize.md`

**Syntax:** `/cost-optimize`

**Description:** You are a cloud cost optimization expert specializing in reducing infrastructure expenses while...

---

### sql-migrations

**Path:** `commands/database/sql_migrations.md`

**Syntax:** `/sql_migrations`

**Description:** SQL Database Migration Strategy and Implementation

---

### 🔹 Deployment

**3 commands**

### README

**Path:** `commands/deployment/README.md`

**Syntax:** `/config-validate`

**Description:** > Commands for configuration validation, deployment verification, and release management.

---

### config-validate

**Path:** `commands/deployment/config_validate.md`

**Syntax:** `/config-validate`

**Description:** You are a configuration management expert specializing in validating, testing, and ensuring the...

---

### migration-observability

**Path:** `commands/deployment/migration_observability.md`

**Syntax:** `/migration_observability`

**Description:** Migration Observability and Real-time Monitoring

---

### 🔹 Documentation

**2 commands**

### README

**Path:** `commands/documentation/README.md`

**Syntax:** `/doc-generate`

**Description:** > Commands for automated documentation generation, API docs, and technical writing.

---

### doc-generate

**Path:** `commands/documentation/doc_generate.md`

**Syntax:** `/doc-generate`

**Description:** You are a documentation expert specializing in creating comprehensive, maintainable documentation...

---

## Command Types

Commands can be categorized by their coordination patterns:

### Orchestration Commands (11)

Complex multi-phase workflows coordinating 5+ specialized agents:

- `/context-restore` - 0 agents
- `/context-restore` - 0 agents
- `/context-save` - 0 agents
- `/full-stack-feature` - 9 agents
- `/improve-agent` - 0 agents
- `/issue` - 0 agents
- `/multi-agent-optimize` - 0 agents
- `/solo-dev-retro` - 3 agents
- `/solo-dev-sprint-plan` - 2 agents
- `/standup-notes` - 0 agents
- _(+ 1 more)_

### Multi-Agent Workflows (13)

Workflows coordinating 2-4 agents for focused tasks:

- `/android-beta-launch` - 6 agents
- `/android-monetization-setup` - 5 agents
- `/android-ship-check` - 5 agents
- `/data-driven-feature` - 8 agents
- `/feature-development` - 11 agents
- `/full-review` - 8 agents
- `/git-workflow` - 5 agents
- `/incident-response` - 9 agents
- `/legacy-modernize` - 11 agents
- `/multi-platform` - 9 agents
- _(+ 3 more)_

### Single-Agent Commands (4)

Commands that invoke a single specialized agent:

- `/smart-debug` - debugger
- `/tdd-green` - test-automator
- `/tdd-red` - test-automator
- `/tdd-refactor` - tdd-orchestrator

### Direct Execution Commands (74)

Commands that execute without explicit agent coordination:

- `/accessibility-audit`
- `/c4-architecture`
- `/ai-review`
- `/cost-optimize`
- `/config-validate`
- `/ai-assistant`
- `/doc-generate`
- `/code-migrate`
- `/git-workflow`
- `/android-gradle-upgrade`
- _(+ 64 more)_

## Usage Patterns

### Basic Command Invocation

```bash
# Simple command
/command-name

# Command with arguments
/command-name "implement user authentication"

# Command with context
/full-stack-feature "add payment processing with Stripe"
```

### Workflow Execution

Commands execute in phases with validation gates:

```
Phase 1: Planning & Architecture
  ↓ (validation gate)
Phase 2: Implementation
  ↓ (validation gate)
Phase 3: Testing & Verification
  ↓ (validation gate)
Phase 4: Deployment & Monitoring
```

## Integration Guide

### When to Use Commands vs Agents vs Skills

**Use Commands when:**
- You need end-to-end feature development
- Multiple specialized agents must coordinate
- Workflow has distinct phases with validation
- You want automated quality gates

**Use Agents when:**
- You need focused expertise in one domain
- Task requires persistent identity/context
- You're building a custom workflow

**Use Skills when:**
- You need reference knowledge on demand
- Domain expertise requires bundled resources
- You want progressive disclosure of information

### Installation

Commands are available in your Claude Code environment at:

```
claude-code-resources/commands/
├── orchestration/
├── security/
├── testing/
├── devops/
└── [other categories]/
```

### Related Resources

- **[Agents Index](../agents/README.md)** - 158 specialized agents
- **[Skills Index](../skills/README.md)** - 132 knowledge packages
- **[Integration Guide](../documentation/integration_with_prompts.md)** - How commands work with prompts

---

## Contributing

Commands sourced from:
- [wshobson/agents](https://github.com/wshobson/agents) - MIT License

Generated: 2026-04-20 05:24:25
