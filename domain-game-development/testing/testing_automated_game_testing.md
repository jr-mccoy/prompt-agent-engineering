---
title: "Automated Game Test Strategy"
category: game-development/testing
description: "Design automated testing strategies for games including unit tests for game logic, replay-based regression, bot playtesting, and CI integration"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-03
difficulty: advanced
tags:
  - testing
  - automation
  - ci-cd
  - bots
  - regression
  - unit-tests
updated: "2026-03-19"
---

# Automated Game Test Strategy

**Objective:** Design a comprehensive automated testing strategy for a game project covering unit tests for game logic, integration tests for system interactions, replay-based regression testing, bot-driven playtesting, and CI pipeline integration for build verification.

**When to Use:** Use this prompt when establishing a testing infrastructure for a game project, scaling QA beyond manual testing, setting up continuous integration for game builds, or when regression bugs are slipping through manual test passes. Critical for live-service games, multiplayer titles, and projects with frequent content updates.

**Instructions:**

1. **Identify Testable Layers**
   Classify game systems by testability and appropriate test approach:
   - **Pure game logic** (deterministic, no rendering): Damage calculation, inventory management, progression math, economy balancing, cooldown timers, state machines — ideal for unit tests
   - **System interactions** (multiple systems, minimal rendering): Combat pipeline (input → animation → hitbox → damage → feedback), AI decision trees with game state, quest/objective triggers — integration tests
   - **Rendering and presentation** (visual output): VFX playback, UI layout, shader correctness — screenshot comparison tests
   - **Full integration** (complete game loop): End-to-end gameplay scenarios, matchmaking flow, save/load round-trips — bot-driven playtests

2. **Design Unit Test Architecture**
   - Set up a test harness that initializes game systems without rendering or audio
   - Create a mock game world that provides deterministic physics and timing
   - Implement deterministic time control (fixed timestep, manual tick advancement)
   - Isolate systems under test from engine subsystems (use interfaces/abstractions)
   - Design test data factories for common game objects (characters, items, projectiles)
   - Establish naming convention: `test_[system]_[scenario]_[expected_result]`
   - Target: All pure game logic functions have unit tests with >80% branch coverage

3. **Build Replay/Recording System**
   - **Input recording:** Capture all player inputs (buttons, analog values, timestamps) with frame-accurate timing
   - **State snapshots:** Record game state at configurable intervals (every N frames or on key events)
   - **Deterministic replay:** Replay recorded inputs against the same game build with identical random seeds
   - **Divergence detection:** Compare replayed state snapshots against recorded snapshots; flag differences exceeding tolerance thresholds
   - **Replay versioning:** Tag replays with build number; auto-retire replays when systems they test are refactored
   - **Storage strategy:** Store replays as compressed input streams (small) rather than full state dumps (large)

4. **Design Bot Playtesting**
   - **Navigation mesh bots:** Traverse all walkable areas, report unreachable zones, measure traversal coverage percentage
   - **Fuzzy input bots:** Generate random but weighted input sequences; bias toward common player actions; detect crashes, soft-locks, and out-of-bounds escapes
   - **Goal-directed bots:** Follow scripted objectives (complete tutorial, play 10 matches, reach level cap); verify progression systems work end-to-end
   - **Stress test bots:** Spawn maximum concurrent players, simulate worst-case server load, measure performance degradation curves
   - **Exploration bots:** Systematically visit every room/area, interact with every interactable, verify no missing collisions or broken triggers
   - **Bot instrumentation:** Log all bot actions, capture screenshots on anomalies, report metrics (completion time, death count, coverage %)

