# iOS Targeted Reviews

This folder contains 32 specialized code review prompts for iOS applications. Unlike codebase-wide reviews, these prompts focus on specific high-risk areas and architectural patterns common in modern iOS development using Swift, SwiftUI, and Apple platform frameworks.

## When to Use Targeted Reviews

Use these prompts when you need deep analysis of a specific subsystem rather than a broad codebase overview. They are particularly useful for:

- **Pre-release audits** of critical features
- **Debugging** specific categories of issues (view update hitches, concurrency bugs, etc.)
- **Architecture reviews** of new implementations
- **Security audits** of sensitive functionality
- **Performance optimization** of bottleneck areas
- **Platform feature adoption** when integrating new Apple APIs

## Prompt Categories

### Architecture & State Management

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [ios_observable_state_management_review.md](ios_observable_state_management_review.md) | @Observable/@ObservableObject patterns | Observation tracking, state propagation, view granularity |
| [ios_repository_pattern_review.md](ios_repository_pattern_review.md) | Repository layer design | Data source abstraction, async sequences, caching |
| [ios_dependency_injection_scope_review.md](ios_dependency_injection_scope_review.md) | DI scope lifecycle | Environment injection, scope leaks, testing |
| [ios_coordinator_navigation_review.md](ios_coordinator_navigation_review.md) | Coordinator/Router navigation patterns | NavigationStack, deep linking, state-driven routing |
| [ios_tca_architecture_review.md](ios_tca_architecture_review.md) | The Composable Architecture review | Reducer composition, dependency management, effect handling |

### SwiftUI Performance

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [ios_swiftui_view_update_review.md](ios_swiftui_view_update_review.md) | View body invalidation | Unnecessary redraws, @State vs @Binding, Equatable conformance |
| [ios_swiftui_list_performance_review.md](ios_swiftui_list_performance_review.md) | LazyVStack/List performance | Cell reuse, prefetching, large dataset handling |
| [ios_core_animation_hitch_review.md](ios_core_animation_hitch_review.md) | Animation hitch review | Commit hitches, render hitches, Instruments diagnostics |
| [ios_swiftui_uikit_interop_review.md](ios_swiftui_uikit_interop_review.md) | UIViewRepresentable bridge | Coordinator lifecycle, update cycle, sizing issues |

### Data Persistence

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [ios_core_data_query_review.md](ios_core_data_query_review.md) | Core Data fetch request efficiency | NSFetchRequest tuning, batch faulting, relationship prefetching |
| [ios_core_data_migration_safety_audit.md](ios_core_data_migration_safety_audit.md) | Migration chain safety audit | Lightweight vs heavyweight migration, mapping models, data integrity |
| [ios_swiftdata_adoption_review.md](ios_swiftdata_adoption_review.md) | SwiftData implementation review | @Model usage, ModelContainer configuration, Core Data coexistence |

### Concurrency & Threading

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [ios_swift_concurrency_safety_review.md](ios_swift_concurrency_safety_review.md) | Swift Concurrency actor isolation | Sendable conformance, actor reentrancy, MainActor usage |
| [ios_combine_pipeline_review.md](ios_combine_pipeline_review.md) | Combine publisher chain review | Subscription lifecycle, backpressure, memory management |
| [ios_background_task_review.md](ios_background_task_review.md) | Background processing review | BGTaskScheduler, URLSession background transfers, expiration handling |

### Security

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [ios_keychain_biometric_review.md](ios_keychain_biometric_review.md) | Keychain/biometric auth review | Access control flags, LAContext policy, Keychain queries |
| [ios_app_transport_security_review.md](ios_app_transport_security_review.md) | ATS configuration review | Exception domains, certificate pinning, TLS requirements |
| [ios_data_protection_review.md](ios_data_protection_review.md) | File Data Protection API review | Protection classes, background access, NSFileProtection |
| [ios_jailbreak_tamper_detection_review.md](ios_jailbreak_tamper_detection_review.md) | Runtime integrity review | Jailbreak detection, debugger checks, binary validation |

