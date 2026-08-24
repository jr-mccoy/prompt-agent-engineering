---
title: "Android Performance Budget & NFR Plan"
category: mobile-development
description: "Set quantified non-functional requirements and performance budgets at planning time — startup, jank, size, memory, network, battery, crash-free and ANR SLOs — so an Android app is built to measurable targets and enforced in CI rather than optimized reactively."
techniques:
  - ST-01
  - ST-03
  - RT-02
  - DT-05
  - QA-08
  - CM-02
difficulty: advanced
tags:
  - android
  - mobile-development
  - performance
  - macrobenchmark
  - baseline-profiles
  - android-vitals
  - nfr
  - slo
updated: "2026-06-06"
related_prompts:
  - ../maintenance/android_reliability_slo_error_budget_review.md
  - ../improvement/android_startup_optimization.md
  - ../improvement/android_baseline_profiles_optimization.md
  - ../analysis/android_performance_audit.md
---

# Android Performance Budget & NFR Plan

**Objective:** Produce a quantified non-functional requirements (NFR) and performance budget specification for an Android app *before implementation begins*, so that startup time, frame rendering, app size, memory, network, battery, crash-free, and ANR targets are explicit numbers tied to a measurement method and a CI/runtime enforcement mechanism — and to define which budgets apply to which device tier, plus how these budgets feed the live app's reliability SLO / error-budget review.

**When to Use:** Use this prompt at planning time for a new app, a major rewrite, or before a performance-sensitive feature initiative. Use it when "the app feels slow" keeps surfacing reactively, when a release was rejected or down-ranked by Play's Android vitals "bad behavior" thresholds, or when leadership needs a defensible, numeric quality bar. Do **not** use it as a profiling/optimization runbook — that is the `improvement/` and `analysis/` prompts' job. This sets the targets they later enforce.

**Sequence Map:** Use after architecture and tech-stack selection; use before implementation. The budgets defined here become the acceptance gates for `improvement/android_startup_optimization.md` and `improvement/android_baseline_profiles_optimization.md`, the comparison baseline for `analysis/android_performance_audit.md`, and the planning input to `maintenance/android_reliability_slo_error_budget_review.md`.

**Important context:** A performance budget is a *contract*, not an aspiration. Every line item needs three things or it is worthless: a concrete number, a measurement method that produces that number repeatably, and an enforcement point that fails a build or flags a release when the number regresses. Budgets that live only in a doc rot within one sprint. The discipline here is to wire each budget into Macrobenchmark + CI, APK/AAB size checks, LeakCanary/StrictMode in debug, and Play Console Android vitals in production — so a regression is caught by a machine, not by a user review. Targets must also be tiered: a flagship at 120 Hz and a low-RAM Go-class device cannot share one frame budget.

---

## Context Gathering

Ask these before drafting any numbers. Pace them — do not dump all at once.

1. **App profile & stakes:**
   - "What kind of app is this (consumer social, productivity, fintech, media/streaming, games-adjacent)? What is the single most latency-sensitive user moment?"
   - "Is this greenfield, or are we ratcheting budgets onto an existing app with known baselines?"
   - "Are there contractual/regulatory uptime or responsiveness commitments?"

2. **Device & audience reality:**
   - "What is the device-tier distribution of your real users (low-end / mid / flagship), by region if relevant? Pull from Play Console device catalog or analytics if it exists."
   - "What is your `minSdk` / `targetSdk`? What refresh rates must you support (60 Hz baseline, 90/120 Hz high-refresh)?"
   - "Is there a hard install-size sensitivity (emerging-market data costs, Wear/Auto, instant app)?"

3. **Current measurement maturity:**
   - "Do you already have Macrobenchmark, Baseline Profiles, a size check in CI, LeakCanary, and Play Console vitals access? Which are missing?"
   - "Do you have a Firebase Performance / custom trace pipeline for field TTID/TTFD, or only lab numbers?"

4. **Tolerance & ownership:**
   - "What crash-free and ANR-free level is 'good enough' vs 'embarrassing' for this app? Who owns the error budget when it is spent?"

---

## Instructions

### Phase 1: Establish device tiers and refresh-rate frame budgets

Define the device tiers the budget applies to. Map each user-facing budget to the tiers it governs. Frame budgets are physics, not opinion — they derive from refresh rate.

| Tier | Definition (planning proxy) | Frame budget governs | Notes |
|------|-----------------------------|----------------------|-------|
| **Low-end** | <= 3 GB RAM, older/efficiency SoC, often 60 Hz, Android Go-adjacent | Startup, jank, memory ceiling, size | Hardest constraints; many budgets are *tier-specific* here |
| **Mid** | 4–6 GB RAM, mainstream SoC, 60–90 Hz | All budgets at default targets | The "must pass" tier for vitals |
| **Flagship** | >= 8 GB RAM, high-refresh 90/120 Hz | Tighter frame budget, higher memory headroom | 120 Hz exposes jank the 60 Hz tier hides |

