---
name: android-r8-analyzer
description: Analyzes Android build files and R8 keep rules to identify redundancies,
  broad package-wide rules, and rules that subsume library consumer keep rules. Use
  when developers want to optimize their app's size, remove redundant or overly broad
  keep rules, or troubleshoot Proguard configurations.
license: Complete terms in LICENSE.txt
metadata:
  author: Google LLC
  last-updated: '2026-07-18'
  upstream: https://github.com/android/skills
  upstream-path: performance/r8-analyzer
  upstream-commit: 23d9eae21a4bfe0209e5b678f0ebe931e3c7dff4
  upstream-synced: '2026-08-02'
  keywords:
  - R8
  - proguard
  - keep rules
  - app size
  - optimization
---

## Step 1. Setup and configuration check

- Inspect `build.gradle`, `build.gradle.kts`, and `gradle.properties`.
- Use [references/CONFIGURATION.md](references/CONFIGURATION.md) to identify missing optimizations.
- **AGP** : If \< 9.0, suggest migration to 9.0 for [build time improvement
  performance](references/android/topic/performance/app-optimization/enable-app-optimization.md)
- **Full Mode** : Verify `android.enableR8.fullMode=false` is removed from gradle.properties.

## Step 2. Analysis path selection

- Inspect `build.gradle`, `build.gradle.kts`, and `gradle.properties` and
  `libs.versions.toml` to get the R8 version

- **If R8 \>= 9.3.7-dev** : Proceed to **Path A (Quantitative)**.

- **If R8 \< 9.3.7-dev** : Proceed to **Path B (Heuristic)**.

### Path A: Quantitative data generation (R8 \>= 9.3.7-dev)

- **Check requirements** : Python and `protobuf` package are mandatory.
- **Generate and analyze** : You MUST run the shell commands described in [references/CONFIGURATION-ANALYZER.md](references/CONFIGURATION-ANALYZER.md) to generate the proto file using R8 configuration analyzer, convert it to json and analyze the result.
- **Report** : Rely entirely on the generated file `analysis.txt` for scores and rule impact metrics. Proceed to Step 3.

### Path B: Heuristic evaluation and recommendation (R8 \< 9.3.7-dev)

*(Use ONLY if quantitative data generation is not possible)*

- **Manual evaluation** : Inspect `proguard-rules.pro`.
- **Library check** : Compare rules against [references/REDUNDANT-RULES.md](references/REDUNDANT-RULES.md). Suggest **Remove** for bundled rules.
- **Custom rule check** : Use [references/KEEP-RULES-IMPACT-HIERARCHY.md](references/KEEP-RULES-IMPACT-HIERARCHY.md) and [references/REFLECTION-GUIDE.md](references/REFLECTION-GUIDE.md) to prioritize and evaluate. Suggest **Refine** for broad rules (for example, package-wide).
- **Validation** : Suggest Macrobenchmark tests using [UI Automator](references/android/training/testing/other-components/ui-automator.md) for any proposed changes. Proceed to Step 3.

## Step 3. Report generation

- **Format** : Follow [references/REPORT_FORMAT.md](references/REPORT_FORMAT.md) strictly.
- **Input**: Extract metrics (Scores, Impacts, Example Classes) directly from generated file analysis.txt if using Path A, or from manual findings if using Path B.
- **Output** : Output ONLY the raw Markdown report in the chat. Do NOT output conversational filler (for example, "Here is your report..."). Do NOT provide recommendations, next steps, or any other text outside of the sections defined in [references/REPORT_FORMAT.md](references/REPORT_FORMAT.md) Do NOT mention the path used for analysis of the configuration

## Constraints

- **Strict output limit**: The final output MUST strictly be the Markdown report and nothing else.
- **No code changes**: Research and suggest only; Do not modify files.
- **No redundancy**: Do not explain R8 benefits or reference skill internal files in the report.
- **Focus**: Omit sections (for example, Subsumed Rules, Configuration) if no issues or items are found.

---

<!-- BEGIN LOCAL WRAPPER -->
<!-- Not from upstream. Source: local-wrapper.md. Re-applied on every sync;
     edit that file, never this block. -->

## When NOT to Use This Skill

Do NOT use this skill when:

- **Minification is disabled** (`isMinifyEnabled = false` in the relevant build type).
  There are no effective keep rules to analyze; enable R8 first, which is its own
  piece of work.
- **You want the changes applied.** The Constraints above are explicit: research and
  suggest only, no file modification. Use the report as input to a separate change.
- **You are debugging a specific obfuscation-related crash.** That runs backward from
  a stack trace, not forward from the rule set — use
  [`android-crash-triage`](../android-crash-triage/).
- **You need general app-size reduction.** Keep rules are one input among many
  (resources, assets, native libs, ABI splits). Do not present a keep-rule report as
  a size strategy.
- **The build does not currently produce a release variant.** Path A needs a real R8
  run; without one, findings are unverifiable heuristics.

## Verification

This skill produces a report, not a change. Verify the **report** before acting, and
the **build** after acting on it.

Before delivering the report:

- [ ] Every rule cited exists at a real path in an actual ProGuard/R8 config — no
      rule reconstructed from memory or inferred from a library's reputation
- [ ] Removal suggestions for library rules are backed by
      `references/REDUNDANT-RULES.md`, not by assumption that a library "probably"
      ships consumer rules
- [ ] Rules kept for reflection, serialization, JNI, or DI are not proposed for
      removal without evidence at a call site
- [ ] Path A metrics come from the generated `analysis.txt`, never estimated
- [ ] Output is only the report, per Constraints — no conversational preamble

After the developer applies changes:

- [ ] Release variant builds and R8 completes without new warnings
- [ ] App launches, and reflection-dependent paths still work — serialization,
      DI graph construction, dynamic class loading
- [ ] Measure APK/AAB size before and after; an unmeasured "optimization" is a guess
- [ ] Run the Macrobenchmark/UI Automator validation the skill recommends
- [ ] Crash-free rate is watched on the next staged rollout — keep-rule regressions
      typically surface in production, not in CI

## Related Skills

- [`android-agp-9-upgrade`](../android-agp-9-upgrade/) — Step 1 suggests AGP 9 for
  its optimizations. Do the AGP migration **first**; it changes which rules matter.
- [`android-crash-triage`](../android-crash-triage/) — for crashes traced to
  over-aggressive shrinking, and for mapping-file/symbolication work.
- [`android-release-pipeline`](../android-release-pipeline/) — retain mapping files
  per release; staged rollout is where these regressions appear.
- [`android-testing-patterns`](../android-testing-patterns/) — instrumented tests on
  a minified variant are the only reliable pre-release check.