### Platform Features

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| [ios_universal_link_deep_link_review.md](ios_universal_link_deep_link_review.md) | Universal Links review | AASA file, entitlements, fallback handling |
| ios_push_notification_review.md | Push notification implementation | APNs configuration, payload handling, silent push |
| ios_widget_timeline_review.md | WidgetKit timeline provider review | Timeline entries, relevance, budget management |
| ios_live_activity_review.md | Live Activities/Dynamic Island review | ActivityKit lifecycle, push token updates, UI constraints |
| ios_app_intent_shortcuts_review.md | App Intents/Shortcuts review | Intent discovery, parameter resolution, Siri integration |

### CloudKit

The cloudkit/ subdirectory contains 8 focused prompts for reviewing CloudKit implementations. CloudKit is complex enough to warrant its own subsection covering data modeling through production operations.

| Prompt | Description | Key Focus Areas |
|--------|-------------|-----------------|
| cloudkit/cloudkit_data_model_design.md | Data model design | Record types, references, asset management |
| cloudkit/cloudkit_sync_architecture.md | Sync architecture | NSPersistentCloudKitContainer, custom sync engines, conflict resolution |
| cloudkit/cloudkit_sharing_setup.md | Sharing setup | CKShare, participant management, zone sharing |
| cloudkit/cloudkit_subscription_notifications.md | Subscription notifications | CKSubscription types, silent push triggers, change tokens |
| cloudkit/cloudkit_security_review.md | Security review | ACLs, record-level permissions, encrypted fields |
| cloudkit/cloudkit_performance_optimization.md | Performance optimization | Batch operations, query indexing, fetch limits |
| cloudkit/cloudkit_error_handling.md | Error handling | CKError codes, retry-after logic, partial failures |
| cloudkit/cloudkit_migration_strategy.md | Migration strategy | Schema versioning, additive changes, backward compatibility |

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

For a messaging app with offline support and CloudKit sync:

1. **Initial Architecture Review:**
   - `ios_observable_state_management_review.md` - Review state patterns
   - `ios_repository_pattern_review.md` - Check data layer
   - `ios_coordinator_navigation_review.md` - Review navigation flow

2. **Security Audit:**
   - `ios_keychain_biometric_review.md` - Review credential storage
   - `ios_app_transport_security_review.md` - Check network security
   - `ios_data_protection_review.md` - Verify file protection classes

3. **Performance Check:**
   - `ios_swiftui_view_update_review.md` - View invalidation efficiency
   - `ios_swiftui_list_performance_review.md` - Message list scrolling
   - `ios_swift_concurrency_safety_review.md` - Concurrency correctness

4. **CloudKit Integration:**
   - `cloudkit/cloudkit_sync_architecture.md` - Sync strategy
   - `cloudkit/cloudkit_error_handling.md` - Failure resilience
   - `cloudkit/cloudkit_sharing_setup.md` - Shared conversations

5. **Pre-Release:**
   - `ios_push_notification_review.md` - Notification configuration
   - `ios_live_activity_review.md` - Live Activity for active calls
   - `ios_background_task_review.md` - Background sync reliability

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

- **Social/Chat Apps** - Focus on real-time updates, message delivery, presence
- **Financial Apps** - Emphasize Keychain security, data protection, audit trails
- **Healthcare Apps** - HIPAA compliance, encryption requirements, HealthKit integration
- **E-commerce Apps** - StoreKit handling, cart persistence, payment security
- **Media Apps** - AVFoundation state, download management, AirPlay
- **Enterprise Apps** - MDM compatibility, managed app configuration, SSO

## Related Resources

- mobile_ios_architecture_review.md - Broad iOS architecture review
- [mobile_app_security_review.md](../../cross-platform/mobile_app_security_review.md) - Broad mobile security review
- mobile_react_native_optimization.md - If using React Native

## Contributing

When adding new targeted review prompts:

1. Follow the established structure (Objective, When to Use, Instructions, etc.)
2. Include detailed code examples in the Example Output section
3. Reference 5-7 prompt engineering techniques from the master index
4. Add the prompt to this README in the appropriate category
5. Cross-reference related prompts
