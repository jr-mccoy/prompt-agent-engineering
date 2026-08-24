---
title: "Game State Machine Design"
category: game-development/architecture
description: "Design hierarchical state machines for game states, character controllers, and AI behavior using FSM, HFSM, and pushdown automata patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - OC-01
difficulty: intermediate
tags:
  - architecture
  - state-machine
  - fsm
  - game-states
  - ai
  - character-controller
updated: "2026-03-19"
related_prompts:
  - domain-game-development/architecture/architecture_scene_management.md
  - domain-game-development/architecture/architecture_save_system.md
---

# Game State Machine Design

**Objective:** Design robust state machine architectures for game systems — including game state management (menu/play/pause), character controllers (idle/run/jump/attack), and AI behavior — using FSM, HFSM, and pushdown automata patterns appropriate to the complexity.

**When to Use:**
- Designing game flow (boot → menu → gameplay → pause → game over)
- Building character controllers with multiple movement and action states
- Implementing AI behavior for NPCs or enemies
- Refactoring spaghetti if/else chains in game logic into structured state patterns
- Don't use when: behavior requires highly dynamic, priority-based decision-making with many concurrent considerations (use behavior trees instead)

**Instructions:**

1. **Identify the State Machine Type Needed**
   - Count the number of distinct states and nesting levels required
   - **Flat FSM** — Use when there are fewer than ~10 states with no logical grouping. All states exist at the same level with direct transitions between them. Best for: simple game flow, basic character controllers, UI screen flow.
   - **Hierarchical FSM (HFSM)** — Use when states naturally group into parent/child relationships (e.g., a "Combat" super-state containing "Attacking", "Blocking", "Dodging"). Substates inherit parent transitions, reducing duplication. Best for: complex character controllers, multi-phase boss AI.
   - **Pushdown Automata** — Use when you need to pause a current state, push a new one onto a stack, and return later (e.g., gameplay → pause menu → resume gameplay). The stack preserves history. Best for: game flow with interrupts, nested menus, cutscene interruptions.
   - Document your choice and rationale before proceeding.

2. **Enumerate States with Entry/Exit/Update Actions**
   - For each state, define:
     - **State ID/Name** — unique, descriptive identifier (e.g., `PlayerState.Jumping`)
     - **Entry Action** — logic that runs once when entering the state (start animation, play sound, initialize timers)
     - **Update Action** — logic that runs every frame/tick while in the state (apply gravity, check input, update timers)
     - **Exit Action** — logic that runs once when leaving the state (stop animation, reset flags, clean up VFX)
     - **Allowed Transitions** — which states this state can transition to
   - Organize states into a table or diagram for clarity.

3. **Define Transitions with Conditions and Priorities**
   - For each transition, specify:
     - **Source State** → **Target State**
     - **Condition** — the trigger or predicate (input event, timer expiry, health threshold, collision)
     - **Priority** — when multiple transitions are valid simultaneously, which wins
     - **Guard Conditions** — additional checks that must pass (e.g., "can only jump if grounded")
     - **Transition Action** — optional logic during the transition itself (play transition animation, apply impulse)
   - Order transitions by priority within each state. First matching transition wins.

4. **Design State Data and Shared Blackboard**
   - **Per-State Data** — data scoped to a single state's lifetime (e.g., jump elapsed time, attack combo counter)
   - **Shared Blackboard** — data accessible across all states (e.g., health, position, velocity, input buffer)
   - Define clear ownership: which system writes, which reads
   - Avoid storing derived data — compute from authoritative sources
   - Plan serialization needs if state must survive save/load cycles

5. **Handle Edge Cases (Interrupted Transitions, Buffered Inputs)**
   - **Input Buffering** — queue inputs during un-cancellable states (e.g., buffer a jump press during landing recovery, execute when recovery ends)
   - **Interrupted Transitions** — define what happens when a state is forcibly exited (e.g., taking damage during attack wind-up: cancel attack, enter hit-stun)
   - **Re-entry** — can a state transition to itself? Define whether entry/exit actions re-fire.
   - **Simultaneous Triggers** — when two transitions are valid in the same frame, priority order resolves the conflict.
   - **Stuck Prevention** — every state must have at least one exit condition or a timeout fallback.

6. **CRITICAL: Verification Checklist**
   - [ ] **No orphaned states** — every state is reachable from the initial state
   - [ ] **No dead-end states** — every state (except terminal states like "GameOver") has at least one outgoing transition
   - [ ] **No impossible transitions** — every transition's condition can actually be satisfied during gameplay
   - [ ] **No missing exit conditions** — no state can trap the player/entity indefinitely
   - [ ] **Animation integration** — every state maps to an animation state or blend tree node
   - [ ] **All inputs handled** — pressing any button in any state has a defined result (even if "do nothing")
   - [ ] **State explosion check** — if you have more than 15-20 states in a flat FSM, consider refactoring to HFSM

**False-Positive Prevention:**

