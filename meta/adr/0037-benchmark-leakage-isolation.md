# ADR-0037 — Benchmark isolation by construction, and the participant snapshot

## Status

Accepted. Implemented in Phase 7.

## Context

Two contamination routes threaten the primary comparison, and both are silent:
a run affected by either produces numbers that look completely normal.

**The benchmark.** If gold labels, rubrics or grader prompts live anywhere the
Condition B agent can read, it can discover the answers.

**The harness itself.** This is the route Phase 7A missed and Phase 7 had to
add. Once `pae-engine/evaluation/` is committed, a raw-repository agent given
the repository root can read the condition definitions, the participant prompt,
the judge logic and the fixtures — contaminating Condition B even though the
benchmark lives outside the repository entirely.

## Decision

**The benchmark lives outside the participant checkout**, in a separate
repository, cloned at run time to a path the participant cannot address. The
harness refuses in sealed mode if the benchmark root resolves inside the
participant root, the source checkout or the output directory. Resolution
follows symlinks, so a symlinked benchmark directory cannot alias its way
inside.

**Runs bind to a participant snapshot, never to the working tree.** The snapshot
is extracted from Git objects at an explicit commit with the evaluation tree
excluded:

```text
excluded:  pae-engine/evaluation/**, evaluation-runs/**, .git/**, virtualenvs
included:  meta/registry/**, the corpus, CLAUDE.md, AGENTS.md, the Engine runtime
```

Reading from Git objects rather than copying the working tree buys three things:
an uncommitted file cannot leak in, the bytes are exactly what the commit says,
and the result is reproducible from `(commit, exclusions)` alone. The manifest
records a digest per file plus one aggregate digest and contains no absolute
paths, so a snapshot of the same commit hashes identically wherever it is built.

Conditions B, C and D bind to the **same** snapshot. If they did not, the
comparison would be measuring different corpora and no amount of statistics
would repair it.

Excluding too much is a failure too: `assert_product_present` refuses a snapshot
missing the registry, the Engine runtime or the corpus, because a snapshot
without those is not the product and every condition would be measuring an empty
repository.

Every isolation check **fails closed** and runs before the first paid request.

## Consequences

- Contamination is prevented structurally rather than by a rule someone must
  remember to maintain.
- Sealed runs cannot be launched from a dirty checkout.
- Snapshot construction costs roughly 15 seconds and some disk per run. Cheap
  next to a contaminated result nobody detects.
- The harness can never be evaluated by the participant it is grading.
