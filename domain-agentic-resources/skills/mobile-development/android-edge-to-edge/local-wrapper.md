## When NOT to Use This Skill

Do NOT use this skill when:

- **The UI is XML/View-based.** Every pattern here assumes Compose. Migrate first
  with [`android-migrate-xml-to-compose`](../android-migrate-xml-to-compose/), or
  handle insets with the View-system APIs instead.
- **You cannot target SDK 35+.** That is a hard prerequisite above, not a suggestion.
- **The app is Wear OS or XR.** Both use a different inset and safe-area model.
  Applying phone edge-to-edge patterns there produces wrong layouts — see
  [`android-xr-jetpack-compose-glimmer`](../android-xr-jetpack-compose-glimmer/).
- **You are debugging a single clipped component and already know the cause.** The
  full plan/apply pass is heavier than editing one modifier.
- **The app deliberately runs immersive/fullscreen** (games, video players, camera
  viewfinders). Those manage system bars directly; forcing standard inset handling
  fights the design.

## Related Skills

- [`android-migrate-xml-to-compose`](../android-migrate-xml-to-compose/) —
  prerequisite for XML screens.
- [`android-accessibility-testing`](../android-accessibility-testing/) — **run
  after.** Inset mistakes surface as touch targets under the navigation bar, which
  is an accessibility failure before it is a cosmetic one.
- [`android-screenshot-testing`](../android-screenshot-testing/) — inset regressions
  are exactly what screenshot tests catch; capture across gesture and 3-button
  navigation modes.
- [`jetpack-compose-patterns`](../jetpack-compose-patterns/) — general Compose
  layout and state work.
- [`android-xr-jetpack-compose-glimmer`](../android-xr-jetpack-compose-glimmer/) —
  different platform, different safe-area rules.
