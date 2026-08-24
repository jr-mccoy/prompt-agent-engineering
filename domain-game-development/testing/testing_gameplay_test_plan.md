---
title: "Gameplay Test Plan Generation"
category: game-development/testing
description: "Generate comprehensive test plans for game features covering functional tests, regression scenarios, edge cases, and platform certification requirements"
techniques:
  - ST-01
  - ST-02
  - ST-03
  - DT-01
  - QA-02
difficulty: intermediate
tags:
  - testing
  - qa
  - test-plan
  - regression
  - game-testing
  - certification
updated: "2026-03-19"
---

# Gameplay Test Plan Generation

**Objective:** Generate comprehensive gameplay test plans for game features covering functional verification, regression scenarios, boundary conditions (extreme inputs, geometry edges), platform-specific certification requirements, and multiplayer edge cases.

**When to Use:** Use this prompt when designing or implementing a new gameplay feature, preparing for QA milestones, building regression suites before a release candidate, or onboarding QA team members who need structured test plans for game mechanics. Essential before alpha, beta, and gold master submissions.

**Instructions:**

1. **Feature Decomposition**
   - Break the gameplay feature into discrete, testable components
   - Identify all player-facing states the feature can produce
   - Map the feature's dependencies on other game systems (physics, animation, audio, UI, networking)
   - Document entry conditions (how the player activates the feature) and exit conditions (how the feature ends)
   - List all configurable parameters (designer-tunable values, difficulty scaling, platform differences)

2. **Functional Test Cases (Happy Path)**
   - Define expected behavior for standard use of the feature
   - Test each entry condition independently
   - Verify visual, audio, and haptic feedback for each state transition
   - Confirm UI elements update correctly (HUD indicators, prompts, meters)
   - Validate camera behavior during the feature
   - Test the feature at each difficulty level or mode variant

3. **Edge Case Identification**
   - **Boundary geometry:** Test at level edges, near collision seams, on slopes at max angle, in tight corridors, at world origin (0,0,0)
   - **Extreme input combinations:** Simultaneous opposing inputs, rapid input toggling, analog stick dead-zone boundaries, all buttons pressed
   - **Rapid state transitions:** Activate/deactivate feature as fast as possible, interrupt with other actions (jump, attack, pause menu)
   - **Save/Load during feature:** Save mid-feature, load into active feature state, checkpoint during feature
   - **Resource boundaries:** Test when stamina/mana/ammo is exactly at threshold, test at zero and maximum values
   - **Timing edge cases:** Activate at exact moment of damage, death, level transition, cutscene trigger

4. **Regression Scenarios**
   - Identify interactions with movement system (does feature break walking, sprinting, crouching?)
   - Test with combat system (can player attack during feature? can enemies damage player?)
   - Verify inventory/equipment interactions (does equipping items during feature cause issues?)
   - Test with save system (does feature state serialize correctly?)
   - Verify multiplayer interactions (does feature replicate correctly? what happens with latency?)
   - Check progression system (do achievements/trophies trigger correctly during feature?)

5. **Platform-Specific Tests**
   - **Controller (console):** Test with analog stick (full range, partial tilt), trigger sensitivity, vibration feedback
   - **Touch (mobile):** Test gesture recognition, multi-touch conflicts, screen orientation changes
   - **Keyboard + Mouse:** Test rebindable keys, simultaneous key combinations, mouse sensitivity scaling
   - **Accessibility:** Test with assist modes enabled, colorblind modes, subtitle timing during feature

6. **Performance Impact Assessment**
   - Measure frame time impact when feature is active vs inactive
   - Profile memory allocations during feature activation (watch for per-frame allocations)
   - Test with maximum entity count in the area (worst-case scenario)
   - Verify LOD transitions don't cause visual artifacts during feature
   - Check for hitches during feature activation (asset streaming, shader compilation)
   - Test sustained use over extended play sessions (memory leaks, performance degradation)

7. **CRITICAL: Verification Checklist**
   - Verify test cases cover ALL user-facing states identified in step 1
   - Verify there are no untested failure paths (every "what if" has a test)
   - Verify platform certification requirements relevant to this feature are addressed
   - Cross-reference with design document to ensure no intended behaviors are untested
   - Confirm edge cases include at least 3 "chaos" scenarios (unexpected player behavior)
   - Assign confidence level (High/Medium/Low) to each test category

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Create tests for internal implementation details (test player-visible behavior, not code structure)
- Assume deterministic physics outcomes in test expectations (use tolerance ranges)
- Write pass/fail criteria that depend on exact frame counts (use frame ranges)
- Test only the "golden path" the designer intended (players will do unexpected things)
- Assume consistent frame rates across platforms in timing-sensitive tests
- Mark "looks fine" as a pass criterion (define what "fine" means objectively)

