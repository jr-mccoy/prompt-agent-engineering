# Game Development & Game Design Prompts

Comprehensive prompts for game development covering design, architecture, engine-specific patterns, testing, multiplayer networking, performance optimization, graphics programming, audio systems, level design, and game economy balancing.

**Total Prompts:** 24 (Phase 1) | **Planned:** 47 total

---

## Directory Structure

| Subdirectory | Count | Focus Area |
|---|---|---|
| [`design/`](design/) | 4 | Game design documents, core loops, mechanics, progression systems |
| [`architecture/`](architecture/) | 3 | State machines, scene management, save systems |
| [`engines/`](engines/) | 4 | Unreal Engine (Blueprint, C++), Unity, Godot architecture review |
| [`testing/`](testing/) | 3 | Gameplay test plans, automated testing, platform certification |
| [`multiplayer/`](multiplayer/) | 3 | Netcode architecture, state sync, matchmaking |
| [`performance/`](performance/) | 2 | Frame budget analysis, rendering optimization |
| [`graphics/`](graphics/) | 2 | Shader review, lighting strategy |
| [`audio/`](audio/) | 1 | Audio system architecture |
| [`level-design/`](level-design/) | 1 | Procedural content generation |
| [`economy/`](economy/) | 1 | Game economy system design |

---

## Prompt Index

### Design

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Game Design Document Generator](design/design_game_design_document.md) | intermediate | Generate structured GDDs from game concepts |
| [Core Game Loop Analysis](design/design_core_loop_analysis.md) | intermediate | Analyze core loops for engagement and retention |
| [Game Mechanics Design](design/design_mechanics_design.md) | advanced | Design mechanics with interaction rules and feedback systems |
| [Player Progression System Design](design/design_player_progression.md) | advanced | Design XP curves, skill trees, and unlock schedules |

### Architecture

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Game State Machine Design](architecture/architecture_state_machine_design.md) | intermediate | Design FSM/HFSM for game states and AI behavior |
| [Scene & Level Management](architecture/architecture_scene_management.md) | intermediate | Design scene loading, transitions, and streaming |
| [Game Save & Serialization](architecture/architecture_save_system.md) | intermediate | Design save/load with versioning and cloud sync |

### Engines

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Unreal Blueprint Review](engines/engines_unreal_blueprint_review.md) | intermediate | Review Blueprint graphs for complexity and performance |
| [Unreal C++ Best Practices](engines/engines_unreal_cpp_patterns.md) | advanced | Analyze Unreal C++ for proper macro usage and GC safety |
| [Unity Architecture Review](engines/engines_unity_architecture_review.md) | intermediate | Review Unity project architecture and lifecycle patterns |
| [Godot Architecture Review](engines/engines_godot_architecture_review.md) | intermediate | Review Godot 4 scene tree design and signal patterns |

### Testing

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Gameplay Test Plan](testing/testing_gameplay_test_plan.md) | intermediate | Generate comprehensive game feature test plans |
| [Automated Game Testing](testing/testing_automated_game_testing.md) | advanced | Design automated testing strategies for games |
| [Platform Certification](testing/testing_platform_certification.md) | intermediate | Platform-specific certification checklists |

### Multiplayer

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Netcode Architecture](multiplayer/multiplayer_netcode_architecture.md) | advanced | Design multiplayer networking architecture |
| [State Synchronization](multiplayer/multiplayer_state_sync.md) | advanced | Design network state sync with prediction and reconciliation |
| [Matchmaking & Lobby](multiplayer/multiplayer_matchmaking_lobby.md) | intermediate | Design matchmaking and session management systems |

### Performance

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Frame Budget Analysis](performance/performance_frame_budget_analysis.md) | advanced | Analyze CPU/GPU frame budgets and profiler data |
| [Rendering Optimization](performance/performance_rendering_optimization.md) | advanced | Optimize draw calls, LOD, culling, and texture streaming |

### Graphics

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Shader Review](graphics/graphics_shader_review.md) | advanced | Review shader code for correctness and performance |
| [Lighting Strategy](graphics/graphics_lighting_strategy.md) | intermediate | Design baked vs real-time lighting strategies |

### Audio

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Audio System Architecture](audio/audio_system_architecture.md) | intermediate | Design audio bus hierarchies and middleware integration |

### Level Design

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Procedural Generation](level-design/level_procedural_generation.md) | advanced | Design procedural content generation systems |

### Economy

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Economy System Design](economy/economy_system_design.md) | advanced | Design game economies with currency flows and balancing |

---

## Related Resources

- **Unity ECS Patterns:** `domain-agentic-resources/skills/other/unity-ecs-patterns/`
- **Godot GDScript Patterns:** `domain-agentic-resources/skills/other/godot-gdscript-patterns/`
- **Unity Developer Agent:** `domain-agentic-resources/agents/languages/unity_developer.md`
- **Minecraft Bukkit Agent:** `domain-agentic-resources/agents/languages/minecraft_bukkit_pro.md`

---

**Phase 2 prompts** (23 additional) are tracked in `MISSING_TOPICS_ANALYSIS.md` under the Game Development Phase 2 section.
