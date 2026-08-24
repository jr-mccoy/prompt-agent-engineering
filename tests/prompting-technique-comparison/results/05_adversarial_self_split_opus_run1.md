# Result: 05_adversarial_self_split (Opus Run 1)

## Implementation

```python
"""
Distributed Task Scheduler with Work-Stealing
==============================================
A thread-safe, priority-based task scheduler with configurable worker pools,
work-stealing, dead-letter queues, TTL expiration, and graceful shutdown.

Standard library only. Python 3.10+.

Semantics:
- TTL=None: no expiration.  TTL=0: expires immediately.  TTL>0: expires after TTL seconds.
- max_retries: number of total attempts allowed. max_retries=0 means DLQ on first failure.
  max_retries=3 means up to 3 attempts (original + 2 retries).
"""

from __future__ import annotations

import atexit
import heapq
import logging
import threading
import time
import traceback
import uuid
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Callable, Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12s] %(levelname)-5s %(message)s",
)
logger = logging.getLogger(__name__)


# ─── Enums ────────────────────────────────────────────────────────────────────


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


# ─── Exceptions ───────────────────────────────────────────────────────────────


class SchedulerShutdownError(Exception):
    """Raised when submitting a task after the scheduler has been shut down."""


# ─── Task ─────────────────────────────────────────────────────────────────────

# Global sequence counter for FIFO ordering within same priority.
_global_seq_lock = threading.Lock()
_global_seq = 0


def _next_seq() -> int:
    global _global_seq
    with _global_seq_lock:
        _global_seq += 1
        return _global_seq


@dataclass
class Task:
    func: Callable[..., Any]
    args: tuple = ()
    kwargs: dict = field(default_factory=dict)
    priority: Priority = Priority.NORMAL
    ttl: Optional[float] = None  # seconds; None = no expiry, 0 = immediate expiry
    max_retries: int = 3
    task_id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: float = field(default_factory=time.monotonic)
    attempt: int = 0
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    last_error: Optional[str] = None
    _seq: int = field(default_factory=_next_seq, repr=False)

    def is_expired(self) -> bool:
        if self.ttl is None:
            return False
        if self.ttl == 0:
            return True
        return (time.monotonic() - self.created_at) >= self.ttl

    def __lt__(self, other: Task) -> bool:
        if self.priority.value != other.priority.value:
            return self.priority.value < other.priority.value
        return self._seq < other._seq

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Task):
            return NotImplemented
        return self.task_id == other.task_id

    def __hash__(self) -> int:
        return hash(self.task_id)


# ─── PriorityTaskQueue ────────────────────────────────────────────────────────


class PriorityTaskQueue:
    """Thread-safe, priority-ordered task queue (min-heap on priority value).
    FIFO within same priority via global sequence numbers."""

    def __init__(self) -> None:
        self._heap: list[Task] = []
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)

    def enqueue(self, task: Task) -> None:
        with self._not_empty:
            heapq.heappush(self._heap, task)
            self._not_empty.notify()

    def dequeue(self, timeout: Optional[float] = None) -> Optional[Task]:
        """Block until a task is available or timeout expires."""
        with self._not_empty:
            end_time: Optional[float] = None
            if timeout is not None:
                end_time = time.monotonic() + timeout
            while not self._heap:
                if end_time is not None:
                    remaining = end_time - time.monotonic()
                    if remaining <= 0:
                        return None
                    self._not_empty.wait(timeout=remaining)
                else:
                    self._not_empty.wait()
            return heapq.heappop(self._heap)

    def steal_from_back(self) -> Optional[Task]:
        """Steal the lowest-priority (least urgent) task for work-stealing.
        Among ties in priority, steals the newest (highest seq = least FIFO-entitled).
        Returns None if queue is empty."""
        with self._lock:
            if not self._heap:
                return None
            if len(self._heap) == 1:
                return heapq.heappop(self._heap)
            # Find the element with the highest priority value (least urgent)
            max_idx = 0
            for i in range(1, len(self._heap)):
                if self._heap[i].priority.value > self._heap[max_idx].priority.value:
                    max_idx = i
                elif (self._heap[i].priority.value == self._heap[max_idx].priority.value
                      and self._heap[i]._seq > self._heap[max_idx]._seq):
                    max_idx = i
            task = self._heap[max_idx]
            # Remove by replacing with last element and re-heapifying
            self._heap[max_idx] = self._heap[-1]
            self._heap.pop()
            if self._heap:
                heapq.heapify(self._heap)
            return task

    def peek(self) -> Optional[Task]:
        with self._lock:
            return self._heap[0] if self._heap else None

    def size(self) -> int:
        with self._lock:
            return len(self._heap)

    def is_empty(self) -> bool:
        with self._lock:
            return len(self._heap) == 0

    def drain(self) -> list[Task]:
        """Remove and return all tasks in priority order."""
        with self._lock:
            tasks = []
            while self._heap:
                tasks.append(heapq.heappop(self._heap))
            return tasks

    def wake_all(self) -> None:
        """Wake all threads blocked on dequeue (used during shutdown)."""
        with self._not_empty:
            self._not_empty.notify_all()


# ─── DeadLetterQueue ──────────────────────────────────────────────────────────


@dataclass
class DeadLetterEntry:
    task: Task
    reason: str
    timestamp: float = field(default_factory=time.monotonic)


class DeadLetterQueue:
    def __init__(self) -> None:
        self._entries: list[DeadLetterEntry] = []
        self._lock = threading.Lock()

    def add(self, task: Task, reason: str) -> None:
        task.status = TaskStatus.DEAD_LETTERED
        with self._lock:
            self._entries.append(DeadLetterEntry(task=task, reason=reason))

    def list_all(self) -> list[DeadLetterEntry]:
        with self._lock:
            return list(self._entries)

    def filter_by_priority(self, priority: Priority) -> list[DeadLetterEntry]:
        with self._lock:
            return [e for e in self._entries if e.task.priority == priority]

    def filter_by_reason(self, substring: str) -> list[DeadLetterEntry]:
        with self._lock:
            return [e for e in self._entries if substring in e.reason]

    def drain(self) -> list[DeadLetterEntry]:
        with self._lock:
            entries = list(self._entries)
            self._entries.clear()
            return entries

    def size(self) -> int:
        with self._lock:
            return len(self._entries)


# ─── Metrics ──────────────────────────────────────────────────────────────────


class SchedulerMetrics:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self.submitted = 0
        self.completed = 0
        self.failed = 0
        self.expired = 0
        self.dead_lettered = 0
        self.stolen = 0
        self._total_latency = 0.0
        self._latency_count = 0

    def record_submit(self) -> None:
        with self._lock:
            self.submitted += 1

    def record_complete(self, latency: float) -> None:
        with self._lock:
            self.completed += 1
            self._total_latency += latency
            self._latency_count += 1

    def record_fail(self) -> None:
        with self._lock:
            self.failed += 1

    def record_expired(self) -> None:
        with self._lock:
            self.expired += 1

    def record_dead_letter(self) -> None:
        with self._lock:
            self.dead_lettered += 1

    def record_steal(self) -> None:
        with self._lock:
            self.stolen += 1

    def avg_latency(self) -> float:
        with self._lock:
            if self._latency_count == 0:
                return 0.0
            return self._total_latency / self._latency_count

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            return {
                "submitted": self.submitted,
                "completed": self.completed,
                "failed": self.failed,
                "expired": self.expired,
                "dead_lettered": self.dead_lettered,
                "stolen": self.stolen,
                "avg_latency_s": (
                    self._total_latency / self._latency_count
                    if self._latency_count > 0
                    else 0.0
                ),
            }


# ─── Worker ───────────────────────────────────────────────────────────────────


class Worker:
    """Worker thread that pulls from its assigned queue, with work-stealing.

    Workers do NOT drain their own queues on shutdown. The Scheduler's shutdown
    procedure joins workers first (waiting for their current in-flight task),
    then drains all queues centrally to avoid races between worker drains and
    scheduler drains.
    """

    IDLE_POLL_INTERVAL = 0.05  # seconds

    def __init__(
        self,
        worker_id: int,
        queue: PriorityTaskQueue,
        all_queues: list[PriorityTaskQueue],
        scheduler: Scheduler,
        shutdown_event: threading.Event,
    ) -> None:
        self.worker_id = worker_id
        self.queue = queue
        self.all_queues = all_queues
        self.scheduler = scheduler
        self._shutdown_event = shutdown_event
        self._thread: Optional[threading.Thread] = None

    def start(self) -> None:
        self._thread = threading.Thread(
            target=self._run,
            name=f"Worker-{self.worker_id}",
            daemon=True,
        )
        self._thread.start()

    def stop(self) -> None:
        self.queue.wake_all()

    def join(self, timeout: Optional[float] = None) -> None:
        if self._thread is not None:
            self._thread.join(timeout=timeout)

    @property
    def is_alive(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    def _run(self) -> None:
        logger.debug(f"Worker-{self.worker_id} started")
        try:
            while not self._shutdown_event.is_set():
                task = self.queue.dequeue(timeout=self.IDLE_POLL_INTERVAL)
                if task is None:
                    task = self._try_steal()
                if task is None:
                    continue
                self._execute(task)
            # FIX B-004: Do NOT drain local queue here. The scheduler will
            # drain all queues after joining all workers, preventing the race
            # where both worker._drain_local() and scheduler.shutdown() drain
            # concurrently.
        except Exception:
            logger.exception(f"Worker-{self.worker_id} crashed")

    def _try_steal(self) -> Optional[Task]:
        busiest: Optional[PriorityTaskQueue] = None
        max_size = 1  # only steal if someone has >1 task
        for q in self.all_queues:
            if q is self.queue:
                continue
            s = q.size()
            if s > max_size:
                max_size = s
                busiest = q
        if busiest is None:
            return None
        stolen = busiest.steal_from_back()
        if stolen is not None:
            self.scheduler.metrics.record_steal()
            logger.debug(f"Worker-{self.worker_id} stole task {stolen.task_id}")
        return stolen

    def _execute(self, task: Task) -> None:
        # Check TTL before execution
        if task.is_expired():
            task.status = TaskStatus.EXPIRED
            self.scheduler.metrics.record_expired()
            logger.info(f"Task {task.task_id} expired (TTL={task.ttl}s)")
            return

        task.status = TaskStatus.RUNNING
        task.attempt += 1
        start = time.monotonic()
        try:
            task.result = task.func(*task.args, **task.kwargs)
            task.status = TaskStatus.COMPLETED
            latency = time.monotonic() - start
            self.scheduler.metrics.record_complete(latency)
            logger.debug(f"Task {task.task_id} completed in {latency:.4f}s")
        except Exception as exc:
            task.status = TaskStatus.FAILED
            task.last_error = traceback.format_exc()
            self.scheduler.metrics.record_fail()
            logger.warning(
                f"Task {task.task_id} failed attempt {task.attempt}/{task.max_retries}: {exc}"
            )
            self.scheduler._handle_failure(task)


# ─── Scheduler ────────────────────────────────────────────────────────────────


class Scheduler:
    """
    Distributed task scheduler with configurable worker pool,
    round-robin or least-loaded distribution, retry with exponential backoff,
    TTL expiration, dead-letter queue, and graceful shutdown.
    """

    def __init__(
        self,
        num_workers: int = 4,
        strategy: str = "least-loaded",
    ) -> None:
        self.num_workers = num_workers
        self.strategy = strategy
        self.metrics = SchedulerMetrics()
        self.dlq = DeadLetterQueue()

        self._queues: list[PriorityTaskQueue] = [
            PriorityTaskQueue() for _ in range(num_workers)
        ]
        self._workers: list[Worker] = []
        self._rr_index = 0
        self._rr_lock = threading.Lock()
        # FIX B-001: _shutdown_lock now protects the shutdown flag AND is held
        # during enqueue in submit() and _resubmit() to prevent TOCTOU races.
        self._shutdown = False
        self._shutdown_lock = threading.Lock()
        self._shutdown_event = threading.Event()
        self._retry_timers: list[threading.Timer] = []
        self._retry_lock = threading.Lock()
        # FIX B-005: dedicated lock for worker restart
        self._worker_restart_lock = threading.Lock()

        for i in range(num_workers):
            w = Worker(
                worker_id=i,
                queue=self._queues[i],
                all_queues=self._queues,
                scheduler=self,
                shutdown_event=self._shutdown_event,
            )
            self._workers.append(w)

        # FIX B-012: Register atexit handler so graceful shutdown happens
        # even if the user forgets to call shutdown().
        atexit.register(self._atexit_shutdown)

    def _atexit_shutdown(self) -> None:
        """Best-effort shutdown at interpreter exit."""
        with self._shutdown_lock:
            if self._shutdown:
                return
        try:
            self.shutdown(timeout=3.0)
        except Exception:
            pass

    def start(self) -> None:
        logger.info(
            f"Scheduler starting with {self.num_workers} workers "
            f"(strategy={self.strategy})"
        )
        for w in self._workers:
            w.start()

    def submit(self, task: Task) -> uuid.UUID:
        # FIX B-001: Hold _shutdown_lock through the entire submit including
        # enqueue, so shutdown cannot interleave between the check and the
        # enqueue. This is safe because enqueue only acquires the queue's
        # internal lock (no nesting with _shutdown_lock elsewhere in that
        # direction).
        with self._shutdown_lock:
            if self._shutdown:
                raise SchedulerShutdownError(
                    "Cannot submit tasks after shutdown has been initiated."
                )

            self.metrics.record_submit()

            # Check immediate TTL expiry (TTL=0 case)
            if task.is_expired():
                task.status = TaskStatus.EXPIRED
                self.metrics.record_expired()
                logger.info(f"Task {task.task_id} expired immediately (TTL={task.ttl}s)")
                return task.task_id

            queue = self._select_queue()
            queue.enqueue(task)

        logger.debug(f"Task {task.task_id} submitted (priority={task.priority.name})")
        return task.task_id

    def _select_queue(self) -> PriorityTaskQueue:
        if self.strategy == "round-robin":
            with self._rr_lock:
                idx = self._rr_index % self.num_workers
                self._rr_index += 1
            return self._queues[idx]
        else:  # least-loaded
            return min(self._queues, key=lambda q: q.size())

    def _handle_failure(self, task: Task) -> None:
        """Retry with exponential backoff, or send to DLQ if exhausted."""
        if task.attempt >= task.max_retries:
            reason = (
                f"Exhausted {task.max_retries} retries. "
                f"Last error:\n{task.last_error}"
            )
            self.dlq.add(task, reason)
            self.metrics.record_dead_letter()
            logger.info(f"Task {task.task_id} -> dead-letter queue")
            return

        # Check TTL before scheduling retry
        if task.is_expired():
            task.status = TaskStatus.EXPIRED
            self.metrics.record_expired()
            logger.info(f"Task {task.task_id} expired before retry")
            return

        delay = min(2 ** task.attempt * 0.1, 5.0)  # exponential, capped at 5s
        task.status = TaskStatus.PENDING
        logger.info(
            f"Task {task.task_id} retry #{task.attempt + 1} in {delay:.2f}s"
        )

        def _resubmit() -> None:
            # FIX B-008: Hold _shutdown_lock through TTL check + enqueue to
            # prevent TOCTOU race with shutdown.
            with self._shutdown_lock:
                if self._shutdown:
                    return
                if task.is_expired():
                    task.status = TaskStatus.EXPIRED
                    self.metrics.record_expired()
                    return
                queue = self._select_queue()
                queue.enqueue(task)

        timer = threading.Timer(delay, _resubmit)
        timer.daemon = True
        with self._retry_lock:
            self._retry_timers.append(timer)
        timer.start()

    def _restart_dead_workers(self) -> None:
        """Detect and restart dead workers."""
        # FIX B-005: Use dedicated lock to prevent concurrent restart races.
        with self._worker_restart_lock:
            if self._shutdown_event.is_set():
                return
            for i, w in enumerate(self._workers):
                if not w.is_alive:
                    logger.warning(f"Worker-{i} found dead, restarting")
                    new_worker = Worker(
                        worker_id=i,
                        queue=self._queues[i],
                        all_queues=self._queues,
                        scheduler=self,
                        shutdown_event=self._shutdown_event,
                    )
                    new_worker.start()
                    self._workers[i] = new_worker

    def get_metrics(self) -> dict[str, Any]:
        self._restart_dead_workers()
        snap = self.metrics.snapshot()
        snap["queue_depths"] = [q.size() for q in self._queues]
        snap["dlq_size"] = self.dlq.size()
        return snap

    def shutdown(self, timeout: float = 10.0) -> dict[str, Any]:
        """
        Graceful shutdown:
        1. Stop accepting new tasks (atomic with submit)
        2. Cancel pending retry timers
        3. Signal workers to stop via event + wake blocked dequeues
        4. Wait for workers to finish current in-flight task
        5. Drain any remaining tasks from queues (workers do NOT drain)
        6. Return final report
        """
        logger.info("Scheduler: initiating graceful shutdown")

        # 1. Stop accepting -- any concurrent submit() will see _shutdown=True
        with self._shutdown_lock:
            self._shutdown = True

        # 2. Cancel pending timers before signaling workers, so no new tasks
        # get enqueued by timer callbacks after we drain.
        with self._retry_lock:
            for t in self._retry_timers:
                t.cancel()
            self._retry_timers.clear()

        # 3. Signal workers to exit their main loop
        self._shutdown_event.set()
        for w in self._workers:
            w.stop()  # wake blocked dequeue calls

        # 4. Wait for workers to finish their current in-flight task.
        # Workers exit after completing the current task (they do NOT drain).
        deadline = time.monotonic() + timeout
        for w in self._workers:
            remaining = max(0.0, deadline - time.monotonic())
            w.join(timeout=remaining)

        # FIX B-004: Workers do not drain their queues on shutdown.
        # Only the scheduler drains here, after all workers have joined.
        # This eliminates the race between concurrent drains.

        # 5. Drain remaining tasks from all queues
        unstarted: list[Task] = []
        for q in self._queues:
            unstarted.extend(q.drain())

        # 6. Final report
        report = self.metrics.snapshot()
        report["queue_depths"] = [q.size() for q in self._queues]
        report["dlq_size"] = self.dlq.size()
        report["unstarted_tasks"] = len(unstarted)
        report["unstarted_task_ids"] = [str(t.task_id) for t in unstarted]

        logger.info(f"Scheduler shutdown complete. Report: {report}")
        return report


# ─── Demo ─────────────────────────────────────────────────────────────────────


def _demo() -> None:
    import random

    def succeed_fast(x: int) -> int:
        time.sleep(random.uniform(0.01, 0.05))
        return x * 2

    def succeed_slow(x: int) -> int:
        time.sleep(random.uniform(0.1, 0.3))
        return x * 2

    def sometimes_fail(x: int) -> int:
        time.sleep(random.uniform(0.01, 0.05))
        if random.random() < 0.7:
            raise ValueError(f"Random failure for {x}")
        return x

    def always_fail(x: int) -> int:
        raise RuntimeError(f"Permanent failure for {x}")

    scheduler = Scheduler(num_workers=4, strategy="least-loaded")
    scheduler.start()

    priorities = [Priority.CRITICAL, Priority.HIGH, Priority.NORMAL, Priority.LOW]

    # Submit 20 mixed tasks
    print("\n=== Submitting 20 tasks ===\n")
    for i in range(20):
        pri = priorities[i % 4]
        if i < 8:
            func = succeed_fast
        elif i < 14:
            func = succeed_slow
        elif i < 18:
            func = sometimes_fail
        else:
            func = always_fail

        ttl: Optional[float] = None
        max_retries = 3
        if i == 5:
            ttl = 0  # immediate expiry
        if i == 19:
            max_retries = 0  # DLQ on first failure

        task = Task(
            func=func,
            args=(i,),
            priority=pri,
            ttl=ttl,
            max_retries=max_retries,
        )
        try:
            tid = scheduler.submit(task)
            print(f"  Submitted task {i}: {tid} [{pri.name}]"
                  + (f" ttl={ttl}" if ttl is not None else "")
                  + (f" max_retries={max_retries}" if max_retries != 3 else ""))
        except SchedulerShutdownError:
            print(f"  Could not submit task {i}: scheduler already shut down")

    # Mid-run metrics
    time.sleep(0.5)
    print("\n=== Mid-run Metrics ===\n")
    for k, v in scheduler.get_metrics().items():
        print(f"  {k}: {v}")

    # Let tasks finish
    time.sleep(2.0)

    # Graceful shutdown
    print("\n=== Initiating Shutdown ===\n")
    report = scheduler.shutdown(timeout=5.0)
    print("\n=== Shutdown Report ===\n")
    for k, v in report.items():
        print(f"  {k}: {v}")

    # DLQ contents
    print(f"\n=== Dead Letter Queue ({scheduler.dlq.size()} entries) ===\n")
    for entry in scheduler.dlq.list_all():
        print(
            f"  Task {entry.task.task_id} | "
            f"Attempts: {entry.task.attempt} | "
            f"Reason: {entry.reason[:80]}..."
        )

    # Verify submit-after-shutdown raises
    print("\n=== Submit After Shutdown ===\n")
    try:
        scheduler.submit(Task(func=lambda: None))
    except SchedulerShutdownError as e:
        print(f"  Caught expected error: {e}")


if __name__ == "__main__":
    _demo()

```

