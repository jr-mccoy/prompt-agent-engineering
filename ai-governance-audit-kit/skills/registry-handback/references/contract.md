# The handback contract

What the Engine actually requires, and what this kit refuses to supply.

## Discovery

`Repository.at()` looks for exactly two files at fixed relative paths:

| Path | Must declare |
|---|---|
| `meta/registry/registry.jsonl` | one JSON object per line |
| `meta/registry/registry-summary.json` | `"schema": "pae-registry-summary/1"` |

Nothing else about the tree matters. That is ADR-0018's whole point, and it is
why a registry generated for a foreign corpus makes the unmodified Engine work
on it.

## Per record

`validate_registry` requires these fields to be **present**:

```
schema_version  uid  kind  id  aliases  lifecycle  title  serving_policy
```

and then checks:

| Check | Rule |
|---|---|
| `schema_version` | exactly `pae-registry-record/1`, or the run stops |
| `uid` | `^pae_[0-9abcdefghjkmnpqrstvwxyz]{12}$`, unique |
| `id` | the public-ID pattern, unique, not shadowed by an alias |
| `serving_policy.value` | one of `standard`, `safety_gated`, `metadata_only`, `excluded` |
| relationship UIDs | every referenced UID is claimed by some record |

For a **live, file-backed** record it additionally checks that
`source.path` is relative and stays inside the root, that the file exists and
is a regular file, that `source.content_sha256` is present with
`checksum_payload: "raw_source_bytes"`, and — with `verify_checksums` — that the
hash matches the bytes on disk.

An unrecognised `serving_policy.value` does not fail validation; the Engine
fails **closed**, treating it as `metadata_only`. The kit sets `standard`
explicitly with a basis line saying no client policy was supplied, rather than
letting a silent fail-closed look like a decision.

## Summary drift

The summary's `total_records`, `by_lifecycle`, `by_kind`, `by_kind_live`,
`by_kind_tombstone` and `by_serving_policy` are recounted from the records and
compared. Any disagreement is a `summary_drift` issue. Both files are
generated together; neither is ever hand-edited.

## Why the registry goes inside the corpus

`source.path` resolves against the repository root. A registry written beside
the corpus produces `missing_source_file` on every record — a registry whose
sources do not resolve is a report with a `.jsonl` extension.

## The four refusals, and what each costs

| Field | What the kit writes | What it would take to do better |
|---|---|---|
| `governance.review_status` | `unknown` | a named human reviewer and a recorded verdict |
| `relationships.copy_of` | `null` | an explicit ledger entry from the corpus owner |
| `license.status` | `unresolved` | the client's own licensing decision |
| `quality[].scheme` | `structural-coverage-observed` | the 46 unobservable rubric points, scored by a person |

Each refusal costs the report a confident-looking field and buys it the
property that every field it does fill in is defensible. `governance.py` makes
the same trade in this repository: `by_review_status: {unknown: <all>}` across
the whole registry, because inferring one from document structure would
fabricate a rubric score.

`assert_nothing_invented()` re-checks all four on every run, and Gate C fails if
any slipped. It is cheap and it is the warranty.

## Cluster findings ride as diagnostics

A detected duplicate is an observation, not an edge. It is written as:

```json
{"code": "exact_duplicate_detected", "severity": "warning",
 "detail": "byte-identical to <path> (evidence: sha256:...). No copy_of edge
            is asserted: which file is the canonical is the corpus owner's to
            declare."}
```

`near_duplicate_candidate` carries the similarity, the method and the shared
term count. Once the client adjudicates, *they* assert the edges — which is
exactly how `meta/VENDORED.tsv` works in this repository.

## Proving the handback

The proof is not that the files look right. It is that a tool nobody
customised runs on a corpus nobody wrote:

```bash
PAE_REPO=/path/to/their/corpus pae stats
PAE_REPO=/path/to/their/corpus pae search "<something in their corpus>"
PAE_REPO=/path/to/their/corpus pae validate-registry
```

Gate C runs the third of those in process, with checksums verified, so the
gate's verdict and the client's own command are the same check.
