---
name: android-adb-operations
description: "Comprehensive ADB command reference and workflow guide for device management, app installation, debugging, log capture, file transfer, shell operations, intent testing, and screen capture. Use this skill when working with ADB, connecting devices, installing APKs, reading logcat, pushing/pulling files, testing deep links, capturing screenshots, or when a developer mentions 'adb', 'logcat', 'device not found', 'install APK', or 'wireless debugging'."
metadata:
  tags:
    - android
    - adb
    - debugging
    - device-management
    - solo-developer
  updated: "2026-03-06"
---

# Android ADB Operations

Comprehensive Android Debug Bridge (ADB) command reference and workflow guide. Covers every common ADB operation from device connection through profiling, organized by task rather than alphabetically, with troubleshooting for the issues developers actually hit.

## Purpose

ADB is the single most-used command-line tool in Android development — every developer uses it daily for installing builds, reading logs, testing deep links, and capturing screenshots. Despite this, most developers know only a fraction of ADB's capabilities and waste time on workarounds that ADB solves directly. This skill provides task-oriented ADB workflows rather than a man-page-style reference. For solo developers, ADB mastery replaces the tribal knowledge that team environments provide through pair programming and shared scripts.

## When to Use This Skill

Use this skill when you need to:
- Connect to a device (USB or wireless) and verify the connection
- Install, uninstall, or manage app packages
- Read and filter logcat output for debugging
- Push files to or pull files from a device
- Test deep links, intents, or broadcasts via command line
- Capture screenshots or screen recordings
- Manage device settings, permissions, or state via shell
- Troubleshoot "device not found", "unauthorized", or connection issues

## When NOT to Use This Skill

Do NOT use this skill when:
- You need ADB-based performance profiling (use `android-adb-profiling` skill)
- You need emulator setup and management (use `android-emulator-management` skill)
- You are debugging a crash from Crashlytics (use `android-crash-triage` skill)
- You need to run instrumented tests (use `android-testing-patterns` skill)

## Prerequisites

- Android SDK Platform Tools installed (`adb` on PATH)
- USB debugging enabled on target device (Settings → Developer Options → USB Debugging)
- For wireless debugging: Android 11+ and both device and computer on same network

## Step 1: Device Connection

### 1.1 USB Connection

```bash
# List connected devices
adb devices

# Expected output:
# List of devices attached
# SERIAL_NUMBER    device

# If you see "unauthorized" — check device for USB debugging prompt and tap "Allow"
# If you see "offline" — unplug, re-plug, check USB cable quality
```

### 1.2 Wireless Connection (Android 11+)

```bash
# On device: Settings → Developer Options → Wireless Debugging → Enable
# Note the IP address and port shown on device

# Pair (first time only)
adb pair IP_ADDRESS:PAIRING_PORT
# Enter the pairing code shown on device

# Connect
adb connect IP_ADDRESS:PORT

# Verify
adb devices
```

### 1.3 Wireless Connection (Legacy, Android 10 and below)

```bash
# Connect via USB first, then:
adb tcpip 5555
adb connect DEVICE_IP:5555
# Now unplug USB
```

### 1.4 Multi-Device Targeting

```bash
# When multiple devices are connected, specify target:
adb -s SERIAL_NUMBER shell
adb -s SERIAL_NUMBER install app.apk

# Use emulator serial for emulators:
adb -s emulator-5554 shell

# Shortcut: target only USB device or only emulator
adb -d shell   # USB device only
adb -e shell   # Emulator only
```

## Step 2: App Lifecycle Management

### 2.1 Installation

```bash
# Install APK
adb install app-debug.apk

# Install with replacement (upgrade)
adb install -r app-debug.apk

# Install with downgrade allowed
adb install -r -d app-debug.apk

# Install to specific user
adb install --user 0 app-debug.apk

# Install split APKs (from app bundle)
adb install-multiple base.apk config.en.apk config.xxhdpi.apk
```

### 2.2 Uninstallation

```bash
# Uninstall app
adb uninstall com.example.myapp

# Uninstall but keep data (useful for reinstall testing)
adb uninstall -k com.example.myapp
```

### 2.3 App Launch and Stop

