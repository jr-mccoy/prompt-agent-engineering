---
name: handback
description: Write a conformant PAE registry into the audited corpus so the unmodified Engine runs on it, and run Gate C by calling the Engine's own validator. Use this command at the end of a governance engagement, or mid-engagement to prove the pipeline end to end. Blocks unless the Engine can open the tree and validation passes with checksums verified, and refuses to invent a copy edge, a review status, a quality tier or a licence.
version: "1.0.0"
category: orchestration
tags: [audit, registry, handback, gate-c, pae-engine, governance]
agents_used: [audit-orchestrator, claim-safety-reviewer]
---

# /handback — Gate C (Stage 6)

*The deliverable is a corpus that works, not a document about one.*

Runs [`prompts/stage-6-registry-handback.md`](../prompts/stage-6-registry-handback.md).

## Usage

```
/handback <corpus_dir> [--write]
```

## What it does

```bash
python3 skills/registry-handback/scripts/handback.py <corpus>          # dry run
python3 skills/registry-handback/scripts/handback.py <corpus> --write  # commit
```

1. Builds one record per artifact, carrying cluster findings as `diagnostics`
   and observed coverage under `structural-coverage-observed`.
2. Writes `meta/registry/registry.jsonl` and `registry-summary.json` **inside**
   the corpus, because `source.path` resolves against the repository root.
3. Runs `assert_nothing_invented()` and then **Gate C** — the Engine's own
   `validate_registry`, with checksums verified.

Without `--write` the whole thing happens in a staged copy that is discarded,
so a failed build can never leave a partial registry in a client tree.

## Prove it

```bash
PAE_REPO=<corpus> pae stats
PAE_REPO=<corpus> pae search "<something they know is there>"
PAE_REPO=<corpus> pae validate-registry
```

## Next

`prompts/stage-7-closeout-and-remediation-plan.md`.
