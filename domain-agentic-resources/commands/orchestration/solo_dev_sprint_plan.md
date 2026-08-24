---
name: solo_dev_sprint_plan
description: Sprint planning optimized for a team of one. Analyzes current project state, backlog, past velocity, and available capacity to produce a realistic 1-2 week plan using half-day estimates instead of story points.
version: "1.0.0"
category: orchestration
tags: [solo-developer, sprint-planning, workflow, productivity, project-management]
agents_used: [solo-dev-architect, mobile-developer]
---

Sprint planning command designed for solo developers who need realistic plans that one person can actually complete:

[Extended thinking: Team sprint planning does not work for solo devs. Story points are meaningless alone. You cannot delegate when stuck. Context switching between features costs more because there is no one to pick up where you left off. This command uses half-day estimates (a solo dev's natural unit of work), accounts for real capacity (not 5 full days — more like 3-4 after meetings, admin, and life), and creates a daily plan. Phase 1 assesses velocity (what actually shipped vs what was planned). Phase 2 triages the backlog. Phase 3 calculates real capacity. Phase 4 builds the sprint. Phase 5 allocates to days.]

## Configuration

### Parameters
- `$ARGUMENTS` — Path to the project root
- `--duration=1w|2w` — Sprint duration (default: 1 week)
- `--available-days=N` — Override available days (default: auto-calculated)
- `--backlog-source=github|file|manual` — Where to find backlog items (default: manual)

## Phase 1: Velocity Assessment

### 1. What Actually Shipped Last Sprint
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Assess development velocity for the project at $ARGUMENTS by analyzing what was actually shipped (not planned) in the last sprint period.

Run:
```bash
# Recent commits (last sprint period)
git log --oneline --after='$DURATION ago' --format='%h %s'

# Group by day
git log --after='$DURATION ago' --format='%ad %s' --date=format:'%Y-%m-%d' | sort

# Count productive days (days with commits)
git log --after='$DURATION ago' --format='%ad' --date=format:'%Y-%m-%d' | sort -u | wc -l

# Total commits
git log --after='$DURATION ago' --oneline | wc -l
```

Report:
### Velocity Assessment
- **Productive days last sprint:** [count] out of [total days]
- **Commits:** [count]
- **Features completed:** [list inferred from commit messages]
- **Bugs fixed:** [list]
- **Maintenance:** [list]

### Realistic Capacity Factor
Based on [productive days]/[total available days] = [X]% utilization
This means: for every 5 available days, plan for [X] days of actual coding.

**Velocity note:** [If utilization < 60%: 'You completed less than planned. Plan less, ship more. If utilization > 90%: 'You were at max capacity. Leave buffer for surprises.']"
- Expected output: Velocity assessment with capacity factor

## Phase 2: Backlog Triage

### 2. Prioritize Work Items
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Triage the backlog for the project at $ARGUMENTS.

Sources to check:
```bash
# VIBE-TODOs (from vibe coding sessions)
grep -rn 'VIBE-TODO' $ARGUMENTS --include='*.kt' --include='*.java' --include='*.ts' --include='*.js' --include='*.py' --include='*.swift' 2>/dev/null

# TODOs and FIXMEs
grep -rn 'TODO\|FIXME' $ARGUMENTS --include='*.kt' --include='*.java' --include='*.ts' --include='*.js' --include='*.py' --include='*.swift' 2>/dev/null

# GitHub issues (if --backlog-source=github)
# gh issue list --state open --limit 20

# Recent retro action items (if solo_dev_retro was run)
# Check for retro output
```

For each item, classify:
| Item | Type | Effort | Priority |
|------|------|--------|----------|
| [description] | feature/bug/debt/maintenance | ½ day / 1 day / 2 days / 3+ days | P0/P1/P2/P3 |

Classification rules:
- **Feature:** New user-facing capability
- **Bug:** Something broken that users experience
- **Debt:** Technical improvement (refactoring, VIBE-TODO cleanup, tests)
- **Maintenance:** Dependency updates, CI fixes, tooling

Priority rules:
- P0: Blocking users or losing data
- P1: Important for next release
- P2: Should do this sprint if time permits
- P3: Backlog — not this sprint

Effort estimation in half-days:
- ½ day: Small, well-defined task (fix a specific bug, add a setting)
- 1 day: Medium task (new screen, API integration)
- 2 days: Large task (new feature with UI + data + logic)
- 3+ days: Too large — break it down into smaller tasks"
- Expected output: Prioritized backlog with effort estimates

## Phase 3: Capacity Planning

### 3. Real Available Time
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Calculate real coding capacity for this sprint.

Sprint duration: $DURATION
Available days override: $AVAILABLE_DAYS (if provided)

Calculation:
1. **Calendar days in sprint:** [count]
2. **Subtract weekends:** [count]
3. **Subtract known non-coding days:** (meetings, admin, planned time off)
4. **Multiply by capacity factor** from Phase 1 velocity assessment
5. **Convert to half-days:** (multiply by 2)
6. **Subtract buffer:** Reserve 10-20% for surprises

Report:
### Capacity for This Sprint
| Item | Half-Days |
|------|-----------|
| Calendar working days | [X] → [X*2] half-days |
| Capacity factor ([Y]%) | -[Z] half-days |
| Buffer (15%) | -[B] half-days |
| **Available capacity** | **[N] half-days** |

### Sprint Composition Target
| Category | % | Half-Days |
|----------|---|-----------|
| Features | 60% | [N] |
| Bug fixes | 20% | [N] |
| Tech debt | 10% | [N] |
| Buffer | 10% | [N] |

**Solo dev reality check:**
- Do NOT plan 100% capacity. You will get sick, have appointments, or hit unexpected blockers.
- A 1-week sprint for a solo dev typically has 6-8 productive half-days, not 10.
- If this is your first sprint using this system, plan for 5 half-days only."
- Expected output: Capacity calculation with realistic numbers

### CONVERGENCE: Phases 1-3 must complete before Phase 4

## Phase 4: Sprint Composition

### 4. Select Sprint Items
- Use Task tool with subagent_type="general-purpose"
- Agent persona: solo-dev-architect
- Prompt: "Build the sprint plan using the backlog from Phase 2 and capacity from Phase 3.

Rules:
1. P0 items go in first (non-negotiable)
2. Fill to 60% with features (highest priority first)
3. Fill to 80% with bug fixes
4. Add one tech debt item (10%)
5. Leave 10% empty as buffer
6. If total effort exceeds capacity: cut the lowest priority item, do not compress estimates
7. Every item must be completable in ≤2 half-days. If larger, break it down.

Sprint plan:
### Sprint [N] — [Start Date] to [End Date]
**Capacity:** [N] half-days
**Planned:** [M] half-days ([%] utilization)

| # | Item | Type | Effort | Priority |
|---|------|------|--------|----------|
| 1 | [description] | [type] | [half-days] | P[N] |
| 2 | ... | ... | ... | ... |

**Stretch goals (if time permits):**
| # | Item | Effort |
|---|------|--------|
| S1 | [description] | [half-days] |

**Explicitly not doing this sprint:**
- [Item] — because [reason]"
- Expected output: Sprint plan with selected items

## Phase 5: Daily Allocation

### 5. Day-by-Day Plan
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Allocate sprint items to specific days.

Allocation principles:
- **Monday:** Hard/creative work (most energy, fewest interruptions)
- **Tuesday-Wednesday:** Core feature development
- **Thursday:** Bug fixes and maintenance (energy dipping)
- **Friday:** Small tasks, tech debt, cleanup (lowest energy, highest chance of early stop)

For 2-week sprints: Week 1 = build, Week 2 = polish and ship

Format:
### Daily Plan

**Day 1 ([date]):**
- AM: [item] (½ day)
- PM: [item] (½ day)

**Day 2 ([date]):**
- AM: [item] (½ day)
- PM: [item] (½ day)

...

### Tips for This Sprint
- [Any specific advice based on the mix of work]
- [Reminder: if stuck on an item for >2 half-days, cut scope or skip it]
- [If sprint has many VIBE-TODOs: 'Consider a vibe-coding cleanup session on [day]']"
- Expected output: Day-by-day allocation

## Success Criteria

- ✅ Past velocity analyzed to inform estimates
- ✅ Backlog triaged with half-day estimates
- ✅ Real capacity calculated with buffer
- ✅ Sprint items selected within capacity
- ✅ Day-by-day allocation provided
- ✅ Stretch goals and explicitly excluded items documented

## Coordination Notes

- Run at the start of each sprint (weekly or biweekly)
- Best used after `solo_dev_retro` which provides velocity data and action items
- Use `vibe_session` command for feature items that benefit from rapid development
- Track completion against plan — adjust future sprints based on actual vs planned
- If consistently completing <70% of plan: reduce planned half-days, you are over-estimating capacity
- If consistently completing >100% of plan: add one more item next sprint
