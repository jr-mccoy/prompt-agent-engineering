# Debugging Strategies — Advanced Techniques and Language-Specific Tools

## Python Debugging

```python
# Built-in debugger (pdb)
import pdb

def calculate_total(items):
    total = 0
    pdb.set_trace()  # Debugger starts here

    for item in items:
        total += item.price * item.quantity

    return total

# Breakpoint (Python 3.7+)
def process_order(order):
    breakpoint()  # More convenient than pdb.set_trace()
    # ... code

# Post-mortem debugging
try:
    risky_operation()
except Exception:
    import pdb
    pdb.post_mortem()  # Debug at exception point

# IPython debugging (ipdb)
from ipdb import set_trace
set_trace()  # Better interface than pdb

# Logging for debugging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def fetch_user(user_id):
    logger.debug(f'Fetching user: {user_id}')
    user = db.query(User).get(user_id)
    logger.debug(f'Found user: {user}')
    return user

# Profile performance
import cProfile
import pstats

cProfile.run('slow_function()', 'profile_stats')
stats = pstats.Stats('profile_stats')
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 slowest
```

---

## Go Debugging

```go
// Delve debugger
// Install: go install github.com/go-delve/delve/cmd/dlv@latest
// Run: dlv debug main.go

import (
    "fmt"
    "runtime"
    "runtime/debug"
)

// Print stack trace
func debugStack() {
    debug.PrintStack()
}

// Panic recovery with debugging
func processRequest() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Panic:", r)
            debug.PrintStack()
        }
    }()

    // ... code that might panic
}

// Memory profiling
import _ "net/http/pprof"
// Visit http://localhost:6060/debug/pprof/

// CPU profiling
import (
    "os"
    "runtime/pprof"
)

f, _ := os.Create("cpu.prof")
pprof.StartCPUProfile(f)
defer pprof.StopCPUProfile()
// ... code to profile
```

---

## Advanced Debugging Techniques

### Technique 1: Binary Search Debugging

```bash
# Git bisect for finding regression
git bisect start
git bisect bad                    # Current commit is bad
git bisect good v1.0.0            # v1.0.0 was good

# Git checks out middle commit
# Test it, then:
git bisect good   # if it works
git bisect bad    # if it's broken

# Continue until bug found
git bisect reset  # when done
```

### Technique 2: Differential Debugging

Compare working vs broken:

```markdown
## What's Different?

| Aspect       | Working         | Broken          |
|--------------|-----------------|-----------------|
| Environment  | Development     | Production      |
| Node version | 18.16.0         | 18.15.0         |
| Data         | Empty DB        | 1M records      |
| User         | Admin           | Regular user    |
| Browser      | Chrome          | Safari          |
| Time         | During day      | After midnight  |

Hypothesis: Time-based issue? Check timezone handling.
```

### Technique 3: Trace Debugging

```typescript
// Function call tracing
function trace(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;

    descriptor.value = function(...args: any[]) {
        console.log(`Calling ${propertyKey} with args:`, args);
        const result = originalMethod.apply(this, args);
        console.log(`${propertyKey} returned:`, result);
        return result;
    };

    return descriptor;
}

class OrderService {
    @trace
    calculateTotal(items: Item[]): number {
        return items.reduce((sum, item) => sum + item.price, 0);
    }
}
```

### Technique 4: Memory Leak Detection

```typescript
// Chrome DevTools Memory Profiler
// 1. Take heap snapshot
// 2. Perform action
// 3. Take another snapshot
// 4. Compare snapshots

// Node.js memory debugging
if (process.memoryUsage().heapUsed > 500 * 1024 * 1024) {
    console.warn('High memory usage:', process.memoryUsage());

    // Generate heap dump
    require('v8').writeHeapSnapshot();
}

// Find memory leaks in tests
let beforeMemory: number;

beforeEach(() => {
    beforeMemory = process.memoryUsage().heapUsed;
});

afterEach(() => {
    const afterMemory = process.memoryUsage().heapUsed;
    const diff = afterMemory - beforeMemory;

    if (diff > 10 * 1024 * 1024) {  // 10MB threshold
        console.warn(`Possible memory leak: ${diff / 1024 / 1024}MB`);
    }
});
```

---

## Debugging Patterns by Issue Type

### Pattern 1: Intermittent Bugs

```markdown
## Strategies for Flaky Bugs

1. **Add extensive logging**
   - Log timing information
   - Log all state transitions
   - Log external interactions

2. **Look for race conditions**
   - Concurrent access to shared state
   - Async operations completing out of order
   - Missing synchronization

3. **Check timing dependencies**
   - setTimeout/setInterval
   - Promise resolution order
   - Animation frame timing

4. **Stress test**
   - Run many times
   - Vary timing
   - Simulate load
```

### Pattern 2: Performance Issues

```markdown
## Performance Debugging

1. **Profile first**
   - Don't optimize blindly
   - Measure before and after
   - Find bottlenecks

2. **Common culprits**
   - N+1 queries
   - Unnecessary re-renders
   - Large data processing
   - Synchronous I/O

3. **Tools**
   - Browser DevTools Performance tab
   - Lighthouse
   - Python: cProfile, line_profiler
   - Node: clinic.js, 0x
```

### Pattern 3: Production Bugs

```markdown
## Production Debugging

1. **Gather evidence**
   - Error tracking (Sentry, Bugsnag)
   - Application logs
   - User reports
   - Metrics/monitoring

2. **Reproduce locally**
   - Use production data (anonymized)
   - Match environment
   - Follow exact steps

3. **Safe investigation**
   - Don't change production
   - Use feature flags
   - Add monitoring/logging
   - Test fixes in staging
```
