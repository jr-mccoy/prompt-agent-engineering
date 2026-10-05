# Android Targeted Reviews

This folder contains 45 specialized code review prompts for Android applications. Unlike codebase-wide reviews, these prompts focus on specific high-risk areas and architectural patterns common in modern Android development.

## When to Use Targeted Reviews

Use these prompts when you need deep analysis of a specific subsystem rather than a broad codebase overview. They are particularly useful for:

- **Pre-release audits** of critical features
- **Debugging** specific categories of issues (memory leaks, sync bugs, etc.)
- **Architecture reviews** of new implementations
- **Security audits** of sensitive functionality
- **Performance optimization** of bottleneck areas

## Prompt Categories

### Architecture & State Management

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [android_sync_architecture_review.md](android_sync_architecture_review.md) | Offline-first sync patterns | Conflict detection, queue processing, retry strategies |
| [android_viewmodel_state_management_review.md](android_viewmodel_state_management_review.md) | ViewModel state patterns | StateFlow usage, side effects, SavedStateHandle |
| [android_repository_pattern_review.md](android_repository_pattern_review.md) | Repository layer design | Data source abstraction, Flow patterns, caching |
| [android_hilt_di_scope_review.md](android_hilt_di_scope_review.md) | Dependency injection scopes | Scope leaks, module organization, testing |

### Database & Persistence

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [android_room_database_query_review.md](android_room_database_query_review.md) | Room DAO efficiency | N+1 queries, indexing, transaction handling |
| [android_room_migration_safety_audit.md](android_room_migration_safety_audit.md) | Database migration safety | Migration chain, data preservation, testing |
| [android_sqlcipher_key_management_review.md](android_sqlcipher_key_management_review.md) | Encrypted database keys | Key generation, Keystore storage, rotation |

### Security

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [android_e2e_encryption_review.md](android_e2e_encryption_review.md) | End-to-end encryption | Signal Protocol, key lifecycle, safety numbers |
| [android_firebase_security_rules_audit.md](android_firebase_security_rules_audit.md) | Firebase security rules | Auth enforcement, data isolation, validation |
| [android_2fa_security_bypass_review.md](android_2fa_security_bypass_review.md) | Two-factor authentication | TOTP implementation, bypass prevention, recovery |

### Background Processing

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [android_workmanager_background_review.md](android_workmanager_background_review.md) | WorkManager patterns | Constraints, chaining, idempotency |
| [android_coroutine_scope_review.md](android_coroutine_scope_review.md) | Coroutine lifecycle | Scope management, memory leaks, cancellation |

### UI & Compose

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [android_compose_recomposition_review.md](android_compose_recomposition_review.md) | Jetpack Compose performance | Recomposition efficiency, stability, remember |
| [android_process_death_recovery_review.md](android_process_death_recovery_review.md) | Process death handling | SavedStateHandle, navigation, form state |

### Platform Features

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [android_geofence_location_review.md](android_geofence_location_review.md) | Location and geofencing | Permissions, battery, Play Store compliance |
| [android_notification_channel_review.md](android_notification_channel_review.md) | Notification channels | Channel configuration, MessagingStyle, FCM |

### Data Sync

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [android_offline_conflict_resolution_review.md](android_offline_conflict_resolution_review.md) | Conflict resolution strategies | Detection, merge logic, edit-delete conflicts |
| [android_crud_sync_verification.md](android_crud_sync_verification.md) | CRUD sync verification | Every CRUD operation for every synced entity, local ↔ cloud propagation |
| [android_data_integrity_audit.md](android_data_integrity_audit.md) | Data integrity audit | Data operations traced from UI action through ViewModel, Repository, local DB, and sync |
| [android_silent_data_loss_detection.md](android_silent_data_loss_detection.md) | Silent data loss detection | Swallowed exceptions, overwrites without merge, orphaned or unreachable data |

### Perceived Performance

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [android_animation_transition_coupling_review.md](android_animation_transition_coupling_review.md) | Animation and transition coupling | Animations that make immediate state changes feel delayed or mushy |
| [android_architectural_coarse_graining_review.md](android_architectural_coarse_graining_review.md) | Architectural coarse-graining | Small user actions triggering disproportionately large state rebuilds |
| [android_async_boundaries_review.md](android_async_boundaries_review.md) | Async boundaries | Unnecessary dispatcher switches, persistence waits, missing optimistic updates |
| [android_compose_recomposition_problems_review.md](android_compose_recomposition_problems_review.md) | Compose recomposition problems | Recomposition problems that make the UI feel less immediate |
| [android_database_observation_review.md](android_database_observation_review.md) | Database observation | Coarse or slow observation adding lag between user actions and UI updates |
| [android_image_media_churn_review.md](android_image_media_churn_review.md) | Image and media churn | Repeated requests, unnecessary transformations, visual churn |
| [android_list_rendering_inefficiency_review.md](android_list_rendering_inefficiency_review.md) | List rendering inefficiency | RecyclerView and LazyColumn updates that are rough or delayed |
| [android_overbroad_ui_updates_review.md](android_overbroad_ui_updates_review.md) | Over-broad UI updates | UI that recomputes or redraws far more than necessary |
| [android_per_update_expensive_work_review.md](android_per_update_expensive_work_review.md) | Per-update expensive work | Expensive transformations on every state change |
| [android_state_propagation_review.md](android_state_propagation_review.md) | State propagation | Wrong or delayed state propagation lagging behind user actions |

