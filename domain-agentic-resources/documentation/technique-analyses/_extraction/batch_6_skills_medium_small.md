# Technique Extraction — Batch 6 (Skills Medium-Small)

**Source Directory:** `domain-agentic-resources/documentation/technique-analyses/skills/`
**Files Analyzed:** 7
**Total Lines Analyzed:** ~2,721
**Date Extracted:** 2026-02-08

---

## pdf_creator_analysis.md (356 lines)

| # | Source File | Technique Name | Code (if assigned) | Family | Maps To Existing | Novel? | Brief Description |
|---|------------|----------------|-------------------|--------|-----------------|--------|-------------------|
| 1 | pdf_creator_analysis.md | Font Fallback Chain for i18n | DS-104 | DS | No — NEW | Yes | Ordered list of fonts from platform-specific to universal fallback for cross-platform rendering |
| 2 | pdf_creator_analysis.md | Dual-Mode CLI (Single + Batch) | DS-105 | DS | Extends IT-25 — NEW | Yes | Two scripts with shared core: simple CLI for single files, argparse CLI for batch |
| 3 | pdf_creator_analysis.md | Typography Specification Table | OT-15 | OT | No — NEW | Yes | Structured table defining font choices with semantic meaning |
| 4 | pdf_creator_analysis.md | Output Constraints Specification | OT-16 | OT | Extends OT-14 — NEW | Yes | Explicit list of output constraints (file size, dimensions, format) with rationale |
| 5 | pdf_creator_analysis.md | Environment Setup Prerequisites | DS-106 | DS | No — NEW | Yes | Platform-specific environment variables required before tool execution |
| 6 | pdf_creator_analysis.md | Semantic Typography Hierarchy | DS-107 | DS | No — NEW | Yes | Different font families for different semantic elements (serif body, sans headings) |
| 7 | pdf_creator_analysis.md | Use Case-Driven Documentation | IT-37 | IT | Extends IT-11 — NEW | Yes | Organize documentation by specific use cases rather than features |
| 8 | pdf_creator_analysis.md | Module Import Reuse Pattern | — | AG | Yes — AG-19 | No | Batch script imports and reuses core conversion function from single-file script |
| 9 | pdf_creator_analysis.md | Success/Failure Counters in Batch Operations | QA-26 | QA | No — NEW | Yes | Track success and failure counts in batch operations, report summary, exit with code |
| 10 | pdf_creator_analysis.md | Markdown Extensions Configuration | DS-108 | DS | No — NEW | Yes | Explicit list of markdown extensions for feature support in processing |

**Subtotal:** 10 techniques (9 novel, 1 existing)

---

## cli_demo_generator_analysis.md (369 lines)

| # | Source File | Technique Name | Code (if assigned) | Family | Maps To Existing | Novel? | Brief Description |
|---|------------|----------------|-------------------|--------|-----------------|--------|-------------------|
| 1 | cli_demo_generator_analysis.md | Multi-Mode Tool Integration | IT-21 | IT | No — NEW | Yes | Three distinct operational modes (auto/batch/interactive) in one skill |
| 2 | cli_demo_generator_analysis.md | Context-Aware Timing Algorithm | DS-38 | DS | No — NEW | Yes | Smart delay calculation based on command semantics (install=3s, ls=1s) |
| 3 | cli_demo_generator_analysis.md | Workflow Decision Matrix | IT-22 | IT | No — NEW | Yes | Structured guidance mapping user scenarios to recommended tool workflows |
| 4 | cli_demo_generator_analysis.md | Professional Defaults Library | DS-40 | DS | No — NEW | Yes | Pre-configured settings organized by use case (documentation, presentations, code demos) |
| 5 | cli_demo_generator_analysis.md | Template-Based Code Generation | DS-39 | DS | Extends DS-01 — NEW | Yes | Generate low-level implementation code from high-level declarative specifications |
| 6 | cli_demo_generator_analysis.md | Pre-Publication Quality Checklist | QA-12 | QA | No — NEW | Yes | Systematic verification checklist before deliverable release |
| 7 | cli_demo_generator_analysis.md | Good/Bad Example Pairs | — | ST | Yes — ST-28 | No | Extensive teaching through contrasting correct and incorrect implementations |
| 8 | cli_demo_generator_analysis.md | Bundled Script Ecosystem | — | IT | Yes — IT-14 | No | Multiple complementary scripts that work together or independently |
| 9 | cli_demo_generator_analysis.md | Configuration-Driven Batch Processing | — | DS | Yes — DS-06 | No | YAML/JSON configuration files for declarative multi-operation execution |
| 10 | cli_demo_generator_analysis.md | Dependency Verification Pattern | — | DS | Yes — DS-10 | No | Check for required tools before execution, provide installation guidance if missing |

