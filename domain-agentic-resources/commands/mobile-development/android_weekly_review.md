---
name: android_weekly_review
description: Weekly review command that pulls metrics from Play Console, Firebase, and codebase to produce a weekly summary with key metrics, trend analysis, and next-week recommendations
version: "1.0.0"
category: mobile-development
tags: [android, weekly, review, metrics, analytics, solo-developer, firebase, play-store]
agents_used: [android-release-manager, firebase-cost-analyst, mobile-developer]
---

Weekly review command for solo Android developers. Synthesizes metrics from development activity, app performance, user engagement, and costs into a structured weekly report with trend analysis and next-week recommendations:

[Extended thinking: Solo developers lack the team structure that forces regular retrospection. Without weekly reviews, problems accumulate silently — crash rates creep up, costs grow, technical debt compounds, and strategic opportunities are missed. This workflow creates a systematic weekly review that takes 30-45 minutes and produces a report covering all the metrics a solo developer should track. Phase 1 gathers development metrics (commits, PRs, tests). Phase 2 gathers production metrics (crashes, ratings, costs). Phase 3 synthesizes into a weekly report with trend analysis and recommendations. The output serves as both a historical record and a planning input for next week.]

## Configuration

### Parameters
- `$ARGUMENTS` — Path to the Android project root
- `--week=YYYY-WNN` — Specific week to review (default: current week)
- `--compare` — Compare with previous week (enabled by default)

## Phase 1: Development Metrics

### 1. Code Activity Summary
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Generate a development activity summary for the Android project at $ARGUMENTS for the past 7 days. Report: (a) Total commits with breakdown by area (feature, bugfix, refactor, test, config), (b) Lines added/removed, (c) Files changed count, (d) Any new TODO/FIXME comments added vs resolved, (e) Test count change (new tests added vs tests removed), (f) If available, test coverage change. Present as a concise dashboard."
- Expected output: Development metrics dashboard

### 2. Technical Debt Assessment
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Assess the current technical health of the Android project at $ARGUMENTS. Quick scan: (a) Compiler warning count (`./gradlew assembleDebug 2>&1 | grep -c warning` or similar), (b) Lint issue count (`./gradlew lintDebug` summary), (c) Deprecated API usage count, (d) TODO/FIXME count, (e) Dependency currency (how many dependencies in libs.versions.toml have newer versions available). Compare with previous week if data is available."
- Expected output: Technical health metrics

### 3. Build Health
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Check build health metrics for the Android project at $ARGUMENTS: (a) Debug build time (run `./gradlew assembleDebug --dry-run` for task count, estimate from previous builds), (b) Release build success/failure, (c) APK/AAB size trend (if previous build artifacts are available for comparison), (d) Test pass rate (run tests and report results). Flag any regressions from previous week."
- Expected output: Build health report

## Phase 2: Production Metrics

### 4. App Performance Review
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Review the production performance of the Android app at $ARGUMENTS. Check available data sources: (a) If Crashlytics data is accessible, report crash-free rate and top crash clusters, (b) If Play Console data is available, report ANR rate and startup time, (c) Check the codebase for any performance-related changes this week, (d) Review any performance monitoring configurations. If direct metrics aren't accessible, analyze the codebase for potential performance issues introduced this week (new heavy operations, missing coroutine dispatchers, large list operations)."
- Expected output: Performance metrics or risk assessment

### 5. User Feedback Analysis
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Analyze user feedback signals for the Android app at $ARGUMENTS. Review: (a) Any user feedback tracking in the codebase (support templates, FAQ content), (b) Known issues documented in README, issues, or TODO comments, (c) Recent changes that address user-reported issues, (d) Any user-facing text or UI changes this week that might affect satisfaction. Categorize feedback themes: bugs, feature requests, UX issues, performance complaints."
- Expected output: User feedback analysis

### 6. Cost and Infrastructure Review
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Review infrastructure costs and configuration for the Android app at $ARGUMENTS. Check: (a) Firebase configuration for cost efficiency (any new Firestore listeners, new Cloud Functions, new storage usage), (b) CI/CD usage (GitHub Actions minutes consumed if available), (c) Any new third-party services added this week, (d) Budget alert configurations. Estimate cost impact of any infrastructure changes made this week."
- Expected output: Cost and infrastructure assessment

### CONVERGENCE: Steps 4-6 must all complete before Phase 3

## Phase 3: Weekly Synthesis

### 7. Weekly Report Generation
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Synthesize all weekly review data for the Android app at $ARGUMENTS into a structured weekly report.

Format:

## Weekly Review — Week of [Date]

### Key Metrics Dashboard
| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| Commits | [N] | [N] | ↑/↓/→ |
| Tests | [N total, N% pass] | [N] | ↑/↓/→ |
| Lint Issues | [N] | [N] | ↑/↓/→ |
| Build Time | [Ns] | [Ns] | ↑/↓/→ |
| App Size | [N MB] | [N MB] | ↑/↓/→ |
| TODO Count | [N] | [N] | ↑/↓/→ |

### Wins This Week
- [What went well — features shipped, bugs fixed, improvements made]

### Concerns
- [What needs attention — regressions, growing debt, user complaints]

### Recommendations for Next Week
1. **Priority 1:** [Most impactful action for next week]
2. **Priority 2:** [Second most impactful action]
3. **Priority 3:** [Third priority]

### Health Score: [1-10]
- Development velocity: [1-10]
- Code quality: [1-10]
- Production stability: [1-10]
- User satisfaction: [1-10]

### Notes
- [Any observations, decisions made, lessons learned]

Be concise — the report should be readable in 5 minutes. Focus on trends and actionable insights, not raw data."
- Expected output: Formatted weekly review report
- Context: Include all findings from Steps 1-6

## Success Criteria

### Technical Criteria
- ✅ Development metrics accurately reflect the week's activity
- ✅ Build health is verified with actual build output
- ✅ Technical debt metrics are captured

### Process Criteria
- ✅ Report is concise and actionable (5-minute read)
- ✅ Trends are identified (not just point-in-time data)
- ✅ Next-week recommendations are specific and prioritized

### Operational Criteria
- ✅ Production health indicators are checked
- ✅ Cost trends are tracked
- ✅ User feedback themes are captured

## Coordination Notes

- Run this command at the end of each work week (Friday afternoon or Sunday evening)
- Save the report to a `weekly-reviews/` directory for historical comparison
- Use the recommendations to plan Monday's standup priorities
- Pair with `android-daily-standup` for daily tracking
- Every 4th weekly review should include a broader quarterly assessment (use `android-quarterly-maintenance` skill)
- Compare week-over-week trends to catch slow-moving problems

Target: $ARGUMENTS
