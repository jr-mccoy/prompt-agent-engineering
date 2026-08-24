# Technique Extraction — Batch 5 (Skill Analysis Files — Small)

**Files analyzed:** 7
**Total lines:** ~1,810
**Date extracted:** 2026-02-08

---

## Extraction Table

| # | Source File | Technique Name | Code (if assigned) | Family | Maps To Existing | Novel? | Brief Description |
|---|------------|----------------|-------------------|--------|-----------------|--------|-------------------|
| 1 | claude_code_history_files_finder_analysis.md | Forensic Recovery Workflow | DS-79 | DS | No — NEW | Yes | Systematic data archaeology: Search → Identify → Extract → Verify → Sanitize |
| 2 | claude_code_history_files_finder_analysis.md | Multi-Mode CLI Design | IT-30 | IT | No — NEW | Yes | Single tool with verb-based subcommands (list, search, stats, recover) |
| 3 | claude_code_history_files_finder_analysis.md | Streaming Line-by-Line Processing | DS-80 | DS | No — NEW | Yes | Process massive files (>100MB) with constant memory via line-by-line JSONL parsing |
| 4 | claude_code_history_files_finder_analysis.md | Capability Boundary Specification | OT-10 | OT | No — NEW | Yes | Explicit "What Can Be Recovered" vs "What Cannot Be Recovered" matrices |
| 5 | claude_code_history_files_finder_analysis.md | Privacy-First Documentation | QA-18 | QA | No — NEW | Yes | Mandatory security/privacy section before sharing recovered content |
| 6 | claude_code_history_files_finder_analysis.md | Path Normalization Transparency | DS-81 | DS | No — NEW | Yes | Documents how system transforms input paths for storage with troubleshooting |
| 7 | video_comparer_analysis.md | Multi-Layered Validation Chain | DS-47 | DS | Partially — extends DS-02 | Yes | Sequential validation stages with progressive specificity (tool → file → format → constraints → content) |
| 8 | video_comparer_analysis.md | Quality Metric Interpretation Dictionary | DS-48 | DS | No — NEW | Yes | Lookup tables mapping metric values to quality levels, use cases, and targets |
| 9 | video_comparer_analysis.md | Self-Contained Interactive Report Generation | OT-08 | OT | Partially — extends OT-01 | Yes | Embed all resources (data, images, styles, scripts) as inline content for zero-dependency reports |
| 10 | video_comparer_analysis.md | Adjustable Constants Configuration Pattern | IT-25 | IT | Partially — extends IT-18 | Yes | Centralize all configuration as named constants at top of script with inline documentation |
| 11 | skills_search_analysis.md | CLI Command Reference Table | OT-18 | OT | Partially — extends OT-02 | Yes | Structured command documentation with syntax, options, and examples |
| 12 | skills_search_analysis.md | Numbered Workflow for Tool Discovery | DS-119 | DS | No — NEW | Yes | 5-step workflow for finding, evaluating, and installing tools |
| 13 | skills_search_analysis.md | Popular Options Directory | IT-45 | IT | No — NEW | Yes | Curated table of commonly-used options with use cases for fast-tracking |
| 14 | skills_search_analysis.md | Restart Requirement Warning | IT-46 | IT | No — NEW | Yes | Explicit warning about post-installation action required for changes to take effect |
| 15 | skills_search_analysis.md | Inline Command Comments | OT-19 | OT | No — NEW | Yes | Explanatory comments after bash commands using # for self-documenting examples |
| 16 | skills_search_analysis.md | Meta-Skill Pattern | AG-24 | AG | No — NEW | Yes | A skill that facilitates discovery and installation of other skills |
| 17 | docs_cleaner_analysis.md | Critical Evaluation Gate | QA-23 | QA | No — NEW | Yes | Mandatory analysis checkpoint before any destructive action |
| 18 | docs_cleaner_analysis.md | Section-by-Section Value Mapping | DS-97 | DS | No — NEW | Yes | Tabular analysis of each documentation section with value justification |
| 19 | docs_cleaner_analysis.md | Three-Tier Value Classification | ST-36 | ST | No — NEW | Yes | Color-coded classification system (Keep=Green, Condense=Yellow, Delete=Red) |
| 20 | docs_cleaner_analysis.md | Quantitative Before/After Metrics | OT-13 | OT | Partially — extends OT-02 | Yes | Explicit metrics showing reduction percentage and value preservation |
| 21 | docs_cleaner_analysis.md | Mandatory Preservation Checklist | QA-24 | QA | Partially — extends QA-01 | Yes | Category-specific checklist to verify all essential content types are preserved |
| 22 | docs_cleaner_analysis.md | Anti-Pattern Table with Solutions | IT-33 | IT | No — NEW | Yes | Structured table of common mistakes with corrective actions |
| 23 | docs_cleaner_analysis.md | Four-Phase Documentation Workflow | DS-98 | DS | Partially — extends DS-01 | Yes | Sequential phases: Discovery → Value Analysis → Consolidation Plan → Execution |
| 24 | docs_cleaner_analysis.md | Output Artifacts Specification | OT-14 | OT | Partially — extends OT-02 | Yes | Explicit enumeration of required deliverables for the task |
| 25 | docs_cleaner_analysis.md | Bundled Template Reference | — | IT | Yes — IT-14 | No | Progressive disclosure - main skill references detailed template in bundled file |
| 26 | claude_md_progressive_disclosurer_analysis.md | Structured Multi-Phase Workflow | — | DS | Yes — DS-03, RT-01 | No | 4-step process: Audit → Classify → Propose → Execute |
| 27 | claude_md_progressive_disclosurer_analysis.md | Decision Table Classification | — | IT | Yes — IT-03, DS-04 | No | Matrix with criteria, classification, and action for content placement |
| 28 | claude_md_progressive_disclosurer_analysis.md | Token Economics Analysis | DS-35 | DS | No — NEW | Yes | Calculate token costs to justify optimization decisions |
| 29 | claude_md_progressive_disclosurer_analysis.md | Three-Tier Information Loading | IT-19 | IT | Partially — extends IT-13 | Yes | Explicit tiers for progressive information access (L1 always, L2 on-demand, L3 skill-triggered) |
| 30 | claude_md_progressive_disclosurer_analysis.md | Anti-Pattern Documentation | ST-28 | ST | No — NEW | Yes | Teaching by contrasting bad examples with good alternatives |
| 31 | claude_md_progressive_disclosurer_analysis.md | Quantitative Optimization Proposal | QA-11 | QA | No — NEW | Yes | Present optimization plans with measurable before/after metrics and impact percentages |
| 32 | claude_md_progressive_disclosurer_analysis.md | Content Classification Matrix | DS-36 | DS | No — NEW | Yes | Multi-dimensional evaluation (Frequency × Complexity × Reusability) |
| 33 | claude_md_progressive_disclosurer_analysis.md | Reference File Pointers | IT-20 | IT | No — NEW | Yes | Lightweight linking strategy with one-line summaries |
| 34 | claude_md_progressive_disclosurer_analysis.md | Size-Based Decision Guidelines | DS-37 | DS | No — NEW | Yes | Thresholds that trigger specific actions based on content size |
| 35 | claude_md_progressive_disclosurer_analysis.md | Success Measurement Criteria | — | QA | Yes — QA-04 | No | Define verification steps post-optimization |
| 36 | mermaid_tools_analysis.md | Context-Aware Naming Algorithm | DS-43 | DS | No — NEW | Yes | Analyze surrounding text context to generate intelligent filenames |
| 37 | mermaid_tools_analysis.md | Diagram-Type Smart Sizing | DS-44 | DS | No — NEW | Yes | Adjust output dimensions based on detected content type |
| 38 | mermaid_tools_analysis.md | Self-Contained Script Package | IT-24 | IT | No — NEW | Yes | Bundle all dependencies (scripts, configs) in single directory |
| 39 | mermaid_tools_analysis.md | Priority-Based Context Detection | DS-45 | DS | No — NEW | Yes | Tiered heuristics for information extraction (specific → general) |
| 40 | mermaid_tools_analysis.md | Environment Variable Configuration | — | IT | Yes — IT-09 | No | Allow runtime customization without editing code |
| 41 | mermaid_tools_analysis.md | Sequential Numbering for Ordering | — | DS | Yes — DS-04 | No | Prefix outputs with sequence numbers to preserve document order |
| 42 | mermaid_tools_analysis.md | Multi-Phase Orchestration Script | — | DS | Yes — DS-11 | No | Main script coordinates multiple sub-processes |
| 43 | mermaid_tools_analysis.md | Scale Factor for Quality Control | — | DS | Yes — DS-09 | No | Separate resolution from dimensions using scale multiplier |
| 44 | mermaid_tools_analysis.md | Lookback Window for Context | DS-46 | DS | No — NEW | Yes | Analyze N lines before target to extract context |
| 45 | mermaid_tools_analysis.md | Prerequisite Verification Guidance | — | IT/DS | Yes — DS-10 | No | Provide verification commands for dependencies |
| 46 | api_design_principles_analysis.md | Domain Theory Grounding | — | ST | Partially — extends ST-26 | Yes | Teach fundamental domain principles before practical patterns |
| 47 | api_design_principles_analysis.md | Multi-Paradigm Comparison | ST-30 | ST | No — NEW | Yes | Teach multiple approaches to same problem side-by-side |
| 48 | api_design_principles_analysis.md | Domain Pattern Library | DS-41 | DS | No — NEW | Yes | Curated collection of proven patterns with working implementations |
| 49 | api_design_principles_analysis.md | HTTP Semantics Enforcement | DS-42 | DS | No — NEW | Yes | Use protocol semantics (HTTP methods, status codes) as design constraints |
| 50 | api_design_principles_analysis.md | Pre-Implementation Checklist | QA-13 | QA | No — NEW | Yes | 137-point verification checklist covering all aspects before building |
| 51 | api_design_principles_analysis.md | Good/Bad Code Comparison | — | ST | Yes — ST-28 | No | Side-by-side comparison of correct vs incorrect implementations |
| 52 | api_design_principles_analysis.md | Bundled Code Templates | IT-23 | IT | No — NEW | Yes | Working code templates packaged with skill for immediate use |
| 53 | api_design_principles_analysis.md | N+1 Problem Prevention Pattern | — | DS | Yes — DS-09 | No | DataLoader pattern with batch loading to prevent query multiplication |
| 54 | api_design_principles_analysis.md | Pagination Pattern Library | — | DS | Yes — DS-03 | No | Multiple pagination strategies (offset, cursor, Relay) with implementations |
| 55 | api_design_principles_analysis.md | Common Pitfalls Section | — | ST | Yes — ST-28 | No | Explicitly list common mistakes developers make |

