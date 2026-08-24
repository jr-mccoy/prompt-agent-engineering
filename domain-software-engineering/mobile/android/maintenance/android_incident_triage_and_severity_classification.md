---
title: "Android Incident Triage and Severity Classification"
category: mobile-development
description: "Rapidly triages Android production incidents, assigns severity, and drives first-response actions with evidence-based classification"
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
  - incident-response
updated: "2026-05-05"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_postmortem_and_corrective_action_planning.md
  - domain-software-engineering/mobile/android/maintenance/android_observability_logging_quality_review.md
  - domain-software-engineering/mobile/android/maintenance/android_regression_prevention_checklist_after_hotfixes.md
  - domain-software-engineering/mobile/android/analysis/android_performance_audit.md
---

# Android Incident Triage and Severity Classification

**Objective:** Triage Android incidents quickly, classify severity consistently, and produce an actionable first-response plan with owners and time bounds.

**When to Use:** Use for active production incidents (crashes, ANRs, data corruption, severe latency, battery drain spikes, sync failures), especially during on-call handoffs.

**Prompt Type:** Modular (120-150 lines)

## Context Gathering

1. "What are users actually experiencing, and on which app version(s)/devices/regions?"
2. "What is the detection source — Crashlytics, Play Console vitals, logs, support tickets, in-product telemetry?"
3. "What is the blast radius — affected users, sessions, % DAU, paid vs. free, geography?"
4. "What changed recently — releases, feature flags, server config, dependency updates?"
5. "What SLA, on-call rotation, and timezone constraints govern response?"

## Instructions

### CRITICAL: Verification Requirements

**Before assigning a severity, you MUST:**

1. **Use evidence, not intuition** — every severity dimension must be justified with a metric, log line, or user report.
2. **Separate symptoms from causes** — list user-visible symptoms before any root-cause hypothesis.
3. **Confirm blast radius** — quantify affected users/sessions/versions; do not infer from a single report.
4. **Distinguish ongoing from historical** — note whether impact is increasing, stable, or already mitigated.
5. **Check recoverability** — can users self-recover (retry, restart, reinstall) or is intervention required?

### False-Positive Prevention

- ❌ Do NOT classify SEV-0/SEV-1 from a single anecdotal report
- ❌ Do NOT promote severity to force attention; use escalation triggers instead
- ❌ Do NOT mix root-cause hypotheses into the severity justification
- ❌ Do NOT skip the targeted diagnostic routing step
- ✅ DO restate impact using only provided evidence
- ✅ DO assign one named owner and ETA per response action

### Severity Rubric

- **SEV-0 (Critical):** Widespread outage / data loss / security risk; core journeys blocked for many users.
- **SEV-1 (High):** Major degradation for an important journey; strong business/user impact.
- **SEV-2 (Medium):** Noticeable defect with workaround; limited blast radius.
- **SEV-3 (Low):** Minor issue, cosmetic/non-critical behavior.

Score each dimension explicitly:

| Dimension | Evidence Required | Weight |
|-----------|-------------------|--------|
| User impact | % users / DAU segment / paid-tier exposure | High |
| Functional impact | Specific blocked journey (purchase/login/sync) | High |
| Data risk | Loss / duplication / corruption indicators | High |
| Time sensitivity | Ongoing vs. historical, trend direction | Medium |
| Recoverability | Self-recovery possible? | Medium |

### Phase 1: Impact Restatement and Severity Decision

| Field | Value |
|-------|-------|
| One-line summary | [User-visible behavior] |
| First detected | [Timestamp + source] |
| Affected versions | [Version codes / channels] |
| Blast radius | [% users / sessions / regions] |
| Severity decision | [SEV-0 / SEV-1 / SEV-2 / SEV-3] |
| Severity justification | [Per-dimension evidence] |

### Phase 2: Incident Class Routing

Identify the most likely incident class and list the exact next diagnostic checks for each:

| Incident Class | Diagnostic Track | First 3 Checks |
|----------------|------------------|----------------|
| Crash / ANR | Stack-trace + ANR trace review | [Top frame, thread state, recent code change] |
| WorkManager / background execution | Lifecycle event audit | [Enqueue/start/retry/success/failure ratios] |
| Process death / state restoration | State checkpoint audit | [SavedStateHandle coverage, restore paths] |
| Data integrity / silent data loss | Write/read/sync conflict path | [Idempotency keys, conflict resolution logs] |
| Performance regression | Hot-path profiling | [Frame time, jank %, startup phases] |

### Phase 3: 0-2 Hour Response Plan

| Time Window | Action | Owner | Exit Criterion |
|-------------|--------|-------|----------------|
| 0-15 min | [Stabilize / mitigate] | [Name + role] | [Observable signal] |
| 15-60 min | [Diagnose primary class] | [Name + role] | [Hypothesis confirmed/rejected] |
| 60-120 min | [Communicate + decide rollback/forward-fix] | [Name + role] | [Decision recorded] |

### Phase 4: Escalation Triggers

Define explicit conditions that would raise severity:

- [ ] Blast radius doubles within next [N] minutes
- [ ] Data-loss evidence appears (any confirmed report)
- [ ] Mitigation fails after [N] attempts
- [ ] Critical journey remains blocked past [SLA window]

## Expected Output

1. Severity Decision (with per-dimension evidence)
2. Evidence Table
3. Immediate Mitigations (separated from root-cause hypotheses)
4. Targeted Diagnostics (one concrete path each for WorkManager reliability, process death recovery, data integrity/loss prevention)
5. 0-2 Hour Action Plan with owner + ETA per action
6. Escalation Triggers
7. Handoff-Ready Incident Brief

## Related Prompts

- [android_postmortem_and_corrective_action_planning.md](android_postmortem_and_corrective_action_planning.md) - Once stabilized
- [android_observability_logging_quality_review.md](android_observability_logging_quality_review.md) - Detection gap analysis
- [android_regression_prevention_checklist_after_hotfixes.md](android_regression_prevention_checklist_after_hotfixes.md) - Post-hotfix review
- [../analysis/android_performance_audit.md](../analysis/android_performance_audit.md) - Performance regression diagnostic
- [../targeted-reviews/android_workmanager_background_review.md](../targeted-reviews/android_workmanager_background_review.md) - Background execution
- [../targeted-reviews/android_process_death_recovery_review.md](../targeted-reviews/android_process_death_recovery_review.md) - State restoration
- [../targeted-reviews/android_silent_data_loss_detection.md](../targeted-reviews/android_silent_data_loss_detection.md) - Data integrity
