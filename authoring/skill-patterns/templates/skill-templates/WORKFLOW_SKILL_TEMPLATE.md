# WORKFLOW Skill Template

> **For multi-step sequential processes.** Use this template when the skill guides through a series of ordered steps to achieve a goal.

---

## When to Use This Template

**Use WORKFLOW when:**
- The skill requires steps executed in a specific order
- There are validation checkpoints between steps
- Each step depends on the previous step's completion
- The process can fail or branch at decision points

**Examples:**
- CI/CD pipeline setup
- Deployment workflows
- Migration processes
- Onboarding procedures
- Release management

---

## Directory Structure

```
{skill-name}/
├── SKILL.md                     # Required: workflow instructions
├── scripts/                     # Automation for complex steps
│   ├── step1_init.sh           # Step 1 automation
│   ├── step2_validate.sh       # Step 2 automation
│   └── rollback.sh             # Recovery automation
├── references/                  # Detailed documentation
│   ├── prerequisites.md        # Requirements documentation
│   ├── troubleshooting.md      # Common issues database
│   └── decision_guide.md       # Branching decision criteria
└── assets/                      # Templates and artifacts
    ├── config.template.yaml    # Configuration templates
    └── checklist.md            # Verification checklists
```

---

## SKILL.md Template

Copy everything below the line and customize:

---

```yaml
---
name: {skill-name}
description: Guides through {process name} with sequential steps and validation checkpoints. Use this skill when {trigger condition 1}, {trigger condition 2}, or when users mention "{trigger phrase 1}", "{trigger phrase 2}", or "{trigger phrase 3}".
---
```

```markdown
# {Skill Name}

{Brief 1-2 sentence overview of what this workflow accomplishes.}

## Purpose

{Explain the problem this workflow solves and why a structured process is valuable. 2-3 sentences maximum.}

## When to Use This Skill

Use this skill when you need to:
- {Specific trigger condition 1}
- {Specific trigger condition 2}
- {Specific trigger condition 3}
- {User mentions these keywords: keyword1, keyword2}

## When NOT to Use This Skill

Do NOT use this skill when:
- {Exclusion condition 1 - redirect to appropriate skill}
- {Exclusion condition 2 - explain why this doesn't apply}
- {The process is already complete - how to verify}

## Prerequisites

Before starting this workflow:
- [ ] {Prerequisite 1 - tool/access requirement}
- [ ] {Prerequisite 2 - environment requirement}
- [ ] {Prerequisite 3 - knowledge/context requirement}

**Verify prerequisites:**
```bash
# Command to verify prerequisites are met
{verification-command}
```

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    {WORKFLOW NAME}                          │
├─────────────────────────────────────────────────────────────┤
│  Step 1: {Phase 1}  ──→  Step 2: {Phase 2}  ──→            │
│                           ↓                                 │
│  Step 4: {Phase 4}  ←──  Step 3: {Phase 3}                 │
│       ↓                                                     │
│    ✓ Done                                                   │
└─────────────────────────────────────────────────────────────┘
```

**Estimated Duration:** {X-Y minutes/hours}

---

## Step 1: {First Phase Name}

**Purpose:** {What this step accomplishes}

**Skip if:** {Condition when this step can be skipped}

### Actions

1. {Action 1 - imperative verb starting}
   ```bash
   {command or code example}
   ```

2. {Action 2}
   ```bash
   {command or code example}
   ```

3. {Action 3}

### Validation Checkpoint

Before proceeding to Step 2, verify:
- [ ] {Verification 1 - expected state}
- [ ] {Verification 2 - expected output}
- [ ] {Verification 3 - no errors present}

**Quick validation:**
```bash
# Command to verify step completed successfully
{validation-command}
```

**Expected output:**
```
{expected output example}
```

### If This Step Fails

| Symptom | Likely Cause | Resolution |
|---------|--------------|------------|
| {Error message 1} | {Root cause} | {Fix steps} |
| {Error message 2} | {Root cause} | {Fix steps} |

---

## Step 2: {Second Phase Name}

**Purpose:** {What this step accomplishes}

