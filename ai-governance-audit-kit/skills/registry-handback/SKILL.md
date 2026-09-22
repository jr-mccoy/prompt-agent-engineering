---
name: registry-handback
description: Write a conformant PAE registry into the audited tree so the client keeps working tooling rather than a PDF. Use this skill to "hand back the audit", "make their corpus searchable", "generate a registry for their library", "give them something that runs", or at the end of any governance engagement. Runs Gate C by calling the Engine's own validator in process, and refuses to invent a copy edge, a review status, a quality tier or a licence.
license: MIT
compatibility: Standard library only, Python 3.9+, plus the PAE checkout it ships inside for `pae_engine.repository` and `pae_engine.validate`. `scripts/handback.py --self-check` proves the unmodified Engine opens what the kit wrote, that a tampered checksum is caught, that an un-inventoriable corpus never reaches a registry, and that a dry run leaves the corpus untouched. No network. Writes only under `--write`.
metadata:
  tags: [audit, registry, handback, gate, governance, pae-engine, deliverable]
  updated: "2026-09-22"
---

# Registry Handback

## Purpose

This is the move that turns a report into an asset.

`Repository.at()` requires exactly two marker files at fixed relative paths —
`meta/registry/registry.jsonl` and `meta/registry/registry-summary.json` — plus
supported schema versions. Nothing ties the Engine to *this* repository's
content, only to that contract (ADR-0018).

So a conformant `meta/registry/` written into the client's own tree makes the
entire Engine — search, routing, context bundling, validation, the MCP server —
work on their corpus unchanged:

```bash
PAE_REPO=/path/to/their/corpus pae stats
PAE_REPO=/path/to/their/corpus pae search "incident timeline"
PAE_REPO=/path/to/their/corpus pae validate-registry
```

If the unmodified Engine opens a registry this kit generated for a foreign
tree, the handback works. If it does not, the kit is a report generator.

## What this refuses to invent

- **No quality tier.** `governance.maturity` is `experimental` and both review
  and eval status are `unknown` for every record. Inferring otherwise from
  document structure would fabricate a rubric score.
- **No copy edges.** `relationships.copy_of` is `null` and `copies` is empty
  *even where a cluster was found*. Copies come from explicit edges, never from
  hashes or filenames (ADR-0012). Cluster findings ride as `diagnostics` —
  observations with evidence — so the client can adjudicate and then assert the
  edges themselves.
- **No licence.** `license.status` is `unresolved`. An audit that guesses a
  client's licensing has invented the fact most expensive to get wrong.
- **No tier-shaped quality scheme.** Observed coverage is recorded under
  `structural-coverage-observed`, whose name says both what the number is and
  how it was obtained.

`assert_nothing_invented()` checks all of this on every run, and Gate C fails
if any of it slipped.

## Why the registry goes *inside* the corpus

`pae validate-registry` resolves each record's `source.path` against the repository
root, and verifies its checksum. A registry written beside the corpus produces
`missing_source_file` on every record. A registry whose sources do not resolve
is a report with a `.jsonl` extension.

## When to Use

- At the end of an engagement, as the deliverable.
- Mid-engagement, to prove the pipeline end to end before writing the report.

## When NOT to Use

- On this repository. `scripts/generate_registry.py` owns that, with membership
  rules tuned to this tree.
- Before Gate 0 passes. `produce()` refuses, because a registry built from an
  empty inventory is a confident, empty, wrong answer.

## Instructions

1. Dry-run first: `scripts/handback.py <corpus>`. The registry is built and
   validated in a staged copy and the corpus is left untouched.
2. Read Gate C. The verdict is the Engine's own `validate_registry` result,
   with checksums verified, not a look at whether the files seem right.
3. Fix findings at their source — a `duplicate_public_id` is a corpus problem,
   not a registry problem — and re-run the dry run.
4. When Gate C passes, run `scripts/handback.py <corpus> --write`.
5. Prove it to the client in their own shell with the three `PAE_REPO` commands
   above. The proof is that the Engine they did not install ran on the corpus
   you did not write.

## Bundled Resources

- `scripts/handback.py` — record building, summary, writing, and Gate C.
- `references/contract.md` — the exact record and summary contract the Engine
  enforces, field by field, and what each refusal above costs and buys.

## Safety

The dry run copies the corpus into a temporary directory and discards it, so a
failed build can never leave a partial registry in a client tree. `--write` is
the only path that touches the corpus, and it writes only under
`meta/registry/`.

## Troubleshooting

- `missing_source_file` on every record: the registry was written outside the
  corpus. Point `--write` at the corpus root.
- `checksum_mismatch`: the corpus changed between inventory and handback.
  Re-run from `corpus-inventory`.
- `summary_drift`: records and summary disagree. Rebuild rather than hand-edit
  either; both are generated.

## Verification

- [ ] Gate C passes with checksums verified.
- [ ] `PAE_REPO=<corpus> pae validate-registry` passes in the client's own shell.
- [ ] `assert_nothing_invented()` returns empty.
- [ ] Every cluster finding is a diagnostic, and no record carries a copy edge.

## Related Skills

- `corpus-inventory`, `duplication-clusters`, `observed-scoring` — the three
  stages whose output this assembles.
- `claim-safety` — governs how the accompanying report may describe this.
