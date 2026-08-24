---
title: "Shader Code Review & Optimization"
category: game-development/graphics
description: "Review shader code in HLSL, GLSL, or ShaderLab for correctness, performance, branching issues, register pressure, and cross-platform compatibility"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-03
difficulty: advanced
tags:
  - graphics
  - shaders
  - hlsl
  - glsl
  - optimization
  - code-review
  - gpu
  - rendering
updated: "2026-03-19"
---

#### Shader Code Review & Optimization

**Objective:** Review shader code (HLSL, GLSL, ShaderLab, Shader Graph) for correctness, performance optimization, branching issues, register pressure, texture sampling efficiency, and cross-platform compatibility across desktop, mobile, and console GPUs.

**When to Use:** When custom shaders are causing GPU bottlenecks, when porting shaders to new platforms (especially desktop to mobile), when reviewing shader PRs, or when shader compilation times or variant counts are growing out of control.

**Instructions:**

1. **Analyze shader structure** and overall organization:
   - Vertex/fragment/compute stage organization and responsibility split
   - Input/output semantics and interpolator count (minimize varyings passed to fragment)
   - Shader variant/keyword count (each keyword doubles variants — 10 keywords = 1024 variants)
   - Multi-pass vs. single-pass design and whether passes can be combined
   - Identify which render pass this shader runs in (shadow, GBuffer, forward, transparent)

2. **Check mathematical correctness:**
   - Precision: are calculations done in appropriate space (world vs. view vs. tangent)?
   - Normalization: are vectors renormalized after interpolation where required?
   - Color space: is linear-to-sRGB conversion handled correctly (manual vs. hardware)?
   - Gamma correctness: are texture samples in correct space before math operations?
   - Normal mapping: is TBN matrix construction correct (handedness, mikktspace compliance)?
   - HDR values: are intermediate results clamped or handled to prevent NaN/Inf propagation?

3. **Identify performance issues:**
   - Dynamic branching: avoid divergent branches on mobile tile-based GPUs (all fragments in a tile execute both paths)
   - Dependent texture reads: texture UV computed in fragment shader forces serialized fetch
   - Excessive ALU: unnecessary `normalize()`, `sqrt()`, `pow()` calls — use approximations where acceptable
   - Redundant calculations: math that could be moved from fragment to vertex shader
   - Unnecessary full-precision: operations that work fine at `half` (16-bit) precision
   - Loop unrolling: dynamic loops prevent compiler optimization — use `[unroll]` where iteration count is known
   - Sincos / transcendental functions: expensive on all GPUs — precompute or use LUT textures

4. **Evaluate register pressure and occupancy:**
   - Count temporary registers used (high VGPR count reduces wave/warp occupancy)
   - Identify variables that can be recomputed rather than stored (trade ALU for registers)
   - Check for excessive interpolators (each varying consumes registers in fragment shader)
   - Review constant buffer layout (packing, alignment, update frequency separation)
   - Compute shader: verify groupshared memory doesn't limit occupancy
   - Target: keep VGPR < 48 for high occupancy on AMD GCN/RDNA, < 64 for reasonable occupancy

5. **Review texture sampling efficiency:**
   - Redundant samples: same texture sampled multiple times with same UV
   - LOD bias: explicit LOD selection in vertex shader or compute to avoid gradient issues
   - Sampling in vertex shader: data that doesn't need per-pixel resolution (e.g., wind offset)
   - Texture atlasing: multiple small textures that could share a single atlas and sampler
   - Sampler reuse: use shared samplers rather than per-texture samplers
   - Anisotropic filtering: only where needed (ground textures at glancing angles, not UI)
   - Gather vs. Sample: use `GatherRed()` when sampling 4 adjacent texels for filters

6. **Cross-platform compatibility review:**
   - `half` vs. `float` precision: `half` is true 16-bit on mobile, often 32-bit on desktop — code must work at both
   - Metal/Vulkan/DX12 differences: resource binding models, push constants, descriptor sets
   - Mobile GPU architecture: tile-based deferred rendering (TBDR) — avoid framebuffer reads, use subpass loads
   - Console-specific intrinsics: wave operations, LDS, async compute compatibility
   - WebGL/WebGPU constraints: no compute shaders in WebGL, limited uniform buffer size
   - Verify shader model requirements match minimum spec (SM 5.0, SM 6.0, GLSL ES 3.0)

