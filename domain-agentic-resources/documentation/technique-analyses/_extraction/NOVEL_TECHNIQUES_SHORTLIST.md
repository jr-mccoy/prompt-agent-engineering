# Novel Techniques Shortlist

**Step:** 0.3
**Date:** 2026-02-09
**Input:** `_extraction/MAPPED_TECHNIQUE_INVENTORY.md` (288 CONFIRMED-NOVEL techniques)
**Purpose:** Evaluate each novel technique for inclusion in MASTER_TECHNIQUE_INDEX.md

---

## Evaluation Criteria

Each of the 288 CONFIRMED-NOVEL techniques was evaluated against three questions:

1. **Truly novel?** Is it a distinct pattern, or just a variation/combination of existing techniques?
2. **General enough?** Is it reusable across 3+ domains, or hyper-specific to one tool/framework?
3. **Adoptable?** Does it represent a prompting pattern other resources could adopt?

**A technique qualifies as a prompting pattern (not just domain knowledge) when it describes HOW to structure instructions to an AI model** — not what domain-specific content to include.

### Verdict Definitions

| Verdict | Meaning | Destination |
|---------|---------|-------------|
| **ADD** | Genuinely novel, general, reusable. Add to MASTER_TECHNIQUE_INDEX.md | Step 0.4 |
| **MERGE_WITH_EXISTING** | Meaningful variant of an existing technique. Update the parent definition. | Step 0.4 (as update) |
| **SKIP** | Too specific to one tool/domain, or an implementation pattern rather than a prompting technique. | `DOMAIN_SPECIFIC_TECHNIQUES_ARCHIVE.md` |

---

## Summary

| Verdict | Count | % of 288 |
|---------|-------|----------|
| **ADD** | 48 | 16.7% |
| **MERGE_WITH_EXISTING** | 23 | 8.0% |
| **SKIP** | 217 | 75.3% |
| **Total** | 288 | 100% |

### Impact on Master Index

- Current master index: **193 active techniques**
- Techniques to ADD: **48**
- Existing techniques to UPDATE (MERGE): **23** (affecting ~17 distinct parent techniques)
- **New total after Step 0.4: ~241 techniques**

### Family Distribution of ADD Techniques

| Family | ADD Count | Current Count | New Total |
|--------|----------|---------------|-----------|
| DS (Domain-Specific) | 15 | 27 | 42 |
| IT (Interaction) | 8 | 2 | 10 |
| NE (Non-Engineering) | 6 | 14 | 20 |
| ST (Structural) | 6 | 11 | 17 |
| OC (Output Control) | 4 | 7 | 11 |
| RT (Reasoning) | 3 | 9 | 12 |
| AG (Agentic) | 3 | 21 | 24 |
| QA (Quality Assurance) | 2 | 14 | 16 |
| ED (Educational) | 1 | 5 | 6 |
| MP (Meta-Prompting) | 1 | 7 | 8 |
| **Total** | **48** (new) + **193** (existing) = **241** |

---

## ADD Techniques (48)

### Structural Family (ST) — 6 new techniques

#### ST-40: Three-Tier Value Classification
- **Description:** Categorize content into three tiers (Keep/Condense/Delete) with color coding or labeling to guide content management decisions.
- **Source:** B5 (Three-Tier Value Classification)
- **Pattern:** Define three categories with clear criteria, apply to each content element, produce a categorized inventory.
- **Why it's novel:** No existing technique addresses content triage. ST-22 (Multi-Solution Comparison) compares approaches; this categorizes existing content for retention decisions.
- **Reusability:** Documentation cleanup, code review (keep/refactor/delete), knowledge base curation, meeting agenda prioritization.

#### ST-42: Criticality Labeling
- **Description:** Use semantic bold prefixes (e.g., **CRITICAL:**, **WARNING:**, **INFO:**) to visually signal priority level inline within documentation or output.
- **Source:** B7b (ST-32 Criticality Labeling)
- **Pattern:** Define 3-5 severity labels with visual markers. Prepend to relevant items. Reader scans labels before content.
- **Why it's novel:** DS-06 (Prioritization and Severity) ranks findings into ordered lists. This is about inline labeling within flowing text, not sorting into ranked sections.
- **Reusability:** Any prompt that generates reports, documentation, code review feedback, configuration files, or operational runbooks.

#### ST-43: Risk-Stratified Documentation
- **Description:** Embed risk levels directly within documentation so that recommendations carry explicit risk context (e.g., "LOW RISK: ...", "HIGH RISK: requires downtime").
- **Source:** B7a (ST-33 Risk-Stratified Documentation)
- **Pattern:** Tag each recommendation/action with a risk level. Group or sort by risk. Provide mitigation steps for HIGH items.
- **Why it's novel:** Extends beyond ST-42 (inline labels) to a full documentation strategy where risk assessment is woven into every recommendation.
- **Reusability:** Infrastructure changes, security recommendations, migration guides, architectural decisions, deployment procedures.

#### ST-44: Progressive Complexity Scaffolding
- **Description:** Build artifacts progressively from minimal viable version to production-grade, with each layer adding complexity. The minimal version must work independently.
- **Source:** B9 (Progressive Complexity Scaffolding)
- **Pattern:** Define 3-4 complexity tiers (minimal → standard → production → enterprise). Each tier is a complete working version. Higher tiers add non-functional requirements.
- **Why it's novel:** ED-01 (Iterative Scaffolding) teaches concepts one at a time. This builds *artifacts* progressively. DS-80 (Multi-Tiered Template Library) provides templates at different levels; this is a process pattern, not a template collection.
- **Reusability:** Code generation, infrastructure templates, documentation, API design, configuration files, tutorial creation.