Frame budget by refresh rate (a frame must complete in):

| Refresh rate | Per-frame budget | Implication |
|--------------|------------------|-------------|
| 60 Hz | **16.6 ms** | Classic jank threshold |
| 90 Hz | **11.1 ms** | |
| 120 Hz | **8.3 ms** | Half the work-per-frame headroom of 60 Hz |

Definitions to lock now: **janky frame** = a frame exceeding its refresh-rate budget; **frozen frame** = a frame taking **> 700 ms** (Android vitals definition); **slow frame** rate is tracked alongside.

**CHECKPOINT 1 (gate):** Tiers are defined with concrete proxies, and every later budget row names which tier(s) it applies to. Do not proceed until the user confirms the tier distribution roughly matches their real audience.

---

### Phase 2: Author the NFR / performance budget table

This is the core deliverable. Each row needs a **target**, a **measurement method**, an **enforcement point**, and the **tier(s)** it applies to. Fill targets to the app's stakes; the values below are starting points, not gospel.

| # | Budget item | Target (default) | Measurement method | Enforced by | Tier |
|---|-------------|------------------|--------------------|-------------|------|
| 1 | **Cold start (TTID)** | <= 500 ms (mid); <= 800 ms (low-end); <= 350 ms (flagship). Android vitals "excessive cold start" = **>= 5 s** is the floor you must never hit | Macrobenchmark `StartupTimingMetric`, `StartupMode.COLD`; field via `reportFullyDrawn()` + Play vitals | Macrobenchmark CI run + Baseline Profiles; Play Console vitals | All (tiered) |
| 2 | **Warm start** | <= 300 ms (mid). Vitals "excessive warm start" floor = **>= 2 s** | Macrobenchmark `StartupMode.WARM` | Macrobenchmark CI | Mid/low |
| 3 | **Hot start** | <= 150 ms. Vitals "excessive hot start" floor = **>= 1.5 s** | Macrobenchmark `StartupMode.HOT` | Macrobenchmark CI | Mid/low |
| 4 | **TTID vs TTFD** | TTFD <= TTID + 1 s; TTFD reported via `reportFullyDrawn()` | Macrobenchmark + field trace | Macrobenchmark + Firebase Perf | All |
| 5 | **Frame rendering / jank** | Janky-frame rate <= **5%** of frames per critical screen | Macrobenchmark `FrameTimingMetric` (P50/P90/P99 frame durations) | Macrobenchmark CI + Baseline Profiles | Per-refresh-tier |
| 6 | **Frozen frames** | Frozen frames (> 700 ms) at **0** on critical paths; Play vitals frozen-frame "bad behavior" floor | `FrameTimingMetric` overruns; Play vitals | Macrobenchmark + Play vitals | All |
| 7 | **Scroll performance** | P99 frame within refresh budget during fling on primary list; no dropped-frame cluster > 2 frames | Macrobenchmark scroll test (`UiDevice` fling) + `FrameTimingMetric` | Macrobenchmark CI | Per-refresh-tier |
| 8 | **Install / download size** | AAB-delivered install <= **15 MB** (low-end target), per-ABI APK <= **target**; absolute regression gate **+250 KB per PR** | `bundletool` size report / APK Analyzer; per-ABI split sizes | CI size-diff check (fail on regression) + R8/resource shrinking | All (tighter low-end) |
| 9 | **Runtime memory ceiling** | Steady-state PSS under <= **device-class %** of available; no growth trend across navigation cycles | Macrobenchmark `MemoryUsageMetric` / `MemoryCountersMetric`; Android Studio profiler | Macrobenchmark CI + StrictMode | All (tiered) |
| 10 | **Memory-leak policy** | **Zero** retained-instance leaks shipped; debug builds fail loudly | LeakCanary (debug); CI instrumentation surfacing leaks | LeakCanary + CI assertion | All |
| 11 | **Network payload** | Critical-path response <= **target KB** (gzip/br on); no N+1 request fan-out on first screen | OkHttp `EventListener` / Charles/Flipper; trace request count + bytes | Review gate + perf test | All |
| 12 | **Network latency budget** | First meaningful data within **TTID budget** on a defined network class; P95 critical call <= target ms | Field trace (Firebase Perf network traces) | Play vitals / Firebase Perf | All |
| 13 | **Battery / background work** | No wakelock > target; background work batched via WorkManager; no excessive wakeups | Battery Historian; Play vitals "excessive background work / wakeups / wake locks" | Play Console vitals + StrictMode | All |
| 14 | **Crash-free sessions (SLO)** | >= **99.5%** sessions crash-free (set per stakes; fintech may demand 99.9%) | Play Console / Crashlytics | Production SLO + error budget | All |
| 15 | **Crash-free users (SLO)** | >= **99.0%** users crash-free | Play Console / Crashlytics | Production SLO + error budget | All |
| 16 | **ANR rate (SLO)** | < **0.47%** ANR rate — Play's "bad behavior" threshold; aim materially under | Play Console Android vitals (user-perceived ANR) | Production SLO + main-thread StrictMode | All |
| 17 | **Crash rate (vitals)** | < **1.09%** user-perceived crash rate (Play "bad behavior" threshold); aim well under | Play Console Android vitals | Production SLO | All |

