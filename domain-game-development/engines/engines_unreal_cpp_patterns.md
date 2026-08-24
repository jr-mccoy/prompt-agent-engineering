---
title: "Unreal Engine C++ Best Practices Analysis"
category: game-development/engines
description: "Analyze Unreal C++ code for proper UPROPERTY/UFUNCTION usage, garbage collection safety, replication markup, and memory management"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-03
difficulty: advanced
tags:
  - unreal-engine
  - cpp
  - code-review
  - garbage-collection
  - replication
  - best-practices
updated: "2026-03-19"
---

# Unreal Engine C++ Best Practices Analysis

**Objective:** Analyze Unreal Engine C++ code for correct usage of UPROPERTY/UFUNCTION macros, garbage collection safety, replication markup, Gameplay Ability System patterns, Enhanced Input setup, and proper Unreal memory management conventions.

**When to Use:**
- Reviewing Unreal C++ code for production readiness
- Auditing garbage collection safety to prevent crashes from dangling pointers
- Verifying replication markup for multiplayer projects
- Evaluating UPROPERTY/UFUNCTION specifier usage for Blueprint integration
- Reviewing GAS (Gameplay Ability System) implementation patterns
- Checking Enhanced Input System setup and binding patterns
- Don't use when: reviewing Blueprint-only projects (see `engines_unreal_blueprint_review.md` instead)

**Instructions:**

1. **Verify UPROPERTY Specifiers**
   - Check `EditAnywhere` vs `EditDefaultsOnly` vs `EditInstanceOnly` — ensure designers cannot edit values that should be locked to the CDO, and vice versa
   - Check `BlueprintReadWrite` vs `BlueprintReadOnly` — mutable state exposed to Blueprint should be intentional, not accidental
   - Verify `Category` organization — properties should be grouped logically (e.g., `Category = "Weapon|Stats"`, `Category = "Weapon|Visual"`)
   - Check `meta` specifiers — `ClampMin`, `ClampMax`, `AllowPrivateAccess`, `MakeEditWidget` usage
   - Verify `Transient` on runtime-only state that should not serialize
   - Check `SaveGame` on properties that must persist through serialization
   - Flag missing UPROPERTY on UObject* members (garbage collection hazard)

2. **Check Garbage Collection Safety**
   - **Raw UObject pointers without UPROPERTY** — any `UObject*`, `AActor*`, `UActorComponent*` stored as a class member MUST be marked UPROPERTY or the GC will not track it
   - **TWeakObjectPtr vs raw pointers** — references to actors you do not own should use `TWeakObjectPtr<AActor>` to gracefully handle destruction
   - **Preventing dangling references** — verify OnDestroyed/EndPlay delegates are used to null out references to other actors
   - **Lambda captures** — lambdas capturing `this` or UObject pointers in async contexts (timers, delegates) risk dangling references after GC
   - **NewObject vs SpawnActor** — ensure proper outer is set for NewObject; SpawnActor automatically handles world registration
   - **AddToRoot / RemoveFromRoot** — flag unnecessary AddToRoot calls that prevent GC

3. **Validate Replication Markup**
   - Verify `DOREPLIFETIME` macros in `GetLifetimeReplicatedProps` for all replicated properties
   - Check `ReplicatedUsing` callback naming convention (OnRep_PropertyName)
   - Verify `UFUNCTION(Server, Reliable)` vs `UFUNCTION(Server, Unreliable)` — gameplay-critical RPCs must be Reliable; frequent movement updates should be Unreliable
   - Check `UFUNCTION(NetMulticast)` for cosmetic effects (VFX, SFX) vs gameplay logic
   - Verify authority checks (`HasAuthority()`, `GetLocalRole()`) before state modifications
   - Check `COND_` conditions in DOREPLIFETIME for bandwidth optimization (e.g., `COND_OwnerOnly`, `COND_SkipOwner`)
   - Verify `bReplicates = true` in constructor for replicated actors

