---
title: "Unreal Engine Blueprint Architecture Review"
category: game-development/engines
description: "Review Unreal Blueprint graphs for complexity, nativization candidates, performance anti-patterns, and Blueprint/C++ boundary decisions"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-02
difficulty: intermediate
tags:
  - unreal-engine
  - blueprints
  - code-review
  - performance
  - architecture
updated: "2026-03-19"
---

# Unreal Engine Blueprint Architecture Review

**Objective:** Review Unreal Engine Blueprint implementations for architectural quality, performance anti-patterns (tick abuse, excessive casting, spaghetti graphs), nativization candidates, and proper Blueprint/C++ boundary decisions.

**When to Use:**
- Reviewing Blueprint-heavy projects before shipping or entering production
- Auditing Blueprint performance in projects with frame-rate issues
- Deciding which Blueprints should be converted to C++ (nativization candidates)
- Evaluating Blueprint architecture in a team codebase for consistency
- Reviewing Blueprint communication patterns (dispatchers, interfaces, direct references)
- Don't use when: reviewing pure C++ Unreal projects with no Blueprint usage

**Instructions:**

1. **Map Blueprint Architecture**
   - Identify the class hierarchy: which Blueprints inherit from which parent classes (Actor, Character, GameMode, PlayerController, etc.)
   - Document component composition per Blueprint (SceneComponent tree, ActorComponent attachments)
   - List Blueprint Interfaces implemented and their usage patterns
   - Note any multiple inheritance workarounds via interfaces
   - Identify reparenting risks (Blueprints inheriting from other Blueprints vs C++ base classes)

2. **Analyze Graph Complexity**
   - Count approximate node count per function/event graph
   - Measure nesting depth (branches within branches, sequences within sequences)
   - Evaluate event graph size — flag graphs with more than ~50 nodes in a single event
   - Check for "spaghetti" indicators: crossing wires, long-distance connections, lack of Reroute nodes
   - Identify collapsed graphs, macros, and functions that should be further decomposed
   - Flag any Blueprint with more than 15 custom functions or events as a complexity concern

3. **Identify Performance Anti-Patterns**
   - **Tick-heavy logic:** Blueprints with complex logic in Event Tick that should use Timers, event-driven patterns, or be moved to C++
   - **Cast on Tick:** Casting to a class every frame instead of caching the result in a variable
   - **Get All Actors of Class:** Called frequently instead of maintaining a cached reference or using subsystems
   - **Unnecessary string operations:** String comparisons for gameplay tags, FName usage where FGameplayTag should be used
   - **Construction Script abuse:** Heavy logic in Construction Script that runs in-editor and slows iteration
   - **Excessive Blueprint communication:** Chains of direct Blueprint references creating tight coupling
   - **Unoptimized loops:** ForEachLoop over large arrays every tick instead of event-driven updates

4. **Evaluate Blueprint/C++ Boundary**
   - Identify math-heavy calculations that would benefit from C++ (pathfinding, physics queries, procedural generation)
   - Flag frequently-ticked systems processing large datasets
   - Note Blueprints that are candidates for nativization (Blueprint-to-C++ compiler)
   - Evaluate whether base classes should be C++ with Blueprint-exposed UFUNCTION/UPROPERTY
   - Check if gameplay-critical systems have appropriate C++ backing (inventory, combat, networking)

5. **Check Interface and Communication Patterns**
   - Evaluate use of Blueprint Interfaces vs Event Dispatchers vs Direct References
   - Check for proper use of Event Dispatchers for one-to-many communication
   - Verify Blueprint Interfaces are used for polymorphic behavior across unrelated classes
   - Flag direct Blueprint-to-Blueprint references that create hard dependencies
   - Review Gameplay Tag usage for loose coupling where appropriate
   - Check for proper use of the Gameplay Ability System (GAS) if present

6. **CRITICAL: Verification Checklist**
   - [ ] **No infinite loops** — verify all loop constructs have proper exit conditions
   - [ ] **No missing null checks on casts** — every Cast node has both success and failure paths connected
   - [ ] **No Tick functions that should be timer-based** — logic that does not need per-frame execution uses SetTimerByFunctionName or event-driven flow
   - [ ] **No orphan event dispatchers** — every dispatcher has at least one binding
   - [ ] **No circular dependencies** — Blueprint A does not reference Blueprint B while B references A
   - [ ] **No unconnected execution pins** — all execution paths are complete (no dangling white wires)
   - [ ] **Cast results cached** — repeated casts to the same class store the result in a variable

