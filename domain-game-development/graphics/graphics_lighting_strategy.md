---
title: "Game Lighting Strategy & Optimization"
category: game-development/graphics
description: "Design lighting strategies covering baked vs real-time tradeoffs, light probe placement, shadow cascades, global illumination, and per-platform budgets"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - graphics
  - lighting
  - baked-lighting
  - global-illumination
  - shadows
  - optimization
updated: "2026-03-19"
related_prompts:
  - domain-game-development/graphics/graphics_shader_review.md
  - domain-game-development/performance/performance_rendering_optimization.md
  - domain-game-development/performance/performance_frame_budget_analysis.md
---

# Game Lighting Strategy & Optimization

**Objective:** Design game lighting strategies that balance visual quality with performance, selecting appropriate combinations of baked and real-time lighting, configuring shadow systems, and setting per-platform lighting budgets.

## When to Use

- Use when planning the lighting pipeline for a new game or level
- Use when lighting is consuming too much of the frame budget
- Use when choosing between baked and real-time approaches for a specific game type
- Don't use for shader code review — use `graphics_shader_review.md` for that

## Instructions

1. **Assess Lighting Requirements**
   - Game type constraints:
     - **Static environments** (puzzle, strategy): Heavily baked, minimal real-time
     - **Semi-dynamic** (RPG, adventure): Baked ambient + real-time key lights
     - **Fully dynamic** (multiplayer, destructible): All real-time, or hybrid with fallbacks
   - Time-of-day system: static vs dynamic day/night cycle
   - Destructible environments: baked lighting breaks when geometry changes
   - Interior vs exterior: different approaches often needed for each
   - Target mood and art style: photorealistic, stylized, noir, cel-shaded

2. **Choose Lighting Pipeline**
   - **Fully baked (lightmaps):**
     - Pros: Best quality for static scenes, zero runtime GPU cost, GI included
     - Cons: Long bake times, large lightmap textures, no dynamic response
     - Best for: mobile, VR, static environments, indie with limited GPU budget
   - **Fully real-time:**
     - Pros: Everything responds to changes, supports dynamic time-of-day
     - Cons: Expensive, limited GI quality, shadow map artifacts
     - Best for: multiplayer, destructible worlds, dynamic lighting essential to gameplay
   - **Hybrid (recommended for most games):**
     - Baked: ambient/fill lighting, GI contribution, static shadows
     - Real-time: key/directional light, dynamic shadows for characters, point lights
     - Pros: Best quality-to-performance ratio
     - Cons: Complexity of managing two systems

3. **Configure Shadow System**
   - **Shadow cascades** (directional light):
     - 2 cascades: mobile, simple scenes
     - 3-4 cascades: PC/console, open worlds
     - Cascade split distances: tune to cover play area (e.g., 10m, 30m, 100m, 500m)
   - **Shadow resolution:** 1024 (mobile) → 2048 (console) → 4096 (PC ultra)
   - **Shadow filtering:** PCF (cheap), PCSS (soft shadows), VSM (variance)
   - **Shadow distance:** Limit max shadow draw distance (200-500m for open world)
   - **Per-object shadows:** Disable shadows for small/distant objects

4. **Design Global Illumination Approach**
   - **Baked GI (lightmaps/light probes):** Pre-computed, high quality, static
   - **Screen-space GI (SSGI):** Cheap approximation, limited range, no off-screen contribution
   - **Voxel GI (VXGI):** Dynamic, good quality, expensive (50-200% of forward lighting cost)
   - **Lumen (Unreal 5):** Software ray tracing + hardware RT, dynamic GI
   - **Light probes:** Place at navigation-relevant points, capture ambient lighting for dynamic objects
   - **Reflection probes:** For specular reflections, box/sphere projection, blend between probes

5. **Set Per-Platform Lighting Budgets**
   - Define maximum light counts per platform:
     - Mobile: 1 directional + 4 point/spot (forward rendering)
     - Console (current-gen): 1 directional + 32-64 local lights (deferred/clustered)
     - PC: 1 directional + 128+ local lights (clustered forward/deferred)
   - Define shadow-casting light limits:
     - Mobile: 1 shadow-casting light (directional only)
     - Console: 4-8 shadow-casting lights
     - PC: 8-16 shadow-casting lights
   - LOD lighting: reduce light count/quality with distance

