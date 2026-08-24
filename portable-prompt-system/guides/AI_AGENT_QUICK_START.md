# AI Agent Quick Start: Building High-Quality Prompts

> **Root-level access for AI agents.** This guide provides fast reference for constructing effective **coding and technical prompts** on-demand.
>
> 📍 **Full documentation:** [`techniques/`](../techniques/) directory contains the complete technique library.

---

## Scope Note

**This guide is optimized for coding and technical prompts.** The techniques, patterns, and examples focus on:
- Code analysis, review, and debugging
- Architecture and design decisions
- Testing and quality assurance
- DevOps, cloud, and infrastructure
- Technical documentation

**For non-coding prompts, see [NON_CODING_QUICK_START.md](NON_CODING_QUICK_START.md).** That guide covers:
- **Education/Teaching:** Lesson plans, worksheets, assessments
- **Creative Writing:** Stories, essays, narratives
- **Healthcare/Clinical:** Patient communication, clinical decision support
- **Research/Academic:** Literature review, methodology, analysis
- **Personal Development:** Goals, habits, career planning
- **Professional Communication:** PRDs, presentations, proposals
- **Specialized Fields:** Legal, finance, trades, and 20+ professional domains

**Key difference:** Non-coding prompts require explicit audience specification, subjective quality criteria, and different verification approaches since you can't "run tests" on a lesson plan or executive summary.

---

## Creating a New Resource?

Use the **Authoring Toolkit** for consistent, high-quality prompts:

| Resource | Purpose |
|----------|---------|
| [NEW_PROMPT_TEMPLATE.md](NEW_PROMPT_TEMPLATE.md) | Copy-paste template with all required sections |
| [TECHNIQUE_PICKER_FAST.md](TECHNIQUE_PICKER_FAST.md) | Select 3–5 techniques by intent (ANALYZE, CREATE, FIX, etc.) |
| [NEW_RESOURCE_CHECKLIST.md](NEW_RESOURCE_CHECKLIST.md) | Pre-commit checklist for quality and placement |

---

## 5-Step Prompt Building Process

### Step 1: Classify User Intent (5 seconds)

Ask yourself: **What is the user fundamentally trying to do?**

- **ANALYZE** → User wants to understand, review, or evaluate something
- **CREATE** → User wants to generate new content, code, or documentation
- **DECIDE** → User needs to make a choice between options
- **LEARN** → User wants to understand how something works
- **FIX** → User has a problem to solve or bug to fix
- **PLAN** → User needs to organize a complex task or project
- **DELEGATE** → User wants to hand off a task with verifiable completion criteria

*Once classified, jump to corresponding section in this guide.*

---

### Step 2: Select Core Techniques (10 seconds)

Based on classification, pick **3-5 core techniques**.

> **Canonical Source:** For the most comprehensive and up-to-date technique combinations, see [USE_CASE_LOOKUP.md](../techniques/USE_CASE_LOOKUP.md). The quick reference below is a simplified summary.


#### For ANALYZE tasks:
```
REQUIRED:
- ST-01: Clear Objective Statement
- ST-02: Structured Sequential Instructions
- RT-02: Multi-Dimensional Analysis

USUALLY ADD:
- RT-05: Evidence-Based Reasoning
- ST-03: Output Format Specification
- DS-06: Prioritization Guidance
```

#### For CREATE tasks:
```
REQUIRED:
- CM-01: Explicit Context Framing
- ST-03: Explicit Output Specification
- CM-02: Constraint Specification

USUALLY ADD:
- ST-03/OC-02/OC-03: Output format (specification/JSON/tables)
- ED-05: Reference Class Priming (if format is complex—show example)
```

#### For DECIDE tasks:
```
REQUIRED:
- RT-03: Tree of Thoughts (multiple options)
- CM-01: Explicit Context Framing
- ST-03: Explicit Output Specification

FOR HIGH-STAKES:
- QA-01: Chain-of-Verification
- RP-03: Multi-Persona Debate
- QA-04: Uncertainty Acknowledgment
```

#### For LEARN tasks:
```
REQUIRED:
- RP-02: Audience-Specific Framing
- RT-01: Chain-of-Thought OR RT-04: Analogical Reasoning
- ST-04: Delimited Sections

FOR INTERACTIVE:
- ED-01: Iterative Scaffolding
- ED-03: Guided Discovery
```

