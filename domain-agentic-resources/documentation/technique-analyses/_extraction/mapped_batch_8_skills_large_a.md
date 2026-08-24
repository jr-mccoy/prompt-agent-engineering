# Mapped Technique Inventory — Batch 8 (Skills Large A)

**Source Batch:** `_extraction/batch_8_skills_large_a.md`
**Master Reference:** `_extraction/master_index_reference.md` (193 active techniques)
**Date Mapped:** 2026-02-09
**Techniques in Batch:** 41

---

## File 1: skill_creator_analysis.md (10 techniques)

| # | Source File | Technique Name | Code | Family | Original Mapping | Verified Mapping | Status | Notes |
|---|------------|----------------|------|--------|-----------------|-----------------|--------|-------|
| 1 | skill_creator_analysis.md | Meta-Skill Self-Reference Pattern | AG-18 | AG | No — NEW | AG-18 | CONFIRMED-EXISTING | AG-18 exists in master index as "Meta-Skill Self-Reference" — exact match despite batch marking as NEW |
| 2 | skill_creator_analysis.md | Multi-Stage Validation Pipeline | DS-24 | DS | No — NEW | QA-08 | MATCHED-EXISTING | CODE COLLISION: DS-24 is "API Reference Bundling" in master index. Sequential validation gates with fail-fast maps to QA-08 "Gate-Based Verification" (binary pass/fail checkpoints that must pass before proceeding) |
| 3 | skill_creator_analysis.md | Content-Based Integrity Validation | QA-09 | QA | Partial — QA-03 | — | CONFIRMED-NOVEL | CODE COLLISION: QA-09 is "Reversibility Assessment" in master index. QA-03 is deprecated (merged into QA-01). Hash-based change detection to invalidate stale security approvals is a distinct pattern not captured by existing techniques |
| 4 | skill_creator_analysis.md | Template-Based Educational Scaffolding | IT-16 | IT | Partial — IT-06 + OT-03 | — | CONFIRMED-NOVEL | IT-16, IT-06, OT-03 all absent from master index. Code templates with embedded TODO markers, contextual examples, and deletion instructions is distinct from ED-01 (iterative scaffolding) and AG-05 (concrete deliverables) |
| 5 | skill_creator_analysis.md | CLI-First Executable Documentation | DS-25 | DS | Partial — DS-02 | — | CONFIRMED-NOVEL | DS-25 absent from master index. Scripts serving dual purpose as documentation and executable tools differs from DS-02 "Metric Specification." Unique pattern of documentation-as-code |
| 6 | skill_creator_analysis.md | Layered Security Validation | DS-26 | DS | Partial — DS-04 | — | CONFIRMED-NOVEL | DS-26 absent from master index. Multi-tool security scanning combining industry standards with custom patterns is distinct from DS-61 "Security Tier Classification" (which is about tiers, not scanning layers) and DS-118 "Security-Default Behavioral Traits" |
| 7 | skill_creator_analysis.md | Progressive Error Reporting | — | IT | Yes — IT-01 | OC-08 | MATCHED-EXISTING | IT-01 absent from master index. Error verbosity adapting to use case maps to OC-08 "Multi-Mode Prompt Architecture" (single prompt with multiple modes triggered by context) |
| 8 | skill_creator_analysis.md | Workflow-Encoded Process Documentation | DS-27 | DS | Partial — RT-04 | ST-02 | MATCHED-EXISTING | DS-27 absent from master index. Documentation structured as numbered procedural steps with skip conditions maps to ST-02 "Structured Sequential Instructions" (numbered step-by-step instructions breaking complex tasks into subtasks) |
| 9 | skill_creator_analysis.md | Reference File Naming Convention Enforcement | — | DS | Yes — OT-05 | CM-02 | MATCHED-EXISTING | OT-05 absent from master index. Self-explanatory filenames enforced through validation maps to CM-02 "Constraint Specification" (explicit must/must-not requirements) applied to naming conventions |
| 10 | skill_creator_analysis.md | Dual-Mode Validation Reporting | IT-17 | IT | No — NEW | OC-08 | MATCHED-EXISTING | IT-17 absent from master index. Same validation logic with gate vs educational reporting modes maps to OC-08 "Multi-Mode Prompt Architecture" (single prompt with multiple modes) |

---

## File 2: gitops_workflow_analysis.md (11 techniques)

