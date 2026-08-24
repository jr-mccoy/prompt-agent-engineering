---
title: "Scene & Level Management Architecture"
category: game-development/architecture
description: "Design scene loading, transition, and management systems with additive loading, streaming, and memory lifecycle patterns"
techniques:
  - ST-01
  - ST-02
  - RT-05
  - DS-03
  - QA-02
difficulty: intermediate
tags:
  - architecture
  - scene-management
  - loading
  - streaming
  - memory
  - transitions
updated: "2026-03-19"
related_prompts:
  - domain-game-development/architecture/architecture_state_machine_design.md
  - domain-game-development/architecture/architecture_save_system.md
---

# Scene & Level Management Architecture

**Objective:** Design scene loading, transition, and management architectures covering additive scene loading, level streaming, scene composition, dependency management, and memory lifecycle for smooth gameplay transitions.

**When to Use:**
- Designing the scene/level structure for a new game project
- Migrating from single-scene to multi-scene architecture
- Solving long load times, memory spikes, or hitches during scene transitions
- Building open-world or seamless-transition level streaming
- Planning how persistent systems (audio, UI, player) survive scene changes
- Don't use when: your game is a single-scene prototype or jam game with no transitions needed

**Instructions:**

1. **Map the Scene Graph (Scenes, Dependencies, Shared Assets)**
   - Inventory every distinct scene or level in the game (menus, gameplay levels, loading screens, cutscenes, boss arenas)
   - Identify **persistent scenes** that must survive across transitions (e.g., AudioManager, GameManager, UI overlay, player entity)
   - Map **asset dependencies** between scenes:
     - Which scenes share assets (player model, common UI, shared materials)?
     - Which assets are unique to one scene (boss-specific VFX, level-specific music)?
   - Identify **scene composition** patterns: are gameplay levels a single monolithic scene, or composed from base + overlays (e.g., base terrain + lighting + enemy spawns)?
   - Create a dependency graph showing which scenes reference which shared asset bundles.

2. **Choose a Loading Strategy**
   - **Single Scene Swap** — Unload current scene entirely, load next scene. Simplest approach. Works for: linear games, menu-to-gameplay transitions, games with loading screens.
   - **Additive Loading** — Load new scene on top of current scene(s). Multiple scenes coexist. Works for: UI overlays, persistent managers, dungeon rooms connected to a hub.
   - **Level Streaming** — Load/unload scene chunks based on player proximity or triggers. Works for: open worlds, seamless area transitions, large continuous levels.
   - **Hybrid** — Combine strategies per transition type (e.g., additive for UI + streaming for world + swap for major area changes).
   - Document the chosen strategy for each transition in the game.

3. **Design the Transition Flow**
   - Define the transition sequence for each type of scene change:
     - **Standard transition:** Trigger → Fade out → Show loading screen → Async load target → Wait for ready → Hide loading screen → Fade in
     - **Seamless transition:** Player approaches boundary → Begin async preload of adjacent chunk → Load completes in background → Activate chunk → Deactivate distant chunk
     - **Instant transition:** Load target scene additively (pre-warmed) → Swap active camera → Unload previous
   - Design the **loading screen** system:
     - Minimum display time (avoid flicker for fast loads)
     - Progress reporting (asset count, percentage, or indeterminate spinner)
     - Interactive loading screens (tips, mini-games, animation)
   - Handle **transition cancellation**: what happens if the player backs out during a load?

4. **Plan Memory Lifecycle (Load Order, Unload Order, Reference Counting)**
   - Define **load order**: persistent scenes first (boot → managers → UI), then gameplay scenes
   - Define **unload order**: gameplay scenes first, persistent scenes never (or only on quit)
   - Implement **asset reference counting** for shared assets:
     - Shared texture used by Scene A and Scene B: only unload when both scenes are unloaded
     - Use addressable assets or asset bundle reference tracking
   - Plan **memory budgets** per platform:
     - Mobile: strict per-scene budgets, aggressive unloading
     - Console: larger budgets, but fixed RAM ceiling
     - PC: flexible, but still need upper bounds
   - Schedule **garbage collection** during loading screens or safe pauses (avoid GC during gameplay)
   - Pre-warm critical assets during loading (shader compilation, texture streaming, audio decompression)

