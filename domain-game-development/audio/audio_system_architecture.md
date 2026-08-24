---
title: "Game Audio System Architecture"
category: game-development/audio
description: "Design game audio system architecture covering bus hierarchy, spatial audio, middleware integration (FMOD/Wwise), memory management, and streaming"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
  - OC-01
difficulty: intermediate
tags:
  - audio
  - fmod
  - wwise
  - spatial-audio
  - sound-design
  - architecture
  - middleware
updated: "2026-03-19"
related_prompts:
  - domain-game-development/performance/performance_profiling_optimization.md
  - domain-game-development/architecture/architecture_engine_selection.md
  - domain-game-development/design/design_player_experience.md
---

# Game Audio System Architecture

**Objective:** Design a game audio system architecture covering audio bus hierarchy and mixing, spatial audio configuration (3D sound, HRTF, occlusion), middleware integration (FMOD Studio, Wwise, or native engine audio), memory budgeting, streaming vs preloaded assets, and priority/voice management.

**When to Use:**
- Starting a new game project and need to plan the audio pipeline from scratch
- Migrating from native engine audio to middleware (FMOD, Wwise)
- Diagnosing audio issues (voice stealing, memory spikes, streaming pops)
- Scaling audio from prototype to production quality
- Don't use when: You only need a single sound effect or background track (just use the engine's built-in audio player)

**Instructions:**

1. **Define Audio Requirements**
   - Determine the number of simultaneous sounds your game needs (typical ranges: mobile 16-32, console 64-128, PC 128-256)
   - Identify the 3D vs 2D audio ratio (e.g., 70% 3D for action games, 20% 3D for puzzle games)
   - Count music layers needed for adaptive/interactive music (stems, transitions, stingers)
   - Set voice count target per platform (hardware limits, CPU budget for mixing)

2. **Design Bus Hierarchy**
   - Create the master bus structure:
     - Master → Music, SFX, UI, Voice, Ambient
     - Sub-buses for granular control: SFX → Combat, Footsteps, Environment, Physics
     - Music → BGM, Stingers, Cinematic
     - Voice → Dialogue, Barks, Narration
   - Define per-bus properties: volume, compression, sidechain ducking (music ducks under dialogue)
   - Plan snapshot/state system for game states (pause, underwater, interior, cutscene, death)

3. **Configure Spatial Audio**
   - Choose distance attenuation model (linear, logarithmic, custom curve) per sound category
   - Define min/max distance ranges (footsteps: 1-15m, explosions: 5-100m, ambient: 10-200m)
   - Configure occlusion and obstruction (raycast-based wall detection, low-pass filter per material)
   - Set up reverb zones (interior rooms, caves, open fields, underwater) with blend transitions
   - Evaluate HRTF for headphone users (binaural rendering, platform support)

4. **Choose Middleware vs Native**
   - **FMOD Studio**: Best for event-based design, indie-to-AA, strong Unity/Unreal integration, free under $200K revenue
   - **Wwise**: Best for AAA pipelines, spatial audio suite, SoundSeed procedural audio, steeper learning curve
   - **Native engine audio**: Sufficient for simple needs (<50 unique sounds), no licensing, limited tooling
   - Evaluate: team expertise, budget, sound designer workflow needs, platform targets

5. **Memory Budget and Asset Strategy**
   - Categorize assets by loading strategy:
     - **Preloaded (always in memory)**: UI sounds, player footsteps, weapon primary fire (<20MB typical)
     - **Streamed from disk**: Music tracks, ambient beds, long dialogue (saves RAM, needs I/O bandwidth)
     - **On-demand loaded**: Uncommon SFX, level-specific sounds (loaded at level start, freed on exit)
   - Choose compression formats per platform:
     - PC: Vorbis (music/ambient), ADPCM (short SFX)
     - Console: Platform-specific HW decoders (Opus on Switch, ATRAC on PlayStation)
     - Mobile: AAC or Vorbis (balance quality vs battery)
   - Set memory budget: mobile 15-30MB, console 50-150MB, PC 100-300MB