#### ST-45: Methodology-Centric Expertise
- **Description:** Define an agent or prompt's identity around a specific methodology (e.g., TDD, DDD, SRE, Lean) rather than a role title, making the methodology the organizing principle for all recommendations.
- **Source:** B2 (ST-36 Methodology-Centric Expertise)
- **Pattern:** Name the methodology. Define its core principles. Filter all recommendations through methodology lens. Reject approaches that violate methodology tenets.
- **Why it's novel:** RP-01 (Expert Role Assignment) assigns a role ("senior engineer"). This structures identity around a methodology, which produces more consistent and principled outputs.
- **Reusability:** Any agent/prompt where philosophical consistency matters: TDD coach, SRE advisor, Lean consultant, Agile facilitator, security-first architect.

#### ST-46: Assertion-Evidence Content Structure
- **Description:** Structure content using the Pyramid Principle: lead with the assertion (conclusion), then provide supporting evidence. Every section starts with its main point.
- **Source:** B9 (DS-33 Assertion-Evidence Content Structure)
- **Pattern:** State conclusion first → provide 2-4 supporting evidence points → optional detail expansion. Apply recursively to subsections.
- **Why it's novel:** ST-05 (Hierarchical Organization) defines structure but not content ordering. This mandates conclusion-first ordering, which is the inverse of most analytical approaches.
- **Reusability:** Executive summaries, presentation slides, code review feedback, architecture decision records, any business communication.

---

### Reasoning & Temporal Family (RT) — 3 new techniques

#### RT-09: Root Cause Explanation Pattern
- **Description:** Structure troubleshooting explanations as: Root Cause → Symptoms → Explanation → Fix. Work backward from cause to observable symptoms, then forward to resolution.
- **Source:** B8 (DS-66 Root Cause Explanation), B4 (DS-27)
- **Pattern:** 1) Identify root cause. 2) List observable symptoms. 3) Explain the causal chain (why root cause produces symptoms). 4) Provide fix targeting the root cause, not symptoms.
- **Why it's novel:** RT-02 (Multi-Dimensional Analysis) analyzes from multiple perspectives. This is specifically about causal chain reasoning for troubleshooting, working backward from cause.
- **Reusability:** Debugging, incident postmortems, performance analysis, infrastructure troubleshooting, medical diagnosis prompts, any diagnostic task.

#### RT-10: Troubleshooting Decision Tree
- **Description:** Organize troubleshooting as a decision tree: Symptom → Diagnostic Command → Possible Cause → Fix, with branching paths based on diagnostic results.
- **Source:** B9 (Troubleshooting Decision Tree)
- **Pattern:** Start with observable symptom. Provide diagnostic command/check. Branch: "If X, then Cause A → Fix A. If Y, then Cause B → Fix B." Continue until all branches resolve.
- **Why it's novel:** DT-06 (Typography Decision Tree) uses binary decisions for classification. This applies decision trees specifically to troubleshooting with executable diagnostic steps at each branch point.
- **Reusability:** Infrastructure debugging, application troubleshooting, customer support scripts, medical triage, hardware diagnostics.

#### RT-11: Error Recovery Patterns for Prompts
- **Description:** Define explicit recovery strategies for when LLM outputs fail: retry with rephrased instruction, fallback to simpler request, escalate to human, or gracefully degrade output.
- **Source:** B6 (RT-12 Error Recovery Patterns for Prompts)
- **Pattern:** Define expected output. Define 2-3 failure modes. For each failure mode, specify: detection criteria → recovery action → fallback output.
- **Why it's novel:** QA-13 (Failure Recovery Specification) handles agent/system failures. This specifically addresses LLM output failures within prompting workflows — when the model doesn't follow instructions correctly.
- **Reusability:** Any multi-step prompt chain, evaluation pipelines, automated content generation, chatbot fallbacks, agentic workflows.

---

### Output Control Family (OC) — 4 new techniques

#### OC-09: Capability Boundary Specification
- **Description:** Explicitly define "Can Do" vs "Cannot Do" matrices that delineate what a prompt/agent/skill is designed to handle and what falls outside its scope.
- **Source:** B5 (OT-10 Capability Boundary Specification)
- **Pattern:** Create two-column table: "This [agent/prompt] CAN: ..." and "This [agent/prompt] CANNOT: ...". Be specific on both sides.
- **Why it's novel:** CM-03 (Scope Definition) defines analysis boundaries. This defines capability boundaries — what the tool itself can and cannot do, managing user expectations upfront.
- **Reusability:** Any agent definition, skill documentation, API documentation, product documentation, chatbot design.

#### OC-10: Mandatory Disclaimer Pattern
- **Description:** Embed required disclaimers (legal, safety, scope limitations) as structural elements that cannot be omitted from output, regardless of context.
- **Source:** B3 (OT-16 Mandatory Disclaimer Pattern)
- **Pattern:** Define disclaimer text. Specify placement (header, footer, inline). Mark as non-removable. Optionally adapt wording to context while preserving core message.
- **Why it's novel:** QA-04 (Uncertainty Acknowledgment) states confidence levels. This is about mandatory boilerplate disclaimers that must always appear — a structural requirement, not a reasoning step.
- **Reusability:** Healthcare prompts, legal advice, financial guidance, safety-critical instructions, any regulated domain.

#### OC-11: Grouped Reporting by Pattern Type
- **Description:** Organize findings/results by pattern category rather than by location or severity, enabling readers to see systemic issues across a codebase or dataset.
- **Source:** B7a (OT-11 Grouped Reporting by Pattern Type)
- **Pattern:** Identify finding categories (e.g., "Authentication Issues", "Input Validation", "Error Handling"). Group all findings under their category. Add per-category summary.
- **Why it's novel:** DS-06 (Prioritization and Severity) sorts by severity. This groups by pattern type — enabling identification of systemic issues rather than individual findings.
- **Reusability:** Security audits, code reviews, accessibility audits, compliance reports, data quality assessments, any analytical report.

