# Technique Picker: Fast Reference

**Purpose:** Quickly select 3–5 canonical techniques based on user intent. All IDs are from the [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md).

> **Canonical Source:** For comprehensive technique combinations with examples and templates, see [USE_CASE_LOOKUP.md](../techniques/USE_CASE_LOOKUP.md). This page provides a simplified quick reference.

---

## By Intent

### ANALYZE
*User wants to understand, review, or evaluate something*

| Technique | ID | One-Line Description |
|-----------|----|---------------------|
| Clear Objective Statement | **ST-01** | Define exactly what to analyze |
| Structured Sequential Instructions | **ST-02** | Numbered steps through analysis |
| Multi-Dimensional Analysis | **RT-02** | Location + Description + Impact + Severity + Recommendations |
| Evidence-Based Reasoning | **RT-05** | Cite file paths, line numbers, quotes |
| Output Format Specification | **ST-03** | Explicit structure for findings |
| Prioritization Guidance | **DS-06** | Rank findings by severity/impact |

**Typical combo:** ST-01 + ST-02 + RT-02 + RT-05 + ST-03 + DS-06

---

### CREATE
*User wants to generate new content, code, or documentation*

| Technique | ID | One-Line Description |
|-----------|----|---------------------|
| Explicit Context Framing | **CM-01** | Provide background, tech stack, conventions |
| Constraint Specification | **CM-02** | Must/Must-Not boundaries |
| Output Format Specification | **ST-03** | Exact structure of deliverable |
| Audience-Specific Framing | **RP-02** | Who will consume this output |
| Reference Class Priming | **ED-05** | Show 1-2 examples of desired output |

**Typical combo:** CM-01 + CM-02 + ST-03 + RP-02

---

### DECIDE
*User needs to make a choice between options*

| Technique | ID | One-Line Description |
|-----------|----|---------------------|
| Tree of Thoughts | **RT-03** | Generate and compare multiple approaches |
| Explicit Context Framing | **CM-01** | Current state, requirements, constraints |
| Output Format Specification | **ST-03** | Structure for options + recommendation |
| Chain-of-Verification | **QA-01** | Self-check the recommendation |

**For high stakes, add:**
| Multi-Persona Debate | **RP-03** | Simulate multiple expert perspectives |
| Adversarial Stress-Test | **QA-02** | "List 3 ways this could be wrong" |

**Typical combo:** RT-03 + CM-01 + ST-03 + QA-01

---

### LEARN
*User wants to understand how something works*

| Technique | ID | One-Line Description |
|-----------|----|---------------------|
| Audience-Specific Framing | **RP-02** | Match explanation to learner level |
| Chain-of-Thought | **RT-01** | Step-by-step reasoning visible |
| Analogical Reasoning | **RT-04** | Explain via familiar comparisons |
| Iterative Scaffolding | **ED-01** | Build understanding progressively |
| Delimited Sections | **ST-04** | Clear sections (Simple Version → Details → Examples) |

**Typical combo:** RP-02 + RT-01 + RT-04 + ST-04

---

### FIX
*User has a problem to solve or bug to fix*

| Technique | ID | One-Line Description |
|-----------|----|---------------------|
| Chain-of-Thought | **RT-01** | Show reasoning step-by-step |
| Evidence-Based Reasoning | **RT-05** | Cite error messages, stack traces, code |
| Hierarchical Task Breakdown | **DT-01** | Break complex problems into sub-problems |
| Root Cause Focus | **DT-01+RT-05** | Trace symptoms back to underlying cause |

**Typical combo:** RT-01 + RT-05 + DT-01

---

### PLAN
*User needs to organize a complex task or project*

| Technique | ID | One-Line Description |
|-----------|----|---------------------|
| Hierarchical Task Breakdown | **DT-01** | Break into phases, tasks, subtasks |
| Structured Sequential Instructions | **ST-02** | Order of execution |
| Explicit Context Framing | **CM-01** | Goals, constraints, dependencies |
| Prioritization Guidance | **DS-06** | Rank by importance/urgency |

**Typical combo:** DT-01 + ST-02 + CM-01 + DS-06

---

### DELEGATE / VERIFY DONE
*User wants to hand off a task with verifiable completion criteria*

| Technique | ID | One-Line Description |
|-----------|----|---------------------|
| Gate-Based Verification | **QA-08** | Binary pass/fail completion tests |
| MVP Gates | **DD-04** | Top 3 high-leverage verification gates |
| Iteration Control | **DD-06** | Max attempts + escalation trigger |
| Self-Audit Table | **DD-07** | Structured table with evidence + location |
| Vague-to-Concrete Translation | **DD-02** | Turn fuzzy requirements into testable criteria |

**Typical combo:** QA-08 + DD-04 + DD-06 + DD-07

**Use prompts from:** `domain-engineering-workflows/done-definition/`

---

## When to Add Heavier QA

Add additional quality techniques for high-stakes work:

| Stakes Level | Add These |
|--------------|-----------|
| **Standard** | Basic self-check (included in template) |
| **Important** | **QA-01** Chain-of-Verification — structured self-critique |
| **Critical** | **QA-02** Adversarial Stress-Test — "What could go wrong?" |
| **Production** | **DD-04** MVP Gates + **DD-06** Iteration Control |

### High-Stakes Signals

Add heavier QA when:
- Security implications (data, access, vulnerabilities)
- Financial impact (costs, revenue, contracts)
- User-facing changes (UX, public API, customer-visible)
- Irreversible actions (deployments, data migrations, deletions)
- Legal/compliance requirements

---

## Quick Decision Matrix

| If user says... | Use intent | Recommended techniques |
|-----------------|------------|----------------------|
| "Review my code" | ANALYZE | ST-01 + ST-02 + RT-02 + RT-05 + DS-06 |
| "Write a function" | CREATE | CM-01 + CM-02 + ST-03 |
| "Which approach is better" | DECIDE | RT-03 + CM-01 + QA-01 |
| "Explain how X works" | LEARN | RP-02 + RT-04 + ST-04 |
| "Debug this error" | FIX | RT-01 + RT-05 + DT-01 |
| "Plan the migration" | PLAN | DT-01 + ST-02 + DS-06 |
| "Make sure it's actually done" | DELEGATE | QA-08 + DD-04 + DD-06 |

---

## Technique ID Quick Reference

| Prefix | Category |
|--------|----------|
| ST | Structural (organization, format) |
| RT | Reasoning (thinking patterns) |
| QA | Quality Assurance (verification) |
| CM | Context Management (inputs, state) |
| RP | Role & Perspective (personas) |
| DT | Decomposition (breakdown) |
| ED | Educational (teaching) |
| DS | Domain-Specific (specialized) |
| DD | Done Definition (completion) |

**Full reference:** [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md)

---

## Related Resources

- **Template:** [NEW_PROMPT_TEMPLATE.md](NEW_PROMPT_TEMPLATE.md)
- **Checklist:** [NEW_RESOURCE_CHECKLIST.md](NEW_RESOURCE_CHECKLIST.md)
- **Full technique catalog:** [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md)
- **Patterns by use case:** [Use Case Lookup](../techniques/USE_CASE_LOOKUP.md)

---

**Last Updated:** 2026-01-31
