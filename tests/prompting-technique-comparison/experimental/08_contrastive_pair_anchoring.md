# Experimental Technique #8: Contrastive Pair Anchoring

> **Hypothesis:** Showing a bad/good pair for a DIFFERENT problem calibrates quality better than instructions alone.

## Prompt (Single Turn)

```
Before the main task, study this contrastive pair carefully.

## BAD Implementation — Thread-Safe Counter (DO NOT COPY)

```python
import threading

class BadCounter:
    def __init__(self):
        self.count = 0
        self.history = []
    
    def increment(self):
        # BUG: race condition - read/modify/write without lock
        current = self.count
        self.count = current + 1
        self.history.append(self.count)  # BUG: list append not atomic with count update
    
    def get_count(self):
        return self.count  # BUG: may read stale value
    
    def reset(self):
        self.count = 0  # BUG: no lock, concurrent increment will corrupt
        self.history.clear()  # BUG: separate operation, not atomic with count reset

class BadWorkerPool:
    def __init__(self, num_workers):
        self.workers = []
        self.running = True  # BUG: boolean assignment isn't enough for visibility
        
    def stop(self):
        self.running = False  # BUG: workers may not see this immediately
        for w in self.workers:
            w.join()  # BUG: no timeout, could hang forever
            # BUG: no handling if join() raises
```

## GOOD Implementation — Thread-Safe Counter

```python
import threading
from typing import List

class GoodCounter:
    def __init__(self):
        self._lock = threading.Lock()
        self._count: int = 0
        self._history: List[int] = []
    
    def increment(self) -> int:
        with self._lock:  # GOOD: single lock protects entire read-modify-write
            self._count += 1
            self._history.append(self._count)  # GOOD: atomic with count update
            return self._count
    
    def get_count(self) -> int:
        with self._lock:  # GOOD: consistent read under lock
            return self._count
    
    def reset(self) -> None:
        with self._lock:  # GOOD: atomic reset of both fields
            self._count = 0
            self._history.clear()

class GoodWorkerPool:
    def __init__(self, num_workers: int):
        self._workers: List[threading.Thread] = []
        self._shutdown_event = threading.Event()  # GOOD: Event for cross-thread signaling
        
    def stop(self, timeout: float = 30.0) -> None:
        self._shutdown_event.set()  # GOOD: Event.set() is immediately visible to all threads
        deadline = time.monotonic() + timeout
        for w in self._workers:
            remaining = max(0, deadline - time.monotonic())
            w.join(timeout=remaining)  # GOOD: bounded wait
            if w.is_alive():
                logging.warning(f"Worker {w.name} did not stop within timeout")
```

## The Key Differences:
1. **Lock discipline**: Every shared field protected by a single lock, not scattered
2. **Atomic operations**: Related state changes happen under the same lock acquisition
3. **Cross-thread signaling**: Use `threading.Event` not bare booleans
4. **Bounded waits**: Never `join()` without timeout
5. **Graceful degradation**: Log warnings instead of crashing on timeout

---

## Now: Your Actual Task

With the same level of rigor as the GOOD example above, implement:

[Paste TASK_DEFINITION.md here]

Apply every principle demonstrated in the GOOD example. Wherever you have shared 
mutable state, it should look like the GOOD counter, not the BAD one. Wherever 
you have thread lifecycle management, it should look like the GOOD worker pool.
```

## What This Tests

- Does the contrastive pair calibrate quality for a different (more complex) task?
- Does the model internalize the delta (not just copy the pattern)?
- Compare against: established technique RT-05 (Evidence-Based Reasoning) which provides evidence but not contrastive examples