6. **Implement Lighting Optimization Techniques**
   - **Light culling:** Don't process lights outside camera frustum
   - **Light clustering/tiling:** Group lights spatially for efficient GPU processing
   - **Shadow culling:** Don't render shadow maps for lights behind camera
   - **Light importance scoring:** Prioritize nearby, bright, large-radius lights
   - **Baked shadow masks:** Use baked shadows for static geometry, real-time for dynamic only
   - **Light layers/channels:** Separate lighting for gameplay (player highlight) vs environment

7. **CRITICAL: Validate Lighting Quality and Performance**
   - Profile lighting GPU cost per platform — should be 20-35% of frame budget
   - Test in worst-case scenes (maximum light overlap, all shadows active)
   - Verify light probe coverage — no dark patches where probes are missing
   - Check shadow cascade transitions — no visible "popping" at cascade boundaries
   - Test time-of-day transitions — smooth, no flickering
   - Compare visual quality across platforms — acceptable degradation, not broken

**False-Positive Prevention (MUST follow):**

❌ **DON'T:**
- Don't recommend fully baked lighting for games with destructible environments
- Don't recommend ray-traced GI without confirming hardware requirements are acceptable
- Don't optimize lighting before profiling — measure first, then tune
- Don't assume more lights = better visuals — art direction matters more than light count
- Don't ignore light probe placement — it's the #1 cause of "weird lighting on characters"

✅ **DO:**
- Profile per-platform before making lighting decisions
- Consider art style — stylized games may look better with fewer, carefully placed lights
- Test with both daytime and nighttime if the game has a day/night cycle
- Verify lighting looks correct on both HDR and SDR displays
- Place light probes at player-accessible locations, not in walls or ceilings

## Expected Output

A lighting strategy document including:

- Lighting pipeline selection with rationale
- Baked vs real-time breakdown per light type
- Shadow configuration (cascades, resolution, filtering)
- GI approach and probe placement guidelines
- Per-platform light count and shadow budgets
- Performance budget allocation
- Quality validation checklist

## Example Output

