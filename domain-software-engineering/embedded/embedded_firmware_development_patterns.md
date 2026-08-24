---
title: "Firmware Development Pattern Analysis"
category: software-engineering/embedded
description: "Analyze firmware code for bare-metal and RTOS projects, identifying architectural issues, timing problems, and reliability risks."
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
  - firmware
  - bare-metal
  - rtos
  - freertos
  - zephyr
  - embedded-c
  - real-time
  - microcontroller
updated: "2026-03-19"
---

# Firmware Development Pattern Analysis

**Objective:** Review firmware source code (bare-metal or RTOS-based) for architectural soundness, timing correctness, memory safety, and adherence to embedded best practices, then deliver prioritized findings with concrete fixes.

---

## Inputs / Context

**Required:**
- **Firmware source code:** C/C++ files, headers, linker scripts, and build configuration
- **Target MCU:** Manufacturer, family, and part number (e.g., STM32F407VG, nRF52840, ESP32-S3)
- **Execution model:** Bare-metal (super-loop, interrupt-driven) or RTOS (FreeRTOS, Zephyr, ThreadX, etc.)

**Optional:**
- Hardware abstraction layer (HAL) in use (vendor HAL, CMSIS, custom)
- Memory map or linker script
- Timing requirements (interrupt latency budgets, task deadlines)
- Safety/certification targets (IEC 61508, MISRA C, AUTOSAR)

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Analyze against the specific MCU's memory layout, peripheral set, and interrupt priority scheme
- Distinguish between hard real-time and soft real-time requirements
- Verify stack sizing for each task/thread if RTOS is used
- Check interrupt priority inversion risks

**Must Not:**
- Apply desktop C/C++ conventions blindly (e.g., dynamic allocation patterns that are unsafe on MCUs)
- Assume a specific compiler without checking (GCC ARM, IAR, Keil may produce different behaviors)
- Recommend `malloc`/`free` in bare-metal or safety-critical contexts without explicit justification

---

## Steps

1. **Architecture Assessment**
   - Identify the firmware architecture pattern: super-loop, interrupt-driven, cooperative scheduler, preemptive RTOS
   - Map the module/layer structure: HAL → drivers → middleware → application
   - Check for proper separation between hardware-dependent and hardware-independent code
   - Verify startup sequence: clock configuration, peripheral initialization order, RTOS kernel start

2. **Memory Analysis**
   - Calculate static memory usage (`.bss`, `.data`, `.rodata`, `.text`) vs. available flash/RAM
   - For RTOS: verify stack allocation per task against worst-case depth (account for ISR stacking)
   - Check for heap usage and fragmentation risk; flag unbounded allocations
   - Verify linker script correctness: section placement, stack/heap region sizing, MPU region alignment
   - Check for uninitialized variable access and missing `volatile` qualifiers

3. **Timing & Concurrency Review**
   For each interrupt handler and RTOS task:
   a. **ISR Analysis:** Measure worst-case execution time; flag handlers that exceed recommended limits; verify they defer work to tasks/bottom-halves appropriately
   b. **Priority Scheme:** Check for priority inversion; verify mutex/semaphore usage protects shared resources; confirm interrupt nesting configuration
   c. **Shared State Protection:** Verify critical sections, atomic operations, or RTOS primitives protect all shared data; flag bare global variables accessed from multiple contexts
   d. **Deadlock Risk:** Trace lock acquisition order across tasks; flag circular dependencies
   e. **Timing Guarantees:** Verify periodic tasks meet their deadlines; check timer configuration accuracy

4. **Peripheral & Driver Review**
   - Verify peripheral clock enabling before register access
   - Check DMA configuration: buffer alignment, cache coherency (on Cortex-M7+), circular vs. normal mode
   - Validate GPIO configuration: alternate function mapping, pull-up/pull-down, drive strength
   - Review communication bus setup: baud rate derivation, error handling, timeout mechanisms

