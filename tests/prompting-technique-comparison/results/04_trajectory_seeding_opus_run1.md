# Result: 04_trajectory_seeding (Opus Run 1)

## Implementation

```python
"""
Distributed Task Scheduler with Work-Stealing

Concurrency design:
    Shared mutable state          Guarded by              Access pattern
    -----------------------------------------------------------------------
    PriorityTaskQueue._heap       self._lock (per-queue)  owner dequeue (front), thieves steal (back), scheduler enqueue
    Worker._stop_event            threading.Event          scheduler writes, worker reads
    Scheduler._metrics            _metrics_lock            workers write (callback), caller reads
    DeadLetterQueue._entries      self._lock               scheduler/workers write, caller reads
    Scheduler._shutdown_event     threading.Event          shutdown writes once, submit reads

    Lock ordering: only ONE queue lock is ever held at a time.
    Steal: release own lock -> acquire victim lock -> release victim lock.
    No nested queue locks => no deadlock.
"""

from __future__ import annotations

import heapq
import logging
import math
import threading
import time
import traceback
import uuid
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Callable, Dict, List, Optional, Tuple

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("scheduler")


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class Priority(Enum):
    CRITICAL = 0
    HIGH = 1
    NORMAL = 2
    LOW = 3


class TaskStatus(Enum):
    PENDING = auto()
    RUNNING = auto()
    COMPLETED = auto()
    FAILED = auto()
    EXPIRED = auto()
    DEAD_LETTERED = auto()


# ---------------------------------------------------------------------------
# Task
# ---------------------------------------------------------------------------

@dataclass
class Task:
    callable_fn: Callable[..., Any]
    args: Tuple[Any, ...] = ()
    kwargs: Dict[str, Any] = field(default_factory=dict)
    priority: Priority = Priority.NORMAL
    ttl: Optional[float] = None          # seconds; None = no expiry
    max_retries: int = 3
    task_id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: float = field(default_factory=time.monotonic)
    attempt_count: int = 0
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    last_error: Optional[str] = None

    # Sequence counter for FIFO ordering within the same priority.
    _seq: int = field(default=0, repr=False)

    def is_expired(self) -> bool:
        if self.ttl is None:
            return False
        return (time.monotonic() - self.created_at) > self.ttl


# Global monotonic sequence for FIFO tie-breaking.
_global_seq_lock = threading.Lock()
_global_seq = 0


def _next_seq() -> int:
    global _global_seq
    with _global_seq_lock:
        _global_seq += 1
        return _global_seq


# ---------------------------------------------------------------------------
# PriorityTaskQueue  (thread-safe, min-heap by (priority, seq))
# ---------------------------------------------------------------------------

class PriorityTaskQueue:
    """Thread-safe priority queue. Lower Priority ordinal = higher urgency."""

    def __init__(self) -> None:
        self._heap: List[Tuple[int, int, Task]] = []   # (priority_val, seq, task)
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)

    def enqueue(self, task: Task) -> None:
        seq = _next_seq()
        task._seq = seq
        with self._not_empty:
            heapq.heappush(self._heap, (task.priority.value, seq, task))
            self._not_empty.notify()

    def dequeue(self, timeout: Optional[float] = None) -> Optional[Task]:
        """Remove highest-priority (lowest ordinal) task. Blocks up to *timeout* seconds."""
        with self._not_empty:
            deadline = None if timeout is None else time.monotonic() + timeout
            while not self._heap:
                remaining = None
                if deadline is not None:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        return None
                self._not_empty.wait(timeout=remaining)
                # Re-check after wakeup; may be spurious or due to shutdown notify.
                if not self._heap:
                    if deadline is not None and time.monotonic() >= deadline:
                        return None
            _, _, task = heapq.heappop(self._heap)
            return task

    def steal_from_back(self) -> Optional[Task]:
        """Non-blocking steal of the LOWEST-priority item (back of queue)."""
        with self._lock:
            if not self._heap:
                return None
            # Find and remove the max (lowest-priority, highest seq) element.
            # O(n) but queues are small; avoids a second data-structure.
            max_idx = 0
            for i in range(1, len(self._heap)):
                if self._heap[i] > self._heap[max_idx]:
                    max_idx = i
            entry = self._heap[max_idx]
            self._heap[max_idx] = self._heap[-1]
            self._heap.pop()
            if self._heap and max_idx < len(self._heap):
                heapq.heapify(self._heap)  # restore heap after swap
            return entry[2]

    def peek(self) -> Optional[Task]:
        with self._lock:
            if self._heap:
                return self._heap[0][2]
            return None

    def size(self) -> int:
        with self._lock:
            return len(self._heap)

    def is_empty(self) -> bool:
        return self.size() == 0

    def drain(self) -> List[Task]:
        """Remove and return all tasks (used during shutdown)."""
        with self._lock:
            tasks = [entry[2] for entry in self._heap]
            self._heap.clear()
            return tasks

    def notify_all_waiters(self) -> None:
        """Wake up any threads blocked in dequeue (used for shutdown)."""
        with self._not_empty:
            self._not_empty.notify_all()


# ---------------------------------------------------------------------------
# DeadLetterQueue
# ---------------------------------------------------------------------------

@dataclass
class DeadLetterEntry:
    task: Task
    reason: str
    timestamp: float = field(default_factory=time.monotonic)


class DeadLetterQueue:
    def __init__(self) -> None:
        self._entries: List[DeadLetterEntry] = []
        self._lock = threading.Lock()

    def put(self, task: Task, reason: str) -> None:
        task.status = TaskStatus.DEAD_LETTERED
        with self._lock:
            self._entries.append(DeadLetterEntry(task=task, reason=reason))

    def list_all(self) -> List[DeadLetterEntry]:
        with self._lock:
            return list(self._entries)

    def filter_by_status(self, status: TaskStatus) -> List[DeadLetterEntry]:
        with self._lock:
            return [e for e in self._entries if e.task.status == status]

    def drain(self) -> List[DeadLetterEntry]:
        with self._lock:
            entries = list(self._entries)
            self._entries.clear()
            return entries

    def size(self) -> int:
        with self._lock:
            return len(self._entries)


# ---------------------------------------------------------------------------
# Scheduler errors
# ---------------------------------------------------------------------------

class SchedulerShutdownError(RuntimeError):
    """Raised when a task is submitted after the scheduler has begun shutdown."""


# ---------------------------------------------------------------------------
# Worker
# ---------------------------------------------------------------------------

class Worker:
    """Runs on its own thread. Pulls from its assigned queue; steals when idle."""

    DEQUEUE_TIMEOUT = 0.25   # seconds to wait before attempting a steal
    STEAL_COOLDOWN = 0.05    # brief pause between steal attempts

    def __init__(
        self,
        worker_id: int,
        own_queue: PriorityTaskQueue,
        all_queues: List[PriorityTaskQueue],
        dead_letter_queue: DeadLetterQueue,
        on_task_complete: Callable[[Task], None],
        on_task_failed: Callable[[Task, str], None],
    ) -> None:
        self.worker_id = worker_id
        self._queue = own_queue
        self._all_queues = all_queues
        self._dlq = dead_letter_queue
        self._on_complete = on_task_complete
        self._on_failed = on_task_failed
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None

    def start(self) -> None:
        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._run, name=f"Worker-{self.worker_id}", daemon=True,
        )
        self._thread.start()

    def stop(self) -> None:
        self._stop_event.set()
        self._queue.notify_all_waiters()

    def join(self, timeout: Optional[float] = None) -> None:
        if self._thread is not None:
            self._thread.join(timeout=timeout)

    @property
    def is_alive(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    # ---- internal -----------------------------------------------------------

    def _run(self) -> None:
        logger.debug("Worker-%d started", self.worker_id)
        while not self._stop_event.is_set():
            task = self._queue.dequeue(timeout=self.DEQUEUE_TIMEOUT)
            if task is None and not self._stop_event.is_set():
                task = self._try_steal()
            if task is not None:
                self._execute(task)
        logger.debug("Worker-%d stopped", self.worker_id)

    def _try_steal(self) -> Optional[Task]:
        """Steal from the busiest OTHER queue."""
        best_queue: Optional[PriorityTaskQueue] = None
        best_size = 0
        for q in self._all_queues:
            if q is self._queue:
                continue
            sz = q.size()
            if sz > best_size:
                best_size = sz
                best_queue = q
        if best_queue is not None and best_size > 1:
            stolen = best_queue.steal_from_back()
            if stolen is not None:
                logger.debug(
                    "Worker-%d stole task %s", self.worker_id, stolen.task_id,
                )
                return stolen
        time.sleep(self.STEAL_COOLDOWN)
        return None

    def _execute(self, task: Task) -> None:
        # TTL check
        if task.is_expired():
            task.status = TaskStatus.EXPIRED
            self._on_failed(task, "TTL expired before execution")
            return

        task.status = TaskStatus.RUNNING
        task.attempt_count += 1
        try:
            task.result = task.callable_fn(*task.args, **task.kwargs)
            task.status = TaskStatus.COMPLETED
            self._on_complete(task)
        except Exception:
            tb = traceback.format_exc()
            task.status = TaskStatus.FAILED
            task.last_error = tb
            self._on_failed(task, tb)


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

@dataclass
class SchedulerMetrics:
    submitted: int = 0
    completed: int = 0
    failed: int = 0
    retried: int = 0
    expired: int = 0
    dead_lettered: int = 0
    total_latency: float = 0.0    # sum of (completion_time - created_at)
    _completed_count_for_avg: int = 0

    @property
    def avg_latency(self) -> float:
        if self._completed_count_for_avg == 0:
            return 0.0
        return self.total_latency / self._completed_count_for_avg


# ---------------------------------------------------------------------------
# Scheduler
# ---------------------------------------------------------------------------

class DistributionStrategy(Enum):
    ROUND_ROBIN = auto()
    LEAST_LOADED = auto()


class Scheduler:
    BASE_BACKOFF = 0.1   # seconds
    MAX_BACKOFF = 5.0    # seconds

    def __init__(
        self,
        num_workers: int = 4,
        strategy: DistributionStrategy = DistributionStrategy.LEAST_LOADED,
    ) -> None:
        self._num_workers = num_workers
        self._strategy = strategy
        self._shutdown_event = threading.Event()
        self._dlq = DeadLetterQueue()
        self._metrics = SchedulerMetrics()
        self._metrics_lock = threading.Lock()

        # One queue per worker.
        self._queues: List[PriorityTaskQueue] = [
            PriorityTaskQueue() for _ in range(num_workers)
        ]
        self._workers: List[Worker] = [
            Worker(
                worker_id=i,
                own_queue=self._queues[i],
                all_queues=self._queues,
                dead_letter_queue=self._dlq,
                on_task_complete=self._handle_complete,
                on_task_failed=self._handle_failed,
            )
            for i in range(num_workers)
        ]

        self._rr_counter = 0
        self._rr_lock = threading.Lock()

        # Start workers.
        for w in self._workers:
            w.start()

        # Watchdog thread to detect and restart dead workers.
        self._watchdog_stop = threading.Event()
        self._watchdog_thread = threading.Thread(
            target=self._watchdog, name="Watchdog", daemon=True,
        )
        self._watchdog_thread.start()

    # ---- public API ---------------------------------------------------------

    def submit(self, task: Task) -> uuid.UUID:
        if self._shutdown_event.is_set():
            raise SchedulerShutdownError("Cannot submit: scheduler is shutting down")

        # TTL=0 means immediately expired.
        if task.ttl is not None and task.ttl <= 0:
            task.status = TaskStatus.EXPIRED
            with self._metrics_lock:
                self._metrics.submitted += 1
                self._metrics.expired += 1
            self._dlq.put(task, "TTL was 0 or negative at submission time")
            return task.task_id

        queue = self._pick_queue()
        queue.enqueue(task)
        with self._metrics_lock:
            self._metrics.submitted += 1
        return task.task_id

    def get_metrics(self) -> dict:
        with self._metrics_lock:
            m = self._metrics
            return {
                "submitted": m.submitted,
                "completed": m.completed,
                "failed": m.failed,
                "retried": m.retried,
                "expired": m.expired,
                "dead_lettered": m.dead_lettered,
                "avg_latency": round(m.avg_latency, 4),
                "queue_depths": [q.size() for q in self._queues],
            }

    @property
    def dead_letter_queue(self) -> DeadLetterQueue:
        return self._dlq

    def shutdown(self, timeout: float = 10.0) -> dict:
        """Graceful shutdown.

        1. Stop accepting new tasks.
        2. Signal workers to finish current task then stop.
        3. Join worker threads.
        4. Drain remaining tasks from queues.
        5. Return final report.
        """
        logger.info("Scheduler shutdown initiated")
        self._shutdown_event.set()

        # Stop watchdog.
        self._watchdog_stop.set()

        # Signal all workers.
        for w in self._workers:
            w.stop()

        # Join workers with timeout.
        deadline = time.monotonic() + timeout
        for w in self._workers:
            remaining = max(0.0, deadline - time.monotonic())
            w.join(timeout=remaining)

        # Drain unstarted tasks.
        unstarted: List[Task] = []
        for q in self._queues:
            unstarted.extend(q.drain())

        final_metrics = self.get_metrics()
        final_metrics["unstarted_tasks"] = len(unstarted)
        final_metrics["dead_letter_size"] = self._dlq.size()

        logger.info("Scheduler shutdown complete: %s", final_metrics)
        return final_metrics

    # ---- callbacks from workers (called on worker threads) -------------------

    def _handle_complete(self, task: Task) -> None:
        latency = time.monotonic() - task.created_at
        with self._metrics_lock:
            self._metrics.completed += 1
            self._metrics.total_latency += latency
            self._metrics._completed_count_for_avg += 1

    def _handle_failed(self, task: Task, reason: str) -> None:
        if task.status == TaskStatus.EXPIRED:
            with self._metrics_lock:
                self._metrics.expired += 1
            self._dlq.put(task, reason)
            return

        # Retry?
        if task.attempt_count < task.max_retries:
            backoff = min(
                self.BASE_BACKOFF * math.pow(2, task.attempt_count - 1),
                self.MAX_BACKOFF,
            )
            with self._metrics_lock:
                self._metrics.retried += 1
            task.status = TaskStatus.PENDING
            # Schedule retry after backoff (non-blocking).
            threading.Timer(backoff, self._resubmit, args=(task,)).start()
        else:
            # Exhausted retries -> DLQ.
            with self._metrics_lock:
                self._metrics.failed += 1
                self._metrics.dead_lettered += 1
            self._dlq.put(task, reason)

    def _resubmit(self, task: Task) -> None:
        if self._shutdown_event.is_set():
            self._dlq.put(task, "Scheduler shut down before retry")
            return
        queue = self._pick_queue()
        queue.enqueue(task)

    # ---- internals ----------------------------------------------------------

    def _pick_queue(self) -> PriorityTaskQueue:
        if self._strategy == DistributionStrategy.ROUND_ROBIN:
            with self._rr_lock:
                idx = self._rr_counter % self._num_workers
                self._rr_counter += 1
            return self._queues[idx]
        else:
            # Least-loaded.
            min_size = float("inf")
            best = self._queues[0]
            for q in self._queues:
                sz = q.size()
                if sz < min_size:
                    min_size = sz
                    best = q
            return best

    def _watchdog(self) -> None:
        """Periodically check workers; restart any that have died."""
        while not self._watchdog_stop.wait(timeout=1.0):
            for i, w in enumerate(self._workers):
                if not w.is_alive and not self._shutdown_event.is_set():
                    logger.warning("Worker-%d found dead, restarting", i)
                    new_worker = Worker(
                        worker_id=i,
                        own_queue=self._queues[i],
                        all_queues=self._queues,
                        dead_letter_queue=self._dlq,
                        on_task_complete=self._handle_complete,
                        on_task_failed=self._handle_failed,
                    )
                    new_worker.start()
                    self._workers[i] = new_worker


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def _demo() -> None:
    import random

    def good_task(task_num: int) -> str:
        time.sleep(random.uniform(0.05, 0.2))
        return f"task-{task_num} done"

    def flaky_task(task_num: int) -> str:
        time.sleep(random.uniform(0.02, 0.1))
        if random.random() < 0.6:
            raise ValueError(f"flaky-{task_num} transient failure")
        return f"flaky-{task_num} succeeded"

    def bad_task(task_num: int) -> str:
        raise RuntimeError(f"bad-{task_num} always fails")

    scheduler = Scheduler(num_workers=4, strategy=DistributionStrategy.LEAST_LOADED)

    priorities = [Priority.CRITICAL, Priority.HIGH, Priority.NORMAL, Priority.LOW]

    # Submit 20 mixed tasks.
    for i in range(20):
        if i < 12:
            fn, args = good_task, (i,)
        elif i < 17:
            fn, args = flaky_task, (i,)
        else:
            fn, args = bad_task, (i,)

        ttl = None
        max_retries = 3
        if i == 5:
            ttl = 0           # immediately expired
        if i == 18:
            max_retries = 0   # DLQ on first failure

        task = Task(
            callable_fn=fn,
            args=args,
            priority=random.choice(priorities),
            ttl=ttl,
            max_retries=max_retries,
        )
        tid = scheduler.submit(task)
        logger.info("Submitted task %d -> %s (priority=%s, ttl=%s, max_retries=%d)",
                     i, tid, task.priority.name, ttl, max_retries)

    # Test submit-after-shutdown error (deferred to after normal submissions).
    # Mid-run metrics.
    time.sleep(0.5)
    print("\n=== Mid-run Metrics ===")
    for k, v in scheduler.get_metrics().items():
        print(f"  {k}: {v}")

    # Let tasks finish.
    time.sleep(3.0)

    # Graceful shutdown.
    print("\n=== Initiating Graceful Shutdown ===")
    report = scheduler.shutdown(timeout=5.0)
    print("\n=== Final Shutdown Report ===")
    for k, v in report.items():
        print(f"  {k}: {v}")

    # DLQ contents.
    dlq_entries = scheduler.dead_letter_queue.list_all()
    if dlq_entries:
        print(f"\n=== Dead Letter Queue ({len(dlq_entries)} entries) ===")
        for entry in dlq_entries:
            reason_first_line = entry.reason.strip().split("\n")[-1]
            print(f"  Task {entry.task.task_id} | attempts={entry.task.attempt_count} | {reason_first_line}")

    # Verify submit-after-shutdown raises.
    try:
        scheduler.submit(Task(callable_fn=lambda: None))
        print("\nERROR: SchedulerShutdownError was not raised!")
    except SchedulerShutdownError as exc:
        print(f"\nCorrectly raised SchedulerShutdownError: {exc}")


if __name__ == "__main__":
    _demo()

```



