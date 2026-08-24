---
title: "Matchmaking & Lobby System Design"
category: game-development/multiplayer
description: "Design matchmaking systems with rating algorithms, queue management, skill-based matching, party handling, and lobby session management"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
  - OC-01
difficulty: intermediate
tags:
  - multiplayer
  - matchmaking
  - elo
  - lobby
  - ranking
  - session-management
updated: "2026-03-19"
related_prompts:
  - domain-game-development/multiplayer/multiplayer_netcode_architecture.md
  - domain-game-development/multiplayer/multiplayer_state_sync.md
  - domain-game-development/design/design_player_progression.md
---

# Matchmaking & Lobby System Design

**Objective:** Design matchmaking and lobby systems covering skill rating algorithms (ELO, Glicko-2, TrueSkill), queue management, skill-based matching, party/group handling, and pre-game lobby session management for competitive and casual multiplayer games.

## When to Use

- Use when designing matchmaking for a new multiplayer game
- Use when match quality is poor (skill mismatches, long queue times, unfair teams)
- Use when adding ranked/competitive modes to an existing game
- Don't use for in-game networking — use `multiplayer_netcode_architecture.md` instead

## Instructions

1. **Define Matchmaking Requirements**
   - Game mode types: 1v1, team (4v4, 5v5), FFA, asymmetric (1v4)
   - Queue types: casual (fast, loose matching), ranked (tight, skill-based), custom/private
   - Party support: solo only, duo, full-stack, mixed party sizes
   - Cross-play: same pool for all platforms, or input-based separation (KB+M vs controller)
   - Region policy: strict region lock, prefer region with fallback, global pool

2. **Select Rating Algorithm**
   - **ELO:** Simple, proven for 1v1 (chess). Rating ±K-factor on win/loss.
     - Pros: Simple to implement, well-understood
     - Cons: Poor for team games, no uncertainty tracking, slow convergence
   - **Glicko-2:** Adds rating deviation (uncertainty) and volatility.
     - Pros: Handles inactivity, faster convergence, confidence intervals
     - Cons: More complex, rating periods need tuning
   - **TrueSkill / TrueSkill 2:** Microsoft's system, designed for team games.
     - Pros: Handles teams, parties, multiple teams, draw probability
     - Cons: Proprietary (TrueSkill 2), complex implementation
   - **OpenSkill:** Open-source TrueSkill alternative, no patent concerns.
     - Pros: Free, handles teams, well-maintained libraries
     - Cons: Less battle-tested than TrueSkill at scale

3. **Design Queue Algorithm**
   - **Matching criteria priority:** Skill > Latency > Queue time > Party balance
   - **Search window expansion:** Start tight (±100 MMR), widen over time
     - 0-30s: ±100 MMR
     - 30-60s: ±200 MMR
     - 60-120s: ±400 MMR
     - 120s+: ±800 MMR or match with best available
   - **Party handling:** Match party vs party when possible, solo-fill if needed
   - **Backfill:** For casual modes, allow mid-match joins with protections (no join if <2min left)

4. **Design Rank/Division System** (for ranked mode)
   - Map continuous MMR to visible ranks (Bronze → Silver → Gold → Diamond → Master)
   - Define promotion/demotion thresholds with hysteresis (prevent rank oscillation)
   - Design placement matches (8-10 games) with accelerated rating changes
   - Consider rank decay for inactive players (after 14-30 days)
   - Separate display rank from matchmaking MMR (display can be aspirational)

5. **Design Lobby and Session Flow**
   - Pre-match lobby: player list, ready-up, character/loadout select, chat, map vote
   - Ready check: all players must confirm within timeout (30-60s), or re-queue
   - Dodge/leave penalty: escalating cooldowns (5min → 15min → 1hr → 24hr)
   - Session lifecycle: queue → match found → lobby → loading → in-game → post-game → queue
   - Handle disconnects: allow reconnect within 2-3 minutes, backfill or continue short