5. **CI Pipeline Integration**
   - **Build stage:** Headless build (no GPU required), compile all platforms, build asset bundles
   - **Smoke test stage:** Boot game to main menu, load each level, verify no crashes within 30 seconds per level
   - **Unit test stage:** Run all unit tests (target: <5 minutes), fail build on any unit test failure
   - **Integration test stage:** Run system integration tests (target: <15 minutes), warn on failures (don't block)
   - **Replay regression stage:** Run top-50 critical replay tests, flag divergence > threshold
   - **Bot soak stage:** Run navigation bots for 10 minutes per level (run nightly, not per-commit)
   - **Performance regression stage:** Run benchmark scene, compare frame time against baseline, alert if >10% regression
   - **Total CI time target:** <30 minutes for commit-level, <2 hours for nightly

6. **Metrics and Reporting**
   - **Coverage tracking:** Lines covered, branches covered, systems exercised (map to design doc features)
   - **Flaky test detection:** Track tests that pass/fail inconsistently across runs; auto-quarantine after 3 flakes in 7 days
   - **Regression dashboards:** Visualize test pass rates over time, frame time trends, memory usage trends
   - **Bot coverage maps:** Heatmap visualization of areas bots have traversed (identify dead zones)
   - **Build health score:** Composite metric (test pass rate × coverage × performance stability)
   - **Alert thresholds:** Page on P0 failures, Slack on P1, daily digest for P2+

7. **CRITICAL: Verification Checklist**
   - Verify all tests are deterministic (run same test 10 times, expect identical results)
   - Verify CI pipeline completes in <30 minutes for commit-level checks
   - Verify bot coverage reaches >90% of navigable space within configured run time
   - Verify replay tests correctly detect known regressions (run against intentionally broken build)
   - Verify flaky test quarantine does not silently hide real failures
   - Verify performance regression detection catches a deliberate 15% frame time increase

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Test rendering output pixel-by-pixel (use screenshot comparison with perceptual tolerance, e.g., SSIM > 0.98)
- Require 100% code coverage for game code (focus coverage on game logic; rendering and input layers are better tested manually)
- Treat floating-point comparison as exact (always use epsilon-based comparison for physics values)
- Run physics-dependent tests without fixed timestep (non-determinism will cause flaky tests)
- Put slow integration tests in the commit-level CI gate (separate fast and slow test tiers)
- Assume bot behavior is representative of real player behavior (bots find different bugs than humans)

✅ **DO:**
- Handle non-determinism from physics and floating-point by using tolerance ranges and deterministic seeds
- Separate fast unit tests (<5 min) from slow integration tests (<15 min) and soak tests (nightly) in CI
- Version-tag all replay recordings with the build hash they were captured on
- Include "canary tests" — intentionally simple tests that should always pass to detect infrastructure failures
- Maintain a "golden build" baseline for performance regression comparison
- Log full reproduction context on test failure (build hash, platform, random seed, input sequence)
- Review quarantined flaky tests weekly — don't let them accumulate silently

**Expected Output:** A complete automated testing strategy document including:
- Test layer classification for each game system
- Unit test architecture with code examples
- Replay system design specification
- Bot types and their coverage objectives
- CI pipeline stage definitions with time budgets
- Metrics dashboard specification
- Flaky test management policy
- Coverage confidence ratings per test layer

**Example Output:**

```markdown
# Automated Testing Strategy: Multiplayer Arena Shooter

## Project Context
- Engine: Unreal Engine 5.4
- Platforms: PC (Steam), PlayStation 5, Xbox Series X
- Multiplayer: 6v6 online, dedicated servers
- Update cadence: Bi-weekly patches, seasonal content drops

---

## 1. Test Layer Classification

| System | Layer | Test Type | Deterministic | Priority |
|--------|-------|-----------|---------------|----------|
| Damage Calculation | Pure Logic | Unit Test | Yes | P0 |
| Weapon Stats/Balancing | Pure Logic | Unit Test | Yes | P0 |
| Inventory Management | Pure Logic | Unit Test | Yes | P0 |
| Matchmaking Rating (MMR) | Pure Logic | Unit Test | Yes | P0 |
| Cooldown/Ability Timers | Pure Logic | Unit Test | Yes | P0 |
| Progression/XP System | Pure Logic | Unit Test | Yes | P1 |
| Loadout Validation | Pure Logic | Unit Test | Yes | P1 |
| Combat Pipeline | System Interaction | Integration | Seeded | P0 |
| AI Bot Behavior Trees | System Interaction | Integration | Seeded | P1 |
| Pickup/Spawn System | System Interaction | Integration | Seeded | P1 |
| Network State Replication | System Interaction | Integration | No* | P0 |
| UI Layout/HUD | Rendering | Screenshot | N/A | P2 |
| VFX Playback | Rendering | Screenshot | N/A | P2 |
| Full Match Flow | Full Integration | Bot Playtest | No | P0 |
| Matchmaking End-to-End | Full Integration | Bot Playtest | No | P0 |

*Network tests use simulated latency with controlled jitter ranges.

---

## 2. Unit Test Architecture

### Test Harness Setup
```cpp
// GameTestHarness.h — Minimal game world for logic testing
class FGameTestHarness {
public:
    FGameTestHarness() {
        // Initialize subsystems WITHOUT renderer, audio, or input
        World = CreateMinimalWorld();
        World->SetFixedTimestep(1.0f / 60.0f);  // Deterministic 60Hz
        World->SetRandomSeed(42);                 // Repeatable RNG
    }

    void Tick(int NumFrames = 1) {
        for (int i = 0; i < NumFrames; i++) {
            World->TickFrame();
        }
    }

    ACharacter* SpawnTestCharacter(FCharacterConfig Config);
    AWeapon* SpawnTestWeapon(FWeaponConfig Config);
    void SimulateHit(ACharacter* Source, ACharacter* Target,
                     FHitResult HitInfo);

private:
    UMinimalGameWorld* World;
};
```

### Example Unit Tests
```cpp
// DamageCalculation.test.cpp
TEST_F(DamageSystemTest, HeadshotDealsDoubleBaseDamage) {
    // Arrange
    auto* Attacker = Harness.SpawnTestCharacter(DefaultConfig);
    auto* Victim = Harness.SpawnTestCharacter(DefaultConfig);
    auto* Rifle = Harness.SpawnTestWeapon(AssaultRifleConfig);
    Attacker->EquipWeapon(Rifle);

    FHitResult Hit;
    Hit.BoneName = "head";
    Hit.Distance = 20.0f;  // meters

    // Act
    float DamageDealt = DamageSystem::CalculateDamage(
        Rifle->GetBaseDamage(), Hit, Attacker, Victim);

    // Assert
    EXPECT_FLOAT_EQ(DamageDealt, Rifle->GetBaseDamage() * 2.0f);
}

TEST_F(DamageSystemTest, DamageFalloffReducesDamageAtRange) {
    auto* Attacker = Harness.SpawnTestCharacter(DefaultConfig);
    auto* Victim = Harness.SpawnTestCharacter(DefaultConfig);
    auto* Rifle = Harness.SpawnTestWeapon(AssaultRifleConfig);
    // Rifle falloff: 100% at 0-30m, 50% at 50m+

    FHitResult CloseHit{.BoneName="body", .Distance=15.0f};
    FHitResult FarHit{.BoneName="body", .Distance=55.0f};

    float CloseDmg = DamageSystem::CalculateDamage(
        Rifle->GetBaseDamage(), CloseHit, Attacker, Victim);
    float FarDmg = DamageSystem::CalculateDamage(
        Rifle->GetBaseDamage(), FarHit, Attacker, Victim);

    EXPECT_FLOAT_EQ(CloseDmg, Rifle->GetBaseDamage());
    EXPECT_NEAR(FarDmg, Rifle->GetBaseDamage() * 0.5f, 0.01f);
}

TEST_F(DamageSystemTest, ShieldAbsorbsDamageBeforeHealth) {
    auto* Victim = Harness.SpawnTestCharacter(DefaultConfig);
    Victim->SetHealth(100.0f);
    Victim->SetShield(50.0f);

    DamageSystem::ApplyDamage(Victim, 80.0f);

    EXPECT_FLOAT_EQ(Victim->GetShield(), 0.0f);
    EXPECT_FLOAT_EQ(Victim->GetHealth(), 70.0f);  // 80 - 50 shield = 30 to health
}

TEST_F(MatchmakingTest, MMRConvergesAfter10Matches) {
    FPlayerMMR Player{.Rating=1500, .Uncertainty=350};

    // Simulate 10 wins against equal opponents
    for (int i = 0; i < 10; i++) {
        Player = MMRSystem::UpdateRating(Player, 1500, EMatchResult::Win);
    }

    // Uncertainty should decrease significantly
    EXPECT_LT(Player.Uncertainty, 150.0f);
    // Rating should increase
    EXPECT_GT(Player.Rating, 1600.0f);
}
```

---

## 3. Replay System Design

### Recording Format
```
ReplayFile {
    Header {
        BuildHash: string        // "a3f7c2b"
        BuildNumber: uint32      // 4521
        MapName: string          // "Arena_Colosseum"
        PlayerCount: uint8       // 12
        RandomSeed: uint64       // 0xDEADBEEF
        RecordDate: timestamp
        TickRate: float          // 60.0
    }
    InputFrames[] {
        FrameNumber: uint32
        PlayerInputs[PlayerCount] {
            MoveX: float16       // -1.0 to 1.0
            MoveY: float16
            LookYaw: float16
            LookPitch: float16
            ButtonMask: uint32   // bit flags for all buttons
        }
    }
    StateSnapshots[] {           // Every 300 frames (5 seconds)
        FrameNumber: uint32
        PlayerStates[PlayerCount] {
            Position: Vector3
            Health: float
            Shield: float
            ActiveWeapon: uint8
            AmmoCount: uint16
        }
        WorldChecksum: uint64    // Hash of relevant world state
    }
}
```

### Divergence Thresholds
| Property | Tolerance | Action on Exceed |
|----------|-----------|------------------|
| Position | 0.1 units | WARN at 0.1, FAIL at 1.0 |
| Health/Shield | 0.01 | FAIL (deterministic system) |
| Ammo Count | 0 | FAIL (deterministic system) |
| World Checksum | exact match | FAIL |
| Frame Timing | 1 frame drift | WARN, re-sync and continue |

---

## 4. Bot Specifications

### Navigation Coverage Bot
- **Purpose:** Verify all walkable space is reachable
- **Method:** Flood-fill navigation mesh, attempt to reach every nav node
- **Coverage Target:** >95% of nav mesh nodes visited within 10 minutes
- **Reporting:** Heatmap PNG per level, list of unreachable nodes
- **Run Frequency:** Nightly

### Fuzzy Input Bot
- **Purpose:** Find crashes and soft-locks through random play
- **Method:** Weighted random input (60% movement, 20% combat,
  10% abilities, 10% UI interaction)
- **Session Length:** 30 minutes per bot instance
- **Concurrency:** 12 bots (simulating full match)
- **Detection:** Monitor for crashes, hangs (no state change >10s),
  out-of-bounds positions, NaN values in game state
- **Run Frequency:** Nightly, 4-hour soak on weekends

### Goal-Directed Bot
- **Purpose:** Verify game flow and progression systems
- **Objectives:**
  1. Complete tutorial sequence (expected: <5 minutes)
  2. Play 10 matches to completion (expected: <60 minutes)
  3. Purchase item from store (expected: <1 minute)
  4. Equip loadout and enter matchmaking (expected: <30 seconds)
  5. Earn first achievement/trophy (expected: within first 3 matches)
- **Failure Criteria:** Objective not completed within 3x expected time
- **Run Frequency:** Per-commit (objectives 1, 4), Nightly (all)

---

## 5. CI Pipeline Stages

```yaml
# .github/workflows/game-ci.yml (simplified)
stages:
  build:
    timeout: 10m
    steps:
      - compile: headless-server (no GPU)
      - compile: client (all platforms)
      - package: asset bundles
    on_failure: BLOCK — notify #build-channel

  smoke_test:
    timeout: 5m
    needs: build
    steps:
      - boot_to_menu: verify main menu loads
      - load_each_level: 30s per level, verify no crash
      - verify_no_errors: check log for fatal/error entries
    on_failure: BLOCK — page on-call engineer

  unit_tests:
    timeout: 5m
    needs: build
    steps:
      - run: GameLogicTests (damage, inventory, MMR, economy)
      - run: NetworkSerializationTests
      - run: ConfigValidationTests
    coverage_threshold: 80%
    on_failure: BLOCK — notify PR author

  integration_tests:
    timeout: 15m
    needs: smoke_test
    steps:
      - run: CombatPipelineTests (with mock world)
      - run: SpawnSystemTests
      - run: PickupInteractionTests
    on_failure: WARN — add label to PR, do not block

  replay_regression:
    timeout: 10m
    needs: smoke_test
    steps:
      - run: top 50 critical replays
      - compare: state snapshots against recorded baseline
    on_failure: WARN — flag divergent replays in PR comment

  # --- NIGHTLY ONLY ---
  bot_soak:
    timeout: 120m
    schedule: "0 2 * * *"
    steps:
      - run: NavigationBot (all maps, 10 min each)
      - run: FuzzyInputBot (12 instances, 30 min)
      - run: GoalBot (full objective suite)
    on_failure: Create JIRA ticket, attach logs + screenshots

  performance_benchmark:
    timeout: 20m
    schedule: "0 3 * * *"
    steps:
      - run: BenchmarkScene at 4K, capture 60s of frame times
      - compare: against golden baseline
      - alert: if P95 frame time regresses >10%
    on_failure: Alert #performance-channel with comparison graphs
```

### Time Budget Summary
| Stage | Time | Trigger | Blocking? |
|-------|------|---------|-----------|
| Build | 10 min | Every commit | Yes |
| Smoke Test | 5 min | Every commit | Yes |
| Unit Tests | 5 min | Every commit | Yes |
| Integration Tests | 15 min | Every commit | No (warn) |
| Replay Regression | 10 min | Every commit | No (warn) |
| Bot Soak | 120 min | Nightly | No (ticket) |
| Performance | 20 min | Nightly | No (alert) |
| **Commit Total** | **~30 min** | — | — |

---

## 6. Metrics Dashboard

### Build Health Score Formula
```
BuildHealth = (UnitPassRate × 0.4)
            + (IntegrationPassRate × 0.2)
            + (ReplayPassRate × 0.2)
            + (PerformanceStability × 0.2)

Where:
  UnitPassRate = passing_unit_tests / total_unit_tests
  IntegrationPassRate = passing_integration / total_integration
  ReplayPassRate = non_divergent_replays / total_replays
  PerformanceStability = 1.0 - (frame_time_regression_pct / 100)
```

### Flaky Test Policy
- Test fails inconsistently across 3 runs in 7 days → auto-quarantine
- Quarantined tests still run but don't block the pipeline
- Weekly review meeting: fix or delete quarantined tests
- Maximum quarantine duration: 14 days (auto-delete if not fixed)
- Dashboard shows quarantine count — treat >10 as a team health alert

### Alert Routing
| Severity | Channel | Response Time |
|----------|---------|---------------|
| Build broken | PagerDuty | <15 minutes |
| P0 test failure | #qa-alerts Slack | <1 hour |
| P1 test failure | PR comment | Before merge |
| Performance regression | #performance Slack | Next business day |
| Flaky test quarantine | Weekly digest email | Weekly review |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Defines purpose of designing comprehensive automated testing strategy
- ST-02 (Sequential Step-by-Step Instructions) - Guides through test layers, architecture, replay, bots, and CI
- RT-02 (Multi-Dimensional Analysis) - Covers unit, integration, replay, bot, and performance testing dimensions
- RT-05 (Comparative Analysis) - Compares test approaches by determinism, speed, and coverage characteristics
- DS-03 (Technical Specification) - Provides concrete code examples, YAML configs, and data formats

**Related Prompts:**
- testing_gameplay_test_plan.md - For generating the manual test plans that complement automation
- testing_platform_certification.md - For platform-specific certification test requirements
- testing_unit_test_generation.md - For detailed unit test generation patterns
- testing_flaky_test_detection.md - For deep-diving flaky test diagnosis
- devops_cicd_pipeline_analysis.md - For CI/CD pipeline optimization beyond game-specific needs
- testing_performance_load_test_planning.md - For load testing multiplayer server infrastructure