**False-Positive Prevention:**

| Mistake | Correction |
|---------|------------|
| ❌ Flagging all Tick usage as a performance problem | ✅ Some systems legitimately need per-frame updates (input processing, smooth interpolation, real-time physics responses); flag only Tick logic that could be event-driven or timer-based |
| ❌ Demanding C++ conversion for simple prototype Blueprints | ✅ Consider project phase — prototypes and game jams benefit from Blueprint speed; production codebases warrant more C++ |
| ❌ Flagging all direct Blueprint references as anti-patterns | ✅ Direct references between tightly related Blueprints (e.g., Weapon → Projectile) are fine; flag only those creating fragile cross-system coupling |
| ❌ Treating all Get All Actors of Class as bad | ✅ Called once in BeginPlay and cached is perfectly acceptable; flag only when called per-frame or in hot loops |
| ❌ Ignoring project scale when reviewing architecture | ✅ A solo developer's jam project has different standards than a 20-person team production — scale recommendations accordingly |
| ❌ Requiring Blueprint Interfaces for every communication | ✅ Event Dispatchers and direct calls are appropriate when the relationship is known and stable; interfaces shine for polymorphism across unrelated types |

**Expected Output:** A structured review report that includes:

1. Blueprint architecture map with class hierarchy and component composition
2. Complexity metrics per Blueprint (node count, nesting depth, function count)
3. Prioritized list of performance anti-patterns with severity ratings
4. Blueprint/C++ boundary recommendations with migration priority
5. Communication pattern assessment with refactoring suggestions
6. Verification checklist results with specific findings

**Example Output:**

```markdown
# Blueprint Architecture Review — Third-Person Shooter Project

**Project:** ShooterGame (UE 5.4)
**Blueprints Reviewed:** 34 Blueprint classes
**Review Date:** 2026-03-19

---

## 1. Blueprint Architecture Map

### Class Hierarchy

```
AActor
├── BP_Weapon (base weapon class)
│   ├── BP_Weapon_Rifle
│   ├── BP_Weapon_Shotgun
│   └── BP_Weapon_RocketLauncher
├── BP_Projectile (base projectile)
│   ├── BP_Projectile_Bullet
│   └── BP_Projectile_Rocket
├── BP_Pickup_Base
│   ├── BP_Pickup_Health
│   ├── BP_Pickup_Ammo
│   └── BP_Pickup_Armor
└── BP_InteractableBase
    ├── BP_Door
    └── BP_Elevator

ACharacter
├── BP_ShooterCharacter (player)
└── BP_EnemyBase
    ├── BP_Enemy_Grunt
    ├── BP_Enemy_Heavy
    └── BP_Enemy_Sniper

APlayerController
└── BP_ShooterPlayerController

AGameModeBase
└── BP_ShooterGameMode

AGameStateBase
└── BP_ShooterGameState