#### OC-12: External Reference Catalog
- **Description:** Include a curated catalog of authoritative external references (official docs, RFCs, standards) as a structured section within the prompt output.
- **Source:** B3 (OT-18 External Reference Catalog)
- **Pattern:** For each reference: [Name] | [URL/Citation] | [What it covers] | [When to consult it]. Organize by topic area.
- **Why it's novel:** QA-05 (Citation Requirements) requires sources for claims. This is a proactive, curated reference section — a knowledge directory, not inline citations.
- **Reusability:** Technical documentation, learning resources, compliance guides, research outputs, any domain with authoritative standards.

---

### Quality Assurance Family (QA) — 2 new techniques

#### QA-16: Quality Rubric with Auto-Iteration
- **Description:** Define a numerical scoring rubric (e.g., 1-10 across multiple dimensions), score the output, and automatically iterate if the score falls below a threshold.
- **Source:** B9 (Quality Rubric with Auto-Iteration)
- **Pattern:** 1) Define 3-5 scoring dimensions with criteria for each score level. 2) Score output on each dimension. 3) If any dimension < threshold OR total < threshold, revise and re-score. 4) Max N iterations.
- **Why it's novel:** DT-03 (Iterative Refinement) refines through multiple passes. DS-02 (Metric Specification) defines metrics. This combines both into a self-scoring auto-iteration loop — the output grades itself and autonomously improves.
- **Reusability:** Content generation, code generation, documentation, any prompt where output quality is measurable and improvable.

#### QA-17: Named Scores for Multi-Dimensional Metrics
- **Description:** Alongside a binary pass/fail verdict, provide named sub-scores (e.g., "Accuracy: 8/10, Completeness: 6/10, Clarity: 9/10") that decompose quality into independently measurable dimensions.
- **Source:** B6 (QA-27 Named Scores Multi-Dimensional)
- **Pattern:** Define 3-7 named dimensions. Score each independently. Provide overall pass/fail based on dimension thresholds. Highlight lowest-scoring dimension for improvement.
- **Why it's novel:** QA-11 (Pass/Fail Test Harness) is binary. DS-02 (Metric Specification) defines what to measure. This provides the multi-dimensional scoring structure itself.
- **Reusability:** LLM evaluation, code review scoring, content quality assessment, rubric-based grading, any evaluation framework.

---

### Non-Engineering Family (NE) — 6 new techniques

#### NE-14: Multi-Audience Documentation Targeting
- **Description:** Generate documentation from a single source that targets multiple audiences (e.g., executives, developers, operators) with different levels of detail and different emphasis.
- **Source:** B3 (NE-15 Multi-Audience Documentation Targeting)
- **Pattern:** Define 2-4 audience profiles with their needs. Generate a single comprehensive document with audience-tagged sections, OR generate multiple versions from one analysis.
- **Why it's novel:** RP-02 (Audience-Specific Framing) tailors one output to one audience. This explicitly generates for multiple audiences simultaneously or sequentially from the same source material.
- **Reusability:** Technical documentation, incident reports, project updates, research papers, product announcements, training materials.

#### NE-15: Data Storytelling Framework
- **Description:** Structure analytical output as a narrative: setup (context) → tension (problem/finding) → resolution (recommendation), with data as supporting evidence rather than raw output.
- **Source:** B3 (NE-16 Data Storytelling Framework)
- **Pattern:** 1) Set the scene (what we're looking at and why). 2) Present the finding as tension/surprise. 3) Support with specific data points. 4) Resolve with actionable recommendation.
- **Why it's novel:** DS-05 (Visualization and Communication Guidance) addresses how to present data visually. This addresses the narrative structure around data — turning analysis into a story.
- **Reusability:** Business reports, data analysis summaries, dashboard commentary, research findings, quarterly reviews, any data-heavy output.

#### NE-16: Non-Judgmental Comparison
- **Description:** Frame comparisons as "Current approach vs. Recommended approach" or "Normal vs. Better" rather than "Wrong vs. Right", preserving dignity while still guiding toward improvement.
- **Source:** B6 (DS-74 Non-Judgmental Comparison)
- **Pattern:** Never label existing practice as "wrong" or "bad." Use "current" / "common" / "typical" vs. "recommended" / "optimized" / "enhanced." Acknowledge valid reasons for current approach before suggesting improvements.
- **Why it's novel:** NE-04 (Good vs Bad Example Calibration) explicitly uses "bad → good" contrast for calibration. This is about tone and framing in the output — avoiding judgment while still conveying improvement direction.
- **Reusability:** Code reviews, performance feedback, educational content, process improvement, any context where the recipient may feel criticized.

#### NE-17: Call-to-Action Mandatory Close
- **Description:** Require every output section or complete response to end with a specific, actionable next step the reader can take immediately.
- **Source:** B6 (Call-to-Action Mandatory Close)
- **Pattern:** Final element of every section/response must be "Next Step: [specific action]" or "Action Required: [concrete task with timeline]." Generic advice ("consider reviewing...") is not acceptable.
- **Why it's novel:** No existing technique mandates actionable closings. OC-06 (Output Contract Structure) defines output format but doesn't require action items.
- **Reusability:** Consulting recommendations, code review feedback, audit findings, coaching sessions, status reports, any advisory output.

#### NE-19: Documentation-as-Product Philosophy
- **Description:** Treat documentation as a product with users, requirements, quality standards, and iteration cycles — not as an afterthought to code or decisions.
- **Source:** B3/B4 (NE-19 Documentation-as-Product Philosophy)
- **Pattern:** Define documentation users. Define their jobs-to-be-done. Set quality metrics (findability, accuracy, completeness). Iterate based on user feedback.
- **Why it's novel:** No existing technique frames documentation with product management thinking. DS-111 (External Methodology Compliance) enforces standards but doesn't apply product thinking.
- **Reusability:** Technical writing, API documentation, knowledge bases, onboarding materials, any documentation-heavy output.

#### NE-20: Third-Party Handoff Package
- **Description:** Generate a self-contained documentation package that allows a third party (vendor, new team member, auditor) to understand and act without requiring additional context or access.
- **Source:** B7a (NE-14 Third-Party Handoff Package)
- **Pattern:** Include: 1) Context summary (what and why). 2) Current state (what exists). 3) Requirements (what's needed). 4) Constraints (what can't change). 5) Success criteria (how to verify). All in one document.
- **Why it's novel:** No existing technique addresses the handoff problem — creating documentation for someone who has zero existing context.
- **Reusability:** Vendor onboarding, team transitions, audit preparation, consultant briefings, open-source project documentation, any cross-boundary communication.