6. **Plan Anti-Smurf and Fair Play**
   - New account detection: accelerated placement (higher K-factor for first 20 games)
   - Win-streak detection: temporary MMR boost for players on 5+ win streaks
   - Party skill spread limit: don't allow Diamond+Bronze parties in ranked
   - Report/feedback system: track player behavior (toxicity, intentional loss)

7. **CRITICAL: Validate Match Quality**
   - Measure average skill difference per match — target <5% of skill range
   - Measure queue time distribution — target 80% of matches found within 60s
   - Measure perceived fairness (win rate should converge to 50% ±5% per player)
   - Test edge cases: very high/low skill players, tiny population (off-peak hours), all parties
   - Simulate with historical data if available: re-run matchmaker on past sessions

**False-Positive Prevention (MUST follow):**

❌ **DON'T:**
- Don't use pure ELO for team games — it doesn't account for team composition
- Don't show raw MMR to players — use display ranks to manage expectations
- Don't match across 200ms+ RTT difference in competitive modes
- Don't make queue windows expand too fast — bad matches cause more churn than waiting
- Don't assume equal skill means equal fun — consider playstyle diversity

✅ **DO:**
- Weight recent performance more heavily than historical (recency bias in rating)
- Separate casual and ranked MMR — players experiment in casual, tryhard in ranked
- Consider population size: small games need wider skill windows, accept lower quality
- Track match quality metrics from day one — you can't improve what you don't measure
- Test with simulated player pools before launch (Monte Carlo queue simulations)

## Expected Output

A matchmaking and lobby design document including:

- Rating algorithm selection with configuration parameters
- Queue algorithm with search window expansion timeline
- Rank/division mapping table
- Lobby session flow diagram
- Anti-smurf and fair play measures
- Match quality KPIs and targets

## Example Output

```markdown
## Matchmaking Design — "Starfall Arena" (4v4 Competitive Shooter)

### 1. Requirements

| Attribute | Value |
|-----------|-------|
| Game modes | Casual 4v4, Ranked 4v4, Custom |
| Party sizes | Solo, Duo, Trio, 4-stack |
| Platforms | PC + Console (cross-play) |
| Regions | NA, EU, Asia-Pacific |
| Expected population | 5,000-50,000 CCU |

### 2. Rating System: OpenSkill (Weng-Lin model)

**Configuration:**
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Initial μ (mean) | 25.0 | Standard default |
| Initial σ (std dev) | 8.333 | High uncertainty for new players |
| β (performance variance) | 4.167 | σ/2, standard |
| τ (dynamics factor) | 0.083 | Allows rating drift over time |
| Convergence target | 20-30 games | Player reaches stable rating |

**MMR calculation:** `MMR = μ - 3σ` (conservative estimate, ranges 0-50)

**Why OpenSkill over alternatives:**
- Free and open-source (no TrueSkill patent issues)
- Handles 4v4 teams natively
- Uncertainty tracking (σ) handles new players and returning players
- Well-maintained libraries: Python, TypeScript, Rust

### 3. Rank Divisions

| Division | MMR Range | % of Players | Icon |
|----------|-----------|-------------|------|
| Bronze | 0 - 10 | 15% | 🥉 |
| Silver | 10 - 18 | 25% | 🥈 |
| Gold | 18 - 25 | 30% | 🥇 |
| Platinum | 25 - 32 | 18% | 💎 |
| Diamond | 32 - 38 | 8% | ♦️ |
| Master | 38 - 44 | 3% | 👑 |
| Grandmaster | 44+ | 1% | ⭐ |

**Promotion/Demotion:**
- Promote: reach division ceiling + win confirmation match
- Demote: fall 2 MMR below division floor (hysteresis prevents oscillation)
- Decay: -1 MMR per week of inactivity after 14 days (ranked only, min = division floor)

**Placement:**
- 10 placement matches with 3× σ adjustment speed
- First placement: median (Gold) ±2 divisions based on results
- Returning seasons: start 3 divisions below previous peak, 5 placement matches

### 4. Queue Algorithm

**Priority order:** Skill match → Ping quality → Queue time → Party balance

**Search window expansion:**

```
Time in Queue | MMR Window | Ping Limit | Notes
0-15s         | ±50 MMR    | <60ms      | Strict, ideal match
15-30s        | ±100 MMR   | <80ms      | Standard
30-60s        | ±200 MMR   | <100ms     | Relaxed skill
60-90s        | ±400 MMR   | <150ms     | Wide skill, relaxed ping
90-120s       | ±600 MMR   | <200ms     | Very wide
120s+         | Any        | <250ms     | Accept anything playable
```

**Party matching rules:**
- 4-stack vs 4-stack preferred (±30s extra wait)
- If no 4-stack available: 4-stack vs (duo + duo) or (trio + solo)
- Solo players: never matched against 4-stack in ranked
- Party skill spread limit (ranked): max 8 MMR difference between party members

### 5. Lobby Flow

```
[Queue] → [Match Found] → [Ready Check (30s)] → [Character Select (60s)]
                                    ↓ (timeout/decline)
                               [Re-queue others]

