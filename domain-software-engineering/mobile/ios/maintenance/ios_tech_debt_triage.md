---
title: "iOS Tech Debt Triage"
category: mobile-development
description: "Triage and prioritize iOS technical debt with impact scoring across user impact, developer velocity, and risk dimensions, effort estimation, quick wins identification, dependency mapping, and sprint planning integration."
techniques:
  - ST-01
  - RT-02
difficulty: intermediate
tags:
  - ios
  - swift
  - technical-debt
  - prioritization
updated: "2026-03-20"
---

# iOS Tech Debt Triage

**Objective:** Systematically triage and prioritize technical debt in an iOS codebase by scoring items across user impact, developer velocity, and risk dimensions, estimating effort, identifying quick wins, mapping dependencies, and integrating results into sprint planning.

**When to Use:** Use this prompt during quarterly planning, after a major release when the team has bandwidth for cleanup, when onboarding new developers who struggle with the codebase, or when velocity is declining due to accumulated complexity. Also useful before major feature work to clear the path.

**Prompt Type:** Modular (300+ lines)

---

## Context Gathering

Before triaging tech debt, gather essential context:

1. **Codebase State:**
   - "What is the approximate codebase size (files, lines of code)?"
   - "What is your test coverage percentage?"
   - "Are there known areas that developers avoid touching?"

2. **Team Context:**
   - "How many iOS developers are on the team?"
   - "What percentage of sprint capacity can be allocated to tech debt?"
   - "Are there new team members who struggle with specific areas?"

3. **Business Context:**
   - "What major features are planned in the next 2-3 quarters?"
   - "Are there upcoming OS/SDK deadlines (WWDC, iOS deprecations)?"
   - "Is there pressure to improve app performance, crash rates, or App Store rating?"

4. **Existing Tracking:**
   - "Do you have an existing tech debt register or backlog?"
   - "Are there compiler warnings being ignored?"
   - "What does your linting tool report (SwiftLint violations)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before prioritizing ANY tech debt item, you MUST:**

1. **Quantify the impact** - Vague statements like "code is messy" are not actionable. Measure the concrete cost.
2. **Validate developer pain** - Confirm debt items with the team. One person's tech debt is another's working code.
3. **Estimate effort accurately** - Include testing, migration, and rollout time, not just coding time.
4. **Map dependencies** - Understand what depends on the debt area before scheduling changes.
5. **Define done** - Each tech debt item must have clear acceptance criteria for completion.

**Tech debt is not inherently bad. It is a conscious tradeoff. Only prioritize debt that has measurable negative impact.**

### False-Positive Prevention

- ❌ Do NOT classify working code as tech debt just because it uses an older pattern
- ❌ Do NOT prioritize aesthetic refactors over impactful structural changes
- ❌ Do NOT estimate effort without accounting for test updates and migration
- ❌ Do NOT schedule debt work that blocks feature delivery without business alignment
- ❌ Do NOT treat all compiler warnings as equal priority
- ✅ DO focus on debt that is actively slowing the team or causing user-facing issues
- ✅ DO include the cost of NOT fixing debt in the impact assessment
- ✅ DO identify debt that is on the critical path for planned features
- ✅ DO balance debt reduction with feature delivery
- ✅ DO track debt reduction velocity sprint over sprint

---

### Phase 1: Tech Debt Inventory

#### 1.1 Automated Discovery

```bash
# Compiler warnings count
xcodebuild build -workspace MyApp.xcworkspace -scheme MyApp 2>&1 \
    | grep "warning:" | wc -l

# Warnings by category
xcodebuild build -workspace MyApp.xcworkspace -scheme MyApp 2>&1 \
    | grep "warning:" \
    | sed 's/.*warning: //' \
    | sed 's/ \[.*$//' \
    | sort | uniq -c | sort -rn | head -20

# SwiftLint violations
swiftlint lint --reporter csv 2>/dev/null | tail -n +2 | cut -d',' -f5 | sort | uniq -c | sort -rn

# TODO/FIXME/HACK markers
grep -rn "TODO\|FIXME\|HACK\|WORKAROUND\|TEMP\|XXX" --include="*.swift" Sources/ | wc -l
grep -rn "TODO\|FIXME\|HACK\|WORKAROUND\|TEMP\|XXX" --include="*.swift" Sources/

# Files with high complexity (large files often indicate tech debt)
find Sources/ -name "*.swift" -exec wc -l {} \; | sort -rn | head -20

# Files with most git churn (frequently changed = high maintenance cost)
git log --since="6 months ago" --name-only --pretty=format: -- "*.swift" \
    | sort | uniq -c | sort -rn | head -20

# Test coverage gaps
xcrun xccov view --report TestResults.xcresult --json \
    | python3 -c "import json,sys; d=json.load(sys.stdin); \
    [print(f'{t[\"lineCoverage\"]*100:.0f}% {t[\"name\"]}') \
    for t in sorted(d['targets'][0]['files'], key=lambda x: x['lineCoverage'])]" \
    | head -20
```

