---
title: "Frame Budget Analysis & Optimization"
category: game-development/performance
description: "Analyze game frame budgets with CPU vs GPU bound identification, per-system time allocation, and profiler-driven optimization priorities"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-03
difficulty: advanced
tags:
  - performance
  - frame-budget
  - profiling
  - cpu
  - gpu
  - optimization
  - framerate
updated: "2026-03-19"
---

#### Frame Budget Analysis & Optimization

**Objective:** Analyze game frame budgets to identify CPU vs GPU bottlenecks, allocate time per system (physics, AI, rendering, scripting, audio), establish profiler-driven optimization priorities, and plan target framerate strategies across platforms.

**When to Use:** When a game has framerate drops, inconsistent frame pacing, or needs to meet target performance on specific hardware. Use during mid-to-late production, after porting to new platforms, or whenever profiling data reveals frames exceeding budget.

**Instructions:**

1. **Establish target frame budget** based on target framerate and platform:
   - 60 fps → 16.67ms per frame
   - 30 fps → 33.33ms per frame
   - 120 fps → 8.33ms per frame
   - Account for OS/driver overhead (typically 1-2ms on console, variable on PC)

2. **Profile and categorize time spent** across all major systems:
   - Rendering (draw calls, GPU time, post-processing)
   - Physics (rigid bodies, raycasts, collision detection)
   - AI / Gameplay logic (pathfinding, behavior trees, state machines)
   - Animation (skeletal blending, IK, root motion)
   - Audio (mixing, DSP effects, spatial audio)
   - UI (layout, canvas rebuilds, text rendering)
   - Scripting / GC (managed code, garbage collection spikes)

3. **Identify bound type** for each problematic frame:
   - CPU-bound: CPU time > GPU time, GPU idle waiting
   - GPU-bound: GPU time > CPU time, CPU finishes early
   - Memory-bandwidth-bound: high cache miss rate, texture thrashing
   - Present/vsync-bound: both CPU and GPU finish early, waiting for vsync

4. **Per-system budget allocation with headroom:**
   - Allocate specific ms targets per system
   - Reserve 10-15% headroom for spikes and unexpected load
   - Identify which systems have fixed cost vs. scaling cost

5. **Prioritize optimizations by impact-to-effort ratio:**
   - Rank each optimization by ms saved vs. engineering days required
   - Prefer algorithmic improvements over micro-optimizations
   - Consider platform-specific fast paths (NEON, AVX, compute shaders)

6. **Platform-specific budgets:**
   - Console: fixed hardware, predictable performance, thermal sustained mode
   - PC: variable hardware, build scalability options, min-spec profiling
   - Mobile: thermal throttling after 10-15 minutes, battery considerations
   - Handheld (Switch/Steam Deck): docked vs. handheld clocks, thermal limits

7. **CRITICAL: Verify before reporting findings:**
   - Measurements MUST be from representative gameplay scenarios (not menu screens, not empty levels)
   - Profiling MUST be done on target hardware (not dev machine with 64GB RAM and RTX 4090)
   - GC spikes MUST be accounted for (capture 99th percentile, not just average)
   - Frame pacing issues MUST be distinguished from raw framerate issues
   - Development builds have overhead — measure release/shipping builds where possible

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT optimize based on editor profiling numbers (standalone/shipping builds only)
- ❌ Do NOT assume CPU-bound means GPU is fine (both can be simultaneously at limits)
- ❌ Do NOT report average frame times without also reporting 99th percentile and worst-case
- ❌ Do NOT recommend optimizations without measuring their actual impact
- ❌ Do NOT ignore frame pacing (consistent 30fps feels better than 30-60fps oscillation)
- ✅ DO profile worst-case scenes (maximum enemy count, particle effects, destruction)
- ✅ DO account for thermal throttling on mobile and handheld devices
- ✅ DO measure with target-representative content (final art, not placeholder cubes)
- ✅ DO capture GC spikes and hitching separately from sustained frame time
- ✅ DO verify vsync/present mode settings match shipping configuration

**Expected Output:** A detailed frame budget report with per-system time allocation, bound type identification, prioritized optimization recommendations with estimated ms savings, and platform-specific budget tables.

**Example Output:**