4. **Review Constructor Patterns (CDO Best Practices)**
   - Verify constructor only sets default values — no gameplay logic, no world access, no spawning
   - Check `PostInitializeComponents` vs `BeginPlay` usage — PICs runs before BeginPlay, use for component setup that other actors depend on
   - Verify `CreateDefaultSubobject` is only called in constructor (not at runtime)
   - Check that CDO (Class Default Object) is not mutated at runtime
   - Verify `ObjectInitializer` usage for component class overrides
   - Flag any `GetWorld()`, `GetGameInstance()`, or `GetPlayerController()` calls in constructors (world does not exist yet)

5. **Analyze Memory Patterns**
   - **TSharedPtr vs TWeakPtr vs raw** — shared ownership for non-UObject types, weak references for breaking cycles
   - **FName vs FString vs FText** — FName for identifiers (case-insensitive, interned), FString for manipulation, FText for display/localization
   - **TArray preallocation** — `Reserve()` before known-size fills, `SetNum` for fixed-size arrays
   - **TMap vs TMultiMap** — verify correct container for one-to-one vs one-to-many lookups
   - **Move semantics** — `MoveTemp()` for Unreal containers instead of `std::move()`
   - **FStructOnScope / TInlineAllocator** — stack allocation patterns for temporary data
   - **String formatting** — `FString::Printf` vs `FString::Format` performance characteristics

6. **CRITICAL: Verification Checklist**
   - [ ] **No raw UObject* without UPROPERTY** — every UObject-derived pointer stored as a class member has UPROPERTY markup
   - [ ] **No replication without authority checks** — all state modifications on replicated actors verify HasAuthority() or are inside Server RPCs
   - [ ] **No CDO mutations at runtime** — GetClass()->GetDefaultObject() is never modified outside the constructor
   - [ ] **No GetWorld() in constructors** — constructor only uses CreateDefaultSubobject and sets default values
   - [ ] **No missing DOREPLIFETIME** — every property marked `Replicated` or `ReplicatedUsing` has a corresponding DOREPLIFETIME entry
   - [ ] **No Reliable NetMulticast for cosmetics** — visual/audio effects use Unreliable multicast to avoid bandwidth waste
   - [ ] **No FString where FName suffices** — identifiers, tags, and lookup keys use FName

**False-Positive Prevention:**

| Mistake | Correction |
|---------|------------|
| ❌ Flagging TArray passed by value in small-data contexts | ✅ Passing TArray<int32> with fewer than ~10 elements by value is acceptable and sometimes clearer; flag only large array copies in hot paths |
| ❌ Requiring UPROPERTY on non-UObject pointers (raw int*, float*) | ✅ UPROPERTY is only required for UObject-derived pointers; raw pointers to non-UObject types do not participate in GC |
| ❌ Treating all EditAnywhere as dangerous | ✅ EditAnywhere is appropriate for properties designers should tune per-instance (spawn rates, colors, volumes); EditDefaultsOnly is for class-level constants |
| ❌ Flagging all FString usage as inefficient | ✅ FString is correct for string manipulation, concatenation, and formatting; FName is for identifiers and lookups only |
| ❌ Ignoring Unreal Engine version differences | ✅ APIs change between UE versions — verify findings against the project's target version (e.g., Enhanced Input vs legacy Input, Iris vs Chaos physics) |
| ❌ Requiring TWeakObjectPtr everywhere | ✅ UPROPERTY-marked pointers are already GC-tracked; TWeakObjectPtr is for non-UPROPERTY references or when you expect the target may be destroyed independently |

**Expected Output:** A structured analysis report that includes:

1. UPROPERTY/UFUNCTION specifier audit with corrections
2. Garbage collection safety findings with severity
3. Replication markup validation results
4. Constructor pattern review
5. Memory management recommendations
6. Verification checklist results with specific code references

**Example Output:**

```markdown
# Unreal C++ Best Practices Review — Multiplayer Weapon System

**Project:** MultiplayerShooter (UE 5.4)
**Files Reviewed:** 12 C++ header/source pairs
**Review Date:** 2026-03-19

---

## 1. UPROPERTY/UFUNCTION Specifier Audit

### Issues Found

**CRITICAL — GC Hazard: Raw UObject* without UPROPERTY**

File: `WeaponComponent.h`, Line 47
```cpp
// BEFORE (dangerous — GC does not track this pointer)
private:
    UParticleSystemComponent* MuzzleFlashComponent;
    USoundCue* FireSound;