5. **Robustness & Safety**
   - Assess watchdog timer configuration and feeding strategy
   - Check fault handler implementations (HardFault, MemManage, BusFault, UsageFault)
   - Verify brown-out detection and graceful shutdown paths
   - Review MISRA C compliance if safety-critical (or flag where MISRA adherence would help)
   - Check for defensive programming: assertions, parameter validation at module boundaries, stack canaries

6. **Build & Toolchain Review**
   - Verify compiler optimization level appropriateness (-O0 for debug, -Os/-O2 for release)
   - Check warning flags: `-Wall -Wextra -Werror` should be enabled
   - Verify that `volatile` is used on all hardware register accesses and ISR-shared variables
   - Check for undefined behavior: signed overflow, strict aliasing violations, unaligned access

7. **Synthesize & Prioritize**
   - Rank findings: Critical (crash/data corruption/safety) → High (reliability/timing) → Medium (maintainability) → Low (style/convention)
   - Provide specific code fixes for Critical and High findings

---

## False-Positive Prevention

- ❌ Do NOT flag missing dynamic memory management — static allocation is often the correct pattern
- ❌ Do NOT flag `goto` in error-cleanup paths — this is idiomatic and recommended in embedded C
- ❌ Do NOT flag vendor HAL inefficiencies unless user asks for HAL optimization
- ❌ Do NOT flag MISRA violations unless user specifies safety-critical or MISRA compliance targets
- ✅ DO flag missing `volatile` on hardware registers and ISR-shared variables
- ✅ DO flag ISR handlers that call non-reentrant functions (printf, malloc, etc.)
- ✅ DO flag stack sizes that leave less than 20% headroom against estimated worst-case
- ✅ DO flag priority inversion scenarios with concrete execution traces

---

## Output Format

### Firmware Architecture Overview
```
Architecture: [super-loop / RTOS (name + version)]
Target MCU: [part number]
Compiler: [toolchain + version]
Memory: [X KB flash used / Y KB total] | [X KB RAM used / Y KB total]
Tasks/Threads: [count with names and priorities]
ISRs: [count with priorities]
```

### Critical Findings
For each:
- **ID:** FW-CRIT-[N]
- **Location:** [file:line]
- **Category:** [Memory Safety | Timing | Concurrency | Peripheral | Safety]
- **Issue:** [description]
- **Impact:** [what fails and when]
- **Evidence:** [specific code or execution trace]
- **Fix:** [code diff or detailed instructions]

### High-Priority Findings
[Same format as Critical]

### Medium/Low Findings
[Abbreviated format: location, issue, recommendation]

### Memory Budget
| Region | Used | Available | Utilization |
|--------|------|-----------|-------------|
| Flash (.text + .rodata) | | | |
| RAM (.data + .bss) | | | |
| Heap | | | |
| Stack (per task) | | | |

### Task/ISR Timing Summary
| Context | Priority | WCET Estimate | Deadline | Status |
|---------|----------|---------------|----------|--------|
| [task/ISR name] | [priority] | [time] | [time] | OK / AT RISK / VIOLATED |

### Recommended Actions
| Priority | Action | Category | Effort |
|----------|--------|----------|--------|
| Critical | [action] | [category] | [estimate] |

---

## Verification

After completing the analysis, explicitly answer:
1. Did I verify findings against the specific MCU's reference manual, not generic ARM assumptions?
2. Did I trace actual execution paths for concurrency findings rather than flagging patterns alone?
3. Did I account for compiler-specific behavior where relevant?
4. For RTOS findings — did I verify against the specific RTOS API semantics (e.g., FreeRTOS vs. Zephyr differences)?

---

**Techniques Used:** ST-01 (Clear Objective), ST-02 (Structured Sequential), RT-02 (Multi-Dimensional Analysis), RT-05 (Evidence-Based), DS-06 (Prioritization), CM-01 (Context Framing), CM-02 (Constraints), QA-02 (Adversarial Stress-Test)