7. **CRITICAL: Verify before finalizing review:**
   - Shader MUST compile on all target platforms without warnings
   - No precision artifacts MUST be verified on mobile devices (not just emulators)
   - Variant count MUST be checked — more than 256 variants per shader is a red flag
   - Shader compilation time MUST be measured — variant explosion causes minutes-long load times
   - Visual output MUST be compared across platforms (screenshot diff for correctness)
   - Performance MUST be measured on the actual shader in context (not isolated benchmarks)

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT micro-optimize shaders that run on less than 1% of screen pixels (small objects, rare paths)
- ❌ Do NOT demand full `float` precision everywhere (color math, UV math, and lighting at `half` is fine for most cases)
- ❌ Do NOT flag dynamic branching as always bad (coherent branches on desktop GPUs are fine — the cost is divergent branches on mobile)
- ❌ Do NOT recommend ALU-heavy workarounds to avoid a single texture sample (texture fetch is often cheaper than 10+ ALU ops)
- ❌ Do NOT ignore variant count (a shader that compiles 4096 variants will destroy build times and load times)
- ✅ DO check if the shader is on a hot path — fullscreen post-process and terrain shaders matter more than a shader on one NPC hat
- ✅ DO consider shader compilation time impact (player experience during loading)
- ✅ DO verify visual correctness alongside performance changes
- ✅ DO test precision changes on actual mobile hardware (half precision rounding differs by chipset)
- ✅ DO review the shader in the context of the full render pass (vertex-bound vs. fragment-bound changes the priority)

**Expected Output:** A shader review report covering correctness issues, performance findings ranked by impact, cross-platform compatibility concerns, and specific code-level recommendations with before/after examples.

**Example Output:**

```markdown
## Shader Code Review Report

### Shader: Custom Water Surface (HLSL)
### File: Shaders/Environment/Water_Surface.hlsl
### Render Pass: Forward transparent
### Platforms: PC (DX12), PS5, Xbox Series X, Nintendo Switch
### Screen Coverage: 5-40% of viewport (large lakes and ocean)

---

### 1. Shader Overview

**Stages:** Vertex + Fragment (no tessellation)
**Features:** Wave displacement, refraction, reflection (SSR + planar fallback),
foam, caustics, depth-based color, Fresnel
**Keywords:** 6 keywords → 64 variants
**Interpolators:** 9 (position, normal, tangent, UV0, UV1, screenPos, worldPos,
viewDir, fogFactor)
**Estimated Instruction Count:** VS: 42, PS: 187

**Verdict:** Fragment-heavy shader on a high-coverage surface — performance
critical. Current 187 instructions is high for a transparent pass shader.

---

### 2. Correctness Issues

#### ISSUE C-01: Incorrect Normal Reconstruction After Wave Displacement

```hlsl
// CURRENT (line 67-71): Normal computed from displaced position
// but using pre-displacement tangent frame
float3 worldNormal = normalize(input.Normal);  // ← Pre-displacement normal!
float3 waveOffset = CalculateWaveDisplacement(input.WorldPos, _Time);
float3 displacedPos = input.WorldPos + waveOffset;
// Normal should be recomputed from displaced surface
```

**Problem:** The normal vector is taken from the original mesh, not the wave-
displaced surface. Lighting will be incorrect — waves will appear to have no
geometric shading variation.

```hlsl
// FIX: Compute normal from wave displacement partial derivatives
float3 waveOffset = CalculateWaveDisplacement(worldPos, _Time);
float3 waveOffsetDX = CalculateWaveDisplacement(worldPos + float3(0.1, 0, 0), _Time);
float3 waveOffsetDZ = CalculateWaveDisplacement(worldPos + float3(0, 0, 0.1), _Time);

float3 tangent = normalize(float3(0.1, waveOffsetDX.y - waveOffset.y, 0));
float3 binormal = normalize(float3(0, waveOffsetDZ.y - waveOffset.y, 0.1));
float3 worldNormal = normalize(cross(binormal, tangent));
```

**Severity:** High (visual correctness)

#### ISSUE C-02: Missing sRGB Conversion on Foam Texture

```hlsl
// CURRENT (line 112):
float4 foamColor = FoamTexture.Sample(SamplerLinear, foamUV);
// Texture is sRGB but sampled as linear — foam will appear washed out
```

```hlsl
// FIX: Use sRGB sampler or manual conversion
float4 foamColor = FoamTexture.Sample(SamplerLinearSRGB, foamUV);
// Or if sampler can't be changed:
// foamColor.rgb = pow(foamColor.rgb, 2.2);
```

**Severity:** Medium (visual correctness, subtle but visible)

#### ISSUE C-03: NaN Propagation from Fresnel Calculation

```hlsl
// CURRENT (line 134):
float fresnel = pow(1.0 - dot(viewDir, normal), 5.0);
// If normal is zero (degenerate mesh) or viewDir parallel to normal,
// dot can produce values > 1.0 or < 0.0, pow of negative = NaN
```

```hlsl
// FIX: Clamp input to safe range
float NdotV = saturate(dot(normalize(viewDir), normalize(normal)));
float fresnel = pow(1.0 - NdotV, 5.0);
```

**Severity:** Medium (causes black pixels on edge cases)

---

### 3. Performance Issues (ranked by impact)

#### PERF P-01: Redundant Texture Samples (saves ~0.4ms at 40% coverage)

```hlsl
// CURRENT: Normal map sampled 3 times with different UVs for detail
float3 normal1 = NormalMap.Sample(Sampler, uv * 1.0).rgb;   // line 78
float3 normal2 = NormalMap.Sample(Sampler, uv * 2.7).rgb;   // line 79
float3 normal3 = NormalMap.Sample(Sampler, uv * 7.3).rgb;   // line 80
float3 blended = normalize(normal1 + normal2 + normal3);