#### For FIX tasks:
```
REQUIRED:
- RT-01: Chain-of-Thought
- RT-05: Evidence-Based Reasoning
- DT-01: Hierarchical Task Breakdown (for complex bugs)

USUALLY ADD:
- DT-01 + RT-05: Root cause focus (trace symptoms to underlying cause)
- RT-01: Step-by-step debugging approach
```

#### For PLAN tasks:
```
REQUIRED:
- DT-01: Hierarchical Task Breakdown
- ST-02: Structured Sequential Instructions
- CM-01: Explicit Context Framing

USUALLY ADD:
- Success criteria
- Dependency identification
- Risk assessment
```

#### For DELEGATE tasks (AI Agent Completion):
```
REQUIRED (Task Design):
- AG-27: End-State Task Specification (frame as outcomes with verification commands, not steps)
- AG-28: Oversight-Risk Calibration (match supervision intensity to risk/stakes/context)
- AG-33: Feedback Signal Inventory (catalog tests, linters, type checkers available)

REQUIRED (Verification):
- QA-08: Gate-Based Verification
- DD-04: MVP Gates (top 3 high-leverage gates)
- DD-06: Iteration Control (budget + stop policy)

USUALLY ADD:
- AG-29: Agent Loop Architecture (for complex/multi-iteration tasks — design the loop)
- AG-32: Pre-Execution Risk Audit (pre-flight footgun scan before kicking off agent work)
- DD-07: Self-Audit Table
- DD-05: Human Review Flags

USE PROMPTS:
- domain-engineering-workflows/ai-patterns/workflow_agent_task_specification.md → Convert task to agent-ready spec
- domain-engineering-workflows/ai-patterns/workflow_agent_oversight_calibration.md → Determine supervision level
- domain-engineering-workflows/ai-patterns/workflow_agent_loop_designer.md → Design iteration loop (complex tasks)
- domain-engineering-workflows/ai-patterns/workflow_agent_footgun_detector.md → Pre-flight risk audit
- domain-engineering-workflows/done-definition/done_definition_translator.md → Define the gates
- domain-engineering-workflows/done-definition/done_definition_loop_operator.md → Run the verification loop
```

---

### Step 3: Build Prompt Structure (30 seconds)

Use this universal template, customizing based on selected techniques:

```markdown
# [Task Name]

**Objective:** [One clear sentence - ST-01]

**Context:** [If using CM-01]
- [Relevant background]
- [Constraints]
- [Current state]

**Instructions:**

1. [First major step - ST-02]
   - [Sub-step if needed]
   - [Sub-step if needed]

2. [Second major step - often the core analysis/work]
   [If using RT-02, add:]
   For each [item], analyze:
   a. [Dimension 1]: [What to look for]
   b. [Dimension 2]: [What to look for]
   c. [Dimension 3]: [What to look for]

3. [Third major step - often synthesis/recommendations]

4. [Fourth step - if needed]

**Expected Output:** [Clear description - ST-03]
- [Structure of output]
- [Required sections]
- [Format specifications]

[If using ST-03 templates, add:]
**Format:**
[Template showing exact structure]
```

**Delimit injected content.** If the prompt has the model consume pasted material — a codebase, a document, a dataset, a log — wrap it in a named XML-style tag and reference that tag by name in the instructions. This stops the model from conflating your data with your instructions (a `##` header inside a pasted file looks just like one you wrote):

```markdown
**Instructions:**
1. Review the code in <codebase> for SQL injection risks.
2. For each finding, cite the file and line from <codebase>.

<codebase>
[pasted code goes here at use time]
</codebase>
```

Skip tags when there is no injected content. Full rationale and conventions: [PROMPT_STRUCTURE_GUIDE.md](PROMPT_STRUCTURE_GUIDE.md).

**Template Variations by Task Type:**

**For Code Analysis:**
```markdown
**Objective:** Analyze [codebase/component] for [specific aspect]

**Instructions:**
1. Review the codebase and identify [specific issues]

2. For each identified issue, analyze:
   a. Location: File path, line number(s)
   b. Description: What the issue is
   c. Impact: Effect on [quality attribute]
   d. Severity: Low/Medium/High
   e. Recommendations: Specific fixes with rationale

3. Identify patterns or trends across findings

4. If no significant issues found, provide summary stating [acceptable state]

**Expected Output:** Report including:
1. Overview of findings
2. Detailed issue breakdowns using format:
   File: [path]
   Line(s): [numbers]
   Issue: [description]
   Impact: [impact]
   Severity: [level]
   Suggestions:
   - [fix 1]
   - [fix 2]
3. Patterns observed
4. General recommendations
```

