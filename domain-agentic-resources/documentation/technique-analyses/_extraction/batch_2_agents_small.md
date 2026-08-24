# Technique Extraction — Batch 2 (Agent Analysis Files — Small)

**Source:** 6 agent analysis files from `technique-analyses/agents/`
**Total Lines Analyzed:** ~1,974
**Date Extracted:** 2026-02-08

---

## Extraction Table

| # | Source File | Technique Name | Code (if assigned) | Family | Maps To Existing | Novel? | Brief Description |
|---|------------|----------------|-------------------|--------|-----------------|--------|-------------------|
| 1 | kubernetes_architect_analysis.md | Principle-Based Guidance | ST-35 | ST | No — NEW | Yes | Define explicit industry principles that govern all agent recommendations |
| 2 | kubernetes_architect_analysis.md | Multi-Provider Expertise | — | DS | Yes — DS-09 | No | Enumerate capabilities across all major cloud providers |
| 3 | kubernetes_architect_analysis.md | Ecosystem Mapping | DS-106 | DS | No — NEW | Yes | Map capabilities to specific tools within complex ecosystems |
| 4 | kubernetes_architect_analysis.md | FinOps Integration | — | DS | Yes — DS-12 | No | Include cost optimization as explicit capability with FinOps methodology |
| 5 | kubernetes_architect_analysis.md | Security-by-Default Behavior | — | AG | Yes — AG-23 | No | Behavioral trait emphasizing security as default posture |
| 6 | kubernetes_architect_analysis.md | Developer Experience Focus | — | IT | Yes — IT-10 | No | Behavioral and capability emphasis on developer usability |
| 7 | kubernetes_architect_analysis.md | Disaster Recovery & Resilience Focus | — | DS | Yes — DS-13 | No | Dedicated section for business continuity and disaster recovery |
| 8 | kubernetes_architect_analysis.md | Technology Evolution Awareness | — | DS | Yes — DS-103 | No | Reference next-generation and emerging technologies |
| 9 | python_pro_analysis.md | Version-Specific Expertise | DS-107 | DS | No — NEW | Yes | Define expertise for specific language/framework versions |
| 10 | python_pro_analysis.md | Modern Tooling Emphasis | DS-108 | DS | No — NEW | Yes | Explicitly highlight current-year tool recommendations |
| 11 | python_pro_analysis.md | Ecosystem Breadth Coverage | — | DS | Yes — DS-09 | No | Cover multiple domains within a language ecosystem |
| 12 | python_pro_analysis.md | Behavioral Standards Emphasis | — | AG | Yes — AG-23 + ST-11 | No | Define behavioral traits around language conventions (PEP 8, type hints) |
| 13 | python_pro_analysis.md | Test Coverage Threshold | — | DS | Yes — DS-02 | No | Specify explicit quality thresholds (>90% coverage) |
| 14 | python_pro_analysis.md | Standard Library Preference | AG-28 | AG | No — NEW | Yes | Behavioral preference for built-in solutions over external dependencies |
| 15 | python_pro_analysis.md | Production-Ready Response Protocol | — | RT | Yes — RT-01 + DS-14 | No | Response approach emphasizing production quality at every step |
| 16 | architect_review_analysis.md | Master-Level Persona Definition | — | ST | Yes — ST-01 + ST-02 | No | Define expert with superlative/elite framing and broad scope |
| 17 | architect_review_analysis.md | Pattern-Centric Knowledge Organization | — | DS | Yes — DS-07 | No | Organize capabilities around design patterns and architecture patterns |
| 18 | architect_review_analysis.md | Quality Attributes Assessment Framework | — | DS | Yes — DS-02 | No | Enumerate non-functional requirements as assessment criteria |
| 19 | architect_review_analysis.md | Architecture Decision Records (ADR) Reference | DS-104 | DS | No — NEW | Yes | Reference industry-standard documentation approaches for decisions (ADRs, C4 model) |
| 20 | architect_review_analysis.md | Impact Assessment Methodology | — | RT | Yes — RT-04 | No | Evaluate changes using impact levels (High/Medium/Low) |
| 21 | architect_review_analysis.md | Anti-Pattern Detection Focus | — | DS | Yes — DS-08 | No | Explicitly include anti-pattern identification in methodology |
| 22 | architect_review_analysis.md | Evolutionary Architecture Emphasis | AG-25 | AG | No — NEW | Yes | Behavioral trait emphasizing enabling change over preventing it |
| 23 | architect_review_analysis.md | Trade-off Acknowledgment | — | RT | Yes — RT-09 | No | Behavioral trait explicitly noting trade-off and business context consideration |
| 24 | architect_review_analysis.md | Referenced Knowledge Base | — | ST | Yes — ST-10 | No | Cite authoritative sources and industry methodologies (Fowler, Evans, Martin) |
| 25 | architect_review_analysis.md | Cloud-Native Technology Stack Coverage | — | DS | Yes — DS-09 | No | Comprehensive coverage of cloud-native technologies across providers |
| 26 | security_auditor_analysis.md | Expert Persona with Domain Depth | — | ST | Yes — ST-01 + ST-02 | No | Define specialist identity with comprehensive domain coverage |
| 27 | security_auditor_analysis.md | Hierarchical Capability Enumeration | — | ST | Yes — ST-04 | No | Structure capabilities in hierarchical domain/subdomain format (9 domains, 50+ capabilities) |
| 28 | security_auditor_analysis.md | Tool Integration Patterns | — | DS | Yes — DS-05 | No | Enumerate specific tools for each capability category (50+ tools) |
| 29 | security_auditor_analysis.md | Proactive Activation Trigger | — | IT | Yes — IT-08 | No | "Use PROACTIVELY for [scenarios]" in agent description |
| 30 | security_auditor_analysis.md | Behavioral Traits as Guardrails | AG-23 | AG | No — NEW | Yes | Define explicit behavioral constraints that apply to all agent actions |
| 31 | security_auditor_analysis.md | Step-by-Step Response Protocol | — | RT | Yes — RT-01 | No | Numbered steps defining how agent should approach any task |
| 32 | security_auditor_analysis.md | Example Interactions as Training Data | — | IT | Yes — RT-07 | No | Provide 7-8 diverse example prompts that trigger the agent |
| 33 | security_auditor_analysis.md | Framework-Based Knowledge Organization | — | DS | Yes — DS-06 | No | Organize knowledge around industry frameworks (OWASP, NIST) |
| 34 | security_auditor_analysis.md | Emerging Technology Section | DS-103 | DS | No — NEW | Yes | Include forward-looking section on emerging technologies |
| 35 | security_auditor_analysis.md | Multi-Category Deployment | AG-24 | AG | No — NEW | Yes | Deploy same agent in multiple category directories for discoverability |
| 36 | tdd_orchestrator_analysis.md | Methodology-Centric Expertise | ST-36 | ST | No — NEW | Yes | Define agent expertise around a specific methodology (TDD, BDD, DDD) |
| 37 | tdd_orchestrator_analysis.md | Cycle Management Pattern | DS-109 | DS | No — NEW | Yes | Structure capabilities around a repeating methodology cycle (red-green-refactor) |
| 38 | tdd_orchestrator_analysis.md | Multi-Agent Coordination | — | AG | Yes — AG-07 | No | Define coordination of multiple specialized agents for testing |
| 39 | tdd_orchestrator_analysis.md | School-Based Approach Documentation | DS-110 | DS | No — NEW | Yes | Document different methodological approaches/schools (Chicago vs London TDD) |
| 40 | tdd_orchestrator_analysis.md | AI-Assisted Enhancement | — | AG | Yes — AG-26 | No | Dedicated section for AI-powered capabilities in methodology |
| 41 | tdd_orchestrator_analysis.md | Cross-Team Governance | AG-29 | AG | No — NEW | Yes | Capabilities for organization-wide methodology compliance and adoption |
| 42 | tdd_orchestrator_analysis.md | Metrics & Quality Assurance | — | DS | Yes — DS-02 + QA-01 | No | Dedicated section for measurement, tracking, and quality gates |
| 43 | tdd_orchestrator_analysis.md | Legacy Code Support | — | DS | Yes — DS-15 | No | Dedicated section for working with existing code and incremental adoption |
| 44 | tdd_orchestrator_analysis.md | Authoritative Source Citation | — | ST | Yes — ST-10 | No | Reference definitive methodology sources (Kent Beck, GOOS) |
| 45 | code_reviewer_analysis.md | AI-Augmented Expertise Definition | AG-26 | AG | No — NEW | Yes | Define expertise that integrates AI tools as core capability |
| 46 | code_reviewer_analysis.md | AI Tool Integration Enumeration | DS-105 | DS | No — NEW | Yes | Enumerate AI-specific tools separate from traditional tools |
| 47 | code_reviewer_analysis.md | Mentor-Style Feedback Emphasis | IT-35 | IT | No — NEW | Yes | Behavioral emphasis on educational, constructive communication |
| 48 | code_reviewer_analysis.md | Production-Reliability Priority | — | AG | Yes — AG-23 | No | Explicit behavioral priority for production safety |
| 49 | code_reviewer_analysis.md | Multi-Layer Review Methodology | RT-13 | RT | No — NEW | Yes | Response methodology with distinct analysis layers (10-step) |
| 50 | code_reviewer_analysis.md | Language-Specific Expertise Sections | — | DS | Yes — DS-10 | No | Enumerate language-specific patterns and best practices (8 languages) |
| 51 | code_reviewer_analysis.md | Severity-Based Feedback Organization | — | OT | Yes — OT-05 + OT-06 | No | Organize feedback by severity and priority levels |
| 52 | code_reviewer_analysis.md | Integration & Automation Patterns | — | DS | Yes — DS-11 | No | Document integration points with development tools (CI/CD, IDE, Slack) |
| 53 | code_reviewer_analysis.md | Team Collaboration Focus | — | IT | Yes — IT-09 | No | Capabilities section dedicated to team dynamics and collaboration |
| 54 | code_reviewer_analysis.md | Continuous Guidance Pattern | AG-27 | AG | No — NEW | Yes | Response approach includes follow-up as explicit step for ongoing engagement |