> Play's two "bad behavior" thresholds (crash rate **1.09%**, ANR rate **0.47%**) are *eligibility floors* — exceed them and discoverability/visibility is penalized. Your internal SLO targets must sit comfortably below these, never at them.

**CHECKPOINT 2 (gate):** Every row has a non-empty number, a method, and an enforcement point. Reject any row that says "fast", "small", or "low" without a figure. Do not proceed to enforcement design with placeholder targets.

---

### Phase 3: Wire each budget to an enforcement mechanism

A budget is only real once a machine can fail on it. Map every category to its enforcement tool and where it runs.

| Enforcement mechanism | Budgets it guards | Where it runs |
|-----------------------|-------------------|---------------|
| **Macrobenchmark** (`androidx.benchmark.macro`) | Startup (cold/warm/hot), TTID/TTFD, frame timing, scroll, memory | Instrumented test on a managed/physical device in CI |
| **Baseline Profiles** (+ optional Startup Profiles) | Startup, jank on first-run/post-update paths | Generated in CI, shipped in AAB; verified via Macrobenchmark `CompilationMode.Partition`/`None` comparison |
| **CI size-diff check** | Install/download size, per-ABI splits | PR job comparing AAB/APK against base branch; fail on regression > threshold |
| **R8 / resource & code shrinking** | Size, runtime cost | Release build config (`isMinifyEnabled`, `isShrinkResources`) |
| **LeakCanary** | Leak policy | Debug builds; surfaced in instrumentation/CI |
| **StrictMode** | Main-thread I/O/disk (ANR/jank precursors), background work | Debug builds; `penaltyDeath`/`penaltyLog` in dev |
| **Play Console Android vitals** | Crash-free, ANR, frozen/slow frames, excessive wakeups/wakelocks, excessive startup, battery | Production; the source of truth for field SLOs |
| **Firebase Performance / custom traces** | Field TTID/TTFD, network latency | Production sampling |

Provide a CI snippet skeleton (the user adapts versions via their version catalog):

```kotlin
// Macrobenchmark — startup budget assertion (module: :macrobenchmark)
@Test
fun coldStartupMeetsBudget() = benchmarkRule.measureRepeated(
    packageName = TARGET_PACKAGE,
    metrics = listOf(StartupTimingMetric()),
    iterations = 10,
    startupMode = StartupMode.COLD,
    compilationMode = CompilationMode.Partial() // with Baseline Profile
) {
    pressHome()
    startActivityAndWait()
}
// CI parses the timeToInitialDisplayMs P50 from the benchmark JSON
// and fails the job if it exceeds the tier budget (e.g. 500 ms mid-tier).
```

```kotlin
// Release build: enforce size + size-affecting shrinking
android {
    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            // CI step runs `bundletool get-size total` on the AAB and
            // diffs against the base branch; fails on > 250 KB regression.
        }
    }
}
```

```kotlin
// Debug: catch main-thread violations and leaks before they become ANRs/OOMs
StrictMode.setThreadPolicy(
    StrictMode.ThreadPolicy.Builder()
        .detectDiskReads().detectDiskWrites().detectNetwork()
        .penaltyLog().build()
)
// LeakCanary auto-installs in debug via the no-op/real artifact split.
```

**CHECKPOINT 3 (gate):** Each budget row in Phase 2 maps to at least one enforcement mechanism here. Any budget with no enforcement is flagged as "aspirational only" and must either get a mechanism or be dropped.

---

### Phase 4: Link budgets to the live SLO / error-budget review

The planning-time budget and the running app's SLO are the same numbers at two lifecycle stages. Hand off explicitly.

- Promote rows 14–17 (crash-free sessions, crash-free users, ANR, crash rate) to **production SLOs** with an explicit **error budget** (e.g., 99.5% crash-free sessions => 0.5% monthly error budget).
- Define the **error-budget policy**: what happens when the budget is spent (feature freeze, reliability sprint, rollback criteria) — and hand this to `maintenance/android_reliability_slo_error_budget_review.md`.
- Set a **review cadence** (e.g., weekly vitals check, monthly SLO review) and the **owner** of each SLO.
- Define **regression alerting**: which dashboard, what threshold, who is paged.

