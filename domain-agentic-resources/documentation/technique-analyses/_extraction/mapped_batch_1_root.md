# Mapped Technique Inventory — Batch 1 (Root-Level Analysis Files)

**Generated:** 2026-02-08
**Input:** `_extraction/batch_1_root.md` (55 techniques) + `_extraction/master_index_reference.md` (193 active techniques)
**Task:** Step 0.2b-1 — Cross-reference Batch 1 techniques against Master Technique Index

---

## Mapping Table

| # | Source File | Technique Name | Code | Family | Original Mapping | Verified Mapping | Status | Notes |
|---|------------|----------------|------|--------|-----------------|-----------------|--------|-------|
| 1 | context_restore_standalone_analysis.md | Semantic Vector Retrieval with Cosine Similarity | — | CM | Partially — extends CM-04 | EXTENDS CM-04; effectively equivalent to CM-06 | EXTENDS-EXISTING | CM-04 (Summary-Expand Loop) verified in master. However, this technique describes vector embeddings + cosine similarity for context retrieval, which is the definition of CM-06 (Semantic Vector-Based Context Management). The original mapping to CM-04 is weak. |
| 2 | context_restore_standalone_analysis.md | Multi-Stage Relevance Scoring | CM-10 | CM | No — NEW | No match found | CONFIRMED-NOVEL | Code collision: CM-10 is already assigned to "Memory Scaffold Architecture" in master. Technique describes composite relevance scoring (semantic similarity + temporal decay + historical impact) — no equivalent in master. Cross-file duplicate of #17. |
| 3 | context_restore_standalone_analysis.md | Token-Budget-Constrained Progressive Loading | — | CM | No — NEW | Yes — CM-07 | MATCHED-EXISTING | Directly matches CM-07 (Token-Budget-Aware Progressive Loading): "Dynamically load context components in priority order until token budget exhausted." Same concept. |
| 4 | context_restore_standalone_analysis.md | Component Prioritization Framework | — | CM/DS | Partially — combines CM + DS-02 | EXTENDS CM + DS-02 | EXTENDS-EXISTING | Both CM family and DS-02 (Metric Specification) verified in master. Combination technique: pre-defined component hierarchy with domain-specific ordering uses metric specification within context management. |
| 5 | context_restore_standalone_analysis.md | Three-Way Context Merging | — | CM | No — NEW | No match found | CONFIRMED-NOVEL | Borrows merge strategies from version control (base/local/remote) for context conflict resolution. No equivalent in master — unique approach. Cross-file duplicate of #16. |
| 6 | context_restore_standalone_analysis.md | Lazy Loading with Context Streaming | — | CM/IT | Partially — extends IT techniques | EXTENDS IT-19 | EXTENDS-EXISTING | Original mapping said "extends IT techniques" without specifying. IT-19 (Three-Tier Information Loading: Metadata → SKILL.md → Bundled resources) is the closest match — both involve progressive/on-demand loading. IT-35 (Mentor-Style Feedback) is unrelated. |
| 7 | context_restore_standalone_analysis.md | Cryptographic Context Validation | — | QA/CM | Partially — extends QA-01 | EXTENDS QA-01 (weak) | EXTENDS-EXISTING | QA-01 (Self-Verification) verified in master. Weak mapping — cryptographic signatures for integrity validation is quite different from self-critique. May warrant its own code if deemed reusable. |
| 8 | context_restore_standalone_analysis.md | Cross-Project Knowledge Transfer | DS-22 or CM-11 | DS/CM | No — NEW | No match found | CONFIRMED-NOVEL | Code collisions: DS-22 is already "EARS Requirements Transformation"; CM-11 does not exist in master (CM goes to CM-10). Concept of transferring semantic vectors between project domains has no equivalent. |
| 9 | context_restore_standalone_analysis.md | Adaptive Context Expansion | — | CM/IT | No — NEW | No match found | CONFIRMED-NOVEL | Dynamically expanding context based on workflow needs discovered at runtime. Related to CM-05 (Progressive Context Accumulation) and CM-07 (Token-Budget Loading) but distinct — emphasis is on runtime discovery of context needs, not pre-planned accumulation or budget management. |
| 10 | context_save_restore_analysis.md | Semantic Context Management | CM-06 | CM | Partially — extends CM-04 | Yes — CM-06 | MATCHED-EXISTING | Proposed code CM-06 directly matches master entry CM-06 (Semantic Vector-Based Context Management). Original "extends CM-04" mapping is superseded — this technique already exists in the master index. |
| 11 | context_save_restore_analysis.md | Multi-Modal Context Representation | — | CM | No — NEW | No match found | CONFIRMED-NOVEL | Supporting multiple storage formats (JSON, Markdown, Protocol Buffers, MessagePack, YAML) for context. More of an implementation pattern than a prompt technique. No equivalent in master. |
| 12 | context_save_restore_analysis.md | JSON Schema for Context Structure | — | OC | Yes — OC-02 | Yes — OC-02 | CONFIRMED-EXISTING | OC-02 (JSON Schema Specification) verified in master: "Provide exact JSON structure expected." Direct match. |
| 13 | context_save_restore_analysis.md | Token-Budget-Aware Context Loading | CM-07 | CM | No — NEW | Yes — CM-07 | MATCHED-EXISTING | Proposed code CM-07 directly matches master entry CM-07 (Token-Budget-Aware Progressive Loading). Already exists in master index. Cross-file duplicate of #3. |
| 14 | context_save_restore_analysis.md | Knowledge Graph Construction | CM-09 | CM | No — NEW | No match found | CONFIRMED-NOVEL | Code collision: CM-09 is already "Authority Boundary Specification" in master. Creating ontological representations and relational metadata from context — no equivalent in master index. |
| 15 | context_save_restore_analysis.md | Context Fingerprinting | CM-08 | CM | No — NEW | No match found | CONFIRMED-NOVEL | Code collision: CM-08 is already "File-Based State Persistence" in master. Unique identifiers for context versions with drift detection — no equivalent in master. |
| 16 | context_save_restore_analysis.md | Three-Way Merge for Context | — | CM | No — NEW | No match found | CONFIRMED-NOVEL | Same concept as #5 (Three-Way Context Merging from context_restore_standalone_analysis.md). Cross-file duplicate — consolidation step should deduplicate. |
| 17 | context_save_restore_analysis.md | Relevance-Based Retrieval | — | CM | No — NEW | No match found | CONFIRMED-NOVEL | Same concept as #2 (Multi-Stage Relevance Scoring from context_restore_standalone_analysis.md). Cross-file duplicate — consolidation step should deduplicate. |
| 18 | full_stack_feature_analysis.md | Multi-Phase Workflow Orchestration | — | AG | Partially — extends AG-07 | EXTENDS AG-07 | EXTENDS-EXISTING | AG-07 (Pipeline Orchestration Patterns) verified in master. This adds sequential phase dependency — each phase's output feeds the next — which is a specific orchestration pattern extending AG-07. |
| 19 | full_stack_feature_analysis.md | Extended Thinking Blocks | MP-05 | MP | No — NEW | Yes — MP-05 | MATCHED-EXISTING | Proposed code MP-05 directly matches master entry MP-05 (Extended Thinking Documentation): "Embed system-level reasoning blocks explaining WHY workflows are structured." Already exists in master index. |
| 20 | full_stack_feature_analysis.md | Explicit Agent Specialization Assignment | — | AG | Partially — extends AG-01 | EXTENDS AG-01 | EXTENDS-EXISTING | AG-01 (Personality-First Role Definition) verified in master. This extends it by assigning agents via subagent_type with domain::specialization naming convention. |
| 21 | full_stack_feature_analysis.md | Context Accumulation Pattern | CM-05 | CM | Partially — extends CM-04 | Yes — CM-05 | MATCHED-EXISTING | Proposed code CM-05 directly matches master entry CM-05 (Progressive Context Accumulation): "Explicitly chain context through multi-step workflows." Original "extends CM-04" mapping is superseded. |
| 22 | full_stack_feature_analysis.md | API-First Design Enforcement | DS-13 | DS | No — NEW | Yes — DS-13 | MATCHED-EXISTING | Proposed code DS-13 directly matches master entry DS-13 (Architecture-First Enforcement): "Enforce architectural decisions before implementation." API-first is a specialization of architecture-first. |
| 23 | full_stack_feature_analysis.md | Parallel Execution with Convergence Points | AG-13 | AG | Partially — extends AG-07 | Yes — AG-13 | MATCHED-EXISTING | Proposed code AG-13 directly matches master entry AG-13 (Parallel-Converge Orchestration): "Parallel agent execution with defined convergence points." Original "extends AG-07" mapping is superseded — technique already has its own code. |
| 24 | full_stack_feature_analysis.md | Comprehensive Success Criteria Specification | — | OT/DS | Yes — DS-02 + OC-04 | Yes — DS-02 + OC-04 | CONFIRMED-EXISTING | DS-02 (Metric Specification) and OC-04 (Conditional Output Logic) both verified in master. Combination of measurable criteria with conditional output handling. |
| 25 | full_stack_feature_analysis.md | Configuration-Driven Workflow Customization | IT-14 | IT | No — NEW | No match found | CONFIRMED-NOVEL | IT-14 not in master (IT family only has IT-19 and IT-35). Related to OC-08 (Multi-Mode Prompt Architecture) but distinct — OC-08 is about mode selection, this is about configuration options modifying workflow behavior. |
| 26 | full_stack_feature_analysis.md | Expected Output Specification | — | OT | Yes — ST-03 | Yes — ST-03 | CONFIRMED-EXISTING | ST-03 (Output Format Specification) verified in master: "Dedicated section describing format, structure, and content requirements." Direct match. |
| 27 | full_stack_feature_analysis.md | Quality Gate Integration Points | — | AG/DS | Yes — AG-08 | Yes — AG-08 | CONFIRMED-EXISTING | AG-08 (Evidence-Based Decision Gates) verified in master: "Require visual/quantitative proof, not just assertions." Dedicated quality gate steps in workflow match this pattern. |
| 28 | improve_agent_analysis.md | Data-Driven Improvement Methodology | — | QA | Partially — extends QA-01 | EXTENDS QA-01 | EXTENDS-EXISTING | QA-01 (Self-Verification) verified in master. Extends it by adding a full measurement cycle: baseline metrics → analysis → improvement → testing → deployment with measurement at each stage. |
| 29 | improve_agent_analysis.md | Failure Mode Classification | — | QA/AG | Yes — AG-09 | Yes — AG-09 | CONFIRMED-EXISTING | AG-09 (Anti-Pattern & Failure Mode Embedding) verified in master: "Explicitly document what leads to failure, embedded in agent identity." Systematic categorization of failure types aligns with this. |
| 30 | improve_agent_analysis.md | Chain-of-Thought Enhancement | — | RT | Yes — RT-01 | Yes — RT-01 | CONFIRMED-EXISTING | RT-01 (Chain-of-Thought) verified in master: "Explicit instruction to show step-by-step reasoning." Direct match. |
| 31 | improve_agent_analysis.md | Constitutional AI Integration | QA-06 | QA | No — NEW | Yes — QA-06 | MATCHED-EXISTING | Proposed code QA-06 directly matches master entry QA-06 (Constitutional AI for Prompts): "Critique-revise loops against defined constitutional principles." Already exists in master index. |
| 32 | improve_agent_analysis.md | A/B Testing Framework | QA-07 | QA | No — NEW | Yes — QA-07 | MATCHED-EXISTING | Proposed code QA-07 directly matches master entry QA-07 (Statistical A/B Testing for Prompts): "Rigorous experimental methods to compare prompt variations." Already exists in master index. |
| 33 | improve_agent_analysis.md | Staged Rollout Pattern | AG-15 | AG | No — NEW | Yes — AG-15 | MATCHED-EXISTING | Proposed code AG-15 directly matches master entry AG-15 (Staged Rollout with Automatic Rollback): "Progressive deployment with quality monitoring and rollback triggers." Already exists in master index. |
| 34 | improve_agent_analysis.md | Multi-Metric Evaluation | — | QA/DS | Yes — DS-02 | Yes — DS-02 | CONFIRMED-EXISTING | DS-02 (Metric Specification) verified in master: "Define specific, measurable criteria." Multi-metric evaluation is an application of metric specification across multiple dimensions. |
| 35 | issue_resolution_analysis.md | Systematic Investigation Framework | — | DT/DS | Yes — DT-01 | Yes — DT-01 | CONFIRMED-EXISTING | DT-01 (Hierarchical Task Breakdown) verified in master: "Break complex tasks into phases and subtasks." Multi-stage investigation (Triage → Root Cause → Planning → Implementation → Testing → Deployment) is a hierarchical breakdown. |
| 36 | issue_resolution_analysis.md | Tool Integration with Explicit Commands | — | DS/OT | Partially — extends DS-03 | EXTENDS DS-03 | EXTENDS-EXISTING | DS-03 (Tool and Methodology Suggestions) verified in master. This extends it by embedding actual CLI commands (gh, git bisect, rg) rather than just recommending tools. |
| 37 | issue_resolution_analysis.md | Priority Classification Framework | — | DS | Yes — DS-06 | Yes — DS-06 | CONFIRMED-EXISTING | DS-06 (Prioritization and Severity Guidance) verified in master: "Explicit instructions to rank findings." 4-tier P0-P3 priority system is a direct application. |
| 38 | issue_resolution_analysis.md | Code Archaeology Techniques | DS-15 | DS | No — NEW | No match found | CONFIRMED-NOVEL | DS-15 not in master (DS family has gap from DS-06 to DS-13). Systematic historical analysis using git bisect, blame, and log for debugging — unique investigation technique with no equivalent in master. |
| 39 | issue_resolution_analysis.md | Test-Driven Bug Fixing | — | DS | Yes — DS-02 | Yes — DS-02 (weak); better match DS-148 | CONFIRMED-EXISTING | DS-02 (Metric Specification) verified in master. However, the mapping is semantically weak — this technique is about TDD for bug fixing, which maps much better to DS-148 (TDD-First Development Pattern): "Write tests before implementation as mandatory workflow step." |
| 40 | issue_resolution_analysis.md | Incremental Commit Strategy | — | DS/OT | Yes — OC-01 | Yes — OC-01 (deprecated → ST-03) | CONFIRMED-EXISTING | OC-01 found in deprecated list — merged into ST-03 (Output Format Specification). Weak mapping: atomic commits with conventional messages is more workflow than output format. |
| 41 | issue_resolution_analysis.md | Comprehensive PR Template | — | OT/QA | Yes — OC-01 + QA-01 | Yes — ST-03 (was OC-01) + QA-01 | CONFIRMED-EXISTING | OC-01 deprecated → ST-03 (Output Format Specification) verified; QA-01 (Self-Verification) verified. PR template combines structured output format with self-review checklist. |
| 42 | issue_resolution_analysis.md | Multi-Test-Layer Strategy | — | DS | Yes — DS-02 | Yes — DS-02 (weak) | CONFIRMED-EXISTING | DS-02 (Metric Specification) verified in master. Weak mapping — test pyramid strategy (unit/integration/E2E) is about testing methodology rather than metric specification. DS-148 (TDD-First Development Pattern) is somewhat related but also not a direct match. |
| 43 | multi_agent_optimize_analysis.md | Multi-Dimensional Agent Profiling | — | AG/DS | Partially — extends AG-07 | EXTENDS AG-07 | EXTENDS-EXISTING | AG-07 (Pipeline Orchestration Patterns) verified in master. Deploying specialized profiling agents across different system layers (DB, Application, Frontend) extends the orchestration pattern. |
| 44 | multi_agent_optimize_analysis.md | Embedded Code Examples as Implementation Guidance | — | ED/OT | Yes — AG-05 | Yes — AG-05 | CONFIRMED-EXISTING | AG-05 (Concrete Deliverable Templates) verified in master: "Include actual working code/examples, not placeholder templates." Direct match. |
| 45 | multi_agent_optimize_analysis.md | Framework-Based Organization | — | ST/DS | Yes — ST-02 + ST-05 | Yes — ST-02 + ST-05 | CONFIRMED-EXISTING | ST-02 (Structured Sequential Instructions) and ST-05 (Hierarchical Organization) both verified in master. Numbered frameworks with subsections combine sequential instructions with hierarchy. |
| 46 | multi_agent_optimize_analysis.md | Cost-Aware Optimization | AG-14 | AG | No — NEW | Yes — AG-14 | MATCHED-EXISTING | Proposed code AG-14 directly matches master entry AG-14 (Cost-Aware Agent Orchestration): "Strategically assign LLM models based on task criticality." Already exists in master index. |
| 47 | multi_agent_optimize_analysis.md | Reference Workflow Examples | — | ED/OT | Yes — ED-02 | Yes — ED-02 (weak); consider ED-05 | CONFIRMED-EXISTING | ED-02 (Progressive Exercise Generation) verified in master. Weak mapping — concrete workflow examples showing step-by-step application maps better to ED-05 (Reference Class Priming): "Show example of excellent output, then ask for similar quality." |
| 48 | standup_notes_analysis.md | Multi-Source Data Orchestration | — | AG/DS | Yes — AG-07 | Yes — AG-07 | CONFIRMED-EXISTING | AG-07 (Pipeline Orchestration Patterns) verified in master. Coordinating Git, Jira, Obsidian, Calendar into single coherent output is multi-source orchestration. |
| 49 | standup_notes_analysis.md | AI-Assisted Commit Summarization | NE-13 | NE | No — NEW | Yes — NE-13 | MATCHED-EXISTING | Proposed code NE-13 directly matches master entry NE-13 (Technical-to-Business Translation): "Convert technical details to business value statements." Converting git commits to business-readable summaries is this exact pattern. |
| 50 | standup_notes_analysis.md | Structured Output Templates with Time Metadata | — | OT/NE | Yes — OC-01 + NE-02 | Yes — ST-03 (was OC-01) + NE-02 | CONFIRMED-EXISTING | OC-01 deprecated → ST-03 (Output Format Specification) verified; NE-02 (Phased Workflow Architecture) verified. Yesterday/Today/Blockers with time estimates combines structured output with phased architecture. |
| 51 | standup_notes_analysis.md | Blocker Escalation Framework | DS-20 | DS | No — NEW | No match found | CONFIRMED-NOVEL | Code collision: DS-20 is already "Frontier Mapping (Capability Classification)" in master. Structured blocker reporting with Impact/Need/From/Tried/Next-Step fields has no direct equivalent. Conceptually overlaps with DS-06 (Prioritization) + ST-03 (Output Format) but is specialized enough to be distinct. |
| 52 | standup_notes_analysis.md | Async-First Communication Principles | NE-14 | NE | Partially — extends NE-01 | EXTENDS NE-01 | EXTENDS-EXISTING | NE-01 (Single-Question Pacing Protocol) verified in master. Extends it for async contexts — designing communication with enough context for distributed timezone consumption. Also related to DS-113 (Async-First Design Principle) but that applies to code, not communication. |
| 53 | standup_notes_analysis.md | Pattern Recognition in Commits | — | DS | No — NEW | Yes — DS-04 | MATCHED-EXISTING | DS-04 (Pattern Recognition Requests) verified in master: "Identify trends, patterns, systemic issues." Extracting accomplishments by recognizing patterns in commit messages is a specific application of DS-04. |
| 54 | standup_notes_analysis.md | Capacity-Aware Planning | — | DS/NE | Yes — NE-09 | Yes — NE-09 | CONFIRMED-EXISTING | NE-09 (Scope Reduction Pressure) verified in master: "Explicit instructions to challenge, cut, and reduce scope." Calculating available time and flagging overcommitment triggers scope reduction. |
| 55 | standup_notes_analysis.md | Follow-Up Action Extraction | DS-21 | DS | No — NEW | No match found | CONFIRMED-NOVEL | Code collision: DS-21 is already "Proximity Assessment (Timeline Classification)" in master. Automatically extracting actionable tasks from standup content — no equivalent in master for automated action item extraction. |