5. **Handle Edge Cases (Interrupted Loads, Low-Memory Recovery, Hot Reload)**
   - **Interrupted loads**: player triggers a new transition before current load finishes — cancel current async operation, clean up partial loads, start new load
   - **Low-memory recovery**: detect memory pressure → force-unload non-essential scenes (distant chunks) → show quality reduction warning → worst case: force return to menu
   - **Scene reload / restart**: unload current gameplay scene, reload same scene — must reset all state, not carry over stale data
   - **Development hot reload**: support reloading a scene without restarting the game during development (editor workflow)
   - **Failed loads**: missing scene file, corrupted bundle — fallback to error scene with recovery options
   - **Async timing**: ensure no frame-rate spikes from loading — spread instantiation across multiple frames

6. **CRITICAL: Verification Checklist**
   - [ ] **No circular dependencies** — scene A does not require scene B which requires scene A
   - [ ] **No memory leaks on scene unload** — every instantiated object is destroyed, every event handler is unsubscribed, every coroutine is stopped
   - [ ] **Persistent objects survive transitions** — managers, audio, player data persist correctly through every transition path
   - [ ] **All transition paths tested** — every valid scene-to-scene path has been traversed (including back-tracking)
   - [ ] **Memory stays within budget** — peak memory after worst-case scene combination fits target platform
   - [ ] **No stale references** — nothing references destroyed objects from a previous scene (null reference errors)
   - [ ] **Loading never blocks main thread** — all file I/O and heavy instantiation is async or spread across frames
   - [ ] **Scene can be reloaded cleanly** — restart level produces identical initial state

**False-Positive Prevention:**

| Mistake | Correction |
|---------|------------|
| ❌ Over-engineering streaming for a game with fewer than 10 small scenes | ✅ Use simple scene swap with loading screens — streaming adds complexity only justified by large or seamless worlds |
| ❌ Assuming all scenes need level streaming | ✅ Only stream scenes that are spatially adjacent and traversed without loading screens; menus and UI should use additive loading |
| ❌ Ignoring target platform memory constraints | ✅ Set per-platform memory budgets before designing scene composition — mobile may need 3 chunks max, console can handle 8+ |
| ❌ Using DontDestroyOnLoad for everything that persists | ✅ Use a dedicated persistent scene loaded additively — DontDestroyOnLoad is harder to manage, debug, and cannot be unloaded |
| ❌ Testing only the "happy path" transition | ✅ Test interrupted loads, rapid scene switching, reload-same-scene, and backwards transitions through every flow |
| ❌ Loading all assets synchronously to "keep it simple" | ✅ Even small games benefit from async loading — synchronous loading causes visible freezes and fails platform certification on consoles |

**Expected Output:** A structured scene management design document that includes:

1. Scene inventory and dependency graph
2. Loading strategy selection per transition type
3. Transition flow sequences with timing
4. Memory lifecycle plan with budgets
5. Edge case handling matrix
6. Verification checklist results

**Example Output:**

```markdown
# Scene Management System — Open-World Action RPG

## 1. Scene Inventory & Dependency Graph

### Scene Catalog

| Scene ID             | Type        | Size (MB) | Persistent | Depends On           |
|----------------------|-------------|-----------|------------|----------------------|
| Boot                 | System      | 2         | No         | —                    |
| PersistentManagers   | System      | 8         | Yes        | —                    |
| UIOverlay            | UI          | 15        | Yes        | PersistentManagers   |
| MainMenu             | Menu        | 25        | No         | UIOverlay            |
| Overworld_Chunk_0_0  | World       | 45        | No         | SharedWorldAssets     |
| Overworld_Chunk_1_0  | World       | 52        | No         | SharedWorldAssets     |
| Overworld_Chunk_0_1  | World       | 48        | No         | SharedWorldAssets     |
| Overworld_Chunk_1_1  | World       | 50        | No         | SharedWorldAssets     |
| Dungeon_CrystalCave  | Interior   | 60        | No         | SharedDungeonAssets   |
| Dungeon_AncientRuins | Interior   | 72        | No         | SharedDungeonAssets   |
| BossArena_Dragon     | Boss        | 35        | No         | SharedWorldAssets     |
| Cutscene_Intro       | Cinematic  | 20        | No         | —                    |
| LoadingScreen        | UI          | 3         | Yes        | —                    |
| SharedWorldAssets    | AssetBundle | 80        | Ref-count  | —                    |
| SharedDungeonAssets  | AssetBundle | 40        | Ref-count  | —                    |

### Dependency Graph

```
Boot
 └──▶ PersistentManagers (additive, never unloaded)
       ├──▶ UIOverlay (additive, never unloaded)
       ├──▶ LoadingScreen (additive, never unloaded)
       └──▶ MainMenu ──▶ Overworld_Chunk_0_0
                              ├──▶ Overworld_Chunk_1_0 (streamed)
                              ├──▶ Overworld_Chunk_0_1 (streamed)
                              ├──▶ Dungeon_CrystalCave (swap via portal)
                              └──▶ BossArena_Dragon (swap via trigger)
