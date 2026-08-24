---
title: "Android CI Test Pipeline Optimization"
category: mobile-development
description: "Optimizes Android CI test execution for faster feedback, higher signal quality, and release-safe quality gates"
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - android
  - mobile-development
  - testing
  - ci
updated: "2026-05-05"
related_prompts:
  - domain-software-engineering/mobile/android/testing/android_test_strategy_design.md
  - domain-software-engineering/mobile/android/testing/android_test_flakiness_triage_quarantine.md
  - domain-software-engineering/mobile/android/testing/android_device_api_test_matrix_design.md
  - domain-software-engineering/mobile/android/publishing/android_release_governance_runbook.md
---

# Android CI Test Pipeline Optimization

**Objective:** Redesign Android test pipelines to reduce cycle time and noise while preserving quality and release confidence.

**When to Use:** Use when CI is slow, flaky, expensive, or too noisy to trust for merge/release decisions.

**Prompt Type:** Modular (120-150 lines)

## Context Gathering

1. "What is current median and p95 CI duration per PR?"
2. "Which test jobs fail most often and why?"
3. "What merge/release SLAs must the pipeline satisfy?"

## Instructions

### CRITICAL: Verification Requirements

1. Measure baseline metrics (duration, queue time, pass rate, retry rate).
2. Separate bottlenecks by stage: build, unit, integration, UI, artifact upload.
3. Validate caching effectiveness (Gradle, dependencies, emulator snapshots).
4. Ensure gating logic maps to risk (critical paths block; low-risk checks can be async).
5. Re-measure after each change and keep rollback plan.

### Optimization Playbook

| Lever | Action | Risk | Validation |
|------|--------|------|------------|
| Parallelization | Split suites by module/shard | Uneven shard time | Compare wall-clock + p95 |
| Test Impact Analysis | Run changed-tests-first | Missed regressions | Periodic full-suite canary |
| Caching | Remote build cache + dependency cache | Stale artifacts | Cache hit/miss audit |
| Environment | Standardized emulator images | Drift | Reproducibility checks |
| Retry Policy | Limited retry + flaky tagging | Hidden defects | Retry reason dashboards |

### Recommended Pipeline Shape

```text
PR Fast Lane (blocking):
1) Static checks + unit tests
2) Targeted integration tests
3) Smoke UI tests

Async Confidence Lane (non-blocking but required before release):
4) Full integration suite
5) Full UI/device matrix
6) Screenshot/visual regression
```

### Quality Gate Policy

- Block merge on critical-path test failures
- Allow non-critical suite quarantine only with owner + SLA
- Require clean Async Confidence Lane before production release

## Expected Output

1. Baseline CI metrics table
2. Bottleneck map + root causes
3. Optimized pipeline design with gating policy
4. Rollout plan (pilot, compare, expand)

## Related Prompts

- [android_test_flakiness_triage_quarantine.md](android_test_flakiness_triage_quarantine.md)
- [android_device_api_test_matrix_design.md](android_device_api_test_matrix_design.md)
- [../analysis/android_test_coverage_analysis.md](../analysis/android_test_coverage_analysis.md)
- [../publishing/play_store_pre_launch_checklist.md](../publishing/play_store_pre_launch_checklist.md)
