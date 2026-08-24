# Master Technique Index — Reference List

**Generated:** 2026-02-08
**Source:** `techniques/MASTER_TECHNIQUE_INDEX.md`
**Purpose:** Flat reference of all technique codes, names, and brief descriptions for cross-referencing against the Consolidated Technique Inventory (Step 0.2b).

---

## Summary

- **Total Active Techniques:** 169
- **Deprecated/Merged Techniques:** 10
- **Families:** 17 (ST, RT, OC, QA, CM, RP, DT, ED, MP, DS, AG, NE, SV, DD, DP, QS, MA)

---

## Active Techniques

| # | Code | Name | Family | Brief Description |
|---|------|------|--------|-------------------|
| 1 | ST-01 | Clear Objective Statement | ST | Concise, unambiguous opening that defines the task's purpose |
| 2 | ST-02 | Structured Sequential Instructions | ST | Numbered, step-by-step instructions breaking complex tasks into subtasks |
| 3 | ST-03 | Output Format Specification | ST | Dedicated section describing format, structure, and content requirements (merged from ST-03 + OC-01) |
| 4 | ST-04 | Delimited Sections | ST | Markdown headers or clear separators for multi-part responses |
| 5 | ST-05 | Hierarchical Organization | ST | Nested structure with main points and sub-points |
| 6 | ST-16 | Behavioral Trait Declarations | ST | Explicit declaration of agent behavioral traits separate from domain expertise |
| 7 | ST-22 | Multi-Solution Comparison Matrix | ST | Side-by-side comparison of competing approaches with objective criteria |
| 8 | ST-35 | Principle-Based Guidance | ST | Define explicit principles that govern all recommendations |
| 9 | ST-37 | Minimal Agent Pattern | ST | Ultra-concise agent definition (30-40 lines) focusing on essential elements only |
| 10 | ST-38/ST-39 | Production-Ready Architecture Patterns | ST | Enterprise-scale architecture patterns with reliability, observability, security built-in |
| 11 | ST-49 | Checks-Effects-Interactions Pattern | ST | Smart contract pattern: Checks → Effects → Interactions (CEI) to prevent reentrancy |
| 12 | RT-01 | Chain-of-Thought (CoT) | RT | Explicit instruction to show step-by-step reasoning |
| 13 | RT-02 | Multi-Dimensional Analysis Framework | RT | Instructions to analyze from multiple perspectives (Location, Description, Impact, Severity, Recommendations) |
| 14 | RT-03 | Tree of Thoughts | RT | Generate multiple approaches and compare them |
| 15 | RT-04 | Analogical Reasoning | RT | Explain concepts through analogies from familiar domains |
| 16 | RT-05 | Evidence-Based Reasoning | RT | Require specific evidence with explicit locations for all claims (merged from RT-05 + DD-08) |
| 17 | RT-06 | Correlation and Cross-Analysis | RT | Combine multiple data sources or metrics |
| 18 | RT-07 | Cascade Effect Analysis | RT | Mapping first-order, second-order, and third-order effects |
| 19 | RT-08 | Workaround Cost Analysis | RT | Document current solutions and their costs to validate real problems |
| 20 | RT-15/RT-20/RT-22 | Sequential Response Approach Pattern | RT | Template-driven sequential response with predictable structure |
| 21 | OC-02 | JSON Schema Specification | OC | Provide exact JSON structure expected |
| 22 | OC-03 | Markdown Table Specification | OC | Specify table structure with column headers |
| 23 | OC-04 | Conditional Output Logic | OC | Instructions for what to output when nothing found |
| 24 | OC-05 | Minimum Length Requirements | OC | Specify minimum depth or length to prevent oversimplification |
| 25 | OC-06 | Output Contract Structure | OC | Standardized 5-part output format for predictable structure |
| 26 | OC-07 | Operating Principles Declaration | OC | Explicit enumeration of behavior rules before task execution |
| 27 | OC-08 | Multi-Mode Prompt Architecture | OC | Single prompt with multiple modes triggered by user selection |
| 28 | QA-01 | Self-Verification | QA | Built-in self-critique step requiring review after initial response (merged from QA-01 + QA-03) |
| 29 | QA-02 | Adversarial Stress-Test | QA | Attack your own answer to find vulnerabilities |
| 30 | QA-04 | Uncertainty Acknowledgment | QA | Explicitly state confidence levels and limitations |
| 31 | QA-05 | Citation Requirements | QA | Require sources for claims |
| 32 | QA-06 | Constitutional AI for Prompts | QA | Critique-revise loops against defined constitutional principles |
| 33 | QA-07 | Statistical A/B Testing for Prompts | QA | Rigorous experimental methods to compare prompt variations |
| 34 | QA-08 | Gate-Based Verification | QA | Binary pass/fail checkpoints that must pass before proceeding (merged from QA-08 + DD-01) |
| 35 | QA-09 | Reversibility Assessment | QA | Dedicated evaluation of whether actions can be undone |
| 36 | QA-10 | Test Battery Protocol | QA | Systematic pre-ship testing checklist with specific tests |
| 37 | QA-11 | Pass/Fail Test Harness | QA | Structured testing with explicit pass criteria and remediation paths |
| 38 | QA-12 | False Positives Identification | QA | Explicit section to identify what NOT to pay attention to |
| 39 | QA-13 | Failure Recovery Specification | QA | Explicit rules for handling repeated failures |
| 40 | QA-14 | Ground Truth Principle | QA | Single authoritative source for specifications to prevent documentation drift |
| 41 | QA-15 | Self-Consistency | QA | Generate multiple independent solutions and select the most consistent answer |
| 42 | CM-01 | Explicit Context Framing | CM | Provide all relevant background upfront |
| 43 | CM-02 | Constraint Specification | CM | Explicit must/must-not requirements |
| 44 | CM-03 | Scope Definition | CM | Clearly define boundaries of analysis |
| 45 | CM-04 | Summary-Expand Loop | CM | Compress conversation at token limits, then expand in new session |
| 46 | CM-05 | Progressive Context Accumulation | CM | Explicitly chain context through multi-step workflows |
| 47 | CM-06 | Semantic Vector-Based Context Management | CM | Use vector embeddings and similarity search for intelligent context retrieval |
| 48 | CM-07 | Token-Budget-Aware Progressive Loading | CM | Dynamically load context components in priority order until token budget exhausted |
| 49 | CM-08 | File-Based State Persistence | CM | Using structured files to maintain context across sessions |
| 50 | CM-09 | Authority Boundary Specification | CM | Explicit three-zone permission model for agent actions |
| 51 | CM-10 | Memory Scaffold Architecture | CM | Structured persistent context file with standardized sections |
| 52 | RP-01 | Expert Role Assignment | RP | Assign specific expert persona |
| 53 | RP-02 | Audience-Specific Framing | RP | Tailor explanation to specific audience |
| 54 | RP-03 | Multi-Persona Debate | RP | Simulate debate between experts with different priorities |
| 55 | RP-04 | Socratic Dialogue | RP | Question-and-answer format for learning |
| 56 | RP-05 | Temperature Simulation | RP | Provide cautious and confident analyses, then synthesize |
| 57 | DT-01 | Hierarchical Task Breakdown | DT | Break complex tasks into phases and subtasks |
| 58 | DT-02 | Specific Focus Areas with Examples | DT | Detailed enumeration of what to look for |
| 59 | DT-03 | Iterative Refinement | DT | Multiple passes to perfect output |
| 60 | DT-04 | Multi-Layer Analysis | DT | Analysis from surface issues to systemic patterns (merged from DT-04 + RT-13) |
| 61 | DT-05 | Element-by-Element Assessment Matrix | DT | Systematic capability evaluation for each component |
| 62 | DT-06 | Typography Decision Tree | DT | Binary decision tree for classification using yes/no questions |
| 63 | ED-01 | Iterative Scaffolding | ED | One concept at a time, check understanding, then proceed |
| 64 | ED-02 | Progressive Exercise Generation | ED | Create exercises matched to current skill level |
| 65 | ED-03 | Guided Discovery | ED | Ask guiding questions instead of giving answers |
| 66 | ED-04 | Personalization Hooks | ED | Ask about interests and incorporate into lessons |
| 67 | ED-05 | Reference Class Priming | ED | Show example of excellent output, then ask for similar quality |
| 68 | MP-01 | Reverse Prompting | MP | Ask AI to write the optimal prompt, then execute it |
| 69 | MP-02 | Recursive Optimization | MP | Iteratively improve a prompt through versions |
| 70 | MP-03 | Task Clarification | MP | Ask for requirements before proceeding |
| 71 | MP-04 | Strategic Edge Case Calibration | MP | Provide baseline, failure mode, and edge case examples |
| 72 | MP-05 | Extended Thinking Documentation | MP | Embed system-level reasoning blocks explaining WHY workflows are structured |
| 73 | MP-06 | Fallback Question Protocol | MP | Systematic "ask questions if insufficient info" pattern |
| 74 | MP-07 | Pattern Recognition Reflection | MP | Systematic reflection on behavioral patterns across time |
| 75 | DS-01 | Framework Application | DS | Apply established business/analysis frameworks with optional parameter definitions (merged from DS-01 + SV-04) |
| 76 | DS-02 | Metric Specification | DS | Define specific, measurable criteria |
| 77 | DS-03 | Tool and Methodology Suggestions | DS | Recommend specific tools or approaches |
| 78 | DS-04 | Pattern Recognition Requests | DS | Identify trends, patterns, systemic issues |
| 79 | DS-05 | Visualization and Communication Guidance | DS | Specify how to present findings visually |
| 80 | DS-06 | Prioritization and Severity Guidance | DS | Explicit instructions to rank findings |
| 81 | DS-13 | Architecture-First Enforcement | DS | Enforce architectural decisions before implementation |
| 82 | DS-19 | Multi-Source Narrative Synthesis | DS | Combine structured data from multiple fragmented tools into coherent narratives |
| 83 | DS-20 | Frontier Mapping (Capability Classification) | DS | GREEN/YELLOW/RED classification system for capabilities |
| 84 | DS-21 | Proximity Assessment (Timeline Classification) | DS | Classify capability gaps by timeline to solution |
| 85 | DS-22 | EARS Requirements Transformation | DS | Aerospace-grade precision for requirements using 5 normative patterns |
| 86 | DS-23 | Domain Theory Grounding | DS | 40+ theories across 10 domains for systematic framework integration |
| 87 | DS-24 | API Reference Bundling | DS | Include comprehensive API documentation to enable autonomous tool usage |
| 88 | DS-44 | Medallion Architecture Layering | DS | Bronze (raw) → Silver (cleaned) → Gold (aggregated) data transformation pattern |
| 89 | DS-48 | Multi-Window Burn Rate Alerts | DS | Monitor error budget consumption across multiple time windows |
| 90 | DS-50 | STRIDE-Per-Interaction Matrix | DS | Apply STRIDE threat model to every interaction point |
| 91 | DS-56 | PostgreSQL Data Type Selection Matrix | DS | Decision matrix for choosing optimal PostgreSQL data types |
| 92 | DS-61 | Security Tier Classification | DS | Defense-in-depth with 6 security layers |
| 93 | DS-80 | Multi-Tiered Template Library | DS | Quick examples → complete references → production templates |
| 94 | DS-107 | Version-Specific Expertise | DS | Define expertise for specific language AND framework versions (merged from DS-107 + DS-31/AG-27) |
| 95 | DS-111 | External Methodology Compliance | DS | Strict adherence to external standards (C4, OWASP, SRE) |
| 96 | DS-113 | Async-First Design Principle | DS | Default to async patterns as primary implementation approach |
| 97 | DS-114 | Federation Architecture | DS | Distributed schema patterns for multi-team GraphQL development |
| 98 | DS-117 | Polyglot Persistence | DS | Multi-database strategy with explicit selection criteria |
| 99 | DS-118 | Security-Default Behavioral Traits | DS | Security as default behavior, not optional guidelines |
| 100 | DS-133 | FinOps Architecture Integration | DS | Cost optimization as architectural pillar, not afterthought |
| 101 | DS-148 | TDD-First Development Pattern | DS | Write tests before implementation as mandatory workflow step |
| 102 | AG-01 | Personality-First Role Definition | AG | Define agents with personality traits, memory, and experience |
| 103 | AG-02 | Skeptical Default Stance | AG | Default to skepticism/failure, requiring overwhelming proof for approval |
| 104 | AG-03 | Layered Mission Hierarchy | AG | Primary → Secondary → Tertiary missions with default requirements |
| 105 | AG-04 | Behavioral Guardrails | AG | Explicit behavioral constraints that apply to all agent actions (merged from AG-04 + AG-23) |
| 106 | AG-05 | Concrete Deliverable Templates | AG | Include actual working code/examples, not placeholder templates |
| 107 | AG-06 | Memory & Learning Architecture | AG | Explicit sections defining what the agent learns and remembers |
| 108 | AG-07 | Pipeline Orchestration Patterns | AG | Multi-agent coordination with explicit handoff protocols |
| 109 | AG-08 | Evidence-Based Decision Gates | AG | Require visual/quantitative proof, not just assertions |
| 110 | AG-09 | Anti-Pattern & Failure Mode Embedding | AG | Explicitly document what leads to failure, embedded in agent identity |
| 111 | AG-10 | Emotional Context Spectrum | AG | Define how personality adapts across different emotional contexts |
| 112 | AG-11 | Taxonomy-Based Classification Systems | AG | Create structured taxonomies for categorizing approaches/elements |
| 113 | AG-12 | Quantitative Success Metrics | AG | Define success with specific, measurable thresholds |
| 114 | AG-13 | Parallel-Converge Orchestration | AG | Parallel agent execution with defined convergence points |
| 115 | AG-14 | Cost-Aware Agent Orchestration | AG | Strategically assign LLM models based on task criticality |
| 116 | AG-15 | Staged Rollout with Automatic Rollback | AG | Progressive deployment with quality monitoring and rollback triggers |
| 117 | AG-16 | Master Prompt for Autonomous Multi-Week Execution | AG | Autonomous multi-week processes with state management |
| 118 | AG-17 | Auto-Resume from Stateful Tracking | AG | Seamless session continuation through structured state management |
| 119 | AG-18 | Meta-Skill Self-Reference | AG | Skills that teach skill creation using themselves as exemplars |
| 120 | AG-26 | AI-Augmented Expertise | AG | Define expertise that integrates AI tools as core capability |
| 121 | AG-30 | Research-First Behavior | AG | Explicitly use WebSearch for current best practices before recommendations |
| 122 | AG-31 | Workflow Position Definition | AG | Explicitly define agent position relative to other agents |
| 123 | NE-01 | Single-Question Pacing Protocol | NE | Ask only one question at a time, pausing for user response |
| 124 | NE-02 | Phased Workflow Architecture | NE | Explicit Phase 1 → Phase 2 → Phase 3 structure with clear handoff logic |
| 125 | NE-03 | Input Template Scaffolding | NE | Dedicated "Your Input" section with labeled placeholder fields |
| 126 | NE-04 | Good vs Bad Example Calibration | NE | Explicit contrast pairs (bad → good) to calibrate quality |
| 127 | NE-05 | Token Budget Control | NE | Explicit token/word limits with fallback instructions |
| 128 | NE-06 | Self-Audit Requirements | NE | Explicit SELF-AUDIT section for verifying output meets criteria |
| 129 | NE-07 | Emotional Validation First | NE | Acknowledge emotional impact before proceeding to analytical work |
| 130 | NE-08 | Catchall Context Gathering | NE | Initial open-ended collection of unstructured information |
| 131 | NE-09 | Scope Reduction Pressure | NE | Explicit instructions to challenge, cut, and reduce scope |
| 132 | NE-10 | Probability-Weighted Scenarios | NE | Multiple scenarios with explicit probability weights |
| 133 | NE-11 | Embedded Calculation Formulas | NE | Direct calculation formulas embedded in the prompt |
| 134 | NE-12 | Cognitive Mode Framing | NE | Explicit THINK/ROLE/MODE directive that sets reasoning stance |
| 135 | NE-13 | Technical-to-Business Translation | NE | Convert technical details to business value statements |
| 136 | NE-18 | Developer Experience Priority | NE | Treat developer experience (DX) as first-class product requirement |
| 137 | SV-01 | Visual Output Specification | SV | Detailed image generation requirements with precise layouts |
| 138 | SV-02 | Grouped Input Gathering | SV | Numbered GROUP sections for collecting structured input |
| 139 | SV-03 | Interview-to-Synthesis Pattern | SV | Gather information through questions, then synthesize into deliverable |
| 140 | SV-05 | Printable Worksheet Output Format | SV | Specialized output requirements for educational materials that can be printed |
| 141 | SV-06 | Confirmation-Before-Proceed Protocol | SV | Explicit instruction to confirm understanding before proceeding |
| 142 | SV-07 | Calculation Specification in Layout | SV | Explicit formulas and calculation logic in visual output specifications |
| 143 | SV-08 | Tiered Discovery Questions | SV | Numbered discovery questions with explicit synthesis at end |
| 144 | SV-09 | Structured Deliverables with Headings | SV | Named sections (A-F) with explicit content requirements |
| 145 | SV-10 | Table Output Specification | SV | Explicit table format with column headers and expected row content |
| 146 | DD-02 | Vague-to-Concrete Translation | DD | Converting adjective-based requirements to noun/verb-based criteria |
| 147 | DD-03 | Fail-Fast Ordering | DD | Ordering gates so cheap checks run before expensive ones |
| 148 | DD-04 | MVP Gates | DD | Identifying the 3 highest-leverage gates for quick validation |
| 149 | DD-05 | Human Review Flags | DD | Explicitly separating checkable items from judgment items |
| 150 | DD-06 | Iteration Control | DD | Defining iteration budgets, escalation triggers, and stop conditions (merged from DD-06 + DD-09) |
| 151 | DD-07 | Self-Audit Table | DD | Structured proof-of-work table with evidence and location |
| 152 | DD-10 | Change Log Iteration | DD | Brief log each iteration of what changed and why |
| 153 | DD-11 | BLOCKED Protocol | DD | Handling gates that cannot be satisfied due to missing inputs |
| 154 | DP-01 | Tool vs. Colleague Shape Decision | DP | Multi-dimensional scoring for autonomous vs iterative AI delegation |
| 155 | DP-02 | Refuse Path Protocol | DP | Graceful degradation when user doesn't provide complete information |
| 156 | DP-03 | Anchored Scoring Scales | DP | Concrete behavioral anchors at 0, 5, and 10 for scoring |
| 157 | DP-04 | Must-Not Constraints | DP | Requiring explicit negative constraints (at least 2 "must not" items) |
| 158 | DP-05 | Stakes-Based Gate Policy | DP | Mandatory approval gates that scale with task risk level |
| 159 | DP-06 | Dominant Driver Identification | DP | Forcing explicit naming of the key factor driving a decision |
| 160 | DP-07 | Failure Mode Prediction | DP | Pre-identifying how the wrong choice fails before making a decision |
| 161 | DP-08 | Role-Based Verification Assignment | DP | Matching verification checks to verifier capabilities |
| 162 | DP-09 | Single Primary Constraint Identification | DP | Forcing choosing ONE bottleneck from a defined set |
| 163 | DP-10 | Reframe Generation | DP | Single sentence that shifts mindset by contrasting focus areas |
| 164 | DP-11 | Safe Experiment Design | DP | Low-risk, reversible experiments in a short time window (48 hours) |
| 165 | DP-12 | Over-Protection Diagnosis | DP | Identifying what you're defending that isn't serving you |
| 166 | DP-13 | Kill Signal Definition | DP | Observable evidence that should trigger stopping and pivoting |
| 167 | DP-14 | Compressed Specification Format | DP | Extremely tight specification format with hard constraints |
| 168 | DP-15 | One-Day Default Rule | DP | Default to action if task is completable in one day AND reversible |
| 169 | DP-16 | Provisional Decision Message Template | DP | Pre-written message announcing intent with deadline for objection |
| 170 | DP-17 | Distribution Wedge Selection | DP | Choose ONE distribution channel to focus on for a time-boxed sprint |
| 171 | DP-18 | Trust Deposits Definition | DP | Identifying specific behaviors that compound reliability over time |
| 172 | DP-19 | Gate Check Pattern | DP | Require specific context before proceeding—refuse to guess |
| 173 | DP-20 | Strict Coach Persona | DP | Define persona that refuses to give advice until questions answered |
| 174 | DP-21 | Consumable Artifact Requirement | DP | Require outputs understandable by others in 60 seconds |
| 175 | DP-22 | Distribution Fallback | DP | Forced accountability with escalating commitment options |
| 176 | DP-23 | Path Variants | DP | Same prompt structure with role-specific customization |
| 177 | DP-24 | Done Fudge Prevention | DP | Done definitions specific enough to prevent rationalizing incomplete work |
| 178 | QS-01 | Training vs Rules Diagnosis | QS | Classify problems by cognitive load to determine training vs rules |
| 179 | QS-02 | Checkable Rule Format | QS | Structured format for documenting rules with triggers, patterns, exceptions |
| 180 | QS-03 | Micro-lesson Structure | QS | Training curriculum through failure stories and exercises |
| 181 | QS-04 | Drift vs Violation Distinction | QS | Separate technical violations from spirit violations that technically pass |
| 182 | QS-05 | Required Decisions Pattern | QS | Force specific decisions rather than making them optional |
| 183 | QS-06 | Exception Template Design | QS | Lightweight exception request format (5 fields max) |
| 184 | MA-01 | Multi-Agent Failure Taxonomy | MA | Five canonical failure patterns for diagnosing multi-agent problems |
| 185 | MA-02 | Two-Tier Architecture (Planner/Worker/Judge) | MA | Three-role separation of concerns for multi-agent systems |
| 186 | MA-03 | Worker Isolation Principle | MA | Workers never coordinate with each other—isolation prevents collision |
| 187 | MA-04 | Tool Diet Pattern | MA | Minimize tool sprawl with Always-On vs On-Demand separation |
| 188 | MA-05 | Session Lifecycle Design | MA | Design for session endings as normal events, not exceptions |
| 189 | MA-06 | Scope Boundary Test | MA | Heuristic for determining when a task is too big for a single worker |
| 190 | MA-07 | Contention Risk Assessment | MA | Evaluate shared resources for contention risk (Low/Medium/High) |
| 191 | MA-08 | Judge Decision Rules | MA | Explicit ACCEPT/RETRY/REJECT decision triggers for quality evaluation |
| 192 | IT-19 | Three-Tier Information Loading | IT | Metadata → SKILL.md → Bundled resources (progressive disclosure) |
| 193 | IT-35 | Mentor-Style Feedback | IT | Educational, constructive communication in feedback |

