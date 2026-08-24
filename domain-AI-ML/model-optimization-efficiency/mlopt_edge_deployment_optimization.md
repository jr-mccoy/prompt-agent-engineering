---
title: "ML Edge / On-Device Deployment Optimization"
category: AI-ML/model-optimization-efficiency
description: "Optimize a model for edge / mobile / embedded deployment — size, memory ceiling, power, and thermal limits — under hard on-device constraints, pairing each optimization with its accuracy cost and an on-device (not host) measurement plan."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-02
  - QA-12
difficulty: advanced
tags:
  - edge-deployment
  - mobile-ml
  - on-device
  - power-efficiency
  - memory-footprint
  - quantization
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-optimization-efficiency/mlopt_quantization_plan.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_compression_tradeoff_analysis.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_inference_latency_optimization.md
---

# ML Edge / On-Device Deployment Optimization

**Objective:** Produce a plan to fit and run a model on an edge / mobile / embedded target within hard device constraints — binary/asset size, RAM ceiling, sustained power/thermal budget, and the available on-device accelerator (NPU/DSP/GPU/CPU) — sequencing the optimizations (format conversion, quantization, pruning/architecture swap, delegate selection) and pairing each with its accuracy cost and a measurement protocol that runs on the device, not the development host.

**When to Use:**
- A model must run on a phone, microcontroller, embedded SoC, or other resource-constrained device.
- A model exceeds the device's RAM, storage, battery, or thermal envelope and must be made to fit.
- You need to pick an on-device runtime/delegate and a precision that the device actually accelerates.

**When NOT to Use:**
- The target is server/cloud serving (use `mlopt_inference_latency_optimization.md` / `mlopt_throughput_batching_optimization.md`).
- You only need a precision plan, not the full device-fit problem (use `mlopt_quantization_plan.md`).
- You want to compare compression families abstractly first (use `mlopt_compression_tradeoff_analysis.md`).

## Inputs / Context

Provide what you can:
- **Target device + on-device runtime** — exact SoC/MCU, available accelerators (NPU/DSP/GPU/CPU), the on-device inference runtime/delegate, and OS. *Ask the user if unspecified — the delegate and supported ops gate everything.*
- **Framework + version** — training framework and the export/conversion path to the on-device format.
- **Hard constraints** — max app/asset size, RAM ceiling at runtime, sustained power/thermal budget, cold-start/load-time limit.
- **Accuracy bar** — the metric, current score, and maximum acceptable drop.
- **Latency need** — required on-device latency (often interactive, e.g., real-time camera/audio).
- **Connectivity** — whether any cloud fallback exists or the model must be fully offline.

## Constraints

**Must:**
- Ask for the target device + on-device runtime/delegate and framework + version; tie every optimization to ops the delegate actually supports (unsupported ops fall back to CPU and erase the win).
- Treat the device RAM ceiling and size limit as hard filters; a model that doesn't fit is not a candidate at any speed.
- Pair every optimization with its accuracy cost and measure latency/power/memory **on the device**, never extrapolated from the host.

**Must Not:**
- Quote specific size/latency/power numbers as measured — mark figures as estimates to verify on the actual device.
- Assume an op or precision is hardware-accelerated on the device's NPU/DSP without confirming delegate support.
- Report host (laptop/server) inference numbers as if representative of the device.

**Instructions:**

1. **Restate the device envelope.** Fix the hard ceilings: asset size, runtime RAM, sustained power/thermal, load-time, and the required latency. These are the constraints every step must respect.

2. **Confirm the runtime, delegate, and op support.** Identify the on-device runtime and accelerator delegate; check which ops run on the NPU/DSP vs fall back to CPU. Unsupported-op fallback is the top cause of "optimized but still slow" on edge.

3. **Convert and baseline on-device.** Convert to the device format and measure the unoptimized on-device size, RAM, latency, and power as the reference — not host numbers.

4. **Apply quantization for the device.** Choose int8/fp16 per delegate support (often int8 for NPUs/DSPs); cross-link `mlopt_quantization_plan.md`. Pair with an on-device accuracy check. This is usually the largest size + power lever on edge.

5. **Apply architecture / pruning levers if still over budget.** Consider a mobile-efficient architecture or structured pruning; weigh the accuracy cost. Prefer architectures whose ops the delegate accelerates.

6. **Optimize memory and load behavior.** Address weight memory-mapping, activation memory reuse, model-load/cold-start time, and avoiding RAM spikes that trigger OS kills on mobile.

7. **Manage power and thermal.** Plan for sustained (not peak) inference: thermal throttling reduces clocks under continuous load, so measure steady-state latency/power over a realistic duty cycle, not a single inference.

