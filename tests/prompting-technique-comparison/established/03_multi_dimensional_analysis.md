# Established Technique #3: Multi-Dimensional + Hierarchical Decomposition

> **Techniques used:** RT-02 (Multi-Dimensional Analysis), DT-01 (Hierarchical Task Breakdown), DT-04 (Layered Analysis), DS-06 (Prioritization Guidance)
> 
> The repo's approach for complex systems: decompose hierarchically, analyze from multiple angles, then implement layer by layer.

## Prompt (Single Turn)

```
# Distributed Task Scheduler — Multi-Dimensional Implementation

## Hierarchical Decomposition

Break this system into layers and implement each completely before moving 
to the next:

### Layer 1: Foundation (Data Model)
Implement these first — they have no dependencies:
- TaskPriority enum (CRITICAL, HIGH, NORMAL, LOW)
- TaskStatus enum (PENDING, RUNNING, COMPLETED, FAILED, EXPIRED, DEAD_LETTERED)
- Task dataclass (UUID, priority, callable + args, creation timestamp, TTL, 
  max_retries, attempt_count, status)
- SchedulerShutdownError exception
- DeadLetterEntry dataclass (task, failure_reason, attempt_timestamps)

### Layer 2: Data Structures (depends on Layer 1)
- PriorityTaskQueue: thread-safe priority queue
  - Priority ordering: CRITICAL > HIGH > NORMAL > LOW
  - FIFO within same priority
  - Methods: enqueue(task), dequeue(timeout) -> Optional[Task], peek(), 
    size(), is_empty()
  - Must use threading.Lock or threading.Condition for thread safety

### Layer 3: Processing (depends on Layers 1-2)
- Worker: task execution engine
  - Own thread via threading.Thread
  - Pulls from assigned PriorityTaskQueue
  - Work-stealing from other workers when idle (steal from busiest, from back)
  - Exception isolation (task failure ≠ worker death)
  - Callbacks to scheduler for completion/failure reporting

### Layer 4: Failure Handling (depends on Layers 1-3)
- DeadLetterQueue: terminal failure storage
  - Stores DeadLetterEntry with failure context
  - Methods: add(task, reason), list_all(), filter_by_error(type), drain() -> List[Task]
- Retry logic: exponential backoff (1s, 2s, 4s...), re-queue on failure, 
  DLQ when max_retries exceeded

### Layer 5: Orchestration (depends on all layers)
- Scheduler: system coordinator
  - Worker pool management (configurable count)
  - Task distribution (round-robin or least-loaded)
  - TTL expiration check before execution
  - Metrics collection (submitted/completed/failed/expired/dead_lettered, 
    avg_latency_ms, worker_queue_depths)
  - Graceful shutdown sequence

## Multi-Dimensional Analysis

For EACH layer, analyze from these 5 dimensions before implementing:

a. **Correctness**: What invariants must hold? What could violate them?
b. **Thread Safety**: What state is shared? What synchronization is needed?
c. **Failure Modes**: What can go wrong? How should each failure be handled?
d. **Performance**: What's the hot path? Any contention bottlenecks?
e. **Edge Cases**: What boundary conditions exist?

## Prioritized Edge Cases

Handle these in order of severity:

**P0 — Will crash the system:**
- Worker thread dies unexpectedly → detect and restart
- Task exception propagates to worker → catch and isolate
- Concurrent submit from multiple threads → thread-safe queue operations

**P1 — Will lose data or corrupt state:**
- Submit after shutdown → SchedulerShutdownError
- Work-stealing races with normal dequeue → proper locking
- Shutdown during in-flight tasks → wait with timeout

**P2 — Will cause incorrect behavior:**
- TTL=0 task → immediately mark EXPIRED
- max_retries=0 → DLQ on first failure
- Steal from empty queue → graceful no-op

**P3 — Will cause poor behavior:**
- All workers idle → efficient wait (Condition.wait, not sleep loop)
- Unbalanced queue depths → work-stealing should balance

## Deliverable

Single Python file. Standard library only. Type hints throughout.
Include `__main__` demo: 4 workers, 20 mixed tasks (success/fail/expire), 
mid-run metrics, graceful shutdown with report.
```

## What This Tests

- Does hierarchical decomposition with multi-dimensional analysis per layer improve architecture?
- Does prioritized edge-case ordering improve coverage?
- Compare against: Experimental #6 (Cognitive Load Separation) which also separates passes