---

### Domain-Specific Family (DS) — 15 new techniques

#### DS-25: Chart Selection Dictionary
- **Description:** Provide a mapping from question types to appropriate visualization types (e.g., "comparison over time → line chart", "part-to-whole → pie/treemap", "distribution → histogram").
- **Source:** B9 (DS-34 Chart Selection Dictionary)
- **Pattern:** Define 5-8 common question types. Map each to 1-2 recommended chart types. Include anti-patterns ("don't use pie charts for >7 categories").
- **Why it's novel:** DS-05 (Visualization and Communication Guidance) says to present findings visually. This provides the specific decision logic for choosing which visualization.
- **Reusability:** Data analysis, dashboard design, presentation creation, reporting, any prompt that generates or recommends visualizations.

#### DS-26: Safe Defaults Pattern
- **Description:** Ensure every configurable parameter, option, or input has a documented safe default value that produces reasonable results without user customization.
- **Source:** B9 (Safe Defaults Pattern)
- **Pattern:** For each parameter: [Name] | [Default Value] | [Why this default] | [When to change it]. Defaults must be conservative/safe, never aggressive.
- **Why it's novel:** No existing technique addresses default value design. CM-02 (Constraint Specification) defines constraints but not defaults.
- **Reusability:** Configuration generation, API design, tool creation, template design, any prompt that produces configurable output.

#### DS-27: Professional Defaults Library
- **Description:** Provide pre-configured default settings organized by professional use case (e.g., "startup MVP defaults", "enterprise production defaults", "learning/experimentation defaults").
- **Source:** B6 (DS-40 Professional Defaults Library)
- **Pattern:** Define 3-5 use case profiles. For each profile, provide a complete configuration set. Explain what differs between profiles and why.
- **Why it's novel:** Extends DS-26 (Safe Defaults) from individual parameters to curated configuration bundles per use case. DS-80 (Multi-Tiered Template Library) provides templates; this provides configuration sets.
- **Reusability:** Tool configuration, infrastructure provisioning, project scaffolding, development environment setup, any multi-configuration output.

#### DS-28: Environment-Specific Guidance
- **Description:** Provide different recommendations based on the target environment's risk tolerance (e.g., development → permissive, staging → moderate, production → strict).
- **Source:** B8 (DS-60 Environment-Specific Guidance)
- **Pattern:** Define 2-4 environment tiers with their risk profiles. Provide tier-specific recommendations. Flag items that differ across tiers.
- **Why it's novel:** No existing technique addresses environment-aware output. DS-06 (Prioritization and Severity) ranks findings but doesn't adapt recommendations to environment.
- **Reusability:** Security recommendations, configuration guidance, deployment procedures, testing strategies, monitoring setup.

#### DS-29: Domain Pattern Library
- **Description:** Include a curated collection of named, reusable patterns specific to the domain, each with working code/examples and "when to use" guidance.
- **Source:** B5 (DS-41 Domain Pattern Library)
- **Pattern:** For each pattern: [Name] | [Problem it solves] | [When to use] | [When NOT to use] | [Working example] | [Common mistakes].
- **Why it's novel:** DS-80 (Multi-Tiered Template Library) provides templates at different complexity levels. This organizes patterns by the problem they solve, with explicit selection guidance.
- **Reusability:** API design, architecture patterns, testing patterns, UI patterns, data modeling patterns, any domain with recurring design decisions.

#### DS-30: Ecosystem Mapping
- **Description:** Map capabilities to specific tools/technologies in the ecosystem, providing a structured inventory of what tools exist for each need.
- **Source:** B2 (DS-106 Ecosystem Mapping)
- **Pattern:** Define capability categories. For each: [Capability] | [Recommended Tool] | [Alternatives] | [Selection Criteria]. Keep current with version/date.
- **Why it's novel:** DS-03 (Tool and Methodology Suggestions) recommends tools. This creates a structured map of the entire ecosystem, not point recommendations.
- **Reusability:** Technology selection, vendor evaluation, migration planning, team onboarding, any prompt that helps users navigate tool landscapes.

#### DS-32: Regulatory Enumeration Pattern
- **Description:** Provide a comprehensive listing of applicable regulations, standards, and compliance requirements for a given domain or jurisdiction.
- **Source:** B3 (DS-130 Regulatory Enumeration Pattern)
- **Pattern:** For each regulation: [Name/Code] | [Jurisdiction] | [What it covers] | [Key requirements] | [Penalties for non-compliance]. Group by category.
- **Why it's novel:** DS-111 (External Methodology Compliance) enforces adherence to one standard. This enumerates all applicable standards for awareness and planning.
- **Reusability:** Compliance planning, legal analysis, healthcare systems, financial services, any regulated domain.

#### DS-33: Jurisdiction-Adaptive Output
- **Description:** Adapt output (recommendations, requirements, examples) based on the target jurisdiction, automatically applying jurisdiction-specific rules and conventions.
- **Source:** B3 (DS-131 Jurisdiction-Adaptive Output)
- **Pattern:** Identify target jurisdiction. Apply jurisdiction-specific rules to all recommendations. Flag items that vary by jurisdiction. Provide multi-jurisdiction comparison when relevant.
- **Why it's novel:** No existing technique addresses jurisdiction-sensitive output. DS-22 (EARS Requirements) handles precision but not jurisdictional variation.
- **Reusability:** Legal advice, tax guidance, compliance recommendations, business formation, privacy policies, any cross-border or multi-state output.

