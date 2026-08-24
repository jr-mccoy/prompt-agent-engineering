---
title: "Multiplayer Netcode Architecture Design"
category: game-development/multiplayer
description: "Design multiplayer networking architecture covering topology selection, tick rates, bandwidth budgets, and protocol selection"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-03
difficulty: advanced
tags:
  - multiplayer
  - networking
  - netcode
  - architecture
  - client-server
  - udp
updated: "2026-03-19"
related_prompts:
  - domain-game-development/multiplayer/multiplayer_state_sync.md
  - domain-game-development/multiplayer/multiplayer_matchmaking_lobby.md
  - domain-game-development/performance/performance_frame_budget_analysis.md
---

# Multiplayer Netcode Architecture Design

**Objective:** Design a multiplayer networking architecture for a game, selecting the appropriate topology (client-server, P2P, relay), tick rate, bandwidth budget, protocol, and authority model based on genre, player count, and platform constraints.

## When to Use

- Use when designing multiplayer networking for a new game from scratch
- Use when evaluating whether an existing architecture fits scaling or latency requirements
- Use when choosing between networking libraries/frameworks (Netcode for GameObjects, Mirror, Photon, ENet)
- Don't use for single-player save sync — use `architecture_save_system.md` instead

## Instructions

1. **Define Multiplayer Requirements**
   - Game genre and interaction type: competitive twitch (FPS, fighting), cooperative PvE, turn-based, MMO
   - Maximum concurrent players per session (2, 4, 16, 64, 100+, MMO-scale)
   - Latency tolerance: tight (<50ms required, FPS), moderate (<150ms, action RPG), relaxed (<300ms, strategy)
   - Platform targets: PC, console, mobile, cross-play combinations
   - Session model: persistent worlds, match-based, drop-in/drop-out

2. **Select Network Topology**
   - **Dedicated server (client-server):** Best for competitive, anti-cheat, 8+ players
     - Pros: Authoritative, scalable, cheat-resistant, consistent for all players
     - Cons: Server hosting cost, single point of failure, added latency
   - **Listen server (player-hosted):** Budget option, 2-8 players
     - Pros: No hosting cost, low latency for host, simpler infrastructure
     - Cons: Host advantage, host migration needed, limited to host's bandwidth
   - **Peer-to-peer (mesh):** For 2-4 players, cooperative
     - Pros: No server needed, lowest latency between peers, cheap
     - Cons: Cheat-vulnerable, scales poorly (O(n²) connections), NAT traversal pain
   - **Relay server:** P2P with relay for NAT traversal (Steam, Epic, Xbox Live)
     - Pros: NAT-friendly, no dedicated server logic, moderate cost
     - Cons: Added relay latency, still cheat-vulnerable

3. **Determine Authority Model**
   - **Server-authoritative:** Server validates all actions, clients predict and reconcile
     - Use for: competitive games, anti-cheat priority
   - **Client-authoritative:** Clients own their state, server relays
     - Use for: cooperative PvE where trust is acceptable
   - **Hybrid:** Server-authoritative for game-critical state, client-authoritative for cosmetic
     - Use for: most games (position = server, animations = client)

4. **Design Tick Rate and Update Frequency**
   - **Server tick rate:** How often the server processes game state
     - FPS competitive: 64-128 Hz (CS2: 64, Valorant: 128)
     - Action games: 30-60 Hz
     - Strategy/RPG: 10-20 Hz
   - **Client send rate:** How often clients send input to server (usually matches tick rate)
   - **Client receive/interpolation rate:** Usually 2× tick rate for smooth interpolation
   - Calculate bandwidth per player: `tick_rate × avg_packet_size × direction`

5. **Set Bandwidth Budget**
   - Per-player bandwidth targets:
     - Mobile: 20-50 KB/s (data cost sensitivity)
     - Console/PC: 50-200 KB/s (typical broadband)
     - Competitive PC: 200-500 KB/s (acceptable for ranked play)
   - Design packet structure: header overhead, payload, compression
   - Plan for variable conditions: packet loss (1-5% typical), jitter, out-of-order delivery

6. **Select Protocol and Transport**
   - **UDP (custom reliability):** Best for real-time games — control over reliability, ordering
   - **UDP with reliability layer:** ENet, GameNetworkingSockets (Valve), LiteNetLib
   - **WebSocket/WebRTC:** For browser-based or cross-platform (adds latency)
   - **TCP:** Only for turn-based or non-real-time (chat, lobbies, matchmaking)
   - Consider: MTU limits (1200-1400 bytes safe), fragmentation avoidance, encryption (DTLS)

