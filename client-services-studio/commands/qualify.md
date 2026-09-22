---
name: qualify
description: Run Gate 0 against a new inquiry and decide whether to spend discovery time on it. Use this command when a lead arrives and you need a ten-minute qualification, a decline, or a booking decision. Blocks on missing decision-maker, absent budget authority, undefined outcome, a sub-floor implied rate, a concentration breach, or any decline-tier disqualifier in the practice config.
version: "1.0.0"
category: orchestration
tags: [client-services, qualification, gate-0, consulting, freelance]
agents_used: [engagement-orchestrator]
---

# /qualify — Gate 0 (Stage 1)

*Not legal, tax, or accounting advice.*

Runs [`prompts/stage-1-qualify-lead.md`](../prompts/stage-1-qualify-lead.md).

## What it does

1. Captures the lead record from what the prospect actually said — nothing inferred.
2. Runs the ten-minute question sequence from your disqualifier work.
3. Executes Gate 0:
   ```bash
   python3 skills/scope-ledger/scripts/scope_ledger.py \
       --gate0 <lead.json> --config config/practice.json
   ```
4. Returns one of: **book discovery**, **probe first** (with the specific question),
   **proceed with protection** (with the named structural change), or **decline**
   (with the decline message).

## Preconditions

- `config/practice.json` exists and carries at least three disqualifiers, one of them
  `decline` tier. If not, run [`/prompts/stage-0-practice-config.md`](../prompts/stage-0-practice-config.md) first.

## Notes

Unknown budget is a discovery question, not a failure. Only a *stated* budget
implying a rate below `walk_away_day_rate` blocks.

A blocked lead is declined in the first conversation, honestly and briefly. If you
override the gate, record which check fired, why, and a review date.
