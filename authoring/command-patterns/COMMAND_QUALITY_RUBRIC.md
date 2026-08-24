# Command Quality Rubric

**Purpose:** Score commands on a 100-point scale for quality assurance
**Target Score:** 75/100 for production-ready commands
**Usage:** Evaluate each section, sum scores, identify improvement areas

---

## Table of Contents

1. [Scoring Overview](#scoring-overview)
2. [Category Breakdown](#category-breakdown)
3. [Detailed Criteria](#detailed-criteria)
   - [Workflow Structure (20 pts)](#1-workflow-structure-20-points)
   - [Agent Configuration (20 pts)](#2-agent-configuration-20-points)
   - [Validation & Gates (15 pts)](#3-validation--gates-15-points)
   - [Error Handling (15 pts)](#4-error-handling-15-points)
   - [Documentation (15 pts)](#5-documentation-15-points)
   - [Configuration (10 pts)](#6-configuration-10-points)
   - [Bonus Points (5 pts)](#7-bonus-points-5-points)
4. [Score Interpretation](#score-interpretation)
5. [Quick Evaluation Checklist](#quick-evaluation-checklist)
6. [Common Deductions](#common-deductions)
7. [Improvement Guide](#improvement-guide)

---

## Scoring Overview

### Score Distribution

| Category | Points | Weight |
|----------|--------|--------|
| Workflow Structure | 20 | 20% |
| Agent Configuration | 20 | 20% |
| Validation & Gates | 15 | 15% |
| Error Handling | 15 | 15% |
| Documentation | 15 | 15% |
| Configuration | 10 | 10% |
| Bonus Points | 5 | 5% |
| **Total** | **100** | **100%** |

### Quality Tiers

| Score | Tier | Status |
|-------|------|--------|
| 90-100 | Exemplary | Gold standard, reference material |
| 80-89 | Excellent | Production-ready, minor improvements possible |
| 75-79 | Good | Production-ready, meets standards |
| 65-74 | Acceptable | Functional, needs improvement |
| 50-64 | Needs Work | Significant gaps, revise before use |
| <50 | Incomplete | Not ready for use |

---

## Category Breakdown

### Visual Score Card

```
┌─────────────────────────────────────────────────────────────┐
│                    COMMAND QUALITY RUBRIC                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  WORKFLOW STRUCTURE                     [    /20]           │
│  ████████████████████                                       │
│                                                             │
│  AGENT CONFIGURATION                    [    /20]           │
│  ████████████████████                                       │
│                                                             │
│  VALIDATION & GATES                     [    /15]           │
│  ███████████████                                            │
│                                                             │
│  ERROR HANDLING                         [    /15]           │
│  ███████████████                                            │
│                                                             │
│  DOCUMENTATION                          [    /15]           │
│  ███████████████                                            │
│                                                             │
│  CONFIGURATION                          [    /10]           │
│  ██████████                                                 │
│                                                             │
│  BONUS                                  [    /5]            │
│  █████                                                      │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  TOTAL SCORE                            [    /100]          │
│  TIER: ___________                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Detailed Criteria

### 1. Workflow Structure (20 Points)

How well the command organizes work into logical phases.

#### 1.1 Phase Organization (8 points)

| Score | Criteria |
|-------|----------|
| 8 | 4-6 well-defined phases with clear purposes and descriptive names |
| 6 | 3-4 phases, clear purposes, mostly descriptive names |
| 4 | Has phases but unclear boundaries or generic names |
| 2 | Minimal phase structure, hard to follow flow |
| 0 | No phase structure, monolithic command |

**Evaluation Questions:**
- Are phases named descriptively (not "Phase 1, Phase 2")?
- Does each phase have a clear purpose?
- Is the phase count appropriate (3-6)?
- Are phase boundaries logical?

#### 1.2 Step Sequencing (6 points)

| Score | Criteria |
|-------|----------|
| 6 | Steps numbered consecutively, dependencies clear, parallel tasks marked |
| 4 | Steps numbered, most dependencies clear |
| 2 | Steps present but unclear sequencing |
| 0 | No clear step structure |

**Evaluation Questions:**
- Are steps numbered across phases?
- Are parallel tasks explicitly marked?
- Are dependencies stated?

#### 1.3 Context Flow (6 points)

| Score | Criteria |
|-------|----------|
| 6 | Explicit context passing between all dependent steps with specific outputs |
| 4 | Context passing present for most steps |
| 2 | Some context references but incomplete |
| 0 | No context passing defined |

**Evaluation Questions:**
- Is "Context from previous" specified where needed?
- Are specific outputs referenced, not entire phases?
- Does context accumulate appropriately?

---

### 2. Agent Configuration (20 Points)

How well agents are selected and configured.

#### 2.1 Agent Selection (6 points)

| Score | Criteria |
|-------|----------|
| 6 | Optimal agent for each task, uses composite paths for specialization |
| 4 | Appropriate agents, some could be more specific |
| 2 | Generic agents used where specialists available |
| 0 | Incorrect or missing agent selection |

**Evaluation Questions:**
- Are specialized agents used (e.g., `security-scanning::security-auditor`)?
- Does each agent match the task requirements?
- Are conditional selections documented?

#### 2.2 Prompt Quality (8 points)

| Score | Criteria |
|-------|----------|
| 8 | Detailed prompts with action verb, numbered requirements, output format, constraints |
| 6 | Good prompts with most elements present |
| 4 | Basic prompts, missing some detail |
| 2 | Vague prompts, unclear instructions |
| 0 | Missing or unusable prompts |

**Prompt Quality Checklist:**
- [ ] Starts with clear action verb
- [ ] Includes $ARGUMENTS reference
- [ ] Has numbered requirements (3+)
- [ ] Specifies output format
- [ ] Notes constraints/context

#### 2.3 Output Specification (6 points)

| Score | Criteria |
|-------|----------|
| 6 | Every step has detailed expected output with format and components |
| 4 | Most steps have output specs, some generic |
| 2 | Few output specifications, mostly vague |
| 0 | No output specifications |

**Evaluation Questions:**
- Is "Expected output" defined for each step?
- Are output components listed?
- Is format specified where relevant (JSON, Markdown)?

---

### 3. Validation & Gates (15 Points)

Quality control mechanisms within the command.

#### 3.1 Phase Gates (6 points)

| Score | Criteria |
|-------|----------|
| 6 | Explicit gates between major phases with clear conditions |
| 4 | Gates present for critical transitions |
| 2 | Some validation but not formalized as gates |
| 0 | No phase gates defined |

**Gate Examples:**
```markdown
- **GATE**: Do not proceed until all tests pass
- **GATE**: Block if CVSS 7+ vulnerabilities found
```

#### 3.2 Success Criteria (6 points)

| Score | Criteria |
|-------|----------|
| 6 | Comprehensive, measurable success criteria covering technical, process, and operational aspects |
| 4 | Good success criteria, mostly measurable |
| 2 | Basic success criteria, not measurable |
| 0 | No success criteria defined |

**Success Criteria Quality:**
- [ ] Are criteria measurable (numbers, yes/no)?
- [ ] Cover technical outcomes?
- [ ] Cover process requirements?
- [ ] Cover operational readiness?

#### 3.3 Convergence Points (3 points)

| Score | Criteria |
|-------|----------|
| 3 | Explicit convergence points after parallel work with completion checklist |
| 2 | Convergence mentioned but not detailed |
| 1 | Implicit convergence |
| 0 | No convergence handling for parallel work |

---

### 4. Error Handling (15 Points)

Recovery and resilience mechanisms.

#### 4.1 Rollback Procedures (6 points)

| Score | Criteria |
|-------|----------|
| 6 | Detailed rollback with specific commands, multiple scenarios covered |
| 4 | Basic rollback documented |
| 2 | Rollback mentioned but not detailed |
| 0 | No rollback procedures |

**Rollback Checklist:**
- [ ] Specific commands provided
- [ ] Multiple failure scenarios covered
- [ ] Communication steps included
- [ ] Root cause analysis mentioned

#### 4.2 Failure Recovery (5 points)

| Score | Criteria |
|-------|----------|
| 5 | Recovery steps for each phase failure with clear actions |
| 3 | Some failure recovery documented |
| 1 | Basic error handling mentioned |
| 0 | No failure recovery |

#### 4.3 Escalation Paths (4 points)

| Score | Criteria |
|-------|----------|
| 4 | Clear escalation levels with triggers and contacts |
| 2 | Basic escalation mentioned |
| 0 | No escalation defined |

---

### 5. Documentation (15 Points)

How well the command is documented and explained.

#### 5.1 Extended Thinking (4 points)

| Score | Criteria |
|-------|----------|
| 4 | Comprehensive extended thinking explaining methodology, approach, and design decisions |
| 2 | Basic extended thinking present |
| 0 | No extended thinking |

**Extended Thinking Quality:**
- [ ] Explains methodology/approach
- [ ] Notes key design decisions
- [ ] 3-5 sentences

#### 5.2 Coordination Notes (4 points)

| Score | Criteria |
|-------|----------|
| 4 | Detailed coordination notes explaining agent interaction, feedback loops, timing |
| 2 | Basic coordination mentioned |
| 0 | No coordination documentation |

#### 5.3 Reference Material (4 points)

| Score | Criteria |
|-------|----------|
| 4 | Includes reference workflows, best practices, or anti-patterns |
| 2 | Some reference material |
| 0 | No reference documentation |

#### 5.4 Clarity and Readability (3 points)

| Score | Criteria |
|-------|----------|
| 3 | Clear formatting, consistent structure, easy to follow |
| 2 | Mostly readable, some inconsistencies |
| 1 | Hard to follow, inconsistent |
| 0 | Poorly formatted, confusing |

---

### 6. Configuration (10 Points)

Flexibility and customization options.

#### 6.1 Flag Options (4 points)

| Score | Criteria |
|-------|----------|
| 4 | Multiple useful flags with clear descriptions and effects |
| 2 | Some flags defined |
| 0 | No flags |

#### 6.2 Parameter Configuration (3 points)

| Score | Criteria |
|-------|----------|
| 3 | Named parameters with valid values and defaults documented |
| 2 | Basic parameters defined |
| 0 | No parameters |

#### 6.3 Mode Selection (3 points)

| Score | Criteria |
|-------|----------|
| 3 | Multiple modes (quick/standard/comprehensive) with clear tradeoffs |
| 2 | Basic mode options |
| 0 | No mode selection |

---

### 7. Bonus Points (5 Points)

Exceptional qualities.

#### 7.1 Innovation (2 points)

| Score | Criteria |
|-------|----------|
| 2 | Novel approach, creative pattern usage, unique coordination |
| 1 | Some innovative elements |
| 0 | Standard approach |

#### 7.2 Reusability (2 points)

| Score | Criteria |
|-------|----------|
| 2 | Highly reusable across different contexts, technology-agnostic |
| 1 | Moderately reusable |
| 0 | Context-specific only |

#### 7.3 Completeness (1 point)

| Score | Criteria |
|-------|----------|
| 1 | Covers all edge cases, comprehensive scope |
| 0 | Standard coverage |

---

## Score Interpretation

### Score to Action Mapping

| Score Range | Action Required |
|-------------|-----------------|
| 90-100 | Ready for use as reference. Document as gold standard. |
| 80-89 | Production-ready. Minor refinements optional. |
| 75-79 | Production-ready. Review before major changes. |
| 65-74 | Usable with caution. Improve weak areas before production. |
| 50-64 | Significant revision needed. Focus on lowest-scoring categories. |
| <50 | Major rewrite required. Use templates as starting point. |

### Category Priority for Improvement

When improving a command, prioritize in this order:

1. **Agent Configuration** (if < 12/20) - Core functionality
2. **Workflow Structure** (if < 12/20) - Organization
3. **Validation & Gates** (if < 9/15) - Quality assurance
4. **Error Handling** (if < 9/15) - Reliability
5. **Documentation** (if < 9/15) - Maintainability
6. **Configuration** (if < 6/10) - Flexibility

---

## Quick Evaluation Checklist

Use this for rapid assessment:

### Must Have (60 points minimum)

```
Workflow Structure:
[ ] Has 3+ phases with descriptive names (4 pts)
[ ] Steps numbered and sequenced (3 pts)
[ ] Context passing defined (3 pts)

Agent Configuration:
[ ] Appropriate agents selected (4 pts)
[ ] Prompts include requirements list (4 pts)
[ ] Expected outputs defined (4 pts)

Validation:
[ ] At least one phase gate (3 pts)
[ ] Success criteria defined (3 pts)

Error Handling:
[ ] Rollback procedure exists (3 pts)
[ ] Failure recovery documented (2 pts)

Documentation:
[ ] Extended thinking present (2 pts)
[ ] Command readable and clear (2 pts)

Subtotal: ___/37 (minimum 25 to be functional)
```

### Should Have (75 points target)

```
[ ] 4-6 well-defined phases (additional 4 pts)
[ ] All steps have context passing (additional 3 pts)
[ ] Composite agent paths used (additional 2 pts)
[ ] Detailed prompts with all elements (additional 4 pts)
[ ] Multiple phase gates (additional 3 pts)
[ ] Measurable success criteria (additional 3 pts)
[ ] Convergence points defined (additional 3 pts)
[ ] Detailed rollback (additional 3 pts)
[ ] Escalation paths (additional 4 pts)
[ ] Coordination notes (additional 4 pts)
[ ] Configuration options (additional 6 pts)

Additional: ___/39
Total: ___/76
```

### Nice to Have (90+ points)

```
[ ] Reference workflows/anti-patterns (additional 4 pts)
[ ] Multiple modes (additional 3 pts)
[ ] Innovation bonus (additional 2 pts)
[ ] Reusability bonus (additional 2 pts)
[ ] Completeness bonus (additional 1 pt)

Bonus: ___/12
Grand Total: ___/88+
```

---

## Common Deductions

### Major Deductions (-5 or more)

| Issue | Deduction | How to Fix |
|-------|-----------|------------|
| No phase structure | -8 | Add 4-6 named phases |
| Vague prompts | -6 | Add numbered requirements, output format |
| No success criteria | -6 | Add measurable criteria |
| No error handling | -6 | Add rollback and recovery |
| No context passing | -6 | Add "Context from previous" |

### Minor Deductions (-2 to -4)

| Issue | Deduction | How to Fix |
|-------|-----------|------------|
| Generic phase names | -2 | Use descriptive names |
| Generic agents | -2 | Use composite paths |
| Missing output specs | -3 | Define expected output |
| No gates | -3 | Add validation gates |
| No configuration | -3 | Add flags/parameters |

### Style Deductions (-1)

| Issue | Deduction | How to Fix |
|-------|-----------|------------|
| Inconsistent formatting | -1 | Standardize structure |
| Missing step numbers | -1 | Number all steps |
| Unclear parallel marking | -1 | Mark parallel tasks |

---

## Improvement Guide

### Quick Wins (Easy +5-10 points)

1. **Add Extended Thinking** (+4 points)
   ```markdown
   [Extended thinking: This workflow coordinates...]
   ```

2. **Add Success Criteria** (+6 points)
   ```markdown
   ## Success Criteria
   - ✅ [Measurable criterion]
   ```

3. **Add Basic Rollback** (+3 points)
   ```markdown
   ## Rollback Procedures
   1. Revert changes...
   ```

4. **Add Configuration Options** (+4 points)
   ```markdown
   ## Configuration
   ### Flags
   - `--quick`: Fast mode
   ```

### Medium Effort (+10-20 points)

1. **Improve All Prompts** (+8 points max)
   - Add action verbs
   - Add numbered requirements
   - Add output format
   - Add constraints

2. **Add Phase Gates** (+6 points)
   - Add gate conditions between phases
   - Define blocking criteria

3. **Add Coordination Notes** (+4 points)
   - Document agent interaction
   - Note timing dependencies

### High Effort (+20+ points)

1. **Restructure Phases** (+8 points)
   - Reorganize into 4-6 phases
   - Use descriptive names
   - Define clear boundaries

2. **Complete Error Handling** (+15 points)
   - Detailed rollback procedures
   - Per-phase failure recovery
   - Escalation paths with triggers

3. **Add Reference Material** (+4 points)
   - Include example workflows
   - Document anti-patterns
   - Add best practices

---

## Scoring Template

Copy and use for evaluation:

```markdown
# Command Quality Evaluation

**Command:** [Name]
**Evaluator:** [Name]
**Date:** [Date]

## Scores

### 1. Workflow Structure (20 pts)
- Phase Organization: ___/8
- Step Sequencing: ___/6
- Context Flow: ___/6
**Subtotal: ___/20**

### 2. Agent Configuration (20 pts)
- Agent Selection: ___/6
- Prompt Quality: ___/8
- Output Specification: ___/6
**Subtotal: ___/20**

### 3. Validation & Gates (15 pts)
- Phase Gates: ___/6
- Success Criteria: ___/6
- Convergence Points: ___/3
**Subtotal: ___/15**

### 4. Error Handling (15 pts)
- Rollback Procedures: ___/6
- Failure Recovery: ___/5
- Escalation Paths: ___/4
**Subtotal: ___/15**

### 5. Documentation (15 pts)
- Extended Thinking: ___/4
- Coordination Notes: ___/4
- Reference Material: ___/4
- Clarity/Readability: ___/3
**Subtotal: ___/15**

### 6. Configuration (10 pts)
- Flag Options: ___/4
- Parameter Configuration: ___/3
- Mode Selection: ___/3
**Subtotal: ___/10**

### 7. Bonus Points (5 pts)
- Innovation: ___/2
- Reusability: ___/2
- Completeness: ___/1
**Subtotal: ___/5**

---

## TOTAL SCORE: ___/100
## TIER: ___________

## Top 3 Strengths
1.
2.
3.

## Top 3 Improvement Areas
1.
2.
3.

## Recommendations
-
```

---

## Related Resources

- **[COMMAND_PATTERN_INDEX.md](COMMAND_PATTERN_INDEX.md)** - Patterns for improvement
- **[COMMAND_QUICK_START.md](COMMAND_QUICK_START.md)** - Creation process
- **[COMMAND_USE_CASE_LOOKUP.md](COMMAND_USE_CASE_LOOKUP.md)** - Pattern selection
- **[full_stack_feature.md](../../domain-agentic-resources/commands/orchestration/full_stack_feature.md)** - Example multi-agent command

---

**Document End**
