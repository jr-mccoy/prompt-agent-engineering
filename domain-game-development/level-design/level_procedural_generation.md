---
title: "Procedural Content Generation Design"
category: game-development/level-design
description: "Design procedural generation systems with algorithm selection (WFC, BSP, Perlin, L-systems), constraint specification, and quality validation"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
  - OC-01
difficulty: advanced
tags:
  - procedural-generation
  - pcg
  - wave-function-collapse
  - bsp
  - level-design
  - algorithms
  - roguelike
updated: "2026-03-19"
related_prompts:
  - domain-game-development/level-design/level_design_review.md
  - domain-game-development/design/design_player_experience.md
  - domain-software-engineering/algorithms/algorithm_design.md
---

# Procedural Content Generation Design

**Objective:** Design procedural content generation systems covering algorithm selection (Wave Function Collapse, BSP trees, Perlin/simplex noise, L-systems, grammar-based generation), constraint specification, seed management and reproducibility, quality validation metrics, and player-experience guardrails.

**When to Use:**
- Building a roguelike, roguelite, or any game with replayable procedural levels
- Generating terrain, dungeons, cities, vegetation, quests, or loot tables procedurally
- Designing a system that must produce thousands of valid, fun levels without manual authoring
- Supplementing hand-crafted content with procedural variation (hybrid approach)
- Don't use when: Your game has a fixed, authored level sequence with no replay variance — hand-craft those levels instead

**Instructions:**

1. **Define Generation Scope**
   - Identify what content is procedurally generated vs hand-crafted:
     - Dungeon/room layouts, terrain heightmaps, city street grids
     - Item/loot placement, enemy encounters, NPC distribution
     - Quest chains, dialogue trees, narrative events
     - Vegetation, rocks, props, decorative details
   - Determine generation frequency: once per run, per level, per chunk, real-time streaming
   - Define output format: tilemap grid, mesh vertices, graph of connected nodes, placement coordinates

2. **Select Algorithm Based on Content Type**
   - Match content requirements to algorithm strengths:

   | Content Type          | Primary Algorithm          | Why                                          |
   |-----------------------|----------------------------|----------------------------------------------|
   | Room-corridor dungeons| BSP Tree Partitioning      | Guarantees connected rectangular rooms        |
   | Tile-based levels     | Wave Function Collapse     | Respects adjacency rules, produces coherent patterns |
   | Terrain heightmaps    | Perlin/Simplex Noise       | Smooth, natural-looking continuous surfaces   |
   | Cave systems          | Cellular Automata          | Organic, irregular shapes from simple rules   |
   | Vegetation/trees      | L-Systems                  | Recursive branching structures                |
   | City layouts          | Voronoi + Road Grammar     | District boundaries with street networks      |
   | Quest generation      | Grammar-Based (CFG)        | Structured narrative with variable details    |
   | Loot/item rolls       | Weighted Random + Pity     | Statistical fairness with progression feel    |

   - Consider hybrid approaches: BSP for room layout + WFC for room interior detail + Perlin for height variation within rooms

3. **Specify Constraints**
   - **Connectivity**: All rooms must be reachable from the entrance (validate with flood fill / BFS)
   - **Pacing**: Alternate combat rooms with rest rooms, enforce minimum distance between boss encounters
   - **Difficulty curve**: Map room difficulty to distance from start (linear, stepped, or wave pattern)
   - **Mandatory features**: Every floor must contain exactly 1 shop, 1 boss room, 1 treasure room, 1 exit
   - **Spatial constraints**: Minimum room size 5x5 tiles, maximum 15x15, corridor width exactly 3 tiles
   - **Aesthetic rules**: No two identical rooms adjacent, biome transitions must use transition tiles

4. **Implement Seed System**
   - Deterministic generation: same seed + same parameters = identical output across all platforms
   - Use a single PRNG (e.g., PCG, xoshiro256) seeded once, consumed in fixed order
   - Shareable seeds: players can share 8-character alphanumeric codes
   - Partial re-generation: support re-rolling a single room/floor without changing the rest (sub-seeds)
   - Daily/weekly challenge seeds: server-distributed seeds for leaderboard runs
   - Store seed in save file for crash recovery and replay

5. **Design Quality Validation**
   - **Playability check**: Flood fill from spawn to exit — reject if not connected
   - **Difficulty scoring**: Sum enemy threat values per room, compare to expected curve (reject outliers >2 standard deviations)
   - **Aesthetic metrics**: Measure room size variance, corridor length distribution, dead-end ratio
   - **Completion time estimate**: Simulate pathfinding from start to exit, reject if estimated time is outside target range
   - **Reject and re-roll**: Set maximum re-roll attempts (e.g., 100) before falling back to a known-good template

