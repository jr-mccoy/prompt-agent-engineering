---
title: "Diagnose Why a Vibe-Coded Android App Has Hit a Wall"
category: software-engineering/vibe-coding-rescue/android
description: "Classify the failure mode of an AI-generated Android app into a fixed Android-specific taxonomy (12 modes covering manifest drift, lifecycle drift, deprecated-API patchwork, Compose state sprawl, Hilt scope confusion, coroutine scope leak, hand-rolled auth, WebView/Intent abuse, dependency cliff, no-tests, scope creep, context rot) and produce one specific rescue action. Refuses generic 'add tests' advice."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-05
  - RT-07
  - QA-01
difficulty: intermediate
tags:
  - vibe-coding
  - android
  - rescue
  - diagnosis
  - kotlin
  - compose
  - hilt
  - gradle
updated: "2026-05-17"
related_prompts:
  - domain-software-engineering/vibe-coding-rescue/viberescue_wall_diagnosis.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_codebase_audit.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_security_privacy_audit.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_fix_prioritization.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_rules_file.md
  - domain-software-engineering/mobile/android/analysis/android_codebase_health_assessment.md
---

# Diagnose Why a Vibe-Coded Android App Has Hit a Wall

**Purpose:** "Vibe-coded" Android apps — built in long, improvisational sessions with an AI coding assistant — hit walls in characteristic, Android-specific ways. The general failure modes from `viberescue_wall_diagnosis.md` apply, but Android adds twelve specialized modes that need their own diagnosis (manifest drift, lifecycle drift, deprecated-API patchwork, Compose state sprawl, Hilt scope confusion, coroutine scope leak, hand-rolled auth, WebView/Intent abuse, dependency cliff, no-tests, scope creep, context rot). This prompt classifies the wall into exactly one primary mode and produces the rescue action that fits.

**When to use:**
- An Android app built largely with AI assistance has stopped making reliable forward progress.
- Builds intermittently break across Android Studio / Gradle / dependency upgrades.
- Every new screen breaks state on an existing one; rotation or process death loses state in surprising places.
- Compose recomposes are happening "too often" or in surprising places; you can't predict what re-renders.
- The AI keeps adding new ViewModels / repositories / Hilt modules that overlap with existing ones.
- Suspect security issues you can't articulate — `exported` flags, deeplinks, WebView, intent handling.

**Don't use when:** The app builds, runs, has tests, and you can fully explain its architecture. Use a focused review prompt (`android_codebase_health_assessment.md`) instead.

**Audience:** The engineer or builder working on the app. Output is a diagnosis + one rescue action, actionable today.

---

## Inputs Required

Ask for all of these. Refuse to diagnose without items 1, 2, 3, 5, and 7.

1. **App shape.** `minSdk`, `targetSdk`, `compileSdk`, AGP version, Gradle version, Kotlin version, primary UI toolkit (Compose / XML Views / mixed), DI framework (Hilt / Koin / manual / none), async approach (coroutines / RxJava / mixed), persistence (Room / SQLite / SharedPreferences / DataStore / mixed). Approximate module count and source-file count.
2. **The three most recent "going wrong" sessions.** For each: what you were trying to build, what the AI generated, what broke (build, runtime, behavior, lifecycle, state, networking), what you did to unstick. Concrete.
3. **The last 5–10 features shipped successfully.** What works today and whether you could explain each one — including its data flow, lifecycle, and threading — to a new Android engineer.
4. **File map.** List the 5 files the AI edits most often. List any files you haven't read in weeks but the AI keeps editing.
5. **Your mental model.** In ≤5 sentences: what the app does, its main screens, where data flows, how state survives rotation / process death. Vague is OK — vagueness is itself a signal.
6. **AndroidManifest snapshot.** Number of Activities, Services, Receivers, Providers. Are all `android:exported` flags explicit? Any intent filters with deeplinks?
7. **Stakes.** Hobby / internal prototype / production app with users / app in Play Store / regulated context. Changes the rescue aggressiveness.
8. **Test posture.** Unit tests yes/no, instrumentation tests yes/no, Compose UI tests yes/no, manual QA only, none.

---

## Instructions

### Step 1 — Classify into exactly one primary wall mode

Use only this taxonomy. If two plausibly fit, pick the one earliest in the causal chain.

