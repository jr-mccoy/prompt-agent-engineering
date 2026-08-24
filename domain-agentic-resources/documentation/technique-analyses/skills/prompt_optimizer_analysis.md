# Technique Analysis: prompt-optimizer

**Resource Type:** Skill
**Path:** `claude-code-resources/skills/llm-application-dev/prompt-optimizer/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 0 scripts, 4 references (1,014 lines total), 0 assets

---

## Summary

This skill transforms vague prompts into precise specifications using **EARS (Easy Approach to Requirements Syntax)** methodology from Rolls-Royce. It's a **requirements engineering** approach applied to prompt optimization, combining formal specification techniques with domain theory grounding. Demonstrates **four-layer enhancement** and **theory-driven prompt design**.

---

## Identified Techniques

### Technique 1: EARS Syntax Transformation

- **Category:** NEW
- **Pattern:** Convert natural language to normative requirements using 5 patterns:
  1. Ubiquitous: "The system shall <action>"
  2. Event-driven: "When <trigger>, the system shall <action>"
  3. State-driven: "While <state>, the system shall <action>"
  4. Conditional: "If <condition>, the system shall <action>"
  5. Unwanted behavior: "If <condition>, the system shall prevent <unwanted action>"
- **Example from resource:**
  ```
  Before: "Create a reminder app with task management"

  After (EARS):
  1. When user creates a task, the system shall guide decomposition into executable sub-tasks
  2. When task deadline is within 30 minutes AND user has not started, the system shall send notification with sound alert
  3. When user completes a sub-task, the system shall update progress and provide positive feedback
  ```
- **Maps to existing:** NEW (requirements engineering methodology not in MASTER_TECHNIQUE_INDEX)
- **Effectiveness:** Transforms ambiguity into precision, creates testable specifications, borrowed from aerospace industry (Rolls-Royce)

### Technique 2: Domain Theory Grounding

- **Category:** NEW
- **Pattern:** Match requirements to established frameworks, then apply framework principles to features
- **Example from resource:**
  ```markdown
  **Common domain mappings:**
  - Productivity → GTD, Pomodoro, Eisenhower Matrix
  - Behavior Change → BJ Fogg Model (B=MAT), Atomic Habits
  - UX Design → Hick's Law, Fitts's Law, Gestalt Principles
  - Security → Zero Trust, Defense in Depth, Privacy by Design
  ```
- **Maps to existing:** NEW (not in MASTER_TECHNIQUE_INDEX)
- **Effectiveness:** Grounds prompts in proven theory, adds credibility, ensures best practices

### Technique 3: Four-Layer Enhancement Process

- **Category:** NEW
- **Pattern:** Systematic refinement through four stages:
  1. EARS syntax transformation (normative requirements)
  2. Domain theory grounding (framework application)
  3. Example extraction (concrete use cases)
  4. Structured prompt generation (Role/Skills/Workflows/Examples/Formats)
- **Example from resource:**
  ```markdown
  **Four-layer enhancement process:**
  1. EARS syntax transformation - Convert descriptive language to normative specifications
  2. Domain theory grounding - Apply relevant industry frameworks
  3. Example extraction - Surface concrete use cases with real data
  4. Structured prompt generation - Format using Role/Skills/Workflows/Examples/Formats framework
  ```
- **Maps to existing:** NEW (meta-process for prompt optimization)
- **Effectiveness:** Comprehensive, systematic, produces production-ready prompts

### Technique 4: Role/Skills/Workflows/Examples/Formats Framework

- **Category:** ST (Structural Techniques)
- **Pattern:** Standard five-section prompt structure
- **Example from resource:**
  ```markdown
  # Role
  [Specific expert role with domain expertise]

  ## Skills
  [5-8 skills aligned with domain theories]

  ## Workflows
  [Complete step-by-step process]

  ## Examples
  [Concrete examples with real data, not placeholders]

  ## Formats
  [Precise output specifications]
  ```
- **Maps to existing:** ST-04 (Structured Prompts) but with **specific five-section template**
- **Effectiveness:** Provides consistent structure, covers all prompt components

### Technique 5: Transformation Checklist (Quality Gates)

- **Category:** QA (Quality Assurance)
- **Pattern:** Systematic checklist for requirement transformation
- **Example from resource:**
  ```markdown
  **Transformation checklist:**
  - [ ] Identify implicit conditions and make explicit
  - [ ] Specify triggering events or states
  - [ ] Use precise action verbs (shall, must, should)
  - [ ] Add measurable criteria ("within 30 minutes", "at least 8 characters")
  - [ ] Break compound requirements into atomic statements
  - [ ] Remove ambiguous language ("user-friendly", "fast")
  ```
- **Maps to existing:** QA-01 (Validation Checklists) applied to prompt requirements
- **Effectiveness:** Ensures completeness, catches ambiguity, enforces standards

### Technique 6: Theory Citation for Credibility

- **Category:** NEW
- **Pattern:** Explicitly reference established frameworks/theories in prompts to add authority
- **Example from resource:**
  ```markdown
  **Selection process:**
  1. Identify primary domain from requirement keywords
  2. Match to 2-4 complementary theories
  3. Apply theory principles to specific features
  4. Cite theories in enhanced prompt for credibility
  ```
- **Maps to existing:** NEW (not in MASTER_TECHNIQUE_INDEX)
- **Effectiveness:** Increases trust in generated outputs, demonstrates domain expertise, leverages proven patterns

### Technique 7: Concrete Example Extraction

- **Category:** RT (Reasoning Techniques)
- **Pattern:** Generate specific examples with real data, not placeholders
- **Example from resource:**
  ```markdown
  Generate specific examples with real data:
  - User scenarios: "When user logs in on mobile device..."
  - Data examples: "Product: 'Laptop', Price: $999, Stock: 15"
  - Workflow examples: "Task: Write report → Sub-tasks: Research (2h), Draft (3h), Edit (1h)"

  Examples must be realistic, specific, varied (success/error/edge cases), and testable.
  ```
- **Maps to existing:** RT-07 (Few-Shot Examples) but with **emphasis on real data vs. placeholders**
- **Effectiveness:** Prevents generic examples, improves model understanding, enables testing

### Technique 8: Progressive Reference Loading (On-Demand Documentation)

- **Category:** IT (Interaction Techniques)
- **Pattern:** Four reference files loaded only when needed
- **Example from resource:**
  ```markdown
  ## Resources
  - references/ears_syntax.md (123 lines) - Complete EARS syntax rules
  - references/domain_theories.md (245 lines) - 40+ theories mapped to 10 domains
  - references/examples.md (321 lines) - Four complete transformation examples
  - references/advanced_techniques.md (325 lines) - Multi-stakeholder requirements

  **When to load references:**
  - EARS syntax clarification needed → ears_syntax.md
  - Domain theory selection requires extensive options → domain_theories.md
  - User requests multiple optimization examples → examples.md
  - Complex requirements with multiple stakeholders → advanced_techniques.md
  ```
- **Maps to existing:** IT-06 (Progressive Disclosure) / IT-15 (Hierarchical Reference Loading)
- **Effectiveness:** Reduces initial context load, scales to complex scenarios, provides depth on demand

### Technique 9: Measurable Success Criteria

- **Category:** DS (Domain-Specific)
- **Pattern:** Require quantifiable metrics in specifications
- **Example from resource:**
  ```markdown
  **Quality criteria:**
  - Actionable workflows: Clear inputs/outputs and decision points
  - Concrete examples: Real data, not "Example 1", "Example 2"
  - Measurable formats: Specific requirements, not "good design"

  **Do's:**
  ✅ Specify measurable criteria (numbers, timeframes, percentages)
  ```
- **Maps to existing:** DS-02 (Metric Specification)
- **Effectiveness:** Enables objective evaluation, removes subjectivity

### Technique 10: Atomic Requirement Decomposition

- **Category:** NEW
- **Pattern:** Break compound requirements into single-action statements
- **Example from resource:**
  ```markdown
  **Do's:**
  ✅ Break down compound requirements (one EARS statement per requirement)

  **Don'ts:**
  ❌ Don't mix multiple actions in one statement
  ```
- **Maps to existing:** NEW (requirements engineering principle not documented)
- **Effectiveness:** Improves testability, reduces ambiguity, enables independent verification

### Technique 11: Multi-Stakeholder Requirements

- **Category:** NEW
- **Pattern:** Create EARS statements for each user type/role
- **Example from resource:**
  ```markdown
  For complex scenarios, see references/advanced_techniques.md:
  - Multi-stakeholder requirements - EARS statements for each user type
  - Non-functional requirements - Performance, security, scalability with quantified thresholds
  - Complex conditional logic - Nested conditions with boolean operators
  ```
- **Maps to existing:** NEW (enterprise requirements pattern)
- **Effectiveness:** Handles complex systems with multiple user types, prevents conflicts

### Technique 12: Before/After Transformation Examples

- **Category:** OT (Output Techniques)
- **Pattern:** Show original requirement and optimized version side-by-side
- **Example from resource:**
  ```markdown
  ## Original Requirement
  [User's vague requirement]

  **Identified Issues:**
  - [Issue 1: e.g., "Lacks specific trigger conditions"]
  - [Issue 2: e.g., "No measurable success criteria"]

  ## EARS Transformation
  [Numbered list of EARS-formatted requirements]

  ## Enhanced Prompt
  [Complete Role/Skills/Workflows/Examples/Formats prompt]
  ```
- **Maps to existing:** OT-04 (Before/After Examples) but applied to **requirement transformation**
- **Effectiveness:** Demonstrates value of optimization, teaches users the methodology

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: EARS Requirements Transformation

- **Description:** Structured methodology for converting natural language to normative specifications using 5 patterns (Ubiquitous, Event-driven, State-driven, Conditional, Unwanted behavior)
- **Implementation:**
  1. Analyze original requirement for weaknesses (ambiguity, missing triggers, no constraints)
  2. Apply appropriate EARS pattern(s)
  3. Make implicit conditions explicit
  4. Add measurable criteria
  5. Decompose into atomic statements
- **Use case:** Transforming vague feature requests into testable specifications for LLM prompts
- **Example:**
  ```
  Before: "Build a dashboard"
  After:
  1. The system shall display key metrics on dashboard home screen
  2. When user selects a metric, the system shall show detailed breakdown with time-series graph
  3. If data is unavailable, the system shall display "No data" message with explanation
  4. While data is loading, the system shall show skeleton UI with loading indicator
  ```
- **Proposed category:** DS (Domain-Specific - Requirements Engineering)
- **Proposed code:** DS-21
- **Source:** Rolls-Royce methodology (2009)

### Pattern 2: Domain Theory Grounding

- **Description:** Systematically match requirements to established frameworks (GTD, BJ Fogg Model, Gestalt, etc.) and apply theory principles to prompt design
- **Implementation:**
  1. Identify primary domain from requirement keywords (productivity, UX, security, etc.)
  2. Select 2-4 complementary theories from domain catalog (40+ theories across 10 domains)
  3. Apply theory principles to specific features in prompt
  4. Cite theories explicitly for credibility and guidance
- **Use case:** Grounding prompts in proven frameworks, ensuring best practices, adding expert credibility
- **Example:**
  ```
  Requirement: "Build a habit-tracking app"

  Domain: Behavior Change
  Selected Theories:
  - BJ Fogg Model (B=MAT): Behavior = Motivation × Ability × Trigger
  - Atomic Habits: Make it obvious, easy, attractive, satisfying

  Applied Principles:
  - Reduce ability requirements (make habits easier to start)
  - Increase trigger effectiveness (timely notifications)
  - Provide satisfaction (streaks, progress visualization)
  ```
- **Proposed category:** ST (Structural Techniques - Framework Integration)
- **Proposed code:** ST-26
- **Source:** A-Xing AI Studio methodology

### Pattern 3: Four-Layer Prompt Enhancement

- **Description:** Systematic refinement process: EARS transformation → Domain grounding → Example extraction → Structured generation
- **Implementation:**
  1. **Layer 1**: Transform natural language to EARS requirements
  2. **Layer 2**: Ground in domain theories (select 2-4 frameworks)
  3. **Layer 3**: Extract concrete examples with real data
  4. **Layer 4**: Generate structured prompt (Role/Skills/Workflows/Examples/Formats)
- **Use case:** Comprehensive prompt optimization from vague to production-ready
- **Example:**
  ```
  Input: "Make a todo app"

  Layer 1 (EARS): "When user creates task, system shall enable priority assignment..."
  Layer 2 (Theory): Apply GTD (capture, clarify, organize, reflect, engage)
  Layer 3 (Examples): "Task: 'Buy groceries', Priority: High, Due: Today 5pm, Tags: [errands, shopping]"
  Layer 4 (Structured): Full Role/Skills/Workflows/Examples/Formats prompt
  ```
- **Proposed category:** MP (Meta-Prompting)
- **Proposed code:** MP-06
- **Source:** Combined EARS + A-Xing methodology

### Pattern 4: Theory Citation for Credibility

- **Description:** Explicitly reference established frameworks/methodologies in prompts to add authority and guide LLM outputs
- **Implementation:**
  - Identify 2-4 relevant theories for the domain
  - Cite theories by name in prompt structure
  - Apply theory principles to specific requirements
  - Use theory terminology to guide LLM behavior
- **Use case:** Professional/enterprise prompts requiring expert credibility, complex domains with established best practices
- **Example:**
  ```
  Role: UX Designer specializing in mobile productivity apps

  Skills:
  - Apply Hick's Law to minimize decision complexity
  - Implement Gestalt principles (proximity, similarity, continuity) for visual hierarchy
  - Follow Fitts's Law for touch target sizing (minimum 44×44 pt)
  - Design using BJ Fogg Behavior Model (B=MAT) for habit formation
  ```
- **Proposed category:** ST (Structural Techniques)
- **Proposed code:** ST-27
- **Source:** Professional requirements engineering practice

### Pattern 5: Atomic Requirement Decomposition

- **Description:** Break compound requirements into single-action, independently testable statements (one action per EARS statement)
- **Implementation:**
  - Identify compound requirements ("The system shall X and Y and Z")
  - Decompose into separate EARS statements
  - Ensure each statement has one clear action
  - Verify each statement is independently testable
- **Use case:** Complex feature specifications, requirements with multiple actions/conditions
- **Example:**
  ```
  Before (Compound):
  "When user submits form, validate inputs, save to database, send email, and redirect to success page"

  After (Atomic):
  1. When user submits form, the system shall validate all required fields
  2. When validation passes, the system shall save form data to database
  3. When database save succeeds, the system shall send confirmation email to user
  4. When email queues successfully, the system shall redirect user to success page
  ```
- **Proposed category:** DS (Domain-Specific - Requirements Engineering)
- **Proposed code:** DS-22
- **Source:** Requirements engineering best practice

---

## Multi-Technique Combinations

### Combination 1: EARS + Domain Theory + Concrete Examples
- **Technique Stack:** DS-21 (novel) + ST-26 (novel) + RT-07
- **Combination Purpose:** Transform vague requirements into theoretically-grounded, testable specifications
- **Flow:**
  1. Apply EARS transformation to create normative requirements
  2. Ground requirements in domain theories (GTD, BJ Fogg, etc.)
  3. Generate concrete examples demonstrating theory application
- **Synergies:** EARS provides structure, theories provide guidance, examples provide clarity

### Combination 2: Four-Layer Enhancement + Progressive Loading
- **Technique Stack:** MP-06 (novel) + IT-15 + DS-02
- **Combination Purpose:** Systematic prompt optimization with on-demand knowledge
- **Flow:**
  1. Start with simple EARS transformation
  2. Load domain theories reference if needed (245 lines)
  3. Load examples reference if user requests (321 lines)
  4. Load advanced techniques for complex cases (325 lines)
- **Synergies:** Minimizes context while providing depth, scales to complexity

### Combination 3: Atomic Decomposition + Measurable Criteria + Transformation Checklist
- **Technique Stack:** DS-22 (novel) + DS-02 + QA-01
- **Combination Purpose:** Ensure requirement quality and testability
- **Flow:**
  1. Break compound requirements into atomic statements
  2. Add measurable criteria to each statement
  3. Verify with transformation checklist
- **Synergies:** Decomposition enables testing, metrics enable measurement, checklist ensures completeness

### Combination 4: Theory Citation + Role/Skills/Workflows Framework + Before/After Examples
- **Technique Stack:** ST-27 (novel) + ST-04 + OT-04
- **Combination Purpose:** Professional prompt generation with demonstrated improvement
- **Flow:**
  1. Show original vague requirement
  2. Apply theories to create expert role with theory-grounded skills
  3. Structure with Role/Skills/Workflows/Examples/Formats
  4. Present before/after comparison
- **Synergies:** Demonstrates value, teaches methodology, produces professional output

---

## Notes for Integration

### Add to MASTER_TECHNIQUE_INDEX:
1. **DS-21: EARS Requirements Transformation** - Rolls-Royce methodology for normative specifications
2. **ST-26: Domain Theory Grounding** - Framework-based prompt design
3. **MP-06: Four-Layer Prompt Enhancement** - Systematic EARS + Theory + Examples + Structure
4. **ST-27: Theory Citation for Credibility** - Explicit framework references
5. **DS-22: Atomic Requirement Decomposition** - Single-action testable statements

### Update USE_CASE_LOOKUP:
- **Use Case: Prompt Optimization** - Add EARS methodology as primary technique
- **Use Case: Requirements Engineering** - Add this skill as bridge between software engineering and prompting
- **Use Case: Enterprise Prompts** - Reference theory grounding for professional credibility

### Cross-reference with prompts:
- **engineering/ prompts** - EARS methodology applicable to feature specifications
- **improvement/ prompts** - Four-layer enhancement process for refactoring
- **business-analysis/ prompts** - Domain theory grounding for business requirements

### Documentation improvements:
1. **AI_AGENT_QUICK_START.md** - Add section on requirements engineering for prompts
2. **New guide**: "From Requirements to Prompts: EARS Methodology"
3. **Reference materials**: Consider extracting domain_theories.md as standalone guide (40+ theories)

### Best practices:
1. **Use EARS patterns** for any requirement specification in prompts
2. **Ground in 2-4 theories** for complex domains (not just one)
3. **Atomic decomposition** improves testability and clarity
4. **Real data in examples** (not placeholders like "Example 1")
5. **Theory citation** adds credibility in professional/enterprise contexts
6. **1,000+ lines of references** shows value of bundled deep knowledge

---

## Analysis Metadata

**Analyzer:** Claude (Task 2.2 Priority 2 - Skills Analysis)
**Analysis Duration:** 25 minutes
**Confidence Level:** High
**Review Status:** Draft
**Priority for Integration:** **Very High** (requirements engineering methodology, 5 novel techniques, foundational for enterprise prompting)

---

## Technique Complexity Score

**Score: 5/5** (Maximum Complexity)

**Rationale:**
- Uses 12+ distinct techniques
- 5 novel patterns not in existing index
- Borrows from aerospace engineering (Rolls-Royce EARS)
- Four-layer systematic enhancement process
- 1,014 lines of bundled deep knowledge (domain theories, examples, advanced techniques)
- Meta-level methodology (optimizes other prompts)
- Combines multiple disciplines (requirements engineering, domain expertise, prompt engineering)

---

## Key Insights

1. **Requirements engineering meets prompting**: EARS methodology from aerospace/automotive (Rolls-Royce) successfully adapted to prompt optimization. This is a **novel cross-disciplinary application**.

2. **Theory grounding is underutilized**: The 40+ theories (GTD, BJ Fogg, Gestalt, Hick's Law, etc.) mapped to 10 domains show systematic approach to framework integration - not commonly documented in prompting resources.

3. **Four-layer process is comprehensive**: EARS transformation → Theory grounding → Example extraction → Structured generation covers all aspects of professional prompt development.

4. **Atomic decomposition enables testing**: Breaking compound requirements into single-action statements is fundamental to software engineering but rarely applied to prompts.

5. **Bundled deep knowledge scales**: 1,014 lines of reference material (theories, syntax rules, examples, advanced techniques) demonstrates how skills can package extensive domain expertise without context bloat.

6. **Real data vs. placeholders**: Explicit emphasis on concrete examples with real data ("Product: 'Laptop', Price: $999" vs. "Product: Example1") significantly improves LLM understanding.

7. **Meta-methodology**: This skill teaches **how to optimize prompts**, making it a meta-prompting resource like prompt-engineering-patterns.

---

## Recommendations

1. **Document EARS methodology** as high-priority technique (DS-21) - foundational for enterprise/professional prompting
2. **Extract domain theories catalog** as standalone resource - 40+ theories is valuable reference
3. **Create "Requirements Engineering for Prompts" guide** combining EARS + other techniques
4. **Add EARS examples** to AI_AGENT_QUICK_START.md for specification tasks
5. **Cross-reference with business-analysis/** prompts - EARS improves requirement clarity
6. **Consider creating EARS template** as reusable asset for prompt specifications
7. **Document theory citation pattern** (ST-27) for professional/enterprise use cases
