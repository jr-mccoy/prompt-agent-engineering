---
title: "Android Observability and Logging Quality Review"
category: mobile-development
description: "Audits Android logging, metrics, and trace quality for faster detection and diagnosis of production incidents"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - android
  - maintenance
  - observability
updated: "2026-05-05"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_incident_triage_and_severity_classification.md
  - domain-software-engineering/mobile/android/maintenance/android_postmortem_and_corrective_action_planning.md
  - domain-software-engineering/mobile/android/analysis/android_performance_audit.md
  - domain-software-engineering/devops/devops_opentelemetry_instrumentation.md
---

# Android Observability and Logging Quality Review

**Objective:** Assess whether current telemetry is sufficient to detect, triage, and diagnose production issues without guesswork.

**When to Use:** During reliability initiatives, after major incidents, and before large releases.

**Prompt Type:** Comprehensive (150-200 lines)

## Context Gathering

1. "What logging patterns and field conventions are used today (provide samples from 2-3 representative flows)?"
2. "Which dashboards and alerts exist, and which fired during the last 3 incidents?"
3. "Which recent incidents required guesswork or post-hoc reproduction to diagnose?"
4. "What SLO targets exist (crash-free sessions, ANR-free sessions, sync success rate, time-to-diagnosis)?"
5. "What privacy/redaction boundaries apply (PII, payment data, health data)?"

## Instructions

### CRITICAL: Verification Requirements

**Before recommending any change, you MUST:**

1. **Tie each gap to an incident or SLO miss** — do not recommend instrumentation in the abstract.
2. **Quantify cost and risk** — every new log/metric must have a cardinality estimate and hot-path overhead assessment.
3. **Validate privacy** — confirm no recommendation introduces PII or violates declared data-safety scope.
4. **Distinguish symptom from root-cause signals** — separate the two in the recommended alert design.
5. **Plan rollout in stages** — quick wins (1-2 weeks) before structural changes (1-2 quarters).

### False-Positive Prevention

- ❌ Do NOT recommend logging that could leak user-identifying data
- ❌ Do NOT add high-cardinality dimensions to metrics without retention/aggregation plan
- ❌ Do NOT propose alerts without a defined runbook destination
- ❌ Do NOT call coverage "sufficient" without evidence from actual incidents
- ✅ DO map every recommendation to a measurable SLO improvement
- ✅ DO mark any logs added on hot paths with overhead measurement requirement

### Phase 1: Logging Quality Audit

| Dimension | Current State | Gap | Risk |
|-----------|---------------|-----|------|
| Structured fields (event name, user-safe IDs, version/build, flow stage) | [Sample] | [Gap] | [Detection / diagnosis impact] |
| Correlation IDs across session / background jobs / network | [Sample] | [Gap] | [Trace continuity loss] |
| Redaction / PII boundaries | [Policy + enforcement] | [Gap] | [Privacy risk class] |
| Log levels and sampling | [Defaults] | [Gap] | [Volume / cost] |

### Phase 2: Coverage Audit

| Failure Mode | Required Checkpoints | Present? | Action |
|--------------|----------------------|----------|--------|
| Crash / ANR | Stack frame + recent activity + memory state | [Y/N] | [Add / harden] |
| WorkManager lifecycle | enqueue / start / retry / success / failure | [Y/N] | [Add / harden] |
| Process death restoration | Saved-state coverage, restore success | [Y/N] | [Add / harden] |
| Data integrity | Write / read / sync conflict + idempotency keys | [Y/N] | [Add / harden] |
| Network boundaries | Request ID, retry, timeout, failure class | [Y/N] | [Add / harden] |

### Phase 3: Signal Usefulness Review

| Alert | Symptom or Root Cause? | Noise Level | Time-to-Diagnosis Support | Recommendation |
|-------|------------------------|-------------|---------------------------|----------------|
| [Alert name] | [Symptom / Root cause] | [High / Med / Low] | [Breadcrumbs available?] | [Keep / tune / merge / delete] |

### Phase 4: Performance and Cost Balance

| Concern | Current Cost | Risk | Mitigation |
|---------|--------------|------|------------|
| Hot-path logging overhead | [ms / call] | [Frame budget impact] | [Sample / async / drop] |
| Metric cardinality | [Series count] | [Cost explosion] | [Bucket / drop dimension] |
| Retention | [Days] | [Investigation window vs. cost] | [Tiered retention] |
| Sampling | [Strategy] | [Lost signal during incidents] | [Adaptive sampling] |

### Phase 5: Roadmap

```text
Quick wins (1-2 weeks, blocking):
1) Close highest-impact coverage gap from Phase 2
2) Add correlation IDs across one critical end-to-end path
3) Tune top noisiest alert

Medium-term (1-2 quarters):
4) Restructure event schema to canonical fields
5) Introduce service-level objectives + error budgets
6) Build incident-replay dashboard from canonical events
```

### Phase 6: Validation Plan

| Change | SLO Affected | Pre-Metric | Post-Metric | Window |
|--------|--------------|------------|-------------|--------|
| [Instrumentation add] | [Time-to-diagnosis / detection latency] | [Baseline] | [Target] | [Days] |

## Expected Output

1. Findings by severity (with incident or SLO evidence)
2. Missing instrumentation map (Phase 2 gaps prioritized)
3. Quick wins (1-2 weeks)
4. Medium-term observability roadmap (1-2 quarters)
5. Validation plan with measurable SLO improvements
6. Cost / privacy guardrails for each recommendation

## Related Prompts

- [android_incident_triage_and_severity_classification.md](android_incident_triage_and_severity_classification.md) - Where coverage gaps surface
- [android_postmortem_and_corrective_action_planning.md](android_postmortem_and_corrective_action_planning.md) - Detection-gap follow-up
- [../analysis/android_performance_audit.md](../analysis/android_performance_audit.md) - Hot-path overhead validation
- [../targeted-reviews/android_workmanager_background_review.md](../targeted-reviews/android_workmanager_background_review.md) - Background instrumentation
- [../targeted-reviews/android_process_death_recovery_review.md](../targeted-reviews/android_process_death_recovery_review.md) - State restoration coverage
- [../targeted-reviews/android_silent_data_loss_detection.md](../targeted-reviews/android_silent_data_loss_detection.md) - Data integrity coverage
- [../../../devops/devops_opentelemetry_instrumentation.md](../../../devops/devops_opentelemetry_instrumentation.md) - Cross-stack tracing