→ [Loading Screen] → [In-Game (10 min)] → [Post-Game (30s)] → [Queue/Menu]
                          ↓ (disconnect)
                     [Reconnect Window (120s)]
                          ↓ (timeout)
                     [Abandon Penalty]
```

**Ready check:** All 8 players must accept within 30s. If any decline, re-queue the 7.

**Dodge penalties (ranked):**
| Offense | Cooldown | MMR Penalty |
|---------|----------|-------------|
| 1st dodge | 5 minutes | -2 MMR |
| 2nd dodge (24h) | 30 minutes | -5 MMR |
| 3rd dodge (24h) | 2 hours | -10 MMR |
| 4th+ dodge (24h) | 24 hours | -15 MMR |

### 6. Anti-Smurf Measures

| Measure | Implementation |
|---------|---------------|
| New account acceleration | σ starts high (8.333), converges fast; first 10 games swing ±5 MMR |
| Win streak detection | 7+ wins: temporarily boost μ by 2× normal adjustment |
| Phone verification | Required for ranked queue (reduces throwaway accounts) |
| Party skill cap | Max 8 MMR spread in ranked parties |
| Hardware fingerprint | Flag multiple accounts on same hardware for review |

### 7. Match Quality KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Avg skill diff per match | <3 MMR (6% of range) | Mean |μ₁ - μ₂| across all match participants |
| Queue time (p50) | <30s | Median time from queue start to match found |
| Queue time (p95) | <120s | 95th percentile |
| Win rate convergence | 50% ±5% | Per player over 50+ games |
| Player-reported fairness | >70% "fair match" | Post-game survey sample |
| Rematch rate | <5% | Same opponents within 3 matches |

### 8. Population Scaling

| CCU Range | Queue Pool Size | Expected Quality |
|-----------|----------------|-----------------|
| <1,000 | Small | Wide skill matches, warn players |
| 1,000-5,000 | Medium | Good matches, occasional skill gaps |
| 5,000-50,000 | Large | Tight matching, fast queues |
| 50,000+ | Very large | Near-perfect matching, instant queues |

**Low-population fallbacks:**
- Merge casual and ranked queues during off-peak (midnight-6am)
- Expand region matching (NA + EU) if single-region pool is <200
- Show estimated queue time to set player expectations
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defines matchmaking quality as the measurable goal
- **ST-02 (Structured Sequential Instructions):** Seven-step process from requirements to validation
- **RT-02 (Multi-Dimensional Analysis):** Evaluates rating systems, queue algorithms, ranks, and anti-smurf independently
- **DS-03 (Tool and Methodology Suggestions):** Recommends specific rating algorithms with configuration parameters
- **OC-01 (Structured Output Format):** Tables, flow diagrams, and KPI matrices

## Related Prompts

- [Netcode Architecture](multiplayer_netcode_architecture.md) — Network layer that matchmaking feeds into
- [State Synchronization](multiplayer_state_sync.md) — Sync layer for matched players
- [Player Progression](../design/design_player_progression.md) — Progression interacts with competitive ranking