✅ **DO:**
- Account for frame-rate-dependent behavior in all timing-sensitive tests
- Include "feel" tests that explicitly require human evaluation (mark them as MANUAL)
- Specify tolerance ranges for physics-dependent outcomes (e.g., "lands within 0.5m of target")
- Test with both fresh installs and saves migrated from previous versions
- Include negative tests (verify the feature does NOT activate when it shouldn't)
- Document reproduction steps precisely enough that any QA tester can execute them
- Test with debug visualization disabled (some bugs only appear without debug overlays)

**Expected Output:** A structured test plan document including:
- Feature overview and testable component breakdown
- Categorized test cases (functional, edge case, regression, platform, performance)
- Clear pass/fail criteria for each test case
- Priority ratings (P0-Critical, P1-High, P2-Medium, P3-Low)
- Estimated execution time per test category
- Manual vs automatable test classification
- Coverage confidence rating per category

**Example Output:**

```markdown
# Test Plan: Wall Running Mechanic — FPS Combat Game

## Feature Overview
Wall Running allows the player to run along vertical surfaces for a limited
duration. The mechanic is core to traversal and combat, enabling access to
elevated positions, flanking routes, and stylish movement chains.

### Testable Components
| ID | Component | Description |
|----|-----------|-------------|
| WR-01 | Wall Detection | Identifying valid wall-run surfaces |
| WR-02 | Entry Conditions | Triggering wall-run from different states |
| WR-03 | Wall-Run Movement | Physics and controls during wall-run |
| WR-04 | Duration & Stamina | Time limits and resource consumption |
| WR-05 | Exit Transitions | Leaving wall-run into other states |
| WR-06 | Combat Integration | Shooting, grenades, abilities during wall-run |
| WR-07 | Camera Behavior | Camera tilt, FOV, and orientation |
| WR-08 | Visual/Audio Feedback | Particles, sounds, controller vibration |
| WR-09 | Multiplayer Replication | Network sync and spectator view |
| WR-10 | UI Integration | HUD indicators and crosshair behavior |

---

## 1. Functional Tests (Happy Path)

### WR-FUNC-001: Basic Wall-Run Activation
- **Precondition:** Player is sprinting toward a valid wall at 30-60 degree angle
- **Steps:**
  1. Sprint toward a flat vertical wall
  2. Jump when within 2m of wall surface
  3. Hold movement stick toward the wall
- **Expected Result:** Player attaches to wall, begins horizontal traversal,
  camera tilts 15 degrees toward wall, wall-run particle effect plays,
  footstep audio switches to wall-run variant
- **Pass Criteria:** Wall-run activates within 3 frames of contact
- **Priority:** P0-Critical
- **Type:** Automated

### WR-FUNC-002: Wall-Run Direction (Left vs Right)
- **Precondition:** Player approaches wall from both left and right sides
- **Steps:**
  1. Approach wall from the left, jump toward it
  2. Verify player runs rightward along wall
  3. Approach same wall from the right, jump toward it
  4. Verify player runs leftward along wall
- **Expected Result:** Wall-run direction matches approach vector;
  camera tilts in the correct direction for each side
- **Pass Criteria:** Direction is correct 100% of the time, camera tilt
  mirrors correctly
- **Priority:** P0-Critical
- **Type:** Automated

### WR-FUNC-003: Wall-Run Duration and Stamina Drain
- **Precondition:** Player has full stamina (100 units)
- **Steps:**
  1. Initiate wall-run on a long flat wall
  2. Do not provide any additional input
  3. Observe stamina meter draining
  4. Note when player detaches from wall
- **Expected Result:** Stamina drains at 25 units/second, wall-run
  ends at 0 stamina (approximately 4 seconds), player drops with
  gravity, stamina bar flashes red at 25% remaining
- **Pass Criteria:** Duration within 4.0s ± 0.2s across all frame rates
- **Priority:** P0-Critical
- **Type:** Automated

### WR-FUNC-004: Wall-Run Jump (Wall Kick)
- **Precondition:** Player is actively wall-running
- **Steps:**
  1. Initiate wall-run
  2. Press jump button during wall-run
  3. Observe launch trajectory
- **Expected Result:** Player launches away from wall at 45-degree angle,
  gains 80% of normal jump height, preserves forward momentum,
  wall-kick sound plays, brief slow-motion effect (100ms)
- **Pass Criteria:** Launch angle 45° ± 5°, height within 10% of design value
- **Priority:** P0-Critical
- **Type:** Automated

### WR-FUNC-005: Wall-to-Wall Chaining
- **Precondition:** Two parallel walls within jump distance (3-5m apart)
- **Steps:**
  1. Wall-run on first wall
  2. Wall-kick toward second wall
  3. Observe if wall-run initiates on second wall
- **Expected Result:** Player chains from wall to wall, stamina continues
  draining (does not reset), chain counter increments in HUD,
  each successive wall-run is 10% shorter (diminishing returns)
- **Pass Criteria:** Chain works up to 5 walls, diminishing returns applied
- **Priority:** P1-High
- **Type:** Automated

---

## 2. Edge Case Tests

### WR-EDGE-001: Wall-Run on Curved Surfaces
- **Precondition:** Map with cylindrical column (radius > 2m)
- **Steps:**
  1. Sprint and jump toward curved wall
  2. Observe if wall-run activates and follows curvature
- **Expected Result:** Wall-run follows surface curvature if radius > 3m;
  rejected if radius < 3m (surface too curved); player slides off with
  "surface too curved" haptic feedback on rejection
- **Pass Criteria:** Curvature threshold correctly enforced, no jittering
- **Priority:** P1-High
- **Type:** Automated + Manual (visual)

### WR-EDGE-002: Wall-Run at Geometry Seams
- **Precondition:** Map with two wall meshes meeting at a seam
- **Steps:**
  1. Wall-run across a geometry seam where two meshes meet
  2. Observe if player passes smoothly or catches/stops
- **Expected Result:** Player traverses seam without interruption if
  surfaces are coplanar (within 5-degree tolerance); wall-run ends
  gracefully if angle exceeds tolerance
- **Pass Criteria:** No physics jitter, no player teleportation, no crash
- **Priority:** P0-Critical
- **Type:** Automated

### WR-EDGE-003: Wall-Run with Simultaneous Opposing Inputs
- **Precondition:** Player is wall-running
- **Steps:**
  1. During wall-run, press both "toward wall" and "away from wall"
  2. During wall-run, press both forward and backward simultaneously
- **Expected Result:** Conflicting inputs do not cause undefined behavior;
  "toward wall" takes priority to maintain wall contact; forward/backward
  conflict results in reduced speed (not reversal)
- **Pass Criteria:** No crashes, no stuck states, deterministic outcome
- **Priority:** P1-High
- **Type:** Automated

### WR-EDGE-004: Rapid Activation/Deactivation
- **Precondition:** Player near a valid wall
- **Steps:**
  1. Jump toward wall and immediately jump away (within 1 frame)
  2. Repeat 20 times rapidly using turbo input
- **Expected Result:** Each activation/deactivation pair completes cleanly;
  no animation desync, no stamina underflow, no orphaned particles;
  audio system does not stack wall-run sounds
- **Pass Criteria:** No degradation after 20 rapid cycles
- **Priority:** P1-High
- **Type:** Automated

### WR-EDGE-005: Save/Load During Wall-Run
- **Precondition:** Auto-save triggers during wall-run (checkpoint placed on wall path)
- **Steps:**
  1. Wall-run through an auto-save checkpoint
  2. After save, continue playing and then reload that save
  3. Observe player state on load
- **Expected Result:** Player loads in falling state at the wall-run position
  (wall-run is NOT restored on load — player falls to ground safely);
  stamina is at the value when saved; no stuck-to-wall state
- **Pass Criteria:** Player lands safely, no clipping through geometry
- **Priority:** P0-Critical
- **Type:** Manual

### WR-EDGE-006: Wall-Run at World Boundary
- **Precondition:** Valid wall-run surface at or near the level boundary
- **Steps:**
  1. Wall-run toward the end of the world boundary
  2. Observe behavior when wall geometry ends abruptly
- **Expected Result:** Player detaches gracefully when surface ends;
  kill volume or teleport-back triggers if player somehow exits boundary;
  no falling through the world
- **Pass Criteria:** Player never reaches out-of-bounds without recovery
- **Priority:** P0-Critical
- **Type:** Automated

---

## 3. Regression Tests

### WR-REG-001: Movement System Interaction
- **Test:** After wall-run ends, verify normal movement is fully restored
- **Verify:** Walk speed, sprint speed, crouch, slide, and jump all
  function identically to pre-wall-run behavior
- **Priority:** P0-Critical
- **Type:** Automated

### WR-REG-002: Combat System Interaction
- **Test:** Fire all weapon types during wall-run
- **Verify:** Hit detection works correctly, recoil patterns are adjusted
  for wall-run spread modifier, reload animation plays correctly,
  grenade throw arc accounts for wall-run velocity
- **Priority:** P0-Critical
- **Type:** Automated + Manual (feel)

### WR-REG-003: Death During Wall-Run
- **Test:** Player receives lethal damage while wall-running
- **Verify:** Death animation plays appropriate variant (not standard
  ground death), ragdoll detaches from wall correctly, kill cam
  functions normally, respawn does not place player on wall
- **Priority:** P1-High
- **Type:** Manual

### WR-REG-004: Ability Usage During Wall-Run
- **Test:** Activate each player ability while wall-running
- **Verify:** Abilities that are allowed during wall-run execute correctly;
  abilities that are blocked show "unavailable" feedback; no ability
  cancels wall-run unintentionally
- **Priority:** P1-High
- **Type:** Automated

---

## 4. Platform-Specific Tests

### WR-PLAT-001: Controller Analog Sensitivity (Console)
- **Test:** Wall-run approach angle using partial analog stick tilt
- **Verify:** Wall-run triggers at 50%+ stick deflection, does not
  trigger at < 30%, smooth transition between 30-50% (grace zone)
- **Platform:** PlayStation 5, Xbox Series X
- **Priority:** P1-High
- **Type:** Manual

### WR-PLAT-002: Keyboard Digital Input (PC)
- **Test:** Wall-run using WASD without analog nuance
- **Verify:** Digital input maps to full-speed wall-run, wall-kick angle
  is fixed at 45° (no analog control), mouse aim is unrestricted
  during wall-run
- **Platform:** PC (Steam)
- **Priority:** P1-High
- **Type:** Automated

### WR-PLAT-003: Haptic Feedback (DualSense)
- **Test:** Verify adaptive trigger and haptic feedback during wall-run
- **Verify:** Left trigger provides slight resistance during wall contact,
  haptic motor simulates footsteps on wall, wall-kick provides
  impulse feedback
- **Platform:** PlayStation 5
- **Priority:** P2-Medium
- **Type:** Manual (FEEL TEST — requires human evaluation)

---

## 5. Performance Tests

### WR-PERF-001: Frame Budget Impact
- **Test:** Measure frame time with wall-run active vs inactive
- **Pass Criteria:** Wall-run adds no more than 0.5ms to frame time
  at 60 FPS target; no frame time spikes > 2ms on activation
- **Priority:** P0-Critical
- **Type:** Automated (profiler capture)

### WR-PERF-002: Memory Allocation During Feature
- **Test:** Profile heap allocations during wall-run activation
- **Pass Criteria:** Zero per-frame heap allocations during sustained
  wall-run; activation allocations < 4KB total; all allocations freed
  on wall-run exit
- **Priority:** P1-High
- **Type:** Automated (memory profiler)

### WR-PERF-003: Worst-Case Entity Stress
- **Test:** Wall-run in area with 50+ active AI, 20 projectiles, 10 particle systems
- **Pass Criteria:** Frame rate stays above 30 FPS minimum (console),
  no hitches > 33ms, wall-run physics remain stable
- **Priority:** P1-High
- **Type:** Automated (stress test scene)

---

## 6. Coverage Summary

| Category | Test Count | Automated | Manual | Confidence |
|----------|-----------|-----------|--------|------------|
| Functional | 5 | 5 | 0 | High |
| Edge Cases | 6 | 4 | 2 | High |
| Regression | 4 | 2 | 2 | Medium |
| Platform | 3 | 1 | 2 | Medium |
| Performance | 3 | 3 | 0 | High |
| **Total** | **21** | **15** | **6** | — |

### Estimated Execution Time
- Automated suite: ~12 minutes
- Manual test pass: ~45 minutes
- Full regression (all categories): ~1 hour

### Known Risk Areas
1. Geometry seam traversal — historically flaky in physics engines
2. Network replication of wall-run state — latency-sensitive
3. Save/load during transient states — serialization edge case
4. Haptic feedback tuning — subjective, requires playtester feedback
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Defines purpose of generating gameplay test plans with specific coverage areas
- ST-02 (Sequential Step-by-Step Instructions) - Guides through feature decomposition, test design, and verification
- ST-03 (Contextual Framing) - Frames testing within game development context with industry-standard terminology
- DT-01 (Classification and Categorization) - Categorizes tests by type, priority, and automation potential
- QA-02 (Adversarial Thinking) - False-positive prevention ensures tests catch real gameplay bugs, not implementation details

**Related Prompts:**
- testing_automated_game_testing.md - For automating the test cases generated by this plan
- testing_platform_certification.md - For platform-specific certification requirements
- testing_unit_test_generation.md - For unit-level game logic tests
- testing_e2e_test_scenario_creation.md - For end-to-end gameplay scenario design
- performance_bottleneck_identification.md - For deep-diving performance issues found during testing
