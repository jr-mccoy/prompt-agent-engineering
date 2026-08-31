# Claude & AI Agents Guide for Prompt & Agent Engineering

**A comprehensive guide for using this repository with Claude Code, Claude Chat, and other AI agents**

---

## Table of Contents

1. [Introduction](#introduction)
2. [Understanding Claude and AI Agents](#understanding-claude-and-ai-agents)
3. [Quick Start for Claude Users](#quick-start-for-claude-users)
4. [Repository Structure for Agents](#repository-structure-for-agents)
5. [Using Prompts with Claude Code](#using-prompts-with-claude-code)
6. [AI Agent Workflows](#ai-agent-workflows)
7. [Prompt Engineering Techniques Library](#prompt-engineering-techniques-library)
8. [Claude Skills Integration](#claude-skills-integration)
9. [Best Practices](#best-practices)
10. [Advanced Techniques](#advanced-techniques)
11. [Troubleshooting](#troubleshooting)

---

## Introduction

This repository contains **93+ professionally crafted prompts** designed specifically for AI coding agents like Claude Code, along with a comprehensive **Prompt Engineering Techniques Library** that catalogs 50+ proven techniques.

**What makes this special for Claude agents:**
- Prompts optimized for Claude's multi-modal capabilities
- Structured for systematic code analysis workflows
- Integration with Claude Code's tool ecosystem
- Built-in prompt engineering best practices
- Skills files designed for Claude Code's skill system

---

## Understanding Claude and AI Agents

### What is Claude Code?

**Claude Code** is Anthropic's official CLI agent for software development tasks. It provides:
- Direct file system access and manipulation
- Git integration and version control
- Bash/terminal command execution
- Multi-file codebase analysis
- Parallel tool execution for efficiency
- Background task management

### What is Claude Chat?

**Claude Chat** is Anthropic's conversational AI interface at claude.ai, great for:
- Exploratory analysis and planning
- Document generation and review
- Learning and understanding prompts
- Prototyping prompt modifications

### Other Compatible AI Agents

This repository works with any LLM-powered coding assistant:
- **Cursor** - AI-powered code editor
- **GitHub Copilot** - GitHub's coding assistant
- **Replit AI** - Interactive coding environment
- **Continue.dev** - VS Code AI extension
- **Aider** - Terminal-based AI pair programmer

---

## Quick Start for Claude Users

### Scenario 1: Using Claude Code for Codebase Analysis

```bash
# Clone this repository
git clone https://github.com/jr-mccoy/prompt-agent-engineering.git
cd prompt-agent-engineering

# Start Claude Code
claude-code

# Ask Claude to use a prompt
"Use the architecture layer identification prompt from code-analysis/architecture/
to analyze my project at /path/to/my/project"
```

### Scenario 2: Using Claude Chat to Learn Prompting

1. Visit [claude.ai](https://claude.ai)
2. Upload or reference prompts from this repository
3. Ask: "Explain how this prompt works and show me how to customize it for my use case"

### Scenario 3: Building Custom Prompts with the Techniques Library

```
"I need to analyze database performance in my application.
Use the prompt-techniques library to build me a custom prompt."
```

Claude will:
1. Reference `techniques/USE_CASE_LOOKUP.md`
2. Select relevant techniques from `MASTER_TECHNIQUE_INDEX.md`
3. Build a customized prompt using proven patterns
4. Execute the analysis

---

## Repository Structure for Agents

### High-Level Organization

```
Prompting-guides/
├── code-analysis/          # 30+ code analysis prompts
│   ├── architecture/       # 9 prompts (layers, patterns, diagrams)
│   ├── performance/        # 7 prompts (bottlenecks, optimization)
│   ├── quality/           # 7 prompts (complexity, documentation)
│   ├── evolution/         # 6 prompts (technical debt, churn)
│   └── security/          # 1 prompt (vulnerability analysis)
│
├── engineering/           # 14 workflow & process prompts
├── business-analysis/     # 20 strategic framework prompts
├── learning/             # 16 educational & interactive prompts
├── testing/              # 1 test generation prompt
├── improvement/          # 3 code enhancement prompts
│
├── techniques/    # NEW! Prompt engineering library
│   ├── MASTER_TECHNIQUE_INDEX.md    # 50+ techniques catalog
│   ├── USE_CASE_LOOKUP.md           # Find techniques by need
│   ├── AI_AGENT_QUICK_START.md      # Fast reference for building
│   └── TECHNIQUE_DECISION_TREES.md  # Decision support
│
├── meta/                 # 8 guides on prompting & tools
└── skills/               # 1 Claude Code skill file
```

### Key Directories for Claude Agents

| Directory | Use When | Claude Agent Capability |
|-----------|----------|------------------------|
| `techniques/` | Building prompts on-demand | AI_AGENT_QUICK_START.md designed for you |
| `code-analysis/` | Analyzing codebases | Perfect for Claude Code's file access |
| `engineering/` | Planning & workflows | Great for sprint planning, postmortems |
| `meta/` | Learning prompt patterns | Essential reading for optimization |
| `skills/` | Advanced agent workflows | Claude Code skill integration |

---

## Using Prompts with Claude Code

### Method 1: Direct Copy-Paste

```bash
# In Claude Code session
"Read the file code-analysis/performance/performance_bottleneck_identification.md
and apply it to my codebase at /path/to/project"
```

**Claude will:**
1. Read the prompt file
2. Load your codebase
3. Apply the prompt systematically
4. Generate analysis output

### Method 2: Reference by Path

```bash
"Use the prompt at engineering/engineering-pre-code-canvas.md
to plan the implementation of feature X"
```

### Method 3: Build Dynamic Prompts

```bash
"I need to analyze API performance and security together.
Use the prompt-techniques library to build a combined prompt."
```

**Claude will reference:**
- `techniques/USE_CASE_LOOKUP.md` for technique selection
- `MASTER_TECHNIQUE_INDEX.md` for technique details
- Relevant example prompts for patterns

### Method 4: Install as Claude Code Skill

```bash
# Copy skill file to Claude Code skills directory
cp skills/agentic_development.md ~/.claude/skills/

# Use the skill in Claude Code
"Use the agentic-development skill to guide my workflow"
```

---

## AI Agent Workflows

### Workflow 1: Comprehensive Codebase Analysis

**Task:** Full analysis of a new codebase

**Steps:**
```
1. "Use architecture_layer_identification.md to map the architecture"
2. "Use architecture_design_pattern_identification.md to find patterns"
3. "Use quality_code_complexity_analysis.md to assess quality"
4. "Use performance_bottleneck_identification.md to find issues"
5. "Use evolution_technical_debt_estimation.md to quantify debt"
```

**Claude Code Advantage:** Can run these in parallel using multi-tool execution

```bash
# Ask Claude:
"Run architecture, quality, and performance analysis in parallel
using the relevant prompts from code-analysis/"
```

### Workflow 2: Feature Planning and Implementation

**Task:** Plan and build a new feature

**Steps:**
```
1. "Use engineering-pre-code-canvas.md to plan the feature"
2. "Reference AI_AGENT_QUICK_START.md to build
   an implementation prompt"
3. "Generate tests using testing/generate_unit_tests.md"
4. "Document with quality/generate_documentation.md"
```

### Workflow 3: Code Review and Improvement

**Task:** Review pull request or code changes

**Steps:**
```
1. "Use quality_code_complexity_analysis.md on the changed files"
2. "Run quality_documentation_coverage_analysis.md"
3. "Check security/vulnerability_analysis.md"
4. "Apply learning/socratic-dialogue-code-review.md for deeper review"
```

### Workflow 4: Learning and Onboarding

**Task:** Understand unfamiliar codebase

**Steps:**
```
1. "Use learning/algorithmic-storytelling.md to explain the flow"
2. "Run learning/code-pattern-recognition.md to identify patterns"
3. "Generate learning/mini-lesson-generation.md for key components"
4. "Create learning/codebase-trivia.md for interactive practice"
```

### Workflow 5: Strategic Business Analysis

**Task:** Evaluate product strategy

**Steps:**
```
1. "Apply business-analysis/swot-analysis.md to current state"
2. "Use business-analysis/competitive-positioning-map.md"
3. "Run business-analysis/product-market-fit.md"
4. "Generate business-analysis/okr-analysis.md for alignment"
```

---

## Prompt Engineering Techniques Library

### Overview

The `techniques/` directory is a **game-changer for AI agents**. It enables:
- Building prompts programmatically on-demand
- Systematic technique selection based on use case
- Quality assurance through proven patterns
- Consistent results across different tasks

### Key Files for Claude Agents

#### 1. AI_AGENT_QUICK_START.md

**Purpose:** Fast reference for building prompts on-the-fly

**Structure:**
```markdown
- 5-Step Prompt Building Process
- Common Pattern Library (ready-to-use templates)
- Technique Quick Reference
- Decision Trees for technique selection
- Time-Saving Tips
```

**How Claude Uses This:**
```
User: "I need to analyze database performance"

Claude:
1. Reads AI_AGENT_QUICK_START.md
2. Classifies intent: Analysis + Performance
3. Selects techniques: ST-04 (Multi-Phase), RT-02 (Criteria-Based)
4. Builds structured prompt
5. Executes analysis
```

#### 2. MASTER_TECHNIQUE_INDEX.md

**Purpose:** Complete catalog of 50+ techniques

**Categories:**
- **ST**: Structural Techniques (organization)
- **RT**: Reasoning Techniques (thinking processes)
- **OC**: Output Control (formatting)
- **QA**: Quality Assurance (verification)
- **CT**: Context Techniques (information management)
- **PE**: Prompt Engineering Meta (self-improvement)
- **AS**: Agent-Specific (Claude Code features)
- **CM**: Combination Methods (multi-technique)
- **AT**: Advanced Techniques (complex scenarios)
- **DT**: Domain-Specific (specialized tasks)

**Example Usage:**
```
"Show me techniques for code review tasks"

Claude references MASTER_TECHNIQUE_INDEX.md:
- RT-01: Chain-of-Thought (CoT)
- QA-01: Self-Verification
- ST-03: Output Format Specification
- DT-04: Multi-Layer Analysis
```

#### 3. USE_CASE_LOOKUP.md

**Purpose:** Find techniques by user need

**Use Cases Covered:**
- Analysis & Review tasks
- Creation & Generation tasks
- Teaching & Explanation tasks
- Decision & Planning tasks
- Problem-Solving tasks
- Quality Assurance tasks

**Example:**
```
User: "Help me debug this performance issue"

Claude references USE_CASE_LOOKUP.md → Problem-Solving section:
- Recommended: RT-04 (Root Cause Analysis)
- Supporting: ST-04 (Multi-Phase Structure)
- Output: OC-02 (Prioritized Lists)
```

#### 4. TECHNIQUE_DECISION_TREES.md

**Purpose:** Guided technique selection

**Decision Flow:**
```
What's the task?
  → Analysis
    → Code quality? → ST-03 + RT-02 + QA-01
    → Performance? → ST-04 + RT-04 + OC-03
    → Security? → RT-05 + QA-02 + OC-04
  → Creation
    → Code? → ST-02 + RT-01 + QA-01
    → Documentation? → ST-03 + ST-05 + CM-02
```

### Building Custom Prompts with Techniques

**Process Claude Follows:**

1. **Classify User Intent**
   ```
   "I need X" → Map to use case category
   ```

2. **Select Techniques**
   ```
   Reference USE_CASE_LOOKUP.md → Get technique codes
   Look up details in MASTER_TECHNIQUE_INDEX.md
   ```

3. **Build Structure**
   ```
   Apply ST techniques (structural)
   Add RT techniques (reasoning)
   Include OC techniques (output control)
   Layer in QA techniques (verification)
   ```

4. **Add Quality Controls**
   ```
   Self-verification steps
   Output validation
   Error handling
   ```

5. **Execute and Iterate**
   ```
   Run the prompt
   Verify output quality
   Refine if needed
   ```

---

## Claude Skills Integration

### What are Claude Code Skills?

Skills are specialized prompt files that Claude Code loads automatically, providing:
- Enhanced agent capabilities
- Domain-specific workflows
- Consistent methodologies
- Reusable patterns

### Using the Agentic Development Skill

**Location:** `skills/agentic_development.md`

**What it provides:**
- Peter Steinberger's "Just Talk To It" methodology
- Parallel agent management strategies
- Tool selection heuristics
- Real-world high-volume development patterns

**Installation:**

```bash
# Method 1: Copy to skills directory
cp skills/agentic_development.md ~/.claude/skills/

# Method 2: Reference in session
"Load and use the skill at skills/agentic_development.md"
```

**Usage Examples:**

```bash
# Example 1: Complex feature development
"Use the agentic-development skill to guide building
a multi-service authentication system"

# Example 2: Large refactoring
"Apply the agentic-development workflow to refactor
the database layer to use TypeORM"

# Example 3: Performance optimization
"Follow the agentic-development patterns to optimize
our API response times"
```

### Creating Custom Skills from Prompts

**Convert any prompt to a skill:**

```bash
# 1. Choose a prompt that suits your workflow
# 2. Copy to skills directory with .md extension
cp code-analysis/architecture/architecture_layer_identification.md \
   ~/.claude/skills/layer-analysis.md

# 3. Add skill metadata at the top
# 4. Reference in Claude Code sessions
```

---

## Best Practices

### For Claude Code Users

#### 1. **Start with Exploration**

```bash
# Good approach
"First, analyze the codebase structure using glob patterns,
then apply the appropriate analysis prompt"

# Less effective
"Just run all analysis prompts"
```

#### 2. **Use Parallel Execution**

```bash
# Claude Code can run multiple tools simultaneously
"Run architecture analysis, quality checks, and performance
analysis in parallel on the codebase"
```

#### 3. **Leverage File Context**

```bash
# Provide specific context
"Use quality_code_complexity_analysis.md on these files:
- src/services/auth.ts
- src/services/user.ts
- src/middleware/validation.ts"
```

#### 4. **Iterate with Refinement**

```bash
# First pass
"Use the bottleneck identification prompt on the API layer"

# Refine
"Now deep-dive into the database queries identified
in the previous analysis"
```

### For Claude Chat Users

#### 1. **Upload Multiple Prompts**

```
Upload several related prompts and ask:
"Compare these prompts and explain when to use each one"
```

#### 2. **Request Customization**

```
"Take the performance_bottleneck_identification.md prompt
and customize it for a React Native mobile app"
```

#### 3. **Learn Techniques**

```
"Analyze this prompt and identify which techniques from
MASTER_TECHNIQUE_INDEX.md it uses"
```

### General Best Practices

#### ✅ DO:

- **Customize prompts** with your specific context
- **Combine prompts** for comprehensive analysis
- **Reference the techniques library** when building custom prompts
- **Start small** - test on limited scope first
- **Use screenshots** - visual context is powerful
- **Iterate** - use outputs as inputs for deeper analysis

#### ❌ DON'T:

- Run all prompts blindly without understanding them
- Ignore the techniques library when creating custom prompts
- Skip reading meta/ guides
- Use prompts verbatim without customization
- Forget to validate outputs

---

## Advanced Techniques

### 1. Multi-Agent Workflows

**Concept:** Use multiple Claude instances or sessions for different aspects

```
Instance 1: Architecture analysis using code-analysis/architecture/
Instance 2: Business analysis using business-analysis/
Instance 3: Learning documentation using learning/

Combine outputs for comprehensive understanding
```

### 2. Prompt Chaining

**Pattern:** Output of one prompt feeds into another

```bash
# Step 1
"Use architecture_layer_identification.md to map layers"
# Output: List of architectural layers

# Step 2
"For each layer identified, run performance_bottleneck_identification.md"
# Output: Performance issues per layer

# Step 3
"Use evolution_refactoring_recommendations.md on problematic layers"
# Output: Refactoring plan
```

### 3. Template Customization

**From techniques library:**

```bash
# Get template
"Show me the template for code analysis from
AI_AGENT_QUICK_START.md"

# Customize
"Modify this template to focus on GraphQL resolvers
instead of REST APIs"

# Apply
"Use the customized template on my GraphQL server code"
```

### 4. Hybrid Human-AI Workflows

```
1. Human: Define objectives and constraints
2. Claude: Generate plan using engineering-pre-code-canvas.md
3. Human: Review and approve plan
4. Claude: Implement using relevant prompts
5. Human: Review outputs
6. Claude: Refine using improvement/ prompts
```

### 5. Meta-Prompting

**Use prompts to improve prompts:**

```bash
"Use engineering/prompt-improvement.md to analyze and
improve the quality_code_duplication_analysis.md prompt
for my specific use case"
```

### 6. Technique Combination Patterns

**From MASTER_TECHNIQUE_INDEX.md:**

```
High-Quality Code Review:
ST-04 (Delimited Sections) + RT-01 (Chain-of-Thought) +
QA-01 (Self-Verification) + DT-04 (Multi-Layer Analysis)

Strategic Planning:
RP-01 (Expert Role Assignment) + RT-03 (Tree of Thoughts) +
OC-03 (Markdown Table Specification) + CM-01 (Explicit Context Framing)

Teaching/Learning:
ST-05 (Example-Driven) + RP-04 (Socratic Dialogue) +
ST-03 (Output Format Specification) + CM-04 (Summary-Expand Loop)
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: "The prompt doesn't work well on my codebase"

**Solution:**
```bash
# 1. Read the prompt first
"Show me the prompt at code-analysis/quality/quality_code_complexity_analysis.md"

# 2. Identify assumptions
"What assumptions does this prompt make about the codebase?"

# 3. Customize
"Modify this prompt for a Python/Django codebase instead of JavaScript"

# 4. Test
"Apply the modified prompt to src/main.py"
```

#### Issue: "I get too much output"

**Solution:**
```bash
# Use focused scope
"Apply this prompt only to the authentication module,
files matching src/auth/**/*.ts"

# Use output control techniques
"Add OC-03 (Hierarchical Summaries) to this prompt
to make output more manageable"
```

#### Issue: "I don't know which prompt to use"

**Solution:**
```bash
# Consult the techniques library
"I need to [describe task]. Check USE_CASE_LOOKUP.md
and recommend which prompts to use"

# Ask for guidance
"What's the difference between architecture_layer_identification.md
and architecture_design_pattern_identification.md?"
```

#### Issue: "Prompt is too generic"

**Solution:**
```bash
# Reference techniques library
"Use MASTER_TECHNIQUE_INDEX.md to add specificity techniques
(CM-01, CM-02) to this prompt"

# Provide context
"Here's my tech stack: [details]. Customize the prompt
for this context"
```

#### Issue: "Results aren't actionable"

**Solution:**
```bash
# Add output control techniques
"Modify this prompt to use OC-02 (Prioritized Lists)
and OC-04 (Decision Matrices) for actionable output"

# Request specific deliverables
"Change the output to include: priority, effort estimate,
and specific files to modify"
```

### Getting Help

#### From the Repository:

1. **Read meta/failure_modes.md** - Common AI agent failures and solutions
2. **Check meta/model_quirks.md** - Claude-specific optimization tips
3. **Review meta/vibe_coding_prompts.md** - Practical patterns

#### From Claude:

```bash
# Ask for explanation
"Explain this prompt in simple terms and show me an example"

# Request modifications
"This prompt isn't working. Here's what happened: [details].
How should I modify it?"

# Get technique recommendations
"What techniques from MASTER_TECHNIQUE_INDEX.md would
improve this prompt for my use case?"
```

---

## Real-World Usage Examples

### Example 1: Onboarding to New Codebase

**Scenario:** You just joined a team with a large unfamiliar codebase

**Claude Code Workflow:**

```bash
# Session start
claude-code

# Step 1: High-level understanding
"Use learning/algorithmic-storytelling.md to explain the
main application flow in /path/to/project"

# Step 2: Architecture mapping
"Apply architecture_layer_identification.md to understand
the system structure"

# Step 3: Pattern recognition
"Run learning/code-pattern-recognition.md to identify
common patterns I should know"

# Step 4: Key components
"Use learning/backend-api-documentation.md to document
the main API endpoints"

# Step 5: Interactive learning
"Generate learning/codebase-trivia.md to help me practice
and retain this knowledge"
```

**Result:** Comprehensive understanding in hours instead of weeks

### Example 2: Pre-Production Performance Audit

**Scenario:** App is slow before launch, need to find and fix issues

**Claude Code Workflow:**

```bash
# Step 1: Identify bottlenecks
"Use performance_bottleneck_identification.md on the
entire codebase, focusing on critical paths"

# Step 2: Analyze resource usage
"Run performance_resource_usage_profiling.md on the
identified problematic areas"

# Step 3: Get specific recommendations
"Apply performance_code_optimization_suggestions.md to
the top 5 bottlenecks"

# Step 4: Plan refactoring
"Use evolution_refactoring_recommendations.md to create
a safe refactoring plan"

# Step 5: Generate test scenarios
"Create performance_test_scenario_generation.md to validate
improvements"
```

**Result:** Systematic performance improvements with validation

### Example 3: Building a Custom Analysis Tool

**Scenario:** Need recurring analysis not covered by existing prompts

**Claude Chat Workflow:**

```markdown
User: "I need a prompt that analyzes React components for
accessibility issues and suggests fixes"

Claude:
1. References techniques/USE_CASE_LOOKUP.md
2. Finds: Analysis + Quality + Code Review use case
3. Reads MASTER_TECHNIQUE_INDEX.md for relevant techniques:
   - ST-04: Multi-Phase Structure
   - RT-02: Criteria-Based Reasoning
   - QA-01: Self-Verification
   - OC-03: Hierarchical Summaries
4. Studies example: quality_code_complexity_analysis.md
5. Builds custom prompt:

---
# React Accessibility Analysis Prompt

## Objective
Analyze React components for WCAG 2.1 AA accessibility compliance
and provide actionable remediation suggestions.

## Phase 1: Component Discovery
[Structured discovery using ST-04]

## Phase 2: Accessibility Audit
[Criteria-based analysis using RT-02]

## Phase 3: Issue Categorization
[Hierarchical summary using OC-03]

## Phase 4: Remediation Plan
[Actionable recommendations with verification using QA-01]

## Output Format
[Structured template using ST-03]
---

User: "Perfect! Save this as a new prompt file"
```

**Result:** Custom, high-quality prompt built using proven techniques

### Example 4: Strategic Product Planning

**Scenario:** Planning next quarter's product direction

**Claude Chat + Claude Code Workflow:**

```bash
# In Claude Chat: Strategic analysis
"Apply these business frameworks to our product:
1. business-analysis/swot-analysis.md
2. business-analysis/competitive-positioning-map.md
3. business-analysis/product-market-fit.md

Here's our product context: [details]"

# Output: Strategic insights and opportunities

# In Claude Code: Technical feasibility
"Based on the strategic opportunities identified,
use engineering-pre-code-canvas.md to plan
implementation of the top 3 initiatives"

# Output: Technical implementation plans

# Back to Claude Chat: Alignment
"Use business-analysis/okr-analysis.md to align
the technical plans with company objectives"

# Output: OKRs and key results
```

**Result:** Strategy → Technical Plan → Measurable Objectives

### Example 5: Code Review Automation

**Scenario:** Want consistent, high-quality code reviews

**Claude Code Workflow:**

```bash
# Create custom review workflow
"Build a code review workflow that combines:
- quality_code_complexity_analysis.md
- quality_documentation_coverage_analysis.md
- security/vulnerability_analysis.md
- learning/socratic-dialogue-code-review.md

Apply to all files in this PR"

# Claude executes:
1. Complexity analysis → identifies complex functions
2. Documentation check → finds undocumented code
3. Security scan → flags potential vulnerabilities
4. Socratic review → asks questions about design decisions

# Output: Comprehensive review with specific action items
```

**Result:** Thorough, consistent code reviews every time

---

## Resources and Further Learning

### Within This Repository

**Essential Reading:**
1. `AI_AGENT_QUICK_START.md` - Start here
2. `meta/vibe_coding_prompts.md` - Practical patterns
3. `meta/comprehensive_prompting_patterns.md` - Deep theory
4. `meta/failure_modes.md` - What to avoid
5. `skills/agentic_development.md` - Advanced workflows

**Reference Materials:**
- `techniques/MASTER_TECHNIQUE_INDEX.md` - All techniques
- `techniques/USE_CASE_LOOKUP.md` - Find by need
- `meta/model_quirks.md` - Claude-specific tips
- `meta/security_checklist.md` - Security best practices

### External Resources

**Official Documentation:**
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Claude Code Documentation](https://github.com/anthropics/claude-code)
- [Claude API Reference](https://docs.anthropic.com/claude/reference)

**Community Resources:**
- [Peter Steinberger's "Just Talk To It"](https://steipete.me/posts/just-talk-to-it)
- [OpenAI Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [Awesome Prompt Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering)

---

## Contributing to This Guide

### Feedback and Improvements

Found something unclear? Have suggestions? Want to add examples?

**How to contribute:**
1. Open an issue describing the improvement
2. Submit a PR with proposed changes
3. Share your success stories and workflows

**What we're looking for:**
- Real-world usage examples
- Claude-specific optimization tips
- New technique combinations
- Workflow improvements
- Troubleshooting solutions

---

## Frequently Asked Questions

### Q: Can I use these prompts with other AI models?

**A:** Yes! While optimized for Claude, these prompts work with:
- GPT-4 and GPT-3.5 (OpenAI)
- Cursor (various models)
- GitHub Copilot (OpenAI models)
- Any LLM-powered coding assistant

Some prompts may need minor adjustments for model-specific features.

### Q: Do I need Claude Code or can I use Claude Chat?

**A:** Both work, but have different strengths:
- **Claude Code:** Best for actual code analysis and modification
- **Claude Chat:** Best for learning, planning, and prototyping

Use both in combination for optimal results.

### Q: How do I know which prompt to use?

**A:** Three approaches:
1. **By category:** Browse directory structure
2. **By use case:** Check `techniques/USE_CASE_LOOKUP.md`
3. **Ask Claude:** "What prompt should I use to [describe task]?"

### Q: Can I modify these prompts?

**A:** Absolutely! Customization is encouraged:
- Adapt to your tech stack
- Add project-specific context
- Combine multiple prompts
- Create derivatives for your needs

### Q: How does the techniques library help?

**A:** It enables:
- Building custom prompts on-demand
- Improving existing prompts systematically
- Understanding why prompts work
- Consistent quality across all prompts

### Q: What's the difference between a prompt and a skill?

**A:**
- **Prompt:** Single-use template for a specific task
- **Skill:** Persistent capability Claude Code loads automatically

Skills are for frequently-used workflows; prompts are for ad-hoc tasks.

### Q: Can Claude build prompts for me?

**A:** Yes! That's what the techniques library enables:

```bash
"I need to [describe task]. Build me a prompt using
the techniques from techniques/"
```

### Q: How do I handle large codebases?

**A:** Strategies:
1. **Scope prompts:** Target specific directories/files
2. **Use parallel execution:** Claude Code runs multiple analyses simultaneously
3. **Hierarchical approach:** Start broad, then dive deep
4. **Iterative refinement:** Multiple passes with increasing specificity

---

## Conclusion

This repository is more than a collection of prompts—it's a **comprehensive system** for AI-assisted software development.

**Key Takeaways:**

✅ **93+ prompts** covering analysis, engineering, business, learning, and more

✅ **50+ techniques** cataloged and ready to use

✅ **Built for Claude** but works with any AI coding assistant

✅ **Systematic approach** to prompt engineering and usage

✅ **Continuously expanding** with new techniques and patterns

**Next Steps:**

1. **Explore** the prompt-techniques library
2. **Try** a few prompts on your current project
3. **Build** a custom prompt using the techniques
4. **Share** your experiences and contribute back

**Remember:** The best prompt is one that's customized for your specific context. Use this repository as a foundation, not a prescription.

---

**Happy Coding with Claude!** 🚀

*For issues, questions, or contributions, visit:*
*https://github.com/jr-mccoy/prompt-agent-engineering*

---

**Document Version:** 1.0
**Last Updated:** 2025-12-08
**Maintained for:** Claude Code, Claude Chat, and AI agent users