**Depends on:** Step 1 completion

**Skip if:** {Condition when this step can be skipped}

### Decision Point

{If there's a branching decision in this step:}

```
Is {condition}?
├─→ YES → Proceed with Option A (below)
└─→ NO  → Skip to Option B (below)
```

### Option A: {Path A Name}

{Instructions for path A}

### Option B: {Path B Name}

{Instructions for path B}

### Actions

1. {Action 1}
   ```bash
   {command or code example}
   ```

2. {Action 2}

### Validation Checkpoint

Before proceeding to Step 3, verify:
- [ ] {Verification 1}
- [ ] {Verification 2}

---

## Step 3: {Third Phase Name}

**Purpose:** {What this step accomplishes}

**Depends on:** Step 2 completion

### Actions

1. {Action 1}
2. {Action 2}
3. {Action 3}

### Validation Checkpoint

- [ ] {Verification 1}
- [ ] {Verification 2}

---

## Step 4: {Final Phase Name}

**Purpose:** {Complete the workflow and verify success}

### Actions

1. {Final action 1}
2. {Final action 2}

### Final Verification

All workflow objectives are complete when:
- [ ] {Success criterion 1}
- [ ] {Success criterion 2}
- [ ] {Success criterion 3}

**Verification command:**
```bash
{final-verification-command}
```

**Success output:**
```
{expected success output}
```

---

## Rollback Procedure

If the workflow must be reversed:

### Partial Rollback (to Step N)

```bash
# Rollback to specific step
{rollback-command}
```

### Full Rollback

```bash
# Complete rollback to initial state
{full-rollback-command}
```

**Post-rollback verification:**
- [ ] {Verify initial state restored}
- [ ] {Verify no artifacts remain}

---

## Common Issues

### Issue: {Problem Description 1}

**Symptoms:** {What the user will observe}

**Quick Diagnosis:**
```bash
{diagnostic-command}
```

**Root Causes:**
1. {Cause A} - {How to identify}
2. {Cause B} - {How to identify}

**Resolution:**
```bash
{fix-command}
```

### Issue: {Problem Description 2}

**Symptoms:** {What the user will observe}

**Resolution:** {Steps to resolve}

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/{script1}` | {What it automates} |
| `scripts/{script2}` | {What it automates} |
| `references/{ref1}.md` | {What it documents} |
| `assets/{template}` | {What it provides} |

## Related Skills

- `{related-skill-1}` - {How it relates/when to use instead}
- `{related-skill-2}` - {How it complements this skill}
- `{related-skill-3}` - {Next step after this workflow}
```

---

## Key Patterns for WORKFLOW Skills

| Pattern | Implementation | Example |
|---------|----------------|---------|
| **SP-02: Numbered Steps** | Use `## Step N: Name` headings | Step 1: Initialize → Step 2: Configure |
| **WP-01: Skip Conditions** | Add "Skip if:" under each step | Skip if: Environment already configured |
| **WP-02: Validation Checkpoints** | Checklist after each step | `- [ ] Verify config applied` |
| **WP-03: Fallback Procedures** | "If This Step Fails" section | Table of symptom → cause → resolution |
| **WP-04: Branching Logic** | Decision Point diagrams | `Is X? YES → Path A, NO → Path B` |
| **QP-06: Safety Constraints** | Rollback Procedure section | Full and partial rollback scripts |

---

## Quality Checklist

Before releasing a WORKFLOW skill:

- [ ] Each step has a clear Purpose statement
- [ ] Skip conditions are documented for optional steps
- [ ] Validation checkpoints exist between steps
- [ ] Common failures have diagnosis and resolution
- [ ] Rollback procedure is documented
- [ ] Dependencies between steps are explicit
- [ ] Time estimates are provided
- [ ] Related skills are linked for adjacent workflows

---

## Example Skills to Study

Production WORKFLOW skills in the repository:
- `helm-chart-scaffolding` - Multi-step Helm chart creation
- `gitops-workflow` - GitOps deployment pipeline
- `database-migration` - Schema migration workflow

---

**Last Updated:** 2026-01-29