---

## Summary

| Metric | Count |
|--------|-------|
| **Total techniques extracted** | 55 |
| **Marked as Novel (Yes)** | 40 |
| **Marked as Existing (No)** | 15 |
| **Unique source files** | 7 |

### By Family

| Family | Count | Novel | Existing |
|--------|-------|-------|----------|
| DS (Domain-Specific) | 22 | 16 | 6 |
| IT (Interaction) | 12 | 8 | 4 |
| OT (Output) | 6 | 5 | 1 |
| QA (Quality Assurance) | 6 | 5 | 1 |
| ST (Structural) | 5 | 3 | 2 |
| AG (Agentic) | 1 | 1 | 0 |

> **Note:** Some techniques span multiple families (e.g., IT/DS). Primary family is used for counting; the secondary family is listed in the table's Family column with a slash. Two techniques (#26, #27) map fully to existing techniques but are included for completeness.

### By Source File

| Source File | Techniques | Novel | Existing |
|------------|-----------|-------|----------|
| claude_code_history_files_finder_analysis.md | 6 | 6 | 0 |
| video_comparer_analysis.md | 4 | 4 | 0 |
| skills_search_analysis.md | 6 | 6 | 0 |
| docs_cleaner_analysis.md | 9 | 8 | 1 |
| claude_md_progressive_disclosurer_analysis.md | 10 | 7 | 3 |
| mermaid_tools_analysis.md | 10 | 5 | 5 |
| api_design_principles_analysis.md | 10 | 5 | 5 |