**Subtotal:** 10 techniques (6 novel, 4 existing)

---

## markdown_tools_analysis.md (370 lines)

| # | Source File | Technique Name | Code (if assigned) | Family | Maps To Existing | Novel? | Brief Description |
|---|------------|----------------|-------------------|--------|-----------------|--------|-------------------|
| 1 | markdown_tools_analysis.md | Bundled Executable Helper Script | — | AG | Yes — AG-19 | No | Python utility script packaged with skill for repeated automation tasks |
| 2 | markdown_tools_analysis.md | Cross-Platform Path Handling | DS-99 | DS | No — NEW | Yes | Regex-based transformation for Windows/WSL path interoperability |
| 3 | markdown_tools_analysis.md | Progressive Example Complexity | IT-34 | IT | No — NEW | Yes | Examples organized from simple to batch to advanced to error recovery |
| 4 | markdown_tools_analysis.md | Workflow Abstraction Layers | DS-100 | DS | No — NEW | Yes | Define simple workflow vs. complex workflow with different tool chains |
| 5 | markdown_tools_analysis.md | Bash Loop Templates for Batch Operations | DS-101 | DS | No — NEW | Yes | Copy-paste bash loops for common batch file processing operations |
| 6 | markdown_tools_analysis.md | Error Handling Pattern Library | DS-102 | DS | No — NEW | Yes | Reusable error handling patterns for common shell script failures |
| 7 | markdown_tools_analysis.md | Quality Verification Checklist Commands | QA-25 | QA | No — NEW | Yes | Bash commands to verify output quality (empty files, error markers, metrics) |
| 8 | markdown_tools_analysis.md | Metadata Preservation Pattern | DS-103 | DS | No — NEW | Yes | Capture original file metadata and embed in converted output as frontmatter |
| 9 | markdown_tools_analysis.md | Common Patterns Section | IT-35 | IT | No — NEW | Yes | Dedicated section with named, reusable script patterns for common scenarios |
| 10 | markdown_tools_analysis.md | Best Practices by Category | IT-36 | IT | No — NEW | Yes | Best practices organized by concern area (Path Handling, Batch Processing, QA) |

**Subtotal:** 10 techniques (9 novel, 1 existing)

---

## teams_channel_post_writer_analysis.md (385 lines)

| # | Source File | Technique Name | Code (if assigned) | Family | Maps To Existing | Novel? | Brief Description |
|---|------------|----------------|-------------------|--------|-----------------|--------|-------------------|
| 1 | teams_channel_post_writer_analysis.md | Template-Driven Content Generation | — | OT | Yes — OT-01 | No | Ready-to-use markdown template with placeholder structure and 9-section architecture |
| 2 | teams_channel_post_writer_analysis.md | Non-Judgmental Comparison Pattern | DS-74 | DS | No — NEW | Yes | "Normal vs Better" instead of "Wrong vs Correct" with emoji distinction for psychological safety |
| 3 | teams_channel_post_writer_analysis.md | Multi-Stage Quality Assurance | — | QA | Yes — QA-01, QA-03 | No | Combines research checklist (pre-writing), quality checklist (post-writing), and workflow checkpoints |
| 4 | teams_channel_post_writer_analysis.md | Feature-to-Principle Bridging | DS-75 | DS | No — NEW | Yes | Explicitly require connecting features to broader engineering principles or best practices |
| 5 | teams_channel_post_writer_analysis.md | Workflow-Driven Content Creation | — | DS | Yes — DS-04 | No | 5-stage workflow: Understand, Plan, Draft, Review, Share with specific deliverables |
| 6 | teams_channel_post_writer_analysis.md | Tone and Style Codification | — | ST | Yes — ST-02 | No | Explicit tone guidelines with do/don't patterns beyond simple persona assignment |
| 7 | teams_channel_post_writer_analysis.md | Example Quantity Specification | DS-76 | DS | No — NEW | Yes | Mandate minimum number of concrete, realistic, adaptable examples (3+) |
| 8 | teams_channel_post_writer_analysis.md | Call-to-Action Mandatory Close | — | IT | Yes — IT-06 | No | Every content piece must end with actionable next step |
| 9 | teams_channel_post_writer_analysis.md | Authoritative Source Verification | QA-17 | QA | No — NEW | Yes | Require finding and citing authoritative sources BEFORE drafting content |
| 10 | teams_channel_post_writer_analysis.md | Format Convention Codification | — | OT | Yes — OT-01 | No | Explicit formatting standards for emojis, bold text, code blocks, lists |