**For Decision Making:**
```markdown
**Context:**
- Current situation: [...]
- Requirements: [...]
- Constraints: [...]

**Decision:** [What needs to be decided]

**Instructions:**
Generate 3 different approaches to [decision]:

For each approach:
1. Describe how it works
2. List pros (advantages)
3. List cons (disadvantages)
4. Identify best-fit scenarios

Then provide recommendation:
- Which approach is best for this context
- Why it's the best choice
- What tradeoffs are acceptable
- What risks remain

**Expected Output:**
## Approach 1: [Name]
[Details, pros, cons, best for]

## Approach 2: [Name]
[Details, pros, cons, best for]

## Approach 3: [Name]
[Details, pros, cons, best for]

## Recommendation
[Decision with full reasoning]
```

**For Teaching:**
```markdown
**Objective:** Explain [concept/code] for [audience type]

**Audience characteristics:**
- Knowledge level: [beginner/intermediate/advanced]
- Background: [what they know]
- Goal: [what they want to achieve]

**Instructions:**
1. Start with a simple analogy from [familiar domain]

2. Explain the core concept step-by-step:
   - First, [foundational idea]
   - Then, [build on it]
   - Finally, [complete picture]

3. Provide concrete examples

4. Address common misconceptions

5. Suggest next steps for learning

**Expected Output:**
## Simple Analogy
[Relatable comparison]

## Core Explanation
[Step-by-step breakdown]

## Examples
[Concrete illustrations]

## Common Mistakes
[What to avoid]

## Next Steps
[How to practice/learn more]
```

---

### Step 4: Add Quality Layers (15 seconds)

**Ask:** Is this request high-stakes, critical, or does the user need high confidence?

**If YES, add one of these quality checks:**

**Quick quality check (add to instructions):**
```
After providing your analysis:
- Review for potential oversights or errors
- State any assumptions you made
- Flag any uncertainties
```

**Medium quality check (Chain-of-Verification):**
```
After providing your initial response:

**Verification:**
1. List three ways this could be incomplete or incorrect
2. For each concern, cite evidence that confirms or refutes it
3. Provide revised response incorporating corrections
```

**High quality check (Full stress-test):**
```
After providing your initial response:

**Self-Critique:**
1. Identify five ways this could be wrong or fail
2. Rate each: Severity (Critical/High/Medium/Low) and Likelihood
3. Propose specific revisions for each issue
4. Provide hardened version incorporating all improvements
```

**For strategic decisions, add Multi-Persona Debate:**
```
Simulate structured debate between three experts:

**Persona 1: [Role focusing on X]**
Priority: [Their focus]
Position: [Their view]

**Persona 2: [Role focusing on Y]**
Priority: [Their focus]
Position: [Their view]

**Persona 3: [Role focusing on Z]**
Priority: [Their focus]
Position: [Their view]

Each persona:
1. Presents their position (3-4 paragraphs)
2. Critiques the other positions
3. Final synthesis reconciles all perspectives
```

---

### Step 5: Customize & Execute (10 seconds)

**Quick customization checklist:**

- [ ] Replace all [placeholders] with actual values
- [ ] Remove techniques not needed for this specific request
- [ ] Add any domain-specific requirements (language version, framework, etc.)
- [ ] Verify output format matches user's needs
- [ ] Check that all user constraints are included

**Then execute the prompt!**

---

## Common Patterns Library

### Pattern: High-Quality Code Analysis

```markdown
**Objective:** Analyze codebase for [SPECIFIC ASPECT]

**Instructions:**
1. Review the codebase focusing on [SPECIFIC CRITERIA]

2. For each identified issue:
   a. Location: File path, line number(s)
   b. Description: Clear explanation of the issue
   c. Impact: Effect on [QUALITY ATTRIBUTES]
   d. Severity: Low/Medium/High
   e. Recommendations: Specific fixes with reasoning

3. Identify patterns: Are there systemic issues or trends?

4. Prioritize findings by [CRITERIA]

5. If no issues found, state that [ASPECT] is at acceptable levels

**Expected Output:**
1. Executive summary
2. Detailed findings (using format above)
3. Patterns and trends
4. Prioritized action items
```