#### DS-34: Documentation-Driven Testing
- **Description:** Generate test cases directly from documentation specifications, ensuring documentation and tests stay synchronized and documentation is testable.
- **Source:** B3/B4 (DS-145 Documentation-Driven Testing)
- **Pattern:** 1) Extract assertions from documentation. 2) Convert each assertion to a test case. 3) Flag documentation claims that are untestable. 4) Report coverage: % of docs with corresponding tests.
- **Why it's novel:** QA-10 (Test Battery Protocol) defines testing checklists. This derives tests from documentation, creating a feedback loop between docs and code.
- **Reusability:** API documentation, specification documents, requirement documents, user stories, any documentation that makes testable claims.

#### DS-35: LLM-as-Judge with Rubric
- **Description:** Use one LLM to evaluate the output of another LLM against a defined rubric, producing structured quality scores and improvement recommendations.
- **Source:** B6 (DS-111 LLM-as-Judge with Rubric)
- **Pattern:** Define rubric dimensions with scoring criteria. Present output to evaluator LLM with rubric. Collect dimension scores + justifications. Optionally feed scores back for iteration.
- **Why it's novel:** QA-01 (Self-Verification) is self-critique. QA-06 (Constitutional AI) uses principles. This uses a separate LLM as an independent evaluator with a structured rubric — a specific evaluation architecture.
- **Reusability:** Prompt evaluation pipelines, content quality assessment, automated grading, any LLM-in-the-loop evaluation system.

#### DS-36: Blocker Escalation Framework
- **Description:** Provide a structured format for reporting blockers with severity, impact, and escalation path, preventing blockers from being buried in status updates.
- **Source:** B1 (Blocker Escalation Framework)
- **Pattern:** For each blocker: [Description] | [Severity: P0-P3] | [Blocked work items] | [Days blocked] | [Owner] | [Escalation path if unresolved by date].
- **Why it's novel:** DD-11 (BLOCKED Protocol) handles individual blocked gates. This is a broader framework for surfacing and escalating all blockers in a project context.
- **Reusability:** Sprint retrospectives, standup reports, project status updates, incident management, any workflow with dependencies.

#### DS-37: Progressive Abstraction Transformation
- **Description:** Transform content through multiple abstraction levels (e.g., raw data → summary → executive brief → tweet-length), each level being a complete and accurate representation at that detail level.
- **Source:** B3 (DS-112 Progressive Abstraction Transformation)
- **Pattern:** Define 3-5 abstraction levels with target length and audience. Transform content for each level. Ensure accuracy is preserved at every level (no misleading simplification).
- **Why it's novel:** NE-05 (Token Budget Control) controls output length. This transforms the same content across multiple abstraction levels, each independently useful.
- **Reusability:** Report generation, briefing documents, content marketing, knowledge base articles, any content that serves multiple audiences at different detail levels.

#### DS-38: Long-Form Documentation Process
- **Description:** Define a multi-phase process for generating comprehensive documentation: outline → draft → review → refine → finalize, with quality gates between phases.
- **Source:** B3/B4 (DS-147 Long-Form Documentation Process)
- **Pattern:** Phase 1: Generate outline with section headers. Phase 2: Draft each section. Phase 3: Self-review for completeness and accuracy. Phase 4: Refine based on review. Phase 5: Add cross-references and index.
- **Why it's novel:** NE-02 (Phased Workflow Architecture) defines generic phases. This specializes the phased approach for long-form documentation with documentation-specific quality gates.
- **Reusability:** Technical documentation, research papers, book chapters, comprehensive guides, any long-form content generation.

#### DS-39: Configuration-Driven Workflow Customization
- **Description:** Define explicit configuration options that modify workflow behavior, allowing users to customize prompt execution without rewriting the prompt.
- **Source:** B1 (Configuration-Driven Workflow Customization)
- **Pattern:** Define configuration block with named options and defaults. Reference options throughout the workflow: "If [option] is enabled, then [behavior]." Document all options upfront.
- **Why it's novel:** OC-08 (Multi-Mode Prompt Architecture) switches between modes. This provides fine-grained configuration within a single mode — more like feature flags than mode switching.
- **Reusability:** Any reusable prompt, skill, or agent that needs user customization: code generators, analysis tools, documentation generators, review workflows.

#### DS-40: Follow-Up Action Extraction
- **Description:** As a standard processing step, extract all actionable items from input or generated content, formatting them as a structured action list with owners and deadlines.
- **Source:** B1 (Follow-Up Action Extraction)
- **Pattern:** Scan content for action-triggering language (decisions made, commitments, todos). For each: [Action] | [Owner] | [Deadline] | [Source context]. Deduplicate and prioritize.
- **Why it's novel:** No existing technique addresses systematic action extraction. DD-07 (Self-Audit Table) tracks completion evidence; this extracts future actions from unstructured content.
- **Reusability:** Meeting notes processing, email summarization, document review, project planning, any input that contains implicit action items.

---

### Interaction Techniques Family (IT) — 8 new techniques

#### IT-20: Progressive Example Complexity
- **Description:** Organize examples in a progression from simple to advanced, where each example builds on the previous one by adding one new concept or complexity dimension.
- **Source:** B6 (IT-34 Progressive Example Complexity)
- **Pattern:** Example 1: Minimal viable (1-2 features). Example 2: Add one complexity (error handling, edge case). Example 3: Production-grade (full feature set). Each example is self-contained and runnable.
- **Why it's novel:** ED-02 (Progressive Exercise Generation) creates exercises matched to skill level. ED-05 (Reference Class Priming) shows one excellent example. This is a documentation structure pattern — multiple examples arranged by complexity.
- **Reusability:** API documentation, library documentation, tutorial creation, configuration examples, any reference material with examples.

