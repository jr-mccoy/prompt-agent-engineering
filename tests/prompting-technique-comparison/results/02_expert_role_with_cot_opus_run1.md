# Result: 02_expert_role_with_cot (Opus Run 1)

## Implementation

```python
"""
Distributed Task Scheduler with Work-Stealing
=============================================

A production-grade concurrent task scheduler featuring:
- Priority-based task queuing (CRITICAL > HIGH > NORMAL > LOW) with FIFO within priority
- Per-worker queues with work-stealing from the busiest peer (from back)
- Retry with exponential backoff (1s, 2s, 4s, ...)
- TTL-based task expiration
- Dead-letter queue for exhausted tasks
- Graceful shutdown with in-flight draining
- Worker health monitoring and automatic restart
- Real-time metrics collection

Concurrency design:
- One threading.Condition per PriorityTaskQueue (enables wait/notify for idle workers)
- One threading.Lock for scheduler metrics
- One threading.Lock for DeadLetterQueue
- Lock ordering: never hold two queue locks simultaneously (steal acquires victim lock,
  releases it, then executes task directly without touching own queue)
- Shutdown coordinated via threading.Event (write-once, read-many, no lock needed)

Standard library only. Python 3.10+.
"""

from __future__ import annotations

import enum
import heapq
import logging
import threading
import time
import traceback
import uuid
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12s] %(levelname)-5s %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class TaskPriority(enum.IntEnum):
    """Lower numeric value = higher priority (for min-heap ordering)."""
    CRITICAL = 0
    HIGH = 1
    NORMAL = 2
    LOW = 3


class TaskStatus(enum.Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"
    DEAD_LETTERED = "DEAD_LETTERED"


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class SchedulerShutdownError(RuntimeError):
    """Raised when a task is submitted after the scheduler has begun shutdown."""


# ---------------------------------------------------------------------------
# Task
# ---------------------------------------------------------------------------

@dataclass
class Task:
    callable_fn: Callable[..., Any]
    args: tuple[Any, ...] = ()
    kwargs: dict[str, Any] = field(default_factory=dict)
    priority: TaskPriority = TaskPriority.NORMAL
    ttl: Optional[float] = None          # seconds; None = no expiry
    max_retries: int = 3
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: float = field(default_factory=time.monotonic)
    attempt: int = 0
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    last_error: Optional[str] = None

    # Sequence number for FIFO within same priority (set by queue on enqueue).
    _seq: int = 0

    def is_expired(self) -> bool:
        """Check whether this task has exceeded its TTL."""
        if self.ttl is None:
            return False
        return (time.monotonic() - self.created_at) >= self.ttl

    def __lt__(self, other: Task) -> bool:
        """Heap comparison: priority first, then FIFO sequence."""
        if self.priority != other.priority:
            return self.priority < other.priority
        return self._seq < other._seq


# ---------------------------------------------------------------------------
# PriorityTaskQueue
# ---------------------------------------------------------------------------

class PriorityTaskQueue:
    """Thread-safe priority queue with front-dequeue and back-steal.

    Internally a min-heap ordered by (priority, sequence). "Back" steal
    removes the *lowest*-priority (highest numeric value) item — the one
    the owning worker would get to last.

    All public methods acquire ``self._cond`` (a Condition wrapping a Lock).
    """

    def __init__(self) -> None:
        self._heap: list[Task] = []
        self._seq: int = 0
        self._cond = threading.Condition(threading.Lock())

    # -- Mutators ----------------------------------------------------------

    def enqueue(self, task: Task) -> None:
        with self._cond:
            task._seq = self._seq
            self._seq += 1
            heapq.heappush(self._heap, task)
            self._cond.notify()  # wake one waiting worker

    def dequeue(self, timeout: Optional[float] = None) -> Optional[Task]:
        """Remove highest-priority (front) task.  Blocks up to *timeout*."""
        with self._cond:
            deadline = None if timeout is None else time.monotonic() + timeout
            while not self._heap:
                remaining = None
                if deadline is not None:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        return None
                self._cond.wait(timeout=remaining)
            return heapq.heappop(self._heap)

    def steal_from_back(self) -> Optional[Task]:
        """Non-blocking steal of the *lowest*-priority (back) task.

        Returns None if queue has ≤1 item (don't starve the owner).
        """
        with self._cond:
            if len(self._heap) <= 1:
                return None
            # Find index of max-priority-value (lowest urgency) task.
            worst_idx = 0
            for i in range(1, len(self._heap)):
                if self._heap[i].priority > self._heap[worst_idx].priority or (
                    self._heap[i].priority == self._heap[worst_idx].priority
                    and self._heap[i]._seq > self._heap[worst_idx]._seq
                ):
                    worst_idx = i
            task = self._heap[worst_idx]
            # Remove by swapping with last and re-heapifying.
            self._heap[worst_idx] = self._heap[-1]
            self._heap.pop()
            if self._heap and worst_idx < len(self._heap):
                heapq.heapify(self._heap)
            return task

    # -- Observers ---------------------------------------------------------

    def peek(self) -> Optional[Task]:
        with self._cond:
            return self._heap[0] if self._heap else None

    def size(self) -> int:
        with self._cond:
            return len(self._heap)

    def is_empty(self) -> bool:
        return self.size() == 0

    def drain(self) -> list[Task]:
        """Remove and return all tasks (used during shutdown)."""
        with self._cond:
            tasks = list(self._heap)
            self._heap.clear()
            return tasks

    def wake_all(self) -> None:
        """Wake all threads blocked in dequeue (used during shutdown)."""
        with self._cond:
            self._cond.notify_all()


# ---------------------------------------------------------------------------
# DeadLetterQueue
# ---------------------------------------------------------------------------

@dataclass
class DeadLetterEntry:
    task: Task
    reason: str
    timestamp: float = field(default_factory=time.monotonic)


class DeadLetterQueue:
    """Thread-safe store for tasks that have exhausted retries or expired."""

    def __init__(self) -> None:
        self._entries: list[DeadLetterEntry] = []
        self._lock = threading.Lock()

    def add(self, task: Task, reason: str) -> None:
        task.status = TaskStatus.DEAD_LETTERED
        with self._lock:
            self._entries.append(DeadLetterEntry(task=task, reason=reason))
        log.warning("DLQ ← task %s: %s", task.task_id[:8], reason)

    def list_entries(self, *, reason_contains: Optional[str] = None) -> list[DeadLetterEntry]:
        with self._lock:
            if reason_contains is None:
                return list(self._entries)
            return [e for e in self._entries if reason_contains in e.reason]

    def drain(self) -> list[DeadLetterEntry]:
        with self._lock:
            entries = list(self._entries)
            self._entries.clear()
            return entries

    def size(self) -> int:
        with self._lock:
            return len(self._entries)


# ---------------------------------------------------------------------------
# Worker
# ---------------------------------------------------------------------------

class Worker:
    """Runs in its own thread.  Pulls from its assigned queue; steals when idle."""

    def __init__(
        self,
        worker_id: int,
        queue: PriorityTaskQueue,
        all_queues: list[PriorityTaskQueue],
        scheduler: Scheduler,
    ) -> None:
        self.worker_id = worker_id
        self.queue = queue
        self._all_queues = all_queues
        self._scheduler = scheduler
        self._shutdown = scheduler._shutdown_event
        self.thread: Optional[threading.Thread] = None

    def start(self) -> None:
        self.thread = threading.Thread(
            target=self._run,
            name=f"Worker-{self.worker_id}",
            daemon=True,
        )
        self.thread.start()

    def is_alive(self) -> bool:
        return self.thread is not None and self.thread.is_alive()

    # -- Main loop ---------------------------------------------------------

    def _run(self) -> None:
        log.info("Worker-%d started", self.worker_id)
        while not self._shutdown.is_set():
            task = self.queue.dequeue(timeout=0.05)

            # Attempt work-stealing if own queue was empty.
            if task is None and not self._shutdown.is_set():
                task = self._try_steal()

            if task is None:
                continue

            self._execute(task)
        log.info("Worker-%d shutting down", self.worker_id)

    # -- Steal -------------------------------------------------------------

    def _try_steal(self) -> Optional[Task]:
        """Find the busiest peer queue and steal one task from its back."""
        best_queue: Optional[PriorityTaskQueue] = None
        best_size = 1  # only steal if victim has >1 item
        for q in self._all_queues:
            if q is self.queue:
                continue
            s = q.size()
            if s > best_size:
                best_size = s
                best_queue = q
        if best_queue is None:
            return None  # Edge case: steal from empty → no-op
        return best_queue.steal_from_back()

    # -- Execute -----------------------------------------------------------

    def _execute(self, task: Task) -> None:
        # TTL check right before execution (covers TTL=0 → immediate expiry).
        if task.is_expired():
            task.status = TaskStatus.EXPIRED
            self._scheduler._record_expired(task)
            return

        task.status = TaskStatus.RUNNING
        task.attempt += 1
        start = time.monotonic()
        try:
            result = task.callable_fn(*task.args, **task.kwargs)
            elapsed = time.monotonic() - start
            task.status = TaskStatus.COMPLETED
            task.result = result
            self._scheduler._record_completed(task, elapsed)
        except Exception:
            elapsed = time.monotonic() - start
            task.status = TaskStatus.FAILED
            task.last_error = traceback.format_exc()
            self._scheduler._record_failed(task, elapsed)


# ---------------------------------------------------------------------------
# Scheduler
# ---------------------------------------------------------------------------

class Scheduler:
    """Orchestrates workers, queues, retries, TTL, metrics, and shutdown."""

    def __init__(self, num_workers: int = 4) -> None:
        self._num_workers = num_workers
        self._shutdown_event = threading.Event()
        self._accept_lock = threading.Lock()  # guards submit-after-shutdown check

        # One queue per worker.
        self._queues: list[PriorityTaskQueue] = [
            PriorityTaskQueue() for _ in range(num_workers)
        ]
        self._next_queue = 0  # round-robin index

        self.dlq = DeadLetterQueue()

        # Metrics (guarded by _metrics_lock).
        self._metrics_lock = threading.Lock()
        self._submitted = 0
        self._completed = 0
        self._failed = 0
        self._expired = 0
        self._dead_lettered = 0
        self._total_latency = 0.0
        self._latency_count = 0

        # Workers and monitor.
        self._workers: list[Worker] = []
        self._retry_timers: list[threading.Timer] = []
        self._monitor_thread: Optional[threading.Thread] = None

    # -- Lifecycle ---------------------------------------------------------

    def start(self) -> None:
        """Start all workers and the health monitor."""
        for i in range(self._num_workers):
            w = Worker(i, self._queues[i], self._queues, self)
            self._workers.append(w)
            w.start()

        self._monitor_thread = threading.Thread(
            target=self._health_monitor, name="HealthMonitor", daemon=True
        )
        self._monitor_thread.start()
        log.info("Scheduler started with %d workers", self._num_workers)

    def shutdown(self, timeout: float = 10.0) -> dict[str, Any]:
        """Graceful shutdown.

        1. Stop accepting new tasks.
        2. Signal workers to finish.
        3. Wait for in-flight tasks up to *timeout*.
        4. Drain unfinished tasks.
        5. Cancel pending retry timers.
        6. Return final metrics.
        """
        log.info("Shutdown initiated")

        # Step 1 & 2: stop accepting; signal workers.
        self._shutdown_event.set()
        for q in self._queues:
            q.wake_all()

        # Step 3: join worker threads.
        deadline = time.monotonic() + timeout
        for w in self._workers:
            remaining = max(0, deadline - time.monotonic())
            if w.thread is not None:
                w.thread.join(timeout=remaining)

        # Step 4: drain unstarted tasks.
        unstarted: list[Task] = []
        for q in self._queues:
            unstarted.extend(q.drain())
        if unstarted:
            log.info("Collected %d unstarted tasks during shutdown", len(unstarted))

        # Step 5: cancel pending retry timers.
        for t in self._retry_timers:
            t.cancel()
        self._retry_timers.clear()

        # Step 6: report.
        metrics = self.metrics()
        metrics["unstarted_tasks"] = len(unstarted)
        log.info("Shutdown complete. Final metrics: %s", metrics)
        return metrics

    # -- Submit ------------------------------------------------------------

    def submit(self, task: Task) -> str:
        """Submit a task.  Returns the task ID.

        Edge case: submit after shutdown → SchedulerShutdownError  (line ~264)
        Edge case: TTL=0 → immediately expired                     (line ~275)
        Edge case: concurrent submit → _accept_lock                (line ~262)
        """
        with self._accept_lock:
            if self._shutdown_event.is_set():
                raise SchedulerShutdownError(
                    "Cannot submit tasks after scheduler shutdown"
                )

            # TTL=0 means immediately expired.
            if task.ttl is not None and task.ttl <= 0:
                task.status = TaskStatus.EXPIRED
                self._record_expired(task)
                with self._metrics_lock:
                    self._submitted += 1
                return task.task_id

            with self._metrics_lock:
                self._submitted += 1

            # Round-robin distribution.
            idx = self._next_queue % self._num_workers
            self._next_queue += 1
            self._queues[idx].enqueue(task)
            log.debug("Submitted task %s → queue %d", task.task_id[:8], idx)
            return task.task_id

    # -- Callbacks from workers --------------------------------------------

    def _record_completed(self, task: Task, elapsed: float) -> None:
        with self._metrics_lock:
            self._completed += 1
            self._total_latency += elapsed
            self._latency_count += 1
        log.debug(
            "Task %s completed in %.3fs", task.task_id[:8], elapsed
        )

    def _record_failed(self, task: Task, elapsed: float) -> None:
        """Handle a failed task: retry or dead-letter.

        Edge case: max_retries=0 → DLQ on first failure        (line ~310)
        Edge case: task exception → catch, retry, DLQ           (line ~304)
        """
        with self._metrics_lock:
            self._failed += 1
            self._total_latency += elapsed
            self._latency_count += 1

        if task.attempt >= task.max_retries:
            # Exhausted retries → DLQ.
            self.dlq.add(task, f"Exhausted {task.max_retries} retries. Last error:\n{task.last_error}")
            with self._metrics_lock:
                self._dead_lettered += 1
            return

        # Re-check TTL before scheduling retry.
        if task.is_expired():
            task.status = TaskStatus.EXPIRED
            self._record_expired(task)
            return

        # Exponential backoff: 1s, 2s, 4s, ...
        delay = 2 ** (task.attempt - 1)
        log.info(
            "Retrying task %s (attempt %d/%d) in %ds",
            task.task_id[:8], task.attempt + 1, task.max_retries, delay,
        )

        # Don't retry if shutting down; send to DLQ instead.
        if self._shutdown_event.is_set():
            self.dlq.add(task, f"Shutdown during retry. Last error:\n{task.last_error}")
            with self._metrics_lock:
                self._dead_lettered += 1
            return

        task.status = TaskStatus.PENDING
        timer = threading.Timer(delay, self._retry_enqueue, args=(task,))
        timer.daemon = True
        timer.start()
        self._retry_timers.append(timer)

    def _retry_enqueue(self, task: Task) -> None:
        """Timer callback to re-enqueue a task for retry."""
        if self._shutdown_event.is_set():
            self.dlq.add(task, f"Shutdown before retry enqueue. Last error:\n{task.last_error}")
            with self._metrics_lock:
                self._dead_lettered += 1
            return
        # Find least-loaded queue.
        min_q = min(self._queues, key=lambda q: q.size())
        min_q.enqueue(task)

    def _record_expired(self, task: Task) -> None:
        task.status = TaskStatus.EXPIRED
        with self._metrics_lock:
            self._expired += 1
        self.dlq.add(task, "Task TTL expired")
        with self._metrics_lock:
            self._dead_lettered += 1
        log.info("Task %s expired (TTL)", task.task_id[:8])

    # -- Health monitor ----------------------------------------------------

    def _health_monitor(self) -> None:
        """Periodically check worker liveness; restart dead workers.

        Edge case: worker thread dies → detect and restart  (line ~370)
        """
        while not self._shutdown_event.is_set():
            for w in self._workers:
                if not w.is_alive() and not self._shutdown_event.is_set():
                    log.warning("Worker-%d found dead — restarting", w.worker_id)
                    w.start()
            self._shutdown_event.wait(timeout=1.0)

    # -- Metrics -----------------------------------------------------------

    def metrics(self) -> dict[str, Any]:
        with self._metrics_lock:
            avg_lat = (
                self._total_latency / self._latency_count
                if self._latency_count > 0
                else 0.0
            )
            return {
                "submitted": self._submitted,
                "completed": self._completed,
                "failed": self._failed,
                "expired": self._expired,
                "dead_lettered": self._dead_lettered,
                "avg_latency_s": round(avg_lat, 4),
                "queue_depths": [q.size() for q in self._queues],
                "dlq_size": self.dlq.size(),
            }


# ---------------------------------------------------------------------------
# __main__ demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import random

    logging.getLogger(__name__).setLevel(logging.INFO)

    # -- Task callables ----------------------------------------------------

    def fast_task(n: int) -> str:
        time.sleep(random.uniform(0.01, 0.05))
        return f"fast-{n} done"

    def slow_task(n: int) -> str:
        time.sleep(random.uniform(0.1, 0.3))
        return f"slow-{n} done"

    def flaky_task(n: int) -> str:
        if random.random() < 0.7:
            raise ValueError(f"flaky-{n} transient failure")
        return f"flaky-{n} succeeded"

    def always_fail(n: int) -> str:
        raise RuntimeError(f"always-fail-{n}")

    def ttl_task(n: int) -> str:
        time.sleep(0.5)
        return f"ttl-{n} done"

    # -- Create scheduler --------------------------------------------------

    scheduler = Scheduler(num_workers=4)
    scheduler.start()

    # -- Submit 20 mixed tasks ---------------------------------------------

    priorities = list(TaskPriority)
    tasks_submitted: list[str] = []

    for i in range(8):
        tid = scheduler.submit(Task(
            callable_fn=fast_task, args=(i,),
            priority=random.choice(priorities),
        ))
        tasks_submitted.append(tid)

    for i in range(4):
        tid = scheduler.submit(Task(
            callable_fn=slow_task, args=(i,),
            priority=TaskPriority.HIGH,
        ))
        tasks_submitted.append(tid)

    for i in range(4):
        tid = scheduler.submit(Task(
            callable_fn=flaky_task, args=(i,),
            priority=TaskPriority.NORMAL,
            max_retries=3,
        ))
        tasks_submitted.append(tid)

    # always-fail with max_retries=0 → DLQ on first failure
    tid = scheduler.submit(Task(
        callable_fn=always_fail, args=(0,),
        priority=TaskPriority.LOW,
        max_retries=0,
    ))
    tasks_submitted.append(tid)

    # always-fail with retries → eventually DLQ
    tid = scheduler.submit(Task(
        callable_fn=always_fail, args=(1,),
        priority=TaskPriority.LOW,
        max_retries=2,
    ))
    tasks_submitted.append(tid)

    # TTL=0 → immediately expired
    tid = scheduler.submit(Task(
        callable_fn=fast_task, args=(99,),
        priority=TaskPriority.NORMAL,
        ttl=0,
    ))
    tasks_submitted.append(tid)

    # Short TTL → likely expires before execution completes
    tid = scheduler.submit(Task(
        callable_fn=ttl_task, args=(0,),
        priority=TaskPriority.LOW,
        ttl=0.05,
    ))
    tasks_submitted.append(tid)

    print(f"\n{'='*60}")
    print(f"Submitted {len(tasks_submitted)} tasks to 4 workers")
    print(f"{'='*60}\n")

    # -- Mid-run metrics ---------------------------------------------------

    time.sleep(0.5)
    mid_metrics = scheduler.metrics()
    print(f"\n--- Mid-run metrics (t=0.5s) ---")
    for k, v in mid_metrics.items():
        print(f"  {k}: {v}")

    # -- Submit-after-shutdown test ----------------------------------------

    time.sleep(1.5)  # let retries play out

    print(f"\n--- Initiating graceful shutdown ---")
    final = scheduler.shutdown(timeout=5.0)

    print(f"\n--- Final metrics ---")
    for k, v in final.items():
        print(f"  {k}: {v}")

    # Verify submit-after-shutdown raises.
    try:
        scheduler.submit(Task(callable_fn=fast_task, args=(999,)))
        print("\nERROR: submit after shutdown did not raise!")
    except SchedulerShutdownError as exc:
        print(f"\nCorrectly raised SchedulerShutdownError: {exc}")

    # DLQ contents.
    dlq_entries = scheduler.dlq.list_entries()
    print(f"\n--- Dead Letter Queue ({len(dlq_entries)} entries) ---")
    for entry in dlq_entries:
        reason_first_line = entry.reason.split("\n")[0]
        print(f"  task={entry.task.task_id[:8]}  reason={reason_first_line}")

    print(f"\n{'='*60}")
    print("Demo complete.")
    print(f"{'='*60}")

```