| Mistake | Correction |
|---------|------------|
| ❌ Using HFSM when a flat FSM with 5 states would suffice | ✅ Match complexity to actual state count — flat FSM is fine for simple systems |
| ❌ Assuming behavior trees are always superior to FSMs | ✅ FSMs are better for deterministic, well-defined state flows; BTs excel at priority-based decisions with many concurrent factors |
| ❌ Ignoring animation system integration | ✅ Design state machine in tandem with animation controller — states must map to animation states or blend tree parameters |
| ❌ Creating one mega-state-machine for everything | ✅ Separate concerns: game flow FSM, character controller FSM, and AI FSM should be independent machines |
| ❌ Letting state count explode via combinatorics | ✅ If combining axes (grounded/airborne × idle/moving × armed/unarmed), use parallel state machines or HFSM layers rather than N×M×K flat states |
| ❌ Hardcoding transitions inside state classes | ✅ Use data-driven transition tables so designers can tune without code changes |

**Expected Output:** A structured state machine design document that includes:

1. State machine type selection with rationale
2. Complete state enumeration table with entry/exit/update actions
3. Transition table or diagram with conditions and priorities
4. Blackboard data schema
5. Edge case handling strategy
6. Verification checklist results

**Example Output:**

```markdown
# Character Controller State Machine — 2D Action Platformer

## 1. State Machine Type Selection

**Type:** Hierarchical Finite State Machine (HFSM)

**Rationale:** The character has 12+ distinct states that naturally group into
ground states (Idle, Run, Crouch, Slide) and air states (Jump, Fall, WallSlide,
WallJump, Dash). HFSM allows shared transitions at the super-state level — for
example, all ground states share a "became airborne" transition to Fall, and all
states share a "health <= 0" transition to Dead. A flat FSM would require
duplicating these transitions across every state.

## 2. State Hierarchy

```
Root
├── Alive (super-state)
│   ├── Grounded (super-state)
│   │   ├── Idle
│   │   ├── Run
│   │   ├── Crouch
│   │   ├── Slide
│   │   └── Attack_Ground
│   ├── Airborne (super-state)
│   │   ├── Jump
│   │   ├── Fall
│   │   ├── WallSlide
│   │   ├── WallJump
│   │   ├── AirDash
│   │   └── Attack_Air
│   └── HitStun
└── Dead
```

## 3. State Definitions

### Grounded > Idle

| Property       | Value                                            |
|----------------|--------------------------------------------------|
| **Entry**      | Play "idle" animation; reset dash flag           |
| **Update**     | Check movement input; check jump input           |
| **Exit**       | (none)                                           |
| **Transitions**| → Run (if |moveInput.x| > deadzone)              |
|                | → Jump (if jumpPressed && grounded)              |
|                | → Crouch (if crouchPressed)                      |
|                | → Attack_Ground (if attackPressed)               |
|                | → Fall (if !grounded) [inherited from Grounded]  |

### Grounded > Run

| Property       | Value                                            |
|----------------|--------------------------------------------------|
| **Entry**      | Play "run" animation; set facing direction       |
| **Update**     | Apply horizontal velocity; flip sprite           |
| **Exit**       | (none)                                           |
| **Transitions**| → Idle (if |moveInput.x| < deadzone)             |
|                | → Jump (if jumpPressed && grounded)              |
|                | → Slide (if crouchPressed && |velocity.x| > 5)  |
|                | → Attack_Ground (if attackPressed)               |

### Airborne > Jump

| Property       | Value                                            |
|----------------|--------------------------------------------------|
| **Entry**      | Apply jump impulse; play "jump" anim; set        |
|                | jumpHoldTimer = 0; consume coyote time           |
| **Update**     | If jumpHeld, extend jump (variable height);      |
|                | apply gravity; increment jumpHoldTimer            |
| **Exit**       | Reset jumpHoldTimer                              |
| **Transitions**| → Fall (if velocity.y < 0 OR jumpReleased OR     |
|                |   jumpHoldTimer > maxJumpHoldTime)                |
|                | → WallSlide (if touchingWall && moveInput toward  |
|                |   wall)                                           |
|                | → AirDash (if dashPressed && !dashUsed)           |
|                | → Attack_Air (if attackPressed)                   |

### Airborne > WallSlide

| Property       | Value                                            |
|----------------|--------------------------------------------------|
| **Entry**      | Play "wall_slide" anim; reduce gravity to         |
|                | wallSlideGravity; spawn dust VFX                  |
| **Update**     | Apply reduced gravity; check for input away       |
|                | from wall (wall release)                          |
| **Exit**       | Restore normal gravity; stop dust VFX             |
| **Transitions**| → WallJump (if jumpPressed)                       |
|                | → Fall (if !touchingWall OR moveInput away)       |
|                | → Idle (if grounded) [inherited from Airborne]    |

### HitStun

| Property       | Value                                            |
|----------------|--------------------------------------------------|
| **Entry**      | Play "hit" anim; apply knockback impulse;         |
|                | set stunTimer = stunDuration; flash sprite        |
| **Update**     | Decrement stunTimer; apply knockback decel        |
| **Exit**       | Stop sprite flash; grant i-frames                 |
| **Transitions**| → Idle (if stunTimer <= 0 && grounded)            |
|                | → Fall (if stunTimer <= 0 && !grounded)           |
|                | → Dead (if health <= 0) [inherited from Alive]    |

## 4. Transition Priority Table (per-frame evaluation order)

| Priority | Transition           | Condition                    | Scope      |
|----------|----------------------|------------------------------|------------|
| 0 (max)  | Any → Dead           | health <= 0                  | Root.Alive |
| 1        | Any → HitStun        | damageTakenThisFrame > 0     | Root.Alive |
| 2        | Grounded.* → Fall    | !isGrounded                  | Grounded   |
| 3        | Airborne.* → Idle    | isGrounded && vel.y <= 0     | Airborne   |
| 4        | State-specific       | (see state definitions)      | Per-state  |

## 5. Shared Blackboard Schema

```csharp
public class CharacterBlackboard
{
    // Physics
    public Vector2 Position;
    public Vector2 Velocity;
    public bool IsGrounded;
    public bool IsTouchingWall;
    public int WallDirection; // -1 left, 0 none, 1 right