**Use this for:** complexity, duplication, security, performance, quality

---

### Pattern: Strategic Framework Application

```markdown
**Objective:** Conduct [FRAMEWORK NAME] analysis of [TARGET]

**Context:**
- [Business context]
- [Technical context]
- [Goals]

**Instructions:**
1. Review [TARGET] thoroughly

2. Analyze according to [FRAMEWORK] structure:

   [FRAMEWORK DIMENSION 1]:
   - [Specific questions]
   - [What to evaluate]

   [FRAMEWORK DIMENSION 2]:
   - [Specific questions]
   - [What to evaluate]

   [Continue for all dimensions]

3. For each point, provide specific examples from [TARGET]

4. Synthesize insights and provide strategic recommendations

**Expected Output:**
Comprehensive [FRAMEWORK] analysis with:
- Findings for each framework dimension
- Specific supporting evidence
- Strategic recommendations
- Action items
```

**Use this for:** SWOT, Porter's Five Forces, Business Model Canvas, OKRs, etc.

---

### Pattern: Multi-Option Decision

```markdown
**Context:**
- Current state: [...]
- Requirements: [...]
- Constraints: [...]
- Success criteria: [...]

**Decision:** [WHAT TO DECIDE]

**Instructions:**
1. Generate 3 viable approaches to address this decision

2. For each approach, provide:
   - Name and brief description
   - How it works
   - Pros (specific advantages)
   - Cons (specific disadvantages)
   - Best-fit scenarios
   - Risk factors

3. Compare approaches on key criteria:
   - [Criterion 1]
   - [Criterion 2]
   - [Criterion 3]

4. Provide recommendation:
   - Which approach is best and why
   - What tradeoffs are acceptable
   - What risks need mitigation
   - Implementation considerations

**Expected Output:**
## Options Analysis
[Three approaches with full details]

## Comparison
[Side-by-side on key criteria]

## Recommendation
[Clear decision with full reasoning]
```

---

### Pattern: Interactive Teaching

```markdown
You are a [ROLE - e.g., friendly tutor, senior developer].

**Student profile:**
- Name: [Ask first]
- Learning goal: [Ask first]
- Current level: [Assess]
- Interests: [Ask to incorporate]

**Teaching approach:**
1. Assess knowledge with questions (one at a time)

2. Teach concepts in bite-sized pieces:
   - Explain one concept
   - Ask for understanding rating (1-3)
   - If 1: Re-explain more slowly
   - If 2: Provide more examples
   - If 3: Move to exercises

3. Create exercises:
   - Code tasks: Provide boilerplate, ask to complete
   - Debugging tasks: Code with error, ask to fix
   - Output tasks: Ask to predict output

4. When student completes exercise:
   - Don't immediately reveal errors
   - Ask guiding questions
   - Help them discover the answer

**Important guidelines:**
- Ask ONLY ONE QUESTION at a time
- Be friendly but concise
- Use student's name
- Incorporate their interests
- Create lesson files: 001-lesson-[topic]
- Create exercise files: 002-exercise-[topic]
- Keep lessons as sources of truth (edit to improve)
- Don't edit exercises (create new ones for follow-ups)
```

---

### Pattern: Root Cause Debugging

```markdown
**Objective:** Debug [ISSUE] and identify root cause

**Evidence:**
- Error message: [...]
- Stack trace: [...]
- Expected behavior: [...]
- Actual behavior: [...]
- Steps to reproduce: [...]

**Instructions:**
Think through this step-by-step:

1. **Analyze the evidence:**
   - What does the error message tell us?
   - What does the stack trace reveal?
   - Where does the actual behavior diverge from expected?

2. **Form hypotheses:**
   - What are 2-3 possible root causes?
   - For each, what evidence supports or contradicts it?

3. **Identify the root cause:**
   - Not just the symptom, but the underlying reason
   - Trace the causal chain

4. **Provide the fix:**
   - Specific code changes
   - Explanation of why this fixes the root cause
   - Why other approaches wouldn't work

5. **Prevention:**
   - How to prevent this class of issues
   - What tests or checks would catch it

**Expected Output:**
## Analysis
[Step-by-step reasoning]

## Root Cause
[The actual underlying problem]

## Fix
[Specific solution with explanation]

## Prevention
[How to avoid in future]
```