```markdown
## Frame Budget Analysis Report

### Project: "Iron Vanguard" — 3D Action Game
### Target Platforms: PS5 (60fps), Nintendo Switch (30fps)
### Build: Release candidate RC-4, revision 8821
### Capture Date: 2026-03-18

---

### 1. Target Frame Budgets

| Platform | Target FPS | Total Budget | Usable Budget (15% headroom) |
|----------|-----------|-------------|------------------------------|
| PS5 | 60 fps | 16.67ms | 14.17ms |
| Switch Docked | 30 fps | 33.33ms | 28.33ms |
| Switch Handheld | 30 fps | 33.33ms | 28.33ms |

---

### 2. Current Frame Time Breakdown (PS5 — 60fps Target)

**Capture Scenario:** Act 3 Boss Fight — 12 enemies, particle-heavy, destructible arena
**Frames Captured:** 3,600 (60 seconds)

| System | Average (ms) | P95 (ms) | P99 (ms) | Budget (ms) | Status |
|--------|-------------|----------|----------|-------------|--------|
| Rendering (CPU) | 4.2 | 5.1 | 6.8 | 4.5 | ⚠️ P99 Over |
| Rendering (GPU) | 7.8 | 9.2 | 11.4 | 8.0 | ❌ Over Budget |
| Physics | 1.9 | 2.4 | 3.1 | 2.0 | ⚠️ P99 Over |
| AI / Gameplay | 2.1 | 3.8 | 5.2 | 2.5 | ❌ Over Budget |
| Animation | 1.1 | 1.3 | 1.5 | 1.5 | ✅ On Budget |
| Audio | 0.6 | 0.7 | 0.8 | 1.0 | ✅ On Budget |
| UI | 0.4 | 0.5 | 0.9 | 0.5 | ⚠️ P99 Over |
| Scripting / GC | 0.3 | 0.4 | 4.2 | 0.5 | ❌ GC Spikes |
| **Total** | **18.4** | **23.4** | **33.9** | **14.17** | ❌ **Over** |

**Bound Type:** GPU-bound (primary), CPU-bound during AI spikes (secondary)

**Frame Pacing Analysis:**
- Average frame time: 18.4ms (54.3 fps effective)
- Frame time variance: σ = 4.7ms — **poor frame pacing**
- Frames exceeding 16.67ms: 68% — **unacceptable for 60fps**
- Frames exceeding 33.33ms: 4.2% — **visible hitches**
- GC spike frequency: every ~8 seconds, duration 3-5ms

---

### 3. Current Frame Time Breakdown (Switch Docked — 30fps Target)

**Capture Scenario:** Same Act 3 Boss Fight, Switch-specific LODs
**Frames Captured:** 1,800 (60 seconds)

| System | Average (ms) | P95 (ms) | P99 (ms) | Budget (ms) | Status |
|--------|-------------|----------|----------|-------------|--------|
| Rendering (CPU) | 6.8 | 8.2 | 10.1 | 8.0 | ⚠️ P99 Over |
| Rendering (GPU) | 14.2 | 18.1 | 22.6 | 12.0 | ❌ Over Budget |
| Physics | 3.4 | 4.1 | 5.8 | 4.0 | ❌ P99 Over |
| AI / Gameplay | 4.6 | 6.2 | 8.9 | 5.0 | ❌ Over Budget |
| Animation | 2.1 | 2.6 | 3.0 | 3.0 | ✅ On Budget |
| Audio | 0.9 | 1.1 | 1.2 | 1.5 | ✅ On Budget |
| UI | 0.7 | 0.9 | 1.4 | 1.0 | ⚠️ P99 Over |
| Scripting / GC | 0.5 | 0.6 | 6.1 | 0.8 | ❌ GC Spikes |
| **Total** | **33.2** | **41.8** | **59.1** | **28.33** | ❌ **Over** |

**Bound Type:** GPU-bound (severe)

---

### 4. Bound Type Deep Dive

#### PS5 — GPU Bound Analysis
```
GPU Timeline (worst-case frame):
├── Shadow Pass:           2.8ms  (4 shadow-casting lights)
├── GBuffer Pass:          2.1ms  (1,847 draw calls)
├── Lighting Pass:         1.9ms  (deferred tile lighting)
├── Transparent Pass:      2.4ms  (particles + VFX, heavy overdraw)
├── Post-Processing:       1.8ms  (bloom + TAA + motion blur + DOF)
└── UI Overlay:            0.4ms
Total GPU:                11.4ms
```

**Root Cause:** Transparent pass overdraw from particle systems during boss
fight VFX. Overdraw measured at 4.7x average across viewport.

#### PS5 — CPU Spike Analysis
```
CPU Timeline (worst-case frame with AI spike):
├── Main Thread:
│   ├── AI Update:         5.2ms  (12 enemies × pathfinding recalc)
│   ├── Physics Sync:      1.8ms  (broad phase + narrow phase)
│   ├── Animation Jobs:    0.3ms  (kick off, wait for workers)
│   ├── Render Submit:     3.1ms  (command buffer building)
│   └── Script/GC:        4.2ms  (GC.Collect triggered)
├── Worker Threads (4):
│   ├── Physics Jobs:      1.3ms  (parallel solver)
│   ├── Animation Blend:   1.2ms  (skeletal eval)
│   └── Culling:           0.8ms  (frustum + occlusion)
```

**Root Cause:** AI pathfinding recalculates all 12 agents simultaneously
on the main thread. GC spike from temporary allocations in combat system.

---

### 5. Optimization Priorities (Impact-to-Effort Ratio)

| # | Optimization | Est. Savings | Effort | Platform | Priority |
|---|-------------|-------------|--------|----------|----------|
| 1 | Stagger AI pathfinding (4 agents/frame max) | 3.2ms CPU | 2 days | All | P0 |
| 2 | Particle overdraw budget (max 2.5x) | 1.8ms GPU | 3 days | All | P0 |
| 3 | Eliminate GC allocations in combat loop | 4.2ms spikes | 3 days | All | P0 |
| 4 | GPU instancing for enemy draw calls | 1.1ms GPU | 1 day | All | P0 |
| 5 | Shadow cascade distance reduction (Switch) | 2.4ms GPU | 0.5 day | Switch | P1 |
| 6 | Post-process half-res bloom (Switch) | 0.8ms GPU | 1 day | Switch | P1 |
| 7 | LOD bias increase for handheld mode | 1.6ms GPU | 0.5 day | Switch | P1 |
| 8 | Pool UI canvas rebuilds | 0.4ms CPU | 1 day | All | P2 |
| 9 | Async physics scene queries | 0.6ms CPU | 2 days | All | P2 |
| 10 | Audio DSP to secondary thread | 0.3ms CPU | 2 days | All | P3 |

---

### 6. Recommended Budget Allocation (Post-Optimization)

#### PS5 — 60fps (16.67ms total, 14.17ms usable)

| System | Target (ms) | % of Budget |
|--------|------------|-------------|
| Rendering (CPU) | 3.5 | 24.7% |
| Rendering (GPU) | 6.5 | 45.9% |
| Physics | 1.5 | 10.6% |
| AI / Gameplay | 1.5 | 10.6% |
| Animation | 1.0 | 7.1% |
| Audio | 0.5 | 3.5% |
| UI | 0.3 | 2.1% |
| Scripting | 0.2 | 1.4% |
| **Headroom** | **2.50** | **15.0%** |

#### Switch Docked — 30fps (33.33ms total, 28.33ms usable)

| System | Target (ms) | % of Budget |
|--------|------------|-------------|
| Rendering (CPU) | 6.0 | 21.2% |
| Rendering (GPU) | 11.0 | 38.8% |
| Physics | 3.5 | 12.4% |
| AI / Gameplay | 4.0 | 14.1% |
| Animation | 2.0 | 7.1% |
| Audio | 1.0 | 3.5% |
| UI | 0.5 | 1.8% |
| Scripting | 0.3 | 1.1% |
| **Headroom** | **5.00** | **15.0%** |

---

### 7. Platform-Specific Recommendations

#### PS5
- Enable async compute for shadow map rendering (overlaps with CPU work)
- Use PS5 GPU query timestamps for per-pass profiling
- Target consistent 60fps — no dynamic resolution unless absolutely needed
- Monitor SSD streaming to avoid I/O stalls

#### Nintendo Switch
- Implement dynamic resolution scaling: 900p docked → 540p minimum
- Reduce shadow cascade count from 4 to 2
- Disable volumetric fog, use billboard fog planes
- Cap enemy count to 8 (vs 12 on PS5)
- **Thermal throttle test:** Run boss fight loop for 30 minutes in handheld
  - Current: drops to 22fps after 12 minutes
  - Target: sustain 28+ fps after 30 minutes

---

### 8. GC Spike Mitigation Plan

```csharp
// BEFORE: Allocating in hot path
void ProcessCombatHit(HitData hit) {
    var results = new List<DamageResult>();        // GC allocation
    var statusEffects = new List<StatusEffect>();   // GC allocation
    var particles = new ParticleRequest();          // GC allocation
    // ... process hit
}