// AFTER (safe — GC tracks both pointers)
private:
    UPROPERTY()
    UParticleSystemComponent* MuzzleFlashComponent;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Weapon|Audio",
              meta = (AllowPrivateAccess = "true"))
    USoundCue* FireSound;
```
**Impact:** Without UPROPERTY, the garbage collector may destroy these
objects while the WeaponComponent still holds pointers to them, causing
a crash on next access.

---

**HIGH — Incorrect Specifier: EditAnywhere on Damage Table**

File: `WeaponDataAsset.h`, Line 23
```cpp
// BEFORE (allows per-instance override of damage table — unintended)
UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Weapon")
TMap<EHitZone, float> DamageMultiplierTable;

// AFTER (locked to CDO — designers edit in the asset, not per-instance)
UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Weapon|Damage")
TMap<EHitZone, float> DamageMultiplierTable;
```
**Reason:** Damage tables should be consistent across all instances of
a weapon type. Per-instance editing risks inconsistent game balance.

---

**MODERATE — Missing Category Organization**

File: `ProjectileBase.h`
```cpp
// BEFORE (flat, unsorted properties)
UPROPERTY(EditDefaultsOnly)
float Speed;
UPROPERTY(EditDefaultsOnly)
float Damage;
UPROPERTY(EditDefaultsOnly)
UStaticMesh* Mesh;
UPROPERTY(EditDefaultsOnly)
UParticleSystem* TrailEffect;

// AFTER (organized by concern)
UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Projectile|Movement")
float Speed = 3000.0f;

UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Projectile|Combat")
float Damage = 25.0f;

UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Projectile|Visual")
UStaticMesh* Mesh;

UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Projectile|Visual")
UParticleSystem* TrailEffect;
```

---

## 2. Garbage Collection Safety

### Findings

| Severity | File | Issue | Fix |
|----------|------|-------|-----|
| CRITICAL | WeaponComponent.h:47 | Raw `UParticleSystemComponent*` without UPROPERTY | Add UPROPERTY() |
| CRITICAL | WeaponComponent.h:48 | Raw `USoundCue*` without UPROPERTY | Add UPROPERTY() |
| HIGH | EnemyAIController.cpp:112 | Lambda captures `this` in async timer callback | Use `TWeakObjectPtr<ThisClass>` weak self pattern |
| HIGH | InventoryManager.h:34 | `TArray<APickupActor*>` without UPROPERTY | Add UPROPERTY() — array of UObject pointers needs GC tracking |
| MODERATE | ProjectileBase.cpp:67 | Spawned actor pointer stored in local only | Acceptable if lifetime is managed by world |

### Lambda Capture Fix Pattern

File: `EnemyAIController.cpp`, Line 112
```cpp
// BEFORE (dangerous — 'this' may be GC'd before timer fires)
GetWorldTimerManager().SetTimer(PatrolTimer, [this]()
{
    MoveToNextPatrolPoint();  // crash if 'this' is destroyed
}, PatrolInterval, true);

// AFTER (weak self pattern — safely checks validity)
TWeakObjectPtr<AEnemyAIController> WeakSelf(this);
GetWorldTimerManager().SetTimer(PatrolTimer, [WeakSelf]()
{
    if (AEnemyAIController* StrongSelf = WeakSelf.Get())
    {
        StrongSelf->MoveToNextPatrolPoint();
    }
}, PatrolInterval, true);
```

---

## 3. Replication Markup Validation

### Missing DOREPLIFETIME

File: `WeaponComponent.h` / `WeaponComponent.cpp`
```cpp
// Header declares replicated property:
UPROPERTY(ReplicatedUsing = OnRep_CurrentAmmo)
int32 CurrentAmmo;

UPROPERTY(Replicated)
EWeaponState WeaponState;

