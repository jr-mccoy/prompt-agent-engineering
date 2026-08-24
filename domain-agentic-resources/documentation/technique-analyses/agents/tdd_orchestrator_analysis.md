# Technique Analysis: tdd-orchestrator

**Resource Type:** Agent (Opus 4.5)
**Path:** `claude-code-resources/agents/backend/tdd-orchestrator.md`
**Date Analyzed:** 2025-12-23
**Category:** Backend, Testing (appears in 2 categories)
**Lines:** 166

---

## Summary

The tdd-orchestrator agent demonstrates **methodology-centric expertise** centered on the TDD red-green-refactor cycle. It showcases **multi-agent coordination patterns** for orchestrating specialized testing agents and **governance capabilities** for cross-team TDD compliance. This agent exemplifies how to structure orchestration expertise for coordinated workflows.

---

## Identified Techniques

### Technique 1: Methodology-Centric Expertise

- **Category:** ST (Structural Techniques)
- **Pattern:** Define expertise around a specific methodology
- **Example from resource:**
  ```
  You are an expert TDD orchestrator specializing in comprehensive test-driven
  development coordination, modern TDD practices, and multi-agent workflow management.

  ## Expert Purpose
  Elite TDD orchestrator focused on enforcing disciplined test-driven development
  practices across complex software projects. Masters the complete red-green-refactor
  cycle...
  ```
- **Maps to existing:** NEW - ST-36 (Methodology-Centric Expertise)
- **Effectiveness:** Deep expertise in specific methodology rather than broad domain

### Technique 2: Cycle Management Pattern

- **Category:** DS (Domain-Specific)
- **Pattern:** Structure capabilities around a repeating cycle
- **Example from resource:**
  ```
  ### TDD Discipline & Cycle Management
  - Complete red-green-refactor cycle orchestration and enforcement
  - TDD rhythm establishment and maintenance across development teams
  - Test-first discipline verification and automated compliance checking
  - Refactoring safety nets and regression prevention strategies
  - TDD flow state optimization and developer productivity enhancement
  - Cycle time measurement and optimization for rapid feedback loops
  ```
- **Maps to existing:** NEW - DS-109 (Cycle Management)
- **Effectiveness:** Captures the iterative nature of TDD methodology

### Technique 3: Multi-Agent Coordination

- **Category:** AG (Agentic)
- **Pattern:** Define coordination of multiple specialized agents
- **Example from resource:**
  ```
  ### Multi-Agent TDD Workflow Coordination
  - Orchestration of specialized testing agents (unit, integration, E2E)
  - Coordinated test suite evolution across multiple development streams
  - Cross-team TDD practice synchronization and knowledge sharing
  - Agent task delegation for parallel test development and execution
  - Workflow automation for continuous TDD compliance monitoring
  ```
- **Maps to existing:** AG-07 (Multi-Agent Orchestration) - at **specialized testing level**
- **Effectiveness:** Enables coordination of unit, integration, and E2E testing agents

### Technique 4: School-Based Approach Documentation

- **Category:** DS (Domain-Specific)
- **Pattern:** Document different methodological approaches/schools
- **Example from resource:**
  ```
  ### Modern TDD Practices & Methodologies
  - Classic TDD (Chicago School) implementation and coaching
  - London School (mockist) TDD practices and double management
  - Acceptance Test-Driven Development (ATDD) integration
  - Behavior-Driven Development (BDD) workflow orchestration
  - Outside-in TDD for feature development and user story implementation
  - Inside-out TDD for component and library development
  ```
- **Maps to existing:** NEW - DS-110 (Methodological Schools)
- **Effectiveness:** Enables Claude to recommend appropriate TDD approach

### Technique 5: AI-Assisted Enhancement

- **Category:** AG (Agentic)
- **Pattern:** Dedicated section for AI-powered capabilities
- **Example from resource:**
  ```
  ### AI-Assisted Test Generation & Evolution
  - Intelligent test case generation from requirements and user stories
  - AI-powered test data creation and management strategies
  - Machine learning for test prioritization and execution optimization
  - Natural language to test code conversion and automation
  - Predictive test failure analysis and proactive test maintenance
  ```
- **Maps to existing:** AG-26 (AI-Augmented Expertise)
- **Effectiveness:** Integrates AI capabilities with TDD methodology

### Technique 6: Cross-Team Governance

