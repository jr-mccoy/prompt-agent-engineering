---
name: android_test_matrix
description: Configures and executes a test matrix across multiple Android API levels and screen configurations. Sets up emulators or Gradle Managed Devices, runs instrumented tests, aggregates results, and highlights device-specific failures.
version: "1.0.0"
category: testing
tags: [android, testing, matrix, emulator, gradle-managed-devices, solo-developer]
agents_used: [android-device-farm-operator, test-automator, android-adb-specialist]
---

Multi-device test matrix command that ensures your app works beyond "works on my phone":

[Extended thinking: Solo developers test on one device. They ship, and immediately get 1-star reviews from users on Samsung Galaxy A-series or older API levels. This command automates multi-device testing by: (1) determining which configurations matter based on the app's minSdk and target audience, (2) setting up emulators or Gradle Managed Devices, (3) running instrumented tests across all configurations, and (4) producing a matrix report that shows exactly which devices pass and which fail. The key insight is that you don't need to test on 50 devices — you need to test on the 5-7 configurations that cover 90% of your users.]

## Configuration

### Parameters
- `$ARGUMENTS` — Path to the Android project root
- `--api-levels=28,30,33,34` — Specific API levels to test (default: auto from minSdk to targetSdk)
- `--use-gmd` — Use Gradle Managed Devices (recommended for CI)
- `--use-ftl` — Use Firebase Test Lab (cloud devices)
- `--screens=phone,tablet` — Screen categories to test (default: phone only)
- `--parallel=N` — Number of parallel emulators (default: 2)

## Phase 1: Matrix Definition

### 1. Determine Test Matrix
- Use Task tool with subagent_type="general-purpose"
- Agent persona: android-device-farm-operator
- Prompt: "Analyze the Android project at $ARGUMENTS and determine the optimal test matrix.

Check:
```bash
# Get minSdk and targetSdk
grep -E 'minSdk|targetSdk' $ARGUMENTS/app/build.gradle.kts 2>/dev/null || grep -E 'minSdkVersion|targetSdkVersion' $ARGUMENTS/app/build.gradle 2>/dev/null

# Get existing test count
find $ARGUMENTS -name '*Test*.kt' -o -name '*Test*.java' | wc -l

# Check if Gradle Managed Devices already configured
grep -r 'managedDevices' $ARGUMENTS/app/build.gradle.kts 2>/dev/null
```

Determine test matrix:
| Configuration | API Level | Screen | Rationale |
|--------------|-----------|--------|-----------|
| Latest target | [targetSdk] | Phone | Must pass — this is your target |
| Mid-range | [targetSdk - 4] | Phone | Covers majority of active devices |
| Min supported | [minSdk] | Phone | Boundary — catches API compatibility issues |
| Large screen | [targetSdk] | Tablet (if --screens=tablet) | Catches layout issues on larger screens |

If --api-levels specified, use those instead.
If --use-ftl, recommend Firebase Test Lab devices (physical, not emulator).

Report the selected matrix and estimated run time."
- Expected output: Test matrix definition with rationale
- GATE: Developer confirms matrix before proceeding

## Phase 2: Environment Setup

### 2. Set Up Test Infrastructure
- Use Task tool with subagent_type="general-purpose"
- Agent persona: android-device-farm-operator
- Prompt: "Set up the test environment for the matrix defined in Phase 1.

If --use-gmd:
```kotlin
// Add to build.gradle.kts if not already present
android {
    testOptions {
        managedDevices {
            localDevices {
                // Create device for each matrix entry
                create('[name]') {
                    device = '[device profile]'
                    apiLevel = [level]
                    systemImageSource = 'google'
                }
            }
            groups {
                create('testMatrix') {
                    targetDevices.add(devices['[name1]'])
                    targetDevices.add(devices['[name2]'])
                    // ...
                }
            }
        }
    }
}
```

If local emulators:
```bash
# Create AVDs for each matrix entry
for each configuration:
    avdmanager create avd -n 'matrix_[api]_[screen]' -k 'system-images;android-[api];google_apis;x86_64' -d '[device]' --force
```

If --use-ftl:
```bash
# Verify gcloud is configured
gcloud firebase test android models list | head -20
# Select physical devices matching matrix
```

