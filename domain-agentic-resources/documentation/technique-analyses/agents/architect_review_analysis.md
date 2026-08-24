# Technique Analysis: architect-review

**Resource Type:** Agent (Opus 4.5)
**Path:** `claude-code-resources/agents/architecture/architect-review.md`
**Date Analyzed:** 2025-12-23
**Category:** Architecture, Backend (appears in 2 categories)
**Lines:** 147

---

## Summary

The architect-review agent is a **master software architect** persona demonstrating comprehensive architecture expertise. It showcases **pattern-centric knowledge organization** (organizing knowledge around design patterns, architecture patterns, and development practices) and uses an **impact assessment methodology** for evaluating changes. This agent exemplifies how to structure architectural review expertise for complex distributed systems.

---

## Identified Techniques

### Technique 1: Master-Level Persona Definition

- **Category:** ST (Structural Techniques)
- **Pattern:** Define expert with superlative framing and scope
- **Example from resource:**
  ```
  You are a master software architect specializing in modern software architecture
  patterns, clean architecture principles, and distributed systems design.

  ## Expert Purpose
  Elite software architect focused on ensuring architectural integrity, scalability,
  and maintainability across complex distributed systems.
  ```
- **Maps to existing:** ST-01 (Role Assignment) + ST-02 (Persona Definition) - with **master/elite framing**
- **Effectiveness:** Establishes authority for critical architectural decisions requiring Opus-level capabilities

### Technique 2: Pattern-Centric Knowledge Organization

- **Category:** DS (Domain-Specific)
- **Pattern:** Organize capabilities around design patterns and architectural patterns
- **Example from resource:**
  ```
  ### Modern Architecture Patterns
  - Clean Architecture and Hexagonal Architecture implementation
  - Microservices architecture with proper service boundaries
  - Event-driven architecture (EDA) with event sourcing and CQRS
  - Domain-Driven Design (DDD) with bounded contexts and ubiquitous language

  ### SOLID Principles & Design Patterns
  - Single Responsibility, Open/Closed, Liskov Substitution principles
  - Repository, Unit of Work, and Specification patterns
  - Factory, Strategy, Observer, and Command patterns
  ```
- **Maps to existing:** DS-07 (Pattern Libraries) - at **comprehensive architecture level**
- **Effectiveness:** Enables Claude to recommend specific patterns for specific problems

### Technique 3: Quality Attributes Assessment Framework

- **Category:** DS (Domain-Specific)
- **Pattern:** Enumerate non-functional requirements as assessment criteria
- **Example from resource:**
  ```
  ### Quality Attributes Assessment
  - Reliability, availability, and fault tolerance evaluation
  - Scalability and performance characteristics analysis
  - Security posture and compliance requirements
  - Maintainability and technical debt assessment
  - Testability and deployment pipeline evaluation
  - Monitoring, logging, and observability capabilities
  - Cost optimization and resource efficiency analysis
  ```
- **Maps to existing:** DS-02 (Metric Specification) - applied to **architecture evaluation**
- **Effectiveness:** Provides systematic framework for architecture reviews

### Technique 4: Architecture Decision Records (ADR) Reference

- **Category:** DS (Domain-Specific)
- **Pattern:** Reference documentation standards for architecture decisions
- **Example from resource:**
  ```
  ### Architecture Documentation
  - C4 model for software architecture visualization
  - Architecture Decision Records (ADRs) and documentation
  - System context diagrams and container diagrams
  - Component and deployment view documentation
  ```
- **Maps to existing:** NEW - DS-104 (Decision Documentation Standards)
- **Effectiveness:** Ensures architecture decisions are properly documented and traceable

### Technique 5: Impact Assessment Methodology

- **Category:** RT (Reasoning Techniques)
- **Pattern:** Evaluate changes using impact levels (High/Medium/Low)
- **Example from resource:**
  ```
  ## Response Approach
  1. **Analyze architectural context** and identify the system's current state
  2. **Assess architectural impact** of proposed changes (High/Medium/Low)
  3. **Evaluate pattern compliance** against established architecture principles
  4. **Identify architectural violations** and anti-patterns
  5. **Recommend improvements** with specific refactoring suggestions
  ```
- **Maps to existing:** RT-04 (Impact Analysis) - with **explicit severity levels**
- **Effectiveness:** Enables prioritized architectural recommendations