6. **Player-Experience Guardrails**
   - Minimum 2 rooms before first combat encounter (safe exploration zone)
   - Guaranteed health pickup within 3 rooms of spawn
   - Boss room always has a save point / rest area in the adjacent room
   - Maximum 5 rooms between shop opportunities
   - No dead-end longer than 2 rooms (prevents excessive backtracking)
   - At least 1 secret room per floor (hidden but discoverable)
   - Enemy density caps per room size (max 1 enemy per 4 tiles of floor space)

7. **CRITICAL: Verify the generation system before shipping.**
   - **Completability**: Run 10,000+ seeds through automated playability verification — 0% soft-lock rate required
   - **No unreachable areas**: Flood-fill validation on every generated level confirms all rooms, items, and exits are accessible
   - **Seed reproducibility**: Generate the same seed on PC, console, and mobile — diff the outputs, they must be identical
   - **Generation time**: Measure p99 generation time — must be under 2 seconds for level load, under 16ms for real-time chunk generation
   - **Edge cases**: Test seeds 0, 1, MAX_UINT64, and seeds that previously caused failures

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT generate purely random content without constraints — randomness without rules produces unplayable, unfun levels
- ❌ Do NOT assume one algorithm fits all content types — BSP cannot make organic caves, cellular automata cannot make structured dungeons
- ❌ Do NOT skip validation because "it usually works" — rare failures destroy player trust in procedural games
- ❌ Do NOT use floating-point arithmetic in generation if cross-platform seed reproducibility is required (FP rounding differs across CPUs)
- ✅ DO test with thousands of seeds to catch edge cases (seed 0, seed MAX, adversarial seeds)
- ✅ DO include manual override / curation hooks so designers can pin specific rooms, encounters, or loot into the procedural flow
- ✅ DO provide a debug visualization mode that shows generation steps, constraint satisfaction, and rejected attempts
- ✅ DO plan for live-ops seed curation (daily challenge seeds verified before distribution)

**Expected Output:** A procedural content generation design document specifying algorithm selection rationale, constraint rules, seed system architecture, quality validation pipeline, and player-experience guardrails — verified with automated testing across thousands of seeds.

**Example Output:**

```markdown
# Procedural Dungeon Generation System — "Crypts of Malara"
## Roguelike Dungeon Crawler | 2D Top-Down Tilemap

---

## 1. Generation Overview

| Parameter              | Value                                    |
|------------------------|------------------------------------------|
| Content Generated      | Dungeon floor layouts, room interiors,   |
|                        | enemy placement, loot distribution       |
| Algorithm Stack        | BSP (layout) + WFC (interiors) + Weighted Random (loot) |
| Grid Size per Floor    | 80x80 tiles                              |
| Tile Size              | 16x16 pixels                             |
| Floors per Run         | 5 standard + 1 boss floor                |
| Target Gen Time        | <500ms per floor (PC), <1.2s (Switch)    |
| Seed Format            | 8-char alphanumeric (32-bit mapped)      |
| PRNG Algorithm         | PCG-XSH-RR (32-bit output, 64-bit state)|

---

## 2. Algorithm Pipeline

```
Seed (32-bit)
    │
    ▼
┌─────────────────────────────────┐
│ STAGE 1: BSP Layout            │
│ Split 80x80 grid recursively   │
│ Min partition: 8x8             │
│ Max depth: 6 splits            │
│ Room in each leaf: 5x5 to 12x12│
│ Output: Room rects + corridors │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ STAGE 2: Room Classification   │
│ Assign room types by rules:    │
│  - Farthest from start → Boss  │
│  - Random leaf → Shop (1/floor)│
│  - Dead-ends → Treasure        │
│  - Remaining → Combat/Rest     │
│ Combat:Rest ratio = 3:1        │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ STAGE 3: WFC Room Interiors    │
│ Tile palette: 24 tile types    │
│ Adjacency rules: 48 rules     │
│ Fill each room rect with WFC   │
│ Add doors at corridor junctions│
│ Backtrack limit: 50 per room   │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ STAGE 4: Entity Placement      │
│ Enemies: weighted by room type │
│ Loot: drop table per room tier │
│ Props: decorative fill (WFC)   │
│ Traps: 1 per 3 combat rooms   │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ STAGE 5: Validation            │
│ Flood fill connectivity ✓      │
│ Difficulty curve check ✓       │
│ Guardrail compliance ✓        │
│ If FAIL → re-roll (max 100)   │
└─────────────────────────────────┘
```

---

## 3. BSP Partitioning Rules

```
function generateBSP(rect, depth, rng):
    if depth >= MAX_DEPTH or rect.area < MIN_PARTITION:
        return Leaf(rect)

    # Choose split direction
    if rect.width / rect.height > 1.25:
        direction = VERTICAL
    elif rect.height / rect.width > 1.25:
        direction = HORIZONTAL
    else:
        direction = rng.choose([VERTICAL, HORIZONTAL])

    # Split position: 40%-60% of dimension (avoid tiny rooms)
    splitRatio = rng.range(0.40, 0.60)
    splitPos = rect.dimension(direction) * splitRatio

    left  = rect.split(direction, splitPos, LEFT)
    right = rect.split(direction, splitPos, RIGHT)

    return Node(
        left:  generateBSP(left,  depth + 1, rng),
        right: generateBSP(right, depth + 1, rng)
    )