#### 1.2 Manual Discovery Categories

Gather tech debt from these sources:

| Source | How to Find | Example Items |
|--------|-------------|---------------|
| **Compiler warnings** | Build output | Deprecated API usage, type inference issues |
| **Linter violations** | SwiftLint report | Complexity, naming, force unwraps |
| **Code comments** | grep TODO/FIXME | Acknowledged shortcuts |
| **Architecture** | Code review, team input | Massive ViewControllers, missing abstractions |
| **Dependencies** | Outdated packages | Pinned to old major versions |
| **Testing** | Coverage reports | Untested critical paths |
| **Documentation** | Missing/outdated docs | No onboarding for complex modules |
| **Build system** | Build time profiling | Slow compilation, redundant targets |
| **CI/CD** | Pipeline configuration | Flaky tests, slow pipelines |
| **Developer experience** | Team survey | Pain points, friction areas |

#### 1.3 Tech Debt Register

```markdown
## Tech Debt Register

| ID | Title | Category | Location | Discovered | Reporter |
|----|-------|----------|----------|------------|----------|
| TD-001 | Massive HomeViewController (2,400 lines) | Architecture | Home/HomeVC.swift | 2025-09 | Team |
| TD-002 | No unit tests for payment flow | Testing | Payments/ | 2025-11 | QA |
| TD-003 | Force unwraps in API response parsing | Safety | Networking/Parser.swift | 2026-01 | Lint |
| TD-004 | Deprecated UIWebView usage | Deprecation | WebContent/ | 2025-06 | Compiler |
| TD-005 | Manual Core Data stack (no migration path) | Architecture | CoreData/ | 2025-03 | Senior Dev |
| TD-006 | 847 SwiftLint violations suppressed | Quality | .swiftlint.yml | 2026-01 | Lint |
| TD-007 | No accessibility labels on onboarding | Accessibility | Onboarding/ | 2026-02 | QA |
| TD-008 | Synchronous image loading in cells | Performance | Feed/FeedCell.swift | 2025-08 | Performance review |
```

---

### Phase 2: Impact Scoring

**CHECKPOINT 1:** Confirm tech debt inventory is complete before scoring.

```markdown
## Inventory Summary

| Category | Count |
|----------|-------|
| Architecture | [N] |
| Testing | [N] |
| Safety | [N] |
| Deprecation | [N] |
| Performance | [N] |
| Quality | [N] |
| Accessibility | [N] |
| **Total** | **[N]** |

**Proceed with impact scoring?**
```

#### 2.1 Three-Dimensional Impact Scoring

Score each item on three dimensions (1-5 scale):

**Dimension 1: User Impact**
| Score | Criteria |
|-------|----------|
| 1 | No user-visible effect |
| 2 | Minor: occasional inconvenience |
| 3 | Moderate: affects some users regularly |
| 4 | Major: significant UX degradation |
| 5 | Critical: crashes, data loss, or security risk |

**Dimension 2: Developer Velocity Impact**
| Score | Criteria |
|-------|----------|
| 1 | No effect on development speed |
| 2 | Minor friction when working in the area |
| 3 | Regularly slows feature development |
| 4 | Significantly blocks multiple features |
| 5 | Makes the area nearly untouchable |

