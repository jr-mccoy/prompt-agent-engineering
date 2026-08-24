---
title: "Android Release Governance Runbook"
category: mobile-development
description: "Orchestrate Android Play Store publishing governance from privacy/compliance audit through rollout and incident response."
techniques:
  - ST-01
  - ST-02
  - ST-05
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - android
  - play-store
  - release-governance
  - compliance
  - staged-rollout
updated: "2026-05-05"
related_prompts:
  - domain-software-engineering/mobile/android/publishing/android_privacy_compliance.md
  - domain-software-engineering/mobile/android/publishing/play_store_data_safety_generator.md
  - domain-software-engineering/mobile/android/publishing/android_release_preparation.md
  - domain-software-engineering/mobile/android/publishing/play_store_pre_launch_checklist.md
  - domain-software-engineering/mobile/android/publishing/play_store_release_management.md
  - domain-software-engineering/mobile/android/publishing/android_staged_rollout.md
  - domain-software-engineering/mobile/android/maintenance/android_incident_triage_and_severity_classification.md
---

# Android Release Governance Runbook

**Objective:** Provide one end-to-end operating flow for Android publishing governance by sequencing existing prompts from compliance validation to post-launch incident response.

## Unified Publishing Flow

Use the following sequence as a single release workflow:

1. **Privacy and compliance audit**  
   Prompt: [`android_privacy_compliance.md`](android_privacy_compliance.md)
2. **Data safety artifacts**  
   Prompt: [`play_store_data_safety_generator.md`](play_store_data_safety_generator.md)
3. **Listing assets and legal copy**  
   Prompts: [`play_store_screenshot_strategy.md`](play_store_screenshot_strategy.md), [`privacy_policy_generator.md`](privacy_policy_generator.md), [`terms_of_service_generator.md`](terms_of_service_generator.md), [`android_play_store_optimization.md`](android_play_store_optimization.md)
4. **Pre-launch checks**  
   Prompts: [`android_release_preparation.md`](android_release_preparation.md), [`play_store_pre_launch_checklist.md`](play_store_pre_launch_checklist.md), [`play_store_policy_compliance_check.md`](play_store_policy_compliance_check.md)
5. **Staged rollout execution**  
   Prompts: [`play_store_release_management.md`](play_store_release_management.md), [`android_staged_rollout.md`](android_staged_rollout.md)
6. **Review-response and incident loop**  
   Prompts: [`play_store_review_response_strategy.md`](play_store_review_response_strategy.md), [`play_store_policy_monitor.md`](play_store_policy_monitor.md)

## Artifacts Produced Checklist

Use this checklist as release exit criteria.

### Play Console Forms
- [ ] App content questionnaire updated
- [ ] Data safety form completed and aligned with implementation
- [ ] Target audience and ads declarations validated
- [ ] Permissions declarations and sensitive API justifications finalized

### Legal and Policy Artifacts
- [ ] Public privacy policy URL published and reachable
- [ ] Terms of service URL published and versioned
- [ ] In-app disclosures match policy language

### Listing Assets
- [ ] Store listing copy (title, short/long description) approved
- [ ] Screenshots complete for required device categories/locales
- [ ] Feature graphic and optional promo assets reviewed

### Pre-Launch and Quality Gates
- [ ] Signed release AAB built and reproducible
- [ ] Version code/name and track strategy approved
- [ ] Pre-launch report triaged (crash, ANR, accessibility, compatibility)
- [ ] Policy compliance checks passed with no blocker findings

### Rollout Gates
- [ ] Stage 1 gate defined (crash/ANR/rating thresholds)
- [ ] Stage progression gates defined (1% → 5% → 20% → 100% or equivalent)
- [ ] Halt/rollback decision criteria documented
- [ ] Monitoring ownership and on-call response windows assigned

## Suggested Operating Cadence

- **T-14 to T-7 days:** Complete compliance, data safety, and legal artifacts.
- **T-7 to T-2 days:** Finalize listing assets and pass pre-launch checks.
- **T-1 to T+7 days:** Run staged rollout with explicit go/no-go gates.
- **Continuous post-launch:** Execute review-response and incident loop, then feed findings into the next release cycle.

## Cross-References

- Android publishing overview: [`../README.md`](../README.md)
- Release readiness deep-dive: [`android_release_preparation.md`](android_release_preparation.md)
- Rollout strategy deep-dive: [`play_store_release_management.md`](play_store_release_management.md)