| # | Source File | Technique Name | Code | Family | Original Mapping | Verified Mapping | Status | Notes |
|---|------------|----------------|------|--------|-----------------|-----------------|--------|-------|
| 11 | gitops_workflow_analysis.md | Multi-Tool Comparison Pattern | DS-53 | DS | No — NEW | ST-22 | MATCHED-EXISTING | DS-53 absent from master index. Parallel implementations for different tools solving the same problem maps to ST-22 "Multi-Solution Comparison Matrix" (side-by-side comparison of competing approaches) |
| 12 | gitops_workflow_analysis.md | Progressive Delivery Patterns | DS-54 | DS | No — NEW | AG-15 | MATCHED-EXISTING | DS-54 absent from master index. Canary/blue-green strategies with quantitative parameters maps to AG-15 "Staged Rollout with Automatic Rollback" (progressive deployment with quality monitoring and rollback triggers) |
| 13 | gitops_workflow_analysis.md | Principle-Driven Instructions | ST-31 | ST | No — NEW | ST-35 | MATCHED-EXISTING | ST-31 absent from master index. Starting with foundational principles before implementation details maps directly to ST-35 "Principle-Based Guidance" (define explicit principles that govern all recommendations) |
| 14 | gitops_workflow_analysis.md | Repository Structure Templates | DS-55 | DS | No — NEW | — | CONFIRMED-NOVEL | DS-55 absent from master index. ASCII directory tree templates showing organizational patterns for project structure is a distinct visual documentation technique not captured by AG-05 (concrete deliverables) or DS-05 (visualization guidance) |
| 15 | gitops_workflow_analysis.md | Sync Policy Configuration | DS-56 | DS | No — NEW | DS-24 | MATCHED-EXISTING | CODE COLLISION: DS-56 is "PostgreSQL Data Type Selection Matrix" in master index. Comprehensive configuration documentation with inline comments maps to DS-24 "API Reference Bundling" (comprehensive documentation to enable autonomous tool usage) |
| 16 | gitops_workflow_analysis.md | Health Assessment Customization | DS-57 | DS | No — NEW | DS-02 | MATCHED-EXISTING | DS-57 absent from master index. Custom health check definitions with programmatic "healthy" criteria maps to DS-02 "Metric Specification" (define specific, measurable criteria) applied to health assessment |
| 17 | gitops_workflow_analysis.md | Reference Pointers with Context | — | IT | Yes — IT-20 | IT-19 | MATCHED-EXISTING | IT-20 absent from master index. Inline pointers to bundled references with contextual guidance maps to IT-19 "Three-Tier Information Loading" (Metadata → SKILL.md → Bundled resources with progressive disclosure) |
| 18 | gitops_workflow_analysis.md | Best Practices Enumeration | DS-58 | DS | No — NEW | ST-35 | MATCHED-EXISTING | DS-58 absent from master index. Numbered lists of best practices with bold key phrase + explanation maps to ST-35 "Principle-Based Guidance" (define explicit principles that govern all recommendations) |
| 19 | gitops_workflow_analysis.md | Troubleshooting Command Sequences | DS-59 | DS | No — NEW | — | CONFIRMED-NOVEL | DS-59 absent from master index. Diagnostic command → fix command structure (Problem → Investigation → Fix) is a distinct troubleshooting documentation pattern not captured by DS-03 "Tool and Methodology Suggestions" or RT-01 chain-of-thought |
| 20 | gitops_workflow_analysis.md | Environment-Specific Guidance | DS-60 | DS | No — NEW | — | CONFIRMED-NOVEL | DS-60 absent from master index. Different recommendations based on environment risk tolerance (non-prod vs prod) is a distinct context-branching pattern not fully captured by OC-04 "Conditional Output Logic" or OC-08 "Multi-Mode Architecture" |
| 21 | gitops_workflow_analysis.md | App of Apps Pattern | — | DS | Yes — DS-04 | DT-01 | MATCHED-EXISTING | DS-04 is "Pattern Recognition Requests" — wrong mapping. Meta-application managing other applications via recursive structure maps to DT-01 "Hierarchical Task Breakdown" (break complex tasks into phases and subtasks) applied to application management |

---

## File 3: i_os_app_developer_analysis.md (10 techniques)