**Dimension 3: Risk**
| Score | Criteria |
|-------|----------|
| 1 | No future risk |
| 2 | Low risk, might cause issues in 12+ months |
| 3 | Moderate risk, will cause issues in 6-12 months |
| 4 | High risk, likely to cause issues in 3-6 months |
| 5 | Imminent risk, will break in next OS/SDK update |

**Composite Score:** `(User Impact * 2) + (Velocity Impact * 1.5) + (Risk * 1.5)` (max 25)

#### 2.2 Scored Tech Debt

```markdown
## Scored Tech Debt

| ID | Title | User | Velocity | Risk | Score | Priority |
|----|-------|------|----------|------|-------|----------|
| TD-004 | Deprecated UIWebView | 2 | 1 | 5 | 13.0 | P1 |
| TD-001 | Massive HomeViewController | 1 | 5 | 3 | 14.0 | P1 |
| TD-002 | No payment flow tests | 4 | 3 | 4 | 18.5 | P0 |
| TD-003 | Force unwraps in parsing | 5 | 2 | 3 | 17.5 | P0 |
| TD-005 | Manual Core Data stack | 2 | 4 | 4 | 16.0 | P1 |
| TD-008 | Sync image loading | 4 | 1 | 2 | 12.5 | P2 |
| TD-006 | SwiftLint violations | 1 | 3 | 2 | 9.5 | P2 |
| TD-007 | Missing a11y labels | 3 | 1 | 3 | 12.0 | P2 |
```

---

### Phase 3: Effort Estimation & Quick Wins

#### 3.1 Effort Estimation

For each tech debt item, estimate total effort including all work:

```markdown
## Effort Breakdown: TD-001 Massive HomeViewController

| Activity | Effort | Notes |
|----------|--------|-------|
| Analysis & planning | 2 hours | Identify extraction points |
| Implementation | 12 hours | Extract 5 child VCs, create coordinator |
| Test updates | 4 hours | Update existing tests, add missing |
| Code review | 2 hours | Senior review of architecture change |
| QA validation | 3 hours | Regression test Home flow |
| **Total** | **23 hours** | ~3 developer-days |
```

#### 3.2 Quick Wins Matrix

Plot items by effort vs impact to find quick wins:

```markdown
## Quick Wins (High Impact, Low Effort)

| ID | Title | Score | Effort | ROI |
|----|-------|-------|--------|-----|
| TD-003 | Force unwraps in parsing | 17.5 | 4 hours | Excellent |
| TD-008 | Sync image loading | 12.5 | 3 hours | Excellent |
| TD-007 | Missing a11y labels | 12.0 | 6 hours | Good |

## Big Bets (High Impact, High Effort)
| ID | Title | Score | Effort | ROI |
|----|-------|-------|--------|-----|
| TD-002 | No payment flow tests | 18.5 | 5 days | Good (risk reduction) |
| TD-001 | Massive HomeVC | 14.0 | 3 days | Good (velocity gain) |
| TD-005 | Manual Core Data | 16.0 | 2 weeks | Moderate |

## Defer (Low Impact, High Effort)
| ID | Title | Score | Effort | ROI |
|----|-------|-------|--------|-----|
| TD-006 | SwiftLint violations | 9.5 | 3 days | Low |
```

#### 3.3 Dependency Mapping

```markdown
## Dependency Map

### TD-001: Massive HomeViewController
- **Blocks:** TD-002 (hard to test without extraction)
- **Blocked by:** Nothing
- **Affects:** Home feature, Deep linking, Analytics

### TD-005: Manual Core Data Stack
- **Blocks:** SwiftData migration (roadmap Q3)
- **Blocked by:** TD-002 (need tests before refactoring data layer)
- **Affects:** All features using persistence

### Recommended Order:
1. TD-003 (quick win, no dependencies)
2. TD-008 (quick win, no dependencies)
3. TD-001 (unblocks TD-002)
4. TD-002 (unblocks TD-005, reduces risk)
5. TD-005 (enables SwiftData roadmap)
```

---

### Phase 4: Sprint Planning Integration

**CHECKPOINT 2:** Confirm scoring and effort estimation complete before sprint planning.

