---
name: cluster
description: Find exact and candidate near-duplicate clusters in an inventoried corpus and report them with evidence. Use this command when a consolidation decision needs proof, when a client asks how much of their library is redundant, or before proposing any merge. Reports byte-identical files from content hashes and lexical near-neighbours from BM25F, and never names a canonical.
version: "1.0.0"
category: analysis
tags: [audit, duplication, clustering, bm25f, governance]
agents_used: [duplication-analyst]
---

# /cluster — Stage 2

*Clusters are findings for adjudication, never asserted copies.*

Runs [`prompts/stage-2-duplication-clusters.md`](../prompts/stage-2-duplication-clusters.md).

## Usage

```
/cluster <corpus_dir>
```

## What it does

```bash
python3 skills/duplication-clusters/scripts/cluster.py \
  --inventory audit/inventory.json --out audit/clusters.json
```

1. Groups byte-identical artifacts by `content_sha256`.
2. Scores all pairs by query-by-document over the Engine's own BM25F index,
   normalized by self-score and reported as the minimum of both directions.
3. Emits every cluster with `canonical_uid: null` and a stated basis.

## Next

`/score-observed`.
