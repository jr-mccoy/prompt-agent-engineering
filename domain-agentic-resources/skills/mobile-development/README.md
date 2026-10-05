# Mobile Development Skills

> Skills for Android, React Native, Next.js, and cross-platform mobile development patterns.

## Skills in This Category

| Skill | Description |
|-------|-------------|
| [android-accessibility-testing](android-accessibility-testing/) | Android-specific accessibility testing using ADB, Accessibility Scanner, TalkBack, and programmatic checks. |
| [android-adb-operations](android-adb-operations/) | Comprehensive ADB command reference and workflow guide for device management, app installation, debugging, log capture, file transfer, shell operations, intent testing, and screen capture. |
| [android-adb-profiling](android-adb-profiling/) | ADB-based performance profiling workflows for CPU, memory, battery, network, and GPU rendering. |
| [android-admob-mediation](android-admob-mediation/) | Integrates Google AdMob with mediation adapters, UMP consent management for GDPR/CCPA, ad format selection (banner, interstitial, rewarded, native, app open), Compose ad wrappers, and subscriber ad suppression. |
| [android-app-survey](android-app-survey/) | Systematic survey methodology for mapping Android application structure, screens, features, navigation flows, and tech stack into a categorized feature map. |
| [android-behavior-audit](android-behavior-audit/) | Behavioral scrutiny methodology for evaluating whether Android app code behavior matches developer intent, with structured finding classification (Likely Bug, Suspicious Pattern, Design Question, Confirmed Correct)… |
| [android-behavior-fix-planning](android-behavior-fix-planning/) | Fix planning and implementation methodology for resolving behavioral discrepancies in Android apps, including blast radius estimation, dependency ordering, minimal-change implementation, and post-fix verification. |
| [android-behavior-trace](android-behavior-trace/) | Deep code path tracing methodology for Android applications that follows user actions through all architectural layers (UI → ViewModel → Repository → Data → Network/Background) and produces a factual behavior catalog. |
| [android-crash-triage](android-crash-triage/) | Systematic crash investigation workflow covering reproduction from stack traces, device/OS isolation, root cause analysis for ANRs, OOMs, and native crashes, and fix production with regression tests. |
| [android-deep-link-architect](android-deep-link-architect/) | Design and validate deep link architecture covering App Links verification, intent filters, Navigation component integration, deferred deep links, and link testing automation. |
| [android-emulator-management](android-emulator-management/) | Android emulator setup, configuration, snapshot management, headless CI execution, and multi-device testing. |
| [android-firebase-sync-validator](android-firebase-sync-validator/) | Validate that Android app data properly syncs to Firebase by analyzing features and verifying cloud infrastructure |
| [android-hilt-di](android-hilt-di/) | Master Hilt dependency injection for Android including module design, scoping, and ViewModel integration |
| [android-multi-source-data-layer](android-multi-source-data-layer/) | Architectural patterns for Android apps that coordinate data across Room (local cache/offline), Firebase Realtime Database (real-time sync), and Firestore (structured queries) through a unified repository layer. |
| [android-play-billing-subscriptions](android-play-billing-subscriptions/) | Implements Google Play Billing Library 7+ for in-app purchases and subscriptions. |
| [android-quarterly-maintenance](android-quarterly-maintenance/) | Comprehensive quarterly maintenance workflow covering dependencies, security, performance, Play Store compliance, Firebase costs, and technical debt. |
| [android-release-pipeline](android-release-pipeline/) | End-to-end Android release workflow covering version bumping, changelog generation, signing config verification, ProGuard/R8 rules validation, bundle generation, and Play Console upload preparation. |
| [android-rich-notification-system](android-rich-notification-system/) | Comprehensive Android notification system covering FCM integration, notification channels per feature, rich notifications with actions and media, geofence-triggered location reminders, in-app messaging, and Android… |
| [android-room-database](android-room-database/) | Master Room persistence library for Android including entity design, DAO patterns, migrations, and type converters |
| [android-screenshot-testing](android-screenshot-testing/) | Screenshot-based UI testing for Android using ADB screen capture, Compose Preview Screenshot Testing, Paparazzi, and Roborazzi. |
| [android-testing-patterns](android-testing-patterns/) | Master Android testing including unit tests, instrumented tests, Compose testing, and end-to-end testing |
| [ios-app-developer](ios-app-developer/) | Develops iOS applications with XcodeGen, SwiftUI, and SPM. |
| [jetpack-compose-patterns](jetpack-compose-patterns/) | Master Jetpack Compose UI development with state management, navigation, theming, and Material 3 |
| [mobile-ui-element-audit](mobile-ui-element-audit/) | Perform hyper-detailed, pixel-level audits of individual mobile UI elements analyzing visual design, interaction states, micro-animations, accessibility, engagement potential, and platform compliance. |
| [mobile-ui-habit-loop-design](mobile-ui-habit-loop-design/) | Design habit-forming engagement systems for mobile apps using the Hook Model, Fogg Behavior Model, gamification science, and behavioral psychology. |
| [mobile-ui-micro-interactions](mobile-ui-micro-interactions/) | Design and implement delightful micro-interactions for mobile apps including touch feedback, transitions, loading states, celebration animations, haptic patterns, and state change animations. |
| [nextjs-app-router-patterns](../web-development/nextjs-app-router-patterns/) | Master Next.js 14+ App Router with Server Components, streaming, parallel routes, and advanced data fetching |
| [react-native-architecture](react-native-architecture/) | Build production React Native apps with Expo, navigation, native modules, and offline sync |
| [react-state-management](../web-development/react-state-management/) | Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query |
| [tailwind-design-system](../web-development/tailwind-design-system/) | Build scalable design systems with Tailwind CSS, design tokens, component libraries, and responsive patterns |