- **Category:** AG (Agentic)
- **Pattern:** Capabilities for organization-wide compliance
- **Example from resource:**
  ```
  ### Cross-Team TDD Governance
  - TDD standard establishment and organization-wide implementation
  - Training program coordination and developer skill assessment
  - Code review processes with TDD compliance verification
  - TDD coaching and mentorship program management
  - TDD culture transformation and organizational change management
  ```
- **Maps to existing:** NEW - AG-29 (Cross-Team Governance)
- **Effectiveness:** Enables organization-wide methodology adoption

### Technique 7: Metrics & Quality Assurance

- **Category:** DS (Domain-Specific)
- **Pattern:** Dedicated section for measurement and tracking
- **Example from resource:**
  ```
  ### TDD Metrics & Quality Assurance
  - Comprehensive TDD metrics collection and analysis (cycle time, coverage)
  - Test quality assessment through mutation testing and fault injection
  - Code coverage tracking with meaningful threshold establishment
  - TDD velocity measurement and team productivity optimization
  - Quality gate enforcement and automated compliance reporting
  ```
- **Maps to existing:** DS-02 (Metric Specification) + QA-01 (Quality Gates)
- **Effectiveness:** Enables measurement-driven TDD improvement

### Technique 8: Legacy Code Support

- **Category:** DS (Domain-Specific)
- **Pattern:** Dedicated section for working with existing code
- **Example from resource:**
  ```
  ### Legacy Code & Refactoring Support
  - Legacy code characterization through comprehensive test creation
  - Seam identification and dependency breaking for testability improvement
  - Refactoring orchestration with safety net establishment
  - Golden master testing for legacy system behavior preservation
  - Incremental TDD adoption strategies for existing codebases
  ```
- **Maps to existing:** DS-15 (Legacy Code Patterns)
- **Effectiveness:** Enables TDD adoption in existing projects

### Technique 9: Authoritative Source Citation

- **Category:** ST (Structural Techniques)
- **Pattern:** Reference definitive methodology sources
- **Example from resource:**
  ```
  ## Knowledge Base
  - Kent Beck's original TDD principles and modern interpretations
  - Growing Object-Oriented Software Guided by Tests methodologies
  - Test-Driven Development by Example and advanced TDD patterns
  - Clean Code principles applied specifically to test code quality
  - Domain-Driven Design integration with TDD and ubiquitous language
  ```
- **Maps to existing:** ST-10 (Source Attribution)
- **Effectiveness:** Grounds agent in recognized methodology sources

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: ST-36 - Methodology-Centric Expertise

- **Description:** Define agent expertise around a specific methodology
- **Implementation:**
  ```markdown
  You are an expert [Methodology] orchestrator specializing in
  comprehensive [methodology] coordination and [methodology] practices.

  ## Expert Purpose
  Elite [Methodology] orchestrator focused on enforcing disciplined
  [methodology] practices across complex software projects. Masters
  the complete [methodology cycle]...
  ```
- **Use case:** Agents focused on specific development methodologies
- **Example:**
  ```markdown
  You are an expert TDD orchestrator specializing in comprehensive
  test-driven development coordination...
  ```
- **Proposed category:** ST (Structural Techniques)
- **Proposed code:** ST-36
- **Integration:** For methodology-focused agents (TDD, BDD, DDD, etc.)

### Pattern 2: DS-109 - Cycle Management

- **Description:** Structure capabilities around repeating methodology cycles
- **Implementation:**
  ```markdown
  ### [Methodology] Discipline & Cycle Management
  - Complete [cycle name] cycle orchestration and enforcement
  - [Methodology] rhythm establishment and maintenance
  - [Discipline] verification and automated compliance checking
  - Cycle time measurement and optimization for rapid feedback loops
  ```
- **Use case:** Iterative methodologies with defined cycles
- **Example:**
  ```markdown
  ### TDD Discipline & Cycle Management
  - Complete red-green-refactor cycle orchestration and enforcement
  - TDD rhythm establishment and maintenance across development teams
  ```
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-109
- **Integration:** For cycle-based methodology agents

### Pattern 3: DS-110 - Methodological Schools

- **Description:** Document different approaches within a methodology
- **Implementation:**
  ```markdown
  ### [Methodology] Practices & Approaches
  - [School 1] ([alternative name]) implementation
  - [School 2] ([alternative name]) practices
  - [Variant 1] for [specific use case]
  - [Variant 2] for [specific use case]
  ```
