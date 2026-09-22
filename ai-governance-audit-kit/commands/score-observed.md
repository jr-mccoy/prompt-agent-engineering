---
name: score-observed
description: Score artifacts from detectors that read them rather than from a rubric block their author wrote, and run Gate A on the result. Use this command to audit skill quality, to locate credentials and absolute paths in a corpus, or whenever a score has to survive someone asking where it came from. Refuses any score with no rubric version, no stated provenance, an asserted tier, or a category above its observable maximum.
version: "1.0.0"
category: analysis
tags: [audit, scoring, rubric, gate-a, security, governance]
agents_used: [audit-orchestrator]
---

# /score-observed — Gate A (Stage 3)

*54 of the rubric's 100 points are mechanically observable. No tier is asserted.*

Runs [`prompts/stage-3-observed-scoring.md`](../prompts/stage-3-observed-scoring.md).

## Usage

```
/score-observed <bundle_or_file>
```

## What it does

```bash
python3 skills/observed-scoring/scripts/observed_score.py <bundle> --json
python3 skills/observed-scoring/scripts/observed_score.py --gate-a audit/score.json
```

1. Runs every observable detector and awards points against the **observable**
   maximum, stated per category.
2. Caps the verdict at `blocked` on any of the three blocking security checks,
   each reported with a file and a line.
3. Reports an author's self-reported rubric block separately, never merged.
4. Runs **Gate A**.

## Next

`/handback`, once findings are collated and the report passes Gate B.
