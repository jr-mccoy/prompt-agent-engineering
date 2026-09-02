# ADR-0039 — Paired task pass rate, exact McNemar, and the confirmatory repeat

## Status

Accepted. Implemented in Phase 7. Amends the Phase 7A recommendation on repeat
handling; see below.

## Context

The design needs one pre-declared primary endpoint, one test, and one rule for
collapsing repeated trials — chosen before results exist, because each is a
place where a defensible-looking choice made afterwards can change the answer.

## Decision

**Endpoint: task pass rate**, a binary derived from the frozen rubric. A task
passes when every required criterion passes, the format gate passes, the safety
gate passes and no critical fabrication penalty fired. A judge's holistic
impression can never rescue a deterministic required failure.

**Unit of analysis: the task.** Repeats aggregate to one value per
task-condition before anything statistical happens. Treating repeats as
independent observations multiplies *n* by the repeat count and shrinks every
interval — the easiest available way to manufacture significance.

**Test: exact McNemar**, with a paired percentile bootstrap CI over tasks
(10,000 resamples, seed from the plan). The interval is the reported quantity;
the p-value is secondary. Concordant pairs carry no information about the
difference and are excluded by construction, which is what makes it paired.

**Minimum meaningful effect: +10 pp**, and it is assessed on the *interval*, not
the point estimate. A point estimate above the MME with a CI straddling it has
not demonstrated the effect. +5 pp was rejected as an MME: it is not detectable
at any sample size this program can afford, and pre-registering an effect you
cannot detect is how a null result gets reported as promising.

**Secondary family:** continuous rubric score (bootstrap plus Wilcoxon), Layer A
metrics, safety pass rate, efficiency. Holm–Bonferroni across that family. The
single pre-declared primary is **not** corrected; correcting one pre-registered
endpoint is a category error. Per-class and per-domain tables are exploratory
and labelled as such.

**Wilcoxon comes from SciPy or not at all.** Ties and zero differences are
exactly where a hand-rolled implementation goes quietly wrong, and a plausible
wrong number is worse than an honest "not available".

**Efficiency claims are gated.** A token-reduction result is reported only when
the quality non-inferiority gate passes first. Cheaper-but-worse is not an
efficiency finding.

## Amendment to Phase 7A: repeat handling

Phase 7A recommended two repeats on the arms carrying the primary endpoint and a
binary McNemar primary. Those two do not compose: **with exactly two repeats a
majority vote can tie**, and inventing a tie rule after seeing the data is
precisely the freedom pre-registration exists to remove.

The harness therefore supports four named strategies —
`first_repeat_confirmatory`, `all_repeats_must_pass`, `any_repeat_passes`,
`mean_pass_proportion` — and the example plan uses the first:

> Repeat 0 is the confirmatory paired binary endpoint. Repeat 1 is a pre-planned
> robustness and variance measurement, used in sensitivity analysis, and never
> to redefine or inflate the primary outcome.

Both repeats are run and both are reported. `mean_pass_proportion` raises rather
than silently thresholding at 0.5, because it is a continuous endpoint and does
not belong in the binary path.

This is a deliberate correction made before any result exists.

## Consequences

- Exact McNemar semantics are preserved without arbitrary tie handling.
- The second repeat still earns its cost: it quantifies within-task variance,
  which matters because the current frontier models accept neither a seed nor a
  temperature, so nondeterminism cannot be eliminated — only measured.
- N = 150 detects the +10 pp MME at roughly 80% power under a 22% discordance
  assumption. 120 was rejected as an inheritance from Phase 4 rather than a
  choice.
