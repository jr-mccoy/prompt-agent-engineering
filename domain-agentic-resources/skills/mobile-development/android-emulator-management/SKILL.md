---
name: android-emulator-management
description: "Android emulator setup, configuration, snapshot management, headless CI execution, and multi-device testing. Covers avdmanager, emulator CLI, Gradle Managed Devices, CI-specific configurations, and emulator console commands. Use this skill when creating AVDs, configuring emulators for CI, managing snapshots, running headless emulators, setting up multi-device testing, or when a developer mentions 'emulator', 'AVD', 'headless', 'Gradle Managed Devices', or 'emulator not booting'."
metadata:
  tags:
    - android
    - emulator
    - avd
    - ci-cd
    - testing
    - solo-developer
  updated: "2026-03-06"
---

# Android Emulator Management

Android emulator setup, configuration, snapshot management, and CI integration. Covers the full emulator lifecycle from AVD creation through headless CI execution and Gradle Managed Devices.

## Purpose

Solo developers typically own 1-2 physical devices but need to test across API levels, screen sizes, and locales. Emulators fill this gap — but only if properly configured. A slow emulator with wrong settings wastes more time than manual testing on a phone. This skill provides recipes for fast, reliable emulators for both local development and CI pipelines.

## When to Use This Skill

Use this skill when you need to:
- Create a new AVD for a specific API level or screen size
- Configure emulators for CI/CD pipelines (headless, fast boot)
- Manage snapshots for quick state restoration
- Set up Gradle Managed Devices for automated test matrices
- Run multiple emulators simultaneously for parallel testing
- Troubleshoot emulator issues (not booting, slow, GPU problems)

## When NOT to Use This Skill

Do NOT use this skill when:
- You need to run ADB commands on an already-running emulator (use `android-adb-operations`)
- You need to profile performance on an emulator (use `android-adb-profiling`)
- You need to run a full test matrix across devices (use `android_test_matrix` command)

## Prerequisites

- Android SDK installed with `emulator`, `avdmanager`, and `sdkmanager` on PATH
- At least one system image installed (`sdkmanager "system-images;android-34;google_apis;x86_64"`)
- Hardware acceleration: KVM on Linux, HAXM or Hypervisor.framework on macOS, WHPX on Windows
- Minimum 8GB RAM (16GB recommended for running emulator alongside IDE)

## Step 1: AVD Creation

### 1.1 Install System Images

```bash
# List available system images
sdkmanager --list | grep "system-images"

# Install common images
sdkmanager "system-images;android-34;google_apis;x86_64"      # Latest
sdkmanager "system-images;android-30;google_apis;x86_64"      # Android 11
sdkmanager "system-images;android-28;google_apis;x86_64"      # Android 9 (minSdk common)
sdkmanager "system-images;android-34;google_apis_playstore;x86_64"  # With Play Store
```

### 1.2 Create AVD

```bash
# Create with avdmanager
avdmanager create avd \
    -n "Pixel_7_API_34" \
    -k "system-images;android-34;google_apis;x86_64" \
    -d "pixel_7" \
    --force

# Create without hardware profile (default phone)
avdmanager create avd \
    -n "Test_API_30" \
    -k "system-images;android-30;google_apis;x86_64"
```

### 1.3 Common Device Profiles

| Profile | Use Case | Command Flag |
|---------|----------|-------------|
| `pixel_7` | Standard phone testing | `-d "pixel_7"` |
| `pixel_7_pro` | Large phone | `-d "pixel_7_pro"` |
| `pixel_tablet` | Tablet testing | `-d "pixel_tablet"` |
| `pixel_fold` | Foldable testing | `-d "pixel_fold"` |
| `Nexus 5` | Small/older phone | `-d "Nexus 5"` |

```bash
# List all available device profiles
avdmanager list device
```

### 1.4 List and Delete AVDs

```bash
# List existing AVDs
avdmanager list avd

# Delete an AVD
avdmanager delete avd -n "Pixel_7_API_34"
```

## Step 2: Emulator Launch and Configuration

### 2.1 Basic Launch

```bash
# Start emulator
emulator -avd Pixel_7_API_34

# Start without window (headless)
emulator -avd Pixel_7_API_34 -no-window

# Start with specific GPU mode
emulator -avd Pixel_7_API_34 -gpu swiftshader_indirect  # Software rendering
emulator -avd Pixel_7_API_34 -gpu host                  # Host GPU (fastest)
emulator -avd Pixel_7_API_34 -gpu auto                  # Auto-detect
```

### 2.2 Performance Options

```bash
# Fast boot with snapshot (default, fastest start)
emulator -avd Pixel_7_API_34 -no-snapshot-save  # Use snapshot but don't save new one

# Cold boot (fresh start, slower but clean)
emulator -avd Pixel_7_API_34 -no-snapshot-load

# Memory allocation
emulator -avd Pixel_7_API_34 -memory 2048  # 2GB RAM for emulator

# CPU cores
emulator -avd Pixel_7_API_34 -cores 4
```

### 2.3 Network Configuration

```bash
# Use proxy
emulator -avd Pixel_7_API_34 -http-proxy http://proxy.example.com:8080

# Custom DNS
emulator -avd Pixel_7_API_34 -dns-server 8.8.8.8,8.8.4.4

# No network (airplane mode)
emulator -avd Pixel_7_API_34 -no-network
```

## Step 3: Snapshot Management

### 3.1 Create and Load Snapshots

```bash
# Save a snapshot (emulator must be running)
adb emu avd snapshot save "logged_in_state"

# Load a snapshot
adb emu avd snapshot load "logged_in_state"

# List snapshots
adb emu avd snapshot list

# Delete a snapshot
adb emu avd snapshot delete "logged_in_state"
```

