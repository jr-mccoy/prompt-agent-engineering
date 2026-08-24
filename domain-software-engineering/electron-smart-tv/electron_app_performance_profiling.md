---
title: "Electron App Performance & Startup Profiling"
category: software-engineering/electron-smart-tv
description: "Profile an Electron smart TV launcher for startup latency, renderer performance, main-process bottlenecks, and memory consumption patterns that affect the experience on low-powered TV hardware."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - DS-06  # Prioritization Guidance
difficulty: intermediate
tags:
  - electron
  - performance
  - startup-time
  - memory-profiling
  - renderer-performance
  - tv-hardware
updated: "2026-02-19"
related_prompts:
  - domain-software-engineering/electron-smart-tv/electron_multi_window_lifecycle_analysis.md
  - domain-software-engineering/analysis/performance/performance_bottleneck_identification.md
---

# Electron App Performance & Startup Profiling

**Objective:** Identify performance bottlenecks in an Electron-based smart TV launcher across app startup, renderer paint, window transitions, and sustained memory consumption, with attention to constraints of low-powered TV hardware (limited CPU, slow storage, 1–2 GB RAM).

---

## When to Use

- Use when: The launcher feels slow to start or transitions between screens lag
- Use when: Targeting deployment on embedded TV hardware, mini PCs, or Raspberry Pi-class devices
- Use when: Adding new features (more channels, richer UI) and need to verify performance budget
- Use when: Memory usage grows over multi-hour sessions (kids watching all day)
- Don't use when: Performance issues are clearly network-related (API latency, slow video loading)

---

## Inputs / Context

**Required:**
- Main process entry point (`main.js`) — startup sequence, window creation, module loading
- Renderer HTML/CSS/JS for the launcher and content views
- Cache manager module (affects startup if it loads/parses a large JSON file)
- Target hardware specs (or "desktop development" if profiling on dev machine)

**Optional:**
- Electron version and Chromium version (affects available performance APIs)
- Performance traces (Chrome DevTools Performance tab recordings)
- Memory snapshots (Chrome DevTools Memory tab)
- `package.json` to review dependency weight

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Measure or estimate startup time from app launch to first interactive paint (launcher tiles are focusable)
- Profile both main process (Node.js) and renderer process (Chromium) separately
- Identify the top 3 contributors to startup latency and the top 3 memory consumers
- Consider the performance envelope of target hardware, not just developer workstations

**Must Not:**
- Report Electron/Chromium baseline memory usage (~80–150 MB per renderer) as a leak — that is the framework's cost
- Recommend micro-optimizations (shaving milliseconds) when there are larger structural issues
- Suggest replacing Electron for performance reasons without quantifying the actual bottleneck
- Ignore the cache manager's JSON parse/serialize cost — for 500 MB cache files, this is significant

---

## Steps

1. **Profile the startup critical path**
   - Trace the sequence from `app.ready` to first `BrowserWindow` showing content:
     1. Main process initialization (module loading, environment config, dotenv parse)
     2. Cache manager initialization (file read, JSON parse, index construction)
     3. `BrowserWindow` creation (webPreferences setup, preload script evaluation)
     4. Renderer load (`launcher.html` → DOM parse → CSS paint → JS execution → first interactive)
   - For each phase, identify: sync vs async, blocking duration, opportunity to defer
   - Check if `require()` calls in main process load heavy dependencies synchronously before the window opens

2. **Analyze renderer painting and layout**
   - Check if the launcher UI triggers layout thrashing (read-write-read cycles on DOM)
   - Verify images are appropriately sized (not loading 1080p thumbnails for 200px tiles)
   - Check CSS for expensive properties in animated elements: `box-shadow`, `filter`, `backdrop-filter`
   - Verify font loading doesn't cause layout shift (FOUT/FOIT)
   - Check if spatial navigation polyfill adds per-frame overhead

3. **Measure window transition performance**
   - Profile the time from "user selects YouTube tile" to "YouTube content is visible and interactive"
   - Check if new windows are created on demand (slow) or pre-created and shown (fast but memory-heavy)
   - Measure the overhead of IPC round-trips during window transitions
   - Check for synchronous IPC (`ipcRenderer.sendSync`) that blocks the renderer

4. **Audit memory consumption patterns**
   - Baseline: Measure memory with just the launcher open (no content windows)
   - Active: Measure with launcher + YouTube window + content loaded
   - Sustained: Estimate memory after 2 hours of use (opening/closing content repeatedly)
   - Check for unbounded growth: event listener accumulation, cache growth without eviction, DOM node accumulation in content views
   - Identify the renderer with highest memory usage and its top allocations