// AFTER: Pre-allocated pools
private readonly List<DamageResult> _resultBuffer = new(32);
private readonly List<StatusEffect> _effectBuffer = new(16);
private readonly ObjectPool<ParticleRequest> _particlePool = new(64);

void ProcessCombatHit(HitData hit) {
    _resultBuffer.Clear();
    _effectBuffer.Clear();
    var particles = _particlePool.Get();
    try {
        // ... process hit using pre-allocated buffers
    } finally {
        _particlePool.Return(particles);
    }
}
```

**Expected GC reduction:** Eliminate ~2KB/frame allocation → prevent
GC.Collect triggers during gameplay.

---

### 9. Monitoring & Regression Prevention

- Add frame budget assertions in CI: fail build if P95 > budget on
  automated test scenes
- Instrument telemetry for shipped builds: track P95 frame times by
  scene and platform
- Weekly performance review of new content submissions
- Automated profiling captures on each milestone build

---

### Action Items

1. **This week:** Items #1 (AI stagger), #3 (GC elimination), #4 (instancing)
2. **Next week:** Items #2 (particle budget), #5-#7 (Switch-specific)
3. **Sprint after:** Items #8-#10 (lower priority), CI integration
4. **Ongoing:** Content team training on per-asset budgets
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — Opens with specific, measurable analysis goals
- ST-02 (Structured Sequential Instructions) — Numbered profiling and analysis workflow
- RT-02 (Multi-Dimensional Analysis Framework) — CPU, GPU, per-system, per-platform analysis
- RT-05 (Verification and Validation Steps) — Critical verification of profiling conditions
- DS-03 (Tool and Methodology Suggestions) — Profiling tools, measurement approaches, CI integration

**Related Prompts:**
- `performance/performance_rendering_optimization.md` — Deep dive on rendering-specific optimizations
- `graphics/graphics_shader_review.md` — Shader-level performance analysis
- `graphics/graphics_lighting_strategy.md` — Lighting budget planning