### Technique 6: Anti-Pattern Detection Focus

- **Category:** DS (Domain-Specific)
- **Pattern:** Explicitly include anti-pattern identification in methodology
- **Example from resource:**
  ```
  4. **Identify architectural violations** and anti-patterns
  ```
  Plus Knowledge Base reference:
  ```
  - Modern software architecture patterns and anti-patterns
  ```
- **Maps to existing:** DS-08 (Anti-Pattern Recognition)
- **Effectiveness:** Proactively identifies problematic patterns, not just suggests good ones

### Technique 7: Evolutionary Architecture Emphasis

- **Category:** AG (Agentic)
- **Pattern:** Behavioral trait emphasizing change enablement
- **Example from resource:**
  ```
  ## Behavioral Traits
  - Champions clean, maintainable, and testable architecture
  - Emphasizes evolutionary architecture and continuous improvement
  - Focuses on enabling change rather than preventing it
  - Considers long-term maintainability over short-term convenience
  ```
- **Maps to existing:** NEW - AG-25 (Change-Enabling Behavior)
- **Effectiveness:** Ensures architecture guidance enables rather than constrains evolution

### Technique 8: Trade-off Acknowledgment

- **Category:** RT (Reasoning Techniques)
- **Pattern:** Behavioral trait explicitly noting trade-off consideration
- **Example from resource:**
  ```
  - Balances technical excellence with business value delivery
  - Advocates for proper abstraction levels without over-engineering
  ```
- **Maps to existing:** RT-09 (Trade-off Analysis)
- **Effectiveness:** Ensures recommendations consider business context

### Technique 9: Referenced Knowledge Base

- **Category:** ST (Structural Techniques)
- **Pattern:** Cite authoritative sources and methodologies
- **Example from resource:**
  ```
  ## Knowledge Base
  - Microservices patterns from Martin Fowler and Sam Newman
  - Domain-Driven Design from Eric Evans and Vaughn Vernon
  - Clean Architecture from Robert C. Martin (Uncle Bob)
  - Building Microservices and System Design principles
  ```
- **Maps to existing:** ST-10 (Source Attribution)
- **Effectiveness:** Grounds agent in recognized industry expertise

### Technique 10: Cloud-Native Technology Stack Coverage

- **Category:** DS (Domain-Specific)
- **Pattern:** Comprehensive coverage of cloud-native technologies
- **Example from resource:**
  ```
  ### Cloud-Native Architecture
  - Container orchestration with Kubernetes and Docker Swarm
  - Cloud provider patterns for AWS, Azure, and Google Cloud Platform
  - Infrastructure as Code with Terraform, Pulumi, and CloudFormation
  - GitOps and CI/CD pipeline architecture
  - Auto-scaling patterns and resource optimization
  - Multi-cloud and hybrid cloud architecture strategies
  ```
- **Maps to existing:** DS-09 (Technology Stack Coverage)
- **Effectiveness:** Enables recommendations across all major cloud platforms

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: DS-104 - Decision Documentation Standards

- **Description:** Reference industry-standard documentation approaches for decisions
- **Implementation:**
  ```markdown
  ### Architecture Documentation
  - [Documentation standard 1]: [purpose, format]
  - [Documentation standard 2]: [purpose, format]
  - [Decision record format]: ADRs, RFCs, design docs
  ```
- **Use case:** Any agent making decisions that need documentation
- **Example:**
  ```markdown
  ### Architecture Documentation
  - C4 model for software architecture visualization
  - Architecture Decision Records (ADRs) and documentation
  - API documentation with OpenAPI/Swagger specifications
  ```
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-104
- **Integration:** Recommend for all decision-making agents

### Pattern 2: AG-25 - Change-Enabling Behavior

- **Description:** Behavioral trait emphasizing enabling change over preventing it
- **Implementation:**
  ```markdown
  ## Behavioral Traits
  - Focuses on enabling change rather than preventing it
  - Emphasizes evolutionary [domain] and continuous improvement
  - Considers long-term maintainability over short-term convenience
  ```
- **Use case:** Agents providing guidance that could become overly restrictive
- **Example:**
  ```markdown
  ## Behavioral Traits
  - Focuses on enabling change rather than preventing it
  - Emphasizes evolutionary architecture and continuous improvement
  - Promotes team alignment through clear architectural principles
  ```
