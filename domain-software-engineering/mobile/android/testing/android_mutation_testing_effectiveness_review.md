---
title: "Android Mutation Testing and Test Effectiveness Review"
category: mobile-development
description: "Evaluates whether Android tests truly detect defects using mutation testing and complementary effectiveness signals"
techniques:
  - ST-01
  - ST-02
  - DS-02
  - QA-01
  - RT-05
difficulty: advanced
tags:
  - android
  - mobile-development
  - testing
  - quality
updated: "2026-05-05"
related_prompts:
  - domain-software-engineering/mobile/android/testing/android_test_strategy_design.md
  - domain-software-engineering/mobile/android/testing/android_unit_test_generation.md
  - domain-software-engineering/mobile/android/testing/android_test_flakiness_triage_quarantine.md
  - domain-software-engineering/mobile/android/analysis/android_test_coverage_analysis.md
---

# Android Mutation Testing and Test Effectiveness Review

**Objective:** Measure test effectiveness beyond coverage percentages by using mutation testing and targeted quality heuristics.

**When to Use:** Use when coverage appears high but escaped defects still occur, or when prioritizing improvements in mature test suites.

**Prompt Type:** Modular (120-150 lines)

## Instructions

### CRITICAL: Verification Requirements

1. Select mutation scope strategically (business-critical modules first).
2. Exclude generated/UI-boilerplate code from mutation scoring.
3. Track mutation score alongside flake rate and escaped defect rate.
4. Review surviving mutants for meaningful gaps vs equivalent mutants.
5. Convert findings into specific new/updated tests.

### Effectiveness Signals

| Signal | What It Shows | Target |
|--------|----------------|--------|
| Mutation Score | Defect detection power | Improve trend quarter-over-quarter |
| Escaped Defects | Real-world misses | Downward trend |
| Flake Rate | Signal trust | < agreed SLO |
| Assertion Strength | Test rigor | Explicit behavior checks |

### Review Template

```markdown
## Test Effectiveness Report

### Mutation Results
- Scope: [modules/classes]
- Score: [x%]
- Surviving mutants: [count]

### High-Value Gaps
1. [Behavior not asserted]
2. [Edge case not covered]

### Improvement Plan
- [ ] Add/strengthen tests in [file/module]
- [ ] Replace weak assertions with behavior-level checks
- [ ] Re-run mutation suite and compare delta
```

## Expected Output

1. Mutation scope + baseline results
2. Surviving mutant analysis with priorities
3. Concrete remediation backlog
4. Re-test cadence integrated into CI/release cycle

## Related Prompts

- [android_unit_test_generation.md](android_unit_test_generation.md)
- [android_test_coverage_analysis.md](../analysis/android_test_coverage_analysis.md)
- [android_test_flakiness_triage_quarantine.md](android_test_flakiness_triage_quarantine.md)
