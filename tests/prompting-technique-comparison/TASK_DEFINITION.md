# Task Definition: Distributed Task Scheduler with Work-Stealing

## Overview

Implement a **distributed task scheduler** in Python (standard library only — `threading`, `queue`, `time`, `dataclasses`, `enum`, `logging`, `uuid`, `typing`) with the following subsystems:

## Requirements

### Core Components

1. **Task** — A unit of work with:
   - Unique ID (UUID)
   - Priority level (CRITICAL, HIGH, NORMAL, LOW)
   - Callable payload with arguments
   - Creation timestamp and TTL (time-to-live)
   - Max retry count
   - Current attempt count
   - Status (PENDING, RUNNING, COMPLETED, FAILED, EXPIRED, DEAD_LETTERED)

2. **PriorityTaskQueue** — Thread-safe priority queue:
   - Enqueue tasks respecting priority ordering
   - Dequeue returns highest priority task (CRITICAL first)
   - Within same priority, FIFO ordering
   - `peek()` without removing
   - `size()` and `is_empty()` methods
   - Timeout support on dequeue

3. **Worker** — Processing unit:
   - Runs in its own thread
   - Pulls tasks from its assigned queue
   - Can steal tasks from other workers' queues when idle
   - Reports task completion/failure back to scheduler
   - Handles task execution with timeout
   - Catches and isolates task exceptions (one bad task never crashes the worker)

4. **DeadLetterQueue (DLQ)** — Failed task storage:
   - Receives tasks that exceeded max retries
   - Stores failure reason and all attempt timestamps
   - Supports inspection (list all, filter by error type)
   - Optional: drain back to main queue for re-processing

5. **Scheduler** — Orchestrator:
   - Manages worker pool (configurable worker count)
   - Distributes tasks across worker queues (round-robin or least-loaded)
   - Handles task retry logic (exponential backoff)
   - Expires tasks past TTL before execution
   - Collects metrics (tasks submitted/completed/failed/expired, avg latency, queue depths)
   - Graceful shutdown: stop accepting new tasks, wait for in-flight tasks, then terminate

### Behavioral Requirements

- **Work-Stealing**: When a worker's queue is empty, it should attempt to steal from the busiest other worker's queue (steal from the back to reduce contention)
- **Retry Logic**: Failed tasks retry with exponential backoff (1s, 2s, 4s...) up to max_retries
- **TTL Expiration**: Tasks whose TTL has elapsed are marked EXPIRED and discarded (not retried)
- **Graceful Shutdown**: `scheduler.shutdown()` must:
  1. Stop accepting new tasks immediately
  2. Let in-flight tasks complete (with a configurable timeout)
  3. Move remaining queued tasks to a "not_started" list
  4. Shut down all worker threads
  5. Return a shutdown report (completed, failed, not_started counts)
- **Metrics**: Scheduler exposes `get_metrics()` returning a dict with at minimum:
  - `tasks_submitted`, `tasks_completed`, `tasks_failed`, `tasks_expired`
  - `tasks_dead_lettered`, `avg_latency_ms`, `worker_queue_depths`

### Edge Cases to Handle

- Task submitted after shutdown initiated → raise `SchedulerShutdownError`
- Task callable raises exception → catch, increment retry, re-queue or DLQ
- Worker thread dies unexpectedly → scheduler detects and restarts it
- All workers idle, no tasks → workers wait efficiently (no busy-spin)
- Work-stealing from empty queues → graceful no-op
- Concurrent submit from multiple threads → thread-safe
- Task with TTL=0 → immediately expired
- Task with max_retries=0 → goes to DLQ on first failure

## Deliverables

A single Python file (`scheduler.py`) containing:
- All classes listed above
- Type hints throughout
- A `if __name__ == "__main__"` demo block that:
  - Creates a scheduler with 4 workers
  - Submits 20 mixed-priority tasks (some that succeed, some that fail)
  - Includes at least one task with short TTL that will expire
  - Prints metrics mid-run and after shutdown
  - Demonstrates graceful shutdown

## Non-Requirements (Explicitly Out of Scope)

- No async/await (use threading only)
- No external packages
- No persistence/serialization
- No network communication (single-process only)
- No GUI or REST API
