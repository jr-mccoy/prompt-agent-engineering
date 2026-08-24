---
title: "Electron Multi-Window Lifecycle & Memory Management Analysis"
category: software-engineering/electron-smart-tv
description: "Analyze Electron multi-window orchestration for lifecycle correctness, memory leaks, dangling references, and proper cleanup when windows are created, hidden, and destroyed."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - DS-06  # Prioritization Guidance
difficulty: advanced
tags:
  - electron
  - window-management
  - memory-leaks
  - lifecycle
  - BrowserWindow
  - garbage-collection
updated: "2026-02-19"
related_prompts:
  - domain-software-engineering/electron-smart-tv/electron_app_performance_profiling.md
  - domain-software-engineering/analysis/performance/performance_bottleneck_identification.md
---

# Electron Multi-Window Lifecycle & Memory Management Analysis

**Objective:** Analyze Electron BrowserWindow creation, reuse, and destruction patterns across a multi-window launcher application to identify memory leaks, dangling event listeners, orphaned processes, and incorrect lifecycle management that could cause crashes or resource exhaustion during extended use.

---

## When to Use

- Use when: The app creates multiple BrowserWindows (launcher, YouTube player, Disney+ viewer) that open and close repeatedly
- Use when: Users report increasing memory usage over time or window-related crashes
- Use when: Windows are shown/hidden rather than created/destroyed and you need to verify correct cleanup
- Use when: The app is designed for long-running sessions (kids watching content for hours)
- Don't use when: The app uses a single window with in-process navigation

---

## Inputs / Context

**Required:**
- Main process file(s) containing `BrowserWindow` creation logic
- All IPC handlers that create, show, hide, or destroy windows
- Event listener registrations on BrowserWindow instances (`closed`, `ready-to-show`, `unresponsive`, etc.)

**Optional:**
- Process manager or window registry code (if windows are tracked in a Map/Set)
- Crash reporter configuration
- Memory profiling data or user-reported memory issues

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Trace every BrowserWindow from creation through destruction, identifying all references held to each instance
- Check that event listeners on destroyed windows are properly removed
- Verify that IPC channel handlers referencing specific windows handle the case where that window is already destroyed
- Identify whether windows are created once and reused, or created/destroyed on each navigation

**Must Not:**
- Assume that Electron automatically cleans up all references when a window is closed — JavaScript references to destroyed BrowserWindows persist and cause crashes if used
- Flag intentional window pooling or caching as a leak without checking if cleanup occurs
- Report memory usage from Chromium's normal multi-process model as a leak
- Ignore renderer process memory — each BrowserWindow spawns a separate renderer process

---

## Steps

1. **Map the window lifecycle graph**
   - Identify every `new BrowserWindow(...)` call and when/where it occurs
   - For each window, determine the lifecycle: created → loaded → shown → hidden → destroyed (or: created → pooled → reused → destroyed)
   - Document which user actions trigger each lifecycle transition (e.g., "user selects YouTube tile → YouTube window created")
   - Check if windows are created eagerly (at app start) or lazily (on demand)

2. **Audit reference management**
   - For each BrowserWindow instance, find all variables, arrays, Maps, Sets, or module-level references that hold it
   - After the `closed` event fires, verify that all references are set to `null` or removed from collections
   - Check for closures in IPC handlers or event callbacks that capture BrowserWindow references
   - Look for patterns where `win.webContents` is stored separately from the window reference

3. **Check event listener cleanup**
   - List all `.on()`, `.once()`, and `.addListener()` calls on each BrowserWindow and its `webContents`
   - Verify that corresponding `.removeListener()` or `.removeAllListeners()` calls exist, OR that `.once()` is used for one-time events
   - Check for listeners registered on `app`, `ipcMain`, `powerMonitor`, `screen`, or `globalShortcut` that reference specific windows
   - Look for `webContents` event listeners (`did-finish-load`, `did-fail-load`, `will-navigate`, `dom-ready`) that are not cleaned up

4. **Analyze IPC handler window coupling**
   - For IPC handlers that send messages to specific windows (e.g., `youtubeWindow.webContents.send(...)`), check that the handler verifies the window still exists
   - Look for patterns like `win.webContents.send()` without checking `win.isDestroyed()`
   - Check if IPC handlers registered for a specific window's lifecycle are removed when that window is destroyed

