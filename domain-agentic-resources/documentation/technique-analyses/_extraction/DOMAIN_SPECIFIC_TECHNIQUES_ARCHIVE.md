# Domain-Specific Techniques Archive

**Created:** 2026-02-09
**Source:** Step 0.3 evaluation of 288 CONFIRMED-NOVEL techniques from `MAPPED_TECHNIQUE_INVENTORY.md`
**Purpose:** Preserve 217 techniques that are too domain-specific for the general MASTER_TECHNIQUE_INDEX but contain valuable prompting patterns for domain-specific prompt development.

**How to use this file:** When building prompts for a specific domain (security, infrastructure, data engineering, mobile, etc.), scan the relevant section below for patterns that can be adapted into your prompt. These aren't general-purpose prompting techniques — they're domain-specific patterns that make prompts in their domain significantly more effective.

---

## Table of Contents

1. [Security & Access Control (16)](#1-security--access-control-16)
2. [Infrastructure & Cloud (25)](#2-infrastructure--cloud-25)
3. [Data Engineering & Observability (9)](#3-data-engineering--observability-9)
4. [API & Development Patterns (11)](#4-api--development-patterns-11)
5. [Tool-Specific Implementation (38)](#5-tool-specific-implementation-38)
6. [Mobile & Platform-Specific (8)](#6-mobile--platform-specific-8)
7. [Testing Patterns (12)](#7-testing-patterns-12)
8. [LLM Evaluation Tooling (7)](#8-llm-evaluation-tooling-7)
9. [Context Management Implementation (5)](#9-context-management-implementation-5)
10. [Documentation Implementation (8)](#10-documentation-implementation-8)
11. [Compliance & Finance (8)](#11-compliance--finance-8)
12. [Agent Architecture (14)](#12-agent-architecture-14)
13. [Networking & Diagnostics (6)](#13-networking--diagnostics-6)
14. [Content Processing (8)](#14-content-processing-8)
15. [Workflow Automation (6)](#15-workflow-automation-6)
16. [Cultural & Organizational (4)](#16-cultural--organizational-4)
17. [Miscellaneous Domain Patterns (32)](#17-miscellaneous-domain-patterns-32)

**Total: 217 techniques**

---

## 1. Security & Access Control (16)

Patterns for security-focused prompts, agents, and skills.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Allowlist-First Strategy | DS-119 | B3/B4 | Default-deny security philosophy: block everything, then selectively allow | Use in any security review prompt: "Start with everything blocked, justify each allow" |
| 2 | Environment-Aware Security Config | DS-120 | B3/B4 | Security settings adapt to dev/staging/prod | Build into deployment prompts: "Vary security strictness by environment tier" |
| 3 | Platform-Specific Security Adaptation | DS-121 | B3/B4 | Security patterns adapt to iOS/Android/Web platforms | Mobile security prompts: "Apply platform-specific security model" |
| 4 | Security Checklist Response Protocol | DS-122 | B3/B4 | Structure security output as a checklist with pass/fail per item | Security audit prompts: "Format findings as checklist with status per control" |
| 5 | Privacy-Security Unified Integration | DS-124 | B3/B4 | Handle privacy and security as unified concern, not separate | Data handling prompts: "Treat privacy and security as one integrated concern" |
| 6 | Context-Aware Security Encoding | DS-125 | B3/B4 | Output encoding adapts to security context (HTML, SQL, URL) | Code generation prompts: "Encode output based on injection context" |
| 7 | Default Deny + Selective Allow | DS-62 | B7b | Network/firewall deny-all + explicit allow rules | K8s/network policy prompts: "Start with deny-all, add minimum necessary allows" |
| 8 | Policy Enforcement Layer Documentation | DS-65 | B7b | Document admission control and policy enforcement layers | K8s security prompts: "Document each policy enforcement point" |
| 9 | Resource-Scoped Permissions | DS-67 | B7b | Fine-grained RBAC patterns scoped to specific resources | RBAC prompts: "Scope permissions to specific resources, not broad categories" |
| 10 | Pattern-Based Credential Detection | DS-82 | B7a | Regex library for detecting credentials in code/config | Security scanning prompts: "Include regex patterns for common credential formats" |
| 11 | Post-Incident Response Checklist | DS-84 | B7a | Structured steps for post-incident cleanup and prevention | Incident response prompts: "Include post-incident remediation checklist" |
| 12 | Layered Security Validation | DS-26 | B8 | Multi-tool security scanning at different layers | Security tooling prompts: "Validate at each security layer with appropriate tool" |
| 13 | Debug Logging Pattern | DS-67 | B8 | Structured logging with subsystem categorization | Logging prompts: "Categorize log output by subsystem and severity" |
| 14 | Content-Based Integrity Validation | QA-3 | B8 | Hash-based change detection for security reviews | Review prompts: "Detect stale approvals via content hash comparison" |
| 15 | Security Checklist Automation | — | B7a | Automate security best practice validation | CI/CD prompts: "Automate security checklist as pre-deployment gate" |
| 16 | QA-18 Privacy-First Documentation | QA-18 | B5 | Security/privacy assessment before sharing any information | Data sharing prompts: "Evaluate privacy implications before output" |

---

## 2. Infrastructure & Cloud (25)

Patterns for infrastructure, cloud, and IaC prompts.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Multi-Cloud Provider Coverage | DS-132 | B3/B4 | Vendor-neutral expertise across AWS/GCP/Azure | Cloud architecture prompts: "Provide multi-cloud alternatives for each service" |
| 2 | IaC Tool Matrix Coverage | DS-134 | B3/B4 | Coverage of Terraform/Pulumi/CloudFormation/CDK | IaC prompts: "Compare IaC tool implementations side by side" |
| 3 | Layer-Based Diagnostic Protocol | DS-137 | B3/B4 | OSI-layer troubleshooting methodology | Network debugging prompts: "Diagnose systematically from L1 to L7" |
| 4 | End-to-End Chain Verification | DS-138 | B3/B4 | Full chain verification (DNS → cert → routing → app) | Infrastructure validation: "Verify each link in the request chain" |
| 5 | Multi-Vantage Testing Strategy | DS-139 | B3/B4 | Test from multiple network vantage points | Network testing prompts: "Test from inside cluster, outside cluster, and external" |
| 6 | Zero-Trust Architecture Pattern | DS-140 | B3/B4 | Never trust, always verify security paradigm | Architecture prompts: "Apply zero-trust to every service boundary" |
| 7 | Service Mesh Integration | DS-141 | B3/B4 | Service mesh as core architecture component | Microservice prompts: "Include service mesh layer for observability and security" |
| 8 | Architecture Documentation Requirements | DS-142 | B3/B4 | Mandatory architecture documentation checklist | Architecture review: "Require documentation for each architectural decision" |
| 9 | DR-First Architecture Pattern | DS-143 | B3/B4 | Disaster recovery as primary design concern | Architecture prompts: "Design for disaster recovery first, features second" |
| 10 | Standard Module Pattern | DS-68 | B7a | Standardized IaC file structure (main/vars/outputs/versions) | Terraform prompts: "Use standard module file structure" |
| 11 | Input Validation Patterns | DS-69 | B7a | Terraform validation blocks for input sanity | Terraform prompts: "Add validation blocks to all input variables" |
| 12 | Module Composition Pattern | DS-70 | B7a | Module output → input composition | IaC prompts: "Wire module outputs to dependent module inputs" |
| 13 | Tag Merging Pattern | DS-71 | B7a | Terraform merge() for default + custom tags | Terraform prompts: "Merge default tags with user-supplied tags" |
| 14 | Conditional Resource Creation | DS-72 | B7a | Terraform count + ternary for optional resources | Terraform prompts: "Use count with ternary for conditional resources" |
| 15 | Terratest Integration Pattern | DS-73 | B7a | IaC integration testing with Terratest | IaC testing prompts: "Generate Terratest cases for module validation" |
| 16 | Repository Structure Templates | DS-55 | B8 | ASCII directory tree templates for project layout | Project scaffolding: "Provide ASCII tree showing file/directory structure" |
| 17 | Troubleshooting Command Sequences | DS-59 | B8 | Problem → Investigation commands → Fix commands | Debug guides: "For each issue, provide investigation then fix commands" |
| 18 | API-First Troubleshooting | — | B9 | Use APIs as primary investigation tool | Cloud troubleshooting: "Use API calls, not console, for investigation" |
| 19 | One-Command Infrastructure Init | — | B7a | Single script creates entire infrastructure | Bootstrap prompts: "Provide one-command setup for entire environment" |
| 20 | Time-Based File Caching | DS-90 | B7a | Timestamp-based cache expiry patterns | Caching prompts: "Implement timestamp-based cache with configurable TTL" |
| 21 | Fallback to Stale Cache | DS-92 | B7a | Stale-while-revalidate caching pattern | Resilience prompts: "Serve stale data while refreshing in background" |
| 22 | Automated Settings Modification | DS-94 | B7a | Safe JSON config modification with backup | Config management: "Backup before modify, validate after" |
| 23 | Quality-of-Service Automatic Classification | — | B9 | Auto-derive QoS from resource configuration | K8s prompts: "Classify QoS tier from resource requests/limits" |
| 24 | Resource Specification Encyclopedia | — | B9 | Field-by-field resource documentation | K8s prompts: "Document every field in the resource specification" |
| 25 | Cloud Provider Annotation Dictionary | — | B9 | Multi-cloud annotation/label management | K8s prompts: "Include cloud-provider-specific annotations" |

---

## 3. Data Engineering & Observability (9)

Patterns for data pipeline, observability, and SRE prompts.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Incremental Strategy Matrix | DS-45 | B7a | Data processing strategy comparison (full/incremental/CDC) | Data pipeline prompts: "Compare processing strategies with tradeoffs" |
| 2 | Idempotent DAG Design | RT-26 | B7a | Design workflow DAGs to be safely re-runnable | Pipeline prompts: "Ensure every DAG step is idempotent" |
| 3 | Dynamic DAG Generation Factory | DS-46 | B7a | Config-driven DAG generation from templates | Airflow/pipeline prompts: "Generate DAGs from configuration, not code" |
| 4 | Column-Level Lineage Documentation | ST-41 | B7a | Document source/transformation/rule per column | Data catalog prompts: "Track lineage at column level, not just table" |
| 5 | Context Propagation Headers | ST-43 | B7a | W3C traceparent header injection for tracing | Observability prompts: "Inject trace context headers at every boundary" |
| 6 | Error Budget Policy Automation | ST-44 | B7a | Automate deployment freezes when error budget exhausted | SRE prompts: "Auto-freeze deployments when error budget hits threshold" |
| 7 | SLO Compliance vs Error Budget | DS-44 | B7a | Separate SLO compliance metric from error budget burn | SRE prompts: "Track SLO compliance and error budget as separate metrics" |
| 8 | Data Flow Trust Boundary Analysis | ST-45 | B7a | Identify trust level at each data flow point | Data security prompts: "Mark trust boundary crossings in data flow" |
| 9 | PostgreSQL MVCC-Aware Design | ST-51 | B7a | Design schemas aware of dead tuple accumulation | PostgreSQL prompts: "Consider MVCC implications in schema design" |

---

## 4. API & Development Patterns (11)

Patterns for API design and software development prompts.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | API-First Documentation Requirement | DS-113 | B3 | Document container/service interfaces as formal API specs | API prompts: "Treat every interface as a formal API contract" |
| 2 | Defensive-First Programming | DS-154 | B3/B4 | Safe coding as default behavioral approach | Code generation: "Default to defensive patterns (null checks, bounds, sanitization)" |
| 3 | HTTP Semantics Enforcement | DS-42 | B5 | Protocol semantics as design constraints (idempotency, safety) | API design prompts: "Enforce HTTP method semantics (GET=safe, PUT=idempotent)" |
| 4 | Multi-Strategy Pagination | DS-101 | B7b | Multiple pagination approaches per API | API design prompts: "Offer cursor, offset, and keyset pagination" |
| 5 | Multi-Instance Authentication | DS-102 | B7b | Instance-aware authentication patterns | SaaS prompts: "Handle multiple instances with separate auth contexts" |
| 6 | Convention-Based Validation Bypass | DS-98 | B7b | Prefix-based validation bypass signals (e.g., `_internal_`) | Tool development: "Use naming conventions to signal validation behavior" |
| 7 | Output Format Adapter Pattern | DS-99 | B7b | Multi-format output adaptation (JSON, YAML, table, etc.) | CLI/API prompts: "Support multiple output formats via adapter pattern" |
| 8 | CLI Tool Pipeline Pattern | DS-100 | B7b | UNIX-style tool composition (stdin/stdout chaining) | CLI prompts: "Design tools for UNIX pipeline composition" |
| 9 | Thread-Safe File Operations | DS-30 | B9 | Atomic read-modify-write with file locking | Concurrent systems: "Use atomic file operations with advisory locks" |
| 10 | Memory Leak Prevention | DS-32 | B9 | Bounded collections + eager resource cleanup | Performance prompts: "Bound collection sizes and cleanup eagerly" |
| 11 | Database Migrations with Schema Versioning | DS-31 | B9 | Schema versioning with automatic migration | Database prompts: "Version schemas and auto-migrate on startup" |

---

## 5. Tool-Specific Implementation (38)

Patterns specific to particular tools, CLIs, or frameworks.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | JSON Processing Pipeline | DS-93 | B7a | Chained jq processing for JSON transformation | Data processing: "Chain jq filters for multi-step JSON transformation" |
| 2 | Model Name Normalization | DS-95 | B7a | Regex-based name reformatting for model names | LLM tooling: "Normalize model names across providers" |
| 3 | Error Suppression in Pipelines | DS-96 | B7a | Redirect errors in multi-command pipelines | Shell scripting: "Suppress non-fatal errors in pipeline stages" |
| 4 | Font Fallback Chain for i18n | DS-104 | B6 | Ordered font lists for cross-platform rendering | i18n prompts: "Define font fallback chain for each script/language" |
| 5 | Environment Setup Prerequisites | DS-106 | B6 | Platform-specific environment variables before execution | Setup guides: "Document required env vars by platform" |
| 6 | Semantic Typography Hierarchy | DS-107 | B6 | Font families per semantic element (heading, body, code) | Design prompts: "Assign typography per semantic element" |
| 7 | Context-Aware Timing Algorithm | DS-38 | B6 | Smart delay based on command semantics | CLI tools: "Add intelligent delays based on operation type" |
| 8 | Cross-Platform Path Handling | DS-99 | B6 | Windows/WSL path interoperability | Cross-platform tools: "Handle path translation between Windows and UNIX" |
| 9 | Workflow Abstraction Layers | DS-100 | B6 | Simple vs complex workflow execution chains | Tool design: "Provide simple and advanced workflow modes" |
| 10 | Bash Loop Templates | DS-101 | B6 | Copy-paste bash processing loop patterns | Shell guides: "Provide ready-to-use loop templates" |
| 11 | Error Handling Pattern Library | DS-102 | B6 | Reusable error handling patterns by category | Error handling guides: "Catalog error handling patterns by error type" |
| 12 | Metadata Preservation Pattern | DS-103 | B6 | Preserve original metadata in converted output | Conversion tools: "Preserve source metadata through transformations" |
| 13 | Template Substitution Composition | OT-17 | B6 | Variable substitution from prior pipeline stages | Template engines: "Compose variables from prior stage outputs" |
| 14 | Image Analysis Prompt Template | DS-116 | B6 | Extract design patterns from images | Vision prompts: "Template for extracting design specs from screenshots" |
| 15 | Interactive PRD Refinement | IT-41 | B6 | Generate then iteratively refine PRDs | Product prompts: "Generate PRD draft, then refine through Q&A" |
| 16 | Timestamped Output Versioning | DS-117 | B6 | Timestamp for automatic version tracking | Output management: "Append timestamps for version tracking" |
| 17 | Visual Validation Feedback | IT-26 | B7a | Colored emoji output for validation results | CLI tools: "Use color/emoji for pass/fail visual feedback" |
| 18 | Force Override with Explicit Warning | IT-31 | B7a | Dangerous operations require loud confirmation | Safety pattern: "Require explicit override with visible warning for dangerous ops" |
| 19 | Conditional Coloring Based on State | OT-12 | B7a | ANSI colors for data state indication | CLI reporting: "Color-code output based on status" |
| 20 | Multi-Mode CLI Design | IT-30 | B5 | Verb-based subcommands in single tool | CLI design: "Use verb-based subcommands (tool add, tool remove)" |
| 21 | Popular Options Directory | IT-45 | B5 | Curated popular options table | Tool docs: "Highlight most popular options in dedicated section" |
| 22 | Restart Requirement Warning | IT-46 | B5 | Post-installation action warnings | Install guides: "Warn about required restarts after installation" |
| 23 | Inline Command Comments | OT-19 | B5 | Self-documenting command examples with inline comments | Documentation: "Add inline comments to command examples" |
| 24 | Self-Contained Script Package | IT-24 | B5 | All dependencies in single directory | Packaging: "Bundle all dependencies in self-contained directory" |
| 25 | Reference File Pointers | IT-20 | B5 | Lightweight linking with summaries | Documentation: "Reference related files with brief summaries" |
| 26 | File-Based Variable Loading | IT-38 | B6 | Load test/config variables from external files | Testing tools: "Load test variables from JSON/YAML files" |
| 27 | Assertion Type Reference Table | IT-39 | B6 | Comprehensive assertion method documentation | Testing docs: "Document all available assertion types with examples" |
| 28 | Best Practices by Category | IT-36 | B6 | Practices organized by concern area | Documentation: "Group best practices by concern (security, performance, etc.)" |
| 29 | Conditional Reference Loading | IT-33 | B7b | Operation-triggered document loading | Agentic: "Load reference docs conditionally based on operation type" |
| 30 | Selective Field Loading | IT-34 | B7b | Selective API field retrieval | API optimization: "Request only needed fields from APIs" |
| 31 | Bundled Executable Scripts | IT-14 | B6 | Co-package scripts with documentation | Skill design: "Bundle executable scripts alongside docs" |
| 32 | Bundled Script Ecosystem | IT-18 | B6 | Multiple complementary scripts as ecosystem | Skill design: "Provide complementary scripts that work together" |
| 33 | Common Patterns Section | IT-35 | B6 | Curated named reusable patterns section | Documentation: "Include dedicated patterns section with named patterns" |
| 34 | One-Time Manual Fix Documentation | IT-33 | B8 | Document one-time workaround instructions | Troubleshooting: "Document manual fixes with one-time cleanup steps" |
| 35 | Bundled Scripts as Reference | IT-30 | B9 | Scripts positioned as flexible starting points | Skill design: "Position scripts as references to adapt, not copy" |
| 36 | Platform-Specific Issue Matrix | — | B9 | Platform-to-requirements mapping | Cross-platform: "Map platform-specific issues and requirements" |
| 37 | Learning Methodology for APIs | — | B9 | Systematic API exploration method | API onboarding: "Provide systematic method to learn an API" |
| 38 | Level-Specific Diagram Syntax | OT-13 | B3 | Diagram syntax per documentation level (C4 levels) | Architecture docs: "Match diagram detail level to documentation level" |

---

## 6. Mobile & Platform-Specific (8)

Patterns for mobile development and platform-specific prompts.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | SwiftUI/UIKit Hybrid Architecture | ST-48 | B4 | Mixed UI framework integration patterns | iOS prompts: "Support both SwiftUI and UIKit in same codebase" |
| 2 | Xcode Cloud Integration | ST-27 | B4 | Apple platform-native CI/CD | iOS CI/CD: "Use Xcode Cloud for Apple ecosystem builds" |
| 3 | Multi-Platform Architecture Declaration | — | B4 | Explicit platform coverage enumeration | Mobile prompts: "Enumerate all target platforms explicitly" |
| 4 | Apple Ecosystem Integration | — | B4 | Cross-device Apple ecosystem thinking | Apple prompts: "Design for iPhone + iPad + Watch + Mac continuity" |
| 5 | Accessibility-First Development | — | B4 | Accessibility as first-class development concern | Mobile prompts: "Build accessibility in from the start, not as afterthought" |
| 6 | Impeller Rendering Engine Focus | — | B4 | Flutter-specific rendering engine patterns | Flutter prompts: "Optimize for Impeller rendering engine" |
| 7 | Multi-Language Entity Mapping | IT-28 | B7b | Cross-language entity resolution | NLP/i18n: "Map entities across languages with cultural adaptation" |
| 8 | Production Application as Skill | — | B9 | Full production app packaged as skill architecture | Agentic: "Package complete app within skill directory structure" |

---

## 7. Testing Patterns (12)

Patterns for testing-specific prompts and workflows.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Self-Healing Test Pattern | DS-149 | B3/B4 | Tests that auto-adapt to non-breaking changes | Test automation: "Build tests that adapt to UI/structure changes" |
| 2 | Test Pyramid Strategy | DS-150 | B3/B4 | Strategic distribution across unit/integration/E2E | Testing strategy: "Define test distribution ratios per pyramid level" |
| 3 | TDD Metrics Framework | DS-151 | B3/B4 | Quantitative TDD effectiveness metrics | TDD evaluation: "Track TDD metrics: coverage, test-first %, cycle time" |
| 4 | Docs-as-Code Pipeline | DS-152 | B3/B4 | Documentation in CI/CD pipeline | DevOps: "Treat documentation as code with CI/CD validation" |
| 5 | SDK Generation from Specs | DS-144 | B3/B4 | Multi-language SDK generation from OpenAPI specs | API tooling: "Generate typed SDKs from OpenAPI specifications" |
| 6 | Long-Form Documentation Process | DS-147 | B3/B4 | Multi-phase comprehensive documentation workflow | — (Note: also ADD'd to master as DS-38) |
| 7 | Progressive Evaluation Modes | DS-109 | B6 | Three-tier LLM evaluation (quick/standard/deep) | LLM eval: "Offer multiple evaluation depth modes" |
| 8 | Python Custom Assertion Pattern | DS-110 | B6 | Structured assertion return format for LLM evaluation | Promptfoo: "Return structured {pass, score, reason} from assertions" |
| 9 | Few-Shot with File-Based Examples | DS-112 | B6 | Load chat-format examples from external files | LLM eval: "Load few-shot examples from files, not inline" |
| 10 | Dual Configuration Pattern | DS-113 | B6 | Production + preview configuration side by side | Tool config: "Maintain production and preview configs in parallel" |
| 11 | Echo Provider for Cost-Free Preview | AG-23 | B6 | Dry-run preview without API calls | LLM tooling: "Offer echo/dry-run mode for testing without API cost" |
| 12 | Prompt Versioning as Code | DS-20 | B6 | Prompts with version control + CI/CD integration | Prompt management: "Version prompts in git with CI/CD validation" |

---

## 8. LLM Evaluation Tooling (7)

Patterns specific to LLM evaluation frameworks (Promptfoo, etc.).

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Reduction Ratio Metric | DS-114 | B6 | Input/output ratio as quality metric for summarization | Eval metrics: "Track compression ratio as quality signal" |
| 2 | Few-Shot with Semantic Selection | — | B6 | Select few-shot examples by semantic similarity | RAG/eval: "Select examples most similar to the input" |
| 3 | Template Variable Interpolation | — | B6 | Reusable prompt templates with variable substitution | Prompt management: "Use {{variable}} templates for prompt reuse" |
| 4 | Structured Asset Library | DS-118 | B6 | Bundled prompt templates as reusable assets | Prompt management: "Organize prompt templates as named assets" |
| 5 | Multi-Stage Workflow with Intermediate Outputs | DS-115 | B6 | Sequential stages producing reusable artifacts | Pipeline design: "Each stage produces persisted intermediate output" |
| 6 | Day 1 Onboarding Guide | — | B7a | Hour-by-hour onboarding with checkpoints | Onboarding: "Structure onboarding by hour with verification checkpoints" |
| 7 | High Freedom Workflow Disclosure | IT-44 | B6 | Explicitly state adaptability and customization freedom | Skill design: "Explicitly tell users what they can customize" |

---

## 9. Context Management Implementation (5)

Implementation-specific patterns for context management in AI systems.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Three-Way Context Merging | — | B1 | Version-control-style merge strategies for context | Context systems: "Merge context from multiple sources like git merge" |
| 2 | Cross-Project Knowledge Transfer | — | B1 | Semantic vector transfer between project contexts | Multi-project: "Transfer relevant knowledge between projects" |
| 3 | Multi-Modal Context Representation | — | B1 | Multi-format context serialization (JSON, YAML, natural language) | Context design: "Serialize context in format appropriate to consumer" |
| 4 | Knowledge Graph Construction | — | B1 | Ontological context representation as knowledge graph | Advanced context: "Build knowledge graph from unstructured context" |
| 5 | Token Economics Analysis | DS-35 | B5 | Token cost calculation for context optimization | Cost optimization: "Calculate token cost per context component" |

---

## 10. Documentation Implementation (8)

Patterns for specific documentation generation approaches.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Architecture Decision Records Reference | DS-104 | B2 | Use ADR format for architectural decisions | Architecture: "Document decisions in ADR format (Context/Decision/Consequences)" |
| 2 | Programmatic Persona Identification | DS-114 | B3 | Identify external systems as personas in architecture | Architecture docs: "Model external systems as personas with needs" |
| 3 | Journey Maps as Architecture | DS-115 | B3 | User journeys as architectural documentation | Architecture docs: "Map user journeys to architectural components" |
| 4 | Multi-Criteria Boundary Identification | DS-116 | B3 | Identify component boundaries by domain/tech/org criteria | Architecture: "Identify boundaries using multiple criteria" |
| 5 | Logical-to-Physical Mapping | DS-117 | B3 | Map logical architecture to physical deployment | Architecture: "Map each logical component to its physical deployment" |
| 6 | Tool Ecosystem Integration | DS-126 | B3 | Named tool ecosystem integration patterns | Tool guides: "Document how tools integrate into existing ecosystem" |
| 7 | AI-as-Core-Capability Pattern | DS-127 | B3 | AI/ML as core capability, not add-on | Agent design: "Position AI as core capability, not plugin" |
| 8 | Industry-Vertical Specialization | DS-128 | B3 | Industry-specific implementation patterns | Vertical prompts: "Customize recommendations for specific industry" |

---

## 11. Compliance & Finance (8)

Patterns for compliance, financial, and blockchain prompts.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Control Type Diversity Requirement | ST-47 | B7a | Mix of preventive/detective/corrective controls | Compliance: "Ensure balanced mix of control types" |
| 2 | Mainnet Forking for Testing | ST-50 | B7a | Fork blockchain mainnet for realistic testing | Blockchain: "Test against forked mainnet for production fidelity" |
| 3 | PostgreSQL Constraint Hierarchy | RT-30 | B7a | PK > FK > UNIQUE > CHECK ordering rationale | Database design: "Apply constraints in hierarchy order" |
| 4 | Backtesting Bias Catalog | DS-64 | B7a | Catalog of biases in backtesting (survivorship, lookahead, etc.) | Finance prompts: "Check for each backtesting bias type" |
| 5 | Walk-Forward Analysis Pattern | ST-53 | B7a | Rolling window time-series validation | Finance/ML: "Use walk-forward windows for time-series validation" |
| 6 | Legal-Technical Implementation Bridge | NE-17 | B3 | Legal documents with technical implementation steps | Legal-tech: "Bridge legal requirements to technical implementation" |
| 7 | Blameless Culture Requirement | NE-20 | B3/B4 | Cultural value (blameless postmortems) as explicit requirement | Incident response: "Frame all analysis as blameless" |
| 8 | Compliance-Aware Architecture | DS-131 | B4 | Architecture designed for compliance from start | Compliance: "Build compliance into architecture, don't bolt on" |

---

## 12. Agent Architecture (14)

Patterns specific to agentic system design and agent behavior.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Hierarchical Documentation Pipeline | AG-30 | B3 | Sequential multi-agent documentation generation | Multi-agent: "Pipeline agents for outline → draft → review → publish" |
| 2 | Incident Command Structure | AG-34 | B3/B4 | Formal incident role assignment (IC, scribe, comms) | Incident agents: "Assign formal ICS roles to agents" |
| 3 | Evolutionary Architecture Emphasis | AG-25 | B2 | Design agents for evolvability over perfection | Agent design: "Build agents that can evolve without rewriting" |
| 4 | Multi-Category Deployment | AG-24 | B2 | Agent discoverability via multi-directory presence | Agent deployment: "Make agents discoverable across multiple categories" |
| 5 | Standard Library Preference | AG-28 | B2 | Behavioral preference for built-in tools over external | Code agents: "Prefer standard library before reaching for dependencies" |
| 6 | Cross-Team Governance | AG-29 | B2 | Organization-wide methodology compliance agent | Governance: "Enforce org-wide standards across teams" |
| 7 | CLI-First Executable Documentation | DS-25 | B8 | Scripts serve as both documentation and executable tools | Skill design: "Make documentation executable via scripts" |
| 8 | AI Tool Integration Enumeration | DS-105 | B2 | Enumerate AI-specific tools as agent capabilities | Agent capabilities: "List AI tools as explicit capabilities" |
| 9 | Proactive Activation Trigger | — | B2 | Agent discovery/invocation trigger phrases | Agent design: "Define trigger phrases that activate the agent" |
| 10 | Legacy Code Support | — | B2 | Incremental adoption for existing codebases | Migration agents: "Support gradual adoption alongside legacy code" |
| 11 | Team Collaboration Focus | — | B2 | Team dynamics as agent capability area | Team agents: "Include team collaboration guidance" |
| 12 | Continuous Guidance Pattern | — | B2 | Follow-up as explicit engagement step | Agent flow: "Always offer follow-up guidance after completion" |
| 13 | Machine Learning Pattern Detection | — | B9 | Apply ML on correction data to detect recurring issues | Meta-agents: "Analyze correction patterns to prevent repeat errors" |
| 14 | Modern Tooling Emphasis | DS-108 | B2 | Time-sensitive tool recommendations (prefer modern) | Agent expertise: "Recommend modern tools, flag deprecated ones" |

---

## 13. Networking & Diagnostics (6)

Patterns for network troubleshooting and diagnostic prompts.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Disaster Recovery & Resilience Focus | — | B2 | Dedicated DR/BC capability and planning | DR prompts: "Include disaster recovery plan for each component" |
| 2 | Pattern-Centric Knowledge Organization | — | B2 | Organize knowledge around named patterns | Knowledge bases: "Organize content by pattern name, not topic" |
| 3 | Cycle Management Pattern | DS-109 | B2 | Manage repeating methodology cycles (sprint, PDCA) | Process prompts: "Define and manage methodology cycle boundaries" |
| 4 | Sequential Evidence Gathering | — | B9 | Prioritized investigation sequences | Troubleshooting: "Gather evidence in order of diagnostic value" |
| 5 | Evidence-Based Investigation Methodology | — | B9 | Systematic hypothesis → evidence → conclusion | Investigation: "Follow scientific method for troubleshooting" |
| 6 | Multi-Format Auto-Detection | DS-85 | B8 | Content signature-based format routing | File processing: "Auto-detect format from content signatures" |

---

## 14. Content Processing (8)

Patterns for content transformation and processing prompts.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Format-Specific Extraction Patterns | DS-86 | B8 | Polymorphic processing per file format | File processing: "Apply format-specific extraction strategy" |
| 2 | Context-Aware Naming Algorithm | DS-43 | B5 | Intelligent filename generation from content | File management: "Generate filenames from content semantics" |
| 3 | Lookback Window for Context | DS-46 | B5 | N-line context analysis window | Text processing: "Analyze N surrounding lines for context" |
| 4 | Size-Based Decision Guidelines | DS-37 | B5 | Size thresholds trigger different processing actions | Content management: "Apply different strategies based on size thresholds" |
| 5 | Content Classification Matrix | DS-36 | B5 | Multi-dimensional content evaluation | Content triage: "Evaluate content on multiple quality dimensions" |
| 6 | Structured Asset Library | DS-118 | B6 | Organized collection of reusable prompt assets | Asset management: "Organize reusable assets with metadata" |
| 7 | Progressive Abstraction Transformation | DS-112 | B3 | Multi-level documentation abstraction | — (Note: also ADD'd to master as DS-37) |
| 8 | Bundled Scripts as Reference Implementations | — | B9 | Scripts as flexible references, not rigid requirements | Skill design: "Position scripts as starting points to customize" |

---

## 15. Workflow Automation (6)

Patterns for automated workflow and pipeline prompts.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Dynamic DAG Generation Factory | DS-46 | B7a | Config-driven DAG generation | Automation: "Generate workflows from configuration templates" |
| 2 | Context-Aware Timing Algorithm | DS-38 | B6 | Smart delay based on command semantics | Automation: "Adjust timing based on operation characteristics" |
| 3 | Error Suppression in Pipelines | DS-96 | B7a | Handle non-fatal errors without stopping pipeline | Pipelines: "Continue pipeline on non-fatal errors, collect for summary" |
| 4 | Multi-Stage Workflow with Intermediate Outputs | DS-115 | B6 | Each stage produces reusable intermediate artifact | Pipelines: "Persist intermediate outputs for debugging and reuse" |
| 5 | Fallback Strategy Pattern | — | B7b | Progressive fallback with increasing generality | — (Note: also MERGE'd into QA-13) |
| 6 | Quality Verification Checklist Commands | QA-25 | B6 | Provide executable commands for verification | Verification: "Include copy-paste verification commands" |

---

## 16. Cultural & Organizational (4)

Patterns related to team culture and organizational approaches.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Blameless Culture Requirement | NE-20 | B3/B4 | Blameless postmortem as explicit cultural value | Postmortems: "Frame all analysis without blame attribution" |
| 2 | Team Collaboration Focus | — | B2 | Team dynamics as capability area | Team prompts: "Include collaboration and team dynamics guidance" |
| 3 | Continuous Guidance Pattern | — | B2 | Always offer follow-up next steps | Agent design: "End every interaction with offered next steps" |
| 4 | Incident Communication Matrix | — | B4 | Stakeholder communication during incidents | Incident comms: "Define what to communicate to each stakeholder tier" |

---

## 17. Miscellaneous Domain Patterns (32)

Remaining domain-specific patterns that don't fit neatly into the categories above.

| # | Technique | Original Code | Source | Description | Prompt Fodder |
|---|-----------|--------------|--------|-------------|---------------|
| 1 | Allowlist-First Strategy | DS-119 | B3/B4 | Default deny, selective allow | Security prompts |
| 2 | Environment-Aware Security Config | DS-120 | B3/B4 | Config varies by environment | Environment-aware prompts |
| 3 | Platform-Specific Security Adaptation | DS-121 | B3/B4 | Security per platform | Platform security |
| 4 | Privacy-Security Unified Integration | DS-124 | B3/B4 | Unified privacy + security | Data handling |
| 5 | Context-Aware Security Encoding | DS-125 | B3/B4 | Encoding per security context | Secure coding |
| 6 | Multi-Cloud Provider Coverage | DS-132 | B3/B4 | Multi-cloud expertise | Cloud architecture |
| 7 | IaC Tool Matrix Coverage | DS-134 | B3/B4 | Multi-IaC-tool coverage | Infrastructure |
| 8 | Zero-Trust Architecture Pattern | DS-140 | B3/B4 | Zero-trust paradigm | Security architecture |
| 9 | Service Mesh Integration | DS-141 | B3/B4 | Service mesh as architecture | Microservices |
| 10 | DR-First Architecture Pattern | DS-143 | B3/B4 | DR as primary concern | Architecture |
| 11 | Non-Judgmental Comparison | DS-74 | B6 | "Normal vs Better" framing | — (Note: ADD'd to master as NE-16) |
| 12 | Code Archaeology Techniques | — | B1 | git bisect/blame/log for debugging | Git prompts: "Use git archaeology to understand code history" |
| 13 | Numbered Workflow Steps | DS-119 | B5 | Explicitly numbered workflow steps | — (captured by ST-02) |
| 14 | Regulatory Enumeration Pattern | DS-130 | B3 | Comprehensive regulation listing | — (Note: ADD'd to master as DS-32) |
| 15 | Jurisdiction-Adaptive Output | DS-131 | B3 | Output varies by jurisdiction | — (Note: ADD'd to master as DS-33) |
| 16 | Professional Defaults Library | DS-40 | B6 | Pre-configured defaults by use case | — (Note: ADD'd to master as DS-27) |
| 17 | Multi-Platform Architecture Declaration | — | B4 | Explicit platform enumeration | Multi-platform |
| 18 | Apple Ecosystem Integration | — | B4 | Cross-device Apple ecosystem | Apple development |
| 19 | Accessibility-First Development | — | B4 | Accessibility as first-class concern | Accessibility |
| 20 | Impeller Rendering Engine Focus | — | B4 | Flutter Impeller optimization | Flutter |
| 21 | Disaster Recovery & Resilience Focus | — | B2 | DR/BC capability | DR planning |
| 22 | Legacy Code Support | — | B2 | Incremental adoption | Migration |
| 23 | Machine Learning Pattern Detection | — | B9 | ML on correction data | Meta-improvement |
| 24 | Production Application as Skill | — | B9 | Full app as skill | Agentic architecture |
| 25 | API-First Troubleshooting | — | B9 | APIs as investigation tool | Cloud troubleshooting |
| 26 | Pre-Implementation Checklist | — | B5 | 137-point pre-build verification | — (Note: MERGE'd into QA-08) |
| 27 | Modern Tooling Emphasis | DS-108 | B2 | Prefer modern tools | Tool recommendations |
| 28 | Proactive Activation Trigger | — | B2 | Agent trigger phrases | Agent design |
| 29 | Cross-Team Governance | AG-29 | B2 | Org-wide methodology compliance | Governance |
| 30 | Standard Library Preference | AG-28 | B2 | Prefer built-in tools | Code generation |
| 31 | Multi-Category Deployment | AG-24 | B2 | Multi-directory discoverability | Agent deployment |
| 32 | Evolutionary Architecture Emphasis | AG-25 | B2 | Design for evolvability | Architecture |

> **Note:** Some techniques appear in both a domain-specific section (1-16) and in this miscellaneous section when they cross categories. The primary listing is in the domain-specific section; entries here marked with "(Note: ADD'd/MERGE'd...)" are cross-references to techniques that were promoted to the master index in the shortlist.

---

## Usage Guide

### When Building Domain-Specific Prompts

1. **Identify your domain** from the sections above
2. **Scan the "Prompt Fodder" column** for patterns relevant to your prompt
3. **Adapt the pattern** to your specific use case — these are starting points, not rigid templates
4. **Combine domain patterns with general techniques** from `MASTER_TECHNIQUE_INDEX.md`

### Example: Building a Kubernetes Security Prompt

Relevant archive entries:
- Section 1: Allowlist-First Strategy, Default Deny + Selective Allow, Resource-Scoped Permissions, Policy Enforcement Layer
- Section 2: Zero-Trust Architecture, One-Command Infrastructure Init
- Section 11: Control Type Diversity Requirement

Combine with master index techniques:
- ST-02 (Structured Sequential Instructions)
- QA-08 (Gate-Based Verification)
- DS-06 (Prioritization and Severity)
- AG-04 (Behavioral Guardrails)

### Example: Building a Financial Analysis Prompt

Relevant archive entries:
- Section 11: Backtesting Bias Catalog, Walk-Forward Analysis Pattern
- Section 3: SLO Compliance vs Error Budget (adapted for financial metrics)

Combine with master index techniques:
- RT-02 (Multi-Dimensional Analysis)
- QA-12 (False Positives Identification)
- NE-11 (Embedded Calculation Formulas)
- DS-02 (Metric Specification)

---

**Total archived: 217 domain-specific techniques across 17 categories**
**Source: Step 0.3 evaluation of MAPPED_TECHNIQUE_INVENTORY.md**