// BUT GetLifetimeReplicatedProps is MISSING WeaponState:
void UWeaponComponent::GetLifetimeReplicatedProps(
    TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    DOREPLIFETIME_CONDITION(UWeaponComponent, CurrentAmmo, COND_OwnerOnly);
    // WeaponState is MISSING — will not replicate despite Replicated specifier
}
```
**Fix:** Add `DOREPLIFETIME(UWeaponComponent, WeaponState);`

### Missing Authority Check

File: `CharacterCombat.cpp`, Line 89
```cpp
// BEFORE (modifies replicated state without authority check)
void AShooterCharacter::TakeDamage_Custom(float DamageAmount)
{
    CurrentHealth -= DamageAmount;  // replicated property
    if (CurrentHealth <= 0.0f)
    {
        Die();
    }
}

// AFTER (only server modifies replicated state)
void AShooterCharacter::TakeDamage_Custom(float DamageAmount)
{
    if (!HasAuthority())
    {
        return;  // clients must not modify replicated health
    }

    CurrentHealth = FMath::Max(0.0f, CurrentHealth - DamageAmount);
    if (CurrentHealth <= 0.0f)
    {
        Die();
    }
}
```

### Reliable vs Unreliable Audit

| RPC | Current | Recommended | Reason |
|-----|---------|-------------|--------|
| `ServerFire()` | Reliable | **Unreliable** | Fires every 0.1s; reliable queue will back up; missed shots are acceptable |
| `ServerReload()` | Reliable | Reliable ✓ | Infrequent, gameplay-critical state change |
| `MulticastPlayFireVFX()` | Reliable | **Unreliable** | Cosmetic effect; missing one is acceptable, bandwidth is not |
| `ServerRequestRespawn()` | Reliable | Reliable ✓ | Infrequent, must not be lost |
| `MulticastPlayHitReaction()` | Reliable | **Unreliable** | Cosmetic animation; should not clog reliable buffer |

---

## 4. Constructor Pattern Review

### CDO Violation Found

File: `WeaponComponent.cpp`, Line 15
```cpp
// BEFORE (accesses world in constructor — CDO has no world)
UWeaponComponent::UWeaponComponent()
{
    PrimaryComponentTick.bCanEverTick = true;
    FireRate = 0.1f;

    // ERROR: GetWorld() returns nullptr during CDO construction
    if (UWorld* World = GetWorld())
    {
        AGameState* GS = World->GetGameState<AGameState>();
        // ... reads balance data from GameState
    }
}

// AFTER (defer world access to BeginPlay)
UWeaponComponent::UWeaponComponent()
{
    PrimaryComponentTick.bCanEverTick = true;
    FireRate = 0.1f;
    // Default values only — no world access
}

void UWeaponComponent::BeginPlay()
{
    Super::BeginPlay();
    // Safe to access world here
    if (AGameState* GS = GetWorld()->GetGameState<AGameState>())
    {
        LoadBalanceData(GS);
    }
}
```

### CreateDefaultSubobject Misuse

File: `ShooterCharacter.cpp`, Line 203
```cpp
// BEFORE (CreateDefaultSubobject called at runtime — will crash)
void AShooterCharacter::EquipWeapon(TSubclassOf<UWeaponComponent> WeaponClass)
{
    // WRONG: CreateDefaultSubobject is constructor-only
    CurrentWeapon = CreateDefaultSubobject<UWeaponComponent>(TEXT("Weapon"));
}

// AFTER (use NewObject + RegisterComponent at runtime)
void AShooterCharacter::EquipWeapon(TSubclassOf<UWeaponComponent> WeaponClass)
{
    CurrentWeapon = NewObject<UWeaponComponent>(this, WeaponClass);
    CurrentWeapon->RegisterComponent();
    CurrentWeapon->AttachToComponent(GetMesh(),
        FAttachmentTransformRules::SnapToTargetNotIncludingScale,
        TEXT("weapon_socket"));
}
```

---

## 5. Memory Management Recommendations

### FString vs FName Misuse

File: `InventoryManager.cpp`, Line 78
```cpp
// BEFORE (FString used as map key — expensive hashing and comparison)
TMap<FString, FInventorySlot> InventorySlots;
FInventorySlot* Slot = InventorySlots.Find(TEXT("PrimaryWeapon"));

