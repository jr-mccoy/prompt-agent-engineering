# Vendored Android Skills — Upstream Provenance & Sync Procedure

Eight skills in this directory are **vendored verbatim** from Google's official
[android/skills](https://github.com/android/skills) repository. They are not our
original work and must not be hand-edited.

**Upstream:** https://github.com/android/skills
**License:** Apache License 2.0 — full text in [`ANDROID_SKILLS_LICENSE.txt`](ANDROID_SKILLS_LICENSE.txt)
**Pinned commit:** `23d9eae21a4bfe0209e5b678f0ebe931e3c7dff4` (2026-07-29)
**Last synced:** 2026-08-02

---

## Vendored skills

| Our directory | Upstream path | Upstream `last-updated` |
|---|---|---|
| `android-agp-9-upgrade` | `build-system/agp/agp-9-upgrade` | 2026-07-23 |
| `android-edge-to-edge` | `system/edge-to-edge` | 2026-04-01 |
| `android-migrate-xml-to-compose` | `jetpack-compose/migration/migrate-xml-views-to-jetpack-compose` | 2026-07-02 |
| `android-navigation-3` | `navigation/navigation-3` | 2026-07-18 |
| `android-play-billing-upgrade` | `play/play-billing-library-version-upgrade` | 2026-07-02 |
| `android-play-policy-insights` | `play/play-policy-insights` | 2026-07-13 |
| `android-r8-analyzer` | `performance/r8-analyzer` | 2026-07-18 |
| `android-xr-jetpack-compose-glimmer` | `xr/display-glasses-with-jetpack-compose-glimmer` | 2026-07-22 |

---

## Why vendored, not rewritten

These skills' value is **first-party grounding**, not prompt craft. The bulk of each
bundle is a `references/android/…` mirror of developer.android.com — AGP 9 release
notes, Play Billing migration guides, Navigation 3 recipes, the R8 configuration
analyzer workflow. We cannot author that content, and any paraphrase of it would be
less accurate and would rot faster than Google updates the original.

What we add is the discipline layer most (not all) upstream skills omit from their
skill bodies — see [Known quality gaps](#known-quality-gaps-vs-our-rubric) below for
where that holds and where it does not.

---

## The only local modification

The sync rewrites exactly two things in each `SKILL.md` frontmatter:

1. `name:` — prefixed to match our directory name (our rubric requires
   `name` == directory name).
2. Provenance keys injected under `metadata:`:

```yaml
metadata:
  author: Google LLC
  last-updated: '2026-07-18'        # upstream's own staleness marker — never strip this
  upstream: https://github.com/android/skills
  upstream-path: performance/r8-analyzer
  upstream-commit: 23d9eae21a4bfe0209e5b678f0ebe931e3c7dff4
  upstream-synced: '2026-08-02'
```

Everything else — body, `references/`, `scripts/` — is byte-identical to upstream.

> **Do not strip `last-updated`.** A previous vendoring removed it, which is how these
> forks drifted undetected: `android-r8-analyzer` sat on a superseded architecture and
> `android-play-billing-upgrade` shipped a factually wrong `compileSdk` requirement
> (claimed PBL 8, upstream had moved to PBL 9).

---

## Local overlays

An **overlay** is a file present in our fork but absent upstream — a deliberate local
addition. The sync script snapshots overlays before overwriting and restores them
afterward, reporting each one, so they survive re-syncs instead of being silently
deleted. `SKILL.md` is never treated as an overlay; the skill body always comes from
upstream verbatim.

Current overlays:

| Skill | Overlay | Why |
|---|---|---|
| `android-xr-jetpack-compose-glimmer` | `references/android/develop/xr/jetpack-xr-sdk/ai-glasses/check-capabilities.md`<br>`…/ai-glasses/first-activity.md`<br>`…/ai-glasses/notifications/behavior.md`<br>`…/ai-glasses/notifications/start-activity.md` | Offline mirrors of four developer.android.com pages that upstream's `SKILL.md` only links to over HTTPS. Keeps the skill usable without network access. |

Those four are now reachable: the skill's wrapper block (below) carries a table
mapping each linked page to its local mirror, so the workflow survives without
network access.

---

## Local wrapper blocks

Upstream skill bodies omit sections our rubric requires. Hand-editing a vendored
`SKILL.md` to add them would be silently discarded on the next sync — so each skill
keeps its additions in **`local-wrapper.md`** at the skill root, and the sync script
appends that file below the upstream body:

```
SKILL.md  =  upstream frontmatter (+ provenance keys)
          +  upstream body, byte-identical
          +  ---
          +  <!-- BEGIN LOCAL WRAPPER -->
          +  contents of local-wrapper.md
```

`local-wrapper.md` is itself an overlay (absent upstream), so it is preserved
automatically. The append is idempotent — guarded by the marker — and the sync
verifies the upstream body above the marker stays byte-identical.

**To change a wrapper, edit `local-wrapper.md`, never the block inside `SKILL.md`.**

What each wrapper adds (only what that skill actually lacked):

| Skill | When NOT to Use | Verification | Related Skills | Extra |
|---|:-:|:-:|:-:|---|
| `android-agp-9-upgrade` | ✅ | — *(has one)* | ✅ | |
| `android-edge-to-edge` | ✅ | — *(`## Checklist`)* | ✅ | |
| `android-migrate-xml-to-compose` | ✅ | — *(Step 9)* | ✅ | |
| `android-navigation-3` | ✅ | ✅ | ✅ | Process-death & back-stack checks |
| `android-play-billing-upgrade` | ✅ | — *(Step 4)* | ✅ | **Anti-fabrication override** |
| `android-play-policy-insights` | ✅ | ✅ | ✅ | Policy-currency caveat; report sanity-check |
| `android-r8-analyzer` | ✅ | ✅ | ✅ | Splits report-verify from post-change verify |
| `android-xr-jetpack-compose-glimmer` | — *(`## Limitations`)* | ✅ | ✅ | Offline mirror index |

The two highest-value additions are not the boilerplate sections:

- **`android-play-billing-upgrade`** — an explicit override of upstream's *"consult
  your knowledge of the Google Play Billing documentation"*, forbidding version
  numbers, SDK minimums, API signatures, and deprecation dates stated from memory.
- **`android-play-policy-insights`** — a policy-currency caveat (the bundled
  `policies.json` is a snapshot; verify against the live URL before acting) plus a
  report sanity-check that applies upstream's own mandates as an output gate.

---

## Re-sync procedure

Run at least quarterly (wired into `android-quarterly-maintenance`), or whenever
upstream announces a release.

```bash
# 1. Clone upstream to a scratch dir
git clone --depth 1 https://github.com/android/skills.git /tmp/android-skills
UPSTREAM_SHA=$(git -C /tmp/android-skills rev-parse HEAD)

# 2. Diff against our vendored copies before syncing (review what changed)
for d in android-agp-9-upgrade android-r8-analyzer android-edge-to-edge \
         android-navigation-3 android-play-billing-upgrade \
         android-play-policy-insights android-migrate-xml-to-compose \
         android-xr-jetpack-compose-glimmer; do
  echo "=== $d ==="
  # upstream path comes from the skill's own metadata.upstream-path
  UP=$(grep -m1 'upstream-path:' "$d/SKILL.md" | sed 's/.*upstream-path: //')
  diff -rq "/tmp/android-skills/$UP" "$d" | grep -v '^Only in .*: \.' || echo "  (no drift)"
done

# 3. Sync
python3 scripts/resync_android_skills.py /tmp/android-skills . "$UPSTREAM_SHA" "$(date +%F)"
```

**After any sync, re-check:**

- [ ] `name:` still matches each directory name
- [ ] `last-updated:` present in all eight
- [ ] Upstream added new skills we should vendor (`find /tmp/android-skills -name SKILL.md`)
- [ ] Upstream *renamed or removed* a skill we vendor
- [ ] Every `local-wrapper.md` survived and was re-appended (script reports `[+wrapper appended]`)
- [ ] Upstream did not add a section a wrapper now duplicates — if it did, trim the wrapper

---

## Known quality gaps vs. our rubric

Scored against [`SKILL_QUALITY_RUBRIC.md`](../../../authoring/skill-patterns/SKILL_QUALITY_RUBRIC.md),
upstream skills land in the **72–82/100** range. They score full marks on progressive
disclosure, actionability, and description/trigger engineering. They lose points on,
across all 20 upstream skills:

| Gap | Incidence upstream | Closed for the 8 we vendor? |
|---|---|---|
| No **Related Skills** section | 20 / 20 | ✅ all 8, via wrapper |
| No **When NOT to Use** / Limitations | 15 / 20 | ✅ all 8 |
| No **Verification** section | 19 / 20 | ✅ all 8 |
| No **Troubleshooting** section | 19 / 20 | ⚠️ only where upstream had one — not synthesized |
| No **False-Positive Prevention** | 20 / 20 | ⚠️ see caveat below |
| No **anti-fabrication clause** | 20 / 20 | ✅ where it matters (`play-billing`, `play-policy-insights`) |

**Important caveat on that table:** it counts *section headings in `SKILL.md` bodies*.
Some skills carry the discipline in `resources/` files loaded by sub-agents instead.
`android-play-policy-insights` is the notable case — see below. Judge a skill by its
whole bundle, not its `SKILL.md` alone.

Two concrete instances worth knowing about when using these:

- **`android-play-billing-upgrade`** instructs the agent to *"consult your knowledge of
  the Google Play Billing documentation"* — an open invitation to assert API surface
  from memory. Treat every version number and API claim it produces as `[VERIFY]`.
- **`android-play-policy-insights`** is the opposite case, and the strongest skill in
  the upstream set. Its `resources/common_mandates.md` enforces presumption of
  compliance, a mandatory `file:line` citation before any Critical/Important finding,
  forced downgrade to Suggestion where compliance can't be verified, exclusion of
  local-only processing, and empty-list discipline. `resources/critic.md` adds a
  review pass grading each finding `VERIFIED` / `MANUAL_REVIEW` / `PRUNED`, and the
  report template carries a proper not-legal-advice, not-a-guarantee-of-approval
  disclaimer. This is stronger false-positive discipline than several of our own
  skills. **It is vendored, not reimplemented.**

  Its real limits are scope and dependencies, not rigor: Play only (no App Store), a
  hard dependency on five bundled Python scripts plus a writable scratch directory
  (`orchestrator.py` fails fast with no fallback), and a policy corpus pinned at
  `2026-07-13` with no instruction to re-verify against live policy pages. Those gaps
  are covered by our complementary
  [`mobile-store-policy-readiness`](mobile-store-policy-readiness/) skill, which is
  script-free, cross-store, and requires live policy verification.

**Status:** the wrapper mechanism above closes When NOT to Use, Verification, and
Related Skills across all eight. Two gaps are deliberately left open:

- **Troubleshooting** is not synthesized. Inventing failure modes for a workflow we
  did not author would be fabrication of exactly the kind this doc warns about. Where
  upstream ships one (`android-agp-9-upgrade`), it stands.
- **False-Positive Prevention** is added only where a skill produces *findings*
  (`android-r8-analyzer`, `android-play-policy-insights`). It is meaningless on a
  migration workflow, and adding an empty section to score rubric points would be
  cargo-culting.

---

## Skills we deliberately do NOT vendor

| Upstream skill | Why not |
|---|---|
| `devtools/android-cli` | Wraps a Google-specific CLI installer; not useful outside their toolchain. |
| `profilers/perfetto-*`, `camera/camerax`, `wear/*`, `identity/*`, `device-ai/*`, `play/engage-sdk-integration`, `jetpack-compose/adaptive`, `jetpack-compose/theming/styles`, `security/android-intent-security`, `testing/testing-setup` | Not yet evaluated for vendoring. Candidates for a future pass — `security/android-intent-security` in particular is strong. |