### Novel Techniques with Proposed Codes

The following techniques were explicitly proposed for addition to MASTER_TECHNIQUE_INDEX by their respective analysis files:

| Proposed Code | Technique Name | Source File |
|--------------|----------------|-------------|
| DS-35 | Token Economics Analysis | claude_md_progressive_disclosurer_analysis.md |
| DS-36 | Content Classification Matrix | claude_md_progressive_disclosurer_analysis.md |
| DS-37 | Size-Based Decision Guidelines | claude_md_progressive_disclosurer_analysis.md |
| DS-41 | Domain Pattern Library | api_design_principles_analysis.md |
| DS-42 | HTTP Semantics Enforcement | api_design_principles_analysis.md |
| DS-43 | Context-Aware Naming Algorithm | mermaid_tools_analysis.md |
| DS-44 | Diagram-Type Smart Sizing | mermaid_tools_analysis.md |
| DS-45 | Priority-Based Context Detection | mermaid_tools_analysis.md |
| DS-46 | Lookback Window for Context | mermaid_tools_analysis.md |
| DS-47 | Multi-Layered Validation Chain | video_comparer_analysis.md |
| DS-48 | Quality Metric Interpretation Dictionary | video_comparer_analysis.md |
| DS-79 | Forensic Recovery Workflow | claude_code_history_files_finder_analysis.md |
| DS-80 | Streaming Line-by-Line Processing | claude_code_history_files_finder_analysis.md |
| DS-81 | Path Normalization Transparency | claude_code_history_files_finder_analysis.md |
| DS-97 | Section-by-Section Value Mapping | docs_cleaner_analysis.md |
| DS-98 | Four-Phase Documentation Workflow | docs_cleaner_analysis.md |
| DS-119 | Numbered Workflow for Tool Discovery | skills_search_analysis.md |
| IT-19 | Three-Tier Information Loading | claude_md_progressive_disclosurer_analysis.md |
| IT-20 | Reference File Pointers | claude_md_progressive_disclosurer_analysis.md |
| IT-23 | Bundled Code Templates | api_design_principles_analysis.md |
| IT-24 | Self-Contained Script Package | mermaid_tools_analysis.md |
| IT-25 | Adjustable Constants Configuration | video_comparer_analysis.md |
| IT-30 | Multi-Mode CLI Design | claude_code_history_files_finder_analysis.md |
| IT-33 | Anti-Pattern Table with Solutions | docs_cleaner_analysis.md |
| IT-45 | Popular Options Directory | skills_search_analysis.md |
| IT-46 | Restart Requirement Warning | skills_search_analysis.md |
| OT-08 | Self-Contained Interactive Report | video_comparer_analysis.md |
| OT-13 | Quantitative Before/After Metrics | docs_cleaner_analysis.md |
| OT-14 | Output Artifacts Specification | docs_cleaner_analysis.md |
| OT-18 | CLI Command Reference Table | skills_search_analysis.md |
| OT-19 | Inline Command Comments | skills_search_analysis.md |
| QA-11 | Quantitative Optimization Proposal | claude_md_progressive_disclosurer_analysis.md |
| QA-13 | Pre-Implementation Checklist | api_design_principles_analysis.md |
| QA-18 | Privacy-First Documentation | claude_code_history_files_finder_analysis.md |
| QA-23 | Critical Evaluation Gate | docs_cleaner_analysis.md |
| QA-24 | Mandatory Preservation Checklist | docs_cleaner_analysis.md |
| ST-28 | Anti-Pattern Documentation | claude_md_progressive_disclosurer_analysis.md |
| ST-30 | Multi-Paradigm Comparison | api_design_principles_analysis.md |
| ST-36 | Three-Tier Value Classification | docs_cleaner_analysis.md |
| AG-24 | Meta-Skill Pattern | skills_search_analysis.md |

