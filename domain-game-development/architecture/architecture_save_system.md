---
title: "Game Save & Serialization System"
category: game-development/architecture
description: "Design save/load systems covering serialization formats, version migration, cloud sync, anti-cheat, and cross-platform compatibility"
techniques:
  - ST-01
  - ST-02
  - RT-05
  - DS-03
  - QA-02
difficulty: intermediate
tags:
  - architecture
  - save-system
  - serialization
  - cloud-save
  - versioning
  - persistence
updated: "2026-03-19"
related_prompts:
  - domain-game-development/architecture/architecture_scene_management.md
  - domain-game-development/architecture/architecture_state_machine_design.md
  - domain-game-development/multiplayer/multiplayer_netcode_architecture.md
---

# Game Save & Serialization System

**Objective:** Design comprehensive game save and serialization systems covering format selection, schema versioning with forward/backward migration, cloud save synchronization, anti-tamper measures, and cross-platform save compatibility.

## When to Use

- Use when designing persistence for a new game (player data, world state, settings)
- Use when adding cloud save support to an existing game
- Use when save corruption or version migration issues are occurring
- Don't use for real-time state replication (multiplayer sync) — use `multiplayer_state_sync.md` instead

## Instructions

1. **Inventory Saveable State**
   - Categorize all persistent data:
     - **Player state:** position, health, inventory, stats, progression, cosmetics
     - **World state:** NPC states, opened doors, defeated enemies, terrain changes
     - **Meta state:** settings, keybinds, accessibility options, tutorials completed
     - **Achievement/unlock state:** milestones, collectibles, completion percentages
   - Estimate total save size per category
   - Identify which data is critical (must never lose) vs recoverable (can rebuild)

2. **Choose Serialization Format**
   - Evaluate options for your needs:
     - **JSON:** Human-readable, easy debugging, larger size, slow parse — good for small games, settings
     - **Binary (custom):** Compact, fast, fragile to schema changes — good for performance-critical saves
     - **Protocol Buffers / FlatBuffers:** Schema-driven, versioned, compact — good for structured data with evolution
     - **SQLite:** Queryable, transactional, good for large world state — good for open-world games
     - **MessagePack / CBOR:** Binary JSON, compact, reasonable speed — good middle ground
   - Consider compression: LZ4 (fast) for frequent saves, zstd (smaller) for cloud upload

3. **Design Version Schema and Migration**
   - Assign a version number to the save format
   - Write migration functions: `migrate_v1_to_v2()`, `migrate_v2_to_v3()`, etc.
   - Chain migrations: loading v1 save in v5 game runs v1→v2→v3→v4→v5
   - Handle additive changes (new fields get defaults) vs breaking changes (restructured data)
   - Never delete fields without a migration step — mark deprecated, remove in next major version

4. **Implement Save/Load Flow**
   - **Auto-save triggers:** zone transitions, checkpoint reached, inventory change, timed interval
   - **Manual save:** save slots (3-5 minimum), slot metadata (screenshot, playtime, level)
   - **Quicksave/quickload:** single-slot fast save for PC games
   - **Save flow:** gather state → serialize → compress → write to temp file → rename (atomic write)
   - **Load flow:** read file → decompress → deserialize → validate → apply state
   - Use atomic writes (write-then-rename) to prevent corruption from crashes mid-save

5. **Design Cloud Sync Strategy**
   - Choose sync model: full upload/download vs differential sync
   - Handle conflicts: last-write-wins, highest-progress-wins, or user-choice prompt
   - Support offline play: queue syncs, merge on reconnect
   - Platform APIs: Steam Cloud, PlayStation Plus, Xbox Cloud, iCloud, Google Play Games
   - Set size limits per platform (Steam: 100MB default, mobile: smaller)

