# Technique Analysis: promptfoo-evaluation

**Resource Type:** Skill
**Path:** `claude-code-resources/skills/llm-application-dev/promptfoo-evaluation/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 642 lines (1 reference: promptfoo_api.md)
**Complexity:** 5/5 (LLM evaluation framework with custom assertions, few-shot patterns, echo provider)

## Overview

The `promptfoo-evaluation` skill provides comprehensive guidance for LLM evaluation using Promptfoo, an open-source framework for testing and comparing LLM outputs. It demonstrates sophisticated testing patterns including echo provider for cost-free previews, Python custom assertions, LLM-as-judge, and advanced few-shot implementations.

**Key Innovation:** Echo provider pattern enables cost-free prompt rendering preview before expensive API calls, combined with file-based variable loading for large-scale evaluations.

## Identified Techniques

### Technique 1: Echo Provider for Cost-Free Preview
- **Category:** AG (Agentic - LLM Testing)
- **Pattern:** Use echo provider to return rendered prompt without API calls
- **Example from resource:**
```yaml
# promptfooconfig-preview.yaml
providers:
  - echo  # Returns prompt as output, no API calls
```
- **Maps to existing:** NEW - **AG-23 Echo Provider for Cost-Free Preview**
- **Effectiveness:** Verify prompt rendering, variable substitution, few-shot structure without consuming API tokens

### Technique 2: Progressive Evaluation Modes
- **Category:** DS (Domain-Specific - LLM Testing)
- **Pattern:** Three evaluation modes: Preview (echo) → Single Model → Multi-Model Comparison
- **Example from resource:**
```bash
# Mode 1: Preview (free, echo provider)
npx promptfoo eval --config promptfooconfig-preview.yaml

# Mode 2: Single model validation
providers: [anthropic:claude-sonnet-4-5]

# Mode 3: A/B comparison
providers: [anthropic:claude-sonnet-4-5, openai:gpt-4.1]
```
- **Maps to existing:** NEW - **DS-109 Progressive Evaluation Modes**
- **Effectiveness:** Iterate quickly with echo, validate with single model, compare with A/B before production

### Technique 3: File-Based Variable Loading
- **Category:** IT (Interaction Techniques)
- **Pattern:** Load test variables from external files using `file://` protocol
- **Example from resource:**
```yaml
vars:
  content: file://data/input.txt
  example_input_1: file://data/examples/input1.txt
  system_prompt: file://prompts/system.md
```
- **Maps to existing:** NEW - **IT-38 File-Based Variable Loading**
- **Effectiveness:** Separates data from configuration; enables reuse of prompts/examples across tests

### Technique 4: Python Custom Assertion Pattern
- **Category:** DS (Domain-Specific - LLM Testing)
- **Pattern:** Structured return format for custom assertions with pass/score/reason/named_scores
- **Example from resource:**
```python
def check_length(output: str, context: dict) -> dict:
    return {
        "pass": bool,
        "score": float,        # 0.0-1.0
        "reason": str,
        "named_scores": dict   # Custom metrics
    }
```
- **Maps to existing:** NEW - **DS-110 Python Custom Assertion Pattern**
- **Effectiveness:** Enables arbitrary quality checks beyond string matching (length, structure, metrics)

### Technique 5: LLM-as-Judge with Rubric
- **Category:** DS (Domain-Specific - LLM Testing)
- **Pattern:** Use secondary LLM to evaluate primary LLM output against criteria
- **Example from resource:**
```yaml
assert:
  - type: llm-rubric
    value: |
      Evaluate the response based on:
      1. Accuracy of information
      2. Clarity of explanation
      3. Completeness
      Score 0.0-1.0 where 0.7+ is passing.
    threshold: 0.7
```
- **Maps to existing:** NEW - **DS-111 LLM-as-Judge with Rubric**
- **Effectiveness:** Automates subjective quality evaluation; scales beyond manual review

### Technique 6: Named Scores for Multi-Dimensional Metrics
- **Category:** QA (Quality Assurance)
- **Pattern:** Return multiple custom metrics alongside pass/fail
- **Example from resource:**
```python
return {
    "pass": True,
    "score": 0.8,
    "named_scores": {
        "relevance": 0.9,
        "input_length": 5000,
        "output_length": 1500,
        "reduction_ratio": 0.7
    }
}
```
- **Maps to existing:** NEW - **QA-27 Named Scores for Multi-Dimensional Metrics**
- **Effectiveness:** Track multiple quality dimensions; enables detailed analysis