AHUD
└── BP_ShooterHUD
```

### Interfaces Implemented

| Interface | Implemented By | Methods |
|-----------|---------------|---------|
| BPI_Interactable | BP_Door, BP_Elevator, BP_Pickup_* | Interact(APawn*), GetInteractionText() |
| BPI_Damageable | BP_ShooterCharacter, BP_EnemyBase, BP_Door | ApplyDamage(float, EDamageType), GetHealth() |
| BPI_TeamAware | BP_ShooterCharacter, BP_EnemyBase | GetTeamID(), IsHostile(AActor*) |

---

## 2. Complexity Analysis

### High Complexity (Action Required)

| Blueprint | Event Graph Nodes | Functions | Max Nesting | Verdict |
|-----------|-------------------|-----------|-------------|---------|
| BP_ShooterCharacter | ~320 | 24 | 5 levels | **CRITICAL** — decompose immediately |
| BP_EnemyBase | ~180 | 16 | 4 levels | **HIGH** — extract AI logic to BT/C++ |
| BP_Weapon | ~95 | 11 | 3 levels | **MODERATE** — consider C++ base |

### Acceptable Complexity

| Blueprint | Event Graph Nodes | Functions | Max Nesting | Verdict |
|-----------|-------------------|-----------|-------------|---------|
| BP_Projectile | ~30 | 4 | 2 levels | Clean |
| BP_Pickup_Base | ~20 | 3 | 1 level | Clean |
| BP_Door | ~25 | 3 | 2 levels | Clean |

### BP_ShooterCharacter — Detailed Findings

The main character Blueprint is the primary concern. The event graph
handles movement, shooting, reloading, sprinting, crouching, interaction,
health/damage, UI updates, and audio — all in a single Blueprint.

**Recommended decomposition:**
- Extract weapon management → BP_WeaponManager (ActorComponent)
- Extract health/damage → BP_HealthComponent (ActorComponent)
- Extract interaction system → BP_InteractionComponent (ActorComponent)
- Keep movement and input handling in the character Blueprint

---

## 3. Performance Anti-Patterns

### CRITICAL — Fix Immediately

**P1: Cast on Tick in BP_ShooterCharacter**
```
Event Tick → Cast to BP_ShooterPlayerController → Get Current Widget → Update Crosshair
```
**Issue:** Casting to the PlayerController every single frame.
**Fix:** Cache the controller reference in BeginPlay:
```
Event BeginPlay → Cast to BP_ShooterPlayerController → SET CachedController
Event Tick → GET CachedController → IsValid → Get Current Widget → Update Crosshair
```
**Impact:** Eliminates ~0.02ms per frame per character instance.

**P2: Get All Actors of Class in BP_EnemyBase Event Tick**
```
Event Tick → Get All Actors of Class (BP_ShooterCharacter) → ForEachLoop → Get Distance → Branch
```
**Issue:** Searching the entire world for player characters every frame
on every enemy instance. With 20 enemies, this is 20 full actor scans/frame.
**Fix:** Use a GameState subsystem that maintains a TArray of active players.
Enemies query the subsystem instead of scanning the world.
**Impact:** Eliminates O(n*m) actor iteration per frame.

### HIGH — Fix Before Release

**P3: Complex math in BP_Weapon Tick**
The bullet spread calculation performs 8 float operations, 3 random
range calls, and a Rotator construction every frame while firing.
**Fix:** Move spread calculation to a C++ UFUNCTION exposed to Blueprint.
**Impact:** ~4x speedup for math-heavy operations in native code.

**P4: String comparison in BP_EnemyBase**
```
Get Tag → ToString → Equals("Enemy.Type.Heavy") → Branch
```
**Issue:** Converting FGameplayTag to string for comparison.
**Fix:** Use native GameplayTag matching:
```
HasMatchingGameplayTag(EnemyTypeHeavy) → Branch
```

### MODERATE — Improve When Possible

**P5: Construction Script in BP_Weapon does line traces**
The weapon Blueprint performs 3 line traces in its Construction Script
to auto-detect attachment points. This runs every time a property changes
in the editor and causes noticeable editor hitches.
**Fix:** Gate with `IsRunningConstructionScript` check, or move to
an editor utility widget.

---

## 4. Blueprint/C++ Boundary Recommendations

### Should Move to C++ (Priority Order)

| Blueprint | Reason | Priority |
|-----------|--------|----------|
| BP_EnemyBase AI logic | Runs every tick on every enemy; math-heavy pathfinding queries | **P0** |
| BP_Weapon spread/recoil math | Float-heavy calculations every frame during fire | **P1** |
| BP_Projectile physics | Tick-based trajectory with collision queries | **P1** |
| BP_ShooterCharacter movement | Complex state machine with many branches per frame | **P2** |

### Fine as Blueprint (Keep)

| Blueprint | Reason |
|-----------|--------|
| BP_Pickup_* | Event-driven, no tick logic, simple overlap response |
| BP_Door / BP_Elevator | Timeline-driven animations, infrequent triggers |
| BP_ShooterHUD | UI logic belongs in Blueprint/UMG for designer iteration |
| BP_ShooterGameMode | Infrequent game flow events (match start, round end) |

### Recommended C++ Base Class Pattern

```cpp
// WeaponBase.h — C++ base with Blueprint-exposed API
UCLASS(Abstract, Blueprintable)
class SHOOTERGAME_API AWeaponBase : public AActor
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintCallable, Category = "Weapon")
    void StartFire();

    UFUNCTION(BlueprintCallable, Category = "Weapon")
    void StopFire();

    UFUNCTION(BlueprintImplementableEvent, Category = "Weapon")
    void OnFireEffects(); // VFX/SFX in Blueprint

