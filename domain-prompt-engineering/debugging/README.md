# Prompt Debugging

Prompts for diagnosing why a prompt fails: isolating reproducers, classifying symptoms, locating regressions, probing variance, and naming root causes.

## When to Use This Subdirectory

- A prompt that worked before now fails.
- Failures are intermittent and you need to know whether it's the prompt or sampling noise.
- The output looks correct but downstream consumers report errors.
- A long agent run drifts off-spec at some unknown turn.
- You need to ship a fix and the team needs to agree on what to change.

## Files

| File | One-line description |
|------|----------------------|
| `debug_minimal_repro_isolator.md` | Greedy + bisect deletion to reduce a failing (prompt, input) pair to its smallest reproducer. |
| `debug_failure_mode_taxonomy.md` | Classify a failed output into one of seven symptom classes (omission, extra, ambiguity, conflict, model deviation, hallucination, format break). |
| `debug_bisect_prompt_changes.md` | Git-bisect-style binary search across prompt revisions to find the breaker. |
| `debug_temperature_sensitivity_probe.md` | Run T = {0, 0.3, 0.7, 1.0} to classify failures as deterministic, variance-driven, temperature-cliff, or stochastic-OK. |
| `debug_input_perturbation_battery.md` | Apply 15 small input transforms (case, whitespace, length, delimiters, etc.) to surface brittleness. |
| `debug_silent_failure_detector.md` | Six-layer validator stack (syntax → type → provenance → invariants → external truth → calibration) for outputs that pass surface checks but are wrong. |
| `debug_multi_turn_drift_diagnosis.md` | Locate the earliest turn at which a behavior metric crossed threshold; classify cause across 7 drift types. |
| `debug_first_failure_cause_isolator.md` | Pick exactly one root cause from a 12-class taxonomy and emit one corrective edit. |

## Suggested Workflow

1. `debug_temperature_sensitivity_probe.md` — rule out sampling noise first.
2. `debug_minimal_repro_isolator.md` — shrink the failing case.
3. `debug_failure_mode_taxonomy.md` — classify the symptom (single output).
4. `debug_input_perturbation_battery.md` — characterize robustness.
5. `debug_silent_failure_detector.md` — when surface looks fine but downstream complains.
6. `debug_bisect_prompt_changes.md` — when "it worked before."
7. `debug_multi_turn_drift_diagnosis.md` — when failure is conversational.
8. `debug_first_failure_cause_isolator.md` — pick one root cause and ship one edit.

## Related

- `../instruction-design/` — once cause is named, fix the rule layer.
- `../model-behavior/` — root-cause when the model violates a clear rule.
- `../evaluation/` — design the eval that catches this failure class going forward.
- `../hallucination-control/` — fix L3 (provenance) failures from `debug_silent_failure_detector.md`.
