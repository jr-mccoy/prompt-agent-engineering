---
title: "Android Contract Testing for Network/Data Boundaries"
category: mobile-development
description: "Defines and validates contracts at API, serialization, repository, and persistence boundaries to prevent integration regressions"
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
  - RT-05
difficulty: advanced
tags:
  - android
  - mobile-development
  - testing
  - contract-testing
updated: "2026-05-05"
related_prompts:
  - domain-software-engineering/mobile/android/testing/android_test_strategy_design.md
  - domain-software-engineering/mobile/android/testing/android_integration_testing.md
  - domain-software-engineering/mobile/android/testing/android_ci_test_pipeline_optimization.md
  - domain-software-engineering/api/api_rest_design_review.md
---

# Android Contract Testing for Network/Data Boundaries

**Objective:** Establish contract tests that verify compatibility and behavior at critical boundaries: API ↔ DTO, DTO ↔ domain, domain ↔ persistence.

**When to Use:** Use when backend schemas evolve frequently, app has sync/offline complexity, or regressions often originate at integration boundaries.

**Prompt Type:** Modular (120-150 lines)

## Instructions

### CRITICAL: Verification Requirements

1. Enumerate boundary contracts from real code paths (not idealized docs).
2. Version and snapshot representative payloads (success + error cases).
3. Validate backward/forward compatibility assumptions explicitly.
4. Test mapping invariants (nullability, defaults, enum evolution, precision).
5. Ensure contract failures are release blockers for affected features.

### Contract Surface Checklist

- API response schema and error envelope
- Auth/token refresh behaviors
- Pagination and sorting semantics
- Local cache persistence model and migration assumptions
- Conflict resolution rules for offline sync

### Output Template

| Boundary | Contract Rule | Test Type | Fixture Source | Priority |
|----------|---------------|-----------|----------------|----------|
| API → DTO | [field/shape constraints] | MockWebServer schema test | [json fixture] | P1 |
| DTO → Domain | [mapping invariant] | JVM unit test | [fixture] | P1 |
| Domain → DB | [persistence invariant] | Room integration test | [fixture] | P1 |

## Expected Output

1. Contract catalog by boundary
2. Prioritized contract test suite plan
3. Fixture/versioning strategy
4. CI gating policy for contract breaks

## Related Prompts

- [android_api_integration.md](../implementation/android_api_integration.md)
- [android_data_layer_implementation.md](../implementation/android_data_layer_implementation.md)
- [../analysis/android_test_coverage_analysis.md](../analysis/android_test_coverage_analysis.md)
