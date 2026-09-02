# ADR-0040 — Public performance-claim governance

## Status

Accepted. Implemented in Phase 7.

## Context

The failure mode this repository is most exposed to is not a bad measurement. It
is a good measurement described badly: a number from a tuning set quoted as
evidence, a development run cited as a result, a directional claim from an
interval that straddles zero, or a bare "PAE has 90% accuracy" with no benchmark
attached.

Every one of those is easy to produce by accident, months later, by someone
reading a report and extracting a sentence.

## Decision

**The report generator contains no canned comparative sentence.** Every
directional word originates in one function, `_direction()`, which reads the
confidence interval. If the interval straddles zero, the only sentence available
says the run does not distinguish the conditions. There is no code path that
writes "improved" without a number requiring it.

**Null and negative results get the same template, the same section order and
the same prominence** as a positive one. Tests render all three from fixed
analyses and assert the wording follows the numbers, including that a negative
summary contains no positive-spin vocabulary.

**A claim-ready sentence is emitted only for a sealed run whose interval
excludes zero.** It always names benchmark and version, task count, PAE commit,
model, conditions, effect, 95% CI and repeat design. There is deliberately no
generic accuracy field to extract:

```text
On sealed benchmark X (N tasks) at PAE commit Y, model Z completed A% under
condition D versus B% under condition B (+D pp; paired 95% CI L to U;
n repeat(s)/task, confirmatory repeat only).
```

**Forbidden**: "PAE makes AI 20% smarter", "PAE has 90% accuracy", "proven to
improve every model", and any number derived from the Phase 4/5 internal sets.

**Every fixture artifact is stamped** `SYNTHETIC TEST FIXTURE — NOT INDEPENDENT
BENCHMARK EVIDENCE`, and every development run is labelled as such in its own
report, so sample output cannot be mistaken for a result by a future reader who
was not there.

**Limitations are generated, not remembered.** Every report states that results
are specific to this benchmark, corpus, commit and models; that participant
outputs are nondeterministic and reproducibility covers inputs and procedure
rather than outputs; that prices drift and token counts are the durable
measurement; that the baseline depends on ripgrep; and that LLM judging remains
imperfect. Single-family runs additionally state that they cannot separate "PAE
helps" from "PAE helps this family".

## Consequences

- A wrong claim requires editing code and deleting a test, not just writing an
  optimistic sentence.
- The negative-result path is exercised in CI on every pull request, so it can
  never rot while the positive path stays healthy.
- Nothing in this repository currently supports any public performance claim,
  and the tooling says so.
