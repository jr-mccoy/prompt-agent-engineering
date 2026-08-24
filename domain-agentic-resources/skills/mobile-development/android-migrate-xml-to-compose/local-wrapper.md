## When NOT to Use This Skill

Do NOT use this skill when:

- **You want to migrate the whole app in one pass.** The ten steps are built around
  one well-chosen screen at a time, starting from Step 1's candidate selection. A
  big-bang rewrite discards the baseline-screenshot safety net that makes Step 9
  meaningful.
- **The screen is scheduled for deletion or redesign.** Migrating UI that is about to
  be replaced is wasted work — rebuild it in Compose directly.
- **The layout is driven by a third-party SDK's own Views** (embedded maps, ad
  containers, payment or vendor SDK UI). Those often have no Compose equivalent;
  wrap with interop rather than migrating.
- **Compose dependencies cannot be added** — minSdk, build constraints, or an
  organizational ban.
- **The screen is heavily custom-drawn** (custom `View.onDraw`, complex touch
  handling). Migration is a rewrite, not a translation, and belongs on a feature
  roadmap rather than in this workflow.

## Related Skills

- [`android-screenshot-testing`](../android-screenshot-testing/) — formalizes the
  Step 4 baseline capture and the Step 9 comparison into a regression suite.
- [`android-edge-to-edge`](../android-edge-to-edge/) — **run after.** Newly migrated
  Compose screens frequently need inset work that the XML original got from the
  View system.
- [`jetpack-compose-patterns`](../jetpack-compose-patterns/) — state hoisting and
  composition patterns for the code you produce in Step 7.
- [`android-navigation-3`](../android-navigation-3/) — once enough screens are
  Compose, fragment-based navigation is usually the next thing to go.
- [`android-testing-patterns`](../android-testing-patterns/) — the Compose UI test
  Step 9 asks you to write.