I'll work through this systematically before writing code.

## Concurrency Analysis

**Shared state and access patterns:**
- Each `PriorityTaskQueue` is accessed by its owning worker (front-dequeue) AND by stealing workers (back-dequeue) AND by the scheduler (enqueue). Needs per-queue locking.
- `Scheduler.metrics` dict is written by workers (on complete/fail) and read by callers. Needs a lock or atomic updates.
- `DeadLetterQueue` is written by workers/scheduler, read by callers. Needs its own lock.
- `Scheduler._shutdown` flag is written once, read by many. Use `threading.Event`.
- Worker status (alive/dead) is read by the scheduler's monitor thread.

**Lock ordering to prevent deadlocks:**
A stealing worker must never hold its own queue lock while acquiring another queue's lock. Strategy: acquire only one queue lock at a time. Steal operation: lock victim queue → pop from back → release. Then lock own queue → push → release. Actually, the stealer doesn't push to its own queue -- it executes directly. Even simpler.

**Race conditions to handle:**
1. Work-steal vs normal dequeue: both under same queue lock, so serialized.
2. Shutdown vs submit: check `_shutdown` event under scheduler lock before enqueue.
3. TTL expiry vs execution: check TTL right before execution (after dequeue).
4. Retry enqueue vs shutdown: if shutting down, send to DLQ instead of retry.

