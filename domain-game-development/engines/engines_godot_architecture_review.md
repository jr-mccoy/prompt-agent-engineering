---
title: "Godot Project Architecture Review"
category: game-development/engines
description: "Review Godot 4 project architecture including scene tree design, signal coupling, autoload usage, resource management, and GDScript/C# interop"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-02
difficulty: intermediate
tags:
  - godot
  - architecture
  - scene-tree
  - signals
  - gdscript
  - code-review
updated: "2026-03-19"
related_prompts:
  - domain-game-development/engines/engines_unity_architecture_review.md
  - domain-game-development/architecture/architecture_state_machine_design.md
  - domain-game-development/architecture/architecture_scene_management.md
---

# Godot Project Architecture Review

**Objective:** Review a Godot 4 project's architecture for proper scene tree design, signal coupling discipline, autoload usage, resource management, and GDScript/C# interop decisions, identifying structural issues before they become costly to fix.

## When to Use

- Use when reviewing a Godot 4 project's overall architecture
- Use when a project is growing unwieldy and needs structural assessment
- Use when migrating from Godot 3 to Godot 4 and need to validate new patterns
- Don't use for GDScript syntax-level code review — use standard code quality tools instead

## Instructions

1. **Analyze Scene Tree Architecture**
   - Map the scene hierarchy depth — flag trees deeper than 5-6 levels (hard to navigate, fragile paths)
   - Check scene composition: are scenes self-contained and reusable, or tightly coupled to parent assumptions?
   - Verify inherited scenes (`.tscn`) are used for variants, not copy-paste duplication
   - Look for "god scenes" — single scenes with 20+ child nodes that should be broken into sub-scenes
   - Check that UI scenes are separate from gameplay scenes (clean separation)

2. **Evaluate Signal Architecture**
   - Check signal direction: signals should flow UP the tree (child → parent), calls flow DOWN (parent → child)
   - Flag cross-tree signal connections that bypass the hierarchy (creates invisible coupling)
   - Look for signal chains (A signals B, B signals C, C signals D) — often indicates missing event bus
   - Verify signals are disconnected when nodes are freed (memory leak risk)
   - Check for overuse of `call_group()` when signals or direct calls would be clearer

3. **Review Autoload Usage**
   - Audit each autoload for necessity — autoloads are global singletons, use sparingly
   - Appropriate autoloads: GameManager, AudioManager, SaveManager, SceneTransition, EventBus
   - Flag inappropriate autoloads: player reference (should use groups), level-specific logic, temporary state
   - Check autoload dependencies — autoloads should not depend on scene tree structure
   - Verify autoload initialization order if they reference each other

4. **Assess Resource Management**
   - Check for `preload()` vs `load()` usage — preload for small/always-needed, load for large/conditional
   - Look for resource leaks: loaded resources never freed, packed scenes held indefinitely
   - Verify `.tres` (text resources) vs `.res` (binary resources) usage — binary for production, text for version control
   - Check custom Resource classes for proper `_init()` defaults
   - Flag any `ResourceLoader.load_threaded_*` patterns for correctness (callback handling)

5. **Review GDScript Patterns**
   - Check for proper use of `@export` annotations (replaces old `export` keyword)
   - Verify `@onready` usage for node references (not fetching in `_ready()` manually)
   - Look for type hints on function signatures and variables (GDScript 4 best practice)
   - Check `_process()` vs `_physics_process()` usage — game logic in physics, visual in process
   - Flag scripts with 300+ lines — likely need decomposition
   - Verify proper `await` usage (replaces yield in Godot 4)

6. **Check GDScript/C# Interop** (if applicable)
   - Verify clear boundaries: which layer uses GDScript, which uses C#
   - Check signal connections between GDScript and C# nodes (requires specific patterns)
   - Verify C# nodes export properties correctly for editor visibility
   - Flag unnecessary language mixing — pick one unless performance demands C#

7. **CRITICAL: Verify Architectural Findings**
   - For each issue found, verify it causes real problems (not just style preference)
   - Check if patterns are Godot-idiomatic before flagging as anti-patterns
   - Verify scene coupling by testing: can a scene be instanced in a test scene independently?
   - Confirm autoload issues by tracing actual dependency graphs
   - Test that suggested refactors don't break signal connections or node paths

**False-Positive Prevention (MUST follow):**

