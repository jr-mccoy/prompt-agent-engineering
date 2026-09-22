---
name: inventory
description: Run Gate 0 against a corpus and produce a counted partition of it into resources and recorded exclusions. Use this command at the start of a governance audit, when a prompt-library count is disputed, or whenever the audit config changes. Blocks on a missing root, a config that matches nothing, an empty corpus, an underivable identity, or two artifacts claiming the same public ID.
version: "1.0.0"
category: orchestration
tags: [audit, inventory, gate-0, governance, corpus]
agents_used: [audit-orchestrator]
---

# /inventory — Gate 0 (Stage 1)

*This kit reports structure. It does not review content.*

Runs [`prompts/stage-1-inventory-the-corpus.md`](../prompts/stage-1-inventory-the-corpus.md).

## Usage

```
/inventory <corpus_dir>
```

## What it does

1. Loads `config/audit.json` and refuses to run if the config is invalid —
   including a `non_resource_prefixes` entry that is a bare directory name.
2. Walks the corpus once, partitioning every file into a counted resource or a
   recorded exclusion.
3. Assigns each resource a UID from `pae_registry.identity.uid_for` and a public
   ID from the configured scope prefix.
4. Runs **Gate 0** and writes `audit/inventory.json`.

```bash
python3 skills/corpus-inventory/scripts/inventory.py <corpus> --out audit/inventory.json
```

## Read the output in this order

1. The Gate 0 verdict.
2. The exclusion counts.
3. The resource count — last, and never quoted without the other two.

## Next

`/cluster`, then `/score-observed`.