**CHECKPOINT 4 (gate):** Production SLOs, an error-budget number, an owner, and a review cadence exist and are routed to the maintenance review prompt.

---

## Expected Output

1. **Device-tier definitions** with concrete proxies and the user's real audience distribution noted.
2. **Frame-budget table** by refresh rate (16.6 / 11.1 / 8.3 ms) with janky/frozen-frame definitions.
3. **The NFR / performance budget table** — every row with target + measurement method + enforcement point + applicable tier(s), covering startup (cold/warm/hot, TTID/TTFD), frame/jank, scroll, size, memory + leak policy, network payload/latency, battery/background, and the crash-free / ANR / crash-rate SLOs including Play's bad-behavior floors.
4. **Enforcement map** tying each budget to Macrobenchmark, Baseline Profiles, CI size checks, R8, LeakCanary, StrictMode, and Play vitals / Firebase Perf, with CI snippet skeletons.
5. **SLO & error-budget handoff** — production SLOs, error-budget number, policy, cadence, owner, and routing to the maintenance review.
6. **Open risks / assumptions** — anything that could not be quantified yet and how it will be resolved.

---

## CRITICAL: Verification Requirements

- [ ] Every budget row has a concrete number (no "fast", "small", "low" without a figure)
- [ ] Every budget row names a measurement method that produces that number repeatably
- [ ] Every budget row names an enforcement point (CI gate, runtime tool, or Play vitals)
- [ ] Frame budgets are derived from refresh rate (16.6 ms @60 Hz, 11.1 ms @90 Hz, 8.3 ms @120 Hz) — not invented
- [ ] Frozen frame = > 700 ms and janky frame = over-budget are stated as definitions
- [ ] Startup budgets distinguish cold / warm / hot and reference TTID vs TTFD
- [ ] Size budget specifies AAB-delivered install size and a per-PR regression threshold
- [ ] Memory budget includes both a steady-state ceiling and a zero-leak policy
- [ ] Crash-free and ANR SLOs sit *below* Play's bad-behavior floors (1.09% crash, 0.47% ANR), not at them
- [ ] At least one budget is explicitly tier-specific (low-end differs from flagship)
- [ ] Production SLOs, an error-budget number, an owner, and a cadence are defined and routed to the maintenance review

## False-Positive Prevention

- ❌ Do NOT pin exact library/Gradle/AGP version numbers in budget targets — they rot; reference tools by name and let the version catalog own versions
- ✅ DO express budgets as numbers tied to a measurement method that survives version bumps
- ❌ Do NOT set a single global frame budget when the app supports 90/120 Hz devices
- ✅ DO tier frame and startup budgets by refresh rate and device class
- ❌ Do NOT treat Play's 1.09% crash / 0.47% ANR thresholds as targets — they are the failure floor
- ✅ DO set internal SLOs comfortably below those floors with an explicit error budget
- ❌ Do NOT accept a budget with no enforcement mechanism ("we'll watch it manually")
- ✅ DO wire each budget to Macrobenchmark, a CI check, a debug-time tool, or Play vitals
- ❌ Do NOT measure startup only in the lab and call it done
- ✅ DO pair lab Macrobenchmark numbers with field TTID/TTFD from `reportFullyDrawn()` + vitals
- ❌ Do NOT conflate this plan with a profiling/optimization runbook
- ✅ DO hand the targets to the `improvement/` and `analysis/` prompts as their acceptance gates

## Techniques Used

- **ST-01** (Clear Objective): Singular focus on quantified NFRs and budgets at planning time
- **ST-03** (Output Format Specification): Mandated budget/enforcement tables with fixed columns
- **RT-02** (Multi-Dimensional Analysis): Budgets evaluated across target, method, enforcement, and tier
- **DT-05** (Element-by-Element Assessment Matrix): Systematic row-by-row coverage of every performance category
- **QA-08** (Gate-Based Verification): CHECKPOINT gates that block progress on placeholder or unenforced budgets
- **CM-02** (Constraint Specification): Must/must-not rules (numbers required, enforcement required, SLOs below vitals floors)

## Related Prompts

- [android_reliability_slo_error_budget_review.md](../maintenance/android_reliability_slo_error_budget_review.md) - Operate the SLOs and error budget defined here on the live app
- [android_startup_optimization.md](../improvement/android_startup_optimization.md) - Optimize against the startup budgets set here
- [android_baseline_profiles_optimization.md](../improvement/android_baseline_profiles_optimization.md) - Enforce startup/jank budgets via Baseline Profiles
- [android_performance_audit.md](../analysis/android_performance_audit.md) - Audit a running app against these budgets
