# Game Development & Game Design Prompts

Comprehensive prompts for game development covering design, architecture, engine-specific patterns, testing, multiplayer networking, performance optimization, graphics programming, audio systems, level design, narrative, NPC AI, game economy and live-ops, and production (pitching and postmortems).

**Total Prompts:** 33 (Phase 1: 24; Phase 2, coverage Wave 4: 9)

---

## Directory Structure

| Subdirectory | Count | Focus Area |
|---|---|---|
| [`design/`](design/) | 6 | Game design documents, core loops, mechanics, progression, difficulty balancing, HUD and game feel |
| [`architecture/`](architecture/) | 3 | State machines, scene management, save systems |
| [`engines/`](engines/) | 4 | Unreal Engine (Blueprint, C++), Unity, Godot architecture review |
| [`testing/`](testing/) | 4 | Gameplay test plans, automated testing, platform certification, playtest protocol |
| [`multiplayer/`](multiplayer/) | 3 | Netcode architecture, state sync, matchmaking |
| [`performance/`](performance/) | 2 | Frame budget analysis, rendering optimization |
| [`graphics/`](graphics/) | 2 | Shader review, lighting strategy |
| [`audio/`](audio/) | 1 | Audio system architecture |
| [`level-design/`](level-design/) | 2 | Procedural content generation, handcrafted blockout and pacing |
| [`economy/`](economy/) | 2 | Game economy system design, live-ops calendar and monetization ethics |
| [`narrative/`](narrative/) | 1 | Quest structure and branching dialogue |
| [`ai/`](ai/) | 1 | NPC and enemy decision architecture (FSM, BT, utility, GOAP) |
| [`production/`](production/) | 2 | Publisher/investor pitch, project postmortem |

---

## Prompt Index

### Design

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Game Design Document Generator](design/design_game_design_document.md) | intermediate | Generate structured GDDs from game concepts |
| [Core Game Loop Analysis](design/design_core_loop_analysis.md) | intermediate | Analyze core loops for engagement and retention |
| [Game Mechanics Design](design/design_mechanics_design.md) | advanced | Design mechanics with interaction rules and feedback systems |
| [Player Progression System Design](design/design_player_progression.md) | advanced | Design XP curves, skill trees, and unlock schedules |
| [Difficulty and Combat Balancing](design/design_difficulty_combat_balancing.md) | advanced | DPS/EHP/TTK tables, difficulty modes, and ethical dynamic difficulty |
| [HUD, UI and Game-Feel Review](design/design_hud_and_game_feel_review.md) | intermediate | HUD hierarchy, readability, accessibility, and frame-by-frame feel of core actions |

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
| [Playtest Protocol and Feedback Synthesis](testing/testing_playtest_protocol_synthesis.md) | intermediate | Decision-linked playtests; observed-vs-said synthesis with counts and confidence |

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
| [Blockout and Pacing Review](level-design/level_blockout_and_pacing.md) | intermediate | Metrics-driven greybox, beat chart, and pacing audit for handcrafted levels |

### Economy

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Economy System Design](economy/economy_system_design.md) | advanced | Design game economies with currency flows and balancing |
| [Live-Ops Calendar and Monetization Ethics](economy/economy_liveops_monetization_ethics.md) | advanced | Capacity-checked season calendar; offer audit for dark patterns, loot boxes and minors |

### Narrative

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Quest Structure and Branching Dialogue](narrative/narrative_quest_and_dialogue_design.md) | intermediate | Branching structure, state variables, dialogue map, line budget, soft-lock audit |

### AI

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [NPC and Enemy AI Decision Architecture](ai/ai_npc_decision_architecture.md) | advanced | Choose FSM/BT/utility/GOAP; behaviour spec, scoring curves, per-frame budget |

### Production

| Prompt | Difficulty | Description |
|--------|-----------|-------------|
| [Publisher and Investor Pitch](production/production_publisher_pitch.md) | advanced | Vertical slice proof, comps with method, budget, milestones, recoupment |
| [Project Postmortem](production/production_project_postmortem.md) | intermediate | Plan vs actual, slip account, root causes, owned actions |

---

## Related Resources

- **Unity ECS Patterns:** `domain-agentic-resources/skills/other/unity-ecs-patterns/`
- **Godot GDScript Patterns:** `domain-agentic-resources/skills/other/godot-gdscript-patterns/`
- **Unity Developer Agent:** `domain-agentic-resources/agents/languages/unity_developer.md`
- **Minecraft Bukkit Agent:** `domain-agentic-resources/agents/languages/minecraft_bukkit_pro.md`

---

**Phase 2** shipped in coverage Wave 4 of [`meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md): narrative and quest design, NPC and enemy AI, handcrafted level blockout and pacing, playtest protocol, difficulty balancing, HUD and game feel, live-ops and monetization ethics, publisher pitch, and project postmortem.
