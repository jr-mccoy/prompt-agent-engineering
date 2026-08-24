## When NOT to Use This Skill

Do NOT use this skill when:

- **Navigation 2 / Navigation-Compose is working and nothing is forcing a move.**
  Navigation 3 is a different model, not a drop-in upgrade. Migrate for a concrete
  reason — adaptive layouts, multi-pane scenes, back-stack control you cannot express
  today — not for currency.
- **The app is fragment- and XML-based.** Migrate the UI layer first with
  [`android-migrate-xml-to-compose`](../android-migrate-xml-to-compose/). Doing both
  at once makes every failure ambiguous.
- **The app is a single screen, or a handful with no shared back stack.** The
  machinery costs more than it returns.
- **You need one specific recipe** (a deep link, a dialog destination). Read that
  recipe directly rather than running a migration.
- **The project pins an older Compose BOM** that predates the required Navigation 3
  artifacts.

## Verification

After migration, confirm:

- [ ] Project builds and IDE sync succeeds
- [ ] Every destination reachable in the old graph is still reachable
- [ ] System back and predictive back behave correctly at every depth, including the
      root — no dead ends, no unexpected app exit
- [ ] Back stack survives configuration change **and** process death (test with "Don't
      keep activities" enabled)
- [ ] `ViewModel` scoping matches intent — scoped ViewModels are cleared when their
      destination leaves the back stack, and not before
- [ ] Every deep link resolves to the same destination and arguments as before
- [ ] Results are returned to the correct caller after a process-death round trip
- [ ] Conditional and multi-back-stack flows behave under rapid navigation
- [ ] Adaptive/multi-pane scenes restore correctly across a fold, rotation, or window
      resize

Untested process death is the most common way a Navigation 3 migration ships broken.

## Related Skills

- [`android-migrate-xml-to-compose`](../android-migrate-xml-to-compose/) —
  prerequisite for fragment-based apps.
- [`android-deep-link-architect`](../android-deep-link-architect/) — deep-link
  design; verify links still resolve after migrating.
- [`android-edge-to-edge`](../android-edge-to-edge/) — scene and pane changes alter
  which composable owns insets.
- [`jetpack-compose-patterns`](../jetpack-compose-patterns/) — state hoisting across
  destinations.
- [`android-testing-patterns`](../android-testing-patterns/) — instrumenting the
  back-stack and process-death checks above.