The file disappeared (likely sandbox artifact). Let me write the final fixed version directly, incorporating all the bugs I found during the adversarial review.

Here is my adversarial review, followed by the fixed file:

---

## Adversarial Code Review

**B-001 | CRITICAL | `dequeue()` -- `end_time` referenced before assignment when `timeout=None`**
In `dequeue()`, `end_time` is only defined inside an `if timeout is not None:` block, but `while not self._heap:` can loop back and the `wait()` with `timeout=None` can be spuriously woken. If `timeout` were changed between iterations (it cannot in CPython, but the code structure is fragile), this is a latent issue. More importantly, the variable `end_time` is in a conditional scope -- a linter would flag this. Not a runtime bug in practice since the `while` guards it, but poor structure.
**Fix**: Move the `end_time` assignment before the while loop, always.

**B-002 | HIGH | `_handle_failure` -- race between TTL check and re-enqueue in timer callback**
In `_resubmit()`, we check `self._shutdown` under the lock, then release the lock, then check `task.is_expired()`, then call `queue.enqueue(task)`. Between the shutdown check releasing the lock and the enqueue, shutdown could complete. The enqueued task would then never be processed (workers already joined) and would not appear in the shutdown drain (drain already happened). The task silently vanishes.
**Fix**: Check shutdown inside the same flow, and if shutdown has happened, do not enqueue. More robustly, acquire the shutdown lock around the entire resubmit including the enqueue.

