---
name: solo_dev_retro
description: Solo developer retrospective that reviews the past sprint/week. Analyzes git history, VIBE-TODOs, decision log, and codebase health to produce a "state of the project" report with prioritized action items for the next sprint.
version: "1.0.0"
category: orchestration
tags: [solo-developer, retrospective, workflow, sprint, productivity]
agents_used: [solo-dev-architect, solo-dev-reviewer, mobile-developer]
---

Solo developer retrospective command that replaces team retrospectives with data-driven project analysis:

[Extended thinking: Solo devs skip retros because "retro with yourself" feels pointless. But they still need the same reflection: what shipped, what went wrong, what's accumulating as debt, and what to focus on next. This command makes it concrete by analyzing git history, counting VIBE-TODOs, reviewing decisions, and measuring codebase health. The output is a state-of-the-project report that a solo dev can review in 5 minutes and use to plan the next week. Phase 1 analyzes activity (what actually shipped). Phase 2 assesses debt (what's accumulating). Phase 3 reviews decisions. Phase 4 measures health. Phase 5 plans next actions.]

## Configuration

### Parameters
- `$ARGUMENTS` — Path to the project root
- `--days=7` — Review period in days (default: 7)
- `--format=brief|detailed` — Output format (default: brief)

## Phase 1: Activity Review

### 1. What Shipped
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Analyze git activity for the past $DAYS days in the project at $ARGUMENTS.

Run:
```bash
# Commits in review period
git log --oneline --after='$DAYS days ago' --format='%h %s'

# Files changed
git log --after='$DAYS days ago' --format='' --name-only | sort | uniq -c | sort -rn | head -20

# Lines added/removed
git log --after='$DAYS days ago' --shortstat | grep 'file' | awk '{ins+=$4; del+=$6} END {print ins\" insertions, \"del\" deletions\"}'

# Commits per day pattern
git log --after='$DAYS days ago' --format='%ad' --date=format:'%A' | sort | uniq -c | sort -rn
```

Report:
### Activity Summary
- **Commits:** [count] in [days] days ([avg per day])
- **Lines:** +[insertions] / -[deletions]
- **Most active day:** [day of week]
- **Busiest files:** [top 5 most-changed files]

### Features/Changes Completed
[Group commits by feature/theme, list as bullet points]

### Observations
- [Any patterns: burst then quiet? steady? all on one day?]
- [Any files being changed repeatedly? (churn indicator)]"
- Expected output: Activity summary with patterns

## Phase 2: Debt Assessment

### 2. Technical Debt Scan
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Scan for technical debt in the project at $ARGUMENTS.

Run:
```bash
# Count VIBE-TODOs
grep -rn 'VIBE-TODO' $ARGUMENTS --include='*.kt' --include='*.java' --include='*.ts' --include='*.js' --include='*.py' --include='*.swift' 2>/dev/null | wc -l

# List VIBE-TODOs
grep -rn 'VIBE-TODO' $ARGUMENTS --include='*.kt' --include='*.java' --include='*.ts' --include='*.js' --include='*.py' --include='*.swift' 2>/dev/null

# Count TODOs and FIXMEs
grep -rn 'TODO\|FIXME' $ARGUMENTS --include='*.kt' --include='*.java' --include='*.ts' --include='*.js' --include='*.py' --include='*.swift' 2>/dev/null | wc -l

# Find largest files (complexity indicator)
find $ARGUMENTS -name '*.kt' -o -name '*.java' -o -name '*.ts' -o -name '*.py' -o -name '*.swift' | xargs wc -l 2>/dev/null | sort -rn | head -10

# Lint warnings (if applicable)
# ./gradlew lintRelease 2>/dev/null | tail -5
```

Report:
### Debt Assessment
| Metric | Count | Trend |
|--------|-------|-------|
| VIBE-TODOs | [count] | [new since last retro if known] |
| TODOs/FIXMEs | [count] | [info] |
| Largest file | [name] ([lines] lines) | [⚠️ if >500 lines] |

### VIBE-TODOs to Address
[List all VIBE-TODOs grouped by file, with line numbers]

### Growing Files (Potential Splits)
[Files >300 lines that have been changed frequently — candidates for splitting]"
- Expected output: Debt assessment with specific items

## Phase 3: Decision Review

### 3. Recent Decisions
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Review the decision log at $ARGUMENTS/decisions/ (if it exists).