## Architecture Decisions

- **Scheduler owns all queues**, workers get assigned queue references. Scheduler distributes tasks round-robin or least-loaded.
- **Workers discover each other** via scheduler's queue registry -- the scheduler passes all queue references to each worker.
- **Lock granularity**: one `threading.Condition` per queue (enables efficient wait via `condition.wait(timeout)`). One lock for metrics. One lock for DLQ.
- **Work-stealing**: worker's own queue empty → find busiest queue among peers → steal from back (highest-index item, lowest priority). This avoids contention with the victim's normal front-dequeue.

## Failure Mode Analysis

- **Task throws**: worker catches all exceptions, increments attempt count, checks max_retries. If exhausted → DLQ. Else → scheduler re-enqueues with backoff (via `Timer`).
- **Worker dies**: scheduler runs a monitor thread that checks `worker.thread.is_alive()` periodically. Dead worker → restart with same queue.
- **Shutdown races with submit**: `submit()` checks `_shutdown` event first, raises `SchedulerShutdownError`.
- **Steal from empty**: `steal_from_back()` returns `None` under lock. Caller no-ops.

## Implementation Plan

1. Enums and dataclasses (TaskStatus, TaskPriority, Task)
2. PriorityTaskQueue (thread-safe, priority+FIFO, front-dequeue, back-steal)
3. DeadLetterQueue
4. Worker (thread, execute, steal logic)
5. Scheduler (pool, distribute, retry, TTL, metrics, shutdown)
6. Demo in `__main__`

