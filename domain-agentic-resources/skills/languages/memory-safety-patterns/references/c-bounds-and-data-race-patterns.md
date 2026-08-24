# Memory Safety: C Resource Management, Bounds Checking, and Data Race Prevention

Safe resource management patterns in C (goto cleanup, opaque pointers, cleanup attributes), bounds-checked array access in C++ and Rust, and thread-safe shared state patterns.

## Pattern 4: Safe Resource Management in C

```c
// C doesn't have RAII, but we can use patterns

#include <stdlib.h>
#include <stdio.h>

// Pattern: goto cleanup
int process_file(const char* path) {
    FILE* file = NULL;
    char* buffer = NULL;
    int result = -1;

    file = fopen(path, "r");
    if (!file) {
        goto cleanup;
    }

    buffer = malloc(1024);
    if (!buffer) {
        goto cleanup;
    }

    // Process file...
    result = 0;

cleanup:
    if (buffer) free(buffer);
    if (file) fclose(file);
    return result;
}

// Pattern: Opaque pointer with create/destroy
typedef struct Context Context;

Context* context_create(void);
void context_destroy(Context* ctx);
int context_process(Context* ctx, const char* data);

// Implementation
struct Context {
    int* data;
    size_t size;
    FILE* log;
};

Context* context_create(void) {
    Context* ctx = calloc(1, sizeof(Context));
    if (!ctx) return NULL;

    ctx->data = malloc(100 * sizeof(int));
    if (!ctx->data) {
        free(ctx);
        return NULL;
    }

    ctx->log = fopen("log.txt", "w");
    if (!ctx->log) {
        free(ctx->data);
        free(ctx);
        return NULL;
    }

    return ctx;
}

void context_destroy(Context* ctx) {
    if (ctx) {
        if (ctx->log) fclose(ctx->log);
        if (ctx->data) free(ctx->data);
        free(ctx);
    }
}

// Pattern: Cleanup attribute (GCC/Clang extension)
#define AUTO_FREE __attribute__((cleanup(auto_free_func)))

void auto_free_func(void** ptr) {
    free(*ptr);
}

void auto_free_example(void) {
    AUTO_FREE char* buffer = malloc(1024);
    // buffer automatically freed at end of scope
}
```

## Pattern 5: Bounds Checking

```cpp
// C++: Use containers instead of raw arrays
#include <vector>
#include <array>
#include <span>

void safe_array_access() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // Safe: throws std::out_of_range
    try {
        int val = vec.at(10);
    } catch (const std::out_of_range& e) {
        // Handle error
    }

    // Unsafe but faster (no bounds check)
    int val = vec[2];

    // Modern C++20: std::span for array views
    std::span<int> view(vec);
    // Iterators are bounds-safe
    for (int& x : view) {
        x *= 2;
    }
}

// Fixed-size arrays
void fixed_array() {
    std::array<int, 5> arr = {1, 2, 3, 4, 5};

    // Compile-time size known
    static_assert(arr.size() == 5);

    // Safe access
    int val = arr.at(2);
}
```

```rust
// Rust: Bounds checking by default

fn rust_bounds_checking() {
    let vec = vec![1, 2, 3, 4, 5];

    // Runtime bounds check (panics if out of bounds)
    let val = vec[2];

    // Explicit option (no panic)
    match vec.get(10) {
        Some(val) => println!("Got {}", val),
        None => println!("Index out of bounds"),
    }

    // Iterators (no bounds checking needed)
    for val in &vec {
        println!("{}", val);
    }

    // Slices are bounds-checked
    let slice = &vec[1..3]; // [2, 3]
}
```

## Pattern 6: Preventing Data Races

```cpp
// C++: Thread-safe shared state
#include <mutex>
#include <shared_mutex>
#include <atomic>

class ThreadSafeCounter {
public:
    void increment() {
        // Atomic operations
        count_.fetch_add(1, std::memory_order_relaxed);
    }

    int get() const {
        return count_.load(std::memory_order_relaxed);
    }

private:
    std::atomic<int> count_{0};
};

class ThreadSafeMap {
public:
    void write(const std::string& key, int value) {
        std::unique_lock lock(mutex_);
        data_[key] = value;
    }

    std::optional<int> read(const std::string& key) {
        std::shared_lock lock(mutex_);
        auto it = data_.find(key);
        if (it != data_.end()) {
            return it->second;
        }
        return std::nullopt;
    }

private:
    mutable std::shared_mutex mutex_;
    std::map<std::string, int> data_;
};
```

```rust
// Rust: Data race prevention at compile time

use std::sync::{Arc, Mutex, RwLock};
use std::sync::atomic::{AtomicI32, Ordering};
use std::thread;

// Atomic for simple types
fn atomic_example() {
    let counter = Arc::new(AtomicI32::new(0));

    let handles: Vec<_> = (0..10)
        .map(|_| {
            let counter = Arc::clone(&counter);
            thread::spawn(move || {
                counter.fetch_add(1, Ordering::SeqCst);
            })
        })
        .collect();

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Counter: {}", counter.load(Ordering::SeqCst));
}

// Mutex for complex types
fn mutex_example() {
    let data = Arc::new(Mutex::new(vec![]));

    let handles: Vec<_> = (0..10)
        .map(|i| {
            let data = Arc::clone(&data);
            thread::spawn(move || {
                let mut vec = data.lock().unwrap();
                vec.push(i);
            })
        })
        .collect();

    for handle in handles {
        handle.join().unwrap();
    }
}

// RwLock for read-heavy workloads
fn rwlock_example() {
    let data = Arc::new(RwLock::new(HashMap::new()));

    // Multiple readers OK
    let read_guard = data.read().unwrap();

    // Writer blocks readers
    let write_guard = data.write().unwrap();
}
```