---

## Batch Summary

### By Status

| Status | Count | Percentage |
|--------|-------|------------|
| CONFIRMED-EXISTING | 19 | 34.5% |
| MATCHED-EXISTING | 13 | 23.6% |
| EXTENDS-EXISTING | 10 | 18.2% |
| CONFIRMED-NOVEL | 13 | 23.6% |
| NEEDS-REVIEW | 0 | 0.0% |
| **Total** | **55** | **100%** |

### Interpretation

- **32 techniques (58.2%)** map directly to existing master index entries (CONFIRMED-EXISTING + MATCHED-EXISTING)
- **10 techniques (18.2%)** extend existing techniques with meaningful additions
- **13 techniques (23.6%)** are confirmed novel with no clear master index equivalent

### MATCHED-EXISTING Detail

These 13 techniques were marked "No — NEW" in the batch but actually match existing master index entries. Many of these were *proposed* by the analysis files and have since been *added* to the master index:

| # | Technique Name | Proposed Code | Matched To | Master Entry Name |
|---|---------------|---------------|------------|-------------------|
| 3 | Token-Budget-Constrained Progressive Loading | — | CM-07 | Token-Budget-Aware Progressive Loading |
| 10 | Semantic Context Management | CM-06 | CM-06 | Semantic Vector-Based Context Management |
| 13 | Token-Budget-Aware Context Loading | CM-07 | CM-07 | Token-Budget-Aware Progressive Loading |
| 19 | Extended Thinking Blocks | MP-05 | MP-05 | Extended Thinking Documentation |
| 21 | Context Accumulation Pattern | CM-05 | CM-05 | Progressive Context Accumulation |
| 22 | API-First Design Enforcement | DS-13 | DS-13 | Architecture-First Enforcement |
| 23 | Parallel Execution with Convergence Points | AG-13 | AG-13 | Parallel-Converge Orchestration |
| 31 | Constitutional AI Integration | QA-06 | QA-06 | Constitutional AI for Prompts |
| 32 | A/B Testing Framework | QA-07 | QA-07 | Statistical A/B Testing for Prompts |
| 33 | Staged Rollout Pattern | AG-15 | AG-15 | Staged Rollout with Automatic Rollback |
| 46 | Cost-Aware Optimization | AG-14 | AG-14 | Cost-Aware Agent Orchestration |
| 49 | AI-Assisted Commit Summarization | NE-13 | NE-13 | Technical-to-Business Translation |
| 53 | Pattern Recognition in Commits | — | DS-04 | Pattern Recognition Requests |