❌ **DON'T:**
- Don't flag `$NodePath` access as bad — it's Godot-idiomatic (but flag hardcoded deep paths)
- Don't insist on dependency injection patterns from enterprise software — Godot uses scene composition
- Don't flag `_process()` usage as wasteful without checking if `set_process(false)` is used when idle
- Don't flag autoloads as anti-patterns universally — 3-5 autoloads is normal for a Godot project
- Don't assume GDScript is "worse" than C# — recommend C# only for CPU-intensive inner loops

✅ **DO:**
- Consider project scope — a game jam project doesn't need the same rigor as a commercial release
- Check Godot 4 migration: are old Godot 3 patterns lingering (yield, export without @, old signal syntax)?
- Verify node references use `@onready` and not `get_node()` in `_ready()` (the latter fails on re-parenting)
- Check that exported variables have proper type annotations for editor UX
- Validate that custom resources have documentation for designer-facing properties

## Expected Output

An architecture review report including:

- Scene tree structure assessment with coupling analysis
- Signal architecture diagram with problematic connections highlighted
- Autoload audit with recommendations
- Resource management findings
- Code pattern issues with specific file/line references
- Prioritized recommendations (P0-P2)

## Example Output

```markdown
## Godot 4 Architecture Review — "Pixel Realms" (2D Action RPG)

### Executive Summary

Reviewed 47 scenes, 82 GDScript files, 3 autoloads. Found **4 critical issues** (P0), **7 moderate issues** (P1), and **5 minor improvements** (P2). Primary concerns: god scene in main level, signal spaghetti in combat system, and missing resource management for loaded levels.

### Scene Tree Assessment

**Project structure:**
```
res://
├── scenes/
│   ├── main_menu.tscn          ✅ Self-contained
│   ├── game_world.tscn         ⚠️ God scene (34 children)
│   ├── player/
│   │   ├── player.tscn         ✅ Well-composed
│   │   └── player_hud.tscn     ✅ Separate from player logic
│   ├── enemies/
│   │   ├── base_enemy.tscn     ✅ Inherited scene pattern
│   │   ├── goblin.tscn         ✅ Extends base_enemy
│   │   └── dragon.tscn         ✅ Extends base_enemy
│   ├── ui/
│   │   ├── inventory.tscn      ⚠️ References $"../../Player" (coupled)
│   │   └── dialogue.tscn       ✅ Signal-driven, decoupled
│   └── levels/
│       ├── forest.tscn         ⚠️ Never freed after transition
│       └── dungeon.tscn        ⚠️ Never freed after transition
├── scripts/
│   ├── autoloads/
│   │   ├── game_manager.gd     ✅ Appropriate autoload
│   │   ├── audio_manager.gd    ✅ Appropriate autoload
│   │   └── player_data.gd      ⚠️ Should be part of save system, not autoload
│   └── components/
│       ├── health_component.gd  ✅ Reusable component
│       └── hitbox_component.gd  ✅ Reusable component
└── resources/
    ├── items/                   ✅ Custom Resource per item
    └── enemies/                 ✅ Enemy stat resources
```

### P0 — Critical Issues

#### 1. God Scene: `game_world.tscn`

**Problem:** `game_world.tscn` has 34 direct children including player, all enemies, UI, environment, camera, and game logic nodes.

**Impact:** Impossible to test subsystems independently. Merge conflicts in team development. Loading the scene loads everything.

**Fix:**
```
game_world.tscn (AFTER)
├── Environment (sub-scene: handles tilemap, parallax)
├── EntityContainer (Node2D, spawns entities dynamically)
├── Player (instanced sub-scene)
├── Camera (follows player via RemoteTransform2D)
├── UILayer (CanvasLayer, loads UI sub-scenes)
└── LevelManager (script: handles level loading/unloading)
```

**Confidence:** High — this is a textbook god-scene anti-pattern.

#### 2. Signal Spaghetti in Combat

**Problem:** Combat system uses 12 cross-tree signal connections:
```
Hitbox → connects to → Enemy.health_component (cross-branch)
Enemy → connects to → Player._on_enemy_died (cross-branch)
Player → connects to → HUD.update_xp (3 levels up, then down)
```

**Impact:** Invisible coupling. Removing or moving any node breaks signals silently.

**Fix:** Introduce a `CombatEventBus` autoload or use signal relay through common parent:
```gdscript
# combat_events.gd (new autoload)
signal damage_dealt(source: Node2D, target: Node2D, amount: float)
signal entity_died(entity: Node2D, killer: Node2D)
signal xp_gained(amount: int)
```

**Confidence:** High — traced 12 connections manually, 8 are cross-branch.

#### 3. Level Resource Leak

**Problem:** `scenes/levels/` scenes are loaded with `load()` but never freed:
```gdscript
# level_transition.gd
func change_level(path: String):
    var new_level = load(path).instantiate()
    get_tree().root.add_child(new_level)
    # OLD LEVEL IS NEVER queue_free()'d