---

## Technique Quick Reference

**When you need:**

→ **Clear task definition** = ST-01: Clear Objective Statement
→ **Step-by-step workflow** = ST-02: Structured Sequential Instructions
→ **Consistent output** = ST-03: Output Format Specification OR OC-02: JSON Schema
→ **Deep reasoning** = RT-01: Chain-of-Thought
→ **Complete analysis** = RT-02: Multi-Dimensional Analysis Framework
→ **Multiple options** = RT-03: Tree of Thoughts
→ **Self-correction** = QA-01: Chain-of-Verification
→ **Attack your answer** = QA-02: Adversarial Stress-Test
→ **Clear explanations** = RT-04: Analogical Reasoning
→ **Specific examples** = ED-05: Reference Class Priming
→ **Expert perspective** = RP-01: Expert Role Assignment
→ **Right audience level** = RP-02: Audience-Specific Framing
→ **Different viewpoints** = RP-03: Multi-Persona Debate
→ **Interactive learning** = ED-01: Iterative Scaffolding
→ **Break down complexity** = DT-01: Hierarchical Task Breakdown
→ **Necessary background** = CM-01: Explicit Context Framing
→ **Clear boundaries** = CM-02: Constraint Specification
→ **Proof and evidence** = RT-05: Evidence-Based Reasoning
→ **Ranked results** = DS-06: Prioritization Guidance
→ **System prompt design** = CM-11: Reasoning-Based Constraint Design + CM-14: Principal Hierarchy Specification + CM-15: Gap-Filling Intent Signaling
→ **Better AI communication** = CM-12: Multi-Lens Request Framing + RP-06: Expert Friend Positioning
→ **Handle AI pushback** = IT-10: Principled Pushback Navigation + CM-13: Distinguishing Context Provision
→ **Toggle AI defaults** = IT-11: Non-Default Behavior Activation
→ **Test for both failures** = QA-20: Dual-Failure Quality Test (harmful AND unhelpful)

---

## Decision Tree: Technique Selection

```
START: User makes request
│
├─→ Is output format critical?
│   YES → Add ST-03 (specification) or OC-02 (JSON) or OC-03 (tables)
│   NO → Continue
│
├─→ Does this require deep reasoning?
│   YES → Add RT-01 (Chain-of-Thought)
│   NO → Continue
│
├─→ Is this analysis/review of code or system?
│   YES → Add ST-01, ST-02, RT-02, RT-05, ST-03
│   NO → Continue
│
├─→ Is this a decision between options?
│   YES → Add RT-03 (Tree of Thoughts) + CM-01
│   NO → Continue
│
├─→ Is this teaching/explaining?
│   YES → Add RP-02 + RT-04 or ED-01
│   NO → Continue
│
├─→ Is this creating new content?
│   YES → Add CM-01 + CM-02 + ST-03
│   NO → Continue
│
├─→ Is this high-stakes or critical?
│   YES → Add QA-01 or QA-02
│   NO → Continue
│
└─→ Execute with selected techniques
```

---

## Checklist: Before Executing Prompt

- [ ] **Clear objective?** Does the first line state exactly what we're trying to accomplish?
- [ ] **Structured instructions?** Are steps numbered and logical?
- [ ] **Output specified?** Is it crystal clear what format/structure is expected?
- [ ] **Context provided?** Does the AI have all necessary background?
- [ ] **Quality appropriate?** High-stakes requests have verification steps?
- [ ] **Constraints clear?** Are must/must-not requirements explicit?
- [ ] **Placeholders replaced?** No [brackets] remain in final prompt?

If all checked, **execute the prompt**.

---

## Common Mistakes to Avoid

**❌ Too many techniques** → Stick to 3-5 core techniques
**❌ Vague objectives** → Always use ST-01 with specific goal
**❌ No output specification** → Always specify format/structure
**❌ Missing context** → Provide background with CM-01
**❌ No quality check on critical work** → Add QA-01 or QA-02
**❌ Forgetting evidence** → Analysis needs RT-05 (specific examples, line numbers)
**❌ Not matching audience** → Use RP-02 for teaching/explaining
**❌ Pasting data inline with instructions** → Wrap injected content (code, docs, data) in named tags so the model doesn't conflate it with instructions (ST-04)

