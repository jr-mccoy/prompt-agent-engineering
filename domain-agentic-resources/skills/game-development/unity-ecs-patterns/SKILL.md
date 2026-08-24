---
name: unity-ecs-patterns
description: Master Unity ECS (Entity Component System) with DOTS, Jobs, and Burst for high-performance game development. Use when building data-oriented games, optimizing performance, or working with large entity counts.
metadata:
  tags:
    - ecs
    - game-dev
    - performance
    - unity
  updated: "2026-04-11"
---
# Unity ECS Patterns

Production patterns for Unity's Data-Oriented Technology Stack (DOTS) including Entity Component System, Job System, and Burst Compiler.

## When to Use This Skill

- Building high-performance Unity games
- Managing thousands of entities efficiently
- Implementing data-oriented game systems
- Optimizing CPU-bound game logic
- Converting OOP game code to ECS
- Using Jobs and Burst for parallelization

## Core Concepts

### 1. ECS vs OOP

| Aspect | Traditional OOP | ECS/DOTS |
|--------|-----------------|----------|
| Data layout | Object-oriented | Data-oriented |
| Memory | Scattered | Contiguous |
| Processing | Per-object | Batched |
| Scaling | Poor with count | Linear scaling |
| Best for | Complex behaviors | Mass simulation |

### 2. DOTS Components

```
Entity: Lightweight ID (no data)
Component: Pure data (no behavior)
System: Logic that processes components
World: Container for entities
Archetype: Unique combination of components
Chunk: Memory block for same-archetype entities
```

## Patterns

### Pattern 1: Basic ECS Setup

```csharp
using Unity.Entities;
using Unity.Mathematics;
using Unity.Transforms;
using Unity.Burst;
using Unity.Collections;

// Component: Pure data, no methods
public struct Speed : IComponentData
{
    public float Value;
}

public struct Health : IComponentData
{
    public float Current;
    public float Max;
}

public struct Target : IComponentData
{
    public Entity Value;
}

// Tag component (zero-size marker)
public struct EnemyTag : IComponentData { }
public struct PlayerTag : IComponentData { }

// Buffer component (variable-size array)
[InternalBufferCapacity(8)]
public struct InventoryItem : IBufferElementData
{
    public int ItemId;
    public int Quantity;
}

// Shared component (grouped entities)
public struct TeamId : ISharedComponentData
{
    public int Value;
}
```

### Pattern 2: Systems with ISystem (Recommended)

```csharp
using Unity.Entities;
using Unity.Transforms;
using Unity.Mathematics;
using Unity.Burst;

// ISystem: Unmanaged, Burst-compatible, highest performance
[BurstCompile]
public partial struct MovementSystem : ISystem
{
    [BurstCompile]
    public void OnCreate(ref SystemState state)
    {
        // Require components before system runs
        state.RequireForUpdate<Speed>();
    }

    [BurstCompile]
    public void OnUpdate(ref SystemState state)
    {
        float deltaTime = SystemAPI.Time.DeltaTime;

        // Simple foreach - auto-generates job
        foreach (var (transform, speed) in
            SystemAPI.Query<RefRW<LocalTransform>, RefRO<Speed>>())
        {
            transform.ValueRW.Position +=
                new float3(0, 0, speed.ValueRO.Value * deltaTime);
        }
    }

    [BurstCompile]
    public void OnDestroy(ref SystemState state) { }
}

// With explicit job for more control
[BurstCompile]
public partial struct MovementJobSystem : ISystem
{
    [BurstCompile]
    public void OnUpdate(ref SystemState state)
    {
        var job = new MoveJob
        {
            DeltaTime = SystemAPI.Time.DeltaTime
        };

        state.Dependency = job.ScheduleParallel(state.Dependency);
    }
}

[BurstCompile]
public partial struct MoveJob : IJobEntity
{
    public float DeltaTime;

    void Execute(ref LocalTransform transform, in Speed speed)
    {
        transform.Position += new float3(0, 0, speed.Value * DeltaTime);
    }
}
```

### Pattern 3: Entity Queries

