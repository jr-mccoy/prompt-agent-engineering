---
title: "Real-Time Systems Design & Debugging"
category: software-engineering/embedded
description: "Design, review, and debug real-time systems for timing correctness, determinism, and deadline compliance."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - CM-01
  - CM-02
  - QA-02
difficulty: advanced
tags:
  - real-time
  - rtos
  - scheduling
  - deadline
  - determinism
  - timing-analysis
  - wcet
  - rate-monotonic
updated: "2026-03-19"
---

# Real-Time Systems Design & Debugging

**Objective:** Analyze a real-time system design or implementation for timing correctness, scheduling feasibility, and deterministic behavior, then identify violations and recommend fixes to meet all deadlines.

---

## Inputs / Context

**Required:**
- **System description:** Tasks/threads with their timing requirements (period, deadline, execution time)
- **Implementation code** or **design specification:** Task definitions, ISR handlers, scheduling configuration
- **Real-time classification:** Hard real-time (deadline miss = failure) vs. soft real-time (deadline miss = degradation)

**Optional:**
- RTOS and version (FreeRTOS, Zephyr, VxWorks, QNX, RTEMS, bare-metal cyclic executive)
- Measured timing data (logic analyzer traces, RTOS trace logs, GPIO toggle measurements)
- Hardware timer configuration and tick frequency
- Shared resource inventory (peripherals, memory regions, communication channels)
- Safety integrity level (SIL, ASIL, DAL)

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Perform schedulability analysis appropriate to the scheduling algorithm in use
- Account for interrupt latency, context switch overhead, and critical section blocking
- Consider the complete priority space (ISRs + tasks) as a unified scheduling problem
- Distinguish between worst-case and average-case behavior — worst-case drives correctness

**Must Not:**
- Use average execution times for hard real-time deadline analysis
- Assume preemption is instantaneous — account for context switch cost
- Ignore the contribution of ISR handlers to CPU utilization
- Recommend over-engineering timing margins without quantifying the cost

---

## Steps

1. **Task Model Extraction**
   Build the complete task table:
   | Task | Type | Period (T) | Deadline (D) | WCET (C) | Priority | Notes |
   |------|------|-----------|-------------|----------|----------|-------|
   For each task, determine:
   - Period (for periodic tasks) or minimum inter-arrival time (for sporadic tasks)
   - Relative deadline (if different from period)
   - Worst-case execution time (measured or estimated)
   - Priority assignment basis (Rate Monotonic, Deadline Monotonic, manual)

   Include ISR handlers as highest-priority "tasks" in the model.

2. **Schedulability Analysis**
   Apply the analysis appropriate to the scheduling policy:

   **Rate Monotonic Scheduling (RMS):**
   - Compute CPU utilization: U = Σ(Ci/Ti)
   - Apply Liu & Layland bound: U ≤ n(2^(1/n) - 1)
   - If U exceeds bound, apply exact response-time analysis

   **Deadline Monotonic Scheduling (DMS):**
   - Apply response-time analysis: Ri = Ci + Σ⌈Ri/Tj⌉·Cj for all higher-priority tasks j
   - Verify Ri ≤ Di for all tasks

   **Fixed-Priority with Blocking:**
   - Include blocking term: Ri = Ci + Bi + Σ⌈Ri/Tj⌉·Cj
   - Bi = maximum blocking time from lower-priority tasks holding shared resources
   - Apply Priority Ceiling Protocol or Priority Inheritance analysis

   **Earliest Deadline First (EDF):**
   - Verify U ≤ 1.0 for feasibility (necessary and sufficient for independent tasks)
   - For tasks with shared resources, apply Stack Resource Policy analysis

   Report: Schedulable / Not Schedulable / Marginal (with utilization headroom)

3. **Timing Verification**
   For each task and ISR:
   a. **WCET Assessment:** Compare measured/estimated WCET against deadline; flag tasks where WCET/deadline ratio exceeds 0.7 (limited headroom)
   b. **Jitter Analysis:** Measure or estimate release jitter and its impact on response time
   c. **Interrupt Latency:** Calculate worst-case interrupt disable time across all critical sections
   d. **Execution Path Analysis:** Identify input-dependent execution paths that may cause WCET variation; flag paths with high variance
   e. **Timer Accuracy:** Verify system tick period, timer resolution, and drift characteristics

