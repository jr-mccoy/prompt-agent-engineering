# ADR-0023 — Executable routing replaces table mechanics, not routing policy

## Status

Accepted. Stage 2 begun; `CLAUDE.md` remains canonical prose.

## Context

[ADR-0006](0006-staged-router-migration.md) planned a two-stage migration.
Stage 1 collapsed three drifting routing surfaces into one canonical prose
router. Stage 2 was to begin once `pae route` existed and had regression
coverage. It now does.

`CLAUDE.md` is 3,149 lines. A machine-readable pass over it finds **1,512
hand-written `"user phrase" → resource` pairs**, of which 887 unique phrases
resolve to registry records. Those mappings predate the search implementation
and were not produced by any algorithm under test, which makes them the closest
thing the repository has to an independent second opinion.

Measured against them:

| Measure | Router |
|---|---|
| resource@1 | 83.4% (83.9% counting registered copies of the named resource) |
| resource@3 | 91.0% |
| scope@1 | 92.2% |
| scope@3 | 96.1% |

These numbers are **flattered** and must not be quoted as evaluation: the
phrases are documentation labels, many of which share vocabulary with their
target's title. On the 120-case regression set, whose natural-language
paraphrases do not, the same router scores 70% top-1 on task retrieval.

The audit also found what the router cannot reproduce. Of `CLAUDE.md`'s
content, the mechanically reproducible part is the `phrase → resource`,
`task → domain` and `task → kind` mapping. Everything else has no registry
representation at all:

- the reuse-before-authoring policy;
- the new-prompt-versus-use-existing decision tree;
- the placement axis for new resources (self / individual / team / product / org);
- load-bearing domain conventions — the bug-bounty authorization gate, psy-ops
  analytic-only output, written-advocacy's no-invented-law rule, discipleship's
  formation-is-not-a-metric rule. `serving_policy: safety_gated` and the
  `quality` assertions record *that* a guard exists, never what it says;
- negative boundaries ("X lives here, **not** there") — search returns
  positives only;
- ordered workflows and pipeline sequencing;
- domain guide entry points, which are registry-excluded `meta_document`s;
- the authoring systems under `authoring/`, also registry-excluded;
- the token-efficiency rules.

The rule-table experiment in [ADR-0022](0022-routing-by-max-aggregation.md) is
the empirical warning: encoding routing prose as a keyword table scored 16.5%.

## Decision

**Phase 4 establishes the executable alternative and measures it. It deletes
nothing.**

- `pae search` and `pae route` ship and are advertised in the bootstrap files.
- The stale Phase 3-era claims in `AGENTS.md` and `START_HERE_FOR_AI.md` that
  no `pae` command exists are corrected — they were already false.
- `CLAUDE.md` gains a pointer to the executable router at its routing entry
  and keeps every line of its routing tables, conventions and policy.
- `scripts/compare_router_to_claude_md.py` makes the comparison reproducible so
  the migration decision rests on re-runnable evidence.

**A later phase may shrink the mechanical tables** — the ~1,075 quoted table
rows and ~584 example bullets whose whole function is `phrase → resource` —
once independent evaluation supports it. The prose that carries policy, safety
semantics, negative boundaries and authoring guidance is **not** migration
material at any stage.

Where the router and the table disagree, the table is evidence, not a defect to
be edited away. Rewriting the documentation so a measurement improves would
destroy the only independent signal available.

## Consequences

- Two routing surfaces exist during the transition: an executable one that is
  authoritative for `phrase → resource` and a prose one that is authoritative
  for everything else. This is deliberate duplication with a stated end date,
  not the drift ADR-0006 was written to stop — the executable side is generated
  from the registry and cannot go stale against it.
- Environments without the Engine installed lose nothing; the prose remains a
  complete fallback.
- The comparison script is a maintenance surface. It is a diagnostic, is not
  imported by the Engine, and can be deleted when the migration completes.

## Related

- [ADR-0006](0006-staged-router-migration.md) — the staged plan this continues
- [ADR-0022](0022-routing-by-max-aggregation.md) — the router being migrated to
- [ADR-0008](0008-generated-counts-control-plane.md) — generated beats
  hand-maintained, the same principle applied to counts