---

## Deprecated/Merged Techniques

These codes are no longer active — they have been merged into other techniques.

| # | Code | Original Name | Merged Into | Date |
|---|------|--------------|-------------|------|
| 1 | OC-01 | Output Format Templates | ST-03 | 2026-01-22 |
| 2 | QA-03 | Reflection and Self-Critique | QA-01 | 2026-01-22 |
| 3 | SV-04 | Domain Framework Application | DS-01 | 2026-01-22 |
| 4 | DD-01 | Gate-Based Verification | QA-08 | 2026-01-22 |
| 5 | DD-08 | Evidence-Location Pattern | RT-05 | 2026-01-22 |
| 6 | DD-09 | Iteration Budget | DD-06 | 2026-01-22 |
| 7 | RT-13 | Multi-Layer Analysis | DT-04 | 2026-01-22 |
| 8 | AG-23 | Behavioral Guardrails (duplicate) | AG-04 | 2026-01-22 |
| 9 | DS-31/AG-27 | Framework Version Specificity | DS-107 | 2026-01-22 |
| 10 | QA-14 (old) | (renumbered) | QA-14 (new) | Note: renumbered to resolve ID collision |

---

## Technique Count by Family

| Family | Prefix | Count | Code Range |
|--------|--------|-------|------------|
| Structural | ST | 11 | ST-01 to ST-49 |
| Reasoning | RT | 9 | RT-01 to RT-22 |
| Output Control | OC | 7 | OC-02 to OC-08 |
| Quality Assurance | QA | 14 | QA-01 to QA-15 |
| Context Management | CM | 10 | CM-01 to CM-10 |
| Role & Perspective | RP | 5 | RP-01 to RP-05 |
| Decomposition | DT | 6 | DT-01 to DT-06 |
| Educational | ED | 5 | ED-01 to ED-05 |
| Meta-Prompting | MP | 7 | MP-01 to MP-07 |
| Domain-Specific | DS | 27 | DS-01 to DS-148 |
| Agentic | AG | 21 | AG-01 to AG-31 |
| Non-Engineering | NE | 14 | NE-01 to NE-18 |
| Specialized Visual | SV | 9 | SV-01 to SV-10 |
| Done Definition | DD | 8 | DD-02 to DD-11 |
| Delegation & Productivity | DP | 24 | DP-01 to DP-24 |
| Quality Systems | QS | 6 | QS-01 to QS-06 |
| Multi-Agent Architecture | MA | 8 | MA-01 to MA-08 |
| Interaction Techniques | IT | 2 | IT-19, IT-35 |
| **TOTAL** | | **193** | |

