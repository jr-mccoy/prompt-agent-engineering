---
name: android-adb-profiling
description: "ADB-based performance profiling workflows for CPU, memory, battery, network, and GPU rendering. Covers systrace/perfetto capture, dumpsys analysis, startup time measurement, and StrictMode configuration — all from the command line without Android Studio Profiler. Use this skill when profiling app performance, investigating jank, measuring startup time, debugging memory leaks, analyzing battery drain, or when a developer mentions 'dumpsys', 'systrace', 'perfetto', 'jank', 'frame drops', or 'memory leak'."
metadata:
  tags:
    - android
    - adb
    - performance
    - profiling
    - solo-developer
  updated: "2026-03-06"
---

# Android ADB Profiling

ADB-based performance profiling workflows that run entirely from the command line. Covers CPU profiling, memory analysis, battery impact measurement, network monitoring, GPU rendering analysis, and startup time benchmarking — all without requiring Android Studio Profiler.

## Purpose

Performance profiling is critical for shipping smooth Android apps, but most developers only profile when they notice visible jank — by then, the problem is often deeply embedded. ADB-based profiling is scriptable, runs from the terminal, works over wireless debugging, and can be integrated into CI pipelines. For solo developers, terminal-based profiling means you do not need Android Studio consuming RAM alongside your app.

## When to Use This Skill

Use this skill when you need to:
- Measure app startup time (cold, warm, hot start)
- Investigate UI jank or dropped frames
- Profile CPU usage during specific operations
- Debug memory leaks or high memory consumption
- Analyze battery impact of your app
- Monitor network usage patterns
- Capture systrace/perfetto traces for detailed analysis
- Benchmark before and after optimization changes

## When NOT to Use This Skill

Do NOT use this skill when:
- You need basic ADB operations (use `android-adb-operations` skill)
- You are investigating a crash (use `android-crash-triage` skill)
- You need to set up profiling infrastructure from scratch in Android Studio
- You need Macrobenchmark/Microbenchmark library setup (use `android-testing-patterns` skill)

## Prerequisites

- ADB connected to target device or emulator
- App installed and runnable on the device
- For Perfetto: Android 10+ (API 29+)
- For systrace: Android SDK platform-tools
- For battery profiling: device with battery (not emulator)

## Step 1: Startup Time Measurement

### 1.1 Basic Startup Timing

```bash
# Cold start (app killed, process not in memory)
adb shell am force-stop com.example.myapp
adb shell am start -W -n com.example.myapp/.MainActivity
# Output: TotalTime: XXX ms — this is your cold start time

# Warm start (app in background, process alive)
adb shell input keyevent KEYCODE_HOME
adb shell am start -W -n com.example.myapp/.MainActivity
# Output: TotalTime: XXX ms — warm start

# Hot start (activity in memory, just brought to front)
adb shell input keyevent KEYCODE_HOME
adb shell am start -W -n com.example.myapp/.MainActivity
# Output: TotalTime: XXX ms — should be near-instant
```

### 1.2 Startup Time Targets

| Start Type | Target | Acceptable | Needs Work |
|-----------|--------|------------|------------|
| Cold | <500ms | <1000ms | >1500ms |
| Warm | <200ms | <500ms | >800ms |
| Hot | <100ms | <200ms | >500ms |

### 1.3 Repeated Measurement Script

```bash
# Run 5 cold starts and average
for i in {1..5}; do
    adb shell am force-stop com.example.myapp
    sleep 2
    adb shell am start -W -n com.example.myapp/.MainActivity 2>/dev/null | grep TotalTime
done
```

## Step 2: CPU Profiling

### 2.1 Quick CPU Check

```bash
# See CPU usage by process
adb shell top -n 1 | grep -i "example"

# Detailed CPU info
adb shell dumpsys cpuinfo | head -30

# CPU usage for specific app
adb shell dumpsys cpuinfo | grep "com.example.myapp"
```

### 2.2 Method Tracing

```bash
# Start method tracing (records all method calls)
adb shell am profile start com.example.myapp /data/local/tmp/trace.trace

# Perform the action you want to profile (in the app)

# Stop tracing
adb shell am profile stop com.example.myapp

# Pull the trace file
adb pull /data/local/tmp/trace.trace ./
# Open in Android Studio: File → Open → trace.trace
```

### 2.3 Simpleperf (CPU Sampling)