```bash
# Check if decisions directory exists
ls $ARGUMENTS/decisions/*.md 2>/dev/null

# If exists, show recent decisions
ls -lt $ARGUMENTS/decisions/*.md 2>/dev/null | head -10

# Show decisions modified in the review period
find $ARGUMENTS/decisions/ -name '*.md' -mtime -$DAYS 2>/dev/null
```

If decisions/ exists:
- List recent decisions with status
- Flag any 'proposed' decisions that need resolution
- Note any decisions older than 6 months that should be reviewed

If decisions/ does not exist:
- Note: 'No decision log found. Consider using solo-dev-decision-log skill to track architectural decisions.'

Report:
### Decision Log Status
- **Total decisions:** [count]
- **Recent (this period):** [count and titles]
- **Needs attention:** [any proposed or stale decisions]"
- Expected output: Decision log status

## Phase 4: Health Metrics

### 4. Codebase Health
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Measure codebase health for the project at $ARGUMENTS.

Run:
```bash
# Total lines of code (source only)
find $ARGUMENTS -name '*.kt' -o -name '*.java' -o -name '*.ts' -o -name '*.py' -o -name '*.swift' | xargs wc -l 2>/dev/null | tail -1

# Test file count
find $ARGUMENTS -name '*Test*.kt' -o -name '*Test*.java' -o -name '*.test.ts' -o -name 'test_*.py' 2>/dev/null | wc -l

# Source file count
find $ARGUMENTS -name '*.kt' -o -name '*.java' -o -name '*.ts' -o -name '*.py' -o -name '*.swift' | wc -l 2>/dev/null

# Build time (if Android)
# ./gradlew assembleDebug --dry-run 2>/dev/null | tail -3

# Dependency count (if Android)
grep -c 'implementation\|api(' $ARGUMENTS/app/build.gradle.kts 2>/dev/null || grep -c 'implementation\|api(' $ARGUMENTS/app/build.gradle 2>/dev/null

# Git branch count
git branch | wc -l
```

Report:
### Codebase Health
| Metric | Value | Status |
|--------|-------|--------|
| Source LOC | [count] | [info] |
| Source files | [count] | [info] |
| Test files | [count] | [⚠️ if 0, ✅ if ratio > 0.3] |
| Dependencies | [count] | [⚠️ if >50] |
| Active branches | [count] | [⚠️ if >5 stale branches] |"
- Expected output: Health metrics table

### CONVERGENCE: Phases 1-4 must all complete before Phase 5

## Phase 5: Next Sprint Planning

### 5. Action Items
- Use Task tool with subagent_type="general-purpose"
- Agent persona: solo-dev-architect
- Prompt: "Based on all retrospective findings, create a prioritized action plan.

Synthesize into:

```
## Solo Dev Retro — [Date] — [Project Name]

### What Shipped
[summary from Phase 1]

### Debt Status
[summary from Phase 2]

### Decisions
[summary from Phase 3]

### Health
[summary from Phase 4]

---

### Top 3 Priorities for Next Sprint
1. [Most important feature or fix]
2. [Second priority]
3. [Third priority]

### 1 Tech Debt Item to Address
- [Specific VIBE-TODO or growing file to tackle]

### 1 Process Improvement to Try
- [Based on patterns observed — e.g., 'commit more frequently', 'write ADRs for library choices', 'add tests for the payment flow']

### Parking Lot (Not Now, But Don't Forget)
- [Items that matter but aren't urgent enough for next sprint]
```

Prioritization rules:
- User-facing bugs > features > tech debt > tooling
- Things that get worse over time (growing files, accumulating TODOs) rank higher
- Quick wins (<30 min) should be done immediately, not scheduled"
- Expected output: Formatted retro report with action items
- Context: Include all findings from Phases 1-4

## Success Criteria

- ✅ Git activity analyzed for the review period
- ✅ Technical debt counted and categorized
- ✅ Decision log reviewed (if exists)
- ✅ Codebase health metrics captured
- ✅ Top 3 priorities identified for next sprint
- ✅ At least one tech debt item selected for remediation

## Coordination Notes

- Run weekly or at the end of each sprint
- Pair with `solo_dev_sprint_plan` to turn action items into a concrete sprint plan
- Use `solo-dev-decision-log` skill to create ADRs for decisions flagged during retro
- Follow up on VIBE-TODOs identified with `solo-dev-self-review` for quality pass