### Cross-File Overlap Notes

Several techniques appear in multiple analysis files with variations:

1. **Anti-Pattern Documentation** appears as ST-28 in `claude_md_progressive_disclosurer_analysis.md` (#30) and is referenced by `docs_cleaner_analysis.md` (#22 as IT-33) and `api_design_principles_analysis.md` (#51, #55 as existing ST-28). The core concept (bad vs. good examples) is the same, but IT-33 specifically uses a structured table format with Problem/Solution columns while ST-28 uses inline Bad/Good contrasts.

2. **Quantitative Before/After Metrics** in `docs_cleaner_analysis.md` (#20, OT-13) overlaps conceptually with **Quantitative Optimization Proposal** in `claude_md_progressive_disclosurer_analysis.md` (#31, QA-11). Both present before/after measurements, but OT-13 focuses on demonstrating impact while QA-11 focuses on proposing changes with measurable predictions.

3. **Bundled Code Templates** (IT-23) in `api_design_principles_analysis.md` (#52) and **Self-Contained Script Package** (IT-24) in `mermaid_tools_analysis.md` (#38) are related but distinct: IT-23 bundles template code for user adaptation, while IT-24 bundles executable scripts with all dependencies.

4. **Three-Tier Value Classification** (ST-36) in `docs_cleaner_analysis.md` (#19) and **Three-Tier Information Loading** (IT-19) in `claude_md_progressive_disclosurer_analysis.md` (#29) both use three tiers but for different purposes: ST-36 classifies content value (Keep/Condense/Delete) while IT-19 classifies information loading priority (Always/On-demand/Skill-triggered).

These overlaps should be reviewed during the consolidation step (0.1j) to determine whether they represent genuinely distinct techniques or should be merged.
