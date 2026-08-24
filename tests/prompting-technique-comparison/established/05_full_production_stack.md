# Established Technique #5: Full Production Stack

> **Techniques used:** CM-01 (Context Framing), CM-02 (Constraint Specification), DS-107 (Version-Specific Expertise), ST-16 (Behavioral Trait Declarations), QA-01 (Chain-of-Verification)
> 
> The repo's maximum-strength production prompt: full context, hard constraints, version pinning, behavioral declarations, and self-verification.

## Prompt (Single Turn)

```
# Production Task: Distributed Task Scheduler

## Context (CM-01)

You are implementing a core infrastructure component for a multi-threaded 
Python application. This scheduler will be used in production to manage 
background task processing with reliability guarantees. The system must 
handle concurrent task submission from multiple threads, graceful degradation 
under failure, and clean shutdown without task loss.

**Technology stack:**
- Python 3.10+ (use match/case if appropriate, walrus operator where it improves clarity)
- threading module (Thread, Lock, RLock, Condition, Event)
- queue module (PriorityQueue for internal use if helpful)
- dataclasses, enum, typing, uuid, time, logging
- NO external dependencies

**Operational context:**
- Expected load: 10-100 tasks/second
- Worker count: 2-16 (configurable)
- Task duration: 10ms to 30s
- Failure rate: ~5% of tasks fail
- Must support 24/7 operation without memory leaks

## Hard Constraints (CM-02)

**MUST:**
- [ ] All shared mutable state protected by locks (no unprotected reads)
- [ ] Lock ordering documented and enforced (prevent deadlocks)
- [ ] Every thread has a top-level exception handler
- [ ] Graceful shutdown completes within configurable timeout
- [ ] Thread-safe metrics collection
- [ ] Type hints on every function signature
- [ ] No busy-waiting (use Condition/Event, not sleep loops)
- [ ] No global state (all state in instances)

**MUST NOT:**
- [ ] No bare `except:` clauses (always catch specific exceptions)
- [ ] No daemon threads (all threads join on shutdown)
- [ ] No `time.sleep()` for synchronization (use proper primitives)
- [ ] No mutable default arguments

**SHOULD:**
- [ ] Prefer `with lock:` over manual acquire/release
- [ ] Use `time.monotonic()` not `time.time()` for durations
- [ ] Use `dataclasses` for data containers
- [ ] Use `enum.Enum` for fixed sets
- [ ] Prefix private attributes with underscore

## Behavioral Declarations (ST-16)

The code should exhibit these behaviors:
- **Defensive**: Assume any task callable can throw any exception at any time
- **Observable**: Every state transition is logged at appropriate level
- **Bounded**: Every wait has a timeout; every retry has a limit
- **Atomic**: Related state changes happen under the same lock
- **Recoverable**: Worker death is detected and worker is restarted

## Implementation Requirements

1. **Task** dataclass:
   - id: UUID, priority: TaskPriority enum, func: Callable, args: tuple, 
     kwargs: dict, created_at: float, ttl: Optional[float], max_retries: int, 
     attempt_count: int, status: TaskStatus enum

2. **PriorityTaskQueue**:
   - Thread-safe, priority-ordered (CRITICAL > HIGH > NORMAL > LOW)
   - FIFO within priority level
   - enqueue(task), dequeue(timeout) -> Optional[Task], peek(), size(), is_empty()

3. **Worker**:
   - Own thread, assigned queue
   - Work-stealing from busiest other worker (from back of their queue)
   - Exception isolation, completion/failure callbacks

4. **DeadLetterQueue**:
   - Stores failed tasks with reason + attempt timestamps
   - list_all(), filter_by_error(error_type), drain() -> List[Task]

5. **Scheduler**:
   - Worker pool (configurable count)
   - Task distribution (round-robin or least-loaded)
   - Retry: exponential backoff (1s, 2s, 4s...) up to max_retries
   - TTL: expire before execution
   - Metrics: submitted/completed/failed/expired/dead_lettered, avg_latency_ms, 
     worker_queue_depths via get_metrics() -> dict
   - Shutdown: stop accepting → wait in-flight (timeout) → collect unstarted → 
     join all → return ShutdownReport

6. **Edge cases**:
   - Submit after shutdown → SchedulerShutdownError
   - Task exception → catch, retry, DLQ
   - Worker death → detect, restart
   - Idle workers → Condition.wait() (not spin)
   - Empty steal → no-op
   - Concurrent submit → safe
   - TTL=0 → expired
   - max_retries=0 → DLQ immediately

## Verification Checklist (QA-01)

After implementation, walk through this checklist and cite specific code:

- [ ] Every `self._lock` protects exactly the state it should
- [ ] No path exists where shared state is accessed without a lock
- [ ] Lock ordering is consistent (no A→B in one path and B→A in another)
- [ ] Every `thread.join()` has a timeout
- [ ] Every `while` loop has an exit condition tied to shutdown
- [ ] Retry backoff is actually exponential, not linear
- [ ] TTL is checked against `time.monotonic()`, not `time.time()`
- [ ] Metrics counters are updated atomically
- [ ] `__main__` demo actually runs without errors

## Deliverable

Single Python file. Complete implementation. `__main__` demo: 4 workers, 
20 mixed tasks (success, failure, expiry), mid-run metrics, graceful shutdown.
```

## What This Tests

- Does the maximum-strength established technique stack match or beat experimental techniques?
- This represents the "best the repo can offer" — every technique is applied precisely
- Compare against: Experimental #1 (Pre-Commitment) and #7 (Recursive Self-Spec) which argue self-generated constraints are stronger
