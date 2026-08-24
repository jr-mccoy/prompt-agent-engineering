---
name: android_daily_standup
description: Morning startup command that reviews last session's changes, checks CI status, pulls latest crash reports, reviews support inbox, and suggests daily priorities based on impact and urgency
version: "1.0.0"
category: mobile-development
tags: [android, daily, standup, productivity, solo-developer, firebase, crashlytics]
agents_used: [android-release-manager, mobile-developer, firebase-cost-analyst]
---

Morning standup command for solo Android developers. Reviews the state of your app and development work to produce a daily briefing with prioritized action items:

[Extended thinking: This workflow replaces the team standup that solo developers don't have. It systematically checks the critical health indicators of an Android app — recent code changes, build status, crash rate, user feedback, and costs — then synthesizes findings into a prioritized daily plan. Phase 1 reviews development state (what changed, what's building). Phase 2 checks production health (crashes, reviews, costs). Phase 3 synthesizes into a priority-ordered action list. This is designed to take 5-10 minutes and prevent the common solo developer mistake of jumping into coding without knowing what's most important today.]

## Configuration

### Parameters
- `$ARGUMENTS` — Path to the Android project root
- `--days=N` — How many days back to review (default: 1, for Monday standup use 3)
- `--verbose` — Include detailed crash stack traces and review text

## Phase 1: Development State Review

### 1. Recent Changes Review
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Review the git log for the Android project at $ARGUMENTS for the last $DAYS days. Summarize: (a) Number of commits, (b) Files changed grouped by category (UI, data, config, tests), (c) Any incomplete work (WIP commits, TODO comments added), (d) Current branch and any open PRs. Keep the summary to 5-10 bullet points focused on what matters for today's planning."
- Expected output: Development activity summary

### 2. Build and CI Status
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Check the CI/CD status for the Android project at $ARGUMENTS. Run `./gradlew assembleDebug` and report: (a) Build success/failure, (b) Any new compiler warnings, (c) Any new lint warnings (run `./gradlew lintDebug`), (d) Test results if available (`./gradlew test`). Report only new issues — not pre-existing ones."
- Expected output: Build health summary with new issues only

## Phase 2: Production Health Check

### 3. Crash Report Summary
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Analyze the production health of the Android app. Check: (a) If there's a Crashlytics dashboard URL or local crash data, summarize recent crash trends, (b) Review any crash-related files or logs in the project, (c) Check if there are known crash issues tracked in issues/TODOs, (d) If the app uses Firebase, check for any error handling patterns that might be insufficient. Report the top 3 most impactful issues by user count."
- Expected output: Crash health summary with top issues

### 4. User Feedback Review
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Review user feedback indicators for the Android app at $ARGUMENTS. Check: (a) Any support email templates or FAQ content that might indicate common issues, (b) Any TODO items related to user-reported bugs, (c) Known issues documented in the project, (d) Any Play Store review response templates that suggest recurring themes. Summarize the top 3 user concerns."
- Expected output: User sentiment summary

### 5. Cost and Infrastructure Check
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Review the infrastructure health of the Android app at $ARGUMENTS. Check: (a) Firebase configuration files for any concerning patterns, (b) Cloud Functions code for potential cost issues (inefficient queries, missing limits), (c) Any budget alert configurations, (d) Dependency update status (check if libs.versions.toml has outdated versions). Flag anything requiring immediate attention."
- Expected output: Infrastructure health summary

### CONVERGENCE: Steps 3-5 must all complete before Phase 3

## Phase 3: Daily Priority Synthesis

### 6. Priority Recommendation
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Based on the standup findings for the Android app at $ARGUMENTS, synthesize a daily priority list.

Priority framework:
- P0 (Do First): Production crashes affecting >1% users, security issues, build failures, cost spikes
- P1 (Do Today): Bug fixes for reported issues, CI warnings that block merge, user-facing quality issues
- P2 (Schedule): Feature work, tech debt, non-urgent improvements, dependency updates
- P3 (Backlog): Nice-to-haves, future planning, learning tasks

Format the output as:

## Today's Standup — [Date]

### App Health
- Crash-free rate: [rate or 'check Crashlytics']
- Build status: [pass/fail]
- Open issues: [count]

### Do First (P0)
- [action item with context]

### Do Today (P1)
- [action item with context]

### Scheduled (P2)
- [action item with context]

### Notes
- [any observations or reminders]

Be concise — this should be readable in under 2 minutes."
- Expected output: Formatted daily standup report
- Context: Include all findings from Steps 1-5

## Success Criteria

### Technical Criteria
- ✅ Build status is verified (compiles without error)
- ✅ Crash health is assessed
- ✅ Recent changes are summarized

### Process Criteria
- ✅ Priorities are ordered by impact and urgency
- ✅ Report is concise (readable in 2 minutes)
- ✅ Action items are specific and actionable

### Operational Criteria
- ✅ Infrastructure concerns are flagged
- ✅ User feedback themes are captured
- ✅ No critical issues are missed

## Coordination Notes

This command is designed to be run at the start of each work session. For best results:
- Run Monday standup with `--days=3` to cover the weekend
- Run after deployments to verify production health
- Compare today's output with yesterday's to track trend direction
- Pair with `android-weekly-review` for comprehensive weekly analysis

Target: $ARGUMENTS