```bash
# Start main activity
adb shell am start -n com.example.myapp/.MainActivity

# Start with intent flags (clear task)
adb shell am start -n com.example.myapp/.MainActivity --activity-clear-task

# Force stop app
adb shell am force-stop com.example.myapp

# Clear app data (like fresh install)
adb shell pm clear com.example.myapp
```

### 2.4 Package Information

```bash
# List installed packages
adb shell pm list packages

# Filter by name
adb shell pm list packages | grep example

# Show package path (where APK lives on device)
adb shell pm path com.example.myapp

# Dump package info (version, permissions, activities)
adb shell dumpsys package com.example.myapp
```

## Step 3: Logcat Mastery

### 3.1 Basic Logcat

```bash
# Stream all logs
adb logcat

# Clear log buffer first, then stream
adb logcat -c && adb logcat

# Save to file
adb logcat > logs.txt
# (Ctrl+C to stop)
```

### 3.2 Filtering

```bash
# Filter by tag and priority (V=Verbose, D=Debug, I=Info, W=Warn, E=Error, F=Fatal)
adb logcat MyAppTag:D *:S
# Shows only MyAppTag at Debug+ level, silences everything else

# Filter by multiple tags
adb logcat MyAppTag:D NetworkManager:W *:S

# Filter by priority only (show all errors)
adb logcat *:E

# Filter by string (grep)
adb logcat | grep -i "exception"

# Filter by PID (your app's process)
adb logcat --pid=$(adb shell pidof -s com.example.myapp)
```

### 3.3 Logcat Format Options

```bash
# Show timestamp
adb logcat -v time

# Show thread ID
adb logcat -v threadtime

# Show with color (terminal must support ANSI)
adb logcat -v color

# Brief format (tag and priority only)
adb logcat -v brief

# Long format (all metadata)
adb logcat -v long
```

### 3.4 Logcat for Crash Investigation

```bash
# Show last N lines (recent crashes)
adb logcat -t 200

# Show logs since specific time
adb logcat -T "03-06 14:30:00.000"

# Dump crash buffer specifically
adb logcat -b crash

# Show all buffers
adb logcat -b all
```

## Step 4: File Operations

### 4.1 Push and Pull

```bash
# Push file to device
adb push local_file.txt /sdcard/Download/

# Pull file from device
adb pull /sdcard/Download/remote_file.txt ./

# Pull entire directory
adb pull /sdcard/DCIM/Camera/ ./camera_backup/

# Push multiple files
adb push file1.txt file2.txt /sdcard/Download/
```

### 4.2 Common File Locations

| Location | What's There |
|----------|-------------|
| `/sdcard/` | Shared external storage (media, downloads) |
| `/sdcard/Download/` | Downloads directory |
| `/sdcard/DCIM/Camera/` | Camera photos |
| `/data/data/com.example.myapp/` | App's private storage (requires root or run-as) |
| `/data/local/tmp/` | Temp directory (writable without root) |

### 4.3 Accessing App Private Storage

```bash
# Use run-as for debuggable apps (no root needed)
adb shell run-as com.example.myapp ls files/
adb shell run-as com.example.myapp cat databases/app.db

# Copy from private storage to accessible location
adb shell run-as com.example.myapp cp databases/app.db /sdcard/Download/
adb pull /sdcard/Download/app.db ./
```

## Step 5: Shell Commands

### 5.1 Interactive Shell

```bash
# Open shell on device
adb shell

# Run single command
adb shell whoami
adb shell date
adb shell df -h
```

### 5.2 Input Simulation

```bash
# Tap at coordinates (x, y)
adb shell input tap 500 800

# Swipe (x1, y1, x2, y2, duration_ms)
adb shell input swipe 500 1500 500 300 300

# Type text
adb shell input text "hello world"

# Key events
adb shell input keyevent KEYCODE_HOME
adb shell input keyevent KEYCODE_BACK
adb shell input keyevent KEYCODE_ENTER
adb shell input keyevent KEYCODE_VOLUME_UP
```

### 5.3 Settings Manipulation

```bash
# Read a setting
adb shell settings get system screen_brightness

# Set a setting
adb shell settings put system screen_brightness 128

# Common settings to manipulate:
adb shell settings put global window_animation_scale 0    # Disable animations (for testing)
adb shell settings put global transition_animation_scale 0
adb shell settings put global animator_duration_scale 0

# Re-enable animations
adb shell settings put global window_animation_scale 1
adb shell settings put global transition_animation_scale 1
adb shell settings put global animator_duration_scale 1
```