```csharp
[BurstCompile]
public partial struct QueryExamplesSystem : ISystem
{
    private EntityQuery _enemyQuery;

    public void OnCreate(ref SystemState state)
    {
        // Build query manually for complex cases
        _enemyQuery = new EntityQueryBuilder(Allocator.Temp)
            .WithAll<EnemyTag, Health, LocalTransform>()
            .WithNone<Dead>()
            .WithOptions(EntityQueryOptions.FilterWriteGroup)
            .Build(ref state);
    }

    [BurstCompile]
    public void OnUpdate(ref SystemState state)
    {
        // SystemAPI.Query - simplest approach
        foreach (var (health, entity) in
            SystemAPI.Query<RefRW<Health>>()
                .WithAll<EnemyTag>()
                .WithEntityAccess())
        {
            if (health.ValueRO.Current <= 0)
            {
                // Mark for destruction
                SystemAPI.GetSingleton<EndSimulationEntityCommandBufferSystem.Singleton>()
                    .CreateCommandBuffer(state.WorldUnmanaged)
                    .DestroyEntity(entity);
            }
        }

        // Get count
        int enemyCount = _enemyQuery.CalculateEntityCount();

        // Get all entities
        var enemies = _enemyQuery.ToEntityArray(Allocator.Temp);

        // Get component arrays
        var healths = _enemyQuery.ToComponentDataArray<Health>(Allocator.Temp);
    }
}
```

### Pattern 4: Entity Command Buffers (Structural Changes)

```csharp
// Structural changes (create/destroy/add/remove) require command buffers
[BurstCompile]
[UpdateInGroup(typeof(SimulationSystemGroup))]
public partial struct SpawnSystem : ISystem
{
    [BurstCompile]
    public void OnUpdate(ref SystemState state)
    {
        var ecbSingleton = SystemAPI.GetSingleton<BeginSimulationEntityCommandBufferSystem.Singleton>();
        var ecb = ecbSingleton.CreateCommandBuffer(state.WorldUnmanaged);

        foreach (var (spawner, transform) in
            SystemAPI.Query<RefRW<Spawner>, RefRO<LocalTransform>>())
        {
            spawner.ValueRW.Timer -= SystemAPI.Time.DeltaTime;

            if (spawner.ValueRO.Timer <= 0)
            {
                spawner.ValueRW.Timer = spawner.ValueRO.Interval;

                // Create entity (deferred until sync point)
                Entity newEntity = ecb.Instantiate(spawner.ValueRO.Prefab);

                // Set component values
                ecb.SetComponent(newEntity, new LocalTransform
                {
                    Position = transform.ValueRO.Position,
                    Rotation = quaternion.identity,
                    Scale = 1f
                });

                // Add component
                ecb.AddComponent(newEntity, new Speed { Value = 5f });
            }
        }
    }
}

// Parallel ECB usage
[BurstCompile]
public partial struct ParallelSpawnJob : IJobEntity
{
    public EntityCommandBuffer.ParallelWriter ECB;

    void Execute([EntityIndexInQuery] int index, in Spawner spawner)
    {
        Entity e = ECB.Instantiate(index, spawner.Prefab);
        ECB.AddComponent(index, e, new Speed { Value = 5f });
    }
}
```

## Advanced Patterns, Performance, and Resources

Patterns 5–8 (Aspect for grouping components, Singleton Components, Baking/Converting GameObjects, Jobs with Native Collections using `NativeParallelMultiHashMap`), Performance Tips (Burst everywhere, `IJobEntity`, `ScheduleParallel`, chunk iteration with `IJobChunk`, enableable components), and external resources (DOTS docs, samples, Burst guide).

See [references/advanced-patterns-performance-and-resources.md](references/advanced-patterns-performance-and-resources.md)

## Best Practices

### Do's
- **Use ISystem over SystemBase** - Better performance
- **Burst compile everything** - Massive speedup
- **Batch structural changes** - Use ECB
- **Profile with Profiler** - Identify bottlenecks
- **Use Aspects** - Clean component grouping

### Don'ts
- **Don't use managed types** - Breaks Burst
- **Don't structural change in jobs** - Use ECB
- **Don't over-architect** - Start simple
- **Don't ignore chunk utilization** - Group similar entities
- **Don't forget disposal** - Native collections leak

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/advanced-patterns-performance-and-resources.md` | Patterns 5–8 (Aspect, Singleton, Baking, Jobs with native collections), Performance Tips, and external resources |