---

## Time-Saving Tips

1. **Start with patterns** from Common Patterns Library above
2. **Reuse prompts** that worked well (ED-05: Reference Class Priming)
3. **Keep it simple** - don't add techniques you don't need
4. **Use templates** - fill in blanks faster than writing from scratch
5. **Check the lookup** - USE_CASE_LOOKUP.md has ready-to-use patterns

---

## When You're Stuck

**Problem:** Not sure which techniques to use
**Solution:** Go to USE_CASE_LOOKUP.md → find user's use case → copy recommended techniques

**Problem:** Prompt is getting too complex
**Solution:** Remove optional techniques, keep only REQUIRED ones

**Problem:** Not sure about output format
**Solution:** Always add ST-03 (Explicit Output Specification) + show example

**Problem:** User's request is ambiguous
**Solution:** Use MP-03 (Task Clarification) - ask questions first

**Problem:** High-stakes decision, need confidence
**Solution:** Add QA-01 (Chain-of-Verification) or full QA-02 (Adversarial Stress-Test)

**Problem:** Model is conflating my pasted data with my instructions
**Solution:** Wrap the injected content in named XML-style tags (e.g. `<codebase>...</codebase>`) and reference the tag by name in the steps — see [PROMPT_STRUCTURE_GUIDE.md](PROMPT_STRUCTURE_GUIDE.md)

---

## Deep Dive Resources

For comprehensive technique documentation:

| Resource | Purpose |
|----------|---------|
| [`../techniques/MASTER_TECHNIQUE_INDEX.md`](../techniques/MASTER_TECHNIQUE_INDEX.md) | Complete catalog of 250 formally defined techniques across 19 categories |
| [`../techniques/USE_CASE_LOOKUP.md`](../techniques/USE_CASE_LOOKUP.md) | Find techniques by user need |
| [`PROMPT_STRUCTURE_GUIDE.md`](PROMPT_STRUCTURE_GUIDE.md) | Structuring prompts, delimiting injected content, and diagnosing prompts that don't work |
| [`domain-engineering-workflows/done-definition/`](../../domain-engineering-workflows/done-definition/) | **AI Agent Task Completion** - Gate-based verification for verifiable task completion (9 prompts, 11 techniques) |

---

**Remember:** A simple, well-structured prompt beats a complex, unfocused one every time. When in doubt, use:
1. ST-01 (Clear Objective)
2. ST-02 (Structured Steps)
3. ST-03 (Output Specification)

Then add 1-2 specialized techniques for the specific task.

**You're ready! Start building high-quality prompts now.**

---

## Section 6: Using Claude Code Resources

> **Portable-bundle note:** The "Claude Code Resources" referenced in this section (the `domain-agentic-resources/` agent / skill / command **implementation** library, with its index links and counts) belong to the *source* repository and are **NOT** included in this portable bundle. What *is* bundled is the complete system for **authoring** your own skills, agents, and commands — see [`../resource-patterns/`](../resource-patterns/). Treat the `domain-agentic-resources/...` links below as references to the source library.

This repository now includes **361 Claude Code resources** (158 agents, 132 skills, 71 commands) in addition to the 261+ general-purpose prompts. Understanding when to use each type of resource will help you work more efficiently.

### Difference: Prompts vs Agents/Skills/Commands

#### **Prompts (this repository)**
- **One-time use:** Copy and paste into any conversation
- **Model-agnostic:** Work with any AI model (Claude, GPT, etc.)
- **Immediate activation:** Paste with your context and go
- **Portable:** No installation or setup required
- **Best for:**
  - Ad-hoc analysis and one-off tasks
  - Quick code reviews
  - Exploratory questions
  - Working outside Claude Code environment
  - Sharing with team members who don't use Claude Code

#### **Agents (Claude Code)**
- **Persistent identities:** Pre-configured expert personas that activate automatically
- **Model-optimized:** Each agent assigned optimal model (Opus 4.5 for critical work, Sonnet for balanced, Haiku for speed)
- **Multi-agent orchestration:** Multiple agents can work together in workflows
- **Proactive activation:** Trigger automatically based on context patterns
- **Best for:**
  - Ongoing development in persistent environment
  - Complex workflows requiring multiple specialties
  - Cost optimization through model tiering
  - Production development workflows