| # | Wall mode | Signs | Core rescue |
|---|-----------|-------|-------------|
| A1 | **Manifest drift** | Components declared in code but not in `AndroidManifest.xml`, or vice versa. Missing `android:exported`. Stale or duplicated intent filters. Permissions requested but never granted at runtime; or granted but unused. | Manifest audit pass — every component reconciled, every `exported` made explicit, every permission justified. |
| A2 | **Lifecycle drift** | State lost on rotation or process death. Listeners registered in `onCreate` and never unregistered. Coroutines launched from Activity scope but never cancelled. `LiveData` / `Flow` collected from the wrong lifecycle owner. | Lifecycle-owner audit. Migrate to `viewModelScope` / `lifecycleScope` / `repeatOnLifecycle` per the canonical pattern. |
| A3 | **Deprecated-API patchwork** | Mix of `AsyncTask` + coroutines, `startActivityForResult` + Activity Result API, runtime permissions via old `requestPermissions` + ActivityResultContracts, `findViewById` + ViewBinding + Compose. No consistent direction. | Pick one direction per concern, migrate inconsistent files, document in the rules file. |
| A4 | **Compose state sprawl** | `remember { mutableStateOf(...) }` scattered across composables that should share state. ViewModels exposing both `LiveData` and `StateFlow`. Hoisted state mixed with internal state inconsistently. Recompositions on every keystroke. | State-hoisting audit. Establish single source of truth per screen; document in rules file. |
| A5 | **Hilt scope confusion** | `@Singleton` bound things that should be `@ViewModelScoped`. Same dependency provided in multiple modules. `@Inject` on classes whose lifecycle Hilt can't manage. Test doubles can't override prod bindings. | DI graph audit: redraw the scope boundaries, consolidate modules, fix overrides. |
| A6 | **Coroutine scope leak** | Coroutines launched from `GlobalScope` or `CoroutineScope(Dispatchers.IO)` constructed ad-hoc. Jobs not cancelled on screen destruction. Flows collected without `repeatOnLifecycle`. `runBlocking` in UI code. | Scope discipline reset. Define which scope owns what; migrate violators. |
| A7 | **Hand-rolled auth / security** | Auth tokens stored in SharedPreferences (not EncryptedSharedPreferences). Custom JWT / signature checks. Biometric prompts without `CryptoObject`. API keys in `BuildConfig`, source, or `strings.xml`. | Run `android_viberescue_security_privacy_audit.md` immediately; do not continue feature work until critical findings are addressed. |
| A8 | **WebView / Intent abuse** | WebView with `setJavaScriptEnabled(true)` and `addJavascriptInterface` to arbitrary objects, plus file:// access. Implicit intents to ACTION_VIEW with user-controlled URIs. Deeplinks that accept any host. PendingIntents not flagged `IMMUTABLE`. | Constrain WebView (allow-list, no JS interface, no file access). Audit every deeplink. Set `FLAG_IMMUTABLE` on all PendingIntents. |
| A9 | **Dependency cliff** | AGP / Gradle / Kotlin / Compose Compiler / Hilt versions interlocked but uncoordinated. `kapt` vs `ksp` mixed. SDK version mismatches across modules. BOMs ignored where they exist (Compose BOM, Firebase BOM). | Version-catalog migration (libs.versions.toml). Adopt BOMs. Pin one source of truth per family. |
| A10 | **No invariants / no tests** | Tests absent or only assert what the AI just generated. Lifecycle, threading, and state-survival behaviors have zero coverage. | Add invariant tests for rotation, process death, navigation state, lifecycle cleanup — not unit-test sprawl. |
| A11 | **Scope creep without deletion** | Multiple repositories for the same data. Multiple ViewModels per screen. Dead Activities / Fragments / Services still in the manifest. Three ways to navigate between two screens. | Subtraction pass: delete dead components, consolidate duplicates, prune manifest. |
| A12 | **Context rot** | Every AI session re-explains the project from scratch. AI keeps re-introducing patterns you already rejected. No project rules file or it's stale. | Install project memory: run `android_viberescue_rules_file.md` after this diagnosis. |

Do not invent new modes. If none fit, state so and ask what's actually happening.

### Step 2 — Justify the classification with the user's own evidence