### Firebase & Firestore

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [firebase_analytics_strategy.md](firebase_analytics_strategy.md) | Firebase Analytics implementation | Core events, naming conventions, funnels, BigQuery export |
| [firebase_app_check_setup.md](firebase_app_check_setup.md) | Firebase App Check with Play Integrity | Attestation setup, debug tokens, enforcement rollout |
| [firebase_auth_implementation.md](firebase_auth_implementation.md) | Firebase Authentication design | Provider selection, account linking, custom claims RBAC, sessions |
| [firebase_cloud_functions_cost_guard.md](firebase_cloud_functions_cost_guard.md) | Cloud Functions cost audit | Infinite loops, excessive invocations, cold start costs |
| [firebase_cloud_functions_design.md](firebase_cloud_functions_design.md) | Cloud Functions architecture | Trigger types, idempotency, retries, emulator development |
| [firebase_cost_monitor_setup.md](firebase_cost_monitor_setup.md) | Firebase cost monitoring | GCP budget alerts, anomaly detection, cost circuit breakers |
| [firebase_cost_optimization.md](firebase_cost_optimization.md) | Firebase cost optimization | Expensive read patterns, listeners vs one-time reads, caching |
| [firebase_crashlytics_workflow.md](firebase_crashlytics_workflow.md) | Crashlytics crash response workflow | Severity classification, crash-free targets, alert thresholds |
| [firebase_emulator_suite_setup.md](firebase_emulator_suite_setup.md) | Firebase Emulator Suite setup | firebase.json config, seed data, CI integration, rules testing |
| [firebase_health_check.md](firebase_health_check.md) | Periodic Firebase project health check | Security rules, cost trends, SDK currency, quota utilization |
| [firebase_incident_response.md](firebase_incident_response.md) | Firebase incident runbooks | Cost spikes, security breaches, outages, data corruption |
| [firebase_remote_config_strategy.md](firebase_remote_config_strategy.md) | Remote Config strategy | Feature flags, A/B tests, gradual rollouts, kill switches |
| [firebase_security_rules_generator.md](firebase_security_rules_generator.md) | Firestore security rules generator | Custom-claims RBAC, field-level validation, rate limiting |
| [firestore_data_model_design.md](firestore_data_model_design.md) | Firestore data model design | Denormalization, subcollections, index planning, cost per query |
| [firestore_query_optimization.md](firestore_query_optimization.md) | Firestore query optimization | N+1 patterns, unnecessary listeners, missing indexes, pagination |

## Usage Pattern

Each prompt follows a consistent structure:

1. **Objective** - Clear statement of what the review covers
2. **When to Use** - Specific scenarios where this review adds value
3. **Instructions** - Detailed checklist organized by sub-topic
4. **Expected Output** - Template for the review report
5. **Example Output** - Complete example with code snippets
6. **Techniques Used** - Prompt engineering techniques applied
7. **Related Prompts** - Other prompts that complement this one
8. **Customization Guide** - How to adapt for different app types

## Example Workflow

For a family organizer app with offline sync and E2E encryption:

1. **Initial Architecture Review:**
   - `android_sync_architecture_review.md` - Review sync strategy
   - `android_repository_pattern_review.md` - Check data layer

2. **Security Audit:**
   - `android_e2e_encryption_review.md` - Review encryption implementation
   - `android_sqlcipher_key_management_review.md` - Check key storage
   - `android_2fa_security_bypass_review.md` - Audit 2FA if applicable

3. **Performance Check:**
   - `android_room_database_query_review.md` - Database efficiency
   - `android_compose_recomposition_review.md` - UI performance
   - `android_coroutine_scope_review.md` - Memory leaks

4. **Pre-Release:**
   - `android_process_death_recovery_review.md` - State restoration
   - `android_notification_channel_review.md` - Notification configuration

## Techniques Applied

All prompts in this collection use consistent prompt engineering techniques:

| Technique | Code | Description |
|-----------|------|-------------|
| Clear Objective Statement | ST-01 | Specific, focused review scope |
| Structured Sequential Instructions | ST-02 | Logical analysis flow |
| Multi-Dimensional Analysis | RT-02 | Multiple angles on each topic |
| Evidence-Based Reasoning | RT-05 | Code examples throughout |
| Output Format Templates | ST-03 | Consistent report structure |
| Prioritization Guidance | DS-06 | Severity-based ordering |
| Edge Case Coverage | QA-02 | Unusual scenarios covered |

## Customization

Each prompt includes a Customization Guide section with app-type specific modifications:

- **Social/Chat Apps** - Focus on real-time sync, message delivery
- **Financial Apps** - Emphasize security, audit trails, transaction safety
- **Healthcare Apps** - HIPAA compliance, encryption requirements
- **E-commerce Apps** - Cart persistence, payment security
- **Media Apps** - Playback state, download management
- **Enterprise Apps** - SSO integration, device policies

## Related Resources

- [mobile_app_security_review.md](../../cross-platform/mobile_app_security_review.md) - Broad mobile security review
- [android_kotlin_best_practices.md](../analysis/android_kotlin_best_practices.md) - General Kotlin patterns
- mobile_react_native_optimization.md - If using React Native

## Contributing

When adding new targeted review prompts:

1. Follow the established structure (Objective, When to Use, Instructions, etc.)
2. Include detailed code examples in the Example Output section
3. Reference 5-7 prompt engineering techniques from the master index
4. Add the prompt to this README in the appropriate category
5. Cross-reference related prompts
