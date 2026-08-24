## When NOT to Use This Skill

Do NOT use this skill when:

- **The target is not an Android app source tree** — iOS, or a store listing you
  cannot build from source. Use
  [`mobile-store-policy-readiness`](../mobile-store-policy-readiness/).
- **Python 3 or a writable workspace scratch directory is unavailable.** Phase 1 has
  an explicit fail-fast mandate: if `orchestrator.py` fails you must stop, and manual
  auditing is forbidden as a fallback. In a constrained environment, use
  [`mobile-store-policy-readiness`](../mobile-store-policy-readiness/), which is
  script-free.
- **The app has already been rejected.** Working backward from a citation is a
  different task — use the rejection playbook in
  [`mobile-store-policy-readiness`](../mobile-store-policy-readiness/).
- **You need App Store / cross-platform coverage.** This skill is Play-only.
- **You want a legal opinion or an approval guarantee.** The generated report's own
  disclaimer is correct: Play review has final authority. Route legal questions to
  `domain-legal/`.

## Policy currency caveat

The bundled `resources/policies.json` and the policy prose in the goal files are a
**snapshot** pinned to this skill's `last-updated` date. Play policy changes
frequently. The audit's *analysis* remains sound, but before acting on any specific
requirement, open the policy URL that `policies.json` carries for that entry and
confirm the current wording. Do not treat a bundled excerpt as verification.

## Verification

The two-phase protocol validates its own *pipeline* (worker JSON exists and parses,
critic chunks complete). That is not the same as validating the *report*. Before
acting on `compliance_report.md`, check:

- [ ] Every `🔴 Critical` and `🟡 Important` finding cites a real file and line, and
      that line actually contains what the finding claims — per the Concrete
      Attributions mandate in `resources/common_mandates.md`
- [ ] No finding rests on code inside `build/`, `test/`, `androidTest/`, or a sample
      module
- [ ] No finding treats local-only processing (on-device cache, prefs, local DB) as
      collection or sharing
- [ ] Findings the critic marked `MANUAL_REVIEW` are presented as open questions, not
      as violations
- [ ] Findings the critic `PRUNED` do not reappear in the final report
- [ ] Empty result sets render as `[]`, not as placeholder or `N/A` entries
- [ ] Data Safety discrepancies are framed against declarations the user actually
      supplied — the skill cannot read the Play Console
- [ ] The disclaimer is intact

Then verify the policy itself is current — see the caveat above. A correct finding
against a superseded policy is still wasted work.

If the run produced an unusually long Critical list, re-check the first three boxes
before escalating anything: over-flagging is the failure mode these mandates exist to
prevent.

## Related Skills

- [`mobile-store-policy-readiness`](../mobile-store-policy-readiness/) — **the
  complement, run after this.** Covers what this skill does not: the Apple App Store,
  non-code submission surfaces (store listing, screenshots, age rating, privacy
  policy URL reachability, review notes), live policy verification, and rejection
  triage. It is script-free, so it also serves as the fallback when this skill's
  prerequisites are unavailable.
- [`android-play-billing-upgrade`](../android-play-billing-upgrade/) — monetization
  findings usually land here.
- [`android-release-pipeline`](../android-release-pipeline/) — gate the release train
  on a clean audit.
- [`android-quarterly-maintenance`](../android-quarterly-maintenance/) — recurring
  cadence; policy drift is a standing risk, not a one-time check.

> **Note on quality.** This skill's false-positive discipline lives in
> `resources/common_mandates.md` and `resources/critic.md` rather than in this body —
> presumption of compliance, mandatory `file:line` citation before any
> Critical/Important finding, forced downgrade where compliance cannot be verified,
> and a `VERIFIED`/`MANUAL_REVIEW`/`PRUNED` critic pass. Read those before assuming
> anything is missing, and preserve them if you ever adapt this skill.