I'll start by mapping out the shared mutable state and concurrency design before implementing.

**Shared State Analysis:**
1. `PriorityTaskQueue._queue` (list) — accessed by owning worker (front) + stealing workers (back) + scheduler (enqueue) → needs per-queue lock
2. `Worker._running` flag — written by scheduler, read by worker thread → use `threading.Event`
3. `Scheduler._metrics` — written by workers (via callback), read by caller → needs its own lock
4. `DeadLetterQueue._tasks` — written by scheduler/workers, read by caller → needs its own lock
5. `Scheduler._queues` list — written once at init, read by all workers for stealing → immutable after init, safe
6. `Scheduler._shutdown` — written once by shutdown, read by submit → use `threading.Event`
7. `Task.status`, `Task.attempt_count` — mutated by worker holding the task; only one worker ever holds a task → no lock needed

**Lock ordering (to prevent deadlock):** Workers only ever hold ONE queue lock at a time. Steal operation: release own lock, then acquire victim lock. No nested queue locks.

---

Everything runs cleanly. The demo shows all the expected behaviors: successful tasks, retried flaky tasks, DLQ for exhausted tasks, TTL=0 immediate expiry, max_retries=0 immediate DLQ, and the submit-after-shutdown error.

The file is at `/home/user/Prompting-guides/distributed_task_scheduler.py`.

