---
name: godot-gdscript-patterns
description: Master Godot 4 GDScript patterns including signals, scenes, state machines, and optimization. Use when building Godot games, implementing game systems, or learning GDScript best practices.
metadata:
  tags:
    - game-dev
    - gdscript
    - godot
    - optimization
  updated: "2026-04-11"
---
# Godot GDScript Patterns

Production patterns for Godot 4.x game development with GDScript, covering architecture, signals, scenes, and optimization.

## When to Use This Skill

- Building games with Godot 4
- Implementing game systems in GDScript
- Designing scene architecture
- Managing game state
- Optimizing GDScript performance
- Learning Godot best practices

## Core Concepts

### 1. Godot Architecture

```
Node: Base building block
├── Scene: Reusable node tree (saved as .tscn)
├── Resource: Data container (saved as .tres)
├── Signal: Event communication
└── Group: Node categorization
```

### 2. GDScript Basics

```gdscript
class_name Player
extends CharacterBody2D

# Signals
signal health_changed(new_health: int)
signal died

# Exports (Inspector-editable)
@export var speed: float = 200.0
@export var max_health: int = 100
@export_range(0, 1) var damage_reduction: float = 0.0
@export_group("Combat")
@export var attack_damage: int = 10
@export var attack_cooldown: float = 0.5

# Onready (initialized when ready)
@onready var sprite: Sprite2D = $Sprite2D
@onready var animation: AnimationPlayer = $AnimationPlayer
@onready var hitbox: Area2D = $Hitbox

# Private variables (convention: underscore prefix)
var _health: int
var _can_attack: bool = true

func _ready() -> void:
    _health = max_health

func _physics_process(delta: float) -> void:
    var direction := Input.get_vector("left", "right", "up", "down")
    velocity = direction * speed
    move_and_slide()

func take_damage(amount: int) -> void:
    var actual_damage := int(amount * (1.0 - damage_reduction))
    _health = max(_health - actual_damage, 0)
    health_changed.emit(_health)

    if _health <= 0:
        died.emit()
```

## Patterns

### Pattern 1: State Machine

```gdscript
# state_machine.gd
class_name StateMachine
extends Node

signal state_changed(from_state: StringName, to_state: StringName)

@export var initial_state: State

var current_state: State
var states: Dictionary = {}

func _ready() -> void:
    # Register all State children
    for child in get_children():
        if child is State:
            states[child.name] = child
            child.state_machine = self
            child.process_mode = Node.PROCESS_MODE_DISABLED

    # Start initial state
    if initial_state:
        current_state = initial_state
        current_state.process_mode = Node.PROCESS_MODE_INHERIT
        current_state.enter()

func _process(delta: float) -> void:
    if current_state:
        current_state.update(delta)

func _physics_process(delta: float) -> void:
    if current_state:
        current_state.physics_update(delta)

func _unhandled_input(event: InputEvent) -> void:
    if current_state:
        current_state.handle_input(event)

func transition_to(state_name: StringName, msg: Dictionary = {}) -> void:
    if not states.has(state_name):
        push_error("State '%s' not found" % state_name)
        return

    var previous_state := current_state
    previous_state.exit()
    previous_state.process_mode = Node.PROCESS_MODE_DISABLED

    current_state = states[state_name]
    current_state.process_mode = Node.PROCESS_MODE_INHERIT
    current_state.enter(msg)

    state_changed.emit(previous_state.name, current_state.name)
```

```gdscript
# state.gd
class_name State
extends Node

var state_machine: StateMachine

func enter(_msg: Dictionary = {}) -> void:
    pass

func exit() -> void:
    pass

func update(_delta: float) -> void:
    pass

func physics_update(_delta: float) -> void:
    pass

func handle_input(_event: InputEvent) -> void:
    pass
```

```gdscript
# player_idle.gd
class_name PlayerIdle
extends State

@export var player: Player

func enter(_msg: Dictionary = {}) -> void:
    player.animation.play("idle")

func physics_update(_delta: float) -> void:
    var direction := Input.get_vector("left", "right", "up", "down")

    if direction != Vector2.ZERO:
        state_machine.transition_to("Move")

func handle_input(event: InputEvent) -> void:
    if event.is_action_pressed("attack"):
        state_machine.transition_to("Attack")
    elif event.is_action_pressed("jump"):
        state_machine.transition_to("Jump")
```

### Pattern 2: Autoload Singletons