#### IT-21: Use Case-Driven Documentation
- **Description:** Organize documentation around user scenarios ("I want to...") rather than feature lists or API endpoints, making it task-oriented.
- **Source:** B6 (IT-37 Use Case-Driven Documentation)
- **Pattern:** Define 5-10 common user scenarios. For each: "I want to [goal]" → step-by-step instructions → expected result → troubleshooting. Cross-reference related scenarios.
- **Why it's novel:** ST-02 (Structured Sequential Instructions) provides step-by-step within a single task. This organizes an entire documentation set around user goals.
- **Reusability:** Product documentation, API guides, tool documentation, onboarding guides, FAQ sections, any user-facing reference material.

#### IT-22: Workflow Decision Matrix
- **Description:** Provide a structured matrix that maps user scenarios/conditions to recommended workflows, helping users select the right approach without reading all options.
- **Source:** B6 (IT-22 Workflow Decision Matrix)
- **Pattern:** Rows = user scenarios. Columns = relevant factors. Cells = recommended workflow/approach. Include "If unsure, start here" default path.
- **Why it's novel:** DT-06 (Typography Decision Tree) uses binary decisions. ST-22 (Multi-Solution Comparison Matrix) compares solutions. This maps scenarios to workflows — a routing table, not a comparison.
- **Reusability:** Tool documentation, process guides, incident response, customer support, any context with multiple valid approaches.

#### IT-23: Symptom-Based Troubleshooting Organization
- **Description:** Organize troubleshooting content by observable symptom (what the user sees) rather than by root cause (what's actually wrong), since users know symptoms but not causes.
- **Source:** B8 (IT-32 Symptom-Based Troubleshooting)
- **Pattern:** Index by symptom: "Error message X" → possible causes → diagnostic steps → fixes. Cross-reference symptoms that share causes.
- **Why it's novel:** RT-09 (Root Cause Explanation) works backward from cause. This works forward from symptom — the user's entry point. They're complementary: this finds the cause, RT-09 explains it.
- **Reusability:** Technical support documentation, debugging guides, medical symptom checkers, hardware troubleshooting, any diagnostic context.

#### IT-24: Template-Based Educational Scaffolding
- **Description:** Use TODO markers and contextual inline comments within templates to guide users on what to customize, turning templates into self-teaching tools.
- **Source:** B8 (IT-4 Template-Based Educational Scaffolding)
- **Pattern:** Place `TODO:` markers at customization points. Add inline comments explaining what goes there, why, and common options. Include a working default that users can learn from before customizing.
- **Why it's novel:** ED-01 (Iterative Scaffolding) teaches concepts interactively. AG-05 (Concrete Deliverable Templates) provides working examples. This makes templates themselves educational through inline guidance.
- **Reusability:** Code templates, configuration templates, document templates, project scaffolding, any generated template that users need to customize.

#### IT-25: Tool Hierarchy Guidance
- **Description:** Explicitly define a preference hierarchy for tools/approaches: "Prefer A. If A isn't available, use B. If B fails, fall back to C." Prevents analysis paralysis when multiple options exist.
- **Source:** B9 (IT-31 Tool Hierarchy Guidance)
- **Pattern:** Rank tools/approaches in explicit preference order. For each: [When to use] | [When to skip to next] | [Tradeoffs vs. preferred]. Provide a clear "start here" default.
- **Why it's novel:** DS-03 (Tool and Methodology Suggestions) recommends tools. This establishes an explicit preference ordering with fallback logic — a decision hierarchy, not just suggestions.
- **Reusability:** DevOps tooling guides, debugging approaches, data processing pipelines, learning resources, any context with multiple valid tools.

#### IT-26: Reference Catalog Pattern
- **Description:** Provide a categorized, searchable catalog of resources (patterns, tools, references) organized by category with brief descriptions, enabling quick lookup.
- **Source:** B7b (IT-29 Reference Catalog Pattern)
- **Pattern:** Organize entries by category. For each: [Name] | [Category] | [Brief Description] | [When to use]. Enable scanning by category or keyword.
- **Why it's novel:** OC-12 (External Reference Catalog) catalogs external references. This is a general organizational pattern for any collection of resources — internal or external.
- **Reusability:** Pattern catalogs, tool inventories, technique indexes, API endpoint directories, glossaries, any reference collection.

#### IT-27: Multi-Template Selection Guide
- **Description:** When providing multiple templates, include explicit selection criteria: "Use Template A when [condition]. Use Template B when [condition]." Prevent users from choosing randomly.
- **Source:** B9 (Multi-Template Selection Guide)
- **Pattern:** List available templates. For each: [Name] | [Best for] | [Not for] | [Complexity level]. Optionally include a decision flowchart.
- **Why it's novel:** DS-80 (Multi-Tiered Template Library) provides templates at different levels. This adds the selection logic — helping users choose the right template.
- **Reusability:** Any prompt that generates multiple variants, configuration templates, project scaffolding, documentation templates, email templates.

---

### Agentic Family (AG) — 3 new techniques

#### AG-19: Time-Critical Response Protocol
- **Description:** Define time-boxed crisis action protocols with specific actions per time window (e.g., "First 15 minutes: ...", "First hour: ...", "First day: ...").
- **Source:** B3/B4 (AG-33 Time-Critical Response Protocol)
- **Pattern:** Define time windows (immediate/short/medium/long). For each window: [Actions to take] | [Decisions to make] | [Information to gather] | [Escalation criteria].
- **Why it's novel:** No existing technique addresses time-pressure scenarios. NE-02 (Phased Workflow) defines phases but not time-boxed crisis phases.
- **Reusability:** Incident response, security breach protocols, production outage runbooks, crisis communication, any time-sensitive operational procedure.

#### AG-20: Meta-Skill Pattern (Discovery)
- **Description:** Define a skill/capability whose primary purpose is to discover and invoke other skills, acting as a router or search layer across available capabilities.
- **Source:** B5 (AG-24 Meta-Skill Pattern)
- **Pattern:** 1) Accept user intent description. 2) Search available skills/resources by keyword/capability. 3) Rank matches by relevance. 4) Present top matches with descriptions. 5) Optionally invoke selected skill.
- **Why it's novel:** AG-18 (Meta-Skill Self-Reference) teaches skill creation. This is about skill discovery — a fundamentally different meta-capability.
- **Reusability:** Any multi-skill agent system, plugin architectures, capability registries, tool selection in agentic workflows.