### Technique 7: Few-Shot Pattern with File-Based Examples
- **Category:** DS (Domain-Specific - Prompt Engineering)
- **Pattern:** Chat format with assistant examples loaded from files
- **Example from resource:**
```json
[
  {"role": "system", "content": "{{system_prompt}}"},
  {"role": "user", "content": "{{example_input_1}}"},
  {"role": "assistant", "content": "{{example_output_1}}"},
  {"role": "user", "content": "{{actual_input}}"}
]
```
```yaml
vars:
  example_input_1: file://data/examples/input1.txt
  example_output_1: file://data/examples/output1.txt
```
- **Maps to existing:** NEW - **DS-112 Few-Shot Pattern with File-Based Examples**
- **Effectiveness:** Maintainable few-shot learning; reuse examples across tests

### Technique 8: Assertion Type Reference Table
- **Category:** IT (Interaction Techniques)
- **Pattern:** Comprehensive table of assertion types with usage and examples
- **Example from resource:**
```markdown
| Type | Usage | Example |
|------|-------|---------|
| `contains` | Check substring | `value: "hello"` |
| `regex` | Pattern match | `value: "\\d{4}"` |
| `python` | Custom logic | `value: file://script.py` |
| `llm-rubric` | LLM grading | `value: "Is professional"` |
```
- **Maps to existing:** Extends **IT-36 Best Practices by Category** → **IT-39 Assertion Type Reference Table**
- **Effectiveness:** Quick reference for choosing appropriate assertion type

### Technique 9: Real-World Example Section
- **Category:** IT (Interaction Techniques)
- **Pattern:** Complete production example with directory structure and context
- **Example from resource:**
```markdown
## Real-World Example

**Project:** Chinese short-video content curation from long transcripts

**Structure:**
```
tiaogaoren/
├── promptfooconfig.yaml
├── prompts/tiaogaoren-prompt.json
├── tests/cases.yaml
├── scripts/metrics.py
└── data/ (5 samples)
```

**See:** `/path/to/your/prompts-project/` for full implementation.
```
- **Maps to existing:** NEW - **IT-40 Real-World Example Section**
- **Effectiveness:** Bridges gap from tutorial to production; users see complete working system

### Technique 10: Dual Configuration Pattern (Production + Preview)
- **Category:** DS (Domain-Specific - LLM Testing)
- **Pattern:** Maintain two configs: one for production (API calls), one for preview (echo)
- **Example from resource:**
```
promptfooconfig.yaml          # Production: real providers
promptfooconfig-preview.yaml  # Preview: echo provider
```
- **Maps to existing:** NEW - **DS-113 Dual Configuration Pattern**
- **Effectiveness:** Iterate safely without API costs; validate before production runs

### Technique 11: Reduction Ratio Metric Pattern
- **Category:** DS (Domain-Specific - Content Curation)
- **Pattern:** Calculate input/output ratio to validate summarization/curation quality
- **Example from resource:**
```python
def check_length(output: str, context: dict) -> dict:
    input_len = len(strip_tags(raw_input))
    output_len = len(strip_tags(output))
    reduction_ratio = 1 - (output_len / input_len)

    return {
        "pass": 0.7 <= reduction_ratio <= 0.9,  # Target: 70-90% reduction
        "score": reduction_ratio
    }
```
- **Maps to existing:** NEW - **DS-114 Reduction Ratio Metric Pattern**
- **Effectiveness:** Quantifies summarization quality; prevents over-summarization or under-summarization

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Echo Provider for Cost-Free Preview (AG-23)
- **Description:** Use echo provider to return rendered prompt without making API calls
- **Implementation:**
  - Create separate preview config: `promptfooconfig-preview.yaml`
  - Set provider to `echo`
  - Run evaluation to see rendered prompts
  - Verify variable substitution, few-shot structure
  - Switch to real providers after validation
- **Use case:** LLM prompt development, few-shot engineering, variable testing
- **Example:** Any LLM evaluation with expensive API calls (GPT-4, Claude Opus)
- **Proposed category:** AG (Agentic - LLM Testing)
- **Proposed code:** AG-23

### Pattern 2: Progressive Evaluation Modes (DS-109)
- **Description:** Three-tier evaluation: Preview (echo) → Single Model → Multi-Model Comparison
- **Implementation:**
  - Tier 1: Echo provider (free, validate structure)
  - Tier 2: Single model (validate quality)
  - Tier 3: Multiple models (A/B comparison)
- **Use case:** LLM prompt optimization, model selection, cost management
- **Example:** Choosing between GPT-4 vs. Claude vs. Gemini for specific task
- **Proposed category:** DS (Domain-Specific - LLM Testing)
- **Proposed code:** DS-109

### Pattern 3: File-Based Variable Loading (IT-38)
- **Description:** Load test variables from external files using file:// protocol
- **Implementation:**
  - Convention: `file://path/to/file.txt`
  - Supports: .txt, .md, .json, .yaml, .pdf, images
  - Paths relative to config file location
