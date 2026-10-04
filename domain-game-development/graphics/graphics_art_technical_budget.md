---
title: "Art Direction to Technical Budget — Per-Asset-Class Triangle, Texture, Material and VFX Budgets Derived from Platform Limits"
category: game-development/graphics
description: "Turn an art direction and a platform's memory and frame limits into budgets artists can build to before content exists: name where fidelity matters most, compute texture memory per asset class from resolution, compression and mips, set triangle counts per LOD with screen-size switch points, cap materials per asset so draw calls fit, set texel density and VFX overdraw rules, and check the scene totals against the platform with headroom — distinct from optimising a pipeline that is already over budget."
techniques:
  - NE-11
  - DS-02
  - DP-06
  - RT-23
difficulty: advanced
tags:
  - technical-art
  - asset-budgets
  - texture-memory
  - lod
  - draw-calls
  - texel-density
  - how-many-polygons
  - art-wont-fit-in-memory
  - setting-art-budgets
updated: "2026-10-03"
related_prompts:
  - domain-game-development/performance/performance_rendering_optimization.md
  - domain-game-development/performance/performance_frame_budget_analysis.md
  - domain-game-development/graphics/graphics_lighting_strategy.md
---

# Art Direction to Technical Budget

**Objective:** Give the art team numbers to build to — per asset class and per scene
— that follow from the platform's limits and from the art direction's own priorities,
so fidelity is spent where the game's look depends on it and the content fits before
anyone has to cut it.

**When to Use:**
- Pre-production or early production: art direction is set and asset creation is
  about to scale up.
- Artists ask "how many triangles?" or "what texture size?" and get different
  answers from different people.
- A new platform target or performance mode needs a budget sheet before content is
  re-authored.
- **Not this prompt if** the game is already over budget and you are profiling the
  frame to cut cost — use
  `domain-game-development/performance/performance_rendering_optimization.md` (draw
  calls, culling, streaming in an existing build) or
  `domain-game-development/performance/performance_frame_budget_analysis.md` (where
  the milliseconds go). For light counts, shadows and GI, use
  `domain-game-development/graphics/graphics_lighting_strategy.md`.

## Inputs / Context

1. **Art direction**: style, camera distance and type, what the look depends on
   (faces, silhouettes, materials, vistas, effects), reference images.
2. **Platform limits** from engineering: texture streaming pool or memory budget,
   main-pass draw-call budget, visible-triangle budget, target frame rate. Mark each
   `[data]` if measured, `[estimate]` if not.
3. **Content plan**: asset classes and counts per level or scene (characters,
   enemies, modular kit, props, vegetation, terrain, VFX).
4. **Engine features** that change the maths: virtualised geometry, texture
   streaming, instancing, compression formats supported `[verify against current docs]`.
5. **Material model**: texture maps per material (albedo, normal, packed masks).

## Method

1. **Name the dominant driver (DP-06).** One sentence: where does this game's look
   live? Every allocation below favours it; everything else is a candidate for reuse,
   trim sheets and tiling.
2. **Set the standards (DS-02).** Texel density per class (pixels per metre at the
   expected camera distance), maps per material, compression per map type, maximum
   texture size per class, materials per asset, LOD count and screen-size switch points.
3. **Compute texture memory (NE-11).**
   `bytes = width × height × bytes per pixel × 1.33 (full mip chain)`.
   Block compression reference: 4 bits/pixel (e.g. BC1) or 8 bits/pixel (e.g. BC5,
   BC7; ASTC 4×4) `[verify against current docs]`. Sum per material set, then per class.
4. **Allocate the pool.** Class totals against the streaming pool or memory budget,
   with headroom for streaming churn (state the percentage). Over budget → cut the
   classes furthest from the dominant driver first.
5. **Set geometry budgets.** Triangles per LOD per class, with the screen size at
   which each LOD switches; visible-triangle estimate for a typical and a worst
   scene. With virtualised geometry, budget memory and overdraw instead of LOD counts.
6. **Set draw-call budgets.** `main-pass draws ≈ Σ visible instances × materials per
   instance` (instanced batches count once). Check a typical and worst scene against
   the budget; shadow passes are a separate line `[measure]`.
7. **Set VFX rules.** Maximum screen coverage of overlapping transparent layers,
   particle counts per effect, texture sheet sizes.
8. **Tag and enforce (RT-23).** Every budget marked `[data]`, `[estimate]` or
   `[guess]`; the guesses become the first profiling captures. Specify the pipeline
   checks (import validators, review gates) that hold artists to the sheet.

## Output Format

```
# Art technical budget — [game]   Platform/mode: [..]   Dominant driver: [..]

## Platform limits        — limit | value | provenance
## Standards              — texel density | maps per material | compression | max texture | LODs
## Texture memory         — class | count | set size | MiB each | MiB total
## Pool allocation        — total vs pool | headroom | cuts made
## Geometry               — class | LOD0 / LOD1 / LOD2 tris | switch screen size
## Draw calls             — class | visible instances | materials | draws | total vs budget
## VFX rules
## Enforcement            — validator / gate per rule
## Open items             — every [guess], with the capture that replaces it
```

