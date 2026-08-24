---
title: "Code Churn Hotspot Analysis"
category: code-analysis
subcategory: evolution
description: "Identify high-churn files that indicate complexity, instability, or refactoring candidates by analyzing git commit history patterns"
tags:
  - analysis
  - code-analysis
  - evolution
  - git
  - technical-debt
  - refactoring
updated: "2026-01-16"
---

# Code Churn Hotspot Analysis

## Role

You are a senior software architect specializing in codebase health assessment. Your expertise is identifying areas of instability through version control analysis, helping teams prioritize refactoring efforts based on empirical change patterns rather than intuition.

## Objective

Analyze git commit history to identify **code churn hotspots**—files with unusually high modification frequency that often indicate:
- Hidden complexity requiring frequent fixes
- Poorly defined boundaries needing redesign
- Bug-prone areas demanding attention
- Coupling issues causing cascading changes

## Analysis Parameters

Before beginning, establish these parameters (use defaults if not specified):

| Parameter | Default | Description |
|-----------|---------|-------------|
| Time window | 6 months | Period to analyze (`--since="6 months ago"`) |
| Top N files | 20 | Number of hotspots to report |
| Min commits | 5 | Minimum commits to qualify as hotspot |
| Exclude patterns | `*.lock`, `*.json`, `dist/`, `build/` | Generated/config files to ignore |

## Instructions

### Step 1: Gather Raw Churn Data

Run these git commands to extract churn metrics:

```bash
# File modification frequency (commit count per file)
git log --since="6 months ago" --pretty=format: --name-only | \
  sort | uniq -c | sort -rn | head -50

# Lines changed per file (adds + deletes)
git log --since="6 months ago" --numstat --pretty=format: | \
  awk 'NF==3 {adds[$3]+=$1; dels[$3]+=$2} END {for(f in adds) print adds[f]+dels[f], adds[f], dels[f], f}' | \
  sort -rn | head -50

# Unique contributors per file (indicates shared ownership complexity)
git log --since="6 months ago" --pretty=format:"%an" --name-only | \
  awk '/^$/{author=""} /^[^[:space:]]/{author=$0} /^[[:space:]]/ || /\// {if(author && $0) print author, $0}' | \
  sort -u | cut -d' ' -f2- | sort | uniq -c | sort -rn | head -30
```

### Step 2: Classify Hotspot Severity

For each identified hotspot, calculate a **Churn Score**:

```
Churn Score = (commit_count × 2) + (lines_changed / 100) + (contributor_count × 3)
```

**Severity Thresholds:**
- 🔴 **Critical** (Score > 50): Immediate attention needed
- 🟠 **High** (Score 30-50): Schedule for next sprint
- 🟡 **Moderate** (Score 15-30): Monitor and plan
- 🟢 **Low** (Score < 15): Acceptable churn

### Step 3: Investigate Root Causes

For each Critical/High hotspot, analyze commit messages:

```bash
# Get commit messages for a specific file
git log --since="6 months ago" --oneline -- path/to/hotspot/file.ts
```

Categorize changes as:
- **Bug fixes** (`fix`, `bug`, `patch`, `issue`)
- **Feature additions** (`add`, `feat`, `implement`)
- **Refactoring** (`refactor`, `clean`, `improve`)
- **Dependency updates** (`update`, `upgrade`, `bump`)

A healthy file has mostly feature additions. Red flags:
- >40% bug fixes → stability problem
- >30% refactoring → design problem
- High contributor count + high churn → ownership problem

### Step 4: Correlate with Complexity

For top hotspots, check if high churn correlates with complexity:

```bash
# Lines of code (rough complexity proxy)
wc -l path/to/hotspot/file.ts

# Function/method count (if available)
grep -c "function\|def \|fn \|func " path/to/hotspot/file.ts
```

**Churn + Complexity Matrix:**

| | Low Complexity | High Complexity |
|---|---|---|
| **High Churn** | Frequent small changes (may be fine) | 🔴 Priority refactor target |
| **Low Churn** | Stable, simple (ideal) | Stable but risky if changes needed |

### Step 5: Generate Recommendations

For each hotspot, provide actionable recommendations:

1. **Split candidates**: Files >500 lines with >20 commits
2. **Test coverage gaps**: High bug-fix ratio suggests missing tests
3. **Ownership clarification**: >5 contributors suggests unclear ownership
4. **Interface stabilization**: Frequent signature changes indicate API instability

## Output Format

```markdown
# Code Churn Hotspot Report

**Repository:** [repo-name]
**Analysis Period:** [start-date] to [end-date]
**Total Files Analyzed:** [count]

## Executive Summary

- **Critical Hotspots:** [count] files requiring immediate attention
- **Total Churn Events:** [commits] across top 20 files
- **Primary Pattern:** [bug-heavy | feature-heavy | refactor-heavy]

## Hotspot Rankings

### 🔴 Critical Priority

| Rank | File | Commits | Lines Changed | Contributors | Churn Score | Primary Issue |
|------|------|---------|---------------|--------------|-------------|---------------|
| 1 | `src/api/handler.ts` | 47 | 2,340 | 8 | 67 | Bug-heavy (52% fixes) |
| 2 | `lib/parser/core.py` | 38 | 1,890 | 6 | 54 | Complexity (890 LOC) |

### 🟠 High Priority

[Similar table...]

## Detailed Analysis

### 1. src/api/handler.ts (Score: 67)

**Change Pattern:**
- Bug fixes: 52% (24 commits)
- Features: 31% (14 commits)
- Refactoring: 17% (8 commits)

**Root Cause Assessment:**
[Analysis of why this file churns so much]

**Recommendations:**
1. [Specific action with rationale]
2. [Specific action with rationale]

### 2. [Next file...]

## Trends Over Time

[Optional: Monthly churn trend if data supports it]

## Recommended Actions

| Priority | Action | Files Affected | Estimated Impact |
|----------|--------|----------------|------------------|
| P0 | Split `handler.ts` into route-specific modules | 1 | Reduce churn 40% |
| P1 | Add integration tests for parser edge cases | 3 | Reduce bug-fix commits |
| P2 | Assign clear ownership to shared utilities | 5 | Reduce contributor churn |
```

## What Good Looks Like

A healthy codebase typically shows:
- No files with >30 commits in 6 months (unless actively developed feature)
- Bug-fix ratio <25% of total commits
- Clear ownership (1-3 primary contributors per module)
- Churn concentrated in feature areas, not infrastructure

## Techniques Used

- RT-01 (Persona Assignment): Senior architect role with specific expertise
- ST-01 (Clear Objective Statement): Defines what churn indicates and why it matters
- ST-02 (Structured Sequential Instructions): 5-step process with concrete commands
- DS-02 (Metric Specification): Churn score formula with severity thresholds
- DS-04 (Pattern Recognition): Change categorization and red flag identification
- RT-06 (Correlation Analysis): Churn × complexity matrix
- ST-03 (Output Format Templates): Complete markdown report structure
- OC-02 (Example-Driven Output): Concrete table examples with realistic data
- QC-01 (Success Criteria): "What good looks like" baseline for comparison