Verify all environments are ready before Phase 3."
- Expected output: Infrastructure setup confirmation
- GATE: All emulators/devices available before proceeding

## Phase 3: Test Execution

### 3. Run Tests Across Matrix
- Use Task tool with subagent_type="general-purpose"
- Prompt: "Execute instrumented tests across all matrix configurations.

If --use-gmd:
```bash
./gradlew testMatrixGroupCheck -Pandroid.testoptions.manageddevices.maxparallel=$PARALLEL
```

If local emulators (run in parallel):
```bash
# Start emulators
for each configuration:
    emulator -avd 'matrix_[api]_[screen]' -no-window -gpu swiftshader_indirect -no-audio -no-boot-anim -port [port] &

# Wait for all to boot
for each emulator:
    adb -s emulator-[port] wait-for-device
    adb -s emulator-[port] shell 'while [[ -z $(getprop sys.boot_completed) ]]; do sleep 1; done'

# Disable animations on all
for each emulator:
    adb -s emulator-[port] shell settings put global window_animation_scale 0
    adb -s emulator-[port] shell settings put global transition_animation_scale 0
    adb -s emulator-[port] shell settings put global animator_duration_scale 0

# Run tests (using Gradle with device targeting or custom scripts)
./gradlew connectedCheck
```

If --use-ftl:
```bash
gcloud firebase test android run \
    --type instrumentation \
    --app $ARGUMENTS/app/build/outputs/apk/debug/app-debug.apk \
    --test $ARGUMENTS/app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk \
    --device model=[model1],version=[api1] \
    --device model=[model2],version=[api2] \
    --timeout 15m \
    --results-dir=test-results
```

Capture per-device results (pass, fail, error, timeout)."
- Expected output: Raw test results per configuration

## Phase 4: Result Analysis

### 4. Aggregate and Report
- Use Task tool with subagent_type="general-purpose"
- Agent persona: android-device-farm-operator
- Prompt: "Analyze test results from all matrix configurations and produce a report.

```
## Test Matrix Report — [Date]

### Summary
| Configuration | Tests | Passed | Failed | Skipped | Status |
|--------------|-------|--------|--------|---------|--------|
| API 34 Phone | [N] | [N] | [N] | [N] | ✅/❌ |
| API 30 Phone | [N] | [N] | [N] | [N] | ✅/❌ |
| API 28 Phone | [N] | [N] | [N] | [N] | ✅/❌ |
| ... | ... | ... | ... | ... | ... |

### Overall: [X]/[Y] configurations passing ([Z]%)

### Device-Specific Failures
[Tests that fail ONLY on specific configurations — these are compatibility bugs]
| Test | Fails On | Passes On | Likely Cause |
|------|----------|-----------|--------------|
| [test name] | API 28 | API 30, 34 | [guess: API change, missing compat] |

### Universal Failures
[Tests that fail on ALL configurations — these are bugs regardless of device]
| Test | Error | Fix Priority |
|------|-------|-------------|
| [test name] | [error] | P[0-3] |

### Flaky Tests
[Tests that pass sometimes, fail sometimes on the same configuration]
| Test | Configuration | Pass Rate |
|------|--------------|-----------|
| [test name] | [config] | [X]% |

### Recommendations
1. [Highest priority fix]
2. [Next priority]
3. [Matrix adjustment suggestion if applicable]

### Matrix Coverage Assessment
- **User coverage estimate:** [X]% of active installs covered by this matrix
- **Recommendation:** [Add/remove configurations? Current matrix sufficient?]
```"
- Expected output: Formatted matrix report
- Context: Include all raw results from Phase 3

## Success Criteria

- ✅ Test matrix covers minSdk to targetSdk range
- ✅ All configurations set up and tests executed
- ✅ Results aggregated per configuration
- ✅ Device-specific failures identified and separated from universal bugs
- ✅ Flaky tests detected
- ✅ Actionable report with fix priorities

## Coordination Notes

- Run before every release (at minimum)
- Pair with `android_ship_check` command for full pre-release verification
- Use `android-emulator-management` skill for emulator troubleshooting
- If device-specific failures found, use `android-crash-triage` skill to investigate
- Track matrix results over time to identify recurring problem configurations
- Start with a 3-device matrix and expand only when crash data justifies it