---

## Summary Statistics

### Totals
- **Total techniques extracted:** 54
- **Marked as novel (Yes):** 19
- **Marked as existing (No):** 35

### By Source File

| Source File | Techniques | Novel | Existing |
|------------|-----------|-------|----------|
| kubernetes_architect_analysis.md | 8 | 2 | 6 |
| python_pro_analysis.md | 7 | 3 | 4 |
| architect_review_analysis.md | 10 | 2 | 8 |
| security_auditor_analysis.md | 10 | 3 | 7 |
| tdd_orchestrator_analysis.md | 9 | 4 | 5 |
| code_reviewer_analysis.md | 10 | 5 | 5 |

### By Family

| Family | Count | Novel | Existing |
|--------|-------|-------|----------|
| AG (Agentic) | 15 | 9 | 6 |
| DS (Domain-Specific) | 22 | 7 | 15 |
| ST (Structural) | 9 | 2 | 7 |
| RT (Reasoning) | 4 | 1 | 3 |
| IT (Interaction) | 3 | 1 | 2 |
| OT (Output) | 1 | 0 | 1 |

### Novel Techniques Identified

| # | Code | Name | Family | Source File |
|---|------|------|--------|------------|
| 1 | ST-35 | Principle-Based Guidance | ST | kubernetes_architect_analysis.md |
| 2 | DS-106 | Ecosystem Mapping | DS | kubernetes_architect_analysis.md |
| 3 | DS-107 | Version-Specific Expertise | DS | python_pro_analysis.md |
| 4 | DS-108 | Tooling Currency | DS | python_pro_analysis.md |
| 5 | AG-28 | Standard Library Preference | AG | python_pro_analysis.md |
| 6 | DS-104 | Decision Documentation Standards | DS | architect_review_analysis.md |
| 7 | AG-25 | Change-Enabling Behavior | AG | architect_review_analysis.md |
| 8 | AG-23 | Behavioral Guardrails | AG | security_auditor_analysis.md |
| 9 | DS-103 | Future-Proofing Expertise | DS | security_auditor_analysis.md |
| 10 | AG-24 | Multi-Category Indexing | AG | security_auditor_analysis.md |
| 11 | ST-36 | Methodology-Centric Expertise | ST | tdd_orchestrator_analysis.md |
| 12 | DS-109 | Cycle Management | DS | tdd_orchestrator_analysis.md |
| 13 | DS-110 | Methodological Schools | DS | tdd_orchestrator_analysis.md |
| 14 | AG-29 | Cross-Team Governance | AG | tdd_orchestrator_analysis.md |
| 15 | AG-26 | AI-Augmented Expertise | AG | code_reviewer_analysis.md |
| 16 | DS-105 | AI Tool Specialization | DS | code_reviewer_analysis.md |
| 17 | IT-35 | Mentor-Style Feedback | IT | code_reviewer_analysis.md |
| 18 | RT-13 | Multi-Layer Analysis | RT | code_reviewer_analysis.md |
| 19 | AG-27 | Continuous Engagement | AG | code_reviewer_analysis.md |

