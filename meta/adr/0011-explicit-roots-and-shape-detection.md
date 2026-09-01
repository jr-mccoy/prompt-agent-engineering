# ADR-0011 — Registry membership is explicit roots plus shape detection, and exclusions are anchored prefixes

## Status

Accepted. Implemented in Phase 2.

## Context

`PROMPT_INDEX.json` cannot answer "what resources exist" (ADR-0007): it contains 667
bundled component files that are not resources, and omits 118 first-class resources
that live in the root toolkits.

Three discovery strategies were available: recurse the whole repository and detect
shapes; require each root to publish a manifest; or allowlist roots explicitly and
detect shapes within them.

Unconstrained recursion fails immediately. The repository contains
`agentic-system-factory/samples/*/agents/`, `childrens-book-studio/design-bundle/agents/`
and `domain-agentic-resources/documentation/technique-analyses/skills/` — sample
bundles, design proofs and documentation that look exactly like resource trees.

Manifests were rejected for a different reason: a manifest is a second thing to keep
in sync, and this repository has repeatedly solved drift by *generating* truth rather
than declaring it (`inventory_counts.py`, `generate_repo_facts.py`, ADR-0008).

A bare directory-name blocklist was tried first during Phase 2A and **failed
measurably**. Blocking the segment name `documentation` silently deleted six genuine
first-class resources — five agents in `domain-agentic-resources/agents/documentation/`
and one command in `commands/documentation/` — because those directories are a
*category* of documentation-writing resources, not documentation about resources.
The intended target was `domain-agentic-resources/documentation/`. Segment names
cannot distinguish the two.

## Decision

Membership requires two independent agreements: an **approved root** and a **shape
detector**.

Approved roots are an explicit allowlist: the 44 `domain-*` directories, read from
the index generator's own `DOMAIN_DIRS` so the two cannot drift, plus five root
toolkits validated in Phase 2A. A root that does not exist on disk is a hard error.

**Exclusions are anchored path prefixes, never bare directory names.** This is a
load-bearing invariant with a regression test, not a stylistic preference.

Detector precedence is fixed and total — every path yields exactly one kind or one
exclusion reason, and ties are impossible because each rule returns immediately.
Discovery fails on a multi-kind match, a duplicate candidate path, or an invalid root
configuration.

Historical paths are judged against the union of current roots and the roots that
appear in `meta/REORG_MAP.tsv`, because a resource removed from a since-retired
domain was still first-class when it existed.

## Consequences

- 4,890 file-backed resources are discovered, reconciling exactly with every
  independently computed count in `meta/REPOSITORY_FACTS.json`.
- Adding a toolkit is a deliberate, reviewable one-line change.
- New sample or demonstration trees must be added to the prefix list, or they will
  be discovered as resources. The dry-run report surfaces this immediately.
