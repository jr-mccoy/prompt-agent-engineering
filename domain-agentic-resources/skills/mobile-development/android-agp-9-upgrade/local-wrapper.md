## When NOT to Use This Skill

Do NOT use this skill when:

- **The project is Kotlin Multiplatform.** Upstream states KMP is unsupported. Stop
  and escalate rather than improvising.
- **AGP is below 9 and you have not run the Upgrade Assistant.** Per Requirements
  above, get to the latest stable AGP 8.x in Android Studio first. Skipping this
  turns one migration into two overlapping ones and makes failures hard to attribute.
- **You only want the latest stable AGP 8.x.** That is the Upgrade Assistant's job,
  not this skill's.
- **You are chasing a Gradle, JDK, or Kotlin upgrade on its own.** Those have their
  own compatibility tables; this skill only handles them as AGP 9 dependencies.
- **The build is already broken.** Fix the existing build first. Migrating on top of
  a red build makes it impossible to tell which failure is which.

## Related Skills

- [`android-r8-analyzer`](../android-r8-analyzer/) — **run after this.** AGP 9
  unlocks optimizations that change which keep rules matter; analyzing beforehand
  produces advice you will have to redo.
- [`android-play-billing-upgrade`](../android-play-billing-upgrade/) — Play Billing
  versions carry their own AGP/Kotlin minimums. If both are due, sequence AGP first.
- [`android-release-pipeline`](../android-release-pipeline/) — CI and signing config
  frequently need updating alongside a major AGP bump.
- [`android-quarterly-maintenance`](../android-quarterly-maintenance/) — the cadence
  that should catch AGP drift before it becomes a forced migration.