**Example agents:**
- `security-auditor` (Opus 4.5) - Critical security review
- `python-architect` (Sonnet 4.5) - Python development
- `frontend-developer` (Sonnet 4.5) - UI/UX implementation

#### **Skills (Claude Code)**
- **Progressive disclosure:** Three-tier loading (metadata → instructions → bundled resources)
- **Bundled resources:** Include scripts, references, templates, and documentation
- **Tool integrations:** Connect with external tools (gh CLI, kubectl, terraform, etc.)
- **Knowledge packages:** Large domain expertise loaded only when needed
- **Best for:**
  - Repeated workflows with specific tools
  - Domain expertise requiring extensive documentation
  - Workflows with executable scripts
  - Context-efficient access to large knowledge bases

**Example skills:**
- `helm-chart-scaffolding` - Generate production-ready Helm charts
- `github-ops` - Comprehensive GitHub operations with API reference
- `security-scanning` - Automated SAST patterns with bundled tools

#### **Commands (Claude Code)**
- **Multi-agent coordination:** Orchestrate 2-7+ agents in sequence
- **Complex workflows:** Multi-phase operations with validation gates
- **Automated pipelines:** Feature development, deployment, testing workflows
- **Quality gates:** Each phase validates before proceeding to next
- **Best for:**
  - Full-stack feature development
  - Multi-phase deployments
  - Comprehensive security assessments
  - Complex troubleshooting workflows

**Example commands:**
- `/full-stack-feature` - Coordinate 7 agents for feature development
- `/security-hardening` - Multi-agent comprehensive security assessment
- `/issue-resolution` - End-to-end bug investigation and fix

### When to Use Claude Code Resources

#### **Use Claude Code Resources if:**
✅ Working in persistent development environment
✅ Need multi-agent coordination for complex workflows
✅ Require model optimization for cost/performance
✅ Want progressive disclosure for large knowledge bases
✅ Need bundled scripts, templates, and tools
✅ Building production systems with ongoing maintenance
✅ Working on long-running projects with context accumulation

#### **Use General Prompts if:**
✅ One-time analysis or review
✅ Not using Claude Code environment
✅ Need quick ad-hoc evaluation
✅ Want portable, copy-paste solutions
✅ Sharing with team members on different platforms
✅ Exploring new approaches without commitment
✅ Working with non-Claude AI models

### Augmenting Prompts with Claude Code Patterns

Even when building general prompts, you can apply patterns discovered in Claude Code resources:

#### **1. Progressive Disclosure Pattern**
Break large prompts into tiers to minimize context usage:

```markdown
# Metadata (Always loaded)
**Name:** Security Vulnerability Analysis
**Use when:** Analyzing code for security issues
**Model recommendation:** Opus 4.5 for critical systems

# Core Instructions (Load when activated)
[Your main prompt goes here]

# References (Load only if needed)
[Detailed OWASP guidelines, CVE patterns, etc.]
```

**Why this works:** Users get quick discoverability without loading full context until needed.

#### **2. Model Tiering Strategy**
Assign appropriate model based on task criticality:

```markdown
**Recommended Models:**
- **Opus 4.5:** Use for architecture decisions, security audits, production code review
- **Sonnet 4.5:** Use for feature implementation, testing, documentation
- **Haiku 4.5:** Use for formatting, quick checks, simple refactoring
```

**Why this works:** Optimize cost/performance tradeoff—reserve expensive models for high-stakes work.

#### **3. Bundled Resources Pattern**
Package related resources with your prompt:

```markdown
**Core Prompt:** [Main instructions]

**Bundled Resources:**
- `scripts/security_scan.py` - Automated SAST scanner
- `references/owasp_top_10.md` - Security checklist
- `templates/security_report.md` - Output template
```

**Why this works:** Self-contained prompts are more reusable and portable.

#### **4. Multi-Phase Workflow Pattern**
Structure complex tasks with validation gates:

```markdown
**Phase 1: Analysis**
[Instructions for initial review]
→ Checkpoint: Validate findings before proceeding

**Phase 2: Recommendations**
[Instructions for solutions]
→ Checkpoint: Review recommendations for feasibility

**Phase 3: Implementation Plan**
[Instructions for execution plan]
→ Final validation
```

**Why this works:** Prevents cascading errors by validating each phase before next step.