```

**Circular dependency check:** PASSED — no scene requires another scene
that transitively requires it back.

## 2. Loading Strategy by Transition Type

| Transition                       | Strategy          | Rationale                            |
|----------------------------------|-------------------|--------------------------------------|
| Boot → PersistentManagers + UI   | Additive          | Must persist forever                 |
| MainMenu → Overworld             | Swap + Loading    | Full context change, large assets    |
| Overworld chunk ↔ chunk          | Streaming          | Seamless open world traversal        |
| Overworld → Dungeon              | Swap + Loading    | Different asset set, interior env    |
| Dungeon → Overworld              | Swap + Loading    | Reverse of above                     |
| Overworld → BossArena            | Swap + Loading    | Isolated arena, custom skybox        |
| Any → MainMenu                   | Swap + Loading    | Full cleanup of gameplay state       |
| Gameplay → Pause Menu            | Additive overlay  | Gameplay scene stays loaded          |

## 3. Transition Flow — Overworld to Dungeon

```
Frame 0:    Player enters dungeon portal trigger
Frame 1:    SceneManager.BeginTransition("Dungeon_CrystalCave")
            → Set player input locked = true
            → Start fade-to-black coroutine (0.5s)
Frame 30:   Fade complete
            → Activate LoadingScreen scene (already loaded)
            → Begin async load: Dungeon_CrystalCave
            → Begin async load: SharedDungeonAssets (if not loaded)
Frame 31+:  Loading screen displays progress
            → Report: "Loading Crystal Cave... 45%"
            → Minimum display time: 1.0 second
Frame ~120: Async load complete
            → Instantiate spawn point, pre-warm shaders
            → Unload Overworld chunks (release references)
            → If SharedWorldAssets ref count == 0, unload it
            → Teleport player to dungeon spawn point
            → Deactivate LoadingScreen
            → Start fade-from-black coroutine (0.5s)
Frame ~150: Fade complete
            → Unlock player input
            → SceneManager.TransitionComplete()
```

## 4. Streaming System — Overworld Chunks

```csharp
public class WorldStreamer : MonoBehaviour
{
    [SerializeField] private int loadRadius = 1;    // chunks
    [SerializeField] private int unloadRadius = 2;  // chunks
    [SerializeField] private float checkInterval = 0.5f;

    private Vector2Int _currentChunk;
    private Dictionary<Vector2Int, AsyncOperation> _loadedChunks = new();
    private HashSet<Vector2Int> _loadingChunks = new();

    private void Start()
    {
        InvokeRepeating(nameof(UpdateStreaming), 0f, checkInterval);
    }

    private void UpdateStreaming()
    {
        Vector2Int playerChunk = WorldToChunk(Player.Position);

        if (playerChunk == _currentChunk) return;
        _currentChunk = playerChunk;

        // Load chunks within radius
        for (int x = -loadRadius; x <= loadRadius; x++)
        {
            for (int y = -loadRadius; y <= loadRadius; y++)
            {
                Vector2Int coord = _currentChunk + new Vector2Int(x, y);
                if (!_loadedChunks.ContainsKey(coord) &&
                    !_loadingChunks.Contains(coord))
                {
                    StartCoroutine(LoadChunkAsync(coord));
                }
            }
        }

        // Unload chunks outside unload radius
        var toUnload = _loadedChunks.Keys
            .Where(c => ChunkDistance(c, _currentChunk) > unloadRadius)
            .ToList();

        foreach (var coord in toUnload)
        {
            UnloadChunk(coord);
        }
    }

