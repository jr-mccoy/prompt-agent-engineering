---
title: "Android Reliability SLO and Error Budget Review"
category: mobile-development
description: "Defines and reviews mobile reliability SLOs (crash-free, ANR-free, sync success, startup) and an error-budget policy that gates releases — turning Android Vitals signals into an actionable release-control loop."
techniques:
  - ST-01
  - ST-02
  - DS-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - android
  - maintenance
  - reliability
  - slo
  - vitals
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_observability_logging_quality_review.md
  - domain-software-engineering/mobile/android/maintenance/android_anr_vitals_analysis.md
  - domain-software-engineering/mobile/android/maintenance/android_on_call_runbook_generator.md
  - domain-software-engineering/mobile/android/publishing/android_staged_rollout.md
---

# Android Reliability SLO and Error Budget Review

**Objective:** Define (or review) a small set of mobile reliability SLOs — crash-free sessions/users, ANR-free sessions, critical-journey success rates, startup latency — set targets grounded in Play's quality bar and current baselines, and establish an error-budget policy that gates releases and triggers reliability work when the budget burns.

**When to Use:** Use when reliability decisions are ad hoc, when "is this good enough to ship?" has no objective answer, after recurring incidents, or when establishing release gates. This converts Android Vitals + Crashlytics signals into a control loop instead of dashboards nobody acts on.

**Prompt Type:** Modular (130-160 lines)

## Context Gathering

1. "What are the current values for crash-free sessions, crash-free users, and user-perceived ANR rate (from Vitals/Crashlytics)?"
2. "What are the critical user journeys, and do you measure their success rate (login, purchase, sync, core action)?"
3. "What startup metric do you track (TTID/TTFD, cold-start p50/p90)?"
4. "What's the release cadence and rollout mechanism (staged rollout %, halt capability)?"
5. "Who owns reliability decisions, and what currently happens when a metric regresses?"

## Instructions

### CRITICAL: Verification Requirements

**Before setting any SLO, you MUST:**

1. **Ground targets in baseline + Play bar** — an SLO target must be achievable from the current baseline and at least meet Play's Bad Behavior thresholds (crash rate / ANR rate that affect discoverability). Do not set aspirational numbers with no plan.
2. **Pick user-centric SLIs** — measure what users experience (crash-free *users*, journey success), not just aggregate counts that hide concentrated pain.
3. **Define the measurement window and source** — every SLI needs a window (e.g., 28-day rolling), a source (Vitals/Crashlytics/in-app), and a denominator definition.
4. **Make the error-budget policy actionable** — specify exactly what happens at budget-burn thresholds (freeze features, divert to reliability, halt rollout).
5. **Avoid SLO sprawl** — 3–5 SLOs maximum; more becomes noise nobody defends.

### False-Positive Prevention

- ❌ Do NOT set 100% / "zero crashes" targets — they leave no error budget and get ignored
- ❌ Do NOT use only aggregate crash-free sessions; it can mask a severe issue hitting a small but important segment
- ❌ Do NOT define an SLO without naming the consequence of breaching it
- ❌ Do NOT gate releases on a metric the team can't measure per-release
- ✅ DO separate per-release gates (canary/staged) from steady-state SLOs (rolling window)
- ✅ DO tie each SLO to an owner and a runbook/escalation path
- ✅ DO revisit targets after the baseline shifts

### Phase 1: SLI / SLO Definition

| SLI | Source | Window | Baseline | Target (SLO) | Play Bar | Owner |
|-----|--------|--------|----------|--------------|----------|-------|
| Crash-free users | [Crashlytics/Vitals] | [28d] | [%] | [%] | [meets?] | [name] |
| Crash-free sessions | [Vitals] | [28d] | [%] | [%] | [meets?] | [name] |
| ANR-free sessions (user-perceived) | [Vitals] | [28d] | [%] | [%] | [meets?] | [name] |
| Critical journey success (e.g. checkout) | [in-app] | [7d] | [%] | [%] | [n/a] | [name] |
| Cold start p90 | [Vitals/Macrobench] | [release] | [ms] | [ms] | [n/a] | [name] |

### Phase 2: Error-Budget Policy

Budget = (100% − SLO target) over the window. Define burn responses:

| Budget State | Condition | Response |
|--------------|-----------|----------|
| Healthy | < 50% budget consumed | Normal feature work |
| Caution | 50–80% consumed | Reliability work prioritized alongside features |
| Burning | 80–100% consumed | Feature freeze on affected area; reliability-only until recovered |
| Exhausted | budget gone / SLO breached | Halt rollouts; incident-style focus; postmortem |

### Phase 3: Release Gate (per-release, distinct from steady-state)

| Gate | Signal | Threshold | Action if Breached |
|------|--------|-----------|--------------------|
| Canary/internal | crash-free, ANR-free on canary | [≥ target − Δ] | Block promotion |
| Staged rollout (e.g. 10%) | crash-free, ANR-free vs. prior version | [no regression > Δ] | Halt rollout |
| Full rollout | sustained over [N] days | [≥ SLO] | Roll back / forward-fix per runbook |

### Phase 4: Review Cadence

- [ ] Weekly: budget burn check; route emerging clusters to triage
- [ ] Per-release: gate evaluation before each promotion step
- [ ] Quarterly: re-baseline SLO targets; retire/adjust noisy SLIs

## Expected Output

1. 3–5 SLIs/SLOs with source, window, baseline, target, and Play-bar comparison
2. Error-budget policy with explicit burn-state responses
3. Per-release gate table (canary → staged → full) with halt/rollback triggers
4. Owner + escalation per SLO (linked to runbooks)
5. Review cadence and re-baselining plan

## Related Prompts

- [android_observability_logging_quality_review.md](android_observability_logging_quality_review.md) - Ensure SLIs are actually measurable
- [android_anr_vitals_analysis.md](android_anr_vitals_analysis.md) - Diagnose ANR-rate SLO breaches
- [android_on_call_runbook_generator.md](android_on_call_runbook_generator.md) - Runbooks the gates escalate into
- [../publishing/android_staged_rollout.md](../publishing/android_staged_rollout.md) - Rollout mechanism the gates control
- [android_performance_regression_detective.md](android_performance_regression_detective.md) - Investigate startup-SLO regressions