| # | Source File | Technique Name | Code | Family | Original Mapping | Verified Mapping | Status | Notes |
|---|------------|----------------|------|--------|-----------------|-----------------|--------|-------|
| 22 | i_os_app_developer_analysis.md | Critical Warnings Table | DS-62 | DS | No — NEW | — | CONFIRMED-NOVEL | DS-62 absent from master index. Upfront table of catastrophic issues (cause + solution) placed immediately after title is a distinct documentation pattern — differs from DS-06 "Prioritization and Severity Guidance" (general ranking) and AG-09 "Anti-Pattern Embedding" (embedded in agent identity) |
| 23 | i_os_app_developer_analysis.md | Quick Reference Command Table | DS-63 | DS | No — NEW | DS-03 | MATCHED-EXISTING | DS-63 absent from master index. Essential commands in task-command table format maps to DS-03 "Tool and Methodology Suggestions" (recommend specific tools or approaches) presented in tabular format |
| 24 | i_os_app_developer_analysis.md | Version Compatibility Matrix | DS-64 | DS | No — NEW | DS-107 | MATCHED-EXISTING | DS-64 absent from master index. API changes organized by version with before/after code maps to DS-107 "Version-Specific Expertise" (define expertise for specific language AND framework versions) |
| 25 | i_os_app_developer_analysis.md | Free vs. Paid Feature Matrix | DS-65 | DS | No — NEW | ST-22 | MATCHED-EXISTING | DS-65 absent from master index. Licensing/account tier comparison table maps to ST-22 "Multi-Solution Comparison Matrix" (side-by-side comparison with objective criteria) applied to feature tiers |
| 26 | i_os_app_developer_analysis.md | Platform Limitation Warnings | IT-32 | IT | No — NEW | CM-02 | MATCHED-EXISTING | IT-32 absent from master index. Explicit "this won't work here" warnings for platform constraints maps to CM-02 "Constraint Specification" (explicit must/must-not requirements). CODE COLLISION: IT-32 also assigned to #35 "Symptom-Based Troubleshooting" |
| 27 | i_os_app_developer_analysis.md | Root Cause Explanation | DS-66 | DS | No — NEW | — | CONFIRMED-NOVEL | DS-66 absent from master index. Root cause → symptom → explanation → fix structure is a distinct 4-part documentation pattern — related to DT-04 "Multi-Layer Analysis" but has a specific reverse-engineering format not captured by existing techniques |
| 28 | i_os_app_developer_analysis.md | Debug Logging Pattern | DS-67 | DS | No — NEW | — | CONFIRMED-NOVEL | DS-67 absent from master index. Structured logging with subsystem categorization and state transition logging is a distinct domain-specific instrumentation pattern not captured by DS-02 "Metric Specification" or ST-05 "Hierarchical Organization" |
| 29 | i_os_app_developer_analysis.md | Correct vs. Incorrect Code Pattern | ST-34 | ST | No — NEW | NE-04 | MATCHED-EXISTING | ST-34 absent from master index. WRONG/CORRECT inline comments showing common mistakes alongside safe alternatives maps to NE-04 "Good vs Bad Example Calibration" (explicit contrast pairs to calibrate quality). CODE COLLISION: ST-34 also assigned to #36 "Principle-Based Guidance" |
| 30 | i_os_app_developer_analysis.md | One-Time Manual Fix Documentation | IT-33 | IT | No — NEW | — | CONFIRMED-NOVEL | IT-33 absent from master index. Explicit "manual, one-time per project" instructions for tool limitations with persistence explanation is a distinct workaround documentation pattern — related to RT-08 "Workaround Cost Analysis" but focused on one-time fixes, not ongoing costs |
| 31 | i_os_app_developer_analysis.md | Deployment Target Migration Checklist | DS-68 | DS | No — NEW | ST-02 | MATCHED-EXISTING | DS-68 absent from master index. Step-by-step guide for changing platform versions (config → compatibility → regenerate) maps to ST-02 "Structured Sequential Instructions" (numbered step-by-step instructions) applied to migration |

---

## File 4: repomix_unmixer_analysis.md (10 techniques)

