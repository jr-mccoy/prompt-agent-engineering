---
title: "Android Test Flakiness Triage and Quarantine"
category: mobile-development
description: "Diagnoses flaky Android tests, isolates root causes, and defines quarantine/deflake workflow without blocking delivery"
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-02
  - QA-01
  - RT-05
difficulty: advanced
tags:
  - android
  - mobile-development
  - testing
  - ci
updated: "2026-05-05"
related_prompts:
  - domain-software-engineering/mobile/android/testing/android_test_strategy_design.md
  - domain-software-engineering/mobile/android/testing/android_ci_test_pipeline_optimization.md
  - domain-software-engineering/mobile/android/testing/android_device_api_test_matrix_design.md
  - domain-software-engineering/mobile/android/analysis/android_test_coverage_analysis.md
  - domain-software-engineering/mobile/android/publishing/play_store_pre_launch_checklist.md
---

# Android Test Flakiness Triage and Quarantine

**Objective:** Identify flaky tests, classify root causes, and implement a quarantine and recovery process that protects CI signal quality while driving long-term fixes.

**When to Use:** Use this prompt when CI has intermittent failures, release confidence drops due to unreliable tests, or teams need a formal “quarantine then deflake” policy.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

1. **Failure Pattern:**
   - "Which tests fail intermittently, and at what frequency?"
   - "Do failures cluster by module, device, API level, or time of day?"

2. **Pipeline Context:**
   - "Which jobs are blocking merges/releases?"
   - "Are retries enabled and masking defects?"

3. **Ownership:**
   - "Who owns each flaky suite?"
   - "What SLA exists for deflaking quarantined tests?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before labeling ANY test as flaky, you MUST:**

1. **Prove non-determinism** - Re-run the same test in stable conditions and confirm inconsistent outcomes.
2. **Rule out infra incidents** - Separate test issues from emulator/device farm outages and transient network failures.
3. **Capture evidence** - Store logs, stack traces, screenshots/videos, and timing artifacts.
4. **Classify root cause** - Timing/race, environment, data dependency, assertion fragility, async misuse, or real product bug.
5. **Assign ownership + SLA** - Every quarantined test requires an owner and a target fix date.

### False-Positive Prevention

- ❌ Do NOT quarantine tests without reproducible evidence
- ❌ Do NOT auto-retry indefinitely to “green” builds
- ❌ Do NOT leave quarantined tests without expiry/review date
- ✅ DO keep quarantined tests visible in dashboards
- ✅ DO prioritize fixes for tests covering critical release paths

---

### Phase 1: Flake Detection and Evidence

#### 1.1 Build a Flake Inventory

| Test | Suite | Failure Rate (7d/30d) | Blocking? | Owner |
|------|-------|------------------------|-----------|-------|
| [testName] | [unit/ui/integration] | [x% / y%] | [Yes/No] | [Team] |

#### 1.2 Collect Repro Artifacts

- CI job link + commit SHA
- Device/API + ABI
- Test runner args
- Logcat + stack trace
- Screenshot/video (for UI)
- Network/backend mock state

---

### Phase 2: Triage and Quarantine Decision

#### 2.1 Root Cause Classification

| Category | Signals | Typical Fix |
|----------|---------|-------------|
| Timing/Race | Passes locally, fails under load | Idling sync, deterministic schedulers |
| Env/Infra | Device farm/API instability | Job isolation, emulator pinning |
| Data Dependency | Shared fixtures mutate state | Test data reset/unique fixtures |
| Assertion Fragility | Pixel/time-sensitive assertions | Tolerant/assertion redesign |
| Product Defect | Consistent failure on valid path | Open bug, block release if critical |

#### 2.2 Quarantine Policy

Quarantine only if all conditions hold:
- [ ] Failure is intermittent (not a deterministic product bug)
- [ ] Evidence captured and issue filed
- [ ] Owner assigned
- [ ] Fix ETA + review date recorded
- [ ] Critical-path substitute coverage exists (or added immediately)

---

### Phase 3: Recovery Plan (Deflake Workflow)

```markdown
## Flaky Test Recovery Plan

### Immediate Actions (0-2 days)
- [ ] Move test to quarantine suite/tag
- [ ] Add CI visibility (separate red/yellow status)
- [ ] Add/confirm compensating test coverage

### Short-Term Fixes (3-10 days)
- [ ] Stabilize async handling (coroutines dispatcher/TestScope)
- [ ] Remove shared mutable state between tests
- [ ] Replace brittle selectors/assertions

### Long-Term Guardrails (ongoing)
- [ ] Flake budget SLO (e.g., <2% per suite)
- [ ] Weekly quarantine review and auto-expiry
- [ ] CI alerting for reintroduced flakes
```

---

## Expected Output

1. Flake inventory with severity and ownership
2. Quarantine decisions with explicit evidence
3. Prioritized deflake backlog
4. CI governance rules (SLA, dashboards, expiry)

---

## Related Prompts

- [android_test_strategy_design.md](android_test_strategy_design.md) - Baseline strategy
- [android_ci_test_pipeline_optimization.md](android_ci_test_pipeline_optimization.md) - Throughput + reliability
- [../analysis/android_test_coverage_analysis.md](../analysis/android_test_coverage_analysis.md) - Confirm substitute coverage while quarantining
- [../publishing/play_store_pre_launch_checklist.md](../publishing/play_store_pre_launch_checklist.md) - Release readiness gates
