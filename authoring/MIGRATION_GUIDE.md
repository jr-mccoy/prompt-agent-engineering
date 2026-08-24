# Migration Guide: Evolving Resources

This guide explains how to migrate and evolve resources in the Prompting-guides repository, including upgrading prompts to skills, converting skills to agents, and modernizing legacy content.

---

## Overview

Resources in this repository follow a maturity progression:

```
Prompt → Skill → Agent → Command
  ↓        ↓       ↓        ↓
Simple   Reusable Multi-step Orchestrated
one-shot module   autonomous workflow
```

As needs evolve, you may need to migrate resources between types. This guide covers:

1. [Prompt → Skill Migration](#prompt--skill-migration)
2. [Skill → Agent Migration](#skill--agent-migration)
3. [Agent → Command Migration](#agent--command-migration)
4. [Quality Tier Upgrades](#quality-tier-upgrades)
5. [Legacy Content Modernization](#legacy-content-modernization)

---

## When to Migrate

### Prompt → Skill

**Migrate when:**
- The prompt is frequently reused across sessions
- You need to bundle scripts, templates, or reference docs
- Multiple related prompts should be consolidated
- The prompt needs progressive disclosure (summary → detail)
- Version tracking and updates are important

**Keep as prompt when:**
- One-time or ad-hoc use
- Simple, focused instruction
- No external resources needed
- Context is highly variable

### Skill → Agent

**Migrate when:**
- The skill requires multi-step reasoning with decisions
- Autonomous operation is needed
- The skill needs to coordinate multiple other skills
- Error recovery and retry logic is complex
- The task requires maintaining state across operations

**Keep as skill when:**
- Linear, predictable workflow
- Human-in-the-loop at each step
- Single capability focus
- No decision branching required

### Agent → Command

**Migrate when:**
- Multiple agents need to work together
- Complex orchestration is required
- Pipeline patterns are needed (parallel, sequential, conditional)
- Cross-cutting concerns (logging, error handling) apply to all agents

**Keep as agent when:**
- Single autonomous task
- No coordination needed
- Simple input → output pattern

---

## Prompt → Skill Migration

### Step 1: Analyze the Prompt

Examine the existing prompt for:

```markdown
## Migration Analysis Checklist

- [ ] Does it have reusable components?
- [ ] Would scripts automate manual steps?
- [ ] Are there reference materials to bundle?
- [ ] Is there progressive complexity (basic → advanced)?
- [ ] Would metadata improve discoverability?
```

### Step 2: Create Skill Structure

Convert the prompt into a skill directory:

**Before (prompt):**
```markdown
# Security Vulnerability Analysis

Analyze the provided code for security vulnerabilities...

## Instructions
1. Check for injection vulnerabilities
2. Review authentication logic
3. Assess data validation
...
```

**After (skill):**
```
security-vulnerability-analysis/
├── SKILL.md              # Core instructions (from prompt)
├── scripts/
│   └── scan_owasp.py     # Automation script
├── references/
│   ├── owasp_top_10.md   # Reference material
│   └── cwe_mapping.md    # Additional context
└── assets/
    └── report_template.md # Output template
```

### Step 3: Create SKILL.md

Transform the prompt into SKILL.md format:

```yaml
---
name: security-vulnerability-analysis
description: Comprehensive security vulnerability analysis for codebases. Use this skill when reviewing code for security issues, preparing for security audits, or when users mention "security review", "vulnerability scan", "OWASP", or "penetration testing".
---
```

```markdown
# Security Vulnerability Analysis

{Original prompt content, enhanced with:}
- When to Use / When NOT to Use sections
- Prerequisites
- Quick Reference table
- Reference Files section linking to bundled resources
```

### Step 4: Extract and Create Supporting Files

**Create scripts for automation:**
```python
# scripts/scan_owasp.py
"""
Automated OWASP Top 10 scanning helper.
Usage: python scan_owasp.py <target_directory>
"""
# Implementation...
```

**Create references for deep knowledge:**
```markdown
# references/owasp_top_10.md
# OWASP Top 10 Reference

Detailed explanations and examples for each vulnerability...
```

### Step 5: Update Discovery Paths

1. Add skill to appropriate category README
2. Update CLAUDE.md mappings if needed
3. Consider cross-linking from related resources

---

## Skill → Agent Migration

### Step 1: Identify Agent Requirements

```markdown
## Agent Migration Checklist

- [ ] Does the skill require autonomous decision-making?
- [ ] Are there conditional branches based on intermediate results?
- [ ] Does it need to coordinate with other skills/tools?
- [ ] Is error recovery complex?
- [ ] Does it maintain state across operations?
```

### Step 2: Design Agent Architecture

**Skill (linear):**
```
Input → Step 1 → Step 2 → Step 3 → Output
```

**Agent (branching):**
```
Input → Analyze → Decision Point
                   ├─→ Path A → Sub-decision → ...
                   ├─→ Path B → ...
                   └─→ Path C → ...
```

### Step 3: Create Agent Definition

**Before (skill SKILL.md):**
```markdown
# Kubernetes Troubleshooting

## Steps
1. Check pod status
2. Review logs
3. Examine events
4. Check resource limits
...
```

**After (agent):**
```markdown
# Kubernetes Troubleshooting Agent

## Role
Autonomous Kubernetes cluster diagnostician that investigates issues,
forms hypotheses, and recommends remediations.

## Decision Framework

### Phase 1: Symptom Identification
- What symptoms are reported?
- Classify: Pod issues, Network issues, Resource issues, Config issues

### Phase 2: Hypothesis Formation
Based on symptoms, generate ranked hypotheses:
1. If pods not starting → Check image pull, resource limits, node capacity
2. If pods crashing → Check logs, resource limits, health checks
3. If network issues → Check services, ingress, network policies

### Phase 3: Investigation
For each hypothesis (highest confidence first):
- Execute diagnostic commands
- Evaluate results
- Confirm or reject hypothesis
- If rejected, move to next hypothesis

### Phase 4: Remediation
Once root cause identified:
- Propose fix with explanation
- Assess blast radius
- Request confirmation for destructive changes

## Available Skills
- `kubernetes-troubleshooting` (diagnostics)
- `helm-chart-operations` (if Helm-managed)
- `cloud-infrastructure` (if cloud-related)

## Guardrails
- Never delete resources without explicit confirmation
- Always explain reasoning before taking action
- Escalate to human if confidence < 70%
```

### Step 4: Add Orchestration Logic

Include decision trees, state management, and coordination patterns:

```markdown
## State Tracking

Maintain investigation state:
```yaml
investigation:
  symptoms: []
  hypotheses:
    - id: h1
      description: "..."
      confidence: 0.8
      status: investigating
  findings: []
  root_cause: null
  remediation: null
```

## Coordination

If issue spans multiple domains:
1. Identify primary domain owner
2. Coordinate with relevant agents
3. Synthesize findings
4. Present unified diagnosis
```

---

## Agent → Command Migration

### Step 1: Identify Orchestration Needs

```markdown
## Command Migration Checklist

- [ ] Multiple agents need to work together
- [ ] Specific execution order matters
- [ ] Parallel execution would improve efficiency
- [ ] Cross-cutting concerns (logging, retries) apply to all
- [ ] Pipeline pattern fits the workflow
```

### Step 2: Design Command Pipeline

**Multiple Agents (uncoordinated):**
```
User → Agent A (manual)
User → Agent B (manual)
User → Agent C (manual)
```

**Command (orchestrated):**
```
User → Command
           ├─→ Agent A ─┐
           ├─→ Agent B ─┼─→ Synthesize → Output
           └─→ Agent C ─┘
```

### Step 3: Create Command Definition

```markdown
# Full Stack Review Command

## Purpose
Orchestrates comprehensive codebase review across multiple domains.

## Pipeline

### Stage 1: Analysis (Parallel)
- `security-review-agent`: Security vulnerabilities
- `performance-review-agent`: Performance issues
- `architecture-review-agent`: Design patterns

### Stage 2: Synthesis
- `report-synthesis-agent`: Combine findings, prioritize, deduplicate

### Stage 3: Output
- Generate unified report
- Create action items
- Assign severity levels

## Configuration

```yaml
pipeline:
  - stage: analysis
    parallel: true
    agents:
      - security-review
      - performance-review
      - architecture-review
    timeout: 300s

  - stage: synthesis
    agent: report-synthesis
    inputs:
      - $analysis.security-review.findings
      - $analysis.performance-review.findings
      - $analysis.architecture-review.findings

  - stage: output
    format: markdown
    template: full_stack_review_report.md
```

## Error Handling

- If any analysis agent fails: Continue with available results, note gaps
- If synthesis fails: Return raw findings with warning
- Timeout: Return partial results with timeout notice
```

---

## Quality Tier Upgrades

Upgrading resources to higher quality tiers.

### Tier 1 → Tier 2 (Basic → Functional)

**Add:**
- Clear structure with sections
- Basic examples
- Input/output specification

### Tier 2 → Tier 3 (Functional → Reliable)

**Add:**
- Multiple examples (3-5)
- Edge case handling
- Error scenarios
- When to Use / When NOT to Use

### Tier 3 → Tier 4 (Reliable → Production-Grade)

**Add:**
- False-Positive Prevention section
- Confidence levels for outputs
- Quality indicators
- Verification checklist
- Worked examples with expected outputs

**Quality Upgrade Checklist:**
```markdown
- [ ] Intent clearly stated
- [ ] Audience specified
- [ ] Context requirements documented
- [ ] Output format specified
- [ ] 3-5 worked examples
- [ ] False-positive prevention
- [ ] Confidence framework
- [ ] Quality indicators
- [ ] Testing/verification approach
```

---

## Legacy Content Modernization

### Migrating from prompts/ to domain-*

**Step 1: Identify correct domain:**
```
prompts/security/*.md → domain-software-engineering/analysis/security/
prompts/testing/*.md → domain-software-engineering/testing/
prompts/business/*.md → domain-business-strategy/
```

**Step 2: Update frontmatter:**
```yaml
# Before
---
title: "Security Review"
---

# After
---
title: "Security Vulnerability Analysis"
category: security
description: "Comprehensive security analysis for codebases"
tags:
  - security
  - analysis
  - code-review
updated: "2026-01-29"
---
```

**Step 3: Apply quality standards:**
- Add False-Positive Prevention
- Add worked examples
- Update cross-references

**Step 4: Update references:**
- Update CLAUDE.md mappings
- Update any linking documents
- Add redirects if URLs matter

---

## Migration Checklist Template

```markdown
## Resource Migration: [Name]

### Source
- Type: [Prompt/Skill/Agent]
- Location: [path]
- Quality Tier: [1-4]

### Target
- Type: [Skill/Agent/Command]
- Location: [new path]
- Quality Tier: [target tier]

### Migration Steps
- [ ] Analyze current resource
- [ ] Design new structure
- [ ] Create new files
- [ ] Migrate content
- [ ] Add enhancements (scripts, references, etc.)
- [ ] Update quality to target tier
- [ ] Update discovery paths (README, CLAUDE.md)
- [ ] Test new resource
- [ ] Archive or redirect old resource
- [ ] Update documentation

### Validation
- [ ] New resource passes quality rubric
- [ ] All links updated
- [ ] No broken references
- [ ] Works as expected in test scenario
```

---

## Common Migration Patterns

### Pattern: Consolidating Related Prompts

Multiple prompts → Single skill with modes:

```
prompts/react-hooks.md
prompts/react-state.md       →  skills/react-development/SKILL.md
prompts/react-performance.md     (with sections for each topic)
```

### Pattern: Adding Automation

Prompt with manual steps → Skill with scripts:

```
prompts/docker-review.md  →  skills/docker-review/
                              ├── SKILL.md
                              └── scripts/
                                  ├── validate_dockerfile.sh
                                  └── check_best_practices.py
```

### Pattern: Creating Agent from Skill

Skill with decision points → Agent with reasoning:

```
skills/incident-response/SKILL.md  →  agents/incident-response-agent.md
(linear steps)                        (decision tree, autonomous)
```

---

**Last Updated:** 2026-01-29