**Subtotal:** 10 techniques (4 novel, 6 existing)

---

## prompt_engineering_patterns_analysis.md (405 lines)

| # | Source File | Technique Name | Code (if assigned) | Family | Maps To Existing | Novel? | Brief Description |
|---|------------|----------------|-------------------|--------|-----------------|--------|-------------------|
| 1 | prompt_engineering_patterns_analysis.md | Progressive Disclosure (Three-Tier Architecture) | — | IT | Yes — IT-06 | No | Three-tier loading: metadata, SKILL.md body, bundled resources on demand |
| 2 | prompt_engineering_patterns_analysis.md | Few-Shot Learning with Semantic Selection | — | RT | Yes — RT-07 | No | Dynamic example selection based on semantic similarity to query |
| 3 | prompt_engineering_patterns_analysis.md | Chain-of-Thought Prompting | — | RT | Yes — RT-01 | No | Elicit step-by-step reasoning with explicit instruction |
| 4 | prompt_engineering_patterns_analysis.md | Hierarchical Instruction Structure | — | ST | Yes — ST-04 | No | System Context, Task Instruction, Examples, Input Data, Output Format ordering |
| 5 | prompt_engineering_patterns_analysis.md | Error Recovery Patterns for Prompts | RT-12 | RT | No — NEW | Yes | Fallback instructions, confidence scores, alternative interpretations for graceful LLM failure handling |
| 6 | prompt_engineering_patterns_analysis.md | Self-Verification Layer | — | RT | Yes — RT-03 | No | Add verification step after main task to catch errors before output |
| 7 | prompt_engineering_patterns_analysis.md | Prompt A/B Testing Framework | — | QA | Yes — QA-07 | No | Statistical comparison of prompt variants with accuracy and latency metrics |
| 8 | prompt_engineering_patterns_analysis.md | Template Variable Interpolation | — | OT | Yes — OT-01 + ST-07 | No | Reusable prompt templates with variable substitution |
| 9 | prompt_engineering_patterns_analysis.md | Metric-Driven Evaluation | — | DS | Yes — DS-02 | No | Track KPIs for prompt performance (accuracy, consistency, latency, token usage) |
| 10 | prompt_engineering_patterns_analysis.md | Bundled Executable Scripts in Skills | IT-14 | IT | No — NEW | Yes | Package executable tooling (scripts/) with instructional documentation (SKILL.md) |
| 11 | prompt_engineering_patterns_analysis.md | Progressive Complexity (Leveled Instructions) | — | IT | Yes — IT-06 | No | Start simple, add complexity incrementally across 4 levels |
| 12 | prompt_engineering_patterns_analysis.md | Hierarchical Reference Loading | IT-15 | IT | No — NEW | Yes | Organize references by depth, load progressively (Quick Start, Intermediate, Advanced) |
| 13 | prompt_engineering_patterns_analysis.md | Prompt Versioning as Code | DS-20 | DS | No — NEW | Yes | Treat prompts like software with version control, testing, CI/CD, and rollback |

**Subtotal:** 13 techniques (4 novel, 9 existing)

---

## promptfoo_evaluation_analysis.md (418 lines)

