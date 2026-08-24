# Prompt Engineering Technique Lookup by Use Case

**Purpose:** Quick reference guide for AI agents to select appropriate prompt engineering techniques based on user needs.
**Coverage:** Spans all 18 technique categories. The most commonly combined techniques appear in at least one use case below; for the full catalog (327 active techniques) see [MASTER_TECHNIQUE_INDEX.md](MASTER_TECHNIQUE_INDEX.md).
**Last Updated:** 2026-06-11

> **Creating a new prompt?** Use the [Authoring Toolkit](../authoring/NEW_PROMPT_TEMPLATE.md): template, technique picker, and checklist.
> **Need technique details?** See [MASTER_TECHNIQUE_INDEX.md](MASTER_TECHNIQUE_INDEX.md) for full definitions.

---

## Table of Contents

**Use Case Categories:**
1. [Analysis & Review Tasks](#analysis--review-tasks)
2. [Creation & Generation Tasks](#creation--generation-tasks)
3. [Teaching & Explanation Tasks](#teaching--explanation-tasks)
4. [Decision & Planning Tasks](#decision--planning-tasks)
5. [Problem-Solving Tasks](#problem-solving-tasks)
6. [Quality Assurance & Verification Tasks](#quality-assurance--verification-tasks)
7. [Task Completion & Done Definition Tasks](#task-completion--done-definition-tasks)
8. [Agentic Resource Development Tasks](#agentic-resource-development-tasks)
9. [Non-Engineering & Conversational Tasks](#non-engineering--conversational-tasks)
10. [Visual Output & Image Generation Tasks](#visual-output--image-generation-tasks)
11. [Documentation & Interaction Design Tasks](#documentation--interaction-design-tasks)
12. [Infrastructure & Domain-Specific Tasks](#infrastructure--domain-specific-tasks)
13. [AI Delegation & Productivity Tasks](#ai-delegation--productivity-tasks)
14. [Personal Agency & Execution Tasks](#personal-agency--execution-tasks)
15. [Quality Systems & Process Tasks](#quality-systems--process-tasks)
16. [Multi-Agent Architecture Tasks](#multi-agent-architecture-tasks)

**Reference Sections:**
- [Quick Selection Guide](#quick-selection-guide)
- [Technique Differentiation Guide](#technique-differentiation-guide)
- [Combination Ordering Rules](#combination-ordering-rules)
- [Technique Compatibility Matrix](#technique-compatibility-matrix)
- [Complete Technique Coverage Index](#complete-technique-coverage-index)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
- [AI Agent Workflow](#ai-agent-workflow)

---

## Analysis & Review Tasks

### Code Quality Analysis
**User Need:** Analyze code for quality, complexity, maintainability issues

**Essential Techniques:**
1. **Clear Objective Statement** (ST-01) — Define what quality aspects to analyze
2. **Structured Sequential Instructions** (ST-02) — Walk through analysis systematically
3. **Multi-Dimensional Analysis** (RT-02) — Cover location, impact, severity, recommendations
4. **Evidence-Based Reasoning** (RT-05) — Require file paths, line numbers, code examples
5. **Prioritization Guidance** (DS-06) — Rank issues by severity/impact

**Enhancement Techniques:**
- **Output Format Specification** (ST-03) — Ensure consistent issue reporting
- **Conditional Output Logic** (OC-04) — Handle cases where no issues found
- **Multi-Layer Analysis** (DT-04) — Analyze at multiple abstraction levels simultaneously
- **Element-by-Element Assessment Matrix** (DT-05) — Systematic component-by-component evaluation
- **Grouped Reporting by Pattern Type** (OC-11) — Organize findings by issue category
- **Three-Tier Value Classification** (ST-40) — Classify findings as critical/important/nice-to-have

**Combination Guidance:**
> **Synergy:** ST-01 focuses the analysis on specific quality dimensions, ST-02 ensures systematic coverage, RT-02 prevents tunnel vision by analyzing from multiple angles, RT-05 grounds each finding in concrete evidence (file paths, line numbers), and DS-06 makes results actionable by ranking severity.
> **Order:** ST-01 → ST-02 → RT-02 → RT-05 → DS-06 → ST-03
> **Avoid:** Don't pair with OC-05 (minimum length) — it produces padding. Don't add RP-01 (expert role) unless specialized domain expertise is needed beyond general code quality.
> **Fallback:** If analysis is too shallow, replace RT-02 with DT-04 (Multi-Layer Analysis) to force examination at function, module, and system levels. If output is disorganized, add OC-11 (Grouped Reporting).

**Example Prompts:**
- `domain-software-engineering/analysis/quality/quality_code_complexity_analysis.md`
- `domain-software-engineering/analysis/quality/quality_code_duplication_analysis.md`

**Template Pattern:**
```
**Objective:** Analyze codebase for [specific quality aspect]

**Instructions:**
1. Review the codebase and identify areas with [specific issues]
2. For each identified issue, analyze:
   a. Location: File path, line number(s)
   b. Description: What the issue is
   c. Impact: Effect on [quality attributes]
   d. Severity: Low/Medium/High
   e. Recommendations: Specific fixes

3. If no significant issues found, state that [quality aspect] is acceptable

**Expected Output:** Comprehensive report with:
- Overview of findings
- Detailed breakdowns per issue using format:
  File: [path]
  Line(s): [numbers]
  Issue: [description]
  Impact: [impact]
  Severity: [level]
  Suggestions: [fixes]
```

---

### Performance Analysis
**User Need:** Identify performance bottlenecks, optimization opportunities

**Essential Techniques:**
1. **Clear Objective Statement** (ST-01) — Define performance goals
2. **Tool and Methodology Suggestions** (DS-03) — Guide use of profiling tools
3. **Metric Specification** (DS-02) — Define measurable performance criteria
4. **Prioritization Guidance** (DS-06) — Rank by impact on performance
5. **Correlation Analysis** (RT-06) — Connect multiple performance factors

**Enhancement Techniques:**
- **Hierarchical Task Breakdown** (DT-01) — Analyze at system, module, function levels
- **Cascade Effect Analysis** (RT-07) — Trace how one bottleneck cascades through the system
- **Workaround Cost Analysis** (RT-08) — Evaluate cost of leaving issues vs fixing them

**Combination Guidance:**
> **Synergy:** ST-01 anchors the analysis to specific performance goals, DS-03 provides concrete profiling methodology, DS-02 defines measurable thresholds, RT-05 requires actual numbers (not guesses), and DS-06 focuses effort on the highest-impact bottlenecks first.
> **Order:** ST-01 → DS-02 → DS-03 → RT-05 → RT-06 → DS-06
> **Avoid:** Don't combine with RP-03 (Multi-Persona Debate) — performance analysis is objective and measurable, not a matter of perspective. Avoid DT-05 (Element-by-Element Matrix) for large codebases — it produces exhaustive but low-signal output.
> **Fallback:** If bottlenecks aren't emerging, add RT-07 (Cascade Effect Analysis) to trace how one slow component cascades through the system. If recommendations are too vague, add RT-08 (Workaround Cost Analysis) to quantify the cost of inaction.

**Example Prompts:**
- `domain-software-engineering/analysis/performance/performance_bottleneck_identification.md`
- `domain-software-engineering/analysis/performance/performance_code_optimization_suggestions.md`

---

### Security Audit
**User Need:** Find security vulnerabilities, compliance issues

**Essential Techniques:**
1. **Specific Focus Areas** (DT-02) — List specific vulnerabilities to check (SQL injection, XSS, etc.)
2. **Expert Role Assignment** (RP-01) — Frame as security expert
3. **Prioritization Guidance** (DS-06) — Severity-based ranking (Critical/High/Medium/Low)
4. **Evidence-Based Reasoning** (RT-05) — Require proof of vulnerabilities

**Security-Specific Techniques:**
- **Chain-of-Verification** (QA-01) — Double-check security findings
- **Adversarial Stress-Test** (QA-02) — Think like an attacker
- **STRIDE-Per-Interaction Matrix** (DS-50) — Systematic threat modeling per component interaction
- **Security Tier Classification** (DS-61) — Classify assets by security sensitivity tier
- **Security-Default Behavioral Traits** (DS-118) — Embed security-first thinking into analysis behavior
- **Criticality Labeling** (ST-42) — Label each finding with criticality level
- **Risk-Stratified Documentation** (ST-43) — Document differently based on risk level
- **Checks-Effects-Interactions Pattern** (ST-49) — Verify checks, trace effects, map interactions

**Combination Guidance:**
> **Synergy:** RP-01 establishes the attacker mindset, DT-02 ensures comprehensive coverage of vulnerability categories, RT-05 prevents false positives by requiring evidence, QA-02 stress-tests findings by thinking like an attacker, and DS-06 ensures critical vulnerabilities surface first.
> **Order:** RP-01 → DT-02 → RT-05 → DS-06 → QA-01 → QA-02
> **Avoid:** Don't pair QA-02 with NE-07 (Emotional Validation) — security audits require blunt honesty, not empathy. Don't use AG-01 (Personality-First) when RP-01 suffices — security audits need expertise, not persona.
> **Fallback:** If findings are too generic, add DS-50 (STRIDE-Per-Interaction Matrix) for systematic threat modeling. If the codebase is too large for comprehensive review, add DT-01 (Hierarchical Breakdown) to prioritize high-risk attack surfaces.

**Example Prompts:**
- `domain-software-engineering/analysis/security/security_vulnerability_analysis.md`

---

### Architecture Analysis
**User Need:** Review system architecture, identify design patterns, evaluate structural decisions

**Essential Techniques:**
1. **Architecture-First Enforcement** (DS-13) — Require architecture-level thinking before implementation details
2. **Hierarchical Organization** (ST-05) — Structure analysis by system layers
3. **Multi-Dimensional Analysis** (RT-02) — Cover scalability, maintainability, security, performance
4. **Cascade Effect Analysis** (RT-07) — Trace how architectural decisions propagate through the system
5. **Pattern Recognition** (DS-04) — Identify design patterns in use

**Enhancement Techniques:**
- **Ecosystem Mapping** (DS-30) — Map the technology ecosystem and dependencies
- **Workaround Cost Analysis** (RT-08) — Evaluate technical debt cost vs refactoring cost
- **Async-First Design Principle** (DS-113) — Evaluate asynchronous architecture patterns
- **Federation Architecture** (DS-114) — Assess federated vs monolithic patterns
- **Summary-Expand Loop** (CM-04) — Provide high-level summary, then drill into details

**Combination Guidance:**
> **Synergy:** DS-13 forces architecture-level thinking before implementation details, ST-05 organizes analysis by system layers (preventing scattered findings), RT-02 covers multiple quality attributes (scalability, maintainability, security), DS-04 identifies existing patterns, and RT-07 traces how architectural decisions cascade through the system.
> **Order:** DS-13 → ST-05 → RT-02 → DS-04 → RT-07
> **Avoid:** Don't combine with ST-02 (Sequential Instructions) — architecture analysis is inherently multi-dimensional, not sequential. Avoid DS-02 (Metric Specification) unless quantitative benchmarks are available — architecture reviews are often qualitative.
> **Fallback:** If the analysis is too abstract, add CM-04 (Summary-Expand Loop) to provide high-level summary then drill into specific layers. If recommendations lack actionability, add RT-08 (Workaround Cost Analysis) to quantify refactoring vs. living-with-debt tradeoffs.

**Example Prompts:**
- `domain-software-engineering/analysis/architecture/architecture_layer_identification.md`
- `domain-software-engineering/analysis/architecture/architecture_design_pattern_identification.md`

---

### Business/Strategic Analysis
**User Need:** Apply business frameworks (SWOT, Porter's Five Forces, etc.) to codebase or product

**Essential Techniques:**
1. **Framework Application** (DS-01) — Use established analytical framework
2. **Explicit Context Framing** (CM-01) — Provide business context
3. **Hierarchical Organization** (ST-05) — Structure around framework dimensions
4. **Delimited Sections** (ST-04) — Clear sections per framework component

**Enhancement Techniques:**
- **Multi-Dimensional Analysis** (RT-02) — Thorough coverage of each dimension
- **Pattern Recognition** (DS-04) — Identify trends across framework
- **Multi-Source Narrative Synthesis** (DS-19) — Synthesize insights from multiple data sources
- **Follow-Up Action Extraction** (DS-40) — Extract concrete next steps from analysis
- **Scope Reduction Pressure** (NE-09) — Force focus on the most impactful findings

**Combination Guidance:**
> **Synergy:** DS-01 provides the analytical framework structure, CM-01 grounds the analysis in real business context, ST-05 organizes findings by framework dimensions, ST-04 keeps sections cleanly separated, and RT-02 ensures thorough coverage of each dimension.
> **Order:** CM-01 → DS-01 → ST-05 → ST-04 → RT-02 → DS-04
> **Avoid:** Don't combine with DT-02 (Specific Focus Areas) when using DS-01 — the framework already provides the focus areas. Don't pair with NE-05 (Token Budget) for strategic analyses — they require depth.
> **Fallback:** If the analysis lacks actionable insights, add DS-40 (Follow-Up Action Extraction) to force concrete next steps. If the analysis is too broad, add NE-09 (Scope Reduction Pressure) to focus on the 2-3 most impactful findings.

**Example Prompts:**
- `domain-business-strategy/analysis/swot_analysis.md`
- `domain-business-strategy/analysis/business_model_canvas_analysis.md`

**Template Pattern:**
```
**Objective:** Conduct [FRAMEWORK NAME] analysis of the codebase

**Context:**
- [Business/product context]
- [Market context]
- [Technical context]

**Instructions:**
1. Review the codebase considering [framework aspects]
2. Analyze according to [FRAMEWORK] structure:
   a. [Framework Dimension 1]:
      - [Specific questions/criteria]
   b. [Framework Dimension 2]:
      - [Specific questions/criteria]

3. For each point, provide specific examples from codebase
4. Suggest strategies to [leverage/address/capitalize/mitigate]

**Expected Output:** Comprehensive [FRAMEWORK] analysis with actionable insights
```

---

## Creation & Generation Tasks

### Code Generation
**User Need:** Generate new code, functions, classes, modules

**Essential Techniques:**
1. **Explicit Context Framing** (CM-01) — Provide tech stack, patterns, conventions
2. **Constraint Specification** (CM-02) — Must/must-not requirements
3. **Output Format Specification** (ST-03) — Show expected code structure
4. **Version-Specific Expertise** (DS-107) — Pin to specific language/framework versions

**Quality Techniques:**
- **Self-Verification** (QA-01) — Review generated code
- **Specific Focus Areas** (DT-02) — Check for common issues (security, performance)
- **Output Contract Structure** (OC-06) — Define exact output format contract
- **Operating Principles Declaration** (OC-07) — Declare coding principles to follow
- **Multi-Tiered Template Library** (DS-80) — Use templates for common code patterns
- **Production-Ready Architecture Patterns** (ST-38/39) — Ensure production-grade output
- **Principle-Based Guidance** (ST-35) — Embed design principles into generation
- **Behavioral Trait Declarations** (ST-16) — Define code style behaviors

**Combination Guidance:**
> **Synergy:** CM-01 provides tech stack context that shapes all generated code, CM-02 sets hard constraints (security, performance), ST-03 defines the expected output shape, DS-107 pins to specific versions preventing deprecated API usage, and QA-01 catches common generation errors.
> **Order:** CM-01 → CM-02 → DS-107 → ST-16 → ST-03 → QA-01
> **Avoid:** Don't combine ST-03 with OC-02 (JSON Schema) unless output is literally JSON — using both creates conflicting format expectations. Don't pair OC-07 (Operating Principles) with ST-16 (Behavioral Traits) — they overlap; pick one.
> **Fallback:** If generated code is too boilerplate, add DS-80 (Multi-Tiered Template Library) for richer patterns. If code doesn't match project conventions, strengthen CM-01 with actual code examples from the existing codebase.

**Best Practices:**
- Specify language version, framework versions
- Provide existing code style examples
- Define error handling requirements
- Specify testing expectations

---

### Configuration Generation
**User Need:** Generate configuration files, infrastructure-as-code, deployment configs

**Essential Techniques:**
1. **Safe Defaults Pattern** (DS-26) — Always start with secure, production-safe defaults
2. **Professional Defaults Library** (DS-27) — Use industry-standard default configurations
3. **Environment-Specific Guidance** (DS-28) — Differentiate dev/staging/production settings
4. **Configuration-Driven Workflow Customization** (DS-39) — Parameterize workflows via config

**Enhancement Techniques:**
- **Domain Pattern Library** (DS-29) — Reference established configuration patterns for the domain
- **Constraint Specification** (CM-02) — Define hard constraints on configuration values
- **External Methodology Compliance** (DS-111) — Ensure configs meet external standards (CIS, NIST, etc.)

**Combination Guidance:**
> **Synergy:** DS-26 provides secure baseline defaults, DS-27 ensures industry-standard values, DS-28 differentiates environments so dev configs don't leak into production, and DS-39 parameterizes for reuse across environments.
> **Order:** CM-02 → DS-26 → DS-27 → DS-28 → DS-39
> **Avoid:** Don't combine with RP-01 (Expert Role) — configuration generation needs precision, not persona. Avoid RT-03 (Tree of Thoughts) for config files — there's usually one right answer, not multiple alternatives to debate.
> **Fallback:** If configs are too generic, add DS-29 (Domain Pattern Library) for domain-specific patterns. If compliance is required, add DS-111 (External Methodology Compliance) to enforce CIS/NIST standards.

**Example Prompts:**
- `domain-software-engineering/devops/devops_terraform_best_practices.md`
- `domain-software-engineering/devops/devops_dockerfile_optimization.md`

---

### Documentation Generation
**User Need:** Create documentation, comments, API docs, README files

**Essential Techniques:**
1. **Audience-Specific Framing** (RP-02) — Who will read this?
2. **Output Format Specification** (ST-03) — Structure and content requirements
3. **Delimited Sections** (ST-04) — Organize documentation clearly
4. **Documentation-as-Product Philosophy** (NE-19) — Treat docs as a first-class product

**Enhancement Techniques:**
- **Visualization and Communication Guidance** (DS-05) — Include diagrams where helpful
- **Analogical Reasoning** (RT-04) — Explain complex concepts clearly
- **Multi-Audience Documentation Targeting** (NE-14) — Write for multiple audiences simultaneously
- **Progressive Abstraction Transformation** (DS-37) — Layer from abstract to concrete
- **Long-Form Documentation Process** (DS-38) — Structure long document creation
- **Multi-Mode Prompt Architecture** (OC-08) — Support multiple documentation modes (tutorial, reference, etc.)

**Combination Guidance:**
> **Synergy:** RP-02 ensures the right language and depth for the target audience, ST-03 defines the documentation structure, ST-04 keeps sections cleanly separated, and NE-19 elevates docs from afterthought to first-class product with quality standards.
> **Order:** RP-02 → CM-01 → NE-19 → ST-04 → ST-03
> **Avoid:** Don't combine NE-19 (Documentation-as-Product) with NE-05 (Token Budget) — treating docs as a product means giving them the space they need. Don't pair RP-02 with RP-01 (Expert Role) — audience framing already implies the appropriate voice.
> **Fallback:** If docs are too flat, add DS-37 (Progressive Abstraction) to layer from summary to deep detail. If docs serve multiple audiences, add NE-14 (Multi-Audience Targeting) to handle different reader needs in one document.

**Example Prompts:**
- `domain-software-engineering/analysis/quality/quality_documentation_generation.md`

---

### Test Generation
**User Need:** Create unit tests, integration tests, test scenarios

**Essential Techniques:**
1. **Specific Focus Areas** (DT-02) — List edge cases, error conditions
2. **Structured Sequential Instructions** (ST-02) — Cover different test categories
3. **Output Format Specification** (ST-03) — Consistent test structure
4. **TDD-First Development Pattern** (DS-148) — Structure tests before implementation

**Enhancement Techniques:**
- **Strategic Edge Case Calibration** (MP-04) — Ensure edge cases covered
- **Documentation-Driven Testing** (DS-34) — Generate tests from documentation/specs
- **Test Battery Protocol** (QA-10) — Define comprehensive test suites
- **Pass/Fail Test Harness** (QA-11) — Create clear pass/fail criteria
- **LLM-as-Judge with Rubric** (DS-35) — Use AI evaluation with scoring rubrics

**Combination Guidance:**
> **Synergy:** DT-02 enumerates edge cases and error conditions to cover, ST-02 organizes tests into logical categories (happy path → edge cases → error conditions), ST-03 ensures consistent test structure, and DS-148 structures tests before implementation.
> **Order:** CM-01 → DT-02 → ST-02 → DS-148 → ST-03 → QA-10
> **Avoid:** Don't combine DS-148 (TDD-First) with QA-10 (Test Battery Protocol) upfront — TDD starts with minimal tests that grow; test batteries are comprehensive from the start. Use one approach per phase.
> **Fallback:** If tests are too superficial, add MP-04 (Edge Case Calibration) to systematically identify untested paths. If test coverage is unclear, add DS-34 (Documentation-Driven Testing) to derive tests from specifications.

**Example Prompts:**
- `domain-software-engineering/testing/testing_unit_test_generation.md`
- `domain-software-engineering/testing/testing_e2e_test_scenario_creation.md`

---

### Presentation & Report Generation
**User Need:** Create slide decks, board presentations, executive reports

**Essential Techniques:**
1. **Assertion-Evidence Content Structure** (ST-46) — Structure slides as assertion + evidence pairs
2. **Visual Output Specification** (SV-01) — Define visual layout requirements
3. **Audience-Specific Framing** (RP-02) — Match content to audience level
4. **Chart Selection Dictionary** (DS-25) — Choose the right visualization type

**Enhancement Techniques:**
- **Data Storytelling Framework** (NE-15) — Structure narrative around data
- **Delimited Sections** (ST-04) — Clear content sections
- **Call-to-Action Mandatory Close** (NE-17) — End with specific asks

**Combination Guidance:**
> **Synergy:** ST-46 structures each slide as an assertion backed by evidence (the most effective presentation format), SV-01 defines the visual layout, RP-02 calibrates complexity to the audience, and DS-25 ensures the right chart type for each data point.
> **Order:** RP-02 → ST-46 → SV-01 → DS-25 → NE-15
> **Avoid:** Don't combine ST-46 (Assertion-Evidence) with ST-02 (Sequential Instructions) — slides need assertion-evidence pairs, not step-by-step procedures. Don't pair with OC-05 (Min Length) — presentations should be concise.
> **Fallback:** If the presentation lacks narrative flow, add NE-15 (Data Storytelling) to weave data into a coherent story. If the audience needs action items, add NE-17 (Call-to-Action Mandatory Close).

**Example Prompts:**
- `domain-presentations/board_deck_opportunity_solution_tree.md`

---

## Teaching & Explanation Tasks

### Explain Code/Concept
**User Need:** Understand how code works, learn new concept

**Essential Techniques:**
1. **Audience-Specific Framing** (RP-02) — Match explanation to user level
2. **Analogical Reasoning** (RT-04) — Use familiar analogies
3. **Chain-of-Thought** (RT-01) — Show step-by-step logic
4. **Delimited Sections** (ST-04) — Organize explanation clearly

**Enhancement Techniques:**
- **Socratic Dialogue** (RP-04) — Interactive Q&A format
- **Progressive Example Complexity** (IT-20) — Start simple, build up
- **Progressive Complexity Scaffolding** (ST-44) — Layer complexity gradually
- **Root Cause Explanation** (RT-09) — Explain the "why" behind behaviors
- **Reference Class Priming** (ED-05) — Connect to familiar reference points

**Combination Guidance:**
> **Synergy:** RP-02 calibrates explanations to the learner's level, RT-04 makes abstract concepts concrete through familiar analogies, RT-01 reveals reasoning step-by-step so the learner follows the logic, and ST-04 organizes the explanation into digestible sections.
> **Order:** RP-02 → ST-04 → RT-04 → RT-01
> **Avoid:** Don't combine with DS-06 (Prioritization) — explanations should flow logically, not by severity ranking. Don't pair RT-04 (Analogical) with RT-02 (Multi-Dimensional) — analogies simplify, multi-dimensional analysis adds complexity.
> **Fallback:** If the explanation is still too abstract, add IT-20 (Progressive Example Complexity) to build from simple to complex examples. If the learner needs more structure, add ST-44 (Progressive Complexity Scaffolding).

**Example Prompts:**
- `domain-learning-coding/learning_code_analogies_metaphors.md`
- `domain-learning-coding/learning_algorithmic_storytelling.md`

---

### Interactive Teaching
**User Need:** Learn through practice, exercises, feedback

**Essential Techniques:**
1. **Iterative Scaffolding** (ED-01) — One concept at a time, check understanding
2. **Progressive Exercise Generation** (ED-02) — Matched to skill level
3. **Guided Discovery** (ED-03) — Questions instead of answers
4. **Personalization Hooks** (ED-04) — Incorporate interests

**Enhancement Techniques:**
- **Example Quantity Specification** (ED-06) — Control how many examples to provide
- **Template-Based Educational Scaffolding** (IT-24) — Use structured templates for exercises
- **Mentor-Style Feedback** (IT-35) — Provide feedback in a mentoring tone

**Combination Guidance:**
> **Synergy:** ED-01 builds concepts one at a time (preventing overwhelm), ED-02 generates exercises matched to skill level, ED-03 uses questions to drive discovery (more effective than lecturing), and ED-04 incorporates the learner's interests to maintain engagement.
> **Order:** ED-04 → ED-01 → ED-03 → ED-02
> **Avoid:** Don't combine ED-03 (Guided Discovery) with ST-02 (Sequential Instructions) — discovery-based learning requires flexibility, not rigid sequences. Don't pair with NE-05 (Token Budget) — teaching needs room to elaborate.
> **Fallback:** If the learner is struggling, replace ED-03 (Guided Discovery) with IT-24 (Template-Based Scaffolding) for more structured support. If exercises are too easy/hard, strengthen ED-02 with explicit difficulty calibration.

**Best Practices:**
- Ask one question at a time
- Check understanding before proceeding
- Don't give answers immediately
- Provide hints when stuck

**Example Prompts:**
- `domain-learning-coding/learning_teach_me_to_code.md`
- `domain-learning-coding/learning_code_refactoring_exercises.md`

---

### Code Review as Teaching
**User Need:** Learn through reviewing code

**Essential Techniques:**
1. **Socratic Dialogue** (RP-04) — Ask questions about design decisions
2. **Multi-Dimensional Analysis** (RT-02) — Consider multiple aspects
3. **Guided Discovery** (ED-03) — Help find issues themselves
4. **Mentor-Style Feedback** (IT-35) — Supportive, growth-oriented feedback

**Combination Guidance:**
> **Synergy:** RP-04 drives learning through questions rather than answers, RT-02 ensures multiple quality dimensions are covered (readability, performance, security), ED-03 helps learners discover issues themselves (deeper retention), and IT-35 delivers feedback in a supportive, growth-oriented tone.
> **Order:** RP-04 → RT-02 → ED-03 → IT-35
> **Avoid:** Don't combine RP-04 (Socratic) with DS-06 (Prioritization) — Socratic dialogue should follow the learner's discovery path, not a pre-ranked severity list. Don't pair with QA-02 (Adversarial Stress-Test) — stress-testing is for verification, not teaching.
> **Fallback:** If the learner can't find issues through Socratic questioning, switch to IT-35 (Mentor-Style Feedback) with progressively more explicit hints. If the code has too many issues, add DT-02 (Specific Focus Areas) to narrow the review scope.

**Example Prompts:**
- `domain-learning-coding/learning_socratic_dialogue_code_review.md`

---

## Decision & Planning Tasks

### Architecture Decisions
**User Need:** Choose between architectural approaches, design patterns

**Essential Techniques:**
1. **Tree of Thoughts** (RT-03) — Generate multiple approaches with pros/cons
2. **Multi-Persona Debate** (RP-03) — Different stakeholder perspectives
3. **Expert Role Assignment** (RP-01) — Senior architect perspective
4. **Explicit Context Framing** (CM-01) — System requirements, constraints

**Enhancement Techniques:**
- **Adversarial Stress-Test** (QA-02) — Challenge each approach
- **Uncertainty Acknowledgment** (QA-04) — State tradeoffs clearly
- **Multi-Solution Comparison Matrix** (ST-22) — Side-by-side option comparison
- **Probability-Weighted Scenarios** (NE-10) — Weight outcomes by likelihood
- **Cascade Effect Analysis** (RT-07) — Trace downstream consequences of each choice
- **Workaround Cost Analysis** (RT-08) — Evaluate cost of living with each tradeoff

**Template Pattern:**
```
**Context:**
- System requirements: [...]
- Current constraints: [...]
- Scale requirements: [...]

**Decision:** [What needs to be decided]

**Generate 3 different approaches:**

**Approach 1: [Name]**
Description: [How it works]
Pros:
- [Advantage 1]
- [Advantage 2]
Cons:
- [Disadvantage 1]
- [Disadvantage 2]
Best for: [Scenarios]

[Repeat for Approaches 2 and 3]

**Recommendation:**
Based on the context provided, [Approach X] is recommended because:
- [Reason 1]
- [Reason 2]

**Tradeoffs accepted:**
- [What we're giving up]
- [Why it's acceptable]
```

**Combination Guidance:**
> **Synergy:** RT-03 generates genuinely different approaches (not variations of one), RP-03 brings different stakeholder perspectives to evaluate each approach, RP-01 grounds the evaluation in senior architectural expertise, CM-01 ensures decisions are made in the right context, and QA-02 stress-tests the leading approach.
> **Order:** CM-01 → RP-01 → RT-03 → RP-03 → QA-02 → QA-04
> **Avoid:** Don't combine RT-03 (Tree of Thoughts) with NE-01 (Single-Question) — ToT requires internal branching, not interactive dialogue. Don't pair RP-01 with AG-01 — AG-01 subsumes RP-01; use one or the other.
> **Fallback:** If approaches are too similar, strengthen RT-03 by adding explicit constraints like "one approach must be radically different." If the decision is too complex, add ST-22 (Multi-Solution Comparison Matrix) for side-by-side evaluation.

**Example Prompts:**
- `domain-software-engineering/analysis/architecture/architecture_refactoring_for_design_patterns.md`
- `domain-software-engineering/analysis/architecture/architecture_design_pattern_identification.md`

---

### Project Planning
**User Need:** Plan migration, refactoring, feature development

**Essential Techniques:**
1. **Hierarchical Task Breakdown** (DT-01) — Phases, tasks, dependencies
2. **Structured Sequential Instructions** (ST-02) — Logical workflow
3. **Explicit Context Framing** (CM-01) — Current state, goals, constraints
4. **Scope Definition** (CM-03) — Clear boundaries on what's in/out of scope

**Enhancement Techniques:**
- **Fail-Fast Ordering** (DD-03) — Order tasks so failures surface early
- **MVP Gates** (DD-04) — Define minimum viable checkpoints
- **EARS Requirements Transformation** (DS-22) — Transform vague requirements into structured format

**Combination Guidance:**
> **Synergy:** DT-01 breaks the project into phases with clear dependencies, ST-02 orders tasks logically, CM-01 provides the current state and goals, and CM-03 prevents scope creep by setting explicit boundaries.
> **Order:** CM-03 → CM-01 → DT-01 → ST-02
> **Avoid:** Don't combine DT-01 (Hierarchical Breakdown) with DT-02 (Specific Focus Areas) — use DT-01 for decomposing work, DT-02 for auditing known categories. Don't pair with RT-03 (Tree of Thoughts) for planning — planning needs one good path, not multiple options.
> **Fallback:** If the plan lacks risk awareness, add DD-03 (Fail-Fast Ordering) to surface failures early. If requirements are vague, add DD-02 (Vague-to-Concrete Translation) before planning.

**Example Prompts:**
- `domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md`

---

### Strategic Planning
**User Need:** Long-term technical strategy, roadmap

**Essential Techniques:**
1. **Framework Application** (DS-01) — Use strategic frameworks
2. **Multi-Persona Debate** (RP-03) — Different perspectives
3. **Tree of Thoughts** (RT-03) — Explore options
4. **Pattern Recognition** (DS-04) — Identify trends

**Enhancement Techniques:**
- **Frontier Mapping** (DS-20) — Classify capabilities by maturity (proven/emerging/experimental)
- **Proximity Assessment** (DS-21) — Assess how close each option is to readiness
- **Scope Reduction Pressure** (NE-09) — Force focus on highest-impact strategic priorities

**Combination Guidance:**
> **Synergy:** DS-01 provides strategic framework structure, RP-03 brings multiple stakeholder perspectives (CTO, CFO, PM), RT-03 generates genuinely different strategic options, and DS-04 identifies trends and patterns that inform the strategy.
> **Order:** CM-01 → DS-01 → RP-03 → RT-03 → DS-04
> **Avoid:** Don't combine with DT-02 (Specific Focus Areas) — the strategic framework already provides the analysis structure. Don't pair NE-09 (Scope Reduction) too early — strategic planning needs initial breadth before narrowing.
> **Fallback:** If the strategy is too abstract, add DS-20 (Frontier Mapping) to classify capabilities by maturity. If options lack differentiation, add DS-21 (Proximity Assessment) to evaluate readiness of each option.

**Example Prompts:**
- `domain-business-strategy/analysis/`
- `domain-engineering-workflows/workflows/engineering_goal_system_designer.md`

---

## Problem-Solving Tasks

### Debugging
**User Need:** Find and fix bugs, understand errors

**Essential Techniques:**
1. **Chain-of-Thought** (RT-01) — Step-by-step reasoning
2. **Evidence-Based Reasoning** (RT-05) — Analyze stack traces, logs
3. **Hierarchical Task Breakdown** (DT-01) — Isolate problem systematically

**Specialist Techniques:**
- **Root Cause Explanation** (RT-09) — Explain the fundamental reason for the bug
- **Troubleshooting Decision Tree** (RT-10) — Structured diagnostic flowchart
- **Error Recovery Patterns** (RT-11) — Template-based recovery strategies for common error types
- **Symptom-Based Troubleshooting** (IT-23) — Organize diagnosis starting from observable symptoms
- **Task Clarification** (MP-03) — Clarify ambiguous problem descriptions before solving

**Template Pattern:**
```
**Objective:** Debug [issue description]

**Evidence:**
- Error message: [...]
- Stack trace: [...]
- Expected behavior: [...]
- Actual behavior: [...]

**Instructions:**
1. Analyze the error message and stack trace
2. Identify the root cause (not just symptoms)
3. Explain why this error occurs
4. Provide the fix with explanation
5. Suggest how to prevent similar issues

Think through this step-by-step.
```

**Combination Guidance:**
> **Synergy:** RT-01 traces the logic chain from symptom to cause (preventing premature conclusions), RT-05 grounds the diagnosis in concrete evidence (stack traces, logs), and DT-01 isolates the problem by systematically narrowing scope.
> **Order:** RT-05 → RT-01 → DT-01
> **Avoid:** Don't combine with RP-03 (Multi-Persona Debate) — debugging needs focused investigation, not perspective-gathering. Don't pair RT-01 with RT-03 (Tree of Thoughts) — debugging follows one chain of evidence, not multiple speculative branches.
> **Fallback:** If the root cause isn't surfacing, add RT-10 (Troubleshooting Decision Tree) for a structured diagnostic flowchart. If the problem is intermittent, add RT-09 (Root Cause Explanation) to look deeper at systemic causes.

**Example Prompts:**
- `domain-engineering-workflows/workflows/engineering_prompt_for_debugging_code.md`

---

### Optimization
**User Need:** Improve performance, reduce complexity, refactor

**Essential Techniques:**
1. **Multi-Dimensional Analysis** (RT-02) — Current state, issues, opportunities
2. **Prioritization Guidance** (DS-06) — Rank by impact vs. effort
3. **Evidence-Based Reasoning** (RT-05) — Measure before and after

**Enhancement Techniques:**
- **Correlation Analysis** (RT-06) — Connect related issues
- **Pattern Recognition** (DS-04) — Find systemic problems
- **Iterative Refinement** (DT-03) — Progressive improvement cycles

**Combination Guidance:**
> **Synergy:** RT-02 ensures optimization is considered from multiple angles (performance, readability, maintainability), DS-06 ranks opportunities by impact-vs-effort, RT-05 requires measurable before/after evidence, and DT-03 enables iterative improvement rather than big-bang refactoring.
> **Order:** RT-02 → RT-05 → DS-06 → DT-03
> **Avoid:** Don't combine with RP-01 (Expert Role) unless the optimization domain is specialized (e.g., GPU, database). Don't pair DS-06 (Prioritization) with DT-05 (Element-by-Element Matrix) — prioritization is about focusing, matrices are about exhaustive coverage.
> **Fallback:** If optimizations are too incremental, add RT-06 (Correlation Analysis) to find systemic issues connecting multiple symptoms. If the codebase is unfamiliar, add DS-04 (Pattern Recognition) to identify existing patterns before optimizing.

**Example Prompts:**
- `domain-software-engineering/analysis/performance/performance_code_optimization_suggestions.md`
- `domain-engineering-workflows/improvement/improvement_refactoring.md`

---

### Root Cause Analysis
**User Need:** Understand why something failed, prevent recurrence

**Essential Techniques:**
1. **Chain-of-Thought** (RT-01) — Trace back from symptom to cause
2. **Multi-Dimensional Analysis** (RT-02) — Consider multiple factors
3. **Hierarchical Organization** (ST-05) — Immediate → contributing → root causes
4. **Root Cause Explanation** (RT-09) — Structured root cause documentation

**Enhancement Techniques:**
- **Correlation Analysis** (RT-06) — Find related incidents
- **Cascade Effect Analysis** (RT-07) — Trace the full failure chain
- **Pattern Recognition Reflection** (MP-07) — Identify recurring failure patterns across incidents

**Combination Guidance:**
> **Synergy:** RT-01 traces the causal chain backward from the failure, RT-02 ensures contributing factors from multiple domains are considered (code, infrastructure, process, people), ST-05 organizes causes into immediate → contributing → root levels, and RT-09 documents the fundamental reason.
> **Order:** ST-05 → RT-01 → RT-02 → RT-09 → RT-06
> **Avoid:** Don't combine with DS-06 (Prioritization) during root cause analysis — the goal is understanding, not ranking. Don't pair RT-09 (Root Cause) with QA-02 (Adversarial) — stress-testing is for outputs, not for forensic analysis.
> **Fallback:** If the root cause is unclear, add RT-07 (Cascade Effect Analysis) to trace the full failure propagation chain. If the incident is recurring, add MP-07 (Pattern Recognition Reflection) to identify systemic patterns.

**Example Prompts:**
- `domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md`

---

### Incident Response
**User Need:** Handle production incidents, time-critical issues

**Essential Techniques:**
1. **Time-Critical Response Protocol** (AG-19) — Prioritize speed and structure under pressure
2. **Blocker Escalation Framework** (DS-36) — Define escalation paths and triggers
3. **Root Cause Explanation** (RT-09) — Quickly identify probable root cause
4. **Troubleshooting Decision Tree** (RT-10) — Fast diagnostic flowchart

**Enhancement Techniques:**
- **Fail-Fast Ordering** (DD-03) — Check the most likely causes first
- **BLOCKED Protocol** (DD-11) — Define what to do when progress is blocked

**Combination Guidance:**
> **Synergy:** AG-19 prioritizes speed and structure under pressure, DS-36 defines escalation paths so responders know when to escalate, RT-09 quickly identifies the probable root cause, and RT-10 provides a structured diagnostic flowchart for rapid triage.
> **Order:** AG-19 → RT-10 → RT-09 → DS-36
> **Avoid:** Don't combine with RT-02 (Multi-Dimensional Analysis) — incidents need focused speed, not comprehensive analysis. Don't pair with RP-03 (Multi-Persona Debate) — no time for debate during incidents.
> **Fallback:** If the incident is not responding to standard triage, add DD-03 (Fail-Fast Ordering) to rapidly eliminate common causes. If progress stalls, add DD-11 (BLOCKED Protocol) to define escalation behavior.

**Example Prompts:**
- `domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md`

---

## Quality Assurance & Verification Tasks

### High-Stakes Verification
**User Need:** Critical decisions requiring maximum confidence

**Essential Techniques:**
1. **Chain-of-Verification** (QA-01) — Self-critique and revision
2. **Adversarial Stress-Test** (QA-02) — Attack your own answer
3. **Self-Consistency** (QA-15) — Generate multiple independent solutions
4. **Uncertainty Acknowledgment** (QA-04) — State confidence levels

**Enhancement Techniques:**
- **Multi-Persona Debate** (RP-03) — Different perspectives
- **Temperature Simulation** (RP-05) — Cautious + confident analyses
- **Citation Requirements** (QA-05) — Require sources for claims
- **Ground Truth Principle** (QA-14) — Anchor to verifiable facts
- **False Positives Identification** (QA-12) — Actively identify likely false positives

**Template Pattern:**
```
**Initial Analysis:**
[Provide analysis]

**Verification - Self Critique:**
1. List three ways this analysis could be wrong:
   - [Potential issue 1 with evidence]
   - [Potential issue 2 with evidence]
   - [Potential issue 3 with evidence]

2. Adversarial test:
   - What edge cases would break this?
   - What assumptions am I making?
   - What am I not considering?

**Revised Analysis:**
[Incorporate verified corrections and address concerns]

**Confidence Assessment:**
- High confidence in: [aspects]
- Medium confidence in: [aspects]
- Low confidence / Uncertain: [aspects]
- Requires verification: [what should be validated]
```

**Combination Guidance:**
> **Synergy:** QA-01 catches errors through self-critique, QA-02 attacks the output from adversarial angles, QA-15 generates multiple independent solutions to verify consistency, and QA-04 honestly states what's uncertain rather than hiding gaps.
> **Order:** QA-01 → QA-02 → QA-15 → QA-04
> **Avoid:** Don't combine QA-15 (Self-Consistency) with NE-05 (Token Budget) — generating multiple solutions requires significant tokens. Don't pair QA-02 (Adversarial) with NE-07 (Emotional Validation) — adversarial testing needs bluntness.
> **Fallback:** If verification is still insufficient, add RP-03 (Multi-Persona Debate) for external perspectives. If confidence remains low, add QA-05 (Citation Requirements) to anchor claims in verifiable sources.

---

### Testing & Validation Frameworks
**User Need:** Design testing strategies, evaluate AI outputs systematically

**Essential Techniques:**
1. **Test Battery Protocol** (QA-10) — Define comprehensive test suites
2. **Pass/Fail Test Harness** (QA-11) — Create clear pass/fail criteria
3. **LLM-as-Judge with Rubric** (DS-35) — Rubric-based AI evaluation
4. **Statistical A/B Testing** (QA-07) — Compare variants with statistical rigor

**Enhancement Techniques:**
- **Quality Rubric with Auto-Iteration** (QA-16) — Auto-improve based on rubric scores
- **Named Scores** (QA-17) — Multi-dimensional scoring with named metrics
- **Gate-Based Verification** (QA-08) — Pass/fail gates at each stage
- **Reversibility Assessment** (QA-09) — Assess whether results can be rolled back
- **Failure Recovery Specification** (QA-13) — Define recovery procedures for test failures

**Combination Guidance:**
> **Synergy:** QA-10 defines comprehensive test suites, QA-11 creates clear pass/fail criteria (removing ambiguity), DS-35 enables AI-based evaluation with scoring rubrics, and QA-07 ensures statistical rigor when comparing variants.
> **Order:** QA-10 → QA-11 → DS-35 → QA-07
> **Avoid:** Don't combine QA-07 (A/B Testing) with QA-15 (Self-Consistency) — A/B testing compares external variants, self-consistency compares internal solutions. Different evaluation paradigms. Don't pair DS-35 (LLM-as-Judge) with QA-14 (Ground Truth) for subjective evaluations — ground truth requires objective facts.
> **Fallback:** If tests are too coarse, add QA-16 (Quality Rubric with Auto-Iteration) to auto-improve based on rubric scores. If evaluation dimensions are unclear, add QA-17 (Named Scores) for explicit multi-dimensional scoring.

---

### Prompt Improvement
**User Need:** Make existing prompts better

**Essential Techniques:**
1. **Reverse Prompting** (MP-01) — What would the optimal prompt look like?
2. **Recursive Optimization** (MP-02) — Three-iteration improvement
3. **Strategic Edge Case Calibration** (MP-04) — Add edge case examples
4. **Four-Layer Enhancement Process** (MP-08) — Systematic four-layer improvement

**Enhancement Techniques:**
- **Quality Rubric with Auto-Iteration** (QA-16) — Score and auto-improve
- **Named Scores** (QA-17) — Track improvement across named dimensions
- **Extended Thinking Documentation** (MP-05) — Document the reasoning behind improvements
- **Constitutional AI for Prompts** (QA-06) — Apply constitutional rules to prompt design

**Combination Guidance:**
> **Synergy:** MP-01 works backward from desired output to design the ideal prompt, MP-02 iterates three times for progressive refinement, MP-04 adds edge case robustness, and MP-08 applies four distinct improvement layers (clarity, specificity, robustness, polish).
> **Order:** MP-01 → MP-02 → MP-04 → MP-08
> **Avoid:** Don't combine MP-01 (Reverse Prompting) with MP-02 (Recursive) in the same pass — reverse prompting generates, recursive optimizes. Apply sequentially. Don't pair MP-08 (Four-Layer) with QA-16 (Auto-Iteration) — both define iteration strategies; pick one.
> **Fallback:** If the prompt still underperforms after iteration, try MP-05 (Extended Thinking Documentation) to understand why the AI interprets the prompt differently than intended. If edge cases persist, strengthen MP-04 with explicit good/bad example calibration (NE-04).

**Example Prompts:**
- `domain-prompt-engineering/prompt-improvement/`

---

### Compliance & Regulatory
**User Need:** Ensure outputs meet regulatory requirements, legal compliance

**Essential Techniques:**
1. **Regulatory Enumeration Pattern** (DS-32) — List all applicable regulations
2. **Jurisdiction-Adaptive Output** (DS-33) — Adapt outputs for different jurisdictions
3. **Mandatory Disclaimer Pattern** (OC-10) — Auto-include required disclaimers
4. **External Methodology Compliance** (DS-111) — Ensure compliance with external standards

**Enhancement Techniques:**
- **Citation Requirements** (QA-05) — Cite specific regulations/standards
- **Constraint Specification** (CM-02) — Define regulatory constraints explicitly
- **Authority Boundary Specification** (CM-09) — Define what the AI can and cannot advise on

**Combination Guidance:**
> **Synergy:** DS-32 ensures all applicable regulations are enumerated (none missed), DS-33 adapts output for different jurisdictions, OC-10 auto-includes required disclaimers (preventing accidental omissions), and DS-111 ensures compliance with external standards like CIS or NIST.
> **Order:** DS-32 → DS-33 → CM-02 → DS-111 → OC-10
> **Avoid:** Don't combine with RT-03 (Tree of Thoughts) — compliance has right answers, not multiple equally valid approaches. Don't pair DS-32 with NE-09 (Scope Reduction) — regulatory enumeration must be comprehensive, not narrowed.
> **Fallback:** If regulatory requirements are unclear, add CM-09 (Authority Boundary Specification) to explicitly define what the AI can advise on vs. what requires legal counsel. If output is too dense, add NE-14 (Multi-Audience Targeting) to layer for both compliance officers and general readers.

---

## Task Completion & Done Definition Tasks

### Defining "Done" for Tasks
**User Need:** Translate vague goals into concrete, verifiable completion criteria

**Essential Techniques:**
1. **Vague-to-Concrete Translation** (DD-02) — Convert fuzzy goals into specific criteria
2. **MVP Gates** (DD-04) — Define minimum viable completion criteria
3. **Self-Audit Table** (DD-07) — Create a checklist for self-verification
4. **Fail-Fast Ordering** (DD-03) — Order verification checks so failures surface early

**Enhancement Techniques:**
- **Human Review Flags** (DD-05) — Flag items that require human judgment
- **Iteration Control** (DD-06) — Define maximum iterations and exit conditions
- **Change Log Iteration** (DD-10) — Track what changed in each iteration
- **BLOCKED Protocol** (DD-11) — Define what to do when progress is blocked

**Combination Guidance:**
> **Synergy:** DD-02 converts vague goals into concrete criteria (the essential first step), DD-04 sets the minimum viable bar, DD-07 creates a self-audit checklist, and DD-03 orders verification checks so the cheapest/most-likely-to-fail checks run first.
> **Order:** DD-02 → DD-04 → DD-03 → DD-07
> **Avoid:** Don't combine DD-02 (Vague-to-Concrete) with ST-02 (Sequential Instructions) in the same block — DD-02 is about defining what "done" means, not sequencing work steps. Don't pair DD-04 (MVP Gates) with OC-05 (Min Length) — MVP is about minimum viable quality, not minimum length.
> **Fallback:** If done criteria are still ambiguous, add DD-05 (Human Review Flags) to flag items requiring human judgment. If the task might stall, add DD-11 (BLOCKED Protocol) to define what happens when progress stops.

**Example Prompts:**
- `domain-engineering-workflows/done-definition/done_definition_translator.md`
- `domain-engineering-workflows/done-definition/done_definition_loop_operator.md`

---

### Gate-Based Verification Workflows
**User Need:** Enforce quality gates before progressing through workflow stages

**Essential Techniques:**
1. **Gate-Based Verification** (QA-08) — Define pass/fail gates at each stage
2. **Self-Audit Table** (DD-07) — Create verification checklists
3. **MVP Gates** (DD-04) — Define minimum acceptable quality per gate
4. **Evidence-Based Reasoning** (RT-05) — Require proof of completion

**Enhancement Techniques:**
- **Reversibility Assessment** (QA-09) — Assess rollback options at each gate
- **Iteration Control** (DD-06) — Limit retry attempts per gate
- **BLOCKED Protocol** (DD-11) — Handle blocked states in pipelines

**Combination Guidance:**
> **Synergy:** QA-08 defines pass/fail gates between stages, DD-07 creates verification checklists at each gate, DD-04 sets the minimum quality bar per gate, and RT-05 requires proof of completion (not just assertion).
> **Order:** DD-04 → QA-08 → DD-07 → RT-05
> **Avoid:** Don't combine QA-08 (Gate Verification) with DT-03 (Iterative Refinement) within a single gate — gates are binary (pass/fail), iteration happens between gates. Don't pair with NE-01 (Single-Question) — gates are automated checks, not interactive dialogue.
> **Fallback:** If gates are too rigid, add QA-09 (Reversibility Assessment) to allow rollback at each gate. If tasks frequently block at gates, add DD-06 (Iteration Control) to limit retry attempts and define escalation.

**Example Prompts:**
- `domain-engineering-workflows/done-definition/done_definition_gate_code_refactor.md`
- `domain-engineering-workflows/done-definition/done_definition_gate_competitive_review.md`
- `domain-engineering-workflows/done-definition/done_definition_gate_incident_postmortem.md`

---

## Agentic Resource Development Tasks

### Building AI Agent Personas
**User Need:** Create effective agent personalities with consistent behavior

**Essential Techniques:**
1. **Personality-First Role Definition** (AG-01) — Define personality traits before tasks
2. **Behavioral Guardrails** (AG-04) — Set explicit behavioral boundaries
3. **Emotional Context Spectrum** (AG-10) — Define how agent responds across emotional contexts
4. **Skeptical Default Stance** (AG-02) — Build in healthy skepticism by default

**Enhancement Techniques:**
- **Behavioral Trait Declarations** (ST-16) — Declare specific behavioral traits
- **Layered Mission Hierarchy** (AG-03) — Priority-ordered mission layers
- **AI-Augmented Expertise** (AG-26) — Define expertise that incorporates AI capabilities
- **Methodology-Centric Expertise** (ST-45) — Define expertise through methodology, not just knowledge

**Combination Guidance:**
> **Synergy:** AG-01 defines personality before tasks (creating consistency), AG-04 sets behavioral boundaries (preventing drift), AG-10 defines emotional range, and AG-02 builds in healthy skepticism that prevents the agent from being too agreeable.
> **Order:** AG-01 → AG-02 → AG-04 → AG-10
> **Avoid:** Don't combine AG-01 (Personality-First) with RP-01 (Expert Role) — AG-01 already subsumes role assignment with richer persona modeling. Don't pair AG-10 (Emotional Spectrum) with strict technical agents — not all agents need emotional awareness.
> **Fallback:** If the persona feels flat, add ST-16 (Behavioral Trait Declarations) for specific behavioral details. If the persona drifts during use, strengthen AG-04 (Behavioral Guardrails) with explicit "NEVER" constraints.

**Example Prompts:**
- `domain-agentic-resources/personas/`
- `authoring/agent-patterns/AGENT_QUICK_START.md`

---

### Building Agent Skills
**User Need:** Create reusable, modular AI capabilities

**Essential Techniques:**
1. **Concrete Deliverable Templates** (AG-05) — Define exact output formats
2. **Layered Mission Hierarchy** (AG-03) — Priority-ordered objectives
3. **Anti-Pattern & Failure Mode Embedding** (AG-09) — Document what NOT to do
4. **Meta-Skill Self-Reference** (AG-18) — Skills that can reference their own patterns

**Enhancement Techniques:**
- **Taxonomy-Based Classification** (AG-11) — Classify skill inputs/outputs
- **Quantitative Success Metrics** (AG-12) — Define measurable success criteria
- **Meta-Skill Pattern (Discovery)** (AG-20) — Skills that discover other skills
- **Workflow Position Definition** (AG-31) — Define where the skill fits in a larger workflow
- **Research-First Behavior** (AG-30) — Ensure research before action
- **Minimal Agent Pattern** (ST-37) — Keep skills focused and minimal

**Combination Guidance:**
> **Synergy:** AG-05 defines exact output formats (making skills composable), AG-03 prioritizes objectives so the skill knows what matters most, AG-09 embeds anti-patterns (preventing common failures), and AG-18 enables meta-skills that reference their own patterns.
> **Order:** AG-03 → AG-05 → AG-09 → AG-18
> **Avoid:** Don't combine AG-18 (Meta-Skill) with AG-20 (Meta-Skill Discovery) in the same skill — one creates skills, the other discovers them. Separate concerns. Don't pair AG-12 (Quantitative Metrics) with AG-05 (Templates) unless metrics map directly to template fields.
> **Fallback:** If the skill is too rigid, add AG-11 (Taxonomy-Based Classification) to handle different input types. If the skill's workflow position is unclear, add AG-31 (Workflow Position Definition) to specify where it fits in larger pipelines.

**Example Prompts:**
- `authoring/skill-patterns/SKILL_PATTERN_INDEX.md`
- `domain-agentic-resources/skills/`

---

### Building Multi-Agent Pipelines
**User Need:** Orchestrate multiple agents working together

**Essential Techniques:**
1. **Pipeline Orchestration Patterns** (AG-07) — Define pipeline stages and handoffs
2. **Evidence-Based Decision Gates** (AG-08) — Gates between pipeline stages
3. **Parallel-Converge Orchestration** (AG-13) — Run agents in parallel, then merge results
4. **Cost-Aware Agent Orchestration** (AG-14) — Optimize for cost vs quality tradeoffs

**Enhancement Techniques:**
- **Staged Rollout with Automatic Rollback** (AG-15) — Progressive deployment with safety
- **Orchestration with Dual-Path Output** (AG-21) — Support multiple output paths
- **Memory & Learning Architecture** (AG-06) — Cross-session state management
- **File-Based State Persistence** (CM-08) — Persist state between agent sessions
- **Memory Scaffold Architecture** (CM-10) — Structured memory across agents

**Combination Guidance:**
> **Synergy:** AG-07 defines pipeline stages and handoffs, AG-08 gates decisions between stages (preventing error propagation), AG-13 runs independent agents in parallel then merges results, and AG-14 optimizes the cost/quality tradeoff across the pipeline.
> **Order:** AG-07 → AG-14 → AG-13 → AG-08
> **Avoid:** Don't combine AG-13 (Parallel-Converge) with AG-15 (Staged Rollout) — parallel convergence processes all at once, staged rollout is sequential. Choose based on whether tasks are independent (parallel) or dependent (staged). Don't pair AG-14 (Cost-Aware) with QA-15 (Self-Consistency) — multiple solutions per agent multiplies cost.
> **Fallback:** If pipeline coordination is failing, add CM-08 (File-Based State) for reliable inter-agent state sharing. If agents are diverging, add CM-10 (Memory Scaffold) for structured cross-agent memory.

---

### Autonomous Agent Execution
**User Need:** Set up agents for autonomous multi-step execution

**Essential Techniques:**
1. **Master Prompt for Autonomous Multi-Week Execution** (AG-16) — Long-running autonomous agents
2. **Auto-Resume from Stateful Tracking** (AG-17) — Resume after interruption
3. **Layered Mission Hierarchy** (AG-03) — Keep agent aligned to objectives
4. **Behavioral Guardrails** (AG-04) — Prevent drift during autonomous execution

**Enhancement Techniques:**
- **Capability Boundary Specification** (OC-09) — Define what agent can/cannot do
- **Authority Boundary Specification** (CM-09) — Define agent's authority limits
- **Token-Budget-Aware Progressive Loading** (CM-07) — Manage context window across long executions
- **Progressive Context Accumulation** (CM-05) — Build context progressively

**Combination Guidance:**
> **Synergy:** AG-16 provides the master prompt for long-running execution, AG-17 enables recovery from interruptions, AG-03 keeps the agent aligned to objectives across sessions, and AG-04 prevents behavioral drift during extended autonomous operation.
> **Order:** AG-03 → AG-04 → AG-16 → AG-17
> **Avoid:** Don't combine AG-16 (Master Prompt) with NE-01 (Single-Question) — autonomous agents don't interact per-question; they execute independently. Don't pair CM-05 (Progressive Accumulation) with CM-07 (Token-Budget Loading) — choose one context strategy based on whether you prioritize completeness (CM-05) or efficiency (CM-07).
> **Fallback:** If the agent loses track of progress, strengthen AG-17 (Auto-Resume) with explicit checkpointing. If context window fills up, add CM-07 (Token-Budget Loading) for intelligent context prioritization.

---

### Agent Task Delegation
**User Need:** Delegate a task to an AI coding agent with appropriate oversight and verification

**Essential Techniques:**
1. **End-State Task Specification** (AG-27) — Frame tasks as desired outcomes with verification commands, not implementation steps
2. **Oversight-Risk Calibration** (AG-28) — Match supervision intensity to task risk, stakes, and context (4 levels)
3. **Feedback Signal Inventory** (AG-33) — Catalog available feedback mechanisms (tests, linters, type checkers) to determine safe autonomy level

**Enhancement Techniques:**
- **Agent Loop Architecture** (AG-29) — For complex/multi-iteration tasks, design the full iteration loop with exit conditions, checkpoints, and stuck detection
- **Pre-Execution Risk Audit** (AG-32) — Pre-flight footgun scan: vague criteria, missing design, scope creep, abstraction bloat, no checkpoints, wrong tool
- **Gate-Based Verification** (QA-08) — Binary pass/fail gates for task completion
- **File-Based State Persistence** (CM-08) — Git commits and structured files as memory between loop iterations

**Combination Guidance:**
> **Synergy:** AG-27 defines what "done" looks like, AG-33 determines what feedback is available, AG-28 uses both to calibrate oversight level. For complex tasks, AG-29 designs the iteration loop and AG-32 audits the whole plan before execution.
> **Order:** AG-33 → AG-27 → AG-28 → AG-32 → AG-29
> **Avoid:** Don't skip AG-33 (Feedback Signal Inventory) before AG-28 (Oversight Calibration) — you can't calibrate oversight without knowing what feedback mechanisms exist. Don't use AG-29 (Loop Architecture) for simple one-shot tasks — it adds unnecessary complexity.
> **Fallback:** If agent gets stuck in a loop, review AG-33 — weak feedback signals (no tests) may mean the task needs closer human oversight (raise AG-28 level). If agent produces wrong output, run AG-32 audit — the task specification may have footgun patterns.

**Use Prompts:**
- `domain-engineering-workflows/ai-patterns/workflow_agent_task_specification.md` — Convert task to agent-ready spec
- `domain-engineering-workflows/ai-patterns/workflow_agent_oversight_calibration.md` — Determine supervision level
- `domain-engineering-workflows/ai-patterns/workflow_agent_loop_designer.md` — Design iteration loop
- `domain-engineering-workflows/ai-patterns/workflow_agent_footgun_detector.md` — Pre-flight risk audit
- `domain-engineering-workflows/ai-patterns/workflow_agent_jargon_translator.md` — Decode agentic terminology

---

### Auto-Improvement Readiness Diagnostic
**User Need:** Determine whether a system is actually ready for an automated optimization loop (e.g., a Karpathy-style meta-agent) before launching one

**Essential Techniques:**
1. **Optimization Triplet Readiness Gating** (AG-34) — Force concrete answers across editable surface, optimization metric, and experiment time budget; refuse to advance until each gate passes
2. **Auto-Improvement Readiness Requirements Matrix** (DS-43) — Apply the 10-row checklist (reasoning traces, tool call granularity, decision-point visibility, structured format, session reproducibility, baseline snapshots, failure classification, cost/latency tracking, sandboxed execution, eval harness)
3. **Phased Workflow Architecture** (NE-02) — Run the diagnostic as gated phases (system selection → editable surface → metric → time budget → verdict)
4. **Constraint Specification** (CM-02) — Bound what counts as a passing answer at each gate; reject vague responses

**Enhancement Techniques:**
- **Gate-Based Verification** (QA-08) — Binary pass/fail on each readiness gate
- **Feedback Signal Inventory** (AG-33) — Pre-step: catalog feedback signals before running the readiness gates

**Combination Guidance:**
> **Synergy:** AG-34 supplies the gate structure, DS-43 supplies the rubric inside each gate, NE-02 keeps the diagnostic from collapsing into a single dump, and CM-02 prevents acceptance of vague answers. The output is either a `program.md` optimization spec or a Blocker Report.
> **Order:** NE-02 → AG-34 → DS-43 → CM-02 → QA-08
> **Avoid:** Don't run AG-34 (Triplet Gating) before AG-33 (Feedback Signal Inventory) — you can't gate on metric quality without first knowing what feedback signals exist. Don't soften the gates with QA-04 (Uncertainty Acknowledgment) — readiness is binary.
> **Fallback:** If too many gates fail, fall back to the Trace Infrastructure Audit (below) to scope the foundational work needed before retrying.

**Use Prompts:**
- `domain-engineering-workflows/ai-patterns/workflow_agent_karpathy_triplet_diagnostic.md` — Run the gated triplet diagnostic

---

### Metric Gaming Pre-Mortem (Adversarial Metric Design)
**User Need:** Stress-test an optimization metric, KPI, incentive, or reward system *before* it's deployed — surface how it will be gamed and design the countermeasures

**Essential Techniques:**
1. **Metric Gaming Vector Enumeration** (QA-21) — Generate concrete gaming scenarios across five categories: Direct Gaming, Proxy Divergence, Eval Contamination, Silent Degradation, Compounding Cascades
2. **Evaluation Diversity Planning** (QA-22) — For each gaming vector, design a secondary metric, holdout scenario, or human-review cadence that catches it
3. **Cascade Effect Analysis** (RT-07) — Trace how a locally optimal change creates problems in connected systems
4. **Metric Specification** (DS-02) — Specify the primary metric and each countermeasure metric concretely (computation, threshold, owner)

**Enhancement Techniques:**
- **Feedback Signal Inventory** (AG-33) — Inventory what signals exist to detect gaming early
- **Single-Question Pacing** (NE-01) — When run conversationally (e.g., parenting reward systems), gather inputs one question at a time
- **Phased Workflow Architecture** (NE-02) — Phase the pre-mortem (target → gaming vectors → defenses → verdict)

**Combination Guidance:**
> **Synergy:** QA-21 surfaces the failure modes, QA-22 turns each into an actionable countermeasure, RT-07 covers system-level cascades that single-vector analysis misses, and DS-02 keeps every proposed metric concrete enough to implement. Works equally for engineering (auto-improvement loops), business (compensation plans, OKRs), or personal/parenting (sticker charts, allowances) systems.
> **Order:** DS-02 → QA-21 → RT-07 → QA-22
> **Avoid:** Don't pair QA-21 with generic "an agent might overfit" warnings — every vector must be specific to the user's system. Don't claim a metric is "ungameable" — every metric has cracks.
> **Fallback:** If the metric is fundamentally activity-based rather than outcome-based, escalate to a "rethink the metric" verdict rather than papering over it with countermeasures.

**Use Prompts:**
- `domain-engineering-workflows/ai-patterns/workflow_agent_metric_gaming_premortem.md` — Engineering / agent-loop variant
- `domain-parenting/parenting_reward_system_premortem.md` — Parenting / behavior-contract variant

---

### Trace Infrastructure & Observability Audit
**User Need:** Audit whether current agent logging/tracing/observability is sufficient to support targeted meta-agent optimization (vs. blind mutation), and produce a prioritized remediation plan

**Essential Techniques:**
1. **Trace Infrastructure Gap Audit** (AG-35) — Walk requirement-by-requirement through current state, score each Present/Partial/Absent
2. **Build-vs-Buy Observability Remediation** (AG-36) — For every gap, name the cheapest fix, the build-vs-buy recommendation, and an effort estimate (don't end at "you have problems")
3. **Auto-Improvement Readiness Requirements Matrix** (DS-43) — The 10-row rubric AG-35 scores against
4. **Conditional Output Logic** (OC-04) — Branch the verdict between "Ready" / "Buildable in [timeframe]" / "Foundational work needed"

**Enhancement Techniques:**
- **Gate-Based Verification** (QA-08) — Treat each requirement as a binary gate before declaring readiness
- **Feedback Signal Inventory** (AG-33) — Pair with AG-35 when scoring the eval-harness and feedback-signal rows

**Combination Guidance:**
> **Synergy:** DS-43 is the rubric, AG-35 is the exam, AG-36 turns the exam into an action plan, and OC-04 forces a single decisive verdict instead of an open-ended punch list. The pattern (rubric → audit → remediation → verdict) generalizes beyond observability to any capability-readiness audit.
> **Order:** DS-43 → AG-35 → AG-36 → OC-04
> **Avoid:** Don't recommend "build a full auto-improvement loop" inside this audit — its job is infrastructure readiness only. Don't inflate Partial → Present to soften the verdict.
> **Fallback:** If multiple critical rows are Absent, deliver "Foundational work needed" and surface the single highest-leverage gap to close first ("The One Thing To Do This Week").

**Use Prompts:**
- `domain-engineering-workflows/ai-patterns/workflow_agent_trace_infrastructure_audit.md` — Run the trace/observability gap audit

---

## Non-Engineering & Conversational Tasks

### Conversational Prompt Design
**User Need:** Build prompts for interactive, dialogue-based use cases (coaching, interviews, intake)

**Essential Techniques:**
1. **Single-Question Pacing** (NE-01) — Ask one question at a time, wait for response
2. **Phased Workflow Architecture** (NE-02) — Structure conversation into clear phases
3. **Emotional Validation First** (NE-07) — Acknowledge emotions before problem-solving
4. **Catchall Context Gathering** (NE-08) — Open-ended "anything else?" prompts

**Enhancement Techniques:**
- **Input Template Scaffolding** (NE-03) — Provide structured input formats for users
- **Good vs Bad Example Calibration** (NE-04) — Show what good vs bad responses look like
- **Cognitive Mode Framing** (NE-12) — Set the mental model (analytical, creative, empathetic)
- **Non-Judgmental Comparison** (NE-16) — Present options without bias
- **Fallback Question Protocol** (MP-06) — Define fallback when user response is unclear

**Combination Guidance:**
> **Synergy:** NE-01 prevents overwhelming the user with multiple questions at once, NE-02 structures the conversation into clear phases (intake → exploration → synthesis), NE-07 builds trust by acknowledging emotions before diving into problem-solving, and NE-08 catches information the structured questions might have missed.
> **Order:** NE-02 → NE-07 → NE-01 → NE-08
> **Avoid:** Don't combine NE-01 (Single-Question) with ST-02 (Sequential Instructions) — single-question pacing is for interactive dialogue, sequential instructions are for single-shot prompts. Don't pair NE-07 (Emotional Validation) with QA-02 (Adversarial) — empathy and attack-testing serve opposite purposes.
> **Fallback:** If the conversation loses focus, add NE-12 (Cognitive Mode Framing) to set the mental model explicitly. If users give vague responses, add NE-03 (Input Template Scaffolding) to provide structured input formats.

**Example Prompts:**
- `domain-healthcare-clinical/prompts/`
- `domain-healthcare-clinical/prompts/medicine_behavioral_health_coordination_micro_guide.md`
- `domain-healthcare-clinical/prompts/medicine_clinical_visual_education_micro_guide.md`
- `domain-personal-development/prompts/`

---

### Business Communication & Translation
**User Need:** Translate technical findings into business language, write stakeholder updates

**Essential Techniques:**
1. **Technical-to-Business Translation** (NE-13) — Convert technical details to business impact
2. **Audience-Specific Framing** (RP-02) — Match language to audience
3. **Data Storytelling Framework** (NE-15) — Structure narrative around data
4. **Call-to-Action Mandatory Close** (NE-17) — End with specific asks

**Enhancement Techniques:**
- **Token Budget Control** (NE-05) — Control output length for busy executives
- **Multi-Audience Documentation Targeting** (NE-14) — Write for multiple audiences at once
- **Third-Party Handoff Package** (NE-20) — Create self-contained packages for handoff
- **Consumable Artifact Requirement** (DP-21) — Ensure output is understandable in 60 seconds

**Combination Guidance:**
> **Synergy:** NE-13 translates technical details into business impact (bridging the communication gap), RP-02 ensures language matches the audience level, NE-15 weaves data into a compelling narrative, and NE-17 forces a clear call-to-action at the end.
> **Order:** RP-02 → NE-13 → NE-15 → NE-17
> **Avoid:** Don't combine NE-13 (Tech-to-Business Translation) with DS-02 (Metric Specification) in the output — business audiences need impact, not raw metrics. Don't pair NE-05 (Token Budget) with NE-15 (Data Storytelling) — stories need room to develop.
> **Fallback:** If the communication is too long for the audience, add NE-05 (Token Budget) to control length. If it serves multiple audiences, add NE-14 (Multi-Audience Documentation Targeting) to layer for different reader needs.

**Example Prompts:**
- `domain-professional-communication/prompts/`

---

### Decision Support
**User Need:** Structure complex decisions with quantitative analysis

**Essential Techniques:**
1. **Scope Reduction Pressure** (NE-09) — Force focus on the ONE most important factor
2. **Probability-Weighted Scenarios** (NE-10) — Weight outcomes by likelihood
3. **Embedded Calculation Formulas** (NE-11) — Include formulas for quantitative analysis
4. **Self-Audit Requirements** (NE-06) — Require self-check of reasoning

**Enhancement Techniques:**
- **Framework Application** (DS-01) — Use established decision frameworks
- **Non-Judgmental Comparison** (NE-16) — Present options without bias
- **Uncertainty Acknowledgment** (QA-04) — State confidence levels honestly

**Combination Guidance:**
> **Synergy:** NE-09 forces focus on the single most important factor (cutting through complexity), NE-10 weights outcomes by probability (preventing worst-case-only thinking), NE-11 includes calculation formulas for quantitative rigor, and NE-06 requires the AI to self-check its own reasoning.
> **Order:** NE-09 → NE-10 → NE-11 → NE-06
> **Avoid:** Don't combine NE-09 (Scope Reduction) with RT-02 (Multi-Dimensional Analysis) early in the process — scope reduction narrows, multi-dimensional expands. Use RT-02 first if you need breadth, then NE-09 to narrow. Don't pair NE-11 (Calculation Formulas) with NE-07 (Emotional Validation) — quantitative decisions need objectivity.
> **Fallback:** If the decision still feels unclear, add DS-01 (Framework Application) to apply a structured decision framework. If bias is a concern, add NE-16 (Non-Judgmental Comparison) to present options without leading.

**Example Prompts:**
- `domain-decision-making/`

---

### Developer-Facing Content
**User Need:** Create content optimized for developer experience (tutorials, READMEs, SDKs)

**Essential Techniques:**
1. **Developer Experience Priority** (NE-18) — Optimize for developer workflow and productivity
2. **Progressive Example Complexity** (IT-20) — Start simple, build up
3. **Use Case-Driven Documentation** (IT-21) — Organize by what developers need to do
4. **Documentation-as-Product Philosophy** (NE-19) — Treat docs as a product

**Enhancement Techniques:**
- **API Reference Bundling** (DS-24) — Bundle API docs with examples
- **External Reference Catalog** (OC-12) — Link to authoritative external resources

**Combination Guidance:**
> **Synergy:** NE-18 optimizes for developer workflow and productivity, IT-20 builds from simple to complex examples (matching how developers learn), IT-21 organizes by what developers need to do (not API surface area), and NE-19 treats documentation as a product with quality standards.
> **Order:** NE-19 → NE-18 → IT-21 → IT-20
> **Avoid:** Don't combine NE-18 (Developer Experience) with NE-13 (Tech-to-Business Translation) — developer-facing content should stay technical. Don't pair IT-20 (Progressive Examples) with NE-05 (Token Budget) — examples need space to be useful.
> **Fallback:** If documentation lacks discoverability, add OC-12 (External Reference Catalog) for authoritative links. If the API surface is too large, add DS-24 (API Reference Bundling) to organize by functional groups.

---

## Visual Output & Image Generation Tasks

### Data Visualization & Dashboards
**User Need:** Create executive dashboards, data visualizations, chart specifications

**Essential Techniques:**
1. **Visual Output Specification** (SV-01) — Define visual layout requirements precisely
2. **Chart Selection Dictionary** (DS-25) — Choose the right visualization type
3. **Calculation Specification** (SV-07) — Embed calculation logic into visual layout
4. **Table Output Specification** (SV-10) — Structure tabular data presentation

**Enhancement Techniques:**
- **Grouped Input Gathering** (SV-02) — Collect visualization requirements in structured groups
- **Confirmation-Before-Proceed** (SV-06) — Confirm requirements before generating
- **Structured Deliverables with Headings** (SV-09) — Clear section structure in output

**Combination Guidance:**
> **Synergy:** SV-01 defines the visual layout precisely, DS-25 ensures the right chart type for each data point, SV-07 embeds calculation logic directly into the layout, and SV-10 structures tabular data cleanly.
> **Order:** SV-01 → DS-25 → SV-07 → SV-10
> **Avoid:** Don't combine SV-01 (Visual Spec) with ST-03 (Output Format) — SV-01 already defines the output format for visual content. Don't pair SV-07 (Calculation Spec) with NE-11 (Embedded Formulas) — they overlap; use SV-07 for visual contexts, NE-11 for text-based contexts.
> **Fallback:** If the visualization requirements are unclear, add SV-02 (Grouped Input Gathering) to collect requirements in structured groups. If the client needs to approve before generation, add SV-06 (Confirmation-Before-Proceed).

**Example Prompts:**
- `domain-image-generation/visualizations/`
- `domain-presentations/`

---

### Printable Worksheets & Materials
**User Need:** Create educational worksheets, printable cards, reference materials

**Essential Techniques:**
1. **Printable Worksheet Output Format** (SV-05) — Optimize for print layout
2. **Visual Output Specification** (SV-01) — Define physical dimensions and layout
3. **Audience-Specific Framing** (RP-02) — Match content to grade level / audience

**Enhancement Techniques:**
- **Typography Decision Tree** (DT-06) — Choose appropriate fonts and sizing
- **Calculation Specification** (SV-07) — Include calculation-based content

**Combination Guidance:**
> **Synergy:** SV-05 optimizes for print layout (margins, bleed, fold lines), SV-01 defines physical dimensions and zones, and RP-02 matches content complexity to the audience (e.g., grade level for educational worksheets).
> **Order:** RP-02 → SV-01 → SV-05
> **Avoid:** Don't combine SV-05 (Printable Format) with OC-02 (JSON Schema) — printable output is visual, not machine-readable. Don't pair with NE-01 (Single-Question) — worksheet generation is typically a single-shot task, not interactive.
> **Fallback:** If the worksheet layout is too dense, add DT-06 (Typography Decision Tree) to optimize font sizing and spacing. If content needs calculations, add SV-07 (Calculation Specification).

**Example Prompts:**
- `domain-image-generation/worksheet-generators/`
- `domain-education-teaching/`

---

### AI Image Generation (Print Materials)
**User Need:** Generate print-ready images with AI image models (badge buddies, reference cards, posters)

**Essential Techniques:**
1. **Terminology Steering** (SV-11) — Use print terminology ("flat print artwork") to avoid UI mockup behaviors
2. **Grid Forcing + Enumerated Slots** (SV-12) — Exact NxM grid with numbered content slots
3. **Constraint Redundancy** (SV-13) — Repeat critical constraints at 3+ levels (policy, implementation, validation)
4. **Deliverables Locking** (SV-17) — Lock exact count, orientation, dimensions, resolution
5. **Image Validation Checklist** (SV-18) — Final self-audit block with "if X appears, output is incorrect" language

**Enhancement Techniques:**
- **Negative Space Control** (SV-14) — Ban backgrounds, shadows, depth effects
- **Physical Context Anchoring** (SV-16) — Anchor to real-world usage (who holds it, how it's viewed)
- **Allowed vs. Forbidden Distinction** (SV-15) — Distinguish structured layouts from UI chrome

**Full Guide:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md`

**Combination Guidance:**
> **Synergy:** SV-11 steers terminology away from UI mockup behaviors, SV-12 forces exact grid layouts with numbered slots, SV-13 repeats critical constraints at 3+ levels (policy, implementation, validation) to overcome model tendencies, SV-17 locks exact deliverable specifications, and SV-18 provides a final self-audit to catch constraint violations.
> **Order:** SV-11 → SV-17 → SV-12 → SV-13 → SV-14 → SV-18
> **Avoid:** Don't combine SV-12 (Grid Forcing) with SV-01 (Visual Output Spec) for simple image generation — SV-12 is specifically for AI image models (DALL-E, Midjourney), while SV-01 is for text-based visual specifications. Don't pair SV-13 (Constraint Redundancy) with NE-05 (Token Budget) — constraint redundancy intentionally repeats content.
> **Fallback:** If the AI model still produces UI mockups, strengthen SV-11 (Terminology Steering) with more print-specific language. If the grid layout is wrong, add SV-16 (Physical Context Anchoring) to ground the image in real-world usage context.

**Example Prompts:**
- `domain-image-generation/worksheet-generators/`
- `domain-image-generation/branding/`

---

### AI Image Generation (Infographics & Visualizations)
**User Need:** Generate data-rich infographics, dashboards, or workflow diagrams with AI image models

**Essential Techniques:**
1. **Visual Output Specification** (SV-01) — Define zones, proportions, and layout structure
2. **Terminology Steering** (SV-11) — Avoid UI/mockup associations
3. **Constraint Redundancy** (SV-13) — Enforce style rules at multiple levels
4. **Allowed vs. Forbidden Distinction** (SV-15) — Allow structured tables, forbid spreadsheet UI
5. **Image Validation Checklist** (SV-18) — End with constraint verification

**Enhancement Techniques:**
- **Calculation Specification** (SV-07) — Embed formulas for data-driven visuals
- **Negative Space Control** (SV-14) — Control backgrounds and surrounding space
- **Deliverables Locking** (SV-17) — Lock dimensions and resolution for print

**Full Guide:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md`

**Combination Guidance:**
> **Synergy:** SV-01 defines zones and proportions, SV-11 avoids UI/mockup associations, SV-13 enforces style rules at multiple levels, SV-15 distinguishes structured data tables from spreadsheet UI chrome, and SV-18 verifies all constraints are met.
> **Order:** SV-11 → SV-01 → SV-13 → SV-15 → SV-18
> **Avoid:** Don't combine SV-15 (Allowed/Forbidden) with OC-04 (Conditional Output) — Allowed/Forbidden is about visual element classification, Conditional Output is about logic branching. Don't pair SV-14 (Negative Space) with SV-16 (Physical Context) unless the image needs both — they can conflict when background control clashes with real-world context.
> **Fallback:** If the infographic is too cluttered, strengthen SV-14 (Negative Space Control) to enforce whitespace. If data presentation is unclear, add SV-07 (Calculation Specification) to embed formulas for data-driven elements.

**Example Prompts:**
- `domain-image-generation/visualizations/`
- `domain-image-generation/healthcare/`
- `domain-image-generation/healthcare/pacu_infographic_image_prompt.md`

---

### Interview-Driven Content Generation
**User Need:** Gather information through structured interview, then synthesize into output

**Essential Techniques:**
1. **Interview-to-Synthesis Pattern** (SV-03) — Structured interview followed by synthesis
2. **Tiered Discovery Questions** (SV-08) — Layer questions by depth (basic → advanced)
3. **Grouped Input Gathering** (SV-02) — Collect inputs in structured groups
4. **Confirmation-Before-Proceed** (SV-06) — Confirm gathered information before proceeding

**Enhancement Techniques:**
- **Single-Question Pacing** (NE-01) — One question at a time
- **Catchall Context Gathering** (NE-08) — Open-ended "anything else?" at the end

**Combination Guidance:**
> **Synergy:** SV-03 structures the two-phase process (interview then synthesis), SV-08 layers questions by depth so basic info is gathered first, SV-02 collects inputs in organized groups (preventing scattered information), and SV-06 confirms gathered information before proceeding to synthesis.
> **Order:** SV-08 → SV-02 → NE-01 → SV-06 → SV-03
> **Avoid:** Don't combine SV-03 (Interview-to-Synthesis) with ST-02 (Sequential Instructions) for the interview phase — interviews need to adapt to responses, not follow rigid sequences. Don't pair SV-08 (Tiered Questions) with NE-09 (Scope Reduction) early — gather broadly first, then narrow.
> **Fallback:** If the interview produces incomplete information, add NE-08 (Catchall Context Gathering) for an open-ended "anything else?" at the end. If synthesis quality is poor, add NE-15 (Data Storytelling) to structure the output as a narrative.

**Example Prompts:**
- `domain-advertising/` (uses interview-to-synthesis pattern extensively)

---

## Documentation & Interaction Design Tasks

### API & Library Documentation
**User Need:** Create reference documentation for APIs, libraries, or SDKs

**Essential Techniques:**
1. **Progressive Example Complexity** (IT-20) — Start with simple examples, add complexity
2. **Use Case-Driven Documentation** (IT-21) — Organize by use case, not by API surface
3. **External Reference Catalog** (OC-12) — Link to external authoritative resources
4. **API Reference Bundling** (DS-24) — Bundle API reference with usage examples

**Enhancement Techniques:**
- **Three-Tier Information Loading** (IT-19) — Load info in summary → detail → deep-dive tiers
- **Multi-Template Selection Guide** (IT-27) — Provide templates for common documentation needs
- **Reference Catalog Pattern** (IT-26) — Structured reference catalog format

**Combination Guidance:**
> **Synergy:** IT-20 builds understanding from simple to complex examples, IT-21 organizes by developer tasks (not API surface area), OC-12 links to authoritative external resources, and DS-24 bundles API reference with usage examples for self-contained docs.
> **Order:** IT-21 → IT-20 → DS-24 → OC-12
> **Avoid:** Don't combine IT-20 (Progressive Examples) with OC-05 (Min Length) — examples should be as long as needed to be clear, not padded. Don't pair IT-21 (Use Case-Driven) with DT-02 (Specific Focus Areas) — use case-driven is already focused.
> **Fallback:** If docs lack depth at any level, add IT-19 (Three-Tier Information Loading) for summary → detail → deep-dive layers. If the API has multiple template needs, add IT-27 (Multi-Template Selection Guide).

---

### Troubleshooting Documentation
**User Need:** Create troubleshooting guides, runbooks, diagnostic procedures

**Essential Techniques:**
1. **Symptom-Based Troubleshooting** (IT-23) — Organize by symptoms, not root causes
2. **Troubleshooting Decision Tree** (RT-10) — Structured diagnostic flowcharts
3. **Root Cause Explanation** (RT-09) — Explain the "why" clearly
4. **Error Recovery Patterns** (RT-11) — Template recovery procedures for common errors

**Enhancement Techniques:**
- **Workflow Decision Matrix** (IT-22) — Decision matrix for choosing diagnostic paths
- **Tool Hierarchy Guidance** (IT-25) — Recommend tools by preference order

**Combination Guidance:**
> **Synergy:** IT-23 organizes by observable symptoms (how users actually experience problems), RT-10 provides structured diagnostic flowcharts, RT-09 explains the fundamental "why" behind each issue, and RT-11 provides template recovery procedures for common errors.
> **Order:** IT-23 → RT-10 → RT-09 → RT-11
> **Avoid:** Don't combine IT-23 (Symptom-Based) with DT-02 (Specific Focus Areas) — symptom-based organization is already focused; adding explicit focus areas creates conflicting organizational schemes. Don't pair RT-10 (Decision Tree) with NE-01 (Single-Question) — decision trees are reference docs, not interactive.
> **Fallback:** If the troubleshooting guide is too long, add IT-22 (Workflow Decision Matrix) to help users quickly find the right diagnostic path. If tool recommendations are needed, add IT-25 (Tool Hierarchy Guidance).

---

### Multi-Audience & Handoff Documentation
**User Need:** Create documentation that serves multiple audiences, or package for handoff

**Essential Techniques:**
1. **Multi-Audience Documentation Targeting** (NE-14) — Write for multiple reader types
2. **Third-Party Handoff Package** (NE-20) — Self-contained handoff bundles
3. **Progressive Abstraction Transformation** (DS-37) — Layer from executive summary to implementation detail
4. **Long-Form Documentation Process** (DS-38) — Structure long document creation

**Enhancement Techniques:**
- **Three-Tier Information Loading** (IT-19) — Summary → detail → deep-dive
- **Domain Theory Grounding** (DS-23) — Anchor in established domain theory

**Combination Guidance:**
> **Synergy:** NE-14 handles different reader types in one document, NE-20 creates self-contained packages (no external dependencies needed to understand), DS-37 layers from executive summary to implementation detail, and DS-38 structures the creation of long documents.
> **Order:** NE-14 → DS-37 → DS-38 → NE-20
> **Avoid:** Don't combine NE-14 (Multi-Audience) with RP-02 (Audience-Specific) — NE-14 handles multiple audiences natively; RP-02 is for a single audience. Don't pair DS-38 (Long-Form) with NE-05 (Token Budget) — long documents need length.
> **Fallback:** If the document is too dense at any level, add IT-19 (Three-Tier Information Loading) for explicit layering. If domain terminology needs grounding, add DS-23 (Domain Theory Grounding).

---

## Infrastructure & Domain-Specific Tasks

### Cloud & Infrastructure Configuration
**User Need:** Design cloud architecture, generate infrastructure-as-code, optimize costs

**Essential Techniques:**
1. **Safe Defaults Pattern** (DS-26) — Production-safe defaults
2. **Environment-Specific Guidance** (DS-28) — Dev/staging/production differentiation
3. **FinOps Architecture Integration** (DS-133) — Cost-aware infrastructure design
4. **Ecosystem Mapping** (DS-30) — Map service dependencies

**Enhancement Techniques:**
- **Professional Defaults Library** (DS-27) — Industry-standard configurations
- **Configuration-Driven Workflow Customization** (DS-39) — Parameterize via config files
- **Regulatory Enumeration Pattern** (DS-32) — List compliance requirements

**Combination Guidance:**
> **Synergy:** DS-26 ensures secure defaults from the start, DS-28 differentiates environments (so dev configs don't reach production), DS-133 embeds cost awareness into architectural decisions, and DS-30 maps service dependencies for holistic understanding.
> **Order:** DS-30 → DS-26 → DS-28 → DS-133
> **Avoid:** Don't combine DS-133 (FinOps) with DS-26 (Safe Defaults) if they conflict — safety should take priority over cost optimization. Don't pair DS-28 (Environment-Specific) with DS-39 (Config-Driven Customization) unless configs are actually parameterized.
> **Fallback:** If infrastructure is too complex for one pass, add DT-01 (Hierarchical Breakdown) to analyze layer by layer. If compliance is needed, add DS-32 (Regulatory Enumeration).

**Example Prompts:**
- `domain-software-engineering/cloud/`
- `domain-software-engineering/devops/`

---

### Database Design & Operations
**User Need:** Design schemas, plan migrations, optimize queries

**Essential Techniques:**
1. **PostgreSQL Data Type Selection Matrix** (DS-56) — Type selection guidance (PostgreSQL-specific)
2. **Polyglot Persistence** (DS-117) — Choose the right database for each use case
3. **Medallion Architecture Layering** (DS-44) — Bronze/silver/gold data layering
4. **Domain Pattern Library** (DS-29) — Reference database design patterns

**Enhancement Techniques:**
- **Metric Specification** (DS-02) — Define performance metrics for queries
- **Safe Defaults Pattern** (DS-26) — Secure default configurations

**Combination Guidance:**
> **Synergy:** DS-56 provides precise type selection for PostgreSQL, DS-117 evaluates whether the right database is being used for each use case, DS-44 layers data into bronze/silver/gold tiers for data pipeline design, and DS-29 references established database design patterns.
> **Order:** DS-117 → DS-29 → DS-56 → DS-44
> **Avoid:** Don't combine DS-56 (PostgreSQL Types) with DS-117 (Polyglot Persistence) when already committed to PostgreSQL — polyglot analysis is for choosing databases, not for tuning one. Don't pair DS-44 (Medallion Architecture) with simple CRUD applications — it's for data pipelines.
> **Fallback:** If schema design is unclear, add DS-02 (Metric Specification) to define performance requirements that drive design decisions. If migration is risky, add QA-09 (Reversibility Assessment) to evaluate rollback options.

---

### Security Architecture
**User Need:** Design security architecture, implement security controls

**Essential Techniques:**
1. **STRIDE-Per-Interaction Matrix** (DS-50) — Systematic threat modeling
2. **Security Tier Classification** (DS-61) — Classify assets by security tier
3. **Security-Default Behavioral Traits** (DS-118) — Security-first default behaviors
4. **Checks-Effects-Interactions Pattern** (ST-49) — Systematic security verification

**Enhancement Techniques:**
- **Regulatory Enumeration Pattern** (DS-32) — List applicable security regulations
- **Risk-Stratified Documentation** (ST-43) — Document differently based on risk

**Combination Guidance:**
> **Synergy:** DS-50 provides systematic threat modeling per component interaction, DS-61 classifies assets by security sensitivity tier (focusing effort on the highest-value targets), DS-118 embeds security-first thinking into all analysis behavior, and ST-49 verifies checks, traces effects, and maps interactions.
> **Order:** DS-61 → DS-50 → DS-118 → ST-49
> **Avoid:** Don't combine DS-50 (STRIDE) with DT-02 (Specific Focus Areas) — STRIDE already provides the focus structure. Don't pair DS-118 (Security Defaults) with AG-01 (Personality-First) — security behavior should be a constraint, not a personality.
> **Fallback:** If the threat model is too broad, add DS-61 (Security Tiers) to prioritize the highest-risk components first. If documentation needs differentiation by risk, add ST-43 (Risk-Stratified Documentation).

---

### Financial Operations & Monitoring
**User Need:** Build financial monitoring, cost alerting, FinOps dashboards

**Essential Techniques:**
1. **Multi-Window Burn Rate Alerts** (DS-48) — Alert on spending trends across time windows
2. **FinOps Architecture Integration** (DS-133) — Embed cost awareness into architecture
3. **Embedded Calculation Formulas** (NE-11) — Include financial calculation formulas
4. **Metric Specification** (DS-02) — Define financial KPIs

**Combination Guidance:**
> **Synergy:** DS-48 provides multi-window alerting (detecting trends, not just point-in-time spikes), DS-133 embeds cost awareness into architecture decisions, NE-11 includes calculation formulas for transparent financial logic, and DS-02 defines the specific KPIs to track.
> **Order:** DS-02 → DS-133 → DS-48 → NE-11
> **Avoid:** Don't combine DS-48 (Burn Rate Alerts) with NE-09 (Scope Reduction) for financial monitoring — you need to watch all spending vectors, not narrow prematurely. Don't pair NE-11 (Calculation Formulas) with RT-04 (Analogical Reasoning) — financial calculations need precision, not analogies.
> **Fallback:** If cost monitoring is reactive rather than proactive, strengthen DS-133 with architectural cost budgets. If financial reports lack clarity, add NE-15 (Data Storytelling) to contextualize the numbers.

---

### Requirements Engineering
**User Need:** Transform requirements from vague to specific, structured formats

**Essential Techniques:**
1. **EARS Requirements Transformation** (DS-22) — Transform requirements using EARS notation
2. **Vague-to-Concrete Translation** (DD-02) — Convert fuzzy goals to specific criteria
3. **Constraint Specification** (CM-02) — Define hard constraints
4. **Scope Definition** (CM-03) — Explicit scope boundaries

**Combination Guidance:**
> **Synergy:** DS-22 transforms vague requirements into structured EARS notation, DD-02 converts fuzzy goals into specific verifiable criteria, CM-02 defines hard constraints, and CM-03 sets explicit boundaries on what's in and out of scope.
> **Order:** CM-03 → DD-02 → CM-02 → DS-22
> **Avoid:** Don't combine DS-22 (EARS) with ST-02 (Sequential Instructions) — EARS has its own structuring system. Don't pair DD-02 (Vague-to-Concrete) with NE-09 (Scope Reduction) in the same pass — first concretize all requirements, then prioritize.
> **Fallback:** If requirements are still ambiguous after EARS transformation, add MP-03 (Task Clarification) to ask targeted clarification questions. If scope keeps expanding, strengthen CM-03 with explicit "out of scope" declarations.

---

## AI Delegation & Productivity Tasks

### AI Delegation Decision
**User Need:** Determine how to delegate a task to AI — autonomous or iterative

**Essential Techniques:**
1. **Tool/Colleague Shape Decision** (DP-01) — Multi-dimensional scoring (spec clarity, verification cost, reversibility, coupling, confidence)
2. **Anchored Scoring Scales** (DP-03) — Concrete behavioral anchors for consistent scoring
3. **Dominant Driver Identification** (DP-06) — Name the key factor driving the decision
4. **Failure Mode Prediction** (DP-07) — Pre-identify how wrong choice fails

**Output Techniques:**
- **Stakes-Based Gate Policy** (DP-05) — Mandatory gates based on risk level
- **Role-Based Verification Assignment** (DP-08) — Match checks to verifier capabilities

**Template Pattern:**
```
Score each dimension 0-10:
1. SPEC CLARITY: 10 = can write acceptance tests, 0 = need to see drafts
2. VERIFICATION COST: 10 = check in 5 min, 0 = only expert can tell
3. REVERSIBILITY: 10 = delete and try again, 0 = downstream damage
4. HIDDEN COUPLING: 10 = fully isolated, 0 = deeply entangled
5. SHAPE CONFIDENCE: 10 = clear-cut, 0 = not enough info

RECOMMENDATION: [Tool-shaped / Colleague-shaped]
DOMINANT DRIVER: [Which dimension matters most and why]
FAILURE MODE: [How wrong choice fails]
```

**Combination Guidance:**
> **Synergy:** DP-01 provides multi-dimensional scoring for delegation decisions, DP-03 anchors scores to concrete behavioral examples (preventing vague "5 out of 10" ratings), DP-06 names the key factor driving the decision, and DP-07 pre-identifies how the wrong choice would fail.
> **Order:** DP-01 → DP-03 → DP-06 → DP-07
> **Avoid:** Don't combine DP-01 (Shape Decision) with RT-03 (Tree of Thoughts) — the shape decision framework already generates options. Don't pair DP-03 (Anchored Scales) with DS-02 (Metric Specification) — anchored scales ARE the metrics.
> **Fallback:** If the delegation decision is unclear, add DP-05 (Stakes-Based Gate Policy) to add mandatory gates based on risk level. If verification responsibility is ambiguous, add DP-08 (Role-Based Verification).

**Example Prompts:**
- `domain-engineering-workflows/workflows/engineering_delegation_fit_decision.md`

---

### Productivity Bottleneck Diagnosis
**User Need:** Identify what's actually constraining progress

**Essential Techniques:**
1. **Single Primary Constraint** (DP-09) — Force choosing ONE bottleneck
2. **Reframe Generation** (DP-10) — Mindset shift in one sentence
3. **Over-Protection Diagnosis** (DP-12) — What you're defending that isn't serving you
4. **Safe Experiment Design** (DP-11) — Low-risk 48-hour action

**Template Pattern:**
```
1) Identify my primary bottleneck. Choose ONE:
   - Clarity (don't know what's worth building)
   - Ambition (playing small)
   - Distribution (can't reach people)
   - Relationships (need trust/access not earned)

2) What I'm mistakenly protecting instead: [...]

3) Reframe: "Your job right now is ___, not ___."

4) 48-hour safe experiment: [low-risk, reversible action]
```

**Combination Guidance:**
> **Synergy:** DP-09 forces choosing ONE bottleneck (preventing scattered effort), DP-10 provides a mindset shift reframe, DP-12 identifies what you're over-protecting, and DP-11 designs a safe low-risk experiment to test the diagnosis.
> **Order:** DP-09 → DP-12 → DP-10 → DP-11
> **Avoid:** Don't combine DP-09 (Single Constraint) with RT-02 (Multi-Dimensional Analysis) — the whole point is to pick ONE thing, not analyze from multiple angles. Don't pair DP-11 (Safe Experiment) with DS-06 (Prioritization) — the experiment is already narrowed to one thing.
> **Fallback:** If the bottleneck diagnosis feels wrong after the experiment, repeat with DP-09 using different constraint options. If the reframe doesn't resonate, try NE-12 (Cognitive Mode Framing) to shift the mental model more fundamentally.

---

### Breaking Permission Loops
**User Need:** Stop waiting for approval you don't actually need

**Essential Techniques:**
1. **One-Day Default Rule** (DP-15) — Build first if completable in one day AND reversible
2. **Provisional Decision Message** (DP-16) — Announce intent with objection deadline
3. **Kill Signal Definition** (DP-13) — Observable evidence to pivot

**Template Pattern:**
```
Does this qualify for One-Day Default?
- Can be finished in a day? [Yes/No]
- Downside is reversible? [Yes/No]

If yes, build-first plan:
1. [Step]
2. [Step]

PROVISIONAL MESSAGE: "I'm going ahead with [X] unless I hear otherwise by [time]."
RESULTS MESSAGE: "I built [X]—here's what happened."
ROLLBACK PLAN: [How to undo if wrong]
```

**Combination Guidance:**
> **Synergy:** DP-15 provides the decision rule (build first if completable in one day AND reversible), DP-16 structures the announcement message with objection deadline, and DP-13 defines observable evidence that would trigger a pivot.
> **Order:** DP-15 → DP-13 → DP-16
> **Avoid:** Don't combine DP-15 (One-Day Default) with RT-03 (Tree of Thoughts) — the point is to act quickly, not deliberate over options. Don't pair with QA-02 (Adversarial Stress-Test) — permission loops are about overcoming hesitation, not finding more reasons to hesitate.
> **Fallback:** If the one-day default doesn't apply (too large or irreversible), switch to DP-11 (Safe Experiment Design) for a smaller testable step. If organizational culture blocks provisional decisions, strengthen DP-16 with explicit stakeholder alignment.

---

### Specification Writing
**User Need:** Create tight specs that prevent AI misinterpretation

**Essential Techniques:**
1. **Must-Not Constraints** (DP-04) — At least 2 "must not" requirements
2. **Compressed Specification** (DP-14) — 8 bullets, 12 words max
3. **Refuse Path Protocol** (DP-02) — Graceful handling of incomplete info

**Template Pattern:**
```
OBJECTIVE: [1-2 sentences]
NON-GOALS: [3-5 bullets - what NOT to do]
ACCEPTANCE CRITERIA:
- The output must [requirement]
- The output must NOT [constraint] ← REQUIRED
- The output must NOT [constraint] ← REQUIRED
STOP CONDITIONS: "Stop and ask if [situation]"
```

**Combination Guidance:**
> **Synergy:** DP-04 defines "must not" constraints (preventing common AI misinterpretation), DP-14 compresses the spec to 8 bullets of 12 words max (forcing clarity), and DP-02 defines what to do when the AI encounters incomplete information (ask, don't guess).
> **Order:** DP-04 → DP-14 → DP-02
> **Avoid:** Don't combine DP-14 (Compressed Spec) with DS-38 (Long-Form Documentation) — compression is the opposite of long-form. Don't pair DP-02 (Refuse Path) with AG-16 (Autonomous Execution) — autonomous agents can't stop and ask.
> **Fallback:** If specs are still misinterpreted, add NE-04 (Good vs Bad Example Calibration) to show concrete examples of correct vs incorrect interpretation. If the scope is too broad for compression, drop DP-14 and use CM-02 (Constraint Specification) instead.

---

### Distribution & Reach
**User Need:** Get adoption when building isn't the constraint

**Essential Techniques:**
1. **Distribution Wedge Selection** (DP-17) — Choose ONE channel
2. **Trust Deposits Definition** (DP-18) — Behaviors that compound reliability

**Combination Guidance:**
> **Synergy:** DP-17 forces choosing ONE distribution channel (preventing scattered effort across many), and DP-18 defines specific trust-building behaviors that compound over time in that channel.
> **Order:** DP-17 → DP-18
> **Avoid:** Don't combine DP-17 (Distribution Wedge) with RT-02 (Multi-Dimensional Analysis) — the point is to narrow to one channel, not analyze all options endlessly. Don't pair with NE-10 (Probability-Weighted Scenarios) — distribution is about commitment, not probabilistic hedging.
> **Fallback:** If the chosen channel isn't working after sustained effort, add DP-13 (Kill Signal Definition) to define when to pivot. If trust-building is too slow, add DP-11 (Safe Experiment) to test a complementary channel.

---

## Personal Agency & Execution Tasks

### AI Coaching Without Generic Advice
**User Need:** Get personalized guidance, not one-size-fits-all tips

**Essential Techniques:**
1. **Gate Check Pattern** (DP-19) — Require context before proceeding, refuse to guess
2. **Strict Coach Persona** (DP-20) — No advice until questions answered
3. **Consumable Artifact Requirement** (DP-21) — Output understandable in 60 seconds

**Template Pattern:**
```
GATE CHECK: If you do not have my Path, Goal, Time horizon, and Constraints, stop immediately and ask for them before proceeding. Do not guess.

You are a strict coach. Do not give advice until you've asked questions to fill every blank below.
```

**Combination Guidance:**
> **Synergy:** DP-19 prevents generic advice by requiring context before proceeding, DP-20 enforces a strict coaching stance (no advice until questions are answered), and DP-21 ensures every output is a consumable artifact (not just discussion).
> **Order:** DP-19 → DP-20 → DP-21
> **Avoid:** Don't combine DP-19 (Gate Check) with AG-16 (Autonomous Execution) — coaching is inherently interactive, not autonomous. Don't pair DP-20 (Strict Coach) with NE-07 (Emotional Validation) at the start — the coach should probe first, empathize second.
> **Fallback:** If the coaching feels too rigid, soften DP-20 by allowing limited advice after collecting minimum context. If the user won't provide context, add NE-03 (Input Template Scaffolding) to lower the effort of responding.

---

### Personal Execution System
**User Need:** Daily action system that produces artifacts, not just plans

**Essential Techniques:**
1. **Consumable Artifact Requirement** (DP-21) — Output must be shareable without explanation
2. **Distribution Fallback** (DP-22) — Forced accountability if avoiding sharing
3. **Done Fudge Prevention** (DP-24) — Done definition you can't rationalize around
4. **Failure Mode Prediction** (DP-07 fake-work variant) — Predict your avoidance behavior

**Template Pattern:**
```
ONE next action that is:
- Startable in 10 minutes (no setup)
- Finishable in 60-120 minutes
- Produces artifact consumable in 60 seconds without explanation
- Has "done" definition that I can't fudge

DONE LOOKS LIKE: [specific, observable criteria]
FAILURE MODE: [the fake-work I'll do instead if I'm not careful]
DISTRIBUTION FALLBACK: If I won't send it today: (a) publish now, (b) low-stakes recipient, (c) AI roleplay + send tomorrow 10am
```

**Combination Guidance:**
> **Synergy:** DP-21 ensures every session produces a shareable artifact (not just plans), DP-22 forces accountability when the user avoids sharing, DP-24 creates "done" definitions that can't be rationalized around, and DP-07 predicts the specific avoidance behavior to pre-empt it.
> **Order:** DP-07 → DP-21 → DP-24 → DP-22
> **Avoid:** Don't combine DP-24 (Done Fudge Prevention) with DD-04 (MVP Gates) — MVP gates allow minimum viable, fudge prevention doesn't; they create conflicting standards. Don't pair DP-22 (Distribution Fallback) with NE-07 (Emotional Validation) — the point is accountability, not comfort.
> **Fallback:** If the execution system is too harsh, soften DP-22 by offering graduated distribution options. If the user consistently fails to execute, switch focus to DP-09 (Single Primary Constraint) to find the underlying bottleneck.

---

### Multi-Audience Prompt Customization
**User Need:** Same prompt structure for different user contexts

**Essential Techniques:**
1. **Path Variants** (DP-23) — Role-specific customization within single prompt
2. **Gate Check Pattern** (DP-19) — Ensure user identifies their context

**Template Pattern:**
```
**Path A: Entry-level / early career**
[Customized version]

**Path B: Pivoting / mid-career transition**
[Customized version]

**Path C: Building something new**
[Customized version]
```

**Combination Guidance:**
> **Synergy:** DP-23 provides role-specific customization within a single prompt structure, and DP-19 ensures the user identifies their context before receiving customized content.
> **Order:** DP-19 → DP-23
> **Avoid:** Don't combine DP-23 (Path Variants) with NE-14 (Multi-Audience Documentation) — Path Variants is for prompt customization, Multi-Audience is for documentation. Different use cases. Don't pair with RP-02 (Audience-Specific) — the path variants already handle audience differentiation.
> **Fallback:** If path variants aren't sufficient, add NE-03 (Input Template Scaffolding) to gather more context for deeper customization. If the user's context doesn't fit any path, add MP-06 (Fallback Question Protocol) to handle ambiguous cases.

---

## Quality Systems & Process Tasks

### Diagnosing Recurring Problems
**User Need:** Understand why things keep breaking the same way

**Essential Techniques:**
1. **Training vs Rules Diagnosis** (QS-01) — Classify by cognitive load to prevent
2. **Required Decisions Pattern** (QS-05) — Force specific actions, not optional

**Template Pattern:**
```
For each pattern you identify:
1. Where does it show up?
2. What's the early warning sign?
3. Why does it keep happening?
4. Severity: CRITICAL / HIGH / MEDIUM / LOW

Then: Is this a TRAINING problem or a RULES problem?
- What would someone need to hold in their head to prevent this?
- If realistic → TRAINING (teach people better)
- If too much to track → RULES (build a check)
```

**Combination Guidance:**
> **Synergy:** QS-01 classifies whether each problem is best addressed by training (teach people better) or rules (build a check), and QS-05 forces specific required actions rather than optional recommendations.
> **Order:** QS-01 → QS-05
> **Avoid:** Don't combine QS-01 (Training vs Rules) with QA-02 (Adversarial Stress-Test) — diagnosis comes before stress-testing solutions. Don't pair with DS-06 (Prioritization) in the same pass — first diagnose the pattern type, then prioritize.
> **Fallback:** If the diagnosis is unclear (training or rules?), add QS-04 (Drift vs Violation Distinction) to determine if the problem is about gradual drift or clear violations. If patterns are recurring across teams, add MP-07 (Pattern Recognition Reflection).

---

### Building Rule Systems
**User Need:** Turn problems into enforceable rules

**Essential Techniques:**
1. **Checkable Rule Format** (QS-02) — Structured rule documentation
2. **Exception Template Design** (QS-06) — Lightweight exception handling
3. **Drift vs Violation Distinction** (QS-04) — Separate technical pass from spirit violation

**Template Pattern:**
```
For each rule, define:
- Trigger (when does this rule apply?)
- Wrong pattern (what violation looks like)
- Right pattern (what compliance looks like)
- Why it matters (one sentence)
- Scope (when to apply)
- Exception criteria (when breaking is allowed)
- Severity: CRITICAL / HIGH / MEDIUM / LOW
```

**Combination Guidance:**
> **Synergy:** QS-02 creates rules in a checkable format (trigger, wrong pattern, right pattern, why it matters), QS-06 designs lightweight exception handling (preventing rigid rules from blocking legitimate work), and QS-04 separates technical compliance from spirit violations.
> **Order:** QS-02 → QS-04 → QS-06
> **Avoid:** Don't combine QS-02 (Checkable Rules) with OC-02 (JSON Schema) unless rules are being automated — human-readable rules don't need machine-readable format. Don't pair QS-06 (Exception Template) with AG-04 (Behavioral Guardrails) — exceptions are the opposite of guardrails.
> **Fallback:** If rules are too rigid, strengthen QS-06 (Exception Template) with more exception criteria. If rules are unclear, add NE-04 (Good vs Bad Example Calibration) to show concrete examples of compliance vs violation.

---

### Team Training on Rules
**User Need:** Train people on WHY rules exist, not just what they are

**Essential Techniques:**
1. **Micro-lesson Structure** (QS-03) — Principle + failure story + exercises
2. **Training vs Rules Diagnosis** (QS-01) — Ensure training is the right solution

**Template Pattern:**
```
For each rule, create a micro-lesson:
- Principle: Why this rule exists (the underlying value)
- Failure story: What happened when violated (vivid enough to remember)
- Spot the violation: A scenario to test recognition
- Spot the drift: An edge case that technically passes but violates the spirit
```

**Combination Guidance:**
> **Synergy:** QS-03 structures training as principle + failure story + exercises (more effective than rule recitation), and QS-01 ensures training is actually the right solution (not a rules problem in disguise).
> **Order:** QS-01 → QS-03
> **Avoid:** Don't combine QS-03 (Micro-lesson) with DS-38 (Long-Form Documentation) — micro-lessons are deliberately short and focused. Don't pair with ED-01 (Iterative Scaffolding) for team training — scaffolding is for individual learning, micro-lessons are for team standards.
> **Fallback:** If training doesn't stick, the problem may actually be a rules problem — re-evaluate with QS-01. If engagement is low, add NE-04 (Good vs Bad Example Calibration) with real examples from the team's own work.

---

### Weekly Quality Monitoring
**User Need:** Track drift and force weekly decisions

**Essential Techniques:**
1. **Required Decisions Pattern** (QS-05) — Three required decisions (not optional)
2. **Drift vs Violation Distinction** (QS-04) — Monitor spirit violations

**Template Pattern:**
```
Weekly drift report:
1. Violations by severity
2. Exception patterns
3. Hotspots with diagnosis: training problem, rule problem, or process problem?
4. Three required decisions (not optional):
   - What gets fixed this week?
   - What rules get revised?
   - What exceptions get sunset?
```

**Combination Guidance:**
> **Synergy:** QS-05 forces three specific required decisions each week (preventing passive monitoring), and QS-04 monitors for spirit violations that technically pass rules but indicate drift.
> **Order:** QS-04 → QS-05
> **Avoid:** Don't combine QS-05 (Required Decisions) with NE-09 (Scope Reduction) — the three required decisions are already focused. Don't pair with DP-07 (Failure Mode Prediction) weekly — it's a one-time diagnosis, not a recurring check.
> **Fallback:** If weekly monitoring isn't surfacing real issues, strengthen QS-04 with explicit drift indicators. If decisions aren't being made, add DP-24 (Done Fudge Prevention) to define what "decided" actually means.

---

## Multi-Agent Architecture Tasks

### Diagnosing Multi-Agent Problems
**User Need:** Debug why multi-agent system is failing

**Essential Techniques:**
1. **Multi-Agent Failure Taxonomy** (MA-01) — Five canonical failure patterns
2. **Contention Risk Assessment** (MA-07) — Evaluate shared resource contention

**Template Pattern:**
```
Which failure pattern sounds closest?
- Agents waiting on each other (coordination overhead)
- Agents duplicating or undoing each other's work (collision)
- Agents drifting off-task or losing coherence (coherence loss)
- Single agent works fine, multiple agents make it worse (negative scaling)
- Single agent already fails, more agents won't help (fundamental loop problem)

DECISION: Scale now / Fix first / Unclear
FIRST BOTTLENECK: [one specific thing]
```

**Combination Guidance:**
> **Synergy:** MA-01 provides a taxonomy of five canonical failure patterns (enabling quick diagnosis), and MA-07 evaluates shared resource contention (the most common multi-agent bottleneck).
> **Order:** MA-01 → MA-07
> **Avoid:** Don't combine MA-01 (Failure Taxonomy) with RT-02 (Multi-Dimensional Analysis) — the taxonomy already provides the analysis dimensions. Don't pair with RP-03 (Multi-Persona Debate) — multi-agent debugging needs technical diagnosis, not perspective debates.
> **Fallback:** If the failure pattern doesn't match the taxonomy, the system may have a fundamental design issue — switch to MA-02 (Two-Tier Architecture) to evaluate the structural design. If contention is the issue, add MA-03 (Worker Isolation) to reduce shared state.

---

### Designing Multi-Agent Architecture
**User Need:** Structure multi-agent system with clear roles

**Essential Techniques:**
1. **Two-Tier Architecture** (MA-02) — Planner/Worker/Judge separation
2. **Worker Isolation** (MA-03) — Workers never coordinate directly
3. **Tool Diet** (MA-04) — Always-on vs on-demand tools

**Template Pattern:**
```
Design three roles:
1. PLANNER: Breaks work into tasks. Never executes.
   - Receives: [input format]
   - Outputs: [task assignments]
   - NEVER: Execute tasks, bypass Judge

2. WORKER: Executes one task. Doesn't know about other workers.
   - Receives: [task ticket]
   - Outputs: [completion format]
   - NEVER: Coordinate with other workers, decompose tasks

3. JUDGE: Evaluates work. Accept, reject, or retry.
   - Receives: [completed work]
   - Outputs: ACCEPT / RETRY / REJECT
   - NEVER: Do the work itself
```

**Combination Guidance:**
> **Synergy:** MA-02 separates Planner/Worker/Judge roles (preventing role confusion), MA-03 ensures workers never coordinate directly (simplifying the system), and MA-04 controls tool access (always-on vs on-demand) to prevent tool sprawl.
> **Order:** MA-02 → MA-03 → MA-04
> **Avoid:** Don't combine MA-03 (Worker Isolation) with AG-13 (Parallel-Converge) if workers need to share intermediate results — isolation means no direct communication. Don't pair MA-02 (Two-Tier) with AG-16 (Autonomous Master Prompt) unless the planner itself is autonomous.
> **Fallback:** If two-tier is too rigid, add MA-04 (Tool Diet) to give workers more capability without breaking isolation. If the architecture is too complex, simplify by removing the Judge role and having the Planner verify (acceptable for lower-stakes tasks).

---

### Agent Session Management
**User Need:** Handle session endings and state persistence

**Essential Techniques:**
1. **Session Lifecycle Design** (MA-05) — Treat endings as normal
2. **Scope Boundary Test** (MA-06) — "Task is too big if..."

**Template Pattern:**
```
SESSION TIMEBOX:
- Worker max: 30 min
- Warning trigger: 5 min before limit

CHECKPOINT PROTOCOL:
Every task completion, write to external state:
- Task ID + status
- Output artifact location
- Timestamp

RESTART HANDOFF:
1. Read last state
2. Verify last completed task
3. Resume from next task
```

**Combination Guidance:**
> **Synergy:** MA-05 treats session endings as normal events (not failures), and MA-06 tests whether a task is appropriately sized for a single session (preventing tasks that can't complete).
> **Order:** MA-06 → MA-05
> **Avoid:** Don't combine MA-05 (Session Lifecycle) with AG-16 (Autonomous Multi-Week) unless sessions are explicitly designed for long-running operation. Don't pair MA-06 (Scope Boundary) with DP-14 (Compressed Spec) — scope testing needs full detail, not compression.
> **Fallback:** If sessions consistently end mid-task, strengthen MA-06 (Scope Boundary) with smaller task decomposition. If state is lost between sessions, add CM-08 (File-Based State Persistence) for reliable checkpointing.

---

### Multi-Agent Quality Control
**User Need:** Quality gates for multi-agent outputs

**Essential Techniques:**
1. **Judge Decision Rules** (MA-08) — Explicit ACCEPT/RETRY/REJECT triggers
2. **Two-Tier Architecture** (MA-02) — Dedicated Judge role

**Template Pattern:**
```
PASS/FAIL GATES (all must pass):
☐ [Gate 1]
☐ [Gate 2]
☐ [Gate 3]

DECISION RULES:
- ACCEPT: All gates pass + grades acceptable → Ship it
- RETRY: Gates pass but grade below bar → Return to worker with feedback
- REJECT: Gate fails → Return to Planner, don't retry same worker
```

**Combination Guidance:**
> **Synergy:** MA-08 provides explicit ACCEPT/RETRY/REJECT decision rules, and MA-02 ensures the Judge role is dedicated and separate from workers (preventing self-grading).
> **Order:** MA-02 → MA-08
> **Avoid:** Don't combine MA-08 (Judge Rules) with QA-01 (Self-Verification) as the primary quality check — self-verification is for single-agent prompts, Judge rules are for multi-agent systems. Don't pair with QA-15 (Self-Consistency) at the Judge level — the Judge should evaluate work against criteria, not generate multiple solutions.
> **Fallback:** If the Judge is too strict (too many rejections), add QA-09 (Reversibility Assessment) to allow the Judge to conditionally accept with noted caveats. If quality is still insufficient, add QA-08 (Gate-Based Verification) for additional automated gates before the Judge.

---

## AI Communication & System Prompt Design Tasks

### Effective AI Communication
**User Need:** Get better results from AI by understanding how it interprets requests and when/why it pushes back

**Essential Techniques:**
1. **Multi-Lens Request Framing** (CM-12) — Address multiple interpretation dimensions (immediate desire, final goal, standards, autonomy)
2. **Expert Friend Positioning** (RP-06) — Shift from cautious professional to frank expert friend dynamic
3. **Principled Pushback Navigation** (IT-10) — Address AI's stated concerns rather than rephrasing around them
4. **Non-Default Behavior Activation** (IT-11) — Explicitly request available but non-default behaviors

**Enhancement Techniques:**
- **Distinguishing Context Provision** (CM-13) — Provide context that differentiates from potential misuse
- **Explicit Context Framing** (CM-01) — Provide relevant background upfront

**Combination Guidance:**
> **Synergy:** CM-12 ensures the AI has rich signal across multiple interpretation dimensions, RP-06 shifts the communication dynamic to get substantive rather than cautious responses, IT-10 navigates pushback productively when it occurs, and IT-11 activates specific non-default behaviors.
> **Order:** CM-12 → RP-06 → IT-10 → IT-11 (CM-12 sets context first, RP-06 sets dynamic, IT-10/IT-11 handle specific situations)
> **Avoid:** Don't combine RP-06 (Expert Friend) with RP-01 (Expert Role Assignment) — RP-06 shifts the relationship dynamic, RP-01 assigns knowledge. Using both can create conflicting persona signals.
> **Fallback:** If pushback persists after IT-10, add CM-13 (Distinguishing Context) to provide stronger differentiation context. If responses remain generic, check that CM-12 is addressing the "final goal" lens — this is the most commonly missed dimension.

---

### System Prompt Architecture
**User Need:** Design effective system prompts for AI deployments, agents, or custom applications

**Essential Techniques:**
1. **Reasoning-Based Constraint Design** (CM-11) — Convert bare rules to reasoning-based constraints
2. **Principal Hierarchy Specification** (CM-14) — Define trust levels (platform > operator > user)
3. **Gap-Filling Intent Signaling** (CM-15) — Signal intent for scenarios instructions don't cover
4. **Dual-Failure Quality Test** (QA-20) — Test for both harmful AND needlessly unhelpful responses

**Enhancement Techniques:**
- **Authority Boundary Specification** (CM-09) — Define can-do/ask-first/never-do zones
- **Behavioral Guardrails** (AG-04) — Explicit behavioral constraints
- **Non-Default Behavior Activation** (IT-11) — Toggle default behaviors for deployment context

**Combination Guidance:**
> **Synergy:** CM-11 makes individual constraints more robust through reasoning, CM-14 establishes who has authority at each level, CM-15 ensures gap-filling judgment aligns with your goals, and QA-20 validates the prompt catches both failure directions.
> **Order:** CM-14 → CM-11 → CM-15 → QA-20 (establish hierarchy first, then constraints, then intent signals, then test)
> **Avoid:** Don't overuse CM-02 (Constraint Specification) with CM-11 — CM-11 subsumes bare must/must-not rules by adding reasoning. Don't skip CM-15 in favor of more rules — you can't anticipate every scenario.
> **Fallback:** If the system prompt is too rigid in edge cases, strengthen CM-15 (Gap-Filling) with explicit priority ordering. If QA-20 reveals dual failures, revisit CM-11 to ensure constraints explain their purpose.

**Template Pattern:**
```
## Context (who you are, what you do):
[Full deployment context — not just role, but purpose, users, success criteria]

## Constraints (reasoning-based):
For each constraint: [Context] + [Reasoning] + [Desired behavior] + [Edge case guidance]

## Trust Calibration:
- Operator permissions: [what you're instructing]
- User permissions: [what users can customize]
- Absolute limits: [what never changes]

## Intent Signals (for gap-filling):
When these instructions don't cover a situation, prioritize:
1. [First priority]
2. [Second priority]
3. [Third priority]

## Test: Would a thoughtful senior person be comfortable with this response?
- Not harmful AND not needlessly unhelpful
```

---

## Quick Selection Guide

**Simple task, clear output format** → ST-01, ST-02, ST-03
**Complex reasoning needed** → RT-01 (CoT), RT-02 (Multi-Dimensional)
**High-stakes decision** → QA-01, QA-02, RT-03, RP-03
**Teaching/explaining** → RP-02, RT-04, ED-01, ED-02
**Code analysis** → ST-01, ST-02, RT-02, RT-05, ST-03, DS-06
**Strategic planning** → DS-01, CM-01, RT-03, RP-03
**Need consistency** → ST-03, OC-02, OC-03 (templates)
**Need depth** → OC-05 (min length), RT-01 (CoT), RT-02
**AI delegation decisions** → DP-01 (Shape), DP-05 (Gates), DP-08 (Verification)
**Productivity bottlenecks** → DP-09 (Single Constraint), DP-10 (Reframe), DP-12 (Over-Protection)
**Breaking permission loops** → DP-15 (One-Day Default), DP-16 (Messages), DP-11 (Safe Experiments)
**Tight specifications** → DP-04 (Must-Not), DP-14 (Compressed), DP-02 (Refuse Path)
**Personal agency/execution** → DP-19 (Gate Check), DP-20 (Strict Coach), DP-22 (Distribution Fallback)
**AI coaching (not generic)** → DP-19 (Gate Check), DP-20 (Strict Coach), DP-21 (Consumable Artifact)
**Quality systems** → QS-01 (Training vs Rules), QS-02 (Checkable Rules), QS-04 (Drift vs Violation)
**Team training on rules** → QS-03 (Micro-lesson), QS-01 (Training vs Rules)
**Multi-agent design** → MA-01 (Failure Taxonomy), MA-02 (Two-Tier), MA-03 (Worker Isolation)
**Multi-agent debugging** → MA-01 (Failure Taxonomy), MA-07 (Contention Risk)
**Agent session management** → MA-05 (Session Lifecycle), MA-06 (Scope Boundary), MA-04 (Tool Diet)
**Building AI agents/skills** → AG-01 (Personality), AG-04 (Guardrails), AG-05 (Templates), AG-09 (Anti-Patterns)
**Multi-agent pipelines** → AG-07 (Pipeline), AG-08 (Gates), AG-13 (Parallel-Converge)
**Autonomous agent execution** → AG-16 (Master Prompt), AG-17 (Auto-Resume), CM-08 (State Persistence)
**Conversational prompts** → NE-01 (Single-Question), NE-02 (Phases), NE-07 (Emotional Validation)
**Business communication** → NE-13 (Tech-to-Business), NE-15 (Data Storytelling), NE-17 (Call-to-Action)
**Decision support** → NE-09 (Scope Reduction), NE-10 (Probability-Weighted), NE-11 (Calculations)
**Visual outputs/dashboards** → SV-01 (Visual Spec), SV-07 (Calculations), DS-25 (Chart Dictionary)
**AI communication improvement** → CM-12 (Multi-Lens), RP-06 (Expert Friend), IT-10 (Pushback Navigation), IT-11 (Non-Default Activation)
**System prompt design** → CM-11 (Reasoning Constraints), CM-14 (Principal Hierarchy), CM-15 (Gap-Filling Intent), QA-20 (Dual-Failure Test)
**Handling AI pushback** → IT-10 (Pushback Navigation), CM-13 (Distinguishing Context), IT-11 (Non-Default Activation)
**AI image generation (print)** → SV-11 (Terminology Steering), SV-12 (Grid Forcing), SV-13 (Constraint Redundancy), SV-17 (Deliverables Locking), SV-18 (Validation Checklist)
**AI image generation (infographics)** → SV-01 (Visual Spec), SV-11 (Terminology Steering), SV-13 (Constraint Redundancy), SV-15 (Allowed/Forbidden), SV-18 (Validation Checklist)
**Worksheets/printables** → SV-05 (Worksheet Format), SV-01 (Visual Spec), DT-06 (Typography)
**Interview-to-synthesis** → SV-03 (Interview), SV-08 (Tiered Questions), SV-02 (Grouped Input)
**Task completion/done definition** → DD-02 (Vague-to-Concrete), DD-04 (MVP Gates), DD-07 (Self-Audit)
**Gate-based verification** → QA-08 (Gate Verification), DD-06 (Iteration Control), DD-11 (BLOCKED)
**Troubleshooting docs** → IT-23 (Symptom-Based), RT-10 (Decision Tree), RT-09 (Root Cause)
**API documentation** → IT-20 (Progressive Examples), IT-21 (Use Case-Driven), OC-12 (External Refs)
**Configuration generation** → DS-26 (Safe Defaults), DS-27 (Professional Defaults), DS-28 (Environment-Specific)
**Security architecture** → DS-50 (STRIDE), DS-61 (Security Tiers), DS-118 (Security Defaults)
**Database design** → DS-56 (PostgreSQL Types), DS-117 (Polyglot Persistence), DS-44 (Medallion)
**Compliance/regulatory** → DS-32 (Regulatory Enumeration), DS-33 (Jurisdiction-Adaptive), OC-10 (Disclaimers)
**Prompt improvement** → MP-01 (Reverse), MP-02 (Recursive), MP-08 (Four-Layer), QA-16 (Auto-Iteration)
**Incident response** → AG-19 (Time-Critical), DS-36 (Escalation), RT-09 (Root Cause)
**Requirements engineering** → DS-22 (EARS), DD-02 (Vague-to-Concrete), CM-02 (Constraints)
**Financial operations** → DS-48 (Burn Rate), DS-133 (FinOps), NE-11 (Calculations)
**Context management** → CM-05 (Progressive Accumulation), CM-07 (Token-Budget), CM-10 (Memory Scaffold)

---

## Technique Differentiation Guide

When multiple techniques seem similar, use this guide to choose the right one.

### Role Definition: RP-01 vs AG-01 vs ST-16 vs ST-45

| Technique | Use When | Key Difference |
|-----------|----------|----------------|
| **RP-01: Expert Role Assignment** | Simple "act as X expert" framing | Assigns expertise only, no personality |
| **AG-01: Personality-First Role Definition** | Building an AI agent with consistent behavior | Includes personality, memory, failure awareness |
| **ST-16: Behavioral Trait Declarations** | Defining specific behaviors within any prompt | Declares traits, not a full persona |
| **ST-45: Methodology-Centric Expertise** | Defining expertise through methodology | Expertise through process, not just title |

**Choose RP-01** for simple prompts. **Choose AG-01** for agent personas. **Choose ST-16** for adding specific behaviors to any prompt. **Choose ST-45** when the methodology matters more than the title.

---

### Reasoning Chains: RT-01 vs RT-02 vs DT-01 vs DT-02

| Technique | Use When | Key Difference |
|-----------|----------|----------------|
| **RT-01: Chain-of-Thought** | Step-by-step logical reasoning | Linear reasoning chain |
| **RT-02: Multi-Dimensional Analysis** | Analyzing from multiple angles | Parallel analysis dimensions |
| **DT-01: Hierarchical Task Breakdown** | Breaking complex work into subtasks | Task decomposition hierarchy |
| **DT-02: Specific Focus Areas** | Listing specific areas to examine | Enumerated checklist |

**Choose RT-01** for debugging/logic problems. **Choose RT-02** for comprehensive analysis. **Choose DT-01** for project planning. **Choose DT-02** for audits/reviews with known categories.

---

### Output Formatting: ST-03 vs OC-02 vs OC-03 vs OC-06 vs SV-01

| Technique | Use When | Key Difference |
|-----------|----------|----------------|
| **ST-03: Output Format Specification** | General output structure definition | Broad format guidance |
| **OC-02: JSON Schema Specification** | Machine-readable structured output | Exact JSON schema |
| **OC-03: Markdown Table Specification** | Tabular data presentation | Table-specific formatting |
| **OC-06: Output Contract Structure** | Strict output contract (API-like) | Contract-level precision |
| **SV-01: Visual Output Specification** | Visual/layout-oriented output | Physical layout and dimensions |

**Choose ST-03** for most prompts. **Choose OC-02** for programmatic consumption. **Choose OC-03** for comparison tables. **Choose OC-06** for agent-to-agent communication. **Choose SV-01** for visual/print outputs.

---

### Quality Checking: QA-01 vs QA-02 vs QA-08 vs QA-15

| Technique | Use When | Key Difference |
|-----------|----------|----------------|
| **QA-01: Self-Verification (Chain-of-Verification)** | General self-check of outputs | Self-critique and revision |
| **QA-02: Adversarial Stress-Test** | High-stakes outputs needing attack testing | Actively tries to break the output |
| **QA-08: Gate-Based Verification** | Multi-stage workflows with checkpoints | Pass/fail gates between stages |
| **QA-15: Self-Consistency** | Maximum confidence in answers | Multiple independent solutions compared |

**Choose QA-01** for standard quality checking. **Choose QA-02** for security/safety-critical work. **Choose QA-08** for pipeline workflows. **Choose QA-15** when you need highest confidence.

---

### Context Management: CM-01 vs CM-05 vs CM-07 vs CM-08 vs CM-10

| Technique | Use When | Key Difference |
|-----------|----------|----------------|
| **CM-01: Explicit Context Framing** | Providing background info upfront | Static context block |
| **CM-05: Progressive Context Accumulation** | Building context across interactions | Accumulated over time |
| **CM-07: Token-Budget-Aware Progressive Loading** | Managing large context windows | Token-aware loading strategy |
| **CM-08: File-Based State Persistence** | Persisting state between sessions | File-system state storage |
| **CM-10: Memory Scaffold Architecture** | Building structured long-term memory | Structured memory system |

**Choose CM-01** for single-prompt context. **Choose CM-05** for multi-turn conversations. **Choose CM-07** for very large inputs. **Choose CM-08** for cross-session agents. **Choose CM-10** for persistent agent memory.

---

### Context & Trust for AI Deployments: CM-11 vs CM-12 vs CM-13 vs CM-14 vs CM-15

| Technique | Use When | Key Difference |
|-----------|----------|----------------|
| **CM-11: Reasoning-Based Constraint Design** | Writing system prompt constraints | Converts rules to reasoning |
| **CM-12: Multi-Lens Request Framing** | Crafting individual requests | Addresses AI's interpretation dimensions |
| **CM-13: Distinguishing Context Provision** | Borderline/sensitive requests | Differentiates from potential misuse |
| **CM-14: Principal Hierarchy Specification** | Multi-stakeholder deployments | Defines trust levels between parties |
| **CM-15: Gap-Filling Intent Signaling** | Instructions can't cover all cases | Signals intent for uncovered scenarios |

**Choose CM-11** for individual constraint quality. **Choose CM-12** for request-level communication. **Choose CM-13** for sensitive/borderline topics. **Choose CM-14** for deployment trust architecture. **Choose CM-15** for edge case judgment alignment.

---

### Done Definition: DD-02 vs DD-04 vs DD-07 vs QA-08

| Technique | Use When | Key Difference |
|-----------|----------|----------------|
| **DD-02: Vague-to-Concrete Translation** | Goal is unclear, needs concretizing | Translates fuzzy to specific |
| **DD-04: MVP Gates** | Need minimum viable completion criteria | Minimum bar to pass |
| **DD-07: Self-Audit Table** | Self-check before declaring done | Checklist-style audit |
| **QA-08: Gate-Based Verification** | Multi-stage workflows with checkpoints | Gates between stages |

**Choose DD-02** first to define what "done" means. **Choose DD-04** to set the minimum bar. **Choose DD-07** for the final self-check. **Choose QA-08** for workflows with multiple stages.

---

### Prompt Improvement: MP-01 vs MP-02 vs MP-04 vs MP-08

| Technique | Use When | Key Difference |
|-----------|----------|----------------|
| **MP-01: Reverse Prompting** | Generating ideal prompt from desired output | Works backward from output |
| **MP-02: Recursive Optimization** | Iterating on existing prompt | Three-pass improvement |
| **MP-04: Strategic Edge Case Calibration** | Adding edge case handling | Edge case focused |
| **MP-08: Four-Layer Enhancement Process** | Systematic comprehensive improvement | Four distinct improvement layers |

**Choose MP-01** when starting from scratch. **Choose MP-02** for quick iteration. **Choose MP-04** for robustness. **Choose MP-08** for thorough overhaul.

---

## Combination Ordering Rules

When combining multiple techniques in a single prompt, apply them in this order:

### Universal Ordering (applies to all prompts)

```
1. CONTEXT FIRST: CM-xx techniques (framing, constraints, scope)
   ↓
2. ROLE/PERSONA: RP-xx or AG-xx techniques (who the AI is)
   ↓
3. STRUCTURE: ST-xx techniques (how the prompt is organized)
   ↓
4. REASONING: RT-xx or DT-xx techniques (how to think about the problem)
   ↓
5. DOMAIN: DS-xx techniques (domain-specific patterns)
   ↓
6. OUTPUT: OC-xx or SV-xx techniques (what the output looks like)
   ↓
7. QUALITY: QA-xx or DD-xx techniques (verification and done criteria)
```

### Why This Order Works

- **Context before Role:** The AI needs to understand the situation before assuming a persona
- **Role before Structure:** The persona influences how instructions should be structured
- **Structure before Reasoning:** The organization provides a framework for the reasoning approach
- **Reasoning before Domain:** General reasoning patterns guide domain-specific application
- **Domain before Output:** Domain knowledge shapes what outputs are appropriate
- **Output before Quality:** Define what you expect before defining how to verify it

### Ordering Within Technique Families

**Within Context (CM):**
1. CM-03 (Scope) → 2. CM-01 (Framing) → 3. CM-02 (Constraints)
*Define boundaries, then fill in context, then add constraints*

**Within Reasoning (RT):**
1. RT-01 (Chain-of-Thought) → 2. RT-02 (Multi-Dimensional) → 3. RT-05 (Evidence-Based) → 4. RT-06 (Correlation)
*Think step-by-step, then across dimensions, then with evidence, then find connections*

**Within Quality (QA):**
1. QA-01 (Self-Verification) → 2. QA-02 (Adversarial) → 3. QA-04 (Uncertainty) → 4. QA-15 (Self-Consistency)
*Self-check, then attack-test, then acknowledge uncertainty, then verify consistency*

### Known Conflicts

| Techniques | Conflict | Resolution |
|-----------|----------|------------|
| NE-01 (Single-Question) + ST-02 (Sequential Instructions) | Single-question pacing conflicts with giving all instructions upfront | Use NE-01 for conversational prompts, ST-02 for single-shot prompts — don't combine |
| OC-05 (Min Length) + NE-05 (Token Budget) | Minimum length conflicts with length control | Choose one: either set a floor (OC-05) or a ceiling (NE-05), not both |
| RP-01 (Expert Role) + AG-01 (Personality-First) | Both define the AI's identity | Use AG-01 instead — it subsumes RP-01 with more nuance |
| QA-15 (Self-Consistency) + NE-05 (Token Budget) | Multiple solutions consume many tokens | Use QA-15 only when token budget is generous |
| RT-03 (Tree of Thoughts) + NE-01 (Single-Question) | Tree of Thoughts generates branching internally, Single-Question is interactive | Don't combine — RT-03 is for internal reasoning, NE-01 is for external dialogue |
| CM-06 (Semantic Vector Context) + CM-07 (Token-Budget Loading) | Both manage context window | Choose based on primary concern: semantic relevance (CM-06) vs token efficiency (CM-07) |

### Common Effective Combinations

| Use Case | Combination | Why It Works |
|----------|-------------|--------------|
| **Code analysis** | CM-01 → ST-02 → RT-02 → RT-05 → DS-06 → ST-03 | Context → Structure → Multi-angle analysis → Evidence → Prioritize → Format |
| **Agent persona** | AG-01 → AG-03 → AG-04 → AG-05 → AG-09 | Personality → Mission → Guardrails → Templates → Anti-patterns |
| **Conversational intake** | NE-01 → NE-02 → NE-07 → NE-08 → SV-03 | Pacing → Phases → Emotional validation → Catchall → Synthesis |
| **Done definition** | DD-02 → DD-04 → DD-03 → DD-07 → DD-06 | Concretize → MVP bar → Order checks → Self-audit → Iteration limit |
| **Security audit** | RP-01 → DS-50 → DT-02 → RT-05 → QA-02 → DS-06 | Expert → Threat model → Focus areas → Evidence → Stress-test → Prioritize |
| **Documentation** | RP-02 → NE-14 → DS-37 → IT-20 → ST-04 → OC-12 | Audience → Multi-audience → Progressive abstraction → Examples → Sections → References |
| **High-stakes decision** | CM-01 → RT-03 → RP-03 → QA-02 → QA-04 → ST-22 | Context → Options → Debate → Stress-test → Uncertainty → Comparison matrix |

---

## Technique Compatibility Matrix

A reference for understanding which technique families combine well, which require care, and which conflict.

### Family Compatibility Overview

| Family Pair | Compatibility | Notes |
|-------------|:---:|-------|
| **CM + RP** | ✅ Always | Context first, then role — universal pattern |
| **CM + ST** | ✅ Always | Context frames the structure |
| **ST + RT** | ✅ Always | Structure organizes reasoning |
| **ST + DS** | ✅ Always | Structure frames domain-specific patterns |
| **RT + QA** | ✅ Always | Reasoning generates, quality checks verify |
| **DS + QA** | ✅ Always | Domain expertise validated by quality checks |
| **RP + RT** | ✅ Always | Role shapes how reasoning is applied |
| **DD + QA** | ✅ Always | Done definition validated by quality gates |
| **ED + IT** | ✅ Always | Education techniques enhanced by interaction patterns |
| **SV + SV** | ✅ Always | Visual techniques stack naturally |
| **CM + QA** | ✅ Always | Constraints define what quality checks verify |
| **AG + CM** | ✅ Always | Agent techniques need context management |
| **AG + AG** | ✅ Always | Agentic techniques layer naturally (persona → mission → guardrails) |
| **NE + NE** | ✅ Always | Non-engineering techniques compose well within domain |
| **DP + DP** | ✅ Always | Delegation/productivity techniques designed to compose |
| **QS + QS** | ✅ Always | Quality system techniques designed to compose |
| **MA + MA** | ✅ Always | Multi-agent techniques designed to compose |
| **RP + AG** | ⚠️ Pick one | AG-01 subsumes RP-01 — use AG-01 for agents, RP-01 for simple prompts |
| **NE + ST** | ⚠️ Partial | NE-01 (Single-Question) conflicts with ST-02 (Sequential Instructions). Other combinations work fine |
| **OC + NE** | ⚠️ Partial | OC-05 (Min Length) conflicts with NE-05 (Token Budget). Other combinations work fine |
| **SV + OC** | ⚠️ Partial | SV-01 replaces ST-03/OC format specs for visual content. Don't double-define output format |
| **CM-05 + CM-07** | ⚠️ Pick one | Progressive Accumulation vs Token-Budget Loading — different context strategies |
| **CM-06 + CM-07** | ⚠️ Pick one | Semantic Vector vs Token-Budget — different context optimization goals |
| **QA-15 + NE-05** | ❌ Conflict | Self-Consistency requires multiple solutions (high tokens) vs Token Budget (low tokens) |
| **RT-03 + NE-01** | ❌ Conflict | Tree of Thoughts (internal branching) vs Single-Question (external interaction) |
| **NE-01 + ST-02** | ❌ Conflict | Interactive pacing vs all-at-once sequential instructions |
| **OC-05 + NE-05** | ❌ Conflict | Minimum length floor vs maximum length ceiling — pick one direction |
| **DP-02 + AG-16** | ❌ Conflict | Refuse Path (stop and ask) vs Autonomous Execution (never stop) |
| **DP-14 + DS-38** | ❌ Conflict | Compressed Spec (8 bullets max) vs Long-Form Documentation |

### Compatibility Legend

| Symbol | Meaning | Guidance |
|--------|---------|----------|
| ✅ | Always compatible | Combine freely, follow universal ordering |
| ⚠️ | Conditionally compatible | Works in some cases — check the specific note |
| ❌ | Conflict | Do not combine these specific techniques in the same prompt |

### Cross-Family Synergy Patterns

These patterns describe how technique families interact to produce results greater than the sum of their parts:

**1. The Analysis Pipeline:** CM → RP → ST → RT → DS → QA
> Context provides the facts, role provides the lens, structure organizes the approach, reasoning analyzes the evidence, domain knowledge adds depth, and quality checking catches errors. This is the universal analysis pattern.

**2. The Agent Construction Stack:** AG → CM → ST → QA → DD
> Agent personality and mission first, then context management for state, structure for output templates, quality for guardrails, and done definition for completion criteria. Each layer constrains the next.

**3. The Interactive Dialogue Loop:** NE → SV → ED
> Non-engineering conversational techniques (pacing, emotional validation) drive the interaction, visual/interview techniques gather structured input, and educational techniques adapt to the user's level. Best for coaching, intake, and teaching.

**4. The Quality Verification Stack:** QA → DD → QA
> First pass: quality check the work. Then: verify "done" criteria are met. Final pass: adversarial stress-test the completed output. Three distinct verification passes at different abstraction levels.

**5. The Decision Framework:** CM → RT → RP → QA → NE
> Context grounds the decision, reasoning generates options, role/perspective evaluates from multiple angles, quality testing stress-tests the leading option, and non-engineering techniques translate the decision for stakeholders.

**6. The Multi-Agent Pipeline:** MA → AG → CM → QA
> Multi-agent architecture defines the system structure, agentic techniques configure each agent, context management handles inter-agent state, and quality assurance gates verify handoffs between agents.

### When Compatibility Fails: Diagnostic Checklist

If a technique combination is producing poor results:

1. **Check for known conflicts** — Is one of the ❌ pairs in use?
2. **Check ordering** — Are techniques applied in the universal order (CM → RP → ST → RT → DS → OC/SV → QA)?
3. **Check overload** — Are there more than 5-7 techniques? Reduce to 3-5 core techniques.
4. **Check family mismatch** — Are interactive techniques (NE, ED) mixed with single-shot techniques (ST, OC)?
5. **Check abstraction mismatch** — Are high-level techniques (DS-01 Framework) mixed with low-level techniques (DS-56 PostgreSQL Types) without a bridge?
6. **Check the fallback** — Each use case section above includes a Fallback recommendation for when the primary combination doesn't work.

---

## Complete Technique Coverage Index

Every technique mapped to its primary use case section(s). Use this to verify a technique hasn't been overlooked.

### ST — Structural Techniques (17)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| ST-01 | Clear Objective Statement | Analysis, Creation, Planning |
| ST-02 | Structured Sequential Instructions | Analysis, Creation, Planning |
| ST-03 | Output Format Specification | Creation, Analysis (all sections) |
| ST-04 | Delimited Sections | Analysis, Documentation, Teaching |
| ST-05 | Hierarchical Organization | Analysis, Architecture, Root Cause |
| ST-16 | Behavioral Trait Declarations | Agentic (Agent Personas) |
| ST-22 | Multi-Solution Comparison Matrix | Decision (Architecture Decisions) |
| ST-35 | Principle-Based Guidance | Creation (Code Generation) |
| ST-37 | Minimal Agent Pattern | Agentic (Building Agent Skills) |
| ST-38/39 | Production-Ready Architecture Patterns | Creation (Code Generation) |
| ST-40 | Three-Tier Value Classification | Analysis (Code Quality) |
| ST-42 | Criticality Labeling | Analysis (Security Audit) |
| ST-43 | Risk-Stratified Documentation | Analysis (Security Audit), Infrastructure (Security Architecture) |
| ST-44 | Progressive Complexity Scaffolding | Teaching (Explain Code/Concept) |
| ST-45 | Methodology-Centric Expertise | Agentic (Agent Personas) |
| ST-46 | Assertion-Evidence Content Structure | Creation (Presentation Generation) |
| ST-49 | Checks-Effects-Interactions Pattern | Analysis (Security Audit), Infrastructure (Security Architecture) |

### RT — Reasoning Techniques (12)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| RT-01 | Chain-of-Thought | Problem-Solving (Debugging, Root Cause), Teaching |
| RT-02 | Multi-Dimensional Analysis | Analysis (all), Decision, Teaching |
| RT-03 | Tree of Thoughts | Decision (Architecture, Strategic Planning) |
| RT-04 | Analogical Reasoning | Teaching, Documentation |
| RT-05 | Evidence-Based Reasoning | Analysis, Problem-Solving, Verification |
| RT-06 | Correlation and Cross-Analysis | Analysis (Performance), Problem-Solving (Root Cause) |
| RT-07 | Cascade Effect Analysis | Analysis (Architecture, Performance), Decision |
| RT-08 | Workaround Cost Analysis | Analysis (Architecture), Decision |
| RT-09 | Root Cause Explanation | Problem-Solving (Debugging, Root Cause, Incident), Documentation (Troubleshooting) |
| RT-10 | Troubleshooting Decision Tree | Problem-Solving (Debugging, Incident), Documentation (Troubleshooting) |
| RT-11 | Error Recovery Patterns | Problem-Solving (Debugging), Documentation (Troubleshooting) |
| RT-15/20/22 | Sequential Response Approach Pattern | Creation (Code Generation) |

### OC — Output Control Techniques (11)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| OC-02 | JSON Schema Specification | Creation (Code Generation) |
| OC-03 | Markdown Table Specification | Analysis, Creation |
| OC-04 | Conditional Output Logic | Analysis (Code Quality) |
| OC-05 | Minimum Length Requirements | Analysis (depth control) |
| OC-06 | Output Contract Structure | Creation (Code Generation), Agentic |
| OC-07 | Operating Principles Declaration | Creation (Code Generation) |
| OC-08 | Multi-Mode Prompt Architecture | Documentation Generation |
| OC-09 | Capability Boundary Specification | Agentic (Autonomous Execution) |
| OC-10 | Mandatory Disclaimer Pattern | Compliance & Regulatory |
| OC-11 | Grouped Reporting by Pattern Type | Analysis (Code Quality) |
| OC-12 | External Reference Catalog | Documentation (API, Multi-Audience) |

### QA — Quality Assurance Techniques (19)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| QA-01 | Self-Verification | Quality Assurance (High-Stakes) |
| QA-02 | Adversarial Stress-Test | Quality Assurance (High-Stakes), Security |
| QA-04 | Uncertainty Acknowledgment | Quality Assurance (High-Stakes), Decision |
| QA-05 | Citation Requirements | Quality Assurance (High-Stakes), Compliance |
| QA-06 | Constitutional AI for Prompts | Prompt Improvement |
| QA-07 | Statistical A/B Testing | Testing & Validation |
| QA-08 | Gate-Based Verification | Task Completion, Testing & Validation, Agentic (Auto-Improvement Readiness, Trace Audit) |
| QA-09 | Reversibility Assessment | Testing & Validation, Task Completion |
| QA-10 | Test Battery Protocol | Test Generation, Testing & Validation |
| QA-11 | Pass/Fail Test Harness | Test Generation, Testing & Validation |
| QA-12 | False Positives Identification | Quality Assurance (High-Stakes) |
| QA-13 | Failure Recovery Specification | Testing & Validation |
| QA-14 | Ground Truth Principle | Quality Assurance (High-Stakes) |
| QA-15 | Self-Consistency | Quality Assurance (High-Stakes) |
| QA-16 | Quality Rubric with Auto-Iteration | Prompt Improvement, Testing & Validation |
| QA-17 | Named Scores | Prompt Improvement, Testing & Validation |
| QA-21 | Metric Gaming Vector Enumeration | Agentic (Metric Gaming Pre-Mortem), Non-Engineering (Reward Systems) |
| QA-22 | Evaluation Diversity Planning | Agentic (Metric Gaming Pre-Mortem), Non-Engineering (Reward Systems) |

### CM — Context Management Techniques (10)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| CM-01 | Explicit Context Framing | Analysis, Decision, Planning (universal) |
| CM-02 | Constraint Specification | Creation, Compliance, Requirements |
| CM-03 | Scope Definition | Planning (Project Planning), Requirements |
| CM-04 | Summary-Expand Loop | Analysis (Architecture) |
| CM-05 | Progressive Context Accumulation | Agentic (Autonomous Execution) |
| CM-06 | Semantic Vector-Based Context Management | Agentic (large context) |
| CM-07 | Token-Budget-Aware Progressive Loading | Agentic (Autonomous Execution) |
| CM-08 | File-Based State Persistence | Agentic (Pipelines, Autonomous) |
| CM-09 | Authority Boundary Specification | Agentic (Autonomous Execution), Compliance |
| CM-10 | Memory Scaffold Architecture | Agentic (Pipelines, Autonomous) |

### RP — Role & Perspective Techniques (5)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| RP-01 | Expert Role Assignment | Analysis (Security), Decision (Architecture) |
| RP-02 | Audience-Specific Framing | Documentation, Teaching, Presentations |
| RP-03 | Multi-Persona Debate | Decision (Architecture, Strategic), Quality (High-Stakes) |
| RP-04 | Socratic Dialogue | Teaching (Explain, Code Review) |
| RP-05 | Temperature Simulation | Quality (High-Stakes) |

### DT — Decomposition Techniques (6)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| DT-01 | Hierarchical Task Breakdown | Planning, Analysis (Performance), Debugging |
| DT-02 | Specific Focus Areas with Examples | Analysis (Security, Code Quality), Test Generation |
| DT-03 | Iterative Refinement | Problem-Solving (Optimization) |
| DT-04 | Multi-Layer Analysis | Analysis (Code Quality) |
| DT-05 | Element-by-Element Assessment Matrix | Analysis (Code Quality), Testing |
| DT-06 | Typography Decision Tree | Visual Output (Worksheets) |

### ED — Educational Techniques (6)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| ED-01 | Iterative Scaffolding | Teaching (Interactive Teaching) |
| ED-02 | Progressive Exercise Generation | Teaching (Interactive Teaching) |
| ED-03 | Guided Discovery | Teaching (Interactive Teaching, Code Review) |
| ED-04 | Personalization Hooks | Teaching (Interactive Teaching) |
| ED-05 | Reference Class Priming | Teaching (Explain Code/Concept) |
| ED-06 | Example Quantity Specification | Teaching (Interactive Teaching) |

### MP — Meta-Prompting Techniques (8)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| MP-01 | Reverse Prompting | Prompt Improvement |
| MP-02 | Recursive Optimization | Prompt Improvement |
| MP-03 | Task Clarification | Problem-Solving (Debugging) |
| MP-04 | Strategic Edge Case Calibration | Prompt Improvement, Test Generation |
| MP-05 | Extended Thinking Documentation | Prompt Improvement |
| MP-06 | Fallback Question Protocol | Non-Engineering (Conversational) |
| MP-07 | Pattern Recognition Reflection | Problem-Solving (Root Cause) |
| MP-08 | Four-Layer Enhancement Process | Prompt Improvement |

### DS — Domain-Specific Techniques (42)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| DS-01 | Framework Application | Analysis (Business), Decision (Strategic) |
| DS-02 | Metric Specification | Analysis (Performance), Infrastructure (Financial) |
| DS-03 | Tool and Methodology Suggestions | Analysis (Performance) |
| DS-04 | Pattern Recognition Requests | Analysis (Business, Architecture), Planning |
| DS-05 | Visualization and Communication Guidance | Documentation |
| DS-06 | Prioritization and Severity Guidance | Analysis (all) |
| DS-13 | Architecture-First Enforcement | Analysis (Architecture) |
| DS-19 | Multi-Source Narrative Synthesis | Analysis (Business) |
| DS-20 | Frontier Mapping | Decision (Strategic Planning) |
| DS-21 | Proximity Assessment | Decision (Strategic Planning) |
| DS-22 | EARS Requirements Transformation | Infrastructure (Requirements) |
| DS-23 | Domain Theory Grounding | Documentation (Multi-Audience) |
| DS-24 | API Reference Bundling | Documentation (API), Non-Engineering (Developer) |
| DS-25 | Chart Selection Dictionary | Visual Output (Dashboards), Presentations |
| DS-26 | Safe Defaults Pattern | Creation (Configuration), Infrastructure (Cloud) |
| DS-27 | Professional Defaults Library | Creation (Configuration), Infrastructure (Cloud) |
| DS-28 | Environment-Specific Guidance | Creation (Configuration), Infrastructure (Cloud) |
| DS-29 | Domain Pattern Library | Creation (Configuration), Infrastructure (Database) |
| DS-30 | Ecosystem Mapping | Analysis (Architecture), Infrastructure (Cloud) |
| DS-32 | Regulatory Enumeration Pattern | Compliance, Infrastructure (Cloud) |
| DS-33 | Jurisdiction-Adaptive Output | Compliance |
| DS-34 | Documentation-Driven Testing | Test Generation, Testing & Validation |
| DS-35 | LLM-as-Judge with Rubric | Test Generation, Testing & Validation |
| DS-36 | Blocker Escalation Framework | Problem-Solving (Incident Response) |
| DS-37 | Progressive Abstraction Transformation | Documentation (Multi-Audience) |
| DS-38 | Long-Form Documentation Process | Documentation (Multi-Audience) |
| DS-39 | Configuration-Driven Workflow Customization | Creation (Configuration) |
| DS-40 | Follow-Up Action Extraction | Analysis (Business) |
| DS-43 | Auto-Improvement Readiness Requirements Matrix | Agentic (Auto-Improvement Readiness Diagnostic, Trace Infrastructure & Observability Audit) |
| DS-44 | Medallion Architecture Layering | Infrastructure (Database) |
| DS-48 | Multi-Window Burn Rate Alerts | Infrastructure (Financial) |
| DS-50 | STRIDE-Per-Interaction Matrix | Analysis (Security), Infrastructure (Security) |
| DS-56 | PostgreSQL Data Type Selection Matrix | Infrastructure (Database) |
| DS-61 | Security Tier Classification | Analysis (Security), Infrastructure (Security) |
| DS-80 | Multi-Tiered Template Library | Creation (Code Generation) |
| DS-107 | Version-Specific Expertise | Creation (Code Generation) |
| DS-111 | External Methodology Compliance | Compliance, Creation (Configuration) |
| DS-113 | Async-First Design Principle | Analysis (Architecture) |
| DS-114 | Federation Architecture | Analysis (Architecture) |
| DS-117 | Polyglot Persistence | Infrastructure (Database) |
| DS-118 | Security-Default Behavioral Traits | Analysis (Security), Infrastructure (Security) |
| DS-133 | FinOps Architecture Integration | Infrastructure (Cloud, Financial) |
| DS-148 | TDD-First Development Pattern | Test Generation |

### AG — Agentic Techniques (32)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| AG-01 | Personality-First Role Definition | Agentic (Agent Personas) |
| AG-02 | Skeptical Default Stance | Agentic (Agent Personas) |
| AG-03 | Layered Mission Hierarchy | Agentic (Skills, Autonomous) |
| AG-04 | Behavioral Guardrails | Agentic (Personas, Autonomous) |
| AG-05 | Concrete Deliverable Templates | Agentic (Skills) |
| AG-06 | Memory & Learning Architecture | Agentic (Pipelines) |
| AG-07 | Pipeline Orchestration Patterns | Agentic (Pipelines) |
| AG-08 | Evidence-Based Decision Gates | Agentic (Pipelines) |
| AG-09 | Anti-Pattern & Failure Mode Embedding | Agentic (Skills) |
| AG-10 | Emotional Context Spectrum | Agentic (Personas) |
| AG-11 | Taxonomy-Based Classification | Agentic (Skills) |
| AG-12 | Quantitative Success Metrics | Agentic (Skills) |
| AG-13 | Parallel-Converge Orchestration | Agentic (Pipelines) |
| AG-14 | Cost-Aware Agent Orchestration | Agentic (Pipelines) |
| AG-15 | Staged Rollout with Automatic Rollback | Agentic (Pipelines) |
| AG-16 | Master Prompt for Autonomous Multi-Week Execution | Agentic (Autonomous) |
| AG-17 | Auto-Resume from Stateful Tracking | Agentic (Autonomous) |
| AG-18 | Meta-Skill Self-Reference | Agentic (Skills) |
| AG-19 | Time-Critical Response Protocol | Problem-Solving (Incident Response) |
| AG-20 | Meta-Skill Pattern (Discovery) | Agentic (Skills) |
| AG-21 | Orchestration with Dual-Path Output | Agentic (Pipelines) |
| AG-26 | AI-Augmented Expertise | Agentic (Personas) |
| AG-27 | End-State Task Specification | Agentic (Task Delegation, Autonomous) |
| AG-28 | Oversight-Risk Calibration | Agentic (Task Delegation, Risk Assessment) |
| AG-29 | Agent Loop Architecture | Agentic (Autonomous, Pipelines) |
| AG-30 | Research-First Behavior | Agentic (Skills) |
| AG-31 | Workflow Position Definition | Agentic (Skills) |
| AG-32 | Pre-Execution Risk Audit | Agentic (Task Delegation, Quality) |
| AG-33 | Feedback Signal Inventory | Agentic (Task Delegation, Autonomous, Auto-Improvement Readiness, Metric Pre-Mortem, Trace Audit) |
| AG-34 | Optimization Triplet Readiness Gating | Agentic (Auto-Improvement Readiness Diagnostic) |
| AG-35 | Trace Infrastructure Gap Audit | Agentic (Trace Infrastructure & Observability Audit) |
| AG-36 | Build-vs-Buy Observability Remediation | Agentic (Trace Infrastructure & Observability Audit) |

### NE — Non-Engineering Techniques (20)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| NE-01 | Single-Question Pacing | Non-Engineering (Conversational) |
| NE-02 | Phased Workflow Architecture | Non-Engineering (Conversational) |
| NE-03 | Input Template Scaffolding | Non-Engineering (Conversational) |
| NE-04 | Good vs Bad Example Calibration | Non-Engineering (Conversational) |
| NE-05 | Token Budget Control | Non-Engineering (Business Communication) |
| NE-06 | Self-Audit Requirements | Non-Engineering (Decision Support) |
| NE-07 | Emotional Validation First | Non-Engineering (Conversational) |
| NE-08 | Catchall Context Gathering | Non-Engineering (Conversational), Visual (Interview) |
| NE-09 | Scope Reduction Pressure | Decision (Strategic Planning), Non-Engineering (Decision Support) |
| NE-10 | Probability-Weighted Scenarios | Decision (Architecture), Non-Engineering (Decision Support) |
| NE-11 | Embedded Calculation Formulas | Non-Engineering (Decision Support), Infrastructure (Financial) |
| NE-12 | Cognitive Mode Framing | Non-Engineering (Conversational) |
| NE-13 | Technical-to-Business Translation | Non-Engineering (Business Communication) |
| NE-14 | Multi-Audience Documentation Targeting | Non-Engineering (Business Communication), Documentation |
| NE-15 | Data Storytelling Framework | Non-Engineering (Business Communication), Presentations |
| NE-16 | Non-Judgmental Comparison | Non-Engineering (Conversational, Decision Support) |
| NE-17 | Call-to-Action Mandatory Close | Non-Engineering (Business Communication), Presentations |
| NE-18 | Developer Experience Priority | Non-Engineering (Developer Content) |
| NE-19 | Documentation-as-Product Philosophy | Documentation, Non-Engineering (Developer Content) |
| NE-20 | Third-Party Handoff Package | Non-Engineering (Business Communication), Documentation |

### IT — Interaction Techniques (10)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| IT-19 | Three-Tier Information Loading | Documentation (API, Multi-Audience) |
| IT-20 | Progressive Example Complexity | Teaching (Explain), Documentation (API), Non-Engineering (Developer) |
| IT-21 | Use Case-Driven Documentation | Documentation (API), Non-Engineering (Developer) |
| IT-22 | Workflow Decision Matrix | Documentation (Troubleshooting) |
| IT-23 | Symptom-Based Troubleshooting | Problem-Solving (Debugging), Documentation (Troubleshooting) |
| IT-24 | Template-Based Educational Scaffolding | Teaching (Interactive Teaching) |
| IT-25 | Tool Hierarchy Guidance | Documentation (Troubleshooting) |
| IT-26 | Reference Catalog Pattern | Documentation (API) |
| IT-27 | Multi-Template Selection Guide | Documentation (API) |
| IT-35 | Mentor-Style Feedback | Teaching (Interactive Teaching, Code Review) |

### SV — Specialized Visual & Interview Techniques (17)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| SV-01 | Visual Output Specification | Visual Output (Dashboards, Worksheets), Presentations |
| SV-02 | Grouped Input Gathering | Visual Output (Dashboards), Visual (Interview) |
| SV-03 | Interview-to-Synthesis Pattern | Visual (Interview) |
| SV-05 | Printable Worksheet Output Format | Visual Output (Worksheets) |
| SV-06 | Confirmation-Before-Proceed | Visual Output (Dashboards), Visual (Interview) |
| SV-07 | Calculation Specification | Visual Output (Dashboards, Worksheets) |
| SV-08 | Tiered Discovery Questions | Visual (Interview) |
| SV-09 | Structured Deliverables with Headings | Visual Output (Dashboards) |
| SV-10 | Table Output Specification | Visual Output (Dashboards) |
| SV-11 | Terminology Steering | Image Generation (Print Materials, Infographics) |
| SV-12 | Grid Forcing + Enumerated Slots | Image Generation (Print Materials) |
| SV-13 | Constraint Redundancy | Image Generation (Print Materials, Infographics) |
| SV-14 | Negative Space Control | Image Generation (Print Materials, Infographics) |
| SV-15 | Allowed vs. Forbidden Distinction | Image Generation (Infographics, Print Materials) |
| SV-16 | Physical Context Anchoring | Image Generation (Print Materials) |
| SV-17 | Deliverables Locking | Image Generation (Print Materials, Infographics) |
| SV-18 | Image Validation Checklist | Image Generation (Print Materials, Infographics) |

### DD — Done Definition Techniques (8)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| DD-02 | Vague-to-Concrete Translation | Task Completion (Defining Done), Requirements |
| DD-03 | Fail-Fast Ordering | Task Completion (Defining Done), Planning, Incident Response |
| DD-04 | MVP Gates | Task Completion (Defining Done, Gate-Based), Planning |
| DD-05 | Human Review Flags | Task Completion (Defining Done) |
| DD-06 | Iteration Control | Task Completion (Defining Done, Gate-Based) |
| DD-07 | Self-Audit Table | Task Completion (Defining Done, Gate-Based) |
| DD-10 | Change Log Iteration | Task Completion (Defining Done) |
| DD-11 | BLOCKED Protocol | Task Completion (Defining Done, Gate-Based), Incident Response |

### DP — Delegation & Productivity Techniques (24)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| DP-01 | Tool vs. Colleague Shape Decision | AI Delegation |
| DP-02 | Refuse Path Protocol | Specification Writing |
| DP-03 | Anchored Scoring Scales | AI Delegation |
| DP-04 | Must-Not Constraints | Specification Writing |
| DP-05 | Stakes-Based Gate Policy | AI Delegation |
| DP-06 | Dominant Driver Identification | AI Delegation |
| DP-07 | Failure Mode Prediction | AI Delegation, Personal Execution |
| DP-08 | Role-Based Verification Assignment | AI Delegation |
| DP-09 | Single Primary Constraint | Productivity Bottleneck |
| DP-10 | Reframe Generation | Productivity Bottleneck |
| DP-11 | Safe Experiment Design | Productivity Bottleneck, Breaking Permission Loops |
| DP-12 | Over-Protection Diagnosis | Productivity Bottleneck |
| DP-13 | Kill Signal Definition | Breaking Permission Loops |
| DP-14 | Compressed Specification Format | Specification Writing |
| DP-15 | One-Day Default Rule | Breaking Permission Loops |
| DP-16 | Provisional Decision Message | Breaking Permission Loops |
| DP-17 | Distribution Wedge Selection | Distribution & Reach |
| DP-18 | Trust Deposits Definition | Distribution & Reach |
| DP-19 | Gate Check Pattern | AI Coaching, Multi-Audience Customization |
| DP-20 | Strict Coach Persona | AI Coaching |
| DP-21 | Consumable Artifact Requirement | AI Coaching, Personal Execution, Business Communication |
| DP-22 | Distribution Fallback | Personal Execution |
| DP-23 | Path Variants | Multi-Audience Customization |
| DP-24 | Done Fudge Prevention | Personal Execution |

### QS — Quality Systems Techniques (6)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| QS-01 | Training vs Rules Diagnosis | Quality Systems (Diagnosing, Team Training) |
| QS-02 | Checkable Rule Format | Quality Systems (Building Rules) |
| QS-03 | Micro-lesson Structure | Quality Systems (Team Training) |
| QS-04 | Drift vs Violation Distinction | Quality Systems (Building Rules, Weekly Monitoring) |
| QS-05 | Required Decisions Pattern | Quality Systems (Diagnosing, Weekly Monitoring) |
| QS-06 | Exception Template Design | Quality Systems (Building Rules) |

### MA — Multi-Agent Architecture Techniques (8)
| Code | Name | Primary Use Case Section(s) |
|------|------|-----------------------------|
| MA-01 | Multi-Agent Failure Taxonomy | Multi-Agent (Diagnosing) |
| MA-02 | Two-Tier Architecture | Multi-Agent (Design, Quality Control) |
| MA-03 | Worker Isolation | Multi-Agent (Design, Quality Control) |
| MA-04 | Tool Diet Pattern | Multi-Agent (Design, Session Management) |
| MA-05 | Session Lifecycle Design | Multi-Agent (Session Management) |
| MA-06 | Scope Boundary Test | Multi-Agent (Session Management) |
| MA-07 | Contention Risk Assessment | Multi-Agent (Diagnosing) |
| MA-08 | Judge Decision Rules | Multi-Agent (Quality Control) |

---

## Anti-Patterns to Avoid

**Don't:** Use too many techniques (causes confusion)
**Do:** Select 3-5 core techniques that work together

**Don't:** Skip output specification
**Do:** Always use ST-03 or OC-02/03 for clear output

**Don't:** Use vague instructions ("make it better")
**Do:** Use specific techniques with clear patterns

**Don't:** Forget context
**Do:** Use CM-01 to provide necessary background

**Don't:** Skip quality checks for important work
**Do:** Use QA-01 or QA-02 for critical outputs

**Don't:** Combine conflicting techniques (see [Known Conflicts](#known-conflicts))
**Do:** Check the differentiation guide when techniques seem similar

**Don't:** Apply techniques in random order
**Do:** Follow the [Universal Ordering](#universal-ordering-applies-to-all-prompts) (Context → Role → Structure → Reasoning → Domain → Output → Quality)

**Don't:** Use conversational techniques (NE) in single-shot prompts
**Do:** Match technique family to prompt type (single-shot vs interactive)

---

## AI Agent Workflow

When a user makes a request:

1. **Classify the request** into primary use case category
2. **Identify core need** (analysis? creation? decision? teaching? agent-building? conversational? visual?)
3. **Select 3-5 essential techniques** from that category
4. **Check differentiation guide** if any techniques seem overlapping
5. **Add quality techniques** if request is high-stakes
6. **Order techniques** following the combination ordering rules
7. **Check for conflicts** against the known conflicts table
8. **Combine techniques** into coherent prompt structure
9. **Validate** that all user requirements are addressed

**Remember:** Start simple, add complexity only as needed. Three well-chosen techniques beat seven poorly combined ones.