---

## Notes

1. **Count discrepancy with audit document:** The audit plan states 169 techniques. This reference counts **193 active technique entries**. The difference comes from:
   - The audit may have been conducted before the 2026-01-31 additions (DP-19 through DP-24, QS-01 through QS-06, MA-01 through MA-08 = 20 techniques)
   - The IT (Interaction Techniques) family (IT-19, IT-35) adds 2 more
   - Some entries like ST-38/ST-39 and RT-15/RT-20/RT-22 are compound codes counting as single entries

2. **Compound codes:** Several techniques use compound code notation:
   - `ST-38/ST-39` — Production-Ready Architecture Patterns (counted as 1)
   - `RT-15/RT-20/RT-22` — Sequential Response Approach Pattern (counted as 1)
   - `DS-107` — merged from DS-107 + DS-31/AG-27

3. **Numbering gaps:** Large gaps exist in some families (e.g., DS jumps from DS-06 to DS-13, from DS-24 to DS-44, etc.). These are noted in the audit as issue M2.

4. **Phase 2 documentation pending:** Many techniques in the high-priority section have "Full documentation: [New technique - Phase 2]" notes, indicating their detailed entries are still pending.

5. **IT family not listed in naming conventions:** The IT (Interaction Techniques) prefix appears in the high-priority section but is not listed in the official ID Prefix Reference table at the top of the Master Index. This should be addressed.
