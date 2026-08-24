## Anti-fabrication override (read before Phase 2)

Phase 2 above instructs you to *"consult your knowledge of the Google Play Billing
documentation."* **Treat that as a pointer to go read the docs, not a licence to
recall them.** Billing API surface, version minimums, and deprecation timelines
change frequently, and a confidently wrong version number sends a developer into a
migration they did not need.

While running this skill:

- Do **not** state a PBL version number, `compileSdk`/`targetSdk` minimum, API
  signature, or deprecation deadline unless you read it in this session from the
  bundled `references/` or an official page.
- Anything unverified is written `[VERIFY: <what to confirm, and where>]`. Never
  substitute a plausible value.
- The bundled `references/android/google/play/billing/release-notes.md` is a snapshot
  pinned to this skill's `last-updated` date. If the migration target is newer than
  that snapshot, say so and verify against the live release notes.
- Do not assert what a specific PBL version "removed" or "introduced" from memory.
  Cite the release-notes entry.

This overrides any conflicting instruction above.

## When NOT to Use This Skill

Do NOT use this skill when:

- **You are integrating Play Billing for the first time.** This is an upgrade path
  that reasons from an existing effective version. Fresh integrations should start
  from the current official getting-started guide.
- **You are designing or changing subscription products** — base plans, offers,
  prepaid plans, grace periods. Use
  [`android-play-billing-subscriptions`](../android-play-billing-subscriptions/).
- **The app does not ship through Google Play** (sideloaded, enterprise, alternative
  store). Play Billing may not apply at all.
- **Only server-side purchase verification is broken.** That is backend work; this
  skill migrates client library usage.
- **The build is already failing for unrelated reasons.** Phase 1 uses build success
  as its discovery signal, so a pre-existing red build corrupts the version detection.

## Related Skills

- [`android-play-billing-subscriptions`](../android-play-billing-subscriptions/) —
  subscription product design, the usual follow-on once the library is current.
- [`android-agp-9-upgrade`](../android-agp-9-upgrade/) — a PBL bump often forces AGP,
  Kotlin, or `compileSdk` minimums. If both are due, sequence AGP first.
- [`android-play-policy-insights`](../android-play-policy-insights/) — billing
  changes carry policy surface (subscription terms disclosure, purchase flows).
- [`mobile-store-policy-readiness`](../mobile-store-policy-readiness/) — verify
  monetization disclosure before submitting the release.
- [`android-release-pipeline`](../android-release-pipeline/) — billing changes need
  testing against real Play test tracks, not just a local build.