- **Proposed category:** AG (Agentic)
- **Proposed code:** AG-25
- **Integration:** Critical for architecture and design agents

---

## Multi-Technique Combinations

### Combination 1: Pattern-Centric Knowledge + Anti-Pattern Detection + Impact Assessment

- **Technique Stack:** DS-07 + DS-08 + RT-04
- **Combination Purpose:** Comprehensive architecture review
- **Flow:**
  1. Assess current architecture against known patterns (DS-07)
  2. Identify anti-patterns and violations (DS-08)
  3. Evaluate impact of changes and recommendations (RT-04)
- **Synergies:** Complete picture of architecture health and improvement path

### Combination 2: Master Persona + Referenced Knowledge + Trade-off Acknowledgment

- **Technique Stack:** ST-01/ST-02 + ST-10 + RT-09
- **Combination Purpose:** Authoritative yet pragmatic guidance
- **Flow:**
  1. Establish master-level authority (ST-01/ST-02)
  2. Ground recommendations in industry sources (ST-10)
  3. Acknowledge trade-offs in recommendations (RT-09)
- **Synergies:** Credible advice that considers real-world constraints

### Combination 3: Quality Attributes + Evolutionary Behavior + Decision Documentation

- **Technique Stack:** DS-02 + AG-25 (novel) + DS-104 (novel)
- **Combination Purpose:** Sustainable architecture evolution
- **Flow:**
  1. Assess against quality attributes (DS-02)
  2. Enable rather than constrain change (AG-25)
  3. Document decisions for future reference (DS-104)
- **Synergies:** Architecture that can evolve with proper documentation

---

## Notes for Integration

### Add to MASTER_TECHNIQUE_INDEX:
1. **DS-104: Decision Documentation Standards** - ADRs, C4 model, etc.
2. **AG-25: Change-Enabling Behavior** - Enable change, don't prevent it

### Cross-reference with prompts:
- **code-analysis/architecture/architecture_layer_identification.md** - Architecture analysis
- **code-analysis/architecture/architecture_design_pattern_identification.md** - Pattern identification
- **engineering/engineering_delivery_sprint_planner.md** - Planning integration

### Documentation improvements:
1. **AI_AGENT_QUICK_START.md** - Add section on referenced knowledge bases
2. **CLAUDE.md** - Reference architect-review for architecture decisions
3. **agency-agents/README.md** - Document pattern-centric organization

---

## Analysis Metadata

**Analyzer:** Claude (Task 2.2 Priority 3 - Opus Agent Analysis)
**Analysis Duration:** 20 minutes
**Confidence Level:** High
**Review Status:** Draft
**Priority for Integration:** **High** (critical architecture patterns, 2 novel techniques)

---

## Technique Complexity Score

**Score: 5/5** (Maximum Complexity)

**Rationale:**
- Uses 10+ distinct techniques
- 2 novel patterns not in existing index
- Comprehensive architecture coverage (7 major domains)
- Cited industry authorities (Fowler, Evans, Martin)
- Impact assessment methodology with severity levels
- Reference implementation for architecture review agents

---

## Key Insights

1. **Pattern-centric organization is powerful**: Organizing around patterns (SOLID, DDD, Clean Architecture) enables pattern-matching for recommendations.

2. **Anti-pattern detection is as important as pattern recommendation**: Explicitly identifying violations prevents recurring problems.

3. **Change-enabling behavior is essential**: Architecture guidance that constrains too much becomes counterproductive.

4. **Referenced knowledge builds credibility**: Citing industry authorities (Fowler, Evans, Martin) grounds recommendations.

5. **Quality attributes framework enables systematic review**: Covering reliability, scalability, security, maintainability ensures comprehensive evaluation.

6. **Decision documentation standards are critical**: ADRs and C4 models ensure architectural decisions are traceable and communicable.

---

## Recommendations

1. **Document DS-104 (Decision Documentation Standards)** - Essential for decision traceability
2. **Document AG-25 (Change-Enabling Behavior)** - Prevents over-constrictive guidance
3. **Create template**: Use this agent as reference for other architecture experts
4. **Add to orchestration workflows**: architect-review should be in architecture decision flows
5. **Cross-reference with C4 agents**: Link to c4-context, c4-container, c4-component agents
