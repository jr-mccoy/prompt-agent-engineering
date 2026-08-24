---
title: "Arduino & Raspberry Pi Development Workflow Analysis"
category: software-engineering/embedded
description: "Review and optimize Arduino and Raspberry Pi projects for reliability, power efficiency, and production readiness."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - CM-01
  - QA-01
difficulty: intermediate
tags:
  - arduino
  - raspberry-pi
  - embedded
  - microcontroller
  - prototyping
  - gpio
  - hardware
updated: "2026-03-19"
---

# Arduino & Raspberry Pi Development Workflow Analysis

**Objective:** Analyze an Arduino or Raspberry Pi project for correctness, reliability, power management, and production readiness, then provide prioritized recommendations for improvement.

---

## Inputs / Context

**Required:**
- **Source code:** The sketch (.ino), Python script, or C/C++ project files
- **Platform:** Arduino (specify board: Uno, Mega, ESP32, etc.) or Raspberry Pi (specify model and OS)
- **Project purpose:** What the device does (e.g., "temperature monitor that logs to SD card every 5 minutes")

**Optional:**
- Hardware schematic or wiring description
- Power source (USB, battery, solar, mains)
- Deployment environment (indoor, outdoor, industrial)
- Required uptime / reliability targets

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Verify pin assignments match the target board's capabilities (PWM, ADC, interrupt-capable pins)
- Check for blocking calls in time-sensitive loops
- Assess memory usage against board limits (SRAM, flash, heap fragmentation)
- Evaluate power management if battery-operated

**Must Not:**
- Assume all Arduino-compatible boards have identical pin mappings or peripherals
- Recommend libraries without verifying board compatibility
- Ignore watchdog timer considerations for long-running deployments

---

## Steps

1. **Platform & Hardware Assessment**
   - Identify the target board and its resource constraints (CPU speed, SRAM, flash, GPIO count)
   - Map declared pin usage against board pinout; flag conflicts (e.g., using SPI pins for GPIO)
   - Verify library compatibility with the specific board variant

2. **Code Quality & Correctness Review**
   For each source file, analyze across these dimensions:
   a. **Timing & Blocking:** Identify `delay()` calls, blocking loops, or long ISR handlers that could cause missed events
   b. **Memory Safety:** Check for buffer overflows, unbounded string concatenation, heap fragmentation, stack overflow risk
   c. **Peripheral Usage:** Verify correct initialization sequence, proper use of interrupts, I2C/SPI bus contention
   d. **Error Handling:** Assess what happens when sensors fail, communication drops, or SD cards are removed
   e. **Concurrency:** For Raspberry Pi — check for race conditions in multi-threaded GPIO access; for Arduino — check ISR safety (volatile variables, atomic operations)

3. **Power & Deployment Analysis**
   - Calculate estimated power draw based on active peripherals
   - Identify sleep mode opportunities (light sleep, deep sleep, peripheral power gating)
   - Assess boot time and recovery behavior after power loss
   - Check for graceful degradation when resources are constrained

4. **Production Readiness Evaluation**
   - Evaluate OTA update capability or update strategy
   - Check for hardcoded credentials, debug serial output left enabled, or test-only code
   - Assess logging strategy (SD card rotation, remote logging, buffer limits)
   - Review watchdog timer usage for crash recovery

5. **Synthesize & Prioritize**
   - Rank all findings by severity: Critical / High / Medium / Low
   - Group recommendations into: Immediate Fixes, Next Iteration, Nice-to-Have

---

## False-Positive Prevention

- ❌ Do NOT flag `delay()` in one-time `setup()` functions where blocking is acceptable
- ❌ Do NOT flag missing sleep modes for USB-powered bench prototypes
- ❌ Do NOT require enterprise-grade error handling for learning/hobby projects unless user requests production readiness
- ✅ DO flag `delay()` inside `loop()` when the project needs to handle interrupts or concurrent sensor reads
- ✅ DO flag missing `volatile` on variables shared between ISR and main loop
- ✅ DO verify actual board SRAM limits before flagging memory concerns

---

## Output Format

### Platform Summary
| Property | Value |
|----------|-------|
| Board | [board name] |
| CPU / Clock | [details] |
| SRAM / Flash | [available vs. used] |
| Pin Usage | [X of Y GPIO used] |

### Critical Findings
For each finding:
- **Location:** [file:line]
- **Issue:** [description]
- **Impact:** [what goes wrong]
- **Fix:** [specific recommendation with code example]

### Power Analysis
- Estimated active draw: [mA]
- Sleep opportunity: [description]
- Battery life estimate: [if applicable]

### Production Readiness Checklist
- [ ] Watchdog timer configured
- [ ] Debug output disabled / gated
- [ ] Credentials externalized
- [ ] OTA update path defined
- [ ] Power-loss recovery tested
- [ ] Memory usage within safe margins (< 80% SRAM)

### Recommended Actions
| Priority | Action | Effort |
|----------|--------|--------|
| Critical | [action] | [estimate] |
| High | [action] | [estimate] |
| Medium | [action] | [estimate] |

---

## Verification

After completing the analysis, explicitly answer:
1. Did I verify pin assignments against the actual board datasheet, not generic Arduino assumptions?
2. Did I check memory usage against the specific board's SRAM limit?
3. Did I distinguish between prototype-appropriate and production-inappropriate patterns?

---

**Techniques Used:** ST-01 (Clear Objective), ST-02 (Structured Sequential), RT-02 (Multi-Dimensional Analysis), RT-05 (Evidence-Based), DS-06 (Prioritization), CM-01 (Context Framing), QA-01 (Verification)