## Vendored Android Skills (upstream: google/android-skills)

Eight skills here are **vendored verbatim** from Google's official
[android/skills](https://github.com/android/skills) repo (Apache-2.0), pinned to a
recorded upstream commit. Their value is first-party grounding — mirrored
developer.android.com reference bundles we cannot author ourselves.

`android-agp-9-upgrade` · `android-edge-to-edge` · `android-migrate-xml-to-compose` ·
`android-navigation-3` · `android-play-billing-upgrade` · `android-play-policy-insights` ·
`android-r8-analyzer` · `android-xr-jetpack-compose-glimmer`

**Do not hand-edit these.** Local edits are lost on the next sync, and hand-edits are
how the previous copies drifted into shipping stale, factually wrong guidance. Each
skill's local additions (When NOT to Use / Verification / Related Skills) live in its
`local-wrapper.md` and are re-appended below the upstream body on every sync — edit
that file, never the block inside `SKILL.md`.

- Provenance, known quality gaps, and the re-sync procedure:
  [`ANDROID_SKILLS_UPSTREAM.md`](ANDROID_SKILLS_UPSTREAM.md)
- Upstream license: [`ANDROID_SKILLS_LICENSE.txt`](ANDROID_SKILLS_LICENSE.txt)
- Sync tool: [`scripts/resync_android_skills.py`](scripts/resync_android_skills.py)

Most upstream skill bodies omit False-Positive Prevention, Verification, and
anti-fabrication clauses — treat version numbers and API claims they emit as
`[VERIFY]` against official docs. (`android-play-policy-insights` is the exception:
its discipline lives in `resources/`, and it is rigorous. See
[`ANDROID_SKILLS_UPSTREAM.md`](ANDROID_SKILLS_UPSTREAM.md).)

**Policy compliance:** run `android-play-policy-insights` (upstream, deep Play static
analysis, needs Python) then [`mobile-store-policy-readiness`](mobile-store-policy-readiness/)
(ours: cross-store, script-free, live-policy verification, rejection triage).

## Usage

These skills provide specialized knowledge for Claude Code. They are automatically invoked when relevant to your task, or can be explicitly referenced.

## Related Resources

- [Skills Index](../README.md) - Complete skills catalog
- [Agents Index](../../agents/README.md) - Task-specific agents
