---
title: "GUI Architecture for Long-Running Background Computation"
category: code-analysis/architecture
description: "Review threading, state management, progress reporting, and cancellation patterns in desktop GUI applications that run long computations"
tags:
  - architecture
  - gui
  - threading
  - pyside6
  - qt
  - background-tasks
  - state-management
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DS-01  # Framework Application
  - DS-03  # Tool and Methodology Suggestions
  - CM-02  # Constraint Specification
  - QA-02  # Adversarial Stress-Test
difficulty: intermediate
version: "1.0"
updated: 2026-03-04
related_prompts:
  - architecture_coupling_cohesion_analysis.md
  - performance_concurrency_synchronization_analysis.md
---

# GUI Architecture for Long-Running Background Computation

**Objective:** Review the architecture of a desktop GUI application that runs long computations (seconds to minutes) in the background, verifying thread safety, UI responsiveness, progress reporting, cancellation correctness, and error propagation between worker and UI threads.

**When to Use:** Use this prompt when a PySide6/PyQt, Tkinter, or other desktop GUI application performs computation that could take more than 1-2 seconds (schedule generation, optimization, data processing). The core concern is: the UI must remain responsive while computation runs, and the two threads must communicate safely.

**Instructions:**

1. **Thread Architecture Audit**

   Identify how background computation is implemented:

   | Pattern | How It Works | Thread Safety | PySide6 Support |
   |---------|-------------|---------------|-----------------|
   | **QThread subclass** | Override `run()` | Manual signal/slot | Native |
   | **QThread + moveToThread** | Move worker object to thread | Signal/slot based | Native, preferred |
   | **QRunnable + QThreadPool** | Submit callable to pool | No direct signals | Good for short tasks |
   | **concurrent.futures** | Python thread/process pool | Requires invokeMethod for UI | Works but not Qt-native |
   | **asyncio + qasync** | Async/await in Qt event loop | Single-threaded async | Complex setup |
   | **multiprocessing** | Separate process | Requires IPC | Best for CPU-bound, complex |

   **Verify:**
   - Is the computation on a separate thread or blocking the main thread?
   - Are ALL widget updates happening on the main thread?
   - Is any widget method called directly from the worker thread? (This is a crash-inducing bug in Qt)

   ```python
   # CORRECT: Worker emits signal, main thread updates UI
   class ScheduleWorker(QObject):
       progress = Signal(int)
       finished = Signal(list)
       error = Signal(str)

       def run(self):
           for i, variant in enumerate(generate_variants()):
               self.progress.emit(i)  # Signal is thread-safe
           self.finished.emit(variants)

   # DANGEROUS: Worker directly updates widget
   class ScheduleWorker(QThread):
       def run(self):
           self.parent().progress_bar.setValue(50)  # CRASH: cross-thread widget access
   ```

2. **Shared State Identification**

   Map all data accessed by both the worker and main thread:

   | Data | Written By | Read By | Protection |
   |------|-----------|---------|------------|
   | Configuration | Main (before launch) | Worker | Pass as immutable snapshot |
   | Roster data | Main (before launch) | Worker | Deep copy at launch time |
   | Progress counter | Worker | Main (via signal) | Signal is atomic |
   | Result variants | Worker (during computation) | Main (after finished) | Pass via signal |
   | Cancel flag | Main | Worker | Use `QAtomicInt` or `threading.Event` |

   **Verify:**
   - Is the configuration deep-copied or frozen before the worker starts?
   - Can the user modify config fields while computation runs? If so, does the running computation see the old or new values?
   - Is the result data safely transferred from worker to main thread (not a shared mutable reference)?

3. **GUI State Machine**

   Define the expected states and transitions:

   ```
   GUI States:
   ┌─────────┐   Generate    ┌───────────┐
   │  IDLE   │──────────────→│ COMPUTING │
   │         │               │           │
   │ [Generate]              │ [Cancel]  │
   │ [Config ✓]              │ [Config ✗]│
   └─────────┘               └─────┬─────┘
        ↑                          │
        │         ┌────────────────┤
        │         ↓                ↓
   ┌─────────┐   Cancel    ┌───────────┐
   │ RESULTS │←────────────│ CANCELLING│
   │ READY   │             │           │
   │         │             │ [wait...] │
   │ [Export] │             └───────────┘
   │ [New Gen]│    Error
   └─────────┘←────────────── COMPUTING
   ```

   **For each state, verify:**
   - Which buttons/menus are enabled/disabled?
   - Can the user queue a second job while one is running?
   - Does the state machine handle rapid state transitions? (Click Generate, immediately click Cancel)

4. **Cancellation Correctness**

   ```python
   # Cooperative cancellation pattern
   class ScheduleWorker(QObject):
       def __init__(self):
           self._cancel_requested = threading.Event()

       def cancel(self):
           self._cancel_requested.set()

       def run(self):
           for day in schedule_days:
               if self._cancel_requested.is_set():
                   self.cancelled.emit()
                   return  # Clean exit
               self.assign_day(day)
   ```

   **Verify:**
   - Is cancellation cooperative (worker checks flag) or forced (thread.terminate)?
   - How frequently does the worker check the cancel flag? (Once per day? Once per constraint check?)
   - After cancel, is the partial state cleaned up? (No half-written database records)
   - Is the cancel flag reset before the next computation starts?