## Verification

- [ ] The dominant driver is named and the allocation visibly favours it.
- [ ] Every texture figure is reproducible from resolution, bytes per pixel and 1.33.
- [ ] Class totals sum to the stated pool use and headroom.
- [ ] Draw-call totals follow from stated instances and materials.
- [ ] Every platform limit and budget carries provenance.
- [ ] Every rule has an enforcement point.

## False-Positive Prevention

1. **A budget is not a quota.** Assets under budget are fine; do not pad them.
2. **Uniform budgets waste fidelity.** Equal sizes for every class ignore the
   dominant driver; unequal allocation is the point.
3. **Worst-case residency is conservative.** Streaming rarely holds every top mip;
   say whether the sheet assumes worst case.
4. **Engine features change the maths.** Virtualised geometry and texture streaming
   alter what to budget; check the engine's current documentation before applying LOD
   counts or pool sizes from another project.
5. **Do not invent platform numbers.** Pool sizes and draw-call budgets come from
   engineering's measurements; mark anything else `[guess]`.

## Example Output

**Input:** Third-person action game, console at 60 fps. Engineering: texture
streaming pool 2,048 MiB `[estimate]`, main-pass draw calls ≤ 3,000 `[data]`.
Art direction: cinematic close-ups of four hero characters; stylised environments.

```
# Art technical budget — action game   Console 60 fps   Dominant driver: hero faces

## Standards
Env texel density 512 px/m; maps per material: albedo, normal, packed ORM.
Compression: albedo BC1 (BC7 if alpha or hero), normal BC5, ORM BC1.
Set size (1.33 mips): 4096 hero = 21.33 + 21.33 + 10.67 = 53.33 MiB;
2048 (BC7 albedo) = 5.33 + 5.33 + 2.67 = 13.33; 2048 (BC1) = 2.67 + 5.33 + 2.67 = 10.67;
1024 (BC1) = 2.67.

## Texture memory
| Class | Count | Set | MiB each | MiB total |
| Hero characters | 4 | head 4096 + body 2048 BC7 | 66.67 | 266.7 |
| Enemies | 6 | 2048 BC7 | 13.33 | 80.0 |
| Env tiling materials | 40 | 2048 BC1 | 10.67 | 426.7 |
| Props, standard | 120 | 1024 | 2.67 | 320.0 |
| Props, hero | 30 → 10 | 2048 BC1 | 10.67 | 320.0 → 106.7 |
| Props, demoted | 0 → 20 | 1024 | 2.67 | 0 → 53.3 |
| Vegetation atlases | 20 | 2048 BC7 | 13.33 | 266.7 |
| VFX | — | — | — | 64.0 |
| Terrain + decals | — | — | — | 150.0 |

## Pool allocation
Before: 1,894.1 MiB of 2,048 = 92.5% (headroom 7.5%; rule ≥ 15%).
Cut furthest from the driver: 20 hero props → 1024. After: 1,734.1 MiB = 84.7% (15.3% headroom).
Hero faces untouched.

## Geometry
| Hero | 80k / 40k / 12k | LOD1 < 40% screen height, LOD2 < 10% |
| Enemy | 30k / 12k / 4k | 30% / 8% |
| Prop | ≤ 5k / 1.5k | 10% |

## Draw calls (typical courtyard)
| Kit pieces | 900 | 1.5 | 1,350 |
| Props | 600 | 1.2 | 720 |
| Vegetation (instanced) | 40 batches | 1 | 40 |
| Characters | 16 | 4 | 64 |
| VFX | — | — | 150 |
| Total | | | 2,324 of 3,000 (77.5%) — shadows [measure] |

## VFX rules
≤ 4 overlapping transparent layers over 25% of screen; sprite sheets ≤ 1024.

## Enforcement
Import validator: max texture size per class folder, compression per map suffix,
material count per mesh; weekly memory report per level.

## Open items
Pool 2,048 MiB [estimate] → confirm on devkit; shadow-pass draws [measure].
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — texture bytes with mips, pool totals and draw-call sums.
- **DS-02 Metric Specification** — texel density, LOD switch points and per-class caps as artist-facing standards.
- **DP-06 Dominant Driver Identification** — the one place fidelity is spent first, which orders every cut.
- **RT-23 Input Provenance Tagging** — data, estimate and guess labels that become the first profiling captures.

## Related Prompts

- `domain-game-development/performance/performance_rendering_optimization.md` — cutting cost once a build exists.
- `domain-game-development/performance/performance_frame_budget_analysis.md` — where the frame's milliseconds come from.
- `domain-game-development/graphics/graphics_lighting_strategy.md` — lighting's share of the same budgets.