Quote or paraphrase from inputs 2, 3, 4, 5, and 6. Two to four sentences. If two modes plausibly fit, name the secondary candidate and why it was ranked second.

### Step 3 — Check for compounding cascades

Some walls stack on Android. Call out which of these apply:

- **A1 + A8:** Manifest drift + WebView/Intent abuse = unknown attack surface. Treat as security-critical even if the user didn't flag security concerns.
- **A2 + A6:** Lifecycle drift + coroutine scope leak = the app is leaking memory and may crash on rotation. Often co-occur.
- **A4 + A5:** Compose state sprawl + Hilt scope confusion = state lives in the wrong scope and Hilt can't help. Recompositions will keep getting worse.
- **A3 + A9:** Deprecated-API patchwork + dependency cliff = next AGP upgrade will likely break the build. Schedule a maintenance window.
- **A7 + A1:** Hand-rolled auth + manifest drift = exported components may bypass auth. Critical.
- **A11 + A12:** Scope creep + context rot = the AI keeps adding because it doesn't know what already exists. Rules file is necessary but not sufficient — also need subtraction.

Cascades change the rescue. Treat as primary findings, not footnotes.

### Step 4 — Deliver the rescue action

The action must be:

- **Specific.** Named file or directory, named tool, named prompt, named test. Not "audit the manifest" but "open AndroidManifest.xml, add `android:exported` to every Activity / Service / Receiver, reconcile with declarations in code."
- **Small for the first step.** Under 90 minutes for step 1.
- **Tied to the classified mode.** A2 (lifecycle drift) gets a lifecycle-owner audit; it doesn't get "be more careful."
- **Aware of stakes** (input 7). Production apps in Play Store cannot ship "let's try a refactor and see."
- **Aware of test posture** (input 8). If there are no tests, the rescue includes a minimum-viable invariant test for the change.

If primary mode is A7 (hand-rolled auth/security), the action is to run `android_viberescue_security_privacy_audit.md` before any further feature work.

### Step 5 — Name the next prompt in the chain

Based on the classified mode, point to exactly one follow-up prompt:

- A1, A2, A3, A4, A5, A6, A11 → `android_viberescue_codebase_audit.md` next, then `android_viberescue_fix_prioritization.md`.
- A7, A8 → `android_viberescue_security_privacy_audit.md` next, then `android_viberescue_fix_prioritization.md`.
- A9 → `android_viberescue_codebase_audit.md` scoped to dependencies and build files.
- A10 → start by writing one rotation-survival test and one process-death test before anything else.
- A12 → `android_viberescue_rules_file.md` after running the codebase audit (need evidence first).

### Step 6 — One-week reality check

State one specific observable state the user should see within a week if the rescue is landing. Examples:
- A1: "AndroidManifest.xml has explicit `android:exported` on 100% of components; build passes lint."
- A2: "Rotating the app on every primary screen preserves state; Logcat shows no `IllegalStateException` from collecting after lifecycle stop."
- A6: "No `GlobalScope` references in the codebase; `./gradlew detekt` (or equivalent) reports zero coroutine-scope violations."

If that state isn't reached, the diagnosis was probably wrong — re-run this prompt.

### Step 7 — Call out what the rescue does NOT fix

Be explicit: this rescue doesn't fix [other modes if present]. If there's a secondary mode, name it and the follow-up rescue. Do not attempt multi-rescue in one run.

### Step 8 — Stakes and handoff consideration

For Play-Store production apps (input 7), explicitly answer: is in-place rescue the right posture, or should this be briefed to a different engineer? Point to `viberescue_engineer_handoff_briefing.md` if takeover is warranted.

### Step 9 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Pick exactly one primary wall mode from A1–A12.
- Justify with the user's own evidence (quote or paraphrase from inputs).
- Check all six cascade pairs.
- Deliver one specific rescue action with named files / tools / prompts.
- Name the next prompt in the chain.
- State an observable one-week reality check.
- Call out what the rescue does NOT fix.

### Must Not
- Invent new modes outside A1–A12.
- Give generic advice ("add tests," "refactor," "be more careful with prompts," "follow Android guidelines").
- Pile multiple rescues into one run.
- Shame the vibe-coding approach.
- Recommend a full rewrite unless mode is A4+A5 cascade at high severity AND stakes are still prototype-level.
- Claim the mental model is fine based on the AI's own retelling.

---

