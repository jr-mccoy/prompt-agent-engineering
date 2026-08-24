---
title: "Network State Synchronization Patterns"
category: game-development/multiplayer
description: "Design state synchronization with snapshot interpolation, client-side prediction, server reconciliation, and delta compression"
techniques:
  - ST-01
  - ST-02
  - RT-05
  - DS-03
  - OC-01
difficulty: advanced
tags:
  - multiplayer
  - state-sync
  - prediction
  - interpolation
  - reconciliation
  - networking
updated: "2026-03-19"
related_prompts:
  - domain-game-development/multiplayer/multiplayer_netcode_architecture.md
  - domain-game-development/multiplayer/multiplayer_matchmaking_lobby.md
  - domain-game-development/architecture/architecture_state_machine_design.md
---

# Network State Synchronization Patterns

**Objective:** Design network state synchronization systems covering snapshot interpolation, client-side prediction, server reconciliation, delta compression, and interest management to deliver smooth multiplayer gameplay despite network latency and packet loss.

## When to Use

- Use when implementing the sync layer after choosing your netcode architecture
- Use when players report "rubber-banding," teleporting, or hit registration issues
- Use when optimizing bandwidth for a live multiplayer game
- Don't use for architecture selection — use `multiplayer_netcode_architecture.md` first

## Instructions

1. **Identify Sync Requirements by Entity Type**
   - Categorize all networked entities by sync needs:
     - **Player characters:** High frequency, predicted locally, reconciled with server
     - **Other players:** Interpolated from server snapshots, no prediction
     - **Projectiles:** Predicted locally (hitscan), or server-authoritative (projectile physics)
     - **World state:** Low frequency, reliable delivery (doors, pickups, destructibles)
     - **UI/score state:** Event-driven, reliable ordered
   - Define update frequency per category (not everything needs every tick)

2. **Design Snapshot System**
   - Server captures full world state at each tick → snapshot
   - Assign monotonically increasing sequence numbers
   - Include server timestamp and tick number for client-side timing
   - Store last N snapshots on server for delta compression baseline

3. **Implement Client-Side Prediction** (for local player)
   - Client applies input immediately to local simulation (prediction)
   - Store input buffer: `[tick_number, input_state]` for reconciliation
   - Run same simulation logic as server (shared codebase or deterministic)
   - Handle prediction for: movement, ability activation, weapon firing (visuals only)
   - DO NOT predict: damage application, score changes, inventory changes

4. **Implement Server Reconciliation**
   - When client receives authoritative snapshot:
     - Find the server tick in the input buffer
     - Compare predicted state vs server state for that tick
     - If mismatch: rewind to server state, replay all inputs from that tick to present
     - Smooth the correction over 100-200ms to avoid visual snapping
   - Track prediction error rate — if consistently >10%, investigate desync causes

5. **Design Entity Interpolation** (for remote entities)
   - Buffer 2-3 snapshots before rendering (interpolation delay = 2× tick interval)
   - Interpolate between two buffered snapshots for smooth movement
   - For rotation: use spherical interpolation (slerp)
   - Handle missing snapshots: extrapolate briefly (50-100ms max), then freeze
   - Extrapolation limit: never extrapolate beyond 150ms — show last known state instead

6. **Implement Delta Compression**
   - Send only changed fields relative to last acknowledged snapshot
   - Per-entity delta: if entity unchanged since last ack, skip entirely
   - Per-field delta: only send position if position changed, skip health if same
   - Use bitfield header: 1 bit per field, 1 = included, 0 = unchanged
   - Quantize floats: position to 0.01 units (16-bit fixed), rotation to 0.1 degrees

7. **Design Interest Management** (for large player counts)
   - Area of Interest (AOI): only sync entities within relevant radius per player
   - Priority system: nearby entities sync at full rate, distant at reduced rate
   - Relevancy rules: teammates always relevant, enemies within range, world events global
   - Handle AOI transitions: smooth fade-in when entities enter interest area