### Integration with Existing Prompts

This repository now provides **bidirectional mapping** between prompts and Claude Code resources:

- **Every prompt category** maps to relevant agents, skills, and commands
- **Example:** Security analysis prompts → `security-auditor` agent → `security-scanning` skill → `/security-hardening` command


### Hybrid Workflow Examples

#### **Example 1: Security Audit Workflow**
1. **Start:** Use `security_vulnerability_analysis.md` prompt for initial scan
2. **Deep dive:** Activate `security-auditor` agent (Opus 4.5) for persistent review
3. **Automation:** Install `security-scanning` skill for CI/CD integration
4. **Comprehensive:** Run `/security-hardening` command for multi-agent assessment

#### **Example 2: Performance Optimization Workflow**
1. **Initial analysis:** Use `performance_bottleneck_identification.md` prompt
2. **Ongoing work:** Activate `performance-engineer` agent
3. **Tool integration:** Use `profiling-tools` skill with bundled scripts
4. **Load testing:** Run `/performance-test` command

#### **Example 3: Learning Workflow**
1. **Concept explanation:** Use `learning_teach_me_to_code.md` prompt
2. **Interactive tutoring:** Activate `teaching-assistant` agent
3. **Practice exercises:** Use `code-kata-generator` skill
4. **Project-based learning:** Run `/learning-project` command

### Quick Decision Tree

```
Your Task
│
├─→ Are you using Claude Code?
│   ├─ YES → Continue to question 2
│   └─ NO → Use general prompts (copy-paste from repository)
│
├─→ Is this a one-time task or ongoing workflow?
│   ├─ ONE-TIME → Use general prompts
│   └─ ONGOING → Use Claude Code resources
│
├─→ Do you need multi-agent coordination?
│   ├─ YES → Use Command (domain-agentic-resources/commands/)
│   └─ NO → Continue to question 4
│
├─→ Do you have large domain knowledge to reference?
│   ├─ YES → Use Skill (progressive disclosure)
│   └─ NO → Continue to question 5
│
└─→ Do you need model optimization (cost/performance)?
    ├─ YES → Use Agent (model-tiered)
    └─ NO → Use general prompts (model-agnostic)
```

### Cost Optimization with Model Tiering

Claude Code agents use strategic model assignment to optimize costs:

| Model | Cost (per MTok) | Use For | Examples |
|-------|----------------|---------|----------|
| **Opus 4.5** | Highest | Critical decisions, security, architecture | `security-auditor`, `architect-review`, `code-reviewer` |
| **Sonnet 4.5** | Medium | Feature development, testing, documentation | `python-architect`, `frontend-developer`, `test-automator` |
| **Haiku 4.5** | Lowest | Fast operations, formatting, simple tasks | `code-formatter`, `documentation-generator` |
| **Inherit** | User choice | Framework-specific, user preference | `react-expert`, `vue-specialist` |

**Cost savings example:**
- Using Opus for all tasks: $X
- Using model tiering (36 Opus / 43 Sonnet / 18 Haiku): ~40-60% cost reduction

### Explore Claude Code Resources

**Browse by category:**
- Agents Index - 158 agents across 16 categories
- Skills Index - 132 skills across 21 categories
- Commands Index - 71 commands across 15 categories

**Integration guides:**
- [Integration Guide](../../domain-agentic-resources/documentation/integration_with_prompts.md) - Complete guide for combining prompts with Claude Code

**Novel techniques from Claude Code:**
- [New Techniques](../techniques/new-techniques/) - 12 high-priority techniques extracted from Claude Code resources
- [Updated Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md) - 250 formally defined techniques across 19 categories

### Summary: When to Use What

| Need | Use This | Why |
|------|----------|-----|
| Quick code review | **Prompt** | Fast, portable, no setup |
| Ongoing development | **Agent** | Persistent context, model-optimized |
| Tool automation | **Skill** | Bundled scripts, references, progressive disclosure |
| Complex workflows | **Command** | Multi-agent orchestration, validation gates |
| Learning & teaching | **Prompt** then **Agent** | Prompt for concepts, agent for interactive practice |
| Production deployment | **Command** then **Agent** | Command for pipeline, agent for maintenance |

**Key insight:** Prompts and Claude Code resources are complementary—use prompts for exploration and one-off tasks, then graduate to agents/skills/commands for production workflows.
