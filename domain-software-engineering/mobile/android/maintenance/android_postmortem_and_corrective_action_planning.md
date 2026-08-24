---
title: "Android Postmortem and Corrective Action Planning"
category: mobile-development
description: "Builds blameless Android incident postmortems and converts findings into prioritized corrective actions with measurable owners"
techniques:
  - ST-01
  - ST-02
  - RT-05
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - android
  - maintenance
  - postmortem
updated: "2026-05-05"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_incident_triage_and_severity_classification.md
  - domain-software-engineering/mobile/android/maintenance/android_observability_logging_quality_review.md
  - domain-software-engineering/mobile/android/maintenance/android_regression_prevention_checklist_after_hotfixes.md
  - domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md
---

# Android Postmortem and Corrective Action Planning

**Objective:** Produce a blameless postmortem that explains what happened, why defenses failed, and what corrective actions will prevent recurrence.

**When to Use:** After production incidents are stabilized and a timeline + evidence are available.

**Prompt Type:** Comprehensive (180-220 lines)

## Context Gathering

1. "What is the incident timeline (UTC) — first signal, escalation, mitigation, all-clear?"
2. "What evidence is available — metrics, logs, traces, user reports, support transcripts?"
3. "What was the final severity, blast radius, and business impact?"
4. "What root-cause hypotheses are confirmed vs. still open?"
5. "Which existing defenses (tests, alerts, runbooks, code review, canary) had a chance to catch this — and why didn't they?"

## Instructions

### CRITICAL: Verification Requirements

**Before publishing the postmortem, you MUST:**

1. **Stay blameless** — describe systems, signals, and decisions; do not name individuals as causes.
2. **Distinguish trigger from contributing factors** — a single proximate trigger is rarely the only cause.
3. **Audit every defensive layer** — for each existing test/alert/review, state explicitly why it did not catch the incident.
4. **Tie every corrective action to a measurable exit criterion** — "improve monitoring" is not an action.
5. **Prioritize by severity-reduction potential, not effort** — high-impact actions win even when expensive.

### False-Positive Prevention

- ❌ Do NOT close the postmortem without owner + due date for every action
- ❌ Do NOT propose actions whose success cannot be measured
- ❌ Do NOT collapse multiple distinct causes into a single "root cause"
- ❌ Do NOT carry over actions from prior postmortems without verification status
- ✅ DO separate "what worked" from "what failed" — both inform future defenses
- ✅ DO require a validation plan that proves recurrence risk is reduced

### Phase 1: Incident Narrative

| Field | Value |
|-------|-------|
| One-line summary | [Plain-language description] |
| User impact | [Affected journeys, user count, duration] |
| Business impact | [Revenue / trust / compliance exposure] |
| Severity | [Final SEV-N + justification] |
| Detection source | [How we first knew] |
| Time to mitigate | [First signal → mitigation] |

### Phase 2: Timeline (UTC)

| Time (UTC) | Event | Source / Signal | Decision Made |
|------------|-------|------------------|----------------|
| [HH:MM] | [What happened] | [Alert / log / report] | [Action taken] |

### Phase 3: Causal Analysis (Root-Cause Tree)

| Layer | Finding | Evidence |
|-------|---------|----------|
| Trigger | [Proximate cause] | [Specific change / signal] |
| Contributing factors | [Conditions enabling impact] | [Evidence] |
| Detection gaps | [Why detection was late] | [Missing signal / threshold] |
| Response gaps | [Why mitigation was slow] | [Runbook / ownership / tooling] |

### Phase 4: Defensive Layer Assessment

For each existing defense, state why it did not prevent or catch the incident:

| Defensive Layer | Existed? | Fired? | Why It Did Not Help | Improvement Required |
|-----------------|----------|--------|---------------------|----------------------|
| Unit / integration tests | [Y/N] | [Y/N] | [Coverage gap, environment difference, etc.] | [Specific test addition] |
| UI / E2E tests | [Y/N] | [Y/N] | [Selector fragility, scenario gap] | [Specific test addition] |
| Code review | [Y/N] | [Caught risk?] | [Review focus, reviewer expertise] | [Checklist update] |
| Static analysis / lint | [Y/N] | [Y/N] | [Rule absent / disabled] | [Rule add or enforce] |
| Alerts / dashboards | [Y/N] | [Y/N] | [Threshold, cardinality, aggregation] | [Alert add or tune] |
| Canary / staged rollout | [Y/N] | [Caught?] | [Stage size, gating signals] | [Gate add or tighten] |
| Runbooks | [Y/N] | [Used?] | [Outdated / missing scenario] | [Runbook update] |

### Phase 5: Corrective Action Plan

Use the Action Taxonomy: **Code** (bug fix, idempotency, retry, state restoration), **Observability** (dashboards, alerts, structured logs, traces), **Quality Gates** (tests, release checks, canary policies), **Process** (on-call runbook, escalation, ownership).

| ID | Category | Action | Owner | Severity Reduction | Effort | Due | Success Criterion |
|----|----------|--------|-------|--------------------|--------|-----|-------------------|
| CA-1 | [Code/Obs/QG/Process] | [Concrete change] | [Name + role] | [Pts how-much-it-reduces-recurrence] | [S/M/L] | [Date] | [Measurable signal] |

### Phase 6: 30 / 60 / 90 Day Plan

```text
Day 30 (containment hardening):
- [Action IDs scheduled to land]

Day 60 (engineering fixes):
- [Action IDs scheduled to land]

Day 90 (systemic improvements):
- [Action IDs scheduled to land]
```

### Phase 7: Validation Plan

| Action ID | Validation Method | Pre-Metric | Post-Metric | Verification Window |
|-----------|-------------------|------------|-------------|---------------------|
| CA-1 | [Test / canary / fault injection / SLO] | [Baseline] | [Target] | [Days] |

## Expected Output

1. Executive Summary
2. Timeline (UTC)
3. Root Cause Tree
4. What Worked / What Failed (Defensive Layer Assessment)
5. Corrective Actions Backlog (with owner, severity-reduction, effort, due date, success criterion)
6. 30 / 60 / 90 Day Plan
7. Verification & Exit Criteria

## Related Prompts

- [android_incident_triage_and_severity_classification.md](android_incident_triage_and_severity_classification.md) - Triage step preceding this prompt
- [android_observability_logging_quality_review.md](android_observability_logging_quality_review.md) - Detection-gap follow-up
- [android_regression_prevention_checklist_after_hotfixes.md](android_regression_prevention_checklist_after_hotfixes.md) - Post-hotfix validation
- [engineering_post_mortem_root_cause_ladder.md](../../../../domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md) - Cross-domain root-cause framework
- [../analysis/android_performance_audit.md](../analysis/android_performance_audit.md) - Performance baseline
- [../targeted-reviews/android_workmanager_background_review.md](../targeted-reviews/android_workmanager_background_review.md) - Background-execution failure modes
- [../targeted-reviews/android_process_death_recovery_review.md](../targeted-reviews/android_process_death_recovery_review.md) - State-loss diagnostics
- [../targeted-reviews/android_silent_data_loss_detection.md](../targeted-reviews/android_silent_data_loss_detection.md) - Data integrity verification