6. **Voice Management and Priority System**
   - Assign priority tiers: Critical (player weapon, dialogue) > High (nearby combat) > Medium (environment) > Low (distant ambient)
   - Define voice stealing policy: steal lowest-priority, oldest, quietest, or farthest voice
   - Configure virtual voices (voices that track position but don't render audio until close enough)
   - Set per-category voice limits (max 4 simultaneous footstep sounds, max 8 gunshots, max 1 music track)

7. **CRITICAL: Verify the architecture before finalizing.**
   - **Voice count validation**: Confirm total voice count does not exceed platform hardware limits (PS5: 512, Switch: 24-48 software mixed, mobile: 16-32)
   - **Bus routing completeness**: Verify every game state has correct bus behavior (pause mutes SFX but not UI, underwater applies low-pass to all except UI, cutscene ducks gameplay audio)
   - **Streaming integrity**: Test that streaming assets don't cause audible pops, clicks, or gaps during level transitions or rapid camera movement
   - **Memory ceiling**: Profile peak memory usage across worst-case scenarios (all buses active, maximum concurrent sounds)

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT require middleware (FMOD/Wwise) for simple games with fewer than 50 sound assets — native engine audio is sufficient
- ❌ Do NOT assume all audio needs 3D spatialization — UI sounds, music, and narration are typically 2D
- ❌ Do NOT set voice limits based on theoretical maximums — profile on actual target hardware
- ❌ Do NOT design reverb zones without considering CPU cost — convolution reverb is expensive on mobile
- ✅ DO plan for platform-specific audio APIs (Core Audio on iOS, AAudio/Oboe on Android, XAudio2 on Xbox)
- ✅ DO test on target hardware speakers AND headphones — spatialization behaves differently
- ✅ DO budget for audio thread CPU time (typically 5-15% of a core)
- ✅ DO implement fallback behavior when voice limit is reached (graceful degradation, not silence)

**Expected Output:** A complete audio system architecture document specifying bus hierarchy, spatial audio configuration, middleware integration plan, memory budget breakdown, streaming strategy, and voice management rules — all validated against platform constraints.

**Example Output:**

```markdown
# Audio System Architecture — "Ironhold: Siege of Shadows"
## Action-Adventure Game | PC / PS5 / Xbox Series X

---

## 1. Audio Requirements Summary

| Parameter               | Value                          |
|-------------------------|--------------------------------|
| Target Platforms        | PC, PS5, Xbox Series X         |
| Max Simultaneous Voices | 128 (PC/Console)               |
| 3D / 2D Ratio           | 75% / 25%                      |
| Music System            | Adaptive (4 stems + stingers)  |
| Dialogue System         | Voiced protagonist + NPCs      |
| Middleware              | FMOD Studio 2.02               |
| Total Audio Assets      | ~2,400 events                  |
| Memory Budget           | 120MB (PC), 80MB (Console)     |

---

## 2. Bus Hierarchy

```
Master Bus [0dB, Limiter -1dBFS]
├── Music Bus [-6dB, Compressor 3:1]
│   ├── BGM (adaptive stems)
│   │   ├── Stem_Percussion
│   │   ├── Stem_Strings
│   │   ├── Stem_Brass
│   │   └── Stem_Ambient_Pad
│   ├── Stingers (combat hits, discoveries)
│   └── Cinematic (pre-rendered cutscene audio)
│
├── SFX Bus [0dB]
│   ├── Combat
│   │   ├── Player_Weapons
│   │   ├── Enemy_Weapons
│   │   ├── Impacts_Hits
│   │   └── Abilities_Magic
│   ├── Footsteps
│   │   ├── Player_Footsteps (surface-aware)
│   │   └── NPC_Footsteps
│   ├── Environment
│   │   ├── Destructibles
│   │   ├── Doors_Mechanisms
│   │   └── Physics_Objects
│   └── Foley
│       ├── Cloth_Armor
│       └── Equipment_Jingle
│
├── Voice Bus [-3dB, Sidechain → Music Duck]
│   ├── Dialogue (story conversations)
│   ├── Barks (combat callouts, grunts)
│   └── Narration (tutorial, lore)
│
├── Ambient Bus [-6dB]
│   ├── Weather (rain, wind, thunder)
│   ├── Nature (birds, insects, water)
│   └── Interior (torches, machinery, drips)
│
└── UI Bus [0dB, Bypass All Effects]
    ├── Menu_Navigation
    ├── Notifications
    └── HUD_Feedback
```

### Sidechain Ducking Rules

| Trigger          | Target Bus   | Duck Amount | Attack | Release |
|------------------|-------------|-------------|--------|---------|
| Dialogue active  | Music        | -12dB       | 100ms  | 500ms   |
| Dialogue active  | Ambient      | -6dB        | 100ms  | 300ms   |
| Cutscene active  | SFX          | -18dB       | 50ms   | 200ms   |
| Pause menu open  | SFX, Ambient | -∞ (mute)   | 0ms    | 100ms   |
| Pause menu open  | Music        | -6dB        | 200ms  | 500ms   |

---

## 3. Spatial Audio Configuration

### Distance Attenuation Curves

| Sound Category    | Model        | Min Dist | Max Dist | Rolloff     |
|-------------------|-------------|----------|----------|-------------|
| Player Weapon     | Logarithmic | 1m       | 60m      | 2.0x        |
| Enemy Weapon      | Logarithmic | 1m       | 45m      | 2.5x        |
| Footsteps         | Linear      | 0.5m     | 15m      | 1.0x        |
| Explosions        | Logarithmic | 5m       | 120m     | 1.5x        |
| NPC Dialogue      | Custom      | 0m       | 12m      | sharp cutoff|
| Ambient Emitters  | Linear      | 5m       | 80m      | 1.0x        |
| UI / Music        | N/A (2D)    | —        | —        | —           |

### Occlusion System

```
Architecture:
  - 3 raycasts per occluded source (direct + 2 diffraction paths)
  - Update frequency: every 4 frames (~66ms at 60fps)
  - Material-based low-pass filter coefficients:

  Material         | LP Cutoff  | Volume Atten
  -----------------+------------+-------------
  Thin Wood        | 2000 Hz    | -4 dB
  Thick Stone      | 600 Hz     | -12 dB
  Metal Door       | 800 Hz     | -10 dB
  Glass            | 3500 Hz    | -3 dB
  Heavy Curtain    | 1200 Hz    | -6 dB
```

### Reverb Zones

```
Zone Configuration:
  ┌─────────────────────────────────────────┐
  │ OUTDOOR (Default)                        │
  │  Reverb: Light plate, 0.8s decay        │
  │  Pre-delay: 20ms                         │
  │                                          │
  │  ┌──────────────────┐  ┌────────────┐   │
  │  │ CAVE             │  │ CASTLE     │   │
  │  │ Reverb: Large    │  │ HALL       │   │
  │  │ hall, 3.2s decay │  │ 2.1s decay │   │
  │  │ Pre-delay: 40ms  │  │ Pre: 30ms  │   │
  │  │ HF Damping: 0.6  │  │ HF: 0.4   │   │
  │  └──────────────────┘  └────────────┘   │
  │                                          │
  │  ┌──────────────────────────────────┐   │
  │  │ UNDERWATER                        │   │
  │  │ LP Filter: 400Hz on all buses     │   │
  │  │ Reverb: 4.5s decay, heavy mud     │   │
  │  │ Pitch shift: -2 semitones         │   │
  │  │ UI bus: BYPASS (stays clear)      │   │
  │  └──────────────────────────────────┘   │
  └─────────────────────────────────────────┘

  Blend distance between zones: 3 meters (crossfade)
```

---

## 4. FMOD Studio Integration

### Event Naming Convention

```
event:/Music/Exploration/Forest_Day
event:/Music/Combat/Boss_Phase1
event:/SFX/Weapons/Sword_Swing_Light
event:/SFX/Weapons/Sword_Impact_{SurfaceType}
event:/SFX/Footsteps/{Surface}_{ArmorWeight}
event:/Voice/Dialogue/{CharacterID}/{LineID}
event:/Ambient/Weather/Rain_{Intensity}
event:/UI/Menu/Button_Hover
```

### Parameter Mapping

| FMOD Parameter     | Game Source              | Range    | Usage                      |
|--------------------|--------------------------|----------|----------------------------|
| MusicIntensity     | Combat threat level      | 0.0–1.0  | Cross-fade music stems     |
| SurfaceType        | Raycast material tag     | 0–8 enum | Footstep/impact variation  |
| Health             | Player HP percentage     | 0.0–1.0  | Heartbeat intensity        |
| TimeOfDay          | World clock normalized   | 0.0–1.0  | Ambient bird/insect mix    |
| InteriorExterior   | Zone trigger             | 0.0–1.0  | Reverb snapshot blend      |
| WindSpeed           | Weather system value     | 0.0–1.0  | Wind howl volume/pitch     |

### Adaptive Music State Machine

```
                    ┌─────────────┐
        ┌──────────→│  EXPLORATION │←──────────┐
        │           └──────┬──────┘            │
        │                  │ enemy detected     │
        │ (8-bar fade)     ▼                   │ (4-bar fade)
        │           ┌─────────────┐            │
        │           │   TENSION   │            │
        │           └──────┬──────┘            │
        │                  │ combat starts      │
        │                  ▼                   │
        │           ┌─────────────┐            │
        └───────────│   COMBAT    │────────────┘
         no enemies └──────┬──────┘  enemies dead
                           │ boss HP < 50%
                           ▼
                    ┌─────────────┐
                    │ BOSS_PHASE2 │
                    └─────────────┘

  Transition rules:
    - Quantize to next beat (120 BPM = 500ms grid)
    - Stinger on transition: "combat_start_hit.wav"
    - Stems added progressively: Pad → Strings → Percussion → Brass
```

---

## 5. Memory Budget

### Asset Allocation (PC Target: 120MB)

| Category         | Count  | Avg Size | Compression | Loaded   | Budget  |
|------------------|--------|----------|-------------|----------|---------|
| UI Sounds        | 45     | 12KB     | ADPCM       | Preload  | 0.5MB   |
| Player SFX       | 120    | 35KB     | ADPCM       | Preload  | 4.2MB   |
| Weapon SFX       | 200    | 50KB     | ADPCM       | Preload  | 10.0MB  |
| Footsteps        | 180    | 20KB     | ADPCM       | Preload  | 3.6MB   |
| Combat Impacts   | 150    | 40KB     | ADPCM       | Preload  | 6.0MB   |
| Dialogue         | 800    | 80KB     | Vorbis q3   | Stream   | 2.0MB*  |
| Music Stems      | 60     | 4MB      | Vorbis q5   | Stream   | 8.0MB*  |
| Ambient Beds     | 40     | 2MB      | Vorbis q3   | Stream   | 4.0MB*  |
| Level-Specific   | 300    | 45KB     | ADPCM       | On-demand| 13.5MB  |
| Reverb IRs       | 12     | 500KB    | PCM 16-bit  | Preload  | 6.0MB   |
| **TOTAL**        | **~1900** |       |             |          | **~58MB** |

*Stream buffer size, not total asset size on disk

### Streaming Configuration

```
Streaming Parameters:
  Buffer size:         256KB per stream
  Max concurrent:      6 streams (2 music + 2 dialogue + 2 ambient)
  Decode thread:       Dedicated audio I/O thread
  Prefetch:            500ms lookahead for music transitions
  Seek granularity:    FMOD subsound boundaries

  Disk I/O Budget:
    6 streams × 256KB buffer × 2 (double buffer) = 3MB I/O bandwidth
    Refresh rate: every 128ms at Vorbis q5 (≈192kbps per stream)
```

---

## 6. Voice Management

### Priority Matrix

| Priority | Category           | Max Voices | Steal Policy         |
|----------|--------------------|------------|----------------------|
| 10 (max) | Player dialogue    | 1          | Never steal          |
| 9        | NPC dialogue       | 2          | Queue, don't steal   |
| 8        | Player weapon      | 4          | Steal oldest         |
| 7        | Stingers           | 2          | Steal oldest         |
| 6        | Enemy weapons      | 8          | Steal quietest       |
| 5        | Combat impacts     | 6          | Steal farthest       |
| 4        | Footsteps          | 4          | Steal farthest       |
| 3        | Environment SFX    | 12         | Steal farthest       |
| 2        | Physics objects    | 6          | Steal quietest       |
| 1 (min)  | Distant ambient    | 8          | Virtualize at >80m   |

### Virtual Voice Thresholds

```
Voice becomes virtual when:
  - Distance > MaxDistance × 0.9
  - Calculated volume < -60dB
  - Occluded with LP cutoff < 300Hz

Voice re-activates when:
  - Distance < MaxDistance × 0.7 (hysteresis prevents thrashing)
  - Calculated volume > -48dB

Total voice allocation:
  Real voices:    128
  Virtual voices: 256 (position tracking only, no DSP)
```

---

## 7. Game State Audio Snapshots

| Game State    | Music   | SFX     | Voice   | Ambient | UI      |
|---------------|---------|---------|---------|---------|---------|
| Normal        | 100%    | 100%    | 100%    | 100%    | 100%    |
| Paused        | 50%     | Muted   | Muted   | Muted   | 100%    |
| Cutscene      | 100%    | 20%     | 100%    | 30%     | Muted   |
| Underwater    | LP 400  | LP 600  | LP 800  | LP 300  | 100%    |
| Death Screen  | Fade→0  | Fade→0  | Muted   | Fade→0  | 100%    |
| Inventory     | 70%     | 30%     | Muted   | 50%     | 100%    |
| Loading       | 100%    | Muted   | Muted   | Muted   | 100%    |

Snapshot transition time: 300ms default, 1500ms for death

---

## 8. Validation Checklist

- [x] Voice count (128) within PS5 limit (512) ✓
- [x] Voice count (128) within Xbox Series X limit (512) ✓
- [x] All bus routes verified for Pause state ✓
- [x] All bus routes verified for Underwater state ✓
- [x] All bus routes verified for Cutscene state ✓
- [x] Streaming buffer tested — no pops during level transitions ✓
- [x] Peak memory: 58MB < 80MB console budget ✓
- [x] Audio thread CPU: 8% of one core at 128 voices ✓
- [x] HRTF tested on PS5 Tempest Engine ✓
- [x] Reverb zone crossfades tested — no discontinuities ✓
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with precise scope covering bus hierarchy, spatial audio, middleware, memory, and voice management
- ST-02 (Structured Sequential Instructions) - Seven numbered steps building from requirements through validation
- RT-02 (Multi-Dimensional Analysis Framework) - Each system analyzed across configuration, impact, and platform constraints
- DS-03 (Tool and Methodology Suggestions) - Recommends FMOD vs Wwise vs native with decision criteria
- OC-01 (Output Structure Specification) - Defines expected deliverable format with tables, diagrams, and validation checklist

**Related Prompts:**
- `domain-game-development/performance/performance_profiling_optimization.md` - Profile audio thread CPU and memory usage
- `domain-game-development/architecture/architecture_engine_selection.md` - Engine choice affects available audio APIs
- `domain-software-engineering/analysis/performance/performance_bottleneck_identification.md` - General performance bottleneck methodology