#### AG-21: Orchestration with Dual-Path Output
- **Description:** Generate output through two independent paths (e.g., different approaches, different models, different prompts) and present both for comparison or merge the best elements.
- **Source:** B9 (AG-22 Orchestration with Dual-Path)
- **Pattern:** Define two generation paths with different strategies. Execute both independently. Present side-by-side comparison. Optionally: auto-select best elements from each.
- **Why it's novel:** AG-13 (Parallel-Converge Orchestration) runs agents in parallel and converges. This specifically uses dual paths for quality through comparison — a verification technique, not just parallelism.
- **Reusability:** Content generation, code review (two reviewers), decision support (two frameworks), any context where independent perspectives improve quality.

---

### Educational Family (ED) — 1 new technique

#### ED-06: Example Quantity Specification
- **Description:** Explicitly mandate a minimum number of examples (e.g., "Provide at least 3 examples for each concept") to prevent under-specification and ensure sufficient illustration.
- **Source:** B6 (DS-76 Example Quantity Specification)
- **Pattern:** State: "For each [concept/rule/pattern], provide at minimum [N] examples showing [variation criteria]." Specify what should vary between examples.
- **Why it's novel:** ED-05 (Reference Class Priming) shows one excellent example. This ensures quantity of examples, which is distinct from quality of a single example.
- **Reusability:** Documentation, tutorials, API references, style guides, coding standards, any context where examples prevent misunderstanding.

---

### Meta-Prompting Family (MP) — 1 new technique

#### MP-08: Four-Layer Enhancement Process
- **Description:** Optimize prompts through four systematic layers: 1) Structure improvement, 2) Clarity refinement, 3) Technique injection, 4) Edge case hardening. Apply layers sequentially.
- **Source:** B7b (Four-Layer Enhancement Process)
- **Pattern:** Layer 1: Fix structural issues (ordering, grouping, formatting). Layer 2: Clarify ambiguous language. Layer 3: Add appropriate techniques (CoT, examples, etc.). Layer 4: Add edge case handling and failure modes.
- **Why it's novel:** MP-02 (Recursive Optimization) iteratively improves prompts but doesn't specify what to improve at each iteration. This provides a structured improvement framework with specific focus areas per layer.
- **Reusability:** Prompt improvement, prompt review, prompt engineering training, any meta-prompting workflow.

---

## MERGE_WITH_EXISTING Techniques (23)

These techniques are meaningful variants of existing master index techniques. In Step 0.4, the parent technique's definition should be updated to note the variant.

| # | Technique Name | Source | Merge Into | Rationale |
|---|---------------|--------|-----------|-----------|
| 1 | Critical Warnings Table | B8 (DS-62) | **DS-06** (Prioritization and Severity) | Variant: Surface catastrophic issues upfront in a dedicated warnings table before the main findings. Adds "upfront critical section" to severity guidance. |
| 2 | Anti-Pattern Table with Solutions | B5 | **AG-09** (Anti-Pattern & Failure Mode Embedding) | Variant: Structured Problem/Solution table format for anti-patterns. Adds tabular format option to AG-09's pattern. |
| 3 | Evidence-Based Investigation Methodology | B9 | **RT-05** (Evidence-Based Reasoning) | Extension: Adds systematic investigation methodology (hypothesis → evidence → conclusion) to evidence requirements. |
| 4 | Production Readiness Checklist Pattern | B9 | **QA-10** (Test Battery Protocol) | Variant: Embeds multiple area-specific checklists (security, performance, reliability) into a single production readiness gate. |
| 5 | Contrastive Role Disambiguation | B3 (AG-31) | **AG-31** (Workflow Position Definition) | Extension: Adds "Use Agent X when [condition], use Agent Y when [condition]" contrastive format to position definitions. |
| 6 | Explicit Agent Handoff Protocol | B9 | **AG-07** (Pipeline Orchestration Patterns) | Extension: Adds failure-triggered handoff protocol — when agent A fails, agent B takes over with full context transfer. |
| 7 | Fallback Strategy Pattern | B7b | **QA-13** (Failure Recovery Specification) | Extension: Adds progressive generality chain — each fallback is broader/simpler than the previous attempt. |
| 8 | Multi-Stage Validation Pipeline | B7a | **QA-08** (Gate-Based Verification) | Extension: Adds progressive validation stages (syntax → semantic → integration → acceptance) to gate-based verification. |
| 9 | Pre-Implementation Checklist | B5 | **QA-08** (Gate-Based Verification) | Variant: Verification gate specifically before implementation begins — a "readiness" gate rather than a "completion" gate. |
| 10 | Mandatory Preservation Checklist | B5 (QA-24) | **QA-01** (Self-Verification) | Variant: Category-specific preservation verification — ensure nothing was accidentally removed or degraded during processing. |
| 11 | Success/Failure Counters | B6 (QA-26) | **DS-02** (Metric Specification) | Extension: Batch operation accounting metrics — processed/succeeded/failed/skipped counts as standard output for batch operations. |
| 12 | Multi-Stage Relevance Scoring | B1 | **CM-06** (Semantic Vector-Based Context Management) | Extension: Composite scoring across semantic, temporal, and historical dimensions for context retrieval. |
| 13 | Adaptive Context Expansion | B1 | **CM-07** (Token-Budget-Aware Progressive Loading) | Extension: Runtime discovery of additional context needs — dynamically expand context when initial loading proves insufficient. |
| 14 | Context Fingerprinting | B1 | **CM-10** (Memory Scaffold Architecture) | Extension: Version identifiers with drift detection — detect when persisted context has become stale. |
| 15 | Symptom-Diagnostic-Fix Pattern | B9 | **RT-09** (Root Cause Explanation — NEW ADD) | Merge: Nearly identical to RT-09 but approaches from symptom-first. Consolidate both perspectives into RT-09's definition. |
| 16 | Sequential Evidence Gathering | B9 | **RT-05** (Evidence-Based Reasoning) | Extension: Prioritized investigation sequences — gather evidence in order of diagnostic value, not alphabetically. |
| 17 | School-Based Approach Documentation | B2 (DS-110) | **ST-22** (Multi-Solution Comparison Matrix) | Variant: Compare competing schools of thought (not just solutions) with philosophical pros/cons. |
| 18 | Feature-to-Principle Bridging | B6 (DS-75) | **NE-13** (Technical-to-Business Translation) | Variant: Link specific features to engineering principles, not just business value. Broadens the "translation" concept. |
| 19 | Content Classification Matrix | B5 (DS-36) | **DT-05** (Element-by-Element Assessment Matrix) | Variant: Multi-dimensional content evaluation matrix. Specializes DT-05 for content classification. |
| 20 | Atomic Requirement Decomposition | B7b (DS-101) | **DT-01** (Hierarchical Task Breakdown) | Variant: Break compound requirements into atomic, independently testable units. Adds atomicity criterion to decomposition. |
| 21 | Real-World Example Section | B6 (IT-40) | **AG-05** (Concrete Deliverable Templates) | Extension: Dedicated end-to-end production example section showing the deliverable in real-world use. |
| 22 | Best Practices by Workflow Stage | B6 (IT-42) | **IT-20** (Progressive Example Complexity — NEW ADD) | Merge: Organize practices by workflow stage (planning → implementation → testing → deployment). Subsumed by progressive complexity. |
| 23 | Complete Usage Example Section | B6 (IT-43) | **AG-05** (Concrete Deliverable Templates) | Extension: Step-by-step usage demonstrations showing how to use generated output. Extends deliverable templates with usage guidance. |