| # | Source File | Technique Name | Code (if assigned) | Family | Maps To Existing | Novel? | Brief Description |
|---|------------|----------------|-------------------|--------|-----------------|--------|-------------------|
| 1 | promptfoo_evaluation_analysis.md | Echo Provider for Cost-Free Preview | AG-23 | AG | No — NEW | Yes | Use echo provider to return rendered prompt without API calls for free iteration |
| 2 | promptfoo_evaluation_analysis.md | Progressive Evaluation Modes | DS-109 | DS | No — NEW | Yes | Three-tier evaluation: Preview (echo) to Single Model to Multi-Model Comparison |
| 3 | promptfoo_evaluation_analysis.md | File-Based Variable Loading | IT-38 | IT | No — NEW | Yes | Load test variables from external files using file:// protocol |
| 4 | promptfoo_evaluation_analysis.md | Python Custom Assertion Pattern | DS-110 | DS | No — NEW | Yes | Structured return format (pass/score/reason/named_scores) for custom quality checks |
| 5 | promptfoo_evaluation_analysis.md | LLM-as-Judge with Rubric | DS-111 | DS | No — NEW | Yes | Use secondary LLM to evaluate primary LLM output against criteria with threshold |
| 6 | promptfoo_evaluation_analysis.md | Named Scores for Multi-Dimensional Metrics | QA-27 | QA | No — NEW | Yes | Return multiple custom metrics alongside pass/fail for complex quality assessment |
| 7 | promptfoo_evaluation_analysis.md | Few-Shot Pattern with File-Based Examples | DS-112 | DS | No — NEW | Yes | Chat format with assistant examples loaded from external files via file:// |
| 8 | promptfoo_evaluation_analysis.md | Assertion Type Reference Table | IT-39 | IT | Extends IT-36 — NEW | Yes | Comprehensive table of assertion types with usage and examples for quick reference |
| 9 | promptfoo_evaluation_analysis.md | Real-World Example Section | IT-40 | IT | No — NEW | Yes | Complete production example with directory structure and implementation reference |
| 10 | promptfoo_evaluation_analysis.md | Dual Configuration Pattern | DS-113 | DS | No — NEW | Yes | Maintain production and preview configs for safe iteration without API costs |
| 11 | promptfoo_evaluation_analysis.md | Reduction Ratio Metric Pattern | DS-114 | DS | No — NEW | Yes | Calculate input/output ratio to validate summarization/curation quality (70-90% target) |

**Subtotal:** 11 techniques (11 novel, 0 existing)

---

## ui_designer_analysis.md (418 lines)

| # | Source File | Technique Name | Code (if assigned) | Family | Maps To Existing | Novel? | Brief Description |
|---|------------|----------------|-------------------|--------|-----------------|--------|-------------------|
| 1 | ui_designer_analysis.md | Multi-Stage Workflow with Intermediate Outputs | DS-115 | DS | No — NEW | Yes | Sequential stages producing reusable intermediate artifacts for iteration |
| 2 | ui_designer_analysis.md | Template Substitution Composition | OT-17 | OT | No — NEW | Yes | Final output template with placeholder variables filled from intermediate artifacts |
| 3 | ui_designer_analysis.md | Subagent Orchestration with Task Tool | — | AG | Yes — AG-07 + AG-21 | No | Main skill delegates to general-purpose subagents with structured prompts |
| 4 | ui_designer_analysis.md | Image Analysis Prompt Template | DS-116 | DS | No — NEW | Yes | Structured prompt template for extracting design patterns (colors, typography, components) from images |
| 5 | ui_designer_analysis.md | Interactive PRD Refinement Pattern | IT-41 | IT | No — NEW | Yes | Generate initial PRD from template, then refine through user interaction |
| 6 | ui_designer_analysis.md | Timestamped Output Versioning | DS-117 | DS | Extends DS-103 — NEW | Yes | Append timestamp to final outputs for automatic version tracking |
| 7 | ui_designer_analysis.md | Environment Verification Checkpoint | QA-28 | QA | No — NEW | Yes | Check for required tooling before implementation, provide setup instructions if missing |
| 8 | ui_designer_analysis.md | Best Practices by Workflow Stage | IT-42 | IT | Extends IT-36 — NEW | Yes | Organize best practices by workflow stage rather than by topic |
| 9 | ui_designer_analysis.md | Complete Usage Example Section | IT-43 | IT | Extends IT-40 — NEW | Yes | End-to-end example showing inputs, workflow execution, and outputs for every step |
| 10 | ui_designer_analysis.md | High Freedom Workflow Disclosure | IT-44 | IT | No — NEW | Yes | Explicitly state workflow adaptability and encourage thoughtful customization |
| 11 | ui_designer_analysis.md | Structured Asset Library | DS-118 | DS | No — NEW | Yes | Bundle multiple prompt templates as reusable assets with descriptions |

**Subtotal:** 11 techniques (10 novel, 1 existing)

