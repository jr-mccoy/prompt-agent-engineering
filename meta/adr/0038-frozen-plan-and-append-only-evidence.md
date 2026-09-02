# ADR-0038 — A frozen plan and append-only evidence

## Status

Accepted. Implemented in Phase 7.

## Context

Every degree of freedom exercised after seeing results is a way for a null
result to become a positive one without anybody lying: adjust the endpoint,
retry the arm that did badly, re-run with a tweaked prompt and keep the better
number, drop the tasks that "clearly didn't work".

Pre-registration removes those degrees of freedom, but only if it is checkable.
An intention recorded in a document is an honour system.

## Decision

**One hashed plan.** `evaluation-plan.json` plus a sidecar digest pins the
benchmark, the PAE commit, the snapshot, conditions, models, prompt hashes, tool
catalog hashes, bundle budget, limits, repeats and repeat strategy, judge
configuration and thresholds, primary and secondary endpoints, the minimum
meaningful effect, the non-inferiority margin, the multiplicity policy, the
retry policy, the exclusion rules, the randomization seed and the pricing
snapshot. No secret ever enters a plan; credentials are named by environment
variable, never valued.

**Sealed execution refuses a mismatched world.** The harness cannot stop anyone
committing after a freeze, but it can refuse to *run*: a changed commit, tool
catalog, prompt or benchmark hash raises rather than proceeding. Development
mode may proceed with warnings and carries a distinct run identity, so its
results can never be mistaken for sealed ones.

**The schedule is materialized before the first paid request**, hashed, and
interleaves conditions rather than blocking them. Generating order lazily as
results arrive would make execution order a function of the results; running all
of B before all of D would confound the primary contrast with provider drift.

**Trials are append-only**, one line per attempt, fsynced. Nothing is ever
rewritten. A re-run cannot overwrite the record of what happened the first time.

**Trial IDs are derived, not random** — a hash of evaluation version, benchmark,
task, condition, model config, repeat and plan. Resume skips only exact
completed IDs, and only when the plan, benchmark and snapshot hashes still
match. A different configuration is a different experiment and gets a new run.

**Model-output caching is disabled in sealed mode**, and where development mode
caches, the key includes the resolved model identity and every prompt and
catalog hash — never a bare model alias, because an alias is not a snapshot and
a silent model swap would otherwise be invisible.

## Consequences

- "We decided this in advance" is verifiable rather than remembered.
- Fixing a defect mid-evaluation forces a new evaluation version, preserving the
  original run. That is the intended friction.
- Evidence files grow monotonically. Storage is cheap; a quietly replaced result
  is not.