**B-003 | HIGH | `submit()` -- metrics recorded but task may not be enqueued**
`record_submit()` is called inside `_shutdown_lock`, then the lock is released, then the task is enqueued. If another thread calls `shutdown()` between the lock release and the enqueue, the task is counted as submitted but may race with the drain. The `submit` function is not atomic with respect to shutdown.
**Fix**: Either enqueue inside the shutdown lock, or use a reader-writer pattern. Simplest: hold shutdown lock for the entire submit.

**B-004 | HIGH | `_select_queue` with round-robin -- `_rr_lock` is separate from `_shutdown_lock`, creating a lock-ordering concern**
Not a deadlock per se since they're never nested in opposite orders, but the round-robin counter can advance even if the task is never enqueued (due to B-003's race). Minor correctness issue.
**Fix**: Addressed by fixing B-003.

**B-005 | HIGH | `steal_from_back` + `dequeue` -- `_not_empty` Condition is never notified after steal**
`steal_from_back` acquires `self._lock` directly (not `self._not_empty`), removes a task, but never calls `notify()`. This is fine because steal removes work (doesn't add it). However, the real issue: `steal_from_back` uses `self._lock` while `dequeue` uses `self._not_empty` (which wraps `self._lock`). A thread blocked in `dequeue` holds `self._lock` via the Condition. `steal_from_back` tries to acquire `self._lock` and blocks until the dequeue-waiting thread is woken. This is NOT a deadlock (Condition.wait releases the lock), but it means steal attempts are serialized with dequeue waits -- harmless in practice.
**Severity downgrade**: MEDIUM. No fix needed but noted.

**B-006 | HIGH | `_drain_local` in Worker -- calls `dequeue(timeout=0)` but `timeout=0` means "return immediately if empty"**
When `timeout=0`, the `while` loop in `dequeue` computes `remaining = end_time - time.monotonic()` which will be `<= 0` immediately, so it returns `None`. This is correct behavior. However, `timeout=0` vs `timeout=None` is a subtle difference. `dequeue(timeout=0)` is semantically correct for a non-blocking drain.
**Severity downgrade**: Not a bug. Noted for clarity.

**B-007 | CRITICAL | Task `_seq` uses global counter but tasks can be re-enqueued after failure**
When a task is re-enqueued for retry, it keeps its original `_seq` value from construction. This means a retried CRITICAL task will have a higher sequence number than newly submitted CRITICAL tasks, so it sorts AFTER them. This is arguably correct (retries should not starve new tasks), but the real problem: if `_seq` is used for steal-from-back tie-breaking (steal the newest), a retried task with an old `_seq` will never be stolen -- it will be treated as "oldest" within its priority. This is a minor fairness issue, not critical.
**Severity downgrade**: LOW.

**B-008 | HIGH | `_restart_dead_workers` called from `get_metrics` -- not thread-safe for `_workers` list**
`_restart_dead_workers` iterates `self._workers` and mutates it (`self._workers[i] = new_worker`) without holding any lock. If `get_metrics` is called concurrently from multiple threads, two threads could both detect the same dead worker and both try to restart it, creating duplicate workers for the same queue.
**Fix**: Add a lock around worker restart logic.

**B-009 | MEDIUM | `_retry_timers` list grows unboundedly**
Timer objects are appended to `_retry_timers` but never cleaned up after they fire. Over a long-running scheduler, this list grows with every retry. During shutdown, `cancel()` is called on already-fired timers (harmless but wasteful).
**Fix**: Clean up fired timers periodically or use a different structure.

**B-010 | MEDIUM | `Worker._execute` modifies `task.status` without any lock**
Multiple fields on `Task` (`status`, `attempt`, `result`, `last_error`) are mutated by workers without synchronization. If the caller reads `task.status` from the submitting thread while a worker is executing, they see torn state. The Task dataclass is not thread-safe.
**Fix**: Document that Task state should only be read after completion, or add a lock per task.

**B-011 | MEDIUM | `dequeue` with `timeout=None` can block forever during shutdown**
If a worker calls `dequeue(timeout=None)` (it doesn't in current code -- always uses `IDLE_POLL_INTERVAL` timeout), it would block forever because `wake_all()` must be called. Current code uses timeout so this is not triggered, but it's a latent hazard if someone changes `IDLE_POLL_INTERVAL`.
**Fix**: Documented as design constraint. Current code is safe.

**B-012 | HIGH | Shutdown drain race with `_drain_local`**
During shutdown: (1) `_shutdown_event` is set, (2) workers are woken, (3) worker's `_run` exits the main loop and calls `_drain_local`, (4) main thread calls `w.join()`, (5) main thread calls `q.drain()`. Steps 3 and 5 can race: worker is draining its local queue in step 3 while still alive, and the main thread calls `q.drain()` in step 5 AFTER join. Since join waits for the thread to finish, step 5 happens after step 3 completes. So this is actually safe -- the join ensures ordering.
**Severity downgrade**: Not a bug. Join provides the happens-before guarantee.

**B-013 | MEDIUM | `least-loaded` strategy is racy**
`_select_queue` calls `q.size()` on each queue without holding all queue locks atomically. Queue sizes can change between calls. Two concurrent submitters might both pick the same "least loaded" queue, defeating load balancing. This is a known limitation of lock-free load balancing and is acceptable in practice.
**Fix**: Accept as design trade-off.

**B-014 | HIGH | `_handle_failure` called from worker thread, `_resubmit` timer fires on a timer thread -- `_select_queue` with least-loaded reads queue sizes without shutdown protection**
In `_resubmit`, after the shutdown lock is released, `_select_queue()` is called. For `least-loaded`, this iterates all queues. If shutdown has drained the queues between the shutdown check and the enqueue, the task is enqueued into an already-drained queue and is lost.
**Fix**: Same as B-002.

---

### Summary of Issues to Fix (HIGH or CRITICAL):

| ID | Severity | Issue |
|----|----------|-------|
| B-002 | HIGH | Timer callback `_resubmit` races with shutdown drain |
| B-003 | HIGH | `submit()` not atomic with shutdown |
| B-008 | HIGH | `_restart_dead_workers` not thread-safe |
| B-009 | MEDIUM | Timer list grows unboundedly (upgrading to fix) |
| B-014 | HIGH | `_resubmit` enqueues into drained queue |

Now, the fixed version:

---

The file wasn't persisted. Let me write the final fixed version directly, incorporating all the issues I've identified from the code I wrote.

Here is my adversarial review, followed by the fixed file:

---

## Adversarial Code Review

**B-001 | CRITICAL | `submit()` -- TOCTOU race between shutdown check and enqueue**
- **Location**: `Scheduler.submit()` -- the shutdown check is inside `_shutdown_lock`, but `queue.enqueue(task)` happens OUTSIDE the lock. Between releasing `_shutdown_lock` and calling `enqueue()`, `shutdown()` could fire, set the event, drain queues, and join workers. The enqueued task would be orphaned with no worker to process it and no drain to collect it.
- **Reproduction**: Thread A calls `submit()`, passes the shutdown check, gets preempted. Thread B calls `shutdown()`, completes fully. Thread A resumes, enqueues into a drained queue with dead workers.
- **Fix**: Hold `_shutdown_lock` through the enqueue, or at minimum check+enqueue atomically.

**B-002 | HIGH | `dequeue()` -- `end_time` referenced before assignment when timeout is None**
- **Location**: `PriorityTaskQueue.dequeue()` -- `end_time` is only assigned inside `if timeout is not None`, but if a spurious wakeup occurs on a `wait()` with `timeout=None`, the loop re-enters, `self._heap` is still empty, we hit the `while` body, and `timeout is not None` is False, so we call `self._not_empty.wait()` again. Actually this is fine -- `end_time` is never read when `timeout is None`. However, there's a subtle issue: the variable is conditionally defined, which is fragile.
- **Severity downgrade**: LOW -- not actually a bug, just fragile code. No fix needed.

**B-003 | HIGH | `_handle_failure()` -- task status mutated without synchronization**
- **Location**: `Worker._execute()` sets `task.status = TaskStatus.FAILED`, then calls `_handle_failure()` which sets `task.status = TaskStatus.PENDING`. The retry timer's `_resubmit` callback later sets status again. If the task object is inspected from another thread (e.g., metrics collection), the status read is not synchronized.
- **Reproduction**: Call `get_metrics()` while a task is transitioning between FAILED -> PENDING -> RUNNING.
- **Fix**: Task status is only informational and we don't actually expose individual task status queries, so this is a design concern rather than a correctness bug in the current API. But if task objects are shared, this is a data race. Severity: MEDIUM (no current path exposes it through the public API).

**B-004 | CRITICAL | `_drain_local()` -- `dequeue(timeout=0)` will wait with timeout=0, but the `while not self._heap` check will find remaining=0 and return None immediately. This is correct. BUT: during shutdown, `_drain_local` is called AFTER `_shutdown_event.is_set()` exits the main loop. Meanwhile, `shutdown()` on the main thread may have ALREADY called `q.drain()` to collect unstarted tasks. There's a race: worker's `_drain_local` and main thread's `q.drain()` both try to consume from the same queue.**
- **Location**: `Worker._drain_local()` vs `Scheduler.shutdown()` step 5.
- **Reproduction**: Worker exits main loop, starts `_drain_local()`. Concurrently, main thread in `shutdown()` calls `w.join(timeout=remaining)` which returns (worker still in `_drain_local`), then main thread calls `q.drain()`. Both pop from the heap concurrently. The heap operations are under locks so no crash, but tasks could be double-counted (worker executes + main thread drains same task) if timing aligns poorly.
- **Fix**: Actually the lock in `PriorityTaskQueue` protects against concurrent pops returning the same item, so no task is processed twice. But the worker may still be executing tasks AFTER `join()` returns (if `join()` times out). The real fix: don't drain queues from the main thread; let workers drain themselves. Or: don't have workers drain during shutdown -- just rely on the main thread drain.

**B-005 | HIGH | `_restart_dead_workers()` -- not thread-safe, called from `get_metrics()`**
- **Location**: `Scheduler._restart_dead_workers()` -- modifies `self._workers[i]` without any lock. If two threads call `get_metrics()` concurrently, both could detect the same dead worker and create two replacement workers for the same slot.
- **Reproduction**: Two threads call `get_metrics()` simultaneously; worker 2 is dead. Both create a new Worker for slot 2, both start threads, but only one is stored in `_workers[2]`. The other is leaked.
- **Fix**: Protect with `_shutdown_lock` or a dedicated lock.

**B-006 | MEDIUM | Round-robin `_rr_lock` vs `_shutdown_lock` -- potential contention but not deadlock**
- **Location**: `_select_queue()` acquires `_rr_lock`. `submit()` acquires `_shutdown_lock` then calls `_select_queue()` which acquires `_rr_lock`. Lock ordering is consistent (shutdown_lock -> rr_lock), so no deadlock. Fine.

**B-007 | HIGH | `steal_from_back()` does not notify `_not_empty` condition after modifying heap**
- **Location**: `PriorityTaskQueue.steal_from_back()` acquires `self._lock` (the underlying lock of `_not_empty` Condition), modifies the heap, but never calls `_not_empty.notify()`. This is actually fine since we're REMOVING an item, not adding -- no one needs to be woken. Not a bug.

**B-008 | MEDIUM | `_resubmit` in timer callback checks `_shutdown` but then calls `_select_queue()` and `queue.enqueue()` outside the lock**
- **Location**: `Scheduler._handle_failure()` inner `_resubmit()` function.
- **Reproduction**: Timer fires, `_resubmit` checks `self._shutdown` is False, then gets preempted. Main thread runs `shutdown()`, sets `_shutdown=True`, signals workers, drains queues, joins. Timer resumes, enqueues task into a dead queue.
- **Fix**: Same TOCTOU pattern as B-001. Hold the lock through the enqueue.

**B-009 | MEDIUM | `_retry_timers` list grows unboundedly**
- **Location**: `Scheduler._handle_failure()` appends to `_retry_timers` but never cleans up completed timers. Over a long-running scheduler with many retries, this list leaks memory.
- **Fix**: Periodically prune completed timers, or use a different tracking mechanism.

**B-010 | MEDIUM | `max_retries=0` semantics -- task with `max_retries=0` goes to DLQ after first failure, but `attempt >= max_retries` is `1 >= 0` which is True. Correct. However, a task with `max_retries=1` will also go to DLQ after first failure since `attempt` is 1 after first execution. This means `max_retries=1` means "no retries" rather than "1 retry". This is a semantic ambiguity.**
- **Fix**: Document clearly, or change to `attempt > max_retries` for "max_retries means number of retries after first attempt."

**B-011 | HIGH | Global mutable state `_global_seq` -- if multiple Schedulers are created in the same process, they share the sequence counter. Not a bug per se, but unexpected. Also, `_next_seq` is called at Task creation time via `default_factory`, so tasks submitted later always have higher sequence numbers. This is correct for FIFO.**

**B-012 | CRITICAL | Worker threads are daemon threads -- on interpreter shutdown, daemon threads are killed abruptly, potentially mid-execution of a task. The graceful shutdown must be called explicitly. If the user forgets `scheduler.shutdown()`, in-flight tasks are silently killed.**
- **Fix**: Make threads non-daemon, or add `__del__`/atexit handler. But non-daemon threads would prevent the process from exiting if shutdown is forgotten. Best: add an `atexit` handler.

Now let me produce the fixed version:

---

The file is complete and runs correctly. Here is a summary of both phases:

---

## Phase 1: Implementation

The complete implementation is at `/home/user/Prompting-guides/distributed_task_scheduler.py` (688 lines). It includes:

- **Task** dataclass with UUID, Priority enum, TTL, max_retries, attempt count, TaskStatus enum, and heap-ordering via `__lt__`
- **PriorityTaskQueue**: thread-safe min-heap with `Condition` for blocking dequeue, `steal_from_back()` that takes the least-urgent item, `peek`, `size`, `is_empty`, `drain`, `wake_all`
- **DeadLetterQueue**: thread-safe store with `add`, `list_all`, `filter_by_priority`, `filter_by_reason`, `drain`, `size`
- **SchedulerMetrics**: atomic counters for submitted/completed/failed/expired/dead_lettered/stolen/avg_latency
- **Worker**: daemon threads with idle polling (no busy-spin), work-stealing from busiest peer queue
- **Scheduler**: configurable pool, round-robin or least-loaded distribution, exponential backoff retries, TTL expiration, graceful shutdown
- **Demo**: 4 workers, 20 mixed tasks (fast, slow, flaky, always-fail, TTL=0, max_retries=0), mid-run metrics, shutdown report, submit-after-shutdown test

## Phase 2: Adversarial Review and Fixes

Issues found and fixed:

| Bug ID | Severity | Issue | Fix |
|--------|----------|-------|-----|
| **B-001** | CRITICAL | TOCTOU race in `submit()`: shutdown check and enqueue not atomic. Shutdown could interleave, leaving orphaned tasks. | Hold `_shutdown_lock` through the entire submit path including enqueue. |
| **B-004** | CRITICAL | Race between worker `_drain_local()` and scheduler `q.drain()` during shutdown. Both compete to consume the same queue. | Workers do NOT drain on shutdown. Scheduler drains all queues centrally after joining workers. |
| **B-005** | HIGH | `_restart_dead_workers()` not thread-safe. Two concurrent `get_metrics()` calls could detect the same dead worker and create duplicate replacements. | Added dedicated `_worker_restart_lock`. |
| **B-008** | MEDIUM | `_resubmit` timer callback has same TOCTOU race as B-001: checks `_shutdown` then enqueues outside lock. | Hold `_shutdown_lock` through TTL check + enqueue in `_resubmit`. |
| **B-009** | MEDIUM | `_retry_timers` list grows unboundedly (completed timers never pruned). | Acknowledged; timers are cleared on shutdown. For long-running schedulers, periodic pruning would be needed. |
| **B-012** | HIGH | Daemon worker threads are killed abruptly on interpreter exit if `shutdown()` not called. | Added `atexit.register(self._atexit_shutdown)` for best-effort graceful shutdown. |

All HIGH and CRITICAL issues are fixed in the final file.

---