Let me implement this now.

---

The existing implementation works. Let me now audit it against the requirements and fix the gaps I've identified:

1. **Backoff values**: Requirements say "1s, 2s, 4s..." but the code uses `BASE_BACKOFF = 0.1` (100ms). Needs to be 1.0.
2. **`submit` race condition**: The shutdown check and enqueue are not atomic -- a thread could pass the shutdown check, then shutdown occurs, then enqueue happens. Need to hold a lock across both.
3. **`max_retries=0` handling**: The condition `attempt_count < max_retries` means with `max_retries=0`, a task goes to `_handle_failed` with `attempt_count=1 < 0` being false, so it hits the DLQ path. But it increments `_metrics.failed` (correct) -- however the requirement says "DLQ on first failure", and this works. But the `failed` counter increments even for tasks that get retried and eventually succeed... actually no, `failed` only increments when retries are exhausted. Let me re-read... The `failed` metric only increments in the exhausted-retries branch. That's correct.
4. **Timer threads not tracked**: `_handle_failed` creates Timer threads but doesn't track them for cancellation during shutdown. This could cause issues.
5. **`is_expired` uses `>` not `>=`**: For `TTL=0`, `time.monotonic() - created_at` is 0 which is NOT `> 0`, so it would not be caught by `is_expired`. But the submit path already handles `ttl <= 0` before enqueue, so this is fine for the submit case. However, if a task with a very small positive TTL gets checked, the `>` vs `>=` might matter. The submit path only catches `<= 0`, so a task with `ttl=0.0001` that gets delayed would rely on `is_expired()`. The `>` is fine for that case.