    // Input (buffered)
    public Vector2 MoveInput;
    public bool JumpPressed;   // true for 1 frame on press
    public bool JumpHeld;      // true while held
    public bool AttackPressed;
    public bool DashPressed;
    public bool CrouchPressed;

    // Resources
    public int Health;
    public int MaxHealth;
    public bool DashAvailable;
    public float CoyoteTimeRemaining;

    // Combat
    public int DamageTakenThisFrame;
    public Vector2 KnockbackDirection;

    // Timers (managed by states)
    public float JumpHoldTimer;
    public float StunTimer;
    public float AttackTimer;
}
```

## 6. Input Buffer Implementation

```csharp
public class InputBuffer
{
    private struct BufferedInput
    {
        public InputAction Action;
        public float Timestamp;
    }

    private Queue<BufferedInput> _buffer = new();
    private float _bufferWindow = 0.15f; // 150ms buffer

    public void RecordInput(InputAction action, float time)
    {
        _buffer.Enqueue(new BufferedInput
        {
            Action = action,
            Timestamp = time
        });
    }

    public bool ConsumeInput(InputAction action, float currentTime)
    {
        // Purge expired inputs
        while (_buffer.Count > 0 &&
               currentTime - _buffer.Peek().Timestamp > _bufferWindow)
        {
            _buffer.Dequeue();
        }

        // Check for matching buffered input
        var temp = new Queue<BufferedInput>();
        bool found = false;

        while (_buffer.Count > 0)
        {
            var input = _buffer.Dequeue();
            if (!found && input.Action == action)
            {
                found = true; // consume it
            }
            else
            {
                temp.Enqueue(input);
            }
        }

        _buffer = temp;
        return found;
    }
}
```

## 7. Edge Case Handling

| Edge Case                        | Resolution                                   |
|----------------------------------|----------------------------------------------|
| Jump pressed while in attack     | Buffer jump input; execute on attack end      |
| Walked off ledge (no jump)       | Grant coyote time (0.1s window to still jump) |
| Damage during attack wind-up     | Interrupt → HitStun (priority 1 beats all)    |
| WallSlide with no wall (moved)   | Immediate transition → Fall                   |
| Dash while dash on cooldown      | Input ignored (no buffer for dash)            |
| Attack → Attack (combo)          | Attack_Ground self-transition with combo++    |
| Landing during AirDash           | → Idle with brief recovery frames             |
| Multiple damage in same frame    | Sum damage, single HitStun transition         |

## 8. Verification Checklist

- [x] **No orphaned states** — all states reachable from Idle (initial state)
- [x] **No dead-end states** — Dead is terminal (intentional); all others
      have outgoing transitions
- [x] **No impossible transitions** — all conditions map to real game inputs
      or physics events
- [x] **No missing exit conditions** — every state has timeout or input exit;
      HitStun uses stunTimer; Attack uses attackTimer
- [x] **Animation integration** — each state maps 1:1 to Animator states;
      transitions use CrossFade with 0.05s blend
- [x] **All inputs handled** — unmapped inputs in each state are no-ops
      (explicitly documented)
- [x] **State count check** — 12 leaf states across 3 hierarchy levels;
      HFSM is appropriate, no explosion risk
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — opens with precise scope covering FSM types and game systems
- ST-02 (Structured Sequential Instructions) — six numbered steps from type selection through verification
- RT-02 (Systematic Classification) — classifies FSM type by complexity and nesting requirements
- DS-01 (Framework Application) — applies formal automata theory (FSM, HFSM, pushdown automata)
- OC-01 (Verification Checklist) — critical verification step ensures no orphaned states, dead ends, or missing exits

**Related Prompts:**
- `domain-game-development/architecture/architecture_scene_management.md` — Scene loading and transition systems
- `domain-game-development/architecture/architecture_save_system.md` — Persisting state machine data across save/load
- `domain-software-engineering/analysis/architecture/architecture_design_pattern_identification.md` — Identifying State pattern usage in existing code