### 5.4 Device Information

```bash
# Android version
adb shell getprop ro.build.version.release

# API level
adb shell getprop ro.build.version.sdk

# Device model
adb shell getprop ro.product.model

# Manufacturer
adb shell getprop ro.product.manufacturer

# Screen size and density
adb shell wm size
adb shell wm density

# Battery status
adb shell dumpsys battery
```

## Step 6: Intent and Deep Link Testing

### 6.1 Deep Links

```bash
# Open a deep link
adb shell am start -a android.intent.action.VIEW -d "https://example.com/product/123"

# Open a custom scheme deep link
adb shell am start -a android.intent.action.VIEW -d "myapp://settings/profile"

# Open with specific package (bypass chooser)
adb shell am start -a android.intent.action.VIEW -d "https://example.com/path" -p com.example.myapp
```

### 6.2 Broadcasts

```bash
# Send a custom broadcast
adb shell am broadcast -a com.example.myapp.CUSTOM_ACTION

# Send broadcast with extras
adb shell am broadcast -a com.example.myapp.REFRESH --es "key" "value" --ei "count" 5

# Common system broadcasts for testing
adb shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true
```

### 6.3 Start Activities with Extras

```bash
# String extra
adb shell am start -n com.example.myapp/.DetailActivity --es "item_id" "abc123"

# Integer extra
adb shell am start -n com.example.myapp/.DetailActivity --ei "page" 3

# Boolean extra
adb shell am start -n com.example.myapp/.DetailActivity --ez "debug" true
```

## Step 7: Screen Capture

### 7.1 Screenshots

```bash
# Capture screenshot to device
adb shell screencap /sdcard/screenshot.png

# Capture and pull in one command
adb exec-out screencap -p > screenshot.png

# Capture, pull, and open (macOS)
adb exec-out screencap -p > screenshot.png && open screenshot.png
```

### 7.2 Screen Recording

```bash
# Record screen (max 3 minutes)
adb shell screenrecord /sdcard/recording.mp4

# Record with options
adb shell screenrecord --size 720x1280 --bit-rate 4000000 --time-limit 30 /sdcard/recording.mp4
# (Ctrl+C to stop early)

# Pull recording
adb pull /sdcard/recording.mp4 ./
```

### 7.3 Bug Report

```bash
# Generate full bug report (takes 1-2 minutes)
adb bugreport ./bugreport.zip

# This captures: logcat, dumpsys, dmesg, procrank, and more
# Use for sharing with library authors or filing issues
```

## Step 8: Permission Management

```bash
# Grant a runtime permission
adb shell pm grant com.example.myapp android.permission.CAMERA

# Revoke a runtime permission
adb shell pm revoke com.example.myapp android.permission.CAMERA

# List permissions for a package
adb shell dumpsys package com.example.myapp | grep "permission"

# Useful for testing permission-denied flows without manually toggling in Settings
```

## Step 9: Network and Connectivity

```bash
# Check connectivity
adb shell ping -c 3 google.com

# Show network interfaces
adb shell ifconfig

# Show Wi-Fi info
adb shell dumpsys wifi | grep "mWifiInfo"

# Enable/disable Wi-Fi (requires root or API 30+)
adb shell svc wifi disable
adb shell svc wifi enable

# Enable/disable mobile data
adb shell svc data disable
adb shell svc data enable
```

---

Troubleshooting Common Issues ("device not found", "device unauthorized", "device offline", install failures, slow Wi-Fi) and the ADB Cheat Sheet (20-command quick reference table) are in the reference file.

See [references/troubleshooting-and-cheat-sheet.md](references/troubleshooting-and-cheat-sheet.md)

---

## Related Skills

- `android-adb-profiling` — ADB-based performance profiling (CPU, memory, battery)
- `android-emulator-management` — Emulator setup, snapshots, and CI integration
- `android-crash-triage` — Production crash investigation using logcat and Crashlytics
- `android-deep-link-architect` — Deep link design and testing patterns
- `android-testing-patterns` — Instrumented test execution

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/troubleshooting-and-cheat-sheet.md` | Troubleshooting ("device not found", "unauthorized", "offline", install failures, slow Wi-Fi) and 20-command ADB cheat sheet table |
