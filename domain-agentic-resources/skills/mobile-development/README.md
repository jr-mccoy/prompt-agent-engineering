# Mobile Development Skills

> Skills for Android, React Native, Next.js, and cross-platform mobile development patterns.

## Skills in This Category

| Skill | Description |
|-------|-------------|
| [android-firebase-sync-validator](android-firebase-sync-validator/) | Validate that Android app data properly syncs to Firebase by analyzing features and verifying cloud infrastructure |
| [android-hilt-di](android-hilt-di/) | Master Hilt dependency injection for Android including module design, scoping, and ViewModel integration |
| [android-room-database](android-room-database/) | Master Room persistence library for Android including entity design, DAO patterns, migrations, and type converters |
| [android-testing-patterns](android-testing-patterns/) | Master Android testing including unit tests, instrumented tests, Compose testing, and end-to-end testing |
| [jetpack-compose-patterns](jetpack-compose-patterns/) | Master Jetpack Compose UI development with state management, navigation, theming, and Material 3 |
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