### 3.2 Snapshot Strategies

| Snapshot Name | When to Create | Use Case |
|--------------|----------------|----------|
| `fresh_install` | After first boot, before any setup | Clean slate testing |
| `logged_in` | After completing login/onboarding | Skip login for feature testing |
| `with_data` | After populating test data | Test with realistic data |
| `permission_granted` | After granting all permissions | Skip permission dialogs |

## Step 4: CI/CD Emulator Configuration

### 4.1 GitHub Actions

```yaml
# .github/workflows/android-tests.yml
jobs:
  instrumented-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up JDK
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Enable KVM
        run: |
          echo 'KERNEL=="kvm", GROUP="kvm", MODE="0666", OPTIONS+="static_node=kvm"' | sudo tee /etc/udev/rules.d/99-kvm4all.rules
          sudo udevadm control --reload-rules
          sudo udevadm trigger --name-match=kvm

      - name: Instrumented Tests
        uses: reactivecircus/android-emulator-runner@v2
        with:
          api-level: 34
          target: google_apis
          arch: x86_64
          profile: pixel_7
          heap-size: 512M
          ram-size: 2048M
          emulator-options: -no-window -gpu swiftshader_indirect -no-snapshot -noaudio -no-boot-anim
          disable-animations: true
          script: ./gradlew connectedCheck
```

### 4.2 Headless Emulator Script (Local CI)

```bash
#!/bin/bash
# start-emulator-headless.sh

AVD_NAME="CI_Test_API_34"

# Create AVD if it doesn't exist
if ! avdmanager list avd | grep -q "$AVD_NAME"; then
    sdkmanager "system-images;android-34;google_apis;x86_64"
    avdmanager create avd -n "$AVD_NAME" -k "system-images;android-34;google_apis;x86_64" -d "pixel_7" --force
fi

# Start emulator in background
emulator -avd "$AVD_NAME" -no-window -gpu swiftshader_indirect -no-audio -no-boot-anim &

# Wait for emulator to boot
adb wait-for-device
adb shell 'while [[ -z $(getprop sys.boot_completed) ]]; do sleep 1; done'

# Disable animations for testing
adb shell settings put global window_animation_scale 0
adb shell settings put global transition_animation_scale 0
adb shell settings put global animator_duration_scale 0

echo "Emulator ready"
```

## Step 5: Gradle Managed Devices

### 5.1 Configuration

```kotlin
// build.gradle.kts (app module)
android {
    testOptions {
        managedDevices {
            localDevices {
                create("pixel7api34") {
                    device = "Pixel 7"
                    apiLevel = 34
                    systemImageSource = "google"
                }
                create("pixel7api30") {
                    device = "Pixel 7"
                    apiLevel = 30
                    systemImageSource = "google"
                }
                create("smallPhoneApi28") {
                    device = "Nexus 5"
                    apiLevel = 28
                    systemImageSource = "google"
                }
            }
            groups {
                create("phoneDevices") {
                    targetDevices.add(devices["pixel7api34"])
                    targetDevices.add(devices["pixel7api30"])
                    targetDevices.add(devices["smallPhoneApi28"])
                }
            }
        }
    }
}
```

### 5.2 Running GMD Tests

```bash
# Run tests on a single managed device
./gradlew pixel7api34Check

# Run tests on all devices in a group
./gradlew phoneDevicesGroupCheck

# Run with parallel execution
./gradlew phoneDevicesGroupCheck -Pandroid.testoptions.manageddevices.maxparallel=3
```

## Step 6: Multi-Device Testing

### 6.1 Running Multiple Emulators

```bash
# Start first emulator
emulator -avd Pixel_7_API_34 -port 5554 &

# Start second emulator (different port)
emulator -avd Test_API_30 -port 5556 &

# Wait for both to boot
adb -s emulator-5554 wait-for-device
adb -s emulator-5556 wait-for-device

# Install on both
adb -s emulator-5554 install app.apk
adb -s emulator-5556 install app.apk
```

### 6.2 Emulator Console Commands

```bash
# Connect to emulator console
telnet localhost 5554

# Simulate GPS location
geo fix -122.084 37.422

# Simulate incoming call
gsm call 5551234567

# Simulate SMS
sms send 5551234567 "Test message"

# Set battery level
power capacity 15
power status not-charging

# Simulate network conditions
network speed edge    # Slow 2G
network speed lte     # 4G LTE
network delay gprs    # High latency
```

## Troubleshooting

### Emulator Won't Boot

```bash
# Check hardware acceleration
emulator -accel-check

# If KVM not available (Linux):
sudo apt install qemu-kvm
sudo adduser $USER kvm

# Try cold boot
emulator -avd Pixel_7_API_34 -no-snapshot-load

# Try software rendering
emulator -avd Pixel_7_API_34 -gpu swiftshader_indirect
```

### Emulator Very Slow

1. Ensure hardware acceleration is enabled (`emulator -accel-check`)
2. Use x86_64 system images, not arm64
3. Allocate more RAM: `-memory 4096`
4. Use Quick Boot (snapshot-based, default)
5. Reduce screen resolution in AVD settings

### "PANIC: Broken AVD system path"

```bash
# Re-download system image
sdkmanager --install "system-images;android-34;google_apis;x86_64"

# Or recreate the AVD
avdmanager delete avd -n Pixel_7_API_34
avdmanager create avd -n Pixel_7_API_34 -k "system-images;android-34;google_apis;x86_64" -d "pixel_7"
```

## Related Skills

- `android-adb-operations` — ADB commands to use once emulator is running
- `android-adb-profiling` — Performance profiling on emulators
- `android-testing-patterns` — Instrumented test execution
- `android-screenshot-testing` — Screenshot testing across emulator configurations