5. **Error Propagation**

   **When the worker raises an exception:**

   | Behavior | Correct? | User Experience |
   |----------|----------|-----------------|
   | Exception caught, emitted via error signal | Yes | User sees error dialog |
   | Exception logged, worker silently stops | Partial | User sees "nothing happened" |
   | Exception propagates, crashes thread | No | App may hang or crash |
   | Exception caught, generic "error occurred" | Partial | User can't diagnose |

   **Verify:**
   - Does the worker's `run()` method have a top-level try/except?
   - Is the exception message (not just type) forwarded to the UI?
   - Does the GUI return to IDLE state on error?
   - Are infeasibility results (no valid schedule possible) reported as a distinct state, not an error?

6. **Progress Reporting**

   **Assess progress granularity:**

   | Granularity | Signal Frequency | User Experience |
   |-------------|-----------------|-----------------|
   | Per-variant | Every 5-30 seconds | Coarse but useful |
   | Per-day assigned | Every 0.1-1 second | Good feedback |
   | Per-constraint check | Every millisecond | Saturates event loop |
   | Indeterminate spinner | Once at start | Minimal feedback |

   **Verify:**
   - Is progress expressed as a percentage, count, or just "working"?
   - Can the user estimate remaining time from the progress indicator?
   - Is the signal emission rate throttled to avoid flooding the Qt event loop?

7. **PySide6 Anti-Pattern Checklist**

   - [ ] No direct widget manipulation from non-main thread
   - [ ] No lambda captures of mutable widget state in signal connections
   - [ ] Worker objects use `deleteLater()` for cleanup
   - [ ] No blocking `exec()` or `sleep()` in the main thread
   - [ ] `QThread.quit()` and `QThread.wait()` called on application exit
   - [ ] No `QThread.terminate()` usage (causes resource leaks)
   - [ ] Signal connections are disconnected or worker is destroyed after use

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag `QThread` subclassing as "always wrong" — it's acceptable for simple cases, just less flexible than `moveToThread`
- Recommend `asyncio` as universally better than threading for Qt — asyncio integration with Qt is complex and not always worth it
- Flag the absence of multiprocessing as an issue — threading is simpler and sufficient unless the computation is truly CPU-bound and benefits from multiple cores
- Report "no progress bar" as critical if the computation typically takes under 3 seconds

✅ **DO:**
- Check for the #1 Qt threading bug: updating widgets from a non-main thread
- Verify that the cancel mechanism actually works (is the flag checked frequently enough?)
- Test the rapid-fire case: start computation, cancel immediately, start again
- Confirm that error state properly resets the UI to a usable state

## Expected Output

1. **Thread Architecture Assessment** — Pattern used, correctness of thread boundary
2. **Shared State Map** — All data crossing the thread boundary with protection mechanism
3. **State Machine Verification** — States, transitions, button enable/disable correctness
4. **Cancellation Audit** — Mechanism, check frequency, cleanup correctness
5. **Error Handling Report** — How exceptions propagate, user experience on failure
6. **Progress Assessment** — Granularity, throttling, user experience
7. **Anti-Pattern Findings** — Checklist results with code references

## Quality Checklist

- [ ] All cross-thread widget access is via signals (not direct calls)
- [ ] Cancel mechanism is tested and responsive
- [ ] Error propagation verified (worker exception → UI error display)
- [ ] GUI state machine transitions are all accounted for
- [ ] Anti-pattern checklist is complete

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focuses review on GUI + background computation architecture
- **ST-02** (Structured Sequential Instructions) — Systematic review from threading to error handling
- **RT-02** (Multi-Dimensional Analysis) — Covers threading, state, cancellation, errors, progress
- **DS-01** (Framework Application) — Applies Qt threading patterns (QThread, signals/slots)
- **DS-03** (Tool and Methodology Suggestions) — PySide6-specific patterns and tools
- **CM-02** (Constraint Specification) — Defines what must/must-not happen across thread boundary
- **QA-02** (Adversarial Stress-Test) — Tests rapid cancel, concurrent jobs, error cases

## Related Prompts

- `architecture_coupling_cohesion_analysis.md` — Coupling between UI and computation layers
- `performance_concurrency_synchronization_analysis.md` — Concurrency issues in the threading model
- `algorithms_constraint_satisfaction_scheduling.md` — The computation being run in the background

## Customization Guide

**For PySide6/PyQt applications:**
- Use `QThread` + `moveToThread` pattern for signal-based communication
- Use `Signal`/`Slot` (not `pyqtSignal` if using PySide6) for type-safe cross-thread communication

**For Tkinter applications:**
- Use `threading.Thread` + `queue.Queue` for cross-thread communication
- Use `root.after()` to poll the queue from the main thread
- No native signal mechanism — must implement polling pattern

**For Electron/web-based desktop apps:**
- Use Web Workers or Node.js `worker_threads` for background computation
- Use `postMessage` for cross-thread communication
- Progress and cancellation patterns are similar but use different APIs