- **Use case:** Large test datasets, reusable prompts, example management
- **Example:** Few-shot examples, long documents, test data libraries
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-38

### Pattern 4: Python Custom Assertion Pattern (DS-110)
- **Description:** Structured return format for custom quality checks
- **Implementation:**
  - Required: `pass` (bool)
  - Optional: `score` (0.0-1.0), `reason` (string), `named_scores` (dict)
  - Access test context via `context['vars']`
- **Use case:** Custom LLM output validation beyond string matching
- **Example:** Length checks, structure validation, metric calculation, business logic
- **Proposed category:** DS (Domain-Specific - LLM Testing)
- **Proposed code:** DS-110

### Pattern 5: LLM-as-Judge with Rubric (DS-111)
- **Description:** Use secondary LLM to evaluate primary LLM output
- **Implementation:**
  - Define evaluation criteria (1-N points)
  - Set threshold for passing score
  - Optional: Override grader model
- **Use case:** Subjective quality evaluation, tone assessment, style checking
- **Example:** "Is response professional?", "Does it follow brand voice?", "Is it empathetic?"
- **Proposed category:** DS (Domain-Specific - LLM Testing)
- **Proposed code:** DS-111

### Pattern 6: Named Scores for Multi-Dimensional Metrics (QA-27)
- **Description:** Return multiple custom metrics alongside pass/fail
- **Implementation:**
  - Primary: `pass` and `score`
  - Named scores: Dictionary of custom metrics
  - Track multiple quality dimensions
- **Use case:** Complex quality assessment, A/B testing, metric dashboards
- **Example:** Response quality (relevance, accuracy, completeness, tone, length)
- **Proposed category:** QA (Quality Assurance)
- **Proposed code:** QA-27

### Pattern 7: Few-Shot Pattern with File-Based Examples (DS-112)
- **Description:** Chat format with assistant examples loaded from external files
- **Implementation:**
  - Chat JSON with user/assistant pairs
  - Load examples via `file://data/examples/input1.txt`
  - 1-3 examples recommended
  - Preview with echo provider first
- **Use case:** Few-shot learning, prompt engineering, task demonstration
- **Example:** Classification, content curation, style transfer
- **Proposed category:** DS (Domain-Specific - Prompt Engineering)
- **Proposed code:** DS-112

### Pattern 8: Assertion Type Reference Table (IT-39)
- **Description:** Comprehensive table of testing assertion types
- **Implementation:**
  - Column 1: Type name
  - Column 2: Usage description
  - Column 3: Example value
- **Use case:** Testing documentation, assertion selection, onboarding
- **Example:** API testing, LLM evaluation, data validation
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-39

### Pattern 9: Real-World Example Section (IT-40)
- **Description:** Complete production example with directory structure and implementation reference
- **Implementation:**
  - Section: "Real-World Example"
  - Project description
  - Directory structure
  - Reference to full implementation path
- **Use case:** Production documentation, case studies, onboarding
- **Example:** Migration guides, architecture references, best practice showcases
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-40

### Pattern 10: Dual Configuration Pattern (DS-113)
- **Description:** Maintain production and preview configs for safe iteration
- **Implementation:**
  - `config.yaml`: Real providers, full evaluation
  - `config-preview.yaml`: Echo provider, structure validation
  - Switch between configs via `--config` flag
- **Use case:** LLM evaluation, API testing, cost management
- **Example:** Prompt development (iterate in preview, validate in production)
- **Proposed category:** DS (Domain-Specific - LLM Testing)
- **Proposed code:** DS-113

### Pattern 11: Reduction Ratio Metric Pattern (DS-114)
- **Description:** Calculate input/output ratio to validate summarization quality
- **Implementation:**
  - Measure input length and output length
  - Calculate ratio: `1 - (output_len / input_len)`
  - Set target range (e.g., 70-90% reduction)
- **Use case:** Summarization, content curation, text compression
- **Example:** Transcript → highlights, article → summary, report → executive summary
- **Proposed category:** DS (Domain-Specific - Content Curation)
- **Proposed code:** DS-114