    private IEnumerator LoadChunkAsync(Vector2Int coord)
    {
        _loadingChunks.Add(coord);
        string sceneName = $"Overworld_Chunk_{coord.x}_{coord.y}";

        var op = SceneManager.LoadSceneAsync(
            sceneName, LoadSceneMode.Additive);
        op.allowSceneActivation = false;

        // Wait until 90% loaded (Unity holds at 0.9 until activation)
        while (op.progress < 0.9f)
            yield return null;

        // Activate when ready
        op.allowSceneActivation = true;
        yield return op;

        _loadingChunks.Remove(coord);
        _loadedChunks[coord] = op;
    }

    private void UnloadChunk(Vector2Int coord)
    {
        string sceneName = $"Overworld_Chunk_{coord.x}_{coord.y}";
        SceneManager.UnloadSceneAsync(sceneName);
        _loadedChunks.Remove(coord);
    }
}
```

## 5. Memory Budget per Platform

| Platform       | Total RAM | Scene Budget | Max Concurrent Chunks | Asset Cache |
|----------------|-----------|--------------|----------------------|-------------|
| PC (min spec)  | 8 GB      | 1.5 GB       | 9 (3×3)              | 512 MB      |
| PS5 / Xbox X   | 16 GB     | 3.0 GB       | 9 (3×3)              | 1 GB        |
| Nintendo Switch | 4 GB      | 800 MB       | 5 (cross shape)      | 256 MB      |
| Mobile (high)  | 6 GB      | 600 MB       | 5 (cross shape)      | 128 MB      |

### Memory Lifecycle Rules

1. **Persistent scenes** (~26 MB) — loaded at boot, never unloaded
2. **Shared asset bundles** — reference counted, unloaded when
   no loaded scene references them
3. **GC scheduling** — force `System.GC.Collect()` during loading
   screens only, never during gameplay
4. **Texture streaming** — enabled on all platforms; max resident
   mip budgets match platform table above
5. **Audio** — stream music from disk; decompress SFX on load

## 6. Edge Case Matrix

| Scenario                          | Handling                                      |
|-----------------------------------|-----------------------------------------------|
| Player crosses chunk boundary     | Load new ring async, unload distant ring       |
|   during combat                   | Combat state preserved in persistent scene     |
| Rapid back-and-forth at boundary  | Debounce: keep chunks for 5s after leaving     |
|                                   | unload radius before actually unloading        |
| Low memory warning (mobile)       | Shrink load radius to 0 (player chunk only),   |
|                                   | force unload all distant chunks, log warning   |
| Scene file missing / corrupt      | Log error, load fallback empty scene, show     |
|                                   | "Area unavailable" message, teleport to hub    |
| Player quits during loading       | Cancel async operations, save current state    |
|                                   | (pre-transition), clean exit                   |
| Reload / restart current scene    | Unload all gameplay scenes, reload fresh,      |
|                                   | re-initialize from checkpoint save data        |

## 7. Verification Results

- [x] **No circular dependencies** — verified via dependency graph traversal
- [x] **No memory leaks** — tested 50 transition cycles; heap stable
      within 5 MB variance
- [x] **Persistent objects survive** — AudioManager, GameManager, UI
      verified across all transition types
- [x] **All paths tested** — 14 transition paths verified including
      backwards traversal and menu returns
- [x] **Memory within budget** — peak 1.2 GB on PC (budget 1.5 GB),
      peak 580 MB on Switch (budget 800 MB)
- [x] **No stale references** — WeakReference audit passed; null-check
      guard on all cross-scene references
- [x] **No main thread blocking** — profiler confirms zero frames
      above 20ms during streaming transitions
- [x] **Clean reload** — restart level 100 times: deterministic
      initial state confirmed via state hash comparison
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — precise scope covering additive loading, streaming, memory lifecycle, and transitions
- ST-02 (Structured Sequential Instructions) — six steps from scene inventory through verification
- RT-05 (Evidence-Based Reasoning) — requires concrete memory budgets, frame timing, and platform-specific constraints
- DS-03 (Comparative Analysis) — compares loading strategies (swap vs. additive vs. streaming) with selection criteria
- QA-02 (Verification Checklist) — critical checklist for circular dependencies, memory leaks, and stale references

**Related Prompts:**
- `domain-game-development/architecture/architecture_state_machine_design.md` — State machines for managing transition flow states
- `domain-game-development/architecture/architecture_save_system.md` — Saving/restoring state across scene transitions
- `domain-software-engineering/analysis/performance/performance_bottleneck_identification.md` — Profiling scene load performance