### CONFIRMED-NOVEL Detail

These 13 techniques have no clear equivalent in the master index:

| # | Technique Name | Proposed Code | Code Collision? | Notes |
|---|---------------|---------------|-----------------|-------|
| 2 | Multi-Stage Relevance Scoring | CM-10 | Yes — CM-10 = Memory Scaffold Architecture | Composite scoring (semantic + temporal + historical). Cross-file dup of #17. |
| 5 | Three-Way Context Merging | — | No | Version-control merge strategies for context. Cross-file dup of #16. |
| 8 | Cross-Project Knowledge Transfer | DS-22 / CM-11 | Yes — DS-22 = EARS Requirements Transformation | Vector mapping between project domains. |
| 9 | Adaptive Context Expansion | — | No | Runtime discovery of context needs. Related to CM-05/CM-07 but distinct. |
| 11 | Multi-Modal Context Representation | — | No | Multi-format serialization. More implementation than prompt technique. |
| 14 | Knowledge Graph Construction | CM-09 | Yes — CM-09 = Authority Boundary Specification | Ontological context representation. |
| 15 | Context Fingerprinting | CM-08 | Yes — CM-08 = File-Based State Persistence | Version identifiers with drift detection. |
| 16 | Three-Way Merge for Context | — | No | Cross-file duplicate of #5. |
| 17 | Relevance-Based Retrieval | — | No | Cross-file duplicate of #2. |
| 25 | Configuration-Driven Workflow Customization | IT-14 | No (IT-14 not in master) | Related to OC-08 but distinct. |
| 38 | Code Archaeology Techniques | DS-15 | No (DS-15 not in master) | git bisect/blame/log for debugging. |
| 51 | Blocker Escalation Framework | DS-20 | Yes — DS-20 = Frontier Mapping | Structured blocker reporting format. |
| 55 | Follow-Up Action Extraction | DS-21 | Yes — DS-21 = Proximity Assessment | Automated action item extraction. |