4. **Concurrency & Shared Resource Analysis**
   - Map all shared resources and their access patterns:
     | Resource | Accessing Tasks | Protection Mechanism | Max Hold Time |
     |----------|----------------|---------------------|---------------|
   - Verify priority ceiling or priority inheritance is correctly implemented
   - Check for priority inversion chains (transitive blocking)
   - Flag deadlock potential: circular lock dependencies, nested critical sections
   - Verify ISR-safe access patterns (no mutex acquisition from ISR context)

5. **Determinism Assessment**
   - Identify sources of non-determinism:
     - Dynamic memory allocation
     - Unbounded loops or recursive calls
     - Cache effects (cache misses in time-critical paths)
     - Branch prediction variability
     - Flash wait states and bus contention
   - For each source, assess impact on WCET and recommend mitigations
   - Check for temporal isolation between independent subsystems

6. **Debugging & Diagnosis** (if a timing problem is reported)
   - Reconstruct the failure scenario from traces/logs
   - Identify the chain of events: which task(s) missed deadlines and why
   - Check for:
     - Unexpected ISR storms (high-frequency interrupts starving tasks)
     - Priority inversion episodes
     - Lock contention spikes
     - Memory allocation stalls
     - Tick timer drift or missed ticks
   - Recommend instrumentation if insufficient data exists

7. **Synthesize & Prioritize**
   - Classify each finding: Deadline Violation / Deadline At Risk / Determinism Issue / Design Improvement
   - Provide specific fixes with expected timing impact

---

## False-Positive Prevention

- ❌ Do NOT flag soft real-time tasks for occasional deadline misses if the system design accounts for it
- ❌ Do NOT require WCET analysis for non-time-critical background tasks
- ❌ Do NOT flag high CPU utilization alone — 85% utilization is fine if schedulability analysis passes
- ❌ Do NOT flag cooperative scheduling as inferior — it is appropriate for many embedded systems
- ✅ DO flag hard real-time tasks without WCET bounds
- ✅ DO flag shared resources accessed without priority inversion protection
- ✅ DO flag ISR handlers that disable interrupts for more than the documented latency budget
- ✅ DO flag dynamic memory allocation in time-critical paths

---

## Output Format

### System Timing Model
```
Scheduling Policy: [RMS / DMS / EDF / Cyclic Executive / Custom]
System Tick: [frequency]
CPU Utilization: [X%] (bound: [Y%])
Schedulability: [PASS / FAIL / MARGINAL]
Tasks: [N] | ISRs: [M]
```

### Task Schedule Analysis
| Task | T (ms) | D (ms) | C (ms) | Priority | Response Time | Slack | Status |
|------|--------|--------|--------|----------|--------------|-------|--------|
| [name] | [period] | [deadline] | [WCET] | [priority] | [R ms] | [ms] | ✅/⚠️/❌ |

### Critical Findings
For each:
- **ID:** RT-CRIT-[N]
- **Type:** [Deadline Violation | Priority Inversion | Determinism | Race Condition]
- **Affected Task(s):** [names]
- **Evidence:** [timing trace, calculation, or code path]
- **Impact:** [missed deadline by X ms / blocking for Y ms / non-deterministic path]
- **Root Cause:** [detailed explanation]
- **Fix:** [specific changes with expected timing improvement]

### Shared Resource Map
| Resource | Tasks | Protocol | Max Block (ms) | Risk |
|----------|-------|----------|----------------|------|
| [name] | [task list] | [PCP/PI/disable-IRQ/none] | [time] | [OK/HIGH] |

### Recommendations
| Priority | Action | Expected Impact | Effort |
|----------|--------|----------------|--------|
| Critical | [action] | [timing improvement] | [estimate] |

---

## Verification

After completing the analysis, explicitly answer:
1. Did I include ISR execution time in the total CPU utilization and response-time calculations?
2. Did I use worst-case (not average) execution times for all hard real-time deadline analysis?
3. Did I verify shared resource blocking is accounted for in the scheduling analysis?
4. Did I check for transitive priority inversion chains, not just direct blocking?

---

**Techniques Used:** ST-01 (Clear Objective), ST-02 (Structured Sequential), RT-02 (Multi-Dimensional Analysis), RT-05 (Evidence-Based), DS-06 (Prioritization), CM-01 (Context Framing), CM-02 (Constraints), QA-02 (Adversarial Stress-Test)