5. **Evaluate dependency weight**
   - Check `node_modules` footprint — large dependencies increase startup time
   - Identify dependencies loaded in main process that could be lazy-loaded
   - Check if `dotenv`, YouTube API clients, or cache manager load transitive dependencies that bloat startup
   - Verify that development-only dependencies are not bundled in production

6. **CRITICAL: Verify findings before reporting**
   - Performance measurements on developer machines (fast SSDs, 16+ GB RAM) do NOT represent TV hardware
   - If profiling on dev hardware, apply scaling factors: 3–5x CPU, 10x storage I/O for typical TV hardware
   - Check that reported bottlenecks are in hot paths, not one-time initialization
   - Verify that memory growth is sustained across multiple cycles, not just transient allocation spikes

7. **Prioritize findings** by user-perceived impact: startup time > window transitions > sustained memory > background overhead.

---

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag Electron's inherent multi-process memory overhead as a bug — each renderer uses 80–150 MB baseline
- Report one-time startup costs as ongoing performance issues
- Flag `JSON.parse()` as slow without measuring the actual file size it parses
- Report async operations as "blocking" when they correctly use non-blocking I/O
- Suggest removing features for performance when lazy loading or deferral would suffice

**DO:**
- Distinguish between main process blocking (freezes all windows) and renderer blocking (freezes one window)
- Measure actual JSON parse time for the cache file at its expected steady-state size
- Check if `BrowserWindow.show()` is called before `ready-to-show` fires (causes white flash)
- Verify that background refresh timers don't fire during startup (competing for CPU)
- Profile with `--enable-logging` and `ELECTRON_ENABLE_STACK_DUMPING` for accurate timing

---

## Expected Output

### Executive Summary
Brief assessment of performance posture with estimated startup time and memory envelope.

### Startup Critical Path
| Phase | Duration (est.) | Blocking? | Deferrable? | Notes |
|-------|----------------|-----------|-------------|-------|
| Module loading | ... | ... | ... | ... |
| Cache init | ... | ... | ... | ... |
| Window creation | ... | ... | ... | ... |
| Renderer paint | ... | ... | ... | ... |
| **Total to interactive** | **...** | | | |

### Findings

#### Finding N: [Name]
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** `file:line`
- **Evidence:** [Measurement, code pattern, or trace data]
- **Impact:** [Quantified: ms added to startup, MB consumed, frames dropped]
- **Recommendation:** [Specific optimization with expected improvement]
- **What would change this assessment:** [E.g., "If cache file is <10 MB, impact is negligible"]

### Memory Budget
| Component | Baseline (MB) | Active (MB) | After 2hrs (MB) | Growth? |
|-----------|---------------|-------------|-----------------|---------|
| Main process | ... | ... | ... | ... |
| Launcher renderer | ... | ... | ... | ... |
| YouTube renderer | ... | ... | ... | ... |
| Cache file (disk) | ... | ... | ... | ... |

### Prioritized Recommendations
| # | Action | Impact | Effort | User-Perceived Improvement |
|---|--------|--------|--------|---------------------------|
| 1 | ...    | ...    | ...    | ...                       |

---

## Verification

**Quick self-check:**
- [ ] Startup critical path identified with blocking/non-blocking classification
- [ ] Both main and renderer process performance assessed
- [ ] Memory consumption analyzed for baseline, active, and sustained scenarios
- [ ] Findings include quantified impact, not just qualitative descriptions
- [ ] Hardware scaling considerations mentioned for TV deployment targets

**High-stakes option (for TV hardware deployment):**
After completing analysis:
1. What is the estimated startup time on a device with 1/5th the CPU and eMMC storage (typical smart TV)?
2. If total system RAM is 2 GB, how many concurrent windows can the app support?
3. Will the JSON cache parse time be acceptable on slow storage as the cache approaches 500 MB?

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Targets Electron-specific performance bottlenecks for TV deployment
- **ST-02 (Structured Sequential Instructions):** Systematic profiling from startup through sustained use
- **RT-02 (Multi-Dimensional Analysis):** Startup, rendering, memory, transitions, dependencies
- **RT-05 (Evidence-Based Reasoning):** Requires measurements or estimates, not subjective impressions
- **DS-06 (Prioritization Guidance):** Ranked by user-perceived impact

---

## Related Prompts

- [Multi-Window Lifecycle & Memory Management Analysis](electron_multi_window_lifecycle_analysis.md) - Deep dive into window-specific memory issues
- [Performance Bottleneck Identification](../analysis/performance/performance_bottleneck_identification.md) - General performance analysis
