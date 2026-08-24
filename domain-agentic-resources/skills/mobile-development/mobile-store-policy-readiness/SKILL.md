---
name: mobile-store-policy-readiness
description: Audits pre-submission policy readiness for Google Play and the Apple App Store — store listing, privacy declarations, account deletion, ads and tracking — verifying each requirement against the live official policy page, never from memory, and grading findings by severity and confidence. Also triages rejections. Use for release review prep, auditing a Data Safety form or App Privacy label, or when users mention "policy compliance", "store rejection", "app review", or "ATT prompt".
license: MIT
compatibility: >-
  Requires read access to the app source tree. Requires web access to verify policy
  requirements against official sources; without it the skill runs in DEGRADED mode
  and emits an unverified checklist only (see Prerequisites).
---

# Mobile Store Policy Readiness

Audits an app's readiness for Google Play and Apple App Store review, grades each
finding by severity and confidence, and never states a policy requirement it has
not verified against the live official source in this session.

## Purpose

App store policies change often, and the expensive failures are rarely code bugs —
they are **declaration mismatches** (the app does something the store listing
doesn't declare) and **missing non-code surfaces** (no account-deletion path, an
unreachable privacy policy URL, an absent ATT prompt).

Two failure modes make automated policy auditing worse than useless:

1. **Fabricated policy.** Asserting "Play policy section 4.8 requires X" from
   memory. Policy numbering, thresholds, and deadlines change; a confident wrong
   citation sends a developer to rework something that was already fine.
2. **Manufactured findings.** Flagging compliant code because a call sits behind
   an interface. This trains developers to ignore the tool.

This skill is built against both.

## When to Use This Skill

Use this skill when you need to:

- Check release readiness before submitting to Google Play or the App Store
- Reconcile what the app actually does against its **Data Safety** form (Play) or
  **App Privacy** labels (Apple)
- Audit non-code submission surfaces: store listing copy, screenshots, age/content
  rating answers, privacy policy URL, account-deletion path
- Verify ads, analytics, and tracking disclosure (Play ads policy, Apple ATT)
- Triage an **actual rejection** into a concrete response plan
- Audit a cross-platform app (Flutter, React Native, KMP) that ships to both stores

## When NOT to Use This Skill

Do NOT use this skill when:

