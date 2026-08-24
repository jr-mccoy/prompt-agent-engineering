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