Parameters:
  MAX_DEPTH        = 6
  MIN_PARTITION    = 8x8 tiles
  ROOM_MARGIN      = 1 tile (wall thickness)
  MIN_ROOM_SIZE    = 5x5 tiles
  MAX_ROOM_SIZE    = 12x12 tiles
  CORRIDOR_WIDTH   = 3 tiles
```

### Room Count Distribution (10,000 seed sample)

```
Room Count │ Frequency
───────────┼──────────────────────────────
     8     │ ██░░░░░░░░░░░░░░░░░░  4.2%
     9     │ ████████░░░░░░░░░░░░ 12.1%
    10     │ ████████████░░░░░░░░ 22.7%
    11     │ ████████████████░░░░ 28.3%   ← median
    12     │ ██████████████░░░░░░ 20.8%
    13     │ ██████░░░░░░░░░░░░░░  9.1%
    14     │ ██░░░░░░░░░░░░░░░░░░  2.8%

  Mean: 10.9 rooms | Std Dev: 1.4 | Min: 8 | Max: 14
```

---

## 4. Constraint Rules

### Room Type Assignment

| Room Type   | Count per Floor | Placement Rule                          |
|-------------|----------------|-----------------------------------------|
| Spawn       | 1              | Random leaf, biased toward center       |
| Boss        | 1              | Farthest room from Spawn (graph dist)   |
| Shop        | 1              | 3-5 rooms from Spawn (mid-run)          |
| Treasure    | 1-2            | Dead-end rooms preferred                |
| Rest        | 2-3            | Adjacent to Boss, every 4th room        |
| Combat      | 4-8            | All remaining rooms                     |
| Secret      | 1              | Hidden wall, connects two adjacent rooms|

### Difficulty Curve

```
Difficulty Score by Room Distance from Spawn:

Score │
  10  │                                          ████
      │                                    ██████
   8  │                              ██████
      │                        ██████
   6  │                  ██████
      │            ██████
   4  │      ██████
      │ █████
   2  │██
      │
   0  └──────────────────────────────────────────────
      0    1    2    3    4    5    6    7    8    9
                    Rooms from Spawn

Formula: difficulty = floor(1.5 + distance * 0.85)
Variance: ±1 per room (adds unpredictability)
```

### Enemy Threat Budget per Room

| Room Difficulty | Threat Budget | Example Composition           |
|----------------|--------------|-------------------------------|
| 1-2 (easy)     | 3-5 pts      | 3 Slimes (1pt each)           |
| 3-4 (medium)   | 6-10 pts     | 2 Skeletons (3pt) + 1 Bat (1pt) |
| 5-6 (hard)     | 11-16 pts    | 1 Knight (8pt) + 2 Archers (4pt) |
| 7-8 (very hard)| 17-24 pts    | 1 Mini-boss (15pt) + 3 Slimes |
| 9-10 (boss)    | 30-50 pts    | 1 Floor Boss (30-50pt)        |

---

## 5. Seed System

```
Seed Architecture:
  Master Seed (32-bit from player input or daily server)
      │
      ├── Floor 1 Sub-Seed: hash(master, "floor", 1)
      │   ├── Layout Sub-Seed: hash(floor_seed, "layout")
      │   ├── Interior Sub-Seed: hash(floor_seed, "interior")
      │   ├── Enemy Sub-Seed: hash(floor_seed, "enemies")
      │   └── Loot Sub-Seed: hash(floor_seed, "loot")
      │
      ├── Floor 2 Sub-Seed: hash(master, "floor", 2)
      │   └── ...
      │
      └── Floor N Sub-Seed: hash(master, "floor", N)

  Hash function: xxHash32 (fast, good distribution)
  Benefit: re-rolling loot doesn't change layout