7. **Plan Infrastructure**
   - Server deployment: cloud (AWS GameLift, Azure PlayFab, Google Cloud) vs bare metal
   - Region selection: minimum 3 regions for global coverage (US, EU, Asia)
   - Scaling: auto-scale based on player demand, warm pools for instant availability
   - Monitoring: player latency dashboards, packet loss tracking, server utilization

8. **CRITICAL: Validate Architecture Against Requirements**
   - Calculate worst-case latency: client input → server process → broadcast → client render
   - Verify bandwidth budget at maximum player count with maximum entity count
   - Test NAT traversal success rate if using P2P or relay
   - Confirm tick rate provides acceptable responsiveness for the game's genre
   - Verify chosen library/framework supports all target platforms
   - Test with simulated 100ms, 200ms, 300ms latency to find the "feels bad" threshold

**False-Positive Prevention (MUST follow):**

❌ **DON'T:**
- Don't recommend dedicated servers for a 2-player cooperative indie game (overkill, costly)
- Don't recommend P2P for competitive multiplayer (cheat vulnerability)
- Don't assume 128-tick is always better — it doubles bandwidth and CPU cost
- Don't ignore mobile bandwidth costs when designing for cross-play
- Don't recommend "just use TCP" for real-time gameplay

✅ **DO:**
- Match topology to player count, budget, and competitive needs
- Calculate actual bandwidth numbers, not just "it should be fine"
- Consider the hosting cost implications for indie vs studio budgets
- Account for worst-case network conditions (150ms latency, 3% packet loss)
- Recommend proven middleware when custom netcode isn't justified

## Expected Output

A netcode architecture document including:

- Requirements summary with latency and player count targets
- Topology selection with rationale
- Authority model design
- Tick rate and bandwidth calculations
- Protocol and transport selection
- Infrastructure plan with regions and scaling
- Latency budget breakdown (client → server → client)

## Example Output

```markdown
## Netcode Architecture — "Starfall Arena" (4v4 Competitive Shooter)

### 1. Requirements

| Attribute | Value |
|-----------|-------|
| Genre | 4v4 team-based FPS |
| Max players/session | 8 (4v4) + 2 spectators |
| Latency target | <60ms RTT for competitive play |
| Platforms | PC + Console cross-play |
| Session model | Match-based, 10-minute rounds |
| Anti-cheat priority | High (ranked competitive) |

### 2. Topology: Dedicated Server (Client-Server)

**Decision: Dedicated server**

| Option | Fit | Reason |
|--------|-----|--------|
| Dedicated server | ✅ Selected | Anti-cheat, fair for all 8 players, consistent tick |
| Listen server | ❌ Rejected | Host advantage unacceptable for competitive FPS |
| P2P mesh | ❌ Rejected | 8 players = 28 connections, cheat-vulnerable |
| Relay | ❌ Rejected | Added relay latency hurts competitive play |

**Infrastructure:**
- Cloud provider: AWS GameLift (auto-scaling, FlexMatch integration)
- Regions: us-east-1, eu-west-1, ap-northeast-1 (US, EU, Asia)
- Instance type: c5.large (2 vCPU, 4 GB RAM) — supports 4 matches per instance
- Target: 50ms maximum server processing time per tick

### 3. Authority Model: Server-Authoritative with Client Prediction

```
Client                          Server
  |                               |
  |-- Input (keys, mouse) ------>|
  |   (predict movement locally) |-- Validate input
  |                               |-- Simulate world
  |<--- State snapshot -----------|-- Broadcast state
  |   (reconcile prediction)      |
  |   (interpolate other players) |
