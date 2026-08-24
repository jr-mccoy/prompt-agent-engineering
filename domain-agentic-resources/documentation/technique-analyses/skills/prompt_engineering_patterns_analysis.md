# Technique Analysis: prompt-engineering-patterns

**Resource Type:** Skill
**Path:** `claude-code-resources/skills/llm-application-dev/prompt-engineering-patterns/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 1 script, 5 references, 2 assets

---

## Summary

This skill is a **meta-prompting resource** that teaches prompt engineering techniques. It demonstrates progressive disclosure architecture, bundled resource organization, and comprehensive documentation patterns. Highly relevant to the Prompting-guides repository as it documents many existing techniques while also revealing novel resource organization patterns.

---

## Identified Techniques

### Technique 1: Progressive Disclosure (Three-Tier Architecture)

- **Category:** IT (Interaction Techniques)
- **Pattern:**
  - Tier 1: Metadata (name + description) - Always loaded (~100 words)
  - Tier 2: SKILL.md body - Loaded when skill triggers (<5k words)
  - Tier 3: Bundled resources - Loaded as needed by Claude
- **Example from resource:**
  ```
  ## Resources
  - references/few-shot-learning.md: Deep dive on example selection
  - references/chain-of-thought.md: Advanced reasoning elicitation techniques
  - assets/prompt-template-library.md: Battle-tested prompt templates
  - scripts/optimize-prompt.py: Automated prompt optimization tool
  ```
- **Maps to existing:** IT-06 (Progressive Disclosure) - but this is a **specific architectural implementation**
- **Effectiveness:** Minimizes context window usage while maximizing capability. Critical for managing large knowledge bases in Claude Code.

### Technique 2: Few-Shot Learning with Semantic Selection

- **Category:** RT (Reasoning Techniques)
- **Pattern:** Dynamic example selection based on semantic similarity to query
- **Example from resource:**
  ```python
  selector = FewShotSelector(
      examples_db="sql_examples.jsonl",
      selection_strategy="semantic_similarity",
      max_examples=3
  )
  ```
- **Maps to existing:** RT-07 (Few-Shot Examples)
- **Effectiveness:** Improves relevance of examples, reduces context pollution

### Technique 3: Chain-of-Thought Prompting

- **Category:** RT (Reasoning Techniques)
- **Pattern:** Elicit step-by-step reasoning with explicit instruction
- **Example from resource:** "Zero-shot CoT with 'Let's think step by step'" and "Few-shot CoT with reasoning traces"
- **Maps to existing:** RT-01 (Chain of Thought)
- **Effectiveness:** Fundamental reasoning technique for complex tasks

### Technique 4: Hierarchical Instruction Structure

- **Category:** ST (Structural Techniques)
- **Pattern:**
  ```
  [System Context] → [Task Instruction] → [Examples] → [Input Data] → [Output Format]
  ```
- **Example from resource:** Explicitly documented as "Instruction Hierarchy" in the skill
- **Maps to existing:** ST-04 (Structured Prompts)
- **Effectiveness:** Provides consistent ordering that LLMs expect, improves output quality

### Technique 5: Error Recovery Patterns

- **Category:** NEW
- **Pattern:** Build prompts that gracefully handle failures with:
  - Fallback instructions
  - Confidence scores
  - Alternative interpretations when uncertain
  - How to indicate missing information
- **Example from resource:**
  ```markdown
  ### Error Recovery
  Build prompts that gracefully handle failures:
  - Include fallback instructions
  - Request confidence scores
  - Ask for alternative interpretations when uncertain
  - Specify how to indicate missing information
  ```
- **Maps to existing:** NEW (not in MASTER_TECHNIQUE_INDEX)
- **Effectiveness:** Prevents silent failures and improves reliability in production systems

### Technique 6: Self-Verification Layer

- **Category:** RT (Reasoning Techniques)
- **Pattern:** Add verification step after main task
- **Example from resource:**
  ```python
  prompt = f"""{main_task_prompt}

  After generating your response, verify it meets these criteria:
  1. Answers the question directly
  2. Uses only information from provided context
  3. Cites specific sources
  4. Acknowledges any uncertainty

  If verification fails, revise your response."""
  ```
- **Maps to existing:** RT-03 (Self-Verification)
- **Effectiveness:** Catches errors before output, improves accuracy

### Technique 7: Prompt A/B Testing Framework

- **Category:** QA (Quality Assurance)
- **Pattern:** Statistical comparison of prompt variants with metrics
- **Example from resource:**
  ```python
  class PromptABTest:
      def run_test(self, test_queries, metrics=['accuracy', 'latency']):
          # 50/50 split between variants
          # Statistical analysis with scipy.stats
  ```
- **Maps to existing:** QA-07 (Statistical A/B Testing for Prompts) - documented in Task 3.2
- **Effectiveness:** Data-driven prompt optimization, reduces subjective evaluation

### Technique 8: Template Variable Interpolation

- **Category:** OT (Output Techniques)
- **Pattern:** Reusable templates with variable substitution
- **Example from resource:**
  ```python
  template = PromptTemplate(
      system="You are an expert SQL developer...",
      instruction="Convert the following natural language query to SQL:\n{query}",
      few_shot_examples=True,
      output_format="SQL code block with explanatory comments"
  )
  ```
- **Maps to existing:** OT-01 (Output Format Specification) + ST-07 (Template-Based Prompts)
- **Effectiveness:** Enables reuse, consistency, and maintainability

### Technique 9: Metric-Driven Evaluation

- **Category:** DS (Domain-Specific)
- **Pattern:** Track KPIs for prompt performance
- **Example from resource:**
  ```markdown
  ## Success Metrics
  - Accuracy: Correctness of outputs
  - Consistency: Reproducibility across similar inputs
  - Latency: Response time (P50, P95, P99)
  - Token Usage: Average tokens per request
  - Success Rate: Percentage of valid outputs
  - User Satisfaction: Ratings and feedback
  ```
- **Maps to existing:** DS-02 (Metric Specification)
- **Effectiveness:** Enables objective evaluation and optimization

### Technique 10: Bundled Executable Scripts

- **Category:** NEW
- **Pattern:** Package executable tools with instructional content
- **Example from resource:**
  - `scripts/optimize-prompt.py`: Automated prompt optimization tool
  - Skill loads script only when needed
- **Maps to existing:** NEW (not in MASTER_TECHNIQUE_INDEX)
- **Effectiveness:** Combines documentation with tooling, enables automation

### Technique 11: Progressive Complexity (Leveled Instructions)

- **Category:** IT (Interaction Techniques)
- **Pattern:** Start simple, add complexity incrementally
- **Example from resource:**
  ```markdown
  ### Progressive Disclosure
  1. Level 1: Direct instruction - "Summarize this article"
  2. Level 2: Add constraints - "Summarize in 3 bullet points..."
  3. Level 3: Add reasoning - "Read article, identify findings, then summarize..."
  4. Level 4: Add examples - Include 2-3 example summaries
  ```
- **Maps to existing:** IT-06 (Progressive Disclosure) but applied to **instruction complexity** not just resource loading
- **Effectiveness:** Reduces over-engineering, matches complexity to task difficulty

### Technique 12: Reference File Pointers

- **Category:** NEW
- **Pattern:** Main skill file points to detailed reference files, loaded on demand
- **Example from resource:**
  ```markdown
  ## Resources
  - references/few-shot-learning.md: Deep dive on example selection
  - references/chain-of-thought.md: Advanced reasoning elicitation
  - references/prompt-optimization.md: Systematic refinement workflows
  ```
- **Maps to existing:** NEW (related to IT-06 but specific architectural pattern)
- **Effectiveness:** Separates overview from deep dives, reduces initial context load

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Error Recovery Patterns for Prompts

- **Description:** Structured approach to handling LLM failures gracefully within prompts
- **Implementation:**
  - Include fallback instructions ("If you cannot determine X, explain why")
  - Request confidence scores ("Rate your confidence 1-10")
  - Ask for alternative interpretations ("If uncertain, provide 2-3 possible interpretations")
  - Specify missing information indicators ("Use 'UNKNOWN' if data is unavailable")
- **Use case:** Production LLM applications requiring reliability
- **Example:**
  ```
  Task: {user_task}

  If you cannot complete this task, explain:
  1. What information is missing
  2. What assumptions you would need to make
  3. An alternative approach

  Confidence in your response (1-10): [score]
  ```
- **Proposed category:** RT (Reasoning Techniques)
- **Proposed code:** RT-12

### Pattern 2: Bundled Executable Scripts in Skills

- **Description:** Package executable tooling with instructional documentation
- **Implementation:**
  - Skill provides instruction (SKILL.md)
  - Scripts provide automation (scripts/)
  - References provide deep knowledge (references/)
  - Assets provide templates (assets/)
- **Use case:** Skills requiring automation alongside guidance
- **Example:**
  ```
  skill-name/
  ├── SKILL.md (how to use)
  ├── scripts/optimize.py (automation)
  ├── references/deep-dive.md (theory)
  └── assets/template.json (starter files)
  ```
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-14

### Pattern 3: Hierarchical Reference Loading

- **Description:** Organize references by depth, load progressively
- **Implementation:**
  - Quick Start in SKILL.md (500 words)
  - Intermediate guides in references/ (2000-5000 words each)
  - Advanced topics in separate references
  - Claude loads based on depth needed
- **Use case:** Complex domains with varying user expertise
- **Example:**
  ```
  SKILL.md → Quick Start (always loaded)
  references/intermediate-guide.md → When user needs more
  references/advanced-patterns.md → When expert needed
  references/edge-cases.md → When debugging
  ```
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-15

### Pattern 4: Prompt Versioning as Code

- **Description:** Treat prompts like software with version control, testing, and CI/CD
- **Implementation:**
  - Version prompts in git
  - Automated testing on every change
  - A/B testing in production
  - Rollback capabilities
  - Documentation of why changes were made
- **Use case:** Production LLM applications requiring stability
- **Example:**
  ```python
  # prompt_v1.2.3.py
  SYSTEM_PROMPT = """..."""  # Version 1.2.3

  CHANGELOG = """
  v1.2.3 (2024-01-15):
  - Added confidence scoring (improves accuracy by 5%)
  - Reduced token usage by 20%
  - Fixed edge case with empty inputs
  """
  ```
- **Proposed category:** DS (Domain-Specific - LLM Engineering)
- **Proposed code:** DS-20

---

## Multi-Technique Combinations

### Combination 1: Progressive Disclosure + Few-Shot + Templates
- **Technique Stack:** IT-06 + RT-07 + OT-01
- **Combination Purpose:** Create reusable, context-efficient prompt systems
- **Flow:**
  1. Load metadata only (name + brief description)
  2. When triggered, load SKILL.md with templates
  3. When examples needed, load few-shot examples from assets
  4. Template renders with selected examples
- **Synergies:** Minimizes context while maximizing capability, enables dynamic example selection

### Combination 2: Chain-of-Thought + Self-Verification + Error Recovery
- **Technique Stack:** RT-01 + RT-03 + RT-12 (novel)
- **Combination Purpose:** Robust reasoning with graceful degradation
- **Flow:**
  1. Elicit step-by-step reasoning (CoT)
  2. Self-verify reasoning meets criteria
  3. If verification fails or uncertain, trigger error recovery patterns
- **Synergies:** Catches errors early, provides fallback strategies, improves production reliability

### Combination 3: Hierarchical Instructions + Metric Evaluation + A/B Testing
- **Technique Stack:** ST-04 + DS-02 + QA-07
- **Combination Purpose:** Data-driven prompt optimization
- **Flow:**
  1. Structure prompt with consistent hierarchy
  2. Define metrics for evaluation
  3. A/B test variants to find optimal structure
- **Synergies:** Systematic optimization, objective decision-making

### Combination 4: Bundled Resources + Reference Pointers + Progressive Complexity
- **Technique Stack:** IT-14 (novel) + IT-15 (novel) + IT-06
- **Combination Purpose:** Scalable knowledge management
- **Flow:**
  1. Start with simple overview in SKILL.md
  2. Point to references for deeper topics
  3. Load references only when complexity needed
  4. Scripts available for automation
- **Synergies:** Efficient context usage, supports all skill levels, enables automation

---

## Notes for Integration

### Add to MASTER_TECHNIQUE_INDEX:
1. **RT-12: Error Recovery Patterns** - Graceful degradation for prompts
2. **IT-14: Bundled Executable Scripts** - Package tooling with documentation
3. **IT-15: Hierarchical Reference Loading** - Progressive depth-based loading
4. **DS-20: Prompt Versioning as Code** - Software engineering for prompts

### Update USE_CASE_LOOKUP:
- **Use Case: LLM Application Development** - Add this skill as primary example
- **Use Case: Prompt Optimization** - Reference A/B testing and iterative refinement patterns
- **Use Case: Production ML Systems** - Reference error recovery and versioning patterns

### Cross-reference with prompts:
- **llm-application-dev prompts** - This skill provides implementation patterns
- **learning/prompt-engineering prompts** - This skill offers advanced techniques
- **engineering/debugging prompts** - Error recovery patterns applicable

### Documentation improvements:
1. **AI_AGENT_QUICK_START.md** - Add section on bundled resources architecture
2. **CLAUDE.md guide** - Reference progressive disclosure principles from this skill
3. **Repository README** - Highlight this skill as example of Claude Code resource

### Best practices:
1. **Three-tier loading** is optimal for context management
2. **Bundled scripts** enable automation without bloat
3. **Reference files** should be 2000-5000 words each (detailed but focused)
4. **Error recovery** should be standard in all production prompts
5. **Prompt versioning** improves maintainability and debugging

---

## Analysis Metadata

**Analyzer:** Claude (Task 2.2 Priority 2 - Skills Analysis)
**Analysis Duration:** 30 minutes
**Confidence Level:** High
**Review Status:** Draft
**Priority for Integration:** **High** (meta-prompting resource, 4 novel techniques, directly relevant to repository)

---

## Technique Complexity Score

**Score: 4/5** (High Complexity)

**Rationale:**
- Uses 12+ distinct techniques
- 4 novel patterns not in existing index
- Complex multi-technique combinations
- Meta-level resource (teaches prompting itself)
- Progressive disclosure architecture requires sophisticated design

---

## Key Insights

1. **Skills are architectural marvels**: The three-tier loading system (metadata → SKILL.md → bundled resources) is a novel context management pattern worthy of documentation.

2. **Meta-prompting goldmine**: This skill documents many techniques we already have BUT shows how to combine them in production systems.

3. **Error recovery is underexplored**: The graceful degradation patterns (fallbacks, confidence scores, alternative interpretations) are not well-documented in existing prompting literature.

4. **Prompts as software**: The versioning, A/B testing, and CI/CD patterns treat prompts like production code - this is a emerging best practice.

5. **Bundled resources enable scale**: By packaging scripts, references, and assets with instructions, skills can provide comprehensive capability without context bloat.

---

## Recommendations

1. **Document IT-14 (Bundled Scripts)** as high-priority technique - enables automation
2. **Document RT-12 (Error Recovery)** for production reliability patterns
3. **Add "Prompts as Code" section** to AI_AGENT_QUICK_START.md
4. **Create mapping**: This skill → existing prompting prompts in repository
5. **Extract A/B testing framework** as reusable tool for prompt evaluation