8. **Define on-device measurement and gates.** Specify measuring size, peak RAM, p50/p95 latency, and energy-per-inference on the device over a sustained run, plus accuracy on a held-out set. Pass = all hard ceilings met AND accuracy drop ≤ budget. Define the fallback (smaller architecture, partial cloud offload, or feature reduction).

**Output Format:**

A markdown plan:
- **Device Envelope** — size/RAM/power/thermal/load/latency ceilings
- **Runtime, Delegate & Op-Support Check** — accelerated vs CPU-fallback ops
- **On-Device Baseline** — unoptimized size/RAM/latency/power
- **Optimization Sequence** — table: Step | Lever | Est. gain | Accuracy cost | Delegate support
- **Memory / Load / Thermal Plan**
- **On-Device Measurement & Gates** — metrics, sustained-run protocol, pass/fail + fallback
- **Open Questions** — device specifics, delegate support, accuracy budget

## Verification

- [ ] The device's hard ceilings (size, RAM, power/thermal, load, latency) are restated and used as filters.
- [ ] On-device runtime/delegate and op support are confirmed before claiming acceleration.
- [ ] Baseline and all results are measured on the device, not the host.
- [ ] Every optimization is paired with an accuracy cost and an on-device measurement.
- [ ] Sustained/thermal-throttled latency and power are measured over a realistic duty cycle, not a single run.
- [ ] Pass/fail gates and a fallback exist.

## False-Positive Prevention

❌ **DON'T:**
- Report inference latency from the dev laptop/emulator as the device latency — they differ by an order of magnitude.
- Assume an int8 model uses the NPU — if even a few ops are unsupported, the graph falls back to CPU and the win vanishes.
- Measure a single cold inference and miss the thermal throttling that slows sustained, real-world use.
- Hit the size target while blowing the runtime RAM ceiling, causing the OS to kill the app under memory pressure.

✅ **DO:**
- Benchmark on the actual device (and a representative low-end device, not just the flagship) over a sustained duty cycle.
- Verify the delegate runs the whole graph on the accelerator; inspect the op-placement report for CPU fallbacks.
- Report peak RAM and energy-per-inference alongside latency, all measured on-device.
- Validate accuracy on-device after conversion/quantization — conversion can subtly change numerics.

## Example Output

```markdown
## Edge Optimization: On-Device Wake-Word + Keyword Model (target: mobile SoC NPU)

### Device Envelope
Asset ≤ 3 MB, runtime RAM ≤ 40 MB, must run continuously at < 1% battery/hr, load < 200 ms, latency p95 ≤ 20 ms.

### Runtime, Delegate & Op-Support Check
On-device runtime + NPU delegate. Conv/depthwise/FC supported on NPU; custom log-mel op falls back to CPU — move it to a preprocessing path so the graph stays on NPU.

### On-Device Baseline (fp32, NPU)
Size 9 MB, RAM 70 MB, p95 28 ms, ~2.4% battery/hr — over budget on size, RAM, power.

### Optimization Sequence
| Step | Lever | Est. gain | Accuracy cost | Delegate support |
|---|---|---|---|---|
| 1 | int8 PTQ (per-channel) | ~4x size, lower power | ~0.5% acc (verify) | NPU int8 supported |
| 2 | Remove CPU-fallback op from graph | latency stability | none | keeps graph on NPU |
| 3 | Depthwise-separable swap if still over | smaller/faster | ~1% acc | supported |

### Memory / Load / Thermal Plan
mmap weights; reuse activation buffers; measure steady-state over a 10-min continuous-listening duty cycle for throttling and battery.

### On-Device Measurement & Gates
Measure size, peak RAM, p95 latency, energy/inference, and accuracy on held-out audio — on the device, sustained run, plus one low-end device.
Pass if size ≤ 3 MB AND RAM ≤ 40 MB AND battery < 1%/hr AND p95 ≤ 20 ms AND accuracy drop ≤ 1%. Else swap architecture or reduce feature set.

### Open Questions
- Confirm NPU int8 op coverage for the full graph; confirm accuracy budget (assumed 1%).
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** envelope → delegate check → baseline → quantize → architecture → memory/thermal → measure/gate.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances size, RAM, power, thermal, latency, and accuracy jointly.
- **CM-02 (Constraint Specification):** device ceilings and delegate op-support as hard constraints.
- **DS-02 (Metric Specification):** fixes on-device, sustained-run measurement of every metric.
- **QA-12 (False Positives Identification):** central to the host-vs-device and CPU-fallback and single-run-vs-throttled traps.

**Related Prompts:**
- `mlopt_quantization_plan.md` — the detailed precision plan behind the largest edge lever.
- `mlopt_compression_tradeoff_analysis.md` — choose among compression families to hit the device budget.
- `mlopt_inference_latency_optimization.md` — graph/kernel levers that also help on-device.
```