// Also: the SAME normal map is sampled AGAIN for caustics (line 145)
float3 causticsNormal = NormalMap.Sample(Sampler, uv * 3.0).rgb;
```

**Fix:** Reuse sample results. 4 texture fetches reduced to 3 (the caustics
sample at `uv * 3.0` is close enough to `uv * 2.7` to share with a slight
UV adjustment). Consider using a single fetch with a detail texture multiply.

#### PERF P-02: Full Precision Where Half Suffices (saves register pressure)

```hlsl
// CURRENT: All computations in float (32-bit)
float3 reflectionColor = ...;     // HDR, needs float ← CORRECT
float3 refractionColor = ...;     // HDR, needs float ← CORRECT
float3 foamColor = ...;           // LDR 0-1, half is fine ← WASTEFUL
float  foamMask = ...;            // 0-1 mask, half is fine ← WASTEFUL
float  depthFade = ...;           // 0-1 fade, half is fine ← WASTEFUL
float3 finalColor = ...;          // HDR output, needs float ← CORRECT
```

```hlsl
// FIX: Use half where appropriate (critical for Switch and mobile)
half3 foamColor = (half3)FoamTexture.Sample(Sampler, foamUV).rgb;
half  foamMask = (half)saturate(shoreline * foamIntensity);
half  depthFade = (half)saturate(sceneDepth - waterDepth);
```

**Impact:** Reduces VGPR usage from ~52 to ~38 on Switch (improves occupancy
from 6 waves to 8 waves per SIMD unit — ~33% throughput increase).

#### PERF P-03: Unnecessary normalize() Calls (saves ~8 ALU)

```hlsl
// CURRENT: 5 normalize() calls in fragment shader
float3 viewDir = normalize(input.ViewDir);           // line 88
float3 lightDir = normalize(_LightDirection);        // line 89 ← UNNECESSARY
float3 halfDir = normalize(viewDir + lightDir);      // line 90
float3 worldNormal = normalize(input.Normal);        // line 91
float3 reflectDir = normalize(reflect(-viewDir, worldNormal)); // line 95 ← UNNECESSARY
```

```hlsl
// FIX:
// _LightDirection is already normalized on CPU — skip
// reflect() of normalized inputs produces normalized output — skip
float3 viewDir = normalize(input.ViewDir);
float3 lightDir = _LightDirection;   // pre-normalized
float3 halfDir = normalize(viewDir + lightDir);  // must normalize (sum)
float3 worldNormal = normalize(input.Normal);    // must normalize (interpolation)
float3 reflectDir = reflect(-viewDir, worldNormal);  // already unit length
```

#### PERF P-04: Dependent Texture Read in Refraction (stall risk)

```hlsl
// CURRENT: UV for scene color read is computed in fragment shader
float2 refractionUV = screenUV + normal.xz * _RefractionStrength;
float3 sceneColor = SceneColorTexture.Sample(Sampler, refractionUV);
```

**Impact:** This is a dependent texture read — GPU cannot prefetch because
UV depends on prior computation. On mobile TBDR GPUs, this serializes the
entire fetch pipeline.

**Mitigation:** This pattern is inherent to refraction and cannot be fully
eliminated. Reduce cost by:
- Sample at half resolution (render refraction buffer at 50% res)
- Use `SampleLevel(refractionUV, 2.0)` to fetch from lower mip (cheaper memory access)

---

### 4. Variant Analysis

**Current Keywords:**
| Keyword | Purpose | Variants Added |
|---------|---------|---------------|
| _FOAM_ON | Enable foam rendering | x2 |
| _CAUSTICS_ON | Enable caustic projection | x2 |
| _SSR_ON | Screen-space reflections | x2 |
| _DEPTH_FOG | Underwater depth fog | x2 |
| _FLOW_MAP | UV flow animation | x2 |
| _TESSELLATION | Adaptive tessellation | x2 |

**Total Variants:** 2^6 = 64

**Assessment:** 64 variants is acceptable. However, review usage:
- `_TESSELLATION` is only used on PC high settings → separate shader recommended
- `_FLOW_MAP` and `_CAUSTICS_ON` are always enabled together → merge into single keyword

**Optimized:** 2^4 = 16 variants (main) + 16 variants (tessellation) = 32 total

---

### 5. Cross-Platform Compatibility

| Issue | Platform | Severity | Fix |
|-------|----------|----------|-----|
| `half` precision foam mask produces banding on Switch | Switch | Medium | Add dither pattern to foam edge |
| `SV_DepthLessEqual` not supported on Switch | Switch | High | Use `SV_Depth` with manual reverse-Z |
| Wave intrinsics used in caustic calc (SM 6.0) | Switch | High | Fallback path without `WaveReadLaneFirst` |
| `GatherRed` used but not available in GLSL ES 3.0 | WebGL | Low | Only affects web build (not a target) |
| Reflection probe fallback uses cubemap array | Switch | Medium | Limit to 2 probes, use individual cubemaps |

#### Switch-Specific Shader Variant

```hlsl
#if defined(PLATFORM_SWITCH)
    // Use half precision for all color calculations
    #define WATER_PRECISION half
    // Disable caustic wave intrinsics
    #define CAUSTICS_SIMPLE 1
    // Reduce normal map layers from 3 to 2
    #define NORMAL_LAYERS 2
    // Use simpler Fresnel (Schlick approximation, no pow)
    #define FRESNEL_FAST 1