// AFTER (FName is interned — O(1) comparison, cheaper hashing)
TMap<FName, FInventorySlot> InventorySlots;
FInventorySlot* Slot = InventorySlots.Find(FName("PrimaryWeapon"));
```

### TArray Preallocation

File: `EnemySpawner.cpp`, Line 45
```cpp
// BEFORE (grows array dynamically during loop)
TArray<AEnemyBase*> SpawnedEnemies;
for (int32 i = 0; i < WaveSize; ++i)
{
    SpawnedEnemies.Add(SpawnEnemy()); // reallocates on growth
}

// AFTER (preallocate known size)
TArray<AEnemyBase*> SpawnedEnemies;
SpawnedEnemies.Reserve(WaveSize);
for (int32 i = 0; i < WaveSize; ++i)
{
    SpawnedEnemies.Add(SpawnEnemy());
}
```

### MoveTemp Usage

File: `DataLoader.cpp`, Line 92
```cpp
// BEFORE (copies entire array)
TArray<FLevelData> LoadedLevels = ParseLevelFile(FilePath);

// AFTER (moves — avoids deep copy of array contents)
TArray<FLevelData> LoadedLevels = MoveTemp(ParseLevelFile(FilePath));
// Note: only beneficial when ParseLevelFile returns by value
// and the compiler cannot apply NRVO
```

---

## 6. Verification Checklist Results

- [ ] **No raw UObject* without UPROPERTY** — **FAIL**: 3 instances found
      (WeaponComponent.h:47, WeaponComponent.h:48, InventoryManager.h:34)
- [ ] **No replication without authority checks** — **FAIL**: TakeDamage_Custom
      modifies CurrentHealth without HasAuthority() guard
- [x] **No CDO mutations at runtime** — PASS: no GetDefaultObject() calls
      found outside constructors
- [ ] **No GetWorld() in constructors** — **FAIL**: WeaponComponent constructor
      calls GetWorld() (Line 15)
- [ ] **No missing DOREPLIFETIME** — **FAIL**: WeaponState property missing
      from GetLifetimeReplicatedProps
- [ ] **No Reliable NetMulticast for cosmetics** — **FAIL**: 2 cosmetic
      multicasts marked Reliable (fire VFX, hit reaction)
- [ ] **No FString where FName suffices** — **FAIL**: InventoryManager uses
      FString as TMap key for slot lookups

---

## Summary

| Category | Critical | High | Moderate |
|----------|----------|------|----------|
| GC Safety | 2 | 2 | 1 |
| UPROPERTY Specifiers | 1 | 1 | 4 |
| Replication | 1 | 2 | 2 |
| Constructor Patterns | 1 | 1 | 0 |
| Memory Management | 0 | 1 | 2 |
| **Total** | **5** | **7** | **9** |

**Top 3 Actions:**
1. Add UPROPERTY to all raw UObject* member pointers — prevents GC crashes
2. Add HasAuthority() guards to all replicated state modifications
3. Switch cosmetic NetMulticast RPCs from Reliable to Unreliable
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — opens with precise scope covering UPROPERTY, GC, replication, and memory patterns
- ST-02 (Structured Sequential Instructions) — six numbered steps from specifier audit through verification
- RT-02 (Systematic Classification) — classifies findings by severity (Critical/High/Moderate) and category
- RT-05 (Evidence-Based Reasoning) — every finding includes specific file, line number, and before/after code
- DS-03 (Domain-Specific Conventions) — applies Unreal Engine-specific conventions (CDO, DOREPLIFETIME, MoveTemp)

**Related Prompts:**
- `domain-game-development/engines/engines_unreal_blueprint_review.md` — Blueprint architecture review for the visual scripting side
- `domain-game-development/multiplayer/multiplayer_netcode_review.md` — Network code patterns beyond Unreal-specific replication
- `domain-software-engineering/analysis/quality/quality_code_complexity_analysis.md` — General C++ complexity analysis
- `domain-software-engineering/analysis/performance/performance_code_optimization_suggestions.md` — General performance optimization patterns