---

## SKIP Techniques (217)

All 217 SKIP techniques are preserved in `DOMAIN_SPECIFIC_TECHNIQUES_ARCHIVE.md` — a separate file in this directory. They are organized by domain for future mining and prompt development.

**SKIP breakdown by domain:**

| Domain Category | Count | Key Themes |
|----------------|-------|------------|
| Security & Access Control | 16 | Allowlist strategies, RBAC, credential detection, security encoding |
| Infrastructure & Cloud | 25 | Terraform, Kubernetes, multi-cloud, IaC, caching patterns |
| Data Engineering & Observability | 9 | DAG design, data lineage, SLO/error budgets, MVCC |
| API & Development Patterns | 11 | HTTP semantics, pagination, authentication, file operations |
| Tool-Specific Implementation | 38 | CLI tools, bash scripting, JSON processing, path handling |
| Mobile & Platform | 8 | iOS, Android, Flutter, SwiftUI, platform-specific patterns |
| Testing Patterns | 12 | Test pyramids, TDD metrics, self-healing tests, CI/CD |
| LLM Evaluation Tooling | 7 | Promptfoo-specific, Python assertions, echo providers |
| Context Management Implementation | 5 | Knowledge graphs, multi-modal context, cross-project transfer |
| Documentation Implementation | 8 | SDK generation, docs-as-code pipeline, font chains |
| Compliance & Finance | 8 | Control types, backtesting, walk-forward analysis, blockchain |
| Agent Architecture | 14 | Multi-category deployment, standard library preference, governance |
| Networking & Diagnostics | 6 | OSI-layer diagnostics, vantage testing, zero-trust, service mesh |
| Content Processing | 8 | Format detection, extraction patterns, metadata preservation |
| Workflow Automation | 6 | DAG factories, timing algorithms, error suppression |
| Cultural/Organizational | 4 | Blameless culture, team collaboration, continuous guidance |
| Miscellaneous | 32 | Various hyper-specific patterns |

---

## Code Assignment Summary

### Codes Filling Existing Gaps

Many recommended codes fill gaps in existing family sequences:

| Family | Gap Codes Used | Remaining Gaps |
|--------|---------------|----------------|
| ST | ST-40, ST-42, ST-43, ST-44, ST-45, ST-46 | ST-06 to ST-15, ST-17 to ST-21, ST-23 to ST-34, ST-36, ST-41, ST-47, ST-48 |
| RT | RT-09, RT-10, RT-11 | RT-12 to RT-14 |
| OC | OC-09, OC-10, OC-11, OC-12 | (none — fills to OC-12) |
| QA | QA-16, QA-17 | (none — extends past QA-15) |
| NE | NE-14, NE-15, NE-16, NE-17, NE-19, NE-20 | (fills gaps at NE-14 to NE-17, extends past NE-18) |
| DS | DS-25 to DS-40 | DS-07 to DS-12, DS-14 to DS-18, DS-41 to DS-43 (many more) |
| IT | IT-20 to IT-27 | IT-01 to IT-18, IT-28 to IT-34 (many more) |
| AG | AG-19, AG-20, AG-21 | AG-22 to AG-25, AG-27 to AG-29 |
| ED | ED-06 | (none — extends past ED-05) |
| MP | MP-08 | (none — extends past MP-07) |

---

## Next Steps

1. **Step 0.4:** Add the 48 ADD techniques to `techniques/MASTER_TECHNIQUE_INDEX.md` with full definitions
2. **Step 0.4:** Update the 17 parent techniques (from 23 MERGE entries) with variant/extension notes
3. **Step 0.5:** Update all counts in CLAUDE.md, README.md, MASTER_TECHNIQUE_INDEX.md header
4. **Future mining:** Review `DOMAIN_SPECIFIC_TECHNIQUES_ARCHIVE.md` for domain-specific prompt development