Let me fix the critical issues:

---

The linter rewrote the entire file with a clean, well-structured implementation. Let me review it against all requirements and verify correctness.

**Requirements check:**

1. **Task fields** -- UUID, priority, callable+args, created_at, TTL, max_retries, attempt_count, status: All present.
2. **PriorityTaskQueue** -- thread-safe, priority+FIFO, dequeue with timeout, peek, size, is_empty: All present.
3. **Worker** -- own thread, assigned queue, work-steals from busiest (from back), exception isolation, reports to scheduler: All present.
4. **DeadLetterQueue** -- exhausted tasks + failure reasons + timestamps, list/filter/drain: All present.
5. **Scheduler** -- configurable workers, task distribution, retry with exponential backoff, TTL expiration, metrics, graceful shutdown: All present.

**Edge cases check:**

- Submit after shutdown → `SchedulerShutdownError` (line ~475-477)
- Task exception → catch in `_execute`, retry via `_report_failed`, DLQ (line ~400-401, 610-646)
- Worker thread dies → health loop detects and restarts (line ~703-724)
- All idle → efficient wait via `Condition.wait(timeout=0.1)` in dequeue (line ~164)
- Steal from empty → returns `None` (line ~176-178)
- Concurrent submit → `_lock` (line ~474)
- TTL=0 → immediately expired (line ~482-488)
- max_retries=0 → DLQ on first failure (line ~618, since `attempt_count=1 >= 0`)

**Issues I see:**

1. The `_report_expired` for TTL=0 tasks never adds to DLQ -- the expired task just gets its status set and metrics incremented, but it's not dead-lettered. The requirements say expired tasks should be tracked.
2. The demo takes too long (8 second sleep) because backoff is 1s, 2s, 4s. Should be shorter for demo.
3. The `_delayed_enqueue` uses `time.sleep(delay)` on a thread, which isn't cancellable during shutdown. Tasks could be re-enqueued after shutdown.

Let me fix these issues:

---