| # | Source File | Technique Name | Code | Family | Original Mapping | Verified Mapping | Status | Notes |
|---|------------|----------------|------|--------|-----------------|-----------------|--------|-------|
| 32 | repomix_unmixer_analysis.md | Multi-Format Auto-Detection | DS-85 | DS | No — NEW | — | CONFIRMED-NOVEL | DS-85 absent from master index. Auto-detecting input format (XML, JSON, Markdown) using content signatures and routing to appropriate parser is a distinct technique — differs from DT-06 "Typography Decision Tree" (binary yes/no questions for human classification) in that it uses automated content signature matching |
| 33 | repomix_unmixer_analysis.md | Format-Specific Extraction Patterns | DS-86 | DS | No — NEW | — | CONFIRMED-NOVEL | DS-86 absent from master index. Different regex/parsing per format with consistent extraction interface (polymorphic processing) is a distinct implementation pattern not captured by existing techniques — implements the strategy pattern for content processing |
| 34 | repomix_unmixer_analysis.md | Validation Workflow Layering | QA-21 | QA | No — NEW | QA-08 | EXTENDS-EXISTING | QA-21 absent from master index. Multi-tiered validation (extraction → structure → content → semantic → automated → readiness) extends QA-08 "Gate-Based Verification" with a detailed multi-tier structure — more granular than QA-08's general gate concept |
| 35 | repomix_unmixer_analysis.md | Symptom-Based Troubleshooting | IT-32 | IT | No — NEW | — | CONFIRMED-NOVEL | IT-32 absent from master index. Organizing troubleshooting by observable symptom rather than root cause (what user sees → possible causes → fix) is a distinct organizational technique. CODE COLLISION: IT-32 also assigned to #26 "Platform Limitation Warnings" |
| 36 | repomix_unmixer_analysis.md | Principle-Based Guidance | ST-34 | ST | No — NEW | ST-35 | MATCHED-EXISTING | ST-34 absent from master index. Organizing best practices as named principles with good/bad examples maps directly to ST-35 "Principle-Based Guidance" (define explicit principles that govern all recommendations). CODE COLLISION: ST-34 also assigned to #29 "Correct vs. Incorrect Code Pattern" |
| 37 | repomix_unmixer_analysis.md | Format Specification Reference | DS-87 | DS | No — NEW | DS-24 | MATCHED-EXISTING | DS-87 absent from master index. Comprehensive format documentation with regex patterns, examples, edge cases, and versioning maps to DS-24 "API Reference Bundling" (include comprehensive documentation to enable autonomous tool usage) |
| 38 | repomix_unmixer_analysis.md | Automated Validation Script Template | DS-88 | DS | No — NEW | AG-05 | MATCHED-EXISTING | DS-88 absent from master index. Complete, copy-paste-ready automation scripts embedded as documentation maps to AG-05 "Concrete Deliverable Templates" (include actual working code/examples, not placeholder templates) |
| 39 | repomix_unmixer_analysis.md | Quality Assurance Checklist | QA-22 | QA | No — NEW | QA-10 | MATCHED-EXISTING | QA-22 absent from master index. Hierarchical checklist with checkboxes for tracking verification steps maps to QA-10 "Test Battery Protocol" (systematic pre-ship testing checklist with specific tests) |
| 40 | repomix_unmixer_analysis.md | Auto-Creating Directory Structure | DS-89 | DS | No — NEW | — | NEEDS-REVIEW | DS-89 absent from master index. Automatically creating parent directories during file write operations may be too implementation-specific to qualify as a general prompting technique — needs evaluation in consolidation step |
| 41 | repomix_unmixer_analysis.md | Progressive Disclosure with Format References | — | IT | Yes — IT-14 | IT-19 | MATCHED-EXISTING | IT-14 absent from master index. SKILL.md providing workflow with references providing deep format knowledge (83% in references) maps to IT-19 "Three-Tier Information Loading" (Metadata → SKILL.md → Bundled resources with progressive disclosure) |

---

## Code Collisions Found

| Collision Code | Entry # | Technique Name | Source File | Resolution |
|---------------|---------|----------------|-------------|------------|
| DS-24 | #2 | Multi-Stage Validation Pipeline | skill_creator_analysis.md | DS-24 is "API Reference Bundling" in master index — technique remapped to QA-08 |
| QA-09 | #3 | Content-Based Integrity Validation | skill_creator_analysis.md | QA-09 is "Reversibility Assessment" in master index — technique is novel, needs new code |
| DS-56 | #15 | Sync Policy Configuration | gitops_workflow_analysis.md | DS-56 is "PostgreSQL Data Type Selection Matrix" in master index — technique remapped to DS-24 |
| IT-32 | #26, #35 | Platform Limitation Warnings / Symptom-Based Troubleshooting | i_os_app_developer / repomix_unmixer | Two different techniques in this batch share code IT-32 — #26 remapped to CM-02, #35 is novel |
| ST-34 | #29, #36 | Correct vs. Incorrect Code / Principle-Based Guidance | i_os_app_developer / repomix_unmixer | Two different techniques in this batch share code ST-34 — #29 remapped to NE-04, #36 remapped to ST-35 |