```bash
# Record CPU samples for 10 seconds (app must be debuggable)
adb shell run-as com.example.myapp simpleperf record -p $(adb shell pidof -s com.example.myapp) --duration 10 -o /data/local/tmp/perf.data

# Pull and analyze
adb pull /data/local/tmp/perf.data ./
# Use simpleperf report locally or open in Android Studio
```

## Step 3: Memory Analysis

### 3.1 Quick Memory Check

```bash
# Memory summary for your app
adb shell dumpsys meminfo com.example.myapp

# Key metrics to watch:
# - TOTAL PSS: Total physical memory used
# - Java Heap: Managed heap usage
# - Native Heap: Native allocations (images, NDK)
# - Graphics: GPU memory for textures/buffers
```

### 3.2 Memory Targets

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Total PSS | <150MB | 150-300MB | >300MB |
| Java Heap | <64MB | 64-128MB | Near dalvik.vm.heapsize |
| Native Heap | <50MB | 50-100MB | >100MB, likely image leak |

### 3.3 Memory Over Time

```bash
# Track memory every 5 seconds (watch for growth = leak)
while true; do
    echo "$(date +%H:%M:%S) $(adb shell dumpsys meminfo com.example.myapp | grep 'TOTAL PSS' | awk '{print $3}') KB"
    sleep 5
done
```

### 3.4 Heap Dump

```bash
# Capture heap dump for analysis
adb shell am dumpheap com.example.myapp /data/local/tmp/heap.hprof

# Pull and convert
adb pull /data/local/tmp/heap.hprof ./

# Convert to standard HPROF format (if needed)
hprof-conv heap.hprof heap-std.hprof
# Open in Android Studio Memory Profiler or Eclipse MAT
```

### 3.5 Procstats (Long-Term Memory)

```bash
# Memory usage over time (background behavior)
adb shell dumpsys procstats --hours 3 com.example.myapp

# Shows: PSS min/avg/max, how often app is in memory, background behavior
# Key insight: if background PSS is high, app is consuming memory when inactive
```

## Step 4: GPU Rendering and Jank Detection

### 4.1 GPU Rendering Stats

```bash
# Enable GPU rendering stats collection
adb shell setprop debug.hwui.profile true

# Get frame rendering times
adb shell dumpsys gfxinfo com.example.myapp

# Key section: "Total frames rendered: X"
# "Janky frames: Y (Z%)" — target: <5% janky frames
# "Number Missed Vsync: N" — frames that missed the 16ms deadline
```

### 4.2 Frame Stats Reset and Measure

```bash
# Reset stats
adb shell dumpsys gfxinfo com.example.myapp reset

# Perform the UI action you want to measure

# Read stats
adb shell dumpsys gfxinfo com.example.myapp

# Look at framestats section for per-frame timing
```

### 4.3 Jank Targets

| Metric | Target | Acceptable | Needs Work |
|--------|--------|------------|------------|
| Janky frames | <5% | 5-10% | >10% |
| 90th percentile frame time | <16ms | 16-32ms | >32ms |
| 99th percentile frame time | <32ms | 32-48ms | >48ms |

### 4.4 Profile GPU Rendering Bars

```bash
# Enable visual bars on device (colored bars at bottom of screen)
adb shell setprop debug.hwui.overdraw show
adb shell setprop debug.hwui.profile visual_bars

# Green line = 16ms target. Bars above the line = janky frames.
# Color meaning: blue=draw, purple=prepare, green=process, red=swap

# Disable when done
adb shell setprop debug.hwui.overdraw false
adb shell setprop debug.hwui.profile false
```

## Step 5: Battery Profiling

### 5.1 Battery Stats

```bash
# Reset battery stats
adb shell dumpsys batterystats --reset

# Use the app normally for 15-30 minutes (unplug from USB for accurate results)
# Or use wireless ADB to monitor while unplugged

# Capture battery stats
adb shell dumpsys batterystats > battery_stats.txt

# Key metrics:
adb shell dumpsys batterystats | grep "com.example.myapp" | head -20
# Look for: Uid, wake locks, wifi/network usage, alarms, GPS usage
```

### 5.2 Battery Historian

```bash
# Capture bug report for Battery Historian
adb bugreport bugreport.zip

# Upload bugreport.zip to Battery Historian:
# https://bathist.ef.lc/ (or run locally with Docker)
# docker run -p 9999:9999 gcr.io/anthropic-battery-historian/anthropic-battery-historian
```

