---
title: "Data Loading Bottleneck Audit"
category: AI-ML/deep-learning
description: "Find and fix input-pipeline bottlenecks starving the accelerator: localize the stall (I/O, decode, augmentation, host-to-device copy, collate) via measurement, then prescribe targeted fixes."
techniques:
  - RT-10
  - ST-02
  - DS-02
  - RT-09
  - QA-01
difficulty: intermediate
tags:
  - data-pipeline
  - gpu-utilization
  - throughput
  - dataloader
  - profiling
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/deep-learning/dl_distributed_training_plan.md
  - domain-AI-ML/deep-learning/dl_mixed_precision_setup.md
  - domain-AI-ML/deep-learning/dl_training_not_converging_debug.md
---

# Data Loading Bottleneck Audit

**Objective:** Diagnose why the accelerator is under-utilized during training by localizing the input-pipeline stall — storage I/O, file decode, augmentation cost, host-to-device transfer, or collate/batching — through targeted measurement, then prescribe the specific fix (prefetch, parallel workers, caching, format change, GPU-side augmentation) and confirm GPU utilization recovers.

**When to Use:**
- GPU/TPU utilization is low and choppy while training; step time is dominated by waiting for data.
- Throughput is far below the model's compute capacity.
- Moving to faster accelerators yielded little speedup (pipeline-bound, not compute-bound).

**When NOT to Use:**
- The model isn't learning (loss flat/NaN) — that's `dl_training_not_converging_debug.md`, not a throughput issue.
- The bottleneck is cross-device communication in distributed training (`dl_distributed_training_plan.md`).
- You want memory headroom, not throughput (`dl_mixed_precision_setup.md`).

## Inputs / Context

Provide what you can:
- **Framework & version** and dataloader API; hardware (accelerator, CPU cores, disk type, network storage?).
- **Observed GPU utilization** pattern (low/choppy/spiky) and step-time breakdown if available.
- **Data format & storage** — many small files vs sharded archives; local SSD vs network/object store.
- **Augmentation pipeline** — what transforms run on CPU per sample and their cost.
- **Current dataloader settings** — workers, prefetch, batch size, pinned memory, caching.

## Constraints

**Must:**
- Localize the bottleneck by measurement (compare a data-only loop vs a compute-only loop) before changing settings.
- Distinguish the stall stages (I/O vs decode vs augmentation vs transfer vs collate) — each has a different fix.
- Confirm the fix by re-measuring GPU utilization/throughput, not by assuming.

**Must Not:**
- Crank up worker count blindly and call it solved without measuring (too many workers can thrash CPU/memory).
- Quote a specific throughput-gain number as fact — frame all gains as to-be-measured on the user's setup.
- Change format, workers, and augmentation at once and lose attribution.

**Instructions:**

1. **Measure the gap.** Compare three loops: (a) full training step time, (b) data-only loop (iterate the loader, no model), (c) compute-only loop (synthetic/cached batch, no loading). This isolates whether you're data-bound and by how much.

2. **Localize the stall stage.** Within the data-only loop, time I/O (read), decode, augmentation, collate, and host-to-device copy separately. The dominant stage is the target.

3. **I/O-bound fixes.** If reads dominate (many small files / network storage): switch to sharded archive formats, increase read parallelism, stage data to local SSD, or cache to memory/disk after first epoch.

4. **Decode/augmentation-bound fixes.** If CPU transforms dominate: add parallel workers up to CPU saturation, move heavy augmentation to the GPU, precompute deterministic transforms, or simplify the pipeline.

5. **Transfer/collate-bound fixes.** If host-to-device copy dominates: enable pinned memory and async transfer, overlap copy with compute via prefetch, and ensure efficient collate (avoid per-sample Python overhead).

6. **Tune overlap and depth.** Set prefetch depth and worker count to overlap loading with compute; find the point where adding workers stops helping (CPU/memory saturation).

7. **Re-measure and confirm.** After each single change, re-run the three-loop comparison; keep the change only if data-bound time shrank and GPU utilization rose. Record the final config.

**Output Format:**

A markdown report:
- **Bound Diagnosis** — data-bound vs compute-bound (three-loop numbers, illustrative).
- **Stall Localization** — which stage dominates + evidence.
- **Targeted Fixes** — table: Stage | Fix | Expected Effect | Order.
- **Overlap/Depth Tuning** — workers/prefetch/pinned settings.
- **Confirmation** — re-measured utilization/throughput per change.
- **Final Pipeline Config.**

## Verification

- [ ] A data-only vs compute-only comparison establishes data-bound before any fix.
- [ ] The dominant stall stage is localized by per-stage timing.
- [ ] Each fix matches its stage (I/O vs decode/aug vs transfer/collate).
- [ ] Changes are applied one at a time and re-measured.
- [ ] Throughput gains are measured, not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Assume low GPU utilization means a slow model — it's usually the input pipeline; measure first.
- Set worker count to a huge number and assume more is better — CPU/memory thrash can slow it down.
- Move augmentation to GPU when the real stall is network I/O on small files.
- Declare it fixed without re-measuring GPU utilization.

✅ **DO:**
- Run the three-loop comparison to confirm data-bound and quantify the gap.
- Time each pipeline stage to localize the dominant cost.
- Apply the stage-matched fix (sharded I/O, GPU aug, pinned async transfer) one at a time.
- Re-measure utilization/throughput and keep only changes that help.

## Example Output

```markdown
## Data Pipeline Audit: Image Classifier, GPU ~35% utilized (choppy)

### Bound Diagnosis (illustrative)
Full step 120ms; compute-only 45ms; data-only 110ms → heavily data-bound.

### Stall Localization
Per-stage timing: I/O reads 70ms (many small JPEGs on network store), decode 20ms, augmentation 15ms, transfer 5ms → I/O dominates.

### Targeted Fixes
| Stage | Fix | Expected Effect | Order |
|---|---|---|---|
| I/O | Pack into sharded archives (e.g., tar/records) | Big read reduction | 1 |
| I/O | Stage shards to local SSD | Removes network latency | 2 |
| Decode/Aug | More workers to CPU saturation | Overlap | 3 |
| Transfer | Pinned memory + async copy | Overlap copy | 4 |

### Overlap/Depth Tuning
Workers raised to ~CPU cores; prefetch depth 4; pinned memory on.

### Confirmation
After sharding + SSD staging: data-only drops to ~50ms; GPU utilization rises to ~85%. Re-measured each step.

### Final Pipeline Config
Sharded archives on local SSD, workers=cores, prefetch=4, pinned async transfer.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** stage branches (I/O / decode / transfer) drive the fix.
- **ST-02 (Structured Sequential Instructions):** measure gap → localize → fix → re-measure.
- **DS-02 (Metric Specification):** three-loop timing and GPU utilization are the diagnostics.
- **RT-09 (Root Cause Explanation):** ties low utilization to the dominant stall stage.
- **QA-01 (Self-Verification):** checklist enforces measure-before-and-after discipline.

**Related Prompts:**
- `dl_distributed_training_plan.md` — when the limiter is inter-device communication, not loading.
- `dl_mixed_precision_setup.md` — when the goal is memory headroom rather than input throughput.
- `dl_training_not_converging_debug.md` — when the issue is learning, not throughput.
```