#else
    #define WATER_PRECISION float
    #define CAUSTICS_SIMPLE 0
    #define NORMAL_LAYERS 3
    #define FRESNEL_FAST 0
#endif
```

---

### 6. Register Pressure Analysis

**Current VGPR Usage (compiled for AMD RDNA2 — PS5/Xbox):**

| Configuration | VGPRs | Occupancy | Assessment |
|---------------|-------|-----------|------------|
| All features ON | 52 | 6/10 waves | ⚠️ Below target |
| No tessellation | 44 | 8/10 waves | ✅ Acceptable |
| No foam, no caustics | 32 | 10/10 waves | ✅ Optimal |

**Current VGPR Usage (compiled for Tegra X1 — Switch):**

| Configuration | Registers | Assessment |
|---------------|-----------|------------|
| All features ON | 38 | ⚠️ High for mobile-class GPU |
| Switch variant (reduced) | 26 | ✅ Target range |

**Recommendations:**
- Ship the "No tessellation" variant as default on console (44 VGPRs)
- Ship the reduced Switch variant (26 registers)
- PC ultra can use the full 52 VGPR version

---

### 7. Summary of Recommendations

| # | Issue | Type | Priority | Est. Impact |
|---|-------|------|----------|-------------|
| 1 | C-01: Wave normal reconstruction | Correctness | P0 | Visual fix |
| 2 | C-03: NaN from Fresnel | Correctness | P0 | Black pixel fix |
| 3 | P-02: half precision (Switch) | Performance | P0 | +33% occupancy |
| 4 | Cross-platform: SM 6.0 fallback | Compatibility | P0 | Switch builds |
| 5 | P-01: Redundant texture samples | Performance | P1 | ~0.4ms saved |
| 6 | C-02: Foam sRGB | Correctness | P1 | Visual fix |
| 7 | P-03: Unnecessary normalize | Performance | P2 | ~8 ALU saved |
| 8 | Variant reduction (64→32) | Build time | P2 | 50% fewer compiles |
| 9 | P-04: Refraction half-res | Performance | P2 | ~0.2ms saved |

**Total Estimated GPU Savings:** 0.6-1.0ms on PS5 at 40% screen coverage
**Switch Impact:** Shader goes from unshippable (38 regs, artifacts) to
viable (26 regs, correct output)
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — Opens with specific shader review scope across languages and platforms
- ST-02 (Structured Sequential Instructions) — Numbered review workflow from structure through cross-platform verification
- RT-02 (Multi-Dimensional Analysis Framework) — Correctness, performance, registers, and compatibility analyzed separately
- RT-05 (Verification and Validation Steps) — Critical verification of compilation, precision, and visual correctness
- DS-03 (Tool and Methodology Suggestions) — GPU profiler usage, register analysis tools, variant counting

**Related Prompts:**
- `performance/performance_rendering_optimization.md` — Rendering pipeline optimization including shader complexity
- `performance/performance_frame_budget_analysis.md` — Overall frame budget context for shader costs
- `graphics/graphics_lighting_strategy.md` — Lighting shader design and optimization