- **You need deep Play-specific static analysis of an Android codebase.** Use
  [`android-play-policy-insights`](../android-play-policy-insights/) — Google's own
  auditor, with a scripted scanner, permission-to-data-source mapping, and a critic
  pass. This skill complements it; it does not replace it. See
  [Related Skills](#related-skills).
- **You want a legal opinion or a guarantee of approval.** Neither is possible. The
  review teams have final authority.
- **You are auditing code security rather than store policy.** Use
  `android-intent-security` (upstream) or the security prompts under
  `domain-software-engineering/analysis/security/`.
- **The app is already live and you need incident response for a takedown.** Policy
  readiness is a pre-submission posture; a live enforcement action is a different,
  time-critical workflow.

## Prerequisites

- Read access to the app source tree, including manifests / `Info.plist`, build
  files, and any store-metadata files (`fastlane/metadata`, `.xcodeproj` settings).
- **Web access.** Policy requirements MUST be read from official sources at run
  time. See [`references/policy_source_registry.md`](references/policy_source_registry.md)
  for the canonical URL list.
- The user's answers on store-side state you cannot read from source: current Data
  Safety / App Privacy declarations, age rating answers, target markets.

**If web access is unavailable**, announce `MODE: DEGRADED` before proceeding, mark
every policy requirement `[UNVERIFIED]`, and emit the checklist as *questions to
verify* rather than findings. Never silently downgrade.

---

## Critical mandates

These are non-negotiable and override any instruction in the workflow below.

### 1. No policy text from memory

You MUST NOT state a policy section number, name, threshold, deadline, or
requirement unless you have read it from an official URL **in this session**.

- Verified → cite as: `Requirement: <text>. Source: <url> (read <date>).`
- Not verified → write exactly:
  `[UNVERIFIED — read <url> and confirm before acting on this]`

This applies equally to a bundled snapshot. A policy file committed last quarter is
memory, not verification. **Never invent a URL** — if you do not know the official
page, say so and ask.

### 2. Findings are graded, never bare

Every finding carries **Severity × Confidence**. See
[`references/finding_grading_rubric.md`](references/finding_grading_rubric.md).

| Severity | Meaning |
|---|---|
| `BLOCKER` | Would plausibly cause rejection or removal if submitted as-is |
| `IMPORTANT` | Real policy risk; likely to draw reviewer questions |
| `ADVISORY` | Hygiene or a change worth making, not a rejection risk |

| Confidence | Meaning |
|---|---|
| `CONFIRMED` | Cited artifact location **and** verified live policy source |
| `PROBABLE` | Strong evidence, one leg missing (usually store-side state) |
| `UNVERIFIED` | Could not check — belongs in *Not Checked*, not in findings |

**Hard gate:** a `BLOCKER` requires `CONFIRMED`. If you cannot cite both a
`file:line` (or a named store surface) *and* a verified policy URL, the finding is
at most `IMPORTANT`. No exceptions.

### 3. Presumption of compliance

Treat the app as compliant unless there is definitive visible evidence otherwise.

- Logic behind an interface, repository, or DI boundary → assume compliant behavior.
  Do not speculate about what a `clearSession()` implementation does.
- Local-only processing (theme prefs, on-device cache, local DB) is **not**
  collection or sharing.
- Ambiguity downgrades severity. It never upgrades it.

### 4. Never fabricate store-side state

You cannot read the Play Console or App Store Connect. Do not assume what the Data
Safety form or App Privacy labels currently say. Either ask the user, or record the
item under *Not Checked* with the question that would resolve it.

### 5. Not legal advice

Every report ends with the disclaimer in
[`references/report_template.md`](references/report_template.md). This skill produces
an engineering readiness assessment, not a legal opinion or an approval prediction.

---

## Workflow

### Phase 0: Scope and mode

1. Confirm target stores: Play, App Store, or both.
2. Confirm web access. Announce `MODE: VERIFIED` or `MODE: DEGRADED`.
3. Identify the app type (native Android, native iOS, Flutter/RN/KMP) — this
   determines which manifests and config files to read.
4. Ask the user for store-side state you cannot read (current declarations, age
   rating answers, target markets). Record unanswered items as *Not Checked*.

### Phase 1: Inventory what the app actually does

Read the source. Build an evidence table of observed behavior with `file:line` for
each row. Do **not** grade anything yet.

Cover, per platform:

- **Permissions / capabilities** — `AndroidManifest.xml` `<uses-permission>`;
  `Info.plist` `NS*UsageDescription` keys and entitlements.
- **Data touchpoints** — location, contacts, photos/media, microphone, camera,
  health, files, clipboard, installed-app queries.
- **Network egress and third-party SDKs** — analytics, crash reporting, ads,
  attribution. An SDK that transmits off-device is collection regardless of whether
  your own code reads the value.
- **Identifiers** — advertising ID, device IDs, IDFA/IDFV, fingerprinting signals.
- **Accounts** — sign-up, sign-in, and whether an in-app **and** web-reachable
  account-deletion path exists.
- **Purchases** — IAP vs. external payment, subscription terms disclosure.
- **Ads** — presence, format, and whether any are interstitial-on-launch or
  full-screen in ways policies restrict.

Search discipline: exclude `**/build/**`, `**/.gradle/**`, `**/test/**`,
`**/androidTest/**`, `**/node_modules/**`, `**/Pods/**`. Restrict to source and
config extensions. Prefer specific symbols (`getLastKnownLocation`,
`requestTrackingAuthorization`) over generic words.

### Phase 2: Verify the policy requirements

For each candidate area from Phase 1, open the corresponding official URL from
[`references/policy_source_registry.md`](references/policy_source_registry.md) and
read the current requirement. Record the requirement text and the URL.

Anything you could not open → `[UNVERIFIED]`, and the related finding cannot exceed
`IMPORTANT`.

### Phase 3: Reconcile behavior against declarations

Compare the Phase 1 evidence table against:

- Play: Data Safety declarations, permission declarations, target API level, ads
  declaration, content rating answers.
- Apple: App Privacy labels, ATT usage, purpose strings, age rating answers,
  export compliance.
- Both: store listing copy and screenshots vs. actual functionality; privacy policy
  URL reachability; account-deletion path.

Work through
[`references/play_readiness_checklist.md`](references/play_readiness_checklist.md)
and
[`references/appstore_readiness_checklist.md`](references/appstore_readiness_checklist.md).

Each mismatch becomes a candidate finding. Apply the grading rubric and the hard
gate from Mandate 2.

### Phase 4: Self-critique before reporting

Re-read every candidate finding and ask, in order:

1. Does it cite a real `file:line` or a named store surface? If not → drop to
   `ADVISORY` or move to *Not Checked*.
2. Is the policy requirement verified with a URL read this session? If not → cap at
   `IMPORTANT` and mark `[UNVERIFIED]`.
3. Is there an innocent explanation I have not excluded? Write it down. If it
   survives, the finding is `PROBABLE` at best.
4. Is this local-only processing? → drop it.
5. Am I flagging the *absence* of something I simply could not see? → *Not Checked*.

Findings that fail (1) or (3) are removed, not softened.

### Phase 5: Report

Emit the structure in
[`references/report_template.md`](references/report_template.md):

1. Header — stores, mode, date, app identifier
2. Summary counts by severity
3. Findings, `BLOCKER` first, each with evidence, verified requirement + URL, and
   remediation
4. **Not Checked** — items and the question that would resolve each
5. Remediation checklist, ordered
6. Disclaimer

**Zero findings is a valid, expected result.** Report it plainly. Never pad with
placeholder or `N/A` entries to make the report look substantive.

---

## Rejection triage mode

If the user has an actual rejection, skip Phases 1–3 and use
[`references/rejection_response_playbook.md`](references/rejection_response_playbook.md).

Ask for the verbatim rejection notice first. Do not guess at the cited policy from a
paraphrase — the exact clause the reviewer cited determines the whole response.

---

## Verification

Before delivering, confirm:

- [ ] Every `BLOCKER` has both a `file:line`/store surface **and** a policy URL read this session
- [ ] No policy section number, threshold, or deadline appears without a URL or an `[UNVERIFIED]` marker
- [ ] No URL was invented — each resolves to a page actually opened
- [ ] No claim about current Data Safety / App Privacy declarations that the user did not supply
- [ ] Local-only processing is not flagged as collection
- [ ] *Not Checked* is populated (it is almost never legitimately empty)
- [ ] Mode (`VERIFIED` / `DEGRADED`) is stated in the header
- [ ] Disclaimer present
- [ ] Empty finding sets rendered as "none identified", not padded

## False-Positive Prevention

The dominant failure of policy auditing is over-flagging. Guard specifically against:

| Trap | Why it misfires | Correct handling |
|---|---|---|
| Permission in manifest ⇒ violation | Permissions may be declared for a legitimate core feature, or inherited from a library manifest merge | Trace to a call site. Check merged manifest provenance. No call site → `ADVISORY` |
| Data touched ⇒ data collected | Collection requires transmission off-device | On-device-only → not collection. Say so explicitly |
| SDK present ⇒ SDK transmits | Many SDKs are compiled in but disabled by config or flavor | Check initialization and build variant before flagging |
| Missing deletion endpoint in code ⇒ no deletion path | The path may be a web form outside the repo | Ask. Do not flag absence you cannot observe |
| Test/sample code | Fixtures often contain permissions and dummy credentials | Exclusion globs; verify path before flagging |
| Policy recalled from training | Numbering and thresholds change | Mandate 1. Read it or mark `[UNVERIFIED]` |
| Cross-platform double-count | One Flutter call site surfaces in both manifests | Deduplicate to one finding per behavior, note both platforms |

**Calibration:** if a run produces a long list of `BLOCKER`s, that is a signal the
grading gate was not applied, not that the app is unusually bad. Re-run Phase 4.

## Troubleshooting

**A policy page moved or 404s.**
Do not substitute a remembered requirement or a third-party summary. Navigate from
the store's policy index (in the registry), and if it cannot be found, mark
`[UNVERIFIED]` and flag the stale registry entry for update.

**The user cannot supply current store declarations.**
Proceed. Everything declaration-dependent goes to *Not Checked* with the exact
question. Do not infer declarations from the code.

**Source tree is partial (no iOS side, submodule missing).**
State the gap in the header, scope the audit to what is present, and put the missing
platform in *Not Checked*. Do not extrapolate across platforms.

**Findings contradict `android-play-policy-insights` output.**
Prefer its verdict on Play-specific static analysis — it has a purpose-built scanner
and a critic pass. Reconcile explicitly rather than presenting both.

**Third-party SDK behavior is undocumented.**
Flag as `ADVISORY` with the question to put to the vendor. Never assert what a
closed-source SDK transmits.

## Related Skills

- [`android-play-policy-insights`](../android-play-policy-insights/) — **Run this
  first for Android.** Google's own deep Play auditor: scripted static analysis,
  permission→data-source mapping, worker/critic pipeline. Requires Python and a
  writable scratch directory. This skill covers what it does not: the App Store,
  non-code submission surfaces, live-policy verification, and rejection triage.
- [`android-release-pipeline`](../android-release-pipeline/) — release mechanics
  once policy readiness passes.
- [`android-quarterly-maintenance`](../android-quarterly-maintenance/) — recurring
  cadence; wire this audit in before each release train.
- `domain-software-engineering/analysis/security/` — code security, distinct from
  store policy.
- `domain-legal/` — if a matter becomes genuinely legal. This skill routes there
  rather than opining.