protected:
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Weapon|Stats")
    float FireRate = 0.1f;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Weapon|Stats")
    float BaseDamage = 25.0f;

    // C++ handles the math-heavy spread calculation
    FRotator CalculateSpread(float CurrentHeat) const;

private:
    float CurrentHeat = 0.0f;
    FTimerHandle FireTimerHandle;
};
```

Blueprints then extend `AWeaponBase` and only handle visual/audio
customization via `OnFireEffects`, while all core logic runs in C++.

---

## 5. Communication Pattern Assessment

### Current Issues

| Pattern | Usage | Issue |
|---------|-------|-------|
| Direct reference: BP_EnemyBase → BP_ShooterCharacter | AI targeting | Hard-couples enemy to specific player class; breaks with different player types |
| Direct reference: BP_ShooterHUD → BP_Weapon | Ammo display | HUD directly reads weapon variables; no separation of concerns |
| Missing dispatchers | Pickup collection | BP_Pickup directly calls functions on character instead of broadcasting |

### Recommended Fixes

1. **Enemy targeting:** Use BPI_TeamAware interface for target resolution
   instead of casting directly to BP_ShooterCharacter.

2. **HUD updates:** Add Event Dispatchers on BP_Weapon:
   ```
   OnAmmoChanged(int CurrentAmmo, int MaxAmmo)
   OnWeaponSwapped(EWeaponType NewWeapon)
   OnReloadStarted(float ReloadDuration)
   ```
   HUD binds to these dispatchers — never reads weapon state directly.

3. **Pickup collection:** Fire a dispatcher OnPickupCollected(EPickupType,
   float Value) and let the character's health/ammo components listen.

---

## 6. Verification Checklist Results

- [x] **No infinite loops** — all ForEachLoops operate on finite arrays;
      no While loops found in any Blueprint
- [ ] **No missing null checks on casts** — **FAIL**: BP_EnemyBase casts
      to BP_ShooterCharacter without handling failure pin (3 instances)
- [ ] **No unnecessary Tick usage** — **FAIL**: 4 Blueprints use Tick
      where timers or events would suffice (see Section 3)
- [x] **No orphan event dispatchers** — all dispatchers have bindings
- [ ] **No circular dependencies** — **FAIL**: BP_ShooterCharacter
      references BP_Weapon, and BP_Weapon references BP_ShooterCharacter
      for owner checks. Refactor: weapon should use an interface.
- [x] **No unconnected execution pins** — all paths complete
- [ ] **Cast results cached** — **FAIL**: 6 uncached repeated casts
      identified across 3 Blueprints

---

## Summary

| Category | Status | Items |
|----------|--------|-------|
| Critical Performance | 🔴 | 2 issues (Cast-on-Tick, GetAllActors-on-Tick) |
| High Performance | 🟡 | 2 issues (math in BP, string tags) |
| Architecture | 🟡 | Character Blueprint needs decomposition |
| Communication | 🟡 | 3 direct references should use interfaces/dispatchers |
| C++ Migration | 🟡 | 4 Blueprints recommended for C++ base classes |
| Verification Failures | 🔴 | 4 checklist items failed |

**Top 3 Actions:**
1. Cache all cast results — quick win, fixes 6 instances
2. Replace GetAllActorsOfClass in enemy Tick with subsystem query
3. Decompose BP_ShooterCharacter into component Blueprints
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — opens with precise scope covering Blueprint complexity, performance, and boundary decisions
- ST-02 (Structured Sequential Instructions) — six numbered steps from architecture mapping through verification
- RT-02 (Systematic Classification) — classifies anti-patterns by severity and Blueprint/C++ boundary by priority
- RT-05 (Evidence-Based Reasoning) — requires specific node references and metrics to support findings
- QA-02 (False-Positive Prevention) — explicit table preventing over-flagging of legitimate Tick usage and prototype code

**Related Prompts:**
- `domain-game-development/engines/engines_unreal_cpp_patterns.md` — C++ best practices for code migrated from Blueprint
- `domain-game-development/performance/performance_profiling_analysis.md` — Frame-level performance profiling
- `domain-software-engineering/analysis/architecture/architecture_design_pattern_identification.md` — General design pattern identification
- `domain-software-engineering/analysis/quality/quality_code_complexity_analysis.md` — Complexity metrics analysis