```

### Seed Encoding

```
Seed Display:  "KRMX-4A7P"  (human-friendly)
Seed Internal: 0xA3F7B201   (32-bit unsigned)

Encoding: Base-32 Crockford (excludes I, L, O, U to avoid confusion)
Alphabet: 0123456789ABCDEFGHJKMNPQRSTVWXYZ

Daily Challenge Seed: UTC date → SHA-256 → truncate to 32 bits
  2026-03-19 → 0x7C2E1A9F → "HM2E-1KTF"
```

---

## 6. Quality Validation Pipeline

```
Validation Steps (run on every generated floor):

Step 1: CONNECTIVITY CHECK
  Algorithm: Flood fill from spawn tile
  Pass condition: All room floor tiles reached
  Failure action: Re-roll layout (Stage 1)
  Time cost: <1ms

Step 2: CRITICAL PATH LENGTH
  Algorithm: BFS shortest path, spawn → boss
  Pass condition: 4 ≤ path_length ≤ 9 rooms
  Failure action: Re-classify rooms (Stage 2)
  Time cost: <1ms

Step 3: DIFFICULTY CURVE VALIDATION
  Algorithm: Score each room, fit to expected curve
  Pass condition: R² > 0.7 against target curve
  Failure action: Swap room types to improve fit
  Time cost: <1ms

Step 4: GUARDRAIL COMPLIANCE
  Checks:
    ✓ Health pickup within 3 rooms of spawn
    ✓ No dead-end longer than 2 rooms
    ✓ Shop reachable without boss fight
    ✓ Boss room has adjacent rest room
    ✓ Enemy density ≤ 1 per 4 floor tiles
  Failure action: Adjust entity placement (Stage 4)
  Time cost: <1ms

Step 5: WFC COMPLETENESS
  Check: No unresolved tiles (contradiction)
  Failure action: Re-run WFC with different collapse order
  Max retries: 50 per room
  Time cost: 10-50ms per room
```

### Automated Test Results (10,000 seeds)

| Metric                        | Result        | Threshold    | Status |
|-------------------------------|---------------|-------------|--------|
| Connectivity pass rate        | 100%          | 100%        | PASS   |
| Avg re-rolls before valid     | 1.3           | <10         | PASS   |
| Max re-rolls observed         | 12            | <100        | PASS   |
| Mean generation time (PC)     | 180ms         | <500ms      | PASS   |
| p99 generation time (PC)      | 420ms         | <1000ms     | PASS   |
| Mean generation time (Switch) | 680ms         | <1200ms     | PASS   |
| Cross-platform seed match     | 100%          | 100%        | PASS   |
| Soft-lock rate                | 0.00%         | 0.00%       | PASS   |
| Difficulty R² (mean)          | 0.82          | >0.70       | PASS   |
| Dead-end violation rate       | 0.00%         | 0.00%       | PASS   |

---

## 7. Designer Override Hooks

```
Overrides available in level editor:

  PIN_ROOM(floor, index, template_id)
    → Forces a specific hand-crafted room at position

  PIN_BOSS(floor, boss_id)
    → Overrides boss selection for a specific floor

  FORCE_LAYOUT(floor, layout_template)
    → Uses a hand-crafted layout, fills with procedural content

  BLACKLIST_TILE(tile_id)
    → Prevents WFC from using specific tiles on this floor

  SET_DIFFICULTY_OVERRIDE(floor, min, max)
    → Clamps difficulty range for tutorial/story floors

  INJECT_EVENT(floor, room_type, event_id)
    → Places a scripted narrative event in a procedural room
```
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Defines precise scope: algorithms, constraints, seeds, validation, guardrails
- ST-02 (Structured Sequential Instructions) - Seven ordered steps from scope definition through verification
- RT-02 (Multi-Dimensional Analysis Framework) - Each algorithm evaluated across content fit, performance, and constraints
- DS-03 (Tool and Methodology Suggestions) - Recommends specific algorithms per content type with rationale
- OC-01 (Output Structure Specification) - Defines expected deliverable with pipeline diagrams, constraint tables, and validation results

**Related Prompts:**
- `domain-game-development/level-design/level_design_review.md` - Review hand-crafted levels that sit alongside procedural content
- `domain-game-development/design/design_player_experience.md` - Player experience pacing that constrains procedural generation
- `domain-software-engineering/algorithms/algorithm_design.md` - General algorithm design methodology