### Code Collision Summary

6 techniques from the analysis files proposed codes that collide with existing (different) master index entries:

| Proposed Code | Analysis File Technique | Master Index Technique |
|--------------|------------------------|----------------------|
| CM-10 | Multi-Stage Relevance Scoring | Memory Scaffold Architecture |
| CM-09 | Knowledge Graph Construction | Authority Boundary Specification |
| CM-08 | Context Fingerprinting | File-Based State Persistence |
| DS-22 | Cross-Project Knowledge Transfer | EARS Requirements Transformation |
| DS-20 | Blocker Escalation Framework | Frontier Mapping (Capability Classification) |
| DS-21 | Follow-Up Action Extraction | Proximity Assessment (Timeline Classification) |

These collisions indicate the analysis files proposed codes that were later assigned to different techniques when added to the master index. Consolidation step (0.2b-10) must reassign codes for any novel techniques that survive deduplication.

### Cross-File Duplicates

4 duplicate pairs identified within this batch (both from the two related context management analyses):

| Pair | Technique A | Technique B | Canonical |
|------|-----------|-----------|-----------|
| 1 | #2 Multi-Stage Relevance Scoring | #17 Relevance-Based Retrieval | #2 (has proposed code) |
| 2 | #5 Three-Way Context Merging | #16 Three-Way Merge for Context | #5 (first occurrence) |
| 3 | #3 Token-Budget-Constrained Progressive Loading | #13 Token-Budget-Aware Context Loading | Both → CM-07 (existing) |
| 4 | #1 Semantic Vector Retrieval w/ Cosine Similarity | #10 Semantic Context Management | Both → CM-06 (existing) |

After deduplication: 55 total → 51 unique techniques (4 cross-file duplicates removed).

### Weak Mapping Flags

These CONFIRMED-EXISTING techniques have mappings that are technically verified but semantically questionable:

| # | Technique | Mapped To | Issue | Better Match |
|---|----------|----------|-------|-------------|
| 39 | Test-Driven Bug Fixing | DS-02 (Metric Specification) | TDD is not metric specification | DS-148 (TDD-First Development Pattern) |
| 40 | Incremental Commit Strategy | OC-01 → ST-03 (Output Format) | Commit strategy is workflow, not output format | No clear single match |
| 42 | Multi-Test-Layer Strategy | DS-02 (Metric Specification) | Test pyramid is testing methodology, not metrics | No clear single match |
| 47 | Reference Workflow Examples | ED-02 (Progressive Exercise Generation) | Examples are reference material, not exercises | ED-05 (Reference Class Priming) |
