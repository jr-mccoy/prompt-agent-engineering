---
name: android_adb_health_check
description: Quick device and app health check via ADB. Captures device state, app memory usage, running services, battery impact, and recent crash logs in a single report. Designed to run in under 60 seconds.
version: "1.0.0"
category: mobile-development
tags: [android, adb, health-check, debugging, solo-developer]
agents_used: [android-adb-specialist, mobile-developer]
---

Quick device and app health check via ADB that produces a single-page report in under 60 seconds:

[Extended thinking: Solo developers often start a testing session by running 5-10 separate ADB commands to check device state, app version, memory usage, and recent errors. This command automates that entire pre-testing ritual into a single invocation. Phase 1 checks device state (connected, battery, storage). Phase 2 checks app state (installed, version, memory, services). Phase 3 captures recent issues (errors, ANRs, crashes). The synthesis produces a one-page report highlighting anything that needs attention. This is the "preflight checklist" a solo developer runs before every testing session.]

## Configuration

### Parameters
- `$ARGUMENTS` — Package name (e.g., `com.example.myapp`)
- `--device=SERIAL` — Target specific device (optional, uses default if only one device)
- `--verbose` — Include full dumpsys output (default: summary only)

## Phase 1: Device State

### 1. Device Connection and Info
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Check ADB device state for health check. Run these commands and report results:

```bash
# Verify device connection
adb devices

# Device info
adb shell getprop ro.product.model
adb shell getprop ro.build.version.release
adb shell getprop ro.build.version.sdk

# Battery
adb shell dumpsys battery | grep -E 'level|status|temperature'

# Storage
adb shell df -h /data | tail -1

# Screen state
adb shell dumpsys power | grep 'mWakefulness'
```

Report as a table:
| Property | Value |
|----------|-------|
| Device | [model] |
| Android | [version] (API [level]) |
| Battery | [level]%, [status], [temp]°C |
| Storage | [used]/[total] ([% used]) |
| Screen | [on/off] |

Flag any concerns:
- Battery < 20% → ⚠️ Low battery may affect testing
- Storage > 90% → ⚠️ Low storage may cause install failures
- Device offline → ❌ Connection issue"
- Expected output: Device state table with flags

## Phase 2: App State (Run in Parallel with Phase 1 if possible)

### 2. App Health
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Check app health for package $ARGUMENTS via ADB. Run these commands:

```bash
# Is app installed?
adb shell pm list packages | grep $ARGUMENTS

# App version
adb shell dumpsys package $ARGUMENTS | grep -E 'versionName|versionCode'

# Is app running?
adb shell pidof -s $ARGUMENTS

# Memory usage (if running)
adb shell dumpsys meminfo $ARGUMENTS | grep -E 'TOTAL|Java Heap|Native Heap|Graphics'

# Running services
adb shell dumpsys activity services $ARGUMENTS | grep -E 'ServiceRecord|intent='

# Active alarms
adb shell dumpsys alarm | grep $ARGUMENTS | head -5
```

Report as:
| Property | Value | Status |
|----------|-------|--------|
| Installed | [yes/no] | [✅/❌] |
| Version | [name] ([code]) | [info] |
| Running | [yes/no, PID if yes] | [info] |
| Memory (PSS) | [X MB] | [✅ <150MB / ⚠️ 150-300MB / ❌ >300MB] |
| Java Heap | [X MB] | [info] |
| Native Heap | [X MB] | [info] |
| Services | [count] running | [info] |
| Alarms | [count] pending | [⚠️ if >5] |

If app is not installed, report that and skip remaining checks."
- Expected output: App health table with status flags

## Phase 3: Recent Issues

### 3. Error and Crash Check
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Check for recent issues with $ARGUMENTS via ADB. Run:

```bash
# Recent errors in logcat (last 200 lines, errors only, app's tag)
adb logcat -t 200 *:E | grep -i '$ARGUMENTS' | tail -10

# Recent crashes
adb logcat -b crash -t 50 | grep -i '$ARGUMENTS'

# ANR traces (check if recent)
adb shell ls -la /data/anr/ 2>/dev/null | tail -5

# Recent tombstones (native crashes)
adb shell ls -la /data/tombstones/ 2>/dev/null | tail -3
```

Report:
- **Recent Errors:** [count in last 200 logcat lines, show top 3 unique errors]
- **Crash Log:** [any crashes found, or 'None']
- **ANR Traces:** [any recent ANR files, or 'None']
- **Native Crashes:** [any recent tombstones, or 'None']

Flag: ❌ if crashes found, ⚠️ if errors > 5, ✅ if clean"
- Expected output: Recent issues report

## Phase 4: Synthesis

### 4. Health Report
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Synthesize all health check results into a single report:

```
## ADB Health Check — [Package] — [Date/Time]

### Device
[device state table from Phase 1]

### App
[app health table from Phase 2]

### Recent Issues
[issues from Phase 3]

### Overall Status: ✅ HEALTHY / ⚠️ ATTENTION NEEDED / ❌ ISSUES FOUND

### Action Items (if any)
1. [highest priority item]
2. [next item]
...

### Ready to Test: YES / NO (reason)
```

Rules for overall status:
- ✅ HEALTHY: No errors, memory normal, no crashes
- ⚠️ ATTENTION NEEDED: High memory, pending errors, low battery/storage
- ❌ ISSUES FOUND: Crashes detected, app not installed, device issues"
- Expected output: Single-page health report
- Context: Include all results from Phases 1-3

## Success Criteria

- ✅ Device connection verified
- ✅ App installation and version confirmed
- ✅ Memory usage checked and classified
- ✅ Recent errors and crashes scanned
- ✅ Single-page report produced in under 60 seconds
- ✅ Clear go/no-go for starting a testing session

## Coordination Notes

- Run this command at the start of every testing session
- Pair with `android_ship_check` for more comprehensive pre-release verification
- If issues found, use `android-crash-triage` skill to investigate crashes
- If memory is high, use `android-adb-profiling` skill for detailed memory analysis