```

**Impact:** Memory grows with each level transition. After 10 transitions, ~200MB leaked.

**Fix:**
```gdscript
func change_level(path: String):
    var old_level = get_tree().get_first_node_in_group("active_level")
    if old_level:
        old_level.queue_free()
    var new_level = load(path).instantiate()
    new_level.add_to_group("active_level")
    get_tree().root.add_child(new_level)
```

**Confidence:** High — confirmed via Godot Debugger Monitors (Objects count rises per transition).

#### 4. Inventory Scene Coupling

**Problem:** `inventory.tscn` script uses hardcoded path:
```gdscript
@onready var player = $"../../Player"
```

**Impact:** Scene cannot be instanced anywhere else. Breaks if Player is renamed or moved.

**Fix:** Use group access or signal:
```gdscript
@onready var player = get_tree().get_first_node_in_group("player")
# Or better: listen for signals via autoload
```

**Confidence:** High — path dependency is explicit in code.

### P1 — Moderate Issues

| # | Issue | Location | Recommendation |
|---|-------|----------|----------------|
| 5 | `player_data.gd` autoload stores runtime state AND save data | `autoloads/` | Split into SaveManager (persistence) and PlayerState (runtime) |
| 6 | No type hints on 23 functions | Various | Add return types and parameter types for editor autocomplete |
| 7 | Godot 3 `yield()` still used in 4 files | combat/, dialogue/ | Replace with `await` (Godot 4 syntax) |
| 8 | `_process()` running on 15 nodes even when paused | enemies/ | Add `set_process(false)` in `_ready()`, enable only when active |
| 9 | Enemy AI in single 280-line script | `enemy_ai.gd` | Decompose into state machine components |
| 10 | Preloading all item icons at startup (200+ textures) | `item_database.gd` | Lazy-load icons when inventory UI opens |
| 11 | No `class_name` on reusable scripts | `components/` | Add `class_name` for editor node creation support |

### P2 — Minor Improvements

| # | Suggestion | Rationale |
|---|-----------|-----------|
| 12 | Use `.tres` for version-controlled resources, `.res` for built assets | Better git diffs |
| 13 | Add `@export_group` annotations to organize inspector properties | Designer UX |
| 14 | Create a `debug/` autoload for runtime debug overlays | Faster debugging |
| 15 | Use `ResourceLoader.load_threaded_request()` for level loading | Eliminate loading hitches |
| 16 | Add `@tool` annotation to frequently-edited scenes for preview | Faster iteration |

### Recommended Priority

1. **This week:** Fix level resource leak (P0 #3) — memory issue affects all players
2. **This sprint:** Break up god scene (P0 #1) and combat signals (P0 #2) — blocks team scaling
3. **Next sprint:** Fix coupling (P0 #4), Godot 3 syntax cleanup (P1 #7), type hints (P1 #6)
4. **Ongoing:** Performance tuning (P1 #8, #10), code decomposition (P1 #9)
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focuses review on Godot 4-specific architectural concerns
- **ST-02 (Structured Sequential Instructions):** Seven-step review process from scene tree through verification
- **RT-02 (Multi-Dimensional Analysis):** Examines scenes, signals, autoloads, resources, and code patterns separately
- **RT-05 (Evidence-Based Reasoning):** Requires tracing actual signal connections and measuring resource leaks
- **QA-02 (Validation and Verification):** CRITICAL step verifies findings against Godot idioms and real impact

## Related Prompts

- [Unity Architecture Review](engines_unity_architecture_review.md) — Equivalent review for Unity projects
- [Game State Machine Design](../architecture/architecture_state_machine_design.md) — For redesigning AI and game state management
- [Scene & Level Management](../architecture/architecture_scene_management.md) — For fixing scene loading issues