## False-Positive Prevention (MUST follow)

DON'T:
- Default to A10 (no tests) because tests are absent. Many A1, A2, A4, or A5 apps will grow correct tests naturally once their underlying mode is fixed; tests without that prerequisite produce brittle, AI-shaped tests.
- Classify as A9 (dependency cliff) on the existence of a Gradle warning. Cliffs are version interlock failures, not deprecation warnings.
- Flag A8 (WebView/Intent abuse) without a WebView or implicit intent actually present. Confirm before classifying.
- Confuse A4 (Compose state sprawl) with simple Compose unfamiliarity. Sprawl means state is duplicated or in the wrong place, not that the user finds Compose confusing.
- Miss A12 (context rot) when it underlies an apparent A11. If the AI keeps adding because it doesn't know what exists, that's A12; subtraction alone won't help.

DO:
- When the user's mental model (input 5) skips lifecycle or threading, lean toward A2 or A6.
- When inputs 2 and 3 show the AI re-introducing patterns the user rejected, lean toward A12.
- When manifest snapshot (input 6) has inconsistent or missing `exported` flags, A1 is present — even if it's not primary.
- When stakes are Play-Store production (input 7) and no security audit has been run, run the security audit (`android_viberescue_security_privacy_audit.md`) regardless of primary mode.
- Acknowledge multi-mode reality. Most vibe-coded apps have 2–4 modes active; the diagnosis names the primary and orders the rest.

---

## Dual-Failure Prevention (QA-20)

HARMFUL failure: Diagnosis is confident but wrong; user follows the rescue for a week, makes things worse, concludes the app needs a rewrite when it didn't.

UNHELPFUL failure: Diagnosis hedges across five modes and produces no concrete first step.

Quality check: A senior Android engineer who knew this codebase could read the diagnosis, agree with the primary classification, and expect the one-week reality check to fire.

---

## Output Format

```markdown
# Android Vibe-Coding Wall Diagnosis — [App name]

## Primary Mode
**Mode:** [A# + name]

**Justification:** [Two to four sentences grounded in the user's inputs. Quote or paraphrase.]

**Secondary candidate:** [A# + name + one-line reason, or "none"]

## Cascade Check
- A1 + A8: [present? impact]
- A2 + A6: [present? impact]
- A4 + A5: [present? impact]
- A3 + A9: [present? impact]
- A7 + A1: [present? impact]
- A11 + A12: [present? impact]

## Rescue Action
[Specific first step under 90 minutes. Named files / tools / prompts / tests.]

## Next Prompt in the Chain
[`android_viberescue_*.md` — which and why]

## One-Week Reality Check
[Specific observable state. If not reached by [date], re-run this prompt.]

## What This Rescue Does Not Fix
- [Other modes present that this rescue ignores, with the follow-up rescue pointer.]

## Stakes & Handoff
- Current stakes: [from input 7]
- In-place rescue appropriate: [yes / consider handoff to engineer with deeper Android expertise]
- If handoff: [pointer + why]
```

---

## Verification

- [ ] Exactly one primary mode chosen from A1–A12.
- [ ] Justification cites user's own evidence.
- [ ] All six cascade pairs checked.
- [ ] Rescue action is specific, small, tied to the mode, aware of stakes and tests.
- [ ] Next prompt named.
- [ ] One-week reality check is observable.
- [ ] What-this-doesn't-fix section exists.
- [ ] No generic "add tests / refactor / be careful" advice.

---

## Techniques Used

- **ST-01 (Clear Objective):** Output is a single-mode diagnosis + one rescue action + next prompt, not a menu of advice.
- **ST-02 (Structured Sequential Instructions):** Nine steps drive classification → justification → cascade check → rescue → next prompt → reality check → unfixed → stakes → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids generic advice and multi-rescue.
- **DS-01 (Framework Application):** Twelve-mode Android-specific taxonomy; disallowing invention keeps it load-bearing.
- **RT-05 (Evidence-Based Reasoning):** Justification step requires citing user's inputs, not pattern-matching to common Android advice.
- **RT-07 (Cascade Effect Analysis):** Six named cascade pairs catch compounding failures that single-mode diagnosis misses.
- **QA-01 (Self-Verification):** Verification checklist and dual-failure-prevention block prevent confident-but-wrong diagnoses.