## Multi-Technique Combinations

The `promptfoo-evaluation` skill demonstrates sophisticated combination of techniques:

1. **Echo Provider + Dual Configuration:**
   - Echo Provider enables cost-free preview
   - Dual Configuration Pattern maintains preview + production configs
   - Result: Iterate safely before expensive API calls

2. **File-Based Variables + Few-Shot Pattern:**
   - File-Based Variable Loading separates examples from config
   - Few-Shot Pattern uses loaded examples in chat format
   - Result: Reusable, maintainable few-shot learning

3. **Python Assertions + Named Scores:**
   - Python Custom Assertion Pattern enables arbitrary logic
   - Named Scores track multiple quality dimensions
   - Result: Rich, multi-dimensional quality analysis

4. **LLM-as-Judge + Progressive Evaluation:**
   - LLM-as-Judge automates subjective evaluation
   - Progressive Modes (echo → single → multi) reduces cost
   - Result: Scalable, automated quality assessment

5. **Real-World Example + Directory Structure:**
   - Real-World Example Section provides production reference
   - Shows complete implementation with file organization
   - Result: Clear path from tutorial to production

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md:
1. **Add 11 new techniques:**
   - AG-23: Echo Provider for Cost-Free Preview
   - DS-109: Progressive Evaluation Modes
   - IT-38: File-Based Variable Loading
   - DS-110: Python Custom Assertion Pattern
   - DS-111: LLM-as-Judge with Rubric
   - QA-27: Named Scores for Multi-Dimensional Metrics
   - DS-112: Few-Shot Pattern with File-Based Examples
   - IT-39: Assertion Type Reference Table
   - IT-40: Real-World Example Section
   - DS-113: Dual Configuration Pattern
   - DS-114: Reduction Ratio Metric Pattern

2. **Create new subcategories:**
   - "LLM Testing" (AG-23, DS-109, DS-110, DS-111, DS-113)
   - "Prompt Engineering" (DS-112)
   - "Content Curation" (DS-114)

3. **Cross-reference existing techniques:**
   - IT-36 (Best Practices by Category) → IT-39 extends to assertion types
   - IT-25 (Multi-Mode Interactive CLI) → DS-109 extends to evaluation modes

### For USE_CASE_LOOKUP.md:
- Add "LLM Evaluation" use case
- Recommended techniques: AG-23, DS-109, IT-38, DS-110, DS-111, QA-27, DS-112

### For AI_AGENT_QUICK_START.md:
- Add example in Section 5: "LLM evaluation with echo provider and custom assertions"
- Demonstrate Progressive Evaluation Modes for cost management

## Summary

**Complexity Rating:** 5/5

The `promptfoo-evaluation` skill is a **comprehensive LLM evaluation framework** demonstrating production-grade testing patterns including echo provider for cost-free previews, Python custom assertions, LLM-as-judge, and file-based variable loading.

**Key Strengths:**
1. **Cost-conscious approach:** Echo provider enables free iteration before expensive API calls
2. **Multi-dimensional quality:** Named scores and custom assertions track complex metrics
3. **Production-ready:** Real-world example with Chinese transcript curation (10k+ characters)
4. **Flexible testing:** String matching → Python logic → LLM-as-judge progression

**Novel Contributions:**
- Echo Provider (AG-23): Universal pattern for LLM prompt preview without API costs
- Progressive Evaluation Modes (DS-109): Structured approach to LLM testing (preview → validate → compare)
- Python Custom Assertion Pattern (DS-110): Standardized format for arbitrary quality checks
- LLM-as-Judge with Rubric (DS-111): Automated subjective quality evaluation

**Recommended Integration Priority:** CRITICAL
- AG-23 (Echo Provider): Essential for cost-effective LLM prompt development
- DS-110 (Python Custom Assertions): Standard for LLM output validation
- DS-111 (LLM-as-Judge): Scales subjective quality assessment

**Lines of Bundled Knowledge:** 642 lines
- SKILL.md: 393 lines (comprehensive tutorial)
- references/promptfoo_api.md: 249 lines (API reference)

**Production Readiness:** 5/5 - Includes real-world example (Chinese short-video curation), cost management (echo provider), multi-dimensional metrics (named scores), and comprehensive assertion types (17+ types)

**Real-World Application:** Chinese transcript → short-video highlights (10k+ char input, 70-90% reduction target, few-shot learning with 2 examples)