```markdown
## Lighting Strategy — "Echoes of Ember" (3D Action RPG, UE5)

### 1. Lighting Requirements

| Attribute | Value |
|-----------|-------|
| Art style | Semi-realistic fantasy |
| Environment type | Mixed interior/exterior, no destruction |
| Time of day | Dynamic day/night cycle (24 min real-time = 1 game day) |
| Platforms | PS5, Xbox Series X, PC (GTX 1070 min) |
| Target framerate | 60 FPS (performance mode), 30 FPS (quality mode) |

### 2. Lighting Pipeline: Hybrid

| Light Type | Approach | Rationale |
|-----------|----------|-----------|
| Directional (sun/moon) | Real-time | Dynamic time-of-day required |
| Ambient/fill | Baked (light probes) | Stable base illumination, free at runtime |
| Torches/campfires | Real-time point lights | Dynamic, flicker animation |
| Interior key lights | Baked (lightmaps) | Static rooms, high quality GI |
| Character lighting | Real-time + probes | Must respond to environment dynamically |
| Volumetric fog | Real-time (half-res) | Atmosphere, god rays |

### 3. Shadow Configuration

**Directional Light (Sun):**
| Parameter | Performance Mode | Quality Mode |
|-----------|-----------------|-------------|
| Cascades | 3 | 4 |
| Resolution | 2048 | 4096 |
| Cascade splits | 15m, 50m, 200m | 10m, 30m, 100m, 500m |
| Filtering | PCF 3×3 | PCSS (contact-hardening) |
| Max distance | 200m | 500m |

**Local Lights (torches, spells):**
| Parameter | Value |
|-----------|-------|
| Shadow-casting limit | 4 simultaneous (nearest priority) |
| Resolution | 512 per light |
| Update frequency | Every frame (nearest 2), every other frame (far 2) |

### 4. Global Illumination

**Approach: Lumen (Software, not Hardware RT)**

| Parameter | Performance Mode | Quality Mode |
|-----------|-----------------|-------------|
| Method | Screen-space (SSGI) | Lumen (software RT) |
| Quality | Medium | High |
| GI bounces | 1 | 2 |
| GPU cost | ~2ms | ~4ms |

**Light Probe Grid:**
```
Exterior: 5m × 5m × 3m grid (covers player height variations)
Interior: 2m × 2m × 2m grid (tighter for rooms, corridors)
Doorways: Extra probes at interior/exterior transitions (3 probes per doorway)
Caves: Follow path with 3m spacing, cluster at openings
```

**Probe placement rules:**
- Never place inside geometry (walls, floors)
- Always place at ground level AND 2m above (character head height)
- Add manual probes at visually important locations (altar, throne, boss arena)
- Total probe count target: ~2,000 per zone (acceptable memory)

### 5. Per-Platform Budgets

| Resource | PS5 / Xbox Series | PC (GTX 1070) | PC (RTX 3070+) |
|----------|-------------------|----------------|-----------------|
| Max visible lights | 64 | 32 | 128 |
| Shadow-casting lights | 6 | 4 | 8 |
| Directional shadow res | 4096 | 2048 | 4096 |
| GI method | Lumen (SW) | SSGI | Lumen (HW RT) |
| Volumetric fog | Half-res | Quarter-res | Full-res |
| Reflection probes | 8 per zone | 4 per zone | 12 per zone |

### 6. Frame Budget Allocation (Lighting)

**Target: 4.5ms of 16.6ms budget (60 FPS) = 27% of frame**

| System | Performance (ms) | Quality (ms) |
|--------|-----------------|-------------|
| Directional shadows | 1.0 | 2.0 |
| Local light shadows | 0.5 | 1.0 |
| Light clustering | 0.3 | 0.3 |
| Global illumination | 1.5 | 3.0 |
| Volumetric fog | 0.5 | 1.0 |
| Reflection probes | 0.3 | 0.5 |
| **Total lighting** | **4.1ms** | **7.8ms** |

Performance mode: ✅ Within 60 FPS budget
Quality mode: ✅ Within 30 FPS budget (33.3ms total)

### 7. Day/Night Cycle Configuration

| Time | Sun Angle | Sun Color (K) | Ambient | Shadows |
|------|-----------|--------------|---------|---------|
| Dawn (6:00) | 5° | 3000K (warm orange) | Dark blue fill | Long, soft |
| Morning (9:00) | 30° | 4500K (warm white) | Light blue fill | Medium |
| Noon (12:00) | 80° | 6500K (neutral white) | Bright sky blue | Short, hard |
| Afternoon (15:00) | 45° | 5500K (warm) | Warm fill | Medium-long |
| Sunset (18:00) | 5° | 2500K (deep orange) | Purple fill | Long, very soft |
| Night (22:00) | -30° | Moonlight 8000K (cool) | Dark blue | Moon shadows only |

**Transition:** Blend all parameters over 30 seconds real-time per game-hour

### 8. Optimization Checklist

- [ ] Profile worst-case scene (maximum torches + fire spells + day/night transition)
- [ ] Verify no light leaking through walls (probe placement check)
- [ ] Test all time-of-day phases for shadow cascade popping
- [ ] Verify character lighting matches environment at all times of day
- [ ] Test HDR and SDR output for correct exposure
- [ ] Confirm mobile/low-spec fallback looks acceptable (SSGI instead of Lumen)
- [ ] Profile and verify lighting stays within 27% of frame budget
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defines quality-performance balance as the goal
- **ST-02 (Structured Sequential Instructions):** Seven-step process from assessment to validation
- **RT-02 (Multi-Dimensional Analysis):** Evaluates baked vs real-time, GI methods, shadow systems independently
- **RT-05 (Evidence-Based Reasoning):** Requires profiling data and per-platform measurements
- **DS-06 (Prioritization and Severity Guidance):** Prioritizes by platform and visual impact

## Related Prompts

- [Shader Code Review](graphics_shader_review.md) — Review custom lighting shaders
- [Rendering Optimization](../performance/performance_rendering_optimization.md) — Broader rendering pipeline optimization
- [Frame Budget Analysis](../performance/performance_frame_budget_analysis.md) — Allocate lighting within total frame budget
