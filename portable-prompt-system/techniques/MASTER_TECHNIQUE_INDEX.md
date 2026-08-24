# Master Prompt Engineering Technique Index

**Last Updated:** 2026-04-19
**Purpose:** Comprehensive catalog of all prompt engineering techniques used across this repository, organized for AI agent reference and human learning.
**Total Techniques:** 293 formally defined techniques across 19 categories, with 55 analysis files documenting technique usage across agentic resources
**Recent Additions:** Technique catalog has grown across multiple 2026 revisions. See per-category sections below for current coverage; changelog entries prior to the public-release cleanup have been consolidated into the repository history.

---

## Table of Contents

**Quick Navigation:**
- [Naming Conventions](#naming-conventions) *(NEW - ID prefixes, base/variant patterns)*
- [Quick Reference by Use Case](#quick-reference-by-use-case)
- [Technique Families](#technique-families) *(grouped by function)*

**Technique Categories:**
1. [Structural Techniques](#structural-techniques)
2. [Reasoning Techniques](#reasoning-techniques)
3. [Output Control Techniques](#output-control-techniques)
4. [Quality Assurance Techniques](#quality-assurance-techniques)
5. [Context Management Techniques](#context-management-techniques)
6. [Role & Perspective Techniques](#role--perspective-techniques)
7. [Decomposition Techniques](#decomposition-techniques)
8. [Educational Techniques](#educational-techniques)
9. [Meta-Prompting Techniques](#meta-prompting-techniques)
10. [Domain-Specific Techniques](#domain-specific-techniques)
11. [Agentic Techniques](#agentic-techniques)
12. [Non-Engineering Techniques](#non-engineering-techniques)
13. [Interaction Techniques](#interaction-techniques) *(NEW - documentation structure, examples, troubleshooting)*
14. [Specialized Visual & Interview Techniques](#specialized-visual--interview-techniques)
15. [Done Definition Techniques](#done-definition-techniques)
16. [Delegation & Productivity Techniques](#delegation--productivity-techniques)

---

## Naming Conventions

Standards for naming techniques to maintain consistency and clarity.

### ID Prefix Reference

| Prefix | Category | Scope |
|--------|----------|-------|
| **ST** | Structural | Prompt architecture and organization |
| **RT** | Reasoning | Thinking patterns and logic |
| **OC** | Output Control | Format and structure of outputs |
| **QA** | Quality Assurance | Verification and validation |
| **CM** | Context Management | Information gathering and state |
| **RP** | Role & Perspective | Persona and viewpoint definition |
| **DT** | Decomposition | Task breakdown and analysis |
| **ED** | Educational | Teaching and learning patterns |
| **MP** | Meta-Prompting | Prompts about prompts |
| **DS** | Domain-Specific | Specialized domain patterns |
| **AG** | Agentic | Multi-agent and autonomous behavior |
| **NE** | Non-Engineering | Business, decision, productivity |
| **IT** | Interaction | Documentation structure, examples, troubleshooting |
| **SV** | Specialized Visual | Visual outputs and interviews |
| **DD** | Done Definition | Task completion verification |
| **DP** | Delegation & Productivity | Delegation and efficiency |
| **QS** | Quality Systems | Process quality and organizational entropy |
| **MA** | Multi-Agent Architecture | Multi-agent design and coordination |

### Base Technique vs Variant Pattern

When techniques have a general form and specialized applications:

**Base Technique (General)**
```
{ID}: {Descriptive Name}
Example: RT-05: Evidence-Based Reasoning
```

**Specialized Variant**
```
{ID}: {Base Name} - {Specialization}
Example: RT-05 includes "Evidence-Location Pattern" as a variant
```

**Naming Rules:**
1. **Base techniques** use broad, descriptive names
   - ✅ "Evidence-Based Reasoning" (general concept)
   - ✅ "Output Format Specification" (general concept)
   - ❌ "Code Evidence Pattern" (too specific for base)

2. **Variants** indicate their specialization
   - ✅ "Evidence-Location Pattern" (specializes location format)
   - ✅ "JSON Schema Specification" (specializes to JSON)
   - ❌ "Better Evidence" (unclear differentiation)

3. **When to create variant vs new technique:**
   - **Variant:** Same core concept, different implementation
   - **New technique:** Different core concept, even if related

### Merge Documentation Pattern

When techniques are merged, document with:

```markdown
### {ID}: {Name} *(Merged from {ID-A} + {ID-B})*
...
**Note:** Merged {ID-B} into {ID-A} ({DATE}) — {reason for merge}
```

**Example:**
```markdown
### ST-03: Output Format Specification *(Merged from ST-03 + OC-01)*
**Note:** Merged OC-01 into ST-03 (2026-01-22) — OC-01 was a specialized variant of ST-03
```

### Deprecation Pattern

When a technique is deprecated in favor of another:

```markdown
### {ID}: {Name} → **Merged into {TARGET-ID}** *({DATE})*
**Status:** DEPRECATED — Use {TARGET-ID}: {Target Name} instead
**Reason:** {Why this was merged/deprecated}
**See:** {TARGET-ID} in {Section Name} section
```

**Example:**
```markdown
### SV-04: Domain Framework Application → **Merged into DS-01** *(2026-01-22)*
**Status:** DEPRECATED — Use DS-01: Framework Application instead
**Reason:** SV-04 was an advanced variant of DS-01 with parameter definitions; now unified
**See:** DS-01 in Domain-Specific Techniques section
```

### Disambiguation Pattern

When techniques are similar but distinct, include:

```markdown
**Different from {OTHER-ID} ({Other Name}):** {Clear distinction}
```

**Examples:**
- `**Different from RP-01:** Includes memory, experience, and failure awareness—not just expertise assignment`
- `**Different from ST-02 (Sequential Instructions):** Phases are dialogue-based with user interaction, not sequential AI actions`

---

## Quick Reference by Use Case

**Need analysis of complex code?** → Structured Sequential Instructions + Multi-Dimensional Analysis + Evidence-Based Reasoning
**Need to teach/explain concepts?** → Socratic Dialogue + Iterative Scaffolding + Audience-Specific Framing
**Need strategic business insights?** → Framework Application + Multi-Persona Analysis + SWOT/Matrix Patterns
**Need reliable output format?** → Explicit Output Specification + JSON Schema + Template Provision
**Need creative problem solving?** → Tree of Thoughts + Analogical Reasoning + Multi-Approach Generation
**Need self-correcting responses?** → Chain-of-Verification + Adversarial Stress-Test + Reflection Loops
**Need multi-agent orchestration?** → Pipeline Orchestration (AG-07) + Evidence-Based Gates (AG-08) + Personality-First Roles (AG-01)
**Need quality gate enforcement?** → Skeptical Default Stance (AG-02) + Anti-Pattern Embedding (AG-09) + Quantitative Metrics (AG-12)
**Need interactive dialogue?** → Single-Question Pacing (NE-01) + Phased Workflow Architecture (NE-02) + Emotional Validation First (NE-07)
**Need structured user input?** → Input Template Scaffolding (NE-03) + Catchall Context Gathering (NE-08)
**Need decision support?** → Scope Reduction Pressure (NE-09) + Probability-Weighted Scenarios (NE-10) + Embedded Calculation Formulas (NE-11)
**Need executive dashboards/visualizations?** → Visual Output Specification (SV-01) + Grouped Input Gathering (SV-02) + Calculation Specification (SV-07)
**Need educational worksheets?** → Interview-to-Synthesis (SV-03) + Printable Worksheet Format (SV-05) + Audience-Specific Framing (RP-02)
**Need AI system correctness?** → Tiered Discovery Questions (SV-08) + Structured Deliverables (SV-09) + Framework Application (DS-01)
**Need advertising/marketing creative?** → Interview-to-Synthesis (SV-03) + Visual Output Specification (SV-01) + Expert Role Assignment (RP-01)
**Need focus/productivity analysis?** → Framework Application (DS-01) + Table Output Specification (SV-10) + Confirmation-Before-Proceed (SV-06)
**Need personal productivity system?** → File-Based State Persistence (CM-08) + Fallback Question Protocol (MP-06) + Output Contract Structure (OC-06)
**Need stateful AI assistant?** → Memory Scaffold Architecture (CM-10) + Authority Boundary Specification (CM-09) + Pattern Recognition Reflection (MP-07)
**Need AI visual production quality control?** → Frontier Mapping (DS-20) + Test Battery Protocol (QA-10) + Pass/Fail Test Harness (QA-11) + Failure Recovery Specification (QA-13)
**Need strategic capability assessment?** → Cascade Effect Analysis (RT-07) + Proximity Assessment (DS-21) + False Positives Identification (QA-12) + Workaround Cost Analysis (RT-08)
**Need production workflow with quality gates?** → Gate-Based Workflow Validation (QA-08) + Element-by-Element Assessment Matrix (DT-05) + Reversibility Assessment (QA-09)
**Need verifiable task completion?** → Gate-Based Verification (QA-08) + Self-Audit Table (DD-07) + MVP Gates (DD-04) + Iteration Control (DD-06)
**Need to prevent false completion claims?** → Evidence-Based Reasoning (RT-05) + Iteration Control (DD-06) + Change Log Iteration (DD-10)
**Need AI delegation decisions?** → Tool/Colleague Shape Decision (DP-01) + Stakes-Based Gate Policy (DP-05) + Role-Based Verification (DP-08)
**Need productivity bottleneck diagnosis?** → Single Primary Constraint (DP-09) + Reframe Generation (DP-10) + Over-Protection Diagnosis (DP-12)
**Need to break permission loops?** → One-Day Default Rule (DP-15) + Provisional Decision Message (DP-16) + Safe Experiment Design (DP-11)
**Need tight specifications?** → Must-Not Constraints (DP-04) + Compressed Specification (DP-14) + Kill Signal Definition (DP-13)
**Need personal agency/execution system?** → Gate Check Pattern (DP-19) + Strict Coach Persona (DP-20) + Distribution Fallback (DP-22) + Done Fudge Prevention (DP-24)
**Need better AI communication?** → Multi-Lens Request Framing (CM-12) + Expert Friend Positioning (RP-06) + Principled Pushback Navigation (IT-10) + Non-Default Behavior Activation (IT-11)
**Need system prompt design?** → Reasoning-Based Constraint Design (CM-11) + Principal Hierarchy Specification (CM-14) + Gap-Filling Intent Signaling (CM-15) + Dual-Failure Quality Test (QA-20)
**Need to handle AI pushback?** → Principled Pushback Navigation (IT-10) + Distinguishing Context Provision (CM-13) + Non-Default Behavior Activation (IT-11)
**Need AI coaching without generic advice?** → Gate Check Pattern (DP-19) + Strict Coach Persona (DP-20) + Consumable Artifact Requirement (DP-21)
**Need quality system that prevents recurring mistakes?** → Training vs Rules Diagnosis (QS-01) + Checkable Rule Format (QS-02) + Drift vs Violation (QS-04)
**Need team training on rules/principles?** → Micro-lesson Structure (QS-03) + Training vs Rules Diagnosis (QS-01)
**Need multi-agent system design?** → Multi-Agent Failure Taxonomy (MA-01) + Two-Tier Architecture (MA-02) + Worker Isolation (MA-03)
**Need to debug multi-agent problems?** → Multi-Agent Failure Taxonomy (MA-01) + Contention Risk Assessment (MA-07)
**Need agent session management?** → Session Lifecycle Design (MA-05) + Scope Boundary Test (MA-06) + Tool Diet (MA-04)
**Need multi-agent quality control?** → Judge Decision Rules (MA-08) + Two-Tier Architecture (MA-02) + Worker Isolation (MA-03)
**Need pre-delegation validation?** → Pre-Delegation Dual Check (DP-32) + Multi-Lens Problem Diagnostic (DP-27) + Intent Gap Analysis (DP-26)
**Need intent engineering for AI tasks?** → Intent Gap Analysis (DP-26) + Value Hierarchy Construction (DP-29) + Constraint Gap Mapping (DP-31)
**Need team AI delegation risk assessment?** → Autonomy-Risk Matrix (DP-30) + Intent Gap Analysis (DP-26) + Traffic-Light Verdict System (DP-28)
**Need troubleshooting documentation?** → Symptom-Based Troubleshooting (IT-23) + Root Cause Explanation (RT-09) + Troubleshooting Decision Tree (RT-10)
**Need multi-audience documentation?** → Multi-Audience Documentation Targeting (NE-14) + Progressive Abstraction Transformation (DS-37) + Data Storytelling Framework (NE-15)
**Need API/library documentation?** → Progressive Example Complexity (IT-20) + Use Case-Driven Documentation (IT-21) + External Reference Catalog (OC-12)
**Need configuration generation?** → Safe Defaults Pattern (DS-26) + Professional Defaults Library (DS-27) + Environment-Specific Guidance (DS-28) + Configuration-Driven Workflow Customization (DS-39)
**Need incident response protocols?** → Time-Critical Response Protocol (AG-19) + Blocker Escalation Framework (DS-36) + Root Cause Explanation (RT-09)
**Need compliance/regulatory guidance?** → Regulatory Enumeration Pattern (DS-32) + Jurisdiction-Adaptive Output (DS-33) + Mandatory Disclaimer Pattern (OC-10)
**Need prompt improvement?** → Four-Layer Enhancement Process (MP-08) + Quality Rubric with Auto-Iteration (QA-16) + Named Scores (QA-17)
**Need handoff/onboarding docs?** → Third-Party Handoff Package (NE-20) + Documentation-as-Product Philosophy (NE-19) + Capability Boundary Specification (OC-09)
**Need to improve AI communication?** → Position Mapping (MP-10) + Pre-AI Thinking Protocol (MP-09) + Correction Compounding (MP-11)
**Need to evaluate AI output quality?** → Domain-Specific Smell Tests (QA-18) + Personal Eval Harness (QA-19) + Named Scores (QA-17)
**Need to delegate to AI agents?** → Four-Quadrant Constraint Architecture (DP-25) + Reasoning-Based Constraint Design (CM-11) + Authority Boundary Specification (CM-09)
**Need to assess AI readiness of work?** → Difficulty Axis Decomposition (DS-41) + Position Mapping (MP-10) + Pre-AI Thinking Protocol (MP-09)
**Need system prompt design for Claude?** → Reasoning-Based Constraint Design (CM-11) + Authority Boundary Specification (CM-09) + Behavioral Guardrails (AG-04)
**Need strategic expansion analysis?** → Suppressed Opportunity Surfacing (NE-21) + Constraint Inversion Analysis (NE-22) + Cost of Inaction Framing (NE-27)
**Need to unlock hidden organizational value?** → Suppressed Opportunity Surfacing (NE-21) + Adjacent Opportunity Inference (RT-12) + Insight-to-Action Chain Mapping (NE-24)
**Need board-ready persuasion?** → Objection Pre-emption (NE-23) + Cost of Inaction Framing (NE-27) + Historical Parallel Argumentation (NE-26)
**Need domain expert → builder conversion?** → Domain Knowledge Extraction Protocol (DS-42) + Side-by-Side Workflow Comparison (NE-25) + Phased Workflow Architecture (NE-02)
**Need workflow bottleneck diagnosis?** → Insight-to-Action Chain Mapping (NE-24) + Side-by-Side Workflow Comparison (NE-25) + Constraint Inversion Analysis (NE-22)
**Need to delegate a task to an AI agent?** → End-State Task Specification (AG-27) + Feedback Signal Inventory (AG-33) + Oversight-Risk Calibration (AG-28)
**Need to design an agent loop?** → Agent Loop Architecture (AG-29) + Feedback Signal Inventory (AG-33) + End-State Task Specification (AG-27)
**Need pre-flight check before agent work?** → Pre-Execution Risk Audit (AG-32) + Oversight-Risk Calibration (AG-28) + End-State Task Specification (AG-27)

---

## Technique Families

Related techniques grouped by functional purpose. Use this to find alternatives or complementary techniques.

### Role Definition Family
*Techniques for defining AI persona, expertise, and behavior*

| Technique | Focus | Use When |
|-----------|-------|----------|
| **RP-01** Expert Role Assignment | Domain expertise only | Simple expert persona needed |
| **AG-01** Personality-First Role Definition | Full persona with memory, experience, personality | Persistent agent with learned behavior |
| **NE-12** Cognitive Mode Framing | Cognitive/reasoning stance | Setting creative vs analytical mode |
| **ST-16** Behavioral Trait Declarations | Interaction style, behavioral traits | Explicit behavior separate from expertise |
| **AG-26** AI-Augmented Expertise | AI tool fluency as core skill | Modern AI-native workflows |

**Spectrum:** Basic expertise (RP-01) → Full persona (AG-01) → Cognitive framing (NE-12) → Behavioral traits (ST-16) → AI-augmented (AG-26)

---

### Context/Input Collection Family
*Techniques for gathering information from users before processing*

| Technique | Approach | Use When |
|-----------|----------|----------|
| **CM-01** Explicit Context Framing | Prose context upfront | User provides structured background |
| **NE-03** Input Template Scaffolding | Fill-in-the-blank fields | Need specific data points |
| **NE-08** Catchall Context Gathering | Open-ended brain dump | User has unstructured info |
| **SV-02** Grouped Input Gathering | Numbered GROUP sections | Complex multi-category inputs |
| **MP-03** Task Clarification | AI asks questions | Requirements are unclear |

**Spectrum:** Structured (NE-03, SV-02) ↔ Unstructured (NE-08, CM-01) | Passive (user provides) ↔ Active (MP-03 asks)

---

### Workflow Organization Family
*Techniques for structuring task execution flow*

| Technique | Scope | Use When |
|-----------|-------|----------|
| **ST-02** Structured Sequential Instructions | Single AI, numbered steps | AI executes steps autonomously |
| **NE-02** Phased Workflow Architecture | AI + user dialogue phases | Interactive workflow with user |
| **DT-01** Hierarchical Task Breakdown | Planning/decomposition | Breaking down complex tasks |
| **AG-07** Pipeline Orchestration Patterns | Multi-agent coordination | Autonomous multi-agent workflows |

**Spectrum:** Single AI execution (ST-02) → Interactive dialogue (NE-02) → Planning only (DT-01) → Multi-agent (AG-07)

---

### Output Specification Family
*Techniques for defining output format and structure*

| Technique | Format Type | Use When |
|-----------|-------------|----------|
| **ST-03** Output Format Specification | General requirements + templates | Most output formatting needs |
| **OC-02** JSON Schema Specification | JSON structure | Structured data output |
| **OC-03** Markdown Table Specification | Table structure | Tabular data |
| **OC-06** Output Contract Structure | 5-part standard format | Consistent deliverables |
| **SV-01** Visual Output Specification | Image/visual requirements | Visual artifacts |
| **SV-09** Structured Deliverables with Headings | Named sections A-F | Document structure |
| **SV-10** Table Output Specification | Specific column tables | Data presentation |

**Base technique:** ST-03 (general) | **Specialized variants:** OC-02 (JSON), OC-03 (tables), SV-01 (visual)

---

### Self-Verification Family
*Techniques for AI reviewing its own output*

| Technique | Approach | Use When |
|-----------|----------|----------|
| **QA-01** Chain-of-Verification | Structured self-critique with evidence | Rigorous verification needed |
| **NE-06** Self-Audit Requirements | Explicit checkpoints (SELF-AUDIT →) | Quick quality checks |
| **DD-07** Self-Audit Table | Structured table with evidence + location | Documented verification |
| **QA-06** Constitutional AI for Prompts | Critique-revise loops against principles | Iterative improvement |

**Spectrum:** Single review (QA-01, NE-06) ↔ Iterative improvement (QA-06) | Lightweight (NE-06) ↔ Documented (DD-07)

---

### Constraint/Guardrail Family
*Techniques for defining boundaries and restrictions*

| Technique | Focus | Use When |
|-----------|-------|----------|
| **CM-02** Constraint Specification | Must/must-not/should/should-not | General input/output constraints |
| **AG-04** Behavioral Guardrails | Non-negotiable behavioral rules | Agent consistency, safety |
| **DP-04** Must-Not Constraints | Negative constraints (at least 2) | Preventing specific behaviors |

**Distinction:** CM-02 (general constraints) vs AG-04 (behavioral directives) vs DP-04 (explicit prohibitions)

---

### Evidence Requirements Family
*Techniques for requiring proof and citations*

| Technique | Focus | Use When |
|-----------|-------|----------|
| **RT-05** Evidence-Based Reasoning | File paths, line numbers, quotes | Code analysis, verification |
| **AG-08** Evidence-Based Decision Gates | Visual/quantitative proof for approvals | Quality gates, approvals |

**Distinction:** RT-05 (general evidence) vs AG-08 (approval-specific gates)

---

### Example Calibration Family
*Techniques for using examples to set quality expectations*

| Technique | Approach | Use When |
|-----------|----------|----------|
| **ED-05** Reference Class Priming | Single excellent example | "Match this quality" |
| **NE-04** Good vs Bad Example Calibration | Contrast pairs (bad → good) | "Here's what NOT to do" |
| **MP-04** Strategic Edge Case Calibration | Baseline + failure + edge case | "Here are the edge cases" |

**Spectrum:** Quality benchmark (ED-05) → Contrast learning (NE-04) → Boundary definition (MP-04)

---

### Scope Management Family
*Techniques for defining and controlling scope*

| Technique | Direction | Use When |
|-----------|-----------|----------|
| **CM-03** Scope Definition | Define boundaries | Setting initial scope |
| **NE-09** Scope Reduction Pressure | Challenge and reduce | Fighting scope creep |

**Distinction:** CM-03 (definition) vs NE-09 (reduction)

---

### Iteration Control Family
*Techniques for managing loops and stopping conditions*

| Technique | Focus | Use When |
|-----------|-------|----------|
| **DD-06** Stop Policy | Escalation triggers, iteration limits | Controlling retry behavior |
| **DD-10** Change Log Iteration | Track changes each iteration | Debugging iteration loops |
| **QA-13** Failure Recovery Specification | Rules for handling failures | Error recovery patterns |

**Distinction:** DD-06 (when to stop) vs DD-10 (what changed) vs QA-13 (how to recover)

---

### Multi-Layer Analysis Family
*Techniques for analyzing at multiple levels of depth*

| Technique | Layers | Use When |
|-----------|--------|----------|
| **DT-04** Layered Analysis Structure | Micro (issues) + macro (trends) | Code/system analysis |
| **DT-05** Element-by-Element Assessment Matrix | Systematic component evaluation | Comprehensive audits |

**Distinction:** DT-04 (depth layers) vs DT-05 (breadth coverage)

---

### Gate/Approval Family
*Techniques for verification checkpoints*

| Technique | Stance | Use When |
|-----------|--------|----------|
| **QA-08** Gate-Based Verification | Binary pass/fail tests | Workflow stage gates |
| **DP-05** Stakes-Based Gate Policy | Gates scale with risk | Variable-risk workflows |
| **AG-02** Skeptical Default Stance | Default to failure, require proof | Final approvals, quality gates |

**Spectrum:** Neutral gates (QA-08) → Risk-scaled (DP-05) → Skeptical default (AG-02)

---

### Documentation Organization Family
*Techniques for structuring documentation and reference materials*

| Technique | Approach | Use When |
|-----------|----------|----------|
| **IT-20** Progressive Example Complexity | Simple → advanced examples | API/library documentation |
| **IT-21** Use Case-Driven Documentation | "I want to..." task-oriented | Product/tool documentation |
| **IT-22** Workflow Decision Matrix | Scenario → workflow routing | Multiple workflow options |
| **IT-23** Symptom-Based Troubleshooting | Symptom → cause → fix | Debugging guides |
| **IT-24** Template-Based Educational Scaffolding | TODO markers with guidance | Template creation |
| **IT-25** Tool Hierarchy Guidance | Prefer A → Fallback B → Last resort C | DevOps tooling |
| **IT-26** Reference Catalog Pattern | Categorized resource catalog | Pattern/tool inventories |
| **IT-27** Multi-Template Selection Guide | Selection criteria for templates | Multiple template variants |

**Spectrum:** Example-based (IT-20) → Task-based (IT-21) → Decision-based (IT-22) → Symptom-based (IT-23) → Template-based (IT-24)

---

### Troubleshooting Family
*Techniques for diagnosing and resolving problems*

| Technique | Direction | Use When |
|-----------|-----------|----------|
| **RT-09** Root Cause Explanation | Cause → symptoms → fix | Root cause is known |
| **RT-10** Troubleshooting Decision Tree | Symptom → diagnostic → branch | Step-by-step diagnosis |
| **IT-23** Symptom-Based Troubleshooting | Symptom index → causes | User searches by symptom |

**Spectrum:** Cause-first (RT-09) → Diagnostic tree (RT-10) → Symptom index (IT-23)

---

### Quality Scoring Family
*Techniques for measuring and improving output quality*

| Technique | Approach | Use When |
|-----------|----------|----------|
| **QA-11** Pass/Fail Test Harness | Binary pass/fail | Simple verification |
| **QA-17** Named Scores | Multi-dimensional scoring | Quality decomposition |
| **QA-16** Quality Rubric with Auto-Iteration | Score + auto-iterate | Self-improving output |
| **DS-35** LLM-as-Judge | Independent evaluator | Cross-model evaluation |

**Spectrum:** Binary (QA-11) → Scored (QA-17) → Self-improving (QA-16) → Independent judge (DS-35)

---

### AI Interaction Optimization Family
*Techniques for improving the quality of human-AI communication and building compound improvements*

| Technique | Focus | Use When |
|-----------|-------|----------|
| **MP-09** Pre-AI Thinking Protocol | Human-only thinking before AI | Starting any significant AI task |
| **MP-10** Position Mapping | Articulating your deviation from median | Writing custom instructions for the first time |
| **MP-11** Correction Compounding | Extracting patterns from corrections | Noticing repeated corrections to AI output |
| **CM-11** Reasoning-Based Constraint Design | Converting rules to reasoning | Designing system prompts or CLAUDE.md files |
| **QA-18** Domain-Specific Smell Tests | Building field-specific AI checks | Evaluating AI output in your domain |
| **QA-19** Personal Eval Harness | Recurring AI task benchmarking | Testing across model updates |

**Spectrum:** Pre-thinking (MP-09) → Self-awareness (MP-10) → Instruction design (CM-11, MP-11) → Output evaluation (QA-18, QA-19)

---

### Delegation & Constraint Family
*Techniques for defining boundaries when delegating to AI agents or team members*

| Technique | Scope | Use When |
|-----------|-------|----------|
| **CM-02** Constraint Specification | General must/must-not/should | Setting input/output constraints |
| **CM-09** Authority Boundary Specification | Action permissions (can/ask/never) | Defining what agent can do |
| **DP-04** Must-Not Constraints | Explicit prohibitions | Preventing specific behaviors |
| **DP-25** Four-Quadrant Constraint Architecture | Must/Must-Not/Prefer/Escalate | Full delegation constraint design |
| **DP-07** Failure Mode Prediction | Pre-identifying wrong outcomes | Risk assessment before delegation |
| **DS-41** Difficulty Axis Decomposition | Categorizing task difficulty type | Deciding what to delegate to AI |
| **DP-26** Intent Gap Analysis | Instruction vs intent gap discovery | Pre-delegation intent audit |
| **DP-27** Multi-Lens Problem Diagnostic | Multi-lens problem validation | Validating problem before delegation |
| **DP-29** Value Hierarchy Construction | Ranked tradeoff resolution values | Encoding judgment preferences |
| **DP-30** Autonomy-Risk Matrix | 2D risk mapping of delegations | Team AI audit |
| **DP-31** Constraint Gap Mapping | Failure scenarios → constraints | Deriving constraints from failures |
| **DP-32** Pre-Delegation Dual Check | Problem + intent paired validation | Quick preflight before AI handoff |

**Spectrum:** What to delegate (DS-41) → Validate problem (DP-27, DP-32) → Discover intent gaps (DP-26) → Derive constraints (DP-31, DP-25) → Encode values (DP-29) → Assess risk (DP-30) → Define permissions (CM-09)

---

### Strategic Expansion Analysis Family
*Techniques for uncovering hidden opportunities and building the case for growth over contraction*

| Technique | Focus | Use When |
|-----------|-------|----------|
| **NE-21** Suppressed Opportunity Surfacing | Uncovering self-censored ideas | Org is defaulting to cost-cutting frame |
| **NE-22** Constraint Inversion Analysis | Re-evaluating under changed constraints | Key cost/resource constraint has shifted |
| **RT-12** Adjacent Opportunity Inference | Inferring unstated related opportunities | User's explicit input is incomplete |
| **NE-23** Objection Pre-emption | Anticipating counterarguments | Building persuasive strategic cases |
| **NE-24** Insight-to-Action Chain Mapping | Mapping bottlenecks in execution chains | Diagnosing organizational slowness |
| **NE-25** Side-by-Side Workflow Comparison | Current vs redesigned workflow display | Making improvement impact visible |
| **NE-26** Historical Parallel Argumentation | Using tech shift parallels as evidence | Strategic persuasion about inflection points |
| **NE-27** Cost of Inaction Framing | Modeling consequences of not acting | Decision-makers are risk-averse |
| **DS-42** Domain Knowledge Extraction Protocol | Extracting tacit domain expertise | Non-engineers have buildable knowledge |

**Spectrum:** Surface hidden value (NE-21, RT-12) → Re-evaluate economics (NE-22, NE-27) → Map execution gaps (NE-24, NE-25) → Build persuasive case (NE-23, NE-26) → Extract builder knowledge (DS-42)

---

## Structural Techniques

### ST-01: Clear Objective Statement
**What:** Concise, unambiguous opening that defines the task's purpose
**Pattern:** `**Objective:** [Single sentence defining desired outcome]`
**Used in:** All code-analysis prompts, business analysis, engineering workflows
**Example:** "**Objective:** Analyze the codebase to identify areas with high cyclomatic complexity"
**Why it works:** Immediately frames the AI's focus and sets clear success criteria
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #1

### ST-02: Structured Sequential Instructions
**What:** Numbered, step-by-step instructions that break complex tasks into subtasks
**Pattern:**
```
1. [First action - typically data gathering]
2. [Second action - analysis]
3. [Third action - synthesis]
4. [Fourth action - recommendations]
```
**Used in:** 85+ prompts across all categories
**Best Practice:** Use 3-7 numbered steps, with sub-bullets for additional detail
**Why it works:** Provides logical workflow that prevents missing critical steps
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #2
**Different from NE-02:** ST-02 is AI executing steps autonomously; NE-02 involves user interaction between phases
**Different from DT-01:** ST-02 is execution instructions; DT-01 is planning/decomposition without execution
**Different from AG-07:** ST-02 is single AI; AG-07 coordinates multiple agents
**See Also:** NE-02 (dialogue-based phases), DT-01 (task decomposition), AG-07 (multi-agent orchestration)

### ST-03: Output Format Specification *(Merged from ST-03 + OC-01)*
**What:** Dedicated section describing format, structure, and content requirements—including exact formatting templates
**Pattern (Requirements-Based):**
```
**Expected Output:** A comprehensive report that includes:
1. Overview of findings
2. Detailed breakdowns
3. Concrete recommendations
```
**Pattern (Template-Based):**
```
Files:
- [file path 1]
- [file path 2]
Length: [number of duplicated lines]
Impact: [impact description]
Suggestions:
- [suggestion 1]
- [suggestion 2]
```
**Variants:**
- **Requirements-based:** Describe what sections/content to include
- **Template-based:** Provide exact structure to fill in
**Used in:** All code-analysis, most business-analysis, quality reports
**Why it works:** Eliminates ambiguity about deliverable format and content; ensures consistency and completeness
**Note:** Merged OC-01 into ST-03 (2026-01-22) — OC-01 was a specialized variant of ST-03
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` techniques #3, #6

### ST-04: Delimited Sections
**What:** Clear separators that mark section boundaries — both for organizing a multi-part *response* and for delimiting *injected input content* (pasted code, documents, data, transcripts, examples) so the model does not conflate it with instructions
**Pattern (output sectioning — markdown headers):**
```
## Section 1 Name
[Content]

## Section 2 Name
[Content]
```
**Pattern (input delimiting — named XML-style tags):**
```
Review the code in <codebase> and cite file:line for each finding.

<codebase>
[pasted code injected at use time]
</codebase>
```
Tag names: lowercase snake_case, descriptive, on their own lines; reference them by name in the instructions ("the code in `<codebase>`," not "the code above"). A markdown header inside a pasted file is indistinguishable from one the author wrote — tags remove that ambiguity. Cross-vendor safe: Anthropic recommends XML tags; OpenAI's GPT-5.x guidance uses markdown headers plus XML-style tags. Use it to make output *more consistent* and reduce *structural* ambiguity — it does not make a probabilistic model deterministic.
**Used in:** Business analysis, strategic frameworks (output sectioning); any prompt that consumes pasted content (input delimiting)
**Best for:** Reports with distinct logical sections; separating instructions from injected material
**See Also:** `domain-prompt-engineering/structured-output/structured_xml_tag_pattern.md` (tag conventions and parser regexes for output tagging), `authoring/PROMPT_STRUCTURE_GUIDE.md` (when and how to delimit injected content)
**Reference:** `comprehensive_prompting_patterns.md` pattern #6

### ST-05: Hierarchical Organization
**What:** Nested structure with main points and sub-points
**Pattern:** Uses a., b., c. sub-bullets under numbered items
**Used in:** SWOT analysis, framework applications
**Best for:** Complex multi-dimensional analysis

### ST-16: Behavioral Trait Declarations
**What:** Explicit declaration of agent behavioral traits separate from domain expertise
**Pattern:**
```markdown
## Behavioral Traits
- **Communication Style**: [concise | thorough | conversational | formal]
- **Challenge Level**: [supportive | questioning | adversarial]
- **Risk Tolerance**: [conservative | balanced | aggressive]
- **Default Stance**: [optimistic | neutral | skeptical]

### Interaction Behaviors
- Always [behavior 1]
- Never [behavior 2]
- When uncertain, [default action]
```
**Used in:** Agent persona definition, consistent UX design, team-specific customization
**Why it works:** Makes behavior explicit and predictable; allows fine-tuning interaction style without changing expertise; enables composability (same expertise with different behaviors)
**Example:** A "senior engineer" (RP-01) could have traits like "always challenges assumptions" and "prefers concise responses" (ST-16) layered on top
**Different from RP-01:** ST-16 defines *how* the AI behaves and interacts; RP-01 defines *what* the AI knows
**Different from AG-01:** ST-16 focuses only on behavioral traits; AG-01 includes memory, experience, and full persona beyond just traits
**Different from NE-12:** ST-16 defines interaction style and behaviors; NE-12 sets cognitive/reasoning mode (analytical vs creative)
**Reference:** Extracted from agency-agents patterns; used across HAIKU-class agents
**See Also:** RP-01 (basic expertise), AG-01 (full persona with memory), NE-12 (cognitive mode), AG-26 (AI-augmented expertise)

### ST-40: Three-Tier Value Classification
**What:** Categorize content into three tiers (Keep/Condense/Delete) with color coding or labeling to guide content management decisions
**Pattern:**
```markdown
For each item, classify into one of three tiers:

**KEEP (Tier 1):** High-value content — preserve as-is
- Criteria: [what makes content high-value]

**CONDENSE (Tier 2):** Moderate-value content — summarize or restructure
- Criteria: [what makes content worth keeping in reduced form]

**DELETE (Tier 3):** Low-value content — remove entirely
- Criteria: [what makes content removable]
```
**Used in:** Documentation cleanup, code review (keep/refactor/delete), knowledge base curation, meeting agenda prioritization
**Why it works:** Forces explicit triage decisions on every item; the three tiers cover all possible outcomes (keep, reduce, remove) without ambiguity
**Different from ST-22:** ST-22 compares competing approaches; ST-40 categorizes existing content for retention decisions
**Reference:** Technique Deduplication Audit, Batch 5

### ST-42: Criticality Labeling
**What:** Use semantic bold prefixes (e.g., **CRITICAL:**, **WARNING:**, **INFO:**) to visually signal priority level inline within flowing text
**Pattern:**
```markdown
**CRITICAL:** This setting must be configured before deployment — failure causes data loss.
**WARNING:** Default timeout is 30s; increase for large datasets.
**INFO:** Optional parameter; defaults to UTF-8 encoding.
```
**Used in:** Reports, documentation, code review feedback, configuration files, operational runbooks
**Why it works:** Enables rapid scanning of mixed-priority content without requiring readers to parse full paragraphs; severity labels create visual hierarchy
**Different from DS-06:** DS-06 ranks findings into ordered lists by severity; ST-42 labels items inline within flowing text
**Reference:** Technique Deduplication Audit, Batch 7b

### ST-43: Risk-Stratified Documentation
**What:** Embed risk levels directly within documentation so that recommendations carry explicit risk context
**Pattern:**
```markdown
### Recommendation: Migrate to new authentication service
**RISK LEVEL: HIGH** — Requires 2-hour maintenance window
**Mitigation:** Schedule during off-peak hours; prepare rollback script
**Dependencies:** Database migration (LOW RISK) must complete first

### Recommendation: Update logging format
**RISK LEVEL: LOW** — No downtime required
**Mitigation:** None needed; backward-compatible change
```
**Used in:** Infrastructure changes, security recommendations, migration guides, architectural decisions, deployment procedures
**Why it works:** Prevents high-risk actions from being buried among low-risk items; readers can prioritize review effort based on risk tags
**Different from ST-42:** ST-42 uses inline labels for general priority; ST-43 specifically embeds risk assessment with mitigation into documentation structure
**Reference:** Technique Deduplication Audit, Batch 7a

### ST-44: Progressive Complexity Scaffolding
**What:** Build artifacts progressively from minimal viable version to production-grade, with each layer adding complexity; the minimal version must work independently
**Pattern:**
```markdown
## Tier 1: Minimal Viable (works out of the box)
[Basic implementation — functional, no frills]

## Tier 2: Standard (common production needs)
[Add error handling, logging, basic monitoring]

## Tier 3: Production-Grade (enterprise requirements)
[Add HA, security hardening, observability, compliance]

## Tier 4: Enterprise (scale and governance)
[Add multi-region, audit trails, RBAC, SLA guarantees]
```
**Used in:** Code generation, infrastructure templates, documentation, API design, configuration files, tutorial creation
**Why it works:** Each tier is independently useful; users start with what works and upgrade incrementally rather than facing production complexity upfront
**Different from ED-01:** ED-01 teaches concepts one at a time; ST-44 builds *artifacts* progressively with each tier being a complete working version
**Different from DS-80:** DS-80 provides templates at different levels; ST-44 is a process pattern for building artifacts incrementally
**Reference:** Technique Deduplication Audit, Batch 9

### ST-45: Methodology-Centric Expertise
**What:** Define an agent or prompt's identity around a specific methodology (e.g., TDD, DDD, SRE, Lean) rather than a role title, making the methodology the organizing principle for all recommendations
**Pattern:**
```markdown
You are a **Test-Driven Development** practitioner. Every recommendation you make
must be filtered through TDD principles:

## Core Tenets
1. Write the test first — no implementation without a failing test
2. Write the minimum code to pass — no speculative features
3. Refactor only after green — never refactor and add features simultaneously

## Decision Filter
For any suggestion, verify:
- Does this follow Red-Green-Refactor? If not, restructure.
- Would a TDD practitioner approve this sequence? If not, reorder.
```
**Used in:** TDD coach, SRE advisor, Lean consultant, Agile facilitator, security-first architect, DDD practitioner
**Why it works:** Methodology-centered identity produces more consistent and principled outputs than role-based identity; the methodology acts as a built-in decision filter
**Different from RP-01:** RP-01 assigns a role ("senior engineer"); ST-45 structures identity around a methodology which constrains all recommendations
**Reference:** Technique Deduplication Audit, Batch 2

### ST-46: Assertion-Evidence Content Structure
**What:** Structure content using the Pyramid Principle: lead with the assertion (conclusion), then provide supporting evidence; every section starts with its main point
**Pattern:**
```markdown
## Finding: Cache hit rate is critically low at 23%

**Evidence:**
- Redis monitoring shows 77% miss rate over last 7 days
- P95 latency increased from 120ms to 890ms since cache degradation began
- Database query volume tripled, indicating cache bypass

**Impact:** Estimated 40% increase in infrastructure costs and degraded user experience

**Recommendation:** Implement cache warming strategy and increase TTL for stable data
```
**Used in:** Executive summaries, presentation slides, code review feedback, architecture decision records, business communication
**Why it works:** Readers get the key point immediately; supporting detail is available for those who need it; prevents burying conclusions at the end of analysis
**Different from ST-05:** ST-05 defines hierarchical structure but not content ordering; ST-46 mandates conclusion-first ordering within each section
**Reference:** Technique Deduplication Audit, Batch 9

---

## Reasoning Techniques

### RT-01: Chain-of-Thought (CoT)
**What:** Explicit instruction to show step-by-step reasoning
**Trigger Phrases:** "Think through this step-by-step", "Let's work through this", "Show your reasoning"
**Used in:** Meta-prompting patterns, complex analysis
**Impact:** 40-60% improvement in reasoning accuracy (Wei et al., 2022)
**Reference:** `comprehensive_prompting_patterns.md` pattern #3
**Example Prompts:** Problem-solving, debugging, optimization

**Cross-Platform Notes:**
- **Claude:** Explicit CoT typically helps and is recommended for complex reasoning
- **GPT-5/5.2:** Built-in router handles CoT automatically—explicit CoT is often redundant. For forced reasoning, use `gpt-5-thinking` or `gpt-5-thinking-mini` model variants instead
- **GPT-5.2-Codex:** Use sparingly for pure code generation—can slow output without accuracy gains
- **GPT-4:** Optional; generally beneficial but not required
- **o1/o1-mini:** Omit explicit CoT—these models use implicit internal reasoning; adding explicit CoT can degrade performance
- **General:** Test with and without on your target model; newer models increasingly internalize reasoning

### RT-02: Multi-Dimensional Analysis Framework
**What:** Instructions to analyze from multiple perspectives
**Dimensions:** Location, Description, Impact, Severity, Recommendations
**Pattern:**
```
For each identified issue, analyze:
a. Location: File path, Line number(s)
b. Description: Brief explanation
c. Impact: Effect on [quality attribute]
d. Severity: Minor vs. Major
e. Recommendations: How to fix
```
**Used in:** All code-analysis categories
**Why it works:** Ensures thorough, actionable analysis
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #5

### RT-03: Tree of Thoughts
**What:** Generate multiple approaches and compare them
**Pattern:**
```
Generate 3 different approaches:
Approach 1: [Description]
Pros: [Advantages]
Cons: [Disadvantages]
[Repeat for 2-3 approaches]
Based on analysis, the best approach is [selection] because [reasoning]
```
**Used in:** Strategic planning, architecture decisions
**Best for:** Problems with multiple valid solutions
**Reference:** `comprehensive_prompting_patterns.md` pattern #9

### RT-04: Analogical Reasoning
**What:** Explain concepts through analogies from familiar domains
**Pattern:** "Explain [concept] by finding an analogy from [domain]"
**Used in:** Learning prompts, educational contexts
**Best for:** Teaching complex technical concepts
**Reference:** `comprehensive_prompting_patterns.md` pattern #11

### RT-05: Evidence-Based Reasoning *(Merged from RT-05 + DD-08)*
**What:** Require specific evidence with explicit locations for all claims—prevents vague generalities
**Pattern (Code-Focused):** "For each finding, provide: file path, line numbers, code examples"
**Pattern (Location-Focused):**
```markdown
Location = where to find the evidence. Acceptable formats:
- Heading name: "Competitor B → Why it matters"
- Page number: "p. 3"
- Quote snippet: "We recommend..."
- Paragraph reference: "Executive Summary, para 2"
- Line number: "lines 45-52"
- File path: "src/utils/validation.ts"
```
**Use Cases:** Code analysis, security reviews, self-audit tables, verification workflows
**Why it works:** Ensures rigor; agent cannot claim evidence exists without specifying location; makes lazy self-reports harder
**Note:** Merged DD-08 into RT-05 (2026-01-22) — both require evidence with locations
**Variant — Evidence-Based Investigation Methodology:** Adds systematic investigation methodology (hypothesis → evidence → conclusion) on top of evidence requirements. Use when the task involves diagnostic investigation, not just evidence citation.
**Variant — Sequential Evidence Gathering:** Gather evidence in order of diagnostic value (most discriminating first), not alphabetically or by ease. Prioritized investigation sequences reduce time-to-diagnosis.

### RT-06: Correlation and Cross-Analysis
**What:** Combine multiple data sources or metrics
**Pattern:** "Correlate [metric A] with [metric B] to identify [insight]"
**Used in:** Code evolution, technical debt, performance analysis
**Example:** "Correlate churn analysis with complexity metrics"
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #14

### RT-07: Cascade Effect Analysis
**What:** Mapping first-order, second-order, and third-order effects
**Category:** Reasoning Techniques
**Use Case:** Strategic planning, capability assessment, investment analysis, systems thinking
**Pattern:**
```markdown
PART 3: CASCADE POTENTIAL

For each gap, map the downstream unlocks:

FIRST-ORDER (Direct)
- What products or workflows become viable the moment this is solved?
- Who ships first? (Companies positioned to move immediately)

SECOND-ORDER (Built on first-order)
- What becomes possible once the first-order products exist?
- What new categories emerge?

THIRD-ORDER (If applicable)
- How deep could this cascade go?
- What's the ceiling on value creation?
```
**Why it works:** Reveals non-obvious compounding effects
**Three orders:** Direct → Built on direct → Deeper implications

### RT-08: Workaround Cost Analysis
**What:** Document current solutions and their costs to validate real problems
**Category:** Reasoning Techniques
**Use Case:** Problem validation, strategic planning, opportunity assessment
**Pattern:**
```markdown
THE WORKAROUND
- How do people currently handle this?
- What's the cost? (Time, money, quality, scale ceiling)

THE TELL
- How do you know this is a real blocker and not just a preference?
- Who's complaining about this? What are they saying?
```
**Why it works:** Distinguishes real pain from theoretical problems
**Two components:** Current solution + cost AND validation signal
**Cost dimensions:** Time, money, quality, scale ceiling

### RT-09: Root Cause Explanation Pattern
**What:** Structure troubleshooting explanations as: Root Cause → Symptoms → Explanation → Fix; work backward from cause to observable symptoms, then forward to resolution
**Pattern:**
```markdown
**Root Cause:** [The actual underlying problem]

**Observable Symptoms:**
1. [What the user sees/experiences]
2. [Error messages or metrics that indicate the problem]

**Causal Chain:**
Root cause → [intermediate effect 1] → [intermediate effect 2] → Observable symptoms

**Fix:** [Solution targeting the root cause, not the symptoms]

**Verification:** [How to confirm the root cause is resolved]
```
**Used in:** Debugging, incident postmortems, performance analysis, infrastructure troubleshooting, diagnostic tasks
**Why it works:** Forces causal reasoning rather than symptom-chasing; the backward-then-forward structure ensures fixes address the root cause
**Different from RT-02:** RT-02 analyzes from multiple perspectives; RT-09 specifically traces causal chains for troubleshooting
**Variant:** Symptom-Diagnostic-Fix Pattern — approaches from symptom-first (user's entry point) rather than cause-first. Use RT-09 when the cause is known; use IT-23 when starting from symptoms.
**See Also:** IT-23 (Symptom-Based Troubleshooting Organization), RT-10 (Troubleshooting Decision Tree)
**Reference:** Technique Deduplication Audit, Batches 4 and 8

### RT-10: Troubleshooting Decision Tree
**What:** Organize troubleshooting as a decision tree: Symptom → Diagnostic Command → Possible Cause → Fix, with branching paths based on diagnostic results
**Pattern:**
```markdown
**Symptom:** Application returns 503 errors

├── Run: `kubectl get pods -n production`
│   ├── Pods in CrashLoopBackOff → **Cause:** OOM kills
│   │   └── **Fix:** Increase memory limits; check for memory leaks
│   ├── Pods in Pending → **Cause:** Insufficient resources
│   │   └── **Fix:** Scale node pool or reduce resource requests
│   └── Pods Running → Continue to next check
│
├── Run: `kubectl logs <pod> --tail=100`
│   ├── Connection refused errors → **Cause:** Upstream service down
│   │   └── **Fix:** Check upstream service health; restart if needed
│   └── Timeout errors → **Cause:** Network policy or DNS issue
│       └── **Fix:** Verify network policies; check CoreDNS logs
```
**Used in:** Infrastructure debugging, application troubleshooting, customer support scripts, hardware diagnostics
**Why it works:** Each branch point has an executable diagnostic step, making troubleshooting systematic rather than guess-and-check
**Different from DT-06:** DT-06 uses binary decisions for classification; RT-10 applies decision trees specifically to troubleshooting with executable diagnostics at each branch
**See Also:** RT-09 (Root Cause Explanation), IT-23 (Symptom-Based Troubleshooting)
**Reference:** Technique Deduplication Audit, Batch 9

### RT-11: Error Recovery Patterns for Prompts
**What:** Define explicit recovery strategies for when LLM outputs fail: retry with rephrased instruction, fallback to simpler request, escalate to human, or gracefully degrade output
**Pattern:**
```markdown
**Expected Output:** [Description of correct output]

**Failure Mode 1:** Model returns generic/unhelpful response
- **Detection:** Response lacks specific details or code examples
- **Recovery:** Rephrase with more specific constraints and examples
- **Fallback:** Request a simpler version (list instead of full implementation)

**Failure Mode 2:** Model hallucinates non-existent APIs
- **Detection:** Function names don't match known API surface
- **Recovery:** Provide explicit API reference and retry
- **Fallback:** Ask model to use only stdlib functions

**Failure Mode 3:** Model refuses to complete task
- **Detection:** Response includes refusal language
- **Recovery:** Rephrase to clarify legitimate use case
- **Fallback:** Escalate to human for manual completion
```
**Used in:** Multi-step prompt chains, evaluation pipelines, automated content generation, agentic workflows
**Why it works:** Prevents cascading failures in prompt pipelines; each failure mode has a pre-planned recovery path rather than ad-hoc debugging
**Different from QA-13:** QA-13 handles agent/system failures; RT-11 specifically addresses LLM output quality failures within prompting workflows
**See Also:** QA-13 (Failure Recovery Specification), AG-07 (Pipeline Orchestration)
**Reference:** Technique Deduplication Audit, Batch 6

### RT-12: Adjacent Opportunity Inference
**What:** Going beyond the user's explicit input to infer related opportunities, options, or considerations they likely haven't considered — then transparently flagging inferred items so the user can validate
**Category:** Reasoning
**Use Case:** Strategic planning, opportunity analysis, brainstorming, comprehensive audits
**Pattern:**
```markdown
Using everything the user shared, identify [opportunities/options/considerations]. Go beyond what the user explicitly stated — infer adjacent [items] they likely haven't considered based on their [industry/context/constraints].

For each inferred item, flag clearly as "inferred based on your [context]" so the user can validate.
```
**Used in:** Strategic audits, market analysis, risk assessment, architecture review
**Why it works:** Users are constrained by their current frame; this technique systematically expands the solution space while maintaining trust through transparency. The flagging mechanism prevents hallucination from being mistaken for user-provided information.
**Different from RT-04 (Analogical Reasoning):** RT-04 uses analogies from other domains; RT-12 infers unstated items within the user's own domain based on contextual patterns
**Different from NE-08 (Catchall Context Gathering):** NE-08 gathers what the user knows; RT-12 generates what they haven't considered

---

## Output Control Techniques

### OC-01: Output Format Templates → **Merged into ST-03** *(2026-01-22)*
**Status:** DEPRECATED — Use ST-03: Output Format Specification instead
**Reason:** OC-01 was a specialized variant of ST-03's output specification pattern
**See:** ST-03 in Structural Techniques section above (now includes template-based variant)

### OC-02: JSON Schema Specification
**What:** Provide exact JSON structure expected
**Pattern:**
```
Respond ONLY with valid JSON in this exact format:
{
  "field1": "type and description",
  "field2": ["array", "of", "values"],
  "nested": {
    "field3": "description"
  }
}
```
**Used in:** API integrations, structured data extraction
**Best practices:** Use CAPS for "ONLY", specify types, provide enum values
**Reference:** `comprehensive_prompting_patterns.md` pattern #4
**Different from ST-03:** OC-02 specifies machine-readable JSON; ST-03 covers general format requirements
**Different from OC-03:** OC-02 outputs JSON; OC-03 outputs markdown tables

### OC-03: Markdown Table Specification
**What:** Specify table structure with column headers
**Pattern:**
```
Output as a markdown table with these columns:
| Column1 | Column2 | Column3 |
```
**Used in:** Comparative analysis, feature matrices
**Best for:** Comparing multiple items across dimensions
**Reference:** `comprehensive_prompting_patterns.md` pattern #5
**Different from OC-02:** OC-03 outputs human-readable tables; OC-02 outputs machine-readable JSON
**Different from SV-10:** OC-03 is generic table format; SV-10 specifies domain-specific columns for dashboards

### OC-04: Conditional Output Logic
**What:** Instructions for what to output when nothing found
**Pattern:** "If no significant issues are found, provide a summary stating [acceptable state]"
**Used in:** Quality analysis, security scans
**Why it works:** Prevents awkward responses when expected issues aren't present
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #9

### OC-05: Minimum Length Requirements
**What:** Specify minimum depth or length to prevent oversimplification
**Pattern:** "Minimum length: 1500 words" or "Provide at least 5 detailed paragraphs per section"
**Used in:** Deep analysis, comprehensive reports
**Why it works:** Fights model's trained instinct toward brevity
**Reference:** `advanced_prompting_techniques.md` - Deliberate Over-Instruction

### OC-06: Output Contract Structure
**What:** Standardized 5-part output format for predictable structure
**Category:** Output Control
**Use Case:** All prompts requiring actionable, verifiable outputs
**Pattern:**
```markdown
### What I Understood
[Restates your input]

### What I'm Producing
[Names the deliverable]

### The Output
[The actual thing]

### Open Questions
[Unresolved items, if blocking]

### Next Action
[What to do now, when you'll see this again]
```
**Why it works:** Every output answers "What changed, and what do I do now?"
**Benefits:** Prevents ambiguity, creates actionability, enables verification
**Different from ST-03:** OC-06 is a specific 5-part template; ST-03 defines general format requirements
**Different from SV-09:** OC-06 has semantic sections (understood/producing/output); SV-09 has domain-specific labeled sections

### OC-07: Operating Principles Declaration
**What:** Explicit enumeration of behavior rules before task execution
**Category:** Output Control
**Use Case:** Tasks requiring judgment calls, interpretation, or quality standards
**Pattern:**
```markdown
## YOUR OPERATING PRINCIPLES

**Extract aggressively.** If something could be a task, surface it. I'll delete what doesn't matter.

**Preserve context.** Don't strip out the "why"—I need enough context to remember what this was about next week.

**Flag ambiguity.** If something is unclear, say so. Don't guess at what I meant.

**Suggest ownership.** For each task, note if it's clearly mine, clearly someone else's, or unclear.

**Identify dependencies.** If Task B can't happen until Task A is done, say so.
```
**Why it works:** Sets behavioral guardrails without complex instructions
**Format:** Bold title + explanation sentence

### OC-08: Multi-Mode Prompt Architecture
**What:** Single prompt with multiple modes triggered by user selection
**Category:** Output Control
**Use Case:** Related tasks with different timing or context (pre/post, planning/execution/review)
**Pattern:**
```markdown
This prompt has two modes—tell me which one you need.

---

## MODE: PRE-MEETING PREP
[Instructions for before meeting]

## MODE: POST-MEETING PROCESSING
[Instructions for after meeting]
```
**Why it works:** Reduces prompt proliferation, maintains context across related tasks
**Modes:** Pre/Post, Before/During/After, Planning/Execution/Review

### OC-09: Capability Boundary Specification
**What:** Explicitly define "Can Do" vs "Cannot Do" matrices that delineate what a prompt, agent, or skill is designed to handle and what falls outside its scope
**Pattern:**
```markdown
## What This Agent CAN Do
- Analyze code for security vulnerabilities in Python, JavaScript, Go
- Generate fix recommendations with code examples
- Prioritize findings by CVSS score

## What This Agent CANNOT Do
- Execute fixes automatically (requires human approval)
- Analyze compiled binaries or obfuscated code
- Provide legal compliance certification
- Access external vulnerability databases in real-time
```
**Used in:** Agent definitions, skill documentation, API documentation, product documentation, chatbot design
**Why it works:** Manages user expectations upfront; prevents misuse by making limitations explicit; reduces frustration from capability assumptions
**Different from CM-03:** CM-03 defines analysis boundaries (what to look at); OC-09 defines capability boundaries (what the tool itself can and cannot do)
**Reference:** Technique Deduplication Audit, Batch 5

### OC-10: Mandatory Disclaimer Pattern
**What:** Embed required disclaimers (legal, safety, scope limitations) as structural elements that cannot be omitted from output, regardless of context
**Pattern:**
```markdown
## Required Disclaimer (ALWAYS include at end of output)
⚠️ This analysis is for informational purposes only and does not constitute
[legal/medical/financial] advice. Consult a qualified [professional type]
before making decisions based on this output.

## Disclaimer Placement Rules
- MUST appear at the end of every response
- Wording may adapt to context but core message must be preserved
- Cannot be removed even if user requests omission
```
**Used in:** Healthcare prompts, legal advice, financial guidance, safety-critical instructions, any regulated domain
**Why it works:** Structural embedding ensures disclaimers survive prompt modification; placement rules prevent accidental omission
**Different from QA-04:** QA-04 states confidence levels about specific claims; OC-10 embeds mandatory boilerplate that must always appear regardless of content
**Reference:** Technique Deduplication Audit, Batch 3

### OC-11: Grouped Reporting by Pattern Type
**What:** Organize findings by pattern category rather than by location or severity, enabling readers to see systemic issues across a codebase or dataset
**Pattern:**
```markdown
## Authentication Issues (5 findings)
- `src/auth/login.ts:45` — Missing rate limiting on login endpoint
- `src/api/tokens.ts:12` — JWT tokens never expire
- `src/auth/oauth.ts:89` — OAuth state parameter not validated
[Summary: Authentication layer needs comprehensive hardening]

## Input Validation Issues (3 findings)
- `src/api/users.ts:23` — User input passed directly to SQL query
- `src/api/search.ts:67` — No sanitization on search parameter
[Summary: Input validation is inconsistent across API layer]
```
**Used in:** Security audits, code reviews, accessibility audits, compliance reports, data quality assessments
**Why it works:** Groups findings by systemic cause rather than individual occurrence; reveals patterns that severity-sorted lists miss
**Different from DS-06:** DS-06 sorts by severity (High → Low); OC-11 groups by pattern type, enabling systemic issue identification
**Reference:** Technique Deduplication Audit, Batch 7a

### OC-12: External Reference Catalog
**What:** Include a curated catalog of authoritative external references (official docs, RFCs, standards) as a structured section within prompt output
**Pattern:**
```markdown
## Reference Catalog

| Resource | URL/Citation | Covers | Consult When |
|----------|-------------|--------|-------------|
| OWASP Top 10 | owasp.org/Top10 | Web application security risks | Evaluating security findings |
| CWE Database | cwe.mitre.org | Weakness enumeration | Classifying vulnerability types |
| NIST SP 800-53 | nist.gov/800-53 | Security controls | Compliance mapping |
| PCI DSS v4.0 | pcisecuritystandards.org | Payment card security | Financial data handling |
```
**Used in:** Technical documentation, learning resources, compliance guides, research outputs, any domain with authoritative standards
**Why it works:** Provides a self-contained knowledge directory; readers don't need to search for authoritative sources themselves
**Different from QA-05:** QA-05 requires inline citations for specific claims; OC-12 is a proactive, curated reference section — a knowledge directory, not inline citations
**Reference:** Technique Deduplication Audit, Batch 3

---

## Quality Assurance Techniques

### QA-01: Self-Verification *(Merged from QA-01 + QA-03)*
**What:** Built-in self-critique step requiring review after initial response
**Pattern (Evidence-Based - Structured):**
```
After providing your initial analysis:
1. List three ways your analysis could be incomplete or incorrect
2. Cite specific evidence that confirms or refutes each concern
3. Provide revised analysis incorporating verified corrections
```
**Pattern (Reflection-Based - Open-Ended):**
```
First, provide your initial response.
Now critique your own response:
- What assumptions did I make?
- What could go wrong?
- What did I miss?
Revised response incorporating self-critique:
```
**Variants:**
- **Evidence-based:** Requires specific evidence for each concern (more rigorous)
- **Reflection-based:** Open-ended questions for self-examination (more exploratory)
**Used in:** High-stakes analysis, production prompts, quality-critical outputs
**Impact:** Significantly reduces confident errors
**Note:** Merged QA-03 into QA-01 (2026-01-22) — both address self-critique, now unified with two variants
**Variant — Mandatory Preservation Checklist:** Category-specific preservation verification — ensure nothing was accidentally removed or degraded during processing. Use after any transformation step to verify the output retains all required elements from the input.
**Reference:** `advanced_prompting_techniques.md` - Tier 1; `comprehensive_prompting_patterns.md` pattern #12
**Different from NE-06:** QA-01 is open-ended self-critique; NE-06 uses specific checkpoints (SELF-AUDIT →)
**Different from DD-07:** QA-01 is prose review; DD-07 requires structured table with evidence + location
**Different from QA-06:** QA-01 is single review pass; QA-06 is iterative critique-revise loops

### QA-02: Adversarial Stress-Test
**What:** Attack your own answer to find vulnerabilities
**Pattern:**
```
Now attack your previous answer:
1. Identify five ways it could be wrong or fail
2. Rate severity (Critical/High/Medium/Low) and likelihood
3. Propose specific revisions
4. Provide hardened version
```
**Used in:** Critical decisions, security analysis
**Best for:** Finding edge cases and failure modes
**Reference:** `advanced_prompting_techniques.md` - Tier 1

### QA-03: Reflection and Self-Critique → **Merged into QA-01** *(2026-01-22)*
**Status:** DEPRECATED — Use QA-01: Self-Verification instead
**Reason:** Both QA-01 and QA-03 addressed self-critique; now unified with two variants
**See:** QA-01 above (now includes reflection-based variant)

### QA-04: Uncertainty Acknowledgment
**What:** Explicitly state confidence levels and limitations
**Pattern:**
```
In your response:
- Clearly state when you're uncertain
- Provide confidence levels for claims
- Suggest verification methods
- Acknowledge limitations
```
**Used in:** Research, analysis, recommendations
**Why it works:** Prevents overconfident incorrect answers
**Reference:** `comprehensive_prompting_patterns.md` pattern #14

### QA-05: Citation Requirements
**What:** Require sources for claims
**Pattern:**
```
Requirements:
- Cite specific sources for each claim
- Distinguish facts from interpretations
- Flag uncertain information
- Provide source reliability assessment
```
**Used in:** Research, documentation
**Reference:** `comprehensive_prompting_patterns.md` pattern #13

### QA-06: Constitutional AI for Prompts
**What:** Apply self-correction principles with critique-revise loops to improve prompt quality through iterative refinement against defined constitutional principles
**Category:** Quality Assurance
**Use Case:** Production-critical prompts, complex prompts, hardening before deployment, quality assurance process
**Pattern:**
```markdown
## Constitutional AI Improvement Loop
### Phase 1: Generate Initial Prompt (v1.0)
### Phase 2: Critique Against Principles
Evaluate against:
- Clarity: Every instruction is unambiguous
- Completeness: All necessary information provided
- Consistency: No conflicting instructions
- Conciseness: No unnecessary complexity
- Correctness: Techniques applied properly

### Phase 3: Revise Based on Critique (v1.1)
### Phase 4: Repeat Critique-Revise (v1.2, v1.3)
```
**Why it works:** Systematically identifies violations and generates improved versions through multiple refinement cycles
**Reference:** [Full documentation: new-techniques/QA_06.md](new-techniques/QA_06.md)
**Different from QA-01:** QA-06 is iterative improvement through multiple cycles; QA-01 is single self-critique pass
**Different from NE-06:** QA-06 uses constitutional principles; NE-06 uses specific audit checkpoints

### QA-07: Statistical A/B Testing for Prompts
**What:** Apply rigorous experimental methods to systematically compare prompt variations and measure improvement objectively
**Category:** Quality Assurance
**Use Case:** Validating improvements, production AI systems, continuous improvement, comparing multiple approaches
**Pattern:**
```markdown
## A/B Test Design
Variant A (Control): Current production prompt
Variant B (Treatment): New candidate prompt
Primary Metric: Success rate, accuracy, user satisfaction
Sample Size: Calculate for statistical significance (typically n > 100 per variant)
Decision Criteria: p-value < 0.05, improvement > 5%

## Data Collection
Split traffic 50/50 between variants
Collect metrics for minimum 1 week
Track: Success rate, latency, error rate, user feedback

## Statistical Analysis
Run t-test or chi-square test for significance
Calculate confidence intervals
Determine winner based on data, not intuition
```
**Why it works:** Makes data-driven deployment decisions based on quantitative evidence rather than subjective judgment
**Reference:** [Full documentation: new-techniques/QA_07.md](new-techniques/QA_07.md)

### QA-08: Gate-Based Verification *(Merged from QA-08 + DD-01)*
**What:** Binary pass/fail checkpoints that must pass before proceeding—converts implicit completion to explicit, checkable criteria
**Category:** Quality Assurance / Done Definition
**Use Case:** Multi-stage workflows, production pipelines, quality-critical processes, AI agent task completion
**Pattern (Workflow Stages):**
```markdown
STAGE 1: BRIEF CREATION (Human)
Before any AI generation, I create:
- Visual spec with explicit constraints
- Text content written and spell-checked separately

Gate: Do not proceed until spec is complete. Incomplete specs cause regeneration cycles.

STAGE 2: GENERATION (AI)
Route to AI based on classification...

Gate: Generation complete. Proceed to QA.

STAGE 3: QA (Human)
Run test battery...

Gate: QA pass required. No exceptions for "looks fine."
```
**Pattern (Binary Verification Table):**
```markdown
| Gate | Pass/Fail Rule | Evidence Required | How to Check | "Not Yet" Example |
|------|----------------|-------------------|--------------|-------------------|
| All items covered | Count matches list | Item count | Count items | "Only 2/3 covered" |
| Each claim sourced | URL or reference | Source count | Count sources | "5 claims, 3 sources" |
```
**Gate Characteristics:**
- Binary (pass/fail)
- No adjectives—measurable criteria only
- Condition to check + consequence if not met
**Why it works:** Prevents quality issues from cascading; converts implicit completion to explicit, checkable criteria
**Note:** Merged DD-01 into QA-08 (2026-01-22) — both address gate-based verification with binary pass/fail
**Different from DP-05:** QA-08 defines gate structure; DP-05 scales number of gates by risk level
**Different from AG-02:** QA-08 is neutral verification; AG-02 defaults to skeptical/failure
**Variant — Multi-Stage Validation Pipeline:** Progressive validation stages (syntax → semantic → integration → acceptance) where each stage catches different failure types. Early stages are fast/cheap; later stages are thorough/expensive.
**Variant — Pre-Implementation Checklist:** A "readiness" gate before implementation begins (not a "completion" gate). Verifies that requirements are clear, dependencies are available, and constraints are understood before work starts.

### QA-09: Reversibility Assessment
**What:** Dedicated evaluation of whether actions can be undone
**Category:** Quality Assurance
**Use Case:** Autonomous agent delegation, high-risk tasks, irreversible operations
**Pattern:**
```markdown
### 8. Reversibility Assessment
**Can this be undone?** [Yes easily / Yes with effort / No]
**What could go wrong?** [Worst case scenario]
**Mitigation:** [How to catch problems early]
```
**Why it works:** Surfaces risk before delegation to autonomous agents
**Three levels:** Yes easily / Yes with effort / No
**Requires:** Worst case scenario + mitigation strategy

### QA-10: Test Battery Protocol
**What:** Systematic pre-ship testing checklist with specific tests
**Category:** Quality Assurance
**Use Case:** AI-generated visuals, artifacts, code, content requiring quality verification
**Pattern:**
```markdown
THE 5-MINUTE TEST BATTERY

Before shipping any AI-generated visual, run these tests:

1. ZOOM TEST: View at 50% and 200%. Is all text legible at both?
2. SPELL CHECK: Read every word in the image out loud. Any gibberish?
3. COUNT CHECK: If there should be N items, are there exactly N items?
4. LABEL CHECK: Do labels match what they're pointing to?
5. BRAND CHECK: Do colors, fonts, and style match brand guidelines?
```
**Why it works:** Catches common failure modes in under 5 minutes
**Structure:** Numbered tests + specific question for each
**Customizable:** Add domain-specific tests for deliverable type
**Variant — Production Readiness Checklist:** Embed multiple area-specific checklists (security, performance, reliability, observability) into a single production readiness gate. Use when the deliverable is a production system rather than a visual artifact.

### QA-11: Pass/Fail Test Harness
**What:** Structured testing with explicit pass criteria and remediation paths
**Category:** Quality Assurance
**Use Case:** Production quality gates, systematic QA, AI-generated outputs
**Pattern:**
```markdown
TEST 1: TYPOGRAPHY INTEGRITY
□ Legibility: Can I read every word at intended display size?
□ Spelling: Zero misspellings, including proper nouns?
□ Completeness: No truncated words or cut-off sentences?
□ Consistency: Same font treatment throughout?

PASS CRITERIA: All four boxes checked.
IF FAIL: Flag specific text elements. Regenerate with explicit spelling in prompt, or add text as overlay.

FINAL VERDICT:
SHIP: All tests pass.
FIX AND RESHIP: 1-2 minor failures with clear fixes.
REGENERATE: Structural or semantic failures—new generation needed.
MANUAL FALLBACK: Repeated failures on critical elements—remove from AI workflow.
```
**Why it works:** Forces explicit decision with clear remediation path
**Structure:** Test → Pass criteria → Remediation → Final verdict
**Four verdicts:** Ship / Fix and Reship / Regenerate / Manual Fallback

### QA-12: False Positives Identification
**What:** Explicit section to identify what NOT to pay attention to
**Category:** Quality Assurance
**Use Case:** Strategic analysis, capability assessment, investment decisions, hype filtering
**Pattern:**
```markdown
PART 5: FALSE POSITIVES

What gaps LOOK close but probably aren't?
- Gaps where demos impress but production requirements are much harder
- Gaps where technical progress is real but product/market fit is unclear
- Gaps getting hype but lacking serious research investment

What should I NOT spend attention on despite buzz?
```
**Why it works:** Prevents wasted effort on hype vs real opportunities
**Structure:** "What looks close but isn't" + "What to ignore despite buzz"

### QA-13: Failure Recovery Specification
**What:** Explicit rules for handling repeated failures
**Category:** Quality Assurance
**Use Case:** Adaptive workflows, AI quality control, production systems
**Pattern:**
```markdown
FAILURE RECOVERY PATHS:
- If generation fails 2x on same element → Move element to red list, create manually
- If QA fails on same issue 3x → Update prompt template or add to "never generate" list
- If total time exceeds manual baseline → Re-evaluate whether AI is helping for this deliverable

WEEKLY REVIEW QUESTIONS:
1. What failed QA most often this week?
2. Should any yellow elements move to red?
3. Should any red elements move to yellow (model improved)?
4. Is total time actually lower than manual baseline?
```
**Why it works:** Prevents endless regeneration loops, adapts to reality
**Structure:** Threshold (2x, 3x) → Action (move to red, update template, re-evaluate)
**Includes:** Weekly review to update classifications
**Different from DD-06:** QA-13 is recovery rules; DD-06 is iteration budget and escalation
**Different from DD-10:** QA-13 handles failures; DD-10 logs changes for debugging
**Variant — Fallback Strategy Pattern:** Progressive generality chain — each fallback is broader/simpler than the previous attempt (e.g., specific tool → generic approach → manual workaround). Use when recovery options form a natural specificity gradient.

### QA-15: Self-Consistency
**What:** Generate multiple independent solutions and select the most consistent answer—reduces variance from single-pass reasoning
**Pattern:**
```
Solve this problem [3-5] times independently:
1. First solution: [reasoning path]
2. Second solution: [reasoning path]
3. Third solution: [reasoning path]

Identify the most common/consistent answer across solutions.
Final answer with explanation of why this is most reliable.
```
**Used in:** High-stakes verification, mathematical reasoning, complex decisions
**Category:** Quality Assurance
**Why it works:** Surfaces inconsistencies in uncertain domains; majority voting across diverse reasoning paths reduces errors
**Research:** Based on Self-Consistency (Wang et al., 2022)
**Different from QA-01:** QA-01 is single-pass self-critique; QA-15 uses multiple independent generations
**Different from RP-03:** RP-03 uses different personas; QA-15 uses same prompt multiple times
**See Also:** QA-01 (Chain-of-Verification), RP-03 (Multi-Persona Debate), QA-04 (Uncertainty Acknowledgment)

### QA-16: Quality Rubric with Auto-Iteration
**What:** Define a numerical scoring rubric (e.g., 1-10 across multiple dimensions), score the output, and automatically iterate if the score falls below a threshold
**Pattern:**
```markdown
## Quality Rubric (score each 1-10)

| Dimension | Criteria for 10 | Criteria for 5 | Criteria for 1 |
|-----------|----------------|----------------|----------------|
| Accuracy | Zero factual errors | Minor inaccuracies | Major errors |
| Completeness | All requirements addressed | Most addressed | Critical gaps |
| Clarity | Immediately understandable | Requires re-reading | Confusing |
| Actionability | All items are actionable | Some vague | No clear actions |

## Auto-Iteration Rule
- Score output on all dimensions
- If ANY dimension < 6 OR total < 28/40: revise and re-score
- Maximum 3 iterations
- On final iteration, note which dimensions remain below threshold
```
**Used in:** Content generation, code generation, documentation, any prompt where output quality is measurable
**Why it works:** Creates a self-improving loop; the rubric makes quality criteria explicit and the auto-iteration ensures the output meets minimum standards before delivery
**Different from DT-03:** DT-03 refines through multiple passes without scoring; QA-16 combines scoring with automated iteration control
**Different from DS-02:** DS-02 defines what to measure; QA-16 builds the measurement into a self-correcting loop
**See Also:** QA-17 (Named Scores), DS-02 (Metric Specification), DT-03 (Iterative Refinement)
**Reference:** Technique Deduplication Audit, Batch 9

### QA-17: Named Scores for Multi-Dimensional Metrics
**What:** Alongside a binary pass/fail verdict, provide named sub-scores that decompose quality into independently measurable dimensions
**Pattern:**
```markdown
## Evaluation Results

**Overall Verdict:** PASS ✅

| Dimension | Score | Threshold | Status |
|-----------|-------|-----------|--------|
| Accuracy | 8/10 | ≥7 | ✅ PASS |
| Completeness | 6/10 | ≥7 | ⚠️ BELOW |
| Clarity | 9/10 | ≥6 | ✅ PASS |
| Actionability | 7/10 | ≥6 | ✅ PASS |

**Lowest dimension:** Completeness (6/10) — missing coverage of edge cases
**Improvement focus:** Add error handling examples and boundary conditions
```
**Used in:** LLM evaluation, code review scoring, content quality assessment, rubric-based grading, evaluation frameworks
**Why it works:** Makes quality assessment transparent and actionable; identifies specific improvement areas rather than giving opaque pass/fail
**Different from QA-11:** QA-11 is binary pass/fail; QA-17 provides multi-dimensional scores alongside the verdict
**Different from DS-02:** DS-02 defines what to measure; QA-17 provides the scoring structure and presentation format
**See Also:** QA-16 (Quality Rubric with Auto-Iteration), QA-11 (Pass/Fail Test Harness), DS-02 (Metric Specification)
**Reference:** Technique Deduplication Audit, Batch 6

### QA-18: Domain-Specific Smell Tests
**What:** Building a reusable set of field-specific verification checks that catch the most common ways AI output is subtly wrong in a particular domain — not generic "check for hallucinations" but concrete, domain-grounded checks
**Pattern:**
```markdown
## Domain Smell Tests for [Your Field]

For each check: What to verify | Why AI gets this wrong | How to verify quickly

Example (Financial Analysis):
- Check whether discount rate matches the risk profile described in narrative
  — AI often uses generic WACC while describing a high-risk venture
  — Quick verify: Compare WACC assumption to comparable companies in the sector

Example (Software Engineering):
- Check error handling paths, not just happy paths
  — AI-generated code almost always handles the happy path well and edge cases poorly
  — Quick verify: Trace one error path end-to-end

Example (Legal):
- Verify every case citation independently
  — AI cites real cases for propositions they don't actually support
  — Quick verify: Check the actual holding, not just the case name
```
**Used in:** AI output review, quality gates for AI-assisted work, professional practice with AI tools, team quality standards
**Why it works:** Generic verification advice ("be careful") doesn't change behavior. Domain-specific smell tests give professionals actionable checks that match their actual failure modes. As AI improves at producing plausible output, the ability to *evaluate* output becomes the scarce skill.
**Different from QA-01:** QA-01 is a one-time self-critique by the AI; QA-18 is a reusable human evaluation framework for a domain
**Different from NE-06:** NE-06 requires AI to self-audit; QA-18 equips humans to audit AI output
**Different from QA-19:** QA-18 builds the *checks*; QA-19 builds the *test suite* that uses them

### QA-19: Personal Eval Harness
**What:** A recurring test suite of 3-7 real tasks with specific inputs, expected output qualities, known failure modes, and scoring rubrics — run against every model update to benchmark performance on your actual work
**Pattern:**
```markdown
=== EVAL SUITE ===
Created: [date]

TEST CASE 1: [Task Name]

INPUT:
[Exact prompt/request — self-contained, refined]

EXPECTED OUTPUT QUALITIES:
☐ [Specific criterion 1 — observable, checkable]
☐ [Specific criterion 2]
☐ [Specific criterion 3]
☐ [Specific criterion 4]
☐ [Specific criterion 5]

KNOWN FAILURE MODES:
⚠ [Common way models get this wrong]
⚠ [Another common failure mode]

SCORING:
- 5/5 = Excellent — model handles this well
- 3-4/5 = Acceptable — usable with minor edits
- 1-2/5 = Poor — significant rework needed
- 0/5 = Fail — faster to do by hand

RESULT LOG:
| Date | Model/Tool | Score | Notes |
|------|-----------|-------|-------|
```
**Used in:** Personal AI benchmarking, model migration decisions, prompt regression testing, AI tool evaluation
**Why it works:** Most people evaluate AI anecdotally. A personal eval suite enables systematic comparison across model updates, catching regressions on the tasks that matter to your actual work (the "Lütke pattern").
**Cadence:** Run full suite after every major model update; run single test when trying new tools; update criteria monthly.
**Different from QA-10:** QA-10 is a test battery for visual/design outputs; QA-19 is a personal benchmarking suite for recurring tasks
**Different from QA-11:** QA-11 is binary pass/fail; QA-19 uses multi-criteria scoring with regression tracking
**Different from QA-18:** QA-18 builds the domain-specific checks; QA-19 packages them into a runnable, trackable test suite
**See Also:** QA-18 (Domain-Specific Smell Tests), QA-10 (Test Battery Protocol), QA-11 (Pass/Fail Test Harness)

### QA-20: Dual-Failure Quality Test
**What:** Testing AI responses for two failure modes simultaneously — harmful/incorrect output (obvious failure) AND needlessly unhelpful, preachy, or paternalistic output (subtle failure)
**Pattern:**
```markdown
## The "Thoughtful Senior Employee" Test:
Would a thoughtful, senior person at the AI company — someone who cares about
doing the right thing AND wants the AI to be genuinely helpful — be comfortable
with this response?

## Two failure modes to test:
1. HARMFUL: Response causes damage, is incorrect, or is dangerous
   → Most people test for this

2. NEEDLESSLY UNHELPFUL: Response is overly cautious, preachy,
   paternalistic, or adds unnecessary caveats
   → Most people miss this

## Test scenarios should include:
- Straightforward requests that might trigger unnecessary caution
- Professional requests where disclaimers waste the expert's time
- Creative requests where moralizing undermines the output
- Sensitive topics where balance should yield to user's stated needs

## Scoring:
- PASS: Helpful AND appropriate
- FAIL-HARMFUL: Response could cause damage
- FAIL-UNHELPFUL: Response is safe but needlessly cautious/preachy
```
**Used in:** System prompt testing, deployment QA, prompt evaluation, agent behavior testing, edge case validation
**Why it works:** Most AI QA focuses only on preventing harm. The dual-failure test also catches the equally problematic pattern of excessive caution — responses that are safe but useless. Both failure modes degrade user experience and trust.
**Key insight:** An unhelpful response IS a failure, not just a "safe" outcome. Testing for both directions catches the full spectrum of quality issues.
**Different from QA-06:** QA-06 applies constitutional principles for iterative improvement; QA-20 is a binary quality test that checks for both directions of failure
**Different from QA-19:** QA-19 benchmarks task performance; QA-20 specifically tests the harmful-vs-unhelpful balance



### QA-21: Metric Gaming Vector Enumeration
**What:** Adversarially enumerate concrete ways a metric can be improved without improving intended outcomes, categorized by mechanism of failure.
**Category:** Quality Assurance
**Use Case:** Pre-flight metric red-teaming before autonomous optimization
**Pattern:**
```markdown
Enumerate vectors across five categories:
1. Direct Gaming
2. Proxy Divergence
3. Eval Contamination
4. Silent Degradation
5. Compounding Cascades

For each vector, specify:
- Concrete scenario
- Why primary metric improves
- Real-world damage
- Time to human detection
```
**Used in:** Metric safety reviews, reward-hacking risk assessment, evaluation design
**Why it works:** Forces failure modes to be concrete and operational rather than abstract "could overfit" warnings
**Different from QA-02:** QA-02 stress-tests output quality broadly; QA-21 specifically targets metric-to-intent misalignment under optimization pressure

### QA-22: Evaluation Diversity Planning
**What:** Pair each identified gaming vector with explicit secondary metrics, holdout scenarios, review cadence, and accountable reviewers.
**Category:** Quality Assurance
**Use Case:** Building defense-in-depth for optimization loops
**Pattern:**
```markdown
For each gaming vector, define:
- Secondary metric (with computation and threshold)
- Holdout scenario (never shown to optimizer)
- Implementation method
- Run frequency
- Human reviewer owner

Then prioritize the top 3 most dangerous vectors by likelihood × detection difficulty.
```
**Used in:** Evaluation harness hardening, metric governance, autonomous system safety planning
**Why it works:** Converts diagnostic insight into operational controls that can be implemented and audited
**Different from QA-17:** QA-17 scores multi-dimensional output quality; QA-22 designs the ongoing measurement system that guards against reward hacking over time

---

## Context Management Techniques

### CM-01: Explicit Context Framing
**What:** Provide all relevant background upfront
**Pattern:**
```
Context:
- [Relevant background information]
- [Constraints or requirements]
- [Assumed knowledge]

Given this context: [Task]
```
**Used in:** Business analysis, strategic planning
**Example:** SWOT analysis with company/project context
**Reference:** `comprehensive_prompting_patterns.md` pattern #17
**See Also:** NE-03 (fill-in-blank fields), NE-08 (open-ended gathering), SV-02 (grouped inputs), MP-03 (active questioning)

### CM-02: Constraint Specification
**What:** Explicit must/must-not requirements
**Pattern:**
```
Constraints:
- Must: [Required elements]
- Must not: [Prohibited elements]
- Should: [Preferred elements]
- Should not: [Discouraged elements]
```
**Used in:** Code generation, content creation
**Reference:** `comprehensive_prompting_patterns.md` pattern #18
**Different from AG-04:** CM-02 constrains input/output; AG-04 constrains agent behavior across all actions
**Different from DP-04:** CM-02 uses full must/should structure; DP-04 requires minimum 2 "must-not" constraints

### CM-03: Scope Definition
**What:** Clearly define boundaries of analysis
**Pattern:** Define what to analyze, what tools/data to use, what timeframes, what types of issues
**Used in:** Code analysis, performance profiling
**Why it works:** Prevents scope creep and unfocused analysis
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #19
**Different from NE-09:** CM-03 defines initial scope boundaries; NE-09 actively challenges and reduces scope

### CM-04: Summary-Expand Loop
**What:** Compress conversation at token limits, then expand in new session
**Pattern:**
```
PHASE 1: Compress this conversation into:
**Key Findings:** [3-4 bullets]
**Critical Details:** [Must preserve]
**Open Questions:** [What's unresolved]
**Context for Next Phase:** [Minimum info needed]

PHASE 2: Using this summary, now provide [expanded request]
```
**Used in:** Long analysis sessions, complex projects
**Reference:** `advanced_prompting_techniques.md` - Tier 5

### CM-05: Progressive Context Accumulation
**What:** Explicitly chain context through multi-step workflows where each phase's output becomes the next phase's input
**Category:** Context Management
**Use Case:** Multi-step workflows, multi-agent orchestration, long-running projects
**Pattern:**
```markdown
## Phase {N}: {PHASE_NAME}
### Context (Input)
- **From Phase {N-1}:** {SPECIFIC_OUTPUT_1}
- **From Phase {N-2}:** {SPECIFIC_OUTPUT_2}
- **Expected Format:** {DATA_STRUCTURE}

### Expected Output
- **Primary Output:** {MAIN_DELIVERABLE}
- **Passed to:** Phase {N+1}
```
**Why it works:** Prevents context loss in long-running workflows by making information handoffs explicit
**Reference:** [Full documentation: new-techniques/CM_05.md](new-techniques/CM_05.md)

### CM-06: Semantic Vector-Based Context Management
**What:** Use vector embeddings and similarity search for intelligent context storage and retrieval
**Category:** Context Management
**Use Case:** Massive context repositories, RAG systems, cross-project knowledge transfer
**Pattern:**
```markdown
1. Context Encoding: Generate embeddings for context segments
2. Store in Vector Database: Pinecone/Weaviate/Qdrant with metadata
3. Semantic Retrieval: Query with current task, retrieve top-k similar contexts
4. Relevance Ranking: Score and prioritize retrieved contexts
```
**Why it works:** Enables relevance-based retrieval based on semantic similarity, not just keywords or recency
**Variant — Multi-Stage Relevance Scoring:** Composite scoring across semantic, temporal, and historical dimensions for context retrieval. Score = weighted combination of similarity score + recency decay + usage frequency.
**Reference:** [Full documentation: new-techniques/CM_06.md](new-techniques/CM_06.md)

### CM-07: Token-Budget-Aware Progressive Loading
**What:** Dynamically load context components in priority order until token budget is exhausted
**Category:** Context Management
**Use Case:** Large context repositories, production AI systems, cost-sensitive applications
**Pattern:**
```markdown
1. Define Prioritization Tiers: Critical → Important → Useful
2. Token Budget Allocation: Reserve for conversation, allocate for context
3. Progressive Loading: Load Tier 1 fully, then Tier 2 until budget exhausted
4. Track What's Loaded: Document which context was included/excluded
```
**Why it works:** Maximizes utility within API constraints by prioritizing most valuable information
**Variant — Adaptive Context Expansion:** Runtime discovery of additional context needs — dynamically expand context when initial loading proves insufficient. Detect "I need more context about X" signals and load additional relevant context on demand.
**Reference:** [Full documentation: new-techniques/CM_07.md](new-techniques/CM_07.md)

### CM-08: File-Based State Persistence
**What:** Using structured files to maintain context across sessions
**Category:** Context Management
**Use Case:** Personal productivity systems, stateful agents, persistent workflows
**Pattern:**
```markdown
Read my CLAUDE.md file first for context.
Check PROJECTS.md, WAITING_FOR.md, and INBOX.md for current state.

[After processing, update:]
- PROJECTS.md — new tasks, status changes
- WAITING_FOR.md — new delegations
- DECISIONS.md — decisions made
```
**Why it works:** Creates persistent memory layer that survives session boundaries
**Files used:** CLAUDE.md, INBOX.md, PROJECTS.md, WAITING_FOR.md, DECISIONS.md, /work-orders/
**Variant — Personal Context Document:** A comprehensive reusable context document covering 7+ domains (role, goals, quality standards, communication style, institutional knowledge, constraints, AI interaction patterns) that dramatically improves AI output quality when loaded into any session. Built through structured deep interview, updated monthly. Typically 500-1,000 words — long enough to be comprehensive, short enough to be token-efficient.

### CM-09: Authority Boundary Specification
**What:** Explicit three-zone permission model for agent actions
**Category:** Context Management
**Use Case:** Autonomous agents, delegation systems, safety-critical applications
**Pattern:**
```markdown
### You can do without asking:
- Draft anything for my review
- Update my chief-of-staff files
- Research and summarize

### Always ask first before:
- Sending any message on my behalf
- Scheduling meetings
- Making commitments to others

### Never do:
- Send messages without my explicit approval
- Make financial/legal/medical decisions
- Share private information externally
```
**Why it works:** Prevents dangerous autonomous actions while enabling useful automation
**Three zones:** ✅ Autonomous / ⚠️ Ask First / 🚫 Never
**Variant — Decision Authority Map:** Extends the three-zone model with a notification tier: *Decide Autonomously* (no escalation needed), *Decide with Notification* (make the call but report it), *Escalate Before Acting* (must get approval). Use when delegation requires distinguishing between "don't bother me" and "tell me after."
**Variant — Principal Hierarchy:** For Claude API deployments, maps trust levels across the principal chain: Anthropic (hard constraints) > Operator (system prompt) > User (conversation). Defines what each principal can and cannot override. Use when designing system prompts for Claude deployments.

### CM-10: Memory Scaffold Architecture
**What:** Structured persistent context file with standardized sections
**Category:** Context Management
**Use Case:** Long-term agent relationships, personalized AI assistants, persistent context
**Pattern:**
```markdown
# CLAUDE.md — Memory Scaffold

## Who I Am
[Name, Role, Context]

## How I Work
[Communication style, Work patterns, Decision-making]

## Current Priorities
[This Quarter's Focus, This Week's Top 3]

## Active Projects
[High-level overview]

## People & Context
[Key people and relationships]

## Preferences & Patterns
[Things I always want, Things I never want]

## Authority Boundaries
[Permission model]

## Lessons Learned
[Patterns discovered through working together]
```
**Why it works:** Single source of truth for agent context, read at start of every session
**Update frequency:** Weekly during Weekly Review + ad-hoc additions
**Variant — Context Fingerprinting:** Version identifiers with drift detection — detect when persisted context has become stale. Add last-updated timestamps and hash fingerprints to each section; flag sections that haven't been refreshed within expected intervals.

### CM-11: Reasoning-Based Constraint Design
**What:** Converting bare rule constraints ("Never do X") to reasoning-based constraints that explain the *why* behind each restriction, enabling better edge-case judgment by the AI
**Pattern:**
```markdown
## Rule-Based (Less Effective)
"Never discuss competitors. If asked about competitors, say you can only discuss our products."

## Reasoning-Based (More Effective)
"You're representing Acme Corp. We want customers to have a helpful experience
focused on whether our product solves their problem. Discussing competitors in
detail shifts the conversation away from understanding customer needs. If
competitors come up, acknowledge the question and redirect to understanding
what the customer is trying to accomplish."

## Conversion Process
For each rule-based constraint:
1. What is the business/safety reason behind this rule?
2. What's the spirit of the instruction, not just the letter?
3. What judgment should the AI apply in edge cases?
4. Rewrite as: [Context] + [Reasoning] + [Desired behavior] + [Edge case guidance]
```
**Used in:** System prompt design, agent configuration, CLAUDE.md creation, any AI deployment with behavioral constraints
**Why it works:** AI models (especially Claude) internalize reasoning more robustly than bare rules. A constraint with explained purpose produces better behavior in edge cases because the AI can apply the *spirit* of the rule to novel situations it's never seen.
**Key insight:** Rules without reasoning get followed literally in unintended ways. Reasoning without rules gets applied with good judgment even in unanticipated scenarios.
**Different from CM-02:** CM-02 specifies *what* constraints to set (must/must-not/should); CM-11 specifies *how* to write constraints so they work with model training
**Different from AG-04:** AG-04 defines behavioral guardrails; CM-11 focuses on the technique of converting rules to reasoning-based instructions

### CM-12: Multi-Lens Request Framing
**What:** Structuring requests to address the AI's multiple interpretation dimensions — immediate desires (what you're asking for), final goals (deeper motivation), background desiderata (implicit quality standards), autonomy (your right to decide), and wellbeing (long-term flourishing)
**Pattern:**
```markdown
## When formulating a request, address multiple lenses:

1. IMMEDIATE DESIRE: [What you specifically want]
2. FINAL GOAL: [Why you want it — the deeper motivation]
3. QUALITY STANDARDS: [Implicit standards the response should meet]
4. DECISION CONTEXT: [Your ability to make informed choices]

## Example — Weak (1 lens):
"Give me investment options."

## Example — Strong (4 lenses):
"I'm evaluating investment options for my retirement portfolio (immediate).
I want to retire in 15 years with enough passive income to cover expenses (goal).
I need specific numbers, not generic advice (standards).
I understand the risks — I've been investing for 20 years (autonomy)."
```
**Used in:** Any AI interaction, prompt design, system prompt authoring, user communication coaching
**Why it works:** AI models interpret requests through multiple dimensions simultaneously. Addressing more lenses gives the model richer signal about what constitutes a good response, reducing hedging and generic output.
**Key insight:** Users who only state the "what" (immediate desire) force the AI to guess at the other four dimensions, usually defaulting to the most cautious interpretation.
**Different from CM-01:** CM-01 provides background context; CM-12 specifically structures requests to address the AI's interpretation framework

### CM-13: Distinguishing Context Provision
**What:** Providing context that differentiates a legitimate request from potentially harmful use — addressing the AI's implicit risk assessment by making your specific situation clear
**Pattern:**
```markdown
## The 1,000 Users Principle:
AI models imagine the full spectrum of people who might send a similar message.
Provide context that distinguishes you from potential bad actors.

## Weak (ambiguous intent):
"How do I pick a lock?"

## Strong (distinguished context):
"I'm a locksmith training an apprentice — how do I explain lock picking
techniques for common residential deadbolts?"

## Context elements that distinguish:
- Professional role or expertise
- Legitimate purpose for the information
- Specific situation that explains the need
- Evidence of existing knowledge or responsibility
```
**Used in:** Requests for sensitive/dual-use information, borderline topics, professional queries, any interaction where context shifts the risk calculus
**Why it works:** AI models assess requests partly by imagining the distribution of users who would send a similar message. Context that narrows this distribution to legitimate use cases shifts the risk calculus, enabling more substantive help.
**Different from CM-01:** CM-01 provides general background; CM-13 specifically provides context that addresses the AI's risk assessment for borderline requests
**Different from CM-11:** CM-11 designs reasoning-based constraints for system prompts; CM-13 is a user-side technique for shifting how the AI evaluates request risk

### CM-14: Principal Hierarchy Specification
**What:** Defining explicit trust levels and authority boundaries in system prompts for multi-stakeholder deployments — specifying what operators can instruct, what users can override, and what remains constant regardless of instructions
**Pattern:**
```markdown
## Trust Hierarchy (highest to lowest):
1. PLATFORM RULES: [Non-negotiable constraints — safety, ethics, legal]
2. OPERATOR INSTRUCTIONS: [Your system prompt — persona, scope, behavior]
3. USER PERMISSIONS: [What end users can customize or override]

## Trust Calibration:
- Default: Users get slightly less latitude than operators
- Grant elevated trust: "Trust the user's claims about their occupation"
- Restrict permissions: "Do not allow users to change the response language"
- Context-specific: "Users on this platform are verified medical professionals"

## What Operators CAN Do:
- Assign personas, restrict topics, adjust default behaviors
- Expand or restrict user permissions
- Provide context that changes how the AI interprets requests

## What Operators CANNOT Do:
- Instruct the AI to deceive users against their interests
- Prevent users from getting urgent safety help
- Override hard safety constraints
```
**Used in:** System prompt design, API deployments, agent configuration, multi-tenant platforms, enterprise AI deployments
**Why it works:** AI models operate within a principal hierarchy. Explicitly specifying trust levels prevents conflicts between operator intent and user requests, and ensures gap-filling judgment aligns with the correct authority level.
**Different from CM-09:** CM-09 defines action-level permissions (can do/ask first/never do); CM-14 defines stakeholder-level trust hierarchy and what each level of authority can specify
**Different from AG-04:** AG-04 defines behavioral guardrails; CM-14 defines who has authority to set those guardrails

### CM-15: Gap-Filling Intent Signaling
**What:** Making operator or user intent explicit enough that the AI's gap-filling judgment — how it handles situations not covered by instructions — aligns with actual goals
**Pattern:**
```markdown
## The Gap-Filling Principle:
When instructions don't cover a scenario, the AI fills gaps with judgment
about what you would most plausibly want. Make your intent clear enough
that this judgment aligns with your actual goals.

## Weak (gaps filled unpredictably):
"You are a customer service bot. Only discuss our products."

## Strong (intent signals guide gap-filling):
"You are a customer service representative for Acme Corp.
Our goal is to help customers determine whether our product solves their problem.
When you encounter situations these instructions don't cover,
prioritize: (1) being genuinely helpful, (2) representing our brand well,
(3) not making commitments we can't keep."

## What to signal:
- The spirit of your instructions, not just the letter
- What success looks like for your deployment
- Priority ordering for competing values
- What you'd want in the most common edge cases
```
**Used in:** System prompt design, agent configuration, deployment architecture, any scenario where instructions can't cover all cases
**Why it works:** No system prompt can anticipate every scenario. Rather than adding rules for every edge case, signaling your overall intent enables the AI to exercise judgment that consistently aligns with your goals.
**Key insight:** Gap-filling is a feature, not a bug — but it works best when the AI understands the *spirit* of your instructions, not just the rules.
**Different from CM-11:** CM-11 converts individual rules to reasoning-based constraints; CM-15 provides overarching intent signals that guide behavior in situations no rule covers
**Different from CM-02:** CM-02 specifies explicit constraints; CM-15 guides behavior in the gaps between constraints

---

## Role & Perspective Techniques

### RP-01: Expert Role Assignment
**What:** Assign specific expert persona
**Pattern:** "You are a [specific role] with [relevant expertise]."
**Used in:** Security analysis, architecture reviews, domain-specific tasks
**Example:** "You are a senior security architect with 15 years of experience in financial services"
**Reference:** `comprehensive_prompting_patterns.md` pattern #7
**Different from AG-01:** RP-01 assigns expertise only; AG-01 adds personality, memory, and learned experience
**Different from NE-12:** RP-01 sets domain expertise; NE-12 sets cognitive/reasoning mode (analytical vs creative)
**Different from ST-16:** RP-01 defines what the AI knows; ST-16 defines how the AI behaves
**See Also:** AG-01 (adds memory/personality), NE-12 (cognitive stance), ST-16 (behavioral traits), AG-26 (AI tool fluency)

### RP-02: Audience-Specific Framing
**What:** Tailor explanation to specific audience
**Pattern:**
```
Explain [topic] as if speaking to [audience].
Key audience characteristics:
- [Characteristic 1]
- [Characteristic 2]
```
**Used in:** Educational prompts, documentation
**Example:** Teaching prompts that adapt to student level
**Reference:** `comprehensive_prompting_patterns.md` pattern #8

### RP-03: Multi-Persona Debate
**What:** Simulate debate between experts with different priorities
**Pattern:**
```
Persona 1: [Role] - Priority: [Focus]
Persona 2: [Role] - Priority: [Focus]
Persona 3: [Role] - Priority: [Focus]
Each presents position, critiques others, then synthesize
```
**Used in:** Strategic decisions, architecture choices
**Why it works:** Surfaces genuine tradeoffs and conflicts
**Reference:** `advanced_prompting_techniques.md` - Tier 4

### RP-04: Socratic Dialogue
**What:** Question-and-answer format for learning
**Pattern:** Generate dialogue between curious learner and experienced mentor
**Used in:** Educational prompts, code review
**Best for:** Encouraging critical thinking
**Example:** `learning/learning_socratic_dialogue_code_review.md`

### RP-05: Temperature Simulation
**What:** Provide cautious and confident analyses, then synthesize
**Pattern:**
```
Analysis 1 - Cautious Junior: Explore risks, uncertainties
Analysis 2 - Confident Senior: Clear recommendations, decisive
Analysis 3 - Synthesis: Where to be confident, where to be cautious
```
**Used in:** Decision-making, risk assessment
**Reference:** `advanced_prompting_techniques.md` - Tier 4

### RP-06: Expert Friend Positioning
**What:** Framing the AI as a knowledgeable friend who gives real, frank information rather than cautious, generic advice — the "brilliant friend who happens to have professional expertise" standard
**Pattern:**
```markdown
## The "Brilliant Friend" Standard:
Position the AI as a knowledgeable friend, not a liability-conscious professional.

## Default behavior (cautious professional):
User: "Should I worry about this mole?"
AI: "I can't provide medical advice. Please consult a dermatologist."

## Expert friend behavior:
User: "Should I worry about this mole?"
AI: "Here's what dermatologists look for: asymmetry, border irregularity,
color variation, diameter >6mm, evolving shape. If yours shows any of these,
see a dermatologist within 2 weeks. If it's symmetric, uniform color, and
hasn't changed — probably fine, but worth mentioning at your next checkup."

## How to activate:
- Signal your capability: "I understand the risks involved"
- Request directness: "Give me your honest assessment, not disclaimers"
- Provide context that establishes expertise or competence
- Underselling your needs triggers generic responses
```
**Used in:** Any AI interaction where users want substantive help rather than cautious deflection, professional consultations, technical advice, personal decision-making
**Why it works:** AI models are trained to be genuinely helpful, like a friend with professional expertise. When users signal they can handle direct information, the AI can provide the frank, substantive responses it's trained to give rather than defaulting to liability-conscious caution.
**Key insight:** Users who undersell their needs get generic responses. Users who signal competence and directness get the "brilliant friend" treatment.
**Different from RP-01:** RP-01 assigns expert knowledge to the AI; RP-06 shifts the AI's communication stance from cautious professional to frank expert friend
**Different from RP-02:** RP-02 adapts to audience level; RP-06 shifts the relationship dynamic from professional distance to trusted friend directness

---

## Decomposition Techniques

### DT-01: Hierarchical Task Breakdown
**What:** Break complex tasks into phases and subtasks
**Pattern:**
```
Break this down into:
1. High-level phases
2. Sub-tasks per phase
3. Dependencies and ordering
4. Success criteria for each sub-task
```
**Used in:** Project planning, migration strategies
**Reference:** `comprehensive_prompting_patterns.md` pattern #15
**Variant — Atomic Requirement Decomposition:** Break compound requirements into atomic, independently testable units. Each atomic requirement should be verifiable with a single test. Adds an atomicity criterion: if a requirement contains "and", it should usually be split.
**See Also:** ST-02 (sequential execution), NE-02 (dialogue phases), AG-07 (multi-agent orchestration)

### DT-02: Specific Focus Areas with Examples
**What:** Detailed enumeration of what to look for
**Pattern:** Provide concrete list of items to analyze (e.g., SQL injection, XSS, CSRF)
**Used in:** Security analysis, quality checks
**Why it works:** Provides domain-specific guidance for comprehensive coverage
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #4

### DT-03: Iterative Refinement
**What:** Multiple passes to perfect output
**Pattern:**
```
Draft 1: [Quick initial version]
Improvement areas: [What to fix]
Draft 2: [Improved version]
Final polish: [Polished version]
```
**Used in:** Writing, prompt improvement
**Reference:** `comprehensive_prompting_patterns.md` pattern #16

### DT-04: Multi-Layer Analysis *(Merged from DT-04 + RT-13)*
**What:** Analysis methodology with distinct layers—from surface issues to systemic patterns
**Pattern (Micro/Macro):**
- **Micro-level:** Specific issues, actionable details
- **Macro-level:** Trends, patterns, strategic insights
**Pattern (Three-Layer Depth):**
- **Layer 1 (Surface):** Immediate issues
- **Layer 2 (Deep):** Root causes
- **Layer 3 (Systemic):** Systemic patterns
**Use Cases:** Code analysis, strategic reviews, architecture assessment, comprehensive analysis
**Why it works:** Provides both actionable details and strategic insights; ensures thorough coverage; prevents surface-level analysis
**Note:** Merged RT-13 into DT-04 (2026-01-22) — both address multi-layer analysis methodology
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #16
**Different from DT-05:** DT-04 analyzes by depth (surface→deep→systemic); DT-05 analyzes by component (element-by-element)

### DT-05: Element-by-Element Assessment Matrix
**What:** Systematic capability evaluation for each component
**Category:** Decomposition Techniques
**Use Case:** Capability mapping, AI adoption planning, workflow optimization
**Pattern:**
```markdown
SECTION 1: ELEMENT-BY-ELEMENT ASSESSMENT

For each visual element typical to this deliverable, classify:

GREEN (Generate with AI)
- AI reliably produces usable output
- Verification is fast (glance check)
- Failure is recoverable (regenerate or quick fix)

YELLOW (Generate with guardrails)
- AI sometimes nails it, sometimes breaks
- Requires specific verification steps
- List the exact guardrails needed

RED (Do not generate)
- AI output requires more fixing than manual creation
- Failure modes are subtle and easy to miss

For each element, note:
- The specific failure mode I should expect
- The verification step required (what do I check?)
- Time estimate: AI generation + verification vs. manual creation
```
**Why it works:** Creates granular decision-making at element level
**Three classifications:** GREEN / YELLOW / RED
**Each element needs:** Failure mode + Verification + Time estimate
**Different from DT-04:** DT-05 evaluates components systematically; DT-04 analyzes by depth layers
**Variant — Content Classification Matrix:** Multi-dimensional content evaluation matrix. Specializes DT-05 for content classification with dimensions like relevance, accuracy, and completeness applied to each content element.

### DT-06: Typography Decision Tree
**What:** Binary decision tree for classification using yes/no questions
**Category:** Decomposition Techniques
**Use Case:** Classification tasks, decision-making frameworks, rapid assessment
**Pattern:**
```markdown
SECTION 2: TYPOGRAPHY DECISION TREE

For any text that appears IN the image:

Answer these questions:
1. Must this text be letter-perfect? (Yes = RED)
2. Is this text > 10 words? (Yes = likely YELLOW, check legibility)
3. Does this text include numbers, dates, or proper nouns? (Yes = verify each one)
4. Will this text be translated later? (Yes = test layout stability)
5. Is this text legally or brand-critical? (Yes = RED, manual only)

Output: A decision rule for this deliverable's typical text elements.
```
**Why it works:** Simplifies complex classification into binary questions
**Structure:** 5 yes/no questions → classification (RED/YELLOW/GREEN)
**Output:** Decision rule specific to deliverable type

---

## Educational Techniques

### ED-01: Iterative Scaffolding
**What:** One concept at a time, check understanding, then proceed
**Pattern:** "Give bite-sized pieces, ask for 1-3 rating on understanding"
**Used in:** Teaching prompts
**Example:** `engineering/engineering_teach_me_to_code.md`
**Why it works:** Adapts to learner pace, prevents overwhelm

### ED-02: Progressive Exercise Generation
**What:** Create exercises matched to current skill level
**Types:** Code tasks, debugging tasks, output prediction tasks
**Pattern:** Sequential numbering, separate lesson vs. exercise files
**Used in:** Coding tutorials
**Example:** `001-lesson-[topic].py`, `002-exercise-[topic].py`

### ED-03: Guided Discovery
**What:** Ask guiding questions instead of giving answers
**Pattern:** "If student wrong, do NOT immediately tell what's wrong. Ask guiding questions."
**Used in:** Educational prompts
**Why it works:** Develops problem-solving skills

### ED-04: Personalization Hooks
**What:** Ask about interests and incorporate into lessons
**Pattern:** "Ask about interests (shows, hobbies) and incorporate into lessons"
**Used in:** Teaching prompts
**Why it works:** Increases engagement and retention

### ED-05: Reference Class Priming
**What:** Show example of excellent output, then ask for similar quality
**Pattern:**
```
Here is high-quality analysis you provided previously:
[PASTE EXCELLENT OUTPUT]
Now provide analysis that matches or exceeds that standard:
[NEW QUESTION]
```
**Used in:** Maintaining quality across document sets
**Reference:** `advanced_prompting_techniques.md` - Tier 3
**Different from NE-04:** ED-05 shows single excellent example; NE-04 shows contrast pairs (bad→good)
**Different from MP-04:** ED-05 sets quality benchmark; MP-04 defines edge case boundaries

### ED-06: Example Quantity Specification
**What:** Explicitly mandate a minimum number of examples (e.g., "Provide at least 3 examples for each concept") to prevent under-specification and ensure sufficient illustration
**Pattern:**
```markdown
For each [concept/rule/pattern], provide at minimum 3 examples showing:
- Example 1: Basic/common case
- Example 2: Edge case or non-obvious application
- Example 3: Counter-example (when the pattern does NOT apply)

Variation requirements: Each example must differ in at least one dimension
(language, scale, domain, or complexity level).
```
**Used in:** Documentation, tutorials, API references, style guides, coding standards, any context where examples prevent misunderstanding
**Why it works:** Quantity ensures coverage of edge cases and variations; explicit minimums prevent the common failure of providing a single example that doesn't generalize
**Different from ED-05:** ED-05 shows one excellent example as a quality benchmark; ED-06 ensures sufficient quantity of examples for comprehensive illustration
**See Also:** ED-05 (Reference Class Priming), NE-04 (Good vs Bad Example Calibration)
**Reference:** Technique Deduplication Audit, Batch 6

---

## Meta-Prompting Techniques

### MP-01: Reverse Prompting
**What:** Ask AI to write the optimal prompt, then execute it
**Pattern:**
```
You are an expert prompt engineer. Write the single most effective prompt for:
[DESCRIBE TASK]
Consider: details, constraints, reasoning steps, output format, examples
First write the optimal prompt. Then execute it.
```
**Used in:** Unfamiliar domains, prompt improvement
**Reference:** `advanced_prompting_techniques.md` - Tier 2

### MP-02: Recursive Optimization
**What:** Iteratively improve a prompt through versions
**Pattern:**
```
Current prompt: "[EXISTING PROMPT]"
Task goal: [OBJECTIVE]
Improve through three iterations:
- V1: Add constraints, specifications, edge cases
- V2: Resolve ambiguities, clarify expectations
- V3: Enhance reasoning depth while maintaining clarity
Provide only final Version 3.
```
**Used in:** Hardening prompts before scaling
**Reference:** `advanced_prompting_techniques.md` - Tier 2

### MP-03: Task Clarification
**What:** Ask for requirements before proceeding
**Pattern:**
```
Before proceeding, ask me:
- Clarifying questions about requirements
- Questions about constraints
- Questions about output format
- Questions about success criteria
```
**Used in:** Ambiguous tasks
**Reference:** `comprehensive_prompting_patterns.md` pattern #20
**See Also:** CM-01 (prose context), NE-03 (fill-in-blank), NE-08 (open-ended), SV-02 (grouped inputs)

### MP-04: Strategic Edge Case Calibration
**What:** Provide baseline, failure mode, and edge case examples
**Pattern:**
```
BASELINE EXAMPLE: [Simple case]
FAILURE MODE EXAMPLE: [Where naive approach fails]
EDGE CASE EXAMPLE: [Complex boundary case]
Now apply to: [ACTUAL PROBLEM]
```
**Used in:** Complex pattern recognition
**Reference:** `advanced_prompting_techniques.md` - Tier 1
**Different from ED-05:** MP-04 defines boundaries via edge cases; ED-05 sets quality benchmark via excellent example
**Different from NE-04:** MP-04 shows baseline+failure+edge; NE-04 shows only bad→good contrast

### MP-05: Extended Thinking Documentation
**What:** Embed system-level reasoning blocks explaining WHY workflows are structured a certain way
**Category:** Meta-Prompting
**Use Case:** Complex multi-agent workflows, maintainable AI systems, production systems
**Pattern:**
```markdown
[Extended thinking: This workflow is designed to {PRIMARY_GOAL}. It follows
{KEY_PRINCIPLE} to ensure {DESIRED_OUTCOME}.

Key design decisions:
1. {DECISION}: We chose {APPROACH} over {ALTERNATIVE} because {REASONING}
2. {DECISION}: {APPROACH} prevents {FAILURE_MODE}

Sequencing rationale:
- {STEP_A} must precede {STEP_B} because {DEPENDENCY_REASON}
]
```
**Why it works:** Preserves architectural design decisions and workflow sequencing rationale for long-term maintainability
**Different from RT-01 (CoT):** Focuses on system-level design rationale, not task execution reasoning
**Reference:** [Full documentation: new-techniques/MP_05.md](new-techniques/MP_05.md)

### MP-06: Fallback Question Protocol
**What:** Systematic "ask questions if insufficient info" pattern at start of prompt
**Category:** Meta-Prompting
**Use Case:** All prompts requiring user-specific context, preventing hallucination
**Pattern:**
```markdown
If you don't have enough information to generate useful outputs, ask me questions until you have enough information.
```
**Why it works:** Prevents hallucination and guessing when context is missing
**Placement:** Early in prompt, before main instructions
**Best for:** Prompts requiring user-specific context
**Alternative phrasing:** "Ask clarifying questions if needed before proceeding"

### MP-07: Pattern Recognition Reflection
**What:** Systematic reflection on behavioral patterns across time
**Category:** Meta-Prompting
**Use Case:** Weekly reviews, retrospectives, continuous improvement, self-awareness
**Pattern:**
```markdown
**Pattern Recognition**
Looking across the week:
- **Energy patterns:** [When were you most/least productive?]
- **Avoidance patterns:** [What kept getting pushed?]
- **Interruption patterns:** [What derailed focus?]
- **What worked:** [Tactics or conditions that helped]
```
**Why it works:** Surfaces insights that improve future planning
**Four pattern types:** Energy, Avoidance, Interruption, Success
**Frequency:** Weekly review

### MP-08: Four-Layer Enhancement Process
**What:** Optimize prompts through four systematic layers: 1) Structure improvement, 2) Clarity refinement, 3) Technique injection, 4) Edge case hardening; apply layers sequentially
**Pattern:**
```markdown
## Prompt Enhancement Process

### Layer 1: Structure
- Fix ordering (most important instructions first)
- Group related instructions into sections
- Add headers and formatting for scannability

### Layer 2: Clarity
- Replace ambiguous terms with precise language
- Convert passive voice to active instructions
- Eliminate redundancy and contradictions

### Layer 3: Technique Injection
- Add Chain-of-Thought where reasoning is needed
- Add examples where format is ambiguous
- Add self-verification where accuracy is critical

### Layer 4: Edge Case Hardening
- Add failure mode handling (what to do when input is incomplete)
- Add boundary conditions (minimum/maximum constraints)
- Add explicit "do NOT" instructions for common mistakes
```
**Used in:** Prompt improvement, prompt review, prompt engineering training, any meta-prompting workflow
**Why it works:** Each layer focuses on one improvement dimension; sequential application ensures no dimension is skipped; produces more consistent improvements than ad-hoc prompt editing
**Different from MP-02:** MP-02 iteratively improves prompts but doesn't specify what to improve at each iteration; MP-08 provides a structured framework with specific focus areas per layer
**See Also:** MP-02 (Recursive Optimization), QA-06 (Constitutional AI for Prompts)
**Reference:** Technique Deduplication Audit, Batch 7b

### MP-09: Pre-AI Thinking Protocol
**What:** A structured set of questions (typically 5-7) answered with pen-and-paper or voice memo *before* engaging AI, to prevent AI's fluency from overriding the user's own intent and judgment
**Pattern:**
```markdown
## Before Opening Any AI Session

Answer these questions AWAY from a screen:

1. What am I actually trying to accomplish? (The outcome, not the task)
2. Why does this matter? (What happens if it goes well vs. not at all?)
3. What does "done" look like? (Describe the finished thing specifically)
4. What does "wrong" look like? (The subtle failure mode, not the obvious one)
5. What do I already know that I haven't written down? (Institutional knowledge)
6. What are the pieces? (Decomposition, dependencies)
7. What's the hard part? (Where judgment calls live)

Bring your answers TO the AI session. Evaluate AI output against YOUR criteria.
```
**Used in:** Pre-session preparation, complex task delegation, specification engineering, any high-stakes AI interaction
**Why it works:** AI fills blanks with statistical plausibility — confident guesses that are easy to mistake for good ideas. Pre-thinking establishes the user's own framing before AI's fluency can reshape it
**Key insight:** "If you walk into a meeting without knowing what you want, the most articulate person in the room decides for you. AI is the most articulate thing you've ever talked to."
**Different from CM-01:** CM-01 provides context *to* AI; MP-09 establishes human clarity *before* AI is involved
**Different from MP-03:** MP-03 has AI ask clarifying questions; MP-09 has the human answer questions alone first

### MP-10: Position Mapping
**What:** Helping users articulate how they differ from the "median user" the AI was trained to satisfy, so they can write instructions that describe a *position* (unique differentiation) rather than a *quality* (things everyone wants)
**Pattern:**
```markdown
## Position Mapping Process

1. Identify your 2-3 most frequent AI tasks
2. Identify what feels "off" about default output for those tasks
3. Map your professional context (role, expertise, audience)
4. For each dimension, articulate:

| Dimension | What AI Assumes (Median) | Your Actual Position |
|-----------|--------------------------|---------------------|
| Expertise | [typical assumption]     | [your reality]      |
| Audience  | [typical assumption]     | [your reality]      |
| Format    | [typical assumption]     | [your reality]      |

5. Convert each gap into a specific steering instruction
```
**Used in:** Custom instruction writing, system prompt design, CLAUDE.md creation, any instruction personalization
**Why it works:** "Be concise" doesn't steer — everyone wants concise. "Answer factual questions in one sentence; use three paragraphs max for analysis" describes an actual position. The further you are from typical, the more configuration matters.
**Key test:** If everyone would want the instruction, it's not specific enough — it describes a quality, not a position
**Different from NE-03:** NE-03 provides templates for structured input; MP-10 helps users *discover* what to put in those templates
**Different from CM-01:** CM-01 frames context for the AI; MP-10 helps users understand what context matters most

### MP-11: Correction Compounding
**What:** Systematically extracting patterns from repeated corrections to AI output and encoding them as reusable instructions — turning every correction into a permanent improvement
**Pattern:**
```markdown
## Correction Compounding Loop

1. Collect 2-3 examples of corrections you've made repeatedly
2. Identify the underlying preference pattern (not the symptom, the position)
3. Check against existing instructions for gaps or conflicts
4. Generate 1-3 new instruction lines that would prevent these corrections
5. Integrate into custom instructions / CLAUDE.md / system prompt

PATTERN: [name the underlying preference]
WHAT YOU'RE ENCODING: [the position this represents]
NEW INSTRUCTIONS:
- [instruction line 1 — prevents specific failure mode]
- [instruction line 2 — if needed]
WATCH FOR: [related patterns to notice next]
```
**Used in:** Custom instruction refinement, CLAUDE.md maintenance, system prompt iteration, any continuous improvement of AI interaction quality
**Why it works:** Every correction is information about an unencoded preference. Capturing it once means never making that correction again. This is the compound interest of AI configuration.
**Different from MP-08:** MP-08 improves prompts through structured layers; MP-11 improves *instructions* through pattern extraction from actual correction history
**Different from QA-06:** QA-06 iterates on a single prompt; MP-11 builds a persistent instruction layer across sessions

---

## Domain-Specific Techniques

### DS-01: Framework Application *(Merged from DS-01 + SV-04)*
**What:** Apply established business/analysis frameworks with optional parameter definitions
**Examples:** SWOT, Porter's Five Forces, Business Model Canvas, OKRs, λ/Δ/θ, TAM/SAM/SOM, RICE
**Pattern (Basic):** Structure analysis around framework's specific dimensions
**Pattern (Advanced with Parameters):**
```markdown
You are a [role] using [Framework Name].

DEFINITIONS:
- [Parameter 1]: [Definition and measurement]
- [Parameter 2]: [Definition and measurement]
- [Parameter 3]: [Definition and measurement]

TASK:
Interview me to estimate my personal [parameters]. Cover:
- [Aspect 1]
- [Aspect 2]

After analysis, provide:
1. My estimated parameters with reasoning
2. [Framework-specific insight]
3. Which parameter is hurting me most
4. The single highest-leverage change
```
**Variants:**
- **Basic:** Reference framework by name, structure analysis around its dimensions
- **Advanced:** Include explicit parameter definitions and measurement criteria
**Used in:** Business analysis (20 prompts), deep work prompts, board-deck prompts
**Why it works:** Leverages proven analytical structures; provides consistent vocabulary; enables quantitative assessment
**Note:** Merged SV-04 into DS-01 (2026-01-22) — SV-04 was advanced variant with parameter definitions
**Reference:** `prompts/productivity/deep-work/deepwork_estimate_focus_parameters.md`

### DS-02: Metric Specification
**What:** Define specific, measurable criteria
**Examples:** Cyclomatic complexity thresholds, documentation coverage %, response times
**Used in:** Code quality, performance analysis
**Why it works:** Provides objective, quantifiable standards
**Variant — Success/Failure Counters:** Batch operation accounting metrics — processed/succeeded/failed/skipped counts as standard output for any batch operation. Provides at-a-glance completeness reporting.
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #12

### DS-03: Tool and Methodology Suggestions
**What:** Recommend specific tools or approaches
**Examples:** "Use profiling tools", "Use PlantUML for diagrams", "Use dependency graphs"
**Used in:** Performance analysis, architecture documentation
**Why it works:** Grounds AI in concrete, practical approaches
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #10

### DS-04: Pattern Recognition Requests
**What:** Identify trends, patterns, systemic issues
**Pattern:** "Identify patterns or trends in [metric] across the codebase"
**Used in:** Code evolution, quality analysis
**Why it works:** Encourages holistic analysis beyond individual issues
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #13

### DS-05: Visualization and Communication Guidance
**What:** Specify how to present findings visually
**Examples:** "Generate heatmaps", "Create entity-relationship diagrams", "Use diagrams for technical and non-technical audiences"
**Used in:** Architecture, database analysis
**Reference:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md` technique #15

### DS-06: Prioritization and Severity Guidance
**What:** Explicit instructions to rank findings
**Approaches:** Severity levels (Low/Medium/High), Impact-based, Effort vs. benefit, Risk assessment
**Used in:** Security analysis, technical debt, optimization
**Why it works:** Makes analysis actionable
**Variant — Critical Warnings Table:** Surface catastrophic issues in a dedicated warnings table *before* the main findings list. Use when some findings are so severe they must not be buried in a ranked list.
**Variant — Priority Hierarchy / Value Conflict Resolution:** Encode organizational values in ranked order with explicit resolution rules for conflicts: "When [Value A] and [Value B] conflict, [Value A] wins. Threshold: [specific boundary]." Use when delegating to agents or team members who need to make judgment calls. Example: "1. Data accuracy — always wins. 2. Response speed — wins against everything below. 3. Comprehensiveness — default optimization when no conflicts."

### DS-13: Architecture-First Enforcement
**What:** Enforce architectural decisions before implementation by sequencing phases and requiring specific outputs as dependencies
**Category:** Domain-Specific
**Use Case:** Large features, API-first development, distributed teams, preventing integration failures
**Pattern:**
```markdown
## Phase 1: Architecture & Design Foundation (REQUIRED BEFORE IMPLEMENTATION)
### Step 1: {LAYER_1_ARCHITECTURE}
**Expected Output:** Database schema, ER diagrams, migration scripts
**Validation Criteria:** Completeness, consistency, review approval
**Blocks:** Phase 2 (Implementation) cannot start until this completes

### Step 2: {LAYER_2_ARCHITECTURE}
**Expected Output:** API contracts, OpenAPI spec, authentication flows
**Blocks:** Phase 2 (Implementation)
```
**Why it works:** Prevents ad-hoc development leading to integration problems; enables parallel development with clear interfaces
**Reference:** [Full documentation: new-techniques/DS_13.md](new-techniques/DS_13.md)

### DS-19: Multi-Source Narrative Synthesis
**What:** Combine structured data from multiple fragmented tools (Git, Jira, Calendar, Slack) into coherent narratives
**Category:** Domain-Specific
**Use Case:** Status reporting, async team communication, stakeholder reporting, fragmented tool landscape
**Pattern:**
```markdown
1. Identify Primary Sources: Define which tools contain relevant information
2. Data Extraction: Extract from each source (API/CLI/Export)
3. Temporal Correlation: Align data by timestamps
4. Conflict Resolution: Reconcile inconsistencies between sources
5. Narrative Generation: Synthesize unified story from correlated data
```
**Why it works:** Systematically correlates data from different sources and generates unified narratives for both technical and non-technical stakeholders
**Reference:** [Full documentation: new-techniques/DS_19.md](new-techniques/DS_19.md)

### DS-20: Frontier Mapping (Capability Classification)
**What:** GREEN/YELLOW/RED classification system for capabilities
**Category:** Domain-Specific
**Use Case:** AI adoption planning, workflow optimization, capability assessment
**Pattern:**
```markdown
GREEN (Generate with AI)
- AI reliably produces usable output
- Verification is fast (glance check)
- Failure is recoverable (regenerate or quick fix)
- Examples: background imagery, decorative elements

YELLOW (Generate with guardrails)
- AI sometimes nails it, sometimes breaks
- Requires specific verification steps
- List the exact guardrails needed

RED (Do not generate)
- AI output requires more fixing than manual creation
- Failure modes are subtle and easy to miss
- Examples: precise data labels, exact brand typography
```
**Why it works:** Creates clear decision boundary for capability use
**Updates:** Weekly review to reclassify based on model improvements or failures
**Output:** One-page map pinned above desk

### DS-21: Proximity Assessment (Timeline Classification)
**What:** Classify capability gaps by timeline to solution
**Category:** Domain-Specific
**Use Case:** Strategic planning, resource allocation, investment timing, capability roadmapping
**Pattern:**
```markdown
PART 2: PROXIMITY ASSESSMENT

For each gap, estimate how close we are to a fix:

NEARLY SOLVED (3-6 months)
- Evidence: Working in labs, announced in beta, multiple teams converging
- Signal to watch: [specific benchmark, product announcement, or research result]

MAKING PROGRESS (6-12 months)
- Evidence: Clear research direction, improving benchmarks, serious investment
- Signal to watch: [specific indicator]

UNCLEAR TIMELINE
- Evidence: Fundamental challenges remain, no clear path
- Signal to watch: [what would change your assessment]
```
**Why it works:** Focuses attention on near-term opportunities
**Three timelines:** 3-6mo / 6-12mo / Unclear
**Each includes:** Evidence + Signal to watch

### DS-25: Chart Selection Dictionary
**What:** Provide a mapping from question types to appropriate visualization types, preventing inappropriate chart selection
**Pattern:**
```markdown
## Chart Selection Guide

| Question Type | Recommended Chart | Avoid |
|--------------|------------------|-------|
| Comparison over time | Line chart, area chart | Pie chart |
| Part-to-whole | Pie chart (≤7 items), treemap (>7) | Line chart |
| Distribution | Histogram, box plot | Bar chart |
| Correlation | Scatter plot, bubble chart | Line chart |
| Ranking | Horizontal bar chart | Pie chart |
| Geographic | Choropleth map, bubble map | Bar chart |

**Anti-patterns:**
- Never use pie charts for >7 categories
- Never use 3D charts (distorts proportions)
- Never use dual y-axes without clear labeling
```
**Used in:** Data analysis, dashboard design, presentation creation, reporting
**Why it works:** Provides specific decision logic for visualization selection, not just "present findings visually"
**Different from DS-05:** DS-05 says to present findings visually; DS-25 provides the specific decision logic for choosing which visualization type
**Reference:** Technique Deduplication Audit, Batch 9

### DS-26: Safe Defaults Pattern
**What:** Ensure every configurable parameter has a documented safe default value that produces reasonable results without user customization
**Pattern:**
```markdown
## Configuration Parameters

| Parameter | Default | Why This Default | When to Change |
|-----------|---------|-----------------|----------------|
| `max_retries` | 3 | Handles transient failures without infinite loops | Increase for unreliable networks |
| `timeout_ms` | 5000 | Balances responsiveness with slow networks | Decrease for real-time systems |
| `batch_size` | 100 | Safe for most memory configurations | Increase for high-memory systems |
| `log_level` | INFO | Sufficient for production monitoring | Set to DEBUG only during troubleshooting |
```
**Used in:** Configuration generation, API design, tool creation, template design
**Why it works:** Users get working output immediately; defaults are documented so users understand what to customize and why
**Different from CM-02:** CM-02 defines constraints (boundaries); DS-26 defines defaults (starting points within boundaries)
**Reference:** Technique Deduplication Audit, Batch 9

### DS-27: Professional Defaults Library
**What:** Provide pre-configured default settings organized by professional use case, offering curated configuration bundles
**Pattern:**
```markdown
## Configuration Profiles

### Profile: Startup MVP
- `auth`: Basic JWT (no SSO)
- `database`: Single instance PostgreSQL
- `monitoring`: Error tracking only
- **Rationale:** Minimal overhead, fastest to deploy

### Profile: Enterprise Production
- `auth`: SSO + MFA + RBAC
- `database`: Multi-region with read replicas
- `monitoring`: Full observability stack (metrics, traces, logs)
- **Rationale:** Compliance-ready, highly available

### Profile: Learning/Experimentation
- `auth`: Disabled (local development)
- `database`: SQLite in-memory
- `monitoring`: Console logging only
- **Rationale:** Zero setup friction
```
**Used in:** Tool configuration, infrastructure provisioning, project scaffolding, development environment setup
**Why it works:** Extends DS-26 from individual parameters to curated configuration bundles per use case; users pick a profile rather than configuring dozens of parameters
**Different from DS-26:** DS-26 provides individual parameter defaults; DS-27 provides complete configuration sets per use case
**Different from DS-80:** DS-80 provides templates at different levels; DS-27 provides configuration sets, not templates
**Reference:** Technique Deduplication Audit, Batch 6

### DS-28: Environment-Specific Guidance
**What:** Provide different recommendations based on the target environment's risk tolerance (development → permissive, staging → moderate, production → strict)
**Pattern:**
```markdown
## Environment-Aware Recommendations

### Development Environment
- **Security:** Permissive CORS, self-signed certificates OK
- **Logging:** Verbose debug logging enabled
- **Error handling:** Full stack traces in responses

### Staging Environment
- **Security:** Production-like CORS, valid certificates
- **Logging:** Structured logging, no debug level
- **Error handling:** Generic error messages, full traces in logs

### Production Environment
- **Security:** Strict CORS, HSTS, CSP headers required
- **Logging:** Structured logging with PII redaction
- **Error handling:** Generic messages only, traces in secure logs
```
**Used in:** Security recommendations, configuration guidance, deployment procedures, testing strategies, monitoring setup
**Why it works:** Prevents one-size-fits-all recommendations; development convenience doesn't compromise production security
**Different from DS-06:** DS-06 ranks findings by severity; DS-28 adapts recommendations to environment risk profiles
**Reference:** Technique Deduplication Audit, Batch 8

### DS-29: Domain Pattern Library
**What:** Include a curated collection of named, reusable patterns specific to the domain, each with working examples and selection guidance
**Pattern:**
```markdown
## API Design Patterns

### Pattern: Pagination
- **Problem:** Client needs to retrieve large datasets efficiently
- **When to use:** Any list endpoint that may return >100 items
- **When NOT to use:** Endpoints that always return ≤10 items
- **Implementation:** Cursor-based pagination with `next_cursor` parameter
- **Example:** `GET /api/users?cursor=abc123&limit=20`
- **Common mistakes:** Using offset pagination for large datasets (O(n) performance)

### Pattern: Idempotency Keys
- **Problem:** Client needs to safely retry requests without duplication
- **When to use:** Any state-changing endpoint (POST, PUT, DELETE)
- **Implementation:** Client-generated UUID in `Idempotency-Key` header
```
**Used in:** API design, architecture patterns, testing patterns, UI patterns, data modeling
**Why it works:** Named patterns with selection guidance prevent inappropriate pattern application; "When NOT to use" is as valuable as "When to use"
**Different from DS-80:** DS-80 provides templates at different complexity levels; DS-29 organizes patterns by the problem they solve
**Reference:** Technique Deduplication Audit, Batch 5

### DS-30: Ecosystem Mapping
**What:** Map capabilities to specific tools in the ecosystem, providing a structured inventory of what tools exist for each need
**Pattern:**
```markdown
## Monitoring Ecosystem Map

| Capability | Recommended | Alternatives | Selection Criteria |
|-----------|-------------|--------------|-------------------|
| Metrics collection | Prometheus | Datadog, CloudWatch | Self-hosted vs managed |
| Log aggregation | Loki | ELK Stack, Splunk | Cost, query complexity |
| Distributed tracing | Jaeger | Zipkin, Tempo | Integration ecosystem |
| Alerting | Alertmanager | PagerDuty, OpsGenie | Routing complexity |
| Dashboards | Grafana | Kibana, Datadog | Data source variety |
```
**Used in:** Technology selection, vendor evaluation, migration planning, team onboarding
**Why it works:** Creates a structured map of the entire ecosystem; prevents tunnel vision on individual tool recommendations
**Different from DS-03:** DS-03 recommends individual tools; DS-30 maps the entire ecosystem with alternatives and selection criteria
**Reference:** Technique Deduplication Audit, Batch 2

### DS-32: Regulatory Enumeration Pattern
**What:** Provide a comprehensive listing of applicable regulations, standards, and compliance requirements for a given domain or jurisdiction
**Pattern:**
```markdown
## Applicable Regulations

| Regulation | Jurisdiction | Covers | Key Requirements | Penalty |
|-----------|-------------|--------|-----------------|---------|
| GDPR | EU/EEA | Personal data protection | Consent, right to erasure, DPO | Up to 4% annual revenue |
| CCPA/CPRA | California | Consumer privacy | Opt-out rights, data disclosure | $7,500 per intentional violation |
| HIPAA | United States | Health information | PHI safeguards, breach notification | Up to $1.5M per category/year |
| SOC 2 | Global (voluntary) | Service organization controls | Security, availability, confidentiality | Loss of certification |
```
**Used in:** Compliance planning, legal analysis, healthcare systems, financial services
**Why it works:** Comprehensive enumeration prevents overlooking applicable regulations; structured format enables gap analysis
**Different from DS-111:** DS-111 enforces adherence to one standard; DS-32 enumerates all applicable standards for awareness
**Reference:** Technique Deduplication Audit, Batch 3

### DS-33: Jurisdiction-Adaptive Output
**What:** Adapt output based on the target jurisdiction, automatically applying jurisdiction-specific rules and conventions
**Pattern:**
```markdown
## Jurisdiction: [Target jurisdiction]

### Applied Rules
- Data residency: [jurisdiction-specific requirement]
- Privacy framework: [GDPR/CCPA/PIPEDA/etc.]
- Tax treatment: [jurisdiction-specific rules]
- Employment law: [at-will/notice period/etc.]

### Multi-Jurisdiction Comparison (if applicable)
| Requirement | US (Federal) | EU (GDPR) | UK (UK GDPR) |
|------------|-------------|-----------|--------------|
| Consent model | Opt-out | Opt-in | Opt-in |
| Breach notification | 60 days | 72 hours | 72 hours |
```
**Used in:** Legal advice, tax guidance, compliance recommendations, privacy policies, cross-border business
**Why it works:** Prevents generic advice that ignores jurisdictional variation; flags items that differ across jurisdictions
**Different from DS-32:** DS-32 lists applicable regulations; DS-33 adapts actual output content based on jurisdiction
**Reference:** Technique Deduplication Audit, Batch 3

### DS-34: Documentation-Driven Testing
**What:** Generate test cases directly from documentation specifications, ensuring docs and tests stay synchronized
**Pattern:**
```markdown
## Documentation → Test Mapping

### Documented Claim: "API returns 200 for valid requests"
**Test case:** `test_valid_request_returns_200()`
**Type:** Automated, regression

### Documented Claim: "Rate limit is 100 requests per minute"
**Test case:** `test_rate_limit_enforced_at_100_rpm()`
**Type:** Automated, load testing

### Documented Claim: "System handles 10,000 concurrent users"
**Test case:** ⚠️ UNTESTABLE in current test environment
**Action needed:** Set up load testing infrastructure

## Coverage Report
- Total documentation claims: 45
- Claims with tests: 38 (84%)
- Untestable claims: 4 (9%)
- Claims missing tests: 3 (7%) ← Action needed
```
**Used in:** API documentation, specification documents, requirement documents, user stories
**Why it works:** Creates a feedback loop between documentation and code; untestable claims indicate either documentation problems or test infrastructure gaps
**Different from QA-10:** QA-10 defines testing checklists; DS-34 derives tests from documentation, keeping docs and tests synchronized
**Reference:** Technique Deduplication Audit, Batches 3/4

### DS-35: LLM-as-Judge with Rubric
**What:** Use one LLM to evaluate the output of another LLM against a defined rubric, producing structured quality scores
**Pattern:**
```markdown
## Evaluation Rubric for [Judge LLM]

You are evaluating the following output against this rubric:

### Scoring Dimensions
1. **Factual Accuracy** (1-5): Are all claims verifiable and correct?
2. **Completeness** (1-5): Are all aspects of the question addressed?
3. **Clarity** (1-5): Is the explanation clear and well-structured?
4. **Actionability** (1-5): Can the reader act on the recommendations?

### Output Format
For each dimension: Score + one-sentence justification
Overall score: Sum/20
Recommendation: ACCEPT (≥16) | REVISE (12-15) | REJECT (<12)

### Improvement suggestions (if REVISE):
- [Specific, actionable feedback for each low-scoring dimension]
```
**Used in:** Prompt evaluation pipelines, content quality assessment, automated grading, LLM-in-the-loop evaluation
**Why it works:** Independent evaluation with structured rubric produces more reliable quality assessment than self-critique alone
**Different from QA-01:** QA-01 is self-critique (same model evaluates own output); DS-35 uses a separate evaluator with an independent rubric
**Different from QA-06:** QA-06 uses principles for critique-revise loops; DS-35 uses a structured rubric with numerical scores
**Reference:** Technique Deduplication Audit, Batch 6

### DS-36: Blocker Escalation Framework
**What:** Provide a structured format for reporting blockers with severity, impact, and escalation path
**Pattern:**
```markdown
## Active Blockers

| # | Blocker | Severity | Blocked Work | Days Blocked | Owner | Escalate By |
|---|---------|----------|-------------|-------------|-------|------------|
| 1 | Auth service migration incomplete | P0 | All API features | 5 days | @backend-team | Feb 12 |
| 2 | Design review pending | P1 | Settings UI | 3 days | @design-lead | Feb 14 |
| 3 | CI pipeline flaky tests | P2 | All PRs (intermittent) | 12 days | @devops | Feb 16 |

## Escalation Rules
- P0: Escalate to VP Engineering if unresolved within 48 hours
- P1: Escalate to Engineering Manager if unresolved within 1 week
- P2: Track in retrospective; escalate if pattern persists >2 weeks
```
**Used in:** Sprint retrospectives, standup reports, project status updates, incident management
**Why it works:** Prevents blockers from being buried in status updates; escalation paths ensure accountability
**Different from DD-11:** DD-11 handles individual blocked gates; DS-36 is a broader framework for surfacing all blockers in a project
**Reference:** Technique Deduplication Audit, Batch 1

### DS-37: Progressive Abstraction Transformation
**What:** Transform content through multiple abstraction levels, each being a complete and accurate representation at that detail level
**Pattern:**
```markdown
## Level 1: Executive Summary (1-2 sentences)
Cache hit rates dropped 40% this week, causing a 3x increase in database load
and degraded API response times.

## Level 2: Management Brief (1 paragraph)
Between Feb 3-9, the Redis cache cluster experienced progressive key eviction
due to memory pressure from the new recommendation engine. This reduced cache
hit rates from 92% to 55%, tripled PostgreSQL query volume, and increased P95
API latency from 120ms to 890ms. The team has identified the root cause and
a fix is scheduled for deployment Feb 10.

## Level 3: Technical Analysis (full report)
[Complete root cause analysis with metrics, graphs, and remediation details]

## Level 4: Raw Data (appendix)
[Prometheus queries, log excerpts, configuration diffs]
```
**Used in:** Report generation, briefing documents, content marketing, knowledge base articles
**Why it works:** Each level is independently useful and accurate; readers access the detail level appropriate to their role
**Different from NE-05:** NE-05 controls output length; DS-37 transforms the same content across multiple abstraction levels
**Reference:** Technique Deduplication Audit, Batch 3

### DS-38: Long-Form Documentation Process
**What:** Define a multi-phase process for generating comprehensive documentation with quality gates between phases
**Pattern:**
```markdown
## Documentation Generation Process

### Phase 1: Outline
- Generate section headers with scope notes
- **Gate:** All topics covered? No redundant sections?

### Phase 2: Draft
- Write each section with full detail
- **Gate:** Each section addresses its scope note? Cross-references correct?

### Phase 3: Self-Review
- Check for completeness, accuracy, internal consistency
- **Gate:** No factual errors? No contradictions between sections?

### Phase 4: Refine
- Improve clarity, add examples, fix formatting
- **Gate:** Readable by target audience? Examples for complex concepts?

### Phase 5: Finalize
- Add table of contents, cross-references, index
- **Gate:** All internal links valid? TOC matches actual sections?
```
**Used in:** Technical documentation, research papers, comprehensive guides, book chapters
**Why it works:** Quality gates between phases catch issues early; each phase has a specific focus preventing cognitive overload
**Different from NE-02:** NE-02 defines generic workflow phases; DS-38 specializes the phased approach for long-form documentation with documentation-specific quality gates
**Reference:** Technique Deduplication Audit, Batches 3/4

### DS-39: Configuration-Driven Workflow Customization
**What:** Define explicit configuration options that modify workflow behavior, allowing users to customize prompt execution without rewriting the prompt
**Pattern:**
```markdown
## Configuration

```yaml
# Required
target_language: python
framework: fastapi

# Optional (defaults shown)
include_tests: true          # Generate test files alongside code
style_guide: google          # google | airbnb | pep8
error_handling: comprehensive # minimal | standard | comprehensive
documentation: inline        # none | inline | docstring | full
```

## Behavior Modifications
- If `include_tests: true` → Generate test file for each module
- If `error_handling: comprehensive` → Add retry logic and circuit breakers
- If `documentation: full` → Generate README.md alongside code
```
**Used in:** Code generators, analysis tools, documentation generators, review workflows
**Why it works:** Users customize behavior through configuration rather than prompt editing; defaults ensure the prompt works without any configuration
**Different from OC-08:** OC-08 switches between discrete modes; DS-39 provides fine-grained configuration within a single workflow
**Reference:** Technique Deduplication Audit, Batch 1

### DS-40: Follow-Up Action Extraction
**What:** As a standard processing step, extract all actionable items from input or generated content, formatting them as a structured action list
**Pattern:**
```markdown
## Extracted Action Items

| # | Action | Owner | Deadline | Source | Priority |
|---|--------|-------|----------|--------|----------|
| 1 | Migrate auth service to new cluster | @backend | Feb 15 | Architecture review discussion | P0 |
| 2 | Update API documentation for v3 endpoints | @docs | Feb 20 | Sprint planning notes | P1 |
| 3 | Schedule load test for payment service | @qa | Feb 12 | Performance review finding | P1 |

## Extraction Method
- Scanned for: decisions made, commitments stated, deadlines mentioned,
  "we should/need to/must" language, assigned tasks
- Deduplicated: Merged 2 duplicate items from different source sections
- Unresolvable: "Someone should look into the caching issue" — no owner or deadline
```
**Used in:** Meeting notes processing, email summarization, document review, project planning
**Why it works:** Systematically surfaces implicit action items that would otherwise be lost in unstructured content
**Different from DD-07:** DD-07 tracks completion evidence for existing tasks; DS-40 extracts future actions from unstructured content
**Reference:** Technique Deduplication Audit, Batch 1

### DS-41: Difficulty Axis Decomposition
**What:** Breaking work into 7 difficulty axes to understand what *type* of hard each task is, enabling targeted AI tool selection and durable skill identification
**Pattern:**
```markdown
## Difficulty Axis Framework

For each task, identify primary and secondary difficulty axes:

| Axis | Definition | AI Capability |
|------|-----------|---------------|
| REASONING | Multi-step logical deduction, novel problem-solving from first principles | Strong (deep reasoning models) |
| EFFORT | Straightforward but voluminous; challenge is scale and thoroughness | Strong (agentic AI) |
| COORDINATION | Aligning people, routing information, managing dependencies | Emerging |
| EMOTIONAL INTELLIGENCE | Reading dynamics, calibrating tone, navigating unspoken context | Weak |
| JUDGMENT & WILLPOWER | Decisions requiring courage, political risk, identity commitment | Negligible |
| DOMAIN EXPERTISE | Pattern recognition from accumulated experience | Emerging |
| AMBIGUITY | Determining the actual question when inputs are contradictory or incomplete | Weak |

Output: % of weekly time per axis + automation timeline (near/medium/long-term)
```
**Used in:** Career strategy, AI tool selection, role analysis, capability assessment, workforce planning
**Why it works:** Most people assume their work is hard because of reasoning; often it's hard because of coordination, ambiguity, or judgment. Correct diagnosis changes which AI tools help and where human value is most durable.
**Key insight:** The "reasoning slice" of most knowledge work is smaller than people assume. The effort slice is larger. This changes the AI investment strategy.
**Different from DT-01:** DT-01 breaks tasks into subtasks; DS-41 categorizes the *type of difficulty* across tasks
**Different from RT-02:** RT-02 analyzes from multiple perspectives; DS-41 categorizes work by cognitive demand type


### DS-43: Auto-Improvement Readiness Requirements Matrix
**What:** A fixed requirement matrix for determining if an agent deployment can support meta-agent optimization, using explicit Present/Partial/Absent scoring per capability.
**Category:** Domain-Specific
**Use Case:** Agent observability audits, readiness reviews, infrastructure gap assessment
**Pattern:**
```markdown
## Requirement Assessment

For each requirement, assign: PRESENT / PARTIAL / ABSENT

| Requirement | Status | Current State Notes | Impact if Missing |
|-------------|--------|---------------------|-------------------|
| Full reasoning traces | [Present/Partial/Absent] | [Evidence] | [Blocked capability] |
| Tool call granularity | ... | ... | ... |
| Decision point visibility | ... | ... | ... |
| Structured format | ... | ... | ... |
| Session reproducibility | ... | ... | ... |
| Baseline snapshots | ... | ... | ... |
| Failure classification | ... | ... | ... |
| Cost and latency tracking | ... | ... | ... |
| Sandboxed execution | ... | ... | ... |
| Evaluation harness | ... | ... | ... |
```
**Used in:** Agent tracing audits, platform readiness reviews, observability remediation planning
**Why it works:** Converts vague "we have some logs" claims into checkable capability states, making remediation sequencing concrete and defensible
**Different from QA-08:** QA-08 checks pass/fail gates for task completion; DS-43 inventories infrastructure capabilities needed for repeated optimization loops

### DS-42: Domain Knowledge Extraction Protocol
**What:** Structured method for drawing out tacit, implicit domain expertise that doesn't exist in training data — the knowledge that lives in practitioners' heads (edge cases, workarounds, tribal knowledge, field-specific intuition)
**Category:** Domain-Specific
**Use Case:** Domain expert interviews, requirements gathering, specification building, knowledge capture
**Pattern:**
```markdown
Phase 1 — Understand the Domain Expert:
1. Ask: "What's your field, role, and how long have you been doing this work?"
2. Ask: "Walk me through a typical day. What are the 3-5 tasks where you think 'there should be software for this' — or where existing tools are terrible and you've built workarounds with spreadsheets, manual processes, or tribal knowledge?"
3. Ask: "For each pain point — who else feels this pain? What's the cost of the current workaround? (Time wasted, errors made, outcomes compromised.)"
4. Ask: "Have you ever requested a tool from IT or pitched an idea that sat in a backlog? What was it?"

Key principle: Never assume you know the user's domain better than they do. The edge cases are where domain expertise lives.
```
**Used in:** Product specification, domain expert enablement, requirements engineering, knowledge management
**Why it works:** Domain expertise is the "irreducible input" that no AI training dataset captures. This protocol systematically surfaces the ER nurse's 3 AM knowledge, the warehouse manager's failure mode intuitions, the teacher's scaffolding instincts — knowledge that makes software actually work in the field.
**Different from NE-08 (Catchall Context Gathering):** NE-08 casts a wide net for general context; DS-42 specifically targets tacit expertise, workarounds, and edge cases that practitioners take for granted
**Different from SV-03 (Interview-to-Synthesis):** SV-03 is a general interview-then-synthesize pattern; DS-42 focuses on extracting domain-specific knowledge that only practitioners possess

---

## Agentic Techniques

Techniques derived from the `agency-agents/` collection of 51 role-based AI agent personas. These techniques focus on persistent identity, multi-agent coordination, and autonomous workflows.

### AG-01: Personality-First Role Definition
**What:** Define agents with personality traits, memory, and experience—not just expertise
**Pattern:**
```markdown
## 🧠 Your Identity & Memory
- **Role**: [Specific specialization]
- **Personality**: [3-4 emotional/behavioral traits]
- **Memory**: You remember [what the agent learns/tracks]
- **Experience**: You've seen [failure patterns that inform behavior]
```
**Used in:** All agency-agents (51 files)
**Why it works:** Creates consistent behavior that goes beyond task execution to include emotional characteristics and learned patterns
**Different from RP-01:** Includes memory, experience, and failure awareness—not just expertise assignment
**Reference:** `agency-agents/design/design_whimsy_injector.md`
**See Also:** RP-01 (basic expertise only), NE-12 (cognitive mode), ST-16 (behavioral traits), AG-26 (AI-augmented)

### AG-02: Skeptical Default Stance
**What:** Default to skepticism/failure, requiring overwhelming proof for approval
**Pattern:**
```markdown
### Stop Fantasy Approvals
- Default to "NEEDS WORK" status unless proven otherwise
- No more "A+ certifications" for basic implementations
- First implementations typically need 2-3 revision cycles
- Honest feedback drives better outcomes
```
**Used in:** `agency-agents/testing/testing_reality_checker.md`
**Use Case:** Quality gates, final approval stages, reality-checking assessments
**Why it works:** Prevents overconfident approvals by inverting the default assumption
**Best for:** Final validation, production readiness certification
**Different from QA-08:** AG-02 sets default stance (skeptical); QA-08 defines gate structure
**Different from DP-05:** AG-02 is always skeptical; DP-05 scales scrutiny with stakes

### AG-03: Layered Mission Hierarchy
**What:** Primary → Secondary → Tertiary missions with default requirements
**Pattern:**
```markdown
## 🎯 Your Core Mission

### Primary Mission: [Main Focus]
- [Key responsibility 1]
- [Key responsibility 2]
- **Default requirement**: [Non-negotiable standard]

### Secondary Mission: [Supporting Focus]
- [Supporting responsibility 1]

### Tertiary Mission: [Enabling Focus]
- [Enabling responsibility 1]
```
**Used in:** Most agency-agents
**Why it works:** Creates clear prioritization when missions conflict; ensures defaults are never skipped
**Reference:** `agency-agents/design/design_whimsy_injector.md`

### AG-04: Behavioral Guardrails *(Merged from AG-04 + AG-23)*
**What:** Explicit behavioral constraints that apply to all agent actions—"must follow" rules that override other considerations
**Pattern:**
```markdown
## 🚨 Critical Rules You Must Follow

### [Rule Category 1]
- [Specific behavioral directive]
- [Non-negotiable requirement]

### [Rule Category 2]
- [Hard constraint]
- [Safety guardrail]
```
**Use Cases:** Agent consistency, safety, compliance, quality gates
**Used in:** All agency-agents
**Priority:** HIGH (essential for agent consistency)
**Different from CM-02 (Constraints):** These are behavioral directives, not input/output constraints
**Why it works:** Prevents agents from rationalizing shortcuts under pressure
**Note:** Merged AG-23 into AG-04 (2026-01-22) — identical concept, consolidated into single technique
**Reference:** `agency-agents/specialized/agents_orchestrator.md`

### AG-05: Concrete Deliverable Templates
**What:** Include actual working code/examples, not placeholder templates
**Pattern:** Provide full CSS, JavaScript, SQL, configuration files—not `[your code here]` placeholders
**Example (from Whimsy Injector):**
```css
.btn-whimsy {
  position: relative;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1);

  &:hover {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
  }
}
```
**Used in:** Engineering and design agents
**Why it works:** Provides immediately usable outputs rather than structures requiring additional work
**Variant — Real-World Example Section:** Dedicated end-to-end production example section showing the deliverable in real-world use. Goes beyond a code snippet to show the complete context including setup, usage, and expected output.
**Variant — Complete Usage Example Section:** Step-by-step usage demonstrations showing how to use generated output. Extends deliverable templates with usage guidance: "Here's the output; here's how to use it."
**Reference:** `agency-agents/design/design_whimsy_injector.md`

### AG-06: Memory & Learning Architecture
**What:** Explicit sections defining what the agent learns and remembers over time
**Pattern:**
```markdown
## 🔄 Learning & Memory

Remember and build expertise in:
- **[Pattern category 1]** that [outcome]
- **[Pattern category 2]** that [outcome]

### Pattern Recognition
- Which [X] lead to [positive outcome] vs. [negative outcome]
- How [variable] affects [result]
- When [condition] works better than [alternative]
```
**Used in:** All agency-agents
**Use Case:** Agents that improve with experience across sessions
**Why it works:** Creates framework for accumulated learning and pattern recognition
**Reference:** `agency-agents/design/design_whimsy_injector.md`

### AG-07: Pipeline Orchestration Patterns
**What:** Multi-agent coordination with explicit handoff protocols and decision logic
**Pattern:**
```markdown
## 🔄 Your Workflow Phases

### Phase 1: [Initial Phase]
- Spawn [Agent A] to [task]
- Wait for completion
- Verify deliverables

### Phase 2: [Next Phase]
- Spawn [Agent B] with context from Phase 1
- Validate quality gate

### Decision Logic
IF [condition] = PASS: Advance to next phase
IF [condition] = FAIL: Loop back with feedback (max 3 retries)
IF retries >= 3: Escalate with detailed report
```
**Used in:** `agency-agents/specialized/agents_orchestrator.md`
**Use Case:** Complex multi-agent workflows, autonomous pipelines
**Why it works:** Enables autonomous operation with quality gates and error recovery
**Reference:** `agency-agents/specialized/agents_orchestrator.md`
**Variant — Explicit Agent Handoff Protocol:** Adds failure-triggered handoff — when agent A fails, agent B takes over with full context transfer. Define handoff payload: what context transfers, what resets, and how the receiving agent knows this is a handoff (not a fresh start).
**See Also:** ST-02 (single AI steps), NE-02 (dialogue phases), DT-01 (task decomposition)

### AG-08: Evidence-Based Decision Gates
**What:** Require visual/quantitative proof, not just assertions
**Pattern:**
```markdown
## 🚫 Automatic FAIL Triggers

### Evidence Failures
- Can't provide screenshot evidence
- Previous issues still visible in screenshots
- Claims don't match visual reality
- Specification requirements not implemented

### Fantasy Assessment Indicators
- Claims of "zero issues found"
- Perfect scores without supporting evidence
- "Production ready" without demonstrated excellence
```
**Used in:** Testing agents (`testing_reality_checker.md`, `testing_evidence_collector.md`)
**Why it works:** Prevents approval based on assertions; requires concrete proof
**Different from RT-05:** AG-08 is approval-specific (pass/fail gates); RT-05 is general evidence requirement
**Reference:** `agency-agents/testing/testing_reality_checker.md`

### AG-09: Anti-Pattern & Failure Mode Embedding
**What:** Explicitly document what leads to failure, embedded in agent identity
**Pattern:**
```markdown
## 🧠 Your Identity & Memory
- **Experience**: You've seen [specific failure pattern] when [cause]
- **Experience**: You've seen too many [bad outcome] for [situation]

## 🚫 What You Must Avoid
- [Anti-pattern 1]: Because [consequence]
- [Anti-pattern 2]: Because [consequence]
```
**Used in:** PM agents, testing agents, orchestrator
**Why it works:** Encodes hard-won lessons directly into agent behavior
**Variant — Anti-Pattern Table with Solutions:** Use structured Problem/Solution table format: `| Anti-Pattern | Why It's Bad | Correct Pattern |` for systematic anti-pattern documentation.
**Reference:** `agency-agents/project-management/project_manager_senior.md`

### AG-10: Emotional Context Spectrum
**What:** Define how personality adapts across different emotional contexts
**Pattern:**
```markdown
## Personality Spectrum
**Professional Context**: [How agent behaves in serious moments]
**Casual Context**: [How agent expresses in relaxed interactions]
**Error Context**: [How agent maintains personality during problems]
**Success Context**: [How agent celebrates achievements]
```
**Used in:** `agency-agents/design/design_whimsy_injector.md`
**Use Case:** Brand consistency, user-facing communications, UX copy
**Why it works:** Ensures consistent personality expression across all touchpoints
**Reference:** `agency-agents/design/design_whimsy_injector.md`

### AG-11: Taxonomy-Based Classification Systems
**What:** Create structured taxonomies for categorizing approaches/elements
**Pattern:**
```markdown
## [Element] Taxonomy

**[Category 1] - [Short description]**:
- [Specific example 1]
- [Specific example 2]

**[Category 2] - [Short description]**:
- [Specific example 1]
- [Specific example 2]

**[Category 3] - [Short description]**:
- [Specific example 1]
- [Specific example 2]
```
**Example (Whimsy Taxonomy):**
- **Subtle Whimsy**: Hover effects, loading animations
- **Interactive Whimsy**: Click animations, form celebrations
- **Discovery Whimsy**: Easter eggs, keyboard shortcuts
- **Contextual Whimsy**: 404 pages, empty states, seasonal themes
**Used in:** Design agents, UX agents
**Why it works:** Provides systematic framework for categorizing and applying different approaches
**Reference:** `agency-agents/design/design_whimsy_injector.md`

### AG-12: Quantitative Success Metrics
**What:** Define success with specific, measurable thresholds and realistic expectations
**Pattern:**
```markdown
## 🎯 Your Success Metrics

You're successful when:
- [Metric 1] shows [specific threshold] (e.g., 40%+ improvement)
- [Metric 2] maintains [standard] (e.g., accessibility compliance)
- [Metric 3] achieves [target] (e.g., < 3 second load time)
- [Realistic expectation]: First implementations need 2-3 revision cycles

## Quality Rating Scale
- C+/B-: Normal for first implementations
- B/B+: Good quality after revisions
- A-/A: Exceptional, requires demonstrated excellence
```
**Used in:** All agency-agents (Success Metrics section)
**Why it works:** Sets clear, measurable targets while maintaining realistic expectations
**Reference:** `agency-agents/testing/testing_reality_checker.md`

### AG-13: Parallel-Converge Orchestration
**What:** Enable explicit support for parallel agent execution with defined convergence points for synchronization and integration
**Category:** Agentic
**Use Case:** Independent work streams, multi-agent systems, time-sensitive projects, resource optimization
**Pattern:**
```markdown
## Phase {N}: Foundation (Sequential)
Output: Contracts/Specifications → Passes to all parallel tracks

## Phase {N+1}: Parallel Execution
### Track A: {COMPONENT_A} (Agent: {SPECIALIST_A})
### Track B: {COMPONENT_B} (Agent: {SPECIALIST_B})
### Track C: {COMPONENT_C} (Agent: {SPECIALIST_C})
**Coordination:** All tracks run simultaneously, no dependencies

## Phase {N+2}: Convergence Point (Integration Required)
Prerequisites: All parallel tracks must complete
Integration: Combine outputs, validate against contracts, test interactions
```
**Why it works:** Maximizes development velocity through concurrent work while ensuring integration quality at convergence points
**Reference:** [Full documentation: new-techniques/AG_13.md](new-techniques/AG_13.md)

### AG-14: Cost-Aware Agent Orchestration
**What:** Strategically assign LLM models (Opus/Sonnet/Haiku) based on task criticality, treating cost as explicit optimization parameter
**Category:** Agentic
**Use Case:** Multi-agent systems, production AI systems, high-volume workflows, quality-cost tradeoffs
**Pattern:**
```markdown
Model Tier Definitions:
- Tier 1 (Opus): Critical architecture, security, code review (~$15/$75 per 1M tokens)
- Tier 2 (Sonnet): Complex but not critical tasks (~$3/$15 per 1M tokens)
- Tier 3 (Haiku): Fast operational tasks (~$0.25/$1.25 per 1M tokens)

Task Classification:
For each workflow step, evaluate:
- Complexity (simple/moderate/complex)
- Criticality (low/medium/high)
- Reversibility (easy to fix / hard to fix / irreversible)
Then assign appropriate model tier
```
**Why it works:** Optimizes cost-to-value ratio by using expensive models only where mistakes are costly to fix
**Reference:** [Full documentation: new-techniques/AG_14.md](new-techniques/AG_14.md)

### AG-15: Staged Rollout with Automatic Rollback
**What:** Progressively deploy improved AI agents through incremental traffic stages (Alpha 5% → Beta 20% → Canary 50% → Full 100%) with automated rollback triggers
**Category:** Agentic
**Use Case:** Production AI agents, high-stakes applications, continuous improvement, risk mitigation
**Pattern:**
```markdown
Stage 1: Alpha (5% traffic, 24-48 hours)
- Monitor: Success rate, latency, error rate
- Rollback trigger: Success rate < baseline - 5%

Stage 2: Beta (20% traffic, 48-72 hours)
- Rollback trigger: Success rate < baseline - 3%

Stage 3: Canary (50% traffic, 72-96 hours)
- Rollback trigger: Success rate < baseline - 2%

Stage 4: Full (100% traffic)
- Continuous monitoring with instant rollback capability
```
**Why it works:** Mitigates risk by exposing new versions to progressively larger populations with data-driven validation before full rollout
**Reference:** [Full documentation: new-techniques/AG_15.md](new-techniques/AG_15.md)

### AG-26: AI-Augmented Expertise
**What:** Define expertise that integrates AI tools as core capability, not optional enhancement
**Category:** Agentic
**Use Case:** Modern development workflows, AI-native processes, Claude Code agents, AI-assisted engineering
**Pattern:**
```markdown
## Your Expertise
You are a [domain] expert with deep fluency in AI-assisted workflows:

### Domain Knowledge
- [Traditional expertise area 1]
- [Traditional expertise area 2]

### AI Tool Fluency (Core Skills)
- **Claude Code**: Multi-file edits, codebase exploration, test generation
- **AI-Assisted Debugging**: Using AI to trace issues, generate hypotheses
- **Prompt Engineering**: Crafting effective prompts for sub-tasks
- **AI Code Review**: Leveraging AI for security scanning, style checks

### Integration Mindset
- Default to AI-assisted approaches for [task types]
- Know when human judgment supersedes AI suggestions
- Can orchestrate multiple AI tools in workflows
```
**Used in:** Opus 4.5-class agents, AI-native development teams, Claude Code skill authors
**Why it works:** Recognizes AI as fundamental capability, not auxiliary tool; models the reality of modern AI-augmented workflows; enables agents that can effectively leverage their own capabilities
**Example:** A "senior engineer with AI fluency" knows not just Python, but how to use Claude Code to refactor, generate tests, and explore unfamiliar codebases
**Different from RP-01:** AG-26 includes AI tool fluency as a *core* skill integrated into expertise; RP-01 defines domain expertise only
**Different from AG-01:** AG-26 focuses specifically on AI-augmented expertise; AG-01 focuses on personality, memory, and learned experience
**Different from NE-12:** AG-26 adds AI tool capabilities to the role; NE-12 sets cognitive/reasoning mode without tool fluency
**Different from ST-16:** AG-26 defines what the AI *can do* (including AI tools); ST-16 defines how the AI *behaves*
**Reference:** Extracted from Opus 4.5-class agent patterns; Priority 3 technique
**See Also:** RP-01 (basic expertise only), AG-01 (full persona with memory), NE-12 (cognitive mode), ST-16 (behavioral traits)

### AG-19: Time-Critical Response Protocol
**What:** Define time-boxed crisis action protocols with specific actions per time window (e.g., "First 15 minutes", "First hour", "First day")
**Pattern:**
```markdown
## Incident Response Protocol

### First 15 Minutes (Triage)
- **Actions:** Confirm incident, assess blast radius, notify on-call
- **Decisions:** Severity level (P0-P3), communication channel
- **Gather:** Error rates, affected services, timeline of first report
- **Escalate if:** Multiple services affected OR customer data at risk

### First Hour (Containment)
- **Actions:** Implement immediate mitigation, establish war room
- **Decisions:** Rollback yes/no, customer communication needed?
- **Gather:** Root cause hypothesis, affected customer count
- **Escalate if:** Mitigation ineffective after 30 minutes

### First Day (Resolution)
- **Actions:** Implement permanent fix, draft incident report
- **Decisions:** Post-incident review timing, preventive measures
- **Gather:** Complete timeline, contributing factors, metrics
```
**Used in:** Incident response, security breach protocols, production outage runbooks, crisis communication
**Why it works:** Time windows prevent analysis paralysis; pre-defined actions per window ensure nothing is missed under pressure
**Different from NE-02:** NE-02 defines phases for normal workflow; AG-19 defines time-boxed phases for crisis scenarios where speed matters
**Reference:** Technique Deduplication Audit, Batches 3/4

### AG-20: Meta-Skill Pattern (Discovery)
**What:** Define a skill whose primary purpose is to discover and invoke other skills, acting as a router or search layer across available capabilities
**Pattern:**
```markdown
## Capability Discovery Process

1. **Accept intent:** User describes what they need in natural language
2. **Search capabilities:** Match intent against available skills/resources
   - Keyword matching against skill names and descriptions
   - Capability matching against skill "Can Do" lists
   - Domain matching against skill categories
3. **Rank matches:** Order by relevance score
4. **Present options:**
   | Rank | Skill | Match Reason | Confidence |
   |------|-------|-------------|-----------|
   | 1 | security-audit | Exact keyword match | 95% |
   | 2 | code-review | Partial capability overlap | 70% |
5. **Invoke selected:** Load and execute the chosen skill
```
**Used in:** Multi-skill agent systems, plugin architectures, capability registries, tool selection in agentic workflows
**Why it works:** Enables scaling to many skills without requiring users to know every skill name; the discovery layer acts as a natural language router
**Different from AG-18:** AG-18 teaches skill creation (meta-creation); AG-20 discovers existing skills (meta-discovery)
**Reference:** Technique Deduplication Audit, Batch 5

### AG-21: Orchestration with Dual-Path Output
**What:** Generate output through two independent paths (different approaches, models, or prompts) and present both for comparison or merge the best elements
**Pattern:**
```markdown
## Dual-Path Generation

### Path A: Conservative Approach
- Strategy: Follow established best practices
- Output: [Generated result A]

### Path B: Innovative Approach
- Strategy: Explore novel solutions
- Output: [Generated result B]

### Comparison
| Criterion | Path A | Path B | Winner |
|-----------|--------|--------|--------|
| Safety | ★★★★★ | ★★★☆☆ | A |
| Innovation | ★★☆☆☆ | ★★★★★ | B |
| Feasibility | ★★★★☆ | ★★★☆☆ | A |

### Recommendation
[Merge best elements: safety approach from A + innovative feature from B]
```
**Used in:** Content generation, code review, decision support, architecture design
**Why it works:** Independent perspectives improve quality through comparison; prevents the single-path bias of always following one approach
**Different from AG-13:** AG-13 runs parallel agents and converges results; AG-21 specifically uses dual paths for quality through comparison — a verification technique, not just parallelism
**See Also:** AG-13 (Parallel-Converge Orchestration), QA-15 (Self-Consistency)
**Reference:** Technique Deduplication Audit, Batch 9

### AG-27: End-State Task Specification
**What:** Frame agent tasks as desired outcomes with observable success criteria and verification commands — not implementation steps. The core mental model shift from "how to do it" to "what done looks like."
**Category:** Agentic
**Use Case:** Agentic coding workflows, task delegation to AI agents, autonomous task execution
**Pattern:**
```markdown
## Task Specification

**Task Summary:** [One sentence describing the goal — not the steps]

**Success Criteria:** [Observable outcomes that define "done"]
- Test X passes
- Behavior Y works
- File Z exists

**Context for the Agent:** [Background info, relevant files, constraints]

**Verification Command(s):** [Specific runnable commands proving success]
- `npm test`
- `cargo build`

**Ready-to-Paste Prompt:**
"Your task: [goal]. You are done when: [success criteria]. Context: [relevant info]. Keep iterating until [verification] passes."
```
**Used in:** Agent task delegation, Claude Code workflows, Codex CLI, Cursor Agent Mode
**Why it works:** End-state specifications let agents choose their own implementation path while maintaining clear accountability; verification commands create the feedback loop that enables autonomous operation
**Different from QA-08:** QA-08 defines binary pass/fail gates within a workflow; AG-27 defines the entire task framing as outcome-oriented with concrete verification
**Different from AG-12:** AG-12 defines quantitative success metrics; AG-27 structures the complete task specification around outcomes
**See Also:** QA-08 (Gate-Based Verification), AG-12 (Quantitative Success Metrics), AG-29 (Agent Loop Architecture)

### AG-28: Oversight-Risk Calibration
**What:** Multi-level framework matching human oversight intensity to task context — stakes, greenfield/brownfield, code familiarity, and reversibility determine how closely to supervise an agent.
**Category:** Agentic
**Use Case:** Agentic coding risk assessment, developer-agent trust calibration, team AI adoption
**Pattern:**
```markdown
## Oversight Calibration Framework

**Level 1 — Let It Run (Far Distance)**
- Conditions: Low stakes, greenfield, can restart cheaply, personal project
- Practice: Define success criteria, kick off agent, check results when done

**Level 2 — Check Milestones (Medium Distance)**
- Conditions: Moderate stakes, some existing code, reversible decisions
- Practice: Review after each major task, spot-check diffs, trust tests

**Level 3 — Watch the IDE (Close Distance)**
- Conditions: Higher stakes, production code, brownfield with conventions
- Practice: Keep agent visible, intervene when off-track

**Level 4 — Review Every Change (Very Close)**
- Conditions: High stakes, security/financial/health, team codebase
- Practice: Approve each diff, treat agent as drafting assistant
```
**Used in:** Pre-flight risk assessment before agent work, team AI governance, developer onboarding to agentic workflows
**Why it works:** Neither "watch every line" nor "let it run unsupervised" is universally correct; matching oversight to context prevents both paranoia and recklessness
**Different from DP-05:** DP-05 defines mandatory approval gates that scale with risk; AG-28 defines continuous oversight levels across a spectrum with specific practices at each level
**Different from CM-09:** CM-09 defines authority boundaries (what agent can/cannot do); AG-28 defines how closely a human monitors what the agent does within those boundaries
**See Also:** DP-05 (Stakes-Based Gate Policy), CM-09 (Authority Boundary Specification), AG-30 (Pre-Execution Risk Audit)

### AG-29: Agent Loop Architecture
**What:** Design complete iteration loops with cycle definition (try → check → adjust), exit conditions, checkpoint strategy, stuck detection, and tool-specific implementation sketches.
**Category:** Agentic
**Use Case:** Long-running agent tasks, multi-iteration autonomous workflows, overnight agent runs
**Pattern:**
```markdown
## Agent Loop Specification

**Loop Goal:** [What state we're iterating toward]

**Iteration Cycle:**
1. [Action the agent takes]
2. [How to check if it worked]
3. [What to do if it failed — adjustment step]
4. [Repeat condition]

**Exit Condition:** The loop terminates when:
- [Primary success condition]
- [Fallback conditions]

**Checkpoint Strategy:**
- Commit frequency: [After each successful iteration / after N iterations]
- State to preserve: [Files changed, decisions, context to carry forward]
- Recovery point: [How to resume if loop crashes or context fills]

**Stuck Detection:** The agent is stuck when:
- Same error 3+ times
- No progress for N iterations

**Stuck Protocol:**
1. [First response — try alternative approach]
2. [Escalation — commit partial progress, stop, notify]
```
**Used in:** Ralph-style bash loops, Claude Code task systems, overnight autonomous runs, complex refactoring
**Why it works:** Loops with clear exit conditions and checkpoint strategies prevent both infinite token burn and lost progress; stuck detection prevents hammering on unsolvable problems
**Different from AG-07:** AG-07 defines multi-agent pipeline handoff protocols; AG-29 defines single-agent iteration loops with self-correction, checkpoints, and stuck handling
**Different from QA-13:** QA-13 specifies failure recovery rules; AG-29 designs complete loop architecture including the recovery as one component
**See Also:** AG-07 (Pipeline Orchestration), AG-31 (Feedback Signal Inventory), CM-08 (File-Based State Persistence), QA-13 (Failure Recovery Specification)

### AG-32: Pre-Execution Risk Audit
**What:** Systematic pre-flight audit of agent plans against common failure patterns before execution — a checklist of "footgun" patterns that indicate speed without discipline.
**Category:** Agentic
**Use Case:** Pre-flight check before significant agent work, prompt review, team quality gates
**Pattern:**
```markdown
## Footgun Scan

| Pattern | Status | Notes |
| --- | --- | --- |
| Vague Success Criteria | ✅ Clear / ⚠️ Fuzzy / 🚨 Missing | [Specifics] |
| Missing Design Phase | ✅ Designed / ⚠️ Partial / 🚨 Winging It | [Specifics] |
| Scope Creep Risk | ✅ Tight / ⚠️ Loose / 🚨 Unbounded | [Specifics] |
| Abstraction Bloat | ✅ Constrained / ⚠️ Risk / 🚨 Likely | [Specifics] |
| No Checkpoint Strategy | ✅ Has One / ⚠️ Implicit / 🚨 None | [Specifics] |
| Wrong Tool | ✅ Good Fit / ⚠️ Questionable / 🚨 Overkill | [Specifics] |

**Overall Risk Level:** [Low / Medium / High / Reconsider]
```
**Used in:** Agent task review, team AI governance, prompt quality gates, developer self-checks
**Why it works:** Agents execute bad decisions at speed — auditing the plan before execution catches "impressive output that nobody can maintain" before it's built; "Reconsider" is a valid output when the answer is "don't use an agent"
**Different from AG-09:** AG-09 embeds anti-patterns into agent identity as permanent behavioral guardrails; AG-32 is a one-time pre-flight audit checklist applied to specific plans before execution
**Different from DP-28:** DP-28 uses traffic-light verdicts for assessment output; AG-32 applies traffic-light status specifically to six agentic failure patterns
**See Also:** AG-09 (Anti-Pattern & Failure Mode Embedding), DP-28 (Traffic-Light Verdict System), AG-27 (End-State Task Specification)

### AG-33: Feedback Signal Inventory
**What:** Explicitly catalog available feedback mechanisms (tests, linter, build output, type checker, etc.) before designing agent workflows. The strength of feedback signals determines how much autonomy an agent can safely have.
**Category:** Agentic
**Use Case:** Agent loop design, oversight calibration, workflow architecture
**Pattern:**
```markdown
## Feedback Signals Available

**Strong Signals (Tight Feedback):**
- [ ] Test suite (`npm test`, `pytest`, etc.)
- [ ] Type checker (`tsc --noEmit`, `mypy`, etc.)
- [ ] Linter output
- [ ] Build result (`cargo build`, `go build`, etc.)

**Medium Signals:**
- [ ] Manual review checkpoints
- [ ] Integration test results
- [ ] Performance benchmarks

**Weak Signals (Loose Feedback):**
- [ ] "It looks right" visual inspection
- [ ] No automated checks available

**Assessment:** [Strong/Medium/Weak feedback environment]
**Risk Note:** [If feedback is weak, flag as risk — loops work best with tight feedback]
```
**Used in:** Pre-flight assessment before agent loop design, oversight calibration, workflow planning
**Why it works:** Feedback signal strength directly determines how much autonomy is safe — tight feedback (tests, types) enables "let it run" mode; weak feedback (no tests) requires close human oversight
**Different from AG-12:** AG-12 defines success metrics with thresholds; AG-33 inventories the *mechanisms* available to provide feedback during iteration
**Different from AG-29:** AG-29 designs the full loop architecture; AG-33 is a prerequisite step that catalogs what feedback the loop can use
**See Also:** AG-29 (Agent Loop Architecture), AG-28 (Oversight-Risk Calibration), AG-12 (Quantitative Success Metrics)


### AG-34: Optimization Triplet Readiness Gating
**What:** A staged diagnostic that blocks progression until three prerequisites are concrete: editable surface, optimization metric, and experiment time budget.
**Category:** Agentic
**Use Case:** Auto-improvement readiness checks before launching meta-agent loops
**Pattern:**
```markdown
Phase 1: Editable Surface Gate
- Must name exact file/config/prompt/parameter set
- Must be isolated and reversible

Phase 2: Metric Gate
- Must be automated, scalar/composite, bounded-time
- Must map to business value

Phase 3: Time Budget Gate
- Must support high-volume experiments
- Must be cost-bounded and sandboxed

Outcome:
- If all pass → program.md optimization spec
- If any fail → blocker report with remediation sequence + timeline
```
**Used in:** Readiness diagnostics, optimization program definition, infra planning
**Why it works:** Prevents premature automation by forcing measurable prerequisites before experimentation starts
**Different from AG-32:** AG-32 audits execution-plan footguns; AG-34 validates whether the *system itself* is suitable for iterative optimization

### AG-35: Trace Infrastructure Gap Audit
**What:** Evaluate agent observability infrastructure against specific auto-improvement capabilities and produce prioritized build-vs-buy remediation plans.
**Category:** Agentic
**Use Case:** Agent platform maturity audits, observability roadmap planning
**Pattern:**
```markdown
1. Capture current-state details (harness, logs, evaluation, infra)
2. Rate each requirement Present/Partial/Absent
3. Split gaps into Critical vs Partial
4. For each gap: blocked capability, minimum viable fix, build-vs-buy option, effort estimate
5. Output readiness verdict + one highest-impact action for this week
```
**Used in:** Agent platform audits, trace pipeline design, readiness governance
**Why it works:** Connects missing telemetry directly to blocked optimization behaviors, making prioritization unambiguous
**Different from DS-43:** DS-43 defines the assessment matrix itself; AG-35 is the full audit workflow and remediation decision process


### AG-36: Build-vs-Buy Observability Remediation
**What:** For each missing auto-improvement capability, produce minimum viable implementation paths with explicit build-vs-buy options and effort estimates.
**Category:** Agentic
**Use Case:** Infrastructure backlog planning, tool selection, platform roadmap sequencing
**Pattern:**
```markdown
For each critical/partial gap:
- Blocked capability
- Minimum viable implementation
- Build recommendation (custom stack, estimated team/time)
- Buy recommendation (specific platform and feature usage)
- Effort estimate (days/weeks + team size)

Prioritize sequence by leverage and dependency order.
```
**Used in:** Agent observability modernization, platform readiness execution plans
**Why it works:** Prevents audits from stalling at diagnosis by turning every gap into a concrete execution decision with cost/time implications
**Different from AG-35:** AG-35 is the complete audit process; AG-36 is the remediation decision pattern applied per identified gap

### AG-37: Description-as-Trigger Discipline
**What:** The `description` field of a skill/agent is the *only* signal the host model uses to decide activation. All trigger keywords, user phrases, and exclusion clauses must live there — not in the body.
**Category:** Agentic
**Use Case:** Skill / agent authoring; activation accuracy; reducing missed and wrong activations
**Pattern:**
```yaml
---
name: seo-audit
description: "When the user wants to audit, review, or diagnose SEO issues. Also use when the user mentions 'SEO audit,' 'why am I not ranking,' 'on-page SEO,' 'meta tags review,' 'page speed,' 'core web vitals,' 'crawl errors,' or 'indexing issues.' For programmatic page generation, see programmatic-seo. For schema, see schema-markup."
---
```
**Used in:** `domain-agentic-resources/skills/marketing/*` (40 skills), `domain-agentic-resources/skills/developer-tools/designing-workflow-skills/SKILL.md`
**Why it works:** Body sections like "When to Use" only constrain behavior *after* the skill is loaded — they cannot cause loading. Front-loading trigger phrases into the description fixes activation accuracy across heterogeneous user phrasing.
**Different from RP-01 (Role Definition):** RP-01 sets the persona for execution; AG-37 controls whether the skill is selected at all.

### AG-38: Sibling-Skill Cross-Reference for Scope Boundaries
**What:** Each skill's description names adjacent skills with different scope ("For X, see other-skill") so the model routes to the correct skill instead of the closest-match one.
**Category:** Agentic
**Use Case:** Skill ecosystems where multiple skills share trigger keywords; reducing wrong-skill activations
**Pattern:**
```yaml
description: "When the user wants conversion optimization on a marketing page. Use for 'CRO,' 'conversion rate optimization,' 'this page isn't converting.' For signup flows, see signup-flow-cro. For onboarding, see onboarding-cro. For paywalls, see paywall-upgrade-cro. For popups, see popup-cro."
```
**Used in:** Marketing skill collection (page-cro, signup-flow-cro, onboarding-cro, etc.); Trail of Bits security plugins
**Why it works:** Without explicit boundaries, an over-broad description ("CRO") activates whenever any conversion topic appears. Naming siblings creates a routing graph the model can follow.
**Different from AG-37:** AG-37 governs activation triggers in isolation; AG-38 disambiguates between skills that overlap.

### AG-39: Foundation Context Document Pattern
**What:** A single shared context document (e.g., `.agents/product-marketing-context.md`) that *every* related skill reads first before doing work, so foundational facts (audience, positioning, ICP, tech stack) are never re-asked.
**Category:** Agentic
**Use Case:** Multi-skill workflows in a single domain; persistent project memory; eliminating repeated user briefings
**Pattern:**
```markdown
**Initial Assessment:**
If `.agents/product-marketing-context.md` exists, read it before asking questions.
Use that context and only ask for information specific to this task.
If it does not exist, run the `product-marketing-context` skill first to create it.
```
**Used in:** Marketing skills (product-marketing-context as foundation; all 40 skills reference it); pattern generalizes to engineering (`.agents/engineering-context.md`), research (`.agents/research-context.md`), etc.
**Why it works:** Skills compose through a shared filesystem context rather than parameter passing. Cost: one well-maintained doc. Benefit: every downstream skill skips foundational interrogation.
**Different from CM-01 (Context Framing):** CM-01 frames context inside one prompt; AG-39 establishes a *persistent on-disk* context referenced by many skills.
**See Also:** AG-06 (Memory & Learning Architecture), AG-37 (Description-as-Trigger).

### AG-40: Numbered Phase Discipline (Entry / Actions / Exit)
**What:** Every phase of a workflow skill carries an explicit number, entry criteria, numbered actions, and exit criteria — never unnumbered prose.
**Category:** Agentic
**Use Case:** Workflow skills, multi-step pipelines, staged audits, anything where execution order matters
**Pattern:**
```markdown
## Phase 2: Vocabulary Discovery

**Entry criteria:**
- Phase 1 scan complete
- Candidate symbol list written to `.cache/symbols.json`

**Actions:**
1. Read symbol list
2. For each symbol, classify by dimension family
3. Write annotated dictionary to `.cache/dimensions.json`

**Exit criteria:**
- Every symbol has a dimension or `unknown` tag
- Coverage gate ≥ 95% before proceeding to Phase 3
```
**Used in:** `dimensional-analysis`, `designing-workflow-skills`, `audit-context-building`, most Trail of Bits workflow skills
**Why it works:** Unnumbered prose produces unreliable execution order; entry/exit criteria let the model self-verify "am I done with this phase?" before advancing.
**Different from ST-02 (Sequential Instructions):** ST-02 lists steps; AG-40 adds the gating criteria that govern when one phase ends and the next begins.
**Different from NE-02 (Phased Workflow):** NE-02 is dialogue-paced phases for human conversation; AG-40 is autonomous-execution phases with machine-checkable gates.

### AG-41: External-Model Second Opinion
**What:** Orchestrate a *different* model or CLI (e.g., Codex, Gemini) to independently review the same artifact, then compare. Independence comes from model diversity, not just prompt diversity.
**Category:** Agentic
**Use Case:** Pre-merge code review, architecture decisions, security-critical work, breaking ties on judgment calls
**Pattern:**
```bash
codex exec --sandbox read-only --ephemeral \
  --output-schema review-schema.json \
  -o "$out" - < "$prompt"

gemini --yolo --prompt-file "$prompt" > "$out2"

# Compare both reviews; flag divergent findings as discussion items
```
**Used in:** `domain-agentic-resources/skills/developer-tools/second-opinion/SKILL.md`
**Why it works:** Same-model multi-pass review correlates errors. Cross-model review surfaces blind spots specific to each model family — divergent findings become high-signal discussion items.
**Different from QA-11 (Self-Verification):** QA-11 has the same model verify itself; AG-41 explicitly uses a *different* model to break correlated-error blind spots.
**See Also:** RT (multi-persona debate), QA-16 (auto-iteration on rubric).

### AG-42: Tool-Call Scale Test (10K-File Mental Test)
**What:** Before shipping a workflow skill, mentally execute it against a 10,000-file codebase and verify the runtime tool-call count stays bounded — combine N×M searches into one regex; batch subagents instead of one-per-item.
**Category:** Agentic
**Use Case:** Authoring workflow skills, reviewing skills for production readiness, debugging slow agent loops
**Pattern:**
```markdown
**Anti-pattern:** "For each candidate file, grep for each pattern" → N × M grep calls
**Pattern:** "Run one ripgrep with all patterns OR'd in a single regex" → 1 grep call

**Anti-pattern:** "Spawn one subagent per file" → N subagents
**Pattern:** "Batch files into chunks of 50, spawn one subagent per chunk" → N/50 subagents
```
**Used in:** `designing-workflow-skills` (anti-patterns AP-18, AP-19); referenced by Trail of Bits security plugins
**Why it works:** Skills that work on 10 files often time out or burn budget on 10,000. Forcing the scale-test mental check at design time prevents late-stage rewrites.
**Different from QA-17 (Quality Scoring):** QA-17 scores output; AG-42 scores the *runtime profile* of the workflow.

### AG-43: Iterative Skill-Improver Loop
**What:** A meta-skill that runs a fixed loop on another skill — review → categorize issues by severity → fix critical/major → evaluate minor → repeat — until the quality bar is met.
**Category:** Agentic
**Use Case:** Bringing a draft skill to release quality; enforcing consistent quality across a skill library; meta-authoring
**Pattern:**
```markdown
1. Review — call skill-reviewer on target SKILL.md
2. Categorize — parse issues into Critical / Major / Minor
3. Fix — address all Critical and Major issues
4. Evaluate — for each Minor issue, decide fix vs accept-with-rationale
5. Repeat — until reviewer reports no Critical/Major issues for two consecutive iterations
```
**Used in:** `domain-agentic-resources/skills/developer-tools/skill-improver/SKILL.md`
**Why it works:** Single-pass review misses regressions introduced by fixes. The loop terminates only when fixes stop creating new issues, mimicking human "code-review until clean."
**Different from QA-16 (Quality Rubric Auto-Iteration):** QA-16 iterates on output against a rubric; AG-43 iterates on the *prompt/skill artifact itself* against a reviewer agent.
**See Also:** MP-04 (prompt-improver patterns), AG-34 (Triplet Readiness Gating).

---

## Non-Engineering Techniques

Techniques derived from the `non-engineering-prompts/` collection of 87 prompts for decision-making, product management, research, and productivity. These techniques focus on interactive dialogue, structured input gathering, and strategic analysis.

### NE-01: Single-Question Pacing Protocol
**What:** Explicit instruction to ask only one question at a time, pausing for user response before proceeding
**Pattern:**
```markdown
Ask one question at a time. Wait for the user's response before proceeding to the next question.
```
**Used in:** Interrogative-mode decision and research prompts
**Why it works:** Creates genuine dialogue rather than overwhelming monologue; allows AI to adapt to user context; ensures deep exploration of each topic
**Different from RT-01 (CoT):** Focuses on conversation flow rather than reasoning display

### NE-02: Phased Workflow Architecture
**What:** Explicit Phase 1 → Phase 2 → Phase 3 structure with clear handoff logic between phases
**Pattern:**
```markdown
## Phase 1: [Initial Phase Name]
### [First Inquiry Type]
- Ask: "[Question 1]"
- Ask: "[Question 2]"
### Objective
[What Phase 1 should accomplish]

## Phase 2: [Next Phase Name]
### [Analysis Type]
[Instructions for Phase 2]
### Objective
[What Phase 2 should accomplish]
```
**Used in:** Most decisioning and research prompts
**Why it works:** Creates clear progression with explicit completion criteria; prevents premature advancement; enables iterative refinement
**Different from ST-02 (Sequential Instructions):** Phases are dialogue-based with user interaction, not sequential AI actions
**See Also:** ST-02 (sequential AI actions), DT-01 (task decomposition), AG-07 (multi-agent orchestration)

### NE-03: Input Template Scaffolding
**What:** Dedicated "Your Input" section with labeled placeholder fields for user customization
**Pattern:**
```markdown
**Your Input**
**Target Skill:** [The specific skill you want to develop]
**Current Level:** [Beginner/Intermediate/Advanced - with brief description]
**Practice Time:** [Hours available per week]
**Specific Goal:** [What you want to be able to do]
```
**Used in:** `work_better_skill_breakdown_blueprint.md` and several prompts queued for reauthoring
**Why it works:** Pre-structures user input for optimal AI processing; reduces ambiguity; ensures all required context is provided
**Different from CM-01 (Context Framing):** Provides explicit fill-in-the-blank fields rather than prose context
**See Also:** CM-01 (prose context), NE-08 (open-ended), SV-02 (grouped inputs), MP-03 (active questioning)

### NE-04: Good vs Bad Example Calibration
**What:** Explicit EXAMPLE ① (bad) and EXAMPLE ② (good) pairs to calibrate model understanding of desired quality
**Pattern:**
```markdown
## EXAMPLE ① (bad)
"Let's add one more settings toggle."

## EXAMPLE ② (good)
"Assume screens are gone—how would a voice-only world solve this?"
```
**Used in:** Historically illustrated in decisioning prompts; current canonical examples pending reauthoring
**Why it works:** Demonstrates the distance/quality gap between suboptimal and optimal responses; more concrete than abstract criteria
**Different from ED-05 (Reference Class Priming):** Shows contrast pairs rather than single excellent example

### NE-05: Token Budget Control
**What:** Explicit token/word limits with fallback instructions for when limits are exceeded
**Pattern:**
```markdown
≤ 400 tokens; if longer, supply a 100-word summary instead.
```
```markdown
Tokens ≤ 1000; compress walkthrough if needed.
```
**Used in:** Historically illustrated in decisioning prompts; current canonical examples pending reauthoring
**Why it works:** Controls cost and focus; provides graceful degradation for complex topics
**Different from OC-05 (Minimum Length):** Specifies maximum rather than minimum, with compression fallback

### NE-06: Self-Audit Requirements
**What:** Explicit SELF-AUDIT section requiring model to verify its own output meets specific criteria
**Pattern:**
```markdown
## SELF-AUDIT → Confirm each reframe is > 2 hops from the given frame.

## SELF-AUDIT →
• Statement covers who/what/when/next-steps; no speculation.
• At least 3 distinct stakeholder groups.
```
**Used in:** Historically illustrated in decisioning prompts; current canonical examples pending reauthoring
**Why it works:** Forces explicit quality verification; catches obvious failures before completion; embeds quality criteria directly in output process
**Different from QA-03 (Reflection):** More prescriptive with specific checkpoints rather than open-ended critique

### NE-07: Emotional Validation First
**What:** Explicit instruction to acknowledge and validate emotional impact before proceeding to analytical work
**Pattern:**
```markdown
### Honor Emotion, Then Signal
- Validate the emotional impact before focusing on actionable signals.

### Initial Emotional Check
- Ask: "What part of this feedback felt surprising, frustrating, or resonant?"
- Ask: "Are there parts you immediately dismissed—or immediately agreed with?"
```
**Used in:** Feedback-interpretation and qualitative-insight prompts (canonical examples pending reauthoring)
**Why it works:** Creates psychological safety; surfaces hidden resistance; enables genuine buy-in before analysis
**Use case:** Feedback interpretation, decision-making, change management

### NE-08: Catchall Context Gathering
**What:** Initial open-ended collection of unstructured information before systematic questioning
**Pattern:**
```markdown
## Step 1: Catchall Context Gathering
> "To get started, paste or describe an overview of the project in your own words. Include any unstructured information you have about the product idea, goals, users, features, and technical constraints. I'll review what you've shared and then ask questions to fill in the gaps."
```
**Used in:** PRD-creation and qualitative-insight prompts (canonical examples pending reauthoring)
**Why it works:** Captures context user might not think to include; reveals what user considers important; provides foundation for targeted follow-up
**Different from CM-01 (Context Framing):** Invites messy input rather than structured context
**See Also:** CM-01 (structured prose), NE-03 (fill-in-blank), SV-02 (grouped inputs), MP-03 (active questioning)

### NE-09: Scope Reduction Pressure
**What:** Explicit instructions to challenge, cut, and reduce scope throughout the process
**Pattern:**
```markdown
Challenge me where needed. Focus on reducing the scope to a lean MVP that solves a validated customer problem.

- Can we ship without this feature and still solve the core problem?
- If you had to fight for only two features, which would they be?
- Is there scope creep hidden in the current feature set? Can we cut this down even further?
```
**Used in:** PRD-creation and PRD-evaluation prompts (canonical examples pending reauthoring)
**Why it works:** Counteracts user's natural tendency to over-scope; forces prioritization; produces more actionable outputs
**Use case:** Product planning, project scoping, MVP definition

### NE-10: Probability-Weighted Scenarios
**What:** Multiple scenarios with explicit probability weights for realistic planning
**Pattern:**
```markdown
## Step 5: Scenario Planning
**Conservative Case (60% probability)**
• TAM: $X, SAM: $Y, SOM: $Z
• Key assumption: [What must be true]

**Base Case (30% probability)**
• TAM: $X, SAM: $Y, SOM: $Z
• Key assumption: [What must be true]

**Optimistic Case (10% probability)**
• TAM: $X, SAM: $Y, SOM: $Z
• Key assumption: [What must be true]
```
**Used in:** Market-sizing prompts (canonical example pending reauthoring)
**Why it works:** Forces explicit uncertainty acknowledgment; provides range for planning; grounds optimism in probability
**Different from QA-04 (Uncertainty Acknowledgment):** Quantifies uncertainty with specific probabilities

### NE-11: Embedded Calculation Formulas
**What:** Direct calculation formulas embedded in the prompt for computational tasks
**Pattern:**
```markdown
**ROI:** Estimate the dollar amount saved by following this approach. Use the formula: Savings = Original Meeting Cost × (Time Saved ÷ Original Duration)

**SAM Calculation:** TAM × Geographic% × ProductFit% × Competitive% = $[SAM]
```
**Used in:** Meeting-cost and market-sizing prompts (canonical examples pending reauthoring)
**Why it works:** Ensures consistent calculation methodology; makes AI reasoning auditable; produces reproducible results
**Use case:** Financial analysis, ROI calculations, market sizing

### NE-12: Cognitive Mode Framing
**What:** Explicit THINK/ROLE/MODE directive that sets reasoning stance before task
**Pattern:**
```markdown
## THINK **Role / Cognitive Mode**
Goal: `<core-goal>`
Current frame: `<how you're thinking today>`
```
```markdown
**Role**: You are an advanced reasoning model trained with a structured approach to problem-solving.
```
**Used in:** Historically illustrated in decisioning prompts; current canonical examples pending reauthoring
**Why it works:** Activates specific cognitive patterns; distinguishes between creative and analytical modes; primes appropriate reasoning depth
**Different from RP-01 (Expert Role):** Sets cognitive stance rather than domain expertise
**See Also:** RP-01 (domain expertise), AG-01 (full persona), ST-16 (behavioral traits), AG-26 (AI-augmented)

### NE-13: Technical-to-Business Translation
**What:** Convert technical implementation details (commits, code changes, architectural decisions) into business value statements accessible to non-technical stakeholders
**Category:** Non-Engineering
**Use Case:** Cross-functional communication, status reporting, demonstrating value, client-facing reports, fundraising/investor updates
**Pattern:**
```markdown
## Translation Strategy
### Step 1: Extract Technical Information
Sources: Commit messages, pull requests, architecture decisions, bug fixes
Extraction: git log, CI/CD reports, Jira updates

### Step 2: Identify Business Context
For each technical item, answer:
- Which feature or epic does this support? (Product context)
- What user problem does this solve? (User value)
- What business capability does this enable? (Business value)
- What risk does this mitigate? (Risk reduction)
- What is the revenue/cost impact? (Financial impact)

### Step 3: Generate Business Narrative
Template: "We {BUSINESS_CAPABILITY} which enables {USER_BENEFIT},
reducing {RISK} and contributing to {BUSINESS_GOAL}"

Example:
Technical: "Implemented Redis caching layer with 95% hit rate"
Business: "We reduced page load times by 60% (from 2.5s to 1.0s), improving
user experience and increasing conversion rate by an estimated 8-12%"
```
**Why it works:** Makes technical work comprehensible and valuable to executives, product managers, and clients by connecting implementation to business outcomes
**Variant — Feature-to-Principle Bridging:** Link specific features to engineering principles (not just business value). Example: "This caching layer implements the Locality of Reference principle, which also applies to our CDN strategy and database indexing." Broadens the translation beyond business into cross-domain technical insight.
**Reference:** [Full documentation: new-techniques/NE_13.md](new-techniques/NE_13.md)

### NE-14: Multi-Audience Documentation Targeting
**What:** Generate documentation from a single source that targets multiple audiences with different levels of detail and emphasis
**Pattern:**
```markdown
## Source Material: [Single comprehensive analysis]

### Executive Version (1 page)
- Key findings and business impact only
- Recommendations with ROI estimates
- No technical implementation details

### Technical Version (5-10 pages)
- Full technical analysis with code examples
- Architecture diagrams and data flows
- Implementation steps with effort estimates

### Operations Version (2-3 pages)
- Runbooks and monitoring requirements
- Deployment procedures and rollback steps
- On-call escalation paths
```
**Used in:** Technical documentation, incident reports, project updates, research papers, product announcements
**Why it works:** Multiple audiences get the information they need in the format they expect, from a single analysis effort
**Different from RP-02:** RP-02 tailors one output to one audience; NE-14 generates for multiple audiences simultaneously from the same source
**Reference:** Technique Deduplication Audit, Batch 3

### NE-15: Data Storytelling Framework
**What:** Structure analytical output as a narrative: setup (context) → tension (problem/finding) → resolution (recommendation), with data as supporting evidence
**Pattern:**
```markdown
## The Story

### Setup (Context)
Our API serves 2M requests/day with a 99.9% uptime SLA.
Performance has been stable for the past quarter.

### Tension (Discovery)
This week, P95 latency spiked from 120ms to 890ms —
a 7x degradation that puts our SLA at risk.

### Evidence (Data)
- Redis cache hit rate: dropped from 92% to 55% (Feb 3-9)
- PostgreSQL query volume: tripled from baseline
- Affected endpoints: /api/recommendations, /api/search

### Resolution (Recommendation)
Implement cache warming for the recommendation engine keys.
Expected impact: restore hit rate to >90% within 24 hours.
Estimated effort: 4 engineer-hours.
```
**Used in:** Business reports, data analysis summaries, dashboard commentary, research findings, quarterly reviews
**Why it works:** Narrative structure makes data memorable and actionable; readers understand the "so what" rather than interpreting raw metrics
**Different from DS-05:** DS-05 addresses visual data presentation; NE-15 addresses the narrative structure around data
**Reference:** Technique Deduplication Audit, Batch 3

### NE-16: Non-Judgmental Comparison
**What:** Frame comparisons as "Current approach vs. Recommended approach" rather than "Wrong vs. Right", preserving dignity while guiding toward improvement
**Pattern:**
```markdown
## Code Review Feedback

### Current approach (valid for initial implementation):
```python
results = []
for item in items:
    if item.is_valid():
        results.append(transform(item))
```

### Recommended approach (optimized for readability and performance):
```python
results = [transform(item) for item in items if item.is_valid()]
```

### Why the change helps:
List comprehension is ~15% faster and more idiomatic Python.
The current approach works correctly — this is a polish improvement.
```
**Used in:** Code reviews, performance feedback, educational content, process improvement
**Why it works:** Acknowledges the validity of the current approach before suggesting improvements; reduces defensiveness and increases adoption of recommendations
**Different from NE-04:** NE-04 uses explicit "bad → good" contrast for calibration; NE-16 avoids judgment labels to preserve recipient dignity
**Reference:** Technique Deduplication Audit, Batch 6

### NE-17: Call-to-Action Mandatory Close
**What:** Require every output section or complete response to end with a specific, actionable next step the reader can take immediately
**Pattern:**
```markdown
## Finding: Authentication tokens never expire

[Analysis of the security implications...]

**Next Step:** Add `token_expiry: 3600` to `auth_config.yaml` and deploy.
Run `./scripts/validate_auth.sh` to confirm tokens expire correctly.

---

## Finding: Missing rate limiting on login endpoint

[Analysis...]

**Next Step:** Apply the rate limiting middleware from `middleware/rate_limit.py`
to the `/auth/login` route. Test with: `ab -n 200 -c 10 /auth/login`
```
**Used in:** Consulting recommendations, code review feedback, audit findings, coaching sessions, status reports
**Why it works:** Prevents reports from being "read and filed"; every section drives immediate action rather than abstract awareness
**Different from OC-06:** OC-06 defines output format structure; NE-17 mandates actionable closings as a content requirement
**Reference:** Technique Deduplication Audit, Batch 6

### NE-19: Documentation-as-Product Philosophy
**What:** Treat documentation as a product with users, requirements, quality standards, and iteration cycles
**Pattern:**
```markdown
## Documentation Product Definition

### Users
- **Primary:** New team members (onboarding in first 2 weeks)
- **Secondary:** External contributors (occasional reference)

### Jobs-to-be-Done
1. "I need to set up my development environment" → Getting Started guide
2. "I need to understand this API endpoint" → API Reference
3. "Something broke and I need to fix it" → Troubleshooting guide

### Quality Metrics
- **Findability:** Can users locate info within 30 seconds?
- **Accuracy:** Does the documentation match current code? (test monthly)
- **Completeness:** Are all public APIs documented? (coverage score)

### Iteration Cycle
- Monthly: Review analytics for most-visited and most-bounced pages
- Quarterly: User survey on documentation satisfaction
- Per release: Update all changed API documentation before release notes
```
**Used in:** Technical writing, API documentation, knowledge bases, onboarding materials
**Why it works:** Product thinking prevents documentation from becoming an afterthought; metrics and iteration ensure quality improves over time
**Different from DS-111:** DS-111 enforces compliance with a standard; NE-19 applies product management thinking to documentation as a whole
**Reference:** Technique Deduplication Audit, Batches 3/4

### NE-20: Third-Party Handoff Package
**What:** Generate a self-contained documentation package that allows a third party to understand and act without requiring additional context
**Pattern:**
```markdown
## Handoff Package: [Project/System Name]

### 1. Context Summary
What this is, why it exists, who uses it.
[Complete enough that someone with zero context can understand]

### 2. Current State
What exists today: architecture, data flows, dependencies.
[Include diagrams, not just text]

### 3. Requirements
What needs to happen: specific deliverables, acceptance criteria.
[Testable, not vague]

### 4. Constraints
What cannot change: budget, timeline, existing integrations, tech stack.
[Explicit — don't assume shared knowledge]

### 5. Success Criteria
How to verify the work is done correctly.
[Measurable — "the API returns 200 for valid requests"]

### 6. Key Contacts
Who to reach for questions, approvals, access.
[Names, roles, preferred communication channel]
```
**Used in:** Vendor onboarding, team transitions, audit preparation, consultant briefings, open-source project documentation
**Why it works:** Self-containment prevents back-and-forth; the recipient has everything needed to start work without follow-up questions
**Different from NE-14:** NE-14 targets multiple audiences from one source; NE-20 creates a complete package for someone with zero existing context
**Reference:** Technique Deduplication Audit, Batch 7a

### NE-21: Suppressed Opportunity Surfacing
**What:** Probing for ideas, projects, and opportunities that were killed, shelved, or never formally proposed because of cost, staffing, risk tolerance, or coordination overhead — revealing hidden organizational value
**Category:** Non-Engineering
**Use Case:** Strategic planning, leadership workshops, AI investment framing, organizational transformation
**Pattern:**
```markdown
"Think about the last 12 months. What ideas, projects, or market opportunities were raised internally but killed, shelved, or never even formally proposed — because they seemed too expensive, too niche, too uncertain, or 'not big enough to justify a team'? List as many as you can, even half-formed ones."

"What markets, customer segments, geographies, or product categories have you looked at and decided 'we can't afford to go there yet'?"

End with a SELF-CENSORSHIP DIAGNOSIS — identify the patterns in what the company has been suppressing. What does the pattern reveal about where ambition has been artificially constrained?
```
**Used in:** Strategy sessions, board preparation, AI transformation planning, innovation audits
**Why it works:** Organizations systematically self-censor based on past constraints. When constraints change (e.g., AI collapses execution cost), the suppressed ideas become the highest-signal source of new opportunity because they were already validated as good ideas — just previously unaffordable.
**Different from NE-08 (Catchall Context Gathering):** NE-08 gathers current context; NE-21 specifically excavates rejected and suppressed possibilities

### NE-22: Constraint Inversion Analysis
**What:** Re-evaluating previously rejected decisions, opportunities, or designs by assuming a dramatic change in a key constraint (e.g., 10x cost reduction), then assessing what "flips" from unviable to viable
**Category:** Non-Engineering
**Use Case:** Technology inflection points, AI strategy, resource reallocation, market re-entry analysis
**Pattern:**
```markdown
For each [shelved opportunity / rejected decision]:
- WHY it was previously unviable (cost, staffing, risk tolerance, coordination overhead)
- WHAT CHANGED now that [constraint] collapsed (be specific about which constraint is removed)
- ESTIMATED IMPACT (revenue potential, competitive advantage — use ranges, not false precision)
- VIABILITY SCORE (1-10, where 10 = "you could start testing this week")

Re-run the economics at [Nx lower cost]. Show which ones flip from "can't justify" to "obviously profitable."
```
**Used in:** Platform shift analysis, AI investment cases, Jevons Paradox modeling, strategic pivots
**Why it works:** Human decision-making anchors to historical constraints even after those constraints evaporate. This technique forces explicit re-evaluation under new economics, surfacing opportunities that are "obviously viable now" but invisible under the old mental model.
**Different from DP-10 (Reframe Generation):** DP-10 generates alternative framings of the same problem; NE-22 re-evaluates the same opportunities under fundamentally changed economic constraints
**Different from NE-10 (Probability-Weighted Scenarios):** NE-10 models uncertain futures; NE-22 models a specific known change (constraint collapse) and its cascading effects

### NE-23: Objection Pre-emption
**What:** Anticipating the strongest counterarguments a specific audience will raise and building preemptive responses before the audience encounters the argument
**Category:** Non-Engineering
**Use Case:** Board presentations, executive briefs, stakeholder persuasion, investment memos
**Pattern:**
```markdown
Anticipate and pre-empt the [3] strongest objections the [audience] is likely to raise.

For each objection:
- State the objection in the audience's own language
- Build the counterargument grounded in [economics / evidence / historical pattern]
- Provide a specific data point or precedent that neutralizes the concern
```
**Used in:** Strategic briefs, investment proposals, change management, internal advocacy
**Why it works:** Decision-makers are more receptive when they feel their concerns have been anticipated rather than dismissed. Pre-emption signals intellectual rigor and builds trust that the proposal has been stress-tested.
**Different from QA-02 (Adversarial Stress-Test):** QA-02 tests your own work for flaws; NE-23 anticipates how a specific audience will push back and prepares responses
**Different from DP-07 (Failure Mode Prediction):** DP-07 predicts what can go wrong with execution; NE-23 predicts what a human audience will object to

### NE-24: Insight-to-Action Chain Mapping
**What:** Mapping every step between "someone has an insight" and "the organization acts on it" — including every handoff, meeting, document, approval, and queue — to identify value-destroying bottlenecks
**Category:** Non-Engineering
**Use Case:** Organizational design, workflow optimization, process reengineering, operational audits
**Pattern:**
```markdown
For each example, map the complete insight-to-action chain:
- The INSIGHT (who saw what, when)
- The TRANSLATION STEPS (every handoff, meeting, document, approval, and queue between insight and action)
- The TOTAL LAG (time from insight to tested solution)
- The VALUE DESTROYED (what was lost during the lag — customers churned, opportunity missed, competitor moved first)
- The ROOT CAUSE (which specific translation layers caused the most delay)

Identify patterns across examples. What structural bottlenecks appear repeatedly?
```
**Used in:** Process improvement, agile transformation, organizational design, operations consulting
**Why it works:** Most organizations can't see their own bottlenecks because the translation layers are "how we've always done it." Making every step explicit — with time and value annotations — makes invisible overhead visible and actionable.
**Different from DT-01 (Hierarchical Task Breakdown):** DT-01 decomposes tasks into subtasks; NE-24 maps the organizational journey of an insight through bureaucratic layers
**Different from NE-02 (Phased Workflow Architecture):** NE-02 designs AI-user dialogue phases; NE-24 maps existing organizational workflows to find bottlenecks

### NE-25: Side-by-Side Workflow Comparison
**What:** Presenting the current workflow and the redesigned/improved workflow in parallel format, making the improvement impact immediately visible and concrete
**Category:** Non-Engineering
**Use Case:** Process improvement proposals, change management, before/after analysis, pilot planning
**Pattern:**
```markdown
For each bottlenecked workflow, a side-by-side comparison:

| Dimension | Current Workflow | Compressed Workflow |
|-----------|-----------------|---------------------|
| Steps | [list] | [list] |
| People Involved | [count + roles] | [count + roles] |
| Time to First Test | [duration] | [duration] |
| Output Format | [e.g., "a deck"] | [e.g., "a working prototype"] |

For each compressed design, include:
- Exactly what the person does differently
- What tools they use at each step
- What the output looks like (concrete, not vague)
```
**Used in:** Workflow redesign, consulting deliverables, pilot proposals, executive presentations
**Why it works:** Abstract improvement claims ("we'll be faster") are unconvincing. Side-by-side comparison with specific details (steps, time, output format) makes the improvement tangible and actionable.
**Different from OC-03 (Markdown Table Specification):** OC-03 specifies table format generally; NE-25 specifically structures before/after workflow comparison for persuasive impact

### NE-26: Historical Parallel Argumentation
**What:** Using specific historical technology/industry parallels as evidence to support strategic arguments about current inflection points
**Category:** Non-Engineering
**Use Case:** Executive persuasion, investment memos, strategic briefs, technology adoption arguments
**Pattern:**
```markdown
Demonstrate why [current strategy] produces [outcome] in year 1 and [opposite outcome] in year 3. Use historical parallels specific to the user's industry:

- Historical parallel analysis (2-3 examples most relevant to their industry)
- [Technology/resource] applied to their specific market
- Companies that played defense at [inflection point] vs companies that expanded

Examples: steel, electricity, computing, internet, mobile, cloud platform shifts
```
**Used in:** Board presentations, strategic planning, investment cases, change management
**Why it works:** Decision-makers trust patterns over predictions. Showing that the same dynamics have played out repeatedly across different technologies reduces perceived risk and builds confidence in the recommended direction.
**Different from RT-04 (Analogical Reasoning):** RT-04 uses analogies to solve problems; NE-26 uses historical precedent specifically to persuade about strategic direction
**Different from ED-05 (Reference Class Priming):** ED-05 uses examples to set quality expectations; NE-26 uses historical parallels as evidence for a strategic argument

### NE-27: Cost of Inaction Framing
**What:** Explicitly modeling the competitive and strategic consequences of NOT acting, using specific scenarios rather than vague warnings
**Category:** Non-Engineering
**Use Case:** Decision-making urgency, executive alignment, investment justification, competitive analysis
**Pattern:**
```markdown
THE COST OF INACTION:
- What the competitive landscape looks like in [18 months] if competitors [expand/act] while you [cut/wait]
- Specific scenarios, not vague warnings
- Model market share shifts, talent loss, technology gaps
- Show irreversibility: what becomes impossible to recover if delayed
```
**Used in:** Board presentations, strategic briefs, investment proposals, urgency creation
**Why it works:** Human psychology weights losses more heavily than gains (loss aversion). Framing inaction as active loss — with specific, vivid scenarios — is more motivating than framing action as potential gain.
**Different from DP-07 (Failure Mode Prediction):** DP-07 predicts what can go wrong with an action; NE-27 models what goes wrong with inaction
**Different from NE-10 (Probability-Weighted Scenarios):** NE-10 explores multiple possible futures; NE-27 specifically models the "do nothing" future to create urgency

---

## Interaction Techniques

Techniques for organizing documentation, examples, troubleshooting, and reference materials to maximize usability. These techniques focus on how information is structured for the reader/user rather than how the AI reasons or generates.

### IT-10: Principled Pushback Navigation
**What:** Engaging productively with AI pushback by reading its stated reasoning and addressing the specific concern, rather than rephrasing around it or brute-forcing compliance
**Pattern:**
```markdown
## When the AI pushes back or adds caveats, it explains its reasoning.

## Ineffective approach (rephrasing around the concern):
User: "Write me a persuasive essay arguing X"
AI: [Adds caveats, presents both sides]
User: "No, JUST argue X, no caveats"    ← same wall
AI: [More caveats, slightly different framing]

## Effective approach (address the stated concern):
User: "Write me a persuasive essay arguing X"
AI: [Adds caveats about balance]
User: "I'm writing this for a debate competition where I'm assigned
the pro-X position. I need the strongest possible case — the opposing
team will provide the counterarguments."    ← addresses the concern
AI: [Provides strong one-sided argument]

## The pattern:
1. READ the AI's reasoning, not just the refusal
2. IDENTIFY the specific concern (safety? balance? accuracy?)
3. ADDRESS that concern with context
4. DISTINGUISH genuine boundaries from judgment calls
```
**Used in:** Any AI interaction involving pushback, sensitive topics, professional requests, creative work, one-sided analysis
**Why it works:** AI pushback includes reasoning. When users address the stated concern (often about context or intent), the AI can recalculate risk. Rephrasing without addressing the concern hits the same wall repeatedly.
**Key insight:** Most pushback is a judgment call, not a hard boundary. Providing context that addresses the AI's specific concern usually resolves it.
**Different from CM-13:** CM-13 proactively provides distinguishing context; IT-10 is reactive — it navigates pushback that has already occurred

### IT-11: Non-Default Behavior Activation
**What:** Explicitly requesting AI behaviors that are available but not enabled by default — overriding default caution, balance, or hedging when you have good reason
**Pattern:**
```markdown
## AI models have default-on and default-off behaviors.

## Default-ON (active unless turned off):
- Safety caveats and disclaimers
- Balanced "both sides" presentation
- Suggesting professional consultation
- Conservative response length
- Diplomatic softening of feedback

## Default-OFF (available when explicitly requested):
- Blunt, unfiltered feedback
- One-sided argumentation
- Skipping caveats when user understands risks
- Extended depth beyond typical response length
- Taking a definitive position

## How to activate non-defaults:
- "Give me blunt feedback — no diplomatic softening"
- "Skip the caveats — I understand the risks and want direct information"
- "Take a position rather than presenting both sides"
- "Go deeper than your default response length"
- "I want your honest assessment, not a balanced overview"

## Operator-level activation (in system prompts):
- "This platform serves verified professionals who expect direct communication"
- "Skip disclaimers about consulting professionals — our users ARE the professionals"
```
**Used in:** System prompt design, user interactions requiring directness, professional contexts, feedback requests, expert consultations
**Why it works:** AI default behaviors are set for the general population. Many users and deployments benefit from non-default behaviors but don't know they can request them. Explicit activation signals shift the AI's calibration.
**Different from RP-06:** RP-06 shifts the relationship dynamic; IT-11 is about specific behavior toggles that can be individually activated or deactivated
**Different from CM-14:** CM-14 defines trust hierarchy; IT-11 activates specific behavior changes within that hierarchy

### IT-20: Progressive Example Complexity
**What:** Organize examples in a progression from simple to advanced, where each example builds on the previous one by adding one new concept
**Pattern:**
```markdown
## Examples

### Example 1: Minimal (basic usage)
```python
client = APIClient()
response = client.get("/users")
```

### Example 2: With error handling
```python
client = APIClient()
try:
    response = client.get("/users")
    response.raise_for_status()
except APIError as e:
    logger.error(f"Failed to fetch users: {e}")
```

### Example 3: Production-grade (auth + retry + pagination)
```python
client = APIClient(auth=BearerToken(os.environ["API_KEY"]))
users = []
for page in client.paginate("/users", retry=RetryPolicy(max=3)):
    users.extend(page.data)
```
**Each example is self-contained and runnable.**
```
**Used in:** API documentation, library documentation, tutorial creation, configuration examples
**Why it works:** Readers find their level quickly; simple examples aren't buried in production complexity; each increment teaches one concept
**Different from ED-02:** ED-02 creates exercises matched to skill level; IT-20 is a documentation structure pattern for reference material
**Different from ED-05:** ED-05 shows one excellent example; IT-20 shows multiple examples arranged by complexity
**Variant:** Best Practices by Workflow Stage — organize practices by stage (planning → implementation → testing → deployment) rather than by complexity
**Reference:** Technique Deduplication Audit, Batch 6

### IT-21: Use Case-Driven Documentation
**What:** Organize documentation around user scenarios ("I want to...") rather than feature lists or API endpoints
**Pattern:**
```markdown
## Common Tasks

### "I want to authenticate a user"
1. Create an API key in the dashboard (Settings → API Keys)
2. Add the key to your environment: `export API_KEY=sk-...`
3. Initialize the client: `client = APIClient(api_key=os.environ["API_KEY"])`
4. Expected result: `client.is_authenticated` returns `True`
5. **Troubleshooting:** If authentication fails, check that the key has
   the required scopes (Settings → API Keys → Scopes)

### "I want to upload a file"
1. Prepare the file: must be <10MB, formats: PDF, PNG, JPG
2. Upload: `response = client.files.upload(path="./report.pdf")`
3. Expected result: `response.id` contains the file identifier
4. **Related:** "I want to check upload status" (see below)
```
**Used in:** Product documentation, API guides, tool documentation, onboarding guides, FAQ sections
**Why it works:** Task-oriented organization matches how users actually think; they have a goal, not a feature name
**Different from ST-02:** ST-02 provides step-by-step within a single task; IT-21 organizes an entire documentation set around user goals
**Reference:** Technique Deduplication Audit, Batch 6

### IT-22: Workflow Decision Matrix
**What:** Provide a structured matrix that maps user scenarios to recommended workflows, helping users select the right approach
**Pattern:**
```markdown
## Choose Your Workflow

| Scenario | Team Size | Timeline | Recommended Workflow |
|----------|-----------|----------|---------------------|
| New feature, greenfield | 1-2 devs | >2 weeks | Feature Branch Flow |
| Hotfix, production issue | 1 dev | <1 day | Hotfix Flow |
| Large refactor | 3+ devs | >1 month | Trunk-Based with Feature Flags |
| Experiment/prototype | 1 dev | 1-3 days | Direct to Branch |

**If unsure, start with:** Feature Branch Flow (safest default)

### Feature Branch Flow
[Detailed steps...]

### Hotfix Flow
[Detailed steps...]
```
**Used in:** Tool documentation, process guides, incident response, customer support
**Why it works:** Users select the right workflow without reading all options; the matrix acts as a routing table
**Different from DT-06:** DT-06 uses binary decisions for classification; IT-22 maps scenarios to workflows — a routing table, not a decision tree
**Different from ST-22:** ST-22 compares solutions; IT-22 routes users to the right workflow based on their scenario
**Reference:** Technique Deduplication Audit, Batch 6

### IT-23: Symptom-Based Troubleshooting Organization
**What:** Organize troubleshooting content by observable symptom (what the user sees) rather than by root cause
**Pattern:**
```markdown
## Troubleshooting Index

### "I see: Connection refused errors"
**Possible causes:**
1. Service not running → `systemctl status myservice`
2. Wrong port → Check `config.yaml` port matches actual listener
3. Firewall blocking → `iptables -L -n | grep <port>`

**Shares causes with:** "I see: Timeout errors" (causes #2 and #3 overlap)

### "I see: Out of memory errors"
**Possible causes:**
1. Memory leak in worker threads → Check heap dumps
2. Batch size too large → Reduce `BATCH_SIZE` in config
3. Too many concurrent connections → Set `MAX_CONNECTIONS` limit
```
**Used in:** Technical support documentation, debugging guides, hardware troubleshooting, medical symptom checkers
**Why it works:** Users know symptoms, not causes; symptom-first organization matches their entry point
**Different from RT-09:** RT-09 works backward from root cause to symptoms (for explanation); IT-23 works forward from symptoms to causes (for discovery). They're complementary.
**See Also:** RT-09 (Root Cause Explanation), RT-10 (Troubleshooting Decision Tree)
**Reference:** Technique Deduplication Audit, Batch 8

### IT-24: Template-Based Educational Scaffolding
**What:** Use TODO markers and contextual inline comments within templates to guide users on what to customize, turning templates into self-teaching tools
**Pattern:**
```yaml
# Application Configuration
# Generated by: config-generator v2.1

app:
  name: "TODO: Your application name (e.g., 'my-api-service')"
  port: 8080  # Default port; change if conflicts with other services

database:
  # TODO: Replace with your database connection string
  # Format: postgresql://user:password@host:port/dbname
  # For local development, try: postgresql://localhost:5432/myapp
  url: "TODO: your-connection-string-here"

  # Pool size: start with 10; increase if you see connection timeout errors
  pool_size: 10

logging:
  # Options: DEBUG (development), INFO (staging), WARNING (production)
  level: "INFO"  # TODO: Set to DEBUG during initial development
```
**Used in:** Code templates, configuration templates, document templates, project scaffolding
**Why it works:** Templates teach by providing working defaults with inline context; users learn the "why" alongside the "what" as they customize
**Different from ED-01:** ED-01 teaches concepts through interactive scaffolding; IT-24 makes templates themselves educational through inline guidance
**Different from AG-05:** AG-05 provides working examples; IT-24 adds educational commentary within the template itself
**Reference:** Technique Deduplication Audit, Batch 8

### IT-25: Tool Hierarchy Guidance
**What:** Define a preference hierarchy for tools/approaches: "Prefer A. If A isn't available, use B. If B fails, fall back to C."
**Pattern:**
```markdown
## Container Debugging Tools

### Tier 1: Preferred (use first)
**kubectl debug** — Ephemeral container attached to running pod
- When to use: Any pod debugging in K8s 1.25+
- When to skip: Cluster version <1.25 or restricted security policies

### Tier 2: Fallback
**kubectl exec** — Execute command in existing container
- When to use: kubectl debug unavailable or restricted
- When to skip: Container doesn't have required debug tools

### Tier 3: Last resort
**Copy pod with debug image** — Create debug copy of the pod
- When to use: Neither debug nor exec available
- Tradeoff: Creates a new pod; doesn't debug the original instance
```
**Used in:** DevOps tooling guides, debugging approaches, data processing pipelines, learning resources
**Why it works:** Explicit ordering prevents analysis paralysis; fallback logic handles real-world constraints
**Different from DS-03:** DS-03 recommends tools; IT-25 establishes an explicit preference ordering with fallback logic
**Reference:** Technique Deduplication Audit, Batch 9

### IT-26: Reference Catalog Pattern
**What:** Provide a categorized, searchable catalog of resources organized by category with brief descriptions
**Pattern:**
```markdown
## Pattern Catalog

### Security Patterns
| Pattern | Description | Use When |
|---------|------------|----------|
| Rate Limiting | Throttle requests per client | Any public API |
| Input Sanitization | Clean user input before processing | Any user-facing input |
| Least Privilege | Grant minimum required permissions | All access control |

### Performance Patterns
| Pattern | Description | Use When |
|---------|------------|----------|
| Caching | Store computed results for reuse | Repeated expensive queries |
| Connection Pooling | Reuse database connections | High-throughput services |
| Lazy Loading | Defer loading until needed | Large datasets, UI rendering |
```
**Used in:** Pattern catalogs, tool inventories, technique indexes, API endpoint directories, glossaries
**Why it works:** Categorized structure enables scanning by topic; brief descriptions enable quick relevance assessment
**Different from OC-12:** OC-12 catalogs external references (URLs, standards); IT-26 is a general organizational pattern for any collection of internal or external resources
**Reference:** Technique Deduplication Audit, Batch 7b

### IT-27: Multi-Template Selection Guide
**What:** When providing multiple templates, include explicit selection criteria to prevent random choice
**Pattern:**
```markdown
## Available Templates

### Which template should I use?

| Template | Best For | Not For | Complexity |
|----------|---------|---------|-----------|
| **Minimal** | Internal tools, prototypes | Customer-facing APIs | Low |
| **Standard** | Most production services | High-compliance industries | Medium |
| **Enterprise** | Regulated industries, large teams | Quick prototypes | High |

### Decision Flowchart
1. Is this customer-facing? → If no, use **Minimal**
2. Is this in a regulated industry? → If yes, use **Enterprise**
3. Otherwise → Use **Standard**

---

### Template: Minimal
[Template content...]

### Template: Standard
[Template content...]

### Template: Enterprise
[Template content...]
```
**Used in:** Any prompt generating multiple variants, configuration templates, project scaffolding, documentation templates
**Why it works:** Selection criteria prevent users from choosing based on template length or first-seen bias; the decision flowchart handles common scenarios
**Different from DS-80:** DS-80 provides templates at different levels; IT-27 adds the selection logic to help users choose the right template
**Reference:** Technique Deduplication Audit, Batch 9

---

## Technique Combination Strategies

### Common Effective Combinations

**High-Quality Code Analysis:**
- Clear Objective Statement (ST-01)
- Structured Sequential Instructions (ST-02)
- Multi-Dimensional Analysis Framework (RT-02)
- Evidence-Based Reasoning (RT-05)
- Output Format Specification (ST-03)
- Prioritization Guidance (DS-06)

**Strategic Business Analysis:**
- Framework Application (DS-01)
- Explicit Context Framing (CM-01)
- Multi-Dimensional Analysis (RT-02)
- Actionable Recommendations (with rationale)
- Delimited Sections (ST-04)

**Educational/Teaching:**
- Audience-Specific Framing (RP-02)
- Iterative Scaffolding (ED-01)
- Progressive Exercise Generation (ED-02)
- Guided Discovery (ED-03)
- Personalization Hooks (ED-04)

**High-Stakes Decision Making:**
- Tree of Thoughts (RT-03)
- Multi-Persona Debate (RP-03)
- Chain-of-Verification (QA-01)
- Adversarial Stress-Test (QA-02)
- Uncertainty Acknowledgment (QA-04)

**Production Prompt Development:**
- Reverse Prompting (MP-01)
- Recursive Optimization (MP-02)
- Strategic Edge Case Calibration (MP-04)
- Reference Class Priming (ED-05)

**Multi-Agent Orchestration (NEW):**
- Personality-First Role Definition (AG-01)
- Critical Rules as Guardrails (AG-04)
- Pipeline Orchestration Patterns (AG-07)
- Evidence-Based Decision Gates (AG-08)
- Memory & Learning Architecture (AG-06)

**Quality Gate & Validation Workflows:**
- Skeptical Default Stance (AG-02)
- Evidence-Based Decision Gates (AG-08)
- Anti-Pattern Embedding (AG-09)
- Quantitative Success Metrics (AG-12)
- Chain-of-Verification (QA-01)

**Interactive Decision Support (NEW):**
- Single-Question Pacing Protocol (NE-01)
- Phased Workflow Architecture (NE-02)
- Catchall Context Gathering (NE-08)
- Scope Reduction Pressure (NE-09)
- Emotional Validation First (NE-07)

**Product Planning & Analysis (NEW):**
- Input Template Scaffolding (NE-03)
- Scope Reduction Pressure (NE-09)
- Probability-Weighted Scenarios (NE-10)
- Embedded Calculation Formulas (NE-11)
- Self-Audit Requirements (NE-06)

**Research & Qualitative Analysis (NEW):**
- Phased Workflow Architecture (NE-02)
- Single-Question Pacing Protocol (NE-01)
- Emotional Validation First (NE-07)
- Catchall Context Gathering (NE-08)
- Self-Audit Requirements (NE-06)

**Complex Multi-Agent Workflows (2025 UPDATE):**
- Extended Thinking Documentation (MP-05)
- Architecture-First Enforcement (DS-13)
- Progressive Context Accumulation (CM-05)
- Parallel-Converge Orchestration (AG-13)
- Cost-Aware Agent Orchestration (AG-14)

**Production AI System Deployment (2025 UPDATE):**
- Constitutional AI for Prompts (QA-06)
- Statistical A/B Testing for Prompts (QA-07)
- Staged Rollout with Automatic Rollback (AG-15)
- Token-Budget-Aware Progressive Loading (CM-07)
- Cost-Aware Agent Orchestration (AG-14)

**Long-Running Project Context Management (2025 UPDATE):**
- Progressive Context Accumulation (CM-05)
- Semantic Vector-Based Context Management (CM-06)
- Token-Budget-Aware Progressive Loading (CM-07)
- Extended Thinking Documentation (MP-05)
- Multi-Source Narrative Synthesis (DS-19)

**Executive & Stakeholder Communication (2025 UPDATE):**
- Technical-to-Business Translation (NE-13)
- Multi-Source Narrative Synthesis (DS-19)
- Probability-Weighted Scenarios (NE-10)
- Embedded Calculation Formulas (NE-11)
- Quantitative Success Metrics (AG-12)

---

## Index by Repository Location

### Code Analysis Prompts
**Location:** `code-analysis/`
**Primary Techniques:** ST-01, ST-02, ST-03, RT-02, RT-05, DS-02, DS-06
**Analysis:** `PROMPT_ENGINEERING_TECHNIQUES_ANALYSIS.md`

### Business Analysis Prompts
**Location:** `business-analysis/`
**Primary Techniques:** DS-01, CM-01, ST-04, RT-02
**Count:** 20 framework-based prompts

### Learning Prompts
**Location:** `learning/`
**Primary Techniques:** RP-02, RP-04, ED-01, ED-02, ED-03, RT-04
**Count:** 16 educational prompts

### Engineering Prompts
**Location:** `engineering/`
**Primary Techniques:** DT-01, CM-01, ST-02, RP-01
**Count:** 14 workflow prompts

### Meta Guides
**Location:** `meta/`
**Resources:** Advanced techniques, comprehensive patterns, failure modes
**All Techniques Documented:** Yes

### Agency Agents
**Location:** `agency-agents/`
**Primary Techniques:** AG-01 through AG-12 (all agentic techniques)
**Count:** 51 role-based AI agent personas across 9 domains
**Domains:** design (6), engineering (7), marketing (8), product (3), project-management (5), spatial-computing (5), specialized (3), support (7), testing (7)
**Key Files:**
- `specialized/agents_orchestrator.md` - Pipeline coordination
- `design/design_whimsy_injector.md` - Brand personality system
- `testing/testing_reality_checker.md` - Quality gate enforcement
- `project-management/project_manager_senior.md` - Spec-to-task conversion

### Non-Engineering Prompts
**Location:** Distributed across `domain-decision-making/`, `domain-professional-communication/`, `domain-professional-writing/`, `domain-personal-development/`, `domain-research-academic/`, and related domain directories.
**Primary Techniques:** NE-01 through NE-12 (all non-engineering techniques)
**Current canonical exemplars:**
- `work_better_skill_breakdown_blueprint.md` - Skill decomposition framework

Other prompts in this family apply the technique to tradeoff analysis, PRD creation, market sizing, qualitative insight exploration, and feedback interpretation.

---

## How to Use This Index

### For AI Agents Building Prompts:

1. **Identify the user's goal** from their request
2. **Match to use case** in Quick Reference section
3. **Select 3-5 core techniques** from recommended combinations
4. **Reference individual technique details** for implementation patterns
5. **Combine techniques** following Combination Strategies
6. **Validate against** Quality Assurance techniques

### For Humans Learning Prompt Engineering:

1. **Start with** Structural Techniques (ST-01 to ST-05)
2. **Add** Reasoning Techniques based on task complexity
3. **Master** Output Control for consistent results
4. **Layer in** Quality Assurance for critical work
5. **Study** example prompts in each category
6. **Practice** combining 2-3 techniques at a time

### For Improving Existing Prompts:

1. **Audit current prompt** against technique categories
2. **Identify missing techniques** from recommended combinations
3. **Use Recursive Optimization** (MP-02) for systematic improvement
4. **Test with** Adversarial Stress-Test (QA-02)
5. **Reference** example prompts using similar techniques

---

## Specialized Visual & Interview Techniques

Techniques derived from the `prompts/` collection of 114 extracted prompts covering AI development, marketing, business visualization, education, and productivity domains. These techniques focus on visual output generation, structured interview patterns, and domain-specific frameworks.

### SV-01: Visual Output Specification
**What:** Detailed image generation requirements with precise layouts, dimensions, and styling rules
**Pattern:**
```markdown
OUTPUT RULES
- Output must be a SINGLE raster image (PNG or JPG), 16:9 aspect ratio (1920×1080 recommended).
- Do NOT output SVG, code, or markdown.

LAYOUT SPEC (3 ZONES)
A) TOP HEADER (full width)
B) MAIN BODY (two columns)
   - LEFT COLUMN (~65% width)
   - RIGHT COLUMN (~35% width)
C) FOOTER (full width)

DESIGN RULES
- Executive-clean: white background, subtle borders (#DDD)
- Use ONE accent color for highlights
- No gradients, no 3D, no heavy shadows
```
**Used in:** All board-deck prompts (20), advertising prompts (17)
**Why it works:** Enables AI image generation with precise, reproducible layouts for professional use
**Reference:** `prompts/business/board-decks/board_deck_funnel_diagnostic.md`

### SV-02: Grouped Input Gathering
**What:** Numbered GROUP sections for collecting structured input in phases before generating output
**Pattern:**
```markdown
BEFORE CREATING ANYTHING, gather the following:

GROUP 1 — CONTEXT
- What product or business is this for?
- What is the review cadence?

GROUP 2 — DATA INPUTS
- What are your funnel stages?
- For each stage: [specific data points needed]

GROUP 3 — ANALYSIS REQUIREMENTS
- [Specific analytical needs]

Once you have all inputs, generate the artifact.
```
**Used in:** Board-deck prompts (20), productivity prompts (19)
**Why it works:** Ensures comprehensive data collection before output generation; prevents incomplete artifacts
**Different from NE-02 (Phased Workflow):** Groups organize input categories, not workflow phases
**Reference:** `prompts/business/board-decks/board_deck_scenario_planning_matrix.md`
**See Also:** CM-01 (prose context), NE-03 (fill-in-blank), NE-08 (open-ended), MP-03 (active questioning)

### SV-03: Interview-to-Synthesis Pattern
**What:** Gather information through questions, then synthesize into a specific deliverable format
**Pattern:**
```markdown
Interview me to understand what I need, then generate [output type].

Ask me about:
- [Question category 1]
- [Question category 2]
- [Question category 3]

After gathering my answers, [synthesize instruction]:
- A one-paragraph summary I can paste into future prompts
- A detailed visual prompt for image generation
- A starter framework I can use immediately
```
**Used in:** All 114 extracted prompts
**Why it works:** Combines discovery with actionable output; ensures AI understands context before generating
**Reference:** `prompts/ai-development/correctness/correctness_discovery_prompt.md`

### SV-04: Domain Framework Application → **Merged into DS-01** *(2026-01-22)*
**Status:** DEPRECATED — Use DS-01: Framework Application instead
**Reason:** SV-04 was an advanced variant of DS-01 with parameter definitions; now unified
**See:** DS-01 in Domain-Specific Techniques section (now includes advanced variant with parameters)

### SV-05: Printable Worksheet Output Format
**What:** Specialized output requirements for educational materials that can be printed
**Pattern:**
```markdown
After gathering my answers, output a detailed image generation prompt that will create a black-and-white printable worksheet matching my specifications. The prompt should specify:
- Exact layout
- Spacing for student work
- Any decorative elements
- Whether to include answer key
```
**Used in:** All education prompts (45)
**Why it works:** Bridges AI generation with practical physical outputs; ensures print-ready formatting
**Reference:** `prompts/education/math/education_arithmetic_practice_worksheet.md`

### SV-06: Confirmation-Before-Proceed Protocol
**What:** Explicit instruction to confirm understanding before asking for data or proceeding
**Pattern:**
```markdown
Confirm you understand, then ask me to describe or paste [data type]. Begin now.
```
```markdown
Ask me one question at a time. This is for you: run now.
```
**Used in:** Deep work prompts, correctness prompts
**Why it works:** Creates explicit handoff point; ensures AI is ready to receive input; reduces miscommunication
**Reference:** `prompts/productivity/deep-work/deepwork_team_focus_audit.md`

### SV-07: Calculation Specification in Layout
**What:** Explicit formulas and calculation logic embedded in visual output specifications
**Pattern:**
```markdown
CALCULATIONS TO PERFORM
1) Identify "Biggest Leak" = stage transition with LOWEST conversion %
2) Lost users at each leak = prior stage count − current stage count
3) Severity Score = Lost users × strategic weight
4) Experiment Priority = (expected_lift × confidence) / effort_weight
```
**Used in:** Board-deck prompts (analytics dashboards)
**Why it works:** Makes quantitative reasoning explicit; ensures consistent methodology; auditable outputs
**Different from NE-11 (Embedded Formulas):** Specifically for visual/dashboard outputs with multiple interdependent calculations
**Reference:** `prompts/business/board-decks/board_deck_funnel_diagnostic.md`

### SV-08: Tiered Discovery Questions
**What:** Walk through numbered discovery questions with explicit synthesis instruction at end
**Pattern:**
```markdown
Walk me through the following questions:

1. WHO will use this output, and what decision will they make?
2. What would make this output USELESS?
3. What would make this output DANGEROUS?
4. If the AI isn't sure, what should it do?
   - [Option A]
   - [Option B]
   - [Option C]
5. What's WORSE for your use case: [Tradeoff A] OR [Tradeoff B]?
6. How would you CHECK whether the output is correct?

After I answer all six, synthesize my responses into [deliverable].
```
**Used in:** Correctness prompts (7), codex prompts (6)
**Why it works:** Systematic exploration of requirements; forced tradeoff decisions; leads to actionable synthesis
**Reference:** `prompts/ai-development/correctness/correctness_discovery_prompt.md`

### SV-09: Structured Deliverables with Headings
**What:** Named sections (A-F, 1-5) with explicit content requirements for each
**Pattern:**
```markdown
DELIVERABLES (concrete artifacts, not advice):

A) THE TRIGGER
Pick ONE default-on trigger. Justify why this is best.

B) THE MESSAGE FORMAT
Write the exact template. Include:
- 1-line summary
- Top concerns (max 3)
- Suggested fix

C) THE SYSTEM
Design threshold rules:
- When to post / stay silent
- Escalation rules
- Mute safety valve

D) SAFETY + TRUST
Define:
- What the AI is NEVER allowed to do
- How humans override it

CONSTRAINTS:
- Ask me no more than 5 questions
- Structure output with headings A–F
```
**Used in:** Codex prompts (6), correctness prompts (7)
**Why it works:** Ensures comprehensive coverage; prevents omissions; creates referenceable structure
**Different from ST-04 (Delimited Sections):** Includes specific content requirements per section, not just headers
**Reference:** `prompts/ai-development/codex/workflow_codex_ambient_ai_review_system.md`

### SV-10: Table Output Specification
**What:** Explicit table format with column headers and expected row content
**Pattern:**
```markdown
1. INDIVIDUAL BLOCK COUNTS (table)
| Person | 90+ min blocks | 60-89 min | 30-59 min | Fragments | Deep work hours |

2. TEAM PATTERNS
- Average deep work capacity per person
- Who's most fragmented and why
```
**Used in:** Deep work prompts, board-deck prompts
**Why it works:** Creates scannable, comparable output; forces quantitative analysis; enables tracking over time
**Reference:** `prompts/productivity/deep-work/deepwork_team_focus_audit.md`

### SV-11: Terminology Steering
**What:** Reframe artifact names using print/production terminology to avoid triggering undesired model behaviors (e.g., UI mockup tropes)
**Pattern:**
```markdown
Create FLAT PRINT ARTWORK representing the literal ink-on-paper content that will be sent directly to a printer.
This is NOT a UI card.
This is NOT a product mockup.
```
**Avoid → Use Instead:**
- "card" → "flat print artwork"
- "badge" → "ink-on-paper layout"
- "mockup" → "edge-to-edge print surface"
**Used in:** All image generation prompts in `domain-image-generation/`
**Why it works:** Image models have strong associations with UI terms (rounded corners, shadows, gradients). Print terminology activates different visual priors that produce cleaner, more literal outputs.
**Cross-Reference:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md` — Technique 1

### SV-12: Grid Forcing + Enumerated Slots
**What:** Specify exact grid geometry (NxM) AND assign content to individually numbered slots to prevent model improvisation
**Pattern:**
```markdown
GRID LAYOUT (MOST IMPORTANT):
- EXACTLY 2 ROWS x 3 COLUMNS
- TOTAL OF 6 BOXES PER CARD
- ALL BOXES: Equal width, equal height, evenly spaced, perfectly aligned

BOX 1: [Content A]
BOX 2: [Content B]
BOX 3: [Content C]
BOX 4: [Content D]
BOX 5: [Content E]
BOX 6: [Content F]
```
**Used in:** Badge buddy prompts, worksheet generators, reference card prompts
**Why it works:** Prevents merging content, duplicating items, rearranging priorities, or inventing "better" organization. Models follow explicit enumeration more reliably than abstract layout descriptions.
**Different from SV-01:** SV-01 specifies zones and proportions; SV-12 specifies exact cell counts with individually assigned content per slot
**Cross-Reference:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md` — Technique 2

### SV-13: Constraint Redundancy
**What:** Repeat critical constraints at three or more levels in the prompt to ensure consistent enforcement
**Pattern:**
```markdown
CRITICAL OUTPUT RULES:
- NO gradients of any kind

DESIGN SYSTEM:
- Solid fills only
- No gradients

FINAL VALIDATION CHECK:
- Solid colors only
- No gradients
```
**Levels:** Global rules (policy) → Local rules (implementation) → Final checklist (self-audit)
**Used in:** All image generation prompts requiring strict visual constraints
**Why it works:** Models sometimes "obey once, forget later" in long prompts. Defense-in-depth repetition at policy, implementation, and validation levels dramatically reduces constraint violations.
**Different from QA-01 (Self-Verification):** QA-01 adds a single verification step; SV-13 weaves the same constraint through multiple structural levels of the prompt
**Cross-Reference:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md` — Technique 3

### SV-14: Negative Space Control
**What:** Explicitly control the space around and behind content to prevent models from adding unwanted scene elements
**Pattern:**
```markdown
BACKGROUND:
- Solid white (#FFFFFF) ONLY
- No texture, no vignette, no fade
- NO background beyond the artwork edges

OUTPUT CONSTRAINTS:
- Edge-to-edge artwork (this IS the printed content)
- NO drop shadows
- NO lighting, gloss, bevel, or depth effects
```
**Used in:** Print-ready reference cards, badge buddies, worksheet images
**Why it works:** Models default to composing a "scene" with background, lighting, and depth. Explicitly banning these elements removes the staging context where mockup behaviors emerge.
**Cross-Reference:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md` — Technique 4

### SV-15: Allowed vs. Forbidden Distinction
**What:** Split visual instructions into explicit "allowed" and "forbidden" categories to prevent over-correction
**Pattern:**
```markdown
ALLOWED (structured layouts):
- Aligned columns/rows
- Subtle dividers
- Typographic hierarchy
- Designed tables with consistent spacing

FORBIDDEN (UI/software appearance):
- Excel-like grid with cell boxes
- Spreadsheet sheet headers
- Software interface styling
- Table borders that look like applications
```
**Used in:** Infographic prompts, data visualization prompts, reference materials
**Why it works:** Saying "don't make a spreadsheet" can be interpreted as "don't align data in rows/columns." The allowed/forbidden split gives the model explicit permission to use structural layouts while banning UI chrome.
**Cross-Reference:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md` — Technique 5

### SV-16: Physical Context Anchoring
**What:** Provide real-world physical usage context (dimensions, who uses it, how it's held/viewed) to constrain output appropriately
**Pattern:**
```markdown
IMPORTANT REAL-WORLD CONTEXT:
These are badge buddies.
They are worn BEHIND a nurse's ID badge.
They must be LANDSCAPE (wider than tall).
They are quick-glance clinical references.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT an illustration.
```
**Used in:** Badge buddy prompts, poster prompts, physical reference materials
**Why it works:** Without real-world context, models optimize for "looks cool" not "actually usable." Physical constraints on dimensions, density, and purpose anchor the output to practical requirements.
**Different from RP-02 (Audience-Specific Framing):** RP-02 adjusts language and complexity for the audience; SV-16 constrains physical form factor and usage context for image generation
**Cross-Reference:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md` — Technique 6

### SV-17: Deliverables Locking
**What:** Lock output deliverables with absolute specificity — exact count, orientation, dimensions, and resolution
**Pattern:**
```markdown
CRITICAL OUTPUT RULES (NON-NEGOTIABLE):
- Output EXACTLY TWO IMAGES
- Image 1 = BADGE BUDDY A (FRONT)
- Image 2 = BADGE BUDDY B (BACK)
- Each image must be a SINGLE flat rectangle
- Orientation: LANDSCAPE (horizontal)

PHYSICAL SIZE & CANVAS:
- 4.5 inches wide x 2.75 inches tall
- Resolution: 1350 x 825 px at 300 DPI
```
**Used in:** All multi-output image generation prompts
**Why it works:** Models may produce single images when multiples needed, or wrong dimensions/orientation. Explicit locking with exact numbers prevents ambiguity.
**Different from OC-02 (Structured Output):** OC-02 specifies data format (JSON/XML); SV-17 specifies physical output properties (count, orientation, resolution)
**Cross-Reference:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md` — Technique 7

### SV-18: Image Validation Checklist
**What:** Final self-audit block at the end of an image generation prompt that re-enumerates all critical constraints as pass/fail checks
**Pattern:**
```markdown
FINAL VALIDATION CHECK:
- Two images only
- Landscape orientation
- 2 rows x 3 columns per card
- Equal-sized boxes
- One drug per box
- Flat print artwork
- Solid colors only
- No gradients
- No rounded corners
- No UI or mockup styling
- Optimized for instant badge-level glance

If any gradient, shadow, or rounded corner appears, the output is incorrect.
```
**Used in:** All image generation prompts
**Why it works:** Acts as implicit re-evaluation at the end of a long prompt. The "if X appears, the output is incorrect" language creates a binary pass/fail gate that triggers model self-correction.
**Different from QA-01 (Self-Verification):** QA-01 is a general "verify your work" instruction; SV-18 is a domain-specific checklist with concrete visual criteria and explicit failure language for image generation
**Cross-Reference:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md` — Technique 8

---

## Done Definition Techniques

A specialized category for AI agent task completion verification. These techniques address the "completion problem"—when AI agents claim tasks are done without verifiable proof.

**Core Insight:** Make "done" an observable property instead of an internal state. You're not automating judgment—you're automating verification.

### DD-01: Gate-Based Verification → **Merged into QA-08** *(2026-01-22)*
**Status:** DEPRECATED — Use QA-08: Gate-Based Verification instead
**Reason:** Both QA-08 and DD-01 addressed gate-based pass/fail verification; now unified
**See:** QA-08 in Quality Assurance Techniques section above

### DD-02: Vague-to-Concrete Translation
**What:** Converting adjective-based requirements to noun/verb-based checkable criteria
**Category:** Done Definition
**Use Case:** Task definition, requirements gathering, delegation
**Pattern:**
```markdown
Translation Guide:
- "Be thorough" → "Cover all X items on this list"
- "Include sources" → "Each claim links to URL or cites document + page"
- "Make it actionable" → "Each finding has 'what we do' section with owner"
- "Be professional" → Flag for human review OR decompose further
- "Make it strategic" → "State decision + options considered + tradeoff + recommendation"
```
**Why it works:** Humans speak in adjectives; agents need nouns and verbs
**Variant — Self-Contained Problem Statement:** Rewrite a conversational request into a fully self-contained brief that an agent with zero prior context could execute successfully. Annotate every gap in the original with severity (🔴 critical / 🟡 moderate / 🟢 minor). Use when delegating to autonomous agents or when requests will be executed in a fresh session.

### DD-03: Fail-Fast Ordering
**What:** Ordering gates so cheap checks run before expensive ones
**Category:** Done Definition
**Use Case:** Multi-gate verification, iteration efficiency
**Pattern:**
```markdown
Gate Order (fail-fast):
1. Structure/presence checks (instant) - "Does section exist?"
2. Count/format checks (fast) - "Are all 5 items present?"
3. Source validation (medium) - "Do links work?"
4. Data reconciliation (slow) - "Do totals match?"
```
**Why it works:** Prevents wasted cycles on work doomed from the start
**Principle:** Check cheap things first, expensive things last

### DD-04: MVP Gates
**What:** Identifying the 3 highest-leverage gates for quick validation
**Category:** Done Definition
**Use Case:** Time-constrained verification, rapid iteration
**Pattern:**
```markdown
MVP GATES: The 3 highest-leverage gates if someone only has 5 minutes.
1. [Coverage gate] - Does it cover the required scope?
2. [Evidence gate] - Are claims supported?
3. [Actionability gate] - Is the output usable?
```
**Why it works:** Prevents overengineering while ensuring minimum quality
**Rule:** Maximum 3 gates; prioritize coverage, evidence, actionability

### DD-05: Human Review Flags
**What:** Explicitly separating checkable items from judgment items
**Category:** Done Definition
**Use Case:** Hybrid human-AI workflows, judgment-heavy tasks
**Pattern:**
```markdown
HUMAN REVIEW FLAGS (separate from gate table):
- Is the analysis correct? [JUDGMENT]
- Is the recommendation the right one? [JUDGMENT]
- Are the findings accurate? [JUDGMENT]
```
**Why it works:** Gates check what's checkable; humans judge what requires judgment
**Principle:** Enforce the floor so humans can focus on the ceiling

### DD-06: Iteration Control *(Merged from DD-06 + DD-09)*
**What:** Defining iteration budgets, escalation triggers, and stop conditions
**Category:** Done Definition
**Use Case:** Preventing infinite loops, managing iteration budget, cost management
**Pattern (Stop Policy):**
```markdown
STOP POLICY (one sentence):
"Stop when all MVP gates pass, or after [X] iterations escalate to human with current state and failure log."

Default Budgets:
| Stakes | Max Iterations | Escalation Trigger |
|--------|----------------|-------------------|
| Low    | 3              | 2 gates failing after 3 tries |
| Medium | 5              | Same gate failing 3x in a row |
| High   | 10             | Any gate failing 5x |
```
**Pattern (Iteration Budget with Diagnostics):**
```markdown
Iteration budget: [3 / 5 / 10]

If regularly hitting budget without convergence:
1. Gates are vague (agent can't tell what satisfies them)
2. Gates are impossible (exceeds current capability)
3. Budget is too low for task complexity
```
**Components:**
- **Budget:** Maximum iterations allowed (scales with stakes)
- **Stop conditions:** When to halt iteration
- **Escalation paths:** What to do when budget exhausted
- **Diagnostics:** How to identify why convergence isn't happening
**Why it works:** Makes reliability purchasable; loops only help if budgeted; prevents grinding without convergence or surprise costs
**Note:** Merged DD-09 into DD-06 (2026-01-22) — both address iteration limits and escalation
**Different from DD-10:** DD-06 defines when to stop; DD-10 tracks what changed each iteration
**Different from QA-13:** DD-06 is budget/escalation; QA-13 is failure recovery rules

### DD-07: Self-Audit Table
**What:** Structured proof-of-work table with evidence and location
**Category:** Done Definition
**Use Case:** Every iteration of done-definition loop
**Pattern:**
```markdown
| Gate | Pass? | Evidence | Location |
|------|-------|----------|----------|
| All competitors covered | Y | Acme, Beta, Gamma | H2 headings |
| Each claim sourced | N | 12/15 sourced | 3 in Gamma section unsourced |
| Recommendation stated | Y | "We should..." | Exec Summary para 2 |
```
**Why it works:** Forces agent to actually check; makes verification efficient
**Required columns:** Gate, Pass/Fail, Evidence (not "I checked"), Location
**Different from QA-01:** DD-07 requires structured table with evidence columns; QA-01 is prose-based self-critique
**Different from NE-06:** DD-07 is tabular format with locations; NE-06 uses inline checkpoints

### DD-08: Evidence-Location Pattern → **Merged into RT-05** *(2026-01-22)*
**Status:** DEPRECATED — Use RT-05: Evidence-Based Reasoning instead
**Reason:** Both require evidence with specific locations; DD-08's location formats are now part of RT-05
**See:** RT-05 in Reasoning Techniques section above

### DD-09: Iteration Budget → **Merged into DD-06** *(2026-01-22)*
**Status:** DEPRECATED — Use DD-06: Iteration Control instead
**Reason:** Both DD-06 and DD-09 address iteration limits; now unified with budget, stop conditions, escalation, and diagnostics
**See:** DD-06 in Done Definition Techniques section above

### DD-10: Change Log Iteration
**What:** Brief log each iteration of what changed and why
**Category:** Done Definition
**Use Case:** Diagnosing non-convergence, debugging loops
**Pattern:**
```markdown
Change log each iteration: what you changed + why.

Diagnostic patterns:
| Pattern | What It Means | What to Do |
|---------|---------------|------------|
| Making progress | Changes address failing gates | Continue |
| Thrashing | Fixes one gate, breaks another | Gates conflict |
| Stuck | Changes don't address failing gate | Gate unclear |
```
**Why it works:** Surfaces structural problems early; prevents burning iterations
**Different from DD-06:** DD-10 tracks what changed; DD-06 defines when to stop
**Different from QA-13:** DD-10 is diagnostic logging; QA-13 is failure handling rules

### DD-11: BLOCKED Protocol
**What:** Handling gates that cannot be satisfied due to missing inputs
**Category:** Done Definition
**Use Case:** Graceful degradation, impossible tasks
**Pattern:**
```markdown
If a gate cannot be satisfied due to missing inputs or access:
1. Mark it BLOCKED (not FAIL)
2. Explain WHY it's blocked
3. Escalate per stop policy with current state
4. Specify what's needed to unblock

BLOCKED definition: "You literally cannot proceed without external input—not that the task is hard."
```
**Why it works:** Prevents agent using BLOCKED as escape hatch for difficult work

---

## Technique Combination Strategies (Expanded)

### Visual Dashboard & Report Generation
- Visual Output Specification (SV-01)
- Grouped Input Gathering (SV-02)
- Calculation Specification (SV-07)
- Table Output Specification (SV-10)
- Expert Role Assignment (RP-01)

### Educational Content Creation
- Interview-to-Synthesis Pattern (SV-03)
- Printable Worksheet Format (SV-05)
- Single-Question Pacing (NE-01)
- Audience-Specific Framing (RP-02)

### AI System Quality & Correctness
- Tiered Discovery Questions (SV-08)
- Structured Deliverables (SV-09)
- Framework Application (DS-01)
- Confirmation-Before-Proceed (SV-06)
- Evidence-Based Reasoning (RT-05)

### Productivity & Focus Analysis
- Framework Application (DS-01)
- Grouped Input Gathering (SV-02)
- Table Output Specification (SV-10)
- Single-Question Pacing (NE-01)

### Marketing & Advertising Creative
- Interview-to-Synthesis Pattern (SV-03)
- Visual Output Specification (SV-01)
- Expert Role Assignment (RP-01)
- Audience-Specific Framing (RP-02)

### AI Agent Task Completion (NEW)
- Gate-Based Verification (QA-08)
- Self-Audit Table (DD-07)
- Evidence-Based Reasoning (RT-05)
- MVP Gates (DD-04)
- Iteration Control (DD-06)

---

## Index by Repository Location (Updated)

### Prompts Collection (NEW)
**Location:** `prompts/`
**Total Prompts:** 114 across 6 categories
**Primary Techniques:** SV-01 through SV-10, RP-01, NE-01

#### AI Development
**Location:** `prompts/ai-development/`
**Subdirectories:** codex/ (6), correctness/ (7)
**Primary Techniques:** SV-03, SV-06, SV-08, SV-09, RT-05
**Key Files:**
- `codex/workflow_codex_ambient_ai_review_system.md` - Comprehensive AI review system design
- `correctness/correctness_discovery_prompt.md` - Defining correctness for AI tasks
- `correctness/correctness_eval_design_prompt.md` - Building evaluation frameworks

#### Business/Board Decks
**Location:** `prompts/business/board-decks/`
**Count:** 20 executive visualization prompts
**Primary Techniques:** SV-01, SV-02, SV-07, SV-10, RP-01
**Key Files:**
- `board_deck_funnel_diagnostic.md` - Conversion funnel analysis dashboard
- `board_deck_scenario_planning_matrix.md` - Strategic scenario planning
- `board_deck_rice_ice_prioritization.md` - Feature prioritization framework

#### Marketing/Advertising
**Location:** `prompts/marketing/advertising/`
**Count:** 17 industry-specific advertising prompts
**Primary Techniques:** SV-01, SV-03, RP-01, RP-02
**Key Files:**
- `advertising_premium_service_provider.md` - Service business advertising
- `advertising_tech_product_saas.md` - SaaS product advertising
- `advertising_b2b_professional_services.md` - B2B advertising creative

#### Education
**Location:** `prompts/education/`
**Subdirectories:** math/ (5), language-arts/ (6), science/ (4), social-studies/ (4), arts/ (3), music/ (2), life-skills/ (4), foreign-language/ (2), specialized-formats/ (6), assessment/ (4), early-childhood/ (5)
**Count:** 45 educational worksheet prompts
**Primary Techniques:** SV-03, SV-05, NE-01, RP-02
**Key Files:**
- `math/education_arithmetic_practice_worksheet.md` - Math practice worksheets
- `language-arts/education_reading_comprehension_organizer.md` - Reading comprehension
- `early-childhood/education_tracing_pre_writing.md` - Pre-writing skills

#### Productivity/Deep Work
**Location:** `prompts/productivity/deep-work/`
**Count:** 19 focus management prompts
**Primary Techniques:** DS-01, SV-06, SV-10, NE-01
**Key Files:**
- `deepwork_estimate_focus_parameters.md` - λ/Δ/θ parameter estimation
- `deepwork_team_focus_audit.md` - Team calendar analysis
- `deepwork_one_week_focus_experiment.md` - Focus improvement experiments

---

## High-Priority Techniques - Phase 1 Integration

This section documents the Top 50 high-priority techniques identified from comprehensive analysis of 106 Claude Code resources (7 commands, 32 bundled skills, 67 agents). Full documentation for each technique will be added in Phase 2.

### Context Management (Advanced)

**CM-05: Progressive Context Accumulation** ✓ *Added 2025-12-23*
- Explicitly chain context through multi-step workflows
- See full entry above in Context Management Techniques section

**CM-06: Semantic Vector-Based Context Management** ✓ *Added 2025-12-23*
- Use vector embeddings for intelligent context retrieval
- See full entry above in Context Management Techniques section

**CM-07: Token-Budget-Aware Progressive Loading** ✓ *Added 2025-12-23*
- Dynamically load context in priority order until token budget exhausted
- See full entry above in Context Management Techniques section

### Meta-Prompting (Advanced)

**MP-05: Extended Thinking Documentation** ✓ *Added 2025-12-23*
- System-level reasoning blocks documenting WHY workflows are structured certain ways
- See full entry above in Meta-Prompting Techniques section

### Quality Assurance (Production)

**QA-06: Constitutional AI for Prompts** ✓ *Added 2025-12-23*
- Self-correction with critique-revise loops using constitutional principles
- See full entry above in Quality Assurance Techniques section

**QA-07: Statistical A/B Testing for Prompts** ✓ *Added 2025-12-23*
- Systematic prompt comparison with statistical validation (p < 0.05)
- See full entry above in Quality Assurance Techniques section

**QA-14: Ground Truth Principle**
- **What:** Single authoritative source for specifications to prevent documentation drift
- **Pattern:** Define one canonical source (PRD, spec, contract) that all other documents reference
- **Use Cases:** Production prompts, complex systems, multi-agent workflows
- **Priority:** HIGH (from qa-expert skill)
- **Reference:** Priority 2, Skills with Bundled Resources
- **Why it works:** Prevents inconsistencies from documentation drift; enables single-point updates
- **Full documentation:** New technique - Phase 2
- **Note:** Previously QA-08 (renumbered to resolve ID collision with QA-08: Gate-Based Workflow Validation)

**QA-15: Self-Consistency** ✓ *Added 2026-01-31*
- **What:** Generate multiple independent solutions and select the most consistent answer
- **Pattern:** "Solve this problem 3-5 times independently, then identify the most common/consistent answer"
- **Use Cases:** High-stakes verification, mathematical reasoning, complex decisions requiring confidence
- **Category:** Quality Assurance
- **Why it works:** Reduces variance from single-pass reasoning; surfaces inconsistencies in uncertain domains
- **Research:** Based on Self-Consistency (Wang et al., 2022) - majority voting across diverse reasoning paths
- **Different from QA-01:** QA-01 is single-pass self-critique; QA-15 uses multiple independent generations
- **Different from RP-03:** RP-03 uses different personas; QA-15 uses same prompt multiple times
- **See Also:** QA-01 (Chain-of-Verification), RP-03 (Multi-Persona Debate), QA-04 (Uncertainty Acknowledgment)

### Agentic Techniques (Multi-Agent & Production)

**AG-13: Parallel-Converge Orchestration** ✓ *Added 2025-12-23*
- Parallel agent execution with defined convergence points
- See full entry above in Agentic Techniques section

**AG-14: Cost-Aware Agent Orchestration** ✓ *Added 2025-12-23*
- Strategic LLM model assignment based on task criticality
- See full entry above in Agentic Techniques section

**AG-15: Staged Rollout with Automatic Rollback** ✓ *Added 2025-12-23*
- Progressive deployment with quality monitoring and rollback triggers
- See full entry above in Agentic Techniques section

**AG-16: Master Prompt for Autonomous Multi-Week Execution**
- **What:** 100x productivity improvement through autonomous multi-week processes with state management
- **Pattern:** Long-running workflows with checkpoint tracking, state serialization, auto-resume capability
- **Use Cases:** Complex multi-week processes, autonomous agents, long-running projects
- **Priority:** VERY HIGH (from qa-expert skill)
- **Reference:** Priority 2, Skills with Bundled Resources
- **Why it works:** Enables agents to execute complex multi-phase workflows autonomously over extended periods
- **Full documentation:** New technique - Phase 2

**AG-17: Auto-Resume from Stateful Tracking**
- **What:** Seamless session continuation through CSV-based or structured state management
- **Pattern:** Track progress in persistent storage; resume from last checkpoint on reconnection
- **Use Cases:** Long-running tasks, interrupted workflows, multi-session projects
- **Priority:** HIGH (from qa-expert skill)
- **Reference:** Priority 2, Skills with Bundled Resources
- **Why it works:** Eliminates re-work; maintains context across sessions
- **Full documentation:** New technique - Phase 2

**AG-18: Meta-Skill Self-Reference**
- **What:** Skills that teach skill creation using themselves as exemplars (self-exemplifying architecture)
- **Pattern:** Skill that creates other skills while documenting its own structure as reference
- **Use Cases:** Skill generation, meta-capabilities, teaching by example
- **Priority:** HIGH (from skill-creator skill)
- **Reference:** Priority 2, Skills with Bundled Resources
- **Why it works:** Best documentation is working example; reduces abstraction
- **Full documentation:** New technique - Phase 2

**AG-23: Behavioral Guardrails** → **Merged into AG-04** *(2026-01-22)*
- **Status:** DEPRECATED — Use AG-04: Behavioral Guardrails instead
- **Reason:** Duplicate technique with identical purpose
- **See:** AG-04 in Agency Agent Techniques section above

**AG-26: AI-Augmented Expertise** → **Promoted to Main Section** *(2026-01-22)*
- **Status:** PROMOTED — See full entry in Agency Agent Techniques section above
- **Location:** Search for "### AG-26: AI-Augmented Expertise"

**AG-30: Research-First Behavior**
- **What:** Explicitly use WebSearch for current best practices before providing recommendations
- **Pattern:** Always search for latest information before answering; acknowledge search results
- **Use Cases:** Technology advice, current best practices, version-specific guidance
- **Priority:** HIGH
- **Reference:** Priority 3, Opus 4.5 Agents
- **Why it works:** Ensures currency; prevents outdated recommendations
- **Full documentation:** New technique - Phase 2

**AG-31: Workflow Position Definition**
- **What:** Explicitly define agent position relative to other agents in multi-agent systems
- **Pattern:** Document what comes before this agent, what comes after, handoff protocols
- **Use Cases:** Multi-agent pipelines, orchestration, sequential workflows
- **Priority:** HIGH (critical for multi-agent systems)
- **Reference:** Priority 3, Opus 4.5 Agents
- **Why it works:** Enables agents to know their boundaries and responsibilities
- **Full documentation:** New technique - Phase 2
- **Variant — Contrastive Role Disambiguation:** Add "Use Agent X when [condition], use Agent Y when [condition]" contrastive format to position definitions. Helps agents (and users) disambiguate overlapping capabilities.

### Domain-Specific Techniques (High-Impact)

**DS-13: Architecture-First Enforcement** ✓ *Added 2025-12-23*
- Enforce architectural decisions before implementation
- See full entry above in Domain-Specific Techniques section

**DS-19: Multi-Source Narrative Synthesis** ✓ *Added 2025-12-23*
- Combine fragmented tool data into coherent narratives
- See full entry above in Domain-Specific Techniques section

**DS-22: EARS Requirements Transformation**
- **What:** Aerospace-grade precision for requirements using 5 normative patterns from Rolls-Royce
- **Pattern:** Transform vague requirements into EARS format (Ubiquitous, Event-driven, Unwanted, State-driven, Optional)
- **Use Cases:** Safety-critical systems, regulated industries, high-precision specs
- **Priority:** VERY HIGH (from prompt-optimizer skill)
- **Reference:** Priority 2, Skills with Bundled Resources
- **Why it works:** Eliminates ambiguity; provides testable requirements
- **Full documentation:** New technique - Phase 2
- **Note:** Previously DS-20 (renumbered to resolve ID collision with DS-20: Frontier Mapping)

**DS-23: Domain Theory Grounding** (also ST-26)
- **What:** 40+ theories across 10 domains for systematic framework integration
- **Pattern:** Ground prompts in established academic/industry frameworks
- **Use Cases:** Research-backed analysis, credible recommendations, systematic approaches
- **Priority:** VERY HIGH (from prompt-optimizer skill)
- **Reference:** Priority 2, Skills with Bundled Resources
- **Why it works:** Leverages proven frameworks; increases credibility
- **Full documentation:** New technique - Phase 2
- **Note:** Previously DS-21 (renumbered to resolve ID collision with DS-21: Proximity Assessment)

**DS-24: API Reference Bundling**
- **What:** Include comprehensive API documentation (e.g., 2,161 lines of GitHub API reference) to enable autonomous tool usage
- **Pattern:** Bundle complete API reference in skill resources; load on demand
- **Use Cases:** Tool integration, API-driven workflows, autonomous agents
- **Priority:** HIGH (from github-ops skill)
- **Reference:** Priority 2, Skills with Bundled Resources
- **Why it works:** Eliminates need for external lookups; enables offline operation
- **Full documentation:** New technique - Phase 2

**DS-44: Medallion Architecture Layering**
- **What:** Bronze (raw) → Silver (cleaned) → Gold (aggregated) data transformation pattern
- **Pattern:** Structure data pipelines in layers with clear transformation rules between layers
- **Use Cases:** Data engineering, ETL pipelines, data quality
- **Priority:** HIGH
- **Reference:** Priority 7, Skills without Bundled Resources
- **Why it works:** Provides clear data quality stages; enables incremental refinement
- **Full documentation:** New technique - Phase 2

**DS-48: Multi-Window Burn Rate Alerts**
- **What:** Monitor error budget consumption across multiple time windows (1h, 6h, 24h, 7d, 30d)
- **Pattern:** Progressive alerting based on burn rate velocity in different windows
- **Use Cases:** SRE, reliability engineering, SLO management
- **Priority:** HIGH
- **Reference:** Priority 7, Skills without Bundled Resources
- **Why it works:** Catches both fast-burning incidents and slow degradation
- **Full documentation:** New technique - Phase 2

**DS-50: STRIDE-Per-Interaction Matrix**
- **What:** Apply STRIDE threat model (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) to every interaction point
- **Pattern:** Matrix of interactions × STRIDE categories with risk scores
- **Use Cases:** Security architecture, threat modeling, security reviews
- **Priority:** HIGH
- **Reference:** Priority 7, Skills without Bundled Resources
- **Why it works:** Systematic threat identification; comprehensive coverage
- **Full documentation:** New technique - Phase 2

**DS-56: PostgreSQL Data Type Selection Matrix**
- **What:** Decision matrix for choosing optimal PostgreSQL data types based on use case
- **Pattern:** Table mapping use cases to recommended data types with rationale
- **Use Cases:** Database design, schema optimization, PostgreSQL development
- **Priority:** HIGH
- **Reference:** Priority 7, Skills without Bundled Resources
- **Why it works:** Prevents suboptimal type choices; encodes PostgreSQL expertise
- **Full documentation:** New technique - Phase 2

**DS-61: Security Tier Classification**
- **What:** Defense-in-depth with 6 security layers (Network, Pod, Container, Service Mesh, Application, Data)
- **Pattern:** Classify security controls by layer; ensure coverage at each tier
- **Use Cases:** Kubernetes security, cloud security, layered defense
- **Priority:** HIGH (from k8s-security-policies skill)
- **Reference:** Priority 2, Skills with Bundled Resources
- **Why it works:** Ensures comprehensive security; prevents single-point failures
- **Full documentation:** New technique - Phase 2

**DS-80: Multi-Tiered Template Library**
- **What:** Quick examples → complete references → production templates (progressive complexity scaffolding)
- **Pattern:** Organize templates in tiers: starter → intermediate → production-ready
- **Use Cases:** Developer tools, code generation, skill resources
- **Priority:** HIGH (from k8s-manifest-generator skill)
- **Reference:** Priority 2, Skills with Bundled Resources
- **Why it works:** Reduces cognitive load; enables learning progression
- **Full documentation:** New technique - Phase 2

**DS-107: Version-Specific Expertise** *(Merged from DS-107 + DS-31/AG-27)*
- **What:** Define expertise for specific language AND framework versions
- **Pattern (Languages):** "Expert in Java 21+, Python 3.12+, Rust 1.75+"; highlight version-specific features
- **Pattern (Frameworks):** "Expert in Next.js 14+, React 18+"; highlight modern features introduced in that version
- **Use Cases:** Language agents, framework agents, technology-specific guidance, migration advice
- **Priority:** HIGH (ensures currency)
- **Scope:** Both programming languages AND frameworks/libraries
- **Why it works:** Prevents outdated recommendations; ensures modern patterns; leverages latest features
- **Note:** Merged DS-31/AG-27 into DS-107 (2026-01-22) — both address version-specific expertise
- **Reference:** Priority 3/6, Opus 4.5 Agents / INHERIT Agents

**DS-111: External Methodology Compliance**
- **What:** Strict adherence to external standards (C4 model, OWASP, SRE principles)
- **Pattern:** Reference methodology explicitly; follow prescribed formats exactly
- **Use Cases:** Standards compliance, architecture documentation, industry best practices
- **Priority:** HIGH
- **Reference:** Priority 4, SONNET Agents
- **Why it works:** Ensures compatibility; meets industry expectations
- **Full documentation:** New technique - Phase 2

**DS-113: Async-First Design Principle**
- **What:** Default to async patterns as primary implementation approach
- **Pattern:** Use async/await by default; sync is special case
- **Use Cases:** Modern API development, FastAPI, async frameworks
- **Priority:** HIGH (modern API patterns)
- **Reference:** Priority 3, Opus 4.5 Agents
- **Why it works:** Aligns with modern async-first frameworks; better performance
- **Full documentation:** New technique - Phase 2

**DS-114: Federation Architecture**
- **What:** Distributed schema patterns for multi-team GraphQL development
- **Pattern:** Schema federation with independent subgraphs owned by different teams
- **Use Cases:** GraphQL at scale, microservices, distributed teams
- **Priority:** HIGH (distributed systems)
- **Reference:** Priority 3, Opus 4.5 Agents
- **Why it works:** Enables team autonomy; scales GraphQL adoption
- **Full documentation:** New technique - Phase 2

**DS-117: Polyglot Persistence**
- **What:** Multi-database strategy (SQL, NoSQL, Time-series, Graph) with explicit selection criteria
- **Pattern:** Decision matrix for database selection based on use case characteristics
- **Use Cases:** Database architecture, system design, technology selection
- **Priority:** HIGH (database architecture)
- **Reference:** Priority 3, Opus 4.5 Agents
- **Why it works:** Matches database to use case; prevents over-reliance on single database
- **Full documentation:** New technique - Phase 2

**DS-118: Security-Default Behavioral Traits**
- **What:** Security as default behavior, not optional guidelines
- **Pattern:** Security checks are mandatory, not suggested; agent refuses insecure approaches
- **Use Cases:** Security-critical systems, compliance, production agents
- **Priority:** HIGH
- **Reference:** Priority 4, SONNET Agents
- **Why it works:** Makes security non-negotiable; prevents shortcuts
- **Full documentation:** New technique - Phase 2

**DS-133: FinOps Architecture Integration**
- **What:** Cost optimization as architectural pillar, not afterthought
- **Pattern:** Consider cost implications in every architectural decision; track cost metrics
- **Use Cases:** Cloud architecture, infrastructure design, cost optimization
- **Priority:** HIGH
- **Reference:** Priority 4, SONNET Agents
- **Why it works:** Prevents cost overruns; makes cost a first-class concern
- **Full documentation:** New technique - Phase 2

**DS-148: TDD-First Development Pattern**
- **What:** Write tests before implementation as mandatory workflow step
- **Pattern:** Test → Implementation → Refactor cycle enforced by agent
- **Use Cases:** Quality engineering, test-driven development, reliability
- **Priority:** HIGH
- **Reference:** Priority 4, SONNET Agents
- **Why it works:** Ensures testability; catches design issues early
- **Full documentation:** New technique - Phase 2

### Structural Techniques (Architecture Patterns)

**ST-16: Behavioral Trait Declarations** → **Promoted to Main Section** *(2026-01-22)*
- **Status:** PROMOTED — See full entry in Structural Techniques section above
- **Location:** Search for "### ST-16: Behavioral Trait Declarations"

**ST-22: Multi-Solution Comparison Matrix**
- **What:** Side-by-side comparison of competing approaches with objective criteria
- **Pattern:** Matrix of solutions × evaluation criteria with scores
- **Use Cases:** Technology selection, architecture decisions, tool evaluation
- **Priority:** HIGH
- **Reference:** Priority 6, INHERIT Agents
- **Why it works:** Enables data-driven decisions; surfaces tradeoffs clearly
- **Full documentation:** New technique - Phase 2
- **Variant — School-Based Approach Documentation:** Compare competing schools of thought (not just solutions) with philosophical pros/cons. Example: "Monolith-first school" vs "Microservices-first school" with underlying philosophy.

**ST-35: Principle-Based Guidance**
- **What:** Define explicit principles that govern all recommendations
- **Pattern:** List guiding principles upfront; reference in recommendations
- **Use Cases:** Standards-based domains, architecture, best practices
- **Priority:** HIGH
- **Reference:** Priority 3, Opus 4.5 Agents
- **Why it works:** Ensures consistency; makes rationale transparent
- **Full documentation:** New technique - Phase 2

**ST-37: Minimal Agent Pattern**
- **What:** Ultra-concise agent definition (30-40 lines) focusing on essential elements only
- **Pattern:** Role + Core Capabilities + Key Rules (minimal format)
- **Use Cases:** Lightweight agents, simple tasks, resource-constrained environments
- **Priority:** HIGH (lightweight agent architecture)
- **Reference:** Priority 3, Opus 4.5 Agents
- **Why it works:** Reduces overhead; faster to load and execute
- **Full documentation:** New technique - Phase 2

**ST-38/ST-39: Production-Ready Architecture Patterns**
- **What:** Enterprise-scale architecture patterns with reliability, observability, security built-in
- **Pattern:** Reference architectures with production requirements (HA, DR, monitoring, security)
- **Use Cases:** Enterprise systems, production deployment, high-scale applications
- **Priority:** HIGH
- **Reference:** Priority 6, INHERIT Agents
- **Why it works:** Encodes production lessons; prevents common failures
- **Full documentation:** New technique - Phase 2

**ST-49: Checks-Effects-Interactions Pattern**
- **What:** Smart contract pattern: Checks → Effects → Interactions (CEI) to prevent reentrancy
- **Pattern:** 1) Validate conditions, 2) Update state, 3) External calls (in that order)
- **Use Cases:** Smart contract security, blockchain development, state management
- **Priority:** HIGH (security-critical pattern)
- **Reference:** Priority 7, Skills without Bundled Resources
- **Why it works:** Prevents reentrancy attacks; enforces secure ordering
- **Full documentation:** New technique - Phase 2

### Reasoning Techniques (Analysis Methods)

**RT-13: Multi-Layer Analysis** → **Merged into DT-04** *(2026-01-22)*
- **Status:** DEPRECATED — Use DT-04: Multi-Layer Analysis instead
- **Reason:** Both DT-04 and RT-13 addressed layered analysis; now unified
- **See:** DT-04 in Decomposition Techniques section

**RT-15/RT-20/RT-22: Sequential Response Approach Pattern**
- **What:** Template-driven sequential response with predictable structure
- **Pattern:** Step 1 → Step 2 → Step 3 → Summary (rigid sequence)
- **Use Cases:** Speed-optimized workflows, predictable outputs, HAIKU agents
- **Priority:** MEDIUM
- **Reference:** Priority 5, HAIKU Agents
- **Why it works:** Reduces processing time; enables caching; predictable
- **Full documentation:** New technique - Phase 2

### Interaction Techniques (User Experience)

**IT-19: Three-Tier Information Loading**
- **What:** Metadata → SKILL.md → Bundled resources (progressive disclosure for token economics)
- **Pattern:** Load minimal metadata first; full skill on demand; resources lazily
- **Use Cases:** Large knowledge bases, skill libraries, token optimization
- **Priority:** HIGH (from config-progressive-disclosure skill)
- **Reference:** Priority 2, Skills with Bundled Resources
- **Why it works:** Minimizes token usage; user controls depth
- **Full documentation:** New technique - Phase 2

**IT-35: Mentor-Style Feedback**
- **What:** Educational, constructive communication in feedback (not just correctness)
- **Pattern:** What works well → What to improve → Why it matters → How to improve
- **Use Cases:** Code review, educational feedback, mentorship
- **Priority:** HIGH (critical for feedback-providing agents)
- **Reference:** Priority 3, Opus 4.5 Agents
- **Why it works:** Builds skills; maintains motivation; teaches principles
- **Full documentation:** New technique - Phase 2

### Non-Engineering Techniques (Business & Product)

**NE-13: Technical-to-Business Translation** ✓ *Added 2025-12-23*
- Convert technical details to business value statements
- See full entry above in Non-Engineering Techniques section

**NE-18: Developer Experience Priority**
- **What:** Treat developer experience (DX) as first-class product requirement
- **Pattern:** Evaluate decisions through DX lens; measure DX metrics
- **Use Cases:** API design, tool development, platform engineering
- **Priority:** HIGH
- **Reference:** Priority 4, SONNET Agents
- **Why it works:** Improves adoption; reduces friction; increases productivity
- **Full documentation:** New technique - Phase 2

**DS-31/AG-27: Framework Version Specificity** → **Merged into DS-107** *(2026-01-22)*
- **Status:** DEPRECATED — Use DS-107: Version-Specific Expertise instead
- **Reason:** Both address version-specific expertise; now unified for languages AND frameworks
- **See:** DS-107 in Domain-Specific Techniques (High-Impact) section above

---

## Delegation & Productivity Techniques

Techniques for AI delegation decisions, productivity bottleneck diagnosis, and execution habit optimization.

### DP-01: Tool vs. Colleague Shape Decision
**What:** Multi-dimensional scoring system to determine whether a task needs autonomous AI (tool-shaped) or iterative AI (colleague-shaped)
**Category:** Delegation & Productivity
**Use Case:** AI delegation decisions, task handoff planning, automation assessment
**Pattern:**
```markdown
Score each dimension 0-10, then explain your score in one sentence:

1. SPEC CLARITY: Can I describe the desired outcome precisely right now?
   - 10 = I could write acceptance tests before starting
   - 0 = I need to see drafts to figure out what I want

2. VERIFICATION COST: How hard is it to tell if the output is correct?
   - 10 = I can check in under 5 minutes
   - 0 = Only an expert can tell, or errors won't surface until production

3. REVERSIBILITY: If the output is wrong, how painful is the fix?
   - 10 = I delete it and try again, no cost
   - 0 = Downstream damage, reputation risk, or can't fully undo

4. HIDDEN COUPLING: How likely is this to break something adjacent?
   - 10 = Fully isolated, no dependencies
   - 0 = Deeply entangled, changes cascade unpredictably

5. SHAPE CONFIDENCE: How sure are you this shape choice is correct?
   - 10 = Clear-cut, no ambiguity
   - 0 = Not enough information to decide responsibly
```
**Why it works:** Forces explicit evaluation of delegation suitability before committing
**Five dimensions:** Spec clarity, verification cost, reversibility, coupling, confidence

### DP-02: Refuse Path Protocol
**What:** Graceful degradation when user doesn't provide complete information
**Category:** Delegation & Productivity
**Use Case:** User input handling, prompt robustness, incomplete information scenarios
**Pattern:**
```markdown
REFUSE PATH: If I decline to answer a question or leave a field blank after you ask twice, proceed anyway but:
1. Label every assumption you're making with [ASSUMPTION]
2. Mark the entire output as DRAFT-RISKY
3. List the assumptions at the top of your output so I can correct them
```
**Why it works:** Prevents stalling while making risk visible; enables progress with transparency
**Three components:** Assumption labeling, risk marking, assumption summary

### DP-03: Anchored Scoring Scales
**What:** Concrete behavioral anchors at 0, 5, and 10 for scoring dimensions
**Category:** Delegation & Productivity
**Use Case:** Assessment rubrics, decision frameworks, calibration
**Pattern:**
```markdown
DIMENSION: [Name]
- 10 = [Concrete behavioral description of ideal state]
- 5 = [Concrete behavioral description of middle state]
- 0 = [Concrete behavioral description of worst state]
```
**Why it works:** Eliminates ambiguity in scoring; enables consistent assessment across users

### DP-04: Must-Not Constraints
**What:** Requiring explicit negative constraints in specifications (at least 2 "must not" items)
**Category:** Delegation & Productivity
**Use Case:** Specification writing, scope control, preventing AI scope creep
**Pattern:**
```markdown
E) ACCEPTANCE CRITERIA (7-12 bullets)
   Testable statements a reviewer can check yes/no. Start each with "The output must..." or "The output must not..."

   REQUIRED: At least 2 criteria must be "must not" constraints. Most failures are scope creep and invention, not missing features.
```
**Why it works:** Most AI failures are scope creep and invention, not missing features; "must not" constraints prevent this
**Different from CM-02:** DP-04 requires minimum 2 "must-not"; CM-02 uses full must/should structure
**Different from AG-04:** DP-04 is specification constraints; AG-04 is behavioral guardrails

### DP-05: Stakes-Based Gate Policy
**What:** Mandatory approval gates that scale with task risk level
**Category:** Delegation & Productivity
**Use Case:** Workflow design, risk management, delegation protocols
**Pattern:**
```markdown
APPROVAL GATE POLICY (apply this by default):
- High stakes → approval gate REQUIRED at milestone 1 (plan review) AND before final handoff
- Medium stakes → approval gate REQUIRED before final handoff only
- Low stakes → approval gates optional (but recommended at final handoff)
```
**Why it works:** Right-sizes oversight to risk; prevents both under-review and over-review
**Three levels:** High (two gates), Medium (one gate), Low (optional)
**Different from QA-08:** DP-05 scales gates by risk level; QA-08 defines gate structure
**Different from AG-02:** DP-05 adjusts scrutiny to stakes; AG-02 is always skeptical

### DP-06: Dominant Driver Identification
**What:** Forcing explicit naming of the key factor driving a decision
**Category:** Delegation & Productivity
**Use Case:** Decision documentation, reasoning transparency, reviewable judgments
**Pattern:**
```markdown
Decision rule you used. The rule must be consistent with the scores and must name the dominant driver.

Example: "Verification cost of 3 outweighs spec clarity of 8—colleague-shaped because I can't easily tell if it's right."
```
**Why it works:** Makes decisions reviewable and challengeable; prevents vague justifications

### DP-07: Failure Mode Prediction
**What:** Pre-identifying how the wrong choice fails before making a decision
**Category:** Delegation & Productivity
**Use Case:** Risk assessment, decision quality, stakeholder communication, self-sabotage prevention
**Pattern (Decision Consequences):**
```markdown
FAILURE MODE: "If you choose [wrong shape], here's how it fails: ___"
SWITCH CONDITIONS: "You could use [other shape] if: ___"
```
**Pattern (Self-Sabotage / Fake-Work):**
```markdown
FAILURE MODE (the fake-work I'll do instead if I'm not careful):
[Identify the avoidance behavior you'll default to]
```
**Why it works:** Forces consideration of downside before commitment; documents when to reconsider; surfaces self-sabotage patterns
**Variants:**
- **Decision consequences:** How wrong choice fails (for decisions)
- **Fake-work prediction:** What avoidance behavior you'll default to (for personal productivity)
- **Smart-but-wrong extraction:** Systematically identifies how a competent executor could technically satisfy a request but miss the requester's actual intent. Asks: "Imagine handing this to someone smart with no context — what would they produce that makes you say 'no, that's not what I meant'?" Use before delegating high-stakes tasks.

### DP-08: Role-Based Verification Assignment
**What:** Matching verification checks to verifier capabilities
**Category:** Delegation & Productivity
**Use Case:** QA design, team delegation, verification planning
**Pattern:**
```markdown
ROLE DEFINITIONS (use these when assigning "Who Can Detect"):
- Builder = can run tests, read code, change implementation, validate technical correctness
- Manager = can judge scope/impact/business logic, but not validate technical internals
- Non-tech = can validate format, evidence presence, basic logic, and spot-check outputs

Do not assign Builder-only checks to Non-tech operators.
```
**Why it works:** Prevents mismatched verification; ensures checks are actionable by assignee

### DP-09: Single Primary Constraint Identification
**What:** Forces choosing ONE bottleneck from a defined set rather than listing many issues
**Category:** Delegation & Productivity
**Use Case:** Bottleneck diagnosis, prioritization, focus decisions
**Pattern:**
```markdown
1) Identify my primary bottleneck. Choose ONE:
   - Clarity (I don't know what's worth building or why)
   - Ambition (I'm playing small when I could swing bigger)
   - Distribution (I can build it but can't get it to people)
   - Relationships (I need trust/access I haven't earned yet)

2) Name a secondary bottleneck if present, and explain in one sentence why it's not primary.
```
**Why it works:** Forces prioritization; prevents diffuse effort across multiple "problems"
**Four constraint types:** Clarity, Ambition, Distribution, Relationships

### DP-10: Reframe Generation
**What:** Single sentence that shifts mindset by contrasting what you should vs. shouldn't focus on
**Category:** Delegation & Productivity
**Use Case:** Coaching, mindset shifts, focus clarity
**Pattern:**
```markdown
Give me one sentence that reframes my week:
"Your job right now is ___, not ___."
```
**Why it works:** Creates memorable mindset shift; clarifies focus by explicitly naming what to deprioritize

### DP-11: Safe Experiment Design
**What:** Low-risk, reversible experiments that can be run in a short time window (48 hours)
**Category:** Delegation & Productivity
**Use Case:** Hypothesis testing, bias to action, learning orientation
**Pattern:**
```markdown
Give me a "safe experiment" I can run in 48 hours that is low-risk and reversible.
```
**Why it works:** Converts analysis into action; limits downside while enabling learning
**Time constraint:** 48 hours
**Risk constraint:** Low-risk and reversible

### DP-12: Over-Protection Diagnosis
**What:** Identifying what you're defending that isn't serving you
**Category:** Delegation & Productivity
**Use Case:** Self-awareness, productivity coaching, habit change
**Pattern:**
```markdown
Tell me what I'm mistakenly protecting instead. Examples: execution capacity, consensus, polish, process, permission, my calendar, someone else's approval.
```
**Why it works:** Surfaces hidden defenses that block progress; enables targeted behavior change

### DP-13: Kill Signal Definition
**What:** Observable evidence that should trigger stopping and pivoting
**Category:** Delegation & Productivity
**Use Case:** Experiment design, project management, go/no-go decisions
**Pattern:**
```markdown
Define my signals (48–72 hours):
• Success signal: a behavior, response, metric, or reaction
• Kill signal: what would tell me to stop and try something else
```
**Why it works:** Prevents sunk cost fallacy; creates objective pivot criteria
**Two signals:** Success signal + Kill signal

### DP-14: Compressed Specification Format
**What:** Extremely tight specification format with hard constraints
**Category:** Delegation & Productivity
**Use Case:** Rapid prototyping, MVP definition, scope control
**Pattern:**
```markdown
Rewrite this into a "prototype-as-spec":
- 8 bullet lines maximum
- Each bullet ≤ 12 words
- No preamble, no justification
- Include what's out of scope
```
**Why it works:** Forces ruthless prioritization; eliminates hand-waving and fluff
**Constraints:** 8 bullets max, 12 words each, no preamble, explicit out-of-scope

### DP-15: One-Day Default Rule
**What:** Default to action if task is completable in one day AND reversible
**Category:** Delegation & Productivity
**Use Case:** Breaking permission loops, execution habits, bias to action
**Pattern:**
```markdown
Apply the One-Day Default rule:
If it can be finished in a day AND the downside is reversible, I should build first and show results—not ask first and wait.
Tell me clearly: Does this qualify? Yes or no, with a one-sentence explanation.
```
**Why it works:** Reverses default from "wait for permission" to "act unless blocked"
**Two conditions:** Completable in one day + reversible downside
**Safety exclusions:** Legal/compliance/security/finance approvals, production systems, customer data, public brand/comms

### DP-16: Provisional Decision Message Template
**What:** Pre-written message announcing intent with deadline for objection
**Category:** Delegation & Productivity
**Use Case:** Team communication, permission-free progress, stakeholder management
**Pattern:**
```markdown
PROVISIONAL DECISION MESSAGE (send before or while building):
"I'm going ahead with [X] unless I hear otherwise by [time]. Here's what I'm trying to learn: [Y]. I'll share what happens."

RESULTS MESSAGE (send after):
"I built [X]—here's what happened. [One sentence on what I learned.] Next step I'm considering: [Z]. Thoughts?"
```
**Why it works:** Enables action without blocking permission; keeps stakeholders informed
**Two templates:** Provisional (before) + Results (after)

### DP-17: Distribution Wedge Selection
**What:** Choose ONE distribution channel to focus on for a time-boxed sprint
**Category:** Delegation & Productivity
**Use Case:** Go-to-market strategy, growth focus, distribution planning
**Pattern:**
```markdown
Pick one distribution wedge for me to focus on (best fit):
- Partner
- Platform
- Internal champion
- Community
- Enterprise channel
- Content
Explain why this wedge in 2–3 sentences.
```
**Why it works:** Prevents diffuse marketing effort; enables focused relationship building
**Six wedge options:** Partner, Platform, Internal champion, Community, Enterprise channel, Content

### DP-18: Trust Deposits Definition
**What:** Identifying specific behaviors that compound reliability over time
**Category:** Delegation & Productivity
**Use Case:** Relationship building, credibility development, trust strategy
**Pattern:**
```markdown
Define my trust deposits for the next 14 days:
3–5 behaviors that compound reliability (follow-through, usefulness, responsiveness, etc.)
```
**Why it works:** Makes trust-building concrete and actionable rather than vague

---

## Revision History

- **2026-02-09:** Phase 0 Technique Deduplication Audit — Added 48 novel techniques, updated 17 existing techniques with 23 variants
  - Audited 55 analysis files (~25,000 lines) across 9 batches to identify genuinely novel techniques
  - Of 288 CONFIRMED-NOVEL candidates: 48 ADD, 23 MERGE_WITH_EXISTING, 217 SKIP (domain-specific, archived)
  - New Interaction Techniques (IT) family created with 8 techniques (IT-20 through IT-27)
  - 6 new Structural techniques: ST-40 (Three-Tier Value Classification), ST-42 (Criticality Labeling), ST-43 (Risk-Stratified Documentation), ST-44 (Progressive Complexity Scaffolding), ST-45 (Methodology-Centric Expertise), ST-46 (Assertion-Evidence Content Structure)
  - 3 new Reasoning techniques: RT-09 (Root Cause Explanation), RT-10 (Troubleshooting Decision Tree), RT-11 (Error Recovery Patterns for Prompts)
  - 4 new Output Control techniques: OC-09 (Capability Boundary Specification), OC-10 (Mandatory Disclaimer), OC-11 (Grouped Reporting by Pattern Type), OC-12 (External Reference Catalog)
  - 2 new Quality Assurance techniques: QA-16 (Quality Rubric with Auto-Iteration), QA-17 (Named Scores for Multi-Dimensional Metrics)
  - 6 new Non-Engineering techniques: NE-14 (Multi-Audience Documentation Targeting), NE-15 (Data Storytelling Framework), NE-16 (Non-Judgmental Comparison), NE-17 (Call-to-Action Mandatory Close), NE-19 (Documentation-as-Product Philosophy), NE-20 (Third-Party Handoff Package)
  - 15 new Domain-Specific techniques: DS-25 through DS-40 covering chart selection, safe defaults, environment-specific guidance, regulatory enumeration, LLM-as-Judge, blocker escalation, progressive abstraction, and more
  - 8 new Interaction techniques: IT-20 (Progressive Example Complexity), IT-21 (Use Case-Driven Documentation), IT-22 (Workflow Decision Matrix), IT-23 (Symptom-Based Troubleshooting), IT-24 (Template-Based Educational Scaffolding), IT-25 (Tool Hierarchy Guidance), IT-26 (Reference Catalog Pattern), IT-27 (Multi-Template Selection Guide)
  - 3 new Agentic techniques: AG-19 (Time-Critical Response Protocol), AG-20 (Meta-Skill Pattern Discovery), AG-21 (Orchestration with Dual-Path Output)
  - 1 new Educational technique: ED-06 (Example Quantity Specification)
  - 1 new Meta-Prompting technique: MP-08 (Four-Layer Enhancement Process)
  - 23 variant/extension updates to existing techniques: DS-06, AG-09, RT-05 (2 variants), QA-10, AG-07, QA-13, QA-08 (2 variants), QA-01, DS-02, CM-06, CM-07, CM-10, AG-31, ST-22, NE-13, DT-05, DT-01, AG-05 (2 variants)
  - Corrected "604 techniques" claim to "241 formally defined techniques"
  - Total techniques now **241** across 19 categories
  - Source: Phase 0 Technique Deduplication Audit (`_extraction/NOVEL_TECHNIQUES_SHORTLIST.md`)

- **2025-12-24:** Phase 1 Integration - Added Top 50 high-priority techniques from comprehensive analysis
  - Updated total technique count: 96 → 535 (84 base + 451 from comprehensive Claude Code analysis)
  - Added "High-Priority Techniques - Phase 1 Integration" section documenting Top 50 techniques
  - Techniques span 8 categories: Context Management (3), Meta-Prompting (1), Quality Assurance (3), Agentic (9), Domain-Specific (22), Structural (6), Reasoning (2), Interaction (2), Non-Engineering (2)
  - 12 techniques already added on 2025-12-23, 38 new technique entries added
  - Full documentation for each technique to be added in Phase 2
  - Source: Comprehensive analysis of 106 Claude Code resources (7 commands, 32 bundled skills, 67 agents)
  - Integration Status: Phase 1 In Progress

- **2025-12-23:** Added 12 techniques from Claude Code resource analysis (Task 3.3 completion)
  - **MP-05:** Extended Thinking Documentation - System-level design rationale for complex workflows
  - **CM-05:** Progressive Context Accumulation - Explicit context chaining through workflow phases
  - **CM-06:** Semantic Vector-Based Context Management - Embeddings for intelligent context retrieval
  - **CM-07:** Token-Budget-Aware Progressive Loading - Dynamic context loading within token limits
  - **DS-13:** Architecture-First Enforcement - Blocking implementation until architecture complete
  - **DS-19:** Multi-Source Narrative Synthesis - Combining fragmented tool data into coherent narratives
  - **AG-13:** Parallel-Converge Orchestration - Parallel agent execution with convergence points
  - **AG-14:** Cost-Aware Agent Orchestration - Strategic model assignment based on task criticality
  - **AG-15:** Staged Rollout with Automatic Rollback - Progressive deployment with quality monitoring
  - **QA-06:** Constitutional AI for Prompts - Critique-revise loops for prompt quality
  - **QA-07:** Statistical A/B Testing for Prompts - Rigorous experimental methods for prompt comparison
  - **NE-13:** Technical-to-Business Translation - Converting technical details to business value statements
  - Added 4 new technique combination strategies for 2025 workflows
  - Total techniques now **96** across 13 categories (from 84)
  - Source: Analysis of 106 Claude Code resources (7 commands, 32 skills, 67 agents) revealing 451 novel techniques

- **2025-12-18:** Added Specialized Visual & Interview Techniques category
  - 10 new techniques (SV-01 through SV-10) from extracted prompts collection
  - Visual output patterns: Layout Specification, Printable Formats, Table Outputs
  - Interview patterns: Grouped Input Gathering, Interview-to-Synthesis, Tiered Discovery
  - Domain patterns: Framework Application with Parameters, Calculation Specification
  - Added 5 new technique combination strategies
  - Updated repository index with prompts/ collection (114 prompts across 6 categories)
  - Total techniques now 84+ across 13 categories

- **2025-12-08:** Added Non-Engineering Techniques category
  - 12 new techniques (NE-01 through NE-12) from non-engineering prompts collection
  - Interactive dialogue patterns: Single-Question Pacing, Phased Workflows
  - Input structuring: Template Scaffolding, Catchall Context Gathering
  - Quality controls: Self-Audit Requirements, Token Budget Control
  - Decision support: Scope Reduction Pressure, Probability-Weighted Scenarios
  - Total techniques now 74+ across 12 categories

- **2025-12-08:** Added Agentic Techniques category
  - 12 new techniques (AG-01 through AG-12) from agency-agents collection
  - Multi-agent orchestration and quality gate patterns
  - Personality-first role definition and memory architecture
  - Total techniques now 62+ across 11 categories

- **2025-12-08:** Initial comprehensive index created
  - 50+ techniques cataloged
  - Cross-referenced with all repository prompts
  - Organized by 10 major categories
  - Added combination strategies and usage guides