**Architecture summary:**

- **Shared state and locking:** Each `PriorityTaskQueue` has its own `threading.Lock` (used via a `Condition` for blocking dequeue). Metrics have a separate `_metrics_lock`. DLQ has its own lock. Only one queue lock is ever held at a time, preventing deadlocks.

- **PriorityTaskQueue:** Min-heap keyed on `(priority_value, sequence_number)`. FIFO within same priority via the global monotonic sequence counter. `dequeue()` blocks with timeout using `Condition.wait()`. `steal_from_back()` is non-blocking and takes the lowest-priority item.

- **Worker:** Each worker owns one queue, dequeues from it with a 250ms timeout, then attempts to steal from the busiest other queue if idle. Exception isolation via try/except in `_execute()`. Reports results to scheduler via callbacks.

- **Work-stealing:** Workers scan all other queues, pick the largest, and steal from its back (lowest-priority item). Steal only happens when the victim has >1 item. A 50ms cooldown after failed steals prevents busy-spinning.

- **Scheduler:** Distributes tasks via least-loaded or round-robin strategy. Retries use exponential backoff via `threading.Timer`. A watchdog thread detects and restarts dead workers. Graceful shutdown: set shutdown flag, signal workers, join threads, drain queues, return report.

- **Edge cases handled:** TTL=0 (immediate expiry at submit), max_retries=0 (DLQ on first failure), submit after shutdown (raises `SchedulerShutdownError`), empty steal (no-op with cooldown), concurrent submit (thread-safe via queue locks).

---

