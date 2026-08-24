---
title: "Android Device/API-Level Test Matrix Design"
category: mobile-development
description: "Designs risk-based Android test matrices across API levels, form factors, chipsets, and OEM variants"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - android
  - mobile-development
  - testing
updated: "2026-05-05"
related_prompts:
  - domain-software-engineering/mobile/android/testing/android_test_strategy_design.md
  - domain-software-engineering/mobile/android/testing/android_ci_test_pipeline_optimization.md
  - domain-software-engineering/mobile/android/testing/android_test_flakiness_triage_quarantine.md
  - domain-software-engineering/mobile/android/publishing/play_store_pre_launch_checklist.md
---

# Android Device/API-Level Test Matrix Design

**Objective:** Create a pragmatic, risk-weighted device/API test matrix that balances coverage, cost, and execution time.

**When to Use:** Use when launching to broader markets, supporting diverse devices, or tightening pre-release compatibility validation.

**Prompt Type:** Modular (120-150 lines)

## Instructions

### CRITICAL: Verification Requirements

1. Derive matrix from actual user distribution (country/device/API analytics).
2. Include minimum supported API, current target API, and latest stable API.
3. Cover high-risk dimensions: OEM skins, low-memory devices, network variability.
4. Map each matrix row to specific test suites (smoke/regression/full).
5. Keep matrix tiered (PR vs nightly vs pre-release) to control cost.

### Matrix Template

| Tier | Device/API | Purpose | Suites | Frequency |
|------|------------|---------|--------|-----------|
| P0 | [Top 2 device+API combos] | Merge confidence | Smoke + critical UI | Per PR |
| P1 | [Top market/API mix] | Regression confidence | Integration + UI | Nightly |
| P2 | [Edge/OEM/low-end] | Compatibility risk | Full regression | Pre-release |

### Design Heuristics

- P0 should represent majority of active users
- P1 should include OEM diversity (Samsung/Pixel/etc.)
- P2 should include boundary devices (low RAM, older API, tablets/foldables if supported)
- Include offline/poor-network scenarios for sync-heavy apps

## Expected Output

1. Tiered matrix with explicit inclusion rationale
2. Suite-to-tier mapping
3. Cost/time estimate and optimization options
4. Pre-release exit criteria based on matrix results

## Related Prompts

- [android_ci_test_pipeline_optimization.md](android_ci_test_pipeline_optimization.md)
- [android_integration_testing.md](android_integration_testing.md)
- [../analysis/android_test_coverage_analysis.md](../analysis/android_test_coverage_analysis.md)
- [../publishing/play_store_pre_launch_checklist.md](../publishing/play_store_pre_launch_checklist.md)