```markdown
## Triage Summary

| Priority | Count | Total Effort | Quick Wins |
|----------|-------|-------------|------------|
| P0 | [N] | [X] dev-days | [N] |
| P1 | [N] | [X] dev-days | [N] |
| P2 | [N] | [X] dev-days | [N] |

**Team capacity for tech debt: [X%] of sprint = [N] dev-days**
**Proceed with sprint allocation?**
```

#### 4.1 Sprint Allocation Strategy

```markdown
## Tech Debt Sprint Plan

### Allocation: 20% of sprint capacity = 4 dev-days per sprint

### Sprint 1: Quick Wins + Foundation
| Item | Effort | Developer | Notes |
|------|--------|-----------|-------|
| TD-003 Force unwrap fix | 0.5 days | Any | Pair with related changes |
| TD-008 Async image loading | 0.5 days | Any | Use Kingfisher/AsyncImage |
| TD-001 HomeVC extraction (start) | 3 days | Senior | Phase 1: Extract 2 child VCs |

### Sprint 2: Continue Architecture + Testing
| Item | Effort | Developer | Notes |
|------|--------|-----------|-------|
| TD-001 HomeVC extraction (finish) | 1 day | Senior | Phase 2: Coordinator |
| TD-002 Payment flow tests | 3 days | Mid-level | Focus on critical paths |

### Sprint 3: Risk Reduction
| Item | Effort | Developer | Notes |
|------|--------|-----------|-------|
| TD-004 UIWebView replacement | 2 days | Any | Use WKWebView |
| TD-007 A11y labels | 1 day | Any | Focus on onboarding |
| TD-005 Core Data planning | 1 day | Senior | Design migration path |
```

#### 4.2 Tracking Metrics

```markdown
## Tech Debt Metrics (Track Monthly)

| Metric | Baseline | Current | Target |
|--------|----------|---------|--------|
| Compiler warnings | 156 | [N] | < 50 |
| SwiftLint violations | 847 | [N] | < 200 |
| Force unwraps | 89 | [N] | < 10 |
| Test coverage | 34% | [N%] | > 60% |
| Files > 500 lines | 23 | [N] | < 10 |
| TODO/FIXME count | 67 | [N] | < 30 |
| Average build time | 4m 12s | [time] | < 3m |
| Tech debt items (P0+P1) | 5 | [N] | 0 |
```

---

## Expected Output

### Tech Debt Triage Report

```markdown
# Tech Debt Triage Report - [App Name] - [Date]

## Summary
- Items inventoried: [N]
- Items scored: [N]
- Quick wins identified: [N] ([X] dev-days total)
- Critical items (P0): [N]

## Priority Breakdown
| Priority | Items | Effort | Sprint Allocation |
|----------|-------|--------|-------------------|
| P0 | [N] | [X] days | Sprint [N]-[N] |
| P1 | [N] | [X] days | Sprint [N]-[N] |
| P2 | [N] | [X] days | Backlog |

## Recommended Sprint Plan
[3-sprint plan with specific items and developers]

## Metrics Dashboard
[Baseline and target metrics]

## Risk Assessment
- Cost of inaction: [description of what happens if debt is not addressed]
- Dependencies on roadmap: [features blocked by tech debt]
```

### Implementation Checklist

- [ ] Tech debt inventory created from all sources (automated + manual)
- [ ] Each item scored on user impact, velocity impact, and risk
- [ ] Quick wins identified (high impact, low effort)
- [ ] Dependencies mapped between debt items
- [ ] Effort estimated with full breakdown (code, tests, review, QA)
- [ ] Sprint allocation aligned with team capacity
- [ ] Tracking metrics baseline established
- [ ] Stakeholders aligned on tech debt investment

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective on prioritizing tech debt for action
- **RT-02** (Multi-Dimensional Analysis): Three-dimensional impact scoring across user, velocity, and risk

---

## Related Prompts

- [ios_crash_analysis.md](ios_crash_analysis.md) - Crash-related tech debt identification
- [ios_deprecation_audit.md](ios_deprecation_audit.md) - Deprecated API tech debt
- [ios_xcode_build_optimization.md](ios_xcode_build_optimization.md) - Build system tech debt
- [ios_performance_regression_detective.md](ios_performance_regression_detective.md) - Performance-related tech debt
- [ios_user_feedback_analysis.md](ios_user_feedback_analysis.md) - User-reported quality issues
