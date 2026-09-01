# ADR-0014 — Metadata may degrade; identity may not

## Status

Accepted. Implemented in Phase 2.

## Context

Of 4,890 file-backed first-class resources, 133 have no frontmatter at all and 2 have
frontmatter that fails to parse — both of the latter for the same reason, an
unquoted `description:` containing a colon-space
(`domain-agentic-resources/skills/non-coding/healthcare/pacu-case-scenario-writer/SKILL.md`
and `ai-investment-research-toolkit/skills/paper-trade-executor/SKILL.md`).

Failing the whole build over one unquoted colon in one of nearly five thousand files
would make the registry hostile to maintain. Silently substituting invented metadata
would be worse: the corpus is full of prompts whose central instruction is not to
fabricate, and a registry that fabricates its own metadata would be indefensible.

`generate_prompt_index.py` handles this with `_fallback_extract()`, a regex scavenger
that pulls what it can from unparseable YAML. That is the right call for a
best-effort search index and the wrong call here, because its output is
indistinguishable from properly parsed metadata.

## Decision

Three failure classes, three behaviours.

**Identity cannot be trusted** — an undecidable kind, a duplicate candidate path, a
UID or public-ID collision, an unresolvable relationship target, a cycle in the move
chain. **Generation aborts.** Identity is the one thing the registry cannot be wrong
about.

**Source parse error** — a degraded record: `metadata_completeness: degraded`,
`serving_policy: metadata_only`, a `frontmatter_parse_failed` diagnostic carrying the
parser's own message, and **no scavenged fields**. Never `stable`.

**Missing optional metadata** — a minimal record: `metadata_completeness: minimal`,
title derived from the first H1 or, failing that, the title-cased slug, and **no
synthesized description**. The legacy index derives a description from the first
paragraph; that is acceptable for search ranking and unacceptable for a registry
field a consumer may treat as authored.

Every derived value is listed in `derived_fields`. Diagnostics land in two
deterministic places: inline on the record, and aggregated in `diagnostics.jsonl`
sorted by code and UID.

## Consequences

- Two known content bugs are surfaced with their exact parser errors instead of being
  hidden or fatal, and are fixable without touching the registry.
- 133 frontmatter-less resources are represented honestly and appear as a standing
  count in `registry-summary.json`, so the gap stays visible.
- A consumer can always distinguish authored metadata from derived metadata, and
  degraded records from complete ones.