### 5.3 Wake Lock Analysis

```bash
# Check for wake locks (major battery drain cause)
adb shell dumpsys power | grep "Wake Locks"

# Detailed wake lock info
adb shell dumpsys batterystats | grep "Wake lock"

# Your app should have zero long-held wake locks
# If you see your package holding wake locks for >10 seconds, investigate
```

### 5.4 Doze Mode Testing

```bash
# Force device into Doze mode (test background behavior)
adb shell dumpsys deviceidle force-idle

# Check if app is whitelisted (should NOT be unless justified)
adb shell dumpsys deviceidle whitelist

# Exit Doze mode
adb shell dumpsys deviceidle unforce

# Test that your app handles Doze correctly:
# - No crashes on wake
# - Deferred work executes after Doze exits
# - No excessive alarms during Doze
```

## Step 6: Network Monitoring

```bash
# Network usage by UID
adb shell dumpsys netstats detail | grep "com.example.myapp" -A 5

# Active network connections
adb shell cat /proc/net/tcp

# DNS resolution test
adb shell ping -c 1 your-api.example.com

# Simulate slow network (requires root)
# Alternatively, use Chrome DevTools network throttling or emulator settings
```

## Step 7: Systrace / Perfetto

### 7.1 Perfetto (Android 10+, Recommended)

```bash
# Quick 10-second trace
adb shell perfetto -o /data/misc/perfetto-traces/trace.perfetto-trace -t 10s sched freq idle am wm gfx view binder_driver hal dalvik camera input res memory

# Pull trace
adb pull /data/misc/perfetto-traces/trace.perfetto-trace ./

# Open at https://ui.perfetto.dev/
```

### 7.2 Systrace (Older devices)

```bash
# Capture systrace (from platform-tools)
python $ANDROID_HOME/platform-tools/systrace/systrace.py \
    --time=5 \
    -o trace.html \
    gfx view wm am dalvik input sched freq

# Open trace.html in Chrome
```

### 7.3 Custom Trace Sections

Add custom sections in your Kotlin code to appear in traces:

```kotlin
import android.os.Trace

Trace.beginSection("MyApp:loadData")
// ... your code ...
Trace.endSection()
```

Then capture with `am` or `gfx` category enabled.

## Step 8: StrictMode Configuration

```bash
# StrictMode is configured in code, not ADB, but ADB helps detect violations:
adb logcat -s StrictMode

# Enable in your Application.onCreate() for debug builds:
```

```kotlin
if (BuildConfig.DEBUG) {
    StrictMode.setThreadPolicy(
        StrictMode.ThreadPolicy.Builder()
            .detectDiskReads()
            .detectDiskWrites()
            .detectNetwork()
            .penaltyLog()       // Log violations
            // .penaltyDeath()  // Crash on violation (aggressive)
            .build()
    )
    StrictMode.setVmPolicy(
        StrictMode.VmPolicy.Builder()
            .detectLeakedClosableObjects()
            .detectLeakedSqlLiteObjects()
            .detectActivityLeaks()
            .penaltyLog()
            .build()
    )
}
```

## Profiling Cheat Sheet

| What to Measure | Command |
|----------------|---------|
| Cold start time | `adb shell am force-stop pkg && adb shell am start -W -n pkg/.Activity` |
| Memory usage | `adb shell dumpsys meminfo pkg` |
| Frame jank % | `adb shell dumpsys gfxinfo pkg` |
| CPU usage | `adb shell dumpsys cpuinfo \| grep pkg` |
| Battery impact | `adb shell dumpsys batterystats \| grep pkg` |
| Heap dump | `adb shell am dumpheap pkg /data/local/tmp/heap.hprof` |
| Perfetto trace | `adb shell perfetto -o /data/misc/perfetto-traces/trace -t 10s sched gfx view` |
| Wake locks | `adb shell dumpsys power \| grep "Wake Locks"` |
| Network stats | `adb shell dumpsys netstats detail \| grep pkg` |

## Related Skills

- `android-adb-operations` — Base ADB commands this skill builds on
- `android-crash-triage` — When profiling reveals crash-inducing conditions
- `android-testing-patterns` — Macrobenchmark and Microbenchmark library setup
- `android-emulator-management` — Emulator configuration for profiling