6. **Add Anti-Tamper and Validation**
   - For competitive/multiplayer: checksum or HMAC on save data, server-side validation
   - For single-player: light validation (catch corruption, not cheating — don't punish modders)
   - Validate on load: range checks, reference integrity, impossible state detection
   - Graceful corruption handling: load last known good backup, inform player

7. **CRITICAL: Verify Save System Integrity**
   - Test full roundtrip: save → quit → load → verify state matches
   - Test version migration chain from oldest to newest format
   - Test corruption recovery: truncated file, bit-flip, empty file
   - Test concurrent saves (auto-save during manual save)
   - Test platform storage limits and quota exceeded scenarios
   - Verify cloud sync conflict resolution produces correct results

**False-Positive Prevention (MUST follow):**

❌ **DON'T:**
- Don't over-secure single-player saves — players expect modding support
- Don't use human-readable JSON for large open-world saves (100MB+ world state)
- Don't skip atomic writes — crashes during save are common on consoles
- Don't assume cloud storage is infinite — check platform quotas
- Don't serialize engine objects directly (Unity GameObject, Unreal AActor) — serialize data, not objects

✅ **DO:**
- Use separate files for settings vs game progress (settings should survive save wipe)
- Include a save file header with version, timestamp, and checksum before the payload
- Plan for save corruption from day one — always have a backup slot
- Test with saves from every prior version of the game in your CI pipeline
- Consider save-file size for cloud sync costs on mobile platforms

## Expected Output

A save system design document including:

- Data inventory with size estimates
- Serialization format selection with rationale
- Schema version migration plan
- Save/load flow diagrams
- Cloud sync architecture
- Validation and anti-tamper strategy
- Platform-specific considerations

## Example Output

```markdown
## Save System Design — "Verdant Wilds" (Survival Crafting Game)

### 1. Data Inventory

| Category | Data | Est. Size | Criticality |
|----------|------|-----------|-------------|
| Player | Position, health, hunger, stats | 512 B | Critical |
| Inventory | Items, quantities, durability, enchantments | 8 KB | Critical |
| Equipment | Equipped items, cosmetic slots | 1 KB | Critical |
| Skills | Skill tree state, XP per skill | 2 KB | Critical |
| World chunks | Terrain modifications per chunk (16x16) | 50 KB/chunk | Recoverable |
| Structures | Player-built buildings, furniture placement | 20 KB | Critical |
| NPCs | NPC states, schedules, relationship values | 5 KB | Recoverable |
| Quests | Quest progress, flags, dialogue state | 3 KB | Critical |
| Settings | Graphics, audio, keybinds, accessibility | 2 KB | Separate file |
| **Total (200 explored chunks)** | | **~10 MB** | |

### 2. Serialization Format

**Decision: MessagePack with zstd compression**

| Format | Size (10MB raw) | Parse Time | Schema Evolution | Choice |
|--------|----------------|------------|------------------|--------|
| JSON | 10 MB | 180 ms | Easy | ❌ Too large |
| Binary (custom) | 4 MB | 15 ms | Fragile | ❌ Migration risk |
| MessagePack | 5 MB | 25 ms | Good | ✅ Selected |
| Protocol Buffers | 4.5 MB | 20 ms | Excellent | Overkill for this scope |

**With zstd compression:** 5 MB → 1.2 MB (saves: disk space, cloud bandwidth)

### 3. Save File Structure

```
[Header - 64 bytes]
├── Magic bytes: "VWLD" (4 bytes)
├── Format version: uint16 (2 bytes)
├── Save timestamp: uint64 (8 bytes)
├── Playtime seconds: uint32 (4 bytes)
├── Player level: uint16 (2 bytes)
├── Chunk count: uint16 (2 bytes)
├── Uncompressed size: uint32 (4 bytes)
├── CRC32 checksum: uint32 (4 bytes)
├── Reserved: (34 bytes)
[Compressed Payload]
├── Player data (MessagePack)
├── Inventory data (MessagePack)
├── World chunks (MessagePack, per-chunk)
├── Quest state (MessagePack)
└── NPC state (MessagePack)
```

### 4. Version Migration

**Current version: 3**

```python
MIGRATIONS = {
    1: migrate_v1_to_v2,  # Added hunger/thirst system
    2: migrate_v2_to_v3,  # Restructured inventory (slot-based → container-based)
}

def load_save(data):
    header = parse_header(data)
    payload = decompress(data[64:])
    save = msgpack.unpack(payload)

    # Chain migrations
    version = header.format_version
    while version < CURRENT_VERSION:
        save = MIGRATIONSversion
        version += 1

    validate(save)
    return save

def migrate_v1_to_v2(save):
    """v1→v2: Added hunger/thirst (Jan 2026 update)"""
    save["player"]["hunger"] = 100.0  # Default full
    save["player"]["thirst"] = 100.0
    save["player"]["temperature"] = 20.0  # Celsius, comfortable
    return save

def migrate_v2_to_v3(save):
    """v2→v3: Inventory restructure (Mar 2026 update)"""
    old_items = save["inventory"]["items"]  # Was flat list
    save["inventory"] = {
        "backpack": old_items[:30],       # First 30 items → backpack
        "hotbar": old_items[30:38],       # Next 8 → hotbar
        "overflow": old_items[38:],       # Remainder → overflow chest
        "containers": {}                  # New: named storage containers
    }
    return save
```

### 5. Save/Load Flow

**Save Flow:**
```
1. Gather state from all systems
2. Build save dictionary
3. Set header.format_version = CURRENT_VERSION
4. Set header.timestamp = now()
5. Serialize payload with MessagePack
6. Compress with zstd (level 3)
7. Calculate CRC32 of compressed payload
8. Write to temp file: save_slot_N.tmp
9. If write successful:
   a. Rename current save → save_slot_N.bak (backup)
   b. Rename temp → save_slot_N.sav (atomic swap)
10. Queue cloud sync upload
```

**Auto-Save Triggers:**
- Every 5 minutes of active play
- On zone/chunk transition
- Before boss encounters
- On manual inventory management (crafting, trading)
- On game minimize/suspend (mobile/console)

**Save Slots:**
- 5 manual slots + 1 auto-save slot + 1 quicksave slot
- Slot metadata stored separately for fast menu display
- Metadata includes: screenshot thumbnail (64x36), playtime, level, zone name

### 6. Cloud Sync

**Platform Integration:**
| Platform | API | Max Size | Sync Model |
|----------|-----|----------|------------|
| Steam | Steam Cloud | 100 MB | Full file upload |
| PlayStation | PS Plus Cloud | 1 GB | Full file upload |
| Xbox | Xbox Cloud | 256 MB | Full file upload |
| Nintendo Switch | NSO Cloud | 32 MB per title | Full file upload |
| Mobile (iOS) | iCloud | 50 MB per app | Key-value + file |

**Conflict Resolution: Highest-Progress-Wins**
```python
def resolve_conflict(local_save, cloud_save):
    local_score = progress_score(local_save)
    cloud_score = progress_score(cloud_save)

    if abs(local_score - cloud_score) < 0.05:
        # Very close — ask user
        return prompt_user_choice(local_save, cloud_save)
    elif local_score > cloud_score:
        return local_save  # Local is ahead
    else:
        return cloud_save  # Cloud is ahead

def progress_score(save):
    """Weighted progress metric"""
    return (
        save.player.level * 10 +
        save.playtime_hours * 2 +
        len(save.quests_completed) * 5 +
        save.world.chunks_explored * 0.5
    )
```

### 7. Validation & Anti-Tamper

**Single-player approach (modder-friendly):**
- CRC32 checksum detects accidental corruption, not intentional edits
- Range validation on load (health 0-999, position within world bounds)
- Reference integrity (equipped items exist in inventory)
- If validation fails: load backup, show warning "Save may be corrupted"

**No encryption** — single-player, modding community is an asset

### 8. Platform-Specific Notes

| Platform | Consideration |
|----------|--------------|
| Steam Deck | Verify save works across Proton/native Linux |
| Nintendo Switch | 32 MB limit — chunk saves may need pruning distant chunks |
| Mobile | Save on every app suspend (OS may kill process) |
| Console | Respect platform suspend/resume save requirements |
| Cross-platform | Use platform-agnostic serialization (no endianness issues) |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Scopes the full save system design challenge
- **ST-02 (Structured Sequential Instructions):** Seven-step process from data inventory through verification
- **RT-05 (Evidence-Based Reasoning):** Requires size estimates, format benchmarks, and platform research
- **DS-03 (Tool and Methodology Suggestions):** Recommends specific formats, compression algorithms, and migration patterns
- **QA-02 (Validation and Verification):** CRITICAL step with roundtrip testing, corruption, and migration chain verification

## Related Prompts

- [Scene & Level Management](architecture_scene_management.md) — Scene lifecycle affects what to save/load
- [Game State Machine Design](architecture_state_machine_design.md) — State machines define saveable game states
- [Netcode Architecture](../multiplayer/multiplayer_netcode_architecture.md) — Server-authoritative saves for multiplayer