---

## Batch Summary

| Status | Count | Percentage |
|--------|-------|------------|
| CONFIRMED-EXISTING | 1 | 2.4% |
| MATCHED-EXISTING | 24 | 58.5% |
| EXTENDS-EXISTING | 1 | 2.4% |
| CONFIRMED-NOVEL | 14 | 34.1% |
| NEEDS-REVIEW | 1 | 2.4% |
| **Total** | **41** | **100%** |

### Novel Techniques Summary (14)

| # | Technique Name | Source File | Brief Description |
|---|----------------|-------------|-------------------|
| 3 | Content-Based Integrity Validation | skill_creator_analysis.md | Hash-based change detection to invalidate stale security approvals |
| 4 | Template-Based Educational Scaffolding | skill_creator_analysis.md | Code templates with embedded TODO markers, contextual examples, and deletion instructions |
| 5 | CLI-First Executable Documentation | skill_creator_analysis.md | Scripts serving dual purpose as documentation and executable tools |
| 6 | Layered Security Validation | skill_creator_analysis.md | Multi-tool security scanning combining industry standards with custom patterns |
| 14 | Repository Structure Templates | gitops_workflow_analysis.md | ASCII directory tree templates showing organizational patterns |
| 19 | Troubleshooting Command Sequences | gitops_workflow_analysis.md | Problem → Investigation → Fix diagnostic command structure |
| 20 | Environment-Specific Guidance | gitops_workflow_analysis.md | Different recommendations based on environment risk tolerance |
| 22 | Critical Warnings Table | i_os_app_developer_analysis.md | Upfront table of catastrophic issues placed immediately after title |
| 27 | Root Cause Explanation | i_os_app_developer_analysis.md | Root cause → symptom → explanation → fix 4-part structure |
| 28 | Debug Logging Pattern | i_os_app_developer_analysis.md | Structured logging with subsystem categorization and state transitions |
| 30 | One-Time Manual Fix Documentation | i_os_app_developer_analysis.md | "Manual, one-time per project" instructions for tool limitations |
| 32 | Multi-Format Auto-Detection | repomix_unmixer_analysis.md | Auto-detect input format using content signatures and route to parser |
| 33 | Format-Specific Extraction Patterns | repomix_unmixer_analysis.md | Polymorphic processing with consistent extraction interface |
| 35 | Symptom-Based Troubleshooting | repomix_unmixer_analysis.md | Organize troubleshooting by observable symptom, not root cause |

### Existing Technique Matches (Most Frequent Targets)

| Master Index Technique | Times Matched | Entries |
|----------------------|---------------|---------|
| ST-35 Principle-Based Guidance | 3 | #13, #18, #36 |
| OC-08 Multi-Mode Prompt Architecture | 2 | #7, #10 |
| ST-22 Multi-Solution Comparison Matrix | 2 | #11, #25 |
| ST-02 Structured Sequential Instructions | 2 | #8, #31 |
| DS-24 API Reference Bundling | 2 | #15, #37 |
| CM-02 Constraint Specification | 2 | #9, #26 |
| IT-19 Three-Tier Information Loading | 2 | #17, #41 |
| QA-08 Gate-Based Verification | 2 | #2, #34 (one MATCHED, one EXTENDS) |

### By Source File

| Source File | Total | CONFIRMED-EXISTING | MATCHED-EXISTING | EXTENDS-EXISTING | CONFIRMED-NOVEL | NEEDS-REVIEW |
|------------|-------|-------------------|-----------------|-----------------|----------------|-------------|
| skill_creator_analysis.md | 10 | 1 | 5 | 0 | 4 | 0 |
| gitops_workflow_analysis.md | 11 | 0 | 8 | 0 | 3 | 0 |
| i_os_app_developer_analysis.md | 10 | 0 | 5 | 0 | 5 | 0 |
| repomix_unmixer_analysis.md | 10 | 0 | 6 | 1 | 2 | 1 |