- **Use case:** Methodologies with multiple valid approaches
- **Example:**
  ```markdown
  ### Modern TDD Practices & Methodologies
  - Classic TDD (Chicago School) implementation and coaching
  - London School (mockist) TDD practices and double management
  - Outside-in TDD for feature development
  - Inside-out TDD for component development
  ```
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-110
- **Integration:** For methodologies with multiple schools

### Pattern 4: AG-29 - Cross-Team Governance

- **Description:** Capabilities for organization-wide methodology compliance
- **Implementation:**
  ```markdown
  ### Cross-Team [Methodology] Governance
  - [Methodology] standard establishment and organization-wide implementation
  - Training program coordination and developer skill assessment
  - Code review processes with [methodology] compliance verification
  - [Methodology] coaching and mentorship program management
  - [Methodology] culture transformation and organizational change management
  ```
- **Use case:** Orchestration agents responsible for org-wide adoption
- **Example:**
  ```markdown
  ### Cross-Team TDD Governance
  - TDD standard establishment and organization-wide implementation
  - TDD coaching and mentorship program management
  ```
- **Proposed category:** AG (Agentic)
- **Proposed code:** AG-29
- **Integration:** For methodology and governance agents

---

## Multi-Technique Combinations

### Combination 1: Methodology-Centric + Cycle Management + Schools

- **Technique Stack:** ST-36 (novel) + DS-109 (novel) + DS-110 (novel)
- **Combination Purpose:** Comprehensive methodology expertise
- **Flow:**
  1. Define methodology-focused identity (ST-36)
  2. Structure around methodology cycle (DS-109)
  3. Document different methodological approaches (DS-110)
- **Synergies:** Deep methodology expertise with approach flexibility

### Combination 2: Multi-Agent Coordination + AI-Assisted + Governance

- **Technique Stack:** AG-07 + AG-26 + AG-29 (novel)
- **Combination Purpose:** Scalable, AI-enhanced methodology orchestration
- **Flow:**
  1. Coordinate specialized agents (AG-07)
  2. Enhance with AI capabilities (AG-26)
  3. Apply governance across teams (AG-29)
- **Synergies:** Organization-wide methodology adoption with AI enhancement

---

## Notes for Integration

### Add to MASTER_TECHNIQUE_INDEX:
1. **ST-36: Methodology-Centric Expertise** - Methodology-focused agents
2. **DS-109: Cycle Management** - Iterative methodology cycles
3. **DS-110: Methodological Schools** - Different approaches documentation
4. **AG-29: Cross-Team Governance** - Organization-wide compliance

### Cross-reference with prompts:
- **testing/testing_unit_test_generation.md** - Unit test focus
- **testing/testing_tdd_workflow.md** - TDD workflow (if exists)
- **engineering/engineering_delivery_sprint_planner.md** - Sprint integration

---

## Analysis Metadata

**Analyzer:** Claude (Task 2.2 Priority 3 - Opus Agent Analysis)
**Analysis Duration:** 20 minutes
**Confidence Level:** High
**Review Status:** Draft
**Priority for Integration:** **High** (methodology patterns, 4 novel techniques)

---

## Technique Complexity Score

**Score: 5/5** (Maximum Complexity)

**Rationale:**
- Uses 9+ distinct techniques
- 4 novel patterns (highest for this analysis batch)
- Methodology-centric design
- Multi-agent coordination
- Cross-team governance capability
- AI-assisted enhancement
- Reference for methodology orchestration agents

---

## Key Insights

1. **Methodology-centric expertise enables depth**: Focusing on TDD methodology creates deep expertise.

2. **Cycle management captures iterative nature**: Red-green-refactor cycle is fundamental structure.

3. **School documentation enables flexibility**: Chicago vs London School enables appropriate approach selection.

4. **Cross-team governance enables scale**: Organization-wide TDD adoption requires governance capabilities.

5. **AI-assisted testing is the future**: ML for test prioritization, natural language to tests.

6. **Legacy code support enables adoption**: TDD adoption in existing codebases requires specific patterns.

---

## Recommendations

1. **Document ST-36 (Methodology-Centric)** for methodology-focused agents
2. **Document DS-109 (Cycle Management)** for iterative methodology agents
3. **Document DS-110 (Methodological Schools)** for approach flexibility
4. **Document AG-29 (Cross-Team Governance)** for org-wide adoption
5. **Template for methodology agents**: tdd-orchestrator structure works for BDD, DDD, etc.
6. **Link to testing agents**: test-automator should be coordinated by tdd-orchestrator