5. **Evaluate renderer process cleanup**
   - Check if renderer processes (visible via Task Manager as separate Electron Helper processes) terminate when their window is destroyed
   - Look for `backgroundThrottling: false` or other settings that keep hidden windows active
   - Check if `webContents.session` is shared or per-window, and whether session data accumulates

6. **CRITICAL: Verify findings before reporting**
   - Distinguish between intentional caching (window hidden for fast re-show) and actual leaks (window destroyed but references remain)
   - Check if apparent reference retention is actually mitigated by `closed` event handlers
   - Verify that Electron version-specific behavior matches your analysis (APIs differ across major versions)
   - For memory growth claims, confirm they persist across window open/close cycles, not just single measurements

7. **Prioritize findings** by impact on long-running session stability.

---

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag `BrowserWindow` references held in module scope as leaks if they are properly nulled on `closed`
- Report Chromium's multi-process overhead (each renderer is a separate process) as a memory leak
- Flag `show: false` windows as leaks — pre-creating hidden windows is a common performance optimization
- Report event listeners registered with `.once()` as needing cleanup — they self-remove after firing
- Flag window caching patterns as leaks without verifying that the cache has a size limit and cleanup logic

**DO:**
- Check that `win.on('closed', () => { win = null })` or equivalent exists for every stored reference
- Verify IPC handlers check `win.isDestroyed()` before calling `win.webContents.send()`
- Confirm that `app.on('window-all-closed', ...)` handles the expected behavior correctly for the platform
- Look for `setInterval` or `setTimeout` callbacks in the main process that reference windows without cleanup
- Check that navigation away from external content properly clears session storage and cookies if required

---

## Expected Output

### Executive Summary
Brief assessment of window lifecycle management correctness and risk of memory-related issues during extended use.

### Window Lifecycle Map
| Window | Creation Trigger | Lifecycle Pattern | Destruction Trigger | References Held |
|--------|-----------------|-------------------|--------------------|-----------------|
| ...    | ...             | ...               | ...                | ...             |

### Findings

#### Finding N: [Name]
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** `file:line`
- **Evidence:** [Code showing the reference retention or missing cleanup]
- **Impact:** [Memory growth rate, crash scenario, or resource exhaustion timeline]
- **Recommendation:** [Specific fix with code example]
- **What would change this assessment:** [Evidence that would modify severity]

### Lifecycle Diagram
```
[User Action] → [Window Created/Shown] → [Content Loaded] → [User Action] → [Window Hidden/Destroyed] → [Cleanup Verified?]
```

### Prioritized Recommendations
| # | Action | Severity | Impact on Long Sessions |
|---|--------|----------|------------------------|
| 1 | ...    | ...      | ...                    |

---

## Verification

**Quick self-check:**
- [ ] Every BrowserWindow creation point has been identified
- [ ] Every stored reference has been traced to its cleanup point
- [ ] IPC handlers that target specific windows have been checked for destroyed-window guards
- [ ] Event listener registration and removal are balanced for each window
- [ ] Findings distinguish between intentional caching and actual leaks

**High-stakes option (for long-running kids app):**
After completing the analysis:
1. If a child opens and closes YouTube 50 times in a session, will memory stabilize or grow unbounded?
2. What happens if a window's renderer process crashes — does the main process clean up correctly?
3. Are there any `setInterval` callbacks that will keep firing after their target window is destroyed?

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focuses on lifecycle correctness in multi-window Electron apps
- **ST-02 (Structured Sequential Instructions):** Systematic audit from creation through destruction
- **RT-02 (Multi-Dimensional Analysis):** Each finding covers severity, evidence, impact, and remediation
- **RT-05 (Evidence-Based Reasoning):** Requires tracing actual references and event listeners in code
- **DS-06 (Prioritization Guidance):** Ranked by impact on long-running session stability

---

## Related Prompts

- [Electron App Performance Profiling](electron_app_performance_profiling.md) - Broader performance analysis including memory
- [Performance Bottleneck Identification](../analysis/performance/performance_bottleneck_identification.md) - General performance analysis