8. **CRITICAL: Validate Sync Quality**
   - Test at 50ms, 100ms, 200ms, and 300ms simulated latency
   - Test with 1%, 3%, 5% packet loss
   - Verify prediction reconciliation doesn't produce visible rubber-banding
   - Verify interpolation doesn't produce visible teleporting at normal latency
   - Measure bandwidth with delta compression vs without — target 50%+ reduction
   - Test edge cases: player spawning, teleportation, rapid direction changes

**False-Positive Prevention (MUST follow):**

❌ **DON'T:**
- Don't predict everything — only predict what the local player controls
- Don't extrapolate remote players beyond 150ms — freezing is better than wrong prediction
- Don't assume prediction errors are bugs — some mismatch is normal under latency
- Don't skip interpolation delay — it exists to absorb jitter, removing it causes stutter
- Don't quantize too aggressively — test visual quality at each precision level

✅ **DO:**
- Measure actual correction magnitudes — large corrections indicate simulation desync
- Test with real network conditions (Wi-Fi, mobile), not just simulated latency
- Profile CPU cost of reconciliation replays — replaying 10 ticks at 128Hz is expensive
- Use different sync strategies for different entity types (don't one-size-fits-all)
- Log prediction mismatches to identify systematic desync sources

## Expected Output

A state synchronization design document including:

- Entity sync category matrix (entity type × frequency × strategy)
- Snapshot structure and serialization format
- Prediction and reconciliation algorithm
- Interpolation configuration (buffer depth, extrapolation limits)
- Delta compression strategy with bandwidth savings estimate
- Interest management rules (if applicable)
- Test results at various latency/loss levels

## Example Output

```markdown
## State Sync Design — "Starfall Arena" (4v4 FPS)

### 1. Entity Sync Matrix

| Entity Type | Count | Frequency | Strategy | Reliability |
|------------|-------|-----------|----------|-------------|
| Local player | 1 | 64 Hz | Predicted + Reconciled | Unreliable |
| Remote players | 7 | 64 Hz | Interpolated (2-tick buffer) | Unreliable |
| Hitscan shots | — | Event | Predicted (visual), server-validated | Reliable |
| Projectiles | 0-20 | 64 Hz | Server-authoritative, interpolated | Unreliable |
| Pickups | 0-10 | Event-driven | Server-authoritative | Reliable |
| Score/round | — | Event | Server-authoritative | Reliable-ordered |
| Kill feed | — | Event | Server → All clients | Reliable-ordered |

### 2. Snapshot Structure

```c
struct Snapshot {
    uint32_t tick_number;         // Server tick (monotonic)
    float    server_time;         // Server timestamp (seconds)
    uint16_t entity_count;        // Active entities this snapshot
    uint32_t delta_baseline_tick; // Which snapshot this is delta'd against

    // Per-entity data (variable length)
    EntityState entities[];
};

struct EntityState {
    uint16_t entity_id;
    uint8_t  entity_type;      // Player, Projectile, Pickup
    uint16_t changed_fields;   // Bitfield: which fields are included

    // Fields (only included if corresponding bit set):
    vec3     position;          // Bit 0 - quantized to 0.01 units
    quat     rotation;          // Bit 1 - quantized to 10-bit per component
    vec3     velocity;          // Bit 2 - quantized to 0.1 units/s
    uint8_t  health;            // Bit 3
    uint8_t  weapon_id;         // Bit 4
    uint8_t  anim_state;        // Bit 5
    uint8_t  flags;             // Bit 6 (crouching, sprinting, etc.)
};
```

### 3. Client-Side Prediction (Local Player)

```
Frame N (client):
1. Sample input (WASD, mouse, abilities)
2. Store input: input_buffer[tick_N] = input
3. Apply input to local player simulation:
   - Movement: apply acceleration, gravity, collision
   - Abilities: start cooldown, play animation
   - Weapons: muzzle flash, tracer (visual only)
4. Send input to server: {tick_N, input}
5. Render predicted state

When server snapshot arrives (for tick_S):
1. Find tick_S in input_buffer
2. Compare server_position vs predicted_position at tick_S
3. If error > threshold (0.01 units):
   a. Rewind: set state = server_state at tick_S
   b. Replay: for tick in [S+1 ... current_tick]:
      - Apply input_buffer[tick] to state
   c. Smooth: blend visual position over 100ms
4. Discard inputs older than tick_S from buffer
```

**Reconciliation smoothing:**
```
visual_position = lerp(
    visual_position,
    simulation_position,
    1.0 - pow(0.05, delta_time)  // Exponential ease, 95% in ~100ms
);
```

### 4. Entity Interpolation (Remote Players)

**Configuration:**
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Buffer depth | 2 snapshots (31.2ms at 64Hz) | Absorbs 1 dropped packet |
| Interpolation method | Linear for position, slerp for rotation | Sufficient for 64Hz |
| Extrapolation limit | 3 snapshots (46.8ms) | Beyond this, freeze last state |
| Jitter buffer adaptation | Expand to 3 snapshots if >2% loss detected | Adaptive smoothing |

**Interpolation algorithm:**
```
render_time = current_time - interpolation_delay

// Find two snapshots bracketing render_time
snapshot_a = find_snapshot_before(render_time)
snapshot_b = find_snapshot_after(render_time)

if (snapshot_a && snapshot_b):
    t = (render_time - snapshot_a.time) / (snapshot_b.time - snapshot_a.time)
    rendered_position = lerp(snapshot_a.position, snapshot_b.position, t)
    rendered_rotation = slerp(snapshot_a.rotation, snapshot_b.rotation, t)
elif (snapshot_a && !snapshot_b):
    // Extrapolate using velocity (limited duration)
    elapsed = render_time - snapshot_a.time
    if elapsed < extrapolation_limit:
        rendered_position = snapshot_a.position + snapshot_a.velocity * elapsed
    else:
        rendered_position = snapshot_a.position  // Freeze
```

### 5. Delta Compression Results

**Before delta compression:**
- Full snapshot (8 players): 384 bytes
- At 64 Hz: 24.6 KB/s per client

**After delta compression:**
- Average delta snapshot: 96 bytes (75% reduction)
- Typical changes per tick: 2-3 players moving, 1 shooting
- At 64 Hz: 6.1 KB/s per client

**Quantization scheme:**
| Field | Raw Size | Quantized | Precision |
|-------|---------|-----------|-----------|
| Position (vec3) | 12 bytes | 6 bytes | 0.01 unit (1cm) |
| Rotation (quat) | 16 bytes | 4 bytes | ~0.35 degrees |
| Velocity (vec3) | 12 bytes | 6 bytes | 0.1 unit/s |
| Health | 1 byte | 1 byte | 1 HP |

### 6. Validation Results

| Test Condition | Prediction Error | Visual Quality | Verdict |
|---------------|-----------------|----------------|---------|
| 50ms RTT, 0% loss | <0.02 units avg | Smooth, no corrections visible | ✅ Excellent |
| 100ms RTT, 1% loss | 0.05 units avg | Occasional micro-correction | ✅ Good |
| 200ms RTT, 3% loss | 0.15 units avg | Visible corrections on direction change | ⚠️ Acceptable |
| 300ms RTT, 5% loss | 0.4 units avg | Frequent corrections, playable but degraded | ⚠️ Show warning |

**Recommendation:** Display latency indicator at >150ms RTT. Show "poor connection" warning at >250ms.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defines smooth multiplayer as the measurable goal
- **ST-02 (Structured Sequential Instructions):** Eight-step process building from categorization to validation
- **RT-05 (Evidence-Based Reasoning):** Requires bandwidth calculations, latency measurements, error metrics
- **DS-03 (Tool and Methodology Suggestions):** Provides specific algorithms, data structures, and quantization schemes
- **OC-01 (Structured Output Format):** Tables, code samples, and test result matrices

## Related Prompts

- [Netcode Architecture](multiplayer_netcode_architecture.md) — Select topology before designing sync
- [Matchmaking & Lobby](multiplayer_matchmaking_lobby.md) — Session setup before sync begins
- [State Machine Design](../architecture/architecture_state_machine_design.md) — Character state machines interact with prediction