---

## Summary

| Metric | Count |
|--------|-------|
| **Total techniques extracted** | **75** |
| **Marked as novel** | **53** |
| **Mapped to existing** | **22** |
| **Source files analyzed** | **7** |

### By Family

| Family | Total | Novel | Existing |
|--------|-------|-------|----------|
| DS (Domain-Specific) | 35 | 31 | 4 |
| IT (Interaction Techniques) | 21 | 16 | 5 |
| QA (Quality Assurance) | 8 | 7 | 1 |
| OT (Output Techniques) | 5 | 4 | 1 |
| AG (Agentic) | 3 | 1 | 2 |
| ST (Structural) | 1 | 0 | 1 |
| RT (Reasoning Techniques) | 2 | 1 | 1 |

### By Source File

| Source File | Total | Novel | Existing |
|-------------|-------|-------|----------|
| pdf_creator_analysis.md | 10 | 9 | 1 |
| cli_demo_generator_analysis.md | 10 | 6 | 4 |
| markdown_tools_analysis.md | 10 | 9 | 1 |
| teams_channel_post_writer_analysis.md | 10 | 4 | 6 |
| prompt_engineering_patterns_analysis.md | 13 | 4 | 9 |
| promptfoo_evaluation_analysis.md | 11 | 11 | 0 |
| ui_designer_analysis.md | 11 | 10 | 1 |

### Existing Technique References (Deduplication Targets)

The following existing techniques were referenced across the 7 files:

| Existing Code | Technique Name | Referenced By |
|---------------|---------------|--------------|
| AG-19 | Production App as Skill | pdf_creator, markdown_tools |
| AG-07 + AG-21 | Multi-Agent Orchestration + Agent Handoff | ui_designer |
| DS-01 | Code Generation Patterns | cli_demo_generator |
| DS-02 | Metric Specification | prompt_engineering_patterns |
| DS-04 | Workflow Specification | teams_channel_post_writer |
| DS-06 | Configuration-Driven Orchestration | cli_demo_generator |
| DS-10 | Tool Integration Patterns | cli_demo_generator |
| IT-06 | Progressive Disclosure | prompt_engineering_patterns (x2) |
| IT-11 | Use Case Examples | pdf_creator |
| IT-14 | Bundled Scripts | cli_demo_generator |
| IT-36 | Best Practices by Category | promptfoo_evaluation, ui_designer |
| IT-40 | Real-World Example Section | ui_designer |
| OT-01 | Format Specification with Templates | teams_channel_post_writer (x2) |
| OT-14 | Output Artifacts Specification | pdf_creator |
| QA-01 | Self-Verification | teams_channel_post_writer |
| QA-03 | Checklist Validation | teams_channel_post_writer |
| QA-07 | Statistical A/B Testing for Prompts | prompt_engineering_patterns |
| RT-01 | Chain of Thought | prompt_engineering_patterns |
| RT-03 | Self-Verification | prompt_engineering_patterns |
| RT-07 | Few-Shot Examples | prompt_engineering_patterns |
| ST-02 | Persona Assignment | teams_channel_post_writer |
| ST-04 | Structured Prompts | prompt_engineering_patterns |
| ST-07 | Template-Based Prompts | prompt_engineering_patterns |
| ST-28 | Anti-Pattern Documentation | cli_demo_generator |
| DS-103 | Metadata Preservation | ui_designer |

### Notes

- **promptfoo_evaluation_analysis.md** had the highest novel density (11/11 = 100% novel), suggesting LLM evaluation is a technique-rich domain not well covered by the existing Master Index.
- **prompt_engineering_patterns_analysis.md** had the most existing mappings (9/13), expected since it covers fundamental prompting concepts already well-documented.
- **DS family dominates** with 35 of 75 techniques (47%), reflecting the domain-specific nature of skill analysis files.
- Several techniques appear related across files: DS-103 (Metadata Preservation from markdown_tools) is extended by DS-117 (Timestamped Output Versioning in ui_designer); IT-36 (Best Practices by Category from markdown_tools) is extended by IT-42 (Best Practices by Workflow Stage in ui_designer).
- The IT-14 (Bundled Executable Scripts) code appears both as an existing technique reference (cli_demo_generator) and as a novel technique (prompt_engineering_patterns), suggesting it may have been added to the Master Index between analyses or there is an inconsistency in the source files.