```gdscript
# game_manager.gd (Add to Project Settings > Autoload)
extends Node

signal game_started
signal game_paused(is_paused: bool)
signal game_over(won: bool)
signal score_changed(new_score: int)

enum GameState { MENU, PLAYING, PAUSED, GAME_OVER }

var state: GameState = GameState.MENU
var score: int = 0:
    set(value):
        score = value
        score_changed.emit(score)

var high_score: int = 0

func _ready() -> void:
    process_mode = Node.PROCESS_MODE_ALWAYS
    _load_high_score()

func _input(event: InputEvent) -> void:
    if event.is_action_pressed("pause") and state == GameState.PLAYING:
        toggle_pause()

func start_game() -> void:
    score = 0
    state = GameState.PLAYING
    game_started.emit()

func toggle_pause() -> void:
    var is_paused := state != GameState.PAUSED

    if is_paused:
        state = GameState.PAUSED
        get_tree().paused = true
    else:
        state = GameState.PLAYING
        get_tree().paused = false

    game_paused.emit(is_paused)

func end_game(won: bool) -> void:
    state = GameState.GAME_OVER

    if score > high_score:
        high_score = score
        _save_high_score()

    game_over.emit(won)

func add_score(points: int) -> void:
    score += points

func _load_high_score() -> void:
    if FileAccess.file_exists("user://high_score.save"):
        var file := FileAccess.open("user://high_score.save", FileAccess.READ)
        high_score = file.get_32()

func _save_high_score() -> void:
    var file := FileAccess.open("user://high_score.save", FileAccess.WRITE)
    file.store_32(high_score)
```

```gdscript
# event_bus.gd (Global signal bus)
extends Node

# Player events
signal player_spawned(player: Node2D)
signal player_died(player: Node2D)
signal player_health_changed(health: int, max_health: int)

# Enemy events
signal enemy_spawned(enemy: Node2D)
signal enemy_died(enemy: Node2D, position: Vector2)

# Item events
signal item_collected(item_type: StringName, value: int)
signal powerup_activated(powerup_type: StringName)

# Level events
signal level_started(level_number: int)
signal level_completed(level_number: int, time: float)
signal checkpoint_reached(checkpoint_id: int)
```

### Pattern 3: Resource-based Data

```gdscript
# weapon_data.gd
class_name WeaponData
extends Resource

@export var name: StringName
@export var damage: int
@export var attack_speed: float
@export var range: float
@export_multiline var description: String
@export var icon: Texture2D
@export var projectile_scene: PackedScene
@export var sound_attack: AudioStream
```

```gdscript
# character_stats.gd
class_name CharacterStats
extends Resource

signal stat_changed(stat_name: StringName, new_value: float)

@export var max_health: float = 100.0
@export var attack: float = 10.0
@export var defense: float = 5.0
@export var speed: float = 200.0

# Runtime values (not saved)
var _current_health: float

func _init() -> void:
    _current_health = max_health

func get_current_health() -> float:
    return _current_health

func take_damage(amount: float) -> float:
    var actual_damage := maxf(amount - defense, 1.0)
    _current_health = maxf(_current_health - actual_damage, 0.0)
    stat_changed.emit("health", _current_health)
    return actual_damage

func heal(amount: float) -> void:
    _current_health = minf(_current_health + amount, max_health)
    stat_changed.emit("health", _current_health)

func duplicate_for_runtime() -> CharacterStats:
    var copy := duplicate() as CharacterStats
    copy._current_health = copy.max_health
    return copy
```

```gdscript
# Using resources
class_name Character
extends CharacterBody2D

@export var base_stats: CharacterStats
@export var weapon: WeaponData

var stats: CharacterStats

func _ready() -> void:
    # Create runtime copy to avoid modifying the resource
    stats = base_stats.duplicate_for_runtime()
    stats.stat_changed.connect(_on_stat_changed)

func attack() -> void:
    if weapon:
        print("Attacking with %s for %d damage" % [weapon.name, weapon.damage])

func _on_stat_changed(stat_name: StringName, value: float) -> void:
    if stat_name == "health" and value <= 0:
        die()
```

## Advanced Patterns, Performance & Best Practices

Object pooling (ObjectPool/PooledBullet with `returned_to_pool` signal), component system (HealthComponent/HitboxComponent/HurtboxComponent), async scene management with `ResourceLoader.load_threaded_request`, encrypted save system (SaveManager with `open_encrypted_with_pass` + Saveable component), performance tips for caching and hot-path optimization, and Do/Don't best practices.

See [references/advanced-patterns-and-save-system.md](references/advanced-patterns-and-save-system.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/advanced-patterns-and-save-system.md` | Object pooling, component system, scene management, save system, performance tips, best practices |

## Related Skills

- `unity-ecs-patterns` - When building games with Unity instead of Godot
- `game-architecture-patterns` - General game architecture patterns
