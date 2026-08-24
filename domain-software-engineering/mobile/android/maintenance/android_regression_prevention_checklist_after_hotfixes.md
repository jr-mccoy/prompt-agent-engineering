---
title: "Android Regression Prevention Checklist After Hotfixes"
category: mobile-development
description: "Structured checklist to prevent secondary regressions after urgent Android hotfixes"
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
  - DS-02
difficulty: intermediate
tags:
  - android
  - maintenance
  - hotfix
updated: "2026-05-05"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_incident_triage_and_severity_classification.md
  - domain-software-engineering/mobile/android/maintenance/android_postmortem_and_corrective_action_planning.md
  - domain-software-engineering/mobile/android/testing/android_test_strategy_design.md
  - domain-software-engineering/mobile/android/publishing/android_release_governance_runbook.md
---

# Android Regression Prevention Checklist After Hotfixes

**Objective:** Ensure emergency fixes do not introduce hidden regressions and that temporary mitigations are retired safely.

**When to Use:** Immediately after shipping a hotfix and during the next stabilization window.

**Prompt Type:** Modular / Checklist (100-130 lines)

## Context Gathering

1. "Which PR/commit(s) constitute the hotfix, and which modules/files did they touch?"
2. "What incident or regression did the hotfix address, and what was its severity?"
3. "Which user journeys, data paths, or background flows are adjacent to the changed surface?"
4. "Were any temporary feature flags, guards, or workarounds introduced?"
5. "What rollout strategy was used (full push, staged rollout, percentage)?"

## Instructions

### CRITICAL: Verification Requirements

**Before marking the hotfix as stable, you MUST:**

1. **Confirm scope discipline** — the hotfix touched only required modules/files; collateral edits are flagged.
2. **Retest critical and adjacent flows** — not just the failing path, but flows sharing state, data, or services.
3. **Validate version coverage** — behavior verified on minSdk + current major Android versions in production.
4. **Document every temporary mitigation** — flags, guards, workarounds get a cleanup ticket and a removal date.
5. **Define rollback criteria** — explicit, testable signals that would trigger reverting the hotfix.

### False-Positive Prevention

- ❌ Do NOT mark the hotfix stable based on the original failing test alone
- ❌ Do NOT leave temporary flags/guards without an owner and removal date
- ❌ Do NOT close the checklist without 7-day monitoring evidence
- ❌ Do NOT skip targeted diagnostic revalidation when the incident class involved background, state restoration, or data integrity
- ✅ DO require evidence (test run, screenshot, log query) for every checklist pass
- ✅ DO file a follow-up issue for any item that passed but with reservations

### Phase 1: Scope Control

| Check | Status | Evidence | Owner |
|-------|--------|----------|-------|
| Hotfix touched only required modules/files | [Pass/Fail] | [Diff summary, file list] | [Name] |
| No collateral refactors or unrelated edits bundled | [Pass/Fail] | [PR review] | [Name] |
| Temporary flags / guards documented with rollback plan | [Pass/Fail/N-A] | [Flag name, owner, removal date] | [Name] |
| Cleanup ticket filed for temporary code | [Pass/Fail/N-A] | [Issue link] | [Name] |

### Phase 2: Verification Depth

| Check | Status | Evidence | Owner |
|-------|--------|----------|-------|
| Critical user journeys retested | [Pass/Fail] | [Test run / screenshot] | [Name] |
| Adjacent flows sanity-tested (shared state / data paths) | [Pass/Fail] | [Test run] | [Name] |
| Version-specific behavior validated (minSdk + current major Android) | [Pass/Fail] | [Device/API matrix evidence] | [Name] |
| Locale / accessibility / large-screen variants checked when relevant | [Pass/Fail/N-A] | [Test run] | [Name] |

### Phase 3: Targeted Diagnostics

Apply when incident class involved background execution, state restoration, or data integrity:

| Check | Status | Evidence | Owner |
|-------|--------|----------|-------|
| WorkManager scheduling/execution behavior revalidated | [Pass/Fail/N-A] | [Lifecycle log audit] | [Name] |
| Process death and state restoration path retested | [Pass/Fail/N-A] | [SavedState audit] | [Name] |
| Data loss/corruption guardrails validated (writes, sync, retries) | [Pass/Fail/N-A] | [Conflict path test] | [Name] |
| Idempotency keys verified on retry-prone operations | [Pass/Fail/N-A] | [Log evidence] | [Name] |

### Phase 4: Observability and Detection

| Check | Status | Evidence | Owner |
|-------|--------|----------|-------|
| New/updated logs are structured and searchable | [Pass/Fail] | [Sample query] | [Name] |
| Dashboards include hotfix impact breakdown by version | [Pass/Fail] | [Dashboard link] | [Name] |
| Alerts tuned to detect recurrence and secondary regressions | [Pass/Fail] | [Alert config] | [Name] |
| 7-day monitoring window defined with explicit signals | [Pass/Fail] | [Monitoring plan] | [Name] |

### Phase 5: Release Safety

| Check | Status | Evidence | Owner |
|-------|--------|----------|-------|
| Staged rollout gates defined (% thresholds, halt criteria) | [Pass/Fail] | [Rollout plan] | [Name] |
| Rollback criteria explicit and testable | [Pass/Fail] | [Criteria doc] | [Name] |
| Forward-fix vs. rollback decision tree documented | [Pass/Fail] | [Decision doc] | [Name] |
| Communication plan (in-app, support, status page) confirmed | [Pass/Fail] | [Comm draft] | [Name] |

### Phase 6: 7-Day Monitoring Plan

| Day | Signal | Threshold | Action if Breached |
|-----|--------|-----------|---------------------|
| 1 | [Crash-free sessions / ANR rate / target metric] | [Threshold] | [Halt / rollback / escalate] |
| 3 | [Same or follow-up signal] | [Threshold] | [Action] |
| 7 | [Stability + cleanup verification] | [Threshold] | [Close or extend] |

## Expected Output

1. Checklist table (item, status, evidence, owner)
2. Residual risk summary
3. Cleanup-ticket inventory for any temporary code/flags
4. 7-day monitoring plan with thresholds and actions
5. Rollback decision tree

## Related Prompts

- [android_incident_triage_and_severity_classification.md](android_incident_triage_and_severity_classification.md) - Original triage that drove the hotfix
- [android_postmortem_and_corrective_action_planning.md](android_postmortem_and_corrective_action_planning.md) - Postmortem that complements this checklist
- [android_observability_logging_quality_review.md](android_observability_logging_quality_review.md) - Detection coverage validation
- [../testing/android_test_strategy_design.md](../testing/android_test_strategy_design.md) - Add regression tests for the patched path
- [../publishing/android_release_governance_runbook.md](../publishing/android_release_governance_runbook.md) - Staged rollout gates
- [../analysis/android_performance_audit.md](../analysis/android_performance_audit.md) - Performance baseline check
- [../targeted-reviews/android_workmanager_background_review.md](../targeted-reviews/android_workmanager_background_review.md) - Background execution
- [../targeted-reviews/android_process_death_recovery_review.md](../targeted-reviews/android_process_death_recovery_review.md) - State restoration
- [../targeted-reviews/android_silent_data_loss_detection.md](../targeted-reviews/android_silent_data_loss_detection.md) - Data integrity