```

**Authority boundaries:**
- **Server-authoritative:** Position, health, ammo, hit detection, score
- **Client-authoritative:** Camera angle, cosmetic animations, UI state
- **Predicted (reconciled):** Own movement, weapon firing (visual only)

### 4. Tick Rate and Update Budget

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Server tick rate | 64 Hz (15.6ms) | Industry standard for competitive FPS |
| Client send rate | 64 Hz | Match server tick for responsive input |
| Client interpolation | 128 Hz | 2× tick for smooth visual interpolation |
| Interpolation delay | 2 ticks (31.2ms) | Buffer for network jitter |

### 5. Bandwidth Budget

**Per-player calculation:**

```
Player state packet:
  - Position (vec3, 12B) + Rotation (quat, 8B)     = 20 bytes
  - Velocity (vec3, 12B)                             = 12 bytes
  - Health (uint8)                                   = 1 byte
  - Weapon state (uint16)                            = 2 bytes
  - Animation state (uint8)                          = 1 byte
  - Input sequence number (uint16)                   = 2 bytes
  - Packet header (sequence, ack, ack_bitfield)      = 8 bytes
  Total per player per tick:                         = 46 bytes

Snapshot packet (8 players):
  - Header + world state                             = 16 bytes
  - 8 × 46 bytes player data                        = 368 bytes
  - Game events (kills, spawns, pickups)             = ~50 bytes avg
  - Delta compression savings                        = -40%
  Total per snapshot:                                ≈ 260 bytes

Bandwidth per client:
  - Download: 260 bytes × 64 Hz                     = 16.6 KB/s
  - Upload: 46 bytes × 64 Hz                        = 2.9 KB/s
  - Total per client:                                = 19.5 KB/s
  - With overhead (retransmits, keepalive):          ≈ 25 KB/s

Server total (10 clients):
  - Upload: 16.6 KB/s × 10                          = 166 KB/s
  - Download: 2.9 KB/s × 10                         = 29 KB/s
  - Total server bandwidth:                          ≈ 195 KB/s per match
```

**Budget assessment:** ✅ Well within PC/console limits (200 KB/s target)

### 6. Protocol Stack

```
Application:    Game state serialization (custom binary)
Reliability:    Custom reliable-ordered (for events), unreliable (for state)
Transport:      UDP (via GameNetworkingSockets / Valve)
Security:       DTLS 1.3 encryption
Network:        IPv4 + IPv6 dual-stack
```

**Packet types:**
| Type | Reliability | Use |
|------|------------|-----|
| Input | Unreliable, redundant (send last 3) | Client → Server |
| Snapshot | Unreliable, delta-compressed | Server → Client |
| Events | Reliable-ordered | Kill confirms, round state, chat |
| Keepalive | Unreliable | Connection health, RTT measurement |

### 7. Latency Budget

```
Total input-to-display latency breakdown:

Client input polling:           1 ms
Client send:                    0.5 ms
Network (client → server):     25 ms (half RTT)
Server queue wait:              8 ms (half tick at 64Hz)
Server processing:             3 ms
Network (server → client):    25 ms (half RTT)
Client interpolation delay:    31.2 ms (2 ticks)
Client render:                 16.7 ms (60 FPS)
─────────────────────────────────────
Total:                        110.4 ms

At 50ms RTT (good connection):  ~110ms input-to-display
At 100ms RTT (moderate):        ~160ms input-to-display
At 200ms RTT (poor):            ~260ms input-to-display — degraded but playable
```

### 8. Scaling Plan

| Player Count | Matches | Servers (c5.large) | Monthly Cost (est.) |
|-------------|---------|-------------------|-------------------|
| 100 CCU | 12 | 3 | ~$300 |
| 1,000 CCU | 125 | 32 | ~$3,000 |
| 10,000 CCU | 1,250 | 313 | ~$28,000 |
| 100,000 CCU | 12,500 | 3,125 | ~$250,000 |

**Auto-scaling policy:**
- Scale up: when match queue time >30s, add instances in steps of 10
- Scale down: when server utilization <30% for 10 minutes, remove excess
- Warm pool: keep 10% extra capacity pre-warmed for demand spikes
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defines specific architecture design scope
- **ST-02 (Structured Sequential Instructions):** Eight-step process from requirements to validation
- **RT-02 (Multi-Dimensional Analysis):** Evaluates topology, authority, tick rate, bandwidth, protocol independently
- **RT-05 (Evidence-Based Reasoning):** Requires actual bandwidth calculations and latency budgets
- **DS-03 (Tool and Methodology Suggestions):** Recommends specific libraries, cloud services, and protocols

## Related Prompts

- [State Synchronization](multiplayer_state_sync.md) — Design the prediction and interpolation layer
- [Matchmaking & Lobby](multiplayer_matchmaking_lobby.md) — Connect players before the netcode takes over
- [Frame Budget Analysis](../performance/performance_frame_budget_analysis.md) — Server tick processing fits within frame budget