### Cross-File Technique References

Some techniques identified as novel in one file are referenced as existing in another, indicating they were first identified in the same batch:

- **AG-23 (Behavioral Guardrails):** First identified as novel in security_auditor_analysis.md; referenced as existing in kubernetes_architect_analysis.md, python_pro_analysis.md, code_reviewer_analysis.md
- **AG-26 (AI-Augmented Expertise):** First identified as novel in code_reviewer_analysis.md; referenced as existing in tdd_orchestrator_analysis.md
- **DS-103 (Future-Proofing Expertise):** First identified as novel in security_auditor_analysis.md; referenced as existing in kubernetes_architect_analysis.md

### Existing Technique Mappings Referenced

| Code | Name | Times Referenced |
|------|------|-----------------|
| DS-09 | Technology Stack Coverage | 3 |
| ST-01 + ST-02 | Role Assignment + Persona Definition | 3 |
| ST-10 | Source Attribution | 2 |
| AG-23 | Behavioral Guardrails | 3 (as existing mapping) |
| DS-02 | Metric Specification | 3 |
| RT-01 | Chain of Thought | 3 |
| DS-05 | Tool Integration | 2 |
| RT-07 | Few-Shot Examples | 1 |
| DS-06 | Domain Standards | 1 |
| DS-07 | Pattern Libraries | 1 |
| DS-08 | Anti-Pattern Recognition | 1 |
| DS-10 | Language-Specific Patterns | 1 |
| DS-11 | Integration Points | 1 |
| DS-12 | Cost Optimization | 1 |
| DS-13 | Resilience Patterns | 1 |
| DS-14 | Production Quality Focus | 1 |
| DS-15 | Legacy Code Patterns | 1 |
| IT-08 | Activation Criteria | 1 |
| IT-09 | Collaborative Workflows | 1 |
| IT-10 | Developer Experience | 1 |
| OT-05 + OT-06 | Severity Classification + Priority Ranking | 1 |
| QA-01 | Quality Gates | 1 |
| RT-04 | Impact Analysis | 1 |
| RT-09 | Trade-off Analysis | 1 |
| ST-04 | Structured Prompts | 1 |
| ST-11 | Convention Adherence | 1 |
| AG-07 | Multi-Agent Orchestration | 1 |
